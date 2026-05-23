#!/usr/bin/env python3
"""Summarize Atlas Reader LoRA evaluation result CSV files."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


SCORE_COLUMNS = [
    "grounding",
    "exactness",
    "actionability",
    "retrieval_discipline",
    "beginner_safety",
    "format_fit",
    "uncertainty_handling",
]


def to_float(value: str) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/summarize_results.py evaluation/RESULTS_TEMPLATE.csv")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Results file not found: {path}")
        return 2

    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
    if not rows:
        print("No result rows found.")
        return 0

    scored = [r for r in rows if any((r.get(c) or "").strip() for c in SCORE_COLUMNS)]
    if not scored:
        print("No scored rows found yet.")
        return 0

    print(f"Rows: {len(rows)}")
    print(f"Scored rows: {len(scored)}")

    for col in SCORE_COLUMNS:
        vals = [to_float(r.get(col, "")) for r in scored]
        print(f"{col}: avg={sum(vals)/len(vals):.2f}")

    pass_values = [r.get("pass_fail", "").lower() for r in scored]
    passes = sum(1 for v in pass_values if v in {"pass", "passed", "true", "1"})
    print(f"Pass rate: {passes}/{len(scored)} = {passes/len(scored):.1%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
