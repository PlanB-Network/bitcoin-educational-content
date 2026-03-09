---
name: Seedkeeper
description: 如何使用 Seedkeeper 智能卡备份我的比特币钱包？
---

![cover](assets/cover.webp)

Seedkeeper 是一款由比利时公司 Satochip 开发的智能卡。Satochip 是一家专注于管理和保护数字密钥的硬件解决方案的公司。Satochip 以其面向比特币生态系统的智能卡系列而闻名，Seedkeeper 的设计旨在替代传统的助记词存储方式。

具体来说，Seedkeeper 是一款多功能、通过 EAL6 认证的智能卡，配备安全处理器和防篡改存储器（即所谓的“安全元件”）。顾名思义，它的作用是以加密和保护的方式存储比特币钱包的助记词和密码。使用 Seedkeeper，您可以直接在卡的加密组件中生成、导入、整理和保存您的密钥。

我认为 Seedkeeper 主要有两个用途，我们将在两篇教程中分别探讨：

- 比特币助记词存储：无需将 12 或 24 个单词写在纸上，您可以将它们导入智能卡并使用 PIN 码保护。
- 密码管理：您可以通过 Seedkeeper 应用程序生成强密码并直接存储在智能卡中，从而获得一个便捷易用的离线密码管理器。

从技术角度来看，Seedkeeper 的容量为 8192 字节，至少可以存储 50 个独立的密钥（具体数量取决于密钥的大小和与之关联的元数据）。您可以通过连接到计算机的智能卡读卡器访问 Seedkeeper，也可以通过带有 NFC 连接的移动应用程序访问。整个系统在离线模式下运行，无需互联网连接，从而最大限度地减少了攻击面。

![Image](assets/fr/001.webp)

一个特别有趣的功能是能够将一个 Seedkeeper 的内容复制到另一个 Seedkeeper，从而创建备份。在本教程中，我们将向您展示如何实现这一点。

Seedkeeper 与 SeedSigner 或 Specter DIY 等无状态钱包硬件结合使用时也非常有趣。在这种情况下，无需在电脑或手机上使用 Satochip 的客户端。Seedkeeper 将种子保存在其安全元件中，可以直接与签名设备一起使用，无需纸质二维码。本教程不会详细介绍这种使用场景，因为它是另一个专门教程的主题：

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1.Seedkeeper 有哪些用例？

在本教程中，我将只讨论与 Bitcoin 相关的用例，因为这正是本教程的主题。我们不会讨论密码管理功能，这将是另一个教程的主题。

## 1. Seedkeeper 的应用场景

本教程仅讨论与比特币相关的应用场景，因为本教程的主题就是比特币。我们不会深入探讨密码管理功能，该功能将在另一篇教程中介绍。

与简单的纸质助记词备份相比，使用 Seedkeeper 具有以下几个优势：

- **防盗**：钱包中的种子不会以明文形式存储。要提取种子，您需要知道 Seedkeeper 的 PIN 码。窃贼即使拿到设备，如果没有这个 PIN 码也无法进行任何操作。

- **分散风险**：您可以将安全措施分为数字层面和物理层面。例如，如果您将 Seedkeeper 的 PIN 码存储在密码管理器中，则需要同时访问该密码管理器并实际持有智能卡才能获取种子（大大降低了被攻击的可能性）。

- **集中管理**：** Seedkeeper 便于管理来自不同钱包的多个种子。

- **轻松备份**：**只需将加密备份复制到其他 SeedKeeper 设备即可。

然而，与简单的纸质助记词备份相比，SeedKeeper 存在一些缺点：

- **价格**：**虽然价格适中（约 25 欧元），但仍然高于一张纸的价格。

