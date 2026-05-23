# QA Test Prompts — ComfyUI Advanced Workflow Design Patterns

1. A user has a giant restore + inpaint + upscale workflow and wants it to feel like an app. Explain how to organize it.
2. A user wants optional branches but does not want the unused branch to load models. Explain switch vs soft switch vs lazy evaluation.
3. A user asks whether bypass is the same as runtime routing. Explain the difference.
4. A user wants to ship reusable upscale and inpaint sections with a node pack. Explain subgraph blueprints and workflow templates.
5. A user wants old workflows to survive a node rename and input refactor. Explain node replacement.
6. A user wants to drive a workflow from Gradio with only five settings exposed. Explain workflow-as-app contracts.
7. A user wants nested subgraphs and a frontend extension. Explain why subgraph node identifiers require care.
