---
name: OPNsense
description: 如何安装和配置 OPNsense 防火墙？
---
![cover](assets/cover.webp)



___



*本教程基于 Florian BURNEL 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。



___



## I.介绍



在本教程中，我们将介绍 OPNsense 开源防火墙。我们将了解它的主要功能、先决条件以及如何安装这个基于 FreeBSD 的解决方案。



在开始之前，你应该知道**OPNsense和pfSense都是基于FreeBSD的开源防火墙。我们可以说，pfSense算是OPNsense的老大哥，因为后者是2015年创建的Fork。最后，需要指出的是，自 2017 年起，**OPNsense 已改用 HardenedBSD 而非 FreeBSD**。HardenedBSD 是 FreeBSD 的增强版本，具有高级安全功能



OPNsense 因其更现代化的用户界面（Interface）和**更频繁的更新频率而脱颖而出。事实上，OPNsense的更新计划包括每年发布两个主要版本，每两周左右更新一次（导致发布次要版本）。如果我们看一下这些解决方案的社区版本，就会发现与pfSense相比，OPNsense的后续行动非常有趣。



![Image](assets/fr/050.webp)



## II.OPNsense 的特点



OPNsense 是一种操作系统，旨在充当防火墙和路由器，但其功能众多，可通过安装附加软件包进行扩展。它适用于生产，主要用于网络安全和流量管理。



### A.主要特点



以下是 OPNsense 的一些主要功能：





- 防火墙和 NAT**：OPNsense 提供先进的状态防火墙功能，具有状态过滤和网络 Address 转换（NAT）功能。





- DNS/DHCP**：可将 OPNsense 配置为管理网络上的 DNS 和 DHCP 服务。它可以充当 DHCP 服务器，也可以用作本地网络上机器的 DNS 解析器。默认情况下还集成了 Dnsmasq。





- VPN**：OPNsense支持多种VPN协议，包括IPsec、OpenVPN和WireGuard，可实现远程访问移动工作站或站点互连的安全连接。





- 网络代理服务器**：OPNsense 包括一个网络代理服务器，用于控制和过滤互联网访问。它还可用于过滤内容和管理网络访问。





- 带宽管理（QoS）**：OPNsense 提供服务质量（QoS）管理功能，可对网络流量进行优先排序，更好地管理网络带宽。





- 专属门户**：该功能可让您通过认证页面（本地基地、凭证等）管理用户对网络的访问。这是公共 Wi-Fi 网络常用的一项功能。





- IDS/IPS**：OPNsense集成了Suricata，提供入侵检测和防御（IDS/IPS）功能，保护网络免受攻击。





- 高可用性（CARP）**：OPNsense支持CARP（*通用Address冗余协议*），以实现多个OPNsense防火墙之间的高可用性，确保即使在硬件故障的情况下，服务也能保持激活状态。





- 报告和监控**：OPNsense 提供实时报告和监控工具，以跟踪网络性能（使用 NetFlow），并通过创建日志发现潜在问题。其中包括图形。Monit 工具已集成到 OPNsense 中，可对防火墙本身进行监控。



### B.附加套餐



这只是 OPNsense 提供的功能概览。此外，通过 OPNsense 管理 Interface 中的**软件包目录**，您还可以**附加功能来丰富防火墙。这些功能包括 ACME 客户端、Wazuh 代理、NTP Chrony 服务以及作为反向代理的 Caddy。



![Image](assets/fr/051.webp)



## III.OPNsense 的先决条件



首先，您需要决定在哪里安装 OPNsense。有几种可能的解决方案，包括将 OPNsense 安装在 .NET Framework 上：





- 作为虚拟机的管理程序，无论是 Hyper-V、Proxmox 还是 VMware ESXi 等。
- 作为*裸金属*系统的机器。这可以是一台充当防火墙的小型 PC。



您还可以通过我们的在线商店购买 ** 个 OPNsense 机架式设备**。



