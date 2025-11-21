---
term: BIP0066
---

引入了交易中簽章格式的標準化。此 BIP 是針對 OpenSSL 處理不同系統中簽章編碼方式的差異而提出的。這種異質性會造成 Blockchain 分裂的風險。BIP66 使用嚴格的 DER 編碼 (*Distinguished Encoding Rules*) 標準化了所有交易的簽章格式。這項變更需要 Soft Fork。對於其啟動，BIP66 接著使用與 BIP34 相同的機制，要求 `nVersion` 欄位增加到版本 3，一旦達到 95% Miner 的臨界值，就拒絕所有版本 2 或更低的區塊。這個臨界值在 2015 年 7 月 4 日的區塊編號 363,725 上被跨越。