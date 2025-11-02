---
name: LNbits 服务器
description: 在带有 PHOENIXD 的 Ubuntu VPS 或 Umbrel 上安装和配置自托管 LNbits 服务器
---

![cover](assets/cover.webp)



LNbits是一个开源的Interface网络应用程序，可将任何Lightning后端（LND、Core Lightning、PHOENIXD）转化为一个完整的服务平台。这种自托管解决方案使您能够独立管理多个Lightning投资组合、部署销售点、创建捐赠系统或计费服务，同时保持对资金的完全控制。



本教程包括两种安装方法： **VPS Ubuntu 与 PHOENIXD**（无需完整 Bitcoin 节点的轻量级解决方案）和 **Umbrel**（与现有 LND 节点集成）。与 Plan B Network 的一般 LNbits 教程（涵盖概念和扩展）不同，本指南侧重于分步技术安装程序。



## 什么是 LNbits？



LNbits 是一个用 Python（FastAPI）开发的 Lightning 会计系统，可连接到现有的后台（LND、Core Lightning、PHOENIXD）。与传统的 Lightning 节点不同，LNbits 提供了一个可访问的 Interface，使您能够用自己的 API 密钥管理多个独立的投资组合。您可以为家人、员工或项目创建子账户，而无需让他们接触到您的所有资金。



解耦架构将信息存储在 SQLite（默认）或 PostgreSQL（生产）中，而资金仍由 Lightning 后台管理。这种分离保证了可移植性：您可以从 PHOENIXD 迁移到 LND，而不会丢失用户数据。



## 主要特点



LNbits 提供多功能**扩展系统**：TPoS（销售点）、Paywall（内容货币化）、Events（票务）、LndHub（BlueWallet 服务器）、Bolt Cards（NFC 支付）、Split Payments（自动分发）和 User Manager（带身份验证的用户管理）。



仪表板**显示实时余额、交易历史和计费工具。每个 Wallet 都有一个包含 API 密钥的唯一 URL，无需传统登录即可访问。三级 API 密钥系统**（管理员、Invoice、只读）为安全集成提供了细粒度的权限控制。



LNbits本机实现了**LNURL**（LNURL-pay、LNURL-Withdraw、LNURL-auth），并支持**Lightning Address**，保证了与现代闪电钱包的兼容性，促进了专业服务的部署。



## 支持的平台



**Ubuntu VPS**：无需完整 Bitcoin 节点的轻量级解决方案。前提条件：1 vCPU、1-2 GB 内存、Ubuntu 22.04 LTS、Python 3.10+、Git、UV。需要使用 HTTPS + 域名进行公开（LNURL 服务）。



**不使用**：从应用程序商店轻松安装。前提条件：具有同步 LND 和开放通道的功能性 Umbrel 节点。自动配置。



下面是 Umbrel 和 Umbrel LND 教程的链接：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 在 Ubuntu VPS 上安装 PHOENIXD



### 步骤 1：保护 VPS 服务器



**在安装**之前，您需要根据技术规则确保 Ubuntu VPS 服务器的安全。这一步对于保护您的基础设施和 "闪电 "资金至关重要。



以下是一份详细的入门指南： **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** 作者：Daniel P. Costas。



本指南涵盖用户配置、安全 SSH、防火墙 (UFW)、fail2ban、自动更新和良好的系统安全实践。



### 步骤 2：安装 PHOENIXD



服务器安全后，您需要安装和配置 PHOENIXD。Plan B Network 提供完整的专门教程，涵盖安装、seed 生成和 systemd 服务配置：



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

一旦 PHOENIXD 启动并运行（使用`./Phoenix-CLI getinfo`检查），请注意`~/.Phoenix/Phoenix.conf`中的**HTTP 密码** - 您需要用它将 LNbits 连接到 PHOENIXD。



### LNbits 部署



安装 UV 并克隆 LNbits ：


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



配置 PHOENIXD 后端：


```bash
cp .env.example .env && nano .env
```



添加到 `.env` 中：


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



使用 `uv run lnbits --host 0.0.0.0 --port 5000` 进行测试，然后使用 `Wants=PHOENIXD.service` 创建 systemd 服务。



## 初始设置和首次使用



### 超级用户激活



在 `.env` 中激活 Interface 管理员：


```
LNBITS_ADMIN_UI=true
```



重启 LNbits（"sudo systemctl restart lnbits"）并获取超级用户 ID：


```bash
cat ~/lnbits/data/.super_user
```



