---
name: ThunderHub
description: Interface 闪电节点管理网络 LND
---
![cover](assets/cover.webp)



## 导言



ThunderHub 是 Lightning 节点（LND）的**开源管理器**，提供可从任何设备或浏览器访问的直观 Interface。



**主要功能：**




- 监控：余额、渠道、交易、路由统计的全局视图
- **管理**：打开/关闭渠道、接收/发送付款、渠道平衡
- 集成：支持 LNURL、通过 Boltz 进行交换、Amboss 备份
- Interface 响应**：兼容移动设备、平板电脑和桌面设备的深色/浅色主题



ThunderHub 与 **Umbrel**、**Voltage**、**RaspiBlitz** 和 **MyNode**轻松集成，简化了节点的日常管理。



**ThunderHub 特别适合正在寻找符合人体工程学的 Interface 来管理其渠道、控制流动性（再平衡）、监控交易以及整合 Amboss 等第三方服务的运营商。通过本地连接或 Tor 连接可确保安全。**



如果您还没有 "闪电 "节点，建议您参考我们的 LND Umbrel 教程：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 安装



根据你的闪电节点托管环境，ThunderHub有多种不同的安装方式。无论你使用的是整套解决方案（Umbrel、Voltage、RaspiBlitz、MyNode、Start9等）还是手动安装，ThunderHub通常都不费吹灰之力。下面，我们将介绍两种常用方法：通过 Umbrel 应用商店和手动安装（适用于服务器或自托管发行版）。



### 通过 Umbrel 安装



Umbrel 将 ThunderHub 集成到其**应用商店**中，使安装变得极为简单。无需命令行或手动配置：一切都通过 Interface Umbrel 完成。只需按照以下步骤操作即可：





- 打开 Umbrel 面板：连接到 Umbrel 节点的 Interface 网络（例如，本地网络上的 `http://umbrel.local`，如果使用 Tor，则通过其 `.onion` Address）。
- 访问应用程序商店：在 Umbrel 的主菜单中，点击 "App Store"（或 "App"）。在可用应用程序列表中搜索 **ThunderHub**。



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- 安装 **ThunderHub**：点击 ThunderHub 应用程序，然后点击安装按钮。如有必要，请确认。Umbrel 会自动下载 ThunderHub 并部署到你的节点上。





- 启动应用程序：安装完成后（几十秒），ThunderHub 会出现在你的主页上。点击图标打开。ThunderHub 会在浏览器中启动。



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**重要提示：** 首次打开 ThunderHub 时，它会自动显示登录所需的**默认密码**。通过 "不再显示 "选项，您可以在以后连接时隐藏该显示。**我们强烈建议您：**




- 立即在密码管理器中保存此密码
- 复制**内容**，供下一步使用
- 保存密码后，选中 "不再显示此内容



![Page de connexion de ThunderHub](assets/fr/03.webp)



然后您将进入登录页面，必须输入上一步复制的密码才能解锁 Interface。



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel 会在后台为 ThunderHub 提供 LND 连接信息（TLS 证书、管理 macaroon 等），因此你无需进行任何额外配置。只需点击几下，ThunderHub 就能在 Umbrel 节点上运行了。



### 手动安装（自托管，不包括 Umbrel）



