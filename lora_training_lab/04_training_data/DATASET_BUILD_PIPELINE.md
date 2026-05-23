# Dataset Build Pipeline

Status: planning / seed-build  
Version added: v0.2.9-dev3

## Goal

Convert Atlas lanes and cards into supervised fine-tuning records for Atlas Reader Mini.

## Pipeline

```text
lanes/cards
  ↓
context-pack builder
  ↓
training-record builder
  ↓
schema validation
  ↓
manual QC
  ↓
smoke dataset
  ↓
training run
  ↓
evaluation
```

## Step 1 — Build context packs

For each lane, create context packs using:

- main card;
- failure card;
- diagnostic branch card;
- source priority or exactness card;
- optional secondary-lane card.

## Step 2 — Write user queries

Each pack should have several query forms:

- beginner phrasing;
- technical phrasing;
- vague phrasing;
- error-message phrasing;
- misrouted/distractor phrasing.

## Step 3 — Generate expected answer

The expected answer should:

- route to the primary lane;
- use relevant cards;
- avoid distractor cards;
- answer compactly;
- name uncertainty;
- avoid unsupported exact identifiers.

## Step 4 — Add negative cases

Every dataset needs negative examples:

- insufficient context;
- stale claim;
- missing source;
- wrong secondary lane;
- tempting but incorrect exact command;
- broad source placeholder.

## Step 5 — Validate schema

Run:

```text
python scripts/validate_training_records.py
```

## Step 6 — Manual QC

Human review should check:

- no invented exact commands;
- no unsupported current-version claims;
- no hidden promotion to v0.3/v1.0;
- no generic AI hype;
- no answer that ignores selected cards.

## Step 7 — Smoke train

Use a 300-600 record dataset only to test the training pipeline.

Do not use smoke-training results as public proof.

## Step 8 — Baseline comparison

Before claiming value, compare:

```text
base model + Atlas RAG
base model + Atlas Reader LoRA + Atlas RAG
```

The LoRA only proves value if it improves over Atlas RAG alone.
