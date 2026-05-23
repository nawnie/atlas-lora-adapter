# RAG Architecture, Chunking, and Embedding Strategy — Vol. 1 Research Kit

    **Lane ID:** RP02
    **Vol. 1 status:** balanced baseline created
    **Status before this correction:** concept scattered across RAG notes and loader notes

## Thesis

    AIWF retrieval should be typed and metadata-rich before it is embedded; dense vectors alone are not enough for code, node names, errors, and package IDs.

## What this lane is for

- typed chunk taxonomy
- metadata contract
- hybrid retrieval policy
- JSONL cards
- CSV record loading
- chunk quality QA
- RAG loader order

## What this lane is not for

- blind folder embedding as the only strategy
- mixing source manifests with semantic cards without metadata
- flattening structured CSVs into anonymous prose

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
