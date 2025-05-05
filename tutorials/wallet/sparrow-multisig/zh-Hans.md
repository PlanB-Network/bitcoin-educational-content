---
name: 麻雀 Wallet - Multisig
description: 在 Sparrow 上创建多重签名组合
---
![cover](assets/cover.webp)



多签名 Wallet（通常称为 "*Multisig*"）是一种 Bitcoin Wallet 结构，它需要不同密钥的多个加密签名才能授权支出。与传统的（"*singlesig*"）Wallet 不同，Multisig 基于**m-of-n**模式：在与 Wallet 相关的_n_个密钥中，_m_个必须共同签署每笔交易。



这种机制可以让多个实体或设备共享投资组合的控制权。例如，在 2 对 3 配置中，会生成三套独立的密钥，但只需要两套密钥即可释放资金。这种结构大大降低了密钥泄露或丢失带来的风险：窃贼只需获得一把密钥，就无法清空 Wallet，而丢失一把密钥的用户仍可使用其余两把密钥存取资金。



![Image](assets/fr/01.webp)



然而，更高的安全性也带来了更大的复杂性。设置 Multisig Wallet 需要确保多个 Mnemonic 短语（每个签名因子一个）和扩展公钥（"*xpub*"）的安全。事实上，如果您使用的是 Multisig 2-of-3 Wallet，要检索 Wallet，您必须拥有全部三个 Mnemonic 短语，或者至少拥有三个短语中的两个。但如果你只有三个短语中的两个，你还需要访问三个 *xpubs*，没有它们就不可能检索到访问它们所保护的比特币所需的公钥。



总而言之，要恢复 Multisig 投资组合，您必须：




- 或访问与每个签名因素相关的所有 Mnemonic 短语；
- 要么拥有阈值所要求的 Mnemonic 短语的最低数量，以便能够签名，要么能够访问所有因子的 xpub，以便检索必要的公钥。



![Image](assets/fr/02.webp)



Multisig 投资组合备份管理可通过*输出脚本描述符*来实现，该脚本描述符将访问基金所需的所有公共数据集中在一起。不过，并非所有投资组合管理软件都具备这一功能。



Multisig 特别适合那些希望加强安全性或对资金进行集体管理的比特币用户：公司、协会、家庭或持有大量比特币的个人用户。它可用于创建去中心化管理方案，例如，在多个管理者或团队成员之间分配签名权。



在本教程中，我们将学习如何使用 **Sparrow Wallet** 创建和使用经典的多重签名 Wallet。如果您想创建带有计时器的定制多重签名组合，我建议您使用 Liana：



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## 先决条件



