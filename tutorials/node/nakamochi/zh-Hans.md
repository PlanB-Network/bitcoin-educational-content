---
name: Nakamochi
description: 节点运行更轻松 - 如何配置和使用 Nakamochi 比特币和闪电网络节点。
---

![image](assets/cover.webp)

运行自己的 Bitcoin 和 Lightning Full node 不再是技术专家才能完成的复杂任务。传统上，建立和管理节点需要对密码学、网络和软件开发有深入的了解。Nakamochi 改变了这一状况，让每个人都能使用节点，无论其技术背景如何。


有了 Nakamochi，任何人都可以在家建立和运营一个节点，实现完全的隐私和财务独立。运行 Full node 不仅能确保自己的交易安全，还能增强 Bitcoin 网络的实力。去中心化和弹性的 Bitcoin 网络依靠广泛的节点分布来确保其安全性和独立性。


### 目录



- 什么是 Nakamochi 及其工作原理？
- 设置仲町
- 关于 Lightning Network
- 在 Lightning Network 中开辟渠道和进行交易



## 什么是 Nakamochi 及其工作原理？


Nakamochi 是一款仅支持 Bitcoin 和闪电网络的 Full node。它包括一个集成的 Bitcoin 和 Lightning Wallet，使用户能够运行一个安全、自主权的 Bitcoin 节点，同时受益于 Lightning Network 的速度和低交易成本。


您的 Nakamochi 节点通过手机应用程序 [BitBanana (Android)](https://bitbanana.app) 和 [Zeus (iOS)](https://bitbanana.app) 进行管理，让您可以随时随地方便地控制节点。这些应用程序就像您的节点的远程控制装置，让您可以直接使用 Bitcoin 或 Lightning 进行支付、管理交易、打开或关闭通道、检查余额以及监控节点性能，一切都非常方便。



## 设置 Nakamochi 仅需 5 分钟


### 步骤 1：接入并开始使用


1.将 Nakamochi 连接到电源和 Wi-Fi 网络。

2.点击 **"设置新的 Wallet"**，安全地存储您的 24 字恢复短语。

3.使用节点管理应用程序（Zeus 或 BitBanana）连接 Nakamochi：

4.打开应用程序，扫描 Nakamochi 上显示的 QR 码。

5.为提高安全性，请在设备上设置 PIN 码。


![image](assets/en/01.webp)

_连接电源并写下您的24个单词助记词_


![image](assets/en/02.webp)

_请等待区块链追上进度_


![image](assets/en/03.webp)

_在 Lightning 选项卡中设置新钱包_


![image](assets/en/04.webp)




_使用节点管理应用扫描二维码_

![image](assets/en/05.webp)

_为额外安全设置PIN码_



**注意：** _允许您的Nakamochi节点与区块链同步。此过程可能会根据您的互联网连接花费一些时间。_



## 关于 Lightning Network


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bitcoin Lightning Network 彻底改变了 Bitcoin 的交易方式，使其更快、更便宜、更高效。它非常适合日常使用，能以最低的费用实现近乎即时的支付，是购买咖啡或处理频繁小额消费等小额交易的理想选择。

通过运行 off-chain，"闪电 "可进行扩展，每秒可支持数千笔交易，而不会使主要的 Bitcoin Blockchain 负荷过重。这使它成为 Bitcoin 演进为实用的全球支付系统的关键角色。

隐私是另一个优势，因为 Lightning 上的交易是通过私人支付渠道进行的，而不是直接记录在 Blockchain 上。这确保了更隐蔽的交易方式，同时保持了 Bitcoin 的强大安全性。



#### 支付渠道说明


Lightning Network 通过支付通道进行操作，这种通道是双方之间的连接，允许进行多项交易，而无需直接与 Blockchain 交互。当通道打开时，每笔交易都会在第二个 Layer Lightning 解决方案上更新双方的余额，从而确保快速、低成本的支付。这种设计确保了可扩展性和私密性，因为个人交易在公共 Ledger 上不会被记录。


**示例：** Alice 和 Bob 通过提交 Bitcoin 打开了一个通道。爱丽丝向鲍勃发送比特币，他们的 off-chain 余额立即更新，没有 On-Chain 记录。如果爱丽丝向查理付款，而爱丽丝与查理没有直接通道，则付款可以通过鲍勃的通道到达查理。通过中间节点进行路由，即使没有直接连接也能确保支付，从而使网络变得高效。



## 在 Lightning Network 中开辟渠道和进行交易


设置好 Nakamochi 并将其连接到节点管理应用程序后，您就可以开始使用 Lightning Network，打开通道并进行交易。


### 在 Zeus（iOS）上打开频道：


1.转到 **"频道 "** 选项卡（底部菜单）。

2.点击 **"+"**，打开一个新频道。

3.扫描或输入要连接的节点的密码。

4.输入锁定金额（与同行一起选择，或使用知名节点的最低固定金额）。

5.点击 **"打开通道 "**。


![image](assets/en/06.webp)

_ZEUS屏幕截图_


更多信息：[Channel | Zeus Documentation](https://docs.zeusln.app/)


### 在 BitBanana（安卓）上打开频道：


1.打开汉堡菜单（左）。

2.转到 **"频道 "**。

3.点击 **"+"**，添加/打开新频道。

4.扫描或粘贴密钥。

5.输入锁定金额（与同行一起选择，或使用知名节点的最低固定金额）。


![image](assets/en/07.webp)

_Bitbanana Screenshot_比特香蕉截图


更多信息: [BitBanana](https://bitbanana.com)


一旦您的通道开通，就可以通过它向网络中的其他参与者付款。余额会以 off-chain 的方式进行调整，确保交易几乎即时完成，并将费用降到最低。

如果您不再需要某个频道，可以关闭该频道。此操作将结算您和同行之间的最终余额，并记录为 On-Chain。理想情况下，双方都同意并在线进行 "合作关闭"（与无反应/离线的同行进行 "强制关闭 "相比，速度更快，费用更少）。

一般来说，我们建议保持通道开放，以降低成本，提高网络可靠性和效率。通过保持通道开放，可以最大限度地减少 On-Chain 交易费，避免因通道重新连接而造成的停机，并保持稳定的路由能力，实现无缝支付处理。这种方法可促进网络的稳健和弹性，同时提升整体用户体验并减少运营开销。



### 实用链接



- [关于 Nakamochi](https://nakamochi.io/)
- [订阅 Nakamochi 的新闻通讯](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)