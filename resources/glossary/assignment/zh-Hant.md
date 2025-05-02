---
term: Assignment
---

在 RGB 通訊協定的邏輯中，Assignment 相當於在 Contract 狀態中修改、更新或建立某些屬性的交易輸出。一個 Assignment 包含兩個 Elements：




- A Seal Definition（參照特定的 UTXO）；
- 一個 Owned State（描述與此新持有人相關狀態的資料）。


因此，Assignment 表示狀態的一部分（例如資產）現在分配給特定的持有人，該持有人通過與 UTXO 相連的 Single-Use Seal 識別。