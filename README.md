# AI Without Fear — Atlas Reader LoRA Lab

<p align="center">
  <img src="08_visuals/AIWF_LOGO.png" alt="AI Without Fear logo" width="220">
</p>

Atlas Reader LoRA is a research and evaluation lab for testing whether a lightweight LoRA adapter can improve how a small language model uses structured retrieval context.

The project focuses on a narrow question: can an adapter learn to follow an Atlas-style lane/card knowledge map instead of treating retrieved context as a flat text dump?

This is an early research repository, not a production package, external benchmark, or universal token-efficiency claim.

## Executive Summary

- **Structured retrieval behavior:** The adapter is trained to use compact Atlas cards, lane labels, source hierarchy, and boundary rules.
- **Recorded token-efficiency signal:** In the current internal evaluation set, compact selected-card prompts averaged **651.4 total tokens** versus **3292.1 total tokens** for the available raw workspace/RAG comparison. That is about **5.05x fewer tokens** under this lab setup.
- **Best current direction:** The strongest evaluated adapter preserved compact-card performance, improved targeted retrieval behavior, and added an off-ramp for questions not supported by Atlas evidence.
- **Evidence boundary:** Results are based on saved local evaluation outputs in this repository. They should be read as project evidence, not as broad claims about all RAG systems or all model sizes.

## Why This Matters

Standard RAG workflows often push large blocks of retrieved text into a model. That can increase token cost, latency, and distraction from irrelevant context.

Atlas-style retrieval tests a different pattern:

```text
large source corpus
-> structured lanes and cards
-> compact evidence pack
-> model answers from selected evidence
```

The LoRA experiment asks whether a small adapter can reinforce the behavior needed for that pattern:

- choose the correct lane or card;
- ignore distractor context;
- follow source hierarchy;
- avoid unsupported exact identifiers;
- use explicit fallback behavior when evidence is missing;
- answer from structured evidence instead of guessing.

## Current Best Evaluation

Current best evaluated adapter configuration:

```text
O_mixed_schema_offramp_4b_r16_lr0001_1epoch
```

| Evaluation | Result | Avg total tokens | Notes |
|---|---:|---:|---|
| Compact seed cards | 65/65 | 651.4 | Preserved previous best compact-card result |
| Targeted top-1 card | 64/65 | 423.6 | One source-label failure |
| Targeted top-3 cards | 65/65 | 660.3 | Passed targeted distractor-card eval |
| Off-ramp / boundary eval | 8/8 | 421.3 | Tests behavior when Atlas evidence is absent |
| Exact-ID / schema eval | 14/16 | 742.0 | Remaining weak edge |

Prior raw-context comparison:

| Path | Avg total tokens | Internal result |
|---|---:|---|
| Compact selected-card prompt | 651.4 | 65/65 compact eval |
| Raw workspace/RAG comparison | 3292.1 | 0/65 in available 4B raw workspace comparison |

Under the recorded internal evaluation conditions, the compact selected-card path used about **5.05x fewer total tokens** than the available raw workspace/RAG comparison. This is evidence for this lab's retrieval-card design, not a universal cost-reduction claim.

## How It Works

```text
user question
-> retrieval selects lane/card context
-> Atlas Reader LoRA biases the model toward structured context use
-> model answers from selected evidence
-> off-ramp behavior handles missing Atlas evidence
```

The design separates knowledge from behavior:

```text
Knowledge = Atlas cards, lanes, and source records
Behavior = LoRA adapter reading discipline
Proof = saved evaluation outputs
```

The adapter is not intended to memorize the Atlas. It is trained to improve how the model reads structured context.

## Current Adapter Snapshot

| Field | Value |
|---|---|
| Base model | `Qwen/Qwen1.5-4B-Chat` |
| Training method | QLoRA SFT |
| Quantization | 4-bit NF4, double quantization enabled |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Epochs | 1 |
| Learning rate | 0.0001 |
| Train records | 683 |
| Eval records | 129 |
| Train loss | 1.463968 |
| Eval loss | 0.827147 |
| Eval token accuracy | 0.834205 |

Result records:

```text
docs/atlas/o_mixed_schema_offramp/O_MIXED_SCHEMA_OFFRAMP_REPORT.md
05_evaluation/previous_adapter_results/PREVIOUS_ADAPTER_RESULTS_FROM_8ZIP.md
05_evaluation/previous_adapter_results/RESULTS_SUMMARY.csv
```

## Quick Start

This repository is structured as a research and evaluation lab. A stable Python package API is not claimed yet.

Lightweight repository checks:

```bash
python scripts/validate_seed_cards.py
python scripts/validate_training_records.py lora_training_lab/04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python lora_training_lab/scripts/qc_labinstall_static.py
python evals/summarize_previous_results.py
```

Training dependencies live separately in:

```text
lora_training_lab/requirements-training.txt
```

Install PyTorch for the target CUDA environment before installing the training stack.

## Repository Map

| Path | Purpose |
|---|---|
| `docs/atlas/o_mixed_schema_offramp/` | Best-run evaluation archive |
| `05_evaluation/previous_adapter_results/` | Prior adapter result summaries |
| `evals/` | Lightweight result-summary tooling |
| `lora_training_lab/` | Training and evaluation lab scaffolding |
| `lora_training_lab/requirements-training.txt` | Training-stack dependencies |
| `01_strategy/` | Strategy, source policy, and claim boundaries |
| `03_lane_system/` | Atlas lane/card source structure |
| `08_visuals/` | Concept diagrams and branding visuals |
| `scripts/` | Repo validation helpers |

## Near-Term Evaluation Plan

The next evaluation pass should focus on the remaining exact-ID and schema-following edge cases while preserving the targeted retrieval gains already recorded.

Primary goals:

- improve exact-ID/schema behavior from 14/16 toward 16/16;
- preserve compact-card and targeted top-3 performance;
- keep answer wording clean instead of echoing synthetic test language;
- expand hard negatives and boundary questions before making stronger generalization claims.

## What This Is Not

This project is **not** claiming:

- a new LoRA algorithm;
- a new foundation model;
- production readiness;
- external benchmark performance;
- broad cross-domain generalization;
- universal adapter portability across base models;
- global 4B parity with larger models;
- general hallucination elimination;
- a universal 80% token-reduction result.

## Source Policy

Citable evidence for this project comes from:

- primary papers;
- official docs;
- official repositories and model cards;
- measured local outputs;
- project-authored notes clearly marked as drafts, strategy, or internal reasoning.

Drafting tools and assistant-generated summaries are not evidence sources.

See:

```text
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
```