在本教程中，我将向您展示如何使用 [Sparrow Wallet 投资组合管理软件](https://sparrowwallet.com/download/) 制作 Multisig。如果您尚未安装该软件，请立即安装。如果您需要帮助，我们也有关于配置 Sparrow Wallet 的详细教程：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

要设置多重签名 Wallet，您需要不同的硬件钱包。例如，对于 Multisig 2-de-3，您可以使用 ：




- Trezor Model One
- Ledger Flex；
- 冷卡 MK3



![Image](assets/fr/03.webp)



在 Multisig 配置中使用不同型号的 Hardware Wallet 是个好主意。这样可以确保在特定型号出现严重问题时，不会影响 Multisig 的整体安全性。此外，它还能让您从每种设备的具体优势中获益。例如，在我的配置中 ：





- Trezor Model One 完全开源，因此可以验证 seed 的生成。不过，由于没有配备安全元件，它仍然容易受到物理攻击；





- 另一方面，Ledger Flex 采用了无法验证的专有固件，但它集成了一个安全元件，可提供出色的物理保护；





- Coldcard 配备了安全元件，其代码可以搜索。对于我们的配置来说，这是一个有趣的选择，因为它提供了其他型号所不具备的验证功能。



在配置 Multisig Wallet 之前，请确保每个 Hardware Wallet 都已正确配置（Mnemonic 生成和保存、PIN 定义）。有关详细说明，请参阅我们为每台 Hardware Wallet 编写的教程，例如 ：



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

正如我们在本教程稍后将看到的，也可以在 Multisig 配置中集成一个与 Hardware Wallet 无关的因子，但其私钥存储在您的电脑中。这种方法显然不如只使用硬件钱包来得安全，但在某些情况下也是可行的。例如，对于 Multisig 2-de-3，您可以选择两个硬件钱包和一个 Software Wallet。



## 创建 Multisig 组合



打开 Sparrow Wallet，点击 "*文件*"选项卡，然后选择 "*新建 Wallet*"。



![Image](assets/fr/04.webp)



为您的多重签名组合指定一个名称，然后点击 "*创建 Wallet*"确认。



![Image](assets/fr/05.webp)



在 "*策略类型*"下拉菜单中，选择 "*多重签名*"选项。



![Image](assets/fr/06.webp)



现在，您可以在右上角定义 Multisig 中密钥的总数，以及授权某项支出所需的联合签名人数。在我的例子中，这是一个 2 对 3 方案。



![Image](assets/fr/07.webp)



在窗口底部，Sparrow Wallet 显示了三个 "*Keystore*"。每个都代表一组密钥。在这里，我使用了三个硬件组合，因此每个 "*Keystore*"都对应其中一个。现在我们来配置它们。



我从冷卡开始。在 "*Keystore 1*"选项卡中，我选择了 "*Airgapped Hardware Wallet*"选项。



![Image](assets/fr/08.webp)



在 Coldcard 上，一旦设备解锁，我就会进入 "*设置*"菜单，然后进入 "*Multisig 钱包*"。



![Image](assets/fr/09.webp)



通过该菜单，您可以管理 Coldcard 参与的 Multisig 组合。我想创建一个新的组合，因此选择了 "*导出 XPUB*"。



![Image](assets/fr/10.webp)



对于 "*账号*"字段，如果您只管理一个账号，可以不填，直接按确认按钮进行验证。



![Image](assets/fr/11.webp)



然后，Coldcard 会在 generate 中生成一个包含 xpub 的文件，保存在 Micro SD 卡中。



![Image](assets/fr/12.webp)



将微型 SD 插入电脑。在 Sparrow Wallet 中，点击 "*Coldcard Multisig*"旁边的 "*Import File...*"按钮，然后选择卡上由 Coldcard 创建的文件。



![Image](assets/fr/13.webp)



您的 xpub 已成功导入。现在，我们将对另外两个硬件钱包重复上述步骤。



![Image](assets/fr/14.webp)



对于 Ledger Flex，我选择 "*Keystore 2*"，然后点击 "*Connected Hardware Wallet*"。确保 Ledger 已连接到电脑，已解锁，并且 Bitcoin 应用程序已打开。



![Image](assets/fr/15.webp)



然后点击 "*扫描...*"按钮。



![Image](assets/fr/16.webp)



在硬件组合名称旁边，点击 "*导入密钥存储*"。



![Image](assets/fr/17.webp)



现在，第二个签名人已在 Sparrow Wallet 中正确注册。



![Image](assets/fr/18.webp)



我用 Trezor One 重复了完全相同的步骤，最终完成了 Multisig 的配置。



![Image](assets/fr/19.webp)



在我的配置中，我们不包括这种情况，但如果您想通过麻雀中的 Software Wallet（Hot Wallet）在 Multisig 中加入签名，只需点击 "*新的或导入的 Software Wallet*"按钮即可。



现在所有签名设备都已导入 Sparrow Wallet，点击 "*应用*"即可完成 Multisig 的创建。



![Image](assets/fr/20.webp)



选择一个强大的密码，以确保对 Sparrow Wallet Wallet 的访问安全。该密码可保护您的公用密钥、地址、标签和交易历史记录免遭未经授权的访问。



记住将密码保存在安全的地方，如密码管理器，以免丢失。



![Image](assets/fr/21.webp)



## 备份 Multisig 投资组合



现在，我们要将*输出脚本描述符*保存在冷卡上（这只适用于在 Multisig 中安装了冷卡的用户），最重要的是，我们要将其备份在一个独立的介质上。



描述符*包含 Multisig 组合中的所有 xpub，以及用于 generate 密钥的派生路径。请记住我们在第一部分中看到的：要恢复 Multisig 组合，您必须拥有***所有的 Mnemonic 词组，或者只拥有达到签名阈值所需的最低数量。但是，在后一种情况下，还必须拥有**缺失的签名者的 xpubs**。描述符*包含 Multisig 的所有 xpub。



如果还不清楚，请记住：要检索 Multisig，每使用一个 Hardware Wallet 就需要最少的 Mnemonic 短语数，具体取决于阈值（在我的例子中为 2 个短语）以及 *描述符*。



该*描述符*不包含私钥，只包含公钥。这意味着它不能访问资金。因此，它不像 Mnemonic 短语那么重要，因为 Mnemonic 短语可以完全访问您的比特币。*Descriptor* 的风险只与保密性有关：如果发生泄露，第三方可以看到您的所有交易，但无法使用您的资金。



我强烈建议您将该*描述符*复制多份，并将其保存在 Multisig 上的每个签名设备中。例如，我将*描述符*打印在纸上，一份保存在 Coldcard 上，一份保存在 Trezor 上，一份保存在 Ledger 上。此外，我还将这份*Descriptor*以 PDF 文件的形式保存在三个 U 盘中，每个 U 盘都与其中一个硬件组合存放在一起。这样，我就能最大限度地避免丢失该*描述符*，并确保每个设备都有两份拷贝（一份实体拷贝和一份数字拷贝）。



您的 Multisig 投资组合创建后，Sparrow 会自动为您提供该*描述符*。点击 "*保存 PDF...*"按钮，即可将其保存为文本和二维码。



![Image](assets/fr/22.webp)



然后，您就可以打印这份 PDF 文件，并将其复制到 U 盘中。



![Image](assets/fr/23.webp)



我们还将在冷卡中注册此*描述符*（如果您在配置中使用冷卡的话）。这将使 Coldcard 能够验证随后签署的每笔交易是否与原始 Wallet 相符：正确的 xpubs、正确的 Address 格式、正确的派生路径......如果没有这个导入的*描述符*，Coldcard 就无法确认 Exchange 地址是否被劫持或 PSBT 是否被篡改。



这也是 Coldcard 在 Multisig 中如此有趣的原因：它针对某些复杂的攻击提供额外的检查，这是其他硬件钱包所不允许的（当然，前提是你用它来签名）。



在 Sparrow 中进入 "*设置*"菜单，然后点击 "*导出...*"。



![Image](assets/fr/24.webp)



在 "*存储卡 Multisig*"选项旁，点击 "*导出文件...*"，将文本文件保存到 Micro SD 卡中。



![Image](assets/fr/25.webp)



然后将卡插入 Coldcard。进入 "*设置*"菜单，然后进入 "*Multisig 钱包*"，选择 "*从 SD 导入*"。



![Image](assets/fr/26.webp)



选择适当的文件并确认导入。



![Image](assets/fr/27.webp)



点击新导入的 Multisig 名称。



![Image](assets/fr/28.webp)



检查 Multisig 配置参数，然后确认注册。



![Image](assets/fr/29.webp)



现在，您的 Multisig 已正确保存在冷卡中。如果您在同一张 Multisig 中拥有多张冷卡，请为每一张冷卡重复此步骤。



除了保存 *Descriptor* 之外，不要忘记特别注意保存每个签名设备的 Mnemonic 短语。如果你刚开始使用，我强烈建议你参考其他教程，学习如何正确保存和管理这些短语：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在用 Multisig 接收第一批比特币之前，**我强烈建议您执行空恢复测试**。记下一些参考信息，如第一次接收 Address，然后在 Wallet 仍为空时重置硬件钱包。接下来，尝试使用 Mnemonic 短语纸质备份在硬件钱包上恢复 Multisig Wallet，然后在麻雀上使用*描述符*。检查恢复后生成的第一个 Address 是否与您最初写下的一致。如果吻合，您就可以放心，您的纸质备份是可靠的。



要了解有关如何执行恢复测试的更多信息，我建议您参考其他教程：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 用 Multisig 接收比特币



您的 Wallet 现在可以接收比特币了。在 Sparrow 中，点击 "*接收*"选项卡。



![Image](assets/fr/30.webp)



在使用 Sparrow Wallet 生成的 Address 之前，请花时间直接在硬件钱包的屏幕上进行检查。这将确保 Address 没有被篡改，并确保您的设备持有花费相关资金所需的私钥。这有助于保护您免受多种攻击。



通过电缆连接时，点击 "*显示 Address*"可在 Trezor 或 Ledger 上显示 Address。



![Image](assets/fr/31.webp)



使用 Coldcard，无需与 Sparrow 进行任何交互即可进行验证。只需打开 "*Address Explorer*"菜单，然后在最下方选择您的 Multisig。



![Image](assets/fr/32.webp)



然后您将看到 Multisig 生成的接收地址。



![Image](assets/fr/33.webp)



检查每个 Hardware Wallet 上显示的 Address 是否与 Sparrow Wallet 中的完全一致。建议在与付款人共享 Address 之前进行检查，以确保其完整性。



然后，您就可以为这个 Address 分配一个 "*标签*"，以标明收到的比特币的来源。这是一种组织管理 UTXO 的好方法。



![Image](assets/fr/34.webp)



验证通过后，您就可以使用 Address 接收比特币了。



![Image](assets/fr/35.webp)



## 用 Multisig 发送比特币



现在，您已经在 Multisig Wallet 上收到了第一个萨特，您也可以花掉它们了！在麻雀中，进入 "*发送*"选项卡，建立新的交易。



![Image](assets/fr/36.webp)



如果您希望使用 "*币控*"，即手动选择要使用的UTXOs，请转到 "*UTXOs*"选项卡。选择您希望使用的UTXOs，然后点击 "*发送所选*"。您将自动跳转到 "*发送*"选项卡，UTXO 已预先填好。



![Image](assets/fr/37.webp)



输入目的地 Address。点击 "*+ 添加*"可添加多个地址。



![Image](assets/fr/38.webp)



添加 "*标签*"来描述这笔费用的用途，以便于跟踪交易。



![Image](assets/fr/39.webp)



输入要发送到所选 Address 的金额。



![Image](assets/fr/40.webp)



根据当前网络条件调整充电速率。例如，请参考 [Mempool.space](https://Mempool.space/)，选择合适的充电级别。



检查所有交易参数后，点击 "*创建交易*"。



![Image](assets/fr/41.webp)



如果您对一切都满意，请点击 "*最终完成交易以供签署*"。



![Image](assets/fr/42.webp)



在屏幕下方，您会看到麻雀正在等待 2 个签名。这是正常现象：这里使用的 Wallet 是 Multisig 2-de-3。



![Image](assets/fr/43.webp)



我开始使用冷卡签名。为此，我将 Micro SD 卡插入电脑，然后点击 "*保存交易*"。



![Image](assets/fr/44.webp)



有三种方法可以将要签名的交易传输到 Hardware Wallet 上，然后再从麻雀中提取。第一种是使用 Micro SD 卡，我们将在这里使用 Coldcard。第二种是通过电缆连接，我们将在第二次签名时使用（Ledger 和 Trezor）。最后，对于 Coldcard Q、Jade Plus 或 Passport V2 等配备摄像头的设备，还可以使用 QR 码通信。



将 PSBT (*Partially Signed Bitcoin Transaction*) 保存在 Micro SD 上后，我将其插入 Coldcard MK3，然后选择 "*准备签署*"菜单。



![Image](assets/fr/45.webp)



在 Hardware Wallet 屏幕上，仔细检查交易参数：收件人的 Address、发送金额和费用。确认交易后，验证以进行签名。



![Image](assets/fr/46.webp)



然后将 Micro SD 放回电脑，在 Sparrow 中点击 "*加载交易*"。从文件中选择由 Coldcard 签名的 PSBT。



![Image](assets/fr/47.webp)



可以看到 Coldcard 签名已经添加。我现在要使用第二个设备（这里是 Ledger）来执行第二个签名要求。我连接它，解锁，然后点击 Sparrow 上的 "*Sign*"。



![Image](assets/fr/48.webp)



点击 Hardware Wallet 名称旁边的 "*Sign*"。



![Image](assets/fr/49.webp)



第一次使用 Ledger 和 Multisig 时，Sparrow 会要求您验证共同签名人的扩展公钥 (xpub)。与冷卡一样，这一步骤可防止您以后盲目签名。要验证此信息，请将 Ledger 屏幕上显示的 xpub 与其他硬件钱包直接提供的 xpub 进行比较。



![Image](assets/fr/50.webp)



核对收件人的 Address、转账金额和交易费，然后签署交易。



![Image](assets/fr/51.webp)



按屏幕签名。



![Image](assets/fr/52.webp)



麻雀现在有了从 Multisig 投资组合中释放资金所需的两个签名。最后检查一次交易，如果一切顺利，点击 "*广播交易*"将其在网络上广播。



![Image](assets/fr/53.webp)



您可以在麻雀 Wallet 的 "*交易*"选项卡中找到该交易。



![Image](assets/fr/54.webp)



恭喜您，现在您已经知道如何在 Sparrow 上设置和使用多重签名 Wallet。如果您觉得本教程有用，请在下面留下 Green 的大拇指。欢迎在您的社交网络上分享本文。感谢您的分享！



要想更进一步，我建议您参考本教程，了解另一种提高 Bitcoin Wallet 安全性的方法，即 passphrase BIP39：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7