---
name: Umbrel Nostr
description: 在 Umbrel 上配置和使用 Nostr 应用程序
---

![cover](assets/cover.webp)



## 先决条件安装 Umbrel



Umbrel 是一个开源平台，可让您在自己的个人服务器上轻松托管 Bitcoin 应用程序和其他服务。它是一个一体化解决方案，大大简化了 Bitcoin 节点和去中心化应用程序的自我托管。



请按照我们的安装指南确保已安装 Umbrel：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Nostr 简介



**Nostr**是一个开放的去中心化网络协议，专为社交网络而设计。它的名字代表_"通过中继传输的笔记和其他东西"_。它允许任何人发布以 JSON 事件形式管理的信息（笔记），并通过中继服务器而非中央平台传播。每个用户都拥有一对作为标识符的加密密钥（私钥/公钥）：公钥（npub）用于标识用户，私钥（nsec）用于签署信息。得益于这种分布式架构，**Nostr 具有抗审查**和极大的灵活性：您可以使用多个客户端，并随意连接多个中继器，而无需依赖单一服务器。



简而言之，Nostr 是一种去中心化通信协议，**客户端**（用户应用程序）通过**中继器**（服务器）发送和接收事件。由于其去中心化和数据主权的价值，自 2023 年以来，该协议在 Bitcoin 社区特别受欢迎。



**注：** 要使用Nostr，您需要私人密钥（由Nostr客户端或专用扩展生成）。 **切勿共享您的私人密钥**，否则任何人都可以冒充您。请将其保存在安全的地方，并使用安全的密钥管理工具（见下文提示）。



## Nostr 的脐带应用



Umbrel 提供了一个集成应用程序生态系统，可以在您的个人节点上充分利用 Nostr。我们将详细介绍与Nostr相关的主要应用程序的使用： **Nostr Relay**、**noStrudel**、**Snort**和**Nostr Wallet Connect**。每个应用程序都能满足特定需求：_Nostr Relay_是**私人中继服务器**，_noStrudel_和_Snort_是**Nostr客户端**（阅读/发布笔记的界面），而_Nostr Wallet Connect_则是将您的**Lightning投资组合**链接到Nostr的工具。



### Nostr 中继站 - 您在 Umbrel 上的私人中继站



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay**是Umbrel的官方应用程序，用于在您的节点上运行您**自己的Nostr中继**。其主要目的是拥有一个**私人**和可靠的中继站，以**实时备份你所有的Nostr**活动。换句话说，除了公共中继站之外，您还可以使用这个个人中继站，确保您的所有笔记、信息和反应都被复制到家中，免受审查或数据丢失的影响。



**安装：** 从 Umbrel 应用程序商店（_社交_类别）安装 _Nostr Relay_。启动后，应用程序将在后台运行（docker 服务）。



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



您将通过 Umbrel 看到其 Interface 网页：它提供基本信息，尤其是中继站的 URL（右上角），您需要复制该 URL 以供进一步使用。此外还有一个同步按钮（地球仪图标）。



**利用你的 Umbrel 中继器 ：



**将中继添加到您的 Nostr 客户端：** 在您的客户端应用程序（如 iOS 上的 Damus、Android 上的 Amethyst、Umbrel 上的 Snort 或 noStrudel 等）中，添加您先前复制的私有中继的 URL。默认情况下，Umbrel 中继监听端口为 **4848**。如果在本地网络上访问，URL 会如下所示：ws://umbrel.local:4848`（或使用 Umbrel 的本地 IP）。



如果您使用 Tailscale（见下文），您甚至可以使用 MagicDNS DNS 别名（通常为 `umbrel` 或自动生成的名称）从任何地方访问它，端口始终为 4848。



如果您喜欢 Tor，请获取 Umbrel 的 .onion Address，并通过与 Tor 兼容的浏览器或客户端使用 4848 端口（参见 Tor 章节）。



将 URL 添加到 Nostr 客户端的中继配置后，连接到该中继。您应该能在客户端看到 Umbrel 中继已连接（通常用 Green 点或类似符号表示）。



**同步历史记录（可选）**：在 Umbrel 上_Nostr Relay_的 Interface 网页中，点击**球** 🌐 图标（位于页面顶部）。此操作将迫使您的 Umbrel 中继连接到您的其他中继（在您的客户端中配置的中继），以**导入您的旧公开**活动。这意味着你过去通过公共中继发布或阅读的笔记也将下载并存储在你的私人中继上。请等待同步完成。



