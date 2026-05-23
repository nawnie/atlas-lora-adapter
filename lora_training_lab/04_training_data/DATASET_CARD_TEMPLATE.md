# Dataset Card Template

## Dataset name

Atlas Reader LoRA Training Set vX

## Purpose

Teach models to read structured RAG context with source hierarchy, lane routing, evidence filtering, and answer discipline.

## Source corpora

List corpora used:

- AIWF Atlas
- synthetic non-AIWF Atlas examples
- other approved corpora

## Task types

List counts by task type:

| Task type | Count |
|---|---:|
| lane_routing | 0 |
| answer_from_context | 0 |
| conflict_resolution | 0 |
| insufficient_context | 0 |
| exactness_guard | 0 |
| freshness_check | 0 |
| answer_format_selection | 0 |
| multi_rag_generalization | 0 |

## Known limitations

- Does not teach current facts.
- May overfit to lane names if multi-corpus examples are weak.
- Does not replace current verification.
- Does not guarantee compatibility across model families.

## Evaluation plan

Reference `evaluation/EVALUATION_PLAN.md`.
