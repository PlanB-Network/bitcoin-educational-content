---
term: DANDELION
---

A proposal aimed at improving the privacy of transaction routing in the Bitcoin network to counteract deanonymization. In the standard operation of Bitcoin, transactions are immediately broadcast to multiple nodes. This phenomenon can potentially allow observers to link transactions, normally anonymous, with IP addresses. The goal of BIP156 is to address this issue. To do this, it introduces an additional phase in the broadcast process to preserve anonymity before public propagation. Thus, Dandelion first uses a "stem" phase where the transaction is sent through a random path of nodes, before being broadcast to the entire network in the "fluff" phase. The stem and fluff are references to the behavior of the transaction's propagation through the network, resembling the shape of a dandelion. This routing method obscures the trail leading back to the source node, making it difficult to trace a transaction through the network back to its origin.

![](../../dictionnaire/assets/36.webp)

