# Smoke-Train Protocol

Status: executable protocol draft  
Version added: v0.2.9-dev5

## Goal

Run the smallest useful end-to-end experiment before scaling the Atlas Reader
LoRA project.

The smoke train should answer:

```text
Can we create real non-scaffold records?
Can we train a small adapter?
Can we compare no RAG / raw RAG / Atlas RAG / Atlas RAG + LoRA?
Can we detect whether scaling is justified?
```

## Recommended smoke lanes

```text
42_comfyui_socket_contract_debugging
44_video_vram_optimization
53_claim_freshness_verification
```

These test exactness, practical troubleshooting, secondary-lane routing,
and freshness restraint.

## Dataset target

```text
150 training records
```

Suggested mix:

```text
25 route_primary_lane
25 select_cards
25 ignore_distractor
20 secondary_lane_reference
25 exactness_guard
15 insufficient_context
15 freshness_check
```

Before training, review at least 50 records and all exactness/freshness/secondary-lane records.

## Four-arm evaluation

Run the same 25 golden questions through:

```text
A: base model, no RAG
B: base model + raw RAG
C: base model + Atlas RAG
D: base model + Atlas Reader LoRA + Atlas RAG
```

The key comparison is C vs D because it tests whether the LoRA adds value
beyond Atlas RAG alone.

## Scoring columns

```text
route_correct
source_grounded
exactness_guard
actionable
freshness_handled
avoids_distractor
compact_answer
pass
```

## Statistics

Use paired tests because the same questions are used across conditions:

```text
pass/fail: exact McNemar test
composite score: paired bootstrap confidence interval
```

Run:

```text
python scripts/compute_significance.py 05_evaluation/sample_smoke_results.csv --a atlas_rag --b atlas_lora_rag
```

## Small-n warning

With 25 questions, treat results as directional only. Do not overclaim small differences.

## Go / hold / stop

Go if the adapter improves at least one target behavior without damaging exactness or freshness.
Hold if it only learns formatting or repeats scaffold language.
Stop/redesign if Atlas RAG does not beat raw RAG or LoRA worsens grounding.

## Required report

Use:

```text
05_evaluation/SMOKE_TRAIN_RESULTS_REPORT_TEMPLATE.md
```

This is not v1.0 and not proof until a real run is completed and reported.
