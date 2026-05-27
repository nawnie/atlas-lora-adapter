# AI Without Fear — Atlas Reader LoRA Lab

<p align="center">
  <img src="08_visuals/AIWF_LOGO.png" alt="AI Without Fear logo" width="220">
</p>

## Current status

The repo has moved past the initial pre-training scaffold phase.

A first measured O mixed-schema off-ramp adapter run has been recorded. This is an internal evaluation result, not a final proof of open-world generalization.

Current best evaluated direction:

```text
O_mixed_schema_offramp_4b_r16_lr0001_1epoch
```

Key O results:

| Eval | O Result |
|---|---:|
| Compact seed cards | 65/65 |
| Targeted top-1 card | 64/65 |
| Targeted top-3 cards | 65/65 |
| Off-ramp focused | 8/8 |
| Hard ID-copy | 14/16 |

See:

```text
docs/atlas/o_mixed_schema_offramp/O_MIXED_SCHEMA_OFFRAMP_REPORT.md
05_evaluation/previous_adapter_results/PREVIOUS_ADAPTER_RESULTS_FROM_8ZIP.md
```

## Concept summary

Atlas Reader LoRA is a structured-RAG research project testing whether a small LoRA adapter can learn a portable reading protocol for a named Atlas contract.

```text
A normal RAG gives the model a pile of notes.
An Atlas gives it a map.
The Atlas Reader LoRA teaches the model how to read the map.
```

The Atlas keeps the knowledge.

The LoRA target is structured Atlas use, not memorization of the Atlas contents.

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

This project targets a bounded research question with measurable outcomes:

```text
Can a small adapter improve how a model reads structured RAG context?
```

The O run supports the mixed-schema off-ramp direction under the recorded internal evaluation conditions. Broader validation is still required.

## AI Without Fear identity

This project is part of the **AI Without Fear** ecosystem.

AIWF framing:

```text
Master principles, not platforms.
Train the behavior. Keep the knowledge in the Atlas.
No proof without a run log.
```

## What this project is

This project is a research/design repository for:

- structured Atlas lanes;
- compact retrieval cards;
- context-pack routing;
- source-priority and exactness-guard behavior;
- small-model-first adapter experiments;
- evaluation before broad performance claims.

## What this project is not

This project is **not** claiming:

- a new LoRA algorithm;
- a new foundation model;
- proof that the adapter transfers across domains;
- proof that small models equal larger models globally;
- that diagrams or metaphors are research evidence;
- that Atlas replaces current source verification.

## Target adapter behavior

```text
read query
select primary lane
use selected cards
ignore distractors
respect source priority
qualify stale/missing evidence
use off-ramp behavior when Atlas evidence is absent
answer compactly
```

## Evaluation path

Earlier adapter results are summarized in:

```text
05_evaluation/previous_adapter_results/
```

The O mixed-schema off-ramp result is summarized in:

```text
docs/atlas/o_mixed_schema_offramp/
```

The next useful run is a P cleanup pass focused on exact lane/card ID preservation and clean answer wording.

## Source policy

Citable sources for this project are:

- primary papers;
- official docs;
- official repositories/model cards;
- measured local outputs;
- project-authored notes clearly marked as drafts or internal reasoning.

AI assistants and drafting tools are not evidence sources.

See:

```text
01_strategy/SOURCE_AND_ATTRIBUTION_POLICY.md
```