- **依赖通用计算设备**：输入和管理助记词需要使用电脑或智能手机，这意味着您的助记词会经过一台比钱包硬件更容易受到攻击的设备。如果该设备遭到入侵，则可能存在风险。因此，我不建议使用 SeedKeeper 来存储钱包硬件的助记词（除非像 SeedSigner 那样在无状态模式下使用，无需电脑）。钱包硬件的作用正是将助记词存储在一个极简且高度安全的环境中。如果您在常用电脑上手动输入助记词，它就不再局限于钱包硬件：它最终会存储在通用计算机上，暴露于多种攻击途径。因此，Seedkeeper 更适合用于热钱包而非冷钱包（SeedSigner/无状态钱包硬件除外）。

- **与 PIN 码相关的丢失风险**：与纸质备份不同，种子文件的直接不可访问性确实能有效防止物理盗窃。但安全始终需要在被盗风险和丢失风险之间取得平衡。如果您的备份需要 PIN 码，一旦丢失该代码，您将无法恢复助记词，从而无法访问您的比特币。

考虑到这些优缺点，我认为 Seedkeeper 的最佳用途（除了其密码管理功能之外）一方面是存储来自**软件钱包**的种子，因为它们已经存在于您的手机或电脑上，或者来自像 Satochip 这样的无屏幕钱包硬件；另一方面是将其与像 SeedSigner 这样的无状态钱包硬件结合使用，这样才能真正发挥其优势。

Seedkeeper 的另一个特别有趣的用途是安全可靠地备份钱包的*描述符*。

## 2. 如何购买 Seedkeeper？

