---
name: atlas-reader
description: Follow the AIWF Atlas protocol when editing or reviewing the repo.
---

# AIWF Atlas Reader Skill

Use this skill when the user asks to work on the Atlas Reader LoRA repo, AIWF source docs, training records, evaluation plans, or installer/training scripts.

## Operating rules

1. Preserve no-wins status unless measured logs exist.
2. Treat report templates as templates.
3. Use source/citation files before adding factual claims.
4. Prefer small, reviewable changes.
5. Do not promote milestones automatically.
6. Distinguish:
   - chat attachment baseline;
   - agent protocol behavior;
   - LoRA-trained behavior.

## Required checks

Before claiming a result, confirm the repo contains a real output file or run log.

If no run log exists, use:

```text
not run yet
not verified yet
template only
prepared for testing
```

## Comparison logic

If agent-guided behavior looks better than chat attachment behavior, mark that as an agent-protocol observation only.

If a LoRA fails on Qwen, do not conclude the Atlas failed. Check:

- base model choice;
- chat template;
- record formatting;
- rank;
- target modules;
- learning rate;
- dropout;
- training data quality;
- eval split;
- context-pack construction.

## Preferred output

Be direct, source-aware, and practical.

No hype.

No fake wins.

Unknown means instrument it.
