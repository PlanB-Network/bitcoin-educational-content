---
name: Spurv Wallet
description: Installere, konfigurere og bruke Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet er en selvforvaltende Bitcoin-programvare for porteføljeforvaltning utviklet av Craig Raw. Denne programvaren med åpen kildekode er verdsatt av bitcoinere for sine mange funksjoner og intuitive Interface.

Det er to måter å bruke Sparrow på:


- Som en Hot Wallet, der de private nøklene er lagret på PC-en.
- Som en Cold Wallet-administrator, der private nøkler oppbevares på en Hardware Wallet. I denne modusen manipulerer Sparrow bare offentlig Wallet-informasjon, sporer midler, genererer adresser og bygger transaksjoner, men Hardware Wallet-signaturen er nødvendig for å gjøre disse transaksjonene gyldige. Den kan derfor erstatte applikasjoner som Ledger Live eller Trezor Suite.

Sparrow støtter lommebøker med én signatur og flere signaturer, og gjør det mulig å administrere flere lommebøker på en smidig måte. Du kan for eksempel styre en Wallet koblet til en Ledger, en annen til en Trezor, og samtidig ha en Hot Wallet.

Programvaren tilbyr også avanserte funksjoner for myntkontroll, slik at du kan velge nøyaktig hvilke UTXO-er som skal brukes i transaksjonene dine for å optimalisere konfidensialiteten.

Når det gjelder tilkobling, lar Sparrow deg koble deg til din egen Bitcoin-node, enten eksternt via en Electrum Server eller med Bitcoin Core. Det er også mulig å bruke en offentlig node hvis du ennå ikke har din egen. Fjerntilkoblinger gjøres via Tor.

## Installer Sparrow Wallet

Gå til [den offisielle nedlastingssiden for Sparrow Wallet] (https://sparrowwallet.com/download/) og velg programvareversjonen som passer til operativsystemet ditt.

![Image](assets/fr/01.webp)

Det er viktig å kontrollere programvarens integritet og autentisitet før du installerer den. Hvis du ikke vet hvordan du gjør dette, finner du en fullstendig veiledning her :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Når Sparrow er installert, kan du hoppe over de innledende forklaringsskjermene og gå rett til skjermbildet for tilkoblingsadministrasjon.

![Image](assets/fr/02.webp)

## Koble til Bitcoin-nettverket

For å samhandle med Bitcoin-nettverket og kringkaste transaksjonene dine, må Sparrow være koblet til en Bitcoin-node. Det er tre hovedmåter å etablere denne forbindelsen på:


- 🟡 Bruke en offentlig node, dvs. koble til en tredjepartsnode som tillater slike tilkoblinger. Hvis du ikke har din egen Bitcoin-node, kan du komme raskt i gang med Sparrow med dette alternativet. Noden du kobler deg til, vil imidlertid se alle transaksjonene dine, noe som kan gå på bekostning av konfidensialiteten din. Det er viktig å ha kontroll over nøklene dine, men det er enda bedre å ha din egen node. Bruk derfor kun dette alternativet hvis du er nybegynner, og vær klar over risikoen for personvernet ditt.
- 🟢 Koble til en Bitcoin Core-node. Hvis du har din egen Bitcoin Core-node, kan du koble den til Sparrow Wallet, enten lokalt hvis Bitcoin Core er installert på samme maskin, eller eksternt.
- 🔵 Tilkobling via en Electrum-server. Hvis Bitcoin-noden din er utstyrt med Electrum, slik tilfellet er med node-in-a-box-løsninger som Umbrel eller Start9, kan du koble deg til den eksternt fra Sparrow.

**Det er å foretrekke å bruke en tilkobling via Electrs eller Bitcoin Core på din egen node for å redusere behovet for å stole på en tredjepart og optimalisere konfidensialiteten**

### Koble til en offentlig node 🟡

Det er veldig enkelt å koble seg til en offentlig node. Klikk på fanen "*Public Server*".

![Image](assets/fr/03.webp)

Velg en node fra nedtrekkslisten.

![Image](assets/fr/04.webp)

Klikk deretter på "*Test Connection*".

![Image](assets/fr/05.webp)

Når du er tilkoblet, vil Sparrow Wallet vise en gul hake nederst i høyre hjørne av Interface for å indikere at du er koblet til en offentlig node.

![Image](assets/fr/06.webp)

### Tilkobling til en Bitcoin-kjerne 🟢

Den andre metoden for å koble til en Bitcoin-node er å koble Sparrow til en Bitcoin Core. Hvis Bitcoin Core er installert på samme maskin, vil autentiseringen skje via cookie-filen. Hvis Bitcoin Core er på en ekstern maskin, må du bruke passordet som er definert i filen `Bitcoin.conf`.

Vær oppmerksom på at hvis du bruker en beskåret Bitcoin Core-node, vil du ikke kunne gjenopprette en Wallet som inneholder transaksjoner som er eldre enn de lokalt lagrede blokkene. For en ny Wallet opprettet på Sparrow vil dette imidlertid ikke være noe problem: De nye transaksjonene dine vil være synlige, selv med en beskåret node.

For å konfigurere en Bitcoin Core-node kan du se en av følgende veiledninger, avhengig av operativsystemet ditt:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Gå til fanen "*Bitcoin Core*" på Sparrow.

![Image](assets/fr/07.webp)

**Med Bitcoin Core local:**

Hvis Bitcoin Core er installert på datamaskinen din, finner du filen `Bitcoin.conf` blant programvarefilene. Hvis denne filen ikke finnes, kan du opprette den. Åpne den med et tekstredigeringsprogram, og sett inn følgende linje:

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

[hånd]

rpcbind=127.0.0.1

rpcbind=192.168.1.18

rpcallowip=127.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser=loic

rpcpassword=mitt_passord

```