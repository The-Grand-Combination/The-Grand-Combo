#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from lib_1966_parser import TopLevelBlockMeta, parse_top_level_block_meta, read_text, rebase_path, resolve_repo_path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = "TGC/tools/1966_extension_scope.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the TGC 1966 timeline submod layer.")
    parser.add_argument("--core-root", default="TGC", help="Base/core mod root (default: TGC).")
    parser.add_argument(
        "--timeline-root",
        default="TGC_Timeline_1966",
        help="1966 timeline runtime root (default: TGC_Timeline_1966).",
    )
    return parser.parse_args()


def _rebase_obj(obj, *, core_root: str, timeline_root: str):
    if isinstance(obj, str):
        return rebase_path(obj, core_root=core_root, timeline_root=timeline_root)
    if isinstance(obj, list):
        return [_rebase_obj(x, core_root=core_root, timeline_root=timeline_root) for x in obj]
    if isinstance(obj, dict):
        return {k: _rebase_obj(v, core_root=core_root, timeline_root=timeline_root) for k, v in obj.items()}
    return obj


def read_manifest(core_root: str = "TGC", timeline_root: str = "TGC_Timeline_1966") -> dict:
    manifest = json.loads(read_text(MANIFEST_PATH, encoding="utf-8"))
    return _rebase_obj(manifest, core_root=core_root, timeline_root=timeline_root)


def build_localisation_index(localisation_files: list[str]) -> dict[str, list[str]]:
    idx: dict[str, list[str]] = {}
    for rel_path in localisation_files:
        for lineno, line in enumerate(read_text(rel_path, encoding="latin-1").splitlines(), 1):
            if not line or line.startswith("#"):
                continue
            key = line.split(";", 1)[0].strip()
            idx.setdefault(key, []).append(f"{rel_path}:{lineno}")
    return idx


UNIT_STAT_HINTS = {
    "attack",
    "defence",
    "hull",
    "gun_power",
    "torpedo_attack",
    "reconnaissance",
    "support",
    "maneuver",
    "siege",
    "maximum_speed",
    "evasion",
    "fire_range",
    "discipline",
    "supply_consumption",
}

NON_UNIT_EFFECT_KEYS = {"army_base", "navy_base"}
LEGACY_UNIT_ALIASES = {"carrier": "aircraftcarrier"}


def discover_unit_keys(core_root: str, timeline_root: str) -> set[str]:
    keys: set[str] = set()
    for rel_dir in (f"{core_root}/units", f"{timeline_root}/units"):
        unit_dir = resolve_repo_path(rel_dir)
        if unit_dir.exists():
            keys.update(p.stem for p in unit_dir.glob("*.txt"))
    return keys


