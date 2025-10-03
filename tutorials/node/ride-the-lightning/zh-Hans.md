---
name: Ride The Lightning (RTL)
description: 使用 Ride The Lightning (RTL) 管理您的 "闪电 "节点
---
![cover](assets/cover.webp)


## 1.导言



**Ride The Lightning (RTL)** 是一个完整的 Interface 网络应用程序，用于管理 Lightning Network 节点。这个自托管网络应用程序提供了一个可从浏览器访问的Lightning**驾驶舱**。RTL 可与所有主要的 Lightning 实现（LND、Core Lightning/CLN 和 Eclair）配合使用，让您完全控制节点和频道。RTL 是开源（MIT 许可）且免费的，已默认集成到许多整套节点解决方案（RaspiBlitz、MyNode、Umbrel 等）中。



**没有图形化的 Interface，Lightning 节点只能通过用户友好的 CLI 命令进行管理。RTL 采用符合人体工程学的 Interface 简化了这些操作。以下是主要应用**：





- 查看频道和节点 - 仪表板显示 On-Chain 余额、闪电流动性（本地/远程）、同步状态、节点别名等。您可以查看频道列表、容量、本地/远程分布和状态。RTL 提供上下文相关的仪表板，可从不同角度分析活动。





- **闪电通道管理** - 只需点击几下即可打开/关闭通道。RTL 让您无需指令即可连接到对等机构并打开通道。您可以调整路由费用，查看余额得分，或启动循环再平衡，在渠道之间重新平衡资金。





- **跟踪和付款** - RTL 管理 "闪电 "交易：通过发票发送付款，generate 接收发票，跟踪交易（付款、路由）的详细历史记录。Interface 还可分析路由，查看哪些付款通过了您的节点。





- **Wallet On-Chain 管理和备份** - On-Chain 选项卡可让您 generate 地址和发送交易。RTL 为 LND 导出 SCB 文件，每次修改通道都会自动更新，从而轻松保存通道。



简而言之，RTL 是 Lightning Network 的**功能强大的仪表板**，提供了一个教育性的 Interface，可用于日常节点试运行。本教程将指导您安装和使用它来管理您的渠道和付款。



## 2.RTL 的技术运作



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



在深入探讨具体问题之前，简要了解**RTL 与 Lightning 节点**在技术层面上的交互方式是非常有用的。



**一般架构：** RTL 是一个使用 Node.js（后端）和 Angular（前端）构建的网络应用程序。具体而言，RTL 作为一个小型本地网络服务器（默认端口为 3000）运行，通过其 API 与你的 Lightning 实现进行对话。这取决于.NET的类型：





- 通过**LND**，RTL 使用 LND 的 REST API（端口 8080）来执行 "闪电 "命令。连接通过 TLS 加密，并需要 LND 的**admin macaroon** 文件进行身份验证。





- 在**Core Lightning (CLN)**下，RTL使用*c-lightning-REST*提供的REST API，或通过`commando`插件使用**access rune**。Umbrel 等解决方案会自动配置这些 Elements。





- 使用 **Eclair**，RTL 会使用配置的验证密码连接到 Eclair REST API。



**配置和安全性：** RTL 通过 JSON 文件 (`RTL-Config.json`)进行配置，您可在该文件中定义网络端口、访问密码以及与节点的连接信息。Interface 网络受登录/密码（默认`密码`可更改）保护，并支持 2FA。默认情况下，RTL 以本地 HTTP (`http://localhost:3000`)方式运行，但对于远程访问，请始终使用安全连接（通过反向代理、Tor 或 VPN 实现 HTTPS）。



简而言之，RTL是一个附加组件，它通过安全应用程序接口连接到您的节点，需要适当的访问令牌，并提供自己的安全Layer。这种模块化架构甚至可以让你用一个RTL实例**管理多个Lightning节点**。



## 3.RTL 安装



由于 RTL 是作为开源软件发布的，因此有多种方法可以将其安装到系统上。本节将介绍两种主要方法：手动安装和通过 Umbrel 安装。



### 手动方法



如果您希望保持精细控制，或将 RTL 集成到自定义配置中，则适合手动安装。以下步骤适用于运行 Linux 的 LND 节点（如 Raspberry Pi 或运行 Ubuntu/Debian 的 VPS），但对于 CLN/Eclair 也类似。



**前提条件：** 确保机器上有一个**同步**的 Bitcoin 节点和一个正常运行的 Lightning 节点（LND、CLN 或 Eclair）。RTL 本身不包含 Lightning 节点，而是连接到现有节点。您还需要安装 **Node.js**（建议使用 14 以上版本）。你可以使用 `node -v` 或从官方网站（https://nodejs.org/en/download/）或软件包管理器安装 Node。



主要安装步骤如下



**下载 RTL 代码**：将 RTL 官方 GitHub 代码库克隆到您选择的目录中。例如



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**安装依赖项**：RTL 是一个 Node.js 应用程序，因此需要安装所需的模块。在 RTL 文件夹中，运行 ：



```bash
npm install --omit=dev --legacy-peer-deps
```



该命令安装必要的 NPM 软件包（忽略开发依赖）。建议使用"--legacy-peer-deps "选项，以避免可能的 Node 依赖关系冲突。



**RTL-Config**：依赖项就位后，准备配置文件。将项目根目录下的 `Sample-RTL-Config.json` 文件复制/重命名为 `RTL-Config.json`。在 .NET Framework 中打开该文件：





- 用户界面密码：选择一个安全密码，并在 "多重通行证" 中输入（而不是默认的 "密码"）。
- 端口：默认为 `3000`。如果您的机器已经占用了该端口，您可以更改。
- **节点**：在 "节点[0]"部分，调整节点的参数：
     - lnNode"：节点的描述性名称（例如，"LND Node Maison"）。
     - lnImplementation`："LND"（或 "CLN"/"ECL"）。
     - 在 "身份验证 "下：
       - macaroonPath`：指定包含 LND macaroon 管理程序的文件夹的完整路径。
       - configPath`：节点配置文件（LND 的配置文件为 `LND.conf`）的路径。
     - 设置 "下：
       - fiatConversion`：如果要转换法定货币，则设置为 "true"。
       - unannouncedChannels`（未通知的频道）：设置为 "true "可查看未通知的频道。
       - 主题颜色 "和 "主题模式"：Interface 自定义。
       - channelBackupPath`：LND 频道备份的路径。
       - lnServerUrl`：Lightning 节点的 URL（例如 `https://127.0.0.1:8080`）。



**启动 RTL 服务器**：在 RTL 文件夹中，运行 ：



```bash
node rtl
```



应用程序启动后，可通过 `http://localhost:3000` 访问。



**可选）将 RTL 作为服务运行**：为实现自动启动，请创建 systemd .NET 服务：



要做到这一点




- 在机器上打开终端。
- 用以下命令创建一个新的服务文件（用你喜欢的编辑器替换 `nano`）：


```bash
sudo nano /etc/systemd/system/RTL.service
```




- 将下面的内容复制并粘贴到该文件中：



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- 将 `/path/to/RTL/rtl` 替换为机器上 `rtl` 文件的实际路径，将 `<your_user>` 替换为 Linux 用户名。
- 保存并关闭文件。
- 重新加载 systemd 配置：


```bash
sudo systemctl daemon-reload
```




- 激活并启动 RTL 服务：


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



现在，每次重启机器时，RTL 都会自动启动。您可以使用 .NET Framework 查看其状态：


```bash
sudo systemctl status RTL
```



### 通过 Umbrel 安装



如果使用 [Umbrel](https://getumbrel.com)，RTL 安装会简单得多：





- 访问 Interface Umbrel（通常通过 `http://umbrel.local`）
- 前往**应用商店**
- 搜索 "乘着闪电"



**重要说明：Umbrel 应用商店中有两个独立的 RTL 应用程序：**




- **Ride The Lightning**（用于 LND）：与 Umbrel 的默认 "闪电 "节点（LND）配合使用。
- Ride The Lightning (Core Lightning)**：只有在 Umbrel 上安装了 *Core Lightning* 应用程序并希望使用 RTL 管理该节点时才使用。



*每个 RTL 版本都预先配置了与相应实现（LND 或 Core Lightning）的对话。如果您没有更改 Lightning 节点，只需选择经典的 LND 版本*。



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- 点击**安装**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**重要：** 安装后，RTL 会显示一个屏幕，其中包含默认密码。 **复制并保存该密码** - 您需要用它登录 Interface RTL。每次启动 RTL 时都会显示该密码，直到您选中 "不再显示 "选项。



Umbrel 会自动处理 ：




- 下载并配置 RTL
- 配置 Lightning 节点的访问权限
- 管理更新
- 确保进入 Interface



安装完成后，应用程序将出现在 Umbrel 上的 "应用程序 "菜单中。点击**"驾驭闪电 "**即可启动它。



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



在登录屏幕上输入您之前复制的密码。登录后，就可以直接从 Umbrel 面板访问 Interface 网络 RTL，无需额外配置！



## 4.介绍和使用 Interface RTL



现在，RTL 已经启动并开始运行，让我们来探索一下它的 Interface Web 及其主要功能。我们将介绍该应用程序的各个部分，让您对其有一个全面的了解。



### 主控制面板



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



登录后，您就可以访问**主控制面板**，了解 Lightning 节点的总体情况。该页面集中了基本信息：




- 您的闪电总余额
- On-Chain 可用余额
- 您的流动资金明细（流入/流出）
- 通过 Lightning 节点快速收发 Satss



### 基金管理 On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



**On-Chain**选项卡可让您直接在主链上管理比特币：




- 以不同单位（Sats、BTC、美元）显示余额
- 完整的交易清单
- Address 代 Taproot (P2TR)、P2SH (NP2WKH) 或 Bech32 (P2WKH)
- UTXO 管理、接收和发送比特币



### 闪电：子菜单的详细介绍



Interface RTL 具有 Lightning Network 专用的侧边菜单，汇集了管理节点的所有基本功能。以下是每个子菜单的详细信息，按截图顺序排列：



#### 1.同行/渠道



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



通过该子菜单可以 ：




- 查看已连接的同行和已打开或正在等待的 "闪电 "频道列表。
- 添加一个新对等（连接到另一个 Lightning 节点）。
- 打开、关闭或管理现有渠道。
- 查看每个通道的详细信息：容量、本地/远程余额、状态、交易历史、余额评分等。



#### 2.交易



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



在该子菜单中，您可以 ：




- 发送闪电付款（通过 Invoice）。
- generate 并管理发票以接收付款。
- 查看发送和接收付款的完整历史记录，包括详细信息（金额、日期、状态、费用、跳过次数等）。



#### 3.路由



该子菜单显示 ：




- 您的节点为其他 Lightning Network 用户路由的付款。
- 路由统计：转发的交易数量、赚取的费用、遇到的错误。
- 可导出历史记录，进行高级分析。



#### 4.推迟



该子菜单提供 ：




- 有关 Lightning 节点活动的详细报告。
- 有关渠道、付款、费用、容量等的图表。
- 更好地了解节点性能的工具。



#### 5.图表查询



通过该子菜单可以 ：




- 探索 Lightning Network 的拓扑结构。
- 搜索特定节点或频道
- 获取有关连通性和整体网络容量的信息。



#### 6.签名/验证



该子菜单提供 ：




- 用节点密钥签署信息的能力（Ownership 的证明）。
- 签名验证，以验证来自其他节点的信息。



#### 7.备份



该子菜单专门用于备份：




- 导出通道备份文件（SCB，用于 LND）。
- 必要时恢复配置或通道。
- 确保备份安全的技巧



#### 8.节点/网络



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



在该子菜单中，您可以找到 ：




- Lightning 节点状态的完整摘要：别名、版本、颜色、同步状态。
- 有关通道（激活、等待、关闭）、总容量和连接性的统计数据。
- 有关全局 Lightning Network 的信息以及您的节点在其中的位置。



### 服务博尔茨交换



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz 是一种隐私友好型非托管 Exchange 服务，可在 Lightning Network 和 Blockchain Bitcoin (On-Chain) 之间转换比特币。它提供两种类型的操作：反向潜艇交换（**交换出**）和潜艇交换（**交换入**）。



#### 交换（反向潜艇交换）



Swap Out 将 Lightning Network 上可用的 Satss 转换为 On-Chain 比特币。当一个节点的输入容量耗尽，或您想从 On-Chain Address 收回资金时，这种机制就会派上用场。操作过程如下




- 用户选择要兑换的金额
- 节点向 Boltz 发送闪电付款
- 在 Exchange 中，Boltz 以 On-Chain 的比特币阻挡了等量的比特币
- 一旦交易得到确认，用户就可以通过透露交换中使用的秘密来领取资金



这个过程是非拘禁性的，Boltz 从不扣留用户的资金。


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### 交换（潜艇交换）



另一方面，交换输入允许 On-Chain 资金重新注入 Lightning Network。这对恢复通道的输出容量特别有用。操作步骤如下：




- 用户向 Boltz 生成的特定 Address 发送比特币
- 只有 Boltz 支付了用户节点产生的闪电 Invoice 后，才能释放这些资金。
- 一旦支付了 Invoice，"闪电 "通道上就有了资金，从而提高了节点的输出能力



![Configuration d'un swap-in](assets/fr/12.webp)



这两种机制使 "闪电 "渠道的流动性得到有效管理，同时保持用户对其资金的主权。



### 配置和定制



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



通过**节点配置**选项卡，您可以定制自己的体验：




- 启动突击通道
- 自定义销售展示
- Block explorer 配置
- 调节 Interface



### 文件和帮助



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



最后，**帮助**部分提供了有关.NET Framework 的全面文档：




- 初始配置
- 同行和渠道管理
- 付款和交易
- 备份和恢复
- 报告和统计数据
- 签名和核实
- 节点和应用程序参数



这款功能全面的 Interface 可让您高效地管理您的 Lightning 节点，从基本操作到高级功能，一切尽在直观、条理清晰的 Interface 中。



## 5.高级用例和安全性



在本节中，您需要了解如何进一步使用 RTL 并确保 Lightning 节点的安全：



### 监测和故障排除



要监控您的节点，可以导出 RTL 数据（日志、CSV）并在 Grafana 等工具中查看。如果出现问题（付款受阻、通道不活动），可查阅 LND/CLN 日志并使用诊断命令（"lncli listchannels"、"lncli pendingchannels "等）。RTL 还提供用于监控路由事件的 Interface 日志。



### 安全的远程访问



切勿直接在互联网上公开 RTL。优先使用.NET：




- **VPN**（如 Tailscale），用于私人加密访问
- **Tor** 实现安全的匿名访问
- 反向代理 **HTTPS** （Nginx/Caddy），前提是您知道如何配置它



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 良好的安全措施





- **保护您的访问权限**：切勿共享 admin.macaroon 或您的 RTL 密码。限制敏感文件的权限。
- 定期备份：每次修改后导出通道备份文件 (SCB) 并将其存储在节点外。
- **更新**：通过最新的安全修复，使 RTL、您的节点和 Umbrel 保持更新。
- **保密性**：在共享日志和截图之前先进行匿名处理。切勿公开共享您的余额或同行列表。
- 单一访问**：RTL 不是多用户。不要共享管理员访问权限。对于只读访问，必要时使用专用的 Macaroon。



通过应用这些原则，你可以极大地限制风险，并保持对闪电节点的控制。



## 7.结论



无论您是初学者还是高级用户，**Ride The Lightning** 都是有效管理 Bitcoin/Lightning 节点的重要工具。它提供了一个清晰的 Interface 来控制你的通道、付款和节点健康状况，同时加深你对 Lightning Network 的理解。



RTL 的突出之处在于其多重实施兼容性、高级功能（再平衡、交换、报告）和教学方法。对于简单的需求，Interface Umbrel 或 Wallet mobile 就足够了，但 RTL 对于主动、优化的节点管理则非常有意义。



了解更多信息 ：




- RTL 官方网站：https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork：[r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - 技术讨论、项目公告、反馈和教育资源
- Umbrel 社区论坛：[community.getumbrel.com](https://community.getumbrel.com) - 官方论坛，设有 Bitcoin/Lightning 专区、指南和常见问题解决方案
- Lightning Network 开发人员：[github.com/lightning](https://github.com/lightning) - 用于跟踪开发和贡献源代码的官方 GitHub 代码库
- 堆栈 Exchange **Bitcoin** ：[Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - 开发人员和高级用户的技术问答



简而言之，RTL 可让您在功能齐全的现代化 Interface 中完全控制 Lightning 节点。



**Sources :** RTL 官方网站；RTL GitHub；Umbrel App Store；Umbrel Community；Plan B Network 资源。



为了加深您对 Lightning Network 工作原理的了解，我还建议您参加这个免费课程：



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb