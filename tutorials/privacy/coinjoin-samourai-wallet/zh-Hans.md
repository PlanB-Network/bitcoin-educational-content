---
name: Coinjoin - Samourai Wallet
description: 如何在Samourai Wallet上执行coinjoin操作？
---
![cover](assets/cover.webp)

***警告：** 继Samourai Wallet的创始人于4月24日被捕，其服务器被查封之后，Whirlpool工具已经无法使用，即使是那些拥有自己的Dojo或使用Sparrow Wallet的个人也是如此。然而，这个工具在未来几周内可能会被重新启用或以不同的方式重新推出。此外，本文的理论部分对于理解coinjoin的原理和目标（不仅仅是Whirlpool），以及理解Whirlpool模型的有效性仍然具有相关性。*

_我们正在密切关注此案件以及相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息参考之用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其所在司法管辖区的法律。_

---

"*一个为街头而生的比特币钱包*"

在本教程中，您将学习什么是coinjoin以及如何使用Samourai Wallet软件和Whirlpool实现来执行coinjoin操作。

## 什么是比特币上的coinjoin？
**Coinjoin是一种打破比特币在区块链上可追踪性的技术**。它依赖于一种具有特定结构的协作交易：coinjoin交易。

Coinjoin通过使链上分析对外部观察者变得复杂，增强了比特币用户的隐私。它们的结构允许将来自不同用户的多个硬币合并到单一交易中，从而模糊了路径，使得难以确定输入和输出地址之间的联系。

Coinjoin的原理基于协作方法：几个希望混合他们的比特币的用户将相同金额作为同一交易的输入。这些金额随后作为等值输出分配给每个用户。交易结束时，不可能将特定的输出与输入中的已知用户关联起来。输入和输出之间不存在直接链接，打破了用户及其UTXO之间的关联，以及每个硬币的历史记录。
![coinjoin](assets/notext/1.webp)

