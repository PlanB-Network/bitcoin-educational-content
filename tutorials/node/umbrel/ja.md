---
name: アンブレル
description: Umbrelの発見とインストール - あなたのBitcoinノードとホームサーバー
---

![cover](assets/cover.webp)



## はじめに



### Bitcoinノードとは？



Bitcoinノードは、Bitcoinコアソフトウェアまたは代替クライアントを実行することによってBitcoinネットワークに参加するコンピュータです。その役割は、ネットワークの運用とセキュリティに不可欠です：





- Blockchainの保管**：Blockchain Bitcoin の完全な最新コピーを保持する。
- トランザクションの検証**：プロトコルのルールに従って各トランザクションとブロックを検証する。
- 情報発信**：新しい取引やブロックを他のノードと共有
- 合意形成**：ネットワークのルール適用に貢献する



自分自身のBitcoinノードを運営することは、金融主権への重要なステップであり、いくつかの重要な利点を提供する：





- 守秘義務**：お客様の情報を第三者に開示することなく、お取引を共有します。
- 検閲への抵抗**：Bitcoinの使用は誰にも止められない
- 独立した検証**：お客様のトランザクションを検証するために他人のノードを信頼する必要はありません。
- 合意形成**：Bitcoinネットワークルール適用への貢献
- ネットワークサポート**：ネットワークの分配と分散化に積極的に参加する。



### アンブレルBitcoinノードを運用するためのシンプルなソリューション



Umbrelは、Bitcoinノードのインストールと管理を簡素化するオープンソースのオペレーティングシステムです。また、あなたのコンピュータを個人的なホームサーバに変身させ、Bitcoinノードのホスティングを容易にします：





- 完全なBitcoinノード
- Bitcoin 必須アプリケーション（エレクトラーズ、Mempool.スペース）
- その他の個人向けサービス（クラウドストレージ、ストリーミング、VPNなど）



エレガントで直感的なInterfaceユーザーにより、Umbrelは、お客様のデータを完全にコントロールしながら、セルフホスティングサービスを誰でも利用できるようにします。



## アンブレルの設置オプション



Umbrel社は、ターンキーオプション（Umbrel Home）と無料のオープンソース版（UmbrelOS）の2つの主な利用方法を提供している。



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### アンブレル・ホーム：ターンキー・ソリューション



Umbrel Home は、最適な体験のために特別に設計された、設定済みのホームサーバーです。このオールインワンハードウェアソリューションには以下が含まれます：



**ハードウェアの特徴




- セルフホスト用に最適化された高性能プロセッサー
- 高速SSDストレージをプリインストール
- 静かな冷却システム
- コンパクトでエレガントなデザイン
- 統合USBおよびイーサネット・ポート



**限定特典




- プラグアンドプレイ・インストール: プラグインしてすぐに使用可能
- プレミアム・サポート
- 自動アップデートの保証
- 統合された移行ウィザード
- ハードウェア完全保証
- すべての機能をフルサポート



**料金**：399ユーロ（シーズンにより変動あり）



### UmbrelOS: オープンソース版



UmbrelOS は、Umbrel オペレーティングシステムの無料オープンソース版です。この柔軟なソリューションにより、Umbrel の基本機能の恩恵を受けながら、独自のハードウェアを使用することができます。



**メリット




- 完全無料
- オープンで検証可能なソースコード
- 選択の自由
- 高度なカスタマイズ・オプション



**対応プラットフォーム




- Raspberry Pi 5：手頃な価格の人気ソリューション
- X86システム：標準的なPCまたはサーバー用
- 仮想マシン：テスト用または既存インフラでの使用



**制限事項




- 地域支援のみ
- Umbrel Homeのために予約されたいくつかの高度な機能
- より技術的な初期設定
- 性能は選択したハードウェアに依存する



このバージョンは：




- テクニカル・ユーザー
- すでに対応機器をお持ちの方
- 学びたい人、実験したい人
- プロジェクトへの貢献を希望する開発者



公式インストールリンク：




