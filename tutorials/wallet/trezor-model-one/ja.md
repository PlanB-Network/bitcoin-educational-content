---
name: トレザー・モデル・ワン
description: Hardware Wallet Model Oneのセットアップと使用方法
---
![cover](assets/cover.webp)



*画像引用：[Trezor.io](https://trezor.io/)*



Trezor Model Oneは、SatoshiLabsが2014年に発売した最初のHardware Walletである。発売から10年以上経った今でも、特に技術的にも予算的にも手に入れやすいHardware Walletを探しているユーザーにとっては興味深い選択肢である。実際、Trezorの公式サイトでの価格は49ユーロだ。この価格帯では唯一のハードウェア・ウォレットのひとつだ。スクリーンがないことが多いTapsignerのような20ユーロ前後のエントリーレベルのデバイスと、Ledger Nano S PlusやTrezor Safe 3のような80ユーロ前後のミドルレンジのデバイスの中間に位置する。



Model Oneは、0.96インチのモノクロOLEDディスプレイと2つの物理ボタンを備えている。バッテリーなしで動作し、電源とデータExchangeにはマイクロUSB接続のみを使用する。



![Image](assets/fr/01.webp)



モデル・ワンの主な欠点は、セキュア・エレメントを搭載していないため、さまざまな物理的攻撃に対して脆弱であることである。これらの攻撃には、デバイスの PIN を特定するための補助チャネルの解析や、後でブルートフォースするために暗号化された seed を抽出する、より高度な技術が含まれる。これらの攻撃は、デバイスへの物理的なアクセスを必要とすることに注意してください。しかし、この脆弱性は、強固なpassphrase BIP39を使用することでかなり減らすことができます。もしこのHardware Walletを選ぶのであれば、passphraseを設定することを強く勧める。



モデル・ワンには2つの重要な利点がある：




- 完全にオープンソースのアーキテクチャに基づいている。セキュア・エレメントを搭載した最近のモデルとは異なり、モデル・ワンのハードウェアとソフトウェアのコンポーネントはすべて監査可能である；
- スクリーンが付いている。私の知る限り、この価格帯のHardware Walletでディスプレイが付いているのはこれだけだ。これは非常に重要な機能で、署名された情報や受信アドレスを確認できるため、多くのデジタル攻撃を防ぐことができる。



したがって、Trezor Model Oneは、予算が限られている初心者や中級者にとっては賢明な選択かもしれない。ただし、セキュアエレメントを搭載していないため、物理的な保護機能には限界があることを認識しておく必要がある。予算が限られているのであれば、これは良い選択肢だが、79ユーロのTrezor Safe 3のような優れたモデルを選ぶ余裕があるのであれば、セキュアエレメントを搭載しているこちらの方が望ましい。



## Trezor Model Oneを開封



Model Oneがお手元に届きましたら、箱とSealが揃っていることを確認し、未開封であることをご確認ください。また、後日セットアップの際に、ソフトウェアによるデバイスの真正性と完全性の確認が行われます。



箱の中身は以下の通り：




- トレザー・モデル・ワン；
- Mnemonicのフレーズを記録するためのカードストック、ステッカー、説明書；
- USB-A-マイクロUSBケーブル。



![Image](assets/fr/02.webp)



デバイスの操作はとても簡単だ：




- 右クリックして確認し、次のステップに進みます；
- 左ボタンで戻る。



## 前提条件



今回のチュートリアルでは、Trezor Model Oneと[Sparrow Wallet portfolio management software](https://sparrowwallet.com/download/)の使い方をご紹介します。このソフトウェアをまだインストールしていない場合は、今すぐインストールしてください。また、Sparrow Walletの設定に関する詳細なチュートリアルもご用意しております：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

また、Model Oneの設定、真正性の確認、ファームウェアのインストールには、Trezor Suiteソフトウェアが必要です。このソフトウェアはそのためだけに使用し、その後はファームウェアのアップデートのためだけに必要となります。Walletの日々の管理には、Bitcoin用に最適化され、初心者でも使いやすいSparrow Walletを独占的に使用する予定だ（SparrowはBitcoinのみをサポートし、アルトコインはサポートしない）。



[公式サイトからTrezor Suiteをダウンロード](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



これらのプログラムについては、あなたのマシンにインストールする前に、（GnuPGで）その真正性と（Hashで）その完全性の両方をチェックすることを強くお勧めします。この方法がわからない場合は、このチュートリアルに従ってください：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezorモデル・ワンの始動



Trezor SuiteとSparrow WalletがインストールされているコンピュータにModel Oneを接続します。



![Image](assets/fr/04.webp)



Trezor Suiteを開き、"*Set up my Trezor*"をクリックします。



![Image](assets/fr/05.webp)



Bitcoin専用ファームウェア*」を選択し、「*Bitcoin専用*のインストール」をクリックします。



![Image](assets/fr/06.webp)



その後、Trezor SuiteがModel Oneにファームウェアをインストールします。インストール中はしばらくお待ちください。



![Image](assets/fr/07.webp)



Continue*」をクリックする。



![Image](assets/fr/08.webp)



## Bitcoinポートフォリオの作成



Trezor Suite上で、「*新しいWalletを作成*」ボタンをクリックします。



![Image](assets/fr/09.webp)



Hardware Walletの利用規約に同意する。



![Image](assets/fr/10.webp)



Trezor Suiteで "*Continue to backup*"をクリックします。



![Image](assets/fr/11.webp)



このソフトウェアは、Mnemonicフレーズの管理方法を説明します。



このMnemonicは、あなたのすべてのビットコインに完全かつ無制限にアクセスできるようにします。このフレーズを持っていれば、Trezor Model Oneに物理的にアクセスできなくても、誰でもあなたの資金を盗むことができます。



Hardware Walletを紛失、盗難、破損した場合、24語のフレーズでビットコインへのアクセスを回復します。そのため、大切に保存し、安全な場所に保管することが非常に重要です。



箱の中に入っている厚紙に書いてもいいし、火災や水害、倒壊から守るために、ステンレス製の台座に刻印するのもおすすめだ。



指示を確認し、「*Walletバックアップを作成*」ボタンをクリックします。



![Image](assets/fr/12.webp)



Model Oneは、乱数ジェネレーターを使ってあなたのMnemonicフレーズを作成します。この操作の間、あなたが監視されていないことを確認してください。スクリーンに表示されたフレーズをお好きな物理媒体に書き留めてください。あなたのセキュリティ戦略によっては、フレーズの完全な物理的コピーを複数作成することを検討してもよい（ただし、何よりも分割しないこと）。単語には番号をつけ、順番に並べることが重要である。



***このチュートリアルで私がしているように、インターネット上でこれらの言葉を決して共有してはなりません。この例のWalletはTestnetでのみ使用され、チュートリアルの最後に削除されます。



Mnemonicのフレーズを保存・管理する適切な方法については、特に初心者の方には、こちらのチュートリアルをご覧になることを強くお勧めします：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

次の単語に移るには、右クリックします。すべての単語を書き終えたら、次のステップに進むためにもう一度右ボタンをクリックします。



![Image](assets/fr/13.webp)



あなたのHardware Walletは再び、あなたのすべての言葉を表示します。すべて書き留めたか確認してください。



![Image](assets/fr/14.webp)



## PINコードの設定



次にPINコードのステップです。PINコードはTrezorのロックを解除します。そのため、不正な物理的アクセスから保護されます。この PIN コードは、Wallet の暗号キーの導出には関与しません。そのため、PIN コードにアクセスできなくても、12 ワードの Mnemonic フレーズを持っていれば、ビットコインへのアクセスを取り戻すことができます。



Trezor Suiteで "*Continue to PIN*"をクリックし、"*Set PIN*"ボタンをクリックします。



![Image](assets/fr/15.webp)



モデル・ワンで確認する。



![Image](assets/fr/16.webp)



できるだけランダムなPINコードを選択することをお勧めします。このコードは、Trezor が保存されている場所とは別の場所に保存してください (パスワードマネージャなど)。PINコードは8桁から50桁の間で定義できます。セキュリティ強化のため、できるだけ長いPINコードを選択することをお勧めします。



PINコードは、Trezor Model Oneに表示されるキーボード構成に従って、数字に対応するドットをクリックして、コンピュータ上のTrezor Suiteに入力する必要があります。



この特定のPIN入力方法は、Trezor Suite経由でもSparrow Wallet経由でも、Trezor Model Oneのロックを解除するたびに必要となります。



![Image](assets/fr/17.webp)



入力が終わったら、"*Enter PIN*"ボタンをクリックしてください。



![Image](assets/fr/18.webp)



確認のため、もう一度暗証番号を入力してください。



![Image](assets/fr/19.webp)



Trezor Suite上で "*Complete setup*"ボタンをクリックします。



![Image](assets/fr/20.webp)



これでModel Oneの設定は完了です。ご希望であれば、Hardware Walletの名前やホームページを変更することができます。



![Image](assets/fr/21.webp)



Hardware Walletの定期的なファームウェアアップデートや、リカバリーテストを行う場合を除き、Trezor Suiteソフトウェアはもう必要ありません。このソフトウェアはBitcoinのみの使用に最適なので、ポートフォリオの管理にはSparrowを使用することにします。



## Sparrow Walletでのポートフォリオの設定



Sparrow Wallet [公式ウェブサイトから](https://sparrowwallet.com/)をダウンロードし、コンピュータにインストールすることから始めましょう。



Sparrow Walletを開いたら、ソフトウェアがBitcoinノードに接続されていることを確認してください。Bitcoinノードは、Interfaceの右下にあるチェックで示されています。Sparrowの接続に問題がある場合は、このチュートリアルの冒頭を参照することをお勧めします：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

File*"タブをクリックし、"*New Wallet*"をクリックする。



![Image](assets/fr/22.webp)



ポートフォリオに名前を付け、「*Wallet*を作成」をクリックする。



![Image](assets/fr/23.webp)



スクリプトの種類*」ドロップダウンメニューで、ビットコインのセキュリティに使用するスクリプトの種類を選択します。私は "*Taproot*"、または失敗した場合は "*Native SegWit*"をお勧めします。



![Image](assets/fr/24.webp)



接続されたHardware Wallet*」ボタンをクリックします。もちろん、Model Oneがコンピュータに接続されている必要があります。



![Image](assets/fr/25.webp)



スキャン*」ボタンをクリックしてください。あなたのモデル・ワンが表示されるはずです。



Sparrow Walletを開いた状態でModel Oneをコンピュータに接続すると、Sparrow上でpassphrase BIP39を入力するよう促されます。この高度なオプションについては、今後のチュートリアルで取り上げます。今のところ、"*Toggle passphrase Off*"を選択するだけで、Trezorを起動するたびにpassphraseの入力を促されるのを防ぐことができます。



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



インポート・キーストア*」をクリックする。



![Image](assets/fr/27.webp)



最初のアカウントの拡張公開鍵を含む、Walletの詳細が表示されます。Apply*」ボタンをクリックして、Walletの作成を完了します。



![Image](assets/fr/28.webp)



Sparrow Walletへのアクセスを保護するために、強力なパスワードを選択してください。このパスワードは、お客様のSparrow Walletデータへの安全なアクセスを保証し、お客様の公開鍵、住所、ラベル、取引履歴を不正アクセスから保護します。



このパスワードを忘れないように、パスワード・マネージャーに保存しておくことをお勧めする。



![Image](assets/fr/29.webp)



そして今、あなたのポートフォリオはSparrow Walletにインポートされました！



![Image](assets/fr/30.webp)



Walletで最初のビットコインを受け取る前に、**空のリカバリーテスト**を行うことを強くお勧めします。Walletがまだ空の状態で、Trezor Model Oneをリセットしてください。その後、紙のバックアップを使ってTrezor上でWalletを復元してみてください。リストア後に生成されたxpubが最初にメモしたものと一致しているか確認してください。もし一致していれば、紙のバックアップが信頼できるものであることが確認できます。



リカバリーテストの方法については、こちらのチュートリアルを参照されたい：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Trezor Model Oneでビットコインを受け取るには？



Sparrowで「*受信*」タブをクリックする。



![Image](assets/fr/31.webp)



Sparrow Walletが提案するAddressを使用する前に、Trezorの画面で確認してください。これにより、Sparrowに表示されたAddressが詐欺でないこと、そしてHardware WalletがこのAddressで確保したビットコインを使用するために必要な秘密鍵を確かに保持していることを確認することができます。これにより、いくつかの攻撃を回避することができます。



このチェックを行うには、"*Display Address*"ボタンをクリックする。



![Image](assets/fr/32.webp)



Trezorに表示されているAddressとSparrow Walletに表示されているWalletが一致しているか確認してください。また、Addressの有効性を確認するために、送信者にAddressを伝える直前にこのチェックを行うことをお勧めします。右のボタンで確認できます。



![Image](assets/fr/33.webp)



また、"*Label*"を追加して、このAddressで確保されるビットコインの出所を記述することもできます。これはUTXOをより良く管理するための良い方法です。



![Image](assets/fr/34.webp)



そして、このAddressを使ってビットコインを受け取ることができる。



![Image](assets/fr/35.webp)



## Trezor Model Oneでビットコインを送るには？



Model Oneで保護されたWalletに最初のSatsが届きました！Trezorをコンピュータに接続し、Sparrow Walletを起動し、"*Send*"タブで新しい取引を構築します。



![Image](assets/fr/36.webp)



Coinコントロール*、つまり取引で消費するUTXOを具体的に選択したい場合は、「*UTXOs*」タブに進みます。消費したいUTXOを選択し、"*Send Selected*"をクリックしてください。Send*"タブの同じ画面にリダイレクトされますが、取引に使用するUTXOはすでに選択されています。



![Image](assets/fr/37.webp)



宛先Addressを入力します。また、「*+追加*」ボタンをクリックすると、複数のアドレスを入力できます。



![Image](assets/fr/38.webp)



この出費の目的を忘れないように「*ラベル*」を書きましょう。



![Image](assets/fr/39.webp)



このAddressに送る金額を選択する。



![Image](assets/fr/40.webp)



その時々の市場に応じて、取引の手数料率を調整しましょう。例えば、[Mempool.space](https://Mempool.space/)を利用して、適切な手数料レートを選択することができます。



取引パラメータがすべて正しいことを確認し、"*Create Transaction*"をクリックします。



![Image](assets/fr/41.webp)



問題がなければ、「*Finalize Transaction for Signing*」をクリックしてください。



![Image](assets/fr/42.webp)



サイン*」をクリックする。



![Image](assets/fr/43.webp)



あなたのTrezor Model Oneの横にある "*Sign*"をクリックしてください。



![Image](assets/fr/44.webp)



Hardware Walletの画面で、受取人の受信Address、送金額、手数料などの取引パラメータを確認する。Trezor上で取引が確認されたら、右クリックして署名する。



![Image](assets/fr/45.webp)



これでトランザクションは署名されました。最後にもう一度問題がないことを確認し、"*Broadcast Transaction*"をクリックしてBitcoinネットワークにブロードキャストします。



![Image](assets/fr/46.webp)



Sparrow Walletの「*取引*」タブにあります。



![Image](assets/fr/47.webp)



おめでとうございます。これでスパローWalletとトレゾアモデルワンの基本的な使い方はご理解いただけたと思います！さらに一歩進めるために、Hardware Walletトレゾアとpassphrase BIP39の使い方の包括的なチュートリアルをお勧めします：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

このチュートリアルが役に立ったと思ったら、下にGreenの親指を残していただけるとありがたい。この記事をあなたのソーシャルネットワークでシェアしてください。ありがとうございました！