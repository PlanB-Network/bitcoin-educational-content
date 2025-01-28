---
term: COINJOIN

---
Coinjoin 是一种用于破解比特币可追溯性的技术。它依赖于具有同名特定结构的协作交易：Coinjoin 交易。Coinjoin 交易通过增加外部观察者分析交易的难度，有助于改善比特币用户的隐私保护。这种结构允许在单个交易中混合多个硬币，从而难以确定输入和输出地址之间的联系。

Coinjoin 的一般操作如下：希望混合的不同用户存入一个金额作为交易的输入。这些输入将产生相同金额的不同输出。在交易结束时，无法确定哪个输出属于哪个用户。从技术上讲，投币交易的输入和输出之间没有任何联系。每个用户和每个 UTXO 之间的链接都已中断，就像每个硬币的历史记录一样。

![](../../dictionnaire/assets/4.webp)

为了使用户在任何时候都不会失去对其资金的控制，交易首先由协调器构建，然后传送给每个用户。每个用户在确认交易适合自己后，在自己这边签名，然后将所有签名添加到交易中。如果用户或协调人试图通过修改币合交易的输出来窃取他人的资金，那么签名将无效，交易将被节点拒绝。为了避免与输入挂钩，参与者的输出记录使用了乔姆盲签，这种情况被称为 "乔姆硬币连接"。

这种机制无需修改比特币协议即可提高交易的保密性。Whirlpool、JoinMarket 或 Wabisabi 等具体的 Coinjoin 实现方案提供了促进参与者之间协调过程的解决方案，并提高了 Coinjoin 交易的效率。下面是一个 Coinjoin 交易的例子：

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

很难确定是谁最先在比特币上提出了 "币合"（coinjoin）的概念，又是谁想到在这种情况下使用大卫-乔姆（David Chaum）的盲签名。人们通常认为是格雷戈里-麦克斯韦尔（Gregory Maxwell）在[2013 年 BitcoinTalk 上的一条信息](https://bitcointalk.org/index.php?topic=279249.0)中首先讨论了这个问题：

使用 Chaum 盲签名：用户连接并提供输入（和更改地址），以及他们希望发送私人硬币的加密盲版地址；服务器签署代币并返回。用户以匿名方式重新连接，解除对其输出地址的屏蔽，并将其发送回服务器。服务器可以看到所有输出都已由其签名，因此所有输出都来自有效的参与者。之后，人们重新连接并签名。

Maxwell, G. (2013, August 22). *CoinJoin：现实世界的比特币隐私*.BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

不过，早先也有人提到过混合中的Chaum签名和币币连接。[2011年6月，邓肯-汤森（Duncan Townsend）在BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0)上介绍了一种混合器，该混合器使用Chaum签名的方式与现代Chaumian币币接合十分相似。在同一主题中，还有[哈希币回复邓肯-汤森的信息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)来改进他的混合器。这条信息提出了最接近于硬币接合的方式。在[亚历克斯-米兹拉希（Alex Mizrahi）2012 年的一条信息](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry)中也提到了类似的系统，当时他正在为 Tenebrix 的创建者提供建议。coinjoin "一词本身并非格雷格-麦克斯韦尔（Greg Maxwell）发明，而是来自彼得-托德（Peter Todd）的一个想法。

> ► *术语 "coinjoin "没有法语翻译。一些比特币玩家也使用 "混合"、"mixing "或 "mixage "来指代币合交易。混合 "是 "接币 "的核心过程。此外，重要的是不要混淆通过 Coinjoins 进行的混合和通过一个中心行为者进行的混合，后者在混合过程中占有比特币。这与用户在过程中不会失去对其比特币控制权的 Coinjoin 毫无关系*。