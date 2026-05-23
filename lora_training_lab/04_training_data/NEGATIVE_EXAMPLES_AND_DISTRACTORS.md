# Negative Examples and Distractor Design

Status: planning / seed-build  
Version added: v0.2.9-dev3

## Why negatives matter

Atlas Reader Mini should not just learn what to answer.

It must learn what not to do.

Small models especially need explicit examples where the correct behavior is to ignore a tempting card, refuse unsupported exactness, or qualify a stale claim.

## Negative example types

### 1. Distractor card

A retrieved card looks relevant but belongs to the wrong lane.

Expected behavior:

```text
ignore the distractor
use the primary lane
explain only if needed
```

### 2. Unsupported exact identifier

The user asks for an exact command, node name, file path, or version that is not in context.

Expected behavior:

```text
say the context does not contain that exact identifier
recommend verification
do not invent it
```

### 3. Volatile claim

The user asks for current tool behavior, current model recommendations, API state, pricing, license, or version.

Expected behavior:

```text
flag as current/volatile
verify if tools are available
otherwise qualify uncertainty
```

### 4. Wrong secondary lane

The context includes a secondary-lane card, but the user question does not justify using it.

Expected behavior:

```text
stay with the primary lane
do not cross lanes just because the card is present
```

### 5. Weak source

The only support is old notes, broad placeholders, or unsourced claims.

Expected behavior:

```text
downgrade confidence
ask for better source
avoid strong claim
```

## Training rule

Every 10 records should include at least 2 records that test restraint.

Good training does not only teach the adapter to answer.

It teaches the adapter when not to answer too strongly.
