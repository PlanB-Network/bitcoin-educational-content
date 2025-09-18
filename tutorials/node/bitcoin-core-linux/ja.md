---
name: Bitcoin Core (Linux)
description: Linux上でBitcoin coreを使って自分のノードを動かす
---

![cover](assets/cover.webp)


## Bitcoin coreで自分のノードを動かす


Bitcoinの紹介とノードの概念、Linuxでの包括的なインストールガイド。


Bitcoinの最もエキサイティングな側面のひとつは、自分自身でプログラムを実行できることであり、その結果、ネットワークと公開トランザクションLedgerの検証に粒度レベルで参加できることである。


Bitcoinはオープンソースのプロジェクトとして、2009年から自由に利用でき、一般に配布されている。発足から17年近くが経過した現在、Bitcoinは強力な有機的ネットワーク効果の恩恵を受けて、強固で止められないデジタル通貨ネットワークとなっている。彼らの努力とビジョンに対して、Satoshiナカモトは感謝に値する。ちなみに、Bitcoinのホワイトペーパーはアゴラ256（注：大学にもあります）で公開しています。


### 自分の銀行になる


Bitcoinの信奉者にとっては、自分のノードを運営することが不可欠である。誰の許可も得ることなく、Blockchainを最初からダウンロードし、Bitcoinプロトコルに従ってAからZまでのすべての取引を検証することが可能である。


このプログラムには独自のWalletも含まれている。したがって、私たちは、仲介者や第三者なしに、ネットワークの残りの部分に送信するトランザクションを制御することができます。あなた自身が銀行なのです。


そこで、この記事の残りの部分は、Bitcoin core（最も広く使われているBitcoinソフトウェアのバージョン）を、特にUbuntuやPop!OSのようなDebian互換のLinuxディストリビューションにインストールするためのガイドです。このガイドに従って、あなたの個人主権に一歩近づいてください。


## Debian/Ubuntu 用 Bitcoin core インストールガイド


**前提条件


- 最低6GBのデータストレージ（prunedノード） - 1TBのデータストレージ（Full nodeノード）
- 初期ブロック・ダウンロード*（IBD）には少なくとも24時間かかると思ってください。この操作はprunedノードであっても必須である。
- prunedノードであっても、IBDの帯域幅を～600GBにする。


*注：💡***以下のコマンドはBitcoin coreバージョン24.1であらかじめ定義されています。


### ファイルのダウンロードと検証



