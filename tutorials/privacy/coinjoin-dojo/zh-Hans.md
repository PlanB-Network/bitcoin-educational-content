---
name: Coinjoin - Dojo
description: 如何使用您自己的Dojo执行coinjoin？
---
![cover](assets/cover.webp)

***警告：** 继Samourai Wallet的创始人于4月24日被捕，其服务器被查封之后，Whirlpool工具不再运作，即使是拥有自己的Dojo或使用Sparrow Wallet的个人也是如此。然而，该工具在未来几周内可能会被重新启用或以不同的方式重新推出。此外，本文的理论部分对于理解coinjoins的原理和目标（不仅仅是Whirlpool），以及理解Whirlpool模型的有效性仍然相关。*

_我们正在密切关注此案件的发展以及与之相关工具的发展。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

---

在本教程中，您将学习什么是coinjoin以及如何使用Samourai Wallet软件和Whirlpool实现，利用您自己的Dojo来执行coinjoin。在我看来，这种方法目前是混合您的比特币的最佳方式。

## 什么是比特币上的coinjoin？
**Coinjoin是一种打破比特币在区块链上可追踪性的技术**。它依赖于一种具有特定结构的协作交易，即同名的coinjoin交易。

Coinjoins通过为外部观察者复杂化链分析来增强比特币用户的隐私。它们的结构允许将来自不同用户的多个硬币合并到单一交易中，从而模糊了路径，使得难以确定输入和输出地址之间的链接。

Coinjoin的原理基于协作方法：几个希望混合他们比特币的用户以相同的金额作为同一交易的输入。这些金额随后作为等值输出重新分配给每个用户。交易结束时，不可能将特定的输出与输入时已知的用户关联起来。输入和输出之间不存在直接链接，这打破了用户及其UTXO之间的关联，以及每个硬币的历史。
![coinjoin](assets/notext/1.webp)

