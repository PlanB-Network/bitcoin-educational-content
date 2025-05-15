---
term: ERLAY
---

Proposed network protocol to improve the efficiency of relaying unconfirmed transactions between Bitcoin nodes.

Currently, each transaction is propagated via a system in which each node broadcasts the transaction of which it is aware to all its peers. The problem is that this leads to a lot of redundancy and bandwidth usage for duplicates. Many transaction broadcasts are unnecessary, as the recipient already knows about these transactions, and each node only needs to know about each transaction once. Erlay proposes to limit by default to 8 the number of peers to which a node directly sends transactions of which it is aware, and then to use a reconciliation process based on the minisketch library to share missing transactions more efficiently.

Erlay would reduce bandwidth consumption by around 40%, making full node operation more accessible to users with limited Internet connections, and thus promoting better network decentralization. This protocol would also maintain almost constant bandwidth consumption as the number of connections increases. This means that it would be much simpler for node operators to accept a very large number of connections from their peers, which would enhance the security of the Bitcoin network by reducing the risk of partitioning, whether intentional or accidental. In addition, Erlay would make it more difficult to determine the originating node of a transaction, thus increasing confidentiality for users of nodes not operating under Tor.

Erlay is proposed in BIP330.