# Concept Map — Data Engineering for AI

## Core Facts
- The 2026 AI data stack is PARK + Lance + lakeFS + Feast/Tecton.
- Synthetic data should be treated as a first-class, versioned data artifact; exact real/synthetic ratios must be validated by downstream evaluation.
- Point-in-time correctness is non-negotiable for any time-sensitive feature.
- Embedding columns must carry model version, hyperparameters, and generation timestamp as metadata.
- lakeFS branching + DVC experiments = the only safe way to run AI data experiments at scale.
- Data contracts + LLM validators catch 80%+ of production data issues before they reach training.
- Cost per embedding generated is now a first-class metric alongside latency and accuracy.
- Multimodal lakehouses (Lance) eliminate the need for separate vector DBs for most workloads.
- Agent-native patterns require ephemeral scratch spaces + versioned context stores.
- Governance (provenance, consent, bias) is now a hard requirement for any model that will be deployed to users.

## Decision Framework
- If you need Git-like experimentation on petabyte-scale data → lakeFS + DVC
- If you need <50ms feature serving for agents → Feast/Tecton online store + Redis/Cassandra
- If you have heavy multimodal data (images + video + embeddings) → Lance + lakeFS
- If you want maximum openness and flexibility → Feast + Ray + DuckDB + Lance
- If you are deep in one cloud → use that cloud's native feature store + lakehouse

## Cross-Topic Hooks
- Topic 21 (Audio/Speech/Music): Use same versioning + quality gates for voice reference datasets and generated audio corpora.
- Topic 22 (Vision/Document): Version image datasets + OCR annotations + VLM embeddings together.
- Topic 23 (Synthetic Data): Synthetic generators must be versioned alongside the data they produce; apply identical contracts.
- Topic 24 (Architecture): This topic is the data foundation layer — every AI application architecture diagram must include the feature store and lakehouse.
- Topic 25 (Hardware): Measure and attribute embedding generation cost to specific feature views; optimize for perf/$.

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 25_hardware_cost_performance_planning
