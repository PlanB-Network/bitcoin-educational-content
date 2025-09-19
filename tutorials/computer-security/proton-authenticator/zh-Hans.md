---
name: Proton Authenticator
description: 如何使用 Proton Authenticator 通过 2FA 确保账户安全？
---
![cover](assets/cover.webp)



双因素身份验证（2FA）为您的账户增加了一道额外的安全屏障，除密码外，还要求提供只有您才拥有密码的额外证明。启用 2FA，即使您的密码因网络钓鱼或数据泄漏而泄露，也能大大降低黑客攻击的风险。如果没有 2FA，攻击者只需要您的密码就能访问您的账户；而有了 2FA，他还需要您的第二个因素，从而挫败了大多数账户盗窃企图。



2FA 有多种类型。短信验证码聊胜于无，但仍然容易受到 SIM 卡交换攻击和拦截。我们不建议将 SMS 作为主要的 2FA。身份验证应用程序（TOTP）可在设备本地生成临时代码，使其更难被拦截。物理安全密钥具有最佳安全性，但需要专用硬件。



Proton Authenticator 是一款 TOTP 验证器。它是 Proton 对现有应用程序局限性的回应：许多应用程序都是专有的，包含广告跟踪器，并且不提供加密备份。Proton Authenticator 与众不同之处在于它是一款开源应用程序，不含广告和跟踪器，并提供端到端加密备份。



## 质子验证器介绍



Proton Authenticator 是由 Proton 开发的一款移动和桌面 TOTP 身份验证应用程序，该公司以提供注重隐私的服务而闻名。与所有 Proton 产品一样，该应用程序是开源的，并经过了独立的安全审核。它可在所有平台（Android、iOS、Windows、macOS、Linux）上免费使用。



Proton Authenticator 具有以下主要功能：





- 为 2FA 账户生成 **TOTP** 代码，与使用 Google Authenticator、Authy 等的大多数网站兼容。





- 可选加密云备份：您可以将应用程序链接到您的质子账户，以端到端加密方式备份和同步密码。如果您丢失了设备，只需重新连接一个新设备即可恢复所有密码。





- 多设备同步：在应用程序中登录 Proton，您的 2FA 密码就会通过端到端加密在多台设备之间自动同步。在 iOS 系统上，可通过 iCloud 进行同步。





- 通过密码或生物识别进行本地锁定：该应用程序提供密码和/或指纹/人脸识别锁定。因此，即使有人实际访问了您未上锁的手机，他们也无法打开 **Proton Authenticator**。





- **无数据收集或跟踪器**：质子承诺不通过应用程序收集任何个人数据。没有隐藏的广告或行为分析。





- 轻松导入/导出：Proton Authenticator 的强项之一是其现有账户导入向导，可与其他应用程序（Google Authenticator、Authy、Aegis 等）兼容。如果需要，您还可以将代码导出到文件中。



简而言之，Proton Authenticator 的目标是成为一个不折不扣的 2FA 解决方案：安全、私密、灵活。



## 安装



