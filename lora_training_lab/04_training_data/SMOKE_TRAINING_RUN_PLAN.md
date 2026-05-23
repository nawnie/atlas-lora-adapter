# Smoke Training Run Plan

Status: planning / seed-build  
Version added: v0.2.9-dev3

## Purpose

The first training run should prove that the training pipeline works.

It should not be treated as proof that Atlas Reader LoRA improves model performance.

## Smoke run target

```text
300-600 training records
18 seed lanes
216 seed cards
small instruct base model
LoRA/QLoRA-style adapter
```

## Success criteria

A smoke run succeeds if:

- training script runs;
- adapter artifact is produced;
- loss behaves reasonably;
- sample outputs follow the requested format better than base;
- evaluation scripts can compare base vs adapter.

## Failure is acceptable

A smoke run can fail due to:

- dataset format issue;
- tokenizer/chat-template mismatch;
- GPU memory issue;
- bad target modules;
- training instability;
- weak examples.

A failed smoke run should produce a failure report, not a silent reset.

## What smoke run does not prove

It does not prove:

- the adapter improves small models generally;
- 4B equals 7B;
- Atlas RAG is better than raw RAG;
- the 128-lane design is correct;
- v1.0 is ready.

## Minimum report

After the smoke run, write:

```text
base model
adapter config
dataset version
record count
training command
hardware
result
sample outputs
failure notes
next decision
```
