# 🛡️ VPN Gate Monitor

> **Every 6 hours** this repo fetches the complete public [VPN Gate](https://www.vpngate.net/en/) server list, **cleans, deduplicates and archives** it — and then does the part that matters: it **opens a real OpenVPN tunnel to every single listed server**, verifies that traffic genuinely exits through it, checks *where* it exits, and measures real download throughput.
>
> **Everything below this line is the auto-generated living report. No hand-edited numbers.**

[![pipeline](https://github.com/G1010yzd10/vpngate-monitor/actions/workflows/vpngate.yml/badge.svg)](https://github.com/G1010yzd10/vpngate-monitor/actions/workflows/vpngate.yml)
[![servers tracked](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FG1010yzd10%2Fvpngate-monitor%2Fmain%2Fbadges%2Fservers.json)](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/badges/servers.json)
[![verified alive](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FG1010yzd10%2Fvpngate-monitor%2Fmain%2Fbadges%2Falive.json)](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/badges/alive.json)
[![avg measured speed](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FG1010yzd10%2Fvpngate-monitor%2Fmain%2Fbadges%2Fspeed.json)](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/badges/speed.json)
[![last run](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FG1010yzd10%2Fvpngate-monitor%2Fmain%2Fbadges%2Fupdated.json)](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/badges/updated.json)

## 📊 Latest results

| | |
|---|---|
| **Run** | [#16 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37119553858) · 2026-10-03 11:25:01 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **99** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **739 of 739** — all 99 current + 640 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **388** — 76 from the current list + 312 historical ♻️ |
| **❌ Dead / unusable** | 351 |
| **Usability** | **76.8%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **11.8 / 13.5 / 37.9 Mbps** |
| **🚀 Fastest verified** | **vpn118756292** · 🇺🇸 United States · **37.9 Mbps** |
| **🧭 Exit-country mismatches** | 5 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.9 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn118756292` | 🇺🇸 United States | ♻️ historical | `67.5.100.174:995`/tcp | 2.3s | **37.9 Mbps** | 392.0 Mbps | 2,119,917 |
| 2 | `vpn918840683` | 🇺🇸 United States | ♻️ historical | `38.34.239.132:1245`/tcp | 2.5s | **33.3 Mbps** | 348.6 Mbps | 3,989,552 |
| 3 | `vpn551800667` | 🇯🇵 Japan | 📋 current | `111.234.191.130:1387`/udp | 2.5s | **25.1 Mbps** | 356.6 Mbps | 604,619 |
| 4 | `vpn714667264` | 🇪🇨 Ecuador | 📋 current | `181.199.60.152:6165`/udp | 2.5s | **25.0 Mbps** | 132.5 Mbps | 1,438,412 |
| 5 | `vpn705687526` | 🇯🇵 Japan | ♻️ historical | `147.192.42.21:1195`/udp | 2.5s | **24.8 Mbps** | 74.8 Mbps | 1,024,306 |
| 6 | `vpn325696545` | 🇯🇵 Japan | ♻️ historical | `39.111.138.50:1195`/udp | 2.5s | **24.5 Mbps** | 728.3 Mbps | 362,807 |
| 7 | `vpn525554372` | 🇯🇵 Japan | ♻️ historical | `101.143.139.46:1612`/udp | 2.5s | **24.4 Mbps** | 431.2 Mbps | 585,686 |
| 8 | `vpn989144671` | 🇯🇵 Japan | 📋 current | `133.32.218.20:2984`/udp | 1.8s | **23.8 Mbps** | 499.7 Mbps | 1,172,890 |
| 9 | `vpn646473951` | 🇯🇵 Japan | ♻️ historical | `147.192.76.151:1195`/udp | 2.5s | **23.7 Mbps** | 676.3 Mbps | 1,442,573 |
| 10 | `vpn707684064` | 🇯🇵 Japan | ♻️ historical | `118.104.225.196:1501`/udp | 2.5s | **22.8 Mbps** | 89.6 Mbps | 881,918 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `vpn918840683` | 🇺🇸 US | 3,989,552 | 348.6 Mbps | 33.3 Mbps | 231 | 13.5 d | 2weeks |
| 2 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 14.2 Mbps | 107 | 126.5 d | 2weeks |
| 3 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 13.9 Mbps | 143 | 126.5 d | 2weeks |
| 4 | `public-vpn-253` | 🇯🇵 JP | 2,897,255 | 465.0 Mbps | 6.0 Mbps | 103 | 128.6 d | 2weeks |
| 5 | `public-vpn-201` | 🇯🇵 JP | 2,851,535 | 237.9 Mbps | 8.3 Mbps | 79 | 126.5 d | 2weeks |
| 6 | `public-vpn-239` | 🇯🇵 JP | 2,829,899 | 392.6 Mbps | 12.8 Mbps | 38 | 126.6 d | 2weeks |
| 7 | `public-vpn-136` | 🇯🇵 JP | 2,804,989 | 557.6 Mbps | 6.4 Mbps | 27 | 126.6 d | 2weeks |
| 8 | `public-vpn-182` | 🇯🇵 JP | 2,781,744 | 1,013.3 Mbps | 2.5 Mbps | 119 | 129.6 d | 2weeks |
| 9 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 13.9 Mbps | 42 | 128.6 d | 2weeks |
| 10 | `public-vpn-66` | 🇯🇵 JP | 2,758,587 | 393.6 Mbps | 9.8 Mbps | 109 | 126.6 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 361 | 220 | 25.1 Mbps | `vpn551800667` |
| 🇰🇷 Korea Republic of (KR) | 217 | 135 | 20.3 Mbps | `vpn922387505` |
| 🇷🇺 Russian Federation (RU) | 46 | 1 | 15.4 Mbps | `vpn452876228` |
| 🇹🇭 Thailand (TH) | 46 | 12 | 14.3 Mbps | `vpn367079905` |
| 🇺🇸 United States (US) | 23 | 3 | 37.9 Mbps | `vpn118756292` |
| 🇻🇳 Viet Nam (VN) | 11 | 6 | 12.0 Mbps | `vpn381476084` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 5 | 3 | 0.9 Mbps | `vpn981204829` |
| 🇦🇷 Argentina (AR) | 3 | 1 | 0.8 Mbps | `vpn510681258` |
| 🇨🇱 Chile (CL) | 3 | 1 | 16.1 Mbps | `vpn690784060` |
| 🇮🇳 India (IN) | 3 | 1 | 8.0 Mbps | `vpn359610091` |
| 🇲🇽 Mexico (MX) | 3 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 1 | 0.9 Mbps | `_unregistered_vpn952021746` |
| 🇵🇪 Peru (PE) | 2 | 0 | 0.0 Mbps | `` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 25.0 Mbps | `vpn714667264` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 12.2 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 1 | 7.3 Mbps | `vpn808337650` |
| 🇲🇲 Myanmar (MM) | 1 | 1 | 0.7 Mbps | `vpn192397778` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn219941769` | 🇰🇷 KR | 772 Mbps | 0.4 Mbps | 0% |
| `public-vpn-237` | 🇯🇵 JP | 686 Mbps | 0.5 Mbps | 0% |
| `vpn771151831` | 🇰🇷 KR | 44 Mbps | 0.0 Mbps | 0% |
| `public-vpn-214` | 🇯🇵 JP | 4,635 Mbps | 4.8 Mbps | 0% |
| `vpn121128130` | 🇯🇵 JP | 599 Mbps | 1.1 Mbps | 0% |
| `public-vpn-198` | 🇯🇵 JP | 809 Mbps | 1.6 Mbps | 0% |
| `vpn882137641` | 🇯🇵 JP | 829 Mbps | 1.7 Mbps | 0% |
| `public-vpn-182` | 🇯🇵 JP | 1,013 Mbps | 2.5 Mbps | 0% |
| `public-vpn-224` | 🇯🇵 JP | 5,635 Mbps | 14.3 Mbps | 0% |
| `vpn482140614` | 🇯🇵 JP | 131 Mbps | 0.4 Mbps | 0% |

Most honest of this round: `vpn763610422` (14 Mbps), `vpn100779275` (15 Mbps), `vpn882552170` (14 Mbps), `vpn346537516` (15 Mbps), `vpn293598259` (13 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn192397778` | 🇲🇲 MM | 🇮🇳 IN | `167.103.2.108` | 0.7 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 0.9 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 0.9 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 0.9 Mbps |
| `vpn808337650` | 🇱🇺 LU | 🇷🇺 RU | `178.66.129.246` | 7.3 Mbps |

## 📈 History

Alive % trend (last 7 runs): `██▇▆▆▁▄`

Avg measured speed (Mbps): `▆▇▁▇▁██`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-10-03 04:45:33 UTC | 94 | 322 | 49% | 12.6 | 77.0 | 5 |
| 2026-10-02 22:01:53 UTC | 97 | 164 | 28% | 12.9 | 97.8 | 5 |
| 2026-10-02 05:01:43 UTC | 97 | 289 | 57% | 9.1 | 54.4 | 5 |
| 2026-10-01 05:13:27 UTC | 96 | 248 | 59% | 12.1 | 73.6 | 6 |
| 2026-09-30 04:59:45 UTC | 93 | 214 | 63% | 8.7 | 23.2 | 7 |
| 2026-09-29 04:50:31 UTC | 91 | 191 | 73% | 11.9 | 80.1 | 3 |
| 2026-09-29 04:45:58 UTC | 93 | 126 | 70% | 11.4 | 53.6 | 2 |

## ⚙️ How the pipeline works

```mermaid
flowchart LR
    C["cron: every 6h"] --> F["fetch vpngate.net CSV API"]
    F --> L["log raw + meta"]
    L --> CL["clean + type-check"]
    CL --> D["dedupe hostname + IP"]
    D --> A["archive .csv.gz snapshot"]
    D --> T["REAL test: OpenVPN tunnel per server<br/>egress + geo + throughput"]
    T --> R["report: README + badges + history"]
    R --> P["commit and push"]
```

1. **Fetch** — `GET /api/iphone/` with retries and endpoint fallback; responses are validated (the API sometimes serves an empty placeholder page to datacenter IPs) and the raw bytes are logged and hashed (sha256).
2. **Clean** — parse the special CSV (`*vpn_servers` marker, `#`-prefixed header), type-check every numeric field, validate IPs, drop broken rows, strip noise.
3. **Dedupe** — remove exact `(HostName, IP)` duplicates, then same-IP entries keeping the highest-scoring one.
4. **Archive** — every run writes an immutable gzipped snapshot to `archive/` (auto-pruned to the newest 360 ≈ 90 days).
5. **Test — the real deal.** For **every** server, every run — not just the API's current list, but **the union of every server that has ever appeared** within the 30-day recall window (kept in `data/known_servers.json`): decode the shared VPN Gate OpenVPN template (all servers ship the same CA + dummy client cert — verified), rebuild each server's config with its remembered `(proto, port)`, force it onto a per-worker `tun` device, disable pushed routes, pin two /32 routes through the tunnel to per-worker Cloudflare anycast IPs, wait for *Initialization Sequence Completed*, then verify egress (`cdn-cgi/trace` through the tunnel must return a foreign exit IP + real exit country) and measure a 5 MB download through the same tunnel. Up to 48 isolated tunnels run in parallel; a server that never completes the handshake is hard-killed after 25 s.
6. **Report** — this README, four live badges, `latest.json`, `summary.json` and the `history.jsonl` log are regenerated and committed by `github-actions[bot]`.

## 📁 Data files & programmatic use

All results are in this repo — hotlink them straight from `https://github.com/G1010yzd10/vpngate-monitor`:

- [`data/latest.json`](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/data/latest.json) — the merged dataset: every cleaned server + its latest real test result
- [`data/servers_clean.csv`](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/data/servers_clean.csv) — cleaned, deduplicated server list (no bulky config blobs)
- [`data/summary.json`](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/data/summary.json) — compact run summary with failure breakdown
- [`data/history.jsonl`](https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/data/history.jsonl) — one JSON line per run, append-only
- [`archive/`](https://github.com/G1010yzd10/vpngate-monitor/tree/main/archive) — immutable gzipped snapshots of every run
- full logs, raw API response and per-server error details are attached to each [Actions run](https://github.com/G1010yzd10/vpngate-monitor/actions) as artifacts (30-day retention)

Grab a working VPN right now:

```bash
curl -s https://raw.githubusercontent.com/G1010yzd10/vpngate-monitor/main/data/latest.json \
  | python3 -c "import json,sys;[print(s['IP'],s['CountryShort'],s['test']['download_mbps'],'Mbps') for s in json.load(sys.stdin) if s['test'] and s['test']['alive']]" \
  | sort -k3 -nr | head
```

Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes · `download_mbps` Mbps (measured through the tunnel).

## 🔬 Methodology & caveats

- **Real tunnels, not CSV checks.** A server only counts as alive if OpenVPN completed its handshake *and* an HTTPS request bound to the tunnel egressed with a foreign IP. A server whose tunnel silently black-holes traffic fails the egress step and is reported dead.
- **No DNS through the VPN.** Test destinations are pinned with `curl --resolve` to per-worker Cloudflare anycast addresses, so a broken/hijacking VPN DNS can never fake a success.
- **Throughput** is one 5 MB download to `speed.cloudflare.com` through the live tunnel — a sample, not a lab measurement.
- **Vantage point**: GitHub Actions runners (Azure, usually US/EU). A server that is slow from there may be fast from your country, and vice versa.
- **Fairness**: volunteer servers are shared — measured speeds dip when many clients are connected (`NumVpnSessions` is listed).
- **Security**: test traffic is TLS to Cloudflare only; we never send anything sensitive through volunteer servers. Neither should you — assume the operator can see traffic metadata.

## ⚠️ Disclaimer

- [VPN Gate](https://www.vpngate.net/en/) is an academic experiment by the University of Tsukuba, Japan (Daiyuu Nobori & co). This project is an independent monitor of its public API and is **not affiliated** with it.
- VPN servers are run by volunteers; some keep connection logs (see `LogType`). Use them legally and responsibly; do not route anything private or illegal through them.
- Data is provided **as-is** for research/educational purposes.

## 📄 License

Code: MIT. Data: originates from VPN Gate's public API — respect their terms.

---
*Auto-generated by [run #16](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37119553858) at 2026-10-03 11:29:16 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