Proton Authenticator 可在所有平台上免费使用。要下载该应用程序，请访问官方网页：[https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*显示应用程序主要功能和 Interface* 的 Proton Authenticator 官方页面



在本页，您可以找到所有操作系统的下载链接：Android、iOS、Windows、macOS 和 Linux。只需点击您选择的操作系统，然后按照标准步骤进行安装即可。



在本教程中，我们将向你展示如何在 macOS 上安装和配置它，然后再看看如何在 iOS 上安装该应用，并在两台设备之间同步代码。



### 在 macOS 上安装



下载并安装应用程序后，启动 Proton Authenticator。首次启动时，应用程序会引导您通过几个初始配置屏幕：



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticator 欢迎屏幕，显示 "每一个代码都是安全的 "信息和 "开始使用 "* 按钮



### 首次进口



如果 Proton Authenticator 检测到您以前使用过其他 2FA 应用程序，则可能会出现一个导入向导。它支持从某些应用程序（Google Authenticator、2FAS、Authy、Aegis 等）直接导入。您也可以跳过这一步，稍后手动添加账户。



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*导入向导，用于从其他身份验证应用程序传输代码*。



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*兼容导入应用程序：2FAS、Aegis Authenticator、Authy、Bitwarden Authenticator、Ente Auth 和 Google Authenticator*



### 本地应用程序保护



设置解锁密码，或启用生物识别解锁（Touch ID）（如果可用）。这一步骤对于防止任何人使用你的 Mac 免费获取你的 2FA 密码至关重要。



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*带有 "保护您的数据 "信息和 "激活 Touch ID "*按钮的 Touch ID 配置屏幕



### 同步选项



该软件还可让你激活 iCloud 同步功能，在苹果设备之间安全备份数据。



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*带有 "使用加密的 iCloud 同步功能安全备份数据 "* 信息的 ICloud 同步选项



完成这些步骤后，Proton Authenticator 即可使用。



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*带有 "创建新代码 "和 "导入代码 "*选项的 Interface 主空质子验证器



## 使用 ProtonMail 添加 2FA 账户



现在我们以 ProtonMail 为例，看看如何添加第一个 2FA 验证码。这种方法适用于所有支持双因素身份验证的服务。



### 在 ProtonMail 上启用 2FA



首先，您可以查阅我们的 ProtonMail 指南，了解更多信息：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

登录 ProtonMail 账户，进入安全设置。查找 "双因素身份验证 "选项并将其激活。



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail 设置页面的 "双因素身份验证 "* 部分包含 "Authenticator 应用程序 "选项



点击按钮激活验证器，ProtonMail 会提示您选择验证应用程序。



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA 配置窗口，带 "取消 "和 "下一步 "* 按钮



然后，ProtonMail 会显示一个 QR 码，供您使用认证应用程序扫描。



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR 码，可使用您的身份验证应用程序扫描，并提供 "手动输入密钥 "选项*。



如果希望手动输入密钥，请单击 "代替手动输入密钥 "查看密钥。



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*手动输入 2FA 信息：密钥、间隔 (30) 和位数 (6)*



### 使用 Proton Authenticator 扫描 QR 码



在 MacOS 上的 Proton Authenticator 中，点击 "创建新代码"。应用程序会为您提供几个选项：**扫描二维码**或**手动输入密钥**。



使用 Mac 的摄像头扫描 ProtonMail 屏幕上显示的 QR 码。扫描二维码后，您将进入新代码配置界面。



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*新条目创建窗口，包含标题（ProtonMail）、密文、发件人（Proton）、数字参数和间隔字段*。



Proton Authenticator 会自动填写信息。您可以根据需要自定义名称，然后点击 "保存"。



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*为 ProtonMail (848 812) 生成 TOTP 代码并显示剩余时间*



### 验证配置



ProtonMail 会要求您输入由 Proton Authenticator 生成的 6 位数代码，以确认 2FA 工作正常。



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail 验证屏幕要求您输入 6 位数代码 (848812)*



从应用程序中复制代码（点击代码）并将其粘贴到 ProtonMail 中以完成激活。



通过验证后，ProtonMail 会要求您下载恢复密码。请务必小心保存。



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail 恢复代码屏幕，包含救援代码列表和 "下载 "* 按钮



### 紧急代码



添加账户时，请保留服务提供的恢复密码。大多数网站都提供静态、一次性使用的恢复密码，您可将其保存在安全的地方。将这些备份代码保存在 Proton Authenticator 之外，以便在您无法访问 2FA 应用程序时可以访问您的账户。



## IOS 安装和代码导入



既然你已经在 macOS 上设置了 Proton Authenticator，你可能还想在 iPhone 或 iPad 上使用它。下面介绍如何在多台设备上获取 2FA 密码。



### 下载 iOS 应用程序



进入 App Store，搜索 "Proton Authenticator"。在您的 iOS 设备上下载并安装该应用程序。



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*iOS 上的安装过程：欢迎屏幕、导入向导、选择兼容的应用程序，以及最后的 "从 Proton Authenticator 导入代码 "* 屏幕



### 方法 1：通过 JSON 文件导出/导入



如果不使用自动同步（iCloud 或 Proton 账户），则需要手动将代码从 Mac 传输到 iPhone：



**第 1 步 - 从 macOS 导出** ：



在 Mac 上打开 Proton Authenticator，进入 "设置"（齿轮图标）。在菜单中点击 "导出"。



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*MacOS 上的 Proton Authenticator 设置菜单，"导出 "选项可见*。



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*导出窗口的文件名为 "Proton_Authenticator_backup_2025"，并带有 "保存 "*按钮



在 Mac 上保存 JSON 文件。你可以通过安全电子邮件发送，或保存在 iCloud Drive 中，以便从 iPhone 访问。



**第 2 步 - 在 iOS 上导入** ：



在 iPhone 上安装 Proton Authenticator，在配置过程中选择导入代码。从列表中选择 "Proton Authenticator"，然后导入 JSON 文件。



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*iOS 上的导入流程：JSON 文件本地化、导入确认以及带有 Face ID 和 iCloud 选项的配置屏幕*。



### 方法 2：自动同步



**通过 Proton 账户（用于多平台同步）** ：



如果您尚未设置 Proton 账户，但希望在不同操作系统之间进行同步，应用程序会提示您创建或连接一个 Proton 账户。



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*设备同步屏幕要求您创建一个免费的 Proton 帐户或连接到现有帐户*。



**通过 iCloud（仅适用于苹果生态系统）** ：


如果您只使用苹果设备，可以在应用程序设置中选择 iCloud 同步。这种方法将在您所有的苹果设备之间自动安全地同步您的代码，而无需质子账户。



## 加密备份和恢复



Proton Authenticator 的主要功能之一是端到端备份 2FA 代码，确保设备丢失或更换后无需重新开始。



### 端到端加密



使用 Proton Authenticator 进行加密云备份时，您的 TOTP 秘密在发送到 Proton 服务器之前会在您的设备上进行本地加密。只有您自己才能在与您的Proton账户相连的设备上进行解密。Proton AG没有读取您注册密码的密钥。



在 iOS 系统上，如果您选择 iCloud 而不是质子账户，您的数据将按照苹果标准进行加密。在安卓系统上，本地备份可以用密码加密备份文件。



### 丢失时的修复



如果您的手机丢失、被盗或更换手机 ：



**启用 Proton 备份**：在新设备上安装 Proton Authenticator。在初始设置期间，登录同一个 Proton 账户。应用程序将立即同步并从加密备份中下载您的所有 2FA 密码。



**使用 iCloud 备份 (iOS)**：使用相同的 Apple ID 连接新的 iPhone/iPad，并确保激活 iCloud Keychain。安装傲腾验证器后，连接到 iCloud。您的密码应通过 iCloud 同步并显示出来。



**没有云备份**：您需要手动导入账户。如果您已导出备份文件，请使用 Proton Authenticator 的导入功能。在最坏的情况下，如果您没有备份，您需要使用每项服务的备份代码，或联系技术支持。



Proton Authenticator 允许您随时以加密文件或多账户 QR 码的形式导出账户。这些选项为您提供了更多保障。



## 最佳做法



使用 2FA 验证器可以大大提高安全性，但必须遵守某些最佳做法：



### 保存您的紧急代码



在激活 2FA 服务时，您通常会收到一份恢复密码列表。不要把它们放在手机上（纸上、加密密码管理器中等）。在验证器完全丢失的情况下，这些静态密码会救你一命。



### 不要混淆密码和 2FA 代码



使用同时存储 TOTP 的密码管理器很有诱惑力。但是，将密码和 2FA 代码放在同一个地方会造成单点故障，削弱双重验证功能。为了获得最大的安全性，许多专家建议将两个因素分开：密码放在安全的管理器中，2FA 代码放在 Proton Authenticator 等单独的应用程序中。不过，使用集成的管理器还是比没有 2FA 好。



### 激活多种 2FA 方法



理想情况下，在关键账户上使用一个以上的第二因素。如果服务允许，不要犹豫添加物理安全密钥。更多信息，请参阅我们的 Yubikey 物理密钥教程：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

同样，也要随身携带打印好的紧急代码。



### 保持低调，保护您的设备



不要让任何人搜索您的解锁手机。使用 Proton Authenticator，您的密码受 PIN 码/生物识别码保护--不要泄露这个 PIN 码。同样，要谨防网络钓鱼：即使使用了 2FA，如果您实时向欺诈网站提供密码，也可能被攻击者利用。



### 更新和审计



不断更新 Proton Authenticator（更新可纠正可能存在的缺陷）。由于代码是开放的，社区会进行非正式审核，Proton 会公布正式审核的结果。



## 与其他应用软件的比较



Proton Authenticator 与其他身份验证应用程序相比如何？以下是比较摘要：



**质子验证器**：开源、可选 E2EE 加密云备份、多设备同步、本地锁定、无跟踪，可用于手机和桌面。



**谷歌验证器**：专有，自 2023 年起通过谷歌账户备份，但没有端到端加密（谷歌可以看到密钥），2023 年增加了多设备同步功能，默认情况下没有应用锁，包含谷歌跟踪器。



**Aegis Authenticator**：开源，仅本地备份，无云端同步，密码/生物识别锁，无跟踪，仅限安卓系统。



**默认**：专有、密码加密云备份但代码封闭、多设备同步、PIN 锁/指纹、收集电话号码、2024 年 3 月停用桌面应用程序。



下面是我们的 Authy 指南：



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator 是目前最全面、最安全的解决方案之一：开源、多设备加密同步、无商业后续服务。



## 资源和支持



### 正式文件




- 官方网站：[proton.me/authenticator](https://proton.me/authenticator) - 产品介绍和下载
- 下载页面：[proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - 适用于所有操作系统的链接
- Proton 支持：[proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - 官方 2FA 激活指南
- 质子博客：[proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - 公告和详细功能



### 源代码和透明度




- **GitHub Proton Authenticator**：[github.com/ProtonMail/protonauthenticator](https://github.com/ProtonMail/proton-authenticator) - 开源代码
- 安全审计：[proton.me/community/security-audits](https://proton.me/community/security-audits) - 独立审计报告



### 建议的安全测试


配置完成后，测试您的设置：




- [Have I Been Pwned](https://haveibeenpwned.com/) - 检查您的账户是否已被入侵
- [2FA Directory](https://2fa.directory/) - 支持 2FA 的服务列表



### 社区和讨论




- Reddit r/Proton：[reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - 官方质子社区
- **隐私指南论坛**：[discuss.privacyguides.net](https://discuss.privacyguides.net) - 有关隐私问题的技术讨论
- Reddit r/privacy：[reddit.com/r/privacy](https://reddit.com/r/privacy) - 一般隐私提示



### 其他




- [Have I Been Pwned](https://haveibeenpwned.com/) - 检查您的账户是否已被入侵
- [2FA Directory](https://2fa.directory/) - 支持 2FA 的服务列表