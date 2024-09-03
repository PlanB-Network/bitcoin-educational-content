---
name: Phoenix

description: 设置您的Phoenix钱包
---

![phoenix](assets/cover.webp)

## 介绍

Phoenix是由Acinq团队创建的一款非托管式闪电网络钱包，该团队是闪电网络Eclair实现的背后力量。

请记住，Phoenix是一款专注于闪电网络支付的移动应用程序，但同时还支持链上支付，通过集成的交换功能。这意味着任何存入Phoenix的链上资金，都会立即被转换成一个闪电网络通道。

同时，如果您想向一个链上地址发送资金，Phoenix将会在内部从您的LN通道交换到链上目的地。请注意，所有这些交换都有成本，因为涉及到链上费用。

在下面的“入门指南”部分，我们将引导您完成设置过程，并进一步解释如何使用Phoenix管理闪电网络流动性。

## 重要资源
- Phoenix官方网页 - [https://phoenix.acinq.co](https://phoenix.acinq.co)
- 文档 / 常见问题页面 - [https://phoenix.acinq.co/faq](https://phoenix.acinq.co/faq)
- [Github页面](https://github.com/ACINQ/phoenix/) | [Github发布页面](https://github.com/ACINQ/phoenix/releases)（直接下载apk）
- [支持和讨论](https://github.com/ACINQ/phoenix/discussions)
- [Acinq博客](https://acinq.co/blog) - 公告

## 视频教程

![Phoenix: 比特币闪电网络钱包教程](https://youtu.be/cbtAmevYpdM?si=zctujxtI0hI-jKpC)

## 入门指南

这里是一个分步指南，介绍如何开始使用Phoenix，设置，进行/接收支付，管理流动性，备份/恢复过程。

### 下载与设置
您可以从以下位置下载并安装Phoenix：[App Store](https://apps.apple.com/us/app/phoenix-wallet/id1544097028) | [Google Play商店](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) | [直接下载apk](https://github.com/ACINQ/phoenix/releases)

按照从欢迎屏幕开始的指示，一步步进行。

![](assets/screenshot2.webp)

您将被告知自动创建闪电网络通道的信息。
从v2.0版本开始是一个重大升级，带来了“拼接”到Phoenix：
- 单一动态通道，
- 不再有1%的入站流动性费用
- 更好的可预测性和控制
- 无需信任的交换

查看[Phoenix博客文章](https://acinq.co/blog/phoenix-splicing-update)了解更多详情，特别是新的费用模型。

![](assets/screenshot3.webp)

### 流动性快速指南

因此，一旦您接收/存入sats到这个钱包，它将自动与ACINQ节点开启通道。通常，通道的大小会略大于您存入的金额。所以每次存款您都会有一个新的通道，除非当您还没有完全耗尽通道并且收到了一个较小的支付，它将被重新填充。

对于Phoenix闪电网络流动性，我们建议以下场景：

随着新版本v0.2.0引入了新的LN功能拼接。这意味着从现在开始，您不必再处理每次收到支付时许多新的小通道了。

如果入站流动性不足，Phoenix将增加您初始通道的大小，但这仍然会涉及链上费用。您可以在Phoenix设置中的支付选项和费用中设置该费用。
因此，我们建议从一个大通道开始使用Phoenix，比如1-3-5M sats。与通道的大小相比，您的提交费用将微不足道，不会对您造成太大影响。此外，与每次存款支付至少3000 sats的费用4-5次（或任何次数您存入小额）相比，您只需支付一次开通通道的费用。
如果您开始从该通道消费，请不要全部花光，因为Phoenix会关闭它。

如果您在通道中留有一些sats，并且从另一个LN钱包/存款来源再次充值，我们有两种情况需要考虑：
- 如果新的存款金额大于您的通道容量，Phoenix将调整通道大小，并且您将支付额外费用。
- 如果新的存款金额小于您的通道容量，则不会涉及任何费用。

因此，尝试根据您个人的消费需求来设置初始通道容量。在通道的限制内消费和替换不会再产生任何费用，使用这款钱包应用的体验将会很流畅。

### 备份
在接下来的屏幕中，您将被告知Phoenix应用将生成一个种子短语作为您钱包的备份。稍后这些种子词必须保存在一个安全的地方！

![](assets/screenshot4.webp)

接下来的屏幕将指示您是想创建一个新钱包还是从种子短语恢复之前的钱包。

![](assets/screenshot5.webp)

一旦新钱包被创建，您将被提醒应该备份种子短语。点击“备份钱包”按钮。

![](assets/screenshot6.webp)

您将被提醒，这些来自种子的词非常重要且敏感，您应该保持它们的私密性。

![](assets/screenshot7.webp)

这些种子词您必须将它们保存在一个安全的地方，比如密码管理器（[KeePass](https://keepass.info/) 或 [Bitwarden](https://bitwarden.com/)），将这个密码管理器的数据库保存在一个离线的USB加密棒中以确保完全的安全。

![](assets/screenshot8.webp)

### 接收支付

在您开始接收之前，请阅读上一章节“流动性快速指南”。

现在，您已经准备好在您的Phoenix钱包中接收sats了！

![](assets/screenshot9.webp)

在Phoenix接收支付，您有以下选项：
- 使用显示的QR码，代表一个“空”的Lightning发票
- 编辑Lightning发票（见QR码下方的编辑按钮），您可以添加一定数量的sats，添加显示给付款人的评论
- 使用/扫描一个LNURL-withdraw QR码
- 从您的Phoenix钱包生成一个链上比特币地址。请记住，这笔支付将被“转换”成一个新的Lightning通道（如果您还没有开通一个）或调整现有Lightning通道的大小。

![](assets/screenshot10.webp)

显示编辑新Lightning发票并为其生成新QR码的屏幕：

![](assets/screenshot11.webp)

这是您可以生成链上BTC地址的屏幕，并被告知向此地址的支付将被“转换”成闪电网络流动性并涉及一些费用。

![](assets/screenshot12.webp)

一旦支付完成，将显示确认屏幕，全部完成！

![](assets/screenshot13.webp)
您可以为每笔收到的付款添加个人备注。这些备注不会保存在其他任何地方，只会保留在您的设备中。如果您恢复您的Phoenix钱包，这些备注将不会被恢复。这是一个用来跟踪您发送和接收的付款的有用功能。
![](assets/screenshot14.webp)

### 发送付款

发送付款是一个相当简单的过程，只需点击主屏幕上的“发送”按钮

![](assets/screenshot15.webp)

系统会提示您允许Phoenix应用访问设备相机，以便能够扫描QR码。

![](assets/screenshot16.webp)

在付款屏幕上，您有3个选项：
- 从接收者的Lightning发票/LNURL中扫描QR码
- 手动输入（粘贴），Lightning地址输入或LNURL-pay代码
- 从本地磁盘加载QR图像

![](assets/screenshot17.webp)

如您在此屏幕上看到的，付款请求已被扫描且详情已自动填写。您只需按“支付”按钮即可。

![](assets/screenshot18.webp)

一旦付款发送并确认，将显示一个包含付款简短详情的确认屏幕，包括支付的费用。如果您想查看更多付款详情，请点击“详情”按钮。

![](assets/screenshot19.webp)

在详情屏幕上，您可以看到付款的技术详情，包括：付款哈希和请求、预图像、目的节点和持续时间。有时这些详情对于跟踪付款、调试或与接收者识别特定付款很有用。

![](assets/screenshot20.webp)

### 设置

在设置菜单中，没有太多事情要做，Phoenix追求简洁。但这里有一个重要方面是管理支付通道和费用的菜单，您可以在这里设置您希望的费用水平。请记住，在内存池高费用环境中，您不应使用非常低的费用，否则您的支付和开通通道将会受阻和/或失败。

设置菜单中的其他选项：
- 显示 - 切换到不同的颜色主题
- Electrum服务器 - 检查您连接的Electrum服务器的状态或指定一个
- Tor - 如果您想在Tor网络后面使用Phoenix
- 应用访问设置 - 为Phoenix设置特定设备服务的权限
- 恢复短语 - 如果您想检查种子词和/或进行新的备份
- 通道列表 - 显示您的Lightning通道的状态和可用的流动性（进/出）
- 日志 - 显示调试日志
- 关闭所有通道 - 只有在您想要永久关闭您的Phoenix节点并将资金恢复到您的链上地址时才应使用的危险选项。稍后可以使用您的Phoenix种子短语通过Electrum钱包检索该地址。

![](assets/screenshot21.webp)

### 重置

如果您处于Phoenix应用出现问题的情况（不进行支付、不连接到Electrum服务器、无法接收支付）或您只是想将其移动到另一台设备，您必须确保两个方面：
- 备份您的种子短语
- 停止您设备中的应用 - 转到应用详情并强制停止服务
- 如果您想将其移动到新设备，请从旧设备卸载它
- 不要在多个设备上运行相同的Phoenix钱包！

![](assets/screenshot22.webp)

一旦您重新安装它或在新设备上安装它，点击“恢复”按钮并按照说明操作

![](assets/screenshot23.webp)
您不能使用从其他钱包应用生成的其他类型的种子。[在此处查看更多详情](https://walletsrecovery.org/)关于其他钱包类型及其种子和派生路径。并非所有的都兼容！
![](assets/screenshot24.webp)

您必须按照特定顺序，逐一输入之前保存的种子词。输入完12个词后，点击“导入”按钮，完成操作。

![](assets/screenshot25.webp)

几刻钟后，您将看到显示的之前的余额。同时，您将收到备份种子的提醒。如果您已经备份，可以直接进入菜单并选择“我已保存备份”。

![](assets/screenshot26.webp)

完成！快乐的闪电网络体验！