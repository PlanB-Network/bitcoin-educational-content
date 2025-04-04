---
name: GrapheneOS

description: Graphene OS 教程
---

> "[GrapheneOS](https://grapheneos.org/) 是一个以隐私和安全为重点的移动操作系统，具有 Android 应用兼容性，由非营利开源项目开发。"

GrapheneOS 最初于 2014 年以 'CopperheadOS' 的名字成立，它基于传统的 Android 代码（AOSP），但进行了许多改进，旨在提高用户隐私和安全性。GrapheneOS 让用户控制他们的手机，而不是大型科技公司。

### 目录:

- 引言
- 准备工作
- 安装
- 应用替代品
- 缺点
- 有用的信息

指南由 https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md 提供

## 为什么使用 GrapheneOS？

现代手机是价值 500 至 1000 美元的追踪和数据收集设备。我们生活的每一个方面都通过它们运行，不幸的是，很多这样的数据以某种形式与第三方共享。
GrapheneOS 专门构建，以减少这种数据共享并提高您的设备安全性，防范潜在的攻击途径。GrapheneOS 没有所谓的账户。您不需要一个账户来下载应用程序或与操作系统交互。简单来说，您不是产品。

GrapheneOS 通过一些简单的核心原则为您的 Android 体验提供额外的安全性。

1. **减少攻击面** - 移除不必要的代码（或者说是预装软件）。
2. **防止漏洞暴露** - 允许用户有足够的细粒度选择他们能接受的妥协。
3. **沙盒隔离** - GrapheneOS 加强了现有的 Android 沙盒，进一步锁定每个应用与手机其余部分通信的能力。

