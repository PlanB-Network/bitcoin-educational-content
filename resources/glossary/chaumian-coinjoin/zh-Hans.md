---
term: CHAUMIAN COINJOIN

---
一种利用 David Chaum 的盲签名和 Tor 进行参与者与协调者服务器之间通信的混币协议。Chaumian 混币协议的目标是确保参与者的比特币不会被协调者窃取，也不会将输入和输出连接在一起。

为此，用户向协调者提交他们的输入和一个加密盲接收地址。这个地址一旦解密，就会接收比特币，作为币合的输出。协调者签署这些代币并将其返还给用户。然后，用户以新的 Tor 身份匿名重新连接到协调者的服务器，并以明文形式透露他们的输出地址，以便构建交易。协调者可以验证所有这些接收地址都来自合法用户，因为他之前已经用自己的私钥对这些地址的盲文版本进行了签名。但是，他无法将特定的输出地址与给定的输入用户联系起来。因此，即使从协调者的角度来看，输入和输出之间也没有联系。一旦交易由协调者构建完成，他就会将其发送回参与者，参与者在验证其输出确实在此交易中后，就会签署该交易以解锁其输入。参与者将签名发送给协调者。一旦收集到所有签名，协调者就可以在比特币网络上广播该 Coinjoin 交易。

![](../../dictionnaire/assets/38.webp)

这种方法可以确保协调者在整个硬币加入过程中既不会破坏参与者的匿名性，也不会窃取比特币。

很难确定是谁最先在比特币上提出了 “混币”（coinjoin）的概念，也很难确定是谁最先想到在比特币上使用 David Chaum 的盲签名（blind signatures）。人们通常认为 Gregory Maxwell 在[2013 年 BitcoinTalk 上的一条消息](https://bitcointalk.org/index.php?topic=279249.0)中首先讨论了这个问题：

> *"通过使用Chaum盲签名：用户连接并提供输入（和更改地址）以及他们想要发送私人硬币的地址的加密盲版；服务器签署代币并将其返回。用户以匿名方式重新连接，解除对输出地址的屏蔽，并将其返回给服务器。服务器可以看到所有输出都已由他签名，因此所有输出都来自有效的参与者。之后，人们重新连接并签名。
Maxwell, G. (2013, August 22). *CoinJoin：现实世界的比特币隐私*.BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

不过，还有其他更早的说法，既有在混合中使用Chaum签名的，也有使用硬币接合的。[2011年6月，Duncan Townsend 在 BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0)上引进了一种混合器，它使用 Chaum 签名的方式与现代的 Chaumian coinjoin 十分相似。在同一主题中，有[一条来自哈希币的回复Duncan Townsend的信息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)来改进他的混币器。这条信息恰恰提出了与硬币接合最相似的地方。在 [Alex Mizrahi 2012 年的一条信息](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry) 中也提到了类似的系统，当时他正在为 Tenebrix 的创建者提供建议。coinjoin 这一词本身并不是 Greg Maxwell 发明的，而是来自 Peter Todd 的一个想法。
