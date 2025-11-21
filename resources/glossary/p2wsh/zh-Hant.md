---
term: P2WSH
---

P2WSH 代表 *Pay to Witness Script Hash*。它是用於在 UTXO 上建立支出條件的標準腳本模型。P2WSH 是在 2017 年 8 月實施 SegWit 時引入的。


這個腳本與 P2SH (*Pay to Public Script Hash*)類似，因為它也是根據腳本的 Hash 來鎖定比特幣。不同之處在於交易中如何包含簽名和腳本。要在這類腳本上花費比特幣，收款人必須提供原始腳本，稱為 `witnessScript` (相當於 `redeemscript`)，以及所需的簽名。這種機制允許實現更複雜的花費條件，例如多重簽名。


在 P2WSH 的情況下，簽章腳本資訊 (`scriptWitness`，等同於 `scriptSig`)會從傳統的交易結構移至稱為 `Witness` 的獨立部分。這個移動是 SegWit (*Segregated Witness*) 更新的一項功能，有助於防止簽名的可篡改性。與傳統交易相比，P2WSH 交易的費用通常較低，因為見證人中的部分費用較低。


P2WSH 位址使用 `Bech32` 編碼與 BCH 碼形式的校驗和書寫。這些位址總是以 `bc1q` 開頭。P2WSH 是版本 0 的 SegWit 輸出。