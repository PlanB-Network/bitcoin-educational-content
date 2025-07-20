---
term: P2SH-P2WSH
---

P2SH-P2WSH 代表 * 付費腳本 Hash - 付費見證腳本 Hash*。它是一個標準的腳本模型，用來建立 UTXO 的支出條件，也稱為 「巢狀 SegWit」。


P2SH-P2WSH 是在 2017 年 8 月實施 SegWit 時推出的。此腳本描述了包裹在 P2SH 中的 P2WSH。它根據腳本的 Hash 鎖定比特幣。與經典 P2WSH 的不同之處在於腳本包裝在經典 P2SH 的 `redeemscript`中。


這個腳本是在 SegWit 推出時為了方便採用而建立的。它允許使用這個新標準，即使服務或錢包尚未與 SegWit 原生相容。因此，今天使用這些類型的包裝 SegWit 腳本已經無多大意義，因為大多數的錢包都已經實現本機 SegWit。P2SH-P2WSH 位址使用 `Base58Check` 編碼寫成，並且總是以 `3` 開頭，就像任何 P2SH Address 一樣。