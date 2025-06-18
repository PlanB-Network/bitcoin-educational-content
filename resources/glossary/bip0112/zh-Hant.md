---
term: BIP0112
---

在 Bitcoin Script 語言中引入操作碼 `OP_CHECKSEQUENCEVERIFY` (CSV)。此操作允許創建交易，其有效性僅在相對於前一個交易有一定的延遲後才生效，延遲的定義可以是區塊數，也可以是時間長度。OP_CHECKSEQUENCEVERIFY」會比較堆疊頂端的值和輸入的 `nSequence` 欄位的值。如果它比較大，而且所有其他條件都符合，腳本就是有效的。因此， `OP_CHECKSEQUENCEVERIFY` 限制了输入的 `nSequence` 字段的可能值，而这个 `nSequence` 字段本身也限制了包含此输入的事务何时可以包含在一个块中。BIP112 於 2016 年 7 月 4 日透過 Soft Fork 引進，與 BIP68 和 BIP113 並列，首次使用 BIP9 方法啟用。