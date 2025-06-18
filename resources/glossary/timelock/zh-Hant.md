---
term: 時間鎖
---

Smart contract 基元允許設定一個以時間為基礎的條件，該條件必須符合才能將交易加入區塊。Bitcoin 上有兩種時間鎖類型：


- 絕對時間鎖定，指定交易不能包含在區塊中的準確時刻；
- 相對時間鎖定，設定從接受先前交易開始的延遲時間。

時間鎖可以定義為以 Unix 時間表示的日期或區塊號碼。最後，時間鎖可以透過在鎖定腳本中使用特定的操作碼 (`OP_CHECKLOCKTIMEVERIFY`或`OP_CHECKSEQUENCEVERIFY`) 應用於一個交易輸出，或透過使用特定的交易欄位 (`nLockTime`或`nSequence`) 應用於整個交易。