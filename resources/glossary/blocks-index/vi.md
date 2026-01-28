---
term: Chỉ mục khối

definition: Cấu trúc LevelDB trong Bitcoin Core lập danh mục siêu dữ liệu và vị trí của các khối.
---
A LevelDB data structure in Bitcoin Core that catalogs metadata about all blocks. Each entry in this index provides details such as the block's identifier, its height in the blockchain, the pointer to the block in the database, and other metadata. This indexing allows for the quick retrieval of a stored block in memory.