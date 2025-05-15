---
term: OP_NOP (0X61)
---

不會對堆疊或腳本的狀態產生任何影響。不執行任何移動、檢查或修改。除非 Soft Fork 另有決定，否則它什麼都不做。事實上，自從 Satoshi Nakamoto 在 2010 年修改後，`OP_NOP` 指令 (`OP_NOP1`(`0XB0`)至`OP_NOP10`(`0XB9`)) 都是以 Soft Fork 的形式來增加新的操作碼。


因此， `OP_NOP2` (`0XB1`) 和 `OP_NOP3` (`0XB2`)已經分別用來實作 `OP_CHECKLOCKTIMEVERIFY` 和 `OP_CHECKSEQUENCEVERIFY`。它们与 `OP_DROP` 结合使用，可以从堆栈中移除相关的时序值，从而允许脚本的执行继续进行，无论节点是否是最新的。因此，`OP_NOP` 指令允許在腳本中插入中斷點，以檢查已經存在或可能隨著未來 Soft fork 而新增的條件。自從 Tapscript 以後，`OP_NOP` 的使用已經被更有效率的 `OP_SUCCESS` 所取代。