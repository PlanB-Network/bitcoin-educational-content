---
name: Boltz
description: 在不同的 Bitcoin 层之间切换，同时保持控制。
---


![cover](assets/cover.webp)



自 2009 年部署以来，Bitcoin 的点对点电子现金系统得到了飞速发展，为各种解决方案注入了活力，使其成为我们在日常行动中可以立即使用的系统，特别是通过 Lightning Network。



然而，Bitcoin 协议各层之间仍存在一个主要问题：流体互操作性。为了充分挖掘 Bitcoin 的潜力，当务之急是找到一种解决方案，实现协议各层之间的交易。这一需求催生了 2019 年的 Boltz，一座连接多个 Bitcoin 层的桥梁。



## 什么是 Boltz？



[Boltz](https://boltz.Exchange)是一个非托管平台，非常适合任何希望在 Bitcoin 协议不同层之间进行交易的人：




- **on chain**：Bitcoin 的主链平均每 10 分钟确认一次交易，交易费用往往很高，不一定能满足用户的需求；
- **Lightning Network**：Bitcoin 覆盖层可实现即时支付，费用低廉，Bitcoin 可用于日常支付；
- **Liquid Network**：由 Blockstream 创建的 Bitcoin 覆盖层，可实现快速、Confidential Transactions 和使用其他基于 Bitcoin 的金融工具；
- **RootStock**：基于 Bitcoin 协议开发智能合约的解决方案。



![layers](assets/fr/01.webp)



这些不同层面之间的互操作性非常重要，因为它为用户提供了充分利用 Bitcoin 生态系统所提供的一切所需的灵活性。



Boltz 使用原子交换技术。这项技术使比特币可以在两层之间直接交换（例如，用 Exchange 链上的 BTC 交换闪电链上的 BTC），无需信任，也无需中介。这些交换被称为 "原子 "交换，因为它们只能产生两个结果：




- 要么 Exchange 成功，两个参与者有效交换了他们的 BTC；
- 要么 Exchange 失败，要么两个参与者都带着原来的 BTC 离开。



通过这种方式，您可以永久性地自我保管比特币，而 Exchange 并不基于对交易对手的任何信任：Exchange 要么成功要么失败，但任何一方都无法窃取对方的资金。



原子 Exchange 与智能合约 [HTLC](https://planb.network/resources/glossary/htlc)（*Hashed Timelock Contract*）协同工作。在这种类型的 Contract 中，金额被 "锁定 "在一个双向通道中，并引入了时间限制，因此如果交易在一定时间内未完成，余额将归还给存款人。这就是 Boltz 平台使用的机制。



## 您与 Boltz 的首次交流



Boltz 是一个非存款网络平台，不需要您提供任何个人信息。Boltz 拥有简约流畅的 Interface，可让您在一分钟内开始交易。



![boltz](assets/fr/02.webp)



进入平台后，您可以在 Bitcoin 生态系统的不同层之间创建原子交换。



![home](assets/fr/03.webp)



您将看到通过 Boltz 可以交易的最小和最大卫星数（Bitcoin 的最小单位），包括网络费用和 Boltz 征收的 0.1% 至 0.5% 的百分比。



![fees](assets/fr/04.webp)



然后选择您希望制作原子 Exchange 的 Layer，并选择您希望接收比特币的 Layer。



![couches](assets/fr/05.webp)



在本教程中，我们将重点介绍从主 Layer 到 Lightning Network 的原子 Exchange。



您可以通过以下选项为交换机配置基站：




- BTC ；
- Sats.



![unités](assets/fr/06.webp)



完成基本配置后，插入原子 Exchange 的金额，然后创建一个等额的闪电 Invoice，或直接插入您的 LNURL。



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



为安全起见，请检查原子 Exchange 的参数，以导出与 Exchange 相关联的备份密钥。



在**设置**图标上，下载备份密钥并适当保存文件。



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



该文件包含与原子交换相关的 12 个投资组合关键词。



然后点击**创建原子 Exchange** 按钮，并支付指定金额。



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

付款确认后，您将自动收到 Lightning Wallet 上的等值金额。



在**退款**菜单中，找到您的原子 Exchange 历史记录，以确定您希望退款的 Exchange。您还可以导入在其他设备上进行的交换历史记录，例如，使用与这些交换相关的备份密钥文件。



![refund](assets/fr/11.webp)



在**历史**菜单中，您可以点击**备份**按钮，下载与救援密钥相关的更详细的交换历史记录。



![backup](assets/fr/12.webp)



⚠️ 也请不要泄露此文件，因为它包含与您的交易相关的所有信息以及与这些交易相关的备份密钥。



Boltz 通过 Tor 网络上的".ion "链接为您提供高度保密性。在浏览器中激活 Tor 浏览器后，选择 "**洋葱**"菜单，即可实现完全匿名的原子交换。



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Boltz 是一个独特的 Exchange 平台，可实现 Bitcoin 生态系统各层之间的互操作性。