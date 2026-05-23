# Agent Protocol Lane

Status: concept lane / pre-test  
Version added: v0.2.9-dev19  
Date: 2026-05-23

## Summary

The agent protocol is a smaller part of the larger Atlas Reader LoRA concept.

It does not replace the LoRA experiment.

It tests whether the Atlas structure is useful as an instruction layer before trying to train that behavior into a model.

## Core framing

```text
Agent protocol = tell the agent how to use the Atlas.
LoRA adapter = train a model to internalize the reading behavior.
Chat attachment = give the model the files and hope it organizes them.
```

All three are useful comparison arms.

## Why this matters

If an agent using `AGENTS.md` or a Codex plugin performs better than simply dropping the Atlas into chat as an attachment, that does not prove the LoRA will work.

But it does show that the Atlas protocol can improve behavior when the model is given a persistent instruction layer.

If a Qwen LoRA fails after the agent protocol works, that does not automatically kill the concept.

It may mean:

- training records are wrong;
- learning rate is wrong;
- LoRA rank is wrong;
- target modules are wrong;
- dataset is too scaffold-like;
- the model's chat template is wrong;
- Qwen needs different formatting;
- the adapter learned format instead of behavior;
- the Atlas protocol is useful as instructions but hard to compress into the chosen adapter.

## Proper conclusion discipline

Do not conclude:

```text
LoRA failed, so Atlas failed.
```

Instead conclude:

```text
LoRA failed under this base model, dataset, and config.
Agent protocol results suggest whether the protocol itself is useful before training.
```

## Three-arm comparison

| Arm | Method | Question answered |
|---|---|---|
| A | Chat attachment | Does the model use Atlas if files are attached once? |
| B | Agent protocol | Does persistent repo guidance improve Atlas use? |
| C | LoRA + Atlas RAG | Can training internalize the behavior? |

## Result interpretation

| Result | Interpretation |
|---|---|
| B > A, C fails | Protocol may work; training variables/model/data may be wrong |
| B > A, C > B | Protocol works and adapter adds value |
| A > B | Agent instructions may be too long, unclear, or misplaced |
| C > A and C > B | Training may successfully compress the behavior |
| A, B, C all fail | Atlas structure, questions, or evaluation design may need redesign |

## No-wins boundary

This lane has not been tested yet.

The repo has prepared:

```text
AGENTS.md
plugin skeleton
comparison plan
citation entries
```

It has not proven that Codex, plugins, AGENTS.md, Qwen, or any LoRA improves results.

## Why it belongs in the whole concept

The Atlas project is not only a LoRA project.

It is a question about structured AI guidance:

```text
Can a model use a map better than a pile of files?
```

The LoRA is one possible implementation.

The agent protocol is another.

The chat attachment baseline is the control.
