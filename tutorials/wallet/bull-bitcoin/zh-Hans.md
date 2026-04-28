---
name: Bull Bitcoin Wallet
description: 了解如何使用 Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*BTC Sessions 的本视频教程将指导您设置和使用 Bull Bitcoin Wallet!


本指南将带您了解 Bull Bitcoin Wallet 的安装、配置和使用。您将学会在 Bitcoin On-Chain、Liquid 和 Lightning 网络上发送和接收资金，以及如何在它们之间移动 Bitcoin。wallet 的广泛功能使其成为管理 Bitcoin 的强大的一体化工具。让我们开始吧。


## 导言


Bull Bitcoin Wallet由[Bull Bitcoin](https://www.bullbitcoin.com/)开发，是一种**自我保管**的Bitcoin wallet，这意味着您可以完全控制自己的私钥，从而完全控制自己的资金，而无需依赖第三方。这款 Wallet 是开源的，以 Cypherpunk 为理念，集简单性、保密性和跨网络交换及 PayJoin 支持等高级功能于一身。它可以让你在三个网络上管理你的比特币： **Bitcoin onchain**、**Liquid** 和 **Lightning**，每个网络都是为特定用途定制的。在[BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)上，您可以查看当前主题和即将进行的开发。由于该项目是 100% 的开源和 "公开构建"，您也可以发送您的建议和遇到的任何错误。虽然现在有些钱包支持多个网络，但 Bull Bitcoin Wallet 通过深度整合所有网络的隐私功能而脱颖而出，成为在所有主要网络中管理 Bitcoin 的强大工具。


## 1️⃣ 先决条件


在开始使用 **Bull Bitcoin Wallet** 之前，请确保您已准备好以下物品：



- 兼容智能手机**：iOS**（iPhone 或 iPad）或安卓**设备
- 互联网连接
- 安全备份介质**：在纸张或金属上写下你的**恢复短语**（12 个字），并将其存放在安全的地方。
- 基础知识**：对 Bitcoin 概念（地址、交易、费用）有起码的了解是有用的，不过本教程会为初学者解释每个步骤。


## 2️⃣安装


您可以通过以下方式安装应用程序：



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(适用于 iOS 设备)
- [Google Play 商店](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) （适用于安卓设备）


安卓用户也有其他选择：



- 直接从 [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) 页面下载 APK 或
- 通过兼容 Nostr 的 [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap) 安装


安装应用程序后，请在欢迎屏幕上配置您的账户。


## 3️⃣ 初始配置


打开时，系统会提示您以下选项：



- 创建新的 Wallet
- 回收 Wallet 和
- 高级选项


首先点击 "高级选项"。


在这里，我们可以在创建或恢复 wallet 之前配置高级设置：


1.启用 "Tor 代理"，通过 Tor 网络路由流量。

1.[Orbot应用程序](https://orbot.app/en/) 需要安装并运行后才能启用

2.Tor 代理仅适用于 Bitcoin（不适用于 Liquid），可能会导致连接速度变慢。

2.设置 "自定义 Electrum Server"，或

3.调整 "恢复公牛 "设置。稍后我们将进一步了解 [Recover Bull](https://recoverbull.com/)。


完成所有可选调整后，点击 "完成"。如果您想重新使用现有的 Wallet，请点击 "恢复 Wallet "并填写恢复短语的 12 个单词。


否则，点击 "创建新的 Wallet"。


![image](assets/en/01.webp)


## 4️⃣主屏幕


在深入了解之前，让我们先看看 "主屏幕"，了解一下方向：



- 交易概览 "和 "设置菜单 "位于顶部。
- 可用余额 "有一个隐私选项，可以 "打开或关闭"。
- 访问 "Bitcoin Bull Exchange "进行 "购买、出售或支付"（这取决于司法管辖区，可能需要 KYC）。
- 在钱包之间 "转移 "资金
- `Secure Bitcoin` 等同于 Onchain Bitcoin Wallet
- 通过 Lightning- / Liquid Network 进行 "即时支付" *（注：Bull Bitcoin Wallet 可通过 Lightning 进行付款和收款。由于通过[*Boltz exchange](https://boltz.exchange/)自动交换，通过Lightning收到的资金将存储在[*Liquid network](https://liquid.net/)（Wallet Instant Payments中）。这样，您就可以与 Lightning 进行互动，而无需管理流动性渠道，同时保持自我保管。）
- 发送 "和 "接收 "资金


![image](assets/en/02.webp)


首先，让我们进行一些重要配置，并从 "备份 "开始。


## 5️⃣备份


要开始备份过程，请点击应用程序右上角的 "齿轮图标 (⚙)"，然后选择 "Wallet 备份"。您将看到两种保护 wallet 安全的方法："加密保险库 "和 "物理备份"。让我们一一探讨。


![image](assets/en/03.webp)


### 物理备份


点击 "物理备份"，查看代表您的恢复或 seed 短语的 12 个单词列表。请考虑以下内容：



- 以最谨慎的态度写下你的 "恢复短语"。写在纸上或金属上，并将其保存在安全的地方（保险箱、离线位置）。该短语是您在丢失设备或删除应用程序时访问比特币的唯一途径。
- 还需要注意的是，任何人都可以用这句话盗取你所有的比特币。千万不要以数字方式存储：
- 无截图
- 没有云、电子邮件或信息备份
- 无复制/粘贴功能（保存到剪贴板的风险）


![image](assets/en/25.webp)


下一个屏幕会让你按照正确的顺序排列单词，以确保你的 seed 短语正确无误。测试成功后，您会收到确认信息。


! **这一点至关重要**。如需进一步帮助 ：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 加密保险库


还可以选择在云中进行加密、匿名备份。但我们在上一段中不是说过，云备份有风险，应该避免吗？不过，Bull Bitcoin 团队开发了一种巧妙的方法来确保备份过程的安全性。具体操作如下


Recoverbull "是一种备份协议，它通过将备份分成两部分来简化 Bitcoin wallet 的安全保护。首先，您的 wallet 备份文件会使用一个强大的加密密钥在您的设备上加密。您可以将加密文件保存到任何地方，如 Google Drive 或您的设备。其次，解锁文件所需的加密密钥存储在密钥服务器中。要恢复 wallet，您需要加密备份文件和密钥，您可以使用 PIN 或密码访问密钥。这种设计确保了在没有特定备份文件的情况下，仅有云备份是无用的，仅有密钥服务器也是无用的。这样，即使其中一部分遭到破坏，也能确保您的资金安全。


把它想象成一个保险箱。加密备份文件就是*保险箱*，您可以将其存储在任何地方（如 Google Drive）。您的恢复密码就是*密钥*，由恢复牛密钥服务器单独存储。小偷需要同时获得您的特定盒子和特定密钥才能打开盒子。这样的设计可以确保即使有人拿到了您的备份文件，如果没有服务器上的密钥，它也是无用的，而服务器上的密钥如果没有您独一无二的备份文件，也是无用的。


了解有关 `Recoverbull` wallet 备份协议的更多信息 [此处](https://recoverbull.com/)。


点击 "加密保险库"，然后点击 "继续 "确认使用默认服务器。连接将通过 "Tor "网络进行，以确保隐私和匿名性。


**了解您的密码**



- 应用程序解锁密码 "***：** 在 "设置 > 安全密码 "中设置的可选密码，用于锁定手机上的应用程序。
- 恢复密码 "***：** 在 "加密保险库 "备份过程中创建的强制密码，用于在恢复过程中解密备份文件。


这是两个不同的 PIN 码。不要忘记您的恢复密码，因为它对恢复 wallet 至关重要。


**恢复密码设置：**



- 您必须创建一个 PIN 或密码才能恢复对 wallet 的访问。
- 个人识别码/密码必须至少为 6 位数（例如，避免使用 123456 这样的简单序列，因为这种密码不被接受）。
- 没有这个 PIN 码，wallet 就无法恢复。


然后，选择保险库提供商：



- 谷歌驱动器 "或
- 自定义位置"（例如您的设备）


![image](assets/en/04.webp)


现在，保存 "备份文件"。接下来，点击 "测试恢复"，选择已保存的备份文件或保险库，然后点击 "解密保险库"。输入你的 "PIN "或 "密码"。如果一切正常，就会出现 "测试成功完成 "屏幕。


### 进口/出口标签


现在我们创建了备份，让我们来看看 "标签"。  Bull Bitcoin wallet 允许用户为其收款地址和交易创建自定义标签，从而增强了私密性和组织性。这些标签可帮助您对资金进行分类，因为发送到贴有标签的地址的交易将继承该标签，您还可以为出站交易贴标签，以跟踪其变化。wallet 完全支持 [BIP-329](https://bip329.org/)标准，这意味着您可以将所有标签导出到文件中，然后导入到另一个 wallet 中。这一功能确保您可以无缝备份交易历史和分类，或在不同的 wallet 实例之间迁移，而不会丢失您的个性化组织。


![image](assets/en/05.webp)


## 6️⃣设置


在确保主要备份安全后，让我们来探索设置中的其他功能。


### A - 确保准入


要保护应用程序的安全，请导航至 "设置"，然后选择 "安全 PIN 码 "以选择 PIN 码。创建一个强大的 PIN 码来锁定对 wallet 的访问。虽然此步骤是可选的，但我们强烈建议您这样做，以防止他人在未经授权的情况下使用您的手机。


![image](assets/en/06.webp)


### B - 连接个人节点（可选）


Wallet BullBitcoin 默认连接到 Electrum 服务器：第一个服务器由 Bull Bitcoin 管理，第二个服务器来自 Blockstream，这两个服务器都被认为不会保留日志，从而降低了跟踪风险。


为了提高保密性，您可以通过 Electrum 服务器将应用程序连接到自己的 Bitcoin 节点。为此，请点击 "设置">"Bitcoin 设置">"Electrum Server 设置"，然后点击 "+ 添加自定义服务器 "以输入服务器地址和凭证。


![image](assets/en/07.webp)


### C - 货币


可用余额以 `sats` 和 `USD` 两种货币显示在主屏幕上。要更改，请导航至 "设置">"货币"。在这里，您可以在`sats/BTC`之间切换，并选择您的`默认法定货币`。


![image](assets/en/08.webp)


### D - Bitcoin 设置


Bitcoin 设置 "菜单可深入访问 wallet 的核心配置和数据。在这里，您可以查看 "安全 Bitcoin "和 "即时支付钱包 "的基本详情，从而实现完全透明的控制。该菜单的主要功能包括



- Wallet 详情：** 导航至您的安全 Bitcoin 或即时支付 wallet，查看具体信息。
- Wallet 指纹：** wallet 的唯一标识符。
- 公钥 (Pubkey)：** 用于 generate 的 Bitcoin 接收地址的密钥。
- Descriptor：** wallet 结构的技术摘要。
- 派生路径：** 用于从主私钥 generate 所有地址的特定路径。
- Address 查看：** 访问未使用的接收地址列表并更改地址（即将推出）


此外，您还可以选择



- 启用自动转账 "设置可设置 wallet 即时余额上限，该上限将自动转账至安全的比特币 wallet。
- 通过 "Mnemonic "短语导入通用钱包或导入 "watch-only"（仅限手表）。
- 连接 "硬件钱包"：目前支持的设备有 ColdcardQ、SeedSigner、Specter、Krux、Blockstream Jade 和 Foundation Passport。


## 7️⃣ Bull Bitcoin Exchange


您可以直接从 wallet 访问 [Bull Bitcoin 交易所](https://www.bullbitcoin.com/)，无需离开应用程序即可购买、出售和支付 Bitcoin。这一集成为您管理 Bitcoin 需求提供了便捷的解决方案。请注意，根据您所在的司法管辖区，访问交易所及其服务可能会受到限制，可能需要完成 "了解您的客户"（KYC）验证，以符合监管标准并使用平台的全部功能。


要开始使用，请点击右下角的 "Exchange"，然后 "注册 "或 "登录 "到您的账户。


交易所提供以下[功能](https://www.bullbitcoin.com/)：



- 用您的银行账户购买 Bitcoin 并进行自我保管
- 非监护
- 个人或公司
- 即时提款
- 无隐藏费用
- 可提供 Lightning Network
- 无交易限制
- 重复购买选项


![image](assets/en/09.webp)


要了解更多信息，请访问本教程：


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣接收资金


使用**Bull Bitcoin Wallet**接收资金既简单又灵活，可支持针对不同使用情况定制的三种不同网络：



- 用于安全、长期存储的 "Bitcoin（onchain）"网络。
- Liquid "网络可实现更快、更保密的交易。
- 即时、低成本支付的 "闪电 "网络。


应用程序会根据您选择的网络自动生成相应的地址或发票。以下是每个网络的操作步骤。


### 通过 Onchain（Bitcoin 网络）接收


要接收 on-chain 资金，您可以从主屏幕选择 "安全 Bitcoin Wallet"，然后点击 "接收"，或者点击 "接收 "主按钮，然后选择 "Bitcoin 网络"。


生成接收地址有两种主要模式：


**默认模式（带附加输入参数的 URI）


默认情况下，wallet 会生成一个 [BIP21 URI]（https://bips.dev/21/）。这是一种标准化格式，其中包含比简单地址更多的信息，包括金额、个人备注和 PayJoin 参数，以提高私密性。这个全面的 URI 被编码成一个 QR 码，可供复制。格式如下bitcoin:<地址>?<参数1>=<value1>&<参数2>=<value2>`。



- 其他输入参数：**
    - 金额：** 以 BTC、sats 或法定货币指定请求的金额。
    - 信息：** 添加发件人可见的个人备注。
    - PayJoin:** 启用此选项可将交易中发送方和接收方的输入合并，从而提高私密性。


URI 示例：


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*重要提示：请不要向本教程中的地址发送任何资金，wallet 将被删除。


![image](assets/en/10.webp)


**只启用复制或扫描 Address 选项


启用 "仅复制或扫描 Address 选项 "后，应用程序将以 SegWit (bech32) 格式生成简单的 Bitcoin 地址。


例如


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


即使您输入了金额或备注，它们也不会包含在二维码或复制的地址中。


![image](assets/en/11.webp)


### 通过 Liquid Network 接收


您可以在 Liquid Network 上接收付款。进入 "接收 "屏幕后，您有两个相同的选项来生成付款请求：


**1.简单 Address：** 复制标准 "Liquid 地址"。这是您的 wallet 在 Liquid 网络上的唯一标识符，不包括任何特定数量或信息。


示例 Address：


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2.详细付款请求（URI）：** 对于更有条理的请求，您可以指定金额和个人备注。这些信息会自动编码成可共享的 URI 和相应的 QR 代码。



- 金额：** 您可以用 Bitcoin (BTC)、Satoshis (Sats) 或法定货币设置金额。
- 注：** 添加个人信息，以识别交易。


**URI 示例：**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


要完成交易，请向发件人提供 "地址 "或 "URI"。您可以将其复制到剪贴板，或让他们直接扫描屏幕上的二维码。


![image](assets/en/12.webp)


### 通过闪电接收



Bull Bitcoin Wallet 还允许您通过 Lightning Network 发送和接收付款。其主要特点是，通过 "闪电 "收到的资金会自动交换并存储在 "即时支付 "Wallet 的 "Liquid Network "上。这项服务由`Boltz`提供支持。这种设计使您能够享受 Lightning 的速度和低成本，而无需管理流动性渠道的复杂性，同时保持资金的完全自我保管。虽然这种混合方法是自我托管的，避免了管理渠道的复杂性，但它引入了第三方服务（Boltz）、小额掉期费，并依赖Liquid Network的职能部门联合会作为关键持有人，这与传统的、非托管的闪电wallet不同，后者由您管理自己的渠道。有关 Liquid 及其管理模式的更多信息，请点击此处：


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- 限制：**
    - 最低金额：** 需要最低发票金额。请在应用程序中查看当前限额
    - 费用：** 收款人需支付小额交换费。该费用从发送方转账金额中扣除，可能会有变动。
- 福利：**
    - 自我监护：** 您的资金始终由您控制，并通过 Liquid 网络安全保管。
    - 避免高昂的 On-Chain 费用：** 通过使用 Lightning 并在 Liquid 上存储，您可以绕过与开设传统 Lightning 通道相关的 on-chain 费用。您可以选择稍后将资金转移到 on-chain 通道，如果累积金额足以支付这笔费用的话。
    - 小贴士：** 两个 Bull Bitcoin 用户之间要进行最经济有效的交易，请直接使用**Liquid 网络**，以完全避免闪电交换费用。


要收到付款，您必须提供 generate "闪电发票"：


1.输入金额 "***:** 指定您希望以 Bitcoin (BTC)、Satoshis (Sats) 或法定货币接收的金额。

2.添加备注 "**（可选）：** 包括备忘录或备注。这将嵌入发票中，并在付款完成后显示在您的交易历史记录中，以便于识别。

3.Invoice有效期`**:**"闪电 "发票具有时效性，将在**12小时**后失效。如果在此期间未付款，发票将失效，您需要重新开具新发票。


通过将发票复制到剪贴板或让对方扫描屏幕上显示的二维码，向发件人提供发票。


![image](assets/en/13.webp)


## 9️⃣寄送资金


您可以直接从主页或任何钱包访问发送屏幕。Bull Bitcoin Wallet 可根据您输入的地址或发票（无论是粘贴的还是通过二维码扫描的）自动检测目的地网络--"Bitcoin"、"Liquid "或 "Lightning"，从而简化发送过程。


### 通过 Bitcoin 网络进行 On-Chain 传输


通过 on-chain 发送资金意味着您的交易将直接记录在 Bitcoin 区块链上。这种方法最适合大额转账或无时间限制的转账。首先，您可以点击右下方的 "发送按钮"，然后扫描或输入一个 "标准 Bitcoin 地址"。


如果您提供的地址不包括具体金额，系统会提示您在发送屏幕上填写详细信息。您可以用自己喜欢的单位指定金额，如 BTC、Satoshis 或等值的法币。您还可以选择添加个人备注，这是供您自己参考的私人备忘录，有助于您日后识别交易。该备注不会与收件人共享。


相反，如果您扫描或粘贴的付款请求已包含所有必要的详细信息，如带有预定义金额的 BIP21 URI，wallet 将绕过数据输入屏幕，直接进入确认屏幕授权付款。


![image](assets/en/14.webp)


在播放交易之前，您将看到一个确认屏幕。请务必花点时间仔细查看每项参数，密切关注收件人地址、发送金额和网络费用。该屏幕还提供了定制交易的强大工具。


您可以通过两种主要方式控制费用。第一种方法是选择所需的交易速度，如低、中或高，wallet 会自动为您计算适当的费用。第二种方法可以更精确地控制费用，您可以设置具体的费用，可以是以卫星为单位的绝对总额，也可以是每字节的相对费率，然后提供预计的确认时间。


对于高级用户，wallet 提供多种设置来微调交易。按费用替换"（RBF）默认为启用，这是一项很有价值的功能，如果交易被卡在内存池中，可以用更高的费用重新广播，从而加快交易速度。您还可以手动选择从哪些 "未支出交易输出"（UTXOs）中支出。这是 UTXO 整合的强大工具，是一种将多个小输入合并为一个大输入的策略。虽然这可能会增加当前交易的费用，但却可以大大降低未来交易的费用，尤其是在网络费用预计会上涨的情况下。


![image](assets/en/15.webp)


当您扫描收件人包含 `pj=` 参数的付款请求（BIP21 URI）时，会自动尝试 PayJoin。如果只是粘贴一个没有额外参数的普通地址，则不会激活此功能。这种协作方法结合了发送方和接收方的输入，打破了共同输入所有权启发式，从而提高了隐私性，在某些情况下还能更好地扩展和节省费用。


### 发送至 Liquid Network


Liquid Network "专为快速、保密交易而设计，费用极低。当您通过 Liquid 发送资金时，这些资金将从您的 "即时支付 Wallet "中提取。过程非常简单：您只需输入或扫描收件人的`Liquid 地址`。


如果地址没有指定金额，发送页面会要求您提供一个金额。您可以输入 BTC、Satoshis 或法币金额。Liquid 的一个主要优势是最低门槛低。与 on-chain 交易一样，您可以为自己的记录添加可选的个人备注。如果支付请求已包含金额，wallet 将直接进入确认界面。


在 Liquid 交易确认屏幕上，您将查看详细信息。费用很低，根据交易的复杂程度计算。费用通常约为 0.1 Sat/vB，简单交易的费用仅为 20-40 Satoshis（例如，截至 2025 年 12 月 21 日为 26 Satoshis）。


![image](assets/en/16.webp)


### 发送至 Lightning Network


您可以扫描闪电 Address（如 "runningbitcoin@rizful.com"），设置金额和收件人备注，也可以扫描预设金额的发票，直接进入确认屏幕。


*请注意，最低金额和费用适用。


Bull Bitcoin Wallet通过从 "即时支付Wallet"（在Liquid上）提取资金并通过 "Boltz "进行交换来发送闪电付款。这种混合方法是完全自我保管的，避免了管理专用闪电通道所需的高额 on-chain 费用，但需要支付 "交换费"。如果收件人也使用Bull Bitcoin wallet，则直接发送到收件人的Liquid地址，成本最低。


## 在钱包之间转移资金


Bull Bitcoin 允许您在 Liquid Network 上的 "安全 Bitcoin" wallet 和 "即时支付 Wallet "之间转移 Bitcoin，或转移到 "外部 Wallet"。要执行转账，只需导航到 "转账 "部分，选择源钱包和目标钱包，输入要转账的金额，然后确认交易即可。


![image](assets/en/17.webp)


## 1️⃣ 1️⃣恢复您的 Bull Bitcoin Wallet


本节介绍了在丢失设备、卸载应用程序或需要更换新设备的情况下，如何重新获取 Bull Bitcoin Wallet 资金。如前所述，有两种主要的恢复方法：使用独特的 "Recoverbull "方法和使用标准的 "BIP39 seed 短语"。


### 方法 1：恢复公牛


回顾：Wallet 备份在本地加密。加密文件可以存储在云存储或其他设备上。加密密钥由密钥服务器存储。两者分开保存，必须结合起来才能恢复 wallet。


首先，我将删除 Wallet 及其上的所有资金，然后重新安装 wallet。我们将再次进入 "欢迎屏幕"。这次，选择 "恢复 Wallet "选项。然后，导航到 "加密保险库 "方法，确认使用 "默认密钥服务器"，并选择存储备份文件的位置或 "保险库提供商"。


![image](assets/en/18.webp)


它会显示保险库已成功导入。点击 "解密保险库 "按钮并输入 "PIN"。下一个屏幕将显示您的 "余额 "和已恢复的 "交易数"。


![image](assets/en/19.webp)


### 方法 2：种子短语


此方法使用 wallet 的主恢复短语，这是一个标准的 12 个单词列表，是您资金的最终备份。这是恢复 Bitcoin wallet 的最通用方法，因为它与任何特定服务或服务器无关。只要拥有这个短语，您就可以在任何兼容设备上恢复 wallet，即使无法访问 Bull Bitcoin 密钥服务器也没问题。


从 "欢迎 "屏幕选择 "恢复 Wallet"。这次选择 "物理备份 "方法。应用程序将显示一个单词网格。按照正确的顺序仔细选择 12 个 seed 短语中的每个单词。要一丝不苟，因为任何一个错误都会导致 wallet 的错误。


## 1️⃣ 2️⃣连接 Hardware Wallet


为了获得最高级别的安全性，许多 Bitcoin 用户选择将资金存储在 "冷存储 "中。这意味着将控制 Bitcoin 的 "私钥 "保存在一个永远不会连接到互联网的设备上。硬件 wallet（或签名设备）是专门为此设计的物理设备。它就像密钥的数字保险库，确保密钥永远不会受到在线计算机或智能手机的潜在威胁。


通过将硬件 wallet 连接到 Bull Bitcoin 应用程序，您可以获得两个世界的最佳体验：冷存储为您的私人密钥提供了无懈可击的安全性，而 Bull Bitcoin wallet 则具有强大的功能和用户友好界面，可用于查看余额和管理交易。在最后一章中，我们将向您介绍如何将硬件 wallet 连接到 Bull Bitcoin wallet，例如 [Coldcard Q](https://coldcard.com/q)。本教程不会深入介绍如何设置 Coldcard Q，您可以在此处了解相关信息：


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### 导入 Wallet


![image](assets/en/26.webp)


首先，从 Coldcard Q 的主菜单中选择 "Export Wallet"，然后选择 "Bull Wallet"。您的 Coldcard 将 generate 一个二维码。


![image](assets/en/20.webp)


打开 Bull Bitcoin Wallet，导航至 "设置">"Bitcoin 设置">"导入 wallet"，然后选择手机上的 "Coldcard Q"，点击 "打开相机 "扫描此二维码以导入硬件 wallet 的公钥。


![image](assets/en/21.webp)


### 使用冷卡 Q 接收


使用已连接的 Coldcard Q 接收 Bitcoin 时，无需将设备与手机进行物理连接。Bull Bitcoin Wallet 已经导入了必要的公钥，可以自行接收 generate 地址。


1.点击已导入的 Coldcard Q 签名设备并选择 "接收"。

2.应用程序将自动从 Coldcard 的 wallet 显示一个新的 Bitcoin 地址。

3.使用此地址接收资金。Bitcoin 将直接与硬件 wallet 的密钥相连，即使在此过程中设备处于离线状态。


![image](assets/en/22.webp)


### 使用冷卡 Q 发送


使用 Coldcard Q 发送 Bitcoin 需要您的实物确认，以授权任何交易。虽然公牛 Wallet 应用程序可用于建立交易，但最终签名只能在硬件 wallet 本身上创建。


首先，打开 wallet 的 "Coldcard Q"，点击 "发送"。然后，"打开相机 "扫描接收地址的二维码。扫描后，输入您要发送的 "金额"，并根据需要调整 "费用优先级"。


如需更多选项，请查看 "高级设置"。这里有 "按费用替换"（RBF）选项，默认情况下已激活，可让您稍后加快卡住的交易。您还可以使用 "Coin Control "选项，该选项允许您手动选择要使用的特定UTXO。


查看所有详细信息后，点击 "显示 PSBT "准备交易。


![image](assets/en/23.webp)


点击 Coldcard Q 上的 "扫描 "按钮，使用摄像头扫描手机上显示的二维码。然后，Coldcard 屏幕会显示所有交易详情。仔细核实金额、收件人地址和您的更改地址。如果一切无误，请按 Coldcard Q 上的 "Enter "按钮签署交易。接下来，屏幕上会出现已签名交易的二维码。


![image](assets/en/24.webp)


在 Bull wallet 上，点击 "我完成了"，然后点击 "相机 "按钮，从您的 Coldcard Q 扫描 "已签署交易 "的二维码。最后查看一次，然后点击 "广播交易"。将交易发送到 Bitcoin 网络后，您的资金就可以到账了。


## 🎯 结论


您现在已经完成了 Bull Bitcoin Wallet 的使用之旅。该应用程序将强大的隐私和安全工具置于您的指尖，使高级功能简单易用。它通过 "PayJoin"（隐藏您在区块链上的交易）和 "Tor integration"（掩盖您的网络活动，防止被窥探）等功能帮助您保持隐私。对于希望获得终极控制的用户，您可以连接到自己的 "个人 Bitcoin 节点"，不再依赖第三方服务器，还可以使用 "硬件 wallet "来完全离线、安全地保存您的私钥。Bull Bitcoin Wallet 拥有智能备份选项和对 Bitcoin、Liquid 和 Lightning 的无缝支持，对于那些认真保护资金隐私、安全并完全由自己控制的人来说，Bull Bitcoin Wallet 是一个强大的一体化选择。


## 公牛 Wallet 资源


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)