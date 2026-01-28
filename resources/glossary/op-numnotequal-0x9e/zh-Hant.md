---
term: OP_NUMNOTEQUAL (0X9E)
definition: 檢查堆疊頂部的兩個元素在數值上是否不同的Opcode。
---

比較堆疊中最頂端的兩個 Elements，檢查它們的數值是否不相等。如果數值不相等，會將 `1` (true) 推到堆疊上，否則會將 `0` (false) 推到堆疊上。這與 `OP_NUMEQUAL` 相反。