Coinjoin交易示例（非我所做）：[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

为了在执行coinjoin时确保每个用户始终控制其资金，过程从由协调者构建交易开始，然后将其传输给参与者。每个用户在验证交易适合他们之后签名。最后将所有收集的签名整合到交易中。如果用户或协调者试图通过修改coinjoin交易的输出来转移资金，则签名将被证明无效，导致节点拒绝交易。

有几种实现coinjoin的方法，如Whirlpool、JoinMarket或Wabisabi，每种方法都旨在管理参与者之间的协调并提高coinjoin交易的效率。
在本教程中，我们将深入探讨**Whirlpool**的实现，我认为这是在比特币上执行coinjoin操作最高效的解决方案。尽管在几个钱包上都可以使用，但在本教程中，我们将专门探讨在没有Dojo的情况下，通过Samourai Wallet移动应用程序使用它的方法。
## 为什么要在比特币上执行coinjoins？
任何点对点支付系统的最初问题之一是双重支付：如何防止恶意个体多次花费同一货币单位，而不求助于中央权威来裁决？

中本聪通过比特币协议提供了解决这一难题的方法，这是一个独立于任何中央权威运作的点对点电子支付系统。在他的白皮书中，他强调，证明没有双重支付的唯一方法是确保支付系统内所有交易的可见性。

为了确保每个参与者都了解交易，必须公开披露这些交易。因此，比特币的运作依赖于一个透明和分布式的基础设施，允许任何节点操作者验证电子签名链的完整性以及每个硬币的历史，从其由矿工创建开始。

比特币区块链的透明和分布式特性意味着网络的任何用户都可以跟踪和分析所有其他参与者的交易。因此，在交易层面上实现匿名是不可能的。然而，在个人识别层面上，匿名性得到了保留。与每个账户都与个人身份相关联的传统银行系统不同，在比特币上，资金与一对加密密钥相关联，从而为用户提供了一种在加密标识符后面的伪匿名形式。

因此，当外部观察者设法将特定的UTXOs与已识别的用户关联起来时，比特币上的保密性就会受到损害。一旦建立了这种关联，就有可能追踪他们的交易并分析他们的比特币历史。Coinjoin正是为了打破UTXOs的可追踪性而开发的技术，从而在交易层面为比特币用户提供了一定程度的保密性。

## Whirlpool是如何工作的？
Whirlpool与其他coinjoin方法不同之处在于使用了“_ZeroLink_”交易，这确保了所有输入和所有输出之间绝对没有技术链接的可能性。通过一种结构实现了这种完美的混合，其中每个参与者贡献了相同数量的输入（挖矿费用除外），从而生成了完全相等数量的输出。
这种对输入的限制性方法赋予了Whirlpool coinjoin交易一个独特的特征：输入和输出之间完全缺乏确定性链接。换句话说，每个输出都有相同的可能性被任何参与者所拥有，与交易中所有其他输出相比。
最初，每个Whirlpool coinjoin的参与者数量限制为5个，包括2个新参与者和3个重混者（我们将在后面进一步解释这些概念）。然而，2023年观察到的链上交易费用的增加促使Samourai团队重新思考他们的模型，以在降低成本的同时提高隐私。因此，考虑到费用的市场情况和参与者数量，协调者现在可以组织包括6、7或8个参与者的coinjoins。这些增强的会话被称为“_Surge Cycles_”。重要的是要注意，无论设置如何，Whirlpool coinjoins总是只有2个新参与者。

因此，Whirlpool交易的特点是输入和输出的数量相同，可以是：
- 5个输入和5个输出；
![coinjoin](assets/notext/2.webp)
- 6个输入和6个输出；
![coinjoin](assets/notext/3.webp)
- 7个输入和7个输出；
![coinjoin](assets/notext/4.webp)- 8个输入和8个输出。
![coinjoin](assets/notext/5.webp)
Whirlpool提出的模型基于小型coinjoin交易。与Wasabi和JoinMarket不同，后两者的匿名集的强度依赖于单个周期内参与者的数量，Whirlpool则依赖于多个小型周期的链接。

在这个模型中，用户只在最初进入池时支付费用，允许他们参与多次重混而无需额外费用。是新加入者为重混者支付挖矿费用。

每当一个coin参与到额外的coinjoin中，连同其过去遇到的同伴，匿名集将呈指数级增长。因此，目标是利用这些免费的重混，每一次发生，都有助于增加每个混合coin关联的匿名集的密度。

Whirlpool的设计考虑了两个重要要求：
- 在移动设备上实施的可访问性，鉴于Samourai Wallet主要是一款智能手机应用；
- 重混周期的速度，以促进匿名集的显著增加。
这些必要条件指导了Samourai Wallet的开发者在设计Whirlpool时的选择，使他们限制了每个周期的参与者数量。参与者太少会妨碍coinjoin的效率，大大减少每个周期生成的匿名集，而参与者太多则会在移动应用上造成管理问题，并会阻碍周期的流动。
**最终，在Whirlpool上每次coinjoin的参与者数量无需过多，因为通过积累多个coinjoin周期来实现匿名集。**

[-> 了解更多关于Whirlpool匿名集的信息。](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### 池和coinjoin费用
为了让这些多个周期有效增加混合币的匿名集，必须建立一定的框架来限制使用的UTXO金额。Whirlpool因此定义了不同的池。

一个池代表一组希望一起混合的用户，他们同意使用UTXO的金额以优化coinjoin过程。每个池指定了UTXO的固定金额，用户必须遵守以参与。因此，要使用Whirlpool进行coinjoins，你需要选择一个池。目前可用的池如下：
- 0.5比特币；
- 0.05比特币；
- 0.01比特币；
- 0.001比特币（= 100,000 sats）。

通过将你的比特币加入一个池，它们将被分割以生成与池中其他参与者完全同质的UTXOs。每个池都有一个最大限额；因此，对于超过此限额的金额，你将被迫要么在同一个池内进行两次单独的入场，要么转移到另一个金额更高的池：

| 池（比特币） | 每次入场的最大金额（比特币） |
|--------------|------------------------------|
| 0.5          | 35                           |
| 0.05         | 3.5                          |
| 0.01         | 0.7                          |
| 0.001        | 0.025                        |
如前所述，当UTXO准备好被整合进coinjoin时，就被视为属于一个池。然而，这并不意味着用户就失去了它的所有权。**通过不同的混合周期，你仍然完全控制着你的密钥，因此，也就控制着你的比特币。**这就是coinjoin技术与其他集中式混合技术的区别所在。

要进入一个coinjoin池，必须支付服务费用以及挖矿费用。每个池的服务费是固定的，旨在补偿负责Whirlpool开发和维护的团队。

使用Whirlpool的服务费只需在进入池时支付一次。完成这一步骤后，你有机会参与无限次的重混，而无需支付任何额外费用。以下是每个池当前的固定费用：

| 池 (比特币) | 入场费 (比特币)        |
|------------|-----------------------|
| 0.5        | 0.0175                |
| 0.05       | 0.00175               |
| 0.01       | 0.0005 (50,000 sats)  |
| 0.001      | 0.00005 (5,000 sats)  |

这些费用本质上是为所选池的入场券，无论你在coinjoin中投入的金额是多少。因此，无论你是以正好0.01 BTC加入0.01池，还是以0.5 BTC进入，费用在绝对值上都保持不变。

因此，在进行coinjoins之前，用户有两种策略可供选择：
- 选择一个较小的池以最小化服务费，知道他们将收到几个小额的UTXO作为回报；
- 或者选择一个较大的池，同意支付更高的费用以获得较少数量的大额UTXO。

通常不建议在coinjoin周期后合并几个混合过的UTXO，因为这可能会破坏获得的保密性，特别是由于Common-Input-Ownership Heuristic (CIOH)。因此，选择一个较大的池，即使这意味着支付更多，也是为了避免在输出时有太多小额UTXO。用户必须权衡这些折中选择，以选择他们偏好的池。

除了服务费外，还必须考虑任何比特币交易固有的挖矿费用。作为Whirlpool用户，你将被要求支付准备交易（`Tx0`）以及第一次coinjoin的挖矿费用。所有后续的重混都将是免费的，这得益于Whirlpool的模型，该模型依赖于新参与者的支付。

实际上，在每次Whirlpool coinjoin中，输入中的两个用户是新参与者。其他输入来自重混者。因此，交易中所有参与者的挖矿费用由这两个新参与者承担，他们随后也将从免费的重混中受益：
![coinjoin](assets/en/6.webp)
得益于这种费用系统，Whirlpool真正地从其他coinjoin服务中脱颖而出，因为UTXOs的匿名集并不与用户支付的价格成正比。因此，仅通过支付池的入场费和两笔交易（`Tx0`和初始混合）的挖矿费用，就有可能实现相当高水平的匿名性。
需要注意的是，用户在完成多次coinjoin后，从池中提取他们的UTXOs时，也必须支付挖矿费用，除非他们选择了`mix to`选项，我们将在下面的教程中讨论。

### Whirlpool使用的HD钱包账户
要通过Whirlpool执行coinjoin，钱包必须生成几个不同的账户。在HD（*分层确定性*）钱包的上下文中，一个账户构成了与其他账户完全隔离的部分，这种分离发生在钱包层次结构的第三层深度，即`xpub`的层级。

理论上，一个HD钱包可以派生出多达`2^(32/2)`个不同的账户。默认使用的初始账户，对应于索引`0'`。

对于适应Whirlpool的钱包，如Samourai或Sparrow，使用4个账户来满足coinjoin过程的需求：
- **存款**账户，由索引`0'`标识；
- **坏账**（或doxxic change）账户，由索引`2 147 483 644'`标识；
- **预混**账户，由索引`2 147 483 645'`标识；
- **后混**账户，由索引`2 147 483 646'`标识。

这些账户中的每一个都在coinjoin中扮演特定的功能。

所有这些账户都链接到一个单一的种子，这允许用户使用他们的恢复短语和必要时的密码短语，恢复访问他们所有的比特币。然而，在这个恢复操作期间，必须向软件指定所使用的不同账户索引。

现在让我们来看看在这些账户中Whirlpool coinjoin的不同阶段。

### Whirlpool上coinjoins的不同阶段
**阶段1：Tx0**
任何Whirlpool coinjoin的起点都是**存款**账户。当你创建一个新的比特币钱包时，这个账户是你自动使用的账户。这个账户必须用希望混合的比特币充值。
`Tx0`代表Whirlpool混合过程的第一步。它旨在通过将它们分割成与所选池量相对应的单位来准备和均衡UTXO，以确保混合的同质性。然后，均衡的UTXO被发送到**预混**账户。至于不能进入池的差异，它被分离到一个特定的账户：**坏账**（或"doxxic change"）。
这个初始交易`Tx0`还用于支付混合协调员的服务费用。与后续步骤不同，这笔交易不是协作性的；用户因此必须承担所有的挖矿费用：
![coinjoin](assets/en/7.webp)

在这个`Tx0`交易的例子中，我们的**存款**账户的一个输入`372,000 sats`被分割成几个输出UTXO，分布如下：
- 一个`5,000 sats`的金额用于协调员的服务费，对应于进入`100,000 sats`池的费用；
- 三个为混合准备的UTXO，重定向到我们的**预混**账户并向协调员注册。这些UTXO在`108,000 sats`每个，以支付它们未来初始混合的挖矿费用；
- 无法进入池的剩余部分，因为太小而被视为有毒变化。它被发送到其特定账户。在这里，这种变化相当于`40,000 sats`;
- 最后，有`3,000 sats`不构成输出，但是是确认`Tx0`所必需的挖矿费用。

例如，这里有一个真实的Whirlpool Tx0（不是我的）：[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**第二步：有毒变化**
无法整合进池的剩余部分，在这里相当于`40,000 sats`，被重定向到**坏账**账户，也被称为“有毒变化”，以确保与钱包中其他UTXO的严格分离。

这个UTXO对用户的隐私是危险的，因为它不仅仍然与其过去相关联，因此可能与其所有者的身份相关联，而且还被标记为属于执行了coinjoin的用户。
如果这个UTXO与混合输出合并，他们将失去在coinjoin周期中获得的所有保密性，特别是因为共同输入所有权启发式（CIOH）。如果它与其他有毒变化合并，用户风险失去保密性，因为这将链接coinjoin周期的不同输入。因此，必须谨慎处理。如何管理这个有毒UTXO将在本文的最后部分详细说明，未来的教程将在PlanB网络上更全面地覆盖这些方法。

**第三步：初始混合**
完成`Tx0`后，等值的UTXOs被发送到我们钱包的**预混**账户，准备引入它们的第一个coinjoin周期，也称为“初始混合”。如果像我们的例子那样，`Tx0`生成了几个用于混合的UTXOs，每个都将被整合到一个单独的初始coinjoin中。

在这些第一次混合结束后，**预混**账户将为空，而我们的硬币，在支付了这第一次coinjoin的挖矿费用后，将被精确调整到所选池定义的金额。在我们的例子中，我们初始的UTXOs的`108 000 sats`将被减少到正好`100 000 sats`。
![coinjoin](assets/en/8.webp)
**第四步：重新混合**
初始混合后，UTXOs被转移到**后混**账户。这个账户收集已经混合的UTXOs和那些等待重新混合的UTXOs。当Whirlpool客户端活跃时，位于**后混**账户的UTXOs自动可用于重新混合，并将被随机选择参与这些新的周期。

作为提醒，然后重新混合是100%免费的：不需要额外的服务费或挖矿费。因此，保持UTXOs在**后混**账户中，维持它们的价值不变的同时，提高了它们的匿名集。这就是为什么允许这些硬币参与多个coinjoin周期很重要。这对你来说严格意义上没有任何成本，而且它增加了它们的匿名度。
当您决定花费混合后的UTXOs时，可以直接从这个**postmix**账户进行。建议将混合后的UTXOs保留在此账户中，以便从免费的重新混合中受益，并避免它们离开Whirlpool循环，这可能会降低它们的保密性。
正如我们将在接下来的教程中看到的，还有一个`mix to`选项，它提供了将您混合后的硬币自动发送到另一个钱包（例如冷钱包）的可能性，这是在定义的一定数量的coinjoins之后。
在讲解理论之后，让我们通过一个教程实践一下如何通过Samourai Wallet Android应用使用Whirlpool，该应用与您自己的Dojo上的Whirlpool CLI和GUI同步！
## 教程：通过您自己的Dojo进行Whirlpool Coinjoin
使用Whirlpool有很多选项。我在这里要介绍的是Samourai Wallet选项，这是一个在Android上的开源比特币钱包管理应用，但这次是**带着您自己的Dojo**。

通过Samourai Wallet使用您自己的Dojo进行coinjoins，在我看来，是迄今为止在比特币上进行coinjoins的最有效策略。这种方法需要一些初始设置方面的投资，但一旦到位，它就提供了持续混合和重新混合您的比特币的可能性，每天24小时，每周7天，无需全时保持Samourai应用程序活跃。事实上，由于Whirlpool CLI在比特币节点上运行，您始终准备好参与coinjoins。然后，Samourai应用程序让您有机会随时随地直接从您的智能手机花费您的混合资金。此外，这种方法的优势在于永远不会将您连接到Samourai团队管理的服务器，从而保护您的`xpub`免受任何外部暴露。

因此，这种技术非常适合那些寻求最大隐私和最高质量coinjoin周期的人。然而，它需要您有一个比特币节点可用，并且，正如我们稍后将看到的，需要一些设置。因此，它更适合中级到高级用户。对于初学者，我建议通过这两个其他教程熟悉coinjoin，这些教程展示了如何从Sparrow Wallet或Samourai Wallet（无Dojo）进行操作：
- **[Sparrow Wallet coinjoin教程](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Samourai Wallet coinjoin教程（无Dojo）](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**。

### 理解设置
首先，您需要一个Dojo！Dojo是基于Bitcoin Core的比特币节点实现，由Samourai团队开发。

要运行您自己的Dojo，您可以选择独立安装Dojo节点，或者利用另一个“盒装节点”比特币节点解决方案之上的Dojo。目前，可用的选项包括：
- [RoninDojo](https://ronindojo.io/)，这是一个增强了额外工具的Dojo，包括安装助手和管理助手。我在这个其他教程中详细介绍了设置和使用RoninDojo的程序：[RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2)；
- [Umbrel](https://umbrel.com/)带有“Samourai Server”应用程序；
- [MyNode](https://mynodebtc.com/)带有“Dojo”应用程序；
- [Nodl](https://www.nodl.eu/) 配备了 "Dojo" 应用程序；- [Citadel](https://runcitadel.space/) 配备了 "Samourai" 应用程序。
![coinjoin](assets/notext/9.webp)
在我们的设置中，我们将与三个不同的界面进行交互：
- **Samourai Wallet**，将托管我们专用于coinjoins的比特币钱包。这个免费的FOSS（自由和开源软件）应用程序可在Android上使用，允许你控制你的混币钱包，特别是从你的智能手机上花费你的postmix；
- **Whirlpool CLI**（_命令行界面_），将在托管Dojo的节点上运行。这个软件将能够访问你的Samourai钱包的密钥。它负责与协调器通信并持续管理coinjoins。它充当你的Samourai钱包在你的节点上的副本，随时准备参与coinjoins；
- **Whirlpool GUI**（_图形用户界面_），我们将使用的图形用户界面来监控Whirlpool CLI的活动并远程启动混币。Whirlpool GUI提供了Whirlpool CLI所执行操作的视觉表示。这个软件必须安装在与Dojo分开的计算机上。对于Umbrel、MyNode、Nodl和Citadel的用户来说，Whirlpool GUI是必需的。然而，对于RoninDojo，Whirlpool GUI界面已经通过`Whirlpool`应用集成到你的节点的网页界面中。因此，你不需要在另一台PC上安装它。

在我看来，使用RoninDojo是通过Dojo执行coinjoins的最佳解决方案。由于这个节点盒子软件与Samourai团队直接合作，RoninDojo在执行此操作方面更加优化。此外，Whirlpool GUI集成到网页界面显著简化了设置过程。在本教程中，我仍然会解释如何使用集成Dojo的其他解决方案（Umbrel、Nodl、MyNode和Citadel）来做到这一点。

### 准备你的Dojo
首先，你需要安装Dojo并获取QR码或链接，以便远程连接到它。这个链接是以`.onion`结尾的Tor地址。如果你使用的是RoninDojo，只需导航到`Pairing`菜单即可访问此信息。
![coinjoin](assets/notext/10.webp)

在`Samourai Dojo`下方，点击`Pair now`按钮。

![coinjoin](assets/notext/11.webp)

你的连接QR码和相应的链接将被显示。

![coinjoin](assets/notext/12.webp)

如果你在Umbrel上，前往App Store并搜索`Samourai Server`应用程序。它位于`Bitcoin`标签下。

![coinjoin](assets/notext/13.webp)

安装应用程序。

![coinjoin](assets/notext/14.webp)

打开应用程序后，你将能够访问连接到你的Dojo的QR码。

![coinjoin](assets/notext/15.webp)

如果你使用的是其他节点盒子软件，如MyNode、Citadel或Nodl，过程与Umbrel类似。你需要安装Samourai或Dojo应用程序以获取连接到你的Dojo所需的信息。

![coinjoin](assets/notext/16.webp)

### 准备你的Samourai Wallet
在检索到您的Dojo连接信息后，现在是时候为coinjoins设置您的钱包了。有两种情况：如果您的智能手机上还没有Samourai Wallet，过程很简单，只需创建一个新的即可。
另一方面，如果您已经有了Samourai Wallet，您将需要重新安装应用程序以将其与新的Dojo关联。这一步是必要的，因为只能在应用程序首次启动时建立与Dojo的连接。然而，由于Samourai在您的手机上自动生成的加密备份文件，这个过程简单且快速。

*如果您从未使用过Samourai，您可以跳过这些初步步骤，直接进行应用程序的安装。*

首先，确保您的Samourai Wallet应用程序是最新的。为此，请检查Google Play商店或将您的应用程序版本在`设置 > 其他`中的版本与Samourai网站上可用的版本进行比较。

![coinjoin](assets/notext/17.webp)

确保您有您的Samourai钱包恢复短语，并且它是可读的。然后，通过导航到`设置 > 故障排除 > 密码短语/备份测试`来测试您的BIP39密码短语，以确认其准确性。

![coinjoin](assets/notext/18.webp)
输入您的密码短语，然后验证Samourai确认其有效性。
![coinjoin](assets/notext/19.webp)

如果您的密码短语无效，或者您没有您的恢复短语，立即停止程序是必要的！**在此操作期间，您有丢失比特币的风险。**在这种情况下，建议将您的资金转移到另一个钱包，并开始使用一个新的空白Samourai钱包。只有在您确定拥有所有必要的备份信息并且您的密码短语有效的情况下，才应该继续进行以下步骤。

然后继续创建您的钱包的加密备份，并将其复制到您的剪贴板。要执行此操作，请点击屏幕右上角的三个小点，然后选择`导出钱包备份`。

![coinjoin](assets/notext/20.webp)

**从这一步开始，不要复制剪贴板上的任何其他内容！**保持您复制的备份绝对是必要的。

如果您正确执行了前面的步骤，您现在可以安全地删除您的Samourai钱包。为此，请前往：`设置 > 钱包 > 安全擦除钱包`。

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*如果您从未使用过Samourai并且从头开始安装应用程序，您可以在此步骤恢复教程。*

您的Samourai应用程序现在已重置。打开应用程序并按照您第一次使用它时的设置步骤进行操作。

![coinjoin](assets/notext/23.webp)

在下一步中，您将访问专门用于配置您的Dojo的页面。选择`Dojo`选项，然后输入您Dojo的登录信息。为此，您可以选择通过按`扫描QR码`来扫描信息。

![coinjoin](assets/notext/24.webp)

*对于Samourai的新用户，接下来将需要从头开始创建一个钱包。如果您需要帮助，您可以查阅在[此教程中，特别是在"创建软件钱包"部分](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)的设置新Samourai钱包的说明。*
如果您正在进行已存在的Samourai钱包的恢复，请选择`Restore existing wallet`，然后选择`I have a Samourai backup file`。
![coinjoin](assets/notext/25.webp)
通常，您应该始终将恢复文件保存在剪贴板中。然后点击`PASTE`将您的文件插入到指定位置。为了解密它，还需要在下方相应的字段中输入您钱包的BIP39密码短语。完成后，点击`FINISH`。
![coinjoin](assets/notext/26.webp)

然后，您将被重定向到您的Samourai钱包，这一次，它将连接到您自己的Dojo。

![coinjoin](assets/notext/27.webp)

### 安装Whirlpool GUI
现在是时候安装Whirlpool GUI了，这是一个图形用户界面，允许您从常用的PC管理您的coinjoin周期。对于RoninDojo用户，这一步不是必需的，因为可以直接通过`Apps > Whirlpool`在网页界面上管理coinjoins。然而，如果您使用的是另一种比特币“节点盒子”解决方案，那么进行这一安装是必须的。
![coinjoin](assets/notext/28.webp)
前往您的个人电脑，从官方Samourai Wallet网站下载与您的操作系统相对应的Whirlpool软件版本。

![coinjoin](assets/notext/29.webp)

在启动Whirlpool GUI之前，需要在您的机器上安装JAVA 8或更高版本。为此，[您可以安装OpenJDK](https://adoptium.net/)。
![coinjoin](assets/notext/30.webp)
您的电脑上还需要在后台运行Tor Daemon或Tor浏览器。确保在每次使用Whirlpool GUI会话之前启动Tor。如果您的机器上还没有安装Tor，[您可以从官方项目网站下载并安装](https://www.torproject.org/download/)，然后确保在后台启动它。

![coinjoin](assets/notext/31.webp)

一旦在您的系统上安装了JDK并且Tor在后台启动，您就可以启动Whirlpool GUI了。

![coinjoin](assets/notext/32.webp)

从Whirlpool GUI，点击`Advanced: Remote CLI`来连接您的Dojo上的Whirlpool CLI。您将需要您的Whirlpool CLI的Tor地址。

![coinjoin](assets/notext/33.webp)

要在Umbrel和其他“节点盒子”解决方案上找到您的Tor地址，只需启动Samourai Server或Dojo应用程序（根据使用的软件，名称可能有所不同）。Tor地址将直接在应用程序的页面上可见。
![coinjoin](assets/notext/34.webp)
在Whirlpool GUI中，输入您之前获得的Tor地址到`CLI address`字段。保留`http://`前缀，但不要在末尾添加`:8899`端口。只粘贴提供给您的地址。
![coinjoin](assets/notext/35.webp)
在Tor代理字段中，如果您使用的是Tor守护进程，请输入`socks5://127.0.0.1:9050`；如果是Tor浏览器，请输入`socks5://127.0.0.1:9150`。当您第一次通过Whirlpool GUI连接到Whirlpool CLI时，可以将API密钥字段留空。如果这不是您第一次连接，请在专用空间中输入您的API密钥。此密钥可以在与您的Tor地址相同的页面上找到。
![coinjoin](assets/notext/36.webp)

填写完所有信息后，点击`Connect`按钮。请等待，连接可能需要几分钟时间。

![coinjoin](assets/notext/37.webp)

### 将您的Samourai Wallet与Whirlpool GUI配对
*对于RoninDojo用户，您可以在此处继续教程。*

我们现在将配置好的Samourai钱包与Whirlpool GUI软件配对，或直接与RoninDojo配对，如果您使用的是这个软件的话。无论您使用的是Whirlpool GUI还是RoninDojo，都会要求您粘贴或扫描Samourai钱包的配对信息。

![coinjoin](assets/notext/38.webp)

要找到这些信息，请转到您钱包的设置。

![coinjoin](assets/notext/39.webp)

点击`Transactions`，然后点击`Pair to Whirlpool GUI`。

![coinjoin](assets/notext/40.webp)

Samourai随后会提供建立连接所需的信息。注意，这些数据很敏感！您可以通过直接复制或在点击QR码符号后使用计算机的摄像头扫描显示的QR码，将其传输到您的PC。

![coinjoin](assets/notext/41.webp)

完成此操作后，在Whirlpool GUI中选择`Initialize GUI`。请等待，因为这一步可能需要一些时间。

![coinjoin](assets/notext/42.webp)

无论您使用的是Whirlpool GUI还是RoninDojo，都会要求您输入Samourai钱包的密码短语。将其插入专用字段，然后按`Login`按钮继续。

![coinjoin](assets/notext/43.webp)

然后，您将到达Whirlpool CLI的主页

![coinjoin](assets/notext/44.webp)

### 从Whirlpool GUI启动coinjoins
*对于RoninDojo用户，遵循的过程是相同的。集成到RoninDojo中的Whirlpool应用界面提供与桌面上的Whirlpool GUI软件相同的选项和功能。因此，您可以以相同的方式遵循这些指示。*
现在一切都设置好了，您可以开始混合您的比特币了。要做到这一点，请将您希望混合的比特币转移到Samourai Wallet的**Deposit**账户。这个操作可以直接通过Samourai Wallet应用或在Whirlpool GUI上进行。从主页面，点击位于左上角的`+ Deposit`按钮。

![coinjoin](assets/notext/45.webp)
Whirlpool GUI 将生成一个接收地址。它还会显示参与每个coinjoin池所需的最低金额。这个金额会根据费用市场的不同而变化。建议存入略高于最低要求的金额，因为如果挖矿费用没有降低，您的UTXO可能不会被接受进入所期望的池中。因此，请将您的比特币发送到提供的地址。要获取新地址，只需点击 `更新地址` 按钮。
![coinjoin](assets/notext/46.webp)

一旦存款确认，您将能够在Whirlpool GUI的 **存款** 账户中看到它出现。

![coinjoin](assets/notext/47.webp)

要开始coinjoin周期，请选择您希望混合的UTXOs并按下 `预混` 按钮。请小心：如果您同时选择了几个不同的UTXOs，它们将在 `TX0` 准备交易期间被合并。这种合并可能会导致隐私降低，特别是如果UTXOs来自不同来源，因为共同输入所有权启发式（CIOH）。

![coinjoin](assets/notext/48.webp)

Whirlpool配置页面将打开。您可以选择您希望进入的池。同时选择用于 `TX0` 和首次coinjoins的挖矿费用。在此页面底部，一个摘要将向您展示doxxic变化的金额以及将被等化并包含在coinjoin周期中的UTXOs的金额和数量。如果您对此配置满意，请按下 `预混` 按钮开始coinjoin周期。
![coinjoin](assets/notext/49.webp)

一旦创建了 `TX0`，您将能够在 **预混** 账户中看到您的等化UTXOs，等待确认。为了让您的硬币能够自动重新混合，每天24小时、每周7天，我推荐激活 `自动混合预混和后混` 选项。您将在位于Whirlpool GUI窗口左侧的 `配置` 标签中找到此功能。
![coinjoin](assets/notext/50.webp)
开始coinjoins后，您可以退出Whirlpool GUI以及Samourai Wallet。只有您的节点需要保持连接，以便能够参与持续的coinjoins。然而，建议定期检查您的coinjoin周期的进展。如果您注意到您的UTXOs有一段时间没有被选中进行coinjoin，这可能表明有一个bug。在这种情况下，转到Whirlpool CLI并选择 `开始` 以重新开始您的coinjoins可用性。

![coinjoin](assets/notext/51.webp)

您的混合UTXOs可以从Whirlpool GUI的 **后混** 账户中看到。此外，您还可以通过Samourai Wallet上的Whirlpool界面直接查看和花费它们。要访问此菜单，请点击屏幕底部的蓝色 `+`，然后选择 `Whirlpool`。

![coinjoin](assets/notext/52.webp)

在Samourai Wallet上，Whirlpool账户通过它们的蓝色轻松识别。这使您可以随时随地直接从您的智能手机花费您的混合UTXOs。

![coinjoin](assets/notext/53.webp)
为了跟踪您的自动coinjoin交易，我还推荐通过Sentinel应用程序设置一个仅限查看的钱包。添加您的**Postmix**账户的ZPUB，并实时监控您的coinjoin周期的进展。如果您想了解如何使用Sentinel，我推荐咨询PlanB网络上的另一个教程：[**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)。