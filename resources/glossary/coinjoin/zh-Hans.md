---
term: COINJOIN
---

Coinjoin是一种用于打破比特币可追踪性的技术。它依赖于一种具有特定结构的协作交易，即coinjoin交易。Coinjoin交易通过使外部观察者更难分析交易来帮助提高比特币用户的隐私保护。这种结构允许在单一交易中混合多个硬币，使得难以确定输入和输出地址之间的链接。

Coinjoin的一般操作流程如下：不同的用户希望混合存入作为交易输入的金额。这些输入将作为相同金额的不同输出出现。在交易结束时，不可能确定哪个输出属于哪个用户。技术上，coinjoin交易的输入和输出之间没有任何联系。每个用户与每个UTXO之间的链接被打破，就像每个硬币的历史一样。

![](../../dictionnaire/assets/4.png)

为了允许在任何时候都不会失去对资金控制的coinjoin，首先由协调者构建交易，然后传输给每个用户。每个人在验证交易适合他们之后，就在自己的一边签名，然后将所有签名添加到交易中。如果用户或协调者试图通过修改coinjoin交易的输出来窃取他人的资金，那么签名将是无效的，交易将被节点拒绝。当使用Chaum的盲签名记录参与者的输出以避免与输入的链接时，这被称为“Chaumian coinjoin”。

这种机制增加了交易的保密性，而不需要修改比特币协议。Coinjoin的特定实现，如Whirlpool、JoinMarket或Wabisabi，提供了解决方案以促进参与者之间的协调过程并提高coinjoin交易的效率。这是一个coinjoin交易的例子：

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

很难确定谁首次在比特币上引入了coinjoin的概念，以及谁想到在这个背景下使用David Chaum的盲签名。人们通常认为Gregory Maxwell是第一个在[2013年BitcoinTalk上的一条消息](https://bitcointalk.org/index.php?topic=279249.0)中讨论它的人：
使用Chaum盲签名：用户连接并提供输入（和找零地址）以及他们希望发送私有硬币的地址的加密盲版本；服务器签署代币并返回它们。用户匿名重新连接，揭示他们的输出地址，并将它们发送回服务器。服务器可以看到所有输出都已由其签名，因此，所有输出都来自有效参与者。后来，人们重新连接并签名。
Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privacy for the real world*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0
然而，早期就有提及Chaum签名在混币（mixing）上下文中的使用，以及coinjoin的使用。[2011年6月，Duncan Townsend在BitcoinTalk上介绍](https://bitcointalk.org/index.php?topic=12751.0)了一种使用Chaum签名的混币器，其方式与现代Chaumian coinjoin非常相似。在同一个讨论帖中，还有[hashcoin回复Duncan Townsend的消息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)，以改进他的混币器。这条消息提出了最接近coinjoin的概念。还有在[2012年Alex Mizrahi的一条消息中](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry)提到了一个类似的系统，当时他正在为Tenebrix的创造者提供建议。"coinjoin"这个术语并非由Greg Maxwell发明，而是来自Peter Todd的一个想法。
> ► *“coinjoin”这个术语没有法语翻译。一些比特币用户也使用“混合”、“混币”或“混币交易”来指代coinjoin交易。混合更多是指coinjoin核心的过程。同时，重要的是不要将通过coinjoins的混合与通过一个中央参与者进行混合混淆，后者在过程中会占有比特币。这与coinjoin的过程无关，在coinjoin过程中，用户不会失去对其比特币的控制。*