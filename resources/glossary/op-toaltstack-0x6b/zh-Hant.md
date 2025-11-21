---
term: op_toaltstack (0x6b)
---

取主堆疊 (*main stack*) 的頂端，並將其移至交替堆疊 (*alt stack*)。這個操作碼用來暫時儲存資料，以備日後在腳本中使用。被移動的項目因此會從主堆疊中移除。之後會使用 `OP_FROMALTSTACK` 將它放回主堆疊頂。