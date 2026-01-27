---
name: BTCPay Server - Umbrel
description: 在 Umbrel 上安装和使用 BTCPay 服务器以接受 Bitcoin 和 Lightning
---

![cover](assets/cover.webp)



在 Bitcoin 生态系统中，接受支付是商家和企业面临的一大挑战。传统的解决方案，无论是银行业务（信用卡、Stripe、PayPal）还是 Bitcoin（BitPay、Coinbase Commerce），都会向中间商收取高额费用，收集您的敏感商业数据，并随心所欲地阻止或审查您的交易。这种依赖性与 Bitcoin 的去中心化、保密性和金融主权等基本原则背道而驰。



BTCPay Server 是解决这一问题的开源解决方案。这种自托管支付处理器将您自己的 Bitcoin 节点变成了专业的基础设施，没有中间商，没有额外的处理费用，也不影响隐私。BTCPay Server 自 2017 年起由全球贡献者社区开发，它允许您将 Bitcoin 和闪电支付直接接收到自己的钱包中，并始终保持对资金的完全控制。



传统上，安装 BTCPay 服务器需要高级技术技能：Linux 服务器配置、掌握 Docker、SSL 证书管理和网络安全。Umbrel 通过与 Bitcoin 和 Lightning 节点直接集成的一键式安装彻底改变了这种方法。这种简化使以前只有经验丰富的技术人员才能做到的事情变得人人都能做到。



**重要提示**：Umbrel 上的 BTCPay 服务器默认仅在本地网络运行。您可以创建发票、接受闪电支付和 Bitcoin 支付，并通过连接到家庭网络的任何设备（电脑、智能手机、平板电脑）管理您的账目。这种配置非常适合当面服务计费、管理面对面支付或从本地网络使用 BTCPay 服务器。另一方面，如果要将 BTCPay 服务器集成到互联网上可公开访问的在线商店中，则需要额外的公开曝光配置（我们将在教程的最后介绍这个问题）。



本教程将指导您在 Umbrel 上完整安装 BTCPay Server、配置 Bitcoin wallet 和 Lightning 节点、创建和支付发票以及管理会计报告。您将了解如何在本地网络上高效使用 BTCPay 服务器，如果您想将其与电子商务网站集成，我们还将介绍公开展示的解决方案。



## 先决条件



要学习本教程，您需要正确安装和配置 Umbrel。如果尚未安装，请参阅我们的 Umbrel 安装教程。



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

您的 Bitcoin 核心节点必须与区块链完全同步（在 Umbrel 的 Bitcoin 应用程序中为 100% 同步）。初始同步通常需要 3 天到 2 周时间，具体取决于您的硬件和互联网连接。



要接受即时闪电支付，你还需要在 Umbrel 上安装 LND (Lightning Network Daemon)。如果你想启用这项功能，请参阅我们关于在 Umbrel 上安装和配置 LND 的教程。



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

为 BTCPay 服务器、其数据库和 "闪电 "数据预留至少 50 GB 的可用磁盘空间。强烈建议通过以太网电缆进行稳定的互联网连接，以避免断线。



## 在 Umbrel 上安装 BTCPay 服务器



从 Umbrel 界面 (`umbrel.local`)，访问 App Store 并在 Bitcoin 类别中搜索 "BTCPay Server"。



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



点击安装。Umbrel 会自动检查 Bitcoin Core 和 LND 是否已安装，然后开始部署（2-5 分钟）。



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



安装完成后，打开应用程序。您需要创建一个管理员账户，并提供强大的凭据。



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



账户创建完成后，BTCPay 服务器会立即提示您开设第一家店铺。选择一个企业名称，并选择一种参考货币（欧元、美元或 BTC）。



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## 访问本地网络上的 BTCPay 服务器



您可以通过本地网络（WiFi或以太网）上的任何设备访问BTCPay服务器。从您的浏览器访问 .NET Framework 3.0：



```url
http://umbrel.local
```



或直接发送至 ：



```url
http://umbrel.local:3003
```



