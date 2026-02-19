---
name: Blitz Wallet
description: 最简单的比特币钱包。
---

![cover](assets/cover.webp)

用户体验是选择比特币钱包时的关键因素之一。在本教程中，我们将向您介绍 Blitz Wallet——一款以简洁为核心理念的钱包：得益于 **Spark** 协议的集成，Blitz 为您提供了市场上最简单、最全面的比特币钱包之一，支持即时支付且无需任何技术管理。

## 什么是 Blitz Wallet？

Blitz Wallet 是一款 **self-custodial** 且 **open source** 的比特币钱包，专注于您的主权掌控以及流畅直观的用户体验。

[Blitz Wallet](https://blitz-wallet.com/) 是一款移动应用，可在 Android（Play Store）和 iOS（App Store）上下载。

与需要管理支付通道和入站流动性的传统 Lightning 钱包不同，Blitz Wallet 依托 **Spark 协议**来消除这些技术复杂性。结果是：从收到第一个聪开始即可即时支付，无需任何预先配置。Blitz 的目标是让比特币支付像普通支付应用一样简单，同时绝不牺牲您对资金的 self-custody。

Blitz Wallet 还支持格式为 `用户名@域名.com` 的**可读地址**（通过 LNURL），让发送比特币像发邮件一样简单，无需每次交易都处理冗长的 invoice 或 QR code。

## 理解 Spark 协议

在进入实操之前，了解 Blitz Wallet 底层运行的技术是很有帮助的：**Spark 协议**。

### 什么是 Spark？

Spark 是一个构建在比特币之上的 open source 二层协议，由 Lightspark 团队开发。它能够实现即时且低成本的交易，同时保持您对比特币的 self-custody。

与依赖两方之间**支付通道**的 Lightning Network 不同，Spark 使用了一种名为 **statechain**（状态链）的技术。其基本原理如下：Spark 不是在每次交易时在区块链上移动比特币，而是将一个用户的**支出权**转移给另一个用户，无需 on-chain 操作。

### 它是如何运作的？

为了直观地理解 Spark，我们可以想象在 Spark 上花费比特币需要完成一个由两块拼图组成的拼图：
- 一块由用户持有（例如 Alice）。
- 另一块由一组被称为 **Spark Entity (SE)** 的运营商持有。

只有两块相匹配的拼图组合在一起，才能花费比特币。

当 Alice 想将比特币发送给 Bob 时，会发生以下情况：Bob 和 SE 之间共同创建一个新的拼图。拼图保持相同的形状，但组成它的拼图块发生了变化。现在是 Bob 的拼图块与 SE 的拼图块相匹配。Alice 的旧拼图块变得不可用，因为 SE 已经销毁了与之对应的拼图块。比特币的所有权已经易手，**且没有在区块链上发生任何交易**。

Bob 随后可以重复相同的过程将这些比特币发送给 Carol，以此类推。每次转账都是通过替换拼图块来完成的，而非通过 on-chain 资金转移。

### 为什么是安全的？

一个合理的问题是：如果 SE 没有真正销毁其旧拼图块会怎样？

Spark Entity 不是一个单一实体：它是一组独立的运营商。SE 的拼图块从不由单个运营商持有。拼图的替换需要多个运营商的协作。在一次转账中，只要有**一个运营商是诚实的**，就足以阻止旧拼图被重新激活。没有任何单个运营商能够秘密地保留一个旧的活跃拼图或在事后重新创建它。

此外，Spark 集成了单方面退出机制：您始终可以在不需要 SE 协作的情况下将比特币取回 on-chain。这一备用机制是 Spark 架构的核心组成部分，确保您永远不会依赖网络来访问您的资金。

### Spark 与 Lightning Network 的对比

Spark 和 Lightning 并非竞争关系：它们是**互补的**。Blitz Wallet 集成了两者，让您能够享受各自的优势。

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **技术**                      | Statechains（状态链）         | 支付通道              |
| **通道管理**                  | 不需要                        | 需要                  |
| **入站流动性**                | 不需要                        | 需要                  |
| **即时交易**                  | 是                            | 是                    |
| **Self-custody**              | 是                            | 是                    |
| **Lightning 兼容性**          | 是（通过 atomic swaps）       | 原生                  |

Lightning Network 仍然是即时支付的优秀协议，但它带来了技术限制（通道管理、入站流动性、节点需在线等），这可能会让新手望而却步。Spark 消除了这些限制，同时仍然与 Lightning 兼容。

## 安装与配置

在本教程中，我们以 Blitz Wallet 的 Android 版本为基础，但以下所有流程同样适用于 iOS。

![installation](assets/fr/01.webp)

由于 Blitz Wallet 是 self-custody 钱包，您可以选择**创建新钱包**或**导入恢复助记词**（12 或 24 个单词）来恢复已有钱包。

在这里，我们选择创建新钱包。以下是我们关于备份恢复助记词的建议：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **重要提示**：这 12 或 24 个恢复词是**访问您比特币的唯一密钥**。Blitz 是 self-custodial 钱包：Blitz 和 Spark 都无法访问您的恢复助记词或资金。如果您丢失了这些词，您将永久失去对比特币的访问权。不要与任何人分享：任何拥有这些词的人都可以花费您的比特币。

然后创建一个 **PIN 码**来保护钱包的访问安全。

![setup-wallet](assets/fr/02.webp)

## 开始使用 Blitz

使用 Blitz 进行交易比大多数其他比特币钱包更加直观。界面极简，围绕三个主要操作：发送、扫描和接收。

### 接收比特币

要在您的 Blitz 钱包上接收比特币，请点击**"向下箭头"**图标（↓），输入您希望接收的聪数金额，添加可选描述，钱包将生成一张账单（invoice），您可以分享给付款人。

⚠️ **注意**：聪（satoshi，简称"sat"）是比特币的最小单位：**1 比特币 = 100,000,000 聪**。

Blitz Wallet 的特色之一是它支持比特币生态系统中的多个网络和协议：

- **Lightning Network**：比特币的二层网络之一，能够以极低的手续费即时完成小额支付。非常适合日常小额消费。

- **Bitcoin (on-chain)**：比特币协议的主链，适用于金额较大、需要最高安全性和最终确认性的交易。

- **Liquid Network**：由 Blockstream 开发的比特币 sidechain（侧链），可使用 Liquid Bitcoin (L-BTC) 进行快速且保密的交易。

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

默认情况下，Blitz 会生成一张 Lightning 账单，但您可以通过点击 **"Choose format"**（选择格式）按钮来选择希望在哪个网络上接收聪。

![receive-sats](assets/fr/03.webp)

### 创建联系人

Blitz Wallet 通过联系人系统简化了比特币的定期发送。

在**联系人**菜单中，您可以保存经常交互的 Blitz 用户名或 Lightning 地址（LNURL）。

这样，您只需几次点击即可向这些地址发送聪，无需每次都扫描 QR code 或手动输入地址。

### 发送比特币

除了经典的比特币发送方式（扫描 QR code、手动输入地址），Blitz 还提供了几种便捷选项：

- **从图片发送**（*From Image*）：从相册导入 QR code。
- **从剪贴板发送**（*From Clipboard*）：粘贴之前复制的地址或账单。
- **手动输入**（*Manual Input*）：直接输入比特币地址、Lightning invoice 或可读地址（例如 `用户名@walletofsatoshi.com`）。
- **从联系人发送**：选择一个预先保存的收款人，几次点击即可发送。

在 **Wallet** 菜单中，点击**"向上箭头"**按钮（↑），选择发送方式，输入发送金额，添加描述并确认交易。

当前最低发送金额为 **1,000 聪**。

![send-bitcoin](assets/fr/05.webp)

## Blitz 商店

除了比特币转账操作，Blitz Wallet 还集成了一个商店，您可以在其中使用比特币直接在应用内购买数字服务。

从主菜单中，点击 **Store** 选项卡进入商店。在这里您还可以访问 **Bitrefill** 平台，直接用比特币从全球数千家商户购买礼品卡。

- **人工智能**：访问最新的生成式 AI 模型（Claude 3.5 Sonnet、GPT-4o、GPT-4o-mini、Gemini Flash 1.5），直接用聪支付积分。根据您的需求提供多种套餐（Casual、Pro、Power）。

![ia-credits](assets/fr/06.webp)

- **匿名短信**：在全球范围内发送和接收短信，无需透露您的个人手机号码。每条发送的消息以聪计费。

![sms-credit](assets/fr/07.webp)

- **WireGuard VPN**：通过订阅 WireGuard VPN（按周、按月或按季度）来保护您的在线隐私，可直接在 Blitz 商店中用比特币支付。您只需在设备上下载 WireGuard 客户端应用即可使用。

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet 的幕后：深入了解

在 Blitz Wallet 简洁易用的背后，隐藏着一个精心设计的技术架构，结合了比特币生态系统的多个层级。

### 余额分配

Blitz Wallet 以透明的方式管理您的余额，根据需求将资金分配到不同的协议上。当您的余额低于 500,000 聪时，Blitz 使用 **Liquid Network** 和 atomic swaps（原子交换）来为您提供流畅的体验，即使是小额也能在 Lightning Network 上进行交易。

这种方式确保新用户无需了解底层机制即可轻松上手。您可以在**设置 > Balance Info** 菜单中查看余额在各层级之间的分配情况。

![balance](assets/fr/09.webp)

### Lightning 模式（可选）

默认情况下，Blitz Wallet 使用 Liquid Network 和 Spark 协议为您提供无需技术配置的流畅体验。不过，Blitz 允许您激活 **Lightning 模式**，当余额达到 **500,000 聪**（0.005 BTC）时将自动开启一个支付通道。

要激活 Lightning 模式，请进入**设置**，然后在**技术设置**部分，点击 **Node Info** 选项。

![enable-lightning](assets/fr/10.webp)

得益于 Spark 协议，此激活是**可选的**：Spark 已经能够进行兼容 Lightning 的支付，无需开启通道或管理入站流动性。原生 Lightning 模式对于希望在应用内拥有自己的 Lightning 节点的高级用户仍然有用。

### 销售终端（PoS）

Blitz Wallet 集成了**销售终端**功能，允许商户直接通过应用接受比特币支付。

在**设置 > Point-of-sale** 菜单中，您可以配置：

- 您商店的唯一标识
- 用于显示价格的当地法定货币
- 给员工的操作说明
- 客户的小费选项

您的客户只需扫描生成的 QR code 即可即时完成比特币支付。

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

编写本教程时使用的资源：
- [Breez](https://breez.technology/) Technology 博客：[*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0)。
