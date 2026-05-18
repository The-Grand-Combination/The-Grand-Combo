#!/usr/bin/env python3
"""Conservative drift check for 1966 timeline full-file overrides.

The separated 1966 timeline submod carries several full-file overrides.  Those
files intentionally differ from core, but any future core-only fix in a duplicated
section can be masked by the submod unless the override is refreshed too.

This tool is read-only.  It compares current core files with their timeline
counterparts and, when a base git ref is available, checks whether core hunks
changed since that ref are also represented in the timeline override.  In
reverse mode, it checks whether changed timeline override hunks look generic and
therefore may need to be ported back to core.
"""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

DEFAULT_CORE_ROOT = "TGC"
DEFAULT_TIMELINE_ROOT = "TGC_Timeline_1966"
MANIFEST_PATH = Path("TGC_Timeline_1966/docs/manifest_1966_timeline.md")
TEXT_OVERRIDE_SUFFIXES = (".txt", ".lua", ".gui", ".gfx")

# Minimum explicit watchlist requested for full override / carrier drift checks.
WATCHED_RELATIVE_PATHS = [
    "common/buildings.txt",
    "decisions/00_Setup.txt",
    "inventions/navy_inventions.txt",
    "technologies/army_tech.txt",
    "technologies/commerce_tech.txt",
    "technologies/culture_tech.txt",
    "technologies/industry_tech.txt",
    "technologies/navy_tech.txt",
    "interface/backend.gui",
    "interface/buildings.gfx",
    "interface/buildunit.gui",
    "interface/combat.gfx",
    "interface/country_military.gfx",
    "interface/country_technology.gui",
    "interface/province_interface.gfx",
    "interface/ships.gfx",
    "interface/unitpanel.gfx",
]

# Tokens that make a difference plausibly timeline-specific.  This is deliberately
# broad and only downgrades diagnostics to INFO; uncertain lines remain WARN.
TIMELINE_HINT_RE = re.compile(
    r"1966|1936|submarine|aircraftcarrier|carrier|supercarrier|unit_folder|"
    r"unit_strip|naval_combat|level\s*=\s*[78]|end_date|option_end_game|"
    r"The World in 1966|NEW_[a-z]+_inventions",
    re.IGNORECASE,
)

NOISE_RE = re.compile(r"^[\s{}\[\](),;]*$|^\s*#")


@dataclass
class Diagnostic:
    severity: str
    relpath: str
    message: str
    samples: list[str] = field(default_factory=list)


