#!/usr/bin/env python3
"""
Validate Atlas Reader Mini training records.

Usage:
    python scripts/validate_training_records.py
    python scripts/validate_training_records.py path/to/file.jsonl
"""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / "04_training_data" / "SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl"

RECORD_TYPES = {
    "route_primary_lane",
    "select_cards",
    "ignore_distractor",
    "secondary_lane_reference",
    "exactness_guard",
    "insufficient_context",
    "freshness_check",
    "answer_pattern",
}


def validate_record(record, line_no):
    issues = []
    required = [
        "record_id",
        "dataset_version",
        "record_type",
        "contract_id",
        "user_query",
        "context_pack",
        "expected_route",
        "expected_answer",
        "quality_flags",
    ]

    for field in required:
        if field not in record:
            issues.append(f"line {line_no}: missing {field}")

    if record.get("record_type") not in RECORD_TYPES:
        issues.append(f"line {line_no}: invalid record_type {record.get('record_type')}")

    pack = record.get("context_pack", {})
    cards = pack.get("cards", [])
    if not isinstance(cards, list) or not cards:
        issues.append(f"line {line_no}: context_pack.cards must be a non-empty list")
    if len(cards) > 5:
        issues.append(f"line {line_no}: context_pack has {len(cards)} cards; max is 5")

    primary = pack.get("primary_lane_id")
    if not primary:
        issues.append(f"line {line_no}: context_pack.primary_lane_id missing")

    for idx, card in enumerate(cards, start=1):
        for field in [
            "lane_id",
            "card_id",
            "card_type",
            "title",
            "canonical_summary",
            "source_priority_rule",
            "do_not_confuse_with",
            "answer_pattern",
            "exactness_guard",
        ]:
            if field not in card:
                issues.append(f"line {line_no}: card {idx} missing {field}")

    route = record.get("expected_route", {})
    if route.get("primary_lane_id") != primary:
        issues.append(f"line {line_no}: expected_route.primary_lane_id does not match context_pack.primary_lane_id")

    answer = record.get("expected_answer", {})
    if not answer.get("answer"):
        issues.append(f"line {line_no}: expected_answer.answer missing")
    if "limits" not in answer:
        issues.append(f"line {line_no}: expected_answer.limits missing")

    return issues


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    issues = []
    count = 0

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        count += 1
        try:
            record = json.loads(line)
        except Exception as exc:
            issues.append(f"line {line_no}: invalid JSON: {exc}")
            continue
        issues.extend(validate_record(record, line_no))

    print(f"Records checked: {count}")
    if issues:
        print("FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
