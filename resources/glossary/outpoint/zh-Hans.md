---
term: OUTPOINT
---

OUTPOINT是对一个未花费交易输出（UTXO）的唯一引用。它由两个元素组成：
* `txid`：创建输出的交易的标识符；
* `vout`：输出在交易中的索引。

这两个元素的组合准确地标识了一个UTXO。例如，如果一个交易的`txid`为`abc...123`，并且输出索引为`0`，则outpoint将被记为：

```text
abc...123:0
```

在新交易的输入（`vin`）中使用outpoint来指示哪个UTXO正在被花费。

> ► *术语“outpoint”通常与“UTXO”同义使用。*