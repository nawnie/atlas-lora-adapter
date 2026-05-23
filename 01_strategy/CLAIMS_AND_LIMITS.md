# Claims and Limits

## Safe claims

The project may claim:

- Atlas Reader LoRA is a proposed adapter strategy.
- The adapter is intended to improve structured-RAG reading behavior.
- The adapter should train behavior, not facts.
- The project will compare no RAG, raw RAG, Atlas RAG, and Atlas Reader LoRA + Atlas RAG.
- The project may help smaller models perform better in bounded source-grounded tasks if evaluation supports it.

## Claims to avoid

Do not claim:

- Atlas Reader LoRA is a new LoRA algorithm.
- It makes RAG obsolete.
- It makes a 4B model equal a 7B model globally.
- One adapter file works across all model architectures.
- The adapter improves results before experiments show it.
- The adapter contains current truth about volatile tools, packages, models, or APIs.
- It replaces official documentation.

## Correct positioning

Atlas Reader LoRA is best described as:

> a new practical adapter use-pattern: a LoRA trained to improve how a model reads, ranks, and applies structured RAG context.

## Research posture

Negative results should be preserved.

Failure can still teach:

- where base models ignore metadata;
- where RAG structure helps without LoRA;
- which behaviors are hard to train;
- whether small models lack enough capacity for the reading task;
- whether the dataset overfits to AIWF-specific language.
