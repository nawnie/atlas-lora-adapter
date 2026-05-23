# Canonical Overview — Model Serving and Deployment

Model serving turns a model file into a usable system. The assistant should know the difference between beginner local serving with Ollama, lightweight GGUF serving with llama.cpp, high-throughput deployment with vLLM/TGI, and app-layer wrappers like Gradio or FastAPI. Deployment guidance must include security: do not expose local model/tool servers to the internet without authentication and network controls.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- Ollama
- llama.cpp
- GGUF
- vLLM
- PagedAttention
- continuous batching
- prefix caching
- TGI
- OpenAI-compatible API
- FastAPI
- Docker
- port binding
- reverse proxy
- model routing
- fallback model

## Source-backed anchors
- vLLM documentation: https://docs.vllm.ai/en/latest/
- llama.cpp HTTP server README: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
- llama-cpp-python OpenAI compatible server: https://llama-cpp-python.readthedocs.io/en/latest/server/
- Ollama: https://ollama.com/
- Hugging Face Text Generation Inference: https://huggingface.co/docs/text-generation-inference/index

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
