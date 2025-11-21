---
term: COINJOIN (混币)

---
Coinjoin 是一种用于破解比特币可追溯性的技术。它依赖于具有同名特定结构的协作交易：Coinjoin 交易。Coinjoin 交易通过增加外部观察者分析交易的难度，有助于改善比特币用户的隐私保护。这种结构允许在单个交易中混合多笔钱币，从而难以确定输入和输出地址之间的联系。

Coinjoin 的一般操作如下：想要进行混币的不同用户存入一个金额作为交易的输入。这些输入将产生相同金额的不同输出。在交易结束时，无法确定哪个输出属于哪个用户。从技术上讲，Coinjoin 交易的输入和输出之间没有任何联系。每个用户和每个 UTXO 之间的连接都已中断，每个钱币的历史记录也是一样。

![](../../dictionnaire/assets/4.webp)

为了使得用户在任何时候都不会失去对其资金的控制，交易首先由协调器构建，然后传送给每个用户。每个用户在确认交易适合自己后，在自己这边签名，然后将所有签名添加到交易中。如果用户或协调人试图通过修改币合交易的输出来窃取他人的资金，那么签名将变成无效，交易将被节点拒绝。为了隐瞒与输入的连接，参与者的输出记录使用了 Chaum 盲签名，这种情况被称为 “Chaumian Coinjoin”。

这种机制无需修改比特币协议即可提高交易的保密性。Whirlpool、JoinMarket 或 Wabisabi 等具体的 Coinjoin 实现方案提供了促进参与者之间协调过程的解决方案，并提高了 Coinjoin 交易的效率。下面是一个 Coinjoin 交易的例子：

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

很难确定是谁最先在比特币上提出了 coinjoin 的概念，又是谁想到在这种情况下使用 David Chaum 的盲签名。人们通常认为 Gregory Maxwell 在[2013 年 BitcoinTalk 上的一条信息](https://bitcointalk.org/index.php?topic=279249.0)中首先讨论了这个问题：

使用 Chaum 盲签名：用户连接并提供输入（和找零地址），以及他们希望发送私人硬币的加密盲版地址；服务器签署代币并返回。用户以匿名方式重新连接，解除对其输出地址的屏蔽，并将其发送回服务器。服务器可以看到所有输出都已由其签名，因此所有输出都来自有效的参与者。之后，人们重新连接并签名。

Maxwell, G. (2013, August 22). *CoinJoin：现实世界的比特币隐私*.BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

不过，早先也有人提到过钱币混合中的 Chaum 签名和coinjoin。[2011年6月，Duncan Townsend 在BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0)上引入了一种混合器，该混合器概念使用 Chaum 签名的方式与现代Chaumian coinjoin十分相似。在同一主题中，还有[哈希币回复Duncan Townsend的信息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)来改进他的钱币混合概念。这条信息提出了最接近于混币的方式。[Alex Mizrahi 于 2012 年的一条信息](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry)中也提到了类似的系统，当时他正在为 Tenebrix 的创建者提供建议。coinjoin 这一词本身并非由 Greg Maxwell 发明，而是来自 Peter Todd 的一个想法。

> ► *“coinjoin”这一术语没有法语翻译。一些比特币参与者也使用 “mix”、“mixing” 或 “mixage” 来指混币交易。混合是 “混币” 的核心过程。此外，重要的是不要混淆通过 Coinjoin 进行的混合和通过一个中心化机构进行的混币，后者在混合过程中占有比特币。这与用户在过程中不会失去对其比特币控制权的 Coinjoin 毫无关系*。
