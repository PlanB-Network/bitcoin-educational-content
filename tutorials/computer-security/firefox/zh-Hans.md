---
name: 火狐浏览器
description: 如何配置火狐浏览器以保护您的隐私？
---

![cover](assets/cover.webp)



## 导言



我们都会花几个小时上网，却往往没有意识到我们的浏览器透露了我们的哪些信息。我们的每一次点击、每一次搜索、每访问一个网站，都在滋养着一个庞大的个人数据收集产业。



![Statistiques navigateurs 2024](assets/fr/01.webp)


*网络浏览器市场份额：Chrome 浏览器占据 65% 的市场份额，其次是 Safari 和 Edge。来源：[gs.statcounter.com]()[gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



如图所示，谷歌 Chrome 浏览器占据了全球 65% 以上的使用率。这种霸权意味着，大多数互联网用户将他们的浏览数据委托给了谷歌，而谷歌的商业模式是以有针对性的广告为基础的。火狐浏览器（Firefox）仅占 3% 的市场份额，它是由 Mozilla 开发的替代产品，Mozilla 是一家非营利组织，在利用用户数据方面没有任何商业利益。



但选择火狐浏览器只是第一步。在默认情况下，即使是火狐浏览器也需要进行调整，以最大限度地提高保护能力。本指南将从最简单到最先进的步骤一步步教你如何将 Firefox 变成一个名副其实的防跟踪盾牌，同时保持愉悦的浏览体验。



### 为什么是 Firefox？





- 免费、开源**（Gecko 引擎）：可审计、透明的代码
- 非营利组织**：Mozilla 基金会，具有普遍意义的使命
- 内置本地保护**：增强跟踪保护 (ETP)、全面 Cookie 保护 (TCP)、状态分区、仅 HTTPS 模式、HTTPS 上的 DNS (DoH)
- 高级自定义**：与 Chrome 浏览器不同，Firefox 可让您深入修改其行为



### 开始前的重要原则





- 没有通用配方**：修改得越多，就越有可能脱颖而出（留下指纹）。这样做的目的是为了更好地保护自己，同时又不引人注目。
- 逐步推进**：更改设置，测试常用网站，然后继续。没必要一次性更改所有设置。
- 个人平衡**：在隐私和易用性之间找到自己的折衷方案。



## 快速安装



![Téléchargement Firefox](assets/fr/02.webp)



**官方下载：** 请访问 [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/)。在该页面上，选择您的操作系统（Windows、macOS、Linux），即可访问相应的下载页面，其中包含具体的安装说明。





- Windows**：下载".exe "安装程序，双击并按照安装向导进行操作
- macOS**：下载".dmg "文件，打开并将 Firefox 拖入 "应用程序 "文件夹
- Linux**：有几种选择 - 包`.deb`/`.rpm`、Flatpak (Flathub)、Snap，或通过软件包管理器（apt、dnf、pacman）。首选 Mozilla 官方源。



**提示：** 安装后，请通过帮助 → **关于火狐**检查更新（对于安全补丁很重要）。



![Configuration initiale Firefox](assets/fr/03.webp)


*启动火狐浏览器的第一个界面：将火狐浏览器设为默认浏览器，将其添加到快捷方式中，然后点击 "保存并继续 "*。



![Création compte Firefox](assets/fr/04.webp)


*可选步骤：创建或登录 Firefox 账户。点击右下角的 "不是现在 "可以跳过此步骤*。



![Page d'accueil Firefox](assets/fr/05.webp)


*配置完成后的火狐主屏幕。注意右上角的☰菜单，可进入 "设置 "和 "扩展"，对火狐浏览器进行自定义*。



## 默认情况下已激活保护功能（令人放心）





- 站点隔离（Fission）**：在渐进式部署中。该功能在单独进程中运行每个站点，以防止一个恶意标签页访问另一个标签页的数据。通过 `about:support` 查看其状态（搜索 "Fission"）。如果未启用，可在 `about:config` 中使用 `fission.autostart = true` 手动激活。
- 全面 Cookie 保护 (TCP)**：默认为激活状态。Cookie 和其他存储仅限于第一方网站（每个网站一个 "罐子"），从而避免跨站跟踪。必要时可通过存储访问 API（集成登录按钮）进行临时例外处理。
- 跳转/重定向跟踪保护**：火狐浏览器会自动检测和清理跳转网站（在目的地之前通过跟踪器重定向的链接）留下的 cookies，从而减少这种跟踪渠道，而无需您采取任何行动。



## 第 1 级--基本（≤ 10 分钟）



目标：在不破坏网络的情况下大幅提高隐私保护。面向 90% 的用户。



要访问设置，点击右上角的菜单 ☰，然后点击 **"设置 "**：



![Paramètres généraux](assets/fr/07.webp)


*火狐设置页面--"常规 "选项卡。您可以在这里配置大部分隐私选项*。



**跟踪保护（ETP）**




- 将**ETP**改为**严格**。您将阻止更多跟踪器（跨站 Cookie、指纹识别、加密、社交小部件......）。
- 如果某个网站出现故障（视频、登录按钮......），请通过 🛡️ 盾停用仅针对该网站的保护，然后刷新标签页。



以下是不同的 ETP 安全级别：




- 标准**（平衡，最大兼容性）
  - 阻止：社交跟踪器、跨站 Cookie（所有窗口）、私人浏览中的跟踪内容、加密货币挖掘器、指纹探测器。
  - 包括 ** 全面 Cookie 保护** (TCP)：每个网站一个罐子。
- 严格** （建议用于保密）
  - 还能阻止所有窗口中的跟踪内容+已知和可疑的指纹识别。
  - 可能会破坏某些网站；请使用 🛡️ 屏蔽进行本地异常处理。
- 自定义**（高级）
  - 微调：cookies、跟踪内容、未成年人、指纹（已知/疑似）。



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies 和网站数据




- 启用**"关闭时删除 cookie 和网站数据 "**，以便每次重启时都能干净利落地重新启动。
- 如果需要，可为 2-3 个重要网站（电子邮件、银行）添加 **例外**。


**自动数据输入、建议和主页**




- 停用**自动填写**（身份证、地址、卡片）。改用密码管理器。
- 搜索**：停用 **"显示搜索建议 "**。
- Address栏**：削减**"赞助商建议 "**和**"上下文建议 "**。
- 主页**：禁用**口袋**和**赞助内容**。



![Paramètres cookies et mots de passe](assets/fr/08.webp)



*仅限 *HTTPS**




- 激活 **"仅在所有窗口中使用 HTTPS 模式 "**。


![Configuration DNS over HTTPS](assets/fr/09.webp)



**遥测和广告测量




- 在 "Firefox 的数据收集 "中，**取消选中所有**。
- 停用 **"隐私友好型广告措施 "** (PPA)。
- 安全浏览**：保持启用（推荐）。火狐浏览器通过散列查询和本地检查根据威胁列表检查网站，防止网络钓鱼和恶意软件，同时将对隐私的影响降到最低。



**全球隐私控制（可选）**




- 激活**GPC**，表明您拒绝出售/共享数据。



**搜索引擎




- 切换到**DuckDuckGo**、**Startpage**、**Qwant**或**Brave Search**（设置 → 搜索）。



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**私人导航**




- 私人窗口 (Ctrl/Cmd+Shift+P) 用于一次性会话（礼物、二级账户......）。避免使用 "始终保持私密 "模式：扩展可能会处于非活动状态，cookie 异常也会变得不那么有用。



**基本扩展**（从官方目录安装）




- uBlock Origin**：阻止广告和当前跟踪，轻量级。
- 隐私獾**：学会阻止跟踪；发送 "请勿跟踪"/"GPC"。
- ClearURLs**（可选）：Firefox (ETP Strict) 和 uBO 已经清理了很多；如果仍能看到 "脏 "URL（utm、fbclid），请保留它。
- Firefox 多账户容器**： **每个容器隔离 cookie/会话和存储；并行多账户；减少跨站跟踪**。官方扩展：`https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`。



![Extension Multi-Account Containers](assets/fr/12.webp)



**密码和 2FA**




- 使用专用密码管理器**（Bitwarden、KeePassXC）。 **避免**在浏览器中存储密码。 **尽可能启用 2FA**。



## 第 2 级 - 强化（隔间和网络）



目标：分隔活动，减少网络泄漏。



**通过 HTTPS 的 DNS（DoH）**




- 默认状态**：在某些地区（美国、加拿大、俄罗斯、乌克兰）已自动激活。其他地区需要手动激活。
- 配置** ：设置 → 常规 → 网络设置 → **启用 DoH** → **Cloudflare**或**Quad9** → **最大保护**。
- 最大保护 = 仅 TRR**（不回退到系统 DNS）。如果企业/酒店网络阻塞，请切换回**标准**或禁用 DoH。
- 冗余**：如果您已经在使用具有自己的安全 DNS 的可信 VPN，DoH 可以作为冗余。
- 验证测试**：https://www.dnsleaktest.com/"应仅显示所选的 DoH 提供商。



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**使用容器和配置文件进行分隔




- 多账户容器**：创建空间（个人、工作、财务、社交网络、购物、一次性）。为经常访问的网站配置**"始终在此容器中打开 "**。官方扩展名："https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/"。
- 为什么要使用它们？
  - 按空间对 cookie/会话/存储进行强隔离**。
  - 减少跨站跟踪**：限制巨头（Facebook、Google）。
  - 在同一服务上同时拥有多个账户**。
  - 降低分段身份之间出现 CSRF/XSS** 的风险。
  - 提示：至少要为社交网络/谷歌、工作、财务设置专用容器。
- Facebook 容器**（可选）：专门用于 FB/Instagram 的简化版本。
- 独立的配置文件**：通过 `about:profiles`（主配置文件、最小 "超安全 "配置文件、测试配置文件）。数据和扩展完全分隔。



**高级扩展**（待定）




- Cookie AutoDelete**：关闭标签页后立即删除网站 cookie（如果 Firefox 长时间处于打开状态，该功能很有用）。
- LocalCDN**：在本地提供当前库（减少对谷歌/微软的调用）。部分兼容。



**手机（安卓）**




- Firefox Android + uBlock Origin**：类似的移动保护。



## 第 3 级 - 专家（about:config 和 Arkenfox）



目标：在可接受的妥协基础上进行高级加固。建议使用**单独的配置文件**。



只能从以下两种方法中选择一种：



**方法 A - 手动修改**：通过`about:config`进行一些有针对性的调整（更简单、更精确的控制）


**方法 B - Arkenfox user.js**：全自动配置（更复杂，最大程度的保护）



➡️ **Arkenfox已经包含了下面提到的所有关于:配置的更改**，还有数百项更改。如果您选择 Arkenfox，请忽略 about:config 部分。



### 方法 A：通过 about:config 手动修改



在 Address 栏中键入 `about:config` → 接受风险。



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- 抗指纹识别（继承自 Tor 浏览器）


```text
privacy.resistFingerprinting = true
```


影响：UTC 时区、**letterboxing**（标准窗口大小）、标准化用户生成/策略、Canvas/WebGL/音频上下文限制。更加统一，但也有一些 "怪癖"（偏移时间，有时有点英语）。





- 禁用 WebRTC（避免 IP 泄露；破坏 Web visio）


```text
media.peerconnection.enabled = false
```





- 引用加兼容（默认）


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


严格选项（可中断付款/SSO）：


```text
network.http.referer.XOriginPolicy = 2
```





- 限制喋喋不休的应用程序接口和投机


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



黄金法则：如果出现故障，就回到上次的修改。



### 方法 B：Arkenfox user.js（全自动配置）



Arkenfox**项目提供了一个由社区维护的 "user.js "文件，可自动应用数百种面向隐私和安全的火狐首选项。重新启动时，火狐会从您的配置文件中读取该文件并应用这些设置。





- 有什么意义？从**一致的硬化基础**开始，无需 "到处点击"；减少疏忽；节省时间。
- 更改内容（示例）：切断遥测、加强 cookie/缓存/引用程序/HTTPS、**RFP** + 信箱化、**WebRTC 禁用**、DoH/TLS 调整、限制聊天 API。
- 何时使用：如果您希望在 10 分钟内加固火狐浏览器，并接受一些例外情况（DRM/流媒体、Web visio、SSO/支付）。
- 优点：快速、一致、**更新**（与 ESR 一致）、**文档**（维基+注释）、可通过重写**自定义**。
- 限制：兼容性（某些网络应用程序）、舒适性（UTC、窗口大小），以及提醒： **它不是 Tor**（没有网络匿名功能）。



安装（最好安装在**专用配置文件**上）


1.保存个人资料/收藏夹，并列出带有 Cookie 例外的网站。


2.从 `https://github.com/arkenfox/user.js` 下载 `user.js`（ESR/稳定版）。


3.通过 `about:profiles` 查找个人资料文件夹：




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4.关闭 Firefox 并将 `user.js` 移至配置文件文件夹的根目录。


5.重新启动；通过 `about:config` 或覆盖文件进行自定义。



更新




- 按照 Arkenfox 发布的版本（与 ESR 一致），替换 `user.js`，重新启动 Firefox；阅读发布说明。



**通过重写进行定制**



Arkenfox 的默认设置是有意限制的。要根据自己的需要调整某些设置（流媒体、Visio、特定网站），可以在 "user.js "的同一文件夹下创建一个 "user-overrides.js "文件。该文件允许你在不修改主文件的情况下 "覆盖 "某些 Arkenfox 偏好设置。



创建 `user-overrides.js` 并添加自定义内容：


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



最佳做法




- 使用单独的**"Arkenfox "配置文件**，并保持 "正常 "配置文件以保证舒适。
- 最小化扩展（uBlock Origin OK），以限制攻击面和唯一性。
- 必要时逐个网站添加例外（屏蔽 🛡️、uBO、NoScript（如使用））。
- 每次更改后都要进行测试：WebRTC/DNS 泄露、掩盖踪迹、CreepJS。



## 最佳做法





- 更新**：火狐浏览器和扩展程序已更新。
- 延期**：合理可靠；注意 "可疑 "赎回。
- 下载**：小心；在 VirusTotal 上测试敏感文件。
- 密码**： **专用管理器**（Bitwarden、KeePassXC）；启用**2FA**；避免在浏览器中存储。
- 卫生**：将 Google/Facebook 限制在容器中；定期关闭/打开以 "重置 "上下文。



## 限制与替代方案





- 加固的浏览器 ≠ 网络匿名性：如果没有**VPN**，你的 IP 仍然可见；即使有了它，也仍然可以进行关联。
- 修改过多会使你**独特**。 **RFP** 标准化；随机化工具（如变色龙）可以......让你与众不同。测试、比较、调整。
- 替代方案/补充方案：
 - Tor 浏览器：通过 Tor 实现网络匿名；速度较慢。请参阅我们的完整安装和配置指南** ：



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad 浏览器："没有 Tor 的 Tor"，与 VPN 结合使用；标准足迹。在我们的专门教程中了解如何安装** ：



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- 推荐组合：火狐浏览器（2 级）+ VPN 用于日常使用；Tor/Mullvad 用于敏感活动；独立配置文件用于分隔。



## 结论



按照本指南逐步操作，您就能将 Firefox 变成真正的数字监控防护堡垒。从基本的 1 级设置到高级的 Arkenfox 配置，每一项更改都能在不影响浏览体验的情况下加强隐私保护。



**您的隐私现在得到了更好的保护**：广告跟踪器已被阻止、cookie 已被分隔、IP Address 泄露已被中和、遥测已被禁用。火狐浏览器不再只是一个浏览器，而是为您量身定制的数字防护工具。



**请记住：保密永远不是必然的。定期测试您的保护措施，更新您的设置，并根据您的习惯变化随时调整您的配置。您的在线匿名性既取决于您的工具，也取决于您的习惯。



## 资源



### Plan ₿ Network




- SCU 202 - 提高个人数字安全：要进一步了解本教程中涉及的数字安全概念**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla 文档




- [增强跟踪保护](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop) ：增强跟踪保护官方指南
- [状态分区](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning)：状态分割技术文档
- [MDN网络安全](https://developer.mozilla.org/docs/Web/Security) ：有关网络安全的完整参考资料



### 阿肯福克斯




- [维基和安装指南](https://github.com/arkenfox/user.js/wiki)：完整的 Arkenfox 项目文档
- [存放和发布](https://github.com/arkenfox/user.js)：下载 user.js 文件并跟踪更新



### 导游和社区




- [PrivacyGuides - 桌面浏览器](https://www.privacyguides.org/en/desktop-browsers/)：浏览器推荐和比较
- Reddit**：r/firefox、r/privacy 以获得反馈和支持
- 隐私指南论坛**：深入的技术讨论



### 测试工具




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/)：数字指纹和反追踪的有效性
- [DNS 泄露测试](https://www.dnsleaktest.com/)：DNS 泄露测试和 DoH 效率
- [BrowserLeaks](https://browserleaks.com/)：完整的测试套件（WebRTC、画布、字体等）
- [BadSSL](https://badssl.com/)：SSL/TLS 证书验证测试
- [CreepJS](https://abrahamjuliot.github.io/creepjs/)：对 50 多种指纹向量进行高级分析
- [Cloudflare DNS 测试](https://1.1.1.1/help) ：检查 Cloudflare DoH 是否正常运行