---
name: Satochip x SeedSigner
description: SeedSignerでSatochipを使うには？
---

![cover](assets/cover.webp)



*このチュートリアルで使用するスマートカード・サポート用のSeedSignerファームウェアのforkを提供してくれた[Crypto Guide](https://www.youtube.com/@CryptoGuide/)に感謝する。



---

サトチップは、walletスマートカード形式のハードウェアで、最高レベルのセキュリティ基準であるEAL6+認証を受けたセキュリティ・エレメントを備えている。ベルギーの同名の会社：Satochipによって設計・製造されています。



約25ユーロという価格のサトーチップは、その優れたコストパフォーマンスで競合製品から抜きん出ている。セキュア・チップのおかげで、物理的な攻撃にも耐えられる。さらに、アプレットのソースコードは完全にオープンソースで、*AGPLv3*の下でライセンスされている。



その一方で、その形式が機能的な制限を課している。サトチップの主な欠点は、統合されたスクリーンがないことである。したがって、ユーザーはコンピュータのディスプレイだけを頼りに、やみくもに取引にサインしなければならない。



この弱点を克服するために、特に興味深いのはSeedSignerと組み合わせて使用することである。このセットアップでは、通信はもはやコンピューターとサトチップの間で直接行われるのではなく、コンピューターとSeedSignerの間でQRコードの交換を介して行われる。SeedSignerは署名される情報を表示し、署名自体はSatochipが行う。従来のSeedSignerの使い方（あるいはSeedkeeperとの併用）とは異なり、seedがSeedSignerに読み込まれることはない。そのため、SeedSignerがSatochipの画面となり、ブラインド署名のリスクを排除することができる。



逆の見方をすれば、SeedSignerとSatochipを併用することで、SeedSignerの大きなギャップを埋めることができる。



私見では、この構成は従来のハードウェア・ウォレットに比べていくつかの利点がある：




- Satochipの価格は約25ユーロで、アプレットはオープンソースなので、空白のスマートカードに自分でインストールできる。そして、SeedSignerのコンポーネントとスマートカード読み取り用の拡張機能のコストを追加する必要がある。このハードウェアをどこで購入するかにもよるが、合計で70ユーロから100ユーロになるはずだ。
- SeedSignerファームウェアとSatochipアプレットである。
- 認証されたセキュリティー要素から利益を得ることができる。
- この設定は、Bitcoinの使用を明確に意図したハードウェアに頼ることなく、完全にDIYで行うことができます。これは、ある種のもっともらしい否認可能性を提供し、ある種の外部からの脅威（国によっては、国家の圧力を含む）に対する抵抗となります。また、商用ハードウェアのウォレットへのアクセスがあなたの地域で制限されていたり、不可能であったりする場合にも、これは興味深い解決策となります。




## 1.必要な材料



このセットアップを行うには、以下のものが必要です：




- 古典的なSeedSignerに必要な通常の機器：
 - GPIOピンを備えたRaspberry Pi Zero、
 - 1.3インチのWaveshareスクリーン、
 - 互換性のあるカメラ、
 - microSDカード。



![Image](assets/fr/01.webp)





- SeedSignerの拡張キットは[Satochip公式ストアから](https://satochip.io/product/seedsigner-extension-kit/)入手可能で、SeedSignerから直接スマートカードの読み書きができます。もう一つの方法は、[外付けのスマートカードリーダー](https://satochip.io/product/chip-card-reader/)を使うことです。これはRaspberry PiのMicro-USBポートにケーブルで接続できます。しかし、私自身はこのソリューションをテストしていません；
- [Satochip](https://satochip.io/product/satochip/)、もしくはSatochipアプレットをインストールするための[空白のスマートカード](https://satochip.io/product/card-for-diy-project/)が必要です(Satochipから販売されている拡張キットには空白のスマートカードが含まれています)。Satochipの拡張キットは[SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/)フォーマットもサポートしています。お好みでこのフォーマットを選ぶことができます。



![Image](assets/fr/02.webp)



SeedSignerの組み立てに必要な機器の詳細については、このチュートリアルのパート1を参照してください：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2.ファームウェアのインストール



SeedSignerをSatochipで使用するためには、スマートカードの読み取りをサポートするために、オリジナルのSeedSignerとは別のファームウェアをインストールする必要があります。これには、[「**3rdIteration**」のforkを使うことをお勧めします](https://github.com/3rdIteration/seedsigner)。お使いのRaspberry Piのモデルに対応する[最新版のイメージ](https://github.com/3rdIteration/seedsigner/releases) (`.zip`)をダウンロードしてください。



![Image](assets/fr/03.webp)



まだお持ちでない場合は、[Balena Etcher]ソフトウェア（https://etcher.balena.io/）をダウンロードし、以下の手順で進めてください：




- microSDカードをコンピュータに挿入します；
- エッチャーを起動します；
- ダウンロードした`.zip`ファイルを選択する；
- ターゲットとしてmicroSDカードを選択します；
- フラッシュ！」をクリックする。



![Image](assets/fr/04.webp)



プロセスが完了するまで待ちます。これでmicroSDを使用する準備が整いました。これでmicroSDの使用準備が整いました。



ファームウェアのインストールとソフトウェアの検証（このステップを踏むことを強くお勧めする）の詳細については、以下のチュートリアルを参照のこと：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3.スマートカードリーダーの組み立て



カメラをRaspberry Pi Zeroに取り付け、カメラピンに慎重に差し込み、黒いタブでロックします。次に、Piをケースの底に置き、ポートが対応する開口部に合うようにします。



![Image](assets/fr/05.webp)



次に、スマートカードリーダーをRaspberry Pi ZeroのGPIOピンに取り付ける。



![Image](assets/fr/06.webp)



スマートカードリーダーが正しい位置に来るまで、プラスチックカバーをスライドさせてください。



![Image](assets/fr/07.webp)



次に、拡張機能のGPIOピンにスクリーンを追加する。



![Image](assets/fr/08.webp)



最後に、ファームウェアの入ったmicroSDカードをRaspberry Pi Zeroのサイドポートに挿入する。



![Image](assets/fr/09.webp)



SeedSignerは、Raspberry Pi ZeroのMicro-USBポート経由でも、拡張機能のUSB-Cポート経由でも接続できます。どちらの方法でも動作します。起動まで数秒待つと、ウェルカムスクリーンが表示されます。



![Image](assets/fr/10.webp)



SeedSignerの初期設定の詳細については、以下のチュートリアルのパート4を参照することをお勧めします：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4.Satochipアプレットでスマートカードをフラッシュする（オプション）



すでにSatochipをお持ちの方は、このステップを飛ばしてステップ4に進んでください。このセクションでは、空のスマートカードにSatochipアプレットをインストールする方法を説明します（DIY方法）。アプレットはスマートカード上で動作する小さなプログラムで、特定の機能を管理することができます。



まず、SeedSignerの「ツール > スマートカードツール」メニューを開いてください。



![Image](assets/fr/11.webp)



次に`DIY Tools > Install Applet`を選択する。



![Image](assets/fr/12.webp)



スマートカードをチップを下向きにしてSeedSignerリーダーに挿入し、`Satochip`アプレットを選択します。



![Image](assets/fr/13.webp)



インストールには数十秒かかることがあります。



![Image](assets/fr/14.webp)



アプレットが正常にインストールされたら、ステップ4に進むことができます。



![Image](assets/fr/15.webp)




## 5.seedの作成と保存



### 5.1.seedの生成



これでハードウェアとソフトウェアがすべて正しく動作するようになったので、Bitcoin ポートフォリオの作成に進むことができます。SeedSignerを接続し、従来のSeedSignerと同様にサイコロを振るか写真を撮ってgenerateを作成します：




- ツール > カメラ / サイコロの目」メニューに進みます；
- その後、選択した方法に従ってエントロピー生成プロセスに従う；
- 最後に、seedを物理メディアにバックアップし、バックアップを入念にチェックする。



![Image](assets/fr/16.webp)



この手順の詳細をご覧になりたい方は、このチュートリアルのパート5をご覧ください：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2.seedをシードキーパーに保存する



いったんseedが生成されると、それがSeedSignerのRAMに存在するのはこのときだけである。私の場合、これを[Seedkeeper](https://satochip.io/product/seedkeeper/)に保存したい。[Seedkeeper](https://satochip.io/product/seedkeeper/)は、秘密を保存するために設計された、もう一つのサトーチップ製品である。このデバイスは、サトチップを紛失した場合の最後の手段として使うつもりだ。



ここで選択するバックアップ戦略は好みによるが、ニーモニック・フレーズのコピーを少なくとも1部、物理メディア（紙や金属）か、ここでのようにSeedkeeperに保存しておくことは必須である。必要に応じてバックアップの数を増やすこともできます。ポートフォリオのバックアップ戦略の詳細については、こちらのチュートリアルをお読みいただきたい：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

シードキーパーでseedをバックアップするには、直接`Backup Seed`メニューに進みます。



![Image](assets/fr/17.webp)



次に、SeedKeeperをスマートカードリーダーに挿入し、「To SeedKeeper」を選択します。



![Image](assets/fr/18.webp)



PINを入力してロックを解除してください。



![Image](assets/fr/19.webp)



Seedkeeperに保存されている様々な秘密を簡単に識別するために、「ラベル」を選択してください。例えば、walletの刻印を残すこともできますし、「Seed」と明示することもできます。お好みやリスクに応じてお選びください。



![Image](assets/fr/20.webp)



もしあなたのバックアップ戦略がこのSeedkeeperだけに依存しているのであれば、今すぐ空のリカバリーテストを実行し、フィンガープリントを比較してバックアップが機能していることを確認することを強くお勧めします。



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

PINコードは、カードが物理的に漏洩した場合にブルートフォース(総当たり)攻撃を防ぐため、できるだけ長くランダムなものにしてください。また、このPINコードのバックアップをSeedkeeperとは別の場所に保管しておく必要があります。この PIN コードがないと、Seedkeeper に保存されているニーモニックにアクセスできず、ビットコインは永久に失われます。



### 5.3.サトシップでseedを節約



あなたのポートフォリオが作成され、保存され、確認されたので、それをSatochipに転送します。これを行うには、seedがSeedSignerのRAMにロードされていることを確認してください。次に「Tools > Smartcard Tools > Satochip Functions」を開きます。



![Image](assets/fr/21.webp)



スマートカードリーダーにSatochipを挿入し、`Initialise with Seed`を選択します。



![Image](assets/fr/22.webp)



カードが新しく初期化されていないため、PINコードはまだ存在しません。このステップをスキップするには、任意のコードを入力してください（ブロックするものではありません）。



![Image](assets/fr/23.webp)



SeedSignerはあなたのSatochipが初期化されていないことを検出します。I Understand`をクリックして確認してください。



![Image](assets/fr/24.webp)



そして、4文字から16文字までのSatochip PINコードを設定することができます。walletのセキュリティーを強化するために、長くてランダムなコードを選んでください。



この暗証番号は、作成後すぐに、安全なパスワードマネージャーか、物理的な媒体に保存することを忘れないでください。後者の場合、暗証番号の入った媒体をサトーチップと同じ場所に保管しないようにしてください。バックアップを取ることが重要です： **このPINがないと、seedにアクセスできず、ビットコインは永遠に失われます**。



![Image](assets/fr/25.webp)



SeedSignerは次に、どのseedをSatochipにインポートするか尋ねてくる。今作成したポートフォリオとフィンガープリントが一致するものを選択する。



![Image](assets/fr/26.webp)



あなたのseedがサトキップにインポートされました。



![Image](assets/fr/27.webp)



これでSeedSignerをオフにすることができます。



passphraseのBIP39を使用してwalletのセキュリティを強化したい場合は、このチュートリアルのパート6を参照してください：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6.Sparrowにwalletをインポートする



お客様のポートフォリオが稼動しましたら、Sparrow Walletまたは他のポートフォリオ管理ソフトウェアにその公開情報（「*keystore*」）をインポートします。このソフトウェアは、あなたの取引を作成、配布、追跡するために使用されます。ただし、この操作に必要な秘密鍵はサトチップ（およびバックアップ）のみが保持しているため、サトチップは取引に署名することはできません。



### 6.1 SeedSignerとSatochipの準備



OSの入ったmicroSDカードを挿入し、SeedSignerの電源を入れます。まだseedを知らないので、何もできません。seedが入っているのはスマートカードリーダーなので、まずはSatochipをスマートカードリーダーに挿入してください。



ホーム画面から「ツール」>「スマートカードツール」>「Satochip Functions」メニューにアクセスします。



![Image](assets/fr/28.webp)



次に`Export Xpub`をクリックする。



![Image](assets/fr/29.webp)



ポートフォリオのタイプを選択する。この例ではシングル・ポートフォリオなので、`Single Sig`を選択する。



![Image](assets/fr/30.webp)



次にスクリプト規格の選択だ。最新の`Native SegWit`を選択する。



![Image](assets/fr/31.webp)



最後に、`Coordinator`、つまり使用したいポートフォリオ管理ソフトを選択する。ここではSparrow Walletを使用する。



![Image](assets/fr/32.webp)



警告メッセージが表示されます：これは完全に正常です。拡張公開鍵(`xpub`)は、あなたのseed(最初のアカウント)に由来するすべてのアドレスを閲覧することを可能にする。しかし、あなたの資金にアクセスすることはできません。その公開はあなたのプライバシーを損なうことになりますが、ビットコインの安全性を損なうものではありません。つまり、残高を見ることはできますが、使うことはできません。



I Understand`をクリックしてください。



![Image](assets/fr/33.webp)



次に、SatochipのPINコードを入力してロックを解除します。これはステップ5で定義して保存したコードです。



![Image](assets/fr/34.webp)



最後に、表示された情報に問題がなければ、`Export Xpub`をクリックしてください。



![Image](assets/fr/35.webp)



SeedSignerは、Sparrow Walletでポートフォリオを管理するために必要なすべてのデータを含むダイナミックQRコードの形であなたのxpubを生成します。ジョイスティックを使って画面の明るさを調整することで、QRコードの読み取りを容易にすることができます。



### 6.2 Sparrow Wallet への新しいポートフォリオのインポート



Sparrow Wallet ソフトウェアがコンピュータにインストールされていることを確認してください。ダウンロード、真偽の確認、正しいインストールの方法がわからない場合は、チュートリアルをご覧ください：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

パソコンでSparrow Walletを開き、メニューバーの`ファイル → Walletのインポート`をクリックします。



![Image](assets/fr/36.webp)



SeedSigner`までスクロールダウンし、`スキャン...`を選択します。ウェブカメラが起動しますので、SeedSignerの画面に表示されているダイナミックQRコードをスキャンしてください。



![Image](assets/fr/37.webp)



ポートフォリオに名前を付け、`Create Wallet`をクリックする。Sparrow は、この wallet へのローカルアクセスをロックするためのパスワードの設定を要求します。強力なパスワードを選択してください：Sparrowのデータ（公開鍵、住所、ラベル、取引履歴）を保護します。ただし、このパスワードは、将来walletを復元する際には必要ありません：あなたのニーモニック・フレーズ（そしておそらくpassphrase）だけが必要となります。



このパスワードを紛失しないよう、パスワード・マネージャーに保存しておくことをお勧めする。



![Image](assets/fr/38.webp)



キーストアが正常にインポートされました。



![Image](assets/fr/39.webp)



Sparrow Walletに表示された`Master fingerprint`が、以前にSeedSignerで見つかったものと一致することを確認する。



SeedSignerは、インポートの有効性を確認するために、Sparrow walletからランダムな受信アドレスをスキャンするよう要求します。



![Image](assets/fr/40.webp)



サトチップ（SeedSigner経由）とSparrow Walletが安全に接続されました。Sparrowは完全な管理インターフェイスとして機能し、Satochipはあなたの取引に署名できる唯一のデバイスのままです。これで、完全にエアギャップされた構成でビットコインを送受信する準備が整いました。



![Image](assets/fr/41.webp)



## 7.ビットコインの送受信



これでサトチップとSparrow Walletが連動するように設定されました。ここでは、このモードでビットコインを送受信する方法を順を追って説明します。



### 7.1 ビットコインを受け取る



#### 7.1.1 受信アドレスの生成



パソコンで Sparrow Wallet を開き、パスワードを使って `Satochip-SeedSigner` wallet のロックを解除します。ソフトウェアがサーバに接続されていることを確認する（右下のインジケータ）。サイドバーの「受信」をクリックする。



![Image](assets/fr/42.webp)



新しいBitcoinアドレスが表示されます。あなたは：




- テキスト形式のアドレス（この例のようにP2WPKHを使っている場合は`bc1q...`で始まる）；
- 関連するQRコード；
- トランザクションをトレースするのに便利な `Label` フィールドである。



walletの各ビットコインのレシートにラベルを追加することを強くお勧めします。そうすることで、各UTXOの出所を簡単に特定することができ、プライバシーをより適切に管理することができます。この重要なテーマについてもっと知りたい方は、Plan ₿ Academyの専用トレーニングをご覧ください：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

ラベルを追加するには、`Label`フィールドに名前を入力し、確定するだけです。



例えば、こうだ：



```txt
Label : Sale of the Raspberry Pi Zero
```



Sparrowのすべてのセクションで、あなたの住所がこのラベルに関連付けられました。



![Image](assets/fr/43.webp)



#### 7.1.2 SeedSignerでのAddress検証



受取アドレスを支払人に伝える前に、そのアドレスがあなたのseedに属していることを確認することが重要です。このステップにより、サ トチップがこのアドレスに関連する取引に署名できることが保証されます。また、Sparrowが不正なアドレスを表示する攻撃を防ぐこともできます。Sparrowは安全でない環境（あなたのコンピューター）上で動作しており、その攻撃対象は完全に隔離されているあなたのSatochipよりもはるかに大きいことに留意してください。このため、walletのハードウェアでアドレスを確認する前に、Sparrowで表示されるアドレスを決して盲目的に信用すべきではありません。



Sparrowでは、住所のQRコードをクリックして拡大すると、フルスクリーンで表示されます。



![Image](assets/fr/44.webp)



SeedSignerのリーダーにSatochipを挿入し、メインメニューから「スキャン」を選択します。パソコンに表示されたQRコードを読み取り、「Satochipカードを使用する」を選択します。



![Image](assets/fr/45.webp)



次に、使用するスクリプトの種類（この場合は`Native SegWit`）を確認し、Satochip PINコードを入力してロックを解除し、`xpub`情報を検証する。



![Image](assets/fr/46.webp)



スキャンされたアドレスがseedに由来するものと一致した場合、SeedSignerはメッセージを表示します：Address Verified`と表示されます。



![Image](assets/fr/47.webp)



そうすれば、そのアドレスがあなたのポートフォリオのものであることを確認できる。



#### 7.1.3 資金の受け取り



このアドレスをテキスト形式またはQRコードで、サッツを送る必要のある人や部署に送信することができます。トランザクションがネットワーク上でブロードキャストされると、Sparrow Walletの`Transactions`タブに表示されます。



![Image](assets/fr/48.webp)



### 7.2 ビットコインを送る



Satochip-SeedSignerの構成でビットコインを送るには3つのステップがあります：




- Sparrow におけるトランザクションの作成 ；
- SeedSignerを介して、Satochip上でこのトランザクションに署名する；
- 最後に、トランザクションはSparrowからネットワーク上にブロードキャストされる。



2つのデバイス間のやりとりは、すべてQRコードを通じてのみ行われる。



#### 7.2.1 Sparrowでのトランザクションの作成



Sparrow Walletでは、左側のサイドバーにある`Send`タブをクリックすることでトランザクションを作成することができる。しかし、私は*Coin Control*を実践できる`UTXOs`タブを使うことを好む。この方法は、トランザクション中に明らかになる情報を制限するために、使用するUTXOを正確にコントロールすることができる。



UTXOs`タブで使いたいコインを選択し、`Send Selected`をクリックします。



![Image](assets/fr/49.webp)



その後、取引フィールドに記入する：




- 支払い先」で、受取人のアドレスを貼り付けるか、カメラアイコンを使ってQRコードをスキャンします；
- Label`に、この支出を追跡するためのラベルを追加する；
- Amount`に送信する金額を入力する；
- 最後に、現在のネットワーク状況に応じて充電率を選択する（見積もりは[mempool.space](https://mempool.space/)で入手可能）。



すべての項目を入力したら、情報をよく確認し、`Create Transaction >>`をクリックしてください。



![Image](assets/fr/50.webp)



最後にもう一度取引の詳細が正確かどうかを確認し、「Finalize Transaction for Signing（署名のために取引を確定する）」をクリックします。



![Image](assets/fr/51.webp)



取引の準備は整いましたが、まだ署名はされていません。PSBT(*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt)をQRコードとして表示するには、`Show QR`をクリックしてください。



![Image](assets/fr/52.webp)



#### 7.2.2 サトシップとの契約



SeedSignerの電源を入れ、通常通りSatochipを挿入します。ホーム画面から「スキャン」を選択し、Sparrowに表示されているQRコードをスキャンします。



![Image](assets/fr/53.webp)



サトチップカードを使用する」オプションを選択する。



![Image](assets/fr/54.webp)



PINコードを入力してスマートカードのロックを解除してください。



![Image](assets/fr/55.webp)



SeedSignerはこれがPSBTであることを検知し、取引の概要を表示する：




   - 送金額、
   - 宛先アドレス、
   - 関連する取引コスト。



詳細を確認する」をクリックし、SeedSignerの画面で直接すべての情報を精査してください。最も重要なチェックポイントは、送金額、送金先の住所、送金手数料です。



![Image](assets/fr/56.webp)



問題がなければ、`Approve PSBT`を選択し、Satochipを使用して取引に署名する。



![Image](assets/fr/57.webp)



署名が完了すると、SeedSignerは署名されたトランザクションを含む新しいQRコードを生成し、Sparrowでスキャンできるようにする。



#### 7.2.3 Sparrowからのトランザクションのブロードキャスト



これでトランザクションは署名され検証されたので、あとはBitcoinネットワークにブロードキャストして、採掘者がブロックに含めることができるようにするだけである。Sparrowで「Scan QR」をクリックする。



![Image](assets/fr/58.webp)



SeedSignerに表示されているQRコード（署名された取引が含まれているもの）をウェブカメラに提示してください。すると、Sparrowに取引の詳細が表示されます。すべての情報が正しいことを確認し、"Broadcast Transaction "をクリックしてBitcoinネットワークにブロードキャストします。



![Image](assets/fr/59.webp)



あなたの取引がネットワークに送信されました。Sparrow Walletの`取引`タブで確認できます。



![Image](assets/fr/60.webp)



## 8.walletを取り戻せ



これまでのセクションで見てきたように、あなたのセキュリティ戦略に応じて、サトチップに加えてリカバリーフレーズをバックアップする方法がいくつかあります：




- 古典的な*SeedQR*をSeedSignerで使用する；
- ニモニック・フレーズを物理的媒体に記録する；
- あるいは、5.2節で説明したように、シードキーパーに保存することもできる。



いずれにせよ、あなたが介入する必要がある主な状況は2つある：Satochipの紛失またはSeedSignerの紛失。それぞれのシナリオにどのように対応すべきかを見てみよう。



### 8.1.さとキップでwalletを取り戻す



サトシップはまだ持っているが、シードシグナーが壊れたり紛失したりした場合、walletはまだサトシップの中にあるので、状況はかなりシンプルに管理できる。



最良の方法は、必要なコンポーネントを推奨し、ゼロから新しいSeedSignerを再構築することです。これは "ステートレス "デバイスなので、同じSeedSignerを使用しているか、別のSeedSignerを使用しているかは関係ありません。



SeedSignerを経由せず、コンピュータから直接Satochipを使用することもできます。この方法は完璧に機能しますが、Bitcoin walletのセキュリティをかなり低下させます。SeedSignerが信頼できるスクリーンとして機能するため、「*エアギャップ*」による隔離を失い、ブラインドで署名しなければなりません。しかし、これは緊急時やSeedSignerを再構築できない場合の一時的な解決策になります。



これを行うには、USBスマートカードまたはNFCリーダーが必要です。Sparrowで復元したいwalletを開き、`Settings`タブで`Replace`をクリックします。



![Image](assets/fr/61.webp)



コンピューターに接続されたスマートカードリーダーにサトチップを挿入し、「Satochip」の隣にある「Import」をクリックします。



![Image](assets/fr/62.webp)



最後に、スマートカードの暗証番号を入力してロックを解除します。その後、walletにアクセスし、接続されたSatochipを使用して直接取引を作成し、署名することができます。



### 8.2.SeedSignerでポートフォリオを取得する



もう一つの、よりデリケートなシナリオは、seedを含むSatochipにアクセスできなくなった場合です：壊れた、紛失した、盗まれた、PINコードを忘れたなど。Satochipが盗まれたり紛失したりした場合、資金へのアクセスが回復したら、すぐに別のseedで生成された新しいwalletにビットコインを移すことを強くお勧めします。こうすることで、潜在的な攻撃者があなたのサッツにアクセスすることができなくなります。



ポートフォリオへのアクセスを回復し、資金を移動するには、seedをSeedSignerにロードするだけです。使用したバックアップメディアによって、いくつかのオプションがあります：





- Seeds > Enter 12-word seed` メニューでニーモニックフレーズを手入力する。



![Image](assets/fr/63.webp)





- ホームページの「スキャン」ボタンをクリックして、*SeedQR*をスキャンしてください。



![Image](assets/fr/64.webp)





- または、「Seeds > From SeedKeeper」メニューからseedをSeedkeeperからロードします（このチュートリアルではこの方法を使用します）。SeedKeeperのPINを入力し、SeedSigner上でseedとして使用するシークレットを選択するだけです。



![Image](assets/fr/65.webp)



seedがSeedSignerにロードされると、どの方法を使っても、1つ以上のスキャン取引に署名して、ビットコインを新しい、妥協のないwalletに移動させることができるようになります。この方法については、以下のチュートリアルのパート7.2を参照してください：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

これで、SeedSignerと組み合わせてBitcoinポートフォリオを安全に管理するためのSatochipの使い方がお分かりいただけたと思います。



この設定に納得したなら、それを可能にするプロジェクトを支援することをためらわないでほしい：




- サトチップウェブサイト](https://satochip.io/shop/)から直接ご購入いただけます；
- SeedSignerプロジェクトに寄付する](https://seedsigner.com/donate/)；
- Crypto GuideのYouTubeチャンネル](https://www.youtube.com/@CryptoGuide/)を購読することで、このチュートリアルで使用した修正ファームウェアをホストしているGitHubリポジトリを管理している人物によって運営されている。