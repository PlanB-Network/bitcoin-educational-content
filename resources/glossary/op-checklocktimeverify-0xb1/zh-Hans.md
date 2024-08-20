---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

除非满足以下所有条件，否则交易无效：
* 栈不为空；
* 栈顶的值大于或等于 `0`；
* `nLockTime` 字段与栈顶值之间的时间锁类型相同（真实时间或区块号）；
* 输入的 `nSequence` 字段不等于 `0xffffffff`；
* 栈顶的值大于或等于交易的 `nLockTime` 字段的值。

如果这些条件中的任何一个不满足，包含 `OP_CHECKLOCKTIMEVERIFY` 的脚本就不能被满足。如果所有这些条件都有效，则 `OP_CHECKLOCKTIMEVERIFY` 作为 `OP_NOP` 行动，意味着它不对脚本执行任何操作。就好像它消失了一样。因此，`OP_CHECKLOCKTIMEVERIFY` 对包含它的脚本所保护的UTXO的支出施加了时间约束。它可以以Unix时间日期或区块号的形式做到这一点。为此，它限制了支出它的交易的 `nLockTime` 字段的可能值，而这个 `nLockTime` 字段本身限制了交易可以被包含在区块中的时间。

> ► *这个操作码是 `OP_NOP` 的替代品。它被放置在 `OP_NOP2` 上。它通常被其首字母缩写 "CLTV" 所引用。注意，`OP_CLTV` 不应与交易的 `nLockTime` 字段混淆。前者使用后者，但它们的性质和行动是不同的。*