"""Shared constants and helpers for the VPN Gate monitor pipeline.

Pipeline layout:

  fetch.py     -- stage 1-5: fetch the VPN Gate CSV API, log, clean, dedupe, archive
  test_vpns.py -- stage 6:  open a REAL OpenVPN tunnel to every listed server,
                            verify traffic egress, geo and throughput
  report.py    -- stage 7:  render README.md (the living report), badges, history

This module intentionally uses the Python standard library only, so that
test_vpns.py can run as root (required to create tun devices) with the system
interpreter and no pip packages.
"""
from __future__ import annotations

import base64
import csv
import gzip
import io
import json
import os
import re
import socket
from datetime import datetime, timezone

# ----------------------------------------------------------------- constants

API_URL = "https://www.vpngate.net/api/iphone/"

# Ordered endpoint candidates. VPN Gate sometimes answers datacenter IP ranges
# with an empty HTML placeholder page instead of the CSV; every response is
# therefore validated and we fall through to the next candidate.
ENDPOINTS = [
    "https://www.vpngate.net/api/iphone/",
    "http://www.vpngate.net/api/iphone/",
    "http://api.vpngate.jp/api/iphone/",
]

USER_AGENT = (
    "Mozilla/5.0 (compatible; vpngate-monitor/1.0; "
    "+https://github.com/g1010yzd10/vpngate-monitor) automated-6-hourly-check"
)

CSV_FIELDS = [
    "HostName", "IP", "Score", "Ping", "Speed", "CountryLong", "CountryShort",
    "NumVpnSessions", "Uptime", "TotalUsers", "TotalTraffic", "LogType",
    "Operator", "Message", "OpenVPN_ConfigData_Base64",
]
INT_FIELDS = {
    "Score", "Ping", "Speed", "NumVpnSessions", "Uptime",
    "TotalUsers", "TotalTraffic",
}
PUBLIC_FIELDS = [f for f in CSV_FIELDS if f != "OpenVPN_ConfigData_Base64"]

DEFAULTS = {
    "connect_timeout": 25,     # s: wait for "Initialization Sequence Completed"
    "trace_timeout": 10,       # s: exit-IP verification request
    "speed_bytes": 5_000_000,  # bytes pulled through the tunnel for throughput
    "speed_timeout": 22,       # s: throughput budget
    "workers": 48,             # parallel isolated tunnels
    "keep_archive": 360,       # csv.gz snapshots kept in archive/
    "min_rows": 100,           # refuse to replace good data with anything smaller
    "history_cap": 2000,       # max lines kept in data/history.jsonl
}

# ---------------------------------------------------------------------- time


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def now_iso() -> str:
    return utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def stamp() -> str:
    return utcnow().strftime("%Y%m%d_%H%M%S")


def iso_to_human(iso: str) -> str:
    return (iso or "").replace("T", " ").replace("Z", " UTC")


# ------------------------------------------------------------------- parsing


def parse_vpngate_csv(text: str):
    """Parse the VPN Gate "iphone" CSV format.

    The payload looks like::

        *vpn_servers
        #HostName,IP,Score,Ping,Speed,...,OpenVPN_ConfigData_Base64
        public-vpn-108,219.100.37.98,3037443,...
        *

    Returns (header, rows, malformed_count). Marker lines (``*vpn_servers``
    and the trailing ``*``) and the ``#``-prefixed header line are handled.
    """
    header, rows, malformed = None, [], 0
    for r in csv.reader(io.StringIO(text)):
        if not r:
            continue
        first = (r[0] or "").strip()
        if first.startswith("*"):
            continue
        if first.startswith("#") or first.lower().startswith("hostname"):
            if header is None:
                header = [c.strip().lstrip("#").strip() for c in r]
            continue
        if len(r) == len(CSV_FIELDS):
            rows.append([c.strip() for c in r])
        else:
            malformed += 1
    if header is None:
        header = list(CSV_FIELDS)
    return header, rows, malformed


def valid_ipv4(s: str) -> bool:
    try:
        socket.inet_aton(s)
        parts = s.split(".")
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    except (OSError, ValueError):
        return False


def clean_row(row):
    """Type-check and normalise one CSV row. Returns a dict or None."""
    if len(row) != len(CSV_FIELDS):
        return None
    d = dict(zip(CSV_FIELDS, row))
    host = (d.get("HostName") or "").strip()
    ip = (d.get("IP") or "").strip()
    if not host or not valid_ipv4(ip):
        return None
    try:
        for f in INT_FIELDS:
            d[f] = int(d.get(f) or 0)
    except ValueError:
        return None
    for f in ("CountryLong", "CountryShort", "LogType", "Operator", "Message"):
        d[f] = (d.get(f) or "").strip().strip('"').strip()
    b64 = re.sub(r"\s+", "", d.get("OpenVPN_ConfigData_Base64") or "")
    try:
        ok = bool(base64.b64decode(b64, validate=False)) if b64 else False
    except Exception:
        ok = False
    d["OpenVPN_ConfigData_Base64"] = b64
    d["_config_ok"] = ok
    return d


