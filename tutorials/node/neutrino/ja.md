---
name: Neutrino
description: LND Neutrinoインストレーション・ガイド
---
![image](assets/cover.webp)


## Raspberry PiとLNDの構成


### 1.Raspberry Pi OS Liteをダウンロード


Windows、Mac、LinuxでマイクロSDカードにイメージをダウンロードしてインストールする手順は、[このページ](https://www.raspberrypi.org/software/operating-systems/)にあります。


### 2.SDカードをフォーマットする


Raspberry Pi ImagerまたはbalenaEtcherを使用する。


**コマンドはLinuxのbashによって解釈される。行頭の記号 `#` は次のテキストがコメントであることを示します。


### 3.SSHを有効にする


フォーマットしたメモリーでRaspberry Piを起動する前に、コンピューターに挿入し、リモート接続を可能にする2つのファイルを作成する必要がある。touch`コマンドを使って/bootパーティションに空のファイルを作成し、フォーマットしたばかりのSDカードの初回起動時にSSH接続ができるようにする。


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4.Wi-Fi接続用ファイルの作成


nanoコマンドを使って`wpa_supplicant.conf`ファイルを作成し、直接編集を始める。このファイルでは、無線LANの設定をコピーし、STARTとENDの間のテキストをコピーし、接続したい無線LANのSSIDとパスワードを修正する必要がある。


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


### 5.接続


次に、SDカードをRaspberry Piに挿入し、Piを電源に接続してOSを起動する。mDNSプロトコルがraspberrypi.localという名前を割り当てるだろう。SSHで接続してみよう。


```
$ ssh pi@raspberrypi.local
password: raspberry
```


うまくいかない場合は、ネットワークを調べる必要がある。接続されているIP Addressを調べてみよう。


```
$ ifconfig
```


例えば192.168.0.0なら、nmapを使ってPiを見つける。


```
nmap -v 192.168.0.0/24
```


ネットワーク上に新しいIPが見つかったとして、SSHで入ってみよう。


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6.Piの設定


```
$ sudo raspi-config
```


- オプション(1)を選択し、ユーザーπのパスワードを変更する。
- オプション(8)を選択し、コンフィギュレーション・ツールを最新バージョンにアップデートする。
- オプション(4)を選択し、タイムゾーンを選択します。
- オプション(7)を選択し、ファイルシステムを展開します。
- 終了


### 7.OSをアップデートする


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8.Bitcoinユーザーを追加する


```
$ sudo adduser bitcoin
```


### 9.Rpiの確保


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


### 10.囲碁のインストール


ラズベリーパイを使用していない場合は、お使いのアーキテクチャに合わせてgoをダウンロードしてください[こちら](https://golang.org/dl/)。


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11.LNDのコンパイルとインストール


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


### 12.LND confファイルの作成


LNDのコンフィギュレーションファイルを作成する。


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


### 13.LNDサービス自動開始


LNDをrpiブート後に起動させるには、systemdに.serviceファイルを作成する必要がある。Bitcoinユーザーとしてログインしていて、piユーザーに戻りたい場合は、単に'exit'とタイプする。


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


journalctlコマンドを実行すれば、ログを見ることができる。


```
$ sudo journalctl -f -u lnd
```


### 14.LNDが始まる


```
$ sudo su - bitcoin
$ lncli create
```


### 15.ノードに資金を追加する


```
$ lncli newaddress p2wkh
```

LNDから戻ってきたAddressにBTCを送金できるようになった。


このコマンドでバランスをチェックできる：


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


取引が確認されたら、チャネルを開設することができる。どのノードでチャンネルを開設するか分からない場合は、1ml.comにアクセスしてノードを選択することができます。


ノードへの接続を開く：


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


それからチャンネルを開く：


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


私たちの資金を確認してください：


```
$ lncli walletbalance
$ lncli channelbalance
```


保留中のチャンネルやアクティブなチャンネルを見ることができる：


```
$ lncli pendingchannels
$ lncli listchannels
```


稲妻Invoiceを支払うために：


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


支払いを受けるには、特定の金額でInvoiceを作成する：


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


自分のノードに関する情報を見るには


```
$ lncli getinfo
```


コマンドの完全なリストは、lncliコマンドを実行するだけで見ることができる：


```
$ lncli
```


最後に、LND APIを呼び出す：


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


ガイド終了！