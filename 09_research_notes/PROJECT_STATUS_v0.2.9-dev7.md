# Project Status Note

Date: 2026-05-22  
Version: v0.2.9-dev7  
Status: runnable training layer added

## Summary

This update adds the first runnable TRL/PEFT QLoRA training layer.

## Added

- `scripts/train_atlas_reader_qlora.py`
- `scripts/create_train_eval_split.py`
- `requirements-training.txt`
- `04_training_data/RUNNABLE_TRAINING_LAYER.md`
- PowerShell launch helpers

## Current boundary

No adapter has been trained.

Do not run meaningful training on scaffold/meta records.

## Next step

Create answer-quality records, split train/eval, then run `A_sanity_r8_lr0001` as a dry run and first sanity train.