def dedupe(servers):
    """Remove duplicates: identical (HostName, IP) pairs first, then any other
    row sharing the same IP (keeping the highest-scored entry).

    Returns (kept, removed_exact, removed_same_ip).
    """
    seen_pair, seen_ip, kept = set(), set(), []
    exact = same_ip = 0
    for s in sorted(servers, key=lambda x: (-x.get("Score", 0), x["HostName"], x["IP"])):
        pair = (s["HostName"], s["IP"])
        if pair in seen_pair:
            exact += 1
            continue
        if s["IP"] in seen_ip:
            same_ip += 1
            continue
        seen_pair.add(pair)
        seen_ip.add(s["IP"])
        kept.append(s)
    return kept, exact, same_ip


# ------------------------------------------------------------------- io


def atomic_write(path: str, data: bytes):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


def write_json(path: str, obj):
    atomic_write(path, (json.dumps(obj, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


def _public_rows(servers):
    return [[str(s.get(f, "")) for f in PUBLIC_FIELDS] for s in servers]


def write_public_csv(path: str, servers):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(PUBLIC_FIELDS)
        w.writerows(_public_rows(servers))
    os.replace(tmp, path)


def write_public_csv_gz(path: str, servers):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", newline="", encoding="utf-8", compresslevel=9) as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(PUBLIC_FIELDS)
        w.writerows(_public_rows(servers))
    os.replace(tmp, path)


def prune_archive(directory: str, keep: int) -> int:
    """Delete oldest snapshots beyond `keep`. Returns number removed."""
    if not os.path.isdir(directory):
        return 0
    files = sorted(f for f in os.listdir(directory)
                   if f.startswith("vpngate_") and f.endswith(".csv.gz"))
    removed = 0
    for f in files[: max(0, len(files) - keep)]:
        try:
            os.remove(os.path.join(directory, f))
            removed += 1
        except OSError:
            pass
    return removed


def read_history(path: str, cap: int):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return out[-cap:]


def write_history(path: str, entries):
    atomic_write(
        path,
        ("\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n").encode("utf-8"),
    )


# -------------------------------------------------------------- formatting


def mbps(bps):
    try:
        return f"{float(bps) / 1_000_000:,.1f}"
    except (TypeError, ValueError):
        return "?"


def fmt_bytes(n):
    n = float(n or 0)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if n < 1000 or unit == "PB":
            return f"{n:,.0f} {unit}" if unit == "B" else f"{n:,.1f} {unit}"
        n /= 1000


def fmt_uptime(ms):
    ms = ms or 0
    days = ms / 86_400_000
    if days >= 1:
        return f"{days:,.1f} d"
    return f"{ms / 3_600_000:,.1f} h"


def country_flag(code: str) -> str:
    code = (code or "").strip().upper()
    if len(code) == 2 and code.isalpha() and code.isascii():
        return "".join(chr(0x1F1E6 + ord(c) - 65) for c in code)
    return "🏳"


def spark(series):
    """Tiny unicode sparkline for a list of numbers."""
    blocks = "▁▂▃▄▅▆▇█"
    vals = [v for v in series if v is not None]
    if not vals:
        return ""
    lo, hi = min(vals), max(vals)
    if hi == lo:
        return "▄" * len(vals)
    return "".join(blocks[min(7, int(8 * (v - lo) / (hi - lo)))] for v in vals)


# ------------------------------------------------------------- test infra


def worker_tun(w: int) -> str:
    """Deterministic tun device name for worker slot w (tun100..tun299)."""
    return f"tun{100 + w}"


def worker_cf_ips(w: int):
    """Two per-worker anycast Cloudflare destination IPs.

    We deliberately spread workers across *distinct* Cloudflare edge IPs in
    104.16.0.0/13 so that the /32 host routes of parallel tunnels never
    collide. Any address in that range terminates TLS for any
    Cloudflare-fronted hostname (routing happens by SNI), which lets us pin
    both the exit-IP trace and the throughput download to the same address
    without any DNS lookup through the VPN.
    """
    return (f"104.16.{w % 256}.{4 + w // 256}", f"104.17.{w % 256}.{4 + w // 256}")
