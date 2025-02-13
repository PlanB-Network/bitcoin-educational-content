---
name: Jade Plus - 绿色
description: 使用绿色软件轻松配置 Jade Plus
---
![cover](assets/cover.webp)

Jade Plus 是 Blockstream 设计的比特币专用硬件钱包。它是经典 Jade 的继承者，在软件方面进行了改进，提供了更多选项，并重新设计了人体工学，使使用更加直观。新版本拥有一个华丽的 1.9 英寸 LCD 屏幕，色域比前一代产品更广。按钮和菜单导航也进行了优化。

Jade Plus 可以多种方式使用：通过 USB-C 有线连接，在 "*Air-Gap*"模式下使用 micro SD 卡（需要适配器），通过蓝牙，甚至通过集成摄像头交换二维码。这款硬件钱包由电池供电。

它的基本黑色版本售价 149.99 美元起，而 "*创世灰*"或 "*月光银*"版本的价格最多可上涨 20 美元。因此，Jade Plus 是一个有趣的选择，它的先进功能可与 Coldcard Q 或 Passport V2 等高端硬件钱包媲美，但价格却相当低廉，接近中端型号。

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus 与大多数投资组合管理软件兼容。以下是撰写本文时（2025 年 1 月）的兼容性摘要：

| 台式机 | 手机 | USB | 蓝牙 | QR | JadeLink | 管理软件

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 | 🔴

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴

| 麻雀 | | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢

Nunchuk | | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢

| 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢

| BlueWallet | | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢



| Keeper | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 | 🔴

在本教程中，我们将通过蓝牙连接设置并使用 Jade Plus 与 Blockstream 的 Green Wallet 移动应用程序。这种设置非常适合初学者。如果您正在寻找更高级的方法，我建议您看看本教程，我们将在二维码模式下使用 Jade Plus 和麻雀钱包：

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
## Jade Plus 安全模式

Jade Plus 采用一种基于 "虚拟安全元素 "的安全模式，由 "盲谕 "实现。具体而言，该机制将用户选择的 PIN 码、Jade 上的一个秘密和 Oracle（由 Blockstream 维护的服务器）持有的一个秘密结合起来，创建一个分布在两个实体上的 AES-256 密钥。在启动过程中，ECDH 交换会确保与 Oracle 的通信安全，并对硬件钱包上的恢复短语进行加密。在实际操作中，如果要访问种子来签署交易，就需要访问.NET Framework：


- Jade Plus 设备本身；
- 要使用密码解锁设备 ；
- 还有神谕的秘密

这种方法的主要优点是在硬件层面不存在单点故障，因为如果攻击者访问了你的 Jade，要提取密钥就必须同时破坏 Jade 和甲骨文。这种模式还意味着 Jade Plus 是完全开源的，避免了与使用真正的物理安全元件（例如 Ledger 上使用的元件）相关的限制。

该系统的缺点是，Jade Plus 的使用取决于 Blockstream 维护的甲骨文。如果甲骨文无法访问，就无法直接使用 PIN 码使用硬件钱包。不过，这并不意味着您的比特币丢失了，因为您仍然可以使用恢复短语找回比特币，您可以在 "*无状态*"模式下在 Jade Plus 中输入恢复短语。为了避免这种依赖性，你也可以配置和管理自己的 Oracle 服务器。

## Jade Plus 开箱

当您收到 Jade Plus 时，请检查包装盒和封条是否完好，以确保您的包裹没有被打开过。

![JADE-PLUS-GREEN](assets/fr/02.webp)

盒子里有 ：


- Le Jade Plus；
- USB-C 电缆；
- 以单词或 "*CompactSeedQR*"的形式记录记忆短语的卡片；
- 一些使用说明 ；
- 一条绳索
- 一些贴纸

![JADE-PLUS-GREEN](assets/fr/03.webp)

该设备有 4 个导航按钮：


- 右下角的按钮可以打开翡翠；
- 设备正面的大按钮用于选择项目；
- 顶部的两个小按钮可以让您向左和向右导航；
- 您还可以同时点击设备顶部的两个按钮来选择项目。

![JADE-PLUS-GREEN](assets/fr/04.webp)

## 设置新的比特币钱包

点击开始按钮。

![JADE-PLUS-GREEN](assets/fr/05.webp)

点击 "*设置翡翠*"。

![JADE-PLUS-GREEN](assets/fr/06.webp)

选择 "开始设置"。*Advanced Setup*（*高级设置*）"选项做同样的事情，但可以访问高级设置。

![JADE-PLUS-GREEN](assets/fr/07.webp)

然后点击 "*创建新钱包*"生成新种子。

![JADE-PLUS-GREEN](assets/fr/08.webp)

点击 "*继续*"按钮，显示新的恢复短语。

![JADE-PLUS-GREEN](assets/fr/09.webp)

您的 Jade Plus 会显示 12 个字的记忆短语。 **这个口诀可以让你完全无限制地使用你所有的比特币。任何拥有该短语的人都可以盗取您的资金，即使没有实际接触到您的 Jade Plus。如果您的 Jade 丢失、被盗或损坏，这 12 个字的短语可以恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。

您可以在包装盒内提供的纸板上书写，或者为了提高安全性，我建议您将其刻在不锈钢底座上，以防火灾、水灾或倒塌。

![JADE-PLUS-GREEN](assets/fr/10.webp)

有关保存和管理记忆短语的正确方法的更多信息，我强烈推荐大家阅读另一篇教程，尤其是初学者：

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
***很明显，你绝对不能在互联网上分享这些文字，就像我在本教程中所做的那样。本作品集样本将仅在 Testnet 上使用，并将在教程结束时删除。

点击屏幕右侧的箭头，显示以下单词。

![JADE-PLUS-GREEN](assets/fr/11.webp)

保存短语后，Jade Plus 会要求您确认。使用设备顶部的按钮按照顺序选择正确的单词，然后点击中央按钮进入下一个单词。

![JADE-PLUS-GREEN](assets/fr/12.webp)

## 将 Jade Plus 连接到绿色钱包

在本教程中，我们将使用 Green Wallet 应用程序来管理 Jade Plus 上托管的钱包。这种方法特别适合初学者。如果你想更详细地管理比特币钱包，也可以使用麻雀钱包，我们将在另一篇教程中介绍：

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
有关安装和设置 Blockstream Green 应用程序的说明，请参阅本教程的第一部分：

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143
进入 Blockstream Green 应用程序后，点击 "*配置新投资组合*"按钮。

![JADE-PLUS-GREEN](assets/fr/13.webp)

选择 "*硬件钱包*"。

![JADE-PLUS-GREEN](assets/fr/14.webp)

激活智能手机上的蓝牙，然后点击 "*连接您的 Jade*"按钮。

![JADE-PLUS-GREEN](assets/fr/15.webp)

授权 Green 应用程序访问蓝牙连接。

![JADE-PLUS-GREEN](assets/fr/16.webp)

该应用程序正在查找您的 Jade Plus。

![JADE-PLUS-GREEN](assets/fr/17.webp)

在 Jade Plus 上，点击 "*蓝牙*"菜单。

![JADE-PLUS-GREEN](assets/fr/18.webp)

在绿色应用程序中选择您的设备。

![JADE-PLUS-GREEN](assets/fr/19.webp)

在 Jade Plus 上确认配对密码。

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green 为您提供一个测试，以确保您的翡翠是真品。点击按钮进行测试。

![JADE-PLUS-GREEN](assets/fr/21.webp)

在 Jade 上确认。

![JADE-PLUS-GREEN](assets/fr/22.webp)

绿色表示您的设备是正品。

![JADE-PLUS-GREEN](assets/fr/23.webp)

## 设置 PIN 码

点击 "*继续*"按钮，选择翡翠的 PIN 码。

![JADE-PLUS-GREEN](assets/fr/24.webp)

PIN 码可以解锁您的翡翠。因此，它可以防止未经授权的物理访问。该 PIN 码不参与钱包加密密钥的生成。因此，即使无法获得 PIN 码，只要拥有 12 个字的记忆短语，就可以重新获得比特币。我们建议选择一个尽可能随机的 PIN 码。并确保将该密码保存在与您的 Jade 存储位置不同的地方（如密码管理器中）。

选择 Jade 上的 6 位数 PIN 码，使用左右按钮滚动数字，使用中间按钮确认数字的输入。

![JADE-PLUS-GREEN](assets/fr/25.webp)

再次确认 PIN 码。

![JADE-PLUS-GREEN](assets/fr/26.webp)

您的比特币钱包已经创建。

![JADE-PLUS-GREEN](assets/fr/27.webp)

## 创建比特币账户

现在，您必须在您的投资组合中创建一个账户。点击 "*创建账户*"按钮。

![JADE-PLUS-GREEN](assets/fr/28.webp)

如果想创建经典的单一密码组合，请选择 "*标准*"。

![JADE-PLUS-GREEN](assets/fr/29.webp)

有关 "*2FA*"选项的更多信息，请参阅本教程：

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9
您的账户已创建。

![JADE-PLUS-GREEN](assets/fr/30.webp)

如果您希望个性化您的绿色投资组合，请点击右上方的三个小圆点。

![JADE-PLUS-GREEN](assets/fr/31.webp)

