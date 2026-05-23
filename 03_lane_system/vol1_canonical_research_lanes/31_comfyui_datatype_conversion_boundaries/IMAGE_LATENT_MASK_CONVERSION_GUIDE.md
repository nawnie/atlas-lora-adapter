# Practical Guide — IMAGE, LATENT, and MASK Conversion Boundaries

## Fast decision table

| User goal | Recommended boundary |
|---|---|
| Apply RGB color, blur, crop, sharpen, composite, or save output | Use `IMAGE` |
| Modify denoising-space tensor before decode | Use `LATENT` |
| Inpaint or restrict where changes apply | Use `MASK` plus conditioning or latent/image compositing path |
| Convert pixels into latent space | Use VAE Encode or a node that explicitly takes a `VAE` and returns `LATENT` |
| Convert latents into pixels | Use VAE Decode or a node that explicitly takes a `VAE` and returns `IMAGE` |
| Build one node for multiple input types | Prefer V3 `MultiType`, `MatchType`, or separate explicit typed inputs with validation |

## Safe `IMAGE` to `LATENT` rewrite checklist

- Identify every line that assumes `[B,H,W,C]`.
- Replace image tensor logic with `latent["samples"]` logic.
- Preserve existing latent dictionary keys unless intentionally replacing them.
- Keep tensor shape `[B,C,H,W]` unless the downstream node expects a changed shape.
- Return `(latent_out,)`, not `latent_out`.
- Validate that `samples` exists and is a tensor.
- Do not use PIL/OpenCV directly on `samples`.

## Safe dual-path design

For V1-style nodes, the most maintainable design is often two explicit inputs:

```python
@classmethod
def INPUT_TYPES(cls):
    return {
        "optional": {
            "image": ("IMAGE", {}),
            "latent": ("LATENT", {}),
        },
        "required": {
            "mode": (["image", "latent"], {"default": "image"}),
        }
    }
```

Then validate that the selected mode has the matching connected input. This is clearer than pretending one implementation can process both spaces identically.

## V3 multi-type design

For newer V3 schema nodes, `MultiType` is the cleaner pattern when the same conceptual input can accept multiple datatypes and the execution method branches safely by actual type.

## Failure signatures

- `KeyError: 'samples'`: code expected a latent dict but received another object.
- `too many indices` or `not enough values to unpack`: tensor shape/channel-order mismatch.
- Red link/socket mismatch: frontend datatype contract prevents incompatible connection.
- Silent bad output: latent tensor was altered mathematically but not semantically correctly for the sampler/model.
