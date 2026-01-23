---
term: BIP0141
definition: 引入 SegWit（隔離見證），將簽名從交易的其餘部分分離出來，以解決延展性（malleability）問題。
---

引入了 Segregated Witness (SegWit) 的概念，其名稱為 SegWit Soft Fork。BIP141 引入了對 Bitcoin 通訊協定的重大修改，旨在解決交易可篡改性問題。SegWit 將見證 (簽章資料) 與其他交易資料分離。這種分離是透過將見證資料插入一個獨立的資料結構來達成的，並在新的 Merkle Tree 中提交，而 Merkle Tree 本身則透過 Coinbase Transaction 在區塊中被引用，這使得 SegWit 與舊版本的通訊協定相容。