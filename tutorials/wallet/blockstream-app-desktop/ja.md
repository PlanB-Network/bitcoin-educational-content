---
name: Blockstream App - Desktop
description: パソコンでHardware Wallet with Blockstream Appを使うには？
---
![cover](assets/cover.webp)



## 1.はじめに



### 1.1 チュートリアルの目的





- このチュートリアルでは、**Blockstream App**をコンピュータ上で使用し、Bitcoin **オンチェーン** Walletを**Hardware Wallet**で管理し、メインのBlockchain Bitcoinに記録されたセキュアなトランザクションを可能にする方法を説明します。
- インストール、初期設定、Hardware Walletの接続、オンチェーンビットコインの受信と送信をカバーしています。
- 注：付録の他のチュートリアルでは、Liquid、ウォッチオンリー、モバイルアプリケーションをカバーしています。



### 1.2 対象読者





- 初心者**の方**：安全なデスクトップソフトウェアとHardware Walletでビットコインを管理したいユーザー。
- 中級者：Hardware Walletを使ったオンチェーン取引や、TorやSPVのようなプライバシーオプションの使い方を理解したい人。



### 1.3.ハードウェア・ウォレットの背景





- Hardware Wallet**、**Cold Wallet**：Hotウォレット**（接続されたデバイス上のソフトウェア・ウォレット）とは異なり、オフラインで秘密鍵を保管する物理的なデバイスであり、サイバー攻撃に対する高度なセキュリティを提供する。
- **推奨用途**：
    - 多額の貯蓄や長期的な貯蓄の確保に最適。
    - コネクテッド・デバイスに関連するリスクから資金を守りたい、セキュリティ重視のユーザーに適している。
- **制限事項**：残高、generateアドレス、およびHardware Wallet署名付き取引のブロードキャストを表示するには、Blockstreamアプリなどのソフトウェアが必要です。



## 2.ブロックストリームアプリのご紹介





- **Blockstream App**は、BitcoinのウォレットとLiquid Networkのアセットを管理するためのモバイル（iOS、Android）およびデスクトップアプリケーションです。2016年にBlockstream社に買収され、*GreenAddress*と呼ばれていたが、*Blockstream Green*（2019年）に改名され、現在は*Blockstream app*（2025年）と呼ばれている。
- **主な特徴**：
- Blockchain Bitcoinのオンチェーン**取引**。
- **Liquid**ネットワークでの取引（Sidechainは高速で機密性の高い取引）。
- **ウォッチ・オンリー**のポートフォリオは、キーにアクセスすることなくファンドを監視するためのものです。
    - プライバシーオプション：**Tor**経由の接続、Electrum経由の**パーソナルノード**への接続、サードパーティノードへの依存を減らすための**SPV**検証。
- Replace-by-fee(RBF)の機能により、未確認トランザクションのスピードアップを図る。
- 互換性**：Blockstream Jade**などのハードウェア・ウォレットを統合。
- **Interface**：初心者のための直感的な操作と、上級者のための高度なオプション。
- 注意：このガイドは、デスクトップ版 Hardware Wallet でのオンチェーン使用に焦点を当てています。付録として提供される他のチュートリアルは、モバイルアプリケーションでの使用、onchain、Liquid、およびWatch-Only機能をカバーしています。



## 3.Blockstream App Desktopのインストールと設定



### 3.1.ダウンロード





