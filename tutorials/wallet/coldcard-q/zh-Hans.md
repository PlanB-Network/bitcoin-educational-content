---
name: COLDCARD Q
description: 设置和使用 COLDCARD Q
---
![cover](assets/cover.webp)

硬件钱包是一种专用于管理和保护比特币钱包私钥的电子设备。与安装在通常连接到互联网的通用机器上的软件钱包（或热钱包）不同，硬件钱包可以实现私钥的物理隔离，降低盗版和盗窃的风险。

硬件钱包的主要目的是尽可能减少设备的功能，从而将攻击面降到最低。更小的攻击面也意味着更少的潜在攻击载体，即攻击者可以利用的系统弱点更少，从而获得比特币。

我们建议使用硬件钱包来保护您的比特币，尤其是如果您持有大量比特币，无论是绝对值还是占总资产的比例。

硬件钱包需配合电脑或智能手机上的钱包管理软件使用。后者管理交易的创建，但使这些交易有效所需的加密签名完全在硬件钱包内进行。这意味着私钥永远不会暴露在潜在的脆弱环境中。

硬件钱包为用户提供双重保护：一方面，它们通过保持私钥离线来保护比特币免受远程攻击；另一方面，它们通常对试图提取私钥的行为提供更大的物理阻力。正是基于这两个安全标准，我们可以对市场上的不同型号进行判断和分类。

在本教程中，我将向您介绍这样一种解决方案：**COLDCARD Q**。

---
由于 COLDCARD Q 功能繁多，我建议将其使用分为两个教程。在第一个教程中，我们将了解设备的初始配置和基本功能。然后，在第二个教程中，我们将学习如何利用 COLDCARD 的所有高级选项。

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## COLDCARD Q 介绍

COLDCARD Q 是加拿大 Coinkite 公司开发的比特币专用硬件钱包。Q 代表了他们迄今为止最先进的产品，被定位为终极比特币硬件钱包。

在硬件方面，COLDCARD Q 配备了最佳用户体验所需的所有功能：


- 大型液晶显示屏简化了导航和操作；
- QWERTY 全键盘
- 集成摄像头，可扫描二维码；
- 两个 microSD 卡槽；
- 可通过三节 AAA 电池（需另购）或 USB-C 线缆供电，实现完全隔离的供电方式；
- 采用来自两家不同制造商的双重安全元件，增强安全性；
- 支持 NFC 近场通信。。

在我看来，COLDCARD Q 只有两个缺点。首先，由于其功能众多，它体积较大，长约 13 厘米，宽约 8 厘米，几乎相当于一部小型智能手机的大小。电池仓也让它显得比较厚。如果您正在寻找一款更小巧、更便携的硬件钱包，那么更加紧凑的 MK4 或许是更好的选择。第二个缺点显而易见，那就是它的价格。在官网上的售价为 239.99 美元，比 MK4 贵了 72 美元，这使得 Q 直接与 Ledger Flex 或 Foundation Passport 等高端硬件钱包展开竞争。

![CCQ](assets/fr/001.webp)

在软件方面，COLDCARD Q 与 Coinkite 的其他设备一样，配备了大量先进功能：

- 掷骰子选项（Dice Roll），以生成您自己的恢复助记词；
- PIN 码 ；
- 最终密码锁定倒计时 ；
- BIP39 密码 ；
- 最终锁定 PIN 码 ；
- 连接倒计时 ；
- SeedXOR；
- BIP85...

简而言之，与 MK4 相比，COLDCARD Q 提供了更好的用户体验，可能非常适合寻求更高易用性的中高级用户。

