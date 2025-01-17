---
name: 绿色 Blockstream - 液体
description: 在 Liquid Network 侧链上建立投资组合
---
![cover](assets/cover.webp)

比特币协议有一些有意的技术限制，这些限制有助于维持网络的去中心化，并确保安全分布在所有用户之间。然而，这些限制有时会让用户感到沮丧，特别是在同时进行大量交易导致拥堵时。长期以来，关于比特币可扩展性的争论在社区中一直存在分歧，尤其是在 "区块大小战争 "期间。自那以后，比特币社区普遍认为，可扩展性必须通过第二层系统的链外解决方案来保证。这些解决方案包括侧链，与闪电网络等其他系统相比，侧链仍然相对陌生，也很少使用。

侧链是与比特币主区块链平行运行的独立区块链。它使用比特币作为记账单位，这要归功于一种叫做 "*双向挂钩*"的机制。该系统可以在主链上锁定比特币，以便在侧链上复制其价值，在侧链上，比特币以原始比特币支持的代币形式流通。这些代币通常与锁定在主链上的比特币保持同等价值，而这一过程可以逆转，以收回比特币上的资金。

侧链的目的是提供额外的功能或技术改进，如加快交易速度、降低费用或支持智能合约。这些创新不能总是直接在比特币区块链上实现，而不影响其去中心化或安全性。因此，侧链可以在保持比特币完整性的同时测试和探索新的解决方案。然而，这些协议往往需要做出妥协，特别是在去中心化和安全性方面，这取决于所选择的治理模式和共识机制。

如今，最著名的侧链可能就是 Liquid 了。在本教程中，我将首先告诉你什么是 Liquid，然后指导你如何通过 Blockstream Green 应用程序开始轻松使用它，从而享受它的所有好处。

![LIQUID GREEN](assets/fr/01.webp)

## 什么是 Liquid Network？

Liquid是比特币的联盟侧链覆盖层，由Blockstream开发，旨在提高交易速度、保密性和功能性。它使用在联盟上建立的双边锚定机制，将比特币锁定在主链上，并创建 Liquid-bitcoins（L-BTC）作为回报，这些代币在 Liquid 上流通，同时仍由原始比特币提供支持。

![LIQUID GREEN](assets/fr/02.webp)

Liquid 网络依赖于一个由比特币生态系统中公认的实体组成的参与者联盟，他们负责验证区块并管理双边挂钩。除 L-BTC 外，Liquid 还能发行其他数字资产，如稳定币和其他加密货币。

![LIQUID GREEN](assets/fr/03.webp)

## 绿色 Blockstream 介绍

Blockstream Green是一款软件钱包，可在移动端和桌面端使用。该钱包前身为*Green Address*，在2016年被收购后成为Blockstream项目。

Green 是一款特别简单易用的应用程序，这使它对初学者很有吸引力。它提供了优秀比特币钱包的所有基本功能，包括 RBF（*收费替换*）、Tor 连接选项、连接自己的节点、SPV（*简单支付验证*）、硬币标记和控制。

Blockstream Green还支持Liquid网络，我们将在本教程中了解这一点。如果你想将 Green 用于其他应用，我建议你也看看其他教程：

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb
## 安装和配置 Blockstream Green 应用程序

第一步当然是下载绿色应用程序。前往应用程序商店：

- [Android版](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)；
- [苹果公司](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590)。
![LIQUID GREEN](assets/fr/04.webp)

