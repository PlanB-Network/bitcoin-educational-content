---
name: Seedkeeper - 密码管理器
description: 如何使用 Seedkeeper 智能卡保存密码？
---

![cover](assets/cover.webp)



Seedkeeper是Satochip公司开发的一款智能卡，Satochip是一家比利时公司，专门从事管理和保护数字机密的硬件解决方案。Satochip 公司因其为 Bitcoin 生态系统开发的一系列智能卡而闻名，它将 Seedkeeper 设想为存储记忆短语和其他数字机密的传统方法的替代方案。



具体来说，Seedkeeper 是一种通过 EAL6 认证的多功能智能卡，带有安全处理器和防篡改存储器（即所谓的 "安全元件"）。顾名思义，它的作用是以加密和受保护的方式存储 Bitcoin 组合的助记符和密码。有了 Seedkeeper，您可以直接将 generate、导入、组织和保存您的秘密到卡的安全元件中。



在我看来，Seedkeeper 有两个主要用途，我们将在两个不同的教程中探讨：




- Bitcoin** 记忆短语存储：无需在纸上写下 12 或 24 个单词，您可以将它们导入智能卡，并用 PIN 码加以保护。
- 密码管理**：您可以通过 Seedkeeper 应用程序 generate 强密码，并将其直接存储在智能卡中，为您提供方便易用的离线密码管理器。



