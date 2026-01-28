---
term: BRANCH-AND-BOUND
---

Method used for selecting inputs in the Bitcoin Core wallet since version 0.17 and invented by Murch. Branch-and-Bound (BnB) searches for a set of UTXOs that exactly matches the required transaction outputs, with the aim of minimizing change and associated fees.
Its goal is to reduce a waste metric that considers both immediate costs and the expected future costs of handling change. This method is more accurate in terms of fee optimization compared to previous heuristics like the *Knapsack Solver*. The *Branch-and-Bound* approach is inspired by the problem-solving method of the same name, invented in 1960 by Ailsa Land and Alison Harcourt.

> ► *This method is also sometimes named "Murch's Algorithm" in reference to its inventor.*