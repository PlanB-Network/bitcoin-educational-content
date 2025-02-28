---
name: Jade Plus - 麻雀
description: 配备麻雀钱包的 Jade Plus 的高级配置
---
![cover](assets/cover.webp)

Jade Plus 是 Blockstream 设计的比特币专用硬件钱包。它是经典 Jade 的继承者，在软件方面进行了改进，提供了更多选项，并重新设计了人体工学，使使用更加直观。新版本拥有一个华丽的 1.9 英寸 LCD 屏幕，色域比前一代产品更广。按钮和菜单导航也进行了优化。

Jade Plus 可以多种方式使用：通过 USB-C 有线连接，在 "*Air-Gap*"模式下使用 micro SD 卡（需要适配器），通过蓝牙，甚至通过集成摄像头交换二维码。这款硬件钱包由电池供电。

它的基本黑色版本售价 149.99 美元起，而 "*创世灰*"或 "*月光银*"版本的价格最多可上涨 20 美元。因此，Jade Plus 是一个有趣的选择，它的先进功能可与 Coldcard Q 或 Passport V2 等高端硬件钱包媲美，但价格却相当低廉，接近中端型号。

![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

在本教程中，我们将在 QR 码模式下设置 Jade Plus 与桌面 Sparrow Wallet 软件的高级配置。这种配置非常适合中级或有经验的用户。如果您正在寻找适合初学者的简单方法，我建议您看看本教程，我们将通过蓝牙连接使用 Jade Plus 和 Green Wallet：

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
## Jade Plus 安全模式

Jade Plus 采用一种基于 "虚拟安全元素 "的安全模式，由 "盲谕 "实现。具体而言，该机制将用户选择的 PIN 码、Jade 上的一个秘密和 Oracle（由 Blockstream 维护的服务器）持有的一个秘密结合起来，创建一个分布在两个实体上的 AES-256 密钥。在启动过程中，ECDH 交换会确保与 Oracle 的通信安全，并对硬件钱包上的恢复短语进行加密。在实际操作中，如果要访问种子来签署交易，就需要访问.NET Framework：


- Jade Plus 设备本身；
- 要使用密码解锁设备 ；
- 还有神谕的秘密

这种方法的主要优点是在硬件层面不存在单点故障，因为如果攻击者访问了你的 Jade，要提取密钥就必须同时破坏 Jade 和甲骨文。这种模式还意味着 Jade Plus 是完全开源的，避免了与使用真正的物理安全元件（例如 Ledger 上使用的元件）相关的限制。

该系统的缺点是，Jade Plus 的使用取决于 Blockstream 维护的甲骨文。如果甲骨文无法访问，就无法直接使用 PIN 码使用硬件钱包。不过，这并不意味着您的比特币丢失了，因为您仍然可以使用恢复短语找回比特币，您可以在 "*无状态*"模式下在 Jade Plus 中输入恢复短语。为了避免这种依赖性，你也可以配置和管理自己的 Oracle 服务器。

另一种管理种子的方法是不在 Jade Plus 上注册。在这种情况下，翠玉将只成为一个签名设备。在初始化过程中，除了通常将恢复短语保存为文字外，您还可以将其保存为手工生成的二维码。这样，每次使用钱包时，就可以使用 Jade 的摄像头导入种子。对于高级用户来说，这可能是一个有趣的选择，这取决于你的安全策略，但你需要小心保存种子并保护它，因为即使作为二维码，它也会让任何人盗取你的资金。我们将在本教程中介绍这个选项，但它并不是强制性的。

## Jade Plus 开箱

当您收到 Jade Plus 时，请检查包装盒和封条是否完好，以确保您的包裹没有被打开过。

![JADE-PLUS-SPARROW](assets/fr/02.webp)

盒子里有 ：


- Le Jade Plus；
- USB-C 电缆；
- 以单词或 "*CompactSeedQR*"的形式记录记忆短语的卡片；
- 一些使用说明 ；
- 一条绳索
- 一些贴纸

![JADE-PLUS-SPARROW](assets/fr/03.webp)

该设备有 4 个导航按钮：


- 右下角的按钮可以打开翡翠；
- 设备正面的大按钮用于选择项目；
- 顶部的两个小按钮可以让您向左和向右导航；
- 您还可以同时点击设备顶部的两个按钮来选择项目。

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## 设置新的比特币钱包

点击开始按钮。

![JADE-PLUS-SPARROW](assets/fr/05.webp)

点击 "*设置翡翠*"。

![JADE-PLUS-SPARROW](assets/fr/06.webp)

选择 "高级设置*"。

![Image](assets/fr/07.webp)

然后点击 "*创建新钱包*"生成新种子。您可以选择 12 个字或 24 个字的记忆短语。两种选择的钱包安全性是相同的，因此选择最简单的保存选项（即 12 个单词）可能更方便。

![Image](assets/fr/08.webp)

点击 "*继续*"按钮，显示新的恢复短语。

![Image](assets/fr/09.webp)

您的 Jade Plus 会显示 12 个字的记忆短语。 **这个口诀可以让你完全无限制地使用你所有的比特币。任何拥有该短语的人都可以盗取您的资金，即使没有实际接触到您的 Jade Plus。如果您的 Jade 丢失、被盗或损坏，这 12 个字的短语可以恢复您对比特币的访问。因此，小心保存并将其存放在安全的地方非常重要。

您可以在包装盒内提供的纸板上书写，或者为了提高安全性，我建议您将其刻在不锈钢底座上，以防火灾、水灾或倒塌。

![Image](assets/fr/10.webp)

有关保存和管理记忆短语的正确方法的更多信息，我强烈推荐大家阅读另一篇教程，尤其是初学者：

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
当然，你绝对不能在互联网上分享这些文字，就像我在本教程中所做的那样。本示例作品集将仅在 Testnet 上使用，并将在教程结束时删除。

点击屏幕右侧的箭头，显示以下单词。

![Image](assets/fr/11.webp)

保存短语后，Jade Plus 会要求您确认。使用设备顶部的按钮按照顺序选择正确的单词，然后点击中央按钮进入下一个单词。

![Image](assets/fr/12.webp)

然后您有两个选择。如介绍中所述，您可以选择将种子直接保存在设备上，然后使用 Blockstream 的 "*虚拟安全元素*"保护系统访问您的钱包（选项 1）；或者将种子保存为二维码，每次使用时扫描一下（选项 2）。

选项 1 请选择 "*否*"，选项 2 请选择 "*是*"。

![Image](assets/fr/13.webp)

### 选项 1：QR 密码解锁

如果选择了选项 1（CompactSeedQR："*No*"），则将直接进入连接方式选择。在本教程中，我们希望通过二维码交换在 Air-Gap 模式下使用设备，因此请选择 "*QR*"。

![Image](assets/fr/27.webp)

点击 "*继续*"。

![Image](assets/fr/28.webp)

PIN 码用于解锁您的玉石，并防止未经授权的物理访问。该 PIN 码不参与钱包加密密钥的生成。因此，即使无法获得 PIN 码，只要拥有 12 个字的记忆短语，就可以重新获得比特币。我们建议您选择一个尽可能随机的 PIN 码。此外，请确保将该密码保存在与您的 Jade 不同的地方，如密码管理器中。

在 Jade 上选择一个 6 位数的 PIN 码，使用左右按钮滚动数字，使用中间按钮确认每个数字。

![Image](assets/fr/29.webp)

再次确认 PIN 码。

![Image](assets/fr/30.webp)

如前言所述，您的种子将加密存储在 Jade Plus 中。要解密种子，您必须提供.NET 文件：


- 有效的 PIN 码（我们刚刚设置的） ；
- Blockstream 维护的神谕秘密。

在本高级教程中，我们将使用 Sparrow Wallet 管理我们的比特币钱包。不过，与 Blockstream 的绿色钱包软件不同，Sparrow 无法访问 Blockstream 服务器上的甲骨文。因此，每次解锁 Jade Plus 时，我们都将使用 Blockstream 网站来检索甲骨文秘密。

访问 https://jadefw.blockstream.com/pinqr/index.html

点击 "*开始 QR 解锁*"。

![Image](assets/fr/31.webp)

点击 "*完成*"，因为您已经在 Jade Plus 上选择了密码。

![Image](assets/fr/32.webp)

使用电脑摄像头扫描 Jade 屏幕上显示的 QR 码。

![Image](assets/fr/33.webp)

在 Jade 上确认，进入下一个屏幕。

![Image](assets/fr/34.webp)

扫描网站上的二维码，获取神谕的秘密。

![Image](assets/fr/35.webp)

现在您的投资组合已经创建，您可以继续下一步，跳过 "*选项 2：CompactSeedQR*"小节。

![Image](assets/fr/36.webp)

每次启动时，点击 "*QR 模式*"。

![Image](assets/fr/37.webp)

选择 "*QR PIN 解锁*"。

![Image](assets/fr/38.webp)

输入您的 PIN 码。

![Image](assets/fr/39.webp)

然后访问 [Blockstream 网站](https://jadefw.blockstream.com/pinqr/qrpin.html) 与甲骨文交换二维码。

![Image](assets/fr/40.webp)

您的翡翠现在已解锁。

![Image](assets/fr/41.webp)

### 方案 2：CompactSeedQR

如果您选择了选项 2（CompactSeedQR："*Yes*"），请再次点击 "*Yes*"。

![Image](assets/fr/14.webp)

点击 "*开始*"。

![Image](assets/fr/15.webp)

您可以使用 Jade Plus 包装盒中提供的 QR 码底座。根据您选择的是 12 个字还是 24 个字的句子，选择相应的方框。您还可以[从 Blockstream 网站打印模板](https://help.blockstream.com/hc/article_attachments/41928319071769)。

您的 Jade Plus 将显示二维码的每个区域。

![Image](assets/fr/16.webp)

用笔在方格内涂色，将种子复制成 QR 码。要准确无误，以确保 Jade Plus 相机稍后可以扫描。使用箭头进入下一个区域。

![Image](assets/fr/17.webp)

完成后，点击 "*完成*"。

![Image](assets/fr/18.webp)

用 Jade Plus 扫描手工制作的 QR 码，检查其有效性。

![Image](assets/fr/19.webp)

如果纸张备份正确，请单击 "*继续*"。

![Image](assets/fr/20.webp)

在本教程中，我们将使用完全基于二维码扫描的连接模式，因此请选择 "*QR*"。

![Image](assets/fr/21.webp)

您还可以选择在 CompactSeedQR 备份之外添加一个 PIN 码，如选项 1。这提供了两种访问钱包的方式：通过 PIN 码和 Blockstream 的 "虚拟安全元素 "系统，或通过 CompactSeedQR。

如果选择双 PIN 码选项，请选择 "*PIN*"，然后按照选项 1 的相同步骤设置 PIN 码。

如果只想继续使用 CompactSeedQR，请选择 "*SeedQR*"。

![Image](assets/fr/22.webp)

现在，您的投资组合已经创建，可以进入下一个步骤了。

![Image](assets/fr/23.webp)

每次启动时，点击 "*QR 模式*"按钮，然后点击 "*扫描 SeedQR*"。

![Image](assets/fr/24.webp)

使用设备的摄像头将保存的种子扫描为 QR 码。

![Image](assets/fr/25.webp)

您的翡翠现在已解锁。

![Image](assets/fr/26.webp)

## 添加 BIP39 密码

BIP39 密码短语是您可以自由选择的密码，它被添加到您的记忆短语中，以加强钱包的安全性。启用该功能后，访问比特币钱包需要同时使用记忆短语和口令。两者缺一不可，否则就不可能找回钱包。

在翡翠增强版上配置该选项之前，强烈建议您阅读本文，以充分了解口令的理论操作，避免可能导致比特币丢失的错误：

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
在 Jade 仍然锁定的情况下（密码只能在设备未解锁时输入），访问 "*选项*"菜单。

![Image](assets/fr/42.webp)

选择 "*BIP39 密码*"。

![Image](assets/fr/43.webp)

在 "*频率*"选项中，你可以选择 Jade Plus 是否会在每次启动时都要求你输入密码：


- "禁用*"禁止使用口令；
- "仅限下次登录*"将要求您返回此菜单，以便在下次启动时激活对密码的请求。该选项允许您不透露密码的使用情况；
- "始终询问*"会导致 Jade 在每次启动时系统地询问您的口令，从而暴露您的钱包受口令保护。

根据您的安全策略选择选项。我个人选择 "*始终询问*"作为示例。

![Image](assets/fr/44.webp)

然后，您可以选择两种输入密码的方法：


- "手动*：虚拟键盘可让您逐个字符输入字母（大写和小写）、数字和符号。这是所有硬件钱包的标准方法；
- "*WordList*"：Blockstream 为 Jade 设计的特定方法，可加快口令输入速度并增加其熵。在输入过程中，系统会建议使用 BIP39 列表中的单词，使解锁更加容易。该方法通过连接所选单词自动生成句子，并用空格分隔（例如："abandon ability able"）。

我个人建议您使用第一种方法，因为这是所有其他投资组合支持工具的标准。

![Image](assets/fr/45.webp)

然后，您可以返回主屏幕，像往常一样使用 PIN 码或 CompactSeedQR（如上图所示）解锁钱包。然后会要求您输入密码。

![Image](assets/fr/46.webp)

在 Jade 键盘上输入，并确保在物理介质（纸质或金属）上做一个或多个备份。在示例中，我使用了一个非常弱的口令，但你需要选择一个强大的随机口令，包括所有类型的字符，并且足够长（就像一个强大的密码）。

![Image](assets/fr/47.webp)

如果密码有效，请确认。

![Image](assets/fr/48.webp)

请注意，BIP39 密码对大小写和错别字敏感。如果您输入的口令与最初配置的口令略有不同，Jade 不会报错，但会推导出另一组加密密钥，与您最初配置的密钥不同。

因此，在配置时一定要记下你的主密钥指纹，它可以在屏幕右下角找到。例如，我的密码是 "PBN"，我的主密钥指纹是 "3AD1AE65"。

![Image](assets/fr/49.webp)

每次使用密码解锁 Jade 时，请检查指纹是否与配置时输入的指纹相同。如果是，说明你的密码是正确的，你访问的是正确的比特币钱包。如果不一样，说明你进入了错误的钱包，需要重新尝试，注意不要输入错误。

在您收到钱包中的第一枚比特币之前，**我强烈建议您执行一次清空恢复测试**。记下一些参考信息，例如您的 xpub 或第一个接收地址，然后在翡翠增强版上删除您的钱包，此时钱包还是空的（"选项 -> 设备 -> 出厂重置"）。然后尝试使用纸质备份的记忆短语和任何口令恢复钱包。检查还原后生成的 cookie 信息是否与您最初写下的信息一致。如果吻合，您就可以放心，您的纸质备份是可靠的。要了解有关如何进行测试恢复的更多信息，请参阅本教程：

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## 在麻雀钱包上配置钱包

在本教程中，我将使用麻雀钱包介绍 Jade Plus 的高级用法。不过，这种硬件钱包与许多其他程序兼容，如 Liana、Nunchuk、Specter、Green 和 Keeper。这些兼容性在连接方面各不相同：USB、蓝牙或 QR 码（详见简介中的表格）。

如果还没有下载 Sparrow Wallet（麻雀钱包）并将其安装到电脑上，请从官方网站下载](https://sparrowwallet.com/)。

![Image](assets/fr/50.webp)

安装前请务必检查软件的真实性和完整性。如果您不知道如何操作，请参考本教程：

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
打开麻雀钱包后，点击 "*文件*"标签，然后点击 "*新建钱包*"。

![Image](assets/fr/51.webp)

为钱包命名，然后点击 "*创建钱包*"。

![Image](assets/fr/52.webp)

选择 "*空格硬件钱包*"。

![Image](assets/fr/53.webp)

点击 "*Jade*"选项旁边的 "*Scan...*"。

![Image](assets/fr/54.webp)

解锁翡翠增强版，如果正在使用，请输入密码。然后进入 "*选项*"菜单，选择 "*钱包*"，点击 "*导出 Xpub*"。

![Image](assets/fr/55.webp)

您的 Jade 将通过多个 QR 码显示您的 Keystore。使用 Sparrow 在机器上扫描它们。

![Image](assets/fr/56.webp)

现在你应该能看到你的 xpub 和主密钥指纹，它们应该与 Jade Plus 上的指纹一致。点击 "*应用*"。

![Image](assets/fr/57.webp)

设置一个强大的密码，以确保安全访问您的麻雀钱包。该密码将保护您的公钥、地址、标签和交易历史记录，防止未经授权的访问。最好将密码保存在密码管理器中，以免忘记。

![Image](assets/fr/58.webp)

您的投资组合已在 Sparrow 上正确配置。

![Image](assets/fr/59.webp)

## 接收比特币

现在，您的 Jade Plus 已经配置好了，您可以在新的比特币钱包上接收第一个卫星数据了。为此，请在 Sparrow 上点击 "*接收*"菜单。

![Image](assets/fr/60.webp)

Sparrow 将显示您作品集中的第一个空白接待地址。

![Image](assets/fr/61.webp)

在使用之前，我们先在 Jade Plus 屏幕上检查一下，确保它属于我们的比特币钱包。在翡翠上点击 "*扫描二维码*"，然后扫描 Sparrow 上显示的地址的二维码。

![Image](assets/fr/62.webp)

检查 Jade 屏幕上显示的地址是否与 Sparrow Wallet 上显示的地址一致。如果一致，请点击复选标记继续。

![Image](assets/fr/63.webp)

然后，您的硬件钱包会确认该地址是您钱包的一部分，并确认它持有相关的私钥。

![Image](assets/fr/64.webp)

如果您的 Jade 验证了该地址，您就可以用它来接收比特币了。当交易在网络上广播时，它就会出现在 Sparrow 上。等到收到足够多的确认信息后，交易才算完成。

![Image](assets/fr/65.webp)

## 发送比特币

现在您的钱包里已经有了一些卫星，您还可以发送一些卫星。为此，请点击 "*UTXOs*"菜单。

![Image](assets/fr/66.webp)

选择希望用作此交易输入的UTXO，然后点击 "*发送所选*"。

![Image](assets/fr/67.webp)

输入收件人地址、提醒您交易目的的标签以及您希望发送到该地址的金额。

![Image](assets/fr/68.webp)

根据当前市场情况调整收费率，然后点击 "*创建交易*"。

![Image](assets/fr/69.webp)

检查所有交易参数是否正确，然后点击 "*最终完成交易以供签署*"。

![Image](assets/fr/70.webp)

点击 "*显示 QR*"来显示 PSBT（*部分签名比特币交易*）。麻雀已经建立了交易，但还缺少签名来解锁输入中使用的比特币。这些签名只能由 Jade Plus 来完成，因为 Jade Plus 承载着你的种子，可以获取签署交易所需的私钥。

![Image](assets/fr/71.webp)

在 Jade Plus 上点击 "*扫描 QR*"，扫描 Sparrow 上显示的 PSBT。

![Image](assets/fr/72.webp)

确认送货地址和发送金额正确无误，然后点击箭头进行验证。

![Image](assets/fr/73.webp)

确保费用金额是您选择的金额，然后点击界面左上角的"√"图标，签署交易。

![Image](assets/fr/74.webp)

在 Sparrow Wallet 上，点击 "*扫描二维码*"并扫描 Jade 上显示的二维码。

![Image](assets/fr/75.webp)

您签署的交易现在可以在比特币网络上广播，并被矿工纳入一个区块。如果一切正常，请点击 "*广播交易*"。

![Image](assets/fr/76.webp)

您的交易已被广播，正在等待确认。

![Image](assets/fr/77.webp)

恭喜您，现在您已经知道如何在 QR 模式下设置和使用 Jade Plus 了。如果您觉得本教程有用，请在下方留下绿色拇指，我将不胜感激。欢迎在您的社交网络上分享本文。感谢您的分享！

要想更进一步，我推荐您阅读有关 Jade Plus 的另一篇教程，我们将通过蓝牙与 Green 手机应用进行配置：

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0