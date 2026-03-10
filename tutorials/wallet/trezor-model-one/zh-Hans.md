---
name: Trezor Model One
description: 设置和使用 Trezor Model One 硬件钱包
---
![cover](assets/cover.webp)

*图片来源：[Trezor.io](https://trezor.io/)*

Trezor Model One 是首款硬件钱包，由 SatoshiLabs 于 2014 年发布。十多年过去了，它仍然是一个不错的选择，尤其适合那些既追求技术易用又注重预算的用户。事实上，它在 Trezor 官网上的售价为 49 欧元。在这个价位上，它是为数不多的硬件钱包之一。这款产品介于售价约 20 欧元的入门级设备（例如通常没有屏幕的 Tapsigner）和售价约 80 欧元的中端设备（例如 Ledger Nano S Plus 或 Trezor Safe 3）之间。

Model One 配备 0.96 英寸单色 OLED 显示屏和两个实体按键。它无需电池，仅通过 micro-USB 接口供电和传输数据。

![Image](assets/fr/01.webp)

Model One 的主要缺点是没有安全元件，这使其容易受到各种物理攻击，其中一些攻击相对容易实施。这些攻击可能包括分析辅助通道以确定设备 PIN 码，或者使用更高级的技术提取加密种子以便稍后进行暴力破解。请注意，这些攻击需要物理接触设备。但是，使用强密语 BIP39 可以显著降低这种漏洞。如果您选择这款硬件钱包，我强烈建议您设置一个密语。

Model One 具有两大优势：

- 它基于完全开源的架构。与配备安全元件的较新型号不同，Model One 的所有硬件和软件组件均可审计；

- 它配备屏幕。据我所知，它是市面上同价位唯一一款配备显示屏的硬件钱包。这是一项非常重要的功能，因为它能够验证签名信息和收款地址，从而有效防止多种网络攻击。

因​​此，Trezor Model One 对于预算有限的初学者和中级用户来说可能是一个明智的选择。然而，由于缺少安全元件，其物理防护能力存在一定的局限性，这一点需要注意。如果您的预算有限，这不失为一个好选择；但如果您预算充足，可以选择更高级的型号，例如售价 79 欧元的 Trezor Safe 3，因为它配备了安全元件。

## Trezor Model One 开箱

收到 Model One 后，请检查包装盒和封条是否完好无损，以确认包装未被打开。稍后设置设备时，系统还会进行软件验证，以确保设备的真实性和完整性。

包装盒内包含：

- Trezor Model One 智能手表；
- 用于记录助记词的卡片纸、贴纸和使用说明；
- USB-A 转 micro-USB 数据线。

![Image](assets/fr/02.webp)

使用设备非常简单：

- 右键单击​​确认并继续下一步；
- 使用鼠标左键返回上一步。

## 前提条件

在本教程中，我将向您演示如何将 Trezor Model One 与 [Sparrow Wallet 钱包管理软件](https://sparrowwallet.com/download/) 结合使用。如果您尚未安装该软件，请立即安装。如果您需要帮助，我们也有关于配置 Sparrow Wallet 的详细教程：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您还需要 Trezor Suite 软件来配置 Model One、检查其真伪和安装固件。我们将只使用该软件进行配置，之后只需进行固件更新。对于钱包的日常管理，我们将只使用 Sparrow Wallet，因为它针对比特币进行了优化，即使是初学者也很容易使用（Sparrow 只支持比特币，不支持其他货币）。

[从官方网站下载 Trezor Suite](https://trezor.io/trezor-suite)

![Image](assets/fr/03.webp)

强烈建议您在将这两个程序安装到您的电脑之前，先使用 GnuPG 检查其真实性，并通过哈希值验证其完整性。如果您不知道如何操作，可以参考以下教程：

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 启动 Trezor Model One

将您的 Model One 连接到已安装 Trezor Suite 和 Sparrow Wallet 的电脑。

![Image](assets/fr/04.webp)

打开 Trezor Suite，然后点击 "*Set up my Trezor*"。

![Image](assets/fr/05.webp)

选择 "*Bitcoin-only firmware*"，然后点击 "*Install Bitcoin-only*"。

![Image](assets/fr/06.webp)

Trezor Suite 将为您的 Model One 安装固件。安装过程中请稍候。

![Image](assets/fr/07.webp)

点击 "*Continue*"。

![Image](assets/fr/08.webp)

## 创建比特币钱包

在 Trezor Suite 上点击 "*Create new Wallet*" 按钮。

![Image](assets/fr/09.webp)

接受硬件钱包上的使用条款。

![Image](assets/fr/10.webp)

在 Trezor Suite 中，点击 “*Continue to backup*”。

![Image](assets/fr/11.webp)

该软件提供了关于如何管理助记词的说明。

这个助记符让您可以完全、不受限制地访问您的所有比特币。任何拥有此短语的人都可以窃取您的资金，即使没有实际访问您的 Trezor Model One 也是如此。

如果您的硬件钱包丢失、被盗或损坏，这 24 个单词的助记词可恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。

您可以将其写在包装盒中提供的纸板上，或者为了增加安全性，我建议将其刻在不锈钢底座上，以防止火灾、洪水或倒塌。

确认说明，然后点击 “*Create Wallet backup*” 按钮。

![Image](assets/fr/12.webp)

Model One 将使用其随机数生成器创建助记词。确保在此操作期间您没有受到监视。在您选择的物理介质上写下屏幕上提供的文字。根据您的安全策略，您可以考虑制作该短语的多个完整物理副本（但最重要的是，不要分割它）。保持单词编号并按顺序排列很重要。

**显然，您绝不能像我在本教程中那样在互联网上分享这些词。此示例钱包将仅在测试网上使用，并将在教程结束时删除**

关于保存和管理助记词短语的正确方法的更多信息，我强烈建议您阅读其他教程，特别是如果您是初学者：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

为了进入下一个单词，请点击右键。写下所有单词后，再次单击右键进入下一步。

![Image](assets/fr/13.webp)

您的硬件钱包再次向您展示您的所有言论。检查您是否已将它们全部写下来。

![Image](assets/fr/14.webp)

## 设置 PIN 码

接下来是 PIN 码步骤。 PIN 码可解锁您的 Trezor。因此，它可以防止未经授权的物理访问。此 PIN 码与钱包加密密钥的派生过程无关。因此，即使无法访问 PIN 码，拥有 12 个单词的助记词也能让您恢复比特币。

在 Trezor Suite 上，点击 “*Continue to PIN*”，然后点击 “*Set PIN*” 按钮。

![Image](assets/fr/15.webp)

在 Model One 硬件钱包上确认。

![Image](assets/fr/16.webp)

我们建议选择尽可能随机的 PIN 码。请务必将此代码保存在与 Trezor 存储位置不同的位置（例如密码管理器中）。您可以定义 8 到 50 位数字的 PIN 码。我建议您选择尽可能长的 PIN 码以增强安全性。

必须根据 Trezor Model One 上显示的键盘配置，通过单击与数字对应的点，在计算机上的 Trezor Suite 中输入 PIN 码。

每次解锁 Trezor Model One 时，无论是通过 Trezor Suite 还是 Sparrow Wallet，都需要这种特定的 PIN 输入方法。

![Image](assets/fr/17.webp)

完成后，点击 "*Enter PIN*" 按钮。

![Image](assets/fr/18.webp)

再次输入密码以确认。

![Image](assets/fr/19.webp)

在 Trezor Suite 上点击 "*Complete setup*" 按钮。

![Image](assets/fr/20.webp)

Model One 的配置工作现已完成。如果您愿意，可以更改 Hardware Wallet 的名称和主页。

![Image](assets/fr/21.webp)

我们将不再需要 Trezor Suite 软件，除非在您的硬件钱包上进行定期固件更新，或者您想运行恢复测试。我们现在将使用 Sparrow 来管理钱包，因为该软件非常适合仅使用比特币。

## 在 Sparrow Wallet 上设置钱包

首先，[从官方网站](https://sparrowwallet.com/) 在您的计算机上下载并安装 Sparrow Wallet（如果您尚未这样做）。

打开 Sparrow Wallet 后，请确保该软件已连接到比特币节点，该节点由界面右下角的勾号指示。如果您在连接 Sparrow 时遇到问题，我建议您查阅本教程的开头部分：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

点击 "*Files*" 选项卡，然后点击 "*New Wallet*"。

![Image](assets/fr/22.webp)

为您的钱包命名，然后点击 "*Create Wallet*"。

![Image](assets/fr/23.webp)

在 "*Script Type*" 下拉菜单中，选择用于保护比特币的脚本类型。我推荐使用 "*Taproot*"，如果不行，也可以使用 "*Native SegWit*"。

![Image](assets/fr/24.webp)

点击 "*Connected Hardware Wallet*" 按钮。当然，您的 Model One 必须与电脑连接。

![Image](assets/fr/25.webp)

点击 "*Scan*" 按钮。您的一号模型就会出现。

当您将 Model One 连接到已打开 Sparrow Wallet 的电脑时，系统会提示您在 Sparrow 中输入 BIP39 Passphrase（密语）。此高级选项将在后续教程中介绍。目前，您可以选择 “*Toggle passphrase Off*” 来阻止 Trezor 每次启动时都提示您输入密语。

https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)

点击 "*Import Keystore**"。

![Image](assets/fr/27.webp)

现在您可以看到 钱包的详细信息，包括第一个账户的扩展公钥。点击 "*Apply*" 按钮，完成钱包创建。

![Image](assets/fr/28.webp)

选择一个强密码来保护您对 Sparrow Wallet 的访问。此密码将确保您对 Sparrow Wallet 数据的安全访问，保护您的公钥、地址、标签和交易记录免受未经授权的访问。

我建议您将此密码保存在密码管理器中，以免忘记。

![Image](assets/fr/29.webp)

现在，您的钱包已被导入到 Sparrow Wallet 上！

![Image](assets/fr/30.webp)

收到第一笔比特币前，**我强烈建议您进行一次空钱包恢复测试**。记下一些参考信息，例如您的 xpub，然后在钱包为空的情况下重置您的 Trezor Model One。然后尝试使用纸质备份在 Trezor 上恢复您的钱包。检查恢复后生成的 xpub 是否与您最初记录的 xpub 一致。如果一致，您可以放心，您的纸质备份是可靠的。

为了了解有关如何执行恢复测试的更多信息，我建议您参考其他教程：

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Model One 接收比特币？

在 Sparrow 上，点击 "*Receive*" 选项卡。

![Image](assets/fr/31.webp)

在使用 Sparrow Wallet 提供的地址之前，请在您的 Trezor 屏幕上进行验证。这样做可以确认 Sparrow 上显示的地址并非虚假地址，并且硬件钱包确实持有用于花费该地址所保护的比特币的私钥。这有助于您避免多种类型的攻击。

网络进行此验证，请点击 “*Display Address*” 按钮。

![Image](assets/fr/32.webp)

请检查您的 Trezor 上显示的地址是否与 Sparrow Wallet 中的地址一致。建议您在将地址告知发送者之前进行此检查，以确保其有效性。您可以按右键确认。

![Image](assets/fr/33.webp)

您还可以添加一个 "*Label*"，以描述将用此地址保护的比特币来源。这是一个很好的做法，可以让您更好地管理您的 UTXO。

![Image](assets/fr/34.webp)

然后，您就可以用这个地址接收比特币。

![Image](assets/fr/35.webp)

## 如何使用 Trezor Model One 发送比特币？

现在您已在 Model One 保护的钱包中收到您的第一个比特币，您也可以使用它！将您的 Trezor 连接到电脑，启动 Sparrow Wallet，然后前往 “*Send*” 选项卡创建新交易。

![Image](assets/fr/36.webp)

如果您想要使用*币控制*，即指定要在交易中使用的 UTXO，请前往 “*UTXOs*” 选项卡。选择您要使用的 UTXO，然后点击 “*Send Selected*” 。您将被重定向到 “*Send*” 选项卡中的同一屏幕，但您选择的 UTXO 已预先选中用于交易。

![Image](assets/fr/37.webp)

输入地址。您也可以点击 "*+ Add*" 按钮以输入多个地址。

![Image](assets/fr/38.webp)

填写 "*Label*"（标签），以记住这笔费用的用途。

![Image](assets/fr/39.webp)

选择要发送到此地址的金额。

![Image](assets/fr/40.webp)

根据当前市场调整交易费率。例如，您可以使用 [Mempool.space](https://Mempool.space/)，选择合适的费率。

确保所有交易参数正确无误，然后点击 "*Create Transaction*"。

![Image](assets/fr/41.webp)

如果一切都已正确无误，请点击 "*Finalize Transaction for Signing*"。

![Image](assets/fr/42.webp)

点击 "*Sign*"。

![Image](assets/fr/43.webp)

点击 Trezor Model One 旁边的 "*Sign*"。

![Image](assets/fr/44.webp)

检查硬件钱包屏幕上的交易参数，包括收款人的接收地址、发送金额和手续费。Trezor 验证交易后，右键单击进行签名。

![Image](assets/fr/45.webp)

您的交易已签名。再次确认一切无误后，点击 “*Broadcast Transaction*” 按钮将其广播到比特币网络。

![Image](assets/fr/46.webp)

您可以在 Sparrot Wallet 的 "*Transactions*" 选项卡中找到它。

![Image](assets/fr/47.webp)

恭喜您，现在您已经掌握了 Trezor Model One 与 Sparrow Wallet 的基本用法！为了更进一步了解，我推荐这篇关于如何使用 Trezor 硬件钱包和 BIP39 Passphrase（密语）来加强安全性的全面教程：

https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您觉得这篇教程有用，请在下方点个赞。欢迎在社交网络上分享这篇文章。非常感谢！
