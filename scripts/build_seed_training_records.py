#!/usr/bin/env python3
"""
Build seed Atlas Reader Mini training records from lane card JSONL files.

This script is intentionally conservative. It creates scaffold records for
manual review, not production-ready training data.

Usage:
    python scripts/build_seed_training_records.py
"""

from pathlib import Path
import json
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
LANES_ROOT = ROOT / "03_lane_system" / "lanes"
OUT = ROOT / "04_training_data" / "generated_seed_training_records.jsonl"

CONTRACT_ID = "atlas-contract_mini_128L-12C-5D_v1"
DATASET_VERSION = "atlas-reader-mini-generated-seed"


def load_cards():
    cards_by_lane = defaultdict(list)
    for lane_dir in sorted(p for p in LANES_ROOT.iterdir() if p.is_dir()):
        jsonl = lane_dir / "RETRIEVAL_CARDS.jsonl"
        if not jsonl.exists():
            continue
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            if line.strip():
                card = json.loads(line)
                cards_by_lane[card["lane_id"]].append(card)
    return cards_by_lane


def compact(card, secondary=False):
    return {
        "lane_id": card["lane_id"],
        "card_id": card["card_id"],
        "card_type": card["card_type"],
        "title": card["title"],
        "canonical_summary": card["canonical_summary"],
        "source_priority_rule": card["source_priority_rule"],
        "do_not_confuse_with": card["do_not_confuse_with"],
        "answer_pattern": card["answer_pattern"],
        "exactness_guard": card["exactness_guard"],
        "is_secondary_lane_card": secondary,
    }


def pick(cards, card_type, limit=1):
    return [c for c in cards if c["card_type"] == card_type][:limit]


def main():
    cards_by_lane = load_cards()
    records = []
    n = 1

    for lane_id, cards in sorted(cards_by_lane.items()):
        selected = []
        for t in ["concept", "failure_signature", "diagnostic_branch", "source_priority"]:
            selected.extend(pick(cards, t, 1))
        selected = selected[:5]

        if not selected:
            continue

        pack = [compact(c) for c in selected]
        records.append({
            "record_id": f"GEN-SEED-{n:05d}",
            "dataset_version": DATASET_VERSION,
            "record_type": "route_primary_lane",
            "contract_id": CONTRACT_ID,
            "user_query": f"Route this question to the correct Atlas lane: {lane_id}",
            "context_pack": {
                "contract_id": CONTRACT_ID,
                "max_cards": 5,
                "primary_lane_id": lane_id,
                "secondary_lane_ids": [],
                "cards": pack,
                "routing_rule": "Primary lane first. No secondary lane unless explicitly supported.",
                "notes": "Generated scaffold record; requires manual review."
            },
            "expected_route": {
                "primary_lane_id": lane_id,
                "secondary_lane_ids": [],
                "used_card_ids": [c["card_id"] for c in pack],
                "ignored_card_ids": []
            },
            "expected_answer": {
                "answer": f"Use `{lane_id}` as the primary lane. Answer from the selected cards and follow exactness/source-priority guards.",
                "limits": "Generated scaffold. Replace with a task-specific answer before production training.",
                "should_refuse_or_qualify": False
            },
            "quality_flags": {
                "has_distractor": False,
                "has_secondary_lane": False,
                "requires_freshness_check": any(c.get("needs_current_verification") for c in selected),
                "tests_exactness_guard": True,
                "is_smoke_test_record": True
            }
        })
        n += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(records)} records to {OUT}")


if __name__ == "__main__":
    main()
