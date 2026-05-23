# Concept Map — ComfyUI Core API, Workflow JSON, and Subgraph Research

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| object_info | class_type, input socket | query anchor / metadata facet |
| class_type | input socket, output socket | query anchor / metadata facet |
| input socket | output socket, links array | query anchor / metadata facet |
| output socket | links array, node widgets_values | query anchor / metadata facet |
| links array | node widgets_values, subgraph | query anchor / metadata facet |
| node widgets_values | subgraph, partial execution | query anchor / metadata facet |
| subgraph | partial execution, schema capture | query anchor / metadata facet |
| partial execution | schema capture, workflow manifest | query anchor / metadata facet |
| schema capture | workflow manifest, object_info | query anchor / metadata facet |
| workflow manifest | object_info, class_type | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
- RP09 — Failure Signature Atlas RAG
- RP10 — Workflow Pattern Library RAG
