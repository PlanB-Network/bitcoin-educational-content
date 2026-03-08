---
name: Sats.mobi
description: 一款可通过 Telegram 访问的托管钱包
---

![cover](assets/cover.webp)

_本教程由_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_) 编写.

## Sats.Mobi

SatsMobi 是一款基于 Telegram 的钱包，它具备闪电网络（托管）钱包的所有功能，并添加了一系列非常有趣的功能。它源自现已停止维护的 LightningTipBot 的一个分支，继承了其所有功能，并添加了更多现代功能，使其更加现代化。与 LNTipBot 一样，Sats.Mobi 也秉持开源理念。您可以从此[仓库](https://github.com/massmux/SatsMobiBot)克隆该钱包，并对其进行独立配置和管理。

如果您只想简单地使用它，只需在 Telegram 上发起聊天即可发现它是一个机器人。

## 设置

在 Telegram 搜索栏中查找 "satsmobi"，就会出现 [机器人](@SatsMobiBot) 的链接。

**注意**：如果您不确定是否要通过 Telegram 进行搜索，请使用以下 [链接](https://t.me/SatsMobiBot) 安全访问机器人

![image](assets/it/01.webp)

您只需按下 _START_ 键即可开始操作。

![image](assets/it/02.webp)

为了探索 Wallet，可以选择左下角的 _Menu_。

![image](assets/it/03.webp)

现在选择主要命令中的 _/help_。

![image](assets/it/04.webp)

Sats.Mobi 会显示一条欢迎信息，列出所有主要功能。启动时，机器人还会创建一个闪电网络地址，该地址与选定的 Telegram 用户名关联（默认情况下是唯一的）。您可以使用此钱包发送和接收聪（比特币）的命令，以及其他一些功能，我们稍后会介绍。不妨也看看 _/advanced_ 选单。

![image](assets/it/05.webp)

值得注意的是，Sats.Mobi 还创建了一个匿名闪电网络地址，用于保护隐私。机器人通过命令运行：只需点击相应的单词，或在消息栏中输入 “/”，然后输入要执行的命令即可。即使钱包刚刚创建，也可以选择例如 _/transactions_ 命令。

![image](assets/it/06.webp)

此命令会显示最新交易列表，在本例中为零。

![image](assets/it/07.webp)

## 接收聪（比特币）

创建发票并接收聪的命令是 _/invoice_。Sats.Mobi 仅以聪（比特币的最小单位）进行交易；因此，为了创建发票，需要在消息栏中输入聪的金额，然后将其发送到与机器人的聊天窗口中。

![image](assets/it/08.webp)

在下面的例子中，选择接收 210 聪。

![cover](assets/it/09.webp)

等待片刻后，发票就会以文本和二维码的形式出现。支付发票后，钱包会显示余额。如果由于某种原因总金额没有更新，请写入 _/balance_ 并按 "enter" 键。

![image](assets/it/10.webp)

## 发送聪（比特币）

虽然 Sats.Mobi 是极其宝贵的资产，不应轻易放弃，但进行一些简短的测试（即几次试验性交易）并不困难。

### 支付发票

支付发票的最简单方法是复制信息字符串 `lnbc1xxxxx` 并在输入 _/pay_ 命令后将其粘贴到信息栏中。 **正确的语法**要求在命令后留一个空格。

![image](assets/it/11.webp)

钱包会发送信息要求确认。点击 _Pay_，发票即可被付款。

![image](assets/it/12.webp)

Sats.Mobi 可以依靠高效、连接良好的闪电节点，很少出现支付失败的情况，因为它总能找到正确的路由。

### 使用手机轻松支付

在 Telegram 上浏览时，Sats.Mobi 也支持移动端。最便捷的移动支付方式是扫描二维码，但由于 Sats.Mobi 并非独立应用，而是社交网络的一部分，因此其设计本身并不支持此功能。为此，Sats.Mobi 致力于尽可能提升移动端的使用体验：它能够解码图像，例如拍摄您要支付的账单二维码照片。

例如，假设您想支付 50 聪的发票。

![image](assets/it/20.webp)

当我们看到这些信息时，就可以拍摄相关二维码的照片。

![image](assets/it/21.webp)

然后，我们打开手机上的 Telegram，在与 Sats.Mobi 的聊天中，附上刚刚拍摄的二维码照片。

![cover](assets/it/22.webp)

选定后，我们将其发送给机器人：

![image](assets/it/23.webp)

Sats.Mobi 会对照片进行解码，并**立即显示付款请求**和正确的描述。聊天会要求确认，您必须按_/pay_键才能继续。

![image](assets/it/24.webp)

请稍等片刻，以便处理付款。

![image](assets/it/25.webp)

50 sats 的发票已支付，无需使用摄像头及其内置扫描功能即可完成支付。

### Sats.Mobi 在 Telegram 群组中的应用

![image](assets/it/27.webp)

Sats.Mobi 为 Telegram 带来了让 LNTipBot 声名鹊起的功能，其中之一就是让群组成员获得有趣的互动体验。

群主可以邀请机器人加入群聊，然后提名 Sats.Mobi 为管理员。从那时起，乐趣就开始了，因为成员可以开始奖励其他用户为群组做出的贡献。

- _/tip_ 通过回复消息来添加提示；
- _/send_ 发送资金，指定闪电地址或 Telegram 用户名为接收者；
- _/faucet_（位于 _/advanced_ 选单中）：创建一系列小费，群组中最快的成员可以通过点击 _/collect_ 来领取。
- _/tipjar_（位于 _/advanced_ 选单中）创建了另一种可发送给组内用户的分发类型。

每个命令都有其语法，主命令选单中对此有详细说明。

如果我们不是群组的创建者呢？没问题：只需请创建者邀请 Sats.Mobi 加入，并将其添加为群组管理员，一切就绪！

## 销售点 (POS)

Sats.Mobi 首次启动时，机器人还会为用户创建另一个功能：**POS 机**。用户可以使用命令 `/pos` 或点击控制台右下角的相关按钮来激活该“设备”。实际上，这个POS系统是一个网页应用，它会在 Telegram 聊天窗口弹出。

![image](assets/it/14.webp)

界面左上角会显示用户的个人 Telegram 用户名，使用方法与其他 POS 系统一样简单：只需在键盘上输入金额即可。假设我们现在要收取 21 欧分的服务费。由于 Sats.Mobi 只支持聪单位（satoshi），所以很难心算换算。而 POS 系统会以欧元作为结算单位，同时显示等值的聪数。

![image](assets/it/15.webp)

点击 _/OK_ 会显示发票，可以通过二维码向客户展示，也可以通过即时消息以字符串的形式发送，这样就可以付款了。

![image](assets/it/16.webp)

![image](assets/it/17.webp)

当然，POS 系统也可以在手机上使用，访问方式与之前相同。

![image](assets/it/18.webp)

它在手机屏幕上的显示效果也很好：

![image](assets/it/19.webp)

## 附加功能

Sats.Mobi 钱包还提供其他功能，进一步完善了其功能。正如我们所见，它扩展了钱包的概念，使其超越了收付款的范畴：

- _/nostr_：将钱包连接到自己的 Nostr 用户，以接收 Zaps；
- _/cashback_：显示可向商家出示的代码，以获得购物返现；
- _/buy_：在机器人中启动一个引导程序，可以用欧元购买聪；
- _/activatecard_：申请激活 NFC 借记卡，该卡可通过 Sats.Mobi 钱包充值，并可激活通知；
- _/link_：为您自己的 Zeus 或 Blue Wallet 创建链接，它们可用作此钱包的遥控器。

## 结论

Sats.Mobi 是一款使用起来令人愉悦且充满乐趣的钱包，它让人想起使用 LNTipBot 的体验，并提供了 LNBits 的更高级功能。但是，请务必记住，**它是一个托管服务**。因此，它应该只用于存放少量比特币，而不是您存放闪电网络资金的主要钱包。此外，它还有 500,000 聪的固有容量限制，建议不要超过此限制。

如果您正在寻找非托管的闪电网络钱包，强烈建议您考虑其他产品。

---
### 文档

- [Github](https://github.com/massmux/SatsMobiBot)
- [视频](https://www.youtube.com/results?search_query=Sats.mobi) 演示
