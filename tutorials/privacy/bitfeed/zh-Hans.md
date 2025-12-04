---
name: Bitfeed
description: 探索主要的 Bitcoin 协议链。
---

![cover](assets/cover.webp)



Bitfeed 是一个可视化 Bitcoin 协议链上层的平台。它是由 Mempool.space 项目的一名贡献者发起的，主要以其简约的外观和易用性脱颖而出。



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

在本教程中，我们将介绍这个工具，它可以让你查看网络上的所有交易和区块。



## 开始使用 Bitfeed



Bitfeed 是一个专注于三个要点的平台：





- Blockchain 磋商**、
- 交易搜索**、
- 可视化记忆库**。



### 咨询区块链



在 Bitfeed 主页上，您主要可以找到 ：





- 搜索栏：该部分是区块链查询的入口。在这里，你可以通过编号或哈希值搜索特定区块。您还可以搜索特定交易和 Bitcoin 地址，以验证网络上的某些交易信息。



![searchBar](assets/fr/01.webp)



在左上角，你可以看到比特币的当前价格，估算单位为美元（USD）。



![price](assets/fr/02.webp)



右侧边栏是平台菜单。通过该菜单，您可以根据自己的喜好自定义平台界面、添加或删除项目以及自定义查看过滤器。例如，按值或按虚拟字节（vBytes）权重查看每个区块的大小。



![menu](assets/fr/03.webp)



页面中央是最后一个挖出的区块，并可查看该区块中包含的所有交易。该部分提供的信息包括时间戳、区块中涉及的比特币总数、区块大小（以字节为单位）、交易次数以及区块中每个虚拟字节的平均交易成本比。



![block](assets/fr/04.webp)



您可以在搜索栏中搜索特定区块，根据您的条件查看频道历史。



例如，我们要查看区块 `879488` 中的交易。



![bloc](assets/fr/05.webp)



该区块的第一笔交易是**币基**交易，它使该区块的矿工能够获得 mining 奖励，该奖励只有在开采出 100 个区块后才能使用，由包含的交易费用和区块补助金组成。该交易使系统能够发行新的比特币。



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

默认情况下，区块中的交易根据两个标准来表示：




- 大小，可以在值和权重（vBytes）之间变化；
- 颜色会因年龄和每个虚拟字节的交易费用比例而不同。



![options](assets/fr/07.webp)



因此，我们可以得出结论，同一区块中的所有交易在区块链中的确认次数相同。最大的方块代表比特币数量最多的交易。



**"信息 "**菜单选项进一步证实了这一解释，它告诉我们区块交易的颜色和大小的翻译。



![infos](assets/fr/08.webp)



您还可以按虚拟字节和费用比率查看一个区块的交易。这种查看方式可能与前一种不同，因为交易中包含的比特币价值并不决定其大小。



![visualisation](assets/fr/09.webp)



### 查看交易



您可以通过搜索栏使用交易标识符搜索交易。您还可以点击一个立方体，查看与该交易相关的信息。



在我们的案例中，让我们来看看占据块 `879488` 中最大空间的交易。



![biggest](assets/fr/10.webp)



你会看到这笔交易有 `42,989`，这代表了正在挖掘的最后一个区块与我们选择的区块之间的差值。这些确认有助于加强 Bitcoin 网络的安全性，因为要恶意修改这笔交易，攻击者需要拥有重写整个主区块链的同等计算能力。



这笔交易的大小为 57 088 vBytes，主要是因为在构建过程中使用了大量的 UTXO（842 个条目）。令人惊讶的是，与整个区块平均 5.82 sats/vByte 的费用相比，所采用的费用比率仍然相对较低（仅为 4 sats/vByte）。



因此，占用空间最大的交易不一定是交易成本比率最高的交易。



![transaction](assets/fr/11.webp)



如果按照**信息**菜单中的比例，交易成本比率最高的交易是紫色的那笔。这是交易 [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35)，其交易成本比率为 `147.49 sats/vBytes`。



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool 可视化



mempool是将等待纳入区块的Bitcoin交易集中在一起的虚拟位置。Bitfeed 允许查询多个 Bitcoin 矿工的 [mempool](https://planb.academy/resources/glossary/mempool)，提供广泛的交易跟踪功能。



![mempool](assets/fr/13.webp)



在本节中，您可以跟踪 Bitcoin 网络主链上所有有效但尚未确认的交易。



![unconfirmed](assets/fr/14.webp)



现在，您已经掌握了如何使用 Bitfeed 平台分析区块和交易的指南，以便可视化 Bitcoin 网络主链上的可用信息，同时受益于简约、易用的界面。如果您喜欢本教程，我们建议您进行下一步：通过 Amboss 项目了解 Lightning Network。



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017
