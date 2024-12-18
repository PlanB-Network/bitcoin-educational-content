---
name: Sentinel Watch-Only
description: 什么是仅观察钱包以及如何使用它？
---
![cover](assets/cover.webp)

---

***警告：** 继Samourai Wallet的创始人于4月24日被逮捕且其服务器被查封后，Sentinel应用仍然可以使用，但**必须使用您自己的Dojo**才能访问区块链信息和广播交易。*

_我们正在密切关注此案件的发展以及与之相关工具的发展情况。请放心，一旦有新信息可用，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守他们所在司法管辖区的法律。_

---

*"保持你的私钥私密。"*

在本文中，我们探讨了关于仅观察钱包的所有需要知道的信息。我们讨论了它们是如何工作的，并检查了市场上可用的不同应用程序。最后，我们提供了关于最受欢迎的仅观察钱包应用之一：Sentinel的详细教程。

## 什么是仅观察钱包？
仅观察钱包，或只读钱包，是一种软件设计，允许用户观察与一个或多个特定比特币公钥相关的交易，而无需访问相应的私钥。

这种类型的应用程序仅保留监控比特币钱包所需的数据，包括查看其余额和交易历史，但它无法访问私钥。因此，使用仅观察应用程序中的钱包是不可能花费钱包中的比特币的。
![watch-only](assets/en/1.webp)
仅观察通常与硬件钱包结合使用。这允许将钱包的私钥“冷存储”，在未连接互联网的设备上，这具有最小的攻击面，将私钥与可能脆弱的环境隔离。另一方面，仅观察应用程序专门存储比特币钱包的扩展公钥（`xpub`、`zpub`等）。这个父密钥不允许发现关联的私钥，因此，不允许花费比特币。然而，它允许派生子公钥和接收地址。通过了解由硬件钱包保护的钱包的地址，仅观察应用程序可以在比特币网络上跟踪这些交易，为用户提供监控余额和生成新接收地址的能力，而无需每次都连接他们的硬件钱包。

