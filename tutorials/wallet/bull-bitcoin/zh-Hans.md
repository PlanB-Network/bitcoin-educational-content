---
name: Bull Bitcoin Wallet
description: 了解如何使用 Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



本指南将带您了解 Bull Bitcoin Mobile 的安装、配置和使用。您将了解如何在三个网络上接收和发送资金：onchain、Liquid 和 Lightning，以及如何将 Bitcoin 从一个网络转移到另一个网络。附录提供了资源和联系方式、背景信息以及技术概念的简要解释。



## 导言



由**[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel))开发的**Bull Bitcoin Mobile**是一款**自我保管**的Bitcoin Wallet，这意味着您可以完全控制自己的私钥，从而完全控制自己的资金，而无需依赖第三方。该 Wallet 是开源的，根植于 Cypherpunk 理念，集简单性、保密性和跨网络交换及 PayJoin 支持等高级功能于一身。它可以让你在三个网络上管理你的比特币： **Bitcoin onchain**、**Liquid** 和 **Lightning**，每个网络都为特定用途量身定制。



### 发展背景



Wallet 应对了一个重大挑战：Bitcoin 网络收费不适合小额支付，也不适合开设小型自托管闪电渠道。Wallet Bull Bitcoin Mobile 依赖于 3 个主要的 Bitcoin 网络，提供自托管解决方案：





- Bitcoin 网络（onchain）：中长期存储 UTXO 和大额交易的理想选择，其费用按比例计算可忽略不计。
- **Liquid Network**：专为快速（约 2 分钟）、更保密（隐藏金额）、低成本交易而设计，非常适合小额积累或保护您的隐私。
- 闪电**网络**：针对即时、低成本支付进行了优化，适合中小型日常交易。



以 Bull Bitcoin Mobile 为例，您可以在**Liquid**或**Lightning**投资组合中积累少量资金，然后，一旦达到相当可观的金额，您就可以在**Liquid**或**Lightning**投资组合中积累更多资金：





- 转移到链上网络进行安全的中期或长期存储，利用上游的 Liquid 和/或 Lightning 提高保密性，并对单笔交易收取链上费用



### 持续演变



Wallet 在不断发展，因此如果您发现本教程与您的最新应用程序之间存在差异，请不要感到惊讶。




- 例如，截至 2025 年 7 月 19 日，**"买入/卖出/支付 "** 按钮在应用程序中是可见的，但显示为灰色，因为这些选项可在 Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel) 上使用，不久将整合为统一的体验。它们的使用仍然完全是可选的。许多其他开发正在进行或计划中：多 Wallet 管理、passphrase、与硬件钱包的兼容性...
- 在 [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)，您可以查看当前主题和即将进行的开发。由于该项目是 100% 的开源和 "公开构建"，您也可以向我们发送您的建议和遇到的任何错误。




## 1.先决条件



在开始使用 **Bull Bitcoin Mobile**之前，请确保您已准备好以下物品：





- 兼容智能手机：**iOS**（iPhone 或 iPad）或**安卓设备**
- 互联网连接
- 安全备份介质：在纸张或金属上写下你的**恢复短语**（12 个字），并将其存放在安全的地方。
- **基本知识**：对 Bitcoin 概念（地址、交易、费用）有起码的了解是有用的，不过本教程会为初学者解释每个步骤。



## 2.安装





