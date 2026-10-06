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
| **Run** | [#27 · view run](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37391197338) · 2026-10-05 23:55:39 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **91** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **1,079 of 1,079** — all 91 current + 988 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **372** — 60 from the current list + 312 historical ♻️ |
| **❌ Dead / unusable** | 707 |
| **Usability** | **65.9%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **10.1 / 11.9 / 56.0 Mbps** |
| **🚀 Fastest verified** | **vpn729038920** · 🇺🇸 United States · **56.0 Mbps** |
| **🧭 Exit-country mismatches** | 6 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.2 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn729038920` | 🇺🇸 United States | ♻️ historical | `38.49.242.56:1538`/tcp | 2.0s | **56.0 Mbps** | 96.5 Mbps | 1,872,287 |
| 2 | `vpn445617380` | 🇺🇸 United States | ♻️ historical | `47.153.119.84:1841`/tcp | 2.3s | **33.7 Mbps** | 66.9 Mbps | 2,047,890 |
| 3 | `vpn908512202` | 🇺🇸 United States | ♻️ historical | `162.224.160.11:1423`/tcp | 2.3s | **31.3 Mbps** | 0.0 Mbps | 730,079 |
| 4 | `vpn167234104` | 🇯🇵 Japan | ♻️ historical | `39.111.221.149:1195`/udp | 2.3s | **21.3 Mbps** | 910.0 Mbps | 640,816 |
| 5 | `vpn772780308` | 🇯🇵 Japan | 📋 current | `133.32.179.21:3724`/udp | 2.5s | **20.6 Mbps** | 370.0 Mbps | 1,034,009 |
| 6 | `vpn525554372` | 🇯🇵 Japan | ♻️ historical | `101.142.196.72:1612`/udp | 2.5s | **20.5 Mbps** | 333.3 Mbps | 637,125 |
| 7 | `vpn736046374` | 🇯🇵 Japan | ♻️ historical | `92.202.136.79:1497`/udp | 2.5s | **20.4 Mbps** | 501.0 Mbps | 1,394,745 |
| 8 | `vpn551800667` | 🇯🇵 Japan | ♻️ historical | `111.234.191.130:1387`/udp | 2.5s | **20.4 Mbps** | 356.6 Mbps | 604,619 |
| 9 | `vpn165481165` | 🇯🇵 Japan | ♻️ historical | `133.149.94.50:1877`/udp | 2.3s | **19.3 Mbps** | 462.8 Mbps | 990,993 |
| 10 | `vpn693017146` | 🇯🇵 Japan | ♻️ historical | `218.131.41.95:1975`/udp | 2.5s | **19.0 Mbps** | 2,558.8 Mbps | 599,858 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-48` | 🇯🇵 JP | 3,016,353 | 949.2 Mbps | 13.3 Mbps | 107 | 126.5 d | 2weeks |
| 2 | `public-vpn-72` | 🇯🇵 JP | 2,981,318 | 602.0 Mbps | 13.9 Mbps | 143 | 126.5 d | 2weeks |
| 3 | `public-vpn-145` | 🇯🇵 JP | 2,779,767 | 396.3 Mbps | 13.0 Mbps | 42 | 128.6 d | 2weeks |
| 4 | `public-vpn-66` | 🇯🇵 JP | 2,758,587 | 393.6 Mbps | 12.5 Mbps | 109 | 126.6 d | 2weeks |
| 5 | `public-vpn-155` | 🇯🇵 JP | 2,714,026 | 349.5 Mbps | 13.7 Mbps | 44 | 126.6 d | 2weeks |
| 6 | `public-vpn-196` | 🇯🇵 JP | 2,679,699 | 701.4 Mbps | 2.5 Mbps | 77 | 126.6 d | 2weeks |
| 7 | `public-vpn-206` | 🇯🇵 JP | 2,311,114 | 530.4 Mbps | 1.8 Mbps | 75 | 128.6 d | 2weeks |
| 8 | `public-vpn-152` | 🇯🇵 JP | 2,193,574 | 313.7 Mbps | 12.6 Mbps | 167 | 126.5 d | 2weeks |
| 9 | `public-vpn-215` | 🇯🇵 JP | 2,075,683 | 403.0 Mbps | 6.0 Mbps | 32 | 127.6 d | 2weeks |
| 10 | `vpn445617380` | 🇺🇸 US | 2,047,890 | 66.9 Mbps | 33.7 Mbps | 67 | 0.0 h | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 498 | 213 | 21.3 Mbps | `vpn167234104` |
| 🇰🇷 Korea Republic of (KR) | 326 | 110 | 16.6 Mbps | `vpn767479473` |
| 🇹🇭 Thailand (TH) | 77 | 8 | 13.4 Mbps | `vpn367019110` |
| 🇷🇺 Russian Federation (RU) | 75 | 3 | 12.9 Mbps | `vpn811012363` |
| 🇺🇸 United States (US) | 30 | 11 | 56.0 Mbps | `vpn729038920` |
| 🇻🇳 Viet Nam (VN) | 22 | 5 | 11.2 Mbps | `vpn381476084` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 6 | 4 | 1.1 Mbps | `vpn981204829` |
| 🇲🇽 Mexico (MX) | 5 | 0 | 0.0 Mbps | `` |
| 🇦🇷 Argentina (AR) | 4 | 2 | 17.6 Mbps | `vpn412340960` |
| 🇮🇳 India (IN) | 4 | 1 | 8.3 Mbps | `vpn359610091` |
| 🇨🇱 Chile (CL) | 3 | 1 | 15.1 Mbps | `vpn690784060` |
| 🇨🇦 Canada (CA) | 2 | 1 | 7.1 Mbps | `vpn779606145` |
| 🇨🇳 China (CN) | 2 | 2 | 6.0 Mbps | `_unregistered_vpn952021746` |
| 🇨🇴 Colombia (CO) | 2 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 2 | 2 | 13.0 Mbps | `vpn890210379` |
| 🇲🇲 Myanmar (MM) | 2 | 1 | 1.3 Mbps | `vpn192397778` |
| 🇵🇪 Peru (PE) | 2 | 0 | 0.0 Mbps | `` |
| 🇺🇦 Ukraine (UA) | 2 | 1 | 13.9 Mbps | `vpn313985146` |
| 🇦🇪 United Arab Emirates (AE) | 1 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 1 | 1 | 5.1 Mbps | `vpn562825704` |
| 🇧🇪 Belgium (BE) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 1 | 1 | 7.3 Mbps | `vpn564048942` |
| 🇨🇭 Switzerland (CH) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇿 Czech Republic (CZ) | 1 | 1 | 7.7 Mbps | `vpn809432043` |
| 🇪🇨 Ecuador (EC) | 1 | 1 | 16.5 Mbps | `vpn714667264` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 8.8 Mbps | `diamondgnd` |
| 🇭🇰 Hong Kong (HK) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇷 Iran (ISLAMIC Republic Of) (IR) | 1 | 0 | 0.0 Mbps | `` |
| 🇱🇹 Lithuania (LT) | 1 | 1 | 13.9 Mbps | `vpn539804093` |
| 🇱🇺 Luxembourg (LU) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 1 | 1 | 5.9 Mbps | `vpn713264157` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn110060260` | 🇯🇵 JP | 189 Mbps | 0.1 Mbps | 0% |
| `vpn517964018` | 🇰🇷 KR | 59 Mbps | 0.1 Mbps | 0% |
| `vpn677403438` | 🇺🇸 US | 158 Mbps | 0.1 Mbps | 0% |
| `vpn771151831` | 🇰🇷 KR | 44 Mbps | 0.0 Mbps | 0% |
| `vpn605991753` | 🇰🇷 KR | 372 Mbps | 0.4 Mbps | 0% |
| `vpn981288372` | 🇯🇵 JP | 139 Mbps | 0.2 Mbps | 0% |
| `vpn779820187` | 🇯🇵 JP | 831 Mbps | 1.2 Mbps | 0% |
| `public-vpn-157` | 🇯🇵 JP | 4,732 Mbps | 13.1 Mbps | 0% |
| `vpn750532477` | 🇺🇸 US | 69 Mbps | 0.2 Mbps | 0% |
| `vpn859005905` | 🇰🇷 KR | 108 Mbps | 0.3 Mbps | 0% |

Most honest of this round: `vpn474602972` (10 Mbps), `vpn510681258` (12 Mbps), `vpn346537516` (13 Mbps), `vpn131652721` (11 Mbps), `vpn313985146` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `vpn962496160` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.24` | 0.4 Mbps |
| `vpn429922709` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.7` | 1.0 Mbps |
| `vpn801372263` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.13` | 1.0 Mbps |
| `vpn981204829` | 🇭🇷 HR | 🇧🇬 BG | `150.40.105.12` | 1.1 Mbps |
| `vpn192397778` | 🇲🇲 MM | 🇮🇳 IN | `167.103.2.119` | 1.3 Mbps |
| `neko69` | 🇬🇧 GB | 🇵🇱 PL | `31.59.137.26` | 1.2 Mbps |

## 📈 History

Alive % trend (last 12 runs): `██▇▆▆▁▄▅▄▃▄▁`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▂`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
*Auto-generated by [run #27](https://github.com/G1010yzd10/vpngate-monitor/actions/runs/37391197338) at 2026-10-06 00:02:53 UTC. Next scheduled run: every 6h (00:00 / 06:00 / 12:00 / 18:00 UTC).*
