---
name: Umbrel LND
description: Lightning Network Daemon(LND)のUmbrelへのインストールと設定に関する上級チュートリアル
---
![cover](assets/cover.webp)




## はじめに



この上級チュートリアルでは、Umbrel ノードへの Lightning Node (LND) アプリケーションのインストール、設定、使用方法について順を追って説明します。チャネルの開設、流動性の管理、ノードをモバイルアプリケーションと同期する方法を学びます。



## 1.前提条件：機能するBitcoinアンブレル・ノード



Lightning をデプロイする前に、Umbrel 上で完全に動作する Bitcoin ノードが必要です。これには、Umbrel をインストールし（Raspberry Pi、NAS、その他のマシン）、Blockchain Bitcoin を完全に同期させる必要があります。



Umbrelをインストールし、Bitcoinノードを設定するには、専用のチュートリアルに従うことをお勧めします：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Lightning Networkはoff-chainのすべてのトランザクションをBitcoinに依存しているため、Bitcoinノードが最新で正しく動作していることを確認してください。



## 2.Lightning Networkの紹介



Lightning Networkは、BitcoinのトランザクションをメインのBlockchainの外で実行することにより、高速化とコスト削減を図るために設計されたセカンドLayerのプロトコルである。



具体的には、2人のユーザーがOn-Chain BTCをブロックすることでチャネルを開設し（最初の取引）、そのチャネル内で即座にExchangeの支払いを行うことができる。このoff-chainの取引はBlockchainに記録されないため、スピードが速く、コストは実質ゼロである。



支払いは（仲介ノードのおかげで）複数のチャネルを経由してネットワーク上のどの受取人にも到達することができ、ほぼ無制限の規模の即時取引が可能です。このようにライトニングは、Blockchain Bitcoinの負荷を軽減しながら、日常的な支払いやマイクロトランザクションに理想的な、非常に高速で低コストのトランザクションを提供する。



Lightningノードを動作させるには、ネットワークに常時接続し、他のLightningノードと相互作用する必要がある。さまざまなソフトウェア実装（LND、Core Lightning、Eclairなど）が存在し、これらはすべて互換性がある。Umbrel は公式 Lightning ノードアプリケーションの一部として LND (Lightning Network Daemon) を使用しています。このチュートリアルでは LND に焦点を当てます。



Lightning Networkの完全な理論的入門については、専用コースを受講されることをお勧めします：



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

このコースでは、Lightning Networkの基本的なコンセプトを徹底的に学び、LNDノードの練習に進みます。



## 3.なぜLNDをセルフホストするのか？



Umbrel上で独自のLightningノード（LND）を運用することで、カストディアルやセミカストディアルのソリューションと比較して、資金やチャネルに対する完全な主権を得ることができます。



### ライトニング・ソリューションの比較 ：



**ソリューション・カストディアル（例：SatoshiのWallet）** ：




- お客様のライトニングビットコインは、信頼できる第三者によって管理されます。
- 使いやすく、技術的な複雑さはない
- オペレーターはあなたの資金を保持し、あなたの取引を追跡することができます。
- コントロールと機密性を犠牲にする



**商品以外の消費者ポートフォリオ（例：Phoenix、Breez）** ：




- ユーザーは秘密鍵を保持し、BTCのOwnershipを保持する。
- 完全なノード管理なし - アプリケーションがバックグラウンドでチャンネルを管理
- シンプルさと主権の妥協
- 流動性をサプライヤー・インフラに依存
- 技術的な制限（1台のスマートフォンでは他のスマートフォンへの支払いをルーティングできない）



**セルフホスト型LNDノード（Umbrel）** ：




- 最大限の主権：On-Chainとoff-chainのBTCは、すべてあなたの管理下にあります。
- チャネルの開設や支払いの管理に第三者は一切関与しません。
- 機密性の向上（お客様のチャネルとトランザクションは、お客様と直接の取引相手のみに知らされます。）
- 利用の自由：独自のサービスやウォレットに接続できる
- 他人のために取引を仲介する可能性（マイクロフィー報酬）
- 技術的責任の増加（メンテナンス、流動性管理、バックアップ）



要するに、LNDのセルフホスティングは、最大限のコントロールが可能だが、より技術的なスキルが必要となる。利便性と主権のトレードオフなのだ。



## 4.ステップバイステップのチュートリアル



### 4.1 Umbrel への Lightning Node アプリケーションのインストールと設定



