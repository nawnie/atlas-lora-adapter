# Concept Map — RAG Architecture, Chunking, and Embedding Strategy

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| semantic markdown | structured rows, json records | query anchor / metadata facet |
| structured rows | json records, code-aware chunks | query anchor / metadata facet |
| json records | code-aware chunks, metadata-only files | query anchor / metadata facet |
| code-aware chunks | metadata-only files, hybrid retrieval | query anchor / metadata facet |
| metadata-only files | hybrid retrieval, reranking | query anchor / metadata facet |
| hybrid retrieval | reranking, heading path | query anchor / metadata facet |
| reranking | heading path, chunk intent | query anchor / metadata facet |
| heading path | chunk intent, retrieval test prompt | query anchor / metadata facet |
| chunk intent | retrieval test prompt, semantic markdown | query anchor / metadata facet |
| retrieval test prompt | semantic markdown, structured rows | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP08 — Compatibility Matrix RAG
- RP09 — Failure Signature Atlas RAG
