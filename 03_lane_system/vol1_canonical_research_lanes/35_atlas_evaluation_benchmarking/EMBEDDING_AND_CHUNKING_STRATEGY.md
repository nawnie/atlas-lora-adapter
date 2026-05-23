# Embedding and Chunking Strategy — Evaluation Harness

## What to index

Index these by default:

- `09_EVALUATION_HARNESS/README.md`
- `09_EVALUATION_HARNESS/EVALUATION_RUBRIC.md`
- `09_EVALUATION_HARNESS/adapter_benchmark_protocol_v2_13.md`
- `09_EVALUATION_HARNESS/golden_question_sets/*.jsonl`
- `09_EVALUATION_HARNESS/expected_source_maps/*.jsonl`
- this lane’s `RETRIEVAL_CARDS.jsonl`

## What not to index by default

- raw result logs
- temporary experiment exports
- previous run artifacts
- scoring spreadsheets unless summarized
- old baseline outputs after they are superseded

## Chunking rule

Chunk by eval object, not by arbitrary token count:

- one golden question per chunk
- one rubric section per chunk
- one expected-source map row per chunk
- one benchmark condition per chunk

## Metadata to preserve

- eval_id
- lane_id
- expected_sources
- risk_level
- required_behavior
- pass_conditions
- disqualifying_errors
- model_under_test
- adapter_version
- date/day label

## Retrieval behavior

When a user asks whether the adapter is useful, retrieve the benchmark protocol and the relevant golden-question results before making claims.
