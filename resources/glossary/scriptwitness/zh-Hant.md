---
term: 劇本見證人
---

SegWit 交易條目中的一個元素，包含解鎖交易中發送的比特幣所需的簽名和公開密鑰。類似於 Legacy 交易的 `scriptSig`, `scriptWitness` 並非放置在相同的位置。事實上，正是這個被稱為 「見證」（英文中的 "*witness*"）的部分，被移到了一個單獨的資料庫中，以解決交易的延展性問題。每個 SegWit 輸入都有自己的`scriptWitness`，而所有的`scriptWitness` Elements 一起構成了交易的`Witness`欄位。


> ► *小心不要混淆`scriptWitness`和`witnessScript`。雖然 `scriptWitness` 包含任何 SegWit 輸入的見證資料，但 `witnessScript` 定義了 P2WSH 或 P2SH-P2WSH UTXO 的支出條件，本身就構成一個腳本，類似於 P2SH 輸出的 `redeemscript`* 。