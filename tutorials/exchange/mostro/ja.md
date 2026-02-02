---
name: Mostro
description: LightningとNostrを介したKYCフリーのBitcoin P2P交換プラットフォーム
---

![cover](assets/cover.webp)



金融主権を損なうことなくビットコインを取得または売却するにはどうすればよいのだろうか。中央集権的なプラットフォームは、恣意的な口座凍結や国家監視の可能性を伴う、個人データを公開する侵襲的なKYC手続きを課します。



**Mostro P2P**は、Lightning Network、Nostrプロトコル、ホールドインボイスを組み合わせた分散型の代替手段を提供します。その主な革新点は、自動化されたエスクローシステムで、ビットコインは取引所を通してあなたの管理下に置かれ、盗難、取引所の倒産、恣意的な没収のリスクを排除します。



## モストロP2Pとは？



Mostro P2Pは、2021年に開始された人気のテレグラムボット**lnp2pbot**の開発者である**grunch**によって作成されたオープンソースのBitcoin交換プロトコルである。lnp2pbotはすでにLightning経由でKYCフリーのP2P交換を可能にしていたが、大きな脆弱性を提示していた： **テレグラムは政府による検閲の影響を受けやすい集中障害点**を構成する。



Mostroは、このコンセプトの**非中央集権的進化**を象徴している。Telegramを**Nostr**プロトコル（分散リレーの検閲不可能なネットワーク）に置き換えることで、Mostroはこのシステムリスクを排除する。このプロトコルは、インスタント・トランザクションのためのLightning Network、検閲に強いコミュニケーションのためのNostr、そして**ホールド・インボイス**を組み合わせ、真に非拘束的な自動エスクローを実現する。



### テクニカル・アーキテクチャ



モストロは、3つの要素を通じて機能している：




- デーモンMostrod**：ユーザーとLightning Network間のやりとりを調整する。
- Lightning**ノード：ホールドインボイスを作成（～24時間の暗号エスクロー）
- Mostro**のお客様：ユーザーインターフェース（CLI、モバイル、ウェブ）



注文はパブリックイベント（タイプ38383）としてNostrに公開され、プライベート取引はエンドツーエンドで暗号化されたメッセージ（NIP-59、NIP-44）を介して送信される。各Mostroインスタンスは独自の手数料（通常0.3％～1％）と取引限度額（インスタンスによって数千～数十万satsの範囲）を定義している。



### 決定的な利点



**検閲に強い**：Nostrリレーが世界のどこかに存在する限り、いかなる政府もMostroをシャットダウンすることはできません。Telegram経由の脆弱なlnp2pbotとは異なり、Mostroは**検閲に強い**交換を可能にします。



**エスクロー非保管**：ライトニング・ホールド・インボイスは、お客様のビットコインを永久に送金することなくロックします。資金はお客様の管理下に置かれ、問題が発生した場合（～24時間）には自動的にお客様に返却されます。



**デザインによる機密性**：ニーズに合わせて2つのモードが利用できます。レピュテーションモード**は、あなたのレピュテーションをNostrキーにリンクし、永続的な信頼を築きます。フルプライベートモード**は、使い捨てのエフェメラルキーで完全な匿名性を保ちます。



## 主な特徴



**分散型コミュニケーション**：すべての注文は暗号署名されたイベントを通じてNostrで公開されます。プライベートな交渉はエンドツーエンドで暗号化されたメッセージで送信され、絶対的な機密性が保証されます。



**評判システム**：反復計算による5つ星評価がNostrに永久保存されます。信頼できるトレーダーとして徐々に評判を高めることができます。



**分散型仲裁**：紛争が発生した場合、公平な仲裁人が証拠を検証し、透明性のある基準に基づいて決定を下す。各紛争は、トレーサビリティのために一意のtokenを生成する。



**支払いの柔軟性**：yadio.io為替レートサービスにより、多くの通貨をサポート。SEPA送金、PayPal、Revolut、現金、および当事者間で合意されたあらゆる方法を受け入れます。



## モストロの顧客が利用可能



