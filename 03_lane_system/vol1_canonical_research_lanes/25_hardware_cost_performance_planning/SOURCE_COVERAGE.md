# Source Coverage — Hardware Cost and Performance Planning

## Primary integrated source

- `03_SOURCE_CONTENT/topics_20_25_expanded_notes/25_Hardware_Cost_Performance_Planning_Expanded_Notes.md`

## Source type

User-provided expanded notes for AIWF Atlas Topic 25, augmented in v3.3 with a local-AI-builder profile section drawn from AIWF practitioner experience on 7–16 GB VRAM consumer hardware.

## Citation / provenance policy

Treat the enterprise-tier content (TPU 8, Blackwell, Inferentia2, MLPerf figures) as a synthesized research note until each referenced external source is independently validated in a source-ledger refresh pass.

Treat the local-AI-builder content as practitioner synthesis: directionally correct on patterns (quantization, offload, attention impls, rent-vs-buy), but **all specific VRAM numbers, model versions, and pricing claims are `volatile_needs_recheck`** per `00_AI_READ_FIRST/ANTI_AI_SLOP_RESEARCH_POLICY.md`.

## Sources to consult during refresh pass

### Enterprise tier

- Google Cloud TPU 8 announcement and pricing pages
- MLPerf Inference results (mlcommons.org/benchmarks/inference)
- NVIDIA Blackwell technical brief
- AWS Inferentia2 pricing and performance docs
- AMD Instinct MI300 documentation
- Vendor calculators (NVIDIA, GCP, AWS) for sanity-checking perf/$ claims

### Local-builder tier

- Model cards on HuggingFace (Flux, WAN, SDXL, Llama family, Qwen family) for fp16/quantized VRAM
- ComfyUI README and CLI args for current `--lowvram`/`--medvram`/`--novram` behavior
- llama.cpp / Ollama model library for quantized LLM sizes
- PyTorch release notes for SDPA / attention defaults
- xformers, FlashAttention, SageAttention release pages
- bitsandbytes README for current Windows/Linux status
- RunPod, Vast.ai, Lambda Labs, fal.ai pricing pages (capture date with quote)

### Community benchmark sources (use with care)

- r/StableDiffusion benchmark threads (methodology varies; cite, don't trust uncritically)
- ComfyUI Discord pinned benchmark posts
- Civitai workflow benchmarks (often biased toward specific quants/optimizers)

## Refresh discipline

When a claim in this lane is restated for public release:

1. Identify whether the claim is enterprise-tier or local-tier.
2. Find at least one primary source (vendor doc, model card, or release notes) — not just a forum post.
3. Capture the date of the source check; if older than 90 days, recheck before publishing.
4. Update the `freshness_class` field in this lane's `lane_profile.json` if the claim's class shifts (e.g. stable → volatile).
