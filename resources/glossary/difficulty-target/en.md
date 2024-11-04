---
term: DIFFICULTY TARGET
---

The difficulty factor, also known as the difficulty target, is a parameter used in the consensus mechanism by proof of work (Proof of Work, PoW) on Bitcoin. The target represents a numerical value that determines the difficulty for miners to solve a specific cryptographic problem, called proof of work, when creating a new block on the blockchain.

The difficulty target is an adjustable 256-bit (64 bytes) number determining an acceptability limit for the hashing of block headers. In other words, for a block to be valid, the hash of its header with `SHA256d` (double `SHA256`) must be numerically lower or equal to the difficulty target. The proof of work consists of modifying the `nonce` field of the block header or the coinbase transaction until the resulting hash is lower than the target value.

This target is adjusted every 2016 blocks (approximately every two weeks), during an event called "adjustment." The difficulty factor is recalculated based on the time it took to mine the previous 2016 blocks. If the total time is less than two weeks, the difficulty increases by adjusting the target downwards. If the total time is more than two weeks, the difficulty decreases by adjusting the target upwards. The goal is to maintain an average mining time of 10 minutes per block. This time between each block helps to prevent divisions of the Bitcoin network, resulting in a waste of computing power. The difficulty target is found in each block header, within the `nBits` field. Since this field is reduced to 32 bits and the target is actually 256 bits, the target is compacted into a less precise scientific format.

![](../../dictionnaire/assets/34.webp)

> ► *The difficulty target is sometimes also called the "difficulty factor." By extension, it can be referred to with its encoding in the block headers with the term "nBits."*