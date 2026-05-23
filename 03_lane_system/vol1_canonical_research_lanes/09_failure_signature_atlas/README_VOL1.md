# Failure Signature Atlas RAG — Vol. 1 Research Kit

    **Lane ID:** RP09
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** concept note plus scattered package/runtime failure maps

## Thesis

    Failures should be retrieved by symptom, log fragment, likely layer, and safe recovery path, not just by package name.

## What this lane is for

- OOM signatures
- missing node signatures
- missing model signatures
- import/ABI errors
- CUDA/cuDNN provider issues
- workflow red-node diagnosis
- bad generation symptoms

## What this lane is not for

- guessing root cause from one vague symptom
- fixing by reinstalling everything first
- mixing destructive repair steps into beginner guidance

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF_RAG_Concept_Additions_v0_1` | 8 | 6 | 0 | 2 | 0 |
| `AIWF_Pip_Package_RAG_Starter_v1_9` | 438 | 366 | 10 | 8 | 43 |
| `AIWF-Project-Chat-Distribution-Roadmap-v0.6-cfg-denoise-inpaint-theory` | 57 | 53 | 0 | 3 | 0 |

## Vol. 1 kit files

- `VOL1_SCOPE.md`
- `CANONICAL_OVERVIEW.md`
- `CONCEPT_MAP.md`
- `EMBEDDING_AND_CHUNKING_STRATEGY.md`
- `RETRIEVAL_CARDS.jsonl`
- `QA_TEST_PROMPTS.md`
- `GAP_AUDIT_AND_VOL2_QUEUE.md`
- `SOURCE_COVERAGE.md`
- `vol1_lane_manifest.json`

## RAG load recommendation

    Load this lane after the preserved source folders. Treat this lane as the canonical, balanced Vol. 1 synthesis for retrieval and planning. The original source folders remain provenance.
