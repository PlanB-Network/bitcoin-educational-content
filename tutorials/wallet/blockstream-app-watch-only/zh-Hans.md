---
name: Blockstream App - 仅限观看
description: 如何在 Blockstream App 上配置 Watch-only wallet？
---

![cover](assets/cover.webp)


## 1.导言


### 1.1 本教程的目的





- 本教程介绍如何设置和使用**Blockstream App** 移动应用程序的**仅监控**功能，在不访问私钥的情况下监控 Bitcoin Wallet。
- 内容包括安装、初始配置、导入扩展公钥，以及使用它跟踪余额和 generate 接收地址。
- 注：附录中提供的其他教程涵盖 Onchain、Liquid 和桌面版。



### 1.2.目标受众





- 初学者**：希望通过直观的移动应用程序监控 Bitcoin 投资组合（通常与 Hardware Wallet 相关联）的用户。
- 中级用户**：希望使用 Tor 或 SPV 等隐私选项管理只读投资组合的用户。
- Hardware Wallet 用户**：无需连接设备即可查看余额和 generate 地址。
- 企业和商店** ：
 - 在不暴露私人密钥的情况下，为会计目的跟踪交易。
 - 验证在线支付系统中未输入私钥的交易。
 - 让员工无需获取私钥即可使用 generate 新接收地址。
- 组织和众筹**：向捐助者透明地显示余额，但不允许获取资金。



### 1.3.介绍 "仅限观看 "功能



只需**监控** Wallet 允许您监控 Bitcoin Wallet 的交易和余额，而无需访问私钥。与传统的 Wallet 不同，它只存储公共数据，如**扩展**公钥**（由此产生了 "**xpub**"，然后是 "zpub"、"ypub "等），这使它能够获取接收地址并跟踪 Blockchain Bitcoin 上的交易历史。没有私钥就无法从应用程序中支付资金，从而保证了更高的安全性。



![image](assets/fr/10.webp)



**为什么要使用 Watch-only wallet？





- 安全性**：是监控由**Hardware Wallet**保护的投资组合的理想选择，同时不会暴露连接设备上的私人密钥。
- 方便**：无需连接 Hardware Wallet，即可查看余额和 generate 新收件人地址。
- 保密性**：与**Tor**或**SPV**等选项兼容，以限制对第三方服务器的依赖。
- 使用案例**：追踪移动中的资金、生成收款地址或验证交易，而无需冒私钥风险。



![image](assets/fr/01.webp)



### 1.4.扩展公钥



扩展公钥**（xpub、ypub、zpub 等）是由 Bitcoin Wallet 生成的数据，可生成所有子公钥及其相关的接收地址，但不提供私钥。





- 工作原理** ：扩展公开密钥通过确定性过程 (BIP-32) 从 seed 短语生成。它创建了一个子公钥层次树，每个子公钥都可转换为接收 Address。Watch-only wallet 使用与被监听 Wallet 相同的派生路径（如 `m/44'/0'/0'`），生成相同的地址，从而可以跟踪资金并创建新的接收地址。



![image](assets/fr/11.webp)





- 扩展的公钥类型
 - xpub**：用于传统组合（地址以 "1 "开头，BIP-44）和 Taproot 组合（地址以 "bc1p "开头，BIP-86）。
 - ypub**：专为兼容的 SegWit 钱包（地址以 "3 "开头，BIP-49）设计。
 - zpub**：与本地 SegWit 组合相关（地址以 "bc1q "开头，BIP-84）。
 - 其他（tpub、upub、vpub 等）**：用于替代网络（如 Testnet）或特定标准。例如，tpub 用于 Testnet 网络。





- 区别** ：xpub、ypub或zpub之间的选择取决于Address类型（传统、SegWit、Taproot或嵌套SegWit）和Wallet使用的BIP标准。请检查您的源组合所需的格式，以确保与 Blockstream App 兼容。





- 安全性和保密性** ：扩展公开密钥在安全性方面并不敏感，因为它不允许使用资金（无法访问私人密钥）。但是，它在保密性方面是敏感的，因为它会显示所有公共地址和相关的交易历史。



**建议**：将扩展公钥作为敏感信息加以保护。



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5.Hot Wallet 提示





- Hot Wallet**、**Software Wallet**、**Wallet mobile**、**Software Wallet**：安装在智能手机、计算机或任何连接到互联网的设备上的应用程序的所有名称，可管理和保护来自 Bitcoin Wallet 的私人密钥。
- 与**硬件钱包**（也称为**Cold钱包**）不同的是，软件钱包是在联网环境中运行的，因此更容易受到网络攻击。





- 建议用途** ：
    - 非常适合管理中等数量的 Bitcoin，尤其是日常交易。
    - 适合初学者或资产有限的用户，对他们来说，Hardware Wallet 可能显得多余。





