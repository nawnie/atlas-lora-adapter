# Evaluation

This folder defines how Atlas Reader LoRA experiments should be tested.

## Core comparison

```text
base model, no RAG
base model + raw RAG
base model + Atlas RAG
base model + Atlas Reader LoRA + Atlas RAG
```

Run the same questions across each condition.

## Key files

| File | Purpose |
|---|---|
| `EVALUATION_PLAN.md` | Methodology |
| `RUBRIC.md` | Scoring rubric |
| `BASELINE_MATRIX.md` | Comparison matrix |
| `GOLDEN_QUESTIONS_SEED.jsonl` | Starter evaluation questions |
| `RESULTS_TEMPLATE.csv` | Results entry template |
