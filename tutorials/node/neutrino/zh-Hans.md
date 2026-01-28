---
name: Neutrino
description: LND 中微子安装指南
---
![image](assets/cover.webp)


## 树莓派与 LND 的配置


### 1.下载 Raspberry Pi OS Lite


在 Windows、Mac 和 Linux 中下载映像并将其安装到 micro SD 卡的说明可在 [本页](https://www.raspberrypi.org/software/operating-systems/) 上找到。


### 2.格式化 SD 卡


使用 Raspberry Pi Imager 或 balenaEtcher。


**注：** 符号 `$` 用作提示符，允许用户向计算机输入命令，这些命令将由 Linux 中的 bash 解释。一行开头的符号 `#` 表示下面的文本是注释。


### 3.启用 SSH


在使用格式化后的内存启动 Raspberry Pi 之前，我们必须将其插入电脑，并创建两个允许我们远程连接的文件。使用 "touch "命令，我们在/boot分区中创建一个空文件，这样就能在首次启动刚格式化的SD卡时实现SSH连接。


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4.为 Wi-Fi 连接创建文件


使用 nano 命令创建 "wpa_supplicant.conf "文件并直接开始编辑。在该文件中，我们需要复制 wifi 配置，复制 START 和 END 之间的文本，并修改要连接的 wifi 的 SSID 和密码。


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


### 5.连接


然后，我们将 SD 卡插入 Raspberry Pi，并将 Pi 连接到电源以启动操作系统。我们需要在网络上识别它，mDNS 协议可能会为它分配 raspberrypi.local 这个名称。让我们尝试通过 SSH 进行连接。


```
$ ssh pi@raspberrypi.local
password: raspberry
```


如果不起作用，我们就需要找出网络。让我们找出我们连接的 IP Address。


```
$ ifconfig
```


例如，如果是 192.168.0.0，则使用 nmap 查找 Pi。


```
nmap -v 192.168.0.0/24
```


假设我们在网络上找到了一个新 IP，让我们通过 SSH 进入。


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6.配置 Pi


```
$ sudo raspi-config
```


- 选择选项 (1)，更改用户 pi 的密码。
- 我们选择选项 (8)，将配置工具更新到最新版本
- 我们选择选项 (4) 来选择时区
- 我们选择选项 (7)，然后展开文件系统
- 完成


### 7.现在更新操作系统


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8.添加 Bitcoin 用户


```
$ sudo adduser bitcoin
```


### 9.确保 rpi


```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'allow SSH from LAN'
$ sudo ufw allow 9735 comment 'allow Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```


### 10.安装围棋


如果您没有使用 raspberry pi，请下载 go for your architecture [此处](https://golang.org/dl/)。


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11.编译并安装 LND


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


### 12.创建 LND 配置文件


创建 LND 配置文件，这应该由 "Bitcoin "用户完成


```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```


```
[Application Options]
# enable spontaneous payments
accept-keysend=1

# Public name of the node
alias=YOUR_ALIAS
# Public color in hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```


### 13.LND 服务自动启动


要让 LND 在 rpi 启动后启动，我们必须在 systemd 中创建 .service 文件。如果我们以 Bitcoin 用户身份登录，并希望切换回 pi 用户，只需键入 "退出


```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```


```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Service execution
###################

ExecStart=/usr/local/bin/lnd


# Process management
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```


```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```


我们可以运行 journalctl 命令查看日志


```
$ sudo journalctl -f -u lnd
```


### 14.现在开始 LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15.为节点添加资金


```
$ lncli newaddress p2wkh
```

您现在可以向 LND 返回的 Address 发送比特币。


使用该命令可以检查余额：


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


交易确认后，我们就可以打开通道了。如果不知道用哪个节点打开通道，可以访问 1ml.com，选择一个节点。


打开与节点的连接：


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


然后打开一个通道：


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


检查我们的资金：


```
$ lncli walletbalance
$ lncli channelbalance
```


我们可以查看待处理频道和活动频道：


```
$ lncli pendingchannels
$ lncli listchannels
```


支付闪电 Invoice：


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


要接收付款，请创建一个特定金额的 Invoice：


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


查看有关我的节点的信息：


```
$ lncli getinfo
```


只需运行 lncli 命令，即可查看完整的命令列表：


```
$ lncli
```


最后，调用 LND API：


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


指南结束！