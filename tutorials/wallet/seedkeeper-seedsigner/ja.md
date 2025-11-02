---
name: シードキーパー×シードシグナー
description: SeedSignerとSeedkeeperの併用方法は？
---

![cover](assets/cover.webp)



*このチュートリアルで[彼らのビデオ](https://www.youtube.com/@satochip/videos)を再利用することに同意してくれた[Satochip](https://satochip.io/)チームに感謝する。また、[Crypto Guide](https://www.youtube.com/@CryptoGuide/)のSeedSignerファームウェアのForkに感謝する。



---

SeedSignerは、標準的なハードウェア（通常はRaspberry Pi Zero周辺）から自分で組み立てるHardware Walletです。このWalletは「*ステートレス*」と呼ばれ、市場に出回っている他のほとんどのモデル（Coldcard、Trezor、Ledgerなど）とは異なり、永久メモリにデータを保存せず、RAMからのみライブで動作します。その結果、あなたのポートフォリオのseedがSeedSignerに保存されることはありません。再起動するたびに、デバイスがあなたの取引に署名できるようにするために、それを入力する必要があります。最も一般的な方法は、seedをQRコードとして保存し、使用するたびにスキャンする方法です（*SeedQR*）。



しかし、この方法には重大なリスクがある。seedをスキャンできるよう、クリアテキストでアクセス可能な状態を維持しなければならないのだ。盗難や侵入があった場合、攻撃者は簡単にseedを入手し、ビットコインを盗むことができる。



この弱点を克服するため、SeedSignerはSatochip社が開発したスマートカードである[**Seedkeeper**](https://satochip.io/product/seedkeeper/)と組み合わせることができる。これにより、PINコードで保護されたsecure elementにMnemonicのフレーズ（または他の秘密）を保存することができる。Seedkeeperアプレットはオープンソースであり、そのsecure elementはEAL6+認証を受けている。SeedSignerと組み合わせて使用することで、非常に興味深いセキュリティ機能を提供する。鍵は完全にオフラインで管理され、信頼できる画面上で取引に署名し、seedは物理的攻撃に強いスマートカードで物理的に保護される。



インストールに必要なものは以下の通りです：




- 古典的なSeedSignerに必要な通常の機器：Raspberry Pi Zero、Waveshare 1.3インチスクリーン、互換性のあるカメラ、microSDカード（下記のSeedSignerチュートリアルに詳細があります）；
- SeedSignerの拡張キットが[Satochip公式ストアで](https://satochip.io/product/seedsigner-extension-kit/)販売されており、SeedSignerから直接スマートカードの読み書きができます。また、Raspberry PiのMicro-USBポートにケーブルで接続して、外付けのスマートカードリーダーを使用する方法もあります。しかし、私自身はこの方法を試していません；
- Seedkeeper、またはSeedkeeperアプレットをインストールするための空白のスマートカード（Satochipから販売されている拡張キットには、すでに空白のスマートカードが含まれています）。



![Image](assets/fr/01.webp)



このチュートリアルでは2つのシナリオを取り上げる：




- すでにBitcoinをお持ちの場合は、新しいファームウェアをインストールしてください。既存のWalletを引き続きご利用いただけます。
- BitcoinのWalletがまだSeedSignerに関連付けられていない場合は、後述のチュートリアルのステップ**5**と**6**に従う必要があります。generateにSeedSignerでMnemonicのフレーズを作成し、*SeedQR*で保存し、このWalletをSparrow walletに接続して管理する方法です。Bitcoin、Wallet、Sparrow、SeedSigner**がすでに動作していることが前提です。



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1.ファームウェアのインストール



SeedSignerをSeedkeeperで使用するためには、SeedSignerのファームウェアとは別のファームウェアをインストールする必要があります。これには、[「*3rdIteration*」のForkを使用することをお勧めします](https://github.com/3rdIteration/seedsigner)。お使いのRaspberry Piのモデルに対応する[最新バージョンのイメージ](https://github.com/3rdIteration/seedsigner/releases) (`.zip`)をダウンロードしてください。



![Image](assets/fr/02.webp)



まだお持ちでない場合は、[Balena Etcher]ソフトウェア（https://etcher.balena.io/）をダウンロードし、以下の手順で進めてください：




- microSDカードをコンピュータに挿入します；
- エッチャーを起動します；
- ダウンロードした`.zip`ファイルを選択する；
- ターゲットとしてmicroSDカードを選択します；
- フラッシュ！」をクリックする。



![Image](assets/fr/03.webp)



プロセスが完了するまで待ちます。これでmicroSDを使用する準備が整いました。これでmicroSDの使用準備が整いました。



ファームウェアのインストールとソフトウェアの検証（このステップを踏むことを強くお勧めする）の詳細については、以下のチュートリアルを参照のこと：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2.スマートカードリーダーの組み立て



![video](https://youtu.be/jqE8HDMCImA)



カメラをRaspberry Pi Zeroに取り付け、カメラピンに慎重に差し込み、黒いタブでロックします。次に、Piをケースの底に置き、ポートが対応する開口部に合うようにします。



![Image](assets/fr/04.webp)



次に、スマートカードリーダーをRaspberry Pi ZeroのGPIOピンに取り付ける。



![Image](assets/fr/05.webp)



スマートカードリーダーが正しい位置に来るまで、プラスチックカバーをスライドさせてください。



![Image](assets/fr/06.webp)



次に、拡張機能のGPIOピンにスクリーンを追加する。



![Image](assets/fr/07.webp)



最後に、ファームウェアの入ったmicroSDカードをRaspberry Pi Zeroのサイドポートに挿入する。



![Image](assets/fr/08.webp)



SeedSignerは、Raspberry Pi ZeroのMicro-USBポート経由でも、拡張機能のUSB-Cポート経由でも接続できます。どちらの方法でも動作します。起動まで数秒待つと、ウェルカムスクリーンが表示されます。



![Image](assets/fr/09.webp)



SeedSignerの初期設定の詳細については、以下のチュートリアルをお勧めします：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3.Seedkeeperアプレットでスマートカードをフラッシュする（オプション）



![video](https://youtu.be/NF4HemyEcOY)



すでに Seedkeeper をお持ちの方は、このステップを飛ばしてステップ 4 に進んでください。このセクションでは、空のスマートカードにSeedkeeperアプレットをインストールする方法を説明します（DIYの方法）。



まず、SeedSignerの「ツール > スマートカードツール」メニューを開いてください。



![Image](assets/fr/10.webp)



次に`DIY Tools > Install Applet`を選択する。



![Image](assets/fr/11.webp)



スマートカードをチップを下向きにしてSeedSignerリーダーに挿入し、`SeedKeeper`アプレットを選択します。



![Image](assets/fr/12.webp)



インストールには数十秒かかることがあります。



![Image](assets/fr/13.webp)



アプレットが正常にインストールされたら、ステップ4に進むことができます。



![Image](assets/fr/14.webp)



## 4.既存のSeedQRをSeedkeeperに保存する



![video](https://youtu.be/X-vmFHU9Ec8)



Bitcoin、Wallet、Mnemonicをスマートカードに保存します。まず、通常通りSeedSignerの電源を入れ、Walletの*SeedQR*をスキャンしてデバイスに読み込みます。seedがインポートされたら、`Done`を選択するだけです。



![Image](assets/fr/15.webp)



seedがロードされたら、`Backup seed` メニューにアクセスしてください。



![Image](assets/fr/16.webp)



次に、SeedKeeperをSeedSignerのドライブに挿入し、「To SeedKeeper」オプションを選択します。



![Image](assets/fr/17.webp)



その後、PINコードの入力を求められます。これは空白のカードですので、コードはまだ定義されていません。このステップをスキップする場合は、任意のコードを入力してください。



![Image](assets/fr/18.webp)



SeedSignerは、Seedkeeperがまだ初期化されていない（パスワードが設定されていない）ことを検知します。I Understand`をクリックしてください。



![Image](assets/fr/19.webp)



シードキーパーの新しいPINコードを4文字から16文字の間で選んでください。Mnemonicフレーズへの物理的なアクセスを保護する唯一の障壁です。



この暗証番号は、作成後すぐに、信頼できるパスワード・マネージャに保存するか、あるいは、あなたの戦略に応じて別の物理的な媒体に保存することを忘れないでください。後者の場合、暗証番号の入った媒体は決してシードキーパーと同じ場所に置かないようにしてください。バックアップを取ることが重要です： **この暗証番号がないと seed にアクセスできず、ビットコインは失われます**。



![Image](assets/fr/20.webp)



その際、Mnemonic フレーズに関連付けて `ラベル` を定義することができる。このラベルは、Seedkeeper に複数の秘密を保存している場合に便利です。



![Image](assets/fr/21.webp)



Mnemonicフレーズがスマートカードに保存されました。



![Image](assets/fr/22.webp)



セキュリティー戦略に関しては、あなたのニーズとリスク・エクスポージャーのレベルに応じて、いくつかのアプローチが可能です。個人的には、seedのコピーを少なくとも2部保管することをお勧めする：




- これは、住所の確認や取引の署名など、日常的な操作のために簡単にアクセスできるようにしておくことができるスマートカードにとっては初めてのことです。この方法は（第5回で説明するように）実用的であり、PINコードによる保護のおかげで安全性が保たれているため、大きなリスクを負うことなくアクセスできる；
- 暗号化されていない Mnemonic フレーズのセカンドコピーで、Seedkeeper を紛失または盗難された場合にのみ使用する、ポートフォリオの究極のバックアップです。このバージョンは暗号化されていないため、2つのバックアップの同時漏洩を防ぐため、より安全な別の場所に保管する必要があります。



保護戦略やリスクプロファイルによっては、seedを複数の異なるSeedkeeperに複製したり、Mnemonicの物理的コピーを複数作成することもできます。これらの方法については、以下のチュートリアルをご覧ください：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5.シードキーパーからseedをロードする



![video](https://youtu.be/ms0Iq_IyaoE)



MnemonicのフレーズをSeedSignerに読み込ませ、Bitcoinのトランザクションに署名することができます。まず、SeedSignerの電源を入れ、`Seeds`メニューを開きます。



![Image](assets/fr/23.webp)



次に、`From SeedKeeper` オプションを選択する。



![Image](assets/fr/24.webp)



シードキーパーをスマートカードリーダーに挿入し、PINコードを入力してロックを解除してください。右下の確認ボタン「KEY3」を押して入力を確認してください。



![Image](assets/fr/25.webp)



Seedkeeper には複数の秘密鍵が格納されていることがあるので、SeedSigner は読み込む秘密鍵の選択を促します。表示されるラベルは、ステップ4で定義した名前に対応しています。私の場合のように、seedを1つしか登録していない場合は、1つの選択肢しか表示されません。



![Image](assets/fr/26.webp)



これで seed がロードされました。画面に表示されるフィンガープリントと Sparrow wallet の設定で指定されたフィンガープリントを比較して、これが正しい Wallet であることを確認してください。このフィンガープリントは、Walletを最初に作成したときにも提供されました。



passphraseを使用している場合は、この段階で適用することができます（このチュートリアルのパート6を参照してください）。そうでなければ、単に`Done`をクリックしてください。



![Image](assets/fr/27.webp)



Walletでは、従来のSeedSignerと同じように、お届け先の確認やお取引のサインを行うことができます。使い方の詳細については、専用チュートリアルをご覧ください：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6.passphrase BIP39でSeedkeeperを使用する



Bitcoinのポートフォリオを保護するためにpassphraseをお使いですか？seedと一緒にシードキーパーに登録することもできます。このソリューションにより、passphraseを使用するたびに手動で小さなキーパッドに入力することなく、Walletを素早くシードシグナーにロードすることができます。



この方法は、passphraseのセキュリティ上の利点を享受しながら、日常的な使用に伴う制約をなくすことができるので、特に面白いと思います。以下は、私が推奨するコンフィギュレーションの例である：




- seedとpassphraseは、強力なPINコードで保護されたSeedkeeperに保管してください（これは重要です）。このバックアップにより、Walletを日常的に簡単に使用できるようになります。ご希望であれば、この情報を2つ目のシードキーパーに複製することもできます；
- また、Mnemonic と passphrase の明確なコピーを紙または金属で保管してください。これは、シードキーパーやその暗証番号を紛失した場合の最後のバックアップです。これらのコピーは同時に漏洩しないよう、必ず別々の場所に保管してください。



この構成では、もし誰かがあなたの平文Mnemonicだけを手に入れたとしても、passphraseを知らなければ何も盗むことはできない（もちろん、ブルートフォース攻撃に耐えられるだけの強度があればの話だが）。逆に、誰かがあなたの平文passphraseを発見しても、対応するMnemonicフレーズがなければ使えないままである。



最後に、誰かがseedとpassphraseの入ったシードキーパーに物理的にアクセスすることに成功しても、PINコードを知らなければ何も引き出すことはできません。passphraseとは異なり、このコードはブルートフォースできません。スマートカードは5回無効な試行をすると自動的にロックされるからです。



したがって、この構成の安全性は2つの重要なポイントに基づいている：




- passphrasestrong**：長く、ランダムで、様々な文字が含まれていなければならない。初期化時にキーボードから一度入力するだけで、その後はSeedkeeperから送信されるので、その複雑さは問題ではない；
- シードキーパーの**強力なPINコード**：これもランダムで16文字からなる。



このセットアップを行うには、まずpassphraseを通常の方法でSeedSignerにロードします。このチュートリアルの手順に従ってください：



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

passphraseを使用したポートフォリオがSeedSignerに正しくロードされたら、`Seeds`メニューを開き、このポートフォリオに対応するフットプリントを選択します。このフットプリントはpassphraseを使用しないポートフォリオのフットプリントとは異なりますのでご注意ください。



![Image](assets/fr/28.webp)



次に`Backup seed`をクリックし、SeedKeeperをドライブに挿入し、`To SeedKeeper`を選択する。



![Image](assets/fr/29.webp)



PINを入力してSeedkeeperのロックを解除し、このシークレットにラベルを割り当てます。ある種のもっともらしい否認性を維持するために指紋をラベルとして残すこともできるし、例えば`passphrase Wallet`と明示することもできる。



![Image](assets/fr/30.webp)



あなたの passphrase ポートフォリオがシードキーパーに登録されました。



![Image](assets/fr/31.webp)



次に起動したら、シードキーパーをドライブに挿入し、「Seeds > From SeedKeeper」に移動するだけです。



![Image](assets/fr/32.webp)



PINコードを入力してスマートカードのロックを解除し、passphraseに対応するWalletを選択します。



![Image](assets/fr/33.webp)



passphraseとWalletの刻印を確認し、確認する。



![Image](assets/fr/34.webp)



passphraseでポートフォリオにアクセスし、SeedSignerで通常行うように取引に署名することができます。



## 7.追加オプション



ツール > スマートカードツール」メニューの中に、Seedkeeperを管理するためのいくつかのオプションがあります：





- 共通ツール」メニューでは、：
 - カードの真偽を確認する；
 - PINコードの変更；
 - 秘密に関連付けられているラベルを変更します；
 - NFC機能を無効にする（チップリーダーのみを使用する場合に推奨）；
 - ファクトリーリセットを実行する。





- SeedKeeperの機能」メニューでは、：
 - 登録された秘密のリストを参照してください；
 - 新しい秘密を保存する；
 - 既存の秘密を削除する；
 - ディスクリプターを保存またはロードする（Multisigポートフォリオに便利な機能）。





- DIYツール」メニューでは、：
 - Seedkeeperアプレットのコンパイル ；
 - アプレットを空のカードにインストールする；
 - Seedkeeperアプレットを削除すると、リセットされ、再び空白になります。



SeedSignerと組み合わせてポートフォリオを安全にバックアップするSeedkeeperの使い方はお分かりいただけたでしょうか。



この設定に納得したなら、それを可能にするプロジェクトを支援することをためらわないでほしい：




- サトチップウェブサイト](https://satochip.io/shop/)から直接ご購入いただけます；
- SeedSignerプロジェクトに寄付する](https://seedsigner.com/donate/)；
- Crypto GuideのYouTubeチャンネル](https://www.youtube.com/@CryptoGuide/)を購読することで、修正されたファームウェアをホストしているGitHubリポジトリを管理している人物によって運営されている。