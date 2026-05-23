# ComfyUI Advanced Workflow Pattern Guide

## Choose the smallest pattern that solves the problem

- Need readability only: use layout, labels, colors, and subgraphs.
- Need reusable sections: use subgraphs or subgraph blueprints.
- Need user-facing examples: use workflow templates.
- Need one of two typed values: use Switch.
- Need unused branch not evaluated: use Soft Switch or lazy custom switch.
- Need runtime graph construction: use Node Expansion with GraphBuilder.
- Need old workflows to survive refactors: use Node Replacement.

## Router workflow skeleton

1. One input block: image, mask, prompt, model preset, operation mode.
2. One model-loading block: keep model/clip/vae boundaries stable.
3. One router block: choose restore, inpaint, upscale, detail, video, or passthrough.
4. One module block per operation: each module should have a narrow input/output contract.
5. One output selector: route final image, preview, mask, latent, video, or debug output.
6. One save/output block: predictable filenames and output type.

## Subgraph boundary rules

Good subgraph boundaries:

- before and after a complete operation
- at stable datatypes such as IMAGE in and IMAGE out
- around a repeated pattern used in multiple workflows
- around detailer/upscale/inpaint modules
- around a set of nodes that should be hidden from beginner users

Bad subgraph boundaries:

- halfway through a sampler unless the latent contract is explicit
- around one random node just to reduce visual clutter
- across unrelated model-loading and output-saving logic
- across a branch that needs different datatypes depending on mode

## Bypass, mute, switch, and lazy branch distinctions

- Bypass/mute is best for manual workflow editing or pre-execution disabling.
- App-side payload mutation is best when a Gradio/API wrapper controls what nodes exist or which values are set before queueing.
- Switch nodes are best for selecting between two already-valid typed inputs.
- Soft/lazy switches are best when evaluating the unselected branch is expensive or invalid.
- ExecutionBlocker is for stopping downstream execution intentionally, usually inside custom node logic.

## Workflow-as-app contract

For workflows controlled by an app, document:

- input node IDs
- exposed widget names
- accepted value ranges
- required model files
- branch modes
- expected output node IDs
- supported ComfyUI version range
- custom node packs required
- fallback behavior

If this contract changes, treat it as a versioned API change.
