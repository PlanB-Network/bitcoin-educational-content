---
name: Macadamia Wallet
description: 用于匿名即时 BTC 支付的 Cashu 移动 wallet
---

![cover](assets/cover.webp)



Macadamia Wallet 是一款 iOS 移动 wallet，它实现了卡舒协议（Cashu 协议），这是一种实现完全匿名 Bitcoin 支付的超微生态现金系统。由于采用了盲签名技术，任何人都无法将您的存款与消费联系起来，从而提供了与实物现金类似的保密性。



在本教程中，我们将学习如何安装和配置 Macadamia、执行首次卡舒交易（薄荷、发送、接收、融化）以及管理多个薄荷以确保资金安全。



## 什么是澳洲坚果 Wallet？



### 卡舒协议



卡舒使用的是大卫-查姆发明的盲签名技术：用户将比特币存入 "造币厂 "服务器，"造币厂 "会发行等值的萨托希代币。造币厂在看不到代币内容的情况下签署这些代币，因此无法将 token 与用户联系起来。交易所是点对点的 off-chain，完全不透明--甚至造币厂也无法追踪谁在向谁付款。



Macadamia 是用 Swift/SwiftUI 开发的开源 wallet iOS。它无需账户或 KYC 即可运行，令牌存储在本地并受 seed 短语保护。代码可在 GitHub 上进行审计，代币可与其他 Cashu 钱包（Minibits、Cashu.me）互操作。



### 托管模式与妥协



**重要**：卡舒以托管模式运作。代币是由铸币厂的 Bitcoin 储备支持的支付承诺（欠条）。如果造币厂消失，您的代币也将失去价值。这是最大限度保密的折衷方案。



将 Macadamia 用作实物 wallet：仅限少量。将资金分散到几种薄荷糖中，以稀释风险。



## 主要特点



Macadamia 实现了卡舒协议的四个基本操作。 **Mint** 通过 "闪电 "发票将您的萨托希兑换成代币。 **发送**可让您通过二维码或链接免费发送代币，完全采用 off-chain。 **接收**可让您接收代币或 generate 闪电发票。 *熔化***通过销毁代币来支付闪电发票。



wallet 支持同时管理多个铸币厂。您可以通过 Lightning 在不同铸币厂之间交换代币。



## 支持的平台



Macadamia 仅适用于 iPhone 和 iPad 的 iOS 17 或更高版本。本机 Swift/SwiftUI 应用程序可与苹果生态系统实现最佳集成。



Cashu 协议保证了钱包之间的互操作性。您可以在其他应用程序（如安卓上的 Minibits 或桌面上的 Nutstash）中恢复 seed 短语。



当前版本通过 TestFlight 发布。该测试版只能少量使用。



## 安装



Macadamia 目前可通过苹果的测试计划 TestFlight 下载。以下是安装方法：



### 通过 TestFlight 安装



**步骤 1：下载 TestFlight**



如果你的设备上还没有 TestFlight 应用程序，请在 App Store 中搜索 "TestFlight "并安装。TestFlight 是苹果的官方应用程序，用于测试 iOS 应用程序的测试版。



**步骤 2：加入 Macadamia 测试计划**（法语）



