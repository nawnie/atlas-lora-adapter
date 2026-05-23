# Research Value Note

This project is useful even if the first Atlas Reader LoRA does not work.

## Why failure still matters

A failed experiment can still answer important questions:

- Do models ignore metadata in retrieved context?
- Do smaller models fail at source hierarchy even when retrieval is good?
- Does Atlas-style structure improve results without any LoRA?
- Does the LoRA overfit to AIWF vocabulary?
- Does the adapter improve formatting but not factuality?
- Does exactness improve while actionability drops?
- Are lane names helping or confusing retrieval?

## What to preserve

For every failed experiment, preserve:

- model and adapter details;
- RAG condition;
- prompt format;
- training data version;
- evaluation questions;
- raw answers;
- rubric scores;
- failure tags;
- qualitative notes.

## Useful negative outcomes

| Finding | Why it matters |
|---|---|
| Atlas RAG helps but LoRA does not | Better retrieval may be enough. |
| LoRA helps 7B but not 4B | Smaller model may lack capacity. |
| LoRA improves format only | Dataset needs stronger source-discipline examples. |
| LoRA overfits to AIWF | Need more multi-RAG examples. |
| Model ignores metadata | Context format or prompt design needs revision. |
| Exactness improves | Adapter may be useful even if overall score is mixed. |

## Research posture

Do not hide failures.

This repo should become a record of what actually helps models read structured RAG.
