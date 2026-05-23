# Concept Map — Workflow Pattern Library RAG

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| pattern card | input contract, processing stage | query anchor / metadata facet |
| input contract | processing stage, output selector | query anchor / metadata facet |
| processing stage | output selector, router shell | query anchor / metadata facet |
| output selector | router shell, subgraph | query anchor / metadata facet |
| router shell | subgraph, node requirement | query anchor / metadata facet |
| subgraph | node requirement, asset requirement | query anchor / metadata facet |
| node requirement | asset requirement, smoke test | query anchor / metadata facet |
| asset requirement | smoke test, beginner control panel | query anchor / metadata facet |
| smoke test | beginner control panel, pattern card | query anchor / metadata facet |
| beginner control panel | pattern card, input contract | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP08 — Compatibility Matrix RAG
