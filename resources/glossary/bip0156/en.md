---
term: BIP0156
---

Proposal, known as Dandelion, which aims to improve the privacy of transaction routing in the Bitcoin network to counteract deanonymization. In the standard operation of Bitcoin, transactions are immediately broadcast to multiple nodes. 
If an observer can monitor each transaction relayed by each node, they may assume that the first node to send a transaction is also its origin, potentially linking normally anonymous transactions to IP addresses.

To address this, BIP156 introduces an additional phase before public broadcast to preserve anonymity.
The protocol uses two stages: 
* a “stem” phase, where the transaction is relayed through a random path of nodes, 
*and a "fluff" phase, where it is broadcast to the entire network.*

The stem and fluff are references to the behavior of the transaction's propagation through the network, resembling the shape of a dandelion.

This routing method obscures the trail leading back to the originating node, making it more difficult to trace transactions back to their source. 
Dandelion significantly improves privacy by limiting the ability of adversaries to deanonymize the network. This method is even more effective when the transaction crosses during the "stem" phase a node that encrypts its network communications, such as with Tor or *P2P Transport V2*. BIP156 has not yet been added to Bitcoin Core.
