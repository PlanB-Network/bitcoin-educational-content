---
term: SCRIPTSIG
---

`scriptSig`是比特币交易输入部分的一个元素。它提供了满足前一笔交易中`scriptPubKey`设定条件所需的数据，从而发挥了与`scriptPubKey`互补的作用。通常，`scriptSig`包含一个数字签名和一个公钥。这个签名由比特币的所有者使用他们的私钥生成，证明他们有权使用UTXO。在这种情况下，`scriptSig`证明了输入的持有者拥有与前一个输出交易中`scriptPubKey`指定的地址相关联的公钥对应的私钥。

当交易被验证时，`scriptSig`中的数据在相应的`scriptPubKey`中执行。如果结果有效，意味着满足了使用资金的条件。如果交易的所有输入提供了验证其`scriptPubKey`的`scriptSig`，则交易有效，可以添加到区块中执行。

例如，这是一个经典的P2PKH `scriptSig`：

```text
<signature> <public key>
```

相应的`scriptPubKey`将是：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig`在英语中有时也被称为“解锁脚本”。*