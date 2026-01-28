---
name: Ashigaru - Whirlpool Coinjoin
description: 如何在 Ashigaru 应用程序上进行硬币接合？
---

![cover](assets/cover.webp)



"*街头的比特币wallet*"



在本教程中，您将了解什么是硬币接合，以及如何使用 Ashigaru Terminal 应用程序和 Whirlpool 实现（一种继承自 Samourai Wallet 的硬币接合协议）进行硬币接合。



## Whirlpool 型同轴接头的工作原理



在本教程中，我将不再赘述币合的概念、币合的作用或 Whirlpool 的理论操作，因为 Plan ₿ Academy 上的 BTC 204 培训课程的第 5 部分已经详细解释了这些主题。如果您还没有掌握 Whirlpool 的操作或硬币连接的原理，我强烈建议您在继续学习之前先查阅第 5 部分：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

不过，这里有一些简单的事实和数据可能会派上用场。



Whirlpool 兼容型投资组合使用 4 个独立账户，以满足投币过程的需要：




- 以索引 `0'` 标识的**存款**账户；
- 以 "2 147 483 644 "为索引的**坏银行**（或*有毒交换*）账户；
- 以 "2 147 483 645 "为索引的**Premix**账户；
- 以 "2 147 483 646 "为索引的**混合后**账户。



在 2025 年 11 月的 Ashigaru 上，有两种面值的现金池可供选择（这一列表可能会在未来几个月中不断变化：因此，请记得在阅读时检查其面值）：




