---
name: スズメ Wallet - Multisig
description: Sparrowでマルチシグネチャ・ポートフォリオを作成する
---
![cover](assets/cover.webp)



マルチシグネチャWallet(しばしば "*Multisig*"と呼ばれる)は、Bitcoin Wallet構造であり、支出を認可するために、異なる鍵による 複数の暗号署名を必要とする。一つの秘密鍵でUTXOのロックを解除できる従来の("*singlesig*") Walletとは異なり、Multisigは**m-of-n**モデルに基づいている。



この仕組みにより、ポートフォリオの制御を複数のエンティティやデバイス間で共有することが可能になる。例えば、2-of-3の構成では、3つの独立した鍵セットが生成されるが、資金を放出するのに必要なのは2つだけである。このアーキテクチャーは、鍵の漏洩や紛失に関連するリスクを劇的に軽減する。たった1つの鍵にアクセスできる泥棒はWalletを空にすることができず、1つを紛失したユーザーは残りの2つで資金にアクセスできる。



![Image](assets/fr/01.webp)



しかし、このセキュリティの高さには複雑さが伴う。MultisigのWalletを設定するには、複数のMnemonicフレーズ（署名要素ごとに1つ）と拡張公開鍵（"*xpub*"）を確保する必要がある。実際、Multisigの2-of-3 Walletを使用する場合、Walletを取得するためには、3つのMnemonic フレーズすべて、あるいは3つのフレーズのうち少なくとも2つを持っていなければならない。しかし、3つのフレーズのうち2つしか持っていない場合、3つの*xpubs*へのアクセスも必要であり、それなしでは、それらが保護するビットコインにアクセスするために必要な公開鍵を取り出すことは不可能である。



要約すると、Multisigポートフォリオを回復させるには、次のことが必要です：




- また、各シグネチャーファクターに関連するすべてのMnemonicフレーズにアクセスすることもできます；
- また、必要な公開鍵を取得するために、全要素のxpubにアクセスすることもできる。



![Image](assets/fr/02.webp)



このMultisigポートフォリオのバックアップ管理は、ファンドへのアクセスに必要なすべての公開データをまとめた*出力スクリプト記述子*によって容易になる。しかし、この機能はまだすべてのポートフォリオ管理ソフトウェアに実装されているわけではない。



Multisigは特に、セキュリティの強化や資金の一括管理を求めるビットコイナーに適している。企業、団体、家族、あるいはかなりの量のビットコインを保有する個人ユーザーなどである。例えば、複数の管理者やチームメンバーに署名権限を分散させるなど、分散型のガバナンススキームを構築するために使用することができます。



このチュートリアルでは、**Sparrow Wallet**を使ってクラシックなマルチシグネチャーのWalletを作成し、使用する方法を学びます。もし、タイムロック付きのカスタマイズされたマルチシグネチャーのポートフォリオを作成したい場合は、代わりにLianaを使用することをお勧めします：



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## 前提条件



