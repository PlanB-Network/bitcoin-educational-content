---
term: PRIMARY PATH

---
In a wallet software using Miniscript, such as Liana for example, the primary path refers to the set of keys allowing immediate spending of funds, without any time-based conditions. This path is always accessible and is used for the daily management of bitcoins, without requiring a wait (timelock) unlike recovery paths. Take the example of a script that incorporates 2 distinct keys: key A, which authorizes the immediate spending of bitcoins, and key B, which allows spending them after a delay defined by a timelock of 52,560 blocks. In this example, key A comes from the primary path, while key B comes from the recovery path.