访问 `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` 管理面板。通过 "服务器 "菜单，您可以配置资金来源、扩展名和用户账户。



### 安全创建账户



**对公开暴露**重要：如果您要将 LNbits 实例公开在可从互联网访问的公共域名上，那么**重要的**就是禁止免费创建用户账户。



从超级用户管理 Interface 进入 "设置"，然后进入 "用户管理 "部分。您会发现 "允许创建新用户 "选项。



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**用于公开展览的域名** ：




- 必须禁用**"允许创建新用户 "选项
- 如果没有这种保护，互联网上的任何人都可以在您的实例上创建账户
- 攻击者可以在您不知情的情况下创建账户并使用您的 LIGHTNING NODE 的流动性
- 您需要从 Interface 超级用户手动创建用户账户。



**仅供当地使用** ：




- 如果您的实例只能在本地访问 (http://localhost:5000) ，则此选项就不那么重要了。
- 不过，禁用该选项是一种良好的常规安全做法



配置完成后，只有超级用户管理员才能通过 Interface "用户 "创建新的用户账户。这种方法保证了对谁能访问 Lightning 基础设施和使用资金的全面控制。



### 打开第一个通道



PHOENIXD 通过自动流动性自动管理渠道。generate 从 LNbits 购买约 30,000 Sats 的闪电 Invoice，并从另一个 Wallet 支付。PHOENIXD 自动为 ACINQ 开通一个通道。开通费（~20-23k Sats）被扣除，余额（~7-10k Sats）在 On-Chain 确认后出现。



使用 `./Phoenix-CLI getinfo` 查看状态。然后考虑禁用自动流动性（`Phoenix.conf` 中的 `auto-liquidity=off`）来控制通道打开。



### 公开展示和 HTTPS



**重要**：公开显示必须使用 HTTPS（API 密钥安全性 + LNURL 兼容性）。仅在本地使用时跳过此步骤。



**Caddy（推荐）**：自动 SSL。sudo apt install -y caddy`, edit `/etc/caddy/Caddyfile` ：


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


重新启动：sudo systemctl restart caddy`。



**Nginx** ：更多控制。安装 `nginx certbot python3-certbot-nginx`，创建 `/etc/nginx/sites-available/lnbits` ：


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


激活： `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`.



在 `.env`中添加： `FORWARDED_ALLOW_IPS=*`



## 伞架安装



### 从应用程序商店部署



进入 Umbrel App Store，搜索 "LNbits"，点击 "安装"。



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel 会自动检查所需依赖项。LNbits 需要 LIGHTNING NODE (LND) 才能运行。如果您的 LIGHTNING NODE 已经运行，请点击 "安装 LNbits "确认。



![Dépendances LNbits](assets/fr/02.webp)



Umbrel 会下载 Docker 映像，自动配置与 LND 的连接，并启动容器（2-5 分钟）。安装完全在后台进行。



### 超级用户初始配置



首次启动时，LNbits 会提示您创建超级用户管理员账户。输入用户名并设置安全密码，以保护对 Interface 管理系统的访问。



![Configuration SuperUser](assets/fr/03.webp)



**重要**：该超级用户账户拥有 LNbits 实例的全部权限。请选择一个强大的密码并妥善保管。



创建账户后，您将自动进入 Interface 主管理区。Umbrel 已将 LND 设置为您的资金来源，所有 "闪电 "付款都将通过您现有的渠道进行。



### 访问 Interface 管理员



在左侧菜单中，点击 "设置 "进入完整的管理面板。



![Interface Settings](assets/fr/04.webp)



钱包管理 "部分显示有关配置的关键信息：




- 资金来源** ：LndBtcRestWallet （直接连接到您的 LND Umbrel 节点）
- 节点余额** ：您的 "闪电 "渠道中可用的流动资金总额
- LNbits 余额**：分配给 LNbits 系统的资金（最初为 0 Sats）



现在，您可以为您创建的所有 LNbits 钱包直接利用 Umbrel 节点的流动性。无需额外配置，LNbits 即可运行。



### 用户管理



LNbits 最强大的功能之一是能够创建多个独立用户，每个用户都有密码验证和独立钱包。这种架构可以利用 Umbrel 节点的流动性，同时为不同用途（企业、家庭、员工、项目等）提供完全独立的子账户。



在侧边菜单中点击 "用户 "进入用户管理。点击 "创建账户 "添加新用户。



![Gestion des utilisateurs](assets/fr/05.webp)



填写用户创建表：




- 用户名**：登录用户名（例如："Satoshi）
- 设置密码**：激活此选项可设置验证密码
- 密码**和**密码重复**：为该用户设置密码



![Création utilisateur satoshi](assets/fr/06.webp)



可选字段（Nostr 公钥、电子邮件、名、姓）可以留空，以便进行最少配置。点击 "创建账户 "确认。



![Confirmation utilisateur créé](assets/fr/07.webp)



现在，新用户会出现在用户列表中，并显示其唯一标识符和用户名。



![Liste des utilisateurs](assets/fr/08.webp)



**重要事项**：每个用户都可以使用自己的密码完全独立地登录。超级用户管理员可通过 Interface 管理工具进行完全控制。



### 用户 Wallet 管理



现在 "Satoshi "用户已经创建，您需要为他分配一个 Wallet Lightning。点击相关用户的 Wallet 图标（第二个图标），然后点击 "创建新 Wallet"。



![Gestion des wallets](assets/fr/09.webp)



对话框提示您为 Wallet 命名。输入一个描述性名称（如 "Satoshi 的 Wallet"）并选择显示货币（CUC、USD、EUR 等）。



![Création wallet](assets/fr/10.webp)



点击 "创建"。LNbits 会立即为该用户生成一个可用的 Wallet 闪电。



![Confirmation wallet créé](assets/fr/11.webp)



现在，您将看到两个现有钱包：自动创建的默认 Wallet "LNbits Wallet"，以及新的 "Wallet Of Satoshi"。为了简化用户体验，您可以点击删除图标（红色垃圾桶）删除默认的 Wallet。



![Wallet final unique](assets/fr/12.webp)



现在，"Satoshi "用户拥有一个单一的、明确标识的 Wallet。每个用户 Wallet 都可以完全自主运行，同时使用底层 LND 节点的流动性。



**主要概念**：所有这些钱包都共享您的 Umbrel 节点的全球流动性。您不需要为每个 Wallet 创建新的闪电通道，LNbits 将充当智能会计 Layer，在您现有的闪电基础设施内管理资金分配。这就是 LNbits 多 Wallet 系统的强大之处。



### 用户登录



注销超级用户账户（右上角图标）并返回 LNbits 登录页面。现在您可以使用新用户的凭据登录。



![Connexion utilisateur satoshi](assets/fr/13.webp)



输入用户名（"Satoshi"）和密码，然后点击 "登录"。用户可直接访问其个人 Wallet，与管理 Interface 完全隔离。



### 来自 Wallet 用户的 Interface



连接后，用户可通过 Wallet Lightning 访问其 Interface。



![Interface wallet utilisateur](assets/fr/14.webp)



Interface 的特点是 ：




- 当前余额**：以 Sats 和所选货币（本例中为 CUC）显示
- 主要操作**："粘贴请求"（粘贴要支付的账单）、"创建 Invoice"（generate 收据）、QR 图标（快速扫描）
- 交易历史** ：所有付款和收款的完整清单
- 右侧面板**：配置和访问选项



### Wallet 移动接入



右侧面板提供了一个特别实用的功能：移动访问 Wallet。展开 "移动访问 "部分，了解可用选项。



![Mobile Access](assets/fr/15.webp)



LNbits 提供了多种在智能手机上使用 Wallet 的方法：



**选项 1：兼容的移动应用程序




- 从 App Store 或 Google Play 下载 **Zeus** 或 **BlueWallet**
- 为该 Wallet 激活 LNbits 中的 **LndHub** 扩展名
- 使用手机应用程序扫描 LndHub QR 码连接 Wallet



**选项 2：通过手机浏览器直接访问**




- 用 QR 码导出到手机 "中显示的 QR 码包含 Wallet 的完整 URL，并集成了身份验证功能
- 用智能手机扫描此二维码，直接在手机浏览器中打开 Wallet
- 将页面添加到主屏幕，以便快速访问



**重要安全**：此 URL 包含全面访问 Wallet 的 API 密钥。切勿公开分享。请像对待 Bitcoin 私有密钥一样对待此 QR 代码 - 任何人扫描此 QR 代码都可获得 Wallet 的完整访问权限。



这项移动功能可将您的 LNbits Umbrel 实例变成您和您朋友名副其实的闪电 Wallet 服务器，同时由于您拥有自主托管的节点，您对自己的资金拥有完全的主权。



### 用户访问共享



这种多用户配置的主要用途是**与家人或亲密圈子**共享钱包。一旦创建了具有专用 Wallet 的用户（例如我们示例中的 "Satoshi"），您就可以与您信任的家庭成员共享这些登录凭据。



**Umbrel 上的访问安全**：在 Umbrel 上访问您的 LNbits 实例自然会受到保护，因为只能通过 .NET Framework 4.0 访问该实例：




- 在本地网络上** ：连接到同一 WiFi/以太网网络的家庭成员可以访问实例
- 通过 VPN**：如果使用 VPN（如在 Umbrel 服务器上配置的 Tailscale），授权用户可获得安全的远程访问权限



这种双重 Layer 保护（网络访问 + 用户身份验证）使 "允许创建新用户 "选项在 Umbrel 上变得不那么重要。只有已经可以访问网络或 VPN 的人才能访问 Interface 登录。



**典型情况**：您创建了一个 "爸爸 "账户、一个 "妈妈 "账户、一个 "企业 "账户等。每个家庭成员都有自己独立的 Wallet Lightning，同时受益于 Umbrel 节点的共享流动性。只需共享用户名和密码，用户就可以通过本地网络的任何设备或 Tailscale VPN 进行连接。更多信息，请参阅我们专门的 Tailscale 教程：



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 探索可用的扩展功能



返回 Interface 超级用户，访问左侧面板的 "扩展 "菜单，了解完整的 LNbits 扩展生态系统。



![Extensions disponibles](assets/fr/16.webp)



LNbits 提供丰富的扩展目录，可将您的实例转化为名副其实的闪电服务平台：





- 点唱机**：由 Sats 支持的点唱机系统（Spotify 支付）
- 支持票**：付费支持系统（接收 Satss 回答问题）
- TPoS**：面向零售商的安全移动销售终端
- 用户管理器**：高级用户和 Wallet 管理（我们刚刚使用过）
- 活动**：活动门票的销售和验证
- LNURLDevices**：销售点管理、ATM、连接交换机
- SMTP**：使用户能够发送电子邮件并赚取 Satss
- Boltcards**：为 Lightning 轻触式支付的 NFC 卡编程
- NostrNip5**：为您的域名创建 NIP5 地址
- 分割支付**：在多个钱包之间自动分配付款



只需点击一下 Interface 即可激活每个扩展。标有 "FREE "的扩展是免费的，有些则是 "付费 "版本。请浏览目录，找出符合您需求的扩展--无论是业务、家庭管理，还是试用 Lightning Network 的功能。



## 优势和局限性



**优势**：财务主权（完全控制资金/密钥/数据）、架构灵活性（无损 VPS→Full node 迁移）、专业扩展系统、直观的 Interface。



**限制** ：软件处于测试阶段（注意数量），安全由管理员负责，URL 包含敏感的 API 密钥（必须使用 HTTPS），多用户管理意味着监护责任。



## 最佳做法



**备份**：seed PHOENIXD/credentials LND、LNbits 数据库、`.env` 文件。每日自动备份，远离生产服务器，加密。定期测试还原。



**维护**：定期检查更新（LNbits、Lightning 后台、操作系统）。在重大更新之前，请务必查看发布说明。





- 在 Umbrel**：应用程序商店会自动通知您新版本。通过 "管理扩展" > "全部更新 "同步扩展。检查 Umbrel 自动备份中是否包含 SQLite 数据库。
- 在 VPS 上**：使用 `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits` 手动更新。监控系统日志：`sudo journalctl -u lnbits -f`.



## 结论



LNbits 自助托管为实现 "闪电 "金融主权提供了具体途径。VPS+PHOENIXD 为快速服务提供了轻量级解决方案，并与现有的 Bitcoin 节点完全集成。可扩展架构可从简单的多用户 Wallet 演进到复杂的业务用例。



自我托管意味着责任：备份种子、保护访问、从适量开始。有了这些预防措施，LNbits 将成为 "闪电经济 "的强大解决方案，同时保持去中心化和自主性。



## 资源



### 正式文件




- [LNbits文档](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [官方安装指南](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### 社区指南




- [Ubuntu服务器初始配置](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) 作者：Daniel P. Costas（逐步提高VPS安全性）
- [在 Ubuntu VPS 上安装 LNbits + PHOENIXD](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) 作者：Daniel P. Costas（完整指南）
- [Clearnet 上的 LNbits 服务器](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [VPS 上的 LNbits](https://github.com/TrezorHannes/vps-lnbits)，作者：Hannes