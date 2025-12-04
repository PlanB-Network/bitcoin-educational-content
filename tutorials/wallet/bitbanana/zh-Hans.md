---
name: 比特香蕉
description: Lightning 节点的移动管理器
---

![cover](assets/cover.webp)



在本教程中，您将学习如何在安卓系统上安装和配置BitBanana，以便通过智能手机控制您的Lightning节点。我们将了解如何将应用程序连接到您现有的基础设施（Umbrel、RaspiBlitz、myNode或任何LND/Core Lightning节点），进行Lightning支付，远程管理您的渠道，查看您的路由收入，以及备份您的配置。您还将了解到保护节点访问的最佳安全实践，以及它与常用替代方案 Zeus 的比较。



## BitBanana 简介



BitBanana 是一款开源安卓手机应用程序，它能将智能手机变成一个完整的仪表盘，用于远程控制您的闪电节点。与在手机上嵌入本地节点的闪电钱包不同，BitBanana 采用的是 100% 远程控制理念：该应用程序不持有 satoshi，仅连接到您现有的基础设施。



该应用程序由 Michael Wünsch 在 MIT 许可下开发，保证完全透明，不收集个人数据，并可验证可重复构建。BitBanana 通过标准 URI（"lndconnect://"和 "clngrpc://"）原生支持 LND 和 Core Lightning，大大简化了初始配置。该应用程序还能识别 LndHub 和 Nostr Wallet Connect，供没有个人节点的用户使用，不过这些模式只能托管运行，功能有限。



该界面可全面访问节点的所有关键功能：发送和接收付款（BOLT11、Lightning Address、LNURL、BOLT12、Keysend）、Lightning 通道管理（打开、关闭、费用调整、再平衡）、高级硬币控制和瞭望塔管理。BitBanana 还实现了多个强大的安全层：生物识别锁定、隐身模式、紧急 PIN 码和用于匿名连接的本地 Tor 支持。



## 支持的平台和安装



### 安装



BitBanana 仅适用于 Android 8.0 或更高版本。iOS 上没有该应用程序，也没有计划推出任何版本。该项目的历史可以解释这一限制：BitBanana 是 Zap Android 的直接继承者，最初由 Michael Wünsch 开发，他决定以自己的品牌继续工作。Zap 是一个独立的应用程序家族（Zap Android、Zap iOS、Zap Desktop），由不同的贡献者以独立的代码库开发。BitBanana 目前只开发 Android 分支。



此外，iOS 生态系统对非托管 Lightning 应用程序造成了重大的监管和技术限制。2023 年，苹果公司以 "违反许可证规定 "为由拒绝了 Zeus 更新；2024 年，Phoenix Wallet 离开了美国 App Store，原因是 Lightning 服务提供商的监管存在不确定性。这些障碍解释了为什么许多 "闪电 "开发者更青睐安卓系统，因为安卓系统为非托管应用程序提供了更开放的政策。



安卓系统有三种安装方法：Google Play 商店（已安装 5000 多次，自动更新）、F-Droid（可重复构建，源代码验证）或从 GitHub 手动下载 APK。



![BitBanana](assets/fr/01.webp)



bitbanana.app 官方网站（左）标榜 "100% 自助托管，零数据收集"。中央屏幕显示三个下载选项：F-Droid（推荐）、Google Play 和 APK。右侧屏幕显示支付提醒的通知权限。



应用程序请求的权限包括：网络（节点连接）、摄像头（二维码）、NFC（LNURL）、后台服务（通知）、生物识别（安全）和 WireGuard VPN。无跟踪器，零数据收集。启用密码或生物识别锁定，确保访问安全。



## 初始配置



### 连接到 LND 节点



要将 BitBanana 连接到 LND 节点（Umbrel、RaspiBlitz、myNode），请获取包含地址、TLS 证书和验证 macaroon 的 `lndconnect` URI 或 QR 代码。



在本教程中，我们通过 umbrel 使用 LND 节点。更多详情，请参阅我们的专门教程 ：



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



在 Lightning Node 应用程序中，访问右上角的菜单并选择 "连接 wallet"。



![BitBanana](assets/fr/04.webp)



选择 **gRPC (Tor)** 通过 Tor 进行连接（推荐）。此时会显示 QR 代码和详细信息（主机 .onion、端口 10009、Macaroon）。



