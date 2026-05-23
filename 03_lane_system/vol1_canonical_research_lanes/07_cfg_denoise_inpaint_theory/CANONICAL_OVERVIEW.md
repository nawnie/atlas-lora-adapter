# Canonical Overview — CFG, Denoise, Img2Img, and Inpainting Theory

## Core idea

    Editing controls are best taught as staged intervention strength: preserve structure first, then repair content, then finish detail.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- CFG
- denoise
- latent noise
- mask boundary
- context crop
- stitch blend
- inpaint conditioning
- LaMa/MAT prefill
- Fooocus inpaint patch
- seam control

## Common retrieval questions

- Why did my inpaint replace too much?
- What denoise range should I use for face-safe restoration?
- When should I crop-and-stitch instead of full-frame inpaint?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
