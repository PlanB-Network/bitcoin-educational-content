---
name: Lightning Watchtower
description: 了解并在 Lightning 节点上使用 Watchtower
---
![cover](assets/cover.webp)



## 守望塔如何运作？



作为 Lightning Network 生态系统的重要组成部分，_Watchtowers_ 为用户的 "闪电 "频道提供额外的保护。它们的主要作用是监控频道状态，并在频道一方试图欺骗另一方时进行干预。



Watchtower 如何确定通道是否已被入侵？它从客户（通道的其中一方）那里获得正确识别和处理任何违规行为所需的信息。这些信息包括最近交易的详细信息、通道的当前状态以及创建惩罚交易所需的 Elements。在向 Watchtower 传输这些数据之前，客户可以对其进行加密，以保持机密性。因此，即使 Watchtower 收到数据，也无法解密，直到违规事件真正发生。这种加密机制可以保护客户的隐私，防止 Watchtower 在未经授权的情况下获取敏感信息。



在本教程中，我们将介绍使用 **Watchtower** ：




- 首先，通过 LND 采用经典的原始方法、
- 然后再用 Satoshi 之眼另辟蹊径、
- 最后，在使用 Umbrel 托管的 Lightning 节点上简化配置 Watchtower。



## 1 - 通过 LND 配置 Watchtower 或客户端



*本教程摘自 [LND 官方文档](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md)。原始版本可能有一些改动



自v0.7.0起，`LND`支持执行私人利他Watchtower，作为`LND`的一个完全集成的子系统。当客户节点离线或无法响应时，"瞭望塔 "可提供第二道防线，防止恶意或意外入侵，从而提高渠道资金的安全级别。



奖赏瞭望塔要求从频道资金中分一杯羹作为服务回报，与之不同的是，利他主义瞭望塔不收取佣金，而是返还受害者的所有资金（扣除 On-Chain 费用）。奖励瞭望塔将在以后的版本中启用，目前仍处于测试和改进阶段。



此外，"LND "现在可以被配置为 "瞭望塔客户端"，保存来自其他利他瞭望塔的加密违规补救事务（即所谓的 "正义事务"）。Watchtower 存储固定大小的加密 Blob，只有在违规方广播撤销 Commitment 状态后，才能解密和发布正义交易。客户与 Watchtower 之间的通信使用短暂密钥对进行加密和验证，这限制了 Watchtower 通过长期凭证追踪客户的能力。



请注意，我们选择在此版本中部署一组有限的功能，这些功能已为`LND`用户提供了重要的安全性。许多其他与 Watchtower 相关的功能要么已接近完成，要么进展顺利；我们将继续在测试过程中提供这些功能，一旦这些功能被认为是安全的，我们将立即提供。



注意：目前，瞭望塔只保存已撤销承诺的 `too_local` 和 `too_remote` 输出；保存 HTLC 输出将在未来版本中部署，因为协议可以扩展到包括加密 blob 中的附加签名数据。



### 配置 Watchtower



要设置 Watchtower，命令行用户需要编译可选的 `watchtowerrpc` 子服务器，它允许通过 gRPC 或 `lncli` 与 Watchtower 交互。已发布的二进制文件默认包含 `watchtowerrpc` 子服务器。



激活 Watchtower 的最低配置为 `Watchtower.active=1`。



您可以使用 `lncli tower info` 检索 Watchtower 配置信息：



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



可通过 `LND -h` 获取全部 Watchtower 配置选项：



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### 监听界面



默认情况下，Watchtower 监听`:9911`，对应所有可用接口上的端口`9911`。用户可以通过 `--Watchtower.listen=` 选项定义自己的监听接口。您可以在 `lncli tower info` 的 `"listeners"` 字段中检查您的配置。如果您在连接 Watchtower 时遇到问题，请确保`<port>`已打开，或您的代理已正确配置为激活的 Interface。



#### 外部 IP 地址



用户还可以使用 `Watchtower.externalip=`指定 Watchtower 的外部 IP Address（es），通过 RPC 或 `lncli tower info` 显示 Watchtower 的完整 URI（pubkey@host:port）：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI 可通过以下命令发送给客户连接和使用：



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



如果 Watchtower 客户需要远程访问，请确保 ：




- 打开 9911 端口（或通过 `Watchtower.listen`定义的端口）。
- 使用代理将开放端口的流量重定向到 Watchtower 的监听 Address。



#### Tor 隐藏服务



Watchtowers 支持 Tor 隐藏服务，并可通过以下选项在启动时自动 generate：



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



然后，.onion Address 会出现在 `lncli tower info` 查询的 `"uris"` 字段中：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



注：Watchtower 公钥与 `LND` 节点的公钥不同。目前，它的作用是 "Soft 白名单"，因为客户需要知道 Watchtower 的公钥才能将其用作备份，以等待更高级的白名单机制。我们建议您不要公开披露这个公钥，除非您准备将 Watchtower 暴露在整个互联网上。



#### Watchtower 数据库目录



可以使用 `Watchtower.towerdir=` 选项移动 Watchtower 数据库。请注意，所选路径将添加后缀 `Bitcoin/Mainnet/Watchtower.db`，以便通过字符串隔离数据库。因此，设置 `Watchtower.towerdir=/path/to/towerdir` 将在 `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`产生一个数据库。



例如，在 Linux 下，Watchtower 的默认数据库位于 ：


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### 配置 Watchtower 客户端



要配置 Watchtower 客户端，您需要两样东西：





- 使用 `--wtclient.active` 选项激活 Watchtower 客户端。



```shell
$  lnd --wtclient.active
```





- 活动 Watchtower 的 URI。



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



您可以用这种方法配置多个瞭望塔。



#### 法律事务收费标准



用户可通过 `wtclient.sweep-fee-rate`选项选择性地设置正义交易的收费率，该选项接受以 sat/byte 为单位的值。默认值为 10 sat/字节，但也可以设定更高的费率，以便在收费高峰期获得更高的优先级。更改 `sweep-fee-rate` 适用于 daemon 重启后的所有新更新。



#### 监督



通过 `lncli wtclient` 命令，用户现在可以直接与 Watchtower 客户端交互，获取或修改所有已注册瞭望塔的信息。



例如，使用 `lncli wtclient tower`，您可以找出当前与上面添加的 Watchtower 协商的会话数量，并通过`active_session_candidate`字段确定它是否用于备份。



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



要获取 Watchtower 会话的信息，请使用 `--include_sessions` 选项。



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



所有 Watchtower 客户端配置选项均可通过 `lncli wtclient -h` 获取：



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - 安装自己的 Satoshi Eye



*本教程部分摘自[Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/)上的一篇文章。对原始版本进行了修改*。



