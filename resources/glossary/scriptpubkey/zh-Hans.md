---
term: SCRIPTPUBKEY

---
比特币交易输出部分的一个脚本，它定义了相关 UTXO 可以使用的条件。因此，该脚本可确保比特币的安全。在最常见的形式中，"scriptPubKey "包含一个条件，要求下一笔交易提供与指定比特币地址相对应的私钥的持有证明。这通常是通过一个脚本来实现的，该脚本要求提供与用于确保这些资金安全的地址相关联的公钥对应的签名。当一笔交易试图使用该UTXO作为输入时，它必须提供一个 "scriptSig"，该 "scriptSig "一旦与 "scriptPubKey "结合，就会满足设定的条件并产生一个有效的脚本。

例如，这里有一个经典的 P2PKH `scriptPubKey`：

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

相应的 `scriptSig` 将是

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *这种脚本在英语中有时也被称为 "锁定脚本"。