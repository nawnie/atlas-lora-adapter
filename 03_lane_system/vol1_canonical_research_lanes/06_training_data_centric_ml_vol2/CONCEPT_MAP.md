# Concept Map — Training, Data-Centric ML, and Volume II Research Spine

## Primary concept chain

```text
user task -> lane classification -> concept card -> source/provenance check -> validation step -> answer/workflow/action
```

## Concepts and relationships

| Concept | Related concepts | Retrieval role |
|---|---|---|
| data-centric ML | dataset split, leakage | query anchor / metadata facet |
| dataset split | leakage, label quality | query anchor / metadata facet |
| leakage | label quality, objective function | query anchor / metadata facet |
| label quality | objective function, evaluation set | query anchor / metadata facet |
| objective function | evaluation set, adapter training | query anchor / metadata facet |
| evaluation set | adapter training, LoRA rank | query anchor / metadata facet |
| adapter training | LoRA rank, overfitting | query anchor / metadata facet |
| LoRA rank | overfitting, release ethics | query anchor / metadata facet |
| overfitting | release ethics, data-centric ML | query anchor / metadata facet |
| release ethics | data-centric ML, dataset split | query anchor / metadata facet |

## Cross-lane links

- No direct same-source link; connect through global RAG index.
