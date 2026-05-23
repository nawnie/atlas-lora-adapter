# Gap Audit and Vol. 2 Queue — Python/Pip Runtime Dependencies and Local AI Environment Support

## Vol. 1 baseline now present

- Cluster taxonomy explicit (9 clusters) with member packages and owned failure types.
- Top-five failure flows documented with diagnostic chains.
- Decision postures (use/wrap/document/build) named.
- Stable vs volatile knowledge split.
- Cross-lane links to RP08 (compatibility), RP09 (failure signatures), RP25 (hardware), RP30 (ComfyUI troubleshooting).
- QA prompts cover diagnostic, conceptual, decision, and volatile-fact axes.

## Remaining Vol. 1 gaps

- A normalized **failure card schema** so each retrieval card carries `symptom`, `cluster`, `likely_cause`, `safe_check`, `minimal_fix`, `advanced_fix`, `rollback`. Today's cards are mostly templated topic stubs.
- A current **known-good version-pair table** for the most-used clusters (Torch+CUDA, ORT+CUDA, ComfyUI+Python+Torch). Pair table belongs in lane RP08 but the entry-point card lives here.
- **Windows-vs-Linux divergence notes** for native-build failures (MSVC Build Tools vs build-essential vs Xcode CLT).
- **`uv` vs `pip` migration guidance** specifically for local AI envs (when uv's resolver helps, when it currently struggles).
- A short **launcher-script template pack** that does the smoke-test discipline named in the overview.
- Direct workflow JSON missing-node/model checks integrated into the runtime support pack.
- Windows PowerShell smoke-test scripts for the most common ComfyUI custom-node dependency clusters.

## Vol. 2 queue (research targets)

- Fill the failure cards with real tracebacks and recovery ladders from current GitHub issues and the AIWF Pip Package RAG Starter source pack.
- Cross-reference the EnvPack's actual `ai_workstation_validator.py` cluster detection logic — its real-world cluster classifications are stronger evidence than synthesized concept cards.
- Capture the ComfyUI-Manager registry boundary: which custom node packs are managed vs require manual install (this list churns; tag every entry `volatile_needs_recheck`).
- Add **NVIDIA driver vs CUDA toolkit vs CUDA wheel** explainer — the three-layer confusion is one of the most common beginner stuck points and isn't documented cleanly anywhere.
- Add **Apple Silicon (MPS) and AMD (ROCm) addenda** — currently the lane is implicitly NVIDIA-CUDA-centric. AIWF audience includes Mac users.
- Add **Conda vs venv vs Docker** decision card for users who already have one of these set up.

## Verification queue (volatile claims to web-check)

| Claim | Where used | Source to check |
|---|---|---|
| PyTorch wheel CUDA-family list | CANONICAL_OVERVIEW, QA prompt 12 | pytorch.org/get-started/locally |
| ComfyUI Python version requirement | QA prompt 13 | comfyanonymous/ComfyUI README, pyproject.toml |
| ONNX Runtime CUDA family names | CONCEPT_MAP | onnxruntime.ai/docs/install |
| `uv` CUDA-aware install support | QA prompt 14 | astral-sh/uv docs |
| ComfyUI Manager registry scope | CANONICAL_OVERVIEW | ltdrdata/ComfyUI-Manager README |
| xformers/flash-attn current Windows wheel availability | CONCEPT_MAP | facebookresearch/xformers releases |
| bitsandbytes Windows status | CONCEPT_MAP | TimDettmers/bitsandbytes README |

All claims above are tagged `volatile_needs_recheck` per `00_AI_READ_FIRST/ANTI_AI_SLOP_RESEARCH_POLICY.md`. Do not publish as canonical until verified.
