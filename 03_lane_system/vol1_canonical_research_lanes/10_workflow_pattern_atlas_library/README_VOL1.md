# Workflow Pattern Library RAG — Vol. 1 Research Kit

    **Lane ID:** RP10
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** concept note plus ComfyUI workflow policy/source passes

## Thesis

    Reusable workflow patterns should be stored as task graphs with required nodes/assets, not as giant one-off JSON blobs.

## What this lane is for

- pattern cards
- workflow graph motifs
- router shell design
- model-loader patterns
- inpaint/upscale/video patterns
- subgraph/componentization policy
- QA smoke tests

## What this lane is not for

- stapling unrelated workflows together without routing logic
- assuming JSON can be generated safely without object_info
- hiding required user inputs deep in the graph

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF_RAG_Concept_Additions_v0_1` | 8 | 6 | 0 | 2 | 0 |
| `AIWF-Project-Chat-Distribution-Roadmap-v0.5-comfyui-core-api-subgraph` | 12 | 9 | 1 | 1 | 1 |
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
