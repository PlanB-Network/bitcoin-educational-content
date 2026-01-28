---
term: OP_FROMALTSTACK (0X6C)

definition: 将元素从备用堆栈移至主堆栈的Opcode。
---
从备用堆栈（alt stack）中移除顶层项目，并将其置于主堆栈（main stack）的顶层。该操作码用于取回临时存储在备用堆栈中的数据。简单地说，它是 `OP_TOALTSTACK` 的反向操作。
