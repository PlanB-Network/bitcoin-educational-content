---
name: 猎户座浏览器
description: 如何在 Mac 和 iPhone 上使用 Orion 浏览器保护隐私？
---

![cover](assets/cover.webp)



## 导言



在大多数浏览器都在大量收集我们的个人数据的情况下，选择一款隐私友好型浏览器变得至关重要。Chrome 浏览器占据了全球 65% 的市场份额，但其商业模式是基于对用户浏览数据的利用。Safari 虽然融入了苹果生态系统，但缺乏先进的保护功能，也不能灵活地支持第三方扩展。



![Répartition du marché des navigateurs](assets/fr/01.webp)


*网络浏览器市场细分：Chrome 浏览器占据 65% 以上的市场份额，其次是 Safari、Edge 和 Firefox*。



**Orion浏览器**是苹果用户的创新选择。这款浏览器由 Kagi 开发，将 WebKit 引擎的速度与零遥测理念相结合。与竞争对手不同的是，Orion 不向远程服务器发送数据，并能屏蔽 99.9% 的广告和跟踪器，包括 YouTube。



它的独特之处是什么？Orion 是唯一一款可以安装 Chrome 浏览器和 Firefox 浏览器扩展的 WebKit**浏览器，提供了两个世界的最佳功能。这种兼容性，加上比其他浏览器低 2 到 3 倍的内存消耗，以及与苹果生态系统（iCloud、钥匙串）的无缝集成，使其成为注重隐私的 Mac 和 iPhone 用户的理想选择。



## 为什么选择 Orion 浏览器？



### 主要优势



**开箱即享最大保护**：Orion 默认拦截 99.9% 的广告（包括 YouTube）以及所有第一方和第三方跟踪器。其技术结合了 WebKit 的智能跟踪防护和 EasyPrivacy 列表，可实现最高效率。独特功能：Orion 可在脚本执行之前**屏蔽指纹脚本，使跟踪成为不可能--与其他仅尝试 "屏蔽 "数据的浏览器相比，这是一种更彻底的方法。



**零可验证遥测**：Orion 采用激进的隐私保护方法，在设计上实现了零遥测。其他浏览器在启动时会发出数以百计的网络请求（IP 指数、浏览器指纹、个人信息），而 Orion 则不同，它从不 "打电话回家"。这一本质区别彻底消除了无意数据泄露的风险。



**卓越性能**：基于 WebKit 的优化版本，Orion 在 Mac 上的运行速度可媲美甚至超越 Safari。在速度计 2.0/2.1 测试中，Orion 在苹果硅处理器上一直名列第一。本地广告拦截功能可将页面加载速度进一步提高 20%至 40%。



**通用扩展支持**：作为一项重大创新，Orion 允许你安装来自 Chrome 网上商城**和** Mozilla 附加组件的扩展。WebExtensions 支持目前处于试验阶段，目标是在测试版发布时实现 100% 的兼容性。你甚至可以在 iPhone 上使用 uBlock Origin、Bitwarden 等许多流行的扩展，这在 iOS 上尚属世界首例，不过有些扩展可能无法完美运行。



### 应注意的局限性





- 供应有限**：目前仅限 macOS 和 iOS/iPadOS。Linux 版本已达到开发里程碑（2025 年达到里程碑 2），但尚未推出公开版本。由于缺乏资源，Windows 和 Android 尚未开发。
- 封闭源代码**：虽然有些组件是开源的，但 Orion 仍然主要是专有的，这也是隐私社区争论的焦点。
- 试验性扩展** ：扩展支持仍处于测试阶段，经常出现不兼容问题。扩展可能会影响性能，有些甚至根本无法运行。
- WebKit 安全性**：与 Chromium 不同，WebKit 不提供如此强大的每个站点进程隔离功能，这在某些情况下可能会带来安全风险。
- 屏蔽测试**：在在线广告测试中，Orion 故意表现不佳（26%-35%），因为 Kagi 认为这些测试 "从根本上存在缺陷"。日常使用中的实际效果要好得多。



## 安装 Orion 浏览器



### 在 macOS 上



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Kagi 主页将 Orion 浏览器介绍为 "具有全面隐私保护和通用扩展支持功能的无广告浏览器 "*。





