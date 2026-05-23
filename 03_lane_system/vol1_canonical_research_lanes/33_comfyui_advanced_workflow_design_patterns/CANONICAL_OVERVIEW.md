# Canonical Overview — ComfyUI Advanced Workflow Design Patterns

Advanced ComfyUI workflow design is the discipline of making complex node graphs reliable, readable, reusable, and controllable.

A mature workflow should have:

1. a clear input contract
2. stable model-loading boundaries
3. branch selectors for optional stages
4. reusable modules for repeated patterns
5. explicit output selection
6. safe error/fallback paths
7. minimal exposed controls for the intended user
8. source-verified version and dependency notes

## Main pattern families

### Subgraph pattern

Use subgraphs when a repeated or complex section should act like one reusable node. Subgraphs are best for “this section always works together” logic, such as crop-and-stitch inpaint modules, face-detail modules, upscaler modules, or video post-processing modules.

### Router pattern

Use routers when one input may flow through different processing branches. Examples include restore vs inpaint vs upscale, SDXL vs Flux, portrait vs product image, or fast preview vs final render.

### Soft-switch pattern

Use soft switches or lazy custom switches when unused branches are expensive or may error if evaluated. This matters for models that should not load, encoders that only apply to one architecture, and optional branches that should not consume VRAM.

### Master-control panel pattern

Use a visible control area to collect the user-facing widgets. The internal graph may be large, but the user should see only the knobs that are safe and meaningful.

### Workflow-as-app contract

When a workflow will be driven from Gradio/API, node IDs, input names, output nodes, model requirements, and supported parameter ranges must be stable. Treat the workflow as an API contract, not as a personal canvas.
