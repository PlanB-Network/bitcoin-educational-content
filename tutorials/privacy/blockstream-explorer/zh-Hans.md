---
name: BLOCKSTREAM 探索者
description: 探索 Bitcoin 和 Liquid Network 的主要 Layer
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer 是一个便于探索交易和 Bitcoin 协议中的 Global State 以及 BLOCKSTREAM 公司开发的 [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid 的项目。



[BLOCKSTREAM.info](https://BLOCKSTREAM.info) 探索器由亚当-巴克（Adam Back）创立的 BLOCKSTREAM 公司于 2014 年发起，旨在为 Bitcoin 提供强大的基础设施，保证各层（On-Chain 和 Liquid）之间的互操作性和交易跟踪，同时增强用户安全性和隐私保护。



在本教程中，我们将介绍其与众不同之处、服务以及如何对 Bitcoin 的 On-Chain 和 Liquid 层的运行和状态进行无缝监控。



## 开始使用 BLOCKSTREAM



### 主航道导航



进入 BLOCKSTREAM.info 浏览器后，在 "**仪表板**"上，默认选择的是 Bitcoin 协议主通道。通过该 Interface，您可以概览.NET 的所有信息：





- 主链尺寸：最近开采的区块



![blocks](assets/fr/01.webp)



本节提供的信息包括最近开采的区块、Timestamp、每个 BLOCK 包含的交易数量、大小（千字节）以及每个 BLOCK 的权重单位（**WU** = *权重单位*）。鉴于主链的每个 BLOCK 都限制为 `4,000,000WU`，或 `4,000kWU`，最后一个测量值很有意义，因为它使我们能够评估 BLOCK 的优化情况。





- 最近的交易



![transactions](assets/fr/02.webp)



交易部分提供的信息包括交易的唯一标识符、所涉及的 Bitcoin 值、虚拟字节 (vB) 大小（代表所有数据（输入和输出）的总和）以及相关的收费率。例如，一个大小为 "153 vB"、费率为 "2 sat/vB "的交易将产生 "306 satoshis "的费用。



### 流体勘探



在 "**块**"菜单中，您可以追溯整个主链的历史，直至最后开采出的 BLOCK。



![blocs](assets/fr/03.webp)



通过点击特定的 BLOCK，您可以获得其中包含的信息和交易的更多详细信息。例如，BLOCK 919330：您可以看到 BLOCK 的 Hash。您还可以浏览到前一个 BLOCK，因为每个已开采的 BLOCK（Genesis 除外）都与前一个 BLOCK 相关联，并保留了前一个 BLOCK 的 Hash。



![metadata](assets/fr/04.webp)



点击**"详细信息 "**按钮，您可以获得有关该BLOCK的更多信息，例如其状态，该状态确认它已被添加到保留和传播的主链中。您还可以了解该 BLOCK 的挖矿难度：该难度代表解决 Mining 的加密问题所需的计算能力，每 2016 个区块（约 2 周）调整一次。



![details](assets/fr/05.webp)



在详细信息部分下方，我们可以找到该 BLOCK 中包含的所有交易。



BLOCK 的第一笔交易称为**交易币基**。它用于分配 Miner 的 Mining 奖励（BLOCK 和 BLOCK 补助金中包含的与交易相关的所有费用）。只有再挖出连续 100 个区块后，才能使用这笔交易产生的比特币。换句话说，要使用这些比特币，Miner 必须等待 BLOCK **919430**的产生。这就是所谓的[*"成熟期 "*](https://planb.network/fr/resources/glossary/maturity-period)。



Coinbase 是一种特殊的交易：它是唯一一种没有实际输入的交易，因为它不会花费之前交易中的任何比特币。




![coinbase](assets/fr/06.webp)



所有其他交易都分为两个部分：输入和输出。



要将比特币作为新交易的输入，交易发起人必须提供与特定脚本相对应的签名，以证明其持有比特币。每个比特币（UTXO）都包含一个脚本，一般需要特定的签名，只有持有者的私钥才能提供。这些脚本是用 Bitcoin 脚本编写的***scriptSig***（在 ASM 中），可以有多种类型。在本例中，我们可以看到使用了 P2SH 类型的UTXO，输出为 P2WPKH 类型（*Pay-to-Witness-Public-Key-Hash*）。



您可以使用启发式方法追踪特定 UTXO 的历史。我们邀请您了解不同的 Bitcoin 启发式方法以及如何加强 Bitcoin 交易的保密性：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



让我们以这笔交易的支出费用为例。点击交易标识符，我们就会跳转到交易详细信息页面的**交易**部分。



![transaction](assets/fr/08.webp)



在此页面，您可以找到该交易包含在哪个 BLOCK 中。根据使用的 Address 类型，交易可以优化其数据（*虚拟字节*），从而支付更少的交易费。例如，该交易使用以 `bc1q` 开头的本地 SegWit BECH32 Address 格式，节省了 53% 的费用。



![trx_details](assets/fr/09.webp)



## Liquid 涂层



Liquid Network 是[*Sidechain*](https://planb.network/en/resources/glossary/Sidechain)和 Bitcoin 协议的 2 级开源解决方案。特别是，它能使 Bitcoin 交易更快、更保密。



在 BLOCKSTREAM.info 浏览器上，点击 **"Liquid"**按钮切换到 Liquid Network。



![liquid](assets/fr/10.webp)



点击我们希望跟踪的其中一笔交易，我们会看到 Bitcoin 的金额被 "**保密**"字样取代。在这个网络中，交易可以是保密的，因此我们无法看到每笔 UTXO 的金额，无论是交易中的还是交易外的。



![liquid_trx](assets/fr/11.webp)



不过，我们注意到，Bitcoin 协议的主要 Layer 上的原则和机制是相同的：Bitcoin 锁定脚本和 UTXO 可追溯性。



![liquid_details](assets/fr/12.webp)



Liquid Network 还提供可供各组织使用的非存储数字资产。在**"资产 "**菜单中，您可以找到已注册资产的列表、资产总数及其相关域。



![assets](assets/fr/13.webp)



对于每种资产，您都可以追踪其发行和烧毁交易的历史（删除流通总量）。



![assets_trxs](assets/fr/14.webp)




## 更多选择



BLOCKSTREAM.info 浏览器还包括 Testnet、Bitcoin、On-Chain 和 Liquid Network 交易的可视化和跟踪。



![testnet](assets/fr/15.webp)



当你使用 Testnet 网络时，你并不使用真正的比特币，但你拥有上述所有功能。



![liquid_testnet](assets/fr/16.webp)



该网络具有不同的链长，您可以连接并测试 Bitcoin 和 Liquid 机制的运行。





- API 部分专为希望将资源管理器的某些功能整合到自己的应用程序中的用户而设。通过 API，您可以查询不同层（On-Chain 和 Liquid）的主链，跟踪交易情况，例如，查询 BLOCK 中交易的平均费用。



![api](assets/fr/17.webp)



现在，您已经准备好利用 BLOCKSTREAM Explorer 的全部潜力来查询 On-Chain 和 Liquid 层上的区块链了。希望本教程对您有所帮助，并向您推荐我们的另一个 Bitcoin Explorer 教程：



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f