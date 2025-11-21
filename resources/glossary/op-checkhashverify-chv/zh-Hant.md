---
term: op_checkhashverify (chv)
---

由 Luke Dashjr 於 2012 年在 BIP17 提出的新作業碼，可提供與 `OP_EVAL` 或 P2SH 相同的功能。它的目的是 Hash `scriptSig` 的結尾，將結果與堆疊頂端進行比較，如果兩個哈希值不匹配，就使交易無效。這個操作碼從未實作。