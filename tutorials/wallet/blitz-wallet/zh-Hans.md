---
name: Blitz Wallet


description: 最简单的 Bitcoin 组合。
---
![cover](assets/cover.webp)



在开始使用 Wallet 时，用户体验是决定性因素之一。在本教程中，我们将向您介绍一款将用户体验作为决定性因素的 Wallet：Blitz Wallet 为您提供最简单、最完整的 Bitcoin 钱包。



## 什么是 Blitz Wallet？



Blitz Wallet 是一款源代码公开（开放源代码）的 Bitcoin 自托管 Wallet，它关注您的主权和用户体验，让您轻松上手。



[Blitz Wallet](https://blitz-Wallet.com/)是一款移动 Wallet，可在 Android（Play Store）和 iOS（App Store）上使用。



⚠️** 重要**：在官方平台上下载 Bitcoin Wallet 对于验证应用程序的真实性以及加强您的资金安全非常重要。



在本教程中，我们将以安卓版 Blitz Wallet 为基础，但下面介绍的所有过程在 iOS 上同样有效。



![installation](assets/fr/01.webp)



由于 Blitz Wallet 是 Bitcoin 的自持组合，您可以选择创建一个新的组合，或从已有的组合中导入 12/24 恢复词。



在此，我们从创建新的投资组合开始。有关备份备份短语的建议，请参阅下文。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗**重要**：这 12 / 24 个恢复单词对于访问您的比特币至关重要。如果丢失，您将无权使用比特币。



不是你的钥匙，也不是你的比特币。




然后创建一个 PIN 码来验证对 Wallet 的访问。



![setup-wallet](assets/fr/02.webp)



## 开始使用 Blitz



与其他大多数 Bitcoin 钱包相比，使用 Blitz 进行交易更加直观。



在 Wallet 菜单中，您可以看到一个简约的 Interface 菜单，该菜单只关注主要操作：



### 接收比特币



要在 Blitz Wallet 上接收比特币，请单击 "向下箭头 "图标，输入您希望接收的比特币金额，Wallet 将为您创建一个 Invoice，供您与发件人共享。



⚠️ **注**：Satoshi（或 "sat"）代表 Bitcoin 的最小单位：1 Bitcoin = 100,000,000 satoshis



Blitz Wallet 的特色之一是支持 Bitcoin 生态系统中的不同网络和频道：





- Lightning Network** ：Bitcoin 重叠之一，可让您即时进行微交易。





- Bitcoin Mainnet** ：Bitcoin 协议的主链，适用于大额交易。





- Liquid Network**：Bitcoin、Mainnet 的平行链，由 BlockStream 开发，使用 Liquid 比特币执行快速、Confidential Transactions。



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

默认情况下，您的所有交易都将在 Liquid Network 上进行，但 Blitz 允许您通过点击**选择格式**按钮来定义接收卫星币的网络。



![receive-sats](assets/fr/03.webp)



### 使用 Blitz 创建联系人



Blitz Wallet 可让您通过 Wallet 轻松发送比特币。



在**联系人**菜单中，您可以注册与您互动最多的闪电用户名或闪电 URL。



这意味着您可以绕过扫描和手动 Address 输入阶段，轻松向这些地址发送卫星数据。



![add-contacts](assets/fr/04.webp)



### 发送比特币



除了传统的比特币发送方法（二维码、手动输入）外，您还可以使用 Wallet 中预先注册的联系人，只需点击三下即可向收件人发送 Satss。



在**Wallet**菜单中，点击 "向上箭头 "按钮，选择发送比特币的方法，然后输入要发送的金额并进行确认。



目前，在闪电战 Wallet 中发送 Bitcoin 的最低金额为 1,000 萨托什。



![send-bitcoin](assets/fr/05.webp)



## 闪电战商店



除了 Bitcoin 传输操作外，Blitz Wallet 还为您提供了一个商店，您可以用比特币支付数字服务。





- 获取人工智能服务**：使用生成式人工智能模型，如Claude 3-5 sonnet、gpt-4o、gpt-4o-mini gemini-flash-1.5，并直接用比特币支付。



![ia-credits](assets/fr/06.webp)





- 在世界任何地方发送短信**：在 Blitz 商店，您可以使用 GSM 服务，在世界任何地方匿名发送短信，并以 Bitcoin 直接计费。



![sms-credit](assets/fr/07.webp)





- 上网完全保密**：在 Wallet Blitz 商店用比特币支付 WireGuard VPN（虚拟专用网络）订阅费。



![wireguard](assets/fr/08.webp)



https://planb.network/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

https://planb.network/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

## Wallet 闪电战的幕后故事：更进一步



Blitz Wallet 操作简单，但背后却蕴藏着强大的功能和个性化定制。



正如我们之前指出的，您收到的所有比特币都默认为 Liquid Network。



当您的余额少于 500,000 萨托希时，Blitz 使用 Liquid Network 小额交易所以 Satoshi 显示您的余额。



之所以采用这种方法，是因为希望为新用户提供便利的启动体验，帮助他们尽可能简单地在 Lightning Network 上进行小额交易。



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

您可以在菜单**设置>余额信息**中查看余额明细。



![balance](assets/fr/09.webp)



不过，Blitz Wallet 可以让您灵活地激活 "闪电 "模式，一旦您的余额达到 500,000 萨托希，该模式就会自动为您打开支付通道。



要激活 "闪电 "模式，请进入**设置**，然后在**技术设置**部分，点击**节点信息**选项。



![enable-lightning](assets/fr/10.webp)



激活 "闪电 "模式后，一旦满足主要条件（余额达到 500,000 萨托希或 0.005 Bitcoin），您就可以在 Lightning Network 上进行交易，而不必再通过 BlockStream 的 Liquid Network。





- 在您的商店接受 Bitcoin** ：



Bitcoin 与 Blitz Wallet 在商店中的整合仍处于试验阶段。我们建议您谨慎使用。



在**设置>销售点**菜单中，您可以设置与您的商店相关的唯一标识符，以及您希望接收付款的当地法定货币。



![pos](assets/fr/11.webp)



如果本教程有助于您掌握 Blitz，那么我们相信您也会喜欢 Muun Wallet 教程。探索 Muun，一款与 Bitcoin 一样强大的简单 Wallet。



https://planb.network/tutorials/wallet/mobile/muun-111b56b0-4872-4130-ad2e-e58f8363451d

