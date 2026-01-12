---
name: Specter Desktop
description: 使用自己的节点，完全自主地管理多签名 Bitcoin 投资组合
---

![cover](assets/cover.webp)



Specter Desktop 是 Cryptoadvance 自 2019 年起开发的一款开源应用程序（MIT 许可），可通过硬件钱包（Ledger、Trezor、Coldcard、BitBox02、Passport 等）和自己的 Bitcoin 基础设施（Bitcoin 核心节点或 Electrum 服务器）方便地管理 Bitcoin 钱包。该应用程序在多签名配置中表现尤为突出，通过在多个独立硬件钱包之间分配签名权，可确保大额资金的安全。



**在本教程中，您将学习如何：**




- 在计算机（Windows、macOS 或 Linux）上安装和配置 Specter Desktop
- 将 Specter 连接到 Electrum 服务器（本例中我们将使用 Umbrel）
- 使用 wallet 硬件创建简单的 wallet（冷卡）
- 完全自主地接收和发送比特币
- 使用多个硬件钱包设置 2 对 3 多重签名 wallet
- 在 Umbrel 服务器上安装 Specter（高级奖励）



您的所有交易都将通过您自己的基础设施在本地进行验证，不会向外部服务器传输任何信息，从而保证了您的保密性和财务主权。签署之前，请务必在 wallet 硬件屏幕上检查交易。



## 下载和安装



访问 Specter Desktop 官方网站下载应用程序。



