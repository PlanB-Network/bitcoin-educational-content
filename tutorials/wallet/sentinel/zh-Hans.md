---
name: Sentinel
description: 何为仅观察钱包（watch-only wallet）以及如何使用它？
---
![cover](assets/cover.webp)

---

**警告：** 4月24日，Samourai Wallet 的创始人被捕，其服务器被查封。Sentinel 应用目前仍可运行，但**您必须使用自己的 Dojo 才能访问区块链信息并广播交易。**
---

*"请务必妥善保管您的私钥。"*

本文将探讨您需要了解的关于仅供查看的钱包的一切。我们将讨论其工作原理，并介绍市面上不同的应用。最后，我们将详细介绍最受欢迎的仅供查看钱包应用之一：Sentinel。

## 何为仅观察钱包？

仅观察钱包（watch-only wallet）是一种软件，旨在允许用户查看与一个或多个特定比特币公钥关联的交易，而无需访问相应的私钥。

这类应用程序仅保留监控比特币钱包所需的数据，包括查看其余额和交易历史记录，但无法访问私钥。因此，无法通过只读钱包应用程序花费钱包中的比特币。

![watch-only](assets/en/1.webp)

仅观察通常与硬件钱包结合使用。这允许将钱包的私钥 “冷存储”，在未连接互联网的设备上，这具有最小的攻击面，将私钥与可能脆弱的环境隔离。另一方面，仅观察应用程序专门存储比特币钱包的扩展公钥（`xpub`、`zpub`等）。这个父密钥不允许发现关联的私钥，因此，不允许花费比特币。然而，它允许派生子公钥和接收地址。通过了解由硬件钱包保护的钱包的地址，仅观察应用程序可以在比特币网络上跟踪这些交易，为用户提供监控余额和生成新接收地址的能力，而无需每次都连接他们的硬件钱包。

## 应该使用哪个仅观察钱包？