Satoshi 之眼（[Rust-TEOS](https://github.com/talaia-labs/Rust-teos)）是一种非存储型 Watchtower 闪电，符合[Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)。它由两个主要部分组成：





- teos**：包括命令行 Interface（CLI）和 Watchtower 的基本服务器功能。编译该_crate_时会产生两个二进制文件--**teosd**和**teos-CLI**。





- teos-common**：包括共享的服务器端和客户端功能（对创建客户端很有用）。



要正确运行 Watchtower，需要先运行 **bitcoind**，然后再使用 **teosd** 命令启动 Watchtower。在运行这两个命令之前，您需要配置**Bitcoin.conf**文件。具体方法如下





- 从源代码安装或下载 Bitcoin core。下载后，将 **Bitcoin.conf** 文件放到 Bitcoin core 用户目录下。有关文件放置位置的详细信息，请参阅此链接，因为这取决于所使用的操作系统。





- 确定位置后，添加以下选项：



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- 服务器**：用于 RPC 请求





- rpcuser** 和 **rpcpassword**：验证 RPC 客户端到服务器的身份





- regtest**：不是必填项，但在计划开发时很有用。



**rpcuser** 和 **rpcpassword** 的值由您选择。书写时必须去掉引号。例如



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



现在，如果运行 **bitcoind**，节点就会启动。





- 对于 Watchtower 部分，您必须首先从源代码中安装 **teos**。请按照此链接中的说明进行操作。





- 在系统上成功安装**teos**并运行测试后，就可以进入最后一步：在 teos 用户目录下设置**teos.toml**文件。该文件应放在主目录下名为 **.teos**（注意圆点）的文件夹中。例如，Linux 下为 **/home//.teos**。找到位置后，创建一个**teos.toml**文件，并根据**bitcoind**上的更改设置这些选项：



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



请注意，这里的用户名和密码必须**带引号**。使用前面的示例 ：



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



完成上述操作后，就可以启动 Watchtower。由于我们在**regtest**上运行，因此当 Watchtower 首次连接时，Bitcoin 测试网络上可能没有区块被挖掘（如果有，那就有问题了）。Watchtower 会对**bitcoind**的最后 100 个区块建立内部缓存；因此，首次启动时可能会出现以下错误：



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



由于我们使用的是 **regtest**，因此只需发出一条 RPC 命令即可实现 Miner 区块，而无需等待其他网络（如 Mainnet 或 Testnet）上的中位 10 分钟延迟。有关如何 Miner 区块的详细信息，请参阅 **bitcoin-cli** 帮助。



![Image](assets/fr/01.webp)



仅此而已：您已成功运行 Watchtower。恭喜您。🎉




## 3 - 在 Umbrel 上配置 Watchtower



在 Umbrel 上，连接 Watchtower 以保护您的 "闪电 "节点非常简单，因为所有操作都是通过图形化 Interface 完成的。远程连接到节点后，打开 "**闪电节点**"应用程序。



![Image](assets/fr/02.webp)



点击 Interface 右上方的三个小圆点，然后选择 "**高级设置**"。



![Image](assets/fr/03.webp)



在 "**Watchtower**"菜单中有两个选项：





- Watchtower 服务**：该选项可让您运行 Watchtower，即监控其他节点通道以侦测任何欺诈企图的服务。如果出现漏洞，您的 Watchtower 会在 Blockchain 上发布交易信息，使用户能够找回被锁定的资金。一旦激活，您的 Watchtower 的 URI 就会出现，并可传达给其他节点，以便它们将其添加到自己的 Watchtower 客户端；





- Watchtower 客户端**：该选项可让您连接外部瞭望塔，保护自己的频道。激活后，您可以添加 Watchtower 服务，您的节点将向其传输有关其频道的必要信息。这些监控塔将监控它们的状态，并在出现欺诈企图时进行干预。



当然，您的首要任务是激活 *Watchtower Client* 以保护您的节点，但我也建议您激活 *Watchtower Service* 以换取其他用户的安全。



![Image](assets/fr/04.webp)



然后点击 Green 的 "**保存并重新启动节点**"按钮。您的 LND 将重新启动。



如果您已激活 Watchtower 服务，还可在同一菜单中找到该服务的 URI。您还可以添加外部 Watchtower 的 URI 以保护您的频道。点击 "**ADD**"确认。



![Image](assets/fr/05.webp)



网上有多个守望先锋。例如，[LN+ 和 Voltage 提供利他的 Watchtower](https://lightningnetwork.plus/Watchtower)，您可以与之连接：



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



另一种方法是与其他比特币用户一起 Exchange Watchtower URI，这样每个人都可以保护对方的节点。



我还建议您设立多个瞭望塔，以降低其中一个无法使用时的风险。



最后，您可以调整 "**Watchtower 客户端扫描费率**"参数。这定义了您愿意为 Watchtower 广播惩罚交易支付的最高费率，以便将其纳入区块。请确保设置一个足够高的值，以适应您通道中锁定的金额。