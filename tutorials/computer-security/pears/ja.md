---
name: Pears
description: ペアーズにアプリケーションをインストールして使用するにはどうすればいいですか？
---

![cover](assets/cover.webp)



このチュートリアルでは、**Holepunch** が開発し、**Tether** がサポートしているピアツーピア (P2P) 技術である **Pears** 上でアプリケーションを実行する方法を学びます。その目的はシンプルで、中央集権的なインフラ（サーバー、ホスト、仲介者）に依存することなく、ウェブアプリケーションを配布し、利用できるようにすることです。言い換えれば、クラウド・プロバイダーが閉鎖したり、国がドメインをブロックしたりしても、アプリケーションはネットワーク・ピアの間で生き続ける。



## 1.梨とは？



Pears はピアツーピアアプリケーションのための実行環境、開発ツール、デプロイメントプラットフォームです。このオープンソースツールは、サーバーやインフラを介さずに、ユーザー間で直接ソフトウェアを構築、共有、実行することを可能にします。具体的には、中央サーバーでアプリケーションをホスティングする代わりに、各ユーザーがネットワークノードとなり、アプリケーションの一部やデータを他のピアと共有する。システム全体が分散ネットワークを形成し、各インスタンスが協力してサービスを利用し続ける。



![Image](assets/fr/01.webp)



このアプローチは、Holepunchが開発した一連のモジュラー・ソフトウェア・ブリックに基づいている：




- ハイパーコア**：中央データベースなしでデータの一貫性とセキュリティを保証する分散ログ。
- Hyperbee**：効率的なデータ整理とブラウジングのためのHypercore上のインデクサー。
- Hyperdrive**：ピア間のアプリケーションファイルの保存と同期に使用される分散ファイルシステム。
- Hyperswarm**と**HyperDHT**：中央サーバーなしで、世界中のピア間の発見と接続を可能にするネットワークレイヤー。
- Secretstream**：2つのピア間の交換を保護するためのE2E暗号化プロトコル。



これらのコンポーネントを組み合わせることで、Pearsは、各ユーザーが積極的にネットワークに参加する、自律的で暗号化された分散型アプリケーションを作成することを可能にします。この分散型アーキテクチャにより、インフラコスト、検閲リスク、SPOF（*Single Point of Failure*）を排除することができます。



## 2.プロジェクトの起源と理念



Pearsは、Mathias BuusとPaolo Ardoino（Tether CEOとBitfinex CTO）によって設立されたHolepunch社によって開発されており、Bitcoinを超えてピアツーピアのロジックを拡張することを使命としている。彼らの野望は「ピアツーピア・インターネット」を構築することであり、そこではあらゆるアプリケーションが、認証なし、サーバーなし、仲介者なしで実行できる。Holepunchは、完全にP2Pのビデオ会議とメッセージング・アプリケーションである**Keet**をすでに開発している。



*この Pears インストールチュートリアルは、お使いのオペレーティングシステムによっていくつかのセクションに分かれています。あなたの環境に対応するセクションに直接移動して、適切な指示に従ってください。




- Linux (Debian)** → パート **3**
- ウィンドウズ** → パート **4**
- macOS** → パート **5**



## 3.Pears を Linux (Debian) にインストールする方法



Debian システムへの Pears のインストールは比較的簡単ですが、いくつかの前提条件があります。



### 3.1. システムを更新する



何よりもまず、システムが最新であることを確認することが重要だ。



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. 依存関係をインストールする



特に `libatomic1` は Bare JavaScript ランタイムで使用されています。以下のコマンドでインストールしてください：



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. NVM経由でNode.jsとnpmをインストールする。



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



### 3.4 npm による Pears のインストール



npm* が利用できるようになれば、Pears CLI をグローバルにインストールすることができます。これにより、どのディレクトリからでも `pear` コマンドを実行できるようになります。



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5.梨の初期化



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



### 3.6.キートで梨をテストする



Pearsが完全に動作していることを確認するには、ネットワーク上ですでに利用可能なP2Pアプリケーション、例えばHolepunchのオープンソースメッセージングおよびビデオ会議ソフトウェアであるKeetを起動することができます。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



![Image](assets/fr/12.webp)



これであなたの Linux システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備ができました。



## 4.WindowsにPearsをインストールする方法



Windows へのインストールは Linux と同様に簡単ですが、いくつかの特別なツールが必要です。



*Linuxを使用している場合は、ステップ6.*に進んでください。



### 4.1. PowerShellを管理者モードで開く。



まず、PowerShell を管理者権限で実行します：




- スタートメニューをクリックする；
- PowerShell と入力する；
- Windows PowerShell*"を右クリックする；
- 管理者として実行*」を選択する。



![Image](assets/fr/15.webp)



### 4.2. NVSをダウンロードする



