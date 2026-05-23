# Training

This folder contains the dataset design for Atlas Reader LoRA training.

## Principle

Do not train on raw Atlas dumps.

Train on structured examples:

```text
user question + retrieved context + metadata -> correct RAG-aware answer
```

## Files

| File | Purpose |
|---|---|
| `TRAINING_DATA_SCHEMA.json` | JSON schema for training records |
| `SAMPLE_RECORDS.jsonl` | Starter examples |
| `TRAINING_EXAMPLE_TYPES.md` | Explanation of task types |
| `DATASET_BUILD_PLAN.md` | How to expand from samples to dataset |
| `DATASET_CARD_TEMPLATE.md` | Dataset card template for future releases |

## Validation

Run:

```powershell
python scripts/validate_training_records.py training/SAMPLE_RECORDS.jsonl training/TRAINING_DATA_SCHEMA.json
```