- 0.25 BTC`，报名费为 `0.0125 BTC`；
- 0.025 BTC，报名费为 0.00125 BTC。



每个混合周期的输入和输出可涉及 5 到 10 个 UTXO。



![Image](assets/fr/01.webp)



## 软件要求



要使用 Whirlpool 进行联接，您需要三个独立的程序：





- Ashigaru Terminal**，可让您直接在电脑上管理您的金币连接；



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**是一款智能手机应用程序，您可以随时随地在*postmix*中使用比特币；



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**，一种 Bitcoin 节点实施方案，可确保您与网络的主权连接，无需依赖第三方服务器。



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

按照各自的教程安装这些工具，然后就可以开始制作第一个硬币拼接了。



## 接收比特币



创建您的投资组合后，您将从一个以索引 "0 "标识的账户开始。这就是 `Deposit` 账户。您将向该账户发送用于 Coinjoins 的比特币。您可以通过 Ashigaru 应用程序（请参阅专门教程的第 5 部分）或 Ashigaru 终端（同样在专门教程的第 5 部分中有详细说明）接收比特币。



一旦您的存款账户中至少有参与最小资金池所需的金额（加上服务费和支付 mining 费用所需的最低金额），您就可以开始首次投币了。



![Image](assets/fr/02.webp)



## 使 Tx0



资金到达您的存款账户并确认交易后，您就可以开始加入硬币的过程了。为此，请在 Ashigaru Terminal 上打开 "钱包 "菜单，然后选择您的 wallet。如果您的 wallet 已锁定，软件会要求您输入密码和 passphrase。



![Image](assets/fr/03.webp)



然后选择 "存款 "账户。



![Image](assets/fr/04.webp)



转到 `UTXOs` 菜单。



![Image](assets/fr/05.webp)



在此，您将看到存款账户中所有 UTXO 的列表。选择您希望在币合循环中发送的UTXO。



为提高保密性并避免 *Common Input Ownership Heuristic (CIOH)*，建议在 Whirlpool 中每个输入只使用一个 UTXO（有关该原则的详细解释，请参阅 BTC 204）。



按键盘上的 "ENTER "键选择一个 UTXO：旁边会出现一个星号"(*)"，表示该 UTXO 已被选中。



![Image](assets/fr/06.webp)



然后点击 "已选混音 "按钮。



![Image](assets/fr/07.webp)



如果您的 UTXO 足够大，可以参加两个可用池中的任何一个，您可以使用箭头选择目标池。在此页面，您将看到 Tx0 的详细信息：




- 将进入池中的UTXO 数量；
- 适用的各种费用（服务费和 mining 费用） ；
- 毒性变化*的量。



仔细检查信息，然后单击 "广播 "以广播 Tx0。



![Image](assets/fr/08.webp)



然后，Ashigaru 会显示 Tx0 的 TXID，确认交易已在网络上广播。



![Image](assets/fr/09.webp)



## 进行联接



播放 Tx0 后，返回存款账户主页，然后点击 "账户"，选择 "Premix "账户。



![Image](assets/fr/10.webp)



在 "UTXOs "菜单中，您将看到各种均衡部件，随时准备进入共混循环。一旦确认 Tx0，Ashigaru Terminal 将自动启动第一个混合周期。



![Image](assets/fr/11.webp)



一旦 Tx0 得到确认，Ashigaru 终端将自动创建和广播第一笔 Coinjoin 交易。进入 "账户 > Postmix > UTXOs"，您可以查看您的均衡 UTXOs，等待确认其第一个周期。



![Image](assets/fr/12.webp)



现在，您可以让 Ashigaru Terminal 在后台运行：它将继续自动混音和混编您的曲目。



## 完成硬币接合



现在，您可以让您的硬币自动重新混合。Whirlpool 模式意味着无需为混币支付额外费用：无服务费，无 mining 费用。因此，让您的钱币参与更多的混合循环只会有利于您的保密性。



要想更好地了解这种机制以及值得等待的周期，我建议您阅读这篇文章：



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

要查看每个作品的混音次数，请打开 "Postmix "账户中的 "UTXOs "菜单。



![Image](assets/fr/13.webp)



要使用混合硬币，请访问 Ashigaru 应用程序，该程序使用与 Ashigaru 终端软件相同的 wallet。打开时显示的 wallet 与您的 "存款 "账户相对应。要访问包含混合 UTXOs 的 "Postmix "账户，请单击右上角的 Whirlpool 符号。



![Image](assets/fr/14.webp)



在这个账户中，您会看到您目前正在混合的所有金币。要使用它们，请按屏幕右下角的 "+"符号，然后选择 "发送"。



![Image](assets/fr/15.webp)



填写交易详情：收件人地址、发送金额，如果您愿意，还可以选择特定的交易结构，以进一步提高保密性（请参阅相应的教程）。



![Image](assets/fr/16.webp)



仔细检查交易详情，然后拖动屏幕底部的箭头确认发货。



![Image](assets/fr/17.webp)



您的交易已签署并在 Bitcoin 网络上广播。



![Image](assets/fr/18.webp)



## 花费有毒变化



请记住Whirlpool 的模型基于棋子在进入棋池之前在 Tx0 的均衡。正是这种机制打破了对UTXO的追踪。在我看来，这是最有效的联编模式，但它也有一个缺点：它产生的*变化*并没有经过联编过程。



这种变化对应于为每个 Tx0 创建的 UTXO。它被隔离在一个名为 "毒变 "或 "坏库"（取决于软件）的特定账户中，以避免与其他UTXO一起使用。这一点非常重要，因为这些UTXO并没有被混合：它们的可追踪链接保持完好无损，而且它们会在您和您的上币活动之间建立联系，从而危及您的机密性。因此，请小心处理，***不要与其他UTXO**一起使用，无论混合与否。将有毒的 UTXO 与混合的 UTXO 结合使用，会使您从联合硬币中获得的所有隐私收益化为乌有。



目前，Ashigaru 并不提供直接访问 "Doxxic Change "账户的功能（至少我还没有找到）。这一功能可能会在未来的更新中加入。在此期间，找回这些资金的唯一方法是将 seed 导入 Sparrow Wallet。后者通常会自动检测到这是与 Whirlpool 一起使用的 wallet，并允许您访问所有四个账户，包括 "Doxxic Change "账户。然后你就可以像使用普通比特币一样从 Sparrow 中使用这些 UTXOs 了。



以下是几种可能的策略，用于管理来自 coinjoins 的外汇 UTXOs，同时不损害您的隐私：





- 将它们混合到较小的池中：** 如果您的有毒 UTXO 足够大，可以加入一个较小的池，这通常是最好的选择。但要注意，千万不要为了达到这个目的而合并几个有毒的 UTXO，因为这样会在 Whirlpool 中的各个条目之间产生联系。





- 将其标记为不可支出：** 另一种谨慎的做法是将其保留在单独的账户中，不要动用。这样可以防止你不小心花掉它们。如果比特币的价值增加，可以开设适应其规模的新池。





- 进行捐赠：** 您可以选择将这些有毒的 UTXOs 转化为对 Bitcoin 开发人员、开源项目或接受 BTC 的协会的捐赠。这样，您就可以在支持生态系统的同时有效地处理这些UTXO。





- 购买预付礼品卡或 Visa 卡：** [Bitrefill](https://www.bitrefill.com/) 等平台可以将比特币兑换成礼品卡或可充值的 Visa 卡，在商店使用。这是一种简单而隐蔽的消费有毒 UTXO 的方式。





- 将它们换成门罗币：** Samourai Wallet 曾经提供一项现已停用的 BTC/XMR 原子交换服务。如果有类似的服务（我个人不知道有类似的服务），这是一个很好的解决方案，可以隔离这些 UTXO，将其转换为莫尼罗，然后最终将其送回 Bitcoin。不过，这种方法成本高昂，而且依赖于可用的流动性。





- 将它们转移到 Lightning Network：** 将这些 UTXOs 转移到 Lightning Network，以享受交易费用的减少，这可能是一个有趣的选择。不过，这种方法可能会泄露某些信息，具体取决于您对 "闪电 "的使用情况，因此应谨慎使用。



## 我怎样才能了解我们硬币接合循环的质量？



要使合并真正有效，输入和输出金额必须高度一致。这种一致性增加了外部观察者可能做出的解释的数量，反过来又增加了交易的不确定性。为了衡量这种不确定性，我们将熵的概念应用到交易中。在这方面，Whirlpool 模式是公认的最有效的模式之一，因为它保证了参与者之间的极佳同质性。如需更深入地了解这一原则，我建议您参考 BTC 204 培训课程第 5 部分的最后一章。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

硬币拼接循环的性能是通过硬币所隐藏的集合的大小来衡量的。这些集合定义了所谓的 "非集合"（*anonsets*）。有两种类型：第一种衡量面对回顾性分析（从现在到过去）的保密性，第二种衡量对前瞻性分析（从过去到现在）的抵抗力。有关这两个指标的完整解释，请阅读以下教程（或再次阅读 BTC 204 培训课程）：



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## 如何管理后混合？



在运行几个币合周期后，最好的策略是将UTXO 保留在 "混合后 "账户中，让它们无限期地重新混合，直到您真的需要使用它们时为止。



有些用户喜欢将混合比特币转移到由 wallet 硬件安全保护的 wallet。这种方法是可行的，但需要一定的严谨性，以确保通过币仓获得的机密性不被泄露。



合并UTXO 是最常见的错误。重要的是，切勿在同一事务中将混合的UTXO与未混合的UTXO合并，否则有可能触发*通用输入Ownership启发式（CIOH）*。这意味着要对UTXO进行严格管理，特别是通过清晰准确的标签。一般来说，合并 UTXOs 是一种不好的做法，如果管理不善，往往会导致失密。



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

在合并混合 UTXOs 时也应谨慎。如果UTXO具有显著的非集 中性，可以考虑进行有限的合并，但这样会不可避免地降低保密程度。避免在进行足够数量的混音之前进行大规模或仓促的合并，因为这可能会在混音前和混音后的作品之间建立推论联系。如有疑问，最好不要合并混音后的 UTXO，而是将它们逐一传输到 wallet 硬件，每次都生成一个新的空白接收地址。别忘了给每个传输的 UTXO 贴上标签。



我们强烈建议不要使用少数脚本将您的混合后UTXO移动到投资组合中。例如，如果您从 `P2WSH` 中的 multi-sig 投资组合中参与了 Whirlpool，那么与您共享此类脚本的人将为数不多。通过将您的混合后UTXOs发送到相同类型的脚本，您可以大大降低您的匿名性。除脚本类型外，其他特定的 wallet 指纹也会损害您的保密性，因此最好从 Ashigaru 应用程序中删除它们。



最后，与所有 Bitcoin 交易一样，切勿重复使用收款地址。每笔付款都必须发送到一个新的、唯一的空白地址。



最简单、最安全的方法是将混合后的UTXO存入 "混合后 "账户，让它们自然混合，只有在需要时才从芦之丸中支出。



Ashigaru 和 Sparrow 钱包采用了额外的保护措施，防止与区块链分析相关的最常见错误，帮助您保护交易的机密性。