---
term: UTXO

---
Acronym for *Unspent Transaction Output*. An UTXO is a transaction output that has not yet been spent, meaning it has not been used as an input for a new transaction. UTXOs represent the fraction of bitcoins that a user owns and are currently available to be spent. Each UTXO is associated with a specific output script (`scriptPubKey`), which defines the necessary conditions to spend the bitcoins. Transactions in Bitcoin consume these UTXOs as inputs and create new UTXOs as outputs. The UTXO model is fundamental to Bitcoin, as it allows for easy verification that transactions are not attempting to spend bitcoins that do not exist or have already been spent.