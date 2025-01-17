---
term: OBSOLETE (BLOCK)
---

Refers to a block without children: a valid block, but excluded from the main Bitcoin chain. It occurs when two miners find a valid block at the same chain height within a short period of time and broadcast it over the network. Nodes eventually choose only one block to include in the chain, according to the principle of the chain with the most accumulated work, rendering the other "obsolete". The process leading to the production of an obsolete block is as follows:
* Two miners find a valid block at the same chain height within a short time interval. Let's call them `Block A` and `Block B`;
* Each broadcasts their block to the Bitcoin node network. Each node now has 2 blocks at the same height. Therefore, there are two valid chains;
* Miners continue to search for proofs of work for the following blocks, but to do so, they must necessarily choose only one block between `Block A` and `Block B` on which they will mine;
* A miner eventually finds a valid block above `Block B`. Let's call it `Block B+1`;
* They broadcast `Block B+1` to the network nodes;
* Since the nodes follow the longest chain (with the most accumulated work), they will estimate that the `Chain B` is the one to follow;
* They will abandon `Block A` which is no longer part of the main chain. It has thus become an obsolete block.

![](../../dictionnaire/assets/9.webp)

> ► *In English, it is referred to as a "Stale Block". In French, it can also be called "bloc périmé" or "bloc abandonné". Although I do not agree with this usage, some bitcoiners use the term "bloc orphelin" to refer to what is actually an obsolete block.*