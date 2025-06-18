---
name: Trezor Safe 5
description: 配置和使用 Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*图片来源：[Trezor.io](https://trezor.io/)*



Trezor Safe 5 是中本聪实验室设计的最新一代 Hardware Wallet，于 2024 年推出。它定位为 Safe 3 的高端版本，注重人体工程学和耐用性。与前代产品 Safe 3 相比，它在安全方面取得了与 Model One 和 Model T 相同的进步。



Safe 5 定位于高端 Hardware Wallet 类别，售价为 169 欧元，竞争对手包括 Coldcard、Ledger Nano X 和 Flex、Jade Plus、Passport 和 Bitbox。



Safe 5 的与众不同之处在于其 1.54 英寸彩色触摸屏，该屏幕由*大猩猩 3* 玻璃保护，具有抗震和防划伤功能。它还配备了*Trezor Touch*触觉引擎，触摸时会发出轻微的震动。与 Safe 3 一样，它采用了安全元件，通过 USB-C 连接操作，并增加了一个 Micro SD 端口。



除了安全方面， Safe 3 和 Safe 5 的主要区别在于设备的质量。它大大改善了用户体验，操作更流畅，屏幕更舒适。在安全性方面，两者不相上下。



![Image](assets/fr/01.webp)



Safe 5 拥有优秀的 Hardware Wallet 所应具备的所有基本功能，包括 passphrase BIP39 的出色集成。不过，它还不支持 Miniscript。



该机型特别适合初学者和中级用户使用。另一方面，它可能无法满足高级用户对 Coldcard 等设备上更多特殊功能的期望。不过，如果你不需要这些高级选项，Trezor Safe 5 可能是个不错的选择。



## Trezor Safe 5 安全模式



与 Safe 3 一样，Trezor Safe 5 也配备了通过 EAL6+ 认证的**安全元件**，这是对早期型号（如 Model One 和 Model T）的重大改进。这是 OPTIGA Trust M V3 芯片，它不直接存储 seed，而是作为加密组件，确保对其访问的安全性。安全元件保留了一个只有在用户正确输入 PIN 码后才能访问的秘密。然后，这个秘密被用来解密 seed，seed 被加密存储在设备的主内存中。



这种混合安全系统提供了更好的物理保护，特别是防止提取攻击或入侵分析，这些都是 Model One 容易出现的问题，尤其是在 PIN 码管理方面。现在，由于使用了安全元件，这些漏洞都被规避了。该机型还采用了开源软件架构：管理私钥生成和使用的代码仍可完全访问和验证。OPTIGA 芯片只管理 PIN 码，这是 Bitcoin Wallet 密钥管理的外部元素。它仅限于发布可用于解密 seed 的秘密。此外，OPTIGA Trust M V3 芯片还受益于相对自由的许可证，该许可证授权中本聪实验室自由发布潜在漏洞（NDA-Free）。



在我看来，这种安全模式是目前市场上最好的折衷方案之一。它结合了安全元件和开源软件管理的优势。在此之前，用户必须在使用芯片提高物理安全性和使用开源软件提高透明度之间做出选择；而 Trezor Safe 则可以同时兼顾这两个方面。



在本教程中，您将学习如何安全地配置和使用 Trezor Safe 5。



## 开箱试用 Trezor Safe 5



当您收到 Safe 5 时，请确保包装盒和 Seal 完好无损，以确认包装未被打开。稍后设置设备时，还将对设备的真实性和完整性进行软件检查。



盒内物品包括 ：




- Trezor Safe 5；
- 一个小袋，内含用于记录 Mnemonic 短语的卡片纸、贴纸和说明；
- USB-C 至 USB-C 连接线。



打开后，Trezor Safe 5 应有保护塑料保护，USB-C 端口应有全息 Seal 保护。确保它在那里。



![Image](assets/fr/02.webp)



设备上的导航相当直观：




- 触摸屏幕下半部向前移动；
- 向下滑动可返回 ；
- 按住屏幕确认操作。



## 先决条件



在本教程中，我将向您演示如何将 Trezor Safe 5 与 [Sparrow Wallet 投资组合管理软件](https://sparrowwallet.com/download/) 结合使用。如果您尚未安装该软件，请立即安装。如果您需要帮助，我们也有关于配置 Sparrow Wallet 的详细教程：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您还需要 Trezor Suite 软件来配置 Safe 5、检查其真伪和安装固件。我们将只使用该软件，之后只在固件更新时才会用到。对于 Wallet 的日常管理，我们将只使用 Sparrow Wallet，因为它针对 Bitcoin 进行了优化，即使是初学者也很容易使用（Sparrow 只支持 Bitcoin，不支持其他币）。



[从官方网站下载 Trezor Suite](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



对于这两个程序，我强烈建议您在将它们安装到机器上之前，先检查它们的真实性（使用 GnuPG）和完整性（通过 Hash）。如果您不知道如何操作，可以参考下面的教程：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 启动 Trezor Safe 5



将 Safe 5 与已安装 Trezor Suite 和 Sparrow Wallet 的电脑连接。



![Image](assets/fr/04.webp)



打开 Trezor Suite，然后点击 "*设置我的 Trezor*"。



![Image](assets/fr/05.webp)



选择 "*仅 Bitcoin 固件*"，然后点击 "*安装仅 Bitcoin*"。



![Image](assets/fr/06.webp)



Trezor Suite 将在 Safe 5 上安装固件。安装过程中请稍候。



![Image](assets/fr/07.webp)



点击 "*继续*"。



![Image](assets/fr/08.webp)



然后进行真实性测试，以确保您的 Hardware Wallet 不是假冒伪劣产品。



![Image](assets/fr/09.webp)



在 Safe 5 上按屏幕确认。



![Image](assets/fr/10.webp)



如果您的 Trezor 是正品，Trezor 套件中将显示一条确认信息。



![Image](assets/fr/11.webp)



然后，您就可以跳过有基本操作说明的窗口。



![Image](assets/fr/12.webp)



## 创建 Bitcoin 投资组合



在 Trezor Suite 上点击 "*创建新的 Wallet*"按钮。



![Image](assets/fr/13.webp)



要创建标准 BIP39 Wallet，首先从下拉菜单中选择 "*传统 Wallet 备份类型*"，然后选择 12 或 24 个字的 Mnemonic 短语（目前建议选择 12 个字）。这样您就可以创建一个经典的单一签名组合。我建议您在此选择符合 BIP39 标准的参数，以方便检索，避免受限于特定环境。最后，点击 "*创建 Wallet*"。



如果您想进一步了解 Trezor 上的其他备份选项，包括*多共享备份*，我建议您也参阅本教程：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



接受 Hardware Wallet 上的使用条款。



![Image](assets/fr/15.webp)



长按屏幕可创建新的投资组合。



![Image](assets/fr/16.webp)



在 Trezor Suite 中，点击 "*继续备份*"。



![Image](assets/fr/17.webp)



该软件提供了如何管理 Mnemonic 短语的说明。



这个 Mnemonic 可以让您完全无限制地访问您的所有比特币。任何持有该短语的人都可以盗取你的资金，即使无法实际接触到你的 Trezor Safe 5。



如果您的 Hardware Wallet 丢失、被盗或破损，这 12 个字的短语可以恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。



您可以在包装盒内提供的纸板上书写，或者为了提高安全性，我建议您将其刻在不锈钢底座上，以防火灾、水灾或倒塌。



确认说明，然后点击 "*创建 Wallet 备份*"按钮。



![Image](assets/fr/18.webp)



Safe 5 将使用随机数生成器创建您的 Mnemonic 短语。请确保在操作过程中无人监视。将屏幕上提供的短语写在你选择的物理介质上。根据您的安全策略，您可以考虑制作几份完整的短语实体副本（但最重要的是，不要将其分割）。重要的是，要对单词进行编号并按顺序排列。



***显然，您绝不能像我在本教程中所做的那样，在互联网上分享这些文字。本例 Wallet 将仅用于 Testnet，并将在教程结束时删除。



有关保存和管理 Mnemonic 短语的正确方法的更多信息，我强烈推荐您阅读本教程，尤其是初学者：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



要进入下一个单词，请点击屏幕底部。您可以通过向下滑动来倒退。写下所有单词后，手指停留在屏幕上即可进入下一步。



![Image](assets/fr/20.webp)



根据顺序选择 Mnemonic 短语中的单词，确认您写下的单词是否正确。



![Image](assets/fr/21.webp)



验证程序完成后，点击屏幕继续。



![Image](assets/fr/22.webp)



## 设置 PIN 码



接下来是输入 PIN 码。PIN 码可以为 Trezor 解锁。因此，它可以防止未经授权的物理访问。该 PIN 码不参与 Wallet 密钥的生成。因此，即使无法获得 PIN 码，只要拥有 12 个字的 Mnemonic 短语，就能重新获得比特币。



在 Trezor Suite 上点击 "*继续密码*"，然后点击 "*设置密码*"按钮。



![Image](assets/fr/23.webp)



确认安全 5.



![Image](assets/fr/24.webp)



建议选择一个尽可能随机的 PIN 码。请务必将该密码保存在与 Trezor 存储位置不同的地方（如密码管理器）。您可以定义 8 至 50 位数字的 PIN 码。我建议你选择一个尽可能长的 PIN 码，以提高安全性。



使用触摸板输入密码。



![Image](assets/fr/25.webp)



完成后，点击右下方的 Green 标记，然后再次确认 PIN 码。



![Image](assets/fr/26.webp)



您的 PIN 码已注册。



![Image](assets/fr/27.webp)



在 Trezor Suite 上点击 "*完成设置*"按钮。



![Image](assets/fr/28.webp)



Safe 5 的配置工作现已完成。如果您愿意，可以更改 Hardware Wallet 的名称和主页。



![Image](assets/fr/29.webp)



除了对 Hardware Wallet 进行定期固件更新，或进行恢复测试外，我们不再需要 Trezor Suite 软件。我们现在将使用 Sparrow 来管理产品组合，因为该软件非常适合 Bitcoin 使用。



## 在麻雀 Wallet 上设置投资组合



如果还没有下载 Sparrow Wallet [从官方网站](https://sparrowwallet.com/) 并安装到电脑上，请先下载并安装 Sparrow Wallet。



打开 Sparrow Wallet 后，请确保软件已连接到 Bitcoin 节点，Interface 右下角的"√"表示该节点。如果您在连接 Sparrow 时遇到困难，我建议您参考本教程的开头部分：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

点击 "*文件*"选项卡，然后点击 "*新 Wallet*"。



![Image](assets/fr/30.webp)



为您的投资组合命名，然后点击 "*创建 Wallet*"。



![Image](assets/fr/31.webp)



在 "*脚本类型*"下拉菜单中，选择用于保护比特币的脚本类型。我推荐使用 "*Taproot*"，如果不行，也可以使用 "*Native SegWit*"。



![Image](assets/fr/32.webp)



点击 "*已连接 Hardware Wallet*"按钮。当然，您的 Safe 5 必须连接到电脑并解锁。



将 Safe 5 连接到打开 Sparrow Wallet 的计算机时，Hardware Wallet 屏幕会提示您输入 passphrase BIP39。这一高级选项将在今后的教程中介绍。现在，您只需点击右上角 Green 的"√"，确认希望使用空的 passphrase（即没有 passphrase）。为防止 Trezor 每次启动时都要求输入 passphrase，请进入 Trezor Suite，进入设置，更改 "*设备*" > "*Wallet默认值 "中的选项。将 "*设备*">"*Wallet 默认*"中的选项更改为 "*标准*"，而不是 "*passphrase*"。



![Image](assets/fr/33.webp)



点击 "*扫描*"按钮。您的 Safe 5 应该会出现。点击 "*导入密钥存储*"。



![Image](assets/fr/34.webp)



现在您可以看到 Wallet 的详细信息，包括第一个账户的扩展公钥。点击 "*应用*"按钮，完成 Wallet 创建。



![Image](assets/fr/35.webp)



选择一个强大的密码以确保对 Sparrow Wallet 的访问安全。该密码将确保安全访问您的 Sparrow Wallet 数据，保护您的公钥、地址、标签和交易历史记录免遭未经授权的访问。



我建议您将此密码保存在密码管理器中，以免忘记。



![Image](assets/fr/36.webp)



现在，您的投资组合已被导入 Sparrow Wallet！



![Image](assets/fr/37.webp)



在您的 Wallet 收到第一枚比特币之前，**我强烈建议您进行一次清空恢复测试**。写下一些参考信息，例如你的 xpub，然后在 Wallet 仍然为空的情况下重置 Trezor Safe 5。然后尝试使用纸质备份在 Trezor 上恢复 Wallet。检查还原后生成的 xpub 是否与你最初写下的一致。如果吻合，就说明纸质备份是可靠的。



要了解有关如何执行恢复测试的更多信息，我建议您参考其他教程：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Safe 5 接收比特币？



在 Sparrow 上，点击 "*接收*"选项卡。



![Image](assets/fr/38.webp)



在使用 Sparrow Wallet 提议的 Address 之前，请在 Trezor 的屏幕上检查一下。通过这种做法，您可以确认 Sparrow 上显示的 Address 不是假的，而且 Hardware Wallet 确实持有使用该 Address 所担保的比特币所需的私钥。这可以帮助你避免几种类型的攻击。



要执行此检查，请单击 "*显示 Address*"按钮。



![Image](assets/fr/39.webp)



检查 Trezor 上显示的 Address 是否与 Sparrow Wallet 上的一致。建议您在将 Address 发送给发信人之前进行此项检查，以确保其有效性。您可以按屏幕确认。



![Image](assets/fr/40.webp)



然后，您可以添加一个 "*标签*"来描述该 Address 所保护的比特币来源。这是一个很好的做法，可以让您更好地管理您的 UTXO。



![Image](assets/fr/41.webp)



然后，您就可以使用这个 Address 接收比特币。



![Image](assets/fr/42.webp)



## 如何使用 Trezor Safe 5 发送比特币？



现在，您已经在 Safe 5 加密的 Wallet 上收到了第一笔 Satss，您也可以花掉它们了！将 Trezor 与电脑连接，用 PIN 码解锁，启动 Sparrow Wallet，然后进入 "*发送*"选项卡建立新交易。



![Image](assets/fr/43.webp)



如果您希望*币控*，即在交易中具体选择消耗哪些UTXOs，请转到 "*UTXOs*"选项卡。选择要消耗的UTXOs，然后点击 "*发送所选*"。您将跳转到 "*发送*"选项卡中的同一界面，但已为交易选择了UTXO。



![Image](assets/fr/44.webp)



输入目的地 Address。您也可以点击 "*+ 添加*"按钮输入多个地址。



![Image](assets/fr/45.webp)



写下 "*标签*"，以记住这笔费用的用途。



![Image](assets/fr/46.webp)



选择要发送到此 Address 的金额。



![Image](assets/fr/47.webp)



根据当前市场调整交易费率。例如，您可以使用 [Mempool.space](https://Mempool.space/)，选择合适的费率。



确保所有交易参数正确无误，然后点击 "*创建交易*"。



![Image](assets/fr/48.webp)



如果一切都令您满意，请点击 "*最终完成交易以供签署*"。



![Image](assets/fr/49.webp)



点击 "*签署*"。



![Image](assets/fr/50.webp)



点击 Trezor Safe 5 旁边的 "*Sign*"。



![Image](assets/fr/51.webp)



检查 Hardware Wallet 屏幕上的交易参数，包括收件人的接收 Address、发送金额和费用。在 Trezor 上验证交易后，按住屏幕进行签名。



![Image](assets/fr/52.webp)



您的交易现在已经签署。最后检查一次是否一切正常，然后点击 "*广播交易*"在 Bitcoin 网络上广播。



![Image](assets/fr/53.webp)



您可以在麻雀 Wallet 的 "*交易*"选项卡中找到它。



![Image](assets/fr/54.webp)



恭喜您，现在您已经掌握了 Trezor Safe 5 与麻雀 Wallet 的基本使用方法！要想更进一步，我向您推荐本综合教程，介绍如何使用 Trezor Hardware Wallet 和 passphrase BIP39 来提高您的安全：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您觉得本教程有用，请在下面留下 Green 的大拇指。欢迎在您的社交网络上分享本文。非常感谢