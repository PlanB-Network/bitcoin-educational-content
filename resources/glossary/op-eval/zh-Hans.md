---
term: OP_EVAL
---

由Gavin Andresen在2011年提出的操作码。它取出位于堆栈顶部的脚本，将其作为`scriptPubKey`的一部分执行，并将其结果放置在堆栈上。由于担心这个操作码的复杂性，`OP_EVAL`最终被放弃，后来被P2SH所取代。