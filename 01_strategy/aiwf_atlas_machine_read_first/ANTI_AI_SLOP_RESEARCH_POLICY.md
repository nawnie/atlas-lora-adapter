# Anti-AI-Slop Research Policy v1.9

The adapter must actively prevent AI-generated research slop. A source-rich archive is only useful if the claims are verified, qualified, and traceable.

## Hard Rules

1. Do not invent citations, model names, benchmark numbers, paper titles, repository statuses, or dates.
2. Do not cite a bibliography entry as proof unless the underlying source actually supports the claim.
3. Do not elevate raw notes into canonical facts without a source tier.
4. Do not preserve AI assistant scaffolding, leftover chat instructions, or unfinished-generation markers. Future work belongs in the roadmap.
5. Do not use broad absolute language for volatile domains. Prefer qualified wording unless a primary/official source supports the statement.
6. For public-release claims, verify with web sources at release time.

## Red Flags

- fabricated or unresolvable references;
- incorrect citations;
- leftover AI comments/instructions;
- fake precision;
- broad "industry standard" claims without supporting source;
- model or hardware rankings without dates and sources;
- docs/API claims not pinned to official docs.

## Required Status Labels

Use these labels in claim manifests and lane profiles:

- `primary_verified`
- `official_docs_verified`
- `peer_reviewed_verified`
- `secondary_verified`
- `volatile_needs_recheck`
- `user_note_unverified`
- `unsupported_remove_from_canonical`

## Practical Release Rule

If a source cannot be checked, the claim can remain in raw provenance but must not be used as canonical advice.
