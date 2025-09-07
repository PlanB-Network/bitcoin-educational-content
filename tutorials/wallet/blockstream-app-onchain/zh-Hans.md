---
name: 区块链应用程序 - Onchain
description: 在手机上设置 Blockstream 应用程序并管理链上交易
---
![cover](assets/cover.webp)


## 1.导言


### 1.1 辅导目标





- 本教程介绍如何使用 **Blockstream App** 移动应用程序管理 Bitcoin **onchain** Wallet，即直接在主 Blockchain Bitcoin 上记录的交易。
- 内容包括安装、初始配置、创建 Software Wallet 以及接收和发送比特币的操作。
- 注：附录中的其他教程涵盖 Liquid、仅观看和桌面版。



![image](assets/fr/01.webp)



### 1.2 目标受众





- 初学者**：希望使用直观移动应用程序管理比特币的用户。
- 中级用户**：希望了解链上功能和隐私选项（如 Tor 或 SPV）的用户。



### 1.3.关于 Hot 钱包的提醒





- Hot、Wallet**、**Software Wallet**、**Wallet mobile**、**Software Wallet**：都是安装在智能手机、电脑或任何联网设备上的应用程序名称，用于管理和保护来自 Bitcoin Wallet 的私人密钥。
- 与**硬件钱包**（也称为**Cold钱包**）不同的是，软件钱包是在联网环境中运行的，因此更容易受到网络攻击。





- 建议用途** ：
    - 非常适合管理中等数量的 Bitcoin，尤其是日常交易。
    - 适合初学者或资产有限的用户，对他们来说，Hardware Wallet 可能显得多余。





- 局限性**：对于存储大额资金或长期储蓄而言，安全性较低。在这种情况下，请选择 Hardware Wallet。




## 2.Blockstream 应用程序介绍