COLDCARD Q 可在 [Coinkite 官方网站](https://store.coinkite.com/store/coldcard) 上购买。您也可以从零售商处购买。

## 教程准备

收到 COLDCARD 后，第一步是检查包装，确保没有被打开过。如果包装破损，这可能表明硬件钱包已损坏，可能不是正品。

![CCQ](assets/fr/002.webp)

打开盒子后，您会发现以下物品：

- 装在一个密封袋中的 COLDCARD Q；
- 用于记录助记词的卡片。

![CCQ](assets/fr/003.webp)

确保袋子没有被拆封或损坏。还要检查包装袋上的编号是否与袋内纸张上的编号一致。请保留此号码以备将来参考。

![CCQ](assets/fr/004.webp)

如果您希望在不连接电脑（气隙）的情况下为 COLDCARD 供电，请在设备背面插入三节 AAA 电池。或者，您也可以通过 USB-C 数据线将其连接到电脑。

![CCQ](assets/fr/005.webp)

在本教程中，您还需要 Sparrow Wallet 来管理您电脑上的比特币钱包。从官方网站下载 [Sparrow Wallet](https://sparrowwallet.com/download/)。我强烈建议您在安装前检查其真实性（使用 GnuPG）和完整性（通过检查其哈希值）。如果不知道如何操作，请参考本教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 选择 PIN 码

现在您可以按左上角的按钮开启 COLDCARD。

![CCQ](assets/fr/006.webp)

按 "*ENTER*" 按钮接受使用条款。

![CCQ](assets/fr/007.webp)

然后，COLDCARD Q 将在屏幕上方显示一个数字。请确保该号码与密封袋上和袋内塑料片上的号码一致。这样可以确保您的包裹在由 Coinkite 包装到您打开之间没有被打开过。按 "*ENTER*" 继续。

![CCQ](assets/fr/008.webp)

前往至 "*选择 PIN 码*" 选单并按 "*ENTER*" 键以确认。

![CCQ](assets/fr/009.webp)

该 PIN 码用于解锁您的 COLDCARD。因此，它可以防止未经授权的访问。该 PIN 与钱包加密密钥的生成过程无关。因此，即使无法获得该 PIN 码，拥有您的助记词也可以重新获得比特币。

COLDCARD PIN 码分为两个部分：前缀（prefix）和后缀（suffix），每个前缀和后缀可包含 2 到 6 位数字，总共 4 到 12 位数字。解锁 COLDCARD 时，首先需要输入前缀，然后设备会显示 2 个单词。然后输入后缀。这两个单词将在此配置步骤中提供给您，请仔细保存，因为每次解锁 COLDCARD 时都需要用到它们。如果在解锁过程中显示的两个单词与您在配置过程中保存的单词一致，这将确认您的设备在上次使用后没有被破解过。

再次点击 "*Choose PIN*"。

![CCQ](assets/fr/010.webp)

确认您已阅读的警告。

![CCQ](assets/fr/011.webp)

现在请选择您的 PIN 码。我们建议您选择一个较长的随机 PIN 码。请确保将该密码放在与存储 COLDCARD 不同的地方。您可以使用随包裹提供的卡片来记录该密码。

输入您选择的前缀，然后按 "*ENTER*" 键确认 PIN 码的第一部分。

![CCQ](assets/fr/012.webp)

然后，屏幕上将显示两个反钓鱼字样。请仔细保存，以备将来参考。您可以使用软件包中附带的卡片将它们写下来。

![CCQ](assets/fr/013.webp)

然后输入密码的第二部分并按 "*ENTER*"。

![CCQ](assets/fr/014.webp)

再次输入密码确认，检查两个反钓鱼词是否与您之前保存的一致。

![CCQ](assets/fr/015.webp)

从现在起，每次解锁您的 COLDCARD 时，请记得检查输入 PIN 密码前缀后屏幕上出现的两个反钓鱼字的有效性。

## 固件更新

首次使用设备时，必须检查并更新固件。为此，请访问 "*Advanced/Tools*" 选单。

![CCQ](assets/fr/016.webp)

**重要提示：** 如果您计划升级固件，并且这不是您第一次使用 COLDCARD（即您已经在 COLDCARD 上创建了一个钱包），请确保您拥有您的助记词，并且它是有效的（以及可选的密语，如果钱包带有密语）。这一点很重要，可避免在设备更新过程中出现问题时丢失比特币。

选择 "*Upgrade Firmware*"。

![CCQ](assets/fr/017.webp)

选择 "*Show Version*"。

![CCQ](assets/fr/018.webp)

您可以查看 COLDCARD 当前的固件版本。例如，我的固件版本是 "*1.2.3Q*"。

![CCQ](assets/fr/019.webp)

查看 [COLDCARD 官方网站](https://coldcard.com/downloads) 是否有更新版本。点击 "Download" 以下载新固件。

![CCQ](assets/fr/020.webp)

此时，我们强烈建议检查下载固件的完整性和真实性。为此，请下载[包含所有版本哈希值并由开发人员签名的文件](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt)，使用[开发者的公开密钥](https://keybase.io/dochex)验证签名，并确保签名文件中显示的哈希值与从网站下载的固件的哈希值一致。如果一切正常，就可以继续更新。

如果您不熟悉这个验证过程，我建议您参考本教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

使用 microSD 卡并将固件文件（文件格式为 `.dfu`）传输到该卡中。将 microSD 卡插入 COLDCARD 的一个端口。

![CCQ](assets/fr/021.webp)

然后，在固件更新选单中选择 "*From MicroSD*"。

![CCQ](assets/fr/022.webp)

选择固件对应的文件。

![CCQ](assets/fr/023.webp)

按 "*ENTER*" 键确认选择。

![CCQ](assets/fr/024.webp)

请等待固件更新。

![CCQ](assets/fr/025.webp)

更新完成后，输入 PIN 码解锁设备。

![CCQ](assets/fr/026.webp)

您的固件现已更新。

## COLDCARD Q 参数

如需，您可以进入 "*Settings*" 选单查看 COLDCARD 的设置。

![CCQ](assets/fr/027.webp)

在该选单中，您可以找到各种自定义选项，例如设置屏幕亮度或选择默认计量单位。

![CCQ](assets/fr/028.webp)

我们将在下一个教程中介绍其他高级设置：

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## 创建比特币钱包

现在是时候生成一个新的比特币钱包了！为此，您需要创建一个助记词。在 Coldcard 上，有三种方法可以生成这个助记词：


- 仅使用内部随机数生成器 (TRNG)；
- 使用 TRNG 和掷骰子的组合来增加熵；
- 只使用掷骰子。

**对于初学者和中级用户，我们建议只使用 COLDCARD 的内部随机数生成器**。

我不建议只使用骰子，因为执行不力会导致熵值不足，危及钱包安全。

不过，最好的方案肯定是第二种，即结合使用 TRNG 和外部熵源。这种方法保证了与 TRNG 本身相同的最低熵，并在内部生成器可能发生故障（无论是否自愿）的情况下增加了额外的安全级别。通过选择这种将 TRNG 和掷骰子相结合的方法，您可以更好地控制句子的生成，而不会增加因您执行不力而带来的风险。

点击 "*New Seed Words*"。

![CCQ](assets/fr/029.webp)

您可以选择句子的长度。我建议您选择 12 个单词的助记词，因为它的管理复杂程度较低，而且与 24 个单词的助记词相比，它提供的钱包安全性也不逊色。

![CCQ](assets/fr/030.webp)

然后 COLDCARD 将显示 TRNG 生成的助记词。如果希望添加额外的外部熵，请按 "*4*" 键。

![CCQ](assets/fr/031.webp)

这将带您进入一个页面，您可以通过掷骰子增加熵。尽可能多地掷骰子（建议至少掷 50 次，但少于 50 次也无妨，因为您已经受益于 TRNG 的熵），并用 "*1*"到 "*6*"键记录结果。完成后，按 "*ENTER*" 键以确认。

![CCQ](assets/fr/032.webp)

根据您刚刚提供的熵值和 TRNG 的熵值，将显示一个新的助记词。

**警告：这个助记词可以完全、不受限制地访问您的所有比特币**。任何拥有这个助记词的人都可以盗取您的资金，即使没有实际接触到您的 COLDCARD。如果您的 COLDCARD 丢失、被盗或破损，该 12 个字的短语可以恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。

您可以把它写在 COLDCARD 随附的纸板上，或者为了增加安全性，我建议您把它刻在不锈钢支架上，以防火灾、水灾或倒塌。无论如何，千万不要把它保存在数字媒介上，否则您可能会丢失比特币。

将屏幕上提供的单词写在您选择的物理介质上。根据您的安全策略，您可以考虑制作几份完整的句子实体副本（但最重要的是，不要将其分割开来）。重要的是，要对单词进行编号并按顺序排列。

显然，与本教程不同的是，**您绝不要在互联网上分享这些单词**。本钱包将仅在 Testnet 上使用，并将在本教程结束后删除。

写下单词后，按 "*ENTER*" 键。

![CCQ](assets/fr/033.webp)

为确保您已正确保存助记词，系统会要求您确认某些单词。在键盘上选择与每个单词对应的数字。

![CCQ](assets/fr/034.webp)

您的钱包现已创建！在屏幕右上角，您可以看到您的主私钥指纹。按 "*ENTER*"。

![CCQ](assets/fr/035.webp)

现在您可以进入 COLDCARD 的主页面。

![CCQ](assets/fr/036.webp)

## 在麻雀上建立新的钱包

在 Sparrow Wallet 软件和 COLDCARD 之间建立通信有多种选择。最直接的是使用 USB-C 数据线。不过，您的 COLDCARD 默认禁用了电缆和 NFC 通信。为了重新激活它们，请进入 "*Settings*"，然后进入 "*Hardware On/Off*"，激活所需的通信选项。

![CCQ](assets/fr/037.webp)

如果希望将 COLDCARD 与电脑完全隔离，可以选择使用二维码或 microSD 卡进行间接 "Air-gap"（空气隔离）通信。这就是我们在本教程中要使用的方法。

前往 "*Advanced/Tools*"。

![CCQ](assets/fr/038.webp)

选择 "*Export Wallet*"。

![CCQ](assets/fr/039.webp)

然后选择 "*Sparrow Wallet*"。

![CCQ](assets/fr/040.webp)

按 "*ENTER*" 键以生成配置文件。

![CCQ](assets/fr/041.webp)

然后选择向 Sparrow Wallet 发送文件的方式。在本例中，我在插槽 "*A*" 中插入了一个 microSD，因此我会选择 "*1*" 按钮。您也可以按 "*QR*" 按钮，在 COLDCARD 屏幕上以二维码的形式显示信息，并用电脑摄像头扫描该二维码。

![CCQ](assets/fr/042.webp)

启动 Sparrow Wallet，跳过介绍页面进入主屏幕。检查屏幕右下方的开关，确保您已正确连接到一个节点。

![CCQ](assets/fr/043.webp)

强烈建议您使用自己的比特币节点。在本教程中，我使用公共节点（黄色），因为我在测试网上使用，但对于生产使用，最好在本地使用 Bitcoin Core（绿色）或在远程节点上使用 Electrum 服务器（蓝色）。

进入 "*File*" 选单，选择 "*New Wallet*"。

![CCQ](assets/fr/044.webp)

为钱包命名，然后点击 "*Create Wallet*"。

![CCQ](assets/fr/045.webp)

在 "*Script Type*" 下拉选单中，选择保护比特币安全的脚本类型。

![CCQ](assets/fr/046.webp)

点击 "*Airgapped Hardware Wallet*"。

![CCQ](assets/fr/047.webp)

在 "*COLDCARD*" 选项卡下，如果要扫描 COLDCARD 上显示的二维码，请单击 "*Scan...*"；如果要从 microSD 中导入文件（这是`.json`文件），请单击 "*Import File...*"。

![CCQ](assets/fr/048.webp)

导入后，检查 Sparrow 上显示的 "*Master fingerprint*"是否与 COLDCARD 上显示的一致。点击 "*Apply*" 以确认创建。

![CCQ](assets/fr/049.webp)

设置强密码以保护您的 Sparrow Wallet 访问权限。此密码将保护您的公钥、地址、标签和交易记录免遭未经授权的访问。

最好把这个密码保存下来，以免忘记（例如保存在密码管理器中）。

![CCQ](assets/fr/050.webp)

您的钱包已在 Sparrow Wallet 上设置完毕。。

![CCQ](assets/fr/051.webp)

在您收到第一笔比特币之前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，例如您的 xpub，然后在钱包为空的情况下重置您的 COLDCARD Q。然后尝试使用您的纸质备份将钱包恢复到 COLDCARD。检查恢复后生成的 xpub 是否与您最初记录的 xpub 一致。如果一致，您可以放心，您的纸质备份是可靠的。

为了了解如何进行恢复测试，我建议您参考这篇教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 接收比特币

为了接收比特币，首先要打开并解锁 COLDCARD。

![CCQ](assets/fr/052.webp)

在 Sparrow Wallet 上，点击 "*Receive*" 选项卡。

![CCQ](assets/fr/053.webp)

在使用 Sparrow 钱包提供的地址之前，请在 COLDCARD 屏幕上检查该地址。这种做法可以让您确认 Sparrow 上显示的地址不是欺诈性的，而且硬件钱包确实持有必要的私钥，以便随后使用该地址安全地消费比特币。这可以帮助您避免几种类型的攻击。

为了执行此检查，请单击 COLDCARD 上的 "*Address Explorer*" 选单。

![CCQ](assets/fr/054.webp)

选择您在 Sparrow 上使用的脚本类型。我使用 Segwit P2WPKH。所以我会点击它。

![CCQ](assets/fr/055.webp)

然后，您就可以按顺序查看不同的派生地址。

![CCQ](assets/fr/056.webp)

使用 Sparrow 检查地址是否匹配。在我的案例中，具有派生路径 `m/84'/1'/0'/0/0` 的地址在 Sparrow 和 COLDCARD 上确实是 `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr`。

![CCQ](assets/fr/057.webp)

另一种验证该地址所有权的方法是用 COLDCARD 直接扫描 Sparrow 上的二维码。在 COLDCARD 主页屏幕上，选择 "**Scan Any QR Code*"。也可以使用键盘上的 "*QR*" 键。

![CCQ](assets/fr/058.webp)

扫描 Sparrow Wallet 上显示的地址的二维码。

![CCQ](assets/fr/059.webp)

确保 COLDCARD 上显示的地址与 Sparrow 上显示的地址一致。然后按 "*1*" 按钮。

![CCQ](assets/fr/060.webp)

至此，地址确认成功。

![CCQ](assets/fr/061.webp)

现在，您可以添加一个 "*Label*"（标签）来描述该地址的比特币来源。这是一个很好的做法，可以让您更好地管理您的 UTXO。

![CCQ](assets/fr/062.webp)

关于标签的更多信息，我还推荐您查看另一篇教程：

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然后，您就可以使用该地址接收比特币。

![CCQ](assets/fr/063.webp)

## 发送比特币

现在，您已经在您的 COLDCARD 安全钱包中收到了第一笔聪，您也可以花掉它们了！

像往常一样，首先打开并解锁 COLDCARD Q，然后打开 Sparrow Wallet 并前往到 "*Send*" 选项卡以准备新的交易。

![CCQ](assets/fr/064.webp)

如果您想进行 "币控制"（Coin Control），即具体选择在交易中消耗哪些 UTXOs，请转到 "*UTXOs*" 选项卡。选择要消费的 UTXO，然后点击 "*Send Selected*"。您将跳转到 "*Send*" 选项卡中的同一界面，但已为交易选择了 UTXO。

![CCQ](assets/fr/065.webp)

输入目的地地址。您也可以点击 "*+ Add*" 按钮输入多个地址。

![CCQ](assets/fr/066.webp)

写下 "*Label*"，以记住这笔费用的用途。

![CCQ](assets/fr/067.webp)

选择要发送到此地址的金额。

![CCQ](assets/fr/068.webp)

根据当前市场调整手续费的费率。

![CCQ](assets/fr/069.webp)

确保所有交易参数正确无误，然后点击 "*Create Transaction*"。

![CCQ](assets/fr/070.webp)

如果一切确认无误，请点击 "*Finalize Transaction for Signing*"。

![CCQ](assets/fr/071.webp)

在 Sparrow 中完成交易后，就该用 COLDCARD 签名了。要将 PSBT（待签名的比特币交易）传输到您的设备，您有几种选择。如果启用了有线数据传输，就可以像使用其他硬件钱包一样，通过 USB-C 连接直接发送交易。在这种情况下，您必须点击 Sparrow 右下角的 "*Sign*" 按钮。在我的例子中，由于 COLDCARD 没有通过电缆连接，因此该按钮处于禁用状态。

![CCQ](assets/fr/072.webp)

如果您希望保持 “空气隔离”（air-gap）连接，避免硬件钱包与电脑直接接触，您有两种选择。第一种，也是比较复杂的方法，是使用 microSD 卡。将 microSD 卡插入电脑，通过 Sparrow 上的 “*Save Transaction*” 按钮记录交易，然后将此卡插入 COLDCARD 的端口。

![CCQ](assets/fr/073.webp)

然后进入 "*Ready To Sign*" 选单。

![CCQ](assets/fr/074.webp)

查看 COLDCARD 上的交易详情，包括收款地址、发送金额和交易费用。

![CCQ](assets/fr/075.webp)

如果一切无误，请按 "*ENTER*" 按钮以签名交易。

![CCQ](assets/fr/076.webp)

然后将 microSD 放回电脑，在 Sparrow 上点击 "*Load Transaction*"，从 microSD 加载已签名的交易。然后，您就可以在上传到比特币网络之前进行最后的检查了。

![CCQ](assets/fr/077.webp)

第二种使用 COLDCARD 在 Air-Gap 模式下进行签名的方法，比 microSD 卡签名方法简单得多，即直接通过设备的摄像头扫描 PSBT。在 Sparrow 中，选择 “*Show QR*”。

![CCQ](assets/fr/078.webp)

在 COLDCARD 上选择 "*Scan Any QR Code*"。您也可以使用键盘上的 "*QR*" 键。

![CCQ](assets/fr/079.webp)

使用 COLDCARD 的摄像头扫描 Sparrow 上显示的二维码。

![CCQ](assets/fr/080.webp)

交易详情将再次出现，以供核实。如果一切正确无误，请按 "*ENTER*" 键以完成签名。

![CCQ](assets/fr/081.webp)

然后，您的 COLDCARD 将以二维码的形式显示已签名的交易。在 Sparrow 上选择 "*Scan QR*"，使用电脑摄像头扫描该二维码。

![CCQ](assets/fr/082.webp)

您签署的交易现在可以在 Sparrow 上看到了。最后检查一次，确认一切无误后，点击 "*Broadcast Transaction*"，在比特币网络上进行广播。

![CCQ](assets/fr/083.webp)

您可以在 Sparrow Wallet 的 "*Transaction*" 选项卡中跟踪您的交易。

![CCQ](assets/fr/084.webp)

恭喜，您现在已经掌握了 COLDCARD Q 与 Sparrow Wallet 的基本使用方法！

如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本教程。非常感谢！

我还建议您看看其他教程，其中我们讨论了 COLDCARD Q 的高级选项：

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
