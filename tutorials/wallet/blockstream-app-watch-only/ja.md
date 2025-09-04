---
name: ブロックストリームアプリ - 時計専用
description: Blockstream AppでWatch-only walletを設定するには？
---

![cover](assets/cover.webp)


## 1.はじめに


### 1.1 チュートリアルの目的





- このチュートリアルでは、**Blockstream App**モバイルアプリケーションの**Watch-Only**機能を設定して使用し、秘密鍵にアクセスせずにBitcoin Walletを監視する方法を説明します。
- インストール、初期設定、拡張公開鍵のインポート、残高とgenerateの受信アドレスを追跡するための使用について説明しています。
- 注：付録の他のチュートリアルでは、Onchain、Liquid、デスクトップバージョンをカバーしています。



### 1.2.対象者





- 初心者Bitcoinポートフォリオ（多くの場合、Hardware Walletと関連している）を直感的なモバイルアプリケーションで監視したいユーザー。
- 中級ユーザー**：TorやSPVなどのプライバシーオプションを使用しながら、読み取り専用のポートフォリオを管理したい方。
- Hardware Walletをお持ちの方端末を接続せずに残高やgenerateアドレスの確認ができます。
- ビジネスとショップ** ：
 - 秘密鍵を公開することなく、会計目的の取引を追跡できます。
 - オンライン決済システムで秘密鍵を入力せずに受け取った取引を検証する。
 - 従業員が秘密鍵にアクセスすることなく、新しい受信アドレスをgenerateできるようにする。
- 団体とクラウドファンディング**：資金へのアクセスを許可することなく、寄付者に透明性のある残高を表示する。



### 1.3.ウォッチ・オンリーの導入



監視専用**Walletは、秘密鍵にアクセスすることなく、Bitcoin Walletの取引や残高を監視することができます。従来のWalletとは異なり、**拡張**公開鍵**（"**xpub**"、その後 "zpub"、"ypub "などを生んだ）などの公開データのみを保存し、Blockchain Bitcoinの受信アドレスの取得や取引履歴の追跡を可能にする。秘密鍵が存在しないため、アプリケーションからの資金の払い出しは不可能であり、セキュリティの強化が保証されている。



![image](assets/fr/10.webp)



**なぜWatch-only walletを使うのか？





- セキュリティ**：Hardware Wallet**で保護されたポートフォリオを、接続デバイスの秘密鍵を公開することなく監視するのに理想的です。
- 便利**です：Hardware Walletを接続することなく、残高確認やgenerateの新しい宛先の確認ができます。
- 機密性**：Tor**や**SPV**などのオプションと互換性があり、サードパーティサーバへの依存を制限できます。
- 使用例**：移動中の資金の追跡、支払いを受けるためのアドレスの生成、秘密鍵を危険にさらすことなくトランザクションを検証する。



![image](assets/fr/01.webp)



### 1.4.拡張公開鍵



拡張公開鍵**（xpub、ypub、zpubなど）は、Bitcoin Walletから派生したデータの一部であり、秘密鍵にアクセスすることなく、 すべての子公開鍵と関連する受信アドレスを生成する。





- 仕組み** ：拡張公開鍵は、seedフレーズから決定論的プロセス（BIP-32）により生成される。子公開鍵の階層ツリーが生成され、各子公開鍵は受信Addressに変換される。監視されるWalletと同じ派生パス（例：`m/44'/0'/0'`）を使用し、Watch-only walletは同じアドレスを生成する。



![image](assets/fr/11.webp)





- 拡張公開鍵タイプ
 - xpub**：レガシーポートフォリオ（"1 "で始まるアドレス、BIP-44）およびTaprootポートフォリオ（"bc1p "で始まるアドレス、BIP-86）に使用される。
 - ypub**：互換性のあるSegWitウォレット（"3 "で始まるアドレス、BIP-49）用に設計されています。
 - zpub**：ネイティブSegWitポートフォリオ（"bc1q "で始まるアドレス、BIP-84）に関連。
 - その他（tpub、upub、vpubなど）***：代替ネットワーク（Testnetなど）や特定の規格に使用される。例えば、tpubはTestnetネットワーク用。





