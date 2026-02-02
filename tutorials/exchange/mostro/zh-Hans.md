---
name: Mostro
description: 通过 Lightning 和 Nostr 实现免 KYC 的 Bitcoin P2P 交易所平台
---

![cover](assets/cover.webp)



如何在不损害金融主权的情况下获取或出售比特币？集中式平台会对你的个人数据实施侵入性的 KYC 程序，并有可能任意冻结账户或进行国家监控。



**Mostro P2P** 提供了一种结合 Lightning Network、Nostr 协议和持有发票的去中心化替代方案。它的主要创新点是：自动托管系统，在整个交换过程中，您的比特币始终处于您的控制之下，消除了盗窃、交易所破产或任意没收的风险。



## 什么是 Mostro P2P？



Mostro P2P 是一种开源的 Bitcoin 交换协议，由**grunch**创建，他是 2021 年推出的流行 Telegram 机器人**lnp2pbot**的开发者。虽然lnp2pbot已经通过Lightning实现了无KYC的P2P交易所，但它存在一个重大漏洞： **Telegram是一个集中式故障点**，容易受到政府的审查。



Mostro代表了这一概念的**去中心化演进**：通过用**Nostr**协议（一个不可感知的分布式中继网络）取代Telegram，Mostro消除了这一系统性风险。该协议结合了用于即时交易的 Lightning Network、用于抗审查通信的 Nostr 和**持有发票**，从而创建了一个真正的非托管自动托管。



### 技术架构



Mostro 的工作由三个部分组成：




- Daemon Mostrod**：协调用户与 Lightning Network 之间的交流
- 闪电**节点：创建持有发票（约 24 小时加密托管）
- Mostro** 客户：用户界面（CLI、移动、网络）



订单在 Nostr 上以公共事件（类型 38383）的形式发布，而私人交易则通过端对端加密信息（NIP-59、NIP-44）传输。每个 Mostro 实例都定义了自己的费用（一般在 0.3% 到 1% 之间）和交易限额（从几千到几十万 sats 不等，视实例而定）。



### 决定性优势



**抗审查**：只要世界上还有 Nostr 中继站，任何政府都无法关闭 Mostro。与通过 Telegram 进行的易受攻击的 lnp2pbot 不同，Mostro 允许进行**防审查**的交换。



**非托管**：闪电持有发票锁定您的比特币，而不会将其永久转移。您的资金仍由您控制，并在出现问题时（约 24 小时）自动返还给您。



**保密设计**：两种模式可满足您的需求。声誉模式**将您的声誉与您的 Nostr 密钥联系起来，以建立持久的信任。完全匿名模式** 使用一次性短暂密钥实现绝对匿名。



## 主要特点



**去中心化通信**：所有订单都通过加密签名事件在 Nostr 上发布。私人协商通过端到端加密信息传输，保证绝对保密。



**信誉系统**：通过迭代计算得出的 5 星评级永久存储在 Nostr 上。让您逐步建立起可靠交易商的声誉。



**分散仲裁**：发生争议时，由公正的仲裁员审查证据，并根据透明的标准做出裁决。每个争议都会生成一个唯一的 token，以便追溯。



**支付灵活**：通过 yadio.io 汇率服务支持多种法定货币。接受 SEPA 转账、PayPal、Revolut、现金以及双方商定的任何方式。



## 可为 Mostro 客户提供服务



Mostro 为您的 P2P 交易所提供两种主要的操作客户端。



### Mostro CLI - 命令行客户端



**Mostro CLI** 是最成熟、功能最强大的客户端。它以 Rust 编写，通过命令行界面提供 Mostro 的全部功能。兼容 macOS、Linux 和 Windows。



**主要控制** ：




