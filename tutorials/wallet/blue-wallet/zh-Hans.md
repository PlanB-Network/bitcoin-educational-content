---
name: Blue Wallet

description: Bitcoin 简洁有力的投资组合
---
![cover](assets/cover.webp)



对于那些对 Bitcoin 的简单易用性持怀疑态度的人来说，开始使用 Bitcoin 似乎是一个巨大的挑战。因此，找到合适的工具来确保这种简便性，对于更好地采用 Bitcoin 作为 Exchange 的媒介而不仅仅是价值储存手段至关重要。



在本教程中，我们将了解 Blue Wallet，这是一种简单但高效的 Bitcoin Wallet，它可以让你亲自管理比特币，也可以基于 [Multisig](https://planb.network/resources/glossary/multisig)创建管理合作社（别担心，我们会再讲的）。



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## 开始使用蓝色 Wallet



Blue Wallet 是一款开放源代码的自我保管 Bitcoin Wallet，可让您控制自己的比特币。它可以作为移动应用程序在 Android 和 iOS 平台上使用。在本教程中，我们将以安卓版本为基础，但所有将要开发的程序在 iOS 平台上同样有效。



![download](assets/fr/01.webp)



⚠️ 请确保在官方平台上下载 Blue Wallet Bitcoin Wallet 应用程序，以保证其真实性，并保护您的比特币免受可能的泄露和黑客攻击。



安装后，您可以创建一个新的 Wallet 并保存 12 个恢复词，或导入现有的 Bitcoin Wallet。了解如何有效备份关键字，以免丢失比特币。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

使用 Blue Wallet，您可以创建独立、专用的 Bitcoin 投资组合。例如，您可以在同一个应用程序中为您的储蓄和日常开支分别建立一个 Wallet 投资组合。



![home](assets/fr/02.webp)



## 投资组合类型



在 Blue Wallet 中，您会发现两种本地 Bitcoin 投资组合类型。



### Bitcoin 组合



如果您已经习惯了其他 Bitcoin 组合，如 Phoenix 或 Aqua，那么在 Interface 上使用 Blue Wallet 的 Bitcoin 组合也不会有任何不适应。



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

蓝色 Wallet 的 Bitcoin Wallet 代表了 Bitcoin 生态系统中的标准 Wallet。只要你拥有恢复字样，就可以花费比特币，恢复字样将在网络上提供有效签名，以证明你拥有比特币。



要创建 Bitcoin 投资组合，请单击**立即添加**按钮，输入投资组合名称并选择 Bitcoin 类型。



![bitcoin-wallet](assets/fr/03.webp)



点击您的 Bitcoin Wallet 预览，您就可以查看您的交易历史以及发送和接收比特币。



⚠️ Bitcoin Wallet 中的所有交易都在 Bitcoin 协议主链 (Mainnet) 上进行。





- 使用 Bitcoin Blue Wallet Wallet 接收比特币非常直观。点击屏幕下方的**接收**按钮。将二维码或您的 Bitcoin Address 分享给发件人，这样他们就可以向您发送比特币了。



您还可以配置预定义金额，以指定希望接收的 Bitcoin 金额。



![receive-bitcoin](assets/fr/04.webp)





- 点击**发送**按钮，向 Bitcoin Address 发送比特币，设置所需金额并验证交易。



![send-bitcoin](assets/fr/05.webp)



Blue Wallet 可让您随心所欲地配置 Bitcoin 装运的参数。



因此，如果您希望您的交易在 Mempool 中迅速得到验证并被矿工纳入区块，您可以选择适合您的交易费率。矿工会根据您选择的比率，或多或少地优先处理您的交易。在我们的 Mempool 空间教程中了解更多信息。



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- 使用 Blue Wallet，您可以为单个快件添加多个收件人。



当您添加第一个收件人的 Bitcoin Address 时，在选项中点击**添加收件人**，添加 Bitcoin Address，然后设置发送给此收件人的金额，以此类推。Blue Wallet 将根据您的单次操作发送多批货物的比特币。



![add-recipients](assets/fr/07.webp)



您可以分别点击**删除收件人**和**删除所有收件人**，删除一个或所有收件人。



![remove-recipient](assets/fr/08.webp)





- **夸大费用**：您是否有一笔交易需要很长时间才能确认？启用费用膨胀功能后，您可以在待处理交易中添加额外的交易费用，以加快交易确认速度。



![bumping](assets/fr/09.webp)



### Multisig 组合



Multisig（多重签名）Wallet 代表由一定数量（最少 2 个）的 Bitcoin 钱包组合而成的 Wallet。在这种类型的 Wallet 中，根据所选的配置和方法，比特币消费成为一种集体合作行为。



在 Blue Wallet 中，您可以为您的协会、家庭和公司创建多签名投资组合。在本节中，我们将探讨这种特殊类型投资组合的方方面面。



添加新的投资组合，并选择类型 **Multisig Vault**，创建多重签名投资组合。



![multisig-vault](assets/fr/10.webp)



点击 **保险库设置**，在您的多重签名组织中定义 m-de-n 配置。



⚠️ 在 m-of-n 配置中，**m** 代表批准交易所需的最少签名数，**n** 代表贵组织的投资组合数。



请务必为贵组织的大多数成员定义最低签名数 (m)。例如，2-of-3 多重签名配置要求贵机构的两个钱包在交易执行前签名。



定义 n 等于 m 的 m-of-n 配置是一个很大的风险。当一个成员失去访问他的 Wallet 的权限时，你就失去了在 Wallet 中消费比特币的授权。



下面是一些确保比特币安全性和可访问性的最佳配置示例：





- 2-de-3 多重签名。





- 5-de-7 多重签名。



![vault-settings](assets/fr/11.webp)



选择 P2WSH 格式，保持最佳做法。



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh)或支付给见证脚本 Hash** 是一种锁定方法，可将您的交易流出比特币（输出）锁定到 Blue Wallet 设置的自定义脚本的 Hash。这种锁定方式的主要优点是可以减少交易数据的大小，并暗中允许您支付较低的交易费用。



