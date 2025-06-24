---
term: BIP0381

---
该 BIP 引入了描述符函数，其为 `pk(KEY)` （Pay-to-PubKey，即支付到公钥）、 `pkh(KEY)` （Pay-to-PubKey-Hash，即支付到公钥哈希）和 `sh(SCRIPT)` （Pay-to-Script-Hash，即支付到脚本哈希）。这些函数规范了在描述符中描述传统脚本类型的方法。BIP381 与所有其他与描述符相关的 BIP（BIP386 除外）已共同在 Bitcoin Core 0.17 版本中实施。
