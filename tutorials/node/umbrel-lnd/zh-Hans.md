---
name: 伞形 LND
description: 在 Umbrel 上安装和配置 Lightning Network Daemon (LND) 的高级教程
---
![cover](assets/cover.webp)




## 导言



本高级教程将带您逐步完成 Umbrel 节点上闪电节点 (LND) 应用程序的安装、配置和使用。您将学习如何打开通道、管理流动资金以及将节点与移动应用程序同步。



## 1.前提条件：正常运行的 Bitcoin Umbrel 节点



在部署 "闪电 "之前，你需要在 Umbrel 上有一个完全正常运行的 Bitcoin 节点。这包括安装 Umbrel（在树莓派、NAS 或其他机器上）并完全同步 Blockchain Bitcoin。



要安装 Umbrel 并配置 Bitcoin 节点，我们建议您按照我们的专门教程 ：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

确保您的 Bitcoin 节点是最新的并能正常工作，因为 Lightning Network 的所有 off-chain 交易都依赖于它。



## 2.Lightning Network 简介



Lightning Network 是第二个 Layer 协议，旨在通过在主 Blockchain 之外进行交易来加快 Bitcoin 的速度并降低成本。



具体而言，"闪电 "使用节点之间的支付通道网络：两个用户通过冻结 On-Chain BTC（初始交易）打开一个通道，然后可以在该通道内即时进行 Exchange 支付。这些 off-chain 交易不记录在 Blockchain 上，因此速度快，成本几乎为零。



付款可以通过多个渠道（得益于中间节点）到达网络上的任何收款人，从而实现几乎无限规模的即时交易。因此，"闪电 "可提供非常快速、低成本的交易，是日常支付或小额交易的理想选择，同时减轻了 Blockchain Bitcoin 的负担。



要运行，"闪电 "节点必须与网络永久连接，并与其他 "闪电 "节点互动。目前有多种软件实现（LND、Core Lightning、Eclair 等），所有这些软件都相互兼容。Umbrel 使用 LND (Lightning Network Daemon) 作为其官方闪电节点应用程序的一部分。本教程主要介绍 LND。



如需了解 Lightning Network 的完整理论介绍，我们建议您参加我们的专门课程 ：



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

本课程将让您全面了解 Lightning Network 的基本概念，然后再进行 LND 节点练习。



## 3.为什么要自行托管 LND？



与托管或半托管解决方案相比，在 Umbrel 上运营自己的闪电节点（LND）使您对资金和渠道拥有完全的主权。



### 闪电解决方案的比较 ：



**Solutions custodiales (ex: Wallet of Satoshi)** ：




- 您的 Lightning 比特币由可信的第三方管理
- 易于使用，无技术复杂性
- 运营商持有您的资金并可追踪您的交易
- 牺牲控制和保密性



**非商品消费投资组合（如 Phoenix、Breez）** ：




- 用户保留其私人密钥，从而保留其 BTC 的 Ownership
- 没有完整的节点管理 - 应用程序在后台管理通道
- 简约与主权之间的妥协
- 流动性依赖供应商基础设施
- 技术限制（一部智能手机无法为其他智能手机提供支付路径）



**自托管 LND 节点（Umbrel）** ：




- 最大主权：您的 On-Chain 和 off-chain BTC 完全由您控制
- 没有第三方参与开通渠道或管理您的付款
- 提高保密性（您的渠道和交易只有您和您的直接同行知道）
- 使用自由：连接自己的服务和钱包
- 可为他人代理交易（小额费用报酬）
- 技术责任增加（维护、流动性管理、备份）



简而言之，自托管 LND 可为您提供最大程度的控制，但需要更多的技术技能。这是在便利和主权之间的权衡。



## 4.分步教程



### 4.1 在 Umbrel 上安装和配置 Lightning Node 应用程序



同步 Umbrel 节点 (Bitcoin) 后，请按照以下步骤操作 ：



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