**使用 Tailscale 进行远程访问**：要从世界任何地方访问 BTCPay 服务器，请使用 Tailscale。这种安全的 VPN 可让您像在本地网络一样连接到 Umbrel。请参阅我们在 Umbrel 上专门介绍 Tailscale 的教程。



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## 配置您的 Bitcoin 组合



要接受付款，您需要配置 Bitcoin wallet。BTCPay 服务器会在仪表板中显示配置选项。



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



要配置 wallet Bitcoin，请转至 "钱包">"Bitcoin"。



您有两种选择：直接在 BTCPay 中创建新的投资组合，或导入现有投资组合。对于导入，有几种方法可供选择：




- 连接硬件 wallet**（推荐）：通过 Vault 应用程序导入公钥
- 导入 wallet 文件**（推荐）：从您的作品集上传导出文件
- 输入扩展公钥**：手动输入 XPub/YPub/ZPub
- 扫描 wallet QR 代码** ：从 BlueWallet、Cobo Vault、Passport 或 Specter DIY 扫描二维码
- 输入 wallet seed**（不推荐） ：输入 12 或 24 个字符的恢复短语



![Options de création de portefeuille](assets/fr/06.webp)



在本教程中，我们将创建一个新的 Hot wallet：因此，私钥将存储在我们的 Umbrel 服务器上。在这种情况下，我们强烈建议您定期将资金转移到冷冻 wallet 上，以避免在服务器上存储大量资金。



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



配置完成后，BTCPay 服务器会确认您的 wallet 已准备好接受 on-chain 付款。



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## 激活 Lightning Network



要接受即时闪电支付，请进入钱包 > 闪电。然后，由于您的 LND 节点已在 Umbrel 上就位，只需点击 "保存 "按钮，即可验证您的 BTCPay 服务器与闪电节点之间的连接。



![Configuration du nœud Lightning](assets/fr/09.webp)



## 创建和支付发票



在 BTCPay 服务器界面，导航至发票 > 创建 Invoice。输入金额，添加可选描述，然后单击创建。



