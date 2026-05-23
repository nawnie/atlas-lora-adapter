# 5-Card Context Pack Design

Status: planning / seed-build  
Version added: v0.2.9-dev3

## Purpose

The 5-card context pack is the working memory unit for Atlas Reader Mini.

It is not five reasoning steps.

It is the maximum number of selected cards the small model is expected to read for one answer.

## Core rule

```text
Primary lane first.
Secondary lane only when selected context explicitly supports it.
No endless hopping.
```

## Standard pack shape

```text
Card 1: main pattern
Card 2: failure signature
Card 3: diagnostic branch
Card 4: source priority / exactness guard
Card 5: optional secondary-lane reference
```

## Why this helps small models

Small models can get lost when too much context is retrieved.

A compact pack gives the model:

- one primary route;
- the main problem pattern;
- a failure signature;
- a branch rule;
- a source/claim rule;
- optionally one cross-lane clue.

## Good pack

A good context pack is:

- small;
- relevant;
- labeled;
- mostly from the primary lane;
- clear about secondary cards;
- clear about what not to claim.

## Bad pack

A bad context pack:

- dumps a whole lane;
- includes many unrelated cards;
- gives multiple competing source rules;
- includes secondary lane cards without explanation;
- lacks an exactness guard;
- lacks an answer pattern.

## Secondary lane rule

A secondary lane card is allowed when:

1. the primary lane card identifies a boundary or workaround;
2. the user query includes a cross-lane clue;
3. the secondary card improves the answer without taking over the route.

Example:

```text
Primary lane: 44_video_vram_optimization
Secondary lane: 45_last_frame_chaining_video_extension
```

Why:

```text
The user has a video-length/VRAM problem, and last-frame chaining may be the workaround.
```

## Training implication

Training records should mark:

```text
primary_lane_id
secondary_lane_ids
used_card_ids
ignored_card_ids
```

This lets the adapter learn:

```text
use the right cards
ignore the wrong cards
cross lanes only when justified
```