从 Interface Umbrel 的 "应用程序商店 "部分安装 Lightning Node 应用程序。



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) 将作为应用程序部署在你的 Umbrel 上。第一次打开它时，你会看到一条警告信息，告知你 "闪电 "是一项实验性技术。



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



您可以选择创建新节点或从备份/seed 恢复节点。首次安装时，请选择创建新节点。闪电节点应用程序将 generate 一个 24 个字符的 Mnemonic 短语（您的 seed 闪电）：请认真写下来（最好是离线写在纸上），因为必要时它将用于恢复您的闪电资金。



**注：在最新版本的 Umbrel 中，安装 "闪电 "应用程序后会提供这个 24 字的 seed（Umbrel 节点本身不提供 Bitcoin）。



![Interface principale de Lightning Node](assets/fr/04.webp)



初始化后，您将访问 Lightning Node 的主 Interface。



![Paramètres de l'application](assets/fr/05.webp)



在应用程序设置中，你会发现许多重要的选项：




   - 查看您的节点 ID（节点的唯一标识符）
   - 连接外部 Wallet（连接 Wallet）
   - 查看密语
   - 访问高级设置
   - 恢复通道
   - 下载频道备份文件
   - 启用自动备份
   - 配置通过 Tor 进行备份（Backup over Tor）



这些选项对于确保 Lightning 节点的安全和管理至关重要。请确保激活自动备份，并妥善保管您的密语。



**有用的资源：**




- [翁布雷尔社区](https://community.umbrel.com) - 供用户分享有关翁布雷尔及其生态系统的问题和解决方案的讨论论坛


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Umbrel 上 Lightning Node 应用程序的功能说明
> - [LND 文档 - 快速入门](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - LND 官方文档

### 4.2 打开 "闪电 "通道



LND 启动并运行后，您就可以打开第一个闪电通道。要找到可连接的优质节点，请



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/)是一个用于寻找可靠节点以打开通道的探索器。



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



例如，[ACINQ 节点](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) 是一个公认的节点，具有出色的可用性和流动性统计数据。



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



在本教程中，我们将与 [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca) 开通一个频道。连接所需的信息（pubkey@ip:port）请参阅其 Amboss 页面。



打开通道 ：



![Bouton d'ouverture de canal](assets/fr/09.webp)



在 "闪电节点 "主页上，点击 "+ OPEN CHANNEL（打开频道）"按钮



![Configuration du canal](assets/fr/10.webp)



在通道配置页面 ：




   - 粘贴从 Amboss 复制的节点 ID（格式：pubkey@ip:port）
   - 定义信道容量（某些节点（如 ACINQ）有最小值，如 400k Sats
   - 必要时调整期初交易费



![Canal en cours d'ouverture](assets/fr/11.webp)



交易发送后，频道将在主页上显示为 "打开"。等待 On-Chain 交易确认。



![Détails du canal](assets/fr/12.webp)



点击频道查看其详细信息：




   - 现状
   - 总容量
   - 流动资金细目（流入/流出）
   - 远程节点的公钥
   - 其他技术信息



### 使用 Lightning Network+ 获取流入的流动性



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ 可在 Umbrel 应用商店中使用，让您更轻松地获得现金。



![Interface principale de LN+](assets/fr/14.webp)



主 Interface 提供三个重要选项：




- "流动性互换：探索现有的互换方案
- "为我开放"：筛选您有资格参与的交换
- "文档"：获取文档



![Message d'erreur LN+](assets/fr/15.webp)



注意：如果您还没有打开频道，点击 "为我打开 "时会看到此错误信息。



![Liste des swaps disponibles](assets/fr/16.webp)



流动性掉期 "页面显示网络上提供的所有掉期报价。



![Swaps éligibles](assets/fr/17.webp)



"Open For Me"（为我打开）只筛选您的节点符合所需条件的交换。



![Détails d'un swap](assets/fr/18.webp)



交换细节示例 ：




- 五角形配置（5 名参与者）
- 每个通道的容量为 300k Sats
- 前提条件：至少 10 个开放通道，总容量为 100 万 Sats
- 可用名额4/5



### 4.3 与移动应用程序（Zeus）同步



要远程控制 Lightning 节点（智能手机），可以使用 Zeus（iOS/Android 上的开源应用程序）。



**宙斯配置伞：**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



确保您的 Umbrel 节点可以访问（默认情况下通过 Tor）。


在 Interface Umbrel 中，打开闪电节点应用程序，然后点击箭头所示的 "连接 Wallet "按钮。



![Page de connexion avec QR code](assets/fr/20.webp)



此时会出现一个二维码，其中包含 lndconnect 格式的 LND 访问数据。该 QR 码的信息量特别大，因此请不要犹豫将其放大以方便阅读。



![Configuration initiale de Zeus](assets/fr/21.webp)



在您的手机上 ：




   - 打开宙斯
   - 在主页上点击 "高级设置"，连接自己的 Lightning 节点
   - 在参数中选择 "创建或连接 Wallet"。



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



在宙斯：




   - 选择 "LND (REST) "作为连接类型
   - 您可以扫描二维码（推荐方法）或手动输入信息。(不要犹豫，放大 Umbrel 的二维码，因为它非常密集）
   - 重要： 如果您的 Umbrel 只能通过 Tor 访问（默认），请激活 "使用 Tor "选项
   - 保存配置



您的 Zeus 现在已连接到您的 Umbrel 节点，允许您进行 "闪电 "付款、查看您的渠道和余额等，同时保持完全的自我管理。



**高级连接选项：**



默认情况下，Zeus ↔ Umbrel 的连接通过 Tor 进行。要想获得更快的连接，有两种选择：



**闪电节点连接（LNC）** ：




   - Lightning Labs 的加密连接机制
   - 在 Umbrel 上安装 Lightning Terminal 应用程序（包括 LNC 访问权限）
   - generate Lightning 终端中的连接二维码（连接 → 通过 LNC 连接 Zeus）
   - 将其扫描至 Zeus（选择 "LNC "作为连接类型）



**VPN Tailscale**：




   - 易于配置的网状 VPN
   - 在 Umbrel（应用商店）和手机上安装 Tailscale
   - 通过 Tailscale 私有 IP 而不是 Tor Address 连接 Zeus



这些选项并不是强制性的，Tor + Zeus 解决方案在大多数情况下都很有效。



> **有用的资源：**
> - [宙斯文档 - Umbrel 连接](https://community.umbrel.com/t/zeus-LN-mobile/7619) - 将宙斯连接到 Umbrel 的官方指南
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus 开源项目
> - [Umbrel Community - 通过 Tailscale 连接 Zeus](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - 使用 Tailscale 将 Zeus 连接到 Umbrel 的指南

## 5.安全和最佳做法



管理自托管的 Lightning 节点需要特别注意安全。



### 节点的备份和安全



**重要的备份类型**



您的闪电伞节点需要两种类型的备份：



**seed句子（24个字）**




- 收回 On-Chain 资金
- 重现 Wallet 闪电的必要条件
- 用于超安全存储（离线、纸质）



**静态通道备份（SCB）** 文件




- 包含闪电通道信息
- 在发生碰撞时强制关闭通道
- 重要：** 切勿手动保存 `channel.db` 文件（有被处罚的风险）



**手动备份程序



手动保存频道 ：


1.访问 "闪电节点 "菜单（"+ 打开通道 "旁边的三个点"⋮"）。


2.下载通道备份文件


3.每次修改通道后导出新的 SCB


4.安全存储 SCB（加密介质、异地副本）



**Umbrel**自动备份系统



Umbrel 具有先进的自动备份系统，可确保 ：



*数据保护：*




- 传输前的客户端加密
- 通过 Tor 网络发送
- 通过随机填充补充数据
- 设备独有的加密密钥



*增强的安全性：*




- 状态变化时即时备份
- 随机间隔的 "诱饵 "备份
- 隐藏备份大小变化
- 防止时间分析



*修复过程：*




- 从您的 seed Umbrel 提取的标识符和密钥
- 只需使用 Mnemonic 短语即可实现完全修复
- 自动恢复最新备份
- 恢复频道设置和数据



### 碰撞修复



如果节点丢失（硬件故障、SD 卡损坏） ：




- 重新安装伞
- 在 "闪电 "应用程序中输入 24 个字的 seed
- 在恢复过程中导入 SCB 文件



LND 将联系您旧渠道的每个合作伙伴，关闭这些渠道并收回您应得的 On-Chain 资金。这些渠道将被永久关闭（如有必要可重新开放）。



### 可用性和欺诈保护



理想情况下，尽可能经常将您的心结留在网上。如果长期不在线：




- 恶意对等设备可尝试广播旧的通道状态
- 闪电 "规定了 "抗议期"（LND 约 2 周）。
- 如果您要离开很长时间，请设置 Watchtower



**Watchtower 配置：**




- 在 LND 高级设置中，添加受信任的 Watchtower 服务器的 URL
- 您可以使用公共服务或安装自己的 Watchtower




要了解有关配置和使用监视塔的更多信息，建议您查看我们的专门教程 ：



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### 其他最佳做法





- 软件更新：** Umbrel 和 LND 保持更新（安全修复）
- 硬件保护：** 使用稳定的系统（带固态硬盘的 Raspberry Pi、迷你电脑）和 UPS
- 网络安全：** 保留默认 Tor 配置，更改 Umbrel 管理员密码（默认："moneyprintergobrrr"）。
- 加密：** 尽可能启用磁盘加密



## 6.附加工具



Umbrel 的 Lightning Node 应用程序提供了管理频道的基本功能，但第三方工具也提供了高级功能。



### 雷霆集线器



Interface 基于网络的现代闪电节点管理系统，可通过 Umbrel 应用商店安装。



**特点：**




- 通道实时可视化（容量、余额）
- 综合再平衡工具
- 支持多路径计费 (MPP)
- 生成二维码 LNURL
- 事务管理 On-Chain



ThunderHub 是监控活动路由节点和执行简单再平衡的理想选择。



### 驾驭闪电 (RTL)



Interface 网络兼容多种 Lightning 实现（LND、Core Lightning、Eclair）。



**亮点：**




- 多节点管理
- 对上下文敏感的仪表板
- 支持潜艇交换（闪电环路）
- 双因素认证
- 导出/导入通道备份



RTL 是管理 Lightning 节点的一把完整的 "瑞士军刀"，它采用更面向专家的方法。



### 其他有用工具





- Lightning Shell** ：通过浏览器使用命令行 (lncli)
- BTC RPC Explorer & Mempool** ：监测 Blockchain
- LNmetrics 和 Torq**：路由性能分析
- Amboss 和 1ML**：节点的 "社交 "管理（别名、联系人、网络分析）



只需点击几下，就能通过 Umbrel 应用商店安装这些工具，无需任何复杂的配置。



**其他工具资源：**




- [ThunderHub.io - 功能](https://thunderhub.io) - ThunderHub 功能概览
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL 文档
- [David Kaspar - 通过 ThunderHub 重新平衡](https://blog.davidkaspar.com) - 重新平衡实用指南
- [管理闪电节点 "指南](https://github.com/openoms/lightning-node-management) - 面向电源用户的高级文档



## 结论



在 Umbrel 上运行自己的 LND 节点是实现金融主权的重要一步。虽然与托管解决方案相比，它需要更多的技术参与，但在控制、保密和积极参与 Lightning Network 方面的好处是相当可观的。



根据本指南，您现在应该能够安装 LND、打开通道、管理流动资金并远程访问节点。随着对生态系统的熟悉，您可以逐步探索高级功能和其他工具。



请记住，您的资金安全取决于您的保障措施和做法。在投入大笔资金之前，请花时间了解各个方面。