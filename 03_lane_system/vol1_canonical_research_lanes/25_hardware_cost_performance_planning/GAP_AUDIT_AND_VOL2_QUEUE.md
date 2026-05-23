# Gap Audit and Vol. 2 Queue — Hardware Cost and Performance Planning

## Vol. 1 baseline now present

- 2026 enterprise landscape (Inference Economy, TPU 8 bifurcation, Blackwell, Inferentia2, MI300, edge NPUs).
- Local AI builder profile with three-tier VRAM table (entry / mid / higher).
- Cost levers ordered by effort-vs-impact (quantize, offload, attention impl, resolution, batching).
- Cloud-GPU fallback decision rule (rent before buy, three-run threshold).
- Laptop + desktop split pattern with concrete role distribution.
- Cross-topic hooks to RP05 (pip/runtime), RP08 (compatibility), RP18 (MLOps), RP20 (data eng), RP24 (app architecture).

## Remaining Vol. 1 gaps

- **Per-model VRAM table** with actual measured VRAM for: SD 1.5, SDXL, Flux Dev fp16/Q8/Q4/NF4, WAN 2.1/2.2, common LLMs 7B/8B/13B/14B at Q3/Q4/Q5/Q6/Q8. Measurements should come from ComfyUI startup logs or `nvidia-smi` during generation, not from model-card claims (which understate).
- **Attention-implementation comparison card** — SDPA vs xformers vs FlashAttention 2 vs SageAttention, with the memory-time tradeoff matrix.
- **Quantization quality-loss notes** — what users actually notice at NF4 vs Q4 vs Q6 vs Q8 for diffusion; what they notice at Q3_K_S vs Q4_K_M vs Q5_K_M for LLM chat.
- **Apple Silicon (MPS) addendum** — practical guidance for M-series users; MPS works but with caveats around fp16 stability and which ops fall back to CPU.
- **AMD ROCm addendum** — current state of consumer Radeon support; what works (most inference) and what doesn't (some attention impls, some training paths).
- **Power budget notes** — RTX 4090 vs 4080 vs 4070 Ti vs 4060 Ti 16GB at the wall under sustained generation; useful for users sizing PSU and worrying about summer ambient temps.

## Vol. 2 queue (research targets)

- Source-backed refresh pass: validate every 2026 model/vendor/hardware claim against current primary sources (vendor docs, MLPerf, model cards).
- Add reproducible benchmark recipes: one ComfyUI workflow + one llama.cpp prompt + a measurement script, so claims can be re-tested rather than re-quoted.
- Add real cloud-GPU pricing snapshots with capture date; treat as `volatile_needs_recheck` and refresh quarterly.
- Add failure signatures specific to this lane (OOM patterns by model, thermal throttling, PSU sag under sustained load) and cross-link to RP09.
- Build an "upgrade decision worksheet" — given current hardware + budget + workload, what's the next dollar best spent on (more VRAM, more RAM, NVMe for model storage, cloud burst).
- Capture community benchmark threads (r/StableDiffusion, ComfyUI Discord) as reference evidence; tag carefully because community benchmarks vary in methodology quality.

## Verification queue (volatile claims to web-check)

| Claim | Where used | Source to check |
|---|---|---|
| TPU 8 perf/$ figures | CANONICAL_OVERVIEW §1 | Google Cloud official announcement page |
| MLPerf Inference 2026 results | CANONICAL_OVERVIEW §2 | mlcommons.org/benchmarks/inference |
| RunPod / Vast.ai hourly pricing | CANONICAL_OVERVIEW §4 (cloud fallback) | runpod.io/pricing, vast.ai (capture date) |
| Flux dev/Schnell VRAM at fp16/Q8/Q4/NF4 | Local Builder tier table | Flux model card on HuggingFace + ComfyUI logs |
| WAN model VRAM and resolution thresholds | Local Builder tier table | WAN release notes, ComfyUI workflow benchmarks |
| LLM 7B quant VRAM (Q4_K_M ≈ 4–5 GB) | Cost levers §1 | llama.cpp model size tables, Ollama model library |
| Current attention-impl recommendations (SDPA default, xformers/SageAttention) | Cost levers §4 | PyTorch release notes, xformers releases |
| ComfyUI `--lowvram`/`--medvram`/`--novram` current behavior | Cost levers §3 | ComfyUI CLI args docs (in code/README) |

All claims above are tagged `volatile_needs_recheck` per `00_AI_READ_FIRST/ANTI_AI_SLOP_RESEARCH_POLICY.md`. Do not publish as canonical until verified.
