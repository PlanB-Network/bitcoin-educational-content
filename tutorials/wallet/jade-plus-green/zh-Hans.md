---
name: Jade Plus - Green
description: 使用 Green 软件轻松配置 Jade Plus 钱包
---
![cover](assets/cover.webp)

Jade Plus 是 Blockstream 设计的一款仅支持比特币的硬件钱包。它是普通 Jade 的升级版，在软件方面进行了改进，增加了更多功能，并重新设计了符合人体工程学的外形，使其使用起来更加直观。这款新版本配备了一块出色的 1.9 英寸 LCD 屏幕，色域比上一代产品更广。按键和选单导航也得到了优化。

Jade Plus 的使用方式多种多样：可通过 USB-C 有线连接，也可使用 micro SD 卡的 “空气隔离” 模式（需要适配器），还可通过蓝牙连接，甚至可以借助内置摄像头交换二维码。这款硬件钱包采用电池供电。

基础黑色版售价 149.99 美元起，而 "*Genesis Grey*" 或 "*Lunar Silver*" 版本的价格最高可在此基础上增加 20 美元。因此，Jade Plus 是一个不错的选择，它拥有媲美 Coldcard Q 或 Passport V2 等高端硬件钱包的先进功能，但价格却相当低廉，接近中端机型。

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus 与大多数钱包管理软件兼容。以下是截至撰写本文时（2025 年 1 月）的兼容性汇总：

| 管理软件              | 桌面端 | 移动端 | USB | 蓝牙      | 二维码 | JadeLink |
| ----------------- | --- | --- | --- | ------- | ---- | -------- |
| Blockstream Green | 🟢  | 🟢  | 🟢  | 🟢（移动端） | 🟢   | 🔴       |
| Liana             | 🟢  | 🔴  | 🟢  | 🔴      | 🔴   | 🔴       |
| Sparrow           | 🟢  | 🔴  | 🟢  | 🔴      | 🟢   | 🟢       |
| Nunchuk           | 🟢  | 🟢  | 🔴  | 🔴      | 🟢   | 🟢       |
| Specter           | 🟢  | 🔴  | 🔴  | 🔴      | 🟢   | 🟢       |
| BlueWallet        | 🟢  | 🟢  | 🔴  | 🔴      | 🟢   | 🟢       |
| Electrum          | 🟢  | 🔴  | 🟢  | 🔴      | 🔴   | 🔴       |
| Keeper            | 🔴  | 🟢  | 🔴  | 🔴      | 🟢   | 🔴       |

在本教程中，我们将通过蓝牙连接，设置并使用 Jade Plus 和 Blockstream 的 Green Wallet 移动应用程序。此设置非常适合初学者。如果您正在寻找更高级的方法，我建议您查看这篇教程，其中我们使用 Jade Plus 和 Sparrow Wallet 的二维码模式：

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Jade Plus 安全模型

Jade Plus 使用基于 “虚拟安全元件”（virtual secure element）的安全模型，该元件由 “盲断言机”（blind oracle）实现。具体来说，该机制结合了用户选择的 PIN 码、Jade 上存储的密钥以及盲断言（由 Blockstream 维护的服务器）持有的密钥，生成一个分布在两个实体上的 AES-256 密钥。在初始化过程中，ECDH 交易所会确保与预言机的通信安全，并对硬件钱包上的恢复助记词进行加密。实际上，当您需要访问种子以签署交易时，您需要访问：

- Jade Plus 设备本身；
- 用于解锁设备的 PIN 码；
- 以及断言机的密钥。

这种方法的主要优势在于硬件层面不存在单点故障，因为即使攻击者获得了您的 Jade 设备，提取密钥也需要同时攻破 Jade 设备和断言机。此外，该模型还意味着 Jade Plus 完全开源，避免了使用真正物理安全元件（例如 Ledger 所使用的元件）所带来的限制。

