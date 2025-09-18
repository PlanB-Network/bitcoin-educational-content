---
name: Blockstream App - Desktop
description: 如何在电脑上使用带有 Blockstream 应用程序的 Hardware Wallet？
---
![cover](assets/cover.webp)



## 1.导言



### 1.1 辅导目标





- 本教程介绍如何在计算机上使用**Blockstream 应用程序**，用**Hardware Wallet**管理**链上**Bitcoin 和**链上**Wallet，实现在主 Blockchain Bitcoin 上记录的安全交易。
- 内容包括安装、初始配置、连接 Hardware Wallet 以及接收和发送链上比特币。
- 注：附录中的其他教程涵盖 Liquid、仅限观看和移动应用程序。



### 1.2 目标受众





- 初学者：希望使用安全桌面软件和 Hardware Wallet 管理比特币的用户。
- 中级用户：希望了解如何使用 Hardware Wallet 进行链上交易以及 Tor 或 SPV 等隐私选项的用户。



### 1.3.硬件钱包的背景





- **Hardware Wallet**、**Cold Wallet**：与**Hot 钱包**（连接设备上的软件钱包）不同，它是一种离线存储私钥的物理设备，可提供高度安全的网络攻击防护。
- **建议用途**：
    - 是确保大额或长期储蓄的理想选择。
    - 适合注重安全、希望保护资金免受联网设备风险影响的用户。
- 限制：需要使用 Blockstream App 等软件查看余额、generate 地址和广播 Hardware Wallet 签名交易。



## 2.Blockstream 应用程序介绍





- **Blockstream App**是一款移动（iOS、Android）和桌面应用程序，用于管理Bitcoin钱包和Liquid Network上的资产。2016年被Blockstream收购，原名为*GreenAddress*，后更名为*Blockstream Green*（2019年），现名为*Blockstream app*（2025年）。
- **主要特点**：
- Blockchain Bitcoin 上的链上**交易**。
    - **Liquid**网络上的交易（Sidechain用于快速、保密的交换）。
- 只需观察**的**投资组合，用于在无法获得密钥的情况下监控基金。
    - 隐私选项：通过**Tor**连接，通过 Electrum 与**个人节点**连接，或通过**SPV**验证，以减少对第三方节点的依赖。
    - 功能 **Replace-by-fee (RBF)** 可加快未确认交易的速度。
- **兼容性**：集成硬件钱包，如 **Blockstream Jade**。
- **Interface**：为初学者提供直观操作，为专家提供高级选项。
- 注意**：本指南侧重于在桌面版 Hardware Wallet 上使用 onchain。作为附录提供的其他教程涵盖了在移动应用程序上使用 onchain、Liquid 和仅观看功能。



## 3.安装和设置 Blockstream App 桌面



### 3.1. 下载





