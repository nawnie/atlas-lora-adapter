# Canonical Overview — Math for AI Practitioners

AIWF math should be operational: enough to debug, choose settings, understand RAG similarity, interpret evaluation metrics, and reason about training behavior. The assistant should translate math into tool behavior: cosine similarity explains retrieval ranking, entropy relates to uncertainty, cross-entropy relates to language-model training, and gradients explain why data quality matters.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- vector
- matrix
- embedding
- dot product
- cosine similarity
- probability
- softmax
- entropy
- cross entropy
- loss function
- gradient descent
- normalization
- precision
- recall
- F1
- ROC-AUC
- RMSE
- bias variance

## Source-backed anchors
- Stanford CS229 course: https://cs229.stanford.edu/
- Stanford CS229 notes: https://cs229.stanford.edu/main_notes.pdf
- scikit-learn metrics and ML docs: https://scikit-learn.org/
- Attention Is All You Need: https://arxiv.org/abs/1706.03762

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
