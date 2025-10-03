---
name: Tailscale
description: 尾标高级教程
---
![cover](assets/cover.webp)



## 1.导言



Tailscale 是下一代 VPN，可在设备之间创建加密网状网络。它能让你像在同一个本地网络上一样连接远程机器，无需复杂的配置或端口开放。



对于自助托管，Tailscale 在虚拟网络中为每个设备分配一个固定的私有 IP，即使您的公共 IP 发生变化，也能稳定地访问您的服务。这意味着您可以远程管理服务器，而无需将服务直接暴露在互联网上。



**主要应用：**




- 从外部管理个人服务器
- 管理 Umbrel/Lightning 节点的速度比 Tor 更快
- 安全访问 Raspberry Pi 或 NAS
- 通过 SSH 或 HTTP 连接服务，无需复杂的网络配置



这种以简化为重点的方法使自助托管商能够安全地访问其服务，避免了传统 VPN 的隐患。



## 2.Tailscale 如何工作



传统 VPN 通过中央服务器传输所有流量，而 Tailscale 与之不同，它创建了一个网状网络，设备之间可以直接通信。中央服务器只处理身份验证和密钥分发，不查看用户数据。



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*图 1：传统 VPN 采用枢纽-辐条架构，所有流量都通过中央服务器*传输



基于 WireGuard，每个设备都会生成自己的加密密钥。协调服务器将公开密钥分发给节点，然后节点之间直接建立端到端加密隧道。为了穿越防火墙，Tailscale 使用了 NAT 穿越技术，最后还使用了保持加密的 DERP 中继器。



![VPN maillé (mesh)](assets/fr/02.webp)


*图 2：设备之间直接通信的尾级网状网络*



所有通信均使用 WireGuard 加密。Tailscale 只能看到元数据（连接），而看不到交换内容。为了获得更大的主权，Headscale 允许协调服务器自行托管。



**安全性和保密性：** 由于采用了 WireGuard，Tailscale 上的所有通信都经过端到端加密。Tailscale 无法读取您的流量，只有您的设备才拥有必要的私钥。服务只能看到元数据：IP 地址、设备名称、连接时间戳和点对点连接日志（无内容）。



然而，这种架构在网络协调方面依赖于 Tailscale Inc.为了消除这种依赖性，Headscale 提供了一种开源替代方案，允许您在使用官方 Tailscale 客户端的同时自行托管控制服务器，从而保证您对网络基础设施的完全主权，但代价是需要更多的技术配置。



**要详细了解 Tailscale 的内部工作原理，包括控制平面管理、NAT 穿越和 DERP 中继，我们向您推荐官方博客上的优秀文章** [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works)**。这篇文章深入解释了使 Tailscale 如此强大的技术概念。**



## 3.安装 Tailscale



Tailscale 可在**常见的**操作系统（Windows、macOS、Linux、iOS 和 Android）上运行。据说在所有平台上的安装都 "简单快捷"。让我们先来看看 Interface 和如何创建账户，然后再了解不同环境下的安装程序。



### 3.1 创建 Tailscale 账户



