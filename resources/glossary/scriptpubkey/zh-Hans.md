---
term: SCRIPTPUBKEY
---

位于比特币交易输出部分的脚本，定义了关联的UTXO可以被花费的条件。因此，这个脚本保护了比特币。在最常见的形式中，`scriptPubKey`包含一个条件，要求下一笔交易提供拥有与指定比特币地址对应的私钥的证明。这通常通过一个要求签名的脚本实现，该签名对应于用于保护这些资金的地址关联的公钥。当一笔交易尝试使用这个UTXO作为输入时，它必须提供一个`scriptSig`，一旦与`scriptPubKey`结合，就满足了设定的条件并产生了一个有效的脚本。

例如，这里是一个经典的P2PKH `scriptPubKey`：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

相应的`scriptSig`将会是：

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.png)

> ► *这个脚本有时也被称为“锁定脚本”（locking script）。*