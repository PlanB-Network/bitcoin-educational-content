---
name: LNbits
description: 商户会计平台
---
![presentation](assets/lnbits-intro.webp)

# 会计系统

LNbits 包含大量工具，用于控制和引导您的进出资金，连接您的网上商店，甚至是您自己创建的硬件钱包或 ATM 等设备。用户类型包括


- 希望将 LNbits 作为资金管理界面及其附加功能的钱包所有者。
- 希望接受比特币链上和闪电网络支付的在线和离线商家或服务提供商。
- 希望构建闪电网络应用程序的开发人员。
- 希望将其节点与 LNbits 系统集成以进行会计核算的节点运营商。
- 所有这些都有不同的需求。我们以模块化的方式构建 LNbits，让每个用户都能以最适合自己的方式使用我们的功能。

# 钱包管理器

LNbits 是一个免费开源的会计系统，而不是节点管理器。通道管理是连接到 LNbits 的 Lightning 节点的权限，它是 LND 或 c-lightning 等的资金来源。LNbits 系统的超级用户或管理员用户负责管理会计功能和内部扩展功能的整体可访问性和配置。

LNbits 充当用户与闪电节点之间的接口，提供一种简单、用户友好的方式来管理支付网络并与之互动。

将 LNbits 视为节点的 "wordpress 模块化框架"。它是一个易于管理的平台，以扩展功能为基础，您可以将其组合起来，用于多种用途。

将 LNbits 视为您自己的银行财务管理软件。您的节点提供支付渠道，而 LNbits 可扩展您的节点，使其能够运行不止一个节点自带的闪电钱包。这些钱包不一定属于您自己。比方说，你作为 LN 节点的运行者，已经有了足够的渠道流动性和资金，现在你想为你的朋友、家人、自己的商店或其他普通商户提供一些比特币银行服务。

您将为他们提供一种简单的方式，让他们在您的节点上开设一个 "银行账户"，而无需访问您节点上的其他钱包，也无需访问您节点上的所有流动性，只需访问他们的部分。您的节点（银行）只是他们支付（进出）的运输提供商。

注意：您的 "客户 "在您的节点上存入 LNbits 银行账户的所有资金都将直接进入您的节点 LN 通道。这意味着您才是这些资金的真正所有者。您将对他们的资金负有重大责任。不要邪恶地携款逃跑，也不要邪恶地收取高额费用。我们要干的是法币银行家，而不是互相干（比特币用户）。

# 演示平台

