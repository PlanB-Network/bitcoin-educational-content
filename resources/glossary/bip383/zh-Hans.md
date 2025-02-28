---
term: BIP383

---
为描述符引入了函数 `multi(NUM, KEY, ..., KEY)` 和 `sortedmulti(NUM, KEY, ..., KEY)`。这些函数允许在描述符中描述多签名脚本，"sortedmulti "按词典顺序对公钥进行排序，以确保导入时的兼容性。BIP383 和所有其他与描述符相关的 BIP（BIP386 除外）已在 0.17 版本的 Bitcoin Core 中实施。