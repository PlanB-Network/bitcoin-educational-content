---
term: op_numequalverify (0x9d)

---
结合了操作 `OP_NUMEQUAL` 和 `OP_VERIFY`。它对堆栈中最上面的两个元素进行数值比较。如果数值相等，`OP_NUMEQUALVERIFY` 会从堆栈中删除为真的结果，并继续执行脚本。如果数值不相等，结果为假，脚本立即失败。