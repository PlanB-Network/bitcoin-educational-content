---
name: Minibits Wallet
description: Minibits Wallet 指南
---

![cover](assets/cover.webp)


在本教程中，我将指导您设置 Minibits Wallet 以使用 ecash。这是一种功能强大、注重隐私的支付技术，可与 Bitcoin 同时使用。Minibits 是一种 ecash 和 Lightning Wallet，可实现即时、廉价和私密的价值转移，是注重隐私的日常交易的理想选择。


在我们深入研究 Minibits 之前，让我们先清楚地了解什么是 ecash，什么不是 ecash。很多人把 ecash 与 Bitcoin 或 Blockchain 技术混为一谈，但它们是根本不同的概念。


Ecash 不是 Bitcoin。它不会取代您自行保管的 Bitcoin Wallet，而是对它的补充。电子现金不是 Blockchain，也不存在于任何公共 Ledger。有趣的是，Ecash 并不是一项新技术--它实际上早于全球网络，其概念在 20 世纪 80 年代和 90 年代就已提出。


ecash的特点：难以置信的私密性（交易不会留下可追踪的历史）、点对点（直接转账，无需中间人），并具有数字无记名工具的功能（如果你拥有它，你就控制了它）。ecash的一个主要优势是可以离线使用--在交易过程中，发送方或接收方都可以断开与互联网的连接。ecash可以由单方或可信实体联盟铸造，是Bitcoin的完美补充技术，可以处理小额、频繁的交易，而Bitcoin则充当结算Layer。


请注意，Minibits 设置是一种 "托管解决方案"，这意味着您信任 Mint 运营商来管理您的资金。这将带来特定风险，您必须在继续操作前了解清楚。


该项目显示了这一重要的免责声明：


- 本 Wallet 仅用于研究目的。
- Wallet 是一个测试版，功能不完整，存在已知和未知的错误。
- 请勿与大额现金一起使用。
- 存储在 Wallet 中的现金由造币厂发行
- 您相信造币厂会用 Bitcoin 支持它，直到您将持有的 Bitcoin 转到另一个 Bitcoin 闪电 Wallet。
- Wallet 所执行的卡舒协议尚未经过广泛的审查或测试。


将 Minibits 视为日常 Wallet，而不是储蓄账户，切勿在此存储大量价值。


## 1️⃣设置您的 Wallet


