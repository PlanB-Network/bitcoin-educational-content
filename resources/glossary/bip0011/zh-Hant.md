---
term: BIP0011
---

BIP 由 Gavin Andresen 於 2012 年 3 月提出，建議在 Bitcoin 上建立多重簽名交易的標準方法。此提案旨在透過要求多重簽名來驗證交易，以加強比特幣的安全性。BIP11 引入了一種新的腳本類型，命名為「M-of-N Multisig」，其中 `M` 代表從 `N` 潛在公開密鑰中所需的最少簽名數量。此標準使用 `OP_CHECKMULTISIG` opcode，此 opcode 已存在於 Bitcoin，但之前不符合節點的標準化規則。雖然這種類型的腳本不再常用於實際的 Multisig 錢包，而傾向於 P2SH 或 P2WSH，但其使用仍然是可能的。它主要用於 Stamps 等元協定。但是，節點可以使用參數 `permitbaremultisig=0`，選擇不中繼這些 P2MS 交易。


> ► *現今此標準稱為「bare-Multisig」或「P2MS」。