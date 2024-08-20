---
term: COVENANT
---

一种机制，允许对特定货币的使用方式施加特定条件，包括在未来的交易中。除了UTXO上的脚本语言通常允许的条件外，covenant还对如何在后续交易中花费这比特币施加了额外的约束。技术上，当UTXO的`scriptPubKey`定义了对花费该UTXO的交易的输出的`scriptPubKey`的限制时，就建立了一个covenant。通过扩展脚本的范围，covenant将使得在比特币上实现许多发展成为可能，如双边锚定drivechains、实现vaults或改进像Lightning这样的覆盖系统。Covenant提案基于三个标准进行区分：
* 它们的范围；
* 它们的实现；
* 它们的递归性。

有许多提案将允许在比特币上使用covenant。在实现过程中最先进的是：`OP_CHECKTEMPLATEVERIFY` (CTV)、`SIGHASH_ANYPREVOUT` (APO)和`OP_VAULT`。其他提案包括：`OP_TX`、`OP_TAPLEAFUPDATEVERIFY` (TLUV)、`OP_EVICT`、`OP_CHECKSIGFROMSTACKVERIFY` (CSFSV)、`OP_CAT`等。

为了更好地理解covenant的概念，考虑这样一个类比：想象一个保险箱，里面装有500欧元的小面额钞票。如果你用正确的钥匙成功打开这个保险箱，那么你可以随意使用这笔钱。这是比特币的正常情况。现在，想象同一个保险箱不是装有500欧元的钞票，而是装有等值的餐券。如果你成功打开这个保险箱，你可以使用这笔钱。然而，你花费的自由受到限制，因为你只能使用这些餐券在特定的餐厅支付。因此，花费这笔钱的第一个条件是能够用适当的钥匙打开保险箱。但关于这笔钱未来使用的还有一个额外的条件：它必须专门在合作餐厅中使用，而不能自由使用。这种对未来交易施加约束的系统就是所谓的covenant。

> ► *在法语中，没有一个术语能精确捕捉"covenant"这个词的含义。人们可以谈论"clause"、"pact"或"commitment"，但这些并不完全对应于"covenant"这个术语。这个术语借用自法律术语，用于描述对财产施加持续义务的合同条款。*