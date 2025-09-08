---
name: Nmap
description: 掌握用于网络映射和漏洞扫描的 Nmap
---

![cover](assets/cover.webp)



*本教程基于 Mickael Dorigny 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文有改动。



___



欢迎阅读本 Nmap 入门教程，本教程专为希望掌握这一强大网络扫描工具的人员而设计。目的是为您提供日常有效使用 Nmap 所需的基础知识。



Nmap 是一种多功能工具，被 IT、网络和网络安全专业人士广泛用于诊断、网络发现和安全审计。本教程针对那些刚进入这些领域并希望学习 Nmap 基础知识的人。建议具备系统和网络管理基础知识。



您将学习 Nmap 的基础知识、如何执行端口扫描、识别网络上的活动主机、检测服务版本和操作系统、执行漏洞扫描等。每个部分都包含详细的解释和实际示例，帮助您掌握在各种情况下使用 Nmap。



本教程结束时，您将对 Nmap 有一个扎实的了解，并能有效地使用它来提高网络的安全性和管理水平。祝您阅读愉快



## 1 - Nmap 简介：什么是 Nmap？



### I.介绍



在第一节中，我们将介绍 Nmap 网络扫描工具。我们将了解有关该工具的关键 Elements 及其一般工作原理。这将有助于我们更好地理解本教程的其余部分。



### II.Nmap 工具介绍



Nmap 是_Network Mapper_的缩写，是一款免费的开源工具，用于**网络发现、映射和安全审计**。它还可用于其他任务，如**网络清单、诊断或监督**。



它可以确定目标网络上的主机是否处于活动状态、是否可以访问、暴露了哪些网络服务、使用了哪些版本和技术，以及其他有用的分析信息。Nmap 可用于扫描特定机器上的单个服务，也可用于扫描大片网络，甚至整个互联网。



Nmap 的优势很多：





- 功能强大、灵活**：Nmap 可以扫描大型网络并使用高级检测技术。它支持 UDP、TCP、ICMP、IPv4 和 IPv6，可以执行版本检测、漏洞扫描或特定协议交互。它的架构是模块化的，这主要归功于 NSE（Nmap 脚本引擎）脚本，我们将在本教程稍后介绍。
- 易于使用**：官方文档丰富且质量上乘。众多社区资源也可帮助您开始使用。
- 知名度和寿命**：Nmap 自 1998 年以来一直是该领域的参考工具。本次更新时的当前版本为 7.95。虽然有其他工具可用于特定任务，但 Nmap 仍是网络映射和分析的必备工具。



**Nmap at the movies**



Nmap 是少数几个在公众中享有一定知名度的安全工具之一。它曾出现在电影《黑客帝国重装上阵》（Matrix Reloaded_）中，崔妮蒂使用它入侵系统的场景极具代表性：



![nmap-image](assets/fr/01.webp)



矩阵以 Nmap 为特色的重装场景



他还出演了其他电影作品。



**反馈



作为一名系统管理员、网络安全审计员和五项测试员，我几乎每天都**使用 Nmap，并**经常向希望加强对网络的掌控和提高诊断能力的系统管理员推荐 Nmap。



### III.高层运作



Nmap 适用于 Linux、Windows 和 macOS。它主要用 C、C++ 和 Lua（用于 NSE 脚本）编写。它主要通过命令行使用，不过也有 Zenmap 等图形界面。不过，我们强烈建议您从命令行开始使用，以便更好地了解它是如何工作的。



举个简单的例子：



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



稍后将详细解释该命令。在本教程中，我们将在 Linux 上使用 Nmap，但它在其他系统上的用途也类似。在 Windows 下，Nmap 依靠**Npcap**库（取代现已过时的 WinPcap）来捕获和注入网络数据包。



Nmap 的使用类似于传统的二进制文件，如 `ls` 或 `ip`。某些高级功能可能需要提升权限，因为该工具有时会以非常规方式处理数据包，以引起目标系统的特定反应（特别是服务或漏洞检测）。



### IV.使用 Nmap 的影响



使用 Nmap 之前，必须了解其对网络和系统的潜在影响：





- 它可以在短时间内发送**万甚至数百万个数据包**，从而使某些网络基础设施达到饱和状态。
- 它可以 generate **畸形或非标准**数据包，可能会破坏某些设备（尤其是工业系统）。
- 它可以产生类似攻击的行为**，从而触发安全系统（防火墙、IDS/IPS 等）的警报。



一般来说，**Nmap 是一个非常健谈的工具**，因为它会产生大量流量以提取尽可能多的信息。因此，在敏感或生产环境中使用之前，最好充分了解其工作原理。



### V.结论



本节将介绍 Nmap 及其主要功能。我们已经看到它是一个重要、强大而灵活的网络映射工具。我们还讨论了它的工作原理和使用时的注意事项，为教程的后续部分做好铺垫。



## 2 - 为什么使用 Nmap？



### I.介绍



在本节中，我们将介绍 Nmap 网络扫描工具的主要用途。我们将看到，它是一种在许多场合和职业中广泛使用的工具，在你的工具箱中拥有它并知道如何掌握它绝对是一项有用的技能。



### II.使用 Nmap 进行诊断和监督



Nmap 可用于网络诊断，更广泛地说，可用于监控。就像 ping 可以用来确定两台主机是否在通信一样，Nmap 也可以用来快速确定一台主机是否处于活动状态，或某项服务是否在运行。借助 [Nmap]（https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"），我们可以获得有关主机响应时间、数据包路径、特定服务响应等方面的精确数据。



例如，可以使用以下命令和结果快速查明主机 **192.168.1.18** 上的网络服务器是否处于活动状态并作出正确响应：



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*使用 Nmap 从远程服务器检索网络服务状态*。



因此，在调试或诊断阶段，使用 Nmap 比著名的 "ping 测试 "更进一步。我们稍后会看到，Nmap 有几种方法可以用来识别某个端口上正在监听的服务，包括其版本。



### III.使用 Nmap 进行网络映射



作为_网络映射器_，网络映射是该工具的主要目标。它可以在本地网络内使用，也可以跨多个网络、子网和 VLAN 使用，以列出所有可连接的主机和服务。Nmap 使这项任务比任何手动方法都更快、更有效。



例如，可使用以下命令快速识别 **192.168.1.0/24** 网络上的活动主机：



```
nmap -sn 192.168.1.0/24
```



*注意："-sP "选项已过时，由"-sn "取代。



![nmap-image](assets/fr/03.webp)



*使用 Nmap 发现网络上可连接的主机*



稍后我们将看到，Nmap 有几种方法用于确定主机是否可以被视为 "活动 "主机，即使它事先没有暴露任何服务。



### IV.使用 Nmap 评估过滤策略



Nmap 的优点是实事求是：它的结果可以确定具体的结论，与任何架构文件或过滤策略都不同。它是评估信息系统分隔有效性的关键工具，因为它可以**验证过滤策略是否真正得到应用**。



在企业网络中，最佳实践要求根据系统的作用、关键性或位置对系统进行分段。过滤规则（通常通过防火墙实施）必须限制区域之间的通信。但这些配置通常比较复杂，而且容易出错。



因此，要验证策略是否得到遵守，最有效的方法就是进行具体测试。例如，可以检查敏感的管理服务（SSH、WinRM、MSSQL、MySQL 等）是否无法从用户区访问。



使用 **Nmap 测试过滤策略**应该是系统性的，然后再将这种策略投入生产。遗憾的是，这种检查往往被忽视。



根据我的经验，在没有验证测试的情况下，很多配置错误都会被忽视。IP 范围或规则疏忽中的一个简单错误，就可能使一个本应隔离的区域受到攻击。



### V.使用 Nmap 进行安全审计和渗透测试



Nmap 有许多有用的功能，可用于安全评估**、渗透测试（pentests），不幸的是，也可用于攻击者。



网络发现功能对攻击者来说至关重要，因为攻击者需要在初始入侵后了解网络拓扑结构。但 Nmap 提供的功能远不止于此：它集成了一个脚本引擎，其中**个专用于漏洞检测**。



例如，该命令可用于检查 FTP 服务是否允许匿名连接，而无需手动连接：



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*使用 NSE 脚本通过 Nmap.* 检查匿名 FTP 身份验证



Nmap 漏洞检测是审计或渗透测试的第一步。它能让您快速识别某些薄弱点，优化您的分析工作。



但要小心： **漏洞扫描工具有其局限性**。Nmap 只涵盖一小部分威胁，如果没有检测到问题，也不能保证系统是安全的。因此，必须**了解所使用脚本的工作原理**，不能完全依赖脚本的判断。



### VI.结论



我们已经看到，掌握 Nmap 可以涵盖从诊断和监控到映射、安全策略评估和漏洞扫描等多种用例。在下一节中，我们将着手安装 Nmap。




## 3 - 安装和配置 Nmap



### I.介绍



在本节中，我们将学习如何在 Linux 和 Windows 操作系统上安装 Nmap 网络扫描工具。本节结束时，我们将掌握开始使用 Nmap 进行未来模块所需的一切。最后，我们将了解使用 Nmap 时可能需要的权限及其原因。



### II.在 Linux 下安装 Nmap



Nmap 最初是为在 GNU/Linux 操作系统上运行而设计的。因此，得益于它的寿命和受欢迎程度，你可以在所有主要 Unix 发行版的官方软件仓库中找到它。在本教程中，我将使用基于 Debian 的操作系统 [Kali Linux]（https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"）。不过，你也可以通过经典的 Debian、CentOS、Red Hat 或其他系统以完全相同的方式使用它！



在 Debian 下，要检查当前软件源中是否有 Nmap，可以使用以下命令：



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



这里的答案清楚地表明，"nmap "软件包存在于软件源中（这里是 Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")的软件源）。从现在起，你可以通过常规的安装命令来安装 Nmap，暂时不用解除任何武装 🙂 ：



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



为了检查 Nmap 安装是否正确，我们将显示其版本：



```
nmap --version
```



这就是预期结果：



![nmap-image](assets/fr/05.webp)



显示当前 Nmap._ 版本的结果。



请注意显示的 "libpcap"（_Packet Capture Library_）库及其版本。libpcap" 也被 Wireshark 使用，Nmap 使用它来创建和操作数据包并监听网络流量。



### III 在 Windows 上安装 Nmap



要在 Windows 操作系统上安装，首先要从官方网站下载二进制文件（别无他法！）：





