---
name: Blue Wallet

description: 比特币简洁有力的钱包
---
![cover](assets/cover.webp)



对于那些对比特币使用便捷性持怀疑态度的人来说，入门似乎是一项巨大的挑战。因此，找到合适的工具来确保比特币的易用性至关重要，这有助于比特币更好地被接受为一种交易媒介，而不仅仅是一种价值储存手段。



在本教程中，我们将了解 Blue Wallet，这是一种简单但高效的比特币钱包，它可以让您亲自管理比特币，也可以基于[多签名](https://planb.academy/resources/glossary/multisig)创建管理合作社（别担心，我们会再讲的）。






## 开始使用 Blue Wallet



Blue Wallet 是一款开放源代码的自我保管比特币钱包，可让您控制自己的比特币。它可以作为移动应用程序在 Android 和 iOS 平台上使用。在本教程中，我们将以安卓版本为基础，但所有将要开发的程序在 iOS 平台上同样有效。



![download](assets/fr/01.webp)



⚠️ 请确保在官方平台上下载 Blue Wallet 应用程序，以保证其真实性，并保护您的比特币免受可能的泄露和黑客攻击。



安装后，您可以创建一个新的钱包并保存 12 个单词的助记词，或导入已有的比特币钱包。了解如何有效备份关键字，以免丢失比特币。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

使用 Blue Wallet，您可以创建独立、专用的比特币钱包。例如，您可以在同一个应用程序中为您的储蓄和日常开支分别建立一个钱包。



![home](assets/fr/02.webp)



## 钱包类型



在 Blue Wallet 中，您会发现两种本地比特币钱包类型。



### 比特币钱包


如果您已经习惯了其他比特币钱包，如 Phoenix 或 Aqua，那么在界面上使用 Blue Wallet 的比特币钱包也不会有任何不适应。



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blue Wallet 的比特币钱包代表了比特币生态系统中的标准钱包。只要您拥有恢复助记词，就可以花费比特币，恢复助记词将在网络上提供有效签名，以证明您拥有比特币。



为了创建比特币钱包，请单击**Add now**按钮，输入钱包名称并选择 “Bitcoin” 的钱包类型。



![bitcoin-wallet](assets/fr/03.webp)



点击您的比特币钱包预览，您就可以查看您的交易历史以及发送和接收比特币。



⚠️ 比特币钱包中的所有交易都在比特币协议主链 (Mainnet) 上进行。





- 使用 Blue Wallet 接收比特币非常直观。点击屏幕下方的 **Receive** 按钮。将二维码或您的 比特币地址分享给发送者，这样他们就可以向您发送比特币了。



您还可以配置预定义金额，以指定希望接收的比特币金额。



![receive-bitcoin](assets/fr/04.webp)





- 点击 **Send** 按钮，向比特币地址发送比特币，设置所需金额并验证交易。



![send-bitcoin](assets/fr/05.webp)



Blue Wallet 可让您随心所欲地配置比特币交易的参数。



因此，如果您希望您的交易在 Mempool 中迅速得到验证并被矿工纳入区块，您可以选择适合您的交易费率。矿工会根据您选择的比率，或多或少地优先处理您的交易。在我们的 Mempool 空间教程中了解更多信息。



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- 使用 Blue Wallet，您可以为单个交易添加多个接收者。



当您添加第一个接收者的比特币地址时，在选项中点击 **Add Recipient**，添加比特币地址，然后设置发送给此接收者的金额，以此类推。Blue Wallet 将根据您的单次操作发送多批的比特币。



![add-recipients](assets/fr/07.webp)



您可以分别点击 “Remove Recipient” 和 “Remove All Recipents” 来移除一个或所有接收者。


![remove-recipient](assets/fr/08.webp)





- **增加费用**：您是否有一笔交易需要很长时间才能确认？启用增加费用功能后，您可以在待处理交易中添加额外的交易费用，以加快交易确认速度。



![bumping](assets/fr/09.webp)



### 多签名钱包



多签名钱包代表由一定数量（最少 2 个）的比特币钱包组合而成的钱包。在这种类型的钱包中，根据所选的配置和方法，比特币消费成为一种集体合作行为。



在 Blue Wallet 中，您可以为您的协会、家庭和公司创建多签名钱包。在本节中，我们将探讨这种特殊类型钱包的方方面面。



添加新的钱包，并选择 **Multisig Vault** 类型，创建多重签名钱包。



![multisig-vault](assets/fr/10.webp)



点击 **Vault Settings**，在您的多重签名组织中定义 m-of-n 配置。



⚠️ 在 m-of-n 配置中，**m** 代表批准交易所需的最少签名数量，**n** 代表贵组织的钱包数量。



请务必为贵组织的大多数成员定义最低签名数 (m)。例如，2-of-3 多重签名配置要求贵机构的两个钱包在交易执行前签名。



❗ 定义 n 等于 m 的 m-of-n 配置是一个很大的风险。当一个成员失去访问他的钱包的权限时，您就失去了钱包中消费比特币的授权。



下面是一些确保比特币安全性和可访问性的最佳配置示例：





- 2-of-3 多签名钱包。





- 5-of-7 多签名钱包。



![vault-settings](assets/fr/11.webp)



选择 P2WSH 格式以保持最佳做法。



❗ **[P2WSH](https://planb.academy/resources/glossary/p2wsh)或支付到见证脚本哈希** 是一种锁定方法，可将您的交易流出比特币（输出）锁定到 Blue Wallet 设置的自定义脚本哈希。这种锁定方式的主要优点在于它可以减少交易数据的大小，并暗中允许您支付较低的交易费用。



在配置中创建或导入 **n** 个钱包。在本教程中，我们将使用 2-of-3 的多签名配置。请确保为每个钱包单独保存恢复助记词。



![vault-keys](assets/fr/12.webp)





- 接收比特币



在多签名页面上，您可以找到交易历史以及接收和发送按钮。



在多重签名钱包中接收比特币的过程与在标准比特币钱包中接收比特币的过程相同。





- **发送比特币**：



通过管理多签名钱包，无论是与其他人还是与自己的第二个钱包签名，比特币消费都将成为一种复合行为。您的钱包的单一签名已不再足够。这就为您的比特币增加了一个安全层面，因为当一个恶意的人只拥有您的一个私钥时，他将无法花费这些比特币。



与 Blue Wallet 的标准比特币钱包一样，您可以在 **Add recipients** 选项中定义多个收件人。



在验证交易时，您需要第二个签名来批准比特币的支出。请记住，我们采用的是 2-of-3 多签名配置。



第二个钱包的签名者（如果他或她也是一个用户）可以通过扫描您刚刚创建的[部分签名交易](https://planb.academy/resources/glossary/psbt) 的二维码，即使他或她不在互联网上（没有 Wi-Fi，没有移动数据），也可以签名该交易。



![mutisig-send](assets/fr/13.webp)





- 进一步使用多签名钱包：



在多签名钱包的界面上，点击**Manage keys**按钮。



如果您忘记了某个签名钱包的恢复助记词，Blue Wallet 会从其内存中删除这些恢复词的备份。这样，您就创建了一个外部备份。



![revoke-key](assets/fr/14.webp)



执行此操作后，您将仅保留与这些恢复词关联的公钥。


⚠️ 只保留公钥（XPUB）可让您为 2-of-3 多重签名配置增加额外的安全级别。事实上，当您的手机遭受攻击时，将所有恢复词保存在同一位置可能会造成严重后果。攻击者即使只能访问您用于签署交易的其中一个密钥库 (VAULT)，也无法窃取您的比特币（至少需要 2 个签名），因为公钥不能用于签署交易。


## Blue Wallet 的更多选择



### 提高钱包访问安全性



在 "Settings" 中的 "**Security**" 选项中，您可以定义使用指纹进行交易、导出或删除钱包。这将对使用智能手机的人进行身份验证。



![biometry](assets/fr/15.webp)



## 开启闪电网络



目前，Blue Wallet 应用程序不再支持本地闪电网络。



在 "Settings" > "**Lightning Settings"** 中，当运行 Lightning Network Daemon (LND) 节点时，可以手动关联闪电钱包。安装 LND Hub，然后输入 Hub 生成的链接来了解钱包。



![ln](assets/fr/16.webp)



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

您现在已经完成了 Blue Wallet 之旅，准备好使用比特币的所有简单功能和强大功能了。我们建议您继续下一步，了解如何借助闪电网络的力量在您的店铺中接受比特币支付。



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06
