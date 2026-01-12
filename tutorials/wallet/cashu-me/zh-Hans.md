---
name: Cashu.me
description: Cashu.me 电子现金使用指南
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*下面是来自 BTC Sessions 的视频教程，该视频指导您如何设置和使用 Cashu.me Bitcoin Wallet，它可以让您访问简单、廉价和私密的 Bitcoin 交易 - 无需应用程序商店！* *。


在本教程中，我们将探索 Cashu.me，这是一个基于浏览器的 Wallet，使用 Chaumian ecash 进行私人 Bitcoin 支付。在开始之前，我们先来简单了解一下 ecash 及其工作原理。


## ecash简介


想象一下，你口袋里的数字现金就像实体钞票一样--私密、即时、点对点使用，无需中介。这就是 ecash 所能实现的：一种将实物现金的私密性带回数字世界的数字支付方式。onchain-Bitcoin将每笔交易记录在任何人都能看到的公共Ledger上，而ecash则不同，它创建的私人代币代表了真实的Bitcoin价值，同时对您的消费习惯保密。


将 ecash 视为存储在您设备上的数字无记名票据--如果您持有它们，您就拥有了它们，就像拥有实物现金一样。这些代币由被称为 "Mints "的可信服务发行，这些服务持有底层的 Bitcoin 储备。当您使用 ecash 时，您不会向整个网络广播您的交易。取而代之的是，您直接与他人交换私人代币，从而创造出一种支付体验，让人感觉更像是将现金交给他人，而不是进行传统的数字支付。


Cashu 是为 Bitcoin 开发的免费开源 Chaumian ecash 协议。该技术建立在大卫-查姆（David Chaum）20 世纪 80 年代的开创性加密研究基础之上，使用 "盲签名 "来确保隐私。当您收到ecash代币时，造币厂会对其进行签名，而不会知道这些代币的下一步用途--这是防止交易被追踪的关键功能。重要的是，ecash 并没有取代 Bitcoin，而是通过解决 Bitcoin 架构要求的一些关键问题对其进行了补充。它提供了实物现金所能提供的隐私（Bitcoin 的透明 Ledger 就缺乏这种隐私），并实现了即时小额交易，无需 Blockchain 费用或确认延迟。


生态现金与 Lightning Network 无缝集成。您可以使用 "闪电 "将 Bitcoin 存入铸币厂（将您的 Bitcoin 价值转换为生态现金代币），然后再提取（将代币转换回可消费的 "闪电 "余额）。它们共同组成了一个强大的组合：Bitcoin 提供了安全结算 Layer，闪电实现了快速交易和网络互操作性，ecash 增加了隐私保护 Layer，使数字支付重新变得真正私密。


## Cashu.me


Cashu.me是一个 "进步的网络应用程序（PWA）"，它实现了Cashu协议--一种专为Bitcoin设计的Chaumian ecash的特定实现。作为一个 PWA，它可以直接在浏览器中运行，无需从应用程序商店进行安装，但您可以将其 "安装 "到您的设备上，以便更方便地访问。这种基于网络的方法可确保跨操作系统的广泛兼容性，同时通过加密协议而非平台限制来维护安全性。


## 🎉 主要功能


让我们深入了解卡舒.me 的功能，探索它能提供什么：



- 闪电上的 Chaumian ecash**：使用盲签名，因此造币厂无法追踪用户余额或交易历史记录
- 自行保管代币**：您可使用 seed 短语在本地控制 ecash 代币
- seed 短语备份**：用于恢复 Wallet 的 12 个字符的恢复短语
- 独立薄荷**：可与多家独立造币厂合作，不会被一家供应商锁定
- 即时免费交易**：在同一造币厂内，支付在数秒内完成，零手续费
- 隐私保护架构**：造币厂无法看到谁在与谁交易
- 离线电子现金**：通过本地传输协议（如 NFC、QR 码、蓝牙等）发送/接收代币，无需互联网连接
- 通过 Nostr 发现 ecash 造币厂**：通过 Nostr 协议查找并验证可信的铸币厂
- 在铸币厂之间交换现金**：所有铸币厂都会说 "闪电"，这意味着您可以在它们之间转移价值。
- 使用 Nostr Wallet Connect (NWC)** 远程控制您的 Wallet：连接到 Nostr Client 等其他应用程序，并通过 NWC 开启 Zapping 功能


关键的权衡在于 "信任"：虽然您可以控制代币本身，但您必须信任造币厂来保管基础 Bitcoin 储备。正如卡舒的文档所述


