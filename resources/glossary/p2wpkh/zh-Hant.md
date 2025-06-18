---
term: P2WPKH
---

P2WPKH 代表 * 付費見證公開金鑰 Hash*。它是一個標準的腳本模型，用於建立 UTXO 的支出條件。P2WPKH 是在 2017 年 8 月實施 SegWit 時引入的。


這個腳本類似 P2PKH (*Pay to Public Key Hash*)，因為它也是根據公開金鑰的 Hash 來鎖定比特幣，也就是接收 Address。不同之處在於交易中如何包含簽名和腳本。在 P2WPKH 的情況下，簽名腳本資訊 (`scriptSig`)從傳統的交易結構移到一個叫做`Witness`的獨立部分。這個移動是 SegWit (*Segregated Witness*) 更新的特色，有助於防止簽章的可篡改性。與傳統交易相比，P2WPKH 交易的費用通常較低，因為見證人中的部分費用較低。


P2WPKH 位址使用 `Bech32` 編碼與 BCH 碼形式的校驗和書寫。這些位址總是以 `bc1q` 開頭。P2WPKH 是版本 0 的 SegWit 輸出。