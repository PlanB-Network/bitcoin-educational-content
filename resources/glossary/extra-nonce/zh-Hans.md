---
term: EXTRA-Nonce
---

用于区块 Coinbase Transaction 的 "scriptSig "字段，除了直接在每个区块的页眉中找到的传统 Nonce 外，该字段允许测试更多的可能性，以使 Hash 低于难度目标。


修改 Coinbase Transaction 中的额外 Nonce 会改变该事务的标识符，从而改变区块中所有事务的 Merkle Root，这也会修改区块头。这样，当经典 Nonce 的范围已经用完时，Miner 可以继续搜索哈希值，而不改变其候选区块的结构。


在 Mining 数据池中，额外 Nonce 通常分为两部分：一部分由数据池生成，用于识别每个切分器；另一部分由切分器修改，用于搜索有效份额。这样，池中的不同切分器就可以同时使用整个非ces范围处理同一个候选区块，而无需在池级重复相同的工作。