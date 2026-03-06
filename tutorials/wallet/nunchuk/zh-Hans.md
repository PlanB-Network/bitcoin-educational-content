---
name: Nunchuk
description: 适用于所有用户的移动钱包
---
![cover](assets/cover.webp)

## 功能强大的钱包

Nunchuk 于 2020 年底问世，其理念清晰明确：将多重签名打造为行业标准。因此，它的设计旨在实现非常高级的功能，并明智地选择直接基于比特币生态系统的参考软件 Bitcoin Core 构建。

经过四年多的开发和使用，Nunchuk 已准备好大规模应用。如果您是新手，对 Nunchuk 还不熟悉，本指南将帮助您迈出第一步，探索这款软件。在您克服最初的挑战后，即可了解其高级功能。本教程面向具备必要技能的中级用户，但他们也可以启发所有人提升技能。我们将从移动版本开始，这一点需要特别说明，因为 Nunchuk 也提供在电脑上运行的版本。

## 下载

第一步当然是决定从哪里下载应用。访问[官方网站](https://nunchuk.io/)，您可以在那里找到一些文档（虽然不多，但总算是个开始）、功能介绍，以及页面底部的所有下载链接。

📌 本教程将向您展示如何从 GitHub 代码库下载软件钱包，以及如何在将其安装到手机之前验证版本。**以下步骤只能在电脑上完成**，因此我建议您在台式机或笔记本电脑上完成所有步骤，并在所有验证完成后，将 `.apk` 文件转移到您的手机。

![image](assets/en/01.webp)

如果您不太熟悉技术，可以直接从官方应用商店下载 `.apk` 文件，然后跳到本教程的配置部分。如果您想尝试一下，请继续按照步骤操作。

因此，请在您的桌面电脑上点击“访问我们的开源代码库”。

该链接将带您进入 Nunchuk 的 GitHub 页面，您可以在那里找到许多仓库。我们将重点关注 _nunchuk-android_ 代码库。

![image](assets/en/02.webp)

在下一个屏幕上，前往右侧的  _Releases_ 部分，然后选择 _Latest_。

![image](assets/en/03.webp)

在 _Assets_ 下，下载发布版本（本例中为 1.67.apk），以及 SHA256SUMS 文件和 SHA256SUMS.asc 文件。

![image](assets/en/04.webp)

为了查找开发者的 GPG 密钥，请返回仓库的 _Releases_ 部分，查找 1.9.53（或更早版本），其中包含获取和下载 _GPG Key_ 的链接。

![image](assets/en/05.webp)

我们将使用 Sparrow Wallet 提供的便捷工具进行验证。该工具有一个专门的窗口用于此目的，并支持 PGP 签名和 SHA256 清单。

然后启动 Sparrow，从 _Tools_ 选单中选择 _Verify Download_。

![image](assets/en/06.webp)

在弹出的窗口中，您会看到一些需要 “填写” 的字段：点击右侧的 _Browse_ 按钮，然后为每个字段选择您刚刚从 GitHub 下载的相应文件。完成所有步骤后，窗口将显示如下内容，带有绿色对勾和清单文件的哈希值确认信息。

![image](assets/en/07.webp)

**注意：此屏幕截图来自 Windows 电脑，同样的操作方法也适用于您电脑上的任何操作系统，只需安装 Sparrow Wallet 即可。已验证！**

您可以参考 Sparrow Wallet 指南下载这款软件钱包：

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

然后，您可以将电脑中的 `.apk` 文件传输到手机上

![image](assets/en/08.webp)

并安装 Nunchuk

![image](assets/en/09.webp)

在手机上启动 Nunchuk 之前，先打开 Orbot，将 "Nunchuk" 添加到 Tor 下的路由应用程序列表中。

![image](assets/en/11.webp)

现在运行 Nunchuk。对于本教程未涉及的项目功能，Nunchuk 打开后会提示您使用邮箱或 Google 账户登录。在您计划使用 Nunchuk Inc. 的高级套餐之前，**请避免登录**，并选择 _Continue as guest_ 选项。

![image](assets/en/12.webp)

## 设置

Nunchuk 以 "主页"（Home）窗口的形式呈现，在这里很容易理解其操作理念，我们稍后将详细介绍。

在底部可以找到选单，第一步选择 _Profile_ 进入设置。

![image](assets/en/10.webp)

然后选择 _Display settings_，继续忽略创建账户的邀请。

![image](assets/en/14.webp)

在下面的屏幕中，您可以检查钱包是否在线，并可以连接到您的服务器，请仔细阅读点击本指南提供的链接中的说明。

![image](assets/en/15.webp)

使用 _Save network settings_ 命令保存设置，返回 _Profile_ 选单并选择 _Security settings_。

![image](assets/en/16.webp)

在该选单中，您可以设置如何保护应用程序的打开。为防止意外访问，您可以使用手机生物识别技术保护 Nunchuk 和/或添加安全密码。

![image](assets/en/17.webp)

还可以查看 _About_ 选单，您可以在 _Profile_ 窗口中找到该选单。

![image](assets/en/18.webp)

这将允许您检查应用程序的版本，或在需要时联系开发者。

![image](assets/en/19.webp)

## 密钥生成和钱包

正如从 Nunchuk 的理念中很容易看出，这款软件旨在作为一个用于管理多重签名钱包的实用工具。为了实现这一功能，Nunchuk 允许在创建钱包时，将钱包本身与用于生成数字签名的密钥分离。

实际上，Nunchuk 的理想使用方式是：创建可以作为 watch-only（只读） 的钱包，而这些钱包依赖的密钥可以被设置为 “cold”（冷钱包）。

在之前的界面中，可能已经注意到底部有一个名为 _Keys_ 的选单。如果刚刚下载 Nunchuk，在 _Home_ 和 _Keys_ 页面中都会看到一个很大的按钮，提示添加一个密钥：_Add Key_。

![image](assets/en/20.webp)

![image](assets/en/21.webp)

**这就是 Nunchuk 的工作方式：** 首先生成/导入密钥，然后创建钱包，并对其进行配置，以选择哪些密钥将授权解锁存储在其中的资金。

即使是在 单签名钱包（singlesig Wallet） 的情况下，也需要先创建密钥，然后才创建钱包。接下来我们就会按照这个顺序操作。为了先熟悉并了解 Nunchuk 的功能，我们将从创建一个单签名钱包开始，用它来打破僵局、进行初步体验。

点击 _Add Key_

![image](assets/en/22.webp)

Nunchuk 显示了许多支持的签名设备，但要开始使用，请选择 _Software_（软件）。

![image](assets/en/23.webp)

Nunchuk 将生成一个助记词，将储存在设备上。然后，您需要写下备份的语序，创造最佳的环境条件，并确保您有时间安静地做好备份。软件只会显示一次助记词，无论您选择现在显示还是稍后显示，因此请选择 _Create and backup now_。

![image](assets/en/24.webp)

Nunchuk 生成 24 个单词的助记词，并立即显示在下一个屏幕上

![image](assets/en/25.webp)

然后进行快速检查，要求您从 3 个选项中选出与助记词序列中的数字相对应的正确单词。

如果您正确写入了助记词，_Continue_（继续）按钮就会开始工作。按下按钮即可继续。

![image](assets/en/26.webp)

为您的按键命名，然后按 _Continue_。

![image](assets/en/27.webp)

在这些步骤的最后，会询问您是否要在助记词中添加[密语（passphrase）](https://planb.academy/en/resources/glossary/passphrase-bip39)。如果您对如何使用密语、安排其备份或其工作原理没有必要的了解，我建议您选择 _I don't need a passphrase_。

![image](assets/en/28.webp)

密钥最终创建完成，并显示在选单中：

- 使用 _Key Spec_ 时，会显示主指纹
- 您可以在右上角的三个圆点处进行设置，删除密钥或签署信息。
- 在密钥名称旁边有一个笔尖图标，点击它就可以编辑密钥名称，例如，将来可以保持密钥的顺序。
- 最后一个命令是检查密钥的健康状态：按 _Run health check_ 键可以让程序检查密钥是否受损。

完成后，点击 _Done_。

![image](assets/en/29.webp)

在 _Keys_ 选单中，您会看到第一个密钥出现。

![image](assets/en/30.webp)

进入 _Home_ 选单后，会出现创建钱包的选项。点击 _Create new wallet_。

![image](assets/en/31.webp)

Nunchuk 向您展示了许多可能性，其中大部分与公司提供的服务有关，而这些服务并不是本教程的主题。

在本指南中，我们将通过详细说明创建 _Hot Wallet_ 和 _Custom wallet_。

让我们从 _Custom wallet_ 开始。

![image](assets/en/32.webp)

简单来说，应用程序会要求您为这个新的钱包命名，并为地址选择脚本。在本教程中，我选择保留默认设置 _Native segwit_。完成后，选择 _Continue_。

![image](assets/en/33.webp)

钱包的配置会要求您设置用哪把钥匙来解锁钱包的资金。如果有多个密钥，您将看到一个可供选择的列表。目前我们只创建了一个，因此我们选择在该密钥上打勾。在右下角，您可以看到 Nunchuk 将如何要求您设置未来的多签名钱包，从而增加 _Required keys_ 的数量。

![image](assets/en/34.webp)

由于我们正在创建一个单签名钱包，所以我们不选择 `1`，然后点击 _Continue_。

最后，会出现一个验证屏幕，您可以在此检查钱包的功能：

- 名称
- `1/1 Multisig`，Nunchuk 也是这样命名钱包的。
- 脚本类型，`Native SegWit`
- `Keys` 及其指纹和派生路径

满意后，点击 _Create wallet_。

![image](assets/en/35.webp)

钱包已经创建好，您可以下载 [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) 文件作为备份。为了返回主选单，请点击左上角的箭头。

![image](assets/en/36.webp)

您现在的位置是 _Home_，显示的是新创建的钱包报告余额和连接状态。点击蓝色区域，即可访问钱包的主要功能。

![image](assets/en/37.webp)

- 右上角的镜头图标允许您进行交易搜索；
- `View Wallet config` 可进入配置选单，在此可编辑钱包名称并启用右上方的高级选项（无法截图）。在这里可以导出钱包配置、标签、替换按键、更改[间隙限制（gap limit）](https://planb.academy/en/resources/glossary/gap-limit) 等。

## 使用 Nunchuk 进行交易

点击 _Receive_。

![image](assets/en/38.webp)

应用程序会显示地址的二维码，或复制/分享 scriptPubKey 以接收链上资金。

![image](assets/en/39.webp)

在这个第一个地址上，我们收到了 UTXO、

![image](assets/en/40.webp)

但我们还是会点击 _Receive_ 以再接收比特币。

![image](assets/en/41.webp)

目的是让您发现 Nunchuk 将新的 Address 报告为_未使用地址_，但同时也显示您有_已使用地址_及其数量。

### 用币控制（Coin Control）消费交易

收到第二个 UTXO 后，回到钱包主屏幕，查看两笔交易的状态，最重要的是，点击 _View coins_ 选项

![image](assets/en/42.webp)

这里将显示各个 UTXO。您可以点击金额旁边的箭头来选择查看特定的 UTXO。

![image](assets/en/43.webp)

并检查UTXO到达时间、描述、UTXO 和区块，以免被花费等等。

![image](assets/en/44.webp)

但是，如果点击右上角的箭头回到 _Coins_ 选单，就可以打开 "Coin Control"，以更可控的方式使用UTXO。

在下面的示例中，我选择了 21,000 聪的 UTXO，然后点击左下角的图标。

![image](assets/en/45.webp)

Nunchuk 会自动打开 _New transaction_ 窗口来花费此UTXO。在花费交易中，您必须首先手动设置金额，或者选择 _Send all selected_ 来发送所有币种控制余额，而不会产生剩余金额。设置好金额后，选择 _Continue_。

![image](assets/en/46.webp)

现在，Nunchuk 会显示粘贴收款地址的位置，您可以填写交易描述并完成交易。

![image](assets/en/47.webp)

选择 _Create transaction_ 会将手续费和交易管理自动委托给应用程序。我建议选择 _Custom transaction_ 以获得更多控制权。

在这个新界面中，请务必选择：

- _Subtract fee from send amount_,，以防止钱包中其他 UTXO 支付手续费，从而避免手续费被消耗并产生剩余金额（这会造成不必要的隐私泄露）；

- 然后，在浏览器中查看后手动设置手续费。

完成以上步骤后，点击 _Continue_。

![image](assets/en/48.webp)

下一个界面是完整的交易详情。如果一切正常，请选择 _Confirm and create transaction_ 进行确认。

![image](assets/en/49.webp)

通过 _Pending signatures_（等待签名），Nunchuk 会提示您该交易正在等待您的签名以批准支出，点击 _Sign_ 即可完成签名。

![image](assets/en/50.webp)

_Broadcast_ 命令将出现在底部，用于传播最终完成并签名的交易。

![image](assets/en/51.webp)

### 从 “Send” 选单进行消费交易

在钱包主页上，我们可以看到交易正在发送并等待确认。我们使用 _Send_ 选单来模拟日常支出。

![image](assets/en/52.webp)

点击 _Send_ 后，会弹出发送交易的界面，与刚才看到的界面相同，但无需经过币种控制。

在这个例子中，我选择了 _Custom transaction_ 并发送了全部金额，但也可以手动设置金额。确定发送金额后，点击 _Continue_。

![image](assets/en/53.webp)

然后，务必确认是否从该 UTXO 中扣除手续费（本例中由于只有一个 UTXO，因此选择是强制性的），根据 Mempool 中的实际情况手动调整手续费，然后点击 _Continue_。

![image](assets/en/54.webp)

如果详情正确无误，请选择 _Confirm and create transaction_。

![image](assets/en/55.webp)

点击 _Sign_ 以签名交易

![image](assets/en/56.webp)

并将其广播到比特币网络。

![image](assets/en/57.webp)

钱包此时余额为零，历史记录正在更新。

![image](assets/en/58.webp)

## 创建热钱包

最后，为了确保 Nunchuk 移动版初始阶段的顺利进行，我们来看看它是如何创建应用内所谓的“热钱包”的。

在 Nunchuk 的 _Home_ 选单中，也就是钱包列表所在的位置，点击右上角的 `+` 号。

![image](assets/en/59.webp)

从选项中选择 _Hot wallet_ 

![image](assets/en/60.webp)

Nunchuk 在演示页面上提供了一些处理 Hot 钱包的建议，您可以选择_继续_继续。

![image](assets/en/61.webp)

稍等片刻，钱包就会创建完成，并以棕色显示在列表中。这是 Nunchuk 用来提醒您尚未备份钱包的颜色。

![image](assets/en/62.webp)

点击钱包的名称，访问其配置，您可能会注意到一个立即备份助记词的邀请。

![image](assets/en/63.webp)

操作步骤与我们之前看到的相同，因此我们不再赘述。完成后，Nunchuk 会带您进入相关的密钥页面，您可以像使用 _Custom_（自定义）程序一样编辑该页面。

![image](assets/en/64.webp)

还可以尝试点击 _Run health check_。

![image](assets/en/65.webp)

或者查看如何在应用程序的 _Home_ 中显示所有钱包。

![image](assets/en/66.webp)

## 请记住，要独立完成后续步骤

就像创建过程有顺序一样，即先生成密钥，再创建钱包，删除这些项目时也需要遵循相反的顺序。

如果您需要删除某个密钥，首先应该删除使用该密钥进行交易的钱包：先删除钱包，再删除密钥。如果您不遵循此顺序，将无法删除密钥。

现在您已经了解了 Nunchuk 的入门方法，可以继续学习这款应用，探索它的更多功能。本教程仅介绍了基本步骤，但这款软件钱包还能满足您更复杂的应用和更高级的需求。
