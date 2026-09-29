"""Unit tests for the VPN Gate CSV parser / cleaner / deduper.

The sample row below is the exact example from the VPN Gate API docs
(the one provided in the repo brief), plus synthetic edge cases.
"""
import base64
import os
import re
import sys
from ipaddress import ip_address, ip_network

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "scripts"))
import common  # noqa: E402

MINI_CFG = "client\ndev tun\nproto udp\nremote 219.100.37.98 1453\n"
B64 = base64.b64encode(MINI_CFG.encode()).decode()


def sample_row():
    return [
        "public-vpn-108", "219.100.37.98", "3037443", "8", "815954222",
        "Japan", "JP", "121", "10929011737", "14960679", "952084324332490",
        "2weeks", "Daiyuu Nobori_ Japan. Academic Use", "", B64,
    ]


def sample_csv():
    header = ",".join(common.CSV_FIELDS)
    return (
        "*vpn_servers\r\n"
        f"#{header}\r\n"
        + ",".join(sample_row()) + "\r\n"
        "*\r\n"
    )


def test_parse_handles_markers_and_header():
    header, rows, malformed = common.parse_vpngate_csv(sample_csv())
    assert header[0] == "HostName"
    assert len(header) == 15
    assert len(rows) == 1
    assert malformed == 0
    assert rows[0][0] == "public-vpn-108"


def test_parse_counts_malformed_rows():
    text = sample_csv() + "broken-row-with,few,fields\n"
    _, rows, malformed = common.parse_vpngate_csv(text)
    assert len(rows) == 1
    assert malformed == 1


def test_clean_row_types_and_flags():
    d = common.clean_row(sample_row())
    assert d is not None
    assert d["Score"] == 3037443 and isinstance(d["Score"], int)
    assert d["Ping"] == 8
    assert d["Speed"] == 815954222
    assert d["CountryLong"] == "Japan"
    assert d["CountryShort"] == "JP"
    assert d["_config_ok"] is True


def test_clean_rejects_bad_ip_and_missing_host():
    row = sample_row()
    row[1] = "999.999.1.1"
    assert common.clean_row(row) is None
    row = sample_row()
    row[0] = ""
    assert common.clean_row(row) is None


def test_clean_rejects_non_numeric():
    row = sample_row()
    row[2] = "not-a-number"
    assert common.clean_row(row) is None


def test_valid_ipv4():
    assert common.valid_ipv4("219.100.37.98")
    assert not common.valid_ipv4("1.2.3")
    assert not common.valid_ipv4("a.b.c.d")
    assert not common.valid_ipv4("256.1.1.1")


def test_dedupe_exact_and_same_ip():
    a = common.clean_row(sample_row())
    b = common.clean_row(sample_row())          # exact duplicate
    c = common.clean_row(sample_row())          # same IP, different hostname
    c["HostName"] = "other-server"
    c["Score"] = a["Score"] - 1                 # lower score -> must lose
    d = common.clean_row(sample_row())          # unrelated server
    d["HostName"] = "another-one"
    d["IP"] = "1.2.3.4"
    kept, exact, same_ip = common.dedupe([a, b, c, d])
    assert len(kept) == 2
    assert exact == 1
    assert same_ip == 1
    assert {s["HostName"] for s in kept} == {"public-vpn-108", "another-one"}
    # the highest-scored survivor of an IP collision must be kept
    assert any(s["HostName"] == "public-vpn-108" for s in kept)


def test_country_flag():
    assert common.country_flag("JP") == "\U0001F1EF\U0001F1F5"
    assert common.country_flag("us") == "\U0001F1FA\U0001F1F8"
    assert common.country_flag("X1") == "\U0001F3F3"
    assert common.country_flag("") == "\U0001F3F3"


def test_worker_cf_ips_unique_and_inside_cloudflare_range():
    cf = ip_network("104.16.0.0/13")
    seen = set()
    for w in range(200):
        ips = common.worker_cf_ips(w)
        for ip in ips:
            assert ip_address(ip) in cf, f"{ip} outside Cloudflare range"
            assert ip not in seen, f"collision on {ip}"
            seen.add(ip)
        assert common.worker_tun(w) == f"tun{100 + w}"


def test_format_helpers():
    assert common.mbps(815954222) == "816.0"
    assert common.fmt_bytes(952084324332490) == "952.1 TB"
    assert common.fmt_uptime(10929011737) == "126.5 d"
    assert common.fmt_uptime(3_600_000) == "1.0 h"


def test_spark():
    assert common.spark([]) == ""
    assert common.spark([5, 5, 5]) == "▄▄▄"
    assert len(common.spark([1, 2, 3, 4, 5])) == 5


