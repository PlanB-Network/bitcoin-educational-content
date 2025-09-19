---
name: Phoenixd
description: 使用 Phoenixd 部署自己的极简 Lightning 节点
---

![cover](assets/cover.webp)



财务自主还意味着控制您的Lightning基础设施。对于希望将Bitcoin Lightning集成到其应用程序中的开发人员和公司而言，**Phoenixd**是理想的解决方案：一个具有自动流动性管理功能的简约、专用Lightning节点。



Phoenixd是ACINQ开发的Lightning服务器，专门用于通过HTTP API发送和接收Lightning付款。与LND或Core Lightning等全功能实现不同，Phoenixd抽象了渠道管理的所有复杂性，同时保留了资金的自我保护功能。



在本教程中，我们将了解如何安装、配置和使用 Phoenixd，以便利用自托管基础架构和易于使用的 API 开发 Lightning 应用程序。



## 什么是 Phoenixd？



Phoenixd是ACINQ开发的一个最小化、专业化的Lightning节点。它是专为希望将 Lightning 集成到其应用程序中的开发人员和企业设计的解决方案，无需 Full node 的复杂管理。



### 工作原理



**Phoenixd是一个最小的闪电节点，它使用ACINQ作为其LSP（闪电服务提供商），以实现自动流动性。当您收到闪电付款时，它会自动打开与 ACINQ 节点的通道，以分配必要的输入容量。这种 "即时 "流动性是瞬时的，但收取的费用正好是所收金额的**1% + Mining 费用**。



**自动管理：** 系统管理三个关键的 Elements：




- 闪电**通道：根据需要自动打开、关闭和管理
- 输入/输出流动性**：通过拼接和通道开放自动提供
- 费用贷记** ：小额付款不足以证明渠道的合理性，将作为未来收费的准备金储存起来



### 凤凰城的好处



**您可以控制自己的私人密钥（12 个字的 seed）和资金。Phoenixd 在本地生成您的 Wallet，无需共享您的密钥。



**个人基础设施：** Phoenixd 在您的服务器上运行，让您可以访问详细的日志、配置和 API 控制。您不再依赖第三方服务来访问您的资金。



**集成应用程序接口：** Phoenixd 具有 HTTP 应用程序接口，可与其他服务、本地 LNURL 支持和定制应用程序开发集成。



**易于集成：** 由于其简单的 REST API，Phoenixd 可以集成到任何需要闪电支付的应用程序或服务中。



**重要说明：** 自动流动资金仍来自作为 LSP（闪电服务提供商）的 ACINQ。Phoenixd 使用与 Phoenix mobile 相同的机制进行自动渠道管理。



## 安装 Phoenixd



### 先决条件



Phoenixd 需要在 Linux 环境下运行（推荐使用 Ubuntu/Debian），并具备一些基本的命令行技能。为获得最佳性能，您需要 .NET Framework 2.0 或更高版本：





- Linux 服务器**：VPS 或连接稳定的本地机器
- OpenJDK 21** ：Java 运行环境
- 稳定的互联网连接**：用于与 Lightning Network 同步
- 域名**（可选） ：用于安全 HTTPS 访问应用程序接口



### 下载和安装



**1.下载 Phoenixd**



