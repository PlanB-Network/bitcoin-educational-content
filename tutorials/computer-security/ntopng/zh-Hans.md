---
name: Ntopng
description: 使用 ntopng 监控网络
---
![cover](assets/cover.webp)



___



*本教程基于 Florian Duchemin 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。



___



## I.介绍



**无论是检查网络流动性、清楚了解使用情况还是进行性能统计，网络流量监控都是企业网络**重要的组成部分。它有助于预测基础设施的变化，并有助于确保用户的使用质量（也称为 QoE，即*体验质量*，与 QoS 相对）。



为此，有许多技术和软件/协议可供使用。例如，Cisco 开发的 Netflow 可用于从 Interface 获取 IP 流量统计数据，但其使用仅限于兼容设备。



因此，在本教程中，我将介绍 **Ntop**，并告诉您如何在基础架构中使用它来监控网络使用情况。



Ntop 是一款开源软件，可安装在任何 Linux 机器上。它是免费的，可以收集以下数据：





- 带宽利用率
- 主要客户
- 主要目的地
- 使用的协议
- 使用的应用程序
- 使用的端口
- 等等。



它现在更名为**Ntopng（新一代）**，免费提供许多基本功能。此外，还提供商业版本，可将配置的警报导出到 SIEM 类型的软件，或使用探针直接定义的规则过滤流量。



## II.先决条件



Ntop 探头的安装因设备和环境而异。因此，我不会在这里为您提供分步指南，但会概述各种可能性。



### A.机载模式



如果您在生产中安装了 pfSense、OPNSense 或 Endian 防火墙，甚至是安装了 NFTables 的 Linux 工作站，那么好消息来了！您可以直接安装 Ntopng 并开始监控您的接口。



这种技术的优点是不需要额外的硬件。另一方面，它会增加资源利用率，因此要确保有足够的硬件或足够大小的虚拟机（至少 2 个内核和 2BG 内存）。



### B.TAP / SPAN 模式



**分路器是**一种网络设备，它能复制通过它的流量并将其发送到另一个设备。**这种设备的优点是不需要对现有基础设施进行任何改动，可以放置在任何地方以监控特定的网络部分，或放置在核心交换机和边缘路由器之间以分析进出互联网的流量。



这种设备的最大缺点是成本高。在当今的千兆网络中，被动式分路器无法正确捕捉网络流量，因此您需要一个主动式设备，价格约为 200 欧元（最低）。



交换机使用**SPAN**模式，也称为**端口镜像**，将流量从一个端口转发到另一个端口。到目前为止，这是我最喜欢的一种方法，因为它设置简单，而且像 tap 一样，可以随意监控部分网络或整个网络。不过，它也有两个缺点：交换机必须集成这一功能，而且使用它可能会增加交换机处理器的负荷。



### C.路由器模式



在 Linux 下挂载路由器并在其上安装 ntopng 是完全可能的。这种方法的唯一缺点是会修改你的网络，无论是内部寻址，还是 "真实 "路由器与你添加的路由器之间的寻址。



注：对于文章[使用 Raspberry Pi 和 RaspAP 创建 Wifi 路由器](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/)的读者，完全可以在 Rpi 上安装 ntopng 来获得准确的统计数据！



### D.桥接模式



一个有趣的替代方法是使用**桥接模式的 Linux 机器。**放置在两台设备之间，这样就可以捕获所有流量，而无需干预基础设施或其设备的配置。由于一台旧机器就能完成这项工作，因此这种方法的成本也很有吸引力。请注意，为达到最佳效果，设备应配备三块网卡，其中两块用于网桥模式，一块用于访问 Interface 和 SSH。也可以只使用两块网卡，但这样设备管理流量也会被捕获...



因此，我将使用**后一种模式。出于实际考虑，我将使用虚拟机进行演示，但在物理机上使用的方法仍然相同。



## III.使用 Interface 电桥准备探头



对于探测器，我选择了一台**Debian 11**机器进行最小化安装。



第一步，始终如一，更新.NET Framework：



```
apt-get update && apt-get upgrade
```



然后安装 **bridge-utils** 软件包，这样我们就可以创建桥接器了：