- 区別** ：xpub、ypub、zpubのいずれを選択するかは、Addressのタイプ（レガシー、SegWit、Taproot、またはネストされたSegWit）と、Walletで使用されるBIP標準によって異なります。Blockstream Appとの互換性を確保するために、ソース・ポートフォリオが要求するフォーマットを確認してください。





- セキュリティと機密性** ：拡張公開鍵は、資金を使用することができない（秘密鍵にアクセスできない）ため、セキュリテ ィの面では機密ではない。しかし、すべての公開アドレスと関連する取引履歴が公開されるため、機密性という点では機密性が高い。



**推奨**：拡張公開鍵を機密情報として保護すること。



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5.Hot Wallet リマインダー





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: スマートフォン、コンピュータ、インターネットに接続されたあらゆるデバイスにインストールされるアプリケーションの名称。
- Coldウォレット**としても知られる**ハードウェアウォレット**とは異なり、ソフトウェアウォレットはオフラインでキーを隔離するため、サイバー攻撃に対してより脆弱である。





- 推奨用途** ：
    - 中程度の量のBitcoinの管理、特に日常的な取引に最適。
    - Hardware Walletは不要と思われる初心者や資産の少ないユーザーに適している。





- 制限**：大口資金や長期貯蓄の保管には安全性が低い。この場合はHardware Walletを選択する。




## 2.ブロックストリームアプリのご紹介





