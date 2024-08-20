---
term: OP_TOALTSTACK (0X6B)
---

将主栈（*main stack*）顶部的数据移动到备用栈（*alt stack*）。这个操作码用于临时存储数据，以便稍后在脚本中使用。因此，被移动的项目将从主栈中移除。`OP_FROMALTSTACK` 将被用来将其重新放回主栈顶部。