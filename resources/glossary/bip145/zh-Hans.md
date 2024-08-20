---
term: BIP145
---

更新JSON-RPC调用`getblocktemplate`以包含对SegWit的支持，符合BIP141的规定。此更新允许矿工在构建区块时考虑到SegWit引入的交易和区块的新“重量”测量以及其他参数，如sigops限制的计算。