# Concept Map — Audio, Speech, and Music AI

## Core Facts
- Qwen3-TTS (0.6B-1.7B) leads open-source zero-shot cloning + instructable style control in 2026.
- Fish Speech S2 excels at multilingual expressive TTS and code-switching.
- Kokoro-82M is the go-to for on-device <100ms latency.
- Full-duplex (PersonaPlex-style) is required for natural agent conversation; cascade is transitional.
- Audio tokenization at 7.5-12Hz enables 30-90min context in models like VibeVoice.
- Reference audio (3-30s clean) + speaker verification is mandatory for production cloning.
- Environmental noise simulation during training is non-negotiable for real-world robustness.
- Version raw audio + codec config + embedding model together (Topic 20 integration).
- Evaluation must include prosody, turn-taking, and human preference — WER is insufficient.
- Edge models (Kokoro) + cloud full models is the dominant 2026 deployment pattern.

## Decision Framework
- Real-time consumer voice agent → Full-duplex (PersonaPlex/Moshi-2) or Kokoro edge
- Enterprise with heavy tools/RAG → Cascade (Qwen2-Audio STT + LLM + Qwen3-TTS)
- Multilingual expressive TTS → Fish Speech S2 or Qwen3-TTS
- On-device/low-power → Kokoro-82M or quantized 0.6B variants
- Music generation → Suno/Udio (commercial) or MusicGen + stem separation (open)

## Cross-Topic Hooks
- Topic 20: Apply lakeFS + DVC + quality gates to voice reference datasets and generated corpora.
- Topic 22: Multimodal agents can combine vision + audio (Qwen2.5-Omni style).
- Topic 23: Synthetic audio/voice data must be versioned with generator configs.
- Topic 24: Voice agents are a core multimodal application pattern.
- Topic 25: Edge inference (Kokoro) dramatically reduces cost vs cloud cascade.

## Related Adapter Lanes
- 02_atlas_architecture_chunking_embedding
- 09_failure_signature_atlas
- 24_ai_application_architecture
- 20_data_engineering_for_ai
- 25_hardware_cost_performance_planning