Mostroは、P2P取引所のために2つの主要な運用クライアントを提供しています。



### Mostro CLI - コマンドラインクライアント



Mostro CLI**は、最も成熟した機能的なクライアントです。Rustで書かれ、コマンドラインインターフェイスを介してMostroの全機能を提供します。macOS、Linux、Windowsと互換性があります。



**メイン・コントロール** ：




- listorders`：利用可能な注文をすべて表示する
- `neworder` : 新規の売買注文を作成する。
- takesell` / `takebuy`：売買注文を取る
- fiatsent`：フィアット決済の送信を確認する
- リリース`：エスクローを解除し、交換を確定する
- getdm`：ダイレクトメッセージを表示する
- レート `rate` : 取引後に取引相手を評価する。



テクニカル・ユーザー、オートメーション、最大限の安全性を必要とする環境に最適。



### Mostro Mobile - スマートフォンアプリケーション



アルファ版の**モバイル・アプリ**は、スマートフォンから直接P2P取引を可能にします。直感的なグラフィカルInterfaceは、タブ付きナビゲーション、注文表示、高度なフィルター、取引相手とコミュニケーションするための統合チャットを備えています。



アンドロイド**で利用可能で（GitHubのAPK経由）、シンプルさと時折のモバイル取引を好むユーザーに最適な選択だ。



### Mostro-web - Interfaceウェブ（開発中）



Interface現在開発中の高度なJavaScriptウェブ・アプリケーション。広範な取引とポートフォリオ管理機能を備えた完全なユーザー体験を提供するように設計されています。インストール不要でブラウザからアクセスできます。



## インストールと設定



このチュートリアルでは、2つの主要なMostroクライアントのインストールと使用方法について説明します：CLIとモバイルアプリケーションです。



### 必須条件



始める前に必要なもの





- 十分な流動性を持つLightning Network** wallet (またはLightning互換機)
 - おすすめPhoenix、Breez、Wallet、Satoshi...
 - 最低1000サトシの流動性をテストする



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Nostr** 秘密鍵 (フォーマット `nsec1...`)
 - [nostrkeygen.com](https://nostrkeygen.com/)で専用の取引キーを作成する。
 - 重要**：Nostrキーは絶対に使用しないでください。
 - 秘密鍵は安全な場所に保管する（パスワード・マネージャー）





- オプションだが推奨**：IPアドレスを隠すためのVPNまたはTor接続



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### モストロ CLI 取り付け



#### macOSの場合



**ステップ1: Rustのチェック**。



Rustがインストールされていることを確認する（バージョン1.64以上が必要）：



```bash
rustc --version
```



Rustがインストールされていない場合：



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**ステップ2: リポジトリのクローン**作成



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**ステップ3：コンフィギュレーション



をコピーして編集する：



```bash
cp .env-sample .env
```



.env`を開き、設定を行う：



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**CLI/モバイル**の同期に重要です：CLIとモバイルアプリで同じ注文にアクセスするには、両方のクライアントで**同じMostro Pubkey**と**同じNostr relays**を使用する必要があります。モバイルアプリの設定でこれらの設定を確認してください。



![Configuration .env](assets/fr/02.webp)



**ステップ4：インストール



CLI をコンパイルしてインストールする：



```bash
cargo install --path .
```



