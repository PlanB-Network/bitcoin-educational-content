---
name: Bisq 2
description: 使用 Bisq 2 和 P2P 比特币兑换完整指南
---
![cover](assets/cover.webp)

## 导言

无 KYC 的点对点（P2P）交易所对于保护用户的保密性和金融自主权至关重要。它们实现了个人之间的直接交易，无需身份验证，这对于那些重视隐私的人来说至关重要。如需更深入地了解理论概念，请参阅 BTC204 课程：

https://planb.network/courses/btc204
### 什么是 Bisq 2？

Bisq 2 是广受欢迎的去中心化 Bisq 交易所的新版本，于 2024 年推出。与其前身不同，Bisq 2 的开发支持多种交易所协议，为用户提供了更大的灵活性。

**主要新功能：**


- 支持多种隐私网络（Tor、I2P）
- 多重身份，提高保密性
- 用于交易机器人的 REST API
- 支持多种投资组合类型
- BSQ 强制存款的角色系统

本指南专门介绍目前唯一可用的协议 "Bisq Easy"。Bisq Easy 是专为比特币新用户设计的。该协议使用户能够在去中心化的点对点平台上以法定货币买卖比特币。交易上限为 600 美元（最低 6 美元），交易所的安全性取决于比特币卖家的信誉。Bisq Easy 没有交易费用或保证金要求。对于低于 600 美元（或等值）的现金交易，Bisq Easy 预计将取代 Bisq 1。

**主要功能：**


- 跨平台桌面应用程序
- 多种交换协议可供选择
- 分散式 P2P 网络
- 注重保密性（无 KYC、使用 Tor）
- 非托管（您保留对资金的控制权）
- 开放源代码（AGPL）

### 与 Bisq 1 的区别

**针对买家：**


- 无需押金
- 无交易费用
- 无采矿费
- 基于供应商信誉的安全性
- 较低的交易限额（相当于 600 美元）

**针对卖家：**


- 无需押金
- 建立声誉
- 燃烧 BSQ 或创建 BSQ 债券的可能性
- 潜在的较高销售溢价（高于市场价 10-15）

**重要说明：** 一旦 Bisq 2 中实施了 Bisq Multisig 协议，旧版本的 Bisq 即可逐步淘汰。不过，Bisq 1 将继续用作 Bisq CAD 和 BSQ-BTC 交易所的管理工具。

### 交流过程


- 要约创建者确定交换条款
- 一旦交易者就条款（付款方式和价格）达成一致，交换就开始了
- 卖方将其银行信息发送给买方，买方将其比特币地址发送给卖方
- 买方以现金支付并通知卖方
- 收到付款后，卖方将比特币发送到买方地址
- 当买方收到比特币时，交换完成

### 重要规则


- 在交换付款信息之前，可无正当理由取消交换
- 交换细节后，不履行义务可能导致流放
- 对于银行转账，**切勿在付款理由中使用 "Bisq "或 "比特币 "**（这可能导致资金被冻结，甚至导致收款人或付款人的银行账户被冻结）。
- 交易者必须每天至少登录一次，以跟踪流程
- 如果出现问题，贸易商可以寻求调解员的服务

## 安装和配置

### 1.下载并验证 Bisq 2

![Téléchargement de Bisq 2](assets/fr/01.webp)


