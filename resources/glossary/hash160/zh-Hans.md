---
term: HASH160

---
比特币中使用的加密函数，主要用于生成传统和 SegWit v0 接收地址。它结合了对输入连续执行的两个哈希函数：首先是 SHA256，然后是 RIPEMD160。因此，该函数的输出为 160 比特。

$$text{HASH160}(x) = （text{RIPEMD160}(\text{SHA256}(x)）$$