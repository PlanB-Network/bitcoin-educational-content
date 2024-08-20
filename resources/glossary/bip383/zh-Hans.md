---
term: BIP383
---

引入了描述符中的函数`multi(NUM, KEY, ..., KEY)`和`sortedmulti(NUM, KEY, ..., KEY)`。这些函数允许在描述符中描述多签名脚本，其中`sortedmulti`将公钥按字典顺序排序，以确保在导入时的兼容性。BIP383与所有其他与描述符相关的BIP（除了BIP386）一起，在Bitcoin Core的0.17版本中实现。