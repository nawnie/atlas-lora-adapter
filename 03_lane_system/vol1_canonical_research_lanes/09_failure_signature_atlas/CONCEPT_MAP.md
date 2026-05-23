# Concept Map — Failure Signature Atlas RAG

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| symptom | log fragment, likely layer | query anchor / metadata facet |
| log fragment | likely layer, confidence | query anchor / metadata facet |
| likely layer | confidence, first safe test | query anchor / metadata facet |
| confidence | first safe test, recovery ladder | query anchor / metadata facet |
| first safe test | recovery ladder, do-not-do step | query anchor / metadata facet |
| recovery ladder | do-not-do step, escalation artifact | query anchor / metadata facet |
| do-not-do step | escalation artifact, support report | query anchor / metadata facet |
| escalation artifact | support report, symptom | query anchor / metadata facet |
| support report | symptom, log fragment | query anchor / metadata facet |

## Cross-lane links

- RP01 — Source Ledger and Evidence Governance
- RP02 — RAG Architecture, Chunking, and Embedding Strategy
- RP03 — ComfyUI Core API, Workflow JSON, and Subgraph Research
- RP04 — ComfyUI Custom Node Ecosystem and Nodepack Evaluation
- RP05 — Python/Pip Runtime Dependencies and Local AI Environment Support
- RP07 — CFG, Denoise, Img2Img, and Inpainting Theory
