---
name: KaleidoSwap
description: 使用 KaleidoSwap 在 Lightning Network 上进行 RGB 资产交易的高级指南
---

![cover](assets/cover.webp)


KaleidoSwap 是一个复杂的开源桌面应用程序，它在 RGB 协议和 Lightning Network 之间架起了一座桥梁。它是管理 RGB 闪电节点、通过 LSPS1 规范与 RGB 闪电服务提供商 (LSP) 交互以及执行 RGB 资产原子交换的综合界面。


作为一种非托管解决方案，KaleidoSwap 使用户能够保持对其密钥和数据的完全控制。通过利用 RGB 的客户端验证范式，它可以在 Bitcoin 的基础上实现私有和可扩展的智能合约。本教程深入探讨了 KaleidoSwap 的高级功能，指导您了解 "彩色 "UTXO 管理、特定资产的渠道流动性和做市商交易模式的复杂性，确保您能充分利用这个强大的去中心化交换协议。


## 安装


KaleidoSwap 提供适用于主要操作系统的预制二进制文件，但对于高级用户来说，从源代码构建可确保您在特定配置下运行最新代码。


### 下载二进制文件


您可以从 [官方网站](https://kaleidoswap.com/) 或 [GitHub 发布页面](https://github.com/kaleidoswap/desktop-app/releases) 下载适用于您操作系统的最新版本。


### 安装方法


1.  **Windows**：下载 `.exe` 安装程序并运行。

2.  **macOS**：下载`.dmg`文件，打开并将 KaleidoSwap 拖到应用程序文件夹。

3.  **Linux**：下载 `.AppImage` 或 `.deb` 文件并安装/运行。



## 节点设置选项


首次启动 KaleidoSwap 时，您将看到**连接屏幕**。这是配置环境的第一步。


![Node Selection Screen](assets/en/01.webp)


您必须选择连接到 RGB Lightning Network 的方式。这种选择会影响您的控制水平和隐私。


### 方案 1：本地节点（建议用于自我保管）


**要完全控制和保护隐私**，请直接在您的机器上运行节点，具体优势如下：


- 自我监护**：钥匙由您掌握。任何第三方都无法冻结您的资金或审查您的交易。
- 隐私**：您的数据将保留在您的设备上。
- 独立性**：不依赖外部服务提供商。


如果选择 ** 本地节点**，则将进入设置屏幕，在此可以创建新的 wallet 或恢复现有的 wallet。


![Local Node Setup Screen](assets/en/02.webp)


### 选项 2：远程节点


连接远程 RGB Lightning Node（在 VPS 或托管服务提供商上自行托管）。


- 优势**：无需使用本地资源，全天候可用。
- 权衡**：需要信任主机或管理远程服务器。


![Remote Node Setup Screen](assets/en/03.webp)


**我们强烈建议您运行自己的节点--无论是本地节点（选项 1）还是远程节点--以充分利用 Bitcoin 和 RGB 的抗审查特性。


## 创建 Wallet


KaleidoSwap 可管理 Bitcoin 和 RGB 资产。wallet 创建过程会初始化一个密钥存储，以确保 on-chain 资金和 Lightning 通道状态的安全。


下面是详细流程：

1.打开 KaleidoSwap，选择 ** 本地节点**。

2.点击 **创建新的 Wallet**。

3. **账户设置**：输入**账户名**并选择**网络**（例如，Bitcoin、Mainnet、Testnet、Signet）。

4. **高级配置**（可选）：如果您是高级用户，可以在 "高级设置 "下配置自定义 RPC 端点、索引器 URL 或代理设置。

5.点击**继续**。

6. **密码**：设置一个强大的密码，以便在本地加密 wallet 文件。

7. **恢复短语**：写下您的 seed 短语并妥善保存。


    - 关键**：要恢复 on-chain 资金和节点身份，需要使用此短语。
    - 警告**： **仅通过 seed 无法完全恢复闪电通道状态**。您还必须维护静态通道备份 (SCB)，以恢复锁定在通道中的资金。


![Wallet Creation Screen](assets/en/04.webp)



## 仪表板概述


创建 wallet 后，您将进入主**面板**。


![KaleidoSwap Dashboard](assets/en/05.webp)


注意：上面的截图显示的是已经注资并有活动频道的 wallet。在您注资之前，新的 wallet 将显示零余额，并且没有活动频道。


## 资助您的 Wallet


要操作 RGB 资产，您需要为 wallet 注资。KaleidoSwap 支持通过 on-chain 交易或 Lightning Network 存入 Bitcoin 和 RGB 资产。


### 存放 Bitcoin


1.点击快速操作菜单中的**存款**。

2.从资产列表中选择 **BTC**。


![Select BTC Asset](assets/en/06.webp)


3.选择您的存款方式： **链式**或闪电式**。


![BTC Deposit Options](assets/en/07.webp)



- 链上**：扫描二维码或复制地址，从另一个 wallet 发送 Bitcoin。
- 闪电**：生成所需金额的发票。


![BTC On-chain Deposit](assets/en/08.webp)


### 存放 RGB 资产和彩色 UTXO


要接收 RGB 资产（如 USDT），您需要特定的 UTXOs 可用来 "着色"（分配资产）。


1.点击 **存款**，选择 RGB 资产（如 USDT）。 **重要**：如果这是您的节点**次接收该特定资产，**请将资产 ID 字段留空**。输入未知资产的 ID 会导致节点返回错误，因为它还没有识别该资产。

2.选择**链式**或**闪电式**。


![USDT Deposit Options](assets/en/09.webp)


#### 链上接收模式：见证与盲目


接收 RGB 资产 on-chain 时，有两种隐私模式：



- 盲目接收（建议用于保护隐私）**：您向发送方提供一个 "blinded "UTXO。您要求发送方向您拥有的现有 UTXO 发送资产，但您混淆了 UTXO 的实际标识符。这将提供更好的隐私保护。
- 证人接收**：您提供了一个标准 Bitcoin 地址。您要求发送人为您创建一个*新的 UTXO，将资产发送到该地址。这样就可以将 RGB 资产直接附加到交易创建的新 UTXO。


#### 闪电存款


对于闪电存款，只需 generate 发票即可。RGB 资产将通过您的公开渠道转给您。


![USDT Lightning Invoice](assets/en/10.webp)



## 利用 RGB 资产打开渠道


要通过 Lightning Network 路由 RGB 资产，您需要一个具有足够流动性和资产配置的通道。最简单的入门方法是从 LSP（闪电服务提供商）**购买通道**。


### 从 Kaleido LSP 购买频道


1.转到 "**渠道**"选项卡。您将看到 "打开通道"（手动）或 "购买通道"（LSP）选项。

2.点击 ** 购买渠道**。


![Channels Dashboard](assets/en/11.webp)


3. **连接到 LSP**：应用程序将连接到默认的 Kaleido LSP。该提供商提供入站流动性并支持 RGB 资产路由。


![Connect to LSP](assets/en/12.webp)


4. **配置通道**：


    - 容量**：选择通道的 Bitcoin 总容量。
    - RGB 分配**：选择您希望接收或发送的 RGB 资产（如 USDT）。LSP 将确保通道配置支持该资产。


![Configure Channel](assets/en/13.webp)



    - RGB 分配**：选择您希望接收或发送的 RGB 资产（如 USDT）。LSP 将确保通道配置支持该资产。


![RGB Allocation](assets/en/14.webp)


5.  **付款**：您必须向 LSP 支付开通通道和提供流动性的费用。您可以使用 **Lightning** 或 **On-chain** Bitcoin 支付。付款可以通过您的内部 KaleidoSwap wallet 或外部 wallet 进行。


![Complete Payment](assets/en/15.webp)


6.确认付款后，LSP 将启动渠道开通交易。您将看到**订单已完成**屏幕。


![Order Completed](assets/en/16.webp)


7.在区块链上确认后，您的通道将处于激活状态，可以进行 RGB 转账。



## 交易：接受者-制造者模式


KaleidoSwap 的交易引擎以**做市商模式**运行。您可以与同行手动交换资产，也可以使用做市商（LSP）。


### 与做市商交换（LSP）


这是最常见的交易方式。您作为**接受者**，根据 LSP（**制造者**）提供的可用流动性执行订单。


1.导航至 "**交易**"选项卡，然后选择 "**做市商**"。

2. **输入金额**：输入要发送的 Bitcoin 金额（或要接收的资产）。界面将显示估计汇率和费用。


![Market Maker Swap](assets/en/17.webp)


3. **确认交换**：查看详细信息，包括汇率和您将收到的确切金额。点击 **确认交换**。


![Confirm Swap](assets/en/18.webp)


4. **处理**：交换在 Lightning Network 上以原子方式执行。您将看到一个状态屏幕，显示交换正在进行中。


![Swap Pending](assets/en/19.webp)


5. **成功**：HTLC 一经结算，交换即告完成，资产进入您的渠道。


![Swap Success](assets/en/20.webp)



## 开发人员 API


对于在 KaleidoSwap 基础上进行开发的开发人员来说，该应用程序提供了一个支持的 API：



- RGB LSPS1**：用于自动清算服务。
- Swap API**：用于程序化交易和做市商。
- WebSocket**：用于实时市场数据订阅。


完整的端点和规格请参阅 [API 文档](https://docs.kaleidoswap.com/api/introduction)。


## 结论


KaleidoSwap 使您能够在 Lightning Network 上利用 RGB 资产的隐私性和可扩展性。通过了解有色UTXO和通道资产分配，您可以充分利用这一强大的去中心化交换协议。