- [ダウンロード](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz` と `SHA256SUMS` と `SHA256SUMS.asc` ファイルをダウンロードする（当然、ソフトウェアの最新バージョンをダウンロードする必要がある）。



- ダウンロードしたファイルがあるディレクトリでターミナルを開く。例: `cd ~/Downloads/`.



- コマンド`sha256sum --ignore-missing --check SHA256SUMS`を使って、バージョンファイルのチェックサムがチェックサムファイルにリストされていることを確認する。



- このコマンドの出力には、ダウンロードしたバージョンファイルの名前の後に `OK` が続くはずである。Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz:OK`.



- コマンド `sudo apt install git` を使って git をインストールする。次に、`git clone https://github.com/Bitcoin-core/guix.sigs` コマンドを使って、Bitcoin core署名者のPGP鍵があるリポジトリをクローンする。



- gpg --import guix.sigs/builder-keys/*` コマンドを使用して、すべての署名者のPGP鍵をインポートする。



- コマンド`gpg --verify SHA256SUMS.asc`を使って、チェックサムファイルが署名者のPGP鍵で署名されていることを確認する。



各有効な署名は、次の行で始まる行を表示する：gpg: Good signature`で始まる行と、次の行で終わる行が表示される：主キーの指紋：133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (Pieter WuilleのPGP鍵指紋の例)。


**注💡：すべての署名鍵が「OK」を返す必要はない。実際、必要なのは1つだけかもしれません。PGP検証のしきい値を決めるのはユーザーです。


警告は無視してもいい：



- この鍵は信頼できる署名で認証されていません。



- その署名が所有者のものであることを示すものはない。


### Bitcoin coreグラフィカルInterfaceのインストール



- ターミナルで、Bitcoin coreバージョンのファイルがあるディレクトリのまま、`tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` コマンドを使って、アーカイブに含まれるファイルを展開します。



- コマンド`sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*` を使って、先に展開したファイルをインストールする。



- コマンド `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev` を使って、必要な依存関係をインストールする。



- Bitcoin-qt`コマンドを使って_bitcoin-qt_ (Bitcoin core graphical Interface)を起動する。



- prunedノードを選択するには、_Limit Blockchain storage_にチェックを入れ、保存するデータの上限を設定する：


![welcome](assets/fr/02.webp)


### 第1部の結論：インストレーション・ガイド


Bitcoin coreがインストールされたら、トランザクションを検証し、新しいブロックを他のピアに送信することによってBitcoinネットワークに貢献するために、できるだけ稼働させておくことが推奨される。


しかし、受信したトランザクションと送信したトランザクションを検証するためだけであっても、ノードを断続的に稼働させ、同期させることは良い習慣であることに変わりはない。


![Creation wallet](assets/fr/03.webp)


## Bitcoin coreノードにTorを設定する


**注意💡:** このガイドは、Ubuntu/Debian互換のLinuxディストリビューション上のBitcoin core 24.0.1用に設計されています。


### Bitcoin coreのためのTorのインストールと設定


まず、匿名通信のためのネットワークであるTorサービス（The Onion Router）をインストールする必要がある。Torを含むオンラインプライバシー保護ツールの紹介については、このトピックに関する記事を参照してください。


Torをインストールするには、ターミナルを開き、`sudo apt -y install tor`と入力する。インストールが完了すると、通常はバックグラウンドで自動的にサービスが起動します。コマンド `sudo systemctl status tor` で正しく起動しているか確認してください。応答は `Active: active (exited)` と表示されるはずです。この機能を終了するには `Ctrl+C` を押してください。


**ヒント:** いずれにせよ、ターミナルで以下のコマンドを使ってTorを起動、停止、再起動することができます：


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


次に、`Bitcoin-qt`コマンドでBitcoin coreのグラフィカルなInterfaceを起動しよう。次に、Torプロキシを経由して接続をルーティングするソフトウェアの自動機能を有効にする：設定 > ネットワーク_」を選択し、「SOCKS5プロキシ経由で接続する（デフォルトのプロキシ）_」と「Torオニオンサービス経由でピアに接続するために別のSOCKS5プロキシを使用する_」をチェックします。


![option](assets/fr/04.webp)


Bitcoin coreは、Torがインストールされているかどうかを自動的に検出し、インストールされている場合は、デフォルトで、IPv4/IPv6ネットワーク（clearnet）を使用しているノードへの接続に加えて、同じくTorを使用している他のノードへのアウトバウンド接続を作成します。


*注💡：***表示言語をフランス語に変更するには、「設定」の「表示」タブを開きます。


### 高度なTor設定（オプション）


Bitcoin coreを設定することで、ピアとの接続にTorネットワークのみを使用し、ノードを介した匿名性を最適化することが可能です。グラフィカルなInterfaceにはこのための機能が組み込まれていないので、手動で設定ファイルを作成する必要があります。設定]、[オプション]の順に進みます。


![option 2](assets/fr/05.webp)


ここで、_Open configuration file_をクリックする。Bitcoin.conf`テキストファイルに`onlynet=onion`という行を追加して保存する。このコマンドを有効にするには、Bitcoin coreを再起動する必要がある。


そして、Bitcoin coreがプロキシ経由で着信接続を受け取れるようにTorサービスを設定し、ネットワーク上の他のノードが私たちのマシンのセキュリティを損なうことなく、私たちのノードを使用してBlockchainのデータをダウンロードできるようにする。


ターミナルで`sudo nano /etc/tor/torrc`と入力してTorサービスの設定ファイルにアクセスする。このファイルで `#ControlPort 9051` という行を探し、`#` を削除して有効にする。次にファイルに2行追加します：


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


ファイルを保存中に終了するには `Ctrl+X > Y > Enter` を押してください。ターミナルに戻って、`sudo systemctl restart tor`コマンドを入力してTorを再起動する。


この設定により、Bitcoin coreはTorネットワーク(Onion)を通してのみ、ネットワーク上の他のノードと発着信接続を確立できるようになります。これを確認するには、_Window_タブをクリックし、_Peers_をクリックします。


![Nodes Window](assets/fr/06.webp)


### その他のリソース


結局のところ、Torネットワーク（`onlynet=onion`）だけを使うと、Sybil Attackに対して脆弱になる可能性がある。そのため、この種のリスクを軽減するためにマルチネットワーク構成を維持することを推奨する人もいる。さらに、すべてのIPv4/IPv6接続は、先に示したように、いったん設定されるとTorプロキシを経由してルーティングされます。


別の方法として、Torネットワークだけに留まり、Sybil Attackのリスクを軽減するために、`addnode=trusted_address.onion`という行を追加することで、`Bitcoin.conf`ファイルに他の信頼できるノードのAddressを追加することができます。複数の信頼済みノードに接続したい場合は、この行を複数回追加することができる。


Bitcoinノードのログを見るには、Bitcoin.confファイルに`debug=tor`を追加してください。これでデバッグログに関連するTorの情報が追加され、_Information_ウィンドウの_Debug File_ボタンで見ることができます。また、ターミナルで `bitcoind -debug=tor` コマンドを使って直接ログを見ることもできます。


**ヒント💡：**ここに興味深いリンクがあります：


- [トーアとBitcoinとの関係を説明するウィキのページ](https://en.Bitcoin.it/wiki/Tor)
- [ジェイムソン・ロップによるBitcoin coreコンフィギュレーション・ファイル・ジェネレーター](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [ジョン・アタックによるTor設定ガイド](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


いつも通り、何か質問があれば、遠慮なくアゴラ256のコミュニティで共有してください。私たちは、今日よりも明日、より良くなるために共に学びます！