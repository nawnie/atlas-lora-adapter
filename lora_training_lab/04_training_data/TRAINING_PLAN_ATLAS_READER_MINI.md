# Atlas Reader Mini Training Plan

Status: planning / seed-build  
Version added: v0.2.9-dev3  
Adapter target: `atlas-reader-mini_{base-model}_128L-12C-5D_v1`

## Current status

This project does not have a trained adapter yet.

Current seed base:

```text
18 seed lanes
216 seed cards
```

This file defines how the first Atlas Reader LoRA should be trained once the dataset is ready.

## Core principle

The LoRA should not memorize the Atlas.

The Atlas/RAG keeps the knowledge.

The LoRA learns the navigation behavior:

```text
read the query
identify the primary lane
use the selected cards
respect source priority
ignore distractors
cross to a secondary lane only when allowed
answer from evidence
qualify missing or volatile claims
```

## Training objective

Train the adapter to follow the Atlas Contract:

```text
128L = 128 lanes
12C = 12 cards per lane
5D = max 5-card context pack
```

The first adapter should be small-model-first:

```text
target range: .8B to 4B
style: compact, bounded, source-disciplined
goal: better structured-RAG navigation, not general intelligence
```

## What a training record teaches

A record should include:

1. Atlas contract metadata.
2. User query.
3. Retrieved context pack.
4. Expected primary lane.
5. Optional secondary lane.
6. Expected used cards.
7. Expected answer.
8. Limits or uncertainty note.
9. Refusal/qualification behavior when evidence is missing.

## Required training example types

| Type | Purpose |
|---|---|
| `route_primary_lane` | Teach primary lane selection |
| `select_cards` | Teach choosing the right cards in the lane |
| `ignore_distractor` | Teach not to follow plausible wrong cards |
| `secondary_lane_reference` | Teach controlled cross-lane routing |
| `exactness_guard` | Teach not to invent commands, paths, versions, node names, or claims |
| `insufficient_context` | Teach saying evidence is missing |
| `freshness_check` | Teach volatile-claim verification behavior |
| `answer_pattern` | Teach response shape and compactness |

## Dataset stages

### Stage 0 — Manual sanity examples

Target:

```text
25-50 carefully written examples
```

Purpose:

- confirm the schema is right;
- confirm the answer format is learnable;
- identify missing fields before generating more examples.

### Stage 1 — Smoke-test dataset

Target:

```text
300-600 examples
```

Purpose:

- prove the training pipeline runs;
- test whether the model learns the response structure;
- test whether the model follows primary-lane routing better than base.

This is not enough for a public performance claim.

### Stage 2 — First serious dataset

Target:

```text
3,000-5,000 examples
```

Based on:

```text
128 lanes
1,536 cards
2-3 examples per card average
```

Purpose:

- test whether Atlas Reader LoRA improves structured-RAG behavior;
- compare against base model + Atlas RAG;
- compare small model with larger model baseline.

### Stage 3 — Public result package

Required before v1.0:

- dataset version;
- adapter name;
- base model;
- training config;
- evaluation matrix;
- raw outputs;
- scored results;
- failure analysis;
- conclusion, good or bad.

## Training data format

Use JSONL.

Each line should be a complete supervised training record.

The repo now includes:

```text
04_training_data/TRAINING_RECORD_SCHEMA_V1.json
04_training_data/CONTEXT_PACK_SCHEMA_V1.json
04_training_data/SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl
scripts/build_seed_training_records.py
```

## Context-pack rule

For Mini v1:

```text
max cards per record: 5
primary lane first
secondary lane only when useful and explicitly represented
```

Recommended pack shape:

```text
1 main pattern card
1 failure signature card
1 diagnostic branch card
1 source priority or exactness card
0-1 secondary lane card
```

## Answer target

Answers should be:

- compact;
- grounded in the cards;
- clear about the route;
- clear about uncertainty;
- practical;
- not overly verbose;
- not pretending unsupported facts are known.

## What not to train

Do not train the LoRA to:

- memorize all Atlas facts;
- hallucinate exact node names or commands;
- ignore source priority;
- always cross lanes;
- answer from weak distractor cards;
- treat diagrams or metaphors as proof;
- claim performance before evaluation.

## First smoke-test recommendation

Use the current seed lanes to build a smoke dataset.

Current viable first target:

```text
18 seed lanes
216 seed cards
300-600 smoke-test training records
```

Suggested record mix:

| Type | Approx count |
|---|---:|
| route_primary_lane | 80 |
| select_cards | 80 |
| ignore_distractor | 80 |
| secondary_lane_reference | 40 |
| exactness_guard | 60 |
| insufficient_context | 40 |
| freshness_check | 40 |
| answer_pattern | 80 |

## Evaluation before training

Before training any LoRA, run baseline tests:

```text
base model, no RAG
base model + raw RAG
base model + Atlas RAG
```

This matters because if Atlas RAG does not beat raw RAG, the lane/card system needs work before adapter training.

## Evaluation after training

After training:

```text
base model + Atlas RAG
base model + Atlas Reader LoRA + Atlas RAG
larger model + Atlas RAG
```

The key question:

```text
Does the adapter improve how the model uses the Atlas, beyond what Atlas RAG already provides?
```

## Failure is allowed

A failed adapter is still useful if documented.

Valid outcomes:

```text
LoRA helps.
LoRA does not help.
LoRA helps only on narrow routing tasks.
Atlas RAG helps but LoRA does not.
Small models still fail despite structure.
The dataset teaches format but not reasoning.
The contract needs redesign.
```

The result should be published honestly when the project reaches v1.0.
