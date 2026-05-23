# Concept Map — AI Application Architecture

## Core Facts
- Start with simple RAG; add agentic complexity only when metrics prove it necessary.
- Instrument every component (tokens, latency, retrieval quality, cost, user satisfaction) from day 1.
- Model routing + caching + small-model preference is the dominant cost-control pattern.
- Full tracing (LangSmith/Phoenix) + offline + online evals is non-negotiable for production.
- Feedback loops (user thumbs, agent trajectories, failure logs) are the fuel for continuous improvement.
- Synthetic data (Topic 23) closes the loop: failures → synthetic regeneration → retraining.
- Multimodal (vision + audio + text) is now the default for most new applications.
- Cost observability must be tied to business value (cost per successful task, not just per token).
- Edge + cloud hybrid deployment is standard for latency-sensitive agents.
- Governance (safety, PII, audit logs) must be designed into the architecture, not bolted on.

## Decision Framework
- Simple Q&A / RAG over documents → Basic RAG + hybrid retrieval + re-ranking
- Complex workflows with tools → LangGraph + ReAct / Plan-and-Execute
- Multi-agent collaboration → CrewAI / AutoGen with clear role definitions
- Voice-first natural conversation → Full-duplex (Topic 21) + lightweight orchestration
- Document-heavy enterprise → Hierarchical document agents (Topic 22) + citations

## Cross-Topic Hooks
- Topic 20: The data layer (lakehouse + feature store) is the foundation of every AI app.
- Topic 21/22: Multimodal input/output is now standard — design for it.
- Topic 23: Synthetic data flywheels are the most powerful continuous improvement mechanism.
- Topic 25: Architecture decisions directly determine inference cost — route intelligently.

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 20_data_engineering_for_ai
- 25_hardware_cost_performance_planning
