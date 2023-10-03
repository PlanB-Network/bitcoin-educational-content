名前：Neutrino
説明：LND Neutrino インストールガイド

# LND を使用した Raspberry Pi の設定

1. Raspberry Pi OS Lite のダウンロード

Raspberry Pi OS Lite をダウンロードし、Windows、Mac、Linux でイメージをマイクロ SD カードにダウンロードしてインストールする手順は、[このページ](https://www.raspberrypi.org/software/operating-systems/)に記載されています。

2. SD カードのフォーマット

Raspberry Pi Imager または balenaEtcher を使用して SD カードをフォーマットします。

> 注意：シンボル`$`はプロンプトとして使用され、ユーザーはコンピュータにコマンドを入力することができます。コマンドは Linux の bash によって解釈されます。行の先頭にあるシンボル`#`は、以下のテキストがコメントであることを示します。

3. SSH の有効化

フォーマットされたメモリを使用して Raspberry Pi を起動する前に、コンピュータに挿入し、リモート接続を可能にする 2 つのファイルを作成する必要があります。`touch`コマンドを使用して、/boot パーティションに空のファイルを作成し、新しくフォーマットされた SD カードの最初の起動時に SSH 接続を有効にします。

```
# 注意：もしmicroSDカードが/media/microSDにマウントされている場合、コマンドは$ sudo touch /media/microSD/boot/sshとなります
$ touch /boot/ssh
```

4. nano コマンドの使用

wpa_supplicant.conf ファイルを作成し、直接編集を開始します。このファイルでは、WiFi の設定をコピーする必要があります。START と END の間のテキストをコピーし、接続したい WiFi の SSID とパスワードを変更します。

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

次に、SD カードを Raspberry Pi に挿入し、Pi を電源に接続してオペレーティングシステムを起動します。ネットワーク上でそれを特定する必要があり、おそらく mDNS プロトコルによって名前 raspberrypi.local が割り当てられます。SSH 経由で接続してみましょう。

```
$ ssh pi@raspberrypi.local
パスワード：raspberry
```

うまくいかない場合は、ネットワークを特定する必要があります。接続している IP アドレスを調べましょう。

```
$ ifconfig
```

例えば、192.168.0.0 である場合、nmap を使用して Pi を見つけます。

```
nmap -v 192.168.0.0/24
```

ネットワーク上で新しい IP を見つけたと仮定して、SSH 経由で入力します。

```
$ ssh pi@192.168.0.30
パスワード：raspberry
```

1. Pi の設定

```
$ sudo raspi-config
```

- オプション（1）を選択し、ユーザー pi のパスワードを変更します。
- オプション（8）を選択して、設定ツールを最新バージョンに更新します。
- オプション（4）を選択して、タイムゾーンを選択します。
- オプション（7）を選択し、ファイルシステムを拡張します。
- 完了

  7. OS の更新

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8. bitcoin ユーザーの追加

```
$ sudo adduser bitcoin
```

9. rpi のセキュリティの確保

```
$ sudo apt install ufw
```

```
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

10.- go をインストールします：Raspberry Pi を使用していない場合は、ここからアーキテクチャに合った go をダウンロードしてください（https://golang.org/dl/）

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # 以下のメッセージが表示されるはずです 'go version go1.13.5 linux/arm'
```

11.- lnd をコンパイルしてインストールします

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

12.- lnd の設定ファイルを作成します。これは 'bitcoin' ユーザーで行う必要があります。

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# スポンティアスペイメントを有効にする
accept-keysend=1

# ノードの公開名
alias=YOUR_ALIAS
# ノードの公開色（16進数）
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPCソケット
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- LND を Raspberry Pi の起動後に開始するために、systemd に.service ファイルを作成する必要があります。
bitcoin ユーザーとしてログインしていて、pi ユーザーに戻りたい場合は、単に 'exit' と入力します。

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# サービスの実行
###################

ExecStart=/usr/local/bin/lnd


# プロセス管理
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# ディレクトリの作成とパーミッション
####################################

# bitcoin:bitcoinとして実行
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# プライベートな /tmp と /var/tmp を提供する。
PrivateTmp=true
# プロセスのために/usr、/boot/、/etcを読み取り専用でマウントします。
ProtectSystem=full

# execve（）を介して新しい特権を取得することをプロセスとそのすべての子プロセスに許可しません。
NoNewPrivileges=true

# /dev/null、/dev/zero、/dev/randomなどのAPI疑似デバイスのみで新しい/dev名前空間を使用します。
PrivateDevices=true

# 書き込み可能で実行可能なメモリマッピングの作成を拒否します。
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

journalctl コマンドを実行してログを表示できます。

```
$ sudo journalctl -f -u lnd
```

14. lnd を起動します。

```
$ sudo su - bitcoin
$ lncli create
```

15. ノードに資金を追加します。

```
$ lncli newaddress p2wkh
```

lnd が返すアドレスに btc を送信します。

残高を確認するには

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

トランザクションが確認されたら、チャネルを開くことができます。チャネルを開くノードがわからない場合は、1ml.com にアクセスしてノードを選択できます。

ノードに接続します。

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

その後、チャネルを開きます。

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

資金を確認します。

```
$ lncli walletbalance
$ lncli channelbalance
```

保留中とアクティブなチャネルを表示できます。

```
$ lncli pendingchannels
$ lncli listchannels
```

ライトニングインボイスを支払うには

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

支払いを受け取るには、特定の金額のインボイスを作成します。

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```

ノードに関する情報を表示するには

```
$ lncli getinfo
```

コマンドの完全なリストは、単に lncli を実行することで表示できます。

```
$ lncli
```

最後に、lnd API に対して呼び出しを行うために

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> END
