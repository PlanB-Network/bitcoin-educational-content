---
term: Blocks/rev*.dat
definition: Files storing undo data to allow for returning to a previous state of the UTXO set.
---

Name of the files in Bitcoin Core that store the data needed to undo the changes made to the UTXO set by previously added blocks. Each file is identified by a unique number matching the corresponding blk*.dat file. 
The rev*.dat files contain undo data, essentially listing all the UTXOs spent as inputs in the block. 
These undo files enable the node to revert to a previous state in the event of a blockchain reorganization (reorg) that causes previously valid blocks to be discarded.
