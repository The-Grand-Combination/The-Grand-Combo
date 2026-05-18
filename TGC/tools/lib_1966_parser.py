from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict


class TopLevelBlockMeta(TypedDict):
    key: str
    area: str | None
    year: int | None
    file: str

ROOT = Path(__file__).resolve().parents[2]

DEFAULT_CORE_ROOT = "TGC"
DEFAULT_TIMELINE_ROOT = "TGC_Timeline_1966"


def resolve_repo_path(rel_path: str) -> Path:
    return ROOT / rel_path


def rebase_path(rel_path: str, *, core_root: str = DEFAULT_CORE_ROOT, timeline_root: str = DEFAULT_TIMELINE_ROOT) -> str:
    """Map manifest/rule paths to caller-selected roots while keeping defaults submod-aware."""
    if core_root != DEFAULT_CORE_ROOT and rel_path.startswith(f"{DEFAULT_CORE_ROOT}/"):
        return f"{core_root}/{rel_path[len(DEFAULT_CORE_ROOT) + 1:]}"
    if timeline_root != DEFAULT_TIMELINE_ROOT and rel_path.startswith(f"{DEFAULT_TIMELINE_ROOT}/"):
        return f"{timeline_root}/{rel_path[len(DEFAULT_TIMELINE_ROOT) + 1:]}"
    return rel_path

def read_text(rel_path: str, encoding: str = "utf-8") -> str:
    return resolve_repo_path(rel_path).read_text(encoding=encoding, errors="ignore")


def parse_top_level_blocks(rel_path: str) -> dict[str, list[tuple[int, str]]]:
    lines = read_text(rel_path).splitlines()
    ordered_blocks: list[tuple[str, list[tuple[int, str]]]] = []
    i = 0
    depth = 0
    while i < len(lines):
        line = lines[i]
        if depth == 0:
            m_open = re.match(r"\s*([a-z0-9_]+)\s*=\s*\{\s*(?:#.*)?$", line)
            if m_open:
                key = m_open.group(1)
                depth = 1
                i += 1
                block: list[tuple[int, str]] = []
                while i < len(lines) and depth > 0:
                    block.append((i + 1, lines[i]))
                    depth += lines[i].count("{") - lines[i].count("}")
                    i += 1
                ordered_blocks.append((key, block))
                depth = 0
                continue
        depth += line.count("{") - line.count("}")
        i += 1

    blocks: dict[str, list[tuple[int, str]]] = {}
    for key, block in ordered_blocks:
        blocks[key] = block
    return blocks


def parse_top_level_block_meta(rel_path: str) -> list[TopLevelBlockMeta]:
    out: list[TopLevelBlockMeta] = []
    for key, block in parse_top_level_blocks(rel_path).items():
        area = None
        year = None
        for _, line in block:
            if area is None:
                ma = re.match(r"\s*area\s*=\s*([a-z0-9_]+)", line)
                if ma:
                    area = ma.group(1)
            if year is None:
                my = re.match(r"\s*year\s*=\s*(\d+)", line)
                if my:
                    year = int(my.group(1))
            if area is not None and year is not None:
                break
        out.append({"key": key, "area": area, "year": year, "file": rel_path})
    return out
