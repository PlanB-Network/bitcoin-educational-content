---
name: Stonewall x2
description: 理解并使用Stonewall x2交易
---
![cover stonewall x2](assets/cover.webp)

***警告：** 继Samourai Wallet的创始人在4月24日被逮捕，其服务器被查封之后，Stonewallx2交易只能通过手动交换PSBTs（参与方之间）来进行，前提是双方用户都连接到自己的Dojo。然而，这些工具可能在未来几周内重新启动。与此同时，您仍然可以查阅本文，以理解Stonewallx2的理论操作并学习如何手动进行这些操作。*

_如果您考虑手动执行Stonewallx2交易，该过程与本教程中描述的非常相似。主要区别在于Stonewallx2交易类型的选择：不是选择`Online`，而是点击`In Person / Manual`。然后，您需要手动交换PSBTs来构建Stonewallx2交易。如果您与合作者身处近距离，可以依次扫描QR码。如果您身处远处，可以通过安全的通信渠道交换JSON文件。教程的其余部分保持不变。_

_我们正在密切关注此案件的发展以及与之相关工具的发展。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守其管辖区的法律。_

---

> *让每一次支出都成为coinjoin。*

## 什么是Stonewall x2交易？

Stonewall x2是一种特定形式的比特币交易，旨在通过与第三方合作（该第三方未参与该支出）来增加用户在支出过程中的隐私。这种方法模拟了两个参与者之间的迷你coinjoin，同时向第三方支付。Stonewall x2交易在Samourai Wallet应用程序和Sparrow Wallet软件上都可用。两者是互操作的。

其操作相对简单：我们使用我们拥有的UTXO进行支付，并寻求第三方的协助，他们也用自己的UTXO贡献。交易结果产生四个输出：其中两个等额，一个用于支付接收者的地址，另一个用于合作者的地址。第三个UTXO返回给合作者的另一个地址，允许他们检索初始金额（对他们来说是一个中性行为，减去挖矿费），最后一个UTXO返回给我们的地址，这构成了支付的找零。

因此，在Stonewall x2交易中定义了三种不同的角色：
- 发送者，实际进行支付的人；
- 合作者，提供比特币以提高交易整体匿名性，同时在最后完全回收他们的资金（对他们来说是一个中性行为，减去挖矿费）；
- 接收者，可能不知道交易的具体性质，只是期待来自发送者的支付。

让我们通过一个例子来更好地理解。Alice在面包店买她的法棍面包，价格是`4,000 sats`。她想用比特币支付，同时保持一定程度的支付隐私。因此，她请求她的朋友Bob协助她完成这个过程。
![schema stonewall x2](assets/en/1.webp)
通过分析这笔交易，我们可以看到面包师确实收到了`4,000 sats`作为面包的付款。Alice使用了`10,000 sats`作为输入，并收到了`6,000 sats`作为输出，结果净余额为`-4,000 sats`，这对应于面包的价格。至于Bob，他提供了`15,000 sats`作为输入，并收到了两个输出：一个是`4,000 sats`，另一个是`11,000 sats`，结果余额为`0`。在这个例子中，我故意忽略了挖矿费用以便于理解。实际上，交易费用是由付款发送者和合作者平均分担的。

## Stonewall和Stonewall x2之间有什么区别？

StonewallX2交易的工作方式与Stonewall交易完全相同，除了前者是协作的而后者不是。正如我们所见，Stonewall x2交易涉及到第三方的参与，这个第三方不参与付款，并且会提供他们的比特币来增强交易隐私。在典型的Stonewall交易中，合作者的角色由发送者扮演。

让我们重新审视Alice在面包店的例子。如果她找不到像Bob这样的人来陪她共同承担费用，她本可以独自完成一个Stonewall交易。因此，两个输入的UTXOs将是她的，她将在输出处收到3个。
![transaction stonewall](assets/en/2.webp)

从外部角度来看，交易模式将保持不变。
![Stonewall还是Stonewall x2?](assets/en/5.webp)
因此，使用Samourai支付工具时，逻辑应该如下：
- 如果商家不支持Payjoin Stowaway，可以与支付之外的另一个人一起完成协作交易，使用Stonewall x2。
- 如果找不到人来进行Stonewall x2交易，可以独自完成一个Stonewall交易，模仿Stonewall x2交易的行为。
- 最后的选项将是与JoinBot进行交易，JoinBot是由Samourai维护的服务器，可以根据请求，充当Stonewall x2交易中的合作者。

如果你想找到一个愿意协助你进行Stonewall X2交易的合作者，你也可以访问这个由Samourai用户维护的非官方Telegram群组，以连接发送者和合作者：[Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin)。

