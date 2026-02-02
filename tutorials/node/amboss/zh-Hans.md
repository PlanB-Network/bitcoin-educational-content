---
name: Amboss
description: 探索和分析 Lightning Network
---

![cover](assets/cover.webp)



Lightning Network是Bitcoin协议的Layer，其主要开发目的是通过提高每笔交易的处理速度，促进Bitcoin支付的日常采用。基于去中心化原则，Lightning Network 由节点（运行 Lightning 实施方案的计算机）组成，它们进行点对点通信，相互传递数据（支付和支付验证）。



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

就像在主链上一样，让用户了解网络的信息和状态，以促进节点之间的连接，并最大限度地减少网络中普遍存在的流动性问题，已变得至关重要。事实上，与 Bitcoin 主链上的交易相比，我们建议在 Lightning Network 上进行金额相对较小的小额支付。



需要注意的是，并非所有的Lightning节点都可以在Amboss平台上使用。



与[Mempool Space](https://Mempool.space)提供有关 Bitcoin 协议主链的有用信息一样，自 2022 年以来，[Amboss](https://amboss.space)提供了有关 ：





- Lightning Network 上的节点
- 支付渠道及其支付能力
- Lightning Network 随时间演变
- 统计中继节点对您的付款收取的费用。



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

在本教程中，我们将带您参观这个平台，它是 Lightning Network 用户、想要连接自己的节点以扩展网络的用户等必不可少的资源。




## 查找成对



Amboss平台的目的之一是让网络中的各个节点能够相互连接和交流信息。在平台主页上，你可以直接搜索你已经知道的节点名称，或者从你使用的最流行的Lightning投资组合中查找节点。



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

在主页上，您还可以找到根据 .NET Framework 3.0 和 .NET Framework 4.0 分类的节点：




- 容量变化：与节点公开密钥相关的 Bitcoin 数量及其所有信道的可用总量。
- 通道演化：与网络中其他节点的新连接数量。
- 节点受欢迎程度：节点的使用频率。



![nodes](assets/fr/03.webp)



因此，要选择正确的连接节点，就必须检查以下标准：





- 确保节点有足够数量的比特币；节点的容量越大，你能支付的比特币数量就越多。





- 确保节点与网络中的其他节点有大量连接和开放通道。





- 通过检查新通道的数量，确保节点处于活跃状态，并受到同行的赞赏；节点打开的新通道越多，就越受网络中其他节点的赞赏。



找到正确的节点后，单击其名称即可跳转到节点信息页面。



在这个 Interface 上，通过查看新创建通道的 Timestamp，您可以获得该节点的活动线索。您还可以找到关于该节点通道容量的信息：如果您想积极利用该节点进行支付，这些信息至关重要。




![node_info](assets/fr/04.webp)



在左侧部分，您可以找到有关该节点位置的更多详细信息。例如，您可以查看 ：




- 公钥：节点名称下方的标识符。
- 该节点的地理位置。




![channels](assets/fr/05.webp)



该 Interface 将告诉您该节点的连接 Address：其形式为 `pubkey@ip:port`。在我们的示例中，我们要连接的节点是 ：




- 公钥 `pubkey` 是： `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`.
- 端口：`9735`



![geoinfo](assets/fr/06.webp)



在**通道**部分，您将看到开放通道列表以及节点与网络中其他节点的连接。在 Interface 中，有几项信息对确认该节点是否符合我们的需求或是否可靠至关重要：





- 接收比率**：节点每收到一百万 Satoshi 将向您收取的费用，具体取决于所选的频道。
- 比率（百万分率）**：表示当您决定通过节点的某个通道付款时，节点将向您收取的每百万单位的 Satoshi 数量。假设您决定通过一个 ppm 比率为 `500 Sats` 的通道支付 `10_000 Sats`，那么您需要向节点支付 `10_000 * 500 / 1_000_000` 个卫星，相当于 `5 Sats`。
- HTLC](https://planb.academy/resources/glossary/htlc) 最大值** ：该节点允许您通过其中一个通道转运的最大数量。



通过查阅本 Interface 中的表格，您还可以找到与之匹配的节点上的所有这些信息。



![channels_info](assets/fr/07.webp)



在**通道地图**部分，您可以看到该节点上各通道的分布和容量。您可以从右侧的下拉列表中选择一个选项，更改显示的分布标准。



![cha_maps](assets/fr/08.webp)



关闭通道**部分根据关闭类型对节点的所有前通道进行分组：




- 相互关闭**：表示双方同意，使用各自的私人密钥签署交易，标志着渠道的关闭和渠道内余额的分配。
- 强制关闭**：表示突然单方面关闭通道的一部分。不建议采用这种关闭方式，因为 Lightning Network 是一个基于惩罚的协议：当你试图骗取一个通道的余额时，你将面临失去该通道所有可用余额的风险。



![closed](assets/fr/09.webp)



了解通过您使用的节点上的通道进行支付的转接费信息



![fees](assets/fr/10.webp)



## 网络信息



Amboss 不仅关注网络成员信息，还关注网络本身的状态。



在左侧 "模拟 "菜单下的 "统计**"部分，有一张图表显示成功付款的概率与付款金额的函数关系。



事实上，你会发现曲线在下降，因为随着付款金额的增加，你看到付款通过的机会也在减少。这反映了 Lightning Network 上真正的流动性问题。例如，您支付的 `10_000` 萨托希有 `79%` 的机会成功支付。另一方面，如果您支付的是 `3_000_000` 沙托西，您成功的几率则不到 `13%`。



![network](assets/fr/11.webp)



网络统计**菜单允许您以图形方式显示 ：




- 付款渠道
- 节点
- 容量
- 费用
- 渠道演变。



![network_stat](assets/fr/12.webp)



在**市场统计**菜单中，**订单详情**选项允许您查看 Lightning Network 上的流动性需求。该图表还可以显示哪些通道需求量最大和/或哪些通道的容量相当大。



![markets](assets/fr/13.webp)




## 工具



Amboss 提供多种工具，帮助您优化搜索和操作。



### Lightning Network 解码器



该工具主要负责为您提供 Lightning Invoice、Lightning Address 或 Lightning URL 结构的详细信息。



例如，在主页的**工具**部分，提交您的闪电 Address。



![decoder](assets/fr/14.webp)



从该解码器中，您可以获得以下信息： ：




- 与 Lightning Address 相关联的节点公钥；
- Address 中 Invoice 的过期时间；
- 您可以发送的最小和最大值；
- 与您的 Address 相关联的 Nostr 节点（如果该节点已启用 Nostr）。



![decode](assets/fr/15.webp)



### 岩浆 IA



探索Amboss推出的最新工具，有效管理与Lightning Network节点的连接。Magma AI 使用专门的人工智能来解决一个重要问题：选择好要连接的节点。



![magma](assets/fr/16.webp)



### Satoshi 计算器



以当地货币（欧元/美元）计算 Bitcoin 的当前价格。在主页上，使用卫星计算器找出当前市场价格。



![calculator](assets/fr/17.webp)




现在您已经对该平台的功能和分析工具有了全面的了解。下面是我们关于 Bitcoin **Mempool.space**资源管理器的文章。



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f