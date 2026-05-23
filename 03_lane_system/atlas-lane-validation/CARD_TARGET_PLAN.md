# Atlas Card Target Plan

Status: Phase 5 planning standard  
Date: 2026-05-22  
Project: Atlas Reader LoRA  
Target: small-model-first structured RAG

## Decision

The first serious Atlas Reader LoRA target is:

```text
128 validated lanes
x 12 validated cards per lane
= 1,536 validated cards
```

This is the baseline target for training and evaluating a small-model-friendly Atlas Reader LoRA.

## Why 12 cards per lane

The goal is to support smaller models first, especially the `.8B` to `4B` range.

Small models need:

- fewer distractions;
- tighter source boundaries;
- clearer routing signals;
- shorter context packs;
- stronger do-not-confuse rules;
- compact answer patterns;
- less redundant retrieval.

Twelve cards per lane is enough to teach the structure without creating an oversized card network that overwhelms small local models.

## Future expansion levels

| Stage | Cards per lane | Total cards across 128 lanes | Purpose |
|---|---:|---:|---|
| Small-model baseline | 12 | 1,536 | Primary target for `.8B` to `4B` models |
| Expanded proof model | 24 | 3,072 | Use after first proof if stronger models benefit |
| Deep expert model | 32 | 4,096 | Later research-grade Atlas Reader variant |

Do not jump to 24 or 32 cards per lane until the 12-card version proves useful.

## Why not 24 or 32 first

More cards are not automatically better.

For small models, more cards can cause:

- over-retrieval;
- attention dilution;
- source confusion;
- slow responses;
- weaker reasoning over too much context;
- increased chance of quoting the wrong card;
- more training noise.

The first target should prove whether a compact Atlas works.

If the compact version works, then a larger Atlas Reader LoRA can be trained later for bigger models.

## Standard 12-card lane kit

Each lane should target this card mix:

| Card type | Count | Purpose |
|---|---:|---|
| Concept cards | 4 | Teach the core ideas of the lane |
| Failure signature cards | 3 | Teach common real-world break patterns |
| Diagnostic branch cards | 2 | Teach routing between possible causes |
| Source priority card | 1 | Teach what evidence to trust first |
| Do-not-confuse card | 1 | Prevent bad neighboring-lane routing |
| Answer pattern card | 1 | Teach the response shape |

Total:

```text
4 + 3 + 2 + 1 + 1 + 1 = 12 cards per lane
```

## Card type definitions

### Concept card

Explains one stable concept in the lane.

Example:

```text
In ComfyUI socket debugging, IMAGE and LATENT are different data types. A model should not assume they are interchangeable.
```

### Failure signature card

Describes a concrete problem pattern.

Example:

```text
User says nodes will not connect, or the workflow reports an input type mismatch. This may indicate an IMAGE/LATENT/MASK/CONDITIONING boundary error.
```

### Diagnostic branch card

Helps choose between similar causes.

Example:

```text
If the error mentions ModuleNotFoundError, route to Python dependency/runtime lane. If the error mentions socket/input type mismatch, route to ComfyUI socket-contract debugging.
```

### Source priority card

Tells the model what source layer wins.

Example:

```text
For exact node class_type names, installed object_info or source-backed node definitions outrank memory or old archive notes.
```

### Do-not-confuse card

Prevents incorrect lane selection.

Example:

```text
Do not confuse missing model files with socket-contract failures. A missing checkpoint is a path/model issue; a failed connection is usually a datatype boundary issue.
```

### Answer pattern card

Teaches the model how to respond.

Example:

```text
Explain the mismatch, identify the boundary, recommend verification, avoid inventing exact node names, then give the next safe step.
```

## Small-model retrieval rule

For `.8B` to `4B` models, do not retrieve too many cards at once.

Recommended retrieval limits:

| Model size | Suggested cards retrieved per answer | Notes |
|---|---:|---|
| `.8B` to `1.5B` | 1-2 cards | Keep answers narrow and highly structured |
| `2B` to `3B` | 2-3 cards | Add one do-not-confuse or source-priority card when needed |
| `4B` | 3-5 cards | Can handle primary + secondary lane support |
| `7B+` | 5-8 cards | Use more context only when evaluation supports it |

The Atlas should retrieve the best few cards, not dump the whole lane.

## Card design for small models

Small-model cards should be:

- compact;
- explicit;
- low ambiguity;
- source-aware;
- task-shaped;
- full of routing cues;
- clear about what not to do.

Avoid long prose cards. A card should be a signpost, not a chapter.

## Training-data target

Minimum training target:

```text
1 card = 1 training record
1,536 cards = 1,536 records
```

Better target:

```text
1 card = 2 training records
1,536 cards = 3,072 records
```

Strong target:

```text
1 card = 3 training records
1,536 cards = 4,608 records
```

Recommended first serious dataset:

```text
3,000 to 5,000 structured training records
```

This supports small-model behavior training without turning the LoRA into a fact memorizer.

## Card validation requirements

A card is validated only if it has:

- lane ID;
- card ID;
- card type;
- title;
- user phrasing;
- canonical summary;
- source priority rule;
- must-retrieve targets;
- do-not-confuse guidance;
- answer pattern;
- exactness guard;
- freshness flag;
- risk level.

## Success criteria

The 12-card target works if it improves:

- correct lane routing;
- source-priority use;
- refusal to invent exact identifiers;
- insufficient-context behavior;
- compact answers from small models;
- raw RAG vs Atlas RAG score;
- Atlas RAG vs Atlas Reader LoRA score.

## Final decision

For Phase 5, lock the first serious card target at:

```text
128 lanes
12 cards per lane
1,536 validated cards
3,000-5,000 training records
small-model-first evaluation
```

If this proves useful, later versions can test 24 or 32 cards per lane for larger models.
