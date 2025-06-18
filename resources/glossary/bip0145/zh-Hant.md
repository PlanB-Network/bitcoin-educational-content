---
term: BIP0145
---

根據 BIP141 更新 JSON-RPC call `getblocktemplate` 以納入對 SegWit 的支援。此更新允許礦工透過考慮 SegWit 引入的交易和區塊的新 「權重 」測量，以及其他參數（例如 sigops 限制的計算）來構建區塊。