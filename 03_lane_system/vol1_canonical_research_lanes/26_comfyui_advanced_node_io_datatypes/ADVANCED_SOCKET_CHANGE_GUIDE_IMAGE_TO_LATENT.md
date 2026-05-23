# Advanced Socket Change Guide: IMAGE to LATENT

## Purpose

This file teaches an AI assistant how to answer user questions like:

> "This ComfyUI node accepts IMAGE, but I want it to accept LATENT. How do I change the node input and output?"

The answer must avoid pretending that socket labels are magic converters. In ComfyUI, the socket type is a contract between nodes. Changing `IMAGE` to `LATENT` changes what object the function receives and returns.

## Core Rule

Changing a ComfyUI custom node from `IMAGE` to `LATENT` requires all three layers to match:

1. `INPUT_TYPES` must declare the new type.
2. `RETURN_TYPES` must declare the returned type.
3. The node function must actually handle the Python object shape/structure for that type.

A node that performs RGB/PIL/OpenCV/pixel math cannot become latent-native by changing only the type string.

## Official Type Facts to Preserve

- Custom node inputs are declared by `INPUT_TYPES`.
- Outputs are declared by `RETURN_TYPES`.
- The node function returns a tuple corresponding to `RETURN_TYPES`.
- `IMAGE` data is tensor-like image data.
- `LATENT` is not the same as `IMAGE`; it is commonly a dictionary containing a `samples` tensor.
- When in doubt, bridge between image space and latent space with VAE encode/decode nodes or require a VAE input inside the node.

## Minimal LATENT Passthrough Node

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
        out = dict(latent)
        out["samples"] = latent["samples"]
        return (out,)
```

## Pattern 1: The Old Node Only Passed the Image Through

If the old node did not inspect or alter pixels, it can often be converted by changing `IMAGE` to `LATENT` and adjusting variable names.

```python
@classmethod
def INPUT_TYPES(cls):
    return {"required": {"latent": ("LATENT", {})}}

RETURN_TYPES = ("LATENT",)
FUNCTION = "run"

def run(self, latent):
    return (latent,)
```

## Pattern 2: The Old Node Did Pixel Work

If the old node uses PIL, OpenCV, RGB channels, width/height pixel operations, blur, mask painting, color matching, or image compositing, keep it as `IMAGE` or add explicit VAE boundaries.

Workflow-level safer approach:

```text
LATENT -> VAEDecode -> IMAGE node -> VAEEncode -> LATENT
```

Node-level approach, if you intentionally want one custom node:

```text
LATENT + VAE -> decode to image -> run image operation -> encode back to latent
```

This requires a VAE input and must preserve batch/device/dtype behavior.

## Pattern 3: Native Latent Processing

A true latent node operates on `latent["samples"]`.

```python
def run(self, latent, multiplier=1.0):
    out = dict(latent)
    samples = latent["samples"]
    out["samples"] = samples * multiplier
    return (out,)
```

Warnings:

- Do not assume latent channel count is always 4 for every model family.
- Do not assume image-space height/width equals latent-space height/width.
- Do not mutate the input dictionary in-place unless you deliberately want side effects.
- Preserve extra latent dictionary keys when possible.
- Keep tensor device and dtype intact.

## Pattern 4: Dual IMAGE/LATENT Acceptance

If a node should accept either `IMAGE` or `LATENT`, do not use wildcard typing casually. Prefer an explicit mode or V3 typed interface where possible.

Suggested machine answer:

> "Use separate inputs or separate nodes unless you have a strong reason to make one flexible node. One clear IMAGE node and one clear LATENT node are usually safer than a magical any-type node."

## Pattern 5: Backward Compatibility

If you published a node and then change its type/name/inputs, use ComfyUI's node replacement/migration pattern rather than breaking old workflows.

## Answer Template for Users

When a user asks how to change IMAGE input/output to LATENT:

1. Explain that type strings and function logic must both change.
2. Ask whether the node does pixel work or latent tensor work only if necessary.
3. Provide a minimal LATENT passthrough example.
4. Provide the VAE bridge pattern if the original node works in image space.
5. Warn about shape/device/dtype/metadata preservation.
6. Recommend workflow-level conversion first unless a native latent operation is clearly needed.
