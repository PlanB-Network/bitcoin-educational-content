---
name: Proton Wallet
description: 安装和使用 Proton 比特币钱包
---
![cover](assets/cover.webp)

Proton 是一家专注于数字隐私的瑞士公司，由欧洲核子研究中心 (CERN) 的科学家于 2014 年创立。Proton 以其开源解决方案而闻名，提供一系列服务，包括 Proton Mail、Proton VPN 和 Proton Drive。

Proton 近期推出了 Proton Wallet，这是一款开源的自托管比特币钱包，可通过移动应用或网页客户端访问，并与您的 Proton 账户关联。目前，该钱包的功能相对经典，具备优秀比特币钱包应有的基本工具，例如 RBF（手续费替换）、标记功能以及添加 BIP39 Passphrase（密语）的功能。

该钱包的特色功能是能够使用接收者的电子邮件地址发送比特币，Proton 会自动生成一个与用户钱包关联的空白比特币地址。Proton 计划在未来添加新功能，包括闪电网络和 CoinJoin（根据其 GitHub 代码库的活动推测，可能使用 Whirlpool）。

## 创建 Proton 账户

为了使用 Proton Wallet，您需要一个 Proton 账户。您可以按照本教程的开头步骤（仅需 “Creating a Proton account” 部分）免费创建一个账户。账户设置完成后，您可以继续学习本教程的其余部分。

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## 连接到 Proton Wallet

访问[Proton Wallet 网站](https://proton.me/wallet)，点击 "*Get Proton Wallet*"按钮。

![Image](assets/fr/01.webp)

选择 "*Free*" 订阅选项，然后点击 "*Sign In*"。

![Image](assets/fr/02.webp)

输入与您的 Proton 账户相关联的电子邮件和密码登录。

![Image](assets/fr/03.webp)

现在您的账户应该会显示出来。点击 "*Start using Proton Wallet now*"。

![Image](assets/fr/04.webp)

## 创建比特币钱包

选择账户的默认法定货币，然后点击 "*Create new wallet*"。

![Image](assets/fr/05.webp)

您的比特币钱包已创建好。理论上，您可以立即开始使用它，但首先保存您的助记符非常重要。为此，请点击界面右上角的 "*Secure your wallet*"。

![Image](assets/fr/06.webp)

如果您还没有在 Proton 上设置备份，您会被要求为您的账户设置备份，并使用 2FA 方法确保账户安全。这些安全措施虽然适用于您的整个 Proton 账户，但当您的比特币钱包集成到 Proton 账户中时，这些措施就显得更加重要了。我强烈建议您进行这些措施。

![Image](assets/fr/07.webp)

为了保存您的助记词，请点击 “*Backup this wallet's seed phrase*”。

![Image](assets/fr/08.webp)

输入您的 Proton 密码。

![Image](assets/fr/09.webp)

然后点击 "*View wallet seed phrase*"，显示钱包的助记词。

![Image](assets/fr/10.webp)

Proton Wallet 会显示您的 12 个单词的助记词。**此助记词赋予您对所有比特币的完全、无限制访问权限**。任何拥有此助记词的人都可以窃取您的资金，即使他们无法访问您的 Proton 账户。如果您丢失了账户访问权限，可以使用此 12 个单词的助记词来恢复您的比特币访问权限。因此，请务必妥善保存并将其存放在安全的地方。

您可以将其写在纸上，或者为了更加安全，我建议您将其刻在不锈钢底座上，以保护其免受火灾、洪水或跌落的损害。

![Image](assets/fr/11.webp)

如需了解如何正确保存和管理助记词，我强烈建议您参考以下教程，尤其如果您是新手：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

当然，与我在本教程中的做法不同，您绝对不能给这些字拍照。

保存助记词后，点击 "*Done*"按钮。

![Image](assets/fr/12.webp)

## 探索界面

Proton Wallet 的界面非常直观。在左侧，您可以找到不同的钱包及其关联的账户。“*Primary*” 是您的主要账户。出于保密考虑，通过 Proton 邮箱地址收到的比特币将被存入一个名为 “*Bitcoin via Email*” 的独立账户。

![Image](assets/fr/13.webp)

为了添加新账户，请点击 "*Add account*"。

![Image](assets/fr/14.webp)

为了创建新钱包，请点击 "*Wallets*" 旁边的 "*+*" 符号。

![Image](assets/fr/15.webp)

在这里您可以为新钱包添加 BIP39 Passphrase（密语）。

![Image](assets/fr/16.webp)

为了加深您对密语的理解，我推荐您阅读这篇教程：

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## 接收比特币

为了接收比特币到您的钱包，请在界面左侧选择所需的账户，然后点击 “*Receive*” 按钮。

![Image](assets/fr/17.webp)

Proton Wallet 会自动生成一个新的空白地址。

![Image](assets/fr/18.webp)

交易完成后，您可以在 “*Transactions*” 部分找到它。点击 “*+Add*” 为交易添加标签。

![Image](assets/fr/19.webp)

## 发送比特币

现在钱包里有了比特币，就可以发送了。在界面左侧选择账户，然后点击 "*Send*"。

![Image](assets/fr/20.webp)

输入收件人的比特币地址。您可以点击小徽标扫描二维码。要发送到电子邮件地址，请直接在此栏输入。输入比特币地址后，点击小箭头，然后点击 "*确认*"。

![Image](assets/fr/21.webp)

输入要发送的法定货币或比特币金额，然后点击 "*Review*"。

![Image](assets/fr/22.webp)

根据当前市场情况选择交易费用。

![Image](assets/fr/23.webp)

为交易添加标签，然后仔细检查所有细节。如果一切无误，点击 "*Confirm and send*"，签名并发送交易。

![Image](assets/fr/24.webp)

您的交易将显示在账户的 "*Transactions*" 部分，等待确认。

![Image](assets/fr/25.webp)

## 登录应用程序

除了网页客户端，Proton Wallet 还可通过移动应用访问。将钱包关联到您的 Proton 账户后，即可在网页客户端和移动应用之间同步您的钱包。

从应用程序商店下载 Proton Wallet：

- [App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548)；
- [Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

安装完成后，点击 "*Log in*"，输入您的电子邮件地址和 Proton 密码。

![Image](assets/fr/27.webp)

然后，您就可以访问您的比特币钱包，其功能与网页客户端相同。

![Image](assets/fr/28.webp)

恭喜您，现在您知道如何设置和使用质子钱包了。如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。感谢您的分享！

如果想进一步了解，我推荐您阅读 Blockstream 最新硬件钱包 Jade Plus 的教程：

https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
