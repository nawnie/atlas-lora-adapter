# ComfyUI Advanced Workflow Design Patterns

This lane teaches an AI assistant how to design advanced ComfyUI workflows as maintainable systems rather than giant unmanaged canvases.

The focus is workflow architecture: when to use subgraphs, switches, soft switches, lazy branches, bypasses, master-control panels, templates, blueprints, reusable groups, and stable workflow-as-app contracts.

## Canonical use

Use this lane when the user asks how to:

- make a large workflow easier to use
- combine restore, upscale, inpaint, face detail, pose, video, or control branches
- build a router workflow with optional stages
- use switches or soft switches without wasting VRAM
- decide whether a branch should be bypassed, muted, switched, lazy, or removed
- package common workflow sections as subgraphs
- expose selected controls while hiding internal complexity
- make workflows shareable, updateable, or app-like

## Core rule

Do not recommend one giant canvas when the user needs repeatability. Prefer a layered design: input contract, branch routers, stable processing modules, explicit outputs, and source-verified subgraphs/templates for reusable sections.
