---
name: Start9

description: 建立 Start9 私人服务器教程

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*以下是来自 Southern Bitcoiner 的视频教程，向您介绍如何设置和使用 Start9 / StartOS 个人服务器，以及如何运行比特币节点。


## 1️⃣引言


### Start9 究竟是什么？


Start9是一家成立于2020年的公司，以开发[**StartOS**](https://github.com/Start9Labs/start-os)而闻名，这是一个基于Linux的操作系统，专为个人服务器设计。它使用户能够轻松地自助托管各种软件服务，如Bitcoin和Lightning节点、消息应用程序或密码管理器，同时保持对其数据的完全控制，并消除对集中式技术平台的依赖。StartOS拥有用户友好的浏览器界面、用于安装服务的精选市场，以及内置的隐私工具，如Tor集成和全系统HTTPS加密。Start9 还提供预装操作系统的硬件设备，不过软件也可以安装在兼容的硬件或虚拟机（VM）上。


### 有哪些选择？


Start9 提供预制和 DIY 部署选项。Server One**](https://store.start9.com/collections/servers/products/server-one)和[**Server Pure**](https://store.start9.com/collections/servers/products/server-pure)是官方硬件设备，采用高性能组件：Server One使用**AMD Ryzen 7 5825U**处理器，可配置内存（16GB-64GB）和存储（2TB-4TB NVMe SSD）；Server Pure配备**英特尔i7-10710U**，也可配置内存和存储选项。如果直接从Start9购买，这两款产品都包含**终身技术支持**。对于喜欢灵活性的用户，StartOS 可以免费安装在各种现有硬件上，包括笔记本电脑、台式机、迷你 PC 和单板计算机，也可以安装在虚拟机中。


![image](assets/en/01.webp)


### 与 Umbrel 有什么不同？


StartOS 和 Umbrel 都能简化自托管服务的安装，但在架构和功能上有所不同。Umbrel 在 Debian/Ubuntu 系统或虚拟机上作为应用层运行，而 Start9 是专用操作系统，需要直接安装硬件或虚拟机。Umbrel 的界面美观大方，受到 macOS 的启发，而 Start9 则将功能性和简约设计放在首位。Umbrel 提供了更多的[应用程序选择](https://apps.umbrel.com/)，而[Start9 Marketplace](https://marketplace.start9.com/)则以先进的技术能力作为补偿。Start9 通过有效的用户界面表单简化了高级设置的访问，减少了命令行交互的需要。它在备份管理方面也很出色，可以进行一键式加密系统备份，而这正是 Umbrel 原生缺乏的功能。StartOS 提供内置监控工具，并对本地网络访问执行 HTTPS 加密，从而提高了安全性。Umbrel 在本地使用未加密的 HTTP，不过两个平台都支持通过 Tor 进行安全的远程访问。Umbrel 适合优先考虑丰富应用生态系统和完善用户界面的用户。对于那些重视安全性、可配置性、备份可靠性和高级服务管理而不需要命令行专业知识的用户来说，Start9 是一个不错的选择。要了解有关 Umbrel 以及与 Start9 不同之处的更多信息，请访问本课程：


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY 先决条件：最低和推荐规格


对于使用最低限度服务的基本用途，**最低规格**为 **1 个 vCPU 内核（主频 2.0GHz 以上）、4GB 内存、64GB 存储**和一个以太网端口。尽管如此，我还是建议远远超出这一要求，尤其是在运行 Bitcoin 节点的情况下。就我个人而言，我一开始用的是 1TB，但很快就用完了。更好的目标是**至少 2TB 存储空间**，以及**四核 CPU（2.5GHz 以上）**和**8GB 以上内存**。这将在性能和使用寿命方面产生巨大的差异。如果你想深入了解，这里有一个关于[可运行 StartOS 的硬件](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229)的最新社区主题。


## 3️⃣下载和刷新固件


要开始设置，请使用另一台计算机访问[Start9 网站](https://start9.com/)，点击 "DOCS "进入文档部分。从那里，访问 "Flashing Guides"，找到相应版本的 StartOS。有两个选项：



- 启动操作系统（树莓派）
- 启动操作系统（X86/ARM）


本教程涉及 "x86/ARM "选项。


最新的操作系统版本可从[Github 发布页](https://github.com/Start9Labs/start-os/releases/latest) 下载。希望测试新功能的用户也可使用[预发布](https://github.com/Start9Labs/start-os/releases) 版本。在页面底部的 "Assets "下，下载 "x86_64 "或 "x86_64-nonfree.iso"。  x86_64-nonfree.iso "镜像包含 Server One 和大多数 DIY 硬件（尤其是图形和网络设备支持）所需的非自由（闭源）软件。


建议通过检查文件的 SHA256 哈希值与 GitHub 上列出的哈希值来验证文件的完整性。对于 Linux，可以使用 "sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso "命令，其他操作系统请参见文档。


下载并验证 StartOS 映像后，必须将其闪存到 USB 驱动器上。建议使用 "BalenaEtcher "软件来完成这项任务。它是一款免费的开源工具，用于将操作系统映像文件写入 USB 驱动器和 SD 卡，适用于 Windows、macOS 和 Linux。从 [Balena Etcher 官方网站](https://www.balena.io/etcher/) 下载相应版本，并运行安装程序。连接目标 USB 驱动器或 SD 卡，打开 Balena Etcher，点击 "从文件闪存 "选择下载的操作系统映像。Etcher 会自动检测连接的驱动器；如果有多个驱动器，请选择正确的目标。点击 "Flash!"开始写入映像。完成后，Etcher 会自动验证写入过程。完成后，安全地移除硬盘，并用它来启动设备。


![image](assets/en/19.webp)


## 4️⃣初始设置


有关初始设置，请参阅 Start9 [documentation](https://docs.start9.com/0.3.5.x/) 页面下的 "用户手册"，然后是 "入门 - 初始设置"。  应参考此官方指南以获取最新信息。


提出了两个方案：



- 重新开始
- 恢复选项


对于新的服务器安装，请选择 "重新启动"。首先，连接服务器电源和以太网电缆。确保用于设置的计算机在同一个本地网络上。从计算机中取出新刷新的 USB 驱动器并将其插入服务器。


您可以从同一网络上的任何计算机远程控制服务器。打开网络浏览器并导航至 `http://start.local`。


**注意**：如果该地址出现连接问题，通常是由于家庭网络无法解析`.local`域名。可以通过直接访问服务器的 IP 地址来解决问题。登录路由器的管理界面（通常是 192.168.1.1 或类似地址），在 DHCP 客户端或网络地图列表中找到设备，即可找到 IP 地址。然后，在浏览器中输入完整的 IP 地址（如 `http://192.168.1.105`）。这将绕过 DNS 解析。如果问题仍然存在，请查阅[常见问题页面](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) 或[联系他们的支持部门](https://start9.com/contact/)


应该会出现 StartOS 设置屏幕。单击 "重新启动 "开始新服务器设置。


![image](assets/en/03.webp)


下一步是选择存储 StartOS 数据的硬盘。


![image](assets/en/04.webp)


为服务器设置一个强大的 "密码"。按照 Start9 的建议将其记录下来，然后点击 "完成"。


![image](assets/en/05.webp)


屏幕将显示 StartOS 正在初始化和设置服务器。下一步是 "下载地址信息"，因为 "start.local "地址仅用于设置，之后将无法使用。


![image](assets/en/06.webp)


配置文件包含两个关键访问地址：一个用于 "本地网络 (LAN)"，另一个用于通过 "Tor "进行安全访问。这两个地址都应保存在安全的密码管理器中。下一步是 "信任您的根 CA"。打开一个新的浏览器标签，按照说明信任根 CA 并登录。也可点击下载文件中的 "下载证书 "下载根 CA 证书。


## 5️⃣信任你的根 CA


下载证书后，服务器的 "根 CA "必须得到操作系统的信任。单击 "查看说明"，找到特定操作系统的指南。


![image](assets/en/07.webp)


对于 Linux 系统，可使用以下命令。首先，打开终端并安装必要的软件包：


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


导航至下载证书的目录，通常为 `~/Downloads` 。执行以下命令，将证书添加到操作系统的信任存储中。使用 `cd ~/Downloads` 更改到下载文件夹。使用 `sudo mkdir -p /usr/share/ca-certificates/start9` 创建所需目录。复制证书文件，使用 `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/` 将 `your-filename.crt` 替换为实际文件名。使用 `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`将证书路径添加到系统配置中，永久注册证书。最后，使用 `sudo update-ca-certificates` 重建信任存储。在执行这些命令前，必须使用实际的证书文件名并验证所有路径。此过程将为 Start9 服务器的 HTTPS 连接建立永久信任。


安装成功后，输出将显示 "已添加 1"。然后，大多数应用程序都能通过 `https` 安全连接。如果使用 Firefox，则需要额外的 [最后一步](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff)。如果使用 Chrome 或 Brave，则需要另一个 [最后步骤](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome)，以配置浏览器尊重根 CA。刷新页面测试连接。如果问题仍然存在，请退出并重新打开浏览器，然后再重新访问页面。


![image](assets/en/08.webp)


## 6️⃣开始使用 StartOS


现在应该可以使用安全 HTTPS 连接登录了。输入 "密码 "以访问 "欢迎屏幕"。


![image](assets/en/09.webp)


该屏幕为入门提供了有用的快捷方式。左侧边栏包含用于导航的主菜单项。


## 7️⃣系统


StartOS 中的 "系统 "选项卡可访问用于管理个人服务器的核心系统功能。它提供了用于系统维护、安全、诊断和配置的工具，无需命令行专业知识。


备份 "部分允许创建完整的系统备份，包括服务、配置和数据，以便日后恢复。这对于灾难恢复或迁移到新硬件至关重要。备份可以存储在外部驱动器上，并使用主密码进行加密。


系统 "选项卡中的 "管理 "部分允许对关键系统功能进行控制。用户可以手动检查并应用 StartOS 更新，保持对系统更新过程的控制。可以侧载官方市场上没有的自定义或第三方服务。如果服务器未通过以太网连接，则可在此部分配置 Wi-Fi 设置。高级用户可以启用 SSH 访问，进行终端级系统管理。


![image](assets/en/10.webp)


Insights" 部分可实时监控服务器的性能和健康状况，通过图表显示 CPU、内存和磁盘的使用情况。它还能显示系统温度，这对 Raspberry Pi 等缺乏主动冷却的设备非常有用。正常运行时间和平均负载指标有助于评估系统稳定性，实时日志可用于排除服务或系统问题。


在 "支持 "部分，用户可以访问内置的常见问题、官方文档和社区支持频道。可从该部分下载调试日志，与 Start9 支持人员共享，以便更快地解决问题。


![image](assets/en/11.webp)


## 8️⃣市场


市场 "用于发现、安装和管理个人服务器上的服务。它提供对 Bitcoin Core、BTCPay Server 和 electrs 等软件的访问。StartOS支持多个市场，包括官方的Start9注册表和社区运营的注册表。点击 "CHANGE "并切换到 "Community Registry"，即可添加这些注册表，从而访问更广泛的服务。


![image](assets/en/12.webp)


## 9️⃣ 安装 Bitcoin 全节点


在 StartOS 上安装 Bitcoin full node 可为 Bitcoin 体验提供完全主权。它可以验证交易，并通过消除对可能记录活动的外部服务的依赖来增强隐私和安全性。对交易进行完全控制，允许交易直接向网络广播。默认选项是 "Bitcoin Core"，它与 StartOS 原生集成，允许与 Specter、Sparrow 或 Electrum 等钱包连接，进行自我托管设置。社区注册中心还提供了另一种选择，即 "Bitcoin Knots"。


要安装 Bitcoin Core，请导航至 "市场"。在默认注册表下找到并安装 Bitcoin Core 服务。安装后，会出现 "Needs Config"（需要配置）提示，要求在服务运行前完成设置。这通常会在更新或全新安装后出现，并提示查看 "RPC 设置"。使用默认配置并单击 "保存"。


![image](assets/en/13.webp)


一旦完全同步，您的节点就可以作为 Sparrow 等钱包的私人后台，提供更高的隐私性和交易验证。但是，对于存储大量数据的用户来说，了解这种直接连接的安全权衡至关重要。当 wallet 直接连接到 Bitcoin Core 时，可能会暴露敏感数据，因为 Bitcoin Core 会在主机上未加密地存储公钥（xpubs）和 wallet 余额。如果系统受损，攻击者就有可能发现您持有的数据，并将您作为攻击目标。


为了降低这种风险，实现更强大的安全模式，您可以建立一个私人 Electrum Server。该服务器充当中间人，为区块链编制索引，但不存储任何 wallet 特定信息。通过将 wallet 连接到自己的 Electrum 服务器，而不是直接连接到 Bitcoin Core，可以防止 wallet 访问节点的敏感数据。


![image](assets/en/14.webp)


## 🔟 设置电子设备


electrs（Electrum Rust 服务器）是一个快速、高效的索引器，可连接到您的 Bitcoin 核心节点，使 Electrum 兼容钱包能够实时查询交易历史和余额。通过在 StartOS 上运行 electrs，您无需依赖第三方 Electrum 服务器，从而大大提高了隐私性和安全性--您的 wallet 查询将直接转到您的自托管节点。


要进行设置，首先要从 StartOS Marketplace 安装 electrs 服务。在继续之前，系统需要完全同步 Bitcoin Core。安装完成后，按照建议的默认值确认 "Needs Config "设置，electrs 就会开始为区块链编制索引，这可能需要一天时间，具体取决于您的硬件。


![image](assets/en/15.webp)


完成后，您就可以连接 Sparrow 或 Specter 等钱包。连接成功后，您的 wallet 就可以直接与您的节点同步，从而提供安全、私密和自我托管的 Bitcoin 体验。


## 1️⃣ 1️⃣ 连接 Sparrow Wallet


要使用 electrs 实现将 `Sparrow Wallet` 连接到 StartOS 节点，首先要确保 Bitcoin Core 已完全同步，并且 electrs 已安装和运行。在设备上打开 Sparrow Wallet，然后导航到 `File` -> `Settings` -> `Server`。然后选择 `Private Electrum Server`。在 URL 字段中输入 electrs 的 `Tor 主机名`和 `端口`，您可以在 StartOS 中的 `服务` -> `electrs` -> `属性`（通常以 `.onion:50001`结尾）下找到。


![image](assets/en/16.webp)


接下来，选中 "使用代理"，将代理地址设置为 "127.0.0.1"，端口设置为 "9050"，从而启用 Tor。点击 "测试连接 "并等待片刻。连接成功后会显示一条确认信息，如 "已连接到电子设备"。验证后，关闭设置并继续创建或恢复 wallet。此设置可确保您的 wallet 通过 electrs 查询自己的节点，提供完全的隐私和无信任操作。


![image](assets/en/17.webp)


## 🎯 结论


Start9的StartOS是一个用户友好、注重隐私的平台，专为自托管Bitcoin和闪电节点、钱包和个人应用程序等基本服务而设计。它提供简洁的图形界面、自动备份、健康监控和安全的 Tor 访问，因此无需命令行技能，非常适合非技术用户使用。它的模块化架构支持与 electrs 或 Sparrow 等工具的无缝集成，让你完全掌控自己的财务和数字主权。StartOS 非常注重透明度、本地控制和可扩展性，它使用户能够从集中式平台中夺回所有权，并运行自己的私有弹性基础设施。