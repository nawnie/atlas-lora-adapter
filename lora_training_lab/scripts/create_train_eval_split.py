#!/usr/bin/env python3
"""
Create deterministic train/eval JSONL split for Atlas training records.

Usage:
    python scripts/create_train_eval_split.py input.jsonl --train-out 04_training_data/train.jsonl --eval-out 04_training_data/eval.jsonl --eval-ratio 0.15
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def read_jsonl(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("--train-out", type=Path, required=True)
    ap.add_argument("--eval-out", type=Path, required=True)
    ap.add_argument("--eval-ratio", type=float, default=0.15)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rows = read_jsonl(args.input)
    if not rows:
        print("No records found.")
        return 2

    random.seed(args.seed)
    random.shuffle(rows)

    eval_count = max(1, int(round(len(rows) * args.eval_ratio)))
    eval_rows = rows[:eval_count]
    train_rows = rows[eval_count:]

    write_jsonl(args.train_out, train_rows)
    write_jsonl(args.eval_out, eval_rows)

    print(f"Input records: {len(rows)}")
    print(f"Train records: {len(train_rows)} -> {args.train_out}")
    print(f"Eval records: {len(eval_rows)} -> {args.eval_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
