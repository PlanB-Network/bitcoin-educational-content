---
term: OP_NUMEQUALVERIFY (0X9D)
---

结合了`OP_NUMEQUAL`和`OP_VERIFY`的操作。它数值比较栈顶的两个元素。如果值相等，`OP_NUMEQUALVERIFY`会从栈中移除真实结果并继续执行脚本。如果值不相等，结果为假，并且脚本立即失败。