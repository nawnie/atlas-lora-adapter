# Runnable Training Layer

Status: implemented script layer  
Version added: v0.2.9-dev7

## What this adds

```text
scripts/train_atlas_reader_qlora.py
scripts/create_train_eval_split.py
requirements-training.txt
tools/powershell/train_atlas_reader.ps1
tools/powershell/dry_run_training_config.ps1
```

## Important

This does not mean the project has trained an adapter.

It means the repo now has a runnable training layer ready for a properly QC'd dataset.

## Preflight

From the repo root:

```powershell
python scripts\validate_training_records.py 04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python scripts\check_training_record_quality.py 04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
```

The sample records are still scaffold examples.

Do not use them as the final training dataset.

## Create a train/eval split

```powershell
python scripts\create_train_eval_split.py `
  04_training_data\YOUR_REAL_RECORDS.jsonl `
  --train-out 04_training_data\train.jsonl `
  --eval-out 04_training_data\eval.jsonl `
  --eval-ratio 0.15
```

## Update a config

Edit one of:

```text
06_experiments/training_configs/A_sanity_r8_lr0001.json
06_experiments/training_configs/B_baseline_r16_lr0002.json
```

Set:

```json
"base_model": "your-local-or-HF-model",
"dataset_train": "04_training_data/train.jsonl",
"dataset_eval": "04_training_data/eval.jsonl"
```

## Dry run

```powershell
python scripts\train_atlas_reader_qlora.py `
  --config 06_experiments\training_configs\A_sanity_r8_lr0001.json `
  --dry-run
```

## Training run

```powershell
python scripts\train_atlas_reader_qlora.py `
  --config 06_experiments\training_configs\A_sanity_r8_lr0001.json
```

## Output

Each run writes under:

```text
06_experiments/runs/<run_id>/
```

Expected files:

```text
config_used.json
runtime_info.json
adapter/
train_metrics.json
run_summary.json
```

## Recommended first run

Start with:

```text
A_sanity_r8_lr0001
```

Then:

```text
B_baseline_r16_lr0002
C_capacity_r32_lr0001
```

## Stop conditions

Stop if the model:

- repeats lane labels instead of answering;
- invents exact commands, paths, versions, or licenses;
- overuses secondary lanes;
- ignores freshness checks;
- only learns scaffold/meta phrasing.


## Training-code citations

The runnable training layer should cite:

```text
hf_trl_sfttrainer
hf_peft_loraconfig
hf_transformers_bitsandbytes
hf_transformers_trainer
hu2021lora
dettmers2023qlora
```

See:

```text
10_source_materials/CITATION_MATRIX.md
10_source_materials/REFERENCES.bib
```


## Additional implementation citations

```text
hf_datasets_docs
hf_accelerate_docs
hf_safetensors_docs
```

These cover dataset handling, training-stack orchestration, and safe tensor serialization dependencies.


## TensorBoard dashboard

Training configs now default to TensorBoard logging:

```json
"report_to": "tensorboard"
```

Start the local dashboard:

```powershell
tools\powershell\start_tensorboard.ps1
```

Default URL:

```text
http://127.0.0.1:6006
```

Details:

```text
04_training_data/TENSORBOARD_TRAINING_DASHBOARD.md
```

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
