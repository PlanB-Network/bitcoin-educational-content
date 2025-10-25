---
name: LineageOS
description: 免费、无缝的智能手机安卓操作系统
---

![cover](assets/cover.webp)



智能手机上预装的传统安卓系统存在许多众所周知的问题：谷歌服务的密集集成导致持续的数据跟踪、制造商强加的不受欢迎的赞助应用程序（膨胀软件），以及几年后放弃更新跟踪，使仍能正常运行的设备被程序淘汰。



LineageOS 为这些问题提供了一个优雅的答案。作为开源社区的产物和 CyanogenMod（2016 年底停产）的直接继承者，LineageOS 是一款基于 Android 的免费移动操作系统，让用户重新掌控自己的智能手机。该项目于 2016 年 12 月正式启动，目前在全球拥有超过 440 万个活跃安装，支持 20 多个不同品牌的数百种手机型号。



![lineageos-homepage](assets/fr/01.webp)



*介绍项目及其目标的 LineageOS 官方网站*



## 什么是 LineageOS？



### 理念和目标



LineageOS 是一个基于 Android 开源项目（AOSP）的开源移动操作系统，由全球众多志愿贡献者社区开发。它的非官方座右铭是 "你的设备，你的规则"：该项目旨在延长智能手机的使用寿命，同时提供精简、隐私友好的安卓体验。



该项目从 CyanogenMod 的废墟中崛起，而 CyanogenMod 是历史上最受欢迎的另类 Android ROM 之一。当 CyanogenMod 公司于 2016 年 12 月关闭时，社区动员起来创建了 LineageOS，保留了其前身的创新精神和开源理念。



与 OEM Android 发行版不同，LineageOS 默认不预装任何谷歌应用软件，完全消除了臃肿软件。用户只需从包含基本应用（电话、信息、相机、浏览器）的极简系统开始，然后自由选择后续添加的应用。



### 影响和社区



官方统计数据显示了该项目的规模：LineageOS 在 224 个国家/地区拥有超过 440 万活跃安装用户，是全球最广泛采用的 Android 替代软件之一。巴西的用户数量超过 200 万，紧随其后的是中国和美国，这表明免费、可定制的安卓系统具有普遍的吸引力。




## 主要特点



### Interface 和用户体验



**纯粹的安卓**：LineageOS 提供接近 AOSP 的纯正 Android 体验，没有制造商的叠加或多余的应用程序。Interface 仍然是安卓用户熟悉的系统，同时由于没有臃肿的软件而提供最佳的流畅性。



**默认不使用谷歌**：出于法律和道德原因，不预装谷歌服务。这种 "无谷歌 "方式保证了对个人数据的完全控制，并通过避免服务在后台运行来提高性能。



### 定制和安全



**高级定制**：LineageOS 解锁了许多 Android 系统无法提供的选项：导航按钮重新配置、可定制的系统主题、适应不同环境（工作、个人、游戏）的使用配置文件。



**Outil Trust**：集成功能可监控设备的安全状态，并对潜在威胁发出警报，提供系统安全的实时可见性。



**扩展更新**：LineageOS 社区致力于每月提供安全补丁，让被制造商停产的设备继续接收最新的安卓安全补丁。



## 兼容设备



LineageOS 支持来自 20 多家制造商的数百款设备：三星、小米、OnePlus、摩托罗拉、索尼、谷歌 Pixel、Fairphone 和其他许多厂商的设备。与石墨烯操作系统（GrapheneOS）等仅限于 Pixel 设备的替代方案相比，这种广泛的兼容性是该项目的主要优势之一。



![devices-compatibility](assets/fr/02.webp)



*LineageOS 兼容设备页面，可按制造商筛选设备*。



![google-devices](assets/fr/03.webp)



*支持谷歌设备，包括 Pixel 4（代号 "火焰"）*。



### 流行设备



