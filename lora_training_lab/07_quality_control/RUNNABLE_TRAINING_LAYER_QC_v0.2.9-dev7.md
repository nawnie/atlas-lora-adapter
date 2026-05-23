# Runnable Training Layer QC v0.2.9-dev7

Status: compile/QC pass  
Date: 2026-05-22

## Added

```text
scripts/train_atlas_reader_qlora.py
scripts/create_train_eval_split.py
requirements-training.txt
04_training_data/RUNNABLE_TRAINING_LAYER.md
tools/powershell/dry_run_training_config.ps1
tools/powershell/train_atlas_reader.ps1
```

## Compile check

- `scripts/train_atlas_reader_qlora.py`: passed
- `scripts/create_train_eval_split.py`: passed
- `scripts/render_atlas_sft_dataset.py`: passed
- `scripts/compute_significance.py`: passed

## What this means

The repo now has a runnable TRL/PEFT QLoRA training script layer.

## What this does not mean

No adapter has been trained.

No performance result exists.

The sample records are still scaffold examples, not final SFT-quality data.

## Before running

1. Replace scaffold records with answer-quality records.
2. Create train/eval split.
3. Edit config `base_model`, `dataset_train`, and `dataset_eval`.
4. Run dry run.
5. Start with `A_sanity_r8_lr0001`.

## Version note

This is not a v0.3.0 promotion.
