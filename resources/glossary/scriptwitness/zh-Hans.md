---
term: SCRIPTWITNESS

---
SegWit 交易条目中的一个元素，包含解锁交易中发送的比特币所需的签名和公钥。与传统交易中的 "scriptSig "类似，"scriptWitness "不在同一位置。事实上，正是这部分被称为 "证人"（英语中的 "*witness*"）的内容被转移到了一个单独的数据库中，以解决交易的可塑性问题。每个 SegWit 输入都有自己的 "scriptWitness"，所有的 "scriptWitness "元素共同构成事务的 "Witness "字段。

> ► *注意不要混淆`scriptWitness`和`witnessScript`。虽然 `scriptWitness` 包含任何 SegWit 输入的见证数据，但 `witnessScript` 定义了 P2WSH 或 P2SH-P2WSH UTXO 的支出条件，其本身就构成一个脚本，类似于 P2SH 输出的 `redeemScript` *。