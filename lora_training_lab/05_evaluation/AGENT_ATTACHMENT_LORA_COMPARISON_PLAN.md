# Agent vs Attachment vs LoRA Comparison Plan

Status: pre-test evaluation design  
Version added: v0.2.9-dev19  
Date: 2026-05-23

## Purpose

This plan separates three different ways of giving Atlas guidance to a model/agent.

The goal is to avoid confusing an agent-protocol win with a LoRA-training win, or a LoRA-training failure with total Atlas failure.

## Arms

| Arm | Name | Description |
|---|---|---|
| A | Chat attachment baseline | Attach Atlas docs/files to chat and ask the model to use them |
| B | Agent protocol | Put Atlas guidance in `AGENTS.md`, repo docs, and optional Codex plugin skill |
| C | LoRA + Atlas RAG | Train an adapter and use it with Atlas retrieval/context packs |

## Hypotheses

### H1: Agent protocol can beat attachment baseline

If B > A, the Atlas protocol may be useful as persistent instructions.

This does not prove LoRA works.

### H2: LoRA failure does not automatically disprove protocol

If B > A and C fails, investigate training variables before rejecting Atlas.

Possible issues:

- Qwen-specific chat template mismatch;
- bad SFT formatting;
- rank too low or too high;
- wrong target modules;
- learning rate mismatch;
- scaffold leakage;
- missing negative examples;
- insufficient context-pack examples;
- weak exactness/freshness examples.

### H3: LoRA success requires C > B or C improves target behavior

If C only matches B, the adapter may not add enough value.

If C improves exactness, freshness, or distractor rejection beyond B, the adapter may be worth continued research.

## Suggested test set

Use the same 25 smoke questions from:

```text
05_evaluation/GOLDEN_QUESTIONS_SMOKE_25.jsonl
```

Run each question through:

```text
A: chat attachment baseline
B: AGENTS.md / agent protocol
C: LoRA + Atlas RAG
```

## Scoring

Use the existing smoke metrics:

```text
route_correct
source_grounded
exactness_guard
actionable
freshness_handled
avoids_distractor
compact_answer
pass
```

Add one field:

```text
guidance_mode = attachment | agent_protocol | lora_atlas_rag
```

## Interpretation table

| Pattern | Meaning |
|---|---|
| B beats A | persistent instructions may help |
| C fails but B beats A | training variables may be wrong; protocol still alive |
| C beats B | adapter may be learning useful behavior |
| A beats B | AGENTS/plugin guidance may be unclear or too broad |
| All fail | evaluation questions or Atlas structure may need redesign |

## No-result boundary

This file is only a comparison plan.

No comparison has been run yet.
