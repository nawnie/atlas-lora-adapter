# Concept Map — Vision-Language, OCR, and Document AI

## Core Facts
- Qwen3-VL-235B-A22B and DeepSeek-VL2/DeepSeek-OCR are verified document-AI anchors; DeepSeek active-parameter claims must be tied to the exact variant.
- Always version raw images + JSON + embeddings together in Lance + lakeFS.
- Agentic OCR (LlamaParse) with citations + confidence is mandatory for enterprise RAG.
- Long documents require hierarchical chunking (page → section → table) + multi-vector retrieval.
- Table/chart understanding is the hardest sub-task — DeepSeek-OCR excels here via Contexts Optical Compression.
- Confidence + LLM validator loops catch 80%+ of extraction errors before they reach downstream agents.
- Scan quality metadata (DPI, noise, skew) is critical for drift detection.
- Synthetic document generation (Topic 23) is the fastest way to improve rare layouts/handwriting.
- Cross-modal retrieval (image + text + table embeddings) dramatically outperforms text-only RAG on documents.
- Governance (consent, PII redaction, provenance) is now required for any production document corpus.

## Decision Framework
- Maximum quality + multilingual → Qwen3-VL-235B
- Efficiency + table-heavy workloads → DeepSeek-VL2 / DeepSeek-OCR
- Agentic enterprise RAG with citations → LlamaParse + Llama-3.2-Vision
- Long legal/financial contracts → Hierarchical chunking + multi-vector retrieval
- Noisy real-world scans → VLM + confidence + LLM validator loop

## Cross-Topic Hooks
- Topic 20: Version document images + annotations + embeddings exactly like any other multimodal dataset.
- Topic 21: Multimodal agents can fuse vision + audio context.
- Topic 23: Use synthetic document generation to fill rare layout gaps.
- Topic 24: Document AI is a core pattern in almost every enterprise AI application architecture.
- Topic 25: VLM inference cost (especially 235B) must be tracked and optimized (quantization, caching, routing to smaller models).

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 20_data_engineering_for_ai
- 25_hardware_cost_performance_planning
