---
name: Tapsigner
description: 使用 Nunchuk 设置和使用 Tapsigner
---
![封面](assets/cover.webp)

硬件钱包是一种专用于管理和保护比特币钱包私钥的电子设备。与安装在通常连接互联网的通用计算机上的软件钱包（或热钱包）不同，硬件钱包能够将私钥物理隔离，从而降低被黑客攻击和盗窃的风险。

硬件钱包的主要目标是最大限度地减少设备的功能，从而缩小其攻击面。较小的攻击面也意味着更少的潜在攻击途径，即攻击者可以利用的系统弱点更少，从而更容易访问比特币。

建议使用硬件钱包来保护您的比特币，尤其是在您持有大量比特币的情况下，无论其绝对价值还是占您总资产的比例。

硬件钱包通常与计算机或智能手机上的钱包管理软件配合使用。该软件负责管理交易的创建，但验证这些交易所需的加密签名完全在硬件钱包内部完成。这意味着私钥永远不会暴露在潜在的安全环境中。

硬件钱包为用户提供双重保护：一方面，它们通过将私钥离线保存来保护您的比特币免受远程攻击；另一方面，它们通常具有更强的物理防护能力，能够有效防止密钥被提取。正是基于这两个安全标准，我们可以对市面上不同的硬件钱包型号进行评判和排名。

在本教程中，我将介绍其中一种解决方案：Coinkite 公司的 Tapsigner。

## Tapsigner 简介

Tapsigner 是一款由 Coinkite 公司设计的硬件钱包，外形类似 NFC 卡。Coinkite 公司也以生产 Coldcard 而闻名。

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner 允许存储一对密钥，包括主私钥和符合 BIP32 标准的链码，从而生成加密密钥树。用户只需将 Tapsigner 靠近手机或 NFC 读卡器，即可使用这些密钥签名交易。

这款 NFC 卡售价 19.99 美元，与其他市面上的硬件钱包相比价格非常实惠。然而，由于其卡式设计，Tapsigner 的功能不如其他设备丰富。它显然没有电池、摄像头或 micro SD 卡读卡器，因为它本质上是一张卡。在我看来，它最大的缺点是硬件钱包没有屏幕，这使得它更容易受到某些类型的远程攻击。实际上，这迫使用户盲目签名，并完全信任电脑屏幕上显示的内容。

尽管存在这些限制，但 Tapsigner 凭借其低廉的价格仍然具有吸引力。除了配备屏幕的硬件钱包保护的储蓄钱包外，这款钱包还可以增强消费钱包的安全性。对于持有少量比特币且不想花费数百欧元购买更复杂设备的用户来说，它也是一个不错的选择。此外，在多重签名配置中使用 Tapsigner，或者未来可能在带有时间锁的钱包系统中使用，都能带来一些有趣的优势。

## 如何购买 Tapsigner？

