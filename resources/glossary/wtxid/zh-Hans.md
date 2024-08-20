---
term: WTXID
---

WTXID是传统TXID的扩展，包括了随SegWit引入的见证数据。TXID是不包括见证数据的交易数据的哈希值，而WTXID则是整个交易数据（包括见证数据）的`SHA256d`哈希值。WTXID存储在一个单独的默克尔树中，其根被放置在coinbase交易中。这种分离允许去除TXID的交易可变性。