- 访问 [官方网站](https://blockstream.com/app/) 并点击"_Download Now_"（立即下载）。下载与您的操作系统（Windows、macOS、Linux）相对应的版本。
- 注意**：请务必从官方来源下载，以避免使用欺诈软件。**



### 3.2. 初始配置





- 主屏幕：首次打开时，应用程序会显示一个没有配置 Wallet 的屏幕。创建或导入的投资组合稍后会出现在这里。



![image](assets/fr/02.webp)





- 自定义设置：点击左下角的设置图标，调整下面的选项，然后退出 Interface 继续。



![image](assets/fr/03.webp)



#### 3.2.1.一般参数





- 在设置菜单中，点击 "**常规**"。
- **功能**：根据需要更改软件语言并激活实验功能。



![image](assets/fr/04.webp)



#### 3.2.2.通过 Tor 连接





- 在设置菜单中，点击 "**网络**"。
- 功能：通过**Tor**路由网络流量，这是一个对连接进行加密的匿名网络。
- 为什么？隐藏你的 IP Address 并保护你的隐私，如果你不信任你的网络（例如公共 Wi-Fi），它是你的理想选择。
- **缺点**：由于加密，可能会降低应用程序的运行速度。
- **建议**：如果保密性优先，请激活 Tor，但要测试连接速度。



![image](assets/fr/05.webp)



#### 3.2.3.连接个人节点





- 在设置菜单中，点击 "**自定义服务器和验证**"。
- 功能：通过 **Electrum 服务器**将应用程序连接到自己的**完整 Bitcoin 节点**。
- 为什么？提供对 Blockchain 数据的全面控制，消除对 Blockstream 服务器的依赖。
- **前提条件**：已配置 Bitcoin 节点。
- **建议**：希望获得最大主权的高级用户。



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4.SPV 核查





- 在设置菜单中，点击 "**自定义服务器和验证**"。
- 功能：使用**简化支付验证（SPV）**，下载区块头并通过包含证明（Merkle）验证您的交易，无需存储完整的 Blockchain。
- 为什么？减少对 Blockstream 默认节点的依赖，同时保持设备的轻量级。
- 缺点：安全性低于 Full node，因为它的某些信息依赖于第三方节点。
- 建议：如果您无法使用个人节点，但又希望使用 Full node 以获得最佳安全性，请激活 SPV。



![image](assets/fr/07.webp)



## 4.将 Hardware Wallet 连接到 Blockstream 应用程序



### 4.1.初步考虑



#### 4.1.1.针对 Ledger 用户





- Blockstream Green 仅支持 Ledger 设备（Nano S、Nano X）上的 **Bitcoin Legacy** 应用程序。
- 连接设备前在 **Ledger Live** 中应遵循的步骤 ：


1.进入 **"设置 "** → **"实验功能 "** 并激活 **开发者模式**。


2.进入 **"我的 Ledger"**→**"应用程序目录 "**，然后安装 **Bitcoin Legacy** 应用程序


3.在启动 Blockstream Green 以建立连接之前，在 Ledger 上打开 **Bitcoin Legacy** 应用程序。




- 注意**：请确保您的 Ledger 已用 PIN 码解锁，并且连接时 Bitcoin 传统应用程序处于激活状态。



#### 4.1.2 初始化 Hardware Wallet





- 如果您的 Hardware Wallet（Ledger、Trezor 或 Blockstream Jade）从未使用过（无论是与 Blockstream Green 还是与 Ledger Live 等其他软件一起使用），您首先需要对其进行初始化。这一步需要在没有摄像头或观察员的安全环境中进行：


1. **seed短语生成/Mnemonic短语**（12、18或24个字）：在纸上认真写下来。


2. **seed 短语验证**：测试 Wallet 从指定词组导入的情况，例如通过验证扩展公钥。在向 Wallet 发送资金和永久保护 seed 短语之前进行。


3. **保护 seed 短语**：将短语存储在物理介质（纸张或金属）上并放在安全的地方。切勿以数字形式存储（禁止截图、云或电子邮件）。




- **重要**：如果设备丢失或发生故障，seed 短语是您找回资金的唯一途径。任何有权限的人都可以盗取您的比特币。
- 用于备份和检查 seed 句子的资源：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3.本教程的配置 ：





- 我们假设 Hardware Wallet 已经用 seed 短语和锁定 PIN 码进行了初始化。
- 我们假设 Hardware Wallet 从未连接过 Blockstream App，因此需要创建一个新账户。如果 Hardware Wallet 已经与 Blockstream App 一起使用，则在打开应用程序时会自动显示账户。



### 4.2.开始连接





- 在主屏幕上点击 "**设置新的 Wallet**"，然后验证条款和条件并点击 "**开始**"：



![image](assets/fr/08.webp)





- 选择 "**在 Hardware Wallet 上**"选项：



![image](assets/fr/09.webp)





- 如果您使用的是 **Blockstream Jade**，请点击相应按钮。否则，请选择 "**连接不同的硬件设备**"：



![image](assets/fr/10.webp)





- 通过 USB 将 Hardware Wallet 与电脑连接，然后在 Blockstream App 中选择它：



![image](assets/fr/22.webp)





- Blockstream 应用程序将导入您的投资组合信息，请稍候：



![image](assets/fr/23.webp)



### 4.3.创建账户





- 如果您的 Hardware Wallet 已与 Blockstream App 配合使用，您的账户将在导入后自动出现在 Interface 中。否则，请点击 "**创建账户**"创建账户：



![image](assets/fr/24.webp)





- 选择 "**标准**"配置经典的 Bitcoin 组合：



![image](assets/fr/25.webp)





- 创建账户后，您就可以访问您的 Interface 主要投资组合：



![image](assets/fr/26.webp)





## 5.将链上 Wallet 与 Hardware Wallet 配合使用



### 5.1.接收比特币





- 在投资组合主屏幕上，点击 "**接收**"：



![image](assets/fr/27.webp)





- 应用程序会显示**空白的接收 Address**。每次接收都使用新的 Address 可以提高保密性。点击 "**复制 Address**"复制 Address，或让发件人扫描显示的二维码：



![image](assets/fr/12.webp)



**选项** ：




- (1) 点击箭头 generate 链接到您的投资组合的新 Address。
- (2) 如需申请具体金额，请点击 "**更多选项**"，然后点击 "**申请金额**"。QR 将被更新，Address 将被 Bitcoin 付款 URI 所取代，例如：`Bitcoin:bc1q...?`Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) 要重复使用以前的 Address，请点击 "**更多选项**"，然后点击 "**地址列表**"：



