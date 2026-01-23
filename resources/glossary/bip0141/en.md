---
term: BIP0141
definition: Introduction of SegWit (Segregated Witness), separating signatures from the rest of the transaction to solve malleability.
---

BIP141 introduced the concept of Segregated Witness (SegWit), which gave its name to the SegWit soft fork.
It represents a major modification to the Bitcoin protocol designed to fix the transaction malleability problem.

SegWit separates the witness data (signatures) from the rest of the transaction data by placing it into a distinct data structure.
This witness data is committed to a new Merkle tree, which is then referenced in the block via the coinbase transaction, ensuring backward compatibility with older versions of the protocol.