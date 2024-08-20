---
term: DNS SEEDS
---

用于新比特币节点加入网络时的初始连接点。这些种子实际上是特定的DNS服务器，它们的地址被永久嵌入到比特币核心代码中。当一个新节点启动时，它会联系这些服务器以获取一个随机的IP地址列表，这些IP地址预计是活跃的比特币节点。然后，新节点可以与此列表上的节点建立连接，以获取执行其初始区块下载（IBD）和与累积工作量最多的链同步所需的信息。截至2024年，以下是比特币核心DNS种子及其维护人员的列表（https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp）：
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS种子是比特币节点建立连接的第二种方法，按优先级排序。第一种方法涉及使用节点自己创建的peers.dat文件。对于新节点来说，这个文件自然是空的，除非用户已经手动修改过它。

> ► *注意，DNS种子不应与“种子节点”混淆，后者是建立连接的第三种方式。*