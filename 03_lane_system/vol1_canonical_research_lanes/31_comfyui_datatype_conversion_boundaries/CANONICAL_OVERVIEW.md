# Canonical Overview — ComfyUI Datatype Boundaries

## Core rule

A ComfyUI socket datatype is a contract between the graph, the frontend, and the node function. Changing a socket from `IMAGE` to `LATENT` is safe only when the Python function also consumes and returns the correct Python object shape.

## IMAGE

`IMAGE` is pixel-space data. In official ComfyUI docs it is a `torch.Tensor` shaped `[B,H,W,C]`, with channel-last layout and usually `C=3`. Use `IMAGE` for RGB operations, PIL/OpenCV work, compositing, pixel masks, previews, saving images, and image-space postprocessing.

## LATENT

`LATENT` is denoising-space data. In official ComfyUI docs it is a dictionary. The sample tensor is stored under the `samples` key and shaped `[B,C,H,W]`, with channel-first layout. For existing Stable Diffusion style models, `C` is generally 4 and spatial dimensions are commonly lower than image-space dimensions. Use `LATENT` for sampling, latent noise, latent routing, latent upscale/downscale, latent blending, and pre-decode operations.

## MASK

`MASK` is usually a single-channel tensor. The official docs describe masks as tensors shaped `[B,H,W]`, while the datatype reference also warns that shapes can vary in practice. Custom nodes should inspect mask dimensions and normalize them before broadcasting or mixing with image/latent tensors.

## VAE boundary

The usual boundary between image space and latent space is the VAE:

- VAE Encode: `IMAGE` to `LATENT`
- VAE Decode: `LATENT` to `IMAGE`

Do not pretend an `IMAGE` and a `LATENT` are interchangeable. They encode different representations, have different shapes, and support different classes of operations.

## CONDITIONING and model objects

`MODEL`, `CLIP`, `VAE`, and `CONDITIONING` are not generic tensors. They are model or conditioning objects with internal structures tied to ComfyUI's sampling pipeline. A user may want to pass them around, route them, merge them, or package them in pipes, but the assistant must not invent internal structures unless verified against source code or official docs.

## Changing a node from IMAGE to LATENT

Safe pattern:

1. Change `INPUT_TYPES` from `("IMAGE", {})` to `("LATENT", {})`.
2. Change `RETURN_TYPES` if the output changes.
3. Rewrite the function body to operate on `latent["samples"]` instead of image pixels.
4. Preserve the latent dictionary keys unless intentionally replacing them.
5. Return a tuple matching `RETURN_TYPES`.
6. Add validation and clear error messages.

Unsafe pattern:

- Only changing the socket text from `IMAGE` to `LATENT` while leaving PIL/OpenCV/RGB code unchanged.

## Minimal LATENT passthrough example

```python
class AIWFLatentPassthrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT", {}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "run"
    CATEGORY = "AI Without Fear/examples"

    def run(self, latent):
        out = latent.copy()
        out["samples"] = out["samples"].clone()
        return (out,)
```

## Minimal latent strength example

```python
class AIWFLatentStrength:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT", {}),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "run"
    CATEGORY = "AI Without Fear/examples"

    def run(self, latent, strength):
        out = latent.copy()
        samples = out["samples"]
        out["samples"] = samples * strength
        return (out,)
```

This example is intentionally simple. Real latent edits can easily damage generations if they ignore sampler stage, sigma schedule, model family, or VAE expectations.

## When to build a new node instead

Build a new node when:

- the old node has many image-space assumptions,
- the old node uses PIL/OpenCV/NumPy RGB operations,
- you want to support both `IMAGE` and `LATENT`,
- old workflows already depend on the existing socket contract,
- changing the existing node would break saved workflow JSON.

## Assistant rule

When the user asks how to change sockets, answer with the datatype contract first, then the code-level edits, then the graph-level boundary implications.
