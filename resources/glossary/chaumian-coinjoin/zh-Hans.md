---
term: CHAUMIAN COINJOIN
---

CHAUMIAN COINJOIN是一种利用David Chaum的盲签名和Tor进行参与者与协调者服务器之间通信的coinjoin协议。CHAUMIAN COINJOIN的目标是确保参与者，协调者既不能窃取比特币，也不能将输入和输出联系起来。

为了实现这一点，用户向协调者提交他们的输入和一个加密的盲化接收地址。这个地址一旦被揭开盲化，就意味着要从coinjoin中接收比特币作为输出。协调者对这些令牌进行签名并将它们返回给用户。然后用户通过一个新的Tor身份匿名重新连接到协调者的服务器，并以明文形式揭示他们的输出地址以构建交易。协调者可以验证所有这些接收地址都来自合法用户，因为他之前已经用他的私钥对它们的盲化版本进行了签名。然而，他不能将特定的输出地址与给定的输入用户关联起来。因此，即使从协调者的角度看，输入和输出之间也没有联系。一旦交易由协调者构建完成，他就将其发送回参与者，参与者在验证他们的输出确实在此交易中后签名以解锁他们的输入。参与者将签名发送给协调者。一旦收集到所有签名，协调者就可以在比特币网络上广播coinjoin交易。

![](../../dictionnaire/assets/38.png)

这种方法确保了协调者在整个coinjoin过程中既不能妥协参与者的匿名性，也不能窃取比特币。

很难确定谁最先在比特币上引入了coinjoin的概念，以及谁想到在这个背景下使用David Chaum的盲签名。人们通常认为Gregory Maxwell是第一个在2013年[BitcoinTalk上的一条消息中](https://bitcointalk.org/index.php?topic=279249.0)讨论它的人：

> *"通过使用Chaum盲签名：用户连接并提供输入（和找零地址）以及他们希望发送他们的私人硬币的地址的加密盲化版本；服务器签署令牌并返回它们。用户匿名重新连接，揭示他们的输出地址，并将它们返回给服务器。服务器可以看到所有输出都已经由他签名，因此，所有输出都来自有效参与者。后来，人们重新连接并签名。"*

Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privacy for the real world*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0
然而，早期也有提及Chaum签名在混币以及coinjoin方面的应用。[2011年6月，Duncan Townsend在BitcoinTalk上发表了一篇帖子](https://bitcointalk.org/index.php?topic=12751.0)，介绍了一种使用Chaum签名的混币器，其方式与现代Chaumian coinjoin非常相似。在同一个讨论帖中，还有[hashcoin回复Duncan Townsend的消息](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793)，提出改进其混币器的建议。这条消息准确地介绍了最接近coinjoin的内容。还有，在[2012年Alex Mizrahi的一条消息中](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry)也提到了一个类似的系统，当时他正在为Tenebrix的创造者提供建议。"coinjoin"这个术语本身并非由Greg Maxwell发明，而是来自Peter Todd的一个想法。