```
apt-get install bridge-utils
```



安装完成后，首先要注意的是网卡的当前名称。在 Debian 系统下，这个名称有多种形式，我们需要它来进行配置。



一个简单的 **ip add** 命令就会返回包含这些信息的输出结果：



![Image](assets/fr/016.webp)



在这里，我看到了 3 个接口：





- Lo**：这是回环 Interface；它是在设备上 "回环 "的虚拟 Interface。基本上，这个 Interface 的 Address 是 127.0.0.1（当然，127.0.0.0/8 中的任何 Address 都可以，因为这个范围是为此目的而保留的），用于与设备本身联系。如果您在工作站上安装了一个网站（例如使用 WAMPP），您可能曾经使用过 "*localhost*"Address。Address 来显示自己机器上的网站。该主机名与 Address 127.0.0.1 相关联，因此也与 Interface 回环相关联。
- ens33**: 这是我的第一个 Interface，它从我的 DHCP 收到了一个 Address
- ens36**: 我的第二个 Interface



现在我已经掌握了所有信息，可以修改 */etc/network/interfaces* 文件来创建我的网桥。下面是它目前的样子（可能会有所不同）：



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



第一部分涉及我的环回 Interface，我不会碰它，然后是 Interface ens33。修改包括添加第二个 Interface（ens36），并用这两个接口配置网桥：



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



下面是对这些最初变化的一些解释：





- auto *Interface***：将在系统启动时自动 "启动 "Interface
- iface *Interface* inet manual** ：使用不带任何 IP Address 的 Interface。如关键字 "static "可定义静态 IP Address，"dhcp "可使用动态寻址。



修改仍在继续：



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



在此，我再解释一下：





- iface br0 inet static**：在这里，我用静态 Address 定义了我的 Interface 网桥 (*br0*)。
- Address、网络掩码、网关**：板寻址信息
- bridge_ports**：要包含在网桥中的接口
- bridge_stp**：生成树协议用于交换机互连，以检测冗余链路并避免环路。由于网桥可以插入两条网络路径之间，因此它可能成为环路的源头，因此有可能启用该协议。我在这里不需要它，所以将其禁用。



保存更改并重新启动网络：



```
systemctl restart networking
```



要检查更改，请再次显示 **ip** 添加命令的结果：



![Image](assets/fr/021.webp)


您可以清楚地看到**我的新 Interface "*br0*"，以及我为其分配的 IP Address。**顺便提一下，您还可以看到我的两个物理接口确实 "UP"，但没有 IP Address。



## IV.安装 NtopNG



现在，我们的探针已经可以嗅探我的网络和路由器之间的流量了，剩下要做的就是安装 ntopng。为此，首先修改*/etc/apt/sources.list*文件，在以**deb**或**deb-src**开头的每一行末尾添加**contrib**。



默认情况下，软件包源只包含符合 DFSG（*Debian Free Sotftware Guidelines*）的软件包，这些软件包由 **main** 关键字标识。您也可以添加这些源：





- contrib**：包含符合 DFSG 标准的软件，但使用了不属于**主**分支的依赖项的软件包
- 非自由**：包含不符合 DFSG 标准的软件包



/etc/apt/sources.list 中的一行示例 ：



```
deb http://deb.debian.org/debian/ bullseye main
```



因此，我只需在这样的行文中加上**contrib**一词。



