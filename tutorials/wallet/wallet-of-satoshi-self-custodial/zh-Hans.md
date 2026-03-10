---
name: Wallet of Satoshi - 自我监护
description: 了解如何配置 Wallet of Satoshi 组合的自托管模式
---

![cover](assets/cover.webp)



***不是你的密钥，就不是你的比特币*"不只是一句俗语，它是 Bitcoin 的基本原则，这意味着如果你不能控制解锁比特币的**私钥，你就不能真正拥有它们。



许多用户一般先使用**托管 wallet**，然后迁移到**自托管 wallet**，由他们自己控制私钥。


在本教程中，我们将不会向您介绍新的自我监护型 wallet。相反，我们将向您介绍 ***Wallet of Satoshi*** wallet 的一项新功能： **自闭模式**。



这一新集成的目的是使用户能够保留对其私人密钥的控制，同时受益于简洁流畅的用户体验。



在进入问题的核心之前，让我们先来看看 Wallet of Satoshi（WoS）提供的特殊自我监护模式。



## 自我监护模式的特点



WoS 自托管模式的简单性和流动性消除了打开闪电通道、管理节点的复杂性......但这怎么可能呢？



Wallet of Satoshi 的自托管模式由**火花**提供支持。这是 Lightspark 利用**状态链**技术为 Bitcoin 开发的 Layer 2 解决方案。



因此，您不能直接在 Lightning Network 上进行交易。**LN**网络和**Spark**之间的互动是通过**原子交换**进行的。



例如，Bob 希望使用 WoS 支付一张闪电发票。他转移他的 satoshi，但在后台，这些 satoshi 被路由到 Spark 上的**Spark 服务提供商（SSP）**，后者反过来在闪电网络上执行支付。



相反，Alice 希望直接从其 WoS 投资组合中获取资金。在这种情况下，**SSP** 通过 LN 接收 sats，并立即记入 Alice 的投资组合。



因此，需要注意的是，要从 WoS 的简单性和流动性中获益，您需要依赖 Spark 的服务器。不过，就安全性而言，如果 SSP 出现恶意或不可用的情况，您可以使用**单边退出**机制，这是一种安全措施，允许您在 Bitcoin on-chain 上收回资金（尽管这可能会很慢，成本很高），从而保证了与私人 "闪电 "节点相媲美的自我监管体验。



考虑到所有这些参数，您就可以决定在 WoS 自我保管中保留多少 sats。



如果您是 Wallet of Satoshi 的新用户，自然需要下载手机 wallet 应用程序。不过，如果您已经在使用 wallet，并想了解如何使用**自我监护模式**，请直接进入本教程的**自我监护模式配置**部分。



## 开始使用 Wallet of Satoshi



前往应用程序商店下载 WoS。



![screen](assets/fr/03.webp)



下载完成后，打开应用程序并按**开始**。



![screen](assets/fr/04.webp)



您将被重定向到应用程序的主界面。事实上，当您首次访问 WoS 时，投资组合已经开始运行，并默认以托管模式打开。



![screen](assets/fr/05.webp)



即使您不想在托管模式下使用 WoS，我们也建议您先进行配置。为此，请参考本教程。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

接下来，让我们来看看自我监护中的 WoS 配置。



## 自我监护模式配置



点击主界面右上角的汉堡包菜单（三条杠图标）。



![screen](assets/fr/06.webp)



然后，在出现的菜单中点击**打开自我监护 Wallet** 子菜单。



![screen](assets/fr/07.webp)



WoS 会立即告诉你，*自我保管模式附带恢复短语。此外，您必须对您的资金安全负全责*。



![screen](assets/fr/08.webp)



勾选 "**我了解**"按钮 (1)，然后按下**打开自我监护 Wallet** 按钮 (2)，按钮显示为亮黄色。



![screen](assets/fr/09.webp)



### 创建自我监护组合



点击**打开自我监护 Wallet** 按钮后，点击**创建新 Wallet** 按钮。



![screen](assets/fr/10.webp)



然后，WoS 将为您创建一个自我监护组合，同样是在同一个应用程序中。您可以在方便的时候随时在**监护**模式（某些地区提供）和**自我监护**模式之间切换。



![screen](assets/fr/11.webp)



创建后，您将跳转到 WoS 自托管主界面。您会发现，WoS 托管投资组合和 WoS 自托管投资组合的总体概览和界面没有任何区别。



### 保存您的记忆短语