通过 "*Rename*"（重命名）选项，您可以自定义投资组合的名称，这对在同一应用程序中管理多个投资组合特别有用。通过 "*单位*"菜单可以更改投资组合的基本单位。例如，您可以选择以卫星币而不是比特币显示。最后，"*参数*"菜单可以让你访问其他选项。例如，您可以在这里找到您的扩展公钥及其描述符，如果您打算从您的 Jade 中设置一个仅用于手表的钱包，这将非常有用。

![JADE-PLUS-GREEN](assets/fr/32.webp)

要在关闭 Jade 后重新连接，请按设备底部的开/关按钮。在绿色应用程序中，从主页选择您的设备：

![JADE-PLUS-GREEN](assets/fr/33.webp)

然后输入 Jade 上的 PIN 码，就可以再次连接了。

![JADE-PLUS-GREEN](assets/fr/34.webp)

您的 Jade 通过 Blockstream 的 "虚拟安全元件 "解锁（见本教程第一部分）。这需要与 Green 应用程序进行蓝牙连接。如果在解锁过程中遇到蓝牙连接问题，请尝试将两台设备分离并重新连接。如果问题仍然存在，您仍然可以通过选择 "*QR 扫描*"选项并按照[Blockstream 网站](https://jadefw.blockstream.com/pinqr/index.html)上的说明对您的翡翠进行解锁。

在您收到钱包中的第一枚比特币之前，**我强烈建议您进行一次清空恢复测试**。记下一些参考信息，例如您的 xpub 或第一个接收地址，然后在绿色应用程序和翡翠增强版上删除您的钱包，此时钱包还是空的（"选项 -> 设备 -> 出厂重置"）。然后尝试使用记忆短语的纸质备份恢复钱包。检查还原后生成的 cookie 信息是否与您最初写下的信息一致。如果吻合，您就可以放心，您的纸质备份是可靠的。要了解有关如何进行测试恢复的更多信息，请参阅本教程 ：

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## 接收比特币

现在，您的比特币钱包已经设置好了，您已经准备好接收您的第一枚比特币了！只需点击绿色应用程序上的 "*接收*"按钮即可。

![JADE-PLUS-GREEN](assets/fr/35.webp)

绿色显示的是一个接收地址，但在使用之前，有必要在翡翠上对其进行检查，以确认它确实属于我们的产品组合。为此，请点击 "*在设备上验证*"按钮。

![JADE-PLUS-GREEN](assets/fr/36.webp)

检查 Jade 上的地址是否与 Green 上的地址相同，然后点击按钮确认。

![JADE-PLUS-GREEN](assets/fr/37.webp)

现在您可以与付款人共享地址，在您的钱包中接收比特币。交易在网络上广播后，就会出现在您的钱包中。等到收到足够多的确认信息后，交易才算完成。

![JADE-PLUS-GREEN](assets/fr/38.webp)

## 发送比特币

钱包里有了比特币，现在还可以发送比特币。点击 "*发送*"。

![JADE-PLUS-GREEN](assets/fr/39.webp)

在下一页，输入收件人地址。您可以手动输入或扫描二维码。

![JADE-PLUS-GREEN](assets/fr/40.webp)

选择付款金额。

![JADE-PLUS-GREEN](assets/fr/41.webp)

在屏幕底部，您可以选择该交易的费率。您可以选择按照应用程序的建议或自定义费用。与其他待处理交易相比，费用越高，交易处理速度越快。有关费用市场信息，请访问 [Mempool.space](https://mempool.space/) 中的 "*交易费用*"部分。

![JADE-PLUS-GREEN](assets/fr/42.webp)

点击 "*下一步*"进入交易摘要屏幕。检查地址、金额和费用是否正确。

![JADE-PLUS-GREEN](assets/fr/43.webp)

如果一切顺利，将屏幕底部的绿色按钮向右滑动，即可在比特币网络上签署并广播交易。

![JADE-PLUS-GREEN](assets/fr/44.webp)

现在会要求您在 Jade 上确认交易。

![JADE-PLUS-GREEN](assets/fr/45.webp)

确保收件人地址正确。点击复选标记确认。

![JADE-PLUS-GREEN](assets/fr/46.webp)

检查收费金额是否正确，然后验证。

![JADE-PLUS-GREEN](assets/fr/47.webp)

您的交易已经签署，并从绿色通道播出。

![JADE-PLUS-GREEN](assets/fr/48.webp)

恭喜您，现在您已经知道如何通过蓝牙连接设置和使用 Jade Plus 与 Blockstream Green 移动应用程序。如果您觉得本教程有用，请在下方留下绿色拇指。欢迎在您的社交网络上分享本文。感谢您的分享！

要想更进一步，我向您推荐这篇关于 Jade Plus 的教程，我们将在 QR 模式下使用麻雀钱包软件对其进行配置。您还将学习如何使用硬件钱包的高级设置：

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262