- Blockstream App**是一款移动（iOS、Android）和桌面应用程序，用于管理Bitcoin投资组合和Liquid Network上的资产。2016年被[Blockstream](https://blockstream.com/)收购，此前曾被命名为*Green Address*和*Blockstream Green*。
- 主要特点** ：
    - Blockchain Bitcoin 上的链上**交易。
    - 网络交易 **Liquid**（Sidechain 用于快速保密交换）。
    - 仅供观察**的投资组合，用于在无法获得密钥的情况下监控基金。
    - 隐私选项：通过**Tor**连接，通过 Electrum 与**个人节点**连接，或通过**SPV**验证，以减少对第三方节点的依赖。
    - 功能 **Replace-by-fee (RBF)** 可加快未确认交易的速度。
- 兼容性**：集成硬件钱包，如 **Blockstream Jade**。
- Interface**：为初学者提供直观操作，为专家提供高级选项。
- 注意**：本指南侧重于链上使用。附录中的其他教程涵盖 Liquid、Watch-Only 和桌面版。



## 3.安装和配置 Blockstream 应用程序



### 3.1. 下载





- 适用于安卓** ：
    - 从 Google Play 商店下载 [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)。
    - 替代方案：通过 [Blockstream 官方 GitHub](https://github.com/Blockstream/green_android) 上提供的 APK 文件进行安装。
- 适用于 iOS**：
    - 从 App Store 下载 [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)。
- 注意**：请务必从官方渠道下载，以避免欺诈性应用。



### 3.2. 初始配置





- 主屏幕**：首次打开时，应用程序会显示一个没有配置 Wallet 的屏幕。创建或导入的投资组合稍后将出现在这里。



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





- 功能**：通过**Electrum**服务器将应用程序连接到自己的**完整 Bitcoin 节点**。
- 为什么？提供对 Blockchain 数据的全面控制，消除对 Blockstream 服务器的依赖。
- 前提条件**：已配置 Bitcoin 节点。
- 建议**：寻求最大主权的高级用户。


#### 3.2.4.SPV 核查





- 功能**：使用 **简化支付验证（SPV）** 直接验证某些 Blockchain 数据，而无需下载整个链。
- 为什么？减少对 Blockstream 默认节点的依赖，同时保持移动设备的轻量级。
- 缺点**：安全性低于 Full node，因为它依赖第三方节点提供某些信息。
- 建议**：如果您无法使用个人节点，但又希望使用 Full node 以获得最佳安全性，请激活 SPV。





## 4.创建 Bitcoin onchain 投资组合



### 4.1.开始创建





- 注意**：在没有摄像头或旁观者的私密环境中设置您的投资组合。
- 从主屏幕点击 "开始"：



![image](assets/fr/04.webp)





- 如果您想管理**Cold Wallet**（离线 Wallet）：点击**"连接翡翠 "**，使用 Hardware Wallet Blockstream 翡翠或其他兼容的 Cold 钱包。



![image](assets/fr/05.webp)





- 出现下一个屏幕：



![image](assets/fr/06.webp)





- (1) **"设置移动 Wallet"**：创建新的 Hot Wallet（Hot Wallet）。
- (2) **"从备份恢复 "**：使用 Mnemonic 短语（12 或 24 个字）导入现有组合。注意：请勿导入 Cold Wallet 短语，因为它会在连接的设备上暴露，使其安全性失效。
- (3) **"只读 "**：导入现有的只读投资组合，以查看余额（例如您的 Cold Wallet 的余额），而不暴露 Mnemonic 短语。请参阅附录中的 "只读 "教程。



**在本教程中**：点击 **"设置移动 Wallet"**，创建 Hot Wallet。


您的 Wallet 将自动创建，并显示 Wallet 主页（此处称为 "我的 Wallet 5"）：



![image](assets/fr/07.webp)



**重要**：Blockstream App简化了Wallet的创建过程，不会自动显示12个字的seed短语。 *尽管现在只需点击一下即可创建投资组合，但如果您不保存seed短语*，则有可能无法使用您的资金。



### 4.2.保存 seed 句子





- 在 Wallet 主屏幕上点击 "安全 "标签，然后点击 "备份 "提示或 "恢复短语 "菜单：



![image](assets/fr/08.webp)



将显示 seed 12 字短语供您保存。





- 以最谨慎的态度写下你的恢复短语。写在纸上或金属上，并将其保存在安全的地方（安全的离线位置）。该短语是您在丢失设备或删除应用程序时访问比特币的唯一途径。
- 还需要注意的是，任何人都可以用这句话盗取你所有的比特币。千万不要以数字方式存储：
 - 无截图
 - 没有云、电子邮件或信息备份
 - 无复制/粘贴功能（保存到剪贴板的风险）



**!这一点至关重要**。有关备份的更多信息 ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3.确认 seed 判决



在向与该 seed 句子相关的 Address 发送资金之前，您必须测试 12 个单词的备份。



为此，我们将写下一个引用，删除 Wallet，用备份恢复它，然后检查引用是否不变。





- 在 Wallet 主屏幕上，点击 "设置 "选项卡，然后点击 "Wallet 详细信息"，复制 zPub（[扩展公开密钥](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602)）：



![image](assets/fr/09.webp)



注：可将 zpub Address 导入 Blockstream 应用程序，以实现 "仅观察 "功能（见附录）。





- 删除应用程序，然后输入 Mnemonic 短语，通过**"从备份恢复 "**恢复 Wallet，并检查 zpub 是否不变。如果是，则说明备份正确，可以向 Wallet 发送资金。





- 要了解有关如何执行恢复测试的更多信息，这里有专门的教程 ：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5.确保应用程序的访问安全



使用强大的 PIN 码锁定应用程序的访问权限：




- 从 Wallet 主屏幕进入 **"安全 "**，然后点击 **"PIN "**。
- 输入并确认 ** 一个随机的 6 位数 PIN 码**。



**生物识别选项**：可提供更多便利，但安全性低于强大的 PIN 码（存在未经授权访问的风险，例如睡眠时的指纹或面部扫描）。



**注意**：密码可确保设备安全，但只有 seed 短语可用于取款。





## 5.使用链上 Wallet



### 5.1.接收比特币





- 在投资组合主屏幕上，点击 "**交易**"，然后点击**"接收 "**。



![image](assets/fr/10.webp)





- 应用程序会显示**空白的接收 Address**（SegWit v0 格式，以 "bc1q... "开头）。每次接收 Bitcoin 时使用新的 Address 可以提高保密性。





- 选项** ：
    - (1) "Bitcoin"：点击选择链上或 Liquid 装运，并选择资产。
    - (2) 点击箭头，选择与该 seed 句子相关联的另一个新的 Address。
    - (3) 您也可以点击右上角的三个点，然后点击 "地址列表"，从已使用/显示的地址中选择一个 Address 地址。
    - (4) 如需申请特定金额，请单击右上方的三个点，选择 "申请金额"，然后输入所需金额。QR 将被更新，Address 将被 Bitcoin 付款 URI 取代。




![image](assets/fr/11.webp)





- 点击 "**分享**"、复制文本或扫描二维码，分享 Address/URI。
- 验证**：尽可能检查与收件人共享的 Address，以避免错误或攻击（如恶意软件修改剪贴板）。



### 5.2. 发送比特币





- 在投资组合主屏幕上，点击 "**交易**"，然后点击**"发送 "**：



![image](assets/fr/12.webp)





- 输入详细信息** ：
    - (1) 通过粘贴或扫描二维码，输入收件人**的**Address。
    - (2) 核对资产和资金汇出账户。
    - (3) 指明要发送的**金额。您可以选择单位：BTC、Satoshis、USD...


2025 年 8 月 3 日的最低金额（冲洗限额）为 546 Sats。




    - (4) 选择 ** 交易费** ：
        - 根据紧急程度从建议选项（如快速、中速、慢速）中进行选择，并显示大致的传输时间。
        - 如需自定义收费，请手动调整每 vbytes 的 Satoshi 数量（有关市场费率，请参阅 [Mempool.space](https://Mempool.space/)）。




![image](assets/fr/13.webp)





- 检查** ：
    - 检查摘要屏幕上的 Address、金额和费用。
    - Address 错误可能导致无法挽回的资金损失。谨防修改剪贴板的恶意软件。



![image](assets/fr/14.webp)





- 确认**：滑动 "发送 "按钮，签署并分发交易。
- 后续**：在 Wallet 的 "交易 "选项卡中，交易显示为 "待定"，直至确认（1 至 6 次确认）：



![image](assets/fr/15.webp)





- 只要交易尚未确认，"Replace by fee "功能（见附录）就可以通过增加交易费用来加快交易处理速度：



![image](assets/fr/16.webp)




## 附录



### A1.其他 Blockstream 教程



使用 Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

在 "仅限观看 "模式下导入和跟踪 Wallet



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

桌面版



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2.Replace-by-fee (RBF) 说明



**定义**：Replace-by-fee（RBF）是 Bitcoin 网络的一项功能，允许发送方通过同意支付更高的费用来加速**链上**交易的确认。



**限制** ：




- RBF 不适用于 Liquid 或 "闪电 "交易。
- 在创建初始交易时，必须将其标记为与 RBF 兼容，Blockstream App 会自动这样做。



**更多信息：**




- [术语表](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3.最佳做法



要安全高效地使用**Blockstream App**，请遵循以下建议。它们将帮助您在**Bitcoin（onchain）**、**Liquid**和**Lightning**网络上保护您的资金、优化您的交易并维护您的机密性。





- 确保您的恢复短语** ：
 - 教程：保存您的 Mnemonic 短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 使用安全验证** ：
 - 激活**强密码**或**生物认证**（指纹或面部识别），以保护对应用程序的访问。
 - 切勿共享您的 PIN 码或生物识别数据。





- 保护您的隐私** ：
 - generate 为每个链上或 Liquid 接收提供一个新的 Address，以限制对 Blockchain 的跟踪。
 - 激活 "增强隐私"、"Tor "和 "SPV "功能。
 - 为了最大限度地保密，请通过 Electrum 服务器将 Wallet 连接到您自己的 Bitcoin 节点，而不要使用公共节点





- 选择最适合您需求的网络** ：
 - Onchain**：长期托管或大额交易的首选（费用与金额相比可忽略不计）。
 - Liquid**：用于快速、低成本的传输，保密性更强。
 - 闪电**：选择即时、低成本的小额转账。





- 请务必检查送货地址** ：
 - 汇款前，请仔细检查 Address。发送到错误的 Address 的资金将永远丢失。使用复制/粘贴或 QR 码扫描，切勿手工复制/修改 Address。





- 优化成本** ：
 - 对于链上交易，根据紧急程度和网络拥塞情况选择适当的收费（慢、中、快）。
 - 少量使用 Liquid 或 Lightning。





- 随时更新应用程序




### A4.额外资源





- 官方链接：**
 - [官方网站](https://blockstream.com/)**
 - [支持移动应用程序](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)**：文档和聊天
 - [GitHub](https://github.com/Blockstream/green_android)**





- 街区探险家：**
 - on chain ： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **[Blockstream Info](https://blockstream.info/Liquid)**
 - 闪电 **[1ML (Lightning Network)](https://1ml.com/)**





- 学习和教程：** ** [Plan ₿ Network](https://planb.network/)** ：
 - 保护您的恢复短语



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [词汇](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** ：
 - [词汇](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb