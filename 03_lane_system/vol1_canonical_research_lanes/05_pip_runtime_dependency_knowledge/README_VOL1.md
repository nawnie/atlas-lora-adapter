# Python/Pip Runtime Dependencies and Local AI Environment Support — Vol. 1 Research Kit

    **Lane ID:** RP05
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** already broad v1.9 package map; needs balanced Vol. 1 bridge into the full data pack

## Thesis

    Runtime failures are cluster failures, not isolated package failures; AIWF support should reason across Python, Torch, CUDA, cuDNN, ONNX, media, web server, and native build boundaries.

## What this lane is for

- package cards
- dependency clusters
- native build failures
- CUDA/cuDNN/TensorRT/Triton maps
- Windows venv islands
- one-click installer support
- smoke-test scripts

## What this lane is not for

- unverified pin advice for every future package version
- blind pip upgrade-all guidance
- mixing incompatible CUDA/Torch wheel families

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF_Pip_Package_RAG_Starter_v1_9` | 438 | 366 | 10 | 8 | 43 |
| `AIWF_Pip_Package_RAG_Starter_v1_5` | 2 | 0 | 0 | 2 | 0 |

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
