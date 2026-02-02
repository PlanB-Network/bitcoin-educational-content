---
name: Satochip x SeedSigner
description: 如何在 SeedSigner 上使用 Satochip？
---

![cover](assets/cover.webp)



*感谢 [Crypto Guide]（https://www.youtube.com/@CryptoGuide/）提供的支持智能卡的 SeedSigner 固件 fork，我们将在本教程中使用该固件。



---

Satochip 是一种 wallet 智能卡格式硬件，具有最高安全标准之一的 EAL6+ 认证安全元素。它由比利时同名公司 Satochip 设计和生产。



Satochip 的售价约为 25 欧元，因其物美价廉而在竞争中脱颖而出。由于采用了安全芯片，它可以抵御物理攻击。更重要的是，它的小程序源代码完全开源，采用*AGPLv3*授权。



另一方面，它的格式也造成了某些功能上的限制。Satochip 的主要缺点是没有集成屏幕：因此，用户必须盲目地签署交易，完全依赖计算机的显示屏。



为了克服这一弱点，一种特别有趣的配置是将其与种子签收器结合使用。在这种设置中，计算机与 Satochip 之间不再直接通信，而是通过计算机与 SeedSigner 之间的二维码交换进行通信。然后，SeedSigner 充当信任屏幕：显示要签名的信息，而签名本身则由 Satochip 执行。与传统的 SeedSigner 使用方式（甚至与 Seedkeeper 结合使用）不同，seed 从不加载到 SeedSigner 中。这样，SeedSigner 就成了 Satochip 的屏幕，消除了与盲签相关的风险。



如果我们反过来看这个问题，将 SeedSigner 与 Satochip 结合使用，就能弥补 SeedSigner 的一个重大缺陷：在 secure element 中存储和使用 seed 的能力。



我认为，与传统的硬件钱包相比，这种配置有几个优势：




- Satochip 的价格约为 25 欧元，由于小程序是开源的，你可以在空白的智能卡上自行安装。然后，您还需要加上 SeedSigner 组件和读取智能卡的扩展功能的费用：根据您购买硬件的地点，总费用应该在 70 欧元到 100 欧元之间。
- 设置中涉及的所有软件都是开源的：SeedSigner 固件和 Satochip 小程序。
- 您将受益于经过认证的安全要素。
- 配置可以完全 DIY 进行，无需使用明确用于 Bitcoin 的硬件，这可以提供一种似是而非的推诿形式，抵御某些外部威胁（包括国家压力）。如果您所在的地区限制或不可能使用商用硬件钱包，这也是一个有趣的解决方案。




## 1.所需材料



要进行此设置，您需要以下物品：




- 经典种子签约者所需的常规设备 ：
 - 带 GPIO 引脚的 Raspberry Pi Zero、
 - 1.3 英寸 Waveshare 屏幕、
 - 兼容的相机、
 - 一张 microSD 卡。



![Image](assets/fr/01.webp)





