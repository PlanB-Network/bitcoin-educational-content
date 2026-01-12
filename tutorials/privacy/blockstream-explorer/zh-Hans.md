---
name: Blockstream Explorer
description: 探索 Bitcoin 和 Liquid Network 的主层
---

![cover](assets/cover.webp)



Blockstream Explorer 是一个便于探索交易和 Bitcoin 协议以及 Blockstream 公司开发的 [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid 的全球状态的项目。



[blockstream.info](https://blockstream.info)探索器由亚当-巴克（Adam Back）创立的公司Blockstream于2014年发起，旨在为Bitcoin提供强大的基础设施，保证各层（on-chain和Liquid）之间的互操作性和交易跟踪，同时增强用户的安全性和隐私性。



在本教程中，我们将了解它的与众不同之处、它的服务以及它如何对 Bitcoin 的 on-chain 和 Liquid 层的运行和状态进行无缝监控。



## 开始使用 Blockstream 浏览器



### 主航道导航



进入 Blockstream.info 浏览器后，在 "**仪表板**"上，默认选择 Bitcoin 协议主链。在此界面中，您可以概览.NET Framework 3.0的所有功能：





- 主链尺寸：最近开采的区块



![blocks](assets/fr/01.webp)



该部分提供了最近开采的区块、时间戳、每个区块中包含的交易数量、大小（千字节）以及每个区块的权重单位（**WU** = *权重单位*）。鉴于主链的每个区块的重量单位限制为 "4,000,000 WU "或 "4,000 kWU"，最后一项测量值非常重要，因为它使我们能够评估区块的优化情况。





- 最近的交易



![transactions](assets/fr/02.webp)



交易部分提供的信息包括交易的唯一标识符、涉及的比特币价值、虚拟字节（vB）大小（代表所有数据（输入和输出）的总和）以及相关费用率。例如，一笔大小为 "153 vB"、费率为 "2 sat/vB "的交易将产生 "306 satoshis "的费用。



### 流体勘探



在 "**区块**"菜单中，您可以追溯整个主链的历史，直到最后一个区块被开采出来。



![blocs](assets/fr/03.webp)



通过点击特定区块，您可以获取其中包含的信息和交易的更多详细信息。例如，区块 919330：您将看到该区块的哈希值。您还可以导航到前一个区块，因为每个已开采区块（Genesis 除外）都与前一个区块有链接，并保留了前一个区块的哈希值。



![metadata](assets/fr/04.webp)



点击**"详细信息 "**按钮，您可以获得有关该区块的更多信息，例如其状态，该状态确认该区块已被添加到保留和传播的主链中。您还可以了解该区块的挖矿难度：该难度代表解决 mining 加密问题所需的计算能力，每 2016 个区块（约 2 周）调整一次。



![details](assets/fr/05.webp)



在详细信息部分下方，我们可以找到该区块中包含的所有交易。



区块中的第一笔交易称为**交易币基**。它用于分配矿工的 mining 奖励（与区块中包含的交易和区块补助相关的所有费用）。只有再挖出连续 100 个区块后，才能使用这笔交易产生的比特币。换句话说，矿工要想使用这些比特币，就必须等待 **919430** 区块的产生。这就是所谓的[*"成熟期 "*](https://planb.academy/fr/resources/glossary/maturity-period)。



Coinbase 是一种特殊的交易：它是唯一一种没有实际输入的交易，因为它不会花费上一笔交易中的任何比特币。




![coinbase](assets/fr/06.webp)



所有其他交易都分为两个部分：输入和输出。



要将比特币作为新交易的输入，交易发起人必须提供与特定脚本相对应的签名，以证明其持有比特币。每个比特币（UTXO）都包含一个脚本，一般需要特定的签名，只有持有者的私钥才能提供。这些脚本是用 Bitcoin 脚本编写的***scriptSig***（在 ASM 中），可以有多种类型。在本例中，我们可以看到使用了 P2SH 类型的UTXO，输出为 P2WPKH 类型（*Pay-to-Witness-Public-Key-Hash*）。



您可以使用启发式方法追踪特定 UTXO 的历史。我们邀请您了解不同的 Bitcoin 启发式方法和加强 Bitcoin 上交易保密性的方法：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



让我们以这笔交易的支出费用为例。点击交易标识符，我们就会跳转到交易详细信息页面的**交易**部分。



![transaction](assets/fr/08.webp)



在该页面，您可以找到交易包含在哪个区块中。根据使用的地址类型，交易可以优化其数据（*虚拟字节*），从而减少交易费用。例如，通过使用以 `bc1q` 开头的本地 SegWit Bech32 地址格式，这笔交易节省了 53% 的费用。



![trx_details](assets/fr/09.webp)



## Liquid 层



Liquid Network 是 Bitcoin 协议的[*侧链*](https://planb.academy/en/resources/glossary/sidechain)和开源二级解决方案。特别是，它能使比特币交易更快、更保密。



在 Blockstream.info 浏览器上，点击 **"Liquid"**按钮，切换到 Liquid 网络。



![liquid](assets/fr/10.webp)



点击我们想要追踪的其中一笔交易，我们会发现比特币的数额被 "**保密**"的字样所取代。在这个网络中，交易可以是保密的，所以我们无法看到每个 UTXO 的金额，无论是交易中的还是交易外的。



![liquid_trx](assets/fr/11.webp)



不过，我们注意到，Bitcoin 协议主层的原则和机制是相同的：比特币锁定脚本和 UTXO 可追溯性。



![liquid_details](assets/fr/12.webp)



Liquid Network 还提供可供各组织使用的非存储数字资产。在**"资产 "**菜单中，您可以找到已注册资产的列表、资产总数及其相关域。



![assets](assets/fr/13.webp)



对于每种资产，您都可以追踪其发行和烧毁交易的历史（删除流通总量）。



![assets_trxs](assets/fr/14.webp)




## 更多选择



Blockstream.info 浏览器还包括 Testnet、Bitcoin、on-chain 和 Liquid Network 上交易的可视化和跟踪。



![testnet](assets/fr/15.webp)



当你使用 Testnet 网络时，你并不使用真正的比特币，但你拥有上述所有功能。



![liquid_testnet](assets/fr/16.webp)



该网络具有不同的链条长度，您可以连接并测试 Bitcoin 和 Liquid 机械装置的运行。





- API 部分专门用于希望将资源管理器的某些功能整合到自己应用程序中的用户。通过 API，您可以查询不同层（on-chain 和 Liquid）的主链，跟踪交易，例如，查询区块中交易的平均费用。



![api](assets/fr/17.webp)



现在，您已经准备好利用 Blockstream Explorer 的全部潜力来查询 on-chain 和 Liquid 层上的区块链了。希望本教程对您有所帮助，并向您推荐我们关于另一个 Bitcoin 浏览器的教程：



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f