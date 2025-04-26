---
term: BRANCH-AND-BOUND

---
Method used for selecting inputs in the Bitcoin Core wallet since version 0.17 and invented by Murch. Branch-and-Bound (BnB) is a search to find a set of UTXOs that matches the exact amount of outputs to be fulfilled in a transaction, in order to minimize change and associated fees. Its goal is to reduce a waste criterion that takes into account both the immediate cost and the future costs expected for the change. This method is more accurate in terms of fees compared to previous heuristics like the *Knapsack Solver*. The *Branch-and-Bound* is inspired by the problem-solving method of the same name, invented in 1960 by Ailsa Land and Alison Harcourt.

> ► *This method is also sometimes named "Murch's Algorithm" in reference to its inventor.*