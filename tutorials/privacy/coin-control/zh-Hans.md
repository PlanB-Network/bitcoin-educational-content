---
name: Coin Control
description: 了解 Coin Control，这是保护您在比特币上隐私的关键工具
---
![cover](assets/cover.webp)


*本教程引自 [Officine Bitcoin 的一节课程](https://officinebitcoin.it/lezioni/coinco/)。*



## 导言



比特币协议的稳固性由简单的核心概念保证。其中，透明性尤为突出：所有比特币交易都是公开的，并且任何人都可以轻松验证。尽管这一特性是协议的基石，因为它能防止欺诈并保证资金的真实性，但它也可能对保密性构成挑战。**你是否想过，如此的透明性会不会损害你的隐私？**



您应该这样做。虽然积累 Satoshi 非 kyc 非常容易，但在消费阶段，您的隐私最容易受到威胁。



### 花费 UTXO 会发生什么



消费 Bitcoin 并不是简单地将价值转移给他人。



通过使用您的 UTXOs，您必须满足协议透明度规定的条件，因为您有义务证明您拥有这些资金。因此，您必须对.NET 的使用负责：




- 暴露你的公开密钥；
- 生成数字签名。



因此，消费的时间最为关键： **消费 Bitcoin 是一种有意识的行为，要尽可能地加以控制**。



## Coin 控制



在 Bitcoin 协议中，不存在 _account_ 或 _monetary units_ 等项目。我强烈推荐的以下课程对 UTXO 的概念做了很好的解释：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

在 Bitcoin 中，您积累并随后花费的是以 Satoshi 计量的小型或大型账户单位，由 "未用交易输出"（**UTXO**，也称为 "币"）表示。在使用UTXOs创建交易时，它们会被完全销毁，并在其位置上创建其他UTXOs。



软件钱包的开发就是为了采用协议提供的特定算法，使用 "随机 "选择的硬币自动做出这种选择。这些算法要满足的唯一标准是支付消费所需的金额。



它们可能会将不同年龄的UTXO混合在一起，或偏向于使用最新或 "最老 "的UTXO，这取决于开发人员选择的算法。最好的软件钱包还计划给用户留下一个重要的选择。



Coin控制 "手册也被称为 "Coin选择"，它是某些软件钱包的一项功能，允许您在建立交易时**手动选择要花费的UTXO。



假设我们有一个 Wallet，3 个UTXO 分别为 21,000、42,000 和 63,000 Satoshi。



![img](assets/en/01.webp)



如果必须花费 2.4 万 Sats，并让算法进行自动选择，那么优秀的 Software Wallet 可能会选择将 UTXO 1 + UTXO 2 组合起来，以支付 2.4 万 Sats 和 Miner 的费用，产生的剩余部分会回到起始 Wallet 的内部 Address。



![img](assets/en/02.webp)



交易完成后，Wallet 的新情况（仅计算 UTXOs）可概括如下。



![img](assets/en/03.webp)



但是，如果有正确的软件和您的意识，您本可以做出不同的、在某些方面更为正确的选择。例如，只选择UTXO2（42,000 Sats）。



![img](assets/en/04.webp)



在你的 Wallet 结束时，在 UTXO 的水平上，这看起来与之前不同。



![img](assets/en/05.webp)



## 为什么要手动 coin control？



![img](assets/en/06.webp)



在上述两个例子中，余额实际上是相同的 `108,280 Sats`。在花费 24,000 Sats 之后，如果没有手动选择，我们在 Wallet 中会有 2 个 UTXO；如果手动控制 Coin，我们总共会有 3 个 UTXO。



我们可能会问自己的问题是：**为什么要做这一切？** 有，或者可能有，几个原因导致我们没有使用 `UTXO1`，**而这些原因正是为什么——在支出阶段——启用手动币控制是应遵循的良好实践之一的根本原因**。



选择UTXO 可以让您在某些方面优于其他方面。如何选择取决于您想要实现的目标。



### 隐私权



手动控制 Coin 的主要优点之一是**了花费者的隐私。让我们始终以我们的例子为例：在没有手动选择 Coin 的情况下，支出 24,000 Satoshi。由于 Bitcoin 的 Blockchain 是公开记录，外部观察者可以毫无疑问地宣布，21,000 Sats 的输入 `UTXO1` 和 42,000 Sats 的输入 `UTXO2` 以及其余的 38,280 Sats 的输入 `UTXO5` **三者属于同一用户**。



另一方面，通过手动选择 `UTXO2`，`UTXO1` 仍然完全保留，在 UTXO 中等待更合适的时间使用。



UTXO1 "可能来自一个 KYC 来源，例如在 Exchange 收到的货物和服务付款，而其他 UTXO 则不是。将 UTXO-kyc 与其他保密性更强的资金混合，会损害非kyc 资金的匿名性。



**KYC资金将不可避免地追溯到付款人的身份。如果这是你的钱包，你会希望外部观察者能够以如此绝对的确定性追溯到你的身份吗？**



例如，可以手动选择UTXO 的钱包允许**隔离一个或多个UTXO**，这是在出现这种情况时可以使用的功能。



虽然我确信 KYC 资金应存放在独立的 Wallet 中，而不是在没有 KYC 的情况下购买的 Bitcoin，但如果您的情况是这样的话，对您的一些地址进行隔离是一个关键的帮助，您可以通过学习手动选择消费输入来加以利用。



### 节省费用



选择正确的 UTXO 进行支出，**可以优化费用**。还是从我们最初的例子开始，Software Wallet 选择了两个 UTXO 来支付费用。两个 UTXO 意味着要向网络显示两个签名。因此，就 vBytes 而言，交易的 "权重 "更大。



另一方面，使用 Coin 手动控制功能，您可以只选择一个足以支付金额的选项，通过降低交易 "权重 "来节省费用。



在收费很高，但你又不得不花费 Bitcoin On-Chain 的时候（例如，开通 Lightning Network 频道），这时 Coin 控制权就变成了正确的经济激励手段。



### 遗体汇总



当您付款并使用 Bitcoin On-Chain 时，收到零钱的可能性几乎总是必然的。每次余款本身就是一次小小的隐私损失，因为它向网络（尤其是收款人）透露了您的 Address 并与您的源输入相关联。



考虑到最好的 Wallet HD 具有 generate 特殊地址，您可以很容易地识别它们，并 "隔离 "各种交易的所有残余；当它们达到一定数量时，您可以手动选择并合并它们，或交换到 Lightning Network（我的首选方法）并处理它们，以便重新获得在消费中失去的隐私。



### 来自 Cold Wallet 的支出



Cold Wallet 是一种可以合理获得较高安全性的工具，可以存储任何金额的资金，以便长期保存。然而，不可预见的事件可能会发生，因此，需要动用储蓄来应付一些意外支出。



我不知道有多少人能分享我的方法，但我的建议是**永远不要直接从 Cold Wallet 中支出，以避免收到相同地址之间的变动**。学会手动选择支付费用所需的UTXO，将其转入Wallet Hot，然后从后者准备交易。然后，如有任何零钱，您可以将其送回 Cold Wallet Address（如果金额足够），将其用于其他支出，或仍然像我们刚才看到的那样将其隔离。



## 实际演示


在 "为什么 "的技术介绍之后，让我们看看如何使用不同的桌面和移动软件来实践 Coin 手动控制。我们将始终使用相同的 Wallet BIP39，并将其导入所选的每种工具，以便向您展示它们之间的细微差别。



## Wallet 台式机



### Sparrow



如果您使用 Sparrow，请打开 Wallet，从左侧菜单中选择 _UTXOs_。您将看到与 Wallet 相关联的所有 UTXO 列表。



只需用鼠标点击其中一个，然后选择_发送所选_即可。Sparrow 还会在命令旁边显示选中后的可用支出总额。在图形上，Sparrow 会用蓝色高亮显示所选的 UTXO。



![img](assets/en/07.webp)



您也可以选择多个。请使用 _CTRL_ 键在列表中选择不相邻的 UTXO。



![img](assets/en/08.webp)



手动选择 UTXO 后，您就可以开始建立交易，Sparrow 将以图形方式向您展示交易的构成。



![img](assets/en/09.webp)



#### 隔离 UTXO



隔离资金是指将资金 "锁定 "在 Wallet 中，使其不能作为交易输入。Sparrow 允许使用此功能，可通过 _UTXOs_ 菜单访问：将鼠标放在要 "锁定 "的 UTXO 上，然后单击鼠标右键。在该程序的功能中，将出现 _Freeze UTXO_（冻结 UTXO）。这样，您就可以用 Sparrow 钱包隔离金币了。



![img](assets/en/29.webp)



### 电石



如果您的 Wallet 桌面是 Electrum，您应该知道可以从_地址_菜单或_硬币_菜单中手动选择UTXO。在这两个菜单中，选择方法都是将鼠标指向所需的 UTXO，右击后选择_添加到 Coin 控件_。



![img](assets/en/10.webp)



即使使用该软件，您也可以选择多个 UTXO，如果它们不相邻，可以使用键盘上的 _CTRL_ 键来帮助选择。



![img](assets/en/11.webp)



从图形上看，Electrum 将通过高亮显示 Green 中所选的 UTXO 来向您显示选择情况，同时底部会出现一个以相同颜色高亮显示的条形图，显示 Coin 控制后的可用余额。



![img](assets/en/12.webp)



选择输出后，您就可以像往常一样通过_发送_菜单建立交易。



#### 隔离 UTXO



Electrum 通过_Coins_菜单提供了这一功能，您可以在该菜单中选择特定的 UTXO，然后点击右键选择_Freeze_。即使没有资金，您也可以从_地址_菜单中 "冻结 "Address，或 "冻结 "Coin，使其不被使用。



![img](assets/en/28.webp)



### 双节棍



打开 Nunchuk 后，您可以从主菜单中选择UTXO。启动 Nunchuk 并单击 _View coins_（查看硬币）。



![img](assets/en/13.webp)



这将打开包含 Wallet 中所有UTXOs 的窗口，您可以通过激活每个金额旁边的复选标记来选择一个或多个UTXOs。选择后，继续_创建交易_。



![img](assets/en/14.webp)



然后，您可以输入目的地 Address，并设置金额和费用。



![img](assets/en/15.webp)



#### 隔离 UTXO



为完整起见，Nunchuk 还允许隔离一个（或多个）UTXO，并有两种不同的方法。进入_View coins_（查看硬币）菜单，从硬币列表中手动选择。然后点击右下角的_More_（更多）菜单：会出现一个选项列表，您可以从中选择_Lock coins_（锁定硬币）。



![img](assets/en/39.webp)



![img](assets/en/40.webp)



您也可以点击为 UTXO 预留的空间，进入_硬币详情_窗口。右上角会显示锁定/解锁 UTXO 的命令。



![img](assets/en/41.webp)



### Blockstream 应用程序



Blockstream App 桌面（以前称为 Green）允许您在开始构建交易时选择 Coin。因此，请打开 Wallet 并点击_发送_。



![img](assets/en/16.webp)



将目标 Address 粘贴到相应字段，然后选择_手动 Coin 选择_。



![img](assets/en/17.webp)



在打开的窗口中，您可以选择一个或多个 UTXO 硬币。在下面的示例中，我们选择了两枚硬币。然后，点击_确认 Coin 选择_来确认您的选择。



![img](assets/en/18.webp)



设置金额和费用，然后正常进行交易。



![img](assets/en/19.webp)



⚠️ 注：在 Green 的_Coins_菜单中，有_Lock_/_Unlock_项，预示着有可能隔离 UTXO。该功能仅在所谓的 Multisig 账户中激活；也仅在选择金额极小的 UTXO 时激活，接近 "Dust "的临界值。



## Wallet 移动电话



也可以从手机中选择钱包，这样就可以手动选择UTXO。第一个例子是蓝色 Wallet。



### 蓝色 Wallet



如果您是 Wallet 的用户，请打开 Wallet 并点击进入与您的一个钱包相关的控制界面。要进入 Coin 控制手册，您必须进入消费阶段，然后点击_发送_。



![img](assets/en/21.webp)



在下一个屏幕中，选择右上角三个点所指示的菜单。打开一个下拉窗口，其中包含一系列命令。选择最后一个：硬币控制



![img](assets/en/22.webp)



此时，蓝色 Wallet 将显示您的所有 UTXO。除了数量外，它们还以不同的颜色显示出来。



![img](assets/en/27.webp)



选择 UTXO，然后选择_Use Coin_。



![img](assets/en/23.webp)



蓝色 Wallet 会带您回到_Send_（发送）窗口，继续建立交易。调整金额和费用，然后选择_Next_（下一步）。



![img](assets/en/24.webp)



此时，您可以像往常一样结束交易。



#### 隔离 UTXO



Blue Wallet 还可以隔离UTXO，使其无法用于消费，这对于移动设备上的 Wallet 来说是个不错的功能。您可以按照刚才介绍的步骤访问 Coin 控制面板，选择 UTXO 后，选择_Freeze_（冻结）而不是_Use Coin_（使用硬币）。



![img](assets/en/26.webp)



### 双节棍



手机版 Nunchuk 还能让用户进行 Coin 控制。如果您在手机上使用该应用程序，请打开它并进入_钱包_菜单。从那里选择_View coins_（查看硬币）。



![img](assets/en/30.webp)



在显示UTXO 列表的窗口中，单击_Select_（选择）。



![img](assets/en/38.webp)



每个 UTXO 旁边都有一个选择功能。与桌面版一样，Nunchuk Mobile 上的手动选择也是通过勾选金额旁边的小方块来完成的。屏幕会显示所选的UTXO数量和可用的总金额。完成后，点击左下角的₿符号，这是开始建立交易的命令。



![img](assets/en/31.webp)



现在您可以完成交易，选择金额并点击_Continue_（继续）。



![img](assets/en/32.webp)



继续像往常一样，粘贴目的地 Address、描述和自定义费用设置。



#### 分离 UTXO



您还可以使用移动双节棍隔离UTXO。进入专用硬币列表窗口，选择要隔离的 UTXO 旁边的箭头。



![img](assets/en/42.webp)



您将看到_硬币详细信息_预留空间，在此您可以选择_锁定此硬币_。



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper 是本指南中最后一个 Wallet。我们将看到它的功能应用于通过 Wallet 单密码控制 Coin，尽管这种用途并不是这个特殊应用程序的目的。在手机上设置好 Keeper 后，启动它并打开一个包含一些资金的 Wallet。在主屏幕中央点击 _View All Coins_（查看所有硬币）。



![img](assets/en/34.webp)



Keeper 会显示UTXO 的概览。要进入选择屏幕，请单击_选择发送_。



![img](assets/en/35.webp)



您可以通过点击相应的命令来勾选硬币。完成后，点击_发送。



![img](assets/en/36.webp)



Bitcoin Keeper 会直接将您带入_发送_菜单，您可以在该菜单中使用选定的 UTXO 建立交易。



![img](assets/en/37.webp)



## Hardware Wallet



本指南中的每个软件钱包都可以是您的一个硬件钱包的专用 Interface。这意味着离线签名设备的 Coin 控制可以通过目前看到的步骤来执行。



### 一般性建议



Coin 控制是选择交易输入的一种非常有效的做法。如果在购买/接收资金时，您能很好地标注 Satoshis 的来源，那么手动选择的效率会更高。如果您想很好地学习这一技巧，我推荐您参考以下教程：



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

我们之前讨论过 "分离残余物"。如果您想锁定残币以便日后处理，并重新获得隐私（在 Layer 2 上交换），您必须注意在每次收到残币时都对其进行 "标记"。在目前看到的软件钱包中，只有 Electrum 对 UTXO 残币进行了图形着色，使其一目了然。其他软件，如 Sparrow，会显示单个 UTXO 的衍生路径链 (`m/84'/0'/0'/1/11`)。



要有效地使用这一技巧，切记一定要在收到的零钱上添加说明：您向其发送资金（付款、教程或其他）的人知道与零钱相关的 Address，并知道它属于您，因为它来自你们一起进行的交易！