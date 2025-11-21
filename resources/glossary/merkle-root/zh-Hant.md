---
term: Merkle Root
---

Merkle Tree 的摘要或「頂部 Hash」，代表樹狀結構中所有資訊的摘要。Merkle Tree 是一種加密累加器結構，有時也稱為「Hash 樹」。在 Bitcoin 的情況下，Merkle 樹用來組織區塊內的交易，並方便快速驗證是否包含特定交易。因此，在 Bitcoin 區塊中，Merkle Root 是透過將成對的交易連續散列，直到只剩下一個 Hash (Merkle Root)。然後，這個 Merkle Root 就會包含在對應區塊的標頭中。這種 Hash 樹狀結構也出現在 UTREEXO（一種允許濃縮 UTXO 節點集的結構）和 MAST Taproot 中。