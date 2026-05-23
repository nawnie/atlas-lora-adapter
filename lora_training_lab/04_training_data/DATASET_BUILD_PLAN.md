# Dataset Build Plan

## Target seed size

Start with:

```text
100-200 training records
25-50 evaluation questions
```

## First source lanes

Use three bounded lanes:

1. ComfyUI socket contract debugging
2. Video VRAM optimization
3. Retrieval card authoring

## Record construction workflow

For each record:

1. Pick a task type.
2. Write a realistic user question.
3. Attach 1-3 relevant context chunks.
4. Optionally attach 1 distractor chunk.
5. Mark expected source use and source ignore rules.
6. Write the ideal output.
7. Validate against schema.
8. Manually review for overclaiming.

## Quality rules

Each record should:

- teach a behavior, not a fact dump;
- avoid stale specifics unless the output flags them as volatile;
- include metadata where possible;
- punish hallucinated exact identifiers;
- preserve source hierarchy;
- include enough context for the expected answer.

## Dataset splits

Recommended initial split:

```text
train: 80%
validation: 10%
test: 10%
```

Do not put near-duplicate questions in different splits.
