---
name: ブロックストリームアプリ - Onchain
description: モバイルでBlockstreamアプリを設定し、オンチェーン取引を管理する
---
![cover](assets/cover.webp)


## 1.はじめに


### 1.1 チュートリアルの目的





- このチュートリアルでは、**Blockstream App** モバイルアプリケーションを使用して、Bitcoin **onchain** Wallet、つまりメインの Blockchain Bitcoin に直接記録されたトランザクションを管理する方法を説明します。
- インストール、初期設定、Software Walletの作成、ビットコインの送受信操作について解説しています。
- 注：付録の他のチュートリアルでは、Liquid、Watch-Only、デスクトップ版をカバーしています。



![image](assets/fr/01.webp)



### 1.2 対象読者





- 初心者**の方：直感的なモバイルアプリケーションでビットコインを管理したいユーザー。
- 中級者**：オンチェーンの機能や、TorやSPVなどのプライバシーオプションを理解しようとしている人。



### 1.3.Hot財布に関する注意事項





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: Bitcoin Walletの秘密鍵を管理し、保護することを可能にする、スマートフォン、コンピュータ、またはインターネットに接続された機器にインストールされるアプリケーションの名称。
- Coldウォレット**としても知られる**ハードウェアウォレット**とは異なり、ソフトウェアウォレットはオフラインでキーを隔離するため、サイバー攻撃に対してより脆弱である。





- 推奨用途** ：
    - 中程度の量のBitcoinの管理、特に日常的な取引に最適。
    - Hardware Walletは不要と思われる初心者や資産の少ないユーザーに適している。





- 制限**：大口資金や長期貯蓄の保管には安全性が低い。この場合はHardware Walletを選択する。




## 2.ブロックストリームアプリのご紹介





