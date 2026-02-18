---
term: OP_CHECKHASHVERIFY (CHV)

definition: 2012年提出的类似于P2SH功能的操作码，从未实施。
---
是 Luke Dashjr 于 2012 年在 BIP17 中提出的一个新操作码，具有与 `OP_EVAL` 或 P2SH 相同的功能。它的目的是对 `scriptSig` 的末尾进行哈希函数，将结果与栈顶进行比较，如果两个哈希值不相同，则使交易无效。该操作码从未实现。
