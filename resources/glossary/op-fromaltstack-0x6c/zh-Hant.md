---
term: OP_FROMALTSTACK (0X6C)
definition: 將元素從備用堆疊移至主堆疊的Opcode。
---

從交替堆疊 (*alt stack*) 移除最頂端的項目，並將其放置在主堆疊 (*main stack*) 的頂端。這個 opcode 用來取回暫時存放在交替堆疊上的資料。簡單來說，它是 `OP_TOALTSTACK` 的反向操作。