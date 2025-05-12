---
name: Lightning Network Daemon (Linux)
description: 在 Linux 上安装和运行 Lightning Network Daemon
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network 是 Bitcoin 的第二个 Layer，特别是由于其交易速度快、成本低，使其具有闪电般的尺寸。



在本教程中，我们将在 Linux 机器（Ubuntu 24.04 发行版）上安装 Lightning Network Daemon 实现。



## 什么是 Lightning Network Daemon？



Lightning Network Daemon 是 Lightning Network 的完整 Go 实现。它由 Lightning Labs 创建，能让你在机器上运行一个完整的 Lightning 节点实例。


换句话说，通过这种实现方式，您可以 ：





- 与Lightning Network**互动：您可以使用命令行直接从机器终端创建闪电投资组合、管理支付渠道和路线等。
- 链接远程 Bitcoin 节点或您自己的 Bitcoin 核心实例**：LND 允许您链接 Bitcoin 实例并将其用作后台。要使用这种实现方式，您不需要在自己的机器上运行 Bitcoin Core 实例。




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## 为什么要有自己的 "闪电 "节点？


闪电是一种 Bitcoin 叠加工具，可优化转账流程并降低交易成本。



通过旋转 "闪电 "节点，您获得了主权和自主权。您可以控制自己的资金，因此请记住：



"不是你的钥匙 也不是你的比特币"



从这个意义上说，运行 "闪电 "节点可以从以下几个方面提高数据的安全性和完整性：





- 全面控制**：管理自己的支付渠道，成为自己的银行，掌握自己的资产。
- 保密性**：无需依赖第三方保护您的隐私即可进行交易。
- 学习和自主**：有了 "lncli "命令，你就可以在终端上自行应用，从而更好地了解 Lightning 的底层进程。
- 权力下放**：在加强和下放 Bitcoin / Lightning Network 方面发挥积极作用。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


在我们的机器上运行 LND 实现实例有两种选择。我们可以在自己的机器上设置环境以便本地运行，或者从 Docker 容器中安装 LND。在这里，我们将集中讨论第一种方案，并在稍后的教程中了解如何使用 Docker。


## 从源代码安装 LND



### 先决条件


由于 LND 是用 Go 编写的，因此需要确保 Linux 机器上有 GoLang 环境和必要的依赖项。





- 硬件要求：**


为了获得流畅、无缝的体验，您的机器需要具备运行 LND Lightning 节点所需的容量。



您将需要 ：


1. **8 GB 内存**，可实现最佳流畅性、


2. **多核处理器（四核或更多）**，以高效管理节点的运行、


3. **至少 5GB 磁盘空间**用于剪枝节点模式，1TB 用于运行 Bitcoin Core（如果使用远程节点，则可选）。





- 安装有用的依赖项：**


下面的命令将允许您在机器上安装运行 LND 所需的工具。除其他事项外，您还需要安装版本管理工具 `Git` 和 `make`，后者可以从源代码执行和构建 LND 实现。



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- 在 Linux 机器上安装 GoLang**



截至本教程发布之日，LND 需要 Go*** 1.23.6 版本才能安装。



如果已经安装了以前的版本，请将其删除，以便安装新的 Go。


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** 环境配置


在你的 `~/.bashrc` 文件中，初始化以下环境变量，将 Go 添加到你的 Linux 系统中。



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- 检查安装** （法语）


```bash
go version
```



![go-version](assets/fr/03.webp)


### 克隆 LND GitHub 仓库



使用 git 在本地计算机上获取 LND 源代码副本


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### 构建和安装



之前安装的 "make "工具将帮助您从 LND 源代码中构建可执行文件，并继续进行安装。



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



在机器上安装 LND



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- 检查您的安装** （法语）



为确保一切顺利，运行此命令后，您将看到当前运行的 LND 版本。



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- 维护和升级



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **重要**：LND 更新可能需要更新版的 Go，因此请务必更新您的系统，以免在安装过程中出现依赖问题。


### 配置 Lightning Network Daemon



Lightning LND 节点的配置与 Bitcoin 类似，都是在包含节点所有参数的配置文件中进行的。为此，您可以在机器根目录下创建一个隐藏文件夹 `.LND`，然后在该文件夹下创建配置文件 `LND.conf`。



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





在配置文件中，您可以设置 LND 节点。



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## 了解您的配置



了解正确、完整安装 LND 节点所需的最低配置非常重要。



根据 `~/.LND/LND.conf` 文件的内容，以下是字段的详细信息：





- noseedbackup**：允许您选择是否希望 LND 对您的投资组合执行自动备份。  将此属性设置为 "0 "可让您手动将还原信息保存在个人选择的安全位置。





- debuglevel**：允许您定义在操作过程中出现错误时，错误和日志的详细程度。





- Bitcoin.active**：指示 LND 作为 Bitcoin 节点运行并与 Bitcoin 网络交互。





- Bitcoin.Mainnet**：指定 LND 连接到 Bitcoin 的主网络 (Mainnet)，您可以为 Bitcoin Signet 和 Bitcoin Regtest 网络分别设置`bitcoind.signet`和`bitcoind.regtest`。





- Bitcoin.node**：指定 LND 应连接的 Bitcoin 节点类型。





- Bitcoin.rpcuser** 和 **Bitcoin.rpcpassword** ：代表。


分别连接到 Bitcoin 节点的登录名（用户、密码





- bitcoind.zmqpubrawblock** 和 **bitcoind.zmqpubrawtx**：分别定义 ZeroMQ 端点，用于接收 Bitcoin 网络上新区块和事务的通知。




## 使用 LND 检查安装情况



您可能需要确保进程已成功完成，并与 Lightning Network 同步，以保持节点信息的最新状态。



要启动 LND 执行程序并获取节点信息，只需键入命令 ：


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## 在 LND 上执行操作



安装完成并检查无误后，即可开始使用。


以下是开始使用的基本命令。



### 创建投资组合


您的 "闪电 "投资组合是任何资金管理行动的第一步。



⚠️ **重要**：仔细记下您的 24 字 **seed 短语**。如果出现问题，您需要它来收回资金。



同时保存 Wallet 密码，以便重启 LND 节点时使用 `lncli unlock` 命令解锁。



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### 查看余额



直接从终端查询您的账户：



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### 节点信息



使用下面的命令找出节点上激活的频道。



```bash
lncli listchannels
```



您还可以获取所连接节点的列表。



```bash
lncli listpeers
```



### 渠道管理



通过 "闪电 "通道，您可以与 Lightning Network 上的另一个节点**直接、成对连接。在该通道中，您可以自由使用 Exchange Satoshis，但不得超过通道的容量。



### 连接到节点



如果您想积极参与并受益于 "闪电 "的强大功能，连接到其他 "闪电 "节点是一项基本行动。



要连接到一个对等体（闪电节点），你需要三条信息：




- 节点的公钥**：这是节点在 Bitcoin 网络中的唯一标识符；
- IP** ：安装节点的机器 IP；
- 端口** ：  机器上允许与该节点通信的开放端口。



你可以在 [amboss](https://amboss.space/) 上找到要连接的节点，这是一个列出 Lightning 节点信息的平台。



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




确保连接到**可靠的节点**，以维护自身系统的完整性。以下是一些选择正确连接的建议。





- 地域多样化**：连接不同地区的节点。





- 信誉**：选择可用性好的节点。





- 容量**：选择流动性好的绳结。





- 收费**：支票路由费。


### 开通支付渠道


要打开支付通道，请确保您已**连接**到对等节点，然后定义您希望在此通道中封锁的**容量**（卫星数量）。



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### 创建闪电 Invoice



Lightning Invoice 表示一串字符，表达您希望在 Lightning Wallet 中收到卫星币的愿望。


使用自己的节点创建 "闪电 "发票可以保护您的数据（地理和个人数据），让您对资金管理拥有 100% 的自主权。



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### 支付闪电 Invoice



```bash
lncli payinvoice <FACTURE>
```


### 关闭通道



有两种方法可以关闭当前节点上的活动通道。





- 合作关闭**：这表示你的节点希望退出支付渠道，确保正在进行的任务已完成，数据已备份，以避免资金损失。


```
lncli closechannel <ID_CANAL>
```




- 强制关闭**：⚠️ 尽可能避免使用，因为这种操作会中断您支付渠道中正在进行的流程，并增加损失资金的风险。


```
lncli closechannel --force <ID_CANAL>
```


## LND 节点的最佳实践和安全性。


使用 Bitcoin/ Lightning 节点时，安全至关重要。以下几点可加强安装的安全性：





- 将您的 "seed 短语 "保存在安全的离线位置。





- 定期备份 `~/.LND/channel.backup` 文件：每次在节点上打开新通道（或关闭旧通道）时，该文件都会保存通道状态。


⚠️ 允许您在数据丢失或节点故障的情况下恢复通道并恢复支付通道中被冻结的资金



您可以使用下面的命令，通过指定该文件的备份路径来恢复您的资金：


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- 确保保存了 Lightning Wallet 的还原词和密码。
- 及时更新系统。



## 当前故障排除


### 经常出现的问题




- bitcoind 连接错误** ：检查您的 RPC 登录信息
- 同步受阻** ：检查您的互联网连接
- 权限错误**：检查文件夹 `~/.LND` 的权限




本教程到此结束。如果您想了解更多有关 "闪电 "的信息，我们将为您提供入门课程，让您更好地了解 Lightning Network 背后的概念和实践。




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb