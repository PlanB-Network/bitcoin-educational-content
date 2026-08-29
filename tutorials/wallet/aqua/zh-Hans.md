---
name: Aqua
description: 一款集比特币、闪电网络与 Liquid 于一体的钱包
---
![cover](assets/cover.webp)

Aqua 是一款移动应用程序，可让您轻松创建比特币和 Liquid 的热钱包。得益于它的交换功能，它还提供了使用闪电网络的可能性，而无需管理自己的节点。它还能在各种网络上管理 USDT 稳定币。

Aqua 应用程序由 JAN3 公司在 Samson Mow 的带领下开发，最初是专为满足拉丁美洲用户的需求而设计的，但它实际上也适合世界各地的任何用户。对于初学者和日常使用比特币支付的人来说，它尤其有趣。

在本教程中，我们将了解如何使用 Aqua 的众多功能。但我们需要先了解一下什么是比特币的侧链，Liquid 是如何工作的，这样我们才能全面地理解 Aqua 的价值。

![AQUA](assets/fr/01.webp)

## 何为侧链（Sidechain）？

比特币协议有一些技术限制，这些限制有助于维持网络的去中心化性质，并确保每个用户的安全。然而，这些限制有时会让用户感到烦恼，特别是在有大量待处理的比特币交易时。长期以来，关于比特币可扩展性的争论在社区中一直存在分歧，尤其是在 "区块大小战争" 期间。自那以后，比特币社区普遍认为，可扩展性必须通过第二层系统的链外解决方案来实现。这些解决方案包括侧链，与闪电网络等其他系统相比，侧链仍然相对陌生，也很少被使用。

侧链是与比特币主区块链平行运行的独立区块链。它使用比特币作为记账单位，这要归功于一种叫做 "*双向挂钩*"（two-way peg）的机制。该系统可以在主链上锁定比特币，以便侧链与主链的价值保持平等，在侧链上，比特币以原始比特币支持的代币形式流通。这些代币通常与锁定在主链上的比特币保持同等价值，而这一过程可以逆转，以收回比特币上的资金。

侧链的目的是提供额外的功能或技术改进，如加快交易速度、降低费用或支持智能合约。这些创新不能总是直接在比特币区块链上实现，而不影响其去中心化或安全性。因此，侧链可以在保持比特币真实性的同时测试和探索新的解决方案。然而，这些协议往往需要在去中心化与安全性之间作出权衡，这取决于所采用的治理模式和共识机制。

## Liquid 是什么？

Liquid 是比特币上的联盟侧链层面，由 Blockstream 开发，旨在提高交易速度、保密性和功能性。它使用在联盟上建立的双边锚定机制，将比特币锁定在主链上，并创建 Liquid-bitcoins（L-BTC）作为回报，这些代币在 Liquid 上流通，同时仍由原始比特币支持。

![AQUA](assets/fr/02.webp)

Liquid 网络依赖于一个由比特币生态系统中公认的实体组成的参与者联盟，他们负责验证区块并管理双边挂钩。除 L-BTC 外，Liquid 还能发行其他数字资产，如 USDT 稳定币和其他加密货币。

![AQUA](assets/fr/03.webp)

## 安装 Aqua 应用程序

第一步当然是下载 Aqua 应用程序。您可以先前往应用程序商店：