对于 Umbrel 以外的用户（例如，在个人服务器、装有 RaspiBlitz 的 Raspberry Pi 上或*独立*安装），ThunderHub 的安装需要一些额外的步骤。下面我们将根据[ThunderHub 官方文档](https://docs.thunderhub.io)介绍源代码安装和配置。



#### 安装



**前提条件：** 根据 [documentation setup](https://docs.thunderhub.io/setup) 确保您的系统满足最低要求：




- **Node.js** 18 或更高版本
- **npm** 已安装
- 访问 LND 验证文件 ：
  - LND TLS 证书 (`tls.cert`)
  - LND 管理马卡龙 (`admin.macaroon`)
  - LND gRPC 服务 Address（主机名：端口）（本地默认为 "127.0.0.1:10009）



**1.获取 ThunderHub 代码：** 按照[安装文档](https://docs.thunderhub.io/installation)中的描述克隆项目的 GitHub 仓库：



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. 安装依赖项并构建应用程序：**



```bash
npm install
npm run build
```



这些命令会安装所有需要的模块，然后编译应用程序（ThunderHub 由 TypeScript/React 编写）。



**3.日后更新：** ThunderHub 为日后更新提供了多种方法：



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### 配置（设置）



**1.主要配置文件：** 在 ThunderHub 文件夹根目录下创建一个`.env.local`文件，用于自定义配置（这将防止更新时覆盖您的设置）。根据 [setup documentation](https://docs.thunderhub.io/setup) 创建主要变量：



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2.服务器账户配置：** 创建在 `ACCOUNT_CONFIG_PATH` 中指定的 YAML 文件：



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3.远程访问：** 要连接到远程 LND 节点，请在 `LND.conf` 中添加 ：



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4.安全性：** 首次启动时，ThunderHub 会自动隐藏 YAML 文件中的 "masterPassword" 和所有账户密码，以避免服务器上出现明文密码。



**5.启动 ThunderHub：**



```bash
npm start
```



默认情况下，服务器通过 3000 端口监听。访问 `http://localhost:3000` （或从本地网络访问 `http://ip-serveur:3000`）。



**6.Docker 替代方案：** ThunderHub 提供官方 Docker 映像：



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



出现 ThunderHub 登录页面。选择已配置的账户并输入密码，即可访问仪表板。



**在其他发行版上的安装：** 预打包节点发行版（RaspiBlitz、MyNode、Start9等）通常通过各自的管理界面提供本地ThunderHub支持。



**更多信息：** 请查阅完整的官方文件：




- 安装：**[docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)**
- 配置：**[docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)**



这些资源详细介绍了 SSO 账户、加密马卡龙、TOR 配置等高级选项。



安装并访问 ThunderHub 后，您就可以使用它的所有功能了。在下面的章节中，我们将介绍 Interface ThunderHub 及其各种选项卡，指导你如何使用。



## Interface 介绍



Interface ThunderHub 的结构围绕一个主菜单（通常显示在左侧栏），由几个关键部分组成。每个部分对应管理闪电节点的一个方面。让我们逐一介绍：





- **主页** - 主页选项卡，包含总仪表板（节点概览和快速操作）。
- **仪表盘** - 可定制的仪表盘，带有小部件和高级指标。
- **Peers** - 闪电对等管理（与其他节点的连接）。
- **渠道** - 闪电渠道的详细管理。
- **再平衡** - 渠道平衡工具（循环支付）。
- **交易** - 闪电付款历史记录（LN 交易）。
- **转发** - 路由统计（由节点转发的付款）。
- **Chain** - Node 的 On-Chain 投资组合（On-Chain BTC：UTXOs，交易）。
- **Amboss** - 与 Amboss 集成（节点监控、备份等）。
- **工具** - 各种工具（备份、签名信息、马卡龙、报告等）。
- **交换** - 通过 Boltz 实现 On-Chain/Lightning 交换功能。
- **Stats** - 高级统计数据和节点性能指标。



*(注：根据 ThunderHub 版本的不同，某些部分的标题或附加功能可能略有不同，但总体原则保持不变）*。



### 主页（常规控制面板）



ThunderHub的**主页**标签是登录后出现的主页。它包含 "总控制面板"（**General Dashboard）**，提供 Lightning 节点状态的**全局概览**，并为常规操作建议**快速操作**。以下是您通常会发现的内容：



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- 余额和容量：在页面顶部，ThunderHub 会显示可用余额。在这里，您通常会看到 On-Chain 余额（节点 Wallet 中的 Bitcoin On-Chain，用 Anchor ⚓ 表示）和闪电余额（您的通道容量，用闪电 Bolt ⚡ 表示）。这样您就能立即了解 On-Chain 和 "闪电 "的资金情况。如果您有多个账户或渠道，请确保您使用的是正确的账户或渠道（例如，Mainnet 与 Testnet）。





- 关键统计数据：**仪表板可显示节点的一些全局指标，例如开放通道数、连接的对等节点数、赚取的路由费（如适用）等。它是节点近期活动和健康状况的汇总。**





- 快速操作：**仪表盘上的按钮可快速执行最常见的任务，而无需浏览菜单。这些快速操作包括：**





- 幽灵：通过 Amboss 设置自定义闪电 Address。
- 捐赠：通过 "闪电" 捐款。
- 登录/前往**Amboss**：连接到您的 Amboss 帐户（快速连接），直接进入 Amboss.space 查看您的节点信息。
- **Address**：输入 Lightning Address 进行付款。
  - 打开**：打开一个新的 "闪电 "通道。点击后会打开一个表单，用于输入要打开通道的远程节点 URI、金额以及（如适用）要使用的最高 On-Chain 费用。
- **解码**：解码闪电 Invoice 或 LNURL，以便在付款前查看详细信息。
- **LNURL**：处理闪电付款或提款的 LNURL。
- 登录 **LnMarkets**：登录 LnMarkets 进行交易。



通过这些快速操作，您可以直接在主页上执行最常用的操作，而无需浏览 Interface 的各种选项卡。



简而言之，ThunderHub 仪表板可让您**快速地查看您的节点，并让您只需单击一下即可执行最常用的操作（发送/接收、打开通道）**。它是日常管理的理想起点。



### 仪表板



仪表盘**部分**与 "主页 "选项卡分开，提供更高级的自定义仪表盘。通过该部分，您可以根据节点操作员的需求创建带有特定部件的自定义视图。





- 可定制的小部件：**与有固定布局的主页不同，仪表板让你可以准确选择要显示的 Elements 以及如何组织它们。**



![Dashboard sans widgets activés](assets/fr/06.webp)



如果没有启用部件，则会显示 "未启用部件！"信息，并带有一个 "设置 "按钮，用于访问自定义参数。



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



在设置中，您可以按类别选择各种部件："Lightning - 信息"、"Lightning - 表格"、"Lightning - 图表 "等。每个小工具都可以通过 "显示/隐藏 "按钮单独激活或停用。



![Bas de la page des paramètres](assets/fr/08.webp)



在设置的底部，你会发现 "返回仪表盘 "按钮可以返回仪表盘，而 "重置小部件 "按钮可以重置默认显示。



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



配置完成后，您的仪表板可以显示各种图表和指标：闪电付款图、已开具发票数量、转发统计、详细余额等。





- 高级指标：**通过图表和实时数据，获取有关节点性能的更详细统计信息。**





- 可配置的概览：**无论您是普通用户还是管理多个路由通道的专业操作员，都可以根据自己的需要定制显示屏。**





- 模块化 Interface：**根据需要添加或删除小部件：前瞻性图表、流动性指标、节点健康警报等。**



该部分对希望监控特定指标或了解其 Lightning 节点更多技术概况的高级用户特别有用。它与 "主页 "部分相辅相成，为如何显示信息提供了更大的灵活性和控制权。



### 同行



对等节点**部分列出了当前作为对等节点与您连接的所有 "闪电 "节点。对等节点**是 Lightning Network 上节点与节点之间的直接连接。即使没有开放通道，您的节点也可以与对等节点连接（例如，只与网络上的 Exchange 八卦信息连接），当然，每个开放通道都自动意味着一个已连接的对等节点。



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



在同行选项卡中，你会看到 ：





- 信息栏：**Interface** 显示有用的详细信息，如同步状态、连接类型（clearnet 或 Tor）、ping、接收/发送的卫星数和交换的数据量。
- 添加对等体：**ThunderHub 允许你通过右上角的"添加"按钮手动连接到一个新的对等体。你需要输入节点的 URI（格式为"<public_key>@<socket>"）。一旦验证通过，ThunderHub 就会发送相应的"lncli connect"命令。如果节点在线并可访问，它就会被添加到你的对等节点列表中。**



### 渠道



渠道**选项卡**是 Lightning 渠道管理的核心。它可能是你最常查阅的部分。它展示了**所有 Lightning 渠道**及其详细信息，并允许你对这些渠道执行管理操作。



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



以下是频道页面的内容：





- 通道列表视图：列出了每个打开（或打开/关闭）的通道，通常还有远程节点的别名、通道总容量，以及说明本地与远程流动性分布的彩色条。ThunderHub 使用颜色代码（通常为蓝色/Green）或百分比来表示通道平衡：例如，蓝色表示本地份额，Green 表示远程份额。如果通道完全平衡（50/50），则条形图上两种颜色各占一半。这样，您就可以一目了然地识别哪些频道不平衡（全部蓝色 = 几乎全部本地频道，全部 Green = 几乎全部远程频道）。





- 信息栏：**Interface** 显示详细的栏目，包括状态、可用操作、对等信息、通道 ID、容量、活动、费用和余额，并以图形方式显示流动性。





- 显示配置：**右上角的拨轮可让您根据自己的喜好自定义频道显示。**





- 状态：您还会看到状态指示器，例如 **"激活"**（通道已打开并开始运行）、**"脱机"**（对等设备已断开连接，因此通道暂时无法使用）、**"等待"**（打开或关闭通道，等待 On-Chain 确认）。





- 频道上的操作：**ThunderHub 为每个频道提供操作按钮（通常为图标形式）**：



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- 编辑费用：**Interface "更新频道策略"可让您调整所有频道参数：基本费率、费率（以 ppm 为单位）、CLTV Delta、最大 HTLC 和最小 HTLC。这样，您就可以针对每个通道单独调整收费政策，以吸引（或阻止）路由流量。** *（注意：ThunderHub 不能替代自动收费管理工具，但对于手动调整非常有效）*。
- 关闭通道（**关闭**）：Interface "关闭通道 "通过定义费用（Sats/vByte），让您选择**合作关闭**（默认）或**强制关闭**（*Force Close*）。 **重要：** 尽可能选择合作关闭，以避免 On-Chain 结算延迟和更高的费用。ThunderHub 会告诉您对方是否在线（可能合作）。如果强行平仓，请务必确认，因为这是不可逆转的，而且会触发带有时间锁的清算交易（在 Bitcoin Mainnet 上一般为 144 个区块或 ~1 天）。
- 打开新频道：**要打开新频道，请单击频道页面右上方的齿轮，然后选择 "打开"。然后，你就可以向新的或现有的对等设备启动一个频道。使用该页面的好处是，你可以看到现有频道的列表，这有助于你决定在哪里打开新频道。**



简而言之，"通道"部分可让您**精细地控制每个通道**。在这里，你可以控制流动资金的分配，决定保留或关闭哪些通道，并设置每个通道的路由参数。ThunderHub 为这些重要的节点管理操作提供了清晰的 Interface 接口。



### 重新平衡



重新平衡**选项卡专门用于频道平衡**。平衡（或*再平衡*）是指通过 Lightning Network 从一个渠道向另一个渠道进行**循环支付**，从而重新调整进出渠道之间的资金分配。这样，您就可以在不引入新资金的情况下，将流动资金从过于充盈的渠道转移到过于空虚的渠道，从而使您的渠道更加有用（一个平衡的渠道既可以发送也可以接收付款）。



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub 为这一操作提供了极大便利，否则在命令行上进行操作会很繁琐。下面介绍如何使用 "重新平衡 "部分：





- 初始频道视图：进入**重新平衡**后，ThunderHub 会显示一个频道列表，每个频道都有一个平衡指示器（类似于**频道**页面上的指示器）。你可以立即看到哪些频道失去了平衡。ThunderHub 可以按照平衡度增加的顺序对频道进行排序，这样最不平衡的频道就会显示在列表的最上方（0.0 表示完全是本地或远程频道）。





- 对等点选择：**Interface 可轻松选择传出和传入对等点进行再平衡。**





- 参数设置：**可以设置**：
  - 您愿意支付的**最高费用**（单位：Sats 和 ppm
  - 使用 "固定 "或 "目标 "选项重新平衡**的**金额
- 路由时应避免的节点
- 寻找路线的最长试验时间





- 选择**来源渠道**：首先选择**流出（来源）**渠道，即您在本地拥有过多流动资金而无法转移的渠道。实际上，这是您的本地份额较高（> 50%）的渠道。让我们设想一个拥有 1,000,000 个 Sats 的 A 频道，其中 900,000 个是本地的，这是一个向其他地方发送 Sats 的好渠道。点击该 A 频道的**发送**按钮，ThunderHub 就会将其标记为来源。





- 选择**目标渠道**：接下来，选择需要接收流动性的**进入（目标）**渠道。通常情况下，这将是一个相反的渠道--大多数资金都在远端（例如，100 万个本地 Satss 中只有 10 万个）。一旦选择了源频道，ThunderHub 将按照相反的顺序（余额递减）对其他频道进行排序，以帮助确定互补性最强的频道。选择一个在本地有空间的 B 频道。然后，ThunderHub 会清楚地显示已选择的两个通道（源 A 和目标 B）。





- 设置收费金额和容差：**表格允许您输入**：





- 要重新平衡的**数量（单位：Sats）**。通常情况下，我们选择的数量等于两个通道在 ~50/50 时的平衡量。例如，ThunderHub 可以预填充源通道多余容量的一半。
  - 您愿意为此操作支付的**最高费用**（可选）。该费用以 Sats 表示（循环路由的总成本）。如果留空，ThunderHub 就会不计成本地搜索路径，这通常是不可取的（最好设置一个限制，例如小规模再平衡的 10 Sats，或最大 ppm）。





- 查找路由：点击按钮查找路由。ThunderHub 会查询 LND，计算从您的源频道通过网络到达目标频道的路由。如果找到符合费用标准的可能路由，它就会显示该路由的跳数和费用详情。例如，它可能会显示找到了一条 3 跳路径，总共需要支付 2 个 Sats 的费用。





- 开始重新平衡：如果您对建议的路线感到满意，请单击**平衡通道**。然后，ThunderHub 将通过 LND 启动循环支付。如果支付成功，您将看到成功通知，频道 A 和频道 B 的余额将被实时修改。ThunderHub 将更新这些通道的余额指示器（理想情况下，它们将比以前更绿，表明余额更好）。





- 调整和迭代：**如果第一次尝试没有找到路线（或路线太昂贵），可以调整参数：**





  - 尝试较小的调整量（有时部分调整会成功，而大量调整会失败）。
  - 逐步提高最高收费标准，但要注意不要支付超过其价值的费用。
  - 使用**获取另一条路线**按钮（如果有）尝试其他路线。
  - 如果情况真的很棘手，可以试试另一对通道。



ThunderHub 使这一过程变得**直观和**形象。只需 4 个步骤（选择输出渠道、选择输入渠道、金额、验证），您就可以完成过去需要复杂手动命令才能完成的工作。该工具对于保持节点平衡、提高路由性能和体验（更轻松地在所有渠道收发付款）非常有价值。



最后要注意的是，重新平衡会消耗路由成本（支付给中间节点），因此这是一项**投资，可使节点更加灵活**。请明智地使用它，例如，为您经常使用的服务提供通道支持（入站流动性），或平衡大型路由通道。ThunderHub可让您**简单、高效**地做到这一点。



### 交易



ThunderHub 中的**交易**部分与您节点的**闪电**交易历史相对应，即通过通道支付或接收的付款和发票。这是您的 LN 业务的一种账目报表。



![Historique des transactions Lightning](assets/fr/14.webp)



在该选项卡中，您可以找到 ：





- Invoice 图表：在右上角，图表显示收到的发票随时间的变化情况，让您直观地了解节点的活动。





- 按时间顺序排列的所有闪电交易列表，包括*从*您的节点进行的交易或*到*您的节点进行的交易。每个条目可显示 ：





- 操作类型： **发送付款**（传出付款）或**接收付款**（传入付款，通过付费 Invoice）。
  - Sats 中的数额。
  - 日期/时间
  - 付款 ID（Hash 或 RHash 预图像）或注释（如果您在 Invoice 中添加了备注）。
  - 状态： **已完成**，或可能**进行中**/*失败*（例如等待解决的付款，但通常 LND 处理速度很快，因此与 On-Chain 交易相比，这里几乎没有 "待处理"）。



简而言之，"交易 "部分是您的**LN 活动日志**。它非常有用，可以用来检查支付是否已完成、花费了多少费用，或追踪闪电交易的历史记录。结合 "转发"（Forwards）部分（接下来会介绍），你就能全面了解通过节点的资金情况。



### 前锋



转发**"选项卡专门用于显示节点的**路由**活动，即通过您的通道**转发的付款（当您作为 Lightning Network 的中间节点时）。如果您将自己的节点作为路由节点运行，这部分内容对跟踪您的性能非常重要。



![Statistiques de routage Lightning](assets/fr/15.webp)



在《前行》中，ThunderHub 介绍了 ：





- 筛选器和显示选项：**右上方的筛选器可让您按天/周/月/年对数据进行排序，并选择图形或表格显示。**





- 活动信息：**如果在所选时间段内未执行路由操作，Interface 会显示 "No forwards for this period（此时间段无转发）"，如本示例所示。**





- 最近转发**表：每个条目对应于通过您的节点转发**的付款。对于每笔转帐，我们通常会看到 ：





  - Timestamp、
  - 路由量（单位：Sats）、
- 这次转发所赚取的**费用**（在 Sats 中，这是您在转入频道收到的费用和在转出频道发送的费用之间的差额）、
  - 使用的传入和传出信道（通常用对等别名或信道 ID 标识）。
  - 状态（通常为*完成*，如果转发途中失败则为失败）。





- 汇总统计：ThunderHub计算并在页面顶部显示特定时间段（如过去24小时或7天等，有时可配置）内的总数和统计数据。



简而言之，"转发"部分提供了"闪电"节点路由活动的**实时概览**。与"通道"和"再平衡"部分一起，构成了优化节点的完整套餐：通道/再平衡用于流动性，远期用于观察结果（流量和利润）。



### 链条



**链**部分对应 LND 节点的 Bitcoin On-Chain 投资组合管理。通过 Interface 可以查看和管理 Bitcoin 资金，这些资金用于打开通道或从关闭的通道接收资金。



![Gestion du portefeuille on-chain](assets/fr/16.webp)



在 Chain，你会发现 ：





- 余额 On-Chain: **显示 Wallet LND 中可用的 BTC 总余额。**





- 未用产出清单：**查看所有未用产出 (UTXO)，包括每项产出的金额、确认、Address 和格式。**





- 交易历史：**所有 Bitcoin 交易的详细表格，包括类型（输入/输出）、日期、金额、费用、确认、包含区块、地址和 txid。**



### 安博斯



ThunderHub与**Amboss**平台（amboss.space）集成，后者提供有关闪电节点的详细信息、流动性市场以及加密通道备份和可用性监控等实用功能。



![Intégration Amboss avec ses options](assets/fr/17.webp)



在 ThunderHub 中，Amboss 部分允许您将节点**链接到您的 Amboss 账户**：





- Ghost Address：**为您的节点设置一个个性化的 Lightning Address**，方便接收付款。





- 自动通道备份：** Amboss 上加密通道备份**（SCB 文件）的旗舰功能。在设置中激活 **Amboss Auto Backup = Yes**，每次更改通道时自动发送加密备份更新。如果发生故障，您可以通过此外部备份恢复资金。





- 健康检查：**激活 Amboss Healthcheck = Yes** 可让您的节点定期向 Amboss 发送 ping。如果您的节点出现离线，您就会收到警报。





- 其他功能：**自动余额推送、Magma/Hydro 集成（流动性市场）以及访问详细的性能统计。**



Amboss 集成增加了一个重要的**安全 Layer**，具有自动外部备份和可用性监控功能，可直接从 ThunderHub 访问。



### 工具



工具**部分**汇集了用于管理节点的各种高级工具。以下是主要的 Elements 工具：



![Interface des outils disponibles](assets/fr/18.webp)





- 备份：**手动管理频道备份（SCB）**。ThunderHub 允许您**下载频道的完整备份文件**（选项 "备份所有频道 -> 下载"）。请将此 "channel-all.bak "文件保存在一个安全的地方--它对于在系统崩溃时恢复资金至关重要。在重新部署节点时，您也可以**导入**备份文件。





- 会计：**财务报告导出工具**，包括特定时期内赚取/支付的费用和路由量。
- 签名信息：**与你的节点签名或验证信息**，通过加密签名证明你的Lightning节点的Ownership。
- 马卡龙（面包房部分）：** 管理 LND** 马卡龙，创建自定义访问。Interface "面包房 "允许您精确选择每个权限："添加或删除同行"、"创建连锁地址"、"创建发票"、"创建马卡龙"、"衍生密钥"、"获取访问密钥"、"获取连锁交易"、"获取发票"、"获取 Wallet 信息"、"获取付款"、"获取同行"、"支付发票"、"撤销访问密钥"、"发送到链地址"、"签署字节"、"签署信息"、"停止 daemon"、"验证字节签名"、"验证信息 "等。每个权限都可以通过 "是/否 "按钮单独激活，以创建一个量身定制的马卡龙。
- 系统信息：**显示 Wallet 版本和激活的 RPC。**



简而言之，"工具 "部分将备份、会计、安全和访问管理等高级管理功能整合到一个统一的 Interface 中。



### 交换



ThunderHub 的 "**交换**"选项卡可让您通过 Boltz 服务将 Lightning satoshis 交换到 Bitcoin On-Chain。该功能可在不关闭通道的情况下，将多余的 "闪电 "流动资金 "倾倒 "到通道中。



![Interface de swap via Boltz](assets/fr/19.webp)



过程很简单：





- **金额**：定义要兑换的金额
- **Address**：输入 Bitcoin 接收 Address
- 执行：ThunderHub 与 Boltz 通信，自动处理 Exchange



**福利：**




- 非托管服务（无现金托管）
- 保留现有渠道
- 易于使用的集成式 Interface



Boltz 只收取少量佣金，您只需支付标准的 Bitcoin 交易费。ThunderHub 会在确认前显示所有费用。



### 统计数据



ThunderHub的**统计**部分提供关于Lightning节点的**高级统计**，用于分析性能和优化路由。



![Statistiques du nœud via Amboss](assets/fr/20.webp)



这一部分对于优化成本、确定成功渠道和规划节点扩展至关重要。



## 结论



**ThunderHub**已成为轻松管理闪电**LND**节点的重要工具。这款现代化的 Interface 提供所有基本功能：渠道管理、支付、监控，以及自动再平衡和 Amboss 集成等高级功能。



**主要福利：**




- Interface 时尚直观
- 强大的工具（再平衡、Boltz 交换、自动备份）
- 与 Umbrel、Voltage、RaspiBlitz 和其他发行版兼容



ThunderHub 实现了高级 Lightning 节点管理的平民化，使以前需要复杂技术命令才能完成的工作变得简单易行。无论您是初学者还是经验丰富的操作员，ThunderHub 都能让您通过现代、全面的 Interface 高效地管理您的 Lightning 节点。



## 资源



**官方链接：**




- 官方网站：**[thunderhub.io](https://thunderhub.io)**
- 文档：**[docs.thunderhub.io](https://docs.thunderhub.io)**
- GitHub 源代码：**[github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)**