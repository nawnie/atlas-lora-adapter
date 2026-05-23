# Project Milestones

Status: active roadmap control  
Current version: v0.2.9-dev21  
Project: Atlas Reader LoRA  
Purpose: keep the project moving in controlled steps without version inflation.

## Current status

The project is currently in the v0.2 planning track.

Current state:

```text
v0.2 — clear plan, no trained adapter yet
v0.2.1 — planning/versioning correction
v0.2.2 — explicit milestone roadmap
v0.2.9-dev21 — GitHub upload prep, forensic preservation, no trained adapter yet
```

The project has a clear path, but nothing should be treated as proven until training and evaluation results exist.

## Version philosophy

Use small versions for small movement.

Do not call the project v1.0 until the first trained adapter experiment has been completed and results have been posted.

A bad result still counts as a result if it is documented honestly.

## Milestone overview

| Version | Milestone name | Main goal | Exit condition |
|---|---|---|---|
| v0.2 | Planning lock | Define concept, architecture, contract, lane/card targets | Strategy is coherent and documented |
| v0.2.1 | Version correction | Correct maturity language and v1.0 gate | Versioning policy exists |
| v0.2.2 | Milestone roadmap | Define v0.3-v1.0 gates | Roadmap has clear exit criteria |
| v0.3 | Lane/card seed | Build first real lane/card validation set | Minimum seed cards and lane records validate |
| v0.4 | Dataset seed | Build first training dataset seed | Dataset validates and maps to cards/lanes |
| v0.5 | Baseline evaluation | Test base models with no RAG, raw RAG, Atlas RAG | Baseline results are recorded |
| v0.6 | First training attempt | Train first Atlas Reader Mini adapter or document failed attempt | Training run is complete or failure is documented |
| v0.7 | Adapter evaluation | Compare adapter + Atlas RAG against baselines | Results table and analysis exist |
| v0.8 | Iteration pass | Fix dataset/contract based on v0.7 results | Improved dataset or contract exists |
| v0.9 | Release candidate | Prepare public research report package | Reproducible notes and final result draft exist |
| v1.0 | First public result | Publish first trained-model outcome, good or bad | Results are shared publicly or repo-ready |

## v0.3 — Lane/card seed

### Goal

Create the first real validated lane/card seed set.

This is the first step where the project begins moving from planning into buildable data.

### Scope

Use a narrow starting set, not all 128 lanes.

Recommended seed lanes:

1. `36_retrieval_card_authoring`
2. `37_small_model_retrieval_optimization`
3. `41_comfyui_workflow_repair`
4. `42_comfyui_socket_contract_debugging`
5. `44_video_vram_optimization`
6. `45_last_frame_chaining_video_extension`

### Deliverables

- lane validation records for seed lanes;
- 12-card target structure for each seed lane;
- card IDs and card types assigned;
- sample validated cards;
- card schema validator pass;
- updated `ATLAS_128_LANE_TARGET.csv` status fields.

### Exit condition

v0.3 is complete when:

```text
6 seed lanes x 12 cards per lane = 72 planned/seeded cards
```

and at least:

```text
24 cards are fully written and validate against schema
```

### Do not advance if

- cards are only titles with no answer behavior;
- `do_not_confuse_with` guidance is missing;
- cards do not map to training example types;
- validation scripts are not passing.

## v0.4 — Dataset seed

### Goal

Convert the seed cards into structured training records.

### Deliverables

- `lora_training_lab/04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl` expanded;
- records cover lane routing, answer from context, conflict resolution, insufficient context, exactness guard, freshness check, and answer-format selection;
- validator script confirms schema compliance;
- dataset card documents source, purpose, limitations, and intended use.

### Minimum target

```text
100 validated training records
```

### Strong target

```text
250 validated training records
```

### Exit condition

v0.4 is complete when:

- training records validate;
- each seed lane has at least 10 training examples;
- at least 20 examples include distractor context;
- at least 20 examples test insufficient context or exactness guard behavior.

### Do not advance if

- records are raw Markdown dumps;
- outputs teach memorized facts instead of RAG-reading behavior;
- examples do not include metadata;
- records cannot be traced back to lanes/cards.

## v0.5 — Baseline evaluation

### Goal

Test whether Atlas-style RAG helps before training a LoRA.

This prevents training from masking weak retrieval design.

### Test conditions

Run the same questions through:

```text
small base model, no RAG
small base model + raw RAG
small base model + Atlas RAG
larger base model, no RAG
larger base model + raw RAG
larger base model + Atlas RAG
```

### Suggested model targets

Small model candidates:

```text
.8B to 4B instruct model
```

Larger comparison model:

```text
7B instruct model
```

Exact model names should be verified when testing begins.

### Deliverables

- baseline test questions;
- model/setup notes;
- raw outputs;
- scored results using rubric;
- summary of where Atlas RAG helped or failed.

### Exit condition

