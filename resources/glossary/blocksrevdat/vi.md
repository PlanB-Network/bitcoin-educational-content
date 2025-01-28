---
term: BLOCKS/REV*.DAT

---
Name of the files in Bitcoin Core that store the information needed to potentially reverse the changes made to the UTXO set by previously added blocks. Each file is identified by a unique number that is the same as the blk*.dat file it corresponds to. The rev*.dat files contain the reversal data corresponding to the blocks stored in the blk*.dat files. This data is essentially a list of all the UTXOs spent as inputs in a block. These reversal files allow the node to revert to a previous state in case of a blockchain reorganization that causes previously validated blocks to be discarded.