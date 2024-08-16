---
name: 守望塔
description: 理解和使用守望塔
---

## 守望塔是如何工作的？

作为闪电网络生态系统的一个重要部分，守望塔为用户的闪电通道提供了额外的保护程度。其主要职责是监控通道的健康状况，并在一方试图欺诈另一方时进行干预。

那么，守望塔如何确定一个通道是否已经被破坏呢？守望塔从客户端（通道的一方）接收它所需的信息，以便正确识别并响应任何违规行为。这些信息通常包括最新的交易细节、当前通道状况以及创建惩罚性交易所需的信息。在将数据传输给守望塔之前，客户端可能会对其进行加密，以保护隐私和保密性。这样即使守望塔获得了数据，也无法解密加密数据，除非真的发生了违规行为。这种加密系统保护了客户端的隐私，同时阻止守望塔未经授权访问私人数据。

## 如何设置您自己的索托斯之眼并开始贡献

索托斯之眼（[RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)）是一个非托管的闪电网络守望塔，符合[BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)。它有两个主要组成部分：

1. teos：包括CLI和塔的服务器端核心功能。构建此包时将产生两个二进制文件——teosd和teos-cli。

2. teos-common：包括服务器端和客户端的共享功能（有助于创建客户端）。

要成功运行塔，您需要在运行塔的teosd命令之前运行bitcoind。在运行这两个命令之前，您需要设置您的bitcoin.conf文件。以下是如何做到这一点的步骤：

1. 从源代码安装比特币核心或下载它。下载后，将bitcoin.conf文件放在比特币核心用户目录中。检查此链接以获取更多有关放置文件位置的信息，因为这取决于您使用的操作系统。

2. 确定需要创建文件的位置后，添加这些选项：

'''
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1
'''

- server：用于RPC请求
- rpcuser和rpcpassword：RPC客户端可以使用它们与服务器进行身份验证
- regtest：不是必需的，但如果您计划进行开发，这会很有用。

rpcuser和rpcpassword需要您自己选择。它们必须不带引号编写。例如：

'''
rpcuser=aniketh
rpcpassword=strongpassword
'''

现在，如果您运行bitcoind，它应该开始运行节点。

1. 对于塔部分，首先，您必须从源代码安装teos。按照此链接中给出的说明进行操作。

2. 在您的系统中成功安装teos并运行测试后，您可以进行最后一步，即在teos用户目录中设置teos.toml文件。该文件需要放在名为.teos的文件夹中，位于您的主文件夹下（注意点），例如，对于Linux，是/home/<your-username>/.teos。一旦您找到了位置，创建一个teos.toml文件，并根据我们在bitcoind上所做的更改设置这些选项。
#bitcoindbtc_network = "regtest"
btc_rpc_user = <您的用户名>
btc_rpc_password = <您的密码>

请注意，在这里用户名和密码需要用引号括起来，也就是说，按照之前的例子：

'''
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
'''

完成这些设置后，您就可以开始运行tower了。由于我们在regtest上运行，所以第一次tower连接到比特币测试网络时，可能不会有任何区块被挖出（如果有的话，那肯定是出了些问题）。tower会构建一个内部缓存，包含来自bitcoind的最新100个区块，因此在第一次运行时我们可能会遇到以下错误：

> ERROR [teosd] 没有足够的区块来启动tower（需要：100）。请至少再挖掘100个区块

鉴于我们在regtest上运行，我们可以通过发出RPC命令来挖掘区块，而无需等待我们通常在其他网络（如mainnet或testnet）中看到的10分钟平均时间。查看bitcoin-cli帮助并查找如何挖掘区块。如果您需要一些帮助，可以阅读这篇文章。

![image](assets/2.webp)

就是这样，您已经成功运行了tower。恭喜您。🎉