获取 Seedkeeper 主要有两种方式。您可以直接从 [Satochip 官方商店购买](https://satochip.io/product/seedkeeper/)，也可以从授权经销商处购买。但由于 Seedkeeper 小程序是开源的（https://github.com/Toporin/Seedkeeper-Applet），您也可以选择将其安装到空白智能卡上（https://satochip.io/product/blank-javacard-for-diy-project/）。

如果您想使用 Seedkeeper 的备份功能，显然需要购买两张智能卡。

## 3. 安装 Seedkeeper 客户端

在本教程中，我们将使用 Seedkeeper 备份种子钱包。第一步是在您的电脑或智能手机上安装软件。在电脑上，您需要下载最新版本的 [Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases)。在移动设备上，Seedkeeper 应用可在 [Google Play 商店](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) 和 [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060) 下载。

![Image](assets/fr/002.webp)

## 4.种子管理器初始化

启动应用程序，点击 "*Click & Scan*" 按钮。

![Image](assets/fr/003.webp)

您将被要求输入种子管家的 PIN 码。由于这是一张新卡，因此尚未定义 PIN 码。请输入任意代码跳过这一步，然后点击 "*Next*"。

![Image](assets/fr/004.webp)

然后将卡片放在智能手机背面。应用程序会检测到 Seedkeeper 尚未初始化，并提示您设置智能卡的 PIN 码，长度为 4 到 16 个字符。为了获得最佳安全性，请选择尽可能长、随机且包含多种字符的强密码。此 PIN 码是防止他人物理接触您的恢复短语的唯一屏障。

**请务必立即保存此 PIN 码**，例如保存在密码管理器中，或保存在单独的物理介质上。如果是后者，切勿将包含 PIN 码的介质与 Seedkeeper 放在同一位置，否则此安全措施将失效。拥有可靠的备份至关重要：如果没有 PIN 码，您将无法恢复存储在 Seedkeeper 中的密钥。

![Image](assets/fr/005.webp)

再次确认 PIN 码。

![Image](assets/fr/006.webp)

Seedkeeper 已初始化。输入刚才设置的 PIN 码即可解锁。

![Image](assets/fr/007.webp)

现在您将进入智能卡管理页面。

![Image](assets/fr/008.webp)

## 5. 在 Seedkeeper 上注册助记词

解锁 Seedkeeper 后，点击 “+” 按钮。

![Image](assets/fr/009.webp)

选择 "Import secret*"。通过 "*Generate secret*" 选项，您可以直接在应用程序中创建新的记忆短语。

![Image](assets/fr/010.webp)

在我们的例子中，我们要将助记词保存在我们的钱包中。点击 "*Mnemonic*"。

![Image](assets/fr/011.webp)

为该机密指定一个 "*Label*"（标签），以便在 Seedkeeper 中存储多条信息时可以轻松识别。

![Image](assets/fr/012.webp)

然后在提供的字段中输入恢复短语。如果您愿意，还可以添加 BIP39 passphrase（密语）或您的 *描述符*。然后点击 "*Import*"。

![Image](assets/fr/013.webp)

*本图片中显示的助记词是虚构的，不属于任何人。它只是一个例子。切勿向任何人透露您自己的助记词，否则您的比特币将会被盗。

将 Seedkeeper 放在智能手机背面。

![Image](assets/fr/014.webp)

您的助记词已注册。

![Image](assets/fr/015.webp)

## 6.在 Seedkeeper 上访问您的助记词

如果您想检查您的记忆短语，请拿起 Seedkeeper，点击 "*Click & Scan*" 按钮。

![Image](assets/fr/016.webp)

输入密码，然后按 "*Next*"。

![Image](assets/fr/017.webp)

将 Seedkeeper 放在智能手机背面。

![Image](assets/fr/018.webp)

这将带您前往所有已注册秘密的列表。在本例中，我想显示 "*Blockstream App*" 钱包的种子，所以我点击它。

![Image](assets/fr/019.webp)

按下 "*Reveal*" 按钮。

![Image](assets/fr/020.webp)

再次扫描 Seedkeeper。

![Image](assets/fr/021.webp)

屏幕上将显示之前录制的助记词。

![Image](assets/fr/022.webp)

## 7.备份 Seedkeeper

现在我们要将我的 Seedkeeper 备份到第二个 Seedkeeper 上，这样就有了两份备份。这种冗余备份可以作为保护比特币策略的一部分：例如，将助记词存储在两个不同的地方以降低物理风险，或者将其中一份备份委托给值得信赖的亲属作为遗产计划的一部分。

为此，请携带您的第二个 Seedkeeper（记得在其中一个上做标记，以免混淆）。首先，按照本教程步骤 4 中的说明初始化它。再次选择一个强密码。根据您的策略，您可以选择不同的密码，也可以使用相同的密码。

![Image](assets/fr/023.webp)

打开应用程序，点击 "*Click & Scan*"，输入 Seedkeeper n°1（源）的密码，然后扫描。

![Image](assets/fr/024.webp)

这将带您进入主页，其中会显示您的密钥列表。点击界面右上角的三个小点。

![Image](assets/fr/025.webp)

选择 "*Make a backup*"，然后按 "*Start*"。

![Image](assets/fr/026.webp)

输入备份卡的 PIN 码（Seedkeeper n°2）。

![Image](assets/fr/027.webp)

然后扫描卡片。

![Image](assets/fr/028.webp)

对主卡（Seedkeeper n°1）做同样的操作，然后点击 "*Make a backup*"。

![Image](assets/fr/029.webp)

现在，您的 Seedkeeper n°2 包含了 Seedkeeper n°1 中存储的所有秘密。

![Image](assets/fr/030.webp)

您可以扫描 Seedkeeper n°2，检查机密是否已被复制。

![Image](assets/fr/031.webp)

就是这样！现在您知道如何使用 Seedkeeper 保存比特币钱包的助记词了。在以后的教程中，我们将介绍如何使用 Seedkeeper 存储您的密码。我还邀请您探索它与 SeedSigner 的结合使用：

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

在本教程中，我们多次提到比特币钱包中的“描述符”（Descriptors）。如果您不了解它们是什么，我建议您参加我们的免费 CYP 201 培训课程，该课程将深入讲解分层确定性钱包（HD Wallet）运行所涉及的所有机制！

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
