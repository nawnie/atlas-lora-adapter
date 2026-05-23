# Baseline Matrix

## Core matrix

| ID | Model size | Adapter | RAG condition | Purpose |
|---|---|---|---|---|
| B4-NO | 4B | none | none | base small-model behavior |
| B4-RAW | 4B | none | raw RAG | raw retrieval benefit |
| B4-ATLAS | 4B | none | Atlas RAG | structured RAG benefit |
| B4-LORA-ATLAS | 4B | Atlas Reader LoRA | Atlas RAG | adapter benefit |
| B7-NO | 7B | none | none | larger baseline |
| B7-RAW | 7B | none | raw RAG | larger raw retrieval |
| B7-ATLAS | 7B | none | Atlas RAG | larger structured RAG |
| B7-LORA-ATLAS | 7B | Atlas Reader LoRA | Atlas RAG | best expected condition |

## What to test

The most important comparison is not only raw score.

Look for behavior changes:

- Does the model use the right lane?
- Does it ignore stale archive chunks?
- Does it refuse to invent exact identifiers?
- Does it ask for verification only when needed?
- Does it produce the right answer format?
- Does the smaller model close the gap with the larger model on bounded tasks?
