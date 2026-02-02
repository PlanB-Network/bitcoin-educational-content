---
name: Joinstr
description: 通过 Nostr 网络实现去中心化 CoinJoins，实现主权 Bitcoin 保密性
---

![cover](assets/cover.webp)



Bitcoin 区块链的透明度使得追踪交易历史成为可能。CoinJoins 通过将多个同时进行的交易混合在一起，打破了这些联系，恢复了与现金相当的保密性。



然而，传统的解决方案依赖于作为单点故障的中央协调员。迫于监管压力，Wasabi 和 Samourai 于 2024 年停止运营。



**Joinstr**通过使用去中心化的Nostr网络进行协调，消除了这一弱点。这一开源应用程序实现了真正的主权 CoinJoins，任何中央机构都无法审查、监控或中断服务。



## 什么是 Joinstr？



Joinstr 是一个开源工具，它利用 Nostr 协议作为协调基础设施，彻底改变了 CoinJoins 方法。与需要专用服务器的集中式解决方案不同，Joinstr 依靠由 Nostr 中继器组成的分布式网络，使参与者能够直接在同行之间进行协调。



**非集中式架构** ：Nostr 网络取代了中央协调员。参与者通过 Nostr 中继器发布加密公告，创建或加入 "池"。这些信息（金额、参与者、地址）对中继器来说是不可理解的，从而确保任何中央实体都无法监控、审查或过滤 CoinJoins。



**SIGHASH_ALL|ANYONECANPAY 机制**：Joinstr 利用这个 Bitcoin 签名标志，允许每个参与者只签署自己的输入，同时验证所有输出。每个用户在本地生成自己的 PSBT，然后通过 Nostr 发布。每个用户在本地生成自己的 PSBT，签名后通过 Nostr 发布。在最终签名之前，您的比特币一直由您全权控制。



**Philosophy**：Joinstr 遵循 Bitcoin 加密朋克精神，旨在实现三个目标： **抵制审查**（任何机构都不能停止服务）、**完全非监禁**（你可以保留自己的私钥）和**平等待遇**（任何 UTXO 都不能受到歧视）。



### 主要特点



**灵活的彩池**：与固定面额不同，任何用户都可以创建一个具有所需精确金额和目标参与人数的资金池，从而优化 UTXO 的使用，而无需人为拆分。



**收费透明**：无协调费。参与者只需平摊 Bitcoin 交易费（每人几千萨托什）。



**短暂性**：不保留用户数据。信息通过加密的短暂 Nostr 信息传输，交易后立即被遗忘。



### 可用平台



本教程重点介绍**Android 应用程序**，这是目前唯一稳定且值得推荐的解决方案。Electrum 插件已经存在，但因兼容性问题而不稳定。网络界面正在开发中。



## Bitcoin 核心配置



Joinstr Android 需要通过 RPC 连接到 Bitcoin 节点。您必须先在电脑上配置 Bitcoin Core，以接受来自手机的连接。



**注意**：有关 Bitcoin Core 完整配置的更多详情，请参阅我们的专门教程 ：



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### 网络要求



#### 查找本地 IP 地址



您的 Android 手机必须能够连接到本地网络上的 Bitcoin 节点。查找计算机的 IP 地址：



**在 macOS 上** ：



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



简单的替代方案：



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**在 Linux 上** ：



```bash
hostname -I | awk '{print $1}'
```



**在 Windows 上** ：



```cmd
ipconfig
```



查找 IPv4 地址（格式为 "192.168.x.x "或 "10.0.x.x"）。



### RPC 配置



#### 编辑 bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



找到您的 `bitcoin.conf` 文件：