- 转到 [bisq.network](https://bisq.network/downloads/)
- 下载与您的操作系统相对应的 Bisq 2 版本（向下滚动页面）
- 验证下载文件的真实性（强烈建议）。有关签名验证的详细指南，请参阅以下教程：

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
### 2.根据系统进行安装

请按照适合您操作系统的安装步骤进行安装。如果在安装过程中遇到任何困难，可以查阅 [Bisq 官方维基] (https://bisq.wiki/Downloading_and_installing) 上的详细指南。

### 3.首次启动


- 启动 Bisq 2 并接受使用条款

![Conditions d'utilisation](assets/fr/01.webp)


- 选择名称和头像，创建新的个人资料

![Création du profil](assets/fr/02.webp)


- 然后，您将进入应用程序的主控制面板，在那里您可以启动 Bisq Easy 购买或出售您的第一枚比特币

![Page d'accueil de Bisq 2](assets/fr/03.webp)

### 4.设置付款方式


- 从主菜单进入付款账户部分

![Liste des comptes de paiement](assets/fr/04.webp)


- 填写所需信息，添加新付款方式

![Création d'un nouveau compte de paiement](assets/fr/05.webp)

预设付款方式是可选项，但建议您在交易时进行预设，以节省时间。您也可以联系您的交易所合作伙伴，在交易过程中直接配置付款方式。

### 5.账户安全

**数据备份：**

与 Bisq 1 不同，Bisq 2 目前没有集成比特币钱包：因此，交易是通过您自己的外部钱包进行的。不过，我们建议您定期备份 Bisq 2 数据文件夹。要找到您的数据文件夹，请查阅 [Bisq 官方维基](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory)。

**身份管理：**

Bisq 2 可让您创建多个身份。每个身份可用于不同类型的交易。您的身份信息存储在数据文件夹中。

## 买卖比特币

### 如何购买比特币

**方案 1：利用现有优惠**


- 在主屏幕上选择 "Bisq Easy"、"入门 "选项卡，然后点击 "开始交易向导"。

![Lancer trade wizard](assets/fr/06.webp)


- 选择 "购买比特币 "并选择货币

![Sélection achat Bitcoin](assets/fr/07.webp)

![Choix de la devise](assets/fr/08.webp)


- 设置您喜欢的付款方式（SEPA、Revolut 等）

![Configuration méthodes de paiement](assets/fr/09.webp)


- 此时，要么您已经有了与之前的标准相对应的报价列表，要么您需要转到 "报价簿"。

![Liste des offres](assets/fr/10.webp)


- 在第二种情况下，您可以使用界面右上方的按钮显示和筛选报价

![Filtres des offres](assets/fr/11.webp)


- 选择报价后，您只需选择付款方式，然后验证交易摘要

![Choix modalités de paiement](assets/fr/12.webp)

![Configuration du trade](assets/fr/13.webp)

![Récapitulatif du trade](assets/fr/14.webp)

**方案 2：创建自己的报价**


- 选择 "Bisq Easy"，然后选择 "Offerbook"。
- 选择交易货币对（如 BTC/EUR）
- 点击 "创建报价
- 按照报价创建向导进行操作：定义金额（固定金额或范围）

![Configuration du montant](assets/fr/20.webp)


- 选择可接受的付款方式

![Sélection méthodes de paiement](assets/fr/21.webp)


  - 检查摘要并发布报价

![Récapitulatif et publication](assets/fr/22.webp)

一旦启动交换 ：


- 向卖家发送您的比特币地址或闪电发票

![Envoi adresse Bitcoin](assets/fr/15.webp)


- 接收卖方的银行信息

![Réception coordonnées bancaires](assets/fr/16.webp)

![Détails coordonnées bancaires](assets/fr/17.webp)


- 付款（不要提及 "Bisq "或 "Bitcoin"）。
- 通知卖方您的付款

![Notification paiement](assets/fr/18.webp)


- 等待比特币到账

![Attente réception](assets/fr/19.webp)

### 如何出售比特币？

Bisq 2 上的出售流程与购买流程类似，主要步骤相同，但顺序相反。您既可以创建自己的销售要约，也可以对现有的购买要约做出回应。以下是该流程中各种选项和阶段的细分：

**方案 1：创建销售要约**


- 选择 "Bisq Easy"，然后选择 "Offerbook"。
- 点击 "创建报价"，然后选择 "出售比特币"。
- 配置您的报价 ：
 - 选择货币（欧元、美元等）
 - 选择可接受的付款方式
 - 设置金额（相当于 6 至 600 美元之间）
 - 设定价格（固定价格或市场价格的百分比）
- 检查详细信息并发布报价

**备选方案 2：接受现有提议**


- 在 "Offerbook "选项卡中浏览报价
- 按货币和付款方式筛选
- 选择适合您的报价
- 查看详情并接受报价

**销售过程：**

一旦启动交换 ：


   - 将您的银行信息发送给买方
   - 等待买家的比特币地址
   - 检查地址是否有效

付款通知后 ：


   - 检查您的账户是否已收到付款
   - 确认金额和详细信息一致
   - 向提供的地址发送比特币
   - 标记交易完成

定稿 ：


   - 等待买家确认
   - 留下交易反馈
   - 为未来的销售建立声誉

**重要提示：** 作为卖家，您需要特别警惕扣款风险。优先选择安全的付款方式，并在发送比特币之前始终检查是否已收到付款。

## 良好做法与安全

### 安全提示

**针对买家：**


- 从少量开始
- 检查卖家的信誉（至少 30,000 分）
- 仅使用建议的付款方式
- 付款前检查卖家是否处于活动状态
- 只能使用交换聊天中提供的银行详细信息
- 切勿在 Bisq 2 平台之外进行通信
- 保留付款凭证
- 切勿发送敏感信息

**针对卖家：**


- 小心使用新账户
- 避免使用对退款敏感的支付方式（PayPal、Venmo）
- 检查账户信息是否与买方一致
- 仅限聊天交流 Bisq 2
- 在有疑问时进行调解

### 建立声誉（针对销售人员）

为了提高您作为卖家在 Bisq 上的声誉，请定期进行交易并与买家保持专业沟通。快速回应买家的要求，以确保获得良好的体验。您还可以创建 BSQ 债券，以显示您对平台的承诺。这些行为将建立信任并吸引更多买家。

### 争议解决


- 通过聊天联系您的同行
- 如有必要，提出争议
- 提供所有要求的证明
- 遵循调解员的指示

### 隐私政策 ：


- 无需注册或集中身份验证
- 所有连接都通过 Tor 网络进行（很快也将通过 I2P 网络进行）
- 无中央服务器存储数据
- 交易详情只有相关方可读取

### 防止新闻检查 ：


- 完全分布式 P2P 网络
- 利用 Tor 网络（以及即将推出的 I2P）抵制审查制度
- 由 DAO 管理的开放源码项目，没有中央法律实体

## 优缺点

### Bisq 2 的优点


- 最高保密性**：无 KYC，使用 Tor
- 分散化**：无中央服务器
- 安全**：开放源代码、非托管代码
- 直观的界面**：比 Bisq 1 更简单
- 灵活性**：多种交换协议

### Bisq 2 的缺点


- 流动性有限** （目前） ：
 - 处于启动阶段的新规程
 - 少量销售优惠
 - 寻找买家的等待时间可能很长
- 交易限额**：每次交易最多 600 美元（使用 Bisq easy）
- 仅限台式机**：无移动应用程序

## 未来议定书

虽然 Bisq Easy 是目前唯一可用的协议，但 Bisq 2 还在开发其他几种协议：


- Bisq Lightning**：基于托管系统的交换协议，使用闪电网络上的多方计算加密技术。
- Bisq MuSig**：将主协议从 Bisq 1 迁移到 Bisq 2，使用 2 对 2 多重身份和保证金。
- BSQ Swaps**：BSQ 和 BTC 之间的即时原子交换。
- Liquid Swaps**：通过原子互换在 Liquid 网络（USDT、BTC-L）上交换资产。
- 莫奈罗交换**：比特币与 Monero 之间的原子交换。
- Liquid MuSig**：使用 L-BTC 的 multisig 协议版本，成本更低，保密性更强。
- 海底交换**：闪电网络上的比特币与链上比特币之间的交换。
- 稳定币交换**：比特币与美元稳定币之间的原子交换。
- Multisig 期权**：创建 P2P 认沽和认购期权，并在链上多位数交易中使用 BTC Blocking。
- Multisig 开放式合约**：可使用 2 对 3 多头配对套利系统创建自定义条件合约。

这些协议目前正在开发中，并将逐步集成到 Bisq 2 中，从而根据用户的具体需求为其提供更大的灵活性。

## 实用资源


- 官方网站：[bisq.network](https://bisq.network)
- 文档：[Bisq Wiki](https://bisq.wiki)
- 支持：[Forum Bisq](https://bisq.community)
- 源代码 ：[GitHub](https://github.com/bisq-network)