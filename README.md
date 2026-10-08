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
| **Run** | [#36 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37857788552) · 2026-10-08 23:09:27 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **97** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **1,610 of 1,610** — all 97 current + 1,513 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **449** — 39 from the current list + 410 historical ♻️ |
| **❌ Dead / unusable** | 1,161 |
| **Usability** | **40.2%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **9.0 / 10.2 / 36.8 Mbps** |
| **🚀 Fastest verified** | **vpn677403438** · 🇺🇸 United States · **36.8 Mbps** |
| **🧭 Exit-country mismatches** | 6 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.2 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn677403438` | 🇺🇸 United States | ♻️ historical | `98.169.175.14:1988`/tcp | 2.0s | **36.8 Mbps** | 157.6 Mbps | 1,851,456 |
| 2 | `vpn526181119` | 🇺🇸 United States | ♻️ historical | `46.110.212.225:4822`/udp | 2.0s | **30.6 Mbps** | 399.4 Mbps | 1,470,909 |
| 3 | `vpn641734582` | 🇺🇸 United States | ♻️ historical | `47.198.109.135:1916`/tcp | 2.3s | **27.5 Mbps** | 42.0 Mbps | 1,925,593 |
| 4 | `vpn729038920` | 🇺🇸 United States | ♻️ historical | `38.49.242.56:1538`/tcp | 2.0s | **26.6 Mbps** | 96.5 Mbps | 1,872,287 |
| 5 | `vpn672056740` | 🇸🇪 Sweden | ♻️ historical | `94.254.62.140:51438`/udp | 2.3s | **25.5 Mbps** | 14.2 Mbps | 430,177 |
| 6 | `vpn908512202` | 🇺🇸 United States | ♻️ historical | `162.224.160.11:1423`/tcp | 2.3s | **23.2 Mbps** | 0.0 Mbps | 730,079 |
| 7 | `vpn510681258` | 🇦🇷 Argentina | ♻️ historical | `181.117.92.157:3997`/udp | 2.5s | **20.6 Mbps** | 219.8 Mbps | 862,253 |
| 8 | `vpn310756240` | 🇷🇺 Russian Federation | ♻️ historical | `46.242.8.30:20508`/udp | 2.5s | **19.9 Mbps** | 51.6 Mbps | 1,068,564 |
| 9 | `vpn554714541` | 🇵🇹 Portugal | ♻️ historical | `85.242.76.210:1591`/tcp | 2.5s | **19.6 Mbps** | 172.3 Mbps | 652,952 |
| 10 | `vpn705687526` | 🇯🇵 Japan | ♻️ historical | `147.192.42.21:1341`/udp | 2.8s | **18.4 Mbps** | 73.5 Mbps | 1,105,605 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 7.5 Mbps | 42 | 128.6 d | 2weeks |
| 2 | `public-vpn-155` | 🇯🇵 JP | 2,714,026 | 349.5 Mbps | 6.0 Mbps | 44 | 126.6 d | 2weeks |
| 3 | `public-vpn-134` | 🇯🇵 JP | 2,711,895 | 135.1 Mbps | 11.2 Mbps | 57 | 6.0 d | 2weeks |
| 4 | `public-vpn-228` | 🇯🇵 JP | 2,701,698 | 102.5 Mbps | 1.0 Mbps | 58 | 6.0 d | 2weeks |
| 5 | `public-vpn-135` | 🇯🇵 JP | 2,601,645 | 333.1 Mbps | 11.6 Mbps | 89 | 128.6 d | 2weeks |
| 6 | `public-vpn-197` | 🇯🇵 JP | 2,563,317 | 148.7 Mbps | 5.7 Mbps | 88 | 5.6 d | 2weeks |
| 7 | `public-vpn-152` | 🇯🇵 JP | 2,520,212 | 134.3 Mbps | 1.5 Mbps | 142 | 5.6 d | 2weeks |
| 8 | `public-vpn-258` | 🇯🇵 JP | 2,453,904 | 163.1 Mbps | 4.6 Mbps | 77 | 6.0 d | 2weeks |
| 9 | `public-vpn-261` | 🇯🇵 JP | 2,431,377 | 194.5 Mbps | 8.3 Mbps | 92 | 5.0 d | 2weeks |
| 10 | `public-vpn-111` | 🇯🇵 JP | 2,411,842 | 126.8 Mbps | 11.6 Mbps | 28 | 5.6 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 712 | 238 | 18.4 Mbps | `vpn705687526` |
| 🇰🇷 Korea Republic of (KR) | 516 | 158 | 16.6 Mbps | `vpn393322206` |
| 🇷🇺 Russian Federation (RU) | 121 | 4 | 19.9 Mbps | `vpn310756240` |
| 🇹🇭 Thailand (TH) | 113 | 9 | 11.4 Mbps | `vpn739493105` |
| 🇺🇸 United States (US) | 47 | 13 | 36.8 Mbps | `vpn677403438` |
| 🇻🇳 Viet Nam (VN) | 30 | 8 | 10.1 Mbps | `vpn268153810` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 7 | 4 | 1.3 Mbps | `vpn429922709` |
| 🇲🇽 Mexico (MX) | 6 | 0 | 0.0 Mbps | `` |
| 🇦🇷 Argentina (AR) | 5 | 2 | 20.6 Mbps | `vpn510681258` |
| 🇮🇳 India (IN) | 5 | 0 | 0.0 Mbps | `` |
| 🇨🇱 Chile (CL) | 4 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 3 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 3 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 3 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 2 | 1 | 13.6 Mbps | `vpn564048942` |
| 🇨🇦 Canada (CA) | 2 | 1 | 17.8 Mbps | `vpn779606145` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇩🇪 Germany (DE) | 2 | 1 | 1.4 Mbps | `vpn695737487` |
| 🇫🇷 France (FR) | 2 | 1 | 3.8 Mbps | `vpn206344472` |
| 🇬🇧 United Kingdom (GB) | 2 | 1 | 16.0 Mbps | `vpn890210379` |
| 🇲🇲 Myanmar (MM) | 2 | 0 | 0.0 Mbps | `` |
| 🇺🇦 Ukraine (UA) | 2 | 1 | 15.9 Mbps | `vpn313985146` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇿 Czech Republic (CZ) | 1 | 1 | 13.9 Mbps | `vpn809432043` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 17.2 Mbps | `vpn714667264` |
| 🇫🇮 Finland (FI) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 11.4 Mbps | `diamondgnd` |
| 🇭🇰 Hong Kong (HK) | 1 | 0 | 0.0 Mbps | `` |
| 🇭🇺 Hungary (HU) | 1 | 1 | 12.4 Mbps | `vpn273160004` |
| 🇮🇷 Iran (ISLAMIC Republic Of) (IR) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇨 Saint Lucia (LC) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 14.3 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 1 | 19.6 Mbps | `vpn554714541` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇸🇪 Sweden (SE) | 1 | 1 | 25.5 Mbps | `vpn672056740` |
| … | +1 more countries | | | |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn771151831` | 🇰🇷 KR | 44 Mbps | 0.0 Mbps | 0% |
| `public-vpn-157` | 🇯🇵 JP | 4,732 Mbps | 10.4 Mbps | 0% |
| `vpn946692838` | 🇯🇵 JP | 230 Mbps | 0.5 Mbps | 0% |
| `vpn756321398` | 🇰🇷 KR | 268 Mbps | 0.7 Mbps | 0% |
| `public-vpn-198` | 🇯🇵 JP | 1,352 Mbps | 3.5 Mbps | 0% |
| `public-vpn-202` | 🇯🇵 JP | 183 Mbps | 0.5 Mbps | 0% |
| `vpn682240449` | 🇰🇷 KR | 553 Mbps | 2.1 Mbps | 0% |
| `vpn171221818` | 🇯🇵 JP | 632 Mbps | 2.4 Mbps | 0% |
| `vpn579453483` | 🇯🇵 JP | 103 Mbps | 0.4 Mbps | 0% |
| `laud` | 🇯🇵 JP | 145 Mbps | 0.6 Mbps | 0% |

Most honest of this round: `vpn672056740` (25 Mbps), `vpn293598259` (11 Mbps), `vpn611780108` (10 Mbps), `vpn168250961` (11 Mbps), `vpn346537516` (11 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 1.3 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 0.8 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 1.1 Mbps |
| `vpn913610646` | 🇺🇸 US | 🇭🇰 HK | `103.212.187.24` | 0.3 Mbps |
| `vpn192906546` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.16` | 1.3 Mbps |
| `vpn695737487` | 🇩🇪 DE | 🇫🇮 FI | `65.109.137.25` | 1.4 Mbps |

## 📈 History

Alive % trend (last 21 runs): `██▇▆▆▁▄▅▄▃▄▁▂▃▄▂▃▃▁▂▃`

Avg measured speed (Mbps): `▆▇▁▇▂██▇▁▅▁▂▃▃▃▇▁▆▄▃▁`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
| 2026-10-05 14:10:31 UTC | 95 | 434 | 45% | 8.8 | 52.2 | 4 |
| 2026-10-05 05:01:08 UTC | 94 | 394 | 44% | 10.9 | 50.4 | 3 |
| 2026-10-03 16:01:20 UTC | 98 | 368 | 45% | 8.8 | 33.1 | 4 |
| 2026-10-03 11:25:01 UTC | 99 | 388 | 52% | 11.8 | 37.9 | 5 |
| 2026-10-03 04:45:33 UTC | 94 | 322 | 49% | 12.6 | 77.0 | 5 |

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
*Auto-generated by [run #36](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37857788552) at 2026-10-08 23:20:48 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
