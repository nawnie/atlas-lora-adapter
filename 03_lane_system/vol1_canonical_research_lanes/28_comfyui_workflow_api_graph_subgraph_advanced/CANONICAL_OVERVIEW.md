# Canonical Overview

This lane covers advanced graph/workflow topics: API-format JSON, prompt submission, node IDs, links, subgraphs, reusable blueprints, and workflow-template packaging.

## API-format workflows

ComfyUI API workflows are JSON graphs. Node IDs are keys; each node stores `class_type` and `inputs`. Frontend workflows can be saved in API format for programmatic execution. For AI assistants, API format is the safest target when generating or patching workflows.

## Subgraphs

Subgraphs let users group nodes into reusable, nestable components. For node-pack distribution, subgraph blueprints can be placed in a `subgraphs` folder and discovered as reusable global components.

## Workflow templates

Custom node authors can include `example_workflows` with JSON workflows and optional thumbnails. AIWF should treat this as the bridge between machine-generated components and beginner-safe examples.

## Node IDs and subgraph IDs

Subgraph-aware frontend extension code must distinguish local node IDs, execution IDs, and locator IDs. Confusing these causes silent UI/runtime failures.
