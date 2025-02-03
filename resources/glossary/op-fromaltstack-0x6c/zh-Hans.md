---
term: op_fromaltstack (0x6c)

---
从备用堆栈（*alt 堆栈*）中移除顶层项目，并将其置于主堆栈（*main 堆栈*）的顶层。该操作码用于取回临时存储在备用堆栈中的数据。简单地说，它是 `OP_TOALTSTACK` 的反向操作。