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
| **Run** | [#41 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/38051160764) · 2026-10-10 12:13:35 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **95** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **1,905 of 1,905** — all 95 current + 1,810 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **855** — 62 from the current list + 793 historical ♻️ |
| **❌ Dead / unusable** | 1,050 |
| **Usability** | **65.3%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **11.3 / 13.4 / 25.6 Mbps** |
| **🚀 Fastest verified** | **vpn325696545** · 🇯🇵 Japan · **25.6 Mbps** |
| **🧭 Exit-country mismatches** | 14 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.9 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn325696545` | 🇯🇵 Japan | ♻️ historical | `39.111.138.50:1195`/udp | 2.5s | **25.6 Mbps** | 728.3 Mbps | 362,807 |
| 2 | `vpn445932459` | 🇯🇵 Japan | 📋 current | `183.180.183.153:5775`/udp | 2.3s | **25.6 Mbps** | 732.7 Mbps | 663,464 |
| 3 | `vpn372889393` | 🇯🇵 Japan | ♻️ historical | `131.147.172.243:1195`/udp | 2.5s | **25.4 Mbps** | 904.6 Mbps | 603,530 |
| 4 | `vpn980413265` | 🇯🇵 Japan | ♻️ historical | `138.64.86.7:51245`/udp | 2.5s | **24.7 Mbps** | 558.8 Mbps | 616,029 |
| 5 | `vpn265387448` | 🇯🇵 Japan | 📋 current | `138.64.81.196:7775`/udp | 2.5s | **24.6 Mbps** | 730.6 Mbps | 605,108 |
| 6 | `vpn821116418` | 🇯🇵 Japan | ♻️ historical | `138.64.97.146:21635`/udp | 2.3s | **24.5 Mbps** | 830.0 Mbps | 579,283 |
| 7 | `vpn169318955` | 🇯🇵 Japan | ♻️ historical | `138.64.86.41:52295`/udp | 2.5s | **24.5 Mbps** | 644.4 Mbps | 717,595 |
| 8 | `vpn393802235` | 🇯🇵 Japan | 📋 current | `14.132.60.48:1742`/udp | 2.5s | **24.3 Mbps** | 2,226.1 Mbps | 595,626 |
| 9 | `vpn679218486` | 🇯🇵 Japan | ♻️ historical | `124.209.226.195:1752`/udp | 2.5s | **23.9 Mbps** | 686.9 Mbps | 597,704 |
| 10 | `vpn522595060` | 🇯🇵 Japan | ♻️ historical | `126.94.82.182:1195`/udp | 2.5s | **23.5 Mbps** | 210.0 Mbps | 576,635 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 7.9 Mbps | 107 | 126.5 d | 2weeks |
| 2 | `public-vpn-64` | 🇯🇵 JP | 2,982,423 | 82.6 Mbps | 1.2 Mbps | 74 | 7.0 d | 2weeks |
| 3 | `public-vpn-182` | 🇯🇵 JP | 2,781,744 | 1,013.3 Mbps | 12.2 Mbps | 119 | 129.6 d | 2weeks |
| 4 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 3.6 Mbps | 42 | 128.6 d | 2weeks |
| 5 | `public-vpn-134` | 🇯🇵 JP | 2,711,895 | 135.1 Mbps | 16.4 Mbps | 57 | 6.0 d | 2weeks |
| 6 | `public-vpn-228` | 🇯🇵 JP | 2,701,698 | 102.5 Mbps | 1.6 Mbps | 58 | 6.0 d | 2weeks |
| 7 | `public-vpn-196` | 🇯🇵 JP | 2,679,699 | 701.4 Mbps | 3.0 Mbps | 77 | 126.6 d | 2weeks |
| 8 | `public-vpn-82` | 🇯🇵 JP | 2,529,472 | 136.8 Mbps | 4.3 Mbps | 72 | 5.6 d | 2weeks |
| 9 | `public-vpn-186` | 🇯🇵 JP | 2,504,954 | 168.1 Mbps | 11.8 Mbps | 184 | 7.6 d | 2weeks |
| 10 | `public-vpn-197` | 🇯🇵 JP | 2,484,860 | 105.0 Mbps | 2.6 Mbps | 102 | 7.3 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 839 | 435 | 25.6 Mbps | `vpn325696545` |
| 🇰🇷 Korea Republic of (KR) | 622 | 344 | 20.9 Mbps | `vpn676301515` |
| 🇷🇺 Russian Federation (RU) | 137 | 5 | 16.0 Mbps | `vpn569153955` |
| 🇹🇭 Thailand (TH) | 133 | 20 | 14.7 Mbps | `vpn622921954` |
| 🇺🇸 United States (US) | 51 | 7 | 20.4 Mbps | `vpn615343043` |
| 🇻🇳 Viet Nam (VN) | 33 | 11 | 10.9 Mbps | `vpn268153810` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 13 | 9 | 0.9 Mbps | `vpn192906546` |
| 🇲🇽 Mexico (MX) | 8 | 2 | 21.5 Mbps | `cetsssa` |
| 🇦🇷 Argentina (AR) | 5 | 1 | 17.4 Mbps | `vpn510681258` |
| 🇮🇳 India (IN) | 5 | 1 | 7.3 Mbps | `vpn359610091` |
| 🇦🇺 Australia (AU) | 4 | 3 | 12.2 Mbps | `vpn727329064` |
| 🇨🇱 Chile (CL) | 4 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 3 | 1 | 2.6 Mbps | `vpn397851595` |
| 🇨🇴 Colombia (CO) | 3 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 3 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 3 | 0 | 0.0 Mbps | `` |
| 🇺🇦 Ukraine (UA) | 3 | 1 | 5.5 Mbps | `vpn313985146` |
| 🇦🇪 United Arab Emirates (AE) | 2 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 1 | 0.4 Mbps | `_unregistered_vpn952021746` |
| 🇩🇪 Germany (DE) | 2 | 1 | 0.8 Mbps | `vpn695737487` |
| 🇬🇧 United Kingdom (GB) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 2 | 7.3 Mbps | `vpn225804116` |
| 🇲🇲 Myanmar (MM) | 2 | 1 | 5.8 Mbps | `vpn192397778` |
| 🇧🇩 Bangladesh (BD) | 1 | 1 | 0.8 Mbps | `vpn342499472` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇾 Belarus (BY) | 1 | 1 | 13.2 Mbps | `vpn339361450` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇿 Czech Republic (CZ) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇪 Estonia (EE) | 1 | 1 | 10.1 Mbps | `vpn191465867` |
| 🇫🇮 Finland (FI) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 2.3 Mbps | `diamondgnd` |
| 🇭🇺 Hungary (HU) | 1 | 1 | 11.2 Mbps | `vpn273160004` |
| 🇮🇩 Indonesia (ID) | 1 | 1 | 7.5 Mbps | `vpn474625344` |
| 🇮🇷 Iran (ISLAMIC Republic Of) (IR) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇨 Saint Lucia (LC) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 13.2 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 1 | 0 | 0.0 Mbps | `` |
| … | +6 more countries | | | |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn699620341` | 🇰🇷 KR | 450 Mbps | 0.1 Mbps | 0% |
| `public-vpn-192` | 🇯🇵 JP | 257 Mbps | 0.1 Mbps | 0% |
| `vpn771151831` | 🇰🇷 KR | 44 Mbps | 0.1 Mbps | 0% |
| `vpn739981111` | 🇯🇵 JP | 118 Mbps | 0.2 Mbps | 0% |
| `vpn372176532` | 🇰🇷 KR | 332 Mbps | 0.5 Mbps | 0% |
| `public-vpn-241` | 🇯🇵 JP | 190 Mbps | 0.3 Mbps | 0% |
| `public-vpn-95` | 🇯🇵 JP | 1,304 Mbps | 2.6 Mbps | 0% |
| `vpn716109838` | 🇰🇷 KR | 624 Mbps | 1.2 Mbps | 0% |
| `public-vpn-198` | 🇯🇵 JP | 1,352 Mbps | 3.0 Mbps | 0% |
| `vpn910767930` | 🇯🇵 JP | 169 Mbps | 0.4 Mbps | 0% |

Most honest of this round: `vpn842523171` (15 Mbps), `vpn977456594` (15 Mbps), `vpn131652721` (13 Mbps), `vpn293598259` (15 Mbps), `vpn611780108` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.135.102` | 0.8 Mbps |
| `vpn191465867` | 🇪🇪 EE | 🇷🇺 RU | `109.252.78.71` | 10.1 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 0.8 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 0.8 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 0.8 Mbps |
| `vpn192397778` | 🇲🇲 MM | 🇮🇳 IN | `167.103.2.99` | 5.8 Mbps |
| `vpn913610646` | 🇺🇸 US | 🇭🇰 HK | `103.212.187.24` | 0.1 Mbps |
| `vpn192906546` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.16` | 0.9 Mbps |
| `vpn695737487` | 🇩🇪 DE | 🇫🇮 FI | `65.109.137.25` | 0.8 Mbps |
| `vpn232859084` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.21` | 0.8 Mbps |
| `vpn265277249` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.9` | 0.9 Mbps |
| `vpn430861125` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.10` | 0.8 Mbps |
| `vpn363342659` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.8` | 0.9 Mbps |
| `vpn256634230` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.22` | 0.9 Mbps |

## 📈 History

Alive % trend (last 26 runs): `██▇▆▆▁▄▅▄▄▄▁▂▃▄▂▃▄▁▂▄▁▂▄▁▃`

Avg measured speed (Mbps): `▆▇▁▇▂██▇▁▅▁▂▃▃▃▇▁▆▄▃▁▁▆▆▆▇`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-10-10 05:17:28 UTC | 100 | 730 | 40% | 11.8 | 83.3 | 11 |
| 2026-10-09 22:28:53 UTC | 96 | 481 | 27% | 11.6 | 28.6 | 11 |
| 2026-10-09 12:55:41 UTC | 94 | 772 | 45% | 11.3 | 94.1 | 9 |
| 2026-10-09 05:33:49 UTC | 95 | 636 | 38% | 11.8 | 42.6 | 6 |
| 2026-10-08 23:09:27 UTC | 97 | 449 | 28% | 9.0 | 36.8 | 6 |
| 2026-10-08 13:09:03 UTC | 93 | 687 | 44% | 8.5 | 28.1 | 8 |
| 2026-10-08 05:29:25 UTC | 96 | 566 | 38% | 9.9 | 96.0 | 7 |
| 2026-10-07 22:56:49 UTC | 94 | 418 | 29% | 10.6 | 32.7 | 8 |
| 2026-10-07 13:01:45 UTC | 98 | 605 | 44% | 11.4 | 64.9 | 4 |
| 2026-10-07 05:20:12 UTC | 97 | 523 | 40% | 9.0 | 49.2 | 5 |
| 2026-10-06 22:32:59 UTC | 93 | 425 | 34% | 11.8 | 102.0 | 5 |
| 2026-10-06 13:07:16 UTC | 99 | 577 | 48% | 9.6 | 21.3 | 7 |
| 2026-10-06 05:51:24 UTC | 97 | 466 | 41% | 9.7 | 48.3 | 6 |
| 2026-10-05 23:55:39 UTC | 91 | 372 | 34% | 10.1 | 56.0 | 6 |
| 2026-10-05 19:57:29 UTC | 94 | 328 | 32% | 9.2 | 44.0 | 4 |

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
*Auto-generated by [run #41](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/38051160764) at 2026-10-10 12:25:18 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
