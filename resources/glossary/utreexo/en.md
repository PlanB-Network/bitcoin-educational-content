---
term: UTREEXO
---

Protocol designed by Tadge Dryja to compact the Bitcoin nodes' UTXO set using an accumulator based on Merkle trees. Unlike the classic UTXO set which requires significant storage space, Utreexo drastically reduces the memory needed by only storing the Merkle tree roots. This allows the node to verify the existence of UTXOs used in transaction inputs, without having to keep the complete set of UTXOs. By using Utreexo, each node only retains a cryptographic fingerprint called a Merkle root. When a transaction is made, the user provides the proofs of ownership of the UTXOs and the corresponding Merkle paths. Thus, the node can verify transactions without storing the entire UTXO set. Let's take an example with a diagram to understand this mechanism:

![](../../dictionnaire/assets/15.webp)

In this example, I intentionally reduced the UTXO set to 4 UTXOs to facilitate understanding. In reality, it's important to imagine that there are almost 140 million UTXOs on Bitcoin at the time of writing these lines. In this diagram, the Utreexo node would only need to keep the Merkle Root in RAM. If it receives a transaction spending UTXO No. 3 (in black), the proof would consist of the following elements:
* UTXO 3;
* HASH 4;
* HASH 1-2.

With this information transmitted by the transaction sender, the Utreexo node performs the following verifications:
* It calculates the imprint of UTXO 3, which gives it HASH 3;
* It concatenates HASH 3 with HASH 4;
* It calculates their imprint, which gives it HASH 3-4;
* It concatenates HASH 3-4 with HASH 1-2;
* It calculates their imprint, which gives it the Merkle root.

If the Merkle root it obtains through its process is the same as the Merkle root it stored in its RAM, then it is convinced that UTXO No. 3 is indeed part of the UTXO set.
This method reduces the RAM requirements for full node operators. However, Utreexo has limitations, including an increase in block size due to additional proofs and the potential dependence of Utreexo nodes on Bridge Nodes to obtain missing proofs. Bridge Nodes are traditional full nodes that provide the necessary proofs to Utreexo nodes, thus allowing full verification. This approach offers a compromise between efficiency and decentralization, making transaction validation more accessible to users with limited resources.
