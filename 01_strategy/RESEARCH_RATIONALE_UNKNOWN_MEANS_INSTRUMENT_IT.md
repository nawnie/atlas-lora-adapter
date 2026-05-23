# Research Rationale: Unknown Means Instrument It

Status: active rationale  
Version added: v0.2.9-dev18  
Date: 2026-05-22

## Core idea

This project is valuable because the outcome is not already known.

If the result were obvious, this would only be implementation work.

The current honest status is:

```text
the mechanism is plausible
the outcome is unknown
the failure modes are measurable
the result teaches something either way
```

That is enough to justify the experiment.

## The working question

```text
Can a small adapter learn the behavior of reading an Atlas,
while the Atlas itself keeps the knowledge?
```

This is deliberately narrower than:

```text
Can small models replace large models?
```

The project is not trying to prove that.

## Why lower odds are useful

Lower odds are not a reason to stop.

Lower odds are a reason to instrument the test.

The useful uncertainty is here:

```text
Can the LoRA learn map-reading behavior separately from facts?
Can that behavior transfer?
Can a structured context pack reduce small-model confusion?
Can source rules and exactness guards be learned as behavior?
```

These are answerable questions.

They require run logs, not slogans.

## What success would mean

A useful success would be limited and measurable:

```text
Atlas RAG + LoRA beats Atlas RAG alone
on at least one target behavior
without worsening source discipline or exactness.
```

Target behaviors:

- lane routing;
- card use;
- distractor rejection;
- exactness guard behavior;
- freshness handling;
- compact answer format.

## What failure would mean

Failure is not waste.

A failure could show that:

```text
the Atlas structure helps but the LoRA adds nothing
the LoRA learns formatting instead of routing
the training data is too scaffold-like
the model is too small
the context pack is too rigid
the evaluation design needs better questions
```

Those are useful results.

## Current project status

```text
seed lanes: 18
seed cards: 216
citation records: 26
installed on target PC: no
adapter trained: no
evaluation completed: no
performance wins claimed: no
```

## Research posture

The project should say:

```text
We do not know.
We built a test bench.
We will run it.
We will publish what happened.
```

The project should not say:

```text
We proved it.
The adapter works.
Small models are solved.
The method wins.
```

## AIWF phase motto

```text
Unknown does not mean impossible.
Unknown means instrument it.
```

This line is a research posture, not a result claim.

## Why this belongs in AI Without Fear

AI Without Fear is not about pretending AI is easy.

It is about making AI systems survivable, teachable, and testable.

This project fits because it does not ask users to trust the model blindly.

It asks the model to follow a map, then records whether it actually did.
