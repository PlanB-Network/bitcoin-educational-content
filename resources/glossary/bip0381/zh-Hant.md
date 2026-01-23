---
term: BIP0381
definition: 在描述符中用於描述 Legacy 腳本的 pk()、pkh() 和 sh() 函數。
---

引入了描述符的函數，特別是 `pk(KEY)` (Pay-to-PubKey), `pkh(KEY)` (Pay-to-PubKey-Hash) 和 `sh(SCRIPT)` (Pay-to-Script-Hash)。這些函數標準化了在描述符中描述 Legacy script 類型的方式。BIP381 與所有其他與描述符相關的 BIP (BIP386 除外) 已在 Bitcoin Core 的 0.17 版中實作。