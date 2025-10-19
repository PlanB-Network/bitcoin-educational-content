---
name: シードキーパー
description: Wallet、BitcoinをSeedkeeperスマートカードでバックアップするには？
---

![cover](assets/cover.webp)



Seedkeeperは、デジタル秘密を管理・保護するハードウェア・ソリューションを専門とするベルギーのSatochip社によって開発されたスマートカードである。Bitcoinエコシステム用のスマートカードで有名なSatochip社は、Mnemonicフレーズを保存する従来の方法に代わるものとしてSeedkeeperを設計した。



具体的には、Seedkeeperは、セキュアなプロセッサと改ざん防止メモリ（すなわち「secure element*」）を搭載したEAL6認定の多機能スマートカードの形をとっている。その名前が示すように、Bitcoin Mnemonicのフレーズとパスワードを暗号化され保護された方法で保存するのがその役割です。Seedkeeperを使用すると、generate、インポート、整理、およびカードの安全なコンポーネントに直接秘密を保存することができます。



私見では、Seedkeeperには主に2つの使い方があると思う：




- Bitcoin** Mnemonicフレーズ保存：12または24の単語を紙に書き留める代わりに、スマートカードにインポートし、PINコードで保護することができます。
- パスワード管理**: Seedkeeperアプリケーションから強力なパスワードをgenerateし、スマートカードに直接保存することができます。



技術的に言えば、Seedkeeperは8192バイトの容量があり、最低50の別々の秘密を保存することができる（正確な数は、そのサイズとそれぞれに関連するメタデータに依存する）。Seedkeeperは、コンピュータに接続されたスマートカードリーダー（https://satochip.io/accessories/）を介して、またはNFC接続されたモバイルアプリケーションを介してアクセスすることができる。システム全体は、インターネットに接続することなくオフラインモードで動作するため、攻撃対象が限定される。



![Image](assets/fr/001.webp)



特に興味深い機能は、バックアップを作成するために、1つのSeedkeeperの内容を別のSeedkeeperに複製する機能です。このチュートリアルでは、その方法をご紹介します。



また、SeedSignerやSpecter DIYのようなステートレスHardware Walletと組み合わせると、Seedkeeperは非常に面白い。この場合、Satochipのコンピュータやモバイルクライアントを使う必要はない。Seedkeeperはseedをsecure elementに保持し、署名デバイスで直接使用できるため、紙のQRコードが不要になる。この特別な使用例については、別の専用チュートリアルのテーマなので、このチュートリアルでは説明しない：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1.シードキーパーの用途は？



このチュートリアルでは、Bitcoinに関連するユースケースのみを扱います。パスワード管理機能については、別のチュートリアルのテーマになるので、ここでは触れません。



Mnemonicのフレーズを紙でバックアップするのに比べ、Seedkeeperを使うことにはいくつかの利点がある：





- Walletのseedは平文ではアクセスできません。これを取り出すには、シードキーパーの暗証番号が必要です。Walletを手に入れた泥棒は、この暗証番号なしでは何もできません。





- リスクを2つの要素に分散する：** セキュリティをデジタル的な要素と物理的な要素に分けることができます。例えば、シードキーパーの暗証番号をパスワード・マネージャーに保存する場合、seedを取得するためには、このマネージャーへのアクセスとスマートカードの物理的な所有の両方が必要になります（攻撃の確率は大幅に減少します）。





- 一元管理：** Seedkeeperは、異なるポートフォリオの複数のシードの管理を容易にします。





- 簡単バックアップ:**暗号化されたバックアップを他のSeedKeepersに複製するだけです。



しかし、seedの単純な紙によるバックアップと比べると、多くのデメリットがある：





- 価格は**控えめ（約25ユーロ）だが、それでも紙1枚よりは高い。





