# Canonical Overview — LLM Fundamentals

LLM fundamentals is the base layer for every assistant using the adapter. The assistant must know the difference between model knowledge, retrieved context, tool output, chat template formatting, and decoding behavior. A retrieval-augmented small model should be treated as a reasoning engine plus external memory, not as a memorized encyclopedia. Transformer attention is stable foundational knowledge; model-family rankings and context-window limits are volatile and must be tagged as fast-moving.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- tokens
- embeddings
- attention
- transformer block
- context window
- KV cache
- logits
- temperature
- top-p
- top-k
- system prompt
- chat template
- instruction tuning
- preference tuning
- quantization
- GGUF
- small-model routing

## Source-backed anchors
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- Hugging Face platform and model ecosystem: https://huggingface.co/
- scikit-learn ML foundations: https://scikit-learn.org/
- Stanford CS229 course description: https://cs229.stanford.edu/

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
