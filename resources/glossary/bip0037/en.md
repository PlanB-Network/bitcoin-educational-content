---
term: BIP0037
definition: Introduction of Bloom Filters allowing light wallets (SPV) to filter transactions without downloading the entire blockchain. Criticized for its privacy flaws.
---

A proposal designed to allow lightweight wallets (*Simplified Payment Verification*) to filter transactions without having to download the entire blockchain. This method is based on the concept of Bloom Filters, probabilistic data structures that efficiently test whether an element belongs to a set. 
These filters enable SPV clients to only receive transactions relevant to their wallet, in order to reduce the bandwidth and RAM required for synchronization, especially on mobile phones. The Bloom filters are sent to a full node, which responds with Merkle blocks. These blocks contain only the filtered transactions, the block header with the Merkle root, and the branches needed to prove that these transactions are part of the Merkle tree.
BIP37 has been criticized for its privacy weaknesses, as it reveals user addresses and transactions to the full nodes being queried. To attempt to remedy this flaw, it is possible to integrate additional transactions, the "false positives", to create plausible deniability. However, the volume of false positives necessary to achieve a satisfactory level of plausible deniability remains significantly high. 
BIP37 has also been criticized for the computational load it places on full nodes and for introducing a potential denial-of-service attack vector. As a result, this feature is disabled by default in Bitcoin Core. To enable it, the parameter `peerbloomfilters=1` must be entered in the configuration file.

