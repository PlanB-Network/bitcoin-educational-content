---
term: INPUT
---

In the context of Bitcoin, an input within a transaction refers to the UTXOs (*Unspent Transaction Outputs*) used as original funds to satisfy the outputs. Each input contains references to previous UTXOs, which will then be consumed by the transaction. These inputs are used to feed new UTXOs which will be created as outputs of the transaction, and which can then be spent in future transactions.

The role of the Bitcoin transaction is therefore to consume UTXOs as inputs, and to create new UTXOs as outputs. The difference between the two corresponds to the transaction fees that can be recovered by the miner who validates the block.

From a broader point of view, in computer science, the term "input" generally refers to data supplied to a function, algorithm or system as operands or information required to perform an operation or calculation. In this sense, the term is used more generically to describe anything supplied to a process in order to obtain a result or output. For example, when data is passed through a cryptographic hash function, this information is referred to as "input".