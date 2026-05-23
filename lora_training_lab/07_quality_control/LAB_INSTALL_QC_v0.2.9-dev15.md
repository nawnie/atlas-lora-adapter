# Lab Install QC v0.2.9-dev15

Status: labinstall hardening/QC pass  
Date: 2026-05-22

## QC focus

This pass checks and hardens the Windows/Python 3.10 lab installer before running it on the user's machine.

## Updated

```text
labinstall.bat
tools/powershell/start_tensorboard.ps1
requirements-training.txt
04_training_data/LAB_INSTALL_GUIDE.md
10_source_materials/CITATION_REGISTRY.json
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/CITATION_MATRIX.md
10_source_materials/REFERENCES.bib
```

## Added

```text
scripts/qc_labinstall_static.py
07_quality_control/LAB_INSTALL_STATIC_QC.generated.json
07_quality_control/LAB_INSTALL_QC_v0.2.9-dev15.md
09_research_notes/PROJECT_STATUS_v0.2.9-dev15.md
```

## Hardening applied

- Added fallback from `py -3.10` to plain `python` if plain `python` is Python 3.10.
- Added optional `nvidia-smi` check.
- Preserved CUDA fallbacks: `cu128`, `cu126`, `cu118`, `cpu`.
- Updated `bitsandbytes` requirement to `bitsandbytes>=0.49.2`.
- Improved TensorBoard launcher to try `tensorboard` command first, then `python -m tensorboard.main`.
- Added static QC script for installer files.

## Compile check

- `scripts/lab_smoke_test.py`: passed
- `scripts/qc_labinstall_static.py`: passed

## Static QC return code

```text
0
```

## Static QC output

```json
{
  "files": {
    "labinstall.bat": true,
    "tools/powershell/labinstall.ps1": true,
    "tools/powershell/start_tensorboard.ps1": true,
    "scripts/lab_smoke_test.py": true,
    "requirements-training.txt": true,
    "04_training_data/LAB_INSTALL_GUIDE.md": true
  },
  "checks": {
    "checks_py310": true,
    "creates_venv310": true,
    "installs_pytorch_from_index": true,
    "supports_cu128": true,
    "supports_cu126": true,
    "supports_cu118": true,
    "supports_cpu": true,
    "runs_smoke_test": true,
    "writes_pip_freeze": true
  },
  "issues": [],
  "passed": true
}

Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/generated/interface/models.py", line 48821, in hydrate_crdt_from_proto
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/remote.py", line 747, in __call__
  File "/tmp/tmp.9eeVjt35CN/artifact_tool_v2-2.7.5/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## Source check

PyTorch official docs currently state latest stable PyTorch requires Python 3.10 or later, Windows supports Python 3.10-3.14, CUDA builds are selected from the official wheel index, and CUDA can be verified with `torch.cuda.is_available()`.

bitsandbytes official docs currently list Python >= 3.10, PyTorch >= 2.4, NVIDIA CUDA support, NF4/FP4 support, and Windows x86-64 CUDA wheel support.

## Boundary

This is static/install QC.

It does not install packages in this environment and does not train an adapter.