- Linux**：`~/.bitcoin/bitcoin.conf
- macOS**：`~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**：`%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



使用您喜欢的文本编辑器打开文件，添加此配置以激活 RPC 服务器。



**入门推荐配置（书签）** ：



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet** 配置（用于生产） ：



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**重要** ：




- 强烈建议**使用 Signet 进行首次测试：该应用程序仍处于开发阶段（测试版），可能仍存在错误。Signet 可让您免费测试，无实际资金风险
- 将 `192.168.1.0/24` 替换为您的网络子网（例如，如果您的 IP 地址是 `192.168.68.57`，则使用 `192.168.68.0/24`）。



**安全**：生成强大的密码：



```bash
openssl rand -base64 32
```



### 初始化



#### 重新启动并检查



1.完全关闭 Bitcoin 核心


2.重新启动以应用配置




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



当 Bitcoin Core 首次启动时，它将下载并同步书签区块链。这一操作比 mainnet 快得多（只需几分钟）。请等待同步完成后再继续操作。



![CRÉATION DE WALLET](assets/fr/04.webp)



同步后，点击 "创建一个新的 wallet"，创建一个新的投资组合。给它取一个明确的名称，如 "tuto_joinstr_signet"。



![WALLET CRÉÉ](assets/fr/05.webp)



您的 wallet 现已创建，可随时接收书签比特币进行测试。



#### 获取书签比特币（测试）



要在书签上测试 Joinstr，您需要免费测试比特币：



![SIGNET FAUCET](assets/fr/06.webp)



使用公共书签，如 ：




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



在 Bitcoin Core 中，generate 新建一个接收地址（"接收 "选项卡），将其复制并粘贴到龙头表单中。如有必要，请解决验证码问题。您将在几秒钟内收到免费的书签比特币。



## 安卓应用程序



### 安装



![APPLICATION ANDROID](assets/fr/07.webp)



前往 [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) 下载最新的 APK 版本。在 Android 浏览器上下载文件，然后打开文件启动安装。如有必要，你需要在手机的安全设置中允许从未知来源安装。



### 应用程序配置



![PERMISSIONS VPN](assets/fr/08.webp)



第一次启动时，Joinstr 应用程序会要求控制内置 VPN 的权限。接受兩個權限要求：OpenVPN 控制和 VPN 連線。VPN 整合需要這些權限，以保護你的網路隱私。



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstr 应用程序分为三个主要选项卡：




- 主页**：主屏幕
- 池**：创建和管理 CoinJoin 池
- 设置**：应用程序配置



![CONFIGURATION SETTINGS](assets/fr/13.webp)



在 "设置 "选项卡中配置设置：



**1.Nostr 中继**：用于池协调的 Nostr 中继地址




- 例如：`wss://relay.damus.io`。
- 其他推荐中继站：`wss://nos.lol`、`wss://relay.nostr.band`、`wss://nostr.fmt.wiz.biz`。
- ⚠️ **重要**：所有参与者必须使用**个相同的 Nostr 中继**才能看到和加入相同的池。如果您使用不同的中继，将无法看到在其他中继上创建的池



**2.节点 URL**：Bitcoin 节点的 IP 地址（不含端口）




- 格式：http://VOTRE_IP_LOCALE
- Example: `http://192.168.68.57`



**3.RPC 用户名** ：在 bitcoin.conf 上的 `rpcuser=` 中配置的用户名




- 例如：`satoshi



**4.RPC 密码** ：在 bitcoin.conf 上的 `rpcpassword=` 中设置的密码



**5.RPC 端口** ：RPC 端口取决于网络




- Mainnet** ：`8332`
- 书签**：`38332`



**6.Wallet**：选择包含要混合的UTXO 的 Bitcoin 核心组合




- 示例：`tuto_joinstr_signet



**7.VPN 网关**：选择 Riseup VPN 服务器




- 例如："(巴黎) vpn07-par.riseup.net
- 其他可用：阿姆斯特丹、西雅图等
- ⚠️ **重要**：同组的所有参赛者必须使用**相同的 VPN 网关**参加 CoinJoin。在混合轮中，所有参赛者必须使用相同的出口 IP 地址，以防止网络分析将参赛者关联起来



Joinstr 应用程序**与 Riseup VPN 原生集成**，简化了参与者之间的协调。



**重要** ：




- 确保手机和电脑处于同一个本地 WiFi 网络中
- 当参与网络池时，VPN 连接将自动激活。
- 设置完所有参数后，点击 **"保存 "**。



## 实际用途



### 创建或加入人才库



![CRÉATION POOL ANDROID](assets/fr/10.webp)



参加 CoinJoin 有两种选择：



**方案 1：创建一个新池**



点击 "池 "选项卡中的 "创建新池"。指定以 BTC 为单位的面值（例如 0.002 BTC）和所需的参与者人数（最少 2 人，为提高匿名性，建议 3-5 人）。然后，应用程序会等待其他用户加入您的资金池。一旦达到所需的人数，输出注册过程就会自动开始，您需要选择要混合的 UTXO，然后点击 "注册"。



**⏱️ 重要**：池在**10 分钟**未活动后失效。如果未达到所需的参与人数，报名池将自动关闭。



**备选方案 2：加入现有人才库**



在 "查看其他资金池 "选项卡中，浏览其他用户创建的可用资金池。选择一个与您的金额相对应的池并加入。确保您配置了与其他参与者相同的 Nostr 中继和 VPN 网关（请参阅 "配置 "部分）。



**UTXO 选择规则**：您的 UTXO 必须略高于彩池面值（sats 盈余在 +500 至 +5000 之间）。



**例如**：对于 0.002 BTC（200,000 sats）的资金池，使用介于 200,500 和 205,000 sats 之间的 UTXO。



![PROCESSUS COINJOIN](assets/fr/11.webp)



整个过程**完全自动**：一旦您的输入完成注册，应用程序就会等待所有参与者注册他们的输入。一旦所有输入都已注册，PSBT 就会创建，并自动用您的密钥签名，然后与其他参与者的签名合并。最后，在 Bitcoin 网络上广播完整的交易。广播完成后，您会收到 TXID（交易标识符）。安卓系统无需手动操作 PSBT。



### on-chain 核查



![TRANSACTION MEMPOOL](assets/fr/12.webp)



