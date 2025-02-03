---
term: sighash_anyprevout

---
关于在比特币中实施新的 SigHash 标志修改器的建议，与 BIP118 一起引入。SIGHASH_ANYPREVOUT "使交易管理更加灵活，尤其适用于闪电网络支付通道和 Eltoo 更新等高级应用。SIGHASH_ANYPREVOUT "可使签名不与任何特定的先前UTXO（*任何先前输出*）绑定。与 `SIGHASH_ALL` 结合使用，可以对事务的所有输出进行签名，但不对输入进行签名。只要满足某些特定条件，就可以在不同的事务中重复使用签名。

> ► *这个 SigHash 修饰符 SIGHASH_ANYPREVOUT 源自约瑟夫-潘（Joseph Poon）在 2016 年提出的 SIGHASH_NOINPUT 概念，最初是为了增强他的闪电网络概念。