- 公式サイト](https://blockstream.com/app/)にアクセスし、"_Download Now_"をクリックします。お使いのOS（Windows、macOS、Linux）に対応するバージョンをダウンロードしてください。
- 注意**：不正なソフトウェアを避けるため、必ず公式ソースからダウンロードしてください。



### 3.2. 初期設定





- ホーム画面：最初に開くと、Wallet が設定されていない画面が表示されます。作成またはインポートされたポートフォリオは、後でここに表示されます。



![image](assets/fr/02.webp)





- 設定のカスタマイズ左下の設定アイコンをクリックし、以下のオプションを調整した後、Interfaceを終了して続行します。



![image](assets/fr/03.webp)



#### 3.2.1.一般的なパラメータ





- 設定メニューの「**一般**」をクリックします。
- **機能**：ソフトウェアの言語を変更し、必要に応じて実験的機能を有効にします。



![image](assets/fr/04.webp)



#### 3.2.2.Tor経由の接続





- 設定メニューの「**ネットワーク**」をクリックします。
- 機能：接続を暗号化する匿名ネットワーク、**Tor**を介してネットワークトラフィックをルーティングします。
- なぜですか？あなたのIP Addressを隠し、プライバシーを保護します。ネットワークが信頼できない場合（公共のWi-Fiなど）に最適です。
- **デメリット**：暗号化によりアプリケーションの動作が遅くなる可能性があります。
- 推奨：機密保持を優先する場合は**Tor**を有効にし、接続速度をテストすること。



![image](assets/fr/05.webp)



#### 3.2.3.パーソナル・ノードへの接続





- 設定メニューの「**カスタムサーバーとバリデーション**」をクリックします。
- 機能：アプリケーションを**Electrumサーバー**経由で**完全なBitcoinノード**に接続します。
- なぜか？Blockchainデータを完全にコントロールし、Blockstreamサーバーへの依存を排除します。
- **前提条件**：設定済みのBitcoinノード。
- 推奨：最大限の主権を求める**上級ユーザー**。



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4.SPVの検証





- 設定メニューの「**カスタムサーバーとバリデーション**」をクリックします。
- 機能：ブロックヘッダーをダウンロードし、完全なBlockchainを保存することなく、包含証明（Merkle）によって取引を検証する**簡易支払い検証（SPV）**を使用します。
- なぜか？Blockstreamのデフォルトノードへの依存を減らし、デバイスの軽量化を実現。
- 欠点：一部の情報をサードパーティーのノードに依存するため、**Full node**よりも安全性が低い。
- 推奨：パーソナル・ノードは使えないが、**Full node**でセキュリティを確保したい場合は**SPV**を有効にする。



![image](assets/fr/07.webp)



## 4.Hardware WalletとBlockstreamアプリの接続



### 4.1.予備的考察



#### 4.1.1.Ledgerをご利用のお客様へ





- Blockstream GreenはLedgerデバイス（Nano S、Nano X）上の**Bitcoin Legacy**アプリケーションのみをサポートします。
- デバイスを接続する前に、**Ledger Live**の手順に従ってください：


1.設定 **→** **実験的機能** に進み、**開発者モード** を有効にしてください。


2.**My Ledger** → **App Catalogue**にアクセスし、**Bitcoin Legacy**アプリケーションをインストールしてください。


3.Blockstream Greenを起動する前に、Ledgerで**Bitcoin Legacy**アプリケーションを開き、接続を確立してください。




- 注意：LedgerがPINコードでロック解除されており、接続時にBitcoinレガシー・アプリケーションがアクティブになっていることを確認してください。



#### 4.1.2 Hardware Walletの初期化





- Hardware Wallet（Ledger、Trezor、Blockstream Jade）を（Blockstream Green、または Ledger Live などの他のソフトウェアと）一度も使用したことがない場合は、まず初期化する必要があります。このステップでは、カメラや監視者のいない安全な環境で行います：


1. **seedフレーズ生成／Mnemonicフレーズ**（12語、18語、24語）：紙に丁寧に書いてください。


2. **seed フレーズ検証**：Wallet のインポートを、拡張公開鍵の検証など、指定された語句からテストする。Wallet への送金の前に実施し、seed フレーズを恒久的に確保する。


3. **seedフレーズの保護**：フレーズは物理的な媒体（紙や金属）で安全な場所に保管してください。決してデジタルで保存しないこと（スクリーンショット、クラウド、電子メールは不可）。




- **重要**：seedフレーズは、デバイスが紛失または故障した場合にあなたの資金を回復する唯一の手段です。誰でもアクセスすることができ、あなたのビットコインを盗むことができます。
- **seed文のバックアップとチェックのためのリソース**：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3.このチュートリアルの設定 ：





- Hardware Walletはすでにseedのフレーズとロック用PINコードで初期化されていると仮定する。
- Hardware WalletをBlockstream Appに接続したことがない場合を想定しています。すでにHardware WalletをBlockstreamアプリでご利用いただいている場合は、アプリを起動すると自動的にアカウントが表示されます。



### 4.2.接続開始





- ホーム画面から「**Setup a New Wallet**」をクリックし、利用規約を確認して「**Get Started**」をクリックします：



![image](assets/fr/08.webp)





- **オンHardware Wallet**」を選択する：



![image](assets/fr/09.webp)





- **Blockstream Jade**を使用している場合は、対応するボタンをクリックしてください。それ以外の場合は、"**Connect a different Hardware Device**" を選択してください：



![image](assets/fr/10.webp)





- Hardware WalletをUSB経由でコンピューターに接続し、Blockstreamアプリで選択します：



![image](assets/fr/22.webp)





- ブロックストリームアプリがお客様のポートフォリオ情報をインポートするまでお待ちください：



![image](assets/fr/23.webp)



### 4.3.アカウントの作成





- Hardware Walletを既にBlockstreamアプリでご利用の場合は、インポート後、自動的にInterfaceにアカウントが表示されます。そうでない場合は、"**Create Account**"をクリックしてアカウントを作成してください：



![image](assets/fr/24.webp)





- クラシックなBitcoinポートフォリオを構成するには、"**Standard**"を選択してください：



![image](assets/fr/25.webp)





- アカウントが作成されると、メインのInterfaceポートフォリオにアクセスできます：



![image](assets/fr/26.webp)





## 5.オンチェーンWalletとHardware Walletの併用



### 5.1.ビットコインを受け取る





- ポートフォリオのメイン画面から「**受信**」をクリックする：



![image](assets/fr/27.webp)





- アプリケーションには、**空白の受信Address**が表示されます。受信ごとに新しいAddressを使用することで、機密性が向上します。Addressをコピーするには「**Addressをコピー**」をクリックするか、表示されたQRコードを送信者に読み取ってもらいます：



![image](assets/fr/12.webp)



**オプション** ：




- (1) 矢印をクリックして、ポートフォリオにリンクされた新しいAddressをgenerateする。
- (2) 特定の金額を要求するには、"**More options**"をクリックし、次に "**Request Amount**"をクリックします。QRが更新され、Addressが次のようなBitcoin支払URIに置き換えられます：`Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) 以前のAddressを再利用するには、"**More options**"をクリックし、"**List of addresses**"をクリックします：



![image](assets/fr/14.webp)





- **検証**：共有されたAddressを慎重にチェックし、エラーや攻撃（マルウェアによるクリップボードの変更など）を回避する。
- 取引がネットワーク上でブロードキャストされると、Walletに表示されます。トランザクションを変更不可能とみなすには、1～6回の確認を待ちます。



![image](assets/fr/28.webp)



### 5.2. ビットコインを送る





- ポートフォリオのメイン画面から「**送信**」をクリックします。



![image](assets/fr/29.webp)





- **詳細を入力**：
    - (1) 選択しているアセットが**Bitcoin**（onchain）であることを確認します。
- (2) 受信者の**Address**を貼り付けるか、ウェブカメラでQRコードをスキャンして入力します。
    - (3) 送信する**金額**を（BTC、サトシ、または他の単位で）示してください。




![image](assets/fr/16.webp)





- 取引手数料（オプション）を選択します：
 - お急ぎの場合は、オプション（速い、普通、遅い）からお選びください。
 - 料金をカスタマイズするには、1バイトあたりのサトシ数を手動で調整します。これらはホーム画面に表示される。Mempool.space](https://Mempool.space/)も参照。



![image](assets/fr/17.webp)





- UTXOの手動選択**（オプション）：Coin の手動選択**」をクリックして、トランザクションで使用する特定の UTXO を選択します。



![image](assets/fr/18.webp)





- 事前確認：サマリー画面でAddress、金額、手数料を確認し、"**Confirm transaction**"をクリックする。このHardware Walletは、UTXO（サトシ）が引き落とされるアドレスに関連する秘密鍵を持っています。



![image](assets/fr/19.webp)





- 最終チェックと署名Hardware Wallet**画面上で、すべての取引パラメータが正しいことを確認し、Hardware Wallet**を使って取引に署名してください。Addressのエラーは、資金の取り返しのつかない損失につながる可能性があります。





- ブロードキャスト：署名されると、Blockstreamアプリは自動的にBitcoinネットワーク上で取引をブロードキャストします。



![image](assets/fr/20.webp)





- **フォローアップ**：
 - Walletのホーム画面には、確認されるまで「保留中」と表示されます。
- 取引が確認されていない限り、**Replace-by-fee（RBF）**機能を使用することで、手数料を増額して確認を早めることができる（付録参照）。



![image](assets/fr/21.webp)



## 付録



### A1.その他のBlockstreamチュートリアル





- Liquid Networkの使い方 ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- ウォッチ・オンリー」のポートフォリオをインポートして追跡する：



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- 携帯電話でのブロックストリーム・アプリの使用 (Hot Wallet) ：



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2.Replace-by-fee（RBF）の説明





- 定義：Replace-by-fee(RBF)はBitcoinネットワークの機能であり、送信者は手数料を上げることで**オンチェーン**取引の確認を早めることができる。
- **制限**：
    - RBFは、LiquidまたはLightning取引では利用できない。
    - 最初の取引はRBF対応とマークされなければならないが、これはBlockstream Appが自動的に行う。
- 詳しくは[用語集](https://planb.network/resources/glossary/RBF-replacebyfee)を参照。



### A3.ベストプラクティス





- **リカバリーフレーズの確保**：
    - Hardware WalletのMnemonicのフレーズを物理的な媒体（紙、金属）で安全な場所に保存してください。
    - 決してデジタルで保存しない（クラウド、Eメール、スクリーンショット）。
    - チュートリアル：Mnemonicのフレーズを保存する：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **プライバシーの保護**：





    - generateはオンチェーン受信ごとに新しいAddressを作成する。
- **Tor**または**SPV**を有効にしてトラッキングを制限する。
    - Electrum経由で自分のBitcoinノードに接続し、最大限の主権を得ることができます。
- 発送先住所は必ずご確認ください：





    - サインをする前に、Hardware Walletの画面でAddressを確認してください。
    - 手作業によるミスを避けるため、コピー＆ペーストまたはQRコードを使用する。
- **コストの最適化**：





    - 緊急度やネットワークの混雑度に応じて料金を調整する（[Mempool.space](https://Mempool.space/)参照）。
    - オンチェーンセキュリティを必要としない高速で低コストの取引には、LiquidまたはLightningを使用する。
- **ソフトウェアのアップデート**：





    - ブロックストリームアプリとHardware Walletファームウェアを最新の機能とセキュリティパッチに更新してください。



### A4.追加リソース





- **公式リンク**：
    - [公式サイト](https://blockstream.com/)
    - [ブロックストリーム・アプリのサポート](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): ドキュメントとチャット
    - [GitHub](https://github.com/Blockstream/green_qt)





- **ブロック・エクスプローラーズ**：
    - オンチェーン : [Mempool.space](https://Mempool.space/)
    - Liquid : 【ブロックストリーム情報】(https://blockstream.info/Liquid)
    - ライトニング : [1ML (Lightning Network)](https://1ml.com/)





- リカバリーフレーズの確保



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network**：



[用語集](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**：



[用語集](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb