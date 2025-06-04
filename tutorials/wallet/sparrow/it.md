---
name: Passero Wallet
description: Installazione, configurazione e utilizzo di Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet è un software di gestione del portafoglio Bitcoin autocustodito sviluppato da Craig Raw. Questo software open-source è apprezzato dai bitcoiners per le sue numerose funzioni e per l'intuitività del Interface.

Esistono due modi per utilizzare Sparrow:


- Come un Hot Wallet, dove le chiavi private sono memorizzate sul PC.
- Come gestore di Cold Wallet, in cui le chiavi private sono conservate in un Hardware Wallet. In questa modalità, Sparrow manipola solo le informazioni pubbliche Wallet, tiene traccia dei fondi, genera indirizzi e crea transazioni, ma la firma Hardware Wallet è necessaria per rendere valide queste transazioni. Può quindi sostituire applicazioni come Ledger Live o Trezor Suite.

Sparrow supporta portafogli a firma singola e multipla e consente una gestione fluida di più portafogli. Ad esempio, è possibile controllare contemporaneamente un Wallet collegato a un Ledger, un altro a un Trezor e anche un Hot Wallet.

Il software offre anche funzioni avanzate di controllo delle monete, consentendo di scegliere con precisione quali UTXO utilizzare nelle transazioni per ottimizzare la riservatezza.

In termini di connessione, Sparrow consente di collegarsi al proprio nodo Bitcoin, sia in remoto tramite un server Electrum, sia con Bitcoin Core. È anche possibile utilizzare un nodo pubblico se non si ha ancora il proprio. Le connessioni remote vengono effettuate tramite Tor.

## Installare Sparrow Wallet

Andare alla [pagina ufficiale di download di Sparrow Wallet] (https://sparrowwallet.com/download/) e scegliere la versione del software corrispondente al proprio sistema operativo.

![Image](assets/fr/01.webp)

È importante verificare l'integrità e l'autenticità del software prima di installarlo. Se non sapete come fare, qui troverete un tutorial completo:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una volta installato Sparrow, è possibile saltare le schermate esplicative iniziali e passare direttamente alla schermata di gestione della connessione.

![Image](assets/fr/02.webp)

## Collegamento alla rete Bitcoin

Per interagire con la rete Bitcoin e trasmettere le proprie transazioni, Sparrow deve essere connesso a un nodo Bitcoin. Esistono tre modi principali per stabilire questa connessione:


- 🟡 Utilizzando un nodo pubblico, cioè collegandosi a un nodo di terze parti che consente tali connessioni. Se non si dispone di un proprio nodo Bitcoin, questa opzione consente di iniziare rapidamente a utilizzare Sparrow. Tuttavia, il nodo a cui vi connettete vedrà tutte le vostre transazioni, il che potrebbe compromettere la vostra riservatezza. Avere il controllo sulle proprie chiavi è essenziale, ma avere un proprio nodo è ancora meglio. Utilizzate quindi questa opzione solo se siete agli inizi, consapevoli dei rischi per la vostra privacy.
- 🟢 Connessione a un nodo Bitcoin Core. Se si dispone di un nodo Bitcoin Core, è possibile collegarlo a Sparrow Wallet, sia localmente se Bitcoin Core è installato sulla stessa macchina, sia in remoto.
- 🔵 Connessione tramite un server Electrum. Se il nodo Bitcoin è dotato di Electrum, come nel caso di soluzioni node-in-a-box come Umbrel o Start9, è possibile collegarsi ad esso in remoto da Sparrow.

**È preferibile utilizzare una connessione tramite Electrs o Bitcoin Core sul proprio nodo per ridurre la necessità di affidarsi a terzi e ottimizzare la propria riservatezza**

### Connettersi a un nodo pubblico 🟡

La connessione a un nodo pubblico è molto semplice. Fare clic sulla scheda "*Server pubblico*".

![Image](assets/fr/03.webp)

Selezionare un nodo dall'elenco a discesa.

![Image](assets/fr/04.webp)

Quindi fare clic su "*Test Connection*".

![Image](assets/fr/05.webp)

Una volta collegato, Sparrow Wallet visualizzerà un segno di spunta giallo nell'angolo inferiore destro di Interface per indicare che si è connessi a un nodo pubblico.

![Image](assets/fr/06.webp)

### Collegamento a un nucleo Bitcoin 🟢

Il secondo metodo di connessione a un nodo Bitcoin consiste nel collegare Sparrow a un Bitcoin Core. Se il Bitcoin Core è installato sulla stessa macchina, l'autenticazione avverrà tramite il file cookie. Se Bitcoin Core si trova su una macchina remota, è necessario utilizzare la password definita nel file `Bitcoin.conf`.

Si noti che se si utilizza un nodo Bitcoin Core potato, non sarà possibile ripristinare un Wallet contenente transazioni precedenti ai blocchi memorizzati localmente. Tuttavia, per un nuovo Wallet creato su Sparrow, questo non sarà un problema: le nuove transazioni saranno visibili, anche se il nodo è stato tagliato.

Per configurare un nodo Bitcoin Core, è possibile consultare una delle seguenti esercitazioni, a seconda del sistema operativo in uso:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Su Sparrow, andare alla scheda "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Con Bitcoin Core locale:**

Se sul computer è installato Bitcoin Core, individuare il file `Bitcoin.conf` tra i file del software. Se questo file non esiste, è possibile crearlo. Aprirlo con un editor di testo e inserire la seguente riga:

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

[mano]

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