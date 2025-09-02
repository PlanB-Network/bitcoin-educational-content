---
name: LibreWolf
description: 如何使用 LibreWolf 隐私浏览器
---

![cover](assets/cover.webp)



每一次点击、每一次搜索、每一个访问过的网站：你的网络浏览器已经成为一个复杂的告密者，为全球商业监控系统提供信息。有 30 多亿人使用的谷歌 Chrome 浏览器将你的日常浏览变成了广告巨头们有利可图的数据。即使是火狐浏览器，尽管它有 "道德 "浏览器的美誉，也会在默认情况下激活遥测机制，将你的浏览习惯传输给 Mozilla。



这一现实提出了一个至关重要的问题：是否仍有可能在互联网上自由浏览，而不被不断监视和剖析？幸运的是，答案是肯定的，这要归功于将用户重新置于关注中心的社区项目。



LibreWolf 体现了这一数字抵抗哲学。作为独立开发者社区的心血结晶，这款浏览器将 Firefox 变成了抵御网络监控的名副其实的盾牌。在商业浏览器寻求将你的注意力货币化的时候，LibreWolf 却反其道而行之：在保持流畅、现代的浏览体验的同时，让追踪者看不到你。



在本教程中，我们将了解 LibreWolf 如何改变你的上网方式，在不牺牲性能或网络兼容性的情况下提供强大的跟踪保护。



![LIBREWOLF](assets/fr/01.webp)


*网络浏览器市场份额：Chrome 浏览器占据了 65% 的市场份额，其次是 Safari 和 Edge。这种主导地位引发了有关网络多样性和隐私的问题*。



## 介绍 LibreWolf



**FreeWolf**是一款开源网络浏览器，源自Mozilla Firefox，由一个独立的自由软件爱好者社区开发和维护。其主要目标是提供注重用户隐私、安全和自由的浏览方式。



具体来说，LibreWolf 使用了 Firefox 的 Gecko 引擎，但其理念却截然不同：Firefox 需要在隐私和易用性之间取得平衡，而 LibreWolf 则选择默认保护隐私。该项目删除了任何可能侵犯个人隐私的内容（遥测、数据收集、赞助模块），同时集成了增强的安全设置。



### 目标：隐私和自由



LibreWolf 旨在最大限度地防止跟踪和指纹识别，同时增强浏览器的安全性。其主要目标包括





- 消除 Firefox 中的所有遥测和数据收集**
- 禁用违背用户自由的功能**，如专有 DRM 模块
- 从一开始就应用隐私/安全设置**和特定补丁程序
- 社区发展保证了透明度和独立性**，不受商业利益的影响



简而言之，LibreWolf 将自己定位为 "如果隐私被放在首位，火狐浏览器的本来面貌"--一个默认情况下尊重你的浏览器，无需额外配置。



### 主要特点



从一开始，LibreWolf 就提供了一系列以隐私为导向的功能：



**没有遥测或数据收集：** 不像 Chrome 或 Firefox 会发送某些使用统计，LibreWolf 完全不会从您的浏览中收集任何数据。没有崩溃报告，没有用户研究，没有赞助商建议。



**LibreWolf 原生集成了 uBlock Origin 扩展，它是市场上最好的广告拦截器和跟踪器之一。默认情况下，LibreWolf 会主动过滤掉任何可能对你进行在线追踪的东西（侵入性广告、追踪脚本、加密货币 Mining）。



**默认使用隐私搜索引擎：** LibreWolf 默认使用 DuckDuckGo 作为初始搜索引擎，它不会保留您的查询历史记录。也有其他面向隐私的替代方案（Searx、Qwant、Whoogle）可供选择。



**强化反指纹保护：** 即使没有 cookies，指纹技术也能通过浏览器的配置对其进行唯一识别。为了应对这种情况，LibreWolf 启动了 Tor 项目的 RFP（抗指纹）技术，使浏览器尽可能通用。测试表明，在 coveryourtracks.eff.org 等工具中，标准火狐浏览器的唯一识别率为 90%，而 LibreWolf 浏览器的唯一识别率仅为 10%-20%（这些数字仅供参考，可能因软硬件配置和安装的扩展而异）。



![LIBREWOLF](assets/fr/07.webp)


