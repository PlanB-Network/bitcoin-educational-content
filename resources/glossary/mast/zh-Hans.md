---
term: MAST
---

缩写“Merkelised Alternative Script Tree（默克尔化替代脚本树）”。这是一种技术，使用Merkle树来总结用户在接收地址中选择的任意数量的消费条件，其中必须满足一个条件才能花费所关注的比特币。Merkle树允许用户选择他们希望满足的条件，而无需在区块链上透露其他条件的细节。这有助于减少与这些脚本相关的费用，创建更复杂的条件，并且随着时间的推移，提高用户隐私（加上使用Schnorr签名）。这个概念是几个提案的主题，但最终通过2021年的Taproot软分叉被添加到比特币中。

> ► *最初，“MAST”代表“Merklized Abstract Syntax Tree（默克尔化抽象语法树）”。在Taproot框架内的使用不再涉及“抽象语法树”。然而，用户继续使用MAST这个术语。因此，Anthony Towns提议在保留这个广泛使用的缩写的同时，改变原始含义为：“Merklized Alternative Script Tree（默克尔化替代脚本树）”。*