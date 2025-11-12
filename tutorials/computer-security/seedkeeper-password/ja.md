---
name: Seedkeeper - パスワード管理
description: シードキーパーのICカードでパスワードを保存するには？
---

![cover](assets/cover.webp)



Seedkeeperは、デジタルシークレットを管理・保護するハードウェアソリューションを専門とするベルギーのSatochip社によって開発されたスマートカードである。Bitcoinエコシステム用の各種スマートカードで有名なSatochip社は、ニモニック・フレーズやその他のデジタル秘密を保存する従来の方法に代わるものとしてSeedkeeperを考案した。



具体的には、Seedkeeperは、セキュア・プロセッサと改ざん防止メモリ（いわゆる「セキュア・エレメント」）を備えた、EAL6認証の多機能スマートカードの形をとっている。その名前が示すように、Bitcoinポートフォリオのニーモニックとパスワードを暗号化され保護された方法で保存するのがその役割です。Seedkeeperを使用することで、generate、インポート、整理、保存をカードのセキュアコンポーネントに直接行うことができます。



私見では、Seedkeeperには主に2つの使い方があると思う：




- Bitcoin**ニモニック・フレーズ・ストレージ：12または24の単語を紙に書き留める代わりに、スマートカードにインポートし、PINコードで保護することができます。
- パスワード管理**: Seedkeeperアプリケーションから強力なパスワードをgenerateし、スマートカードに直接保存することができます。



技術的に言えば、Seedkeeperは8192バイトの容量を持ち、最低50の別々の秘密を保存することができる（正確な数は、そのサイズとそれぞれに関連するメタデータに依存する）。Seedkeeperは、コンピュータに接続されたスマートカードリーダー（https://satochip.io/accessories/）を介して、またはNFC接続されたモバイルアプリケーションを介してアクセスすることができる。システム全体は、インターネットに接続することなくオフラインモードで動作するため、攻撃対象が限定される。



![Image](assets/fr/001.webp)



特に興味深い機能は、バックアップを作成するために、1つのSeedkeeperの内容を別のSeedkeeperに複製する機能です。このチュートリアルでは、その方法をご紹介します。



このチュートリアルでは、SeedKeeperを従来のパスワードに使用する方法のみを説明します。もしBitcoin walletニーモニックフレーズを保存するためにSeedKeeperを使用したい場合は、こちらのチュートリアルをご覧ください：



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1.シードキーパーの入手方法は？



