---
name: 漩涡统计工具 - 匿名集
description: 理解匿名集的概念以及如何使用WST计算它
---
![cover](assets/cover.webp)

***警告：** 继Samourai Wallet的创始人在4月24日被逮捕，其服务器被查封之后，漩涡统计工具（Whirlpool Stats Tool，简称WST）已无法下载，因为它托管在Samourai的Gitlab上。即使您之前已将此工具下载到本地机器上，或者它已安装在您的RoninDojo节点上，目前WST也无法正常工作。它依赖OXT.me提供的数据进行运行，而该网站现已无法访问。当前，由于Whirlpool协议处于非活动状态，WST并不特别有用。然而，这些软件有可能在未来几周内重新启用。此外，本文的理论部分对于理解coinjoin的原理和目标（不仅仅是Whirlpool），以及理解Whirlpool模型的有效性仍然相关。您还可以学习如何量化coinjoin周期所提供的隐私保护。*

_我们正在密切关注此案件以及相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息参考之用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

---

*"打破你的硬币留下的链接"*

在本教程中，我们将研究匿名集的概念，这是一种指标，允许我们估计Whirlpool上coinjoin过程的质量。我们将介绍这些指标的计算方法和解释。在理论部分之后，我们将通过学习使用Python工具*漩涡统计工具*（Whirlpool Stats Tools，简称WST）计算特定交易的匿名集来进行实践。

## 什么是比特币上的coinjoin？
**Coinjoin是一种打破比特币在区块链上可追踪性的技术**。它依赖于一种具有特定结构的协作交易：coinjoin交易。

coinjoin交易通过使外部观察者难以进行链分析，增强了比特币用户的隐私。它们的结构允许将来自不同用户的多个硬币合并到单一交易中，从而模糊了轨迹，使得难以确定输入和输出地址之间的链接。

coinjoin的原理基于协作方法：几个希望混合他们的比特币的用户以相同的金额作为同一交易的输入。这些金额随后以等值输出的形式重新分配。交易结束时，不可能将特定的输出与给定的用户关联起来。输入和输出之间不存在直接链接，从而打破了用户与其UTXO之间的关联，以及每个硬币的历史记录。

![coinjoin](assets/notext/1.webp)

coinjoin交易示例：
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
为了在执行coinjoin时确保每位用户始终控制着自己的资金，这个过程从一个协调者构建交易开始，然后将其传输给每位参与者。每位用户在验证交易符合自己的需求后签名。所有收集到的签名最终被整合到交易中。如果用户或协调者试图通过修改coinjoin交易的输出来转移资金，签名将被证明无效，导致节点拒绝该交易。
coinjoin有几种实现方式，如Whirlpool、JoinMarket或Wabisabi，每种方式都旨在管理参与者之间的协调并提高coinjoin交易的效率。
在这个教程中，我们将重点介绍我最喜欢的实现方式：Whirlpool，它可以在Samourai Wallet和Sparrow Wallet上使用。我认为，对于比特币上的coinjoins来说，它是最高效的实现方式。
## Bitcoin上使用coinjoin的效用是什么？
coinjoin的效用在于它能够通过将你的币淹没在一群无法区分的币中来产生合理的否认性。这一行动的目标是打破过去到现在以及从现在到过去的可追溯性链接。

换句话说，一个知道你在coinjoin周期入口处初始交易的分析师，不应该能够确定地识别出你在混币周期出口处的UTXO（从周期入口到周期出口的分析）。

![coinjoin](assets/en/2.webp)

相反，一个知道你在coinjoin周期出口处的UTXO的分析师，应该无法确定周期入口处的原始交易（从周期出口到周期入口的分析）。

![coinjoin](assets/en/3.webp)

为了评估分析师将过去与现在联系起来（反之亦然）的难度，需要量化你的币隐藏在其中的群体的大小。这个度量告诉我们具有相同概率的分析数量。因此，如果正确的分析在3个具有相同概率的分析中淹没，你的隐藏程度非常低。另一方面，如果正确的分析在一组20000个同样可能的分析中，你的币就隐藏得非常好。

而且，这些群体的大小代表了被称为“匿名集”的指标。

## 理解匿名集
匿名集作为评估特定UTXO隐私程度的指标。更具体地说，它们衡量在包含被研究币的集合中无法区分的UTXOs的数量。需要一个均匀的UTXO集合，这意味着匿名集通常是在coinjoin周期上计算的。这些指标的使用对于Whirlpool coinjoins来说特别相关，因为它们的一致性。

