#!/usr/bin/env python3
"""Stage 1-5 -- fetch, log, clean, deduplicate and archive the VPN Gate list.

Source: the public VPN Gate CSV API (https://www.vpngate.net/api/iphone/).
The payload starts with a ``*vpn_servers`` marker line, has a ``#``-prefixed
header line, and ends with a ``*`` marker line -- all handled by common.py.

Outputs (under --data-dir):
  raw/latest.csv      untouched API response (gitignored; input for the tester)
  servers_clean.csv   cleaned + deduplicated server list (no bulky base64 blob)
  last_fetch.json     fetch metadata: counts, timings, sha256, dedupe stats

Under --archive-dir:
  vpngate_YYYYMMDD_HHMMSS.csv.gz   immutable snapshot, auto-pruned to
                                   --keep-archive newest files
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def plog(msg):
    print(f"[fetch] {msg}", flush=True)


def looks_like_vpngate_csv(body: bytes) -> bool:
    head = body[:512].lstrip().lower()
    return head.startswith(b"*vpn_servers") or b"#hostname," in head


def try_fetch(timeout: int):
    """Try every known endpoint; return the first response that is real CSV."""
    sess = requests.Session()
    sess.headers.update({"User-Agent": common.USER_AGENT, "Accept": "*/*"})
    retry = requests.adapters.Retry(
        total=3, backoff_factor=10,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    sess.mount("http://", adapter)
    sess.mount("https://", adapter)

    last_err = "no endpoint attempted"
    for url in common.ENDPOINTS:
        t0 = time.monotonic()
        try:
            r = sess.get(url, timeout=timeout)
            dur = time.monotonic() - t0
            body = r.content or b""
            ok = r.status_code == 200 and looks_like_vpngate_csv(body)
            plog(f"GET {url} -> HTTP {r.status_code}, {len(body):,} bytes "
                 f"in {dur:.1f}s, looks_like_csv={ok}")
            if ok:
                return url, r.status_code, body, dur
            last_err = (f"{url}: HTTP {r.status_code}, {len(body):,} bytes "
                        f"but not VPN Gate CSV (blocked or placeholder page)")
        except Exception as e:  # noqa: BLE001
            last_err = f"{url}: {type(e).__name__}: {e}"
            plog(f"GET {url} -> FAILED {last_err}")
    return None, None, None, last_err


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--archive-dir", default="archive")
    ap.add_argument("--min-rows", type=int, default=common.DEFAULTS["min_rows"])
    ap.add_argument("--keep-archive", type=int, default=common.DEFAULTS["keep_archive"])
    ap.add_argument("--timeout", type=int, default=60)
    args = ap.parse_args()

    os.makedirs(os.path.join(args.data_dir, "raw"), exist_ok=True)
    os.makedirs(args.archive_dir, exist_ok=True)
    t_start = time.monotonic()

    # ---- stage 1: fetch (with endpoint fallback + retries) ----------------
    url, status, raw, dur = try_fetch(args.timeout)
    if raw is None:
        plog(f"FATAL could not fetch a valid CSV from any endpoint: {dur}")
        return 2
    sha = hashlib.sha256(raw).hexdigest()

    # ---- stage 2: log / persist raw ---------------------------------------
    raw_path = os.path.join(args.data_dir, "raw", "latest.csv")
    common.atomic_write(raw_path, raw)
    plog(f"raw response archived -> {raw_path} ({len(raw):,} bytes, sha256 {sha[:16]}...)")

    # ---- stage 3: clean ----------------------------------------------------
    header, rows, malformed = common.parse_vpngate_csv(raw.decode("utf-8-sig", "replace"))
    plog(f"parsed: rows={len(rows):,} malformed={malformed} header_cols={len(header)}")
    cleaned, bad = [], 0
    for row in rows:
        c = common.clean_row(row)
        if c:
            cleaned.append(c)
        else:
            bad += 1
    plog(f"clean: kept={len(cleaned):,} dropped_invalid={bad} "
         f"(bad ip / missing hostname / bad numbers)")

    # ---- stage 4: dedupe ---------------------------------------------------
    kept, exact, same_ip = common.dedupe(cleaned)
    plog(f"dedupe: unique={len(kept):,} removed_exact={exact} removed_same_ip={same_ip}")

    if len(kept) < args.min_rows:
        plog(f"FATAL only {len(kept)} valid servers (< {args.min_rows}); "
             f"refusing to overwrite good data with a broken fetch")
        return 2

    # ---- outputs ------------------------------------------------------------
    csv_path = os.path.join(args.data_dir, "servers_clean.csv")
    common.write_public_csv(csv_path, kept)
    plog(f"wrote {csv_path} ({len(kept):,} rows, base64 config column excluded)")

    meta = {
        "fetched_at": common.now_iso(),
        "source": url,
        "http_status": status,
        "raw_bytes": len(raw),
        "sha256": sha,
        "duration_s": round(dur, 2),
        "rows_parsed": len(rows),
        "rows_malformed": malformed,
        "rows_cleaned": len(cleaned),
        "rows_dropped_invalid": bad,
        "removed_exact_duplicates": exact,
        "removed_same_ip_duplicates": same_ip,
        "unique_servers": len(kept),
    }
    common.write_json(os.path.join(args.data_dir, "last_fetch.json"), meta)

    # ---- stage 5: archive ----------------------------------------------------
    arch = os.path.join(args.archive_dir, f"vpngate_{common.stamp()}.csv.gz")
    common.write_public_csv_gz(arch, kept)
    removed = common.prune_archive(args.archive_dir, args.keep_archive)
    plog(f"archived snapshot -> {arch} (pruned {removed} old snapshots, "
         f"keep={args.keep_archive})")

    plog(f"DONE in {time.monotonic() - t_start:.1f}s: {len(kept):,} unique clean servers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
