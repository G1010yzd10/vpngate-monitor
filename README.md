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
| **Run** | [#12 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/36967078459) · 2026-10-02 05:01:43 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **97** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **504 of 504** — all 97 current + 407 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **289** — 79 from the current list + 210 historical ♻️ |
| **❌ Dead / unusable** | 215 |
| **Usability** | **81.4%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **9.1 / 10.4 / 54.4 Mbps** |
| **🚀 Fastest verified** | **vpn729038920** · 🇺🇸 United States · **54.4 Mbps** |
| **🧭 Exit-country mismatches** | 5 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.2 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn729038920` | 🇺🇸 United States | 📋 current | `38.49.242.56:1538`/tcp | 2.0s | **54.4 Mbps** | 96.5 Mbps | 1,872,287 |
| 2 | `vpn714667264` | 🇪🇨 Ecuador | ♻️ historical | `181.199.60.152:6165`/udp | 2.3s | **30.2 Mbps** | 164.5 Mbps | 1,160,113 |
| 3 | `vpn783399234` | 🇺🇸 United States | 📋 current | `50.0.119.51:995`/tcp | 2.3s | **28.5 Mbps** | 679.4 Mbps | 1,907,490 |
| 4 | `vpn445617380` | 🇺🇸 United States | ♻️ historical | `47.153.119.84:1841`/tcp | 2.3s | **25.9 Mbps** | 66.9 Mbps | 2,047,890 |
| 5 | `vpn118756292` | 🇺🇸 United States | ♻️ historical | `67.5.100.174:995`/tcp | 2.5s | **24.3 Mbps** | 392.0 Mbps | 2,119,917 |
| 6 | `vpn412340960` | 🇦🇷 Argentina | ♻️ historical | `186.12.228.57:12429`/udp | 6.8s | **19.7 Mbps** | 56.3 Mbps | 603,821 |
| 7 | `vpn525464003` | 🇦🇷 Argentina | 📋 current | `186.12.171.228:38819`/udp | 2.5s | **18.4 Mbps** | 47.7 Mbps | 608,097 |
| 8 | `vpn705687526` | 🇯🇵 Japan | ♻️ historical | `147.192.42.21:1195`/udp | 2.5s | **18.0 Mbps** | 83.0 Mbps | 628,061 |
| 9 | `vpn539804093` | 🇱🇹 Lithuania | ♻️ historical | `77.79.18.229:1974`/tcp | 2.8s | **17.0 Mbps** | 143.2 Mbps | 621,643 |
| 10 | `vpn616243951` | 🇯🇵 Japan | ♻️ historical | `112.139.83.36:1238`/udp | 2.5s | **16.9 Mbps** | 97.9 Mbps | 667,188 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 9.1 Mbps | 107 | 126.5 d | 2weeks |
| 2 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 11.4 Mbps | 143 | 126.5 d | 2weeks |
| 3 | `public-vpn-253` | 🇯🇵 JP | 2,897,255 | 465.0 Mbps | 1.6 Mbps | 103 | 128.6 d | 2weeks |
| 4 | `public-vpn-251` | 🇯🇵 JP | 2,889,525 | 334.3 Mbps | 3.6 Mbps | 94 | 129.6 d | 2weeks |
| 5 | `public-vpn-225` | 🇯🇵 JP | 2,839,678 | 256.7 Mbps | 1.4 Mbps | 76 | 128.6 d | 2weeks |
| 6 | `public-vpn-205` | 🇯🇵 JP | 2,834,021 | 383.7 Mbps | 0.5 Mbps | 92 | 127.6 d | 2weeks |
| 7 | `public-vpn-239` | 🇯🇵 JP | 2,829,899 | 392.6 Mbps | 6.3 Mbps | 38 | 126.6 d | 2weeks |
| 8 | `public-vpn-137` | 🇯🇵 JP | 2,811,720 | 1,442.8 Mbps | 7.0 Mbps | 153 | 126.5 d | 2weeks |
| 9 | `public-vpn-136` | 🇯🇵 JP | 2,804,989 | 557.6 Mbps | 11.8 Mbps | 27 | 126.6 d | 2weeks |
| 10 | `public-vpn-182` | 🇯🇵 JP | 2,781,744 | 1,013.3 Mbps | 6.0 Mbps | 119 | 129.6 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 259 | 168 | 18.0 Mbps | `vpn705687526` |
| 🇰🇷 Korea Republic of (KR) | 138 | 80 | 15.7 Mbps | `vpn767479473` |
| 🇹🇭 Thailand (TH) | 31 | 9 | 12.3 Mbps | `vpn622921954` |
| 🇷🇺 Russian Federation (RU) | 27 | 1 | 7.2 Mbps | `vpn254736373` |
| 🇺🇸 United States (US) | 18 | 10 | 54.4 Mbps | `vpn729038920` |
| 🇻🇳 Viet Nam (VN) | 6 | 5 | 10.4 Mbps | `vpn268153810` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 5 | 4 | 1.5 Mbps | `vpn429922709` |
| 🇦🇷 Argentina (AR) | 3 | 3 | 19.7 Mbps | `vpn412340960` |
| 🇨🇦 Canada (CA) | 2 | 1 | 2.7 Mbps | `vpn779606145` |
| 🇮🇳 India (IN) | 2 | 2 | 14.8 Mbps | `vpn213215154` |
| 🇲🇽 Mexico (MX) | 2 | 2 | 16.1 Mbps | `vpn764449825` |
| 🇵🇪 Peru (PE) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇱 Chile (CL) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 1 | 1 | 3.2 Mbps | `_unregistered_vpn335506854` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 30.2 Mbps | `vpn714667264` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 12.3 Mbps | `diamondgnd` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 17.0 Mbps | `vpn539804093` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn964630803` | 🇯🇵 JP | 1,829 Mbps | 0.9 Mbps | 0% |
| `vpn219941769` | 🇰🇷 KR | 772 Mbps | 0.7 Mbps | 0% |
| `public-vpn-205` | 🇯🇵 JP | 384 Mbps | 0.5 Mbps | 0% |
| `public-vpn-198` | 🇯🇵 JP | 962 Mbps | 1.6 Mbps | 0% |
| `public-vpn-184` | 🇯🇵 JP | 1,053 Mbps | 2.0 Mbps | 0% |
| `public-vpn-206` | 🇯🇵 JP | 530 Mbps | 1.1 Mbps | 0% |
| `public-vpn-214` | 🇯🇵 JP | 433 Mbps | 0.9 Mbps | 0% |
| `vpn481575539` | 🇯🇵 JP | 395 Mbps | 0.9 Mbps | 0% |
| `public-vpn-196` | 🇯🇵 JP | 701 Mbps | 1.8 Mbps | 0% |
| `public-vpn-195` | 🇯🇵 JP | 959 Mbps | 2.8 Mbps | 0% |

Most honest of this round: `vpn100779275` (10 Mbps), `_unregistered_vpn335506854` (3 Mbps), `vpn137812529` (12 Mbps), `vpn729038920` (54 Mbps), `cetsssa` (13 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpngateyunyoooscar` | 🇺🇸 US | 🇭🇰 HK | `70.39.207.220` | 0.7 Mbps |
| `vpn118469396` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.23` | 1.4 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 1.5 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 1.3 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 1.4 Mbps |

## 📈 History

Alive % trend (last 4 runs): `▇█▃▁`

Avg measured speed (Mbps): `▇█▁█`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
*Auto-generated by [run #12](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/36967078459) at 2026-10-02 05:04:42 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