目前，最完整的仅观察应用是 [Sentinel](https://github.com/wanderingking072/sentinel-android)，最初由 Samourai Wallet 团队开发，如今由社区维护。它汇集了优秀仅观察钱包所需的所有核心功能：
- 支持扩展密钥、公钥和地址；
- 能够将多个账户或钱包组织成集合；
- 无需直接使用硬件钱包即可生成用于接收比特币的地址；
- 支持离线构建和广播交易；
- 可选择连接到自己的比特币节点；
- 集成 Tor 以增强隐私保护。
Sentinel 的独特缺点在于该应用仅适用于 Android 系统，且不支持多重签名钱包。因此，如果您拥有 Android 设备且您的钱包是传统的单签名钱包，我推荐使用 Sentinel。
对于想要追踪多签名钱包的用户，据我所知，Blue Wallet 是唯一一款为这类钱包提供 “仅观察” 模式的应用，并且支持 Android 和 iOS 系统。
对于正在寻找 Sentinel 替代方案的 iOS 用户，[Green Wallet](https://blockstream.com/green/) 或 [Blue Wallet](https://bluewallet.io/watch-only/) 或许是不错的选择，尽管它们的 “仅观察” 功能不如 Sentinel 全面。

![watch-only](assets/notext/2.webp)
## 如何使用 Sentinel 仅观察钱包？
### 安装和设置
首先，安装 Sentinel 应用程序。您可以使用[项目 Github 仓库中提供下载的 APK](https://github.com/wanderingking072/sentinel-android/releases) 来完成此操作。

接下来，您必须强制连接到您自己的 Dojo，因为 Samourai Wallet 的服务器已不再可用。如果您还没有自己的 Dojo，可以使用社区在 [The Dojo Bay](https://dojobay.pw/) 网站上提供的 Dojo，或者按照我们的教程安装您自己的 Dojo :

https://planb.academy/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9

![watch-only](assets/notext/4.webp)

然后，您将进入 Sentinel 的主页面。

![watch-only](assets/notext/6.webp)

为了开始，您可以设置应用程序。点击右上角的三个小点，然后点击 `Settings`。

![watch-only](assets/notext/7.webp)
通过选择 `User PIN code`，您可以设置密码以保护对仅观察钱包的访问。您还可以更改参考货币，以将您的余额转换为法定货币，甚至通过激活 `Hide fiat values` 选项来隐藏法定货币值。为了增加安全性，您可以激活 `Disable Screenshots`，这样可以防止对您的 Sentinel 应用程序进行任何截图，从而避免在外部屏幕上泄露任何信息。
![watch-only](assets/notext/8.webp)

在这个设置选单中，您还可以备份您的 Sentinel。

### 使用仅观察钱包
从主页，按蓝色的 `NEW` 按钮添加一个新的扩展公钥以进行跟踪。然后，您可以选择扫描您的密钥的二维码，或通过选择 `Paste Pubkey` 直接粘贴密钥（`xpub`、`zpub`...）。

![watch-only](assets/notext/9.webp)

通常，您的钱包的 `xpub` 可以通过您使用的钱包管理软件直接访问。例如，如果您使用 Sparrow 管理您的硬件钱包，此信息位于 `Settings` 标签下的 `Keystore` 部分。

![watch-only](assets/notext/10.webp)
在 Sentinel 中输入扩展公钥后，应用程序会提供创建新集合的选项。集合代表一组组织在一起的扩展公钥。这个选项不仅允许您列出所有的 `xpubs`，还可以有序地对它们进行分类。例如，如果您有一个 Samourai Wallet，里面有多个账户（存款、混币前、混币后等），您可以将所有这些账户归入 `Samourai` 集合下。对于为您的家人管理的钱包，您可能会创建一个名为 `Family` 的集合。

选择 `Create new collection`。然后为您刚刚集成的扩展密钥输入一个名称。例如，如果我扫描了我的Samourai Wallet 的存款账户，我会将这个密钥命名为 `Deposit`。点击 `SAVE` 以完成。

![watch-only](assets/notext/11.webp)

接下来，为这个集合命名，并按屏幕右上角的验证图标以保存集合。您的集合现在在 Sentinel 首页上可见。

![watch-only](assets/notext/12.webp)

如果您希望添加另一个扩展公钥，再次点击 `NEW` 并输入您的密钥。

![watch-only](assets/notext/13.webp)

然后，系统会提示您选择希望将此密钥集成到的集合，或创建一个新集合。例如，在我的情况下，我专门为我的Ledger 钱包设置了一个集合。

![watch-only](assets/notext/14.webp)

为了详细查看集合中的扩展密钥，只需点击它。然后您可以通过不同的标签页浏览交易历史。

![watch-only](assets/notext/15.webp)

从一个集合中，通过点击右上角的三个小点，然后点击 `View Unspent Outputs`，您可以访问被跟踪钱包持有的 UTXO（未花费交易输出）列表。

![watch-only](assets/notext/16.webp)

### 通过 Sentinel 发送和接收比特币
与任何优秀的仅观察钱包一样，Sentinel 允许您生成接收地址，以便在被追踪钱包上接收比特币。但 Sentinel 还提供了一项高级功能：创建和广播部分签名比特币交易 (PSBT)。因此，持有私钥的钱包可以对此交易进行签名，签名后，Sentinel 即可将其广播到比特币网络。让我们看看如何操作。

**注意：不建议向未经钱包自身验证的接收地址接收比特币。** 如果持有私钥的钱包（例如硬件钱包）未明确确认某个地址与其关联，则向该地址发送比特币存在风险。事实上，如果没有此确认，就无法保证该地址确实属于您的钱包。因此，应谨慎使用仅供查看钱包的接收功能，并谨记发送的资金可能丢失。

为了通过 Sentinel 接收比特币，请选择您感兴趣的集合，然后点击与您要转账的扩展公钥对应的选项卡。

![watch-only](assets/notext/17.webp)

最后，点击屏幕左下角的箭头图标。Sentinel 为您生成一个空白的接收地址。您可以复制它，或使用二维码扫描它。

![watch-only](assets/notext/18.webp)
为了从 Sentinel 生成 PSBT 并因此启动支出交易，请转到您希望进行支付的钱包的扩展密钥。以我的Samourai Wallet 的存款账户为例。然后点击屏幕右下角的箭头图标。
![watch-only](assets/notext/19.webp)

输入与您的交易相关的所有参数：
- 输入收款人地址（点击二维码图标，您可以扫描此地址）；
- 指定发送到此地址的金额；
- 确定交易费用。

填写交易所需的所有字段后，按下 `COMPOSE UNSIGNED TRANSACTION` 按钮。

![watch-only](assets/notext/20.webp)

然后，您将访问 PSBT，它代表一个构建但未签名的比特币交易，因为 Sentinel 无法访问您的私钥。您可以选择复制此交易，将其导出为 `.psbt` 文件，或通过动画二维码扫描它。

![watch-only](assets/notext/21.webp)

接着，前往拥有私钥的钱包（Samourai、硬件钱包等）签名交易。

![watch-only](assets/notext/22.webp)

交易签名后，您可以返回到 Sentinel 广播它。为此，从主选单点击右上角的三个小点，然后点击`Broadcast transaction`。

![watch-only](assets/notext/23.webp)

您有三种方式输入您的已签名 PSBT：
- 直接从剪贴板粘贴；
- 从 `.psbt` 文件导入；
- 通过二维码扫描。

![watch-only](assets/notext/24.webp)

在灰色框架中输入已签名交易后，您可以点击绿色的 `BROADCAST TRANSACTION` 按钮，在比特币网络上广播它。Sentinel 将给您提供其 TXID。

![watch-only](assets/notext/25.webp)