Tapsigner 可在 Coinkite 官方网站 [https://store.coinkite.com/store/category/tapsigner](https://store.coinkite.com/store/category/tapsigner) 购买。您也可以在网站上找到 [认证经销商列表](https://coinkite.com/resellers)，以便从实体店购买。

您还需要一部支持 NFC 通信的手机，或者一个可以读取 13.56 MHz 标准频率 NFC 卡的 USB 设备。

## 如何使用 Nunchuk 初始化 Tapsigner？

收到 Tapsigner 后，第一步是检查包装是否已被打开。如果包装损坏，则可能表明卡片已被盗用，并非真卡。CoinKite 会随 Tapsigner 附赠一个可屏蔽无线电波的保护套。请确保您的包裹中包含此保护套。

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

为了管理钱包，我们将使用 **Nunchuk Wallet** 移动应用程序。确保您的智能手机兼容 NFC，然后从[Google Play 商店](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) 或直接通过其[ `.apk` 文件](https://github.com/nunchuk-io/nunchuk-android/releases)下载 Nunchuk。

![TAPSIGNER NUNCHUK](assets/notext/03.webp)
如果您是第一次使用 Nunchuk，应用会提示您创建账户。但本教程无需创建账户。因此，请选择 "*Continue as guest*" 即可无需账户继续操作。
![TAPSIGNER NUNCHUK](assets/notext/04.webp)

然后点击 "*Unassisted wallet*"。

![TAPSIGNER NUNCHUK](assets/notext/05.webp)

接下来，点击 “*I'll explore on my own*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/06.webp)

进入 Nunchuk 后，点击 “*Keys*” 标签旁的 “*+*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/07.webp)

选择 “*Add NFC key*”。

![TAPSIGNER NUNCHUK](assets/notext/08.webp)

然后点击 “*Add TAPSIGNER*”。

![TAPSIGNER NUNCHUK](assets/notext/09.webp)

点击 “*Continue*”，然后将您的 Tapsigner NFC 卡靠近您的智能手机。

![TAPSIGNER NUNCHUK](assets/notext/10.webp)

如果您的 Tapsigner 是新的，Nunchuk 将提议初始化它。点击“*Yes*”。

![TAPSIGNER NUNCHUK](assets/notext/11.webp)

现在您需要选择如何生成您的主链代码。

Tapsigner 使用 BIP32 标准。这意味着，用于保护您比特币的加密密钥的派生并不像 BIP39 钱包那样依赖于助记词，而是直接依赖于主私钥和主链码。这两个元素会通过 HMAC 函数进行处理，从而确定性地、分层地派生出您钱包的其余部分。

主私钥由集成到 Tapsigner 中的 TRNG（真随机数生成器）直接生成。而主链码则必须从外部提供。在此步骤中，您可以选择：点击 “Automatic” 让 Nunchuk 自动生成，或者选择 “Advanced” 并在提供的字段中输入主链码自行生成。

![TAPSIGNER NUNCHUK](assets/notext/12.webp)

接下来，您需要选择一个 PIN 码。在 “*Starting PIN*” 区域，输入 Tapsigner 背面印有的 PIN 码。

![TAPSIGNER NUNCHUK](assets/notext/14.webp)
现在将您的 Tapsigner 卡放在手机背面以进行初始化。
![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk 将为您的钱包生成恢复文件，以便在您丢失 NFC 卡时重新访问您的比特币。该文件使用写在 Tapsigner 背面的备份代码进行加密。要恢复您的比特币，您必须拥有此文件以及解密代码。因此，务必将此代码打印一份副本，因为如果您丢失了 NFC 卡，也将无法访问此代码，因为它目前仅写入卡上。请务必创建加密恢复文件的多个备份。

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

为您的钱包选择一个名称。

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

您的钱包的基础现在已经设置好了。要随时验证您的 Tapsigner 的真实性，您可以点击 “*Run health check*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

输入您的 PIN 码。

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

然后将您的卡放在手机背面。

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## 如何在 Tapsigner 上创建钱包？

返回到 Nunchuk 首页，您可以看到您的 Tapsigner 已在可用的签名设备中注册。

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

您现在需要为您的比特币钱包生成密钥。为此，点击 “*Wallet*” 标签右侧的 “*+*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

点击 “*Create new wallet*”。

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

然后选择 “*Create a new wallet using existing keys*” 选项。

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

为您的钱包选择一个名称，然后点击 “*Continue*”。

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

选择您的 Tapsigner 作为这组新密钥的签名设备，然后点击 “*Continue*”。

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

如果一切正确无误，请确认创建。

![TAPSIGNER NUNCHUK](assets/notext/27.webp)

然后您可以保存钱包的配置文件。该文件仅包含您的公钥，这意味着即使有人访问了该文件，也无法窃取您的比特币。但是，他们可以追踪您的所有交易。因此，该文件仅对您的隐私构成风险。在某些情况下，它可能对恢复您的钱包至关重要。

![TAPSIGNER NUNCHUK](assets/notext/28.webp)

就这样，您的钱包成功创建了！

![TAPSIGNER NUNCHUK](assets/notext/29.webp)

不使用 Tapsigner 时，请记得将其存放在 Coinkite 提供的保护套中，该保护套可以屏蔽无线电波，防止未经授权的读取。

## 如何在 Tapsigner 上接收比特币？

为了接收比特币，请点击您的钱包。

![TAPSIGNER NUNCHUK](assets/notext/30.webp)

然后使用生成的地址来接收比特币。如果您之前在这个钱包上接收过比特币，您需要点击 “*Receive*” 按钮来生成一个新的空白接收地址。

![TAPSIGNER NUNCHUK](assets/notext/31.webp)

一旦发送者的交易被广播，您将在您的钱包上看到它出现。

![TAPSIGNER NUNCHUK](assets/notext/32.webp)

点击 “*View coins*”。

![TAPSIGNER NUNCHUK](assets/notext/33.webp)

选择您的新 UTXO（未花费交易输出）。

![TAPSIGNER NUNCHUK](assets/notext/34.webp)

点击 “*Tags*” 旁边的 “*+*” 来给您的 UTXO 添加一个标签。这是一个好习惯，因为它帮助您记住您的 UTXO 的来源，并为未来的支出优化您的隐私。

![TAPSIGNER NUNCHUK](assets/notext/35.webp)

选择一个现有标签或创建一个新标签，然后点击 “*Save*”。您还可以创建 “*collections*” 来更系统地整理您的比特币。

![TAPSIGNER NUNCHUK](assets/notext/36.webp)

## 如何使用 Tapsigner 发送比特币？

现在您的钱包中有了比特币，您也可以发送它们。为了做到这一点，请点击您选择的钱包。

![TAPSIGNER NUNCHUK](assets/notext/37.webp)

点击 “*Send*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/38.webp)

选择要发送的金额，然后点击 “*Continue*”。

![TAPSIGNER NUNCHUK](assets/notext/39.webp)

添加一个 “*note*” 到您未来的交易中，以记住其用途。

![TAPSIGNER NUNCHUK](assets/notext/40.webp)
接下来，在指定字段中手动输入接收者的地址。
![TAPSIGNER NUNCHUK](assets/notext/41.webp)

您也可以通过点击屏幕右上角的图标来扫描编码的二维码地址。

![TAPSIGNER NUNCHUK](assets/notext/42.webp)

点击 “*Create Transaction*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/43.webp)

