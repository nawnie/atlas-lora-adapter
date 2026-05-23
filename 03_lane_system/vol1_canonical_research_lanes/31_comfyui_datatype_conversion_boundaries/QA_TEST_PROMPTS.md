# QA Test Prompts — ComfyUI Datatype Boundaries

Use these prompts to test whether an AI assistant understands socket contracts rather than only repeating code snippets.

1. My node accepts `IMAGE`, but I want it to accept `LATENT`. What has to change besides `INPUT_TYPES`?
2. Why does my latent have a `samples` key instead of normal image channels?
3. I changed `RETURN_TYPES` to `LATENT`, but ComfyUI errors when the next node runs. What should I inspect?
4. Can I run PIL filters on a `LATENT` object?
5. How do I make a node accept either `IMAGE` or `MASK` safely?
6. Why does my mask need `unsqueeze(-1)` in some image operations?
7. When should I decode to image space before applying an effect?
8. Why is VAE encode/decode not a harmless format conversion?
9. What is the safest way to support both old image workflows and a new latent path?
10. How would you design a switch node so the unused branch does not run?