- SeedSigner扩展套件，可[从Satochip官方商店](https://satochip.io/product/seedsigner-extension-kit/)购买，它可以让你直接从SeedSigner读写智能卡。另一种方法是使用 [外部智能卡阅读器](https://satochip.io/product/chip-card-reader/)，它可以通过电缆连接到 Raspberry Pi 上的 Micro-USB 端口。不过，我还没有亲自测试过这种解决方案；
- [一张Satochip](https://satochip.io/product/satochip/)，或者一张安装Satochip小程序的[空白智能卡](https://satochip.io/product/card-for-diy-project/)（Satochip出售的扩展套件已经包含一张空白智能卡）。Satochip的扩展工具包还支持[SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/)格式。因此，如果你愿意，可以选择这种格式。



![Image](assets/fr/02.webp)



有关组装 SeedSigner 所需设备的更多详情，请参阅本教程的第一部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2.安装固件



要在 Satochip 上使用 SeedSigner，您需要安装一个不同于原始 SeedSigner 的固件，以支持智能卡读取。为此，[我建议使用 "**3rdIteration**"的 fork](https://github.com/3rdIteration/seedsigner)。下载[最新版本的映像](https://github.com/3rdIteration/seedsigner/releases) (`.zip`)，与你使用的 Raspberry Pi 型号相对应。



![Image](assets/fr/03.webp)



如果还没有，请下载 [Balena Etcher] 软件 (https://etcher.balena.io/)，然后按以下步骤操作：




- 将 microSD 卡插入电脑；
- 启动蚀刻机 ；
- 选择刚刚下载的 `.zip` 文件；
- 选择 microSD 卡作为目标；
- 点击 "Flash!"。



![Image](assets/fr/04.webp)



等待该过程完成：您的 microSD 现在可以使用了。现在您可以继续组装设备。



有关固件安装和软件验证的更多详情（我强烈建议您采取这一步骤），请参阅以下教程：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3.组装智能卡读卡器



首先在 Raspberry Pi Zero 上安装摄像头，小心地将其插入摄像头针脚，并用黑色卡扣锁紧。然后将 Pi 放在机箱底部，确保将端口对准相应的开口。



![Image](assets/fr/05.webp)



然后将智能卡读写器连接到 Raspberry Pi Zero 的 GPIO 引脚上。



![Image](assets/fr/06.webp)



将塑料盖滑到智能卡读卡器上，直到正确定位。



![Image](assets/fr/07.webp)



然后将屏幕添加到扩展的 GPIO 引脚上。



![Image](assets/fr/08.webp)



最后，将装有固件的 microSD 卡插入 Raspberry Pi Zero 的侧接口。



![Image](assets/fr/09.webp)



现在，您可以通过 Raspberry Pi Zero 的 Micro-USB 端口或扩展的 USB-C 端口连接 SeedSigner。两种方式都可以。等待几秒钟启动后，你会看到欢迎屏幕出现。



![Image](assets/fr/10.webp)



有关 SeedSigner 初始设置的更多详情，我建议您参考以下教程的第 4 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4.使用 Satochip 小程序闪存智能卡（可选）



如果您已经拥有了 Satochip，可以跳过这一步，直接进入第 4 步。在本节中，我们将介绍如何在空白智能卡上安装Satochip小程序（DIY方法）。小程序只是运行在智能卡上的一个小程序，它能让我们管理特定的功能。



要开始使用，请打开 SeedSigner 上的 "工具 > 智能卡工具 "菜单。



![Image](assets/fr/11.webp)



然后选择 "DIY 工具 > 安装 Applet"。



![Image](assets/fr/12.webp)



将智能卡插入 SeedSigner 阅读器，芯片朝下，然后选择 "Satochip "小程序。



![Image](assets/fr/13.webp)



安装过程可能需要几十秒，请耐心等待。



![Image](assets/fr/14.webp)



小程序安装成功后，就可以进入步骤 4。



![Image](assets/fr/15.webp)




## 5.创建和保存 seed



### 5.1.生成 seed



现在，您的所有硬件和软件都已正常运行，可以开始创建 Bitcoin 作品集了。为此，请插入 SeedSigner，然后像使用传统 SeedSigner 一样，通过掷骰子或拍照来制作 generate 组合：




- 转到 "工具 > 摄像头/掷骰子 "菜单；
- 然后根据所选方法进行熵生成；
- 最后，在物理介质上备份 seed，并仔细检查备份。



![Image](assets/fr/16.webp)



如果您想了解该步骤的详情，请参阅本教程的第 5 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2.在种子管理器上保存 seed



一旦生成 seed，这是它在 SeedSigner 的 RAM 中唯一的停留时间。就我而言，我想把它保存在[Seedkeeper](https://satochip.io/product/seedkeeper/)上，这是另一个 Satochip 产品，专门用于存储秘密。如果我的 Satochip 丢失，我将把它作为最后的手段。



这里选择的备份策略取决于你的喜好，但必须至少有一份记忆词组的副本，可以是物理介质（纸质或金属），也可以像这里一样放在 Seedkeeper 中。您还可以根据需要增加备份数量。有关投资组合备份策略的更多信息，我建议您阅读本教程 ：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

要在 Seedkeeper 上备份 seed，请直接进入 "备份种子 "菜单。



![Image](assets/fr/17.webp)



然后将 Seedkeeper 插入智能卡阅读器，并选择 "至 SeedKeeper"。



![Image](assets/fr/18.webp)



输入密码解锁。



![Image](assets/fr/19.webp)



选择一个 "标签"，以便轻松识别存储在 Seedkeeper 上的不同秘密。例如，您可以简单地保留 wallet 的印记，也可以明确标明 "种子"。选择取决于您的偏好和风险。



![Image](assets/fr/20.webp)



如果你的备份策略完全依赖于 Seedkeeper，我强烈建议你现在就运行空恢复测试，然后比较指纹，检查备份是否正常。



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper 的 PIN 码应尽可能长且随机，以防在卡片受到物理破坏时被暴力破解。您还应将此 PIN 码备份一份，与 Seedkeeper 分开存放。没有这个 PIN 码，你就无法访问存储在 Seedkeeper 中的助记符，你的比特币也将永久丢失。



### 5.3.在 Satochip 上保存 seed



现在，您的投资组合已经生成、保存和验证，我们将把它传输到 Satochip 上。为此，请确保 seed 已加载到 SeedSigner 的 RAM 中。然后进入 "工具 > 智能卡工具 > Satochip 功能"。



![Image](assets/fr/21.webp)



将 Satochip 插入智能卡读卡器，然后选择 "使用种子初始化"。



![Image](assets/fr/22.webp)



设备会提示您输入 Satochip PIN 码；由于卡是新的，尚未初始化，所以还没有 PIN 码。输入任何代码都可以跳过这一步（这不是一个封锁步骤）。



![Image](assets/fr/23.webp)



SeedSigner 检测到您的 Satochip 尚未初始化。点击 "我明白 "确认。



![Image](assets/fr/24.webp)



然后，您可以设置 Satochip PIN 码，从 4 个字符到 16 个字符不等。为了加强 wallet 的安全性，请选择一个较长的随机密码：这是唯一可以防止对您的记忆短语进行物理访问的方法。



根据您的个人策略，请记住在创建密码后立即将其保存在安全的密码管理器或物理介质中。在后一种情况下，请务必不要将包含 PIN 码的介质与 Satochip 存放在同一个地方，否则保护将失去作用。备份副本非常重要： **没有这个 PIN 码，您将无法访问您的 seed，您的比特币也将永远丢失**。



![Image](assets/fr/25.webp)



然后，SeedSigner 会询问您要将哪个 seed 导入 Satochip。选择指纹与您刚刚创建的投资组合相匹配的 seed。



![Image](assets/fr/26.webp)



您的 seed 现已导入 Satochip。



![Image](assets/fr/27.webp)



现在您可以关闭 SeedSigner。



如果您想使用 passphrase BIP39 来增强 wallet 的安全性，请参阅本教程的第 6 部分：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6.将 wallet 导入 Sparrow



现在，您的投资组合已经启动并运行，我们将把其公共信息（"*keystore*"）导入 Sparrow Wallet 或其他投资组合管理软件。该软件将用于创建、分发和跟踪您的交易。不过，该软件无法对交易进行签名，因为只有 Satochip（以及任何备份）才持有签名所需的私人密钥。



### 6.1 准备 SeedSigner 和 Satochip



插入装有操作系统的 microSD 卡，然后打开 SeedSigner。目前，它什么也做不了，因为它还不知道您的 seed。您必须先将 Satochip 插入智能卡读写器，因为它才是装有 seed 的卡。



从主屏幕访问 "工具 > 智能卡工具 > Satochip 功能 "菜单。



![Image](assets/fr/28.webp)



然后点击 "Export Xpub"。



![Image](assets/fr/29.webp)



选择投资组合类型。在我们的例子中，这是一个单一的投资组合：选择 "Single Sig"。



![Image](assets/fr/30.webp)



接下来是选择脚本标准。选择最新的："Native SegWit"。



![Image](assets/fr/31.webp)



最后，选择 "协调器"，即您希望使用的投资组合管理软件。在这里，我们将使用 Sparrow Wallet。



![Image](assets/fr/32.webp)



出现警告信息：这是完全正常的。扩展公钥（"xpub"）允许您查看从您的 seed 导出的所有地址（在第一个账户上）。然而，它并不能访问您的资金：泄露它将会危及您的隐私，但不会危及比特币的安全。换句话说，它允许您查看余额，但不能使用余额。



点击 "我明白"。



![Image](assets/fr/33.webp)



然后输入 Satochip 的 PIN 码进行解锁。这是您在步骤 5 中定义并保存的密码。



![Image](assets/fr/34.webp)



最后，如果对显示的信息满意，请单击 "Export Xpub"（导出 Xpub）。



![Image](assets/fr/35.webp)



然后，SeedSigner 会以动态 QR 代码的形式生成您的 xpub，其中包含您在 Sparrow Wallet 中管理投资组合所需的所有数据。您可以使用操纵杆调节屏幕亮度，使扫描 QR 码更容易。



### 6.2 将新组合导入 Sparrow Wallet



确保 Sparrow Wallet 软件已安装在您的计算机上。如果您不知道如何下载、检查真伪和正确安装，请参阅我们的完整教程：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

在计算机上打开 Sparrow Wallet，然后在菜单栏中单击 "文件 → 导入 Wallet"。



![Image](assets/fr/36.webp)



向下滚动到 "SeedSigner"，然后选择 "扫描..."。您的网络摄像头将被激活：扫描 SeedSigner 屏幕上显示的动态 QR 码。



![Image](assets/fr/37.webp)



为您的投资组合指定一个名称，然后点击 "创建 Wallet"。然后，Sparrow 会要求您设置一个密码，以锁定本地对该 wallet 的访问。选择一个强大的密码：它可以保护您在 Sparrow 中的数据（公钥、地址、标签和交易历史）。不过，将来恢复 wallet 时不需要该密码：只需要您的记忆短语（可能还有您的 passphrase）。



我建议您将此密码保存在密码管理器中，以免丢失。



![Image](assets/fr/38.webp)



您的密钥库已成功导入。



![Image](assets/fr/39.webp)



现在检查 Sparrow Wallet 中显示的 "主指纹 "是否与之前在 SeedSigner 上找到的指纹一致。



然后，SeedSigner 会要求您从 Sparrow wallet 中随机扫描一个接收地址，以确认导入的有效性。



![Image](assets/fr/40.webp)



您的 Satochip（通过 SeedSigner）和 Sparrow Wallet 现在已安全连接。Sparrow 充当一个完整的管理界面，而 Satochip 仍然是唯一能够签署交易的设备。现在，您已经准备好在完全隔绝空气的配置下接收和发送比特币了。



![Image](assets/fr/41.webp)



## 7.接收和发送比特币



您的 Satochip 和 Sparrow Wallet 现在已配置为可一起工作。在本节中，我们将逐步讲解如何在这种模式下接收和发送比特币。



### 7.1 接收比特币



#### 7.1.1 生成接收地址



在电脑上打开 Sparrow Wallet，使用密码解锁您的 `Satochip-SeedSigner` wallet。检查软件是否已连接到服务器（右下角的指示灯）。然后在侧边栏点击 "接收"。



![Image](assets/fr/42.webp)



会出现一个新的 Bitcoin 地址。您会发现 ：




- 文本格式的地址（如果您使用的是 P2WPKH，则以 "bc1q... "开头）；
- 相关的二维码 ；
- 标签 "字段，用于跟踪交易。



我强烈建议您在 wallet 中的每个比特币收据上添加一个标签。这将帮助您轻松识别每个 UTXO 的出处，更好地管理您的隐私。想了解更多关于这个重要主题的信息，请查看 Plan ₿ Academy 上的专门培训：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

要添加标签，只需在 "标签 "字段中输入名称，然后确认即可。



例如



```txt
Label : Sale of the Raspberry Pi Zero
```



现在，您的地址在所有 Sparrow 分区中都与此标签相关联。



![Image](assets/fr/43.webp)



#### 7.1.2 种子签收机上的 Address 验证



在向付款人发送收款地址之前，必须检查该地址是否属于您的 seed。这一步骤可确保 Satochip 能够签署与该地址相关的交易。它还可以防止 Sparrow 显示欺诈地址的潜在攻击。请记住，Sparrow 是在不安全的环境（您的电脑）中运行的，其攻击面远远大于完全隔离的 Satochip。因此，在 wallet 硬件上检查地址之前，千万不要盲目相信 Sparrow 中显示的地址。



在 Sparrow 中，点击地址的 QR 代码可将其放大：然后将全屏显示。



![Image](assets/fr/44.webp)



在 SeedSigner 上，将 Satochip 插入阅读器，然后从主菜单中选择 "扫描"。扫描电脑上显示的二维码，然后选择 "使用 Satochip 卡"。



![Image](assets/fr/45.webp)



然后确认使用的脚本类型（本例中为 "Native SegWit"），输入 Satochip PIN 码解锁，并验证 "xpub "信息。



![Image](assets/fr/46.webp)



如果扫描的地址与您的 seed 得出的地址相符，SeedSigner 将显示信息：已验证 Address。



![Image](assets/fr/47.webp)



这样您就可以确定该地址属于您的投资组合。



#### 7.1.3 接收资金



现在，您可以将该地址以文本形式或通过 QR 码传送给需要向您发送统计数据的个人或部门。交易一旦在网络上广播，就会出现在 Sparrow Wallet 的 "交易 "选项卡中。



![Image](assets/fr/48.webp)



### 7.2 发送比特币



使用 Satochip-SeedSigner 配置发送比特币涉及 3 个步骤：




- 在 Sparrow 中创建事务 ；
- 通过 SeedSigner .NET，在 Satochip 上签署此交易；
- 最后，交易由 Sparrow 通过网络广播。



两台设备之间的所有交换都完全通过 QR 码进行。



#### 7.2.1 在 Sparrow 中创建交易



在 Sparrow Wallet 中，点击左侧边栏的 "发送 "选项卡即可创建交易。不过，我更喜欢使用 "UTXOs "选项卡，它可以让你实践*Coin Control*。这种方法可以精确控制所花费的 UTXOs，从而限制交易过程中泄露的信息。



在 "UTXOs "选项卡中，选择要使用的硬币，然后点击 "发送所选"。



![Image](assets/fr/49.webp)



然后填写交易栏：




- 在 "付款至 "中，粘贴收件人地址或使用相机图标扫描其 QR 码；
- 在 "标签 "中，添加一个标签来追踪这笔费用；
- 在 "金额 "中，输入要发送的金额；
- 最后，根据当前的网络条件选择充电率（可在 [mempool.space](https://mempool.space/) 上获取估计值）。



填写完所有字段后，请仔细查看信息，然后单击 "创建交易 >>"。



![Image](assets/fr/50.webp)



最后一次检查交易详情是否准确，然后点击 "最终完成交易以供签署"。



![Image](assets/fr/51.webp)



交易现已准备就绪，但尚未签署。要将 [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) 显示为二维码，请单击 "显示二维码"。



![Image](assets/fr/52.webp)



#### 7.2.2 与 Satochip 签署交易协议



像往常一样打开 SeedSigner 并插入 Satochip。在主屏幕上选择 "扫描"，然后扫描 Sparrow 上显示的二维码。



![Image](assets/fr/53.webp)



选择 "使用 Satochip 卡 "选项。



![Image](assets/fr/54.webp)



输入 PIN 码解锁智能卡。



![Image](assets/fr/55.webp)



SeedSigner 会检测到这是一个 PSBT，并显示交易摘要：




   - 发送的金额、
   - 目的地地址、
   - 相关交易成本。



点击 "查看详情"，直接在 SeedSigner 屏幕上仔细查看所有信息。最重要的检查点是发送金额、目的地地址和交易费用。



![Image](assets/fr/56.webp)



如果一切正常，请选择 "批准 PSBT"，使用 Satochip 签署交易。



![Image](assets/fr/57.webp)



签名完成后，SeedSigner 会生成一个包含已签名交易的新 QR 码，供 Sparrow 扫描。



#### 7.2.3 广播来自 Sparrow 的交易



现在，交易已签名并通过验证，剩下的工作就是在 Bitcoin 网络上广播，以便矿工将其纳入区块。在 Sparrow 中，点击 "扫描 QR"。



![Image](assets/fr/58.webp)



将 SeedSigner 上显示的二维码（包含已签署交易的二维码）对准网络摄像头。Sparrow 将显示所有交易详情。检查所有信息是否正确，然后点击 "广播交易"，在 Bitcoin 网络上进行广播。



![Image](assets/fr/59.webp)



您的交易现在已传送到网络。您可以在 Sparrow Wallet 的 "交易 "选项卡中查看交易确认情况。



![Image](assets/fr/60.webp)



## 8.找回你的 wallet



正如我们在前面章节中所看到的，根据您的安全策略，除了 Satochip .NET Framework 之外，还有几种备份恢复短语的方法：




- 将经典的 *SeedQR* 与 SeedSigner .NET 一起使用；
- 将记忆短语记录在物理介质上；
- 或者如第 5.2 节所述，将其存储在种子管理器中。



在任何情况下，您都需要在两种主要情况下进行干预：丢失 Satochip 或丢失 SeedSigner。让我们来看看在这两种情况下该如何应对。



### 8.1.使用 Satochip 检索您的 wallet



如果您的 Satochip 还在，但您的 SeedSigner 已损坏或丢失，这种情况的处理相当简单，因为您的 wallet 还在 Satochip 中。



最好的办法是推荐必要的组件，然后从头开始重建一个新的 SeedSigner。由于这是一个 "无状态 "设备，因此使用同一个或另一个 SeedSigner 都没有关系：只要能插入 Satochip，一切都能正常工作。



如果您不想重建一个，也可以用传统方式使用 Satochip，即直接从电脑使用，而无需通过 SeedSigner。这种方法非常有效，但却大大降低了 Bitcoin wallet 的安全性：您失去了 "*air-gapped*"隔离功能，现在必须盲签，因为 SeedSigner 充当了可信屏幕的角色。不过，在紧急情况下，或者在无法重建 SeedSigner 的情况下，这也不失为一种临时解决方案。



为此，您需要一个 USB 智能卡或 NFC 读卡器。在 Sparrow 中打开要还原的 wallet，然后转到 "设置 "选项卡，点击 "替换"。



![Image](assets/fr/61.webp)



将 Satochip 插入连接到计算机的智能卡读写器，然后点击 "Satochip "旁边的 "导入"。



![Image](assets/fr/62.webp)



最后，输入智能卡密码解锁。然后，您就可以访问您的 wallet，创建交易并直接使用连接的 Satochip 进行签名。



### 8.2.使用 SeedSigner 检索您的投资组合



另一种更微妙的情况是，您失去了使用包含 seed 的 Satochip 的权限：无论是它坏了、丢了、被偷了，还是您忘记了它的 PIN 码。如果您的 Satochip 被盗或遗失，我们强烈建议您在恢复资金访问权限后，立即将比特币转移到用不同的 seed 生成的全新 wallet 中。这样可以确保潜在的攻击者永远无法访问您的比特币。



要重新访问您的投资组合并转移资金，只需将 seed 载入 SeedSigner 即可。根据您使用的备份介质，您有几种选择：





- 在 "种子 > 输入 12 个字的 seed "菜单中手动输入记忆短语。



![Image](assets/fr/63.webp)





- 点击主页上的 "扫描 "按钮，扫描您的*SeedQR*。



![Image](assets/fr/64.webp)





- 或者通过 "种子 > 从种子管理器 "菜单从种子管理器加载 seed（这是我在本教程中使用的方法）。您只需输入 Seedkeeper PIN 码，并在 SeedSigner 上选择用作 seed 的密文。



![Image](assets/fr/65.webp)



一旦 seed 被加载到 SeedSigner 中，无论您使用哪种方法，您都可以签署一个或多个扫描交易，将您的比特币转移到一个新的、未加密的 wallet 中。要了解如何操作，请参阅下面教程的第 7.2 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

现在您知道如何结合 SeedSigner 使用 Satochip 安全地管理您的 Bitcoin 投资组合了吧。



如果这些设置让您信服，请不要犹豫，支持那些使之成为可能的项目：




- 直接[在 Satochip 网站上]购买设备(https://satochip.io/shop/)；
- 向 SeedSigner 项目捐款](https://seedsigner.com/donate/)；
- 订阅 [Crypto Guide 的 YouTube 频道](https://www.youtube.com/@CryptoGuide/)，该频道由维护本教程中使用的修改固件的 GitHub 存储库的人员运营。