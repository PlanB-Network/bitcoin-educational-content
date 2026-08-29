---
name: Ledger Flex
description: 设置和使用 Ledger Flex
---
![cover](assets/cover.webp)

硬件钱包是一种专门用于管理和保护比特币钱包私钥的电子设备。与安装在通常连接互联网的通用计算机上的软件钱包（或热钱包）不同，硬件钱包能够将私钥物理隔离，从而降低被黑客攻击和盗窃的风险。

硬件钱包的主要目标是最大限度地减少设备的功能，从而缩小其攻击面。攻击面越小，潜在的攻击途径就越少，也就是说，攻击者可以利用的系统中的薄弱环节就越少，从而更容易访问比特币。

建议使用硬件钱包来保护您的比特币，尤其是在您持有大量比特币的情况下，无论其绝对价值或占总资产的比例如何。

硬件钱包需与电脑或智能手机上的钱包管理软件配合使用。该软件负责创建交易，但验证这些交易所需的加密签名仅在硬件钱包内部完成。这意味着私钥永远不会暴露在潜在的安全环境中。

硬件钱包为用户提供双重保护：一方面，它们通过将私钥离线保存来保护您的比特币免受远程攻击；另一方面，它们通常具有更强的物理防护能力，能够有效防止密钥被提取。正是基于这两个安全标准，我们可以对市面上不同的硬件钱包型号进行评判和排名。

在本教程中，我将介绍其中一种解决方案：**Ledger Flex**。

![LEDGER FLEX](assets/notext/01.webp)

## Ledger Flex 简介

Ledger Flex 是由法国公司 Ledger 生产的硬件钱包，售价为 249 欧元。

![LEDGER FLEX](assets/notext/02.webp)

它配备了一块大尺寸的 E Ink 触摸屏，采用黑白显示技术。这项技术也应用于电子阅读器。E Ink 屏幕即使在阳光直射下也能提供清晰易读的显示效果，并且在屏幕静止时几乎不耗电。其工作原理是利用含有黑白颜料颗粒的微胶囊。当施加电荷时，黑色或白色颗粒会移动到屏幕表面，从而形成文字或图像。

Ledger Flex 配备了 CC EAL6+ 认证的“安全元件”芯片，可有效防止硬件遭受物理攻击。屏幕由该芯片直接控制。一个常见的批评点是，这款芯片的代码并非开源，因此用户需要对该组件的完整性有一定的信任度。不过，该组件会接受独立专家的审核。

在使用方面，Ledger Flex 提供多种连接方式：蓝牙、USB-C 和 NFC。大屏幕方便用户轻松查看交易详情。Ledger 的另一大优势在于其对比特币新功能的快速响应，例如 Miniscript。

经过测试，我对这款产品的品质印象深刻。用户体验极佳，设备操作直观。它是一款优秀的硬件钱包。然而，在我看来，它有两个主要缺点：一是无法验证芯片代码，二是价格，它的价格明显高于竞争对手。作为对比，Foundation 的顶级型号售价为 199 美元，Coinkite 的售价为 219.99 美元，而同样配备大尺寸触摸屏的最新款 Trezor 售价为 169 欧元。

