---
term: BIP0034
definition: Soft fork requiring the inclusion of the block height in the coinbase transaction, guaranteeing the uniqueness of each block.
---

Soft fork activated in March 2013, starting from block 227,930, which introduced version 2 for Bitcoin blocks. This new block version required that the `scriptSig` of the coinbase transaction include the height of the block being created. 
This change clarified how the network agrees to modify block structure and consensus rules and also enforced the uniqueness of each block and its coinbase transaction.