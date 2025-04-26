---
term: ASICBOOST

---
ASICBOOST is an algorithmic optimization method invented in 2016, designed to increase the efficiency of Bitcoin mining by about 20% by reducing the amount of calculations needed for each hash attempt of the header. This technique exploits a feature of the SHA256 hash function, used for mining, which divides the data into blocks before processing them. ASICBOOST retains one of these blocks unchanged across multiple hashing attempts, allowing the miner to only do part of the work for this block over several attempts. This data sharing enables the reuse of results from previous calculations, thereby reducing the total number of calculations needed to find a valid hash.

ASICBOOST can be used in two forms: Overt ASICBOOST and Covert ASICBOOST. The Overt ASICBOOST form is visible to everyone, as it involves using the `nVersion` field of the block as a nonce, and not altering the real `Nonce`. The Covert form seeks to hide these modifications by using Merkle trees. However, this second method has become less effective since the introduction of SegWit due to the second Merkle tree, which increases the number of calculations needed to use it.

In summary, ASICBOOST allows miners not to have to perform a true complete SHA256 for all hashing attempts, as part of the result remains unchanged, which speeds up the work of miners.