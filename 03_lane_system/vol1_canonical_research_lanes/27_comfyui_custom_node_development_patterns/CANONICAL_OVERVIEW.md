# Canonical Overview

This lane covers custom node authoring patterns beyond a minimal node: execution control, caching behavior, hidden inputs, lazy inputs, output nodes, validation, and schema-forward design.

## Minimal contract

A backend custom node is a Python class. It defines `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, `CATEGORY`, and a method whose name matches `FUNCTION`. `INPUT_TYPES` returns required, optional, and hidden input groups. `RETURN_TYPES` declares output sockets. The function returns a tuple that corresponds exactly to `RETURN_TYPES`.

## Execution/caching policy

ComfyUI caches outputs and executes nodes that may produce changed outputs. If a node depends on external files, randomness, mutable state, or ignored inputs, it may need explicit `IS_CHANGED` handling or a seed/file-hash input.

## Hidden inputs

Use hidden inputs for advanced context such as `UNIQUE_ID`, `PROMPT`, `EXTRA_PNGINFO`, and `DYNPROMPT`. Do not expose hidden inputs as normal user controls unless the user needs to reason about them.

## Lazy evaluation

Use lazy inputs when a node may not need expensive upstream data. Router/switch nodes, model merge nodes, and conditional output nodes should prefer lazy inputs plus `check_lazy_status`.

## V1 vs V3

V1 nodes are still common. V3 schema is the forward-looking path for richer typing, `MultiType`, `MatchType`, and future extension features. AIWF should teach both: maintain V1 compatibility for existing packs; prefer V3 for new advanced pack design when stable in the target ComfyUI version.
