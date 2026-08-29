---
name: Trezor Safe 3
description: 配置和使用 Safe 3 硬件钱包
---
![cover](assets/cover.webp)

*图片来源：[Trezor.io](https://trezor.io/)*

Trezor Safe 3 是一款由 SatoshiLabs 设计并于 2023 年推出的硬件钱包。它非常小巧轻便（仅重 14 克），专为初学者和中级用户设计。它是广受欢迎的 Model One 的升级版，在保留品牌开源理念的同时，进行了多项重大改进，这使其区别于主要竞争对手 Ledger。Safe 3 的售价为 79 欧元。因此，它定位在中端硬件钱包市场，直接与 Ledger Nano S Plus 竞争。

Safe 3 没有电池，完全通过 USB-C 接口供电和通信。它配备了一块 0.96 英寸的单色 OLED 显示屏和两个实体按键。

![Image](assets/fr/01.webp)

Safe 3 具备优秀硬件钱包应有的所有基本功能，包括对 BIP39 Passphrase（密语）的出色集成。不过，它目前尚不支持 Miniscript。

这款钱包特别适合初学者，甚至可能是我推荐给新用户的硬件钱包。它也同样适合中级用户。另一方面，对于寻求更专业功能的高级用户（例如 Coldcard 等设备提供的功能），它可能无法满足他们的需求。但是，如果您不需要这些高级功能，Trezor Safe 3 或许是一个绝佳的选择。

## Trezor Safe 3 的安全特性

Trezor Safe 3 现在配备了 EAL6+ 认证的**安全元件**，相比之前的 Model One 和 Model T 等型号，这是一个显著的进步。该安全元件是 OPTIGA Trust M V3 芯片，它不直接存储种子，而是作为加密组件来保护种子访问的安全。安全元件会保存一个秘密信息，只有在用户正确输入 PIN 码后才能访问。该秘密信息随后用于解密存储在设备主内存中的加密种子。

这种混合安全系统提供了更强大的物理保护，尤其能够抵御提取攻击或侵入式分析。Model One 曾深受这些问题的困扰，尤其是在 PIN 码管理方面。如今，由于使用了安全元件，这些漏洞得以规避。此外，该型号还采用了开源软件架构：管理私钥生成和使用的代码完全可访问且可验证。OPTIGA 芯片仅管理 PIN 码，PIN 码是比特币钱包密钥管理之外的一个独立元素。它只发布一个可用于解密种子的秘密信息。此外，OPTIGA Trust M V3 芯片采用相对宽松的许可协议，授权 SatoshiLabs 可以自由发布潜在的漏洞。

在我看来，这种安全模型是目前市场上最佳的折衷方案之一。它结合了安全元件和开源软件管理的优势。以前，用户必须在芯片增强的物理安全性和开源的透明度之间做出选择；而 Trezor Safe 3 则让您可以同时享受两者的优势。

在本教程中，我们将向您展示如何安全地设置和使用 Trezor Safe 3。

## Trezor Safe 3 开箱

收到 Safe 3 后，请检查包装盒和封条是否完好无损，以确认包装未被打开。稍后设置设备时，系统也会进行软件验证，以确认设备的真实性和完整性。

包装盒内包含：
- Trezor Safe 3；
- 一个包含卡片（用于记录助记词）、贴纸和使用说明的收纳袋；
- USB-C 转 USB-C 数据线。

![Image](assets/fr/02.webp)

打开包装后，您的 Trezor Safe 3 应该由保护塑料膜包裹，USB-C 端口应该由全息防伪封条保护。确保它在那里。

![Image](assets/fr/03.webp)

设备上的导航非常简单：使用右键向右滚动，使用左键向左滚动。同时按下两个按钮即可确认操作。

![Image](assets/fr/04.webp)

## 前提条件

在本教程中，我将向您展示如何将 Trezor Safe 3 与 [Sparrow Wallet 钱包管理软件](https://sparrowwallet.com/download/) 配合使用。如果您尚未安装此软件，请立即安装。如果您需要帮助，我们还提供了一份关于配置 Sparrow Wallet 的详细教程：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您还需要 Trezor Suite 软件来配置 Safe 3、检查真伪和安装固件。我们将只使用该软件，之后只需进行固件更新。对于 Wallet 的日常管理，我们将只使用 Sparrow Wallet，因为它针对 Bitcoin 进行了优化，即使是初学者也很容易使用（Sparrow 只支持 Bitcoin，不支持其他币）。

[从官方网站下载 Trezor Suite](https://trezor.io/trezor-suite)

![Image](assets/fr/05.webp)

对于这两个程序，我强烈建议您在安装到电脑之前，先使用 GnuPG 检查其真实性，并通过哈希值验证其完整性。如果您不知道如何操作，可以参考以下教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 启动 Trezor Safe 3

将您的 Safe 3 连接到已安装 Trezor Suite 和 Sparrow Wallet 的电脑。

![Image](assets/fr/06.webp)

打开 Trezor Suite，然后点击 "*Set up my Trezor*"。

![Image](assets/fr/07.webp)

选择 "*Bitcoin-only firmware*"，然后点击 "*Install Bitcoin-only*"。

![Image](assets/fr/08.webp)

Trezor Suite 将在 Safe 3 上安装固件。安装过程中请稍候。

![Image](assets/fr/09.webp)

点击 "*Continue*"。

![Image](assets/fr/10.webp)

然后进行真伪验证，确保您的硬件钱包不是假货或已被盗用。

![Image](assets/fr/11.webp)

在 Safe 3 上按右键以确认。

![Image](assets/fr/12.webp)

如果您的 Trezor 是正品，Trezor Suite 中将显示确认信息。

![Image](assets/fr/13.webp)

之后您可以跳过包含基本操作说明的窗口。

![Image](assets/fr/14.webp)

## 创建比特币钱包

在 Trezor Suite 中，点击 “Create new Wallet” 按钮。

![Image](assets/fr/15.webp)

对于标准钱包，您可以选择默认备份类型。这将创建一个经典的单签名钱包，并带有 12 个单词的助记词。点击 “Create Wallet”。

如果您想了解 Trezor 上提供的其他备份选项，包括 “Multi-share Backup”，我建议您也参考这篇教程：

https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)

接受硬件钱包的使用条款。

![Image](assets/fr/17.webp)

再次按下右键创建新钱包。

![Image](assets/fr/18.webp)

在 Trezor Suite 中，点击 “*Continue to backup*”。

![Image](assets/fr/19.webp)

该软件会提供关于如何管理助记词的说明。

此助记词赋予您对所有比特币的完全、无限制访问权限。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Trezor Safe 3。

如果您的硬件钱包丢失、被盗或损坏，这 12 个单词的助记词可以恢复您对比特币的访问权限。因此，务必妥善保存并将其存放在安全的地方。

您可以将其写在包装盒内提供的纸板上，或者为了更安全，我建议您将其刻在不锈钢底座上，以保护其免受火灾、洪水或倒塌的损害。

确认说明后，点击 “*Create Wallet backup*” 按钮。

![Image](assets/fr/20.webp)

Safe 3 将使用其随机数生成器生成您的助记词。请确保在此过程中无人监视。将屏幕上显示的单词写在您选择的物理介质上。根据您的安全策略，您可以考虑制作几份完整的助记词副本（但最重要的是，不要将其拆分）。务必保持单词编号并按顺序排列。

**显然，您绝不能像我在本教程中那样在互联网上分享这些单词。此示例钱包仅在测试网上使用，教程结束后将被删除**

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)

为了继续输入下一个单词，请点击右键。点击左键可以返回上一步。记下所有单词后，按住右键进入下一步。

![Image](assets/fr/22.webp)

按照顺序选择助记词的单词，以确认您已正确记录。使用左右键在不同选项之间切换，然后同时点击两个按钮选择正确的单词。

![Image](assets/fr/23.webp)

完成验证程序后，点击右侧的按钮。

![Image](assets/fr/24.webp)

## 设置 PIN 码

接下来是设置 PIN 码的步骤。PIN 码用于解锁您的 Trezor 设备，从而防止未经授权的物理访问。此 PIN 码不参与钱包加密密钥的生成。即使无法获取 PIN 码，只要拥有您的 12 个单词的助记词，您就能重新访问您的比特币。

在 Trezor Suite 中，点击“*继续输入 PIN 码*”，然后点击“*设置 PIN 码*”按钮。

![Image](assets/fr/25.webp)

使用 Safe 3 进行确认。

![Image](assets/fr/26.webp)

我们建议您选择一个尽可能随机的 PIN 码。请务必将此 PIN 码保存在与 Trezor 设备不同的位置（例如，密码管理器）。您可以设置 8 到 50 位的 PIN 码。为了提高安全性，我建议您选择尽可能长的 PIN 码。

​​使用左右按钮选择每个数字。要确认您的选择并继续选择下一个数字，请同时按下左右按钮。

![Image](assets/fr/27.webp)

完成后，点击数字开头的 “*ENTER*” 勾号，然后再次确认您的 PIN 码。

![Image](assets/fr/28.webp)

您的 PIN 码已注册。

![Image](assets/fr/29.webp)

在 Trezor Suite 中，点击 “*Complete setup*” 按钮。

![Image](assets/fr/30.webp)

您的 Safe 3 配置现已完成。您可以根据需要更改硬件钱包的名称和主页。

![Image](assets/fr/31.webp)

您需要定期更新硬件钱包固件或进行恢复测试，否则我们将不再需要 Trezor Suite 软件。现在我们将使用 Sparrow 来管理钱包，因为这款软件非常适合仅用于比特币交易。

## 在 Sparrow Wallet 上设置钱包

首先，如果您尚未安装 Sparrow Wallet，请从官方网站 (https://sparrowwallet.com/) 下载并安装到您的计算机上。

打开 Sparrow Wallet 后，请确保软件已连接到比特币节点，连接成功后，界面右下角会显示一个勾号。如果您在连接 Sparrow 时遇到问题，建议您阅读以下教程的开头部分：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

点击 "*File*" 选项卡，然后点击 "*New Wallet*"。

![Image](assets/fr/32.webp)

为您的钱包命名，然后点击 "*Create Wallet*"。

![Image](assets/fr/33.webp)

在 "*Script Type*" 下拉选单中，选择用于保护比特币的脚本类型。我推荐使用 "*Taproot*"，如果不行，也可以使用 "*Native SegWit*"。

![Image](assets/fr/34.webp)

点击 "*Connected Hardware Wallet*" 按钮。当然，您的 Safe 3 必须连接到计算机并解锁。

![Image](assets/fr/35.webp)

点击 "*Scan*"按钮。您的 Safe 3 应该会出现。点击 "*Import Keystore*"。

![Image](assets/fr/36.webp)

现在您可以查看钱包的详细信息，包括您第一个账户的扩展公钥。点击 “*Apply*” 按钮完成钱包创建。

![Image](assets/fr/37.webp)

选择一个强密码来保护您对 Sparrow Wallet 的访问。此密码将确保您对 Sparrow Wallet 数据的安全访问，保护您的公钥、地址、标签和交易记录免受未经授权的访问。

我建议您将此密码保存在密码管理器中，以免忘记。

![Image](assets/fr/38.webp)

现在，您的钱包已被导入到 Sparrow Wallet！

![Image](assets/fr/39.webp)

在您收到钱包中的第一个比特币之前，**我强烈建议您执行一次空钱包恢复测试**。记下一些参考信息，例如您的 xpub，然后在钱包为空的情况下重置您的 Trezor Safe 3。然后尝试使用您的纸质备份在 Trezor 上恢复您的钱包。检查恢复后生成的 xpub 是否与您最初记录的 xpub 一致。如果一致，您可以放心，您的纸质备份是可靠的。

为了了解更多关于如何执行恢复测试的信息，我建议您参考以下教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Safe 3 接收比特币？

在 Sparrow 中，点击 “*Receive*” 选项卡。

![Image](assets/fr/40.webp)

为了使用 Sparrow Wallet 提供的地址之前，请先在您的 Trezor 硬件钱包屏幕上进行验证。此操作可确保您在 Sparrow 上看到的地址并非欺诈地址，并且您的硬件钱包确实持有用于后续花费该地址所保护的比特币的私钥。这有助于您避免多种类型的攻击。

要执行此验证，请点击 “*Display Address*” 按钮。

![Image](assets/fr/41.webp)

检查您的 Trezor 硬件钱包上显示的地址是否与 Sparrow Wallet 中的地址一致。建议您在将地址告知发送方之前进行此验证，以确保其有效性。您可以使用按钮进行确认。

![Image](assets/fr/42.webp)

然后，您可以添加 “*Label*”（标签）来描述将使用此地址保护的比特币的来源。这是一个有助于您更好地管理 UTXO（未花费交易输出）的好习惯。

![Image](assets/fr/43.webp)

然后您可以使用此地址接收比特币。

![Image](assets/fr/44.webp)

## 如何使用 Trezor Safe 3 发送比特币？

现在您已在 Safe 3 安全钱包中收到您的第一个聪（比特币），您也可以使用它！将您的 Trezor 连接到电脑，使用 PIN 码解锁，启动 Sparrow Wallet，然后转到 “*Send*” 选项卡创建新交易。

![Image](assets/fr/45.webp)

如果您希望进行 “币控制”（Coin Control），即选择要在交易中使用的特定 UTXO，请转到“*UTXOs*” 选项卡。选择您要使用的 UTXO，然后点击 “*Send Selected*”。您将被重定向到 “*Send*” 选项卡中的同一屏幕，但您的 UTXO 已预先选中用于交易。

![Image](assets/fr/46.webp)

输入接收地址。您也可以点击 “*+Add*” 按钮输入多个地址。

![Image](assets/fr/47.webp)

添加 "*Label*"，以记住这笔费用的用途。

![Image](assets/fr/48.webp)

选择要发送到该地址的金额。

![Image](assets/fr/49.webp)

根据当前市场调整交易手续费率。例如，您可以使用 [Mempool.space](https://Mempool.space/) 选择合适的费率。

确保所有交易参数正确无误，然后点击 "*Create Transaction*"。

![Image](assets/fr/50.webp)

如果一切正确无误，请点击 "*Finalize Transaction for Signing*"。

![Image](assets/fr/51.webp)

点击 "*Sign*"。

![Image](assets/fr/52.webp)

点击 Trezor Safe 3 旁边的 "*Sign*"。

![Image](assets/fr/53.webp)

检查 Hardware Wallet 屏幕上的交易参数，包括收件人的接收 Address、发送金额和费用。在 Trezor 上验证交易后，同时点击两个按钮进行签名。

![Image](assets/fr/54.webp)

您的交易已签名。请再次确认一切无误，然后点击 “*Broadcast Transaction*” 将其广播到比特币网络上。

![Image](assets/fr/55.webp)

您可以在 Sparrow Wallet 的 “*Transactions*” 标签页中找到它。

![Image](assets/fr/56.webp)

恭喜！您现在已经掌握了 Trezor Safe 3 与 Sparrow Wallet的基本使用方法！为了更进一步了解，我推荐这篇关于如何使用 Trezor 硬件钱包和 BIP39 Passphrase（密语）来增强安全性的全面教程：

https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您觉得这篇教程有用，请在下方点个赞。欢迎在社交网络上分享这篇文章。非常感谢！