Umbrel ノード（Bitcoin）の同期が完了したら、以下の手順に従ってください：



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Interface Umbrelの "App Store "セクションからLightning Nodeアプリケーションをインストールします。



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND（Lightning Network Daemon）はアプリケーションとしてあなたのUmbrelにデプロイされます。最初に開くと、ライトニングが実験的な技術であることを知らせる警告メッセージが表示されます。



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



新しいノードを作成するか、バックアップ/seedからノードを復元するかを選択できます。初めてインストールする場合は、新規ノードの作成を選択してください。Lightning Nodeアプリはgenerateに24語のMnemonicフレーズ（あなたのseed Lightning）を表示します：必要に応じてLightning資金をリストアするために使用されるため、慎重に（理想的にはオフラインで紙に）書き留めてください。



**注：Umbrel の最近のバージョンでは、Lightning アプリをインストールすると、この 24 ワードの seed が提供されます（Bitcoin Umbrel ノード自体では提供されません）。**



![Interface principale de Lightning Node](assets/fr/04.webp)



初期化後、Lightning Node のメイン Interface にアクセスします。



![Paramètres de l'application](assets/fr/05.webp)



アプリケーションの設定には、重要なオプションがいくつもあります：




   - ノードID（ノード固有の識別子）を参照する。
   - 外部Walletを接続する（Walletを接続する）
   - 秘密の言葉を見る
   - 詳細設定にアクセスする
   - チャンネルの回復
   - チャンネル・バックアップ・ファイルのダウンロード
   - 自動バックアップを有効にする
   - Tor経由のバックアップを設定する（Backup over Tor）



これらのオプションは、Lightningノードのセキュリティと管理に不可欠です。自動バックアップを有効にして、秘密の単語を安全に保管してください。



**有用なリソース**




- [Umbrel Community](https://community.umbrel.com) - Umbrelとそのエコシステムに関する問題や解決策を共有するためのディスカッションフォーラム


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - UmbrelにおけるLightning Nodeアプリの機能の説明。
> - [LND ドキュメント - クイックスタート](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - LND公式ドキュメント

### 4.2 ライトニングチャンネルの開設



LNDが稼働したら、最初のLightningチャンネルを開設できます。接続先の優良ノードを見つけるには



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/)は、チャンネルを開くための信頼できるノードを見つけるためのエクスプローラです。



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



例えば、[ACINQノード](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f)は、優れた可用性と流動性の統計で認知されたノードである。



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



このチュートリアルでは、[Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca)でチャンネルを開設します。接続に必要な情報(pubkey@ip:port)は彼らのAmbossページに記載されています。



チャンネルを開くには



![Bouton d'ouverture de canal](assets/fr/09.webp)



Lightning Nodeのホームページで、"+ OPEN CHANNEL "ボタンをクリックします。



![Configuration du canal](assets/fr/10.webp)



チャンネル・コンフィギュレーション・ページ ：




   - AmbossからコピーしたノードID（フォーマット：pubkey@ip:port）を貼り付ける。
   - チャンネル容量の定義（ACINQのようないくつかのノードでは、例えば400k Satsのような最小値がある）
   - 必要に応じて取引開始手数料を調整する



![Canal en cours d'ouverture](assets/fr/11.webp)



トランザクションが送信されると、そのチャンネルはホームページに「オープニング」と表示されます。On-Chainトランザクションの確認を待ちます。



![Détails du canal](assets/fr/12.webp)



チャンネルをクリックすると詳細が表示されます：




   - 現在の状況
   - 総容量
   - 流動性の内訳（出入金）
   - リモート・ノードの公開鍵
   - その他の技術情報



### Lightning Network+を利用した流動性の獲得



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+はUmbrel App Storeで入手可能で、現金の入手が容易になる。



![Interface principale de LN+](assets/fr/14.webp)



メインのInterfaceには3つの重要なオプションがある：




- 「流動性スワップ：利用可能なスワップ・オファーを探る
- "Open For Me"：対象となるスワップを絞り込む
- 「ドキュメントへ」：ドキュメントにアクセスする



![Message d'erreur LN+](assets/fr/15.webp)



注：まだチャンネルを開いていない場合、"Open For Me "をクリックすると、このエラーメッセージが表示されます。



![Liste des swaps disponibles](assets/fr/16.webp)



流動性スワップ」ページには、ネットワーク上で利用可能なすべてのスワップ・オファーが表示される。



![Swaps éligibles](assets/fr/17.webp)



"Open For Me "は、あなたのノードが必要な条件を満たすスワップのみをフィルタリングします。



![Détails d'un swap](assets/fr/18.webp)



スワップ詳細の例：




- ペンタゴン構成（参加者5名）
- 1チャンネルあたり300kSatsの容量
- 前提条件：総容量1M Satsのオープン・チャンネルが最低10個必要
- 空席あり：4/5



### 4.3 モバイルアプリケーション（Zeus）との同期



Lightningノードをリモート（スマートフォン）で制御するには、Zeus（iOS/Androidで利用可能なオープンソースアプリケーション）を使用します。



**アンブレルを使ったゼウスのコンフィギュレーション :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Umbrel ノードがアクセス可能であることを確認してください（デフォルトでは Tor 経由）。


Interface UmbrelでLightning Nodeアプリを開き、矢印で示した「Connect Wallet」ボタンをクリックします。



![Page de connexion avec QR code](assets/fr/20.webp)



QRコードが表示され、LNDのアクセスデータがlndconnect形式で表示されます。このQRコードは特に情報量が多いので、遠慮なく拡大して読んでください。



![Configuration initiale de Zeus](assets/fr/21.webp)



携帯電話で：




   - オープン・ゼウス
   - ホームページで「詳細設定」をクリックし、独自のLightningノードを接続します。
   - パラメータで "Walletを作成または接続する "を選択する。



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



ゼウスで




   - 接続タイプとして「LND（REST）」を選択する。
   - QRコードをスキャンするか（推奨方法）、情報を手入力することができます。(アンブレルのQRコードは非常に高密度なので、拡大することをためらわないでください。）
   - 重要: UmbrelがTor経由でのみアクセス可能な場合、"Use Tor "オプションを有効にしてください（デフォルト）。
   - 設定の保存



ZeusはUmbrelノードに接続され、Lightningの支払い、チャンネル、残高などの確認ができるようになりました。



**高度な接続オプション:**。



デフォルトでは、Zeus ↔ Umbrel 接続は Tor 経由です。より高速な接続には、2つの選択肢があります：



**ライトニング・ノード・コネクト（LNC）** ：




   - ライトニング・ラボの暗号化接続メカニズム
   - UmbrelにLightningターミナルアプリをインストールする（LNCアクセスも含む）
   - generate ライトニングターミナルの接続 QR コード (Connect → LNC 経由で Zeus を接続)
   - Zeusにスキャンします（接続タイプとして「LNC」を選択します）。



**VPNテールスケール**：




   - 設定が簡単なメッシュVPN
   - Umbrel（Appストア）と携帯電話にTailscaleをインストールする。
   - Tor Addressの代わりにTailscaleプライベートIP経由でZeusに接続する



これらのオプションは必須ではなく、Tor + Zeusソリューションはほとんどの場合うまく機能する。



> **有用なリソース**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - ゼウスとアンブレルの公式接続ガイド
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - ゼウス・オープンソース・プロジェクト
> - [Umbrel Community - Tailscaleを使ったZeusの接続](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Tailscaleを使ったZeusとUmbrelの接続ガイド

## 5.安全性とベストプラクティス



セルフホスト型のLightningノードを管理するには、セキュリティに特に注意を払う必要がある。



### ノードのバックアップとセキュリティ



**重要なバックアップの種類**



Lightning Umbrel ノードには 2 種類のバックアップが必要です：



**seedの文章（24語）**。




- On-Chainの資金を回収
- Walletライトニングを再現するために必要なもの
- 超セキュアなストレージ（オフライン、紙媒体）用



**スタティック・チャンネル・バックアップ（SCB）**ファイル




- ライトニング・チャンネル情報を含む
- クラッシュ時にチャンネルを強制閉鎖できるようにする。
- **重要:** `channel.db` ファイルは決して手動で保存しないでください (罰則の危険性があります)。



**手動バックアップ手順**



チャンネルを手動で保存するには ：


1.Lightning Nodeメニューにアクセス（"+ Open Channel "の隣にある3つの点"↪Sm_22EE"）


2.チャンネル・バックアップ・ファイルのダウンロード


3.各チャンネルの変更後に新しいSCBをエクスポートする


4.SCBを安全に保管する（暗号化メディア、オフサイトコピー）



**自動バックアップシステム**



Umbrelは、洗練された自動バックアップ・システムを備えています：



**データ保護**




- 送信前のクライアント側の暗号化
- Torネットワーク経由の送信
- ランダム充填によるデータ補足
- デバイス固有の暗号化キー



**セキュリティー強化**




- ステータス変更時の即時バックアップ
- ランダムな間隔で「おとり」バックアップ
- バックアップサイズの変更を隠す
- 時間分析からの保護



**修復プロセス**




- seedアンブレルの識別子とキー
- Mnemonicフレーズのみで完全修復可能
- 最新バックアップの自動復元
- チャンネル設定とデータをリストア



### クラッシュの修復



ノードが失われた場合（ハードウェアの故障、SDカードの破損）：




- アンブレルの再装着
- Lightningアプリで24ワードのseedを入力してください。
- リストア時にSCBファイルをインポート



LNDは、あなたの旧チャンネルの各パートナーに連絡を取り、そのチャンネルを閉鎖し、On-Chainの資金を回収します。チャンネルは永久に閉鎖されます（必要に応じて再開されます）。



### 可用性と詐欺防止



できるだけ頻繁にオンラインに結び目を残しておくのが理想的です。長期不在の場合




- 悪意のあるピアが古いチャンネル状態をブロードキャストしようとする可能性がある。
- ライトニングは「抗議期間」を設けている（LNDでは約2週間）
- 長期不在の場合は、Watchtowerを設定する。



**Watchtowerの構成**




- LNDの詳細設定で、信頼できるWatchtowerサーバーのURLを追加する。
- 公共サービスを利用するか、自分でWatchtowerをインストールする。




ウォッチタワーの設定と使用方法については、専用のチュートリアルをご覧になることをお勧めします：



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### その他のベストプラクティス





- **ソフトウェア・アップデート:** UmbrelとLNDを最新の状態に保つ（セキュリティ修正）
- **ハードウェアの保護:** 安定したシステム（SSD搭載のRaspberry Pi、ミニPC）とUPSを使用する。
- **ネットワーク・セキュリティ:** デフォルトのTorコンフィギュレーションを維持し、Umbrelの管理者パスワードを変更する（デフォルト："moneyprintergobrrr"）。
- 暗号化：**可能であれば、ディスク暗号化を有効にする。**



## 6.追加ツール



UmbrelのLightning Nodeアプリはチャンネル管理に必要不可欠な機能を提供しますが、サードパーティのツールは高度な機能を提供します。



### サンダーハブ



Interface Umbrel App Store経由でインストール可能な、最新のWebベースのLightningノード管理システム。



**特徴：**。




- チャンネルのリアルタイム可視化（容量、残高）
- 統合リバランスツール
- マルチパス課金（MPP）のサポート
- QRコード生成 LNURL
- トランザクション管理 On-Chain



ThunderHubは、アクティブなルーティングノードを監視し、簡単なリバランシングを実行するのに理想的です。



### ライド・ザ・ライトニング（RTL）



Interfaceは、いくつかのLightning実装（LND、Core Lightning、Eclair）と互換性があります。



**ハイライト:**




- マルチノード管理
- 状況に応じたダッシュボード
- サブマリン・スワップのサポート（ライトニング・ループ）
- 2ファクタ認証
- チャンネル・バックアップのエクスポート/インポート



RTLは、Lightningノードを管理するための完全な "スイスアーミーナイフ "であり、より専門家志向のアプローチである。



### その他の便利なツール





- **ライトニング・シェル** ：ブラウザ経由のコマンドライン (lncli)
- **BTC RPC エクスプローラー & Mempool**：モニタリング Blockchain
- **LNmetrics & Torq**：ルーティング性能分析
- **Amboss & 1ML**：ノードの「ソーシャル」管理（エイリアス、コンタクト、ネットワーク分析）



これらのツールは、複雑な設定なしに、Umbrel App Storeから数回クリックするだけでインストールできます。



**追加ツールリソース：**。




- [ThunderHub.io - 機能](https://thunderhub.io) - ThunderHubの機能概要
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTLドキュメンテーション
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - リバランスの実践ガイド
- [ガイド「Lightningノードの管理」](https://github.com/openoms/lightning-node-management) - パワーユーザー向けの高度なドキュメント



## 結論



Umbrel上で独自のLNDノードを運営することは、金融主権への重要な一歩です。カストディアル・ソリューションよりも技術的な関与が必要ですが、管理、機密性、Lightning Networkへの積極的な参加という点で、そのメリットは相当なものです。



このガイドに従うことで、LNDのインストール、チャンネルの開設、流動性の管理、ノードへのリモートアクセスができるようになります。エコシステムに慣れてきたら、徐々に高度な機能や追加ツールを試してみてください。



あなたの資金の安全性は、あなたの安全策と慣行にかかっていることを忘れないでください。大金を投じる前に、時間をかけてあらゆる面を理解すること。