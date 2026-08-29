---
name: Passport Core
description: 手动配置和使用 Passport 硬件钱包
---
![cover](assets/cover.webp)

Passport 是一款仅支持比特币的硬件钱包，由 Foundation Devices 设计，该公司是一家美国公司，于 2020 年 4 月在波士顿成立。

本教程中介绍的 Passport “*Batch 2*” 是“*Founder's Edition*” 的升级版。它以其高端设计、高清彩色屏幕和符合人体工程学的实体键盘而著称。它采用“气隙”模式运行，确保您的钱包私钥完全隔离，可通过 MicroSD 卡或二维码进行通信。该设备配备一块可拆卸、可充电的诺基亚 BL-5C 电池，容量为 1200 mAh。由于 BL-5C 电池型号广泛，因此可以轻松更换。

💡 **更新：** 自2025年3月起，该硬件钱包不再称为 “Passport” 或 “Passport V2”，而是 “Passport Core”。

在连接方面，Passport 配备了 MicroSD 卡槽、用于充电的 USB-C 接口以及用于扫描二维码的后置摄像头。

在安全性方面，Passport 内置安全元件，并且其源代码完全开源。它具备一款优秀比特币硬件钱包应有的所有功能。需要注意的是，Passport 目前尚不支持 miniscript，但该功能计划于 2025 年第二季度推出。

Passport 的售价为 199 美元，定位为高端硬件钱包，与 Coldcard Q、Jade Plus、Tezor Safe 5 以及 Ledger 的顶级型号展开竞争。

![Image](assets/fr/01.webp)

您可以通过多种方式管理 Passport 上的安全钱包。这款硬件钱包兼容市面上大多数钱包管理软件，包括 Sparrow Wallet、Specter Desktop、Nunchuk 和 Keeper 等。在本教程中，我们将学习如何将 Passport 与 Sparrow Wallet 配合使用。

如果您是新手，最简单的选择是将 Passport 与 Foundation 开发的原生 Envoy 应用配合使用。要了解如何将 Envoy 与 Passport 配合使用，请查看以下教程：

https://planb.academy/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Passport 开箱

收到 Passport 后，请检查包装盒和纸箱上的封条是否完好无损，以确认包裹未被打开。设备设置过程中，系统还会进行软件验证，以确认设备的真实性和完整性。

![Image](assets/fr/02.webp)

盒内物品包括 ：


- 一台 Passport 硬件钱包；
- 一张纸板，用来写下您的助记词；
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

## 启动 Passport

按下设备侧面的电源键启动设备。

![Image](assets/fr/04.webp)

按确认按钮进入下一个选单。

![Image](assets/fr/05.webp)

在本教程中，我们将使用 Sparrow Wallet 管理 Passport 安全钱包。选择 "*Manual Setup*"。

![Image](assets/fr/06.webp)

然后接受使用条款。

![Image](assets/fr/07.webp)

下一步是检查您的设备。这将确认您的 Passport 的真实性，并确保其在运输过程中未被篡改。系统会提示您扫描二维码。

![Image](assets/fr/08.webp)

