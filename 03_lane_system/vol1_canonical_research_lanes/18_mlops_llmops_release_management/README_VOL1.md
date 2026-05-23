# MLOps, LLMOps, and Release Management — Vol. 1 Lane

## Lane ID
`18_mlops_llmops_release_management`

## Purpose
Define versioned release discipline for AI systems: prompts, datasets, models, evals, deployments, monitoring, rollbacks, and change logs.

## Machine-use summary
LLMOps extends MLOps into prompt, retrieval, tool, model, and evaluation versioning. The assistant should treat each AI app release as a bundle: model version, prompt version, retrieval index version, dataset version, eval result, config, and rollback path. The adapter itself should follow this discipline.

## How an AI assistant should use this lane
- Retrieve this lane when user asks about mlops, llmops, and release management concepts, implementation decisions, risks, or architecture tradeoffs.
- Prefer this lane's canonical overview before raw source notes.
- Treat model rankings, current tools, and vendor claims as fast-moving unless source freshness says otherwise.
- For answerable implementation questions, combine this lane with relevant app, deployment, data, or safety lanes.

## Primary related lanes
- `02_atlas_architecture_chunking_embedding`
- `11_gradio_ui_research`
- `24_ai_application_architecture`
