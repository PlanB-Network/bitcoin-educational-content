---
term: SCRIPTSIG

---
比特币交易中位于输入端的一个元素。scriptSig "提供必要的数据，以满足上一笔交易的 "scriptPubKey "所设定的条件。因此，它对 `scriptPubKey` 起着补充作用。通常，"scriptSig "包含一个数字签名和一个公钥。签名由比特币所有者使用其私钥生成，并证明他们有使用UTXO的授权。在这种情况下，"scriptSig "证明输入的持有者拥有与上一笔输出交易的 "scriptPubKey "中指定的地址相关的公钥对应的私钥。

交易通过验证后，"scriptSig "中的数据将在相应的 "scriptPubKey "中执行。如果结果有效，则表示已满足支出资金的条件。如果交易的所有输入都提供了验证其`scriptPubKey`的`scriptSig`，则交易有效，可以添加到区块中执行。

例如，这里有一个经典的 P2PKH `scriptSig`：

```text
<signature> <public key>
```

相应的 `scriptPubKey` 将是

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *`scriptSig`在英语中有时也被称为 "解锁脚本"。