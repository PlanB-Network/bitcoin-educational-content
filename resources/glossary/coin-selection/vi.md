---
term: COIN SELECTION

---
The process by which a Bitcoin wallet software chooses which UTXOs to use as inputs to satisfy the outputs of a transaction. The method of coin selection is important because it has consequences on the cost of a transaction and the user's privacy. It often aims to minimize the number of inputs used, in order to reduce the transaction size and associated fees, while trying to preserve privacy by avoiding merging coins from different sources (CIOH). Several methods exist for coin selection, such as the *Knapsack Solver* or the *Branch-and-Bound*. When coin selection is performed manually by the user, it is referred to as “*Coin Control*”.

> ► *In English, it is referred to as "Coin Selection".*