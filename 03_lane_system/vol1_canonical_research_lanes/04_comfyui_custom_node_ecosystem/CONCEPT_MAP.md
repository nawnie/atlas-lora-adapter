# Concept Map — ComfyUI Custom Node Ecosystem and Nodepack Evaluation

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| safe_to_generate | guarded_generate_after_schema_check, RAG-only node | query anchor / metadata facet |
| guarded_generate_after_schema_check | RAG-only node, nodepack summary | query anchor / metadata facet |
| RAG-only node | nodepack summary, install risk | query anchor / metadata facet |
| nodepack summary | install risk, maintenance mode | query anchor / metadata facet |
| install risk | maintenance mode, native core vs wrapper | query anchor / metadata facet |
| maintenance mode | native core vs wrapper, class_type verification | query anchor / metadata facet |
| native core vs wrapper | class_type verification, safe_to_generate | query anchor / metadata facet |
| class_type verification | safe_to_generate, guarded_generate_after_schema_check | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP08 — Compatibility Matrix RAG
- RP09 — Failure Signature Atlas RAG
