---
term: SCRIPTWITNESS
---

SegWit交易条目中的一个元素，包含解锁交易中发送的比特币所需的签名和公钥。类似于传统交易中的`scriptSig`，但`scriptWitness`的位置不同。实际上，被称为“见证人”（英文中的`*witness*`）的这部分，被移到一个单独的数据库中，以解决交易可变性问题。每个SegWit输入都有其自己的`scriptWitness`，所有的`scriptWitness`元素 together 形成交易的`Witness`字段。

> ► *注意不要将`scriptWitness`与`witnessScript`混淆。虽然`scriptWitness`包含任何SegWit输入的见证数据，但`witnessScript`定义了P2WSH或P2SH-P2WSH UTXO的消费条件，并构成了一个自成一体的脚本，类似于P2SH输出的`redeemScript`。*