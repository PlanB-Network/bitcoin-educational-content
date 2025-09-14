---
term: BIP0152
---

BIP152, known as “Compact Block Relay,” aims to reduce the bandwidth required for block transmission over the Bitcoin network. 
Adopted in November 2016 with Bitcoin Core version 0.13.0, this protocol enables compact communication of block data, based on the assumption that nodes already hold most transactions of a recently mined block in their mempool.
Instead of transmitting each transaction in full, which would result in duplication, BIP152 proposes sending only short identifiers for transactions already known to peers, accompanied by a few selected transactions (notably the coinbase transaction and those the node is likely not to know). The node can then request any missing transactions from its peers. Compact Block Relay thus decreases the amount of data exchanged during block propagation, which reduces bandwidth spikes and improves the overall efficiency of the network.