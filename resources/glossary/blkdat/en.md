---
term: Blk*.dat
definition: Files in Bitcoin Core storing raw data of blockchain blocks.
---

Name given to the files in Bitcoin Core that store the raw block data of the blockchain. Each file is identified by a unique number in its filename. 
Blocks are stored in chronological order, starting with blk00000.dat. When this file reaches its maximum capacity, the following blocks are recorded in blk00001.dat, then blk00002.dat, and so on. 
Each blk file has a maximum capacity of 128 mebibytes (MiB), equivalent to a little over 134 megabytes (MB). These files have been moved to the `/blocks` folder since version 0.8.0.