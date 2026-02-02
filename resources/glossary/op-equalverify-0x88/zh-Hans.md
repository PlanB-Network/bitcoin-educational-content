---
term: OP_EQUALVERIFY (0X88)

definition: 结合了 OP_EQUAL 和 OP_VERIFY，如果数值不同则使交易失效。
---
结合了 `OP_EQUAL` 和 `OP_VERIFY` 的功能。它首先检查堆栈顶部两个值是否相等，然后要求结果非零，否则交易无效。`OP_EQUALVERIFY` 主要用于地址验证脚本。
