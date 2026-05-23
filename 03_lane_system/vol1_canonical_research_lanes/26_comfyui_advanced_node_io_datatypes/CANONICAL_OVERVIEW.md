# Canonical Overview

This lane teaches ComfyUI's socket/data contract layer: what a node accepts, what it returns, and what must change when a user wants to modify an input or output type.

## Core rule

Changing a node from `IMAGE` to `LATENT` is not a label-only edit. The socket label, Python value shape, execution logic, and downstream compatibility all change.

- `IMAGE` is a `torch.Tensor` shaped `[B,H,W,C]` with C=3.
- `MASK` is a `torch.Tensor` shaped `[B,H,W]`.
- `LATENT` is a `dict` whose sample tensor is stored at `latent["samples"]` and shaped `[B,C,H,W]`, usually C=4.

## Practical pattern: image node to latent node

Original image passthrough:

```python
class ImagePassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"image": ("IMAGE", {})}}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = "AI Without Fear/examples"

    def run(self, image):
        return (image,)
```

Latent passthrough:

```python
class LatentPassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"latent": ("LATENT", {})}}

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "run"
    CATEGORY = "AI Without Fear/examples"

    def run(self, latent):
        out = latent.copy()
        samples = out["samples"]
        # samples shape: [B, C, H, W]
        out["samples"] = samples
        return (out,)
```

## Safe conversion rule

If the user wants a node to accept latents instead of images, ask the AI to inspect the node's computation:

1. Does the function use pixel-space assumptions? If yes, it cannot be changed directly.
2. Does it use PIL, OpenCV, RGB channels, alpha, or image dimensions? If yes, it is image-space.
3. Does it operate on tensors generically and preserve shape? It may be portable to latent-space.
4. Does it need to decode/encode through a VAE? If yes, add explicit VAE inputs and make the conversion visible.
5. Does it return the same datatype it accepts? Match `RETURN_TYPES` to actual returned object.

## Multi-type pattern

For new V3-style nodes, ComfyUI supports `MultiType` inputs for a slot that can accept more than one datatype. Use this when the computation can honestly branch based on type. Do not use multi-type to hide incompatible behavior.

## Dangerous anti-patterns

- Changing `("IMAGE", {})` to `("LATENT", {})` without changing the function body.
- Treating `LATENT` like a tensor instead of a dictionary.
- Returning `samples` directly while declaring `RETURN_TYPES = ("LATENT",)`.
- Running PIL/OpenCV logic on latent tensors.
- Using wildcard `*` without validation and branch handling.
