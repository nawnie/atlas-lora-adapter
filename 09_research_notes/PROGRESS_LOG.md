# Atlas LoRA Adapter - Progress Log

This file tracks major decisions, experiments, and progress for the standalone `nawnie/atlas-lora-adapter` project.

## 2026-05-22 - Phase 1 repo creation and direction lock-in

- Decided to spin the Atlas Reader LoRA into its own dedicated repository: `nawnie/atlas-lora-adapter`.
- Primary source corpus for early testing: `nawnie/ai-without-fear`.
- Created initial README and strategy document.
- Confirmed the core separation:
  - Knowledge lives in RAG / Atlas.
  - Reading behavior lives in the LoRA.

## 2026-05-22 - Phase 2 testing and documentation scaffold

- Added roadmap.
- Added training schema and starter JSONL records.
- Added evaluation plan, rubric, baseline matrix, and golden-question seed.
- Added experiment templates.
- Added validation and result-summary scripts.
- Added research-value note to preserve useful negative findings.

## Next priorities

1. Expand `training/SAMPLE_RECORDS.jsonl` into a 100-200 record seed dataset.
2. Select first 3 Atlas lanes for real example generation.
3. Run validator after every dataset update.
4. Choose first base model candidate.
5. Run no-RAG / raw-RAG / Atlas-RAG baselines before training.
