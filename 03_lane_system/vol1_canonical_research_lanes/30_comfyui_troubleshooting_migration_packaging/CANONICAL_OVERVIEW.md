# Canonical Overview

This lane covers advanced troubleshooting, node migration, packaging, source verification, and safe distribution for ComfyUI workflows and node packs.

## Troubleshooting hierarchy

Start with the default workflow and no custom nodes. Then distinguish frontend extension problems from backend/dependency problems. Use binary search to isolate the bad node pack. Preserve logs.

## Dependency safety

ComfyUI custom node ecosystems often break because one pack pins a dependency that conflicts with another. AIWF should prefer isolated environments, one-click installers that report conflicts clearly, and reports that users can paste for help.

## Node replacement and migration

When a node is renamed or deprecated, use node replacement/migration paths where available. For AI-generated workflow JSON, prefer stable class_type strings and pin custom-node source/commit where possible.

## Distribution safety

A reliable node pack includes README, install instructions, requirements, example workflows, optional subgraphs, changelog, license, source links, and smoke-test instructions.
