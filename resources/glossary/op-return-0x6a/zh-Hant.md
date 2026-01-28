---
term: OP_RETURN (0X6A)
definition: 使輸出不可花費的Opcode，常用於記錄任意數據。
---

表示無效的腳本，使包含該腳本的輸出無法使用。因此，網路節點可以從其 UTXO 套件中移除此輸出。`OP_RETURN` 通常用來記錄 Blockchain 中的任意資料。