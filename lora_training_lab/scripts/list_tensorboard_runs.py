#!/usr/bin/env python3
"""
List TensorBoard event files under experiment runs.

Usage:
    python scripts/list_tensorboard_runs.py
"""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "06_experiments" / "runs"
def main() -> int:
    event_files = sorted(RUNS.rglob("events.out.tfevents.*")) if RUNS.exists() else []
    print(f"TensorBoard event files found: {len(event_files)}")
    for p in event_files:
        print(str(p.relative_to(ROOT)).replace("\\", "/"))
    out = {"runs_dir": str(RUNS.relative_to(ROOT)).replace("\\", "/"), "event_file_count": len(event_files), "event_files": [str(p.relative_to(ROOT)).replace("\\", "/") for p in event_files]}
    (ROOT / "06_experiments" / "tensorboard_event_inventory.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
