---
name: Sparrow Wallet - 多重签名
description: 在 Sparrow 上创建多重签名钱包
---
![封面](assets/cover.webp)


多重签名钱包（通常称为“*Multisig*”）是一种 Bitcoin 钱包结构，需要来自不同密钥的多个密码学签名，才能授权一笔支出。与传统的（“*singlesig*”）钱包不同，传统钱包只需一个私钥就足以解锁一个 UTXO，而多重签名基于 **m-of-n** 模型：在与钱包关联的 _n_ 个密钥中，必须有 _m_ 个密钥共同签署每笔交易。


这种机制可以让多个实体或设备共同控制一个钱包。例如，在 2-of-3 配置中，会生成三组独立的密钥，但只需要其中两组就能释放资金。这种架构大幅降低了密钥被攻破或丢失所带来的风险：只拿到一个密钥的小偷无法清空钱包，而丢失一个密钥的用户仍然可以用剩下的两个密钥访问自己的资金。


![图片](assets/fr/01.webp)


然而，更高的安全性也带来了更高的复杂度。设置一个多重签名钱包，需要保护多个助记词（每个签名因子一个）以及扩展公钥（“*xpub*”）。事实上，如果你使用的是 2-of-3 多重签名钱包，要恢复这个钱包，你必须拥有全部三个助记词，或者至少拥有三个助记词中的两个。但如果你只有三个助记词中的两个，还需要访问全部三个 *xpubs*，否则就无法恢复访问其所保护的 bitcoins 所需的公钥。


总结一下，要恢复一个多重签名钱包，你必须：


- 要么访问与每个签名因子关联的全部助记词；
- 要么拥有达到阈值所需的最少数量助记词，以便能够签名，同时还要访问所有因子的 xpubs，以恢复必要的公钥。


![图片](assets/fr/02.webp)


*输出脚本描述符*让多重签名钱包备份的管理更容易，因为它们会把访问资金所需的所有公开数据组合在一起。不过，并非所有钱包管理软件都已经实现了这个功能。


多重签名特别适合希望获得更高安全性或共同管理资金的 bitcoiners：公司、协会、家庭，或者持有大量 bitcoins 的个人用户。它可以用于创建去中心化治理方案，例如在多名管理者或团队成员之间分配签名权限。


在本教程中，我们将学习如何使用 **Sparrow Wallet** 创建和使用一个经典的多重签名钱包。如果你想创建带有 timelocks 的自定义多重签名钱包，我建议改用 Liana：


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## 前提条件


