---
term: BIP145

---
更新 JSON-RPC 调用 `getblocktemplate` 以根据 BIP141 加入对 SegWit 的支持。此更新允许矿工在构建区块时考虑到 SegWit 引入的交易和区块的新 "权重 "度量以及其他参数，例如 sigops 限制的计算。