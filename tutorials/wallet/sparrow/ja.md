---
name: Sparrow Wallet
description: Sparrow Walletのインストール、設定、使用方法
---
![cover](assets/cover.webp)

Sparrow Walletは、Craig Raw氏によって開発されたセルフカストディBitcoinポートフォリオ管理ソフトウェアです。このオープンソースソフトウェアは、その多くの機能と直感的なInterfaceでビットコイナーに高く評価されています。

スパローには2つの使い方がある：


- Hot Walletのように、秘密鍵はPCに保存される。
- ColdのWalletマネージャーとして、秘密鍵はHardware Walletに保持される。このモードでは、Sparrowは公開されたWallet情報を操作し、資金を追跡し、アドレスを生成し、トランザクションを構築するだけであるが、これらのトランザクションを有効にするにはHardware Walletの署名が必要である。したがって、Ledger LiveやTrezor Suiteのようなアプリケーションを置き換えることができる。

Sparrowはシングルサインウォレットとマルチサインウォレットをサポートしており、複数のウォレットを流動的に管理することができます。例えば、Ledgerに接続されたWallet、Trezorに接続されたHot、Walletを同時にコントロールすることができます。

また、このソフトウェアには高度なコイン・コントロール機能があり、取引に使用するUTXOを正確に選択して機密性を最適化することができます。

接続に関しては、Sparrowは自分のBitcoinノードに接続することができます。Electrumサーバー経由でリモート接続するか、Bitcoin Coreで接続します。自分のノードをまだ持っていない場合は、パブリックノードを使うことも可能です。リモート接続はTor経由で行います。

## スパローWalletを装着

Sparrow Wallet公式ダウンロードページ](https://sparrowwallet.com/download/)にアクセスし、お使いのOSに対応するソフトウェアのバージョンを選択してください。

![Image](assets/fr/01.webp)

ソフトウェアをインストールする前に、そのソフトウェアの完全性と信頼性をチェックすることが重要です。その方法がわからない場合は、ここに完全なチュートリアルがあります：

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrowのインストールが完了したら、最初の説明画面をスキップして、そのまま接続管理画面に進むことができます。

![Image](assets/fr/02.webp)

## Bitcoinネットワークへの接続

Bitcoinネットワークと相互作用し、トランザクションをブロードキャストするには、SparrowはBitcoinノードに接続する必要があります。この接続を確立するには主に3つの方法があります：


- 🜞 パブリックノードを使う、つまりそのような接続を許可しているサードパーティーノードに接続する。自分のBitcoinノードを持っていない場合、このオプションでSparrowをすぐに始めることができます。しかし、接続先のノードがあなたの全てのトランザクションを見ることになり、機密性が損なわれる可能性があります。鍵を管理することは不可欠ですが、自分のノードを持つことはさらに良いことです。ですから、このオプションは、プライバシーへのリスクに注意しながら、始めたばかりの場合にのみ使用してください。
- 🟢 Bitcoin Coreノードへの接続。BitcoinCoreが同じマシンにインストールされている場合はローカルに、BitcoinCoreがインストールされていない場合はリモートで、BitcoinCoreをSparrow Walletに接続することができます。
- 🔵 Electrumサーバー経由での接続。UmbrelやStart9のようなnode-in-a-boxソリューションのように、BitcoinノードにElectrumが搭載されている場合、Sparrowからリモート接続することができます。

**第三者を信頼する必要性を減らし、機密性を最適化するために、自ノードでElectrsまたはBitcoin Core経由の接続を使用することが望ましい**。

### パブリック・ノード🜞に接続する。

パブリック・ノードへの接続は非常に簡単です。パブリック・サーバー*」タブをクリックする。

![Image](assets/fr/03.webp)

ドロップダウンリストからノードを選択します。

![Image](assets/fr/04.webp)

そして、"*Test Connection*"をクリックする。

![Image](assets/fr/05.webp)

接続が完了すると、Sparrow WalletはInterfaceの右下に黄色いチェックを表示し、パブリックノードに接続していることを示します。

![Image](assets/fr/06.webp)

### Bitcoinコアへの接続

Bitcoinノードに接続する2つ目の方法は、SparrowとBitcoin Coreをリンクすることです。Bitcoin Coreが同じマシンにインストールされている場合、認証はクッキーファイルを介して行われます。Bitcoin Coreがリモートマシンにある場合は、`Bitcoin.conf`ファイルで定義されたパスワードを使用する必要があります。

剪定されたBitcoin Coreノードを使用する場合、ローカルに保存されたブロックより前のトランザクションを含むWalletをリストアすることができないことに注意してください。しかし、Sparrowで作成された新しいWalletでは、これは問題ではありません：剪定されたノードであっても、新しいトランザクションは表示されます。

Bitcoin Coreノードを設定するには、お使いのオペレーティング・システムに応じて、以下のチュートリアルのいずれかを参照してください：

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Sparrowの「*Bitcoin Core*」タブを開きます。

![Image](assets/fr/07.webp)

*Bitcoinコア・ローカル使用時：*

Bitcoin Coreがインストールされている場合は、ソフトウェアファイルの中から`Bitcoin.conf`ファイルを探します。このファイルが存在しない場合は、作成することができます。テキストエディタで開き、以下の行を挿入してください：

```ini
server=1
```

その後、変更を保存します。

また、Bitcoin-QTのInterfaceグラフィックから、"*設定*">"*オプション...*"に移動し、"*RPCサーバーを有効にする*"オプションを有効にすることによって、これを行うことができます。> オプション...*"に移動し、"*RPCサーバーを有効にする*"オプションを有効にします。

変更後はソフトウェアを再起動することをお忘れなく。

![Image](assets/fr/08.webp)

その後、Sparrow Walletに戻り、Cookieファイルのパスを入力します。Cookieファイルは、OSにもよりますが、通常`Bitcoin.conf`と同じフォルダにあります：

| ~/Library/Application Support/Bitcoin | **macOS** | ~/Library/Application Support/Bitcoin | **macOS** | ~/Library/Application Support/Bitcoin

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%Bitcoin | %APPDATA%Bitcoin | %APPDATA%Bitcoin | %APPDATA%Bitcoin

|**Linux** | ~/.Bitcoin

![Image](assets/fr/09.webp)

他のパラメータはデフォルトのままにして、URL `127.0.0.1`とポート `8332` を指定し、"*Test Connection*"をクリックする。

![Image](assets/fr/10.webp)

接続が確立されます。右下にGreenのチェックマークが表示され、Bitcoin Coreノードに接続されていることを示します。

![Image](assets/fr/11.webp)

**Bitcoinコア・リモコン付き:**。

Bitcoin Coreが同じネットワークに接続された別のマシンにインストールされている場合は、まずソフトウェアファイルの中から`Bitcoin.conf`ファイルを探します。このファイルがまだ存在しない場合は、作成することができます。テキストエディタでこのファイルを開き、以下の行を追加します：

```ini
server=1
```

ファイルを編集したら、お使いのオペレーティングシステムに適したフォルダに保存してください：

**MacOS** | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin | ~/Library/Application Support/Bitcoin

| ----------- | ------------------------------------- |

| ウィンドウズ | %APPDATA%Bitcoin

|**Linux** | ~/.Bitcoin

この操作は、Bitcoin-QT Interface グラフィカル Interface からも実行できます。メニューの "*Settings*"から "*Options...*"を選択し、"*Enable RPC server*"にチェックを入れて有効にします。Bitcoin.conf`ファイルが存在しない場合は、"*Open Configuration File*"をクリックして、このInterfaceから直接作成することができます。

![Image](assets/fr/12.webp)

ローカルネットワーク上のBitcoin CoreをホストしているマシンのIP Addressを探します。これを行うには、[Angry IP Scanner](https://angryip.org/)のようなツールを使用することができます。議論のために、あなたのノードのIP Addressが`192.168.1.18`であると仮定しましょう。

Bitcoin.conf`ファイルに以下の行を追加し、ノードのIP Addressに合わせて`rpcbind=192.168.1.18`を設定する。

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Bitcoin.conf`ファイルに、リモート接続用のユーザー名とパスワードを追加する。loic`をユーザー名に、`my_password`を強力なパスワードに置き換えてください：

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

ファイルを修正して保存した後、Bitcoin-QT ソフトウェアを再起動してください。

これでスパローWalletに戻ることができる。**User / Pass**タブを開きます。`Bitcoin.conf`ファイルに設定したユーザー名とパスワードを入力します。他のパラメータはデフォルトのまま、つまりURL `127.0.0.1`とポート `8332` のままにしておく。次に **Test Connection** をクリックする。

![Image](assets/fr/15.webp)

接続が確立されます。右下にGreenのチェックが表示され、Bitcoin Coreノードに接続されていることを示します。

![Image](assets/fr/16.webp)

### Electrumサーバーに接続する 🔵。

最後の接続方法は、リモートElectrumサーバーを使う方法です。この方法では、他のデバイスからTor経由でノードに接続し、Sparrow上のポートフォリオをより素早く閲覧することができます。UmbrelやStart9のような、ワンクリックでElectrumをインストールできるnode-in-a-boxソリューションをお持ちの方に特に適しています。

これを行うには、ElectrumサーバーのTor `.onion' Addressを取得します。例えばUmbrelの場合、Electrsアプリケーションの中にあります。

![Image](assets/fr/17.webp)

Sparrow Walletの「*Private Electrum*」タブにアクセス。

![Image](assets/fr/18.webp)

空欄にTor Addressを入力してください。他の設定はデフォルトのままで構いません。そして "*Test Connection*"をクリックしてください。

![Image](assets/fr/19.webp)

接続が確認されます。このウィンドウを閉じると、Electrumサーバーに接続されていることを示す青いチェックマークが右下に表示されます。

![Image](assets/fr/20.webp)

## 温かいポートフォリオを作る

Sparrow Wallet が Bitcoin ネットワークと通信するように設定されたので、最初の Wallet を作成する準備ができました。このセクションでは、Hot Wallet、つまり秘密鍵がコンピュータに保存されているWalletの作成について説明します。あなたのコンピュータはインターネットに接続された複雑なマシンであるため、非常に大きな攻撃対象となります。従って、Hot Wallet は限られた量のビットコインにのみ使用すべきです。より大量のビットコインを保管するには、安全なWalletとHardware Walletをお選びください。これをお探しの場合は、次のセクションに進んでください。

HotのWalletを作成するには、Sparrow Walletのホーム画面から「*ファイル*」タブをクリックし、「*新規Wallet*」をクリックします。

![Image](assets/fr/21.webp)

ポートフォリオの名前を入力し、"*Create Wallet*"をクリックします。

![Image](assets/fr/22.webp)

Interfaceの上部で、「*シングル署名*」または「*マルチ署名*」のどちらのポートフォリオを作成するかを選択できます。そのすぐ下で、UTXOをロックするスクリプトのタイプを選択する。最新の規格を使用することをお勧めします：「*Taproot (P2TR)*」。

![Image](assets/fr/23.webp)

次に「*新規またはインポートされたSoftware Wallet*」をクリックします。

![Image](assets/fr/24.webp)

ほぼすべてのBitcoinポートフォリオ・ソフトウェアでサポートされているBIP39標準を選択してください。次に、回復フレーズの長さを選択する。現在のところ、どちらも同じようなセキュリティーを提供しているため、12語のフレーズで十分ですが、12語のフレーズの方が保存が簡単です。

![Image](assets/fr/25.webp)

generate **New** ボタンをクリックして、Wallet の Mnemonic フレーズを generate にしてください。このフレーズにより、あなたのすべてのビットコインに完全かつ無制限にアクセスできるようになります。このフレーズを所持している者は、あなたのコンピュータに物理的にアクセスしなくても、あなたの資金を盗むことができます。

この12単語のフレーズは、コンピュータの紛失、盗難、破損の際にビットコインへのアクセスを回復します。したがって、慎重に保存し、安全な場所に保管することが非常に重要です。

紙に刻むこともできますし、セキュリティを高めるために、ステンレス鋼に刻んで、火災、洪水、倒壊から守ることもできます。Mnemonicの媒体の選択は、あなたのセキュリティ戦略によって異なりますが、適度な量を含むWalletを暖かく過ごすためにスパロウを使用するのであれば、紙で十分でしょう。

Mnemonicのフレーズを保存・管理する適切な方法については、特に初心者の方には、こちらのチュートリアルをご覧になることを強くお勧めします：

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**もちろん、このチュートリアルで私がしているように、インターネット上でこれらの言葉を決して共有してはいけません。この例のWalletはTestnetでのみ使用し、チュートリアルの最後には削除します。**

また、"*Use passphrase*"のボックスをクリックして、passphrase BIP39を追加することもできます。警告：passphraseの使用は非常に便利ですが、その仕組みを理解していないと非常に危険です。そのため、この短い理論的な記事を読むことを強くお勧めする：

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Mnemonicとpassphraseを物理メディアに保存したら、"*Confirm Backup*"をクリックします。

![Image](assets/fr/27.webp)

12語を再入力して正しく保存されたことを確認し、「*Create Keystore*」をクリックします。

![Image](assets/fr/28.webp)

その後、「*Import Keystore*」をクリックし、Mnemonicのフレーズからポートフォリオ・キーをgenerateに取り込む。

![Image](assets/fr/29.webp)

**Apply**」をクリックし、ポートフォリオの作成を完了します。

![Image](assets/fr/30.webp)

Sparrowポートフォリオへのアクセスを保護するために、強力なパスワードを設定してください。このパスワードを忘れないように、パスワードマネージャーで管理しておくと良いでしょう。このパスワードは鍵の導出には使用されません。Sparrow Walletを経由してWalletにアクセスするためにのみ使用されます。したがって、このパスワードがなくても、BIP39互換のアプリケーションからビットコインにアクセスするには、Mnemonicのフレーズで十分です。

![Image](assets/fr/31.webp)

これで Hot Wallet が作成されました。Hardware WalletをSparrowで使用する予定がない場合は、このチュートリアルの*ビットコインの受け取り*セクションまで読み飛ばしてかまいません。

## Coldポートフォリオの管理

Sparrow Walletを使用する2つ目の方法は、Hardware Walletのポートフォリオマネージャーとして設定することです。この構成では、Bitcoin Walletの秘密鍵はHardware Walletのみに残り、Sparrowは公開情報のみにアクセスします。このアプローチでは、秘密鍵が専用デバイス（多くの場合、セキュアチップを搭載）に保管されるため、前述のHotウォレットよりも高いレベルのセキュリティが提供されます。

Hardware WalletをSparrowに接続するには、主に2つの方法があります：


- Trezor Safe 3やLedger Nano S Plusなどのエントリーモデルでよく使用されるケーブル；
- MicroSDカードまたはQRコードExchangeを介したエアギャップモード、つまり直接有線接続なし。

Sparrowはこれら全ての通信方法をサポートしており、市場にあるほとんどのハードウェアウォレットと互換性があります。

このチュートリアルでは、ケーブル付きのLedger Nano Sを使用しますが、Air-Gapモードでも手順は同様です。Hardware Walletの詳細については、Plan ₿ Networkの専用チュートリアルをご覧ください。

始める前に、WalletがHardware Walletに設定済みであることを確認してください。有線接続の場合は、ケーブルでパソコンと接続してください。

Sparrow Walletにいわゆる「*Keystore*」（ポートフォリオ管理に必要な公開情報）をインポートするには、「*File*」タブをクリックし、「*New Wallet*」をクリックします。

![Image](assets/fr/32.webp)

ポートフォリオに名前を付け、"*Create Wallet*"をクリックしてください。Hardware Walletの名前を入力することをお勧めします。

![Image](assets/fr/33.webp)

Interfaceの上部で、ポートフォリオを "*Single Signature*"または "*Multi Signature*"から選択します。この例では、シングル・シグネチャーのポートフォリオを設定します。

UTXOをロックするスクリプトの種類を選択します。Hardware Walletが対応している場合は、「*Taproot (P2TR)*」を選ぶといいだろう。

![Image](assets/fr/34.webp)

次に、接続方法によって手順が異なります。エアギャップ方式の場合は「*エアギャップHardware Wallet*」を選択します。その後、お使いの機器に応じた手順に従ってください。

![Image](assets/fr/35.webp)

私のようにケーブル接続の場合は、"*Connected Hardware Wallet*"を選ぶ。

![Image](assets/fr/36.webp)

スキャン」をクリックし、Sparrowにデバイスを検出させます。デバイスが接続され、ロックが解除されていることを確認してください。Ledgerなど一部の機種では、検出を有効にするために「**Bitcoin**」アプリケーションを開く必要があります。

![Image](assets/fr/37.webp)

Import "を選択する。

![Image](assets/fr/38.webp)

**Apply**」をクリックし、ポートフォリオの作成を完了します。

![Image](assets/fr/39.webp)

Sparrow Walletへのアクセスを保護するために強力なパスワードを設定します。このパスワードは、あなたの公開鍵、アドレス、取引履歴を保護します。パスワードマネージャに保存することをお勧めします。なお、このパスワードは鍵の導出には関係ありません。このパスワードがなくても、BIP39互換のソフトウェアを使って、Mnemonicからビットコインにアクセスすることができます。

![Image](assets/fr/40.webp)

これでSparrow上で管理ポートフォリオが設定されました。

![Image](assets/fr/41.webp)

## ビットコインを受け取る

WalletがSparrowにセットアップされたら、ビットコインを受け取ることができます。**受信**メニューにアクセスするだけです。

![Image](assets/fr/42.webp)

Sparrowは、あなたのWalletの中で最初に未使用のAddressを表示します。このAddressに "*Label*"を追加することで、将来これらのサトシの由来を思い出すことができます。

![Image](assets/fr/43.webp)

Hot Walletを使用している場合は、表示されたAddressをコピーするか、関連するQRコードをスキャンすることで、すぐに使用することができます。

Hardware Walletを使用する場合、使用前に端末の画面でAddressを確認することが非常に重要です。有線の場合は、Hardware Walletを接続してロックを解除し、Sparrowで「*Address*を表示」をクリックします。Hardware Walletに表示されているAddressとSparrowに表示されているAddressが一致していることを確認してください。

![Image](assets/fr/44.webp)

Hardware Walletエアギャップユーザーの場合、Address検証は機種によって異なります。正確な手順については、専用のPlan ₿ Networkチュートリアルをご覧ください。

支払人によりトランザクションがブロードキャストされると、「*Transactions*」タブに表示されます。クリックすると、txidなどの詳細が表示されます。

![Image](assets/fr/45.webp)

Addresses*"タブでは、すべての受信トレイアドレスのリストが表示されます。すでに使用されているかどうか、ラベルが追加されているかどうかを確認できます。 *受信*」アドレスは、「*受信*」をクリックした際にSparrowが表示するアドレスで、着金用のものです。Change*」アドレスは、Exchangeの取引に使用されます。つまり、インプットのUTXOの未使用分を回収するために使用されます。

![Image](assets/fr/46.webp)

UTXOs*"タブには、すべてのUTXO、つまりあなたが保持しているBitcoinフラグメントが表示されます。それぞれのUTXOの量と関連するラベルを見ることができます。

![Image](assets/fr/47.webp)

## ビットコインを送る

Walletでサトシを手に入れたあなたには、サトシを送るという選択肢もある。この方法はいくつかあるが、直接 "*送信*"メニューに行くよりも、使うコインをより正確にコントロールするために "*UTXOs*"メニューを使うことをお勧めする（*コインコントロール*）（初心者なら後者で十分かもしれないが）。

![Image](assets/fr/48.webp)

このトランザクションのインプットとして使用したいUTXOを選択し、"*Send Selected*"をクリックしてください。この方法によって、UTXOの中から最も適切なソースを選択することができ、経費や受取時に適用されるラベルに応じて、支払いの機密性を最適化することができます。選択したUTXOの合計が、送信する金額より大きいことを確認してください。

![Image](assets/fr/49.webp)

受取人のAddressを「*Pay to*」欄に入力してください。カメラアイコンをクリックして、ウェブカメラでAddressをスキャンすることもできます。"*+Add*"ボタンをクリックすると、一度の決済で複数の宛先へのお支払いが可能です。

![Image](assets/fr/50.webp)

お取引にラベルを貼って、その目的を思い出してください。このラベルは、あなたのExchangeにも関連付けられます。

![Image](assets/fr/51.webp)

このAddressに送られる金額を入力する。

![Image](assets/fr/52.webp)

現在の市況に応じて料金レートを調整します。料金の絶対値を入力するか、スライダーで料金を調整します。

![Image](assets/fr/53.webp)

Interfaceの下部には、"*Efficiency*"と "*Privacy*"のどちらかを選ぶことができる。私の場合、このポートフォリオにはUTXOが1つしかないため、"*Privacy*"オプションは利用できない。「*Efficiency*」は古典的な取引に相当し、「*Privacy*」はStonewallタイプの取引で、ミニCoinJoinをシミュレートすることで機密性を強化する取引構造であり、連鎖分析をより複雑にする。

![Image](assets/fr/54.webp)

Sparrowは、インプット、アウトプット、取引手数料を示す概要図を表示します（この図が示唆するところとは逆に、手数料は実際にはアウトプットではないことに注意してください）。全てに問題がなければ、"*Create Transaction*"をクリックしてください。

![Image](assets/fr/55.webp)

Elementsの詳細ページが表示されます。すべての情報が正しいことを確認し、"*Finalize Transaction for Signing*"をクリックしてください。

![Image](assets/fr/56.webp)

デフォルトのSighashを維持することが重要です。このトレーニングコースでは、Sighashについて知っておくべきことをすべて説明しています：

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

次の画面では、使用しているWalletのタイプによってオプションが異なります：


- Hardware WalletのAir-Gapの場合、"*Show QR*"をクリックしてデバイスで署名できるPSBTを表示し、"*Scan QR*"を使用して署名されたPSBTをSparrowにロードします。同様の方法で、"*Save Transaction*"オプションも動作しますが、microSD .NET上の交換が対象となります；
- Hot Walletの場合は、「*サイン*」をクリックし、Walletのパスワードを入力してサインするだけです；
- 有線のHardware Walletの場合は、「*Sign*」をクリックして、署名されていないトランザクションをデバイスに送信することもできます。

![Image](assets/fr/57.webp)

Hardware Walletで、受取人のAddress、送金額、料金を確認する。すべてが正しければ、署名に進む。

トランザクションが署名されると、Sparrowに再表示され、Bitcoinネットワーク上でブロードキャストされ、ブロックに組み込まれる準備が整います。問題がなければ、"*Broadcast Transaction*"をクリックしてください。

![Image](assets/fr/58.webp)

あなたの取引は現在ブロードキャストされ、確認待ちです。

![Image](assets/fr/59.webp)

## Sparrowでのポートフォリオの管理と設定

設定」タブでは、ポートフォリオの詳細情報をご覧いただけます：


- ポートフォリオ・タイプ（シングル・シグまたはmulti-sig）；
- 使用スクリプトのタイプ ；
- ポートフォリオに割り当てた名前；
- マスターキー刻印；
- 迂回路；
- アカウントの拡張公開鍵。

![Image](assets/fr/60.webp)

エクスポート*」ボタンを使えば、Sparrowで設定した情報を保持したまま、他のソフトで使えるようにポートフォリオ情報をエクスポートすることができます。

アカウントの追加 "ボタンをクリックすると、ポートフォリオにアカウントを追加できます。アカウントは、個別の受信トレイアドレスに対応します。この機能は、例えば、Mnemonicのワンフレーズで、個人用とビジネス用のアカウントを分けたい場合に便利です。

Advanced*」ボタンをクリックすると、SparrowのAddress検索のカスタマイズやポートフォリオパスワードの変更など、高度な設定にアクセスできます。

![Image](assets/fr/61.webp)

Sparrow Wallet を終了すると、Wallet は自動的にロックされます。次にソフトを開くと、パスワードでロックを解除するよう促すウィンドウが表示されます。

![Image](assets/fr/62.webp)

このウィンドウが開かない場合、またはSparrowで別のポートフォリオを開きたい場合は、「*ファイル*」タブをクリックし、「*Wallet*を開く」を選択します。

![Image](assets/fr/63.webp)

ファイルマネージャーを開き、Sparrowがウォレットを保存しているフォルダを開きます。開きたいWalletを選択し、パスワードを入力するだけでロックが解除されます。

![Image](assets/fr/64.webp)

設定 "の下にある "*ファイル*"メニューには、すでに前のセクションで説明したBitcoinネットワーク接続パラメータがあります。また、使用する単位、変換用の不換紙幣、情報ソースなど、様々なパラメーターを調整することができます。

![Image](assets/fr/65.webp)

「**View**」タブでは、カスタマイズオプションや、ポートフォリオの取引検索をリフレッシュする「**Refresh Wallet**」など、便利なコマンドにアクセスできます。

![Image](assets/fr/66.webp)

ツール*"タブには、.NET Frameworkを含むいくつかの高度なツールがまとめられています：


- "*Sign/Verify Message*"では、受信しているAddressの所持を証明したり、署名を確認したりすることができる。
- また、「*Send To Many*」は、Interfaceを簡略化したもので、一度に複数の受取アドレスに取引を行うことができるため、一括消費に便利である。
- "*Sweep Private Key*"を使用すると、シンプルな秘密鍵で保護されたビットコインを取得し、Sparrow Walletに転送することができます。これは特に、HDウォレットが普及する前の2010年代初頭のビットコインをお持ちの方に便利です。
- "ダウンロードの検証 "は、お使いのデバイスにインストールする前に、ダウンロードしたソフトウェアの完全性と信頼性を検証します。
- "*Restart In*"を使用すると、TestnetまたはSignetネットワーク上のウォレットに切り替えることができます。これは、実質的な価値のないコインでテストネットワークにアクセスしたい場合に便利です。

![Image](assets/fr/67.webp)

Bitcoinポートフォリオを日常的に管理するための優れたツールであるSparrow Walletソフトウェアについては、すべてご理解いただけたと思います。

このチュートリアルが役に立ったと思ったら、下にGreenの親指を残していただけるとありがたい。あなたのソーシャルネットワークでシェアしてください。ありがとうございました！

また、Hardware Wallet COLDCARD Q を Sparrow Wallet で設定する方法を説明した別のチュートリアルもお勧めです：

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3