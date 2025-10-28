---
name: StashPay
description: 适合所有人的简约型 Bitcoin Wallet
---

![cover](assets/cover.webp)



用户体验是全球采用 Bitcoin 解决方案的关键因素。对于许多钱包和 Exchange 平台来说，提供流畅、简单和无技术障碍的体验是首要任务。在这方面，StashPay 以其简约的方式脱颖而出，同时也展示了 Lightning Network 的强大功能。



在本教程中，我们将了解这种投资组合的工作原理，以及它如何成为小企业或个体经营者的理想选择。



## 开始使用 StashPay



StashPay 是一款 "闪电 "自助托管 Wallet，其简约、以用户为中心的用户体验得到了广泛认可。  有了这款 Wallet，您不需要任何技术知识就可以接收和发送您的第一个卫星币。



StashPay 是一个使用 React Native 开发的开源项目，旨在解决即使在 Bitcoin 协议主链上进行交易也需要支付高额交易费的问题。它可以通过[网站]（https://stashpay.me/）上的下载链接以移动应用程序的形式在安卓和 iOS 平台上使用。



![introduce](assets/fr/01.webp)



请务必从网站上下载 Android 应用程序，因为它不在 Google Play 商店中提供。


下载完成后，请授予必要的权限，以便在 Android 手机上安装应用程序。



安装应用程序后，StashPay 会在您首次打开时为您创建一个初始 Bitcoin Wallet。在进行任何交易之前，我们建议您备份该 Wallet。以下是我们确保您的恢复短语得到正确备份的所有指导原则。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

点击 "设置 "图标进入 StashPay 设置，然后点击**创建备份**选项。然后授权显示恢复短语。请勿将恢复短语复制到手机剪贴板上，因为手机上安装的其他欺诈性应用程序可能会访问这些短语。



![backup](assets/fr/02.webp)



您也可以通过点击 ** 恢复 Wallet** 选项并插入 12 或 24 个恢复字词来恢复您已在使用的 Bitcoin Wallet。



### 在 StashPay 上接收您的第一个卫星币



在主屏幕上点击 "接收**"按钮，然后设置一个大于红色指定金额的金额。在我们的例子中，使用 StashPay Wallet 收到的金额不能少于 0.11 美元。



![receive](assets/fr/03.webp)



确定金额后，您可以点击**创建 Invoice** 按钮，然后扫描或复制 Invoice 发送给您的 satoshis 发件人。



![receive_sats](assets/fr/04.webp)



点击主页上的 "时钟 "图标，即可查看交易历史记录。



![network_fee](assets/fr/05.webp)



您会注意到，要领取卫星币，您必须支付网络费。这些费用将从您即将收到的 Satoshis 中扣除。这是因为 StashPay 是基于 Breez 开发工具包的 Wallet。若要通过该工具包的无闪电节点实现来接收 Satoshis，Breez 将向客户（在我们的案例中为 StashPay）收取 `0.25% + 40 satoshis` 的费用。更多信息，请参阅我们的Misty Breez教程。



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### 使用 StashPay 发送比特币



使用 StashPay 发送比特币非常直观，这要归功于它简约的 Interface。在主屏幕上，点击**发送**按钮。扫描二维码或粘贴您要发送比特币的 Address。StashPay 会自动检测您要发送比特币的 Bitcoin 协议链。



![send](assets/fr/06.webp)



由于 StashPay 是基于 Breez 开发套件的 Wallet，因此它具有一个有趣的优势：以低成本在主链上发送比特币。Breez 使用 Boltz 服务在 Bitcoin 协议的不同链之间进行交易，使实施开发套件的客户能够在其应用程序中直接受益于这项服务。



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

不过，Breez SDK 规定了向主链上的 Address 发送比特币的最低金额。



![onchain](assets/fr/07.webp)



您也可以使用收件人的闪电 Address 发送比特币。查看交易详情，然后点击**发送**按钮确认。



![confirm](assets/fr/08.webp)



## 更多配置



在 StashPay 设置中，您可以调整配置，个性化使用 Wallet。



StashPay 可让您根据自己选择的当地货币 Exchange 萨托希。点击**货币**选项，然后在 StashPay 提供的 +113 种货币列表中搜索您的货币。



![currencies](assets/fr/09.webp)



在**接收选项**菜单中，你可以找到使用 StashPay 接收比特币的所有设置。例如，选择 "**选择闪电或主链**"，就可以让你的 Wallet 从主链上接收比特币。



![receive-onchain](assets/fr/10.webp)



通过**扫描链上地址**选项，您可以检查链接到您不同地址的所有UTXOs（您尚未花费的比特币），从而刷新Wallet的余额。



![rescan](assets/fr/11.webp)



导出日志**菜单会列出 Breez 和 Boltz 基础设施的所有操作，这些操作涉及您的交易以及 Bitcoin 协议链之间的原子交换。



![export](assets/fr/12.webp)



您刚刚掌握了StashPay的极简版Bitcoin Wallet。如果您觉得本教程有用，我们向您推荐我们的教程：如何开始使用 Bitcoin 并赚取您的第一个比特币。



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f