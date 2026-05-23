# Canonical Overview â€” Hardware Cost and Performance Planning

## Core Definition
Hardware Cost & Performance Planning is the discipline of matching AI workloads (training vs inference, latency vs throughput, model size) to the cheapest accelerator that meets SLAs while optimizing total cost of ownership, energy efficiency, and scalability.

## Metadata
Topic 25, v2.2, 2026-05-19, Sources: Google Cloud TPU 8 announcement (April 2026), MLPerf Inference 2026, Pinggy.io hardware guide, Mindcast AI TPU bifurcation analysis.

## Executive Summary Extract
## 1. Executive Summary & 2026 Landscape

2026 is the â€œInference Economy.â€ Training is a one-time or periodic cost; inference dominates ongoing spend for most organizations. The April 2026 Google TPU 8 bifurcation (separate 8t training and 8i inference chips) and the rise of SRAM-heavy inference chips (Groq, Cerebras, NVIDIA Blackwell) have fundamentally changed planning.

**Key 2026 Hardware Options**:
- **NVIDIA H200 / Blackwell B200 / DGX** â€” Best flexibility, ecosystem, lowest latency on complex/custom workloads. Highest absolute performance.
- **Google TPU 8t (Training)** â€” use official about 2.7Ã— training price/performance wording unless another official source is pinned.
- **Google TPU 8i (Inference)** â€” 80% better perf/$, 384 MB SRAM/chip for ultra-low latency agent serving. Designed for millions of concurrent agents.
- **AWS Inferentia2** â€” Excellent price/perf on AWS for compatible models.
- **AMD MI300** â€” Strong open alternative to NVIDIA.
- **Edge NPUs** (Apple Neural Engine, Qualcomm, NVIDIA Jetson) â€” For on-device models (Kokoro, quantized small VLMs).

**Core Metrics**:
- Performance per Dollar (most important for inference)
- Performance per Watt (energy = major ongoing cost)
- Latency p50/p95 vs Throughput
- Total Cost of Ownership (hardware + electricity + networking + software + opportunity cost)

---

## Core Concepts / Architecture Extract
## 2. Planning Framework (Step-by-Step)

1. **Profile the Workload**
   - % training vs inference (most orgs are 5-10% training, 90-95% inference)
   - Daily/peak token volume
   - Latency requirements (real-time agents <200ms vs batch < few seconds)
   - Model family & size (7B vs 70B vs 235B)
   - Multimodal? (vision/audio adds heavy compute)

2. **Run Benchmarks**
   - MLPerf Inference (latest 2026 results)
   - Vendor calculators + your own traces
   - Real A/B tests on target hardware

3. **Model Total Cost**
   - Hardware amortization
   - Electricity, cooling, lease/facility, and location costs (measure explicitly; do not assume a universal percentage)
   - Networking & storage
   - Software licensing / cloud markup
   - Opportunity cost of latency or downtime

4. **Choose Architecture**
   - NVIDIA: maximum flexibility, rapid iteration, complex models
   - TPU 8i: massive scale inference, agent fleets, best perf/$
   - Inferentia2: all-in on AWS, cost-sensitive inference
   - Edge NPUs: latency-critical or privacy-sensitive (voice agents, on-device VLMs)

5. **Design for Optimization**
   - Model routing (small model for 80% of traffic)
   - Quantization (int8, int4, AWQ, GPTQ)
   - Caching & speculative decoding
   - Batch sizing & continuous batching
   - Edge + cloud hybrid

---

## Best Practices / Patterns Extract
## 3. 2026 Cost Optimization Playbook

- **Route aggressively**: 7B/8B models for simple queries, 70B+ only when necessary.
- **Quantize everything possible**: int8 for most inference, int4 for edge.
- **Cache aggressively**: semantic cache hits can reduce cost 50-80%.
- **Measure and attribute**: cost per successful task, not per token.
- **Right-size clusters**: avoid over-provisioning; use serverless where possible.
- **Track energy**: kWh per 1M tokens is becoming a sustainability + cost metric.

---

## 4. Local AI Builder Profile (AIWF Audience)

The sections above describe enterprise inference economics. AIWF's actual audience is the local AI builder running a single workstation or a desktop + laptop pair. The decision logic is different and deserves its own profile.

### Hardware tiers we plan for

