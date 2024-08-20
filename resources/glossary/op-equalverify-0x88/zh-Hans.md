---
term: OP_EQUALVERIFY (0X88)
---

结合了`OP_EQUAL`和`OP_VERIFY`的功能。它首先检查栈顶两个值的相等性，然后要求结果非零，否则，交易无效。`OP_EQUALVERIFY`显著用于地址验证脚本中。