"""Summarize recorded Atlas adapter evaluation results.

This script is intentionally lightweight. It reads the repo-safe CSV summary and
prints a Markdown table. It does not load model weights, adapters, GPUs, or raw
lab archives.
"""

from __future__ import annotations

import csv
from pathlib import Path

RESULTS_PATH = Path(__file__).resolve().parents[1] / "05_evaluation" / "previous_adapter_results" / "RESULTS_SUMMARY.csv"


def parse_pass_count(value: str) -> tuple[int, int] | None:
    """Parse strings like '59/65' into integer numerator/denominator pairs."""
    if not value or "/" not in value:
        return None
    left, right = value.split("/", 1)
    try:
        return int(left), int(right)
    except ValueError:
        return None


def pass_rate(value: str) -> str:
    parsed = parse_pass_count(value)
    if parsed is None:
        return "n/a"
    passed, total = parsed
    if total == 0:
        return "n/a"
    return f"{(passed / total) * 100:.1f}%"


def main() -> None:
    if not RESULTS_PATH.exists():
        raise SystemExit(f"Missing results file: {RESULTS_PATH}")

    with RESULTS_PATH.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    headers = [
        "Run",
        "Adapter pass",
        "Adapter rate",
        "Base pass",
        "Base rate",
        "Adapter tokens",
        "Base tokens",
        "Key read",
    ]

    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")

    for row in rows:
        print(
            "| "
            + " | ".join(
                [
                    row.get("run", ""),
                    row.get("adapter_pass", ""),
                    pass_rate(row.get("adapter_pass", "")),
                    row.get("base_pass", ""),
                    pass_rate(row.get("base_pass", "")),
                    row.get("adapter_avg_total_tokens", ""),
                    row.get("base_avg_total_tokens", ""),
                    row.get("key_read", ""),
                ]
            )
            + " |"
        )


if __name__ == "__main__":
    main()
