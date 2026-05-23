#!/usr/bin/env python3
"""
Render Atlas training records into chat-style SFT JSONL.

Input records must follow TRAINING_RECORD_SCHEMA_V1.json.

Output format:
{"messages": [{"role":"system","content":"..."}, {"role":"user","content":"..."}, {"role":"assistant","content":"..."}]}

Usage:
    python scripts/render_atlas_sft_dataset.py input.jsonl output.chat.jsonl
"""

from pathlib import Path
import json
import sys


SYSTEM = """You are Atlas Reader Mini.
Follow the Atlas Contract.
Primary lane first.
Use no more than 5 cards.
Use secondary lanes only when selected cards justify it.
Answer from evidence.
Do not invent exact commands, paths, node names, versions, licenses, or current facts.
Qualify missing or stale evidence."""


def format_card(card):
    dnc = "; ".join(card.get("do_not_confuse_with", []))
    return (
        f"- {card.get('card_id')} | lane={card.get('lane_id')} | type={card.get('card_type')} | title={card.get('title')}\n"
        f"  summary: {card.get('canonical_summary')}\n"
        f"  source_rule: {card.get('source_priority_rule')}\n"
        f"  do_not_confuse_with: {dnc}\n"
        f"  answer_pattern: {card.get('answer_pattern')}\n"
        f"  exactness_guard: {card.get('exactness_guard')}\n"
    )


def render_record(record):
    pack = record["context_pack"]
    cards = "\n".join(format_card(c) for c in pack.get("cards", []))
    user = f"""Atlas Contract:
{record.get('contract_id')}

User Query:
{record.get('user_query')}

Primary Lane:
{pack.get('primary_lane_id')}

Secondary Lanes:
{', '.join(pack.get('secondary_lane_ids', [])) or 'none'}

Context Pack:
{cards}

Routing Rule:
{pack.get('routing_rule', 'Primary lane first.')}"""
    assistant = record["expected_answer"]["answer"]
    limits = record["expected_answer"].get("limits", "")
    if limits:
        assistant = assistant.rstrip() + "\n\nLimits: " + limits
    return {
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "metadata": {
            "record_id": record.get("record_id"),
            "record_type": record.get("record_type"),
            "primary_lane_id": pack.get("primary_lane_id"),
        }
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/render_atlas_sft_dataset.py input.jsonl output.chat.jsonl")
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    count = 0
    dst.parent.mkdir(parents=True, exist_ok=True)
    with src.open("r", encoding="utf-8") as fin, dst.open("w", encoding="utf-8") as fout:
        for line in fin:
            if not line.strip():
                continue
            record = json.loads(line)
            fout.write(json.dumps(render_record(record), ensure_ascii=False) + "\n")
            count += 1
    print(f"Rendered {count} records to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
