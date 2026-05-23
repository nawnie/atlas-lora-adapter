# Concept Map — Source Ledger and Evidence Governance

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| source ledger | evidence grade, claim lineage | query anchor / metadata facet |
| evidence grade | claim lineage, refresh queue | query anchor / metadata facet |
| claim lineage | refresh queue, canonical source | query anchor / metadata facet |
| refresh queue | canonical source, derived card | query anchor / metadata facet |
| canonical source | derived card, provenance path | query anchor / metadata facet |
| derived card | provenance path, conflict note | query anchor / metadata facet |
| provenance path | conflict note, staleness risk | query anchor / metadata facet |
| conflict note | staleness risk, source ledger | query anchor / metadata facet |
| staleness risk | source ledger, evidence grade | query anchor / metadata facet |

## Cross-lane links

- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP08 — Compatibility Matrix RAG
- RP09 — Failure Signature Atlas RAG
