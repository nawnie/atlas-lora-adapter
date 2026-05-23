# AI Without Fear — Atlas Reader LoRA Lab

<p align="center">
  <img src="08_visuals/AIWF_LOGO.png" alt="AI Without Fear logo" width="220">
</p>

## Current status: pre-install

This package has not been installed on the target PC yet.

No training run has completed.

No adapter exists yet.

No performance wins are claimed.

Report templates are included because future runs need clean places to record evidence.

Current version: **v0.2.9-dev21**  
Status: **GitHub upload prep / seed-build / public-review package**  
Training status: **no adapter trained yet**

Atlas Reader LoRA is a structured-RAG research project testing whether a small LoRA adapter can learn a **portable reading protocol** for a named Atlas contract.

The short version:

```text
A normal RAG gives the model a pile of notes.
An Atlas gives it a map.
The Atlas Reader LoRA teaches the model how to read the map.
```

## Visual overview

<p align="center">
  <img src="08_visuals/ATLAS_SYSTEM_OVERVIEW_DIAGRAM.png" alt="What the Atlas Reader LoRA adapter is" width="900">
</p>

<p align="center"><strong>What the LoRA adapter is:</strong> the Atlas keeps the knowledge; the adapter is tested as a portable reading behavior for that structure.</p>

<p align="center">
  <img src="08_visuals/ATLAS_ROUTING_SYSTEM_FLOWCHART_OVERVIEW.png" alt="How Atlas cards and the five-card context pack work" width="900">
</p>

<p align="center"><strong>How the cards work:</strong> selected cards form a compact context pack so small models get a map instead of an unfocused pile of notes.</p>

<p align="center">
  <img src="08_visuals/ATLAS_ROUTING_FLOWCHART_OVERVIEW.png" alt="How Atlas lanes route a query to cards and sources" width="900">
</p>

<p align="center"><strong>How lanes route the query:</strong> lanes act as broad routes; cards inside the lane point the model toward the relevant evidence.</p>


## Research rationale

This project is worth exploring because the outcome is unknown but testable.

```text
Unknown does not mean impossible.
Unknown means instrument it.
```

The current goal is not to claim a win.

The current goal is to build the test bench, run it locally, save the logs, and let the evidence decide.

See:

```text
01_strategy/RESEARCH_RATIONALE_UNKNOWN_MEANS_INSTRUMENT_IT.md
05_evaluation/EVALUATION_RATIONALE_USEFUL_FAILURE.md
```

## AI Without Fear identity

This project is part of the **AI Without Fear** ecosystem.

AIWF framing:

```text
Master principles, not platforms.
Train the behavior. Keep the knowledge in the Atlas.
No proof without a run log.
```

Brand/system files:

```text
01_strategy/AIWF_BRAND_SYSTEM.md
00_landing_page/AIWF_ATLAS_READER_LANDING_DRAFT.md
08_visuals/AIWF_VISUAL_BRANDING_NOTES.md
```

## What this project is

This project is a research/design repository for:

- structured Atlas lanes;
- compact retrieval cards;
- 5-card context-pack routing;
- source-priority and exactness-guard behavior;
- small-model-first training experiments;
- evaluation before performance claims.

## What this project is not

This project is **not** claiming:

- a new LoRA algorithm;
- a new foundation model;
- proof that the adapter works before training/evaluation;
- proof that small models equal larger models globally;
- that diagrams or metaphors are research evidence.

## Current seed status

```text
18 seed lanes
216 seed cards
21 sample/scaffold training records
3 diagrams
```

The sample training records are **schema/scaffold examples**, not final SFT-quality records.


## Brand / positioning quick read

For public-facing language, use:

```text
Atlas Reader LoRA tests a portable reading protocol for a versioned structured-RAG contract.
```

Avoid claiming a new LoRA algorithm or proven performance before training.

See:

```text
01_strategy/BRAND_AND_POSITIONING_GUIDE.md
00_landing_page/PUBLIC_SUMMARY_DRAFT.md
10_source_materials/CITATION_STYLE_GUIDE.md
```