首先，请访问[Minibits 网站](https://www.minibits.cash/)，在那里你可以找到所有主要平台的下载选项。iOS 用户可以从[App Store](https://testflight.apple.com/join/defJQgTD)下载，而欧盟 iOS 用户还可以从[Freedom Store](https://freedomstore.io/)安装。安卓用户可以从[Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet)获取应用程序，或直接从[GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases)页面下载 APK 文件。


安装 Minibits 时，您将看到解释基本概念的介绍性屏幕--如果您已经熟悉该技术，可以通读或跳过这些屏幕。完成这些初始步骤后，系统会提示您在以下两个选项中进行选择：


- 为新用户提供 "找到了，带我去 Wallet "或
- 恢复丢失的 Wallet`（如果从备份恢复）。


![image](assets/en/01.webp)

完成初始设置后，您将进入主屏幕，其中有几个重要的 Elements 注意事项。顶角的 "个人资料 "图标将带您进入个人资料页面，您可以在此访问您的 Minibits Wallet Address 并选择 "批量接收 "选项。② 在屏幕中间，您将看到可以使用的薄荷糖，默认选择 Minibits 薄荷糖。下面的操作行提供了发送 ecash 或闪电付款、扫描二维码和接收付款的选项。最后，底部导航栏包含主屏幕、交易历史、联系人和设置的快捷方式。


![image](assets/en/02.webp)


## 2️⃣管理薄荷糖


默认情况下，启动应用程序时会启用 Minibits 造币厂。然而，ecash 的优势之一是能够使用多个铸币厂，以提高分散性和安全性。要添加另一个铸币厂，请导航到 "设置"，然后选择 "管理铸币厂"，最后点击 "添加铸币厂"。


[Bitcoinmints.com]（Bitcoinmints.com）提供了一份全面的可用铸币厂列表，并附有用户评级，帮助您选择信誉良好的铸币厂。使用多个铸币厂可以降低风险。如果一个造币厂出现问题，您在其他造币厂的资金仍然可以使用。


![image](assets/en/04.webp)


## 3️⃣创建备份


备份可以说是整个设置过程中最关键的一步。要访问 "备份 "选项，请导航至 "设置"->"备份"，您会在这里找到两个重要选项：

1.您的 seed 短语 "包含 "12 个单词"，允许您在设备丢失时恢复您的现金余额。此 seed 短语是您在所有已添加的造币厂中使用所有 ecash 的万能钥匙。将其写在物理介质（纸张或金属）上，并安全地存储在多个位置。切勿将您的 seed 短语以数字形式存储，以免泄露。考虑访问此 [教程](https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) 以了解保护您的 Wallet 的最佳做法。

2.Wallet backup"，其中包含一个长备份字符串。


**注意**：使用此备份恢复 Wallet 时，您仍然需要 seed 的短语。


![image](assets/en/05.webp)


## 4️⃣ 创建 Minibits Wallet Address


下一步导航至底部的 "联系人"，然后点击 "更改"->"更改 Wallet Address"，自定义您的专用 "Minibits Wallet Address"。输入您喜欢的 Address 并检查可用性。


![image](assets/en/07.webp)


设置完 Address 后，系统会提示您支付小额 "捐款 "以支持该项目。虽然这是可选项，但我强烈建议如果您计划经常使用该服务，可以考虑捐款。像 Minibits 这样的开源项目依赖社区支持来继续开发和维护。即使是微薄的捐款也有助于确保项目的长久性。


![image](assets/en/08.webp)


## 5️⃣ Nostr 设置


如果您想给您在 Nostr 上关注的人支付小费，您可以通过选择 "联系人"，然后选择 "公开 "来 "添加您的 npub 密钥"。这将把您的 Minibits Wallet 连接到 Nostr 社交网络，实现无缝小费支付。


您也可以选择 "使用自己的配置文件"，进入 "设置"，然后进入 "隐私"，导入自己的 Nostr Address 和密钥。但请注意，这样做将会阻止您的 Wallet 与 minibits.cash Nostr 和 LNURL Address 服务器通信，从而禁用闪电 Address 功能以接收 ZAP 和付款。


![image](assets/en/09.webp)


## 6️⃣接收资金


要初始接收资金，您需要通过闪电 Invoice 为 Wallet 充值。这个过程很简单：点击 "充值"，输入要充值的 "金额"，选择添加 "备忘录"，然后点击 "创建 Invoice"。然后，您需要使用另一个闪电 Wallet 支付这个 Invoice，这样就可以将 Bitcoin 闪电支付转换成 Minibits Wallet 中的 ecash 代币。


![image](assets/en/10.webp)


## 7️⃣发送资金


现在您已经为 Wallet 注资，您可以通过两种不同的方式发送资金。


### 发送现金


第一个选项是直接发送 ecash。点按 "发送"，然后选择 "发送 ecash"，输入 "金额"，然后点按 "创建 token. "这将 generate 一个二维码，您可以与收件人共享或让他们直接用设备扫描。收件人几乎可以立即看到代币出现在他们的 Wallet 中，没有 Blockchain 费用或确认延迟。


![image](assets/en/11.webp)


### 使用闪电支付


第二个选项是通过闪电支付。点击 "发送"，然后选择 "使用闪电支付"。你可以从 Nostr 的 "联系人 "中选择（如果你已经连接了 npub），或者使用 "粘贴 "或 "扫描 "选项输入/粘贴闪电 Address、Invoice 或 LNURL 付款代码。确认收件人后，系统会提示你输入 "要支付的金额"，可选择添加备注，然后点击 "确认"，再点击 "立即支付 "完成闪电交易。


![image](assets/en/12.webp)


## 8️⃣ 创建 NWC 连接


Minibits 的另一个强大功能是创建 "Nostr Wallet Connect (NWC) "连接，允许其他应用程序从您的 Wallet 请求付款，而无需暴露您的私钥。


要进行设置，请进入 "设置"，然后选择 "Nostr Wallet Connect"，再点击 "添加连接"。给连接起一个描述性的名字，以识别应用程序和相关用户账户。设置合理的每日最大限额，以控制通过此连接的消费金额，然后点击`保存`完成设置。


这项功能对 Nostr Clients 等服务特别有用，因为在这些服务中，您可以启用自动小费功能，而无需手动批准每笔交易。


![image](assets/en/12.webp)


## 🎯 结论


Minibits 是进入电子现金世界的一个便捷入口，提供注重隐私的支付方式，与您持有的 Bitcoin 相得益彰。请记住始终保持适当的备份，考虑使用多个铸币厂以实现冗余，并只在此托管解决方案中存储适当的金额。


有关其他资源，请查看 Minibits GitHub 存储库、官方网站和 Telegram 频道，社区成员会在该频道积极讨论开发工作并排除故障。


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Website](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


ecash生态系统仍在不断发展，但Minibits等工具正使越来越多的普通用户可以使用这一强大的隐私技术。