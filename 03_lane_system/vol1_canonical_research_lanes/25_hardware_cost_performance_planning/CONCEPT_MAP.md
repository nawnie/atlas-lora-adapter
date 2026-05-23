# Concept Map — Hardware Cost and Performance Planning

## Core Facts
- 2026 is the Inference Economy — inference dominates TCO for almost every organization.
- Google TPU 8i (April 2026) delivers 80% better perf/$ than prior generation for agent-scale inference.
- NVIDIA Blackwell + H200 remains the flexibility king for complex/custom workloads.
- Performance per Dollar and Performance per Watt are the two most important metrics for inference planning.
- Model routing + quantization + caching can reduce inference cost 50-80% with minimal quality loss.
- Edge NPUs (Kokoro, quantized VLMs) are mandatory for <100ms real-time agents.
- Power, cooling, facility/lease, and location costs can dominate operating expense; measure kWh per workload and full facility cost instead of assuming a universal percentage.
- TPU 8i’s 384 MB SRAM per chip is specifically designed for millions of concurrent low-latency agents.
- Right-sizing + hybrid edge/cloud is more important than choosing the single “fastest” chip.
- Cost observability must be tied to business outcomes (cost per successful task).

## Decision Framework
- Maximum flexibility + complex models → NVIDIA H200/Blackwell
- Massive scale low-latency agent inference → Google TPU 8i
- All-in on AWS + cost-sensitive → Inferentia2
- <100ms real-time / on-device → Edge NPUs (Kokoro, Jetson, Apple Neural Engine)
- Balanced open ecosystem → AMD MI300

## Cross-Topic Hooks
- Topic 20: Measure and attribute embedding generation cost to specific feature views.
- Topic 21: Edge inference (Kokoro) is mandatory for natural voice agents.
- Topic 22: Large VLMs (235B) have high inference cost — route to smaller models when possible.
- Topic 24: Architecture decisions (routing, caching, edge) directly determine hardware cost.

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 20_data_engineering_for_ai
