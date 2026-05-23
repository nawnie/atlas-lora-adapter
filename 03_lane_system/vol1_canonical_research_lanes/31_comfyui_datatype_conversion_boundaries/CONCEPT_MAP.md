# Concept Map — ComfyUI Datatype Boundaries

```text
ComfyUI graph
  ├─ socket datatype contract
  │   ├─ frontend connection validation
  │   ├─ backend function argument type
  │   └─ workflow JSON compatibility
  ├─ tensor-like datatypes
  │   ├─ IMAGE -> torch.Tensor [B,H,W,C]
  │   ├─ MASK -> torch.Tensor, usually [B,H,W]
  │   └─ LATENT -> dict with samples [B,C,H,W]
  ├─ model/pipeline datatypes
  │   ├─ MODEL
  │   ├─ CLIP
  │   ├─ VAE
  │   └─ CONDITIONING
  ├─ sampling datatypes
  │   ├─ NOISE
  │   ├─ SAMPLER
  │   ├─ SIGMAS
  │   └─ GUIDER
  ├─ conversion boundaries
  │   ├─ VAE Encode: IMAGE -> LATENT
  │   ├─ VAE Decode: LATENT -> IMAGE
  │   ├─ mask resize/broadcast
  │   └─ conditioning encode/combine
  └─ advanced routing
      ├─ lazy inputs
      ├─ V3 MultiType
      ├─ V3 MatchType
      └─ explicit separate typed inputs
```

## Relationship notes

- `IMAGE` operations are generally user-visible and post-decode.
- `LATENT` operations are generally sampler-adjacent and pre-decode.
- `MASK` can guide either image-space compositing or latent-space denoise control, but shape normalization is required.
- `CONDITIONING` changes what the model is guided toward, not the pixel/latent tensor directly.
- `VAE` is the canonical image/latent bridge.
