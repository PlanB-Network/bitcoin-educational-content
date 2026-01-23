---
term: Atomic multi-path payments
definition: An enhanced version of multi-path payments on Lightning where each fragment has a distinct secret, ensuring the payment is settled in full or not at all.
---

Improved version of MPP (*Multi-Path Payments*) in which each payment fragment has a distinct partial secret, ensuring that the transaction is settled atomically, i.e. in full or not at all.

MPPs are payment techniques used on Lightning Network that enable a transaction to be broken down into several smaller parts and routed through different paths. In other words, each payment fraction takes a different route through the network. This helps bypass liquidity limitations on a single channel by distributing the payment across multiple routes.

In basic MPPs, each payment fraction shares the same secret, and therefore the same Hash in HTLCs. This can make the transaction potentially traceable, an observer present on several routes can link all these identical secrets together. Moreover, since all parts rely on the same secret, it is not atomic: some parts might succeed while others fail, resulting in an incomplete payment.

AMP solves these issues by assigning a unique partial secret to each payment fragment.  Once all the fragments have been received, they enable the recipient to reconstruct the full secret and claim the payment. This method makes partial settlement of the payment impossible, as a possession of all the partial secrets is required to unlock the payment. This ensures **atomicity**: the payment either completes fully or fails entirely. AMP also enhance privacy, as there are no longer a shared hash that links the parts across different routes.

Another advantage of AMPs is that only the sender and receiver need to support AMP; intermediate nodes handle these payments as standard HTLCs and remain unaware they're part of a larger, multipart payment.
