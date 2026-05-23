# Canonical Overview — Audio, Speech, and Music AI

## Core Definition
Audio/Speech/Music AI encompasses ASR, TTS, music generation, and full-duplex voice agents, with 2026 emphasis on end-to-end models that preserve prosody and enable natural multi-turn interaction without text transcription.

## Metadata
Topic 21, v2.2, 2026-05-19, Sources: SiliconFlow 2026 benchmarks, fishaudio GitHub, Qwen3-TTS technical report, NVIDIA PersonaPlex Jan 2026 announcement, NeurIPS 2025 AI for Music Workshop.

## Executive Summary Extract
## 1. Executive Summary & 2026 State of the Art

Audio AI in 2026 is defined by three breakthroughs:
1. **End-to-End / Full-Duplex Speech LLMs** (NVIDIA PersonaPlex, Moshi derivatives, Qwen2-Audio) that eliminate the STT → LLM → TTS cascade for natural conversation.
2. **Ultra-light edge models** (Kokoro-82M, CosyVoice2-0.5B) running on-device with <100ms latency.
3. **High-fidelity open-source TTS** (Fish Speech S2, Qwen3-TTS 1.7B) matching or beating closed models on multilingual prosody and zero-shot cloning.

**Key Data Engineering Implication**: Audio datasets are now first-class multimodal citizens. Your lakehouse must handle raw waveforms, spectrograms, tokenized audio (7.5-12Hz codecs), speaker embeddings, and long-form transcripts with equal versioning and quality guarantees.

---

## Core Concepts / Architecture Extract
## 2. Core Concepts & Taxonomy

**Speech-to-Text (ASR)**: Whisper-large-v3, Canary, Parakeet, Qwen2-Audio — 2026 focus is long-context (>30min) and code-switching.
**Text-to-Speech (TTS)**:
- Autoregressive: Fish Speech, CosyVoice, Tortoise (legacy)
- Non-autoregressive / Fast: Kokoro, VITS, StyleTTS2
- 2026 Leader: Qwen3-TTS (instructable, zero-shot from 3-30s reference, excellent prosody)
**Music Generation**: Suno v4, Udio, Minimax Music-2, Stable Audio 2.5, MusicGen (open). Text-to-music + stem separation + controllable editing.
**Audio Understanding**: Qwen2-Audio, Gemini-2.5 Audio, Audio Flamingo — captioning, event detection, music tagging, speaker diarization.

**Full-Duplex Voice Agents**: The killer app of 2026. Models that listen and speak simultaneously, handle interruptions, backchannels ("uh-huh", laughter), and maintain context across turns without text transcription bottleneck.

---

## Best Practices / Patterns Extract
## 5. 2026 Best Practices & Data Scientist Playbook

1. **Reference Audio Management** (Zero-shot cloning is table stakes)
   - Store 5-30s clean reference per speaker with consent metadata
   - Version references separately from generated audio
   - Use speaker verification to prevent cloning abuse

2. **Long-Context Audio Handling**
   - VibeVoice-style 7.5Hz tokenization for 30-90 min context
   - Chunking strategy: 30s semantic chunks + overlap for continuity

3. **Edge + Cloud Hybrid**
   - Kokoro-82M or quantized Qwen3-TTS-0.6B on-device for wake-word + routing
   - Cloud full model for complex responses

4. **Environmental Robustness**
   - Train with real-world noise (cafes, cars, wind) — do not rely on clean studio data
   - Add dereverberation and denoising as optional preprocessing stages

5. **Evaluation Beyond WER**
   - Speaker similarity (cosine on embeddings)
   - Prosody naturalness (human MOS or proxy models)
   - Turn-taking quality (interruption success rate, backchannel appropriateness)
   - Audio Turing Test (human vs generated in blind A/B)

---
