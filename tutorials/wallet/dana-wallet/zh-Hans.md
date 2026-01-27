---
name: Dana Wallet
description: 无声支付的极简组合 (BIP-352)
---

![cover](assets/cover.webp)



重复使用 Bitcoin 地址是对用户保密性最直接的威胁之一。当收款人共享一个地址接收多笔付款时，任何观察者都可以追踪所有相关交易并重建他们的财务历史。这个问题对内容创作者、慈善机构或活动家的影响尤为严重，因为他们希望在不泄露自己或捐赠者隐私的情况下公开显示捐赠地址。



德纳 Wallet 为解决这一问题提供了优雅的解决方案：静默支付。这种极简的开源 wallet 于 2024 年推出，可生成一个可重复使用的静态地址，同时保证收到的每笔付款最终都会出现在区块链上的一个单独地址上。发件人无需事先与收件人互动，外部观察者也无法将单个交易联系在一起。在区块链上，这些支付看起来就像完全普通的 Taproot 交易。



Dana Wallet 可在 Mainnet 和 Signet 上使用，但开发人员仍然认为它是试验性的，并建议不要存入不准备损失的资金。在本教程中，我们将使用 Signet 版本来探索 "无声支付"，而无需冒任何实际资金的风险。



## 什么是德纳 Wallet？



### 理念和目标



Dana Wallet 采用 "SP 优先 "方法：wallet 只生成静默支付地址，并只接受这种类型的支付。您无法使用此应用程序创建经典的 Bitcoin 地址（传统、SegWit 或 Taproot 标准）。这种刻意的限制可以让您集中精力学习 BIP-352 协议，而不受其他功能的干扰。简洁的界面特意强调易用性，而不是繁多的选项，即使对 on-chain 保密概念一无所知的用户也能轻松使用该工具。



该项目完全开源，使用 Flutter 开发移动界面，使用 Rust 开发内部加密逻辑。这种架构将流畅的用户体验与密集扫描操作的最佳性能相结合。



### 静默支付如何运作？



静默支付（BIP-352）基于使用椭圆曲线 Diffie-Hellman 密钥 Exchange (ECDH) 的复杂加密机制。收款人生成一个静态地址（在 mainnet 上以 "sp1... "开头，在 Signet 上以 "tsp1... "开头），该地址由两个不同的公开密钥组成：一个扫描密钥（$B_{scan}$）用于检测收到的付款，另一个支出密钥（$B_{spend}$）用于支出收到的资金。通过这种分离，可以在 wallet 硬件上保留支出密钥，而在连接的设备上使用扫描密钥。



当发件人希望付款时，他的 wallet 将其输入的私人密钥与收件人的公共扫描密钥相结合，计算出一个共享的 ECDH 密钥。这个秘密会产生一个加密 "调整"，与收款人的消费密钥相加，就能为该交易创建一个唯一的 Taproot 地址。



收款人可以使用他的私人扫描密钥和交易中可见的公开密钥（Diffie-Hellman 数学特性）复制这一计算。这样，他就能在不与发件人进行任何事先交互的情况下检测并花费这笔资金。



这种方法有几个优点：




- 收款人保密**：每笔付款的最终收款地址不同
- 发件人保密**：没有连接付款的持久标识符
- 无第三方服务器**：协议自主运行
- 无差别交易**：静默支付看起来就像普通的 Taproot 交易



其主要缺点是扫描成本高：收件人必须分析每一笔新的 Taproot 交易，才能检测出是为他准备的交易。



如果您想了解更多有关静默支付技术操作的信息，我们向您推荐有关 Bitcoin 保密性的 BTC204 课程，其中有一章专门介绍静默支付：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 支持的平台



Dana Wallet 是一款安卓应用程序。APK 可通过开发人员提供的 F-Droid 专用仓库、Obtainium 或直接从 GitHub 下载。对于 Linux 用户，在技术上可以编译 Flutter 应用程序到桌面。



该应用程序未在 iOS 或官方商店（Google Play、App Store）上提供，这反映了它的试验性地位和对技术受众的关注。



## 安装



### 必要的先决条件



要在 Android 上安装 Dana Wallet，您需要在安全设置中启用 "未知来源 "选项的 Android 设备。无需账户或注册。



### 增加 F-Cold 押金



