---
name: Jade Plus - Sparrow
description: 配备 Sparrow Wallet 的 Jade Plus 的高级配置
---
![cover](assets/cover.webp)

Jade Plus 是 Blockstream 设计的一款仅支持比特币的硬件钱包。它是普通 Jade 的升级版，在软件方面进行了改进，增加了更多功能，并重新设计了符合人体工程学的外形，使其使用起来更加直观。这款新版本配备了一块出色的 1.9 英寸 LCD 屏幕，色域比上一代产品更广。按键和选单导航也得到了优化。

Jade Plus 的使用方式多种多样：可通过 USB-C 有线连接，也可使用 micro SD 卡的 “空气隔离” 模式（需要适配器），还可通过蓝牙连接，甚至可以借助内置摄像头交换二维码。这款硬件钱包采用电池供电。

基础黑色版售价 149.99 美元起，而 "*Genesis Grey*" 或 "*Lunar Silver*" 版本的价格最高可在此基础上增加 20 美元。因此，Jade Plus 是一个不错的选择，它拥有媲美 Coldcard Q 或 Passport V2 等高端硬件钱包的先进功能，但价格却相当低廉，接近中端机型。

![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

在本教程中，我们将使用桌面版 Sparrow Wallet 软件，在二维码模式下设置 Jade Plus 的高级配置。此配置非常适合中级或经验丰富的用户。如果您正在寻找更简单的入门方法，我建议您查看以下教程，其中我们使用 Jade Plus 通过蓝牙连接 Green Wallet：

https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Jade Plus 安全模式

Jade Plus 安全模型

Jade Plus 使用基于 “虚拟安全元件”（virtual secure element）的安全模型，该元件由 “盲断言机”（blind oracle）实现。具体来说，该机制结合了用户选择的 PIN 码、Jade 上存储的密钥以及盲断言（由 Blockstream 维护的服务器）持有的密钥，生成一个分布在两个实体上的 AES-256 密钥。在初始化过程中，ECDH 交易所会确保与预言机的通信安全，并对硬件钱包上的恢复助记词进行加密。实际上，当您需要访问种子以签署交易时，您需要访问：

- Jade Plus 设备本身；
- 用于解锁设备的 PIN 码；
- 以及断言机的密钥。

这种方法的主要优势在于硬件层面不存在单点故障，因为即使攻击者获得了您的 Jade 设备，提取密钥也需要同时攻破 Jade 设备和断言机。此外，该模型还意味着 Jade Plus 完全开源，避免了使用真正物理安全元件（例如 Ledger 所使用的元件）所带来的限制。

该系统的缺点是 Jade Plus 的使用依赖于 Blockstream 维护的断言机。如果该断言机无法访问，则无法再使用 PIN 码直接操作硬件钱包。然而，这并不意味着您的比特币就此丢失，因为您仍然可以使用助记词找回它们。您可以在 Jade Plus 的 “无状态”（stateless）模式下输入助记词。为了绕过这种依赖性，您还可以配置和管理自己的断言机服务器。

管理助记词的另一种方法是不要将其注册到 Jade Plus 上。在这种情况下，Jade 就仅作为签名设备使用。在初始化过程中，除了像往常一样将助记词保存为单词之外，您还需要将其保存为手动生成的二维码。这样，每次使用钱包时，您都可以使用 Jade 的摄像头导入助记词。对于高级用户来说，这可能是一个不错的选择，具体取决于您的安全策略。但您需要谨慎地保存和保护您的助记词，因为即使是二维码，也可能让任何人窃取您的资金。我们将在本教程中介绍此选项，但这并非强制性的。

## Jade Plus 开箱

当您收到 Jade Plus 时，请检查包装盒和封条是否完好，以确保您的包裹没有被打开过。

![JADE-PLUS-SPARROW](assets/fr/02.webp)

盒子里有 ：


- Le Jade Plus；
- USB-C 电缆；
- 以单词或 "*CompactSeedQR*" 的形式记录助记词的卡片；
- 一些使用说明 ；
- 一条绳索
- 一些贴纸

![JADE-PLUS-SPARROW](assets/fr/03.webp)

该设备有 4 个导航按钮：

- 右下角的按钮可以打开 Jade；
- 设备正面的大按钮用于选择项目；
- 顶部的两个小按钮可以让您向左和向右导航；
- 您还可以同时点击设备顶部的两个按钮来选择项目。

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## 设置新的比特币钱包

点击开始按钮。

![JADE-PLUS-SPARROW](assets/fr/05.webp)

点击 "*Setup Jade*"。

![JADE-PLUS-SPARROW](assets/fr/06.webp)

选择 "*Advanced Setup*"。

![Image](assets/fr/07.webp)

然后点击 "*Create a New Wallet*" 以生成新种子。您可以选择 12 个单词或 24 个单词的助记词。两种选择的钱包安全性是相同的，因此选择最简单的保存选项（即 12 个单词）可能更方便。

![Image](assets/fr/08.webp)

点击 "*继续*"按钮，显示新的恢复短语。

![Image](assets/fr/09.webp)

您的 Jade Plus 上会显示您的 12 个单词的助记词。**此助记词可让您完全无限制地访问您的所有比特币。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Jade Plus。如果您的 Jade 丢失、被盗或损坏，这 12 个单词的助记词可帮助您恢复对比特币的访问权限。因此，请务必妥善保管此助记词并将其存放在安全的地方。**

您可以将其写在包装盒内提供的纸板上，或者为了更加安全，我建议您将其刻在不锈钢底座上，以保护其免受火灾、洪水或跌落的损害。

![Image](assets/fr/10.webp)

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，您绝不能像我在本教程中那样在互联网上分享这些助记词。此示例钱包仅用于测试网，并将在教程结束后删除。

点击屏幕右侧的箭头以显示以下助记词。

![Image](assets/fr/11.webp)

保存助记词后，Jade Plus 会要求您确认。使用设备顶部的按钮，按顺序选择正确的单词，然后点击中间的按钮进入下一个单词。

![Image](assets/fr/12.webp)

然后您有两个选择。如介绍中所述，您可以选择将种子直接保存在设备上，然后使用 Blockstream 的 "*虚拟安全元素*"（"*Virtual Secure Element*"）保护系统访问您的钱包（选项 1）；或者将种子保存为二维码，每次使用时扫描一下（选项 2）。

对于选项 1，请选择 “No”，对于选项 2，请选择 “Yes”。

![Image](assets/fr/13.webp)

### 选项 1：二维码 PIN 码解锁

如果您选择了选项 1（CompactSeedQR：“No“），您将直接进入连接方式选择页面。在本教程中，我们将通过二维码交换在 Air-Gap 模式下使用设备，因此请选择“*QR*”。

![Image](assets/fr/27.webp)

点击 “*Continue*”。

![Image](assets/fr/28.webp)

PIN 码用于解锁您的 Jade 设备，并防止未经授权的物理访问。此 PIN 码不与生成您钱包的加密密钥无关。因此，即使无法获取此 PIN 码，只要拥有您的 12 个单词的助记词，即可重新访问您的比特币。我们建议您选择尽可能随机的 PIN 码。此外，请确保将此代码保存在与 Jade 设备不同的位置，例如密码管理器中。

在您的 Jade 设备上选择一个 6 位数的 PIN 码，使用左右按钮滚动选择数字，并使用中间按钮确认每个数字。

![Image](assets/fr/29.webp)

再次确认 PIN 码。

![Image](assets/fr/30.webp)

如前言所述，您的种子将加密存储在 Jade Plus 中。为了解密种子，您必须提供文件：

- 有效的 PIN 码（我们刚刚设置的） ；
- Blockstream 维护的断言机秘密。

在本高级教程中，我们将使用 Sparrow Wallet 来管理我们的比特币钱包。但是，与 Blockstream 的 Green Wallet 软件不同，Sparrow 无法访问 Blockstream 服务器上的断言机。因此，每次解锁 Jade Plus 时，我们都需要使用 Blockstream 的网站来获取断言机密钥。

访问 https://jadefw.blockstream.com/pinqr/index.html

点击 "*Start QR Unlock*"。

![Image](assets/fr/31.webp)

点击 "*Done*"，因为您已经在 Jade Plus 上选择了密码。

![Image](assets/fr/32.webp)

使用电脑摄像头扫描 Jade 屏幕上显示的二维码。

![Image](assets/fr/33.webp)

在 Jade 上确认，进入下一个屏幕。

![Image](assets/fr/34.webp)

扫描网站上的二维码，以获取断言机的秘密。

![Image](assets/fr/35.webp)

现在您的钱包已经创建，您可以继续下一步，跳过 "*选项 2：CompactSeedQR*" 部分。

![Image](assets/fr/36.webp)

每次启动时，点击 "*QR Mode*"。

![Image](assets/fr/37.webp)

选择 "*QR PIN Unlock*"。

![Image](assets/fr/38.webp)

输入您的 PIN 码。

![Image](assets/fr/39.webp)

然后访问 [Blockstream 网站](https://jadefw.blockstream.com/pinqr/qrpin.html) 与断言机交换二维码。

![Image](assets/fr/40.webp)

您的 Jade 现在已解锁。

![Image](assets/fr/41.webp)

### 选项 2：CompactSeedQR

如果您选择了选项 2（CompactSeedQR："*Yes*"），请再次点击 "*Yes*"。

![Image](assets/fr/14.webp)

点击 "*Start*"。

![Image](assets/fr/15.webp)

您可以使用 Jade Plus 包装盒中提供的二维码底座。根据您选择的 12 个或 24 个单词的助记词，选择相应的方框。您还可以[从 Blockstream 网站打印模板](https://help.blockstream.com/hc/article_attachments/41928319071769)。

您的 Jade Plus 将显示二维码的每个区域。

![Image](assets/fr/16.webp)

用笔涂满方格，并将您的种子复制成二维码。务必精确，以确保 Jade Plus 摄像头稍后能够扫描到它。使用箭头键前往下一个区域。

![Image](assets/fr/17.webp)

完成后，点击 "*Done*"。

![Image](assets/fr/18.webp)

用 Jade Plus 扫描手工制作的二维码，检查其有效性。

![Image](assets/fr/19.webp)

如果纸张备份正确，请单击 "*Continue*"。

![Image](assets/fr/20.webp)

在本教程中，我们将使用完全基于二维码扫描的连接模式，因此请选择 "*QR*"。

![Image](assets/fr/21.webp)

您还可以选择在 CompactSeedQR 备份之外添加一个 PIN 码，如选项 1。这提供了两种访问钱包的方式：通过 PIN 码和 Blockstream 的 "虚拟安全元素" 系统，或通过 CompactSeedQR 访问。

如果选择双 PIN 码选项，请选择 "*PIN*"，然后按照选项 1 的相同步骤设置 PIN 码。

如果只想继续使用 CompactSeedQR，请选择 "*SeedQR*"。

![Image](assets/fr/22.webp)

现在，您的钱包已创建，可以进入下一个步骤了。

![Image](assets/fr/23.webp)

每次启动时，点击 "*QR Mode*"按钮，然后点击 "*Scan SeedQR*"。

![Image](assets/fr/24.webp)

使用设备的摄像头将保存的种子扫描为二维码。

![Image](assets/fr/25.webp)

您的 Jade 现在已解锁。

![Image](assets/fr/26.webp)

## 添加 BIP39 Passphrase（密语）

BIP39 密码短语是一个可选密码，您可以自由选择，它会添加到您的助记词中，以增强钱包安全性。启用此功能后，访问您的比特币钱包需要同时输入助记词和密码短语。缺少其中任何一个，都将无法恢复钱包。

在 Jade Plus 上配置此选项之前，强烈建议您阅读以下文章，以充分了解密码短语的理论操作，并避免可能导致比特币丢失的错误：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在您的 Jade 仍处于锁定状态时（只有在设备未解锁时才能输入密码短语），访问 “Options” 选单。

![Image](assets/fr/42.webp)

选择 "*BIP39 Passphrase*"。

![Image](assets/fr/43.webp)

在 "*Frequency*" 选项中，您可以选择 Jade Plus 是否会在每次启动时都要求您输入密码：


- "Disabled"，禁止使用密语；
- "Next Login Only"，将要求您返回此选单，以便在下次启动时激活对密语的请求。该选项允许您不透露密语的使用情况；
- "Always Ask" 会导致 Jade 在每次启动时系统地询问您的密语，从而暴露您的钱包受口令保护。

根据您的安全策略选择选项。我个人选择 "Always Ask" 作为示例。

![Image](assets/fr/44.webp)

然后，您可以选择两种输入密码的方法：

- "*Manual*"：虚拟键盘可让您逐个字符输入字母（大写和小写）、数字和符号。这是所有硬件钱包的标准方法；
- "*WordList*"：Blockstream 为 Jade 设计的特定方法，可加快密语输入速度并增加其熵。在输入过程中，系统会建议使用 BIP39 列表中的单词，使解锁更加容易。该方法通过连接所选单词自动生成句子，并用空格分隔（例如："abandon ability able"）。

我个人建议您使用第一种方法，因为这是所有其他投资组合支持工具的标准。

![Image](assets/fr/45.webp)

然后，您可以返回主屏幕，像往常一样使用 PIN 码或 CompactSeedQR（如上图所示）解锁钱包。然后会要求您输入密码。

![Image](assets/fr/46.webp)

在 Jade 键盘上输入，并确保在物理介质（纸质或金属）上做一个或多个备份。在示例中，我使用了一个非常弱的密语，但您需要选择一个强大的随机密语，包括所有类型的字符，并且足够长（就像一个强大的密码）。

![Image](assets/fr/47.webp)

如果密语有效，请确认。

![Image](assets/fr/48.webp)

请注意，BIP39 密语对大小写和错别字敏感。如果您输入的密语与最初配置的密语略有不同，Jade 不会报错，但会推导出另一组加密密钥，与您最初配置的密钥不同。

因此，在配置时一定要记下您的主密钥指纹，它可以在屏幕右下角找到。例如，我的密语是 `Plan ₿ Academy`，我的主密钥指纹为 `3AD1AE65`。

![Image](assets/fr/49.webp)

每次使用密语解锁 Jade 时，请检查指纹是否与配置时输入的指纹相同。如果是，则说明您的密语是正确的，您访问的是正确的比特币钱包。如果不一样，说明您进入了错误的钱包，需要重新尝试，注意不要输入错误。

在您收到钱包中的第一枚比特币之前，**我强烈建议您执行一次清空恢复测试**。记下一些参考信息，例如您的 xpub 或第一个接收地址，然后在 Jade 增强版上删除您的钱包，此时钱包还是空的（`Options -> Device -> Factory Reset`）。然后尝试使用纸质备份的助记词和任何密语恢复钱包。检查还原后生成的 cookie 信息是否与您最初写下的信息一致。如果吻合，您就可以放心，您的纸质备份是可靠的。为了解有关如何进行测试恢复的更多信息，请参阅本教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 在 Sparrow Wallet 上配置钱包

在本教程中，我将使用 Sparrow Wallet 介绍 Jade Plus 的高级用法。不过，这种硬件钱包与许多其他程序兼容，如 Liana、Nunchuk、Specter、Green 和 Keeper。这些兼容性在连接方面各不相同：USB、蓝牙或二维码（详见简介中的表格）。

如果还没有下载 Sparrow Wallet 并将其安装到电脑上，请从[官方网站下载](https://sparrowwallet.com/)。

![Image](assets/fr/50.webp)

安装前请务必检查软件的真实性和完整性。如果您不知道如何操作，请参考本教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

打开 Sparrow Wallet 钱包后，点击 "*Files*" 标签，然后点击 "*New Wallet*"。

![Image](assets/fr/51.webp)

为钱包命名，然后点击 "*Create Wallet*"。

![Image](assets/fr/52.webp)

选择 "*Airgapped Hardware Wallet*"。

![Image](assets/fr/53.webp)

点击 "*Jade*" 选项旁边的 "*Scan...*"。

![Image](assets/fr/54.webp)

解锁 Jade Plus，如果正在使用，请输入密语。然后进入 "*Options*" 选单，选择 "*Wallet*"，点击 "*Export Xpub*"。

![Image](assets/fr/55.webp)

您的 Jade 将通过多个二维码显示您的 Keystore。使用 Sparrow 在机器上扫描它们。

![Image](assets/fr/56.webp)

现在您应该能看到您的 xpub 和主密钥指纹，它们应该与 Jade Plus 上的指纹一致。点击 "*Apply*"。

![Image](assets/fr/57.webp)

设置一个强大的密码，以确保安全访问您的 Sparrow Wallet。该密码将保护您的公钥、地址、标签和交易历史记录，防止未经授权的访问。最好将密码保存在密码管理器中，以免忘记。

![Image](assets/fr/58.webp)

您的钱包已在 Sparrow 上正确配置。

![Image](assets/fr/59.webp)

## 接收比特币

现在，您的 Jade Plus 已经配置好了，您可以在新的比特币钱包上接收比特币了。为此，请在 Sparrow 上点击 "*Receive*" 选单。

![Image](assets/fr/60.webp)

Sparrow 将显示您钱包中的第一个空白接待地址。

![Image](assets/fr/61.webp)

在使用之前，我们先在 Jade Plus 屏幕上检查一下，确保它属于我们的比特币钱包。在翡翠上点击 "*Scan QR*"，然后扫描 Sparrow 上显示的地址的二维码。

![Image](assets/fr/62.webp)

检查 Jade 屏幕上显示的地址是否与 Sparrow Wallet 上显示的地址一致。如果一致，请点击复选标记继续。

![Image](assets/fr/63.webp)

然后，您的硬件钱包会确认该地址是您钱包的一部分，并确认它持有相关的私钥。

![Image](assets/fr/64.webp)

如果您的 Jade 验证了该地址，您就可以用它来接收比特币了。当交易在网络上广播时，它就会出现在 Sparrow 上。等到收到足够多的确认信息后，交易才算完成。

![Image](assets/fr/65.webp)

## 发送比特币

现在您的钱包里已经有了一些聪（比特币），您还可以发送一些聪。为此，请点击 "*UTXOs*" 选单。

![Image](assets/fr/66.webp)

选择希望用作此交易输入的 UTXO，然后点击 "*Send Selected*"。

![Image](assets/fr/67.webp)

输入接收者地址、提醒您交易目的的标签以及您希望发送到该地址的金额。

![Image](assets/fr/68.webp)

根据当前市场情况调整收费率，然后点击 "*Create Transaction*"。

![Image](assets/fr/69.webp)

检查所有交易参数是否正确，然后点击 "*Finalize Transaction for Signing*"。

![Image](assets/fr/70.webp)

点击 "*Show QR*" 来显示 PSBT（*部分签名比特币交易*）。Sparrow 已经建立了交易，但还缺少签名来解锁输入中使用的比特币。这些签名只能由 Jade Plus 来完成，因为 Jade Plus 承载着您的种子，可以获取签署交易所需的私钥。

![Image](assets/fr/71.webp)

在 Jade Plus 上点击 "*Scan QR*"，扫描 Sparrow 上显示的 PSBT。

![Image](assets/fr/72.webp)

确认地址和发送金额正确无误，然后点击箭头以进行验证。

![Image](assets/fr/73.webp)

确保费用金额是您选择的金额，然后点击界面左上角的 "√" 图标，签名交易。

![Image](assets/fr/74.webp)

在 Sparrow Wallet 上，点击 "*Scan QR*" 并扫描 Jade 上显示的二维码。

![Image](assets/fr/75.webp)

您签名的交易现在可以在比特币网络上广播，并被矿工纳入一个区块。如果一切正常，请点击 "*Broadcast Transaction*"。

![Image](assets/fr/76.webp)

您的交易已被广播，正在等待确认。

![Image](assets/fr/77.webp)

恭喜您，现在您已经知道如何在二维码模式下设置和使用 Jade Plus 了。如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。感谢您的分享！

如果您想进一步学习，我推荐您阅读关于 Jade Plus 的另一篇教程，我们将通过蓝牙与 Green 手机应用进行配置：

https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
