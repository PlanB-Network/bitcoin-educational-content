---
name: Liquid Bootcamp 基础知识
goal: 全面了解 Liquid Network 和 Elements 项目，学习如何在保密交易、令牌化和去中心化网络架构方面实施先进的解决方案。
objectives: 

  - 了解 Liquid 架构的基本原理及其与 Bitcoin 的关系。
  - 学习使用 Elements 软件配置和操作 Liquid 节点。
  - 探索在 Liquid Network 上使用保密交易和资产发行。
  - 掌握 Liquid 在资本市场应用的业务和技术方面。

---

# 引入 Liquid 网络


踏上旨在深入了解 Liquid Network 和 Elements 项目的教育之旅。本训练营将理论与实践相结合，向您传授实施和利用 Liquid 功能所需的技术、架构和业务基础知识。从保密交易到生态系统设计，本课程非常适合希望扩展 Bitcoin 生态系统内高级工具知识的人员。


课程由行业专家主讲，内容包括 Liquid 架构、令牌化应用、Elements 的技术概念以及 Breez SDK 等创新用例。该课程专为初学者和中级用户设计，同时也为希望掌握 Liquid 作为优化项目平台的资深开发人员提供价值。

+++

# 导言


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## 课程概述


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


欢迎参加 Liquid Bootcamp，这是一个全面的培训，旨在让您掌握有效利用 Liquid Network 和 Elements 项目的知识和技能。本课程全面探讨 Liquid 的独特功能，包括 Confidential Transactions、资产发行及其联合网络架构，同时还介绍了 Elements 的基本概念，Elements 是支持 Liquid 的软件。


在整个训练营期间，您将探索 Liquid Network 的实际应用，从设置和操作节点到了解其在 Bitcoin 资本市场和代币化中的应用。通过行业专家的演讲，您还将深入了解 HTLC、Breez SDK 和 Blockstream AMP 项目等高级主题。


本训练营最初是作为现场活动进行的，遵循为现场课程设计的结构化时间表（如图所示）。但是，在这次课程改编中，对内容进行了重新组织，以更好地适应在线形式，并促进学员的理解。新的顺序确保了从基础概念到更高级和技术主题的逻辑递进，从而最大限度地提升了学习体验。


本课程将理论知识与实践经验相结合，以满足不同专业水平学员的需求。本训练营结束时，您将对 Liquid 的架构、与 Bitcoin 的集成以及如何利用其创新功能构建和优化金融解决方案有扎实的了解。


立即潜入 Liquid 侧链的世界，释放其全部潜能！

# 基础知识


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid 结构


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network 架构和共识模式


