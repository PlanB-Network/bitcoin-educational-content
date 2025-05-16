---
term: P2SH-P2WPKH
---

P2SH-P2WPKH 代表 * 付費給腳本 Hash - 付費給見證公開金鑰 Hash*。它是一個標準的腳本模式，用來建立 UTXO 的支出條件，也稱為「巢狀 SegWit」。


P2SH-P2WPKH 是在 2017 年 8 月實施 SegWit 時推出的。這個腳本是包裹在 P2SH 中的 P2WPKH。它根據公開密鑰的 Hash 鎖定比特幣。與經典 P2WPKH 的不同之處在於，該腳本包裹在經典 P2SH 的 `redeemscript`中。


這個腳本是在 SegWit 推出時為了方便採用而建立的。它允許使用這個新的標準，即使是尚未與 SegWit 原生相容的服務或錢包。這是一種邁向新標準的過渡腳本。今天，使用這些類型的包裝 SegWit 腳本已經不再有很大的意義，因為大多數的錢包已經實現了本機 SegWit。P2SH-P2WPKH 位址是使用 `Base58Check` 編碼寫成的，並且總是以 `3` 開頭，就像任何 P2SH Address 一樣。


> ► *`P2SH-P2WPKH`有時也稱為`P2WPKH-nested-in-P2SH`。