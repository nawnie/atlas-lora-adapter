# Atlas Reader LoRA — Public Summary Draft

Status: public-facing draft  
Version added: v0.2.9-dev11  
Date: 2026-05-22

## What it is

Atlas Reader LoRA is a structured-RAG adapter experiment.

It asks a simple question:

```text
Can a small LoRA learn how to read a structured knowledge map without memorizing the map itself?
```

## Why it exists

A normal RAG system often retrieves chunks.

This project organizes knowledge into:

```text
lanes
cards
source-priority rules
do-not-confuse rules
answer patterns
5-card context packs
```

The goal is to make small models less lost when they receive retrieved context.

## Current status

```text
seed lanes: 18
seed cards: 216
citation records: 22
diagrams: 3
trained adapters: 0
completed training runs: 0
```

## What has been built

- Atlas lane/card structure;
- training-record schemas;
- training-data QC gates;
- related-work positioning;
- source and citation system;
- smoke-train evaluation protocol;
- runnable TRL/PEFT QLoRA training layer;
- diagrams for the routing model.

## What has not been proven

The project has not yet proven:

- the adapter works;
- Atlas RAG beats raw RAG;
- small models match larger models;
- the contract transfers to a second domain.

Those are testable claims for future runs, not current conclusions.

## Why the project may matter

The contribution is not a new LoRA algorithm.

The possible contribution is a clean interface discipline:

```text
a named Atlas contract
a portable reading adapter
a small-model-first card budget
a measurable evaluation protocol
```

If the adapter transfers to another Atlas, the project has a stronger research result.

If it fails, the failure is still useful because the repo is structured to show what broke.

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
