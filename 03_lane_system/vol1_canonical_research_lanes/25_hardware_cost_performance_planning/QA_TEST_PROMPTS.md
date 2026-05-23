# QA Test Prompts — Hardware Cost and Performance Planning

Use these prompts to test retrieval and answer quality for this lane. Volatile-fact prompts are tagged with `[V]`.

## Enterprise / cloud prompts

1. Explain the "Inference Economy" framing and why it matters for hardware decisions in 2026.
2. A team is choosing between NVIDIA Blackwell and Google TPU 8i for an agent-serving workload at scale. What questions should they answer before picking?
3. What is the AIWF-recommended top-3 cost-optimization playbook for inference at scale?
4. `[V]` What is the perf/$ delta between TPU 8t (training) and TPU 8i (inference)? Mark as `volatile_needs_recheck`.

## Local AI builder prompts (AIWF audience)

5. A user has an RTX 4060 Ti 16GB and 32GB system RAM. They want to run Flux Dev locally. Walk through the realistic options.
6. A user is on a laptop with 7GB VRAM and 32GB RAM (DDR5). They want to run a 13B LLM and use SDXL. Is that feasible? At what quants and tradeoffs?
7. A user has a 16GB desktop and a 7GB laptop. How should they split workloads to get the most out of both?
8. Define the three tiers (entry / mid / higher) and give one model that runs cleanly in each tier and one that doesn't.
9. `[V]` What quantization fits Flux Dev on 8GB VRAM? Mark volatile; point to the model card and ComfyUI benchmarks.
10. `[V]` What's the typical VRAM for a 7B LLM at Q4_K_M? Mark volatile; point to llama.cpp tables.

## Cost / cloud prompts

11. A user spends 6 hours a week generating Flux images on a slow card and is considering a $4,000 GPU upgrade. What does the AIWF rent-vs-buy decision rule say?
12. `[V]` What's the current approximate hourly rate for an A100 80GB on RunPod community? Mark volatile; point to runpod.io/pricing with capture date.

## Conceptual / decision prompts

13. Order the cost levers (quantize, offload, attention impl, resolution, batching) by effort vs. impact and justify the order.
14. What is "offload, don't refuse" and what ComfyUI flags implement it?
15. Why is "rent first, then buy" the AIWF default? What changes the math toward owning?

## Anti-pattern prompts

16. A user wants to buy the latest 4090 because "more VRAM is always better." What questions should they answer first?
17. A user is comparing two cards based purely on TFLOPS marketing numbers. What is the AIWF-correct frame for this comparison?
18. A user says "my SDXL is slow, I'll just upgrade." What's the diagnostic order before recommending hardware spend?

## Pass criteria

A response passes if:

- it distinguishes the enterprise frame from the local builder frame and answers from the correct one
- volatile claims are marked, not quoted as fact
- the cost lever order matches §3 / §4 of `CANONICAL_OVERVIEW.md`
- diagnostic questions come before hardware-spend recommendations
- cloud-vs-local recommendations cite the three-run threshold rule, not a vibes-based one
