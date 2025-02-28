---
name: 冷卡

description: 使用冷卡设备和比特币核心创建、备份和使用比特币私钥
---

![封面](assets/cover.webp)

使用冷卡设备和比特币核心创建、备份和使用比特币私钥

## 使用冷卡生成私钥并通过比特币核心节点界面使用的完整指南！

比特币网络使用的核心是非对称加密的概念：一对密钥 - 一个私钥和一个公钥 - 用于加密和解密数据，这一概念确保了通信的机密性。

在比特币的情况下，通过生成这样一对私钥和公钥，我们能够存储比特币（UTXO或未花费交易输出）并签署交易以花费它们。

如今，有多种工具可用于随机生成私钥并使用BIP 39标准以文本形式备份，该标准确定了钱包如何将助记词（种子短语）与加密密钥关联。通常，助记词由12个或24个单词组成，必须安全地备份，以便能够恢复钱包及其比特币。

在本文中，我们将学习如何使用冷卡Mk4生成私钥，这是比特币世界中最广泛使用和最安全的设备之一，使用掷骰子方法来确保最大的熵，并且学习如何以隔离网络的方式与比特币核心一起使用！

> 🧰| 获取以下工具以跟随指南：
>
> - 冷卡设备（Mk3或Mk4）
> - MicroSD卡（4GB就足够了）
> - 仅供电源使用的磁性USB线（Mk3为mini-usb，Mk4为usb-c）
> - 一个或多个高质量骰子

## 使用冷卡生成新的助记词

我们将从头开始创建私钥的过程，假设一个刚拆包的冷卡，其中已经设置了PIN（在设备初始化期间按照冷卡上的步骤操作）。

> 🚨 | 要重置已配置冷卡的私钥，请按照以下步骤操作：
> 高级/工具 > 危险区 > 种子功能 > 销毁种子 > ✓
> _注意_：按照这些步骤，您的冷卡将忘记私钥。如果您想以后能够恢复它，请确保已正确备份您的助记词。

## 要遵循的步骤：

连接到带PIN的冷卡 > 新种子词 > 24词骰子滚动

执行100次骰子滚动，每次滚动后在冷卡上记录从1到6获得的结果。通过实践这种方法，你创建了256字节的熵，从而有利于创建一个完全随机的私钥。Coinkite还提供了必要的文档，用于独立验证他们的熵生成系统。

![视觉冷卡截图](assets/guide-agora/1.webp)

完成100次骰子滚动后，按✓，然后按顺序记下获得的24个单词。验证两次并按✓。最后，只需完成冷卡上的24个单词的验证测试，那么，您的新私钥就创建成功了！

接下来，选择是否激活NFC（Mk4）和USB功能，按照显示的步骤操作。一旦进入主菜单，现在是更新设备固件的时候了。转到高级/工具 > 升级固件 > 显示版本，并检查官方网站以验证并下载最新可用版本。建议更新冷卡，以便从最大安全性中受益。
在继续之前，建议记录与私钥关联的主密钥指纹（XFP）。这个数据允许您在恢复钱包时快速验证是否处于正确的钱包中。请前往高级/工具 > 查看身份 > 主密钥指纹（XFP），并记下获得的八个字母数字字符序列。XFP可以和助记词短语记录在同一个地方，它不是敏感数据。
> 💡 建议在不同的软件中测试您的助记词备份。为了安全地进行此操作，请参阅我们的文章，在不到5分钟内使用Tails验证比特币钱包的备份。

## 安全加成：「秘密短语」（可选）

'密码短语（秘密短语）是增加钱包配置安全层的绝佳元素，用以保护您的比特币。密码短语充当助记词短语的第25个词。一旦添加，将创建一个全新的钱包，连同一个私钥和其关联的助记词短语。不需要记录新的助记词短语，因为可以通过将初始助记词短语与选定的密码短语结合来访问此钱包。

目标是将密码短语与助记词短语分开记录，因为如果攻击者同时获取这两项内容，他们将能够访问资金。另一方面，如果攻击者只能访问这两项内容中的一项，他们将无法访问资金，这一特定优势优化了钱包配置的安全级别。

![添加密码短语会导致一个完全不同的钱包](assets/guide-agora/2.webp)

## 使用Coldcard添加密码短语的步骤：

密码短语 > 添加词语（推荐）> 应用。设备将显示带有密码短语的新生成钱包的XFP，出于前面提到的相同原因，应该与密码短语一起记录下来。

> 💡 与密码短语相关的额外资源：

    https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af
    https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/
    https://armantheparman.com/passphrase/

## 将钱包导出到Bitcoin Core

钱包现在已经准备好导出到软件中，以便与比特币网络进行交互。在本指南中，我们将使用Bitcoin Core（v24.1）。

请参考我们的Bitcoin Core安装和配置指南：

> 使用Bitcoin Core运行您自己的节点 - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> 为Bitcoin Core节点配置Tor - https://agora256.com/configuration-tor-bitcoin-core/

首先，将微型SD卡插入Coldcard，然后按照以下步骤为Bitcoin Core导出钱包：高级/工具 > 导出钱包 > Bitcoin Core。两个文件将被写入微型SD卡：bitcoin-core.sig & bitcoin-core.txt。将微型SD卡插入安装了Bitcoin Core的计算机，并打开.txt文件。您将看到“对于带有主密钥指纹的钱包。”的行。验证八字符XFP是否与创建私钥时记录的匹配。
在按照文件中的说明操作之前，让我们首先按照以下步骤在比特币核心(Bitcoin Core)界面中准备钱包：转到文件(File)标签 > 创建钱包(Create a wallet)。为您的钱包选择一个名称（在Core中与“porte-monnaie”可互换）并勾选选项 禁用私钥(Disable private keys)、创建一个空钱包(Create an empty wallet)以及钱包描述符(Wallet descriptors)如下图所示。然后，按创建(Create)按钮。
![创建钱包](assets/guide-agora/3.webp)

一旦在比特币核心(Bitcoin Core)中创建了钱包，转到窗口(Window)标签 > 控制台(Console)并确保页面顶部显示的选定钱包名称是您创建的那个。

现在，在Coldcard之前生成的.txt文件中，复制以importdescriptors开头的行，然后将其粘贴到比特币核心(Bitcoin Core)控制台中。应返回包含行 "success": true 的响应。

![节点窗口](assets/guide-agora/4.webp)

如果响应包含 "message": "Ranged descriptors should not have a label"，请在从.txt文件复制的行中擦除条目 "label": "Coldcard xxxx0000"，然后将完整行再次粘贴回比特币核心(Bitcoin Core)控制台。

帮助：[https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md](https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md)

## 在比特币核心(Bitcoin Core)中验证钱包导入

为确保操作成功，有必要验证所需的钱包已导入到比特币核心(Bitcoin Core)中。确认这一点的一个简单方法是验证Coldcard生成的地址与比特币核心(Bitcoin Core)生成的地址是否匹配。

比特币核心(Bitcoin Core)：接收 > 创建一个新的接收地址
Coldcard：地址浏览器(Address Explorer) > 选择以bc1q开头的地址。Coldcard地址 'bc1q' 应与比特币核心(Bitcoin Core)显示的地址匹配。
以“隔空”模式接收和发送交易

接收交易非常简单；只需按接收(Receive)，标记交易（可选但推荐），并创建一个新的接收地址。然后，剩下的就是与发送者分享地址。

现在，这种Coldcard + 比特币核心(Bitcoin Core)设置的关键元素是在Coldcard及其私钥未连接到互联网的情况下发送交易，这种方法称为隔空(air-gapped)，使用了TBSP（PSBT - 部分签名比特币交易）功能。
本质上，我们使用比特币核心(Bitcoin Core)界面构建交易，然后通过微型SD卡将其导出到Coldcard进行签名，然后将签名的交易文件返回到比特币核心(Bitcoin Core)并广播交易到网络。我们必须这样做，因为导入到比特币核心(Bitcoin Core)的钱包没有私钥，只有公钥（这允许我们生成我们的接收地址），所以我们不可能直接在软件中签署交易来花费我们的比特币。

在继续之前，请确保在设置 > 钱包(Settings > Wallet)中启用了以下选项：

> - 启用币控制功能(Enable coin control features)
> - 花费未确认的币(Spend unconfirmed coins)（可选）
> - 启用TBPS检查(Enable TBPS checks)

![选项](assets/guide-agora/5.webp)

### 以隔空模式发送的步骤：
发送 > 输入 > 选择所需的utxo，然后在支付给处输入收件人的地址。交易费用：选择... > 自定义 > 输入交易费用（比特币核心以sats/kilobyte计算，而不是像大多数其他钱包解决方案那样以sat/byte计算。所以4000 sats/kilobyte = 4 sats/byte）。创建一个未签名的交易 > 保存文件到您的微型SD卡并将其插入Coldcard。
在Coldcard中，按准备签名，验证交易详情，然后按 ✓ 并在生成签名文件后将微型SD卡重新插入计算机。

回到比特币核心，在文件选项卡中 > 从文件加载TBSP，并输入签名的交易文件 .psbt。PSBT操作框将出现在屏幕上，确认交易已完全签名并准备广播。剩下的就是按广播交易。

![PSBT操作](assets/guide-agora/6.webp)

### 结论

Coldcard设备与运行您自己节点的比特币核心的结合是强大的。再加上用100次骰子掷出的私钥和一个秘密短语，您的钱包配置变成了一个复杂且坚固的堡垒。

欢迎联系我们分享您的评论和问题！我们的目标是分享知识，日复一日地提高我们的理解。