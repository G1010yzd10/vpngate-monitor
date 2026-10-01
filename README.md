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
| **Run** | [#9 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/36818709347) · 2026-10-01 05:13:27 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **96** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **422 of 422** — all 96 current + 326 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **248** — 74 from the current list + 174 historical ♻️ |
| **❌ Dead / unusable** | 174 |
| **Usability** | **77.1%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **12.0 / 13.6 / 73.6 Mbps** |
| **🚀 Fastest verified** | **vpn908512202** · 🇺🇸 United States · **73.6 Mbps** |
| **🧭 Exit-country mismatches** | 6 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.8 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn908512202` | 🇺🇸 United States | ♻️ historical | `162.224.160.11:1423`/tcp | 2.0s | **73.6 Mbps** | 0.0 Mbps | 730,079 |
| 2 | `vpn445617380` | 🇺🇸 United States | ♻️ historical | `47.153.119.84:1841`/tcp | 2.0s | **59.3 Mbps** | 66.9 Mbps | 2,047,890 |
| 3 | `vpn618163192` | 🇯🇵 Japan | ♻️ historical | `59.146.142.232:1341`/udp | 2.5s | **27.0 Mbps** | 201.1 Mbps | 700,761 |
| 4 | `vpn693017146` | 🇯🇵 Japan | ♻️ historical | `218.131.41.95:1975`/udp | 2.5s | **24.0 Mbps** | 2,558.8 Mbps | 599,858 |
| 5 | `vpn922387505` | 🇰🇷 Korea Republic of | ♻️ historical | `175.209.13.17:1195`/udp | 2.5s | **21.4 Mbps** | 86.3 Mbps | 891,936 |
| 6 | `vpn764449825` | 🇲🇽 Mexico | ♻️ historical | `201.142.133.52:1412`/tcp | 2.3s | **21.3 Mbps** | 39.7 Mbps | 612,996 |
| 7 | `vpn991364498` | 🇯🇵 Japan | 📋 current | `130.62.148.209:32061`/udp | 2.0s | **21.2 Mbps** | 328.7 Mbps | 602,214 |
| 8 | `vpn998856828` | 🇯🇵 Japan | ♻️ historical | `60.119.230.125:1644`/udp | 2.0s | **20.8 Mbps** | 78.9 Mbps | 1,401,260 |
| 9 | `vpn705687526` | 🇯🇵 Japan | ♻️ historical | `147.192.42.21:1195`/udp | 2.3s | **19.6 Mbps** | 83.0 Mbps | 628,061 |
| 10 | `vpn971336380` | 🇯🇵 Japan | 📋 current | `217.178.229.142:38435`/udp | 2.5s | **19.1 Mbps** | 35.3 Mbps | 694,358 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `vpn918840683` | 🇺🇸 US | 3,989,552 | 348.6 Mbps | 17.8 Mbps | 231 | 13.5 d | 2weeks |
| 2 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 14.8 Mbps | 107 | 126.5 d | 2weeks |
| 3 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 13.0 Mbps | 143 | 126.5 d | 2weeks |
| 4 | `public-vpn-201` | 🇯🇵 JP | 2,851,535 | 237.9 Mbps | 6.7 Mbps | 79 | 126.5 d | 2weeks |
| 5 | `public-vpn-225` | 🇯🇵 JP | 2,839,678 | 256.7 Mbps | 12.3 Mbps | 76 | 128.6 d | 2weeks |
| 6 | `public-vpn-205` | 🇯🇵 JP | 2,834,021 | 383.7 Mbps | 11.4 Mbps | 92 | 127.6 d | 2weeks |
| 7 | `public-vpn-137` | 🇯🇵 JP | 2,811,720 | 1,442.8 Mbps | 3.5 Mbps | 153 | 126.5 d | 2weeks |
| 8 | `public-vpn-136` | 🇯🇵 JP | 2,804,989 | 557.6 Mbps | 13.6 Mbps | 27 | 126.6 d | 2weeks |
| 9 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 16.9 Mbps | 42 | 128.6 d | 2weeks |
| 10 | `public-vpn-90` | 🇯🇵 JP | 2,772,770 | 403.2 Mbps | 14.4 Mbps | 165 | 126.5 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 222 | 138 | 27.0 Mbps | `vpn618163192` |
| 🇰🇷 Korea Republic of (KR) | 112 | 73 | 21.4 Mbps | `vpn922387505` |
| 🇹🇭 Thailand (TH) | 28 | 11 | 15.1 Mbps | `vpn241487766` |
| 🇷🇺 Russian Federation (RU) | 21 | 2 | 10.7 Mbps | `vpn531681209` |
| 🇺🇸 United States (US) | 11 | 6 | 73.6 Mbps | `vpn908512202` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 5 | 5 | 0.7 Mbps | `vpn178522347` |
| 🇻🇳 Viet Nam (VN) | 5 | 4 | 13.4 Mbps | `vpn268153810` |
| 🇦🇷 Argentina (AR) | 3 | 2 | 15.8 Mbps | `vpn525464003` |
| 🇨🇦 Canada (CA) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇱 Chile (CL) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 1 | 1 | 0.7 Mbps | `_unregistered_vpn335506854` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 14.4 Mbps | `vpn714667264` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 5.7 Mbps | `diamondgnd` |
| 🇮🇳 India (IN) | 1 | 1 | 4.1 Mbps | `vpn359610091` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 10.4 Mbps | `vpn539804093` |
| 🇲🇽 Mexico (MX) | 1 | 1 | 21.3 Mbps | `vpn764449825` |
| 🇷🇴 Romania (RO) | 1 | 1 | 2.2 Mbps | `opengw` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn219941769` | 🇰🇷 KR | 772 Mbps | 0.8 Mbps | 0% |
| `public-vpn-183` | 🇯🇵 JP | 1,355 Mbps | 2.9 Mbps | 0% |
| `public-vpn-137` | 🇯🇵 JP | 1,443 Mbps | 3.5 Mbps | 0% |
| `public-vpn-58` | 🇯🇵 JP | 1,056 Mbps | 2.8 Mbps | 0% |
| `vpn981204829` | 🇭🇷 HR | 205 Mbps | 0.6 Mbps | 0% |
| `vpn857437370` | 🇯🇵 JP | 675 Mbps | 2.2 Mbps | 0% |
| `public-vpn-257` | 🇯🇵 JP | 353 Mbps | 1.2 Mbps | 0% |
| `vpn178522347` | 🇭🇷 HR | 202 Mbps | 0.7 Mbps | 0% |
| `public-vpn-66` | 🇯🇵 JP | 394 Mbps | 1.5 Mbps | 0% |
| `vpn517964018` | 🇰🇷 KR | 78 Mbps | 0.3 Mbps | 0% |

Most honest of this round: `vpn763610422` (14 Mbps), `vpn408435278` (13 Mbps), `vpn445617380` (59 Mbps), `vpn832579312` (16 Mbps), `vpn145338946` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.135.243` | 2.2 Mbps |
| `vpn118469396` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.23` | 0.7 Mbps |
| `vpn178522347` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.17` | 0.7 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 0.7 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 0.7 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 0.6 Mbps |

## 📈 History

Alive % trend (last 3 runs): `▆█▁`

Avg measured speed (Mbps): `▇█▁`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
*Auto-generated by [run #9](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/36818709347) at 2026-10-01 05:15:48 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
