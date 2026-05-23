# ComfyUI Core API, Workflow JSON, and Subgraph Research — Vol. 1 Research Kit

    **Lane ID:** RP03
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** v0.5 focused pass

## Thesis

    Workflow JSON generation must be schema-first: object_info/socket names and link topology are more reliable than remembered node labels.

## What this lane is for

- object_info capture
- workflow JSON validation
- link/socket source-of-truth policy
- subgraph and partial execution patterns
- schema capture scripts
- partner-node boundaries

## What this lane is not for

- guessing node socket names
- generating custom-node workflows without local schema confirmation
- treating display names as class_type strings

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF-Project-Chat-Distribution-Roadmap-v0.5-comfyui-core-api-subgraph` | 12 | 9 | 1 | 1 | 1 |
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
