# AI Without Fear — Atlas Reader LoRA Lab

<p align="center">
  <img src="08_visuals/AIWF_LOGO.png" alt="AI Without Fear logo" width="220">
</p>

## Executive Summary

- **Structured-RAG adapter lab:** Atlas Reader LoRA tests whether a lightweight LoRA adapter can learn to follow a lane/card knowledge map instead of treating retrieved context as a flat text dump.
- **Internal token-efficiency signal:** in the recorded internal evals, compact selected-card prompts averaged **651.4 total tokens** versus **3292.1 total tokens** for the available raw workspace/RAG comparison, about **5.05x fewer tokens** under this lab setup.
- **Current best direction:** the O mixed-schema off-ramp adapter preserved compact-card performance, improved targeted retrieval behavior, and added a boundary path for questions not supported by Atlas evidence.

This is a research/evaluation repo, not a production package or external benchmark claim.

## Performance Benchmarks

Current best evaluated run:

```text
O_mixed_schema_offramp_4b_r16_lr0001_1epoch
```

| Eval | O Result | Avg total tokens | Notes |
|---|---:|---:|---|
| Compact seed cards | 65/65 | 651.4 | Preserved previous best compact-card result |
| Targeted top-1 card | 64/65 | 423.6 | One source-label failure |
| Targeted top-3 cards | 65/65 | 660.3 | Passed targeted distractor-card eval |
| Off-ramp / boundary eval | 8/8 | 421.3 | Tests behavior when Atlas evidence is absent |
| Exact-ID / schema eval | 14/16 | 742.0 | Remaining weak edge |

Prior raw-context comparison:

| Path | Avg total tokens | Internal result |
|---|---:|---|
| Compact O selected-card prompt | 651.4 | 65/65 compact eval |
| Raw workspace/RAG comparison | 3292.1 | 0/65 in available 4B raw workspace comparison |

Under the recorded internal evaluation conditions, the compact selected-card path used about **5.05x fewer total tokens** than the available raw workspace/RAG comparison. This is not a universal cost-reduction claim; it is evidence for this lab's retrieval-card design.

## Why This Matters for Enterprise RAG

### Token Cost Bottleneck

Standard RAG can push large context blocks into the model. That increases token cost, latency, and noise. Atlas-style retrieval cards test whether the model can use a compact index/map instead of a full workspace dump.

### Retrieval Discipline

The project tests whether an adapter can learn behaviors enterprise teams care about:

- choose the correct lane/card;
- ignore distractor context;
- follow source hierarchy;
- avoid unsupported exact identifiers;
- answer from structured evidence instead of guessing.

### Boundary / Off-Ramp Behavior

The O run adds explicit off-ramp behavior. When Atlas evidence is absent, the model should not force the nearest Atlas lane. It should route to the appropriate fallback path: stable pretrained knowledge, current-source verification for volatile facts, or user-provided files for private/local facts.

## Quick Start

This repo is currently structured as a research/evaluation lab. A stable Python package API is not claimed yet.

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
Knowledge = Atlas / RAG cards
Behavior = LoRA adapter
Proof = saved evaluation outputs
```

The adapter is not intended to memorize the Atlas. It is trained to improve how the model reads structured context.

## Current Status

Current best internal adapter:

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
- a universal 80% token reduction claim.

## Repo Map

| Path | Purpose |
|---|---|
| `docs/atlas/o_mixed_schema_offramp/` | O mixed-schema off-ramp evaluation archive |
| `05_evaluation/previous_adapter_results/` | Prior J/K/L/N/workspace result summaries |
| `evals/` | Lightweight result-summary tooling |
| `lora_training_lab/` | Training and evaluation lab scaffolding |
| `lora_training_lab/requirements-training.txt` | Training-stack dependencies |
| `01_strategy/` | Strategy, source policy, and claim boundaries |
| `03_lane_system/` | Atlas lane/card source structure |
| `08_visuals/` | Concept diagrams and branding visuals |
| `scripts/` | Repo validation helpers |

## Next Evaluation Step

The next planned run is P: a focused cleanup pass for exact-ID/schema behavior.

Target:

```text
preserve O's targeted retrieval gains
improve exact-ID/schema eval from 14/16 toward 16/16
keep answer wording clean instead of echoing synthetic test language
```

## Source Policy

Citable evidence for this project comes from:

- primary papers;
- official docs;
- official repositories/model cards;
- measured local outputs;
- project-authored notes clearly marked as drafts or internal reasoning.

AI assistants and drafting tools are not evidence sources.

See:

```text
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
```
