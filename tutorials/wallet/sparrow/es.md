---
name: Gorrión Wallet
description: Instalación, configuración y uso de Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet es un software de gestión de carteras Bitcoin de autocustodia desarrollado por Craig Raw. Este software de código abierto es apreciado por los bitcoiners por sus numerosas funciones y su Interface intuitivo.

Hay dos formas de utilizar Sparrow:


- Como una Hot Wallet, donde sus claves privadas se almacenan en su PC.
- Como gestor de Cold Wallet, donde las claves privadas se mantienen en un Hardware Wallet. En este modo, Sparrow sólo manipula información pública de Wallet, rastrea fondos, genera direcciones y construye transacciones, pero la firma de Hardware Wallet es necesaria para que estas transacciones sean válidas. Por tanto, puede sustituir a aplicaciones como Ledger Live o Trezor Suite.

Sparrow soporta monederos de firma única y multi-firma, y permite una gestión fluida de múltiples monederos. Por ejemplo, puedes controlar simultáneamente una Wallet conectada a una Ledger, otra a un Trezor, y tener también una Hot Wallet.

El software también ofrece funciones avanzadas de control de monedas, que le permiten elegir con precisión qué UTXO utilizar en sus transacciones para optimizar su confidencialidad.

En términos de conexión, Sparrow te permite conectarte a tu propio nodo Bitcoin, ya sea remotamente a través de un Servidor Electrum, o con Bitcoin Core. También es posible usar un nodo público si aún no tienes uno propio. Las conexiones remotas se realizan a través de Tor.

## Instalar Sparrow Wallet

Vaya a [la página oficial de descarga de Sparrow Wallet](https://sparrowwallet.com/download/) y elija la versión de software que corresponda a su sistema operativo.

![Image](assets/fr/01.webp)

Es importante comprobar la integridad y autenticidad del software antes de instalarlo. Si no sabes cómo hacerlo, encontrarás un completo tutorial aquí :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Una vez instalado Sparrow, puedes saltarte las pantallas explicativas iniciales e ir directamente a la pantalla de gestión de la conexión.

![Image](assets/fr/02.webp)

## Conexión a la red Bitcoin

Para interactuar con la red Bitcoin y transmitir sus transacciones, Sparrow debe estar conectado a un nodo Bitcoin. Hay tres formas principales de establecer esta conexión:


- 🟡 Utilizando un nodo público, es decir, conectándote a un nodo de terceros que permita este tipo de conexiones. Si no tienes tu propio nodo Bitcoin, esta opción te permite empezar a usar Sparrow rápidamente. Sin embargo, el nodo al que te conectes verá todas tus transacciones, lo que podría comprometer tu confidencialidad. Tener control sobre tus claves es esencial, pero tener tu propio nodo es aún mejor. Así que utiliza esta opción sólo si estás empezando, siendo consciente de los riesgos para tu privacidad.
- 🟢 Conexión a un nodo Bitcoin Core. Si tienes tu propio nodo Bitcoin Core, puedes conectarlo a Sparrow Wallet, ya sea localmente si Bitcoin Core está instalado en la misma máquina, o remotamente.
- 🔵 Conexión a través de un servidor Electrum. Si tu nodo Bitcoin está equipado con Electrs, como es el caso de las soluciones node-in-a-box como Umbrel o Start9, puedes conectarte a él remotamente desde Sparrow.

**Es preferible utilizar una conexión a través de Electrs o Bitcoin Core en su propio nodo para reducir la necesidad de confiar en un tercero y optimizar su confidencialidad**

### Conectarse a un nodo público 🟡

Conectarse a un nodo público es muy sencillo. Haz clic en la pestaña "*Servidor público*".

![Image](assets/fr/03.webp)

Seleccione un nodo de la lista desplegable.

![Image](assets/fr/04.webp)

A continuación, haga clic en "*Probar conexión*".

![Image](assets/fr/05.webp)

Una vez conectado, Sparrow Wallet mostrará una marca amarilla en la esquina inferior derecha de Interface para indicar que estás conectado a un nodo público.

![Image](assets/fr/06.webp)

### Conexión a un Bitcoin Core 🟢

El segundo método para conectarse a un nodo Bitcoin es vincular Sparrow a un Bitcoin Core. Si el Bitcoin Core está instalado en la misma máquina, la autenticación será a través del archivo cookie. Si Bitcoin Core está en una máquina remota, necesitará usar la contraseña definida en el archivo `Bitcoin.conf`.

Ten en cuenta que si utilizas un nodo Core Bitcoin podado, no podrás restaurar un Wallet que contenga transacciones anteriores a los bloques almacenados localmente. Sin embargo, para una nueva Wallet creada en Sparrow, esto no será un problema: tus nuevas transacciones serán visibles, incluso con un nodo podado.

Para configurar un nodo Bitcoin Core, puede consultar uno de los siguientes tutoriales, en función de su sistema operativo:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
En Sparrow, vaya a la pestaña "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Con Bitcoin Core local:**

Si Bitcoin Core está instalado en su ordenador, localice el archivo `Bitcoin.conf` entre los archivos de software. Si este archivo no existe, puede crearlo. Ábralo con un editor de texto e inserte la siguiente línea:

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

servidor=1

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

rpcpassword=mi_contraseña

```