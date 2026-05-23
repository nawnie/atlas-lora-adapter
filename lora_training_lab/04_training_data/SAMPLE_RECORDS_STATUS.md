# Sample Training Records Status

Status: scaffold examples only  
Version added: v0.2.9-dev4

## Summary

`SAMPLE_ATLAS_READER_MINI_RECORDS.jsonl` is a schema and concept demonstration file.

It is useful for:

- validating record shape;
- testing the validator;
- showing how context packs attach to records;
- proving the repo can generate seed records.

It is not yet a final supervised fine-tuning dataset.

## Why not final

Many current sample answers are meta/scaffold answers such as:

```text
Route this to the lane.
Use the selected cards.
Follow the source-priority and exactness guards.
```

That is good for testing structure.

It is not enough for final LoRA training because the model needs examples that actually answer the user.

## Required next step

Before training, convert scaffold records into answer-quality records.

A training-grade record should contain:

```text
user question
selected cards
expected route
actual useful answer
limits/uncertainty
ignored distractor behavior when applicable
```

## Do not train final adapters on this file alone

This file may be used for pipeline testing.

It should not be used as the only source for a real adapter training run.
