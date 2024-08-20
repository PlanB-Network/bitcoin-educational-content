---
term: BIP112
---

引入了比特币脚本语言中的操作码`OP_CHECKSEQUENCEVERIFY`（CSV）。此操作允许创建交易，其有效性仅在相对于之前的交易之后的一定延迟后生效，该延迟以区块数量或时间长度定义。`OP_CHECKSEQUENCEVERIFY`将栈顶的值与输入的`nSequence`字段的值进行比较。如果它更大且满足所有其他条件，则脚本有效。因此，`OP_CHECKSEQUENCEVERIFY`限制了输入消费它的`nSequence`字段可能的值，而这个`nSequence`字段本身限制了包含此输入的交易可以被包含在区块中的时间。BIP112通过2016年7月4日的软分叉引入，与BIP68和BIP113一起激活，首次使用BIP9方法激活。