# Concept Map — CUDA, Torch, and Runtime Alignment

## Core concepts

- GPU acceleration is a stack: driver, CUDA runtime expectations, PyTorch build, and optional backends.
- Active venv determines torch behavior.
- Current docs are required for exact install commands.

## Likely user intents

- Diagnose torch.cuda unavailable.
- Separate OOM from binary mismatch.
- Handle optional backend errors.

## Neighboring lanes

- 38_windows_ai_workstation_setup
- 44_video_vram_optimization
- 05_pip_runtime_dependency_knowledge
