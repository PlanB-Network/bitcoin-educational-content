---
name: Satodime
description: 了解如何通过移动应用程序使用 Satodime
---
![cover](assets/cover.webp)



本指南指导您安装、配置和使用 Satodime 移动应用程序。您将学习如何持有您的银行卡、创建保险箱、添加资金、解封和恢复私钥。附录提供了资源、最佳实践和技术说明。



## 导言



**Satodime**由**[Satochip](https://satochip.io/fr/)**开发，是一种安全的不记名卡，用于以有形和简单的方式存储Bitcoin。它可以作为自我保管的 Hardware Wallet，您可以完全控制自己的私钥，而无需依赖第三方。它是开源的，并通过了 EAL6+ 认证，最多可支持三个独立的保险箱。



### 产品背景



Satodime 是一种**卡，属于任何实际拥有它的人**，无需事先注册或身份验证。它满足了对安全、便携式 Bitcoin 存储的需求，允许任何持有该卡的人通过手机应用程序扫描该卡来使用它或转移比特币，从而占有或解封保险箱。与纸质钞票不同，它使用安全芯片来Seal私钥，只有在解封后才会显示，这使得该卡类似于现金，Ownership由实际拥有情况决定。比特币卡是将比特币作为礼物赠送的理想选择，它有助于比特币在人与人之间的安全转移，而移动应用程序则利用近场通信技术实现智能手机的无障碍交互。





- 安全**：生成私钥并存储在防篡改芯片中；状态可见（密封、未密封、空）。
- 功能**：通过应用程序直接购买比特币（Paybis 合作伙伴）；管理 Mainnet 和 Testnet。
- 开源**：代码采用 AGPLv3 许可，可在 GitHub 上验证。



### 持续演变



应用程序定期更新。请查看 Satochip 网站或商店了解更新情况。例如，可能会添加新的区块链或购买功能。请查看 [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) 了解正在进行的开发。



## 1.先决条件



在开始使用**Satodime**之前，请确保您已准备好以下物品：





- 兼容的智能手机**：支持 NFC 功能的安卓或 iOS 设备。
- Satodime** 卡：新卡或未初始化。
- 互联网连接**：下载应用程序。
- 基础知识**：了解私人/公共密钥和丢失风险（不可逆转）。
- 安全介质**：用于记录解封后的私人密钥的安全场所（纸张、金属；绝不能是数字介质）。



## 2.安装





- 下载申请表** ：
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - 检查开发商（Satochip），避免受骗。
 - Satodime 是**开源**。源代码：[Satochip 的 GitHub](https://github.com/Toporin/Satodime-Applet)。





- 安装并启动应用程序**：如有必要，请激活手机上的 NFC。



![image](assets/fr/01.webp)



## 3.初始配置



### 3.1 启动应用程序并扫描



打开应用程序并按照向导操作。将 Satodime 卡放在手机的 NFC 读卡器上（通常在背面）。在整个操作过程中按住不放，以确保连接稳定。





- 如果 NFC 不工作，请检查手机设置。
- 祝酒词确认成功："成功阅读"。



![image](assets/fr/02.webp)



一般来说，** 下列所有操作都需要通过扫描 Satodime 卡进行确认**



### 3.2 保管卡片 (*Ownership*)



首次使用时，请成为卡的所有者，以确保安全：





- 点击应用程序中的 "*Take Ownership*"。
- 确认操作：生成唯一的所有者密钥。
- 再次扫描地图以应用更改。
- 警告**：此步骤不可逆转。请参阅 [*Ownership* 文章](https://satochip.io/satodime-Ownership-explained/)。



![image](assets/fr/03.webp)




## 4.创建一个安全的



Satodime 最多支持 3 个保险箱。创建一个用于存储 Bitcoin ：





- 选择一个空保险箱（如保险箱 01）。
- 选择 Blockchain (Bitcoin)。
- 点击 "*创建和 Seal*"。
- 将卡扫描至 generate 和 Seal 的私人密钥（解封前未知）。
- 恭喜**：您的保险箱现已封存，可随时接收资金。



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5.增加资金



密封后，将比特币装入保险箱：





- 选择保险箱。
- 点击 "*添加资金*"。
- 复制公共 Address 或扫描二维码。
- 从另一个 Wallet 发送资金。
- 在 Blockchain 上确认后检查余额。
- 购买选项：点击 "*购买*"，直接通过 Paybis（维萨卡、万事达卡等）购买。适用费用



![image](assets/fr/06.webp)



## 6.拆封保险箱



要获取私人密钥并将资金转移到其他地方，请打开保险箱的封条：





- 选择密封保险箱。
- 点击 "解除密封"。
- 确认警告：此操作不可逆转。
- 扫描卡片即可解封。
- 保险箱设置为 "*解封*"；现在可以查看/导出私钥。
- 警告**：一旦解封，私人密钥就可以访问。如果有人占有了您的智能手机，他们就可以访问该密钥，从而恢复保险箱中的资金（不可逆转）。



![image](assets/fr/07.webp)



## 7.恢复私人密钥



解封后，导出密钥供另一个 Wallet 使用：





- 确保您处于安全的环境中。
- 点击 "*显示私钥*"。
- 选择格式：传统格式、SegWit、WIF 等。
- 复制密钥或扫描二维码。
- 安全**：切勿共享您的私人密钥。离线存储。
- 将其导入与基金管理兼容的 Wallet 软件程序（如 Sparrow wallet 或 Electrum）。



![image](assets/fr/08.webp)





## 8.重置后备箱



重置保险箱会不可逆转地删除相关的私人密钥。换句话说，如果您没有备份私人密钥，或将其导入另一个 Wallet，重置保险箱将导致其中的资金不可逆转地损失。



![image](assets/fr/09.webp)



重置中继器后，插槽就会清空，并为新中继器做好准备。



## 9.转运 Ownership



例如，要通过 Satodime 提供比特币，您必须 ：




- 请使用 Ownership 号卡片、
- 创建一个 Bitcoin 保险箱、
- 把萨特转移到那里、
- 转移卡片 Ownership：下一个扫描卡片的人成为其所有者、
- 将 Satodime 卡交给您选择的人，请他们下载应用程序，然后扫描卡以获取 Ownership，从而获取 "存储 "在卡上的比特币。



![image](assets/fr/10.webp)




## 附录



### A1.最佳做法



要安全地使用 **Satodime** .NET Framework 2.0，请访问 **Satodime** .NET Framework 2.0：





- 确保卡的安全**：像对待现金一样对待它；如果不是失主，丢失 = 资金损失。
- 密钥备份**：解封后，将私人密钥记录在安全的物理介质上。绝不数字化。
- 检查状态**：始终扫描以确认卡 Ownership 和保险箱的密封/非密封状态。
- 保密**：使用新地址；避免集中交换转账。
- 更新**：通过商店更新应用程序。
- 找回**：如果卡丢失但仍在，则资金在 Blockchain 上；如果未封存，则使用私人密钥。



### A2.额外资源



具体到 Satodime ：




- [Satodime产品](https://satochip.io/fr/product/satodime/)
- [手机指南](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network](https://planb.network/) 有关自我保管、私钥等方面的教程。



**保存您的恢复短语** ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Satochip（品牌首款产品）教程：**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**种子管理人教程：**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3.关于 Satochip



**官方链接** ：




- [Satochip网站](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- 支持： info@satochip.io



**Satochip**是一家比利时公司，致力于开发用于管理和存储比特币及其他加密货币的硬件和软件解决方案。其旗舰产品 Satochip Hardware Wallet 是一款配备 EAL6+ 认证 secure element 的 NFC 卡。作为补充，Satochip 还推出了 Mnemonic 短语和密码管理器 Seedkeeper 和不记名卡 Satodime，可根据用户需求提供全面的产品系列。其设备由开源软件驱动，旨在实现 Bitcoin 安全的民主化。