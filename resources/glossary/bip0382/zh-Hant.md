---
term: BIP0382
---

為描述符引進了函數 `wpkh(KEY)` (Pay-to-Witness-PubKey-Hash) 和 `wsh(SCRIPT)` (Pay-to-Witness-Script-Hash) 。這些函式將在描述符中描述 SegWit 腳本類型的方式標準化。BIP382 與其他所有與描述符相關的 BIP（BIP386 除外）已在 Bitcoin Core 的 0.17 版中實作。