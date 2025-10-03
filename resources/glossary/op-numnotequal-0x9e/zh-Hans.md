---
term: OP_NUMNOTEQUAL (0x9E)

---
对堆栈中最上面的两个元素进行比较，检查它们在数值上是否不相等。如果数值不相等，则向堆栈推送 `1`（true），否则推送 `0`（false）。这与 `OP_NUMEQUAL` 相反。
