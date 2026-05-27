# Evaluation Utilities

This folder contains lightweight, repo-safe evaluation helpers.

These utilities do not require:

- GPU access;
- model weights;
- adapter artifacts;
- raw zip archives;
- private lab files.

## Available Script

```bash
python evals/summarize_previous_results.py
```

The script reads:

```text
05_evaluation/previous_adapter_results/RESULTS_SUMMARY.csv
```

and prints a small Markdown table with pass counts, pass rates, token counts, and notes.

## Scope

This folder summarizes already-recorded result files. It is not the full model-evaluation harness.

The training/evaluation lab lives under:

```text
lora_training_lab/
```
