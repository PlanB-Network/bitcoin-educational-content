---
term: WTXID

---
传统 TXID 的扩展，包括 SegWit 引入的见证数据。TXID 是交易数据（不包括见证数据）的哈希值，而 WTXID 是整个交易数据（包括见证数据）的 `SHA256d` 哈希值。WTXID 存储在一棵独立的哈希树中，其根位于 coinbase 交易中。这种分离可以消除 TXID 的交易可熔融性。