- [Raspberry Pi 5へのインストール](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [x86 システムへのインストール (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [仮想マシンのインストール](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



このチュートリアルでは、Raspberry Pi 5にUmbrelOSをインストールすることに集中しますが、基本的な原則は他のプラットフォームでも変わりません。



## Raspberry Pi 5へのUmbrel OSのインストール



### 必要なコンポーネント



このインストールには ：





- Raspberry Pi 5 (4 GB または 8 GB RAM)
- Raspberry Piの公式電源Supply（安定性のために重要です!）
- MicroSDカード（最低32GB）
- microSDカードリーダー
- データ保存用の外付けSSD
- イーサネットケーブル
- SSD接続用USBケーブル



### インストール手順



**UmbrelOS**のダウンロード



![Téléchargement UmbrelOS](assets/fr/01.webp)




- 公式サイト](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)をご覧ください。
- 最新バージョンのUmbrelOS for Raspberry Pi 5をダウンロードする



**バレナ・エッチャー



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Balena Etcher](https://www.balena.io/etcher/)をダウンロードしてインストールする。



**microSD**カードの準備



![Insertion carte microSD](assets/fr/03.webp)




- コンピュータのカードリーダーにmicroSDカードを挿入する。



**画像点滅



![Flashage UmbrelOS](assets/fr/04.webp)




- バレナ・エッチャー
- ダウンロードした UmbrelOS イメージを選択します。
- microSDカードを保存先として選択する
- Flash!"をクリックし、プロセスが終了するまで待つ。
- カードを安全に取り出す



**microSDカードのインストール



![Installation microSD](assets/fr/05.webp)




- microSD カードを Raspberry Pi 5 に挿入します。



**ペリフェラル接続



![Connexion périphériques](assets/fr/06.webp)




- 外付けSSDを利用可能なUSBポートに接続します。
- Piとルーターの間にイーサネットケーブルを接続します。



**電源オン



![Démarrage du Pi](assets/fr/07.webp)




- Raspberry Pi公式電源Supplyを接続する。
- システムが起動するまで数分待つ。



**ファーストアクセス



![Accès interface web](assets/fr/08.webp)




- 同じネットワークに接続されているデバイスで、ブラウザーを開く。
- アンブレルのInterfaceウェブサイトにアクセスする：http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



もし`umbrel.local`が動かない場合は、ローカルネットワーク上のRaspberry PiのIP Addressを見つける必要があります。以下の方法があります：




- ルーターのInterfaceを参照してください。
- nmapのようなネットワークスキャナーを使う
- コンピュータのターミナルで`arp -a`コマンドを使う。



## アンブレルの第一歩



Umbrel が起動し、ブラウザからアクセスできるようになったら、以下の手順に従ってください：



### 初期設定



**アカウントを作成する



![Création compte](assets/fr/10.webp)




- ユーザー名の選択
- 安全なパスワードの設定
- Umbrel にアクセスするには、以下の認証情報が必要です。



**アカウント確認



![Confirmation compte](assets/fr/11.webp)




- ダッシュボードにアクセスするには「次へ」をクリックします。



**Interface**の発見



![Interface Umbrel](assets/fr/12.webp)




- Umbrel App Storeにアクセスする
- 多くのアプリケーションをご覧ください
- Bitcoinに必要なアプリケーションのインストールから始めよう。



### Bitcoinアプリケーションのインストール



**Bitcoinノード



![Bitcoin Node](assets/fr/13.webp)




- 最初にインストールするアプリケーション
- Blockchain Bitcoin全体をダウンロードして確認する



**選挙人



![Installation Electrs](assets/fr/14.webp)




- Bitcoinウォレット接続用Electrumサーバー
- Bitcoinノードとの同期



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Blockchain用Interfaceディスプレイ
- 取引とブロックをリアルタイムで追跡



## Mempool.spaceで取引を追跡する



Mempool.spaceはオープンソースのBlockchainエクスプローラーで、Bitcoinネットワークをリアルタイムで可視化します。トランザクションを追跡し、トランザクションがネットワーク上でどのように伝播するかを理解することができます。



### Mempoolとコンファメーションを理解する



Mempool」（メモリープール）は、未確認のBitcoinトランザクションがブロックに含まれる前に保管される仮想の待合室のようなものである。トランザクションがどのように処理されるかを説明しよう：



1. **ブロードキャスト**：トランザクションを送信すると、最初にBitcoinネットワークにブロードキャストされます。


2. **Mempoolで待機中：Minerで待機中。


3. **最初の確認未成年者がブロックに含める（1回目の確認）


4. **追加の確認**：あなたのトランザクションを含むブロックの後に採掘された新しいブロックは、それぞれ確認を追加します。



推奨される確認回数は金額によって異なる：




- 少額の場合：1-2回の確認で十分です。
- 多額の場合：6回の確認は一般的に非常に安全であると考えられている



### Mempool.spaceからInterfaceを探る



1. **ホームページ**では、Bitcoinのネットワークの概要をご覧いただけます：




   - 最近採掘されたブロック
   - 優先順位別のコスト見積もり
   - Mempoolの現状



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **取引を検索する特定の取引を追跡するには、その識別子（txid）をページ上部の検索バーに貼り付けます。



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### 取引詳細の分析



あなたの取引が見つかったら、Mempool.spaceは完全な分析を提示します：



1. **必須情報** ：




   - ステータス（確定か否か）
   - 支払った費用（単位：Sats/vB）
   - 確認時間の目安



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **トランザクション構造** ：




   - 入出力の視覚的表現
   - 関係住所の詳細リスト
   - 譲渡金額



3. **技術データ** ：




   - 取引重量
   - 仮想サイズ
   - 使用フォーマットとバージョン
   - その他の特定のメタデータ



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### UmbrelでMempool.spaceを使用する利点



1. **機密性**：リクエストはあなた自身のノードを経由します。


2. **独立性**：サードパーティのサービスに依存する必要なし


3. **信頼性**：公共ブラウザがダウンしてもデータにアクセスできる



このアプリケーションを使用すると、効率的に取引を監視し、手数料が確認速度にどのように影響するかを理解し、Bitcoinネットワークがどのように機能するかをよりよく理解することができます。



## Wallet Bitcoinをノードに接続する



### 電子機器構成



**ローカル接続



![Connexion locale](assets/fr/18.webp)




- ローカルネットワーク用
- 迅速で簡単なセットアップ



**Tor**経由のリモート接続



![Connexion Tor](assets/fr/19.webp)




- どこからでもノードにアクセスするには
- より安全でプライベート



### スパローWalletとの接続



**パラメーターへのアクセス



![Paramètres Sparrow](assets/fr/20.webp)




- オープンスパロー Wallet
- 環境設定 > サーバー
- 既存の接続を変更する」をクリック



**接続タイプの選択



スパローには3つの接続モードがある：



***パブリックサーバー




- 公開サーバーへの接続（blockstream.info、Mempool.spaceなど）
- シンプルだがプライベート性は低い



***Bitcoinコア




- Bitcoinノードへの直接接続
- プライベートだが遅い



***プライベート・エレクトラム




- Electrsサーバーに接続
- 機密性とパフォーマンスを両立



**選挙人**の構成



Electrsアプリケーションに表示される情報を使って接続タイプを選択します：



どちらの場合も、"Use SSL "と "Use proxy "オプションのチェックは外したままにしておく。



**ローカル接続


ホスト： umbrel.local


ポート番号：50001



**リモート接続（Tor）**。


ホスト：[あなたのAddress-鬼]。


ポート番号：50001



Tor接続は、ローカルネットワークの外でノードにアクセスしたい場合に必要です。



![Configuration connexion](assets/fr/21.webp)


Sparrow Walletソフトウェアの詳細については、包括的なチュートリアルを用意しています：


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## 結論



これでUmbrelを使用する準備が整いました。データを完全にコントロールしながら、Bitcoin ネットワークに積極的に参加することができます。あなたのホームサーバーの機能を拡張するために、Umbrel App Store で利用可能な他の多くのアプリケーションを自由に探索してください。



## 有用なリソース



### 公式文書




- [アンブレル公式サイト](https://umbrel.com)
- [アンブレルのドキュメント](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoinアプリケーション




- [Bitcoinコア](https://Bitcoin.org/fr/)
- [選挙人](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [すずめ Wallet](https://sparrowwallet.com)



### コミュニティ




- [フォーラムの傘](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [ツイッター傘](https://twitter.com/umbrel)