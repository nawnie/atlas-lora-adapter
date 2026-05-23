# Source Ledger and Evidence Governance — Vol. 1 Research Kit

    **Lane ID:** RP01
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** concept/early structure

## Thesis

The RAG should know why it believes a claim, where the claim came from, and when the claim must be refreshed.

## What this lane is for

- source registry design
- evidence quality labels
- refresh queues
- source-to-card lineage
- duplicate/source conflict handling
- claim confidence policy

## What this lane is not for

- making unsupported factual claims
- treating old chat notes as canonical without source grading
- overwriting provenance labels

## Source folders used

    | Source folder | Files | Markdown | CSV | JSON/JSONL | Code |
    |---|---:|---:|---:|---:|---:|
    | `AIWF-Project-Chat-Distribution-Roadmap-v0.3-rag-source-ledger` | 8 | 8 | 0 | 0 | 0 |
| `AIWF-Project-Chat-Distribution-Roadmap-v0.6-cfg-denoise-inpaint-theory` | 57 | 53 | 0 | 3 | 0 |
| `AIWF_RAG_Concept_Additions_v0_1` | 8 | 6 | 0 | 2 | 0 |

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
