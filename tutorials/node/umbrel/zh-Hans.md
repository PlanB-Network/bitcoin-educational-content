---
name: 伞
description: 发现并安装 Umbrel - 您的 Bitcoin 节点和主服务器
---

![cover](assets/cover.webp)



## 导言



### 什么是 Bitcoin 节点？



Bitcoin 节点是通过运行 Bitcoin 核心软件或替代客户端参与 Bitcoin 网络的计算机。它的作用对网络的运行和安全至关重要：





- Blockchain 存储**：维护一份完整、最新的 Blockchain Bitcoin 副本
- 交易验证**：根据协议规则验证每个交易和区块
- 信息传播**：与其他节点共享新交易和区块
- 建立共识**：促进网络规则的应用



运行自己的 Bitcoin 节点是实现金融主权的关键一步，可带来几大好处：





- 保密性**：共享您的交易，不会向第三方透露您的信息
- 抵制审查**：没人能阻止你使用 Bitcoin
- 独立验证**：无需信任他人的节点来验证您的交易
- 建立共识**：促进 Bitcoin 网络规则的应用
- 网络支持**：成为网络分配和权力下放的积极参与者



### Umbrel：运行 Bitcoin 节点的简单解决方案



Umbrel 是一个开源操作系统，可简化 Bitcoin 节点的安装和管理。它还能将你的计算机转变为个人和私人家庭服务器，使托管 .NET 服务器变得容易：





- 一个完整的 Bitcoin 节点
- Bitcoin 基本应用（Electrs、Mempool.space）
- 其他个人服务（云存储、流媒体、VPN 等）



Umbrel 拥有优雅、直观的 Interface 用户界面，使所有人都能使用自助托管服务，同时保留对数据的完全控制。



## 伞架安装选项



Umbrel 提供两种使用其解决方案的主要方式：交钥匙方案（Umbrel Home）和免费开源版本（UmbrelOS）。



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home：交钥匙解决方案



Umbrel Home 是一款预配置家庭服务器，专为最佳体验而设计。这个一体化硬件解决方案包括



**硬件功能**




- 为自托管而优化的高性能处理器
- 预装高速 SSD 存储器
- 静音冷却系统
- 紧凑、优雅的设计
- 集成 USB 和以太网端口



**独家福利**




- 即插即用安装：插上电源即可使用
- 提供专门协助的高级支持
- 保证自动更新
- 集成迁移向导
- 全套硬件保修
- 全面支持所有功能



**价格**：399 欧元（价格可能因季节而异）



### UmbrelOS：开源版本



UmbrelOS 是 Umbrel 操作系统的免费开源版本。这种灵活的解决方案让您可以使用自己的硬件，同时受益于 Umbrel 的基本功能。



**福利**




- 完全免费
- 开放、可验证的源代码
- 选择自由
- 高级定制选项



**支持的平台**




- Raspberry Pi 5：受欢迎且经济实惠的解决方案
- X86 系统适用于标准个人电脑或服务器
- 虚拟机：用于测试或在现有基础设施上使用



**限制条件




- 仅限社区支持
- 部分高级功能保留给 Umbrel Home
- 技术性更强的初始配置
- 性能取决于所选硬件



该版本适用于 ：




- 技术用户
- 已拥有兼容设备的用户
- 希望学习和尝试的人
- 希望为项目做出贡献的开发人员



官方安装链接 ：




