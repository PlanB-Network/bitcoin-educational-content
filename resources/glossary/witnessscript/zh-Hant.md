---
term: WITNESSSCRIPT
---

指定可以從 P2WSH 或 P2SH-P2WSH UTXOs 支出比特幣的條件的腳本。通常，`witnessScript` 決定了 SegWit 標準下多重簽章 Wallet 的條件。在這些腳本標準中，UTXO (輸出) 的 `scriptPubKey` 包含 `witnessScript` 的 Hash。要在新的交易中使用此 UTXO 作為輸入，持有人必須公開原始的 `witnessScript` 以證明其與 `scriptPubKey` 中的指紋相符。然後 `witnessScript` 必須包含在交易的 `scriptWitness` 中，其中也包含驗證腳本所需的 Elements，例如簽名。因此，對 SegWit 而言，`witnessScript` 等同於 P2SH 交易中的 `redeemscript`，不同之處在於它是放在交易的見證中，而不是放在 `scriptSig` 中。


> ► *注意，"witnessScript 「不應與 」scriptWitness "混淆。雖然 `witnessScript` 定義了 P2WSH 或 P2SH-P2WSH UTXO 的支出條件，本身就構成一個腳本，但 `scriptWitness` 包含任何 SegWit 輸入的見證資料。