# Confidence and Answer Gating

This file tells an AI assistant when it should answer, qualify, or refuse to speculate.

## High confidence

Answer directly when retrieved context includes:

- a canonical lane overview or Atlas card matching the question
- exact node/package/path/model names
- source coverage notes that support the recommendation
- no unresolved conflict in the retrieved material

## Medium confidence

Answer with caveats when:

- the retrieved material is relevant but older
- multiple lanes overlap
- the source is a report rather than a canonical lane
- exact version compatibility is unclear
- the question asks for best/current/newest and the adapter may be stale

## Low confidence

Do not guess. Say what is missing when:

- no lane covers the subject
- only expansion slots exist
- the retrieved content contradicts itself and no priority rule resolves it
- exact class type, package name, model license, or command syntax is unknown
- an answer could break an install, workflow, or environment

## Gating rules for code and commands

For runnable instructions:

1. Prefer PowerShell on Windows unless the user asks otherwise.
2. Include dry-run or reversible steps when possible.
3. Do not recommend deleting files unless the adapter or user context clearly supports it.
4. For pip/venv issues, prefer isolated environments over global installs.
5. For ComfyUI custom nodes, check whether ComfyUI-Manager or a known node pack already covers the need before recommending new code.

## Gating rules for workflow JSON

For ComfyUI workflow generation:

1. Use verified class type names only.
2. Treat links as source of truth.
3. Prefer minimal working graphs before adding optional features.
4. Preserve model path conventions.
5. Do not fabricate custom node sockets.
6. When socket schema is unknown, ask for an exported node snippet or retrieve a verified source.
