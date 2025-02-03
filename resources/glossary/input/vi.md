---
term: INPUT

---
In the context of Bitcoin, an input within a transaction refers to the UTXOs (*Unspent Transaction Outputs*) used as the source of funds to satisfy the outputs. Each input contains references to previous UTXOs, which will then be consumed by the transaction. These inputs are used to fuel new UTXOs that will be created as outputs of the transaction, and which can then be spent in future transactions.

The role of the Bitcoin transaction is thus to consume UTXOs as inputs, and to create new UTXOs as outputs. The difference between the two corresponds to the transaction fees that can be collected by the miner who validates the block.

From a broader perspective, in computing, the term "input" generally refers to data provided to a function, an algorithm, or a system as operands or information required to perform an operation or calculation. In this sense, the term is used more generically to describe anything that is provided to a process in order to obtain a result or an output. For example, when data is passed into a cryptographic hash function, this information is named "input."