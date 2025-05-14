---
name: 迷雾微风
description: 无弓闪电 Wallet。
---

![misty-breez-cover](assets/cover.webp)



Misty Breez是Breez公司基于其软件开发工具包和BlockStream公司开发的**Liquid**网络开发的闪电自持Wallet。


它采用了一种全新的方法来实现无 "闪电 "节点的操作：这是 Bitcoin 网络间传输的潜在**游戏改变者**。


在本教程中，我们将介绍这种投资组合的工作原理，并为您提供完整的概述。



## Misty Breez 如何工作？



Misty Breez 是一个不使用 Lightning 节点作为后台的实现。它是在 Breez SDK 和 Liquid 的基础上开发的。



Liquid 是与 Bitcoin 网络并行的 Layer，在速度和交易成本方面有显著改善。这个 Layer 允许 Misty Breez 不再使用 "闪电 "节点，而是使用第三方 Exchange 服务，如**Boltz**，以确保 Liquid Network 和 Lightning Network 之间的互操作性。别急，我们会再来讨论这个问题。



现在，让我们从 Misty Breez Wallet 开始冒险。



## 开始使用 Misty Breez



Misty Breez 移动应用程序可在 Google Play Store（Android）和 Apple Store（iOS）等官方下载平台上下载。您也可以从 [Misty Breez] 官方网站（https://breez.technology/misty/）转到正确的应用程序。



⚠️ 请注意不要将 Misty Breez 与 Breez Wallet 混淆。



⚠️ **重要**：为了您比特币的安全，请务必从官方平台下载应用程序，以确保其真实性。



![download-misty-breez](assets/fr/01.webp)



在本教程中，我们将从 Android 设备开始。不过，本节详述的每个步骤和具体功能都适用于 iOS。



安装后，Misty Breez 会让您选择创建一个新的 Wallet 或恢复一个有恢复字样的旧闪电 Wallet。


在本教程中，我们选择创建一个新的投资组合。



⚠️Misty Breez 目前正处于开发阶段，因此我们建议您从合理的金额开始。



![create-wallet](assets/fr/02.webp)


### 保存您的恢复词 ：


在创建新的作品集时，您首先要做的一件事就是备份您的 12 个恢复词。


下面是一些关于如何备份备份短语的提示。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

要备份短语，请选择**首选项 > 安全**菜单，然后选择**检查您的备份短语**选项。



![backup](assets/fr/03.webp)


为了提高安全性，您还可以**创建一个 PIN 码**，以验证对 Wallet 的访问。




在 Misty Breez 接受的多种货币中找到您的当地货币。在 "**首选项">"法定货币 "**菜单中配置您的货币，然后选择您需要的一种或多种货币。



![devises](assets/fr/04.webp)



### 进行首次交易


如果您已经熟悉 Breez 的产品组合，就不会对 Misty Breez 直观的 Interface 感到陌生。



在 Interface 的 "**余额**"菜单上，点击 "**接收**"选项，创建发票，在 Wallet 上接收比特币。



⚠️ Misty Breez 会要求您在手机设置中激活应用程序的通知，以便您有权获得闪电 Address。



通过 Misty Breez，您可以 ：




- 在 Lightning Network 上接收从**100 萨托希**到**25,000,000 萨托希**的比特币。
- 在 Bitcoin 主网络上接收比特币，**25,000 萨托希**起。



![transactions](assets/fr/05.webp)



这就是 Misty Breez 的神奇之处。


Breez Wallet 为您提供了一个 "闪电 "节点，并要求您自己承担开通和关闭支付通道的费用，而 Misty Breez 则不同，它不要求您做任何事情。如前所述，Misty Breez 甚至不是基于 "闪电 "节点工作的。



让我们走近幕后。



实际上，您拥有一个与 Misty Breez 投资组合相关联的 Liquid 投资组合。从逻辑上讲，您将以与第三方海底卫星转换服务相关的固定费率处理 L-BTC（Liquid Bitcoin），这将使您能够与 Lightning Network 互操作。



当您在 Misty Breez Wallet 上收到付款时，发件人会向您发送 Satoshis，然后通过 Boltz（目前由 Misty Breez 使用）等转换服务将发送的 Satoshis 转换为 L-BTC，并在您的 Misty Breez Wallet 上接收（关联 Liquid Wallet）。


以下是幕后流程的简化示意图。



![lnswap-in](assets/fr/06.webp)



点击**余额**菜单中的 Interface，点击**发送**选项，支付闪电 Invoice。


插入 Lightning Invoice、收件人的 Lightning Address 或扫描 Invoice 上的二维码即可付款。



![send-bitcoins](assets/fr/07.webp)



在幕后，您会启用与您的 Misty Breez Wallet 相关联的 Liquid Wallet，通过 Boltz 将等值的 L-BTC 转换为卫星币，然后将这些卫星币转入收件人的 Lightning Wallet（存在于 Lightning Network 上）。



![send-bitcoin-bts](assets/fr/08.webp)



Misty Breez 基础设施的这一功能使用户即使在 Misty Breez 离线时也能进行交易。



对于更有经验的用户，还可在菜单 ** 参数设置 > 开发人员** 中了解有关 .NET 开发人员的更多详情：




- Breez 软件开发包的版本。
- Misty Breez Wallet 的公开密钥。
- 借款人，从主公钥中提取的唯一标识符。
- 您的投资组合余额。
- 提示 Liquid，用于发送小额 L-BTC。
- Bitcoin 提示器，用于发送少量 Bitcoin。



您还可以执行某些操作，例如与 Liquid Network 同步、备份密钥、共享活动日志以及选择重新扫描 Liquid Network。



![dev-mode](assets/fr/09.webp)


恭喜您！您现在已经对 Misty Breez 组合及其对 Bitcoin 网络间交易的贡献有了很好的了解。如果您觉得本教程有用，请向我们伸出 Green 大拇指。我们很高兴收到您的来信。



如果您想进一步了解，我还建议您查看我们关于 Aqua Wallet 的教程，其工作原理与 Misty Breez 相似：



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125