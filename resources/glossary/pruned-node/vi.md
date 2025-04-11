---
term: PRUNED NODE

---
A pruned node, in English "Pruned Node", is a full node that performs pruning of the blockchain. This involves progressively removing the oldest blocks, after having duly verified them, to keep only the most recent blocks. The retention limit is specified in the `bitcoin.conf` file via the `prune=n` parameter, where `n` is the maximum size taken by the blocks in megabytes (MB). If `0` is noted after this parameter, then pruning is disabled, and the node retains the blockchain in its entirety.

Pruned nodes are sometimes considered as different types of nodes from full nodes. The use of a pruned node can be particularly interesting for users facing storage capacity constraints. Currently, a full node must have almost 600 GB just for storing the blockchain. A pruned node can limit the required storage to up to 550 MB. Although it uses less disk space, a pruned node maintains a level of verification and validation similar to that of a full node. Pruned nodes therefore offer more confidence to their users in comparison with light nodes (SPV).