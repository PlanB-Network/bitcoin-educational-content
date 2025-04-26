---
term: RECOVERY PATH

---
In a wallet software using Miniscript, such as Liana for example, the recovery paths refer to sets of keys that only become operational after a defined period of inactivity in the script that locks the bitcoins (timelock). Recovery paths are usable only once the timelocks have expired, thus offering a method of recovering funds when the primary path is not available. Consider the example of a script that incorporates 2 distinct keys: key A, which authorizes the immediate spending of bitcoins, and key B, which allows spending them after a delay defined by a timelock of 52,560 blocks. In this example, key A comes from the primary path, while key B comes from the recovery path.