---
term: txid（交易識別碼）
---

與每個 Bitcoin 交易相關的唯一識別碼。它透過計算交易資料的 `SHA256d` Hash 產生。txid 用作參考，以便在 Blockchain 中找到特定的交易。它也用來參考 UTXO，UTXO 基本上是前一個交易的 txid 和指定輸出 (也稱為「vout」) 的索引的串接。對於 SegWit 之後的交易，txid 不再考慮交易見證，消除了延展性。