推荐的方法是添加 Dana Wallet 的专用 F-Droid 资源库。请访问 `fdroid.silentpayments.dev`，在那里您可以找到软件源链接和二维码扫描。该资源库目前提供 3 个应用程序：Mainnet 版本、Development 和 Signet。



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### 通过 F-Droid 安装



打开安卓设备上的 F-Droid 应用程序，然后通过右下角的图标进入 "设置"。选择 "资源库 "管理应用程序源。按 "+"按钮添加新资源库，然后扫描二维码或粘贴 "https://fdroid.silentpayments.dev/fdroid/repo "链接。添加版本库后，您将看到 Dana Wallet 的三个可用版本。选择 "Dana Wallet - Bookmark"，然后按 "安装"。



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## 初始配置



### 创建投资组合



首次启动时，Dana Wallet 会显示一个欢迎屏幕，介绍其使命："无中间商收发捐赠"。按 "开始 "继续。下一个屏幕将介绍该应用程序的三大优势：




- 轻松捐款**：几秒钟内即可开始接收捐款
- 默认隐私**：无需服务器或复杂的基础设施
- 类似电子邮件的体验**：收发比特币就像收发电子邮件一样简单



您可以选择 "还原 "来还原现有的投资组合，或选择 "创建新的 wallet "来创建新的投资组合。按 "创建新的 wallet"。



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



然后，应用程序会生成一个恢复短语，您应将其仔细记在物理介质上。即使是没有实际价值的测试资金，也要采用良好的备份方法。



### Interface 和参数



创建投资组合后，您将进入主界面，分为两个选项卡："交易 "和 "设置"。



交易**"选项卡显示你的比特币余额（及其兑换成美元的情况）、最近交易列表和两个操作按钮："付款 "用于发送资金，还有一个接收按钮（下载图标）。



设置**选项卡提供四个选项：




- 显示 seed 短语**：显示您的恢复短语，以便妥善保存
- 更改法定货币**：更改显示货币（默认为美元）
- 设置后端 URL**：配置 Blindbit 服务器 URL（见下一节）
- 擦除 wallet**：从设备上完全擦除 wallet



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit 服务器



Dana Wallet 使用名为 **Blindbit** 的索引服务器来检测您的静默支付。了解其工作原理对于评估应用程序的信任模式非常重要。



**我们为什么需要服务器？



要检测静默支付，理论上 wallet 必须扫描每个区块中的所有 Taproot 交易，并对每个交易进行加密计算（ECDH）。在手机上，这种操作的计算量和带宽消耗太大。



Blindbit 服务器通过预先计算所有 Taproot 交易的中间数据（称为 "调整"）来解决这一问题。然后，您的 wallet 将下载这些调整数据（每笔交易 33 字节），并在***本地执行最终计算，以检查付款是否属于您。



**保密**



在传统的 Electrum 服务器上，您会透露自己的地址，而 Blindbit 服务器则不同，它不知道哪些付款属于您。它向所有用户提供相同的数据，由您的手机进行最终验证。因此，相对于服务器而言，您的信息是保密的。



**默认服务器



Dana Wallet 使用公共服务器 "silentpayments.dev/blindbit/signet"（Signet）或 "silentpayments.dev/blindbit/mainnet"（Mainnet）。如果您托管自己的服务器，可以在设置中更改该 URL。



**托管您自己的 Blindbit 服务器**



对于希望拥有完全主权的用户，可以托管自己的 Blindbit Oracle 服务器。这需要.NET Framework 2.0 或更高版本的服务器：




- 一个完整的 Bitcoin 核心节点 **非插箭**（非 pruned）
- 安装 Blindbit Oracle（可在 GitHub 上获取：`setavenger/blindbit-oracle`）。
- 约 10 GB 的额外磁盘空间
- 技术技能（Go 语言编译、服务器配置）



目前还没有针对 Umbrel 或 Start9 的打包应用程序。目前，安装仍需手动操作。这是一个正在积极发展的领域，未来可能会出现更方便的解决方案。



## 日常使用



### 接收资金



要接收比特币，请在主屏幕上按接收按钮（下载图标）。Dana Wallet 会在书签上以 "tsp1q...... "格式显示您完整的静默支付地址。界面提供多个选项：




- 显示 QR 代码**：显示地址的 QR 代码，方便扫描
- 共享**：通过手机应用程序共享地址
- 复制**：将地址复制到剪贴板



