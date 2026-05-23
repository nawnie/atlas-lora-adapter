# Atlas LoRA Adapter Roadmap

Status: Phase 2 planning and scaffold  
Date: 2026-05-22

## North-star goal

Build and test the **Atlas Reader LoRA**: a LoRA/adapter trained to improve how a model reads structured, lane-based RAG context.

The adapter should improve:

- lane routing;
- source-priority discipline;
- evidence filtering;
- conflict handling;
- freshness warnings;
- exactness discipline;
- answer-format selection;
- insufficient-context behavior.

## Research goal

The project should produce useful evidence even if the first adapter fails.

The main research question is:

> Can a parameter-efficient adapter improve a model's ability to use structured RAG context, compared with raw RAG or no RAG?

Secondary questions:

1. Does Atlas-style lane routing reduce irrelevant context use?
2. Does source hierarchy reduce hallucinated or stale answers?
3. Does a 4B model with Atlas Reader LoRA + Atlas RAG approach or exceed a 7B base model on bounded source-grounded tasks?
4. Does the adapter generalize to another structured RAG corpus outside AIWF?
5. Which task types benefit most: routing, exactness, troubleshooting, formatting, or refusal?

## Phase 1 — Concept lock-in

Status: complete

Deliverables:

- standalone repo scaffold;
- README;
- initial strategy document;
- progress log.

## Phase 2 — Documentation and test scaffold

Status: current

Deliverables:

- roadmap;
- architecture overview;
- claims and limits;
- standard RAG vs Atlas-style RAG comparison;
- training data schema;
- sample JSONL records;
- evaluation plan;
- baseline matrix;
- golden-question seed set;
- experiment templates;
- validation script;
- results summarizer;
- research-value note.

Exit criteria:

- `scripts/validate_training_records.py` passes on `lora_training_lab/04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl`;
- evaluation files define the first baseline comparison;
- sample records cover at least 6 task types;
- claims stay bounded and testable.

## Phase 3 — Dataset seed build

Goal: create the first real training/evaluation dataset.

Tasks:

1. Select first 3 Atlas lanes:
   - ComfyUI socket contract debugging;
   - video VRAM optimization;
   - retrieval card authoring.
2. Build 100-200 high-quality training examples.
3. Include relevant context and distractor context.
4. Add expected behavior metadata.
5. Build 25-50 golden evaluation questions.
6. Validate schema and manually review examples.

Exit criteria:

- at least 100 valid training records;
- at least 25 golden questions;
- no examples that train stale facts as permanent truth;
- no examples that reward invented paths, commands, APIs, or node names.

## Phase 4 — First adapter experiment

Goal: train first small adapter.

Candidate base model family:

- Qwen instruct-class 4B or 7B;
- exact model choice must be verified at experiment time.

Experiment matrix:

- base model, no RAG;
- base model + raw RAG;
- base model + Atlas RAG;
- base model + Atlas Reader LoRA + Atlas RAG.

Exit criteria:

- adapter trains without obvious collapse;
- evaluation results are recorded;
- qualitative failures are documented.

## Phase 5 — 4B vs 7B comparison

Goal: test the bounded-performance claim.

Question:

> Can 4B + Atlas Reader LoRA + Atlas RAG match or exceed 7B base / 7B raw RAG on source-grounded troubleshooting tasks?

Exit criteria:

- at least 25 shared questions;
- rubric scores recorded;
- examples of wins and losses preserved;
- no public claim beyond measured results.

## Phase 6 — Cross-corpus generalization

Goal: test whether this is an AIWF memorization adapter or a reusable RAG-reading adapter.

Candidate second corpora:

- hotel operations Atlas;
- Python project docs Atlas;
- vehicle repair Atlas;
- fiction/worldbuilding Atlas.

Exit criteria:

- adapter shows at least some transfer in source hierarchy, insufficient-context handling, or answer formatting;
- failure cases are documented.

## Phase 7 — Public research report

Goal: publish a clear result, even if negative.

Deliverables:

- methodology;
- dataset description;
- baseline matrix;
- scoring rubric;
- quantitative results;
- qualitative examples;
- limitations;
- next steps.

## Definition of success

The project works if the adapter measurably improves any of the following:

- source-groundedness;
- exactness;
- refusal to invent unsupported details;
- correct lane/source use;
- beginner-safe troubleshooting;
- answer format consistency;
- smaller-model usefulness in bounded tasks.

## Definition of useful failure

The project still produces useful research if it shows:

- RAG structure helps without LoRA;
- LoRA overfits to one corpus;
- models ignore metadata;
- source hierarchy is difficult to learn;
- smaller models cannot reliably use structured context;
- evaluation reveals which behaviors require prompting, retrieval design, or base-model capacity instead of LoRA.

