---
term: 帳戶
---

在 HD (Hierarchical Deterministic) 錢包中，根據 BIP32，一個帳戶代表深度為 3 的衍生 Layer。每個帳戶從 `/0'/` 開始順序編號（硬化衍生，因此實際上是 `/2^31/` 或 `/2 147 483 648/`）。眾所皆知的 `xpubs` 就是位於這個衍生深度。現在，在 HD Wallet 中通常只使用一個帳戶。然而，最初的構想是在同一個 Wallet 中區分不同的使用類別。例如，如果我們使用外部 Taproot (P2TR) 接收 Address 的標準衍生路徑：`m/86'/0'/0「/0/0`，則帳戶索引就是第二個`/0」/`。


![](../../dictionnaire/assets/17.webp)