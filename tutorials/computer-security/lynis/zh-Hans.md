---
name: Lynis
description: 使用 Lynis 对 Linux 机器进行安全审计
---
![cover](assets/cover.webp)



___



*本教程基于 Fares CHELLOUG 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。*



___



## I.介绍



**在本教程中，我们将学习如何使用 Lynis 对 Linux 机器执行安全审计！对于那些不了解**Lynis**的人来说，它是一个小型命令行工具，可以分析服务器的配置，并提出**改善机器安全性的建议。



Lynis 是 CISOFY 的一款开源工具，CISOFY 是一家专门从事**系统审计和加固**的公司。如果你想在加固 Linux 和常用服务（SSH、Apache2 等）方面取得进展，Lynis 就是你的盟友！Lynis 不仅能告诉你出了什么问题，还能提供建议，为你指明正确的方向（节省你的时间）。



**Lynis** 可与大多数 Linux 发行版配合使用，包括 **Debian、FreeBSD、HP-UX、NetBSD、NixOS、OpenBSD、Solaris**。Lynis 面向 Linux / UNIX 用户，但也兼容**macOS**。安装非常快捷，没有软件包级别的依赖性管理。



它有多种用途：





- 安全审计
- 合规性测试（PCI、HIPAA 和 SOX）
- 更苛刻的系统配置
- 漏洞检测



该工具被包括系统管理员、IT 审计员和五项测试人员在内的广大用户广泛使用。在分析方面，该工具基于**CIS Benchmark、NIST、NSA、OpenSCAP**等标准以及**Debian、Gentoo、Red Hat**的官方建议。



