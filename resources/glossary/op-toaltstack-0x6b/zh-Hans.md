---
term: OP_TOALTSTACK (0x6B)

---
将主堆栈（main stack）的顶部数据移至备用堆栈（alt stack）。此操作码用于临时存储数据，供以后在脚本中使用。被移动的项目将从主栈中移除。然后将使用 `OP_FROMALTSTACK` 把它放回主栈顶部。
