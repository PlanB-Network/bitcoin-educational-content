---
name: Bitcoin 购物券机器人 P2P
description: 如何使用 BitcoinVoucherBot 买卖 Bitcoin P2P
---

![image](assets/cover.webp)



我们仍然听说过 BitcoinVoucherBot，这是一个 Telegram 机器人，通过 SEPA 银行转账购买 Bitcoin，无需 [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer)。遗憾的是，自 2025 年 11 月起，集中形式的 BitcoinVoucherBot 不再提供无需 KYC 的服务。



在本指南中，我们将了解新的实现方式是如何工作的，它允许用户直接在新的 P2P（点对点）市场上买卖 Bitcoin，因此无需 KYC。为了应对日益威胁数字自由和隐私的新限制，开发人员创建了这一扩展，让用户能够通过 P2P（点对点）以高度匿名的方式买卖 Bitcoin。让我们一起来看看这种新的交换方式是如何运作的。



要使用该服务，您必须通过 Lightning Network 进行转账。因此，请确保您的 wallet 支持该协议，并允许您使用 "LNURL "或 "Lightning Address "接收和发送资金。



在支持的 wallet 型飞机中，我们可以找到





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (托管与非托管互换)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



或任何具有 "闪电 Address "并生成 Bolt11 发票的 wallet。目前不支持生成 Bolt12 发票的 wallet。更多信息请参阅 [Bolt](https://planb.academy/resources/glossary/bolt) 的定义。



在本教程中，考虑到 Wallet of Satoshi 易于直接使用，我们将使用 Wallet of Satoshi。



**注意**：Wallet of Satoshi 虽然在初学者中很受欢迎，但它是托管模式，对资金的控制有限；只能短暂使用，应立即转移到非托管模式以获得完全主权。截至 2025 年 10 月，它在全球 iOS/Android 平台上提供了稳定的自我托管模式（更新应用程序），具有自主私钥、模式切换、自定义闪电地址和 seed 12 字备份功能。不过，在整合之前，它仍是一个临时解决方案，长期管理上更倾向于 wallet 非托管成熟模式。



很好！现在我们可以开始我们的旅程了，我们将一步一步地指导您创建账户、管理购买和销售匹配，以及使用您的限制区域。



## Wallet 和注册



首先，如果您的智能手机上还没有安装该软件，请下载 Wallet of Satoshi。





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



如果您从未使用过 Wallet of Satoshi，并想了解它的工作原理，我建议您按照本教程进行操作，以便正确激活并安全备份。



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

现在您的 wallet 已经准备就绪，可以开始发送少量 sats。请记住，为了完成 P2P（Peer-To-Peer）平台注册，您需要发送 1000 个 sats 作为控制措施：这是为了建立一道屏障，防止任何虚假匹配（诈骗）类型的攻击，防止任何人在没有任何垃圾邮件过滤器的情况下注册。



![image](assets/it/02.webp)



我们现在可以打开 P2P（点对点）平台，进行注册。您可以通过台式电脑或智能手机上的浏览器登录，也可以通过 Telegram BitcoinVoucherBot 或 .onion 链接登录，以提供更高水平的隐私保护。



如果您选择使用 Tor .onion 链接，我还推荐使用 "Tor Browser"。如果您还不了解它，可以通过此链接了解更多信息：



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

现在，请选择到达平台的方式。





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [电脑桌面/浏览器 智能手机](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



您将被重定向到主页。



按 "Get Starter "立即开始



![image](assets/it/03.webp)



在下一个屏幕中，您必须选择并输入密码（方框 A），然后重复输入密码（方框 B）。我建议您立即将密码保存到备份介质中，可以是 "Bitwarden "之类的安全数字设备：



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

或将密码保存在纸质介质上（**警告**：这不是一个好的解决方案，但如果是作为临时解决方案，也是可以的）。



勾选验证框，说明您不是机器人（C 框）。请注意 请勿启用 RSA 加密，除非您确切知道它是什么以及如何工作。在此阶段您不需要做任何事情。点击 "生成头像"（"Generate Avatar"）（方框 D）。



![image](assets/it/04.webp)



现在您必须支付 1000 sats 来完成注册。



1.从顶部开始，首先看到随机生成的、极其重要的 "头像 ID"。小心保存，就像我建议你保存密码一样。


2.然后，您必须在下面的字段中输入您的 "闪电 Address"。如果您购买了 Bitcoin，这将允许您接收付款或退款。如果您使用的是 Wallet 或 Satoshi，您可以点击接收，复制您的 Address。


3.勾选验证框，说明您不是机器人。


4.支付 1000 sats 以进入您的禁区。如果您无法框选，请用鼠标点击（在电脑上）或用手指点击（在浏览器/Telegram 智能手机上），复制您需要粘贴到 Wallet of Satoshi 的地址，完成发票付款。



![image](assets/it/05.webp)



这是您的 LNURL Address。



![image](assets/it/06.webp)



恭喜您您已永久创建了自己的 "头像"，您可以在这里查看摘要。我再次建议您按照我之前的建议，仔细保存您的 "头像 "和密码。



单击 "我已保存证书，请继续"（译为："我已保存证书，请继续）



![image](assets/it/07.webp)



现在您已进入平台中心，可以查看所有交易匹配及其详细信息。为了看得更清楚，您可以在下面看到台式电脑网站上固有的图片。





- 类型"（"Type"）定义是 "卖出"（"Sell"）销售还是 "买入"（"Buy"）购买
- "金额"（"Amount"）：如果匹配类型为 "卖出"，则表示用户要卖出多少 sats；如果匹配类型为 "买入"，则表示用户愿意买入多少 Bitcoin。
- "带保证金的 BTC 价格"（"带保证金的 BTC 价格"）：显示的价格考虑了高于标记值的保证金。
- "保证金"（"Margin"）是应用于市场价格的百分比，如果是负号 (-)，您将获得市场价格的折扣；如果是正号 (+)，您将获得市场价格的溢价。
- "方法"（"Method"）表示用户希望用哪种方式付款。
- "创作者 "是用户在平台上使用的独特头像。
- "Rep"（声誉） 用户的声誉等级从 -5 不可靠到 +5 极其可靠不等。
- "状态"（"Status"）：表示匹配的状态。在示例截图中，所有匹配都显示为 "打开"（"Open"）。
- "过期"（"Expiration"）：显示距离比赛过期还有多少时间，如果没有人选择，比赛将被取消。



![image](assets/it/08.webp)



点击右上角的 "头像 "进入个人主页。



![image](assets/it/09.webp)



在这里，您可以看到您的头像名称、用户 ID、创建日期和声誉，这将对您在谈判中的行为产生积极或消极的影响。



![image](assets/it/10.webp)



在 "设置 "部分，您可以查看注册时输入的 "闪电 Address"，并在必要时进行更改。您还可以选择创建公钥，如前所述，只有在您具备相应技能的情况下才能设置公钥。它用于加密您与对方直接从电脑交换的信息。



强烈推荐使用 Telegram 通知功能。激活该功能后，会出现一个二维码，您可以将其与 Telegram 应用程序相框：这样，您就可以直接在 Telegram 的机器人聊天中收到与您的比赛相关的所有操作的实时通知。



![image](assets/it/11.webp)



最后，您会看到您的推荐部分，其中包含您邀请的用户所产生的收益。在这里，您可以使用按钮分享您的链接或二维码，再往下一点，您可以查看匹配列表，跟踪您的声誉以及相应的分数。



![image](assets/it/12.webp)



## 创建订单购买 Bitcoin



进入市场：从主导航栏点击购物车符号 "市场"（"Marketplace"）打开订单簿。然后开始新订单：按下 "新订单 "按钮（"New Order"）开始流程。



![image](assets/it/13.webp)





- 设置订单详情：
- 选择 "购买 Bitcoin"（"Buy Bitcoin"）选项。
- 输入您想要的 sats 数量。
- 确定价格利润率（在市场价值的 -20% 和 +20% 之间）。
- 选择付款方式（即时 SEPA 等）。
- 表示首选货币。
- 确认订单：点击 "创建订单"（"确认订单"）进入申报阶段。



![image](assets/it/14.webp)



押金要求：激活订单需要支付相当于总金额 10%的押金，外加服务费。




- 定金支付：创建订单时，系统会自动生成一张 "闪电 "发票。定金只是暂时的，订单完成后会退还。
- 主要功能
- 押金：订单金额的 10%。
- 服务费：使用平台的费用。
- 时间限制：您有 5 分钟时间付款，否则交易将失效。



![image](assets/it/15.webp)



付款成功后，订单将显示在账簿中，所有用户都可以选择并接受该订单。要创建卖出订单，您只需点击 "卖出 Bitcoin"（"Sell Bitcoin"），输入您要卖出的 satoshi 数量，设置保证金，选择付款方式和货币，然后存入 10% 作为保证金。完成后，您的匹配将出现在列表中。



![image](assets/it/16.webp)



## 如何接受订单



1.卖家可以看到书中所有可用订单的列表。


2.查看详细信息：每份订单都会显示以下信息：




  - Bitcoin 的数量、
  - 价格保证金、
  - 付款方式、
  - 用户口碑



![image](assets/it/17.webp)



3.点击订单，打开包含所有信息的完整表格。


4.按 "出售 Bitcoin"（"Sell Bitcoin"）接受建议。



![image](assets/it/18.webp)



## 卖方要求的押金



订单被接受后，系统会生成一张付款发票。定金包括



- 订单总金额、



- 服务委员会。



定金必须在规定期限内支付，否则交易将不予确认。



![image](assets/it/19.webp)



## 发送付款指示



支付定金后，交易将显示在卖方的个人仪表板上，卖方必须向买方提供详细信息，以完成法币支付。



1.卖方会在其面板上显示正在进行的交易。


2.点击 "提交付款说明"。


3.输入法币支付的所有必要信息（IBAN、收款人、地址、支付原因等）。


4.点击 "发送信息"（"Send Message"），将数据传输给买方。



![image](assets/it/20.webp)



## 付款程序



买方会在平台聊天中收到一条信息，其中包含以法定货币付款所需的所有数据：




- 银行详细信息：IBAN 以及卖方账户持有人的姓名和地址。
- 精确金额：要转账的精确法币金额。
- 原因/描述：交易中应包含的文本。
- 时限：完成付款的最后期限。



转账在 P2P 系统之外进行，必须通过个人的银行机构进行。



⚠️ **重要说明：** 只有在通过银行实际安排转账或法币支付后，才能在平台上进行确认。



![image](assets/it/21.webp)



## 确认付款



这一步对买方至关重要，只有在核实付款已实际发出后才能执行。



1.收款数据：买方已收到卖方的付款指示。


2.付款执行：从个人银行账户安排法币转账。


3.验证：检查操作处理是否正确。


4.在平台上确认：点击交易页面上的 "确认法币支付"（"Confirm fiat payment"）。


确认法币付款 "按钮出现在交易部分，只有在确认付款已发送后才可使用。



![image](assets/it/22.webp)



流程的最后一步是卖方确认收到法币付款，然后将 sats 发放给买方。



![image](assets/it/23.webp)



## 结论



希望本教程能帮助您使用一种新的方法来交易 Bitcoins 甚至直接购买它们，既可以用于自己的价值存储，也可以开始将日常支付带入生活。不过，要应对我们的数字世界即将发生的一切，这仍然是一扇需要探索的大门。



控制我们的机构正在收紧绞索，催生一个日益受控的互联网。购买 P2P 后，您将完全匿名，不会留下任何痕迹，也不会受到第三方的后续影响。