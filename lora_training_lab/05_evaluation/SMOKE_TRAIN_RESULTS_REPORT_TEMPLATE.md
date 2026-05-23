# Smoke Train Results Report

Status: template  
Version added: v0.2.9-dev5

## Run metadata

| Field | Value |
|---|---|
| Date | TBD |
| Base model | TBD |
| Adapter name | TBD |
| Dataset version | TBD |
| Toolchain | TBD |
| Hardware | TBD |

## Evaluation matrix

| Arm | Condition | Result |
|---|---|---|
| A | base model, no RAG | TBD |
| B | base model + raw RAG | TBD |
| C | base model + Atlas RAG | TBD |
| D | base model + Atlas Reader LoRA + Atlas RAG | TBD |

## Significance

Paste output from:

```text
python scripts/compute_significance.py 05_evaluation/SMOKE_RESULTS.csv --a atlas_rag --b atlas_lora_rag
```

## Failure cases

| Question ID | Condition | Failure type | Notes |
|---|---|---|---|

## Go / hold / stop decision

```text
TBD
```

## Interpretation

Do not claim final proof from the smoke run.

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
