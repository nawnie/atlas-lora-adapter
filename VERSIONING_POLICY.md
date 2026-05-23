# Versioning and Release Policy

Status: active project policy  
Project version: v0.2 planning track  
Date: 2026-05-22

## Current project status

This project is still in planning and research-design status.

The current project state should be described as:

```text
v0.2 — clear plan, no trained adapter yet
```

The repository has a defined concept, architecture, roadmap, lane/card targets, naming contract, and evaluation intent. It does not yet have a trained model, completed dataset, benchmark results, or released adapter.

## Versioning rule

Do not keep bumping major or large phase numbers for documentation-only changes.

Use small patch versions unless there is a meaningful project-state change.

Recommended version pattern:

```text
v0.1   initial concept
v0.2   clear project plan and architecture
v0.2.1 small documentation/schema/roadmap updates
v0.3   first usable dataset seed and validation scripts
v0.4   first baseline evaluation without LoRA
v0.5   first small training run attempt
v0.6   first repeatable training pipeline
v0.7   first cross-model or cross-corpus comparison
v0.8   candidate release with reproducible evaluation package
v0.9   pre-v1 release candidate
v1.0   first trained adapter results publicly reported
```

## v1.0 gate

v1.0 does not mean success.

v1.0 means the project has completed and reported the first real trained-model experiment.

The result can be positive, negative, or mixed.

The v1.0 release requires:

1. a trained Atlas Reader LoRA or clearly documented failed training attempt;
2. documented base model and training setup;
3. dataset version used;
4. Atlas contract version used;
5. evaluation questions and rubric;
6. raw results;
7. analysis of what worked and what failed;
8. public outcome report.

## Important principle

A failed model can still be a successful research artifact if the failure is documented clearly.

The project is committed to sharing the outcome either way.

The v1.0 report should answer:

```text
Did structured Atlas-style RAG improve model behavior?
Did Atlas Reader LoRA improve how the model used that RAG?
Where did smaller models still fail?
Did the lane/card contract help or create confusion?
What should be changed before the next training run?
```

## Naming note

Earlier archive names used phase labels such as Phase 3, Phase 4, Phase 5, and Phase 6. Treat those as build-session packaging labels, not true product maturity versions.

Going forward, use semantic project versions.

Current corrected archive line:

```text
atlas-lora-adapter-v0.2.1-planning-2026-05-22.zip
```

## Patch version guidance

Use patch versions for:

- wording polish;
- README updates;
- schema field tweaks;
- naming convention improvements;
- roadmap cleanup;
- small sample-record additions;
- non-breaking documentation.

Example:

```text
v0.2.1
v0.2.2
v0.2.3
```

## Minor version guidance

Use minor versions for meaningful project movement.

Examples:

```text
v0.3 = first validated dataset seed
v0.4 = first baseline raw RAG vs Atlas RAG results
v0.5 = first adapter training attempt
```

## Major version guidance

Do not use v1.0 until the first trained model experiment has been completed and results have been posted.

The result does not need to be good.

It needs to be real, documented, and reproducible enough to learn from.

## Human approval gate for milestone jumps

No AI assistant, automated script, agent, or outside reviewer may promote this project from an `x.x.9` release to the next `x+1.0` or `x.(x+1).0` milestone release without explicit approval from Shawn O'Hagan.

Examples:

```text
v0.2.9 -> v0.3.0 requires Shawn approval
v0.3.9 -> v0.4.0 requires Shawn approval
v0.9.9 -> v1.0.0 requires Shawn approval
v0.9 -> v1.0 requires Shawn approval
```

An AI may recommend a release promotion, prepare evidence, and draft release notes. It may not make the promotion official.

Required approval language should be explicit, such as:

```text
Approved: promote to v0.3.0
```

or:

```text
I approve this as v0.3.0
```

Ambiguous replies such as `A`, `continue`, `looks good`, or `package it` do not authorize a milestone version jump.

See `HUMAN_RELEASE_APPROVAL_GATE.md`.
