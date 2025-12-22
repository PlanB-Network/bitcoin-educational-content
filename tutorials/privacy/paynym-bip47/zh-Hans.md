---
name: BIP47 - PayNym
description: 在 Ashigaru 上使用可重复使用的付款代码
---
![cover](assets/cover.webp)



您在 Bitcoin 上可能犯的最严重的隐私错误就是重复使用地址。每当同一地址收到几笔付款时，这些交易就会链接在一起，向全世界提供您的交易地图。因此，强烈建议您始终为每张收据创建唯一的 generate 地址。但对于某些 Bitcoin 应用程序来说，这并不是一个简单的问题。



由 Justus Ranvier 于 2015 年提出的 BIP47 为这一问题提供了一个优雅的答案。它引入了**可重复使用支付代码**的概念：一种独特的标识符，几乎可以接收无限数量的链上比特币支付，而无需重复使用地址。由于采用了基于 ECDH（椭圆曲线上的差分-赫尔曼）交换的加密机制，对同一代码的每次支付都会产生一个空白地址，该地址与发送方和接收方之间的关系相关。



![Image](assets/fr/01.webp)



**PayNym**是由 Samourai Wallet 开发的系统，现在由 Ashigaru 接管。在本教程中，我们将了解如何激活您的 PayNym、与联系人交换支付密码以及在不重复使用地址的情况下进行交易。



我在这里就不详细介绍 BIP47 的操作了。如果您想深入了解，请参阅我的 BTC 204 培训课程第 6.6 章。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 先决条件



要学习本教程，您只需在 Ashigaru 应用程序上安装 wallet。如果您不知道如何下载、验证、安装应用程序或创建 wallet，我建议您先参考本教程：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## 申请 PayNym



第一步是申请您的 PayNym。每个 wallet 只需执行一次该操作。它将您从 seed (`PM...`)中获得的 BIP47 支付代码与 PayNym 实施所特有的唯一标识符联系起来。然后，这个更简短、更易读的标识符就可以传送给您的通讯员，以方便交换，而不必共享冗长、完整的 BIP47 代码。



为此，请点击界面左上方的 PayNym 图片，然后点击付款代码 "PM..."。



![Image](assets/fr/02.webp)



然后点击右上角的三个小圆点，选择 "Claim PayNym"。



![Image](assets/fr/03.webp)



点击 "申请您的 PAYNYM "按钮进行确认。



![Image](assets/fr/04.webp)



刷新页面：您的 PayNym ID 现在显示在您的图片下方，就在您的 BIP47 付款代码上方。



![Image](assets/fr/05.webp)



您的 PayNym 现已激活，可用于首次 BIP47 交易。



## 连接联系人



PayNym 之间有两种连接方式： **follow** 和 **connect**。跟随 "操作完全免费。它通过Soroban在两个PayNym之间建立链接，Soroban是一种基于Tor的加密通信协议，由Samourai团队开发，Ashigaru采用。通过这种链接，两个互相关注的用户可以私下交换信息，尤其是协调合作交易，如 Stowaway 或 StonewallX2（我们将在另一篇教程中介绍）。这个步骤是 PayNym 特有的，不是 BIP47 协议的一部分。



![Image](assets/fr/06.webp)



另一方面，连接操作（`connect`）需要一个 on-chain 事务。它包括执行 BIP47 中定义的通知事务。该 Bitcoin 事务包含 "OP_RETURN "输出中的元数据，可在付款人和收款人之间建立加密通信通道。通过该通道，付款人将能为每笔付款提供 generate 唯一的收款地址，收款人将收到这些付款的通知，并能使用与这些地址相关联的 generate 私钥，以便日后使用这些资金。



这种通知交易是有成本的：mining 费用和发送到收件人通知地址以发出连接信号的 546 sats。一旦建立连接，就可以通过 BIP47 进行几乎无限量的支付。



一言以蔽之




- follow"：免费，通过 Soroban 建立加密通信，适用于 Ashigaru 的协作工具；
- 连接"：收费，执行 BIP47 通知交易，以激活付款人和收款人之间的通道。



要与 PayNym 进行交互，您必须首先*关注它。这是建立 BIP47 连接前的第一步。比方说，您想向 PayNym `+instinctiveoffer10`发送定期付款。



进入 Ashigaru 上的 PayNym 页面，然后点击界面右下方的 `+` 按钮。



![Image](assets/fr/07.webp)



然后，您可以粘贴收件人的完整付款码，或扫描他们的 QR 码。



![Image](assets/fr/08.webp)



如果您只有他的 PayNym ID，请访问 [Paynym.rs](https://paynym.rs/)，找到与他的付款码相关的二维码。



![Image](assets/fr/09.webp)



扫描二维码后，点击 "FOLLOW"（跟随）按钮跟随 PayNym。



![Image](assets/fr/10.webp)



对于协作交易（*cahoots*），"FOLLOW "操作就足够了。但是，要发送 BIP47 付款，您需要建立连接：点击 "CONNECT "执行通知交易。



![Image](assets/fr/11.webp)



然后在网络上广播通知交易。请等待至少一次确认后再进行首次支付。



![Image](assets/fr/12.webp)



## 支付 BIP47



现在您已与收款人连接，可以向使用 BIP47 协议自动生成的唯一地址发送付款，而无需事先与收款人交换任何信息。



在 PayNym 主页，点击要付款的联系人。



![Image](assets/fr/13.webp)



在界面右上方，点击箭头图标。



![Image](assets/fr/14.webp)



输入要发送的金额。您无需输入接收地址：该地址将通过 BIP47 协议自动生成。



![Image](assets/fr/15.webp)



仔细检查交易细节，包括费用，然后拖动屏幕底部的绿色箭头，签署并广播交易。



![Image](assets/fr/16.webp)



交易已发送。



![Image](assets/fr/17.webp)



在这个例子中，付款是付给我的另一个 PayNym 钱包的。因此，我可以看到这笔钱已经到了我的另一个 Ashigaru wallet 上，没有手动交换任何地址：只使用了 PayNym 的标识符。



![Image](assets/fr/18.webp)



通过 Ashigaru 应用程序上的 PayNym 实现，您现在知道如何使用 BIP47 可重复使用支付代码了。现在，您可以与任何希望向您付款（尤其是定期付款）的人共享此付款代码。您还可以在您的网站或社交网络上发布您的 PayNym ID，以接收捐款。



要加深对该协议的了解，详细了解其工作原理及其对保密的影响，我强烈建议您参加我的 BTC 204 课程：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c