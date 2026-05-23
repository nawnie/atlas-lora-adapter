# Release Gates

Status: active planning document  
Current gate: v0.2 planning / v0.2.9-dev21 GitHub upload prep

## Current status

The project currently has a clear research path, but no trained adapter.

Current version:

```text
v0.2.9-dev21
```

Next small update version:

```text
v0.2.9-dev22 or owner-approved v0.3.0
```

## Gate table

| Version | Gate | What must exist |
|---|---|---|
| v0.1 | Concept seed | Initial idea, plain-language explanation, rough strategy |
| v0.2 | Planning lock | Architecture, roadmap, Atlas contract, lane/card targets |
| v0.2.1 | Planning patch | Versioning policy, cleanup, small docs/schema corrections |
| v0.3 | Dataset seed | First validated training records and validator pass |
| v0.4 | Baseline eval | Raw RAG vs Atlas RAG baseline results |
| v0.5 | First training attempt | First LoRA training run or documented failed attempt |
| v0.6 | Repeatable pipeline | Training steps can be repeated from docs/scripts |
| v0.7 | Comparison pass | Small vs larger model or cross-corpus comparison |
| v0.8 | Research package | Evaluation package and findings prepared for outside review |
| v0.9 | v1 candidate | Release candidate with results and reproduction notes |
| v1.0 | First public result | First trained-model result posted, whether good or bad |

## v1.0 release rule

v1.0 is not a marketing milestone.

v1.0 is the first completed evidence milestone.

A v1.0 release may say:

- the adapter helped;
- the adapter did not help;
- the adapter helped only in narrow cases;
- the dataset was not strong enough;
- smaller models still failed;
- the Atlas contract needs redesign.

All of those outcomes are valid if documented honestly.

## Project commitment

The project is committed to sharing the outcome.

If the LoRA works, the results should be posted.

If the LoRA fails, the failure data should be posted.

The research value is in the measured outcome, not in pretending the first attempt worked.

## Detailed milestone file

Detailed version-by-version milestone gates are now tracked in:

```text
MILESTONES.md
```

Use `MILESTONES.md` as the primary task-control file for v0.3 through v1.0.

## Human approval requirement

All milestone jumps from an `x.x.9` release to the next `.0` release require explicit approval from Shawn O'Hagan.

This applies even when the documented exit gate appears complete.

The release gate can be marked `ready_for_owner_review`, but it cannot be marked `approved` or promoted until Shawn gives explicit approval.

See:

```text
HUMAN_RELEASE_APPROVAL_GATE.md
```
