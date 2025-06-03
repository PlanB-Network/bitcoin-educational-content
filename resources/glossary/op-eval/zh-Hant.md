---
term: OP_EVAL
---

Gavin Andresen 在 2011 年提出的 Opcode。它取得位於堆疊頂端的腳本，將它當成 `scriptPubKey` 的一部分來執行，並將其結果放置在堆疊上。由於擔心這個操作碼的複雜性而放棄了 `OP_EVAL`，這個操作碼最終會被 P2SH 取代。