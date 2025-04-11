---
term: op_equalverify (0x88)

---
结合了 `OP_EQUAL` 和 `OP_VERIFY` 的功能。它首先检查堆栈顶部两个值是否相等，然后要求结果非零，否则事务无效。`OP_EQUALVERIFY` 主要用于地址验证脚本。