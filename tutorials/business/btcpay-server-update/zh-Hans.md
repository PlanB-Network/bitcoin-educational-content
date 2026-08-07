---
name: 更新 BTCPay Server
description: 为你的 BTCPay Server 实例应用安全更新，并轮换重要凭证
---

![封面](assets/cover.webp)

运行自己的支付处理器意味着你也是自己的安全团队。当 BTCPay Server 维护者发布安全版本时，没有人会替你修补你的实例：更新、验证以及随后进行的凭证轮换都需要由你来执行。

本教程会完整讲解整个流程，无论你以哪种方式部署 BTCPay Server：检查正在运行的版本、按你的部署类型应用更新、验证更新确实生效，并轮换攻击者可能在你的实例存在漏洞时捕获的秘密。

如果你还没有部署 BTCPay Server，请先从安装指南开始：

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## 2026 年 8 月的严重漏洞

⚠️ **严重安全警报（2026 年 8 月 7 日）：** 一个影响 BTCPay Server 的严重漏洞正被积极利用，并可能导致资金损失。请立即通过 `Admin Dashboard > Server > Maintenance > Update` 将你的实例更新到 **版本 2.4.2**，然后检查页脚是否显示 `2.4.2`。如果你无法立刻更新，请关闭你的 BTCPay Server。更新完成后，你还必须彻底刷新你的 Macaroon 和你的 `macaroons.db`，彻底刷新任何其他 Lightning 后端的身份验证字符串；如果你在 BTCPay Server 内部生成了一个热的链上钱包，请转移这些资金并重新创建钱包。集成方还应将 NBXplorer 更新到版本 2.6.10。来源：[BTCPay Server 2.4.2 发布说明](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)。

版本 2.4.2 于 2026 年 8 月 7 日发布。发布说明指出，它修复了一个已经在野外被利用的严重漏洞，该漏洞由 `brunoerg` 和 `benthecarman` 通过 Bitcoin Red Team 工作报告。同一个版本还修复了一个通过 Greenfield Basic 身份验证绕过 TOTP 双因素身份验证的问题，并默认在账户创建五分钟后禁用 Greenfield Basic 身份验证。

“正被积极利用”会带来两个后果：

- **更新不是可选项，也不是可以安排到下周再做的事情。** 一个可从互联网访问的未修补实例必须要么更新，要么关闭。
- **仅仅更新本身还不够。** 如果你的实例在修补前已被攻破，攻击者可能已经持有你的 Lightning 凭证副本，以及 BTCPay Server 为你生成的任何热钱包密钥材料。这些秘密在更新后仍然有效，直到你轮换它们。下面的轮换部分是人们容易跳过的部分，而它才是真正保护你资金的部分。

## 步骤 1 — 查明你正在运行哪个版本

登录你的 BTCPay Server，并查看**任意页面的页脚**：版本字符串会显示在那里。你也可以打开 `Admin Dashboard > Server > Maintenance`，其中会显示当前版本和更新控件。

如果你的实例暴露了 Greenfield API，`GET /api/v1/server/info` 也会返回版本。

任何低于 `2.4.2` 的版本都存在漏洞。

## 步骤 2 — 更新

### 自托管 Docker 部署（标准安装）

这涵盖官方 Docker 部署，也就是你从 BTCPay Server 文档、LunaNode 一键启动器以及大多数 VPS 安装中获得的部署方式。

最简单的路径是使用 Web 界面：

1. 前往 `Admin Dashboard > Server > Maintenance`。
2. 点击 **Update**。
3. 等待容器被拉取并重启。界面会有几分钟不可用。

如果 Web 界面无法访问，或者你希望查看日志，请通过 SSH 执行：

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

在默认安装中，`$BTCPAY_BASE_DIRECTORY` 是 `/root`，因此目录是 `/root/btcpayserver-docker`。该脚本会拉取最新镜像、重新创建容器，并打印生成的版本。

Docker 部署会随 BTCPay Server 一起附带 NBXplorer，因此标准更新也会将 NBXplorer 带到推荐的 `2.6.10`。如果你单独运行 NBXplorer——这在集成方和自定义技术栈中很常见——请显式更新它。

### Umbrel

打开 Umbrel 仪表板，前往 **App Store**，找到 BTCPay Server，并在有可用更新时应用更新。

⚠️ **重要：** 应用商店包由 Umbrel 团队重新打包，可能会比上游滞后数小时或数天。更新后，请检查 BTCPay Server 页脚中的版本。如果它仍低于 `2.4.2`，请从 Umbrel 仪表板**停止该应用**，等待打包版本发布，而不是让一个存在漏洞的实例继续运行。

