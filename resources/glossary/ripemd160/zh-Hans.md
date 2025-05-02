---
term: RIPEMD160

---
*Research and development in Advanced Communications technologies in Europe Integrity Primitives Evaluation Message Digest 160* 的缩写。这是一种加密哈希函数，可从任意输入生成 160 位哈希值。在比特币系统中，它用于将公钥转换为传统和 SegWit v0 标准的接收地址（对于 SegWit v1，公钥不会经过哈希处理）。在这个过程中，首先对公钥使用 `SHA256` 哈希函数，然后对结果使用 `RIPEMD160` 哈希函数。在比特币系统中，这两种不同哈希函数的组合被称为 `HASH160`。`RIPEMD160` 也用于确定性钱包和分层钱包，以计算密钥指纹。具体来说，`HASH160` 可用于计算父密钥的指纹，然后包含在扩展密钥（xpub、xprv 等）的元数据中。
