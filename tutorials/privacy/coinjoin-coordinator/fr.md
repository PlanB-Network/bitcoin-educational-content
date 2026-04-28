---
name: Coordinateur Coinjoin - WabiSabi
description: Comment mettre en place et faire fonctionner un coordinateur de coinjoin en suivant le protocole WabiSabi (utilisé dans Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Introduction 👋


Dans ce guide d'expert, nous allons vous aider à mettre en place un coordinateur coinjoin, essentiellement un serveur qui rassemble les personnes qui veulent économiser sur les frais de transaction ou augmenter leur confidentialité sur la chaîne dans des transactions collaboratives. Puisqu'il n'y a plus de coordinateur géré par une société et fourni avec Wasabi Wallet, les utilisateurs doivent trouver et sélectionner leur propre serveur de coordinateur. Seuls quelques coordinateurs se sont manifestés en demandant des frais de coordination de 0%, c'est pourquoi les développeurs de Wasabi Wallet ont travaillé dur pour rendre aussi facile que possible la gestion de votre propre coordinateur communautaire (sur un matériel aussi petit qu'un Raspberry Pi5 !). Les coordinateurs actuellement actifs qui demandent 0% de frais de coordination peuvent être trouvés sur [LiquiSabi](https://liquisabi.com) et plus important encore sur [nostr](https://github.com/Kukks/WasabiNostr).


## Exigences 🫴



- VPS (nœud hébergé) ou ordinateur/serveur (nœud auto-hébergé)
- Nœud Bitcoin Core élagué/complet (testé avec v29.0)


En option :


- (sous-)domaine transférant le trafic vers le nœud (par exemple, coinjoin.[yourdomain].io)


Il est recommandé d'avoir une certaine expérience des invites de ligne de commande et de bash, car toutes les étapes ne peuvent pas être automatisées.


Du point de vue matériel, il est conseillé d'avoir un système avec :


- 4 cœurs
- 16 GO DE RAM
- 2 TB SSD ou NVMe (pour un nœud complet) / 128 GB SSD (pour un nœud pruned)


De telles exigences peuvent être satisfaites par un Raspberry Pi 5 pour seulement 120 $, sans compter le stockage qui coûte environ 100 $ pour une clé NVMe de 2 To.


Les VPS bon marché sont généralement équipés d'un seul cœur et de 4 Go de RAM, ce qui est trop peu pour synchroniser et vérifier l'intégralité du bitcoin blockchain à la hauteur du bloc 911817.


En ce qui concerne le stockage, un nœud complet nécessitera au minimum 2 To de disque de stockage, de préférence de type SSD ou NVMe. Lors de l'élagage du blockchain, un disque de stockage beaucoup plus petit est acceptable (par exemple, un SSD de 128 Go).


Si vous avez l'intention d'utiliser un coordinateur pour des coinjoins de grande taille (plus de 300 entrées), il est conseillé de choisir un système doté de cœurs plus rapides ou plus récents, plus performants pour toutes les vérifications de signatures.


## Installation 🛠️


Sur le nœud, nous voulons télécharger et installer la dernière version de Wasabi Wallet, qui comprend un backend et un coordinateur sous forme d'exécutables autonomes à côté de wallet.


Trouvez la dernière version : [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) et vérifiez la signature PGP de la version avec les clés : [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Les détails du déploiement diffèrent en fonction du matériel (architecture CPU) et du choix du système d'exploitation. Ci-dessous, les différents détails sont donnés pour un Raspberry Pi (ARM-64) avec le RaspiBlitz basé sur le Debian comme point de départ. Passez à la suite pour le déploiement du système d'exploitation Ubuntu (X86-64) en utilisant Nix.


Vous trouverez les instructions d'installation ici : [Wasabi Docs] (https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Déploiement de RaspiBlitz/Debian


Pour les nœuds RaspiBlitz (testés avec la version 1.11), un déploiement script à partir du code source peut être utilisé : [home.admin/config.scripts/bonus.wasabi.sh] (https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Déploiement facile


Pour un déploiement minimal, il suffit d'extraire les exécutables pour votre plateforme dans un dossier.

Exemple de codes de ligne de commande pour Debian/Ubuntu :


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Il devrait en résulter le message de signature valide suivant :


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Vous pouvez ensuite procéder à l'installation du paquet téléchargé :


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Configuration 🧾


Avant de lancer le coordinateur, vous devez éditer le fichier Config.json avec votre :


- Bitcoin RPC Références
- Paramètres préférés de la ronde
- Clé publique étendue du coordinateur (création d'un nouveau SegWit wallet pour la réception des poussières collectées)

**Avertissement** : Taproot wallet se traduira par des UTXO non dépensables ! Utilisez une wallet Segwit native ici.


- Types d'adresses d'entrée et de sortie autorisés
- Configuration de l'annonceur pour la publication sur nostr (nom, description, Uri, entrées minimales, relais nostr, clé privée nostr)


Vous pouvez faire fonctionner le coordinateur accessible uniquement via l'adresse .onion, ou utiliser votre domaine clearnet personnalisé.


Rechercher ou créer le fichier de configuration sur ce chemin :


`~/.walletwasabi/coordinator/Config.json`


Modifiez-le à l'aide de la commande :


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Voir cet exemple Config.json :


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Configuration de la Tor 🧅


Pour remplir votre OnionServicePrivateKey, vous devrez probablement en générer une au préalable.


Wasabi Wallet générera une clé privée pour vous si vous l'exécutez la première fois avec ``"PublishAsOnionService" : true,`` défini dans le fichier Config.json.


Exécutez le coordinateur une fois avec la commande :


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Pour connaître l'adresse de votre service caché Onion, vérifiez les journaux du coordinateur avec :


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


et vous trouverez quelque chose comme :


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


L'URL longue se terminant par .onion est votre adresse de service cachée ou CoordinatorUri.


Ou vérifiez à nouveau votre fichier de configuration du coordinateur avec :


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Qui devrait être automatiquement remplie à présent.


## Course à pied ⚡


Une fois que tous les paramètres de configuration ont été définis, vous pouvez lancer le service de coordination et commencer à annoncer votre premier tour 🕶️


Il suffit de lancer le coordinateur avec la commande :


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Vous pouvez suivre le tour en cours et le nombre de UTXO/de pièces enregistrés en vérifiant (dans le navigateur Tor pour .onion) :


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Facultatif : débogage du serveur du coordinateur


Vous pouvez surveiller les problèmes ou les erreurs dans le fichier journal à ``~/.walletwasabi/backend/Logs.txt``


Les problèmes typiques incluent les problèmes de connexion RPC, qui doivent être activés dans ``~/.bitcoin/bitcoin.conf`` avec :


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Optionnel : Exécution du serveur backend


Avec le coordinateur, vous pouvez également fournir un serveur dorsal aux utilisateurs qui ne disposent pas de leur propre nœud bitcoin, auquel ils peuvent se connecter pour obtenir des estimations de frais et des filtres de blocs.


Démarrez ce service à l'aide de la commande :


```
wbackend
```


## Inviter des utilisateurs de Wasabi à votre coordinateur 🫂


Pour que d'autres utilisateurs trouvent votre service, vous pouvez compter sur l'annonceur de nostr, ou partager un lien magique avec votre domaine (clearnet) ou votre service caché (lien .onion) et arrondir les paramètres comme ceci :


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Lorsqu'un utilisateur copie le lien magique et ouvre son Wasabi Wallet, le logiciel affichera automatiquement le dialogue du coordinateur avec votre domaine et vos paramètres.


![detected](assets/en/02.webp)


💚🍣 Félicitations pour la décentralisation de la confidentialité du bitcoin 🕶️


N'oubliez pas votre entraînement [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet est réservé à la défense 🛡️