コンパイルには1～2分かかる。mostro-cli`の実行ファイルは `~/.cargo/bin/` にインストールされます。



![Installation du CLI](assets/fr/03.webp)



**ステップ5：チェック



すべてが機能していることを確認する：



```bash
mostro-cli --help
```



注文の完全なリストが表示されるはずだ。



![Vérification avec --help](assets/fr/04.webp)



#### Linux（Ubuntu/Debian）の場合



インストールはmacOSと同じだが、.NET Frameworkが追加されている：



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



その後、macOSセクションのステップ3と4に従ってください。



#### ウィンドウズ



まず、[rustup.rs](https://rustup.rs/)を使ってRustをインストールし、PowerShell ：



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



同じ設定：`.env-sample`を`.env`にコピーし、パラメーターを記入する。



### モストロ・モバイルのインストール



#### アンドロイド



**ステップ1**：GitHubリリースページ](https://github.com/MostroP2P/mobile/releases)にアクセスし、**app-release.apk**ファイル(約65 MB)をダウンロードしてください。



![Page GitHub Releases](assets/fr/10.webp)



**ステップ2：ダウンロードしたら、ダウンロードしたAPKファイルを開きます。Androidは、このソースからのインストールを承認するように要求します。



![Téléchargement et installation APK](assets/fr/11.webp)



**ステップ3オンボーディング画面に従い、機能性を確認します：




- Bitcoinを自由に取引 - KYC**なし：Nostrのおかげで本人確認なしで取引
- デフォルトのプライバシー**：レピュテーションモードとフルプライバシーモードから選択
- あらゆる段階でのセキュリティ**：非保留請求書による保護



![Écrans d'accueil Mostro](assets/fr/12.webp)



**ステップ 4**：オンボーディングを続けて、：




- 完全に暗号化されたチャット**：エンドツーエンドの暗号化通信
- オファーを受ける**：オーダーブックを閲覧し、オファーを選択する
- 必要なものが見つかりませんか？あなた自身のカスタマイズされた順序を作成する



![Suite onboarding](assets/fr/13.webp)



**ステップ5：オンボーディングが完了すると、アプリは自動的にNostrキーのペアを生成します。メニュー(⑰)から**アカウント**に進み、**秘密の言葉**(リカバリーフレーズ)を保存します。また、この画面で前述のプライバシーモードを変更するオプションがあります。



![Menu et sauvegarde des clés](assets/fr/15.webp)



**重要**：回復フレーズを安全な場所（パスワードマネージャー、紙の金庫）に書き留めてください。



### 初期セキュリティ設定



どのようなプラットフォームを使うにせよ：





- 専用キー**：取引には別のNostr IDを使用
- 少額から**：sats 10,000円以下からスタートできる。
- 複数のリレー**：地理的に異なる3～5台のリレーを構成する
- ネットワーク保護**：VPNまたはTorを有効にしてIPアドレスを隠す
- Walletセキュア**：wallet Lightningの自動ロックを有効にする



## CLIとの併用



このセクションでは、実際のユースケースに従って、Mostro CLIを介したビットコインの購入を示します。



### ステップ1：受注可能なオーダーをリストアップする



listorders` コマンドはすべての有効なオーダーを表示します：



```bash
mostro-cli listorders
```



各注文の詳細が記載された表が表示されます：ID、タイプ（買い/売り）、金額、通貨、支払い方法。



![Liste des ordres disponibles](assets/fr/05.webp)



この例では、Revolut経由で5ユーロを売る注文が表示されています（ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`）。



### ステップ2：注文を受ける



これらのビットコインを購入するには、 `takesell` で注文を取る：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



MostroはBTCを受け取るために**Lightning invoice**の提出を求めます。正確な金額はサトシで表示されます（ここでは4715 sats）。



![Prise d'ordre de vente](assets/fr/06.webp)



### ステップ 3: ライトニング請求書の提出



wallet（Phoenix、Breezなど）から正確な金額のLightning請求書を作成し、：



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



システムは出荷を確認し、エスクローを有効にする前に売り手が保留請求書を支払うのを待つよう指示する。



![Envoi de la Lightning invoice](assets/fr/07.webp)



### ステップ4：販売者に連絡する



エスクローが有効化されたら、`dmtouser`を使って売り手から支払いの詳細を要求します：



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### ステップ5：答えの取得



ダイレクトメッセージで売り手の反応を確認する：



```bash
mostro-cli getdm
```



売り手はあなたに支払いID（ここでは彼のRevtag: `@satoshi`）を教えます。



![Réception de la réponse](assets/fr/09.webp)



### ステップ 6: フィアット決済



同意された方法（この例ではRevolut）で、指定された連絡先までお支払いください。 **すべての証拠書類**（スクリーンショット、取引参照）を保管してください。



### ステップ 7: 支払い発送の確認



支払いが完了したら、Mostro にお知らせください：



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### ステップ8：ビットコインの受け取り



売り手がフィアットの受領を確認し、`release`コマンドでエスクローを解除すると、あなたは即座に提供したLightningインボイスでビットコインを受け取ります。



### ステップ9：評価



売り手を評価し、分散型評価に貢献する：



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### 便利なコマンド



**注文のキャンセル** (注文が入る前) ：


```bash
mostro-cli cancel -o <order-id>
```



**新しい販売注文を作成する** ：


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**紛争を開く** ：


```bash
mostro-cli dispute -o <order-id>
```



## モバイル・アプリケーションとの併用



このセクションでは、実際のユースケースに沿って、モストロ・モバイルによるビットコインの販売について説明します。



### Interfaceメイン



このアプリケーションには3つのメインタブがあります：





- オーダーブック**：利用可能な買い（BUY BTC）と売り（SELL BTC）の注文を閲覧できます。
- 私の取引**：有効な注文と過去の注文を表示
- チャット**：数字を使って取引相手とコミュニケーション



![Interface principale](assets/fr/14.webp)



### 推奨構成



取引前に、メニュー (↪26) > **Settings** でいくつかの設定を行います：





- ライトニングAddress**（オプション）：直接支払いを受ける場合
- リレー**：弾力性のためにいくつかのNostrリレーを追加する（例えば `wss://nos.lol`、`wss://relay.damus.io`）。
- Mostro Pubkey**：使用しているMostroインスタンスの公開鍵を確認する。



