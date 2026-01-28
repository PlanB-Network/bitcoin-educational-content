---
term: HASH160

definition: 结合了 SHA256 和 RIPEMD160 的函数，用于生成比特币地址。
---
比特币中使用的加密函数，主要用于生成传统和 SegWit v0 接收地址。它结合了对输入连续进行的两个哈希函数：首先使用 SHA256，然后将结果输入到 RIPEMD160。因此，该函数的输出为 160 比特。

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$
