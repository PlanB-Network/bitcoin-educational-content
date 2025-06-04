---
name: Sparrow Wallet
description: Installing, configuring and using Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet is a self-custody Bitcoin portfolio management software developed by Craig Raw. This open-source software is appreciated by bitcoiners for its many features and intuitive Interface.

There are two ways to use Sparrow:


- Like a hot wallet, where your private keys are stored on your PC.
- As a cold wallet manager, where private keys are held on a Hardware Wallet. In this mode, Sparrow only manipulates public wallet information, tracks funds, generates addresses, and builds transactions, but the Hardware Wallet signature is required to make these transactions valid. It can therefore replace applications such as Ledger Live or Trezor Suite.

Sparrow supports single-signature and multi-signature wallets, and enables fluid management of multiple wallets. For example, you can simultaneously control one wallet connected to a Ledger, another to a Trezor, and also have a hot wallet.

The software also offers advanced coin control features, allowing you to choose precisely which UTXOs to use in your transactions to optimize your confidentiality.

In terms of connection, Sparrow lets you connect to your own Bitcoin node, either remotely via an Electrum Server, or with Bitcoin Core. It's also possible to use a public node if you don't yet have your own. Remote connections are made via Tor.

## Install Sparrow Wallet

Go to [the official Sparrow Wallet download page](https://sparrowwallet.com/download/) and choose the software version that corresponds to your operating system.

![Image](assets/fr/01.webp)

It's important to check the integrity and authenticity of the software before installing it. If you don't know how to do this, you'll find a complete tutorial here :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Once Sparrow has been installed, you can skip the initial explanatory screens and go straight to the connection management screen.

![Image](assets/fr/02.webp)

## Connecting to the Bitcoin network

To interact with the Bitcoin network and broadcast your transactions, Sparrow must be connected to a Bitcoin node. There are three main ways to establish this connection:


- 🟡 Using a public node, i.e. connecting to a third-party node that allows such connections. If you don't have your own Bitcoin node, this option lets you get started with Sparrow quickly. However, the node you connect to will see all your transactions, which could compromise your confidentiality. Having control over your keys is essential, but having your own node is even better. So use this option only if you're just starting out, while being aware of the risks to your privacy.
- 🟢 Connecting to a Bitcoin Core node. If you have your own Bitcoin Core node, you can connect it to Sparrow Wallet, either locally if Bitcoin Core is installed on the same machine, or remotely.
- 🔵 Connection via an Electrum server. If your Bitcoin node is equipped with Electrs, as is the case with node-in-a-box solutions such as Umbrel or Start9, you can connect to it remotely from Sparrow.

**It is preferable to use a connection via Electrs or Bitcoin Core on your own node to reduce the need to trust a third party and optimize your confidentiality**

### Connect to a public node 🟡

Connecting to a public node is very simple. Click on the "*Public Server*" tab.

![Image](assets/fr/03.webp)

Select a node from the drop-down list.

![Image](assets/fr/04.webp)

Then click on "*Test Connection*".

![Image](assets/fr/05.webp)

Once connected, Sparrow Wallet will display a yellow tick in the bottom right-hand corner of Interface to indicate that you are connected to a public node.

![Image](assets/fr/06.webp)

### Connecting to a Bitcoin Core 🟢

The second method of connecting to a Bitcoin node is to link Sparrow to a Bitcoin Core. If Bitcoin Core is installed on the same machine, authentication will be via the cookie file. If Bitcoin Core is on a remote machine, you'll need to use the password defined in the `Bitcoin.conf` file.

Please note that if you use a pruned Bitcoin Core node, you won't be able to restore a wallet containing transactions predating the locally stored blocks. However, for a new wallet created on Sparrow, this won't be a problem: your new transactions will be visible, even with a pruned node.

To configure a Bitcoin Core node, you can consult one of the following tutorials, depending on your operating system:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
On Sparrow, go to the "*Bitcoin Core*" tab.

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

If Bitcoin Core is installed on your computer, locate the `Bitcoin.conf` file among the software files. If this file does not exist, you can create it. Open it with a text editor and insert the following line:

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

[hand]

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