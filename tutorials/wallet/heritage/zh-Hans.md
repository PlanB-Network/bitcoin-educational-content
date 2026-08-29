---
name: Heritage
description: 一款通过 Taproot 脚本集成继承机制的比特币钱包。
---

![cover](assets/cover.webp)

在身故或丧失行为能力的情况下，如何妥善传承比特币对任何加密资产持有者来说都是一项重大挑战。如果没有合适的继承计划，这些资产将无法被您的亲人追回。

Heritage 提供了一种优雅的解决方案，它直接在比特币区块链上实现了 “死亡开关” 机制。这款开源钱包允许用户配置链上继承条件：如果所有者在设定的时间内没有进行任何交易，预先指定的备用密钥即可释放资金。

## 何为 Heritage？

Heritage 是通过 Taproot 脚本集成继承机制的比特币钱包。该开源软件由 Jérémie Rodon 在 MIT 许可下开发，保证了其透明度和耐用性。

Heritage 使用编码在比特币地址中的 Taproot 脚本。每个 UTXO 都集成了两种类型的支出条件：

- **主要路径**：所有者可以随时使用其主密钥花费其比特币
- **备用路径**：对于每个指定的继承人，脚本会将他们的公钥与时间锁结合使用

每个所有者的交易都会自动推迟继承条款的激活日期。如果所有者长期处于不活跃状态（例如去世或丧失行为能力），则这些条件会自动触发。

## Heritage 的服务（可选）

Heritage 提供两种使用方式：

**自己动手（免费）**：仅使用开源应用程序。您可以使用自己的节点自主管理一切。此选项提供内置备份访问、内置继承功能以及对您的比特币的独家控制权。但是，您需要自行创建提醒（日历、提醒事项），以免忘记续订时间锁，并且不会自动通知您的继承人。

**使用 Heritage 的服务（每年 0.05%）**：btc-heritage.com 服务添加了简化管理的功能：

- 到期前自动提醒
- 自动通知继承人，指导他们完成恢复过程
- 优先支持
- 简化描述符管理

费用：每年管理金额的 0.05%，最低 0.5 mBTC/年。第一年免费。

该服务保持非托管性质：您的私钥从未离开过您的设备。Heritage 无法访问您的资金。

## Heritage 的命令行工具

对于喜欢使用终端的高级用户，Heritage 提供了一个命令行工具 (CLI)，用于精细控制和物理隔离的机器操作。

![Page Heritage CLI](assets/fr/03.webp)



完整的 CLI 文档可在 [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli) 访问。在此有下载、连接服务、创建钱包（使用 Ledger 或本地密钥）、管理继承人和交易的说明。

本教程主要介绍桌面应用程序，大多数用户更容易使用该程序。

## Heritage Desktop

Heritage Desktop 是一个图形应用程序，具有直观的界面，可指导用户完成配置过程的每一步。

### 下载

