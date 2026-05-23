# Query Routing Matrix

Use this matrix to route user questions to the correct adapter layer before answering.

| User intent | Primary layer | Secondary layer | Notes |
|---|---|---|---|
| What should I use? | `01_CANONICAL_RESEARCH_LANES` | `02_RETRIEVAL_INDEX` | Prefer canonical recommendations and decision cards. |
| How do I install/fix this? | `05_failure_signature_atlas_rag` and pip/runtime lanes | `03_SOURCE_CONTENT` | Check failure signatures before generic advice. |
| What does this node/package do? | custom node ecosystem lane | source content | Preserve exact class names and repo status. |
| Build a workflow | workflow pattern lane + ComfyUI JSON lane | node ecosystem lane | Separate conceptual graph from exact node JSON. |
| Explain a concept | canonical overview + concept map | Atlas cards | Use teaching structure, not raw source dump. |
| Compare options | Atlas cards + source coverage | reports/manifests | Mention confidence and currentness limits. |
| Is this current? | source coverage + manifests | official docs if available | Fast-moving facts should be verified externally. |
| What changed? | reports/change history | manifests | Use dedupe/consolidation maps for provenance. |
| Add a new topic | expansion slots + future topic intake template | schemas | Use the same lane kit. |
| Evaluate answers | evaluation harness | Atlas cards | Score retrieval quality, not just final prose. |

## Default routing rule

If a query can be answered from both source content and a canonical lane, retrieve the canonical lane first. Use the source archive to confirm provenance, details, or older-version context.

## Fast-moving subject rule

For current model releases, active GitHub repos, package versions, security issues, licenses, and hosted service behavior, treat the adapter as a baseline and verify against current primary sources when a live web connection is available.
