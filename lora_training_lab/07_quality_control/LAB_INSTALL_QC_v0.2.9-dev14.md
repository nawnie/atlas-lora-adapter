# Lab Install QC v0.2.9-dev14

Status: install helper QC pass  
Date: 2026-05-22

## Added

```text
labinstall.bat
tools/powershell/labinstall.ps1
scripts/lab_smoke_test.py
04_training_data/LAB_INSTALL_GUIDE.md
07_quality_control/LAB_INSTALL_QC_v0.2.9-dev14.md
09_research_notes/PROJECT_STATUS_v0.2.9-dev14.md
```

## Target

```text
Windows
Python 3.10
local venv: .venv310
NVIDIA CUDA PyTorch default: cu128
```

## Compile check

- `scripts/lab_smoke_test.py`: passed

## Installer behavior

The installer:

- checks `py -3.10`;
- creates `.venv310`;
- installs PyTorch from selected official PyTorch wheel index;
- installs training requirements;
- runs package/CUDA smoke test;
- writes `lab_pip_freeze.txt`.

## Source citation added

```text
pytorch_get_started
```

## Boundary

This installs the lab environment.

It does not train an adapter or prove model quality.