- 局限性**：对于存储大额资金或长期储蓄而言，安全性较低。在这种情况下，请选择 Hardware Wallet。




## 2.Blockstream 应用程序介绍





- Blockstream App**是一款移动（iOS、Android）和桌面应用程序，用于管理Bitcoin投资组合和Liquid Network上的资产。2016年被[Blockstream](https://blockstream.com/)收购，此前曾被命名为*Green Address*和*Blockstream Green*。
- 主要特点** ：
    - Blockchain Bitcoin 上的链上**交易。
    - 在**Liquid**网络上进行交易（Sidechain用于快速、保密的交流）。
    - 只需观察**的投资组合，用于在无法获得密钥的情况下监控基金。
    - 隐私选项：通过**Tor**连接，通过 Electrum 与**个人节点**连接，或通过**SPV**验证，以减少对第三方节点的依赖。
    - 功能 **Replace-by-fee (RBF)** 可加快未确认交易的速度。
- 兼容性**：集成硬件钱包，如 **Blockstream Jade**。
- Interface**：为初学者提供直观操作，为专家提供高级选项。
- 注意**：本指南重点介绍 Onchain 的使用。附录中的其他教程涉及 Onchain、Watch-Only 和桌面版。




## 3.安装和配置 Blockstream 应用程序



### 3.1. 下载





- 适用于安卓** ：
    - 从 Google Play 商店下载 [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)。
    - 替代方案：通过 [Blockstream 官方 GitHub](https://github.com/Blockstream/green_android) 上提供的 APK 文件进行安装。
- 适用于 iOS**：
    - 从 App Store 下载 [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)。
- 注意**：请务必从官方渠道下载，以避免欺诈性应用。



### 3.2. 初始配置





- 主屏幕**：首次打开时，应用程序会显示一个没有配置 Wallet 的屏幕。创建或导入的投资组合稍后会出现在这里。



![image](assets/fr/02.webp)





- 自定义设置**：点击 "应用程序设置"，调整以下选项，点击 "保存"，重新启动应用程序并创建您的作品集。



![image](assets/fr/03.webp)



#### 3.2.1.增强隐私保护（仅限安卓系统）





- 功能**：禁用屏幕截图，隐藏任务管理器中的应用程序预览，并在锁定手机时锁定访问权限。
- 为什么？保护您的数据，防止未经授权的物理访问或屏幕捕获恶意软件。



#### 3.2.2.通过 Tor 连接





- 功能**：通过**Tor**路由网络流量，这是一个对连接进行加密的匿名网络。
- 为什么？隐藏你的 IP Address 并保护你的隐私，如果你不信任你的网络（例如公共 Wi-Fi），它是你的理想选择。
- 缺点**：由于加密，可能会降低应用程序的运行速度。
- 建议**：如果保密性优先，请激活 Tor，但要测试连接速度。



#### 3.2.3.连接个人节点





- 功能**：通过**Electrum 服务器**将应用程序连接到自己的**完整 Bitcoin 节点**。
- 为什么？提供对 Blockchain 数据的全面控制，消除对 Blockstream 服务器的依赖。
- 前提条件**：已配置 Bitcoin 节点。
- 建议**：希望获得最大主权的高级用户。



#### 3.2.4.SPV 核查





- 功能**：使用**简化支付验证（SPV）**直接验证某些 Blockchain 数据，而无需下载整个链。
- 为什么？减少对 Blockstream 默认节点的依赖，同时保持移动设备的轻量级。
- 缺点**：安全性低于 Full node，因为它的某些信息依赖于第三方节点。
- 建议**：如果您无法使用个人节点，但又希望使用 Full node 以获得最佳安全性，请激活 SPV。





## 4.创建 Bitcoin "只看不买 "投资组合



### 4.1.恢复扩展公开密钥



要设置 Watch-only wallet，必须首先获取要监控的 Wallet 的扩展公钥（xpub、ypub、zpub 等）。该信息通常可在软件或 Hardware Wallet 的设置或 "Wallet 信息 "部分找到。





- 使用 Blockstream 应用程序的示例：从 Wallet 主屏幕进入 "设置"，然后进入 "Wallet 详情"，复制 zpub .NET 文件：



![image](assets/fr/09.webp)





- 替代方案 1：generate 包含扩展公钥的二维码，供下一步扫描。
- 替代方案 2：如果 Wallet 提供 output descriptor，则使用 output descriptor。



### 4.导入 Wallet 专用监视器





- 注意**：在没有摄像头或旁观者的私密环境中设置您的投资组合。
- 在主屏幕上点击 "设置新的投资组合"，然后点击 "开始"：



![image](assets/fr/04.webp)





- 出现下一个屏幕：



![image](assets/fr/06.webp)






- (1) **"设置移动 Wallet"**：创建新的 Hot Wallet。请参阅附录中的 "Blockstream App - Onchain "教程。
- (2) **"从备份恢复 "**：使用 Mnemonic 短语（12 或 24 个字）导入现有组合。注意：请勿从 Cold Wallet 导入词组，因为它会在连接的设备上暴露，使其安全性失效。
- (3) **"仅限观看 "**：本教程中我们感兴趣的选项。





- 然后选择 "**单一签名**"和 "**Bitcoin**"网络：



![image](assets/fr/12.webp)





- 粘贴扩展公钥（xpub、ypub、zpub 等）、扫描相应的二维码或输入 output descriptor。即使应用程序指定的是 "xpub"，也可以授权使用 ypub、zpub 等密钥。然后点击 "连接"：



![image](assets/fr/13.webp)




### 4.3.使用 Wallet 仅表



导入后，Watch-only wallet 会显示扩展公钥衍生地址的总余额和交易历史。只有链上交易可见（Liquid 交易被忽略）。要监控 Liquid Wallet，请在上一步中选择 "Liquid"，重复导入。





- 查看余额和历史**：从主屏幕查看总余额和链上交易历史：



![image](assets/fr/14.webp)





- generate 一个接收 Address**：点击 "交易"，然后点击 "接收"，创建一个新的链上 Address。通过二维码或复制分享，即可接收资金：



![image](assets/fr/15.webp)





- 发送资金**：点击 **"交易 "**，然后点击 **"发送 "**。您可以输入 ：
 - 收件人的 Address。
 - 交易金额。
 - 交易费。



但是，由于 Watch-only wallet 不持有私钥，因此不能直接发送资金。要签署交易，请通过扫描二维码连接 Hardware Wallet 或 Exchange PSBT（例如 Coldcard Q 上的一个选项）。



![image](assets/fr/16.webp)





- 注意**：请务必检查收款 Address 和交易详情，以免出错。发送到错误的 Address 的资金无法收回。




## 附录



### A1.其他 Blockstream 应用程序教程





- 使用 Onchain 网络 ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- 使用 Liquid Network ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 桌面版 ：



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2.扩展公开密钥





- 术语表 ：
 - [扩展公用钥匙](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- 课程 ：
 - [Les clés publiques étendues](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/les-cles-etendues-8dcffce1-31bd-5e0b-965b-735f5f9e4602)




### A3.最佳做法



要安全高效地使用**Blockstream App**，请遵循以下建议。它们将帮助您在**Bitcoin（onchain）**、**Liquid**和**Lightning**网络上保护您的资金、优化您的交易并维护您的机密性。





- 确保您的恢复短语** ：
 - 教程：保存 Mnemonic 短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 使用安全验证** ：
 - 激活**强密码**或**生物认证**（指纹或面部识别），以保护对应用程序的访问。
 - 切勿共享您的 PIN 码或生物识别数据。





- 保护您的隐私** ：
 - generate 为每个链上或 Liquid 接收提供一个新的 Address，以限制 Blockchain 上的跟踪。
 - 激活 "增强隐私"、"Tor "和 "SPV "功能。
 - 为了最大限度地保密，请通过 Electrum 服务器将 Wallet 连接到您自己的 Bitcoin 节点，而不要使用公共节点





- 选择最适合您需求的网络** ：
 - Onchain**：长期托管或大额交易的首选（费用与金额相比可忽略不计）。
 - Liquid**：用于快速、低成本传输，保密性更强。
 - 闪电**：选择即时、低成本的小额转账。





- 请务必检查送货地址** ：
 - 汇款前，请仔细检查 Address。发送到错误 Address 的资金将永远丢失。使用复制/粘贴或二维码扫描，切勿手工复制/修改 Address。





- 优化成本** ：
 - 对于链上交易，根据紧急程度和网络拥塞情况选择适当的收费（慢、中、快）。
 - 少量使用 Liquid 或 Lightning。





- 不断更新应用程序




### A4.额外资源





- Blockstream 官方链接：**
 - [官方网站](https://blockstream.com/)**
 - [支持移动应用程序](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)**：文档和聊天
 - [GitHub](https://github.com/Blockstream/green_android)**





- 街区探险家：**
 - Onchain： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **[Blockstream Info](https://blockstream.info/Liquid)**
 - 闪电 **[1ML (Lightning Network)](https://1ml.com/)**





 - 学习和教程：** ** [Plan ₿ Network](https://planb.network/)** ：
  - 保护您的恢复短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [词汇](https://planb.network/fr/resources/glossary/Liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** ：
 - [词汇](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb