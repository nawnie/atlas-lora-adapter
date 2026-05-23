# Canonical Overview — AI Application Architecture

## Core Definition
AI Application Architecture is the discipline of designing distributed systems that combine retrieval, agents, memory, tools, evaluation, and continuous improvement while meeting latency, cost, reliability, and safety requirements.

## Metadata
Topic 24, v2.2, 2026-05-19, Sources: SystemDesignHandbook 2026 AI Architecture Guide, LangGraph/CrewAI production patterns, LangSmith/Phoenix observability reports.

## Executive Summary Extract
## 1. Executive Summary & 2026 Reality

AI application architecture has moved far beyond “call an LLM API.” Modern systems are complex distributed platforms that combine retrieval, memory, tools, agents, evaluation loops, multimodal flows, and continuous improvement — all while meeting strict latency, cost, and reliability SLAs.

**Core 2026 Patterns**:
- Simple RAG (still 60%+ of production systems)
- Agentic RAG (retrieval as a tool, dynamic planning)
- Multi-Agent Systems (specialized agents + orchestrator)
- Full-Duplex Voice Agents (Topic 21)
- Document-Centric Agents (Topic 22)
- Self-Improving Systems (synthetic data flywheels — Topic 23)

---

## Core Concepts / Architecture Extract
## 2. Core Architectural Components

**Ingestion & Indexing Layer** (Topic 20 foundation)
- Multimodal lakehouse (Lance + lakeFS)
- Embedding generation (Ray + Qwen2.5-VL / text-embedding-3-large)
- Chunking strategies (fixed, semantic, hierarchical, agentic)

**Retrieval Layer**
- Hybrid search (vector + keyword + metadata)
- Re-ranking (Cohere, bge-reranker, LLM reranker)
- Query rewriting / expansion / decomposition
- Agentic retrieval (LLM decides what to retrieve and how)

**Orchestration & Agent Layer**
- LangGraph, CrewAI, AutoGen, Semantic Kernel, custom state machines
- Tool calling (structured outputs + validation)
- Memory (short-term, long-term, entity memory)
- Planning (ReAct, Plan-and-Execute, Reflexion, Tree-of-Thoughts)

**LLM / VLM Gateway**
- Model routing (small model for simple queries, frontier for hard)
- Caching (semantic + exact), fallback, rate limiting
- Cost tracking per request / per user / per feature

**Evaluation & Observability**
- Offline evals (RAGAS, ARES, custom LLM judges)
- Online evals (A/B testing, shadow traffic, user feedback)
- Drift detection (data, embedding, performance)
- Full tracing (LangSmith, Phoenix, Helicone, custom)

**Serving & Scaling**
- Async queues, batching, speculative decoding
- Edge deployment (Topic 25)
- Model distillation & quantization

---

## Best Practices / Patterns Extract
## 3. Best Practices & Anti-Patterns

**Best Practices**:
- Start simple (RAG) → measure → add complexity only when metrics demand it.
- Instrument everything from day 1 (tokens, latency p95, retrieval precision, user satisfaction, cost).
- Use feature flags for model versions and retrieval strategies.
- Design for continuous improvement (feedback → synthetic data → retraining).
- Cost-first design: route 80% of traffic to small models, reserve frontier models for hard cases.

**Anti-Patterns**:
- “LLM as a monolith” — one giant prompt that tries to do everything.
- No observability — flying blind in production.
- Ignoring cost until the bill arrives.
- Over-engineering before validating the simple version.

---
