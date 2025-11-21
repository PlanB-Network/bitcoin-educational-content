---
term: BRANCH-AND-BOUND (分支与限界法)

---
自 0.17 版起在 Bitcoin Core 钱包中用于选择输入的方法，由 Murch 发明。分支与边界（BnB）是一种搜索方法，旨在找到一组 UTXO，该 UTXO 与交易中需要完成的输出量相匹配，以尽量减少变动和相关费用。其目标是减少浪费标准，该标准既考虑了当前成本，也考虑了变更的未来预期成本。与以往的启发式方法（如*Knapsack Solver*）相比，这种方法在费用方面更为精确。分支与边界的灵感来源于 Ailsa Land 和 Alison Harcourt 于1960年发明的同名问题解决方法。

> ► *这种方法有时也被称为 “Murch's Algorithm”，以纪念其发明者。*