您需要考虑运行 OPNsense 所需的硬件资源。本文档页面](https://docs.opnsense.org/manual/hardware.html)对此有详细说明。



**生产所需的最低资源和建议资源：**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

最后，**您的资源需求首先取决于需要管理的连接数**，因此也取决于**您的带宽需求**。此外，您还需要**记住将要激活和使用的服务**（代理、入侵检测等......），因为它们可能会占用 CPU 和/或内存。



您还需要 OPNsense 安装 ISO 映像，可从 [官方网站](https://opnsense.org/download/) 下载。若要在虚拟机上安装，请选择 "**dvd**"作为镜像类型，以获取 ISO 镜像（然后随心所欲地使用它......）。要通过可启动 USB 密钥安装，请选择 "**vga**"选项，以获取 "**.img**"文件。



![Image](assets/fr/048.webp)



您还需要一台电脑用于 OPNsense 管理和测试。



## IV.目标配置



我们的目标是





- 创建一个内部虚拟网络（192.168.10.0/24 - 局域网）**，可通过 OPNsense 防火墙访问互联网。在生产使用中，这可以是您的本地网络、有线网络和/或 Wi-Fi 网络。
- 激活并配置 NAT**，以便内部虚拟网络中的虚拟机可以访问互联网
- 激活并配置 OPNsense** 上的 DHCP 服务器，以便向未来连接到内部虚拟网络的机器分发 IP 配置
- 配置防火墙**，只允许 HTTP (80) 和 HTTPS (443) 从局域网流向广域网。
- 配置防火墙**，允许虚拟局域网使用 OPNsense 作为 DNS 解析器 (53)。



如果您使用的是 Hyper-V 平台，则会得到以下表示：



![Image](assets/fr/033.webp)



## V.安装 OPNsense 防火墙



### A.准备可启动 USB 密钥



第一步是准备安装介质： **装有OPNsense**的可启动USB密钥。当然，如果你是在虚拟环境中工作，这是可选项，但无论如何，你都需要下载 OPNsense 安装 ISO 映像。



下载后，您会得到一个包含".img "**格式镜像的**压缩包。你可以使用各种应用程序**创建可启动 U 盘**，其中包括**balenaEtcher**：使用极其简单。更重要的是，应用程序会识别存档中的映像，因此您无需事先解压。





- [下载 balenaEtcher](https://etcher.balena.io/)



程序安装完成后，选择图像和 USB 密钥，然后点击 "Flash"！稍等片刻。



![Image](assets/fr/049.webp)



现在可以安装了。



### B.安装 OPNsense 系统



启动托管 OPNsense 的机器。你会看到一个类似下图的欢迎页面。几秒钟后，如图所示的界面就会出现在窗口中。让程序运行吧......



![Image](assets/fr/019.webp)



将 OPNsense 映像加载到机器上，以便以 "**live**"模式访问系统，即暂时存储在内存中。



![Image](assets/fr/025.webp)



然后，您将看到与下面类似的 Interface。使用登录名 "**installer**"和密码 "**opnsense**"登录。请注意，键盘目前是**QWERTY**。此时，我们将**启动 OPNsense 安装程序**。



![Image](assets/fr/026.webp)



屏幕上会出现一个新向导。第一步是选择与您的配置相对应的键盘布局。对于 AZERTY 键盘，请从列表中选择 "**法语（重音符号键）**"选项，然后双击**。



![Image](assets/fr/027.webp)



第二步是选择要执行的任务。在这里，我们要使用**ZFS 文件系统**进行安装。在 "**安装（ZFS）**"一行定位，并用**回车**确认。



![Image](assets/fr/028.webp)



第三步，选择 "**条**"，因为我们的机器只配备了**个磁盘**：不可能有冗余来确保防火墙存储及其数据的安全。当安装在物理计算机上，通过 RAID 原理防止磁盘出现硬件故障时，这一点尤为重要。



![Image](assets/fr/029.webp)



第四步，只需按**回车**键确认。



![Image](assets/fr/030.webp)



最后，选择 "**是**"并按**回车**键确认。



![Image](assets/fr/031.webp)



现在你需要等待 OPNsense 的安装...这个过程大约需要 5 分钟。



![Image](assets/fr/032.webp)



安装完成后，我们可以在重启前更改 "**root**"密码。选择 "**Root Password**"，按**Enter**键，输入两次密码 "**root**"。



![Image](assets/fr/020.webp)



最后，选择 "**完成安装**"并按**回车**。借此机会**从虚拟机的 DVD 驱动器中弹出磁盘**。在虚拟机设置中，还可以设置首次启动到磁盘。



![Image](assets/fr/021.webp)



虚拟机会重新启动并从磁盘加载 OPNsense 系统，因为我们刚刚安装了它。使用控制台中的 "root "账户和新密码登录（否则，默认密码为 "**opnsense**"）。



### D.连接网络接口



屏幕如下所示。选择 "**1**"并按**Enter**键，将机器的网卡与 OPNsense 接口关联起来。



![Image](assets/fr/022.webp)



首先，向导会要求您配置链路聚合和 VLAN。请指定 "**n**"以拒绝，每次都要用**回车**验证您的答案。接下来，您需要将两个接口 "**hn0**"和 "**hn1**"分配给**WAN**和**LAN**。原则上，"**hn0**"对应广域网，另一个 Interface 对应局域网。



具体操作如下



![Image](assets/fr/023.webp)



我们现在有：





- 与 "**hn1**"网卡和 OPNsense 默认 IP Address 相关联的 Interface **局域网**，即 **192.168.1.1/24**。
- Interface **WAN**与 "**hn0**"网卡相关联，并与本地网络上通过**DHCP**检索到的 IP Address 相关联（得益于我们的外部虚拟交换机）。



出于安全考虑，OPNsense 管理 Interface 默认只能从局域网 Interface 访问。因此，您必须连接到防火墙的局域网 Interface 才能进行管理。如果无法连接，可以暂时从广域网管理 OPNsense。这需要禁用防火墙功能。



为此，请通过 "**8**"选项切换到 shell 模式，并运行以下命令：



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E.访问 OPNsense Interface 管理系统



可使用局域网** Interface（或广域网）的 IP Address 通过 HTTPS 访问 OPNsense 管理 Interface。浏览器将带您进入登录页面。使用之前选择的 "root "账户和密码登录。



![Image](assets/fr/034.webp)



等待几秒钟...系统将提示您按照向导进行基本配置。点击 "**下一步**"继续。



![Image](assets/fr/036.webp)



第一步是定义主机名、域名、选择语言并定义用于名称解析的 DNS 服务器。保留 "**启用解析器**"选项将允许防火墙用作 DNS 解析器，这对我们虚拟局域网中的机器非常有用。



![Image](assets/fr/037.webp)



进入下一步。虽然默认情况下已经配置了服务器，但向导会为您提供**定义用于日期和时间同步**的 NTP 服务器的选项。此外，必须选择与您的地理位置相对应的时区（除非您有特殊要求）。



![Image](assets/fr/038.webp)



接下来是一个重要步骤： **配置 Interface 广域网**。目前，它是在 DHCP 模式下配置的，除非您想设置静态 IP Address，否则将保持这种配置模式。



![Image](assets/fr/039.webp)



还是在 Interface 广域网配置页面，如果广域网侧的网络使用私有寻址，则需要取消选中 "**Block access to private networks via WAN**"（**阻止通过广域网访问私有网络）选项。如果您运行的是实验室，则可能会出现这种情况，因此可能会阻止您访问互联网。



![Image](assets/fr/040.webp)



接下来，你可以**定义一个 "root "**密码，但这是可选项，因为我们已经定义好了。



![Image](assets/fr/041.webp)



继续到最后，启动配置重载。如果需要继续通过广域网进行控制，请在此过程完成后重启上述命令。



![Image](assets/fr/042.webp)



仅此而已！



![Image](assets/fr/035.webp)



### E.DHCP 配置



我们的目的是使用 OPNsense DHCP 服务器在虚拟局域网中分配 IP 地址。为此，我们需要访问该菜单位置：



```
Services > ISC DHCPv4 > [LAN]
```



**如你所见，局域网默认情况下已经启用了 DHCP ** 如果你对这项服务不感兴趣，就应该禁用它。虽然它已经启用，而且我们也想使用它，但还是有必要查看一下它的配置。



如有需要，您可以更改要分发的 IP 地址范围： **192.168.10.10**至**192.168.10.245**，具体取决于当前设置。



![Image](assets/fr/046.webp)



我们还可以看到，"**DNS 服务器**"、"**网关**"、"**域名**"等字段默认为空。事实上，这些不同字段的某些选项和默认值是自动继承的。例如，对于 DNS 服务器，将分配 Interface 局域网的 IP Address，使 OPNsense 防火墙可用作 DNS 解析器。



如有必要，在进行任何更改后保存配置。



![Image](assets/fr/047.webp)



要测试 DHCP 服务器，需要将一台机器连接到防火墙的局域网。



这台机器必须从 OPNsense DHCP 服务器获取 IP Address，我们的机器必须能够访问网络。互联网接入必须正常。请注意，如果从广域网访问 OPNsense 时禁用了防火墙功能，这将禁用 NAT，使您无法访问网络。



**注意**：从 OPNsense 管理 Interface 可以看到当前发布的 DHCP 租约。为此，请访问以下位置： **服务 > ISC DHCPv4 > 租约**。



![Image](assets/fr/045.webp)



### F.配置 NAT 和防火墙规则



好消息是，我们现在可以从局域网访问 OPNsense 管理 Interface。



```
https://192.168.1.10
```



登录 OPNsense 后，让我们来看看 NAT 配置。转到这个位置： **防火墙 > NAT > 出站**。在这里，你可以选择自动（默认）或手动创建出站 NAT 规则。



通过 "**自动生成外向 NAT 规则**"选项选择自动模式，然后点击 "**保存**"（原则上，此配置已是活动配置）。在自动模式下，OPNsense 会自行为每个网络创建一个 NAT 规则。



![Image](assets/fr/043.webp)



目前，所有连接到虚拟局域网 "**192.168.10.0/24**"的计算机都可以不受限制地访问互联网。不过，我们的目标是限制对广域网的访问，只能使用 HTTP 和 HTTPS 协议，以及防火墙 Interface 局域网上的 DNS。



因此，我们需要创建防火墙规则...浏览菜单如下 **防火墙 > 规则 > 局域网**。



**默认情况下，有两条规则授权所有 IPv4 和 IPv6 的局域网出站流量**。点击每行开头最左边的 Green 箭头，停用这两条规则。



然后创建三条新规则，授权 **LAN 网络**（即 "**LAN net**"）为 ：





- 使用**HTTP**访问所有目的地。
- 使用 **HTTPS** 访问所有目的地。
- 通过**DNS协议**（这意味着使用防火墙作为 DNS）在其**Interface LAN**（即 "**LAN Address**"）上请求**OPNsense**，否则通过其 IP Address 授权您的 DNS 解析器。



结果如下



![Image](assets/fr/044.webp)



剩下的工作就是点击 "**应用更改**"，将新的防火墙规则切换到生产中。 **请注意，所有未明确授权的流量默认都将被阻止



局域网机器可以使用 HTTP 和 HTTPS 访问互联网。所有其他协议都将被阻止。



![Image](assets/fr/018.webp)



## IV.结论



按照本指南，您就可以安装 OPNsense 并立即开始使用。OPNsense 提供多种功能，可有效保护和管理网络流量，适合在专业环境中使用。



这只是安装的开始：您可以自由探索菜单和配置其他功能，使 OPNsense 满足您的需求。