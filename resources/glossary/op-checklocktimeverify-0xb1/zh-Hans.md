---
term: op_checklocktimeverify (0xb1)

---
使交易无效，除非满足所有这些条件：


- 堆栈不是空的；
- 堆栈顶部的值大于或等于 `0`；
- 在 `nLockTime` 字段和堆栈顶部的值（实时或块编号）之间，时间锁定的类型是相同的；
- 输入的 `nSequence` 字段不等于 `0xffffffffffff`；
- 堆栈顶部的值大于或等于事务的 `nLockTime` 字段的值。

如果不满足其中任何一个条件，则无法满足包含 `OP_CHECKLOCKTIMEVERIFY` 的脚本。如果所有这些条件都有效，那么 `OP_CHECKLOCKTIMEVERIFY` 将作为 `OP_NOP` 运行，这意味着它不会对脚本执行任何操作。就好像它消失了一样。因此，"OP_CHECKLOCKTIMEVERIFY "对包含它的脚本的UTXO的使用时间施加了限制。它可以采用 Unix 时间日期或块编号的形式。为此，它限制了使用它的事务的 `nLockTime` 字段的可能值，而这个 `nLockTime` 字段本身也限制了该事务何时可以包含在一个区块中。

> ► *此操作码是 `OP_NOP` 的替代。它被放在 `OP_NOP2` 上。它通常被缩写为 "CLTV"。注意，"OP_CLTV "不应与事务的 "nLockTime "字段混淆。前者使用后者，但它们的性质和作用是不同的*。