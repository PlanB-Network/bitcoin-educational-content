---
term: MULTI-PATH PAYMENTS (MPP)
---

A generic term for all payment techniques on Lightning that enable a transaction to be broken down into several smaller parts and routed via different routes. In other words, each payment fraction takes a different node path. This makes it possible to bypass liquidity limitations on a single channel in the route.

Multi-path payments also offer slight advantages in terms of confidentiality, as it becomes more difficult for an observer to link each payment fragment to the whole transaction. However, in its basic version, all fragments share the same secret for HTLCs, which can make the transaction traceable if an observer is present on several routes. What's more, because the secret is unique for all fractions of the payment, it is not atomic. This means that some parts of the payment may be executed successfully, while others may fail. These drawbacks are corrected with "Atomic Multi-Path Payment".