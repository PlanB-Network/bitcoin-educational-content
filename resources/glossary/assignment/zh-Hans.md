---
term: Assignment
---

在 RGB 协议的逻辑中，Assignment 相当于一个事务输出，它修改、更新或创建 Contract 状态中的某些属性。一个 Assignment 包含两个 Elements：




- 一个 Seal Definition（参考具体的 UTXO）；
- 一个 Owned State（描述新注册人相关状态的数据）。


因此，Assignment 表示状态的一部分（如资产）现在分配给了特定的持有者，该持有者通过与 UTXO 相关联的 Single-Use Seal 确定。