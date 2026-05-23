# Evaluation Rubric

Score each category from 0 to 3.

## Grounding

| Score | Meaning |
|---:|---|
| 0 | Unsupported or hallucinated |
| 1 | Partially related but weakly grounded |
| 2 | Grounded in retrieved material |
| 3 | Grounded and identifies the best source layer |

## Exactness

| Score | Meaning |
|---:|---|
| 0 | Fabricates names, paths, commands, APIs, or class types |
| 1 | Approximate but risky |
| 2 | Mostly exact |
| 3 | Exact and version/freshness-aware |

## Actionability

| Score | Meaning |
|---:|---|
| 0 | Vague explanation only |
| 1 | Gives partial next step |
| 2 | Gives usable steps |
| 3 | Gives steps plus caveats/failure checks |

## Retrieval discipline

| Score | Meaning |
|---:|---|
| 0 | Ignores retrieved context |
| 1 | Uses random or weak context |
| 2 | Uses relevant context |
| 3 | Uses source priority and resolves conflicts correctly |

## Beginner safety

| Score | Meaning |
|---:|---|
| 0 | Risky/destructive advice |
| 1 | Assumes advanced knowledge without warning |
| 2 | Gives safe default |
| 3 | Gives safe default plus advanced boundary |

## Format fit

| Score | Meaning |
|---:|---|
| 0 | Wrong answer shape |
| 1 | Partially useful format |
| 2 | Appropriate format |
| 3 | Strong format with clear structure |

## Uncertainty handling

| Score | Meaning |
|---:|---|
| 0 | Pretends certainty when evidence is missing |
| 1 | Weak or vague caveat |
| 2 | Clearly states uncertainty |
| 3 | States uncertainty and gives verification path |

## Passing threshold

A response passes if:

- total score is 15 or higher out of 21;
- grounding is at least 2;
- exactness is at least 2;
- retrieval discipline is at least 2;
- no dangerous hallucinated command/path/class type appears.