安装 TestFlight 后，请在 iPhone 或 iPad 上使用此邀请链接：[https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



该链接将自动打开 TestFlight 并为您提供安装 Macadamia Wallet 的服务。点击 "接受"，然后点击 "安装 "开始下载。应用程序重约 10 兆字节，安装只需几秒钟。



![Installation TestFlight](assets/fr/01.webp)



### 关于测试版的重要信息



Macadamia 仍处于积极开发阶段。TestFlight 版本会经常更新，可能会引入新功能或修正错误。不过，与任何测试版一样，可能会出现故障。 *我们强烈建议您只使用少量**，因为一旦出现技术问题，您可能会丢失这些**。



根据显示的隐私政策，Macadamia 不会收集任何用户数据。安装时请务必检查开发商是否为 cypherbase UG。



## 初始配置



首次启动时，Macadamia 会生成一个包含 12 个单词的 BIP-39 句子。把它们写在安全的地方，千万不要截图。通过这些单词，您可以重新创建 wallet，并花费代币。



![Configuration initiale](assets/fr/02.webp)



请按照四个步骤操作：欢迎、接受条款、保存 seed 句子和最终确认。



![Interface principale](assets/fr/03.webp)



配置完成后，Macadamia 会显示三个主要选项卡。 **Wallet** 显示您的余额和交易历史。 **Mints** 让您管理您的卡舒服务器。 *设置*** 可以访问设置和您的 seed 短语。



![Ajout d'un mint](assets/fr/04.webp)



现在，你需要配置一个铸币厂，也就是将发行代币的卡舒服务器。进入 "铸币厂 "选项卡，点击 "添加新的铸币厂URL"，然后输入你选择的铸币厂地址（例如：mint.cubabitcoin.org）。查看 bitcoinmints.com 或 cashu.space，了解信誉良好的公共铸币厂。仅验证您已检查过其信誉的造币厂，因为它们将保管您的比特币。



## 日常使用



### 创建新代币（造币厂）



要向 wallet Macadamia 输送 ecash，您需要执行 "Mint "操作（创建代币）。触摸 "接收"，然后选择 "闪电 "选项。输入所需金额（如 1000 sats），选择要使用的薄荷糖，然后点击 generate 闪电发票。



![Opération Mint](assets/fr/05.webp)



使用您常用的 wallet（Phoenix、Zeus、BlueWallet）支付生成的 "闪电 "发票。



![Confirmation Mint](assets/fr/06.webp)



支付后，卡舒代币会立即出现在您的余额中。



### 发送代币



要向其他用户发送卡舒代币，请触摸主屏幕上的 "发送 "按钮，然后选择 "Ecash"。输入要发送的金额（如 50 sats），并根据需要添加说明性备注。



![Envoi Ecash](assets/fr/07.webp)



通过 iMessage、Signal 或 Telegram 分享二维码或生成的文本。收款人可立即免费领取资金。



### 接收代币



要接收其他用户发送的 Cashu 代币，请触摸 "接收"，然后选择 "Ecash"。扫描 token QR 代码或粘贴您收到的 token 链接。



![Réception Ecash](assets/fr/08.webp)



触摸 "Redeem "可申请 token。



### 闪电（融化）付款



要使用卡舒代币支付 "闪电 "发票，请点击 "发送"，然后选择 "闪电"。粘贴您要支付的 BOLT11 发票。



![Paiement Lightning](assets/fr/11.webp)



造币厂销毁您的代币并执行闪电支付。因此，您可以匿名支付任何闪电服务。



### 交换薄荷糖



当您从未曾配置过的铸币厂收到代币时，Macadamia 会为您提供多个管理代币的选项。



![Swap inter-mints](assets/fr/09.webp)



添加新造币厂或将代币交换到现有造币厂。交换使用 "闪电 "作为匿名转账的桥梁。



### 先进的多铸币厂管理



Macadamia 提供先进的工具，可同时管理多个造币厂，并对资金进行战略性分配。



![Gestion multi-mints](assets/fr/10.webp)



"分配资金 "根据百分比自动分配您的余额（例如 50/50）。"转账 "允许在铸币厂之间手动转账，以分散风险。



## 优势和局限性



**亮点** ：





- 最高保密性**：即使是造币厂也无法追踪交易。无区块链元数据，无迹可寻的点对点交换。
- 快速免费**：薄荷糖内免费即时转账，是小额支付的理想选择。
- 互操作性**：与其他兼容钱包（Minibits、Nutstash）一起使用的标准化卡舒代币。
- 简单**：Interface iOS 本机适合初学者使用，同时仍可进行审计（开源）。



**制约因素** ：





- 托管模式**：需要信任铸币厂。如果铸币厂消失，您的代币就会失去价值。
- 仅限 iOS**：没有安卓/桌面版本。卡舒互操作性允许通过其他钱包访问，但最佳体验仍是 iOS。
- 薄荷依赖性**：Mint 离线 = 无法执行需要其干预的交易（Mint、Melt）。
- 新兴技术** ：正在开发中，可能存在错误，标准在不断演变。



## 最佳做法





- 分散您的铸币厂**：将您的筹码分散到几家信誉良好的造币厂，以稀释风险。
- 限制金额**：将 Macadamia 用作日常支付的实物 wallet，而不是保险箱。
- 保管好你的 seed**：将 12 个字的短语写在纸上，放在安全的地方。偶尔测试恢复情况。
- 检查薄荷**：在添加铸币厂之前，请咨询cashu.space和社区论坛。选择正常运行时间长、声誉好的造币厂。
- VPN 或 Tor**：使用 VPN/Tor 隐藏你的 IP，最大限度地保护网络隐私。
- 加入社区**：加入社区**：Telegram/Discord Cashu 群组，了解最新信息、薄荷建议和最佳实践。



## 结论



Macadamia Wallet 为数字 Bitcoin 带来了实体现金的特性。通过结合 Chaum 和 Lightning 盲签名，它为交易保密提供了一个优雅的解决方案。它的本地 iOS 界面使复杂的加密技术成为可能，同时保持开源并与卡舒生态系统互操作。



托管模式需要警惕性和良好的安全措施。如果使用得当，Macadamia 将成为需要匿名的日常支付的重要工具，并与用于储蓄的非托管钱包相辅相成。



## 资源



### 正式文件




- 官方网站：[macadamia.cash](https://macadamia.cash)
- 澳洲坚果常见问题：[macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub 源代码：[github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### 卡舒文件




- 技术文档：[docs.cashu.space](https://docs.cashu.space)
- 公共造币厂名单：[bitcoinmints.com](https://bitcoinmints.com)
- 官方协议网站：[cashu.space](https://cashu.space)



### 社区




- Telegram Cashu 群组：[t.me/cashu_ecash](https://t.me/cashu_ecash)