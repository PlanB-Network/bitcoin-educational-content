---
term: BIP0022

definition: Tiêu chuẩn JSON-RPC getblocktemplate cho phép phần mềm khai thác giao tiếp với các nút đầy đủ để xây dựng các khối.
---
BIP proposed in 2012 by Luke Dashjr that introduces a standardized JSON-RPC method for external mining interfaces, called "getblocktemplate". With the increase in mining difficulty, the use of specialized external software for producing proof of work has developed. This BIP proposes a common communication standard for the block template between full nodes and software specialized in mining. This method involves sending the entire structure of the block, rather than just the header, to allow the miner to customize it.