## 应该使用哪个仅观察钱包？
目前，最全面的仅观察应用程序是[Sentinel](https://sentinel.watch/)，由Samourai Wallet的团队开发。它包含了一个好的仅观察钱包所需的所有基本功能：
- 支持扩展密钥、公钥和地址；
- 能够将多个账户或钱包组织成集合；
- 在不直接使用硬件钱包的情况下生成接收比特币的地址；
- 能够离线构建和广播交易；
- 选项连接到自己的比特币节点；
- 集成Tor以增强隐私。
Sentinel的独特缺点在于该应用程序仅适用于Android，且不支持多签名钱包。因此，如果您拥有Android设备且您的钱包是经典的单签名，我推荐使用Sentinel。
对于希望跟踪多签名钱包的用户，Blue Wallet是我所知的唯一一个为这类钱包提供仅观察模式的应用程序，且它可以在Android和iOS上使用。
对于寻找Sentinel替代品的iOS用户，[Green Wallet](https://blockstream.com/green/) 或 [Blue Wallet](https://bluewallet.io/watch-only/) 可能是可选项，尽管它们的仅观察功能不如Sentinel的全面。![watch-only](assets/notext/2.webp)
## 如何使用Sentinel仅观察钱包？
### 安装和设置
首先安装Sentinel应用程序。您可以通过Google Play商店或使用[官方网站上可下载的APK](https://sentinel.watch/download/)来完成此操作。

![watch-only](assets/notext/3.webp)

首次打开应用程序时，您可以选择：
- `连接到Dojo`；
- `连接到Samourai的服务器`。

Dojo由Samourai团队开发，是一个完整的比特币节点版本，可以独立安装，或一键添加到诸如[Umbrel](https://umbrel.com/) 和 [RoninDojo](https://ronindojo.io/)等节点盒解决方案中。

[**-> 了解如何在树莓派上安装RoninDojo v2。**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

如果您有自己的Dojo，您可以在此阶段连接它。通过这样做，当检查您的比特币网络交易信息时，您将受益于最高级别的隐私保护。

![watch-only](assets/notext/4.webp)

否则，可以选择使用Samourai的默认服务器。您还可以选择是否通过Tor连接。

![watch-only](assets/notext/5.webp)

然后，您将进入Sentinel的主页面。

![watch-only](assets/notext/6.webp)

为了开始，您可以设置应用程序。点击右上角的三个小点，然后点击`设置`。

![watch-only](assets/notext/7.webp)
通过选择`用户PIN码`，您可以设置密码以保护对仅观察钱包的访问。您还可以更改参考货币，以将您的余额转换为法定货币，甚至通过激活`隐藏法定货币值`选项来隐藏法定货币值。为了增加安全性，您可以激活`禁用截图`，这样可以防止对您的Sentinel应用程序进行任何截图，从而避免在外部屏幕上泄露任何信息。
![watch-only](assets/notext/8.webp)

在这个设置菜单中，您还可以备份您的Sentinel。

### 使用仅观察钱包
从主页，按蓝色的`新建`按钮添加一个新的扩展公钥以进行跟踪。然后，您可以选择扫描您的密钥的二维码，或通过选择`粘贴公钥`直接粘贴密钥（`xpub`、`zpub`...）。

![watch-only](assets/notext/9.webp)

通常，您的钱包的`xpub`可以通过您使用的钱包管理软件直接访问。例如，如果您使用Sparrow管理您的硬件钱包，此信息位于`设置`标签下的`密钥库`部分。

![watch-only](assets/notext/10.webp)
在Sentinel中输入扩展公钥后，应用程序会提供创建新集合的选项。集合代表一组组织在一起的扩展公钥。这个选项不仅允许你列出所有的`xpubs`，还可以有序地对它们进行分类。例如，如果你有一个Samourai Wallet，里面有多个账户（存款、预混、后混等），你可以将所有这些账户归入`Samourai`集合下。对于为你的家人管理的钱包，你可能会创建一个名为`Family`的集合。

选择`Create new collection`。然后为你刚刚集成的扩展密钥输入一个名称。例如，如果我扫描了我的Samourai钱包的存款账户，我会将这个密钥命名为`Deposit`。点击`SAVE`以完成。

![watch-only](assets/notext/11.webp)

接下来，为这个集合命名，并按屏幕右上角的验证图标以保存集合。你的集合现在在Sentinel首页上可见。

![watch-only](assets/notext/12.webp)

如果你希望添加另一个扩展公钥，再次点击`NEW`并输入你的密钥。

![watch-only](assets/notext/13.webp)
然后，系统会提示你选择希望将此密钥集成到的集合，或创建一个新集合。例如，在我的情况下，我专门为我的Ledger钱包设置了一个集合。
![watch-only](assets/notext/14.webp)

要详细查看集合中的扩展密钥，只需点击它。然后你可以通过不同的标签页浏览交易历史。

![watch-only](assets/notext/15.webp)

从一个集合中，通过点击右上角的三个小点，然后点击`View Unspent Outputs`，你可以访问被跟踪钱包持有的UTXOs列表。

![watch-only](assets/notext/16.webp)

### 通过Sentinel发送和接收比特币
作为任何好的仅观察钱包，Sentinel允许你生成接收地址以在被跟踪的钱包上接收比特币。但Sentinel还提供了另一个高级功能：创建和广播部分签名的比特币交易（PSBT）。因此，持有私钥的钱包可以签署这笔交易，一旦签署，就可以通过Sentinel在比特币网络上广播。让我们看看如何做到这一切。

**注意，不推荐在未经钱包本身验证的接收地址上接收比特币。**如果持有私钥的钱包，如硬件钱包，没有明确确认某个地址与其关联，那么向这个地址发送比特币是一种风险做法。事实上，没有这种确认，就没有保证该地址真的属于你的钱包。因此，仅观察钱包的接收功能应谨慎使用，牢记发送的资金可能会丢失。

通过Sentinel接收比特币，选择感兴趣的集合，然后点击对应于你希望转移资金的扩展公钥的标签页。

![watch-only](assets/notext/17.webp)

最后，点击屏幕左下角的箭头图标。Sentinel为你生成一个空白的接收地址。你可以复制它，或使用QR码扫描它。

![watch-only](assets/notext/18.webp)
要从Sentinel生成PSBT并因此启动支出交易，请转到您希望进行支付的钱包的扩展密钥。以我的Samourai钱包的存款账户为例。然后点击屏幕右下角的箭头图标。
![watch-only](assets/notext/19.webp)

输入与您的交易相关的所有参数：
- 输入收款人地址（点击二维码图标，您可以扫描此地址）；
- 指定发送到此地址的金额；
- 确定交易费用。

填写交易所需的所有字段后，按下`COMPOSE UNSIGNED TRANSACTION`按钮。

![watch-only](assets/notext/20.webp)

然后，您将访问PSBT，它代表一个构建但未签名的比特币交易，因为Sentinel无法访问您的私钥。您可以选择复制此交易，将其导出为`.psbt`文件，或通过动画二维码扫描它。

![watch-only](assets/notext/21.webp)

接着，前往拥有私钥的钱包（Samourai、硬件钱包等）签名交易。

![watch-only](assets/notext/22.webp)

交易签名后，您可以返回到Sentinel广播它。为此，从主菜单点击右上角的三个小点，然后点击`Broadcast transaction`。

![watch-only](assets/notext/23.webp)

您有三种方式输入您的已签名PSBT：
- 直接从剪贴板粘贴；
- 从`.psbt`文件导入；
- 通过二维码扫描。

![watch-only](assets/notext/24.webp)

在灰色框架中输入已签名交易后，您可以点击绿色的`BROADCAST TRANSACTION`按钮，在比特币网络上广播它。Sentinel将给您提供其TXID。

![watch-only](assets/notext/25.webp)