![Page d'accueil Specter](assets/fr/01.webp)



在下载页面，选择与您的操作系统相对应的版本：macOS、Windows 或 Linux。



![Téléchargement selon l'OS](assets/fr/02.webp)



下载完成后，按照操作系统的常规说明安装应用程序。对于 macOS，将图标拖入 "应用程序"。对于 Windows，运行安装程序。对于 Linux，请按照软件包说明进行安装。



## 初始配置



首次启动时，Specter Desktop 会要求您选择连接类型。您可以连接到 Electrum 服务器或自己的 Bitcoin 核心节点。



![Choix du type de connexion](assets/fr/03.webp)



在本例中，我们将使用与运行在 Umbrel 上的 Electrum 服务器的连接。



如需了解更多信息，请参阅我们的 Umbrel 教程：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

该选项的同步速度比 Bitcoin Core 更快。如果您愿意，可以选择 "Bitcoin Core "并配置与本地节点的连接。无论您选择哪种方式，下面的步骤都是一样的。



选择 "Electrum 连接"，然后选择 "输入我自己的"，配置您自己的 Electrum 服务器。



![Configuration Electrum](assets/fr/04.webp)



输入 Electrum 服务器的地址。以 Umbrel 为例，地址为 `umbrel.local`，端口为 `50001`。点击 "连接 "建立连接。



连接完成后，欢迎界面就会出现，并附有一份清单供您开始使用。现在您需要添加硬件钱包。



![Écran d'accueil](assets/fr/05.webp)



## 添加 wallet 硬件



在左侧菜单中点击 "添加设备"，添加 wallet 硬件。



Specter Desktop 支持多种硬件钱包：Trezor、Ledger、BitBox02、Coldcard、KeepKey、Keystone、Cobo Vault 等等。



如果您想了解更多信息，请参阅我们的硬件 wallet 教程。



![Sélection du type de hardware wallet](assets/fr/06.webp)



选择 wallet 硬件。在本例中，我们使用的是 Coldcard MK4。



下面是我们为 wallet 硬件编写的教程：



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

对于冷卡，您需要通过 USB 连接或 microSD 卡从 wallet 硬件导出公钥。



![Import des clés du Coldcard](assets/fr/07.webp)



按照显示的说明从冷卡中导出密钥。为 wallet 硬件命名（此处为 "MK4 Tuto"）。导入密钥后，您可以使用单个密钥创建一个 wallet，也可以添加其他硬件钱包创建一个多签名 wallet。



![Dispositif ajouté](assets/fr/08.webp)



## 创建投资组合



添加 wallet 硬件后，点击 "创建单一密钥 wallet"，创建单一签名 wallet。



为你的投资组合命名（例如 "Wallet for tuto"）并选择地址类型。选择 "Segwit"，使用可优化交易成本的本地 bech32 地址。



![Configuration du portefeuille](assets/fr/09.webp)



一旦创建了您的投资组合，Specter 会提供一个备份 PDF 文件，其中包含恢复投资组合所需的所有公开信息（描述符、扩展公开密钥）。该文件不包含您的私钥。



![Sauvegarde du portefeuille](assets/fr/10.webp)



## 接收比特币



要接收比特币，请在左侧菜单中选择您的 wallet，然后点击 "接收 "选项卡。



Specter 会自动生成带有二维码的新接收地址。



![Génération d'une adresse de réception](assets/fr/11.webp)



您可以复制地址或扫描二维码。在将地址发送给任何人之前，请务必检查 wallet 硬件屏幕上的地址。



## 查看历史和地址



收到比特币后，您可以在 "交易 "选项卡中查看您的交易。



![Historique des transactions](assets/fr/12.webp)



通过 "地址 "选项卡，您可以查看投资组合生成的所有地址及其使用状态和相关金额。



![Liste des adresses](assets/fr/13.webp)



## 发送比特币



要发送比特币，请点击 "发送 "选项卡。输入收件人地址、要发送的金额，如果希望手动选择 UTXOs（币控），请勾选高级选项。



![Création d'une transaction](assets/fr/14.webp)



点击 "Create Unsigned Transaction（创建未签名交易）"建立交易。然后，Specter 会要求你用 wallet 硬件签署交易。



![Signature de la transaction](assets/fr/15.webp)



如果您使用的是 Coldcard，您可以选择通过 USB 或使用 microSD 卡（空气盖）签名。在 wallet 硬件屏幕上确认交易，仔细检查目标地址和金额。



签署交易后，您就可以在 Bitcoin 网络上进行广播。



![Options de diffusion](assets/fr/16.webp)



点击 "发送交易 "发送交易。Specter 会确认您的交易已发送，您可以在 "交易 "选项卡中跟踪交易状态。



![Diffusion de la transaction](assets/fr/17.webp)



## 创建和使用多重签名组合



Specter Desktop 的一大优势是能够简化多重签名组合的管理。多签名 wallet 需要多个签名才能授权交易，从而消除了单点故障。例如，2-on-3 配置需要三个独立硬件钱包的两个签名来验证任何支出。



要创建多签名 wallet，首先要通过 "添加设备 "添加所有签名硬件钱包。在本例中，我们将使用三种不同的硬件钱包：Coldcard MK4（已在前面添加）、Passport 和 Ledger。制造商的多样化避免了对单一供应链或固件的依赖，从而加强了安全性。



下面是 Ledger 和 Passport 教程的链接：



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

通过命名 wallet 硬件（如 "Passport multi"）添加 Passport，并通过 microSD 卡或二维码导入密钥。然后点击 "继续 "继续。



![Ajout du Passport](assets/fr/23.webp)



然后通过 USB 连接 Ledger，在 wallet 硬件上打开 Bitcoin 应用程序，添加 Ledger。为其命名（如 "ledger multi"），然后点击 "Get via USB"（通过 USB 获取）和 "Continue"（继续），导入其公钥。



![Ajout du Ledger](assets/fr/24.webp)



在 Specter 注册三个硬件钱包后，点击 "添加 wallet"，选择 "多重签名 "选项，创建多重签名 wallet。



![Choix du type de wallet](assets/fr/25.webp)



选择您希望包含在多重签名法定人数中的三个硬件钱包：MK4 Tuto、Passport multi 和 ledger multi。点击 "继续 "进入下一步。



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



选择多重签名配置。选择 "Segwit "作为地址类型，以享受优化费用。授权交易所需签名（3 个中的 1 个）"参数可让您定义阈值：对于 2 对 3 配置，需要 2 个签名。每个 wallet 硬件都会显示相应的多重签名密钥。点击 "创建 wallet "完成创建。



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



您的 "Multi tuto "多签名作品集现已创建。Specter 建议您立即保存包含作品集描述的备份 PDF 文件。点击 "保存备份 PDF "下载这个重要文件。



![Wallet multisig créé](assets/fr/28.webp)



Specter 还可以通过 QR 码或文件向每个硬件钱包导出 wallet 信息。这样，某些硬件钱包（如 Coldcard 或 Passport）就能直接在内存中存储多重 ID 配置。



对于 Passport，解锁设备后进入 "管理帐户">"连接 Wallet">"Specter">"Multisig">"QR 码"，然后扫描 Specter 生成的 QR 码。然后 Passport 会要求您扫描 wallet 的接收地址，以验证多重 ID 配置。



对于 MK4，将其插入电脑并解锁。然后点击 "保存 MK4 Tuto 文件"，将文件保存到 MK4 中。下次签署 wallet 硬件时，MK4 将使用该文件完成多重签名的配置。



![Export vers les hardware wallets](assets/fr/29.webp)



您可以随时通过投资组合的 "设置 "选项卡，然后点击 "导出"，访问备份信息：



![Accès au backup PDF](assets/fr/30.webp)



日常使用仍与简单的 wallet 类似：您可以正常使用 generate 接收地址。要发送比特币，请进入 "发送 "选项卡，输入收件人地址和金额，然后点击 "创建未签名交易"。



![Création d'une transaction multisig](assets/fr/31.webp)



Specter 会创建一个 PSBT (Partially Signed Bitcoin Transaction)，并显示 "Acquired 0 of 2 signatures"（获得 2 个签名中的 0 个）。现在您必须使用三个硬件钱包中的至少两个进行签名。点击第一个 wallet 硬件（如 "MK4 Tuto"），使用冷卡签名，然后点击第二个硬件（如 "Passport multi"），获得所需的第二个签名。



![Signature de la transaction](assets/fr/32.webp)



获得所需的 2 个签名后（界面显示 "已获得 2 个签名中的 2 个 "和 "交易已准备好发送"），点击 "发送交易"，即可在 Bitcoin 网络上广播交易。



![Transaction prête à être diffusée](assets/fr/33.webp)



这种多重签名方法尤其适用于公司（需要多位经理批准支出）、家庭（保护多代遗产）或管理大笔资金的个人（硬件钱包的地理分布可抵御局部灾害）。



### 多重签名备份的极端重要性



**请注意**：备份多位密码组合与备份单个密码组合有本质区别。仅靠您的恢复短语（seed 短语）不足以恢复多组密码组合。您还必须备份**output descriptor** (output descriptor)，其中包含多组密码组合的配置信息。



output descriptor 包括基本数据：每个联合签名者的扩展公钥 (xpubs)、签名阈值（在我们的例子中为 2 对 3）、使用的脚本类型（本地、嵌套或传统 Segwit），以及每个 wallet 硬件的旁路路径。如果没有该描述符，即使您拥有三个恢复短语中的两个，也无法重建 wallet 或访问比特币。该描述符可让软件知道如何将公钥组合到 generate 和 Bitcoin 中与您的资金相对应的地址。



Specter Desktop 会在您创建多 ID 组合时自动生成一个备份 PDF 文件。该 PDF 文件包含完整的描述符、每个 wallet 硬件的指纹以及恢复所需的所有公共信息。 **该文件不包含您的私人密钥**，因此本身不允许您使用比特币，但允许任何访问该文件的人查看您的完整交易历史和余额。



要正确备份您的多重签名配置，请按照以下步骤操作：创建您的作品集后，点击 "设置 "选项卡，然后点击 "导出 "并选择 "保存备份 PDF"。创建该 PDF 的多个副本：至少打印两份纸质副本，同时保留一份加密的数字副本。在不同的地理位置，将 PDF 的一份副本与您的每个恢复短语一起保存。



在防火防水的金属板上镌刻您的恢复短语，以保证其使用寿命。千万不要低估这些备份的重要性：如果您丢失了计算机上的 `~/.specter` 文件夹，并且在没有描述符备份的情况下丢失了一个硬件钱包，那么您的所有资金都将无可挽回地丢失，即使是 2 对 3 配置也是如此。多签名冗余可防止 wallet 硬件丢失，但前提是您已正确备份 wallet 的描述符。



## Specter Desktop 的优势和局限性



**优势**：无需第三方服务器，通过完全本地验证实现最佳保密性。多签名灵活性，可进行高级配置（公司、家庭、个人）。支持广泛的硬件 wallet，具有全面的互操作性（USB 和空气盖）。



**限制**：对 Bitcoin 高级概念（UTXO、描述符、推导路径）的学习曲线较长。



## 最佳做法



在验证之前，请务必检查硬件 wallet 屏幕上的地址和金额，以防止恶意软件。



将 PDF 备份与种子分开保存。这些公共描述符可以存储在银行保险库或加密云中，便于恢复而不会暴露私人密钥。



在使用大额资金的投资组合之前，测试 token 金额的恢复。创建、测试、删除和恢复，以验证您的程序。



及时更新 Specter 和固件。按地域（家庭/办公室/附近）分布您的多重签名共同签名人，以抵御局部灾难。使用描述性标签，方便会计和报税。



## 奖励：在 Bitcoin 服务器上安装（Umbrel、RaspiBlitz、Start9）



如果您已经拥有 Umbrel、RaspiBlitz、MyNode 或 Start9 等 Bitcoin 服务器，您可以直接从它们的应用程序商店安装 Specter Desktop。这种方法有几个显著优势：应用程序会自动与本地 Bitcoin 核心节点进行配置，可通过网络界面从网络上的任何设备全天候访问，甚至可以通过 Tor 安全地远程访问。您的整个 Bitcoin 基础设施都集中在一台专用服务器上，从而简化了管理并加强了您的主权。



### 从 Umbrel 应用程序商店安装



从 Umbrel 界面进入 App Store，搜索 Specter Desktop。点击 "安装 "启动安装。



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



安装完成后，在 Umbrel 上打开 Specter Desktop。欢迎屏幕会要求你选择连接类型。如果你在 Umbrel 上使用 Specter，请点击 "更新设置 "配置连接。



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



选择 "远程 Specter USB 连接"，以便在远程 Umbrel 服务器上使用 Specter 时，可以使用连接到本地计算机的 USB 硬件钱包。



![Configuration Remote Specter USB](assets/fr/20.webp)



按照显示的说明配置 HWI 网桥。您需要访问设备网桥设置，并将域 `http://umbrel.local:25441` 添加到白名单。单击 "Update（更新）"保存配置。



![HWI Bridge Settings](assets/fr/21.webp)



如果您也想在本地电脑上使用 USB 硬件钱包，请将 Specter Desktop 应用程序下载到电脑上，并将其设置为 "是，我远程运行 Specter"。点击 "保存 "完成配置。



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## 结论



Specter Desktop 使高级 Bitcoin 配置民主化，在不牺牲主权或保密性的情况下实现多重签名。对于管理大量资金的用户来说，它能将机构实践转化为个人也能部署的解决方案。



尽管该应用程序需要在基础设施和学习方面进行初始投资，但它提供了完全的主权：对验证基础设施的控制、密钥的实际所有权以及不受第三方监控的交易。无论您是确保储蓄安全的个人、创建多代同堂保险箱的家庭，还是管理现金流的公司，Specter Desktop 都是兼顾最高安全性和绝对主权的参考工具。



## 资源



### 正式文件




- [Specter Desktop 官方网站](https://specter.solutions/desktop/)
- [GitHub源代码](https://github.com/cryptoadvance/specter-desktop)
- [完整文档](https://docs.specter.solutions/)



### 社区和支持




- [Telegram Specter 社区组](https://t.me/spectersupport)
- [Reddit论坛](https://reddit.com/r/specterdesktop/)
- [GitHub错误报告](https://github.com/cryptoadvance/specter-desktop/issues)