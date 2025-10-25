---
name: Mempool
description: 探索整个 Bitcoin 生态系统。
---

![cover](assets/cover.webp)



Bitcoin 协议是一个开放咨询的匿名分散网络。成员（节点），即拥有 Bitcoin 软件实例的计算机，可以不受限制地访问 Bitcoin 上发布的所有数据。然而，在 Bitcoin 的早期，该协议并不像今天这样可以被广泛使用。


在使用 Bitcoin 的早期，必须运行一个 Bitcoin 节点，才能使用适当的工具（bitcoin-cli）通过命令行查询网络。



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

因此，Bitcoin 社区启动了一些项目，以扩大 Bitcoin 社区，让没有节点和/或不具备所需技术技能的人也能更方便地使用 Bitcoin。



在本教程中，我们将了解**Mempool.space**项目、其功能及其对 Bitcoin 生态系统的影响。



## 什么是 Mempool.space？



**Mempool.space**是一个开源资源管理器，提供有关各种Bitcoin协议网络的交易、交易费用、区块和矿工的有用信息。它于 2020 年推出，通过具有代表性的图形、流畅的动画和简洁的界面大大改善了用户体验。



为了理解该项目，Mempool（内存池）是一个虚拟空间，Bitcoin 网络上所有等待确认的交易都存储在其中。Mempool 就像一个 "候机室"，Bitcoin 交易在这里等待确认。网络上的每台计算机（节点）都有自己的等候室，这就解释了为什么并非所有人都能同时看到所有交易。



该平台对 Bitcoin 生态系统的主要影响在于，它允许您访问 Bitcoin 上大多数节点内存区域中的各种信息，而无需运行一个节点。Mempool.space 是一个用于查看和搜索 Bitcoin 协议网络的存储库。



由于 Mempool.space 在生态系统中的使用越来越广泛，而且它是开源的，因此它被集成到越来越多的个人主机系统中。现在，您可以直接在个人节点上拥有自己的 Mempool.space 实例。请参阅我们在 Umbrel 节点上配置 Mempool.space 的教程。



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Mempool.space 的基础知识