验证您的交易详情，然后点击您的 Tapsigner 旁边的 “*Sign*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/44.webp)

输入您的 PIN 码以解锁它。

![TAPSIGNER NUNCHUK](assets/notext/45.webp)

然后将 Tapsigner 放在您的智能手机背面。
![TAPSIGNER NUNCHUK](assets/notext/46.webp)
您的交易现已签名。请最后再次检查一切是否正确，然后点击 “*Broadcast Transaction*” 将其广播到比特币网络上。

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

您的交易现在正在等待确认。

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## 如果 Tapsigner 丢失，如何恢复钱包？

如果您丢失了 Tapsigner，您可以使用卡片背面记下的代码恢复您的钱包。因此，将此代码与 Tapsigner 分开保存很重要，因为如果卡片丢失，访问此代码的能力也将丢失。您还需要钱包的加密备份。

为了恢复，我们将使用 Nunchuk 应用程序，但请记住，这意味着暂时将您的资金保护在一个热钱包中。如果您的 Tapsigner 保护了大量资金，考虑使用新的 Coldcard 遵循相同的恢复过程。

打开 Nunchuk 应用程序，然后点击 “*Keys*” 标签旁的 “*+*” 按钮。

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

选择 “*Add NFC key*”。

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

选择 “*Recover TAPSIGNER key from backup*” 选项。

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

然后，您将被重定向到您设备的文件资源管理器。定位并选择您钱包的加密备份文件。通常，此文件的名称以`backup...` 开头。

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

输入用于解密备份文件的密码。此密码与您最初记录在 Tapsigner 背面的密码一致。

![TAPSIGNER NUNCHUK](assets/notext/53.webp)

然后为您的恢复钱包选择一个名称。

![TAPSIGNER NUNCHUK](assets/notext/54.webp)

您现在已重新获得对比特币的访问权限。您的钱包现在作为热钱包进行管理，可在 Nunchuk 应用的 “*Keys*” 选项卡中查看。接下来，您需要在 “*Wallets*” 部分中创建一个新的加密密钥集，并将此密钥与之关联。为此，您可以再次按照本教程 “*How to create a wallet on a Tapsigner?*” 部分中的步骤进行操作。

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

如果您丢失了 Tapsigner，我强烈建议您立即将比特币转移到您拥有的另一个钱包，最好是使用硬件钱包进行保护的钱包。没错，您丢失的 Tapsigner 钱包可能落入了不法分子手中。因此，务必清空您刚刚找回的钱包，并停止使用。

恭喜！您现在已经掌握了 Tapsigner 的使用方法！如果您觉得这篇教程有用，请在下方点赞。欢迎在社交网络上分享这篇文章。非常感谢！
