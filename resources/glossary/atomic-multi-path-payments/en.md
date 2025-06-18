---
term: ATOMIC MULTI-PATH PAYMENTS
---

Improved version of MPP (*Multi-Path Payments*) where each payment fragment has a distinct partial secret, ensuring that the transaction is settled atomically, i.e. in full or not at all.

MPPs are payment techniques on Lightning that enable a transaction to be broken down into several smaller parts and routed via different routes. In other words, each payment fraction takes a different node path. This circumvents liquidity limitations on a single channel in the route. In basic MPPs, each payment fraction shares the same secret, and therefore the same Hash in HTLCs. This can make the transaction traceable if an observer is present on several routes, as he can link all these identical secrets together. What's more, because the secret is unique for all parts of the payment, it is not atomic. This means that some parts of the payment may be executed successfully, while others may fail.

In AMP, unique partial secrets are used for each fraction. Once all the fragments have been received, they enable the recipient to reconstruct the original general secret and claim the full payment. This method makes partial settlement of the payment impossible, as possession of all the partial secrets is required to unlock the full payment. This ensures that the payment is fully successful or fully unsuccessful (i.e., atomic). AMP also improves confidentiality, as there are no longer any visible links between different routes.

One advantage of AMPs is that they work even if only the receiver and sender have implemented this method. Intermediary nodes process these payments as conventional transactions using HTLCs, unaware that they are processing fractions of a larger payment.