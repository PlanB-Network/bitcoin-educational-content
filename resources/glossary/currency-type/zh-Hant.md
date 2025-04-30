---
term: 貨幣種類
---

在確定性和分層（HD）錢包的情況下，貨幣類型（英文為 *coin type*）是一個衍生層級，可根據使用的各種加密貨幣區分 Wallet 的分支。此衍生的 Layer 由 BIP 44 定義，位於衍生結構的深度 2，在主密鑰和目的之後。例如，對於 Bitcoin，分配的索引為 `0x80000000`，在衍生路徑中注為 `/0'/`。這表示從這個路徑衍生出來的所有位址和帳號都與 Bitcoin 相關聯。這種衍生的 Layer 可以在多貨幣的 Wallet 中明確區分不同的資產。以下是各種加密貨幣使用的索引：


- Bitcoin: `0x80000000`；
- Bitcoin Testnet: `0x80000001`；
- Litecoin: `0x80000002`；
- Dogecoin: `0x80000003`；
- Ethereum: `0x8000003c`...


![](../../dictionnaire/assets/21.webp)