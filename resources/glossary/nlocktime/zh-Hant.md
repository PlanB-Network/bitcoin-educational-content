---
term: NLOCKTIME
---

交易中的內嵌欄位，設定一個以時間為基礎的條件，在此條件之前，交易無法加入有效區塊。此參數允許指定精確的時間 (Unix Timestamp) 或特定的區塊數量，作為交易被視為有效的條件。因此，它是絕對的時間鎖（不是相對的）。`nLockTime` 會影響整個交易，並有效地實現時間驗證，而 opcode `OP_CHECKLOCKTIMEVERIFY` 只允許比較堆疊的頂端值與 `nLockTime` 值。