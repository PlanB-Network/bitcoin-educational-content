---
name: 佐林操作系统
description: 安装和使用 Zorin OS 作为 Windows 的现代替代品的完整指南
---

![cover](assets/cover.webp)



## 导言



操作系统（OS）是计算机运行的基本软件：它管理硬件、软件、安全和用户界面。


Zorin OS 是一个 Linux 发行版，专门用于简化从 Windows 的过渡，同时提供开源软件的优势：安全性、稳定性、隐私性和性能。



Zorin OS 基于 Ubuntu LTS，将软件的高兼容性与熟悉的可定制界面相结合，使其成为 Windows 的可靠、易用的替代品。



## 为什么选择 Zorin OS？





- 熟悉的 Interface**：类似 Windows 的外观（开始菜单、任务栏）
- 轻松过渡**：专为来自 Windows 的用户设计
- 增强安全性**：Linux 架构，病毒风险更低
- 尊重隐私**：不收集侵入性数据
- 优化性能**：在普通机器上运行良好
- Ubuntu LTS** 基础：稳定性、定期更新和广泛兼容性
- 高级个性化**：通过卓灵外观工具。



## 安装和配置



### 1.先决条件



**所需设备：**





- 至少 **8 GB**（建议 12 GB）的 USB 密钥；
- 至少有**25 GB 可用磁盘空间**的计算机
- 互联网连接（推荐）。



### 2.下载 Zorin OS





- 访问官方网站：[https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- 选择 **卓灵操作系统核心**（建议使用免费版本）



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- 下载 ISO 映像



Zorin OS 还提供 .NET Framework 3.0：





- Zorin OS Lite**（旧电脑）
- Zorin OS Pro**（收费，提供高级功能和支持）



## 创建可启动 USB 密钥



您可以使用多种工具，如 Balena Etcher ：





- 下载并安装 [Balena Etcher](https://etcher.balena.io/)。
- 打开 Balena Etcher，然后选择 Zorin ISO 映像。
- 选择 USB 密钥作为目标介质。
- 点击 Flash，等待进程结束。



![Utilisation de Balena Etcher](assets/fr/05.webp)



## 按键启动和 BIOS 访问



关闭要安装 Zorin OS 的计算机，然后插入 USB 密钥。


电脑启动后，进入 BIOS（"ESC"、"F9 "或 "F11"，视品牌而定），选择 USB 密钥作为启动设备，然后按 "Enter "键启动程序。





- 启动时，选择 ** 尝试或安装 Zorin OS**。



![capture](assets/fr/08.webp)





- 如果您使用英伟达™（NVIDIA®）显卡，请选择 **尝试或安装 Zorin OS（现代英伟达™（NVIDIA®）驱动程序）**。
- 检查文件时请稍候。



![capture](assets/fr/09.webp)





- 在 Zorin OS 安装程序中，选择语言**法语**，然后点击安装**Zorin OS**。



![capture](assets/fr/10.webp)





- 选择键盘布局。



![capture](assets/fr/11.webp)





- 选中 **在安装 Zorin OS 时下载更新** 和 **为图形和 Wi-Fi 硬件以及其他媒体格式安装第三方软件**。



![capture](assets/fr/12.webp)





- 要在整个磁盘上安装 Zorin OS：选择 **擦除磁盘并安装 Zorin OS**。



![capture](assets/fr/14.webp)



在安装 Windows 的同时安装 Zorin OS（双启动）：





- 选择 Windows 启动管理器旁边的**安装 Zorin OS**。



![capture](assets/fr/15.webp)





- 如果您尚未对磁盘进行分区，请选择要分配给 Zorin OS 的磁盘空间，然后点击 ** 立即安装**。



![capture](assets/fr/16.webp)





- 两次确认光盘上的更改。



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- 选择地理区域 **巴黎**。



![capture](assets/fr/18.webp)





- 创建用户账户并为电脑命名。



![capture](assets/fr/19.webp)





- 请等待 Zorin OS 安装。



![capture](assets/fr/20.webp)





- 安装完成后，点击 ** 立即重启**。



![capture](assets/fr/21.webp)





- 取出 USB 安装密钥，然后按 Enter。



![capture](assets/fr/22.webp)



## 发现并使用 Zorin OS



### 首次启动



启动电脑时，会进入 Linux 启动管理器 GRUB。默认情况下，**Zorin OS** 被选中；30 秒后，它会自动启动。



![capture](assets/fr/23.webp)



如果您将 Zorin OS 作为 Windows 的双启动程序安装，则可以通过选择 **Windows 启动管理器**启动到 Windows。



使用用户账户登录 ：



![capture](assets/fr/24.webp)



首次启动时，会启动**欢迎使用 Zorin OS** 应用程序，帮助您了解新操作系统。



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### 更新系统



更新管理器 "很快就会打开，通知您有更新可用。点击**立即安装**按钮即可安装。



![capture](assets/fr/33.webp)



您可以在 **Software** > 更新应用程序中手动检查更新：



![capture](assets/fr/34.webp)



### 个性化



使用 Zorin OS 的第一件事就是选择你最喜欢的**桌面布局。你会发现布局与 Windows 上的布局相似（专业版的布局更加相似）。



为此，请打开 **Zorin Appareance** > **Type** ：



![capture](assets/fr/35.webp)



然后打开**设置**，自定义系统：


**声音 - 设置 - Zorin OS



![capture](assets/fr/36.webp)



**在线账户 - 设置 - Zorin OS



![capture](assets/fr/37.webp)



### 应用



有几种安装应用程序的方法：





- Software** 是 Zorin OS 的应用程序商店。应用程序有多个来源：Apt、Flatpak 和 Snap。



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install（命令行） ：



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



有关在 Zorin OS 中安装应用程序的更多信息，请参阅此页：[安装应用程序 (zorin.com)](https://zorin.com/help/install-apps/)。



### Windows 应用程序



要安装 Windows 应用程序，首先要通过终端 .NET 安装**zorin-windows-app-support**软件包：



```bash
sudo apt install zorin-windows-app-support
```



有关兼容 Windows 应用程序及其兼容性级别的列表，请参阅 [Wine Application Database] 页面 (https://appdb.winehq.org/)。在那里，你可以找到以下与兼容性级别（从优到劣）相对应的徽章：白金徽章、黄金徽章、白银徽章、青铜徽章和垃圾徽章。



要安装 Windows .exe 或 .msi 应用程序，您有两种选择：





- 打开**PlayOnLinux**，点击**安装**按钮，浏览兼容的应用程序和游戏。



![capture](assets/fr/41.webp)





- 双击应用程序的 **.exe 或 .msi** 文件，让安装程序引导您进行安装。



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## 结论和其他资源



Zorin OS 是 Windows 的可靠、经济的替代品，集简单性、安全性和隐私性于一身。



它能使用户顺利过渡到 Linux，而不会牺牲舒适度或工作效率。



为了进一步保护您的数字生活，我们建议您使用隐私友好型服务，尤其是加密通信服务：



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2