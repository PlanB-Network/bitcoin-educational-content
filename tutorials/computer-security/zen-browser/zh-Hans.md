---
name: 禅宗浏览器
description: 如何使用 Zen 浏览器进行高效、保密的浏览？
---

![cover](assets/cover.webp)



在当今的网络浏览器领域，谷歌 Chrome 浏览器占据了 65% 以上的市场份额，但这一霸权引发了有关隐私和技术多样性的重要问题。与大多数流行浏览器一样，Chrome 浏览器大量收集浏览数据，为谷歌的广告算法提供素材。



![Parts de marché des navigateurs](assets/fr/01.webp)



面对这一现实，新的浏览器不断涌现，它们秉承着不同的理念：兼顾现代用户体验和尊重隐私。2024 年推出的 Zen 浏览器就是这种理念的一部分，它以火狐浏览器为基础，为当今用户重新设计，提供了一种创新的替代方案。



Zen 浏览器因其独特的 Interface（垂直标签页）、可组织会话的工作区以及分屏视图等高效功能而脱颖而出。但除了这些符合人体工程学的创新之外，最重要的是它的 Commitment 隐私保护功能：无遥测、强化的反跟踪保护和透明的社区开发。



在本教程中，我们将了解 Zen 浏览器如何通过结合生产力、个性化和隐私来改变您的浏览方式。



## 安装 Zen 浏览器



### 官方下载



Zen 浏览器适用于 Windows、macOS 和 Linux。访问官方网站：zen-browser.app/download



![Site officiel Zen Browser](assets/fr/02.webp)



网站会自动检测您的系统，并提出相应的链接：



![Page de téléchargement](assets/fr/03.webp)





- Windows:** .exe 安装程序，适用于 Windows 10/11（x64 和 ARM64 版本）
- macOS:** Intel 和 Apple Silicon 兼容 .dmg 磁盘映像（macOS 蒙特利及更高版本）
- Linux：** 有多种选择：
  - Flatpak** （推荐）：`flatpak install flathub app.zen_browser.Zen`.
  - AppImage**：可移植、直接执行
  - 档案 tar.gz** ：需手动解压缩
  - AUR** (Arch Linux) ：Zen 浏览器软件包



### 逐步安装



**在 Windows 上：**




- 下载 .exe 文件
- 运行安装程序（如果 SmartScreen 发出警报，请单击 "其他信息"，然后单击 "无论如何都要运行"）。
- 选择安装目录
- 勾选 "启动 Zen 浏览器 "可立即启动



**在 MacOS 上：**




- 下载 .dmg 文件
- 挂载磁盘镜像
- 将 Zen 浏览器拖入 "应用程序 "文件夹
- 首次启动时：右键单击 >"打开"，切换到网守



**在 Linux 上：**




- Flatpak：** 通过软件包管理器自动安装
- AppImage:** `chmod +x ZenBrowser.AppImage` 然后双击
- tar.gz:** 解压缩并运行 zen-browser 可执行文件



### 首次发射和初始配置



首次启动时，Zen 浏览器会引导您完成几个配置步骤：



![Import de données](assets/fr/04.webp)


*可选择从其他浏览器导入数据（收藏夹、历史记录、密码）*。



![Configuration initiale](assets/fr/05.webp)


*选择默认搜索引擎和配置引脚标签*。



![Personnalisation visuelle](assets/fr/06.webp)


*选择工作区的颜色并验证以访问浏览器*。



