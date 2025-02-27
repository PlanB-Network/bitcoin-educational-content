---
name: 质子钱包
description: 安装和使用 Proton 比特币钱包
---
![cover](assets/cover.webp)

Proton 是一家专门从事数字隐私保护的瑞士公司，由欧洲核子研究中心的科学家于 2014 年创立。Proton 以其开源解决方案著称，提供包括 Proton Mail、Proton VPN 和 Proton Drive 在内的一整套服务。

质子公司最近推出了质子钱包（Proton Wallet），这是一个开源的、自我保管的比特币钱包，可以通过移动应用程序或网络客户端与质子账户相连。目前，该钱包的功能还比较经典，具备一个优秀比特币钱包所应具备的基本工具，如RBF（*Replace-By-Fee*）、标记或添加BIP39口令的功能。

该钱包的特殊功能是可以使用收件人的电子邮件地址发送比特币，Proton 会为此自动生成一个与用户钱包相连的空白比特币地址。质子计划在未来添加新的功能，包括闪电和硬币连接（可能使用 Whirlpool，正如其 GitHub 存储库上的活动所建议的那样）。

## 创建 Proton 账户

要使用质子钱包，您需要一个质子账户。您可以按照本教程的第一步免费创建一个质子邮箱（仅 "*创建质子账户*"部分）。账户设置完成后，您就可以继续本教程的其余部分。

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
## 连接到质子钱包

访问[质子钱包网站](https://proton.me/wallet)，点击 "*获取质子钱包*"按钮。

![Image](assets/fr/01.webp)

选择 "*免费*"订阅选项，然后点击 "*登录*"。

![Image](assets/fr/02.webp)

输入与您的 Proton 帐户相关联的电子邮件和密码登录。

![Image](assets/fr/03.webp)

现在您的账户应该会显示出来。点击 "*立即开始使用质子钱包*"。

![Image](assets/fr/04.webp)

## 创建比特币钱包

选择账户的默认法定货币，然后点击 "*创建新钱包*"。

![Image](assets/fr/05.webp)

您的比特币钱包已经创建。理论上，您可以立即开始使用它，但首先保存您的助记符非常重要。为此，请点击界面右上角的 "*保护您的钱包*"。

![Image](assets/fr/06.webp)

如果您还没有在 Proton 上设置备份，您会被要求为您的账户设置备份，并使用 2FA 方法确保账户安全。这些安全措施虽然适用于您的整个 Proton 账户，但当您的比特币钱包集成到 Proton 账户中时，这些措施就显得更加重要了。我强烈建议您执行这些措施。

![Image](assets/fr/07.webp)

要保存记忆短语，请点击 "*备份此钱包的种子短语*"。

![Image](assets/fr/08.webp)

输入您的 Proton 密码。

![Image](assets/fr/09.webp)

然后点击 "*查看钱包种子短语*"，显示钱包的记忆短语。

![Image](assets/fr/10.webp)

质子钱包会显示您的 12 字记忆短语。 **这个口诀可以让您完全不受限制地使用您所有的比特币**。任何拥有该短语的人都可以盗取您的资金，即使无法访问您的 Proton 账户。如果您失去了访问您账户的权限，这个 12 个字的短语可以用来恢复您对比特币的访问。因此，仔细保存并存放在安全的地方非常重要。

您可以把它写在纸上，或者为了更安全起见，我建议把它刻在不锈钢底座上，以防火灾、水灾或倒塌。

![Image](assets/fr/11.webp)

有关保存和管理记忆短语的正确方法的更多信息，我强烈推荐大家阅读另一篇教程，尤其是初学者：

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
当然，与我在本教程中的做法不同，你绝对不能给这些字拍照。

保存短语后，点击 "*完成*"按钮。

![Image](assets/fr/12.webp)

## 发现界面

质子钱包的界面非常直观。左侧是不同的钱包及其相关账户。主要*"账户是您的主账户。为保密起见，通过 Proton 电子邮件地址收到的比特币会被存放在一个名为 "*通过电子邮件收到的比特币*"的独立账户中。

![Image](assets/fr/13.webp)

要添加新账户，请点击 "*添加账户*"。

![Image](assets/fr/14.webp)

要创建新的投资组合，请点击 "*钱包*"旁边的 "*+*"符号。

![Image](assets/fr/15.webp)

在这里您可以为新钱包添加 BIP39 密码。

![Image](assets/fr/16.webp)

要加深对口令的了解，我推荐您阅读本教程：

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
## 接收比特币

要在钱包中接收比特币，请在界面左侧选择所需的账户，然后点击 "*接收*"按钮。

![Image](assets/fr/17.webp)

然后，质子钱包会自动生成一个新的空白地址。

![Image](assets/fr/18.webp)

交易完成后，您可以在 "*交易*"部分找到它。点击 "*+添加*"，为交易指定一个标签。

![Image](assets/fr/19.webp)

## 发送比特币

现在钱包里有了比特币，就可以发送了。在界面左侧选择账户，然后点击 "*发送*"。

![Image](assets/fr/20.webp)

输入收件人的比特币地址。您可以点击小徽标扫描二维码。要发送到电子邮件地址，请直接在此栏输入。输入比特币地址后，点击小箭头，然后点击 "*确认*"。

![Image](assets/fr/21.webp)

输入要发送的法定货币或比特币金额，然后点击 "*Review*"。

![Image](assets/fr/22.webp)

根据当前市场情况选择交易费用。

![Image](assets/fr/23.webp)

为交易添加标签，然后仔细检查所有细节。如果一切无误，点击 "*确认并发送*"，签署并发送交易。

![Image](assets/fr/24.webp)

您的交易将显示在账户的 "*交易*"部分，等待确认。

![Image](assets/fr/25.webp)

## 登录应用程序

除网络客户端外，Proton 钱包还可通过手机应用程序访问。通过将钱包链接到您的质子账户，您可以在网络客户端和手机应用程序之间同步钱包。

从应用程序商店下载质子钱包：


- [在 App Store 上](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548)；
- [On Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

安装完成后，点击 "*登录*"，输入您的电子邮件地址和 Proton 密码。

![Image](assets/fr/27.webp)

然后，您就可以访问您的比特币钱包，其功能与网页客户端相同。

![Image](assets/fr/28.webp)

恭喜您，现在您知道如何设置和使用质子钱包了。如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。感谢您的分享！

如果想进一步了解，我推荐您阅读 Blockstream 最新硬件钱包 Jade Plus 的教程：

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262