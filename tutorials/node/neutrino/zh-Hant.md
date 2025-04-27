---
name: 中微子
description: LND Neutrino 安裝指南
---

# 使用 LND 設定 Raspberry Pi


#### 1.下載 Raspberry Pi OS Lite

在 Windows、Mac 和 Linux 中下載映像檔並安裝到 micro SD 卡的說明，請參閱 [本頁](https://www.raspberrypi.org/software/operating-systems/)。


#### 2.格式化 SD 卡

使用 Raspberry Pi Imager 或 balenaEtcher。


**Note:** 符號 `$` 用作提示符，允許使用者在電腦中輸入命令，命令將由 Linux 中的 bash 解譯。行首的符號 `#` 表示下面的文字是註解。


#### 3.啟用 SSH


在使用格式化的記憶體啟動 Raspberry Pi 之前，我們必須將它插入電腦，並建立兩個檔案，讓我們可以遠端連線。使用 `touch` 指令，我們在 /boot 磁碟分割中建立一個空檔，使剛格式化的 SD 卡第一次開機時能夠進行 SSH 連線。


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4.建立 Wi-Fi 連線的檔案

使用 nano 指令建立 `wpa_supplicant.conf` 檔案，並直接開始編輯。在此檔案中，我們需要複製 wifi 設定，複製 START 和 END 之間的文字，並修改要連線的 wifi 的 SSID 和密碼。


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


#### 5.連接

然後，我們將 SD 卡插入 Raspberry Pi，並將 Pi 連接到電源，以啟動作業系統。我們需要在網路上識別它，mDNS 協定可能會為它指定 raspberrypi.local 這個名稱。讓我們嘗試透過 SSH 連線。

```
$ ssh pi@raspberrypi.local
password: raspberry
```

如果不起作用，我們需要找出網路。讓我們找出我們連線的 IP Address。


```
$ ifconfig
```


例如，如果是 192.168.0.0，請使用 nmap 來尋找 Pi。


```
nmap -v 192.168.0.0/24
```


假設我們在網路上找到新的 IP，讓我們透過 SSH 進入。


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6.設定 Pi

```
$ sudo raspi-config
```


- 選擇選項 (1)，然後變更使用者 pi 的密碼。
- 我們選擇選項 (8) 將組態工具更新至最新版本
- 我們選擇選項 (4) 來選擇我們的時區
- 我們選擇選項 (7)，然後展開檔案系統
- 完成


#### 7.現在更新作業系統

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8.新增 Bitcoin 使用者

```
$ sudo adduser bitcoin
```


#### 9.保護 rpi


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


#### 10.安裝 Go

如果您沒有使用 raspberry pi，請下載 go for your architecture [這裡](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11.編譯並安裝 LND


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


#### 12.建立 LND conf 檔案

建立 LND 組態檔案，這應該使用「Bitcoin」使用者來完成


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


#### 13.LND 服務自動啟動

要讓 LND 在 rpi 開機後啟動，我們必須在 systemd 中建立 .service 檔案。如果我們以 Bitcoin 使用者登入，想要切回 pi 使用者，只要輸入 'exit' 即可。


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


我們可以執行 journalctl 指令檢視日誌


```
$ sudo journalctl -f -u lnd
```


#### 14.現在我們開始 LND


```
$ sudo su - bitcoin
$ lncli create
```


#### 15.將資金加入節點


```
$ lncli newaddress p2wkh
```

現在您可以傳送 btc 到 LND 傳回的 Address。


使用此指令，您可以檢查餘額：


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


交易確認後，我們就可以開啟一個通道。如果您不知道要在哪個節點開啟通道，可以到 1ml.com 選擇節點。


開啟與節點的連線：

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


然後開啟通道：

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


檢查我們的基金：

```
$ lncli walletbalance
$ lncli channelbalance
```


我們可以檢視待定和作用中的頻道：

```
$ lncli pendingchannels
$ lncli listchannels
```


支付閃電 Invoice：

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


若要接收付款，請建立特定金額的 Invoice：

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


檢視關於我的節點的資訊：

```
$ lncli getinfo
```


只要執行 lncli 指令，就可以看到完整的指令清單：

```
$ lncli
```


最後，對 LND API 進行呼叫：

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


指南結束！