## Immediate next commands

From repo root:

```powershell
python scripts/validate_seed_cards.py
python scripts/validate_training_records.py lora_training_lab/04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python scripts/check_training_record_quality.py lora_training_lab/04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
python lora_training_lab/scripts/qc_labinstall_static.py
```


## Phase 3 — 128-Lane Atlas Validation Gate

Before serious Atlas Reader LoRA training, the project should validate a broad Atlas lane network.

Target:

```text
35 existing AIWF Atlas lanes
+ 93 new/expanded lanes
= 128 validated RAG lanes
```

This gate exists because the LoRA should learn how to read structured RAG, not memorize a tiny subset of AIWF topics.

Phase 3 deliverables:

- `atlas-lane-validation/ATLAS_128_LANE_TARGET.md`
- `atlas-lane-validation/ATLAS_128_LANE_TARGET.csv`
- `atlas-lane-validation/atlas_128_lane_target.json`
- `atlas-lane-validation/LANE_VALIDATION_SCHEMA.json`
- `atlas-lane-validation/LANE_VALIDATION_WORKFLOW.md`
- `atlas-lane-validation/PRETRAINING_GATE.md`

Minimum pretraining dataset target:

```text
128 lanes x 6 records per lane = 768 structured training records
```

Stronger target:

```text
128 lanes x 10 records per lane = 1,280+ structured training records
```

The first MVP can still use 3 lanes for smoke testing, but public performance claims should wait until the lane-validation gate is satisfied.

## Phase 5 — 12-Card Small-Model Baseline

Decision:

```text
128 lanes x 12 cards per lane = 1,536 validated cards
```

This is the first serious card target for Atlas Reader LoRA.

The goal is to support `.8B` to `4B` models by using compact, high-signal card sets. Larger card targets such as 24 or 32 cards per lane should wait until the 12-card version produces useful evidence.

Phase 5 deliverables:

- `atlas-lane-validation/CARD_TARGET_PLAN.md`
- `strategy/SMALL_MODEL_ATLAS_READER_MODE.md`
- `training/ATLAS_CARD_SCHEMA_V1.json`
- `training/ATLAS_CARD_TEMPLATE.json`

Training implication:

```text
1,536 cards -> 3,000 to 5,000 structured training records
```

Evaluation implication:

Small-model tests should retrieve only a few cards at a time and measure whether the model routes correctly, ignores distractors, respects source priority, and avoids unsupported exact claims.

## Phase 6 — Atlas Contract Naming

Decision:

```text
atlas-reader-{tier}_{base-model}_{lane-count}L-{cards-per-lane}C-{retrieval-depth}D_v{version}
```

Purpose:

Make the adapter name describe the Atlas/RAG structure it was trained to navigate.

Baseline adapter name:

```text
atlas-reader-mini_qwen3-4b_128L-12C-5D_v1
```

This keeps the small-model LoRA tied to a clear contract:

- 128 lanes;
- 12 cards per lane;
- retrieval depth around 5 cards;
- compact card schema;
- `.8B` to `4B` target range.

Deliverables:

- `strategy/ATLAS_CONTRACT_NAMING.md`
- `strategy/ATLAS_CONTRACT_SCHEMA_V1.json`
- `strategy/atlas-contract_mini_128L-12C-5D_v1.json`

## Version correction: v0.2 planning track

This project is still early planning and research design.

The current state is best labeled:

```text
v0.2 — clear path, no trained adapter yet
```

Small documentation, schema, naming, and roadmap changes should use patch versions such as:

```text
v0.2.1
v0.2.2
```

Do not call the project v1.0 until the first trained adapter experiment is complete and results are posted.

The v1.0 result can be positive, negative, or mixed. The key requirement is that the outcome is shared honestly.

## Milestone roadmap v0.3 through v1.0

The detailed milestone plan now lives in:

```text
MILESTONES.md
```

Short version:

| Version | Focus | Exit condition |
|---|---|---|
| v0.3 | Lane/card seed | 6 seed lanes planned; 24+ cards fully written and validated |
| v0.4 | Dataset seed | 100+ validated training records |
| v0.5 | Baseline evaluation | 25+ golden questions tested across no RAG, raw RAG, and Atlas RAG |
| v0.6 | First training attempt | First adapter training run completed or failed with documentation |
| v0.7 | Adapter evaluation | Adapter compared against baseline outputs |
| v0.8 | Iteration pass | Dataset/contract improved based on evidence |
| v0.9 | Release candidate | Public result package prepared |
| v1.0 | First public result | Trained-model outcome posted, good or bad |

Do not advance versions based on planning alone. Advance only when the exit condition is met.
