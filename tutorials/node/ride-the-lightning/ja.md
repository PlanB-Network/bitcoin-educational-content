---
name: Ride The Lightning (RTL)
description: Ride The Lightning (RTL)を使用してLightningノードを管理します。
---
![cover](assets/cover.webp)


## 1.はじめに



**Ride The Lightning (RTL)**は、Lightning Networkノードを管理するための完全なInterfaceウェブアプリケーションです。このセルフホスト・ウェブアプリケーションは、ブラウザからアクセス可能なLightning**コックピット**を提供します。RTLはすべての主要なLightning実装（LND、Core Lightning/CLN、Eclair）で動作し、ノードとチャンネルを完全にコントロールできます。オープンソース（MITライセンス）で無償のRTLは、多くのターンキーノードソリューション（RaspiBlitz、MyNode、Umbrelなど）にデフォルトで統合されています。



**グラフィカルなInterfaceがなければ、LightningノードはユーザーフレンドリーなCLIコマンドによってのみ管理できます。RTLは、人間工学に基づいたInterfaceにより、これらの操作を簡素化します。主なアプリケーションは以下の通りです：**





- **チャンネルとノードの表示** - ダッシュボードには、On-Chainの残高、Lightningの流動性（ローカル/リモート）、同期ステータス、ノードのエイリアスなどが表示されます。チャンネルリスト、キャパシティ、ローカル/リモート分配、ステータスを確認できます。RTLは、様々な角度からアクティビティを分析するために、コンテキストに応じたダッシュボードを提供します。





- **ライトニング・チャンネル管理** - 数回のクリックでチャンネルをオープン/クローズ。RTLでは、コマンドなしでピアに接続し、チャネルを開くことができます。ルーティング手数料の調整、残高スコアの表示、チャネル間の資金をリバランスするサーキュラーリバランスの開始が可能です。





- **トラッキングと支払い** - RTLはライトニングトランザクションを管理します：インボイスで支払いを送信し、generateでインボイスを受け取り、詳細な履歴でトランザクション（支払い、ルーティング）をトラッキングします。また、Interfaceはルーティングを分析し、どの支払いがあなたのノードを通過しているかを確認します。





- **Wallet On-Chainの管理とバックアップ** - On-Chainタブでは、generateのアドレスとトランザクションの送信ができます。RTLはLND用のSCBファイルをエクスポートすることで、チャンネルを簡単に保存できます。



要するに、RTLはLightning Network**のための**強力なダッシュボードであり、日常的にあなたのノードを操縦するための教育的なInterfaceを提供します。このチュートリアルでは、チャンネルと支払いを管理するためのインストールと使用方法について説明します。



## 2.RTLの技術的運用



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



本題に入る前に、**技術的なレベルで**RTLがLightningノードとどのように相互作用するかを簡単に理解しておくと便利です。



**一般的なアーキテクチャ:** RTLは、Node.js（バックエンド）とAngular（フロントエンド）で構築されたWebアプリケーションです。具体的には、RTLは小さなローカルWebサーバー（デフォルトではポート3000）として動作し、APIを介してLightning実装と対話します。.Node.jaの種類によって、RTLは異なります：





- **LND** では、RTL は LND の REST API (port 8080) を使用して Lightning コマンドを実行します。接続はTLSで保護され、認証にはLNDの **admin macaroon** ファイルが必要です。





- コアライトニング(CLN)では、RTLは*c-lightning-REST*によって提供されるREST APIか、`commando`プラグインを介した**アクセスルーン**を使用する。Umbrelのようなソリューションは、これらのElementsを自動的に設定します。





- **エクレア**では、RTLは設定された認証パスワードを使用してエクレアREST APIに接続します。



