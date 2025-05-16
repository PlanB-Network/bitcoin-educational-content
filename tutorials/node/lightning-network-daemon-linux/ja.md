---
name: Lightning Network Daemon (Linux)
description: Linux上でのLightning Network Daemonのインストールと実行
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning NetworkはBitcoinの第二のLayerであり、特に取引のスピードと低コストのおかげで、電光石火の次元に達することができる。



このチュートリアルでは、Linuxマシン（Ubuntu 24.04ディストリビューション）にLightning Network Daemonの実装をインストールする。



## Lightning Network Daemonとは？



Lightning Network DaemonはLightning Networkの完全なGo実装です。Lightning Labsによって作成され、あなたのマシン上でLightningノードの完全なインスタンスを実行できる。


言い換えれば、この実装では、：





- Lightning Network**との対話コマンドラインを使って、ライトニング・ポートフォリオの作成、支払いチャネルやルートの管理など、さまざまなことをマシンターミナルから直接行うことができます。
- リモートのBitcoinノード、または自分のBitcoin Coreインスタンスをリンクする**：LNDでは、Bitcoinインスタンスをリンクし、バックエンドとして使用することができます。この実装を使用するには、あなたのマシン上で Bitcoin Core インスタンスを実行する必要はありません。




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## なぜ独自のLightningノードを持つのか？


ライトニングは、送金プロセスを最適化し、取引コストを削減するBitcoinオーバーレイである。



ライトニング・ノードをローテーションすることで、主権と自主性を得ることができます。資金をコントロールするのはあなたです：



「鍵でもビットコインでもない。



この意味で、ライトニング・ノードを稼働させることで、データのセキュリティと完全性は以下のように向上する：





- トータル・コントロール**：独自の支払いチャネルを管理し、独自の銀行となり、資産を管理することができます。
- 守秘義務**：お客様のプライバシーを保護するために第三者に依存することなく取引を行うことができます。
- 学習と自律性**：lncli`コマンドのおかげで、Lightningの基本的なプロセスをターミナルから自分で適用することで、よりよく理解することができる。
- 地方分権**：Bitcoin／Lightning Networkの強化・分散化に積極的に取り組む。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


LND実装のインスタンスを我々のマシンで実行するには、2つの選択肢がある。自分のマシンに環境を構築してローカルで実行するか、DockerコンテナからLNDをインストールするかだ。ここでは、最初の選択肢を中心に説明し、Dockerを使った方法は後のチュートリアルで説明する。


## ソースコードからLNDをインストールする



### 前提条件


LNDはGoで書かれているので、LinuxマシンにGoLang環境と必要な依存関係があることを確認する必要がある。





- ハードウェア要件


スムーズでシームレスな体験のためには、LNDライトニング・ノードを動かすのに必要な容量がマシンに必要です。



必要なもの


1. **8GBのRAM**で最適な流動性を実現、


2. *ノードの動作を効率的に管理するためのマルチコアプロセッサ（クアッドコア以上）***、


3. **剪定ノード・モードでは最低5GBのディスク容量**、Bitcoin Coreを実行する場合は1TBのディスク容量（リモート・ノードを使用する場合はオプション）





- 便利な依存関係のインストール


以下のコマンドを実行すると、LNDを実行するために必要なツールをあなたのマシンにインストールすることができる。特に、バージョン管理ツールである `Git` と、ソースコードから LND の実装を実行・ビルドできる `make` をインストールする必要がある。



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- LinuxマシンにGoLangをインストールする**。



このチュートリアルの時点では、LNDのインストールにはGo***のバージョン1.23.6が必要です。



以前のバージョンがすでにインストールされている場合は、それを削除して新しいGoをインストールします。


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- 環境設定


~/.bashrc`ファイルで以下の環境変数を初期化し、LinuxシステムにGoを追加する。



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- インストールの確認**（フランス語）


```bash
go version
```



![go-version](assets/fr/03.webp)


### LNDのGitHubリポジトリをクローンする



gitを使用して、LNDのソースコードのコピーをあなたのマシン上でローカルに取得する。


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### ビルドとインストール



先にインストールした `make` ツールを使って、LND のソースコードから実行ファイルをビルドし、インストールを進めることができる。



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



マシンにLNDをインストールする



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- インストールの確認**（フランス語）



すべてがスムーズに進んだことを確認するために、このコマンドを実行すると、現在実行しているLNDのバージョンが表示されるはずだ。



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- メンテナンスとアップグレード



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **重要**です：LND アップデートには、より新しいバージョンの Go が必要になる場合があります。


### Lightning Network Daemonの設定



Lightning LND ノードの設定は Bitcoin と同様で、ノードの全パラメータを含む設定ファイルで行います。これを行うには、マシンのルートに隠しフォルダ `.LND` を作成し、その中に設定ファイル `LND.conf` を作成します。



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





コンフィギュレーション・ファイルでは、LNDノードを設定することができる。



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## 設定を理解する



LNDノードを正しく完全にインストールするために必要な最小構成を理解することが重要です。



