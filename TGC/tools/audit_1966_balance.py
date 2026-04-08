#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RULES_PATH = ROOT / "TGC/tools/1966_balance_rules.json"


class Reporter:
    def __init__(self) -> None:
        self.items: list[tuple[str, str]] = []

    def add(self, level: str, message: str) -> None:
        self.items.append((level, message))

    def dump(self) -> None:
        levels = ["FAIL", "WARN", "INFO"]
        counts = {k: 0 for k in levels}
        for lvl, _ in self.items:
            counts[lvl] = counts.get(lvl, 0) + 1

        print("1966 BALANCE AUDIT (diagnostic, non-blocking)")
        print(f" - FAIL: {counts.get('FAIL', 0)}")
        print(f" - WARN: {counts.get('WARN', 0)}")
        print(f" - INFO: {counts.get('INFO', 0)}")

        for lvl in levels:
            group = [msg for x, msg in self.items if x == lvl]
            if not group:
                continue
            print(f"\n[{lvl}]")
            for msg in group:
                print(f" - {msg}")


def infer_bucket(message: str) -> str:
    m = message.lower()
    if any(x in m for x in ["build_cost", "upkeep", "key goods", "economic ", "supply_cost"]):
        return "economic plausibility issues"
    if any(x in m for x in ["coverage", "unreadable year", "unknown monitored unit", "missing/unreadable", "cannot estimate"]):
        return "structural/data confidence issues"
    return "stat progression issues"


def extract_unit_and_subject(message: str) -> tuple[str, str]:
    m_colon = re.match(r"^([a-z0-9_]+):", message)
    if m_colon:
        return m_colon.group(1), "costs/data"
    m_pair = re.match(r"^([a-z0-9_]+)\s+([a-z0-9_]+)\b", message)
    if m_pair:
        return m_pair.group(1), m_pair.group(2)
    return "global", "audit"


def build_stat_tier_map(rules: dict[str, Any], monitored_stats: set[str]) -> dict[str, str]:
    stat_tiers_cfg: dict[str, list[str]] = rules.get("stat_tiers", {})
    tier_by_stat: dict[str, str] = {}
    for tier_name in ("primary", "secondary", "structural"):
        for s in stat_tiers_cfg.get(tier_name, []):
            tier_by_stat[s] = tier_name
    for s in monitored_stats:
        tier_by_stat.setdefault(s, "secondary")
    return tier_by_stat


def get_stat_signal_quality(assignments: int, units_with_signal: int) -> str:
    if assignments == 0:
        return "formal_coverage_only"
    if assignments < 8 or units_with_signal < 2:
        return "limited_signal"
    return "strong_signal"


def build_priority_summary(
    items: list[tuple[str, str]],
    units_cfg: dict[str, Any],
    tier_by_unit: dict[str, str],
    tier_by_stat: dict[str, str],
    stat_signal_quality: dict[str, str],
    stat_priority_weights: dict[str, Any],
) -> tuple[dict[str, list[tuple[int, str]]], list[tuple[int, str]]]:
    buckets: dict[str, list[tuple[int, str]]] = {
        "structural/data confidence issues": [],
        "stat progression issues": [],
        "economic plausibility issues": [],
    }
    playtest_candidates: list[tuple[int, str]] = []

    for level, msg in items:
        if level not in {"FAIL", "WARN"}:
            continue
        unit, subject = extract_unit_and_subject(msg)
        bucket = infer_bucket(msg)
        base = 100 if level == "FAIL" else 60
        score = base

        important_stats = set(units_cfg.get(unit, {}).get("important_stats", []))
        tier = tier_by_unit.get(unit, "secondary")
        if tier == "core":
            score += 20
        elif tier == "secondary":
            score += 5
        elif tier == "low_signal":
            score -= 15
        stat_tier = tier_by_stat.get(subject, "secondary")
        tier_weights = stat_priority_weights.get("tier", {})
        signal_weights = stat_priority_weights.get("signal", {})
        score += int(tier_weights.get(stat_tier, 0))
        signal_quality = stat_signal_quality.get(subject, "limited_signal")
        score += int(signal_weights.get(signal_quality, 0))
        if subject in important_stats:
            score += 20
        if "high-confidence coverage" in msg or "low timeline coverage" in msg:
            score += 15
        if "outside final_range" in msg or "milestone" in msg or "cumulative" in msg:
            score += 10
        if "build_cost outside range" in msg or "upkeep_cost outside range" in msg:
            score += 15

        short = (
            f"{unit} | unit_tier={tier} | stat_tier={stat_tier} | stat_signal={signal_quality} | "
            f"{subject} | {msg} | {level}"
        )
        buckets[bucket].append((score, short))
        structural_warn_floor = int(stat_priority_weights.get("structural_warn_focus_score_min", 100))
        if bucket != "structural/data confidence issues" and not (tier == "low_signal" and level == "WARN"):
            if level == "WARN" and signal_quality == "formal_coverage_only":
                continue
            if level == "WARN" and stat_tier == "structural" and score < structural_warn_floor:
                continue
            playtest_candidates.append((score, f"{unit}: {subject} -> {msg}"))

    for k in buckets:
        buckets[k].sort(key=lambda x: x[0], reverse=True)
    playtest_candidates.sort(key=lambda x: x[0], reverse=True)
    return buckets, playtest_candidates[:5]


def read_text(rel_path: str, encoding: str = "utf-8") -> str:
    return (ROOT / rel_path).read_text(encoding=encoding, errors="ignore")


