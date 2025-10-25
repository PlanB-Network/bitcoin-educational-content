---
name: Ente Auth
description: 开源端到端加密 2FA 验证器
---
![cover](assets/cover.webp)



双因素身份验证（2FA）已成为确保在线账户安全不可或缺的工具。除了常用密码外，它还需要一个临时代码，通常由专用应用程序生成。这种机制被称为 TOTP（基于时间的一次性密码），它可以保证即使您的密码被泄露，攻击者也无法在不拥有第二个因素的情况下访问您的账户，而第二个因素每 30 秒更新一次。



然而，选择合适的身份验证应用程序并非易事。Google Authenticator 虽然很受欢迎，但有很大的局限性：专有代码无法审计、没有端到端加密的同步，以及在手机出现问题时代码丢失的风险。其他解决方案，如 Authy，需要电话号码，不能保证完全保密。



**Ente Auth** 作为一种现代、安全的选择脱颖而出。这款免费、开源、跨平台的应用程序由[Ente Photos](https://ente.io)团队开发，提供端到端加密云备份和所有设备之间的无缝同步。与专有解决方案不同的是，Ente Auth 可让您完全控制自己的验证码，而不会损害您的隐私。



在本教程中，我们将逐步向您介绍如何安装和使用 Ente Auth，以及该解决方案与传统身份验证器不同的原因。



## Ente Auth 简介



Ente Auth 由 Ente Photos（端到端加密和隐私友好型照片存储服务）背后的团队开发。Ente Auth 秉承 Ente 的理念（"Ente "在马拉雅拉姆语中意为 "我的"，象征着对数据的控制），旨在让用户重新获得对其双因素验证码的完全控制权。



### 主要特点



**标准 TOTP 代码**：Ente Auth 生成的临时代码与大多数服务（GitHub、Google、Binance、ProtonMail 等）兼容。您可以根据需要添加多个 2FA 账户，应用程序会根据您提供的秘密计算代码。



**端到端加密云备份**：您的密码安全地在线存储。只有您自己才能解密--加密密钥来自您的密码，只有您自己知道。Ente（服务器）不知道您的秘密，甚至不知道您的账户名称，因为所有内容都是在客户端使用零知识架构加密的。



**多设备同步**：您可以在多台设备（智能手机、平板电脑、电脑）上安装 Ente Auth，并在所有设备上访问您的密码。任何更改都会通过加密云自动即时传播到您的其他设备，为您的日常工作提供极大的灵活性。



**极简、直观的 Interface**：该应用程序提供精简的 Interface，即使非技术用户也能轻松学会。2FA 账户显示服务名称、登录名和 6 位密码，并实时更新。Ente Auth 还会提前几秒钟显示下一个密码，以避免因过期而无法使用。



**开源并经过审核**：Ente Auth 的源代码在 AGPL v3.0 许可下 [GitHub 上公开](https://github.com/ente-io/auth)。任何开发人员都可以对其进行审核，检查是否存在缺陷或不良行为。实施的加密技术已经过[独立外部审计](https://ente.io/blog/cryptography-audit/)，这是应用程序安全性的保证。



### 优势和局限性



**福利：**




- 通过端到端加密设计实现隐私保护
- 在所有设备之间安全同步
- 可审计的开放源代码
- Interface 清晰、直观的用户界面 Interface
- 自动备份，防止代码丢失
- 适用于所有平台（手机和台式机）



**限制：**




- 同步需要互联网连接
- 高级用户可能更喜欢 100% 离线解决方案，如 Aegis（仅限安卓系统）
- 与成熟的解决方案相比相对较新



## 安装



Ente Auth 适用于大多数流行平台。您可以从 [官方网站](https://ente.io/auth) 或官方商店下载应用程序。



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth 下载页面，包含所有可用平台*。



### 安卓


您有几种选择：




- Google Play 商店：搜索 "Ente Auth"，进行经典安装
- **F-Droid**：可从安卓开源应用程序目录中获取，保证结构经过验证，无专有内容
- **手动安装**：APK 文件可从[项目的 GitHub 页面](https://github.com/ente-io/auth/releases)下载，并集成了新版本通知功能



### iOS（iPhone/iPad）


通过搜索应用程序名称，直接从苹果应用程序商店安装 Ente Auth。iOS 应用程序也可通过 Mac App Store 在装有 Apple Silicon 芯片（M1/M2）的 Mac 上运行。



### 计算机（Windows、macOS、Linux）


Ente Auth 提供本地桌面应用程序。请访问 [ente.io/download](https://ente.io/download) 或 [GitHub Releases section](https://github.com/ente-io/auth/releases) ：





- 视窗：提供 EXE 安装程序
- **macOS**：在应用程序中拖放 DMG 磁盘映像
- **Linux**：提供多种格式（AppImage 便携版、.deb 用于 Debian/Ubuntu、.rpm 用于 Fedora/Red Hat）



**注：** 本教程基于 Ente Auth v4.4.4 及更高版本。早期版本可能与 Interface 有细微差别。



### Interface 网络


无需安装，您可以从任何浏览器通过 [auth.ente.io](https://auth.ente.io)访问您的代码。Interface 网络版仅限于查看代码（用于故障排除），因为出于安全原因，添加账户需要使用手机或桌面应用程序。



## 首次配置



### 创建账户



首次启动 Ente Auth 时，您有两个选项：



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*带有账户创建选项的 Ente Auth 主页屏幕*。



**有账户（推荐）**：选择 "创建账户"，然后输入您的电子邮件 Address 和密码。 **重要**：该密码是加密数据的主密码。选择一个强大、唯一的密码，因为没有不丢失数据的常规重置程序。如果您丢失了密码，您的加密数据将无法恢复。



**离线模式**：选择 "无备份使用 "可在本地使用应用程序，无需云。在此模式下，您的代码会保留在设备上，但需要手动导出以避免丢失。



![Vérification email et récupération de clé](assets/fr/03.webp)



*电子邮件验证过程和生成 24 个字符的恢复密钥*。



可能需要电子邮件验证，以确认账户创建并在新设备上进行恢复。Ente Auth 还将为您提供一个 24 个字符的恢复密钥（基于 BIP39 方法）。 **请务必将此密钥**保存在安全的地方：这是您在忘记密码时恢复数据的唯一方法。



### 当地安全



我强烈建议启用密码或生物识别的本地保护。进入 **设置 → 安全性 → 锁屏**，然后配置.NET Framework 3.0：





- 生物识别解锁：面部 ID、指纹，视设备功能而定
- 特定于应用程序的 **PIN/密码**
- 自动锁定延迟：例如 "立即" 或 30 秒未活动后



这种保护可以防止有人在未经授权的情况下访问您的密码，如果有人获得了您的解锁手机。请注意，此锁只是一个额外的屏障：即使没有此保护，您的数据仍然是端到端加密的。



## 添加 2FA 账户



### 标准程序



要添加新的 2FA 账户，让我们以在公牛 Bitcoin 上激活 2FA 为具体例子：



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auth 的主 Interface 准备添加第一个 2FA* 账户



**服务端 (Bull Bitcoin)**：登录您的公牛 Bitcoin 账户，进入安全设置并启用双因素身份验证。



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* 安全设置菜单



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*在 Bull Bitcoin* 上启用双因素身份验证的选项



然后，该服务会显示一个 QR 码，供您使用身份验证应用程序扫描：



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Bull Bitcoin 生成的 QR 代码，可使用您的验证器扫描*。



**在 Ente Auth**：点击 "输入设置密钥"，然后扫描 Bull Bitcoin 显示的二维码。Ente Auth 将自动识别账户并填写字段。



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*在 Ente Auth* 中配置 Bull Bitcoin 账户详情



您可以自定义服务名称和登录名，以方便查找。默认情况下，高级设置（SHA1 算法、30 秒周期、6 位数字）一般都是正确的。



**服务端验证**：返回 Bull Bitcoin，输入 Ente Auth 生成的 6 位数代码，完成激活。



![Saisie du code 2FA](assets/fr/09.webp)



*输入 Ente Auth 生成的验证 2FA* 激活的代码



![2FA activée](assets/fr/10.webp)



*确认公牛 Bitcoin* 上的 2FA 激活成功



**备份代码**：Bull Bitcoin 将为您提供恢复密码。**将它们保存在安全的地方，与您的验证器分开。**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*公牛 Bitcoin* 上的 generate 紧急备用代码选项



![Codes de récupération](assets/fr/12.webp)



*要妥善保存的恢复密码清单*



### 组织和管理



Ente Auth 具有多项实用功能：



**快速复制**：按下代码可将其自动复制到剪贴板。



**对上下文敏感的操作**：长按（或右键单击桌面）可编辑、删除、共享或固定条目。



**标签和搜索**：使用标签（个人/专业、服务类别）整理您的账户，并使用搜索栏快速筛选。



![Création d'un tag](assets/fr/17.webp)



*标签创建过程：上下文菜单和创建对话框*。



![Tag appliqué](assets/fr/18.webp)



*标签 "Bitcoin "成功应用于公牛 Bitcoin* 账户



**自动图标**：由于集成了 [Simple Icons] 图标包 (https://simpleicons.org/)，每个条目都可以用服务徽标进行说明。



**临时安全共享**：安全共享是 Ente Auth 的一项独特功能，可让您在不泄露基本秘密的情况下向同事发送 2FA 验证码。generate 加密链接的有效期最长为 2、5 或 10 分钟，接收者可实时看到验证码，但无法导出或访问账户数据。这种方法是技术援助或临时协作的理想选择，提供了简单截图或短信无法达到的安全级别。



![Partage sécurisé](assets/fr/19.webp)



*Interface 临时安全共享：选择持续时间（5 分钟）*



**安全导出/导入**：Ente Auth 可让您将代码导出到其他应用程序，或从 Google Authenticator 和其他解决方案导入代码。可通过加密文件或 QR 码导出，确保数据的可移植性，同时不影响安全性。



**BIP39 恢复密钥**：应用程序根据 BIP39（Bitcoin Improvement Proposal，Bitcoin 改进提案）标准自动生成一个 24 个字符的恢复短语，与加密货币钱包相同。该短语是您的终极恢复密钥，即使您忘记了主密码，也能恢复所有密码。



## 配置和设置



Ente Auth 提供大量自定义选项，可通过应用程序设置进行访问：



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Ente Auth*可用参数概览



### 账户和数据管理



![Paramètres de sécurité](assets/fr/14.webp)



*高级安全选项：电子邮件验证、PIN 码、活动会话*。



安全设置允许您 ：




- 启用新连接的电子邮件验证
- 激活密码匙
- 查看各种设备上的活动会话
- 设置 PIN 码或生物识别技术



### Interface 和使用选项



![Paramètres généraux](assets/fr/15.webp)



*Interface 参数和应用定制*



一般设置包括 ：




- 语言：Interface 多语种
- 显示：大图标，紧凑模式
- 隐私**：隐藏代码、快速搜索

The line appears to have an unbalanced ** marker. Here's the corrected version:

- **隐私**：隐藏代码、快速搜索
- 遥测**：错误报告（可禁用）

The line is already correctly formatted. The ** markers are balanced (one opening ** and one closing **), making "遥测" bold as intended.



## 备份和同步



### 加密的工作原理



当您使用已连接的 Ente 账户添加账户时，应用程序会立即使用您的主密钥（源自您的密码）对这些敏感数据进行本地加密。加密后的数据将发送到 Ente 服务器进行存储。



有了这一机制，您的密码可随时获得端到端加密云备份。如果您丢失了设备，只需重新安装 Ente Auth 并重新连接：应用程序将自动下载并解密您的所有密码。



### 多设备同步



如果您在智能手机和电脑上都使用 Ente Auth，那么其中一台设备上的任何添加或更改都会在几秒钟内出现在另一台设备上。这种同步通过 Ente 的云进行，但由于数据是端到端加密的，服务器只能看到不可读的加密内容。



![Synchronisation mobile](assets/fr/16.webp)



*同步演示：可在移动端和桌面端访问同一个 Bull Bitcoin 账户*。



无缝同步：在智能手机上安装 Ente Auth，使用您的凭据登录，您的所有 2FA 代码（此处为 Bull Bitcoin）都会自动出现。上面的示例显示了台式机和手机之间的完美同步--两台设备上都可以访问同一个 Bull Bitcoin 码。



在保密性方面，Ente 或任何第三方都无法访问您的 2FA 秘密。即使是元数据（标签、备注、服务名称），在发送之前也会进行加密。这种零知识架构确保只有您才能破译您的密码。



### 离线使用



同步需要互联网，但由于所有数据都存储在本地，Ente Auth 可在每台设备上完美地离线运行。一旦恢复连接，离线更改就会排队并同步。



## 安全和隐私



### 加密保证



Ente Auth 基于强大的端到端加密和零知识架构。您的密码由您单独持有的密钥加密，该密钥通过先进的密钥推导功能从您的主密码中推导出来。



**零知识架构：Ente 无法实际访问您的数据。即使是元数据（服务名称、标签、备注），也会在传输前在客户端加密。这种方法可确保在您的服务器受到攻击或政府提出要求时，Ente 只能披露没有您的密码就无法读取的加密数据。**



**本地加密**：加密过程完全在您的设备上进行，然后再发送到云端。Ente 服务器只接收和存储加密数据，即使服务管理员也无法进行未经授权的访问。



### 透明度和审计



由于代码是[开放源代码](https://github.com/ente-io/auth)，社区可验证不存在后门。Ente 已经进行了[多次外部审计](https://ente.io/blog/cryptography-audit/)，以验证其实施的安全性：





- **Cure53**（德国）：应用程序和密码安全审计
- 符号软件公司**（法国）**：专业密码技术
- **Fallible**（印度）：渗透测试和漏洞分析



这些由公认公司进行的独立审计保证 Ente Auth 的加密实施符合最佳安全实践，没有重大缺陷。



### 隐私政策



Ente Auth 采用[典范隐私政策](https://ente.io/privacy/)，以尽量减少数据收集为基础。只保留服务运行所严格必需的信息：您的电子邮件 Address，用于身份验证和账户恢复。



**无跟踪或遥测**：与大多数应用程序不同，Ente Auth 不收集使用指标、碰撞识别数据和行为信息。应用程序在运行过程中不会出现干扰性广告或分析跟踪器。



**GDPR 合规**：Ente 完全遵守《欧洲通用数据保护条例》。您有权随时访问、更正或删除您的数据。只需点击[数据导出](https://ente.io/take-control/)，即可永久删除您的账户，并从服务器上删除您的所有数据。



**分散、安全的存储**：您的加密数据在 3 个不同国家的 3 个不同提供商处复制，保证最佳可用性，同时避免对单一云提供商的依赖。



Ente 的商业模式以付费的 Ente Photos 服务为基础，这使我们能够免费、无限制地**提供 Ente Auth 服务**，而不会通过将您的数据货币化来损害您的隐私。这种方式保证了服务的可持续性，而无需依赖广告或转售个人数据。



## 与其他解决方案的比较



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth 是为数不多的兼具源代码透明、加密云备份和跨平台同步等所有优势的解决方案之一。



## 推荐使用案例



### 个人用户



Ente Auth 非常适合有安全意识的人系统地激活 2FA。您不必再担心更换手机时丢失密码，也不必在便利性和安全性之间做出选择。



### 家庭和多设备使用



如果您使用多台设备，这款应用程序就会发挥它的作用。您可以在智能手机和平板电脑上保存代码，或同步安全地共享某些家庭代码（Netflix、家庭云）。



### 专业用途



对于管理敏感账户的团队而言，Ente Auth 通过集成在 "组织和管理 "部分的高级共享功能，在确保安全的同时促进了协作。



## 最佳做法





- 保存您的紧急代码：将各项服务提供的恢复密码与手机分开保存。





- 使用强大的主密码：您的 Ente Auth 主密码必须唯一且强大，因为它可以保护您的所有代码。





- 激活本地保护：配置 PIN 码或生物识别技术，防止未经授权的物理访问。





- 不要过度定制：避免高级修改，以免影响同步。





- 保持应用程序更新：更新可纠正安全漏洞并改进功能。





- 测试恢复：偶尔检查是否可以在其他设备上还原代码。



## 结论



Ente Auth 是双因素身份验证的现代化综合解决方案。这款开源应用程序集安全性、透明度和易用性于一身，既能满足高要求用户的需求，又不失便利性。



与将您锁定在不透明生态系统中的专有解决方案不同，Ente Auth 让您重新掌控身份验证数据，同时通过加密备份防止意外丢失。



无论您是希望保护个人账户安全的个人，还是管理企业访问的团队，Ente Auth 都是您在不损害隐私的前提下实现数字安全现代化的明智选择。



## 资源和支持



### 正式文件




- 官方网站：[ente.io/auth](https://ente.io/auth)
- 帮助中心：[help.ente.io/auth](https://help.ente.io/auth)
- 技术博客：[ente.io/blog](https://ente.io/blog)



### 源代码和透明度




- **GitHub**：[github.com/ente-io/auth](https://github.com/ente-io/auth)
- **密码学审计**：[ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### 社区




- **Discord**：[discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**：[r/enteio](https://reddit.com/r/enteio)