---
term: op_numequalverify (0x9d)
---

結合操作 `OP_NUMEQUAL` 和 `OP_VERIFY`。它以數值比較堆疊上最頂端的兩個 Elements。如果值相等，`OP_NUMEQUALVERIFY` 會從堆疊中移除為真的結果，並繼續執行腳本。如果值不相等，結果為假，腳本會立即失敗。