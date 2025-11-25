---
name: 道場
description: プライバシーと自律性のためのオープンソースBitcoinノード
---

![cover](assets/cover.webp)



*このチュートリアルは、[足軽の公式ドキュメント](https://ashigaru.rs/docs/)をベースに、私が引き継いで拡張したものです。より分かりやすくするために全項目を書き直し、さらに詳細な説明を加え、初心者の方にも分かりやすいようにイラストを添えました*。



---

Dojoは、Bitcoin coreノードをベースとした、特定のプライバシー指向のBitcoinウォレットのバックエンドサーバーとして動作するように設計されたオープンソースのプログラムです。歴史的には、Whirlpool（CoinJoin）、Ricochet、Stonewall、PayNym...のような高度なプライバシー機能を提供するモバイルWalletであるSamourai Walletで動作するように開発されました。Samourai Walletは開発者の逮捕により閉鎖されましたが、そのコミュニティの後継である**あしがるWallet**が引き継ぎ、Bitcoin使用時にデータを管理したいユーザーに完全な体験を提供するためにDojoに依存し続けています。



![Image](assets/fr/01.webp)



実用的には、DojoはWalletとBitcoinネットワークのゲートウェイとして機能する。Dojoがなければ、軽量のモバイルWalletは、あなたのUTXOの状態や履歴を取得するために、あるいはあなたの取引をブロードキャストするために、第三者のサーバーに問い合わせなければならない。これは、第三者のサーバーに依存し、機密データ（使用されたアドレス、金額、支払い頻度など）が漏れることを意味します。Dojoでは、このサーバーを自分でホストし、自分のBitcoinノードに直接接続します。こうすることで、すべてのポートフォリオ・リクエストは、仲介者なしに、あなたがコントロールするインフラを通過し、あなたの機密性と主権を強化します。



## 道場開設の条件



Dojoサーバーを立ち上げるのに、超強力なマシンは必要ありません。エントリーレベルのコンピュータと安定したインターネット接続、そして24時間365日電源を入れっぱなしにできる環境があれば、誰でも道場を立ち上げることができます。



### マシンタイプを選択



を使うことができる：




- ラップトップ
- デスクトップコンピュータ；
- ミニPC（Intel NUC、Lenovo Thincentre Tinyなど）。



それぞれの選択肢には長所と短所がある：




- 価格：再生品のミニPCやデスクトップは、新品のノートPCよりも安いことが多い。
- フットプリント：ミニPCは場所をとりません。
- 電源Supply：ノートPCにはバッテリーが搭載されているため、ミニPCと違って停電時にシャットダウンしないという利点がある。
- アップグレード性：バーボンは一般的に、メモリの追加やHardディスクの交換が簡単にできる。



機材選びの詳細については、このコースを受講することをお勧めする：



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### 推奨機材



新しいマシンを買う必要はありません。以下の仕様の再生コンピューターは、シングルボードエレクトロニクス（Raspberry Piなど）よりもはるかに優れたパフォーマンスを発揮します。



*最低スペック：***。




- X86-64アーキテクチャ（64ビットプロセッサ）。
- 2 GHzデュアルコアプロセッサまたはそれ以上。
- 最小8GB RAM。
- 2TB以上のNVMe SSD（BitcoinのBlockchainと必要なインデックスを保存するため）。



**推奨オペレーティングシステム **




- Ubuntu 24.04 LTSのようなDebianベースのディストリビューション。



**推奨機材




- HP EliteDesk / EliteBook
- デル・オプティプレックス
- レノボThinkCentre / ThinkPad
- インテル NUC
- その他



他のハードウェア構成でDojoサーバーを実行することは完全に可能です。しかし、最高のパフォーマンスを得て問題を抑えるためには、 上記の推奨事項に従うことをお勧めします。



このチュートリアルでは、Intel Pentium Dual-Core G4400Tプロセッサー、8GB RAM、2TB SSDを搭載した古いThinkCentre Tinyを使用します。



## 1 - Ubuntuのインストール



*すでに設定されているデバイスにDojoをインストールする場合は、この手順を省略して直接手順2.*に進むことができます。



選んだハードウェアを準備したら、いよいよオペレーティング・システムをインストールしよう。Debianのディストリビューションであればほぼ何でも使えるが、UbuntuのLTSバージョンを選ぶことをお勧めする。以下はその手順だ：



### 1.1. ブート可能なUSBキーを作成する



すでに動作しているコンピュータ（いつものマシン）から、Ubuntu LTS ISOイメージ[公式サイトから](https://ubuntu.com/download/desktop)をダウンロードします（執筆時点では`24.04`ですが、他のものがあれば最新のものを使ってください）。



![Image](assets/fr/02.webp)



8GB以上のUSBキーをこのコンピュータに挿入し、[Balena Etcher](https://etcher.balena.io/)などのソフトウェアを使用してブータブルキーを作成します。先ほどダウンロードしたUbuntu ISOイメージを選択し、USBキーをターゲットデバイスとして選択し、作成プロセスを開始します（数分かかる場合がありますので、気長にお待ちください）。



![Image](assets/fr/03.webp)



電源を切ったコンピュータ（Dojoを実行したいコンピュータ）にブータブルUSBキーを挿入します。マシンを起動し、すぐにキーボードの**F12**または**F10**（モデルによる）を押してブートメニューにアクセスします。次に、コンピュータの起動順序で優先デバイスとしてUSBキーを選択します。



![Image](assets/fr/04.webp)



### 1.2. オペレーティング・システムをインストールする。



Ubuntuのホーム画面が表示されます。Ubuntu*を試すかインストールする」を選択します。



![Image](assets/fr/05.webp)



その後、古典的なUbuntuのインストール手順に従う：




- 言語を選択します。
- キーボードの種類を選択します。
- RJ45ケーブルで接続している場合は、Wi-Fiの設定は不要です。
- Ubuntu*のインストール」をクリックし、サードパーティ製ソフトウェア（Wi-Fiドライバ、マルチメディアコーデックなど）をインストールするオプションにチェックを入れる。
- ウィザードがインストールの種類を尋ねたら、「*Erase disk and install Ubuntu*」を選択します。 **警告**: この操作はディスクの内容を完全に消去します。選択したディスクがDojo用のNVMe SSDに対応していることをよく確認してください。
- 簡単なユーザー名を作成する（例："*loic*"）。
- マシンに名前を付ける（例："*dojo-node*"）。
- 強力なパスワードを設定し、安全に保管する。
- セキュリティを強化するために、"*Request my password to log in*"オプションを有効にしてください。
- タイムゾーンを指定し、「*インストール*」をクリックします。
- インストールが完了するまで待ちます。完了後、システムは自動的に再起動します。
- コンピュータの再起動時にUSBインストールキーを取り外してください。



Ubuntuのインストールプロセスの詳細については、専用のチュートリアルを参照してください：



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. システム・アップデート



最初のブート後、***Ctrl + Alt + T*** キーの組み合わせでターミナルを開き、以下のコマンドを実行してシステムをアップデートする：



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2.外構工事



Dojo が正常に動作するためには、システム上に特定のソフトウェアブリックが存在する必要があります。これらはソフトウェア・リポジトリーの管理、通信、アーカイブの解凍、Docker コンテナー内での Dojo の実行に使用されます。これらの操作はすべてターミナルで行います。



### 2.1.準備



次のコマンドを実行すると、個人用フォルダに戻ります。これは一連のインストールを実行する前の良い習慣です。



```bash
cd ~/
```



ソフトウェアをインストールする前に、マシンで利用可能なソフトウェアのデータベースが最新であることを確認してください。これにより、旧バージョンのインストールを避けることができます。



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. ユーティリティのインストール



いくつかのツールをシステムに追加する必要がある：




- apt-transport-https`：HTTPS経由で安全にパケットをダウンロードできる。
- `ca-certificates`: 暗号化された接続に必要な証明書を管理する。
- curl`：インターネットからファイルを取得する
- `gnupg-agent`: GPG 鍵管理用
- software-properties-common`: APTリポジトリを操作するためのユーティリティを提供する。
- unzip`: ZIP 形式のファイルを解凍する。



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



インストール中、システムから確認を求められることがあります。y*」キーを押し、「*Enter*」を押してください。



![Image](assets/fr/08.webp)



### 2.3. トルソックスをインストールする



Torsocksは、特定のコマンドをTorネットワーク経由で実行することを可能にし、通信の機密性を向上させる。



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. DockerとDocker Composeをインストールする。



DojoはDockerコンテナ内で動作します。これは、各サービスが独立した環境で隔離され、メンテナンスやセキュリティが簡素化されることを意味します。これを行うには、Dockerと、複数のコンテナを同時に管理できるDocker Composeツールをインストールする必要があります。



#### Docker署名キーを追加する



Dockerは独自のデジタル署名キーを提供する。これを追加することで、ダウンロードされたパッケージの信頼性を検証します。



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### 公式Dockerリポジトリが追加されました



次に、公式のDockerパッケージがどこにあるかをシステムに教える必要があります。このコマンドは、パッケージマネージャの設定に新しいリポジトリを追加します。



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### DockerとDocker Composeのインストール



これで主要なDockerコンポーネントをインストールできる。



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### ユーザー認証



デフォルトでは、管理者権限で実行されたコマンドのみがDockerを起動できる。より便利にするために、現在のユーザーを "*docker*"グループに追加することをお勧めする。これにより、毎回`sudo`と入力しなくてもDockerを使うことができる。



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3.シングルユーザー作成（オプション）



システムのセキュリティを向上させたい場合は、Dojo を実行するためだけの別のユーザーを作成することをお勧めします。Dojoでセキュリティ上の問題が発生しても、メインのアカウントが直接危険にさらされることはありません。



### 3.1. ユーザーアカウントの作成



以下のコマンドは、"*dojo*"という新しいユーザーを作成する。このユーザーはホームディレクトリ `/home/dojo` を持ち、bashターミナルにアクセスできる。また、管理者コマンドを実行できるようにsudoグループに追加される。



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2.パスワードの設定



このアカウントには強力なパスワードを割り当てることが重要だ。理想的には、Bitwardenのようなパスワード・マネージャーを使って、Hardから推測できるような長い組み合わせをgenerateにすることです。



```bash
sudo passwd dojo
```



その後、選択したパスワードを入力し、2回目の確認を求められます。



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3.ユーザーにDockerの使用を許可する



ユーザー「*dojo*」がDojoの実行に必要なコンテナを起動できるようにするには、そのユーザーをDockerグループに追加する必要がある。これにより、各コマンドの前に `sudo` を付ける必要がなくなる。



```bash
sudo usermod -aG docker dojo
```



### 3.4.システム再起動



グループの変更を有効にするには、マシンを再起動する必要があります。



```bash
sudo reboot
```



### 3.5.新しいユーザーでログイン



システムが再起動したら、***dojo***ログインと先ほど定義したパスワードでログインしてください。以降のすべての手順は、この専用アカウントから実行する必要があります。



## 4.Dojoをダウンロードして確認する



Dojo をインストールする前に、ファイルが公式の開発者から提供されたものであり、変更されていないことを確認することが重要です。このステップでは、ファイルの信頼性と完全性を確認するために PGP とハッシュを使用します。



### 4.1. 開発者のPGP鍵をインポートする。



開発者の公開鍵を Tor 経由でダウンロードし、ローカルのキーチェーンにインポートします。この鍵は Dojo ファイルに関連付けられた署名を検証するために使用されます。



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Dojoの最新バージョンをダウンロードする。



Dojo のソースコードを含む圧縮アーカイブを取得します。この例では、最新バージョンは `1.27.0` です。[公式 GitHub リポジトリの最新バージョンはこちら](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) に従ってコマンドを修正してください。



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3.指紋と署名のダウンロード



開発者は、アーカイブのデジタル指紋をリストアップしたファイルと、彼らのPGPキーで署名されたファイルを公開しています。ファイルをローカルで比較するためにダウンロードしてください。



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4.PGP署名の確認



フィンガープリント・ファイルがインポートされた鍵によって署名されていることを確認する。



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



正しい結果は、鍵 `E53AD419B242822F19E23C6D3033D463D6E544F6` と関連するAddress `dojocoder@pm.me` による有効な署名を表示する。鍵が認証されていないという警告が表示されるかもしれないが、無視して構わない。



一方、署名が無効な場合は、直ちにインストール作業を中止し、最初からやり直してください。



![Image](assets/fr/17.webp)



### 4.5.アーカイブの完全性をチェックする



ダウンロードしたファイルのSHA256フィンガープリントを計算し、フィンガープリント・ファイルを開いて2つの値を比較する。



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



2つのフィンガープリントが同じなら、アーカイブが変更されていないことを確信できる。異なる場合は、それ以上進まず、ファイルを削除してください。



![Image](assets/fr/18.webp)



### 4.6.ファイルの抽出と整理



検証が正常に完了したら、アーカイブを解凍してDojoインストール専用のフォルダを用意します。



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7.不要なファイルのクリーンアップ



不要になった一時ファイルやアーカイブを削除し、環境をクリーンに保つ。



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5.道場の構成



Dojo はバックエンドサーバーで、ポートフォリオと対話し、Bitcoin ノードを管理するためのいくつかのサービスをまとめています。その設定は複雑ですが、このプロジェクトでは以下のコンポーネントを自動的にインストールして設定するシンプルな方法を提供しています：




- Dojo（メインAPI）
- Bitcoin core（Bitcoinノード完成）
- BTC-RPCエクスプローラー（Web Block explorer）
- フルクラムインデクサー（ブロックとトランザクションの迅速なインデックス作成）
- フルクラムのエレクトラムサーバーがTorネットワークで利用可能
- ローカルネットワークで利用可能なフルクラムエレクトラムサーバー
- 管理資格



### 5.1. 管理資格



さまざまなサービスへのアクセスを確保するためには、generateといういくつかのユニークな識別子が必要だ：




- bitcoind_rpc_user`。
- bitcoind_rpc_password`。
- mysql_root_password`。
- mYSQL_USER
- mysql_password`。
- nODE_API_KEY`
- node_admin_key`。
- ノード_jwt_secret`。



これらの識別子は、**ユニークで**なければならず（これは非常に重要です：複数のサービスで同じパスワードを使用してはなりません）、数字、大文字、小文字（英数字）のみで構成され、高いレベルのセキュリティを保証するために40文字程度でなければなりません。繰り返しになるが、パスワード・マネージャーを使うことを強くお勧めする。



### 5.2.設定ファイルへのアクセス



Dojo の設定ファイルは `conf/` フォルダにあります。このディレクトリに移動します：



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3.Bitcoin coreの構成



Bitcoin core設定ファイルをnanoテキストエディタで開く：



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



このファイルに、生成された識別子を入力する：



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***`your-ID-here`と`your-password-here`を自分のログイン名（強力なパスワード付き）に置き換えてください。



また、Bitcoin coreが使用するキャッシュメモリのサイズを調整することで、パフォーマンスを向上させることも可能です（RAMに余裕があれば、より多く使用することもできます）：



```
BITCOIND_DB_CACHE=2048
```



変更を保存してエディターを閉じるには




- Ctrl+Xキーを押す
- タイプ `y`
- 次に "*Enter*"を押す



### 5.4.MySQL の設定



次にMySQLデータベース設定を開く：



```bash
nano docker-mysql.conf.tpl
```



ログイン情報を入力してください：



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***「your-ID-here`」と「your-password-here`」を自分のログイン名（強力でユニークなパスワード）に置き換える。



同じように保存する（`Ctrl + X`, `y`, "*Enter*"）。



![Image](assets/fr/23.webp)



### 5.5.フルクラムインデクサーの構成



以下のファイルを開く：



```bash
nano docker-indexer.conf.tpl
```



パラメータを追加してFulcrumを有効にし、Dojoに正しく統合する：



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



次に、設定によって2つの可能性があります。Dojoが普段使っているコンピュータとは別のマシン（専用機やサーバなど）にインストールされている場合、ローカルネットワークにIP Addressを入力します：



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



マシンのローカルIP Addressを調べるには、別のターミナルを開き、以下のコマンドを入力する：



```bash
hostname -I
```



第二の可能性：Dojoを普段使っているパソコンで直接実行する場合は、設定ファイルにあるデフォルト値のままにしておきます：



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



保存してエディターを終了する（`Ctrl + X`, `y`, "*Enter*"）。



### 5.6.ノードサービス設定



最後に、メインのDojoサービスの設定を開きます：



```bash
nano docker-node.conf.tpl
```



ログイン情報を入力してください：



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***your-password-here` をあなた自身の認証情報（強力でユニークなパスワード）に置き換えてください。



![Image](assets/fr/26.webp)



それからローカル・インデクサをアクティブにする：



```
NODE_ACTIVE_INDEXER=local_indexer
```



保存してエディターを終了する（`Ctrl + X`, `y`, "*Enter*"）。



### 5.7.ログイン管理



設定が完了したら、生成されたすべての識別子を保存する必要はない。絶対に保存しなければならないのは：



```
NODE_ADMIN_KEY
```



このログインは、後で道場維持ツールにログインできるようにします。他のすべてのログインはパスワードマネージャや手書きのメモから削除することができます。これらのログイン名は、Dojo 設定ファイルからアクセス可能です。



## 6.道場設置



この段階で、Dojoがあなたのマシンにインストールされ、起動されます。この操作により、いくつかのサービス（Bitcoin core、フルクラムインデクサー、Dojoバックエンドなど）が起動し、Blockchain Bitcoinの完全な同期が開始されます。ハードウェアやインターネット接続によっては、数日かかる場合があります。



### 6.1.Dockerが正しく動作しているか確認する



インストールを開始する前に、Dockerが動作可能であることを確認する。以下のコマンドを実行する：



```bash
docker run hello-world
```



このコマンドは、小さなテスト・コンテナをダウンロードして起動する。すべてが正しく動作すれば、以下のようなメッセージが表示されるはずだ：



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



このメッセージが表示されない場合は、.NET Frameworkでマシンを再起動してください：



```bash
sudo reboot
```



その後、**dojo**アカウントにログインし直し、テストコマンドを再度実行してください。エラーが続く場合は、Dockerが正しくインストールされていません。この場合、Dockerをインストールするステップ `2.4.` に戻り、各コマンドを注意深く確認してください。



### 6.2.Dojoのインストールディレクトリに移動します。



インストールに必要なスクリプトは `my-dojo` フォルダにあります。このディレクトリに移動する：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



ls` コマンドを使用して、`dojo.sh` ファイルが存在することを確認する。これは Dojo のインストールとすべてのサービスの起動を自動化するメインスクリプトです。



![Image](assets/fr/29.webp)



### 6.3.インストール開始



を実行してインストールを開始する：



```bash
./dojo.sh install
```



y`を押し、"*Enter*"を押してインストールを確認する。



![Image](assets/fr/30.webp)



このスクリプトは：




- をダウンロードし、必要なDockerコンテナを起動する、
- Bitcoin coreを初期化し、Blockchainの同期を開始する、
- 取引と住所を追跡するために、フルクラムのインデクサーを起動する、
- Dojo バックエンドとその API を有効にします。



bitcoind`、`soroban`、`nodejs`、`fulcrum` などのカラフルな参照で、ログがスクロールしていくのが見えるだろう。このスクロールは、Dojo が起動し、さまざまなサービスを実行し始めていることを示している。



![Image](assets/fr/31.webp)



### 6.4.ログ表示を終了する



ログはターミナルにリアルタイムで表示されます。Dojo がバックグラウンドで実行中にコマンドプロンプトに戻るには、 ：



```
Ctrl + C
```



ご心配なく：ログ表示を停止してもサービスは停止しません。DockerはバックグラウンドでDojoを実行し続けます（IBDを継続させたい場合は、コンピュータを停止する必要は当然ありません）。



### 6.5.イニシャル・ブロック・ダウンロード（IBD）の理解



起動時に Bitcoin core は 2009 年以降の Blockchain をすべてダウンロードし、検証する必要がある。このステップは***Initial Block Download* (IBD)***と呼ばれます。これは、Dojoノードが各Bitcoinブロックとトランザクションを独立して検証できるようにするために不可欠です。



この同期の期間はいくつかの要因に左右される：




- プロセッサのパワーと使用可能なRAMメモリの量、
- ディスクの速度、
- ノードが接続するピアの数と質、
- インターネット接続の速度



実際には、この作業には通常**2～7日**かかります。この間、マシンを起動し続けることができます。マシンの電源が入っている時間が長ければ長いほど、同期は早く完了します。Bitcoin coreのログを参照するか、Dojoメンテナンスツール（次項参照）をインストールして、定期的に同期状況を確認することをお勧めします。



IBD、そしてより一般的に、Bitcoinノードの操作と役割についての知識を深めるために、このコースをご覧になることをお勧めする：



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7.同期モニタリング



Dojoを初めてインストールする場合、Blockchain Bitcoin (*IBD*)の完全なダウンロードと、フルクラムによるこのBlockchainのインデックス作成という、2つの主要な作業が完全に完了するのを待つ必要があります。接続状況やマシンのパワーにもよりますが、数日かかる場合があります。この間、プロセスの進行状況をモニターして、すべてがスムーズに進行していることを確認してください。



同期の状態をモニターするには2つの方法がある：




- 道場メンテナンスツール（DMT）を使用する。これは簡単であるが、IBD中はほとんど詳細を提供しない；
- あなたのマシンのDojoログを直接参照します。



### 7.1.道場メンテナンスツール(DMT)による確認



道場メンテナンスツールは、安全なウェブベースのInterfaceで、プラントの状態を監視し、特定の操作を行うことができます。IBDの進捗状況をモニターする最も簡単でアクセスしやすい方法です。初期同期の段階では、表示される情報が制限されることがあります。例えば、DMTにはフルクラムのインデックス作成の詳細な進捗状況は表示されません。一方、同期が完了すると、DMTには：




- Greenのすべてのライト；
- 各サービス (ノード、インデクサ、Dojo DB) の最後に検証されたブロック。



アクセスするには、自分のDMTのURLを知っていて、[Torブラウザを使って](https://www.torproject.org/download/)接続する必要がある。これを行うには、ターミナルを開き、`/my-dojo`ディレクトリに移動する：



```bash
cd ~/dojo-app/docker/my-dojo
```



次に以下のコマンドを実行する：



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



そうすると、Tor経由でのDojoへの接続に関連するすべての情報にアクセスできるようになります。ここで興味があるのは以下のURLです：



```
Dojo API and Maintenance Tool =
```



どのネットワーク上のどのマシンからでも（リモートからでも）DMTにアクセスするには、Torブラウザを開き、このURLの後に`/admin`を入力します。例えば、URLが `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion` の場合、[Tor Browser](https://www.torproject.org/download/) バーに入力する必要があります：



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **このAddressの秘密は厳守してください。



その後、認証ページにリダイレクトされます。DMTは先ほど生成した `NODE_ADMIN_KEY` パスワードを使ってログインします。



![Image](assets/fr/33.webp)



ログインすると、*Dojo Maintenance Tool*にアクセスできます！IBD中は「*Full node*」メニューの「*最新ブロック*」情報を見ることができ、Bitcoinノードの現在の状態を知ることができます。



![Image](assets/fr/34.webp)



このAddressをTor Browserにブックマークしておくと後で簡単に呼び出せます。



道場が完全に同期されると、DMTホームページのすべてのインジケータにGreenチェック✅が表示されるはずです。



### 7.2.Dojoログによる検証



IBDの進行状況を追跡する2つ目の方法は、マシンのログを直接参照することだ。この方法は、より正確でリアルタイムのモニタリングが可能です。Bitcoin coreがどのようにブロックをダウンロードし、フルクラムがどのようにインデックスを作成しているかを見ることができます。



Dojoをホストしているマシンに接続し、ターミナルを開く。すべてのコマンドは `my-dojo` ディレクトリから実行します。このフォルダに移動します：



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin coreログ



Bitcoin coreのログを表示し、IBDの経過を追跡する：



```bash
./dojo.sh logs bitcoind
```



最初に、ブロックヘッダーの同期前段階が表示される：



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



この数値が100%に達すると、Bitcoin coreはBlockchainの完全ダウンロードを開始する。IBDの進行状況がわかるだろう。現在のブロックの高さを知るには、`height=`で示される値を見る。また、`progress=`というキーをたどって、IBDの進捗率を知ることもできる。



![Image](assets/fr/36.webp)



いつものように、ログを閉じてコマンドプロンプトに戻るには、`Ctrl + C`の組み合わせを使う。



#### フルクラムのログ



Bitcoin coreがヘッダーの事前同期を完了すると、フルクラムはBlockchainのインデックス作成を開始する。そのログを：



```bash
./dojo.sh logs fulcrum
```



最後にインデックスされたブロックの高さは、`height:`の後に表示され、インデックスの進捗率も表示されます。



![Image](assets/fr/37.webp)



### 7.3.フルクラムデータベースの破損



Fulcrumは、特に強力なインデクサですが、そのデリケートなデータベース管理のため、インストールは複雑です。初期同期中に電源が切れたり、マシンが突然シャットダウンした場合、インデクサーのデータベースが破損する可能性があります。例えば、以下のようなログがあれば、これを見ることができる：



```bash
fulcrum | The database has been corrupted etc...
```



**注：** この種のエラーは、近々リリースされるフルクラム2.0で修正されるはずです。



この場合、bitcoind（Bitcoinのノード）には影響はありません。ただし、フルクラムの破損したデータを削除し、同期を最初からやり直すまでは、フルクラムを使用することはできません。これがその仕組みだ：



ストップ道場：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



フルクラムコンテナとボリュームのみを削除する：



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



通常は `my-dojo_data-fulcrum` という名前になりますが、そうでない場合は、前のコマンドで返された名前を使用してください。



その後、Dojoを立ち上げ、Fulcrumをゼロから作り直す：



```bash
./dojo.sh upgrade
```



その後、ログを参照することで、フルクラムが正常に動作していることを確認できます：



```bash
docker logs -f fulcrum
```




## 8.道場メンテナンスツールの使用



Bitcoinノットが最も多いProof of Workでワープヘッドと同期し、Blockchainがフルクラムによって100％インデックスされたら、道場を使い始めることができます。



あなたのDojoは、定期的に新しいバージョンで強化された幅広い機能を提供しています。私の意見では、最も重要な2つは：




- 足軽Walletに接続して、自分のノードでBlockchainのデータを参照したり、取引を放送したりすることができる、
- そしてBlock explorerは、Blockchain Bitcoinの情報にアクセスすることができ、あなたが管理していない外部のインスタンスにデータを公開することはありません。



では、その使い方を見てみよう。


### 8.1.足軽と道場をつなぐ



足軽Walletと道場の接続はとても簡単です。QRコードが表示されるので、足軽アプリで直接読み取ります。



![Image](assets/fr/38.webp)



足軽アプリでは、Walletを作成または復元した後に初めて起動すると、「*道場サーバーの設定*」のページにリダイレクトされます。QRスキャン*」を押し、DMTに表示されているQRコードを読み取ってください。



![Image](assets/fr/39.webp)



そして「*Continue*」ボタンをクリックする。



![Image](assets/fr/40.webp)



これで道場に接続されました。



![Image](assets/fr/41.webp)



### 8.2.Block explorerを使う



Dojoは自動的にBlock explorer、[BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer)をインストールします。これは、あなた自身のBitcoinノードからのデータを直接利用します。エクスプローラーを使えば、Interfaceのウェブを通じて、BlockchainやMempoolの生の情報にアクセスすることができます。そのため、例えば、保留中の取引のステータスをチェックしたり、Addressの残高を見たり、ブロックの構成を簡単に調べたりすることができる。



アクセスするには、ブラウザからTorのAddressを取得するだけです。そのためには、DMTのAddressを取得したときと同じコマンドを実行します：



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Tor経由でDojoのすべての接続情報にアクセスできます。ここで興味があるのは以下のURLです：



```
Block Explorer =
```



すでにDMTに接続している場合は、接続JSONの中の「*ペアリング*」メニューにもこのAddressがあります：



![Image](assets/fr/43.webp)



ネットワーク上のどのマシンからでも（リモートからでも）ブラウザにアクセスするには、[Tor Browser](https://www.torproject.org/download/)を開き、先ほど取得したURLを入力する。



⚠️ **このAddressの秘密は厳守してください。



そうすれば、自分だけのBlock explorerを手に入れることができる。



![Image](assets/fr/44.webp)



*画像クレジット：https://ashigaru.rs/.*



取引を追跡するには、右上の検索バーにtxidを入力するだけ。



![Image](assets/fr/45.webp)



*画像クレジット：https://ashigaru.rs/.*



Addressに関連するムーブメントをチェックするには、検索バーにAddressと入力して同じように進む。



![Image](assets/fr/46.webp)



*画像クレジット：https://ashigaru.rs/.*



また、検索バーにブロックのHashや高さを入力すると、詳細が表示される。



![Image](assets/fr/47.webp)



*画像クレジット：https://ashigaru.rs/.*



## 9.道場のメンテナンス



### 9.1 道場を止める



データベース、特にフルクラムインデクサーを破損する可能性があります。電源を切る必要がある場合は、必ずDojoのクリーンシャットダウンを行い、すべての手続きが完了したら、マシンの電源も切ってください：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 道場を更新する



Dojo は定期的に進化し、バグを修正し、安定性を向上させ、機能を追加するために新しいバージョンがリリースされます。そのため、[アップデートを定期的に確認する](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) ことと、Dojo をアップデートすることが重要です。このプロセスは最初のインストールと似ていますが、設定を維持したまま、特定のファイルを利用可能な最新バージョンに置き換える必要があります。以下は、クリーンで安全なアップデートのための詳細な手順です：



現在のDojoのバージョンを調べるには、：



```bash
./dojo.sh version
```



このステップは任意ですが、OS のアップデートから始めることをお勧めします。これにより、非互換性のリスクが減り、Dojo が使用する依存関係が最新になります：



```bash
sudo apt-get update
sudo apt-get upgrade
```



Dojoディレクトリに移動し、現在のサービスを停止する：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



その後、システムを再起動してクリーンな状態にする：



```bash
sudo reboot
```



Dojoにはデジタル署名されたファイルが付属しています。これらの PGP 署名は、ファイルが開発者から発信されたものであり、 何らかの方法で変更されていないことを保証します。Dojo を最初にインストールしたときと同じように、Dojo を更新するたびに確認することが重要です。まず開発者の公開鍵を Tor 経由でダウンロードし、.NET Framework にインポートします：



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



個人用ディレクトリに戻る：



```bash
cd ~/
```



Tor 経由で GitHub から Dojo の最新版をダウンロードする。この例では、バージョン `1.28.0`です（執筆時点ではまだ存在しません：これは単なる例です）。ファイルとリンクを[インストールしたいバージョンに](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases)置き換えることを忘れないでください：



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



PGPフィンガープリントと署名を含むファイルもダウンロードしてください（もう一度言いますが、コマンドでバージョンを調整することを忘れないでください）：



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



ダウンロードしたフィンガープリント・ファイルが開発者の鍵で署名されていることを確認する：



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



正しい結果が表示されるはずです：



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



鍵が未認証であるという警告が表示されることがあるが、これは重要ではない。一方、署名が無効であったり、別の鍵に対応している場合は、それ以上進まず、リンクを確認しながらやり直す。



次にアーカイブのSHA256フィンガープリントを計算し、公式フィンガープリント・ファイルと比較する：



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



2つの指紋が完全に一致すれば、アーカイブは本物で無傷です。異なる場合は、直ちにファイルを削除し、続行しないでください。



ホームディレクトリにあるアーカイブを解凍する：



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



そして、Dojoディレクトリに内容をコピーし、古い.NETファイルを上書きします：



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



この操作により、`~/dojo-app/docker/my-dojo/conf`にある設定ファイルは保持されますが、他のファイルはすべて更新されたバージョンに置き換えられます。



環境をクリーンに保つには、不要なファイルを削除してください：



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Dojo scripts ディレクトリに戻り、update コマンドを実行します：



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



このコマンドはDockerに新しいファイルでイメージを再構築するよう指示し、すべてのサービスを自動的に再起動する。プロセスの最後に、ログをチェックして、Bitcoin core、Fulcrum、Dojoがすべて正しく動作していることを確認してください：



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



サービスがエラーなく開始し、ログにブロックが処理されていることが表示されていれば、Dojoは最新で動作可能です。