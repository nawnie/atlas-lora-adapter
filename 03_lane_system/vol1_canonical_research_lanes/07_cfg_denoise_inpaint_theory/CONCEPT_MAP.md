# Concept Map — CFG, Denoise, Img2Img, and Inpainting Theory

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| CFG | denoise, latent noise | query anchor / metadata facet |
| denoise | latent noise, mask boundary | query anchor / metadata facet |
| latent noise | mask boundary, context crop | query anchor / metadata facet |
| mask boundary | context crop, stitch blend | query anchor / metadata facet |
| context crop | stitch blend, inpaint conditioning | query anchor / metadata facet |
| stitch blend | inpaint conditioning, LaMa/MAT prefill | query anchor / metadata facet |
| inpaint conditioning | LaMa/MAT prefill, Fooocus inpaint patch | query anchor / metadata facet |
| LaMa/MAT prefill | Fooocus inpaint patch, seam control | query anchor / metadata facet |
| Fooocus inpaint patch | seam control, CFG | query anchor / metadata facet |
| seam control | CFG, denoise | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP08 — Compatibility Matrix RAG
- RP09 — Failure Signature Atlas RAG
