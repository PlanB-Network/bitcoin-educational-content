---
name: LNP2PBot
description: LNP2PBot 和 P2P 比特币交易完整指南
---
![cover](assets/cover.webp)

## 导言

无 KYC 的点对点（P2P）交易所对于保护用户的保密性和金融自主权至关重要。它们实现了个人之间的直接交易，无需身份验证，这对于重视隐私的人来说至关重要。如需更深入地了解理论概念，请参阅 BTC204 课程：

https://planb.network/courses/btc204
点对点（P2P）买卖比特币是获取或处置比特币最隐秘的方法之一。LNP2PBot 是一个开源的 Telegram 机器人，可促进闪电网络上的点对点交换，实现快速、低成本、无 KYC 的交易。

### 为什么使用 Lnp2pbot？


- 无需 KYC
- 闪电网络上的快速交易
- 低成本
- 通过 Telegram（一款在世界任何地方都能访问的流行信息应用程序）实现简单的界面
- 综合声誉系统
- 自动托管，确保交易安全
- 支持多种货币
- 活跃且不断发展的社区

### 先决条件

要使用 Lnp2pbot，您需要 ：

1.闪电网络钱包（推荐使用 Breez、Phoenix 或 Blixt）

2.已安装 Telegram 应用程序 (https://telegram.org/)

3.具有已定义用户名的 Telegram 账户

## 安装和配置

### 1.配置闪电钱包

首先安装一个兼容的闪电钱包。以下是我们的详细推荐：

**推荐的投资组合**


- [Breez](https://breez.technology)**：
  - 非常适合初学者
  - 直观、现代的界面
  - 非托管（您保留对资金的控制权）
  - 与 Lnp2pbot 完美兼容
  - 适用于 iOS 和安卓系统

下面是这款钱包的教程链接：

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co)** ：
  - 简单可靠
  - 自动通道配置
  - 原生支持 BOLT11 发票
  - 非常适合日常交易
  - 适用于 iOS 和安卓系统

下面是这款钱包的教程链接：

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** ：
  - 技术性较强，但非常完整
  - 高级配置选项
  - 非常适合有经验的用户
  - 开放源代码
  - 适用于安卓系统

下面是这款钱包的教程链接：

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**关于其他投资组合的重要说明**

⚠️ **重要**：在销售 sats 之前，请确保您的投资组合支持 "持有 "发票，机器人将其用作托管系统。


- 中本聪钱包**：接收中本聪效果很好，但如果销售取消，余额更新可能会出现延迟。
- Muun**：不建议使用，因为机器人路由费限制（最高 0.2%）可能导致支付失败。
- Aqua**：可接收卫星信号，但在销售取消的情况下，余额更新可能会延迟很长时间（最长 48 小时）。

💡 **提示**：为获得最佳体验，请选择推荐的组合（Breez、Phoenix 或 Blixt）。

⚠️ **重要**：不要忘记将恢复短语保存在安全的地方。

### 2.开始使用 Lnp2pbot

1.点击此链接访问机器人：[@lnp2pBot](https://t.me/lnp2pbot)

2.Telegram 将自动打开

3.点击 "启动 "或发送"/start "命令

4.如果您还没有用户名，机器人会要求您创建一个用户名

5.机器人将引导您完成初始配置

### 3.加入社区


- 加入主频道：[@p2plightning](https://t.me/p2plightning)
- 支持：[@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## 买卖比特币

在 Lnp2pbot 上兑换比特币有两种主要方式：

1.浏览并回复市场上的现有报价

2.创建自己的购买或销售报价

在本指南中，我们将详细介绍如何使用.NET Framework 3.0：


- 从现有报价中购买比特币
- 通过创建自己的报价出售比特币

### 如何购买比特币

**1.查找并选择报价**

![Sélection d'une offre de vente](assets/fr/01.webp)

浏览 [@p2plightning](https://t.me/p2plightning)中的优惠信息，点击您感兴趣的广告下的 "购买 satoshis "按钮。

**2.验证报价和金额**

![Validation de l'offre](assets/fr/02.webp)

1.返回机器人聊天

2.确认您的报价选择

3.输入您希望购买的法定货币金额

4.机器人会要求您提供一张 "闪电 "发票，金额单位为沙托什

**3.联系卖家**

![Mise en relation](assets/fr/03.webp)

发票寄出后，机器人会让您与卖家取得联系。

**4.与卖方的沟通**

![Chat privé](assets/fr/04.webp)

点击卖家昵称，打开私人聊天频道，您可以在此交流法币支付细节。

**5.付款确认

![Confirmation du paiement](assets/fr/05.webp)

完成法币支付后，在机器人聊天中使用 `/fiatsent`命令。交易完成后，您就可以给卖家评分，交易也将结束。

### 如何出售比特币

**1.创建销售报价**

![Création d'une offre de vente](assets/fr/06.webp)

要创建销售报价，只需使用 ：

出售

然后，机器人会一步一步地指导你：

1.选择货币

2.指出要卖多少沙托希

3.就价格而言，您有两种选择：


   - 为卫星数量设定固定价格
   - 使用市场价格，可选择使用溢价（正溢价或负溢价）

💡 **提示**：溢价允许您根据市场价格调整价格。例如，溢价-1% 意味着您的售价比市场价低 1%。

**2.订单创建确认**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

创建订单后，您会看到一个确认信息，您可以选择使用 `/cancel`命令取消订单。

**3.管理销售**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- 当买家回复您的报价时，您会收到带有二维码和发票的付款通知。
- 查看买家的资料和信誉。

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- 点击买家昵称，打开私人讨论频道。
- 向买方传达法币支付详情。
- 等待买方确认法币付款。
- 检查您的账户是否已收到付款。

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- 使用 `/release`确认交易并完成订单。您将有机会给买家评分。

## 良好做法与安全

### 安全提示


- 从少量开始
- 经常检查用户的声誉
- 仅使用建议的付款方式
- 在机器人聊天中保持所有交流
- 切勿共享敏感信息

### 信誉系统


- 每个用户都有一个声誉分数
- 成功交易可增加您的分数
- 选择信誉良好的用户
- 向版主报告任何可疑行为

### 争议解决

1.出现问题时，保持冷静和专业

2.使用 `/dispute` 命令开票

3.提供所有必要的证明

4.等待主持人

## 与其他解决方案的比较

与 Peach、Bisq、HodlHodl 和 Robosat 等其他 P2P 交易所解决方案相比，Lnp2pbot 有若干优缺点：

### Lnp2pbot 的优势


- 无需 KYC** ：与某些平台不同，Lnp2pbot 不需要身份验证，从而保护了用户的机密性。
- 快速交易**：得益于闪电网络，交易几乎瞬时完成。
- 费用低** ：交易费用低于传统交易所。
- 移动可用性**：LNP2PBot 可通过 Telegram 访问，便于在移动设备上使用。
- 易于使用** ：Lnp2pbot 界面直观，即使经验不足的用户也能轻松使用。

### Lnp2pbot 的缺点


- 依赖 Telegram**：使用 Lnp2pbot 需要 Telegram 帐户，这可能不适合所有用户。
- 流动性较低**：与 Bisq 等更成熟的平台相比，流动性可能更有限。

相比之下，Bisq 等解决方案提供更高的流动性和桌面界面，但可能涉及更高的费用和更长的交易时间。同时，HodlHodl 和 Robosat 也提供免 KYC 交易，但收费结构和界面不同。

## 有用资源


- 官方网站： https://lnp2pbot.com/
- 文件：https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- 支持：[@lnp2pbotHelp](https://t.me/lnp2pbotHelp)