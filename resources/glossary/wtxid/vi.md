---
term: WTXID

---
An extension of the traditional TXID, including witness data introduced with SegWit. While the TXID is a hash of the transaction data excluding the witness, the WTXID is the `SHA256d` of the entire transaction data, witness included. WTXIDs are stored in a separate Merkle tree whose root is placed in the coinbase transaction. This separation allows for the removal of the TXID's transaction malleability.