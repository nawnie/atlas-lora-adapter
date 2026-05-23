# Concept Map — Model Serving and Deployment

## Core nodes
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

## Relationships
- This lane supports AIWF's machine-facing adapter behavior.
- It should be connected to `24_ai_application_architecture` when the user asks how to build an application.
- It should be connected to `14_evaluation_observability` when the user asks how to prove quality.
- It should be connected to `15_safety_security_red_team` when the answer involves tools, files, users, deployments, or untrusted inputs.

## Retrieval hints
- Search exact technical terms first.
- Use semantic retrieval for architecture and decision questions.
- Use source metadata to separate current implementation facts from durable concepts.