从技术上讲，Seedkeeper 的容量为 8192 字节，可以存储至少 50 个独立的秘密（具体数量取决于秘密的大小和与每个秘密相关的元数据）。Seedkeeper可以[通过与电脑连接的智能卡读卡器](https://satochip.io/accessories/)访问，也可以通过与NFC连接的移动应用程序访问。整个系统在离线模式下运行，无需互联网连接，从而保证了有限的攻击面。



![Image](assets/fr/001.webp)



一个特别有趣的功能是可以将一个 Seedkeeper 中的内容复制到另一个 Seedkeeper 中以创建备份。在本教程中，我们将向你展示如何做到这一点。



在本教程中，我们只介绍如何使用 SeedKeeper 以密码管理器的方式保存传统密码。如果您想使用 SeedKeeper 保存 Bitcoin wallet 记忆短语，请参阅本教程：



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1.如何获得种子管家？



获取 Seedkeeper 有两种主要方式。你可以 [直接从 Satochip 官方商店购买](https://satochip.io/product/seedkeeper/) 或从授权经销商处购买。不过，由于[种子管家小程序是开源的](https://github.com/Toporin/Seedkeeper-Applet)，你也可以选择自己安装到[空白智能卡](https://satochip.io/product/blank-javacard-for-diy-project/)上。



如果要使用 Seedkeeper 的备份功能，显然需要购买两张智能卡。



## 2.安装 Seedkeeper 客户端



第一步是在电脑或智能手机上安装软件。在电脑上，您需要 [下载最新版本的 Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases)。在手机上，Seedkeeper 应用程序可在 [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) 和 [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060) 上下载。



![Image](assets/fr/002.webp)



## 3.种子管理器初始化



启动应用程序，点击 "*点击和扫描*"按钮。



![Image](assets/fr/003.webp)



您将被要求输入种子管家的 PIN 码。由于这是一张新卡，因此尚未定义 PIN 码。请输入任意代码跳过这一步，然后点击 "*下一步*"。



![Image](assets/fr/004.webp)



然后将卡放在智能手机背面。应用程序会检测到 Seedkeeper 尚未初始化，并提示您设置智能卡的 PIN 码，长度在 4 到 16 个字符之间。为获得最佳安全性，请选择一个尽可能长、随机且由多种字符组成的强大 PIN 码。该 PIN 码是防止物理访问密码的唯一屏障。



**还请记住，现在**保存此 PIN 码，例如保存在密码管理器中，或保存在单独的物理介质中。在后一种情况下，切勿将包含 PIN 码的介质与 Seedkeeper 放在同一个地方，否则这种安全措施就会失去作用。重要的是要有一个可靠的备份：没有 PIN 码，就无法恢复 Seedkeeper 中存储的秘密。



![Image](assets/fr/005.webp)



再次确认 PIN 码。



![Image](assets/fr/006.webp)



Seedkeeper 已初始化。输入刚才设置的 PIN 码即可解锁。



![Image](assets/fr/007.webp)



现在您将进入智能卡管理页面。



![Image](assets/fr/008.webp)



## 4.在 Seedkeeper 上保存密码



种子守护者解锁后，点击 "*+*"按钮。



![Image](assets/fr/009.webp)



选择 "生成密码*"。通过 "*导入密文*"选项，您可以保存现有密文（例如，您过去创建的密码）。



![Image](assets/fr/010.webp)



在本例中，我们要保存一个密码。点击 "*密码*"。



![Image](assets/fr/011.webp)



为该秘密指定一个 "*标签*"，以便在 Seedkeeper 中存储多条信息时可以轻松识别。您还可以添加与密码和网站 URL 相关的标识符。



![Image](assets/fr/012.webp)



选择密码的长度和参数，然后点击 "*生成*"，再点击 "*导入*"。



![Image](assets/fr/013.webp)



将 Seedkeeper 放在智能手机背面。



![Image](assets/fr/014.webp)



您的密码已注册。



![Image](assets/fr/015.webp)



## 5.访问您的 Seedkeeper 密码



如果要检查密码，请带上 Seedkeeper 并点击 "*点击并扫描*"按钮。



![Image](assets/fr/016.webp)



输入密码，然后按 "*下一步*"。



![Image](assets/fr/017.webp)



将 Seedkeeper 放在智能手机背面。



![Image](assets/fr/018.webp)



这将带您进入所有已注册密码的列表。在本例中，我想显示 Plan ₿ Academy 账户的密码，因此点击了它。



![Image](assets/fr/019.webp)



按下 "*揭示*"按钮。



![Image](assets/fr/020.webp)



再次扫描 Seedkeeper。



![Image](assets/fr/021.webp)



屏幕上将显示您之前保存的密码。您可以复制它并在相关网站上使用。



![Image](assets/fr/022.webp)



## 6.备份 Seedkeeper



现在，我们要在第二个 Seedkeeper 上备份我的 Seedkeeper，这样就有了两份备份。这种冗余可以作为确保最重要密码安全的策略的一部分：例如，将种子管理器分别存放在两个不同的地方，以限制物理风险，或者将一份副本委托给值得信赖的亲戚。



为此，请带上你的第二个 Seedkeeper（记得在两个 Seedkeeper 中的一个上做上标记，以免混淆）。按照本教程第 3 步所述，首先对其进行初始化。再次，选择一个强大的 PIN 码。根据自己的策略，可以选择不同的 PIN 码，也可以保留相同的 PIN 码。



![Image](assets/fr/023.webp)



打开应用程序，点击 "*点击和扫描*"，输入 Seedkeeper n°1（信号源）的 PIN 码，然后扫描。



![Image](assets/fr/024.webp)



这将带你进入主页，上面有你的秘密列表。点击界面右上方的三个小圆点。



![Image](assets/fr/025.webp)



选择 "*制作备份*"，然后按 "*开始*"。



![Image](assets/fr/026.webp)



输入备份卡的 PIN 码（Seedkeeper n°2）。



![Image](assets/fr/027.webp)



然后扫描卡片。



![Image](assets/fr/028.webp)



对主卡（Seedkeeper n°1）做同样的操作，然后点击 "*制作备份*"。



![Image](assets/fr/029.webp)



现在，您的 Seedkeeper n°2 包含了 Seedkeeper n°1 中存储的所有秘密。



![Image](assets/fr/030.webp)



您可以扫描 Seedkeeper n°2，检查机密是否已被复制。



![Image](assets/fr/031.webp)



这就是全部内容！现在你知道如何使用 Seedkeeper 来存储密码了吧。在今后的教程中，我们将介绍如何使用 Seedkeeper 备份 Bitcoin wallet。我还会邀请你来了解它与 SeedSigner 的结合使用：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356