# Atlas Reader LoRA Pretraining Gate

Status: required gate before serious LoRA training

## Purpose

This document prevents the project from training too early on an underspecified RAG structure.

The Atlas Reader LoRA should learn structured-RAG reading behavior. To learn that behavior, it needs a sufficiently broad and validated lane network.

## Required before serious training

Training should not proceed beyond small smoke tests until these conditions are met:

| Requirement | Target |
|---|---:|
| Total target lanes listed | 128 |
| Validated lanes minimum for first serious run | 64 |
| Fully validated lanes before public performance claim | 128 |
| Minimum retrieval cards per lane | 8 |
| Minimum QA prompts per lane | 3 |
| Minimum training records per lane | 6 |
| Stronger target training records per lane | 10 |
| Minimum total records for first serious run | 768 |
| Stronger dataset target | 1,280+ |

## Allowed before gate completion

The following are allowed before the full gate is complete:

- schema design;
- training data examples;
- validator scripts;
- three-lane MVP smoke tests;
- prompt-only experiments;
- raw RAG vs Atlas RAG comparisons;
- documentation and research notes.

## Not allowed before gate completion

Do not make public claims that:

- Atlas Reader LoRA improves performance;
- 4B models match 7B models;
- the adapter generalizes across corpora;
- the adapter is ready for release.

## Why this matters

If the model is trained too early, it may learn surface habits instead of Atlas-reading behavior.

The 128-lane gate forces the project to build enough structured variety for the LoRA to learn the actual protocol:

```text
route -> rank -> verify -> answer -> qualify -> cite/source-map
```

## Research value

Even if LoRA training fails, the lane-validation dataset will still be useful.

It will produce:

- structured RAG evaluation data;
- raw RAG vs Atlas RAG comparison data;
- small-model routing failure data;
- source-priority adherence data;
- hallucination/exactness data;
- insufficient-context behavior data.

That failure data is still research-relevant.

## Card gate update

The first serious Atlas Reader LoRA training gate now uses:

```text
128 validated lanes
12 validated cards per lane
1,536 validated cards total
```

This replaces any larger early-card target. Larger 24-card or 32-card lane variants are reserved for later experiments after the compact small-model version proves useful.

Minimum card composition per lane:

- 4 concept cards
- 3 failure signature cards
- 2 diagnostic branch cards
- 1 source priority card
- 1 do-not-confuse card
- 1 answer pattern card

Small-model retrieval should usually use 1-5 cards per answer depending on model size.
