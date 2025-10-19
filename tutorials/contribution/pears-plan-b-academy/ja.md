---
name: 地図 ₿ アカデミー - 梨アプリ
description: Pears に Plan ₿ Academy アプリケーションをインストールして使用するにはどうすればいいですか？
---

![cover](assets/cover.webp)



ご存知のように、プラン₿アカデミーはBitcoinに特化した最大の教育データベースであり、コース、チュートリアル、オープンライセンスの下で公開された何千ものリソースが集められています。もともとPlan ȏ Academyはウェブサイトでした。しかし、もし検閲などで普通にアクセスできなくなったらどうなるでしょうか？



このチュートリアルでは、**Holepunch**によって開発され、**Tether**によってサポートされているピアツーピア(P2P)技術である**Pears**のおかげで、**Plan ₿ Academy**プラットフォームを真に計測不能な方法で実行する方法を学びます。



Pears は、Plan ₿ Academy のプラットフォームを、一元化された Web サイトに依存することなく実行できるようにするソフトウェアです。このチュートリアルでは、Pears をコンピューターにインストールし、Pears 経由で Plan ȏ Academy にアクセスできるようにします。



Pearsの目的はシンプルで、中央集権的なインフラ（サーバー、ホスト、仲介者）に依存することなく、ウェブアプリケーションの配布と利用を可能にすることだ。言い換えれば、クラウドプロバイダーが閉鎖したり、国がドメインをブロックしたりしても、アプリケーションはネットワークの仲間の中で生き続けるのです。このアプローチにより、私たちの教育プラットフォームであるPlan ₿ Academyは、単一障害点なしに、世界中どこからでもアクセスし続けることができるのです。



---

**TL;DR :**。





- 梨をインストールする；





- 以下のコマンドを実行して、Plan ₿ Academy アプリケーションを起動します：



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1.梨を設置する



### 1.1 梨とは？



Pears はピアツーピアアプリケーションのための実行環境、開発ツール、デプロイメントプラットフォームです。このオープンソースツールは、サーバーやインフラを介さずに、ユーザー間で直接ソフトウェアを構築、共有、実行することを可能にします。具体的には、中央サーバーでアプリケーションをホスティングする代わりに、各ユーザーがネットワークノードとなり、アプリケーションの一部やデータを他のピアと共有する。システム全体が分散ネットワークを形成し、各インスタンスが協力してサービスを利用し続ける。



![Image](assets/fr/01.webp)



このアプローチは、Holepunchが開発した一連のモジュラー・ソフトウェア・ブリックに基づいている：




- ハイパーコア**：中央データベースなしでデータの一貫性とセキュリティを保証する分散ログ。
- Hyperbee**：効率的なデータ整理とブラウジングのためのHypercore上のインデクサー。
- Hyperdrive**：ピア間のアプリケーションファイルの保存と同期に使用される分散ファイルシステム。
- Hyperswarm**と**HyperDHT**：中央サーバーなしで、世界中のピア間の発見と接続を可能にするネットワークレイヤー。
- Secretstream**：2つのピア間の交換を保護するためのE2E暗号化プロトコル。



これらのコンポーネントを組み合わせることで、Pearsは、各ユーザーが積極的にネットワークに参加する、自律的で暗号化された分散型アプリケーションを作成することを可能にします。この分散型アーキテクチャにより、インフラコスト、検閲リスク、SPOF（*Single Point of Failure*）を排除することができます。



Pearsは、Mathias BuusとPaolo Ardoino（Tether CEOとBitfinex CTO）によって設立されたHolepunch社によって開発されており、Bitcoinを超えてピアツーピアのロジックを拡張することを使命としている。彼らの野望は「ピアツーピア・インターネット」を構築することであり、そこではあらゆるアプリケーションが、認証なし、サーバーなし、仲介者なしで実行できる。Holepunchはすでに、完全にP2Pのビデオ会議とメッセージング・アプリケーションである**Keet**を開発している。



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*この Pears インストールチュートリアルは、お使いのオペレーティングシステムによっていくつかのセクションに分かれています。あなたの環境に対応するセクションに移動し、適切な指示に従ってください。




- Linux (Debian)** → パート **1.2.**.
- ウィンドウズ** → パート **1.3.**.
- macOS** → パート **1.4.**.




