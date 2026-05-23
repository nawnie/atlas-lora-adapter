# Canonical Overview

This lane covers frontend extension patterns: custom browser-side behavior, widgets, hooks, UI state, subgraph-aware UI behavior, and extension risk.

## Frontend extension packaging

A custom node pack can expose browser JavaScript by exporting `WEB_DIRECTORY` and placing JS files in that directory. The browser loads JS files when the Comfy page loads.

## Hooks and app extensions

Extensions register with `app.registerExtension` and implement lifecycle hooks. Use hooks conservatively: they can improve UX, but they are a common source of breakage after frontend updates.

## UI safety

Frontend extensions should be optional where possible. Do not make backend computation depend on fragile UI state unless the state is serialized into workflow/API data.

## When to build UI controls

Build custom UI only when built-in widgets, promoted inputs, subgraphs, and workflow templates cannot express the user interaction. For beginner-facing AIWF tools, prefer stable controls over clever UI hacks.