![Création d'une nouvelle facture](assets/fr/10.webp)



然后，您可以点击 "结账 "按钮来显示发票。然后，BTCPay 会生成一张带有统一二维码 (BIP21) 的发票，其中包含 Bitcoin 地址和闪电发票。



![Détails de la facture générée](assets/fr/11.webp)



客户可以使用任何兼容的 wallet 扫描 QR 码。



![Page de paiement avec QR code](assets/fr/12.webp)



一旦付款，发票在几秒钟内就会在 Lightning 系统中 "结算"。



![Confirmation de paiement réussi](assets/fr/13.webp)



## 付款管理和跟踪



在 "报告 "部分的 "发票 "选项卡中，您可以找到发票的完整历史记录，包括日期、金额、状态和付款方式。如有需要，您可以将其导出。



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## 商店配置



BTCPay 服务器允许您管理具有不同参数的多个商店。每个商店代表一个独立的业务实体：电子商务商店、实体销售点或服务计费。



在商店设置中，您可以找到几个重要部分：



![Paramètres du magasin](assets/fr/15.webp)





- 常规设置**：商店名称、参考货币（BTC、EUR、USD）、发票到期时间（默认 15 分钟）、所需区块链确认次数
- 汇率**：汇率来源和法币/Bitcoin 转换的配置
- 结账外观**：自定义结账页面的外观（徽标、颜色、个性化信息）
- 电子邮件设置**：配置收到付款的电子邮件通知
- 访问令牌**：管理用于电子商务集成（WooCommerce、Shopify 等）的 API 令牌
- 用户**：管理用户访问商店的不同级别权限（所有者、访客）
- 网络钩子**：网络钩子配置，以便与您的会计或企业资源规划系统实时同步



BTCPay 服务器还提供插件部分，可通过电子商务集成、销售点系统和其他工具扩展功能。



![Gestion des plugins](assets/fr/16.webp)



## 当地使用的优势和局限性



**BTCPay 服务器相对于 Umbrel 的优势** ：




- 完全主权：独家控制私人密钥和资金，任何第三方都无法冻结或审查您的付款
- 节省大量成本：网络成本仅为 Bitcoin（Lightning 的几美分），而传统处理器的网络成本为 2-3
- 高度保密：无需注册、身份验证或与第三方公司共享数据
- 开放源码架构通过庞大的开发者社区保证了透明度、可审计性和可持续性
- 可通过 Umbrel 轻松安装，无需高级技术技能



**重要限制** ：




- 仅限本地网络**：Umbrel 上的 BTCPay 服务器只能通过您的家庭网络访问。非常适合面对面计费、自由职业者服务或小型实体企业，但不适合公开访问的在线商店。
- 全面技术责任：节点维护、定期备份、连接监控
- 闪电式流动性管理：开辟和管理有足够进货能力的渠道
- 支持仅限于社区文档和论坛，需要比商业客户服务部门更多的自主权



这种本地网络限制是将 BTCPay 服务器集成到电子商务商店的主要障碍，因为客户需要能够从互联网上的任何地方访问支付页面。



## 最佳做法和安全



激活 Umbrel 自动备份，并在外部介质（U 盘、硬盘、加密云）上存储一份副本。将 Bitcoin 种子（恢复短语）保存在安全、物理独立的地方。备份 LND 的 channel.backup 文件，用于闪电恢复。



定期监控 Bitcoin Core 同步、闪电通道和 BTCPay 服务器响应。每周进行一次简单测试：generate 并支付几 Satoshis 的账单。及时更新 Umbrel（安全补丁、增强功能）。在重大更新前做好备份。对于专业用途，考虑使用外部监控（UptimeRobot）和电子邮件/SMS 警报。



## 为网店公开 BTCPay 服务器



要将BTCPay服务器整合到基于网络的电子商务商店（WooCommerce、Shopify等）中，您的客户需要能够从任何地方访问支付页面，而不仅仅是您的本地网络。



**解决方案nginx代理管理器**



您可以使用 Nginx Proxy Manager（可在 Umbrel 应用商店下载）公开 BTCPay 服务器。此解决方案需要.NET Framework 3.0或更高版本：




- 域名（经典域名或通过 DuckDNS、No-IP、Afraid.org 获取的免费域名）
- 在路由器上配置端口转发（端口 80 和 443
- 安装自动管理 SSL 证书的 Nginx 代理管理器



这种配置会将服务器暴露在互联网上，因此需要格外警惕（强密码、2FA、定期更新）。我们将编写专门的教程，详细介绍这一完整程序。



## 结论



Umbrel 上的 BTCPay 服务器将 Bitcoin 节点的强大功能与 Umbrel 的简易性相结合，创建了一个可供所有人使用的自托管专业支付基础设施。这种金融主权伴随着维护责任，但与以下好处相比，Umbrel 大大简化了操作负担：免除手续费、保护您的隐私、抵制审查和完全控制您的资金。



本地网络的使用已经涵盖了广泛的应用：自由职业者服务计费、当面支付、小型实体店，或者只是在受控环境中学习和实验 Bitcoin 和 Lightning。对于需要公开的电子商务需求，Nginx 代理管理器解决方案已经存在，但需要额外的技术配置，我们将在专门的教程中详细介绍。



无论您是在经营一家企业、一个新兴项目，还是只是在做实验，Umbrel 上的 BTCPay 服务器都能为您提供完全的财务自主权。这条道路从您的第一家商店、第一张发票、第一笔直接进入您的主权基础设施的付款开始。



## 资源



### 正式文件




- [BTCPay服务器官方网站](https://btcpayserver.org)
- [完整的 BTCPay 服务器文档](https://docs.btcpayserver.org)
- [GitHub BTCPay 服务器](https://github.com/btcpayserver/btcpayserver)
- [Tailscale文档](https://tailscale.com/kb)


### 社区和支持




- [论坛 BTCPay 服务器](https://chat.btcpayserver.org)
- [论坛雨伞](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)