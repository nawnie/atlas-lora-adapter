# AGENTS.md

## Project

AI Without Fear — Atlas Reader LoRA Lab

## Current status

This repo is pre-install, pre-training, and pre-evaluation.

Do not claim that the installer works, the adapter works, or the method improves results unless a real run log exists.

Read first:

```text
PROJECT_PREINSTALL_STATUS.md
PROJECT_STATUS.md
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
01_strategy/AGENT_PROTOCOL_LANE.md
07_quality_control/REPORT_TEMPLATE_POLICY.md
```

## Working agreements

- Preserve the no-wins guardrail.
- Treat report templates as templates, not results.
- Do not cite AI assistants as sources.
- Cite primary papers, official docs, official repos/model cards, or measured local outputs.
- Keep AIWF voice practical, source-aware, and no-hype.
- Prefer PowerShell/Windows-friendly commands when adding setup instructions.
- Do not promote the project to `v0.3.0` without explicit owner approval.

## Atlas behavior protocol

When working on Atlas-related tasks:

1. Identify the primary lane or doc area.
2. Use the smallest relevant context.
3. Check source/citation policy before adding claims.
4. Flag freshness-sensitive claims.
5. Do not invent exact commands, versions, paths, licenses, node names, or benchmark results.
6. If evidence is missing, write `not verified yet`.
7. If a result is only a future report template, label it as a template.

## Code expectations

Before packaging changes:

```powershell
python scripts\validate_seed_cards.py
python scripts\validate_training_records.py lora_training_lab\04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python scripts\check_training_record_quality.py lora_training_lab\04_training_data\SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python lora_training_lab\scripts\qc_labinstall_static.py
```

Only run commands that are appropriate for the local environment and explain failures plainly.

## Agent protocol lane

This repo uses `AGENTS.md` as one testable implementation of the Atlas idea.

The agent protocol is not a LoRA result.

If agent-guided work beats chat attachment use, that may indicate the Atlas instructions are useful. If a LoRA fails, investigate the training variables before rejecting the concept.
