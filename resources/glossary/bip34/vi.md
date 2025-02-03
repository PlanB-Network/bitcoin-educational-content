---
term: BIP34

---
Soft fork applied in March 2013, starting from block 227,930, which introduced version 2 for Bitcoin blocks. This new version requires that each block includes in the `scriptSig` of the coinbase transaction the height of the block being created. This change serves to clarify the way in which the network agrees to modify the structure of the blocks and the consensus rules. Additionally, it enforces the uniqueness of each block and each coinbase transaction.