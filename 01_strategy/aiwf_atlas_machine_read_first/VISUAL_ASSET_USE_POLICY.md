# Visual Asset Use Policy

Visual assets are supporting explanation tools. They do not replace source verification, Atlas cards, or canonical lane summaries.

## Default Behavior

- Index `16_VISUAL_ASSETS/README.md` and `16_VISUAL_ASSETS/VISUAL_ASSET_INDEX.md`.
- Do not index raw SVGs by default.
- Retrieve raw SVGs only when the user asks for diagrams, visual assets, guide images, or Gradio UI illustrations.

## When To Suggest A Diagram

Suggest or use a visual when the answer involves:

- multi-step systems;
- source-verification gates;
- AIWF load order;
- Atlas routing;
- ComfyUI datatype boundaries;
- Gradio-to-ComfyUI automation;
- lakeFS versioning;
- synthetic-data flywheels;
- evaluation harness comparisons;
- cost/model routing.

## Humor Boundaries

Torchie may appear in visual callouts, but technical diagrams should remain clear first and funny second. If a joke makes the flow harder to understand, the joke goes into the nearest airlock.


## Torchie Rebrand Rule

Use `16_VISUAL_ASSETS/torchie_callouts/torchie_2026_rebrand_reference_sheet.png` as the canonical Torchie reference. Use only the Torchie 2026 rebrand assets for new guide art, UI callouts, and workflow cards.

Reusable clip-art duplicates are allowed when intentionally placed in guide layouts. Duplicate active Markdown, prompt, schema, or workflow-instruction files are not allowed; consolidate those into one canonical file plus pointers when needed.