了解更多关于 GrapheneOS 功能集的技术细节 [这里](https://grapheneos.org/features)。

### 简化过渡

如果您多年来一直深陷于 Google 或 Apple 生态系统中，一夜之间失去所有这些便利的想法可能会让人感到害怕。但是，通过一些仔细考虑的应用安装决策（稍后介绍），可以减少或消除这种预期的困难。

尽管替代品变得越来越好，但这种变化的想法仍然可能令人望而却步。如果您发现自己处于这种情况，我最好的建议是，暂时将您的新 GrapheneOS 设备与现有手机并行使用。从那里开始，您可以慢慢地每周减少使用 2-3 个应用，直到您发现自己只使用 GrapheneOS 设备。

如果您采取这种方法，请对自己严格要求，尽快切断对被监视替代品的依赖。我们人类是懒惰的，往往会选择最少阻力的路径。记住您首次进行切换的原因。

**您选择用您的时间，有时是您辛苦赚来的钱（取决于您安装的替代应用程序）来支付，而不是用您的个人数据。**

## 开始使用

GrapheneOS 目前仅为[谷歌 Pixel](https://grapheneos.org/faq#supported-devices) 系列手机生产（颇具讽刺意味）。这并非没有充分的理由。Pixel 提供最佳的基于硬件的安全性，以补充加固操作系统所做的工作。这包括特定组件隔离和验证启动等内容。

### 选择设备

在选择要在其上安装 GrapheneOS 的 Pixel 时，请确保检查设备将继续获得默认[安全更新](https://support.google.com/pixelphone/answer/4457705?hl=zh-CN#zippy=%2Cpixel-xl-a-a-g-a-g)的时间长度。
在撰写本文时，Pixel 6a 是目前价格最便宜且拥有良好长期支持的型号，保修期至2027年7月。如果您选择了这款型号，需要注意的是，出厂版本的股份操作系统（stock OS）无法进行OEM解锁。您需要通过空中更新（over-the-air update）将其更新至2022年6月或更晚的版本。更新后，您还需要对设备进行出厂重置以修复OEM解锁问题。所有其他已解锁运营商锁的型号将可以直接安装GrapheneOS。

在选择设备时，您还需要确保购买的是解锁版本。某些运营商，如Verizon，出售的设备是引导程序锁定的，这完全阻止了以下过程。

### 安装GrapheneOS

GrapheneOS的[网络安装器](https://grapheneos.org/install/web)使整个过程变得非常简单，任何人都可以在10分钟内完成。
以下指南是从上述链接中提取的简化版本。

您需要准备的是：

- Pixel 设备
- 一根从手机到电脑的USB线
- 一台可以运行网络浏览器的电脑（任何基于Chromium的浏览器：Chrome, Edge, Brave等）

1. 第一步是进入 **设置** > **关于手机** 并反复点击构建号码，直到看到 **'开发者模式'** 被激活。
2. 接下来前往 **设置** > **系统** > **开发者选项** 并启用 **'OEM解锁'**。
3. 现在重启设备并在手机开机时按住音量减按钮。
4. 将手机连接到您的笔记本电脑，如果出现授权提示，请允许连接。
5. 在网络安装器页面上，点击 '解锁引导程序'。
6. 然后您会看到手机选项发生变化。使用音量按钮更改选择为 `解锁` 并使用电源按钮确认。
7. 接下来在网络安装器页面点击下载发布版本。
8. 下载完毕后，继续下一步点击 '刷写发布版本'。这个过程需要一两分钟，期间无需触摸手机。
9. 最后，进入网络安装器的下一步并点击 **锁定引导程序**。您需要像之前的过程中那样更改选择并用电源按钮确认。
10. 当您看到 `开始` 字样时，用电源按钮确认，设备将启动进入您的新的无Google操作系统。

![image](assets/2.webp)

GrapheneOS启动屏幕

_初次启动和设置后，建议从设置 > 系统 > 开发者选项中禁用OEM解锁。_

_您可能还想采取额外的、可选但推荐的步骤，通过Auditor app验证安装。您需要一台安装了该应用的另一部Android手机来完成此步骤。有关此步骤的说明可以在[这里](https://attestation.app/tutorial)找到。_

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

视频详细介绍了上述简单步骤

如果这些简单的步骤看起来有些困难，您可以考虑购买已预装GrapheneOS软件的Pixel[预装版](https://ronindojo.io/en/roninmobile)。但请注意，这样做您需要对提供商有一定程度的信任。

### 预装应用程序

现在您已经设置好了，您可能会注意到GrapheneOS在首次安装时看起来非常简洁。默认情况下，您将拥有这些应用程序：

![image](assets/3.webp)

默认应用程序
您可能不熟悉的两个术语是“审计员”和“钒”。

- [审计员应用](https://play.google.com/store/apps/details?id=app.attestation.auditor)利用基于硬件的安全特性来验证设备的身份以及操作系统的真实性和完整性。它将验证设备是否运行着原厂操作系统、引导程序是否已锁定，以及操作系统是否未被篡改。
- [钒](https://github.com/GrapheneOS/Vanadium)是基于Chromium网络浏览器的隐私和安全加固变体。

## 自定义

手机设置是个人化的事情，但这里有一些我在安装GrapheneOS时首先更改的设置，以让自己感觉更舒适。

### 设置壁纸和更新主题

前往设置 > 壁纸和样式。在这里我会：

- 更新从网上下载的家用和锁屏背景图片。
- 选择整个用户界面中使用的强调色。
- 启用暗色主题。

### 显示电池百分比

前往 **设置** > **电池**，然后在状态栏启用 **显示电池百分比**。

### 导入联系人

**从另一部安卓手机** - 前往联系人应用并寻找导出到VCF选项。

**从iOS** - 使用像是Export Contact这样的应用，并使用'vCard'导出选项来导出VCF文件。
一旦你有了VCF文件，你可以通过外部存储选项（如microSD卡或USB驱动器）将其传输到你的GrapheneOS设备。如果你手边没有这些设备，你可以选择通过下面列出的许多应用之一分享。

![image](assets/4.webp)

个性化主屏幕

## 替代应用

为了使您的手机有用，您将想要安装一些应用程序！以下选项之所以被包括，是因为我个人使用过它们，或者它们从更广泛的隐私社区获得了强烈推荐。还有许多其他未提及的优秀替代品，[Awesome Privacy](https://awesome-privacy.xyz)为所有类型的设备提供了一个非常广泛的隐私保护应用列表。

仅仅因为一个应用是自由和开源软件（FOSS），并不意味着它不会有潜在的隐私泄露。使用[Exodus](https://reports.exodus-privacy.eu.org/en/)查看您偏好的应用在隐私审计中的表现如何。

### F-Droid

[F-Droid](https://f-droid.org/)是一个可安装的安卓FOSS应用目录。客户端使在您的设备上浏览、安装和更新应用变得简单。值得一提的是，通过F-Droid的更新有时可能比其他应用商店慢。这主要取决于应用是否通过主F-Droid仓库或自定义仓库找到。

要安装F-Droid，只需通过GrapheneOS手机上的浏览器访问他们的网站并点击下载。这将下载一个`.apk`文件。然后，系统会询问您是否想要安装该应用。

除了在F-Droid中默认仓库找到的应用外，许多开源项目也会在F-Droid应用设置中托管自己的仓库。如果是这种情况，相关项目会在其网站上引导您完成此操作所需的非常简单的步骤。

![image](assets/5.webp)

F-Droid主屏幕

### 极光商店
[Aurora Store](https://auroraoss.com/) 是 Google Play 商店的一个 FOSS（自由开源软件）版本。Aurora 的外观和感觉与传统的 Play 商店非常相似，允许您下载和更新您通常通过 Google 选项找到的任何应用程序。
Aurora 的杀手级功能是匿名登录。这意味着您可以下载任何您喜爱的应用程序，这些应用程序通过 F-Droid 或直接 APK 不可用，而无需登录您的 Google 账户。

在您急于将此设置为默认安装选项之前，请记住，我们试图远离的许多应用程序都是从 Play 商店安装的。仅仅因为它们可以通过 Aurora 访问，并不改变一些可能嵌入跟踪功能的事实。虽然不总是可能，但只要您能够，就在通过 Aurora 下载之前寻找 F-Droid 的替代品。

要安装 Aurora，只需在 F-Droid 中搜索“Aurora Store”。

Aurora 也有一些潜在的攻击途径，因为“匿名账户”实际上是由 Aurora 创建和控制的。理论上，它们可能提供恶意更新或将应用推送到您的手机，尽管您仍然需要在设备上接受安装提示。Aurora 有时也会因为地区和设备读取错误而导致某些应用不显示。通常可以通过以下步骤解决这个问题。

**顶级提示** - 有时 Aurora Store 会遇到速率限制，限制您搜索和安装应用的能力。要解决这个问题，请转到 **设置** > **应用程序** > **Aurora** > **默认打开**，然后添加域名 `play.google.com`。现在，每当您导航到具有“通过 Play 商店下载”链接的产品或服务网站时，点击它将在 Aurora 中打开该应用，供您下载。

![image](assets/6.webp)

Aurora Store 主屏幕

### APK 下载

Android 上的应用程序也可以通过 `.apk` 文件下载和安装。这是一个很好的替代方案，不需要第三方应用商店，只需直接从项目或服务的网站或 GitHub 仓库下载文件。

这种方法的缺点是您不会获得自动更新，因此您需要监视该服务的通信渠道以了解新版本。然而，有一个很好的项目叫做 Obtanium，旨在解决这个问题。[Obtainium](https://github.com/ImranR98/Obtainium) 允许您直接从它们的发布页面安装和更新开源应用，并在新版本可用时接收通知。

![image](assets/7.webp)

Obtanium 预览

### Web 应用

对于您可能想要不频繁使用的服务，并且不想下载原生应用程序的时候，您可以简单地访问网页版本。如今，许多网站也提供渐进式 Web 应用（PWA）支持。这是指您可以将特定网站（例如 Twitter.com）的书签添加到手机的主屏幕上。然后当您点击图标时，它会以全屏应用程序的形式打开，没有典型浏览器体验中的常见干扰。您可以在下面看到这是如何实现的示例。

要在 GrapheneOS 的原生浏览器 Vanadium 中实现这一点，只需导航到所选网站，点击屏幕右上角的三个垂直点，然后点击 **“添加到主屏幕”**。

这种方法的唯一缺点是，因为这只是一个书签的网页，您不会获得任何形式的通知。尽管有些人可能会认为这是一个积极的方面！

![image](assets/8.webp)

Twitter PWA

### Web 浏览器
选择预包装选项，Vanadium，你真的不会出错。这款应用的表现与我尝试过的任何其他移动浏览器无异，我从未遇到过任何兼容性问题。
当你需要访问Tor原生的`.onion`网站时，你可以直接从他们的[网站](https://www.torproject.org/download/#android)或通过F-Droid下载Tor浏览器APK。

### VPNs

为了保护你的在线活动不被窥探的互联网服务提供商（ISP）所知，使用虚拟私人网络（VPN）应用是一个不错的选择。VPN通过加密隧道将你的互联网流量发送到由VPN服务提供商控制的共享IP地址，以确保你的设备活动无法与你联系起来。

以下是3个受到良好评价的选项，它们允许你使用比特币支付服务费用，且无需提供任何个人信息。所有3个选项都可以通过F-Droid获得。

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### 消息传递

近年来，加密消息解决方案变得越来越多。然而，问题仍然存在，如果你没有使用它的联系人，那么即使你安装了最好、最私密的选项，又有什么意义呢？

大多数对隐私领域不感兴趣的人可能会使用WhatsApp或iMessage。前者可以通过Aurora Store下载，但后者显然不适用于GrapheneOS！

- [Signal](https://signal.org/) 是一款较为流行的端到端加密（E2EE）通讯应用，它有着强大的记录和丰富的功能集。Signal需要一个电话号码来注册，所以如果你打算与那些你宁愿他们不知道你电话号码的人聊天，或许可以考虑一些替代方案。Signal必须通过Aurora Store下载。
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) 是一款相对较新的E2EE通讯应用。它没有用户ID，不需要电话号码或个人信息。人们可以通过扫描你的个人二维码或访问你的独特链接来找到你。Simplex还允许高级用户运行自己的服务器，以进一步减少对任何中心化实体的依赖。Simplex没有桌面客户端，所以如果多设备是你的优先列表上的，它可能不适合。Simplex for Android可以通过F-Droid获得。
- [Threema](https://threema.ch/en/faq/libre_installation) 提供了与Simplex类似的体验，但已经存在更长时间，因此感觉更加成熟一些。Threema不是免费的，终身许可费用为4.99美元，可以用比特币购买。Threema提供了网络客户端和原生桌面应用。Android应用可以通过F-Droid获得。
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) 是官方Telegram应用的一个非官方FOSS分支，用于Android。Telegram拥有E2EE的“秘密聊天”，但默认选项并不私密。Telegram FOSS可以从F-Droid下载。

![image](assets/9.webp)
左边：Threema
右边：Simplex

### 媒体
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) 是一个跨平台的Spotify客户端，不需要Premium账户即可使用。Spotube可以通过F-Droid获取。
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) 是一个出色的应用程序，可以免费从YouTube音乐流媒体任何音乐。ViMusic可以从F-Droid下载。
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) 提供了一个没有烦人广告和可疑权限的YouTube体验。使用NewPipe，你可以订阅频道，后台听音乐，甚至下载视频以供离线观看。NewPipe可以通过F-Droid访问。
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) 是一个播客播放器，允许你订阅并管理所有喜爱的节目。AntennaPod可以通过F-Droid获取。

![image](assets/11.webp)

左侧：Spotube
右侧：ViMusic

### 地图

如果你在使用GrapheneOS的地图应用时想要语音辅助，你需要安装[RHVoice](https://rhvoice.org/installation/)并[配置](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available)它。

- [Magic Earth](https://www.magicearth.com/) 是一个支持逐转导航、3D和离线地图的地图替代品。Magic Earth可以从Aurora Store下载。
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) 是一个基于众包的OpenStreetMap数据的地图替代品，适用于旅行者、游客、徒步旅行者和骑行者。它是一个注重隐私的、开源的Maps.me应用分支（以前称为MapsWithMe），支持100%的功能无需活动的互联网连接，并且可以从F-Droid下载。
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) 是另一个出色的地图替代品，支持上述所有功能。

![image](assets/13.webp)

左侧：Magic Earth
右侧：Organic Maps

### 电子邮件

- [Proton Mail](https://proton.me/mail) 提供一个免费的私人电子邮件服务，支持经过审计的E2EE。Proton还提供支持自定义域名和[别名](https://proton.me/support/creating-aliases)的付费版本。Proton Mail可以作为直接APK或通过Aurora下载。
- [Tutanota](https://tutanota.com/) 提供与Proton Mail相同的功能，包括可选的付费服务，并且可以作为直接APK或通过F-Droid下载。
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) 是一个开源电子邮件客户端，几乎适用于每一个电子邮件提供商。它支持多个账户、统一收件箱和OpenPGP加密标准。

![image](assets/15.webp)

左侧：Proton Mail
右侧：Tutanota

### 生产力

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) 是一个文件同步程序。它实时同步两个或更多设备之间的文件，安全地保护免受窥探。你的数据仅属于你自己，你有权选择数据的存储位置、是否与第三方共享以及如何通过互联网传输。Syncthing可以通过F-Droid获取。
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) 允许您的所有设备在连接到家庭网络时轻松相互通信。轻松发送文件、照片、剪贴板数据到您的所有设备（甚至包括iOS设备！）。KDE Connect可以从F-Droid下载。
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) 是一个端到端加密的笔记应用，用于在您所有的设备之间同步您的想法和待办事项列表。他们的免费计划应该覆盖大多数个人使用场景。Notesnook可通过F-Droid获得。
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) 与Notesnook非常相似，但需要付费计划才能匹配其功能集。Standard Notes可以通过F-Droid下载。
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) 是一个键盘应用，允许您自定义几乎所有您能想到的与手机打字体验相关的事情。可以通过F-Droid下载。
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) 是默认的Google键盘应用。根据我的经验，它提供了迄今为止最好的打字和滑动体验。如果您下载了这个应用，请确保完全禁用所有网络相关权限。可以通过Aurora下载。

![image](assets/17.webp)

左侧：Notesnook
右侧：KDE Connect

### 生活方式

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) 是一个设计精美的开源天气应用，可通过F-Droid获得。它还支持许多不同大小的小部件，因此您可以直接从主屏幕查看您选择的位置的天气。
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) 是一个开源且保护隐私的翻译应用，支持200多种语言。Translate You可通过F-Droid下载。
- [Proton Calendar](https://proton.me/calendar/download) 是一个简单易用的端到端加密日历，与您的Proton电子邮件账户无缝交互。Proton Calendar可以作为APK下载或通过Aurora商店下载。
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) 是一个用于显示和存储登机牌、优惠券、电影票和会员卡等的应用。只需下载相关的`pkpass`或`espass`文件并用该应用打开。PassAndroid可通过F-Droid下载。

![image](assets/19.webp)
左侧：Geometric Weather
右侧：Proton Calendar

### 安全/隐私

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) 提供一个免费且端到端加密的跨平台密码管理解决方案，适用于您的所有设备。他们的付费服务允许您将2FA代码集成到应用中。Bitwarden的服务器端可以自托管，Android应用可通过F-Droid获得。
- [Proton Pass](https://proton.me/pass/download) 提供一个类似于Bitwarden的免费服务，但[Proton Unlimited](https://proton.me/pricing)客户能够访问额外的高级功能。Proton Pass可以通过APK或Aurora下载。
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) 是一个用于支持一次性密码协议系统的双因素认证应用。用户可以通过扫描二维码轻松添加令牌。FreeOTP 可通过 F-Droid 获取。
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) 是一个免费、安全且开源的 Android 应用，用于管理您在线服务的两步验证令牌。Aegis 可通过 F-Droid 获取。
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) 是一个付费的跨平台服务，它在本地加密您的数据，以便您可以安全地上传到您喜欢的云服务。Cryptomator 可通过 F-Droid 下载。

