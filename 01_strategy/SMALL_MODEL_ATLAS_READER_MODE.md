# Small-Model Atlas Reader Mode

Status: Phase 5 design note  
Date: 2026-05-22  
Target model range: `.8B` to `4B`

## Purpose

Atlas Reader LoRA is being designed small-model-first.

The first proof target is not a giant model with a massive context window. The first target is to make small local models better at reading structured RAG.

The project should assume the model may have limited reasoning depth, limited context discipline, and weaker ability to ignore distractor chunks.

## Design rule

For `.8B` to `4B` models:

```text
Less context, better structure.
```

A small model should not be asked to read an entire lane. It should be handed a tight set of cards that already contain the routing, source, and answer instructions.

## Recommended context pack

A small-model context pack should usually contain:

1. one primary lane card;
2. one failure or diagnostic card;
3. one do-not-confuse or source-priority card;
4. optional answer-pattern card.

For `.8B` models, use 1-2 cards.

For `4B` models, use 3-5 cards.

## Why this matters

Large models can sometimes recover from messy retrieval.

Small models usually cannot.

If retrieval gives a small model too many cards, it may:

- blend unrelated topics;
- ignore source priority;
- answer from the wrong card;
- miss the exact failure signature;
- hallucinate missing commands or paths;
- give generic advice.

The Atlas should compensate by making the retrieval context extremely legible.

## Card style for small models

Cards should use short, direct fields.

Prefer:

```text
Use when:
Do not confuse with:
Trust first:
Exact identifiers:
Answer pattern:
Verification needed:
```

Avoid:

- long essay-style cards;
- overlapping cards with nearly identical summaries;
- vague card titles;
- hidden assumptions;
- unsupported commands;
- broad cards that cover too many failure types.

## Training implications

The LoRA should learn to use compact cards, not long documents.

Training examples should include:

- short retrieved context;
- one relevant card;
- one distractor card;
- expected source choice;
- expected refusal or qualification when exact evidence is missing.

## Evaluation implications

Small-model tests should measure:

- whether the model picks the right card;
- whether it ignores the distractor card;
- whether it avoids unsupported exact identifiers;
- whether it answers in the correct format;
- whether it knows when the context is not enough.

## Goal

The small-model goal is not to make a `.8B` model act like a frontier model.

The goal is to test whether structured cards and Atlas Reader LoRA can make small models more useful, safer, and more source-disciplined on bounded tasks.
