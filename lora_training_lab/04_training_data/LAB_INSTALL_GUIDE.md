# Lab Install Guide

Status: install helper added  
Version added: v0.2.9-dev14  
Target: Windows + Python 3.10 + NVIDIA GPU

## Main installer

From the repo root:

```cmd
labinstall.bat
```

Default PyTorch build:

```text
cu128
```

Alternative builds:

```cmd
labinstall.bat cu126
labinstall.bat cu118
labinstall.bat cpu
```

## What it does

The installer:

1. checks for Python 3.10 through `py -3.10`;
2. creates `.venv310`;
3. upgrades pip/setuptools/wheel;
4. installs PyTorch from the selected PyTorch wheel index;
5. installs `requirements-training.txt`;
6. runs `scripts/lab_smoke_test.py`;
7. writes `lab_pip_freeze.txt`.

## Why Python 3.10

The user environment target is Python 3.10.

PyTorch's current Windows install page states that PyTorch on Windows supports Python 3.10-3.14 and that the latest stable PyTorch requires Python 3.10 or later [pytorch_get_started].

## TensorBoard

After install:

```powershell
tools\powershell\start_tensorboard.ps1
```

Default URL:

```text
http://127.0.0.1:6006
```

## First dry run

After real train/eval data exists and config paths are set:

```cmd
python scripts\train_atlas_reader_qlora.py --config 06_experiments\training_configs\A_sanity_r8_lr0001.json --dry-run
```

## Notes

Fast internet helps with model and package downloads, but the installer still checks the environment because most failures come from:

- wrong Python version;
- wrong venv;
- PyTorch CPU build accidentally installed;
- CUDA not visible to PyTorch;
- missing training packages.

## Source basis

- PyTorch's official local install page provides the current Windows/Python support and pip/CUDA wheel guidance [pytorch_get_started].
- Hugging Face's TRL/PEFT/Transformers docs support the training stack used by this project.


## v0.2.9-dev15 QC notes

The installer was hardened to:

- fall back from `py -3.10` to plain `python` if plain `python` is Python 3.10;
- run an optional `nvidia-smi` check before install;
- keep CUDA build fallbacks: `cu128`, `cu126`, `cu118`, and `cpu`;
- use `bitsandbytes>=0.49.2`;
- warn clearly if the smoke test fails;
- check TensorBoard import after install.

## bitsandbytes Windows note

The bitsandbytes installation guide lists Python >= 3.10 and PyTorch >= 2.4 as minimum requirements, and currently lists Windows x86-64 wheels for NVIDIA CUDA 11.8-12.6 and 12.8-12.9 builds [hf_bitsandbytes_install].

If bitsandbytes fails, try:

```cmd
labinstall.bat cu126
labinstall.bat cu118
python -m pip install --upgrade bitsandbytes
```

## Static installer QC

Run:

```cmd
python scripts\qc_labinstall_static.py
```

This checks that the installer files and expected CUDA fallback paths exist.


## AIWF note

This installer is part of the AI Without Fear lab workflow:

```text
install cleanly
test honestly
watch the graphs
save the logs
do not claim victory until the run earns it
```

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