- 列表订单显示所有可用订单
- neworder`：创建新的买入或卖出订单
- `takeell`/`takebuy`：接受买入或卖出指令
- 法币发送确认发送法币付款
- 释放解除托管并完成交换
- `getdm`：查看直接消息
- 汇率"：在交换后评估您的交易对手



是技术用户、自动化和需要最大安全性的环境的理想选择。



### Mostro Mobile - 智能手机应用程序



阿尔法版本的**移动应用程序**可直接通过智能手机进行 P2P 交易。直观的图形化 Interface 具有标签导航、订单查看、高级过滤器和集成聊天功能，可与交易对手进行交流。



它适用于**Android**（通过 GitHub 上的 APK），是喜欢简单和偶尔进行移动交易的用户的最佳选择。



### Mostro-web - Interface web（开发中）



Interface 高级 JavaScript 网络应用程序正在积极开发中。旨在提供完整的用户体验，具有广泛的交易和投资组合管理功能。通过浏览器访问，无需安装。



## 安装和配置



本教程将指导您安装和使用两个主要的 Mostro 客户端：CLI 和移动应用程序。



### 必要的先决条件



在开始之前，您需要 ：





- 可使用的 Lightning Network** wallet，有足够的流动资金（或与 Lightning 兼容）。
 - 推荐使用：Phoenix, Breez, Wallet of Satoshi...
 - 至少 1000 沙托希的流动资金进行测试



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- 一把 Nostr** 私钥（格式为 "nsec1......"）。
 - 在 [nostrkeygen.com](https://nostrkeygen.com/) 上创建专用交易密钥
 - 重要**：切勿使用个人 Nostr 主密钥
 - 将私人密钥保存在安全的地方（密码管理器）





- 可选但建议**：VPN 或 Tor 连接，以掩盖您的 IP 地址



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI 安装



#### 在 macOS 上



**第 1 步：Rust 检查**



检查 Rust 是否已安装（要求 1.64 以上版本）：



```bash
rustc --version
```



如果未安装 Rust ：



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**第 2 步：克隆版本库**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**第 3 步：配置**



复制并编辑.NET 文件：



```bash
cp .env-sample .env
```



打开 `.env` 并配置设置：



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**对 CLI/Mobile** 同步很重要：要在 CLI 和手机应用程序上访问相同的订单，您必须在两个客户端中使用**相同的 Mostro Pubkey** 和**相同的 Nostr 中继器**。请在移动应用程序的 "设置 "中检查这些设置。



![Configuration .env](assets/fr/02.webp)



**第 4 步：安装**



编译并安装 CLI .NET Framework：



```bash
cargo install --path .
```



编译需要 1-2 分钟。mostro-cli" 可执行文件将安装在 `~/.cargo/bin/` 中。



![Installation du CLI](assets/fr/03.webp)



**第 5 步：检查**



检查一切正常：



```bash
mostro-cli --help
```



您将看到完整的订单列表。



![Vérification avec --help](assets/fr/04.webp)



#### 在 Linux（Ubuntu/Debian）上



安装与 macOS 相同，但增加了 .NET Framework 3.0：



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



然后按照 macOS 部分的步骤 3 和 4 进行操作。



#### 在 Windows 上



首先通过 [rustup.rs](https://rustup.rs/) 安装 Rust，然后使用 PowerShell ：



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



相同配置：将 `.env-sample` 复制到 `.env`，然后填写参数。



### 安装 Mostro Mobile



#### 在安卓系统上



**步骤 1**：访问 [GitHub 发布页面](https://github.com/MostroP2P/mobile/releases) 并下载 **app-release.apk** 文件（约 65 MB）。



![Page GitHub Releases](assets/fr/10.webp)



**步骤 2：下载完成后，打开下载的 APK 文件。安卓系统会要求您授权从该来源进行安装。



![Téléchargement et installation APK](assets/fr/11.webp)



**步骤 3**：按照介绍功能的上机屏幕操作：




- 自由交易 Bitcoin - 无需 KYC** ：借助 Nostr，交易无需身份验证
- 默认隐私**：在信誉模式和完全隐私模式之间进行选择
- 每一步都安全**：提供非保管式发票保护



![Écrans d'accueil Mostro](assets/fr/12.webp)



**第 4 步**：继续入职，了解 ：




- 完全加密聊天**：端对端加密通信
- 接受报价**：浏览订单簿并选择报价
- 找不到您需要的产品吗？创建您自己的定制订单



![Suite onboarding](assets/fr/13.webp)



**第5步：一旦注册完成，应用程序会自动生成一对Nostr密钥。进入菜单（☰），然后**账户**保存你的**密语**（恢复短语）。在这个界面，你还可以选择更改之前提到的隐私模式。



![Menu et sauvegarde des clés](assets/fr/15.webp)



**重要**：将恢复短语写在安全的地方（密码管理器、纸质保险箱）。



### 初始安全配置



无论您使用什么平台 ：





- 专用密钥**：使用单独的 Nostr 身份进行交易
- 小额**：从低于 34,000 古瓦的金额开始起步
- 多个中继**：配置 3-5 个不同地理位置的中继器
- 网络保护**：激活 VPN 或 Tor 隐藏你的 IP 地址
- Wallet 安全**：激活 wallet Lightning 的自动锁定功能



## 与 CLI 一起使用



本节根据实际使用案例，演示通过 Mostro CLI 购买比特币。



### 步骤 1：列出可用订单



listorders "命令显示所有活动订单：



```bash
mostro-cli listorders
```



您将看到一个表格，其中包含每个订单的详细信息：ID、类型（买入/卖出）、金额、货币、付款方式。



![Liste des ordres disponibles](assets/fr/05.webp)



在此示例中，通过 Revolut 卖出 5 欧元的订单可见（ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`）。