**設定とセキュリティ:** RTLはJSONファイル(`RTL-Config.json`)によって設定され、ウェブポート、アクセスパスワード、ノードへの接続情報を定義する。Interfaceのウェブはログイン/パスワード（デフォルトの`password`は変更可能）で保護され、2FAをサポートしている。デフォルトでは、RTLはローカルのHTTP（`http://localhost:3000`）として実行されるが、リモートアクセスの場合は常にセキュアな接続（リバースプロキシ、Tor、VPN経由のHTTPS）を使用すること。



つまり、RTLは、セキュアなAPIを介してノードに接続し、適切なアクセストークンを必要とし、独自のセキュリティLayerを提供する追加コンポーネントです。このモジュラーアーキテクチャにより、単一のRTLインスタンスで複数のLightningノードを管理することも可能です。



## 3.RTLインストレーション



RTLはオープンソースソフトウェアとして配布されているため、システムにインストールするにはいくつかの方法があります。このセクションでは、手動インストールとUmbrel経由のインストールという2つの主なアプローチを取り上げます。



### マニュアル方式



手動インストールは、きめ細かなコントロールを維持したい場合や、カスタム設定にRTLを統合する場合に適しています。以下の手順は、Linux（例えばRaspberry PiやUbuntu/Debianを実行しているVPS）を実行しているLNDノードのためのものですが、CLN/エクレアでも同様です。



