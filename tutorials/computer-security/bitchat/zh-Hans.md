---
name: Bitchat
description: 去中心化、无互联网的信息传递，实现自由通信
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*BTC Sessions 的本视频教程将指导您设置和使用 Bitchat!


Bitchat 诞生于一次快速原型开发工作中，[@jack](https://primal.net/jack) 在一次周末编码会议上提出了最初的概念。随后不久，[@calle](https://primal.net/calle) 加入了该项目，共同开发 Android 实现。目前，Jack 负责 iOS 版本的开发，而 calle 则在许多其他贡献者的支持下负责 Android 版本的开发。


## 介绍：自由聊天，远离网络


试想一下，在网络瘫痪、发生自然灾害或通信受限的地方发送信息的情景。Bitchat 让这一切成为可能。它是一款去中心化的点对点信息应用，可以跳过中央服务器，让设备之间直接对话，完全离线使用蓝牙和网状网络。Bitchat 在设计时考虑到了隐私和恢复能力，非常适合在传统连接不可靠或不可用的地区使用，例如在灾难情况下、偏远地区，或者对于那些希望躲避监控的人来说。Bitchat 的核心是使用加密技术确保每条信息都经过端到端加密、验证和防篡改。


在本教程中，我们将介绍 Bitchat 的工作原理，以及如何使用它进行真正私密的离线交流。


## 🚀 主要功能


Bitchat 可通过这些 [功能](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features) 实现离线消息传递：



- 跨平台兼容**：iOS 和 Android 之间的协议完全兼容。
- 分散式网状网络**：通过蓝牙低功耗 (BLE) 自动发现同伴和多跳信息中继
- 端到端加密**：X25519 密钥交换 + 用于私人信息的 AES-256-GCM
- 基于频道的聊天**：基于主题的群组消息传送，可选择密码保护
- 存储和转发**：为离线对等设备缓存信息，并在其重新连接时进行传输
- 隐私第一**：无账户、无电话号码、无持久性标识符
- IRC 风格命令：熟悉的 `/join、/msg、/who` 风格界面。
- 信息保留**：可选的全频道信息保存，由频道所有者控制
- 紧急擦除**：轻按三下徽标，立即清除所有数据
- 现代安卓用户界面**：采用 Material Design 3 的 Jetpack Compose
- 深色/浅色主题**：与 iOS 版本相匹配的终端美学风格
- 电池优化**：自适应扫描和电源管理


## 1️⃣Bitchat如何運作 - 簡而言之


Bitchat 可让您直接通过蓝牙（"BLE "如下所示）向附近的手机发送信息，无需互联网或手机信号。开始聊天时，手机会进行安全握手，为对话创建一个唯一的临时加密密钥。每条信息都会受到端到端加密保护，而且每条信息都会使用一个新密钥，以确保过去的信息安全，即使您的手机稍后被入侵也是如此。最后，该应用会将信息分割成小块，并与随机的虚假数据混合，以隐藏你的信息活动。对于设备与设备之间的直接聊天，它只能在大约 100 米的范围内起作用。这就像在拥挤的房间里传递加密纸条一样--设备之间直接窃窃私语，每条信息之后都会撕碎密钥。


Bitchat 还允许您使用 Nostr 协议和 "#geohashes "加入基于位置的聊天室。geohash 是一个简短的代码，如 `#u33d`，代表一个特定的地理区域，小到一个社区，大到整个城市或地区。只需输入标签，您就可以 "远程传送 "到世界各地的任何 geohash 聊天室。您的信息将通过一个分散的中继网络发送，从而保护您的确切位置。此外，每次加入 geohash 聊天室时，您都会获得一个新的临时身份，从而为您基于位置的对话增加了一层额外的隐私保护。


有关更准确的技术细节，请参阅 [官方白皮书](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)。


## 2️⃣安装和设置


### 哪里可以买到 Bitchat


您可以通过以下方式安装 Bitchat



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) （适用于 iOS 设备）
- [Google Play 商店](https://play.google.com/store/apps/details?id=com.bitchat.droid) （适用于安卓设备）


安卓用户也有其他选择：



- 直接从 [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) 页面下载 APK 或
- 通过兼容 Nostr 的 [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr) 安装


![image](assets/en/01.webp)


**注意**：本教程主要侧重于 Android 的实现。iOS 版本可能有所不同。


### 设置过程


安装完成后，打开 Bitchat，即可看到初始权限界面。你需要做的是


1. **授予这些必要的权限：**


   - 蓝牙访问**（发现附近的 Bitchat 用户）
   - 精确定位**（安卓系统需要此功能才能使用蓝牙功能）
   - 通知**（接收私人信息提醒）

2. **禁用电池优化**：


   - 这允许 Bitchat 在后台运行
   - 持续保持网状网络连接


点击 "授予权限"，按照 "提示 "和 "禁用电池优化 "进入下一个屏幕。


![image](assets/en/02.webp)


欢迎来到 Bitchat 的主屏幕。让我们开始吧


### 设置


先说第一件事。点击 "Bitchat 徽标 "可打开设置菜单。  可使用以下选项：



- 设置 "外观"（系统/亮/暗）。
- 为 geohash 启用 "工作证明"，以阻止垃圾邮件（可选）
- 打开 "Tor"，增强隐私保护。


![image](assets/en/16.webp)


### 设置您的身份


点击顶部的 "bitchat/anonXXXX "字段选择用户名。这将是他人在蓝牙和互联网模式下看到您的方式。例如，您可以将 "anon2022 "更改为您选择的用户名。


![image](assets/en/03.webp)


### 选择网络频道


使用 "#location channels "菜单（用户名右侧）切换连接类型：



- BLE 网状***：默认蓝牙模式（无网络，距离 10 至 50 米）
- #geohashes**：使用 [Nostr 协议] 的互联网地理社区(https://nostr.com/)


当您选择 "#geohashes "模式时，Bitchat会与Nostr协议集成，以启用地理社区。您的消息会发布到 "分散的 Nostr 中继器"，而不是 Bitchat 的点对点网络，这样就可以进行更广泛但经过位置过滤的对话。最重要的是，您的 Bitchat 身份密钥会对所有 Nostr 事件进行加密签名，以保持身份验证，而 geohash 标签（如邻里的 `#u4pruyd`）会根据您选择的精确度过滤消息。这意味着您可以参与本地讨论，而无需透露确切坐标，不过需要互联网接入。


![image](assets/en/04.webp)


### 监测同行

许可证CC-BY-SA-V4

对等计数器显示用户：



- 附近（BLE 网格）或
- 在您的 geohash 区域 (#geohashes)


![image](assets/en/05.webp)


## 3️⃣全球聊天和私人信息


Bitchat 提供两种不同的通信模式，以满足不同的需求：



- 公共频道：** 用于与他人公开对话。您可以通过本地 BLE 网状网络连接附近的用户，也可以通过全球 #geohash 连接支持互联网的位置社区。
- 私人信息：** 用于一对一的安全对话。这些信息会建立直接的加密连接，为您的交流保密。


了解这两种模式将有助于您在对话中游刃有余。


### 公共渠道：社区中心


定位频道 "菜单（右上角）控制您的公开可见性。选择 "mesh "可通过 BLE 网状连接到附近的所有用户，通常是 10-50 米范围内的设备。这将创建一个开放论坛，向范围内的每个人广播信息，非常适合发布活动公告或本地警报。


如需更广泛的地理覆盖范围，可选择任何 "#geohash "标签，加入按位置筛选的互联网社区。这些频道使用 Nostr 协议中继，允许跨城市或跨地区通信，同时保持基于位置的相关性。您的信息会实时显示给同一频道中的其他人，新参与者加入后会自动看到最近的信息历史记录。


![image](assets/en/06.webp)


### 私人对话：安全加密


要开始私人对话，请直接单击 "用户概览 "中显示的任何 "用户名"。您还可以点击 "星形图标 "将该用户标记为收藏夹，这样即使该用户处于离线状态，也会在联系人列表中保持可见。


![image](assets/en/07.webp)


当您开始私聊时，Bitchat 会自动启动 "安全握手"。设备交换短暂密钥，为您的对话创建专门的加密隧道。通过持续的端到端加密，这一过程可确保您的所有信息和共享文件保持机密。私密信息支持文本和文件共享。


![image](assets/en/08.webp)


## 4️⃣附加功能


您可以在 Bitchat 的任意位置输入 `/`，立即访问操作面板。这将显示一个用于快速操作的命令菜单。



- 管理连接**：屏蔽用户 "或 "解除屏蔽对等体
- 频道控制**：显示频道 "或 "加入/创建频道
- 社会交往**：送上热情拥抱 "或 "用鳟鱼拍打" 🎣
- 聊天维护**：清除聊天信息
- 隐私工具**：查看在线人员 "或 "发送私人信息


命令会立即执行，如"/block Satoshi "让批评者闭嘴，或"/hug Hal "传播积极的信息🫂。


![image](assets/en/09.webp)


## 5️⃣创建频道


Bitchat 中的频道可以围绕主题、地点或社区进行有组织的交流。要创建自己的频道，请遵循以下工作流程：


### 步骤 1：创建频道


要创建频道，请在任何聊天工具中输入 `/j` 或 `/join`，然后输入频道名称（例如 `/j <频道名>`）。创建后会出现一个新的 `icon ⧉`，表示新频道。其他用户可以输入相同的命令（例如 `/j bitchat_tutorial`）加入。


![image](assets/en/10.webp)


### 步骤 2：配置设置


除默认命令外，通道内还提供以下设置：



- `/save`用于在本地保存信息
- `/transfer` 转移通道所有权和
- /pass`更改频道密码。


对于私人社区，该命令可启用密码保护，要求获准成员在加入前输入自定义密码。


## 6️⃣紧急模式


现在，让我们来谈谈 "恐慌模式"：点击三下 "Bitchat "徽标，应用程序中的所有本地消息和数据就会被完全清除。这是你的终极隐私保障，非常适合需要立即谨慎处理的情况。


**重要提醒：** _"恐慌 "模式是永久性的。一旦激活，数据将无法恢复。请谨慎使用。


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash 频道可根据 "地理位置 "而非传统网络连接进行有针对性的对话。该功能将bitchat转变为一种位置感知通信工具，是本地协调、社区建设和特定位置讨论的理想选择。


### #geohashes#如何工作


该系统使用[Geohash 系统](https://en.wikipedia.org/wiki/Geohash) 将世界划分为网格方格，哈希值中的每个字符都代表更高的精度：



- 4**级（如`u33d`）：覆盖范围约为 25km × 25km - 全城讨论的理想选择
- 6** 级（如`u33d8z`）：覆盖范围约为 1.2 千米 × 1.2 千米 - 邻域精度
- 8** 级（例如，`u33d8z1k`）：覆盖范围约为 150 m × 150 m - 街道分段精度


精确选择兼顾了隐私和实用性：级别越高，创建的专属区域越多，但能更精确地显示您的位置。


### 加入 `#geohash` 频道


1.进入 "#定位频道 "菜单。

2.选择所需的精度等级，然后输入 `#geohash`（例如 #u33d）。

3.轻按 "Teleport "按钮加入 "#location channel"。


![image](assets/en/12.webp)


或者，您也可以点击 "地图图标"，使用地图视图来确定精度级别，然后点击 "选择 "加入 "#定位频道"。


![image](assets/en/13.webp)


**重要提醒**：_#geohash功能需要激活的互联网连接--与通过蓝牙离线操作的BLE网格不同。


## 8️⃣热图


热图是发现世界各地 Bitchat 活动和频道的一种很酷的方式。[位图](https://bitmap.lat/) 可视化并追踪 Nostr 网络中基于位置的匿名消息，显示短暂的 Nostr 事件。看一看并加入特定地点的频道和聊天。


![image](assets/en/15.webp)


## 🎯 结论


Bitchat 可在传统信息传递失败的情况下实现安全、分散的通信。它能够利用 BLE 网状网络在没有互联网基础设施的情况下运行，因此适用于抗议活动、灾区和连接受限或审查的偏远地区。该应用通过历时密钥加密、基于 geohash 的定位通道和恐慌模式数据清除功能确保隐私。


该应用程序仍处于早期开发阶段，但已初见成效。用户应注意偶尔出现的错误，并通过 [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) 报告问题。计划中的改进包括使用 Cashu 协议进行应用程序内私人交易的 "ecash "集成。


![image](assets/en/14.webp)


## 📚 Bitchat 资源


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)