### 步骤 2：接受订单



要购买这些比特币，请使用 `takesell` 下单：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro 会要求您提供**闪电发票**，以接收 BTC。发票上会标明具体金额（此处：4715 sats）。



![Prise d'ordre de vente](assets/fr/06.webp)



### 步骤 3：提供闪电发票



从您的 wallet（Phoenix、Breez 等）生成一张金额准确的 "闪电 "发票，然后发送给 ：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



系统确认发货后，会告诉您等待卖方支付暂扣发票后再启动托管。



![Envoi de la Lightning invoice](assets/fr/07.webp)



### 步骤 4：联系卖家



托管激活后，使用 `dmtouser` 向卖方索取付款详情：



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### 步骤 5：获取答案



查看直接消息，查看卖家的回复：



```bash
mostro-cli getdm
```



卖家会向您提供他的付款 ID（这里是他的 Revtag：`@satoshi`）。



![Réception de la réponse](assets/fr/09.webp)



### 步骤 6：支付法定货币



通过约定的方式（本例中为 Revolut）将付款发送至所提供的详细联系方式。 **保留所有证明文件**（截图、交易参考）。



### 第 7 步：确认付款发送



付款后，请通知 Mostro ：



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### 步骤 8：接收比特币



一旦卖方确认收到法币并使用 "释放 "命令解除托管，您就会立即收到您提供的闪电发票上的比特币。



### 步骤 9：评估



为卖家评分，为分散式声誉做出贡献：



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### 实用命令



**取消订单** （在订单被接受之前） ：


```bash
mostro-cli cancel -o <order-id>
```



**创建新的销售订单** ：


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**开启争端** ：


```bash
mostro-cli dispute -o <order-id>
```



## 与移动应用程序一起使用



本节通过一个真实的使用案例，演示如何通过 Mostro Mobile 销售比特币。



### Interface 主机



应用程序有 3 个主要选项卡：





- 订单簿**：浏览可用的买入（买入 BTC）和卖出（卖出 BTC）订单
- 我的交易**：查看您的有效订单和历史订单
- 聊天**：使用数字与对手交流



![Interface principale](assets/fr/14.webp)



### 建议配置



交易前，通过菜单（☰）> **设置**进行一些设置：





- 闪电 Address**（可选）：直接接收付款
- 中继**：添加多个 Nostr 中继器以提高复原能力（例如，`wss://nos.lol`, `wss://relay.damus.io`)
- Mostro 公钥**：检查您正在使用的 Mostro 实例的公钥



