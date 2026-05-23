# Embedding and Chunking Strategy — Python/Pip Runtime Dependencies

## Why this lane needs special handling

Pip/runtime answers depend on **exact identifiers** — package names, version specifiers, error message strings, file paths, and class names. Dense semantic embeddings tend to lose these. Retrieval that misses `bitsandbytes` because it semantically merged it into "quantization library" is a failure.

## Chunking rules

- **One concept card per chunk.** Do not merge "venv island" and "wheelhouse" even though they're related; the user's query will anchor on one or the other.
- **Keep tracebacks intact.** When a failure card cites a real traceback, the traceback is one chunk; do not split at line breaks.
- **Keep version-pair tables intact.** Tables encode the relationship between cells; splitting a Torch+CUDA pair table by row destroys the meaning.
- **Code blocks are atomic.** PowerShell, bash, and pip command examples must not split across chunks. Half a `pip install` command is worse than no command.
- **One failure flow per chunk.** From symptom → diagnosis → minimal fix → smoke test → rollback. Splitting these reads as out-of-order advice.

## Required metadata per chunk

| Field | Purpose |
|---|---|
| `lane_id` | Routes to RP05 |
| `cluster` | One of the nine clusters in `CONCEPT_MAP.md` |
| `os_scope` | `windows`, `linux`, `macos`, or `cross_platform` |
| `severity` | `info`, `warning`, `breaks_install`, `breaks_runtime`, `breaks_environment` |
| `freshness_class` | `stable`, `slow_changing`, `fast_moving`, `volatile` |
| `claim_confidence` | One of the seven labels from `ANTI_AI_SLOP_RESEARCH_POLICY.md` |
| `requires_admin` | `true` if the fix needs elevated privileges or system PATH changes |
| `doc_role` | `concept_card`, `source_note`, `package_card`, `node_card`, `failure_card`, `manifest`, `code`, `qa_prompt` |
| `action_policy` | `use`, `wrap`, `document`, `build`, `verify_first` |
| `retrieval_keys` | exact names, package names, node class types, failure strings, workflow names |

## Hybrid retrieval policy

Run dense + sparse retrieval in parallel for this lane:

- **Dense embeddings** — for concept queries ("how do venvs differ from global pip"), conceptual diagnostics ("what is an ABI mismatch").
- **Sparse / lexical (BM25)** — for exact-name queries (`bitsandbytes`, `flash-attn`, `cu124`, `ImportError: DLL load failed`).

Merge using reciprocal rank fusion or score normalization. Sparse retrieval is *more* important here than in conceptual lanes; do not weight dense above 0.7.

## Re-ranking

Re-rank top-20 candidates by:

1. exact match on package name in user query (boost ≥1.5)
2. matching OS scope to user OS if known (boost ≥1.2)
3. matching cluster to the inferred cluster from the symptom (boost ≥1.3)
4. recency of the underlying source pack (mild boost; do not let recency outrank exactness)

## Do not embed as text

- `lane_profile.json` — control file, not retrievable content
- `vol1_lane_manifest.json` — control file
- `GAP_AUDIT_AND_VOL2_QUEUE.md` — roadmap, not canonical answer material (index only for maintenance queries)
- duplicate maps unless auditing
- raw manifests unless the query is about archive structure
- generated report counts without their source path
- old version labels as current truth
- code files without code-aware chunking

## Retrieval test

For any new chunk, run the QA prompts in `QA_TEST_PROMPTS.md` against the index. A pass means:

- diagnostic prompts return the matching cluster card in top-3
- volatile-fact prompts return the card *and* its `volatile_needs_recheck` flag is preserved in the retrieved metadata
- exact-name queries (e.g. "bitsandbytes Windows") return the relevant card in top-1
- a good retrieval result includes at least one conceptual chunk and one provenance chunk when the user asks for a technical or operational decision
