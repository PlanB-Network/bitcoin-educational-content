---
name: Satochip
description: 设置和使用 Satochip 智能卡
---
![cover](assets/cover.webp)

硬件钱包是一种专门用于管理和保护比特币钱包私钥的电子设备。与安装在通常连接互联网的通用计算机上的软件钱包（或热钱包）不同，硬件钱包能够将私钥物理隔离，从而降低被黑客攻击和盗窃的风险。

硬件钱包的主要目标是最大限度地减少设备的功能，从而缩小其攻击面。更小的攻击面意味着更少的潜在攻击途径，也就是说，攻击者可以利用的系统漏洞更少，从而更容易访问比特币。

建议使用硬件钱包来保护您的比特币，尤其是在您持有大量比特币的情况下，无论其绝对价值或占总资产的比例都相当高。

硬件钱包通常与计算机或智能手机上的钱包管理软件配合使用。该软件负责创建交易，但验证这些交易所需的加密签名完全在硬件钱包内部完成。这意味着私钥永远不会暴露在潜在的安全环境中。

硬件钱包为用户提供双重保护：一方面，它们通过将私钥离线存储来保护您的比特币免受远程攻击；另一方面，它们通常具有更强的物理防御能力，能够有效防止密钥被提取。正是基于这两个安全标准，我们可以对市面上不同的硬件钱包型号进行评判和排名。

在本教程中，我将介绍其中一种解决方案：Satochip。

## Satochip 简介

Satochip 是一款卡片式硬件钱包，内置 EAL6+ 认证芯片，该芯片符合极高的安全标准（NXP JCOP）。它由一家比利时公司生产。

![SATOCHIP](assets/notext/01.webp)

这款智能卡售价 25 欧元，与其他硬件钱包相比价格非常实惠。该芯片是一个安全元件，能够有效抵御物理攻击。此外，它的代码是开源的（AGPLv3）。

然而，由于其外形设计，Satochip 的功能不如其他硬件钱包丰富。它显然没有电池、摄像头或 micro SD 卡读卡器，因为它本质上是一张卡。在我看来，它最大的缺点是硬件钱包没有屏幕，这使得它更容易受到某些类型的远程攻击。事实上，这迫使用户盲目签名，并完全信任电脑屏幕上显示的内容。

尽管存在这些限制，Satochip 仍然因其价格低廉而具有吸引力。除了配备屏幕的硬件钱包外，这款钱包还可以增强消费钱包的安全性，作为储蓄钱包的补充。对于那些持有少量比特币且不想花费数百欧元购买更复杂设备的用户来说，它也是一个不错的选择。此外，Satochip 在多重签名配置中的应用，或者未来可能在带有时间锁的钱包系统中的应用，都可能带来一些有趣的优势。

Satochip 公司还提供另外两款产品。 Satochip 有两款产品：Satodime 和 Seedkeeper。Satodime 是一款用于离线存储比特币的卡片，但不支持交易。它类似于纸钱包，安全性更高，例如可以作为礼物赠送。Seedkeeper 是一款助记词管理器，可以安全地保存助记词，无需将其直接记录在纸上。

## 如何购买 Satochip？