def validate_effect_unit_targets(rel_path: str, unit_keys: set[str]) -> list[str]:
    failures: list[str] = []
    lines = read_text(rel_path).splitlines()
    i = 0
    while i < len(lines):
        if re.match(r"\s*effect\s*=\s*\{\s*(?:#.*)?$", lines[i]):
            depth = 1
            i += 1
            effect_lines: list[tuple[int, str, int]] = []
            while i < len(lines) and depth > 0:
                cur = lines[i]
                effect_lines.append((i + 1, cur, depth))
                depth += cur.count("{") - cur.count("}")
                i += 1

            j = 0
            while j < len(effect_lines):
                lineno, txt, local_depth = effect_lines[j]
                if local_depth == 1:
                    ma = re.match(r"\s*activate_unit\s*=\s*([a-z0-9_]+)", txt)
                    if ma:
                        unit_key = ma.group(1)
                        if unit_key not in unit_keys:
                            failures.append(f"UNIT target unknown key '{unit_key}' in {rel_path}:{lineno} (activate_unit)")

                    mb = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*(?:#.*)?$", txt)
                    if mb:
                        key = mb.group(1)
                        sub_depth = 1
                        k = j + 1
                        sub: list[tuple[int, str]] = []
                        while k < len(effect_lines) and sub_depth > 0:
                            ln2, t2, _ = effect_lines[k]
                            sub.append((ln2, t2))
                            sub_depth += t2.count("{") - t2.count("}")
                            k += 1

                        if key not in NON_UNIT_EFFECT_KEYS:
                            joined = "\n".join(x[1] for x in sub)
                            looks_like_unit_target = any(re.search(rf"\b{re.escape(stat)}\b", joined) for stat in UNIT_STAT_HINTS)
                            if looks_like_unit_target and key not in unit_keys:
                                if key in LEGACY_UNIT_ALIASES and LEGACY_UNIT_ALIASES[key] in unit_keys:
                                    failures.append(
                                        f"UNIT target legacy key '{key}' in {rel_path}:{lineno} (use '{LEGACY_UNIT_ALIASES[key]}')"
                                    )
                                else:
                                    failures.append(f"UNIT target unknown key '{key}' in {rel_path}:{lineno}")
                        j = k
                        continue
                j += 1
            continue
        i += 1
    return failures


def block_has_section_year(block_lines: list[tuple[int, str]], section: str, expected_year: int) -> bool:
    i = 0
    while i < len(block_lines):
        _, line = block_lines[i]
        m = re.match(rf"\s*{re.escape(section)}\s*=\s*\{{\s*(?:#.*)?$", line)
        if not m:
            i += 1
            continue

        depth = 1
        i += 1
        while i < len(block_lines) and depth > 0:
            _, cur = block_lines[i]
            if re.search(rf"\byear\s*=\s*{expected_year}\b", cur):
                return True
            depth += cur.count("{") - cur.count("}")
            i += 1
    return False


def find_named_block_lines(rel_path: str, block_key: str) -> list[tuple[int, str]] | None:
    lines = read_text(rel_path).splitlines()
    i = 0
    while i < len(lines):
        m = re.match(rf"\s*{re.escape(block_key)}\s*=\s*\{{\s*(?:#.*)?$", lines[i])
        if not m:
            i += 1
            continue

        depth = 1
        i += 1
        block: list[tuple[int, str]] = []
        while i < len(lines) and depth > 0:
            block.append((i + 1, lines[i]))
            depth += lines[i].count("{") - lines[i].count("}")
            i += 1
        return block
    return None


def main() -> int:
    args = parse_args()
    m = read_manifest(args.core_root, args.timeline_root)
    branches = m["tech_tree"]["branches"]
    late_min_year = m["tech_tree"].get("late_tech_min_year", 1936)
    invention_files = m["invention_files"]
    loc_files = m["localisation_files"]
    structural = m["structural"]
    stale_rules = m.get("stale_reference_rules", [])
    unit_keys = discover_unit_keys(args.core_root, args.timeline_root)

    failures: list[str] = []
    loc_index = build_localisation_index(loc_files)
    loc_keys = set(loc_index)

    all_tech: list[TopLevelBlockMeta] = []
    expected_areas = 0

    for b in branches:
        rel_path = b["file"]
        area_spec = b["areas"]
        expected_areas += len(area_spec)
        blocks = parse_top_level_block_meta(rel_path)
        all_tech.extend(blocks)
        by_area: dict[str, list[TopLevelBlockMeta]] = defaultdict(list)
        for x in blocks:
            if x["area"]:
                by_area[x["area"]].append(x)
        for area, expected in area_spec.items():
            actual = len(by_area.get(area, []))
            if actual != expected:
                failures.append(f"TECH area tier mismatch in {rel_path}: {area} has {actual}, expected {expected}")

    tech_idx: dict[str, list[str]] = defaultdict(list)
    for x in all_tech:
        tech_idx[x["key"]].append(x["file"])
    for k, files in tech_idx.items():
        if len(files) > 1:
            failures.append(f"TECH duplicate definition for {k}: {', '.join(sorted(set(files)))}")

    late_keys = sorted({x["key"] for x in all_tech if x["year"] is not None and x["year"] >= late_min_year})
    for k in late_keys:
        if k not in loc_keys:
            failures.append(f"TECH missing localisation key: {k}")
        if f"{k}_desc" not in loc_keys:
            failures.append(f"TECH missing localisation desc: {k}_desc")

    all_inv: list[TopLevelBlockMeta] = []
    for rel in invention_files:
        all_inv.extend(parse_top_level_block_meta(rel))
    inv_idx: dict[str, list[str]] = defaultdict(list)
    for x in all_inv:
        inv_idx[x["key"]].append(x["file"])
    for k, files in inv_idx.items():
        if len(files) > 1:
            failures.append(f"INVENTION duplicate definition for {k}: {', '.join(sorted(set(files)))}")
        if k not in loc_keys:
            failures.append(f"INVENTION missing localisation key: {k}")
        if f"{k}_desc" not in loc_keys:
            failures.append(f"INVENTION missing localisation desc: {k}_desc")

    unit_target_files = sorted({b["file"] for b in branches} | set(invention_files) | set(structural.get("unit_target_files_extra", [])))
    for rel in unit_target_files:
        failures.extend(validate_effect_unit_targets(rel, unit_keys))

    for rule in stale_rules:
        pat = re.compile(rf"\b{re.escape(rule['old_key'])}\b")
        for rel in rule["files"]:
            for n, line in enumerate(read_text(rel).splitlines(), 1):
                if pat.search(line):
                    failures.append(f"STALE reference {rule['old_key']} found in {rel}:{n} (expected context: {rule['new_key']})")

    d = structural["decision_alignment"]
    decision_block = find_named_block_lines(d["file"], d["decision_key"])
    if not decision_block:
        failures.append(f"STRUCTURAL missing {d['decision_key']} block in {d['file']}")
    else:
        if not block_has_section_year(decision_block, "potential", d["potential_year"]):
            failures.append(f"STRUCTURAL {d['decision_key']} potential must include year = {d['potential_year']}")
        if not block_has_section_year(decision_block, "allow", d["allow_year"]):
            failures.append(f"STRUCTURAL {d['decision_key']} allow must include year = {d['allow_year']}")

    for chk in structural["required_patterns"]:
        if not re.search(chk["pattern"], read_text(chk["file"]), re.S):
            failures.append(f"STRUCTURAL {chk['message']}")
    for chk in structural.get("core_forbidden_patterns", []):
        if resolve_repo_path(chk["file"]).exists() and re.search(chk["pattern"], read_text(chk["file"]), re.S):
            failures.append(f"CORE CLEANUP {chk['message']}")
    for req in structural["required_files"]:
        if not resolve_repo_path(req).exists():
            failures.append(f"STRUCTURAL missing file: {req}")
    for forbidden in structural.get("core_forbidden_files", []):
        if resolve_repo_path(forbidden).exists():
            failures.append(f"CORE CLEANUP forbidden timeline-only file remains: {forbidden}")
    for req_bin in structural.get("required_binary_files", []):
        path = resolve_repo_path(req_bin)
        if not path.exists():
            failures.append(f"STRUCTURAL missing binary asset: {req_bin}")
        elif path.stat().st_size <= 0:
            failures.append(f"STRUCTURAL empty binary asset: {req_bin}")

    print("1966 extension full-tree static validation")
    print(f" - scope manifest: {MANIFEST_PATH}")
    print(f" - core root: {args.core_root}")
    print(f" - timeline root: {args.timeline_root}")
    print(f" - expected tech areas: {expected_areas}")
    print(f" - parsed tech definitions: {len(all_tech)}")
    print(f" - late-tech localisation perimeter (year >= {late_min_year}): {len(late_keys)} keys")
    print(f" - tracked invention files: {len(invention_files)}")
    print(f" - parsed inventions in tracked files: {len(all_inv)}")
    print(f" - discovered unit keys: {len(unit_keys)}")
    print(" - structural checks: submod runtime + core cleanup + docs")

    if failures:
        print("\nFAILED checks:")
        for item in failures:
            print(f" - {item}")
        return 1

    print("\nOK: full-tree 1966 static checks passed (25 areas @ 12 tiers + localisation + structure).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