- [在 Raspberry Pi 5 上安装](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [在 x86 系统上安装 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [虚拟机安装](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



在本教程中，我们将专注于在 Raspberry Pi 5 上安装 UmbrelOS，但基本原理与其他平台类似。



## 在 Raspberry Pi 5 上安装 Umbrel OS



### 所需组件



安装时，您需要 ：





- Raspberry Pi 5（4 GB 或 8 GB 内存）
- 正式的 Raspberry Pi 电源 Supply（对稳定性至关重要）
- MicroSD 卡（至少 32 GB）
- 微型 SD 读卡器
- 用于数据存储的外置固态硬盘
- 以太网电缆
- 连接固态硬盘的 USB 电缆



### 安装步骤



**下载 UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- 访问 [官方网站](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- 下载最新版 UmbrelOS for Raspberry Pi 5



**Balena Etcher** 安装



![Téléchargement Balena Etcher](assets/fr/02.webp)




- 下载并在计算机上安装 [Balena Etcher](https://www.balena.io/etcher/)。



**准备 microSD** 卡



![Insertion carte microSD](assets/fr/03.webp)




- 将 microSD 卡插入电脑读卡器



*图像闪烁***



![Flashage UmbrelOS](assets/fr/04.webp)




- 启动 Balena Etcher
- 选择下载的 UmbrelOS 映像
- 选择 microSD 卡作为目的地
- 点击 "Flash！"，等待程序完成
- 安全弹出存储卡



**安装 microSD 卡



![Installation microSD](assets/fr/05.webp)




- 将 microSD 卡插入 Raspberry Pi 5



**外设连接**



![Connexion périphériques](assets/fr/06.webp)




- 将外置固态硬盘连接到可用的 USB 端口
- 在 Pi 和路由器之间连接以太网电缆



**开机



![Démarrage du Pi](assets/fr/07.webp)




- 连接 Raspberry Pi 官方电源 Supply
- 等待几分钟让系统启动



**首次访问**



![Accès interface web](assets/fr/08.webp)




- 在连接到同一网络的设备上，打开浏览器
- 请访问 Umbrel 的 Interface 网站：`http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



如果`umbrel.local`不起作用，您需要在本地网络中找到 Raspberry Pi 的 IP Address。您可以




- 请查阅路由器的 Interface
- 使用 nmap 等网络扫描仪
- 在电脑终端中使用 `arp -a` 命令



## 踏上 Umbrel 的第一步



启动 Umbrel 并可通过浏览器访问后，请按照以下步骤开始操作：



### 初始配置



**创建账户**



![Création compte](assets/fr/10.webp)




- 选择用户名
- 设置安全密码
- 您需要这些凭据才能访问您的 Umbrel



**账户确认



![Confirmation compte](assets/fr/11.webp)




- 点击 "下一步 "进入仪表板



**发现 Interface**



![Interface Umbrel](assets/fr/12.webp)




- 访问 Umbrel 应用程序商店
- 探索多种可用的应用程序
- 首先安装 Bitcoin 的基本应用程序



### 安装 Bitcoin 应用程序



**Bitcoin 节点**



![Bitcoin Node](assets/fr/13.webp)




- 第一个安装的应用程序
- 下载并检查整个 Blockchain Bitcoin



**选举人**



![Installation Electrs](assets/fr/14.webp)




- 连接 Bitcoin 钱包的 Electrum 服务器
- 与 Bitcoin 节点同步



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Blockchain 的 Interface 显示屏
- 实时跟踪交易和区块



## 使用 Mempool.space 跟踪交易



Mempool.space 是一个开源的 Blockchain 浏览器，提供 Bitcoin 网络的实时可视化。您可以通过它跟踪交易，了解交易在网络上的传播情况。



### 了解 Mempool 和确认



Mempool"（内存池）就像一个虚拟的等候室，所有未经确认的 Bitcoin 事务都会先存放在这里，然后才会被纳入区块。下面是交易的处理过程：



1. **广播**：发送交易时，会首先在 Bitcoin 网络上广播


2. **Waiting in Mempool**：等待 Miner 根据费用选定


3. **第一次确认**：未成年人将其列入一个区块（第一次确认）


4. **附加确认**：在包含您的交易的区块之后挖掘出的每个新区块都会添加一个确认



建议的确认次数取决于 ：




- 对于小额付款：1-2 次确认即可
- 对于大笔金额：一般认为 6 次确认非常安全



### 从 Mempool.space 探索 Interface



1. **主页**为您提供 Bitcoin 网络的概况：




   - 最近开采的区块
   - 不同优先事项的成本估算
   - Mempool 的现状



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **搜索交易**：要跟踪特定交易，请将其标识符 (txid) 粘贴到页面顶部的搜索栏中。



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### 分析交易详情



一旦找到您的交易，Mempool.space 将为您提供完整的分析：



1. **基本信息** ：




   - 状态（确认与否）
   - 支付的费用（单位：Sats/vB）
   - 预计确认时间



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **交易结构** ：




   - 输入和输出的可视化表示
   - 所涉地址的详细清单
   - 转账金额



3. **技术数据** ：




   - 交易重量
   - 虚拟尺寸
   - 使用的格式和版本
   - 其他特定元数据



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### 在 Umbrel 上使用 Mempool.space 的优势



1. **保密性**：您的请求将通过您自己的节点处理


2. **独立**：无需依赖第三方服务


3. **可靠性**：即使在公共浏览器瘫痪时也能访问数据



通过该应用程序，您可以有效地监控您的交易，了解费用对确认速度的影响，并更好地了解 Bitcoin 网络的工作原理。



## 将 Wallet Bitcoin 连接到您的节点



### 电子设备配置



**本地连接



![Connexion locale](assets/fr/18.webp)




- 用于本地网络
- 设置更快更简单



*通过 Tor 进行远程连接***



![Connexion Tor](assets/fr/19.webp)




- 从任何地方访问您的节点
- 更安全、更私密



### 与麻雀 Wallet 连接



**获取参数



![Paramètres Sparrow](assets/fr/20.webp)




- 开放式麻雀 Wallet
- 转到首选项 > 服务器
- 点击 "修改现有连接



**选择连接类型



麻雀提供三种连接模式：



*公共服务器****




- 连接到公共服务器（如 blockstream.info、Mempool.space）
- 简单但不那么私密



***Bitcoin核心****




- 与 Bitcoin 节点直接连接
- 私人但速度较慢



***私人电子琴****




- 连接到您的 Electrs 服务器
- 兼具保密性和性能



**选举人**配置



使用我们之前看到的 Electrs 应用程序中显示的信息选择连接类型：



在这两种情况下，请不要选中 "使用 SSL "和 "使用代理 "选项。



**本地连接


主机：umbrel.local


端口号：50001



**远程连接（托尔）**


主机：[your-Address-onion]


端口号：50001



如果要在本地网络之外访问节点，则必须使用 Tor 连接。



![Configuration connexion](assets/fr/21.webp)


有关 Sparrow Wallet 软件的更多信息，我们有一个全面的教程：


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## 结论



您的 Umbrel 现在可以使用了。您可以积极参与 Bitcoin 网络，同时完全控制您的数据。您可以随意探索 Umbrel 应用商店中的许多其他应用程序，以扩展您的家庭服务器的功能。



## 有用资源



### 正式文件




- [Umbrel官方网站](https://umbrel.com)
- [雨伞文件](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin 的应用




- [Bitcoin核心](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### 社区




- [论坛雨伞](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [推特雨伞](https://twitter.com/umbrel)