访问[官方验证网站](https://validate.foundationdevices.com/)，选择 "*Passport*"。

![Image](assets/fr/09.webp)

使用 Passport 的摄像头扫描网站上显示的二维码。

![Image](assets/fr/10.webp)

然后，设备将显示 4 个单词。

![Image](assets/fr/11.webp)

在网站上输入这些文字，确认Passport的真实性，然后点击 "*Validate*"（*验证*）。

![Image](assets/fr/12.webp)

如果出现 "*Passed" 信息，则说明您的硬件钱包是真实的。现在您就可以用它来保护比特币钱包了。

![Image](assets/fr/13.webp)

在 Passport 上确认检测结果。

![Image](assets/fr/14.webp)

## 设置 PIN 码

接下来是设置 PIN 码的步骤。PIN 码可以解锁您的 Passport。因此，它可以防止未经授权的物理访问。PIN 码与钱包加密密钥的生成无关。因此，即使无法获得 PIN 码，只要拥有 12 或 24 个单词的助记词，就能重新获得比特币。

![Image](assets/fr/15.webp)

我们建议选择一个尽可能随机的 PIN 码。此外，请务必将该密码保存在与您的 Passport 存储位置不同的地方（如密码管理器中）。

您可以选择 6 到 12 位数字的 PIN 码。我建议您尽量设置得长一些。

使用键盘输入密码。完成后，点击确认按钮。

![Image](assets/fr/16.webp)

再次确认 PIN 码。

![Image](assets/fr/17.webp)

您的 PIN 码已设置好。

![Image](assets/fr/18.webp)

## 更新 Passport 固件

您的硬件钱包建议您更新固件。我建议您立即更新，以受益于最新版本带来的改进和修复。如要继续，请单击右侧的确认按钮。

![Image](assets/fr/19.webp)

您的 Passport 已准备好通过 MicroSD 卡接收新固件。

![Image](assets/fr/20.webp)

为此，请使用 Passport 包装盒内附带的 MicroSD 卡（或其他卡），并将其插入您的计算机。请从[Foundation 官方文档网站](https://docs.foundation.xyz/firmware-updates/passport/)或[其 GitHub 代码库](https://github.com/Foundation-Devices/passport2/releases)下载最新固件版本。

![Image](assets/fr/21.webp)

在您的设备上安装之前，我们强烈建议您检查下载固件的真实性和完整性。如果您需要帮助，请参阅本教程 ：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

检查 `.bin` 文件后，将其放在 MicroSD 上，然后插入 Passport。Passport 文件资源管理器将打开。选择 `vN.N.N-passport.bin` 文件。

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

我们将创建一个新的比特币钱包。点击确认按钮。

![Image](assets/fr/27.webp)

为了创建新的钱包，请点击 "*Create New Seed*"。

![Image](assets/fr/28.webp)

您可以选择 12 或 24 个单词的助记词。这两个选项提供的安全性相似，因此您可以选择最容易保存的选项，即 12 个单词。

![Image](assets/fr/29.webp)

点击 "*Continue*"。

![Image](assets/fr/30.webp)

现在，您的 Passport 将生成您的 "*Backup Code*"（备份代码）。这是一串数字，可用于解密存储在 MicroSD 上的钱包备份。该备份系统是基金会设备特有的，是助记词额外的备份，但与其他比特币软件不兼容。

如果您决定使用此 "*Backup Code*"，请务必将其保存在与包含钱包加密备份的 MicroSD 不同的位置。不过，如果您认为有一个好的助记词备份就足够了，也可以选择不使用该系统。

![Image](assets/fr/31.webp)

输入 "*Backup Code*"，确认保存正确。

![Image](assets/fr/32.webp)

如果已插入 MicroSD，则已将钱包的加密备份保存在其中。

![Image](assets/fr/33.webp)

您的 Passport 将显示您的 12 个单词的助记词。此助记词赋予您对所有比特币的完全、无限制访问权限。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Passport。

如果您的 Passport 丢失、被盗或破损，这 12 个单词的助记词可以恢复您对比特币的访问。因此，小心保存Passport 并将其存放在安全的地方非常重要。

您可以将其写在盒子里提供的纸板上，或者为了更安全，我建议您将其刻在不锈钢底座上，以保护它免受火灾、洪水或倒塌的损害。

点击确认按钮即可查看您的助记词。

![Image](assets/fr/34.webp)

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，您绝不能像我在本教程中那样在互联网上分享这些助记词。此示例钱包仅用于测试网，并将在教程结束后删除。

请务必将此助记词备份到电脑上。

![Image](assets/fr/35.webp)

您的 Passport 已成功配置。点击确认按钮以继续。

![Image](assets/fr/36.webp)

## 选单探索

Passport 界面有三个主要选单：

- "*Account*"（账户）;
- "*More*"（更多）;
- "*Settings*（设置）"。

如果想在这些选单之间切换，请使用方向键上的左右箭头。

### *Account*" 选单

在 "*Account*" 选单中，您可以找到比特币钱包的主要功能。您可以通过摄像头或 MicroSD 卡槽签署交易。

![Image](assets/fr/37.webp)

*Account Tools*" 子选单提供了各种选项，如验证地址、信息交易签名或查询您的钱包中的地址。

![Image](assets/fr/38.webp)

在 "*Manage Account*" 子选单中，您可以将比特币钱包连接到钱包管理软件（我们将在本教程的后续步骤中介绍），或者查看和重命名您的账户。

![Image](assets/fr/39.webp)

### "More" 选单

在 "*More*" 选单中，您可以在钱包中创建一个与同一助记词关联的新账户。

![Image](assets/fr/40.webp)

您也可以输入 BIP39 Passphrase（密语，请见下一节）或使用临时种子。

![Image](assets/fr/41.webp)

### "Settings" 选单

在 "*Settings*" 选单中，您可以找到钱包和设备的所有设置。

![Image](assets/fr/42.webp)

"*Device*" 子选单提供了自定义屏幕亮度、设置自动锁定前的延迟、更改 PIN 码或重命名设备等选项。

![Image](assets/fr/43.webp)

"*Backup*" 子选单允许您导出加密钱包备份、检查现有备份的有效性或再次查找您的“备份代码”。

![Image](assets/fr/44.webp)

“*Firmware*” 子选单用于更新 Passport 的固件。我们建议您定期进行这些更新，以便享受最新的修复和功能。

![Image](assets/fr/45.webp)

通过 "*Bitcoin*" 子选单，您可以更改显示的单位（比特币或聪），管理多签名钱包，或切换到 "*Testnet*" 模式。

![Image](assets/fr/46.webp)

在 "*Advanced*" 中，您可以查看助记词，对插入的 MicroSD 卡执行操作，将 Passport 重置为出厂设置，或执行真伪验证（如之前所述）。

![Image](assets/fr/47.webp)

您可以启用 “*Security Words*” 功能，该功能会在您输入 PIN 码前四位后解锁设备时显示两个特定的单词，从而增加一层安全保障。这两个单词需要在配置过程中保存，以确保 Passport 设备未被更换或篡改。如果日后出现任何异常情况，我们建议您不要使用该设备。我建议您启用此选项，以防止设备遭受物理损坏的大部分风险。

![Image](assets/fr/48.webp)

最后，"*Extensions*" 子选单可让您激活设备特定用途的功能，如 Whirlpool（一种混币交易的协议）。

![Image](assets/fr/49.webp)

## 添加 BIP39 Passphrase（密语）

继续操作之前，如果您愿意，可以添加一个 BIP39 密语。 BIP39 密语是一个可选密码，您可以自由选择，它会被添加到您的助记词中，以增强钱包安全性。启用此功能后，访问您的比特币钱包需要同时输入助记词和密语。缺少其中任何一个，都将无法恢复相关的钱包。

在 Passport 上配置此选项之前，强烈建议您阅读以下文章，以充分了解密码短语的理论操作，并避免可能导致比特币丢失的错误：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

为了激活它，请进入 "*More*" 选单并点击 "*Enter Passphrase*"。

![Image](assets/fr/50.webp)

使用 aA1 键盘输入您的密语，并确保将其保存在纸质或金属介质上至少一次。示例中我使用的是一个非常弱的密语，但您应该选择一个强的密语，包含所有字符类型，并且长度足够（类似于强密码一样）。

![Image](assets/fr/51.webp)

请注意，BIP39 密语区分大小写和拼写错误。如果您输入的密码短语与初始配置的略有不同，Passport 不会报告错误，但会生成另一组加密密钥，该密钥将与您初始钱包中的密钥不同。

因此，在配置时，务必记下下一步将获得的密钥指纹。例如，我的密语是 `Plan ₿ Academy`，对应的密钥指纹为 `745D526B`。

![Image](assets/fr/52.webp)

每次解锁 Passport 时，您都需要返回此选单输入密码并将其应用到您的钱包。Passport 不会保存您的密语。

每次解锁后，记下密语后，请在此确认屏幕上检查生成的指纹是否与您在配置过程中记下的指纹相同。如果相同，则说明您的密语正确，并且您正在访问正确的比特币钱包。如果不同，则说明您访问的钱包有误，需要重试，并注意不要输入错误。

在您的钱包收到第一批比特币之前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，例如您的 xpub 或第一个接收地址，然后在 Passport 钱包仍为空时将其删除（`Settings -> Advanced -> Erase Passport`）。然后尝试使用您之前备份的助记词和密语来恢复钱包。检查恢复后生成的 cookie 信息是否与您最初记录的信息一致。如果一致，则可以确定您的纸质备份是可靠的。要了解更多关于如何进行测试恢复的信息，请参阅以下教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## 在 Sparrow Wallet 上配置钱包

在本教程中，我将向您展示如何将 Passport 高级地与 Sparrow Wallet 结合使用。不过，这款硬件钱包也兼容 Envoy（Foundation 应用程序）、Keeper、BlueWallet、Nunchuk、Specter 以及许多其他钱包。

首先，如果您尚未安装 Sparrow Wallet，请从[官方网站](https://sparrowwallet.com/)下载并安装到您的计算机上。

![Image](assets/fr/54.webp)

安装前，请务必检查软件的真实性和完整性。如果您不知道如何操作，请参阅此教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

打开 Sparrow Wallet 后，点击 “*Files*” 选项卡，然后点击 “*New Wallet*”。

![Image](assets/fr/55.webp)

为钱包命名，然后点击 "*New Wallet*"。

![Image](assets/fr/56.webp)

选择 "*Airgapped Hardware Wallet*"。

![Image](assets/fr/57.webp)

点击 "*Passport*" 选项旁边的 "*Scan...*"。这将打开您的网络摄像头。

![Image](assets/fr/58.webp)

在硬件钱包上，前往 "*Account*" 选单，选择 "*Manage Account*" 子选单，然后点击 "*Connect Wallet*"。

![Image](assets/fr/59.webp)

在出现的下拉列表中，选择 "*Sparrow*"。

![Image](assets/fr/60.webp)

然后选择 "*Single-sig*"（*单签名钱包*），进行不带多密码的正常配置。

![Image](assets/fr/61.webp)

选择 "*QR Code*" 选项。

![Image](assets/fr/62.webp)

然后，您的 Passport 将生成动态二维码。使用电脑摄像头将它们扫描到 Sparrow 软件中。

![Image](assets/fr/63.webp)

现在您应该可以看到您的 xpub 和主密钥指纹，它们应该与您输入密码时在 Passport 上显示的指纹一致。点击 "*Apply*" 按钮。

![Image](assets/fr/64.webp)

设置一个强密码来保护您的 Sparrow 钱包。此密码将保护您的公钥、地址、标签和交易记录免受未经授权的访问。建议您将此密码保存在密码管理器中，以免忘记。

![Image](assets/fr/65.webp)

然后，您的 Passport 会提示您扫描第一个接收地址，以确认导入成功。

![Image](assets/fr/66.webp)

在 Sparrow 中，前往 "*Receive*" 选项卡，扫描第一个地址的二维码。

![Image](assets/fr/67.webp)

如果操作成功，您的 Passport 将显示 "*Verified*"。

![Image](assets/fr/68.webp)

这表明导入成功。

![Image](assets/fr/69.webp)

## 接收比特币

现在您的 Passport 已设置完毕，您可以开始在新比特币钱包中接收比特币了。为此，请在 Sparrow 中点击 “*Receive*” 选单。

![Image](assets/fr/70.webp)

Sparrow 将显示您钱包中的第一个空白收款地址。您可以添加标签。

![Image](assets/fr/71.webp)

使用前，我们将在 Passport 屏幕上检查该地址，以确保它属于您的比特币钱包。在 Sparrow 钱包中，您可以根据需要点击放大地址的二维码。在 Passport 的 “Account” 选单中，选择 “Account Tools”。

![Image](assets/fr/72.webp)

点击 "*Verify Address*"，然后扫描 Sparrow Wallet 上显示的二维码。

![Image](assets/fr/73.webp)

确保 Passport 上显示与 Sparrow 上显示的地址完全一致，并显示 "*Verified*"。

![Image](assets/fr/74.webp)

现在您可以使用它来接收比特币。当交易在网络上广播后，它将出现在 Sparrow 中。请等待收到足够的确认，以确保交易最终完成。

![Image](assets/fr/75.webp)

## 发送比特币

现在您的钱包里有一些聪（sats），您也可以发送一些比特币。为此，请点击 “*UTXO*” 选单。

![Image](assets/fr/76.webp)

选择您要用作此交易输入的 UTXO，然后点击 “*Send Selected*”。

![Image](assets/fr/77.webp)

输入接收者的地址、用于提醒您交易用途的标签以及您要发送到该地址的金额。

![Image](assets/fr/78.webp)

根据当前市场情况调整收费率，然后点击 "*Create Transaction*"。

![Image](assets/fr/79.webp)

检查所有交易参数是否正确，然后点击 "*Finalize Transaction for Signing*"。

![Image](assets/fr/80.webp)

点击 “*Show QR*” 以显示 PSBT（部分签名比特币交易）。Sparrow 已创建交易，但仍缺少解锁输入比特币所需的签名。这些签名只能由 Passport 执行，Passport 存储着您的种子，并提供签署交易所需的私钥。

![Image](assets/fr/81.webp)

在 Passport 上前往 "*Account*" 选单，点击 "*Sign with QR Code*"。

![Image](assets/fr/82.webp)

扫描 Sparrow 钱包中显示的 PSBT（部分签名比特币交易）。

![Image](assets/fr/83.webp)

确认接收地址和发送金额正确，然后点击确认按钮。

![Image](assets/fr/84.webp)

检查兑换地址。在我的示例中，由于交易仅包含一个输出，因此没有兑换地址。

![Image](assets/fr/85.webp)

确保手续费是您选择的金额。

![Image](assets/fr/86.webp)

如果所有信息都正确，请点击确认按钮签名交易。

![Image](assets/fr/87.webp)

在 Sparrow Wallet 中，点击 “*Scan QR*”，然后扫描您钱包地址栏中显示的二维码。

![Image](assets/fr/88.webp)

您已签名的交易现已准备好在比特币网络上广播，并由矿工放入到区块中。如果一切正确，请点击 “*Broadcast Transaction*”。

![Image](assets/fr/89.webp)

您的交易已被广播，正在等待确认。

![Image](assets/fr/90.webp)

恭喜！您现在已经了解如何配置和使用 Passport。如果您觉得本教程有用，请在下方点赞。欢迎在您的社交网络上分享这篇文章。感谢分享！

为了解更多信息，请参阅我们关于 Liana 软件的教程：

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
