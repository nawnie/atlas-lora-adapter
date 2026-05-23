# Citation Style Guide

Status: active citation style guide  
Version added: v0.2.9-dev11  
Date: 2026-05-22

## Purpose

This guide keeps source language consistent across the repo.

## Citation files

Use these as the source system:

```text
10_source_materials/SOURCE_CITATIONS.md
10_source_materials/CITATION_MATRIX.md
10_source_materials/CITATION_REGISTRY.json
10_source_materials/REFERENCES.bib
10_source_materials/CONVERSATION_SOURCE_AUDIT.md
```

## Markdown citation style

Use citation keys in square brackets when writing repo docs:

```text
Retrieval-aware fine-tuning is prior art [zhang2024raft].
LoRA itself is prior art [hu2021lora].
QLoRA supports memory-efficient adapter training [dettmers2023qlora].
```

For official docs:

```text
The training script uses TRL SFTTrainer behavior documented by Hugging Face [hf_trl_sfttrainer].
```

## When to cite

Cite when claiming:

- prior art exists;
- a training API supports a feature;
- a paper introduced a method;
- a source justifies a training setting;
- a current tool behavior is being described;
- a performance or evaluation result exists.

## When not to cite

Do not cite:

- AI assistant output;
- drafting chats;
- unsourced summaries;
- project metaphors as evidence;
- diagrams as proof.

## Source priority

For technical/API claims:

```text
official documentation > repo source code > blog/tutorial > assistant summary
```

For research claims:

```text
paper/preprint > official project page > secondary article > assistant summary
```

For Atlas project claims:

```text
measured project outputs > project source docs > planning notes > discussion drafts
```

## Fast-moving claims

Mark these as freshness-sensitive:

- current model recommendation;
- package version;
- API behavior;
- commercial license;
- hardware compatibility;
- pricing;
- security guidance.

## Public release rule

Before public release, every citation should have:

```text
key
title
authors or organization
year
URL
what claim it supports
```

That is now tracked in `CITATION_REGISTRY.json`.
