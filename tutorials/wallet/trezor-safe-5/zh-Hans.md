---
name: Trezor Safe 5
description: 配置和使用 Safe 5 硬件钱包
---
![cover](assets/cover.webp)

*图片来源：[Trezor.io](https://trezor.io/)*

Trezor Safe 5 是由 SatoshiLabs 设计并于 2024 年发布的最新一代硬件钱包。它定位为 Safe 3 的高端版本，注重人体工学设计和耐用性。与 Model One 和 Model T 相比，它继承了 Safe 3 的所有安全优势。

Safe 5 的售价为 169 欧元，定位为高端硬件钱包，与 Coldcard、Ledger Nano X 和 Flex、Jade Plus、Passport 和 Bitbox 等产品展开竞争。

Safe 5 的亮点在于其 1.54 英寸彩色触摸屏，采用康宁第三代大猩猩玻璃（*Gorilla Glass 3*）保护，具有出色的抗冲击和防刮擦性能。它还配备了 Trezor Touch 触觉引擎，触摸时会发出轻微震动反馈。与 Safe 3 一样，它也内置安全元件，并通过 USB-C 接口供电，此外还增加了一个 Micro SD 卡槽。

Safe 5 与 Safe 3 的主要区别在于设备品质，而非安全性。Safe 5 显著提升了用户体验，操作更加流畅，屏幕也更加舒适。在安全性方面，两者不相上下。

![Image](assets/fr/01.webp)

Safe 5 具备优秀硬件钱包应有的所有基本功能，包括对 BIP39 密码短语的出色集成。但目前尚不支持 Miniscript。

这款产品尤其适合初学者和中级用户。另一方面，对于寻求Coldcard等设备所具备的更特定功能的高级用户而言，Trezor Safe 5可能无法满足他们的所有期望。不过，如果您不需要这些高级功能，Trezor Safe 5或许是一个绝佳的选择。

## Trezor Safe 5 安全型号

与 Safe 3一样，Trezor Safe 5 配备了 EAL6+ 认证的**安全元件**，相比之前的 Model One 和 Model T 等型号，这是一个显著的进步。该安全元件采用 OPTIGA Trust M V3 芯片，它并不直接存储种子，而是作为加密组件来保护种子的访问安全。安全元件会保存一个秘密信息，只有在用户正确输入 PIN 码后才能访问。然后，该秘密信息用于解密存储在设备主内存中的加密种子。

这种混合安全系统提供了更强大的物理保护，尤其能够有效抵御提取攻击或侵入式分析，而 Model One 恰恰容易受到这些问题的困扰，尤其是在 PIN 码管理方面。由于使用了安全元件，这些漏洞现在已被规避。该模型还保持了开源软件架构：管理私钥生成和使用的代码完全可访问且可验证。OPTIGA 芯片仅管理 PIN 码，PIN 码是比特币钱包密钥管理之外的一个元素。它仅限于发布一个可用于解密种子的秘密信息。此外，OPTIGA Trust M V3 芯片受益于相对宽松的许可协议，该协议授权 SatoshiLabs 可以自由发布潜在漏洞（无需签署保密协议）。

在我看来，这种安全模型是目前市场上最佳的折衷方案之一。它结合了安全元件和开源软件管理的优势。以前，用户必须在芯片带来的增强物理安全性和开源带来的透明度之间做出选择；而使用 Trezor Safe，您可以同时受益于两者。

在本教程中，您将学习如何安全地配置和使用您的 Trezor Safe 5。

## Trezor Safe 5 开箱

收到 Safe 5 后，请检查包装盒和封条是否完好无损，以确认包装未被打开。稍后设置设备时，系统也会进行软件验证，以确认设备的真伪和完整性。

包装盒内包含：

- Trezor Safe 5；
- 一个包含卡片（用于记录助记词）、贴纸和使用说明的收纳袋；
- USB-C 转 USB-C 数据线。

打开包装后，Trezor Safe 5 应由保护塑料膜包裹，USB-C 接口应贴有全息防伪标签。请确认标签完好无损。

![Image](assets/fr/02.webp)

设备上的导航操作相当直观：

- 轻触屏幕下半部分即可前进；
- 向下滑动即可返回；
- 长按屏幕以确认操作。

## 前提条件

在本教程中，我将向您展示如何将 Trezor Safe 5 与 [Sparrow Wallet 钱包管理软件](https://sparrowwallet.com/download/) 配合使用。如果您尚未安装此软件，请立即安装。如果您需要帮助，我们还提供了关于配置 Sparrow Wallet 的详细教程：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您还需要 Trezor Suite 软件来配置 Safe 5、验证其真伪并安装固件。我们将仅使用此软件进行这些操作，之后它仅用于固件更新。对于钱包的日常管理，我们将完全使用 Sparrow Wallet，因为它针对比特币进行了优化，并且易于使用，即使是新手也能轻松上手（Sparrow 仅支持比特币，不支持其他加密货币）。

[从官方网站下载 Trezor Suite](https://trezor.io/trezor-suite)

![Image](assets/fr/03.webp)

对于这两个程序，我强烈建议您在安装到您的计算机之前，先使用 GnuPG 验证其真伪，并通过哈希值验证其完整性。如果您不知道如何操作，可以参考以下教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 启动 Trezor Safe 5

将您的 Safe 5 连接到已安装 Trezor Suite 和 Sparrow Wallet 的电脑。

![Image](assets/fr/04.webp)

打开 Trezor Suite，然后点击 “*Set up my Trezor*”。

![Image](assets/fr/05.webp)

选择 "*Bitcoin-only firmware*"，然后点击 "*Install Bitcoin-only*"。

![Image](assets/fr/06.webp)

Trezor Suite 将在您的 Safe 5 上安装固件。请耐心等待安装完成。

![Image](assets/fr/07.webp)

点击 "*Continue*"。

![Image](assets/fr/08.webp)

然后进行真伪验证，确保您的硬件钱包不是假货或已被盗用。

![Image](assets/fr/09.webp)

在您的 Safe 5 上，按下屏幕进行确认。

![Image](assets/fr/10.webp)

如果您的 Trezor 是正品，Trezor Suite 中将显示确认信息。

![Image](assets/fr/11.webp)

然后，您就可以跳过有基本操作说明的窗口。

![Image](assets/fr/12.webp)

## 创建比特币钱包

在 Trezor Suite 上点击 "*Create new Wallet*" 按钮。

![Image](assets/fr/13.webp)

为了创建标准的 BIP39 钱包，首先从下拉选单中选择 “*Legacy Wallet backup types*”，然后选择 12 个单词或 24 个单词的助记词（目前建议使用 12 个单词）。这将使您能够创建一个经典的单签名钱包。我建议您在此处选择符合 BIP39 标准的参数，以便于恢复并避免被限制在特定环境中。最后，点击 “*Create Wallet*”。

如果您想了解 Trezor 上提供的其他备份选项，包括 “Multi-share Backup”，我建议您也参考此教程：

https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/14.webp)

接受硬件钱包上的使用条款。

![Image](assets/fr/15.webp)

长按屏幕可创建新的钱包。

![Image](assets/fr/16.webp)

在 Trezor Suite 中，点击 "*Continue to backup*"。

![Image](assets/fr/17.webp)

该软件会提供如何管理助记词的说明。

此助记词赋予您对所有比特币的完全、无限制访问权限。任何拥有此助记词的人都可以窃取您的资金，即使他们无法实际接触到您的 Trezor Safe 5。

如果您的硬件钱包丢失、被盗或损坏，这 12 个单词的助记词可以恢复您对比特币的访问权限。因此，务必妥善保存并将其存放在安全的地方。

您可以将其写在包装盒内提供的纸板上，或者为了更加安全，我建议您将其刻在不锈钢底座上，以防止火灾、洪水或跌落造成的损坏。

确认说明，然后点击 “*Create Wallet backup*” 按钮。

![Image](assets/fr/18.webp)

Safe 5 将使用其随机数生成器生成您的助记词。请确保在此过程中无人监视。将屏幕上显示的单词写在您选择的物理介质上。根据您的安全策略，您可以考虑制作几份完整的助记词纸质副本（但最重要的是，不要将其分割）。务必保持助记词编号并按顺序排列。

**显然，您绝不能像我在本教程中那样在互联网上分享这些助记词。此示例钱包仅在测试网上使用，并将在本教程结束后删除。**

关于如何正确保存和管理助记词的更多信息，我强烈建议您参考以下教程，尤其如果您是初学者：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)

为了看下一个助记词，请点击屏幕底部。您可以通过向下滑动来返回上一个助记词。写下所有单词后，按住屏幕继续下一步。

![Image](assets/fr/20.webp)

按顺序选择助记词组中的每个单词，确认您已正确记录。

![Image](assets/fr/21.webp)

确认无误后，点击屏幕继续。

![Image](assets/fr/22.webp)

## 设置 PIN 码

接下来是设置 PIN 码的步骤。PIN 码用于解锁您的 Trezor 钱包，从而防止未经授权的物理访问。此 PIN 码与钱包加密密钥的生成过程无关。因此，即使您无法获取 PIN 码，只要拥有您的 12 个单词的助记词，即可重新访问您的比特币。

在 Trezor Suite 中，点击 “*Continue to PIN*”，然后点击 “*Set PIN*” 按钮。

![Image](assets/fr/23.webp)

使用 Safe 5 进行确认。

![Image](assets/fr/24.webp)

我们建议您选择一个尽可能随机的 PIN 码。请务必将此 PIN 码保存在与 Trezor 钱包不同的位置（例如，密码管理器）。您可以设置 8 到 50 位数字的 PIN 码。为了提高安全性，我建议您设置一个尽可能长的 PIN 码。

​​使用触摸板输入您的 PIN 码。

![Image](assets/fr/25.webp)

完成后，点击右下角的绿色对勾，然后再次确认您的 PIN 码。

![Image](assets/fr/26.webp)

您的 PIN 码已注册。

![Image](assets/fr/27.webp)

在 Trezor Suite 上点击 "*Complete setup*" 按钮。

![Image](assets/fr/28.webp)

您的 Safe 5 配置现已完成。您可以根据需要更改硬件钱包的名称和主页。

![Image](assets/fr/29.webp)

除了定期更新硬件钱包固件或进行恢复测试外，我们将不再需要 Trezor Suite 软件。现在我们将使用 Sparrow 来管理钱包，因为这款软件非常适合仅用于比特币交易。

## 在 Sparrow Wallet 上设置钱包

首先，如果您尚未安装 Sparrow Wallet，请[从官方网站](https://sparrowwallet.com/)下载并安装到您的计算机上。

打开 Sparrow Wallet 后，请确保该软件已连接到比特币节点，连接成功后，界面右下角会显示一个勾号。如果您在连接 Sparrow 时遇到问题，建议您参考本教程的开头部分：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

点击 "*File*" 选项卡，然后点击 "*New Wallet*"。

![Image](assets/fr/30.webp)

为您的钱包命名，然后点击 "*Create Wallet*"。

![Image](assets/fr/31.webp)

在 "*Script Type*" 下拉选单中，选择用于保护比特币的脚本类型。我推荐使用 "*Taproot*"，如果不行，也可以使用 "*Native SegWit*"。

![Image](assets/fr/32.webp)

点击 "*Connected Hardware Wallet*" 按钮。当然，您的 Safe 5 必须连接到电脑并解锁。

当您将 Safe 5 连接到已打开 Sparrow Wallet 的电脑时，硬件钱包界面会提示您输入 BIP39 Passphrase（密语）。此高级选项将在后续教程中介绍。目前，您可以直接点击右上角的绿色勾号，确认使用空密语（即不设置密语）。为避免 Trezor 每次启动时都要求您输入密码短语，请打开 Trezor Suite，进入设置，将 "*Device*" > "*Wallet default*" 中的 "*passphrase*" 选项更改为 "*Standard*"。

![Image](assets/fr/33.webp)

点击 "*Scan*"按钮。您的 Safe 5 应该会出现。点击 "*Import Keystore*"。

![Image](assets/fr/34.webp)

现在您可以看到钱包的详细信息，包括第一个账户的扩展公钥。点击 "*Apply*"按钮以完成创建钱包。

![Image](assets/fr/35.webp)

选择一个强大的密码以确保对 Sparrow Wallet 的访问安全。该密码将确保安全访问您的 Sparrow Wallet 数据，保护您的公钥、地址、标签和交易历史记录免遭未经授权的访问。

我建议您将此密码保存在密码管理器中，以免忘记。

![Image](assets/fr/36.webp)

现在，您的钱包已被导入到 Sparrow Wallet 中！

![Image](assets/fr/37.webp)

在您收到第一笔比特币之前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，例如您的 xpub，然后在钱包为空的情况下重置您的 Trezor Safe 5。然后尝试使用纸质备份在 Trezor 上恢复您的钱包。检查恢复后生成的 xpub 是否与您最初记录的 xpub 一致。如果一致，您可以放心，您的纸质备份是可靠的。

为了了解更多关于如何进行恢复测试的信息，我建议您参考以下教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Safe 5 接收比特币？

在 Sparrow 中，点击 “*Receive*” 选项卡。

![Image](assets/fr/38.webp)

在使用 Sparrow Wallet 提供的地址之前，请在 Trezor 的屏幕上进行验证。这样做可以确认 Sparrow 显示的地址并非虚假地址，并且硬件钱包确实持有用于花费该地址所保护的比特币的私钥。这有助于您避免多种类型的攻击。

为了进行此验证，请点击 “*Display Address**” 按钮。

![Image](assets/fr/39.webp)

检查 Trezor 上显示的地址是否与 Sparrow Wallet 中的地址一致。建议您在将地址告知发送者之前进行此验证，以确保其有效性。您可以点击屏幕进行确认。

![Image](assets/fr/40.webp)

然后，您可以添加一个 “*Label*”（标签）来描述将使用此地址保护的比特币的来源。这是一个良好的实践，可以帮助您更好地管理您的 UTXO（未花费交易输出）。

![Image](assets/fr/41.webp)

然后，您可以使用此地址接收比特币。

![Image](assets/fr/42.webp)

## 如何使用 Trezor Safe 5 发送比特币？

现在，您已在 Safe 5 保护的钱包中收到了您的第一个聪（比特币），您也可以使用它们了！将您的 Trezor 连接到您的计算机，使用 PIN 码解锁，启动 Sparrow Wallet，然后转到 “*Send*” 选项卡以创建新的交易。

![Image](assets/fr/43.webp)

如果您想要进行*币控制*（Coin Control），即在交易中具体选择消耗哪些 UTXO，请前往 "*UTXOs*" 选项卡。选择要消费的 UTXO，然后点击 "*Send Selected*"。您将跳前往 "*Send*" 选项卡中的同一界面，但已为交易选择了 UTXO。

![Image](assets/fr/44.webp)

输入接收者的地址。您也可以点击 “+ Add” 按钮输入多个地址。

![Image](assets/fr/45.webp)

添加 "*Label*"（标签），以记住这笔支出的用途。

![Image](assets/fr/46.webp)

选择要发送到此地址的金额。

![Image](assets/fr/47.webp)

根据当前市场情况调整您的交易手续费率。例如，您可以使用 [Mempool.space](https://Mempool.space/) 选择合适的费率。

确保所有交易参数均正确，然后点击 “*Create Transaction*”。

![Image](assets/fr/48.webp)

如果一切都正确无误，请点击 "*Finalize Transaction for Signing*"。

![Image](assets/fr/49.webp)

点击 "*Sign*"。

![Image](assets/fr/50.webp)

点击 Trezor Safe 5 旁边的 "*Sign*" 按钮。

![Image](assets/fr/51.webp)

在您的硬件钱包屏幕上检查交易参数，包括收款人的接收地址、发送金额和手续费。交易在 Trezor 上验证通过后，按住屏幕进行签名。

![Image](assets/fr/52.webp)

您的交易现已签名。请再次确认一切无误，然后点击 “*Broadcast Transaction*” 将其广播到比特币网络上。

![Image](assets/fr/53.webp)

您可以在 Sparrow Wallet 的 “*Transactions*” 标签页中找到它。

![Image](assets/fr/54.webp)

恭喜！您现在已经掌握了 Trezor Safe 5 与 Sparrow Wallet 的基本使用方法！为了更进一步，我推荐这篇关于如何使用 Trezor 硬件钱包和 BIP39 Passphrase（密语）来增强安全性的全面教程：

https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您觉得这篇教程有用，请在下方点个赞。欢迎在社交网络上分享这篇文章。非常感谢！
