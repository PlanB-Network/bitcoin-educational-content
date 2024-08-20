---
term: OP_CHECKHASHVERIFY (CHV)
---

OP_CHECKHASHVERIFY (CHV) 是Luke Dashjr 在 2012 年的 BIP17 中提出的一个新操作码，它将提供与 `OP_EVAL` 或 P2SH 相同的功能。其设计目的是对 `scriptSig` 的末尾进行哈希处理，将结果与堆栈顶部进行比较，如果两个哈希值不匹配，则使交易无效。这个操作码从未被实现。