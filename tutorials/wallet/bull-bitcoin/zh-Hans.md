---
name: Bull Bitcoin Wallet
description: 了解如何使用 Bull Bitcoin 钱包
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*以上由 BTC Sessions 制作的视频教程将指导您设置和使用 Bull Bitcoin 钱包!*


本指南将带您了解 Bull Bitcoin 钱包的安装、配置和使用。您将学会在比特币链上、Liquid 和 闪电网络上发送和接收资金，以及如何在它们之间转移比特币。钱包的广泛功能使其成为管理比特币的强大的一体化工具。让我们开始吧。


## 导言


Bull Bitcoin 钱包由 [Bull Bitcoin](https://www.bullbitcoin.com/)开发，是一种**自我保管**的比特币钱包，这意味着您可以完全控制自己的私钥，从而完全控制自己的资金，而无需依赖第三方。这款钱包是开源的，以密码朋克哲学价值为理念，集简单性、保密性和跨网络交换及 PayJoin 支持等高级功能于一身。它可以让您在三个网络上管理您的比特币： **链上比特币**、**Liquid** 和 **闪电网络*，每个网络都是为特定用途定制的。在[BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)上，您可以查看当前主题和即将进行的开发。由于该项目是 100% 的开源和 "公开构建"，您也可以发送您的建议和遇到的任何错误。虽然现在有些钱包支持多个网络，但 Bull Bitcoin 钱包通过深度整合所有网络的隐私功能而脱颖而出，成为在所有主要网络中管理比特币的强大工具。


## 1️⃣ 先决条件


在开始使用 **Bull Bitcoin Wallet** 之前，请确保您已准备好以下物品：



- **兼容的智能手机**：iOS（iPhone 或 iPad）或 Android 设备
- 互联网连接
- **安全备份介质**：在纸张或金属上写下您的**恢复助记词**（12 个单词），并将其存放在安全的地方。
- **基础知识**：对比特币概念（地址、交易、费用）的了解是有用的，不过本教程会为初学者解释每个步骤。


## 2️⃣安装


您可以通过以下方式安装应用程序：



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(适用于 iOS 设备)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) （适用于安卓设备）


安卓用户也有其他选择：



- 直接从 [GitHub 公布](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) 页面下载 APK 或
- 通过兼容 Nostr 的 [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap) 安装


安装应用程序后，请在欢迎屏幕上配置您的账户。


## 3️⃣ 初始配置


打开时，系统会提示您以下选项：



- `Create New Wallet`
- `Recover Wallet`
- `Advanced Options`


首先点击 `Advanced Options`


在这里，我们可以在创建或恢复 wallet 之前配置高级设置：


1.启用 `Tor proxy`，通过 Tor 网络路由流量。