Liquid Network 是建立在 Elements 代码基础上的联合侧链，旨在扩展 Bitcoin 的功能，同时依赖其基本安全性。与 Bitcoin 的 [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) 不同，Liquid 采用的是联盟[共识](https://planb.academy/resources/glossary/consensus)模式。该网络由分布在全球各地的成员（包括[交易](https://planb.academy/resources/glossary/transaction-tx)所、交易平台和基础设施提供商）共同维护。从这些成员中选出 15 名 "职能人员 "担任[区块](https://planb.academy/resources/glossary/block)签名者。


这些职能人员以确定的循环方式生成区块，每分钟生成一个新区块。这种精确的时间安排与 Bitcoin 的十分钟概率间隔形成鲜明对比。要使一个区块有效，需要 15 个职能部门中至少 11 个部门的签名（三分之二加一的阈值）。这种机制为 Liquid 提供了 "两区块终局性"，这意味着一旦交易得到两次确认（约两分钟），从数学上讲就不可能再重组链条。这种速度和确定性对于套利、自动交易和快速交易所间结算至关重要。


联盟是动态的。通过动态联盟（Dynafed）协议，网络可以在不需要硬 [fork](https://planb.academy/resources/glossary/fork) 的情况下轮换功能部件或更新参数。这样，系统就可以无缝地发展和更换硬件或成员，同时保持持续运行。


### Confidential Transactions 和资产管理


Liquid 的一个显著特点是它原生支持 Confidential Transactions（CT）和多种资产。在 Bitcoin 主链上，所有交易细节--发送方、接收方和金额--都是公开的。在 Liquid 中，CT 使用加密承诺从公共分类账中隐藏资产类型和金额，同时仍允许网络验证交易是否有效（即没有发生[通货膨胀](https://planb.academy/resources/glossary/inflation)）。只有持有保密密钥的参与者才能查看具体数值，从而为转移大量头寸的机构提供必要的商业隐私。


Liquid 将所有资产视为[区块链](https://planb.academy/resources/glossary/blockchain)的 "原生 "公民。这包括 Liquid Bitcoin (LBTC)、稳定币（如 USDT）和安全代币。发行资产不需要复杂的智能合约；这是协议的基本功能。


#### 受监管资产和 AMP

对于安全令牌等需要合规的资产，Liquid 采用了 Blockstream 资产管理平台（AMP）。这引入了一个许可层，交易需要授权服务器的二次签名。这样，发行者就可以在细粒度上执行规则（如白名单或 KYC 要求），将区块链的效率与传统金融的监管控制结合起来。


### 双向 Peg 和安全基础设施


Liquid 和 Bitcoin 之间通过双向挂接保持连接。用户将 Bitcoin 发送到 mainchain 上的一个生成地址，即可实现 "挂钩"。这些资金被锁定 102 次确认（约 17 小时），以消除重组风险。一旦确认，就会在 Liquid 侧链上铸造等量的 LBTC。


挂钩退出 "流程使用户能够用 LBTC 兑换 Bitcoin。这需要燃烧 LBTC 和联盟的加密授权。为防止盗窃，挂钩输出由联盟成员持有的挂钩输出授权密钥（PAK）严格控制。此外，资金可以通过第三方提供商（如 SideSwap）进行即时交换，从而绕过结算延迟，实现更快的流动性。


#### 硬件安全模块（HSM）

严格通过硬件实现安全。职能部门不在标准服务器上保存[私人密钥](https://planb.academy/resources/glossary/private-key)，而是使用硬件安全模块（HSM）。这些设备与主机服务器的逻辑隔绝，并按照严格的规则进行编程。例如，如果一个数据块的高度不大于前一个数据块的高度，HSM 就会拒绝签署该数据块，从而防止历史记录被改写。这种 "对抗性 "安全模式假定主服务器可能被入侵，从而确保即使物理位置被攻破，密钥仍然安全。


## Elements 的基本原理


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements：Liquid 的基础


Elements 是一个开源区块链平台，源自 Bitcoin 核心代码库。它扩展了 Bitcoin 的功能，使独立于侧链的区块链能够在 Bitcoin 之间转移资产。Bitcoin Core 为 Bitcoin 网络提供动力，而 Elements 则是 Liquid Network 和其他定制侧链背后的软件引擎。


两者关系简单明了：Liquid 是 Elements 侧链的一个特定 "实例"，经配置后用于联合共识模型的生产。熟悉 Bitcoin 的开发者会发现 Elements 非常直观，因为它保留了与 RPC 相同的（远程过程调用）接口和命令行结构（`elements-cli`、`elements-d`、`elements-qt`）。关键区别在于配置：设置 `chain=liquidv1` 可将[节点](https://planb.academy/resources/glossary/node)连接到主 Liquid 网络，而 `chain=elementsregtest` 则可启动本地回归测试环境，开发人员可在该环境中即时 generate 块，并在无外部依赖的情况下进行测试。


#### 资产发行

Elements 的一个突出特点是原生资产发行。与代币是复杂智能合约的以太坊不同，Elements 中的资产是通过简单的 RPC 命令（`issueasset`）创建的一等公民。


- 唯一标识符：** 每个资产都有一个 64 个字符的十六进制唯一标识符。
- 再发行代币：** 发行者可以选择创建再发行代币，授予持有者以后铸造更多资产的权利（对稳定币或安全代币有用）。
- 资产注册表：** 由于十六进制 ID 不便于人类阅读，Blockstream 资产注册表将这些 ID 映射为名称和股票代码（如 "USDT"），类似于资产的 DNS。


### 通过 Confidential Transactions 隐私


Elements 解决了公共区块链的主要局限之一：缺乏商业隐私。在 Bitcoin 上，每笔交易金额都是全世界可见的。Elements 引入了**Confidential Transactions (CT)**，通过加密技术对金额和资产类型进行保密，同时仍允许网络验证交易的有效性。


这是通过**佩德森承诺**和**范围证明**实现的。


- Pedersen 承诺**以加密承诺取代可见金额。由于采用了同态加密，验证者可以检查 *输入承诺 = 输出承诺 + 费用*，而无需查看实际值。
- 范围证明** 通过数学方法证明隐藏值是有效范围内的正整数，防止用户凭空创造金钱（如使用负数）。


对于外部观察者来说，保密交易显示的是有效的输入和输出，但模糊了发送的*内容*和*数量*。只有发送方和接收方（拥有保密密钥）才能查看明文数据。


### 开发和 RPC 工作流程


与 Elements 节点的交互主要通过其 JSON-RPC 接口完成。这样，用 Python、JavaScript 或 Go 编写的应用程序就可以与区块链进行通信。



- 设置：** 开发人员通常以 `regtest` 模式启动。这允许即时生成区块（"生成区块"），以立即确认交易，绕过实时网络的 1 分钟区块时间。
- 命令：** `getblockchaininfo` 等标准 Bitcoin 命令以及 `dumpblindingkey` （用于审核 CT）或 `pegin` （用于将 BTC 移入侧链）等 Elements 专用命令。
- 别名：** 为管理多个节点（例如，用于测试的 "发送方 "和 "接收方"），开发人员通常使用 shell 别名，如指向不同数据目录的 `e1-cli` 和 `e2-cli`，在单台机器上模拟[点对点](https://planb.academy/resources/glossary/peertopeer-p2p)网络。


这种架构使开发人员能够利用 Bitcoin 生态系统强大而熟悉的工具构建复杂的金融应用程序，如证券平台或私人支付网关。


## 连接 Bitcoin 层


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### 跨 Layer 基础设施和 HTLC


Bitcoin 生态系统已发展成为一个多层架构，其中主链提供结算，闪电提供速度，而 Liquid 则实现了先进的资产功能。要在这些层级之间实现无中心化中介的价值移动，需要一种无信任的加密基元：Hash 时间锁定 Contract ([HTLC](https://planb.academy/resources/glossary/htlc))。


HTLC 可创建一个有条件的[支付通道](https://planb.academy/resources/glossary/payment-channel)，以原子方式连接独立系统。它通过两个主要约束条件发挥作用：**[哈希](https://planb.academy/resources/glossary/hash-function)锁**和**时间锁**。


- Hash 锁：** 如果接收者透露了与特定加密哈希值相匹配的秘密 "预图像"，就可以立即使用资金。
- 时间锁定：** 如果接收方未能在设定的时间范围（区块高度）内揭示秘密，原发送方可以收回资金。


这种双路径结构确保了安全性。在跨层交换中，两个网络使用相同的哈希锁。当接收方在一个层（如 Liquid）上泄露秘密索取资金时，发送方也能看到该秘密，然后发送方可以在另一个层（如 Lightning）上使用该秘密索取对等资金。这种加密绑定保证了交换要么对双方都成功完成，要么对双方都失败，从而消除了一方损失资金而另一方获得资金的风险。


### Taproot 和 MuSig2 升级


传统 HTLC（[SegWit](https://planb.academy/resources/glossary/segwit) v0）功能良好，但存在隐私和效率方面的缺陷。它们需要发布整个[脚本](https://planb.academy/resources/glossary/script)逻辑 on-chain，使得区块链分析师很容易识别掉期交易，并且由于数据量大而成本较高。[Taproot](https://planb.academy/resources/glossary/taproot)（SegWit v1）和 MuSig2 协议的推出彻底改变了这一架构。


Taproot 允许通过 MuSig2 进行**密钥聚合**。MuSig2 可让交换参与者将他们的密钥合并成一个单一的聚合[公钥](https://planb.academy/resources/glossary/public-key)，而不是披露一个包含多个公钥的复杂脚本。


- 合作 "密钥路径"：** 如果双方同意交换（"快乐路径"），则共同签署交易。在网络看来，这与标准的单笔签名支付完全相同。它占用的区块空间极小，而且完全不会泄露任何关于交换条件的信息。
- 对抗性 "脚本路径"：** 如果一方变得反应迟钝或怀有恶意，底层脚本（包含哈希值/时间锁）才会被披露。这是以[梅克尔树](https://planb.academy/resources/glossary/merkle-tree)的形式组织的，允许诚实的一方只公开收回资金所需的特定分支，而隐藏合同逻辑的其他部分。


### 实际执行：Liquid-Lightning 交换


在实践中，这些协议实现了 Bitcoin 各层之间的无缝交换。典型的 Liquid 到 Lightning 的交换始于客户向服务提供商提出交换请求。客户提供一张 [Lightning 发票](https://planb.academy/resources/glossary/invoice-lightning)，服务提供商将等价的 Liquid Bitcoin（L-BTC）锁定到启用了 Taproot 的 HTLC 地址中。


原子性在付款结算时执行。服务提供商必须拥有预图像，才能申请 L-BTC 。只有在成功支付客户的 Lightning 账单时，服务提供商才能获得预图像。闪电支付完成后，前置图像就会显示出来，服务提供商就可以解锁 Liquid 资金。


#### Wallet 摘要和 UTXO 管理

对于最终用户来说，这种复杂性完全被抽象化了。Aqua 等现代[钱包](https://planb.academy/resources/glossary/wallet)在后台处理密钥生成、发票创建和签名过程。用户只需使用 Liquid 余额 "支付 "闪电发票即可。在幕后，服务管理 [UTXO](https://planb.academy/resources/glossary/utxo) 整合，定期清理小额、无人认领或退款的输出，以保持 wallet 的效率，并在高流量期间将费用影响降至最低。


## Liquid Network 概览


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network 架构与共识


Liquid Network是建立在**Elements**代码库基础上的联盟侧链。Elements是Bitcoin核心的fork，提供软件基础，而Liquid则是生产网络的实现。与依赖于竞争性 [mining](https://planb.academy/resources/glossary/mining) 的 Bitcoin 的 Proof-of-Work 不同，Liquid 采用的是**联邦共识**模式。


该网络由分布在全球各地的 15 个 "职能实体 "负责维护。这些实体运行着专门的服务器，发挥着两个关键作用：

1.  **区块生产：** 职能人员按照确定的循环时间表轮流创建区块，每分钟生成一个新区块。

2.  **区块签名：** 要使一个区块有效，它必须由 15 个职能部门中的至少 11 个签署。


这种 11-15 的阈值可确保网络能够承受多达四个节点的故障而不会停止。这种权衡的主要优势在于**确定的最终性**。Bitcoin 处理的是概率问题，而 Liquid 则在两个区块（约两分钟）后实现结算确定性。一旦一个区块上有一个确认，链就无法重组，这使得它在套利和快速结算方面非常有效。


### Confidential Transactions 和本土资产


Liquid 的最大特点是默认使用 **Confidential Transactions (CT)**。在 Bitcoin mainchain 中，发送方、接收方和金额都是公开的。Liquid 对此进行了改进，通过加密技术屏蔽了金额和资产类型，同时保留了发送方和接收方的地址，以便核实。


为确保用户无法印钞（如发送负数），Liquid 采用了 **Pedersen Commitments** 和 **Range Proofs**。这些加密原语允许网络验证*输入=输出+费用*以及所有数值均为正整数，而不会向公共分类账透露具体数字。只有持有保密密钥的参与者才能查看解密后的数据。


#### 资产发行

Liquid 将所有资产都视为 "原生资产"。无论是 Liquid Bitcoin（L-BTC）、USDT 等稳定币，还是证券 token，它们都具有相同的架构。发行资产不需要智能合约，只需要简单的 RPC 调用。


- 不受监管的资产：** 任何人都可以擅自发行。
- 受监管资产：** 利用 Blockstream 资产管理平台 (AMP)，发行商可以通过要求授权服务器在资产移动前进行二次签名，从而执行合规规则（如 KYC/AML）。


### 双向挂钩和动态联合会


Bitcoin 和 Liquid 之间的桥梁是**双向 Peg**。它允许用户将 BTC 移入侧链（Peg-in）并返回 mainchain（Peg-out）。


**eg-in 过程：**

这是无须许可的。用户向联邦控制的地址发送 BTC。为防止 Bitcoin 区块链重组，这些资金必须等待**102 次确认**（约 17 个小时）后，才能在侧链上铸造等价的 L-BTC。


**eg-out 过程：**

要返回 Bitcoin，就需要烧掉 L-BTC。然而，为防止基础 Bitcoin 储备被盗，挂钩退出并非完全自动化。它们需要持有**挂钩退出授权密钥（PAK）**的成员授权。Bitcoin 资金本身由 11-15 个多重签名的 wallet 保证安全，密钥保存在硬件安全模块（HSM）中，与功能主治服务器隔绝。


**Dynamic Federation (Dynafed):**

为确保使用寿命，Liquid 采用了 Dynafed 协议，该协议允许网络在没有硬性 fork 的情况下轮换职能人员或更新参数。如果需要更换职能人员，网络会广播一个过渡事务。经过两周的重叠期后，新的配置就会接替，从而使联盟能够无缝发展，同时保持持续的正常运行时间。


## 生态系统和资本市场


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network：商业战略和生态系统


Liquid 不仅仅是一个技术侧链，它还是一个以业务为中心的基础设施层，旨在处理 Bitcoin mainchain 无法有效支持的资本市场的复杂需求。[Lightning Network](https://planb.academy/resources/glossary/lightning-network) 针对高频率、低价值支付进行了优化，而 Liquid 则以高价值转账、资产发行和交易所间结算为目标。


该生态系统由**Liquid 联合会**推动，该联合会由约 73 家公司组成，包括交易所、交易平台和基础设施提供商。这种合作模式与传统的金融清算所类似，但运作透明度更高，结算时间大大缩短（2 分钟对 T+2 天）。


### 真实世界资产（RWA）的代币化


Liquid 的核心商业案例是 "代币化"--将现实世界的价值（股票、债券、mining 合同）表示为区块链上的数字代币。这提供了三个主要优势：

1.  **全天候全球市场：** 取消银行营业时间和地域限制。

2.  **运行效率：** 通过共享、不可变的分类账消除对账错误。

3.  **原子结算：** 通过确保交付与付款同步进行，降低交易对手风险。


#### 受监管资产和 AMP

由于法律规定，大多数机构资产不能进行无权限交易。资产管理平台（AMP）** 是执行这些规则的技术标准。


- 白名单：** 发行人可限制 KYC 验证过的地址持有和交易。
- Multisig 控制：** 合规行动（如冻结被盗资金或补发丢失的令牌）通过多重签名授权进行管理，确保任何一名员工都不能单方面采取行动。


这种基础设施如今已投入使用。像**Stalker**这样的平台在欧洲提供端到端的代币化服务，而**Sideswap**则充当去中心化交易所和非托管wallet，实现资产的点对点交易，如**区块流Mining票据（BMN）**和代币化的微策略股票（CMSTR）。


### 现实世界的成功：梅菲尔案例研究


墨西哥的**Mayfell**公司最有力地证明了 Liquid 的实用性。在这个市场上，传统的融资方式依赖于纸质期票--这种票据容易丢失、欺诈和处理缓慢--Mayfell 将整个基础设施转移到了 Liquid 上。



- 规模：** 发行了 25 000 多张期票，价值超过**15 亿美元。
- 隐私：** 使用 Liquid 的 Confidential Transactions，贷款金额只有出借人和借款人可见，既保护了商业隐私，又允许审计人员验证分类账的完整性。
- 影响：** 通过区块链将非银行贷款机构与全球资本市场连接起来，梅菲尔降低了成本，扩大了墨西哥中小型企业获得信贷的机会，证明了 Liquid 的价值主张远远超出了投机交易的范畴。


### 与其他连锁店相比的战略定位


Liquid 与众多代币化平台（以太坊、Solana 等）展开竞争，但它具有明显的战略优势：


- 监管明确性：** Liquid 使用 Bitcoin （L-BTC）作为其原生资产。它没有预先开采的 token 或 ICO，避免了困扰其他 L1 区块链的 "未注册证券 "风险。
- 稳定性：** 不同于以太坊的账户模型，交易失败仍会烧掉气体费用，Liquid 的 UTXO 模型是确定性的，对关键任务财务数据而言是可靠的。
- 隐私性：** 默认保密性是大多数金融机构的要求，Liquid 原生提供了这一功能，而公有链在没有复杂附加组件的情况下很难实现这一功能。


对于开发者来说，这个生态系统提供了一个明显的机会：构建工具（仪表盘、钱包、合规集成），将传统金融与 Bitcoin 的安全结算层连接起来。


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP：Liquid 上的许可资产控制


Blockstream AMP（资产管理平台）是 Liquid Network 上的关键基础设施层，专为受监管的数字证券和稳定币发行商而设计。虽然 Liquid 提供了一个具有原生资产发行功能的无权限基础层，但受监管实体往往需要严格的监督和合规能力。AMP 在不牺牲 Liquid 的 Confidential Transactions 隐私优势的前提下，通过引入特定资产的许可控制层，弥补了这一差距。


该平台的核心价值主张基于两项主要功能：全面的发行人可见性和交易授权。与标准 Liquid 资产不同，AMP 资产允许发行人保持完全的 unblinded 审计跟踪。这种透明度对于监管报告和内部审计至关重要。此外，AMP 通过联署机制执行严格的授权模式。AMP 资产的每次转移都需要 AMP 服务器的签名。这使得发行人可以执行复杂的 off-chain 规则，例如冻结账户、将经认可的投资者列入白名单或施加转账限制，从而有效地充当分散网络中的集中式看门人。


#### 业务权衡

这种架构引入了特定的权衡。该系统依赖于 AMP 服务器的可用性；如果服务器充当联合签名人并脱机，资产流动性就会暂停。此外，在维护用户间隐私的同时，投资者必须接受发行人对其持有资产的完全可见性。这种模式非常适合合规的安全代币，但不适合抗审查的[加密货币](https://planb.academy/resources/glossary/cryptocurrency)。


### 架构演变与集成路径


目前，AMP 生态系统正在从第一阶段向更加灵活、可互操作的 "第二版 "架构过渡。传统系统要求发行商维护完全同步的 Elements 节点，并迫使开发人员严重依赖单一的 Green SDK。虽然功能强大，但这造成了很高的技术门槛，限制了 wallet 的选择。


下一代架构将复杂性转移到服务器上，从根本上简化了这些要求。在这种新模式中，AMP 服务器负责处理交易构建、UTXO 选择和费用计算等繁重工作。它向发行方提供只需签名的部分签名 Elements 交易（PSET）。这种 "智能服务器、傻瓜 wallet "方法使发行商无需运行全节点，并可使用硬件钱包和标准多签名设置进行资金管理。


对于开发人员来说，这种演变意味着从专有 SDK 转向标准描述符和 PSET 工作流程。钱包现在可以向 AMP 服务器注册多重签名描述符，以建立授权权限。这使 AMP 开发与更广泛的 Bitcoin wallet 标准保持一致，使任何能够处理 PSBT/PSET 格式的应用程序都能进行集成。我们鼓励开发人员使用 Liquid Wallet 工具包 (LWK) 等工具，这些工具支持这些基于描述符的现代架构，确保他们的应用程序能够适应新的 AMP 标准。


### Liquid Wallet 生态系统和保密性


由于原生资产和 Confidential Transactions 等特性，在 Liquid 上构建应用程序需要浏览比标准 Bitcoin 开发更复杂的堆栈。该生态系统由分层架构提供支持：secp256k1-zkp 等低级库处理加密基元，而高级工具包则管理 wallet 逻辑。


历史上，Green 开发工具包（GDK）提供了一个全面但僵化的解决方案。现代的替代方案是 Liquid Wallet 工具包（LWK），它提供了一种模块化方法。LWK 将关注点分离成不同的板块，独立处理描述符、签名和硬件通信，让开发人员可以灵活地构建定制解决方案，而无需承担单体库的开销。


#### 处理 Confidential Transactions

在这个生态系统中，最明显的挑战是管理盲法生命周期。在 Liquid 中，交易输出使用椭圆曲线衍射-赫尔曼（ECDH）密钥交换进行加密。发送方使用接收方的加密公钥对资产数量和类型进行加密，生成范围证明，在不泄露价值的情况下验证交易的有效性。


wallet 要发挥作用，必须成功逆转这一过程。当 wallet 检测到输入的交易时，它会尝试使用其私人保密密钥解除对输出的保密。如果共享密钥匹配，wallet 就能解密该值，并将其添加到用户的余额中。这个过程是计算密集型的，需要精确管理致盲因子，以确保交易在数学上是平衡的，而 LWK 等工具旨在为开发者抽象出这一复杂性。


# 技术


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - 无节点


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Breez Liquid SDK 简介


Breez Liquid SDK 是一个自我托管的开源工具包，旨在弥合 Liquid Network 与更广泛的 Bitcoin 生态系统之间的差距。它的主要任务是抽象 Lightning Network 节点管理和原子交换的复杂性，使开发人员能够构建无摩擦的金融应用。


它采用 "移动优先 "理念构建，核心逻辑采用 Rust 编写，以确保性能和安全性，但它利用 UniFFI（统一外来函数 Interface）为 Kotlin、Swift、Python、C#、Dart 和 Flutter 提供本地绑定。这确保了开发人员可以将 Bitcoin 功能集成到他们喜欢的环境中，而无需管理低级加密操作。


**支持的交易类型：**

SDK 以 Liquid 为 "大本营"。它擅长三种特定操作：

1.  **Liquid 至 Liquid：** 直接 on-chain 转移。

2.  **Liquid 到 Lightning：** 使用 Liquid 资金支付 Lightning 发票。

3.  **Liquid 到 Bitcoin：** 直接将资金交换到 Bitcoin mainchain。


*注意：SDK 不支持 Lightning-to-Lightning 或 Bitcoin-to-Bitcoin 直接交易。它完全是以 Liquid 为中心的工具。


### 支付架构：海底掉期


为实现 Liquid、"闪电 "和 Bitcoin 之间的互操作性，Breez 无需中央托管机构，而是依靠**潜艇交换**。这是一种原子操作，交易要么在两个网络上成功完成，要么在两个网络上失败，确保资金在传输过程中不会丢失。


#### 闪电发送（潜艇交换）

当用户支付闪电发票时，SDK 会在 Liquid Network 上广播一个 "锁定 "交易。这实际上是将资金托管起来。交换提供商（Boltz）会检测到这一情况，支付闪电发票，然后使用支付预图像（加密收据）索要锁定的 Liquid 资金。


#### 闪电接收（反向潜艇交换）

接收 "闪电 "是一个相反的过程。用户生成发票，交换提供商将资金锁定在 Lightning Network 上。SDK 通过 WebSockets 监控这一过程。一旦锁定得到确认，SDK 就会自动执行索偿交易，将等值资金转入用户的 Liquid wallet。


#### 跨链 Bitcoin

对于 Liquid 到 Bitcoin 的传输，架构采用 "双交换 "机制。锁定交易在两条链上同时进行。发送方在 Bitcoin 上申请资金，而接收方在 Liquid 上申请资金。这就实现了无信任桥接，而无需依赖 federated peg 输出或集中交换。


### 开发人员 Interface 和自动化管理


Breez SDK 将复杂的财务流程浓缩为标准化的三步流程，从而简化了开发人员的体验： **连接、准备和执行**。


1.  **连接：** 初始化 wallet，使用 Liquid Wallet 工具包（LWK）与区块链同步，并为实时监控建立 WebSocket 连接。

2.  **准备：** 在投入资金之前，该步骤会计算并返回所有相关的网络费用和掉期成本，使用户界面能够向用户提供清晰的总额。

3.  **执行：** 这一步构建事务、广播事务并启动交换。


#### 自动安全机制

SDK 最关键的功能之一是**自动退款管理**。在网络故障或交易对手不合作的情况下，资金理论上可能会被卡在时间锁定的合约中。SDK 完全抽象了恢复逻辑。它监控每笔掉期的状态；如果掉期失败或超时，SDK 会自动构建并广播退款交易，将资金返还到用户的 wallet 中。


此外，SDK 还处理**元数据解析**。它将 off-chain 交换数据（由 Boltz 交换器提供）与 on-chain 交易历史记录合并。这可确保用户的交易历史记录是人类可读的，能显示发票详情和付款背景，而不仅仅是原始的十六进制交易哈希值。


# 最后部分


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## 评论与评级


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## 期末考试


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## 结论


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>