---
name: Phoenix
description: 安装和使用 Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix 是一款由 ACINQ 开发的自托管闪电钱包和节点。ACINQ 是一家专注于闪电网络软件解决方案的法国公司。与比特币由第三方持有的托管闪电钱包（例如 Wallet of Satoshi）不同，Phoenix 允许用户完全掌控自己的私钥。

Phoenix 作为嵌入手机的真正闪电节点运行，自动与 ACINQ 的闪电节点建立通道。该应用程序基于 Lightning-KMP，这是一个用 Kotlin 编写的跨平台闪电网络实现，并针对移动钱包进行了优化。与其他闪电节点解决方案不同，Phoenix 大大简化了管理。用户无需处理通道的开启和关闭、运行比特币节点或管理 闪电网络上的流动性。Phoenix 会在后台处理所有这些技术操作。

这款应用结合了移动闪电钱包的易用性和便捷性，以及真正个人闪电网络节点的安全性和自主性。Phoenix 让您能够安全、高效、自主地使用闪电网络，同时享受流畅直观的用户体验。

作为回报，需要支付一定的费用：

- 通过闪电网络发送资金需支付金额的 0.4% 加上 4 聪；
- 如果通过闪电网络接收现金，则需支付金额的 1%；
- 开通每个通道需支付 1000 聪。

在我看来，Phoenix 是托管式闪电钱包和手动管理闪电网络节点之间一个绝佳的过渡方案。这款应用同样适合初学者和高级用户，他们无需处理管理自己的 LND 或 Core Lightning 的细节。让我们一起来看看如何使用它吧！

![Image](assets/fr/01.webp)

## 安装应用程序

前往您的应用商店并安装 Phoenix：

- 在 [Google Play 商店](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet)；
- 在 [App Store](https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB) 上。

![Image](assets/fr/02.webp)

您也可以安装应用程序[使用其 GitHub 仓库中的 apk 文件](https://github.com/ACINQ/phoenix/releases)。

![Image](assets/fr/03.webp)

## 创建钱包

应用程序启动后，点击 "*Next*" 按钮跳过演示，然后点击 "*Start*"。

![Image](assets/fr/04.webp)

选择 "*Create a new wallet*"。

![Image](assets/fr/05.webp)

这样就完成了，您的闪电网络钱包和节点已创建完毕。

![Image](assets/fr/06.webp)

## 保存助记词

开始之前，我们需要保存您的 12 个单词的助记词。此助记词可让您完全无限制地访问您的所有比特币。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的手机。

如果您的手机丢失、被盗或损坏，这 12 个单词的助记词可以恢复您对比特币的访问权限。因此，妥善保存并将其存放在安全的地方至关重要。

您可以将其写在纸上，或者为了更加安全，可以将其刻在不锈钢上，以防止火灾、洪水或碰撞损坏。助记词的存储介质选择取决于您的安全策略，但如果您使用 Phoenix 作为日常钱包，且存储金额适中，纸张就足够了。

如需了解更多关于如何正确保存和管理助记词的信息，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

点击界面顶部显示的信息 "*Save your wallet...*"。

![Image](assets/fr/07.webp)

然后点击 "*Save my wallet*"。

![Image](assets/fr/08.webp)

然后点击 "*View my key*"，将您的助记词保存在实体介质上。

![Image](assets/fr/09.webp)

勾选界面底部的两个复选框，确认备份已成功完成。

![Image](assets/fr/10.webp)

## 应用程序设置

在进行首次交易之前，您可以点击界面左下方的齿轮图标来自定义设置。

![Image](assets/fr/11.webp)

在 "*Display*" 选单中，您可以选择应用程序主题、比特币面值和本地法定货币。

![Image](assets/fr/12.webp)

在 "*Payment options*" 中，您可以找到闪电支付的各种高级设置。您可以保留默认设置。

![Image](assets/fr/13.webp)

在 "*Channel management*"中，设置开通 "闪电" 通道时准备支付的最高费用。

![Image](assets/fr/14.webp)

在 "*Access control*" 选单中，我强烈建议您激活一个身份验证系统，以确保您手机上应用程序的访问安全。这将防止任何可以访问您未上锁手机的人访问 Phoenix 并盗取您的比特币。

![Image](assets/fr/15.webp)

在 "*Electrum server*" 选单中，如果您有一个 Electrs 服务器，您可以连接它来广播您的交易。

![Image](assets/fr/16.webp)

为提高连接的保密性，请在 "*Tor*" 选单中启用通过 Tor 进行连接。虽然使用 Tor 可能会略微减慢您的支付速度，并且在接收时需要在前台打开 Phoenix 应用程序，但它能显著提高您的隐私保护。

![Image](assets/fr/17.webp)

## 通过链上接收比特币

首次使用时，您可以选择将链上资金存入凤凰钱包。您也可以直接从 "闪电"（Lightning）进行首次存款（见下一节），但无论哪种情况，开通第一个通道都需要支付额外费用。

点击 "*Receive*" 按钮。

![Image](assets/fr/18.webp)

向左滑动二维码以显示一个比特币接收地址。将您希望存入 Phoenix 的金额发送到该地址。

![Image](assets/fr/19.webp)

在链上收到的金额将首先显示为您的钱包余额下的待定金额。资金需要经过 3 次确认后才能使用。

![Image](assets/fr/20.webp)

收到资金后，Phoenix 会自动为您打开一个闪电通道。现在，您可以通过闪电网络发送和接收比特币了。

![Image](assets/fr/21.webp)

## 通过闪电网络接收比特币

为了通过闪电网络接收卫星，请点击 "*Receive*"按钮。

![Image](assets/fr/22.webp)

Phoenix 会生成一张闪电发票。您既可以扫描它，也可以将它发送给希望向您转送比特币的人。

![Image](assets/fr/23.webp)

点击 "*Edit*" 按钮，您可以在发票上添加接收者可以看到的说明，并定义发送者必须发送的具体金额。

![Image](assets/fr/24.webp)

上面提到的传统发票只能使用一次。若需要一种可重复使用的收款方式，可以使用您的可重复使用二维码，它实际上是一个 BOLT12 报价

![Image](assets/fr/25.webp)

一旦发票或 BOLT12 报价被支付完成，相应的交易就会出现在您的闪电钱包中。

![Image](assets/fr/26.webp)

## 通过闪电网络发送比特币

现在您已经坐在 Phoenix 上，您就可以通过闪电网络进行付款了。首先单击 “*Send*” 按钮。

![Image](assets/fr/27.webp)

有多种选项可供您选择。通过点击 “*Scan QR code*”，您可以扫描闪电发票、BOLT12 报价，甚至是链上支付的接收地址。

![Image](assets/fr/28.webp)

您也可以通过键盘在界面顶部的字段中手动输入这些信息，或输入闪电地址（BOLT12 或 LNURL）。也可以使用 "*Paste*" 按钮直接粘贴信息。

![Image](assets/fr/29.webp)

在这个例子中，我扫描了一张 10,000 聪的发票。为了付款，只需点击 "*Pay*"。

![Image](assets/fr/30.webp)

交易已完成。

![Image](assets/fr/31.webp)

恭喜，您现在知道如何配置和使用 Phoenix。如果您发现本教程有用，请在下面给我点赞，我将不胜感激。请随意在您的社交网络上分享这篇文章。感谢分享！

如果想要更进一步学习，请查看 Alby Hub 上的本教程，这是另一个用于启动您自己的闪电节点的创新且易于使用的解决方案：

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

为了了解有关闪电网络技术操作的更多信息，您可以在 Plan ₿ Academy 上找到 Fanis Michalakis 的精彩免费培训：

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
