---
name: Misty Breez
description: 无节点的闪电网络钱包。
---

![misty-breez-cover](assets/cover.webp)

Misty Breez 是一款由 Breez 基于其软件开发工具包 (SDK) 和 BlockStream 开发的 Liquid 网络开发的闪电自持钱包。

它采用了一种全新的无需闪电节点即可运行的方式：这有可能彻底改变比特币网络间的转账方式。

在本教程中，我们将介绍这款钱包的工作原理，并为您提供全面的概述。

## Misty Breez 如何工作？

Misty Breez 的后端无需闪电节点。它基于 Breez SDK 和 Liquid 开发。

Liquid 是比特币网络的并行层，显著提升了速度并降低了交易成本。该并行层使 Misty Breez 无需闪电节点，而是使用 Boltz 等第三方交易服务来确保 Liquid 网络和闪电网络之间的互操作性。别着急，我们稍后会详细介绍。

现在，让我们开始 Misty Breez 钱包的探索之旅吧。

## Misty Breez 入门指南

Misty Breez 移动应用可在官方下载平台下载，例如 Google Play 商店（Android 系统）和 Apple Store（iOS 系统）。您也可以通过 [Misty Breez 官方网站](https://breez.technology/misty/) 下载。

⚠️ 请勿将 Misty Breez 与 Breez 钱包混淆。

⚠️ **重要提示**：为了保障您的比特币安全，请务必从官方平台下载应用，以确保其真实性。

![download-misty-breez](assets/fr/01.webp)

本教程将以安卓设备为例进行讲解。不过，本节中介绍的每个步骤和具体功能也适用于 iOS 系统。

安装 Misty Breez 后，您可以选择创建新钱包或恢复您拥有恢复助记词的旧闪电钱包。

在本教程中，我们将创建一个新钱包。

⚠️ Misty Breez 目前仍处于开发阶段，因此我们建议您从合理的金额开始。

![create-wallet](assets/fr/02.webp)

### 保存您的助记词：

创建新钱包后，您应该做的第一件事就是备份您的 12 个助记词。

以下是一些关于如何备份助记词的提示。

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

要备份您的助记词，请选择 **Preferences > Security** 选单，然后选择 **Check your Backup Phrase** 选项。

![backup](assets/fr/03.webp)

为了增强安全性，您还可以 **create a PIN code** 来验证您对钱包的访问权限。

在 Misty Breez 接受的多种货币中查找您的本地货币。从 **Preferences > Fiat Currencies** 选单配置您的货币，然后选择您需要的货币。

![devises](assets/fr/04.webp)

### 进行您的首次交易

如果您已经熟悉 Breez 钱包，那么 Misty Breez 直观的界面对您来说将非常容易上手。

在界面 **Balance** 选单中，点击 **Receive** 选项，创建发票以接收您钱包中的比特币。

⚠️ Misty Breez 会要求您在手机设置中启用应用程序通知，以便您获得闪电网络地址。

使用 Misty Breez，您可以：

- 在闪电网络上接收 100 聪至 25,000,000 聪的比特币。
- 在比特币主网络上接收 25,000 聪起的比特币。

![transactions](assets/fr/05.webp)

这就是 Misty Breez 的神奇之处。

与 Breez 钱包不同，Breez 钱包会为您提供闪电网络节点，并要求您自行承担开通和关闭支付通道的费用，而 Misty Breez 则不会要求您做任何事情。如前所述，Misty Breez 甚至不依赖于闪电网络节点运行。

让我们深入了解一下它的工作原理。

实际上，您拥有一个与 Misty Breez 钱包关联的 Liquid 钱包。逻辑上讲，您将以固定汇率处理 L-BTC（Liquid Bitcoin），该汇率与第三方比特币转换服务相关联，使您能够与闪电网络进行互操作。

当您在 Misty Breez 钱包收到付款时，您的发送者会向您发送比特币，这些比特币将通过 Boltz（Misty Breez 目前使用的服务）等转换服务转换为 L-BTC，并最终发送到您的 Misty Breez 钱包（关联的 Liquid 钱包）。

以下是幕后流程的简化示意图。

![lnswap-in](assets/fr/06.webp)

点击 “Balance” 选单中的界面，然后点击 “Send” 选项以支付闪电发票。

输入闪电发票、接收者的接收者地址，或者直接扫描发票上的二维码即可完成付款。

![send-bitcoins](assets/fr/07.webp)

在后台，您需要启用与您的 Misty Breez 钱包关联的 Liquid 钱包，通过 Boltz 将等值的 L-BTC 转换为聪（satoshi），然后将这些聪转移到接收者的闪电钱包（在闪电网络上）。

![send-bitcoin-bts](assets/fr/08.webp)

Misty Breez 的这项基础设施功能使用户即使在 Misty Breez 离线时也能进行交易。

对于经验丰富的用户，还有一个 **Preferences > Developers** 选单，其中包含以下详细信息：

- Breez 软件开发工具包的版本。
- 您的 Misty Breez 钱包的公钥。
- 借款人，即从主公钥派生的唯一标识符。
- 您的钱包余额。
- Liquid 小费，用于发送少量 L-BTC。
- Bitcoin 小费，用于发送少量比特币。

您还可以进行某些操作，例如与 Liquid 网络同步、备份密钥、共享活动日志以及选择重新扫描 Liquid 网络。

![dev-mode](assets/fr/09.webp)

恭喜！您现在对 Misty Breez 钱包及其对比特币网络间交易的贡献有了很好的了解。如果您觉得本教程有用，请给我们点个赞。我们非常期待您的反馈。

为了进一步学习，我还建议您了解一下我们关于 Aqua 钱包的教程，它的工作方式与 Misty Breez 类似：

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125