def test_prune_and_history_roundtrip(tmp_path):
    d = tmp_path / "archive"
    d.mkdir()
    for i in range(5):
        (d / f"vpngate_2026010{i}_0000.csv.gz").write_bytes(b"x")
    removed = common.prune_archive(str(d), keep=3)
    assert removed == 2
    assert len(list(d.iterdir())) == 3

    h = tmp_path / "history.jsonl"
    common.write_history(str(h), [{"a": 1}, {"a": 2}])
    assert common.read_history(str(h), cap=10) == [{"a": 1}, {"a": 2}]


def test_extract_proto_port_and_template():
    cfg = (
        "client\n\ndev tun\n\nproto tcp\n\nremote 219.100.37.98 443\n\n"
        "cipher AES-128-CBC\nauth SHA1\n\n<ca>\n-----BEGIN CERTIFICATE-----\n"
        "AAAA\n-----END CERTIFICATE-----\n</ca>\n"
    )
    proto, port = common.extract_proto_port(cfg)
    assert (proto, port) == ("tcp", 443)

    tpl = common.extract_template(cfg)
    assert "remote 219.100.37.98" not in tpl
    assert not re.search(r"(?mi)^\s*proto\s+\S+\s*$", tpl)
    assert "BEGIN CERTIFICATE" in tpl  # shared certs survive

    rebuilt = common.build_config_from_template(tpl, "udp", "1.2.3.4", 1194)
    assert "proto udp" in rebuilt
    assert "remote 1.2.3.4 1194" in rebuilt
    assert "BEGIN CERTIFICATE" in rebuilt
    # rebuilding for a different server keeps nothing of the old endpoint
    assert "219.100.37.98" not in rebuilt


def test_registry_update_prune_and_plan():
    reg = {}
    s = common.clean_row(sample_row())
    s["_proto"], s["_port"] = "tcp", 443
    common.update_registry(reg, [s], "2026-01-01T00:00:00Z")
    assert len(reg) == 1
    e = next(iter(reg.values()))
    assert e["port"] == 443 and e["proto"] == "tcp"
    assert e["first_seen"] == "2026-01-01T00:00:00Z"

    common.update_registry(reg, [s], "2026-01-02T00:00:00Z")
    assert next(iter(reg.values()))["occurrences"] == 2
    assert next(iter(reg.values()))["last_seen"] == "2026-01-02T00:00:00Z"

    plan = common.build_test_plan(reg, [])
    assert len(plan) == 1
    assert plan[0]["in_current_list"] is False
    assert plan[0]["port"] == 443

    plan2 = common.build_test_plan(reg, [{"HostName": s["HostName"],
                                          "IP": s["IP"]}])
    assert plan2[0]["in_current_list"] is True

    # entries without endpoints never make it into the plan
    reg["ghost|5.6.7.8"] = {"HostName": "ghost", "IP": "5.6.7.8"}
    assert len(common.build_test_plan(reg, [])) == 1

    # prune: recall_days=0 -> cutoff now -> the 2026-01-02 entry is stale
    dropped = common.prune_registry(reg, recall_days=0, cap=100)
    assert dropped == 2
    assert reg == {}


def test_build_config_for_worker():
    import test_vpns
    cfg_text = (
        "client\n\ndev tun\n\nproto tcp\n\nremote 9.9.9.9 443\n\n"
        "<ca>\n-----BEGIN CERTIFICATE-----\nAAAA\n-----END CERTIFICATE-----\n</ca>\n"
    )
    tpl = common.extract_template(cfg_text)
    cfg = test_vpns.build_config(tpl, "tcp", "1.2.3.4", 443, 7, (2, 6))
    assert "dev tun107" in cfg                      # per-worker tun device
    assert "remote 1.2.3.4 443" in cfg
    assert not re.search(r"(?mi)^dev tun$", cfg)     # original dev replaced
    assert "route-nopull" in cfg                     # runner route protected
    assert "route 104.16.7.4 255.255.255.255" in cfg  # pinned CF anycast /32
    assert "route 104.17.7.4 255.255.255.255" in cfg
    assert "data-ciphers-fallback AES-128-CBC" in cfg
    assert "tls-cipher DEFAULT:@SECLEVEL=0" in cfg
    assert "BEGIN CERTIFICATE" in cfg                # shared certs intact


def test_public_csv_has_endpoint_columns(tmp_path):
    s = common.clean_row(sample_row())
    s["_proto"], s["_port"] = "tcp", 443
    p = tmp_path / "servers_clean.csv"
    common.write_public_csv(str(p), [s])
    text = p.read_text()
    assert text.splitlines()[0].endswith("Proto,Port")
    assert text.splitlines()[1].endswith(",tcp,443")