### 1.2 - Linux (Debian) に Pears をインストールするには？



Debian システムへの Pears のインストールは比較的簡単ですが、いくつかの前提条件が必要です。



#### 1.2.1.システムの更新



何よりもまず、システムが最新であることを確認することが重要だ。



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 依存関係のインストール



Pears は、Bare JavaScript ランタイムで使用される `libatomic1` を含む多くのシステムライブラリに依存しています。以下のコマンドでインストールしてください：



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 NVM経由でのNode.jsとnpmのインストール



Pears は *Node.js* のパッケージマネージャである *npm* から配布されています。Pears は直接 *Node.js* に依存して動作するわけではありませんが、 インストールの際には必要です。Linux 上で *Node.js* をインストールする場合、推奨される方法は *NVM* (*Node Version Manager*) です。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



その後、ターミナルをリロードして*NVM*を有効にする：



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



NVM* がインストールされていることを確認する：



```bash
nvm --version
```



![Image](assets/fr/06.webp)



その後、*Node.js*の安定版（現在のLTSなど）をインストールする：



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Node.js*と*npm*のインストールを確認してください：



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 npm による Pears のインストール



npm* が利用できるようになれば、Pears CLI をグローバルにインストールすることができます。これにより、どのディレクトリからでも `pear` コマンドを実行できるようになります。



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5.梨の初期化



インストールが終わったら、ターミナルで以下のコマンドを実行するだけだ：



```bash
pear
```



初回起動時に、Pears はピアツーピアネットワークに接続し、必要なコンポーネントをダウンロードします。このプロセスは中央のサーバーを必要とせず、他のピアから直接ファイルを取得します。



![Image](assets/fr/10.webp)



ダウンロードが完了したら、もう一度コマンドを実行し、すべてが機能していることを確認する：



```bash
pear
```



![Image](assets/fr/11.webp)



すべてが正しくインストールされていれば、Pears Help が表示され、使用可能なコマンドのリストが表示されます。



#### 1.2.6.キートによる洋ナシのテスト



Pearsが完全に動作していることを確認するには、ネットワーク上ですでに利用可能なP2Pアプリケーション、例えばHolepunchのオープンソースメッセージングおよびビデオ会議ソフトウェアであるKeetを起動することができます。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



![Image](assets/fr/12.webp)



これであなたの Linux システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備ができました。



### 1.3 - Pears を Windows にインストールするには？



Windows へのインストールは Linux と同様に簡単ですが、いくつかの特別なツールが必要です。



*Linux を使っていて、すでに Pears をインストールしている場合は、そのままステップ 2 に進んでください。



#### 1.3.1.PowerShellを管理者モードで開く



まず、PowerShell を管理者権限で実行します：




- スタートメニューをクリックする；
- PowerShell と入力する；
- Windows PowerShell*"を右クリックする；
- 管理者として実行*」を選択する。



![Image](assets/fr/15.webp)



#### 1.3.2.NVSをダウンロード



Pears は *Node.js* のパッケージマネージャである *npm* を使ってインストールします。Windows の場合、Holepunch が推奨する方法は *NVS* (*Node Version Switcher*) を使う方法で、このシステムでは *NVM* よりも安定しています。



PowerShellで以下のコマンドを実行し、最新バージョンの*NVS*をインストールする：



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3.Node.jsのインストール



インストール後、PowerShellを再起動し、以下のコマンドを入力する：



```powershell
nvs
```



利用可能な *Node.js* バージョンのリストが表示されるはずです。キーボードの `a` キーを押して最初のものを選択してください。



![Image](assets/fr/17.webp)



*Node.js*がインストールされている。



![Image](assets/fr/18.webp)



#### 1.3.4.インストールの確認



Node.js*と*npm*にアクセスできることを確認する：



```powershell
node -v
npm -v
```



どちらのコマンドもバージョン番号を返さなければならない。



![Image](assets/fr/19.webp)



#### 1.3.5.npm による Pears のインストール



Node.js* と *npm* が利用可能になったら、 **Pears CLI** をシステムにグローバルにインストールします：



```powershell
npm install -g pear
```



これにより、グローバルな *npm* ディレクトリに `pear` バイナリがインストールされます。



![Image](assets/fr/20.webp)



#### 1.3.6.梨のチェックと初期化



インストールが完了したら、：



