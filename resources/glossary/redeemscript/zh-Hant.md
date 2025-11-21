---
term: redeemscript
---

定義輸入必須符合特定條件才能解鎖與 P2SH 輸出相關的資金的腳本。在 P2SH UTXO 中，`scriptPubKey` 包含`redeemscript`的 Hash。當交易希望將此 UTXO 作為輸入使用時，它必須提供與`scriptPubKey`中包含的 Hash 相匹配的清晰`redeemscript`。因此，在輸入的 `scriptSig` 中會提供 `redeemscript` 以及其他滿足腳本條件所需的 Elements，例如簽名或公開金鑰。這種封裝的結構可以確保在比特幣真正被花掉之前，花費條件的細節是隱藏的。它主要用於 Legacy P2SH 多重簽名錢包。