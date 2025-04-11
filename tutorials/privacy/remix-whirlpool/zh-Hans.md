---
name: Remix - Whirlpool
description: Whirlpool应进行多少次混币重混？
---

![cover remix- wp](assets/cover.webp)

***警告：** 随着Samourai Wallet创始人在4月24日被捕以及其服务器被查封，Whirlpool统计工具不再提供下载，因为它托管在Samourai的Gitlab上。即使您之前已经将此工具下载到本地机器上，或者它已安装在您的RoninDojo节点上，WST此时将无法运行。它依赖于OXT.me提供的数据来运行，而这个网站现在无法访问。当前，由于Whirlpool协议处于非活动状态，WST并不特别有用。然而，这些软件在未来几周内可能会被重新启用的可能性仍然存在。此外，本文的理论部分对于理解coinjoin的原理和目标（不仅仅是Whirlpool），以及理解Whirlpool模型的有效性仍然相关。您还可以学习如何量化coinjoin周期所提供的隐私保护。*

_我们正在密切关注此案件以及相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

---

> *"打破你的硬币留下的链接"*

这是一个我经常被问到的问题。**在使用Whirlpool进行coinjoins时，应该进行多少次重混以达到令人满意的结果？**

coinjoin的目的是通过将你的硬币与一组无法区分的硬币混合，提供合理的否认性。这一行动的目标是打破从过去到现在以及从现在到过去的可追溯性链接。换句话说，一个知道你在coinjoin周期入口处的初始交易的分析师，不应该能够确定地识别出你在重混周期出口处的UTXO（从入口周期到出口周期的分析）。
![past-present links diagram](assets/en/1.webp)

相反，一个在coinjoin周期出口处知道你的UTXO的分析师，也应该无法确定原始交易在周期入口处的情况（从出口周期到入口周期的分析）。
![present-past links diagram](assets/en/2.webp)
然而，重混的次数并不是评估分析师在建立过去与现在之间或反之亦然的链接时遇到的困难的可靠标准。一个更相关的指标将是你的硬币隐藏的群组的大小。这些指标被称为“匿名集”。在Whirlpool的情况下，有两种类型的匿名集。

首先，我们可以确定你的UTXO在coinjoin周期出口处隐藏的群组的大小，即，这个群组内存在的无法区分的硬币数量。
![probable UTXOs at exit](assets/en/3.webp)
这个指标，在法语中被称为“prospective anonset”，在英语中称为“forward anonset”或“forward-looking metrics”，它允许我们评估您的硬币抵抗分析追踪其从coinjoin周期的进入到退出路径的能力。这个指标估计了您的UTXO在coinjoin过程中从其入口点到出口点抵抗重建其历史尝试的程度。例如，如果您的交易参与了其第一个coinjoin周期，并且进行了两个额外的下游周期，那么您的硬币的prospective anonset将是`13`：![forward anonset](assets/en/4.webp)
其次，另一个指标可以计算出来，以评估您的硬币抵抗从现在到过去的分析的能力。通过了解您在周期结束时的UTXO，这个指标确定了可能构成您在coinjoin周期中输入的Tx0交易的数量（从周期的结束到开始的分析）。这个指标衡量了分析师在您的硬币经过coinjoins之后追踪其起源的难度。![Probable sources at input](assets/en/5.webp)
这个指标的名称是“backward anonset”或“backward-looking metrics”。在法语中，我喜欢称之为“anonset rétrospectif”。在下面的图表中，这对应于所有的橙色Tx0气泡：
![backward anonset](assets/en/6.webp)
要了解更多关于这些指标计算方法的信息，我推荐阅读我在这个话题上的[Twitter线索](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20)。我们也在准备一篇关于PlanB网络的更全面的文章。

我知道提供的答案可能看起来不够满意，因为您希望得到一个特定的remix数量，我正在引导您查看文档。原因是remix的数量是一个不可靠的指标，用于评估在coinjoin周期中获得的匿名度。因此，不可能定义一个固定的remix数量作为一个绝对和普遍的安全阈值。

