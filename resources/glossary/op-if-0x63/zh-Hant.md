---
term: OP_IF (0X63)
---

如果堆疊頂端的值是非零 (true)，則執行腳本的下列部分。如果值為零 (false)，這些操作會被跳過，直接移到 `OP_ELSE` 之後的操作 (如果有的話)。`OP_IF` 可以在腳本中啟動條件控制結構。它根據在執行交易時所提供的條件來決定腳本中的控制流程。`OP_IF` 與 `OP_ELSE` 和 `OP_ENDIF` 的使用方式如下：


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```