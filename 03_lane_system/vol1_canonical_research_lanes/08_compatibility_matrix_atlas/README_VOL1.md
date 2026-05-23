# Compatibility Matrix RAG — Vol. 1 Research Kit

    **Lane ID:** RP08
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** concept note only; now promoted to Vol. 1 lane

## Thesis

The assistant should answer “will this work together?” before it answers “how do I install it?”

## What this lane is for

- hardware/software compatibility
- model asset placement
- nodepack requirements
- Python/CUDA/Torch compatibility
- workflow missing asset detection
- commercial/license caveats

## What this lane is not for

- assuming all models fit all hardware
- installing every nodepack in one environment without risk separation
- ignoring model license when building public workflows

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF_RAG_Concept_Additions_v0_1` | 8 | 6 | 0 | 2 | 0 |
| `AIWF_Pip_Package_RAG_Starter_v1_9` | 438 | 366 | 10 | 8 | 43 |
| `aiwf_node_research_pass02N_flux_model_control_sampler_mds_v1_4` | 246 | 114 | 119 | 13 | 0 |

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