> ......造币厂正在运行闪电基础设施，并为造币厂的 ecash 用户保管 satoshis。一旦用户想换成 Lightning，就必须相信造币厂会将他们的 ecash 转换成 Redeem。

- 卡舒文件，[一般安全和隐私问题](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


这使得 ecash 成为 Bitcoin 本身的托管解决方案，但您仍可完全控制代币。


## 1️⃣初始设置


① 首先在浏览器中访问 [Wallet.cashu.me](https://Wallet.cashu.me)。由于 Cashu.me 是一个 "PWA"，您无需从应用程序商店下载，只需直接在浏览器中打开网站即可。为了方便访问，您可以选择将其安装到设备的主屏幕上。


要安装 PWA，请点击浏览器中的⋮菜单按钮并选择 "添加到主屏幕"。安装完成后，关闭浏览器标签，从设备的主屏幕启动 Cashu.me。在欢迎界面，点击 "下一步 "继续。


③ 安全至关重要。将您的 seed 短语安全地保存在密码管理器中，或者最好写在纸上。如果您无法使用本设备，这 12 个字的恢复短语是您恢复资金的唯一方法。点击 👁️ 图标显示您的 seed 短语，按顺序认真写下所有 12 个单词，然后勾选 "我已写下"。点击 "下一步 "继续，并在下一屏幕的 "条款 "复选框中打勾确认接受 "条款"。


![image](assets/en/01.webp)


完成设置后，您需要连接到 "薄荷糖"。点击 "添加铸币厂"，然后点击 "发现铸币厂"，查看 Nostr 社区推荐的铸币厂。为了进一步验证，您可以在 [bitcoinmints.com](bitcoinmints.com) 查看薄荷评级。


然后点击 "点击浏览薄荷糖"，查看完整列表。复制薄荷糖的 URL，将其粘贴到 URL 字段中，并给它起一个好记的名字，以此来选择薄荷糖。在本例中，我们将使用


URL：`https://mint.minibits.cash/Bitcoin`

名称：Minibits


![image](assets/en/02.webp)


点击 `ADD MINT` 完成此过程。在确认屏幕上，确认您信任该薄荷糖的操作员，然后再次轻点`添加薄荷糖`。Minibits 造币厂现在将出现在您的主屏幕上。Wallet 设置完成后，您需要在进行交易前为其注资。


![image](assets/en/03.webp)


## 2️⃣资助您的 Wallet


Cashu.me 为您的 Wallet 提供两种不同的汇款方式。当您点击主屏幕上的 "接收 "时，您将看到通过 "现金 "或 "闪电 "接收资金的选项。


![image](assets/en/04.webp)


### 通过 LIGHTNING 筹集资金


第一个选项是通过闪电 Invoice 为 Wallet 提供资金。如果您添加了不同的铸币厂，请选择一个铸币厂，并确定您希望收到的 "金额 (Sats)"。然后点击 "创建Invoice."，您就会得到一个QR码，您可以用另一个闪电Wallet扫描，或者您也可以直接 "复制 "Invoice，然后粘贴到另一个Wallet中，为您的cashu.me Wallet支付和注资。


![image](assets/en/05.webp)


### 接收现金


ecash 方法可让您直接从另一个 ecash Wallet 接收代币。首先点击 "接收 "按钮，然后选择 "ecash "选项。您可以 "粘贴 "或 "扫描 "或使用 "NFC "从另一个 Wallet 提交现金 token。如果您选择粘贴，请输入您从其他 Wallet 复制的 token 字符串，"金额 "和 "薄荷糖 "将自动显示。点 "接收 "完成交易，Sats 将出现在您的 Wallet 中。请注意，您的余额现在分布在多个铸币上。例如，您的 Minibits "铸币厂 "中可能有 1,000 Sats，而 Coinos "铸币厂 "中可能有另外 1,000 Sats。这种不同铸币厂之间的分离是卡舒架构的一个重要方面。


![image](assets/en/06.webp)


### 交换薄荷糖


如果您不再信任您所添加的某个造币厂，cashu.me提供了一个从一个造币厂到另一个造币厂的 "资金交换 "功能。进入造币厂选项卡，向下滚动直到看到 "Multimint Swaps"。从下拉菜单中选择 "FROM "和 "TO "造币厂，然后输入您要转移的金额。点击 "SWAP "在铸币厂之间转移代币。这将通过闪电交易执行，因此您需要为潜在的闪电费用留出空间。在我的例子中，1 sat 就足够了。


![image](assets/en/07.webp)


## 3️⃣寄送资金


要发送 Sats，Cashu.me 提供两种选择。通过 "现金 "或 "闪电 "发送。让我们来看看这两种方式。


### 通过闪电发送


要通过 Lightning 发送，请按照以下步骤操作：


1.点击主屏幕上的 "发送"，然后选择 "闪电

2.应用程序会提示您输入 "Lightning Invoice "或 "Address"。您可以直接粘贴 Invoice/Address，或使用扫描 QR 码选项直观地捕捉它，然后用 `ENTER` 加以确认。

3.使用下拉栏选择要支付的 Mint，然后点击 "PAY "确认。 **注意**：在 "设置"->"实验 "下还有一个使用 "Multinut "的选项，可以让你同时支付多个薄荷糖的发票。

4.成功完成后，您将看到付款确认和从余额中扣除的金额。


![image](assets/en/08.webp)


### 通过 ecash 发送


发送电子现金同样简单明了。


1.点击 "发送"，然后选择 "现金 "选项。

2.选择薄荷糖"，在 Sats 中输入您要发送的 "金额"，然后点击 "发送 "确认。

3.这将创建一个 "动画 QR 码"，您可以通过调整速度和大小参数来定制该 QR 码。任何人都可以通过扫描该 QR 码立即获得 Redeem 的 Sats，也可以点击 "复制"，通过蓝牙、NFC 或标准信息等其他渠道将 token 字符串发送给其他人。

4.我正在打开另一个 Wallet。从剪贴板粘贴并在另一个 Wallet 中选择 "接收现金"。


![image](assets/en/09.webp)


## 4️⃣附加功能


除了核心的发送和接收功能外，Cashu.me 还提供了强大的附加功能，可增强您在 Nostr 生态系统中的 Bitcoin 体验。


### Nostr Wallet 连接


Nostr Wallet Connect (`NWC`)通过在 Wallet 和社交应用程序之间建立无缝连接，改变了您与 Nostr 应用程序的交互方式。该协议允许 [Damus](https://damus.io/) 或 [Primal](https://primal.net/home) 等应用程序直接通过 Nostr 中继请求付款，而无需离开应用程序。


在 Cashu.me 中设置 "NWC"：


1.转到左上角汉堡菜单上的 "设置

2.滚动到 "NOSTR Wallet CONNECT "部分并点击 "启用 "按钮

3.然后，您将设定一个限额，以确定申请从 Wallet 中支出的最高金额。

4.配置完成后，您可以复制连接字符串并将其粘贴到任何支持 "NWC "的 Nostr 客户端，从而实现即时斩波和小费功能。


![image](assets/en/10.webp)


### Lightning Address via npub.cash


Cashu.me与[npub.cash](https://npub.cash/)整合，为您提供与Nostr协议无缝对接的闪电Address。在这里，您可以注册并通过提供您的 Nostr `nsec` 申请您的用户名，费用为 5,000 Sats 并支持 npub.cash 项目，您也可以使用任何 Nostr 公钥 (`npub`) 而无需注册。


首先，进入 "设置 "并点击 "启用 "使用 npub.cash 的闪电 Address。这将 generate 一个 npub.cash Address，默认使用从您的 Wallet seed 短语导出的`npub`字符串。


或者，访问 [this webpage](https://npub.cash/username)，使用您自己的 Nostr `nsec` 申请自定义用户名，这样您就可以获得类似 username@npub.cash 的个性化 Lightning Address。


![image](assets/en/11.webp)


## 🎯 结论


Cashu.me提供私人Bitcoin支付，其功能与实物现金类似--点对点即时支付，不会暴露您的交易历史。我个人非常欣赏它的 PWA 架构，因为它的运行不受应用程序商店的限制。Wallet 将 Bitcoin 的安全性、"闪电 "的速度和 ecash 的私密性结合在一起，提供的用例可以提高日常 Bitcoin 的采用率。


虽然通过自我保管，您可以完全控制您的ecash代币，但请记住，造币厂作为可信赖的第三方，持有底层的Bitcoin储备。使用多个造币厂并在它们之间交换的能力提供了灵活性，同时也维护了隐私。


得益于 NWC 和 npub.cash 地址等功能，Cashu.me 对于重视隐私和主权而非大技术政策限制的社交客户来说，是一个极具吸引力的 Wallet 选项。


## 资源


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)