**照常使用Nostr：** 从现在起，您在Nostr上进行的任何新活动（发表的笔记、反应、加密的私人信息等）都将照常转发到公共中继**，并同时转发到您的Umbrel中继**。如果您的 Nostr 客户端配置正确，它将把每个事件发送到所有中继站（包括您的中继站）。您的私人中继将作为实时备份。即使出现暂时断开连接的情况，您的客户也能通过该中继站重新同步丢失的数据。



在后台，Umbrel 的 _Nostr Relay_ 基于开源的 **nostr-rs-relay**项目（Rust 协议实现）。它支持整个 Nostr 协议和许多标准 NIP（NIP-01、02、03、09、11、12、15、16、20、22、26、28、33 等），保证了与客户的最大兼容性。



### noStrudel - 探险家的 Nostr 客户端



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel**是一个面向强大用户的Nostr网络客户端，是详细了解和探索Nostr网络的理想工具。它是一种沙盒，用于检查事件和中继，以及实验协议的高级功能。Interface 是英文版，技术性相对较强，非常适合对 Nostr 内部运作充满好奇的资深用户使用。



**安装：** 从 Umbrel 应用程序商店安装 _noStrudel_（类别 _Social_）。启动后，可通过浏览器访问 Umbrel 的 Address（如 `http://umbrel.local` 或通过其 .onion/Tailscale 访问，见外部访问部分）。



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**配置继电器：** 打开 noStrudel 时，您会在右上角看到一个 "设置继电器 "按钮。点击该按钮即可配置继电器。



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



在此页面上，粘贴之前复制的 Umbrel 中继的 URL。您还可以添加应用程序默认的其他中继。配置好中继后，点击左下角的 "登录 "继续。



![Options de connexion dans noStrudel](assets/fr/06.webp)



**连接：** noStrudel 为您提供多种连接选项。在本例中，我们将选择 "私钥"，并粘贴之前生成的 Nostr 私钥。如果您还没有密钥，可以安装[Nostr Connect]扩展（https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj）来创建和/或保存您的Nostr密钥，从而更安全地与各种Nostr应用程序通信。



![Interface principale de noStrudel](assets/fr/07.webp)



连接后，您可以使用 noStrudel 通过 Nostr 分享您的笔记。通过 Interface，您可以访问 .NET 和 .NET 应用程序：





- 完整的 Nostr 面板，包括备注时间线、通知、消息、个人资料搜索
- 中继管理和连接状态
- 用于检查事件及其 JSON 内容的高级工具
- 时间线过滤器和 PIN 的配置选项



**提示：** 在_noStrudel_上，您可以设置_时间线过滤器_或测试不同的_NIP（Nostr Implementation Possibilities）_。例如，检查对 NIP-05（分散标识符）或更多最新功能的支持。这使得_noStrudel_成为在受控环境中进行实验的绝佳工具。



### Snort - Umbrel 上的现代 Nostr 客户



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort**是Umbrel上的另一款Nostr网络客户端，它提供了一个现代、快速、简洁的**Interface**，用于与去中心化社交网络进行交互。与针对高级用户的 noStrudel 不同，_Snort_ 的目标是在不牺牲功能的前提下简化使用。它采用 React 构建，用户体验整洁，让人联想到经典的社交网络，适合日常使用。



**安装：** 从 Umbrel 应用程序商店安装 _Snort_（类别 _Social_）。



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



打开 Snort 后，会在左下角看到一个 "注册 "按钮。



![Options de connexion dans Snort](assets/fr/10.webp)



您可以选择注册或连接到现有账户（本教程将使用现有账户）。



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort 提供多种连接方法。您可以使用先前安装的 Nostr Connect 扩展或其他可用方法。连接后，您就可以充分使用应用程序了。



来自 _Snort_ 的 Interface 提供 ：





- 帖子/对话/全局**显示，可在笔记、主题讨论或全局信息源之间导航
- 用于**通知**、**信息** (DM)、**搜索**、**配置文件**等的选项卡。
- **+** 或 _Write_ 按钮可发布新笔记
- 管理**订阅（以下）**和**列表**
- 继电器管理菜单可添加/删除继电器并跟踪其可用性



