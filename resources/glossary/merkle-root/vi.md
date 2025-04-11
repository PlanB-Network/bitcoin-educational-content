---
term: MERKLE ROOT

---
Digest or "top hash" of a Merkle tree, which represents a summary of all the information present in the tree. A Merkle tree is a cryptographic accumulator structure, sometimes also called a "hash tree". In the context of Bitcoin, Merkle trees are used to organize transactions within a block and to facilitate the rapid verification of the inclusion of a specific transaction. Thus, in Bitcoin blocks, the Merkle root is obtained by successively hashing transactions in pairs until only one hash remains (the Merkle root). This is then included in the header of the corresponding block. This hash tree is also found in UTREEXO, a structure that allows condensing the UTXO set of nodes, and in the MAST Taproot.