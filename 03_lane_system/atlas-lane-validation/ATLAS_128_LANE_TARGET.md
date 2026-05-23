# Atlas 128-Lane Validation Plan

Status: Phase 3 planning requirement  
Date: 2026-05-22  
Project: Atlas Reader LoRA  
Purpose: require a broad, validated lane set before LoRA training begins.

## Summary

The Atlas Reader LoRA should not be trained against a tiny or weak RAG structure. If the adapter is supposed to learn how to read Atlas-style RAG, then the training corpus needs enough validated lanes to show the model the full reading protocol.

The target is:

```text
35 existing AIWF Atlas lanes
+ 93 new/expanded lanes
= 128 validated RAG lanes before serious LoRA training
```

This does not mean every lane must be perfect before any experiment. It means the first meaningful training run should be gated behind a validated, varied lane target so the LoRA learns general Atlas-reading behavior instead of overfitting to three favorite AIWF topics.

## Why 128 lanes

128 is large enough to create varied routing pressure without becoming unbounded.

It creates enough examples for the model to learn:

- source hierarchy;
- lane routing;
- do-not-confuse boundaries;
- failure signature recognition;
- answer-format selection;
- volatile-claim handling;
- exactness discipline;
- insufficient-context behavior;
- cross-domain structured-RAG reading.

The target is not magic. It is a practical engineering checkpoint: enough lanes to test whether the adapter learns a reusable reading protocol.

## How this supports LoRA efficiency

A RAG-reader LoRA becomes efficient when it learns the structure instead of memorizing facts.

A broad validated lane set gives training examples like:

```text
same reading protocol
+ different lane
+ different source type
+ different task format
+ different failure signature
= reusable Atlas-reading behavior
```

Without enough lanes, the model may learn shallow patterns like "AIWF means ComfyUI" or "always answer in one troubleshooting style."

With 128 validated lanes, the LoRA has a better chance of learning:

```text
read the metadata
route the question
rank the source
check freshness
avoid unsupported exact claims
format the answer for the task
```

## Pre-training gate

Do not begin the first serious Atlas Reader LoRA training pass until the repository has:

1. a 128-lane target list;
2. validation records for each lane;
3. at least 8 retrieval cards per lane;
4. at least 3 QA/golden questions per lane;
5. `ANSWER_PATTERNS.md` guidance per lane;
6. `DO_NOT_CONFUSE_WITH.md` guidance per lane;
7. a minimum seed of training records across all core task types;
8. baseline evaluation questions for raw RAG vs Atlas RAG.

## Lane validation minimum

Each lane should have:

```text
CANONICAL_OVERVIEW.md
CONCEPT_MAP.md
RETRIEVAL_CARDS.jsonl
SOURCE_COVERAGE.md
FAILURE_SIGNATURES.md
QA_TEST_PROMPTS.md
ANSWER_PATTERNS.md
DO_NOT_CONFUSE_WITH.md
GAP_AUDIT_AND_VOL2_QUEUE.md
lane_profile.json
```

A lane is not considered training-ready if it only has a title and a description.

## Minimum examples per lane

For the first 128-lane dataset, the minimum target is:

| Example type | Minimum per lane |
|---|---:|
| lane routing | 1 |
| answer from context | 1 |
| insufficient context | 1 |
| exactness guard | 1 |
| freshness/confidence check | 1 |
| conflict or distractor handling | 1 |

That is 6 records per lane minimum.

```text
128 lanes x 6 records = 768 minimum structured training examples
```

A stronger target is 10 records per lane:

```text
128 lanes x 10 records = 1,280 structured training examples
```

The first MVP can still test on three lanes, but any performance claim about Atlas Reader LoRA should wait for broader lane coverage.

## Files in this folder

```text
atlas-lane-validation/
  ATLAS_128_LANE_TARGET.md
  ATLAS_128_LANE_TARGET.csv
  atlas_128_lane_target.json
  LANE_VALIDATION_SCHEMA.json
  LANE_VALIDATION_WORKFLOW.md
  PRETRAINING_GATE.md
```

## Final rule

The Atlas Reader LoRA is only as strong as the RAG structure it learns to read.

Build the map before training the map-reader.
