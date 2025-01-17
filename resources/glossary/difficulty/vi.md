---
term: DIFFICULTY

---
An adjustable parameter that determines the complexity of the proof of work required to add a new block to the blockchain and earn the associated reward. This difficulty is represented by the difficulty target, a 256-bit value that sets the upper limit that the block header's hash must meet to be considered valid. The goal is for the hash, achieved through a double execution of SHA256 (SHA256d), to be less than or equal to this target. To reach this hash, miners manipulate the `nonce` in the block header. The difficulty adjusts every 2016 blocks, or approximately every two weeks, to maintain the average block creation time at about 10 minutes.