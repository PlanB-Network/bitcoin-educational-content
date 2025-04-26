---
term: OP_IF (0X63)

---
如果堆栈顶部的值为非零（true），则执行脚本的以下部分。如果值为零（false），则跳过这些操作，直接执行 `OP_ELSE` 后面的操作。`OP_IF` 可以在脚本中启动条件控制结构。它根据事务执行时提供的条件确定脚本中的控制流。`OP_IF` 与 `OP_ELSE` 和 `OP_ENDIF` 的使用方式如下：

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```