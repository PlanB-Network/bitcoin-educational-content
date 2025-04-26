---
term: MERKLE TREE
---

A Merkle Tree is a cryptographic accumulator. It's a method for proving the membership of a given piece of information within a larger set. It is a data structure that facilitates the verification of information in a compact format. In the Bitcoin system, Merkle Trees are used to group and condense the transactions of a block into a single hash, called the Merkle Root (or "*Root Hash*"). Each transaction is hashed, then the adjacent hashes are hashed together hierarchically until the Merkle Root is obtained.

![](../../dictionnaire/assets/1.webp)

This structure allows for the quick verification of whether a specific transaction is included in a given block without having to analyze all the transactions. For example, if I only have the Merkle Root and I want to verify that `TX 7` is indeed part of the tree, I would only need the following proofs:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
With these pieces of information, I am able to calculate the intermediate nodes up to the Merkle Root.

![](../../dictionnaire/assets/2.webp)

Merkle Trees are notably used for light nodes (known as "SPV") that only keep the block headers, but not the transactions. This structure is also found in the UTREEXO protocol, a protocol that allows for the condensing of the UTXO set of nodes, and in the MAST Taproot.

> ► *The Merkle Tree is named after Ralph Merkle, a cryptographer who designed this structure in 1979. A Merkle Tree can also be called a "hash tree". In French, it is referred to as "Arbre de Merkle" or "arbre de hachage".*