**建议的中继配置：** 要添加 Umbrel 中继，请转到设置 - 中继。在 Snort 的中继列表中输入您的中继 URL（`ws://umbrel:4848` 或其他 URL，具体取决于您的配置）。这样，除了公共中继外，Snort 还会在私人中继上发布您的笔记。



### Nostr Wallet Connect - 将您的 Lightning Wallet 连接到 Nostr



**Nostr Wallet Connect (NWC)**是一个应用程序，可将您的Umbrel（闪电）**节点连接到兼容的Nostr应用程序，以进行闪电支付（例如，发送_zaps_，即 "喜欢 "内容的小额支付）。在本教程中，我们将介绍如何将 noStrudel 连接到您的 Lightning 节点，以便直接从 Interface 进行支付。



**安装和配置：**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



从 Umbrel 上的 Alby 商店安装 _Nostr Wallet Connect_。



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



在 noStrudel 中，点击右上角的个人资料，然后点击 "管理 "按钮。



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



点击 "闪电"，然后点击 "连接 Wallet"。



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



在可用的连接选项中，选择 "Umbrel"。



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



点击 "连接"，系统将自动跳转到 Umbrel Nostr Wallet 连接会话。



![Page de configuration des autorisations NWC](assets/fr/17.webp)



在 Nostr Wallet Connect 页面，您可以 ：




   - 确定最高预算
   - 验证授权
   - 设置连接的过期时间


点击 "连接 "完成。



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



您将重定向到 noStrudel，并收到一条确认信息：您现在可以从 Wallet/LND 节点斩杀整个世界！



有了NWC，您通过Nostr**进行的**Lightning支付（Zaps到奖励帖子、_Value for Value_支付等）将从**您自己的节点**开始。您不必再通过外部服务进行交易，也不必每次都用手机扫描二维码。用户体验得到极大提升，同时还保持了非托管性和隐私友好性。



如果你想知道如何在 Umbrel 上建立自己的 "闪电 "节点，我建议你看看另一篇全面的教程：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 高级配置和安全



在高级水平上同时使用 Umbrel 和 Nostr 需要特别注意**安全性**和**连接性**。以下是一些关于如何保护您的配置并随时随地以最佳方式访问配置的提示。



### 安全的外部访问Tor 和 Tailscale



出于安全考虑，您的 Umbrel 默认只能在本地网络上访问（通过 Tor）。要在离家之外与 Nostr 互动，您有两种首选解决方案： **Tor**（通过洋葱网络匿名访问）和**Tailscale**（私人 VPN 网状网络）。





- 通过 Tor 访问：** Umbrel 自动为其 Interface 网络和应用程序配置**Tor 服务（.onion）**。这意味着您可以在任何地方使用 Tor 浏览器访问 Interface Umbrel（包括 _noStrudel_ 或 _Snort_），而不会暴露您的公共 IP。Tor 用于从本地网络之外访问您的 Umbrel 服务，而不会将您的设备暴露在互联网上（[在您的系统上设置 Tor - 指南 - Umbrel 社区](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)）。_要使用此选项，请进入 Umbrel 设置并检索您的 Umbrel .onion URL（或扫描提供的二维码）。在 Tor 浏览器上访问该 .onion Address：您将获得与本地相同的 Interface。然后，您就可以像在家里一样使用 Nostr 应用程序了。


**通过 Tor 的 Nostr 中继：** 如果你希望你的客户（或授权朋友）可以通过 Tor 访问你的 Nostr 中继，这是有可能实现的。Umbrel 并不直接提供中继的 .onion Address，但由于它在 4848 端口运行，你可以使用 .onion Address：





    - 使用 UI Umbrel 的 .onion Address，并配置客户端通过该 Interface 进行连接（WebSocket 不切实际）、





    - 或者***将 4848 端口作为单独的洋葱服务公开。这需要在 Umbrel 上对 Tor 进行配置（适合熟悉 SSH 的高级用户）。或者，也可以考虑在其他服务器上建立一个**Tor 隧道**，重定向到 Umbrel：不过，对于个人使用来说，使用 Tailscale 是最简单的。