根据官方统计，使用率最高的机型包括各种不同价位和机龄的设备，这表明 LineageOS 不仅能优化新机，还能为老款智能手机注入新的活力。



### 安装前的要点



**解锁启动加载器**：检查您的制造商/运营商是否允许解锁。一些品牌（如华为）在最近的机型上已经取消了这种可能性，而其他品牌则规定了特定的程序。



**精确型号**：下载与您的设备精确对应的 ROM 至关重要。两个商品名称相似的型号可能在技术上有所不同（例如 Galaxy S10 与 S10 5G），因此需要不同的镜像。



**可扩展支持**：较新的设备可能不会立即得到支持，因为移植工作需要一名志愿开发人员来负责。反之，如果某个设备的维护者退出了项目，则可能停止支持。



## 安装



### 必要的先决条件



⚠️ **开始使用前请仔细阅读这些说明**，以避免出现任何问题！



**返回固件（如有必要）：**




- 安卓闪存工具**：使用谷歌官方工具 [flash.android.com](https://flash.android.com)，通过网络浏览器（需要 Chrome/Edge 浏览器）轻松将 Pixel 设备还原为原版 Android 系统。
- 替代**：手动从 [developers.google.com/android/images](https://developers.google.com/android/images) 出厂图像



**强制性先决条件测试：**




- 使用原始系统启动设备至少一次**
- 测试所有功能**：短信、通话、Wi-Fi、移动数据
- 重要**：检查你是否可以发送/接收短信和拨打/接听电话（包括通过 WiFi 和 4G/5G）。如果在原版系统上无法使用，那么在 LineageOS 上也无法使用！
- 最新设备**：有些设备要求在原系统上至少使用一次 VoLTE/VoWiFi，以配置 IMS



**系统准备：**




- 删除设备中的所有谷歌**账户，以避免 "出厂重置保护"（可能会阻止激活）。
- 完全备份** ：此过程将完全删除您的手机。备份照片、联系人、应用程序和重要文件



**ADB 和 Fastboot 工具：** 按照 [LineageOS 官方指南](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) 安装 Android SDK 平台工具。使用 `adb version` 和 `fastboot --version` 验证安装。



**电话配置：**




- 激活 **开发者选项**：设置 > 关于 > 点击 "版本号 "7 次



![android-version](assets/fr/06.webp)



*导航至 "设置">"关于手机"，激活开发者模式*。





- 在 "开发人员 "选项中启用**USB 调试**
- 激活 **OEM解锁**（对解锁启动加载程序至关重要）



![developer-options](assets/fr/07.webp)



*启用开发人员选项、USB 调试和 OEM 解锁*。



### 详细安装



⚠️ **这些说明针对 LineageOS 22.2。请准确遵循每个步骤。如果出现故障，请勿继续！



#### 步骤 1：固件检查



**需要**固件：在继续之前，您的设备必须已安装 Android 13（适用于 Pixel 4）。固件是指股票系统中包含的特定设备图像。



![pixel4-info](assets/fr/04.webp)



*Pixel 4 官方页面，含下载链接和安装指南*。



![downloads-page](assets/fr/05.webp)



*LineageOS 构建版下载页面和文件*



**像素 4 专用下载：**




- 构建 LineageOS**：[download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- 所需文件**：从本页下载 3 个所需文件（这些文件将在以下步骤中使用）：
  - lineage-22.2-YYYYMMDD-nightly-flame-signed.zip`（主 ROM）
  - dtbo.img`（分区设备树 blob）
  - boot.img（恢复 LineageOS）



⚠️ **重要**：检查安卓版本，而不是制造商的操作系统版本。使用定制 ROM（即使是 LineageOS）并不能保证满足此要求。



💡 **提示**：如果对固件有疑问，请先返回原系统再继续！



#### 步骤 2：解锁启动加载程序



⚠️ **此步骤将删除所有数据！





- 测试 ADB 连接**：通过 USB 连接设备，并在电脑终端上使用 "adb devices "命令进行测试



![adb-devices](assets/fr/08.webp)



*使用 `adb devices`* 命令检查 ADB 连接





- 在手机上授权连接**



![usb-debugging-auth](assets/fr/09.webp)



*通过计算机的 RSA 指纹启用 USB 调试*。





- 启动到启动加载程序模式** ：


```
adb -d reboot bootloader
```


或按住 ** 音量减 + 电源** 设备关闭





- 检查 fastboot** 连接：


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*在终端中使用 Fastboot 命令检查连接情况 *



![bootloader-screen](assets/fr/11.webp)



*Pixel 4 的 fastboot 显示屏，包含系统信息*。





- 解锁启动加载器** ：


```
fastboot flashing unlock
```


在设备上使用音量键导航，然后按**电源**键选择 "解锁启动加载程序 "并确认操作



![unlock-bootloader](assets/fr/12.webp)



*确认设备上的启动加载程序已解锁*



⚠️ **确认解锁后，手机将自动重新启动**





- 自动重启**后，在开发人员选项中重新启用 USB 调试




#### 步骤 3：闪存其他分区



⚠️ **恢复正常工作所必需**





- 重启启动加载程序**：音量下+电源
- Flash**（将 `/path/to/`替换为下载文件的文件夹） ：


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*通过 fastboot* 闪存 dtbo 和 boot.img 分区



#### 步骤 4：安装 LineageOS 恢复软件





- 闪存恢复** （将 `/path/to/`替换为下载文件的文件夹） ：


```
fastboot flash boot /chemin/vers/boot.img
```




- 在恢复**中重新启动以检查



#### 步骤 5：安装 LineageOS





- 在恢复模式下重新启动**：音量下+电源→恢复模式



![recovery-mode](assets/fr/14.webp)



*Interface 从 LineageOS 恢复，带主菜单*。





- 出厂重置** ：键入 "出厂重置"→"格式化数据/出厂重置"。



![factory-reset](assets/fr/15.webp)



*LineageOS* 恢复系统中的工厂重置过程





- 返回主菜单**
- 侧载 LineageOS** ：
   - 在设备上："应用更新"→"从 ADB 应用
   - 在电脑上： `adb -d sideload /path/to/lineageos.zip`.



![apply-update](assets/fr/16.webp)



*在恢复*中选择 "应用更新"，然后选择 "从 ADB 应用



![sideload-process](assets/fr/17.webp)



*正在通过 Sideload* 安装 LineageOS



![sideload-terminal](assets/fr/18.webp)



*在终端中执行侧载命令，并显示安装进度*



💡 **正常**：进程可能会在 47% 时停止或显示 "成功 "错误 - 这是正常现象！



#### 步骤 6：首次启动





- 重新启动**："立即重启系统"
- 首次启动**：可能需要 15 分钟



🎉 **安装完成！**



### 注意事项



⚠️ **警告**：LineageOS 按 "原样 "提供，不提供担保。我们将尽一切努力确保一切正常运行，但安装风险由您自行承担！



**关键检查：**




- 固件兼容性**：请务必在型号下载页面上查看所需的固件版本
- 安装 LineageOS 后，切勿重新锁定**启动加载器
- 请按照设备的具体说明**操作



## 配置和应用



### 首次启动


精简的 Interface，接近安卓系统，无需谷歌。配置简单：语言、Wi-Fi，无需账户。



### 替代应用



**确保应用程序源的安全：**



**F-Droid**：基准开源应用软件商店，预装于 LineageOS for microG 或可直接下载。F-Droid 只提供经过验证和透明编译的开源软件，保证不含跟踪器或恶意组件。



**极光商店**：无需谷歌账户即可访问 Google Play 商店的匿名客户端。极光借用共享的匿名账户，让你在下载主流应用程序的同时保护自己的隐私。



**基本替代应用：**





- 导航**：有机地图（基于 OpenStreetMap 的离线地图）
- 通信**：Signal（端到端加密信息）、K-9 Mail（免费电子邮件客户端）
- 媒体**：NewPipe（无广告、无跟踪 YouTube）、VLC（通用媒体播放器）
- 生产力**：Nextcloud（自托管云）、Simple Calendar（CalDAV 同步）
- 安全性**：Bitwarden（密码管理器）、Aegis Authenticator（2FA 密码）



这些应用程序（其中大部分通过 F-Droid 提供）形成了一个连贯的生态系统，可以完全取代谷歌服务，同时提供现代化的功能性用户体验。



## 使用和维护



### 每日体验



LineageOS 改变了 Android 体验，将流畅性和响应速度放在首位。精简的 Interface 在旧设备上尤其有效，由于没有厚重的覆盖层和多余的进程，旧设备焕发了新的生机，性能普遍优于制造商的 ROM。



基本功能（通话、短信、照片、浏览）可无缝运行，而定制工具可使系统在不影响稳定性的情况下根据个人喜好进行微调。



### OTA 更新系统



LineageOS 拥有特别易用的空中下载更新系统。新版本会通过通知自动提出，安装只需点击几下，无需复杂的技术干预。这一过程完全保留了你已安装的数据和应用程序。



这些定期更新是一项重要的资产，尤其是对于已被制造商停产的设备而言，它们可以继续受益于最新的安卓安全补丁。



### 建议的最佳做法



**安装后的安全性：**




- 为解锁设置强大的 PIN 码或密码
- 检查是否已启用存储加密（通常为默认设置）
- 通过 F-Droid 安装 Bitwarden 等密码管理器



**预防性维护：**




- 定期 OTA 安全更新
- 限制在可信来源（F-Droid、极光商店）安装应用程序
- 定期审查授予应用程序的权限
- 偶尔重启可优化性能并释放内存



## 优势和局限性



✅ **福利：**




- 默认隐私（无谷歌跟踪）
- 广泛的兼容性（300 多种型号）
- 性能卓越（无臃肿软件）
- 旧设备的扩展更新



❌ **限制：**




- 技术安装
- 无安卓自动驾驶/谷歌支付功能
- 银行应用程序可能存在问题



## GrapheneOS vs LineageOS：有什么区别？



### 不同的方法



**GrapheneOS** 专注于最高安全性，仅在谷歌 Pixels 上运行，以利用其专用安全芯片。该系统采用了大量先进的漏洞缓解措施，并大大加强了应用程序沙箱功能。



**LineageOS** 在尽可能多的设备上兼顾了安全性、隐私性和便利性。这种方法更加务实，旨在扩展兼容性而非绝对安全。



### 管理 Google 服务



**GrapheneOS**：提供可选的沙盒 Google Play 系统。Google Play 可以安装，但在严格的沙盒中运行，没有特殊的系统权限。这种独特的方法使得在使用谷歌生态系统的同时，还能保持严格的安全控制。



**LineageOS**：允许用户选择安装谷歌服务（GApps）、microG（免费替代品）或完全不安装谷歌服务。最大限度地满足你的需求。



### 技术比较



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### 使用建议



**如果您拥有 Pixel，如果最高安全性是您的首要任务，如果您接受增强保护的限制，请选择 GrapheneOS**。



**如果你拥有非像素设备，正在寻求隐私与实用性之间的良好平衡，或希望自由选择与谷歌生态系统妥协的程度，请选择 LineageOS**。



## 结论



LineageOS 为重新掌控你的 Android 智能手机提供了一个成熟的选择。不粘连的体验、最佳的性能、广泛的兼容性：兼具私密性和日常实用性的理想选择。



## 资源



### 正式文件




- [LineageOS官方网站](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - 按机型分类的安装指南
- [适用于 microG 的 LineageOS](https://lineage.microg.org) - 集成 microG 的版本



### 社区




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon账号@LineageOS](https://fosstodon.org/@LineageOS)



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1