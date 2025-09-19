---
name: WireGuard
description: DebianおよびWindowsでのWireGuard VPNの設定
---
![cover](assets/cover.webp)



___



*このチュートリアルは[IT-Connect](https://www.it-connect.fr/)に掲載されたFlorian BURNEL氏のオリジナルコンテンツに基づいています。ライセンス[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文に変更が加えられている可能性があります。*



___



## I.プレゼンテーション



このチュートリアルでは、セキュリティをおろそかにすることなくパフォーマンスを向上させる無料のオープンソースVPNソリューション、WireGuardをベースにしたVPNの設定方法を学びます。



WireGuardは比較的最近のソリューションで、2020年3月から安定版リリースとして提供されており、バージョン5.6**から**Linuxカーネルに直接統合されています。これは、異なるバージョンのカーネルを使用する古いLinuxディストリビューションからのアクセスを妨げるものではない。OpenVPNやIPSecのようなソリューションと比較して、WireGuardは、この記事の最後に見るように、使用がより簡単で、はるかに高速です。



WireGuardの主なポイント





- シンプル、軽量、超高効率！
- UDPのみの運用（特定のファイアウォールを通過する際に不利になる可能性がある）
- クライアント・サーバー・モデルではなく、ピアツーピア・モデルで動作する
- 鍵Exchangeによる認証。秘密鍵/公開鍵によるSSHと同じ原理。
- ChaCha20による対称暗号化、Poly1305によるメッセージ認証、Curve25519、BLAKE2、SipHash24などのアルゴリズムを使用。
- IPv4とIPv6の両方をサポート
- マルチプラットフォーム：Windows、Linux、BSD、macOS、Android、iOS、OpenWRT (ProtonVPNにも実装)
- 他のソリューションが数十万行であるのに対し、わずか4,000行。



暗号の部分については、使用されている様々なアルゴリズムが厳選され、いくつかの方法で監査され、その分野を専門とするセキュリティ研究者によって検査されている。



プロジェクト公式サイト[wireguard.com](https://www.wireguard.com/)



この紹介を読んで、あなたはこの解決策に納得しましたか？あとは読み進めるだけだ！



## II.ラボ・ワイヤーガード図



WireGuardをセットアップするための私のラボを紹介する前に、**WireGuardを使用して2つのリモートインフラ**を相互接続するだけでなく、**リモートクライアントを企業ネットワークやホームネットワーク**などのインフラに接続することも想像できることを知っておく必要があります。これは、先日のチュートリアル「[SynologyでOpenVPN](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)」で紹介したOpenVPNと同じ精神です。



OpenWRTで考えられるように、WireGuardがルーターまたはファイアウォールで直接設定されていない場合、フローがWireGuardのペアに到達するようにポート転送を設定する必要があります。



![Image](assets/fr/034.webp)



では、私の研究室と今日のセットアップについて説明しよう。



ここでは、Debian 11マシンをWireGuardサーバーとして使用し、WindowsクライアントをWireGuard VPNクライアントとして使用します。WireGuardは「ピアツーピア」**モデルで動作するため、クライアントとサーバーの関係について話すのは少し誤解を招くかもしれません。クライアント-サイト**接続をセットアップしようとしているとき、それは少し語弊があります。代わりに、2つのペア、または**2つのWireGuard接続ポイント**があるとします。



つまり、私のWindowsマシンからDebian 11マシンのリモートLANにアクセスすることも、その逆も可能だ。すべてはトンネルの設定とWireGuardピアのファイアウォールに依存する。



この例では、以下のケースを取り上げます： **ホームネットワークに接続されたWindowsピア1から、WireGuard VPNトンネルを経由して会社のサーバーにアクセスするため、会社のネットワークにアクセスしたい**。この場合、次のようになります：



![Image](assets/fr/035.webp)



IPアドレスに換算すると、：





- ホームネットワーク： 192.168.1.0/24
- 企業ネットワーク： 192.168.100.0/24
- **WireGuardトンネルネットワーク**： 192.168.110.0/24


+ トンネル内のピア1（Windows）のIP Address： 192.168.110.2/24


+ トンネル内のピア2(Debian)のIP Address： 192.168.110.121/24



これだけだ！さあ、コンフィギュレーションに取り掛かろう！



**注：デフォルトでは、WireGuardはUDPモードでポート51820**で動作します。



## III WireGuardサーバーのインストールと設定



このチュートリアルでは、Windowsマシンを "クライアント"、Debianマシンを "サーバー "と呼ぶことにする。



### A.Debian11へのWireGuardのインストール



WireGuardのインストール・パッケージはDebian 11の公式リポジトリで入手できるので、パッケージ・キャッシュを更新してインストールするだけです：



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuardサーバー部分と、設定を管理するための便利なコマンドを利用できる各種ツールがインストールされます。



### B.Interface ワイヤーガードの設置



コマンド "wg" **を使って、秘密鍵と公開鍵をgenerateする必要がある。2つのペア、つまりサーバーとクライアント（クライアントも鍵ペアを必要とする）間の認証に不可欠である。**



秘密鍵「**/etc/wireguard/wg-private.key**」と公開鍵「**/etc/wireguard/wg-public.key**」をこのコマンドシーケンスで作成する：



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



公開鍵の値はコンソールで返されます。WireGuard設定ファイルに、秘密鍵の値を**追加する必要があります**。この値を取得するには、以下のコマンドを入力し、値をコピーします：



```
sudo cat /etc/wireguard/wg-private.key
```



設定ファイルを "**/etc/wireguard/**"に作成します。たとえば、WireGuardに関連付けられたInterfaceネットワークが "eth0 "と同じ原理で "wg0 "になると考えれば、このファイルの名前を "**wg0.conf**"とすることができます。



```
sudo nano /etc/wireguard/wg0.conf
```



このファイルでは、まず以下の内容を追加しなければならない（後で完成させるために戻ってくる）：



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



セクション `[Interface]` はサーバー部分の宣言に使用される。以下にいくつかの情報を示す：





- **Address**：VPNトンネル内のInterface WireGuardのIP Address（リモートLANとは異なるサブネット）
- **SaveConfig**：Interfaceがアクティブである間，コンフィギュレーションを保存（保護）する．
- **ListenPort**：WireGuardのリスニングポート。この場合、51820がデフォルトのポートですが、カスタマイズすることもできます。
- **PrivateKey**: サーバの秘密鍵(*wg-private.key*)の値。



ファイルを保存して閉じる。**wg-quick**コマンドで、このInterfaceの名前（ファイル名がwg0.confなのでwg0）を指定して起動する：



```
sudo wg-quick up wg0
```



Debian 11 サーバーの IP アドレスをリストアップすると、"wg0" という名前の新しい Interface と、設定ファイルで定義された IP Address が表示されます：



```
ip a
```



![Image](assets/fr/027.webp)



同じ精神で、"wg show "コマンドでInterfaceの "wg0 "コンフィギュレーションを表示することができる：



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



最後に、Interface wg0 WireGuardの自動起動を有効にする必要があります：



```
sudo systemctl enable wg-quick@wg0.service
```



とりあえず、WireGuardのサーバー側の設定は置いておく。



### C.IP転送を有効にする



私たちの Debian 11 マシンが (ルータのように) **異なるネットワーク間、つまり VPN ネットワークとローカルネットワーク間で **パケットをルーティングできるようにするには、[IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/) を有効にする必要があります。デフォルトでは、この機能は無効になっています。



この設定ファイルを修正する：



```
sudo nano /etc/sysctl.conf
```



ファイルの最後に以下のディレクティブを追加し、保存する：



```
net.ipv4.ip_forward = 1
```



それだけだ。



### D.IPマスカレードを有効にする



サーバーがパケットを正しくルーティングし、WindowsマシンからリモートLANにアクセスできるようにするには、DebianサーバーでIPマスカレードを有効にする必要がある。これは一種のNAT有効化である。この設定をLinuxのファイアウォール上でUFWを通して行おうと思います。UFWは使い慣れたものです（[ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/) ）。



UFWをまだ持っておらず、セットアップしたい場合（Nftablesを使うこともできる）、.NET Frameworkをインストールすることから始めよう：



```
sudo apt install ufw
```



まず、リモート・サーバーのコントロールを失わないように、SSHを有効にする必要がある（ポート番号を合わせる）：



```
sudo ufw allow 22/tcp
```



UDPの51820番ポートも、WireGuardに使用するため、許可する必要がある（ここでもポート番号を合わせる）：



```
sudo ufw allow 51820/udp
```



次に、IPマスカレードを有効にするための設定を続ける。そのためには、ローカル・ネットワークに接続されているInterfaceの名前を取得する必要がある。もし名前がわからなければ、"ip a "を実行するとカードの名前が表示される。私の場合は「**ens192**」です。



![Image](assets/fr/036.webp)



この情報を使うことにする。以下のファイルを編集する：



```
sudo nano /etc/ufw/before.rules
```



ローカル・ファイアウォールのNATテーブルのPOSTROUTING文字列内で、Interface **ens192**（Interfaceの名前に合わせる）のIPマスカレードを有効にするために、ファイルの最後に以下の行を追加する：



```
# NAT - IP masquerade
*nat*
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



写真はその様子：



![Image](assets/fr/037.webp)



この設定ファイルを開いたまま、次のステップに進む。



### E.WireGuard 用 Linux ファイアウォールの設定



同じコンフィギュレーション・ファイルで、企業ネットワーク「192.168.100.0/24」を宣言し、コンタクトできるようにする。以下は、追加する2つのルールである（理想的には、「*# ok icmp code for FORWARD*」セクションの後にルールをグループ化する）：



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



例えば "192.168.100.11 "のように、1つのホストだけを認証したい場合は簡単だ：



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



これでファイルを保存して閉じることができます。あとはUFWを有効にしてサービスを再起動すれば、今回の変更が適用される：



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



これで Debian サーバー設定の最初の部分は完了です。



## IV.Windows用WireGuardクライアント



WireGuardクライアントは、Windows、macOS、Androidなどで利用可能です。これは素晴らしいニュースです。すべてのダウンロードはこちらのページから可能です：[WireGuard クライアント](https://www.wireguard.com/install/).この例では、Windows上でクライアントをセットアップします。LinuxでWireGuardクライアントをセットアップするには、Debianマシンでwg0.confファイルを作成するのと同じ原則に従ってください（NATなどは一切不要です）。



### A.WireGuard Windowsクライアントのインストール



実行ファイルまたはMSIパッケージをダウンロードしたら、インストールは簡単だ。



![Image](assets/fr/038.webp)



### B.WireGuardプロファイルを作成する



まずソフトウェアを開き、新しいトンネルを作成します。これを行うには、"**トンネルの追加**"ボタンの右側にある矢印をクリックし、"**空のトンネルの追加**"ボタンをクリックします。



![Image](assets/fr/028.webp)



設定ウィンドウが開きます。新しいトンネル構成が作成されるたびに、WireGuardはこの構成専用の秘密鍵/公開鍵ペアを生成します。**この設定では、「ピア」、つまりリモートサーバーを宣言する必要があります：**



```
[Interface]
PrivateKey = <la clé privée du PC>
```



特に、このInterface（*Address*）でIP Addressを宣言し、[Peer]ブロックを介してリモートWireGuardサーバーを宣言する必要があります。以下の画像は、Linuxサーバー側で作成した設定ファイルを思い出させるものです。



Interface]`ブロックから始めて、IP Address "**192.168.110.2**"を追加してみよう。サーバーはこのネットワークセグメント上にIP Address "**192.168.110.121**"を持っていることを覚えておこう。これで：



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



次に、3つのプロパティを持つ「Peer」ブロックを宣言する必要がある：



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



写真で見る：



![Image](assets/fr/029.webp)



**Peerブロックについて少し説明する：**





- **PublicKey**: WireGuard Debian 11 サーバの公開鍵です (この値は "*sudo wg*" コマンドで取得できます)。
- **AllowedIPs**：このWireGuard VPNネットワーク経由でアクセス可能なIPアドレス/サブネットで、この場合、自分のWireGuard VPN（*192.168.110.0/24*）およびリモートLAN（*192.168.100.0/24*）に固有のサブネットです。
- **Endpoint**: これはDebian 11ホストのIP Addressで、WireGuardの接続ポイントです（パブリックIP Addressを指定する必要があります）。



最後に、"**Name**"フィールドに名前を入力し（スペースは入れない）、クライアントの公開鍵をコピー＆ペーストする。「**Register**」をクリックする。



### C.WireGuardサーバでクライアントを宣言する



Debianサーバーに戻り、WireGuard設定において「**Peer**」、すなわちWindows PCを宣言するときが来ました。まず最初に、Interface「wg0」**の設定を変更するために、Interface「wg0」**を停止する必要があります：



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



次に、先に作成した設定ファイルを修正する：



```
sudo nano /etc/wireguard/wg0.conf
```



このファイルでは、`[Interface]`ブロックに続いて、`[Peer]`ブロックを宣言する必要がある：



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



この[Peer]ブロックには、Windows 10 PCの公開鍵(**PublicKey**)とPCのInterfaceのIP Address(**AllowedIPs**)が含まれています。このWireGuardトンネルでは、サーバーはWindowsクライアントと連絡するためだけに通信するため、"**192.168.110.2/32**"という値が使用されます。



あとはファイルを保存するだけです(*CTRL+O、Enter、CTRL+X via Nano*)。Interface "wg0 "を再起動する：



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



ピア宣言が機能しているかどうかを確認するには、次のコマンドを使うことができる：



```
sudo wg show
```



リモートホストがWireGuard接続を設定すると、そのIP Addressは「エンドポイント」値に移動します。



![Image](assets/fr/033.webp)



最後に、rootアクセスを制限するために設定ファイルを保護する：



```
sudo chmod 600 /etc/wireguard/ -R
```



### D.最初のWireGuard接続



コンフィギュレーションの準備ができたので、Windows PCからコンフィギュレーションを開始できる。これを行うには、"**WireGuard**"クライアントで、"**Activate**"ボタンをクリックします：接続は "Off "から "On "に変わります**が、これは動作することを意味しません。接続が "Off "から "On "に変わります。 **接続が確立されると、2台のマシンはそれぞれに設定されたInterface WireGuardを介して通信します！



![Image](assets/fr/030.webp)



問題が発生した場合、これは "**Logbook**"タブに表示されます。このため、"*Receiving keepalive packet from peer 1*"というメッセージが表示されます。



![Image](assets/fr/031.webp)



WireGuardの「**ジャーナル**」タブに以下のようなメッセージが表示された場合は、双方で宣言された公開鍵が正しいかどうかを確認する必要があります。



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



リモートPCから、サーバー側のInterface WireGuardのIP Addressと、リモートLAN上のホストにpingを打つことができます。



![Image](assets/fr/032.webp)



### E.パフォーマンスOpenVPNとWireGuardの比較



WireGuard VPNに接続したリモートPCからファイルサーバーにアクセスし、[SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/)経由でファイルを転送して転送速度を確認した。**WireGuardの場合、最大で約45 Mb/sです。**



![Image](assets/fr/025.webp)



同じ条件で、今度はOpenVPN接続（UDP）で、同じ操作を行った場合、スループットはまったく違う：約3MB/s。この違いは明らかです！



![Image](assets/fr/026.webp)



これは興味深いことで、例えばWiFi接続から4G/5G接続に切り替えた場合、再接続は非常に速く、中断は目に見えない。



### F.ボーナス：フルトンネルWireGuard



現在の設定では、トラフィックの一部がVPNを経由し、インターネットブラウジングを含め、残りは顧客のインターネット接続を経由します。WireGuardの**フル・トンネル・モード**に切り替えて、すべてのトラフィックがVPNトンネルを通過するようにするには、設定を少し変更する必要があります。



まず、.NET Frameworkにresolvconfパッケージをインストールする必要がある：



```
sudo apt-get update
sudo apt-get install resolvconf
```



これが終わったら、Debianマシンの "wg0.conf "プロファイルを修正する必要がある：Interfaceを停止し、それを修正し、再起動する。



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



次に、`[Interface]`ブロックに、使用するDNSサーバーを追加する。私の場合は研究室のドメインコントローラーだが、DebianマシンにBind9をインストールしてローカルリゾルバを持つこともできる。



```
DNS = 192.168.100.11
```



ファイルを保存し、Interface を再起動する：



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



最後に、Windows 10ワークステーション上のトンネル設定で、「AllowedIPs」セクションを修正して、すべてがトンネルを通過しなければならないことを示す必要があります。を置き換える：



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



によって：



```
AllowedIPs = 0.0.0.0/0
```



これで「**キルスイッチ**」オプションも有効になることがわかる。



![Image](assets/fr/040.webp)



最後に、この満杯のトンネルを利用して、小さなフローテストを実施した：



![Image](assets/fr/039.webp)



WireGuardのコンフィギュレーションは非常にシンプルで理解しやすく、何よりもメンテナンスが簡単です。 **WireGuardは将来のVPN**と考えられているので、注視しておいた方がいいだろう！また、パフォーマンス面でもOpenVPNと比較してWireGuardに大きなメリットがあることがわかります。



追加ドキュメント：





- [マン - コマンドwg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [男・コマンドwgクイック](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN は稼働中です！おめでとうございます！**