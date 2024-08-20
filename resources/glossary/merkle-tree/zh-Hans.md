---
term: MERKLE TREE
---

Merkle树是一种加密累加器。它是一种证明给定信息片段属于更大集合的方法。这是一种数据结构，便于以紧凑的格式验证信息。在比特币系统中，Merkle树被用来将一个区块的交易分组并压缩成一个单独的哈希值，称为Merkle根（或“*根哈希*”）。每一笔交易都会被哈希处理，然后相邻的哈希值会层次化地合并处理，直到得到Merkle根。

![](../../dictionnaire/assets/1.png)

这种结构允许快速验证特定交易是否包含在给定区块中，而无需分析所有交易。例如，如果我只有Merkle根，而我想验证`TX 7`确实是树的一部分，我只需要以下证明：
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`。
有了这些信息，我就能计算出中间节点直到Merkle根。

![](../../dictionnaire/assets/2.png)

Merkle树特别用于轻节点（被称为"SPV"），这些节点只保留区块头部，而不是交易。这种结构也出现在UTREEXO协议中，该协议允许压缩节点的UTXO集合，并且在MAST Taproot中也有应用。

> ► *Merkle树以设计这种结构的密码学家Ralph Merkle的名字命名，成立于1979年。Merkle树也可以被称为“哈希树”。在法语中，它被称为"Arbre de Merkle"或"arbre de hachage"。*