![image](assets/21.webp)
左侧：Proton Pass
右侧：Bitwarden

### 云解决方案

- [Proton Drive](https://proton.me/drive/download) 是一个付费的端到端加密（E2EE）云解决方案，用于备份和存储您的所有文件。在撰写本文时，他们刚刚宣布了一个 Windows 桌面客户端，但 Mac 和 Linux 用户必须继续使用网页版本从他们的计算机同步（暂时）。Android 客户端可以作为 APK 或通过 Aurora 获取。
- [Skiff](https://skiff.com/download) 也提供付费的端到端加密（E2EE）云存储和文件协作工具。他们提供 Mac 和 Windows 桌面客户端（以及一个网页应用），他们的 Android 客户端必须从 Aurora 下载。
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) 提供一个功能齐全的基于云的解决方案，用于协作、跨设备同步和文件存储。更高级的用户可以选择在他们喜欢的任何硬件上自行托管这个免费且开源的软件。Android 客户端可以通过 F-Droid 下载。
- [Cryptpad](https://cryptpad.fr/) 提供一个免费的、基于网页的、端到端加密的 Google Docs 替代品。

![image](assets/23.webp)

Proton Drive

## 缺点

开源和保护隐私的替代品比您习惯使用的科技巨头应用要多，而且有些通常比封闭源代码、充满间谍软件的替代品更好。

然而，当转移到 GrapheneOS 时，由于没有替代品，您必须放弃一些舒适的功能。这些包括：

- **Apple CarPlay/Android Auto** - 您需要坚持使用传统的蓝牙、USB 或 Aux。
- **Apple/Google Pay** - 几乎每个人无论如何都会随身携带他们的钱包！
- **银行应用** - 并不是说这些根本就不工作。有些实际上工作得很完美。其他一些只有在启用了 Google Play 服务时才工作（下面有更多说明），还有一些根本就不工作。在[这里](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/)阅读有关您银行的报告，以查看当前的状态。如果您的银行在不工作的列表上，不用担心，记住您可以将 URL 保存为主屏幕上的网页应用。
- **推送通知** - 大多数应用在您不使用特定应用时向您发送更新通知，都是通过 Google Play 服务完成的。这些服务默认不会与 GrapheneOS 一起安装，所以如果您发现自己在朋友发送电子邮件时没有立即收到通知，这可能就是原因。好消息是，上面提到的一些应用已经实现了自己的后台连接，以定期检查更新，然后在需要时给您发送通知。

### 沙盒化的 Google Play
GrapheneOS具有一个兼容性层，提供安装和使用Google Play官方发布版本的选项，这一切都在标准应用沙箱中进行。在GrapheneOS中，Google Play绝对不会获得任何特殊访问权限或特权，与绕过应用沙箱并获得大量高权限访问相反。

如果您发现自己实在离不开那些您最喜欢的应用的推送通知，或者某个“必须有”的应用没有Play服务就无法使用，GrapheneOS允许您在完全沙箱化的环境中[安装](https://grapheneos.org/usage#sandboxed-google-play-installation)这些服务。一旦安装，这些服务无需Google账户即可工作，每个服务的权限都可以严格控制。

在您急于在第一天就安装这些之前，我敦促您看看没有它们您能走多远。您可能会惊讶地发现，有多少应用在没有它们的情况下也能完美正常地工作。

如果您确实想安装它们，只需轻触预安装的“应用”应用程序，然后选择“Google Play服务”。考虑将它们与那些您离不开的不太私密的应用一起安装在一个完全独立的用户配置文件中，以提供与手机其余部分隔离的额外层次。

![image](assets/24.webp)

Play服务安装屏幕

### 配置文件

GrapheneOS允许您在手机内拥有独立的手机体验。额外的配置文件可以安装它们自己的应用和服务，并且不能访问所有者账户的任何文件或数据。
如果您只有一两个必须使用Play服务的应用，但非常少使用，那么在一个单独的配置文件中安装这些应用和Play服务可能是一个很好的主意，以进一步增强由于在所有者配置文件中运行它们而留下的任何微小的隐私影响。

您可以在[这里](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2)阅读更多关于这种用例的信息。

如果您决定添加一个适合您用例的单独配置文件，应用[Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/)可能对您有用。Insular允许您轻松地将任何现有应用克隆到新配置文件中，无需通过本指南早期介绍的任何传统安装路线。Insular还允许您快速“冻结”任何这些应用，完全禁用该应用的所有后台服务的运行。

![image](assets/24.webp)

用户配置文件管理屏幕

### e-SIM卡

如果您想将手机隐私提升到一个新的水平，并拥有一个与您的现实世界身份脱钩的蜂窝服务，eSIM卡可能适合您。eSIM卡是一种您可以在线购买并通过二维码添加到手机的虚拟SIM卡。提供这种服务的公司，可以使用比特币匿名支付，包括[Silent.Link](https://silent.link/)和[Bitrefill](https://www.bitrefill.com/gb/en/esims/)。

eSIM卡不应被视为手机隐私的完全解决方案。当在正确的手中使用时，它们可以是一个有用的工具，但如果您的目标是完全“离网”，请您研究使用任何类型的蜂窝服务的[权衡](https://grapheneos.org/faq#cellular-tracking)。

在GrapheneOS中，必须安装沙箱化的Play服务以进行eSIM卡配置。

## 备份
在完成新的去谷歌化Pixel手机设置之后，创建备份是个好主意。这个备份将使您能够在丢失手机或手机被盗/丢失的情况下，将手机恢复到相同的状态。

您可以选择将备份文件存储到任何外部存储媒介上，或者使用像Nextcloud这样的自托管云解决方案，尽管一些用户报告后一种选项的成功程度不同。

创建您的第一个备份：

1. 转到**设置** > **系统** > **备份**，然后记下您的12个单词恢复代码。此代码在以后的日期解密备份文件时是必需的。丢失代码，就丢失了访问手机备份的能力。
2. 接下来选择您的存储位置。我建议使用外部USB驱动器或工业级microSD卡。
3. 选择要备份的数据。如果您指定的存储介质上有足够的空间，我建议选择所有内容。
4. 点击右上角的三个点，并选择**立即备份**。

![image](assets/26.webp)

备份屏幕

记住，如果您正在向外部存储媒介进行离线备份，定期完成此步骤是有意义的，以确保如果发生最坏的情况，您的手机上任何最近的重要更新都不会丢失。

![video](https://www.youtube.com/embed/eyWmcItzisk)

详细说明备份过程的视频

## 结论

近年来，GrapheneOS软件已经显著成熟。它比以往任何时候都更稳定、更兼容。将此与蓬勃发展的开源和隐私保护应用生态系统结合起来，使GrapheneOS成为与原生Android或iOS相比，即使对于像您一样的“普通”人来说也是一个真正可行的替代方案！

数据泄露和大规模监控在当今世界如此普遍，以至于它们几乎不再成为头条新闻。保护自己的责任在于您。沿途将有调整和牺牲，但减少这种侵犯的暴露并不像您认为的那么困难。

我希望这个指南在某种程度上帮助您走上旅程。如果您发现这个指南有用，并希望支持我的工作，请考虑发送[捐赠](/tips)。

如果您是现有的GrapheneOS用户，或因本指南成为一个用户，请考虑[捐赠](https://grapheneos.org/donate)以支持他们的重要工作。

### 了解更多

GrapheneOS是一个任何人都可以轻松花费数周时间深入研究的领域。有这么多您可以学习和调整的东西，以便根据您的需求和威胁模型定制体验。以下是一些您可以继续您的旅程的链接：

- [GrapheneOS官方使用指南](https://grapheneos.org/usage) - 官方网站
- [GrapheneOS论坛](https://discuss.grapheneos.org/) - 官方网站
- [GrapheneOS设置大师班](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - 'The Privacy Wayfinder'的视频
- [GrapheneOS通用播客](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - 'Watchman Privacy'的播客

全部功劳归于：https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md