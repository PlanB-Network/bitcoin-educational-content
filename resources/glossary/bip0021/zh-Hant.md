---
term: BIP0021
---

提案由 Nils Schneider 和 Matt Corallo 撰寫，以 Luke Dashjr 撰寫的 BIP20 為基礎，而 BIP20 又來自 Nils Schneider 撰寫的另一份文件。BIP21 定義了接收位址應如何在 URI（*統一資源識別碼*）中編碼，以方便付款。例如，一個遵循 BIP21 的 Bitcoin URI，其中我會要求標籤為 "*Pandul*"的人向我發送 0.1 BTC，它會是這樣的：


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


這項標準化改善了 Bitcoin 交易的使用者體驗，可點選連結或掃描 QR 代碼來啟動其參數。Bitcoin Wallet 軟體目前已廣泛採用 BIP21 標準。