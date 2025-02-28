---
term: BIP112

---
在比特币脚本语言中引入操作码 `OP_CHECKSEQUENCEVERIFY` (CSV)。该操作允许创建一些交易，这些交易的有效性只有在相对于前一个交易有一定延迟后才会生效，延迟时间可以用区块数量或时间长度来定义。OP_CHECKSEQUENCEVERIFY "比较堆栈顶端的值和输入的 "nSequence "字段的值。如果数值较大，且满足所有其他条件，则脚本有效。因此，"OP_CHECKSEQUENCEVERIFY "限制了输入的 "nSequence "字段的可能值，而这个 "nSequence "字段本身也限制了包含此输入的事务何时可以包含在一个代码块中。BIP112 于 2016 年 7 月 4 日通过软分叉引入，与 BIP68 和 BIP113 并列，首次使用 BIP9 方法激活。