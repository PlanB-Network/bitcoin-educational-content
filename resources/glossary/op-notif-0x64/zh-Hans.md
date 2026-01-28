---
term: OP_NOTIF (0X64)

definition: 如果顶部条件为假，则执行脚本的一部分的Opcode（与 OP_IF 相反）。
---
该操作码方式与 `OP_IF` 相反，如果堆栈顶部的值为零（false），则执行脚本的下一部分。
