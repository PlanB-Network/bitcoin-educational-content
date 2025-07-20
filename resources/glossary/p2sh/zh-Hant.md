---
term: P2SH
---

P2SH 代表 * 付費腳本 Hash*。它是用於在 UTXO 上建立支出條件的標準腳本模型。P2PK 和 P2PKH 腳本的支出條件是預先定義的，與此不同，P2SH 允許在交易腳本中整合任意的支出條件和附加功能。


技術上來說，在 P2SH 交易中，`scriptPubKey` 包含`redeemscript`的加密 Hash，而不是明確的支出條件。這個 Hash 是使用 `SHA256` Hash 得到的。當向 P2SH Address 發送比特幣時，底層的 `redeemscript` 不會被透露。交易中只包含其 Hash。P2SH 位址以 `Base58Check` 編碼，並以數字 `3` 開頭。當收件人想要花掉收到的 bitcoins 時，他們必須提供一個與 `scriptPubKey` 中的 Hash 匹配的 `redeemscript`，以及滿足這個 `redeemscript`條 件的必要資料。例如，在 P2SH 多重簽名腳本中，腳本可能需要來自多個私人金鑰的簽名。


使用 P2SH 提供了更大的靈活性，因為它允許在寄件者不知道細節的情況下建構任意的腳本。P2SH 於 2012 年隨 BIP16 推出。