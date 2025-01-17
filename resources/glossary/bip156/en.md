---
term: BIP156
---

Proposal, known as Dandelion, which aims to improve the privacy of transaction routing in the Bitcoin network to counteract deanonymization. In the standard operation of Bitcoin, transactions are immediately broadcast to multiple nodes. If an observer is able to see each transaction relayed by each node on the network, they might assume that the first node to send a transaction is also the originating node of that transaction, and therefore that it comes from the node's operator. This phenomenon could potentially allow observers to link transactions, normally anonymous, with IP addresses.

The goal of BIP156 is to address this issue. To do this, it introduces an additional phase in the broadcast to preserve anonymity before public propagation. Thus, Dandelion first uses a "stem" phase where the transaction is sent through a random path of nodes, before being broadcast to the entire network in the "fluff" phase. The stem and fluff are references to the behavior of the transaction's propagation through the network, resembling the shape of a dandelion (*a dandelion* in English).

This routing method obscures the trail leading back to the source node, making it difficult to trace a transaction through the network back to its origin. Dandelion thus improves privacy by limiting the adversaries' ability to deanonymize the network. This method is even more effective when the transaction crosses during the "stem" phase a node that encrypts its network communications, such as with Tor or *P2P Transport V2*. BIP156 has not yet been added to Bitcoin Core.

![](../../dictionnaire/assets/36.webp)

