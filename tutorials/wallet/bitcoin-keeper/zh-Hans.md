---
name: Bitcoin Keeper
description: 用于安全和多重签名的比特币移动钱包
---

![cover](assets/cover.webp)



对于任何意识到金融主权所涉利害关系的持有者来说，比特币的安全管理是一项重大挑战。移动钱包的简单性和多重签名解决方案的稳健性之间的技术差距对于许多用户来说似乎令人望而生畏。 Bitcoin Keeper 正是处于这个十字路口，提供了一种渐进的安全方法，伴随着用户的发展。


Bitcoin Keeper 是一款专门针对比特币的开源移动应用程序，由 BitHyve 团队开发。它的目标是使高级资产管理变得易于访问，特别是多重签名配置，同时为初学者保持直观的界面。该应用程序采用的口号是“确保今天的安全，规划明天”，体现了其长期支持的理念。


与管理多种加密货币的通用钱包不同，Bitcoin Keeper 严格关注比特币。这种仅限比特币的方法减少了潜在的攻击面并极大地简化了用户体验。该应用程序还因其对最广泛的硬件钱包的原生集成及其先进的 UTXO 管理功能而脱颖而出。



## 何为 Bitcoin Keeper？



### 理念和目标



Bitcoin Keeper 的设计旨在满足比特币用户希望完全控制其私钥的特殊需求。该项目完全遵循比特币的基本原则：开放和可审计的源代码、尊重隐私和用户主权。使用该应用程序无需注册或提供个人信息，甚至可以离线运行进行签名操作。



其核心目标是提供一种灵活、面向未来的工具，通过继承功能将比特币储存数年甚至数代。该应用程序使用户能够从简单的移动钱包开始，然后逐步发展为更安全的多重签名解决方案。



### 应用程序的架构



Bitcoin Keeper 围绕两个不同的概念组织资金管理。**热钱包** 是一个简单的单密钥钱包，存储在手机上，专为日常支出和少量金额而设计。**保险箱** 是多签名的（多密钥的），需要多个密钥才能授权支出，专为长期安全存储而设计。



### 主要功能



Bitcoin Keeper 支持市场上几乎所有的硬件钱包：Coldcard、Trezor、Ledger、Keystone、BitBox02、Jade、Seedsigner、Passport 和 Coinkite 的 Tapsigner。根据设备的不同，集成方式也不同：二维码扫描、NFC 连接或文件导入。



该应用程序还提供先进的 UTXO 管理功能，包括交易标签、发送时手动选择输入的币控制，以及部分签名交易的 PSBT 格式支持。



## 安装和初始配置



Bitcoin Keeper 可通过 Google Play Store 在 安卓上免费下载，也可通过 App Store 在 iOS 上免费下载。其中列出的发行商为 BitHyve。安装前，请确保您的设备没有恶意软件，是最新的版本，并且设备系统处于安全、未改动的状态。



首次启动时，应用程序会要求您创建一个安全 PIN 码。该密码可保护对钱包的访问，并对本地敏感数据进行加密。选择一个强大的密码并记住它。然后，您可以激活生物识别身份验证（指纹或 Face ID），以加快解锁速度。



![Installation et configuration du PIN](assets/fr/01.webp)



然后，应用程序会显示几个介绍性屏幕，解释其三大支柱：创建钱包发送和接收比特币、兼容硬件钱包的密钥管理以及传承比特币的传统计划。按下 "Get Started"，然后选择 "Start New" 以创建新配置。



