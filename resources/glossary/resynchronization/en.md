---
term: RESYNCHRONIZATION
---

Refers to a phenomenon in which the blockchain undergoes a modification of its structure due to the existence of competing blocks at the same height. This occurs when a portion of the blockchain is replaced by another chain with a greater amount of accumulated work.

These resynchronizations are part of the natural functioning of Bitcoin, where different miners may find new blocks almost simultaneously, thus splitting the Bitcoin network into two. In such cases, the network can temporarily divide into competing chains. Eventually, when one of these chains accumulates more work, the other chains are abandoned by the nodes, and their blocks become what are called "obsolete blocks" or "orphan blocks." This process of replacing one chain with another is resynchronization.

![](../../dictionnaire/assets/9.webp)

Resynchronizations can have various consequences. First, if a user had a transaction confirmed in a block that turns out to be abandoned, but this transaction is not found in the ultimately valid chain, then their transaction becomes unconfirmed again. This is why it is advised to always wait for at least 6 confirmations to consider a transaction as truly immutable. After 6 blocks deep, resynchronizations are so unlikely that the chance of one occurring can be considered virtually nil.

Furthermore, at the global system level, resynchronizations imply a waste of the miners' computational power. Indeed, when a split occurs, some miners will be on chain `A`, and others on chain `B`. If chain `B` is eventually abandoned during a resynchronization, then all the computational power deployed by the miners on this chain is, by definition, wasted. If there are too many resynchronizations on the Bitcoin network, the overall security of the network is therefore reduced. This is partly why increasing the block size or reducing the interval between each block (10 minutes) can be dangerous.

> ► *Some bitcoiners prefer to use "orphan block" to refer to an expired block. Also, even though it's an Anglicism, in common language, a "reorganization" or a "reorg" is often preferred over "resynchronization."*