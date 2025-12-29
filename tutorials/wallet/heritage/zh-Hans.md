---
name: 遗产
description: 通过 Taproot 脚本集成继承机制的 Bitcoin 组合
---

![cover](assets/cover.webp)



对于任何加密资产持有者来说，在死亡或丧失工作能力的情况下传承比特币都是一项重大挑战。如果没有合适的继承计划，你的亲人将无法收回这些资产。



Heritage 通过直接在 Bitcoin 区块链上实现死人切换机制，提供了一个优雅的答案。这种开源的 wallet 可以配置 on-chain 继承条件：如果所有者在规定时间内不再进行交易，预先指定的替代密钥就可以释放资金。



## 什么是遗产？



Heritage 是通过 Taproot 脚本集成继承机制的 Bitcoin 组合。该开源软件由 Jérémie Rodon 在 MIT 许可下开发，保证了透明度和耐用性。



Heritage 使用以 Bitcoin 地址编码的 Taproot 脚本。每个 UTXO 包含两类支出条件：





- 主路径** ：所有者可以随时使用他的主键花费他的比特币
- 替代路径**：对于每个指定的继承人，脚本会将其公共密钥与时间锁结合起来



每笔业主交易都会自动推迟继承条款的激活日期。如果长期不活动（死亡、丧失行为能力），则会自动触发条件。



## 遗产服务（可选）



Heritage 提供两种使用方式：



**自己动手（免费）**：仅使用开源应用程序。你可以用自己的节点自主管理一切。该选项提供内置备份访问、内置继承和对比特币的独家控制。不过，您需要创建自己的提醒（日历、提醒事项），以免忘记更新时间锁，而且继承人不会收到自动通知。



**使用服务（每年0.05%）** ：btc-heritage.com 服务增加了简化管理的功能：




- 到期前自动提醒
- 自动通知继承人，指导他们完成恢复过程
- 优先支持
- 简化描述符管理



费用：每年管理金额的 0.05%，最低 0.5 mBTC/年。第一年免费。



该服务保持非托管性质：您的私钥从未离开过您的设备。Heritage 无法访问您的资金。



## 传统 CLI



对于喜欢使用终端的高级用户，Heritage 提供了一个命令行工具 (CLI)，用于细粒度控制和气隙式机器运行。



![Page Heritage CLI](assets/fr/03.webp)



完整的 CLI 文档可在 [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli) 获取。这里有下载、连接服务、创建钱包（使用 Ledger 或本地密钥）、管理继承人和交易的说明。



本教程主要介绍桌面应用程序，大多数用户更容易使用该程序。



## 传统桌面



Heritage Desktop 是一个图形应用程序，具有直观的界面，可指导用户完成配置过程的每一步。



### 下载