![Paramètres de l'application](assets/fr/16.webp)



**对于 CLI/Mobile 同步**很重要：如果您同时使用 CLI 和移动应用程序，请在两个客户端配置**完全相同的 Nostr 中继和 Mostro Pubkey**。如果没有完全相同的配置，您将无法在两个界面上看到相同的订单。在 "设置"（上面的截图）中可以看到的中继器和 Mostro Pubkey 必须与 CLI ".env "文件中的一致。



### 步骤 1：创建卖出订单



按右下角的绿色**"+"**按钮，然后选择**出售**（红色按钮）。



![Boutons de création d'ordre](assets/fr/17.webp)



填写创建表 ：



1. **货币**：选择您希望接收的货币（欧元、美元等）


2. **金额** ：输入法定金额（如 1 至 3 欧元）


3. **付款方式** ：选择付款方式（如 "Revolut）


4. **价格类型**：选择 "市场价格


5. **溢价**：调整溢价（滑块从 -10% 到 +10%，建议：0% 以快速出售）



按**提交**发布订单。



### 第 2 步：出版确认



您的订单现已发布！该订单可使用 24 小时。您可以随时执行 `cancel` 命令，在买家接受之前取消订单。



![Ordre publié](assets/fr/18.webp)



订单出现在**我的交易**标签中，状态为 "待处理"，徽章为 "由您创建"。



### 步骤 3：买家接受您的订单



当买家接受您的订单时，您会收到通知。详情请查看 **我的交易**。



![Ordre pris par un acheteur](assets/fr/19.webp)



**重要说明**：您现在必须**支付显示的持有发票**，以将您的比特币（此处为 4674 sats 换 1-5 欧元）锁定在托管中。您最多有**15分钟的时间**，否则兑换将被取消。



复制暂扣发票并从 wallet Lightning（Phoenix、Breez 等）中支付。



### 步骤 4：与买家沟通



托管激活后，按**CONTACT**键打开与买家的加密聊天。



买方（此处为 "anonymous-gloriaZhao"）将与您联系，询问您的付款详情。请回复您的详细信息（Revtag、IBAN 等）。



![Chat avec l'acheteur](assets/fr/20.webp)



### 步骤 5：收到法定货币付款



等待您的 Revolut 账户（或其他约定方式）收到法币付款。 **仔细检查**：




- 确切数额
- 发件人
- 参考文献（如有要求



买家会通过聊天通知您他已付款。Mostro 也会显示一条信息，确认已将法币发送给您。



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### 步骤 6：解除托管



在您的账户上**确认收到**法币付款后，按下绿色的**RELEASE**按钮，确认后就可以将 sats 发送给买方。



![Libération de l'escrow](assets/fr/20.webp)



比特币通过 "闪电 "发票即时转给买方。



### 第 7 步：评估考虑因素



发布后，按**RATE**给买家评分。选择 1 到 5 星（此处为 5/5），然后按**提交评分**。



![Évaluation de la contrepartie](assets/fr/21.webp)



交流结束了！



### 使用手机应用程序购买比特币



**购买**比特币的过程与此类似，但正好相反：



1.浏览 ** 订单簿** > ** 购买 BTC** 选项卡，查看卖出订单


2.点击感兴趣的订单查看详情


3.按**接单**


4.提供 Lightning 发票（由 wallet 生成）


5.等待卖家激活托管服务


6.通过**CONTACT**联系卖家了解付款详情


7.发送法币付款（保留凭证）


8.核实后卖方解除托管


9.通过闪电发票即时接收比特币


10.给卖家评分 (1-5 星)



### 问题管理



**取消订单**：在**我的交易**中，按下您的订单，然后按下**取消**按钮（仅在订单被执行前可用）。



**打开争议**：如果出现分歧，请在订单详情中按**驳回**。附上所有证据（聊天截图、银行交易参考）。



## 优势和局限性



### 益处



**金融主权**：由于持有发票机制，您的比特币永远不会离开您的直接控制，消除了交易所破产或盗版的风险。



**抗审查**：任何机构都无法关闭网络或审查您的指令。只要 Nostr 中继器处于工作状态，系统就能正常工作。



**默认匿名**：只有假名 Nostr 密钥能识别您的身份，无需 KYC 或个人数据。端到端加密通信。



**付款灵活**：可以使用任何双方都接受的付款方式（转账、移动应用程序、现金、易货）。



### 局限性



**早期开发**：需要初级界面和技术学习曲线。



**流动性有限**：订单数量有限，尤其是大额订单或稀有货币。



**技术要求**：需要对 Lightning 和 Nostr 有基本了解。



**个人责任**：出现问题时没有集中支持，需要谨慎。



## 结论



Mostro P2P 将 Lightning Network、Nostr 和自动托管结合在一起，实现了真正的去中心化交易，是中心化交易所的一个有前途的替代选择。尽管开发尚早，流动性有限，但该平台已经提供了金融主权、抗审查和默认匿名性。



对于喜欢自主性和保密性的比特币用户来说，Mostro 是一个值得逐步探索的可行选择。它的去中心化架构保证了社区而非商业的发展，为未来真正自由的 Bitcoin 交易所铺平了道路。



## 资源



### 正式文件




- [Mostro官方网站](https://mostro.network)
- [技术文件](https://mostro.network/docs-english/index.html)
- [Mostro基金会](https://mostro.foundation)



### 源代码和开发




- [主 GitHub 代码库](https://github.com/MostroP2P/mostro)
- [网络客户端](https://github.com/MostroP2P/mostro-web)
- [客户 CLI](https://github.com/MostroP2P/mostro-cli)



### 社区




- [Nostr协议](https://nostr.com)
- [Lightning Network 指南](https://lightning.network)