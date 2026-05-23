# QA Test Prompts — ComfyUI Workflow API Automation and Gradio Bridge Patterns

Use these prompts to test whether the adapter can guide a ComfyUI automation assistant.

1. I exported my ComfyUI workflow but posting it to `/prompt` fails. What format should I use?
2. Build me the basic Python pattern to queue a ComfyUI prompt and change the positive prompt text first.
3. How do I get the generated image back after I queue a workflow through the API?
4. I want a Gradio app with prompt, seed, input image, and output image. What is the clean architecture?
5. How should I handle multiple users so one user does not see another user's output?
6. Should I poll `/history` or use WebSocket updates for progress?
7. How do I upload an image for an img2img or inpaint workflow before queueing the prompt?
8. What errors should I show when ComfyUI rejects the prompt?
9. What is the difference between local `/prompt` and cloud `/api/prompt`?
10. How do I avoid overloading my 16GB GPU from a Gradio front end?