![image](assets/fr/14.webp)





- 验证**：仔细检查共享 Address，避免错误或攻击（如恶意软件修改剪贴板）。
- 交易在网络上广播后，将出现在您的 Wallet 中。等待 1 到 6 次确认后，交易将不可更改。



![image](assets/fr/28.webp)



### 5.2. 发送比特币





- 在作品集主屏幕上点击 "**发送**"。



![image](assets/fr/29.webp)





- **输入详细信息**：
    - (1) 检查所选资产是否为 **Bitcoin**（链上）。
    - (2) 通过粘贴或使用网络摄像头扫描二维码，输入收件人**的**Address。
- (3) 指明要发送的**金额（以 BTC、Satoshis 或其他单位表示）**。




![image](assets/fr/16.webp)





- 选择 **交易费用**（可选） ：
 - 根据紧急程度从建议选项（快速、中速、慢速）中选择，并预计确认时间。
 - 如需自定义收费，可手动调整每 vbyte 的 Satoshis 数。这将显示在主屏幕上。另请参阅 [Mempool.space](https://Mempool.space/)。



![image](assets/fr/17.webp)





- 手动选择UTXO**（可选）**：点击**手动选择 Coin**，选择要在交易中使用的特定UTXO。



![image](assets/fr/18.webp)





- 初步核实：在摘要屏幕上检查 Address、金额和费用，然后点击 "**确认交易**"。实际上，只有在您用 Hardware Wallet 签名后，交易才会被释放到网络上，因为只有 Hardware Wallet 才拥有与UTXO（satoshis）扣款地址相关的密匙。



![image](assets/fr/19.webp)





- 最后检查和签名：确保 **Hardware Wallet** 屏幕上的所有交易参数**正确**，然后使用该屏幕签署交易。Address 错误可能导致不可挽回的资金损失。





- 广播：一旦签署，Blockstream App 将自动在 Bitcoin 网络上广播交易。



![image](assets/fr/20.webp)





- **后续行动**：
 - 交易在 Wallet 主页屏幕上显示为 "待处理"，直至确认。
 - 只要交易尚未确认，就可以使用 **Replace-by-fee (RBF)** 功能，通过增加费用来加快确认速度（见附录）。



![image](assets/fr/21.webp)



## 附录



### A1.其他 Blockstream 教程





- 使用 Liquid Network ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- 导入并跟踪 "仅供观察 "的投资组合：



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- 在手机上使用 Blockstream 应用程序 (Hot Wallet) ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2.Replace-by-fee (RBF) 说明





- 定义：Replace-by-fee (RBF) 是 Bitcoin 网络的一项功能，允许发送方通过增加费用来加快**链上**交易的确认。
- **限制**：
    - RBF 不适用于 Liquid 或 Lightning 交易。
    - 初始交易必须标记为与 RBF 兼容，Blockstream App 会自动进行标记。
- 更多信息，请参见 [我们的术语表](https://planb.network/resources/glossary/RBF-replacebyfee)。



### A3.最佳做法





- 确保您的恢复短语**安全**：
    - 将您的 Hardware Wallet 的 Mnemonic 短语保存在物理介质（纸张、金属）上，放在安全的地方。
    - 切勿以数字方式存储（云、电子邮件、截图）。
    - 教程：保存您的 Mnemonic 短语：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **保护您的隐私**：





    - generate 为每次链上接收提供一个新的 Address。
    - 激活**Tor**或**SPV**以限制跟踪。
    - 通过 Electrum 连接到您自己的 Bitcoin 节点，以获得最大的主权。
- 请务必检查**送货地址**：





    - 签字前请检查 Hardware Wallet 屏幕上的 Address。
    - 使用复制/粘贴或 QR 码，避免人工出错。
- **优化成本**：





    - 根据紧急程度和网络拥塞情况调整收费（见 [Mempool.space](https://Mempool.space/)）。
    - 使用 Liquid 或 Lightning 进行无需链上安全的快速、低成本交易。
- **更新软件**：





    - 让您的 Blockstream 应用程序和 Hardware Wallet 固件保持更新，提供最新功能和安全补丁。



### A4.额外资源





- **官方链接**：
    - [官方网站](https://blockstream.com/)
    - [支持 Blockstream 应用程序](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)：文档和聊天
    - [GitHub](https://github.com/Blockstream/green_qt)





- **街区探险家**：
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - 闪电：[1ML (Lightning Network)](https://1ml.com/)





- 保护您的恢复短语：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network**：



[术语表](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**：



[术语表](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb