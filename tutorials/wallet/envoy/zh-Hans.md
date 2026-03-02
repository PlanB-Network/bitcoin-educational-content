---
name: Envoy
description: 在 Envoy 应用程序中设置和使用 Passport 钱包
---
![cover](assets/cover.webp)

Envoy 是 Foundation 开发的比特币钱包管理应用程序。它专为与 Passport 硬件钱包配合使用而设计。

本教程中与 Envoy 应用程序一起提供的 Passport “*Batch 2*” 是 "*Founder's Edition*" 的后续版本。它以其优质的设计、高清彩色屏幕和符合人体工程学的物理键盘而脱颖而出。它以“*Air-Gap*”（空气隔离）模式运行，确保您钱包的私钥保持完全隔离，并可通过 MicroSD 卡或二维码进行通信。该设备配备可拆卸、可充电的诺基亚 BL-5C 电池，容量为 1200 mAh。这种非专有电池可以轻松更换，因为 BL-5C 型号在商店中随处可见。

在连接性方面，Passport 配备了 MicroSD 端口、用于充电的 USB-C 端口以及用于扫描二维码的后置摄像头。

在安全性方面，Passport 集成了安全元件，并且设备的源代码完全开源。它提供了优秀比特币硬件钱包所需的所有功能。请注意，Passport 尚不支持 miniscript，但计划于 2025 年第二季度推出此功能。

Passport 售价 199 美元，定位高端硬件钱包，与 Coldcard Q、Jade Plus、Tezor Safe 5 和 Ledger 的顶级型号竞争。

![Image](assets/fr/01.webp)

为了在 Passport 上管理安全钱包，您有多种选择。这种硬件钱包与市场上大多数钱包管理软件兼容，包括 Sparrow Wallet、Specter Desktop、Nunchuk 和 Keeper 等。

本教程面向初级和中级用户，我们将介绍如何在 Passport 上使用 Envoy 应用程序。这是充分利用硬件钱包的最简单方法。

如果您是高级用户并且想要探索更复杂的功能，我建议您查看我们使用 Sparrow Wallet 配置 Passport 的其他教程：

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## 拆箱 Passport

当您收到护照时，请确保盒子和纸箱上的封条完好无损，以确认包裹未被打开。设置时还将对设备的真实性和完整性进行软件验证。

![Image](assets/fr/02.webp)

盒内物品包括 ：

- Passport 钱包；
- 一张纸板，用来写下您的记忆短语；
- 用于充电的 USB-C 连接线；
- MicroSD 卡 ；
- 两个 MicroSD 转 Lightning 或 USB-C 适配器；
- 贴纸

在设备上，您可以找到 ：

- 键盘 (1) ；
- USB-C 端口 (2)；
- 删除按钮 (3)；
- 返回按钮 (4) ；
- 确认按钮 (5)；
- 方向垫 (6)；
- 开/关按钮 (7)；
- 状态指示灯 (8)；
- MicroSD 接口 (9) ；
- 用于切换模式 aA1 的按钮 (10) ；
- 后置摄像头

![Image](assets/fr/03.webp)

## 下载 Envoy 应用程序

前往应用程序商店下载 Envoy ：

- 在 [Google Play 商店](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy)；
- 在 [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818)；
- 在 [F-Cold](https://foundation.xyz/fdroid/) 上。

![Image](assets/fr/50.webp)

您也可以直接[从 Foundation 的 GitHub 代码库](https://github.com/Foundation-Devices/envoy/releases) 下载 APK 文件。

![Image](assets/fr/51.webp)

打开应用程序后，选择 "*Manage Passport*"。

![Image](assets/fr/52.webp)

选择是否要激活 Tor 连接以加强保密性，然后按 "*Continue*"。

![Image](assets/fr/53.webp)

如果您的 Passport 已配置，请选择“*Connect an existing Passport*”；如果您首次初始化硬件钱包，请选择 “*Set up a new Passport*”。

![Image](assets/fr/54.webp)

接受使用条款。

![Image](assets/fr/55.webp)

然后您将被要求验证 Passport 的真实性。点击 “*Next*”。

![Image](assets/fr/56.webp)

## 启动护照

按设备侧面的开/关按钮将其启动。

![Image](assets/fr/04.webp)

按确认按钮进入下一个选单。

![Image](assets/fr/05.webp)

在本教程中，我们将使用 Envoy 来管理 Passport 保护的钱包。选择 "*Envoy App*"。

![Image](assets/fr/57.webp)

点击 "*Continue on Envoy*"。

![Image](assets/fr/58.webp)

下一步是检查您的设备。这可以确认您 Passport 的真实性，并确保其在运输过程中没有被篡改。系统会要求您扫描二维码。

![Image](assets/fr/08.webp)

使用您的 Passport 扫描应用程序中显示的动态二维码。扫描完成后，点击 "*Next*"。

![Image](assets/fr/59.webp)

然后用手机扫描 Passport 上显示的二维码。

![Image](assets/fr/60.webp)

如果出现 "*Your Passport is secure*" 信息，这就证明您的硬件钱包是真实的。现在您就可以用它来保护比特币钱包了。

![Image](assets/fr/61.webp)

在 Passport 上确认检测结果。

![Image](assets/fr/14.webp)

## 设置 PIN 码

接下来是 PIN 码步骤。PIN 码可解锁您的 Passport。因此，它可以防止未经授权的访问。PIN 码与钱包加密密钥的派生过程无关。因此，即使无法访问 PIN 码，拥有 12 或 24 个单词的助记词也能让您重新获得比特币。

![Image](assets/fr/15.webp)

我们建议选择尽可能随机的 PIN 码。另外，请务必将此代码保存在与您的 Passport 存储位置不同的位置（例如密码管理器中）。

您可以选择 6 到 12 位数字的 PIN 码。我建议您尽量设置得长一些。

使用键盘输入密码。完成后，点击确认按钮。

![Image](assets/fr/16.webp)

再次确认所输入的 PIN 码。

![Image](assets/fr/17.webp)

您的 PIN 码已注册。

![Image](assets/fr/18.webp)

## 更新 Passport 固件

您的硬件钱包建议您更新其固件。我建议您立即更新，以受益于最新版本带来的改进和修复。请单击右侧的确认按钮以继续。

![Image](assets/fr/19.webp)

您的 Passport 已准备好通过 MicroSD 卡接收新固件。

![Image](assets/fr/20.webp)

### 没有 Envoy 应用程序

为此，请使用 Passport 盒（或其他卡）中包含的 MicroSD 卡，并将其插入计算机。从 [基金会文档站点](https://docs.foundation.xyz/firmware-updates/passport/) 或 [其 GitHub 存储库](https://github.com/Foundation-Devices/passport2/releases) 下载最新固件版本。

![Image](assets/fr/21.webp)

在将其安装到您的设备上之前，我们强烈建议您检查下载的固件的真实性和完整性。如果您需要这方面的帮助，请参阅本教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 使用 Envoy 应用程序

另一种更简单的选择是直接使用 Envoy 应用程序。点击 "*Download Firmware*"。

![Image](assets/fr/62.webp)

使用 Passport 随附的适配器将 MicroSD 卡连接到您的手机。

![Image](assets/fr/63.webp)

在文件资源管理器中选择 MicroSD 卡来保存固件。

![Image](assets/fr/64.webp)

固件现已保存。从智能手机中取出 MicroSD 并将其插入 Passport。

![Image](assets/fr/65.webp)

Passport 文件资源管理器将打开。选择 `vN.N.N-passport.bin` 文件。

![Image](assets/fr/22.webp)

点击 "*Select*"。

![Image](assets/fr/23.webp)

然后确认固件安装。

![Image](assets/fr/24.webp)

请等待更新完成。

![Image](assets/fr/25.webp)

更新完成后，输入 PIN 码解锁设备并继续配置。

![Image](assets/fr/26.webp)

## 创建一个新的比特币钱包

现在我们会创建一个新的比特币钱包了。点击确认按钮。

![Image](assets/fr/27.webp)

为了创建新的钱包，请点击 "*Create New Seed*"。

![Image](assets/fr/28.webp)

您可以选择 12 个字或 24 个单词的助记词。这两个选项提供的安全性相似，因此您可以选择最容易保存的选项，即 12 个单词。

![Image](assets/fr/29.webp)

点击 "*Continue*"。

![Image](assets/fr/30.webp)

现在，您的 Passport 将生成您的 "*Backup Code*"。这是一系列数字，可用于解密存储在 MicroSD 上的钱包备份。该备份系统特定于基金会设备，构成助记词的额外备份，但与其他比特币软件不兼容。

如果您决定使用此 "*Backup Code*"，请务必将其保存在与包含钱包加密备份的 MicroSD 不同的位置。不过，如果您认为有一个好的助记词备份就足够了，也可以选择不使用该系统。

![Image](assets/fr/31.webp)

输入 "*Backup Code*"，确认保存正确。

![Image](assets/fr/32.webp)

如果已插入 MicroSD，则已将钱包的加密备份保存在其中。

![Image](assets/fr/33.webp)

您的 Passport 将显示您的 12 单词的助记词。有了这个助记词，您就可以完全不受限制地使用您的所有比特币。任何拥有这个助记词的人都可以盗取您的资金，即使没有您 Passport 的物理访问权限。

如果您的护照丢失、被盗或破损，这 12 个字的助记词可以恢复您对比特币的访问。因此，小心保存护照并将其存放在安全的地方非常重要。

您可以在包装盒内提供的纸板上书写，或者为了提高安全性，我建议您将其刻在不锈钢底座上，以防火灾、水灾或倒塌。

点击确认按钮，查看您的记忆短语。

![Image](assets/fr/34.webp)

关于保存和管理助记词的正确方法的更多信息，我强烈推荐大家阅读另一篇教程，特别是如果您是初学者：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，您绝不能像我在本教程中所做的那样在互联网上分享这些单词。该示例钱包仅在测试网上使用，并将在教程结束时删除。

请为该助记词进行物理备份。

![Image](assets/fr/35.webp)

您的 Passport 已成功配置。单击确认按钮继续。

![Image](assets/fr/36.webp)

## 在 Envoy 上设置钱包

在本教程中，我将向您展示如何将 Passport 与 Envoy 应用程序一起使用。然而，这款硬件钱包还与 Sparrow Wallet、Keeper、BlueWallet、Nunchuk、Spectre 等许多钱包兼容......

![Image](assets/fr/66.webp)

使用 Envoy 应用程序扫描 Passport 上显示的二维码。

![Image](assets/fr/67.webp)

您的公钥现已导入到应用程序中。点击 "*Validate receive address*"。

![Image](assets/fr/68.webp)

使用 Passport 扫描 Envoy 上显示的地址。

![Image](assets/fr/69.webp)

您的护照将确认在 Envoy 上导入的钱包是否有效。请在应用程序中确认。

![Image](assets/fr/70.webp)

现在您可以在 Envoy 上访问钱包的公开信息，但要花比特币，您需要使用您的 Passport。

![Image](assets/fr/71.webp)

## 了解 Passport 选单

Passport 界面有三个主要选单：


- "*Account*"（账户）；
- "*More*"（更多）；
- "*Settings*"（设置）。

为了了解这些选单，请使用方向盘上的左右箭头。

### “*Account*" 选单

在 “*Account*" 选单中，您可以找到比特币钱包的主要功能。您可以通过摄像头或 MicroSD 端口签署交易。

![Image](assets/fr/37.webp)

“*Account Tools*” 子选单提供诸如验证地址、签署消息或查询钱包中的地址等选项。

![Image](assets/fr/38.webp)

在 "*Manage Account*" 子选单中，您可以将比特币钱包连接到钱包管理软件（我们将在本教程的下一步介绍），或者查看和重命名您的账户。

![Image](assets/fr/39.webp)

### “More” 选单

在 “More” 选单中，您可以在钱包中创建一个新帐户，链接到相同的助记词。

![Image](assets/fr/40.webp)

您还可以输入 BIP39 Passphrase（密语）或使用临时种子。

![Image](assets/fr/41.webp)

### “Settings” 选单

在 "“Settings”" 选单中，您可以找到钱包和设备的所有设置。

![Image](assets/fr/42.webp)

"*Device*" 子选单为您提供自定义屏幕亮度、设置自动锁定前的延迟、更改 PIN 码或重命名设备的选项。

![Image](assets/fr/43.webp)

“*Backup*” 子选单可让您导出加密钱包备份、检查现有备份的有效性，或再次查找 “*Backup Code*"。

![Image](assets/fr/44.webp)

“*Firmware*” 子选单用于更新 Passport 的固件。我们建议您定期进行这些更新，以便从最新的修复和功能中获益。

![Image](assets/fr/45.webp)

通过 "*Bitcoin*" 子选单，您可以更改显示的单位（BTC 或 satoshis），管理可能的多签名钱包，或切换到 "*Testnet*" 模式。

![Image](assets/fr/46.webp)

在 "*Advanced*" 中，您可以查看助记词的单词，对插入的 MicroSD 执行操作，将 Passport 重置为出厂设置，或执行先前执行的真实性检查。

![Image](assets/fr/47.webp)

您可以激活 "*Security Words*"，该功能可在输入 PIN 码的前四位数字后解锁设备时显示两个特定的词，从而增加一层安全性。这些文字将在配置时保存，以确保 Passport 未被更换或篡改。如果日后出现任何不一致的情况，我们建议您不要使用该设备。我建议您激活此选项，以防止设备受到物理破坏的大部分风险。

![Image](assets/fr/48.webp)

最后，"*Extensions*" 子选单可让您激活设备特定用途的功能，如 Whirlpool 或 Coinjoin（混币）协议。

![Image](assets/fr/49.webp)

## 接收比特币

现在您的 Passport 已设置完毕，您已准备好在新的比特币钱包中接收您的第一个比特币。为此，请在 Envoy 上点击您的 “*Primary 0*” 账户。

![Image](assets/fr/72.webp)

点击 "*Receive*" 按钮。

![Image](assets/fr/73.webp)

您的 Envoy 应用程序会显示您钱包上第一个可用的空白地址。在使用它之前，让我们检查 Passport 屏幕上的地址，以确保它确实属于我们的比特币钱包。在 Passport 的 "*Account*" 选单中，选择 "*Account Tools*"。

![Image](assets/fr/74.webp)

点击 "*Verify Address*"，然后扫描 Envoy 上显示的二维码。

![Image](assets/fr/75.webp)

确保护照上显示的地址与 Sparrow 上显示的地址完全一致，并显示 "*Verified*"。

![Image](assets/fr/76.webp)

您现在可以使用它来接收比特币。当交易在网络上广播时，它将出现在 Envoy 上。等到您收到足够的确认后才能认为交易已确定。

![Image](assets/fr/77.webp)

## 发送比特币

既然您的钱包里有一些比特币，您也可以发送一些。为此，请单击 “*Send*” 按钮。

![Image](assets/fr/78.webp)

输入接收者地址，可以直接粘贴，也可以用智能手机摄像头扫描二维码。

![Image](assets/fr/79.webp)

确定要发送的金额，然后点击 "*Confirm*"。

![Image](assets/fr/80.webp)

根据当前市场情况选择交易费用，然后查看交易信息。如果一切正确，请单击 “*Sign with Passport*”。

![Image](assets/fr/81.webp)

在交易上添加标签，以便清楚记录交易目的。

![Image](assets/fr/82.webp)

然后，Envoy 显示 PSBT（*部分签名的比特币交易*）。应用程序已经构建了交易，但仍然缺少解锁输入中使用的比特币的签名。这些签名只能由 Passport 执行，Passport 托管您的种子，可以访问签署交易所需的私钥。

![Image](assets/fr/83.webp)

在护照上进入 "*Account*" 选单，点击 "*Sign with QR Code*"。

![Image](assets/fr/84.webp)

扫描 Envoy 上显示的 PSBT（*部分签名比特币交易*）。

![Image](assets/fr/85.webp)

确认接收地址和发送金额无误，然后按确认按钮。

![Image](assets/fr/86.webp)

检查兑换地址。在我的示例中，没有，因为交易包含单个输出。

![Image](assets/fr/87.webp)

确保费用是您选择的费用。

![Image](assets/fr/88.webp)

如果所有信息都正确无误，请点击确认按钮以签名交易。

![Image](assets/fr/89.webp)

您的 Passport 会以二维码的形式显示您已签名的交易。

![Image](assets/fr/90.webp)

在 Enjoy 应用程序中，点击二维码图标，然后扫描 Passport 屏幕上显示的 PSBT。

![Image](assets/fr/91.webp)

最后检查一次交易细节。如果一切无误，按 "*Send Transaction*" 在比特币网络上广播。

![Image](assets/fr/92.webp)

您的交易正在等待确认。您可以直接从账户中查看交易状态。

![Image](assets/fr/93.webp)

恭喜您，现在您已经知道如何在 Envoy 应用程序中设置和使用 Passport 了。如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。感谢您的分享！

如需了解更多信息，请参阅我们的 Liana 软件教程：

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