该演示可在 [https://legend.lnbits.com](https://legend.lnbits.com)上找到。该演示功能齐全，可用于了解闪电网络以及 LNbits 和 LNURL 的一般功能。虽然我们无法阻止您使用该演示，但我们希望您不要将其用于您的生产设置。我们不仅经常在服务器上测试新功能，而且还鼓励您以主权方式运行自己的节点和 LNbits。如果您认为运行一个节点过于繁琐，您可以将 LNbits 连接到云中的托管资金服务，如 Opennode、Luna 或 Votage，或者连接到 Telegram 上的 Lightning Tipbot。

# LNbits 传单

想向您的商户或建筑商朋友提供一些基本信息吗？我们非常高兴地宣布，我们的第一份宣传单可供大家使用。该传单的尺寸是全球典型的传单格式，共 6 页（2 折），宽 3508，高 2480px。

LNbits for merchants：[EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits for Builder：[EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# 一些基本知识

LNbits 基于 LNURL 协议工作，这意味着请求以两种形式有效：一种是 https://clearnet 链接（不允许自签名证书），另一种是 http://v2/v3 洋葱链接。要提供可在野外使用的 LNbits 服务（如 LNURLp/w QR 码或 NFC 卡），您需要将 LNbits 开放到 clearnet (https)。

在安装 LNbits 之前，请务必阅读并理解以下关于 LNbits 及其可能性的一般指南。


- [LND 指南](https://docs.lightning.engineering/) | 安装 LND
- [LND 配置示例](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND 设置
- [CLN 指南](https://docs.corelightning.org/docs/installation) | 安装 CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Run a Watchtower](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | 非常重要！

更多在特定使用场景中使用 LNbits 的详细指南，请点击此处：


- [LNbits 入门](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [使用 LNbits 保障您的安全](https://youtu.be/i5FQf96e6zg) | Youtube 视频
- [闪电网络上的私人银行](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | 子栈指南
- [为您的亲朋好友运行托管钱包](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [小型餐馆/酒店的 LNbits](https://darthcoin.substack.com/p/lnbits-for-small-merchants)｜Substack 指南
- [使用 LNbits Streamer 副驾驶员](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack 指南
- [用 LNbits 启动您的 NOSTR 市场](https://darthcoin.substack.com/p/lnbits-nostr-market) | 子栈指南
- [在学校项目或节日活动中使用 LNbits](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)分包指南

# 安装 LNbits

## 基本安装指南

LNbits 可安装在任何 Linux 操作系统机器上。它不需要功能强大的机器或服务器，只需要足够的内存和磁盘空间来存放数据库。它可以与 BTC/LN 节点（本地 PC 或远程 VPS）分开运行，也可以与 BTC/LN 节点一起安装在同一台机器上，或者已经安装在捆绑节点软件的机器上。

你可以选择最常用的软件包管理器，如 poetry 和 nix。LNbits 默认使用 SQLite 作为数据库。你也可以使用 PostgreSQL，建议高负载应用程序使用 PostgreSQL。[以下是使用 poetry 或 nix 进行基本安装的指南](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)。

对于新手，您可以找到更详细的分步指南，让您的 LNbits 在特定环境中运行：


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [VPS 上的 LNbits](https://github.com/TrezorHannes/vps-lnbits)，作者：Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) by Leo

您还可以在[在 VPS 上使用 PostgreSQ 进行 dockerised 安装，使用 nginx 将 LightningTipBot 作为资金来源](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) 上找到视频。

[此处有更多安装场景](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server)。

关于捆绑软件节点，请参阅其有关 LNbits 的具体文档：[Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

如果你不懂技术，既不想自己托管资金来源，也不想托管你的LNbits，你可以使用[LNbits SaaS版](https://saas.lnbits.com)（软件即服务）。它基本上就像云中的 LNbits，但您可以自己定义资金来源（例如您的节点、LNbits 钱包、LNtipbot、fakewallet 等）和环境变量，而其他云解决方案大多不具备这种功能。

[这里有一份如何在特定用例中使用 LNbits SaaS 的详细指南](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)。

## 资金来源

LNbits 并非节点管理软件，而是在 LND 或 CLN 资金来源基础上开发的以 LN 为中心的会计系统。首次安装后，您可以访问 http://localhost:5000/ 上的 LNbits。

要修改资金来源，请访问超级用户 URL 并在 "管理服务器 "中选择资金来源，或者编辑 .env 文件，将 "LNBITS_BACKEND_WALLET_CLASS "修改为您需要的资金来源（如果您在".env "中设置了 "adminUI=TRUE"）。

通过 "ls -a "扩展命令来列出目录中的文件，就能在 lnbits/ 或 lnbits/apps/data 文件夹中找到 .env 文件。

您可能还需要安装其他软件包或执行其他设置步骤，选择所需的资金来源。重新启动后，您的新设置将被激活。

LNbits 可以使用哪些资金来源？

LNbits 可在多种闪电网络资金来源之上运行。目前，LNbits 支持 CoreLightning、LND、LNbits、LNPay 和 OpenNode，并将定期添加更多支持。

重要的是，要选择一个具有良好流动性和良好同行关系的来源。如果您使用 LNbits 提供公共服务，您的用户的付款才能双向愉快地流动。

后端钱包（资金来源）可使用以下 LNbits 环境变量在`.env`文件中或超级用户账户中的 Manage-Server 部分进行配置。

如果您想使用 .env 版本，可以在这里找到参数：

### 核心照明


- CLN
  - lnbits_backend_wallet_class`： **CoreLightningWallet**
  - corelightning_rpc`：/file/path/lightning-rpc
- 火花（c-闪电）
  - lnbits_backend_wallet_class`： **火花钱包**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - SPARK_TOKEN：访问密钥

### 闪电网络守护进程


- LND (REST)
  - lnbits_backend_wallet_class`： **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - lnd_rest_cert`：/file/path/tls.cert
  - lnd_rest_macaroon`：/file/path/admin.macaroon 或 Bech64/Hex
  - LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - lnbits_backend_wallet_class`： **LndWallet**
  - LND_GRPC_ENDPOINT"： ip_address
  - LND_GRPC_PORT：端口
  - lnd_grpc_cert`：/file/path/tls.cert
  - lnd_grpc_macaroon`：/file/path/admin.macaroon 或 Bech64/Hex

您也可以使用 AES 加密的 macaroon（更多信息），方法是使用


  - LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

要加密 macaroon，请运行`./venv/bin/python lnbits/wallets/macaroon/macaroon.py`。

### LNbits（另一个 LNbits 实例）


- 托管在云服务器或您自己的家庭服务器上的 LNbits 实例
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - `lnbits_endpoint`: https://lnbits.mydomain.com
  - LNBITS_KEY： my-lnbits-AdminKey
- LNbits Legend 演示服务器（切勿将此服务器用于生产/商业用途，仅用于测试！！）。
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - `lnbits_endpoint`: https://legend.lnbits.com
  - LNBITS_KEY：legend-lnbits-AdminKey

### 闪电提示机器人

要从 Telegram 连接 [Lightning Tipbot](https://t.me/LightningTipBot)，您需要设置以下参数：


  - lnbits_backend_wallet_class`： **LnTipsWallet**
  - `lnbits_endpoint`: https://ln.tips
  - LNBITS_KEY`：要获得密钥，你需要在 Telegram 上与 LightningTipbot 私聊时运行一次 /api。

另请参阅本教程，了解如何通过 vps 安装 [LNbits 和 LightningTipBot](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)。

### IBEX HUB

注册 [此处](https://ibexpay.ibexmercado.com/onboard)，然后从那里获取密钥/令牌，终点是 https://ibexpay-api.ibexmercado.com。

更多信息请参阅 [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

为使发票监听器正常工作，您必须在 LNbits 中设置一个可公开访问的 URL，并设置一个 [LNPay webhook](https://dashboard.lnpay.co/webhook/)，指向 `<您的 LNbits 主机>/wallet/webhook`，事件为 "钱包接收"，且不提供任何秘密。设置 `https://mylnbits/wallet/webhook` 将是收到付款通知的端点 url。


  - lnbits_backend_wallet_class`： **LNPayWallet**
  - lnpay_api_endpoint`: https://api.lnpay.co/v1/
  - LNPAY_API_KEY`: sak_apiKey
  - LNPAY_WALLET_KEY`: waka_apiKey

### 开放节点

要使发票生效，您需要在 LNbits 中设置一个可公开访问的 URL。网络钩子设置是可选的。


  - lnbits_backend_wallet_class`： **OpenNodeWallet**
  - `opennode_api_endpoint`: https://api.opennode.com/
  - OPENNODE_KEY：opennodeAdminApi 密钥

### 阿尔比

Alby 是一个浏览器扩展，具有 LN 钱包功能和 LNDHUB 账户，可用作 LNbits 的资金来源。[更多详情请点击这里](https://getalby.com/)。

要使发票生效，您必须在 LNbits 中拥有一个可公开访问的 URL。无需手动设置 webhook。您可以在此处生成 Alby 访问令牌： https://getalby.com/developer/access_tokens/new


- lnbits_backend_wallet_class`：AlbyWallet
- `alby_api_endpoint`: https://api.getalby.com/
- alby_access_token`：访问令牌

## 其他 / 故障排除指南

下面是一些补充说明，以备不时之需。点击箭头展开说明。

### Killswitch 🚨

最近，不仅在整个金融领域，在 LNbits 中也出现了许多危险的漏洞，因此我们决定对此采取一些措施。现在，当可能导致资金损失的漏洞或错误再次出现时，您可以选择接收警告和/或直接采取行动。

![killswitchn](assets/lnbits-killswitch.webp)

如果切换到 void-wallet，实例上的所有用户类型都会看到黄色横幅，通常在主题/语言区域右上方的 "LNbits 正处于测试阶段 "通知旁边--这是最明显的提示，说明发生了什么。请查看窗口左侧绿色突出显示的新服务器标签。

它是如何工作的？启用杀毒开关后，LNbits 核心团队将每隔 X 分钟（可指定）检查一次仅对 LNbits 核心团队开放的秘密 github 仓库。如果该仓库中出现漏洞，它就会作为一个信号，触发所有订阅安装的杀毒开关，并将你的 LNbits 实例转换为使用无效钱包。如果云层已经清空，并且你已经安装了安全更新，你就可以通过管理服务器部分将资金来源设置为你的节点、钱包或任何你正在使用的东西。如果你不知道该如何配置，本维基中有关于切换资金来源的部分。

### 管理员和超级用户的区别

LNbits 管理用户界面可让您通过 LNbits 前端更改 LNbits 设置。默认情况下它是禁用的，当你第一次在 .env 文件中设置环境变量 `LNBITS_ADMIN_UI=true` 时，设置将被初始化并使用。此后将使用数据库中的相应设置，而不是 .env 文件中的设置。

### 超级用户

通过管理用户界面，我们引入了超级用户，它拥有服务器访问权限，因此可以通过前端和 api 更改可能导致服务器崩溃或无响应的设置，例如更改资金来源。超级用户只存储在数据库的设置表中。设置 "重置为默认值 "并重新启动后，就会创建一个新的超级用户。我们还为 API 路由添加了一个装饰器，用于检查超级用户是否存在。其 ID 不会通过应用程序编程接口和前端发送，只会接收一个 bool（是/否）来判断您是否是超级用户。

只有超级用户才可以通过 "充值 "版块向不同的钱包充值。

您也可以在创建超级用户时通过 webhook 将其发布到另一个服务。更多信息请见 https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `类 SaaSSettings`.

在前台，您还可以打开 "管理服务器 "部分，选择 "主题"->"自定义徽标"，更改 "创建钱包 "页面上显示的商店图像。

### 管理员用户

环境变量：LNBITS_ADMIN_USERS"，逗号分隔的用户 ID 列表。管理员用户可以更改管理界面中的设置 - 但资金来源设置除外，因为这需要重启服务器，并可能导致服务器无法访问。此外，他们还可以访问 `LNBITS_ADMIN_EXTENSIONS`中专门为他们设置的所有扩展。

### 允许用户

环境变量：LNBITS_ALLOWED_USERS"，逗号分隔的用户 ID 列表。通过定义这些用户，LNbits 将不再对公众开放。只有定义的用户和管理员才能访问 LNbits 前端。

#### 更新 LNbits

只需复制粘贴以下 CLI 命令，即可正常更新 LNbits 本地实例：

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

如果运行 Raspiblitz 或 MyNode，您可能还需要一个

```
sudo systemctl restart lnbits
```

结尾，因为它将 LNbits 作为一项服务运行。

在 Umbrel/Citadel 上的命令是

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### 从 SQLite 迁移到 PostgreSQL

如果您已经在 SQLite 数据库上安装并运行 LNbits，我们强烈建议您迁移到 postgres，以便大规模运行 LNbits。

附带的脚本可以轻松完成迁移。你需要已经安装了 Postgres，而且应该有用户密码（参见上文的 Postgres 安装指南）。此外，在迁移之前，你的 LNbits 实例需要在 Postgres 上运行一次，以实现数据库模式：

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

希望现在一切都能正常运行并完成迁移...再次启动 LNbits，检查一切是否正常。

#### 备份和恢复数据库

请参阅 [关于备份和还原过程的详细指南](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore)。

#### 从我的节点为我的 LNbits 钱包注资不起作用

如果要从作为 LNbits 资金来源的同一节点发送卫星，则需要编辑 lnd.conf 文件。

需要包含的参数有允许循环路径=1

请在 lnd.conf 中的应用程序选项部分这样做。否则，在某些捆绑节点上，LND 的启动可能会失败。

注意：建议使用新的 adminUI 扩展和 "充值 "选项为 LNbits 账户充值。

#### 错误 426

我遇到了错误："lnurl 需要通过可公开访问的 https 域或 tor 传输。需要 426 次升级"</摘要

出现这种错误通常是因为在 ngnix 隧道后面的 LNbits 没有正确转发 LNURL 地址。停止 LNbits 并编辑 .env 文件，添加这一行：

`forwarded_allow_ips=*`

此外，如果使用 ngnix 设置，请确保在 ngnix 配置中包含这些头文件：

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### 网络错误

扫描 QR 时出现 "https 错误"、"网络错误 "或其他错误</摘要

坏消息，这是一个路由错误，可能有很多原因。首先用 [Lightning Decoder](https://lightningdecoder.com/)检查 QR 的 LNURL，看看有没有什么奇怪的地方。让我们尝试几个最有可能的问题及其解决方案。

LNbits 只能通过 Tor 运行，无法在 lnbits.yourdomain.com 等公共域名上打开。


- 鉴于您希望您的设置保持如此，请使用 .onion URI 打开您的 LNbits 钱包并再次创建。这样生成的 QR 就可以通过这个 .onion URI 访问，因此只能通过 tor 访问。请勿通过 .local URI 生成 QR，因为它无法通过互联网访问，只能通过家庭局域网访问。
- 打开用于扫描 QR 的 LN 钱包应用程序，这次使用 tor（请参阅钱包应用程序设置）。如果应用程序不提供 tor，您可以使用 Orbot（安卓）代替。有关如何使用 clearnet/https 打开 LNbits 的详细说明，请参阅安装部分。

#### 防止他人在我的 LNbits 上生成钱包

当您在 clearnet 中运行 LNbits 时，基本上每个人都可以在上面生成一个钱包。由于您节点的资金与这些钱包绑定，因此您可能希望防止这种情况发生。有两种方法可以做到这一点：

在 `.env` 文件中配置允许的用户和扩展名（[参见此处的 env 示例](https://github.com/lnbits/lnbits/blob/main/.env.example)）。只有在 .env 文件中使用 `adminUI=FALSE` 设置时才会起作用，否则需要在 "管理服务器 "部分 -> "用户"->"允许的用户 "中进行设置。之后其他人将无法使用。

#### 自定义发票到期时间范围

现在，您可以生成自定义有效期的发票。与后端兼容：目前已兼容 LndRestWallet、LndWallet、CoreLightningWallet、EclairWallet、LnbitsWallet 和 SparkWallet！

您可以在 .env 文件中设置 "LIGHTNING_INVOICE_EXPIRY"，或使用管理界面更改所有发票的默认值。在 /api/v1/payments 端点中还有一个新字段，您可以在 JSON 数据中设置过期时间。

## 已删除 Wallet-URL

### 演示服务器 legend.lnbits 上的钱包

请务必将您的钱包URL、Export2phone-QR或LNDhub的副本保存在安全的地方。如果丢失，LNbits 无法帮助您找回。

### 自己的资金来源/节点上的钱包

请务必将您的钱包 URL、Export2phone-QR 或 LNDhub 的副本保存在安全的地方。你可以在 LNbits 用户管理器扩展或 sqlite 数据库中找到所有 LNbits 用户和钱包 ID。要编辑或读取 LNbits 数据库，请进入 LNbits /data 文件夹，找到名为 sqlite.db 的文件。你可以用 excel 或专门的 SQL 编辑器（如 [SQLite 浏览器](https://sqlitebrowser.org/)）打开并编辑它。

您还可以通过 cli 转储钱包，查看数据库中的每个钱包。

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

输出结果如下

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

您想把这些值放到一个 url 中，就像这样

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

其中，将 f8a43fc363ea428db5c53b3559935f1f 替换为名称前面的值（在我们的示例中为 f8a43fc363ea428db5c53b3559935f1f），1280ff5910a9c485a782a2376f338b6c 是您的用户，应成为名称后面显示的值。要退出 sqlite3，请输入

```
.quit
```

#### 反之亦然。

试试 fiatjaf 提供的 [encoder](https://lnurl-codec.netlify.app/) 或 [this one](https://lightningdecoder.com/).要支付或检查 LNURLp，也可以使用 [LNurlpay](https://wwww.lnurlpay.com/)。应说明是 HTTPS 而不是 HTTP。

#### 配置人们在向我的 LNURLp QR 付款时看到的注释

创建 LNURL-p 时，默认情况下不填写注释框。这意味着付款时不允许附加注释。

要允许发表评论，请添加评论框的字符长度，从 1 到 250 不等。输入数字后，评论框将显示在付款过程中。您也可以编辑已创建的 LNURL-p 并添加该数字。

![lnbits comments](assets/lnbits-comments.webp)

#### 将链上 BTC 存入 LNbits

有两种方法可将 sats 从 onchain BTC 兑换成 LN BTC（或 LNbits）。

##### 通过外部交换服务。

其他无法访问您的 LNb 的用户可以使用交换服务，如 [Boltz](https://boltz.exchange/)、[FixedFloat](https://fixedfloat.com/)、[DiamondHands](https://swap.diamondhands.technology/) 或 [ZigZag](https://zigzag.io/)。如果您在 LNbits 实例中只提供 LNURL/LN 发票，但付款人只有链上 sats，因此他们必须先在自己这边交换这些 sats，这就很有用了。程序很简单：用户向交换服务发送链上比特币，并提供 LNbits 的 LNURL / LN 发票作为交换目的地。

##### 使用 Onchain 和 Boltz LNbits 扩展。

请记住，这是一个独立的钱包，而不是 LNbits 在您的 LN 资金来源中作为 "您的钱包 "所代表的 LN btc 钱包。通过使用 LNbits Boltz 或 Deezy 扩展，这个链上钱包也可用于将 LN btc 兑换到（例如您的硬件钱包）。如果您经营的网店与您的 LNbits 链接，用于 LN 支付，那么定期将 LN 中的所有 sats 放入 onchain 将会非常方便。这将为您的 LN 信道提供更多空间，以便接收新的 Sats。

为没有比特币硬件钱包的用户提供的程序：


- 使用 Electrum 或 Sparrow 钱包创建一个新的链上钱包，并将备份种子保存在安全的地方。
- 进入钱包信息，复制 xpub。
- 转到 LNbits - Onchain 扩展，用该 xpub 创建一个新的手表专用钱包。
- 进入 LNbits - Tipjar 扩展，创建一个新的 Tipjar。除 LN 钱包外，也选择 onchain 选项。
- 可选项 - 进入 LNbits - SatsPay 扩展，为 onchain btc 创建一个新的收费项目。您可以选择链上和 LN 或两者。然后会创建一张可以共享的发票。
- 可选项 - 如果您将 LNbits 链接到 Wordpress + Woocommerce 页面，一旦您创建/链接了手表专用钱包和 LN btc 商店钱包，客户就可以在同一屏幕上同时选择两种支付方式。

当您在 LNbits 收到付款时，交易日志将只显示交易的恢复类型。

![lnbits payment details](assets/lnbits-payment-details.webp)

在交易概览中，您会发现一个绿色小箭头表示已收到，红色箭头表示已发送资金。

如果您点击这些箭头，弹出的详细信息窗口会显示所附邮件以及发件人姓名（如果有的话）。

在 LNbits 中，要配置一个名字出现在付款中，目前是不可能的 - 但可以接收。只有当发件人的 LN 钱包支持 [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) 如 [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents)时，才可以这样做。

然后，您将在 LNbits 交易的详细信息中看到一个别名/假名（点击箭头）。请注意，您可以在这里给出任何名字，如果您收到的是真实发件人的名字，它可能与之无关。

![lnbits namedesc](assets/lnbits-namedesc.webp)

要在钱包应用程序中导入您的 LNbits 账户，请使用您要使用的账户/钱包打开 LNbits，进入 "管理扩展 "并激活 LNDHUB 扩展。打开 LNDHUB 扩展，选择要使用的钱包，然后根据钱包的安全级别扫描 "admin "或 "invoice only" QR。

您可以使用 [Zeus](https://zeusln.app/) 或 [Bluewallet](https://bluewallet.io/) 作为 lndhub 账户的钱包应用程序，其中 BW 支持多个此类钱包。

为此，我们建议将 LN 网络 URI 设置为您自己节点的 URI。如果你的 LNbits 实例仅支持 Tor，那么你也必须在激活 Tor 的情况下使用这些应用程序。在这种情况下，你还需要通过 Tor .onion 地址打开 LNbits 页面。

如果在链上扩展中使用 ypub 时出现 "不支持的哈希类型 "错误，请检查您的 LNbits 实例是否使用了 python 3.10，它可能受 [此问题](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python) 的影响。按照 stackoverflow 答案中的说明编辑 openssl.cnf，然后重启 LNbits。

## 使用 LNbits 制作工具和构建

LNbits 拥有各种[开放式 API](https://legend.lnbits.com/docs)和工具，可用于编程和连接到各种不同的设备，适用于数以亿计的用例。

初学制作时，可以从 Ben Arc 提供的有关基于 LNbits 制作小工具的 [MakerBits 演示](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) 开始。

### 重要的是


- LNbits 基于 LNURL 协议工作，该协议的请求以两种形式有效：一种是 https://clearnet 链接（不允许自签名证书），另一种是 http://v2/v3 洋葱链接。要提供 LNbits 服务，如 LNURLp/w QR 码或 NFC 卡（可在野外使用），您需要将 LNbits 开启到 clearnet (https)。
- 只能使用数据线为 esp32 供电。并不是所有电缆都能在为 esp 供电的同时支持数据，如果 esp 附带的电缆是只供电的，你就不是第一个了。
- 确保不要使用连接有其他设备的 USB 集线器。这会导致难以调试的怪异效果（例如无法启动或停止）。
- 要在 MacOS 上实现 esp 项目，您需要 UART 桥接器驱动程序。如果您在 Mac 或 Linux 系统上遇到驱动程序问题，可以在这里找到；如果涉及 TTGO 显示器，则可以在这里找到。如果在 Windows 系统上遇到连接问题，请务必下载旧版本的 11.1.0，因为新版本的驱动程序无法使用！您还可以在这里找到一个串行终端来检查连接情况--设置为波特率 115200。
- 尽管使用 Platform.io 会更方便（例如，依赖项会自动安装），但我们还是建议所有初学构建的人使用 Arduino。
- TT-Go 显示屏 S3：屏幕保护膜标签的颜色可以告诉您是使用哪个控制器（ST7735_redtab、ST7735_blacktag、ST7735_greetab、greentab128......）制作的。如果您在编程时发现屏幕不能正确显示图形，例如颜色错误、镜像图像或边缘有杂散像素，请保留它以便调试。如果你需要这样做，这里有一份针对不同显示器进行调整的史诗级指南
- 始终使用小写的 lnurl239xx，而不是 LNURLl239xx
- 添加 lightning:lnurl1234xyz 将创建一个 QR，要求在扫描时打开该发票的用户钱包（iOS 上最后安装的 lightning 应用程序，Android 中的设置）。
- 如果您通过网络闪存 esp32，则只能使用这些浏览器（TL:DR Chrome、Edge 和 Opera）。
- 请注意该 PIN-OUT 参考文献，以便为 esp
- 当您使用 FOSSoftware 或 FOSGuides 时，请务必链接作者。每个人都喜欢看着自己的宝贝成长，这也会启动一个令人印象深刻的建筑链:)

如果你在项目中需要帮助，请访问 [Makerbits Telegram 群组](https://t.me/makerbits) - 我们会帮你！

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

以下是您可以使用 LNbits 构建的一些项目类别：


- [Nostr签名设备](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade机器](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)。
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [闪电猪](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [硬件钱包](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [自动售货机](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [比特币行情](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [罗拉与网状网络](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [帮助与资源](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [这里有更多 "由 LNbits 支持 "的项目实例](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits)。
- [LNbits用例](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)