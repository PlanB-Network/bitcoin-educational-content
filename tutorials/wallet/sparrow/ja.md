---
name: スズメ Wallet
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

*Bitcoinコア・ローカル使用時：***。

Bitcoin Coreがインストールされている場合は、ソフトウェアファイルの中から`Bitcoin.conf`ファイルを探します。このファイルが存在しない場合は、作成することができます。テキストエディタで開き、以下の行を挿入してください：

```ini
server=1
````
Sauvegardez ensuite vos modifications.
Vous pouvez également effectuer cette configuration via l'interface graphique de Bitcoin-QT en naviguant dans "*Settings*" > "*Options...*" et en activant l'option "*Enable RPC server*".
N'oubliez pas de redémarrer le logiciel après ces modifications.
![Image](assets/fr/08.webp)
Revenez ensuite à Sparrow Wallet et renseignez le chemin vers votre fichier de cookie, généralement situé dans le même dossier que le `bitcoin.conf`, selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
![Image](assets/fr/09.webp)
Laissez les autres paramètres par défaut, l'URL `127.0.0.1` et le port `8332`, puis cliquez sur "*Test Connection*".
![Image](assets/fr/10.webp)
La connexion est établie. Une coche verte apparaîtra en bas à droite pour indiquer que vous êtes connecté à un nœud Bitcoin Core.
![Image](assets/fr/11.webp)
**Avec Bitcoin Core à distance :**
Si Bitcoin Core est installé sur une autre machine connectée sur le même réseau, commencez par localiser le fichier `bitcoin.conf` parmi les fichiers du logiciel. Si ce fichier n'existe pas encore, vous pouvez le créer. Ouvrez ce fichier avec un éditeur de texte et ajoutez la ligne suivante :
```

server=1

```
Après avoir modifié le fichier, assurez-vous de l'enregistrer dans le dossier approprié selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
Il est également possible de réaliser cette manipulation via l'interface graphique de Bitcoin-QT. Accédez au menu "*Settings*", puis "*Options...*", et activez l'option "*Enable RPC server*" en cochant la case correspondante. Si le fichier `bitcoin.conf` n'existe pas, vous pouvez le créer directement depuis cette interface en cliquant sur "*Open Configuration File*".
![Image](assets/fr/12.webp)
Trouvez l'adresse IP de la machine qui héberge Bitcoin Core dans votre réseau local. Pour cela, vous pouvez utiliser un outil tel que [Angry IP Scanner](https://angryip.org/). Supposons, pour l'exemple, que l'adresse IP de votre nœud soit `192.168.1.18`.
Dans le fichier `bitcoin.conf`, ajoutez les lignes suivantes, en configurant `rpcbind=192.168.1.18` pour correspondre à l'adresse IP de votre nœud.
```

[手]

rpcbind=127.0.0.1

rpcbind=192.168.1.18

rpcallowip=127.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser=loic

rpcpassword=my_password

```