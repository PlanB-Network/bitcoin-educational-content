---
term: ASICBOOST
---

ASICBOOST is an algorithmic optimization method invented in 2016, designed to improve Bitcoin mining efficiency by approximately 20% by reducing the amount of calculations required for each block header hashing attempt. This technique exploits a feature of the SHA256 hash function, used for mining, which processes data in chunks. AsicBoost keeps one of these chunks unchanged across multiple hashing attempts, allowing miners to reuse part of the previous computation, thereby lowering the total number of calculations needed to find a valid hash.

ASICBOOST can be used in two forms: Overt ASICBOOST and Covert ASICBOOST. The Overt ASICBOOST form is visible to everyone, as it involves using the `nVersion` field of the block as a nonce, without altering the standard `Nonce`. The Covert form, on the other hand, attempts to hide these modifications by using Merkle trees. However, this second method became largely ineffective after the activation of SegWit, which introduced a second Merkle tree that increases the computation cost, negating the optimization.

In summary, ASICBOOST allows miners to avoid performing a full SHA256 computation for every hash attempt by reusing a portion of the work, thereby accelerating the mining process.