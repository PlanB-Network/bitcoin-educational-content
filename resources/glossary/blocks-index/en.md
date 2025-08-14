---
term: BLOCKS INDEX
---

A LevelDB data structure in Bitcoin Core that catalogs metadata for all blocks. Each entry in this index provides details such as the block's identifier, the block height in the blockchain, the location of the block on disk and other metadata. 
This indexing structure enables quick location of a block on disk.
