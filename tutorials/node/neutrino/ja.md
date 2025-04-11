---
name: Neutrino
description: LND Neutrinoのインストールガイド
---

# Raspberry PiでLNDを設定する

1. Raspberry Pi OS Liteのダウンロード

Raspberry Pi OS Liteをダウンロードします。Windows、Mac、Linuxでのイメージのダウンロードとmicro SDカードへのインストール方法は、[このページ](https://www.raspberrypi.org/software/operating-systems/) で見つけることができます。

2. SDカードのフォーマット化

Raspberry Pi ImagerまたはbalenaEtcherを使用してSDカードをフォーマット化します。

> 注意: シンボル`$`はプロンプトとして使用され、ユーザーがコンピュータにコマンドを入力することを可能にします。これらのコマンドはLinuxのbashによって解釈されます。行の先頭に`#`がある場合、その後のテキストはコメントであることを示します。

3. SSHの有効化

フォーマット化されたメモリを持つRaspberry Piを起動する前に、リモート接続を可能にするための2つのファイルを作成する必要があります。`touch`コマンドを使用して、/bootパーティションに空のファイルを作成し、新しくフォーマット化されたSDカードの最初の起動時にSSH接続を有効にします。

```
# 注意: microSDカードが/media/microSDにマウントされている場合、コマンドは
# $ sudo touch /media/microSD/boot/ssh となります
$ touch /boot/ssh
```

4. nanoコマンドの使用

wpa_supplicant.confファイルを作成し、直接編集を開始します。このファイルには、wifi設定をコピーする必要があり、STARTとENDの間のテキストをコピーし、接続したいwifiのSSIDとパスワードを変更します。

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

5. 接続

その後、SDカードをRaspberry Piに挿入し、Piを電源に接続してオペレーティングシステムを起動します。ネットワーク上でそれを識別する必要があります。mDNSプロトコルがそれにraspberrypi.localという名前を割り当てる可能性があります。SSH経由で接続してみましょう。

```
$ ssh pi@raspberrypi.local
password: raspberry
```

うまくいかない場合は、ネットワークを調べる必要があります。接続しているIPアドレスを見つけましょう。

```
$ ifconfig
```

例えば、それが192.168.0.0である場合、nmapを使用してPiを見つけます。

```
nmap -v 192.168.0.0/24
```

ネットワーク上に新しいIPを見つけたと仮定して、SSH経由で入ります。

```
$ ssh pi@192.168.0.30
password: raspberry
```

1. Piの設定

```
$ sudo raspi-config
```

- option (1) を選択し、ユーザーpiのパスワードを変更します。
- option (8) を選択して、設定ツールを最新バージョンに更新します。
- option (4) を選択して、タイムゾーンを選択します。
- option (7) を選択し、その後ファイルシステムの拡張を選択します。
- Finish（完了）

  7.- OSを更新します。

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- bitcoin userを追加します。

```
$ sudo adduser bitcoin
```

9.- rpiをセキュアにします。

```
$ sudo apt install ufw
```

```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'LANからSSHを許可'
$ sudo ufw allow 9735 comment 'Lightningを許可'
$ sudo ufw allow 10009 comment 'Lightning gRPCを許可'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

10.- Goのインストール：raspberry piを使用していない場合は、こちらからアーキテクチャに合ったGoをダウンロードしてください (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # 'go version go1.13.5 linux/arm'というメッセージが表示されるはずです
```

11.- lndのコンパイルとインストール

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

12.- lnd設定ファイルの作成、これは'bitcoin'userで行うべきです。

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

13.- RPI起動後にLNDが起動するようにするには、systemdに.serviceファイルを作成する必要があります。bitcoin userとしてログインしていて、piユーザーに戻りたい場合は、単に'exit'と入力します

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

ログを表示するには、次のコマンドを実行します：journalctl

```
$ sudo journalctl -f -u lnd
```

14. これで lnd を開始します。

```
$ sudo su - bitcoin
$ lncli create
```

15. 私たちのノードに資金を追加します。

```
$ lncli newaddress p2wkh
```

lnd が返したアドレスに btc を送ります。

残高を確認する

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

トランザクションが確認されたら、チャネルを開くことができます。どのノードとチャネルを開くかわからない場合は、1ml.com にアクセスしてノードを選択できます。

ノードへの接続を開く：

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

その後、チャネルを開きます。

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

私たちの資金を確認します。

```
$ lncli walletbalance
$ lncli channelbalance
```

保留中およびアクティブなチャネルを表示できます。

```
$ lncli pendingchannels
$ lncli listchannels
```

ライトニングインボイスを支払う方法

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

支払いを受け取るには、特定の金額のインボイスを作成します。

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

私のノードに関する情報を表示する

```
$ lncli getinfo
```

コマンドの完全なリストは、単に lncli を実行することで見ることができます。

```
$ lncli
```

lnd API への呼び出しを行う方法

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> 終わり
