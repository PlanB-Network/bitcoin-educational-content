---
term: GOSSIP
---

Gossip is a peer-to-peer (P2P) distributed algorithm for disseminating information epidemically to all network agents. For Bitcoin, Lightning and other distributed systems, this protocol enables the global state of nodes to be exchanged and synchronized in just a few cycles. Each node propagates information to one or more random or non-random neighbors, who in turn propagate the information to other neighbors, and so on, until a globally synchronized state is reached.

In Lightning, gossip is a communication protocol between nodes to share information on the current state and topology of the network. The gossip protocol enables nodes to know the dynamic state of payment channels and other nodes, to facilitate the routing of transactions across the network without requiring direct connections between all nodes.

> ► *In French, "gossip protocol" could be translated as "protocole de bavardage". Source : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*