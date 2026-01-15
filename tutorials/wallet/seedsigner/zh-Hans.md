---
name: SeedSigner
description: DIY 无状态、经济实惠、完全空气封接的 wallet 硬件
---

![cover](assets/cover.webp)



SeedSigner 是一个开源的 wallet Bitcoin 硬件，任何人都可以使用廉价的通用电子元件自行制作。与 Ledger、Coldcard 或 Trezor 等商业产品不同，这不是一个由公司生产的即用型设备：它是一个社区项目，允许任何人创建自己的设备，并控制每一个步骤。



SeedSigner 的设计是 100% ***空气屏蔽***：它从不连接互联网，没有 Wi-Fi 或蓝牙（在 Raspberry Pi Zero v1.3 的情况下），也从不与计算机连接以交换数据。通信完全通过二维码交换系统进行。具体来说，您的投资组合管理软件（如 Sparrow Wallet）会以 QR 码的形式显示要签署的交易；您使用 SeedSigner 的摄像头扫描这些 QR 码，然后设备会使用临时存储在其 RAM 中的私钥签署交易。最后，它会生成包含已签名交易的 QR 码，您可以用软件扫描这些 QR 码，将其发送到 Bitcoin 网络。



![Image](assets/fr/001.webp)



SeedSigner 也是***无状态***。换句话说，与其他硬件钱包不同，它不会永久保存您的 seed 或私钥。每次重启时，它的内存都会完全清空，除非您将设备配置为将设置保存在 microSD 卡上。因此，每次使用时都必须重新输入 seed，最实用的方法是将其存储为 QR 码，在启动时使用 SeedSigner 的摄像头扫描。这种操作模式大大降低了攻击面：即使小偷偷了您的设备，他也不会在上面找到任何信息，因为默认情况下它总是空的。



另一种存储 seed 并与 SeedSigner 一起使用的方法是将 *SeedKeeper* 智能卡与兼容读卡器结合使用。这将为您提供一个非常强大的*安全元素*来存储 seed，同时使用 SeedSigner 屏幕来签署交易。但这种特殊配置将是另一个专门教程的主题。在此，我们将重点介绍 SeedSigner 的基本使用方法：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner 项目在 Bitcoin 生态系统中占有重要地位，因为它为世界各地的每个人提供了利用先进的安全技术保护比特币的可能性。它的主要优势在于其易用性：所需硬件的购买价格不到 50 美元。更重要的是，它能让生活在受限国家的人们利用标准计算机组件构建自己的 wallet 硬件，因为这些组件很容易找到，而且受监管限制较少。



不过，即使不在这些特殊情况下，SeedSigner 对您来说也是一个有趣的选择：它是开源的，可以无状态和空中屏蔽运行，并减少了与 wallet 硬件供应链相关的攻击向量。



## 1.所需设备



要创建 SeedSigner，您需要以下组件：