在配置中创建或导入**n**个投资组合。在本教程中，我们将使用 2 对 3 的多重签名配置。请确保为每个组合单独保存恢复字样。



![vault-keys](assets/fr/12.webp)





- 接收比特币



在 Multisig Wallet 页面上，您可以找到交易历史以及接收和发送按钮。



在多重签名 Wallet 中接收比特币的过程与在标准 Bitcoin Wallet 中接收比特币的过程相同。





- **发送比特币**：



通过管理多重签名 Wallet，无论是与其他人还是与自己的第二个 Wallet 签名，比特币消费都将成为一种复合行为。您的 Wallet 的单一签名已不再足够。这就为你的比特币增加了一个 Layer 的安全性，因为当一个恶意的人只拥有你的一个私钥时，他将无法花费这些比特币。



与 Blue Wallet 的标准 Bitcoin 产品组合一样，您可以在**添加收件人**选项中定义多个收件人。



在验证交易时，您需要第二个签名来批准比特币的支出。请记住，我们采用的是 2-de-3 多重签名配置。



第二位 Wallet 签名人（如果他或她也是用户）可以通过扫描您刚刚创建的[部分签名交易](https://planb.network/resources/glossary/psbt) 的二维码，即使他或她不在互联网上（没有 Wi-Fi，没有移动数据），也可以签署该交易。



![mutisig-send](assets/fr/13.webp)





- 多种签名**组合**，让您走得更远：



在多重签名 Wallet 的 Interface 上，单击**管理按键**按钮。



如果您忘记了其中一个签名组合的恢复字词（**忘记这个 seed...**），您将通知蓝色 Wallet 从其内存中删除这些字词的备份。这样，您就有了一个外部备份。



![revoke-key](assets/fr/14.webp)



执行此操作后，您只需保留与这些恢复字词相关的公开密钥。



⚠️ 只保留公钥（XPUB）可让您为 2-3 多重签名配置增加额外的安全级别。事实上，当您的手机受到攻击时，将所有恢复字保存在一个地方可能是有害的。攻击者如果只能访问您用来签署交易的一个 **VAULT**（关键字），就无法盗取您的比特币（至少需要 02 个签名），因为公钥不能用来签署交易。



## 蓝色 Wallet 的更多选择



### 提高组合访问安全性



在 "设置 "中的 "**安全**"选项中，您可以定义使用指纹进行交易、导出或删除 Wallet。这将对使用智能手机的人进行身份验证。



![biometry](assets/fr/15.webp)



## 激活 Lightning Network



Blue Wallet 应用程序不再支持 Lightning Network。



在 "设置">"**Lightning 设置 "**中，当运行 Lightning Network Daemon (LND) 节点时，可以手动关联 Lightning Wallet。安装 LND Hub，然后输入 Hub 生成的链接来关联 Wallet。



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

您现在已经完成了蓝色 Wallet 之旅，准备好使用 Bitcoin 的所有简单功能和强大功能了。我们建议您迈出下一步，了解如何借助 Lightning 的强大功能在店铺中接受 Bitcoin 付款。



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06