如屏幕所示，您可以在社交网络上公开分享该地址，而不会泄露您的隐私。



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



要在 Signet 上获得第一笔测试资金，请使用专用的静默支付龙头，网址为 `silentpayments.de/faucet/signet`。复制你的地址 "tsp1..."，粘贴到龙头提供的字段中，然后验证请求。等待区块被挖出（在 Signet 上大约需要 10 分钟）。



### 发送付款



要发送资金，请按主屏幕上的 "付款 "按钮。此时会出现 "选择收款人 "屏幕，有三个指定收款人的选项：




- 手动输入付款信息
- 从剪贴板粘贴**：从剪贴板粘贴地址
- 扫描 QR 码**：扫描包含地址的 QR 码



收件人地址确认后，您可以在 "输入金额 "屏幕上输入要发送的金额（单位：叙利亚先令）。您的可用余额会显示出来以供参考。按 "继续选择费用 "继续。



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



下一个屏幕显示三个收费等级，具体取决于所需的紧急程度：




- 快速**（10-30 分钟）：快速确认费用较高
- 正常**（30-60 分钟）：中等费用
- 慢**（1 小时以上）：非紧急交易最低收费



选择费用等级后，"准备发送？"确认屏幕会汇总所有详细信息：目的地地址、金额、预计时间和交易费用。请仔细核对这些信息，然后按 "发送 "键发送交易。



交易发送后，会以 "未确认 "的状态出现在您的历史记录中，直到被纳入拦截。您的余额也会相应更新。



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## 优势和局限性



### 亮点





- 教学**：以学习为重点的简化界面 无声支付
- 双向**：与其他组合不同，同时支持发送和接收
- 开源**：GitHub 上完全可审计的代码
- 专用 Faucet**：更容易获得试验资金
- 无账户**：无需注册或提供个人资料



### 需要考虑的制约因素





- 实验**：未经审核的软件，在 Mainnet 上慎用
- 平台有限**：主要是安卓系统，没有 iOS 版本
- 功能缩减**：无硬币控制、无子账户、无 "闪电 "功能
- 密集扫描**：付款检测需要消耗大量资源



## 最佳做法



### seed 安全



即使是背景毫无价值的 Signet 测试，也要认真对待你的恢复短语。使用设置中的 "显示 seed 短语 "选项，认真写下它。作为一种良好做法，为 Signet 和 Mainnet 维护完全独立的钱包：永远不要在用于接收真实资金的 wallet 上使用为测试而创建的 seed。



### 关于试验状态的警告



Dana Wallet 的开发人员认为它仍处于试验阶段。他们明确表示"不要使用你不愿意损失的资金"。出于学习目的，请选择 Signet 版本。如果您使用 Mainnet 版本，请限制自己的 token 金额。



### 备份和恢复



静默支付资金恢复需要与 BIP-352 协议兼容的 wallet。标准的 wallet 无法扫描区块链来恢复 UTXO 静默支付。请保留已安装的 Dana Wallet 或在首次启动时使用 "还原 "选项恢复现有的 wallet。



## 与 BIP-47 和 PayJoin 的比较



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

无声支付消除了 BIP-47 通知交易，但扫描费用更高。PayJoin 解决的是另一个问题（输入相关性），可与静默支付结合使用。



## 结论



Dana Wallet 是在无风险环境下学习静默支付的重要教育工具。它采用简约的方式，让你了解 BIP-352 协议的基本机制，而不会被次要功能所干扰。通过对 Signet 的实验，你将对 Bitcoin 交易保密这一前景广阔的技术有一个实际的了解。



静默支付在协调易用性和尊重隐私方面迈出了重要一步。社区的热情以及与各种钱包（Cake Wallet、BitBox02、BlueWallet 用于发送）的首次集成，都预示着在未来，发布捐款地址将不会再损害其所有者的财务隐私。



## 资源



### 正式文件




- Dana Wallet GitHub 代码库：https://github.com/cygnet3/danawallet
- F-Cold 押金： https://fdroid.silentpayments.dev
- 静默支付社区网站：https://silentpayments.xyz
- 规格 BIP-352: https://bips.dev/352



### Signet 测试工具




- Faucet 无声付款： https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit 服务器（自行托管）




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle