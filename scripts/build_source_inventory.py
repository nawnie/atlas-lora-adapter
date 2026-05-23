#!/usr/bin/env python3
"""
Build/update source and training-code inventory.

Usage:
    python scripts/build_source_inventory.py
"""

from pathlib import Path
import hashlib
import json
import datetime


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "10_source_materials"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def categorize(path: Path) -> str:
    rp = rel(path)
    if rp.startswith("10_source_materials/"):
        return "source_material"
    if rp.startswith("scripts/") or rp.startswith("tools/powershell/") or rp == "requirements-training.txt":
        return "training_or_repo_code"
    if rp.startswith("06_experiments/training_configs/"):
        return "training_config"
    if rp.startswith("03_lane_system/"):
        return "lane_card_source"
    if rp.startswith("04_training_data/"):
        return "training_data_design"
    if rp.startswith("05_evaluation/"):
        return "evaluation_design"
    if rp.startswith("01_strategy/"):
        return "strategy_and_claim_governance"
    if rp.startswith("07_quality_control/"):
        return "quality_control"
    if rp.startswith("08_visuals/"):
        return "visual_asset"
    if rp.startswith("09_research_notes/"):
        return "research_note"
    return "repo_root_or_other"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = [p for p in sorted(ROOT.rglob("*")) if p.is_file() and ".git" not in p.parts]
    records = []
    training_code = []

    for p in files:
        record = {
            "path": rel(p),
            "category": categorize(p),
            "bytes": p.stat().st_size,
            "sha256": sha256(p),
        }
        records.append(record)
        if (
            record["path"].startswith("scripts/")
            or record["path"].startswith("tools/powershell/")
            or record["path"].startswith("06_experiments/training_configs/")
            or record["path"] == "requirements-training.txt"
        ):
            training_code.append(record)

    payload = {
        "generated_utc": datetime.datetime.now(datetime.UTC).isoformat(),
        "policy": "AI assistants are drafting aids, not sources.",
        "training_code_count": len(training_code),
        "file_count": len(records),
        "training_code": training_code,
        "files": records,
    }

    (OUT_DIR / "SOURCE_INVENTORY.generated.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_DIR / 'SOURCE_INVENTORY.generated.json'}")
    print(f"Files: {len(records)}")
    print(f"Training/code files: {len(training_code)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