def run_git(args: list[str], check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


def git_ref_exists(ref: str) -> bool:
    result = run_git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"])
    return result.returncode == 0


def normalize_line(line: str) -> str:
    return " ".join(line.strip().split())


def is_substantive(line: str) -> bool:
    return bool(normalize_line(line)) and not NOISE_RE.match(line)


def is_timeline_line(line: str) -> bool:
    return bool(TIMELINE_HINT_RE.search(line))


def read_text_lines(path: Path) -> list[str]:
    data = path.read_bytes()
    # Victoria 2 mod files in this repo are mostly ASCII/Windows-1252 compatible;
    # latin-1 keeps the check lossless enough for line comparison without writes.
    return data.decode("latin-1").splitlines()


def parse_manifest_override_paths(manifest: Path, timeline_root: str, core_root: str) -> set[str]:
    """Return relative paths from manifest rows marked as override/carrier."""
    if not manifest.exists():
        return set()
    paths: set[str] = set()
    table_re = re.compile(r"\| `([^`]+)` \| `([^`]+)` \| (.+) \|")
    for line in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
        match = table_re.match(line.strip())
        if not match:
            continue
        timeline_path, core_path, note = match.groups()
        note_l = note.lower()
        if "override" not in note_l and "carrier" not in note_l:
            continue
        prefix = f"{timeline_root}/"
        core_prefix = f"{core_root}/"
        if timeline_path.startswith(prefix) and core_path.startswith(core_prefix):
            relpath = timeline_path[len(prefix) :]
            if relpath.endswith(TEXT_OVERRIDE_SUFFIXES):
                paths.add(relpath)
    return paths


def changed_added_lines_since(base_ref: str, path: Path) -> tuple[list[str], str | None]:
    """Return added/current lines in hunks changed since base_ref."""
    result = run_git(["diff", "--unified=0", base_ref, "--", str(path)])
    if result.returncode != 0:
        return [], result.stderr.strip() or "git diff failed"

    added: list[str] = []
    for line in result.stdout.splitlines():
        if not line.startswith("+") or line.startswith("+++"):  # diff metadata
            continue
        text = line[1:]
        if is_substantive(text):
            added.append(text)
    return added, None


def summarize_full_difference(core_lines: list[str], timeline_lines: list[str]) -> tuple[int, int, int]:
    diff = difflib.SequenceMatcher(
        None,
        [normalize_line(line) for line in core_lines],
        [normalize_line(line) for line in timeline_lines],
        autojunk=False,
    )
    core_only = timeline_only = timeline_hint_lines = 0
    for tag, i1, i2, j1, j2 in diff.get_opcodes():
        if tag == "equal":
            continue
        core_only += sum(1 for line in core_lines[i1:i2] if is_substantive(line))
        changed_timeline_lines = [line for line in timeline_lines[j1:j2] if is_substantive(line)]
        timeline_only += len(changed_timeline_lines)
        timeline_hint_lines += sum(1 for line in changed_timeline_lines if is_timeline_line(line))
    return core_only, timeline_only, timeline_hint_lines


def check_one_forward(relpath: str, core_root: Path, timeline_root: Path, base_ref: str) -> list[Diagnostic]:
    core_path = core_root / relpath
    timeline_path = timeline_root / relpath
    diagnostics: list[Diagnostic] = []

    if not timeline_path.exists():
        return [Diagnostic("FAIL", relpath, f"timeline override missing: {timeline_path}")]

    if not core_path.exists():
        return [
            Diagnostic(
                "INFO",
                relpath,
                "timeline carrier has no current core counterpart; no core drift can be checked for this path",
            )
        ]

    core_lines = read_text_lines(core_path)
    timeline_lines = read_text_lines(timeline_path)
    core_norm = [normalize_line(line) for line in core_lines]
    timeline_norm_set = {normalize_line(line) for line in timeline_lines if is_substantive(line)}

    added_lines, error = changed_added_lines_since(base_ref, core_path)
    if error:
        diagnostics.append(Diagnostic("FAIL", relpath, error))
        return diagnostics

    missing_from_timeline = []
    timeline_expected = []
    for line in added_lines:
        norm = normalize_line(line)
        if not norm or norm in timeline_norm_set:
            continue
        if is_timeline_line(line):
            timeline_expected.append(line)
        else:
            missing_from_timeline.append(line)

    if missing_from_timeline:
        diagnostics.append(
            Diagnostic(
                "WARN",
                relpath,
                f"{len(missing_from_timeline)} changed core line(s) since {base_ref} are not present in the timeline override",
                missing_from_timeline[:5],
            )
        )
    elif added_lines:
        diagnostics.append(
            Diagnostic(
                "OK",
                relpath,
                f"{len(added_lines)} changed core line(s) since {base_ref} are represented in the timeline override or look timeline-specific",
            )
        )

    if timeline_expected:
        diagnostics.append(
            Diagnostic(
                "INFO",
                relpath,
                f"{len(timeline_expected)} changed core line(s) since {base_ref} look timeline-specific and were not treated as drift",
                timeline_expected[:5],
            )
        )

    if core_norm == [normalize_line(line) for line in timeline_lines]:
        diagnostics.append(Diagnostic("OK", relpath, "override content currently matches core"))
    else:
        core_only, timeline_only, timeline_hint_lines = summarize_full_difference(core_lines, timeline_lines)
        if not added_lines:
            diagnostics.append(
                Diagnostic(
                    "INFO",
                    relpath,
                    "override differs from core, but no core hunk changed since "
                    f"{base_ref}; full diff summary: core-only lines={core_only}, "
                    f"timeline-only lines={timeline_only}, timeline-hint lines={timeline_hint_lines}",
                )
            )
        else:
            diagnostics.append(
                Diagnostic(
                    "INFO",
                    relpath,
                    "override differs from core; review WARN entries above for possible newly introduced drift",
                )
            )

    return diagnostics


def check_one_reverse(relpath: str, core_root: Path, timeline_root: Path, base_ref: str) -> list[Diagnostic]:
    """Check whether changed timeline override hunks look generic and core-worthy."""
    core_path = core_root / relpath
    timeline_path = timeline_root / relpath
    diagnostics: list[Diagnostic] = []

    if not timeline_path.exists():
        return [Diagnostic("FAIL", relpath, f"timeline override missing: {timeline_path}")]

    added_lines, error = changed_added_lines_since(base_ref, timeline_path)
    if error:
        diagnostics.append(Diagnostic("FAIL", relpath, error))
        return diagnostics

    if not core_path.exists():
        if added_lines:
            diagnostics.append(
                Diagnostic(
                    "INFO",
                    relpath,
                    "timeline carrier has no current core counterpart; changed submod lines were treated as timeline-only carrier content",
                    added_lines[:5],
                )
            )
        else:
            diagnostics.append(
                Diagnostic(
                    "INFO",
                    relpath,
                    "timeline carrier has no current core counterpart; no submod hunk changed since "
                    f"{base_ref}",
                )
            )
        return diagnostics

    core_lines = read_text_lines(core_path)
    timeline_lines = read_text_lines(timeline_path)
    core_norm_set = {normalize_line(line) for line in core_lines if is_substantive(line)}

    generic_only = []
    timeline_expected = []
    for line in added_lines:
        norm = normalize_line(line)
        if not norm or norm in core_norm_set:
            continue
        if is_timeline_line(line):
            timeline_expected.append(line)
        else:
            generic_only.append(line)

    if generic_only:
        diagnostics.append(
            Diagnostic(
                "WARN",
                relpath,
                f"{len(generic_only)} changed timeline line(s) since {base_ref} are not present in core and do not look timeline-specific",
                generic_only[:5],
            )
        )
    elif added_lines:
        diagnostics.append(
            Diagnostic(
                "OK",
                relpath,
                f"{len(added_lines)} changed timeline line(s) since {base_ref} are present in core or look timeline-specific",
            )
        )
    else:
        diagnostics.append(
            Diagnostic(
                "OK",
                relpath,
                f"no timeline override hunk changed since {base_ref}",
            )
        )

    if timeline_expected:
        diagnostics.append(
            Diagnostic(
                "INFO",
                relpath,
                f"{len(timeline_expected)} changed timeline line(s) since {base_ref} look 1966-specific and were not treated as generic core drift",
                timeline_expected[:5],
            )
        )

    if generic_only or timeline_expected or added_lines:
        diagnostics.append(
            Diagnostic(
                "INFO",
                relpath,
                "reverse mode only classifies changed submod hunks; existing baseline override differences are not reclassified",
            )
        )
    elif [normalize_line(line) for line in core_lines] != [normalize_line(line) for line in timeline_lines]:
        core_only, timeline_only, timeline_hint_lines = summarize_full_difference(core_lines, timeline_lines)
        diagnostics.append(
            Diagnostic(
                "INFO",
                relpath,
                "override differs from core at baseline; no submod hunk changed since "
                f"{base_ref}; full diff summary: core-only lines={core_only}, "
                f"timeline-only lines={timeline_only}, timeline-hint lines={timeline_hint_lines}",
            )
        )

    return diagnostics


def count_by_severity(diagnostics: Iterable[Diagnostic]) -> dict[str, int]:
    counts = {"FAIL": 0, "WARN": 0, "INFO": 0, "OK": 0}
    for diagnostic in diagnostics:
        counts[diagnostic.severity] = counts.get(diagnostic.severity, 0) + 1
    return counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Read-only drift check for TGC_Timeline_1966 full-file overrides."
    )
    parser.add_argument("--core-root", default=DEFAULT_CORE_ROOT, help="core mod root (default: TGC)")
    parser.add_argument(
        "--timeline-root",
        default=DEFAULT_TIMELINE_ROOT,
        help="timeline submod root (default: TGC_Timeline_1966)",
    )
    parser.add_argument(
        "--base-ref",
        default="HEAD",
        help="git ref used to identify changed hunks (default: HEAD; use a merge-base/main ref in CI or after commits)",
    )
    parser.add_argument(
        "--reverse",
        "--check-submod-to-core",
        action="store_true",
        help="check changed timeline override hunks for possible generic fixes that should be ported back to core",
    )
    parser.add_argument(
        "--fail-on-warn",
        action="store_true",
        help="exit non-zero when WARN diagnostics are present; intended for CI drift enforcement",
    )
    args = parser.parse_args(argv)

    core_root = Path(args.core_root)
    timeline_root = Path(args.timeline_root)
    base_ref = args.base_ref

    watched = set(WATCHED_RELATIVE_PATHS)
    watched.update(parse_manifest_override_paths(MANIFEST_PATH, args.timeline_root, args.core_root))

    diagnostics: list[Diagnostic] = []

    if not core_root.exists():
        diagnostics.append(Diagnostic("FAIL", str(core_root), "core root does not exist"))
    if not timeline_root.exists():
        diagnostics.append(Diagnostic("FAIL", str(timeline_root), "timeline root does not exist"))
    if not git_ref_exists(base_ref):
        diagnostics.append(Diagnostic("FAIL", base_ref, "base ref is not a valid git commit"))

    if diagnostics:
        watched_paths: list[str] = []
    else:
        watched_paths = sorted(watched)
        for relpath in watched_paths:
            if args.reverse:
                diagnostics.extend(check_one_reverse(relpath, core_root, timeline_root, base_ref))
            else:
                diagnostics.extend(check_one_forward(relpath, core_root, timeline_root, base_ref))

    counts = count_by_severity(diagnostics)
    direction = "submod -> core" if args.reverse else "core -> submod"
    print("1966 SUBMOD OVERRIDE DRIFT CHECK (read-only)")
    print(f" - core root: {core_root}")
    print(f" - timeline root: {timeline_root}")
    print(f" - base ref: {base_ref}")
    print(f" - direction: {direction}")
    print(f" - fail on warn: {args.fail_on_warn}")
    print(f" - watched override/carrier paths: {len(watched_paths)}")
    print(f" - FAIL: {counts['FAIL']}")
    print(f" - WARN: {counts['WARN']}")
    print(f" - INFO: {counts['INFO']}")
    print(f" - OK: {counts['OK']}")

    for severity in ("FAIL", "WARN", "INFO", "OK"):
        items = [item for item in diagnostics if item.severity == severity]
        if not items:
            continue
        print(f"\n[{severity}]")
        for item in items:
            print(f" - {item.relpath}: {item.message}")
            for sample in item.samples:
                print(f"   sample: {sample}")

    if counts["FAIL"]:
        return 1
    if args.fail_on_warn and counts["WARN"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
