# Brand and Positioning Guide

Status: active brand guide  
Version added: v0.2.9-dev11  
Date: 2026-05-22

## One-sentence positioning

Atlas Reader LoRA tests whether a small adapter can learn a portable reading protocol for a named, versioned structured-RAG contract.

## Plain-language version

A normal RAG gives the model a pile of notes.

An Atlas gives the model a map.

Atlas Reader LoRA tries to teach the model how to read that map.

## Voice

Use a clear field-manual voice:

- direct;
- practical;
- source-aware;
- honest about limits;
- excited, but not hype-driven;
- friendly without sounding like sales copy.

## Core metaphor

Use:

```text
map
lanes
cards
context pack
source rules
proof by measured run
```

Avoid:

```text
magic
breakthrough
new algorithm
autonomous researcher
solves RAG
replaces larger models
```

## Claim boundaries

Safe:

```text
This project proposes a methodology/interface standard.
This project tests whether a content-agnostic adapter can learn Atlas reading behavior.
This project has not trained or evaluated an adapter yet.
This project treats negative results as useful research.
```

Unsafe:

```text
This is a new LoRA algorithm.
This proves small models can match larger models.
This proves Atlas RAG is better than raw RAG.
This adapter works before training/evaluation.
```

## Source language

Use:

```text
cited source
primary paper
official documentation
project-authored draft
measured local output
```

Avoid:

```text
AI said
Claude said
ChatGPT said
the bot found
```

AI assistants are drafting aids, not sources.

## Good public phrasing

> Atlas Reader LoRA is a structured-RAG adapter research project. It does not invent LoRA or retrieval-aware fine-tuning; it tests a specific interface idea: a versioned Atlas contract that a small adapter can learn to navigate.

## Bad public phrasing

> We invented a new way to make tiny models as smart as large models.

## The project's strongest claim

The strongest current claim is not performance.

The strongest current claim is disciplined research design:

```text
clear hypothesis
bounded contribution
source-aware related work
versioned contract
training plan
smoke protocol
negative-result policy
```

## The next proof point

The next proof point is the smoke train:

```text
base model + Atlas RAG
vs
base model + Atlas Reader LoRA + Atlas RAG
```

Until that runs, all performance language must remain conditional.


## AIWF brand layer

This project should be presented as:

```text
AI Without Fear — Atlas Reader LoRA Lab
```

The technical artifact remains:

```text
Atlas Reader LoRA
```

The AIWF layer gives it public identity, educational tone, and continuity with the broader AI Without Fear ecosystem.

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