| Tier | VRAM | RAM | What runs cleanly | What needs quantization | What's out of scope |
|---|---|---|---|---|---|
| Entry laptop | 6â€“8 GB | 16â€“32 GB | SD 1.5, SDXL with offload, small LLMs (7B Q4) | Flux (NF4/GGUF Q4), 8B LLMs (Q5+) | Flux fp16, 13B+ LLMs at high quant, video models |
| Mid desktop | 12â€“16 GB | 32 GB | SDXL, Flux (Q8/Q6/NF4), 8B LLMs at higher quant, smaller video | Flux fp16, 13Bâ€“14B LLMs (Q4â€“Q6), WAN video at low res | 70B LLMs, multi-model concurrency |
| Higher desktop | 24 GB | 32â€“64 GB | Flux fp16, 13B LLMs at quality quant, WAN video at modest res | 70B LLMs (Q3â€“Q4), high-res video, training | Multi-GPU workloads, full-precision 70B+ |

All exact VRAM thresholds are **volatile** â€” model weights, attention implementations (FlashAttention, SageAttention), and offload schedulers change real-world VRAM use month to month. Recheck against the model card and a current ComfyUI benchmark before publishing as guidance.

### Cost levers for local builders (in order of effort vs. impact)

1. **Quantize the LLM.** A 7B model at Q4_K_M takes ~4â€“5 GB VRAM; the same model at fp16 is ~14 GB. Quality loss is small for most chat/instruction workloads. AWQ and GPTQ are competitive; GGUF (via llama.cpp/Ollama) is the most portable.
2. **Quantize the diffusion model.** Flux at NF4 or GGUF Q8 fits cleanly on 12 GB; Q4 variants fit on 8 GB with offload. Quality difference vs fp16 is visible but workflow-tolerable.
3. **Offload, don't refuse.** ComfyUI's model-offload settings, `--lowvram`/`--medvram`/`--novram`, and `enable_sequential_cpu_offload` in diffusers move idle weights to RAM. Slower, but lets a 16 GB card run jobs that would otherwise OOM.
4. **Match attention to hardware.** xformers, FlashAttention, SDPA, and SageAttention give different memory-time tradeoffs. SDPA (default in current PyTorch) is the safe baseline; xformers is the historical workhorse; SageAttention is the newer entrant. All version-volatile â€” recheck.
5. **Use the right resolution.** SDXL at 1024Ã—1024 is the design point. Going to 1536Â² doubles compute. Most "quality" wins from upscalers come after generation, not before.
6. **Batch only when you have headroom.** Batched generation amortizes overhead but multiplies VRAM. Single-image is the safe default on entry/mid tiers.

### Cloud GPU as a fallback (rent, don't buy first)

Renting an H100 or A100 by the hour beats a $4,000 upgrade for occasional large jobs. Current hourly rate orders of magnitude (volatile, recheck):

- **RunPod community/secure** â€” A100 80GB and H100 SXM at competitive hourly rates; supports persistent volumes and ComfyUI templates
- **Vast.ai** â€” variable price by host, often cheapest tier; less stable than RunPod
- **Lambda Labs / Paperspace / fal.ai** â€” managed inference endpoints for diffusion models specifically

Decision rule for AIWF: rent for the first three runs of a workflow before recommending a hardware upgrade. If the user runs the same workload daily, the math flips toward owning.

### The 7B laptop / 16GB desktop split (specific to this Atlas's primary author)

A common AIWF builder pattern is "smaller laptop + bigger desktop." Concrete distribution:

- **Laptop (7â€“8 GB VRAM)** â€” drafting, prompt iteration, small LLM (7B Q4) for chat, SD 1.5 quick passes, all writing/editing.
- **Desktop (16 GB VRAM)** â€” final renders, Flux jobs, 13Bâ€“14B LLMs at quality quant, WAN video, batch upscaling.
- **Shared via lakeFS or a network share** â€” workflow JSONs, LoRAs, prompt history. The laptop drafts; the desktop produces.

This split is genuinely cheaper than a single high-end machine for the AIWF use case because the laptop carries portability and the desktop carries compute â€” neither one has to compromise.

### What the local builder profile does NOT cover

- Multi-GPU training and pipeline parallelism (out of scope; route to RP18 MLOps lane)
- Datacenter cooling, PSU sizing, rack planning (out of scope for AIWF)
- Mac-specific tuning beyond "MPS works, expect 1.5â€“3x slower than CUDA on equivalent VRAM" (Vol. 2 â€” needs dedicated card)
- AMD ROCm (Vol. 2 â€” needs dedicated card; current state is "works for inference, training is rougher")

---
