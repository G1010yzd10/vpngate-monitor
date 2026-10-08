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
| **Run** | [#35 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37782060596) · 2026-10-08 13:09:03 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **93** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **1,544 of 1,544** — all 93 current + 1,451 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **687** — 66 from the current list + 621 historical ♻️ |
| **❌ Dead / unusable** | 857 |
| **Usability** | **71.0%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **8.5 / 9.8 / 28.1 Mbps** |
| **🚀 Fastest verified** | **vpn445617380** · 🇺🇸 United States · **28.1 Mbps** |
| **🧭 Exit-country mismatches** | 8 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.2 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn445617380` | 🇺🇸 United States | ♻️ historical | `47.153.119.84:1841`/tcp | 2.3s | **28.1 Mbps** | 66.9 Mbps | 2,047,890 |
| 2 | `vpn268164757` | 🇺🇦 Ukraine | ♻️ historical | `5.58.0.221:1195`/udp | 2.3s | **22.5 Mbps** | 95.5 Mbps | 703,315 |
| 3 | `vpn510681258` | 🇦🇷 Argentina | ♻️ historical | `181.117.92.157:3997`/udp | 2.5s | **20.3 Mbps** | 219.8 Mbps | 862,253 |
| 4 | `vpn452876228` | 🇷🇺 Russian Federation | 📋 current | `91.245.139.241:1554`/udp | 2.5s | **20.3 Mbps** | 33.7 Mbps | 580,924 |
| 5 | `vpn679218486` | 🇯🇵 Japan | ♻️ historical | `124.209.226.195:1752`/udp | 2.5s | **18.4 Mbps** | 686.9 Mbps | 597,704 |
| 6 | `vpn169318955` | 🇯🇵 Japan | ♻️ historical | `138.64.86.41:52295`/udp | 2.5s | **17.9 Mbps** | 467.0 Mbps | 599,413 |
| 7 | `vpn325696545` | 🇯🇵 Japan | ♻️ historical | `39.111.138.50:1195`/udp | 2.5s | **17.8 Mbps** | 728.3 Mbps | 362,807 |
| 8 | `vpn381887891` | 🇯🇵 Japan | ♻️ historical | `120.75.89.149:1355`/udp | 2.5s | **17.5 Mbps** | 935.4 Mbps | 723,708 |
| 9 | `vpn909153861` | 🇯🇵 Japan | ♻️ historical | `138.64.96.118:14355`/udp | 2.5s | **17.2 Mbps** | 292.9 Mbps | 1,237,377 |
| 10 | `vpn672056740` | 🇸🇪 Sweden | 📋 current | `94.254.62.140:51438`/udp | 2.5s | **16.9 Mbps** | 14.2 Mbps | 430,177 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `vpn918840683` | 🇺🇸 US | 4,066,296 | 348.6 Mbps | 9.5 Mbps | 208 | 22.9 d | 2weeks |
| 2 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 10.6 Mbps | 143 | 126.5 d | 2weeks |
| 3 | `public-vpn-136` | 🇯🇵 JP | 2,804,989 | 557.6 Mbps | 10.0 Mbps | 27 | 126.6 d | 2weeks |
| 4 | `public-vpn-182` | 🇯🇵 JP | 2,781,744 | 1,013.3 Mbps | 4.5 Mbps | 119 | 129.6 d | 2weeks |
| 5 | `public-vpn-66` | 🇯🇵 JP | 2,758,587 | 393.6 Mbps | 9.8 Mbps | 109 | 126.6 d | 2weeks |
| 6 | `public-vpn-155` | 🇯🇵 JP | 2,714,026 | 349.5 Mbps | 10.6 Mbps | 44 | 126.6 d | 2weeks |
| 7 | `public-vpn-135` | 🇯🇵 JP | 2,601,645 | 333.1 Mbps | 10.5 Mbps | 89 | 128.6 d | 2weeks |
| 8 | `public-vpn-228` | 🇯🇵 JP | 2,371,862 | 120.8 Mbps | 1.9 Mbps | 63 | 5.6 d | 2weeks |
| 9 | `public-vpn-105` | 🇯🇵 JP | 2,337,056 | 163.2 Mbps | 7.4 Mbps | 90 | 5.6 d | 2weeks |
| 10 | `public-vpn-206` | 🇯🇵 JP | 2,311,114 | 530.4 Mbps | 1.0 Mbps | 75 | 128.6 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 689 | 354 | 18.4 Mbps | `vpn679218486` |
| 🇰🇷 Korea Republic of (KR) | 487 | 264 | 16.0 Mbps | `vpn922387505` |
| 🇷🇺 Russian Federation (RU) | 118 | 9 | 20.3 Mbps | `vpn452876228` |
| 🇹🇭 Thailand (TH) | 108 | 24 | 12.1 Mbps | `vpn719752522` |
| 🇺🇸 United States (US) | 45 | 3 | 28.1 Mbps | `vpn445617380` |
| 🇻🇳 Viet Nam (VN) | 29 | 9 | 9.9 Mbps | `vpn268153810` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 7 | 4 | 1.4 Mbps | `vpn801372263` |
| 🇲🇽 Mexico (MX) | 6 | 0 | 0.0 Mbps | `` |
| 🇦🇷 Argentina (AR) | 5 | 2 | 20.3 Mbps | `vpn510681258` |
| 🇮🇳 India (IN) | 5 | 1 | 3.6 Mbps | `vpn359610091` |
| 🇨🇱 Chile (CL) | 4 | 1 | 15.0 Mbps | `vpn548414740` |
| 🇨🇴 Colombia (CO) | 3 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 3 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 2 | 1 | 13.2 Mbps | `vpn564048942` |
| 🇨🇦 Canada (CA) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 1 | 0.3 Mbps | `_unregistered_vpn952021746` |
| 🇩🇪 Germany (DE) | 2 | 1 | 1.4 Mbps | `vpn695737487` |
| 🇫🇷 France (FR) | 2 | 1 | 4.9 Mbps | `vpn206344472` |
| 🇬🇧 United Kingdom (GB) | 2 | 1 | 1.5 Mbps | `neko69` |
| 🇲🇲 Myanmar (MM) | 2 | 0 | 0.0 Mbps | `` |
| 🇺🇦 Ukraine (UA) | 2 | 2 | 22.5 Mbps | `vpn268164757` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇿 Czech Republic (CZ) | 1 | 1 | 13.1 Mbps | `vpn809432043` |
| 🇪🇨 Ecuador (EC) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇮 Finland (FI) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 6.6 Mbps | `diamondgnd` |
| 🇭🇰 Hong Kong (HK) | 1 | 1 | 6.0 Mbps | `vpn986755484` |
| 🇭🇺 Hungary (HU) | 1 | 1 | 14.1 Mbps | `vpn273160004` |
| 🇮🇷 Iran (ISLAMIC Republic Of) (IR) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇨 Saint Lucia (LC) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 15.7 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 1 | 1 | 3.0 Mbps | `vpn878390428` |
| 🇵🇹 Portugal (PT) | 1 | 1 | 15.1 Mbps | `vpn554714541` |
| 🇷🇴 Romania (RO) | 1 | 1 | 1.2 Mbps | `opengw` |
| 🇸🇪 Sweden (SE) | 1 | 1 | 16.9 Mbps | `vpn672056740` |
| 🇹🇼 Taiwan (TW) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn981288372` | 🇯🇵 JP | 139 Mbps | 0.1 Mbps | 0% |
| `public-vpn-257` | 🇯🇵 JP | 562 Mbps | 0.6 Mbps | 0% |
| `public-vpn-157` | 🇯🇵 JP | 4,732 Mbps | 7.8 Mbps | 0% |
| `public-vpn-192` | 🇯🇵 JP | 312 Mbps | 0.5 Mbps | 0% |
| `vpn567810523` | 🇯🇵 JP | 47 Mbps | 0.1 Mbps | 0% |
| `public-vpn-206` | 🇯🇵 JP | 530 Mbps | 1.0 Mbps | 0% |
| `public-vpn-183` | 🇯🇵 JP | 571 Mbps | 1.1 Mbps | 0% |
| `vpn579453483` | 🇯🇵 JP | 103 Mbps | 0.2 Mbps | 0% |
| `vpn481575539` | 🇯🇵 JP | 395 Mbps | 0.9 Mbps | 0% |
| `vpn756321398` | 🇰🇷 KR | 268 Mbps | 0.7 Mbps | 0% |

Most honest of this round: `vpn977456594` (11 Mbps), `vpn293598259` (11 Mbps), `vpn611780108` (10 Mbps), `vpn690047693` (12 Mbps), `vpn672056740` (17 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.135.243` | 1.2 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 1.2 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 1.4 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 1.2 Mbps |
| `neko69` | 🇬🇧 GB | 🇵🇱 PL | `31.59.137.26` | 1.5 Mbps |
| `vpn913610646` | 🇺🇸 US | 🇭🇰 HK | `103.212.187.24` | 0.3 Mbps |
| `vpn192906546` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.16` | 1.3 Mbps |
| `vpn695737487` | 🇩🇪 DE | 🇫🇮 FI | `65.109.137.25` | 1.4 Mbps |

## 📈 History

Alive % trend (last 20 runs): `██▇▆▆▁▄▅▄▃▄▁▂▃▄▂▃▃▁▂`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▂▃▂▂▆▁▆▄▃`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-10-08 05:29:25 UTC | 96 | 566 | 38% | 9.9 | 96.0 | 7 |
| 2026-10-07 22:56:49 UTC | 94 | 418 | 29% | 10.6 | 32.7 | 8 |
| 2026-10-07 13:01:45 UTC | 98 | 605 | 44% | 11.4 | 64.9 | 4 |
| 2026-10-07 05:20:12 UTC | 97 | 523 | 40% | 9.0 | 49.2 | 5 |
| 2026-10-06 22:32:59 UTC | 93 | 425 | 34% | 11.8 | 102.0 | 5 |
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
*Auto-generated by [run #35](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37782060596) at 2026-10-08 13:19:03 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