访问 [btc-heritage.com](https://btc-heritage.com)，点击 "Download application"。

![Page d'accueil Heritage](assets/fr/01.webp)



选择与您的操作系统（Linux 64bits 或 Windows 64bits）相对应的版本。二进制文件没有数字签名，可能会触发安全警告。



![Page de téléchargement](assets/fr/02.webp)



### 在 Linux 上安装



在 Linux 上，应用程序以 AppImage 格式发布。运行前，您需要安装 `libfuse2` 依赖项：



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)


然后将文件设为可执行文件并运行：


```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```

### 首次启动

首次启动时，上机向导会为您提供三种选择：

![Onboarding initial](assets/fr/05.webp)



- **Setup an Heritage Wallet**（设置 Heritage 钱包）：创建带有遗产计划的新钱包
- **Inherit bitcoins**（继承比特币）：作为继承人收回比特币
- **Explore by myself**（自己探索）：在没有帮助的情况下探索功能

选择 "Setup an Heritage Wallet"，创建第一个钱包。

### 连接到比特币网络

选择连接到比特币网络的方式：

![Choix connexion](assets/fr/06.webp)

- **Using the Heritage Service**：管理基础设施，简化继承人的工作
- **Using my own node**：连接到自己的 Bitcoin Core 或 Electrum 节点

在本教程中，我们将使用自己的节点。

### 私钥管理

选择如何管理私钥：

![Gestion des clés](assets/fr/07.webp)



- **With a Ledger Hardware Device** ：使用硬件钱包实现最高安全性（推荐使用）
- **Local storage with password**：带密码保护的本地存储密钥
- **Restore an existing wallet** ：使用现有助记词恢复

### 节点配置

如果您使用自己的节点，应用程序会引导您完成配置。请确保您的比特币或 Electrum 节点：

- 已安装并运行
- 已与比特币网络同步
- 已配置为接受 RPC 连接（适用于 Bitcoin Core）

![Configuration nœud](assets/fr/08.webp)

节点准备就绪后，点击 "我的 Bitcoin 节点已启动并运行"。

### 状态面板

点击右上角的 "Status" 按钮，然后点击 "Open Configuration"，以查看访问连接参数。

![Panneau Status](assets/fr/09.webp)

设置 Electrum 服务器的 URL（例如，如果使用 Umbrel，则为 `umbrel.local:50001`）。

![Configuration Electrum](assets/fr/10.webp)

### 创建钱包

建立连接后，点击 WALLETS 标签中的 "Create Wallet"。

![Créer wallet](assets/fr/11.webp)

弹出窗口解释了 Heritage 的分离式架构：

![Architecture split](assets/fr/12.webp)

1. **Key Provider (Offline)**：管理私钥并签署交易。可用 Ledger 或钱包软件。

2. **Online Wallet**：处理与比特币网络的同步、地址创建和交易广播。

填写创建钱包表单：

![Formulaire création wallet](assets/fr/13.webp)





- **Wallet Name**：用于识别您的钱包的独特名称
- **Key Provider**：对于本教程，请选择 “Local Key Storage”
- **New/Restore**：选择 “New" 以生成新的种子
- **Word Count**：建议使用 24 words，以获得最高安全性

输入强密码并选择在线钱包选项：

![Options Online Wallet](assets/fr/14.webp)

- **Local Node**：使用自己的 Electrum 或 Bitcoin Core 节点
- **Heritage Service**：使用传统服务（建议用于通知功能）

点击 "Create Wallet" 以完成创建。

### 钱包界面

您的钱包已创建完成。界面显示：
![Interface wallet](assets/fr/15.webp)

- Balance（余额）
- SEND（发送）和 RECEIVE（接收）按钮
- Transaction history（交易历史）
- Heritage configuration history（Heritage 的配置历史）
- Wallet addresses（钱包地址）


### 创建继承人

前往 "HEIRS" 选项卡以添加继承人。

![Page Heirs](assets/fr/16.webp)

弹出的信息说明了这一点：

- 继承人是与个人关联的比特币公钥
- 每个继承人都有自己的助记词
- 第一个继承人应该是您自己的“备份”（以防主钱包丢失）

#### 创建备份继承人

点击 "Create Heir" 并命名为 "Backup"。

![Création héritier Backup](assets/fr/17.webp)

弹出窗口解释了为什么一个 12 个单词的助记词（无需 passphrase/密语）对继承人来说是安全的：

1. **不能立即使用**：继承人密钥在时间锁定到期前无法使用资金

2. **漏洞检测**：如果有人访问该助记词，您可以更新 Heritage 的配置

3. **长期使用**：多年后，密语可能会被遗忘

配置继承人 ：

![Configuration héritier](assets/fr/18.webp)

- **Key Provider**：本地密钥存储
- **New**：生成新的助记词
- **Word Count**：选择 12 words


完成创建 ：

![Finalisation héritier](assets/fr/19.webp)


- **Heir Type**：选择 Extended Public Key
- **Export to Service**：可选，可自动通知继承人

备份继承人现已创建：

![Héritier créé](assets/fr/20.webp)



#### 保存继承人的助记词

点击 “Backup”，然后点击 "Show Mnemonic"：

![Afficher mnemonic](assets/fr/21.webp)



**重要提示**：请记下这 12 个单词并妥善保管。这是找回资金的关键。


![Phrase mnémotechnique](assets/fr/22.webp)


#### 从应用程序中移除种子

记下助记词后，访问继承人参数（齿轮图标）：

![Paramètres héritier](assets/fr/23.webp)

使用 "Strip Heir Seed "从应用程序中删除私钥。确认已保存助记词。

![Strip Heir Seed](assets/fr/24.webp)

这是一种安全措施：只有公钥保留在应用程序中，足以配置继承。

#### 创建第二继承人

重复该过程，创建第二个继承人（例如 "Satoshi"）。现在您将有两个继承人：

![Deux héritiers](assets/fr/25.webp)

- **Backup**：您的个人应急密钥
- **Satoshi**：指定继承人

### Heritage 配置

返回钱包，点击 "Settings" 图标：

![Paramètres wallet](assets/fr/26.webp)

在 "Heritage Configuration" 部分，点击 "Create"：

![Heritage Configuration](assets/fr/27.webp)

为每个继承人设定时间限制：

![Configuration délais](assets/fr/28.webp)

- **Backup**：180 天（6 个月）- 到期日期：2026-06-18
- **Satoshi**：455 天（15 个月）- 到期日期：2027-03-20

**重要**：每个继承人的延迟时间必须长于前一个继承人。第一位继承人（Backup）将首先获得资金。

同时，请配置：

![Configuration finale](assets/fr/29.webp)

- **Reference Date**：计算周转时间的起始日期
- **Minimum Maturity Delay**：交易后的最短延迟时间（建议设置为 10 天）

点击 "Create" 以验证配置。

Heritage 配置现已激活：

![Configuration active](assets/fr/30.webp)

它显示了两个继承人各自的截止日期和失效日期。

### 保存描述符

**重要提示**：保存您的钱包描述符。没有这些描述符，即使您拥有助记词，也不可能恢复资金。

点击 "Backup Descriptors"：

![Bouton Backup](assets/fr/31.webp)

保存包含比特币描述符的 JSON 文件：

![Backup descripteurs](assets/fr/32.webp)

该文件应与各自的助记词一起传给您的继承人。

### 接收比特币

点击 "RECEIVE"（接收），以生成接收地址：

![Recevoir bitcoins](assets/fr/33.webp)

恭喜您！您的 Heritage Wallet 可以接收比特币了。每个生成的地址都会自动包含您的 Heritage 条件。



收到交易后，您的余额就会更新：



![Solde mis à jour](assets/fr/34.webp)

历史记录显示交易和相关遗产配置。

---

## 继承人的追偿

一旦设定的时间过去，继承人就可以取回资金。

### 前提条件

继承人需要：

1.他的 12 个单词助记词


2.原始钱包描述符备份文件（JSON）

### 创建继承人的钱包



在 "HEIRS" 选项卡中，弹出窗口会提醒您这些前提条件：

![Page Heir Wallets](assets/fr/35.webp)

**请注意**：如果没有描述符备份文件，即使使用正确的助记词，也无法访问资金。

点击 "Create Heir Wallet"：



![Créer Heir Wallet](assets/fr/36.webp)



请填写页面上的表单：



![Formulaire Heir Wallet](assets/fr/37.webp)

- **Heir Wallet Name**：用于识别该继承人的名称 wallet
- **Key Provider**：本地密钥存储
- **Restore**：选择此选项可输入现有助记词

输入继承人助记词的 12 个单词，并配置遗产提供者：

![Entrée mnemonic](assets/fr/38.webp)


- **Heritage Provider**："Local"，使用自己的节点和备份文件

加载 JSON 备份文件并点击 "Create Heir Wallet"：

![Chargement backup](assets/fr/39.webp)



### 继承人钱包的界面

继承人钱包以创建好。最初，如果时间锁定尚未到期，则无法继承：

![Pas d'héritage disponible](assets/fr/40.webp)

一旦延迟结束，资金与比特币网络同步，它们就会出现在 Inheritances List 中：

![Héritage disponible](assets/fr/41.webp)

界面将显示 ：

- Key type and fingerprint（密语类型和指纹）
- Total inheritable funds（可继承资金总额）
- Current spendable amount, 0 sat if timelock has not yet expired.(当前可消费金额，如果时间锁定尚未到期，则为 0 聪）
- 到期和失效日期

到期时，"Spend" 按钮会将比特币转入个人钱包中。

---

## 最佳实践

### 保存描述符

钱包描述符对于重建您的 Heritage 地址至关重要。**如果没有描述符，即使您有助记词，也无法找回您的资金。

### 密语安全

- 尽可能使用 Ledger 作为主密钥
- 切勿将继承人的助记词与您自己的助记词存储在同一位置
- 将信息分散存储在多个介质和位置

### 为您的亲人准备的文档

编写清晰的说明，解释恢复过程的每个步骤。您的继承人在关键时刻可能不熟悉比特币。

## 其他方案

还有其他解决方案可以管理您的比特币传输，例如 Liana 和 Bitcoin Keeper。您可以在下方找到我们的教程：

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## 结论

Heritage 允许您通过桌面应用程序以自主的方式规划您的比特币传承。实施过程中需要仔细考虑合适的时间安排和密钥安全。别忘了将以下内容传承给您的继承人：

- 他们的 12 个单词助记词
- 描述符备份文件
- 恢复说明

## 资源





- [Heritage 的官方网站](https://btc-heritage.com)
- [文件 CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage 命令行界面](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage 桌面](https://github.com/crypto7world/heritage-gui)