如上所述，[Mempool.space](https://Mempool.space) 是一个 Bitcoin 协议浏览器，可让您通过图形化的 Interface 实时监控您的交易及其在所选 Bitcoin 网络上的传播。



Mempool.space 支持许多 Bitcoin 协议网络。


在菜单栏中，您可以找到以下网络：




- **Mainnet** ：主要的 Bitcoin 网络，在此进行真正的 Bitcoin 交易。
- **Signet**：使用数字签名验证区块的测试网络，无需主网络所需的资源。
- Testnet 3：基于 Bitcoin 协议的无风险测试和开发网络。
- **Testnet 4**：Testnet 3 的新版本为测试环境带来了更高的稳定性和新的共识规则。



![reseaux](assets/fr/01.webp)



在首页左侧的 Green 中，您将看到未来可能出现的区块（交易组），这些区块已准备好接受验证并整合（挖掘）到 Bitcoin 网络中。平均每十分钟就有一个区块被挖掘出来：请保留这些信息，因为它们在我们以后的开发过程中会派上用场。


在右侧的紫色区域，您可以看到最近在 Bitcoin 上挖掘出的区块，最后挖掘出的区块的编号代表当前网络的高度。



![blocs](assets/fr/02.webp)



交易费用**部分**是一个交易费用估算器。分配给您的交易的费用越高，您的交易就越有可能被添加到下一个准备开采的区块中。


交易费代表 Miner 将您的交易插入 Mining 候选区块的成本。它由 sat/vB（Satoshi/虚拟字节）的比率定义，代表您为您的交易在候选区块中占用的空间所支付的 satoshis 数量。



⚠️ 重要提示：在 Mempool 饱和的情况下，矿工会优先处理提供最佳 Satoshi/vByte 比率的交易。您的交易越重（越大），就越需要更多的 Satoshis 才能快速加入。



![fees-visualizer](assets/fr/03.webp)



通过 **Mempool 护目镜** 部分，您可以直观地看到交易占用的空间。



![mempool](assets/fr/04.webp)



由于矿工必须提供 Proof of Work 以将其候选区块添加到已开采区块链中，因此大约每十分钟开采一个区块。这种难度每**2016个区块**，相当于约**2周**。您可以在此查看这一难度的演变。



![difficulty](assets/fr/05.webp)



在主链上添加一个新区块后，验证区块的 Miner 有权获得由固定部分（每 21 万个区块**减半，相当于减半期间约 4 年**）和交易费组成的奖励。



![halving](assets/fr/06.webp)



## 访问您的交易详情



在 Mempool.space 搜索栏中，您可以输入您的 Bitcoin Address 或您的 transaction ID，以查找更多有关您的历史记录。



![search](assets/fr/07.webp)



在交易详情页面，您可以找到有关交易的一般信息：




- **状态**：添加到区块时已确认，在 Mempool 中等待时未确认。
- 交易费。
- **预计到达时间 (ETA)**：您的交易加入区块所需的大致时间。它根据与该交易相关的费用比率计算得出。



![general-txinfo](assets/fr/08.webp)



流程**部分**显示交易组件的图表。



输入（之前的 UTXO），用于您的交易，输出则给予收款人使用每个输出中的比特币的权利，只需出示其支出所需的签名即可。



![flow](assets/fr/09.webp)



有关所用地址的更多详情，请参阅**输入和输出**部分。



![address](assets/fr/10.webp)



了解不同的 Bitcoin 交易方案，提高您的保密性。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 加快交易速度



在 Bitcoin 生态系统中，矿工对交易的验证与该交易的相关交易费用有着内在联系。矿工优先考虑费用比率（satoshis/vBytes）较高的交易，如果您不支付矿工接受的合理费用，就会影响您交易的有效性。您的交易将被卡在 Mempool 中，等待接受其费用比率的区块。



幸运的是，Bitcoin 网络上有两种方法可以加快交易确认。





- **RBF** - 按费用替换：这种方法允许您使用与低费用交易相同的条目，但这次是通过增加交易费用来加快验证。您的新交易将更快通过验证，并被纳入一个区块，使低费交易失效。



您可以使用接受该机制的投资组合执行费用替换操作。例如，请参阅我们有关 Blue Wallet 投资组合的文章。



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent：受 RBF 启发的一种方法，但在接收方。当您作为接收方的交易在 Mempool 中被阻止时，尽管该交易尚未被确认，但您可以选择花费该交易的产出（UTXOs），方法是为新交易分配更多费用，从而使您作为接收方的交易和发起的交易的平均费用鼓励矿工将这两个交易都包含在一个区块中。



⚠️ 第一笔交易必须包含在一个区块中，以便确认第二笔交易。



如果所有这些术语看起来太专业，我建议您 [查阅我们的术语表](https://planb.network/resources/glossary)，其中包含与 Bitcoin 及其生态系统有关的所有技术术语的定义。



除了这些方法外，Mempool.space 还与 Bitcoin 网络中超过 80% 的矿工建立了联系，通过向 Exchange 中的矿工支付对价，将您的低成本交易插入下一个准备开采的区块中，从而加速您的任何**未确认**交易，甚至是那些未激活 RBF 的交易。



在交易详情页面，点击 **Accelerate** 按钮，然后继续向矿工支付交易对价。



![accelerate-section](assets/fr/11.webp)


## 未成年人



Miner 指管理矿场的人，即参与 Mining 进程的计算机，该进程包括参与 Proof-of-Work。Miner 将其 Mempool 中的待处理交易分组，形成一个候选区块。然后，它通过修改各种非ces，为该数据块的标头寻找一个小于或等于目标值的有效 Hash。如果他找到了有效的 Hash，他就会向 Bitcoin 网络广播他的区块，并将相关的金钱奖励（由区块补贴（无中生有的新比特币）和交易费组成）收入囊中。



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗矿工就像 "验证员"，负责验证交易并将其归类到区块中。要向 Bitcoin 网络添加一个新区块，他们必须解决一个复杂的数学难题（Proof-of-Work）。第一个解开谜题的 Miner 将赢得 Bitcoin 奖励（区块赠款+区块中包含的交易费用）。



通过监测 Proof of Work 的难度，您可以直观地看到矿工所需计算能力的变化。您将在下面的章节中看到 ：





- 估算矿工在上一次难度调整中获得的总回报，以及估算每 21 万个区块（约 04 年）一次的下一次 Halving 区块分配。



![rewards](assets/fr/12.webp)



该难度每 2016 个区块（约两周）调整一次。它与矿工每 2016 个区块 Miner 所需的平均时间成反比。


当矿工平均耗时少于 10 分钟时，难度增加，证明矿工验证 Miner 区块更容易。相反，当平均用时超过 10 分钟时，难度就会降低。



![mining-pool](assets/fr/13.webp)





- 矿工小组：考虑到所涉及的难度，一组矿工在我们称之为 "**池**"的 Bitcoin 上合作帮助寻找 Proof of Work。当一组矿工挖出一个区块时，所获得的奖励将根据每个 Miner 部分解搜索的成功率（即在搜索 Proof-of-Work 时所贡献的算力）进行分配，或者根据合作商定的报酬方式进行分配。





![mining](assets/fr/14.webp)



## Lightning Network 基础设施



Mempool 不仅提供有关 Bitcoin 网络基础设施（主链）的信息。它还为 Bitcoin 的闪电叠加集成了可视化和探索工具。



在**Lightning**部分，您可以查看 Lightning 节点之间的所有现有连接。



![network-stats](assets/fr/15.webp)



本 Interface 提供以下信息 ：





- Lightning Network 统计数据。



![distribution](assets/fr/16.webp)




⚠️ **重要**：支付通道的容量是指一个节点在闪电交易中可以发送给另一个节点的最大金额。





- 闪电节点根据互联网服务提供商（托管服务）分配，也可选择根据支付通道容量分配。



![distribution](assets/fr/17.webp)





- Lightning Network 整体能力的历史。


您还可以根据支付渠道的容量对这些节点进行排名。



![ranking](assets/fr/18.webp)



## 更多图形



Mempool.space 是享受与 Bitcoin 协议网络互动的理想平台。这些图表不仅提供可视化数据，帮助您决定何时进行交易，还提供精确的参数，使您能够实时直观地了解 Bitcoin 网络和相关闪电基础设施的强度和健康状况。



在**图形**部分，您可以查看 Bitcoin 网络的基本数据：




- Mempool 的大小变化：您可以观察 Mempool 的大小如何波动，这可以表明网络活动量的高低。



![graphs](assets/fr/19.webp)






- 所选网络上交易量和交易费的变化：通过跟踪每秒交易量的变化，您可以预测拥堵期或活动低谷期，并优化您的交易费用。通过该图表，您可以了解网络处理交易量的能力。



![graphs](assets/fr/20.webp)



现在，您已经到达了 Mempool.space 的终点，成为您自己的探索者并实时跟踪您的交易吧。下面是我们关于 Bitcoin **公共池**探索者的文章。



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1