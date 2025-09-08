---
name: 灰度日志
description: 集中管理并轻松分析日志
---
![cover](assets/cover.webp)



___



*本教程基于 Florian BURNEL 在 [IT-Connect](https://www.it-connect.fr/) 上发表的原创内容。授权许可 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有改动。



___



## 在 Debian 12 上部署 Graylog



### I.介绍



Graylog 是一个开源的 "日志汇 "解决方案，旨在实时集中、存储和分析来自机器和网络设备的日志。在本教程中，我们将学习如何在 Debian 12 机器上安装免费版 Graylog！



在信息系统中，每台**服务器，无论是运行**Linux**还是**Windows**，以及每台**网络设备**（交换机、路由器、防火墙等......），都会**生成自己的日志**，并存储在本地。由于日志存储在每台机器上，事件分析和关联非常困难...这就是**Graylog**的用武之地。它将充当**日志汇，这意味着**你的所有机器都将向它发送日志**（例如通过系统日志）。然后，Graylog 将**存储这些日志并编制索引**，同时允许您执行全局搜索并创建警报。



Graylog 是一款分析和监控工具，可以更轻松地识别可疑行为和各种问题（稳定性、性能等）。




![Image](assets/fr/034.webp)



**注：免费版**Graylog Open** 并不像 Wazuh 那样是 SIEM，尤其是它缺乏真正的入侵检测功能。



### II.先决条件



堆栈灰度日志**基于**个组件，我们需要安装和配置这些组件。在这里，我们将在同一台服务器上安装所有组件，但也可以创建基于多个节点的集群，并将角色分配到多台服务器上。在本教程中，我们将安装迄今为止的最新版本**Graylog 6.1**。





- MongoDB 7**，Graylog 当前推荐的版本（最低 5.0.7，最高 7.x）。
- OpenSearch**，亚马逊创建的 Elasticsearch 的开源 Fork（最小 1.1.x，最大 2.15.x）。
- OpenJDK 17**



**Graylog 服务器**运行于**Debian 12**，但也可在其他发行版上安装，包括通过 Docker 安装。虚拟机配备**8 GB内存**和**256 GB磁盘空间**，以便为所有组件提供足够的资源（否则会严重影响性能）。不过，我只是给出一个粗略的指导，因为**Graylog 架构的大小取决于需要处理的信息量**。Graylog 可以每天处理 30 MB 或 300 MB 的数据，也可以每天处理 300 GB 的数据......它是一个**可扩展的解决方案**，能够处理**兆字节的日志**（请参阅[本页](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)）。



![Image](assets/fr/032.webp)



来源: Graylog



开始配置前，请为 Graylog 机器分配静态 IP Address，并安装最新更新。请务必设置本地机器的时区，并为日期和时间同步定义一个 NTP 服务器。下面是要运行的命令：



```
sudo timedatectl set-timezone Europe/Paris
```



**注意：如果使用**Graylog 数据节点**，则无需安装**OpenSearch。



### III 逐步安装 Graylog



让我们从更新软件包缓存开始，安装接下来需要的工具。



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A.安装 MongoDB



完成后，我们开始安装 MongoDB。下载与 MongoDB 存储库相对应的 GPG 密钥：



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



然后将 MongoDB 6 版本库添加到 Debian 12 机器上：



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



接下来，我们将更新软件包缓存，并尝试安装 MongoDB：



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



由于缺少一个依赖项，因此无法安装 MongoDB： **libssl1.1**。我们必须手动安装这个软件包后才能继续，因为 Debian 12 的软件仓库中没有这个软件包。



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



我们将使用**wget**命令下载名为 "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**"（最新版本）的 DEB 包，然后使用**dpkg**命令进行安装。这将产生以下两条命令：



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



重新启动 MongoDB 安装：



```
sudo apt-get install -y mongodb-org
```



然后重启 MongoDB 服务，使其在 Debian 服务器启动时自动启动。



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



安装好 MongoDB 后，我们就可以继续安装下一个组件了。



#### B.安装 OpenSearch



下面我们继续在服务器上安装 OpenSearch。以下命令将为 OpenSearch 软件包添加签名密钥：



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



然后添加 OpenSearch 软件仓库，这样我们就可以用 **apt** 下载软件包了：



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



更新软件包缓存 ：



```
sudo apt-get update
```



然后**安装 OpenSearch**，注意**定义实例的管理员**账户的默认密码。这里的密码是 "**IT-Connect2024!**"，但请用强密码替换该值。 **避免使用 "**P@ssword123**"之类的弱密码**，至少使用 8 个字符**，每种类型（小写、大写、数字和特殊字符）至少一个字符，否则安装结束时会出错。 **自 OpenSearch 2.12.** 起，这是一个先决条件。



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



安装过程中请耐心等待...



完成后，花点时间进行最低配置。打开 YAML 格式的配置文件：



```
sudo nano /etc/opensearch/opensearch.yml
```



打开文件后，设置以下选项：



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



此 OpenSearch 配置用于设置单个节点。下面是对我们使用的不同参数的一些解释：





- cluster.name：graylog**：该参数以 "**graylog**"命名 OpenSearch 群集。
- node.name：${HOSTNAME}**：节点名称是动态设置的，与本地 Linux 机器的名称一致。即使我们只有一个节点，正确命名它也很重要。
- path.data：/var/lib/opensearch**：该路径指定 OpenSearch 在本地计算机上存储数据的位置，本例中为 "**/var/lib/opensearch**"。
- path.logs：/var/log/opensearch**：该路径定义了 OpenSearch 日志文件的存储位置，此处为 "**/var/log/opensearch**"。
- discovery.type：single-node**：该参数将 OpenSearch 配置为使用单个节点，因此选择 "**single-node**"选项。
- network.host：127.0.0.1**：该配置确保 OpenSearch 只监听其 Interface 本地环路，这就足够了，因为它与 Graylog 位于同一服务器上。
- action.auto_create_index：false**：通过禁用自动索引创建，OpenSearch 在发送没有现有索引的文档时不会自动创建索引。
- plugins.security.disabled：true**：该选项会停用 OpenSearch 安全插件，这意味着不会有身份验证、访问管理或通信加密。此设置可在设置 Graylog 时节省时间，但在生产中应避免使用（请参阅 [this page](https://opensearch.org/docs/1.0/security-plugin/index/) ）。



有些选项已经存在，因此只需去掉 "#"就可以激活它们，然后标出你的值。如果找不到选项，可以直接在文件末尾声明。



![Image](assets/fr/023.webp)



保存并关闭此文件。



#### C.配置 Java（JVM）



您需要配置 OpenSearch 使用的 Java 虚拟机，以调整该服务可使用的内存量。编辑以下配置文件：



```
sudo nano /etc/opensearch/jvm.options
```



根据此处部署的配置，**OpenSearch 将从 4 GB 分配内存开始，最多可增加到 4 GB**，因此在运行过程中不会出现内存变化。这里的配置考虑到了虚拟机总共有 **8 GB 内存**这一事实。两个参数的值必须相同。这意味着要替换 ：



```
-Xms1g
-Xmx1g
```



有了这些台词：



```
-Xms4g
-Xmx4g
```



下面是要进行的修改的图片：



![Image](assets/fr/022.webp)



保存后关闭该文件。



此外，我们还需要检查 Linux 内核中 "**max_map_count**"参数的配置。它定义了每个进程映射内存区域的限制，以满足我们应用程序的需求。 *与 Elasticsearch** 一样，*OpenSearch** 建议将该值设置为 "262144"，以避免内存管理错误。



原则上，在新安装的 Debian 12 机器上，数值已经正确。但我们还是要检查一下。运行以下命令



```
cat /proc/sys/vm/max_map_count
```



如果得到的值不是 "**262144**"，请运行以下命令，否则不必运行。



```
sudo sysctl -w vm.max_map_count=262144
```



最后，启用 OpenSearch 自动启动并启动相关服务。



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



如果显示系统状态，应该会看到一个 Java 进程，内存为 4 GB。



```
top
```



![Image](assets/fr/029.webp)



下一步：安装期待已久的 Graylog！



#### D.安装 Graylog



要**安装最新版本的 Graylog 6.1**，请运行以下 4 个命令**下载并安装 Graylog 服务器**：



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



完成后，我们需要对 Graylog 的配置进行一些修改，然后再尝试启动它。



让我们从配置这两个选项开始：





- password_secret**：该参数用于定义 Graylog 用来确保用户密码存储安全的密钥（与盐密钥类似）。该密钥必须**唯一**且**随机**。
- root_password_sha2**：该参数对应于 Graylog 中的默认管理员密码。它存储为 Hash SHA-256。



我们首先要为 **password_secret** 参数生成一个 96 个字符的密钥：



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



复制返回值，然后打开 Graylog 配置文件：



```
sudo nano /etc/graylog/server/server.conf
```



将密钥粘贴到 **password_secret** 参数中，如下所示：



![Image](assets/fr/027.webp)



保存并关闭文件。



接下来，需要为默认创建的 "**admin**"账户设置密码。在配置文件中，必须存储密码的 Hash，也就是必须计算出密码的 Hash。下面的示例给出了密码 "**LogsWells@**"的 Hash：请根据自己的密码调整该值。



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



将获得的值复制为输出值（行末不带连字符）。



再次打开 Graylog 配置文件：



```
sudo nano /etc/graylog/server/server.conf
```



像这样将值粘贴到 **root_password_sha2** 选项中：



![Image](assets/fr/026.webp)



在配置文件中，设置 "**http_bind_address**"选项。指定 "**0.0.0.0:9000**"，这样就可以通过任何服务器 IP Address 在**9000**端口访问 Graylog 的 Interface 网络。



![Image](assets/fr/024.webp)



然后将 "**elasticsearch_hosts**"选项设置为 "http://127.0.0.1:9200"，以声明我们的本地 OpenSearch 实例。这是必要的，因为我们没有使用**Graylog 数据节点**。如果没有这个选项，就无法继续...



![Image](assets/fr/025.webp)



保存并关闭文件。



该命令激活 Graylog，使其在下次启动时自动启动，并立即启动 Graylog 服务器。



```
sudo systemctl enable --now graylog-server
```



完成后，尝试从浏览器连接 Graylog。输入服务器的 IP Address（或名称）和端口 9000。



**供参考：**



不久前，当您第一次登录 Graylog 时，会出现类似下面的验证窗口。你必须输入登录名 "**admin**"和密码。然后，你会惊讶地发现连接无法正常工作。



![Image](assets/fr/031.webp)



我们有必要回到 Graylog 服务器的命令行查看日志。然后我们可以看到，**第一次连接**时，必须**使用日志中指定的临时口令**。



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



然后，您必须使用用户 "**admin**"和临时密码重新进行连接，这样才能登录！



**这种情况已不复存在。您只需使用管理员账户和命令行配置的密码登录即可



![Image](assets/fr/033.webp)



**欢迎来到格雷罗格的GW -8



![Image](assets/fr/019.webp)



#### E.灰色日志：创建新的管理员账户



您可以创建自己的个人管理员账户，而不是使用 Graylog 原生创建的管理员账户。点击 "**系统**"菜单，然后点击 "**用户和团队**"，点击 "**创建用户**"按钮。然后填写表格并为您的账户分配管理员角色。



![Image](assets/fr/020.webp)



与本地管理员账户不同，个性化账户可以包含更多信息，如姓名和电子邮件 Address。此外，当每个人使用一个命名账户工作时，这还能确保更好的可追溯性。



## 使用 rsyslog 将日志发送到 Graylog



### I.介绍



在第二部分中，我们将学习如何配置 Linux 机器将日志发送到 Graylog 服务器。为此，我们将在系统上安装并配置 Rsyslog。



### II.配置 Graylog 以接收 Linux 日志



我们将从配置 Graylog 开始。有三个步骤需要完成：





- 创建一个**输入**，以创建一个入口点，允许 Linux 机器通过 UDP**发送 Syslog 日志。
- 创建一个新的**索引**，用于存储和**索引所有 Linux 日志**。
- 创建**流**，将 Graylog 收到的日志路由**到新的 Linux 索引。



#### A.创建系统日志输入



登录 Graylog Interface，点击菜单中的 "**系统**"，然后点击 "**输入**"。在下拉列表中选择 "**系统日志 UDP**"，然后点击 "**启动新输入**"按钮。也可以创建 TCP Syslog 输入，但这需要使用 TLS 证书：这是安全方面的一个优点，但不在本文讨论之列。



![Image](assets/fr/001.webp)



屏幕上会出现一个向导。首先为输入端命名，例如 "**Graylog_UDP_Rsyslog_Linux**"，然后选择端口。默认端口为 "**514**"，但也可以自定义。这里选择的是端口 "**12514**"。



![Image](assets/fr/016.webp)



您也可以选中 "**存储完整信息**"选项，将完整的日志信息存储到 Graylog 中。点击 "**启动输入**"。



![Image](assets/fr/017.webp)



新的输入已创建并激活。Graylog 现在可以通过 12514/UDP 端口接收 Syslog 日志，但我们还没有完成应用程序的配置。



![Image](assets/fr/018.webp)


**注意：一个输入端可用于存储多台 Linux 机器的日志。



#### B.创建新的 Linux 索引



我们需要在 Graylog 中创建一个索引来存储来自 Linux 机器的日志。Graylog 中的**索引**是一种存储结构，其中包含收到的日志，即收到的消息。Graylog 使用 OpenSearch 作为其存储引擎，对消息进行索引是为了实现快速、高效的搜索。



在 Graylog 中点击菜单中的 "**系统**"，然后点击 "**索引**"。在出现的新页面上，点击 "**创建索引集**"。



![Image](assets/fr/005.webp)



为该索引命名，例如 "**Linux 索引**"，添加说明和前缀，然后确认。在此，我们将在该索引中**存储所有 Linux 日志**。也可以创建特定索引，只存储某些日志（只存储 [SSH] 日志（https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"）、Web 服务日志等）。



![Image](assets/fr/006.webp)



现在，我们需要创建一个新的流，将消息路由到该索引。



#### C.创建流



要创建新数据流，请点击 Graylog 主菜单中的 "**数据流**"。然后点击右侧的 "**创建流**"按钮。在出现的窗口中，为流命名，例如 "**Linux 流**"，并在名为 "**索引集**"的字段中选择索引 "**Linux 索引**"。确认您的选择。



**注意：除非勾选 "**从'默认流'中删除匹配**"选项，否则该流对应的信息也将包含在 "**默认流**"中。



![Image](assets/fr/002.webp)



然后，在蒸汽设置中点击 "**添加流规则**"按钮，添加新的消息路由规则。如果找不到这个窗口，请点击菜单中的 "**流**"，然后在流对应的行上点击 "**更多**"，再点击 "**管理规则**"。



选择 "**匹配输入**"类型，并选择先前创建的 UDP**Rsyslog 输入。点击 "**创建规则**"按钮确认。现在，所有发送到新输入端的信息都将被发送到 Linux 的索引。



![Image](assets/fr/003.webp)



您的新数据流应出现在列表中，并处于 "**运行**"状态。信息带宽显示 "**0 msg/s**"，因为我们目前没有向 Rsyslog UDP 输入发送任何日志。要查看某个数据流的日志，只需点击其名称即可。



![Image](assets/fr/004.webp)



**Graylog 方面一切就绪**。下一步是配置 Linux 机器。



### III.在 Linux 上安装和配置 Rsyslog



在本地或远程登录 Linux 机器，使用有权限提升其权限的用户账户（通过 sudo）。否则，请直接使用 "root "账户。



#### A.安装 Rsyslog 软件包



首先更新软件包缓存并安装名为 "**rsyslog**"的软件包。



```
sudo apt-get update
sudo apt-get install rsyslog
```



然后检查服务状态。大多数情况下，它已经在运行了。



```
sudo systemctl status rsyslog
```



#### B.配置 Rsyslog



Rsyslog 的主配置文件位于此处：



```
/etc/rsyslog.conf
```



此外，"**/etc/rsyslog.d/**"目录用于存储 Rsyslog 的其他配置文件。在主配置文件中，有一个 "包含 "指令，用于导入该目录下的所有 "**.conf**"文件。这样就可以在不修改主配置文件的情况下为 Rsyslog 配置附加文件。



在该目录中，必须使用数字来定义加载顺序，因为文件是按字母顺序加载的。添加数字前缀可以管理多个配置文件之间的优先级。在这里，我们只有一个附加文件，所以问题不大。



在该目录下，我们将创建一个名为 "**10-graylog.conf**"的文件：



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



在该文件中，插入这一行 ：



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



下面是对这句话的解释：





- *.*`：表示将 Linux 机器上的所有 Syslog 日志都发送到 Graylog。
- `@`：表示以 UDP 方式传输。要切换到 TCP，必须指定 "**@@**"。
- 192.168.10.220:12514"：表示 Graylog 服务器的 Address 和发送日志的端口（与输入对应）。
- RSYSLOG_SyslogProtocol23Format：对应于要发送到 Graylog 的信息格式。



完成后，保存文件并重启 Rsyslog。



```
sudo systemctl restart rsyslog.service
```



执行此操作后，第一批邮件就会到达 Graylog 服务器！



### IV.在 Graylog 中显示 Linux 日志



在 Graylog 中，您可以点击 "**流**"并选择您的新流以查看相关信息。或者，点击 "**搜索**"，选择您的 Steam 并启动搜索。



以下是 Interface 的一些主要特点：



**1** - 选择显示信息的时间段。默认情况下，显示最近 5 分钟的信息。



**2** - 选择要显示的数据流。



**3** - 启用消息列表自动刷新功能（例如每 5 秒刷新一次）。否则，它将是静态的，您必须手动刷新。



**4** - 点击放大镜，在修改周期、数据流或过滤器后启动搜索。



**5** - 输入栏，用于指定搜索过滤器。在这里，我指定了 "**source:srv\-docker**"，以便只显示新机器的日志，我刚刚在这台机器上设置了 Rsyslog。



日志由 Linux 机器发送：



![Image](assets/fr/015.webp)



### V.识别 SSH 连接失败



Graylog 的优势在于其索引日志的能力，可以根据不同的标准进行搜索：源机器、Timestamp、消息内容等...我们可以查找失败的 SSH 连接。



从远程计算机（例如 Graylog 服务器）尝试连接到您刚刚配置了 Rsyslog 的 Linux 服务器。例如



```
ssh [email protected]
```



然后故意输入错误的**用户名**和**密码**，以**generate 连接错误**。在 "**/var/log/auth.log**"文件中，这会出现类似以下的 generate 日志信息：



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



您可以在 Graylog 上找到这些信息。



在 Graylog 上，使用以下搜索过滤器只显示匹配的信息：



```
message:Failed password AND application_name:sshd
```



如果您有多个服务器，并希望分析特定服务器的日志，请在............之外指定其名称：



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



下面是在一台机器上的结果概览，在这台机器上，我在一天中的不同时间产生了多次连接错误：



![Image](assets/fr/009.webp)



从 IP 地址为 Address"**192.168.10.199**" 的机器尝试连接未果。如果您想进一步了解该主机的活动，可以**搜索该 IP Address**。Graylog 将输出所有主机（已配置日志发送功能）上引用此 IP Address 的所有日志。



在这种情况下，使用的过滤器可以是 ：



```
message:"192.168.10.199"
```



我们得到了额外的结果（这并不奇怪，因为我们没有对 SSH 应用程序进行过滤）：



![Image](assets/fr/008.webp)



### VI.结论



按照本教程，您应该能够配置一台 Linux 机器，将其日志发送到 Graylog 服务器。这样，您就能将 Linux 主机的日志集中到日志汇中！



若要更进一步，可考虑创建仪表板和警报，以便在检测到异常情况时接收通知。



![Image](assets/fr/007.webp)