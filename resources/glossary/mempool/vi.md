---
term: MEMPOOL

---
A contraction of the terms "memory" and "pool". This refers to a virtual space in which Bitcoin transactions awaiting inclusion in a block are grouped together. When a transaction is created and broadcast on the Bitcoin network, it is first verified by the network's nodes. If it is deemed valid, it is then placed in the Mempool of each node, where it remains until it is selected by a miner to be included in a block.

It is important to note that each node in the Bitcoin network maintains its own Mempool, and therefore, there can be variations in the content of the Mempool between different nodes at any given time. Notably, the `maxmempool` parameter in the `bitcoin.conf` file of each node allows operators to control the amount of RAM (random access memory) that their node will use to store pending transactions in the Mempool. By limiting the size of the Mempool, node operators can prevent it from consuming too many resources on their system. This parameter is specified in megabytes (MB). The default value for Bitcoin Core to date is 300 MB.

Transactions present in the Mempool are provisional. They should not be considered immutable until they are included in a block, and after a certain number of confirmations. These can often be replaced or purged.