点击屏幕顶部位于 Wallet of Satoshi 名称和汉堡包菜单之间的 **Keychain + Backup Wallet** 图标。



![screen](assets/fr/12.webp)



WoS 提供两种不同的方式保存您的 12 个单词（记忆短语）： **通过 Google Drive 备份**和手动备份**。



虽然我们建议使用最安全的手动备份，但我们也会向你展示如何通过 Google Drive 备份。



#### 通过谷歌硬盘备份



单击**谷歌硬盘备份**按钮。



![screen](assets/fr/13.webp)



如果您选择使用 Google Drive 进行备份，您的 Google 账户很有可能会受到威胁。恶意者可以访问包含您的 12 个单词的文件，从而访问您的 wallet。



添加密码对包含 12 个单词的文件进行加密无疑是增加一层安全保障的好方法。



因此，请激活高级选项中的**用密码加密**按钮。



![screen](assets/fr/14.webp)



在出现的新界面上，设置一个强密码，然后再次确认。



![screen](assets/fr/15.webp)



重要的是要记住，一旦选择了密码，就一定不能忘记它或丢失写密码的介质。如果忘记或丢失了密码，您将再也无法使用您的 12 个字，也就无法使用您的资金。



选择密码后，选择一个用于备份的 Google 账户，然后授予 WoS 所需的访问权限。



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



等待几秒钟。中奖了！备份已成功完成。



![screen](assets/fr/18.webp)



您始终可以选择第二种备份方法：手动备份，进行额外备份。


#### 手动备份



如果您选择手动备份，我们强烈建议您参考本教程，其中探讨了安全备份记忆词组的最佳做法，以免丢失比特币的访问权限。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

按下**手动备份**按钮。



![screen](assets/fr/19.webp)



在接下来的界面中，WoS 会提醒您在进行手动备份之前要注意一些安全防范措施。



激活**我明白**按钮，然后按下**下一步**按钮。



![screen](assets/fr/20.webp)



然后，您将看到 12 个单词。保存它们，然后点击**下一步**按钮。



![screen](assets/fr/21.webp)



在这个新界面上，按照正确的顺序按下单词。



![screen](assets/fr/22.webp)



最后，点击**下一步**按钮。恭喜您，备份已完成！备份已完成。



![screen](assets/fr/23.webp)



## 恢复自我保管的投资组合



当您更换手机或因其他原因想要恢复或还原 WoS 自保管 wallet 时，请按照以下步骤操作。



要打开 WoS 投资组合，请单击主界面右上角的汉堡包菜单。


在出现的菜单中，单击**打开自我监护 Wallet** 子菜单。


在出现的新界面上，按下 ** 恢复现有 Wallet** 按钮。



![screen](assets/fr/24.webp)



选择恢复方法，然后进入下一步。



![screen](assets/fr/25.webp)



### 通过 Google Drive 恢复



1.按下 ** 从 Google Drive 还原** 按钮。


2.选择一个 Google 账户，让 WoS 检索保存在 Google Drive 上的恢复数据。


3.然后从包含 12 个单词的文件中输入加密密码（当然，如果您之前已经定义了密码）。


4.稍等片刻，待恢复生效后，您就可以再次访问您的投资组合了。



### 手动修复



1.按下 ** 手动还原** 按钮。


2.然后输入记忆短语的 12 个单词，将每个单词写在起始编号的前面。


3.稍等片刻，待恢复生效后，您就可以再次访问您的投资组合了。




### 在 WoS 托管和 WoS 自托管之间转移比特币



当您在 WoS 托管 wallet 中拥有比特币 (sats) 并创建了 WoS 自托管 wallet 时，您的资金不会丢失。更妙的是，您可以将其转移到自我托管的投资组合中，反之亦然。



为此：


您可以复制闪电 WoS 自助托管地址或您创建的发票。



![screen](assets/fr/26.webp)



现在打开监护 wallet，按下 **Envoyer** 按钮。



然后粘贴地址或发票。再按一次 **Envoyer**。



返回到您的自我托管投资组合，您会看到您确实收到了资金。



![screen](assets/fr/27.webp)



## 发送和接收比特币



至于在自我托管模式下发送和接收比特币，就像一般概述和接口一样，它们与通过 WoS 托管 wallet 发送和接收比特币没有什么不同。



请参阅在 Plan₿ 网络上使用 Wallet of Satoshi 的基本教程。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

现在，您可以在自我监护模式下自行配置和操作 Wallet of Satoshi。



如果您觉得本教程有用，请在下方给我留下绿色拇指。非常感谢！