![Écrans d'introduction](assets/fr/02.webp)



## 了解应用程序的界面



Bitcoin Keeper 的界面围绕四个主要选项卡展开，可从底部导航栏进入：



![Les quatre onglets de l'application](assets/fr/03.webp)



**Wallet** 选项卡显示您的钱包及其余额。您可以在这里访问您的钱包，发送和接收比特币。"Hot Wallet" 和 "Single-Key" 或 "Multi-Key" 标签可让您快速识别每个钱包的类型。



**Keys**选项卡集中管理您的签名密钥。在这里，您可以找到应用程序生成的移动密钥，以及从硬件钱包导入的所有密钥。您还可以在这里添加新的签名设备。



**Concierge** 标签提供支持服务：向支持团队提交问题，并与比特币顾问联系以获得个性化帮助。



在 **More**（更多选项）选项卡中，可以访问个人服务器连接、密钥备份、继承文件、显示首选项和钱包管理等设置。



## 连接自己的服务器



为了加强您的保密性，Bitcoin Keeper 允许您将应用程序连接到自己的 Electrum 服务器，而不是使用默认的公共服务器。



![Configuration du serveur Electrum](assets/fr/04.webp)



从 "More" 选项卡向下滚动，找到服务器设置。按 "Public Server" 配置新连接。您可以在 "公共服务器"（预配置的公共服务器）和 "私人 Electrum"（您自己的服务器）之间进行选择。



对于专用服务器，请输入 URL（如 Umbrel 节点的 umbrel.local）和端口号（通常为 50001）。如果服务器支持 SSL，则激活 SSL。您也可以扫描配置 QR 代码。输入参数后，按 "连接到服务器"。



如果您还没有自己的 Bitcoin 结，请看看我们关于 Umbrel 的教程，这是一种简单而实惠的自编绳结的方法：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## 接收比特币



在 "Wallets" 选项卡中选择要接收资金的钱包，按下该按钮。钱包屏幕会显示余额和三个操作按钮：Send Bitcoin、Receive Bitcoin 和 View All Coins。



![Réception de bitcoins](assets/fr/05.webp)



按 "Recieve Bitcoin"。Bitcoin Keeper 将以 Bech32 格式生成一个新的接收地址（以 bc1... 为开始）及其二维码。您可以在该地址上添加标签，以识别资金来源。通过显示二维码或复制文本地址，与发送者共享该地址。



应用程序会为每次接收自动生成一个新地址，以保护您的隐私。如有必要，可使用 "Get New Address" 获取空白地址。



## UTXO 管理



Bitcoin Keeper 可让您查看构成余额的 UTXO（未花费的交易输出）。在钱包屏幕上，按 "View All Coins" 进入 UTXO 管理屏幕。



![Gestion des UTXO](assets/fr/06.webp)



“Manage Coins” 屏幕单独列出每个 UTXO 及其数量和标签。通过该界面，您可以追踪比特币的来源并对其进行整理。您可以通过 "Select to Send" 选择特定的 UTXO，与币控制一起发送，从而避免不同来源的比特币混在一起。



## 发送比特币



如果您想要发送比特币，请选择源钱包，然后按 "Send Bitcoin"。输入目的地地址（粘贴或通过二维码扫描），并可选择添加标签以识别接收者。



![Envoi de bitcoins](assets/fr/07.webp)



下一个界面允许您输入要发送的金额。界面会显示您的可用余额和法币换算。选择收费优先级：Low（ ~60 分钟）、Mediun 或 High（优先）。实时显示以 sats/vbyte 为单位的估计费用。按 "Send" 继续。



![Confirmation et envoi](assets/fr/08.webp)



摘要屏幕显示所有详细信息：钱包来源、目的地地址、交易优先级、网络费用、发送金额和总额。请仔细检查这些信息，因为比特币交易是不可逆的。按 "Confirm & Send" 以发送交易。



系统会显示 "Send Successful" 确认，并附带完整的摘要。在 "Recent Transaction" 历史记录中可以看到交易及其标签。



## 保存密钥



备份恢复密钥是关键的一步。在 "More" 选项卡进入 "Backup and Recovery" 部分，点击 "Recovery Key"。



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



屏幕会显示备份状态。要验证备份，应用程序会要求您确认助记词中的某个特定单词（如第 7 个单词）。该验证可确保您正确填写了助记词。



在 "Recovery Key Settings" 中，您可以通过 "View Recovery Key" 查看完整的助记词，并查看密钥的签名者指纹。将 12 字助记词保存在纸张上，放在安全的地方，远离潮湿和火源。切勿将其存储在已连接的设备上。



## 添加外部密钥（硬件钱包）



Bitcoin Keeper 的主要优势之一是集成了硬件钱包。在 "Keys" 选项卡中，按 "Add key" 可添加新的签名设备。



![Ajout d'une clé hardware](assets/fr/10.webp)



选择 "Add key from a hardware" 连接硬件钱包。应用程序支持多种设备：BitBox02、Coldcard、Blockstream Jade、Keystone、Krux、Ledger、Foundation Passport、TwentyTwo Portal、Seedsigner 和 Specter Solutions。



### Tapsigner 配置



Tapsigner 是 Coinkite 推出的一款 NFC 卡，特别适用于移动设备。如果您想了解更多信息，我们有专门的教程：



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

为了添加 Tapsigner，请从硬件钱包列表中选择它。



![Configuration du Tapsigner](assets/fr/11.webp)



首先输入印在卡背面的 6-32 位 PIN 码（新卡的默认值），如果已经配置，则输入您的 PIN 码。按 "Proceed"，然后在显示 "Ready to scan" 时将 Tapsigner 靠近手机背面。NFC 通信会自动导入公钥。然后您可以添加一个描述（如 "地铁卡"）来识别该密钥的用途。



## 创建多签名钱包



设置好密钥后，就可以创建一个结合多个设备的多重签名钱包。在 "Wallets" 标签中，点击 "Add Wallet"。



![Création d'un nouveau wallet](assets/fr/12.webp)



您有三个选项："Create Wallet"，用于创建新钱包，"Import Wallet" 用于恢复现有的钱包，或 "Collaborative Wallet" 用于共享保险库。选择 "Create Wallet"，然后选择 "Bitcoin Wallet"。



![Sélection du type de wallet](assets/fr/13.webp)



下一个屏幕显示不同的配置："Single-key"、"2 of 3 multi-key" 或 "3 of 5 multi-key"。如需自定义 multi-sig，请按 "Select custom setup"。例如，选择 "1 of 2"：需要从两个可能的按键中选择一个签名。



然后选择组成 Vault 的密钥。在我们的例子中，我们将 "移动密钥"（手机软件密钥）和 "TAPSIGNER"（地铁卡）结合在一起。这种配置具有冗余性：如果其中一个密钥无法使用，您可以随时使用另一个密钥进行消费。



![Finalisation du wallet multisig](assets/fr/14.webp)



为您的 wallet 命名（如 "测试计划 B"），添加可选描述，并选中所选按键。按 "创建 Wallet"。此时会出现 "Wallet 创建成功 "的确认信息，提醒您保存 wallet 恢复文件。



新的多密钥 wallet 现在会出现在 "钱包 "选项卡中，标签为 "多密钥"，并显示 "1 of 2"。



### 保存配置文件



**简单的钱包只需恢复助记词即可恢复访问，而多签名钱包则不同，它还需要配置文件来描述保险箱的结构（相关的密钥、需要多少签名）。如果没有该文件，即使使用了所有恢复助记词，也无法恢复钱包。



![Export du fichier de configuration](assets/fr/15.webp)



为了导出此文件，请在 "Wallets" 选项卡中选择您的钱包，然后按右上角的 "Settings" 图标（齿轮）。在 "Wallet Settings" 中点击 "Wallet configuration file"。有几种导出选项可供选择：

- **PDF export**：生成包含所有钱包信息的完整文档
- **Show QR**：显示二维码，以便在其他设备上导入配置
- **Airdrop / File Export**：通过共享选项导出文件
- **NFC**：通过 NFC 与兼容设备共享

将此配置文件与您的恢复助记词分开保存，最好保存在加密或打印介质上。如果您丢失了手机，该文件和每个相关密钥的恢复助记词将使您能够在 Bitcoin Keeper 或任何其他兼容软件上恢复您的多签名钱包。



## 最佳做法



### 资金管理



根据比特币的用途安排比特币的结构：一个热门的单密钥钱包用于金额有限的当前支出，一个或多个多签名 Vault 用于长期储蓄。有系统的 UTXO 标签可以帮助您追踪资金的来源，这对于管理保密性和避免不同来源的比特币混在一起特别有用。



确保手机安全：激活生物识别锁，定期执行系统更新，对已安装的应用程序保持警惕。并随时更新 Bitcoin Keeper 的安全补丁。



### 备份安全



在纸张上至少保存两份每个恢复助记词的副本，存放在不同的位置。对于大额资金，可考虑刻上抗灾金属字样。切勿将这些助记词存储在连接互联网的设备上，也切勿对其拍照。



对于多签名保险库，还需保存配置文件（钱包恢复文件），其中包含相关的公钥和保险库结构。该文件与密钥恢复短语相结合，可在任何兼容软件（如 Sparrow 或 Specter）上恢复钱包。



## 优势和局限性



### 优点





- 仅支持比特币应用，可降低复杂性和风险
- 原生集成多数据库，并提供逐步指导
- 很多支持该应用程序的硬件钱包（Tapsigner、Coldcard、Ledger、Jade 等）
- 先进的 UTXO 管理和币控制
- 可连接到个人 Electrum 服务器
- 开放、可审计的源代码



### 需要考虑的限制因素





- 界面主要语言是英语
- 某些高级功能（云备份、辅助服务器）需要升级
- 多签名配置需要初始培训



## 结论



Bitcoin Keeper 是管理比特币的可扩展解决方案。从简单的热钱包到多签名金库，Bitcoin Keeper 采用了渐进式方法，这意味着用户可以根据需求变化升级安全性。轻松集成 Tapsigner 等硬件钱包的能力为实现强大的配置而不过度复杂铺平了道路。



只使用比特币、开放源代码和尊重隐私使其与比特币生态系统的核心价值相一致。



本教程涵盖免费版 Bitcoin Keeper 的基本功能。该应用程序还提供高级功能（云备份、辅助服务器备份、Canary Wallets），这将是专门教程的主题。在即将推出的指南中，我们还将探讨继承规划功能，借助集成在应用程序中的 "增强型保险库" 和随附文件，该功能可让您为向亲人传输比特币做好准备。



## 资源





- 官方网站：[bitcoinkeeper.app](https://bitcoinkeeper.app)
- 帮助中心：[help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- 源代码：[github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)
