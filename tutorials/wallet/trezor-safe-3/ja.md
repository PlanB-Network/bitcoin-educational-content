---
name: Trezor Safe 3
description: Hardware Walletセーフ3の設定と使用
---
![cover](assets/cover.webp)



*画像引用：[Trezor.io](https://trezor.io/)*



Trezor Safe 3は、2023年にSatoshiLabsによってデザインされたHardware Walletです。初心者から中級者まで使えるように設計された、非常にコンパクトで軽量なモデル（14グラム）です。有名なModel Oneの後継機であり、主要な競合機であるLedgerとは一線を画すブランドのオープンソースアプローチを維持しつつ、大幅な機能追加が施されている。Safe 3の価格は79ユーロ。そのため、Hardware Walletのミッドレンジ・セグメントに位置づけられ、Ledger Nano S Plusと直接競合する。



Safe 3はバッテリーを持たず、USB-C接続のみで動作し、電源と通信の両方に使用される。0.96インチの小型モノクロOLEDディスプレイと2つの物理ボタンが特徴だ。



![Image](assets/fr/01.webp)



Safe 3は、passphrase BIP39の優れた統合を含め、優れたHardware Walletに期待されるすべての必須機能を提供する。しかし、まだMiniscriptをサポートしていない。



このモデルは特に初心者に適しており、私が初めて使う人に薦めるHardware Walletかもしれない。また、中級者にも適している。一方で、Coldcardのようなデバイスに搭載されている、より特殊な機能を求める上級ユーザーの期待には応えられないかもしれない。とはいえ、このような高度なオプションを必要としないのであれば、Trezor Safe 3は優れた選択肢かもしれない。



## トレザー・セーフ3安全モデル



これは OPTIGA Trust M V3 チップであり、seed を直接保存するのではなく、seed へのアクセ スを保護する暗号コンポーネントとして機能します。セキュア・エレメントは、ユーザーがPINを正しく入力した場合にのみアクセスできる秘密を保持する。この秘密は、デバイスのメイン・メモリーに暗号化されて保存されているseedを復号化するために使用される。



このハイブリッド・セキュリティ・システムは、特に、モデル・ワンが特に暗証番号管理で陥りがちであった、抜き取り攻撃や侵入分析に対する物理的な保護が向上している。セキュア・エレメントを使用することで、これらの脆弱性は回避されている。このモデルはまた、オープンソースのソフトウェア・アーキテクチャを維持している。秘密鍵の生成と使用を管理するコードは、完全にアクセス可能で検証可能なままである。OPTIGAチップは、Bitcoin Wallet鍵管理の外部要素であるPINコードのみを管理する。OPTIGAチップは、seedの復号化に使用できる秘密鍵のみを公開する。また、OPTIGA Trust M V3チップは比較的自由なライセンスの恩恵を受けており、SatoshiLabsは潜在的な脆弱性を自由に公表することができます。



このセキュリティー・モデルは、現在市販されているものの中で最も優れた妥協点のひとつだと私は考えている。セキュアエレメントの利点とオープンソースのソフトウェア管理が組み合わされている。以前は、ユーザーはチップによる物理的セキュリティの強化とオープンソースによる透明性のどちらかを選択しなければなりませんでしたが、Trezor Safe 3では、両方のメリットを享受することが可能です。



このチュートリアルでは、Trezor Safe 3 を安全に設定し、使用する方法を説明します。



## Trezor Safe 3を開封



Safe 3 がお手元に届きましたら、箱と Seal が無傷であることを確認し、パッケージが開封されていないことを確認してください。後日、セットアップ時にソフトウェアによるデバイスの真正性と完全性の確認も行われます。



箱の中身は以下の通り：




- トレザー・セーフ 3；
- Mnemonicのフレーズを記録するためのカードストック、ステッカー、説明書が入ったポーチ；
- USB-C - USB-Cケーブル。



![Image](assets/fr/02.webp)



開封すると、Trezor Safe 3は保護プラスチックで保護され、USB-CポートはホログラムSealで固定されているはずです。それがそこにあることを確認してください。



![Image](assets/fr/03.webp)



右ボタンで右に、左ボタンで左にスクロールします。アクションを確定するには、両方のボタンを同時に押します。



![Image](assets/fr/04.webp)



## 前提条件



このチュートリアルでは、Trezor Safe 3 と[Sparrow Wallet ポートフォリオ管理ソフトウェア](https://sparrowwallet.com/download/) の使い方を紹介します。このソフトウェアをまだインストールしていない場合は、今すぐインストールしてください。また、Sparrow Wallet の設定に関する詳細なチュートリアルもご用意しております：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

また、Safe 3の設定、真正性の確認、ファームウェアのインストールには、Trezor Suiteソフトウェアが必要です。このソフトウェアはそのためだけに使用し、その後はファームウェアのアップデートのためだけに必要です。Walletの日常的な管理には、Bitcoinに最適化され、初心者でも使いやすいSparrow Walletを独占的に使用します（SparrowはBitcoinのみをサポートし、アルトコインはサポートしません）。



[公式サイトからTrezor Suiteをダウンロード](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



これらのプログラムについては、あなたのマシンにインストールする前に、（GnuPGで）その真正性と（Hashで）その完全性の両方をチェックすることを強くお勧めします。この方法がわからない場合は、こちらのチュートリアルを参考にしてください：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3の起動



Trezor Suite と Sparrow Wallet がインストールされているコンピュータに Safe 3 を接続します。



![Image](assets/fr/06.webp)



Trezor Suiteを開き、"*Set up my Trezor*"をクリックします。



![Image](assets/fr/07.webp)



Bitcoin専用ファームウェア」を選択し、「**Bitcoin専用**をインストール」をクリックします。



![Image](assets/fr/08.webp)



その後、Trezor Suite が Safe 3 にファームウェアをインストールします。インストール中はしばらくお待ちください。



![Image](assets/fr/09.webp)



Continue*"をクリックする。



![Image](assets/fr/10.webp)



そして、あなたのHardware Walletが偽物でないこと、あるいは危険にさらされていないことを確認するために、真正性テストに進む。



![Image](assets/fr/11.webp)



Safe 3 で右ボタンを押して確定します。



![Image](assets/fr/12.webp)



Trezorが本物であれば、Trezor Suiteに確認メッセージが表示されます。



![Image](assets/fr/13.webp)



そうすれば、基本的な操作方法が書かれたウィンドウをスキップすることができる。



![Image](assets/fr/14.webp)



## Bitcoinポートフォリオの作成



Trezor Suite上で、「*新しいWalletを作成*」ボタンをクリックします。



![Image](assets/fr/15.webp)



標準的なポートフォリオの場合、デフォルトのバックアップタイプを選ぶことができます。これは12語のMnemonicフレーズを持つ古典的なシングルシグナルのポートフォリオを作成します。Wallet*を作成」をクリックしてください。



マルチシェアバックアップ*を含む、Trezorで利用可能なその他のバックアップオプションについて詳しく知りたい場合は、こちらのチュートリアルも参考にされることをお勧めします：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Hardware Walletの利用規約に同意する。



![Image](assets/fr/17.webp)



もう一度右ボタンを押すと、新しいポートフォリオが作成されます。



![Image](assets/fr/18.webp)



Trezor Suiteで "*Continue to backup*"をクリックします。



![Image](assets/fr/19.webp)



このソフトウェアには、Mnemonicフレーズの管理方法が記載されています。



このMnemonicは、あなたのすべてのビットコインに完全かつ無制限にアクセスできるようにします。このフレーズを持っていれば、Trezor Safe 3に物理的にアクセスできなくても、誰でもあなたの資金を盗むことができます。



この12単語のフレーズは、Hardware Walletの紛失、盗難、破損の際にビットコインへのアクセスを回復します。そのため、大切に保存し、安全な場所に保管することが非常に重要です。



箱の中に入っている厚紙に書いてもいいし、火災や水害、倒壊から守るために、ステンレス製の台座に刻印するのもおすすめだ。



指示を確認し、「*Walletバックアップを作成*」ボタンをクリックします。



![Image](assets/fr/20.webp)



Safe 3 は、乱数ジェネレーターを使用して Mnemonic フレーズを作成します。この操作の間、あなたが監視されていないことを確認してください。画面に表示された言葉を、お好きな物理的媒体に書き留めてください。あなたのセキュリティ戦略によっては、フレーズの完全な物理的コピーを複数作成することを検討してもよいでしょう（ただし、何よりも分割しないでください）。単語には番号をつけ、順番に並べることが重要である。



**このチュートリアルで私がしているように、インターネット上でこれらの言葉を決して共有してはならない。この例のWalletはTestnetでのみ使用し、チュートリアルの最後に削除します。**



Mnemonicのフレーズを保存・管理する適切な方法については、特に初心者の方には、こちらのチュートリアルをご覧になることを強くお勧めします：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



次の単語に進むには、右クリックします。左ボタンをクリックすると前に戻ることができます。すべての単語を書き終えたら、右ボタンを押したまま次のステップに進みます。



![Image](assets/fr/22.webp)



Mnemonic フレーズの単語を順番に従って選択し、正しく書き込まれていることを確認します。左右のボタンで候補を移動し、2つのボタンを同時にクリックして正しい単語を選びます。



![Image](assets/fr/23.webp)



この確認手続きが完了したら、右のボタンをクリックしてください。



![Image](assets/fr/24.webp)



## PINコードの設定



次にPINコードのステップです。PINコードはTrezorのロックを解除します。そのため、不正な物理的アクセスから保護されます。このPINコードはWalletの暗号キーの導出には関与しません。したがって、PIN コードにアクセスできなくても、12 ワードの Mnemonic フレーズを持っていれば、ビットコインへのアクセスを取り戻すことができます。



Trezor Suiteで "*Continue to PIN*"をクリックし、"*Set PIN*"ボタンをクリックします。



![Image](assets/fr/25.webp)



セーフ 3 で確認する。



![Image](assets/fr/26.webp)



できるだけランダムなPINコードを選択することをお勧めします。このコードは、Trezor が保存されている場所とは別の場所に保存してください (パスワードマネージャなど)。PINコードは8桁から50桁の間で定義できます。セキュリティ強化のため、できるだけ長いPINコードを選択することをお勧めします。



左右のボタンで各桁を選択します。選択を確定して次の桁に進むには、両方のボタンを同時に押します。



![Image](assets/fr/27.webp)



完了したら、桁の頭にある「*ENTER*」チェックマークをクリックし、2回目の暗証番号の確認を行います。



![Image](assets/fr/28.webp)



PINコードが登録されました。



![Image](assets/fr/29.webp)



Trezor Suite上で "*Complete setup*"ボタンをクリックします。



![Image](assets/fr/30.webp)



これで Safe 3 の設定は完了です。必要に応じて、Hardware Wallet の名前とホームページを変更できます。



![Image](assets/fr/31.webp)



Hardware Walletの定期的なファームウェアアップデートや、リカバリーテストを行う場合を除き、Trezor Suiteソフトウェアはもう必要ありません。このソフトウェアはBitcoinのみの使用に完璧に適しているため、ポートフォリオの管理にはSparrowを使用することにする。



## Sparrow Walletでのポートフォリオの設定



Sparrow Wallet [公式ウェブサイトから](https://sparrowwallet.com/)をコンピューターにダウンロードし、インストールすることから始めましょう。



Sparrow Walletを開いたら、ソフトウェアがBitcoinノードに接続されていることを確認してください。Bitcoinノードは、Interfaceの右下隅にあるチェックマークで示されています。Sparrowの接続に問題がある場合は、このチュートリアルの冒頭を読むことをお勧めします：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

**File**タブをクリックし、**New Wallet**をクリックする。



![Image](assets/fr/32.webp)



ポートフォリオに名前を付け、"*Create Wallet*"をクリックします。



![Image](assets/fr/33.webp)



スクリプトの種類*」ドロップダウンメニューで、ビットコインのセキュリティに使用するスクリプトの種類を選択します。私は "*Taproot*"、または失敗した場合は "*Native SegWit*"をお勧めします。



![Image](assets/fr/34.webp)



Connected Hardware Wallet*」ボタンをクリックします。Safe 3 がコンピュータに接続され、ロックが解除されている必要があります。



![Image](assets/fr/35.webp)



スキャン*」ボタンをクリックします。Safe 3 が表示されます。キーストアのインポート*」をクリックします。



![Image](assets/fr/36.webp)



最初のアカウントの拡張公開鍵を含む、Walletの詳細が表示されます。**Apply**」ボタンをクリックすると、Walletの作成が完了します。



![Image](assets/fr/37.webp)



Sparrow Walletへのアクセスを保護するために、強力なパスワードを選択してください。このパスワードにより、Sparrow Walletデータへの安全なアクセスが保証され、公開鍵、住所、ラベル、取引履歴が不正アクセスから保護されます。



このパスワードを忘れないように、パスワード・マネージャーに保存しておくことをお勧めする。



![Image](assets/fr/38.webp)



そして今、あなたのポートフォリオはSparrow Walletにインポートされた！



![Image](assets/fr/39.webp)



Walletで最初のビットコインを受け取る前に、**空のリカバリーテスト**を行うことを強くお勧めします。Walletの中身が空の状態で、Trezor Safe 3をリセットしてください。その後、紙のバックアップを使ってTrezorでWalletを復元してみてください。リストア後に生成されたxpubが最初にメモしたものと一致しているか確認してください。もし一致していれば、紙のバックアップが信頼できるものであることが確認できます。



リカバリーテストの方法については、こちらのチュートリアルを参照されたい：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Trezor Safe 3 でビットコインを受け取るにはどうすればよいですか？



Sparrowで「*受信*」タブをクリックする。



![Image](assets/fr/40.webp)



Sparrow Walletが提案するAddressを使用する前に、Trezorの画面で確認してください。これにより、Sparrowに表示されているAddressが詐欺でないこと、そしてAddressで確保したビットコインを使用するために必要な秘密鍵がHardware Walletにあることを確認することができます。これにより、いくつかの攻撃を回避することができます。



このチェックを行うには、"*Display Address*"ボタンをクリックする。



![Image](assets/fr/41.webp)



Trezorに表示されているAddressとSparrow Walletに表示されているAddressが一致しているか確認してください。また、Addressの有効性を確認するために、送信者にAddressを伝える直前にこのチェックを行うことをお勧めします。ボタンで確認できます。



![Image](assets/fr/42.webp)



そして、このAddressで確保されるビットコインのソースを記述するために、"*Label*"を追加することができます。これはUTXOをより良く管理するための良い方法です。



![Image](assets/fr/43.webp)



このAddressを使ってビットコインを受け取ることができる。



![Image](assets/fr/44.webp)



## Trezor Safe 3を使ってビットコインを送金する方法は？



セーフ3セキュアWalletで最初のSatsを受け取ったので、あなたもそれを使うことができます！Trezorをコンピュータに接続し、PINコードでロックを解除してSparrow Walletを起動し、「*送信*」タブで新しいトランザクションを構築します。



![Image](assets/fr/45.webp)



Coinコントロール*、つまり取引で消費するUTXOを具体的に選択したい場合は、「*UTXOs*」タブに進みます。消費したいUTXOを選択し、"*Send Selected*"をクリックしてください。Send*"タブの同じ画面にリダイレクトされますが、取引に使用するUTXOはすでに選択されています。



![Image](assets/fr/46.webp)



宛先Addressを入力します。また、「*+追加*」ボタンをクリックすると、複数のアドレスを入力できます。



![Image](assets/fr/47.webp)



この出費の目的を忘れないように「*ラベル*」を書きましょう。



![Image](assets/fr/48.webp)



このAddressに送る金額を選択する。



![Image](assets/fr/49.webp)



その時々の市場に応じて、取引の手数料率を調整してください。例えば、[Mempool.space](https://Mempool.space/)を利用して、適切な手数料レートを選択することができます。



取引パラメータがすべて正しいことを確認し、"*Create Transaction*"をクリックします。



![Image](assets/fr/50.webp)



問題がなければ、「*Finalize Transaction for Signing*」をクリックしてください。



![Image](assets/fr/51.webp)



サイン*」をクリックする。



![Image](assets/fr/52.webp)



Trezor Safe 3 の横にある「*Sign*」をクリックします。



![Image](assets/fr/53.webp)



Hardware Walletの画面で、受取人の受信Address、送金額、請求額などの取引パラメータを確認してください。Trezorで取引が確認されたら、両方のボタンを同時にクリックして署名します。



![Image](assets/fr/54.webp)



これであなたの取引は署名されました。最後にもう一度問題がないことを確認し、"*Broadcast Transaction*"をクリックしてBitcoinネットワークにブロードキャストしてください。



![Image](assets/fr/55.webp)



Sparrow Walletの "*Transactions*"タブにあります。



![Image](assets/fr/56.webp)



スパローWalletとトレザーセーフ3の基本的な使い方はご理解いただけたと思います！さらに一歩進んで、Hardware Wallet Trezorとpassphrase BIP39の組み合わせで安全性を高めるための包括的なチュートリアルをお勧めします：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

このチュートリアルが役に立ったと思ったら、以下にGreenの親指を残していただけるとありがたい。この記事をあなたのソーシャルネットワークでシェアしてください。ありがとうございました！