- Blockstream App**は、BitcoinのポートフォリオとLiquid Network上の資産を管理するためのモバイル（iOS、Android）およびデスクトップアプリケーションです。2016年に[Blockstream](https://blockstream.com/)に買収され、以前は*Green Address*、その後*Blockstream Green*という名称でした。
- 主な特徴** ：
    - Blockchain Bitcoinでのオンチェーン**取引。
    - Liquid**ネットワークでの取引（Sidechainは高速で機密性の高い取引）。
    - ウォッチ・オンリー**のポートフォリオは、キーにアクセスすることなくファンドを監視するためのものです。
    - プライバシーオプション：**Tor**経由の接続、Electrum経由の**パーソナルノード**への接続、サードパーティノードへの依存を減らすための**SPV**検証。
    - Replace-by-fee(RBF)**の機能により、未確認取引のスピードアップを図る。
- 互換性**：Blockstream Jade**などのハードウェア・ウォレットを統合。
- Interface**：初心者向けの直感的な操作と、上級者向けの高度なオプション。
- 注**：このガイドはオンチェインの使用に焦点を当てています。付録の他のチュートリアルでは、Onchain、Watch-Only、デスクトップ版について説明しています。




## 3.Blockstream アプリのインストールと設定



### 3.1.ダウンロード





- アンドロイド用** ：
    - Google Playストアから[Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)をダウンロードしてください。
    - 別の方法Blockstreamの公式GitHub](https://github.com/Blockstream/green_android)にあるAPKファイルからインストールする。
- iOSの場合** ：
    - App Storeから[Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)をダウンロードしてください。
- 注意**：不正なアプリケーションを避けるため、必ず公式ソースからダウンロードしてください。



### 3.2. 初期設定





- ホーム画面**：最初に開くと、Walletが設定されていない画面が表示されます。作成またはインポートされたポートフォリオは後でここに表示されます。



![image](assets/fr/02.webp)





- 設定のカスタマイズアプリケーション設定 "をクリックし、以下のオプションを調整し、"保存 "をクリックしてアプリケーションを再起動し、ポートフォリオを作成します。



![image](assets/fr/03.webp)



#### 3.2.1.プライバシーの強化（Androidのみ）





- 機能**：スクリーンショットを無効にし、タスクマネージャーでアプリケーションのプレビューを非表示にし、電話がロックされているときにアクセスをロックします。
- なぜですか？不正な物理的アクセスや画面キャプチャ型マルウェアからデータを保護します。



#### 3.2.2.Tor経由の接続





- 機能**：接続を暗号化する匿名ネットワーク、**Tor**を介してネットワークトラフィックをルーティングします。
- なぜですか？あなたのIP Addressを隠し、プライバシーを保護します。あなたのネットワーク（例えば、公共のWi-Fi）が信頼できない場合に最適です。
- デメリット**：暗号化によりアプリケーションの動作が遅くなる可能性があります。
- 推奨**：機密保持を優先する場合はTorを有効にし、接続速度をテストすること。



#### 3.2.3.パーソナル・ノードへの接続





- 機能**：Electrumサーバー**を経由して、**完全なBitcoinノード**にアプリケーションを接続します。
- その理由Blockchainのデータを完全にコントロールし、Blockstreamサーバーへの依存を排除します。
- 前提条件**：設定済みのBitcoinノード。
- 推奨**：最大限の主権を求める上級ユーザー。



#### 3.2.4.SPVの検証





- 機能**：簡易支払い検証（SPV）**を使用し、チェーン全体をダウンロードすることなく、特定のBlockchainデータを直接検証する。
- なぜか？Blockstreamのデフォルト・ノードへの依存を減らしつつ、モバイル・デバイス向けに軽量化を実現。
- 欠点**：情報の一部をサードパーティ製ノードに依存するため、Full nodeよりも安全性が低い。
- 推奨**：パーソナル・ノードは使えないが、Full nodeのセキュリティが最適であれば、SPVをアクティブにする。





## 4.Bitcoin「ウォッチ・オンリー」ポートフォリオの作成



### 4.1.拡張公開鍵の復元



Watch-only walletを設定するには、まず監視対象のWalletの拡張公開鍵（xpub、ypub、zpubなど）を入手する必要があります。この情報は、一般に、お使いのソフトウェアまたはHardware Walletの設定または「Wallet情報」で入手できます。





- ブロックストリームアプリでの例Walletのホーム画面から「設定」→「Wallet詳細」と進み、zpub ：



![image](assets/fr/09.webp)





- 代替案1：次のステップでスキャンするための、拡張公開鍵を含むQRコードをgenerateに送る。
- 代替案2：Walletがあればoutput descriptorを使う。



### 4.2. Walletウォッチ・オンリーのインポート





- 注意**：カメラや監視者のいないプライベートな環境でポートフォリオをセットアップしてください。
- ホーム画面から「新しいポートフォリオを設定する」をクリックし、「開始」をクリックします：



![image](assets/fr/04.webp)





- 次の画面が表示される：



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** ：新しいHot Walletを作成する。付録のチュートリアル「Blockstream App - Onchain」を参照。
- (2) **「バックアップからの復元」**：Mnemonicフレーズ（12語または24語）を使用して既存のポートフォリオをインポートします。注意Cold Wallet からフレーズをインポートしないでください。接続されたデバイス上でフレーズが公開され、セキュリティが無効になります。
- (3) **"Watch-Only "**: このチュートリアルで関心のあるオプションです。





- 次に、"**Single signature**"と "**Bitcoin**"ネットワークを選択します：



![image](assets/fr/12.webp)





- 拡張公開鍵（xpub、ypub、zpubなど）を貼り付けるか、対応するQRコードを読み取るか、output descriptorを入力する。アプリケーションが "xpub "を指定しても、ypub、zpubなどの鍵も認証される。次に「接続」をクリックする：



![image](assets/fr/13.webp)




### 4.3.Walletウォッチ・オンリーの使用



インポートされると、Watch-only wallet は、拡張公開鍵に由来するアドレスの合計残高と取引履歴を表示する。オンチェーン・トランザクションのみが表示される（Liquid トランザクションは無視される）。Liquid Walletを監視するには、前のステップで「Liquid」を選択してインポートを繰り返す。





- 残高と履歴を見る**：ホーム画面から、合計残高とオンチェーン取引履歴を見ることができます：



![image](assets/fr/14.webp)





- generateを受信Address**とする：取引"、"受取 "の順にクリックし、新しいオンチェーンAddressを作成する。QRコードまたはコピーで共有し、資金を受け取る：



![image](assets/fr/15.webp)





- 資金を送る：Transact "をクリックし、次に "Send "をクリックしてください。を入力します：
 - 受取人のAddress。
 - 取引金額。
 - 取引手数料。



ただし、Watch-only walletは秘密鍵を保持していないため、直接送金することはできません。取引に署名するには、QRコードをスキャンしてHardware WalletまたはExchange PSBTを接続する（Coldcard Qなどで利用できるオプション）。



![image](assets/fr/16.webp)





- 注意**：エラーを避けるため、必ず受取Addressと取引明細を確認してください。間違ったAddressに送金された資金は取り戻せません。




## 付録



### A1.その他のBlockstreamアプリのチュートリアル





- Onchainネットワークの使用 ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Liquid Networkの使い方 ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- デスクトップ版：



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2.拡張公開鍵





- 用語集：
 - [拡張公開鍵](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- コース：
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3.ベストプラクティス



ブロックストリームアプリ**を安全かつ効率的に使用するには、以下の推奨事項に従ってください。これらの推奨事項は、**Bitcoin (onchain)**、**Liquid**、**Lightning** ネットワーク上で資金を保護し、取引を最適化し、機密性を保持するのに役立ちます。





- リカバリーフレーズの確保** ：
 - チュートリアルMnemonicフレーズの保存



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 安全な認証を使用する** ：
 - アプリケーションへのアクセスを保護するために、**強力な暗証番号**または**生体認証**（指紋または顔認証）を有効にします。
 - 暗証番号や生体認証データは絶対に共有しないでください。





- プライバシーの保護** ：
 - generateは、Blockchainのトレースを制限するために、オンチェーンまたはLiquidの受信ごとに新しいAddressを作成する。
 - プライバシー強化"、"Tor"、"SPV "機能を有効にする。
 - 最大限の機密性を確保するためには、Walletを公開ノードではなく、Electrumサーバー経由で自分のBitcoinノードに接続してください。





- お客様のニーズに最適なネットワークをお選びください：
 - オンチェーン**：長期保管や大口取引に有利（手数料は金額に対してごくわずか）。
 - Liquid**：機密性を強化した高速、低コストの転送に使用。
 - ライトニング**：少額を即座に低コストで送金できます。





- 発送先住所は必ずご確認ください：
 - 送金する前に、Addressをよく確認してください。間違ったAddressに送金された資金は永遠に失われます。コピー・ペーストかQRコード・スキャンを使用し、決して手でAddressをコピー・修正しないでください。





- コストの最適化** ：
 - オンチェーン取引では、緊急度とネットワークの混雑度に応じて適切な手数料（低速、中速、高速）を選択する。
 - 少量の場合はLiquid、またはライトニングを使用する。





- アプリケーションを最新の状態に保つ




### A4.追加リソース





- ブロックストリーム公式リンク
 - [公式サイト](https://blockstream.com/)**
 - [モバイルアプリケーションのサポート](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : ドキュメントとチャット
 - [GitHub](https://github.com/Blockstream/green_android)**





- ブロック・エクスプローラー
 - オンチェイン **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **ブロックストリーム情報](https://blockstream.info/Liquid)**
 - ライトニング **[1ML (Lightning Network)](https://1ml.com/)**





 - 学習とチュートリアル:** **[Plan ₿ Network](https://planb.network/)** ：
  - 回復フレーズの確保



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [用語集](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** ：
 - [用語集](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
