---
name: Bitcoin Keeper
description: Bitcoin 移动式 wallet 用于安全，multi-sig 用于安全
---

![cover](assets/cover.webp)



对于任何意识到金融主权利害关系的持有者来说，比特币的安全管理都是一项重大挑战。在移动 wallet 的简易性和 multi-sig 解决方案的稳健性之间，技术差距似乎令许多用户望而生畏。Bitcoin Keeper 正是定位在这一交叉点上，提供一种渐进的安全方法，伴随用户的发展。



Bitcoin Keeper 是一款开源移动应用程序，由 BitHyve 团队开发，专门用于 Bitcoin。它的目标是在为初学者提供直观界面的同时，实现高级投资组合管理，尤其是多签名配置。该应用程序的口号是 "保障今天，规划明天"，体现了其长期支持的理念。



与管理多种加密货币的通用钱包不同，Bitcoin Keeper 严格专注于 Bitcoin。这种只针对比特币的方法减少了潜在的攻击面，大大简化了用户体验。该应用程序的另一个突出特点是原生集成了最普遍的硬件钱包和先进的 UTXO 管理功能。



## 什么是 Bitcoin Keeper？



### 理念和目标



Bitcoin Keeper 的设计旨在满足比特币用户希望完全控制其私钥的特殊需求。该项目完全遵循 Bitcoin 的基本原则：开放和可审计的源代码、尊重隐私和用户主权。使用该应用程序无需注册或提供个人信息，甚至可以离线运行进行签名操作。



其核心目标是提供一种灵活、面向未来的工具，通过继承功能将 BTC 储存数年甚至数代。该应用程序使用户能够从简单的移动 wallet 开始，然后逐步发展为更安全的多重签名解决方案。



### 应用架构



Bitcoin Keeper 围绕两个不同的概念组织资金管理。**Hot Wallet** 是一个简单的单键 wallet，存储在手机上，专为日常支出和少量金额而设计。保险箱**是多签名（多钥匙）保险箱，需要多把钥匙才能授权支出，专为长期安全存储而设计。



### 主要特点



Bitcoin Keeper 支持市场上几乎所有的硬件钱包：Coldcard、Trezor、Ledger、Keystone、BitBox02、Jade、Seedsigner、Passport 和 Coinkite 的 Tapsigner。根据设备的不同，集成方式也不同：二维码扫描、NFC 连接或文件导入。



该应用程序还提供先进的 UTXO 管理功能，包括交易标签、发送时手动选择输入的硬币控制，以及部分签名交易的 PSBT 格式支持。



## 安装和初始配置



Bitcoin Keeper 可通过 Google Play Store 在 Android 上免费下载，也可通过 App Store 在 iOS 上免费下载。其中列出的发行商是 BitHyve。安装前，请确保您的设备没有恶意软件，是最新版本，且未被root或越狱。



首次启动时，应用程序会要求您创建一个安全 PIN 码。该密码可保护对 wallet 的访问，并对本地敏感数据进行加密。选择一个强大的密码并记住它。然后，您可以激活生物识别身份验证（指纹或 Face ID），以加快解锁速度。



![Installation et configuration du PIN](assets/fr/01.webp)



然后，应用程序会显示几个介绍性屏幕，解释其三大支柱：创建 wallet 发送和接收比特币、兼容硬件 wallet 的密钥管理以及传承比特币的传统计划。按下 "开始"，然后选择 "新建 "创建新配置。