匿名集允许在适当的情况下，评判coinjoins的质量。较大的匿名集大小意味着增加的匿名性级别，因为在集合中区分特定UTXO变得困难。

匿名集有两种类型：
- **预期匿名集；**
- **回顾性匿名集。**
第一个指标显示了在周期结束时，已知入口处的UTXO，被隐藏的研究UTXO所在的群体的大小，即这个群体中存在的无法区分的币的数量。这个指标允许衡量币的保密性对过去到现在（入口到出口）分析的抵抗力。在英文中，这个指标的名称是“*forward anonset*”，或者“*forward-looking metrics*”。
![coinjoin](assets/en/4.webp)
此指标估计了您的UTXO在coinjoin过程中从入口点到出口点的历史重构尝试中受到的保护程度。

例如，如果您的交易参与了其第一个coinjoin周期，并且完成了两个其他后代周期，那么您的硬币的预期匿名集将是`13`：

![coinjoin](assets/en/5.webp)

第二个指标显示了在周期结束时知道UTXO的情况下，给定硬币的可能来源数量。这个指标衡量了硬币保密性对从现在到过去（从出口到入口）的分析的抵抗力，即，对分析师来说追溯到您的硬币在coinjoin周期之前的起源有多困难。用英语来说，这个指标的名称是“*backward anonset*”，或者“*backward-looking metrics*”。

![coinjoin](assets/en/6.webp)

知道了周期结束时的UTXO，回顾性匿名集确定了可能构成您进入coinjoin周期的入口的潜在Tx0交易的数量。在下面的图表中，这对应于所有橙色气泡的总和。

![coinjoin](assets/en/7.webp)

## 使用Whirlpool Stats Tools (WST)计算匿名集
要计算经过coinjoin周期的您自己的硬币的这些指标，您可以使用Samourai Wallet特别开发的工具：*Whirlpool Stats Tools*。

如果您有RoninDojo，WST已预装在您的节点上。因此，您可以跳过安装步骤，直接遵循使用步骤。对于那些没有RoninDojo节点的人，让我们看看如何在计算机上安装这个工具。

您将需要：Tor浏览器（或Tor）、Python 3.4.4或更高版本、git和pip。打开一个终端。要检查这些软件在您的系统上的存在和版本，请输入以下命令：
```plaintext
python --version
git --version
pip --version
```

如果需要，您可以从它们各自的网站下载它们：
- https://www.python.org/downloads/ (自3.4版本起，pip直接随Python一起提供)；
- https://www.torproject.org/download/；
- https://git-scm.com/downloads。
安装所有这些软件后，从终端克隆WST仓库：
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

导航到WST目录：
```plaintext
cd whirlpool_stats
```

安装依赖项：
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

您也可以手动安装它们（可选）：
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

导航到`/whirlpool_stats`子文件夹：
```plaintext
cd whirlpool_stats
```

启动WST：
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

在后台启动Tor或Tor浏览器。

**-> 对于RoninDojo用户，您可以直接在这里恢复教程。**

将代理设置为Tor (RoninDojo)，
```plaintext
socks5 127.0.0.1:9050
```
或者根据您使用的情况，配置到Tor浏览器：```plaintext
socks5 127.0.0.1:9150
```

这种操作将允许您通过Tor下载OXT上的数据，以避免泄露有关您交易的信息。如果您是新手，这一步看起来复杂，要知道它只涉及通过Tor引导您的互联网流量。最简单的方法包括在您的电脑上后台启动Tor浏览器，然后执行仅第二个命令通过这个浏览器连接（`socks5 127.0.0.1:9150`）。

![WST](assets/notext/11.webp)

接下来，导航到您打算使用`workdir`命令下载WST数据的工作目录。这个文件夹将用于存储您从OXT检索的交易数据，形式为`.csv`文件。这些信息对于计算您希望获得的指标至关重要。您可以自由选择此目录的位置。创建一个专门用于WST数据的文件夹可能是明智的。例如，我们选择下载文件夹。如果您使用的是RoninDojo，这一步不是必需的：
```plaintext
workdir path/to/your/directory
```

命令提示符应随后更改以指示您的工作目录。

![WST](assets/notext/12.webp)

然后从包含您交易的池中下载数据。例如，如果我在`100,000 sats`池中，命令是：
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

WST上的面额代码如下：
- 0.5比特币池：`05`
- 0.05比特币池：`005`
- 0.01比特币池：`001`
- 0.001比特币池：`0001`
一旦数据下载完毕，加载它。例如，如果我在`100,000 sats`池中，命令是：
```plaintext
load 0001
```

这一步根据您的电脑可能需要几分钟。现在是泡一杯咖啡的好时机！:)

![WST](assets/notext/14.webp)

加载数据后，输入`score`命令并跟上您的TXID（交易标识符）以获取其匿名集：
```plaintext
score TXID
```

**注意**，使用哪个TXID的选择取决于您希望计算的匿名集。为了评估一个硬币的预期匿名集，需要通过`score`命令输入对应于其第一个coinjoin的TXID，这是与此UTXO进行的初始混合。另一方面，要确定回顾性匿名集，您必须输入执行的最后一个coinjoin的TXID。总而言之，预期匿名集是从第一次混合的TXID计算的，而回顾性匿名集是从最后一次混合的TXID计算的。

WST随后会显示回顾性评分（*向后看的指标*）和预期评分（*向前看的指标*）。例如，我随机取了一个不属于我的Whirlpool上的硬币的TXID。

![WST](assets/notext/15.webp)
有关的交易：[7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
如果我们将这笔交易视为所涉及硬币的第一次混币操作，那么它将从预期匿名集`86,871`中受益。这意味着它隐藏在`86,871`个无法区分的硬币中。对于一个知道这枚硬币在混币周期开始时并试图追踪其输出的外部观察者，他们将面临`86,871`个可能的UTXO，每个都有相同的可能性是被寻找的硬币。

如果我们考虑这笔交易是该硬币的最后一次混币，那么它具有`42,185`的回顾性匿名集。这意味着有`42,185`个潜在来源对于这个UTXO。如果一个外部观察者在周期结束时识别出这枚硬币并寻求追踪其来源，他们将面临`42,185`个可能的来源，所有这些来源都有相同的可能性是被寻找的起源。

除了匿名集分数外，WST还根据匿名集为您提供了输出在池中的扩散率。这个另一个指标简单地允许您评估您的硬币改进的潜力。这个率对于预期匿名集特别有用。实际上，如果您的硬币有15%的扩散率，这意味着它可以与池中15%的硬币混淆。这很好，但您仍然有很大的改进空间，可以通过继续混币来实现。另一方面，如果您的硬币有95%的扩散率，那么您接近了池的极限。您可以继续混币，但您的匿名集不会有太大增加。

重要的是要注意，WST计算的匿名集并不完全准确。鉴于需要处理的大量数据，WST使用*HyperLogLogPlusPlus*算法显著减轻了与本地数据处理和所需内存相关的负担。这是一种算法，允许在维持结果高精度的同时估计非常大的数据集中不同值的数量。因此，提供的分数足够好，可以用于您的分析，因为它们非常接近实际情况的估计，但不应将其解释为单位的确切值。

总之，记住不是必须为您在混币中的每个硬币系统地计算匿名集。Whirlpool的设计本身就提供了保证。实际上，回顾性匿名集很少是一个问题。从您的初始混合开始，您就因为自创世纪混币以来的前几次混合的遗产而获得了特别高的回顾性分数。至于预期匿名集，只需将您的硬币保留在混币后账户中足够长的时间即可。
这就是为什么我认为在*持有 -> 混币 -> 消费 -> 替换*策略中使用Whirlpool特别相关的原因。在我看来，最合逻辑的方法是将大部分比特币储蓄保持在冷钱包中，同时持续在Samourai上进行一定数量的coinjoin操作以支付日常开销。一旦来自coinjoin的比特币被消费，就用新的比特币替换它们，以返回到混合片段的定义阈值。这种方法允许人们摆脱对我们UTXO匿名集的担忧，同时使coinjoin的有效性所需的时间变得不那么限制。

**外部资源：**

- [关于链分析的法语播客](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [关于HyperLogLog的维基百科文章](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai的Whirlpool统计仓库
- Samourai的Whirlpool网站
- [Samourai关于隐私和比特币的英文Medium文章](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Samourai关于匿名集概念的英文Medium文章](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)