- 官方网站上的 Nmap 下载页面：[https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




然后，您需要下载名为 `nmap-<VERSION>-setup.exe` 的二进制文件：



![nmap-image](assets/fr/06.webp)



nmap for Windows 安装二进制文件下载页面



一旦在系统中安装了这个二进制文件，只需运行它即可安装 Nmap。这是一个直接的安装过程，你可以将所有选项保留为默认值。



我的反应是取消选中 "zenmap (GUI Frontend)"（zenmap（图形用户界面前端））。这是 Nmap 的图形化 Interface，我没有用过，本教程也不会涉及，但一旦你掌握了 Nmap 命令行工具，就可以随意尝试！



![nmap-image](assets/fr/07.webp)



在 Windows 上安装 Nmap 时可选择取消选择 Zenmap



在 Nmap 安装结束后，建议进行第二次安装：安装 "Npcap "库：



![nmap-image](assets/fr/08.webp)



在 Windows 下安装 Nmap 时安装 "Npcap "库



这是一个库，Nmap 依靠它来管理网络通信，即构建、发送和接收网络数据包。如果你在 Windows 上使用 Wireshark，可能已经接触过这个库，因为它也使用并需要安装。



与 Linux 一样，打开命令提示符或[Powershell]终端（https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell"）并键入以下命令，即可验证 Nmap 是否已安装：



```
nmap --version
```



这就是预期结果：



![nmap-image](assets/fr/09.webp)



显示当前 Nmap._ 版本的结果。



Nmap 已在 Windows 上安装。您可以按照本教程以与 Linux 完全相同的方式使用它。



### IV.使用 Nmap 所需的本地权限



但顺便问一下，使用 Nmap 时，**是否有必要提升系统的本地权限？ **这取决于**。



在其最基本的形式下，即在不使用其选项的情况下，Nmap 不一定需要权限。不过，你很快就会意识到，最好在有权限的情况下（Linux 下为 "root"，Windows 下为 "administrator "或同等权限）使用 Nmap，这样才能充分发挥它的潜力，否则就有可能收到类似这样的错误信息：



![nmap-image](assets/fr/10.webp)



当 Nmap 选项需要 root 权限时，Linux 下的错误信息。



无论是在 Linux 还是 Windows 上，Nmap 在很多情况下都会要求您提供权限访问。主要原因如下（非详尽列表）：





- 构建 "原始 "网络数据包**：Nmap 能够使用多种扫描方法，包括高级数据包操作和构建。例如，当我们要执行 TCP SYN 扫描时，就会遇到这种情况，这种扫描不遵守 TCP 交换的经典_三方握手_。要做到这一点，Nmap 需要使用操作系统原生函数以外的函数，这些函数只知道如何遵守网络通信中的良好做法（它调用了上面看到的 "Npcap "和 "libcap "库）。正因为 Nmap 不按 "标准 "方式行事，所以它才能推断出操作系统、服务和某些漏洞的某些信息。





- 监听网络通信**：Nmap 的某些选项要求它监听网络以获取某些信息。这种操作在操作系统中被认为是敏感的，因为它还允许你监听系统中其他应用程序的通信。与 Wireshark 一样，Nmap 也需要特定权限才能执行此操作，而直接进入特权会话更容易获得这些权限。





- 监听特权端口**：在操作系统中，0 到 1024 端口（TCP 和 UDP）被称为特权端口，也就是说，它们被保留给非常特殊的用途，因此受到保护。虽然这个理由在今天有些过时，但要监听这些端口仍然需要一定的权限，Nmap 可能必须这样做，这取决于它将如何使用。





- 发送 UDP 数据包：** 同样，在 UDP 端口（无状态协议）上监听网络应用程序需要操作系统的特权权限。因此，如果您想执行 UDP 扫描，则需要特权会话，Nmap 必须监听响应才能分析扫描的回复。




更确切地说，至少在 Linux 下，可以在没有实际 root 的情况下运行 Nmap 及其所有功能和选项。这是通过向二进制文件授予正确的_能力_来实现的。不过，这需要高级操作，可能不如直接使用权限运行 Nmap 实用。此外，这种方法并不常见，如果配置不当，可能会带来安全问题。



不过，这与我们的 Nmap 教程有些出入，所以我们暂时不讨论它。



在本教程的其余部分，假定 Nmap 始终以 "root "身份运行（在 shell 中以 "root "身份或通过 "sudo "命令），或在 Windows 下以管理员终端运行，即使没有说明。否则，您可能会体验到与本教程细微但明显的不同。



### V.结论



就是这样！Nmap 现在已经安装在我们的操作系统上，无需进一步配置即可使用。本节结束了对 Nmap 的介绍和演示。希望它能让你大开眼界，并迫不及待地开始实践。



说正经的，我们现在对 Nmap 映射工具有了更深入的了解，知道了它的最常见用途和局限性。让我们继续前进！




## 4 - 使用 Nmap 扫描 TCP 和 UDP 端口



### I.介绍



在本节中，我们将学习如何使用 Nmap 网络扫描工具执行第一次端口扫描。我们将看到如何使用它来编译主机上暴露的网络服务列表，无论是使用 TCP 还是 UDP 协议。



从现在起，请记住只扫描受控环境中获得明确授权的主机。





- 作为提醒：[刑法典：第三章：攻击自动数据处理系统](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**如果您手头没有**，我建议您使用以下免费解决方案，它们就能满足您的需求！





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")** ：黑客培训平台 Hack The Box 不断提供易受攻击的系统，供您随意攻击。该平台提供数百个系统，但更新的 20 台机器全年免费提供，可通过 OpenVPN VPN 访问。





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")** ：该平台提供大量故意造成漏洞的系统供下载，可通过 VirtualBox（也是免费解决方案）或其他方式使用。下载后，无需 VPN - 一切都在本地进行。




此外，您还可以在自己喜欢的操作系统上***创建一个虚拟机，并在上面安装各种服务作为测试目标。这样做的好处是，在扫描过程中，你还能看到服务器端发生了什么，尤其是通过 Wireshark，当我们进行更高级的测试时，你还能参与本地防火墙的工作。



让我们脚踏实地！



### II.通过 Nmap 扫描主机的 TCP 端口



#### A.使用 Nmap 进行首次 TCP 端口扫描



现在我们通过 Nmap 执行第一次扫描。我们的目的很简单：我们要找出刚刚部署的网络服务器暴露了哪些服务，看看是否有任何意外情况，例如不应该被访问的管理服务，或者暴露了我们认为已经退役的应用程序的端口。



在我的例子中，要扫描的主机的 IP Address 是 "192.168.1.18"：



```
nmap 192.168.1.18
```



下面是一个可能的结果。我们看到一个经典的 Nmap 返回值，包含大量信息：



![nmap-image](assets/fr/11.webp)



使用 Nmap._ 进行简单 TCP 扫描的结果



快速查看一下这个结果，我们就会明白，在这台主机上可以访问 TCP/22 和 TCP/80 端口。



默认情况下，如果你不告诉它，Nmap 只扫描 TCP 端口。



#### B.了解简单 Nmap 扫描的结果



不过，让我们更进一步来理解这个输出结果：每一行都很重要，首先是要知道刚刚做了什么，其次是要正确解释扫描结果本身。



第一行主要是提醒扫描版本和日期（毕竟对记录和存档很有用！）：



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



第二行显示主机 "debian.home (192.168.1.19) "的开始扫描结果。当我们同时开始扫描多个主机时，这些信息将非常有用：



```
Nmap scan report for debian.home (192.168.1.19)
```



第三行告诉我们，有关主机处于 "运行 "状态，即激活状态：



```
Host is up (0.00022s latency).
```



最后，Nmap 通知我们，998 个被识别为关闭的 TCP 端口没有显示在 .NET 中：



```
Not shown: 998 closed tcp ports (conn-refused)
```



这为我们节省了近 1000 行看起来像 .NET Framework 2.0 的输出：



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



感谢他让我们免去了这一麻烦！



为什么是 998 个 "关闭 "端口？加上 2 个开放端口就是 1000 个，这就是 Nmap 在默认配置下扫描的端口数，而不是现有的 65535 个 TCP 端口！我们稍后会看到，这完全是可以轻松定制的。但是，如果目标主机有一个服务监听在一个相当特殊的端口上，那么这个 "默认 "扫描就不会发现它。



在这些信息之后，我们发现了最有趣的东西：一张按照 "端口 - 状态 - 服务 "三栏编排的表格：





- 第一列 "端口 "简单地表示目标端口/协议，重要的是要看它是 TCP 端口（`<port>/tcp`）还是 UDP 端口（`<port>/udp`）。





- STATE"（状态）列表示在此端口上发现的网络服务的状态，由 Nmap 根据获得的响应确定。可以是 "打开"、"关闭"、"过滤 "或 "未知"。我们稍后会看到 Nmap 是如何区分这些不同状态的。





- SERVICE"（服务）一栏表示在相关端口上公开的服务。但请注意，我们在这里没有使用主动服务发现选项。Nmap 依赖于端口/协议与所谓分配的服务之间的本地引用："/etc/services "文件




如果查看 Linux 系统上的"/etc/services "文件，会发现一个与 Nmap 显示的链接类似的 "port/protocol - service "链接：



![nmap-image](assets/fr/12.webp)



提取 Linux 下"/etc/services "文件的内容。



重要的是要明白，Nmap 暂时还没有执行任何主动服务发现。例如，如果是这样的话，它就无法识别 TCP/80 端口后面的 SSH 服务。因此，了解如何使用正确的选项非常重要 - 它很快就会到来！



了解如何解释 Nmap 的输出是掌握该工具的重要部分。好消息是，无论使用什么选项，输出结果都大致相同。



#### C.引擎盖下：通过 Wireshark 进行网络分析



如果仔细观察一下扫描服务器的主机的网络 Interface 或服务器本身的网络 Interface 上发生了什么，Nmap 的操作就会更加清晰。这就是我们要做的。



我在这里向你展示的只是 Wireshark 中可以看到的部分内容。如果你想进一步了解，可以在扫描过程中自己进行网络捕获，然后浏览捕获的内容。



在此测试中，我的扫描主机（192.168.1.18）和目标主机（192.168.1.19）位于同一个本地网络。



Nmap 首先通过发送 ARP 请求来确定目标主机是否在本地网络中处于活动状态。如果收到响应，它就知道主机处于活动状态，并开始网络扫描：



![nmap-image](assets/fr/13.webp)



Nmap发出ARP请求，以确定本地网络中是否存在目标主机。



如果要扫描的主机位于远程网络上，Nmap 会首先发送 ping 请求，并尝试连接一些最常暴露的端口（TCP/80、TCP/443）：



![nmap-image](assets/fr/14.webp)



由 Nmap 发出的 ping 请求，以确定目标主机在远程网络上是否可达



如果测试得到响应，则认为目标处于活动状态。



一旦 Nmap 确定目标处于活动状态，它就会尝试用网卡上配置的 DNS 服务器解析其域名：



![nmap-image](assets/fr/15.webp)



Nmap 扫描目标的 dNS 解析度



既然 Nmap 已经确定了目标并知道它处于活动状态，它就开始扫描 TCP 端口：



![nmap-image](assets/fr/16.webp)



在 Nmap 扫描期间 tCP SYN 数据包传输和 RST/ACK 接收



为此，它会在默认范围内的每个 TCP 端口上**发送 TCP SYN 数据包并等待响应**。在上面的截图中，它从扫描的服务器上接收到 TCP RST/ACK 数据包，意思是 "继续前进，没什么可看的"--换句话说，这些端口是关闭的。正如我们在结果中看到的，扫描的大部分端口都是这种情况。但有两个例外：



![nmap-image](assets/fr/17.webp)



对发送到 22 端口的 TCP SYN 数据包的响应，在扫描目标上激活



在上面的截图中，我们看到了目标主机**发送的 TCP SYN/ACK 数据包。端口处于活动状态，并暴露了一项服务。Nmap 确认收到响应，然后终止连接（TCP RST/ACK）。 **这就是它如何知道 TCP/22 端口处于活动状态的**。



我们在这里看到，Nmap 在扫描 TCP 网络时尊重 "三方握手"（Three Way Handshake）。出于性能考虑，可以要求它不响应服务器的返回，这样在扫描大型网络时可以节省几千个数据包。不过，我们将在本教程稍后部分讨论这些选项和优化方法。



现在我们对如何进行 TCP 扫描以及扫描时实际发生的情况有了更好的了解。我们还看到，默认情况下，Nmap 只对有限的几个端口执行 TCP 端口扫描。



### III.使用 Nmap 扫描 UDP 端口



#### A.使用 Nmap 进行首次 UDP 端口扫描



现在让我们看看如何扫描主机的 UDP 端口。正如我们所看到的，Nmap 默认总是扫描 TCP 端口。如果我们没有意识到这一点，就会错过很多信息。



需要提醒的是，在本次测试中，我的扫描主机（192.168.1.18）和目标主机（192.168.1.19）位于同一个本地网络。



```
nmap -sU 192.168.1.19
```



在此，所获得的返回值格式与 TCP 扫描相同，但所显示的活动服务是按要求以 `<port>/UDP` 格式显示的！



![nmap-image](assets/fr/18.webp)



使用 Nmap._ 进行简单 UDP 扫描的结果。



-sU "选项用于告诉 Nmap 你想在 UDP 上工作，而不是默认的 TCP。



顺便提一下，你可能会注意到 Nmap 要求 UDP 扫描具有 "root "权限，这在教程前面已经提到过。



注意：自最新版本的 Nmap 起，建议始终以管理员权限运行 UDP 扫描，以确保结果可靠，因为某些功能需要对网络套接字进行原始访问。



由于 UDP 中没有 "三方握手"（Three Way Handshake），UDP 扫描可能需要很长时间（在我的例子中，扫描 1000 个端口需要 1100 秒），这意味着 Nmap 会等待发送的每个 UDP 数据包的返回，只有在一定时间（超时）后没有返回时，才会将端口判定为 "关闭"。扫描主机的这种响应不是系统性的，通常会限制每秒的响应次数，以避免某些放大攻击。这与 TCP 不同，在 TCP 中，无论端口是打开还是关闭，被扫描主机都会立即做出响应。我们稍后会看到如何优化这一点。



UDP 的第二个难点是**服务并不总是响应传入的数据包**，原因很简单，这并不总是必要的，而且这也是 UDP 的原理。在这种情况下，如果没有收到 ICMP "端口不可达"，服务就会被 Nmap 标记为 "打开|过滤"，如上图所示。



#### B.引擎盖下：通过 Wireshark 进行网络分析



与 TCP 扫描一样，让我们使用 Wireshark 分析仔细看看 UDP 扫描期间在网络层发生了什么。Nmap 判断主机是否处于活动状态的行为是一样的。



扫描 UDP 时唯一真正的区别是，Nmap 不会等待 "三方握手"，因为 UDP（无状态协议）中不存在这种机制：



![nmap-image](assets/fr/19.webp)



在 Nmap 扫描期间传输 uDP 数据包和接收 ICMP（端口不可达



从上面的截图中我们可以看到，Nmap 将发送大量 UDP 数据包，而其中大部分都会收到一个 ICMP 数据包 "Destination unreachable (Port unreachable)"（目标不可达（端口不可达））作为回应。这是正常现象，因为这是 [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122")定义的 UDP 端口不可到达时的适当响应：



![nmap-image](assets/fr/20.webp)



摘自 RFC 1122._



让我们仔细看看 Wireshark 的捕获，它显示了 UDP 中***的三种可能情况：



![nmap-image](assets/fr/21.webp)



使用 Nmap._ 对不同端口进行 UDP 扫描时的网络捕获。



这三种情况如下：





- 第一个 Exchange 由第 3、4 和 8、9 号数据包组成。3、4 和 8、9 号数据包。Nmap 在传统 SNMP 端口上发送 UDP 数据包，因此 ** 提前构造符合协议的数据包**。然后从服务器获取响应（8 号和 9 号数据包）。结果：Nmap 收到响应，服务 "打开"。





- 第二个 Exchange 由数据包 6 和 7 组成。Nmap 向端口 UDP/165 发送一个 "空 "UDP 数据包（无协议结构），并收到一个 ICMP 数据包作为回复："目标不可达（端口不可达）"。结果：Nmap 收到了（否定的）回复，主机正常运行，但它试图访问的服务在该端口上无法运行，该端口将被标记为 "已关闭"。





- 最后一个 Exchange 包含第 12 号数据包：Nmap 向 UDP/1235 端口发送了一个 "空 "UDP 数据包。没有任何回应，甚至没有来自被扫描主机的明确拒绝。结果：Nmap 将端口标记为 "open|filtered"（开放|过滤），因为它无法判断这是因为存在防火墙（配置为不响应），还是因为活动的 UDP 服务，该服务无论如何都不返回响应（在 UDP 中不是强制性的）。




下面是 Nmap 在这三种情况下显示的结果：



![nmap-image](assets/fr/22.webp)



通过 Nmap._ 进行 UDP 扫描的可能结果



现在我们对如何进行 UDP 扫描以及扫描时实际发生的情况有了更好的了解。到目前为止，我们只是以一种非常简单的方式使用 Nmap，并没有真正决定扫描哪些端口，但这种情况即将改变！



### IV.使用 Nmap 微调端口扫描



#### A.Nmap 默认行为提醒



正如我们所看到的，如果不指定任何选项，Nmap 会自己选择要扫描的数量和端口。这是 Nmap 使用的 "默认 "配置，当你没有告诉它具体要做什么的时候。这些默认选项的目的是提供一个暴露的主要端口的概念，这些端口是按暴露的频率（最常见或最频繁的端口）而不是按数字顺序（端口 1、2、3 等）来选择的，同时也是为了避免在没有指定适当选项的情况下开始扫描 65535 个可能的端口，因为对于 "默认 "用例来说，这些选项太长而且太拗口了。



**如何选择这些端口？



默认模式下扫描的 1000 个端口是根据其出现频率选择的。这些统计数据由 Nmap 维护，更新方式与二进制文件本身及其脚本（模块）相同。您可以在"/usr/shares/nmap/nmap-services "文件中查看这些统计数据：



![nmap-image](assets/fr/23.webp)



从文件"/usr/shares/nmap/nmap-services"._____中提取出来。



在第三列中，我们可以看到类似概率（介于 0 和 1 之间）或百分比分布的内容。这是每对端口/协议出现的频率。我们可以看到，最知名的端口（本摘录中的 FTP、SSH、TELNET 和 SMTP）的数值要比其他端口高得多。



#### B.为 Nmap 扫描精确指定目标端口



然而，在现实世界中，我们可能只需要扫描一个特定的端口，或几个端口，或特定范围的端口。Nmap 可以很容易地做到这一点，而且对 UDP 和 TCP 的扫描都是统一的。



**通过 Nmap 扫描特定端口**



如果我们只想扫描一个端口，而不是 1000 个，可以通过 Nmap 的"-p "或"--port "选项指定该端口：



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



因此，扫描速度自然会快很多，Nmap 将只发出检测主机是否处于活动状态所需的数据包，然后再检测指定端口是否可用。如果只想快速测试展示网站上的网络服务是否正常运行，这样就可以节省时间。



**通过 Nmap 扫描多个端口**



同样，我们也可以使用相同的选项向 Nmap 指定多个端口，并用逗号将指定的端口连接起来：



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



无论顺序如何，Nmap 都会检查所有这些端口，而且只检查目标主机上的端口。在 Nmap 的输出中，您会注意到它**明确地告诉我们所有端口及其状态**，即使它们是 "关闭 "的。这与默认行为不同，默认行为下的完整输出会占用太多空间：



![nmap-image](assets/fr/24.webp)



*对指定端口进行 Nmap TCP 扫描的结果。



**扫描一系列端口



如果要扫描的端口数量太多，可以按范围指定，例如 ：



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



当然，您也可以根据自己的喜好进行搭配，例如，您可以根据自己的喜好进行搭配：



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP和UDP端口扫描



您还可以同时对选定的端口执行 UDP 和 TCP 扫描：



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



在最后一个示例中，您会发现 "U: "表示 UDP 端口，"T: "表示 TCP 端口。下面是这种扫描的可能输出结果：



![nmap-image](assets/fr/25.webp)



*使用 Nmap.* 进行 TCP 和 UDP 端口扫描的结果



这真是一种有趣的自定义扫描方式！



**扫描所有端口



最后，还可以向 Nmap 指定更大或更小的范围。我们看到，Nmap 默认选择的列表包含 1000 个端口。我们还可以使用"--top-ports "选项，要求 Nmap 列出最常访问的前 100 个端口或前 200 个端口：



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



最后，我们可以使用"-p-"符号要求它扫描所有可能的端口（全部 65535）：



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



后者需要更长的时间，尤其是 UDP，但您一定不会错过任何开放端口。



*注意："-p-"选项是扫描所有 TCP 端口的推荐方法。对于 UDP 扫描，出于性能考虑，建议限制端口数量，因为完整扫描所有 UDP 端口可能需要很长时间*。



在教程的后面，我们将看到如何优化 Nmap 扫描的速度以满足我们的需要，这对扫描所有 TCP 和 UDP 端口特别有用。



### V.结论



在本节中，我们终于有了一些实际操作的机会，因此我们现在知道了**如何使用 Nmap 的基本方法来扫描主机的 TCP 和 UDP 端口**。我们还详细了解了网络层面的情况，以及 ** Nmap 如何确定 TCP 或 UDP 端口是否处于活动状态**。最后，我们知道了如何精细地选择要扫描的端口，以及 ** Nmap 的默认选项的实际作用**。接下来，我们将重复使用这些知识，并将其应用于扫描整个网络，包括全局映射和网络发现。




## 5 - 使用 Nmap 进行网络映射和发现



### I.介绍



在本节中，我们将学习如何使用 Nmap 网络扫描工具来映射网络。我们将通过 Nmap 的各种选项了解它在这项任务中的功效。最后，我们将了解向 Nmap 指定扫描目标的不同方法。



特别是，我们将使用在上一节中学到的有关 Nmap 如何确定主机是否处于活动状态以及是否可连接的知识。



正如 Nmap 介绍中提到的，这是一款网络映射器。因此，它是绘制本地或远程网络上可访问主机列表的完美工具。



**作者归来：**



事实上，作为一名网络安全审计员和五项测试员，我在进行内部渗透测试时会系统地使用 Nmap 来了解我的位置、本地网络上的邻居、可以访问的其他网络以及位于这些网络上的系统。我的目标很简单：绘制网络地图，确定信息系统的规模，尤其是勾勒出其攻击面。



网络映射在网络诊断、监督、资产映射方面也很有用（你真的确定你的 IS 完全由活动目录或 GLPI/OCS 清单中的内容组成吗？它还可用于检测信息系统中是否存在影子 IT。



### II.使用 Nmap 扫描网络范围



#### A.使用 Nmap 扫描发现网络



现在我们要更上一层楼，分析整个本地网络。没有比这更简单的了：我们只需重复使用上一节中的命令，但指定一个 CIDR 而不是简单的 IP Address。



CIDR（无类域间路由**）是指定网络范围及其范围（使用掩码）的 "经典 "符号。例如，"192.168.0.0/24 "是十进制掩码符号 "255.255.255.0 "的 "翻译"。



要通过指定 CIDR 来使用 Nmap，我们可以如下使用它：



```
# Scan a CIDR
nmap 192.168.0.0/24
```



与上一节中的端口一样，也可以指定多个主机、多个网络或多个范围：



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



下面是我们在网络上运行扫描时可能得到的结果示例：



![nmap-image](assets/fr/26.webp)



Nmap 扫描映射多个网络的结果



特别是，我们看到几个活动主机，每个主机部分都以这样一行开头：



```
Nmap scan report for <name> (<IP>)
```



这样，我们就能清楚地看到下面的结果指的是哪台主机。最后一行也很重要：



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



我们知道，在扫描的网络中，Nmap 发现了 5 台活动主机。



#### B.引擎盖下：通过 Wireshark 进行网络分析



现在，我们将仔细研究通过 Nmap 进行网络发现时在网络层面发生的情况。



如上一节所述，Nmap 默认使用 ARP 协议检测本地网络中是否存在主机：



![nmap-image](assets/fr/27.webp)



使用 Nmap 及其默认选项扫描本地网络时捕获的 aRP 数据包



因此，它几乎可以检测到本地网络上的所有主机，因为对 ARP 请求的响应一般都是由网络上所有活动主机提供的，不会出现任何可疑之处。



对于远程网络，Nmap 使用多种技术组合：



![nmap-image](assets/fr/28.webp)



使用 Nmap 及其默认选项扫描远程网络时捕获的 iCMP 和 TCP 数据包



更准确地说，Nmap 使用 ICMP echo 数据包（ping 的典型情况）和 ICMP Timestamp 数据包，后者通常用于计算数据包的传输时间。它希望得到远程网络主机的响应。



但事情远不止这些。从上面的 Wireshark 截图中可以看到，**TCP SYN** 数据包被系统地发送到要扫描网络中每个潜在主机的 TCP/443 端口，以及 TCP/80 端口上的**TCP ACK** 数据包。



**为什么要将 TCP 数据包发送到端口作为网络发现的一部分？



向给定端口发送 SYN 数据包可让 Nmap **确定该端口上是否有服务在监听**。如果主机用 SYN/ACK 数据包回复 SYN 数据包，这表明它处于活动状态，并且该端口上有服务在监听。因此，Nmap 会在该服务上试试运气，**即使 ping 没有得到响应**。



向给定端口发送 ACK 数据包允许 Nmap **确定该主机上是否存在防火墙**。如果主机用 RST（重置）数据包响应 ACK 数据包，这表明该主机上可能存在防火墙，并阻止了未经请求的流量。这样，即使主机没有响应其他请求，也暴露了它在网络上的存在。



但需要注意的是，使用这种技术进行防火墙检测并非在所有情况下都完全可靠。有些主机可能会因为存在防火墙以外的原因（如特定服务或操作系统配置）而 generate RST 响应。此外，现代防火墙可以配置为不响应此类发现尝试。



现在我们已经有了长足的进步，可以执行基本的网络发现了。现在，我们将查看更多选项，以便更好地控制 Nmap 的行为。



### III.使用 Nmap 在不扫描端口的情况下发现网络



您可能已经注意到，默认情况下，Nmap 会在发现活动主机后**执行端口扫描，这会增加大量数据包并等待扫描响应。如果您的网络上有 5 台主机，Nmap 将尝试检查大约 5,000 个端口的状态，这将花费更长的时间。



不过，也可以使用 Nmap 的选项来执行**只发现网络上的活动主机**，而不发现它们的服务。



如果我们只想知道哪些主机可以访问，而不想知道它们提供的服务和端口，那么我们可以使用"-sn "选项，只使用 ICMP Echo（ping）和 ARP 请求**进行扫描。换句话说，就是完全禁止端口扫描：



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



下面是 Nmap 在不进行端口扫描的情况下进行网络发现的结果：



![nmap-image](assets/fr/29.webp)



未使用 Nmap 进行端口扫描的网络发现结果。



我们已经提到过单独使用 ICMP 发现主机（对于远程网络）可能存在的局限性。这就是为什么 Nmap 还使用了一些技巧，可以暴露主机上防火墙或特定服务的存在。在选项的帮助下，我们可以重复使用这些技巧，甚至扩展它们，而不必对发现的每台主机重新进行完整的端口扫描。



为此，我们将使用"-PS"（TCP SYN）和"-PA"（TCP ACK）选项，它们允许我们指定希望加入的端口作为主机发现的一部分，以及"-PP "选项：



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



与默认选项相比，这种扫描已能确保更全面地发现主机。



我们开始使用多个选项，编写相当全面的命令。这是因为我们知道 Nmap 的工作原理及其 "默认 "选项的局限性，这些选项有时会导致我们浪费时间或错过重要的 Elements。这就是花时间掌握它的意义所在！



详细介绍我们上次订单的选项：





- "`-sn`：禁止对 Nmap 发现的每台活动主机进行端口扫描。





- "`-PP`：启用 ICMP echo（ping 扫描）以发现主机。





- "`-PS <PORT>`"： 在指定端口上发送 TCP SYN 数据包，以检测是否有任何活动服务背叛了未响应 ping 的主机。





- "`-PA <PORT>`"： 在指定的端口上发送 TCP ACK 数据包，以检测是否存在未响应 ping 的活动防火墙。




在上面的示例中，我为"-PS "选项指定了我认为在 Nmap 上下文中最常暴露的端口。然后将在每台主机上测试这些不同的端口，不是要看它们所承载的服务是否真的处于活动状态，而是要看这是否允许我们发现一台没有响应我们的 ICMP Echo 而仍然处于活动状态的主机（通过服务或主机防火墙的响应）。



下面是扫描时的网络捕获结果，在本例中是对单台目标主机的提取：



![nmap-image](assets/fr/30.webp)



Nmap 在高级网络发现过程中发送的数据包，无需端口扫描



我们找到 TCP SYN 数据包、TCP/80 端口上的 TCP ACK 和 ICMP echo。Nmap 将对我们的网络发现扫描所针对的每台主机执行所有这些测试。



### IV.使用资产文件作为 Nmap 的目标



在现实信息系统中，指定目标可能很快就会变得复杂，因为信息系统有时可能由数十或数百个网络、子网和 VLAN 组成。这就是为什么使用文件作为 Nmap 的源文件比在命令行上逐个指定目标要简单的原因。



首先，创建一个简单的文件，每行包含一个条目：



![nmap-image](assets/fr/31.webp)



文件，每行包含一个目标（主机或网络



接下来，我们可以使用目前看到的所有 Nmap 选项，并指定"-iL <path/file>"选项：



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



然后，Nmap 将扫描文件中包含的所有目标。



如果想确保所有目标都被考虑在内，可以使用"-sL -n "选项。这样，Nmap 将只解释文件中的 CIDR 和主机并显示给您，而不会通过网络发送任何数据包：



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



这样可以确保要扫描的主机列表准确无误。



我想与大家分享的最后一个重要提示涉及将**主机或网络排除作为扫描**的一部分。在许多情况下，尤其是当我们希望确保信息系统的**敏感组件不会受到我们的扫描**干扰或破坏时，这种排除主机的需要可能是必要的。



这类需求的常见例子是公司拥有工业（PLC）或医疗保健设备。这些设备有时设计不佳，根本无法接收格式不佳或过多的数据包。出于可用性或业务/人为风险等明显原因，最好将它们排除在测试之外。



要从扫描中排除 IP 地址或网络，我们可以使用 Nmap 的"--exclude"（排除）选项，例如 ：



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



在本例中，我扫描网络 "192.168.1.0/24"，但不包括位于该网络中的主机 "192.168.1.140"。Nmap 不会向该主机发送任何数据包。另一个子网排除的例子：



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



同样，我扫描大型网络 "10.0.0.0/16"，但不会扫描网络 "10.0.100.0/24"。我再次建议使用"-sL -n "选项，以非常清楚地了解哪些主机将被扫描，哪些主机将被排除在扫描范围之外，尤其是在敏感环境下运行时。



### V.网络发现和端口扫描



现在我们可以将本节所学与上一节关于端口扫描选项的内容结合起来。默认情况下，我们已经看到 Nmap 会扫描它发现的每个活动主机上最频繁的 1000 个端口。我们已经了解了如何在不需要的情况下阻止这种行为，但我们也可以完全控制它，甚至可以根据需要扩展它。



例如，以下命令将检查每台扫描主机上的 TCP/22 端口是否存在监听服务：



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap 将首先执行网络发现，列出活动主机，并检查每个主机的 TCP/22 端口是否存在服务。



同样，我们可以对 "192.168.0.0/24 "网络上发现的每台主机上的所有 TCP 端口进行全面扫描，例如不包括主机 "192.168.0.4"：



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



您可以根据自己的需要，自由组合我们目前所学到的所有选项。



### VI.结论



在本节中，我们已经了解了如何使用 Nmap 的各种选项来映射网络。现在，我们已经对扫描目标、Nmap 的端口扫描行为和主机发现方法有了细致的了解。最重要的是，我们知道了 Nmap 的默认行为和限制，以及如何使用其主要选项更进一步。



在下一节中，我们将了解发现 Nmap 扫描的服务和操作系统版本的机制和选项。




## 6 - 使用 Nmap 检测服务和操作系统版本



### I.介绍



在本节中，我们将学习如何使用 Nmap 发现并准确检测扫描主机使用的服务和操作系统版本。我们将详细了解 Nmap 如何完成这项任务，以及该工具的局限性，以便更好地理解和解释其结果。



正如我们在本教程前面的章节中所看到的，默认情况下，Nmap 不会查看它扫描并认为开放的端口上暴露了什么服务。因此，如果您正在监听 TCP/22 端口上的网络服务，Nmap 会继续将其报告为开放，但会报告为 "SSH "服务。这是因为它使用系统本地的 [数据库](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) 来查找端口/协议与服务名称（`/etc/services/` 文件）之间的关系。



在大多数情况下，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 会为您提供正确的信息，因为在生产环境中这种情况很少见。但是，剩下的情况是经典服务（[SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/)、HTTP 等）暴露在非经典端口上（例如 SSH 服务的 2022），在这种情况下，Nmap 无法在本地数据库中找到匹配的端口，或者找到的端口与实际情况不符，您就会错过重要信息。



幸运的是，Nmap 提供了非常精确的选项和机制，可以发现开放端口背后可能隐藏的确切服务。它甚至有一个查询和签名数据库，可以识别确切的技术和版本。除服务外，Nmap 还能识别所使用的技术及其版本。



这就是我们本节要讨论的内容。



### II.如何检测技术或版本



#### A.提醒如何识别技术或版本



要识别一种技术和一个版本，需要检索监听目标端口的服务、内容管理系统、应用程序或软件的名称。例如，网页由内容管理系统（`WordPress`）管理，由网络服务（`Apache`、IIS、Nginx）运行，由服务器（Linux 或 Windows）托管。但如何知道哪个网络服务在运行呢？



查找这些信息的经典方法是 "抓取横幅"（_banner grabbing_），即找到相关服务显示这些信息的位置并读取数据。通常，在默认配置或处理过程中，服务会在连接后的第一个响应中显示其名称甚至版本。



![nmap-image](assets/fr/32.webp)



在 FTP 服务建立 TCP 连接后立即显示版本



在这里，我们可以看到，通过 `telnet` 与该服务进行简单的 TCP 连接会产生一个包含其技术和版本的 TCP 数据包。



一旦确定了所面对的服务类型，还可以向该服务发送特定命令或请求，以从中提取信息。也可以盲目发送这些请求/命令（不确定它们是否是正确的服务类型），希望其中一个请求/命令能引起相关服务的响应。



在其他更高级的情况下，有必要发送特定的数据包以引起反应，如错误，从而提供所使用的版本或技术的详细信息。



可以想象，Nmap 将使用所有这些技术来尝试识别端口上托管的服务的确切类型，以及其技术名称和版本。



#### B.了解 Nmap 探测和匹配



为了对扫描的每个端口进行所有这些检查，Nmap 使用一个经常更新的本地数据库（就像二进制文件或其模块一样）。这是一个几千行的文本文件：/usr/share/nmap/nmap-service-probes`。



该文件由许多条目组成，所有条目都围绕着两个主要指导方针：





- Probe"：这是 Nmap 将发送的数据包的定义，目的是引起要识别的服务作出反应。把它想象成类似 _Hello?Guten Tag?你好？嗯......也许是 Buenos Dias？一旦目标服务收到它能理解的探测（即使用正确的协议），它就会响应 Nmap，Nmap 就能确认它是哪种服务。





- Match"（匹配）：这些是 Nmap 应用于所获响应的正则表达式。如果发送 HTTP GET 请求引起了服务的响应，它将对该响应应用数十种正则表达式，以识别是否存在 "Apache"、"Nginx"、"Microsoft IIS "等字样。




针对特定情况还有一些其他指令，但要了解 Nmap 如何工作和自定义使用，主要还是这些指令。为了使理论部分更加具体，这里有一个例子：



![nmap-image](assets/fr/33.webp)



Nmap的"/usr/share/nmap/nmap-service-probes "文件中的探测示例



在这个示例的第一行，我们看到了一个名为 `GetRequest`的简单易懂的探针。这是一个 TCP 数据包，其中包含一个使用 HTTP/1.0 向网络服务根目录发出的空 HTTP GET 请求，随后是换行和空行。



端口 "行告诉 Nmap 向哪个端口发送此探针。这可以让您确定测试的优先级，节省时间。



最后，我们有两个 `match` 的示例。第一个例子是，如果这一行中包含的正则表达式与收到的服务响应相匹配，扫描的网络服务就会被归类为 "ajp13"。



为了帮助您了解探针的外观，下面列出了本文件中的一些探针（编写本教程时共有 188 个探针）。



![nmap-image](assets/fr/34.webp)



Nmap 使用的几个探针的示例，这些探针存在于文件 `/usr/share/nmap/nmap-service-probes`._ 中。



前两种（称为 "NULL "和 "GenericLines"）在此特别值得关注，因为它们只是发送一个空的 TCP 数据包或一个包含换行符的数据包。服务器服务通常会在接收到连接后立即发布自己的消息，而不需要客户端的任何具体操作、命令或请求。



下面是一个稍微复杂的 _match_ 案例：



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



这里的 `m|` 和 `|` 之间包含了准确的正则表达式，它对该文件中的任何正则表达式进行了分界。请花点时间阅读整个示例。你会注意到正则表达式中的一个选择：`([\d.]+)`，用于隔离一个版本。本示例还定义了其他 Elements，如产品名称 `p/nginx/`、检索到的版本 `v/$1/` 和带有版本的 CPE `cpe:/a:igor_sysoev:nginx:$1/`。



CPE（通用平台枚举）是一种标准化的符号系统，用于识别和描述软件和硬件。这种格式能更有效地管理漏洞和安全配置，最重要的是，无论涉及何种产品，都能以统一的方式表示它们。下面是两个 CPE 示例：`cpe:/o:microsoft:windows_8.1:r1` 和`cpe:/a:apache:http_server:2.4.35`。



在这里，我们清楚地标识了它们的类型：`o`代表操作系统，`a`代表应用程序、供应商、产品和版本。



因此，在与这些正则表达式之一_match_匹配的情况下，我们不仅会检索到服务的名称，还会检索到它的版本和确切的 CPE，从而更容易找到影响该版本的 CVE。你会在 Nmap 的标准输出中发现这些信息，而且你会发现这些信息对其他用途也非常有用，我们将在后面几节中介绍。



_matches_的具体语法，以及更广泛地说，`/usr/share/nmap/nmap-service-probes`文件中的指令的语法并不仅限于此，如果你不习惯操作Nmap及其结果，可能会觉得相当复杂。然而，你至少应该记住它的存在和一般操作，这将在你以后理解或调试一个结果、定制一个扫描或甚至为 Nmap 开发做贡献时派上用场。



### III.使用 Nmap 检测版本



现在我们通过一个简单的选项 `-sV`来使用所有这些复杂的 _Probe_ 和 _Match_ 机制。这只是告诉 Nmap：试着找出你设置为开放的服务和端口版本。



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



下面是一个完整的例子，说明了这样一条命令的结果：



![nmap-image](assets/fr/35.webp)



Nmap 对暴露在网络上的应用程序进行版本检测的结果



在这里，我们可以看到 Nmap 成功地识别了该目标暴露的所有网络服务版本，并在新的 `VERSION` 列中显示了这些信息。如果这些信息是恢复签名的一部分，那么就可以看到相当精确的信息，甚至可以精确到操作系统。



要详细了解漏洞扫描过程中发生的情况，我们可以使用 `--version-trace` 选项。这将提供调试模式视图，显示导致检测的_Probe_：



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



因此，我们将有大量信息需要整理。尝试找出以 "服务扫描 Hard 匹配 "开头的行。然后你会看到类似这样的行：



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



我们可以清楚地看到哪些 _Probes_ 被用来检测技术和版本（在本例中是 `NULL` 和 `GetRequest` _Probes_），以及检索到的信息。



### IV.掌握测试和检测的准确性



现在，我们要回到 `/usr/share/nmap/nmap-service-probes` 文件中的一个指令，我们之前没有查看过这个指令：



![nmap-image](assets/fr/36.webp)



文件中的 probes `rarity` 指令



该指令用于表示与_Probe_相关的稀有度（即优先级/概率）。这个从 1 到 9 的符号允许您在发送 _Probes_ 时控制 Nmap 执行的分析的完整性。在 Nmap 的 "记号 "系统中，稀有度为 1 时，可提供绝大多数情况下的信息，而稀有度为 8 或 9 时，则代表非常特殊的情况，特定于很少出现的配置或服务。



更清楚地说，在默认情况下，Nmap 会向每个待识别的服务发送稀有度从 1 到 7 的_Probes_。为了让您更好地了解_Probes_在_rarity_中的分布情况，下面是它们的数量：



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



8 和 9 的 "稀有度 "比其他的要多，这似乎有违直觉。这正是因为稀有度 1 探测器是通用的，在大多数情况下都能工作，与服务无关（还记得 `NULL` 探测器，它只是发送一个空 TCP 数据包）。而更复杂的探针在每个服务中几乎都是独一无二的。



如果我们想手动管理我们希望在版本扫描中使用的探针，可以使用 `--version-intensity` 选项。下面是两个例子：



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



最后，这里有一个 _Probe_ 9 和 8 的例子：



![nmap-image](assets/fr/37.webp)



文件 `/usr/share/nmap/nmap-service-probes`._ 中稀有度为 8 和 9 的探针示例



这两个探测器可以检测 Quake1 和 Quake2 服务器（视频游戏）。怀旧意味浓厚，但在日常生活中可能用处不大。



根据您对精确度或速度的需求，请记住 "稀有性 "原则的存在并可能影响结果。



### V.使用 Nmap 检测操作系统



现在我们来看看 Nmap 如何帮助我们检测网络中被扫描和检测到的主机的操作系统。为此，请使用 Nmap 的 `-O`（表示 `OS Scan`）选项。



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



下面是一个结果示例。在这里，Nmap 告诉我们这可能是一个 Linux 操作系统，并提供了有关其确切版本的各种统计数据。



![nmap-image](assets/fr/38.webp)



检测 Nmap 识别操作系统的概率



为此，Nmap 将使用多种技术，其工作方式与 _Probes_ 和 _Matches_ 的技术和版本检测非常相似。主要区别在于，Nmap 将使用相当 "低级 "的 ICMP、TCP、UDP 和其他协议参数。下面是两个检测 Microsoft Windows 11 操作系统的测试示例：



![nmap-image](assets/fr/39.webp)



Nmap 检测 Windows 11 操作系统的测试示例



让我们面对现实吧，这些测试很难解释，我们不会在 Nmap 入门教程中尝试深入理解它们。如果你想深入了解，包含这些信息的文件是 `/usr/share/nmap/nmap-os-db`。



不过，您需要注意的是，操作系统检测更多是 Nmap 确定的概率，而不是确定性。



### VI.结论



在本节中，我们学习了如何使用 Nmap 的选项来检测扫描主机和服务的技术、版本和操作系统。现在我们已经很好地理解了 Nmap 如何远程获取这些信息。我们还查看了管理冗长度和测试准确性的选项，以及工具在这些方面的限制。



下一节，我们将学习如何使用 Nmap 的 NSE 脚本对信息系统进行安全分析。如果需要，请花时间重读上一节内容，并且不要犹豫，亲自实践和深入研究该工具，以便更好地掌握我们迄今为止所学到的知识。




## 7 - 安全分析：检测漏洞



### I.介绍



在本节中，我们将学习如何使用 Nmap 网络扫描工具来检测和分析扫描目标上的漏洞。特别是，我们将了解完成此任务的各种可用选项，并研究该工具的功能限制，以便更好地理解和解释其结果。



在第一节中，我们将了解 Nmap 的漏洞扫描器，以及如何使用基本的漏洞检测选项。在接下来的章节中，我们将进一步了解该功能的工作原理，以及如何对其进行定制。



### II.使用 Nmap 检测漏洞



我们现在要使用 Nmap 网络扫描仪来检测信息系统服务和系统中的漏洞。这意味着，除了发现活动主机、列举暴露的服务以及检测版本和技术外，Nmap 还将查找漏洞。



为实现这一目标，Nmap 依赖于 NSE（_Nmap 脚本引擎_）脚本，这些脚本可视为模块，可实现细粒度的测试方法。



有了正确的选项，我们就可以让 Nmap 在发现的每个服务上使用各种 NSE 脚本，从而发现 .NET 服务：





- 配置故障 ；





- 发现更多更先进的版本和操作系统；





- 已知漏洞 (CVE) ；





- 弱标识符 ；





- 恶意软件感染的特征 Elements ；





- 拒绝服务的可能性 ；





- 等等。




如您所见，NSE 脚本大大扩展了 Nmap 的网络操作能力。它可以执行比以往更高级的任务。好消息是，像往常一样，这些功能可以通过选项在默认情况下使用。这就是我们接下来要看到的。



### III.漏洞扫描示例



使用 Nmap 扫描主机上的单个端口、该主机上的所有服务或多个网络上检测到的所有服务时，都可以使用 NSE 脚本。因此，我们可以在迄今为止学习过的所有情况下使用我们将要看到的选项。



要通过 Nmap 扫描启用漏洞扫描，我们需要使用 `-sC` 选项：



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



请记住，默认情况下，如果您不指定任何内容，Nmap 将只扫描 1000 个最常见的端口。它不会检测目标可能暴露的更特殊端口上的漏洞。



在生产信息系统中使用此功能之前，请继续阅读本教程。在接下来的章节中，我们将了解如何更好地控制运行测试的影响和类型。



例如，通过重复使用以前学到的知识，我们可以更全面地扫描目标的所有 TCP 端口：



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



下面是使用 NSE 脚本进行 Nmap 扫描的结果：



![nmap-image](assets/fr/40.webp)



通过 Nmap._ 对主机进行漏洞扫描的结果示例



在这里，我们可以看到在漏洞分析中显示的其他相关信息：





- FTP 服务可以匿名访问，不受身份验证保护。负责验证的 NSE 脚本告诉了我们这一点，甚至还显示了 FTP 服务的部分树形结构。在这里我们可以看到，我们可以访问 Windows 系统的 `C` 目录！





- 负责高级网络服务检索的 NSE 脚本会显示页面标题，让我们更好地了解网络服务的托管内容。





- 我们还对 SMB 服务配置（脚本 "smb2-time"、"smb-security-mode "和 "smb2-security-mode"）进行了小型分析。这些信息在网络扫描结果之后以不同的方式显示，以便于阅读。特别是，该信息显示没有 SMB Exchange 签名。这一配置弱点允许在 SMB 中继攻击中使用目标，而这是入侵/网络攻击测试中经常被利用的一个显著安全漏洞。




当然，这只是一个例子。Nmap 为许多服务提供了 NSE 脚本，可针对各种漏洞。我们将在下一节详细介绍这些可能性。



作为漏洞扫描介绍的结尾，这里有一个用于网络发现、TCP 端口扫描、版本和漏洞检测的完整命令：



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



下面的命令看起来更像是 Nmap 的实际用例！



### IV.了解 Nmap 在漏洞扫描方面的局限性



让我们明确一点：Nmap 无法对信息系统进行完整的渗透测试，也无法模拟红队行动。如果您不想产生虚假的安全感，就必须了解它的一些局限性：





- 覆盖范围有限**：尽管 Nmap 的 NSE 脚本功能强大，但与其他专门的漏洞发现工具相比，其测试覆盖范围可能有限。可用的 NSE 脚本可能无法覆盖某些漏洞，如 Active Directory 漏洞、敏感数据暴露或更高级的网络应用程序漏洞。





- 漏洞复杂性**：某些类型的漏洞可能因其复杂性而很难用 NSE 脚本检测到。例如，需要与远程服务进行复杂交互的漏洞可能无法被 Nmap 有效检测到（如文件共享中的过大权限或网络应用程序中的权限控制漏洞）。





- 被动检测**：Nmap 主要通过主动扫描来检测漏洞，这意味着如果不与目标主机建立主动连接，它可能无法有效地检测潜在漏洞。因此，在主动扫描过程中没有表现出来的漏洞可能会被遗漏（如网络应用程序中的代码注入）。





- 依赖更新**：Nmap的NSE脚本[数据库](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/)在不断发展，但在发现新漏洞和向Nmap添加相应脚本之间可能会有延迟。因此，Nmap 可能并不总是最新的漏洞。





- 假阳性和假阴性**：与任何安全工具一样，Nmap 的 NSE 脚本可能产生假阳性（错误的漏洞警报）或假阴性（未检测到的真实漏洞）。在分析 Nmap 结果时要注意这一点。




因此，了解 Nmap 做什么和不做什么以及如何解释其结果非常重要。特别是，我们在本教程中看到，默认选项可能会导致我们错过重要的 Elements，而仔细使用是可以发现这些问题的。



无论您是网络系统管理员、安全工程师还是 CISO，使用 Nmap 都能让您对信息系统的安全状况有一个总体了解。这是确保系统安全的重要第一步，可由 IT 团队定期执行。但是，它不应该取代[网络安全]专家 (https://www.it-connect.fr/cours-tutoriels/securite-informatique/) 的干预和建议，后者能比 Nmap 更全面地发现弱点。



### V.结论



在模块 3 的第一节，我们介绍了通过 Nmap 进行漏洞扫描。我们现在知道了如何使用主选项来执行这项任务，但也知道了这项工作的局限性。在下一节中，我们将使用 NSE 脚本更深入地了解这一功能，将 Nmap 的功能扩展十倍。



## 8 - 使用 Nmap 的 NSE 脚本



### I.介绍



在本节中，我们将深入了解 NSE（_Nmap 脚本引擎_）脚本。特别是，我们将了解为什么脚本是该工具的一大优势，脚本是如何工作的，以及如何浏览和使用许多现有脚本。



本节是上一教程的后续，在上一教程中我们学习了如何基本使用 Nmap 的漏洞扫描功能。现在我们将仔细研究 [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/)在这方面的工作原理，以便再次进行更精确、更可控的扫描。



### II.Nmap NSE 脚本的概念



Nmap 的 NSE 脚本允许您以高度灵活的方式扩展其功能。它们是用 LUA 编写的，这种脚本语言比 Nmap 使用的 C 或 C# 更易于处理和访问。在 Nmap 中使用 LUA 脚本而不是独立工具的好处是，它允许我们利用 Nmap 的执行速度和标准功能（主机、端口和版本发现等）。



这些脚本按类别编排，一个脚本可能属于多个类别：



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


从技术上讲，脚本所属的类别直接在其代码中标明。



![nmap-image](assets/fr/41.webp)



nSE 脚本类别 `ftp-anon`._



该示例显示了 NSE 脚本 `ftp-anon.nse` 的部分代码，我们在上一节看到了该脚本的执行过程。



### III.列出现有的 NSE 脚本



默认情况下，Nmap 的 NSE 脚本位于 `/usr/share/nmap/scripts/` 目录中，没有特定的树形结构或层次。下面是该目录的内容概览：



![nmap-image](assets/fr/42.webp)



提取包含 NSE 脚本的 `/usr/share/nmap/scripts/` 目录的内容。



该目录包含 5000 多个 NSE 脚本。在大多数情况下，脚本名称的第一部分包含脚本所属的协议或类别。这样我们就可以对列表进行排序，例如，如果我们想列出所有针对 FTP 服务的脚本，就可以这样做：



![nmap-image](assets/fr/43.webp)



名称以 `ftp-`._ 开头的 NSE Nmap 脚本列表



Nmap 并没有提供浏览和列出 NSE 脚本的选项；您可以使用命令 `-script-help`，后面跟一个类别的名称或一个单词：



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



不过，输出结果将是每个脚本的名称及其描述，如果搜索出几十个脚本，就不是最佳结果了：



![nmap-image](assets/fr/44.webp)



使用 Nmap 的 `--script-help` 命令的结果



我认为，最有效的方法是使用 `/usr/share/nmap/scripts/` 目录中的经典 Linux 命令：



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



请随意浏览您感兴趣的模块代码，以便更好地了解 NSE 脚本的工作原理。



### IV.使用 Nmap 的 NSE 脚本



现在，我们将学习如何通过仔细选择我们感兴趣的 NSE 脚本来执行漏洞扫描。



#### A.按类别选择脚本



首先，我们可以选择执行属于特定类别的所有脚本。我们需要用参数 `-script <category>` 向 Nmap 指明这个类别或这些类别：



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



第一个命令相当于 `nmap -sC` 命令。默认情况下，Nmap 会选择 `default` 类别中的脚本，但这只是为了便于论证。例如，下一条命令将使用 `discovery` 类别中的所有脚本：



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



正如我们所看到的，一些类别可以让我们快速识别相关 NSE 脚本的作用（"发现"、"漏洞"、"漏洞利用"），而其他类别则定义了所执行测试的风险、检测或稳定性级别。如果我们处于敏感环境中，对脚本选择所执行的不同操作没有很好的把握，我们可以选择合并选择，只选择那些属于 "发现 "和 "安全 "类别的脚本：



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



如果您绝对并明确地希望将脚本排除在 `dos` 和 `intrusive` 类别之外，可以使用以下符号：



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



请注意，上述排除条件将导致使用所有其他未明确排除的类别。为了更公平起见，我们可以举例说明：



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



下面是一些按类别处理 NSE 脚本的示例，尤其是在实际环境中使用 Nmap 进行漏洞分析时。



#### B.选择脚本作为一个单元



我们还可以选择在分析过程中执行单个特定测试，即与 NSE 脚本相对应的测试。为此，我们需要在 `-script <name>` 参数中指定脚本名称。以 `ftp-anon.nse` 脚本为例：



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



这样，我们就得到了一个非常精确的结果：



![nmap-image](assets/fr/45.webp)



通过 Nmap._ 在 FTP 端口上使用 NSE `ftp-anon` 脚本的结果



我们看到的是在端口 21 上运行 `ftp-anon` 脚本的结果，没有其他端口，因为我们指定了 `-p 21` 选项。我们也可以执行基本端口扫描，只在发现的 FTP 服务上执行 `ftp-anon` NSE 脚本：



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



因此，如果 Nmap 在另一个端口上发现了 FTP 服务，它也会执行这个匿名连接测试。



要了解 NSE 脚本的简要说明，可以使用上文提到的 `--script-help` 选项：



![nmap-image](assets/fr/46.webp)



帮助显示 NSE 脚本 `sshv1`._ 的结果



简而言之，我们可以再次重复使用迄今为止使用过的所有网络发现选项、服务、版本和技术！



#### C.管理脚本参数



在使用 Nmap 的过程中，您会遇到某些需要输入参数才能正常运行的 NSE 脚本。我们现在来看看如何通过 Nmap 的选项向这些脚本传递参数。



以 `ssh-brute` 脚本为例，它允许你对 SSH 服务进行暴力破解。



经典的暴力攻击包括测试多个密码（有时是数百万个），以尝试验证特定账户。通过尝试如此多的密码，攻击者赌的是用户使用了用于攻击的密码字典中的弱密码的概率。



该脚本有 "默认 "选项，我们可以根据实际情况进行定制。例如，在这次攻击中，我们可以向 Nmap 提供用户列表和要使用的密码字典。据我所知，不可能轻易列出脚本所需的参数，因此最可靠的方法是访问 Nmap 官方网站。通过 `--script-help` 选项可以直接链接到 NSE 脚本的文档：



![nmap-image](assets/fr/47.webp)



显示 NSE `ssh-brute` 脚本帮助并链接到 nmap.org._ 的结果



点击指定链接，我们就进入了网站 [https://nmap.org](https://nmap.org/) 的这个网页：



![nmap-image](assets/fr/48.webp)



可以传递给 Nmap 的 `ssh-brute` NSE 脚本的参数列表



这里我们可以清楚地看到可以使用的参数，在我们的上下文中主要是 `passdb`（包含密码列表的文件）和 `userdb`（包含用户列表的文件）。这里的文档指的是 Nmap 内部库，因为这些暴力破解机制和相关选项是互通的，可以在多个脚本（`ssh-brute`, `mysql-brute`, `mssql-brute`等）中统一使用，因此或多或少会有相同的参数：



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



在最后一条命令中可以看到，我们可以使用 `-scripts-args key=value,key=value` 选项为 Nmap 脚本指定必要的参数。下面是通过 `ssh-brute` NSE 脚本执行 SSH 强制时 Nmap 输出的可能结果：



![nmap-image](assets/fr/49.webp)



通过 Nmap._ 强制执行 SSH 的结果



如您所见，在交互式输出（终端输出）中，NSE 脚本生成的信息以 `NSE: [script name]` 为前缀，这样更容易找到。在通常的 Nmap 结果显示中，我们只需简要说明是否发现了弱标识符（包括密码，切记）。



为了更进一步，也为了提醒大家，除了我们已经介绍过的所有选项外，还可以使用以下命令：发现 "10.10.10.0/24 "网络，扫描 2000 个最常用的 TCP 端口，对 FTP 服务执行匿名访问搜索，对 SSH 服务执行暴力攻击：



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



这只是许多可用脚本及其选项中的一个例子。但我们现在对如何掌握 NSE 脚本、脚本是否需要参数以及如何将这些参数传递给 Nmap 有了更好的了解。



### V.结论



在本节中，我们学习了如何使用 Nmap 的 NSE 脚本来执行各种任务。我邀请您花点时间了解不同类别的脚本和脚本本身，看看它们能自动执行多少测试。



几节以来，我们已经积累了或多或少的高级发现、扫描和枚举选项。现在，你应该意识到 Nmap 的输出和结果显示开始变得相当广泛，有时甚至对我们的终端来说过于冗长。在下一节中，我们将学习如何掌握这些输出，特别是将其存储到各种格式的文件中。






## 9 - 管理 Nmap 输出数据




### I.介绍



在本节中，我们将看看 Nmap 产生的输出，特别是格式化输出的各种选项。我们将看到 Nmap 可以生成多种输出格式以满足不同需求，这也是该工具的一大优势。



默认情况下，Nmap 提供扫描和测试结果的详细视图。这包括扫描的主机和服务、检测到可访问的主机和服务、开放端口的具体情况、端口状态和版本。此外，终端输出中还提供了 NSE 脚本的详细信息。不过，即使信息格式清晰，这些输出也会很快变得浩如烟海，很难在结果中找到准确的信息。



### II.掌握 Nmap 输出格式



#### A.将扫描结果保存在文本文件中



为了方便起见，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 可以很容易地将输出保存为文本文件。这不仅有助于存档、与其他测试进行比较，还有助于使用专门的文字处理工具或脚本语言（如 Sublime text、[PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/)、Python、grep、sed 等）浏览这些输出。要将 Nmap 的标准输出存储在文本文件中，我们可以使用 `-oN <filename>` 选项（"normal "中的 "N"）：



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



这并不奇怪，因为 Nmap 会在我们的终端中显示其通常的标准输出，但也会在指定的文件中显示。



#### B.generate 浓缩格式的 Nmap 输出



在 "文本 "样式中还有第二种输出格式，可以很容易地被人类解读："可抓取 "格式。



创建这种格式的目的是提供 Nmap 输出的 "浓缩 "视图，其结构便于 `grep` 等工具处理。让我们来看看这类输出的一个示例：



![nmap-image](assets/fr/50.webp)



nmap 网络扫描，并以 "grepable "格式输出。



在这里，我对一个 /24 网络进行了网络发现、端口扫描以及技术和版本分析，然后将输出结果以 "可抓取 "格式存储在一个文件中。最后，我得到了一个文件，其中每个活动主机包含 2 行内容：





- 第一行告诉我，这样或那样的主机已_Up_；





- 第二行告诉我扫描了哪些端口，它们的状态以及以非常特殊的格式检索到的技术和版本信息：端口>/<状态>/<协议>/<服务>/<版本>/,"。




这种带有固定分隔符的格式允许文字处理工具（如 `grep`）或脚本和编程语言进行快速处理。例如，如果 Nmap 执行的扫描量很大，输出结果很难浏览，使用下面的命令就可以轻松检索到主机 `10.10.10.5` 的信息：



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



反之，我也可以轻松列出所有开放 21 端口的主机，因为端口和 IP 位于同一行：



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



要 generate 这样的输出，我们需要使用 `-oG <filename>.gnmap` 选项（"grep "中的 "G"）。根据习惯，我在这里使用`.gnmap`扩展名来表示这样的文件，但也可以随意使用你喜欢的扩展名：



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



这种格式有多种用途，尤其适用于快速脚本编写/排序。不过，这种格式正逐渐被放弃，转而使用我们接下来要介绍的格式。



注意：自 Nmap 7.90 起，`-oG` greppable 格式已被正式弃用。它仍可用于兼容目的。它仍可用于兼容性目的，但建议您使用 XML 或普通格式进行任何开发或自动解析。



#### C.Nmap 输出的 XML 格式



本教程中最后一种值得一提的格式是 XML。与前两种格式不同的是，这种格式不是设计给人阅读的，而是给其他工具或脚本阅读的。



XML（可扩展标记语言）是一种用于存储和传输数据的标记语言，通过自定义标记提供分层结构。



在 Nmap 中，XML 格式用于 generate 关于已执行扫描的详细报告，包括检测到的主机、端口和漏洞信息，以及标准 Nmap 输出中未显示的其他信息。



要 generate XML 格式的输出文件，我们需要使用 `-oX` 选项（"XML "中的 "O"）：



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



结果是终端中的 Nmap 标准输出，以及当前目录中的 XML 格式文件。



当然，XML 格式不是为人类阅读和解释而设计的。尽管如此，如果您想对这种格式的 Nmap 输出进行脚本编写或自动分析，您仍然需要对所使用的标记和结构有所了解。例如，下面是 Nmap 创建的 XML 文件的部分内容，其中显示了 1 台主机的扫描结果：



![nmap-image](assets/fr/51.webp)



Nmap 扫描期间 1 台主机的 XML 记录示例



这里有很多信息，我们对两个开放端口特别感兴趣：



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



我们知道，这种格式将有助于自动解析结果，因为每条信息都被整齐地排列在一个专用的、命名的标签或属性中。特别是，我们发现了一条以前从未遇到过的信息：CPE。



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



我们在模块 2 的第 2 节中简要提到了 CPE，该信息在版本检测时通过匹配来确定。Nmap 使用其服务、技术和版本检测机制来查找相关的 CPE。



这样，我们就可以在使用这些信息的数据库和应用程序中重复使用这些信息。我特别想到了引用 CVE 的 NVD 数据库。每个 CVE 都包含受该漏洞影响的 CPE。下面是 NVD 数据库中有关 `a:microsoft:internet_information_services:7.5` 的 CVE 示例：



![nmap-image](assets/fr/52.webp)



在 NVD 数据库中的 CVE 详情中存在 CPE



我们现在对这种格式的好处有了更好的了解，它提供了非常清晰的信息结构，并包含 Nmap 收集或处理的所有数据。



作为条件反射，我系统地同时以三种格式保存我的 Nmap 扫描。这是通过 `-oA <name>` 选项（"A "代表 "All"）实现的，它会创建一个 `<name>.nmap` 文件、一个 `<name>.xml` 文件和一个 `<name>.gnmap` 文件。这样，当我需要重新查看结果时，我就不会丢失任何东西了。



有了这三种格式，你就拥有了保存并最终以自动化方式处理 Nmap 结果所需的一切。我们将在下一节中再次使用 XML 格式，届时我们将了解如何将 Nmap 与其他安全工具结合使用。



#### III.从 Nmap 扫描生成 HTML 报告



XML 格式提供了许多可能性，尤其是可以作为生成 HTML 格式报告的基础，这样浏览起来会更直观。



要将 XML 格式的 Nmap 文件转换为网页，我们将使用 `xsltproc` 工具，首先需要安装该工具：



```
# Install the xsltproc tool
sudo apt install xsltproc
```



安装该工具后，只需向其提供要转换的 XML 文件和要生成的 HTML 报告名称即可：



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



这样，我们就能很好地安排整个扫描的结构，甚至在目录中加入一些颜色和可点击的链接！



![nmap-image](assets/fr/53.webp)



从 xsltproc._ 生成的 HTML 格式 Nmap 扫描报告中提取内容



概括地说，Nmap 保存的 XML 文件包含对另一个 XSL 格式文件的引用：



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



因此，转换为 HTML 是 Nmap 提供和促进的一项功能，"xsltproc "是执行这项任务的常用和公认的工具（它不属于 Nmap 工具套件）。



XSLT（可扩展样式表语言转换）是 XSL 的一个子集，可将 XML 数据显示在网页上，并与 XSL 样式并行 "转换 "为 HTML 格式的可读格式化信息。



来源：[helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



报告中的信息量相当于 Nmap 的 XML 格式，高于标准终端输出（_交互式输出_）。



### IV.管理 Nmap 的冗余级别



现在我们来看看 Debugger Nmap 或跟踪其进度的几个选项。



我们应该提到的第一个选项是 `-v` 选项，它可以增加 Nmap 的冗余度。下面是一个例子：



![nmap-image](assets/fr/54.webp)



使用 `-v`._选项查看 nmap 的冗余输出



在扫描许多主机和端口时，由于显示的信息太多，终端输出将变得难以利用。因此，该选项应与前面的选项结合使用，这些选项允许将 Nmap 的标准输出存储在一个文件中。与使用冗余度有关的信息不会包含在此输出文件中。从上面的示例中可以看出，这种冗余允许您清楚直接地跟踪 Nmap 的操作和发现。对于数据显示可能较慢的较长时间扫描，这可以避免对 Nmap 的当前活动视而不见，并知道事情的进展和速度。要进一步提高冗余度，可以使用 `-vv` 选项。



要进一步跟踪 Nmap 在扫描过程中的活动，可以使用 `--packet-trace` 选项。使用 `-v` 选项，我们会得到 Nmap 发现的所有开放端口的实时日志，而使用该选项，我们会得到发送到端口的每个数据包的日志行。这自然会产生非常冗长的输出，但可以详细监视 Nmap 的活动，下面是一个例子 ：



![nmap-image](assets/fr/55.webp)



通过`--packet-trace`._详细监控 Nmap 活动。



同样，如果使用了 `-oN`、`-oG`、`-oX` 或 `-oA` 选项，这些信息将不会记录在 Nmap 生成的输出文件中。



最后，Nmap 还提供两个调试选项：d "和 "dd"。这些选项的行为类似于 `-v` 冗余选项，但增加了额外的技术信息，如扫描开始时的技术参数摘要：



![nmap-image](assets/fr/56.webp)



时序选项在 Nmap 调试视图中显示



在接下来的几节中，我们将了解 "定时 "选项有哪些，以及为什么值得了解它们。



最后，如果只想获得 Nmap 扫描进度的基本合成概览，可以使用 `--stats-every 5s` 选项。这里的 "5s "指的是 5 秒，可以根据需要修改。这是我们从 Nmap 收到进度反馈的频率：



![nmap-image](assets/fr/57.webp)



Nmap的"--stats-every "选项显示的信息



特别是，我们可以获得进度百分比以及所处阶段的指示：通过 [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/)发现主机阶段、发现暴露的 TCP 端口阶段等。在扫描过程中按下 "回车键"，也可以在终端输出中获得这些信息。



不过，Nmap 并不擅长估计任务需要多长时间，尤其是因为它事先不知道要扫描多少主机和服务。



### V.结论



在本节中，我们研究了许多将 Nmap 扫描结果保存为不同文件格式的选项。这将非常有用，因为在实际情况下，扫描结果可能会占几百甚至几千行！我们还了解了如何为调试目的或获取扫描进度报告而增加 Nmap 的冗余级别。



XML 格式在下一节将特别有用，我们将在这一节介绍一些可以处理 Nmap 结果的工具。




## 10 - 将 Nmap 与其他安全工具结合使用



### I.介绍



在本节中，我们将介绍 Nmap 与其他免费开源安全工具的一些经典用法。特别是，我们将利用前面几节学到的知识进一步增强 Nmap 的功能和效率。



将 Nmap 扫描结果保存为 XML 的功能使数据与许多其他工具兼容。如今，几乎所有编程和脚本语言都有能够解析 XML 的库，这使得处理这些数据变得更加容易。许多工具，尤其是那些针对攻击性安全的工具，都有处理 Nmap 生成的 XML 格式的功能。让我们仔细看看。



我将提及一些进攻性工具，但并不详细说明它们的使用方法和工作原理。我假定读者熟悉这些工具的基本用法，而且它们已经投入使用。网络安全]专业人士 (https://www.it-connect.fr/cours-tutoriels/securite-informatique/)、正在接受培训的人员或决定深入研究这一主题的人员会对本节内容特别感兴趣。



### II.将 Nmap 结果导入 Metasploit



我们要了解的第一个在进攻性安全和漏洞研究中重用 Nmap 数据的工具是 Metasploit。



Metasploit 是一个漏洞利用和攻击框架。它是一个免费的解决方案和公认的工具，包含大量用 Ruby 或 Python 编写的模块。通过这些模块，可以利用漏洞、实施攻击、生成后门、管理回调（C&C 或通信与控制功能）并统一使用所有功能。



特别是，这个广为人知、使用广泛的运行框架可以与 postgreSQL [数据库](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) 配合使用，其中存储了主机、端口、服务、身份验证信息等。





- Metasploit 官方文档：[https://docs.metasploit.com/](https://docs.metasploit.com/)




这就是 Nmap 及其输出发挥作用的地方，因为 Nmap 输出的 XML 格式可以很容易地导入 Metasploit 的数据库，以填充其主机和服务数据库，然后可以迅速指定这些主机和服务为这次或那次攻击的目标。



进入 Metasploit 交互式 shell 后，我首先要创建一个工作区，一种专属于我当天环境的空间：



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



创建工作区后，我们需要验证与数据库的通信是否正常：



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



最后，我们可以使用 Metasploit `db_import` 命令以 XML 格式导入我们的 Nmap 扫描：



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



下面是执行所有这些命令的结果：



![nmap-image](assets/fr/58.webp)



将 XML 格式的 Nmap 扫描导入 Metasploit 数据库



在这里，你可以看到每台主机及其服务都已导入。然后，可以通过命令 `services` 或 `services -p <port>` 显示特定服务的数据：



![nmap-image](assets/fr/59.webp)



从 XML 文件导入 Metasploit 数据库的服务列表



最后，有了 `-R` 选项，我们就可以在模块中快速、轻松地重复使用这些数据。该选项将 "转换 "作为 `RHOSTS` 指令输入的服务列表，而 `RHOSTS` 指令则用于指定要实施攻击的目标。下面是一个使用 `ssh_login` 模块的示例，通过该模块可以对 [SSH] 服务进行暴力攻击 (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/)：



![nmap-image](assets/fr/60.webp)



使用 `services -R` 选项导入指定为攻击目标的服务



这只是在 Metasploit 中使用 Nmap 数据的一个小例子，但它让你略微了解到作为渗透测试、漏洞扫描或网络攻击的一部分，这些信息可以多么快速、轻松地重复使用。值得一提的是，Nmap 可以直接从 Metasploit 运行，将结果导入数据库（命令 `db_nmap`），这是另一个有趣的话题！



### III.将 Nmap 与 Aquatone 网络扫描仪配合使用



在本节关于重用 Nmap 结果进行攻击性安全和漏洞分析的部分，我想介绍的第二个工具是 Aquatone。



Aquatone 是一款网络扫描仪，设计用于有效探索网络上的网络应用程序。它提供先进的网络服务发现、子域识别、端口分析和网络应用指纹识别功能。所有功能都以 HTML、JSON 和文本报告的形式简明扼要地呈现，便于进行网络安全分析。



与 Metasploit 一样，Aquatone 可以直接处理 Nmap 的 XML 格式，并将其用作扫描目标。特别是，它可以从 Nmap 报告可能包含的所有数据中只提取感兴趣的主机和服务（网络服务）。





- 工具链接：[Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




要在 Aquatone 中使用 Nmap 的 XML 输出，只需将 XML 文件通过管道发送给 Aquatone 即可。下面是一个示例：



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Aquatone 通常在主机上执行端口发现以查找网络服务，而在这种情况下，它将完全依赖 Nmap 的结果，因为 Nmap 已经执行了这一操作，从而节省了时间：



![nmap-image](assets/fr/61.webp)



使用 XML 格式的 Nmap 结果与 `aquatone`._



以下是 Aquatone 报告的摘要，供您参考：



![nmap-image](assets/fr/62.webp)



报告示例



就我个人而言，我经常使用 Aquatone 快速了解网络上的网站类型，这主要归功于它的屏幕截图功能。



同样，拥有 XML 格式的完整 Nmap 报告可以节省时间，并便于在其他工具中重复使用。



### IV.结论



这两个例子清楚地表明，Nmap 的 XML 格式使其他工具可以很容易地使用其结果，因为它是一种结构化的、易于使用的数据格式。还有许多其他工具能够处理这些结果，如自动报告工具、图形表示法或更复杂的专有漏洞扫描仪。



当然，您也可以使用 Python、[PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) 或任何其他具有 XML 解析库的语言开发自己的脚本和工具，以便根据需要操作和重用 Nmap 结果数据。



本节将结束 Nmap 高级使用教程模块，特别是通过 NSE 脚本进行漏洞扫描。



本教程的下一部分将重点介绍 Nmap 可以执行的特定扫描的一些额外的、技术性更强的最佳实践和技巧。我们还将了解扫描性能优化选项，这些选项在扫描大型网络时特别有用。




## 11 - 提高网络扫描性能



### I.介绍



在本章中，我们将学习如何通过使用各种特定选项来优化使用 Nmap 执行网络扫描的速度。特别是，我们将进一步了解 Nmap 的内部工作原理，从 _timeout_ 管理到工具的预存配置。



既然我们已经充分了解了 Nmap 的功能，那就让我们来了解一下它的威力吧。如果你曾在大型网络中使用过该工具，你可能会注意到，尽管该工具功能强大，但有些扫描却需要很长时间。这是有道理的：一个简单的 `nmap` 命令加上几个选项就能 generate 数以百万计的数据包，目标是成千上万的潜在系统和服务。



更有甚者，某些网络设备配置可能会有意降低传输速率（每秒数据包数量），从而有可能出于安全原因拒绝您的数据包或禁止您的 IP Address。



根据具体情况，可能值得尝试优化所有这些，我们将在本章中看到这一点。



在任何情况下，你都可以通过 Nmap 调试（选项 `-d`，见上一章）检查我们将要查看的参数的默认值，以及你将要使用的选项是否被正确考虑：



![nmap-image](assets/fr/63.webp)



通过 Nmap 的 `-d` 选项查看定时选项。



### II.管理 Nmap 扫描的速度



#### A.管理并行化



默认情况下，Nmap 在扫描中使用并行化来优化扫描，它使用的所有参数都可以通过各种选项修改。不过，实际需要修改这些参数的情况非常罕见，所以我们不会在本教程中详细介绍：





- min-hostgroup/max-hostgroup<size>：并行主机扫描组的大小。





- `--min-parallelism/max-parallelism <numprobes>`：探针的并行化。





- scan-delay/-max-scan-delay<time>： 调整探测器之间的延迟。




只要知道它们存在并可以使用就可以了。



#### B.管理每秒数据包数量



默认情况下，Nmap 本身会根据网络响应调整每秒发送的数据包数量。但可以通过定义每秒数据包数的最高值和/或最低值来强制设置。可以使用选项 `--min-rate<number>`和 `-max-rate<number>`进行设置，其中 `number` 代表每秒的数据包数量。例如



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



这些选项允许你根据具体需要调整扫描速度，要么加快扫描过程，要么限制所使用的带宽。后一种情况（限制扫描速度）最有可能让你使用这些选项，尤其是在使用 Nmap 时遇到网络延迟的情况下（这种情况很少见）。



### III.管理连接失败和超时



我们可以使用另一个参数来优化 Nmap 扫描的速度（或保证更高的准确性），这就是 _timeout_ 和 _retry_。



对于 _timeouts_，这是**无响应超时**，Nmap 将停止等待响应并认为服务或主机不可达。对于 _retry_（重试），这是 Nmap 在继续执行操作前**连续尝试操作的次数。



与并行化一样，超时和重试管理也可应用于主机或服务发现阶段：





- min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>：指定 Exchange 的往返时间。同样，该参数实际上是在扫描过程中即时计算和调整的。您不太可能需要使用它，因为 Nmap 会根据网络反应即时计算该时间。





- `-max-retries <number>`：限制端口扫描时数据包重传的次数。默认情况下，Nmap 可以对单个服务进行多达 10 次重试，特别是在发现网络层延迟或丢失的情况下，但大多数情况下只进行一次重试。





- `--host-timeout <time>`：指定 Nmap 在一台主机上进行所有操作的最长时间，包括端口扫描、服务检测以及与该主机有关的任何其他操作。如果超过这个时间间隔而没有任何响应或**完成操作**，Nmap 将放弃该主机而不显示任何相关结果，并转到列表中的下一个主机。这允许您控制 Nmap 在给定主机上花费的最长时间，避免在顽固主机上卡住，优化整体扫描时间。




在日常工作中，我使用"--max-retries "和"--host-timeout "选项来优化扫描：



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



这些参数为根据特定需求和网络条件调整扫描行为提供了额外的灵活性。不过，您需要注意这些参数对扫描主机负载和潜在准确性损失的影响。



### IV.使用准备好的配置



我们在本章中看到的各种选项可以单独使用，也可以作为Nmap提供的现成配置的一部分。启用这些_templates_（配置模板）的选项是 `-T <number>` 或 `-T <name>`。有 5 个可用的 _templates_ 级别：



```
-T<0-5>: Set timing template (higher is faster)
```



默认情况下，Nmap 使用 _template_ 3 (_normal_)，这通常就足够了。



就我而言，我通常在需要相当快（同时尽可能完整）的情况下工作，我经常使用 `-T4` 选项。



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



下面是这次扫描的调试信息：



![nmap-image](assets/fr/64.webp)



在 Nmap 扫描期间使用 `-T4` 设置



### V.结论



在本章中，我们介绍了可以用来管理 Nmap 的功能、攻击性和性能的各种技术和选项。这些选项在扫描大型网络时特别有用，在隐身情况下则更为罕见。



下一章，我们将介绍一些使用 Nmap 并确保其安全性的最佳实践。




## 12 - 使用 Nmap 时的数据安全性和保密性



### I.介绍



在本章中，我们将介绍一些有关 Nmap 生成、处理和存储数据的安全性，尤其是保密性的良好做法。



在信息系统中使用 Nmap 很快就会被归类为攻击行为。因此，需要采取一系列预防措施，以便在法律框架内行事，同时保证预定目标、收集的数据和用于扫描的系统的安全。



### II.获得适当授权



在扫描网络或系统之前，请确保您已获得适当授权。未经授权扫描系统漏洞（"NSE 脚本"）可能是非法的，并可能产生法律后果，特别是如果信息系统安全不属于您的正式职权范围。





- 作为提醒：[刑法典：第三章：攻击自动数据处理系统](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III.保护敏感数据



Nmap 生成的结果可被视为敏感信息，尤其是当这些结果包含信息系统中可能被攻击者利用的弱点信息时。但当这些结果涉及并非所有人都能访问的系统（如敏感、工业、医疗保健或[备份]信息系统 (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)）时，也同样如此。



我们还看到，根据所使用的 NSE 脚本，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 的 NSE 扫描结果也可能包含标识符。



因此，恶意人员如果设法获取这些扫描结果，就会掌握信息系统的地图和大量技术信息，而无需亲自执行这些操作，否则就有可能被发现。



因此，在使用 Nmap 时必须注意不要不适当地收集或存储敏感信息，包括但不限于以下信息：





- 加密输出数据：如果需要存储或传输 Nmap 扫描结果，请务必加密以保护数据机密性。这将防止未经授权截获敏感信息。理想情况下，数据一离开用于执行扫描的系统就应加密（用强密码加密的 ZIP 压缩包是一个很好的开始）。





- 设置访问控制：确保只有经过授权的人才能访问 Nmap 扫描结果，并将其存储在那里。设置适当的访问控制，以保护敏感信息免遭未经授权的访问。





- 处理数据时保持警惕：在传输、复制或处理扫描数据时，确保严格控制数据安全。这意味着：不要把它们随意放在连接到互联网的工作站的 "下载 "目录中，不要让它们通过内部 HTTP 文件 Exchange 应用程序传输，不要在午休时打开记事本而不锁定工作站，等等。




### IV.处理侵袭性扫描



正如我们在本教程中所看到的，Nmap 在网络层可以非常啰嗦。它还可以发送格式不正确的数据包，在生成的网络帧和数据包中不严格遵守协议结构。所有这些行为都会对某些系统和服务造成影响，有时甚至会导致系统和网络资源失灵或饱和。



为了避免任何事故，您需要掌握 Nmap 的行为，并知道如何通过本教程中讨论的各种选项使其适应使用环境。在包含工业[硬件](https://www.it-connect.fr/actualites/actu-materiel/)的信息系统中，我们使用Nmap的方式不一定与在由受本地防火墙保护的Windows系统组成的用户网络或网络核心中使用Nmap的方式相同。



希望本教程中的各种课程已教会您如何掌握和分析 Nmap 的行为，但最好的学习方法是边做边学。因此，请确保您熟悉将要使用的 Nmap 选项。



### V.保护扫描系统



在第一章中，我们看到在大多数情况下，Nmap需要以 "root "或本地管理员的身份运行。这是因为它通过网络库执行网络操作，有时是在相当低的级别上，从系统稳定性或其他应用程序的保密性的角度来看，这些操作需要很高的风险权限。



因此，Nmap 可被视为安装系统的敏感组件。请确保使用最新版本的 Nmap，因为旧版本可能包含已知的安全漏洞。通过使用最新版本，可以最大限度地降低与使用该工具相关的风险。



如果你选择不以`root`身份通过会话使用Nmap，而是授予特权用户特定的权限，使他拥有使用Nmap所需的一切（`sudo`或_capabilities_），请注意Nmap可以作为完整的权限提升的一部分：



![nmap-image](assets/fr/65.webp)



通过 `sudo`._ 提升 Nmap 权限



在这里，我通过 `sudo` 使用 Nmap 命令，但这允许我在系统上以 `root` 的身份获得一个交互式 shell，而这并不是最初的目标。



在不是为执行网络扫描而设计的系统上安装 Nmap 也是非常不可取的。我特别想到服务器或工作站。一方面，这会增加权限提升的潜在途径，但最重要的是，它会让攻击者毫不费力地获得攻击工具。



最后，用于扫描的系统的安全性必须得到更广泛的保证，使其本身不会成为入侵或信息泄漏的媒介。作为系统管理员，最好使用专用系统，最好是有使用寿命限制的系统，而不是自己的工作站。



### VI.结论



总之，在实际或生产条件下使用 Nmap 之前，请确保您已正确掌握它，并在处理和管理其结果时保持警惕。如果最初的目的是提高公司的安全性，但却造成了损失、泄露了数据或助长了漏洞，那就太可惜了。



## 13 - 通过 TCP 进行端口扫描：SYN、连接和 FIN



### I.介绍



在本章和下一章中，我们将仔细研究 Nmap 中可用的不同类型的 TCP 扫描，从最常用的开始：SYN、Connect 和 FIN 扫描。



您可能已经注意到，Nmap 为 TCP 扫描提供了多个选项：



![nmap-image](assets/fr/66.webp)



Nmap._ 中提供的扫描技术。



这里的目的是解释其中的一些方法，帮助您了解它们的区别、优势和局限性。您会发现，根据具体情况或您想要了解的内容，选择一种或另一种方法会更好。



### II.TCP SYN 扫描或 "半开扫描



我们要看的第一种 TCP 扫描是 "TCP SYN Scan"，也称为 "Half Open Scan"。如果你还记得我们在第一次端口扫描后进行的网络扫描，这就是 [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/)以 root 权限运行时默认使用的扫描类型。



翻译将有助于您理解这种扫描的工作原理。事实上，TCP SYN 扫描会向每个目标端口发送一个 TCP SYN 数据包，这是客户端（请求建立连接的客户端）发送的第一个数据包，是著名的 "三方握手 "TCP 的一部分。通常情况下，如果目标服务器上的端口是开放的，并且后面有服务在运行，服务器就会发回一个 TCP SYN/ACK 数据包，以验证客户端的 SYN 并初始化 TCP 连接。该响应以 SYN 和 ACK 标志设为 1 的 TCP 数据包的形式出现，使我们能够确认端口已打开并连接到服务。



另一方面，如果端口被关闭，服务器将向我们发送一个 RST 和 ACK 标志设为 1 的 `TCP` 数据包，以终止连接请求，这样我们就知道这个端口后面似乎没有服务在运行：



![nmap-image](assets/fr/67.webp)



打开和关闭端口的 tCP SYN 扫描行为图



为了更具体地了解 "TCP SYN Scan"，我对 TCP/80 端口进行了扫描，该端口上有一台活动的网络服务器。使用 Wireshark 进行网络扫描后，我们可以看到以下流量（扫描源：`10.10.14.84`）：



![nmap-image](assets/fr/68.webp)



在 TCP SYN 扫描开放端口时进行网络捕获



在第一行，我们看到扫描源正在向 TCP/80 端口上的主机 "10.10.10.203 "发送一个 TCP 数据包。在这个 TCP 数据包中，SYN 标志被设置为 1，表示这是一个 TCP 连接初始化请求。



然后，在第二行中，我们看到目标回应了 "TCP SYN/ACK"，这意味着它接受初始化连接，因此可以接收 TCP/80 端口上的数据流。因此，我们可以推断出 TCP/80 端口是开放的，扫描的服务器上有网络服务器。



然后，我们的主机会发回一个 RST 数据包关闭连接，使被扫描主机不再保持开放的 TCP 连接等待响应。在扫描许多端口的情况下，不关闭 TCP 连接可能会导致拒绝服务，使服务器可维持的等待响应的连接数量达到饱和（参见 [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



在 Wireshark 中，您可以查看我们执行的每个测试的 TCP 标志状态。这将显示数据包是否为 SYN、SYN/ACK、ACK 等数据包：



![nmap-image](assets/fr/69.webp)



在 Wireshark 中查看数据包的 TCP 标志（此处为 TCP SYN）



相反，我在两台机器之间进行了相同的测试，但这次扫描的是一个没有服务活动的 TCP/81 端口（扫描源：`10.10.14.84`）：



![nmap-image](assets/fr/70.webp)



在 TCP SYN 扫描关闭端口期间进行网络捕获



当端口未打开时，被扫描的主机会响应我的 "TCP SYN"，返回一个 "TCP RST/ACK"。



如前所述，从特权终端运行 Nmap 时，TCP SYN 扫描是默认模式，可以通过 `-sS` (`scan SYN`) 选项强制执行：



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




出于速度考虑，"TCP SYN 扫描 "是最常用的扫描方式。另一方面，如果在一台服务器上或从网络上的同一来源观察到太多次客户端未能完成三方握手（即在服务器 SYN/ACK 之后未发送 ACK）的情况，就会让人觉得可疑。事实上，客户端在收到响应 TCP SYN 的 TCP SYN/ACK 数据包后的正常行为是发送 "确认"（ACK），然后启动 Exchange。



尽管如此，它的扫描速度还是稍快一些，因为它不需要为每个肯定响应发送 ACK。SYN 扫描的优点是速度快，因为每个要扫描的端口只需发送一个数据包，但代价是被检测到的机会更大。



此外，TCP SYN 扫描还能检测端口是否被防火墙过滤（保护）。事实上，目标主机前的防火墙在收到它应该保护的端口上的 TCP SYN 数据包时，可以通过其行为方式检测出来。防火墙根本不会响应。但是，正如我们所看到的，在这两种情况下（开放或关闭端口），主机都会做出响应。这第三种行为将揭示被扫描主机和运行扫描的机器之间是否存在防火墙。下面是 Nmap 在扫描端口被防火墙过滤时返回的结果：



![nmap-image](assets/fr/71.webp)



nmap 扫描已过滤端口时的显示



当我们在扫描时进行网络捕获时，实际上可以看到没有任何响应：



![nmap-image](assets/fr/72.webp)



在 TCP SYN 扫描期间对防火墙过滤的端口进行网络捕获



封闭端口和过滤端口的区别如下：过滤端口是受防火墙保护的端口，而封闭端口是没有服务运行的端口，因此无法处理我们的 TCP 数据包。某些类型的 TCP 扫描（如 TCP SYN 扫描）能够检测端口是否被过滤，而其他类型的扫描则不能。



### III.TCP 连接扫描或完全开放扫描



第二种 TCP 扫描是 "TCP 连接扫描"，也称为 "完全打开扫描"。它的工作方式与 TCP SYN 扫描相同，但这次是在服务器做出肯定响应（SYN/ACK）后返回一个 "TCP ACK"。这就是它被称为 "完全打开 "的原因，因为连接是完全打开的，并且是在扫描期间打开的每个端口上启动的，因此尊重了 TCP _Three Way Handshake_（三方握手）：



![nmap-image](assets/fr/73.webp)



打开和关闭端口的 tCP 连接扫描行为图



下面是针对开放端口进行 "TCP 连接扫描 "时可以看到的网络传输情况：



![nmap-image](assets/fr/74.webp)



在 TCP 连接扫描开放端口时进行网络嗅探



我们可以看到，客户端发送的第一个 TCP 数据包是 "TCP SYN"，然后服务器会回复一个 "TCP SYN/ACK"，表明端口是开放的，并且正在提供服务。为了全程模拟合法客户端，Nmap 会向服务器发送一个 `TCP ACK` 回文。相反，当扫描一个关闭的端口 ：



![nmap-image](assets/fr/75.webp)



在 TCP 连接扫描关闭端口期间进行网络捕获



请注意，服务器对我们的 `SYN` 数据包的响应再次是一个 `TCP RST/ACK` 数据包，因此我们可以推断出端口已关闭，没有服务在上面运行。



使用 Nmap 时，`-sT`（`scan Connect`）选项用于执行 TCP 连接扫描。请注意，在非特权会话中使用 Nmap 时，这是默认的 TCP 扫描模式：



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



TCP 连接扫描 "模拟的是更合法的连接请求，其行为与 lambda 客户端最为相似，因此在端口数量减少的情况下更难发现扫描。不过，它的速度较慢，因为它会在被扫描机器的开放端口上完全初始化每个 TCP 连接。



如果安装了网络入侵检测和保护服务（IDS、IPS、EDR），对 10,000 个端口进行 Nmap 扫描仍然很容易被检测到。当攻击者想保持低调时，他会倾向于关注少量战略性选择的端口，如 445（SMB）或 80（HTTP），这些端口通常在服务器上开放，存在常见漏洞。



由于 TCP Connect Scan 在这两种情况下都希望得到响应，因此它还能检测到目标主机上是否存在可能正在过滤端口的防火墙。



### IV.TCP FIN 扫描或 "隐形扫描



TCP FIN 扫描 "也称为 "隐形扫描"，它利用客户端终止 TCP 连接的行为来检测开放端口。



在 TCP 中，会话结束意味着发送 FIN 标志设为 1 的 TCP 数据包。在正常的 Exchange 中，服务器会停止与客户端的所有通信（无响应）。如果服务器与客户端没有活动的 TCP 连接，则会发送一个`RST/ACK`。因此，我们可以通过向一组端口发送 `TCP FIN` 数据包来区分开放端口和关闭端口：



![nmap-image](assets/fr/76.webp)



打开和关闭端口的 tCP FIN 扫描行为图



我再次在_隐形扫描_过程中捕获了网络，这就是当扫描端口打开时看到的情况：



![nmap-image](assets/fr/77.webp)



在 TCP FIN 扫描开放端口期间进行网络捕获



我们可以看到，客户端发送一到两个数据包来终止 TCP 连接，而服务器并不响应。它只是接受连接的结束并停止通信。



下面是我们现在扫描封闭端口时看到的情况：



![nmap-image](assets/fr/78.webp)



在 TCP FIN 扫描关闭端口期间进行网络捕获



我们看到服务器发回了一个 `TCP RST/ACK` 数据包，因此开放端口和关闭端口的行为是不同的，我们可以通过发送 TCP FIN 数据包来列出服务器上的开放端口。使用 Nmap，`-sF`（`scan FIN`）选项用于执行 TCP FIN 扫描：



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN 扫描无法在 Windows 主机上运行，因为当 TCP FIN 数据包发送到未开放的端口时，操作系统往往会忽略这些数据包。因此，如果在 Windows 主机上运行 TCP FIN 扫描，你会得到所有端口都已关闭的印象。



因此，熟悉几种扫描方法并了解它们之间的区别非常重要。



在这两种情况下，TCP FIN 都不会等待响应，因此无法检测目标主机和扫描源之间是否存在防火墙。



下面是 Nmap 的 TCP FIN 扫描结果示例：



![nmap-image](assets/fr/79.webp)



Nmap._ 进行 TCP FIN 扫描的结果。



事实上，主机对某个端口没有响应可能意味着该端口被过滤了，但也可能意味着该端口是开放和活动的。



这种扫描被称为 "隐形 "扫描，因为它不会产生大量 generate 流量，一般也不会导致目标系统出现日志记录。它可用于谨慎地发现网络上的端口，而不会引起任何警报。不过，如上所述，其有效性会因目标系统而异，其随意性也会因安全设备的配置而异。



### V.结论



关于 Nmap 提供的不同 TCP 扫描类型的两章中的第一章就讲到这里！在下一章中，我们将学习 XMAS、Null 和 ACK TCP 扫描类型，它们以不同的方式检测主机上的开放端口。





## 14 - 通过 TCP 进行端口扫描：XMAS、Null 和 ACK



### I.介绍



在本节中，我们将继续探索 Nmap 提供的各种 TCP 扫描方法。在这里，我们将学习 `XMAS`、`Null` 和 `ACK` 方法，它们使用 TCP 特有的功能来检索给定目标上打开的端口和服务的信息。



### II.TCP XMAS 扫描



XMAS Scan TCP 有点不寻常，因为它完全不模拟网络上正常的用户或机器行为。事实上，XMAS Scan 发送 TCP 数据包时会将 "URG"（紧急）、"PSH"（推送）和 "FIN"（完成）标志设为 1，以绕过某些防火墙或过滤机制。



之所以叫 XMAS，是因为看到这些标记打开是不寻常的。当 TCP 数据包中的三个标志同时设置时，看起来就像一棵点亮的圣诞树：



![nmap-image](assets/fr/80.webp)



XMAS 扫描中使用的 tCP 标志



这里不详细介绍这些标记的作用，但重要的是要知道，在发送启用了这三个标记的数据包时，目标端口后面的活动服务不会返回任何数据包。另一方面，如果端口关闭，我们将收到一个 TCP RST/ACK 数据包。现在，我们就能在列出机器上的端口时区分开放端口和关闭端口的行为了：



![nmap-image](assets/fr/81.webp)



打开和关闭端口的 tCP XMAS 扫描行为图



还是按照同样的逻辑，在检测到开放端口（扫描源 "10.10.14.84"）时，对一台有活动网络服务器的主机的 TCP/80 端口进行网络扫描，会显示以下行为：



![nmap-image](assets/fr/82.webp)



在 TCP XMAS 扫描开放端口时进行网络捕获



我们可以看到，扫描源向主机 `10.10.10.203`发送了两个 TCP XMAS 数据包（标记 `FIN`、`PSH` 和 `URG` 设为 1），目标没有返回，这表明端口是开放的。相反，当对一个关闭的端口执行 "TCP XMAS 扫描 "时，会观察到以下结果：



![nmap-image](assets/fr/83.webp)



在 TCP XMAS 扫描关闭端口期间进行网络捕获



然后，我们的 TCP 数据包会得到一个 `TCP RST/ACK`，表示端口已关闭。要在 Nmap 中使用这种技术，`-sX`（`scan XMAS`）选项允许您执行 TCP XMAS 扫描：



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



值得注意的是，与 TCP SYN 或 Connect 等其他类型的扫描不同，TCP XMAS 扫描无法检测目标与扫描计算机之间可能存在的防火墙。事实上，如果目标端口被过滤（即受防火墙保护），两台主机之间的活动防火墙将确保不会返回 TCP。因此，在没有响应的情况下，无法知道端口是受防火墙保护还是开放和活动的。您还应该注意，与 TCP FIN 扫描一样，某些应用程序或操作系统（如 Windows）可能会扭曲此类扫描的结果。



注意：最近版本的 Windows 对 XMAS/FIN/NULL 扫描的支持仍然有限，对此类目标的扫描结果可能不一致。(2025年更新)_



### III.TCP 空扫描



与 TCP XMAS 扫描相反，TCP Null 扫描会发送所有标志都设置为 0 的 TCP 扫描数据包。这也是机器间正常 Exchange 中永远不会出现的行为，因为在描述 TCP 协议的 RFC 中并没有规定发送不带标志的 TCP 数据包。这也是更容易被检测到的原因。



与 TCP XMAS 扫描一样，这种扫描也会干扰某些防火墙或过滤模块，使数据包通过：



![nmap-image](assets/fr/84.webp)



打开和关闭端口的 tCP 空扫描行为图



下面是在开放端口上进行 TCP 空扫描时网络上可以看到的情况：



![nmap-image](assets/fr/85.webp)



在 TCP Null 扫描开放端口时进行网络捕获



扫描机器发送一个无标记数据包（Wireshark 中为"[<None>]"），服务器不会作出任何回应。相反，当目标端口关闭 ：



![nmap-image](assets/fr/86.webp)



在 TCP Null 扫描关闭端口期间进行网络捕获



要使用 Nmap 执行 TCP Null 扫描，只需使用 `-sN` (`scan Null`) 选项：



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



由于端口开放时和防火墙激活时的响应（两种情况下都没有服务器反馈）完全相同，因此 TCP Null 扫描无法检测到防火墙的存在。更有甚者，防火墙甚至会伪造结果，暗示端口已打开，因为即使端口已被过滤，防火墙也不会响应没有标记的 TCP 数据包。在使用无法区分开放端口和受过滤（防火墙保护）端口的扫描（如 "TCP Null"、"XMAS "或 "FIN "扫描）时，需要注意这一重要信息，以便在解释所获结果时保持一致。



### IV.TCP ACK 扫描



TCP ACK 扫描用于检测目标主机上或目标与扫描源之间是否存在防火墙。



与其他扫描不同，TCP ACK 扫描并不试图识别主机上哪些端口是开放的，而是识别过滤系统是否处于活动状态，并对每个端口作出 "已过滤 "或 "未过滤 "的响应。有些 TCP 扫描（如 "TCP SYN "或 "TCP Connect"）可以同时进行这两种扫描，而有些 TCP 扫描（如 "TCP FIN "或 "TCP XMAS"）则根本无法确定是否存在过滤。这就是 TCP ACK 扫描有用的原因：



![nmap-image](assets/fr/87.webp)



已过滤和未过滤端口的 tCP ACK 扫描行为图



我们将使用 Nmap 的 `-sA` 选项来执行这种类型的扫描。下面是在端口被过滤（即被防火墙阻止和保护）的情况下进行 TCP ACK 扫描的结果：



![nmap-image](assets/fr/88.webp)



在 TCP ACK 扫描期间显示 nmap._



有防火墙和无防火墙主机的结果示例。Nmap 在主机 `10.10.10.203`的端口 TCP/80 和 TCP/81 上返回 "filtered"。通过 Wireshark 进行网络分析，结果如下：



![nmap-image](assets/fr/89.webp)



在 TCP ACK 扫描期间对未被防火墙过滤的端口进行网络捕获



如果存在防火墙，目标计算机不会返回任何信息。



要使用 Nmap 启动此扫描，请使用 `-sA`（`扫描 ACK`）选项：



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V.结论



除了已经介绍的方法外，我们还研究了三种不同的通过 TCP 进行扫描的方法。这些不同的方法将在非常特殊的条件和环境下使用，特别是在渗透测试或红队行动中，在这些情况下，需要谨慎行事。



## 15 - Nmap CheatSheet - 命令教程摘要



### I.介绍



以下是 Nmap 许多命令和用例的简短摘要，以便您在日常使用中快速找到并重复使用。



### II.Nmap：CheatSheet IT-Connect



下面是所介绍命令的小抄。本页可让您轻松找到 Nmap 最常用的用法。





- 端口扫描




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- 发现活动主机




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



注意："-sP "选项已过时多年，应改为"-sn"。(2025年更新)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- 版本检测




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE 脚本：寻找漏洞




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Nmap 输出管理




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- 性能优化




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP 扫描类型




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



希望这些命令对你有用。不要忘记根据具体情况调整扫描目标，并参考官方文档以全面掌握所执行的测试。



### III.结论



Nmap 教程现已完成。您现在已经掌握了使用这一全面而强大的工具所需的基础知识。我们强烈建议您在生产环境中使用前，先在受控环境（Hack The Box、VulnHub、虚拟机）中练习。



关于该工具的内部工作原理和高级功能，还有很多有待探索。不过，掌握这里介绍的命令和概念将使您能够自信地使用 Nmap，并使其具有实用性。