- **下载申请表**：
- [Google Play 商店](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) 从安卓设备的应用程序商店下载
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) 直接下载安卓设备的 **APK**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) 通过 TestFlight 为苹果设备下载
 - 检查开发人员的姓名（Bull Bitcoin），避免出现欺诈性申请。
 - 确保下载的版本与 GitHub 上显示的最新稳定版本一致。
 - Bull Bitcoin Mobile 是**开源**。查看代码：[BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- 安装应用程序




## 3.初始配置



### 3.1 启动应用程序 ：



该应用程序为两个组合使用了一个独特的 12 个字的恢复短语：




- 安全 **Bitcoin Wallet**：用于 Bitcoin 网络（链上）的交易
- 即时支付的 **Wallet**：用于 Liquid 和 Lightning 网络上的即时交易



打开时，系统会提示您导入现有的恢复短语，或创建新的 Wallet ：



![image](assets/fr/02.webp)



### 3.2 恢复词组 ：



如果您希望重新使用现有的 Wallet，请单击 "**恢复 Wallet**"并填写恢复短语的 12 个字。



否则，点击 "**创建新的 Wallet**"：




- 以最谨慎的态度写下您的恢复短语。写在纸上或金属上，并将其保存在安全的地方（保险箱、离线位置）。该短语是您在丢失设备或删除应用程序时访问比特币的唯一途径。
- 还需要注意的是，任何人都可以用这句话盗取你所有的比特币。千万不要以数字方式存储：
 - 无截图
 - 没有云、电子邮件或信息备份
 - 无复制/粘贴功能（保存到剪贴板的风险）



**!这一点至关重要**。如需进一步帮助 ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 确保访问安全 ：





- 进入设置，然后点击 ** 密码**。
- 设置强大的**PIN 码**，以保护对应用程序的访问。
- 此步骤为可选步骤，但强烈建议使用，以防止任何可以访问手机的人访问您的 Wallet。



![image](assets/fr/03.webp)



### 3.4 连接个人节点（可选）：



Wallet BullBitcoin 默认连接到 Electrum 服务器：第一个服务器由 Bull Bitcoin 管理，第二个服务器来自 Blockstream，这两个服务器都被认为不会保留日志，从而降低了追踪风险。



为了提高保密性，您可以通过 Electrum 服务器将应用程序连接到您自己的 Bitcoin 节点上（说明可在［BullBitcoin 的 GitHub］(https://github.com/orgs/SatoshiPortal/projects/49) 上获取）。




## 4.接收资金



使用**Bull Bitcoin Mobile**接收资金非常简单，而且可根据您的需求量身定制，无论您使用的是.NET还是.NET：




  - 长期保护**Bitcoin（onchain）** 网络、
- **Liquid网络**，实现更快、更多的Confidential Transactions、
- 闪电**网络**进行即时、低额支付。



应用程序会根据所选网络自动生成 Lightning 接收地址或 Invoice 地址。以下是每个网络的操作步骤。



### 4.1. Onchain（Bitcoin 网络）



在主屏幕上，您可以 ：




- 或选择 "**安全 Bitcoin Wallet**"，然后点击 "**接收 "**：



![image](assets/fr/04.webp)





- 或点击 "**接收 "**，然后选择**Bitcoin**网络：



![image](assets/fr/05.webp)



#### 4.1.1.仅复制或扫描 Address "选项已禁用（默认值）



![image](assets/fr/06.webp)





- 这样就可以访问可选的高级参数。您可以指定 ：
- 以 BTC、Sats 或法定货币表示的**金额**。
 - 在 URI / QR 码副本中附上**个人说明**。
 - 激活 **PayJoin**（详见附录 3），通过合并发件人和收件人条目提高保密性。





- **自动生成 URI 的示例**：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- 使用**复制 URI 与发件人共享，或让他扫描二维码**。



#### 4.1.2.仅复制或扫描 Address "选项已启用



![image](assets/fr/07.webp)





- 如果启用**"仅复制或扫描 Address"**选项，应用程序将生成 SegWit (bech32) 格式的简单 Bitcoin Address。





- 例如



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



即使您输入了金额或备注，它们也不会包含在 QR 码或 Address 的副本中。





- 使用**复制**：复制 Address 与发件人共享，或让他扫描二维码。



#### 4.1.3.生成新的 Address





- 为什么每次交易都要使用新的 Address？这样可以**保护您的隐私**，防止多笔付款被链接到同一个 Address，并限制在 Blockchain 上进行跟踪的可能性。
- 默认情况下，公牛 Bitcoin 会自动生成一个未使用的 Address。
 - 点击屏幕下方的**"新建 Address"**，即可强制创建新的 Address。
 - 您的所有地址都与 seed 短语相关联：无论您使用多少个地址，您的投资组合都将显示单一余额，并可在发货时自动合并资金。





- 提示：始终使用公牛 Bitcoin 提供的新 **Address**，除非您有特殊需要（如接收捐赠的公共 Address）。



### 4.2.Liquid



在主屏幕上，您可以 ：




- 或选择**即时付款 Wallet**，然后点击**"接收 "**，再点击**"Liquid"**：



![image](assets/fr/08.webp)





- 或点击 "**接收 "**，然后选择**Liquid**网络：



![image](assets/fr/09.webp)



进入 **"接收 "** 屏幕后，复制一个 Liquid Address：





- 无金额或备注。例如



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- 或指定**金额**（以 BTC、Sats 或法币表示）和/或**个人备注**，将其包含在 URI / QR 代码副本中。例如



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**使用**：复制 Address/URI 与发件人共享，或让他扫描二维码。



### 4.3.闪电



在主屏幕上，您可以 ：




- 或选择 "**即时付款 Wallet**"，然后点击 "**接收 "**：



![image](assets/fr/10.webp)





- 或点击 "**接收 "**，然后选择**闪电**网络：



![image](assets/fr/11.webp)



#### 4.3.1.运行、限制和效益





- 机制：公牛 Bitcoin Wallet 是一款能够通过 "闪电 "进行支付和接收的 Wallet。通过 **Boltz** 自动交换，通过闪电收到的资金将存储在 **Liquid** 网络（Wallet即时支付中）。这使您能够与 Lightning 进行互动，而无需管理流动性渠道，同时保持自我保管。





- 限制：
- 购买 generate 和 Invoice 时，最低金额**为 100 星**（截至 2025 年 7 月 19 日）。
- 您支付的费用**将从发件人发送的金额中扣除，这与使用 Wallet Lightning native 接收不同，在后者中，只有发件人在发送金额之外支付转账费用**。截至 2025 年 7 月 19 日，47 Sats 将从发送金额中扣除。





- **福利**：
- **自我监护**：您的资金仍由您控制，存储在 Liquid Network 上。
- 没有高昂的链上费用：存储在 Liquid 上可避免为开通闪电通道或增加流动性而支付高昂的链上存款费用。当 Liquid 上积累的金额足以支付相关费用时，您可以稍后再进行这些操作。





- 提示：**如果发送方有 Wallet Bull Bitcoin，请直接使用 Liquid Network，以避免交换费**



#### 4.3.2.generate Invoice





- 输入**金额**（以 BTC、Sats 或法币表示）





- 添加**个人备注**，该备注将并入 Invoice。如果发件人支付了 Invoice，您的 Wallet 也会将其包含在交易详情中。





- Invoice 有效期：**闪电 Invoice 的有效期为 12 小时**。过期作废，不能再支付。必须生成新的 Invoice。





- 使用**复制**：复制 Invoice 与发件人共享，或让他扫描二维码。




## 5.发送资金



### 5.1.基本原则



无论是从主页，还是从钱包 ：



![image](assets/fr/12.webp)



进入发送屏幕：



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** 可根据输入的 Address 或 Invoice（复制或通过二维码扫描）自动检测网络（Bitcoin、Liquid 或 Lightning），从而轻松发送汇款。



### 5.2. 链上传输（Bitcoin 网络）



#### 5.2.1.发送屏幕



**行动**：输入或扫描 Bitcoin onchain Address





- 如果未定义金额，例如 ：



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- 然后，您可以在发送屏幕上选择 ：
 - 以 BTC、sat 或法币表示的金额。最低金额：546 萨托什，2025 年 7 月 22 日。
 - 用于标识交易的可选备注。只有您可以在交易详情中看到。



![image](assets/fr/14.webp)





- 如果金额已经定义，例如 ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



然后，您将直接进入下面的确认界面。



#### 5.2.2 确认屏幕



花时间检查所有参数，特别是金额、目的地 Address 和费用。


然后就可以调整参数了：



![image](assets/fr/15.webp)




- 费用：您可以选择：
- 您的交易执行速度和相关费用都会估算出来。
- 以绝对费用（总费用，单位为卫星）或相对费用（每字节费用）模式计算费用，并估算您的交易速度





- **高级设置**：





- **Replace-by-fee (RBF)**：默认情况下已激活，该功能通过支付更高的费用来加快交易速度（详见附录 4）。





- 手动选择 UTXO：如果您的资金存储在多个不同的 Wallet 地址，您可以选择发送资金的地址。为什么要这样做？随着 Bitcoin 的采用率越来越高，转账费用也在增加。从多个地址发送小额资金比从单个 Address 发送资金更贵，但现在这样做可以避免日后费用更高时再这样做。这就是所谓的 **UTXO 合并**。



![image](assets/fr/16.webp)





- 使用 **PayJoin** 发送：如果提供 URI 的收件人已激活该功能，例如：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



然后，公牛 Bitcoin Mobile 将通过将您的 UTXO 与收件人的 UTXO 合并作为输入来配置发送，从而提高保密性（详见附录 3）。



### 5.3.发送至 Liquid



#### 5.3.1 发送屏幕



**Liquid**网络可实现快速交易（每分钟一个区块，约 2 分钟），比链上网络更加保密（掩盖金额），且费用极低。资金从**即时支付 Wallet** 提取。



**行动**：输入或扫描 Liquid Address





- 如果未定义金额，例如 ：



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



然后，您可以在发送屏幕上选择 ：




- 以 BTC、sat 或法币表示的金额。无最低限额，1 Satoshi 也可；
- 用于标识交易的可选备注。只有您可以在交易详情中看到。



![image](assets/fr/17.webp)





- 如果金额已经定义，例如 ：



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



然后，您将直接进入下面的确认界面。



#### 5.3.2 确认屏幕



花时间检查所有参数，尤其是数量和目的地 Address。



![image](assets/fr/18.webp)





- 费用：与交易的复杂程度成比例，一般按 0.1 Sat/vB 计算，即简单交易为 20-40 Satoshis（7/22/2025 时为 33 Sats）。



### 5.4.发送到 "闪电



#### 5.4.1 发送屏幕



**Lightning**网络可实现即时、低成本的小额支付，是日常小额交易的理想选择。



**行动**：输入或扫描闪电 Invoice





- 如果您扫描 LN-URL Address，可以设置金额


例如： `orangepeel@walletofsatoshi.com`。


然后就可以在发送屏幕上选择 ：




 - 以 BTC、sat 或法币表示的金额。2025 年 7 月 23 日的最低金额为 1000 萨托希
 - 用于标识交易的可选备注。它将发送给收件人。



![image](assets/fr/19.webp)





- 如果扫描的 Lightning Invoice 含有规定数量的


例如



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



然后，您将直接进入下面的确认界面。



注：金额必须大于 21 Sats （2025 年 7 月 23 日



#### 5.4.2 运行、限制和效益





- 机制：资金从**即时支付 Wallet** (Liquid)中提取，并通过**Liquid → Lightning** 与**Boltz**的交换进行转换。





- 限制：
- 最低**量高于 Wallet 闪电本机**（见上文）
- 支出**加** Liquid → 通过 Boltz 进行闪电交换





- **福利**：
- 自我监管：您的资金仍在您的控制之下，存储在 Liquid Network 上，如有需要，可通过 "闪电" 转账
- 没有高昂的链上费用：存储在 Liquid 上，为您节省了开通闪电通道或增加流动性所需的高昂链上存款费用。当 Liquid 上积累的金额足以支付相关费用时，您可以稍后再进行这些操作。





- 提示：**如果收件人有 Wallet Bull Bitcoin，请直接使用 Liquid Network，以避免交换成本**



#### 5.3.3 确认屏幕



花时间检查所有参数，特别是数量和目的地 Address。



![image](assets/fr/20.webp)




## 6.查看历史



通过**Bull Bitcoin Mobile**，可轻松跟踪您在**Bitcoin（onchain）**、**Liquid**和**Lightning**网络上的交易。历史记录可通过两种方式访问，并显示每类交易的详细信息。您也可以使用外部区块浏览器查看您的交易。



### 6.1.访问历史





- 通过主屏幕** ：
 - 点击**安全 Bitcoin Wallet** 查看**链上**交易，或点击**即时支付 Wallet** 查看**Liquid**和**闪电**交易。
 - 历史记录显示在投资组合总额的正下方，根据所选的 Wallet 类型进行筛选。



![image](assets/fr/21.webp)





- 通过专用网页：
 - 在主屏幕上，点击**历史符号**（时钟图标或类似图标）。
- 访问列出所有交易的页面，可按操作类型进行筛选：**发送**、**接收**、**交换**、**PayJoin**、**卖出**、**买入**（注：卖出和买入正在开发中，2025 年 7 月 20 日暂时不可用）。



![image](assets/fr/22.webp)



### 6.2.交易详情



每笔交易都会显示特定信息，具体取决于网络和操作类型（发送或接收）。以下是链上**交易**的详细信息：



![image](assets/fr/23.webp)



### 6.3.通过 Block explorer 进行检查



附录 4 列出了**Bitcoin onchain**、**Liquid** 和**Lightning**网络的勘探者名单。



对于**闪电**，交易在公共浏览器上不可见。请在应用程序中查看详细信息（包括 Boltz 的交换 ID）。




## 7.设置



可从公牛 Bitcoin 应用程序主页直接访问 "设置 "页面，该页面用于配置和管理产品组合和用户体验的各个方面。



![image](assets/fr/24.webp)





- **Wallet 备份**：显示用于安全备份的组合恢复短语。有关管理和存储恢复短语的最佳做法，请参阅第 3 节 "组合创建"。





- **Wallet 详情**：
- **Pubkey**：与 Wallet 相关联的公开密钥，用于 generate Bitcoin 接收地址。
- 派生路径：用于从私人密钥获取 **generate Wallet** 地址的派生路径。





- Electrum 服务器（Bitcoin 节点）：建立与定制的 Bitcoin 节点的连接，用于链上交易。





- **PIN 码**：激活和/或修改安全密码，以保护对应用程序和 Wallet 功能的访问。





- **货币**：选择以 BTC 或 Sats 以及默认法定货币（美元、欧元等）显示金额。





- 自动交换设置：**自动交换**功能允许您自动将您的 BTC 从**即时支付 Wallet (Liquid)** 转至您的**Bitcoin On-Chain** Wallet，只要金额达到您认为足以支付交易费的阈值。





- 日志：可查看活动日志，这些日志可与技术支持共享，以方便故障排除。





- **Telegram 访问支持**：直接链接到官方 Telegram 频道，为用户提供帮助。





- Github 访问：链接到[Bull Bitcoin Github 代码库](https://github.com/SatoshiPortal) 以查看开放源代码或报告问题。




## 附录



### A1.PayJoin (P2EP) 说明



![image](assets/fr/25.webp)



**定义** ：




- PayJoin，或**支付到终端（P2EP）**，是一种 Bitcoin 交易技术，可增强**链**网络的保密性。它将发送方和接收方条目合并在一个交易中，使金额和地址更难追踪。



**行动：**




- 在 PayJoin 交易中，发送方和接收方通过兼容的 PayJoin 服务器合作进行 generate 联合交易。
- 接收方不再只提供发送方的条目（UTXO），它也提供自己的一个UTXO。这就模糊了 Blockchain 上的信息：现在有两个条目，而不是与实际金额相对应的一个条目，输出也不能直接反映交换的金额。
- 最终交易类似于标准的 Bitcoin 交易（多输入/多输出），但通过隐写结构隐藏了实际发送金额和地址之间的链接。



**用于公牛 Bitcoin 移动式**




- 接收**地址供应**（Address Supply）：PayJoin 默认已启用。
- 发送** ：例如，Wallet 会自动检测 PayJoin URI 并对交易进行相应配置：



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**福利**




- 增强保密性：PayJoin 使交易中所有条目均属于单一实体的假设失效。有了 PayJoin，输入来自发送方和接收方，从而打破了这一假设。
- **金额屏蔽**：实际交换金额不直接显示在输出中。它是根据接收方的 UTXO 入站和出站之间的差额计算出来的，从而使分析具有误导性。



**限制**




- PayJoin 要求发送方和接收方使用兼容的钱包，否则将使用标准的链上交易。
- 交易略微复杂（输入和输出较多），因此成本略高。
- 尽管其设计类似于标准交易，但先进的启发式方法（如模糊的输出、已知的 PayJoin 服务器）可能会让人怀疑其使用，尽管没有绝对的把握。



**更多信息：**




- [术语表](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2.Replace-by-fee (RBF) 的说明



**定义**：Replace-by-fee（RBF）是 Bitcoin 网络的一项功能，允许发送方通过同意支付更高的费用来加速**链上**交易的确认。



**限制** ：




- RBF 不能用于 Liquid 或闪电交易。
- 在创建初始交易时，必须将其标记为与 RBF 兼容，除非禁用，否则 Bull Bitcoin Mobile 会自动将其标记为与 RBF 兼容。



**更多信息：**




- [术语表](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3.最佳做法



要安全高效地使用**Bull Bitcoin Mobile**，请遵循以下建议。它们将帮助您在**Bitcoin（onchain）**、**Liquid**和**Lightning**网络上保护您的资金、优化您的交易并维护您的机密性。





- 确保您的恢复短语**安全**：
 - 教程：[Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- 使用**安全验证**：
 - 激活**强密码**或**生物认证**（指纹或面部识别），以保护对应用程序的访问。
 - 切勿共享您的 PIN 码或生物识别数据。





- **保护您的隐私**：
 - generate 为每个链上或 Liquid 接收创建一个新的 Address，以限制对 Blockchain 的跟踪。
 - 有条件时使用 PayJoin，以提高链上发送量的保密性
 - 为了最大限度地保密，请通过 Electrum 服务器将您的 Wallet 连接到您自己的 Bitcoin 节点，而不要使用公共节点





- 选择最适合您需求的**网络**：
- **Onchain**：长期托管或大额交易的首选（费用与金额相比可忽略不计）。
- **Liquid**：用于快速、低成本传输，保密性更强。
- **闪电**：选择即时、低成本的小额转账。如果您是两个 Wallet Bull Bitcoin 用户，请选择 Liquid，以避免通过 Boltz 的闪电 <> Liquid 掉期费用。





- 请务必检查**送货地址**：
 - 汇款前，请仔细检查 Address。发送到错误 Address 的资金将永远丢失。使用复制/粘贴或二维码扫描，切勿手工复制/修改 Address。





- **优化成本**：
 - 对于链上交易，根据紧急程度和网络拥塞情况选择适当的收费（慢、中、快）。
 - 少量使用 Liquid 或 Lightning。
 - 如果预计需要加快确认速度，请为链上装运激活 Replace-by-fee (RBF) （见附录 4）。





- 不断更新应用程序




### A4.额外资源





- 官方链接和支持：
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : 支持电子邮件
- [Bull Bitcoin 官方网站](https://bullbitcoin.com/)：有关 Bull Bitcoin 服务、创建账户、访问应用程序的信息
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile)：查看代码、演进和路线图，为开发做出贡献...
- [Account X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- **Wallet 移动电话的 Telegram** 群组：与支持人员群聊，请参见 "设置 "页面。





- 街区探险家：
 - on chain ： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **[Blockstream Info](https://blockstream.info/Liquid)**
 - 闪电 **[1ML (Lightning Network)](https://1ml.com/)**





- 学习和教程：**[Plan ₿ Network](https://planb.network/)**：
 - 保护您的恢复短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network**：
- [词汇](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**：
- [词汇](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5.公牛 Bitcoin



#### 公司概况



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**，是专门针对 Bitcoin 的历史最悠久的非存款 Exchange 平台，于 2013 年在加拿大蒙特利尔的 Bitcoin 大使馆成立。该公司由 Bitcoin 生态系统中公认的先驱弗朗西斯-普利奥特（Francis Pouliot）领导，将自己定位为促进金融主权和用户自主的关键参与者。公司的使命是通过使用 Bitcoin 作为自由和支付工具，让个人重新掌控自己的资金，同时拒绝 Bitcoin 之外的法定货币和加密货币。



![image](assets/fr/26.webp)



[创建您的帐户](https://app.bullbitcoin.com/registration/orangepeel) 购买和销售 Bitcoin 可享受 0.25% 的折扣。



#### 价值观和理念



公牛 Bitcoin 以其 Commitment 至 Cypherpunk 的原则和 Bitcoin 的道德规范而脱颖而出：





- 独家关注 **Bitcoin** ：该平台实现了去中心化、抗审查货币的愿景。





- **非托管**：用户将资金汇入自己的投资组合，从而保留对比特币的完全控制权。





- **保密性**：最大限度减少个人数据收集，999 美元以下的交易可选择免 KYC 购买。数据受相关法规（加拿大 FINTRAC、法国 AMF）保护。





- **透明**：无隐藏费用，成本包含在价差（买卖价格之间的差额）中。





- **金融主权**：Bitcoin 号公牛提倡独立于传统银行系统和中央机构。



#### 主要服务





- **法币存款**：用户可以在指定的加拿大邮局通过银行转账或现金/借记卡为公牛 Bitcoin 账户存入法定货币（加元、欧元等）。





- 购买 **Bitcoin** ：用户可以购买 Bitcoin，直接发送到他们的非存款组合中，保证对资金的完全控制。





- 定期购买 **Bitcoin**：公牛 Bitcoin 提供定期自动循环购买服务（DCA - 美元成本平均法），利用您的可用余额，将比特币直接转移到用户控制的 Wallet，减少价格波动的影响。



请注意，一个名为 "自动购买 "的选项允许您在法币触及您的 Bull Bitcoin 余额时立即将其转换为比特币，并将比特币发送到您自己的 Wallet。该选项还可以与您的银行安排的定期银行转账相结合，以进行 DCA。此选项可自动累积 Bitcoin，而无需打开应用程序。






- 以固定价格买入 Bitcoin 的 **"限价订单"**：允许您以用户预先指定的价格买入 Bitcoin，当公牛 Bitcoin 指数价格达到或低于设定限价时，限价自动执行。





- 出售 **Bitcoin**：用户可以出售比特币，并通过银行或 SEPA 转账将资金以法定货币直接存入自己的银行账户。





- 第三方支付：Bull Bitcoin 可以让用户用比特币向银行账户发送法币，对收款人完全透明。





- 公牛 **Bitcoin Prime**：公牛 Bitcoin Prime 是专为高净值客户和企业客户提供的高级服务，可提供定制解决方案和高级支持。其中包括享受费用减免、专职账户经理和量身定制的企业服务。这项服务面向寻求深入专业知识和优先待遇的机构、专业交易商和企业客户。





- 移动 **Wallet**：公牛 Bitcoin 提供开源的自托管移动 Wallet，可在 Android 和 iOS 上使用，支持链上交易、Liquid 和 Lightning Network 交易。





- 教育支持：免费指南和个性化辅导，帮助用户创建、保护和管理自己的 Bitcoin 投资组合，加强财务自主性。



#### 合规与安全





- 监管：公牛 Bitcoin 已在加拿大 FINTRAC 和法国 AMF 注册，符合 KYC/AML 要求。





- **安全**：使用安全的投资组合和离线存储建议。个人数据托管在公牛的 Bitcoin 基础设施上，该基础设施 100% 自托管，不依赖任何第三方。