1.[Orbot 应用程序](https://orbot.app/en/) 需要安装并运行后才能启用

2.Tor proxy仅适用于比特币（不适用于 Liquid），可能会导致连接速度变慢。

2.设置 `Custom Electrum Server`，或

3.调整 `Recover Bull` 设置。稍后我们将进一步了解 [Recover Bull](https://recoverbull.com/)。


完成所有可选调整后，点击 `Done`。如果您想重新使用现有的钱包，请点击 `Recover Wallet` 并填写恢复助记词的 12 个单词。


否则，点击 `Create a New Wallet`。


![image](assets/en/01.webp)


## 4️⃣主屏幕


在深入了解之前，让我们先看看 "主屏幕"，了解一下方向：



- `transaction overview`（交易概览）和 `settings menu`（设置）位于页面顶部。
- `Available Balance`（余额）提供隐私选项，可自由 `turned on or off`（开启或关闭）。
- 进入 `Bitcoin Bull Exchange` 可进行 `Buy, Sell, or Pay`（购买，出售，支付）操作（功能视地区法规而定，可能需要 KYC）。
- 支持钱包之间的转账 `Transfer`。
- `Secure Bitcoin` 对应链上比特币钱包（Onchain Bitcoin Wallet）。
- 通过闪电 / Liquid 网络进行 `Instant payments`。
  *（说明：Bull Bitcoin Wallet 支持通过闪电网络进行收付款。通过闪电网络接收的资金会自动经由 [*Boltz exchange*](https://boltz.exchange/) 转换后存入 [*Liquid network*](https://liquid.net/) 的钱包即时支付中。这样您无需自己管理流动性通道，就能在保持自我托管的前提下使用闪电网络。）*
- `Send`（发送）和 `Receive`（接收）比特币。


![image](assets/en/02.webp)


首先，让我们进行一些重要配置，并从 `Backup` 备份开始。


## 5️⃣备份


开始备份过程时，请点击应用程序右上角的 "齿轮图标 (⚙)"，然后选择 "钱包备份"。您将看到两种保护钱包安全的方法：`Encrypted Vault`（加密密钥库） 和 `Physical Backup`(物理备份）。让我们一一探讨。


![image](assets/en/03.webp)


### 物理备份


点击 `Physical Backup` (物理备份），查看代表您的恢复或种子助记词，由 12 个单词组成。请考虑以下因素：



- 以最谨慎的态度写下您的 "恢复助记词"。写在纸上或金属上，并将其保存在安全的地方（保险箱、离线位置）。该助记词是您在丢失设备或删除应用程序时访问比特币的唯一途径。
- 还需要注意的是，任何人都可以用这个助记词盗取您所有的比特币。千万不要以数字方式存储：
- 不要截图
- 不要使用云、电子邮件或信息备份
- 不要使用复制/粘贴功能（有保存到剪贴板的风险）


![image](assets/en/25.webp)


下一个屏幕会让您按照正确的顺序排列单词，以确保您的种子助记词正确无误。测试成功后，您会收到确认信息。


! **这一点至关重要**。如需进一步帮助，请打开以下链接：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 加密密钥库


还可以选择在云中进行加密、匿名备份。但我们在上一段中不是说过，云备份有风险，应该避免吗？不过，Bull Bitcoin 团队开发了一种巧妙的方法来确保备份过程的安全性。具体操作如下：


`Recoverbull` 是一种备份协议，它通过将备份分成两部分来简化比特币的安全保护。首先，您的钱包备份文件会使用一个强大的加密密钥在您的设备上加密。您可以将加密文件保存到任何地方，如 Google Drive 或您的设备。其次，解锁文件所需的加密密钥存储在密钥服务器中。为了恢复钱包，您需要加密备份文件和密钥，您可以使用 PIN 或密码访问密钥。这种设计确保了在没有特定备份文件的情况下，仅有云备份是无用的，仅有密钥服务器也是无用的。这样，即使其中一部分遭到破坏，也能确保您的资金安全。


把它视为一个保险箱。加密备份文件就是*保险箱*，您可以将其存储在任何地方（如 Google Drive）。您的恢复密码就是*密钥*，由 Recoverbull 密钥服务器单独存储。小偷需要同时获得您的特定盒子和特定密钥才能打开盒子。这样的设计可以确保即使有人拿到了您的备份文件，如果没有服务器上的密钥，它也是无用的，而服务器上的密钥如果没有您独一无二的备份文件，也是无用的。


了解关于 `Recoverbull` 钱包备份协议的[更多信息](https://recoverbull.com/)。


点击 `Encrypted Vault`，然后点击 `Continue` 以使用默认服务器确认。连接将通过 `Tor` 网络进行，以确保隐私和匿名性。


**了解您的密码**



- `App Unlock PIN`：在 `Settings > Security PIN` 中设置的可选密码，用于锁定手机上的应用程序。
- `Recovery PIN`：在 `Encrypted Vault` 备份过程中创建的强制密码，用于在恢复过程中解密备份文件。


这是两个不同的 PIN 码。不要忘记您的恢复 PIN 码，因为它对恢复钱包至关重要。


**恢复密码设置：**



- 您必须创建 PIN 码或密码才能恢复对钱包的访问权限。
- PIN 码/密码必须至少为 6 位数字（例如，请避免使用 123456 等简单序列，此类序列不被接受）。
- 没有此 PIN 码，您将无法恢复钱包访问权限。


然后，选择保险库提供商：

- `Google Drive` 或
- 自定义（如您的设备）


![image](assets/en/04.webp)


现在，保存 "备份文件"。接下来，点击 `Test Recovery`，选择已保存的备份文件或保险库，然后点击 `Decrypt Vault`。输入您的 "PIN 码" 或 "密码"。如果一切正常，就会出现 "Test completed successfully" 页面。


### 导入/带出标签


现在我们已经创建了备份，接下来让我们看看标签功能。Bull Bitcoin 钱包允许用户为收款地址和交易创建自定义标签，从而增强隐私性和组织性。这些标签有助于您对资金进行分类，因为发送到已标记地址的交易将继承该标签，您还可以为出站交易添加标签以跟踪其找零。该钱包完全支持 [BIP-329](https://bip329.org/)标准，这意味着您可以将所有标签导出到文件并将其导入到另一个钱包。此功能确保您可以无缝备份交易历史记录和分类，或在不同钱包之间迁移它们，而不会丢失您的个性化组织。

![image](assets/en/05.webp)


## 6️⃣设置


在确保主要备份安全后，让我们来探索设置中的其他功能。


### A - 确保准入


为了保护应用程序的安全，请前往 `Settings`，然后选择 `Security PIN` 以选择 PIN Code。创建一个强大的 PIN 码来锁定对钱包的访问。虽然此步骤是可选的，但我们强烈建议您这样做，以防止他人在未经授权的情况下使用您的手机。


![image](assets/en/06.webp)


### B - 连接个人节点（可选）


Wallet BullBitcoin 默认连接到 Electrum 服务器：第一个服务器由 Bull Bitcoin 管理，第二个服务器来自 Blockstream，这两个服务器都被认为不会保留日志，从而降低了跟踪风险。


为了提高保密性，您可以通过 Electrum 服务器将应用程序连接到自己的比特币节点。为此，请点击 `Settings > Bitcoin Settings > Electrum Server Settings`，然后点击 `+ Add Custom Server` 添加自定义服务器以输入服务器地址和凭证。


![image](assets/en/07.webp)


### C - 货币


可用余额以 `sats` 和 `USD` 两种货币显示在主屏幕上。要更改，请导航至 `Settings > Currency` 。在这里，您可以在 `sats/BTC` 之间切换，并选择您的 `默认法定货币`。


![image](assets/en/08.webp)


### D - 比特币设置


`Bitcoin Settings` 选单可深入访问钱包的核心配置和数据。在这里，您可以查看 "安全比特币" 和 "即时支付钱包" 的基本详情，从而实现完全透明的控制。该选单的主要功能包括：



- **Wallet Details**：前往您的安全比特币钱包或即时支付钱包查看具体信息。
- **Wallet Fingerprint**：您钱包的唯一标识符。
- **Public Key（Pubkey)**：用于生成您的比特币接收地址的密钥。
- **Descriptor**：您钱包结构的简要技术说明。
- **Derivation Path**：用于从您的主私钥生成所有地址的特定路径
- **Address View**：访问您未使用的接收地址和找零地址列表（即将推出）。


此外，您还可以选择：



- 启用自动转账设置，即可设置最大即时钱包余额，余额将自动转入安全的比特币钱包。
- 通过助记词导入通用钱包或导入仅查看钱包。
- 连接硬件钱包：目前支持的设备包括 ColdcardQ、SeedSigner、Specter、Krux、Blockstream Jade 和 Foundation Passport。


## 7️⃣ Bull Bitcoin 交易时


您可以通过钱包直接访问 [Bull Bitcoin 交易所](https://www.bullbitcoin.com/)，无需离开应用即可购买、出售和支付比特币。此集成为您提供了一种便捷的比特币管理方案。请注意，根据您所在司法管辖区的规定，访问交易所及其服务可能受到限制，并且您可能需要完成 “了解您的客户”（KYC）验证才能符合监管标准并使用平台的全部功能。


为了开始使用，请点击右下角的 `Exchange`，然后 `Sign Up`（注册）或 `Login`（登录）到您的账户。


交易所提供以下[功能](https://www.bullbitcoin.com/)：



- 使用您的银行账户自行保管购买比特币
- 非托管
- 个人或企业均可
- 即时提现
- 无隐藏费用
- 支持闪电网络
- 无交易限额
- 可定期购买


![image](assets/en/09.webp)


要了解更多信息，请访问本教程：


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣接收资金


使用 **Bull Bitcoin Wallet** 接收资金既简单又灵活，可支持针对不同使用情况定制的三种不同网络：



- 比特币（链上）网络提供安全、长期的存储服务。
- Liquid 网络提供快速、更私密的交易服务。
- 闪电网络提供即时、低成本的支付服务。

该应用会根据您选择的网络自动生成相应的地址或发票。以下是针对每种网络的具体操作步骤。


### 通过链上（比特币网络）接收资金


要接收链上资金，您可以从主屏幕选择 “Secure Bitcoin Wallet” 并点击 “Receive”，或者点击主 “Receive” 按钮，然后选择比特币网络。


生成接收地址有两种主要模式：


**默认模式（带有附加输入参数的 URI）**


默认情况下，钱包会生成一个 [BIP21 URI](https://bips.dev/21/)。这是一种标准化格式，包含比简单地址更多的信息，例如金额、个人备注和 PayJoin 参数，以增强隐私性。此完整 URI 会被编码成二维码，并可供复制。格式如下：bitcoin:<地址>?<参数1>=<值1>&<参数2>=<值2>。


- 其他输入参数：**
    - **Amount：** 指定请求的金额，以 BTC、聪或法定货币表示。
    - **Μessage：** 添加一条对发送方可见的个人备注.
    - **PayJoin：** 启用此选项可通过合并交易中发送方和接收方的输入来提高隐私性。


URI 例子：


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*重要提示：请勿向本教程中提到的地址发送任何资金，否则钱包将被删除。*

![image](assets/en/10.webp)


**已启用复制或扫描地址选项


启用 `Copy or scan Address only option` 后，应用程序将以 SegWit (bech32) 格式生成简单的比特币地址。


例如：


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


即使您输入了金额或备注，它们也不会包含在二维码或复制的地址中。


![image](assets/en/11.webp)


### 通过 Liquid Network 接收


您可以在 Liquid Network 上接收付款。进入“接收”界面后，您可以使用以下两种方式生成付款请求：


**1.**简单地址**：复制标准的 Liquid 地址。这是您在 Liquid Network 上的钱包的唯一标识符，不包含任何具体金额或消息。


地址例子：


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2.详细付款请求（URI）：** 您可以指定金额和备注，以便更清晰地表达您的付款请求。这些信息将自动编码成可共享的 URI 及其对应的二维码。



- **Amount**：您可以设置比特币 (BTC)、聪 (Sats) 或法定货币的金额。
- **Note**： 添加个人留言以标识交易。


**URI 例子：**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


要完成交易，请向发件人提供 "地址 "或 "URI"。您可以将其复制到剪贴板，或让他们直接扫描屏幕上的二维码。


![image](assets/en/12.webp)


### 通过闪电网络接收



Bull Bitcoin Wallet 还允许您通过闪电网络收发款项。其关键特性在于，通过闪电网络收到的资金会自动兑换并存储在您“即时支付钱包”内的 “Liquid Network” 上。这项服务由 “Boltz” 提供支持。这种设计使您能够享受闪电网络的快速和低成本，而无需管理流动性通道的复杂性，同时还能完全自主地保管您的资金。虽然这种混合模式是自主托管的，并且避免了管理通道的复杂性，但它引入了第三方服务（Boltz）、少量兑换费，并且依赖于 Liquid Network 的联盟成员作为密钥持有者，这与传统的非托管闪电钱包（您自行管理通道）有所不同。您可以在这里了解更多关于 Liquid 及其治理模型的信息：


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- **限额：**
  - **最低金额：** 需要达到最低发票金额。请在应用程序中查看当前限额。
  - **费用：** 您（收款人）需支付少量兑换费。此费用将从发送方转账的金额中扣除，并且可能会有所变动。

- **优势：**
  - **自托管：** 您的资金始终由您掌控，并安全地存储在 Liquid Network 上。
  - **避免高额链上费用：** 通过使用闪电并将资金存储在 Liquid 上，您可以绕过开设传统闪电通道所产生的链上费用。当累计金额达到一定规模并足以支付费用时，您可以选择稍后将资金转移到链上通道。

- **提示：** 对于两个 Bull Bitcoin 用户之间最具成本效益的交易，请直接使用 **Liquid Network**，以完全避免闪电兑换费用。


要接收付款，您必须生成“闪电支付发票”：

1. “输入金额”：指定您希望以比特币 (BTC)、聪 (Sats) 或法定货币接收的金额。

2. “添加备注”（可选）：添加备注或说明。此备注将嵌入发票中，并在付款完成后显示在您的交易记录中，方便您识别。

3. “发票有效期”：闪电支付发票有时效性，将在 12 小时后过期。如果在此期限内未付款，发票将失效，您需要生成新的发票。

您可以将发票复制到剪贴板或让付款人扫描屏幕上显示的二维码，从而将发票提供给付款人。


![image](assets/en/13.webp)


## 9️⃣寄送资金


您可以直接从主页或任何钱包访问发送界面。Bull Bitcoin Wallet 简化了流程，它会根据您输入的地址或发票（无论是粘贴还是通过扫描二维码）自动检测目标网络——比特币、Liquid 或 Lightning。


### 通过比特币网络进行链上交易


链上转账意味着您的交易将直接记录在比特币区块链上。这种方法最适合大额转账或对时间要求不高的转账。要开始操作，您可以点击右下角的 “Send” 按钮，然后扫描或输入一个标准的比特币地址。

如果您提供的地址未包含具体金额，系统会提示您在发送界面填写详细信息。您可以选择您偏好的单位来指定金额，例如比特币、聪或等值的法币。您还可以选择添加个人备注，这是一条私人备忘录，供您日后参考以识别交易。此备注不会与接收者共享。

相反，如果您扫描或粘贴的付款请求已包含所有必要信息，例如带有预定义金额的 BIP21 URI，则钱包将跳过数据输入界面，直接跳转到确认界面以授权付款。


![image](assets/en/14.webp)


在您的交易广播之前，您将看到一个确认屏幕。请务必花些时间仔细检查每个参数，尤其要注意收款地址、发送金额和网络费用。此屏幕还提供强大的工具，方便您自定义交易。

您可以通过两种主要方式控制费用。第一种方法是选择所需的交易速度，例如低、中或高，钱包会自动为您计算相应的费用。第二种方法允许您更精确地控制费用，您可以设置具体的费用，以聪为单位的绝对总额或每字节的相对费率表示，钱包会根据具体情况提供预估的确认时间。

对于高级用户，钱包提供了多种设置来微调交易。“手续费替换”（RBF）默认启用，这是一项实用功能，如果交易卡在内存池中，您可以通过提高费用重新广播来加速交易。您还可以手动选择要花费的“未花费交易输出”（UTXO）。这是 UTXO 整合的强大工具，UTXO 整合策略是将多个小额交易合并为一个大额交易。虽然这可能会增加当前交易的手续费，但它可以显著降低未来交易的手续费，尤其是在网络费用预计上涨的情况下。


![image](assets/en/15.webp)


当您扫描包含 `pj=` 参数的接收者付款请求（BIP21 URI）时，系统会自动尝试使用 PayJoin。如果您只是粘贴一个没有其他参数的纯地址，则此功能不会被激活。这种协作方式通过结合发送者和接收者的输入来增强隐私性，打破了共同输入所有权的启发式规则，并且在某些情况下还能更好地扩展规模并节省费用。


### 通过 Liquid Network 发送


Liquid Network 旨在实现快速、保密且费用极低的交易。当您通过 Liquid 发送资金时，资金将从您的“即时支付钱包”中扣除。流程非常简单：您只需输入或扫描收款人的 “Liquid 地址” 即可。


如果地址未指定金额，系统会在发送屏幕上提示您输入金额。您可以输入比特币 (BTC)、聪 (satoshi) 或法币金额。Liquid 的一个主要优势是其较低的最低交易门槛。与链上交易一样，您可以添加可选的个人备注以供自己记录。如果付款请求已包含金额，钱包将直接跳转到确认页面。


在 Liquid 交易的确认页面上，您可以查看交易详情。手续费非常低，并根据交易的复杂程度计算。通常约为 0.1 sat/vB，对于简单的交易而言，这相当于 20-40 satoshi（例如，截至 2025 年 12 月 21 日，约为 26 satoshi）。


![image](assets/en/16.webp)


### 通过闪电网络发送


您可以扫描闪电地址（如 "runningbitcoin@rizful.com"），设置金额和接收者备注，也可以扫描预设金额的发票，直接进入确认屏幕。


*请注意，最低金额和费用适用。


Bull Bitcoin Wallet 通过从您的即时支付钱包（基于 Liquid）提取资金，然后通过 Boltz 进行兑换，从而发送闪电网络支付。这种混合方式完全由您自行托管，避免了管理专用闪电网络通道的高额链上费用，但需要支付兑换费。为了获得最低成本，如果收款人也使用 Bull Bitcoin Wallet，您可以直接向其 Liquid 地址发送款项。


## 钱包之间的资金转移


Bull Bitcoin 允许您在安全比特币钱包和 Liquid Network 上的即时支付钱包之间，或向外部钱包转移比特币。如果想要进行转账，只需前往 “Transfer” 部分，选择源钱包和目标钱包，输入您要转移的金额，然后确认交易即可。

![image](assets/en/17.webp)


## 1️⃣1️⃣ 恢复您的 Bull Bitcoin Wallet


本节将介绍如果您丢失设备、卸载应用程序或需要更换新设备，如何重新访问您的 Bull Bitcoin Wallet 资金。如前所述，有两种主要的恢复方法：使用独特的 Recoverbull 方法和使用标准的 BIP39 助记词。


### 第一方法：恢复公牛


概述：钱包备份在本地加密。加密文件可以存储在云存储或其他设备上。加密密钥由 Recoverbull 密钥服务器存储。两者分别保存，必须结合使用才能恢复钱包。


首先，我将删除钱包及其所有资金，然后重新安装钱包。我们将再次进入欢迎界面。这次，选择 “Recover Wallet” 选项。然后，前往 “Encrypted Vault” 方法，确认使用默认密钥服务器，并选择您存储备份文件的位置或保险库提供商。


![image](assets/en/18.webp)


它会提示信息显示金库已成功导入。点击 “Decrypt Vault” 按钮并输入密码。下一个屏幕将显示您的余额和已恢复的交易数量。


![image](assets/en/19.webp)


### 第二方法：种子助记词


此方法使用您钱包的主恢复助记词，这是一个标准的 12 个单词的列表，可作为您资金的终极备份。它是恢复比特币钱包最通用的方法，因为它不依赖于任何特定的服务或服务器。只要您拥有此助记词，即使无法访问 Bull Bitcoin Key 服务器，您也可以在任何兼容设备上恢复您的钱包。

在欢迎屏幕上，选择 “Recover Wallet”。这次，选择 “Physical backup“ 方法。应用程序将显示一个单词网格。请仔细按顺序选择 12 个单词助记词中的每个单词。务必一丝不苟，因为任何一个错误都会导致钱包恢复错误。


## 1️⃣2️⃣ 连接硬件钱包


为了获得最高级别的安全性，许多比特币用户选择将资金存储在 “冷存储” 中。这意味着将控制您比特币的 “私钥” 保存在永远不会连接到互联网的设备上。“硬件钱包”（或签名设备）是一种专为此目的而设计的专用物理设备。它就像一个数字保险库，确保您的密钥永远不会暴露在联网电脑或智能手机的潜在威胁之下。


通过将硬件钱包连接到 Bull Bitcoin 应用程序，您可以兼得两者的优势：既能享受冷存储对私钥的绝对安全保障，又能使用 Bull Bitcoin 钱包的强大功能和用户友好界面来查看余额和管理交易。在本章中，我们将向您展示如何将硬件钱包（例如 [Coldcard Q](https://coldcard.com/q)）连接到您的 Bull Bitcoin 钱包。本教程不会详细介绍 Coldcard Q 的设置；您可以点击此处了解相关信息：


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### 导入钱包


![image](assets/en/26.webp)


首先，在您的 Coldcard Q 主选单中，选择 `Export Wallet`，然后选择 `Bull Wallet`。您的 Coldcard 将生成一个二维码。


![image](assets/en/20.webp)


打开 Bull Bitcoin Wallet，依次前往 `Settings` > `Bitcoin Settings` > `Import wallet`，然后选择手机上的 `Coldcard Q`，点击 `Open the camera` 扫描此二维码以导入硬件钱包的公钥。


![image](assets/en/21.webp)


### 使用 Coldcard Q 接收


使用已连接的 Coldcard Q 接收比特币时，无需将设备与手机进行物理连接。Bull Bitcoin Wallet 已导入必要的公钥，可以自动生成地址。


1. 点击已导入的 Coldcard Q 签名设备，然后选择 `Receive`。

2. 应用将自动显示 Coldcard 钱包中的新比特币地址。

3. 使用此地址接收资金。即使设备在接收过程中处于离线状态，比特币也会直接安全地存储在硬件钱包的密钥中。


![image](assets/en/22.webp)


### 使用 Coldcard Q 发送比特币

使用 Coldcard Q 发送比特币需要您进行硬件确认以授权交易。虽然 Bull Wallet 应用用于构建交易，但最终签名只能在硬件钱包本身上生成。

首先，打开您的 Coldcard Q 钱包并点击 `Send`。然后，打开相机扫描接收地址的二维码。扫描后，输入您要发送的金额，并根据需要调整手续费优先级。

更多选项，请查看 “Advanced Settings”。您可以在这里找到 `Replace by Fee` 选项，该选项默认启用，可用于加快稍后卡住的交易。您还可以使用 `Coin Control` 选项，手动选择要花费的特定 UTXO。

确认所有详细信息后，点击 `Show PSBT` 以准备交易。


![image](assets/en/23.webp)


点击 Coldcard Q 上的 `Scan` 按钮，使用其摄像头扫描手机上显示的二维码。Coldcard 屏幕将显示所有交易详情。请仔细核对金额、接收地址和找零地址。确认无误后，按下 Coldcard Q 上的 `Enter` 按钮签署交易。随后，屏幕上将显示已签名交易的二维码。


![image](assets/en/24.webp)


在 Bull Wallet 中，点击 `I'm done`，然后点击 “摄像头” 按钮，扫描 Coldcard Q 上 “已签名交易” 的二维码。Bull Wallet 将显示已签名交易的摘要页面。请再次确认，然后点击 `Broadcast`  以广播交易。此操作会将交易发送到比特币网络，您的资金将立即到账。


## 🎯 结论


您已完成 Bull Bitcoin Wallet 的使用体验。这款应用将强大的隐私和安全工具置于您的指尖，让高级功能触手可及。它通过 `PayJoin` 等功能帮助您保护隐私，该功能可隐藏您在区块链上的交易； `Tor integration` 功能可保护您的网络活动免受窥探。如果您想要完全掌控自己的资金，您可以连接到 “您自己的个人比特币节点”，摆脱对第三方服务器的依赖，并使用硬件钱包将您的私钥完全离线且安全地保存。凭借智能备份选项以及对比特币、Liquid 和 Lightning 的无缝支持，Bull Bitcoin Wallet 是任何认真对待资金隐私、安全和完全自主控制的用户的强大而全面的选择。


## Bull Wallet 资源


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [官方网站](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)
