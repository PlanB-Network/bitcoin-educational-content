---
name: Coinjoin 协调员 - WabiSabi
description: 如何按照 WabiSabi 协议（在 Wasabi Wallet 2.0 中使用）设置和运行硬币连接协调器
---

![cover](assets/cover.webp)


---

## 导言 👋


在本专家指南中，我们将帮助您设置一个 Coinjoin 协调员，本质上是一个服务器，它将希望在合作交易中节省交易费用或增加链上隐私的人聚集在一起。由于 Wasabi Wallet 不再捆绑公司运行的协调器，用户必须寻找并选择自己喜欢的协调器服务器。只有少数协调者要求收取 0% 的协调费，因此 Wasabi Wallet 的开发者一直在努力使运行自己的社区协调者变得尽可能简单（在小到 Raspberry Pi5 的硬件上！）。目前活跃的要求 0% 协调费的协调人可以在 [LiquiSabi](https://liquisabi.com) 上找到，更重要的是可以在 [nostr](https://github.com/Kukks/WasabiNostr) 上找到。


## 要求 🫴



- VPS（托管节点）或计算机/服务器（自托管节点）
- 经修剪/完整的 Bitcoin 核心节点（使用 v29.0 进行测试）


可选：


- (将流量转发至节点的（子）域（例如：coinjoin.[yourdomain].io）


由于并非所有步骤都能自动执行，建议您具备一定的命令行提示和 bash 操作经验。


硬件方面，建议系统配备


- 4 个内核
- 16 GB 内存
- 2 TB SSD 或 NVMe（用于全节点）/ 128 GB SSD（用于 pruned 节点）


Raspberry Pi 5 只需 120 美元就能满足这些要求，其中不包括存储设备，2TB NVMe 存储棒的价格约为 100 美元。


廉价的 VPS 通常只有 1 个内核和 4GB 内存，我发现这对于同步和验证区块高度为 911817 的整个比特币 blockchain 来说太少了。


存储方面，全节点至少需要 2TB 磁盘存储，最好是 SSD 或 NVMe 类型。在修剪 blockchain 时，可以使用更小的存储驱动器（如 128GB SSD）。


如果您打算运行一个协调器来处理大型（300 个以上输入）的硬币拼接，建议您选择一个具有更快/更新内核的系统，它具有更高的性能来进行所有签名验证。


## 安装 🛠️


在节点上，我们要下载并安装最新发布的 Wasabi Wallet 版本，其中包括后台和协调器，作为 wallet 旁边的独立可执行文件。


查找最新版本：[Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) 并使用密钥验证该版本的 PGP 签名：[PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


部署细节因硬件（CPU 架构）和操作系统的选择而异，下面给出的是以基于 Debian 的 RaspiBlitz 为起点的 Raspberry Pi（ARM-64）的不同细节。跳转至使用 Nix 部署（X86-64）Ubuntu 操作系统。


请在此处查找安装说明：[Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### 部署 RaspiBlitz/Debian


对于 RaspiBlitz（经 v1.11 测试）节点，可使用从源代码构建的部署 script：[home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### 轻松部署


对于最低限度的部署，您只需将平台的可执行文件解压缩到一个文件夹中即可。

Debian/Ubuntu 的命令行代码示例：


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


这样就会产生以下有效的签名信息：


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


然后就可以安装下载的软件包了：


```
sudo apt install ./Wasabi-2.7.2.deb
```



## 配置 🧾


在运行协调器之前，您需要编辑 Config.json 文件：


- Bitcoin RPC 全权证书
- 首选回合参数
- 协调员扩展公钥（创建新的 SegWit wallet，用于接收收集到的灰尘）

**警告**：Taproot wallet 将导致 UTXO 无法使用！在此使用本地 Segwit wallet。


- 允许的输入和输出地址类型
- 通过 nostr 发布的播报员配置（名称、描述、Uri、最小输入、nostr 中继、nostr 私钥）


您可以运行只能通过 .onion 地址访问的协调器，也可以使用您自定义的 clearnet 域名。


在此路径上查找或创建配置文件：


`~/.walletwasabi/coordinator/Config.json`.


用命令进行编辑：


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


请参见 Config.json 示例：


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Tor 配置 🧅


要填写你的 OnionServicePrivateKey，你可能需要先生成一个。


如果第一次运行 Wasabi Wallet 时在 Config.json 文件中设置了 ``"PublishAsOnionService":true,```，Wasabi Wallet 就会为你生成私钥。


用命令运行一次协调员：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


要查看洋葱隐藏服务地址，请使用以下方法查看协调程序日志：


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


你会发现类似的内容：


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


以 .onion 结尾的长 URL 是您的隐藏服务地址或 CoordinatorUri。


或再次检查协调器配置文件：


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


现在应自动填写。


## 运行 ⚡


设置好所有配置参数后，您就可以运行协调器服务，开始宣布第一轮 🕶️


只需执行命令启动协调器即可：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


您可以通过检查（在 Tor 浏览器中检查 .onion）来监控当前回合和已注册 UTXO 的数量：


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### 可选：调试协调器服务器


您可以在 ```~/.walletwasabi/backend/Logs.txt``` 的日志文件中监控任何问题或错误。


典型问题包括 RPC 连接问题，必须在 ```~/.bitcoin/bitcoin.conf``` 中启用：


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### 可选：运行后端服务器


与协调器一起，您还可以为没有自己比特币节点的用户提供一个后台服务器，以连接到该服务器，进行费用估算和区块过滤。


用命令启动该服务：


```
wbackend
```


## 邀请 Wasabi 用户到您的协调员 🫂


要让其他用户找到您的服务，您可以依靠 nostr 播报器，或者共享一个带有您的域名（clearnet）或隐藏服务（.onion 链接）的神奇链接，并像这样设置参数：


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


当用户复制魔法链接并打开 Wasabi Wallet 时，软件将自动显示带有您的域和参数的协调器对话框。


![detected](assets/en/02.webp)


💚🍣 祝贺比特币隐私去中心化 🕶️


记住你的训练 [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika)，Wasabi Wallet 只用于防御 🛡️