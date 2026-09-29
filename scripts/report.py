#!/usr/bin/env python3
"""Stage 7 -- render README.md (the living report), badges, history.

Reads (under --data-dir):
  last_fetch.json   stage 1-5 metadata (required for a full report)
  results.json      stage 6 real VPN test output (optional -> "pending" mode)
  history.jsonl     append-only per-run summary

Writes:
  README.md                       the full auto-generated report
  badges/*.json                   shields.io endpoint badges
  data/latest.json                merged dataset (cleaned fields + test results)
  data/summary.json               compact run summary incl. error breakdown
  data/history.jsonl              updated (idempotent per fetch)

Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

REPO_DEFAULT = "g1010yzd10/vpngate-monitor"


def plog(msg):
    print(f"[report] {msg}", flush=True)


def esc(v):
    """Escape a value for a markdown table cell."""
    return str(v if v is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def trunc(v, n=42):
    v = str(v or "")
    return v if len(v) <= n else v[: n - 1] + "…"


def read_json(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        plog(f"WARN could not read {path}: {e}")
        return None


def read_servers_csv(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            for k in common.INT_FIELDS:
                try:
                    row[k] = int(row.get(k) or 0)
                except (TypeError, ValueError):
                    row[k] = 0
            out.append(row)
    return out


def median(vals):
    v = sorted(vals)
    return v[len(v) // 2] if v else None


def speed_color(mbps):
    if mbps is None:
        return "lightgrey"
    if mbps >= 100:
        return "brightgreen"
    if mbps >= 30:
        return "green"
    if mbps >= 10:
        return "yellowgreen"
    if mbps >= 3:
        return "orange"
    return "red"


def alive_color(pct):
    if pct is None:
        return "lightgrey"
    if pct >= 60:
        return "brightgreen"
    if pct >= 40:
        return "green"
    if pct >= 20:
        return "yellow"
    return "red"


# ------------------------------------------------------------------ renderer


def render(readme_path, repo, meta, results_doc, servers, history):
    env = os.environ
    run_no = env.get("GH_RUN_NUMBER", "—")
    run_url = env.get("GH_RUN_URL", "")
    event = env.get("GH_EVENT", "local")
    repo_url = f"https://github.com/{repo}"
    raw_base = f"https://raw.githubusercontent.com/{repo}/main"

    tests = (results_doc or {}).get("results", [])
    tmeta = results_doc or {}
    by_key = {(t.get("HostName"), t.get("IP")): t for t in tests}

    merged = []
    for s in servers:
        entry = {f: s.get(f, "") for f in common.PUBLIC_FIELDS}
        t = by_key.get((s.get("HostName"), s.get("IP")))
        entry["test"] = ({k: t.get(k) for k in (
            "alive", "connect_ms", "via", "proto", "exit_ip", "exit_country",
            "geo_match", "http_s", "download_mbps", "downloaded_bytes",
            "speed_capped", "error")} if t else None)
        merged.append(entry)

    tested = [e for e in merged if e["test"]]
    alive = [e for e in tested if e["test"].get("alive")]
    dead = [e for e in tested if not e["test"].get("alive")]
    untested = len(merged) - len(tested)
    fetched = meta.get("unique_servers", len(merged)) if meta else len(merged)
    alive_pct = (100.0 * len(alive) / len(tested)) if tested else None
    usability = (100.0 * len(alive) / fetched) if fetched else None
    speeds = [e["test"]["download_mbps"] for e in alive
              if e["test"].get("download_mbps")]
    avg_sp = sum(speeds) / len(speeds) if speeds else None
    med_sp = median(speeds) if speeds else None
    max_sp = max(speeds) if speeds else None
    mismatches = [e for e in alive if e["test"].get("geo_match") is False]
    conns = [e["test"]["connect_ms"] for e in alive if e["test"].get("connect_ms")]

    fastest = sorted(alive, key=lambda e: (-e["test"].get("download_mbps") or 0,
                                           -e.get("Score", 0)))[:10]
    topscore = sorted(alive, key=lambda e: (-e.get("Score", 0),
                                            -(e["test"].get("download_mbps") or 0)))[:10]

    # countries ------------------------------------------------------------
    countries = defaultdict(lambda: {"n": 0, "alive": 0, "best": 0.0, "best_host": ""})
    for e in merged:
        c = countries[(e.get("CountryShort") or "??",
                       e.get("CountryLong") or "Unknown")]
        c["n"] += 1
        if e["test"] and e["test"].get("alive"):
            c["alive"] += 1
            mb = e["test"].get("download_mbps") or 0
            if mb > c["best"]:
                c["best"], c["best_host"] = mb, e.get("HostName", "")
    country_rows = sorted(countries.items(), key=lambda kv: (-kv[1]["n"], kv[0][0]))

    # honesty ----------------------------------------------------------------
    def claimed_mbps(e):
        return (e.get("Speed") or 0) / 1_000_000.0

    honest = [e for e in alive
              if e["test"].get("download_mbps") and claimed_mbps(e) > 0]
    honest.sort(key=lambda e: (e["test"]["download_mbps"] / claimed_mbps(e)))

    # failure breakdown -------------------------------------------------------
    fails = Counter(((e["test"].get("error") or "unknown").split(":")[0])
                    for e in dead)

    # badges -------------------------------------------------------------------
    def badge(label, message, color):
        return {"schemaVersion": 1, "label": label, "message": str(message),
                "color": color}

    badges = {
        "servers": badge("servers tracked", f"{fetched:,}", "blue"),
        "alive": badge("verified alive",
                       (f"{len(alive):,}/{fetched:,} ({usability:.0f}%)"
                        if usability is not None else "pending"),
                       alive_color(usability)),
        "speed": badge("avg measured speed",
                       (f"{avg_sp:.1f} Mbps" if avg_sp is not None else "pending"),
                       speed_color(avg_sp)),
        "updated": badge("last run",
                         common.iso_to_human(meta.get("fetched_at")) if meta
                         else "pending",
                         "informational"),
    }

    # ---------------------------------------------------------------- markdown
    L = []
    ap = L.append

    ap("# 🛡️ VPN Gate Monitor")
    ap("")
    ap("> **Every 6 hours** this repo fetches the complete public "
       "[VPN Gate](https://www.vpngate.net/en/) server list, **cleans, "
       "deduplicates and archives** it — and then does the part that matters: "
       "it **opens a real OpenVPN tunnel to every single listed server**, "
       "verifies that traffic genuinely exits through it, checks *where* it "
       "exits, and measures real download throughput.")
    ap(">")
    ap("> **Everything below this line is the auto-generated living report. "
       "No hand-edited numbers.**")
    ap("")
    wl = f"{repo}/actions/workflows/vpngate.yml"
    ap(f"[![pipeline](https://github.com/{wl}/badge.svg)]"
       f"(https://github.com/{wl})")
    for name in ("servers", "alive", "speed", "updated"):
        b = badges[name]
        url = quote(f"{raw_base}/badges/{name}.json", safe="")
        ap(f"[![{b['label']}](https://img.shields.io/endpoint?url={url})"
           f"]({raw_base}/badges/{name}.json)")
    ap("")

    # latest results ----------------------------------------------------------
    ap("## 📊 Latest results")
    ap("")
    if meta is None and not servers:
        ap("⏳ **No run has completed yet.** The first automated run is "
           "scheduled right after this repo was pushed — this report will "
           "fill itself in automatically.")
        ap("")
    else:
        run_line = f"#{run_no}"
        if run_url:
            run_line = f"[#{run_no} · view run]({run_url})"
        ap("| | |")
        ap("|---|---|")
        ap(f"| **Run** | {run_line} · "
           f"{common.iso_to_human(meta.get('fetched_at')) if meta else '—'}"
           f" · trigger: `{event}` |")
        ap(f"| **Servers fetched (unique)** | **{fetched:,}** |")
        if meta:
            ap(f"| **Duplicates removed** | "
               f"{meta.get('removed_exact_duplicates', 0):,} exact + "
               f"{meta.get('removed_same_ip_duplicates', 0):,} same-IP |")
        ap(f"| **Servers tested** | **{len(tested):,} of {fetched:,}** — "
           f"every single one, every run |" if tested else
           f"| **Servers tested** | ⏳ pending first test run |")
        if tested:
            ap(f"| **✅ Verified alive** (tunnel up + egress proven) | "
               f"**{len(alive):,}** |")
            ap(f"| **❌ Dead / unusable** | {len(dead):,} |")
            if usability is not None:
                ap(f"| **Usability** | **{usability:.1f}%** of everything "
                   f"VPN Gate lists right now actually works |")
            if avg_sp is not None:
                ap(f"| **⚡ Measured speed (avg / median / max)** | "
                   f"**{avg_sp:.1f} / {med_sp:.1f} / {max_sp:.1f} Mbps** |")
            if fastest:
                f0 = fastest[0]
                ap(f"| **🚀 Fastest verified** | **{esc(f0.get('HostName'))}** · "
                   f"{common.country_flag(f0.get('CountryShort'))} "
                   f"{esc(f0.get('CountryLong'))} · "
                   f"**{f0['test']['download_mbps']:.1f} Mbps** |")
            ap(f"| **🧭 Exit-country mismatches** | {len(mismatches):,} "
               f"(server exits somewhere else than it claims) |")
            if conns:
                ap(f"| **🤝 Handshake time (alive, avg)** | "
                   f"{sum(conns) / len(conns) / 1000:.1f} s |")
        if untested:
            ap(f"| **Untested** | {untested:,} |")
        ap("")

    # fastest -----------------------------------------------------------------
    ap("## 🚀 Fastest verified servers")
    ap("")
    if fastest:
        ap("| # | Server | Country | Endpoint | Handshake | Measured ↓ | "
           "Claimed ↓ | Score |")
        ap("|---:|---|---|---|---:|---:|---:|---:|")
        for i, e in enumerate(fastest, 1):
            t = e["test"]
            ap(f"| {i} | `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryLong'))} | `{esc(t.get('via') or e.get('IP'))}`"
               f"{'/' + esc(t.get('proto')) if t.get('proto') else ''} | "
               f"{(t.get('connect_ms') or 0) / 1000:.1f}s | "
               f"**{t.get('download_mbps') or 0:.1f} Mbps** | "
               f"{common.mbps(e.get('Speed'))} Mbps | {e.get('Score', 0):,} |")
        ap("")
        ap("*Measured = 5 MB download through the live tunnel to "
           "speed.cloudflare.com. Claimed = the server's self-reported line "
           "speed in the VPN Gate API.*")
    else:
        ap("⏳ No verified-alive servers yet — waiting for the first "
           "completed test run.")
    ap("")

    # top score -----------------------------------------------------------------
    ap("## ⭐ Top-scored & verified alive")
    ap("")
    if topscore:
        ap("| # | Server | Country | Score | Claimed ↓ | Measured ↓ | "
           "Sessions | Uptime | Log policy |")
        ap("|---:|---|---|---:|---:|---:|---:|---:|---|")
        for i, e in enumerate(topscore, 1):
            t = e["test"]
            ap(f"| {i} | `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | {e.get('Score', 0):,} | "
               f"{common.mbps(e.get('Speed'))} Mbps | "
               f"{t.get('download_mbps') or 0:.1f} Mbps | "
               f"{e.get('NumVpnSessions', 0):,} | "
               f"{common.fmt_uptime(e.get('Uptime'))} | "
               f"{esc(e.get('LogType'))} |")
    else:
        ap("⏳ Pending first completed test run.")
    ap("")

    # countries -----------------------------------------------------------------
    ap("## 🌍 Countries")
    ap("")
    if country_rows:
        ap("| Country | Servers | Verified alive | Best measured ↓ | "
           "Fastest server |")
        ap("|---|---:|---:|---:|---|")
        for (short, long_), c in country_rows[:40]:
            ap(f"| {common.country_flag(short)} {esc(long_)} ({esc(short)}) | "
               f"{c['n']:,} | {c['alive']:,} | "
               f"{c['best']:.1f} Mbps | `{esc(c['best_host'])}` |")
        if len(country_rows) > 40:
            ap(f"| … | +{len(country_rows) - 40} more countries | | | |")
    else:
        ap("⏳ Pending data.")
    ap("")

    # honesty --------------------------------------------------------------------
    ap("## 🕵️ Claim vs. reality")
    ap("")
    if honest:
        ap("The VPN Gate `Speed` field is whatever the server *claims*. "
           "Here is the truth, measured through a live tunnel — the hall of "
           "shame (claimed ≫ delivered):")
        ap("")
        ap("| Server | Country | Claims | Delivers | Reality ratio |")
        ap("|---|---|---:|---:|---:|")
        for e in honest[:10]:
            t = e["test"]
            ratio = t["download_mbps"] / claimed_mbps(e)
            ap(f"| `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | "
               f"{claimed_mbps(e):,.0f} Mbps | {t['download_mbps']:.1f} Mbps | "
               f"{ratio * 100:.0f}% |")
        ap("")
        best = honest[-5:]
        if best:
            names = ", ".join(f"`{esc(e.get('HostName'))}` "
                              f"({e['test']['download_mbps']:.0f} Mbps)"
                              for e in reversed(best))
            ap(f"Most honest of this round: {names}.")
    else:
        ap("⏳ Pending first completed test run.")
    ap("")

    # geo mismatches ----------------------------------------------------------------
    ap("## 🧭 Exit-country mismatches")
    ap("")
    if mismatches:
        ap("These servers are listed under one country but your traffic "
           "**actually exits somewhere else** (verified via Cloudflare's "
           "geo view of the exit IP) — useful to know before you trust one:")
        ap("")
        ap("| Server | Claims | Actually exits via | Exit IP | Measured ↓ |")
        ap("|---|---|---|---|---:|")
        for e in mismatches[:15]:
            t = e["test"]
            ap(f"| `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | "
               f"{common.country_flag(t.get('exit_country'))} "
               f"{esc(t.get('exit_country'))} | `{esc(t.get('exit_ip'))}` | "
               f"{t.get('download_mbps') or 0:.1f} Mbps |")
    else:
        ap("None detected in the latest run"
           + ("." if tested else " — pending first test run.") if not tested
           else ". ✅ Every verified server exits where it claims.")
    ap("")

    # history ------------------------------------------------------------------------
    ap("## 📈 History")
    ap("")
    if len(history) > 1:
        alive_series = [h.get("alive_pct") for h in history]
        speed_series = [h.get("avg_mbps") for h in history]
        ap(f"Alive % trend (last {len(history)} runs): "
           f"`{common.spark(alive_series)}`")
        ap("")
        ap(f"Avg measured speed (Mbps): `{common.spark(speed_series)}`")
        ap("")
        ap("| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |")
        ap("|---|---:|---:|---:|---:|---:|---:|")
        for h in reversed(history[-15:]):
            ap(f"| {common.iso_to_human(h.get('time'))} | "
               f"{h.get('fetched', 0):,} | {h.get('alive', 0):,} | "
               f"{h.get('alive_pct', 0):.0f}% | "
               f"{h.get('avg_mbps') or 0:.1f} | {h.get('max_mbps') or 0:.1f} | "
               f"{h.get('mismatches', 0)} |")
    else:
        ap("History builds up here run by run "
           f"(currently {len(history)} entr{'y' if len(history) == 1 else 'ies'}).")
    ap("")

    # pipeline --------------------------------------------------------------------------
    ap("## ⚙️ How the pipeline works")
    ap("")
    ap("```mermaid")
    ap("flowchart LR")
    ap("    C[\"cron: every 6h\"] --> F[\"fetch vpngate.net CSV API\"]")
    ap("    F --> L[\"log raw + meta\"]")
    ap("    L --> CL[\"clean + type-check\"]")
    ap("    CL --> D[\"dedupe hostname + IP\"]")
    ap("    D --> A[\"archive .csv.gz snapshot\"]")
    ap("    D --> T[\"REAL test: OpenVPN tunnel per server<br/>egress + geo + throughput\"]")
    ap("    T --> R[\"report: README + badges + history\"]")
    ap("    R --> P[\"commit and push\"]")
    ap("```")
    ap("")
    ap("1. **Fetch** — `GET /api/iphone/` with retries and endpoint "
       "fallback; responses are validated (the API sometimes serves an empty "
       "placeholder page to datacenter IPs) and the raw bytes are logged and "
       "hashed (sha256).")
    ap("2. **Clean** — parse the special CSV (`*vpn_servers` marker, "
       "`#`-prefixed header), type-check every numeric field, validate IPs, "
       "drop broken rows, strip noise.")
    ap("3. **Dedupe** — remove exact `(HostName, IP)` duplicates, then "
       "same-IP entries keeping the highest-scoring one.")
    ap("4. **Archive** — every run writes an immutable gzipped snapshot to "
       "`archive/` (auto-pruned to the newest 360 ≈ 90 days).")
    ap("5. **Test — the real deal.** For **every** server, every run: decode "
       "its embedded OpenVPN config, force it onto a per-worker `tun` device, "
       "disable pushed routes, pin two /32 routes through the tunnel to "
       "per-worker Cloudflare anycast IPs, wait for *Initialization Sequence "
       "Completed*, then verify egress (`cdn-cgi/trace` through the tunnel "
       "must return a foreign exit IP + real exit country) and measure a 5 MB "
       "download through the same tunnel. Up to 48 isolated tunnels run in "
       "parallel; a server that never completes the handshake is hard-killed "
       "after 25 s.")
    ap("6. **Report** — this README, four live badges, `latest.json`, "
       "`summary.json` and the `history.jsonl` log are regenerated and "
       "committed by `github-actions[bot]`.")
    ap("")

    # data files ---------------------------------------------------------------------------
    ap("## 📁 Data files & programmatic use")
    ap("")
    ap(f"All results are in this repo — hotlink them straight from "
       f"`{repo_url}`:")
    ap("")
    ap(f"- [`data/latest.json`]({raw_base}/data/latest.json) — the merged "
       f"dataset: every cleaned server + its latest real test result")
    ap(f"- [`data/servers_clean.csv`]({raw_base}/data/servers_clean.csv) — "
       f"cleaned, deduplicated server list (no bulky config blobs)")
    ap(f"- [`data/summary.json`]({raw_base}/data/summary.json) — compact "
       f"run summary with failure breakdown")
    ap(f"- [`data/history.jsonl`]({raw_base}/data/history.jsonl) — one JSON "
       f"line per run, append-only")
    ap(f"- [`archive/`]({repo_url}/tree/main/archive) — immutable gzipped "
       f"snapshots of every run")
    ap("- full logs, raw API response and per-server error details are "
       "attached to each [Actions run]("
       f"https://github.com/{repo}/actions) as artifacts (30-day retention)")
    ap("")
    ap("Grab a working VPN right now:")
    ap("")
    ap("```bash")
    ap(f"curl -s {raw_base}/data/latest.json \\")
    ap("  | python3 -c \"import json,sys;[print(s['IP'],s['CountryShort'],"
       "s['test']['download_mbps'],'Mbps') for s in json.load(sys.stdin) "
       "if s['test'] and s['test']['alive']]\" \\")
    ap("  | sort -k3 -nr | head")
    ap("```")
    ap("")
    ap("Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-"
       "reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes "
       "· `download_mbps` Mbps (measured through the tunnel).")
    ap("")

    # methodology -----------------------------------------------------------------------------
    ap("## 🔬 Methodology & caveats")
    ap("")
    ap("- **Real tunnels, not CSV checks.** A server only counts as alive if "
       "OpenVPN completed its handshake *and* an HTTPS request bound to the "
       "tunnel egressed with a foreign IP. A server whose tunnel silently "
       "black-holes traffic fails the egress step and is reported dead.")
    ap("- **No DNS through the VPN.** Test destinations are pinned with "
       "`curl --resolve` to per-worker Cloudflare anycast addresses, so a "
       "broken/hijacking VPN DNS can never fake a success.")
    ap("- **Throughput** is one 5 MB download to `speed.cloudflare.com` "
       "through the live tunnel — a sample, not a lab measurement.")
    ap("- **Vantage point**: GitHub Actions runners (Azure, usually US/EU). "
       "A server that is slow from there may be fast from your country, and "
       "vice versa.")
    ap("- **Fairness**: volunteer servers are shared — measured speeds dip "
       "when many clients are connected (`NumVpnSessions` is listed).")
    ap("- **Security**: test traffic is TLS to Cloudflare only; we never send "
       "anything sensitive through volunteer servers. Neither should you — "
       "assume the operator can see traffic metadata.")
    ap("")

    # disclaimer --------------------------------------------------------------------------------
    ap("## ⚠️ Disclaimer")
    ap("")
    ap("- [VPN Gate](https://www.vpngate.net/en/) is an academic experiment "
       "by the University of Tsukuba, Japan (Daiyuu Nobori & co). This "
       "project is an independent monitor of its public API and is **not "
       "affiliated** with it.")
    ap("- VPN servers are run by volunteers; some keep connection logs "
       "(see `LogType`). Use them legally and responsibly; do not route "
       "anything private or illegal through them.")
    ap("- Data is provided **as-is** for research/educational purposes.")
    ap("")
    ap("## 📄 License")
    ap("")
    ap("Code: MIT. Data: originates from VPN Gate's public API — respect "
       "their terms.")
    ap("")
    if run_url:
        ap("---")
        ap(f"*Auto-generated by [run #{run_no}]({run_url}) at "
           f"{common.now_iso().replace('T', ' ').replace('Z', ' UTC')}. "
           f"Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*")
        ap("")

    return "\n".join(L).rstrip() + "\n", badges, merged, {
        "meta": meta, "fetched": fetched, "tested": len(tested),
        "alive": len(alive), "dead": len(dead), "untested": untested,
        "alive_pct": alive_pct, "usability": usability,
        "avg_mbps": avg_sp, "median_mbps": med_sp, "max_mbps": max_sp,
        "mismatches": len(mismatches),
        "avg_connect_ms": (sum(conns) / len(conns)) if conns else None,
        "fastest": [{"HostName": e.get("HostName"), "IP": e.get("IP"),
                     "CountryShort": e.get("CountryShort"),
                     "download_mbps": e["test"].get("download_mbps")}
                    for e in fastest],
        "failure_breakdown": dict(fails.most_common(12)),
        "runner_ip": tmeta.get("runner_ip"),
        "run": {"number": run_no, "url": run_url, "event": event,
                "generated_at": common.now_iso()},
    }


# ------------------------------------------------------------------------ main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--badges-dir", default="badges")
    args = ap.parse_args()

    repo = os.environ.get("GH_REPO", REPO_DEFAULT)
    meta = read_json(os.path.join(args.data_dir, "last_fetch.json"))
    results_doc = read_json(os.path.join(args.data_dir, "results.json"))
    servers = read_servers_csv(os.path.join(args.data_dir, "servers_clean.csv"))
    hist_path = os.path.join(args.data_dir, "history.jsonl")
    history = common.read_history(hist_path, common.DEFAULTS["history_cap"])

    readme, badges, merged, s = render(args.readme, repo, meta, results_doc,
                                       servers, history)

    common.atomic_write(args.readme, readme.encode("utf-8"))
    plog(f"wrote {args.readme} ({len(readme):,} bytes)")

    os.makedirs(args.badges_dir, exist_ok=True)
    for name, doc in badges.items():
        common.write_json(os.path.join(args.badges_dir, f"{name}.json"), doc)
    plog(f"wrote {len(badges)} badges -> {args.badges_dir}/")

    common.write_json(os.path.join(args.data_dir, "latest.json"), merged)
    plog(f"wrote {args.data_dir}/latest.json ({len(merged):,} servers)")

    # history (idempotent per fetch: re-rendering the same fetch replaces
    # its own line instead of duplicating it)
    if meta is not None:
        run_key = meta.get("fetched_at") or common.now_iso()
        entry = {
            "run_key": run_key,
            "time": meta.get("fetched_at") or common.now_iso(),
            "fetched": s["fetched"],
            "tested": s["tested"],
            "alive": s["alive"],
            "alive_pct": round(s["alive_pct"], 1) if s["alive_pct"] is not None else None,
            "avg_mbps": round(s["avg_mbps"], 2) if s["avg_mbps"] is not None else None,
            "max_mbps": s["max_mbps"],
            "mismatches": s["mismatches"],
            "run": s["run"],
        }
        if history and history[-1].get("run_key") == run_key:
            history[-1] = entry
        else:
            history.append(entry)
        common.write_history(hist_path, history)
        plog(f"history -> {hist_path} ({len(history)} entries)")

    # compact summary (also used by the commit step)
    common.write_json(os.path.join(args.data_dir, "summary.json"), s)
    plog(f"wrote {args.data_dir}/summary.json")

    # GitHub step summary, if running inside Actions
    gss = os.environ.get("GITHUB_STEP_SUMMARY")
    if gss and os.path.exists(os.path.dirname(gss) or "."):
        with open(gss, "a", encoding="utf-8") as f:
            f.write("\n### 🛡️ VPN Gate Monitor — run summary\n\n")
            f.write(f"- Fetched **{s['fetched']:,}** unique servers\n")
            if s["usability"] is not None:
                f.write(f"- Real-tested **{s['tested']:,}** — "
                        f"**{s['alive']:,} verified alive** "
                        f"({s['usability']:.0f}% usable)\n")
            else:
                f.write(f"- Real-tested {s['tested']:,}\n")
            if s["avg_mbps"] is not None:
                f.write(f"- Avg measured speed **{s['avg_mbps']:.1f} Mbps**, "
                        f"max **{s['max_mbps']:.1f} Mbps**\n")
            f.write(f"- Exit-country mismatches: {s['mismatches']}\n")
            if s["fastest"]:
                f0 = s["fastest"][0]
                f.write(f"- Fastest: `{f0['HostName']}` "
                        f"({f0['CountryShort']}) — "
                        f"{f0['download_mbps']:.1f} Mbps\n")
        plog("appended GitHub step summary")

    if s["usability"] is not None:
        plog(f"DONE: fetched={s['fetched']} tested={s['tested']} "
             f"alive={s['alive']} usability={s['usability']:.1f}%")
    else:
        plog(f"DONE: fetched={s['fetched']} tested={s['tested']} "
             f"alive={s['alive']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