对于安卓用户，您也可以通过`.apk`文件[可在 Blockstream 的 GitHub 上获取](https://github.com/Blockstream/green_android/releases)安装应用程序。

![LIQUID GREEN](assets/fr/05.webp)

启动应用程序，然后勾选 "我接受条件...*"框。

![LIQUID GREEN](assets/fr/06.webp)

首次打开 Green 时，主屏幕上没有配置的投资组合。之后，如果你创建或导入投资组合，它们就会出现在这个界面中。在创建投资组合之前，我建议你调整应用程序设置，以满足自己的需要。点击 "应用程序设置"。

![LIQUID GREEN](assets/fr/07.webp)

仅适用于 Android 系统的 "*增强隐私*"选项可通过禁用屏幕截图和隐藏应用程序预览来增强隐私。一旦手机被锁定，它还会自动锁定应用程序的访问权限，使你的数据更难暴露。

![LIQUID GREEN](assets/fr/08.webp)

对于那些希望加强隐私保护的用户，程序提供了通过 Tor（一个对所有连接进行加密的网络，使你的活动难以被追踪）根植流量的选项。虽然这个选项可能会略微减慢程序的运行速度，但还是强烈建议使用它来保护你的隐私，尤其是在你不使用自己的完整节点时。

![LIQUID GREEN](assets/fr/09.webp)

对于拥有自己完整节点的用户，Green Wallet 提供了通过 Electrum 服务器与之连接的选项，以保证对比特币网络信息和交易传播的完全控制。但这个功能是针对经典比特币钱包的，所以如果你使用的是 Liquid，就不需要这个功能了。

![LIQUID GREEN](assets/fr/10.webp)

另一个替代功能是 "*SPV 验证*"选项，它允许您直接验证某些区块链数据，从而减少对 Blockstream 默认节点的信任，不过这种方法并不能提供完整节点的所有保证。同样，这只会影响您的链上比特币钱包，而不会影响 Liquid。

![LIQUID GREEN](assets/fr/11.webp)

根据需要调整这些设置后，点击 "*保存*"按钮并重新启动应用程序。

![LIQUID GREEN](assets/fr/12.webp)

## 在 Blockstream Green 上创建液体投资组合

现在您已准备好创建 Liquid 投资组合。点击 "*开始*"按钮。

![LIQUID GREEN](assets/fr/13.webp)

您可以选择创建本地软件钱包或通过硬件钱包管理冷钱包。本教程的重点是在 Liquid 上创建热钱包，因此您需要选择 "*在此设备上*"选项。您也可以使用兼容的硬件钱包（如 Blockstream Jade）来保护您的 Liquid 钱包。

![LIQUID GREEN](assets/fr/14.webp)

然后，你可以选择恢复现有的比特币钱包或创建一个新钱包。在本教程中，我们将创建一个新钱包。但是，如果你需要从现有的液体钱包的记忆短语中重新生成一个新的钱包，比如在硬件钱包丢失之后，你需要选择第二个选项。

![LIQUID GREEN](assets/fr/15.webp)

然后，您可以选择 12 个字或 24 个字的记忆短语。如果您的手机出现问题，这个短语可以让您通过任何兼容软件恢复对钱包的访问。目前，选择 24 个字的短语并不比 12 个字的短语更安全。因此，我建议您选择 12 个字的记忆短语。

然后，绿色将为您提供记忆短语。在继续之前，请确保您没有被监视。点击 "*显示恢复短语*"将其显示在屏幕上。

![LIQUID GREEN](assets/fr/16.webp)

**本记忆法可让您完全不受限制地访问您的所有比特币 ** 任何拥有本记忆法的人都可以盗取您的资金，即使无法实际访问您的手机。

在手机丢失、被盗或损坏的情况下，它可以恢复对比特币的访问。因此，在物理介质（而非数字介质）**上仔细备份并将其存放在安全的地方非常重要。你可以把它写在一张纸上，或者为了增加安全性，如果这是一个大型钱包，我建议把它刻在一个不锈钢支架上，以防止火灾、水灾或倒塌的风险（对于旨在保护少量比特币的热钱包，简单的纸质备份可能就足够了）。

*显然，您绝不能像我在本教程中所做的那样，在互联网上分享这些文字。本示例作品集将仅在 Liquid 的 Testnet 上使用，并将在教程结束后删除。

![LIQUID GREEN](assets/fr/17.webp)

在物理介质上正确记录记忆短语后，点击 "*继续*"。然后，绿色钱包会要求您确认记忆短语中的一些单词，以确保您正确记录了这些单词。在空白处填上缺失的单词。

![LIQUID GREEN](assets/fr/18.webp)

选择设备的 PIN 码，用于解锁绿色钱包。这可以防止未经授权的物理访问。该 PIN 码不参与钱包加密密钥的生成。因此，即使无法获得 PIN 码，只要拥有 12 或 24 个字的记忆短语，就可以重新获得比特币。

我们建议您选择一个尽可能随机的 6 位数 PIN 码。请务必保存好这个密码，以免忘记，否则就只能通过助记符找回钱包了。然后，您可以添加生物识别拦截选项，避免每次使用时都要输入 PIN 码。一般来说，生物识别技术的安全性远远低于 PIN 码本身。因此，在默认情况下，我建议你不要设置这个解锁选项。

![LIQUID GREEN](assets/fr/19.webp)

再次输入密码确认。

![LIQUID GREEN](assets/fr/20.webp)

等待您的投资组合创建完成，然后点击 "*创建账户*"按钮。

![LIQUID GREEN](assets/fr/21.webp)

在 "*活动*"框中，选择 "*液体比特币*"。然后，您可以选择一个标准的单签名钱包（我们将在本教程中使用），或者一个受双因素身份验证（2FA）保护的钱包。

![LIQUID GREEN](assets/fr/22.webp)

就这样，您的 Liquid 钱包就使用绿色应用程序创建完成了！

![LIQUID GREEN](assets/fr/23.webp)

在您的 Liquid 钱包收到第一个比特币之前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，如您的 xpub 或第一个接收地址，然后在 Green 应用程序上删除您的钱包，此时钱包还是空的。然后尝试使用纸质备份在 Green 上恢复钱包。检查还原后生成的 cookie 信息是否与您最初写下的信息一致。如果吻合，您就可以放心，您的纸质备份是可靠的。要了解有关如何进行测试恢复的更多信息，请参阅本教程：

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## 建立流动性投资组合

如果您想个性化您的作品集，请点击右上角的三个小圆点。

![LIQUID GREEN](assets/fr/24.webp)

通过 "*Rename*"（重命名）选项，您可以自定义投资组合的名称，如果您在同一个应用程序中管理多个投资组合，这个选项尤其有用。

![LIQUID GREEN](assets/fr/25.webp)

通过 "*单位*"菜单，您可以更改钱包的基本单位。例如，您可以选择用卫星币而不是比特币显示。

![LIQUID GREEN](assets/fr/26.webp)

通过 "*设置*"菜单可以访问比特币钱包的各种选项。

![LIQUID GREEN](assets/fr/27.webp)

例如，您可以在这里找到您的*描述符*，如果您计划在此 Liquid 投资组合中设置一个只供观看的投资组合，它可能会派上用场。

![LIQUID GREEN](assets/fr/28.webp)

您还可以更改钱包密码和激活生物识别连接。

![LIQUID GREEN](assets/fr/29.webp)

## 使用您的流动资金组合

现在，您的 Liquid 投资组合已经建立，您已经准备好接收第一批 L-sats 了！

如果您还没有 L-BTC，您有几种选择。第一种是直接向您发送比特币。如果有人想在 Liquid 上用比特币付款给你，只需给他们一个收款地址即可。另一种方法是在链上或闪电网络上用比特币兑换 L-BTC。为此，您可以使用 [Boltz 等桥接器](https://boltz.exchange/)。只需在网站上输入您的 Liquid 地址，然后通过闪电网络或链上付款即可。

![LIQUID GREEN](assets/fr/30.webp)

要生成液体地址，请单击 "*接收*"按钮。

![LIQUID GREEN](assets/fr/31.webp)

然后，绿色将显示您钱包中的第一个空白接收地址。您可以扫描相关的二维码，或直接复制地址来发送 L-BTC。

![LIQUID GREEN](assets/fr/32.webp)

交易在网络上广播后，就会出现在您的钱包中。

![LIQUID GREEN](assets/fr/33.webp)

等到收到足够多的确认后，交易才算确定。在 Liquid 上，确认应该很快，因为每分钟都会发布一个区块。

![LIQUID GREEN](assets/fr/34.webp)

如果您的 Liquid 组合中有 L-sats，您现在也可以发送它们。点击 "*发送*"。

![LIQUID GREEN](assets/fr/35.webp)

在下一页，输入收件人的液体地址。您可以手动输入或扫描二维码。

![LIQUID GREEN](assets/fr/36.webp)

选择付款金额。

![LIQUID GREEN](assets/fr/37.webp)

点击 "*下一步*"进入交易摘要屏幕。检查地址、金额和费用是否正确。

![LIQUID GREEN](assets/fr/38.webp)

如果一切顺利，将屏幕底部的绿色按钮向右滑动，即可在比特币网络上签署并广播交易。

![LIQUID GREEN](assets/fr/39.webp)

您的交易将显示在比特币钱包仪表板上，等待确认。

![LIQUID GREEN](assets/fr/40.webp)

现在你知道如何通过 Blockstream Green 应用程序轻松使用 Liquid 侧链了吧！

如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。非常感谢

我还建议您查看 Blockstream Green 移动应用程序的其他综合教程，了解如何设置链上比特币热钱包：

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143