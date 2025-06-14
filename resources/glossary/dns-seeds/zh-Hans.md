---
term: DNS SEEDS

---
新加入网络的比特币节点的初始连接点。这些种子实际上是特定的 DNS 服务器，它们的地址永久嵌入在 Bitcoin Core 代码中。当一个新节点启动时，它会联系这些服务器，以获得一个随机的 IP 地址列表，其中可能包含已启用的比特币节点。然后，新节点可以与列表中的节点建立连接，获取初始化区块下载（IBD）所需的信息，并与累积工作量最多的区块链同步。截至 2024 年，以下是Bitcoin Core DNS 种子列表及其维护负责人 (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp)：


- seed.bitcoin.sipa.be：Pieter Wuille；
- dnsseed.bluematt.me：Matt Corallo；
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us：Luke Dashjr；
- seed.bitcoinstats.com：Christian Decker；
- seed.bitcoin.jonasschnelli.ch：Jonas Schnelli；
- seed.btc.petertodd.net：Peter Todd；
- seed.bitcoin.sprovoost.nl：Sjors Provoost；
- dnsseed.emzy.de：Stephan Oeste；
- seed.bitcoin.wiz.biz：Jason Maurice；
- seed.mainnet.achownodes.xyz：Ava Chow.

按优先级排序，DNS 种子是比特币节点建立连接的第二种方法。第一种方法是使用节点自己创建的 peers.dat 文件。如果是新节点，这个文件一定是空的，除非用户手动对其进行更改。

> ► *请注意，DNS 种子不应与 “Seed Nodes” 混淆，后者是建立连接的第三种方式。
