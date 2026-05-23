# Vol. 1 Scope — ComfyUI Workflow API Automation and Gradio Bridge Patterns

## In scope

- ComfyUI local API execution concepts
- API prompt format and workflow JSON boundaries
- `/prompt`, `/history`, `/queue`, `/view`, `/upload/image`, `/system_stats`, and `/object_info` usage patterns
- WebSocket vs polling design decisions
- safe payload mutation for UI controls
- Gradio Blocks, queues, state, file uploads, and result display patterns
- local app safety and beginner-facing workflow contracts

## Out of scope

- ComfyUI Cloud billing details beyond endpoint distinction
- public Internet deployment without an auth/security layer
- custom node datatype internals covered by lane 31
- full production SaaS orchestration outside a local AIWF app pattern
- vendor-specific hosted ComfyUI platforms except as optional deployment targets

## Boundary rule

Do not tell a user to send the normal UI workflow JSON directly to the API unless it is in API format. If the exact format is unknown, instruct the user to export the workflow in API format or inspect whether nodes are keyed by node ID with `class_type` and `inputs`.