![Paramètres de l'application](assets/fr/16.webp)



**CLI/モバイル同期**のために重要です：CLIとモバイルアプリの両方を使用している場合、両方のクライアントで**まったく同じNostrリレーとMostroパブキー**を設定してください。このように同一の設定を行わないと、両方のインターフェイスで同じ注文が表示されません。設定(上のスクリーンショット)に表示されているリレーとMostro Pubkeyは、CLIの`.env'ファイルにあるものと一致していなければなりません。



### ステップ1：売り注文の作成



右下の緑の**"+"**ボタンを押し、**SELL**（赤いボタン）を選択します。



![Boutons de création d'ordre](assets/fr/17.webp)



作成フォームに記入する：



1. **通貨**：受け取りたい通貨を選択してください（EUR、USDなど）。


2. **金額** ：金額をフィアットで入力（例：1～3ユーロ）


3. **支払い方法** ：お支払い方法をお選びください。


4. **価格タイプ**："市場価格 "を選択


5. **プレミアム**：プレミアムを調整する（-10%から+10%までのスライダー、推奨：早く売るには0%)



注文を公開するには、**送信**を押してください。



### ステップ2：出版確認



ご注文が公開されました！24時間有効です。cancel`コマンドを実行することで、バイヤーが注文する前にいつでもキャンセルすることができます。



![Ordre publié](assets/fr/18.webp)



注文は**My Trades**タブに表示され、ステータスは "Pending"、バッジは "Created by you "です。



### ステップ3：バイヤーが注文を受ける



バイヤーがあなたの注文を受けると、通知が届きます。詳細は**My Trades**をご覧ください。



![Ordre pris par un acheteur](assets/fr/19.webp)



**重要なお知らせです：ビットコイン(ここでは1-5ユーロで4674sats)をエスクローにロックするために、表示されたホールドインボイス**を支払う必要があります。最長15分**の猶予があります。



保留の請求書をコピーし、wallet Lightning（Phoenix、Breezなど）から支払う。



### ステップ4：買い手とのコミュニケーション



エスクローが有効になったら、**CONTACT**を押して、バイヤーとの暗号化されたチャットを開きます。



バイヤー（ここでは "anonymous-gloriaZhao"）があなたの支払詳細を要求するためにあなたに連絡します。あなたの詳細（Revtag、IBANなど）を返信してください。



![Chat avec l'acheteur](assets/fr/20.webp)



### ステップ 5: フィアット決済の受領



Revolut口座（またはその他の合意された方法）にフィアットペイメントが入金されるまでお待ちください。 **よくご確認ください：




- 正確な金額
- 送信者
- 要求があれば、参考文献



バイヤーは、支払いを送信したことをチャットで通知します。Mostroはまた、フィアットがあなたに送信されたことを確認するメッセージを表示します。



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### ステップ6：エスクローの解除



あなたのアカウントで**フィアット支払いの受領**を確認したら、緑の**RELEASE**ボタンを押して、バイヤーにサッツを送信することを確認します。



![Libération de l'escrow](assets/fr/20.webp)



ビットコインはLightningインボイスを通じて即座に買い手に送金される。



### ステップ7：検討を評価する



リリース後、**RATE**を押してバイヤーを評価します。1つ星から5つ星（ここでは5/5）まで選択し、**Submit Rating**を押してください。



![Évaluation de la contrepartie](assets/fr/21.webp)



交換は終わった！



### モバイルアプリでビットコインを購入



ビットコインを**買う**プロセスは似ているが逆だ：



1.売り注文を表示するには、**Order Book** > **BUY BTC**タブをブラウズします。


2.興味深いオーダーをクリックして詳細を見る


3.注文を取る**を押す


4.Lightningの請求書（walletから作成されたもの）をご提出ください。


5.売り手がエスクローを有効にするのを待つ


6.お支払いの詳細については、**CONTACT**経由で出品者にお問い合わせください。


7.不換紙幣で支払う（証拠を残す）


8.売主は確認後、エスクローを解除する


9.Lightningインボイスでビットコインを即座に受け取る


10.販売者を評価する (1-5 星)



### 問題管理



**注文のキャンセルMy Trades**で、注文を押してから**CANCEL**ボタンを押します（注文が取られる前にのみ利用可能）。



**紛争を開く**：不一致が発生した場合は、注文の詳細で**DISPUTE**を押してください。すべての証拠（チャットのスクリーンショット、銀行取引の参照）を添付してください。



## 利点と限界



### メリット



**金融主権**：ホールドインボイスメカニズムにより、取引所の倒産や海賊版のリスクを排除し、ビットコインを直接管理することができます。



**検閲に強い**：いかなる権力もネットワークを遮断したり、あなたの命令を検閲することはできません。Nostrのリレーが稼働している限り、システムは機能します。



**デフォルトの匿名性**：KYCや個人情報なしで、仮名のNostrキーのみがあなたを識別します。エンドツーエンドの暗号化通信。



**支払いの柔軟性**：支払い方法の柔軟性**：相互に認められたあらゆる支払い方法が可能です（送金、モバイルアプリ、現金、物々交換）。



### 制限事項



**開発初期**：初歩的なインターフェースと技術的な学習が必要。



**限られた流動性**：注文数に限りがある、特に金額が大きい、または希少な通貨。



**技術的要件**：LightningとNostrの基本的な理解が必要。



**個人責任**：問題発生時の集中サポートはなく、注意が必要。



## 結論



Mostro P2Pは、中央集権的な取引所に代わる有望な選択肢であり、Lightning Network、Nostr、自動エスクローを組み合わせ、真の分散型取引を実現する。開発初期で流動性が限られているにもかかわらず、このプラットフォームはすでに金融主権、検閲耐性、デフォルトの匿名性を提供している。



自律性と機密性を好むビットコイナーにとって、Mostroは漸進的な探求に値する実行可能な選択肢である。その非中央集権的なアーキテクチャは、商業的進化よりもむしろコミュニティを保証し、真に自由なBitcoin取引所の未来への道を開く。



## リソース



### 公式文書




- [モストロ公式サイト](https://mostro.network)
- [技術資料](https://mostro.network/docs-english/index.html)
- [モストロ財団](https://mostro.foundation)



### ソースコードと開発




- [メインGitHubリポジトリ](https://github.com/MostroP2P/mostro)
- [ウェブクライアント](https://github.com/MostroP2P/mostro-web)
- [お客様 CLI](https://github.com/MostroP2P/mostro-cli)



### コミュニティ




- [Nostrプロトコル](https://nostr.com)
- [Lightning Networkガイド](https://lightning.network)