Coinjoin交易示例（非本人所为）：[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

为了在执行coinjoin时确保每个用户始终控制其资金，过程从由协调者构建交易开始，然后将其传输给参与者。每个用户在确认交易适合自己后签名。最后将所有收集到的签名整合到交易中。如果用户或协调者试图通过修改coinjoin交易的输出来挪用资金，签名将被证明无效，导致节点拒绝该交易。

有几种实现coinjoin的方法，如Whirlpool、JoinMarket或Wabisabi，每种方法都旨在管理参与者之间的协调并提高coinjoin交易的效率。
在本教程中，我们将深入探讨**Whirlpool**的实现，我认为这是在比特币上执行coinjoins的最高效解决方案。尽管在几个钱包上都可以使用，但在本教程中，我们将专门探讨其与Samourai Wallet移动应用程序一起使用的情况，不涉及Dojo。
## 为什么要在比特币上执行coinjoins？
任何点对点支付系统的初始问题之一是双重支付：如何防止恶意个体多次花费同一货币单位，而不求助于中央权威来裁决？

中本聪通过比特币协议提供了解决这一难题的方法，这是一个独立于任何中央权威运作的点对点电子支付系统。在他的白皮书中，他强调，证明双重支付不存在的唯一方法是确保支付系统内所有交易的可见性。

为了保证每个参与者都知道交易，必须公开披露这些交易。因此，比特币的运作依赖于一个透明和分布式的基础设施，允许任何节点操作者验证电子签名链的完整性以及每个币的历史，从矿工创建它开始。

比特币区块链的透明和分布式特性意味着任何网络用户都可以跟踪和分析所有其他参与者的交易。结果是，交易级别的匿名是不可能的。然而，在个人识别级别上，匿名性得到了保留。与每个账户都与个人身份相关联的传统银行系统不同，在比特币上，资金与一对加密密钥相关联，从而为用户提供了在加密标识符后的一种伪匿名形式。

因此，当外部观察者设法将特定的UTXOs与已识别的用户关联起来时，比特币上的保密性就会受到威胁。一旦建立了这种关联，就有可能追踪他们的交易并分析他们的比特币历史。Coinjoin正是为了打破UTXOs的可追踪性而开发的技术，从而在交易级别为比特币用户提供了一定程度的保密性。

## Whirlpool是如何工作的？
Whirlpool与其他coinjoin方法不同之处在于使用了“_ZeroLink_”交易，这确保了所有输入和所有输出之间绝对没有技术链接的可能性。通过一种结构实现了这种完美的混合，其中每个参与者贡献了相同数量的输入（挖矿费用除外），从而生成了完全相等数量的输出。
这种对输入的限制性方法赋予了Whirlpool coinjoin交易一个独特的特征：输入和输出之间完全缺乏确定性链接。换句话说，每个输出都有与任何参与者相比，与交易中所有其他输出相同的被归属的概率。
最初，每个Whirlpool coinjoin的参与者数量限制为5个，包括2个新参与者和3个重混者（我们将进一步解释这些概念）。然而，2023年观察到的链上交易费用的增加促使Samourai团队重新思考他们的模型，以在降低成本的同时提高隐私。因此，考虑到费用的市场情况和参与者数量，协调者现在可以组织包括6、7或8个参与者的coinjoins。这些增强的会话被称为“_Surge Cycles_”。重要的是要注意，无论配置如何，Whirlpool coinjoins总是只有2个新参与者。

因此，Whirlpool交易的特点是输入和输出的数量相同，可以是：
- 5个输入和5个输出；
![coinjoin](assets/notext/2.webp)
- 6个输入和6个输出；
![coinjoin](assets/notext/3.webp)
- 7个输入和7个输出；
![coinjoin](assets/notext/4.webp)- 8个输入和8个输出。
![coinjoin](assets/notext/5.webp)
Whirlpool提出的模型基于小型coinjoin交易。与Wasabi和JoinMarket不同，后两者的匿名集的健壮性依赖于单个周期中参与者的数量，Whirlpool则依赖于多个小型周期的链接。

在这个模型中，用户只在最初进入池时支付费用，允许他们参与多次重混而无需额外费用。是新加入者为重混者支付挖矿费用。

每当一个硬币参与到一个额外的coinjoin中，与它在过去遇到的同伴一起，其匿名集将呈指数级增长。因此，目标是利用这些免费的重混，每一次发生，都有助于增强与每个混合硬币相关联的匿名集的密度。

Whirlpool的设计考虑了两个重要要求：
- 考虑到Samourai Wallet主要是一款智能手机应用，因此需要能够在移动设备上实现的可访问性；
- 重混周期的速度，以促进匿名集的显著增加。
这些必要条件指导了Samourai Wallet的开发者在设计Whirlpool时，使他们限制了每个周期的参与者数量。参与者太少会妨碍coinjoin的效率，极大地减少每个周期生成的匿名集，而参与者过多则会在移动应用上引起管理问题，并会阻碍周期的流动。
**最终，Whirlpool上每次coinjoin的参与者数量无需过多，因为通过累积多个coinjoin周期就能实现匿名集。**

[-> 了解更多关于Whirlpool匿名集的信息。](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### 池和coinjoin费用
为了让这些多个周期有效增加混合硬币的匿名集，必须建立一定的框架来限制使用的UTXO金额。Whirlpool因此定义了不同的池。

一个池代表一组希望一起混合的用户，他们同意使用UTXO的金额以优化coinjoin过程。每个池指定了UTXO的固定金额，用户必须遵守以参与。因此，要使用Whirlpool进行coinjoins，你需要选择一个池。目前可用的池如下：
- 0.5比特币；
- 0.05比特币；
- 0.01比特币；
- 0.001比特币（= 100,000 sats）。

通过将你的比特币加入一个池，它们将被分割以生成与池中其他参与者完全同质的UTXOs。每个池都有一个最大限额；因此，对于超过此限额的金额，你将被迫要么在同一个池中进行两次单独的加入，要么转向另一个金额更高的池：

| 池（比特币） | 每次加入的最大金额（比特币） |
|--------------|----------------------------|
| 0.5          | 35                         |
| 0.05         | 3.5                        |
| 0.01         | 0.7                        |
| 0.001        | 0.025                      |
如前所述，当UTXO准备好被整合进coinjoin时，被认为属于一个池。然而，这并不意味着用户失去了它的所有权。**通过不同的混合周期，你保留了对你的密钥的完全控制，因此，也就控制了你的比特币。**这就是coinjoin技术与其他集中式混合技术的区别所在。

要进入一个coinjoin池，必须支付服务费用以及挖矿费用。每个池的服务费是固定的，旨在补偿负责Whirlpool开发和维护的团队。

使用Whirlpool的服务费只需在进入池时支付一次。完成这一步骤后，你有机会参与无限次数的重混，而无需支付任何额外费用。以下是每个池的当前固定费用：

| 池 (比特币) | 入场费 (比特币)        |
|------------|-----------------------|
| 0.5        | 0.0175                |
| 0.05       | 0.00175               |
| 0.01       | 0.0005 (50,000 sats)  |
| 0.001      | 0.00005 (5,000 sats)  |

这些费用本质上充当了所选池的入场券，无论你在coinjoin中投入的金额是多少。因此，无论你是以正好0.01 BTC加入0.01池，还是以0.5 BTC进入，费用在绝对值上保持不变。

在进行coinjoins之前，用户因此在2种策略之间有选择：
- 选择一个较小的池以最小化服务费，知道他们将收到几个小额的UTXO作为回报；
- 或者选择一个较大的池，同意支付更高的费用以获得较少数量但价值更大的UTXO。

通常不建议在coinjoin周期后合并几个混合的UTXO，因为这可能会损害获得的保密性，特别是由于Common-Input-Ownership Heuristic (CIOH)。因此，选择一个较大的池，即使这意味着支付更多，也是明智的，以避免输出太多小额UTXO。用户必须权衡这些折中，以选择他们偏好的池。

除了服务费外，任何比特币交易固有的挖矿费用也必须考虑。作为Whirlpool用户，你将被要求支付准备交易（`Tx0`）以及第一次coinjoin的挖矿费用。所有后续的重混都将是免费的，这得益于Whirlpool的模型，该模型依赖于新参与者的支付。

实际上，在每个Whirlpool coinjoin中，输入中的两个用户是新参与者。其他输入来自重混者。因此，交易中所有参与者的挖矿费用由这两个新参与者承担，他们随后也将从免费的重混中受益：
![coinjoin](assets/en/6.webp)
得益于这种费用系统，Whirlpool真正地与其他coinjoin服务区分开来，因为UTXOs的匿名集并不与用户支付的价格成正比。因此，仅通过支付池的入场费和两次交易（`Tx0`和初始混合）的挖矿费用，就有可能实现相当高水平的匿名性。
请注意，用户在完成多次coinjoin后从池中提取他们的UTXOs时，也必须支付挖矿费用，除非他们选择了`mix to`选项，我们将在下面的教程中讨论。

### Whirlpool使用的HD钱包账户
要通过Whirlpool执行coinjoin，钱包必须生成几个不同的账户。在HD（*分层确定性*）钱包的上下文中，一个账户构成了与其他账户完全隔离的一个部分，这种分隔发生在钱包层次结构的第三层深度，即`xpub`的层级。

理论上，一个HD钱包可以派生出多达`2^(32/2)`个不同的账户。默认情况下，所有比特币钱包使用的初始账户对应于索引`0'`。

对于适配Whirlpool的钱包，如Samourai或Sparrow，使用4个账户来满足coinjoin过程的需求：
- **存款**账户，由索引`0'`标识；
- **坏账**（或doxxic change）账户，由索引`2 147 483 644'`标识；
- **预混**账户，由索引`2 147 483 645'`标识；
- **后混**账户，由索引`2 147 483 646'`标识。

这些账户中的每一个都在coinjoin过程中扮演特定的功能。

所有这些账户都链接到一个单一的种子，这允许用户使用他们的恢复短语和（如果适用）他们的密码短语恢复对所有比特币的访问权限。然而，在这种恢复操作中，必须向软件指定所使用的不同账户索引。

现在让我们看看在这些账户中Whirlpool coinjoin的不同阶段。

### Whirlpool上coinjoins的不同阶段
**阶段1：Tx0**
任何Whirlpool coinjoin的起点都是**存款**账户。当你创建一个新的比特币钱包时，这个账户是你自动使用的账户。这个账户必须用希望混合的比特币充值。
`Tx0`代表Whirlpool混合过程的第一步。它旨在通过将它们分成与所选池量相对应的单位来准备和均衡UTXO，以确保混合的同质性。然后，均衡的UTXO被发送到**预混**账户。至于不能进入池的差异，它被分离到一个特定的账户：**坏账**（或"doxxic change"）。
这个初始交易`Tx0`还用于支付混合协调员的服务费。与后续步骤不同，这笔交易不是协作性的；用户因此必须承担所有挖矿费用：
![coinjoin](assets/en/7.webp)

在这个`Tx0`交易的例子中，我们的**存款**账户的一个输入`372,000 sats`被分成几个输出UTXO，分布如下：
- 一个`5,000 sats`的金额用于协调员的服务费，对应于进入`100,000 sats`池的费用；
- 三个为混合准备的UTXO，重定向到我们的**预混**账户并注册给协调员。这些UTXO在`108,000 sats`每个，以覆盖它们未来初始混合的挖矿费用；
- 无法进入池的剩余部分，因其过小而被视为有害变化。它被发送到其特定账户。在这里，这种变化相当于`40,000 sats`;
- 最后，有`3,000 sats`不构成输出，但是这是确认`Tx0`所必需的挖矿费用。

例如，这里有一个真实的Whirlpool Tx0（不是我的）：[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**第二步：有害变化**
无法整合进池的剩余部分，在这里相当于`40,000 sats`，被重定向到**坏账**账户，也被称为“有害变化”，以确保与钱包中其他UTXO的严格分离。

这个UTXO对用户的隐私是危险的，因为它不仅仍然与其过去相关联，因此可能与其所有者的身份相关联，而且还被标记为属于执行了coinjoin的用户。
如果这个UTXO与混合输出合并，他们将失去在coinjoin周期中获得的所有保密性，特别是因为Common-Input-Ownership-Heuristic (CIOH)。如果它与其他有害变化合并，用户将因为这将链接不同的coinjoin周期的输入而失去保密性。因此，必须谨慎处理。如何管理这个有害UTXO将在本文的最后部分详细说明，未来的教程将在PlanB网络上更深入地介绍这些方法。

**第三步：初始混合**
`Tx0`完成后，等值UTXOs被发送到我们钱包的**预混**账户，准备引入它们的第一个coinjoin周期，也称为“初始混合”。如果，如我们的例子，`Tx0`生成了多个用于混合的UTXOs，每个都将被整合进一个单独的初始coinjoin。

在这些首次混合结束后，**预混**账户将为空，而我们的硬币，在支付了这第一次coinjoin的挖矿费用后，将被精确调整到所选池定义的金额。在我们的例子中，我们初始的`108 000 sats`UTXOs将被减少到精确的`100 000 sats`。
![coinjoin](assets/en/8.webp)
**第四步：重新混合**
初始混合后，UTXOs被转移到**后混**账户。这个账户收集了已经混合的UTXOs和等待重新混合的UTXOs。当Whirlpool客户端活跃时，**后混**账户中的UTXOs自动可用于重新混合，并将被随机选择参与这些新周期。

作为提醒，重新混合然后是100%免费的：不需要额外的服务费或挖矿费。因此，保持UTXOs在**后混**账户中，维持它们的价值不变的同时，还提高了它们的匿名集。这就是为什么允许这些硬币参与多个coinjoin周期很重要。这对你来说严格意义上没有任何成本，而且它增加了它们的匿名程度。
当您决定花费混合后的UTXOs时，可以直接从这个**postmix**账户进行。建议将混合后的UTXOs保留在此账户中，以便从免费的重新混合中受益，并避免它们离开Whirlpool循环，这可能会降低它们的保密性。
正如我们在接下来的教程中将看到的，还有一个`mix to`选项，它提供了将您混合后的硬币自动发送到另一个钱包（如冷钱包）的可能性，这是在定义的coinjoins次数之后。
在讲解理论之后，让我们通过Samourai Wallet Android应用的教程实践一下使用Whirlpool吧！
## 教程：在Samourai Wallet上使用Coinjoin Whirlpool
使用Whirlpool有许多选项。我在这里要介绍的是Samourai Wallet选项（不含Dojo），这是一个在Android上的开源比特币钱包管理应用程序。

在没有Dojo的情况下使用Samourai的优点是操作相当简单，设置快速，且除了一部Android手机和网络连接外不需要其他设备。

然而，这种方法有两个显著的缺点：
- Coinjoins只会在Samourai在后台运行且已连接时发生。这意味着，如果您想要24/7混合和重新混合您的比特币，您必须不断保持Samourai开启；
- 如果您在不连接自己的Dojo的情况下使用Samourai Wallet，那么您的应用程序将不得不连接到Samourai团队维护的服务器，并且您将向他们透露您钱包的`xpub`。这些匿名信息对您的应用程序找到您的交易是必需的。

克服这些限制的理想解决方案是在您个人的比特币节点上操作您自己的Dojo，与Whirlpool CLI实例关联。这样，您将避免任何信息泄露并实现完全独立。尽管下面介绍的教程对于某些目标或初学者来说是有用的，为了真正优化您的coinjoin会话，推荐使用您自己的Dojo。关于设置此配置的详细指南将很快在PlanB Network上提供。

### 安装Samourai Wallet
首先，您显然需要Samourai Wallet应用程序。您可以直接从官方网站使用APK下载它，从他们的GitLab下载，或从Google Play商店下载。

### 创建一个软件钱包
安装软件后，您需要继续在Samourai上创建一个比特币钱包。如果您已经有一个，可以直接跳到下一步。

打开应用程序后，按蓝色的`Start`按钮。然后，系统会要求您选择手机文件中的一个位置，用于存储新钱包的加密备份。

![samourai](assets/notext/9.webp)
通过点击对应的切换开关激活Tor。在这个阶段，您也可以选择一个特定的Dojo。然而，在这个教程中，我们将继续使用默认的Dojo；所以您可以禁用该选项。当Tor连接时，按`Create a new wallet`按钮。
![samourai](assets/notext/10.webp)

Samourai Wallet接着提示您设置一个BIP39密码短语。这个额外的密码非常重要，因为它直接作用于您的私钥的派生。这个密码短语的潜在丢失将导致无法访问您的比特币，使它们不可挽回地丢失。要恢复您的Samourai钱包，必须同时拥有您的12个单词的恢复短语和密码短语。
因此，选择一个强大的密码短语并制作一份或多份物理副本（在纸上或金属介质上）以确保您的比特币安全至关重要。完成这些任务后，勾选`我已了解在丢失的情况下...`的框，然后按`NEXT`按钮。
![samourai](assets/notext/11.webp)

然后您必须定义一个由5到8位数字组成的PIN码。这个代码将保护您手机上钱包的访问。每次您想打开Samourai应用时都会请求这个代码。选择一个强大的PIN码，并确保保留备份副本。之后，您可以按`NEXT`按钮。

![samourai](assets/notext/12.webp)

Samourai将邀请您再次输入PIN码以确认。输入它，然后按`FINALIZE`。

![samourai](assets/notext/13.webp)

然后您将访问由12个单词组成的恢复短语。这个短语允许您使用之前输入的密码短语恢复您的钱包。强烈建议在物理介质上（如纸张或金属材料）制作这个短语的一份或多份副本，以确保在出现问题时您的比特币的安全。

完成这些备份后，您将被引导到您的新Samourai钱包的界面。

![samourai](assets/notext/14.webp)

您将被提供获取您的PayNym Bot的机会。如果您愿意，可以请求它，尽管它对我们的教程来说不是必需的。

![samourai](assets/notext/15.webp)
在开始在这个新钱包上接收比特币之前，强烈建议重新检查您的钱包备份（密码短语和恢复短语）的有效性。要验证密码短语，您可以选择位于屏幕左上角的PayNym Bot图标，然后按照以下路径操作：
```plaintext
Settings > Troubleshooting > Passphrase/backup test
```

输入您的密码短语进行验证。

![samourai](assets/notext/16.webp)

Samourai将确认它是否有效。

![samourai](assets/notext/17.webp)

要验证您的恢复短语备份，请访问位于屏幕左上角的PayNym Bot图标，并按照此路径操作：
```plaintext
Settings > Wallet > Show 12-word recovery phrase
```

Samourai将显示一个带有您恢复短语的窗口。确保它与您的物理备份完全匹配。

为了进一步进行完整的恢复测试，请记下您钱包的一个见证元素，例如其中一个`xpubs`，然后继续删除您的钱包（前提是它仍然是空的）。目标是尝试仅使用您的物理备份恢复这个空钱包。如果恢复成功，这表明您的备份是有效和可靠的。

### 接收比特币
创建钱包后，您将从一个账户开始，由索引`0'`标识。这是我们在前面部分讨论的**存款**账户。您需要将打算用于coinjoins的比特币转移到这个账户。

为此，请点击屏幕右下角的蓝色`+`符号。

![samourai](assets/notext/18.webp)

然后点击绿色的`Receive`按钮。

![samourai](assets/notext/19.webp)

Samourai将自动生成一个新的空白地址来接收比特币。

![samourai](assets/notext/20.webp)
您可以将比特币发送到那里进行混币。
![samourai](assets/notext/21.webp)

### 制作Tx0
当交易被确认后，我们可以开始进行coinjoin过程。为此，请点击屏幕右下角的蓝色`+`按钮。

![samourai](assets/notext/22.webp)

然后点击蓝色的`Whirlpool`。

![samourai](assets/notext/23.webp)

等待Whirlpool初始化，Samourai创建必要的账户。

![samourai](assets/notext/24.webp)

然后你会进入Whirlpool首页。点击`Start`。
![samourai](assets/notext/25.webp)
选择你希望发送到coinjoin周期中的**存款**账户的UTXO，然后点击`Next`。

![samourai](assets/notext/26.webp)

在下一步中，你需要选择分配给`Tx0`以及你的第一次混币的费用等级。这个设置将决定你的`Tx0`和你的初始coinjoin（或初始coinjoins）的确认速度。请记住，`Tx0`和初始混币的挖矿费用由你负责，但你不必为后续的重新混币支付挖矿费用。你可以选择`Low`、`Normal`或`High`选项。

![samourai](assets/notext/27.webp)

在同一个窗口中，你可以选择你将进入的池。鉴于我最初选择了一个`454,258 sats`的UTXO，我的唯一可能选择是`100,000 sats`池。这个页面还向你展示了池的服务费，除了挖矿费用，这允许你知道这个coinjoin周期的总成本。如果一切适合你，选择适当的池并继续点击蓝色的`VERIFY CYCLE DETAILS`按钮。

![samourai](assets/notext/28.webp)

然后你可以看到你的coinjoin周期的所有细节：
- 将进入池的UTXOs数量；
- 发生的各种费用；
- doxxic变更的金额...

验证信息，然后点击绿色的`START CYCLE`按钮。

![samourai](assets/notext/29.webp)

一个窗口将出现，提供你将进入coinjoin周期产生的有毒变更标记为“不可花费”。选择`YES`，这个UTXO将在你的钱包中不可见，也不能被选择用于未来的交易。然而，它将在你钱包的UTXO列表中保持可访问，你可以手动更改其状态。建议选择此选项，以避免任何可能在以后危害你的隐私的操作错误。如果你选择`NO`，有毒变更将保持在你的钱包中可用。如果你想了解更多关于管理和使用这种有毒变更的信息，我建议你阅读本教程的最后一部分。

![samourai](assets/notext/30.webp)

Samourai将然后广播你的Tx0。

![samourai](assets/notext/31.webp)

### 进行coinjoins
一旦Tx0被广播，你可以在Whirlpool菜单的`Transactions`标签中找到它。

![samourai](assets/notext/32.webp)
您准备混合的UTXOs位于`Mixing in progress...`标签页中，对应于**Premix**账户。![samourai](assets/notext/33.webp)

一旦`Tx0`被确认，您的UTXOs将自动注册到协调器中，初始混合将自动依次开始。

![samourai](assets/notext/34.webp)

通过检查`Remixing`标签页，对应于**Postmix**账户，您将观察到来自初始混合的UTXOs。这些硬币将保持准备状态，以便进行后续的重新混合，这将不会产生任何额外费用。我推荐您阅读这篇其他文章，以了解更多关于重新混合过程和coinjoin周期的效率：[REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)。

![samourai](assets/notext/35.webp)

通过按下位于其右侧的暂停按钮，可以暂时暂停UTXO的重新混合。要使其再次符合重新混合的条件，只需再次点击同一个按钮。重要的是要注意，每个用户和每个池同时只能进行一次coinjoin。因此，如果您有6个`100 000 sats`的UTXOs准备进行coinjoin，那么只能混合其中一个。混合一个UTXO后，Samourai Wallet将随机选择您的一个新UTXO进行重新混合，以实现每个硬币混合的多样化和平衡。

![samourai](assets/notext/36.webp)

为了确保您的UTXOs持续可用于重新混合，需要在后台保持Samourai应用程序的活动状态。您应该在手机上看到一个通知，确认Whirlpool正在运行。关闭应用程序或关闭手机将暂停coinjoins。

### 完成coinjoins
要花费您混合的比特币，请转到Whirlpool菜单标签中注明`Remixing`的**Postmix**账户。

![samourai](assets/notext/37.webp)

点击位于右下角的蓝色Whirlpool标志。

![samourai](assets/notext/38.webp)

然后点击`Spend Mixed UTXOs`。

![samourai](assets/notext/39.webp)

然后，您可以像进行任何其他Samourai Wallet交易一样，输入收款人地址和要发送的金额。蓝色背景表明资金是从Whirlpool账户而非**存款**账户中支出的。

![samourai](assets/notext/40.webp)

通过点击右上角的3个小点，您可以选择特定的UTXOs。
![samourai](assets/notext/41.webp)
通过点击窗口右上角的白色方块，您可以使用相机扫描接收地址的二维码。

![samourai](assets/notext/42.webp)

输入您的支出交易所需的信息，然后点击蓝色的`VERIFY TRANSACTION`按钮。

![samourai](assets/notext/43.webp)
在下一步中，您可以选择修改与您的交易相关的费率。您还可以通过勾选相应的框来启用Stonewall选项。如果Stonewall选项不可选，这意味着您的**Postmix**账户中没有足够大小的UTXO来支持这种特定的交易结构。
[-> 了解更多关于Stonewall交易的信息。](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

如果一切符合您的满意，点击绿色的`SEND ... BTC`按钮。

![samourai](assets/notext/44.webp)

Samourai随后将进行签名您的交易，然后在网络上广播。您只需等待直到它被矿工添加到一个区块中。

![samourai](assets/notext/45.webp)

### 使用SCODE
有时，Samourai Wallet团队会提供“SCODEs”。SCODE是一个促销代码，它为池子的服务费提供折扣。Samourai Wallet偶尔会在特殊事件期间向其用户提供此类代码。我建议您[关注Samourai Wallet](https://twitter.com/SamouraiWallet)的社交媒体，以免错过未来的SCODES。

要在Samourai上应用SCODE，在开始新的coinjoin周期之前，转到Whirlpool菜单并选择位于屏幕右上角的三个小点。

![samourai](assets/notext/46.webp)

点击`SCODE (促销代码) Whirlpool`。

![samourai](assets/notext/47.webp)

在打开的窗口中输入SCODE，然后点击`OK`进行验证。

![samourai](assets/notext/48.webp)

Whirlpool将自动关闭。等待Samourai完成加载，然后再次打开Whirlpool菜单。

![samourai](assets/notext/49.webp)

通过再次点击三个小点，然后选择`SCODE (促销代码) Whirlpool`来确保您的SCODE已正确注册。如果一切正常，您就可以开始一个新的Whirlpool周期，并在服务费上享受折扣。需要注意的是，这些SCODE是临时的：它们在几天后就会失效。

## 如何知道我们的coinjoin周期的质量？
为了使coinjoin真正有效，它必须在输入和输出的金额之间展示良好的一致性。这种一致性增加了外部观察者可能的解释数量，从而增加了围绕交易的不确定性。为了量化coinjoin产生的不确定性，可以通过计算交易的熵来实现。要深入探索这些指标，我推荐您参考教程：[BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy)。Whirlpool模型被认为是为coinjoins带来最多同质性的模型。
接下来，我们将根据一个硬币在其中被隐藏的群组的范围，评估几个coinjoin周期的性能。这些群组的大小定义了所谓的匿名集（anonsets）。有两种类型的匿名集：第一种是针对回顾性分析（从现在到过去）评估获得的隐私；第二种是针对前瞻性分析（从过去到现在）。为了详细解释这两个指标，我邀请您参考教程：[WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)。

## 如何管理postmix？
在执行coinjoin周期后，最佳策略是将您的UTXOs保留在**postmix**账户中，等待将来使用。甚至建议让它们无限期地重新混合，直到您需要花费它们为止。

一些用户可能会考虑将他们混合的比特币转移到由硬件钱包保护的钱包中。这是可能的，但重要的是要严格遵循Samourai Wallet的建议，以免损害获得的保密性。

合并UTXOs是最常犯的错误。为了避免CIOH（*Common-Input-Ownership-Heuristic*），必须避免在同一笔交易中将混合的UTXOs与未混合的UTXOs结合起来。这需要在钱包内仔细管理您的UTXOs，特别是在标记方面。除了coinjoin之外，合并UTXOs通常是一种不良做法，如果没有得到适当管理，往往会导致保密性的损失。
您还应该对混合UTXOs之间的合并保持警惕。如果您的混合UTXOs具有显著的匿名集，适度的合并是可能的，但这将不可避免地降低您的硬币的隐私。确保合并既不太大，也不在重新混合次数不足的情况下进行，因为这会在coinjoin周期前后建立您的UTXOs之间可推断的链接。如果对这些操作有疑问，最佳做法是不要合并postmix UTXOs，并且每次将它们逐一转移到您的硬件钱包，每次生成一个新的空白地址。再次，记得正确标记每个接收到的UTXO。

还建议不要将您的postmix UTXOs转移到使用不常见脚本的钱包。例如，如果您从使用`P2WSH`脚本的多签名钱包进入Whirlpool，您与原本拥有同类型钱包的其他用户混合的机会很小。如果您将您的postmix退出到这同一个多签名钱包，您混合比特币的隐私级别将大大降低。除了脚本之外，还有许多其他钱包指纹可能会欺骗您。

与任何比特币交易一样，也应避免重用接收地址。每一笔新交易都必须在一个新的空白地址上接收。

最简单和最安全的解决方案是让您的混合UTXOs在它们的**postmix**账户中休息，让它们重新混合，并且只在花费时触碰它们。Samourai和Sparrow钱包对所有这些与链分析相关的风险有额外的保护。这些保护帮助您避免犯错。

## 如何管理doxxic change？
接下来，您必须小心管理doxxic change，即无法进入coinjoin池的零钱。这些由于使用Whirlpool而产生的有毒UTXOs，因为它们建立了您与使用coinjoin之间的联系，对您的隐私构成风险。因此，必须谨慎处理它们，尤其是不要将它们与其他UTXOs结合在一起，特别是混合的UTXOs。以下是考虑它们使用的不同策略：
- **在较小的池中混合它们：**如果你的有毒UTXO足够大，可以单独进入一个较小的池子，考虑混合它。这通常是最好的选择。然而，关键是不要合并几个有毒UTXO以进入一个池子，因为这可能会链接你的不同条目。
- **将它们标记为“不可支出”：**另一种方法是停止使用它们，在它们的专用账户中将它们标记为“不可支出”，然后只是持有。这确保了你不会意外地花费它们。如果比特币的价值增加，可能会出现更适合你的有毒UTXO的新池子；
- **进行捐赠：**考虑进行捐赠，即使是微小的捐赠，也可以给在比特币及其相关软件上工作的开发者。你也可以向接受BTC的组织捐赠。如果管理你的有毒UTXO似乎太复杂，你可以通过捐赠来简单地处理它们；
- **购买礼品卡：**像[Bitrefill](https://www.bitrefill.com/)这样的平台允许你用比特币兑换可以在各种商家使用的礼品卡。这可以是一种处理你的有毒UTXO而不失去相关价值的方式；
- **在门罗币上整合它们：**Samourai Wallet现在提供BTC和XMR之间的原子交换服务。这是通过在门罗币上整合它们来管理有毒UTXO的理想方式，通过KYC保护你的隐私，然后再将它们发送回比特币。然而，这个选项在挖矿费用和由于流动性限制而产生的溢价方面可能成本较高；
- **将它们发送到闪电网络：**将这些UTXO转移到闪电网络以受益于降低的交易费用是一个可能有趣的选项。然而，这种方法可能会根据你使用闪电网络的方式揭露某些信息，因此应谨慎实践。

关于实施这些不同技术的详细教程将很快在PlanB Network上提供。

**额外资源：**
- [Samourai Wallet视频教程](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956);
- [Samourai Wallet文档 - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [关于coinjoins的Twitter线索](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [关于coinjoins的博客文章](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).