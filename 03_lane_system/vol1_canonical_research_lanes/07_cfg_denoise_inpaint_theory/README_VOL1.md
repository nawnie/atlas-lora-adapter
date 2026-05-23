# CFG, Denoise, Img2Img, and Inpainting Theory — Vol. 1 Research Kit

    **Lane ID:** RP07
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** focused v0.6 pass inside roadmap archive

## Thesis

    Editing controls are best taught as staged intervention strength: preserve structure first, then repair content, then finish detail.

## What this lane is for

- CFG behavior
- denoise strength
- img2img edit strength
- inpaint conditioning
- crop-and-stitch logic
- mask blur/differential diffusion
- prompt rewrite for restoration
- failure-mode mapping

## What this lane is not for

- one magic setting for all edits
- using high denoise when identity/structure must survive
- teaching inpainting as only prompt writing

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF-Project-Chat-Distribution-Roadmap-v0.6-cfg-denoise-inpaint-theory` | 57 | 53 | 0 | 3 | 0 |
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
