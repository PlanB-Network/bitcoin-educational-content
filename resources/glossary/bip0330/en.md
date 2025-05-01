---
term: BIP0330
---

A proposal known as "*Erlay*", which aims to optimize the propagation of unconfirmed transactions in the Bitcoin network. Currently, transactions are broadcast to all the peers of a node, resulting in redundancy and overuse of bandwidth. BIP330 proposes to limit this broadcast to 8 peers by default, then use a reconciliation mechanism to efficiently share missing transactions. Erlay reduces bandwidth consumption by around 40%. It also avoids a linear increase in bandwidth consumption with the number of peers connected to the node.