访问 [GitHub releases] 页面 (https://github.com/ACINQ/phoenixd/releases) 并下载适用于您的架构的最新版本：



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2.首次启动



启动 Phoenixd 进行初始化：



```bash
./phoenixd
```



首次启动时，系统会要求您输入 "我明白 "确认两个重要步骤：



*信息 1 - 备份：***


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**保存这 12 个字** - 这是你康复的唯一保证。



**信息 2 - 自动清算：**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



每次确认时都输入 "我明白"。



![Premier démarrage](assets/fr/01.webp)



*Phoenixd 首次启动：备份确认和自动流动性*。



**3.在役配置**（仅有法文版本）



若要连续运行，请创建 systemd .NET 文件：



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*通过 systemd 和 2m sat* 的 "自动流动性"，Phoenixd 服务已激活并投入运行



## 配置和安全



### 配置文件



Phoenixd 会自动创建包含基本参数的 `~/.phoenix/phoenix.conf`：



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**主要参数：**




- 自动流动性"：自动打开通道的大小（默认：200 万 Sats）
- http-password`：应用程序接口（Invoice 创建和付款发送）的管理员密码
- http-password-limited-access`：限制密码（仅限创建 Invoice）



### 使用 HTTPS 安全访问



默认情况下，只能通过本地 HTTP (`http://127.0.0.1:9740`)访问 Phoenixd API。要从外部（移动应用程序、其他服务器、网络集成）使用您的节点，您需要配置安全的 HTTPS 访问。



**反向代理原则：**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** 充当**反向代理**：它通过 443 端口监听来自互联网的 HTTPS 请求，将其重定向到本地的 Phoenixd（9740 端口），然后将加密后的响应发送回客户端。



**SSL/TLS** 证书是一个数字文件，.NET Framework 4.0 支持该文件：




- 证明服务器身份**（防止中间人攻击）
- 启用 HTTPS** 加密：包括 API 密码在内的所有数据在传输过程中均已加密
- 由 Let's Encrypt 通过 certbot 工具免费签发**



这种配置允许您 ：




- 从互联网安全访问应用程序接口**
- 在传输过程中加密 API** 密码（防止密码以明文传输）
- 将 Phoenixd** 集成到需要 HTTPS 的外部应用程序中
- 遵守金融应用程序接口的安全标准**



使用 nginx 配置 HTTPS 反向代理：



**1.Nginx** 配置



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2.SSL** 证书



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### 功能测试



检查 Phoenixd 是否正常工作：



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



这些命令应返回有关节点状态和余额（最初为空）的 JSON 信息。



![Commandes CLI](assets/fr/03.webp)



*用于检查节点状态的 Getinfo 和 getbalance 命令*



## 使用应用程序接口



### 首次接收测试



**1.创建闪电** Invoice



使用应用程序接口创建第一个 Invoice：



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### 了解自动清偿机制



**基本原理：** 当您收到闪电付款时，Phoenixd 有时需要打开一个新通道才能收到付款。打开通道需要支付一定费用，该费用**自动从收到的金额中扣除。



**100,000 GW 的具体例子-13:**



![Premier test de réception](assets/fr/04.webp)



*首次验收测试：收到 Sats 10 万欧元，扣除流动资金费用后，Sats 最终余额为 75.561 欧元*。



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**费用计算：**




- 服务费**：渠道容量的 1%（2,115,000 千兆瓦-15）= 21,150 千兆瓦-15
- Mining 费用**：~3,289 Sats（用于 On-Chain 交易）
- 总计**：24,439 Sats 自动扣除



**使用 CLI 命令进行验证：**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*付款后的最终余额：闪电发货后剩余 257 Sats*



**小额付款的费用抵免：** 如果您收到的付款数额太小，不足以开通频道（< 约 25k Sats），则这些付款将存储在不可退还的 "费用抵免 "中。当您收到足够数额的款项时，该信用额将用于支付未来的频道费用。



**2.按照通道开口**



观看 Phoenixd 日志：



```bash
journalctl -u phoenixd -f
```



您将看到通道的开通和流动性费用的自动扣除。费用因 Mempool Bitcoin 条件而异，但始终包括 1%的服务费和当前的 Mining 费用。



**3.检查通道**



```bash
./phoenix-cli listchannels
```



该命令显示活动频道的状态和余额。



### 完成应用程序接口操作



Phoenixd 通过 9740 端口提供 REST 应用程序接口，使 .NET 开发人员能够使用 Phoenixd：



**基本操作：**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**重要费用：**




- 收款**：1% + Mining 自动清算费
- 运费**： 0.Lightning Network运费的4%路由费



**Webhooks：** Webhooks使Phoenixd能够在事件发生时（收到付款、支付Invoice、通道打开等）自动通知**您的应用程序。您的应用程序将收到即时的 HTTP 通知，而无需不断地向 Phoenixd 请求更新。



**当客户为订单付款时，您的在线商店会自动收到通知，以便即时验证交易。



phoenix.conf "中的配置：


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## 高级应用



### LNURL 集成



Phoenixd 本机支持 LNURL 协议，可实现高级集成：



**LNURL-Pay:** 为兼容 LNURL 的服务付费


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** 从 LNURL 服务检索资金


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** 通过 Lightning 验证访问服务


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### 与 LNbits 集成



根据其 [官方文档](https://docs.lnbits.org/guide/wallets.html)，LNbits 可以使用 Phoenixd 作为资金来源：



**LNbits 配置：**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



通过这种集成，您可以创建由 Phoenixd 节点驱动的 LNbits 子账户，提供基于网络的 Interface 以管理多个闪电钱包。



### 定制应用



得益于其全面的 REST API，您可以开发.NET 应用程序：



**电子商务：** 将闪电支付直接集成到您的商店中


**捐赠服务：** 带有发票和自动网络钩子的捐赠系统


**社交网络机器人：** 具有提示功能的 Telegram/Discord 机器人


**付费墙闪电：** 只需支付闪电费用即可获得高级内容



## 安全和最佳做法



### 访问保护



**API 密码：** 自动生成的密码是 "闪电 "宝库的钥匙。切勿共享密码，如有疑问，请更改密码。



**防火墙：** 切勿让 9740 端口直接连接互联网。始终使用带有 HTTPS 的 nginx。



**增强身份验证：** 考虑使用 VPN 或 Tailscale 来限制只有授权设备才能访问服务器。



### 重要备份



**seed 恢复：** 将您的 12 个单词保存在服务器外的安全位置。这是您恢复的唯一保证。



*~/.phoenix 目录：** 定期（在 Phoenixd 关闭后）备份此文件夹，以保留通道状态并加快恢复速度。



**服务恢复代码：** 还请保留您与凤凰卫视激活 2FA 的所有服务的备份代码。



### 监测和维护



**监测日志：**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**更新：** 关注 [GitHub releases](https://github.com/ACINQ/phoenixd/releases) 以获取新版本。更新只需替换二进制文件并重启服务即可。



## 与替代品的比较



### Phoenixd 与 Phoenix 标准



**凤凰标准（移动）：**




- ✅ 立即安装，零配置
- ✅ Interface 移动直观型
- ✅ 与 Phoenixd 相同的自动保存功能
- ❌ 没有面向开发人员的应用程序接口
- ❌ 无法访问详细日志



**Phoenixd（服务器）：**




- ✅ 用于集成的 HTTP API
- ✅ 完全访问日志
- 个人基础设施
- ❌ 需要技术技能
- ❌ 需要维护服务器



**两者都使用 ACINQ 作为自动流动性的 LSP。



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ 全面控制，完整的闪电协议
- ✅ 大型社区，成熟的生态系统
- ❌ 复杂的人工流动性管理
- 学习曲线大



**Phoenixd :**




- 自动流动性管理（如 Phoenix mobile）
- ✅ 面向开发人员的应用程序接口
- ✅ 简化配置
- ❌ 将 ACINQ 用作 LSP（无独立路由选择）
- ❌ 灵活性低于完整节点



## 解决常见问题



### 应用程序接口访问问题



**验证失败 "错误：**


1.检查文件 `~/.phoenix/phoenix.conf` 中的密码


2.检查验证格式 `-u:password`


3.确保 Phoenixd 正在运行 (`./phoenix-CLI getinfo`)



**连接超时：**




- 检查 Phoenixd 是否在正确的端口（9740）上监听
- 在配置 HTTPS 之前测试本地访问
- 检查日志：journalctl -u phoenixd -f



### 流动性问题



**付款未到：**


1.检查金额是否超过最低阈值（~30k Sats）


2.查看日志以确定通道错误


3.必要时重启 Phoenixd



**贷方支出 "余额：**


小额付款作为备付金存储。收到较大金额时，会触发通道开放并释放这些资金。



## 结论



Phoenixd 是易用性与开发人员技术主权之间的绝佳折衷方案。它提供了简单而强大的 Lightning API，具有自动流动性管理功能，消除了传统 Lightning 节点的复杂性。



该解决方案尤其适合希望实现 .NET 技术的开发人员和公司：




- 将 Bitcoin Lightning 集成到您的应用程序中
- 避免 "闪电 "渠道管理的复杂性
- 受益于自主托管的基础设施
- 简单可靠的应用程序接口



有了Phoenixd，您就可以利用现代化的REST API和技术方面的自动管理，构建自己的私有Lightning基础架构。这是实现项目中Lightning集成民主化的理想解决方案。



## 有用资源



### 正式文件




- GitHub Phoenixd** ：[github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - 源代码和发行版
- 凤凰服务器**站点：[phoenix.acinq.co/server](https://phoenix.acinq.co/server) - 完整文档
- 常见问题 Phoenixd** ：[phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - 常见问题



### 社区支持




- GitHub 问题** ：[github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - 技术支持
- Twitter ACINQ** ：[@ACINQ_co](https://twitter.com/ACINQ_co) - 新闻和公告