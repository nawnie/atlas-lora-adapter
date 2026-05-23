# Concept Map — Python/Pip Runtime Dependencies and Local AI Environment Support

## Primary diagnostic chain

```text
symptom -> failing surface -> cluster classification -> minimal fix -> smoke test -> rollback if needed
```

The chain is intentionally diagnostic-first. AIWF's value here is teaching the user to *name* the cluster before reaching for commands.

## Cluster taxonomy

| Cluster | Member packages (typical) | Owns these failures |
|---|---|---|
| Python build | `python`, `pip`, `setuptools`, `wheel`, `uv` | "no module named pip", venv creation errors, interpreter ABI mismatch |
| Torch family | `torch`, `torchvision`, `torchaudio`, `xformers`, `flash-attn`, `bitsandbytes` | CUDA-not-available, "operator not implemented for cuda", DLL load failures, kernel-not-found |
| Transformers stack | `transformers`, `tokenizers`, `safetensors`, `accelerate`, `peft`, `diffusers` | model load errors, tokenizer mismatch, "config has no attribute" |
| ONNX/provider | `onnxruntime`, `onnxruntime-gpu`, `onnxruntime-directml` | "CUDAExecutionProvider not available", silent CPU fallback, missing provider |
| Media stack | `Pillow`, `opencv-python`, `imageio`, `ffmpeg-python`, system `ffmpeg` | "decoder not found", PNG vs JPEG mode errors, video-codec failures |
| Web/serve | `fastapi`, `uvicorn`, `gradio`, `pydantic`, `httpx`, `websockets` | port-in-use, async/event-loop conflicts, "ASGI app failed to start", Pydantic v1 vs v2 errors |
| Native build | MSVC Build Tools / gcc + headers / Xcode CLT, CMake, Rust toolchain | "Microsoft Visual C++ 14.0 required", "failed building wheel", linker errors |
| Model/data | model file presence, safetensors hash, model card config | "no such file", "tensor shape mismatch", "model expects float16" |
| Process runtime | port use, GPU memory leaks across runs, zombie Python processes | "CUDA out of memory after the second run", port already bound, hung subprocess |

## Concept relationships

| Concept | Depends on | Often confused with | Retrieval role |
|---|---|---|---|
| venv island | Python build | global pip install | environment-isolation anchor |
| wheelhouse | Python build, ABI | source-from-scratch builds | reproducibility anchor |
| ABI boundary | CUDA wheel family, native toolchain | "the wheel is wrong" | silent-failure anchor |
| CUDA wheel family | Torch family | "I have CUDA installed" (toolkit != wheel-bundled libs) | install-pairing anchor |
| provider mismatch | ONNX/provider cluster | "ORT installed but slow" | runtime-route anchor |
| native build toolchain | platform-specific | "I have Python, why does this need a compiler" | environment-prereq anchor |
| import smoke test | all clusters | full-workflow test | early-failure anchor |
| package cluster | all of the above | "just update everything" | safe-update anchor |
| external binary dependency | media stack, web stack | "Python should have this built in" | system-dependency anchor |

## Most common failure flows (for retrieval)

1. **User updated Torch -> custom nodes broke.** Cluster: Torch family. Fix: pin Torch+xformers+flash-attn together; the custom nodes wanted a specific xformers ABI.
2. **CUDA out of memory only on second run.** Cluster: Process runtime + Torch family. Fix: torch.cuda.empty_cache() between runs, or restart the process; check for leaked references in custom node code.
3. **ComfyUI launched but a node is red.** Cluster: Native build OR Torch family. Most common path: a custom node tried to build a wheel at install time and silently failed; check the ComfyUI console for the build error from earlier in the log.
4. **Gradio app says "address already in use".** Cluster: Web/serve + Process runtime. Fix: change port or kill the stranded process; on Windows, `netstat -ano | findstr :7860` then `taskkill /pid <pid> /f`.
5. **`pip install onnxruntime-gpu` succeeded but CPU is used.** Cluster: ONNX/provider. Fix: check CUDA toolkit version matches ORT's bundled requirements; ORT publishes wheels per CUDA family same as Torch.

## Cross-lane links

- **RP08** — Compatibility Matrix Atlas (for the version-pair table itself)
- **RP09** — Failure Signature Atlas (for symptom->cluster mapping)
- **RP30** — ComfyUI Troubleshooting, Migration, and Packaging
- **RP25** — Hardware Cost and Performance Planning (for hardware-driven environment choices)

## Cards in this lane

See `RETRIEVAL_CARDS.jsonl`. Each card represents one cluster concept and links to source packs for evidence.
