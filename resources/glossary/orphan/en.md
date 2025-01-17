---
term: ORPHAN
---

Theoretically, an orphan block refers to a valid block received by a node that has not yet acquired the parent block, that is, the previous one in the chain. Although valid, this block remains isolated locally as an orphan.

However, in common usage, the term "orphan block" often refers to a block without a child: a valid block, but not retained in the main Bitcoin chain. This occurs when two miners find a valid block at the same chain height within a short period and broadcast it over the network. Nodes eventually choose only one block to include in the chain, based on the principle of the chain with the most work accumulated, making the other "orphan."

![](../../dictionnaire/assets/9.webp)

> ► *Personally, I prefer to use the term "orphan block" to talk about a block without a parent and the term "stale block" to refer to a block that does not have a child. I find this more logical and understandable, although a majority of bitcoiners do not follow this usage.*