```powershell
pear
```



初回起動時に、Pears はピアツーピアネットワークから必要なコンポーネントを自動的にダウンロードします。このプロセスには少し時間がかかります。



![Image](assets/fr/21.webp)



すべてがうまくいっていれば、CLI Pears のヘルプ画面が表示され、使用可能なサブコマンド（run、seed、info...）のリストが表示されます。



#### 1.3.7.キートで洋ナシをテストする



Pearsが完全に動作していることを確認するには、ネットワーク上ですでに利用可能なP2Pアプリケーション、例えばHolepunchのオープンソースメッセージングおよびビデオ会議ソフトウェアであるKeetを起動することができます。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



![Image](assets/fr/22.webp)



これであなたの Windows システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備が整いました。



### 1.4.PearsをmacOSにインストールするには？



macOS への Pears のインストールは Linux へのインストールと似ていますが、Apple 環境特有の調整がいくつか必要です。その手順を一緒に見ていきましょう。



*Linux または Windows を使用していて、すでに Pears をインストールしている場合は、そのままステップ 2 に進んでください。



#### 1.4.1.システム要件の確認



インストールする前に、*Xcode Command Line Tools* がシステムに存在することを確認してください。本パッケージは_Node.js_とその依存関係に必要なコンパイルツールを提供します。



これを行うには、キーボードショートカット `Cmd + Space bar` でターミナルを開き、`Terminal` と入力して `Enter` キーを押します。ターミナルでこのコマンドを入力すると、インストールが開始されます：



```bash
xcode-select --install
```



ツールがすでにシステムにインストールされている場合は、macOSが知らせてくれる。



#### 1.4.2.NVMのインストール



Pears は *Node.js* のパッケージマネージャである *npm* から配布されています。Pears は *Node.js* に直接依存して動作するわけではありませんが、 インストールの際には必要です。macOS で *Node.js* をインストールする場合、*NVM* (*Node Version Manager*) を使うことを推奨します。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



その後、端末をリロードして*NVM*を有効にする：



```bash
source ~/.zshrc
```



zsh*ではなく*bash*を使う場合は、：



```bash
source ~/.bashrc
```



次に、*NVM*がインストールされていることを確認する：



```bash
nvm --version
```



ターミナルは、システムにインストールされている*NVM*のバージョンを返すはずです。



#### 1.4.3 Node.jsとnpmのインストール



その後、*Node.js*の安定版（現在のLTSなど）をインストールする：



```bash
nvm install --lts
```



インストールが完了したら、インストールされているバージョンを確認する：



```bash
node -v
npm -v
```



どちらのコマンドもバージョン番号を返さなければならない。



#### 1.4.4 npm による Pears のインストール



npm* が利用できるようになれば、Pears CLI をシステムにグローバルにインストールすることができます。これにより、どのディレクトリからでも `pear` コマンドを実行できるようになります。



```bash
npm install -g pear
```



#### 1.4.5.梨の初期化



インストールが終わったら、ターミナルで以下のコマンドを実行するだけだ：



```bash
pear
```



初回起動時に、Pears はピアツーピアネットワークに接続し、必要なコンポーネントをダウンロードします。このプロセスは中央のサーバーを必要とせず、他のピアから直接ファイルを取得します。



ダウンロードが完了したら、もう一度コマンドを実行し、すべてが機能していることを確認する：



```bash
pear
```



すべてが正しくインストールされていれば、Pears Help が表示され、使用可能なコマンドのリストが表示されます。



#### 1.4.6.キートによる洋ナシのテスト



Pears が完全に動作していることを確認するには、すでにネットワーク上で利用可能な P2P アプリケーション、たとえば Holepunch のオープンソースのメッセージングおよびビデオ会議ソフトウェアである Keet を起動します。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



これであなたの macOS システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備が整いました。



## 2.梨にプラン₿アカデミーを使うには？



Pears がインストールされ実行されると、P2P ネットワーク経由で **Plan ₿ Academy** プラットフォームを直接実行することができます。ターミナルで以下のコマンドを実行するだけです（Linux、Windows、macOSで同じコマンドです）：



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



アップロードされると、Plan ₿ AcademyはPears環境で開き、オリジナルのウェブサイトと同じように使用できますが、中央サーバーに依存する必要はありません。



![Image](assets/fr/14.webp)