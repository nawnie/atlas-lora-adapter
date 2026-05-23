# Concept Map — Compatibility Matrix RAG

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| compatibility edge | requirement node, model path | query anchor / metadata facet |
| requirement node | model path, VRAM tier | query anchor / metadata facet |
| model path | VRAM tier, CUDA family | query anchor / metadata facet |
| VRAM tier | CUDA family, workflow asset contract | query anchor / metadata facet |
| CUDA family | workflow asset contract, node class requirement | query anchor / metadata facet |
| workflow asset contract | node class requirement, license caveat | query anchor / metadata facet |
| node class requirement | license caveat, risk tier | query anchor / metadata facet |
| license caveat | risk tier, compatibility edge | query anchor / metadata facet |
| risk tier | compatibility edge, requirement node | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP05 — Python/Pip Runtime Dependencies and Local AI Environment Support
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP09 — Failure Signature Atlas RAG