.LND/LND.conf`ファイルの内容から、フィールドの詳細を以下に示す：





- noseedbackup**：LNDにポートフォリオの自動バックアップを実行させるかどうかを選択できます。  このプロパティを`0`に設定すると、リストア情報を個人的に選択した安全な場所に手動で保存することができます。





- debuglevel**：アクション中にエラーが発生した場合のエラーとログの詳細レベルを定義できます。





- Bitcoin.active**：Bitcoinノードとして動作し、Bitcoinネットワークと相互作用するようLNDに指示する。





- Bitcoin.Mainnet**：Bitcoinのメインネットワーク(Mainnet)に接続するLNDを指定します。Bitcoin SignetとBitcoin Regtestのネットワークに対して、それぞれ`bitcoind.signet`と`bitcoind.regtest`の値を設定できます。





- Bitcoin.node**：LNDが接続するBitcoinノードの種類を指定する。





- Bitcoin.rpcuser**と**Bitcoin.rpcpassword** ：を表す。


Bitcoinノードに接続するためのログイン（ユーザー、パスワード）をそれぞれ設定します。





- bitcoind.zmqpubrawblock**と**bitcoind.zmqpubrawtx**：それぞれ、Bitcoinネットワーク上の新しいブロックとトランザクションに関する通知を受け取るためのZeroMQエンドポイントを定義する。




## LNDでインストールを確認する



おそらく、プロセスが成功したことを確認し、Lightning Networkと同期してノード情報を最新に保つことを望むだろう。



LNDの実装を開始し、あなたのノードに関する情報を取得するには、単にコマンドを入力します：


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## LNDでのアクション



インストールが完了し、チェックされたら、使用を開始できます。


ここでは、必要不可欠なコマンドを紹介しよう。



### ポートフォリオを作成する


ライトニング・ポートフォリオは、資金を管理するためのあらゆる行動の第一歩である。



⚠️ **重要**です：24語の**seedフレーズ**を注意深くメモしてください。問題が発生した場合、資金を回収するために必要になります。



また、LNDノードを再起動したときに`lncli unlock`コマンドでロックを解除できるように、Walletのパスワードも保存しておくこと。



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### 残高の確認



ターミナルから直接口座の照会ができます：



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### ノードに関する情報



以下のコマンドを使って、自分のノードでどのチャンネルがアクティブかを調べます。



```bash
lncli listchannels
```



また、自分が接続しているノードのリストを取得することもできる。



```bash
lncli listpeers
```



### チャネル管理



ライトニング・チャンネルは、Lightning Networkの他のノードと**直接、ペア・バイ・ペア**で接続することができます。このチャンネルでは、Exchange Satoshisをチャンネル容量まで自由に使用することができます。



### ノードに接続する



他のLightningノードに接続することは、Lightningのパワーに積極的に参加し、その恩恵を受けようとするならば、基本的な行動です。



ピア（ライトニング・ノード）に接続するには、3つの情報が必要です：




- ノードの公開鍵**：これはBitcoinネットワークにおけるノードの一意な識別子である；
- IP** ：ノードがインストールされているマシンのIP；
- PORT** ：  このノードとの通信を許可するマシンで開いているポート。



amboss](https://amboss.space/)は、Lightningノードの情報を一覧できるプラットフォームで、接続するノードを見つけることができる。



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




自分のシステムの完全性を保つために、**信頼できるノード**に接続するようにしてください。適切な接続を選択するための推奨事項は以下の通りです。





- 地理的分散**：さまざまな地域のノードに接続。





- 評判**：可用性の高いノードを選ぶ。





- キャパシティ**：流動性の高いノットを選ぶ。





- チャージ**：小切手発行手数料。


### 決済チャネルを開設する


支払いチャネルを開くには、ピアノードに**接続**されていることを確認し、このチャネルでブロックしたい**容量**（サトシの量）を定義します。



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### ライトニングInvoiceの作成



ライトニングInvoiceは、ライトニングWalletでサトシの受け取りを希望する文字列を表します。


独自のノードでLightningインボイスを作成することで、（地理的および個人的な）データを保護し、資金の管理を100％自主的に行うことができます。



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### ライトニングInvoiceの支払い



```bash
lncli payinvoice <FACTURE>
```


### チャンネルを閉じる



現在のノードでアクティブなチャンネルを閉じるには2つの方法がある。





- 協調閉鎖**：これはあなたのノードが支払いチャネルから撤退することを希望していることを示すもので、進行中のタスクが完了し、資金の損失を避けるためにデータがバックアップされていることを確認します。


```
lncli closechannel <ID_CANAL>
```




- 強制閉鎖**：⚠️ 可能な限り回避してください。この措置により、支払チャネルで進行中のプロセスが中断され、資金が失われるリスクが高まります。


```
lncli closechannel --force <ID_CANAL>
```


## LNDノードのベストプラクティスと安全性。


Bitcoin/Lightningノードを使用する際には、安全性が最も重要です。以下は、設置の安全性を強化するためのいくつかのポイントです：





- seedフレーズ`は安全なオフラインの場所に保管してください。





- ~/.LND/channel.backup`ファイルを定期的にバックアップしてください：このファイルは、あなたのノードで新しいチャンネルがオープンされる (または古いチャンネルがクローズされる) たびに、チャンネルの状態を保存します。


⚠️ データ損失やノード障害が発生した場合、チャネルを復元し、決済チャネルでブロックされた資金を回復することができます。



このファイルのバックアップパスを指定すれば、以下のコマンドで資金を復元できる：


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Lightning Walletの復元ワードとパスワードが保存されていることを確認してください。
- システムを最新の状態に保つ。



## 現在のトラブルシューティング


### 頻発する問題




- bitcoind 接続エラー** ：RPCのログイン情報を確認する
- 同期がブロックされた** ：インターネット接続を確認してください
- パーミッションエラー**：フォルダ `~/.LND` の権限を確認してください。




このチュートリアルはここまでです。Lightningについてもっと知りたいという方には、Lightning Networkのコンセプトと実践について理解を深めていただくための入門コースをご用意しています。




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb