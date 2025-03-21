---
name: Pardal Wallet
description: Instalação, configuração e utilização do Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet é um software de gerenciamento de portfólio Bitcoin de autocustódia desenvolvido por Craig Raw. Este software de código aberto é apreciado pelos bitcoiners pelas suas muitas funcionalidades e Interface intuitivo.

Existem duas formas de utilizar o Sparrow:


- Como um Hot Wallet, em que as suas chaves privadas são armazenadas no seu PC.
- Como um gestor Cold Wallet, onde as chaves privadas são mantidas num Hardware Wallet. Neste modo, o Sparrow apenas manipula informações públicas do Wallet, rastreia fundos, gera endereços e cria transacções, mas a assinatura Hardware Wallet é necessária para tornar estas transacções válidas. Por conseguinte, pode substituir aplicações como o Ledger Live ou o Trezor Suite.

O Sparrow suporta carteiras de assinatura única e carteiras de assinatura múltipla e permite a gestão fluida de várias carteiras. Por exemplo, pode controlar simultaneamente um Wallet ligado a um Ledger, outro a um Trezor, e também ter um Hot Wallet.

O software também oferece funcionalidades avançadas de controlo de moedas, permitindo-lhe escolher com precisão quais os UTXOs a utilizar nas suas transacções para otimizar a sua confidencialidade.

Em termos de ligação, o Sparrow permite-lhe ligar-se ao seu próprio nó Bitcoin, quer remotamente através de um servidor Electrum, quer com o Bitcoin Core. Também é possível usar um nó público se ainda não tiveres o teu próprio nó. As conexões remotas são feitas via Tor.

## Instalar o Sparrow Wallet

Aceda à [página oficial de transferência do Sparrow Wallet] (https://sparrowwallet.com/download/) e escolha a versão do software que corresponde ao seu sistema operativo.

![Image](assets/fr/01.webp)

É importante verificar a integridade e a autenticidade do software antes de o instalar. Se não sabe como o fazer, encontrará um tutorial completo aqui :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Uma vez instalado o Sparrow, pode saltar os ecrãs explicativos iniciais e ir diretamente para o ecrã de gestão da ligação.

![Image](assets/fr/02.webp)

## Ligação à rede Bitcoin

Para interagir com a rede Bitcoin e transmitir as suas transacções, o Sparrow deve estar ligado a um nó Bitcoin. Existem três formas principais de estabelecer esta ligação:


- usando um nó público, ou seja, conectando-se a um nó de terceiros que permite tais conexões. Se não tiver o seu próprio nó Bitcoin, esta opção permite-lhe começar a utilizar o Sparrow rapidamente. No entanto, o nó ao qual se liga verá todas as suas transacções, o que pode comprometer a sua confidencialidade. Ter controlo sobre as suas chaves é essencial, mas ter o seu próprio nó é ainda melhor. Por isso, use esta opção apenas se estiver a começar, tendo em conta os riscos para a sua privacidade.
- conectando a um nó Bitcoin Core. Se tiver o seu próprio nó Bitcoin Core, pode ligá-lo ao Sparrow Wallet, quer localmente, se o Bitcoin Core estiver instalado na mesma máquina, quer remotamente.
- ligação através de um servidor Electrum. Se o seu nó Bitcoin estiver equipado com Electrum, como é o caso das soluções node-in-a-box como o Umbrel ou o Start9, pode ligar-se a ele remotamente a partir do Sparrow.

**É preferível utilizar uma ligação via Electrs ou Bitcoin Core no seu próprio nó para reduzir a necessidade de confiar em terceiros e otimizar a sua confidencialidade**

### Ligar a um nó público 🟡

A ligação a um nó público é muito simples. Clique no separador "*Servidor público*".

![Image](assets/fr/03.webp)

Selecione um nó na lista pendente.

![Image](assets/fr/04.webp)

Em seguida, clique em "*Testar ligação*".

![Image](assets/fr/05.webp)

Uma vez ligado, o Sparrow Wallet apresentará um visto amarelo no canto inferior direito do Interface para indicar que está ligado a um nó público.

![Image](assets/fr/06.webp)

### Ligação a um núcleo Bitcoin 🟢

O segundo método de ligação a um nó Bitcoin é ligar o Sparrow a um Bitcoin Core. Se o Bitcoin Core estiver instalado na mesma máquina, a autenticação será feita através do arquivo cookie. Se o Bitcoin Core estiver em uma máquina remota, será necessário utilizar a senha definida no arquivo `Bitcoin.conf`.

Por favor, note que se você usar um nó Bitcoin Core podado, você não será capaz de restaurar um Wallet contendo transações anteriores aos blocos armazenados localmente. No entanto, para um novo Wallet criado no Sparrow, isso não será um problema: suas novas transações serão visíveis, mesmo com um nó podado.

Para configurar um nó Bitcoin Core, pode consultar um dos seguintes tutoriais, dependendo do seu sistema operativo:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
No Sparrow, aceda ao separador "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Com o Bitcoin Core local:**

Se o Bitcoin Core estiver instalado no seu computador, localize o ficheiro `Bitcoin.conf` entre os ficheiros de software. Se esse arquivo não existir, é possível criá-lo. Abra-o com um editor de texto e insira a seguinte linha:

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

[mão]

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