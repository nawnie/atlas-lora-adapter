# Source Coverage — ComfyUI Datatype Boundaries

## Verified source set

- Official ComfyUI backend datatype documentation.
- Official ComfyUI Images, Latents, and Masks documentation.
- Official ComfyUI custom node property documentation.
- Official ComfyUI hidden/flexible input documentation.
- Official ComfyUI lazy evaluation documentation.
- Official ComfyUI V3 migration documentation for MultiType, MatchType, and custom types.

## Confidence

High for datatype names, shapes, `INPUT_TYPES`, `RETURN_TYPES`, function return tuple rules, lazy input mechanics, and V3 MultiType/MatchType existence.

Medium for higher-level design recommendations, because workflow design depends on the specific node function, model family, and user graph.

## Verification rule

When a claim concerns current ComfyUI implementation behavior, prefer official docs or current source before using old community examples.
