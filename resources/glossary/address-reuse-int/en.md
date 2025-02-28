---
term: ADDRESS REUSE (INT)
---

Address reuse is said to be "internal" when it occurs within the same transaction both as an input and an output. In this configuration, internal address reuse is a blockchain analysis heuristic that allows for a plausible hypothesis about the transaction's change. Indeed, if there are two outputs and one of them uses the same receiving address as the input, then it is likely that the second output is leaving the initial user's possession. The output with the reused address likely represents the change.

![](../../dictionnaire/assets/10.webp)