- 通过 Tailscale 接入：** [Tailscale](https://tailscale.com/) 是一种网状 VPN 解决方案，可在您的设备和 Umbrel 之间创建虚拟专用网络。其优势在于：它的工作原理与局域网相同，但通过互联网进行加密，无需复杂配置。 **无论 Umbrel 位于哪个网络位置（[Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)）**，Tailscale 都会为其分配一个固定 IP 和专用域名。实际上，一旦您在 Umbrel 上安装了 Tailscale（来自 Umbrel App Store，类别 _Networking_），***和***您的设备（手机、电脑......），您就可以通过 Address 如 `100.x.y.z` （Tailscale IP）或名称如`umbrel.tailnet123.ts.net`到达 Umbrel。


对于 Nostr_，Tailscale 非常有用：如果您的手机激活了 Tailscale，就能连接到 `ws://umbrel:4848`（多亏了 MagicDNS）或直接连接到 Tailscale IP 和 4848 端口以使用中继。像 Damus 或 Amethyst 这样的客户端会看到你的 Umbrel，就像它在同一个本地网络上一样。 **提示：** 在 Tailscale 中启用**MagicDNS**选项，使用主机名 "umbrel"，而不是记忆 IP。这样，即使您在移动中（[Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)），也能顺利连接到中继器。


此外，Tailscale 还允许你通过一个简单的浏览器，使用私有 IP 或分配的域名访问 Interface Umbrel（以及 _noStrudel/Snort_ 网络客户端）。无需使用 Tor 浏览器，而且数据传输速度通常比通过 Tor 网络更快。




**注：Tor 和 Tailscale 并不相互排斥。你可以为匿名访问或特定服务而保持 Tor 处于活动状态，而日常使用 Tailscale 则是因为它简单易用。在这两种情况下，你都不需要在路由器上打开端口，这就加强了安全性。



### 确保 Nostr 中继的安全（推荐做法）



如果您在 Umbrel 上托管 Nostr 中继，尤其是在高级情况下，请务必采用一些良好做法：





- 私人或受限中继：** 默认情况下，您的 Umbrel 中继是私人的（不对外公布），如果您只通过 Tailscale 或局域网访问，陌生人将无法访问。 **链接保密 ** 不要在公共 Nostr 网络上广播，除非你想自愿接待其他用户，这是另一个问题（节制、带宽等）。对于个人使用，我们建议仅限于您自己访问，必要时仅限于几位可信赖的朋友和家人访问。





- 白名单/认证**：nostr-rs-relay 实现支持**NIP-42**认证机制以及公钥白名单。通过启用这些选项，你可以限制你的中继，使它**只接受由特定密钥（你的）**签署的事件，或者客户必须通过身份验证才能发布。设置这需要在 Umbrel 中编辑中继的 `config.toml` 配置文件（通过 Docker 容器中的 SSH）。这样，即使有人发现了你的中继站，如果他们不在列表中，也无法在那里发布任何内容。





- 更新和维护：** 随时更新您的 Umbrel 和 _Nostr Relay_ 应用程序。更新可能包括性能改进（如更好地处理垃圾邮件）和安全修复。在 Umbrel 上，请定期在 App Store 上查看 _Nostr Relay_ 的更新，并在必要时应用这些更新。





- 监控和限制：** 留意中继器的使用情况。nostr-rs-relay提供可配置的**速率和存储限制**（配置中的 "限制"，如每秒事件数、最大事件大小、旧事件清除......）。对于私人使用，你可能不需要接触这些参数，但如果需要，请注意这些参数的存在（[nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)）。





- 确保 Nostr 密钥的安全：** 这一点已经提到过，但至关重要：切勿在您不完全信任的 Interface 中输入您的 Nostr 私钥。相反，应使用浏览器扩展或外部设备（如单独手机上的 Nostr 签名器）来签署敏感操作。在 Umbrel 上，您的网络客户端（如 _Snort_ 和 _noStrudel_）可以通过 NIP-07 在不知道您的秘钥的情况下工作。利用这个机会，将舒适性和安全性结合起来。




按照这些提示，您的 Umbrel 节点与 Nostr 的整合将既强大**又安全。您将拥有一个完整的环境：一个用于闪电支付的 Bitcoin 节点、一个用于数据主权的私有 Nostr 中继器，以及用于浏览这个新的去中心化社交网络的高性能 Nostr 网络客户端。享受与 Umbrel 一起探索 Nostr 的乐趣！