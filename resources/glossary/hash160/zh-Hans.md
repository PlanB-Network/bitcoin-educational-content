---
term: HASH160
---

在比特币中使用的加密函数，特别用于生成传统和SegWit v0接收地址。它结合了两个依次对输入执行的哈希函数：首先是SHA256，然后是RIPEMD160。因此，此函数的输出是160位。

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$