def read_rules() -> dict[str, Any]:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def get_final_range(stat_cfg: dict[str, Any]) -> tuple[float | None, float | None]:
    final_cfg = stat_cfg.get("final_range", {})
    if not isinstance(final_cfg, dict):
        return None, None
    return final_cfg.get("min"), final_cfg.get("max")


def get_historical_relevance_start_year(unit_cfg: dict[str, Any], default_year: int) -> int:
    value = unit_cfg.get("historical_relevance_start_year", default_year)
    try:
        year = int(value)
    except (TypeError, ValueError):
        return default_year
    return max(year, default_year)


def parse_goods_costs(rel_path: str) -> dict[str, float]:
    text = read_text(rel_path)
    costs: dict[str, float] = {}
    current: str | None = None
    for line in text.splitlines():
        m_open = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*(?:#.*)?$", line)
        if m_open:
            current = m_open.group(1)
            continue
        if current:
            m_cost = re.match(r"\s*cost\s*=\s*([0-9.]+)", line)
            if m_cost:
                costs[current] = float(m_cost.group(1))
            if line.strip() == "}":
                current = None
    return costs


def parse_unit_block(unit_file: str, unit_key: str) -> dict[str, Any]:
    lines = read_text(unit_file).splitlines()
    data: dict[str, Any] = {"stats": {}, "build_cost": {}, "supply_cost": {}, "unit_domain": None}

    i = 0
    while i < len(lines):
        if re.match(rf"\s*{re.escape(unit_key)}\s*=\s*\{{\s*$", lines[i]):
            depth = 1
            i += 1
            mode: str | None = None
            while i < len(lines) and depth > 0:
                cur = lines[i]
                stripped = cur.strip()

                if re.match(r"\s*build_cost\s*=\s*\{", cur):
                    mode = "build"
                    i += 1
                    continue
                if re.match(r"\s*supply_cost\s*=\s*\{", cur):
                    mode = "supply"
                    i += 1
                    continue

                if mode and stripped == "}":
                    mode = None
                    i += 1
                    continue

                if mode == "build" or mode == "supply":
                    m = re.match(r"\s*([a-z0-9_]+)\s*=\s*([-0-9.]+)", cur)
                    if m:
                        if mode == "build":
                            data["build_cost"][m.group(1)] = float(m.group(2))
                        else:
                            data["supply_cost"][m.group(1)] = float(m.group(2))
                else:
                    m_type = re.match(r"\s*type\s*=\s*([a-z_]+)\b", cur)
                    if m_type:
                        data["unit_domain"] = m_type.group(1)
                    m_stat = re.match(r"\s*([a-z0-9_]+)\s*=\s*([-0-9.]+)\s*(?:#.*)?$", cur)
                    if m_stat:
                        data["stats"][m_stat.group(1)] = float(m_stat.group(2))

                depth += cur.count("{") - cur.count("}")
                i += 1
            return data
        i += 1

    return data


def estimate_costs(cost_block: dict[str, float], goods_costs: dict[str, float]) -> tuple[float | None, list[str], list[tuple[str, float]]]:
    missing_goods = [g for g in cost_block if g not in goods_costs]
    if missing_goods:
        return None, missing_goods, []

    contributions = [(g, cost_block[g] * goods_costs[g]) for g in cost_block]
    contributions.sort(key=lambda x: x[1], reverse=True)
    estimated = sum(v for _, v in contributions)
    return estimated, [], contributions[:3]


def infer_block_year(block_lines: list[tuple[int, str]]) -> int | None:
    for _, line in block_lines:
        m_year = re.match(r"\s*year\s*=\s*(\d{4})\b", line)
        if m_year:
            return int(m_year.group(1))
    return None


def parse_top_level_blocks(rel_path: str) -> dict[str, list[tuple[int, str]]]:
    lines = read_text(rel_path).splitlines()
    blocks: dict[str, list[tuple[int, str]]] = {}
    i = 0
    while i < len(lines):
        m_open = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*$", lines[i])
        if not m_open:
            i += 1
            continue
        key = m_open.group(1)
        depth = 1
        i += 1
        block: list[tuple[int, str]] = []
        while i < len(lines) and depth > 0:
            block.append((i + 1, lines[i]))
            depth += lines[i].count("{") - lines[i].count("}")
            i += 1
        blocks[key] = block
    return blocks


def extract_year_refs(block_lines: list[tuple[int, str]]) -> set[str]:
    refs: set[str] = set()
    for _, line in block_lines:
        m_inv = re.findall(r"\binvention\s*=\s*([a-z0-9_]+)\b", line)
        refs.update(m_inv)
        m_flag = re.findall(r"\b([a-z0-9_]+)\s*=\s*1\b", line)
        refs.update(m_flag)
    return refs


def extract_limit_year_refs(block_lines: list[tuple[int, str]]) -> set[str]:
    refs: set[str] = set()
    in_limit = False
    depth = 0
    for _, line in block_lines:
        if not in_limit and re.match(r"\s*limit\s*=\s*\{\s*$", line):
            in_limit = True
            depth = 1
            continue
        if not in_limit:
            continue

        depth += line.count("{") - line.count("}")
        if "NOT" not in line:
            m_inv = re.findall(r"\binvention\s*=\s*([a-z0-9_]+)\b", line)
            refs.update(m_inv)
            m_flag = re.findall(r"\b([a-z0-9_]+)\s*=\s*1\b", line)
            refs.update(m_flag)
        if depth <= 0:
            in_limit = False
    return refs


def build_year_inference(scan_files: list[str]) -> tuple[dict[str, int], dict[str, str]]:
    all_blocks: dict[str, list[tuple[int, str]]] = {}
    for rel in scan_files:
        all_blocks.update(parse_top_level_blocks(rel))

    year_by_key: dict[str, int] = {}
    year_reason: dict[str, str] = {}
    unresolved = set(all_blocks.keys())

    for key in list(unresolved):
        direct = infer_block_year(all_blocks[key])
        if direct is not None:
            year_by_key[key] = direct
            year_reason[key] = "direct"
            unresolved.remove(key)

    changed = True
    while changed:
        changed = False
        for key in list(unresolved):
            refs_all = extract_year_refs(all_blocks[key])
            refs_limit = extract_limit_year_refs(all_blocks[key])
            candidate_refs = [r for r in refs_all if r in year_by_key]
            if not candidate_refs:
                continue

            limit_candidate_refs = [r for r in refs_limit if r in year_by_key]
            if limit_candidate_refs:
                inferred = max(year_by_key[r] for r in limit_candidate_refs)
                ref_reasons = [year_reason.get(r, "unknown") for r in limit_candidate_refs]
            else:
                inferred = max(year_by_key[r] for r in candidate_refs)
                ref_reasons = [year_reason.get(r, "unknown") for r in candidate_refs]

            if inferred:
                year_by_key[key] = inferred
                if all(x in ("direct", "inferred_strong") for x in ref_reasons):
                    year_reason[key] = "inferred_strong"
                else:
                    year_reason[key] = "inferred_weak"
                unresolved.remove(key)
                changed = True

    return year_by_key, year_reason


def parse_effect_unit_assignments(
    rel_path: str,
    monitored_units: set[str],
    monitored_stats: set[str],
    inferred_years: dict[str, int],
    year_reason: dict[str, str],
    global_scope_units: dict[str, set[str]],
) -> dict[str, list[dict[str, Any]]]:
    lines = read_text(rel_path).splitlines()
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)

    def append_assignment(
        target_unit: str,
        scope_key: str,
        scope_kind: str,
        stat: str,
        raw_val: str,
        line_no: int,
        invention: str,
        block_year: int | None,
        block_year_source: str | None,
    ) -> None:
        out[target_unit].append(
            {
                "source_file": rel_path,
                "invention": invention,
                "line": line_no,
                "stat": stat,
                "value": float(raw_val),
                "year": block_year,
                "year_source": block_year_source,
                "scope_key": scope_key,
                "scope_kind": scope_kind,
            }
        )

    def resolve_targets(scope_key: str) -> tuple[list[str], str] | None:
        if scope_key in monitored_units:
            return [scope_key], "unit"
        global_targets = sorted(global_scope_units.get(scope_key, set()))
        if global_targets:
            return global_targets, "global"
        return None

    i = 0
    while i < len(lines):
        inv_match = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*$", lines[i])
        if not inv_match:
            i += 1
            continue
        inv_key = inv_match.group(1)
        inv_depth = 1
        i += 1
        block: list[tuple[int, str]] = []
        while i < len(lines) and inv_depth > 0:
            block.append((i + 1, lines[i]))
            inv_depth += lines[i].count("{") - lines[i].count("}")
            i += 1

        block_year = infer_block_year(block)
        block_year_source = "direct" if block_year is not None else None
        if block_year is None and inv_key in inferred_years:
            block_year = inferred_years[inv_key]
            block_year_source = year_reason.get(inv_key, "inferred_weak")

        j = 0
        while j < len(block):
            ln3, t3 = block[j]

            m_inline = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{(.*)\}\s*$", t3)
            if m_inline:
                scope_key = m_inline.group(1)
                body = m_inline.group(2)
                resolved = resolve_targets(scope_key)
                if resolved is not None:
                    targets, scope_kind = resolved
                    for stat, raw_val in re.findall(r"([a-z0-9_]+)\s*=\s*([-0-9.]+)", body):
                        if stat in monitored_stats:
                            for target_unit in targets:
                                append_assignment(
                                    target_unit,
                                    scope_key,
                                    scope_kind,
                                    stat,
                                    raw_val,
                                    ln3,
                                    inv_key,
                                    block_year,
                                    block_year_source,
                                )
                j += 1
                continue

            m_scope = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*$", t3)
            if m_scope:
                scope_key = m_scope.group(1)
                resolved = resolve_targets(scope_key)
                if resolved is None:
                    j += 1
                    continue
                targets, scope_kind = resolved
                sub_depth = 1
                j += 1
                while j < len(block) and sub_depth > 0:
                    ln4, t4 = block[j]
                    m_stat = re.match(r"\s*([a-z0-9_]+)\s*=\s*([-0-9.]+)", t4)
                    if m_stat and m_stat.group(1) in monitored_stats:
                        for target_unit in targets:
                            append_assignment(
                                target_unit,
                                scope_key,
                                scope_kind,
                                m_stat.group(1),
                                m_stat.group(2),
                                ln4,
                                inv_key,
                                block_year,
                                block_year_source,
                            )
                    sub_depth += t4.count("{") - t4.count("}")
                    j += 1
                continue

            j += 1
    return out


