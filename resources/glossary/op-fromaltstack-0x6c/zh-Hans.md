---
term: OP_FROMALTSTACK (0X6C)
---

从备用栈（*alt stack*）中移除顶部项目，并将其放置在主栈（*main stack*）的顶部。这个操作码用于检索临时存储在备用栈上的数据。简单来说，它是`OP_TOALTSTACK`的反向操作。