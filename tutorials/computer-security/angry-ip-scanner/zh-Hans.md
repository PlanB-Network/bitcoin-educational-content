---
name: Angry IP Scanner
description: 扫描网络的简单方法
---
![cover](assets/cover.webp)



___



*本教程基于 Florian BURNEL 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。*



___



## I.介绍



如何快速轻松地扫描 Windows 网络中的联网机器？答案就是 Angry IP Scanner。这个开源项目可让你使用简单易用的图形 Interface 轻松扫描网络。



个人可以使用该工具**扫描自己的本地网络，IT 专业人员也可以出于同样目的使用该工具。一些网络犯罪团伙**已使用该工具扫描企业网络（与 Nmap 的扫描方式相同），这证明**该工具非常实用**。一个很好的例子就是 [勒索软件组织 RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/)。它仍然是一款不错的软件，但与其他网络和安全导向型工具一样，它也可能被滥用。



在这里，我们将在**Windows 11**上使用它，但也完全可以在其他版本的**Windows**以及**Linux**和**macOS**上使用它。



与 Nmap 相比，**Angry IP** Scanner 的全面性要差一些，但对于快速、基本的网络分析来说，它仍然很有趣，而且因为它触手可及。它可以**检测连接到网络的主机**，并识别**主机名**和**打开的端口**。



如果您想进一步了解，请参阅 Nmap 教程 ：



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II.开始使用 Angry IP 扫描仪



### A.下载并安装 Angry IP Scanner



你可以从应用程序的官方网站或 GitHub 下载最新版本的 Angry IP Scanner。我们将使用后一种方式。点击下面的链接，下载 EXE 版本："**ipscan-3.9.1-setup.exe**".





- [愤怒的 IP 扫描仪 GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



运行可执行文件继续安装。安装过程中没有任何特殊操作。



![Image](assets/fr/013.webp)



### B.运行初始网络扫描



首次启动时，请花点时间阅读 "**开始使用**"窗口中的说明，进一步了解该工具的工作原理。顺便提一下，有几个术语需要注意：





- **Feeder**：负责从随机 IP 范围或 IP 地址列表文件中生成要扫描的 IP 地址列表的模块。
- **获取器**：一组用于获取网络上主机信息的模块。例如，有用于检测 MAC 地址、扫描端口、检测主机名或发送 HTTP 请求的获取器。



![Image](assets/fr/018.webp)



要扫描 IP 子网，只需在 "**IP 范围**"字段中输入**起始 IP Address** 和**终止 IP Address**（否则，请在右侧更改类型）。然后点击 "**开始**"按钮。



![Image](assets/fr/019.webp)



几十秒后，结果就会出现在软件的 Interface 中。 **对于分析范围内的每个 IP Address，你将看到 Angry IP 扫描仪是否检测到主机。** 屏幕上还会显示摘要，说明活动主机的数量（本例中为 6 台）和端口开放的主机数量。



![Image](assets/fr/020.webp)



在这里，我们可以看到一台名为 "**OPNsense.local.domain**"的主机，它与 IP Address "**192.168.10.1**"相关联，可通过**端口 80** 和 **443**（HTTP 和 HTTPS）访问。右键单击主机可使用其他命令，如 ping、跟踪路由和通过该 IP Address 打开浏览器。



![Image](assets/fr/012.webp)



### C.添加扫描端口



默认情况下，**Angry IP Scanner** 将扫描 3 个端口： **80**（HTTP）、**443**（HTTPS）和**8080**。您可以在应用程序首选项中添加要扫描的更多端口。点击 "**工具**"菜单，然后点击 "**端口**"选项卡。



在这里，您可以通过 "**端口选择**"选项修改端口列表。您可以**以逗号分隔的特定端口号，也可以**端口范围。下面的示例添加了两个端口： **445**（SMB）和**389**（LDAP）。要扫描 1 到 1000 的端口，请输入 "**1-1000**"。未指定端口扫描是在 TCP、UDP 还是两者中进行。



![Image](assets/fr/021.webp)



如果您再次运行扫描，很可能会得到新的信息。在下面的例子中，Angry IP Scanner 告诉我，由于新配置了要扫描的端口，主机 "**SRV-ADS-01**"和 "**SRV-ADS-02**"上的 389 和 445 端口是开放的。



![Image](assets/fr/022.webp)



**注**：从 "**扫描仪**"菜单，您可以将扫描结果导出到文本文件。



如果您希望进一步扫描，请点击 "**工具**"菜单，然后点击 "**撷取器**"。这将为扫描增加 "功能"。只需选择一个取样器并向左移动即可激活它。这将在扫描结果中增加一列。



![Image](assets/fr/014.webp)



下面的示例显示了 "**网络BIOS 信息**"和 "**网络检测**"功能。前者提供附加信息，如机器的 MAC Address 和域名，后者则显示网页标题（可显示网络服务器或应用程序的类型）。



![Image](assets/fr/011.webp)



最后，您还可以在首选项中更改 "**ping**"所用的方法，即考虑主机是否处于活动状态。由于有些主机不响应 ping，因此可以尝试其他方法（UDP 数据包、TCP 端口探测、ARP、UDP + TCP 组合等）。



## III.结论



简单有效：Angry IP Scanner 可检测连接到网络的主机，并允许你配置端口扫描。就选项而言，它不如 Nmap 灵活，也没有 Nmap 走得远，但它是快速扫描的良好开端。



如果您想在图形 Interface 中使用**Nmap**，可以使用**Zenmap 应用程序**（见下文概述）。



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d