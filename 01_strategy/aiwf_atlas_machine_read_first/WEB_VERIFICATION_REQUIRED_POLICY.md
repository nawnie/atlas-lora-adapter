# Web Verification Required Policy v1.9

This adapter must not rely on an old temporary "no web" assumption. Web verification is required whenever a claim is volatile, current, tool/API-specific, legal/licensing-related, source-integrity-related, or otherwise likely to drift.

## Required Web Verification Cases

Use current web verification for:

1. current model rankings, model availability, weights, licenses, benchmark numbers, and release dates;
2. software APIs, ComfyUI custom-node behavior, node class names, workflow schemas, install paths, and registry behavior;
3. hardware specs, pricing, performance-per-dollar, performance-per-watt, cloud instance details, and TCO statements;
4. security, safety, governance, academic/publication policy, legal, and licensing claims;
5. anything described as latest, current, 2026, modern, active, deprecated, maintained, abandoned, official, or state-of-the-art;
6. any claim being prepared for a release README, research report, or public repository.

## Exceptions

Do not browse only when the user explicitly says not to browse, or when the task is pure rewriting of already-provided text and no factual update is needed.

## Machine Behavior

When retrieving from this adapter, AI systems should prefer verified source pins and should not turn user notes, summaries, or raw research drafts into hard facts unless a source tier supports the claim.
