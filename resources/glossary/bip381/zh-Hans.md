---
term: BIP381

---
引入了描述符函数，特别是 `pk(KEY)` （Pay-to-PubKey）、 `pkh(KEY)` （Pay-to-PubKey-Hash）和 `sh(SCRIPT)` （Pay-to-Script-Hash）。这些函数规范了在描述符中描述传统脚本类型的方法。BIP381 与所有其他与描述符相关的 BIP（BIP386 除外）一起在 Bitcoin Core 0.17 版本中实施。