v0.5 is complete when:

- at least 25 golden questions are tested;
- raw outputs are saved;
- results are scored;
- the repo contains a baseline analysis.

### Do not advance if

- baseline outputs are not saved;
- results are only described from memory;
- scoring rubric is not used;
- Atlas RAG does not beat raw RAG on any meaningful metric and no fix plan exists.

## v0.6 — First training attempt

### Goal

Run the first Atlas Reader Mini training attempt.

This can be a success or a documented failure.

### Target adapter

```text
atlas-reader-mini_{base-model}_128L-12C-5D_v1
```

For a first practical test, use a compatible small local instruct model.

### Deliverables

- training command or notebook;
- model/base details;
- dataset version;
- Atlas contract version;
- training logs;
- failure notes if training fails;
- adapter artifact if training succeeds.

### Exit condition

v0.6 is complete when:

- a training run completes, or
- a failed run is documented well enough to reproduce or diagnose.

### Do not advance if

- training settings are not recorded;
- dataset version is unclear;
- base model is not documented;
- failure is hidden or hand-waved.

## v0.7 — Adapter evaluation

### Goal

Evaluate whether the trained adapter changes model behavior.

### Test matrix

Compare:

```text
base model, no RAG
base model + raw RAG
base model + Atlas RAG
base model + Atlas Reader LoRA + Atlas RAG
larger base model, no RAG
larger base model + Atlas RAG
```

### Metrics

Use the project rubric:

- grounding;
- exactness;
- actionability;
- retrieval discipline;
- beginner safety;
- AIWF alignment;
- lane routing accuracy;
- source-priority adherence;
- insufficient-context behavior.

### Deliverables

- scored results;
- raw outputs;
- analysis;
- failure patterns;
- decision: continue, redesign, or stop training.

### Exit condition

v0.7 is complete when the adapter has been evaluated against baselines and the project can honestly say what changed.

### Do not advance if

- only cherry-picked examples are shown;
- failed prompts are omitted;
- comparisons are not run against baseline outputs.

## v0.8 — Iteration pass

### Goal

Use v0.7 results to improve the system.

### Possible outcomes

If the adapter helped:

- expand dataset;
- improve lane/card coverage;
- test another small base model;
- prepare repeatable training pipeline.

If the adapter did not help:

- identify whether the issue was dataset quality, card design, retrieval quality, base model weakness, or training setup;
- revise contract or training data;
- rerun a small test.

If results were mixed:

- isolate tasks where it helped;
- remove or rewrite confusing training examples;
- split Mini and Extended contracts more clearly.

### Deliverables

- v0.8 improvement plan;
- revised dataset or contract;
- updated failure analysis;
- next-run checklist.

### Exit condition

v0.8 is complete when a clear change has been made based on evidence.

### Do not advance if

- the project ignores bad results;
- the next run repeats the same failed design without explanation;
- no decision log is updated.

## v0.9 — Release candidate

### Goal

Prepare a clean public research package.

### Deliverables

- final README pass;
- versioned dataset card;
- model/training notes;
- evaluation report draft;
- limitations and failure notes;
- reproducibility checklist;
- public claims review.

### Exit condition

v0.9 is complete when the project is ready to publish results without overstating them.

### Do not advance if

- claims exceed evidence;
- setup cannot be understood by someone else;
- failure cases are hidden;
- licensing/source limits are unclear.

## v1.0 — First public result

### Goal

Publish the first trained-model outcome.

The result can be good, bad, or mixed.

### Required contents

- base model;
- adapter name;
- Atlas contract;
- dataset version;
- training setup;
- evaluation setup;
- raw or summarized results;
- failure cases;
- what was learned;
- next-step recommendation.

### Valid v1.0 outcomes

All of these are valid:

```text
The adapter helped.
The adapter did not help.
The adapter helped only in narrow tasks.
The dataset was too weak.
The card contract needs redesign.
Small models still failed.
Atlas RAG helped but LoRA did not.
```

### Exit condition

v1.0 is complete when the first trained-model result is shared.

## Operating rule

Every milestone should answer:

```text
What changed?
What evidence exists?
What failed?
What is the next decision?
```

If those questions cannot be answered, the milestone is not complete.

## Owner approval rule for milestone jumps

A completed exit condition does not automatically promote the project to the next `.0` milestone.

Any jump from `x.x.9` to the next `.0` version requires explicit approval from Shawn O'Hagan.

AI assistants may prepare a recommendation packet, but cannot approve the release themselves.

Required owner action:

```text
Approved: promote to vX.Y.0
```

Without that approval, the highest allowed status is:

```text
ready_for_owner_review
```

## v0.2.5 status note

The seed lane/card count target for the v0.3 gate has now been started:

```text
6 seed lanes
72 seed cards
```

This does not automatically promote the project to v0.3. The next step is quality control and validation against schemas, then owner review for milestone promotion when ready.
