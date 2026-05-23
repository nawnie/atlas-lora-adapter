# ComfyUI Custom Node Ecosystem and Nodepack Evaluation — Vol. 1 Research Kit

    **Lane ID:** RP04
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** large but uneven pass with high coverage in some packs and RAG-only notes in others

## Thesis

    AIWF should evaluate existing node packs before building new nodes, then classify each pack as use, wrap, document, or build.

## What this lane is for

- nodepack coverage
- workflow generation safety
- class_type strings
- install risk
- maintenance status
- model file requirements
- ComfyUI Manager install flow

## What this lane is not for

- rebuilding solved node packs without a clear gap
- using deprecated IDs in new workflows
- making beginner workflows depend on unstable expert wrappers by default

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `aiwf_node_research_pass02N_flux_model_control_sampler_mds_v1_4` | 246 | 114 | 119 | 13 | 0 |
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