![Page d'accueil Zen Browser](assets/fr/07.webp)


*带有特色边栏的 Zen 浏览器主页*



## Zen 浏览器介绍



**Zen 浏览器**是一款免费的开源网页浏览器，源自 Mozilla Firefox，自 2024 年 3 月起由一个充满热情的志愿者社区开发。与大型技术公司的浏览器不同，Zen 浏览器没有任何商业公司的支持，资金完全来自社区的贡献。



**重要说明：** Zen 浏览器目前处于**试用版**。虽然该版本在日常使用中表现稳定，但仍需经常更新并偶尔出现错误。



该项目的口号是："欢迎使用更平静的互联网"。这一理念体现在浏览器中，它关注的是用户体验而非个人数据，在美观、速度和隐私之间寻求完美平衡。



### 为提高生产力而重新设计的 Interface



Zen 浏览器通过多项创新彻底改变了浏览体验：



**垂直标签页：** 与传统浏览器不同，Zen 采用垂直侧边栏显示标签页，而不是水平显示。受 Arc 浏览器的启发，这一符合人体工程学的选择最大限度地扩大了显示空间，改善了导航效果，尤其是在打开多个标签页的情况下。



**工作空间：** 在专用空间中按项目或主题组织标签页。例如，"工作 "空间用于放置专业标签页，"观察 "空间用于放置阅读标签页，等等。你可以从一个空间即时切换到另一个空间。



**分割视图：** 在单个窗口中并排显示多个网站，是比较信息或同时处理多个信息源的理想选择。



**Glance：** 在临时模式窗口中快速预览链接，而无需打开新标签页，非常适合查阅参考资料而不会丢失上下文。



### 默认情况下的隐私保护



Zen 浏览器原生集成了强大的隐私保护功能：





- 增强型反跟踪功能：** 自动阻止跟踪器、第三方 cookie 和指纹脚本
- 禁用遥测：** 不向外部服务器发送数据
- 通过 HTTPS 发送 DNS：** 加密 DNS 请求以防止监控
- 减少对谷歌的依赖：** Zen 浏览器移除了与谷歌服务的大部分连接，但仍有部分连接（安全浏览、更新）。



### 使用 Zen Mods 进行高级定制



Zen 通过**Zen Mods**提供了一个独特的定制生态系统：一个由社区创建的主题和修改库，用于改变浏览器的外观和行为。



**推荐的流行 Zen Mods：**





- SuperPins** ⭐：将图钉标签变成风格化按钮，让 Interface 看起来更专业
- 凝聚力**：统一的透明样式，统一 URL 栏、侧边栏和书签
- 更好的查找栏**：将搜索栏移到顶部，更符合人体工程学原理
- 悬停时展开侧边栏**：悬停时自动扩展侧边栏，最大化屏幕空间
- 更好的卸载标签**：通过不活动标签页的可视化指示器优化内存管理
- 净化 URL 棒**：Interface 净化 Address 栏，去除多余的 Elements
- 透明禅**：具有流畅动画的优雅透明效果



**Zen Mod 安装：**




- 前往 [Zen Mods 官方图库](https://zen-browser.app/mods)
- 浏览可用主题库



![Galerie Zen Mods](assets/fr/12.webp)





- 点击所需修改的 "安装



![Installation SuperPins](assets/fr/13.webp)


*举例说明：安装流行的超级插销* 修改器





- 主题立即适用
- 您可以随时停用或尝试其他功能



Zen Mods 不局限于视觉主题：有些修改了 Interface 的行为（动画、元素布局、自定义快捷方式）。这种模块化方法允许每位用户创建自己理想的浏览环境。



![Gestion des Zen Mods](assets/fr/16.webp)


*Interface 用于管理安装在参数中的 Zen 模式*。



**⚠️ 关于个性化和指纹识别的重要说明：**


你对 Zen 浏览器定制得越多（主题、扩展、MOD），你的**数字足迹**就越独特，因此也就越可追溯。这是一种根本性的妥协：




- 最大程度的个性化** = 最佳的用户体验 BUT 独特、易于识别的印记
- 默认配置** = 更常见的足迹，但个性化体验较少



Zen 浏览器选择了用户体验而非完美的匿名性。如果您的优先级是绝对匿名，请选择 Tor 浏览器或 Mullvad 浏览器，它们会对所有用户进行统一配置。



此外，Zen 基于 Firefox，与整个 Firefox 扩展生态系统兼容。



## 优缺点



### ✅ 亮点





- 隐私设计：** 启用反跟踪保护，禁用遥测技术，不收集数据
- 创新的 Interface：** 垂直选项卡、工作区和拆分视图大大提高了工作效率
- 快速更新：** 在 72 小时内与 Firefox 同步更新安全补丁
- 高级定制：** 社区主题、微调、与 Firefox 扩展兼容
- 开放源代码和社区：** 透明代码、合作开发、独立于大科技公司



### 电流限制





- 无移动版本：** 仅在 PC（Windows、macOS 和 Linux）上提供
- DRM 不兼容：** Netflix、Disney+、Spotify 和其他流媒体服务目前无法使用
- 年轻项目：** 小团队，社区支持，偶尔出现错误
- 学习曲线：** Interface 与众不同，习惯使用横向选项卡的用户需要进行调整



## 隐私和安全高级配置



访问 Zen 浏览器设置 ：



![Accès aux paramètres](assets/fr/14.webp)


*点击拼图图标（扩展），然后点击底部的 "禅设置 "*。



![Interface des paramètres](assets/fr/15.webp)


*带有所有可用选项卡的禅参数总览*。



### 优化默认设置



Zen 浏览器从一开始就采用了高隐私配置，其性能优于大多数浏览器：





- 严格的反跟踪保护：** 默认激活 "标准 "级别，可阻止.NET、ASP.NET 和 SQL：
  - 跨站跟踪 cookie 和超级 cookie
  - 广告跟踪脚本（Google Analytics、Facebook Pixel 等）
  - 利用你的 CPU 来 Miner 加密货币的 Cryptominters
  - 通过画布、WebGL 和音频上下文进行指纹识别





- 完全隔离 cookie：** 第一方隔离可防止一个网站读取另一个网站的 cookie
- 大部分遥测功能已禁用：** 大部分数据收集功能已移除，但与 Mozilla/Google 服务的某些连接可能会保留，并需要额外的手动配置
- 默认情况下的安全 DNS：** 启用 DNS-over-HTTPS，以防止窥探您的请求
- 仅启用 HTTPS：** 在所有网站上强制加密连接



### 推荐的隐私设置



**1.选择防跟踪保护级别：**


设置 > 隐私与安全 > 增强跟踪保护



![Protection anti-pistage](assets/fr/18.webp)



**标准（推荐默认值）：**




- 兼顾保护和性能，页面正常加载
- 阻止：社交追踪器、跨站 Cookie、私人窗口中的追踪内容、加密挖掘、指纹识别器
- 包括 ** 全面 Cookie 保护**：按站点隔离 Cookie，防止跨站点跟踪



**严格（最大保护）：**




- 增强保护，但可能会破坏某些网站或内容
- 阻止：社交跟踪器、跨站 cookie、****窗口中的跟踪内容、已知和可疑浏览器
- 建议有经验的用户使用



**定制（细粒度控制）：**




- 精确选择要屏蔽的跟踪器和脚本
- 单独选项Cookies、跟踪内容、加密、已知/可疑跟踪器
- 根据需求进行微调的理想选择



**2.更改搜索引擎：**


设置 > 搜索 > 默认搜索引擎 ：



![Configuration moteur de recherche](assets/fr/20.webp)





- DuckDuckGo**：无貌相，无过滤气泡，结果中立
- Startpage**：匿名谷歌结果，总部设在荷兰（RGPD）
- Searx**：去中心化元搜索引擎，无日志，开源
- 勇敢搜索**：独立索引，非来自谷歌
- 避免**：谷歌、必应、雅虎（大量数据收集）



**3.配置安全 DNS（通过 HTTPS 的 DNS）：**


设置 > 隐私和安全 > HTTPS DNS（页面底部）



![Configuration DNS sur HTTPS](assets/fr/19.webp)



**默认保护：**




- Zen 自动决定何时使用安全 DNS
- 在有安全 DNS 的地区使用安全 DNS
- 如果安全提供商出现问题，则回退到默认 DNS
- 通过 VPN、家长控制或企业政策自动停用



**增强保护（建议）：**




- 您可以控制何时使用安全 DNS 并选择提供商
- 使用选定的提供商，必要时退到 DNS 系统
- 默认提供商：** Cloudflare（快速、匿名日志）
- 替代方案：** 转至 Quad9、NextDNS（视可用情况而定



**最大保护（高级用户）：**




- 禅宗***始终只使用安全 DNS
- 使用 DNS 系统前的安全警告
- 警告：** 如果安全 DNS 不可用，网站可能无法加载



**4.仅启用 HTTPS 模式：**


设置 > 隐私和安全 > 仅 HTTPS 模式 > **已启用**




- 强制所有连接使用 HTTPS
- 如果网站仅支持 HTTP，则发出警报



**5.管理默认权限：**


设置">"隐私与安全">"权限"：




- 地点**：座（卡服务除外）
- 摄像头/麦克风**：块（根据具体情况授权）
- 通知**：阻止（防止垃圾邮件）
- 自动播放**：屏蔽音频和视频



### 建议的安全扩展



**基本扩展：**




- uBlock Origin**：最有效的广告拦截器和跟踪器
  - 推荐列表：EasyList、EasyPrivacy、Peter Lowe 的广告和跟踪服务器列表
  - 为有经验的用户提供高级模式





- 清除URLs**：删除 URL 跟踪参数（utm_source、fbclid 等）
- Cookie 自动删除**：关闭标签页时自动删除 cookie 和浏览数据
- Decentraleyes**：在本地提供 JS 库，以避免使用 Google/Cloudflare CDN



**高级扩展（经验丰富的用户）：**




- NoScript**：细粒度 JavaScript 控制（可能会破坏许多网站）
- Privacy Badger** (EFF)：跟踪器行为检测
- 临时容器**：将每个标签隔离在单独的容器中



## 了解 Zen 浏览器中没有 DRM 的情况



### 什么是 DRM？



DRM（数字版权管理）** 是对数字内容进行加密以防止复制的保护技术。它们需要一个专有的浏览器模块（如**谷歌 Widevine**）来解密和读取受保护的媒体。



**需要 DRM 的服务：**




- 视频流媒体：** Netflix、Disney+、HBO Max、亚马逊 Prime Video
- 高级音乐：** Spotify Premium、YouTube Music、Deezer
- 在线培训：** Udemy、Coursera（受保护的视频）



### 为什么 Zen 浏览器没有 DRM？



**主要原因：**


1. **成本和复杂性：** 谷歌 Widevine 许可证不是免费的，需要经过繁琐的审批程序。


2. **项目理念：** DRM 是一个专有的 "黑盒子"，与开源方法和独立于谷歌的做法格格不入


3. **资源有限：** 团队专注于 Interface 创新和保密工作



### 实际影响



**❌ 无法获得的服务：**


Netflix、Disney+、Spotify Premium、YouTube Premium、Udemy/Coursera 付费培训课程



![Erreur DRM Prime Video](assets/fr/17.webp)


*尝试播放受 DRM 保护的内容时的典型错误信息*。



**✅ 职能服务：**


免费 YouTube、Twitch、Vimeo、新闻网站、社交网络、播客



**旁路解决方案：**




- 仅使用 Firefox/Chrome 浏览器进行流媒体传输
- 本地应用程序（Netflix、Spotify）
- 选择无 DRM 内容（YouTube、Twitch、Bandcamp、PeerTube）



**当前状态：** Zen 团队已开始获取 Widevine 许可证，但尚未给出时间表。这一过程完全取决于谷歌的批准。



## 日常使用



### Interface 和导航



**标签式侧栏：**




- 每页的标题和缩略图
- 新标签页的 "+"按钮
- 拖放重组
- 上下文相关操作：右键复制、关闭、移动



**工作领域：**




- 侧边栏顶部的选择器
- 创建主题区域
- 在上下文之间快速切换
- 所有空间均可使用钉入式标签



![Création d'un nouvel espace](assets/fr/11.webp)


*Interface 以创建新工作区*



**高级功能：**




- 分割视图**：选择多个选项卡 > 右键单击 > "拆分 x 个选项卡"。
- 浏览**：Alt + 点击链接进行预览



### 实用快捷键





- ctrl+T`：新建标签页
- ctrl+空格工作区菜单
- ctrl+B`：显示/隐藏侧边栏
- ctrl+Shift+P`：私人窗口
- alt+点击一瞥（预览）



### 最佳做法





- 整理您的空间**：创建主题空间（工作、手表、个人）
- 使用固定标签**：针对您最常访问的网站
- 利用分割视图**：适合在大屏幕上进行多任务处理
- 保持更新**：定期检查更新
- 探索 Zen Mods**：根据自己的喜好定制外观



## 结论



Zen 浏览器是网络浏览器生态系统中的一股清流。通过将创新、高效的 Interface 与严格尊重隐私相结合，它为技术巨头的浏览器提供了一个可靠的替代选择。



它的垂直标签和工作空间真正改变了那些同时处理多个项目的用户的浏览体验。它的 "无谷歌 "理念和社区开发使其成为关注数字主权的用户的一致选择。



虽然 Zen 浏览器仍有一些限制（没有移动功能、缺少 DRM），但它已经足够成熟，可以满足日常使用的需要，而且由于其活跃的社区，Zen 浏览器正在迅速改进。



对于既重视工作效率又重视隐私的比特币用户和技术用户来说，Zen 浏览器绝对值得一试。你很可能会采用这种新的、更安静、更高效的浏览方式。



## 资源



### 官方链接




- [Zen 浏览器官方网站](https://zen-browser.app)
- [完整文档](https://docs.zen-browser.app)
- [GitHub源代码](https://github.com/zen-browser/desktop)
- [下载页面](https://zen-browser.app/download)


### 社区和支持




- [官方讨论区](https://discord.gg/zen-browser)
- [Reddit r/zen_browser](https://reddit.com/r/zen_browser)
- [Zen Mods Gallery](https://zen-browser.app/mods)