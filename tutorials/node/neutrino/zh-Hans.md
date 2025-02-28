---
name: Neutrino
description: LND Neutrino 安装指南
---

# Raspberry Pi 配置 LND

1. 下载 Raspberry Pi OS Lite

下载 Raspberry Pi OS Lite，关于如何在 Windows、Mac 和 Linux 上下载并安装镜像到 micro SD 卡的指南可以在[这个页面](https://www.raspberrypi.org/software/operating-systems/)找到。

2. 格式化 SD 卡

使用 Raspberry Pi Imager 或 balenaEtcher 格式化 SD 卡。

> 注意：符号 `$` 用作提示符，允许用户输入命令到计算机中，命令将由 Linux 中的 bash 解释。行首的符号 `#` 表示后面的文本是注释。

3. 启用 SSH

在用格式化好的内存启动 Raspberry Pi 之前，我们必须将其插入到计算机中并创建两个文件，这两个文件将允许我们远程连接。使用 `touch` 命令，在 /boot 分区创建一个空文件，以在首次启动新格式化的 SD 卡时启用 SSH 连接。

```
# 注意：如果 microSD 卡已经挂载在 /media/microSD，命令应该是
# $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. 使用 nano 命令

我们创建 wpa_supplicant.conf 文件并直接开始编辑它。在这个文件中，我们需要复制 wifi 配置，复制 START 和 END 之间的文本，并修改你想要连接到的 wifi 的 SSID 和密码。

```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ END -------
```

5. 连接

然后，我们将 SD 卡插入 Raspberry Pi 并连接电源启动操作系统。我们需要在网络上识别它，mDNS 协议可能会将其命名为 raspberrypi.local。让我们尝试通过 SSH 连接。

```
$ ssh pi@raspberrypi.local
password: raspberry
```

如果不行，我们需要找出网络。让我们找出我们连接到的 IP 地址。

```
$ ifconfig
```

例如，如果是 192.168.0.0，使用 nmap 来找到 Pi。

```
nmap -v 192.168.0.0/24
```

假设我们在我们的网络上找到了一个新的 IP，让我们通过 SSH 进入。

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. 配置 Pi

```
$ sudo raspi-config
```

- 选择选项 (1) 并更改用户 pi 的密码。
- 我们选择选项 (8) 更新配置工具到最新版本
- 我们选择选项 (4) 选择我们的时区
- 我们选择选项 (7) 然后选择 Expand filesystem
- 完成

  7.- 我们更新操作系统

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- 我们添加 bitcoin 用户

```
$ sudo adduser bitcoin
```

9.- 我们保护 rpi

```
$ sudo apt install ufw
```
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment '允许来自局域网的SSH'
$ sudo ufw allow 9735 comment '允许Lightning'
$ sudo ufw allow 10009 comment '允许Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- 我们安装go：如果您不是使用树莓派，请在此处下载适合您架构的go（https://golang.org/dl/）

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # 应显示以下消息 'go version go1.13.5 linux/arm'
```

11.- 我们编译并安装lnd

```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```

12.- 我们创建lnd配置文件，这应该以'bitcoin'用户身份完成

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# 启用自发支付
accept-keysend=1

# 节点的公开名称
alias=YOUR_ALIAS
# 十六进制的公开颜色
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC套接字
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- 为了使LND在树莓派启动后自动启动，我们必须在systemd中创建.service文件。
如果我们以bitcoin用户身份登录并想切换回pi用户，只需输入'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# 服务执行
###################

ExecStart=/usr/local/bin/lnd


# 进程管理
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# 目录创建和权限
####################################

# 以bitcoin:bitcoin身份运行
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# 加固措施
####################

# 提供私有的/tmp和/var/tmp。
```
```
PrivateTmp=true
# 为进程挂载 /usr、/boot/ 和 /etc 为只读。
ProtectSystem=full

# 禁止进程及其所有子进程通过 execve() 获得新权限。
NoNewPrivileges=true

# 使用一个新的 /dev 命名空间，仅包含 API 伪设备，如 /dev/null、/dev/zero 和 /dev/random。
PrivateDevices=true

# 拒绝创建可写和可执行的内存映射。
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

我们可以通过运行 journalctl 命令查看日志

```
$ sudo journalctl -f -u lnd
```

14. 现在我们启动 lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. 为我们的节点添加资金

```
$ lncli newaddress p2wkh
```

将 btc 发送到 lnd 返回的地址

检查余额

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

一旦交易被确认，我们可以开启一个通道。如果你不知道与哪个节点开启通道，你可以访问 1ml.com 并选择一个节点。

连接到一个节点：

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

然后开启一个通道

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

检查我们的资金

```
$ lncli walletbalance
$ lncli channelbalance
```

我们可以查看待处理和活跃的通道

```
$ lncli pendingchannels
$ lncli listchannels
```

支付一个闪电网络发票

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

接收付款，为特定金额创建一个发票

```
$ lncli addinvoice --memo '我在LN上的第一笔付款' --amt 100
```

查看我的节点信息

```
$ lncli getinfo
```

通过简单运行 lncli 可以看到完整的命令列表

```
$ lncli
```

最后，调用 lnd API

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> 结束