该项目的 Address 位于 **Github**：





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [从 CISOFY 下载 Lynis](https://cisofy.com/lynis/#download)



在本逐步教程中，我将**使用运行 Debian 12** 的 VPS，并将重点放在 SSH 部分，因为我想检查其配置并加以改进。



## II.下载和安装



下载和安装 Lynis 有多种方法。请从以下列表中选择您喜欢的一种。



### A.从 Debian 软件源安装



这种安装模式允许你在系统的任何地方使用 **lynis** 命令，而不像从源代码安装那样，你必须位于目录中。



通过 SSH 连接到服务器，输入以下命令安装 Lynis ：



```
sudo apt-get update
sudo apt-get install lynis -y
```



这就是你的收获：



![Image](assets/fr/024.webp)



### B.从官方网站下载



您也可以从 Cisofy 网站下载：



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



这就是你的收获：



![Image](assets/fr/032.webp)



接下来，我们将使用以下命令解压压缩包：



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



这就是你的收获：



![Image](assets/fr/020.webp)



让我们转到**lynis**文件夹：



```
cd lynis
```



我们可以使用以下命令检查更新：



```
./lynis update info
```



这就是你的收获：



![Image](assets/fr/023.webp)



### C.从 GitHub 下载



我们将使用以下命令从 GitHub 官方仓库下载 **Lynis** （*git* 必须存在于你的计算机中）：



```
git clone https://github.com/CISOfy/lynis.git
```



这就是你的收获：



![Image](assets/fr/060.webp)



## III.使用 Lynis



我们的机器上有 Lynis，让我们来学习如何使用它！



### A.主要控制和选项



要显示可用命令，只需输入以下命令：



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



这就是你的收获：



![Image](assets/fr/039.webp)



您还可以获得以下选项



![Image](assets/fr/040.webp)



要显示所有可用命令，请输入以下命令：



```
sudo lynis show
```



这就是你的收获：



![Image](assets/fr/022.webp)



如果要显示所有选项，必须输入 ：



```
sudo lynis show options
```



这就是你的收获：



![Image](assets/fr/021.webp)



在本文接下来的内容中，我们将学习如何使用某些选项。



### B.进行系统审计



我们将要求**Lynis**审核我们的系统，突出哪些配置是正确的，哪些可以改进。为此，请输入以下命令：



```
sudo lynis audit system
# ou
./lynis audit system
```



默认情况下，如果运行此命令时未以 root 用户身份登录，工具将以当前登录用户的权限运行。在这种情况下，某些测试将无法运行：



![Image](assets/fr/052.webp)



以下是在此模式下不会执行的测试：



![Image](assets/fr/051.webp)



执行命令后，分析就开始了。请稍等片刻。



审核结束后，您会得到以下结果（我们可以看到，**Lynis** 已经正确识别了**Debian 12** 系统，并将使用**Debian 插件**进行分析）：



![Image](assets/fr/017.webp)



接下来，Lynis 会列出一组与他在我们系统上检查过的所有内容相对应的要点。正如我们将看到的那样，这是按类别组织的。值得注意的是，我们会用颜色代码来突出建议：





- 红色**表示关键的 Elements 或最佳实践未得到遵守（例如缺少一个软件包），即您的服务器不遵守这一点**
- 黄色**表示建议或部分符合建议**（例如，符合用这种颜色突出显示的某一点（非优先事项）是一个有利条件）
- **Green** 用于服务器配置符合要求的点
- 白色**，中性时**



在这里，我们可以看到 Lynis 建议安装 **fail2ban**：



![Image](assets/fr/057.webp)



在 "**启动和服务**"部分，我们发现通过*systemd*提供的服务保护有待改进。积极的一面是，Grub2 已经存在，.NET Framework 上的权限也没有问题：



![Image](assets/fr/029.webp)



然后是 "**内核**"和 "**内存与进程**"部分：



![Image](assets/fr/037.webp)



接下来是 "**用户、组和身份验证**"部分。工具提示我们 "**/etc/sudoers.d**"目录的权限存在警告。目前，我们还不知道更多信息，但我们可以在分析结束时看到建议。



![Image](assets/fr/049.webp)



下面是 "**外壳"、"文件系统 "和 "USB 设备 "** 部分的内容。除其他内容外，我们还可以看到关于挂载点的建议，以及该机器目前允许使用 USB 设备。



![Image](assets/fr/048.webp)



接下来是以下部分"这里说明，不再使用的软件包可以清除，而且没有能够管理自动更新的实用程序。



![Image](assets/fr/058.webp)



我们可以看到防火墙已激活（是的，还有 iptables！）。此外，我们还可以看到它找到了未使用的规则，并安装了 Apache 网络服务器。



![Image](assets/fr/055.webp)



由于服务已被识别，接下来将对网络服务器本身进行分析。



我们可以看到，它找到了**Nginx**配置文件，在 SSL/TLS 部分，**密码器**的配置使用了不安全的协议。另一方面，根据 Lynis，日志管理是正确的。



![Image](assets/fr/038.webp)



我的 VPS 服务器上有 SSH 服务。它的配置由 Lynis 分析。不得不说，SSH 的安全性很容易提高！一旦我们获得了建议，我们会再详细讨论这方面的问题。



![Image](assets/fr/026.webp)



以下是**"SNMP 支持"、"数据库"、"PHP"、"Squid 支持"、"LDAP 服务"、"日志和文件 "**部分。



关于日志管理，有一个非常重要的建议：强烈建议不要只在本地存储日志。如果机器被攻击者破坏，他很可能会试图清除自己的痕迹......因此，我们需要将日志外部化。



![Image](assets/fr/050.webp)



在这里，我们可以审计易受攻击的服务、账户管理、计划任务和 NTP 同步。在横幅和标识部分显示的级别较低：这是可以理解的，如果显示系统版本，就会给潜在的攻击者以提示。这是默认设置。



如果能激活**auditd**，以便在进行**取证**分析时获得日志，那就更有意思了。此外，还检查了**NTP**，因为要有效地搜索日志，系统最好能按时运行，这样可以简化搜索。



![Image](assets/fr/036.webp)



然后，Lynis 介绍了加密 Elements、虚拟化、容器和安全框架。有些部分是空的，因为与分析的机器没有对应关系。不过，我们可以看到我有两个过期的 SSL 证书，而且我还没有激活 **SELinux**。



![Image](assets/fr/027.webp)



这里也有改进的余地：没有反病毒或反恶意软件扫描仪，我们对文件权限提出了建议。



![Image](assets/fr/028.webp)



接下来，Lynis 重点加强 Linux 内核配置（包括 IPv4 协议栈规则）以及 Linux 机器 "主 "目录的管理。



![Image](assets/fr/035.webp)



分析到此结束...最后一点表明，在这台机器上安装 ClamAV 会给我们带来一切好处。



![Image](assets/fr/030.webp)



## IV.建议



审核结束后，就是阅读和分析建议的时候了。在这里，我们可以获得针对 Lynis 所做的每项测试的建议和解释。



以 SSH 建议为例。 **对于每项建议，你都能找到推荐的参数和解释安全要点的链接 ** 这取决于你的具体情况和用途。



让我们来看看一些建议的例子，这些建议直接呼应了整个审计中强调的要点...



### A.建议实例





- 正如我们前面所看到的，NTP 对时间戳日志非常重要：



![Image](assets/fr/043.webp)





- Lynis 还建议安装**apt-listbugs**软件包，以便在通过**apt.**安装软件包时获取有关关键漏洞的信息。



![Image](assets/fr/041.webp)





- 该工具建议我们安装 **needrestart，以便**查看哪些进程正在使用旧版本的库，需要重新启动。



![Image](assets/fr/054.webp)





- 该建议建议安装 **fail2ban**，以自动阻止无法通过身份验证（尤其是暴力）的主机。



![Image](assets/fr/044.webp)





- 要强化系统服务，他建议我们为机器上的每个服务运行蓝色命令。



![Image](assets/fr/056.webp)





- 他建议为所有受保护的账户密码设置有效期。



![Image](assets/fr/031.webp)





- 该建议建议设置密码年龄的最小值和最大值。除其他外，这将确保密码定期更改。



![Image](assets/fr/042.webp)





- 我们建议使用单独的分区，以限制磁盘空间问题对一个分区的影响。



![Image](assets/fr/047.webp)





- 本建议建议禁用 USB 存储器和火线，以防止数据泄漏



![Image](assets/fr/033.webp)





- 要满足这一建议，只需安装和配置 **非扩展升级**即可。



![Image](assets/fr/053.webp)



### B.安装推荐软件包



为了改进系统配置，我们要在机器上安装一些软件包：一些是 Lynis 推荐的，一些是我个人推荐的。



只要花一点时间对它们进行配置，你就会有一个良好的工作基础。为此，请参考 IT-Connect 网站、网络上的其他文章和工具文档。



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



关于已安装软件包的一些信息 ：





- **Clamav** 是一款杀毒软件。
- **unattend-upgrades** 可以让你自动管理更新，甚至重启机器或自动清除旧软件包，它是完全可配置的。
- **rkhunter** 是一款反 rootkit 软件，可扫描文件系统。
- **Fail2ban** 将根据您的要求读取日志文件，并与**iptables**协同工作，例如禁止试图在 SSH 中 "暴力 "您的服务器的 IP 地址。



### C.关于 SSH 的建议



让我们来看看 SSH 建议。建议如下。别担心，我们马上会介绍如何改进配置。



![Image](assets/fr/034.webp)



让我们仔细看看我当前在:**/etc/ssh/sshd_config** 中的**SSH**配置



![Image](assets/fr/018.webp)



以下建议的配置仍可优化，但为您提供了一个良好的基础。 *请注意，为了提高可读性，我删除了一些注释*。



我们将 ：





- 更改 SSH 连接端口（忘记默认的 22）
- 提高日志的冗长程度，从 **INFO 提高到 VERBOSE**
- 将**登录时间**设置为**2 分钟**



如果两分钟内未输入连接信息，连接将被断开。





- 激活**严格模式**



指定在验证连接之前，"sshd "是否要检查用户文件的模式和所有者以及用户的主目录。这通常是可取的，因为有时新手会不小心让自己的目录或文件完全被所有人访问。默认值为 "是"。





- 将**最大允许次数**设为 3



这表示在关闭通信前认证尝试失败的次数。





- 将 **MaxSessions** 设置为 2



这表示同时会话的最大数量。





- 启用公钥验证



```
PubkeyAuthentication yes
```





- 保留密码验证 ：



```
PasswordAuthentication yes
```



禁止空密码和**Kerberos**验证，以及**直接根验证**



```
PermitEmptyPasswords no
PermitRootLogin no
```



确保有 "**PermitRootLogin no"，如果等于 "yes"，则为 "绝对邪恶 "**。





- 禁止 TCP 连接重定向



```
AllowTcpForwarding no
```



表示是否允许 TCP 重定向，默认设置为 "是"。请注意：如果用户可以访问 shell，禁用 TCP 重定向并不能提高安全性，因为他们仍然可以设置自己的重定向工具。





- 禁止 X11 重定向



```
X11Forwarding no
```



表示是否接受 X11 重定向，默认设置为 "否"。请注意：即使禁用了 X11 重定向，也不会提高安全性，因为用户仍然可以设置自己的重定向器。如果选择**使用登录**，X11 重定向将自动禁用。





- 设置客户端与 sshd 之间的通信超时



```
ClientAliveInterval  300
```



定义超时时间（以秒为单位），在超时后，如果没有收到客户端的数据，sshd 服务将发送一条消息，要求客户端作出回应。默认情况下，该选项设置为 "0"，即不向客户端发送这些信息。只有第 2 版 SSH 协议支持该选项。



```
ClientAliveCountMax 0
```



根据 sshd 的[文档（*man 页*）](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html)，该选项的含义如下："设置在客户端没有回应的情况下**sshd**发送的保留信息（见上文）的数量。如果在等待信息发送过程中达到此阈值，**sshd** 将断开客户端连接并终止会话。需要注意的是，这些保持信息与**KeepAlive**选项（如下）截然不同。连接保持信息是通过加密隧道发送的，因此无法伪造。由 **KeepAlive** 启用的 TCP 级连接保持是可伪造的。当客户端或服务器需要知道连接是否处于空闲状态时，连接保持机制就会发挥作用。





- 禁用**motd、banner、lastlog**，防止信息泄露



```
PrintMotd no
```



指定当用户以交互模式登录时，sshd 是否应显示"/etc/motd "文件的内容。在某些系统中，shell 也会通过 /etc/profile 或类似文件显示这些内容。默认值为 "是"。



```
Banner none
```



值得注意的是，在某些司法管辖区，在验证前发送信息可能是获得法律保护的先决条件。在给予连接授权之前，指定文件的内容会被传送给远程用户。该选项需要配置，因为默认情况下不会显示任何信息。



在图像中，这提供了 ：



![Image](assets/fr/019.webp)



### D.审计得分



最后，别忘了检查**Lynis 审核分数**！我们看到**我的加固得分是 63**，报告文件可在 "**/var/log/lynis-report.dat**"中查看。还有一个文件 "**/var/log/lynis.log**"。



**换句话说，得分越高越好！因此，您需要在允许机器和托管服务正常运行（即进行功能测试）的前提下，努力提高配置，以获得尽可能高的分数。**



![Image](assets/fr/046.webp)



让我们看看我的第二台服务器的结果，在这台服务器上，我花了更多时间进行加固！所以分数高一些（**76**）也是正常的。



![Image](assets/fr/045.webp)



## V.Lynis 自动规划



**Lynis**还提供通过计划任务运行检查的选项。事实上，**"--cronjob "** 选项将运行所有 Lynis 测试，无需验证或用户操作。这样，你就可以非常简单地创建一个脚本，运行**Lynis**，并将输出结果放入一个带有时间戳的文件中，文件名则为相关服务器的名称。下面是一个这种类型的文件，可以放在 */etc/cron.daily* 文件夹中：



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



AUDITOR_NAME **变量只是一个变量，我们将在** Lynis **的** "--审计员" **选项中设置该变量，以便在报告中显示该名称：**



![Image](assets/fr/059.webp)



我们还将创建一些上下文变量，这些变量将帮助我们更好地组织自己，例如用于命名报告和时间戳的主机名和日期，以及我们要放置报告的文件夹的路径。



## VI.结论



Lynis 是一款非常实用的工具，当你想更多地了解 Linux 服务器的配置情况，尤其是安全方面的情况时，它能帮你节省时间，提高效率。不过，不要忘了，每项修改在应用于生产之前都必须经过测试，同时要考虑到自己的使用情况和环境。



您可能不会将相同的配置应用于暴露在网络中的 VPS，在这种情况下，您只需要一个 SSH 连接（因为您是唯一的连接者），而不像**bastion**或**scheduler**需要多个**SSH.**连接。



一旦有了适合自己的加固配置，建议采用自动化工具，这样就不必手动重做任务，因为这样既费时又容易出错。例如，你可以使用 **：Puppet、Chef、Ansible 等...... **



在实施之前，不要忘记与团队进行沟通：你需要让他们明白为什么要做出这些改变，而不仅仅是告诉他们你要做出这些改变。归根结底，目的是将好的做法传承下去，这样才能增加成功的机会。



最后，您还可以将**Lynis**与其他工具（有多种）进行比较。如果你想在保持开源的同时实现集中管理，我推荐你使用 [Wazuh] 工具 (https://wazuh.com/)。



**本教程结束，祝您和 Lynis 玩得愉快！**