![BitBanana](assets/fr/02.webp)



在 BitBanana 中，按 "CONNECT NODE"（连接节点），扫描二维码或粘贴 URI。授权摄像头访问，然后在确认前检查显示的 .onion 地址。



**核心闪电**连接



如果您使用 Core Lightning (CLN) 而不是 LND，流程仍然相同，URI `clngrpc://` 包含相互 TLS 证书。Core Lightning 本机支持 BOLT12（报价），实现了 LND 所不具备的可重复使用发票和定期付款功能。



**无个人节点的连接（LNbits/托管）**



如果您没有闪电节点，BitBanana 可以通过 LndHub（BlueWallet 和 LNbits 使用的协议）或 Nostr Wallet Connect (NWC) 连接到托管服务。请注意：这些模式以托管模式运行（服务托管您的资金），功能有限。您无法管理渠道或配置路由费用，只能发送和接收闪电付款。



有关 LNbits 或 Nostr Wallet Connect 的更多详情，请参阅我们的各种教程：



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## 日常使用



### Interface 主



主屏幕显示 "闪电 "余额，左上角的菜单可进入以下部分：频道、路由、签名/验证、节点、联系人、设置、备份。时钟图标（右上角）打开交易历史记录。底部的 "发送 "和 "接收 "按钮允许您发送和接收您的卫星币。



![BitBanana](assets/fr/05.webp)



### 闪电和 on-chain 付款



![BitBanana](assets/fr/10.webp)



**发送付款：** 在主屏幕上点击 "发送 "按钮。在付款界面（左侧），您可以将地址或付款数据粘贴到 "Address 或付款数据 "字段中，右上方有一个 QR 扫描仪用于扫描代码。您还可以选择保存在 "联系人 "部分的联系人，以避免每次都要扫描。



BitBanana 可智能识别所有付款格式：经典 Lightning 发票（以 `lnbc` 开头的字符串）、Lightning Address（电子邮件格式，如 `utilisateur@domaine.com`）、用于动态支付的 LNURL-pay 代码、用于提取资金的 LNURL-withdraw，甚至是直接向 Lightning 公钥支付的 Keysend 而无需事先开具发票。应用程序会在后台自动执行必要的 LNURL 解析。



加载发票后，BitBanana 会显示全部详细信息：确切金额、预计路由费用、付款描述（如果收款人提供）和发票到期日。确认后，付款将通过您的 "闪电 "通道进行路由。然后，您可以在交易详情中逐个查看路径和实际支付的费用。



**接收付款：** 按 "接收 "按钮。选择器（右屏）可让您选择闪电（通过您的渠道即时付款）或 On-Chain。对于 "闪电 "收款，请输入所需的金额（单位为 satoshis）（或保留为 0 以创建无固定金额的发票供付款人填写），并添加可选的描述以显示在发票上。BitBanana 会立即生成带有二维码的闪电发票，以供扫描。您还可以将发票复制为文本并通过电子邮件发送。一旦收到付款，推送通知就会提醒您，交易会立即显示在历史记录中，并包含所有详细信息。



### 通道和路由



![BitBanana](assets/fr/06.webp)



通道 "部分显示您的发送/接收功能，并列出带有独特头像的通道。每个通道都显示本地和远程余额之间的流动性分配。触摸通道可查看全部详情和操作（关闭、更改路由费用）。右上方的三个点可进入 "重新平衡 "选项，重新平衡您的渠道流动性。+"按钮可打开一个新通道。



路由部分（中央屏幕）显示按时期（1D、1W、1M、3M、6M、1Y）划分的转发收入，并提供详细的转发历史记录，以优化您的策略。



签名/验证（右屏）允许您对信息进行加密签名/验证，以证明节点控制。



### 多节点和参数



![BitBanana](assets/fr/07.webp)



**管理节点（Manage Nodes）**：列出您的节点，并带有手动添加、扫描 QR 或在节点间切换的按钮。特别是，您可以为同一节点设置不同类型的连接：局域网、VPN 或 Tor。



**管理联系人**：存储您的 "闪电 "联系人，以便快速付款。



**设置**：自定义货币、语言和头像。安全与隐私部分：应用程序锁定（PIN/生物识别）、隐藏余额（隐身模式）、Tor（IP 匿名化）。配置价格计算器、区块探索器、自定义费用估算器。



## 优势和局限性



**亮点：**




- 全面移动性：随时随地控制您的 "闪电 "节点
- 全功能：支付（LNURL、Lightning Address、BOLT 12）、通道管理、硬币控制、瞭望塔、多节点
- 安全性PIN 码/生物识别、隐身模式、紧急 PIN 码、本地 Tor、屏幕截图拦截
- 免费、开源（MIT）、零佣金、零数据收集



**限制：**




- 需要一个激活的 Lightning 节点（或托管模式下的 LNbits）
- 未计划推出 iOS 版本
- 确保手机访问权限至关重要（马卡龙管理员 = 节点的全部访问权限）



## 最佳做法



**安全：**




- 激活密码/生物识别锁（防止未经授权访问节点）
- 设置紧急 PIN 码（在胁迫情况下删除敏感数据）
- 切勿共享您的登录 URI 或 macaroon
- 敌对环境下的隐身模式



**登录：**




- VPN 网状结构（Tailscale、ZeroTier）：速度和安全性之间的最佳折中方案
- Tor：最大保密性，较高延迟
- Clearnet：除非必要，避免使用（IP 暴露、开放端口）



### 备份和恢复



最后是 "备份 "菜单，通过它可以保存配置，以便进行电话迁移或重新安装。



![BitBanana](assets/fr/08.webp)



**重要：** 备份不包含 seed 或通道备份（在节点上完成）。它包含：节点配置（地址、证书、宏）、标签、联系人和参数。恢复按钮允许您导入现有备份。保存前需要确认。



![BitBanana](assets/fr/09.webp)



输入加密密码（右侧屏幕）。系统会打开文件选择器（左侧屏幕）以保存 `BitBananaBackup_2025-XX-XX.dat`。确认 "已创建备份"。



**安全性：** 加密存储备份（个人云、USB、NAS）。切勿共享文件或密码。定期测试恢复。备份恢复的是连接，而不是资金。



## BitBanana vs Zeus：有什么区别？



如果您正在探索管理闪电节点的移动应用程序，您很可能会遇到 Zeus，它是 BitBanana 的热门替代产品。BitBanana 只关注对现有节点的远程控制，而 Zeus 则不同，它采用了一种更全面的方法，提供两种操作模式：直接嵌入应用程序的 Lightning 节点（集成 LND 的嵌入模式）和与 BitBanana 类似的远程连接外部节点。



这种双重功能使 Zeus 对希望在没有任何基础架构的情况下尝试使用 Lightning 的初学者特别有吸引力。嵌入式模式可以立即启动一个完整的移动节点，而高级用户则可以在配置好个人节点后切换到远程连接。Zeus 还支持用于远程连接的 LND 和 Core Lightning，如 BitBanana。



Zeus 的另一大优势是其跨平台可用性（iOS 和安卓），而 BitBanana 仍然只基于安卓。Zeus 还整合了奥林巴斯 LSP 基础设施，以促进通过即时渠道接收闪电支付、面向商家的销售点系统以及管理流动性的集成交换功能。



不过，BitBanana 仍保留了其特有的优势：更简洁、更精简的界面，更佳的用户体验（UX），这要归功于其专注于远程控制，以及带有上下文解释的教育方法。Zeus 提供了更多功能，但代价是界面更加复杂。该应用程序仍然特别适合希望远距离控制节点而不需要监护功能的用户。



要了解有关 Zeus 的更多信息，请参阅以下教程：



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## 结论



BitBanana 可将您的安卓智能手机变成一个完整的闪电仪表盘，为节点运营商提供前所未有的移动性。该应用程序涵盖所有功能：支付（所有格式）、渠道管理、硬币控制、瞭望塔、多节点，并增强了安全性（PIN/生物识别、Tor、紧急 PIN）。



BitBanana 拥有完全的主权，不会收集任何数据，也不会损害您资金的保密性和控制权。开放源代码（MIT）保证了透明度。



## 资源



### 正式文件




- [BitBanana网站](https://bitbanana.app)
- [完整文档](https://docs.bitbanana.app)
- [GitHub源代码](https://github.com/michaelWuensch/BitBanana)



### 安装




- [Google Play 商店](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)