シードキーパーを入手するには、主に2つの方法があります。Satochipの公式ストアから直接購入する方法](https://satochip.io/product/seedkeeper/)と、正規代理店から購入する方法です。しかし、Seedkeeperアプレットはオープンソースなので(https://github.com/Toporin/Seedkeeper-Applet)、自分で[空のスマートカード](https://satochip.io/product/blank-javacard-for-diy-project/)にインストールすることもできます。



Seedkeeperのバックアップ機能を使用する場合は、当然ながらスマートカードを2枚購入する必要があります。



## 2.Seedkeeperクライアントのインストール



まずはパソコンやスマートフォンにソフトをインストールします。パソコンの場合は、[Satochip-Utilsの最新版をダウンロード](https://github.com/Toporin/Satochip-Utils/releases)する必要があります。携帯電話の場合は、「Google Play Store」(https://play.google.com/store/apps/details?id=org.satochip.seedkeeper)と「Apple App Store」(https://apps.apple.com/be/app/seedkeeper/id6502836060)でシードキーパーのアプリケーションを入手できます。



![Image](assets/fr/002.webp)



## 3.シードキーパーの初期化



アプリケーションを起動し、「*Click & Scan*」ボタンをクリックします。



![Image](assets/fr/003.webp)



シードキーパーのPINコードの入力を求められます。新しいカードのため、PINコードはまだ設定されていません。このステップをスキップする場合は、任意のコードを入力し、「*次へ*」をクリックしてください。



![Image](assets/fr/004.webp)



その後、カードをスマートフォンの背面に置きます。アプリケーションはSeedkeeperがまだ初期化されていないことを検知し、スマートカードのPINコードを4文字から16文字の間で設定するよう促します。セキュリティのため、PINコードはできるだけ長く、ランダムで、さまざまな文字からなる堅牢なものをお選びください。このPINコードが、パスワードへの物理的アクセスに対する唯一の障壁となります。



**この暗証番号は、パスワードマネージャーや別の物理的な媒体などに保存してください。後者の場合、暗証番号の入った媒体は決してシードキーパーと同じ場所に置かないようにしてください。暗証番号がなければ、Seedkeeper に保存された秘密を復元することはできません。



![Image](assets/fr/005.webp)



PINコードをもう一度確認してください。



![Image](assets/fr/006.webp)



これでシードキーパーは初期化されました。先ほど設定したPINコードを入力するとロックが解除されます。



![Image](assets/fr/007.webp)



スマートカードの管理ページに移動します。



![Image](assets/fr/008.webp)



## 4.Seedkeeperにパスワードを保存



シードキーパーのロックが解除されたら、「*+*」ボタンをクリックします。



![Image](assets/fr/009.webp)



秘密の生成*"を選択します。シークレットをインポート*"オプションは、既存のシークレット（例えば、過去に作成したパスワード）を保存することができます。



![Image](assets/fr/010.webp)



この場合、パスワードを保存したい。パスワード*」をクリックしてください。



![Image](assets/fr/011.webp)



このシークレットに「*ラベル*」を付けておくと、複数の情報をシードキーパーに保存している場合に、識別しやすくなります。また、パスワードやサイトのURLに関連する識別子を追加することもできます。



![Image](assets/fr/012.webp)



パスワードの長さとパラメータを選択し、「*Generate*」、「*Import*」の順にクリックします。



![Image](assets/fr/013.webp)



シードキーパーをスマートフォンの背面に置きます。



![Image](assets/fr/014.webp)



パスワードが登録されました。



![Image](assets/fr/015.webp)



## 5.シードキーパーのパスワードにアクセスする



パスワードを確認したい場合は、シードキーパーを持って「*クリック＆スキャン*」ボタンをクリックしてください。



![Image](assets/fr/016.webp)



PINコードを入力し、「*次へ*」を押してください。



![Image](assets/fr/017.webp)



シードキーパーをスマートフォンの背面に置きます。



![Image](assets/fr/018.webp)



登録されている秘密のリストが表示されます。この例では、私の Plan ₿ Academy アカウントのパスワードを表示したいので、それをクリックします。



![Image](assets/fr/019.webp)



を押してください。



![Image](assets/fr/020.webp)



もう一度シードキーパーをスキャンしてください。



![Image](assets/fr/021.webp)



以前に保存したパスワードが画面に表示されます。これをコピーして、該当するウェブサイトで使用することができます。



![Image](assets/fr/022.webp)



## 6.Seedkeeperのバックアップ



私のシードキーパーのバックアップを2つ目のシードキーパーに取り、2つのコピーを持つようにします。例えば、物理的なリスクを抑えるためにシードキーパーを2つの別々の場所に保管したり、信頼できる親戚にコピーを託したりすることができます。



これを行うには、2つ目のシードキーパーを持参します（混乱を避けるため、2つのうち1つをマークで識別することを忘れないでください）。このチュートリアルのステップ3で説明したように、初期化から始めてください。もう一度、強力なPINコードを選んでください。あなたの戦略に応じて、異なるPINを選択するか、同じものを維持することができます。



![Image](assets/fr/023.webp)



アプリケーションを開き、「*Click & Scan*」をクリックし、シードキーパーn°1（ソース）の暗証番号を入力し、スキャンします。



![Image](assets/fr/024.webp)



これにより、あなたの秘密のリストが表示されたホームページが表示されます。インターフェイスの右上にある3つの小さな点をクリックしてください。



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



以上です！これでSeedkeeperを使ったパスワードの保存方法はお分かりいただけたと思います。次回のチュートリアルでは、Seedkeeperを使ってBitcoin walletをバックアップする方法をご紹介します。また、SeedSignerとの組み合わせもぜひお試しください：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356