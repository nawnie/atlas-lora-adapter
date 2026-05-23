# Architecture Overview

## System components

```text
Base model
  + Atlas Reader LoRA
  + structured RAG corpus
  + retrieval policy / system prompt
  + evaluation harness
  = source-aware domain assistant
```

## Responsibilities

| Component | Responsibility |
|---|---|
| Base model | language generation, reasoning, instruction following |
| Atlas-style RAG | external knowledge, source paths, lane context, exact references |
| Atlas Reader LoRA | reading discipline, routing, source hierarchy, answer behavior |
| System prompt | runtime policy and project-specific rules |
| Evaluation harness | proof, regression checks, failure analysis |

## Design principle

Do not train the adapter to memorize facts that should remain in RAG.

Train the adapter to:

- read metadata;
- respect source priority;
- choose the right lane;
- detect weak context;
- avoid unsupported exact identifiers;
- produce useful answer formats.

## Deployment pattern

```text
Question
  -> retrieve context from structured RAG
  -> attach metadata and source roles
  -> model + Atlas Reader LoRA reads context
  -> answer follows source discipline
  -> evaluation records quality
```

## Future adapter stack

Possible future adapters:

```text
Atlas Reader LoRA
AIWF Voice LoRA
Code Repair LoRA
Tool-Use Discipline LoRA
```

These should be tested separately before combining.