*使用 TEST YOUR BROWSER（测试你的浏览器）按钮打开 EFF 测试页面 [Cover Your Tracks](https://coveryourtracks.eff.org/)。该页面用于评估对跟踪器和指纹识别的保护。



![LIBREWOLF](assets/fr/08.webp)


*掩护你的踪迹 "测试结果。显示信息 "您拥有强大的网络跟踪保护"，表明 LibreWolf.* 保护的有效性



**LibreWolf默认激活严格的安全设置。火狐浏览器的 "增强跟踪保护 "被提升到了 "严格 "级别，可阻止数千个跟踪器、第三方 cookie 和恶意内容。它还激活了网站和 cookie 隔离（*Total Cookie Protection*），为每个域分割数据，并限制 WebRTC（限制 *ICE 候选*，并在存在代理时通过代理路由），以降低 IP Address 泄露的风险。



**快速的引擎更新：** 项目密切关注 Firefox 的发展：LibreWolf 始终基于火狐浏览器的最新稳定版本，维护者努力在火狐浏览器每次正式发布后的 24 至 72 小时内发布新版本。



## 优缺点



### 益处





- 没有遥测或不必要的连接：** LibreWolf 不传输任何使用数据，确保完全尊重您的隐私。





- 开源和基于社区：** 该项目 100%开源，由志愿者维护。这种独立性保证了任何广告模式都不会影响开发工作。





- 预配置隐私：** LibreWolf 为您节省宝贵的时间：无需花费数小时强化 Firefox 设置，一切都已完成。





- 本地广告拦截器/跟踪器：** uBlock Origin 集成为标准配置，因此你无需做任何事情就能防止广告和错误。





- 卓越的防指纹保护：** 由于 RFP 和大量隐私设置，LibreWolf 大幅减少了您在网络上的独特数字足迹。





- 提高性能、减轻重量：** 通过移除遥测和某些非必要功能，LibreWolf 可以比标准 Firefox 更快、更省电。



### 缺点和局限性





- 无内置自动更新：** LibreWolf 不会自我更新。您需要在新版本发布后立即安装，以确保安全。





- 与某些服务的兼容性降低：** 由于其非常严格的设置，LibreWolf 在某些网站上可能会遇到问题。由于 LibreWolf 默认禁用了 Widevine DRM，Netflix 和 Disney+ 流媒体平台将无法使用。





- 没有内置的匿名网络：** 与 Tor 浏览器不同，LibreWolf 本身不会通过 Tor 或 VPN 路由流量。如果你需要网络匿名，你需要手动配置一个代理/VPN。





- 非持久性 cookie 和会话（默认）：** 出于保密原因，每次关闭浏览器时，LibreWolf 都会删除 cookie、历史记录和网站数据。每次登录时，您都需要重新登录您的账户。





- 没有移动版本或云端同步：** LibreWolf 只能在桌面上使用（Windows、Linux、macOS）。没有移动应用程序，因此无法通过云同步账户或书签。



## 安装 LibreWolf



**官方网站：** [librewolf.net](https://librewolf.net)



LibreWolf 适用于所有主流桌面操作系统：Linux、Windows 和 macOS。要下载 LibreWolf，请访问官方网站：



![LIBREWOLF](assets/fr/02.webp)


*LibreWolf 主页 (librewolf.net) 显示浏览器徽标、蓝色安装按钮以及源代码和文档链接。一个大的蓝色箭头指向安装按钮*。



点击 "安装 "按钮，获取操作系统的详细说明：



![LIBREWOLF](assets/fr/03.webp)


*LibreWolf.* 下载的操作系统选择页面



安装方式因操作系统而异：



### 在 Linux 上


LibreWolf 为许多发行版提供编译。在 Debian/Ubuntu 及其衍生版本上，可以使用官方 APT 代码库。另外，LibreWolf 在 Flathub 上以 Flatpak 发布：


```
flatpak install flathub io.gitlab.librewolf-community
```



### 在 Windows 上


从官方网站下载安装程序 (.exe)，或使用 .NET Framework 3.0：




- Chocolatey:** `choco install librewolf`.
- WinGet:** `winget install librewolf`.



### 在 macOS 上


LibreWolf 以 .dmg 包的形式提供给 Mac。从官方网站下载磁盘镜像，然后将 LibreWolf 应用程序拖放到 "应用程序 "文件夹中。或者，你也可以通过 Homebrew 安装。




## 配置和首次使用



首次启动时，你会看到熟悉的 Firefox Interface，但它更加简洁：主页上只有搜索栏，没有赞助商建议。你会在工具栏中看到 uBlock Origin 图标，这表明拦截器处于激活状态。



![LIBREWOLF](assets/fr/04.webp)


*带有扩展和菜单的 LibreWolf 主页。右上角的蓝色箭头表示菜单图标（三个横条）



LibreWolf 会自动以 "严格"（反跟踪）模式加载网页，默认搜索引擎为 DuckDuckGo。你可以尝试访问一个跟踪测试网站（例如 amiunique.org），观察暴露的足迹--它应该比使用标准浏览器时要普通得多。



### 隐私设置



LibreWolf 已经为隐私做了最佳配置。在菜单 → 选项 → 隐私与安全中，你会看到 LibreWolf 已设置为增强跟踪保护模式：严格。




- 站点间跟踪器
- 第三方 cookie
- 已知跟踪内容
- 加密采矿
- 数字指纹探测器



![LIBREWOLF](assets/fr/05.webp)


*安全和隐私选项卡页面显示 LibreWolf.* 的安全设置



禁用了 WebRTC（防止 IP 泄露），并启用了全面 Cookie 保护。遥测和 Firefox 调查已完全禁用。



### Cookie 和历史记录管理



默认情况下，LibreWolf 会在每次关闭时删除 cookies 和本地存储。如果这种行为对你造成困扰，你可以在隐私与安全 → Cookies 和网站数据中调整，取消选中 "关闭 LibreWolf 时删除 cookies 和网站数据"。



![LIBREWOLF](assets/fr/06.webp)


*同一页面再往下一点，显示关闭浏览器时删除 cookie 的选项*。



### 添加有用的扩展功能



原则上，LibreWolf 不鼓励添加不必要的扩展，因为每个扩展都可能是一个追踪载体。尽管如此，一些信誉良好的扩展程序还是可以提升您的使用体验：




- 火狐浏览器多账户容器**（由 Mozilla 提供），用于分区浏览
- Decentraleyes** 或 **LocalCDN**，为本地常用图书馆提供服务



尤其要避免使用 "免费 VPN "扩展或可疑的代理服务器，uBlock Origin 已能满足你 99% 的需求。



## 日常使用



### 日常网页浏览


使用 LibreWolf 进行日常上网活动。与其他浏览器的主要区别在于，你留下的广告痕迹要少得多。得益于 uBlock 的过滤列表，许多网站上的 "接受 cookie "横幅都会消失。



### 使用私人选项卡进行分隔


尽管 LibreWolf 会在会话结束时删除所有内容，但在会话期间为某些任务打开一个私人浏览器窗口（Ctrl+Shift+P）可能会很有用，以便隔离特定身份。



### 利用多账户容器


安装多账户容器扩展可以极大地帮助你将你的活动分割成密不透风的筒仓。例如，您可以为银行网站定义一个 "银行 "容器，为 Facebook/Twitter 等定义一个 "社交网络 "容器。每个容器都有自己的 cookie、会话和隔离存储。每个容器都有自己的 cookie、会话和隔离存储。



### 按站点微调权限管理


LibreWolf 可让您根据具体情况控制授予网站的权限（位置、摄像头、麦克风、通知）。只向您信任的网站授予必要的权限。



## 使用 LibreWolf 的最佳实践



1. **保持 LibreWolf 的最新版本：** 定期检查网站以获取新版本，尤其是在稳定的 Firefox 版本发布之后。



2. **避免将个人身份和私人浏览混为一谈：** 理想的做法是，在进行敏感研究的同一会话中，不要用个人账户登录。



3. **不要给 LibreWolf 安装过多的扩展：** 您安装的每个扩展都可能带来安全或指纹风险。



4. **另外使用 VPN 或 Tor 代理：** LibreWolf 不会让您对 ISP 匿名。为了实现网络匿名，您可以在可信的 VPN 后面使用 LibreWolf。



5. **保存重要数据：** 书签、密码（如果存储在本地）。考虑使用外部密码管理器（KeePassXC、Bitwarden），而不是浏览器的基本密码管理器。



## 与其他浏览器的比较



LibreWolf 是面向隐私的浏览器 "工具箱 "的一部分：



**LibreWolf 与 Firefox 的比较：** LibreWolf 已经加固，没有任何遥测技术。Firefox 保留了多设备同步和庞大用户群的优势，但需要手动配置才能达到 LibreWolf 的保密级别。



**Brave使用Chrome/Chromium代码，并通过可选的广告计划整合了商业模式。LibreWolf 作为火狐浏览器的社区 Fork，保留了 Mozilla 的免费生态系统，与谷歌没有任何关系。



**LibreWolf 与 Tor 浏览器的对比：** Tor 浏览器在面对强大监控的匿名性方面具有不可替代的作用，但在日常使用中速度较慢，令人不舒服。LibreWolf则更快更实用，适合日常浏览经典网页。



**LibreWolf 与 Mullvad 浏览器的比较：** Mullvad 浏览器在标准化方面走得更远，但代价是可用性降低（无法保留登录 cookie）。LibreWolf 取得了平衡：非常私密，但日常可用。



## 结论



LibreWolf 为那些寻求超隐秘的 "日常 "浏览器而又不想使用 Tor 的极端匿名性的用户提供了一个极佳的解决方案。它是活动家、记者、开发人员或想要经典网页浏览（速度快、与现代网站兼容），同时又想躲避广告跟踪和大技术公司的高级用户的理想选择。



尽管它有一定的局限性（不能自动更新、与某些服务的兼容性较差），但对于任何希望重新控制数字隐私的人来说，LibreWolf 都是一个非常有价值的工具。它的易用性和默认配置使其成为注重隐私的用户的明智之选。



## 资源



### 正式文件




- [LibreWolf官方网站](https://librewolf.net)
- [源代码在 Codeberg 上](https://codeberg.org/librewolf)
- [官方常见问题](https://librewolf.net/docs/faq)



### 指南和比较




- [隐私指南](https://www.privacyguides.org/en/desktop-browsers/)
- [隐私比较测试](https://privacytests.org)



### 社区支持




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)。