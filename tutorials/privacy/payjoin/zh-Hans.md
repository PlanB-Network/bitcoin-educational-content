---
name: Payjoin
description: 什么是比特币上的Payjoin？
---
![Payjoin 缩略图 - 隐写术](assets/cover.webp)

***注意：** 继Samourai Wallet的创始人于4月24日被逮捕，其服务器被查封后，Payjoins Stowaway在Samourai Wallet上仅能通过手动交换PSBT（Partially Signed Bitcoin Transaction，部分签名的比特币交易）在有关方之间进行，前提是双方用户都连接到他们自己的Dojo。至于Sparrow，通过BIP78的Payjoins仍然可以工作。然而，这些工具可能在未来几周重新启动。与此同时，您仍然可以阅读本文以理解payjoins的理论运作机制。*

_我们正在密切关注此案件以及相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守他们所在司法管辖区的法律。_

---
## 理解比特币上的Payjoin交易

Payjoin是一种特定结构的比特币交易，它通过与支付接收者合作，增强了用户在支付过程中的隐私。

2015年，[LaurentMT](https://twitter.com/LaurentMT)首次在一个可通过[此处](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt)访问的文档中提到了这种方法，称之为“隐写术交易”。这项技术后来被Samourai Wallet采用，该钱包在2018年成为第一个通过Stowaway工具实现它的客户端。Payjoin的概念也出现在[BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki)和[BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki)中。有几个术语用来指代Payjoin：
- Payjoin
- Stowaway
- P2EP（Pay-to-End-Point，支付至终点）
- 隐写术交易

Payjoin的独特之处在于其生成的交易乍一看似乎很普通，但实际上是两方之间的小型Coinjoin。为了实现这一点，交易结构涉及到实际发送者以及支付接收者在输入中的参与。接收者在交易中间包含了一笔对自己的支付，这使得他们得以收款。

让我们来看一个具体的例子：如果你用`10,000 sats`的UTXO购买了一个价值`4000 sats`的法棍，并选择了Payjoin，你的面包师将添加一个属于他们的、价值`15,000 sats`的UTXO作为输入，他们将全额接收这个作为输出，除了你的`4000 sats`：
![Payjoin交易图解](assets/en/1.webp)
在这个例子中，面包师输入了`15,000 sats`，并得到了`19,000 sats`的输出，净增`4000 sats`，这正是面包的价格。在你这边，你输入了`10,000 sats`，最终得到`6,000 sats`的输出，表示一个`-4000 sats`的余额，这也是面包的价格。为了简化例子，我故意省略了这笔交易中的挖矿费用。
## Payjoin交易的目的是什么？

Payjoin交易有两个目的，允许用户增强他们支付的隐私性。
首先，Payjoin旨在通过创建链分析中的诱饵来误导外部观察者。这通过共同输入所有权启发式（CIOH）成为可能。通常，当区块链上的一笔交易有多个输入时，假设所有这些输入很可能属于同一个实体或用户。因此，当分析师检查一个Payjoin交易时，他们会被引导认为所有输入都来自同一个人。然而，这种看法是不正确的，因为支付接收者也贡献了输入，与实际支付者并排。因此，链分析被引向了一种最终被证明是错误的解释。

此外，Payjoin还允许欺骗外部观察者关于已支付金额的实际数额。通过检查交易结构，分析师可能会认为支付等同于其中一个输出的金额。然而，实际上，支付金额并不对应于任何输出。它实际上是接收者的输出UTXO和接收者的输入UTXO之间的差额。从这个意义上说，Payjoin交易属于隐写术的领域。它允许在充当诱饵的假交易中隐藏实际交易金额。

> 隐写术是一种在其他数据或对象中隐藏信息的技术，以使隐藏信息的存在不被察觉。例如，一个秘密消息可以隐藏在与之无关的文本的一个点中，使其对肉眼不可检测（这是微点技术）。与加密不同，加密使信息在没有解密密钥的情况下变得不可理解，隐写术不修改信息。它仍然以明文显示。其目标更多是隐藏秘密消息的存在，而加密则明确揭示了隐藏信息的存在，尽管没有密钥无法访问。

让我们回到支付面包的Payjoin交易的例子。
![Payjoin交易外观示意图](assets/en/2.webp)
通过在区块链上看到这笔交易，一个遵循链分析常规启发式的外部观察者会这样解释："*Alice合并了2个UTXOs作为交易的输入，以支付`19,000 sats`给Bob*。"
![Payjoin交易的错误解释示意图](assets/en/3.webp)
这种解释显然是不正确的，因为如你所知，这两个输入UTXOs并不属于同一个人。此外，实际的支付价值不是`19,000 sats`，而是`4,000 sats`。因此，外部观察者的分析被引向了一个错误的结论，确保了利益相关者的保密性。![payjoin交易图解](assets/en/1.webp)
如果您想分析一个真实的Payjoin交易，这里有一个我在测试网上进行的交易：[8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)
[**-> 探索我们的教程，了解如何使用Samourai Wallet进行Payjoin**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)

[**-> 探索我们的教程，了解如何使用Sparrow Wallet进行Payjoin**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)

**外部资源：**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.