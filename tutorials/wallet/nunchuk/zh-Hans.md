---
name: Nunchuk
description: 适合所有人使用的 Wallet 移动电话
---
![cover](assets/cover.webp)



## 功能强大的 Wallet


Nunchuk 于 2020 年底面世，其理念非常明确：使多重签名成为一种标准。因此，Nunchuk 的设计旨在实现非常先进的功能，其设计直接基于 Bitcoin 生态系统的参考软件 Bitcoin Core，这是一个非常有价值的选择。



经过 4 年多的开发和使用，它已经可以大规模试用了。如果你是初学者，对 Nunchuk 不熟悉，本指南将帮助你迈出第一步，发现这款软件的高级功能。本教程本身是专门为具备必要技能的中级用户编写的，他们可以按照教程中的所有步骤进行操作，但也可以启发每个人了解如何提高技能。我们将从手机版开始，指出这一点很有必要，因为 Nunchuk 的软件也可以在电脑上运行。



## 下载


第一步肯定是决定在哪里下载应用程序。请访问 [官方网站](https://nunchuk.io/)，在那里您可以找到一些文档（不多，但这是个开始）、功能介绍以及页面末尾的所有下载链接。



📌 在本教程中，我决定向你展示如何从 Github 代码库下载 Software Wallet，以及如何在手机上安装前验证版本。 **以下步骤只能在电脑上完成**，因此我建议您在台式机或笔记本电脑上完成所有这些步骤，并在完成所有验证后将".apk "文件传输到手机上。



![image](assets/en/01.webp)



如果你的技术不是很先进，可以决定从官方商店下载 `.apk`，然后直接跳到本教程的配置部分。另一方面，如果你想跃跃欲试，请继续一步一步地学习。



因此，请从您的台式电脑点击_访问我们的开放源代码库_。



该链接将带您进入 Nunchuk 的 Github 页面，在那里您可以找到许多软件仓库。我们将重点关注_nunchuk-android_这个版本库。



![image](assets/en/02.webp)



在下一个屏幕中，找到右侧的_Releases_部分，然后选择_Latest_。



![image](assets/en/03.webp)



在 _Assets_ 下，下载版本（本例中为 1.67.apk）以及 SHA256SUMS 文件和 SHA256SUMS.asc。



![image](assets/en/04.webp)



要查找开发人员的 GPG 密钥，请返回版本库的_Releases_部分，查找 1.9.53（或更早版本），其中包含获取和下载_GPG 密钥_的链接。



![image](assets/en/05.webp)



我们将通过 Sparrow wallet 提供的便捷工具进行验证，该工具有一个专用窗口，支持 PGP 签名和 SHA256 文件。



然后启动 Sparrow，从_工具_菜单中选择_验证下载_。



![image](assets/en/06.webp)



在弹出的窗口中，您可以找到需要 "填写 "的字段：选择右侧的_Browse_（浏览）按钮，然后为每个字段选择您刚从 Github 下载的相应文件。完成所有步骤后，窗口将如下所示，其中 Green 为复选标记，Hash 为清单确认。



![image](assets/en/07.webp)


**注：截图来自 Windows 电脑，同样的方法可用于电脑上的任何操作系统，只需安装 Sparrow wallet。并已验证！**



您可以找到 Sparrow wallet 指南，下载此 Software Wallet


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

然后，您可以将电脑中的 `.apk` 文件传输到手机上



![image](assets/en/08.webp)



并安装 Nunchuk



![image](assets/en/09.webp)



在手机上启动 Nunchuk 之前，先打开 Orbot，将 "新来者 "放入 Tor 下的路由应用程序列表中。



![image](assets/en/11.webp)



现在运行 Nunchuk。对于项目功能--这不是本教程的主题--Nunchuk一旦打开，就会邀请你通过电子邮件或谷歌个人资料登录。在你计划使用Nunchuk公司的高级计划之前，**避免登录**，选择_以访客身份继续_选项继续。



![image](assets/en/12.webp)



## 设置


Nunchuk（双节棍）以 "主页"（Home）窗口的形式呈现，在这里很容易理解其操作理念，我们稍后将详细介绍。



在底部可以找到菜单，第一步选择_Profile_进入设置。



![image](assets/en/10.webp)



然后选择_显示设置_，继续忽略创建账户的邀请。



![image](assets/en/14.webp)



在下面的屏幕中，您可以检查 Wallet 是否在线，是否可以连接服务器，请密切注意点击_本指南_提供的链接上的说明。



![image](assets/en/15.webp)



使用_保存网络设置_命令保存设置，返回_配置文件_菜单并选择_安全设置_。



![image](assets/en/16.webp)



在该菜单中，您可以设置如何保护应用程序的打开。为防止意外访问，您可以使用手机生物识别技术保护 Nunchuk 和/或添加安全密码。



![image](assets/en/17.webp)



还可以查看 _About_ 菜单，您可以在_Profile_ 窗口中找到该菜单。



![image](assets/en/18.webp)



这将允许您检查应用程序的版本，或在需要时联系开发人员。



![image](assets/en/19.webp)



## 密钥生成和 Wallet


从 Nunchuk 的理念中不难看出，该软件旨在成为管理多签名钱包的有用工具。为了实现这一功能，Nunchuk 允许创建 Wallet，将其与安排数字签名所需的密钥分离。



事实上，Nunchuk 的理想操作方式是创建只可观看的钱包，依赖于可以 "冷藏 "的按键。



在前面的界面中，你可能已经注意到底部有一个名为_Keys_的菜单。如果你刚刚下载了 Nunchuk，那么在 _Home_ 和 _Keys_ 中，你会看到一个大按钮，邀请你添加一个键，即 _Add Key_。



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**这就是 Nunchuk 的工作方式：** 首先，您要 generate/导入密钥，然后创建 Wallet，配置它以选择哪些密钥将授权解锁存储在它上面的资金。



即使是 Wallet singlesig，也是先创建密钥，然后才创建 Wallet。这正是我们现在要做的，从 Wallet singlesig 开始，打破僵局，探索 Nunchuk 的功能。



单击_添加密钥_



![image](assets/en/22.webp)



双节棍显示了许多支持的签名设备，但要开始使用，请选择_Software_（软件）。



![image](assets/en/23.webp)



双节棍将 generate 一个 Mnemonic 储存在设备上。然后，您需要写下备份的语序，创造最佳的环境条件，并确保您有时间安静地做好备份。软件只会显示一次 Mnemonic，无论您选择现在显示还是稍后显示，因此请选择_立即创建并备份_。



![image](assets/en/24.webp)



Nunchuk 生成 24 个单词的 Mnemonic 句子，并立即显示在下一个屏幕上



![image](assets/en/25.webp)



然后进行快速检查，要求您从 3 个选项中选出与 Mnemonic 序列中的数字相对应的正确单词。


如果您正确写入了 Mnemonic，_Continue_（继续）按钮就会开始工作。按下按钮即可继续。



![image](assets/en/26.webp)



为您的按键命名，然后按_继续_。



![image](assets/en/27.webp)



在这些步骤的最后，会询问您是否要在 Mnemonic 短语中添加 [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39)。如果您对如何使用 passphrase、安排其备份或其工作原理没有必要的了解，我建议您选择 _我不需要口令_。



![image](assets/en/28.webp)



密钥最终创建完成，并显示在菜单中：




- 使用 _Key Spec_ 时，会显示主指纹
- 您可以在右上角的三个圆点处进行设置，删除密钥或签署信息。
- 在密钥名称旁边有一个笔尖图标，点击它就可以编辑密钥名称，例如，将来可以保持密钥的顺序。
- 最后一个命令是检查密钥的健康状态：按_Run health check_键可以让程序检查密钥是否受损。



完成后，点击_Done_（放弃



![image](assets/en/29.webp)



在 _Keys_ 菜单中，你会看到第一个键出现。



![image](assets/en/30.webp)



进入 _Home_ 菜单后，会出现创建 Wallet 的选项。点击_创建新钱包_。



![image](assets/en/31.webp)



Nunchuk 向您展示了许多可能性，其中大部分与公司提供的服务有关，而这些服务并不是本教程的主题。



在本指南中，我们将通过详细说明创建_Hot Wallet 和_Custom wallet_。


让我们从_定制钱包_开始。



![image](assets/en/32.webp)



简单来说，应用程序会要求你为这个新的 Wallet 命名，并为地址选择脚本。在本教程中，我选择保留默认设置_Native segwit_。完成后，选择_Continue_（继续



![image](assets/en/33.webp)



Wallet 的配置会要求您设置用哪把钥匙来解锁 Wallet 的资金。如果有多个密钥，您将看到一个可供选择的列表。目前我们只创建了一个，因此我们选择在该密钥上打勾。在右下角，您可以看到 Nunchuk 将如何要求您设置未来的 Wallet 多重签名，从而增加_所需密钥_的数量。



![image](assets/en/34.webp)



由于我们正在创建一个单数，所以我们不选择 `1`，然后点击_继续_。



最后，会出现一个验证屏幕，您可以在此检查 Wallet 的功能：




- 名称
- 1/1 Multisig"，Nunchuk 也是这样命名 Wallet 的。
- 脚本类型，"本地 SegWit
- 钥匙 "及其指纹和派生路径



满意后，按_创建钱包_。



![image](assets/en/35.webp)



Wallet 已经创建，您可以下载 [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) 文件作为备份。要返回主菜单，请单击左上角的箭头。



![image](assets/en/36.webp)



您现在的位置是_Home_，显示的是新创建的 Wallet 报告余额和连接状态。点击蓝色区域，即可访问 Wallet 的主要功能。



![image](assets/en/37.webp)





- 右上角的镜头图标允许您进行交易搜索；
- 查看 Wallet 配置 "可进入配置菜单，在此可编辑 Wallet 名称并启用右上方的高级选项（无法截图）。在这里可以导出 Wallet 配置、标签、替换按键、更改 [gap limit](https://planb.network/en/resources/glossary/gap-limit) 等。



## 使用双节棍进行交易



奖项_获得_



![image](assets/en/38.webp)



程序会显示 Address 的 QR 码，或复制/分享 scriptPubKey 以接收链上资金。



![image](assets/en/39.webp)



在这第一架 Address 上，我们有一架 UTXO 到达、



![image](assets/en/40.webp)



但我们还是会点击 _Receive 来接收另一个。



![image](assets/en/41.webp)



目的是让您发现 Nunchuk 将新的 Address 报告为_未使用地址_，但同时也显示您有_已使用地址_及其数量。



### 用硬币控制消费交易



当第二个 UTXO 也到货后，回到 Wallet 主屏幕，查看两笔交易的状态，最重要的是，点击 _View coins_ 选项



![image](assets/en/42.webp)



在这里您将看到单个的 UTXO。在这里，您可以点击金额旁边的小箭头，选择查看其中一个UTXO。



![image](assets/en/43.webp)



并检查其到达时间、描述、UTXO 块，以便不会花掉等等。



![image](assets/en/44.webp)



但是，如果点击右上角的箭头回到_硬币_菜单，就可以打开 "硬币控制"，以更可控的方式使用UTXO。



在下面的示例中，我选择了 21,000 Sats 中的 UTXO，然后点击左下角的符号。



![image](assets/en/45.webp)



Nunchuk 会自动打开_New transaction_（新建交易）窗口来花费这笔 UTXO。在消费交易中，首先必须手动设置金额，或者选择_发送所有选定_来发送所有硬币控制余额，而不产生余额。设置好金额后，选择_继续_。



![image](assets/en/46.webp)



现在，Nunchuk 会显示在哪里粘贴要将这些资金转入的 Address，详细说明并完成交易。



![image](assets/en/47.webp)



选择 "创建交易 "可将自动收费和交易管理委托给应用程序。我建议选择_自定义交易_，以获得更多控制权。



在这个新界面中，选择




- 从发送金额中减去费用_，以防止费用被 Wallet 中的另一个 UTXO 支付、花费并产生余额（这是可避免的隐私损失）；
- 然后在资源管理器上检查后手动设置费用。



完成所有这些步骤后，点击_继续_。



![image](assets/en/48.webp)



下一个屏幕是交易的完整摘要。如果一切正常，请选择_确认并创建交易_。



![image](assets/en/49.webp)



通过_Pending signatures_（等待签名），Nunchuk 会提醒您交易p正在等待您的签名来批准支出，您可以点击_Sign_（签名）。



![image](assets/en/50.webp)



_Broadcast_ 命令出现在底部，用于传播最终完成并签名的事务。



![image](assets/en/51.webp)



### 从菜单 _Send_ 发送交易



在 Wallet 的主页面上，我们可以看到交易发出并等待确认，而我们则使用 _Send_ 菜单来模拟日常开支。



![image](assets/en/52.webp)



事实上，单击 "发送 "会弹出发送交易的屏幕，该屏幕与刚才看到的屏幕相同，但不经过硬币控制。



在第二个例子中，我决定选择_自定义交易_并发送全部金额，但我也可以手动设置。确定发送金额后，请按_继续_。



![image](assets/en/53.webp)



然后一定要确定是否从有关的 UTXO 中减去费用（在本例中，选择是被迫的，因为只有一个），根据 Mempool 中当时的情况手动调整费用，然后按_Continue_（继续）。



![image](assets/en/54.webp)



如果摘要屏幕令人满意，请选择_确认并创建交易_。



![image](assets/en/55.webp)



用 _Sign_ 签署交易



![image](assets/en/56.webp)



并传播到网络。



![image](assets/en/57.webp)



Wallet 此时余额为零，历史记录正在更新。



![image](assets/en/58.webp)



## 创建 "Hot Wallet



最后，为了不遗漏 Nunchuk mobile 初始阶段的任何内容，让我们来看看该程序如何创建所谓的 "Hot Wallet"。



在 Nunchuk 的_Home_菜单中，钱包列表出现的地方，点击右上角的 "+"。



![image](assets/en/59.webp)



从选项中选择 _热钱包



![image](assets/en/60.webp)



Nunchuk 在演示页面上提供了一些处理 Hot 钱包的建议，您可以选择_继续_继续。



![image](assets/en/61.webp)



片刻之后，Wallet 就会创建，并以棕色出现在列表中。Nunchuk 会用这种颜色提醒您尚未备份 Wallet。



![image](assets/en/62.webp)



点击 Wallet 的名称，访问其配置，您可能会注意到一个立即备份 Mnemonic 短语的邀请。



![image](assets/en/63.webp)



操作步骤与我们之前看到的相同，因此我们不再赘述。完成后，Nunchuk 会带你进入相关的密钥页面，你可以像使用_Custom_（自定义）程序一样编辑该页面。



![image](assets/en/64.webp)



还可以尝试_运行健康检查_



![image](assets/en/65.webp)



或查看如何在应用程序的首页显示所有钱包。



![image](assets/en/66.webp)



## 牢记继续独立


正如创建有一个顺序，即首先生成密钥，然后生成 Wallet，从应用程序中删除这些项目时也需要保持相反的顺序。



如果您需要删除其中一个密钥，应首先有远见地删除 Wallet 或钱包，因为它们使用其中一个签名密钥进行交易：首先删除钱包，然后才是密钥。如果不按此顺序操作，将无法删除密钥。



现在您已经知道了如何开始使用 Nunchuk，您可以继续研究这款应用程序，探索它的秘密。在本教程中，我们只是迈出了第一步，但这款 Software Wallet 还能帮助您满足更复杂的应用和更高级的需求。