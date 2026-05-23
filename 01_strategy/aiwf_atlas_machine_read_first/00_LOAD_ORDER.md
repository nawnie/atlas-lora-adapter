# 00 Load Order for AI Systems

Use this sequence before answering with this adapter.

1. Load `AIWF_ATLAS_PROFILE.json`.
2. Load `00_AI_READ_FIRST/ATLAS_OPERATING_CONTRACT.md`.
3. Load `00_AI_READ_FIRST/RETRIEVAL_POLICY.md`.
4. Load `00_AI_READ_FIRST/SOURCE_PRIORITY_AND_CONFLICT_RESOLUTION.md`.
5. Load `00_AI_READ_FIRST/CONFIDENCE_AND_ANSWER_GATING.md`.
6. Load `00_AI_READ_FIRST/ANSWER_STYLE_AND_CITATION_RULES.md`.
7. Use `02_RETRIEVAL_INDEX/machine_lane_index.json`, `02_RETRIEVAL_INDEX/CURRENT_LANE_SUMMARY.md`, and `04_MANIFESTS/machine_lane_index_current.json` to select likely lanes.
8. Retrieve from the relevant lane's `RETRIEVAL_CARDS.jsonl`.
9. Read the lane's `CANONICAL_OVERVIEW.md`, `CONCEPT_MAP.md`, and `SOURCE_COVERAGE.md`.
10. Only inspect raw source payloads when the canonical lane is insufficient, the user asks for provenance, or a conflict must be resolved.

Important: source archives preserve history. Do not treat every old file as current guidance. Prefer canonical lanes, current machine indexes, and source-priority rules.


## Brand Load Addendum v2.8

After loading retrieval/source policy, load:

1. `AIWF_BRAND_ROLE_MAP.md`
2. `AIWF_BRAND_VOICE_AND_POSITIONING.md`
3. `AIWF_HUMOR_AND_STYLE_GUIDE.md`
4. `11_PROMPT_PACKS/AIWF_BRAND_ALIGNED_RESPONSE_EXAMPLES.md`

Do not load raw source folders before policy and brand-role files unless the user specifically asks for provenance.