交易广播后，您将收到 TXID（交易标识符）。在 [mempool.space](https://mempool.space) 或您喜欢的浏览器上查看。要在书签上测试，请使用 [mempool.space/signet](https://mempool.space/signet)。



您可以观察到 ：





- N 个参赛**：每位参赛者一份（例如，2 份参赛作品）
- N 个相同的输出**：面额的确切金额（此处为 2 个输出，每个输出 0.00199800 BTC）
- 流程图**：mempool.space 直观显示输入和输出的混合情况
- 特点** ：交易可识别为 SegWit、Taproot、RBF 等。



由于所有主要输出的数量相同，因此**不可能确定哪个属于哪个**。这就是 CoinJoin 的基本原则：输出不可区分。



**Exemple de transaction signet** ：[404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**请注意**：如果您的 UTXO 大于资金池面额，您将有外汇输出（盈余）。这些外汇 UTXO 仍可追踪，必须与您的匿名输出分开管理。切勿将其与混合输出合并。



## CoinJoin 质量和匿名包



CoinJoin 的效率是通过其**anonset**来衡量的：交易产生的相同价值的产出数量。这个数字越高，就越难确定哪个输入对应哪个输出。



Joinstr 目前平均产生 2 到 5 个参与者**。这些数字低于传统的集中式协调者，如 Wasabi（50-100 人）或 Whirlpool（5-10 人），但这就是分散化的代价。



💡 **要详细了解匿名集及其计算**，请参阅我们的完整课程：[匿名集](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431)。



### Joinstr 与其他 CoinJoins 的比较




| 方面 | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **每个池的参与者** | 50-100 | 5-10 | 可变 (P2P) | **2-5** |
| **协调员** | 中央集中（2024年关闭） | 中央集中（活跃） | P2P maker/taker | **无 (Nostr)** |
| **抗审查性** | 弱 | 中 | 很高 | **很高** |
| **协调费用** | 百分比 | 入场费 | 支付给制造者 | **无** |
| **UTXO歧视** | 是（黑名单） | 否 | 否 | **否** |

💡 **其他活性 CoinJoin 溶液** ：




- Ashigaru**：Whirlpool 协议的开源实施，由中央协调人员负责，但可以分散部署。在 2024 年夺取 Samourai Wallet 后继续运行。
- JoinMarket**：去中心化的 P2P 解决方案，不设中央协调人，基于制造者/接受者商业模式，由 "制造者 "提供流动性，并由 "接受者 "支付报酬。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**基本权衡**：Joinstr 和 JoinMarket 是仅有的两个没有中央协调人的解决方案。JoinMarket 采用 P2P 商业模式，有经济激励机制，而 Joinstr 则使用 Nostr 进行无成本协调。Joinstr 牺牲了即时的大规模匿名性，以换取简单性（无制造者/接受者管理）和完全无协调费用。



**实用建议**：为弥补参赛人数较少的不足，可使用不同的参赛者连续进行几轮 CoinJoin。在每轮比赛之间间隔开来并更换诺斯特接力，以最大限度地提高保密性。



有关比特币隐私的更多信息，请随时查阅我们的完整课程：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 优势和局限性



### 亮点



**增强隐私**：结合 Nostr 通信加密、参与者之间共享 VPN 以及建议使用 Tor，可提供难以绕过的多层保护。



**透明、成本最低**：没有协调费用，只有 mining 费用由参与者公平分担。任何运营商都不征收百分比。



### 需要考虑的制约因素





- 可变流动性**：资金池规模较小，可以等待参与者聚集在一起
- 项目进行中**：应用程序处于测试阶段，可能存在错误。先在书签上进行少量测试
- 假冒攻击**：一个对手可能控制多个现金池参与者



## 最佳做法



**UTXO 隔离**：切勿将混合的 UTXO 与未混合的 UTXO 混合。为匿名输出使用单独的组合。



**必须进行多轮**：与不同的参与者至少连续进行 3 轮。改变数量和时间，避免模式化。每轮间隔几个小时。



**网络保护**：除内置 VPN 外，系统地使用 Tor。为每次重要会话生成短暂的 Nostr 密钥。



**谨慎进步**：从少量开始收藏书签。



## 结论



Joinstr 代表了真正去中心化的 Bitcoin 隐私解决方案。通过使用 Nostr 进行协调，它消除了对中央协调者的依赖，同时维护了用户主权。



**适用于重视抵制审查，并准备执行多轮 CoinJoin 以弥补较小资源池的用户。



在金融审查日益严格的背景下，保护隐私的去中心化工具变得至关重要。



## 资源



### 正式文件




- [Joinstr官方网站](https://joinstr.xyz)
- [用户文档](https://docs.joinstr.xyz/users/using-joinstr)
- [技术文件](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab源代码](https://gitlab.com/invincible-privacy/joinstr)
- [安卓应用程序](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### 教程




- [Electrum 插件教程](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - 完整指南 作者：Uncensored Tech



### 社区和支持




- [Telegram Joinstr Group](https://t.me/joinstr) - 社区支持和书签角
- [关于 DelvingBitcoin 的技术讨论](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### 附加工具




- [Bookmark Faucet](https://signetfaucet.com) - 免费测试比特币
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet 替代品
- [Mempool.space](https://mempool.space) - 含隐私分析的 Block explorer