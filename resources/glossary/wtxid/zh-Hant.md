---
term: WTXID
---

傳統 txid 的延伸，包括 SegWit 引入的見證資料。txid 是不含見證資料的交易資料的 Hash，而 WTXID 則是整個交易資料的 `SHA256d`，包括見證資料。WTXID 儲存於獨立的 Merkle Tree，其根位於 Coinbase Transaction。這種分離允許移除 txid 的交易延展性。