其余步骤请参见 [NtopNG] 网站 (https://packages.ntop.org/apt/)，对于 Debian 11，您需要添加 Ntop 源，以便将来安装。添加工作可通过使用 .NET Framework 3.0 自动完成：



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



然后是实际安装阶段：



```
apt-get clean all
apt-get update
apt-get install ntopng
```



第一条命令是删除 apt 软件包管理器的缓存。第二条命令将更新软件包列表，第三条命令将安装 NtopNG。



安装后，**NtopNG 软件可直接从 Debian 机器的 3000 端口**。因此，对我来说，它是 "http://192.168.1.23:3000`"。



![Image](assets/fr/022.webp)



NtopNG 主页



系统会显示默认登录名和密码，只需输入即可！



## V.使用 NtopNG



首次登录时，系统首先会要求您更改默认的管理密码和语言。不幸的是，法语不在其中。



然后，您就来到了仪表盘上：



![Image](assets/fr/023.webp)



NtopNG 仪表板



别不习惯这个！如果你注意到屏幕上方的黄色方框 你会看到一句话："*License expires in 04:57*"。默认情况下，安装后会启动 NtopNG 完整版的试用，但试用时间（非常有限）。一旦达到 "倒计时"，*社区*版本将被激活，仪表板也会发生变化：



![Image](assets/fr/024.webp)



新的 NtopNG 社区仪表板



首先要做的是**检查是否有正确的 Interface 正在监听**。在左上角的可用接口下拉列表中，您可以选择我们感兴趣的 Interface：br0



![Image](assets/fr/025.webp)



Interface 选择



新窗口显示的是 "最大缺陷通话者"，即通信量最大的设备。这里只显示了两个电台：



![Image](assets/fr/026.webp)



**源主机显示在左侧，目的地显示在右侧 ** 这样就可以直观地看到每台主机使用的总带宽，并获得网络流量的总体情况。这还不错，但我们还可以更进一步...



例如，如果我点击 "*主机*"，就会得到一张图表，显示网络上每台主机的发送和接收功耗。例如，在这里我可以看到，仅 192.168.1.37 就占了我流量的 80%：



![Image](assets/fr/027.webp)



如果我点击有关主机的 IP Address，就会跳转到一个摘要页面：



![Image](assets/fr/028.webp)



例如，我可以看到它是一台 VMWare 机器（通过识别我的 MAC Address 的 YES），它的名称是 DESKTOP-GHEBGV1（因此肯定是一台 Windows 主机），而且我还可以**收到和发送的数据包以及数据量的统计**。



您还将注意到本摘要顶部的一个新菜单。我建议您点击 "**应用程序**"，看看是什么带来了如此多的流量：



![Image](assets/fr/017.webp)


哈，看来我们找到答案了！在左边的图表中，**我们看到 76.6% 的流量来自...Windows Update**，所以这台主机正在下载更新！



NtopNG 采用了一种名为 DPI 的技术，即 "深度包检测"（Deep Packet Inspection）*，使其能够对每个网络流进行分类，并定义其背后的应用程序（或应用程序系列）。



为了演示，我在主机上启动了一个 YouTube 视频：



![Image](assets/fr/018.webp)



**立即识别并分类流量！



注意：由于显而易见的原因，此类软件可能会引发隐私问题，因此请在适当的条件下谨慎使用。还请注意，可以**匿名化结果**，该选项可在**设置 >偏好设置 > 杂项**中找到，名为 "**屏蔽主机 IP Address**"。



## VI.检测和警报



NtopNG 还能对某些信息源发出安全警报。这些警报可在左侧横幅上的**警报**菜单中找到。例如，我这里共有 2851 个警报，分为不同的严重程度：通知、警告和错误。



![Image](assets/fr/019.webp)



让我们来看看高度临界警报，我有 17 个！



点击该图可查看警报详情。这里没有什么令人担忧的，只是一个假阳性，下载更新被归类为 HTTP 流中的二进制文件传输，这确实可能意味着一次攻击。



![Image](assets/fr/020.webp)



不过，由于我使用的是免费版本，所以无法排除作为警报来源的域或主机，因此您必须密切关注它们，以免错过更令人担忧的情况。如果出现.NET病毒，NtopNG 将发出 generate 警报：





- 通过 HTTP 下载二进制文件
- 可疑的 DNS 流量
- 使用非标准端口
- SQL 注入检测
- 跨站脚本 (XSS)
- 等等。



## VII.结论



在本教程中，我们了解了**如何使用 NtopNG**设置探针，使我们能够**分析网络流量**，直观地了解协议使用情况和每台主机的占用情况，还能检测可疑流量。



遗憾的是，我无法在本文中介绍所有的功能和可能性，但请放心探索！



该解决方案可在企业基础设施中永久实施。NtopNG 还能将结果导出到 InfluxDB 数据库，使您能够使用 Graphana 等第三方工具创建自己的仪表盘。