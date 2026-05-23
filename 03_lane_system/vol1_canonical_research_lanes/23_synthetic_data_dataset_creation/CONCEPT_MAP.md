# Concept Map — Synthetic Data and Dataset Creation

## Core Facts
- Treat synthetic data generators as versioned artifacts; do not assume a universal synthetic-data percentage without source verification.
- The 5-step pipeline (chunk → context → query → evolution → label + verify) is the industry standard.
- Rigorous curation (dedup + LLM judge + bias audit) is non-negotiable — raw synthetic output is toxic.
- Always mix real data with curated synthetic data; tune the ratio by downstream task lift, diversity, hallucination rate, and model-collapse risk.
- RAG-grounded generation + execution feedback dramatically reduces hallucinations.
- Version synthetic generators + prompts + seed data together for full reproducibility.
- Downstream task performance (not surface quality) is the only true success metric.
- Synthetic data excels at rare edge cases, red-teaming, and instruction diversity.
- Governance (provenance, consent, watermarking) is required for any production synthetic corpus.
- Continuous monitoring + periodic real-data refresh prevents silent degradation.

## Decision Framework
- Instruction tuning / alignment → 5-step pipeline + DeepEval + heavy curation
- Code / math / tool-use → Execution feedback loops (run tests, verify answers)
- Rare edge cases / long-tail → Targeted synthetic generation from failure logs
- Privacy-sensitive domains → Fully synthetic with strong differential privacy + watermarking
- Maximum diversity → Multi-agent debate + data evolution

## Cross-Topic Hooks
- Topic 20: Version synthetic generators exactly like any other data product; apply data contracts.
- Topic 21/22: Generate synthetic audio, images, documents to augment real datasets.
- Topic 24: Synthetic trajectories are essential for training reliable agents.
- Topic 25: Synthetic data generation has non-trivial compute cost — track and optimize.

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 20_data_engineering_for_ai
- 25_hardware_cost_performance_planning