- 请访问 [kagi.com/orion](https://kagi.com/orion/)
- 点击 "**下载适用于 macOS 的 Orion**"。



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Orion 浏览器下载页面显示 MacOS 和 iOS 的可用性，并提供 App Store 链接*。





- 打开下载的 `.dmg` 文件
- 将 Orion 应用程序拖入 "应用程序 "文件夹
- 首次启动时，macOS 会要求您确认打开



**Alternative Homebrew** ：


```bash
brew install --cask orion
```



### 在 iPhone/iPad 上





- 打开**应用商店**
- 搜索 "**Orion Browser by Kagi**"
- 安装免费应用程序（兼容 iOS 15 及以上版本）



### 初始配置



首次发射时，Orion 会引导您完成几个步骤：



**1.欢迎屏幕


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion 浏览器欢迎屏幕突出显示主要功能：更快的浏览速度、零遥测、广告拦截和扩展支持*。



**2.Interface** 定制


![Options de personnalisation](assets/fr/05.webp)


*自定义屏幕可让您根据自己的喜好配置选项卡和 Interface 的外观*。





- 数据导入**：轻松从 Safari、Chrome 或 Firefox 转移收藏夹和密码
- ICloud 同步**：激活后可在所有 Apple 设备上找到您的收藏夹和标签页



**3.在移动设备上安装**


![Installation sur iOS](assets/fr/06.webp)


*iOS 上的安装屏幕显示二维码，以便从 App Store 快速下载 Orion 浏览器*。



**4.欢迎使用 Interface 和基本工具



![Page d'accueil Orion](assets/fr/07.webp)


*Orion 浏览器 Interface 主页：箭头表示可直接从 Address 栏* 访问的三个关键工具



配置完成后，您会发现 Orion 的 Interface 简化版配备了**三个基本工具**（箭头所示）：





- 屏蔽 🛡️**：显示隐私报告，其中包含当前页面上被阻止的项目数量
- 刷 🖌️**：自定义页面显示（主题、字体、移除分散注意力的 Elements）
- 齿轮 ⚙️**：配置网站特定参数（权限、屏蔽等）



这些工具随时可用，可让您控制每个网站的浏览体验。



**重要**：Orion 是免费的，无需注册或创建账户即可运行。



![Orion+ dans les préférences](assets/fr/08.webp)


*偏好设置中的 Orion+ 订阅屏幕，提供支持开发的可选订阅*。



**Orion+（可选）**：为支持项目开发，Kagi 提供 Orion+（每月 5 美元、每年 50 美元或终身 150 美元）。这种自愿订阅可使.NET Framework 3.0成为可能：




- 直接与开发团队沟通
- 根据您的需求影响浏览器的发展
- 访问具有最新实验功能的夜间版本
- 受益于最新的 WebKit 引擎
- 在反馈论坛上获得独特的徽章



Orion+ 保证项目的独立性："您的资助有助于我们保持独立，并信守成为用户最佳浏览器的承诺"。正是这种用户出资模式使 Orion 保持了无广告和无遥测的特性。



## 最大限度保密的配置



### 基本参数



通过 **Orion → 首选项**（或 ⌘, ）访问首选项：



**1.搜索 - 私人搜索引擎**



![Configuration du moteur de recherche](assets/fr/09.webp)


*默认搜索引擎配置：选择 DuckDuckGo 可最大限度地保护隐私*。





- 默认引擎**：选择 **DuckDuckGo**、**Startpage** 或 **Kagi**，以获得最佳隐私保护（避免使用 Google/Bing）。
- 搜索建议**：禁用搜索建议，防止键盘输入信息泄露给搜索引擎服务器



**2.隐私--一般**保护



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orion 隐私设置显示内容拦截器，包含 119 156 个活动规则、跟踪器移除选项和自定义用户代理*。



**内容拦截器默认处于激活状态** ：




- EasyList** ：119k+ 广告拦截规则
- EasyPrivacy**：防止跟踪
- 管理过滤列表**：添加其他列表（建议使用 Hagezi）



**隐私选项** ：




- 删除 URL 中的跟踪器**："仅限私人浏览 "可清除复制的链接
- 共享碰撞报告**："请求批准后 "尊重您的同意
- 自定义用户代理**：可进行修改以绕过某些拦截



![YouTube avec Privacy Report](assets/fr/10.webp)


*使用 Orion 观看 YouTube 的示例：看不到广告，隐私报告显示屏蔽了许多 Elements* 。



**3.网站设置 - 按网站进行控制**



![Website Settings pour YouTube](assets/fr/11.webp)


*显示兼容性选项、内容屏蔽和特定网站权限的 YouTube 网站设置*。



**快速访问**：点击 Address 栏中的齿轮 ⚙️ 进行调整：




- 兼容性模式**：通过暂停扩展解决显示问题
- 内容阻止程序**：必要时停用对特定网站的拦截
- JavaScript/Cookies**：按网站进行细粒度控制
- 权限**：摄像头、麦克风、位置单独配置



**4.高级自定义筛选器**（见下文）



**创建自定义筛选器** （隐私 → 管理筛选器列表 → 自定义筛选器） ：



**简化语法**（兼容 Adblock Plus）：




- `reddit.com##.promotedlink`：隐藏赞助的 Reddit 帖子
- |ads.example.com^`：完全屏蔽广告域
- `@@@||site-utile.com^`：为网站创建异常



**提示：访问 [FilterLists.com](https://filterlists.com)，获取数千份随时可用的专门列表。



### 建议的扩展



Orion 本身支持 Chrome 和 Firefox 扩展。直接从官方商店安装即可：



**Essentials** ：




- uBlock Origin**：为本地拦截器添加细粒度控制
- Bitwarden**：开源密码管理器
- 清除 URL**：删除 URL 跟踪参数



**可选** ：




- 本地 CDN**：为本地共享库提供服务
- Cookie 自动删除**：关闭标签页后自动删除 cookie
- NoScript**：全面控制 JavaScript 的执行（高级用户）



安装.NET Framework




- 访问 [chrome.google.com/webstore](https://chrome.google.com/webstore) 或 [addons.mozilla.org](https://addons.mozilla.org)
- 点击 "添加到 Chrome/Firefox"。
- Orion 将自动拦截并安装扩展



**注意**：由于扩展支持是试验性的，许多扩展可能无法正常工作或影响性能。如果出现问题（网站不再运行、速度变慢），请逐个禁用扩展，以找出问题根源。



## 日常使用



### Interface 和独特功能




![Outil de personnalisation pinceau](assets/fr/13.webp)


*用于自定义显示的 Orion 刷子菜单：字体大小、主题（浅色/深色）、停用粘贴式页眉和删除分散注意力的 Elements*



**画笔工具：高级定制**



Orion 的**刷**工具是一项独特的功能，可让您自定义每个网站的显示内容：



**主题选项** ：




- 在每个网站的浅色和深色主题之间切换
- 自动适应您的系统偏好



**排版控制** ：




- 字体大小**：使用 A- 和 A+ 按钮调整字体大小
- 字体样式**：更改字体系列（默认或自定义）



**Interface 清洁** ：




- 禁用粘性标题**：删除滚动时停留在顶部的标题
- 清除 Elements**：永久删除恼人的 Elements（广告、弹出式窗口、cookie 横幅广告）
  - 点击 "+ 删除"，然后选择要隐藏的项目
  - 对有持续性广告或可视化跟踪 GW 的网站非常有用-13



**持久性**：所有这些设置都会按域保存，并在您下次访问时自动重新应用。



**高级选项卡管理** ：




- 垂直标签**：通过菜单栏激活（侧面标签功能）
- 压缩标签** ：在 "偏好设置"→"选项卡"→"布局 "中选择 "压缩"，以节省空间
- 标签组**：按主题组织会议
- 多种配置文件**：通过菜单栏（配置文件功能）创建独立身份，数据完全隔离



**低功耗模式**：受到 iPhone 的启发，该模式会在 5 分钟后自动暂停不活动的标签页，最多可减少 90% 的能耗。在 Mac 上可通过 Orion 的菜单栏激活，在 iOS 上可在设置中激活。



**内置工具**（编辑菜单及其他） ：




- 编辑页面上的文本**：临时修改任何文本（编辑菜单）
- 允许复制和粘贴**：绕过复制限制（编辑菜单）
- 复制清除链接**：右键单击链接以删除跟踪参数
- 聚焦模式**：全屏导航，无需分心
- 画中画**：在浮动窗口中观看视频
- 在 Internet Archive 中打开**：直接访问存档版本
- 隐私报告**：点击屏蔽 🛡️，查看各页面屏蔽的项目



### 私人浏览管理



猎户座的私人导航 (⌘⇧N) 提供：




- 完全隔离 cookie 和会话
- 关闭时自动删除
- 历史记录和缓存停用
- 增强指纹识别保护



**提示**：要进行高级分隔，可通过菜单栏（配置文件功能）创建**独立的配置文件**。每个预案在 Dock 中显示为单独的应用程序，其自身的设置、扩展和数据完全隔离。



### 性能优化和隐私



让猎户座保持快速和私密




- 扩展** ：严格限制到最低限度（可能会降低性能）
- 低功耗模式**：长时间使用时启动（可节省 90% 的电量）
- 隐私报告**：点击防护罩 🛡️ 实时查看阻塞情况
- 视觉定制**：使用 🖌️ 笔刷调整显示效果并移除干扰的 Elements
- 复制干净链接**：右键复制无跟踪器的链接
- 单独配置文件**：使用专用配置文件将您的活动分门别类
- 网站设置**：单击齿轮 ⚙️ 按网站调整权限
- 定期清理**：通过猎户座清除缓存 → 清除浏览数据



## 与替代品的比较



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**对比 Safari**：Orion 通过高级拦截器和扩展支持提供卓越的保护，同时保持 WebKit 性能。



**与 Chrome 浏览器相比**：由于支持 Chrome 浏览器扩展功能，因此具有无与伦比的私密性，同时不影响兼容性。



**与 Firefox**相比：在 Mac 上运行速度更快，Interface 更直观，但细粒度控制较少，而且不是开源。



**与 Brave**相比：理念相似，但 Orion 避免了加密/BAT 争议，并提供更好的苹果集成。



## 推荐使用案例



**适合** ：




- 苹果用户寻求比 Safari 更多的隐私保护
- 希望在不使用扩展程序的情况下屏蔽所有广告（包括 YouTube）的用户
- 开发人员需要集成隐私保护功能的 WebKit 开发工具
- IPhone 用户希望在移动设备上使用桌面扩展（独特创新）
- 需要将自己的活动分门别类的专业人员（多重档案）
- 寻求更好电池管理（低功耗模式）的移动用户



**如果** ：




- 您主要使用 Windows/Linux（无可用版本）
- 完全开源对您的威胁模式至关重要
- 您依赖的特定扩展可能无法正常工作
- 您需要超越苹果生态系统的跨平台同步功能
- 您更喜欢成熟、稳定的解决方案（自 2021 年起处于永久测试状态）



## 注意事项和安全



### 独特的安全功能



**革命性的反指纹保护**：Orion 是唯一一款能在指纹脚本扫描系统之前完全阻止其执行的浏览器。这种 "无脚本运行=无指纹识别可能 "的方法优于其他浏览器使用的传统屏蔽方法。



**透明白名单**：猎户座会维护一个小型的公开网站列表（browserbench.org、wizzair.com），这些网站会自动禁用阻止功能，以避免出现故障。这种透明度使用户能够准确了解何时以及为何会解除封堵。



**未经审核的扩展**：支持 Chrome/Firefox 扩展程序会带来额外风险，因为这些扩展程序不是为 WebKit 设计的，也未针对此环境进行专门审核。



### 维护和更新





- 自动更新**：通过 Sparkle 在 macOS 上自动更新 Orion
- 漏洞跟踪**：定期检查安全补丁的发布说明
- 错误报告**：使用 [orionfeedback.org](https://orionfeedback.org) 报告问题




## 结论



Orion 浏览器代表着 macOS 和 iOS 上的隐私保护向前迈进了一大步。它的零遥测方法，加上超高效的原生拦截器和对通用扩展的独特支持，使其成为注重隐私的苹果用户的绝佳选择。



**重要**：自 2021 年起，Orion 仍处于永久测试阶段，存在扩展兼容性限制和固有的 WebKit 风险。请根据您的威胁模型评估这些权衡。



对于在 Mac 或 iPhone 上的日常使用，它可能是苹果生态系统中保密性、性能和易用性之间的最佳折衷方案，前提是你接受它的局限性。



请记住：保护您的隐私不仅仅取决于您的浏览器。将 Orion 与最佳实践（强密码、2FA、必要时使用 VPN）相结合，可获得最佳的在线安全性。



## 资源和支持



### 正式文件




- 官方网站**：[kagi.com/orion](https://kagi.com/orion/)
- 完整的常见问题**：[browser.kagi.com/faq](https://browser.kagi.com/faq)
- 社区论坛**：[community.kagi.com](https://community.kagi.com)
- 错误跟踪**：[orionfeedback.org](https://orionfeedback.org)
- GitHub Orion** ：[github.com/OrionBrowser](https://github.com/OrionBrowser) - 开放源码组件
- 博客 Kagi** ：[blog.kagi.com](https://blog.kagi.com) - 新闻和更新



### 建议的验证测试



配置完成后，测试您的设置：




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - 指纹测试
- [DNS 泄漏测试](https://www.dnsleaktest.com/) - 检查 DNS 是否泄漏
- [BrowserLeaks](https://browserleaks.com/) - 完整的隐私测试套件



### Plan ₿ Network 的替代品


要获得最大程度的保护，请查阅我们的其他指南：




- [加固的火狐浏览器](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - 高级多平台配置
- [Tor 浏览器](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - 完全网络匿名
- [Mullvad浏览器](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - 最大程度的指纹保护



如果您想更多地了解浏览器的历史和操作，以及日常生活中的主要数字对象，我邀请您来了解我们新的免费培训课程 SCU 202（可在 Plan ₿ Network 上获取）：



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