访问 [btc-heritage.com](https://btc-heritage.com)，点击 "下载应用程序"。



![Page d'accueil Heritage](assets/fr/01.webp)



选择与您的操作系统（Linux 64bits 或 Windows 64bits ）相对应的版本。二进制文件没有数字签名，可能会触发安全警告。



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



### 首次发射



首次启动时，上机向导会为您提供三种选择：



![Onboarding initial](assets/fr/05.webp)





- 设置遗产 Wallet**：创建带有遗产计划的新 wallet
- 继承比特币**：作为继承人收回比特币
- 自己探索**：在没有帮助的情况下探索功能



选择 "设置遗产 Wallet"，创建第一个 wallet。



### Bitcoin 网络连接



选择连接 Bitcoin 网络的方式：



![Choix connexion](assets/fr/06.webp)





- 使用遗产服务**：管理基础设施，简化继承人的工作
- 使用我自己的节点**：连接到自己的 Bitcoin 核心或 Electrum 节点



在本教程中，我们将使用自己的节点。



### 私钥管理



选择如何管理私钥：



![Gestion des clés](assets/fr/07.webp)





- 使用 Ledger 硬件装置** ：使用 wallet 硬件实现最高安全性（推荐使用）
- 本地存储，带密码**：带密码保护的本地存储密钥
- 还原现有的 wallet** ：从现有 seed 恢复



### 节点配置



如果您使用自己的节点，应用程序会指导您进行配置。请确保您的 Bitcoin 或 Electrum 节点是 .NET 的：




- 已安装并运行
- 与 Bitcoin 网络同步
- 配置为接受 RPC 连接（用于 Bitcoin 核心）



![Configuration nœud](assets/fr/08.webp)



节点准备就绪后，点击 "我的 Bitcoin 节点已启动并运行"。



### 状态面板



点击右上角的 "状态"，然后点击 "打开配置"，访问连接参数。



![Panneau Status](assets/fr/09.webp)



设置 Electrum 服务器的 URL（例如，如果使用 Umbrel，则为 `umbrel.local:50001`）。



![Configuration Electrum](assets/fr/10.webp)



### 创建 wallet



建立连接后，点击 WALLETS 标签中的 "创建 Wallet"。



![Créer wallet](assets/fr/11.webp)



弹出式窗口解释了 Heritage .NET 的分割结构：



![Architecture split](assets/fr/12.webp)



1. **密钥提供商（离线）**：管理私钥并签署交易。可以是 Ledger 或 wallet 软件。


2. **联机 Wallet**：处理与 Bitcoin 网络的同步、地址创建和事务广播。



填写创建表 ：



![Formulaire création wallet](assets/fr/13.webp)





- Wallet 名称**：用于标识 wallet 的唯一名称
- 密钥提供者**：本教程选择本地密钥存储
- 新建/恢复**：选择 "新建 "以 generate 新的 seed
- 字数**：建议 24 个字，以确保最大安全性



输入高强度密码并选择在线 Wallet 选项：



![Options Online Wallet](assets/fr/14.webp)





- 本地节点**：使用自己的 Electrum 或 Bitcoin 核心节点
- 遗产服务**：使用传统服务（建议用于通知功能）



点击 "创建 Wallet "完成创建。



### Interface 转自 wallet



您的 wallet 已创建。界面显示 ：



![Interface wallet](assets/fr/15.webp)





- 平衡
- 发送和接收按钮
- 交易历史
- 遗产配置历史
- wallet 地址



### 创建继承人



转到 "继承人 "选项卡创建继承人。



![Page Heirs](assets/fr/16.webp)



弹出的信息说明了这一点：




- 继承人是与个人相关的 Bitcoin 公钥
- 每个继承人都有自己的记忆词组
- 第一位继承人应该是自己的 "备份"（以防主 wallet 丢失）。



#### 创建备份继承人



点击 "创建继承人 "并命名为 "备份"。



![Création héritier Backup](assets/fr/17.webp)



弹出窗口解释了为什么不含 passphrase 的 12 个字的句子对继承人是安全的：


1. **不能立即使用**：继承人钥匙在时间锁定到期前无法使用资金


2. **漏洞检测**：如果有人访问该短语，您可以更新遗产配置


3. **长期使用**：多年后，passphrase 可能会被遗忘



配置继承人 ：



![Configuration héritier](assets/fr/18.webp)





- 密钥提供者** ：本地密钥存储
- 新**：生成新的 seed
- 字数**：12 个字



完成创建 ：



![Finalisation héritier](assets/fr/19.webp)





- 继承人类型**：扩展公钥
- 导出到服务**：可选项，可自动通知继承人



备份继承人现已创建：



![Héritier créé](assets/fr/20.webp)



#### 保存继承人的记忆词组



单击 "备份 "继承人，然后单击 "显示 Mnemonic"：



![Afficher mnemonic](assets/fr/21.webp)



**重要提示：记下这 12 个字，并妥善保管。这是找回资金的关键。



![Phrase mnémotechnique](assets/fr/22.webp)



#### 从应用程序中删除 seed



写下短语后，访问继承人参数（齿轮图标）：



![Paramètres héritier](assets/fr/23.webp)



使用 "Strip Heir Seed "从应用程序中删除私钥。确认已保存短语。



![Strip Heir Seed](assets/fr/24.webp)



这是一种安全措施：只有公钥保留在应用程序中，足以配置继承。



#### 创建第二继承人



重复该过程，创建第二个继承人（例如 "Satoshi"）。现在您将有两个继承人：



![Deux héritiers](assets/fr/25.webp)





- 备份**：您的个人应急钥匙
- Satoshi**：指定继承人



### 遗产配置



返回 wallet，点击 "设置 "图标：



![Paramètres wallet](assets/fr/26.webp)



在 "遗产配置 "部分，点击 "创建"：



![Heritage Configuration](assets/fr/27.webp)



为每个继承人设定时间限制：



![Configuration délais](assets/fr/28.webp)





- 备份**：180 天（6 个月） - 到期日期：2026-06-18
- Satoshi**：455 天（15 个月） - 到期日期：2027-03-20



**重要**：每个继承人的延迟时间必须长于前一个继承人。第一位继承人（备份）将首先获得资金。



同时配置 ：



![Configuration finale](assets/fr/29.webp)





- 参考日期**：计算周转时间的起始日期
- 最低到期延迟**：交易后的最短延迟时间（建议为 10 天）



点击 "创建 "验证配置。



遗产配置现已激活：



![Configuration active](assets/fr/30.webp)



它显示了两个继承人各自的截止日期和失效日期。



### 保存描述符



**重要**：保存您的 wallet 说明。没有这些描述符，即使有记忆短语，也不可能恢复资金。



单击 "备份描述符"：



![Bouton Backup](assets/fr/31.webp)



保存包含 Bitcoin 描述符的 JSON 文件：



![Backup descripteurs](assets/fr/32.webp)



该文件应与各自的记忆短语一起传给您的继承人。



### 接收比特币



点击 "RECEIVE（接收）"，generate 接收地址：



![Recevoir bitcoins](assets/fr/33.webp)



恭喜您您的 Heritage Wallet 已准备好接收比特币。每个生成的地址都会自动包含您的 Heritage 条件。



收到交易后，您的余额就会更新：



![Solde mis à jour](assets/fr/34.webp)



历史记录显示交易和相关遗产配置。



---

## 继承人的追偿



一旦设定的时间过去，继承人就可以取回资金。



### 先决条件



继承人需要：


1.他的 12 字记忆短语


2.原始 wallet 描述符备份文件（JSON）



### 创建继承人 Wallet



在 "继承 "选项卡中，弹出窗口会提醒您这些先决条件：



![Page Heir Wallets](assets/fr/35.webp)



**请注意**：如果没有描述符备份文件，即使使用正确的记忆短语，也无法访问资金。



点击 "创建继承人 Wallet"：



![Créer Heir Wallet](assets/fr/36.webp)



请填写表格：



![Formulaire Heir Wallet](assets/fr/37.webp)





- 继承人 Wallet 名称**：用于识别该继承人的名称 wallet
- 密钥提供者** ：本地密钥存储
- 恢复**：选择此选项可输入现有短语



输入继承人记忆短语的 12 个单词，并配置遗产提供者：



![Entrée mnemonic](assets/fr/38.webp)





- 遗产提供者**："本地"，使用自己的节点和备份文件



加载 JSON 备份文件并点击 "创建继承人 Wallet"：



![Chargement backup](assets/fr/39.webp)



### Interface 继承人 Wallet



创建继承人 Wallet。最初，如果时间锁定尚未到期，则无法继承：



![Pas d'héritage disponible](assets/fr/40.webp)



一旦延迟结束，资金与 Bitcoin 网络同步，它们就会出现在遗产列表中：



![Héritage disponible](assets/fr/41.webp)



界面显示 ：




- 钥匙类型和指纹
- 可继承资金总额
- 当前可消费金额（如果时间锁定尚未到期，则为 0 Sat）
- 到期和失效日期



到期时，"支出 "按钮会将比特币转入个人 wallet 中。



---

## 最佳做法



### 保存描述符



wallet 描述符对于重建遗产地址至关重要。 **如果没有描述符，即使有记忆短语，您也无法找到您的资金。



### 钥匙安全





- 尽可能使用 Ledger 作为主键
- 切勿将继承人的判决与自己的判决存放在同一地方
- 通过多种媒体和地点传播信息



### 为您的亲人提供文件



编写清晰的说明，解释恢复过程中的每个步骤。在关键时刻，您的继承人可能并不熟悉 Bitcoin。



## 替代品



还有其他管理比特币传输的解决方案，包括 Liana 和 Bitcoin Keeper。您可以在下面找到我们的教程：



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## 结论



Heritage 允许您通过桌面应用程序以主权方式规划 Bitcoin 的继承。实施时需要深思熟虑地考虑适当的时间框架和保密问题。别忘了传给您的继承人：




- 他们的 12 字记忆短语
- 描述符备份文件
- 恢复说明



## 资源





- [遗产官方网站](https://btc-heritage.com)
- [CLI号文件](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub 传统桌面](https://github.com/crypto7world/heritage-gui)