---
name: WireGuard
description: 在 Debian 和 Windows 上设置 WireGuard VPN
---
![cover](assets/cover.webp)



___



*本教程基于 Florian BURNEL 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。*



___



## I.介绍



在本教程中，我们将学习如何配置基于 WireGuard 的 VPN，这是一个免费的开源 VPN 解决方案，在提高性能的同时不会忽略安全性。



WireGuard 是一个相对较新的解决方案，自 2020 年 3 月起已作为稳定版本发布，并有幸自 5.6** 版本起直接集成到**Linux 内核中。这并不妨碍使用不同版本内核的旧版 Linux 发行版访问它。与 OpenVPN 和 IPSec 等解决方案相比，WireGuard 使用起来更简单，速度也更快，我们将在本文结尾看到这一点。



关于 WireGuard .NET 的一些要点





- 简单、轻便、高效！
- 仅通过 UDP 运行（这在穿越某些防火墙时可能是一个不利因素）
- 以点对点模式而非客户服务器模式运行
- 通过 Exchange 密钥进行身份验证，原理与使用私人/公共密钥的 SSH 相同
- 使用多种算法：ChaCha20 对称加密、Poly1305 信息验证以及 Curve25519、BLAKE2 和 SipHash24 等其他算法
- 支持 IPv4 和 IPv6
- 多平台：Windows、Linux、BSD、macOS、Android、iOS、OpenWRT（并在 ProtonVPN 中实施）
- 仅需 4,000 行代码，而其他解决方案则需要数十万行代码



在加密部分，所使用的各种算法都是经过精挑细选的，通过多种方式进行审核，并由该领域的专业安全研究人员进行检查。



项目官方网站：[wireguard.com](https://www.wireguard.com/)



看完这篇介绍，你是否对这一解决方案深信不疑？剩下的就是继续阅读了！



## II.实验室 WireGuard 图表



在介绍我设置 WireGuard 的实验室之前，你应该知道，你可以想象**使用 WireGuard 将两个远程基础设施**互联，也可以**将远程客户端与基础设施（如公司网络或家庭网络）**互联。这与 OpenVPN 的原理相同，正如我们最近在教程"[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/) "中看到的那样。



如果 WireGuard 没有直接设置在路由器或防火墙上（OpenWRT 可以做到这一点），则需要设置端口转发，以便流量到达 WireGuard 对。



![Image](assets/fr/034.webp)



现在我来介绍一下我的实验室，以及我们今天要建立的实验室。



我将使用 Debian 11 机器作为 WireGuard 服务器，使用 Windows 客户端作为 WireGuard VPN 客户端。虽然说客户-服务器关系有点误导，因为**WireGuard 采用的是 "点对点 "**模式。当你试图建立 "客户端到站点 "的连接时，这就有点名不副实了。比方说，我将有两对或**两个 WireGuard 连接点**（如果你愿意的话）：一个在 Debian 11 下，另一个在 Windows 下。



这两对设备可以双向通信，也就是说，从我的 Windows 机器可以访问 Debian 11 机器的远程局域网，反之亦然：这完全取决于隧道的配置和 WireGuard 对等设备的防火墙。



在本例中，我将重点讨论以下情况： **我想通过连接到家庭网络的 Windows Peer 1 访问公司网络，以便通过 WireGuard VPN 通道访问公司服务器**。如下图所示：



![Image](assets/fr/035.webp)



就 IP 地址而言，这给出了 ：





- 家庭网络： 192.168.1.0/24
- 公司网络：192.168.100.0/24
- **WireGuard 隧道网络**： 192.168.110.0/24


+ 隧道中对等设备 1（Windows）的 IP Address： 192.168.110.2/24


+ 隧道中 Peer 2（Debian）的 IP Address： 192.168.110.121/24



这就是全部内容！让我们开始配置吧！



**注：默认情况下，WireGuard 采用 UDP 模式，端口为 51820。**



## III WireGuard 服务器的安装和配置



在本教程中，我将使用 "客户端 "来表示 Windows 机器，而使用 "服务器 "来表示 Debian 机器，因为尽管这是点对点的，但似乎更有意义。



### A.在 Debian 11 上安装 WireGuard



WireGuard 安装包可在 Debian 11 官方软件仓库中找到，因此我们只需更新软件包缓存并安装即可：



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



将安装 WireGuard 服务器部分，同时还将安装各种工具，以便使用有用的命令来管理配置。



### B.安装 Interface WireGuard



使用 ** 命令 "wg "**，我们需要 generate 私钥和公钥：这对两对密钥（即服务器和客户端，客户端也需要一对密钥）之间的身份验证至关重要。



我们将使用此命令序列创建私钥 "**/etc/wireguard/wg-private.key**"和公钥 "**/etc/wireguard/wg-public.key**"：



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



控制台将返回公钥的值。在 WireGuard 配置文件中，我们需要**添加私钥的值**。要获取该值，请输入下面的命令并复制该值：



```
sudo cat /etc/wireguard/wg-private.key
```



现在是在 "**/etc/wireguard/**"中创建配置文件的时候了。例如，如果我们认为与 WireGuard 相关联的 Interface 网络将是 "wg0"，则可以将该文件命名为 "**wg0.conf**"，原理与 "eth0 "相同。



```
sudo nano /etc/wireguard/wg0.conf
```



在该文件中，我们必须首先添加以下内容（稍后再完成）：



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



[Interface]"部分用于声明服务器部分。下面是一些信息：





- **Address**：VPN 隧道内 Interface WireGuard 的 IP Address（与远程 LAN 不同的子网）
- **SaveConfig**：只要 Interface 处于活动状态，配置就会被保存（并受到保护）。
- **ListenPort**：WireGuard 的监听端口。在本例中，51820 是默认端口，但也欢迎自定义端口
- **PrivateKey**：服务器私钥的值 (*wg-private.key*)



保存文件并关闭。使用 "**wg-quick**"命令，我们可以指定 Interface 的名称（wg0，因为文件名为 wg0.conf）来启动它：



```
sudo wg-quick up wg0
```



如果列出 Debian 11 服务器的 IP 地址，就会看到一个名为 "wg0 "的新 Interface，配置文件中定义了 IP Address：



```
ip a
```



![Image](assets/fr/027.webp)



同样，我们也可以通过 "wg show "命令显示 Interface "wg0 "的配置：



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



最后，我们需要激活 Interface wg0 WireGuard 的自动启动功能：



```
sudo systemctl enable wg-quick@wg0.service
```



我们暂时不讨论 WireGuard 服务器端的配置。



### C.启用 IP 转发



为了让 Debian 11 机器能够在不同网络（如路由器）**之间**路由数据包，即在 VPN 网络和本地网络之间**路由数据包**，我们需要启用 [IP 转发](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/)。默认情况下，该功能是禁用的。



修改此配置文件 ：



```
sudo nano /etc/sysctl.conf
```



在文件末尾添加以下指令并保存：



```
net.ipv4.ip_forward = 1
```



仅此而已。



### D.启用 IP 伪装



为了让我们的服务器能正确路由数据包，并让 Windows 机器能访问远程局域网，我们需要在 Debian 服务器上激活 IP 伪装。这是一种 NAT 激活。我将通过 UFW 在 Linux 防火墙上执行此配置，我习惯使用 UFW（[ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)）。



如果您还没有 UFW 并想对其进行设置（也可以使用 Nftables），请先安装 .NET Framework 2.0：



```
sudo apt install ufw
```



首先，需要启用 SSH，以免失去对远程服务器的控制（调整端口号）：



```
sudo ufw allow 22/tcp
```



UDP 端口 51820 也必须经过授权，因为我们将其用于 WireGuard（再次调整端口号）：



```
sudo ufw allow 51820/udp
```



接下来，我们将继续配置以启用 IP 伪装。为此，我们需要获取连接到本地网络的 Interface 的名称。如果不知道名称，请运行 "ip a "查看网卡名称。在我的例子中，是 "**ens192**"网卡。



![Image](assets/fr/036.webp)



我们将使用这些信息。编辑以下文件：



```
sudo nano /etc/ufw/before.rules
```



在文件末尾添加这几行，以便在本地防火墙 NAT 表的 POSTROUTING 字符串中**启用 Interface ens192** 的 IP 伪装（修改 Interface 名称）：



```
# NAT - IP masquerade
*nat*
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



图片显示 ：



![Image](assets/fr/037.webp)



保持打开该配置文件，并进入下一步。



### E.WireGuard 的 Linux 防火墙配置



还是在同一个配置文件中，我们要声明公司网络 "192.168.100.0/24"，这样就可以与它联系了。下面是要添加的两条规则（最好在 "*# ok icmp code for FORWARD*"部分之后，以便将规则分组）：



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



如果只想授权一台主机，例如 "192.168.100.11"，也很容易：



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



现在可以保存文件并关闭。剩下的工作就是激活 UFW 并重启服务，以应用我们的更改：



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Debian 服务器配置的第一部分现已完成。



## IV.用于 Windows 的 WireGuard 客户端



WireGuard 客户端可用于 Windows、macOS、Android 等系统。这是一个好消息。本页面提供所有下载：[WireGuard 客户端](https://www.wireguard.com/install/)。在本例中，我将在 Windows 上设置客户端。要在 Linux 上设置 WireGuard 客户端，请遵循在 Debian 机器上创建 wg0.conf 文件的相同原则（不包括所有 NAT 等）。



### A.安装 WireGuard Windows 客户端



下载可执行文件或 MSI 软件包后，安装非常简单：只需启动安装程序，然后......瞧，安装完毕！ 🙂



![Image](assets/fr/038.webp)



### B.创建 WireGuard 配置文件



首先打开软件创建一个新隧道。为此，请单击 "**添加隧道**"按钮右侧的箭头，然后单击 "**添加空隧道**"按钮。



![Image](assets/fr/028.webp)



将打开一个配置窗口。每次创建新的隧道配置时，WireGuard 都会生成该配置专用的私钥/公钥对。**在此配置中，我们需要声明 "对等方"，即远程服务器：**



```
[Interface]
PrivateKey = <la clé privée du PC>
```



我们需要完成此配置，特别是在此 Interface 上声明 IP Address（*Address*），还要通过 [Peer] 块声明远程 WireGuard 服务器。下图应该能让你想起我们在 Linux 服务器端创建的配置文件。



让我们从"[Interface]"块开始，添加 IP Address "**192.168.110.2**"；记住服务器在此网段上的 IP Address "**192.168.110.121**"。这样就得到 ：



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



接下来，我们需要声明具有三个属性的 "Peer "块，从而形成以下配置：



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



图片 ：



![Image](assets/fr/029.webp)



**关于[同行]区块的一些解释：**





- 公钥**：这是 WireGuard Debian 11 服务器的公钥（可通过 "*sudo wg*"命令获取其值）
- **AllowedIPs**：这些是可通过此 WireGuard VPN 网络访问的 IP 地址/子网，在本例中是我的 WireGuard VPN（*192.168.110.0/24*）和我的远程局域网（*192.168.100.0/24*）专用的子网。
- 端点：这是 Debian 11 主机的 IP Address，因为这是我们的 **WireGuard** 连接点（您需要指定公共 IP Address）。



最后，在 "**名称**"字段中输入名称（不含空格），并复制和粘贴客户端的公钥，因为我们需要在服务器上声明它。点击 "**注册**"。



### C.在 WireGuard 服务器上声明客户端



现在该返回 Debian 服务器，在 WireGuard 配置中声明 "**Peer**"，即我们的 Windows PC。首先，我们需要 ** 停止 Interface "wg0"** 以修改其配置：



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



接下来，修改之前创建的配置文件：



```
sudo nano /etc/wireguard/wg0.conf
```



在该文件中，在"[Interface]"块之后，我们需要声明一个"[Peer]"块：



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



此 [Peer] 块包含 Windows 10 PC 的公钥（**PublicKey**）和 PC 的 Interface 的 IP Address（**AllowedIPs**）：服务器在此 WireGuard 隧道中的通信仅用于联系 Windows 客户端，因此值为 "**192.168.110.2/32**"。



剩下的工作就是保存文件（*CTRL+O 然后回车，然后通过 Nano* CTRL+X）。重新启动 Interface "wg0"：



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



要检查同行声明是否有效，可以使用这条命令：



```
sudo wg show
```



一旦远程主机建立了 WireGuard 连接，其 IP Address 就会上移到 "端点 "值。



![Image](assets/fr/033.webp)



最后，我们将保护配置文件，限制 root 访问：



```
sudo chmod 600 /etc/wireguard/ -R
```



### D.第一个 WireGuard 连接



现在配置已经就绪，我们可以从 Windows PC 启动配置。为此，请在 "**WireGuard**"客户端中点击 "**激活**"按钮：连接将从 "关闭 "变为 "打开 "**，但这并不意味着可以正常工作。这完全取决于您的配置是否正确。 **连接建立后，我们的两台机器将通过各自配置的 Interface WireGuard 进行通信！



![Image](assets/fr/030.webp)



如果出现问题，这将在 "**日志**"选项卡中显示。两台主机将定期发送 Exchange 数据包，以检查连接状态，因此会出现 "*从对等设备 1 接收保持数据包*"的信息。



![Image](assets/fr/031.webp)



如果 WireGuard 的 "**日志**"选项卡显示如下信息，则需要检查双方声明的公钥是否正确。



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



我可以从远程电脑上 ping 服务器端 Interface WireGuard 的 IP Address，以及远程局域网上的主机。



![Image](assets/fr/032.webp)



### E.性能：OpenVPN 与 WireGuard



通过连接到 WireGuard VPN 的远程 PC，我可以访问文件服务器，并通过 [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) 传输文件，查看传输速率。**使用 WireGuard，我的最高传输速率约为 45 Mb/s，这很不错，因为我使用的是 WiFi。**



![Image](assets/fr/025.webp)



在相同的条件下，但这次通过 OpenVPN 连接（UDP）进行相同的操作，吞吐量完全不同：约为 3 MB/s。差异显而易见！



![Image](assets/fr/026.webp)



这一点很有趣，因为例如，如果您从 WiFi 连接切换到 4G/5G 连接，重新连接的速度会非常快，以至于看不到中断。



### F.奖励：全隧道 WireGuard



在当前配置下，部分流量流经 VPN，其余流量流经客户的互联网连接，包括互联网浏览。如果我们想切换到 WireGuard **全隧道模式**，让所有流量都通过 VPN 隧道，我们需要对配置做一些更改....



首先，您需要在 .NET Framework 上安装 "resolvconf "软件包：



```
sudo apt-get update
sudo apt-get install resolvconf
```



完成上述操作后，您需要修改 Debian 机器上的 "wg0.conf "配置文件：停止 Interface，修改配置文件，然后重新启动。



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



接下来，**在"[Interface]"块中，我们添加要使用的 DNS 服务器**。在我的例子中，它是我实验室的域控制器，但我们也可以在 Debian 机器上安装 Bind9，以使用本地解析器。



```
DNS = 192.168.100.11
```



保存文件，然后重启 Interface ：



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



最后，在 Windows 10 工作站的隧道配置中，需要修改 "AllowedIPs"（允许的 IP）部分，以表明所有内容都必须通过隧道。替换 ：



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



作者 ：



```
AllowedIPs = 0.0.0.0/0
```



您可以看到，这也启用了 **"杀死开关"** 选项。



![Image](assets/fr/040.webp)



最后，我利用这条全隧道进行了一次小流量测试，结果如下：



![Image](assets/fr/039.webp)



WireGuard 的配置非常简单易懂，最重要的是易于维护。 **WireGuard 被认为是 VPN 的未来**，因此我们最好密切关注它！我们还可以看到，WireGuard 在性能方面的优势也非常明显，与 OpenVPN 相比，这是 WireGuard 的一大优势。



其他文件 ：





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**您的 WireGuard VPN 已启动并运行！恭喜您**