确实，您的硬币的每一个额外的remix都会增加其匿名集。然而，重要的是要理解，主要是您的同伴执行的remixes，为您的prospective anonset的增长做出贡献。通过Whirlpool模型，仅通过参与之前coinjoins的同伴的活动，您的交易就可以仅通过两到三个coinjoin周期就达到相当高的prospective anonset水平。

另一方面，retrospective anonset在我们的案例中不是一个问题。实际上，从您的初始coinjoin开始，您就从之前的池交易中获得了继承，立即给您的硬币一个高backward anonset，每个随后的周期都会有边际增加。
理解可信否认性的创建永远不是完整的也很重要。它依赖于追踪你的硬币的可能性。这种可能性随着隐藏它的群体大小的增加而降低。因此，你应该根据你的个人期望调整你的匿名集目标。问问自己，是什么原因促使你使用coinjoin以及实现这些目标所需的匿名程度。例如，如果使用coinjoin仅仅是为了在给你的教子发送一些sats作为生日礼物时保护你的钱包隐私，那么非常高的匿名程度是不必要的。你的教子可能无法进行深入的链分析，即使他们能够，这对你的生活也不会造成灾难性的后果。然而，如果你是一个威权政权的目标，哪怕是最微小的信息都可能导致监禁，你的行动就需要被更严格的标准指导。

要确定这些著名的匿名集指标，你可以使用一个名为**WST**（Whirlpool Stats Tool）的Python工具。

然而，并不总是需要计算你每一个coinjoin的硬币的匿名集。Whirlpool的设计本身就已经为你提供了保证。如前所述，回顾性匿名集很少是一个问题。从你的初始混合开始，你就已经获得了一个特别高的回顾性分数。至于前瞻性匿名集，你只需要将你的硬币保留在混币后账户中足够长的时间。例如，这是我一个`100,000 sats`硬币在coinjoin池中度过两个月后的匿名集分数：
![WST匿名集](assets/en/7.webp)
它显示了一个`34,593`的回顾性分数和一个`45,202`的前瞻性分数。具体来说，这意味着两件事：
- 如果一个分析师在周期结束时知道我的硬币并尝试追踪其来源，他们将遇到`34,593`个潜在来源，每个来源都有同等的可能性是我的。
- 如果一个分析师在周期开始时知道我的硬币并尝试确定其在结束时的对应关系，他们将面临`45,202`个可能的UTXOs，每个都有同样的可能性是我的。
这就是为什么我认为在`Hodl -> Mix -> Spend -> Replace`策略中使用Whirlpool特别相关。在我看来，最合逻辑的方法是将大部分储蓄以比特币形式保存在冷钱包中，同时不断地在Samourai上保持一定数量的硬币进行coinjoin以支付日常开销。一旦来自coinjoins的比特币被花费，它们就会被新的比特币替换，以返回到定义的混合硬币阈值。这种方法使我们能够摆脱对我们UTXOs匿名集的担忧，同时使coinjoins变得有效所需的时间变得不那么限制性。

我希望这个回答能对Whirlpool模型有所启发。如果你想了解更多关于比特币上coinjoins是如何工作的，我推荐阅读[我关于这个话题的全面文章](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2)。

**外部资源：**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
作为一名熟练的专业翻译人员，您的主要任务是将以下技术内容从英文准确翻译成简体中文。请遵循上述指南，以确保翻译的高质量：

- 如何安装和使用Whirlpool Stats Tools (WST) 进行CoinJoin交易的匿名集计算：[https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/](https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/)
  
- 深入了解Whirlpool的匿名集：[https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7).

请注意，这些链接仅供参考，以帮助您理解需要翻译的内容类型。实际翻译工作应基于上述指南进行，确保技术内容的完整性，同时确保翻译在简体中文中是可理解的并且在上下文上准确。