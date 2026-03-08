---
name: Satodime
description: 了解如何通过移动应用程序使用 Satodime
---
![cover](assets/cover.webp)

本指南将指导您安装、配置和使用 Satodime 移动应用程序。您将学习如何领取您的卡片、创建保险箱、充值、解封和找回您的私钥。附录提供了相关资源、最佳实践和技术说明。

## 导言

**Satodime** 由 **[Satochip](https://satochip.io/fr/)** 开发，是一款安全便捷的比特币存储卡，让您以直观易用的方式存储比特币。它是一款自托管钱包硬件，让您完全掌控自己的私钥，无需依赖任何第三方。Satodime 开源且通过 EAL6+ 认证，最多支持三个独立的保险箱。

### 产品背景

Satodime 是一款**便携式卡**，所有权归持有者所有，无需事先注册或身份验证。它满足了安全便携的比特币存储需求，任何持有者都可以通过手机应用程序扫描卡片来使用或转移比特币，从而获得比特币或解锁保险箱。与纸币不同，Satodime 使用安全芯片密封私钥，只有在解锁后才能显示私钥，使其类似于现金，所有权由实际持有决定。 Satochip 是赠送比特币的理想之选，它能安全地实现比特币的即时转账，同时其移动应用程序利用 NFC 技术，方便用户通过智能手机进行交互。

- **安全**：私钥生成并存储在防篡改芯片中；状态可见（已密封、未密封、空）。
- **功能**：通过应用程序直接购买比特币（Paybis 合作伙伴）；管理主网和测试网。
- **开源**：代码采用 AGPLv3 许可证，可在 GitHub 上验证。

### 持续演变

应用程序定期更新。请查看 Satochip 网站或商店了解更新信息。例如，可能会添加新的区块链或购买功能。请查看[Satochip GitHub](https://github.com/Toporin/Satodime-Applet)，了解正在进行的开发。

该应用程序会定期更新。请访问 Satochip 网站或商店查看更新。例如，可能会添加新的区块链或购买功能。请访问 [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) 查看最新开发进展。

## 1. 前提条件

开始使用 **Satodime** 之前，请确保您拥有以下物品：

- **兼容的智能手机：支持 NFC 功能的 Android 或 iOS 设备。
- **Satodime** 卡：全新或未初始化。
- **互联网连接**：用于下载应用程序。
- **基本知识**：了解私钥/公钥及其丢失风险（不可逆）。
- **安全介质**：用于安全记录已解封私钥的容器（纸张、金属；切勿使用数字存储）。

## 2.安装

- **下载应用程序** ：
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - 检查开发商（Satochip），避免受骗。
 - Satodime 是**开源**的。源代码：[Satochip 的 GitHub](https://github.com/Toporin/Satodime-Applet)。

- **安装并启动应用程序**：如有必要，激活手机上的 NFC。

![image](assets/fr/01.webp)

## 3.初始配置

### 3.1 启动应用程序并扫描

打开应用程序并按照向导操作。将 Satodime 卡放在手机的 NFC 读取器上（通常在背面）。操作过程中请按住卡片，以确保连接稳定。

- 如果 NFC 无法工作，请检查手机设置。

- 成功后会弹出提示："Successful reading"。

![image](assets/fr/02.webp)

通常情况下，**以下所有操作都需要扫描 Satodime 卡进行确认**

### 3.2 获取卡片所有权

首次使用时，请先获取卡片所有权以确保卡片安全：

- 在应用程序中点击 “Take Ownership”。
- 确认操作：这将生成一个唯一的卡主密钥。
- 再次扫描地图以应用更改。
- 警告：此步骤不可逆。请参阅[关于*所有权*的文章](https://satochip.io/satodime-ownership-explained/)。

![image](assets/fr/03.webp)

## 4.创建保险箱（safe）

Satodime 最多支持 3 个保险箱。创建一个用于存储比特币：

- 选择一个空的保险箱（例如，保险箱 01）。
- 选择区块链（Bitcoin）。
- 点击 “*Create & Seal*”。
- 扫描卡片以生成并密封私钥（在解封之前未知）。
- 恭喜！您的保险箱现已密封，可以接收资金。

![image](assets/fr/04.webp)

![image](assets/fr/05.webp)

## 5.增加资金

保险箱封存后，即可向其中充值比特币：

- 选择保险箱。
- 点击 “*Add funds*”。
- 复制公钥地址或扫描二维码。
- 从其他钱包发送资金。
- 区块链确认后，查看余额。
- 购买选项：点击 “*Purchase*” 即可通过 Paybis（Visa、Mastercard 等）直接购买。需支付相关费用。
![image](assets/fr/06.webp)

## 6. 解锁保险箱

为了访问私钥并将资金转移到其他位置，请解锁保险箱：

- 选择已封存的保险箱。
- 点击 “Unseal”。
- 确认警告：此操作不可逆。
- 扫描卡片以解锁。
- 保险箱状态变为 “*Unsealed*”；现在可以查看/导出私钥。
- **警告**：私钥一旦解封即可访问。如果有人拿到您的智能手机，他们就能访问此密钥，从而找回您保险箱中的资金（此操作不可逆）。

![image](assets/fr/07.webp)

## 7.恢复私钥

解封后，导出私钥以便在其他钱包中使用：

- 确保您处于安全的环境中。
- 点击 “*Show private key*”。
- 选择格式：Legacy、SegWit、WIF 等。
- 复制私钥或扫描二维码。
- 安全提示：切勿共享您的私钥。请将其离线保存。
- 将其导入与资金管理兼容的钱包软件（例如 Sparrow Wallet 或 Electrum）。

![image](assets/fr/08.webp)

## 8.重置保险箱

重置保险箱会永久删除关联的私钥。换句话说，如果您没有备份私钥或将其导入其他钱包，重置保险箱将导致其中的资金永久丢失。

![image](assets/fr/09.webp)

重置保险箱后，保险箱即可清空，准备插入新的保险箱。

## 9.转移所有权

例如，为了通过 Satodime 提供比特币，您必须：

- 获得卡的所有权，
- 创建一个比特币保险箱，
- 将聪（比特币）转入该保险箱，
- 转移卡的所有权：下一个扫描该卡的人将成为卡的所有者，
- 将 Satodime 卡交给您选择的人，并邀请他们下载应用程序，然后扫描该卡以获取其所有权，从而访问卡上“存储”的比特币。

![image](assets/fr/10.webp)

## 附录

### A1.最佳做法

安全使用 **Satodime**：

- **安全保管卡片**：像对待现金一样对待卡片；如果卡片丢失且非持卡人本人，则资金将丢失。
- **密钥备份**：解封后，将私钥记录在安全的物理介质上。切勿使用数字方式。
- **检查状态**：始终扫描卡片以确认持卡人身份以及保险箱的密封/未密封状态。
- **保密性**：使用新地址；避免使用中心化交易所进行转账。
- **更新**：通过应用商店保持应用程序更新。
- **找回**：如果卡片丢失但持卡人本人在场，资金已存储在区块链上；如果卡片已开封，则使用私钥进行找回。

### A2.其他资源

具体到 Satodime ：

- [Satodime 产品](https://satochip.io/fr/product/satodime/)
- [移动端指南](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)

[Plan ₿ Academy](https://planb.academy/)提供关于自我保管、私钥等方面的教程。

**保存您的助记词** ：

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Satochip（该品牌的首款产品）教程** :

https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Seedkeeper 教程：**

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3.关于 Satochip

**官方链接** ：

- [Satochip 网站](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- 支持：info@satochip.io

**Satochip** 是一家比利时公司，致力于开发用于管理和存储比特币及其他加密货币的软硬件解决方案。其旗舰产品 Satochip 硬件钱包是一款配备 EAL6+ 认证安全元件的 NFC 卡。此外，Satochip 还提供 Seedkeeper（助记词和密钥管理器）以及 Satodime（存储卡），以满足用户的各种需求。Satochip 的设备基于开源软件，旨在普及比特币安全。