专门的 Umbrel 指南涵盖该应用本身：

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

逻辑相同：从 StartOS 市场更新 BTCPay Server，然后在页脚中验证版本。如果打包版本还不是 `2.4.2`，请停止该服务，直到它达到该版本。

### 托管和第三方托管

如果是其他人在运营你的实例（托管服务商、协会、朋友的服务器），你仍然需要确认。请向运营方索要页脚中显示的版本字符串，并明确询问下面所述的更新后凭证轮换是否已经完成。“我们更新了”和“我们已经轮换了你的 Macaroon”不是同一个答案。

## 步骤 3 — 验证更新确实生效

重新加载 BTCPay Server 界面并读取页脚中的版本。它必须显示 `2.4.2` 或更高版本。

不要因为更新命令没有报错退出就相信它已经成功：在资源受限的机器上，镜像拉取可能静默失败，并让之前的容器继续运行。每一次都要读取版本。

## 步骤 4 — 轮换你的凭证

这一步会把“已修补”变成“安全”。由于该漏洞在修复发布前已经被利用，请把你的实例持有的每一个秘密都视为攻击者可能已经知晓。

### Lightning：LND

重新生成 Macaroon **以及** `macaroons.db` 文件。只删除 macaroon 文件还不够——LND 会从存储在 `macaroons.db` 中的根密钥派生 Macaroon，因此持有旧 macaroon 副本的攻击者会继续拥有访问权限，直到该数据库被重新创建。

流程如下：停止 LND，从网络目录中删除 `macaroons.db` 和 `*.macaroon` 文件（对于 mainnet，是 LND 数据目录内的 `data/chain/bitcoin/mainnet/`），然后重启并解锁 LND，它会重新创建这些文件。先备份该目录，并重新配对所有使用旧 Macaroon 的应用程序——BTCPay Server 本身、Zeus、Thunderhub、RTL、Alby，以及你编写的任何脚本。

如果你还将 LND 暴露在互联网之上，请同时检查它的 TLS 证书和任何 `lnd.conf` 凭证。

### Lightning：其他后端

任何使用字符串向你的节点进行身份验证的东西都必须获得新的字符串：

- **Core Lightning**：重新生成该连接使用的 rune 或访问凭证。
- **Phoenixd**：轮换 HTTP 密码。
- **LNbits 及类似工具**：撤销并重新签发管理员密钥和发票密钥。
- **存储在 BTCPay Server 商店设置中的远程节点连接字符串**：用新的秘密重写它们。

### 在 BTCPay Server 内部生成的热链上钱包

如果你让 BTCPay Server 为你生成链上钱包——而不是连接硬件钱包，或导入密钥从未接触服务器的 XPUB——那么该种子曾经存在于这台机器上。

请把它视为已经废弃：

1. 创建一个新钱包，最好使用硬件钱包，这样密钥就不会再次位于服务器上。
2. 将资金从旧钱包扫到新钱包。
3. 在商店设置中用新钱包替换派生方案。
4. 永远不要重复使用旧种子。

观察钱包设置（XPUB 或硬件钱包）不需要这样做：私钥从未在服务器上。这正是安装指南推荐它们的原因。

### BTCPay Server 账户和 API 密钥

趁此机会：

- 更改实例上每个用户账户的密码。
- 撤销并重新签发所有 Greenfield **API 密钥**。
- 重新注册双因素身份验证，因为 2.4.2 修复了一个 2FA 绕过问题。
- 打开 `Admin Dashboard > Server > Users`，检查是否存在任何意外账户。
- 检查最近的**支出**、**拉取支付**和**退款**，确认没有你未创建的条目。
- 检查你的 Webhook 及其秘密。

## 步骤 5 — 为下一次保持知情

安全版本只会帮助那些听说它们的运营者：

- 关注 [GitHub 上的 BTCPay Server 发布](https://github.com/btcpayserver/btcpayserver/releases)——GitHub 可以在仓库每次发布新版本时向你发送电子邮件。
- 关注该项目的公告渠道和[官方博客](https://blog.btcpayserver.org/)。
- 让你的实例保持在一个可以快速更新的版本上：你落后得越多，紧急更新就越痛苦。

自托管让你拥有对支付的主权。这种主权的代价正是如此：阅读发布说明，并成为那个亲自打补丁的人。
