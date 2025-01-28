---
term: op_checkhashverify (chv)

---
是 Luke Dashjr 于 2012 年在 BIP17 中提出的一个新操作码，具有与 `OP_EVAL` 或 P2SH 相同的功能。它的目的是对 `scriptSig` 的末尾进行散列，将结果与栈顶进行比较，如果两个散列不匹配，则使事务无效。该操作码从未实现。