- Raspberry Pi Zero
    - 建议使用 1.3 版，因为它既没有 Wi-Fi 也没有蓝牙，可确保完全隔离。
 - W 和 v2 版本也兼容，但集成了 Wi-Fi/Bluetooth 芯片。因此，建议将无线电模块从卡上取下，使其物理停用。操作相对简单，但需要精确度（对于 Zero W 来说，精细的钳子就足够了，而对于 v2 来说，则需要使用热笔来移除隐藏模块的金属板）。本教程不再赘述，但您可以在本文档中找到所有说明： *[硬件禁用 WiFi/蓝牙](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*。
 - 请注意：某些 Raspberry Pi Zero 型号在销售时没有预焊 GPIO 引脚。您可以直接购买集成引脚的版本（最简单的解决方案），或者单独购买引脚并自己焊接（更复杂的解决方案）。
 - 别忘了附上微型 USB 电源。



![Image](assets/fr/002.webp)





- Waveshare 1.3 英寸屏幕（240×240 px）** （法语）
    - 选择这种特殊型号至关重要：还有其他类似的屏幕，但分辨率不同。如果没有 240×240 px 的分辨率，显示屏将无法使用。
    - 屏幕上有三个按钮和一个迷你操纵杆，用于用户界面。



![Image](assets/fr/003.webp)





- 兼容 Raspberry Pi Zero** 的摄像头
    - 方案 1：带宽金色垫子的标准相机（请检查与外壳的兼容性）。
    - 方案 2：更小巧的 "*Zero*"摄像头，专为 Pi Zero 设计。



![Image](assets/fr/004.webp)





- MicroSD** 卡
    - 建议容量：4 至 32 GB。





- 住房（可选但建议）** （可选但建议）** （可选但建议）** （可选但建议）**)
    - 保护设备，方便使用。
    - 最受欢迎的模型是 "*橙色药盒*"，其[开源 STL 文件可用于 3D 打印](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures)。
    - 盒子还可从[与项目相关的独立经销商](https://seedsigner.com/hardware/)处购买。



![Image](assets/fr/005.webp)



你可以单独购买这些组件，也可以选择包含所有必要硬件的现成软件包，以简化操作。就我个人而言，我是[在这个法国网站](https://bitcoinbazar.fr/)上订购的，但你也可以在[SeedSigner 项目硬件页面](https://seedsigner.com/hardware/)上找到全球各地区的供应商名单。如果你想单独购买组件，可以在各大电子商务平台或专业商店购买。



## 2.准备软件



硬件准备就绪后，您需要在 microSD 卡上安装 SeedSigner 系统。为此，请进入日常使用的个人电脑，插入用于 SeedSigner 的 microSD。



### 2.1.下载



访问 [该项目的官方 GitHub 代码库](https://github.com/SeedSigner/seedsigner/releases)。在软件的最新版本上，下载 ：




- 与您的 Pi 型号相对应的 `.img` 映像。
- .sha256.txt "文件。
- .sha256.txt.sig "文件。



![Image](assets/fr/006.webp)



在开始安装之前，让我们先检查一下软件。



### 2.2 在 Linux 和 macOS 下进行验证



首先，从 Keybase 直接导入 SeedSigner 项目的官方公钥：



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



终端会提示你已导入或更新密钥。接下来，在签名文件上运行验证命令（记得根据版本修改命令，此处为 "0.8.6.`"）：



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



如果一切正常，输出结果应为 "良好签名"。这意味着文件 `.sha256.txt`已被你刚刚导入的密钥签名，且签名有效。忽略警告信息 `警告：此密钥未通过可信签名认证`：这是正常的，因为现在要由你来检查所使用的密钥是否属于 SeedSigner 项目。



为此，请将显示的指纹最后 16 个字符与[Keybase.io/SeedSigner](https://keybase.io/seedsigner)、其[官方 Twitter](https://twitter.com/SeedSigner/status/1530555252373704707)或[SeedSigner.com](https://seedsigner.com/keybase.txt)上发布的文件中的字符进行比较。如果这些标识符完全匹配，就可以确定密钥确实是项目的。如有疑问，请立即停止，并向 SeedSigner 社区（Telegram、X、GitHub......）寻求帮助。



验证密钥后，就可以检查下载的映像是否被修改过（切记根据版本修改命令，此处为 "0.8.6.`"）：



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- 在 Linux 下，该命令是内置的。
- 警告："Big Sur (11) "之前的 macOS 版本不识别"--忽略丢失 "选项。在这种情况下，请删除该选项并忽略有关丢失文件的警告。



预期结果是在 `.img` 文件旁边显示 "OK"。这就确认了上传的图像与项目发布的图像完全相同，没有被修改过。



### 2.3 窗口验证



在 Windows 系统中，操作步骤类似，但命令不同。首先安装 [Gpg4win](https://www.gpg4win.org/)，然后打开 *Kleopatra* 应用程序。从 URL Keybase 导入 SeedSigner 项目的公钥：



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



接下来，在下载文件所在文件夹中打开 PowerShell（`Shift` + 右键单击 > `在此打开 PowerShell`）。运行以下命令检查清单签名（记住根据版本修改命令，此处为 `0.8.6.`）：



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



如果一切正常，输出结果应为 "良好签名"。这意味着文件 `.sha256.txt`已被你刚刚导入的密钥签名，且签名有效。忽略警告信息 `警告：此密钥未通过可信签名认证`：这是正常的，因为现在要由你来检查所使用的密钥是否属于 SeedSigner 项目。



为此，请将显示的指纹最后 16 个字符与[Keybase.io/SeedSigner](https://keybase.io/seedsigner)、其[官方 Twitter](https://twitter.com/SeedSigner/status/1530555252373704707)或[SeedSigner.com](https://seedsigner.com/keybase.txt)上发布的文件中的字符进行比较。如果这些标识符完全匹配，就可以确定密钥确实是项目的。如有疑问，请立即停止，并向 SeedSigner 社区（Telegram、X、GitHub......）寻求帮助。



验证密钥后，需要检查映像文件是否已损坏。为此，请在 PowerShell 中使用以下命令 ：



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



以 Raspberry Pi Zero 2 为例（请根据您的版本修改命令，此处为 "0.8.6.`"）：



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



然后，PowerShell 会计算图像文件的 SHA256 哈希值。将此散列值与 `seedsigner.0.8.6.sha256.txt` 中的相应值进行比较。




- 如果两个值完全相同，则检查成功，可以继续。
- 如果两者不同，则说明文件已损坏或损坏。请不要使用它，重新开始下载。



![Image](assets/fr/013.webp)



验证成功可确保您的 `.img` 文件是真实的（由 SeedSigner 签名）且未被篡改（未修改）。这样您就可以安全地进入下一步。



### 2.4.闪存图像



如果还没有，请下载 [Balena Etcher] 软件 (https://etcher.balena.io/)，然后 ：




- 将 microSD 卡插入电脑。
- 启动蚀刻机。
- 选择已下载并验证的 `.img` 文件。
- 选择 microSD 卡作为目标。
- 点击 "Flash!"。



![Image](assets/fr/014.webp)



等待该过程完成：您的 microSD 就可以使用了。现在是组装时间！



## 3.SeedSigner 组件



准备好 microSD 卡并用 SeedSigner 软件闪存后，就可以进行最后的组装了。由于某些部件（尤其是桌布、摄像头和 GPIO 引脚）易碎，因此请慢慢来。



### 3.1 准备机壳



首先，打开机箱。检查它是否干净，内部紧固件上是否有残留的 3D 打印塑料。注意：




- 摄像头位置（前端的小圆孔）。
- 屏幕的开口。
- Raspberry Pi Zero 的微型 USB 端口和 microSD 插槽的开口。



### 3.2 摄像头安装



找到 Raspberry Pi Zero 上的摄像头带状连接器：它是电路板侧面的一条黑色细带，稍微抬起即可打开。小心抬起，不要用力：只需倾斜几毫米即可。



![Image](assets/fr/015.webp)



插入相机盖。棕色/铜色部分应朝下。确保它稳固地插入连接器，不要扭曲。



![Image](assets/fr/016.webp)



关闭黑色条，锁定桌布（您会感觉到轻微的咔哒声）。轻轻检查桌布是否固定不动。



![Image](assets/fr/017.webp)



然后将相机模块放入外壳的相应孔中。根据型号的不同，可能会直接卡入，也可能需要用小胶条固定。镜头必须完全对准，朝外。



### 3.3 安装 Raspberry Pi Zero



如果使用外壳，请将 Raspberry Pi Zero 板插入其中。小心地将端口与提供的开口对齐。



然后将 Waveshare 显示器放在 Raspberry Pi Zero 的顶部。Pi 的 GPIO 引脚应与显示器的母接头完全对齐。慢慢地将显示屏按到针脚上，每边用力均匀，避免弯曲。



![Image](assets/fr/018.webp)



如果有机箱，则通过添加前面板和操纵杆完成组装。



最后，将包含闪存软件的 microSD 卡插入 Raspberry Pi Zero 的边缘插槽。确保卡入到位。



### 3.4 首次启动



将微型 USB 电源线连接到专用端口。等待约一分钟。此时会出现 SeedSigner 徽标，然后是主屏幕。



![Image](assets/fr/019.webp)



首先，进入 "设置 > 输入/输出测试 "菜单，检查各个组件是否正常工作。



![Image](assets/fr/020.webp)



测试所有按钮，确保它们反应正常。然后点击 "KEY1 "按钮，检查相机是否按预期工作。这将拍摄一张照片。



![Image](assets/fr/021.webp)



### 3.5 相机调整



根据您安装 SeedSigner 的方式，摄像头可能会显示倒置图像。要纠正这种情况，请转到 "设置 > 高级 > 相机旋转"，必要时选择 180° 旋转。



![Image](assets/fr/022.webp)



如果你改变了摄像头的方向或希望以后再更改其他设置（如界面语言），你需要在 microSD 上启用持久设置。否则，由于 Raspberry Pi Zero 没有持久内存，每次重启都会恢复默认设置。



为此，请打开 "设置 > 持久设置 "菜单，然后选择 "已启用"。



![Image](assets/fr/023.webp)



如果一切正常，您的 SeedSigner 就可以使用了！



## 4.种子签约者设置



在创建 Bitcoin wallet 之前，我们先来配置 SeedSigner。由于 SeedSigner 是在没有持久内存的 Raspberry Pi Zero 上运行的，因此除非将设置保存在 microSD 卡上，否则不会自动保存。因此，请确保您已启用该选项，否则这些设置将在重启时丢失（见第 3.5 步）。



### 4.1 进入参数菜单



启动 SeedSigner，等待主屏幕出现。使用操纵杆导航到 "设置 "选项，然后按中央按钮进行验证。现在进入主设置菜单。



![Image](assets/fr/024.webp)



### 4.2 选择投资组合管理软件



然后进入 "协调器软件 "菜单。



![Image](assets/fr/025.webp)



协调器 "是指投资组合管理软件，SeedSigner 将通过二维码与之通信。该软件安装在您的电脑或智能手机上。它将使您能够管理您的比特币，但无法访问您的私人密钥。SeedSigner 仍然是唯一能够对你的交易进行签名的设备。



当前固件版本支持多个程序：Sparrow、Specter、BlueWallet、Nunchuk 和 Keeper。我使用的是**Sparrow Wallet**，我特别推荐它，因为它操作简单，功能丰富。



如果不知道如何安装，可以参考本教程：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

只需从菜单中选择您所需的软件即可。



![Image](assets/fr/026.webp)



### 4.3 单位和数量显示



在 "面值显示 "菜单中，您可以选择显示金额的单位：




- BTC
- mBTC`（毫比特币，或 0.001 BTC）
- gW-15（沙托希，或 1/100,000,000 BTC）



一般来说，**sats** 设备对小量使用最为实用。



![Image](assets/fr/027.webp)



### 4.4 高级设置



现在进入 "高级 "菜单。这里有几个有用的选项：




- gW-17 network`：仅在希望在 Testnet 上使用 SeedSigner 时修改。
- qR 代码密度"：调整每个 QR 代码所含的信息量。您可以保留默认值，除非您觉得扫描时难以读取。
- Xpub export`：启用或禁用扩展公钥（"xpub"、"ypub"、"zpub"）通过 QR 码导出到投资组合管理软件（我们稍后会用到此功能，因此暂时不启用）。
- 脚本类型"：定义允许锁定比特币的脚本类型。您不需要修改此参数，因为脚本类型将直接设置为 Sparrow。这里只涉及种子签名者有权操作的脚本。



### 4.5 语言选择



最后，在 "语言 "菜单中，您可以根据自己的喜好更改界面语言。



![Image](assets/fr/028.webp)



## 5.创建和保存 seed



seed （或助记词组）是 Bitcoin 投资组合的基础。它用于生成您的私人密钥和地址，并为您提供资金访问权限。SeedSigner 提供了几种生成 seed 的方法，我们将在本节中一一介绍。



在我们开始之前，有几项重要提醒：




- 拥有这个短语的任何人都可以盗取你的资金，即使无法实际访问你的 SeedSigner；
- 通常，在 wallet 硬件丢失或被盗的情况下，可以使用一个 12 个字符的短语来恢复 wallet。但由于 SeedSigner 是一个*无状态*设备，它永远不会注册你的 seed。因此，您的物理备份不是简单的备份副本，而是使用 wallet 的**唯一途径。如果您丢失了这些备份，您的比特币将永久丢失。因此，请小心备份，备份在多个介质上并放在安全的地方；
- 如果你刚刚开始学习，我强烈建议你阅读本教程，详细了解管理记忆短语所涉及的风险：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 访问 seed 创建工具



从 SeedSigner 主屏幕进入 "工具 "菜单。



![Image](assets/fr/029.webp)



现在，您将 generate 您的 seed。seed 只是一个大的随机数。生成的随机数越多，安全性就越高。SeedSigner 提供了两种方法：




- 相机"：seed 是由照片的视觉噪音产生的。你拍摄一张随机环境（物体、风景、人脸等）的图像，其像素变化被用来生成 generate 熵。这是一种快速方法，但不可复制。
- 掷骰子"：通过掷骰子产生必要的熵。这种方法比较耗时，但可重复，因此可以验证。如果您选择这种方法，请遵循本教程中的建议（此处无需计算校验和，SeedSigner 会负责计算）：



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 用照片创建 seed



如果您选择拍照方式，请点击 "新建 seed"（带相机图标），拍照并验证。然后选择句子的长度（12 或 24 个字），句子将显示在屏幕上以便保存。以下步骤与 5.3 部分相同。



### 5.3 用骰子创建 seed



在本教程中，我们使用**掷骰子**方法。点击 "新建 seed"（带骰子图标）。



![Image](assets/fr/030.webp)



然后选择记忆短语的长度。12 个单词已经提供了足够的安全性，所以我建议选择这个长度。



![Image](assets/fr/031.webp)



掷骰子并使用光标输入结果数字。按中间的按钮来验证每次输入。如果出现错误，您可以返回。使用多个不同的骰子，以减少任何不平衡骰子的影响。确保在操作过程中没有人在监视您。



![Image](assets/fr/032.webp)



输入 50 个数字后，SeedSigner 就会生成您的句子。 **如果您刚开始学习，请仔细阅读本教程中的说明：**。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 显示和保存 seed



在合适的实物支撑物（纸张或金属）上认真写下记忆短语的单词。



![Image](assets/fr/033.webp)



### 5.5 检查备份



为避免任何备份错误，SeedSigner 会要求您验证备份。单击 "验证"。



![Image](assets/fr/034.webp)



然后根据单词在句子中的顺序输入所需的单词。例如，在这里我必须选择句子中的第三个单词。



![Image](assets/fr/035.webp)



如果您出错，SeedSigner 会通知您，您必须重新开始，并确保记下给您的助记词。这一验证步骤可确保您的备份正确完整。验证完成后，屏幕将显示 "备份已验证"。



![Image](assets/fr/036.webp)



要进行更完整的修复测试，请参考本教程 ：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 理解 "无状态设备 "概念



SeedSigner 是一款没有永久内存的设备。这意味着 seed 不会存储在设备中（与 Ledger、Trezor 或 Coldcard 等设备不同）。一旦关闭电源，seed 就会从 RAM 中完全消失。当您重新启动时，SeedSigner 会恢复到空白状态：这时您必须再次将 seed 交给它，它才能对您的交易进行签名。



这提供了必要的保护。与其他硬件钱包不同，SeedSigner 基于 Raspberry Pi Zero，而 Raspberry Pi Zero 没有包括 *Secure Element* 在内的物理保护。但是，由于没有存储敏感数据，即使设备受到物理破坏，攻击者也无法提取你的私钥或花费你的比特币。



另一方面，这种架构也意味着额外的责任：如果没有备份，您的资金肯定会丢失。这就是我推荐**双重备份**的原因。您已经有了恢复短语：这是您的主要长期备份，应保存在安全的地方。现在，我们将以**QR 代码**的形式创建该短语的副本。



每次使用 SeedSigner 时，您都要用设备的摄像头扫描这个 QR 码，这样它就会在您签署交易时将您的 seed 暂时加载到内存中。这第二个备份用于日常使用，也必须小心保管：任何持有此 QR 码的人都可以完全访问您的比特币。


我还建议您将二维码和记忆短语分别存放在两个不同的位置，以免在索赔时丢失所有内容。



最后，一种更先进、更安全的替代方法是将 SeedSigner 与**SeedKeeper**一起使用，后者可将 seed 存储在 secure element 中。要了解更多信息，请参阅本教程：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 写入主密钥指纹



验证完成后，SeedSigner 会显示 wallet 主密钥的指纹。该指纹可识别您的 wallet，并确保您将来使用正确的恢复短语。它不会泄露任何有关您私人密钥的信息，因此您可以安全地将其存储在数字介质中。只需确保您保存了一份可访问的副本，并且永远不会丢失。



![Image](assets/fr/037.webp)



在此阶段，您还可以添加**passphrase BIP39**，以加强 wallet 的安全性。根据您的备份策略，这种选择可能是值得的，但也有风险：如果您丢失了 passphrase，您将永远无法访问您的比特币。



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

如果您还不熟悉 passphrase 概念，我邀请您阅读这篇有关该主题的综合教程：



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 将 seed 保存为 QR 格式 (*SeedQR*)



SeedSigner 可让您将 seed 转换成纸质 QR 码，即 *SeedQR*。这种方法可简化 wallet 的重新加载，因为它避免了手动重新输入每个单词。



为此，您需要与记忆短语长度相对应的空白纸张或金属 QR 码。如果您购买了 SeedSigner 的全套软件包，通常会随附模板。如果没有，您可以在此处下载并打印（或手工复制）：




- [12字格式](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24字格式](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [紧凑格式 12 个字](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [紧凑格式 24 个字](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



在 seed 屏幕中，选择 "备份种子"。



![Image](assets/fr/039.webp)



然后选择 "导出为 SeedQR"。



![Image](assets/fr/040.webp)



然后根据可用的纸张模板选择所需的格式（普通或紧凑）。



![Image](assets/fr/041.webp)



单击 "开始 "开始创建 *SeedQR*。然后，SeedSigner 将显示一系列网格（A1、A2、B1 等），每个网格对应代码的一部分。



![Image](assets/fr/042.webp)



在保存页上仔细复制每个黑点，然后使用操纵杆移动到下一个区块。慢慢来：一个简单的错位就可能导致二维码无法使用。



一些小贴士




- 开始时用铅笔，以便纠正错误，完成后再用黑色细钢笔；
- 只需在正方形中间对准一个中心点即可，无需完全填满。



![Image](assets/fr/043.webp)



然后点击 "确认 SeedQR"，扫描您的二维码以检查其是否正常工作。



![Image](assets/fr/044.webp)



如果显示 "成功 "信息，说明您的 *SeedQR* 有效：您可以继续下一步。



![Image](assets/fr/045.webp)



**请将此表作为您的恢复短语严格保管。任何持有此 QR 码的人都可以重建你的私人密钥并盗取你的比特币。



恭喜您，您的 Bitcoin 投资组合已开始运行！现在，我们将把它的公共组件导入到 **Sparrow Wallet** 中，以便轻松管理。



## 6.将 wallet 导入 Sparrow



设置好 SeedSigner 并正确生成和保存 seed 后，下一步就是将该投资组合与 Sparrow Wallet 等管理软件连接起来。您的 seed 将始终保持离线状态，因为只有您的投资组合的公开部分才会传输到 Sparrow。这将使软件能够显示您的地址、交易并建立新的交易，但却无法花费您的比特币。要使用您的比特币，您的 SeedSigner 必须签署 Sparrow 准备好的交易。



### 6.1 准备 SeedSigner



插入装有操作系统的 microSD，打开 SeedSigner，然后加载刚刚从备份二维码中创建的 seed。在主屏幕上选择 "扫描"，然后用 SeedSigner 扫描 SeedQR。



![Image](assets/fr/046.webp)



检查主密钥上的指纹是否与 wallet 上的指纹一致。如果您使用的是 passphrase，请在此阶段输入。



![Image](assets/fr/047.webp)



这将带您进入您的作品集菜单，我的作品集名为 "d4149b27"。如果你回到主屏幕，选择 "种子"，然后选择与你的作品集相对应的打印。然后点击 `Export Xpub`。



![Image](assets/fr/048.webp)



选择投资组合类型。在我们的例子中，这是一个单一的投资组合：选择 "Single Sig"。



![Image](assets/fr/049.webp)



其次是脚本标准的选择。就交易成本而言，最新、最经济的是 "Taproot"。因此，我建议您选择这一标准。



![Image](assets/fr/050.webp)



此时会出现一条警告信息。这是正常现象：该扩展公钥 (`xpub`)允许您查看从 seed 导出的所有地址（在第一个账户上）。它不允许您使用资金，但可以显示您的投资组合结构。如果它泄露了，会影响你的隐私，但不会影响比特币的安全：它允许你查看比特币，但不允许你花费比特币。



单击 "我明白"，如果对显示的信息满意，再单击 "导出 Xpub"。



然后，SeedSigner 会以动态 QR 代码的形式生成您的 xpub，其中包含您在 Sparrow Wallet 中管理投资组合所需的所有数据。



![Image](assets/fr/051.webp)



您可以使用操纵杆调节屏幕亮度，以方便扫描二维码。



### 6.2 将新组合导入 Sparrow Wallet



确保您的计算机上安装了 Sparrow Wallet 软件。如果您不知道如何正确下载、检查和安装，请参阅我们的完整教程：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

在计算机上打开 Sparrow Wallet，然后在菜单栏中单击 "文件 → 导入 Wallet"。



![Image](assets/fr/052.webp)



向下滚动到 "SeedSigner"，然后选择 "扫描..."。您的网络摄像头将打开：扫描 SeedSigner 屏幕上显示的动态 QR 码。



![Image](assets/fr/053.webp)



为您的投资组合指定一个名称，然后点击 "创建 Wallet"。然后，Sparrow 会要求您设置一个密码，以锁定本地对该 wallet 的访问。选择一个强大的密码：它可以保护对 Sparrow 中投资组合数据（公钥、地址、标签和交易历史）的访问。日后恢复投资组合时不需要该密码：只需要您的记忆短语（可能还需要您的 passphrase）。



我建议您将此密码保存在密码管理器中，以免丢失。



![Image](assets/fr/054.webp)



您的密钥库现已成功导入。



![Image](assets/fr/055.webp)



然后检查 Sparrow 中显示的 "主指纹 "是否与之前在 SeedSigner 中记录的指纹一致。



您的 SeedSigner 和 Sparrow Wallet 现在可以安全地连接在一起。Sparrow 充当一个完整的管理界面，而 SeedSigner 仍然是唯一能够签署交易的设备。现在，您已准备好在完全隔绝空气的配置下接收和发送比特币。



## 7.接收和发送比特币



您的 SeedSigner 和 Sparrow Wallet 现在已经配置好一起工作了。在最后一节，我们将看看如何使用这种配置来接收和发送比特币。



### 7.1 接收比特币



#### 7.1.1 生成接收地址



在电脑上打开 Sparrow Wallet，使用密码解锁 SeedSigner wallet。确保软件已连接到服务器（右下角有缺口）。在侧边栏点击 "接收"。



![Image](assets/fr/056.webp)



显示新的 Bitcoin 地址。您将看到 ：




- 文本地址（如果像我一样使用 P2TR，则以 "bc1p... "开头）、
- 相应的二维码、
- 用于跟踪交易的 "标签 "字段。



我强烈建议您在 wallet 的每个比特币收据上添加一个标签。这样您就可以很容易地识别每个 UTXO 的来源，并改善您的隐私管理。要深入了解这一重要主题，您可以查看 Plan ₿ Academy 上的专门培训：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

要添加标签，只需在 "标签 "字段中输入名称，然后确认即可。



例如



```txt
Label : Sale of the Raspberry Pi Zero
```



现在，您的地址在所有 Sparrow 部分都与此标签相关联。



![Image](assets/fr/057.webp)



#### 7.1.2 种子签名者的 Address 验证



在共享接收地址之前，请务必检查该地址是否属于您的 seed。这一步骤可确保您的 SeedSigner 能够签署与该地址相关的交易。它还能防止 Sparrow 显示欺诈地址的攻击。请记住，Sparrow 是在不安全的环境（您的计算机）中运行的，与完全隔离的 SeedSigner 相比，Sparrow 的攻击面要大得多。因此，在使用 wallet 硬件验证之前，千万不要盲目相信 Sparrow 上显示的接收地址。



在 Sparrow 上，点击地址的二维码可将其放大：然后将全屏显示。



![Image](assets/fr/058.webp)



在 SeedSigner 的主菜单中选择 "扫描"。扫描电脑屏幕上显示的二维码，然后选择与 wallet 相对应的 seed（在我的例子中，是 `d4149b27` 指纹）。



![Image](assets/fr/059.webp)



如果扫描的地址与您的 seed 中的地址相符，SeedSigner 屏幕将显示信息：已验证 Address。



![Image](assets/fr/060.webp)



这将确认该地址属于您的 wallet，您可以放心地从该地址接收比特币。



#### 7.1.3 接收资金



现在，您可以将此地址（文本或 QR 码形式）发送给需要向您发送统计数据的人员或部门。交易一旦在网络上广播，就会出现在 Sparrow Wallet 的 "交易 "选项卡中。



![Image](assets/fr/061.webp)



### 7.2 发送比特币



使用 SeedSigner 发送比特币只需 3 个步骤：




- 在 Sparrow 中创建事务 ；
- 种子签发人的交易签名 ；
- 通过 Sparrow 进行交易的最终分配。



两台设备之间的所有交换都完全使用 QR 码。



#### 7.2.1 在 Sparrow 中创建交易



在 Sparrow Wallet 中，您可以点击左侧边栏的 "发送 "选项卡。不过，我更喜欢使用 "UTXOs "选项卡，它允许您练习 "*Coin 控制*"。这种方法可以让您精确控制所使用的 UTXOs，因此您可以控制交易过程中透露的信息。



在 "UTXOs "选项卡中，选择要使用的硬币，然后点击 "发送所选"。



![Image](assets/fr/062.webp)



然后填写交易栏：




- 在 "支付到 "中，粘贴收件人地址或点击相机图标扫描二维码；
- 在 "标签 "中，添加一个标签来跟踪这项支出；
- 在 "金额 "中，输入要发送的金额；
- 最后，根据当前的市场条件选择费率（可在 [mempool.space](https://mempool.space/) 上获取估算值）。



填写完毕后，请仔细核对信息，然后点击 "创建交易 >>"。



![Image](assets/fr/063.webp)



检查交易详情，确保一切正确无误，然后点击 "最终完成交易以供签署"。



![Image](assets/fr/064.webp)



交易现已准备就绪，但尚未签署。要将 [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) 显示为二维码，请单击 "显示二维码"。



![Image](assets/fr/065.webp)



#### 7.2.2 与种子签署人签署交易



像往常一样，打开 SeedSigner 并扫描您的 SeedQR 以访问您的投资组合。从主屏幕选择 "扫描"，然后扫描 Sparrow 上显示的二维码。



![Image](assets/fr/066.webp)



然后选择与您的产品组合相匹配的 seed。



![Image](assets/fr/067.webp)



SeedSigner 会自动检测到这是一个 PSBT，并显示交易摘要：




   - 发送的金额、
   - 输出地址、
   - 相关交易成本。



点击 "查看详情"，直接在 SeedSigner 屏幕上仔细检查所有信息。最重要的检查项目是发送金额、收件人地址和收费金额。



![Image](assets/fr/068.webp)



如果一切正常，请选择 "批准 PSBT"，使用相应的私钥签署交易。



![Image](assets/fr/069.webp)



签名后，SeedSigner 会生成一个包含已签名交易的新 QR 码，供 Sparrow 扫描。



![Image](assets/fr/070.webp)



#### 7.2.3 广播来自 Sparrow 的交易



既然交易是有效的，它就需要在 Bitcoin 网络上广播，以便矿工将其添加到区块中。



在 Sparrow 上，单击 "QR 扫描"。



![Image](assets/fr/071.webp)



将 SeedSigner 显示的 QR 码（已签名交易的 QR 码）对准网络摄像头。Sparrow 将解码签名并显示完整的交易详情。最后检查所有信息是否正确，然后点击 "广播交易 "在 Bitcoin 网络上广播。



![Image](assets/fr/072.webp)



您的交易现已发送至 Bitcoin 网络。您可以在 Sparrow Wallet 的 "交易 "选项卡中查看交易进度。



![Image](assets/fr/073.webp)



您现在已经掌握了使用 SeedSigner 的基础知识。为了加深您的知识并探索更高级的用途，我邀请您参考以下教程：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[您还可以通过比特币捐款支持 SeedSigner 开源项目的开发！](https://seedsigner.com/donate/)**



*图片来源：本教程中的部分图片来自[SeedSigner 项目官方网站](https://seedsigner.com/) 和[GitHub 存储库](https://github.com/SeedSigner/seedsigner)*。