## Quick start for reviewers

Read these first:

```text
REPO_NAVIGATION.md
DIRECTORY_MAP.md
01_strategy/RELATED_WORK.md
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
lora_training_lab/04_training_data/OVERNIGHT_TRAINING_RUN_MATRIX.md
lora_training_lab/05_evaluation/SMOKE_TRAIN_PROTOCOL.md
07_quality_control/PUBLIC_REVIEW_CHECKLIST.md
```

## Repository map

The landing page stays short on purpose. The build notes, audits, and handoff records live in the repo where reviewers can inspect them without crowding the front page.

Start here:

```text
REPO_NAVIGATION.md
PROJECT_STATUS.md
CHANGELOG.md
07_quality_control/PUBLIC_REVIEW_CHECKLIST.md
```

## Main idea

The Atlas contract defines the shape of the structured RAG system:

```text
128L = 128 lanes
12C = 12 cards per lane
5D = up to 5 cards in the context pack
```

The adapter should learn behavior:

```text
read query
select primary lane
use selected cards
ignore distractors
respect source priority
qualify stale/missing evidence
answer compactly
```

The Atlas keeps the knowledge.

The LoRA should learn how to use the Atlas.

## Diagrams

The three project diagrams are displayed near the top of this README and stored in:

```text
08_visuals/
```

Included diagrams:

```text
ATLAS_SYSTEM_OVERVIEW_DIAGRAM.png — what the LoRA adapter is
ATLAS_ROUTING_SYSTEM_FLOWCHART_OVERVIEW.png — how the cards work
ATLAS_ROUTING_FLOWCHART_OVERVIEW.png — how lanes route the query
```

See:

```text
08_visuals/DIAGRAM_INDEX.md
```

## Training plan

Training work is planned but not executed.

Important files:

```text
lora_training_lab/04_training_data/TRAINING_PLAN_ATLAS_READER_MINI.md
lora_training_lab/04_training_data/TRAINING_RECORD_QUALITY_GATES.md
lora_training_lab/04_training_data/OVERNIGHT_TRAINING_RUN_MATRIX.md
lora_training_lab/04_training_data/ATLAS_SFT_FORMATTING_GUIDE.md
lora_training_lab/06_experiments/training_configs/
```

## Evaluation plan

The next proof step is a smoke train and 4-arm evaluation:

```text
A: base model, no RAG
B: base model + raw RAG
C: base model + Atlas RAG
D: base model + Atlas Reader LoRA + Atlas RAG
```

The key comparison is:

```text
C vs D
```

because that tests whether the LoRA adds value beyond Atlas RAG alone.

Evaluation files:

```text
lora_training_lab/05_evaluation/SMOKE_TRAIN_PROTOCOL.md
05_evaluation/GOLDEN_QUESTIONS_SMOKE_25.jsonl
scripts/compute_significance.py
```

## Source policy

AI assistants, chatbots, and drafting tools are not research sources.

Valid sources are:

- primary papers;
- official docs;
- official repositories/model cards;
- measured local outputs;
- project-authored notes clearly marked as drafts or internal reasoning.

See:

```text
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
```

## Release governance

This repo is still below the `v0.3.0` milestone.

Promotion to `v0.3.0` requires explicit owner approval.

Valid approval language should be explicit, such as:

```text
Approved: promote to v0.3.0
```

No AI assistant or automation may promote this project across a `.0` milestone gate without that approval.

## Current best next step

The next real work should be:

```text
turn scaffold training records into answer-quality records
run the 3-lane smoke protocol
score the 4-arm comparison
publish the outcome honestly
```

## Project records

Detailed build history and quality-control notes are intentionally kept outside the landing page:

```text
CHANGELOG.md
09_research_notes/
07_quality_control/
GITHUB_UPLOAD_NOTES.md
RAG_HANDOFF_GUIDE.md
```

The short version: this is a pre-training research lab, not a finished adapter. The next useful result is a measured run log, even if the result is "this version failed."
