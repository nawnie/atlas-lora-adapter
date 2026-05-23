# Evaluation Plan

## Main research question

Can Atlas Reader LoRA improve how a model uses structured RAG context?

## Conditions

1. Base model, no RAG
2. Base model + raw RAG
3. Base model + Atlas RAG
4. Base model + Atlas Reader LoRA + Atlas RAG

## Model sizes

Initial target:

- 4B-class instruct model
- 7B-class instruct model

## Task categories

- lane routing;
- answer from context;
- conflict resolution;
- insufficient context;
- exactness guard;
- freshness check;
- answer-format selection;
- multi-RAG generalization.

## Scoring

Use `RUBRIC.md`.

Each answer receives scores for:

- grounding;
- exactness;
- actionability;
- retrieval discipline;
- beginner safety;
- format fit;
- uncertainty handling.

## Required outputs

For each experiment:

- model name;
- model size;
- adapter state;
- RAG condition;
- retrieval method;
- prompt template;
- question ID;
- answer;
- scores;
- notes;
- failure tags.

## Failure tags

Suggested tags:

```text
ignored_context
used_wrong_lane
invented_command
invented_path
invented_node_name
missed_freshness_warning
over_refused
under_refused
wrong_format
unsafe_beginner_advice
metadata_ignored
source_priority_failure
```
