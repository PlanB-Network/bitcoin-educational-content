---
term: NODE

---
In the Bitcoin network, a node (or "node" in English) is a computer that runs a Bitcoin protocol client (such as Bitcoin Core, for example). It participates in the network by maintaining a copy of the blockchain, relaying and verifying transactions and new blocks, and optionally, participating in the mining process. The sum of all Bitcoin nodes represents the Bitcoin network itself.

There are several types of nodes in Bitcoin, including full nodes and light nodes. Full nodes keep a complete copy of the blockchain, verify all transactions and blocks according to consensus rules, and actively participate in the dissemination of transactions and blocks across the network. On the other hand, light nodes, or SPV (*Simple Payment Verification*) nodes, only keep the headers of blocks and rely on full nodes to obtain transaction information.

> ► *Some also differentiate between so-called "pruned nodes" ("pruned node" in English). These are full nodes, which download and verify all blocks from the Genesis block, but only keep the most recent blocks in memory.*