该系统的缺点是 Jade Plus 的使用依赖于 Blockstream 维护的断言机。如果该断言机无法访问，则无法再使用 PIN 码直接操作硬件钱包。然而，这并不意味着您的比特币就此丢失，因为您仍然可以使用助记词找回它们。您可以在 Jade Plus 的 “无状态”（stateless）模式下输入助记词。为了绕过这种依赖性，您还可以配置和管理自己的断言机服务器。

管理助记词的另一种方法是不要将其注册到 Jade Plus 上。在这种情况下，Jade 就仅作为签名设备使用。在初始化过程中，除了像往常一样将助记词保存为单词之外，您还需要将其保存为手动生成的二维码。这样，每次使用钱包时，您都可以使用 Jade 的摄像头导入助记词。对于高级用户来说，这可能是一个不错的选择，具体取决于您的安全策略。但您需要谨慎地保存和保护您的助记词，因为即使是二维码，也可能让任何人窃取您的资金。我们将在本教程中介绍此选项，但这并非强制性的。

## Jade Plus开箱

当您收到 Jade Plus 时，请检查包装盒和封条是否完好，以确保您的包裹没有被打开过。

![JADE-PLUS-GREEN](assets/fr/02.webp)

在盒子内，您会看到以下物品 ：

- Le Jade Plus；
- USB-C 电缆；
- 以单词或 "*CompactSeedQR*" 的形式记录助记词的卡片；
- 一些使用说明 ；
- 一条绳索
- 一些贴纸

![JADE-PLUS-GREEN](assets/fr/03.webp)

该设备有 4 个导航按钮：

- 右下角的按钮可以打开 Jade；
- 设备正面的大按钮用于选择项目；
- 顶部的两个小按钮可以让您向左和向右导航；
- 您还可以同时点击设备顶部的两个按钮来选择项目。

![JADE-PLUS-GREEN](assets/fr/04.webp)

## 设置新的比特币钱包

点击开启按钮。

![JADE-PLUS-GREEN](assets/fr/05.webp)

点击 "*Setup Jade*"。

![JADE-PLUS-GREEN](assets/fr/06.webp)

选择 “Begin Setup”。您也可以点击 "*Advanced Setup*"。如果您选择了高级设置，您就可以访问高级设置。

![JADE-PLUS-GREEN](assets/fr/07.webp)

然后点击"*Create a New Wallet*"以生成新种子。

![JADE-PLUS-GREEN](assets/fr/08.webp)

点击 "*Continue*" 按钮以显示新的恢复助记词。

![JADE-PLUS-GREEN](assets/fr/09.webp)

您的 Jade Plus 上会显示您的 12 个单词的助记词。**此助记词可让您完全无限制地访问您的所有比特币。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Jade Plus。如果您的 Jade 丢失、被盗或损坏，这 12 个单词的助记词可帮助您恢复对比特币的访问权限。因此，请务必妥善保管此助记词并将其存放在安全的地方。**

您可以将其写在包装盒内提供的纸板上，或者为了更加安全，我建议您将其刻在不锈钢底座上，以保护其免受火灾、洪水或跌落的损害。

![JADE-PLUS-GREEN](assets/fr/10.webp)

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，您绝不能像我在本教程中那样在互联网上分享这些助记词。此示例钱包仅用于测试网，并将在教程结束后删除。

点击屏幕右侧的箭头以显示以下助记词。

![JADE-PLUS-GREEN](assets/fr/11.webp)

保存助记词后，Jade Plus 会要求您确认。使用设备顶部的按钮，按顺序选择正确的单词，然后点击中间的按钮进入下一个单词。

![JADE-PLUS-GREEN](assets/fr/12.webp)

## 将 Jade Plus 连接到 Green Wallet

在本教程中，我们将使用 Green Wallet 应用程序来管理托管在 Jade Plus 上的钱包。此方法特别适合初学者。如果您想更详细地管理您的比特币钱包，您还可以使用 Sparrow Wallet，我们将在另一篇教程中介绍它：

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

为了解安装和设置 Blockstream Green 应用程序的说明，请参阅另一篇教程的第一部分：

https://planb.academy/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

进入 Blockstream Green 应用程序后，点击 "*Configure a new wallet*" 按钮。

![JADE-PLUS-GREEN](assets/fr/13.webp)

选择 "*On Hardware Wallet*"。

![JADE-PLUS-GREEN](assets/fr/14.webp)

激活智能手机上的蓝牙，然后点击 "*Connect your Jade*" 按钮。

![JADE-PLUS-GREEN](assets/fr/15.webp)

授权 Green Wallet 应用程序访问蓝牙连接。

![JADE-PLUS-GREEN](assets/fr/16.webp)

该应用程序正在查找您的 Jade Plus。

![JADE-PLUS-GREEN](assets/fr/17.webp)

在 Jade Plus 上，点击 "*Bluetooth*" 选单。

![JADE-PLUS-GREEN](assets/fr/18.webp)

在 Green 应用程序中选择您的设备。

![JADE-PLUS-GREEN](assets/fr/19.webp)

在 Jade Plus 上确认配对代码。

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green 为您提供一个测试，以确保您的 Jade 是一个真品。点击 “Confirm Check” 按钮以进行测试。

![JADE-PLUS-GREEN](assets/fr/21.webp)

在 Jade 上确认。

![JADE-PLUS-GREEN](assets/fr/22.webp)

Green 显示您的设备是正品（“Your Jade is genuine”）。

![JADE-PLUS-GREEN](assets/fr/23.webp)

## 设置 PIN 码

点击 "*Continue*" 按钮，选择 Jade 的 PIN 码。

![JADE-PLUS-GREEN](assets/fr/24.webp)

PIN 码可以解锁您的 Jade。因此，它可以防止未经授权的访问。该 PIN 码与钱包加密密钥的生成过程无关。因此，即使无法获得 PIN 码，只要拥有 12 个单词的助记词，就可以重新获得比特币。我们建议选择一个随机的 PIN 码，并确保将该密码保存在与您的 Jade 存储位置不同的地方（如密码管理器中）。

选择 Jade 上的 6 位数 PIN 码，使用左右按钮选择数字，使用中间按钮确认数字的输入。

![JADE-PLUS-GREEN](assets/fr/25.webp)

再次确认 PIN 码。

![JADE-PLUS-GREEN](assets/fr/26.webp)

您的比特币钱包已创建。

![JADE-PLUS-GREEN](assets/fr/27.webp)

## 创建比特币账户

现在，您必须在您的钱包中创建一个账户。点击 "*Create an account*" 按钮。

![JADE-PLUS-GREEN](assets/fr/28.webp)

如果想创建普通的单签名钱包，请选择 "*Standard*"。

![JADE-PLUS-GREEN](assets/fr/29.webp)

为了了解与 "*2FA*" 选项有关的更多信息，请参阅本教程：

https://planb.academy/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

您的账户已创建。

![JADE-PLUS-GREEN](assets/fr/30.webp)

如果您想要个性化您的 Green 钱包，请点击右上方的三个小圆点。

![JADE-PLUS-GREEN](assets/fr/31.webp)

通过 "*Rename*"（重命名）选项，您可以自定义钱包的名称，这对在同一应用程序中管理多个钱包特别有用。通过 "*Unit*" 选单，您可以更改钱包的基本单位。例如，您可以选择以聪（Satoshi）单位而不是比特币计量单位显示余额。最后，"*Parameters*" 选单可以让您访问其他选项。例如，您可以在这里找到您的扩展公钥及其描述符，如果您打算从您的 Jade 中设置一个仅用于仅观察的钱包，这将非常有用。

![JADE-PLUS-GREEN](assets/fr/32.webp)

如果您想要在关闭 Jade 后重新连接，请按设备底部的开/关按钮。在 Green 应用程序中，从主页选择您的设备：

![JADE-PLUS-GREEN](assets/fr/33.webp)

然后输入 Jade 上的 PIN 码之后，您就可以重新连接了。

![JADE-PLUS-GREEN](assets/fr/34.webp)

您的 Jade 设备通过 Blockstream 的“虚拟安全元件”解锁（请参阅本教程的第一部分）。这需要通过蓝牙连接 Green 应用程序。如果在解锁过程中遇到蓝牙连接问题，请尝试断开并重新连接这两个设备。如果问题仍然存在，您仍然可以通过选择 “*QR Scan*” 选项并按照[Blockstream 网站](https://jadefw.blockstream.com/pinqr/index.html)上的说明来解锁您的 Jade 设备。

在您收到钱包中的第一笔比特币之前，**我非常建议您进行一次清空恢复测试**。记下一些参考信息，例如您的 xpub 或第一个接收地址，然后在 Green 应用程序和 Jade Plus 设备上清空您的钱包（`Options -> Device -> Factory Reset`）。然后尝试使用您之前记录的助记词纸质备份来恢复您的钱包。检查恢复后生成的 cookie 信息是否与您最初记录的信息一致。如果成功，您可以放心，您的纸质备份是可靠的。要了解更多关于如何进行测试恢复的信息，请参阅以下教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 接收比特币

现在您的比特币钱包已设置完毕，可以接收您的第一笔聪（sats）了！只需点击 Green 应用上的 “*Receive*” 按钮即可。

![JADE-PLUS-GREEN](assets/fr/35.webp)

Green 会显示一个接收地址，但在使用之前，务必在 Jade 设备上验证该地址是否属于您的钱包。为此，请点击 “*Verify on device*” 按钮。

![JADE-PLUS-GREEN](assets/fr/36.webp)

在 Jade 设备上确认地址与 Green 上的地址一致，然后点击按钮进行确认。

![JADE-PLUS-GREEN](assets/fr/37.webp)

现在您可以将此地址分享给付款人，以便接收比特币。交易广播到网络后，它将出现在您的钱包中。请等待收到足够的确认信息后再确认交易完成。

![JADE-PLUS-GREEN](assets/fr/38.webp)

## 发送比特币

钱包里有了比特币后，您现在就可以发送比特币了。点击 "*Send*"。

![JADE-PLUS-GREEN](assets/fr/39.webp)

在下一页，输入收款人的地址。您可以手动输入，也可以扫描二维码。

![JADE-PLUS-GREEN](assets/fr/40.webp)

选择付款金额。

![JADE-PLUS-GREEN](assets/fr/41.webp)

在屏幕底部，您可以选择本次交易的手续费。您可以选择按照应用程序的建议设置，也可以自定义手续费。相对于其他待处理交易，手续费越高，您的交易处理速度就越快。关于手续费市场信息，请访问 [Mempool.space](https://mempool.space/) 的 “*Transaction Fees*” 部分。

![JADE-PLUS-GREEN](assets/fr/42.webp)

点击 "*Next*" 进入交易详情页面。检查地址、金额和手续费是否正确。

![JADE-PLUS-GREEN](assets/fr/43.webp)

如果一切正确无误，将屏幕底部的绿色按钮向右滑动，即可在比特币网络上签名并广播交易。

![JADE-PLUS-GREEN](assets/fr/44.webp)

现在，您会被要求在 Jade 上确认交易。

![JADE-PLUS-GREEN](assets/fr/45.webp)

确保接收者地址正确。点击复选标记以确认。

![JADE-PLUS-GREEN](assets/fr/46.webp)

检查手续费金额是否正确，然后验证。

![JADE-PLUS-GREEN](assets/fr/47.webp)

您的交易已签名，并从 Green Wallet 通道传播出去。

![JADE-PLUS-GREEN](assets/fr/48.webp)

恭喜您，现在您已经知道如何通过蓝牙连接设置和使用 Jade Plus 与 Blockstream Green 移动应用程序。如果您觉得本教程有用，请在下方留下绿色拇指。欢迎在您的社交网络上分享本文。感谢您的分享！

如果您想要进一步前进，我向您推荐这篇关于 Jade Plus 的教程，我们将在二维码模式下使用 Sparrow Wallet 软件对其进行配置。您还将学习如何使用硬件钱包的高级设置：

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
