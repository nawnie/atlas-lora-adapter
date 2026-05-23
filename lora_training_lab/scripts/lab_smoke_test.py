#!/usr/bin/env python3
"""
Atlas Reader LoRA lab install smoke test.

Checks:
- Python version
- core training imports
- PyTorch CUDA visibility
- TensorBoard import
"""

from __future__ import annotations

import importlib
import json
import platform
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_import(name: str):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        return True, version, None
    except Exception as exc:
        return False, None, str(exc)


def main() -> int:
    report = {
        "python": sys.version,
        "platform": platform.platform(),
        "checks": {},
    }

    print("Python:", sys.version)
    if sys.version_info[:2] != (3, 10):
        print("WARNING: This lab installer targets Python 3.10.")
        report["python_warning"] = "not_python_3_10"

    required = [
        "torch",
        "transformers",
        "datasets",
        "accelerate",
        "peft",
        "trl",
        "safetensors",
        "tensorboard",
    ]
    optional = ["bitsandbytes"]

    ok = True
    for name in required + optional:
        success, version, error = check_import(name)
        report["checks"][name] = {"ok": success, "version": version, "error": error}
        label = "OK" if success else ("WARN" if name in optional else "FAIL")
        print(f"{label}: {name} {version if version else error}")
        if not success and name in required:
            ok = False

    try:
        import torch
        print("torch version:", torch.__version__)
        print("cuda available:", torch.cuda.is_available())
        report["torch_cuda_available"] = bool(torch.cuda.is_available())
        if torch.cuda.is_available():
            print("cuda device:", torch.cuda.get_device_name(0))
            print("cuda capability:", torch.cuda.get_device_capability(0))
            report["cuda_device"] = torch.cuda.get_device_name(0)
            report["cuda_capability"] = torch.cuda.get_device_capability(0)
        else:
            ok = False
            print("FAIL: CUDA is not available to PyTorch.")
    except Exception as exc:
        ok = False
        report["torch_runtime_error"] = str(exc)
        print("FAIL: torch runtime check failed:", exc)

    out = ROOT / "lab_smoke_test_report.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Wrote:", out)

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