## 如何购买 Ledger Flex？
Ledger Flex 现已在[官方网站](https://shop.ledger.com/pages/ledger-flex)上开放购买。如果您想在实体店购买，也可以在 Ledger 网站上找到[认证经销商列表](https://www.ledger.com/reseller)。

## 前提条件

收到 Ledger Flex 后，第一步是检查包装，确保其未被打开。

![LEDGER FLEX](assets/notext/03.webp)

Ledger 的包装内应包含两条密封条。如果这两条密封条缺失或损坏，则可能表明该硬件钱包已被篡改，并非正品。

![LEDGER FLEX](assets/notext/04.webp)

打开后，您应该在盒子里找到以下物品：
- Ledger Flex；
- USB-C 数据线；
- 用户手册；
- 用于记录助记词的卡片。

![LEDGER FLEX](assets/notext/05.webp)

对于本教程，您将需要 2 个软件：Ledger Live 来初始化 Ledger Flex，以及 Sparrow Wallet 来管理您的比特币钱包。从官方网站下载 [Ledger Live](https://www.ledger.com/ledger-live) 和 [Sparrow Wallet](https://sparrowwallet.com/download/)。

![LEDGER FLEX](assets/notext/06.webp)
我们很快会提供一个教程，教导您如何验证您下载的软件的真实性和完整性。我强烈建议在这里对 Ledger Live 和 Sparrow 进行验证。

## 如何用 Ledger Live 初始化 Ledger Flex？

按住右侧按钮几秒钟以开启您的 Ledger Flex。

![LEDGER FLEX](assets/notext/07.webp)

浏览不同的介绍页面。

![LEDGER FLEX](assets/notext/08.webp)

选择 “*Set up without Ledger Live*” 选项，然后点击 “*Skip Ledger Livee*” 按钮。

![LEDGER FLEX](assets/notext/09.webp)

接下来，系统会要求您为您的 Ledger 选择一个名称。点击 “*Set name*”，然后输入您选择的名称。

![LEDGER FLEX](assets/notext/10.webp)

为您的设备选择一个 PIN 码，这将用于解锁您的 Ledger。因此，这是一种防止未经授权的物理访问的保护措施。这个 PIN 码不参与您钱包的加密密钥的派生。因此，即使没有这个 PIN 码，拥有您的 24 个单词的助记词也能让您重新获得对您比特币的访问权。

建议选择一个尽可能随机的 8 位数 PIN 码。同时，确保将此代码保存在与您的 Ledger Flex 存放位置不同的地方（例如，在密码管理器中）。

![LEDGER FLEX](assets/notext/11.webp)

再次输入您的 PIN 码以确认。

![LEDGER FLEX](assets/notext/12.webp)

然后，系统会提示您选择是恢复现有钱包还是创建一个新钱包。在本教程中，我们将介绍从头开始创建一个新钱包，因此选择 “*Set up as a new Ledger*” 选项以生成一个新的助记词。

![LEDGER FLEX](assets/notext/13.webp)

您的 Flex 将提供关于如何管理您的恢复助记词的指导。

**此助记词可让您完全且无限制地访问您的所有比特币。**任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Ledger 设备。这 24 个单词的助记词可以在您的 Ledger Flex 设备丢失、被盗或损坏时帮助您恢复对比特币的访问权限。因此，务必将其妥善保存在安全的地方。
您可以将其写在 Ledger 设备随附的硬纸板上，或者为了更加安全，我建议您将其刻在不锈钢材质上，以防止火灾、洪水或设备倒塌等风险。

您可以通过触摸屏幕浏览这些说明并跳过页面。

![LEDGER FLEX](assets/notext/14.webp)
Ledger 设备将使用其随机数生成器生成您的助记词。请确保在此过程中无人窥视。将 Ledger 设备生成的单词写在您选择的物理介质上。根据您的安全策略，您可以考虑制作几份完整的助记词副本（但最重要的是，不要将其拆分）。务必按顺序编号并记录单词。

***显然，您绝不应该像本教程中那样在互联网上分享这些单词。此示例钱包仅用于测试网，教程结束后将被删除。***

![LEDGER FLEX](assets/notext/15.webp)

要移动到下一组单词，请点击 “*Next*” 按钮。记录所有单词后，点击 “*Done*” 按钮继续下一步。

![LEDGER FLEX](assets/notext/16.webp)

点击 “*Start confirmation*” 按钮，然后按顺序选择助记词，确认您已正确记录。重复此步骤，直到记录第 24 个单词。

![LEDGER FLEX](assets/notext/17.webp)

如果您确认的助记词与 Flex 在上一步中提供的助记词完全一致，则可以继续。否则，说明您的助记词备份有误，需要重新开始。

![LEDGER FLEX](assets/notext/18.webp)

好了，您的助记词已在 Ledger Flex 上正确创建。在使用此助记词创建新的比特币钱包之前，让我们一起来了解一下设备设置。

## 如何修改 Ledger 的设置？

为了锁定和解锁您的 Ledger，请按侧面按钮。然后，系统会要求您输入在上一步设置的 PIN 码。

![LEDGER FLEX](assets/notext/19.webp)

为了访问设置，请点击设备左下角的齿轮符号。

![LEDGER FLEX](assets/notext/20.webp)

“*Name*” 选单允许您更改 Ledger 的名称。

![LEDGER FLEX](assets/notext/21.webp)

在 “*About this Ledger*” 中，您将找到有关您的 Flex 的信息。

![LEDGER FLEX](assets/notext/22.webp)

在 “*Lock screen*” 选单中，您可以通过选择 “*Customize lock screen picture*” 更改锁屏显示的图像。得益于设备的 E Ink 屏幕技术，可以在不消耗电池的情况下持续开启屏幕。E Ink 屏幕在维持静态图像时不使用能源。然而，在显示变化时它们确实消耗能源。
“*Auto-lock*” 子选单允许您配置并激活在确定的不活动期后自动锁定您的 Ledger。
![LEDGER FLEX](assets/notext/23.webp)
"*Sounds*" 选单允许您开启或关闭您的 Flex 的声音。在 "Language" 选单中，您可以更改显示语言。
![LEDGER FLEX](assets/notext/24.webp)

点击右箭头，您可以访问其他设置。"*Change PIN*" 允许您更改您的 PIN 码。

![LEDGER FLEX](assets/notext/25.webp)

"*Bluetooth*"（蓝牙）和 "*NFC*"（近场通讯）选单允许您管理这些通信。

![LEDGER FLEX](assets/notext/26.webp)

在 "*Battery*" 中，您可以设置 Ledger 的自动关机功能。

![LEDGER FLEX](assets/notext/27.webp)

"*Advanced*" 部分提供更高级的安全设置。建议启用“PIN 码随机排列”选项以增强安全性。您也可以在此选单中配置 BIP39 Passphrase（密语）

![LEDGER FLEX](assets/notext/28.webp)

密语是一个可选的密码，与恢复助记词结合使用，为您的钱包提供了额外的安全层。

目前，您的钱包由一个包含 24 个单词的助记词生成。这个恢复助记词非常重要，因为它允许您在丢失钱包密钥时恢复所有密钥。然而，它也构成了一个单点故障 (SPOF)。如果它被破解，您的比特币就会面临风险。这就是密码的作用所在。密码是一个可选的密码，您可以随意选择，它与助记词结合使用，以增强钱包的安全性。

密语不应与 PIN 码混淆。它在生成加密密钥的过程中发挥着作用。它与助记词协同工作，修改用于生成密钥的种子。因此，即使有人获得了您的 24 个单词的助记词，如果没有密语，他们也无法访问您的资金。使用密码实际上会创建一个具有不同密钥的新钱包。即使对密码进行细微的修改，也会生成一个不同的钱包。

密语是增强比特币安全性的强大工具。但是，在使用前了解其工作原理至关重要，以免丢失钱包访问权限。我将在另一个专门的教程中解释如何使用密语。

![LEDGER FLEX](assets/notext/29.webp)

密语是强化比特币安全性的一种非常强大的工具。不过，在启用之前务必要充分了解其工作原理，以避免失去对钱包的访问权限。因此我在另一篇专门的教程中做了详细讲解：

https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

最后，最后一个设置页面允许您重置您的 Ledger。只有在您确定它不包含任何保护比特币的密钥时，才进行这个重置，因为您可能会永久失去访问您的资金的权限。
![LEDGER FLEX](assets/notext/30.webp)

## 如何安装比特币应用程序？

首先，在您的电脑上启动 Ledger Live 软件，然后连接并解锁您的 Ledger Flex。

![LEDGER FLEX](assets/notext/31.webp)

在 Ledger Live 中，前往 "*My Ledger*" 选单。系统将要求您授权访问您的 Flex。

![LEDGER FLEX](assets/notext/32.webp)

在您的 Ledger 上点击 "*Allow*" 按钮以验证访问。

![LEDGER FLEX](assets/notext/33.webp)

首先，如果您的 Ledger Flex 的固件不是最新的，Ledger Live 将自动提供更新它。如果适用，点击 "*Update Firmware*"，然后点击 "*Install update*" 开始安装。

![LEDGER FLEX](assets/notext/34.webp)

在您的 Ledger 上点击 "*Install*" 按钮，然后等待安装过程完成。

![LEDGER FLEX](assets/notext/35.webp)

您的 Ledger Flex 的固件现在已经是最新的。

![LEDGER FLEX](assets/notext/36.webp)

如果您愿意，您可以更改您的 Ledger Flex 的锁屏壁纸。为此，请点击“*Add >*”。

![LEDGER FLEX](assets/notext/37.webp)

点击 “*Upload from computer*” 按钮，，然后从您的照片中选择壁纸。

![LEDGER FLEX](assets/notext/38.webp)

您可以裁剪图片。

![LEDGER FLEX](assets/notext/39.webp)

从不同选项中选择一个对比度，然后点击 “*Confirm contrast*”。

![LEDGER FLEX](assets/notext/40.webp)

在您的 Flex 上，点击 “*Load picture*” 按钮。

![LEDGER FLEX](assets/notext/41.webp)

如果您对图片满意，点击 “*Keep*” 以将其设置为您的锁屏壁纸。

![LEDGER FLEX](assets/notext/42.webp)

最后，我们将添加比特币应用程序。为此，在 Ledger Live 上，点击 “*Bitcoin（BTC）*” 旁边的 “*Install*” 按钮。

![LEDGER FLEX](assets/notext/43.webp)

应用程序将安装在您的 Flex 上。

![LEDGER FLEX](assets/notext/44.webp)

从现在起，您不再需要使用 Ledger Live 软件来日常管理您的钱包。您可以偶尔使用它来更新固件（如有新版本）。其他所有操作，我们将使用 Sparrow Wallet，它是一款功能更全面的比特币钱包管理工具。

## 如何使用 Sparrow 设置新的比特币钱包？

打开 Sparrow Wallet，跳过介绍页面即可进入主页面。查看屏幕右下角的开关，确认您已正确连接到节点。

我强烈建议您使用自己的比特币节点。在本教程中，我使用公共节点（黄色），因为我使用测试网（testnet），但对于正常使用，最好选择本地的 Bitcoin Core（绿色）或连接到远程节点的 Electrum 服务器（蓝色）。

![LEDGER FLEX](assets/notext/45.webp)

点击 “*File*” 选单然后 “*New Wallet*”。

![LEDGER FLEX](assets/notext/46.webp)

为这个钱包选择一个名称，然后点击 “*Create Wallet*”。

![LEDGER FLEX](assets/notext/47.webp)

在 “*Script Type*” 下拉选单中，选择将用于保护您的比特币的脚本类型。我推荐选择 “*Taproot*”，如果不可用，选择 “*Native SegWit*”。

![LEDGER FLEX](assets/notext/48.webp)

点击 “*Connected Hardware Wallet*” 按钮。

![LEDGER FLEX](assets/notext/49.webp)

将您的 Ledger Flex 连接到电脑，用您的 PIN 码解锁它，然后打开 “*Bitcoin*” 应用程序。在本教程中，我使用的是 “*Bitcoin Testnet*” 应用程序，但主网的程序保持相同。

![LEDGER FLEX](assets/notext/50.webp)

在 Sparrow 上，点击 “*Scan*” 按钮。

![LEDGER FLEX](assets/notext/51.webp)

然后点击 “*Import Keystore*”。

![LEDGER FLEX](assets/notext/52.webp)

现在您可以看到您钱包的详细信息，包括您第一个账户的扩展公钥。点击 “*Apply*” 按钮以完成钱包的创建。

![LEDGER FLEX](assets/notext/53.webp)

为了确保访问 Sparrow Wallet 的安全，请选择一个强密码。这个密码将保护您在 Sparrow 上的钱包数据安全，帮助防止未经授权的访问您的公钥、地址、标签和交易历史。

我建议您将这个密码保存在密码管理器中，以免忘记。

![LEDGER FLEX](assets/notext/54.webp)

现在，您的钱包已经创建成功了！

![LEDGER FLEX](assets/notext/55.webp)
在钱包中接收您的第一笔比特币之前，我强烈建议您进行一次恢复测试。记下一个参考信息，比如您的 xpub，然后在钱包还空的时候重置您的 Ledger Flex。之后，尝试使用您的纸质备份在 Ledger 上恢复您的钱包。检查恢复后生成的 xpub 是否与您最初记下的一致。如果是这样，您就可以确信您的纸质备份是可靠的。

## 如何使用 Ledger Flex 接收比特币？

点击 “*Receive*” 标签。

![LEDGER FLEX](assets/notext/56.webp)

将您的 Ledger Flex 连接到电脑，输入 PIN 码以解锁，然后打开 “*Bitcoin*” 应用程序。

![LEDGER FLEX](assets/notext/57.webp)

在使用 Sparrow Wallet 提供的地址之前，请在您的 Ledger Flex 的屏幕上验证它。这种做法允许您确认 Sparrow 上显示的地址不是欺诈性的，并且 Ledger 确实持有以后使用这个地址保护的比特币所需的私钥。

为了进行这项验证，请点击 “*Display Address*” 按钮。

![LEDGER FLEX](assets/notext/58.webp)

确保您的 Ledger Flex 上显示的地址与 Sparrow Wallet 上指示的地址匹配。还建议在给发送者提供您的地址之前进行这项验证，以确保其有效性。

![LEDGER FLEX](assets/notext/59.webp)

您可以添加一个 “*Label*” 来描述将用这个地址保护的比特币的来源。这是一个好习惯，有助于您更好地管理您的 UTXO（未花费交易输出）。

![LEDGER FLEX](assets/notext/60.webp)

关于标签的更多信息，我还建议您查看这个教程：

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然后，您可以使用这个地址来接收比特币。

![LEDGER FLEX](assets/notext/61.webp)

## 如何使用 Ledger Flex 发送比特币？

现在您已经在您的 Flex 保护的钱包中收到了您的第一笔聪（比特币），您也可以消费它！将您的Ledger连接到电脑，解锁它，启动 Sparrow Wallet，然后前往 “*Send*” 标签以构建新的交易。

![LEDGER FLEX](assets/notext/62.webp)

如果您想进行“*币控制*”（Coin Control），即特定选择哪些 UTXO 在交易中消费，请前往 “*UTXOs*” 标签。选择您要消费的 UTXO，然后点击“*Send Selected*”。您将被重定向到 “*Send*” 标签的同一屏幕，但您的 UTXO 已为交易选择。

![LEDGER FLEX](assets/notext/63.webp)
输入目的地址。通过点击“*+ Add*” 按钮，您也可以输入多个地址。

![LEDGER FLEX](assets/notext/64.webp)

记下一个 “*Label*”，以记住这次支出的目的。

![LEDGER FLEX](assets/notext/65.webp)

选择发送到此地址的金额。

![LEDGER FLEX](assets/notext/66.webp)

调整您的交易费率以适应当前市场。

![LEDGER FLEX](assets/notext/67.webp)

确保您的交易设置正确无误，然后点击 “*Create Transaction*”。

![LEDGER FLEX](assets/notext/68.webp)

如果一切正确无误，请点击 “*Finalize Transaction for Signing*”。

![LEDGER FLEX](assets/notext/69.webp)

点击“*Sign*”。

![LEDGER FLEX](assets/notext/70.webp)

在您的 Ledger Flex 旁边点击 “*Sign*”。

![LEDGER FLEX](assets/notext/71.webp)

在您的 Flex 屏幕上验证交易设置，包括接收者的接收地址、发送金额和费用金额。

![LEDGER FLEX](assets/notext/72.webp)

为了签名，请长按 “*Hold to sign*” 按钮。

![LEDGER FLEX](assets/notext/73.webp)

您的交易现已签名。点击 “*Broadcast Transaction*” 将其广播到比特币网络上。

![LEDGER FLEX](assets/notext/74.webp)

您可以在 Sparrow Wallet 的 “*Transactions*” 标签中找到它。

恭喜您，现在您已经掌握了使用 Ledger Flex 与 Sparrow Wallet 的基本操作！在未来的教程中，我们将看到如何结合使用 Ledger Flex 和 Liana 来利用 Miniscript。

如果您觉得这个教程有帮助，我会非常感激您在下方点赞。欢迎在您的社交网络上分享这篇文章。非常感谢！
