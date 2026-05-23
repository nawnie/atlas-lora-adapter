# Vol. 1 Scope — ComfyUI Advanced Workflow Design Patterns

## In scope

- workflow modularity and subgraph design
- switch and soft-switch routing
- lazy branch evaluation and execution-blocking concepts
- master-control panel patterns
- bypass, mute, and runtime-routing distinctions
- reusable workflow components and subgraph blueprints
- template packaging for custom node packs
- app-like workflow contracts for Gradio or API front ends
- migration-aware workflow and node-pack design

## Out of scope

- low-level tensor datatype conversion covered by lane 31
- local API automation covered by lane 32
- full frontend extension development beyond subgraph implications
- custom model architecture design
- unsafe public deployment of ComfyUI servers

## Boundary rule

When the user wants optional workflow branches, distinguish three cases:

1. UI-only organization: use subgraphs, labels, colors, groups, or templates.
2. Pre-execution choice: use bypass/mute or app-side API payload mutation.
3. Runtime choice: use typed switches, soft switches, lazy inputs, or custom router nodes.