Satochip 可在[官方网站](https://satochip.io/product/satochip/)购买。您也可以在 Satochip 网站上找到[认证经销商列表](https://satochip.io/resellers/)，了解实体店购买信息。

Satochip 提供两种方式与您的钱包管理软件交互：NFC 通信或智能卡读卡器。如果您选择 NFC 方式，请确保您的设备兼容该技术，或者购买一个外置 NFC 读卡器。Satochip 的工作频率为 13.56 MHz。您也可以购买智能卡读卡器。您可以在 Satochip 官网或其他地方找到它。

![SATOCHIP](assets/notext/02.webp)

## 如何用 Sparrow 设置 Satochip？

收到您的 Satochip 后，第一步是检查包装确保它未被打开。Satochip 的包装应该包括一个封条贴纸。如果这个贴纸缺失或损坏，可能表明智能卡已经被篡改，可能不是正品。
![SATOCHIP](assets/notext/03.webp)
您会在里面找到 Satochip。

![SATOCHIP](assets/notext/04.webp)

为了管理钱包，在这个教程中，我建议使用 Sparrow Wallet。如果您还没有下载这个软件，[请访问官方网站下载它](https://sparrowwallet.com/download/)。您也可以查看我们即将推出的 Sparrow Wallet 教程。

![SATOCHIP](assets/notext/05.webp)

将您的 Satochip 插入智能卡阅读器或放在 NFC 读卡器上，并将读卡器连接到已经打开 Sparrow 的计算机上。

![SATOCHIP](assets/notext/06.webp)

打开 Sparrow Wallet 并确保您正确连接到了比特币节点。为此，检查右下角的勾选标记：如果您连接到公共节点，它应该是黄色的；连接到 Bitcoin Core 时，为绿色；连接到 Electrum 时，为蓝色。

![SATOCHIP](assets/notext/07.webp)

在 Sparrow Wallet 上，点击 "*File*" 标签。

![SATOCHIP](assets/notext/08.webp)

然后点击 "*New Wallet*" 选单。

![SATOCHIP](assets/notext/09.webp)

为您的钱包选择一个名称，然后点击 "*Create Wallet*"。

![SATOCHIP](assets/notext/10.webp)

点击 "*Connected Hardware Wallet*" 按钮。

![SATOCHIP](assets/notext/11.webp)

点击 "*Scan...*" 按钮。

![SATOCHIP](assets/notext/12.webp)

您的 Satochip 应该会出现。点击 "*Import Keystore*"。

![SATOCHIP](assets/notext/13.webp)

接下来，您需要设置一个 PIN 码来解锁您的 Satochip。选择一个强密码，长度为 4 到 16 个字符之间。然后请备份这个密码。

请注意，这个密码不是助记词。这意味着即使没有这个密码，您的助记词也会允许您在必要时重新导入您的钱包到软件中。密码仅用于保护访问 Satochip 本身的安全。它等同于其他硬件钱包上的 PIN 码。

输入密码后，再次点击 "*Import Keystore*" 按钮。

![SATOCHIP](assets/notext/14.webp)

再次记录密码，然后点击 "*Initialize*" 按钮。

![SATOCHIP](assets/notext/15.webp)

您接下来将进入生成助记词的窗口。点击 “*Generate New*” 按钮。

![SATOCHIP](assets/notext/16.webp)

请将您的助记词写在纸上或金属介质上，制作一份或多份纸质副本。请注意，此助记词无需任何额外保护即可完全访问您的比特币。因此，即使他人无法接触到您的 Satochip 芯片或其 PIN 码，一旦发现此助记词，即可立即窃取您的比特币。因此，妥善保管这些备份至关重要。此外，如果您的 Satochip 芯片丢失、损坏或您忘记了 PIN 码，此助记词还能帮助您重新访问您的比特币。

![SATOCHIP](assets/notext/17.webp)

您的比特币钱包已成功创建。

![SATOCHIP](assets/notext/18.webp)

再次点击 “*Import Keystore*” 按钮。

![SATOCHIP](assets/notext/19.webp)

您的钱包现在已创建。您的私钥现在存储在 Satochip 的智能卡上。点击 “*Apply*” 按钮以继续。

![SATOCHIP](assets/notext/20.webp)

建议设置一个额外的密码来保护 Sparrow Wallet 管理的公开信息，除了您的 Satochip 的 PIN 码。这个密码将确保访问 Sparrow Wallet 的安全性，有助于保护您的公钥、地址和交易历史记录不受未经授权的访问。

![SATOCHIP](assets/notext/21.webp)

在两个字段中输入您的密码，然后点击 “*Set Password*” 按钮。

![SATOCHIP](assets/notext/22.webp)

就这样，您的 Satochip 现在已在 Sparrow Wallet 上配置完成。

![SATOCHIP](assets/notext/23.webp)

现在您的钱包已创建，您可以断开您的 Satochip。将其保管在安全的地方！

## 如何使用 Satochip 接收比特币？

在您的钱包中，点击 “*Receive*” 标签页。

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet 为您的钱包生成一个地址。通常，对于其他硬件钱包，建议点击 “*Display Address*” 以直接在设备屏幕上验证地址。不幸的是，Satochip 不提供这个选项，但请确保在您的其他钱包中使用它。

![SATOCHIP](assets/notext/25.webp)

您可以添加一个 “*Label*” 来描述将通过此地址保护的比特币的来源。这是一个好习惯，有助于您更好地管理您的 UTXO（未花费交易输出）。

![SATOCHIP](assets/notext/26.webp)

关于标签的更多信息，我还推荐查看以下教程：

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然后您可以使用这个地址来接收比特币。

![SATOCHIP](assets/notext/27.webp)

## 如何使用 Satochip 发送比特币？

现在您已经在您的 Satochip 安全钱包中收到了您的第一笔比特币，您也可以消费它！将您的 Satochip 连接到您的电脑，启动 Sparrow Wallet，然后转到 “*Send*” 标签页构建一个新的交易。

![SATOCHIP](assets/notext/28.webp)
如果您想进行币控制，即特别选择哪些 UTXO 在交易中消耗，前往 “*UTXOs*” 标签页。选择您希望消费的UTXO，然后点击 “*Send selected*”。您将被重定向到 “*Send*” 标签页的相同屏幕，但您的 UTXO 已为交易选择。

![SATOCHIP](assets/notext/29.webp)

输入目的地址。您也可以通过点击 “*+Add*” 按钮输入多个地址。

![SATOCHIP](assets/notext/30.webp)

添加一个 “*Label*”（标签），以记住这笔支出的目的。

![SATOCHIP](assets/notext/31.webp)

选择发送到此地址的金额。

![SATOCHIP](assets/notext/32.webp)

根据当前市场调整您的交易费率。

![SATOCHIP](assets/notext/33.webp)

确保您的交易所有参数都正确，然后点击 “*Create Transaction*”。

![SATOCHIP](assets/notext/34.webp)

如果一切正确无误，点击 “*Finalize Transaction for Signing*”。

![SATOCHIP](assets/notext/35.webp)

点击 “*Sign*”。

![SATOCHIP](assets/notext/36.webp)

在您的 Satochip 旁边再次点击 “*Sign*”。

![SATOCHIP](assets/notext/37.webp)

输入您的 Satochip 的 PIN 码，然后再次点击 “*Sign*” 以签名您的交易。

![SATOCHIP](assets/notext/38.webp)

您的交易现在已签名。点击 “*Broadcast Transaction*” 将其广播到比特币网络上。

![SATOCHIP](assets/notext/39.webp)

您可以在 Sparrow Wallet 的 “*Transactions*” 标签页中找到它。

![SATOCHIP](assets/notext/40.webp)

恭喜，您现在已经了解 Satochip 的用法！如果您觉得这个教程有帮助，我会很感激您在下面点个赞。欢迎在您的社交网络上分享这篇文章。非常感谢！
