# Training Record Quality Gates

Status: active QC guidance  
Version added: v0.2.9-dev4  
Scope: Atlas Reader Mini training data

## Purpose

The training-record schema can confirm structure.

It cannot confirm that a record is worth training on.

This file defines the quality gates a record should pass before it is included in a real SFT/LoRA dataset.

## Gate 1 — Schema validity

A record must parse as JSONL and include:

- record ID;
- dataset version;
- record type;
- Atlas contract ID;
- user query;
- context pack;
- expected route;
- expected answer;
- quality flags.

## Gate 2 — Context-pack discipline

A valid Mini context pack must follow:

```text
1-5 cards maximum
primary lane first
secondary lane only when justified
no whole-lane dumps
no endless lane hopping
```

## Gate 3 — The expected answer must be real

Do not train final SFT on answers that only say:

```text
Route this to the lane.
Use the selected cards.
Follow the rules.
```

Those are scaffold/meta examples.

They are useful for schema testing, but not enough for final behavior training.

A production training answer should actually answer the user while showing the behavior.

## Gate 4 — Distractors must be meaningful

A distractor should be plausible enough to tempt the model.

Weak distractors teach very little.

A good distractor:

- shares surface words with the query;
- belongs to a neighboring lane;
- would cause a recognizable wrong answer;
- is clearly marked as ignored in `expected_route.ignored_card_ids`.

## Gate 5 — Exactness guard must be tested

Records should include cases where the user asks for:

- exact command;
- exact file path;
- exact node name;
- exact version;
- exact license/commercial-use claim;
- exact model recommendation.

If the context does not contain the evidence, the expected answer must qualify or refuse the exact claim.

## Gate 6 — Freshness must be explicit

Volatile claims need a freshness path.

Volatile examples include:

- current model recommendations;
- current package versions;
- API behavior;
- pricing;
- licensing;
- security guidance;
- current tool compatibility.

The expected answer should say what source type is needed.

## Gate 7 — No hidden overclaims

A record must not teach the model to claim:

- Atlas RAG works before evaluation;
- the LoRA improves performance before evaluation;
- small models equal larger models globally;
- diagrams prove implementation;
- old notes override current docs.

## Gate 8 — Human review before training

Before any real smoke training run, a human should review at least:

```text
50 random records
all freshness_check records
all exactness_guard records
all secondary_lane_reference records
all high-risk records
```

## Current sample-record status

The current sample records are scaffold/testing records.

They validate the schema and demonstrate the intended shape.

They are not yet a final training dataset.
