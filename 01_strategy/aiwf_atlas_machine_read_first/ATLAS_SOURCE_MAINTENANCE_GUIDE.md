# Atlas Source Maintenance Guide

The AIWF Atlas uses source lists as a maintenance system, not decoration. The purpose is to make updates easier, reduce stale claims, and keep the Atlas from drifting into confident nonsense.

## Start here

Use these files for source maintenance:

- `04_MANIFESTS/ATLAS_SOURCE_MASTER_INDEX.md`
- `04_MANIFESTS/ATLAS_SOURCE_DOMAIN_COUNTS_CURRENT.csv`
- `04_MANIFESTS/ATLAS_SOURCE_URL_INVENTORY_CURRENT.csv`
- `04_MANIFESTS/ATLAS_SOURCE_URL_INVENTORY_CURRENT.jsonl`

## Current counts

- Total URL references: 10973
- Unique URLs: 3429
- Unique domains: 242

## How to use the domain counts

Domain counts are update priority signals. A heavily cited domain should be checked first during release verification because a single stale vendor page or moved documentation section can affect many Atlas answers.

Domain counts are not authority scores. Official docs, primary papers, standards bodies, and source repositories still outrank blogs and summaries even when cited fewer times.

## Recommended update order

1. Official project docs and repositories.
2. Primary papers and standards.
3. Vendor docs for APIs, model files, pricing, licensing, and hardware.
4. Benchmarks and model-ranking pages.
5. Secondary explainers and blog posts.

## Atlas answer rule

When a claim is volatile, the assistant should prefer the newest verified primary source. If no primary source is available, the answer must say that the claim is provisional.