Pears は *Node.js* のパッケージマネージャである *npm* を使ってインストールします。Windows の場合、Holepunch が推奨する方法は *NVS* (*Node Version Switcher*) を使う方法で、このシステムでは *NVM* よりも安定しています。



PowerShellで以下のコマンドを実行し、最新バージョンの*NVS*をインストールする：



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Node.jsをインストールする。



インストール後、PowerShellを再起動し、以下のコマンドを入力する：



```powershell
nvs
```



利用可能な *Node.js* バージョンのリストが表示されるはずです。キーボードの `a` キーを押して最初のものを選択してください。



![Image](assets/fr/17.webp)



*Node.js*がインストールされている。



![Image](assets/fr/18.webp)



### 4.4.インストールを確認する



Node.js*と*npm*にアクセスできることを確認する：



```powershell
node -v
npm -v
```



どちらのコマンドもバージョン番号を返さなければならない。



![Image](assets/fr/19.webp)



### 4.5.npm による Pears のインストール



Node.js* と *npm* が利用できるようになったら、 **Pears CLI** をシステムにインストールします：



```powershell
npm install -g pear
```



これにより、グローバルな *npm* ディレクトリに `pear` バイナリがインストールされます。



![Image](assets/fr/20.webp)



### 4.6.梨のチェックと初期化



インストールが完了したら、：



```powershell
pear
```



初回起動時に、Pears はピアツーピアネットワークから必要なコンポーネントを自動的にダウンロードします。このプロセスには少し時間がかかります。



![Image](assets/fr/21.webp)



すべてがうまくいっていれば、CLI Pears のヘルプ画面が表示され、使用可能なサブコマンド（run、seed、info...）のリストが表示されます。



### 4.7.キートで梨をテストする



Pearsが完全に動作していることを確認するには、ネットワーク上ですでに利用可能なP2Pアプリケーション、例えばHolepunchのオープンソースメッセージングおよびビデオ会議ソフトウェアであるKeetを起動することができます。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



![Image](assets/fr/22.webp)



これであなたの Windows システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備が整いました。



## 5.PearsをmacOSにインストールするには？



macOS への Pears のインストールは Linux へのインストールと似ていますが、Apple 環境特有の調整がいくつか必要です。その手順を一緒に見ていきましょう。



*Linux または Windows を使用していて、すでに Pears をインストールしている場合は、そのまま **ステップ 6** に進んでください。



### 5.1.システム要件の確認



インストールする前に、*Xcode Command Line Tools* がシステムに存在することを確認してください。本パッケージは_Node.js_とその依存関係に必要なコンパイルツールを提供します。



これを行うには、キーボードショートカット `Cmd + Space bar` でターミナルを開き、`Terminal` と入力して `Enter` キーを押します。ターミナルでこのコマンドを入力すると、インストールが開始されます：



```bash
xcode-select --install
```



ツールがすでにシステムにインストールされている場合は、macOSが知らせてくれる。



### 5.2. NVMをインストールする



Pears は *Node.js* のパッケージマネージャである *npm* から配布されています。Pears は *Node.js* に直接依存して動作するわけではありませんが、 インストールの際には必要です。macOS 上での *Node.js* のインストールには、複数のバージョンの Node を並行して管理できる *NVM* (*Node Version Manager*) を使うことを推奨します。



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



その後、ターミナルをリロードして*NVM*を有効にする：



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



### 5.3. Node.jsとnpmをインストールする。



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



### 5.4 npm による Pears のインストール



npm* が利用できるようになれば、Pears CLI をシステムにグローバルにインストールすることができます。これにより、どのディレクトリからでも `pear` コマンドを実行できるようになります。



```bash
npm install -g pear
```



### 5.5.梨の初期化



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



### 5.6.キートで梨をテストする



Pearsが完全に動作していることを確認するには、ネットワーク上ですでに利用可能なP2Pアプリケーション、例えばHolepunchのオープンソースメッセージングおよびビデオ会議ソフトウェアであるKeetを起動することができます。



```bash
pear run pear://keet
```



このコマンドは Pears ネットワークから直接 Keet アプリケーションを読み込みます。Keet が正しく起動すれば、Pears は完全に動作しています。



これであなたの macOS システムは Pears を使ってピアツーピアアプリケーションを実行し、ホストする準備が整いました。



## 6.梨にアプリケーションを使うには？



Pears が起動したら、以下のコマンドでアプリケーションを直接実行することができます：



```bash
pear run pear://[KEY]
```



KEY]`を使用したいアプリケーションキーに置き換えるだけです。



![Image](assets/fr/13.webp)



Pears上でPlan ₿ Academyプラットフォームを実行する方法については、こちらの包括的なチュートリアルをご覧ください：



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Pearsで起動したKeetメッセージング・アプリケーションの使い方は、こちらのチュートリアルをご覧ください：



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b