- Blockstream App**は、BitcoinのポートフォリオとLiquid Networkの資産を管理するためのモバイル（iOS、Android）およびデスクトップアプリケーションです。2016年に[Blockstream](https://blockstream.com/)に買収され、以前は*Green Address*、その後*Blockstream Green*という名称だった。
- 主な特徴** ：
    - Blockchain Bitcoinのオンチェーン**取引。
    - ネットワークトランザクション**Liquid**（Sidechainは高速で機密性の高いやり取りを行うため）。
    - ウォッチ・オンリー**のポートフォリオは、キーにアクセスすることなくファンドを監視するためのものです。
    - プライバシーオプション：**Tor**経由の接続、Electrum経由の**パーソナルノード**への接続、サードパーティノードへの依存を減らすための**SPV**検証。
    - Replace-by-fee(RBF)**の機能により、未確認トランザクションを高速化。
- 互換性**：Blockstream Jade**などのハードウェア・ウォレットを統合。
- Interface**：初心者向けの直感的な操作と、上級者向けの高度なオプション。
- 注**：本ガイドはオンチェーンでの使用に焦点を当てています。付録の他のチュートリアルでは、Liquid、Watch-Only、デスクトップ版について説明しています。



## 3.Blockstream アプリのインストールと設定



### 3.1.ダウンロード





- アンドロイド用** ：
    - Google Playストアから[Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)をダウンロードしてください。
    - 別の方法Blockstreamの公式GitHub](https://github.com/Blockstream/green_android)にあるAPKファイルからインストールする。
- iOSの場合** ：
    - App Storeから[Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590)をダウンロードしてください。
- 注意**：不正なアプリケーションを避けるため、必ず公式ソースからダウンロードしてください。



### 3.2. 初期設定





- ホーム画面最初に開くと、Wallet が設定されていない画面が表示されます。作成またはインポートされたポートフォリオは後でここに表示されます。



![image](assets/fr/02.webp)





- 設定のカスタマイズアプリケーション設定 "をクリックし、以下のオプションを調整し、"保存 "をクリックしてアプリケーションを再起動し、ポートフォリオを作成します。



![image](assets/fr/03.webp)



#### 3.2.1.プライバシーの強化（Androidのみ）





- 機能**：スクリーンショットを無効にし、タスクマネージャーでアプリケーションのプレビューを非表示にし、電話がロックされているときにアクセスをロックします。
- なぜですか？不正な物理的アクセスや画面キャプチャ型マルウェアからデータを保護します。


#### 3.2.2.Tor経由の接続





- 機能**：接続を暗号化する匿名ネットワーク、**Tor**を介してネットワークトラフィックをルーティングします。
- なぜですか？あなたのIP Addressを隠し、プライバシーを保護します。ネットワークが信頼できない場合（公共のWi-Fiなど）に最適です。
- デメリット**：暗号化によりアプリケーションの動作が遅くなる可能性があります。
- 推奨**：機密保持を優先する場合はTorを有効にし、接続速度をテストすること。


#### 3.2.3.パーソナル・ノードへの接続





- 機能**：アプリケーションを**Electrum**サーバー経由で**完全なBitcoinノード**に接続します。
- その理由Blockchainのデータを完全にコントロールし、Blockstreamサーバーへの依存を排除します。
- 前提条件**：設定済みの Bitcoin ノード。
- 推奨**：最大限の主権を求める上級ユーザー。


#### 3.2.4.SPVの検証





- 機能**：簡易支払い検証(SPV)**を使用し、チェーン全体をダウンロードすることなく、特定のBlockchainデータを直接検証します。
- なぜか？Blockstreamのデフォルト・ノードへの依存を減らしつつ、モバイル・デバイス向けに軽量化を実現。
- 欠点**：情報の一部をサードパーティーのノードに依存するため、Full nodeよりも安全性が低い。
- 推奨**：パーソナル・ノードは使えないが、Full nodeが最適なセキュリティのために必要であれば、SPVをアクティブにする。





## 4.Bitcoinオンチェーン・ポートフォリオの作成



### 4.1.作成開始





- 注意**：カメラや監視者のいないプライベートな環境でポートフォリオをセットアップしてください。
- ホーム画面から「Get Started」をクリック：



![image](assets/fr/04.webp)





- Cold Wallet**（オフラインWallet）を管理したい場合：**"Connect Jade "**をクリックし、Hardware Wallet Blockstream Jadeまたは他の互換性のあるColdウォレットを使用します。



![image](assets/fr/05.webp)





- 次の画面が表示される：



![image](assets/fr/06.webp)





- (1) **"Setup Mobile Wallet"** ：Hot Wallet (Hot Wallet) を新規作成します。
- (2) **「バックアップからの復元」**：Mnemonicフレーズ（12語または24語）を使用して既存のポートフォリオをインポートします。注意：Cold Wallet フレーズをインポートしないでください。Cold Wallet フレーズは、接続されたデバイス上で公開され、セキュリティが無効になります。
- (3) **"Watch-Only "**：既存の読み取り専用ポートフォリオをインポートし、Mnemonic フレーズを公開せずに残高（例：Cold Wallet）を表示します。付録の「Watch Only」チュートリアルを参照。



**このチュートリアルでは**：Setup Mobile Wallet"**をクリックして、Hot Walletを作成します。


Walletが自動的に作成され、Walletのホームページ（ここでは「My Wallet 5」）が表示されます：



![image](assets/fr/07.webp)



**重要**です：ブロックストリーム・アプリは、seedの12語のフレーズを自動的に表示しないことで、Walletの作成を簡素化しました。 *ワンクリックでポートフォリオが作成されるようになったとはいえ、seedフレーズ*を保存しないと、資金へのアクセスができなくなるリスクがあります。



### 4.2.seedの文章を保存する





- Walletのホーム画面で "Security "タブをクリックし、"Back Up "プロンプトまたは "Recovery Phrase "メニューをクリックする：



![image](assets/fr/08.webp)



seed 12語のフレーズが表示されますので、保存してください。





- リカバリーのフレーズを細心の注意を払って書き留める。紙や金属に書き留め、安全な場所（オフラインの安全な場所）に保管してください。このフレーズは、デバイスの紛失やアプリケーションの削除の際に、ビットコインにアクセスする唯一の手段となります。
- また、このフレーズを使っている人なら誰でも、あなたのビットコインをすべて盗むことができるという点にも注意が必要です。決してデジタルに保存しないでください：
 - スクリーンショットなし
 - クラウド、Eメール、メッセージングバックアップなし
 - コピー／ペーストができない（クリップボードに保存される危険性がある）



**!このポイントは重要です**。バックアップの詳細については：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3.seedの文章を確認する



このseedセンテンスに関連するAddressに資金を送る前に、12ワードのバックアップをテストしなければならない。



そのために、リファレンスを書き留め、Walletを削除し、バックアップでリストアし、リファレンスが変更されていないことをチェックする。





- Walletのホーム画面で、「設定」タブをクリックし、「Walletの詳細」をクリックし、zPub（[拡張公開鍵](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602)）をコピーする：



![image](assets/fr/09.webp)



注：zpub Addressは、"Watch Only "機能のためにBlockstreamアプリケーションにインポートすることができます（付録を参照）。





- アプリケーションを削除し、Mnemonicのフレーズを入力して**"Restore from Backup "**からWalletを復元し、zpubが変更されていないことを確認してください。バックアップが正しければ、Walletに資金を送ることができます。





- リカバリーテストの実施方法については、専用のチュートリアルをご覧ください：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5.アプリケーションへのアクセスの保護



強力なPINコードでアプリケーションへのアクセスをロックします：




- Walletのホーム画面から、**"Security "**に進み、**"PIN "**をクリックする。
- ランダムな6桁のPINコード**を入力し、確認してください。



**生体認証オプション**：利便性を高めるために利用できるが、堅牢なPINコードより安全性は低い（不正アクセスのリスク、例えば睡眠中の指紋や顔のスキャン）。



**注**：PINはデバイスを保護するが、seedフレーズのみが資金を取り出すために使用できる。





## 5.オンチェーンWalletの使い方



### 5.1.ビットコインを受け取る





- ポートフォリオのホーム画面から「**Transact**」をクリックし、次に「**"Receive "**」をクリックする。



![image](assets/fr/10.webp)





- アプリケーションには**空白の受信Address**（SegWit v0フォーマット、`bc1q...`で始まる）が表示されます。Bitcoinを受信するたびに新しいAddressを使用することで、秘匿性が向上します。





- オプション** ：
    - (1) "Bitcoin"：オンチェーンまたはLiquid貨物をクリックして選択し、資産を選択します。
    - (2) 矢印をクリックして、このseedセンテンスにリンクされている別の新しいAddressを選択します。
    - (3)右上の3つの点をクリックし、"List of Addresses "をクリックすることで、すでに使用／表示されているAddressから選択することもできます。
    - (4) 金額を指定して請求する場合は、右上の3つの点をクリックして「Request amount」を選択し、希望する金額を入力する。QRが更新され、AddressがBitcoinの支払URIに変わります。




![image](assets/fr/11.webp)





- Address/URIを共有するには、"**共有**"をクリックするか、テキストをコピーするか、QRコードをスキャンしてください。
- 検証**：受信者と共有されたAddressを可能な限りチェックし、エラーや攻撃（マルウェアによるクリップボードの改ざんなど）を回避する。



### 5.2. ビットコインを送る





- ポートフォリオのホーム画面から、"**Transact**"をクリックし、次に**"Send "**をクリックします：



![image](assets/fr/12.webp)





- 詳細を入力** ：
    - (1) 受取人**の**Addressを貼り付けるか、QRコードをスキャンして入力する。
    - (2) 送金元の資産と口座を確認する。
    - (3) 送信する**金額を指定します。単位を選択できます：BTC、サトシ、米ドル、...


2025年3月8日の最低限度額（ダッシュリミット）は546Sats。




    - (4) **取引手数料** を選択する：
        - 緊急度に応じて推奨されるオプション（例：高速、中速、低速）から選択すると、おおよその転送時間が表示されます。
        - カスタマイズされた料金については、vバイトあたりのSatoshiの数を手動で調整する（市場料金については[Mempool.space](https://Mempool.space/)を参照）。




![image](assets/fr/13.webp)





- チェック** ：
    - サマリー画面でAddress、金額、料金を確認する。
    - Addressのエラーは、取り返しのつかない損失をもたらす可能性があります。クリップボードを改ざんするマルウェアにご注意ください。



![image](assets/fr/14.webp)





- 確認**：送信 "ボタンをスライドさせ、取引に署名し配布する。
- フォローアップ**：Walletの "Transact "タブでは、取引は確認（1～6回の確認）されるまで "pending "と表示される：



![image](assets/fr/15.webp)





- 取引が確定していない限り、"Replace by fee "機能（付録参照）により、取引手数料を増額することで、その処理を早めることができる：



![image](assets/fr/16.webp)




## 付録



### A1.その他のBlockstreamチュートリアル



Liquid Networkの使い方



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

ウォッチ・オンリー」モードでのWalletのインポートとトラッキング



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

デスクトップ版



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2.Replace-by-fee（RBF）の説明



**定義**：Replace-by-fee（RBF）はBitcoinネットワークの機能であり、送信者が高い手数料を支払うことに同意することで、**オンチェーン**取引の確認を早めることができる。



**限界** ：




- RBFは、LiquidまたはLightning取引では利用できない。
- 最初の取引は、作成時にRBF互換とマークされなければならないが、これはBlockstream Appが自動的に行う。



**詳細はこちら




- [用語集](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3.ベストプラクティス



ブロックストリームアプリ**を安全かつ効率的に使用するには、以下の推奨事項に従ってください。これらの推奨事項は、**Bitcoin (onchain)**、**Liquid**、および**Lightning**ネットワーク上で資金を保護し、取引を最適化し、機密性を保持するのに役立ちます。





- リカバリーフレーズの確保** ：
 - チュートリアルMnemonicフレーズの保存



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- 安全な認証を使用する** ：
 - アプリケーションへのアクセスを保護するために、**強力な暗証番号**または**生体認証**（指紋または顔認証）を有効にします。
 - 暗証番号や生体認証データは絶対に共有しないでください。





- プライバシーの保護** ：
 - Blockchainのトレースを制限するために、generateまたはLiquidの受信ごとに新しいAddressを作成する。
 - プライバシー強化"、"Tor"、"SPV "機能を有効にする。
 - 最大限の機密性を確保するため、Walletはパブリック・ノードを使用せず、Electrumサーバーを経由して自分のBitcoinノードに接続してください。





- お客様のニーズに最適なネットワークをお選びください：
 - オンチェーン**：長期保管や大口取引に有利（手数料は金額に対してごくわずか）。
 - Liquid**：機密性を強化した高速、低コストの転送に使用。
 - ライトニング**：少額を即座に低コストで送金できます。





- 発送先住所は必ずご確認ください：
 - 送金する前に、Addressをよく確認してください。間違ったAddressに送金された資金は永遠に失われます。コピー・ペーストかQRコード・スキャンを使用し、決してAddressを手でコピー・修正しないでください。





- コストの最適化** ：
 - オンチェーン取引では、緊急度とネットワークの混雑度に応じて適切な手数料（低速、中速、高速）を選択する。
 - 少量ならLiquid、少量ならライトニングを使う。





- アプリケーションを最新の状態に保つ




### A4.追加リソース





- 公式リンク
 - [公式サイト](https://blockstream.com/)**
 - [モバイルアプリケーションのサポート](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : ドキュメントとチャット
 - [GitHub](https://github.com/Blockstream/green_android)**





- ブロック・エクスプローラー
 - on chain ： **[Mempool.space](https://Mempool.space/)**
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