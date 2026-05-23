#!/usr/bin/env python3
"""
Strict quality check for Atlas Reader Mini training records.

This is not a JSON Schema validator. It checks for common training-quality risks.

Usage:
    python scripts/check_training_record_quality.py
    python scripts/check_training_record_quality.py path/to/file.jsonl
"""

from pathlib import Path
import json
import sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / "04_training_data" / "SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl"

SCAFFOLD_PHRASES = [
    "route this to",
    "route to `",
    "use the selected cards",
    "generated scaffold",
    "seed training record",
    "this is a routing-discipline example",
]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    warnings = []
    type_counts = Counter()
    count = 0

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        count += 1
        record = json.loads(line)
        rid = record.get("record_id", f"line-{line_no}")
        rtype = record.get("record_type", "UNKNOWN")
        type_counts[rtype] += 1

        cards = record.get("context_pack", {}).get("cards", [])
        if len(cards) > 5:
            warnings.append(f"{rid}: too many context cards")
        if not cards:
            warnings.append(f"{rid}: no context cards")

        answer = record.get("expected_answer", {}).get("answer", "").lower()
        limits = record.get("expected_answer", {}).get("limits", "").lower()

        if any(phrase in answer or phrase in limits for phrase in SCAFFOLD_PHRASES):
            warnings.append(f"{rid}: scaffold/meta answer; not production SFT quality")

        if rtype == "ignore_distractor" and not record.get("expected_route", {}).get("ignored_card_ids"):
            warnings.append(f"{rid}: ignore_distractor record has no ignored_card_ids")

        if rtype == "secondary_lane_reference" and not record.get("expected_route", {}).get("secondary_lane_ids"):
            warnings.append(f"{rid}: secondary_lane_reference has no secondary_lane_ids")

        if record.get("quality_flags", {}).get("requires_freshness_check"):
            if "verify" not in answer and "qualif" not in answer and "current" not in answer:
                warnings.append(f"{rid}: freshness flag set but answer may not require verification/qualification")

    print(f"Records checked: {count}")
    print("Record type counts:")
    for key, value in sorted(type_counts.items()):
        print(f"- {key}: {value}")

    if warnings:
        print("WARNINGS")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print("PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
