# Repackage QC v0.2.9-dev20

Status: repackage/QC pass  
Date: 2026-05-23

## User request

- Repackage the repo.
- Put LoRA training stuff in its own root folder.
- Pull in updated AIWF Atlas information.
- Add lanes/cards where useful.
- Make training easy to remove before using repo as RAG.

## Results

```text
lora_training_lab isolated: yes
uploaded source preserved without .git: yes
canonical VOL1 lanes copied: 35
canonical VOL1 retrieval cards copied: 410
all lane/card dirs after merge: 53
all retrieval cards after merge: 626
incoming files preserved: 2137
```

## Full repo archive

Includes `lora_training_lab/`.

## RAG-clean archive

Generated separately with `lora_training_lab/` removed.

## No-wins boundary

No adapter has been trained. No local install result exists. No performance claim is added by this repackage.
