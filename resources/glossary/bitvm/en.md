---
term: BitVM
definition: Protocol allowing arbitrary off-chain computations with on-chain dispute possibility, extending Bitcoin's capabilities.
---

Protocol introduced by Robin Linus in 2023, aimed at extending Bitcoin's application development capabilities. 
BitVM makes it possible to perform any computational operation off-chain and use the result to decide how the locked bitcoins are spent. It also enables on-chain dispute resolution if one party claims a fraudulent result.
This gives Bitcoin an almost Turing-complete computational capability without requiring any changes to consensus rules.
BitVM replicates the behavior of a `NAND` logic gate using the combined opcodes `OP_BOOLAND` (which replicates an `AND` gate) and `OP_NOT` (which replicates a `NOT` gate). 
A NAND gate is a "universal gate" because it can be combined to reproduce any other logic gate and, by extension, any computational circuit. The idea with BitVM is to store these `NAND` computation sequences as leaves within the MAST of a Taproot transaction.