- 汎用コンピューティング・デバイスへの依存:** seed の入力と管理には、コンピュータまたはスマートフォンが必要です。これは、Mnemonic が Hardware Wallet よりもはるかに広い攻撃対象領域を持つマシンを通過することを意味します。つまり、MnemonicはHardware Walletよりもはるかに広い攻撃対象領域を持つマシンを通過することになる。これは、ワークステーションが侵害された場合のリスクとなり得る。これが、Hardware WalletのseedをSeedkeeperで保存することをお勧めしない理由です（SeedSignerのようにコンピュータを使わずにステートレスで使用する場合を除く）。Hardware Walletの役割は、まさにseedを最小限の安全性の高い環境に保存することです。seedを普段使っているコンピュータに手動で入力することで、seedはもはやHardware Walletに限定されることはありません。そのため、ColdよりもHotのWalletにSeedkeeperを使う方がよいでしょう（SeedSigner/ステートレスHardware Walletを除く）。





- PINに関連する紛失のリスク：** seedは紙のバックアップとは異なり、直接アクセスできないため、確かに物理的な盗難からの保護は提供される。しかし、いつもそうであるように、セキュリティは盗難のリスクと紛失のリスクとのバランスをとることです。バックアップに暗証番号が必要な場合、この暗証番号を紛失すると、Mnemonicのフレーズを復元することができなくなり、ビットコインにアクセスできなくなります。



これらの長所と短所を考慮すると、SeedKeeperは（パスワード管理機能を除けば）、**ソフトウェア・ポートフォリオ**のシードを保存するのに最適な使い方だと思います。



Seedkeeperのもう一つの興味深い使用例は、ポートフォリオの*ディスクリプタ*を安全かつ確実にバックアップできることです。



## 2.シードキーパーの入手方法は？



シードキーパーを入手するには、主に2つの方法があります。Satochipの公式ストアから直接購入する方法](https://satochip.io/product/seedkeeper/)と、正規代理店から購入する方法です。しかし、Seedkeeperアプレットはオープンソースなので(https://github.com/Toporin/Seedkeeper-Applet)、自分で[空のスマートカード](https://satochip.io/product/blank-javacard-for-diy-project/)にインストールすることもできます。



Seedkeeperのバックアップ機能を使用する場合は、当然ながらスマートカードを2枚購入する必要があります。



## 3.Seedkeeperクライアントのインストール



このチュートリアルでは、seedのポートフォリオをSeedkeeperにバックアップします。まず、パソコンまたはスマートフォンにソフトウェアをインストールします。PCの場合は、[Satochip-Utilsの最新版をダウンロード](https://github.com/Toporin/Satochip-Utils/releases)する必要があります。モバイルの場合、Seedkeeperアプリケーションは[Google Playストア](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper)と[Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060)で入手できます。



![Image](assets/fr/002.webp)



## 4.シードキーパーの初期化



アプリケーションを起動し、「*Click & Scan*」ボタンをクリックします。



![Image](assets/fr/003.webp)



シードキーパーのPINコードの入力を求められます。新しいカードのため、PINコードはまだ設定されていません。このステップをスキップする場合は、任意のコードを入力し、「*次へ*」をクリックしてください。



![Image](assets/fr/004.webp)



その後、カードをスマートフォンの背面に置きます。アプリケーションはSeedkeeperがまだ初期化されていないことを検知し、スマートカードのPINコードを4文字から16文字の間で設定するよう促します。できるだけ長く、ランダムで、さまざまな文字からなる強力なパスワードを設定してください。このPINコードが、リカバリーフレーズへの物理的アクセスに対する唯一の障壁となります。



**この暗証番号は、パスワードマネージャーや別の物理的な媒体などに保存してください。後者の場合、暗証番号の入った媒体は決してシードキーパーと同じ場所に置かないようにしてください。暗証番号がなければ、Seedkeeper に保存された秘密を復元することはできません。



![Image](assets/fr/005.webp)



PINコードをもう一度確認してください。



![Image](assets/fr/006.webp)



これでシードキーパーは初期化されました。先ほど設定したPINコードを入力するとロックが解除されます。



![Image](assets/fr/007.webp)



スマートカードの管理ページに移動します。



![Image](assets/fr/008.webp)



## 5.シードキーパーにseedを登録する



シードキーパーのロックが解除されたら、「*+*」ボタンをクリックします。



![Image](assets/fr/009.webp)



Import secret*"を選択します。generate secret*"オプションを使用すると、アプリケーション内から直接新しいMnemonicフレーズを作成できます。



![Image](assets/fr/010.webp)



この場合、seedをポートフォリオに保存したい。Mnemonic*」をクリックしてください。



![Image](assets/fr/011.webp)



このシークレットには「*ラベル*」を付け、シードキーパーに複数の情報を保存する場合に、簡単に識別できるようにします。



![Image](assets/fr/012.webp)



次に、リカバリーフレーズを入力します。必要であれば、passphrase BIP39やあなたの*ディスクリプタ*を追加することもできます。そして "Import*"をクリックしてください。



![Image](assets/fr/013.webp)



*この画像に写っているMnemonicは架空のものであり、誰のものでもありません。あくまで一例です。自分のMnemonicを決して他人に公開しないでください。



シードキーパーをスマートフォンの背面に置きます。



![Image](assets/fr/014.webp)



あなたのseedが登録されました。



![Image](assets/fr/015.webp)



## 6.シードキーパーでseedにアクセスする



自分のMnemonicフレーズをチェックしたい場合は、シードキーパーを手に取り、「*Click & Scan*」ボタンをクリックしてください。



![Image](assets/fr/016.webp)



PINコードを入力し、「*次へ*」を押してください。



![Image](assets/fr/017.webp)



シードキーパーをスマートフォンの背面に置きます。



![Image](assets/fr/018.webp)



登録されているシークレットのリストが表示されます。この例では、ポートフォリオ「*BLOCKSTREAM App*」のseedを表示したいので、それをクリックする。



![Image](assets/fr/019.webp)



を押してください。



![Image](assets/fr/020.webp)



もう一度シードキーパーをスキャンしてください。



![Image](assets/fr/021.webp)



録音したMnemonicのフレーズが画面に表示されます。



![Image](assets/fr/022.webp)



## 7.Seedkeeperのバックアップ



私のシードキーパーのバックアップを2番目のシードキーパーに取り、2つのコピーを持つようにします。この冗長性は、ビットコインを安全に保管するための戦略の一部となり得ます。例えば、物理的なリスクを抑えるためにフレーズを2つの別々の場所に保管したり、相続計画の一環としてコピーを信頼できる親族に託したりすることができます。



これを行うには、2つ目のシードキーパーを持参します（混乱を避けるため、2つのうち1つをマークで識別することを忘れないでください）。このチュートリアルのステップ4で説明したように、初期化から始めます。もう一度強力なパスワードを選んでください。あなたの戦略に応じて、別のパスワードを選択するか、同じパスワードを維持することができます。



![Image](assets/fr/023.webp)



アプリケーションを開き、「*Click & Scan*」をクリックし、Seedkeeper n°1（ソース）のパスワードを入力し、スキャンします。



![Image](assets/fr/024.webp)



これにより、あなたの秘密のリストが表示されたホームページに移動します。Interfaceの右上にある3つの小さな点をクリックしてください。



![Image](assets/fr/025.webp)



Make a backup*」を選択し、「*Start*」を押します。



![Image](assets/fr/026.webp)



バックアップカード（Seedkeeper n°2）のPINコードを入力してください。



![Image](assets/fr/027.webp)



それからカードをスキャンする。



![Image](assets/fr/028.webp)



メインカード(Seedkeeper n°1)も同様にし、"*Make a backup*"をクリックします。



![Image](assets/fr/029.webp)



あなたのシードキーパー2号には、シードキーパー1号に保存されているすべてのシークレットが入っています。



![Image](assets/fr/030.webp)



シードキーパーn°2をスキャンして、シークレットがコピーされていることを確認することができます。



![Image](assets/fr/031.webp)



以上です！これでBitcoin WalletのMnemonicフレーズを保存するSeedkeeperの使い方がわかりました。次回のチュートリアルでは、Seedkeeperを使ってパスワードを保存する方法をご紹介します。また、SeedSignerとの組み合わせもぜひお試しください：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

このチュートリアルでは、Bitcoin ポートフォリオの ***Descriptors*** について何度か触れてきました。それが何なのかご存知ないですか？その場合は、HDポートフォリオの運用に関わるすべてのメカニズムについて詳しく説明する、無料のCYP 201トレーニング・コースを受講されることをお勧めします！



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f