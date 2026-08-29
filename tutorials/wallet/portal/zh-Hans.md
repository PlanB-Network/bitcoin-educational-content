---
name: Portal
description: 配置并使用 TwentyTwo-Devices 硬件钱包 Portal
---
![cover](assets/cover.webp)

Portal 是由 TwentyTwo Devices 设计的比特币硬件钱包，TwentyTwo Devices 是一家专门为比特币爱好者创建开源硬件钱包的公司。TwentyTwo Devices 由 Magical Bitcoin 项目（[此后称为 BDK](https://github.com/bitcoindevkit)）的创建者 Alekos Filini 创立，曾在 Blockstream 和 BHB Network 工作过，其目标是专注于用户自主性、简单性和安全性。

Portal 与市场上其他硬件钱包的不同之处在于它与智能手机的原生集成。它无需电缆或电池即可工作。它使用 NFC 技术为自身供电并与任何兼容的移动钱包进行通信。其有趣的设计是为了符合人体工程学而设计的。圆形部分位于智能手机背面，显示一个屏幕，您可以在其中检查交易详细信息，然后使用专用按钮进行签名。

![Image](assets/fr/01.webp)

Portal 完全开源，基于 Rust 编写的固件，并使用 BDK（比特币开发套件）进行密钥和交易管理。它的售价为 89 欧元[在官方网站上](https://store.twenty-two.xyz/products/portal-hardware-wallet)。

在撰写本文时，Portal 与 Nunchuk 和 Bitcoin Keeper 应用程序兼容。在本教程中，我们将使用 Nunchuk 对其进行配置。

## 拆箱

当您收到 Portal 时，请检查包装盒和密封标签是否完好。在里面，您会在密封袋中找到您的 Portal 钱包。

确保密封完好无损，以确认袋子没有被打开。袋子上以大写字母显示的唯一编号应与蓝色封条下黑色书写的编号、盒子标签上的编号以及首次启动时屏幕上显示的编号相对应。

![Image](assets/fr/02.webp)

## 安装 Nunchuk

为了管理在 Portal 上的钱包，我们将使用 Nunchuk 应用程序。从 [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073)或直接通过[此文件`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases)下载该应用程序。

![Image](assets/fr/03.webp)

如果您第一次使用 Nunchuk，应用程序会提示您创建一个账户。就本教程而言，没有必要创建账户。选择 "*Continue as guest*" 即可在没有账户的情况下继续使用。

![Image](assets/fr/04.webp)

## Portal 配置

在 Nunchuk 主屏幕上，点击屏幕上方的 "*NFC*" 标志。

![Image](assets/fr/05.webp)

将您的 Portal 置于智能手机的背面以激活它。

![Image](assets/fr/06.webp)

Nunchuk 将识别您的门户。然后点击 "*Continue*"。

![Image](assets/fr/07.webp)

要创建新的钱包，请选择 "*Generate seed on Portal*"，然后点击 "*Continue*"。

![Image](assets/fr/08.webp)

您可以选择 12 或 24 个单词的助记词。这两个选项提供的安全性相似，因此您可以选择最容易保存的一个，即 12 个单词。

![Image](assets/fr/09.webp)

然后系统会要求您选择一个密码。该密码可解锁您的 Portal。因此，它可以防止未经授权的物理访问。此密码不参与钱包加密密钥的派生。因此，即使无法访问此密码，拥有 12 或 24 个单词的助记词也将使您能够重新获得对比特币的访问权限。建议选择尽可能随机且足够长的密码。确保将此密码保存在与 Portal 存储位置不同的位置（例如密码管理器中）。

![Image](assets/fr/10.webp)

您的门户将显示您的 12 个单词的助记词。这个助记符让您可以完全、不受限制地访问您的所有比特币。任何拥有此助记词的人都可以窃取您的资金，即使没有实际访问您的 Portal 也是如此。

如果您的 Portal 丢失、被盗或损坏，这 12 个单词的助记词可恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。

您可以将其写在一张纸上，或者为了增加安全性，我建议将其刻在不锈钢底座上，以防止火灾、洪水或倒塌。

关于保存和管理助记词的正确方法的更多信息，我强烈建议您阅读其他教程，特别是如果您是初学者：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，您绝对不能像我在本教程中那样在互联网上分享这些单词。此示例钱包仅用于测试网，并将在本教程结束后删除。

用力按下 Portal 上的按钮，即可输入下一个单词。请确保将整个手指放在按钮上并保持几秒钟，以便正确识别交互。

![Image](assets/fr/11.webp)

然后，您的 Portal 网站将确认您在 Nunchuk 中输入的密码。

![Image](assets/fr/12.webp)

现在您已经完成了门户网站的配置和记忆短语的创建！

![Image](assets/fr/13.webp)

## 比特币钱包配置

在 Nunchuk 上点击 "*Continue*"，同时仍将您的 Portal 对准手机背面。

![Image](assets/fr/14.webp)

在本教程中，我将设置一个单签名钱包，因此选择了该选项。

![Image](assets/fr/15.webp)

使用默认账户，即钱包中的第一个账户（编号为 0）。Nunchuk 会要求您确认 Portal 密码以解锁钱包。

![Image](assets/fr/16.webp)

在 Portal 上，确认将您的 xpub 导出到 Nunchuk。这样您就可以通过智能手机管理钱包，但无法在没有 Portal 的情况下花费比特币。点击按钮确认。

请注意，由于本教程是在测试网上进行的，因此您看到的派生路径与我的不同。

![Image](assets/fr/17.webp)

为您的钱包命名，例如 "*Portal*"，然后点击 "*Continue*"。

![Image](assets/fr/18.webp)

接下来，Nunchuk 会显示您的描述符。建议您备份此描述符。虽然描述符不允许您花费比特币，但它可以让您在钱包恢复时，根据助记词追踪密钥的派生路径。请将其妥善保管，因为即使泄露描述符本身可能不会造成安全问题，但确实存在保密性问题。

点击 "*Done*"。

![Image](assets/fr/19.webp)

现在，您需要为您的比特币钱包生成公钥。为此，请点击 "*Create new wallet*" 按钮。

![Image](assets/fr/20.webp)

再次点击 "*Create new wallet*"。然后选择 "*Create a new wallet using existing keys*" 选项。

![Image](assets/fr/21.webp)

为您的钱包选择一个名称，然后点击 "*Continue*"。

![Image](assets/fr/22.webp)

选择您的 Portal 作为这组新密钥的签名设备，然后点击 "*Continue*"。

![Image](assets/fr/23.webp)

如果一切符合您的要求，请验证创建。

![Image](assets/fr/24.webp)

然后，您可以保存您的钱包配置文件。该文件仅包含您的公钥，这意味着即使有人访问了该文件，也无法窃取您的比特币。但是，他们可以追踪您的所有交易。因此，该文件仅对您的隐私构成风险。在某些情况下，它可能对于恢复您的钱包至关重要。

![Image](assets/fr/25.webp)

就这么简单！

![Image](assets/fr/26.webp)

## 如何通过 Portal 接收比特币？

为了接收比特币，请选择您的钱包。

![Image](assets/fr/27.webp)

使用生成的地址前，请在 Portal 屏幕上进行核对。为此，请单击 "*Receive*"。

![Image](assets/fr/28.webp)

点击三个点，然后选择 "*Verify address via PORTAL*"。然后输入您的密码。

![Image](assets/fr/29.webp)

将您的 Portal 设备放在手机背面，然后按下按钮确认。

![Image](assets/fr/30.webp)

确保 Portal 上显示的地址与您 Nunchuk 控制器上的地址一致，然后再次按下按钮确认。如果地址相同，您可以将此地址提供给付款人。

![Image](assets/fr/31.webp)

一旦接收者的交易被广播，您就会看到它出现在您的钱包上。

![Image](assets/fr/32.webp)

点击 "*View corners*"。

![Image](assets/fr/33.webp)

选择新的 UTXO。

![Image](assets/fr/34.webp)

点击 “*Tags*” 旁边的 “*+*” 即可为您的 UTXO 添加标签。这是一个好习惯，它可以帮助您记住您的比特币来源，并在您未来的消费中优化您的隐私。

![Image](assets/fr/35.webp)

选择一个现有标签或创建一个新标签，然后点击 "*Save*"（保存）。您还可以创建 "*collections*"，以更结构化的方式整理您的比特币。

![Image](assets/fr/36.webp)

## 如何使用 Portal 发送比特币？

现在您的钱包里有比特币了，您也可以发送比特币。为此，请点击您选择的钱包。

![Image](assets/fr/37.webp)

点击 "*Send*" 按钮。

![Image](assets/fr/38.webp)

选择要发送的金额，然后点击 "*Continue*"。

![Image](assets/fr/39.webp)

在未来的交易中添加 "*note*"（备注），以提醒您交易的目的。

![Image](assets/fr/40.webp)

然后在提供的字段中输入接收者的地址。您也可以点击屏幕右上方的图标，扫描编码为二维码的地址。然后点击 "*Create Transaction*" 按钮。

![Image](assets/fr/41.webp)

检查您的交易详情，然后点击您的账户旁边的 “*Sign*” 按钮，并输入您的密码。

![Image](assets/fr/42.webp)

将您的账户放在手机背面。检查接收者的地址和金额是否正确。如果可以，请点击按钮以继续。

![Image](assets/fr/43.webp)

请确认交易费用正确，然后再次按按钮签署您的交易。

![Image](assets/fr/44.webp)

您的交易已经签署。您可以在 Nunchuk 上最后一次检查交易细节，然后点击 "*Broadcast Transaction*" 按钮在比特币网络上广播。

![Image](assets/fr/45.webp)

您的交易正在等待确认。

![Image](assets/fr/46.webp)

恭喜，您现在已经掌握了 Portal 的使用方法！如果您觉得本教程有用，请在下方点赞。欢迎在您的社交网络上分享这篇文章。非常感谢！

想了解更多信息，请查看我们关于分层确定性钱包工作原理的完整培训课程：

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