在本教程中，我将向你展示如何使用 [Sparrow Wallet 钱包管理软件](https://sparrowwallet.com/download/) 创建一个多重签名钱包。如果你还没有安装这个软件，请现在安装。如果需要帮助，我们也有一篇关于配置 Sparrow Wallet 的详细教程：


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

要设置一个多重签名钱包，你需要不同的硬件钱包。例如，对于一个 2-of-3 多重签名，你可以使用：


- 一个 Trezor Model One；
- Ledger Flex；
- 一个 Passport Core。


![图片](assets/fr/03.webp)


在多重签名配置中使用不同品牌的硬件钱包是一个好主意。这样可以确保如果某个特定型号遇到严重问题，不会影响你的多重签名整体安全性。此外，它还能让你受益于每台设备的特定优势。例如，在我的配置中：



- Trezor Model One 是完全开源的，因此可以验证种子生成过程。不过，由于它没有配备 Secure Element，它仍然容易受到物理攻击；



- 另一方面，Ledger Flex 使用无法验证的专有固件，但它集成了一个 Secure Element，可以提供出色的物理保护；



- Passport Core 结合了完全开源的固件、Secure Element，以及通过隔空 QR 码交换数据的方式。它是一个独立的第三签名器，可以验证地址并签署 PSBT，而无需 USB 数据连接。


在配置你的多重签名钱包之前，请确保每个硬件钱包都已正确配置（助记词生成和保存、PIN 设置）。有关详细说明，你可以查阅我们针对每个硬件钱包的教程，例如：


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

正如我们稍后将在本教程中看到的，也可以在你的多重签名配置中集成一个不与硬件钱包关联的因子，其私钥存储在你的 PC 上。这种方法显然不如只使用硬件钱包安全，但在某些情况下可能有意义。例如，对于一个 2-of-3 多重签名，你可以选择两个硬件钱包和一个软件钱包。

> ⚠️ **Coldcard MK3 安全提示：**不要在运行早于 4.2.0 固件的 MK3 上创建新种子。在早期固件上生成的种子必须更换，并且资金必须转移。因此，本教程使用 Passport Core 作为隔空参考签名器。


## 创建多重签名钱包


打开 Sparrow Wallet，点击“*File*”选项卡，然后选择“*New Wallet*”。


![图片](assets/fr/04.webp)


为你的多重签名钱包指定一个名称，然后点击“*Create Wallet*”确认。


![图片](assets/fr/05.webp)


在“*Policy Type*”下拉菜单中，选择“*Multi Signature*”选项。


![图片](assets/fr/06.webp)


现在可以在右上角定义你的多重签名中的密钥总数，以及授权一笔支出所需的共同签名者数量。在我的示例中，这是一个 2-of-3 方案。


![图片](assets/fr/07.webp)


在窗口底部，Sparrow Wallet 会显示三个“*Keystore*”。每一个都代表一组密钥。在这里，我使用三个硬件钱包，所以每个“*Keystore*”都对应其中一个。现在我们来配置它们。


我从 Passport Core 开始。在“*Keystore 1*”选项卡中，我选择“*Airgapped Hardware Wallet*”选项。


![图片](assets/fr/08.webp)


在 Passport 上，打开你要使用的账户，然后选择“*Connect Wallet*”>“*Sparrow*”>“*Connect as Multisig*”。Passport 会显示一个动画 QR 码，其中包含其公钥信息。

在 Sparrow 中，选择“*Passport*”旁边的“*Scan...*”，并用电脑的摄像头扫描该动画 QR 码。将 Sparrow 显示的主密钥指纹与 Passport 显示的指纹进行核对，然后导入 keystore。

你的 Passport xpub 现在已经导入。对 Ledger Flex 和 Trezor Model One 重复相应流程。


对于 Ledger Flex，我选择“*Keystore 2*”，然后点击“*Connected Hardware Wallet*”。请确保 Ledger 已连接到电脑、已解锁，并且 Bitcoin 应用程序已打开。


![图片](assets/fr/15.webp)


然后点击“*Scan...*”按钮。


![图片](assets/fr/16.webp)


在你的硬件钱包名称旁边，点击“*Import Keystore*”。


![图片](assets/fr/17.webp)


第二个签名者现在已在 Sparrow Wallet 中正确注册。


![图片](assets/fr/18.webp)


我用 Trezor One 重复完全相同的流程，以完成多重签名配置。


![图片](assets/fr/19.webp)


在我的配置中我们不覆盖这种情况，但如果你想在多重签名中加入通过 Sparrow 软件钱包（热钱包）完成的签名，只需点击“*New or Imported Software Wallet*”按钮。


现在所有签名设备都已导入 Sparrow Wallet，你可以点击“*Apply*”来完成多重签名创建。


![图片](assets/fr/20.webp)


选择一个强密码来保护对你的 Sparrow Wallet 钱包的访问。这个密码会保护你的公钥、地址、标签和交易历史，防止未经授权的访问。


请记得将此密码保存在安全位置，例如密码管理器中，以免丢失。


![图片](assets/fr/21.webp)


## 备份多重签名钱包


我们现在会把*输出脚本描述符*保存在独立介质上，并保留多份副本。


*描述符*包含你的多重签名钱包中的所有 xpubs，以及用于生成密钥的派生路径。请记住我们在第 1 部分中看到的内容：要恢复一个多重签名钱包，你必须拥有**全部**助记词，或者只拥有达到签名阈值所需的最少数量助记词。不过，在后一种情况下，还必须拥有缺失签名者的 **xpubs**。*描述符*包含你的多重签名的所有 xpubs。


如果这还不清楚，只要记住这一点：要恢复一个多重签名，你需要根据阈值拥有所用每个硬件钱包的最少数量助记词（在我的例子中：2 个助记词），以及*描述符*。


这个*描述符*不包含私钥，只包含公钥。这意味着它不能访问资金。因此，它不像助记词那样关键，因为助记词可以完整访问你的 bitcoins。*描述符*的风险只与保密性有关：如果它被泄露，第三方可以观察你的所有交易，但不能花费你的资金。


我强烈建议你为这个*描述符*创建多份副本，并把它们与多重签名中的每个签名设备一起保存。例如，在我的情况下，我会把*描述符*打印在纸上，并分别与 Passport、Trezor 和 Ledger 各保存一份。我也会把这个*描述符*以 PDF 文件形式保存在三个 USB 盘上，每个 USB 盘与一个硬件钱包一起存放。这样，我会最大化避免丢失这个*描述符*的机会，并确保每台设备旁边都有两份副本（一份实体副本和一份数字副本）。


创建多重签名钱包后，Sparrow 会自动向你提供这个*描述符*。点击“*Save PDF...*”按钮，将它同时保存为文本和 QR 码。


![图片](assets/fr/22.webp)


然后你可以打印这个 PDF，并把它复制到你的 USB 盘上。


![图片](assets/fr/23.webp)


Passport 会使用 Sparrow 导入的 multisig 配置，在 QR 配对和签名流程中显示并验证相关密钥信息。请独立保存*描述符*：如果某个签名器不可用，它仍然是恢复钱包的必要信息。


除了保存*描述符*之外，也不要忘记特别注意保存每个签名设备的助记词。如果你刚开始，我强烈建议你查阅另一篇教程，学习如何正确保存和管理它们：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在你的多重签名接收第一笔 bitcoins 之前，**我强烈建议你执行一次空钱包恢复测试**。记录一些参考信息，例如第一个接收地址，然后在钱包仍为空时重置你的硬件钱包。接着，尝试使用纸质助记词备份在硬件钱包上恢复你的多重签名钱包，再使用*描述符*在 Sparrow 上恢复。检查恢复后生成的第一个地址是否与你最初记下的地址一致。如果一致，你就可以放心，你的纸质备份是可靠的。


要进一步了解如何执行恢复测试，我建议你查阅另一篇教程：


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 在你的多重签名上接收 bitcoins


你的钱包现在已准备好接收 bitcoins。在 Sparrow 中，点击“*Receive*”选项卡。


![图片](assets/fr/30.webp)


在使用 Sparrow Wallet 生成的地址之前，请花时间直接在你的硬件钱包屏幕上检查它。这将确保该地址没有被篡改，并且你的设备持有花费相关资金所需的私钥。这有助于保护你免受多种攻击向量的影响。


为此，在通过线缆连接时，点击“*Display Address*”，以在你的 Trezor 或 Ledger 上显示该地址。


![图片](assets/fr/31.webp)


使用 Passport 时，选择 multisig 账户并选择“*Verify Address*”。扫描 Sparrow 显示的接收地址 QR 码。Passport 会在屏幕上确认该地址是否属于这个 multisig 钱包。


检查每个硬件钱包上显示的地址是否与 Sparrow Wallet 中的地址完全一致。建议在把地址分享给付款人之前立即进行此检查，以确认其完整性。


然后你可以为这个地址分配一个“*Label*”，以说明收到的 bitcoins 的来源。这是组织管理你的 UTXOs 的好方法。


![图片](assets/fr/34.webp)


完成验证后，你可以使用该地址接收 bitcoins。


![图片](assets/fr/35.webp)


## 使用你的多重签名发送 bitcoins


现在你已经在多重签名钱包中收到第一笔 Sats，也可以花费它们了！在 Sparrow 中，前往“*Send*”选项卡来构建一笔新交易。


![图片](assets/fr/36.webp)


如果你想使用 *Coin Control*，即手动选择你希望花费的 UTXOs，请前往“*UTXOs*”选项卡。选择你希望花费的 UTXOs，然后点击“*Send Selected*”。你会被自动重定向到“*Send*”选项卡，并且 UTXOs 已经预先填好。


![图片](assets/fr/37.webp)


输入目标地址。点击“*+ Add*”可以添加多个地址。


![图片](assets/fr/38.webp)


添加一个“*Label*”来描述这笔支出的目的，以便更容易跟踪你的交易。


![图片](assets/fr/39.webp)


输入要发送到所选地址的金额。


![图片](assets/fr/40.webp)


根据当前网络状况调整费率。例如，查阅 [Mempool.space](https://Mempool.space/) 来选择合适的费用水平。


检查所有交易参数后，点击“*Create Transaction*”。


![图片](assets/fr/41.webp)


如果一切都符合你的预期，点击“*Finalize Transaction for Signing*”。


![图片](assets/fr/42.webp)


在屏幕底部，你会看到 Sparrow 正在等待 2 个签名。这是正常的：这里使用的钱包是一个 2-of-3 多重签名。


![图片](assets/fr/43.webp)


我先用 Passport 签名。在 Sparrow 中，点击“*Show QR*”，将 PSBT（*Partially Signed Bitcoin Transaction*）显示为动画 QR 码。在 Passport 上，选择 multisig 账户并选择“*Sign with QR Code*”，然后扫描 Sparrow 显示的 QR 码。


在你的硬件钱包屏幕上，仔细检查交易参数：收款人的地址、发送金额和费用。确认交易后，批准以继续签名。


批准交易后，Passport 会将已签名的 PSBT 显示为动画 QR 码。在 Sparrow 中，点击“*Scan QR*”，并用你的摄像头扫描这些二维码。然后会添加 Passport 的签名。现在我用 Ledger 完成第二个必需签名：我连接并解锁它，然后在 Sparrow 中点击“*Sign*”。


![图片](assets/fr/48.webp)


点击你的硬件钱包名称旁边的“*Sign*”。


![图片](assets/fr/49.webp)


第一次将 Ledger 与这个多重签名一起使用时，Sparrow 会要求你验证共同签名者的扩展公钥（xpubs）。与 Passport 一样，此步骤可以防止你以后盲目签名。要验证这些信息，请将 Ledger 屏幕上显示的 xpub 与其他硬件钱包直接提供的 xpub 进行比较。


![图片](assets/fr/50.webp)


检查收款人的地址、转账金额和交易费，然后签署交易。


![图片](assets/fr/51.webp)


按下屏幕以签名。


![图片](assets/fr/52.webp)


Sparrow 现在已经获得从多重签名钱包释放资金所需的两个签名。最后再次检查交易，如果一切正常，点击“*Broadcast Transaction*”将其广播到网络。


![图片](assets/fr/53.webp)


你可以在 Sparrow Wallet 的“*Transactions*”选项卡中找到这笔交易。


![图片](assets/fr/54.webp)


恭喜，你现在知道如何在 Sparrow 上设置和使用多重签名钱包了。如果你觉得本教程有用，我会很感谢你在下方留下一个绿色拇指。也欢迎你在社交网络上分享这篇文章。感谢分享！


要继续深入，我建议你查阅这篇关于提高 Bitcoin 钱包安全性的另一种方法的教程，即 BIP39 passphrase：


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