- [Android 版本](https://play.google.com/store/apps/details?id=io.aquawallet.android)；
- [苹果版本](https://apps.apple.com/us/app/aqua-wallet/id6468594241)。
![AQUA](assets/fr/04.webp)

对于 Android 用户，您还可以选择通过 `.apk` 文件安装应用程序[可在其 GitHub 上访问](https://github.com/AquaWallet/aqua-wallet/releases)。

![AQUA](assets/fr/05.webp)

启动应用程序，然后勾选 "*I have read and agreed to the Terms of Service & Privacy Policy*" 框。

![AQUA](assets/fr/06.webp)

## 在 Aqua 上创建您的作品集

点击 "*Create Wallet*" 按钮。

![AQUA](assets/fr/07.webp)

这样，您的钱包已经创建好了！

![AQUA](assets/fr/08.webp)

但首先，由于这是一个自我保管的钱包，您必须准备一个助记词的物理备份。 **这个助记词能让您访问您所有的比特币**。任何拥有该助记词的人都可以盗取您的比特币，即使他们无法访问您的手机。

它可以让您在手机丢失、被盗或损坏时恢复您的比特币。因此，重要的是要将它小心保存在物理介质（而不是数字介质）上并存放在安全的地方。您可以把它写在一张纸上，或者为了增加安全性，如果这是一个大型钱包，我建议把它刻在一个不锈钢支架上，以防止火灾、水灾或倒塌的风险（对于旨在保护少量比特币的热钱包，简单的纸质备份可能就足够了）。

为此，请单击 "Settings" 选单。

![AQUA](assets/fr/09.webp)

然后点击 "*View Seed Phrase*"。请准备该 12 个字助记词的物理备份。

![AQUA](assets/fr/10.webp)

在同一设置选单中，您还可以更改应用程序语言和法定货币。

![AQUA](assets/fr/11.webp)

使用钱包接收第一笔比特币前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，如您的 xpub 或第一个接收地址，然后在 Aqua 应用程序上删除您的钱包（钱包还是空的，没有比特币）。然后尝试使用您的助记词纸质备份在 Aqua 上恢复钱包。检查还原后生成的 cookie 信息是否与您最初写下的信息一致。如果吻合，您就可以放心，您的纸质备份是可靠的。如果您想要了解有关如何进行测试恢复的更多信息，请参阅本教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

您无法在我的屏幕上看不到这一选项，因为我在使用模拟器，但您还可以在设置中找到通过生物识别认证系统锁定应用的选项。我强烈建议您启用此安全功能，因为如果未开启，任何拥有您解锁手机的人都可能盗取您的比特币。您可以在 iOS 上使用 Face ID 或在 Android 上使用指纹。如果这些方法在认证时失败，您仍然可以通过手机的PIN 码访问该应用程序。

## 使用 Aqua 接收比特币

钱包设置完成后，您就可以接收比特币了！只需点击 "*Wallet*" 选单中的 "*Receive*" 按钮即可。

![AQUA](assets/fr/12.webp)

您可以选择接收比特币的方式：链上、闪电网络或 Liquid 网络。

![AQUA](assets/fr/13.webp)

对于链上交易，Aqua 会生成一个特定的接收地址，您可以在此接收比特币。

![AQUA](assets/fr/14.webp)

与此相似，如果您选择 Liquid，Aqua 将为您提供一个 Liquid 地址。

![AQUA](assets/fr/15.webp)

如果您想要通过 "闪电网络"（Lightning）接收比特币，您首先需要输入要接收的金额。

![AQUA](assets/fr/16.webp)

然后，点击 "*Generate Invoice*"。

![AQUA](assets/fr/17.webp)

Aqua 将创建一张闪电钱包接收资金的发票。请注意，与链上和 Liquid 选项不同，通过闪电钱包收到的资金将使用 Boltz 工具在 Liquid 上自动转换为 L-BTC，因为 Aqua 不是一个闪电节点。这个过程允许您通过闪电接收和发送资金，但不会将比特币以闪电比特币的形式存储。

![AQUA](assets/fr/18.webp)

就我个人而言，我会先通过 "闪电" 向 Aqua 发送比特币。一旦交易完成并提供了发票，我们就会收到确认。

![AQUA](assets/fr/19.webp)

为了检查交换的状态，请返回钱包主页，点击 "*L2 Bitcoin*" 账户，其中列出了闪电交易（通过交换）和 Liquid 交易。

![AQUA](assets/fr/20.webp)

在此处，您可以查看您的交易和 L-BTC 余额。

![AQUA](assets/fr/21.webp)

## 使用 Aqua 进行比特币交换

现在您的 Aqua 钱包中已经有了比特币，您可以直接从应用程序中进行交换，将其转移到主比特币区块链或 Liquid 中。您还可以将比特币兑换成 USDT 稳定币（或其他形式的货币）。为此，请进入 "*Marketplace*" 选单。

![AQUA](assets/fr/22.webp)

点击 "*Swaps*"。

![AQUA](assets/fr/23.webp)

在 "*Transfer from*" 框中，选择您要交易的资产。目前，我只拥有 L-BTC，所以我选择了 L-BTC。

![AQUA](assets/fr/24.webp)

在 "*Transfer to*" 框中，选择掉期的目标资产。我选择了 Liquid 网络上的 USDT。

![AQUA](assets/fr/25.webp)

输入您希望转换的金额。

![AQUA](assets/fr/26.webp)

点击 "*Confirm*" 以确认。

![AQUA](assets/fr/27.webp)

确认交换设置无误后，在屏幕底部拖动 “Swap” 按钮以完成操作。

![AQUA](assets/fr/28.webp)

您的交换现已确认。

![AQUA](assets/fr/29.webp)

在我们的钱包中，您可以发现我们现在在 Liquid 上拥有 USDT。

![AQUA](assets/fr/30.webp)

## 使用 Aqua 发送比特币

现在您的 Aqua 钱包里已经有了比特币，您可以发送比特币了。点击 "*Send*" 按钮。

![AQUA](assets/fr/31.webp)

选择要发送的货币，或选择进行交易的网络。就我而言，我将通过闪电网络发送比特币。

![AQUA](assets/fr/32.webp)

接下来，输入发送付款所需的信息：对于链上比特币或 Liquid 比特币，您需要输入接收地址；对于闪电比特币，您需要一个发票。您可以直接将这些信息粘贴到提供的字段中，或者使用二维码图标打开相机扫描地址或发票。然后点击 "*Continue*"。

![AQUA](assets/fr/33.webp)

如果所有信息都正确无误，请再次点击 "*Continue*"。

![AQUA](assets/fr/34.webp)

然后 Aqua 会向您显示交易详情。请确保所有信息正确无误，包括目的地地址、费用和金额。为了确认交易，请滑动屏幕底部的 "*Slide to send*" 按钮。

![AQUA](assets/fr/35.webp)

然后，您将收到发送比特币的确认信息。

![AQUA](assets/fr/36.webp)

现在您知道如何使用 Aqua 应用程序接收和使用比特币、闪电和 Liquid 资金了。

如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢！

我还建议您查看关于 Blockstream Green 移动应用程序的其他综合教程，这是另一种有趣的 Liquid 钱包设置解决方案：

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

