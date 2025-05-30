---
name: Sats.mobi

description: 可通过电报访问的托管 Wallet
---

![cover](assets/cover.webp)


_本教程由_ [Bitcoin 校园](https://linktr.ee/bitcoincampus_) 编写


## Sats.Mobi

SatsMobi 是在 Telegram 上运行的 Wallet，具有 Lightning Network（托管）Wallet 的所有功能，以及一系列非常有趣的特性。它源于现已停产的 LightningTipBot 的 Fork，在继承其所有功能的同时增加了更多新功能，从而使其更加现代化。与 LNTipBot 一样，Sats.Mobi 也奉行开源理念。Wallet 可以从这个 [资源库](https://github.com/massmux/SatsMobiBot)中克隆，进行独立配置和管理。


如果你想简单地使用它，在 Telegram 上开始聊天就会显示它是一个机器人。


## 设置

在 Telegram 搜索栏中查找 "satsmobi"，就会出现 [机器人]（@SatsMobiBot）的链接。


**注意**：如果您不确定是否要通过 Telegram 进行搜索，请使用以下 [链接](https://t.me/SatsMobiBot) 安全访问机器人


![image](assets/it/01.webp)


您只需按下 _START_ 键即可开始操作。


![image](assets/it/02.webp)


要探索 Wallet，可以选择左下角的_菜单。


![image](assets/it/03.webp)


现在选择主要命令中的 _/help_。


![image](assets/it/04.webp)


Sats.Mobi 通过显示一条消息欢迎我们，并列出了所有主要功能。启动时，机器人还会创建一个 LN Address，与 Telegram 上选择的句柄相连（默认情况下是唯一的）。通过这个 Wallet 发送和接收 Sats 的命令以及其他功能我们稍后会看到。我们还可以看看_/高级_菜单


![image](assets/it/05.webp)


值得注意的是，Sats.Mobi 还创建了一个匿名的 LN Address，用于获取隐私。该机器人使用命令工作：只需点击相应的单词，或在信息栏中输入斜线"/"，然后输入您要执行的命令。即使 Wallet 刚刚创建，也可以选择_/transactions_等命令。


![image](assets/it/06.webp)


该命令显示最新交易列表，在本例中等于零。


![image](assets/it/07.webp)


## 接收 Sats

创建 Invoice 和接收 Sats 的命令是 _/invoice_。Sats.Mobi 只在 Satoshi 中运行，Satoshi 是 Bitcoin 的最小单位；因此，要创建 Invoice，必须在消息栏中用 Sats 写入金额，然后在与机器人的聊天中发送。

![image](assets/it/08.webp)


在下面的例子中，选择接收 210 Sats。


![cover](assets/it/09.webp)


等待片刻后，Invoice 就会以文本和 QR 码的形式出现。支付 Invoice 后，Wallet 会显示余额。如果由于某种原因总金额没有更新，请写入 _/balance_ 并按 "enter "键。


![image](assets/it/10.webp)


## 发送 Sats


虽然 Sats.Mobi 是极其宝贵的资产，不应轻易放弃，但进行一些简短的测试（即几次试验性交易）并不困难。


### 支付 Invoice


支付 Invoice 的最简单方法是复制信息字符串 `lnbc1xxxxx` 并在输入 _/pay_ 命令后将其粘贴到信息栏中。 **正确的语法**要求在命令后留一个空格。


![image](assets/it/11.webp)


Wallet 会发送信息要求确认。点击_Pay_，Invoice 即可付款。


![image](assets/it/12.webp)


Sats.Mobi 可以依靠高效、连接良好的 Lightning 节点，很少出现支付失败的情况，因为它总能找到正确的路由。


### 用手机轻松支付


在 Telegram 上浏览，Sats.Mobi 也可在手机上使用。使用手机支付最方便的功能是扫描二维码，但 Wallet.Mobi 在设计上缺少这一功能，因为它不是一个独立的应用程序，而是包含在一个社交网络中。因此，Sats.Mobi 的程序设计尽可能方便移动体验：它确实可以解码图像，比如您要支付的 Invoice QR 码的照片。


例如，假设您想支付 50 Sats 的 Invoice。


![image](assets/it/20.webp)


当我们看到这些信息时，就可以拍摄相关二维码的照片。


![image](assets/it/21.webp)


然后，我们打开手机上的 Telegram，在与 Sats.Mobi 的聊天中，附上刚刚拍摄的二维码照片


![cover](assets/it/22.webp)


选定后，我们将其发送给机器人：


![image](assets/it/23.webp)

Sats.Mobi 会对照片进行解码，并**立即显示付款请求**和正确的描述。聊天会要求确认，您必须按_/pay_键才能继续。

![image](assets/it/24.webp)


请稍等片刻，以便处理付款。


![image](assets/it/25.webp)


Invoice 换 50 Sats，这一结果是在不使用照相机及其集成扫描功能的情况下取得的。


### Telegram 群组中的 Sats.Mobi


![image](assets/it/27.webp)


Sats.Mobi 为 Telegram 带来了让 LNTipBot 声名鹊起的功能，其中之一就是让群组成员获得有趣的互动体验。

群主可以邀请机器人加入群聊，然后提名 Sats.Mobi 为管理员。从那时起，乐趣就开始了，因为成员可以开始奖励其他用户为群组做出的贡献。


- _/tip_ 通过回复消息来添加提示；
- _/send_ 发送资金，指定 LN Address 或 Telegram 句柄为收件人；
- _/水龙头_（在_/高级_菜单中）可以创建一系列提示，小组中速度最快的成员可以通过点击_/收集_来收集这些提示；
- _/tipjar_（在 _/Advanced_（高级）菜单中）创建了另一种可发送给组内用户的分发类型。


每个命令都有自己的语法，在主命令菜单中都有解释。


如果我们不是群组的所有者？没问题：只需要求创始人邀请 Sats.Mobi，将其添加为群组管理员，就可以了！


## 销售点 (POS)


首次启动 Sats.Mobi 时，机器人还为用户创建了另一项功能： **POS**。用户可通过_/pos_命令或点击右下角控制台的相关按钮激活 "设备"。事实上，POS 是一个网络应用程序，会在 Telegram 聊天工具上以弹出式窗口打开


![image](assets/it/14.webp)


Interface 会在左上角显示用户的 Telegram 账号，使用方法与所有 POS 一样简单：在键盘上输入金额。假设我们现在要为一项服务收取 21 欧分。由于 Sats.Mobi 只能本地管理 Sats，要在头脑中进行转换并不容易。相反，POS 会显示欧元作为记账单位，同时显示 Satoshi 的等值。


![image](assets/it/15.webp)

点击 _/OK_ 会显示 Invoice，可以通过二维码向客户展示，也可以通过即时消息以字符串的形式发送，这样就可以付款了。

![image](assets/it/16.webp)

![image](assets/it/17.webp)


当然，POS 也可以在手机上使用，访问方式与前述相同。


![image](assets/it/18.webp)


在手机屏幕上也能很好地显示：


![image](assets/it/19.webp)


## 附加功能


Sats.Mobi Wallet 还具有其他功能，如我们所见，它将 Wallet 的概念扩展到了收款和付款操作之外：


- _/nostr_：将 Wallet 连接到自己的 Nostr 用户，以接收 Zaps；
- _/cashback_：显示可向商家出示的代码，以获得购物返现；
- _/buy_：在机器人中启动一个引导程序，可以用欧元购买 Sats；
- _/activatecard_：申请激活 NFC 借记卡，该卡可通过 Sats.Mobi Wallet 充值，并可激活通知；
- _/link_：为您自己的 Zeus 或 Blue Wallet 创建链接，它们可用作此 Wallet 的遥控器。


## 结论

Sats.Mobi 是一款使用起来愉快而有趣的 Wallet，它能让您重温使用 LNTipBot 的体验，使用 LNBits 的更高级功能。不过，重要的是要记住，**它是一种托管服务**。因此，它只能用来存放极少量的 Sats，而不是存放 Lightning Network 资金的主要 Wallet。它还有一个内在容量限制，相当于 500 000 个 Sats，建议不要超过这个限制。


如果您正在寻找非保管型 Lightning Network 钱包，建议您最好去看看其他产品。


---
### 文件


- [Github](https://github.com/massmux/SatsMobiBot)
- 视频播放列表](https://www.youtube.com/results?search_query=Sats.mobi) 演示