[**-> 了解更多关于Stonewall交易**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Stonewall x2交易的目的是什么？

Stonewall x2结构为交易增加了大量的熵，并混淆了链上分析。从外部来看，这样的交易可以被解释为两个个体之间的小型Coinjoin。但实际上，它是一次支付。这种方法在链上分析中产生了不确定性，甚至导致了错误的线索。

让我们回到Alice、Bob和面包师的例子。区块链上的交易看起来会是这样：
![stonewall x2 public](assets/en/3.webp)
依靠常见链分析启发式规则的外部观察者可能会错误地得出结论：“Alice 和 Bob 执行了一个小额的 coinjoin，每人输入一个 UTXO，输出两个 UTXO。”![misinterpretation stonewall x2](assets/en/4.webp)这种解释是不正确的，因为正如你所知，一个 UTXO 被发送给了 Baker，Alice 只有一个找零输出，而 Bob 有两个。
![transaction stonewall x2](assets/en/1.webp)
即使外部观察者设法识别出 Stonewall x2 交易的模式，他们也不会拥有所有信息。他们将无法确定两个相同金额的 UTXO 中哪一个对应于支付。此外，他们将无法知道是 Alice 还是 Bob 进行了支付。最后，他们将无法确定两个输入 UTXO 是来自两个不同的人，还是属于将它们合并的一个人。这最后一点是因为，正如我们上面讨论的，经典的 Stonewall 交易与 Stonewall x2 交易遵循完全相同的模式。从外部且没有关于上下文的额外信息，不可能区分 Stonewall 交易和 Stonewall x2 交易。然而，前者不是协作交易，而后者是。这增加了对这笔费用的更多疑问。
![Stonewall or Stonewall x2 ?](assets/en/5.webp)

## 如何建立 Paynyms 之间的连接以通过 Soroban 协作？

与 Samourai 上的其他协作交易（*Cahoots*）一样，执行 Stonewall x2 涉及发送方和合作者之间部分签名交易的交换。这种交换可以手动完成，如果你与你的合作者身处同一地点，或者通过 Soroban 通信协议自动完成。

如果你选择第二个选项，你需要在能够执行 Stonewall x2 之前建立 Paynyms 之间的连接。为此，你的 Paynym 必须“关注”你合作者的 Paynym，反之亦然。

**访问合作者的 Paynym:**

首先，需要获取合作者 Paynym 的支付代码。在 Samourai Wallet 应用中，你的合作者必须按下位于屏幕左上角的他们的 Paynym（小机器人）图标，然后点击他们的 Paynym 昵称，以 `+...` 开头。例如，我的是 `+namelessmode0aF`。

![samourai paynym](assets/notext/6.webp)
如果你的合作者使用 Sparrow Wallet，他们应该点击 'Tools' 标签，然后点击 'Show PayNym'。![paynym sparrow](assets/notext/7.webp)
**从 Samourai Wallet 关注你的合作者的 PayNym:**

如果你正在使用 Samourai Wallet，启动应用并以同样的方式访问 'PayNyms' 菜单。如果这是你第一次使用你的 PayNym，你将需要获取其标识符。

![request paynym samourai](assets/notext/8.webp)

然后点击屏幕右下角的蓝色 '+'。
![add collaborator paynym](assets/notext/9.webp)
你可以通过选择 'PASTE PAYMENT CODE' 粘贴你合作者的支付代码，或者按 'SCAN QR CODE' 打开相机扫描他们的二维码。
![粘贴 Paynym 标识符](assets/notext/10.webp)
点击“FOLLOW”按钮。
![关注 Paynym](assets/notext/11.webp)
点击“YES”确认。
![确认关注 Paynym](assets/notext/12.webp)
接下来，软件会提供一个“CONNECT”按钮。在我们的教程中不需要点击此按钮。此步骤仅在您计划作为 [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093) 的一部分向另一个 PayNym 进行支付时需要。
![连接 Paynym](assets/notext/13.webp)
一旦您的 PayNym 开始关注您的合作者的 PayNym，重复此过程，但方向相反，这样您的合作者也可以关注您。然后，您可以执行 Stonewall x2 交易。

**从 Sparrow Wallet 关注您合作者的 PayNym：**

如果您使用的是 Sparrow Wallet，打开您的钱包并访问“Show PayNym”菜单。如果您是第一次使用您的 PayNym，您需要通过点击“Retrieve PayNym”来获取一个标识符。
![请求 Paynym Sparrow](assets/notext/14.webp)
然后在“Find Contact”框中输入您合作者的 PayNym 标识符（他们的昵称“+...”或他们的支付代码“PM...”），并点击“Add Contact”按钮。
![添加联系人 Paynym](assets/notext/15.webp)
接下来，软件会提供一个“Link Contact”按钮。在我们的教程中不需要点击此按钮。此步骤仅在您计划作为 [BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093) 的一部分向指定的 PayNym 进行支付时需要。

一旦您的 PayNym 开始关注您的合作者的 PayNym，重复此过程，但方向相反，这样您的合作者也可以关注您。然后，您可以执行 Stonewall x2 交易。
## 如何在 Samourai Wallet 上进行 Stonewall x2 交易？

如果您已完成连接 Paynyms 的前面步骤，您终于可以进行 Stonewall x2 交易了！要做到这一点，请按照我们在 Samourai Wallet 上的视频教程操作：
![Stonewall x2 教程 - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## 如何在 Sparrow Wallet 上进行 Stonewall x2 交易？

如果您已完成连接 Paynyms 的前面步骤，您终于可以进行 Stonewall x2 交易了！要做到这一点，请按照我们在 Sparrow Wallet 上的视频教程操作：
![Stonewall x2 教程 - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**外部资源：**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.