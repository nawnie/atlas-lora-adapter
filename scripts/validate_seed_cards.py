#!/usr/bin/env python3
"""
Validate Atlas seed lane cards.

Usage:
    python scripts/validate_seed_cards.py
"""

from pathlib import Path
import json
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
LANES = ROOT / "03_lane_system" / "lanes"

REQUIRED_LANE_FILES = [
    "CANONICAL_OVERVIEW.md",
    "CONCEPT_MAP.md",
    "RETRIEVAL_CARDS.jsonl",
    "SOURCE_COVERAGE.md",
    "FAILURE_SIGNATURES.md",
    "QA_TEST_PROMPTS.md",
    "ANSWER_PATTERNS.md",
    "DO_NOT_CONFUSE_WITH.md",
    "GAP_AUDIT_AND_VOL2_QUEUE.md",
    "lane_profile.json",
]

REQUIRED_CARD_FIELDS = [
    "card_id",
    "lane_id",
    "card_type",
    "title",
    "user_phrasing",
    "canonical_summary",
    "must_retrieve",
    "source_priority_rule",
    "do_not_confuse_with",
    "answer_pattern",
    "exactness_guard",
    "needs_current_verification",
    "risk_level",
]

EXPECTED_MIX = {
    "concept": 4,
    "failure_signature": 3,
    "diagnostic_branch": 2,
    "source_priority": 1,
    "do_not_confuse": 1,
    "answer_pattern": 1,
}

VALID_TYPES = set(EXPECTED_MIX)
VALID_RISKS = {"low", "medium", "high"}


def main() -> int:
    issues = []
    cards = []

    for lane_dir in sorted(p for p in LANES.iterdir() if p.is_dir()):
        lane_id = lane_dir.name

        for filename in REQUIRED_LANE_FILES:
            if not (lane_dir / filename).exists():
                issues.append(f"{lane_id}: missing {filename}")

        jsonl = lane_dir / "RETRIEVAL_CARDS.jsonl"
        if not jsonl.exists():
            continue

        for line_no, line in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                card = json.loads(line)
            except Exception as exc:
                issues.append(f"{lane_id}:{line_no}: invalid JSON: {exc}")
                continue

            cards.append(card)

            for field in REQUIRED_CARD_FIELDS:
                if field not in card:
                    issues.append(f"{lane_id}:{card.get('card_id', 'UNKNOWN')}: missing field {field}")

            if card.get("lane_id") != lane_id:
                issues.append(f"{lane_id}:{card.get('card_id')}: lane_id mismatch: {card.get('lane_id')}")

            if card.get("card_type") not in VALID_TYPES:
                issues.append(f"{lane_id}:{card.get('card_id')}: invalid card_type {card.get('card_type')}")

            if card.get("risk_level") not in VALID_RISKS:
                issues.append(f"{lane_id}:{card.get('card_id')}: invalid risk_level {card.get('risk_level')}")

            for array_field in ["user_phrasing", "must_retrieve", "do_not_confuse_with"]:
                if not isinstance(card.get(array_field), list) or not card.get(array_field):
                    issues.append(f"{lane_id}:{card.get('card_id')}: {array_field} must be non-empty list")

    by_lane = defaultdict(list)
    for card in cards:
        by_lane[card.get("lane_id", "UNKNOWN")].append(card)

    for lane_id, lane_cards in sorted(by_lane.items()):
        mix = Counter(card.get("card_type") for card in lane_cards)
        if len(lane_cards) != 12:
            issues.append(f"{lane_id}: expected 12 cards, found {len(lane_cards)}")
        if dict(mix) != EXPECTED_MIX:
            issues.append(f"{lane_id}: expected mix {EXPECTED_MIX}, found {dict(mix)}")

    duplicate_ids = [card_id for card_id, count in Counter(card.get("card_id") for card in cards).items() if count > 1]
    if duplicate_ids:
        issues.append(f"duplicate card IDs: {duplicate_ids}")

    print(f"Lanes checked: {len(by_lane)}")
    print(f"Cards checked: {len(cards)}")

    if issues:
        print("FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
