#!/usr/bin/env python3
"""
Static QC for Atlas Reader lab installer files.

Usage:
    python scripts/qc_labinstall_static.py
"""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "labinstall.bat",
    "tools/powershell/labinstall.ps1",
    "tools/powershell/start_tensorboard.ps1",
    "scripts/lab_smoke_test.py",
    "requirements-training.txt",
    "04_training_data/LAB_INSTALL_GUIDE.md",
]

def main() -> int:
    issues = []
    files = {}
    for rel in REQUIRED:
        p = ROOT / rel
        files[rel] = p.exists()
        if not p.exists():
            issues.append(f"missing {rel}")

    bat = (ROOT / "labinstall.bat").read_text(encoding="utf-8") if (ROOT / "labinstall.bat").exists() else ""
    checks = {
        "checks_py310": "py -3.10" in bat and "python --version" in bat,
        "creates_venv310": ".venv310" in bat,
        "installs_pytorch_from_index": "download.pytorch.org/whl" in bat,
        "supports_cu128": "cu128" in bat,
        "supports_cu126": "cu126" in bat,
        "supports_cu118": "cu118" in bat,
        "supports_cpu": "cpu" in bat,
        "runs_smoke_test": "lab_smoke_test.py" in bat,
        "writes_pip_freeze": "lab_pip_freeze.txt" in bat,
    }
    for key, passed in checks.items():
        if not passed:
            issues.append(f"failed check: {key}")

    req = (ROOT / "requirements-training.txt").read_text(encoding="utf-8") if (ROOT / "requirements-training.txt").exists() else ""
    if "bitsandbytes>=0.49.2" not in req:
        issues.append("requirements-training.txt should pin bitsandbytes>=0.49.2 or newer")
    if "tensorboard" not in req.lower():
        issues.append("requirements-training.txt missing tensorboard")

    report = {
        "files": files,
        "checks": checks,
        "issues": issues,
        "passed": not issues,
    }
    out = ROOT / "07_quality_control" / "LAB_INSTALL_STATIC_QC.generated.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if not issues else 1

if __name__ == "__main__":
    raise SystemExit(main())