**前提条件：** マシンに**同期**したBitcoinノードと動作中のLightningノード（LND、CLNまたはエクレア）があることを確認してください。RTLにはLightningノード自体は含まれておらず、既存のノードに接続します。また、**Node.js**がインストールされている必要があります（バージョン14以上を推奨）。`node -v` で確認するか、公式サイト (https://nodejs.org/en/download/) またはパッケージマネージャからNodeをインストールしてください。



主な設置段階は以下の通り：



**RTLコードをダウンロードする：** RTLの公式GitHubリポジトリをお好きなディレクトリにクローンしてください。例えば



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**依存関係のインストール**：RTLはNode.jsアプリケーションなので、必要なモジュールをインストールする必要があります。RTLフォルダで：



```bash
npm install --omit=dev --legacy-peer-deps
```



このコマンドは必要な NPM パッケージをインストールします (開発依存関係は無視します)。Node の依存関係の衝突を避けるために `--legacy-peer-deps` オプションを指定することを推奨する。



**RTL-Config**：依存関係が整ったら、設定ファイルを準備する。プロジェクトルートにある `Sample-RTL-Config.json` ファイルを `RTL-Config.json` にコピー/リネームする。このファイルを.NET Frameworkで開いてください：





- UIパスワード：安全なパスワードを選択し、`multiPass`に入力する（デフォルトの`"password"`の代わりに）。
- **ポート**: デフォルト `3000`。このポートがすでに使われている場合は変更できる。
- **Node**: `nodes[0]`セクションで、ノードのパラメータを調整する：
     - lnNode`: ノードの説明的な名前 (例 `"LND Node Maison"`).
     - lnImplementation`: `"LND"`（または`"CLN"`/`"ECL"`）。
     - 認証`」の下にある：
       - macaroonPath`: LND の macaroon 管理画面を含むフォルダへのフルパスを指定します。
       - `configPath`: ノードの設定ファイル（LND の場合は `LND.conf`）へのパス。
     - settings`の下にある：
       - fiatConversion`: フィアット通貨に変換したい場合は `true` を設定する。
       - unannouncedChannels`: `true`に設定すると、予告されていないチャンネルが表示される。
       - themeColor`と `themeMode`：Interface のカスタマイズ。
       - channelBackupPath`: LND チャンネルバックアップのパス。
       - lnServerUrl`：LightningノードのURL (例: `https://127.0.0.1:8080`).



**RTLサーバーを起動する：RTLフォルダで.NET Frameworkを実行する**



```bash
node rtl
```



アプリケーションが起動し、`http://localhost:3000`からアクセスできる。



**(オプション) RTLをサービスとして実行する**：自動スタートアップのために、systemd ：



そのためには




- マシンのターミナルを開く。
- 以下のコマンドで新しいサービスファイルを作成する（`nano`はお好みのエディタで置き換えてください）：


```bash
sudo nano /etc/systemd/system/RTL.service
```




- 以下の内容をコピーして、このファイルに貼り付けてください：



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- path/to/RTL/rtl`をあなたのマシン上の`rtl`ファイルへの実際のパスに、`<your_user>`をあなたのLinuxユーザー名に置き換えてください。
- ファイルを保存して閉じる。
- systemdの設定をリロードする：


```bash
sudo systemctl daemon-reload
```




- RTLサービスをアクティブにして起動する：


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTLはマシンがリブートされるたびに自動的に起動するようになった。その状態は：


```bash
sudo systemctl status RTL
```



### アンブレルを使ったインスタレーション



Umbrel](https://getumbrel.com)を使えば、RTLのインストールはもっと簡単になる：





- Interface Umbrelにアクセスする（通常は`http://umbrel.local`経由）。
- **App Store**にアクセス
- "ライド・ザ・ライトニング "で検索



**重要：Umbrel App Storeには2つの別々のRTLアプリケーションがあります。**




- **Ride The Lightning** (LND用): UmbrelのデフォルトのLightningノード(LND)用。
- **Ride The Lightning (Core Lightning)**: Umbrelに*Core Lightning*アプリケーションをインストールし、このノードをRTLで管理したい場合にのみ使用します。



*それぞれのRTLバージョンは、対応する実装（LNDまたはCore Lightning）と対話するようにあらかじめ設定されています。Lightningノードを変更していない場合は、クラシックなLNDバージョンを選択してください。*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- **インストール**をクリック



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**重要：**インストール後、RTLはデフォルトパスワードの画面を表示します。 **このパスワードをコピーして保存してください** - Interface RTLにログオンする際に必要になります。このパスワードは "Don't show it again "オプションをチェックするまで、RTLが起動するたびに表示されます。



Umbrelは自動的に：




- RTLのダウンロードと設定
- Lightning ノードへのアクセス設定
- アップデートの管理
- Interfaceへのアクセス確保



インストールが完了すると、アプリケーションはUmbrelの*アプリケーション*メニューに表示されます。**Ride The Lightning**をクリックして起動してください。



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



ログイン画面で、先ほどコピーしたパスワードを入力します。ログインすると、Interface ウェブ RTL に Umbrel ダッシュボードから直接アクセスできるようになります！



## 4.Interface RTLの紹介と使い方



RTLが稼動した今、そのInterfaceウェブと主な機能を探ってみよう。Interfaceのウェブと主な機能について見ていきましょう。



### メイン・コントロール・パネル



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



ログインするとすぐに**メインダッシュボード**にアクセスし、Lightningノードの概要を確認できます。このページには重要な情報が集約されています：




- ライトニングの合計残高
- On-Chain 残高あり
- 流動性の内訳（出入金）
- Lightningノード経由でSatsを送受信するためのクイックアクセス



### 資金管理 On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



On-Chain**タブでは、メインチェーン上でビットコインを直接管理することができます：

The line appears to be correctly formatted already. The ** markers are balanced and properly placed for bold formatting of "タブ" (tab).




- 異なる単位での残高表示（Sats、BTC、USD）
- 取引一覧
- Address世代 Taproot (P2TR), P2SH (NP2WKH) または Bech32 (P2WKH)
- UTXO管理、ビットコインの送受信



### ライトニング：サブメニューの詳細表示



Interface RTLには、Lightning Network専用のサイドメニューがあり、ノードの管理に必要な機能がまとめられています。各サブメニューの詳細を、スクリーンショットの順番でご紹介します：



#### 1.ピア/チャンネル



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



このサブメニューで ：




- 接続中のピアとライトニングチャンネルが開いているか、待機しているかのリストを表示します。
- 新しいピアを追加する（他のLightningノードに接続する）。
- 既存チャンネルの開設、閉鎖、管理
- 各チャネルの詳細を表示：容量、ローカル/リモート残高、ステータス、取引履歴、残高スコアなど。



#### 2.トランザクション



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



このサブメニューでは、：




- ライトニングの支払いを送る（Invoice経由）。
- generateに請求書を管理し、支払いを受ける。
- 送受信された支払いの履歴を、詳細（金額、日付、ステータス、チャージ、スキップ回数など）付きで完全に表示します。



#### 3.ルーティング



このサブメニューには ：




- あなたのノードが他のLightning Networkユーザーのためにルーティングした支払い。
- ルーティング統計：中継されたトランザクション数、獲得手数料、発生したエラー。
- 高度な分析のためにエクスポート可能な履歴。



#### 4.延期



このサブメニューでは、：




- Lightningノードのアクティビティに関する詳細レポート。
- チャネル、支払い、料金、キャパシティなどに関する図表。
- ノードのパフォーマンスをよりよく理解するためのツール。



#### 5.グラフ検索



このサブメニューで ：




- Lightning Networkのトポロジーを探る。
- 特定のノードまたはチャンネルを検索します。
- 接続性と全体的なネットワーク容量に関する情報を入手する。



#### 6.サイン／ベリファイ



このサブメニューには ：




- 自分のノードの鍵でメッセージに署名する機能（Ownershipの証明）。
- 他のノードからのメッセージを認証するための署名検証。



#### 7.バックアップ



このサブメニューはバックアップ専用です：




- チャンネルバックアップファイル（LND用SCB）をエクスポートします。
- 必要に応じてコンフィギュレーションやチャンネルをリストアする。
- バックアップを保護するためのヒント



#### 8.ノード/ネットワーク



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



このサブメニューには ：




- Lightningノードのステータス（エイリアス、バージョン、カラー、同期ステータス）の完全な概要。
- チャネルの統計（アクティブ、待機中、クローズ）、総容量、接続性。
- グローバルLightning Networkとその中での自分のノードの位置に関する情報。



### サービスボルツ・スワップ



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltzは、Lightning NetworkとBlockchain Bitcoin (On-Chain)の間でビットコインを変換する、プライバシーに配慮した非保護のExchangeサービスです。2種類のオペレーションを提供しています：リバース・サブマリン・スワップ(**スワップ・アウト**)とサブマリン・スワップ(**スワップ・イン**)です。



#### スワップ・アウト（逆サブマリン・スワップ）



Swap OutはLightning Networkで利用可能なSatsをOn-Chainのビットコインに変換します。このメカニズムは、ノードが受信容量を使い果たした場合や、On-Chain Addressから資金を回収したい場合に便利です。プロセスは以下のように動作します：




- 交換する金額を選択します。
- ノードはBoltzにLightningの支払いを送信する。
- Exchangeで、BoltzはOn-Chainのビットコインで同額をブロックする。
- 取引が確認されると、ユーザーはスワップで使用された秘密を明かすことで資金を請求することができる。



このプロセスは非保護であり、ボルツが利用者の資金を預かることはない。


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### スワップ・イン（サブマリン・スワップ）



一方、スワップ・インは、On-Chainの資金をLightning Networkに再投入することができます。これは特にチャンネルの出力容量を回復するのに便利です。手順は以下の通り：




- ユーザーはBoltzが生成した特定のAddressにビットコインを送金する。
- これらの資金は、Boltzがユーザーのノードから発生するLightning Invoiceを支払った場合にのみ解放される。
- Invoiceの支払いが完了すると、ライトニング・チャネルで資金が利用可能になり、ノードの出力能力が向上する。



![Configuration d'un swap-in](assets/fr/12.webp)



これら2つのメカニズムにより、ライトニング・チャネルの流動性を効率的に管理することが可能になると同時に、ユーザーの資金に対する主権を維持することができる。



### 設定とカスタマイズ



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



**Node Config**タブでは、使用感をカスタマイズすることができます：




- 未発表チャンネルの活性化
- セール表示のカスタマイズ
- Block explorerの構成
- Interfaceの調整



### ドキュメントとヘルプ



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



最後に、**ヘルプ**セクションは、.NET Frameworkに関する包括的なドキュメントを提供しています：




- 初期設定
- ピア・チャネル・マネジメント
- 支払いと取引
- バックアップとリストア
- レポートと統計
- 署名と検証
- ノードとアプリケーションのパラメータ



基本的な操作から高度な機能まで、Lightningノードを効率的に管理できる、直感的で整理された総合的なInterfaceです。



## 5.高度なユースケースとセキュリティ



このセクションでは、RTLをさらに進め、Lightningノードを保護するために知っておくべきことを説明します：



### モニタリングとトラブルシューティング



ノードを監視するには、RTLデータ（ログ、CSV）をエクスポートし、Grafanaなどのツールでそれらを表示することができます。問題（ブロックされた支払い、非アクティブチャネル）が発生した場合、LND/CLN ログを参照し、診断コマンド（`lncli listchannels`、`lncli pendingchannels`など）を使用します。RTL はルーティングイベントを監視するための Interface ログも提供している。



### 安全なリモートアクセス



インターネット上でRTLを直接公開しないこと。.NETを優先すること：




- **VPN**（Tailscaleなど）によるプライベートな暗号化アクセス
- **Tor**による安全な匿名アクセス
- リバースプロキシ **HTTPS** (Nginx/Caddy) 設定方法を知っている場合のみ。



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 適切な安全対策





- **アクセス権の保護**: admin.macaroonやRTLパスワードは決して共有しないでください。機密ファイルのパーミッションを制限する。
- **定期的なバックアップ**: チャネルバックアップファイル(SCB)を変更毎にエクスポートし、ノードの外部に保存します。
- **アップデート**: RTL、お使いのノード、Umbrel を最新のセキュリティフィックスに保ちます。
- **守秘義務**: ログやスクリーンショットは、共有する前に匿名化してください。残高やピアリストは決して公開しないでください。
- シングルアクセス：RTLはマルチユーザーではありません。管理者アクセスを共有しないでください。読み取り専用アクセスには、必要に応じて専用のマカロンを使用してください。



これらの原則を適用することで、リスクを大幅に制限し、Lightningノードをコントロールすることができます。



## 7.結論



**Ride The Lightning**は、初心者から上級者まで、Bitcoin/Lightningノードを効果的に管理するために不可欠なツールです。Lightning Networkの理解を深めながら、チャンネル、支払い、ノードの健全性をコントロールするための明確なInterfaceを提供します。



RTLは、その複数実装の互換性、高度な機能（リバランシング、スワップ、レポート）、そして教育的アプローチで際立っています。シンプルなニーズであれば、Interface UmbrelやWallet mobileで十分ですが、アクティブで最適化されたノード管理にはRTLが最適です。



詳しくは：




- RTL公式ウェブサイト：https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork：[r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - 技術的な議論、プロジェクトのアナウンス、フィードバック、教育リソース
- **アンブレルコミュニティフォーラム**：[community.getumbrel.com](https://community.getumbrel.com) - Bitcoin/Lightning専用セクション、ガイド、一般的な問題の解決策を含む公式フォーラム。
- Lightning Network開発者：[github.com/lightning](https://github.com/lightning) - GitHubの公式リポジトリで、開発状況の確認やソースコードの投稿ができます。
- スタック Exchange **Bitcoin** ：[Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - 開発者と上級ユーザーとの技術的なQ&A



つまり、RTLは、最新のフル機能を備えたInterfaceで、ライトニング・ノードを完全にコントロールできるのだ。



**ソース :** RTL公式サイト; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Networkリソース。



Lightning Networkがどのように機能するのか理解を深めるために、この無料コースを受講することもお勧めする：



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb