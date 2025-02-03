---
term: TRANSACTION WITNESS

---
Refers to a component of Bitcoin transactions that was moved with the SegWit soft fork to address the issue of transaction malleability. The witness contains the signatures and public keys necessary to unlock the bitcoins spent in a transaction. In Legacy transactions, the witness represented the sum of `scriptSig` from all inputs. In SegWit transactions, the witness represents the sum of `scriptWitness` for each input, and this part of the transaction is now moved into a separate Merkle tree within the block.

Before SegWit, signatures could be slightly altered without being invalidated before a transaction was confirmed, which changed the transaction identifier. This made it difficult to build various protocols, as an unconfirmed transaction could see its identifier change. By separating the witnesses, SegWit makes transactions non-malleable, as any change in the signatures no longer affects the transaction identifier (TXID), but only the witness identifier (WTXID). In addition to solving the malleability issue, this separation allows for an increase in the capacity of each block.

> ► *In English, "témoin" is translated as "witness".*