![Écrans d'introduction](assets/fr/02.webp)



## 发现接口



Bitcoin Keeper 的界面围绕四个主要选项卡展开，可从底部导航栏进入：



![Les quatre onglets de l'application](assets/fr/03.webp)



钱包**选项卡显示您的钱包及其余额。您可以在这里访问您的钱包，发送和接收比特币。标签 "Hot Wallet "和 "单钥 "或 "多钥 "可让您快速识别每个 wallet 的类型。



密钥**选项卡集中管理您的签名密钥。在这里，您可以找到应用程序生成的移动密钥，以及从硬件钱包导入的所有密钥。您还可以在这里添加新的签名设备。



**Concierge** 标签提供支持服务：向支持团队提交问题，并与 Bitcoin 顾问联系以获得个性化帮助。



在 **More**（更多选项）选项卡中，可以访问个人服务器连接、密钥备份、继承文件、显示首选项和 wallet 管理等设置。



## 连接自己的服务器



为了加强保密性，Bitcoin Keeper 允许您将应用程序连接到自己的 Electrum 服务器，而不是使用默认的公共服务器。



![Configuration du serveur Electrum](assets/fr/04.webp)



从 "更多 "选项卡向下滚动，找到服务器设置。按 "添加服务器 "配置新连接。您可以在 "公共服务器"（预配置的公共服务器）和 "私人 Electrum"（您自己的服务器）之间进行选择。



对于专用服务器，请输入 URL（如 Umbrel 节点的 umbrel.local）和端口号（通常为 50001）。如果服务器支持 SSL，则激活 SSL。您也可以扫描配置 QR 代码。输入参数后，按 "连接到服务器"。



如果您还没有自己的 Bitcoin 结，请看看我们关于 Umbrel 的教程，这是一种简单而实惠的自编绳结的方法：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## 接收比特币



从 "钱包 "选项卡中选择要接收资金的 wallet，按下该按钮。wallet 屏幕会显示余额和三个操作按钮：发送 Bitcoin、接收 Bitcoin 和查看所有硬币。



![Réception de bitcoins](assets/fr/05.webp)



按 "接收 Bitcoin"。Bitcoin Keeper 将以 Bech32 格式生成一个新的接收地址（以 bc1... 开始）及其 QR 码。您可以在该地址上添加标签，以识别资金来源。通过显示 QR 代码或复制文本地址，与发件人共享该地址。



应用程序会为每次接收自动生成一个新地址，以保护您的隐私。如有必要，可使用 "获取新 Address "获取空白地址。



## UTXO 管理



Bitcoin Keeper 可全面查看构成余额的 UTXO（未使用的交易输出）。在 wallet 屏幕上，按 "查看所有硬币 "进入角落管理器。



![Gestion des UTXO](assets/fr/06.webp)



管理硬币 "屏幕单独列出每枚 UTXO 及其数量和标签。通过该视图，您可以追踪硬币的来源并对其进行整理。您可以通过 "选择发送 "选择特定的UTXO，与硬币控制一起发送，从而避免不同来源的硬币混在一起。



## 发送比特币



要发送，请选择源组合，然后按 "发送 Bitcoin"。输入目的地地址（粘贴或通过 QR 码扫描），并可选择添加标签以识别收件人。



![Envoi de bitcoins](assets/fr/07.webp)



下一个界面允许您输入要发送的金额。界面会显示您的可用余额和法币换算。选择收费优先级：低（经济，~60 分钟）、中或高（优先）。实时显示以 sats/vbyte 为单位的估计费用。按 "发送 "继续。



![Confirmation et envoi](assets/fr/08.webp)



摘要屏幕显示所有详细信息：wallet 来源、目的地地址、交易优先级、网络费用、发送金额和总额。请仔细检查这些信息，因为 Bitcoin 交易是不可逆的。按 "确认并发送 "发送交易。



系统会显示 "发送成功 "确认，并附带完整的摘要。在 "最近交易 "历史记录中可以看到交易及其标签。



## 保存钥匙



备份恢复密钥是关键的一步。从 "更多 "选项卡进入 "备份和恢复 "部分，点击 "恢复密钥"。



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



屏幕会显示备份状态。要验证备份，应用程序会要求您确认短语中的某个特定单词（如第 7 个单词）。该验证可确保您正确填写了恢复短语。



在 "恢复密钥设置 "中，您可以通过 "查看恢复密钥 "查看完整的短语，并查看密钥的签名者指纹。将 12 字短语保存在纸张上，放在安全的地方，远离潮湿和火源。切勿将其存储在已连接的设备上。



## 添加外部密钥（wallet 硬件）



Bitcoin Keeper 的主要优势之一是集成了硬件钱包。在 "密钥 "选项卡中，按 "添加密钥 "可添加新的签名设备。



![Ajout d'une clé hardware](assets/fr/10.webp)



选择 "从硬件添加密钥 "连接硬件 wallet。应用程序支持多种设备：BitBox02、Coldcard、Blockstream Jade、Keystone、Krux、Ledger、Foundation Passport、TwentyTwo Portal、Seedsigner 和 Specter Solutions。



### Tapsigner 配置



Tapsigner 是 Coinkite 推出的一款 NFC 卡，特别适用于移动设备。如果您想了解更多信息，我们有专门的教程：



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

要添加 Tapsigner，请从硬件钱包列表中选择它。



![Configuration du Tapsigner](assets/fr/11.webp)



首先输入印在卡背面的 6-32 位 PIN 码（新卡的默认值），如果已经配置，则输入您的 PIN 码。按 "Proceed（继续）"，然后在显示 "Ready to scan（准备扫描）"时将 Tapsigner 靠近手机背面。NFC 通信会自动导入公钥。然后您可以添加一个描述（如 "Métro Card"）来识别该密钥。



## 创建多标识组合



设置好密钥后，就可以创建一个结合多个设备的多重签名 wallet。从 "钱包 "标签，点击 "添加 Wallet"。



![Création d'un nouveau wallet](assets/fr/12.webp)



您有三个选项："创建 Wallet "用于新组合，"导入 Wallet "用于恢复现有的 wallet，或 "协作 Wallet "用于共享保险库。选择 "创建 Wallet"，然后选择 "Bitcoin Wallet"。



![Sélection du type de wallet](assets/fr/13.webp)



下一个屏幕提供不同的配置："单键"、"2 of 3 多键 "或 "3 of 5 多键"。如需自定义 multi-sig，请按 "选择自定义设置"。例如，选择 "1 of 2"：需要从两个可能的按键中选择一个签名。



然后选择组成 Vault 的密钥。在我们的例子中，我们将 "移动密钥"（手机软件密钥）和 "TAPSIGNER"（地铁卡）结合在一起。这种配置具有冗余性：如果其中一个密钥无法使用，您可以随时使用另一个密钥进行消费。



![Finalisation du wallet multisig](assets/fr/14.webp)



为您的 wallet 命名（如 "测试计划 B"），添加可选描述，并选中所选按键。按 "创建 Wallet"。此时会出现 "Wallet 创建成功 "的确认信息，提醒您保存 wallet 恢复文件。



新的多密钥 wallet 现在会出现在 "钱包 "选项卡中，标签为 "多密钥"，并显示 "1 of 2"。



### 保存配置文件



**简单的 wallet 只需恢复短语即可恢复访问，而 wallet multisig 则不同，它还需要配置文件来描述保险箱的结构（哪些密钥参与、需要多少签名）。如果没有该文件，即使使用了所有恢复短语，也无法重建 wallet。



![Export du fichier de configuration](assets/fr/15.webp)



要导出此文件，请在 "钱包 "选项卡中选择您的 wallet 多 ID，然后按右上角的 "设置 "图标（齿轮）。在 "Wallet 设置 "中点击 "Wallet 配置文件"。有几种导出选项可供选择：





- 导出 PDF**：生成包含所有 wallet 信息的 PDF 文档
- 显示 QR**：显示可扫描的 QR 代码，以便将配置导入到其他设备上
- 空投/文件导出**：通过手机的共享选项导出文件
- NFC**：通过 NFC 与兼容设备共享



将此配置文件与您的恢复短语分开保存，最好保存在加密或打印介质上。如果您丢失了手机，该文件和每个参与密钥的恢复短语将使您能够在 Bitcoin Keeper 或任何其他兼容软件上重建 wallet 多密钥。



## 最佳做法



### 基金组织



根据比特币的用途安排比特币的结构：一个热门的 wallet Single-Key 用于金额有限的当前支出，一个或多个 Vaults Multi-Key 用于长期储蓄。系统化的 UTXO 标签可以帮助你追踪资金的来源，这对于管理保密性和避免不同来源的比特币混在一起特别有用。



确保手机安全：激活生物识别锁，定期执行系统更新，对已安装的应用程序保持警惕。并随时更新 Bitcoin Keeper 的安全补丁。



### 备份安全



在纸张上至少保存两份每个恢复短语的副本，存放在不同的地理位置。对于大额资金，可考虑刻上抗灾金属字样。切勿将这些短语存储在连接互联网的设备上，也切勿对其拍照。



对于 multi-sig 保险库，还需保存配置文件（Wallet 恢复文件），其中包含参与的公开密钥和保险库结构。该文件与密钥恢复短语相结合，可在任何兼容软件（如 Sparrow 或 Specter）上重建 wallet。



## 优势和局限性



### 亮点





- 仅 Bitcoin 应用可降低复杂性和风险
- 原生集成多数据库，并提供逐步指导
- 扩展硬件 wallet 支持（Tapsigner、Coldcard、Ledger、Jade 等）
- 先进的 UTXO 管理和硬币控制
- 可连接到个人 Electrum 服务器
- 开放、可审计的源代码



### 需要考虑的制约因素





- Interface 主要使用英语
- 某些高级功能（云备份、辅助服务器）需要升级
- Multisig 配置需要初始培训



## 结论



Bitcoin Keeper 是管理比特币的可扩展解决方案。从简单的热钱包 wallet 到多签名金库，Bitcoin Keeper 采用了渐进式方法，这意味着可以根据需求变化升级安全性。轻松集成 Tapsigner 等硬件钱包的能力为实现强大的配置而不过度复杂铺平了道路。



只使用比特币、开放源代码和尊重隐私使其与 Bitcoin 生态系统的核心价值相一致。



本教程涵盖免费版 Bitcoin Keeper 的基本功能。该应用程序还提供高级功能（云备份、辅助服务器备份、金丝雀钱包），这将是专门教程的主题。在即将推出的指南中，我们还将探讨继承规划功能，借助集成在应用程序中的 "增强型保险库 "和随附文件，该功能可让您为向亲人传输比特币做好准备。



## 资源





- 官方网站：[bitcoinkeeper.app](https://bitcoinkeeper.app)
- 帮助中心：[help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- 源代码：[github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)