访问 [https://tailscale.com/](https://tailscale.com/)，点击页面右上方的 "开始 "按钮。




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscale 主页解释了这一概念，并提供了免费入门*。



要使用 Tailscale，首先需要通过身份提供商创建一个账户：



![Page de connexion Tailscale](assets/fr/04.webp)


*选择身份提供商连接到 Tailscale（Google、Microsoft、GitHub、Apple 等）*。



登录后，Tailscale 会要求你提供一些有关你的预期用途的信息：



![Questionnaire d'utilisation](assets/fr/05.webp)


*更好地了解您的使用情况（个人或专业）的表格*



创建账户后，即可在设备上安装 Tailscale：



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale 可让您在不同的系统上安装应用程序*。



### 3.2 在不同平台上的安装





- 在 Windows 和 macOS 上：只需从 Tailscale 官方网站下载图形应用程序并安装（Windows 为 .msi 文件，Mac 为 .dmg 文件）。安装后，应用程序会启动图形 Interface，让你（通过浏览器）连接到 Tailscale 账户，以验证机器。



![Connexion d'un appareil macOS](assets/fr/08.webp)


*将 MacBook 连接到尾网*



![Connexion réussie](assets/fr/09.webp)


*确认设备已连接至 Tailscale* 网络





- 在 Linux（Debian、Ubuntu 等）上：**您有几种选择。最简单的方法是运行官方安装脚本：例如，在 Debian/Ubuntu：**



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



该脚本将添加 Tailscale 官方软件源并安装软件包。你也可以 [手动添加 APT 仓库](https://pkgs.tailscale.com) 或使用普通 Snap 或 apt 软件包。安装完成后，daemon `tailscaled` 将在后台运行。然后，您需要**验证节点**（见下文 Interface CLI 与 web 的对比）。在其他发行版（Fedora、Arch......）上，该软件包也可通过标准软件仓库或通用安装脚本获得。对于无头服务器，请使用 CLI：例如，如果使用预先生成的身份验证密钥，请使用 `sudo tailscale up --auth-key <key>`；如果使用交互式登录，请使用 `tailscale up`（它将提供一个访问 URL 以验证设备身份）。





- 在基于 ARM 的系统（Raspberry Pi 等）上：**我们通常使用 Linux，因此方法与上述相同（脚本或软件包）。请注意，Tailscale 支持 ARM32/ARM64 架构，不会出现任何问题。许多用户通过 apt 或轻量级发行版（DietPi 等）将 Tailscale 安装在 Raspberry Pi 操作系统上，以便随处访问他们的 Pi。**





- 在 iOS 和 Android 上：**Tailscale 提供官方移动应用程序**。只需从 [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) 或 [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android) 安装 *Tailscale* 即可。



![Installation sur iPhone](assets/fr/11.webp)


*在 iPhone 上安装 Tailscale 的步骤：欢迎、隐私、通知、VPN*。



![Connexion sur iPhone](assets/fr/12.webp)


*连接到 tailnet，选择账户并在 iPhone 上验证*。



安装应用程序后，首次启动时会要求你通过所选的提供商（谷歌、Apple ID、微软等，取决于你在 Tailscale 上使用的提供商）进行身份验证--这与其他平台上的程序相同，通常是重定向到 OAuth 网页。之后，移动应用程序会创建 VPN（在 iOS 上，你需要接受 VPN 配置插件）。然后，应用程序就可以在后台运行，让您可以随时随地访问您的尾网。 *请注意：* 在移动设备上，一次只能有**个活动 VPN**，因此请确保您没有同时连接其他 VPN，否则 Tailscale 将无法建立自己的 VPN。在安卓系统上，如果你想隔离某些用途（例如，在特定应用程序中使用 Tailscale 的配置文件），你可以设置一个单独的工作配置文件。



### 3.3 添加多个设备和验证



连接第一台设备后，Tailscale 会提示你添加其他设备到网络：



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface 显示已连接的第一个设备，并正在等待其他设备*。



添加多个设备后，就可以检查它们是否能相互通信了：



![Test de connectivité entre appareils](assets/fr/13.webp)


*确认设备之间可以通过 ping* 进行通信



然后，Tailscale 会建议其他配置，以增强您的体验：



![Suggestions de configuration](assets/fr/14.webp)


*关于设置 DNS、共享设备和管理访问的建议*。



### 3.4 管理仪表板



通过网络管理控制台，您可以查看和管理所有连接的设备：



![Tableau de bord des machines](assets/fr/15.webp)


*连接设备列表及其特性和状态*



**Interface Web 与 Interface CLI：** Tailscale 提供两种互补的网络交互方式：**Interface Web 管理**和**命令行客户端 (CLI)**。





- Interface Web（管理控制台）：可通过 [https://login.tailscale.com](https://login.tailscale.com)访问，该网络控制台是 Tailscale 网络的中央控制台。它列出了所有设备（**机器**）、它们的在线/离线状态、它们的 Tailscale IP 地址等。在这里，您可以**管理设备**（重命名、密钥过期、授权路由、禁用节点）、**管理用户**（在组织范围内）以及定义安全规则（ACL）。您还可以在这里配置 MagicDNS、标签或验证密钥（generate 之前的验证密钥用于自动添加设备）等全局选项。Interface Web 对于概览和应用将通过协调服务器传播到所有节点的更改非常方便。**例如：**一旦有关节点宣布自己是**子网路由**或**退出节点**，只需在控制台中点击一下即可激活。





- Interface 命令行 (CLI)：** `tailscale` 命令可在安装了 Tailscale 的每台设备上的 CLI 中使用。通过 CLI，您可以在本地完成所有操作：连接（`tailscale up`）、检查状态（`tailscale status`，查看哪些对等设备已连接）、调试（`tailscale ping <ip>`）等。有些功能甚至是 CLI 的**独有功能或更高级的功能，例如





  - tailscale up --advertise-routes=192.168.0.0/24` 来公布子网路由、
  - tailscale up --advertise-exit-node` 来建议将你的机器作为退出节点、
  - tailscale设置--accept-routes=true`（或`--exit-node=<IP>`）以使用路由或出口节点、
  - tailscale ip -4` 以显示设备的尾标 IP、
  - 尾标锁定/解锁"（如果使用 *tailnet-lock* 高级安全功能）、
  - 或 `tailscale file send <node>` 来使用 **Taildrop**（设备间文件传输）。


CLI 在没有 Interface 图形的服务器上非常有用，还可用于编写某些操作的脚本。 **使用中的差异：** 大多数基本配置可通过网络或 CLI 进行。例如，添加设备可以通过控制台提示，或在设备上运行 "tailscale up "并通过网络验证。同样，重命名设备也可以通过控制台或`tailscale set --hostname` 来完成。 **总之**，网络控制台是全局网络管理的理想选择（尤其是在多台机器/用户的情况下），而 CLI 则便于对特定机器、自动化脚本进行细粒度控制，或在没有图形用户界面的系统上使用。



## 4.在 Umbrel 上使用 Tailscale



Umbrel 是一个流行的自托管平台（主要用于 Bitcoin/Lightning 节点和其他自托管服务，通过其应用程序商店）。要安装和配置 Umbrel，我们建议您按照我们的专门教程 ：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

将 Umbrel 和 Tailscale 结合使用是一个特别有趣的用例，因为 Umbrel 本机集成了易于部署的 Tailscale 模块。以下是 Tailscale 如何与 Umbrel 集成及其带来的好处：



### 4.1 伞形筒的安装和配置





- 在 Umbrel 上安装 Tailscale：**Umbrel 的应用程序商店中有 Tailscale 官方应用程序。安装再简单不过了：**



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Umbrel App Store 中的 Tailscale 应用程序页面*



从 Interface Web Umbrel 打开应用程序商店，搜索**Tailscale**，然后点击*Install*。几秒钟后，应用程序就会安装到 Umbrel 上。打开后，Umbrel 会显示一个页面，允许您将节点链接到 Tailscale。



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Umbrel 的 Interface* 中的尾鳞连接屏幕



只需**点击 "登录 "**，就会跳转到 Tailscale 身份验证页面：



![Page d'authentification Tailscale](assets/fr/18.webp)


*通过身份提供商连接到 Tailscale*



您可以通过 Tailscale 帐户（Google/GitHub/等）或输入您的电子邮件进行验证。通常，在 Umbrel 上，Interface 会要求你访问 [https://login.tailscale.com](https://login.tailscale.com)并登录--这将验证 Umbrel Tailscale 应用程序。



![Confirmation de connexion réussie](assets/fr/19.webp)


*确认 Umbrel 设备已连接至 Tailscale 网络*。



完成后，您的 Umbrel 将 "进入 "您的 Tailscale 网络，并以名称（如 *umbrel*）出现在您的控制台上。然后，您可以点击设备的 IP Address 进行复制，检索与设备相关联的 IPv6 Address 或 MagicDNS。



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscale 管理控制台显示多个已连接的设备，包括 Umbrel*




### 4.2 远程访问 Umbrel 服务



一旦 Umbrel 连接到 Tailscale，**你就可以在任何地方访问 Interface Umbrel 及其上运行的应用程序，就像在本地网络上一样**。这是 Tor 的主要优势之一。



访问非常简单：您无需使用 `umbrel.local`（只能在本地网络上使用），而是直接从连接到 tailnet 的任何设备上使用 Umbrel 的 Tailscale IP Address (`http://100.x.y.z`)。无论您身在何处，使用何种网络连接（4G、公共 Wi-Fi、公司网络），都能正常工作。



**可通过 Tailscale 访问的 Umbrel 托管应用程序示例：**





- Interface 主 **Umbrel**：只需在浏览器中输入 `http://100.x.y.z` 即可访问您的 Umbrel 仪表板
- **Bitcoin 节点**：无延迟管理 Bitcoin 节点，查看同步和统计数据
- Lightning 节点：使用ThunderHub、RTL或其他Lightning管理界面，即时响应
- **Mempool**：查看 Bitcoin 交易和 Mempool 无 Tor 延迟
- **noStrudel**：访问托管在 Umbrel 上的 Nostr 服务



**通过 Tailscale 将外部钱包连接到 Bitcoin 或 lightning 节点：**



Tailscale 还能让安装在其他设备上的 Bitcoin 和 Lightning 钱包直接连接到 Umbrel 节点：





- **Sparrow wallet (Bitcoin)**：这个外部 Wallet Bitcoin 可以使用 Tailscale IP Address 直接连接到 Umbrel 的 Electrum 服务器：



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*使用 Umbrel 的 Tailscale IP Address* 在 Sparrow wallet 中配置私人 Electrum 服务器



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*带有 Umbrel Tailscale IP Address* 的 Sparrow 中的 Electrum 服务器别名列表



请阅读我们的完整指南，了解如何将 Sparrow wallet 与您的 Bitcoin 节点进行配置：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- 宙斯（闪电）：这个 Wallet 移动 Lightning 可以连接到 Umbrel 上的 Lightning 节点。无需将端点配置为".onion"，只需设置 Umbrel 的 Tailscale IP 和 Lightning API 端口。与 Tor 相比，连接将是瞬时的。



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*配置 Zeus 通过 Tailscale* IP Address 连接到 Lightning 节点



要在 Lightning 节点上配置 Zeus，请参阅我们的详细教程 ：



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

要进一步了解 Lightning Network 及其在 Umbrel 上的工作原理，请访问 ：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 与 Tor 相比的优势



Umbrel 本机通过 Tor（为其网络服务提供`.onion`地址）提供远程访问。虽然 Tor 具有保密（匿名）和无需注册的优势，但许多用户发现**Tor 在日常使用中速度缓慢且不稳定**（网页加载缓慢、超时等）--*"通过 Tor 访问 Umbrel 太慢了 "* 一些人抱怨道。



Tailscale 通常提供**快、低延迟的**连接，因为流量直接通过（或通过快速中继），而不是通过 3 个 Tor 节点跳转。此外，Tailscale 还提供了 "本地网络 "体验：使用私有 IP，应用程序可以直接映射（例如，SMB 网络驱动器上的 \100.x.y.z）。



也就是说，Tor 的优势在于去中心化和 Umbrel 的 "开箱即用"，而 Tailscale 则需要信任第三方（或托管 headcale）。Tor 对于无客户端访问也很有用（通过任何 Tor 浏览器，你都可以查看 Umbrel 的用户界面，而 Tailscale 则需要在访问设备上安装客户端）。



**总而言之**，对于交互式使用（闪电钱包、频繁的网络界面），Tailscale 与 Tor 相比，提供了明显的舒适性和速度，但代价是会产生轻微的外部依赖性。许多人选择同时使用这两种**方案**：日常使用 Tailscale，将 Tor 作为备用方案，或者在不邀请他人进入自己的 VPN 的情况下与他人共享访问权限。



### 4.4 安全



通过将 Tailscale 与 Umbrel 结合使用，可以避免将 Umbrel 暴露在互联网上。Umbrel 节点只能由尾网中其他经过验证的设备访问，大大降低了攻击面（没有端口向陌生人开放，没有通过互联网攻击网络服务的风险）。



除了您的服务已经进行的任何加密（例如，即使内部 HTTP 也在隧道中）外，通信也会加密（WireGuard）。如果你想对网络进行分区，你仍然可以应用 Tailscale ACL 来阻止特定的尾网设备访问 Umbrel。Umbrel 本身看不出有什么不同，它认为自己提供的是本地服务。



---

在本节的最后，在 Umbrel 上集成 Tailscale 只需点击几下，并**大程度地提高自托管节点的可访问性。你可以从任何地方安全、高效地管理 Umbrel 及其服务，就像在家里一样。对于受 Tor 延迟影响的实时应用程序（闪电），或者更广泛地说，对于任何寻求简单专用连接的自托管节点，这都是一个特别有用的解决方案。所有这一切，都不会暴露你盒子上的一个端口**，也不需要复杂的网络配置。



## 5.高级管理和用例



### 5.1 Tailscale 高级功能



**网络管理：** 通过管理控制台 (login.tailscale.com)，您可以管理设备、查看连接并配置访问规则。



**MagicDNS:** 自动解析设备名称（如 `raspberrypi.tailnet.ts.net`），避免记忆 IP 地址。



**ACL 和访问控制：** 通过 JSON 规则精确定义谁能访问网络中的哪些内容，是隔离某些设备或限制访问特定服务的理想选择。



**设备共享可让你邀请他人访问特定的机器，而无需让他们访问你的整个网络。**



**子网路由器：** Tailscale 机器可充当整个子网的网关，通过一台配置好的机器访问非 Tailscale 设备（物联网、打印机等）。



**退出节点：** 将一台机器用作互联网网关，使用其 IP 退出。适用于公共 Wi-Fi 或绕过地理限制。



**Taildrop：** AirDrop 的安全替代品，允许你在 Tailscale 设备之间传输文件，无论它们的平台或位置如何。与仅限于苹果生态系统和物理距离的 AirDrop 不同，Taildrop 可在所有设备（Windows、Mac、Linux、Android、iOS）之间传输文件，即使这些设备位于不同国家。文件在设备间直接传输，采用端到端加密，无需通过中央服务器。可根据系统使用命令行 "tailscale file cp "或图形化 Interface 应用程序。



### 5.2 与其他解决方案的比较



**与 OpenVPN 的比较：** Tailscale 的配置要简单得多（无需打开端口，无需管理证书），但需要依赖第三方服务。OpenVPN 完全可控，但需要更多专业知识。



**作为直接竞争对手，ZeroTier 在 Layer 2（以太网）上运行，支持广播/多播，而 Tailscale 在 Layer 3（IP）上运行。ZeroTier 提供更大的网络灵活性，而 Tailscale 则更倾向于简单易用。**



**与 Tor 的比较：** Tor 具有 Tailscale 所没有的匿名性，但速度要慢得多。Tor 是去中心化的，不需要账户，而 Tailscale 速度更快，提供类似局域网的体验。



**Vs WireGuard manual:** Tailscale 可自动执行 WireGuard 原始版本需要手动处理的所有密钥和连接管理。它本质上是 WireGuard + 简化管理 Layer。



总之，Tailscale 将自己定位为一个以简化为导向的现代解决方案，非常适合个人和小型团队使用。对于需要完全控制的纯粹主义者，Headscale 提供了一种自我托管的替代方案。



## 6.结论



**Tailscale 的优势：** Tailscale 为自助托管提供了多项优势：





- **简单、高性能** - 可在所有平台上快速安装，无需复杂的网络配置。流量沿着机器之间最直接的路径（P2P 网状）传输，具有 WireGuard 协议的性能，没有中央服务器限制吞吐量。
- **安全性和灵活性** - 端到端加密、减少攻击面和高级功能（ACL、SSO/MFA 身份验证）。即使在 NAT 后面或移动中也能使用，通过子网路由器和出口节点使网络适应您的需求。



**限制：** 也请记住：





- **外部依赖性** - 在标准版本中，服务依赖于 Tailscale Inc.可通过 Headscale（自托管替代方案）绕过这一依赖。
- **其他限制因素** - 部分源代码封闭，免费版本在某些高级用途上受到限制，不支持 Layer 2（广播/多播），需要接入互联网才能建立连接。



**Tailscale 是个人自助主机和小型团队、需要访问分散资源的开发人员、VPN 初学者和移动用户的理想选择。对于需要全面控制的公司，Headscale 或 WireGuard 等其他解决方案可能更适合。**



**探索Headscale的完全自托管、API和DevOps集成（Terraform），或Innernet（类似但完全自托管）和Netmaker等替代方案。**



Tailscale 是自助托管的必备工具，它简单高效，让您的私有基础架构像在云中一样容易访问，同时还能在家中进行控制。



## 7.有用资源



### 正式文件





- Tailscale 文档中心：[docs.tailscale.com](https://docs.tailscale.com) - 完整的英文文档、安装指南、教程和技术参考资料。
- **Tailscale 如何工作**：[How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - 介绍 Tailscale 内部运作的详细文章。
- **Changelog**：[tailscale.com/changelog](https://tailscale.com/changelog) - 跟踪更新和新功能。



### 实用指南





- 家庭实验室教程：[tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - 自我托管的具体指导。
- **配置退出节点**：[tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - 配置退出节点的详细指南。
- 使用 **Taildrop**：[tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - 在 Tailscale 设备之间传输文件。



### 比较





- **Tailscale 与其他解决方案的比较**：[tailscale.com/compare](https://tailscale.com/compare) - 与其他 VPN 和网络解决方案（ZeroTier、OpenVPN 等）的详细比较。



### 社区





- **Reddit**：[r/Tailscale](https://www.reddit.com/r/tailscale/) - 讨论、问题和反馈。
- **GitHub**：[github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - 客户源代码，用于跟踪开发和报告问题。
- **Discord**：[discord.gg/tailscale](https://discord.gg/tailscale) - 用户和开发人员社区。



Tailscale 定期提供新内容和新功能。请访问他们的 [官方博客](https://tailscale.com/blog/) 了解最新消息和案例研究。