def format_assignment_origin(item: dict[str, Any]) -> str:
    scope_key = item.get("scope_key") or "unknown_scope"
    scope_kind = item.get("scope_kind") or "unit"
    scope_txt = f"{scope_kind}:{scope_key}"
    return f"{scope_txt} in {item['source_file']}:{item['line']} ({item['invention']})"


def check_key_goods_availability(production_types_file: str, key_goods: list[str], rep: Reporter) -> None:
    txt = read_text(production_types_file)
    for g in key_goods:
        if re.search(rf"\boutput_goods\s*=\s*{re.escape(g)}\b", txt):
            rep.add("INFO", f"KEY GOODS mapping present in production types: {g}")
        else:
            rep.add("WARN", f"KEY GOODS missing production output mapping: {g}")


def main() -> int:
    rules = read_rules()
    rep = Reporter()

    units_cfg: dict[str, Any] = rules["units"]
    coverage_tiers_cfg: dict[str, list[str]] = rules.get("coverage_tiers", {})
    tier_by_unit: dict[str, str] = {}
    for tier_name in ("core", "secondary", "low_signal"):
        for u in coverage_tiers_cfg.get(tier_name, []):
            tier_by_unit[u] = tier_name
    for u in units_cfg:
        tier_by_unit.setdefault(u, "secondary")
    files_cfg: dict[str, str] = rules["files"]
    monitored_units = set(units_cfg.keys())
    discovered_units = {p.stem for p in (ROOT / "TGC/units").glob("*.txt")}
    unit_groups: dict[str, list[str]] = rules.get("unit_groups", {})
    coverage_cfg: dict[str, Any] = rules.get("timeline_coverage", {})
    coverage_warn_below = float(coverage_cfg.get("warn_below_pct_important", 60))
    coverage_info_good = float(coverage_cfg.get("info_good_pct", 80))
    confidence_cfg: dict[str, Any] = rules.get("confidence_coverage", {})
    confidence_time_high = float(confidence_cfg.get("time_high_pct", 80))
    confidence_high_warn_below = float(confidence_cfg.get("high_conf_warn_below_pct", 50))
    confidence_high_good = float(confidence_cfg.get("high_conf_info_good_pct", 70))
    monitored_stats_set = set(rules["monitored_stat_catalog"])
    tier_by_stat = build_stat_tier_map(rules, monitored_stats_set)
    stat_priority_weights: dict[str, Any] = rules.get("stat_priority_weights", {})
    detected_stats_by_unit: dict[str, set[str]] = {}
    covered_stats_by_unit: dict[str, set[str]] = {}
    unit_domain_by_unit: dict[str, str | None] = {}

    for group_name, members in unit_groups.items():
        unknown_members = [u for u in members if u not in discovered_units]
        if unknown_members:
            rep.add("WARN", f"UNIT GROUP {group_name}: unknown members {', '.join(sorted(unknown_members))}")
        else:
            rep.add("INFO", f"UNIT GROUP {group_name}: {len(members)} member(s)")

    # 1) unit target sconosciute nelle regole
    for unit in sorted(monitored_units):
        if unit not in discovered_units:
            rep.add("FAIL", f"RULES unknown monitored unit target: {unit}")

    goods_costs = parse_goods_costs(files_cfg["goods"])

    baselines: dict[str, dict[str, float]] = defaultdict(dict)

    # 2) stat monitorate mancanti/non leggibili + 5) costo build/upkeep non calcolabile
    for unit, cfg in units_cfg.items():
        unit_data = parse_unit_block(cfg["unit_file"], unit)
        stats = unit_data["stats"]
        unit_domain_by_unit[unit] = unit_data.get("unit_domain")
        detected_stats = {s for s in stats.keys() if s in monitored_stats_set}
        covered_stats = {s for s in cfg.get("monitored_stats", {}).keys() if s in monitored_stats_set}
        detected_stats_by_unit[unit] = detected_stats
        covered_stats_by_unit[unit] = covered_stats
        missing_coverage = sorted(detected_stats - covered_stats)
        if missing_coverage:
            rep.add("WARN", f"{unit}: unit stats detected but not covered by rules: {', '.join(missing_coverage)}")

        for stat, stat_cfg in cfg["monitored_stats"].items():
            if stat not in stats:
                rep.add("FAIL", f"{unit}: monitored stat missing/unreadable in unit file: {stat}")
            else:
                baseline = stats[stat]
                baselines[unit][stat] = baseline
                rep.add("INFO", f"{unit}: baseline {stat}={baseline}")

        est_build, miss_build, top_build = estimate_costs(unit_data["build_cost"], goods_costs)
        est_upkeep, miss_upkeep, top_upkeep = estimate_costs(unit_data["supply_cost"], goods_costs)

        if miss_build:
            rep.add("FAIL", f"{unit}: cannot estimate build_cost; missing goods costs: {', '.join(sorted(miss_build))}")
        if miss_upkeep:
            rep.add("FAIL", f"{unit}: cannot estimate supply_cost; missing goods costs: {', '.join(sorted(miss_upkeep))}")

        if est_build is not None:
            build_top = ", ".join(f"{g}={v:.2f}" for g, v in top_build) if top_build else "none"
            rep.add("INFO", f"{unit}: economic build_est={est_build:.2f}; top3_build=[{build_top}]")
            build_range = cfg.get("estimated_build_cost_range", {})
            b_min = build_range.get("min")
            b_max = build_range.get("max")
            if (b_min is not None and est_build < b_min) or (b_max is not None and est_build > b_max):
                rep.add("WARN", f"{unit}: estimated build_cost outside range ({est_build:.2f}, expected {b_min}..{b_max})")

        if est_upkeep is not None:
            upkeep_top = ", ".join(f"{g}={v:.2f}" for g, v in top_upkeep) if top_upkeep else "none"
            rep.add("INFO", f"{unit}: economic upkeep_est={est_upkeep:.2f}; top3_upkeep=[{upkeep_top}]")
            upkeep_range = cfg.get("estimated_upkeep_cost_range", {})
            u_min = upkeep_range.get("min")
            u_max = upkeep_range.get("max")
            if (u_min is not None and est_upkeep < u_min) or (u_max is not None and est_upkeep > u_max):
                rep.add("WARN", f"{unit}: estimated upkeep_cost outside range ({est_upkeep:.2f}, expected {u_min}..{u_max})")

        expected_goods = set(cfg.get("key_goods_expectations", []))
        unit_goods = set(unit_data["build_cost"].keys()) | set(unit_data["supply_cost"].keys())
        if expected_goods and expected_goods.isdisjoint(unit_goods):
            rep.add(
                "WARN",
                f"{unit}: none of expected key goods found in unit costs ({', '.join(sorted(expected_goods))})",
            )

    land_units = {u for u, domain in unit_domain_by_unit.items() if domain == "land"}
    naval_units = {u for u, domain in unit_domain_by_unit.items() if domain == "naval"}
    if not land_units:
        land_units = set(unit_groups.get("all_land_units", [])) & monitored_units
    if not naval_units:
        naval_units = set(unit_groups.get("all_naval_units", [])) & monitored_units
    global_scope_units: dict[str, set[str]] = {
        "army_base": set(land_units),
        "navy_base": set(naval_units),
    }

    milestone_years: list[int] = sorted(
        int(y) for y in rules.get("milestone_years", [1836, 1850, 1870, 1900, 1910, 1919, 1929, 1936, 1945, 1955, 1966])
    )
    default_milestone_year = milestone_years[0] if milestone_years else 1836
    inferred_years, year_reason = build_year_inference(rules["scan_files"])
    direct_blocks = sum(1 for _, reason in year_reason.items() if reason == "direct")
    strong_blocks = sum(1 for _, reason in year_reason.items() if reason == "inferred_strong")
    weak_blocks = sum(1 for _, reason in year_reason.items() if reason == "inferred_weak")
    rep.add(
        "INFO",
        f"YEAR INFERENCE: resolved {len(inferred_years)} block year(s) [direct={direct_blocks}, inferred_strong={strong_blocks}, inferred_weak={weak_blocks}]",
    )
    all_assignments: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rel in rules["scan_files"]:
        found = parse_effect_unit_assignments(
            rel,
            monitored_units,
            monitored_stats_set,
            inferred_years,
            year_reason,
            global_scope_units,
        )
        for k, vals in found.items():
            all_assignments[k].extend(vals)

    relevant_assignments_by_unit: dict[str, list[dict[str, Any]]] = {}
    for u, cfg in units_cfg.items():
        monitored_stats = set(cfg.get("monitored_stats", {}).keys())
        relevant_assignments_by_unit[u] = [
            item for item in all_assignments.get(u, []) if item.get("stat") in monitored_stats
        ]

    stat_assignment_count: dict[str, int] = defaultdict(int)
    stat_assignment_units: dict[str, set[str]] = defaultdict(set)
    covered_units_by_stat: dict[str, int] = defaultdict(int)
    for u, cfg in units_cfg.items():
        for s in cfg.get("monitored_stats", {}):
            covered_units_by_stat[s] += 1
        for item in relevant_assignments_by_unit.get(u, []):
            s = item.get("stat")
            if not s:
                continue
            stat_assignment_count[s] += 1
            stat_assignment_units[s].add(u)
    stat_signal_quality: dict[str, str] = {}
    for s in monitored_stats_set:
        stat_signal_quality[s] = get_stat_signal_quality(
            stat_assignment_count.get(s, 0),
            len(stat_assignment_units.get(s, set())),
        )

    relevant_assignment_items = [x for vals in relevant_assignments_by_unit.values() for x in vals]
    total_effect_assignments = len(relevant_assignment_items)
    known_year_assignments = sum(1 for x in relevant_assignment_items if x.get("year") is not None)
    rep.add(
        "INFO",
        f"TIMELINE PLACEMENT (count): known={known_year_assignments}/{total_effect_assignments}, unknown={total_effect_assignments - known_year_assignments}",
    )
    direct_assignments = sum(1 for x in relevant_assignment_items if x.get("year_source") == "direct")
    strong_assignments = sum(1 for x in relevant_assignment_items if x.get("year_source") == "inferred_strong")
    weak_assignments = sum(1 for x in relevant_assignment_items if x.get("year_source") == "inferred_weak")
    unknown_assignments = total_effect_assignments - direct_assignments - strong_assignments - weak_assignments
    rep.add(
        "INFO",
        f"TIMELINE CONFIDENCE (count): direct={direct_assignments}, inferred_strong={strong_assignments}, inferred_weak={weak_assignments}, unknown={unknown_assignments}",
    )
    tech_items = [x for x in relevant_assignment_items if "/technologies/" in x.get("source_file", "")]
    inv_items = [x for x in relevant_assignment_items if "/inventions/" in x.get("source_file", "")]
    unit_scoped_assignments = sum(1 for x in relevant_assignment_items if x.get("scope_kind") == "unit")
    global_scoped_assignments = sum(1 for x in relevant_assignment_items if x.get("scope_kind") == "global")
    global_scope_breakdown: dict[str, int] = defaultdict(int)
    for item in relevant_assignment_items:
        if item.get("scope_kind") == "global":
            global_scope_breakdown[item.get("scope_key", "global")] += 1
    if global_scope_breakdown:
        detail = ", ".join(f"{k}={v}" for k, v in sorted(global_scope_breakdown.items()))
        rep.add(
            "INFO",
            f"EFFECT SCOPE COUNTS: unit_scoped={unit_scoped_assignments}, global_scoped={global_scoped_assignments} [{detail}]",
        )
    else:
        rep.add(
            "INFO",
            f"EFFECT SCOPE COUNTS: unit_scoped={unit_scoped_assignments}, global_scoped={global_scoped_assignments}",
        )

    def _src_counts(items: list[dict[str, Any]]) -> tuple[int, int, int, int]:
        direct = sum(1 for x in items if x.get("year_source") == "direct")
        inferred = sum(1 for x in items if x.get("year_source") in ("inferred_strong", "inferred_weak"))
        unknown = sum(1 for x in items if x.get("year") is None)
        return len(items), direct, inferred, unknown

    t_total, t_direct, t_inferred, t_unknown = _src_counts(tech_items)
    i_total, i_direct, i_inferred, i_unknown = _src_counts(inv_items)
    rep.add(
        "INFO",
        "TIMELINE CONFIDENCE BY SOURCE: "
        f"tech_total={t_total}, tech_direct={t_direct}, tech_inferred={t_inferred}, tech_unknown={t_unknown}, "
        f"invention_total={i_total}, invention_direct={i_direct}, invention_inferred={i_inferred}, invention_unknown={i_unknown}",
    )
    direct_tech_examples = [x for x in tech_items if x.get("year_source") == "direct"][:3]
    if direct_tech_examples:
        for ex in direct_tech_examples:
            rep.add(
                "INFO",
                f"DIRECT TECH EXAMPLE: {format_assignment_origin(ex)} {ex['stat']}={ex['value']} year={ex.get('year')}",
            )
    else:
        rep.add("INFO", "DIRECT TECH EXAMPLE: none found in current scanned assignments")

    invention_examples = inv_items[:3]
    if invention_examples:
        for ex in invention_examples:
            rep.add(
                "INFO",
                f"INVENTION EXAMPLE: {format_assignment_origin(ex)} {ex['stat']}={ex['value']} "
                f"year={ex.get('year')} confidence={ex.get('year_source') or 'unknown'}",
            )
    else:
        rep.add("WARN", "INVENTION EXAMPLE: none found for monitored units in scanned invention files")

    # v3 signal-quality summary per unit: helps distinguish broad coverage from high-value coverage.
    signal_summary: dict[str, dict[str, int]] = {}
    for unit, cfg in units_cfg.items():
        unit_items = relevant_assignments_by_unit.get(unit, [])
        monitored_stats = set(cfg.get("monitored_stats", {}).keys())
        touched_stats = {x.get("stat") for x in unit_items if x.get("stat") in monitored_stats}
        signal_summary[unit] = {
            "assignments": len(unit_items),
            "touched_stats": len(touched_stats),
            "monitored_stats": len(monitored_stats),
        }
        rep.add(
            "INFO",
            f"{unit}: signal assignments={len(unit_items)}, monitored_stats={len(monitored_stats)}, touched_stats={len(touched_stats)}",
        )
        if len(unit_items) == 0:
            rep.add("WARN", f"{unit}: no readable timed deltas found in scanned files; coverage is baseline/economic only")

    # 3) delta singolo oltre soglia + 4) delta cumulative oltre soglia + 5) stima finale fuori range assoluto
    cumulative_positive: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    cumulative_negative: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))

    for unit, cfg in units_cfg.items():
        for item in relevant_assignments_by_unit.get(unit, []):
            stat = item["stat"]
            delta = item["value"]
            s_cfg = cfg["monitored_stats"].get(stat)
            if not s_cfg:
                continue
            max_delta = s_cfg.get("max_single_delta")

            if delta >= 0:
                cumulative_positive[unit][stat] += delta
            else:
                cumulative_negative[unit][stat] += delta
            if max_delta is not None and abs(delta) > max_delta:
                rep.add(
                    "WARN",
                    f"{unit} {stat} delta too large from {format_assignment_origin(item)} ({delta}, max_single_delta {max_delta})",
                )

    for unit, cfg in units_cfg.items():
        historical_start_year = get_historical_relevance_start_year(cfg, default_milestone_year)
        for stat, s_cfg in cfg["monitored_stats"].items():
            baseline = baselines.get(unit, {}).get(stat)
            if baseline is None:
                continue
            pos_delta = cumulative_positive[unit][stat]
            neg_delta = cumulative_negative[unit][stat]
            total_delta = pos_delta + neg_delta
            estimated_final = baseline + total_delta

            stat_assignments = [a for a in relevant_assignments_by_unit.get(unit, []) if a["stat"] == stat]
            unknown_year_delta = sum(a["value"] for a in stat_assignments if a.get("year") is None)
            unknown_year_count = sum(1 for a in stat_assignments if a.get("year") is None)
            known_year_count = len(stat_assignments) - unknown_year_count
            known_years = sorted({a["year"] for a in stat_assignments if a.get("year") is not None})
            first_known_year = known_years[0] if known_years else None
            last_known_year = known_years[-1] if known_years else None

            total_abs_delta = sum(abs(a["value"]) for a in stat_assignments)
            unit_scope_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("scope_kind") == "unit")
            global_scope_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("scope_kind") == "global")
            known_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("year") is not None)
            unknown_abs_delta = total_abs_delta - known_abs_delta
            coverage_pct = 0.0 if total_abs_delta == 0 else (known_abs_delta / total_abs_delta) * 100.0
            direct_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("year_source") == "direct")
            strong_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("year_source") == "inferred_strong")
            weak_abs_delta = sum(abs(a["value"]) for a in stat_assignments if a.get("year_source") == "inferred_weak")
            high_conf_abs = direct_abs_delta + strong_abs_delta
            high_conf_pct = 0.0 if total_abs_delta == 0 else (high_conf_abs / total_abs_delta) * 100.0

            milestone_estimates: list[str] = []
            for year in milestone_years:
                est = baseline + sum(
                    a["value"] for a in stat_assignments if a.get("year") is not None and a["year"] <= year
                )
                milestone_estimates.append(f"{year}:{est:.3f}")

            rep.add(
                "INFO",
                f"{unit} {stat}: baseline_raw {baseline:.3f}, "
                f"first_known_year {first_known_year if first_known_year is not None else 'n/a'}, "
                f"last_known_year {last_known_year if last_known_year is not None else 'n/a'}, "
                f"cumulative +{pos_delta:.3f}, cumulative -{abs(neg_delta):.3f}, "
                f"milestones[{', '.join(milestone_estimates)}], estimated_final {estimated_final:.3f}, "
                f"scope_unit {unit_scope_abs_delta:.3f}, scope_global {global_scope_abs_delta:.3f}, "
                f"time_direct {direct_abs_delta:.3f}, time_inferred_strong {strong_abs_delta:.3f}, "
                f"time_inferred_weak {weak_abs_delta:.3f}, time_unknown {unknown_abs_delta:.3f}, "
                f"time_coverage {coverage_pct:.1f}%, high_conf_coverage {high_conf_pct:.1f}%",
            )
            if unknown_year_count > 0:
                rep.add(
                    "INFO",
                    f"{unit} {stat}: unknown-year deltas excluded from milestones: count={unknown_year_count}, total={unknown_year_delta:+.3f} "
                    f"(known_count={known_year_count})",
                )
            important_stats = set(cfg.get("important_stats", []))
            if total_abs_delta > 0 and stat in important_stats and coverage_pct < coverage_warn_below:
                rep.add(
                    "WARN",
                    f"{unit} {stat} low timeline coverage ({coverage_pct:.1f}% < {coverage_warn_below:.1f}%)",
                )
            elif coverage_pct >= coverage_info_good:
                rep.add("INFO", f"{unit} {stat} timeline coverage is good ({coverage_pct:.1f}%)")
            if (
                total_abs_delta > 0
                and stat in important_stats
                and coverage_pct >= confidence_time_high
                and high_conf_pct < confidence_high_warn_below
            ):
                rep.add(
                    "WARN",
                    f"{unit} {stat} timeline mostly placed but low high-confidence coverage ({high_conf_pct:.1f}% < {confidence_high_warn_below:.1f}%)",
                )
            elif high_conf_pct >= confidence_high_good:
                rep.add("INFO", f"{unit} {stat} high-confidence coverage is good ({high_conf_pct:.1f}%)")
            max_pos = s_cfg.get("max_cumulative_positive_delta")
            max_neg = s_cfg.get("max_cumulative_negative_delta")
            if max_pos is not None and pos_delta > max_pos:
                rep.add(
                    "WARN",
                    f"{unit} {stat} cumulative positive delta too large (+{pos_delta:.3f}, max {max_pos})",
                )
            if max_neg is not None and abs(neg_delta) > max_neg:
                rep.add(
                    "WARN",
                    f"{unit} {stat} cumulative negative delta too large ({neg_delta:.3f}, max -{max_neg})",
                )
            min_final, max_final = get_final_range(s_cfg)
            if (min_final is not None and estimated_final < min_final) or (max_final is not None and estimated_final > max_final):
                rep.add(
                    "WARN",
                    f"{unit} {stat} estimated final outside final_range (baseline {baseline:.3f} + delta {total_delta:+.3f} = {estimated_final:.3f}, expected {min_final}..{max_final})",
                )
            milestone_ranges = s_cfg.get("milestone_ranges", {})
            skipped_milestone_years: list[int] = []
            for year in milestone_years:
                if year < historical_start_year:
                    if milestone_ranges.get(str(year)) or milestone_ranges.get(year):
                        skipped_milestone_years.append(year)
                    continue
                cfg_y = milestone_ranges.get(str(year)) or milestone_ranges.get(year)
                if not cfg_y:
                    continue
                m_min = cfg_y.get("min")
                m_max = cfg_y.get("max")
                m_est = baseline + sum(
                    a["value"] for a in stat_assignments if a.get("year") is not None and a["year"] <= year
                )
                if (m_min is not None and m_est < m_min) or (m_max is not None and m_est > m_max):
                    rep.add(
                        "WARN",
                        f"{unit} {stat} milestone {year} outside configured range ({m_est:.3f}, expected {m_min}..{m_max})",
                    )
            if skipped_milestone_years:
                years_txt = ", ".join(str(y) for y in skipped_milestone_years)
                rep.add(
                    "INFO",
                    f"{unit} {stat}: skipped milestone range checks for pre-applicability years [{years_txt}] "
                    f"(historical_relevance_start_year={historical_start_year})",
                )

    check_key_goods_availability(files_cfg["production_types"], rules["economic"]["key_goods"], rep)

    rep.dump()
    priority_buckets, playtest_focus = build_priority_summary(
        rep.items,
        units_cfg,
        tier_by_unit,
        tier_by_stat,
        stat_signal_quality,
        stat_priority_weights,
    )
    print("\nPRIORITY SUMMARY")
    for bucket in ("structural/data confidence issues", "stat progression issues", "economic plausibility issues"):
        print(f"\n - {bucket}")
        top_items = priority_buckets.get(bucket, [])[:8]
        if not top_items:
            print("   * none")
            continue
        for score, text in top_items:
            print(f"   * [score {score}] {text}")

    print("\nRECOMMENDED PLAYTEST FOCUS")
    if not playtest_focus:
        print(" - No high-priority WARN/FAIL playtest targets identified from current run.")
    else:
        for _, text in playtest_focus:
            print(f" - {text}")

    # Tiered watchlists (short practical summary by unit).
    fail_by_unit = {extract_unit_and_subject(msg)[0] for lvl, msg in rep.items if lvl == "FAIL"}
    main_warn_by_unit: dict[str, str] = {}
    for lvl, msg in rep.items:
        if lvl not in {"FAIL", "WARN"}:
            continue
        u, _ = extract_unit_and_subject(msg)
        if u not in units_cfg:
            continue
        current = main_warn_by_unit.get(u)
        if current is None:
            main_warn_by_unit[u] = msg
            continue
        if lvl == "WARN" and u in fail_by_unit:
            continue
        if "milestone" in msg and "milestone" not in current:
            main_warn_by_unit[u] = msg

    def _print_watchlist(title: str, tier_name: str) -> None:
        print(f"\n{title}")
        members = sorted(u for u in units_cfg if tier_by_unit.get(u, "secondary") == tier_name)
        if not members:
            print(" - none")
            return
        for u in members:
            sig = signal_summary.get(u, {"assignments": 0, "touched_stats": 0})
            top_warn = main_warn_by_unit.get(u, "none")
            print(
                f" - {u} | tier={tier_name} | signal_assignments={sig['assignments']} | "
                f"touched_stats={sig['touched_stats']} | top_warning={top_warn}"
            )

    _print_watchlist("CORE WATCHLIST", "core")
    _print_watchlist("SECONDARY WATCHLIST", "secondary")
    _print_watchlist("LOW-SIGNAL COVERAGE", "low_signal")

    print("\nSTAT COVERAGE SUMMARY")
    total_detected = sum(len(v) for v in detected_stats_by_unit.values())
    total_covered = sum(len(covered_stats_by_unit.get(u, set()) & detected_stats_by_unit.get(u, set())) for u in units_cfg)
    global_detected_stats = sorted({s for vals in detected_stats_by_unit.values() for s in vals})
    global_covered_stats = sorted({s for vals in covered_stats_by_unit.values() for s in vals})
    print(f" - total_covered_stats={total_covered}")
    print(f" - total_detected_stats={total_detected}")
    print(f" - global_detected_stat_types={len(global_detected_stats)}")
    print(f" - global_covered_stat_types={len(global_covered_stats)}")
    for u in sorted(units_cfg):
        det = detected_stats_by_unit.get(u, set())
        cov = covered_stats_by_unit.get(u, set()) & det
        missing = sorted(det - cov)
        if missing:
            print(f" - {u}: covered_stats={len(cov)}/{len(det)} missing={', '.join(missing)}")
        else:
            print(f" - {u}: covered_stats={len(cov)}/{len(det)}")

    print("\nSTAT DIAGNOSTIC QUALITY")
    for tier_name in ("primary", "secondary", "structural"):
        print(f" - {tier_name.upper()}")
        stats = [s for s, t in tier_by_stat.items() if t == tier_name]
        if not stats:
            print("   * none")
            continue
        for s in sorted(stats):
            covered_units = covered_units_by_stat.get(s, 0)
            assignments = stat_assignment_count.get(s, 0)
            units_with_signal = len(stat_assignment_units.get(s, set()))
            quality = stat_signal_quality.get(s, "limited_signal")
            print(
                f"   * {s}: covered_units={covered_units}, assignments={assignments}, "
                f"units_with_signal={units_with_signal}, quality={quality}"
            )

    print("\nTOP STAT WATCHLIST")
    stat_watch: dict[str, tuple[int, str]] = {}
    for level, msg in rep.items:
        if level not in {"FAIL", "WARN"}:
            continue
        unit, subject = extract_unit_and_subject(msg)
        if subject not in monitored_stats_set:
            continue
        score = 100 if level == "FAIL" else 60
        score += int(stat_priority_weights.get("tier", {}).get(tier_by_stat.get(subject, "secondary"), 0))
        score += int(stat_priority_weights.get("signal", {}).get(stat_signal_quality.get(subject, "limited_signal"), 0))
        score += 10 if tier_by_unit.get(unit, "secondary") == "core" else 0
        prev = stat_watch.get(subject)
        if prev is None or score > prev[0]:
            stat_watch[subject] = (score, msg)
    top_stats = sorted(stat_watch.items(), key=lambda x: x[1][0], reverse=True)[:8]
    if not top_stats:
        print(" - none")
    else:
        for stat, (score, msg) in top_stats:
            print(
                f" - {stat} | tier={tier_by_stat.get(stat, 'secondary')} | "
                f"units_with_signal={len(stat_assignment_units.get(stat, set()))} | "
                f"quality={stat_signal_quality.get(stat, 'limited_signal')} | score={score} | top_issue={msg}"
            )

    # Diagnostic tool: non-blocking by design.
    return 0


if __name__ == "__main__":
    sys.exit(main())
