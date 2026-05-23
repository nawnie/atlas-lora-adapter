# Concept Map — Video VRAM Optimization

## Core concepts

- Video pipelines amplify memory pressure compared with still-image jobs.
- Frame count and frames-per-batch are major scaling controls.
- Runtime evidence should drive diagnosis.

## Likely user intents

- Diagnose OOM and scaling failures.
- Differentiate runtime setup vs memory pressure.
- Provide small-model-friendly troubleshooting steps.

## Neighboring lanes

- 45_last_frame_chaining_video_extension
- 39_cuda_torch_runtime_alignment
- 62_vram_memory_management
