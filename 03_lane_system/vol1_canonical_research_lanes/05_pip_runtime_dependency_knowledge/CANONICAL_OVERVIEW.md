# Canonical Overview — Python/Pip Runtime Dependencies and Local AI Environment Support

## Core idea

Runtime failures in local AI are cluster failures, not isolated package failures. A working stack is a tuned dependency graph across Python, PyTorch, CUDA toolkit, cuDNN, ONNX Runtime, transformers, diffusers, media libs (ffmpeg/PIL/opencv), web servers (FastAPI/Uvicorn/Gradio), and native build toolchains. When one piece slips an ABI version, the whole graph can fail to import even though `pip install` reported success.

AIWF support should diagnose at the cluster level — name which cluster owns the error before suggesting a fix — and prefer reversible, isolated repair over global reinstalls.

## Operational model

Use this lane as a decision layer:

1. Identify the failing surface — install, import, inference, render, serve.
2. Classify the cluster: Python build, Torch/CUDA family, ONNX provider, native build, model/data, or process/runtime.
3. Retrieve the concept card for that cluster from `RETRIEVAL_CARDS.jsonl`.
4. Check the source/provenance folder for known-good version pairs.
5. Produce an action: smoke test → minimal fix → advanced fix → rollback path.

## Main concepts (Vol. 1 baseline)

- **venv island** — an isolated environment whose interpreter, site-packages, and binaries cannot leak into another project's environment. Python's `venv`, `uv`, and `conda` all produce islands; the difference is binary management.
- **wheelhouse** — a local or remote cache of pre-built `.whl` files keyed by Python version, platform, and ABI tag. Production installs should prefer a wheelhouse over building from source.
- **ABI boundary** — the compiled interface between Python C extensions and the host (interpreter version, CUDA version, GLIBC version on Linux, MSVC runtime on Windows). Mismatch produces silent imports that fail at first runtime call.
- **CUDA wheel family** — PyTorch publishes parallel wheel sets keyed to CUDA toolkit minor version (e.g. `cu118`, `cu121`, `cu124`, `cu126`). Wheels in different families are not mix-and-match; downstream packages (xformers, flash-attn, bitsandbytes, onnxruntime-gpu) must match the chosen Torch family. Specific current pairs are volatile — check pytorch.org/get-started before installing.
- **provider mismatch** — when ONNX Runtime, TensorRT, or DirectML is asked to use a provider whose backing library isn't installed or doesn't match the model. Common form: "CUDAExecutionProvider not available, falling back to CPU" with no obvious error.
- **native build toolchain** — the compiler/header chain needed when no pre-built wheel exists for a package on the current platform: MSVC Build Tools on Windows, gcc + CUDA headers on Linux, Xcode CLT on macOS. Missing toolchain produces verbose multi-page errors that bury the real cause near the bottom.
- **import smoke test** — a deliberately small script that `import torch; torch.cuda.is_available()` plus the project's two or three critical packages, run immediately after install. Catches ABI breaks before the user wastes time loading models.
- **package cluster** — a group of packages that must move together: e.g. `{torch, torchvision, torchaudio, xformers}` or `{transformers, tokenizers, safetensors, accelerate}`. Updating one without the others is the most common AIWF user failure mode.
- **external binary dependency** — non-Python binaries the stack depends on (ffmpeg, git, espeak-ng, sox). On Windows these usually need PATH entries; on Linux they need apt/yum packages; users on either platform discover them only when something fails.

## Common retrieval questions

- Why did a ComfyUI custom node fail to import after a Torch update?
- Which package cluster owns this error message?
- Can this Gradio module run in a separate venv to avoid a conflict with ComfyUI?
- What should the one-click installer test before the first launch?
- Why does ONNX Runtime fall back to CPU even though I have a GPU?
- Why does pip say "successfully installed" but the import fails?

## Decision postures (use / wrap / document / build)

- **Use** — `uv` for fast modern venv creation; `pip` from a venv for ComfyUI custom nodes; ComfyUI Manager for installing well-known node packs.
- **Wrap** — provide AIWF launcher scripts that activate the venv, set CUDA paths, run smoke tests, and surface clean error messages instead of raw tracebacks.
- **Document** — known-good Torch+CUDA pairs, custom-node compatibility windows, and "ABI broke" recovery procedures.
- **Build** — only when no existing tool covers the user's failure mode (e.g. AIWF EnvPack's whole reason to exist).

## Stable vs fast-moving knowledge

**Stable** — cluster boundaries, ABI concepts, the venv-island principle, smoke-test discipline, "don't update one cluster member without the others" rule.

**Fast-moving (volatile, recheck before publishing)** —
- exact PyTorch + CUDA toolkit pairings (currently varies by Torch minor version; check pytorch.org)
- ComfyUI's current Python version requirement
- ComfyUI Manager's current scope (it has expanded several times)
- xformers / flash-attn / bitsandbytes Windows build status
- which custom-node packs ship pre-built wheels vs require source build
- ONNX Runtime provider names and packaging
- `uv` feature availability vs `pip`

## AIWF brand alignment

Beginner-safe defaults: always recommend a venv island over global install, smoke-test before model loads, and prefer ComfyUI Manager over manual node installation when the node is in the manager registry. Reserve manual install instructions for nodes that aren't registered.

Calm-incident voice for install failures. Most pip errors are scary-looking but pattern-matchable; the lane's job is to make the pattern visible.