今回のチュートリアルでは、[ポートフォリオ管理ソフト Sparrow Wallet](https://sparrowwallet.com/download/)を使ってMultisigを作る方法を紹介します。まだインストールしていない方は、今すぐインストールしてください。また、Sparrow Walletの設定方法についても詳しく解説しています：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

マルチシグネチャーのWalletをセットアップするには、異なるハードウェア・ウォレットが必要です。例えば、Multisigの2-de-3の場合、.NETを使用することができます：




- トレザー・モデル・ワン；
- Ledgerフレックス；
- コールドカードMK3。



![Image](assets/fr/03.webp)



Multisigのコンフィギュレーションでは、Hardware Walletのメーカーを使い分けるのがいい。特定の機種に重大な問題が発生しても、Multisig全体の安全性には影響しない。さらに、各機種特有のメリットも享受できる。例えば、私の構成では：





- Trezor Model Oneは完全にオープンソースであり、seed世代の検証が可能である。しかし、セキュア・エレメントを搭載していないため、物理的な攻撃に対して脆弱であることに変わりはない；





- 一方、Ledger Flexは、検証不可能な独自ファームウェアを採用しているが、優れた物理的保護を提供するセキュア・エレメントを内蔵している；





- Coldcardはセキュア・エレメントを搭載しており、そのコードは検索可能である。他のモデルにはない検証機能を備えているため、我々の構成には興味深い選択だ。



Multisig Wallet を設定する前に、各 Hardware Wallet が正しく設定されていることを確認してください（Mnemonic の生成と保存、暗証番号の定義）。詳細な手順については、各Hardware Walletのチュートリアルを参照してください：



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

このチュートリアルの後半で説明するように、Hardware Walletとは関係なく、秘密鍵がPCに保存されているファクターをMultisigのコンフィギュレーションに統合することも可能です。この方法は、ハードウェア・ウォレットを排他的に使用するよりも明らかに安全ではありませんが、場合によっては適切かもしれません。例えば、Multisig 2-de-3の場合、2つのハードウェア・ウォレットと1つのSoftware Walletを選択することができます。



## Multisigポートフォリオの作成



Sparrow Wallet を開き、"*File*"タブをクリックし、"*New Wallet*"を選択します。



![Image](assets/fr/04.webp)



マルチシグネチャー・ポートフォリオに名前を付け、「*Wallet*を作成」をクリックして確定します。



![Image](assets/fr/05.webp)



Policy Type*」ドロップダウンメニューで、「*Multi Signature*」オプションを選択する。



![Image](assets/fr/06.webp)



右上には、Multisigのキーの総数と、出費を承認するために必要な連帯保証人の数を定義することができます。私の例では、これは2対3のスキームである。



![Image](assets/fr/07.webp)



Sparrow Walletのウィンドウ下部には、3つの「*Keystore*」が表示されている。それぞれがキーのセットを表している。ここでは、3つのハードウェア・ポートフォリオを使っているので、それぞれの「*Keystore*」はそのうちの1つに対応している。これから設定を行います。



コールドカードから始める。キーストア1*』タブで、『*Airgapped Hardware Wallet*』オプションを選択する。



![Image](assets/fr/08.webp)



Coldcardの場合、デバイスのロックが解除されると、「*設定*」メニューから「*Multisig財布*」に進みます。



![Image](assets/fr/09.webp)



このメニューでは、コールドカードが参加しているMultisigポートフォリオを管理することができる。新規に作成したいので、"*Export XPUB*"を選択する。



![Image](assets/fr/10.webp)



アカウント番号*」フィールドについては、1つのアカウントしか管理していない場合は空白のままにしておき、確認ボタンを押して直接認証することができます。



![Image](assets/fr/11.webp)



Coldcardは、マイクロSDカードに保存されたあなたのxpubを含むファイルをgenerateします。



![Image](assets/fr/12.webp)



このマイクロSDをパソコンに挿入します。Sparrow Walletの "*Coldcard Multisig*"横の "*Import File...*"ボタンをクリックし、カード上のColdcardで作成されたファイルを選択します。



![Image](assets/fr/13.webp)



xpubは正常にインポートされました。他の2つのハードウェアウォレットでこの手順を繰り返します。



![Image](assets/fr/14.webp)



Ledger Flexでは、"*Keystore 2*"を選択し、"*Connected Hardware Wallet*"をクリックします。Ledgerがコンピューターに接続され、ロックが解除され、Bitcoinアプリケーションが開いていることを確認します。



![Image](assets/fr/15.webp)



そして「*スキャン...*」ボタンをクリックする。



![Image](assets/fr/16.webp)



ハードウェア・ポートフォリオの名前の横にある「*Import Keystore*」をクリックする。



![Image](assets/fr/17.webp)



2人目の署名者がスパロウWalletに正しく登録されました。



![Image](assets/fr/18.webp)



Trezor Oneでもまったく同じ手順を繰り返し、Multisigのコンフィギュレーションを確定する。



![Image](assets/fr/19.webp)



私の設定ではこのケースはカバーしていませんが、Multisigの中にスパロウのSoftware Wallet（Hot Wallet）を経由したサインを入れたい場合は、「*新規またはインポートされたSoftware Wallet*」ボタンをクリックするだけです。



これですべての署名デバイスがSparrow Walletにインポートされたので、"*Apply*"をクリックしてMultisigの作成を確定することができます。



![Image](assets/fr/20.webp)



Sparrow Wallet Walletへのアクセスを保護するために、強力なパスワードを選択してください。このパスワードは、あなたの公開鍵、アドレス、ラベル、取引履歴を不正アクセスから保護します。



このパスワードを紛失しないよう、パスワード・マネージャーなど安全な場所に保存することを忘れないでください。



![Image](assets/fr/21.webp)



## Multisigポートフォリオのバックアップ



出力スクリプト記述子*をコールドカードに保存し（これはMultisigにコールドカードを装着しているユーザーだけに適用されます）、何よりもそのバックアップを独立した媒体に保存しておきます。



この*Descriptor*には、Multisig ポートフォリオに含まれるすべての xpub と、generate に使用された派生パスが含まれる。Multisigポートフォリオを復元するためには、Mnemonicのフレーズをすべて**持つか、署名のしきい値に達するために必要な最小限の数だけ持つかのどちらかでなければならない。しかし、後者の場合、欠落している署名者の**xpubs**を持つことも不可欠である。Descriptor*には、あなたのMultisigのxpubがすべて含まれている。



Multisigを検索するためには、Hardware Walletを使用するごとに、閾値に応じた最低数のMnemonicフレーズ（私の場合は2フレーズ）と*ディスクリプタ*が必要です。



この*Descriptor*は秘密鍵を含まず、公開鍵のみを含む。これは、資金へのアクセスを与えないことを意味する。従って、ビットコインに完全にアクセスできる Mnemonic フレーズほど重要ではありません。Descriptor*のリスクは機密性だけであり、危殆化した場合、第三者はあなたの取引をすべて観察することはできるが、あなたの資金を使うことはできない。



この*Descriptor*のコピーを複数作成し、Multisigの各署名デバイスと一緒に保管することを強くお勧めします。例えば、私の場合、*Descriptor*を紙に印刷し、Coldcardに1部、Trezorに1部、Ledgerに1部、それぞれ保管しています。また、この*Descriptor*をPDFファイルとして3つのUSBスティックに保存し、それぞれをハードウェア・ポートフォリオの1つと一緒に保管する。こうすることで、私はこの*ディスクリプタ*を紛失しない可能性を最大限に高め、各デバイスに2つのコピー（物理的なものとデジタルなもの）を確実に持っている。



Multisigポートフォリオが作成されると、Sparrowは自動的にこの*Descriptor*を提供します。PDF保存...*」ボタンをクリックすると、テキストとしてもQRコードとしても保存できます。



![Image](assets/fr/22.webp)



その後、このPDFを印刷し、USBスティックにコピーすることができます。



![Image](assets/fr/23.webp)



また、この*Descriptor*をColdcardに登録する（もしColdcardを使用するのであれば）。これにより、Coldcardは、後で署名された各トランザクションがオリジナルのWalletに対応していることを確認できるようになる。正しいxpub、正しいAddressフォーマット、正しい派生パス...。このインポートされた*Descriptor*がなければ、Coldcardは、Exchangeアドレスがハイジャックされていないこと、またはPSBTが改ざんされていないことを確認できない。



これはMultisigにおいてColdcardが非常に興味深い点である。Coldcardは、他のハードウェア・ウォレットが許さない、ある種の巧妙な攻撃に対する追加チェックを提供する（もちろん、署名に使用することが前提だが）。



Sparrowで "*設定*"メニューにアクセスし、"*エクスポート...*"をクリックします。



![Image](assets/fr/24.webp)



Coldcard Multisig*"オプションの横にある "*Export File...*"をクリックし、テキストファイルをマイクロSDカードに保存します。



![Image](assets/fr/25.webp)



次にカードをColdcardに挿入します。Settings*」メニューから「*Multisig Wallets*」を選択し、「*Import from SD*」を選択します。



![Image](assets/fr/26.webp)



適切なファイルを選択し、インポートを確認する。



![Image](assets/fr/27.webp)



新しくインポートしたMultisigの名前をクリックします。



![Image](assets/fr/28.webp)



Multisigの設定パラメータを確認し、登録を確定する。



![Image](assets/fr/29.webp)



これで Multisig が Coldcard に正しく保存されました。同じMultisigに複数のColdcardを使用している場合は、それぞれのColdcardに対してこの手順を繰り返してください。



Descriptor*の保存に加え、Mnemonicフレーズの保存にも特に注意してください。これから始める方は、この他のチュートリアルを参考にして、正しい保存と管理方法を学ぶことを強くお勧めします：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Multisigで最初のビットコインを受け取る前に、**空のリカバリーテスト**を行うことを強くお勧めします。最初に受け取った Address などの参考情報をメモし、Wallet がまだ空の状態でハードウェアウォレットをリセットします。次に、Multisig Wallet を、Mnemonic のフレーズペーパー・バックアップを使ってハードウェア・ウォレット上でリストアし、次に *Descriptor* を使って Sparrow 上でリストアしてみてください。リストア後に生成された最初のAddressが、最初にメモしたものと一致しているかどうかを確認してください。もし一致していれば、紙のバックアップが信頼できるものであることが確認できます。



リカバリーテストの方法については、こちらのチュートリアルを参照されたい：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Multisigでビットコインを受け取る



これでWalletはビットコインを受け取る準備ができました。Sparrowの "*Receive*"タブをクリックしてください。



![Image](assets/fr/30.webp)



Sparrow Walletで生成されたAddressを使用する前に、時間をかけてハードウェアウォレットの画面で直接確認してください。これにより、Addressが改ざんされていないこと、および関連する資金を使用するために必要な秘密鍵がデバイスに保持されていることを確認できます。これは、多くの攻撃ベクトルからあなたを守るのに役立ちます。



Addressを表示するには、"*Display Address*"をクリックし、TrezorまたはLedgerにAddressを表示させます。



![Image](assets/fr/31.webp)



Coldcardを使えば、この検証はSparrowとのやり取りなしに行うことができます。Address Explorer*」メニューを開き、一番下にあるMultisigを選択するだけです。



![Image](assets/fr/32.webp)



すると、Multisigが生成した受信アドレスが表示される。



![Image](assets/fr/33.webp)



各 Hardware Wallet に表示されている Address が Sparrow Wallet の Address と正確に一致していることを確認する。Addressの完全性を確認するため、支払人とAddressを共有する直前に行うことをお勧めする。



そしてこのAddressに "*Label*"を割り当て、受け取ったビットコインの出所を示すことができます。これはUTXOの管理を整理する良い方法です。



![Image](assets/fr/34.webp)



これが確認されると、Addressを使ってビットコインを受け取ることができる。



![Image](assets/fr/35.webp)



## Multisigでビットコインを送る



Multisig Walletで最初のSatsを受け取りました！Sparrowの "*Send*"タブで新しいトランザクションを作成します。



![Image](assets/fr/36.webp)



コインコントロール*を使用する場合、つまり使用したいUTXOを手動で選択する場合は、「*UTXOs*」タブに移動します。使用したいUTXOを選択し、"*Send Selected*"をクリックしてください。自動的に "*Send*"タブにリダイレクトされ、UTXOはすでに入力されています。



![Image](assets/fr/37.webp)



宛先Addressを入力します。Add*" をクリックすると、複数のアドレスを追加できます。



![Image](assets/fr/38.webp)



ラベル*」を追加して、この支出の目的を説明すると、取引の追跡が容易になります。



![Image](assets/fr/39.webp)



選択した Address に送信する金額を入力する。



![Image](assets/fr/40.webp)



現在のネットワーク状況に応じて充電率を調整してください。例えば、[Mempool.space](https://Mempool.space/)を参照して、適切な充電レベルを選択してください。



すべての取引パラメータをチェックした後、"*Create Transaction*"をクリックする。



![Image](assets/fr/41.webp)



全てに問題がなければ、"*Finalize Transaction for Signing*"をクリックしてください。



![Image](assets/fr/42.webp)



画面の下に、スパロウが2つのサインを待っているのが見えるだろう。これは普通のことで、ここで使われているWalletはMultisig 2-de-3である。



![Image](assets/fr/43.webp)



コールドカードでサインを始めます。これを行うには、マイクロSDカードをコンピュータに挿入し、"*Save Transaction*"をクリックします。



![Image](assets/fr/44.webp)



署名するトランザクションをHardware Walletに送信し、Sparrowから取り出すには3つの方法があります。1つ目はマイクロSDカードを使用する方法です。2つ目はケーブル接続で、2つ目の署名（LedgerとTrezor）に使用します。最後に、Coldcard Q、Jade Plus、Passport V2などのカメラ付きデバイスの場合、QRコード通信を使用することも可能です。



PSBT（*Partially Signed Bitcoin Transaction*）をマイクロSDに保存したら、それをColdcard MK3に挿入し、"*Ready to Sign*"メニューを選択する。



![Image](assets/fr/45.webp)



Hardware Walletの画面で、取引パラメータ（受取人のAddress、送金額、手数料）を注意深く確認します。トランザクションが確認されたら、署名に進むためにバリデーションを行います。



![Image](assets/fr/46.webp)



次にマイクロ SD をコンピュータに戻し、Sparrow で「*Load Transaction*」をクリックします。ファイルからColdcardが署名したPSBTを選択します。



![Image](assets/fr/47.webp)



Coldcardの署名が追加されているのがわかります。次に2つ目のデバイス（この場合はLedger）を使って2つ目の署名を行う。Ledgerを接続し、ロックを解除して、Sparrowの "*Sign*"をクリックする。



![Image](assets/fr/48.webp)



Hardware Walletの名前の横にある "*Sign*"をクリックしてください。



![Image](assets/fr/49.webp)



このMultisigで初めてLedgerを使うとき、Sparrowは共同署名者の拡張公開鍵(xpubs)を検証するように要求します。Coldcardと同様に、このステップにより、後でやみくもに署名することを防ぐことができます。この情報を検証するには、Ledgerの画面に表示されるxpubと、他のハードウェアウォレットから直接提供されるxpubを比較してください。



![Image](assets/fr/50.webp)



受取人のAddress、送金額、取引手数料を確認し、取引に署名する。



![Image](assets/fr/51.webp)



スクリーンを押してサインする。



![Image](assets/fr/52.webp)



これでスパロウはMultisigポートフォリオから資金を放出するのに必要な2つのサインを手に入れた。最後にもう一度トランザクションをチェックし、すべてがうまくいったら、"*Broadcast Transaction*"をクリックしてネットワーク上にブロードキャストする。



![Image](assets/fr/53.webp)



この取引はスパローWalletの「*取引*」タブにあります。



![Image](assets/fr/54.webp)



おめでとうございます、これでSparrowでのマルチシグネチャWalletの設定と使い方がわかりました。もしこのチュートリアルが役に立ったら、以下にGreenの親指を残していただけるとありがたいです。この記事をあなたのソーシャルネットワークでシェアしてください。シェアありがとうございました！



Bitcoin、Wallet、passphrase BIP39のセキュリティーを向上させる別の方法については、このチュートリアルを参照されることをお勧めします：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7