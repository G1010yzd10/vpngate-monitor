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
| **Run** | [#30 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37541235007) · 2026-10-06 22:32:59 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **93** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **1,252 of 1,252** — all 93 current + 1,159 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **425** — 46 from the current list + 379 historical ♻️ |
| **❌ Dead / unusable** | 827 |
| **Usability** | **49.5%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **11.8 / 13.6 / 102.0 Mbps** |
| **🚀 Fastest verified** | **vpn132949429** · 🇺🇸 United States · **102.0 Mbps** |
| **🧭 Exit-country mismatches** | 5 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.0 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn132949429` | 🇺🇸 United States | ♻️ historical | `47.155.228.164:1392`/udp | 2.0s | **102.0 Mbps** | 150.2 Mbps | 1,848,446 |
| 2 | `vpn729038920` | 🇺🇸 United States | ♻️ historical | `38.49.242.56:1538`/tcp | 2.3s | **28.5 Mbps** | 96.5 Mbps | 1,872,287 |
| 3 | `vpn525554372` | 🇯🇵 Japan | ♻️ historical | `101.142.196.72:1612`/udp | 2.5s | **24.0 Mbps** | 333.3 Mbps | 637,125 |
| 4 | `vpn679218486` | 🇯🇵 Japan | 📋 current | `124.209.226.195:1752`/udp | 2.3s | **23.2 Mbps** | 686.9 Mbps | 597,704 |
| 5 | `vpn615496887` | 🇯🇵 Japan | ♻️ historical | `220.254.1.124:1657`/udp | 2.5s | **23.1 Mbps** | 810.1 Mbps | 596,108 |
| 6 | `vpn693017146` | 🇯🇵 Japan | ♻️ historical | `218.131.41.95:1975`/udp | 2.5s | **22.1 Mbps** | 2,558.8 Mbps | 599,858 |
| 7 | `vpn321670159` | 🇯🇵 Japan | 📋 current | `61.21.197.1:1598`/udp | 2.5s | **21.1 Mbps** | 735.0 Mbps | 617,695 |
| 8 | `vpn767479473` | 🇰🇷 Korea Republic of | ♻️ historical | `211.226.144.221:1195`/udp | 2.5s | **20.5 Mbps** | 78.3 Mbps | 1,366,895 |
| 9 | `vpn384156708` | 🇯🇵 Japan | 📋 current | `133.32.233.192:1062`/udp | 2.3s | **20.5 Mbps** | 926.3 Mbps | 887,448 |
| 10 | `vpn677403438` | 🇺🇸 United States | ♻️ historical | `98.169.175.14:1988`/tcp | 2.5s | **19.7 Mbps** | 157.6 Mbps | 1,851,456 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 15.2 Mbps | 107 | 126.5 d | 2weeks |
| 2 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 13.8 Mbps | 143 | 126.5 d | 2weeks |
| 3 | `public-vpn-136` | 🇯🇵 JP | 2,804,989 | 557.6 Mbps | 15.7 Mbps | 27 | 126.6 d | 2weeks |
| 4 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 13.3 Mbps | 42 | 128.6 d | 2weeks |
| 5 | `public-vpn-66` | 🇯🇵 JP | 2,758,587 | 393.6 Mbps | 16.4 Mbps | 109 | 126.6 d | 2weeks |
| 6 | `public-vpn-155` | 🇯🇵 JP | 2,714,026 | 349.5 Mbps | 16.4 Mbps | 44 | 126.6 d | 2weeks |
| 7 | `public-vpn-196` | 🇯🇵 JP | 2,679,699 | 701.4 Mbps | 4.1 Mbps | 77 | 126.6 d | 2weeks |
| 8 | `public-vpn-135` | 🇯🇵 JP | 2,601,645 | 333.1 Mbps | 16.1 Mbps | 89 | 128.6 d | 2weeks |
| 9 | `public-vpn-206` | 🇯🇵 JP | 2,311,114 | 530.4 Mbps | 3.4 Mbps | 75 | 128.6 d | 2weeks |
| 10 | `vpn750532477` | 🇺🇸 US | 2,174,484 | 38.4 Mbps | 7.4 Mbps | 4 | 18.2 h | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 574 | 254 | 24.0 Mbps | `vpn525554372` |
| 🇰🇷 Korea Republic of (KR) | 389 | 127 | 20.5 Mbps | `vpn767479473` |
| 🇷🇺 Russian Federation (RU) | 86 | 1 | 10.4 Mbps | `vpn856084155` |
| 🇹🇭 Thailand (TH) | 86 | 6 | 14.6 Mbps | `vpn719752522` |
| 🇺🇸 United States (US) | 35 | 10 | 102.0 Mbps | `vpn132949429` |
| 🇻🇳 Viet Nam (VN) | 24 | 6 | 11.1 Mbps | `vpn381476084` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 6 | 4 | 0.9 Mbps | `vpn429922709` |
| 🇦🇷 Argentina (AR) | 5 | 1 | 17.7 Mbps | `vpn510681258` |
| 🇲🇽 Mexico (MX) | 5 | 0 | 0.0 Mbps | `` |
| 🇨🇱 Chile (CL) | 4 | 1 | 12.8 Mbps | `vpn548414740` |
| 🇮🇳 India (IN) | 4 | 1 | 8.1 Mbps | `vpn359610091` |
| 🇨🇴 Colombia (CO) | 3 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 3 | 1 | 13.5 Mbps | `vpn314968721` |
| 🇨🇦 Canada (CA) | 2 | 1 | 18.6 Mbps | `vpn779606145` |
| 🇨🇳 China (CN) | 2 | 2 | 6.1 Mbps | `_unregistered_vpn952021746` |
| 🇬🇧 United Kingdom (GB) | 2 | 1 | 11.4 Mbps | `vpn890210379` |
| 🇲🇲 Myanmar (MM) | 2 | 1 | 1.8 Mbps | `vpn192397778` |
| 🇺🇦 Ukraine (UA) | 2 | 1 | 11.9 Mbps | `vpn313985146` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 1 | 1 | 6.8 Mbps | `vpn562825704` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 1 | 1 | 10.9 Mbps | `vpn564048942` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇿 Czech Republic (CZ) | 1 | 1 | 10.7 Mbps | `vpn809432043` |
| 🇩🇪 Germany (DE) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 14.7 Mbps | `vpn714667264` |
| 🇫🇮 Finland (FI) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 2.4 Mbps | `diamondgnd` |
| 🇭🇰 Hong Kong (HK) | 1 | 1 | 10.7 Mbps | `vpn986755484` |
| 🇮🇷 Iran (ISLAMIC Republic Of) (IR) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇨 Saint Lucia (LC) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 12.8 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn219941769` | 🇰🇷 KR | 751 Mbps | 0.4 Mbps | 0% |
| `vpn421074651` | 🇰🇷 KR | 283 Mbps | 0.2 Mbps | 0% |
| `vpn981288372` | 🇯🇵 JP | 139 Mbps | 0.1 Mbps | 0% |
| `vpn771151831` | 🇰🇷 KR | 44 Mbps | 0.1 Mbps | 0% |
| `vpn779820187` | 🇯🇵 JP | 831 Mbps | 1.3 Mbps | 0% |
| `public-vpn-157` | 🇯🇵 JP | 4,732 Mbps | 14.4 Mbps | 0% |
| `public-vpn-257` | 🇯🇵 JP | 353 Mbps | 1.3 Mbps | 0% |
| `vpn481575539` | 🇯🇵 JP | 395 Mbps | 1.5 Mbps | 0% |
| `public-vpn-210` | 🇯🇵 JP | 174 Mbps | 0.8 Mbps | 0% |
| `public-vpn-194` | 🇯🇵 JP | 257 Mbps | 1.5 Mbps | 1% |

Most honest of this round: `vpn510681258` (18 Mbps), `vpn613456364` (14 Mbps), `vpn346537516` (16 Mbps), `vpn137812529` (17 Mbps), `vpn853332775` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 0.9 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 0.8 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 0.7 Mbps |
| `vpn192397778` | 🇲🇲 MM | 🇮🇳 IN | `167.103.2.105` | 1.8 Mbps |
| `vpn962496160` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.24` | 0.5 Mbps |

## 📈 History

Alive % trend (last 15 runs): `██▇▆▆▁▄▅▄▃▄▁▂▃▄`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▂▃▂▂`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-10-06 13:07:16 UTC | 99 | 577 | 48% | 9.6 | 21.3 | 7 |
| 2026-10-06 05:51:24 UTC | 97 | 466 | 41% | 9.7 | 48.3 | 6 |
| 2026-10-05 23:55:39 UTC | 91 | 372 | 34% | 10.1 | 56.0 | 6 |
| 2026-10-05 19:57:29 UTC | 94 | 328 | 32% | 9.2 | 44.0 | 4 |
| 2026-10-05 14:10:31 UTC | 95 | 434 | 45% | 8.8 | 52.2 | 4 |
| 2026-10-05 05:01:08 UTC | 94 | 394 | 44% | 10.9 | 50.4 | 3 |
| 2026-10-03 16:01:20 UTC | 98 | 368 | 45% | 8.8 | 33.1 | 4 |
| 2026-10-03 11:25:01 UTC | 99 | 388 | 52% | 11.8 | 37.9 | 5 |
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
*Auto-generated by [run #30](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37541235007) at 2026-10-06 22:41:36 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
