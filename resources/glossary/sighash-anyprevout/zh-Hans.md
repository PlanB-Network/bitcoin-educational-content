---
术语：SIGHASH_ANYPREVOUT
---

在比特币中引入了一个新的SigHash标志修饰符的提案，与BIP118一同介绍。`SIGHASH_ANYPREVOUT`允许在交易管理中提供更大的灵活性，特别是对于像闪电网络上的支付通道和Eltoo更新这样的高级应用。`SIGHASH_ANYPREVOUT`使得签名不再与任何特定的先前UTXO（*任何先前的输出*）绑定。与`SIGHASH_ALL`结合使用时，它将允许对交易的所有输出进行签名，但不包括任何输入。这将使得在满足某些特定条件的情况下，可以重复使用签名于不同的交易中。

> ► *这个SigHash修饰符SIGHASH_ANYPREVOUT是基于Joseph Poon在2016年最初为了增强他的闪电网络概念而提出的SIGHASH_NOINPUT的想法而衍生出来的。*