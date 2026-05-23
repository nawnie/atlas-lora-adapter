# QA Test Prompts — CFG, Denoise, Img2Img, and Inpainting Theory

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** Why did my inpaint replace too much?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** What denoise range should I use for face-safe restoration?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** When should I crop-and-stitch instead of full-frame inpaint?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
