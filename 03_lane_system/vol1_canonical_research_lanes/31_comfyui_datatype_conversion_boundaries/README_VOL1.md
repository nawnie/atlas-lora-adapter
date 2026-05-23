# ComfyUI Datatype Conversion and Boundary Design

Lane ID: `RP31`  
Status: Vol. 1 advanced ComfyUI research pass 02  
Purpose: Teach AI assistants how to reason about ComfyUI datatype boundaries before recommending node edits, datatype conversions, workflow rewiring, or custom socket changes.

## Use this lane when

- The user wants a node that accepts `IMAGE` to accept `LATENT`, or the reverse.
- The user asks why two sockets cannot connect.
- The user asks about `IMAGE`, `LATENT`, `MASK`, `CONDITIONING`, `MODEL`, `CLIP`, or `VAE` objects.
- The user wants a custom node to support more than one datatype.
- The user wants to move work earlier or later in the graph to save VRAM, preserve quality, or avoid VAE encode/decode loss.

## Source priority

Use official ComfyUI datatype, image/mask/latent, custom node properties, lazy evaluation, and V3 schema docs first. Use source code or verified node-pack examples only after the official datatype contract is understood.
