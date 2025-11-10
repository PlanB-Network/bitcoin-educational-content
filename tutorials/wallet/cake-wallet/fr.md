---
name: Gâteau Wallet
description: Tutoriel sur le Cake Wallet et les paiements silencieux
---

![cover](assets/cover.webp)


Ce guide explore [**Cake Wallet**](https://cakewallet.com/) : un wallet open-source, non conservateur, axé sur la confidentialité et multi-devises, disponible pour Android, iOS, macOS, Linux et Windows. Nous nous pencherons sur les fonctionnalités de confidentialité propres à Bitcoin, sur l'envoi et la réception de Bitcoin via **Silent Payments** (un protocole de confidentialité on-chain amélioré) et sur l'implémentation de PayJoin v2 pour les transactions asynchrones.


## 🎉 Caractéristiques principales



- les [**Paiements silencieux (BIP-352)**](https://bips.dev/352/) améliorent les précédents [codes de paiement BIP 47](https://silentpayments.xyz/docs/comparing-proposals/bip47/), également appelés "PayNyms", grâce à des adresses furtives réutilisables. Lorsqu'un expéditeur utilise votre adresse de paiement silencieux, son wallet dérive une adresse unique à usage unique à l'aide de différentes clés qui seront combinées en une adresse unique à usage unique Taproot. Les enregistrements de la blockchain montrent des transactions non liées, ce qui empêche de relier les paiements entrants. Les paiements silencieux offrent toute une série d'avantages, notamment
    - Adresses réutilisables : Il n'est pas nécessaire d'utiliser une nouvelle adresse generate pour chaque transaction, ce qui améliore l'expérience de l'utilisateur et la protection de la vie privée
    - Aucune augmentation des coûts : Les paiements silencieux n'augmentent ni la taille ni le coût des transactions.
    - Anonymat renforcé : Les observateurs extérieurs ne peuvent pas relier les transactions à une adresse de paiement silencieux.
    - Aucune interaction entre l'expéditeur et le destinataire n'est nécessaire : Les transactions peuvent être effectuées sans aucune communication entre les parties.
    - Des adresses uniques pour chaque paiement : Élimination du risque de réutilisation accidentelle des adresses.
    - Aucun serveur n'est nécessaire : Les paiements silencieux peuvent être effectués sans nécessiter de serveur dédié.
- PayJoin v2** atténue l'analyse du graphe des transactions en fusionnant les entrées des expéditeurs et des destinataires en une seule transaction. Le gâteau Wallet met en œuvre deux avancées essentielles :
    - Transactions asynchrones** : L'expéditeur et le destinataire n'ont plus besoin d'être en ligne simultanément pour effectuer une transaction privée.
    - Communication sans serveur** : Aucune des parties n'a besoin de faire fonctionner un serveur Payjoin, ce qui élimine un obstacle technique majeur.
- Le contrôle de la Coin** permet de sélectionner manuellement la UTXO pendant les transactions. Cela permet d'éviter une liaison accidentelle des adresses lors de l'utilisation de plusieurs UTXO d'origines différentes.
- Prise en charge de TOR**, permettant aux utilisateurs d'acheminer leur trafic réseau via le réseau Tor
- RBF** (Replace-By.Fee) vous permet d'ajuster les frais après l'envoi d'une transaction.


## 1️⃣ Installation de votre Wallet


Cake Wallet offre un large éventail de plateformes. Vous pouvez choisir entre `Android`, `iOS / macOS`, `Linux` et `Windows`.  Pour commencer, visitez https://docs.cakewallet.com/get-started/ et sélectionnez votre système d'exploitation.


![image](assets/en/01.webp)


Après l'installation, attribuez un `PIN` (4 ou 6 chiffres). Vous verrez alors :


1. `Créer un nouveau Wallet` (pour les nouveaux utilisateurs)

2. `Restore Wallet` (pour les portefeuilles existants)


![image](assets/en/02.webp)


Sur l'écran suivant, vous pouvez choisir parmi une large gamme de crypto-monnaies. Sélectionnez `Bitcoin` et tapez sur `Suivant` et fournissez un `nom Wallet` pour identifier le wallet. En tapant sur "Paramètres avancés", une série de "Paramètres de confidentialité" apparaît. Effectuez ces changements :



- Fiat API:** sélectionner `Tor Only` (achemine les demandes de prix via Tor)
- Swap:** sélectionner `Tor Only` (anonymisation du trafic d'échange)


Le type BIP-39 seed est généré par défaut, avec une option pour passer au type Electrum seed. Les chemins de dérivation sont les suivants :



- Electrum : `m/0'`
- BIP-39 : `m/84'/0'/0`


Si vous souhaitez ajouter une couche de sécurité supplémentaire, vous pouvez mettre en place une "passphrase".  L'objectif principal d'une passphrase est de fournir une protection supplémentaire contre les attaques physiques. Même si un attaquant trouve la phrase seed, il ne peut pas accéder à votre wallet sans la passphrase correcte. En d'autres termes, la phrase seed représente à elle seule une wallet, tandis que la phrase seed plus la passphrase créent une wallet entièrement différente, sans aucun lien avec l'originale. Cette fonction permet également de créer des "portefeuilles secrets" protégés par la passphrase, et vous donne la possibilité de nier l'existence de la wallet. Dans une situation de coercition, vous pourriez révéler la phrase seed tout en gardant des actifs plus importants en sécurité dans le wallet protégé par la passphrase.


Si vous utilisez déjà votre propre nœud, cochez `Add New Custom Node` et fournissez votre `Node Address` pour valider les transactions et les blocs au sein de votre propre infrastructure. Une fois terminé, tapez sur `Continue` et `Next` pour créer votre wallet.


![image](assets/en/03.webp)


L'écran suivant contient une clause de non-responsabilité :


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Pour connaître les meilleures pratiques en matière de sauvegarde de votre phrase mnémotechnique, veuillez consulter ce tutoriel :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Appuyez sur "Je comprends. Montrez-moi ma seed` et sauvegardez ces mots dans un endroit sûr ! Tapez ensuite sur `Vérifier seed` et après vérification `Ouvrir Wallet`.


## 2️⃣ Paramètres


Avant d'aller plus loin, jetons un coup d'œil à l'"écran d'accueil" et aux "réglages".


L'écran d'accueil affiche différents éléments :



- le `menu hamburger` nous amène aux `réglages`
- Solde disponible
- Silent Payments Card pour commencer à scanner les transactions envoyées à votre adresse Silent Payment
- La carte Payjoin permet d'activer Payjoin pour préserver la vie privée et économiser des frais
- en bas, il y a des raccourcis vers `Wallet Overview`, `Receive`, `Swap` entre Bitcoin et d'autres devises, `Send` et `Buy`


![image](assets/en/11.webp)


En tapant sur l'icône "menu hamburger", vous ouvrez le menu des paramètres. Passons en revue les options.


![image](assets/en/05.webp)


### A - Connection & sync 🔗


Ici, nous pouvons reconnecter le wallet, gérer les nœuds et nous connecter à notre propre nœud (recommandé). L'option `Silent Payments Scanning` nous permet de personnaliser l'analyse en spécifiant soit `Scan from block height` (analyse à partir de la hauteur du bloc) soit `Scan from date` (analyse à partir de la date).


![image](assets/en/06.webp)


En tant que fonction "alpha", il y a aussi l'option "Activer Tor intégré" pour acheminer le trafic à travers le réseau Tor.


### B - Paramètres des paiements silencieux 🔈


Il est possible d'activer la carte Paiements silencieux sur l'écran d'accueil pour afficher cette fonction. L'activation de la fonction "Toujours scanner" permet au wallet de surveiller en permanence la blockchain pour détecter les paiements silencieux entrants. Nous pouvons spécifier des paramètres de balayage pour adapter le processus de balayage à nos besoins, comme décrit ci-dessus.


![image](assets/en/07.webp)


### C - Sécurité et sauvegarde 🗝️


Pour sécuriser notre wallet, nous pouvons créer une sauvegarde en suivant les instructions de l'application. Cela nous permettra d'avoir une copie sûre de nos clés privées et de récupérer notre wallet en cas de perte ou de vol. De plus, nous pouvons voir notre phrase seed et nos clés privées, changer notre PIN, activer l'authentification biométrique, Signer / Vérifier et configurer 2FA pour un niveau de protection supplémentaire.


![image](assets/en/08.webp)


**Note** : À partir de septembre 2025, l'authentification biométrique par empreinte digitale sur les appareils Android devra fonctionner avec au moins une implémentation biométrique de classe 2. Pour plus de détails, voir [ici] (https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Toutefois, cette exigence pourrait changer à l'avenir.


### D - Paramètres de confidentialité 🔒


Nous pouvons également améliorer la sécurité de notre wallet en utilisant Tor pour crypter notre connexion Internet et protéger notre vie privée lorsque nous accédons à des sources externes. De plus, nous pouvons empêcher les captures d'écran pour garder nos informations wallet confidentielles, activer les adresses auto-générées pour en créer de nouvelles à chaque transaction, et désactiver les actions d'achat/vente pour empêcher les transactions non autorisées. De plus, nous pouvons "Activer PayJoin", qui est une autre fonction de confidentialité que nous examinerons plus tard.


![image](assets/en/09.webp)


### E - Autres réglages 🔧


D'autres paramètres nous permettent de gérer la priorité des frais et de définir le niveau de frais par défaut pour nos transactions. Cela nous permet de contrôler les frais de transaction associés à nos paiements silencieux, en tenant compte de l'utilisation actuelle du réseau.


![image](assets/en/10.webp)


## 3️⃣ Recevoir des ₿itcoins en utilisant Silent Payments


Il y a plusieurs options et types d'adresses disponibles pour recevoir Bitcoin. `Segwit (P2WPKH)` *(commençant par bc1q....)* est l'option par défaut.  Dans cet exemple, sélectionnons "Paiements silencieux".


Pour recevoir un paiement silencieux, appuyez d'abord sur l'icône "Recevoir" dans Cake Wallet. Ensuite, entrez le montant que vous attendez de recevoir. Pour spécifier le type d'adresse, tapez à nouveau sur "Recevoir" en haut de l'écran, puis sélectionnez "Paiements silencieux" dans les options.


Sur l'écran principal, votre code QR réutilisable Silent Payment et votre adresse s'affichent. Comme prévu, l'adresse est assez longue :


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Maintenant, utilisez un wallet compatible BIP-352 (tel que le Blue Wallet) pour scanner ce code QR et envoyer le paiement. Vous verrez que le wallet dérive une adresse de destination unique de votre adresse silencieuse.


![image](assets/en/13.webp)


## 4️⃣ Envoyer des ₿itcoins avec Silent Payments


Comme la Blue Wallet ne peut qu'"envoyer" des paiements silencieux, nous utiliserons une autre BIP 352 compatible wallet comme partie réceptrice. Ce processus est identique à celui d'une transaction Bitcoin normale.



- Tapez sur "Envoyer" sur l'écran d'accueil
- soit en collant notre adresse réutilisable `sp1qq...`, soit en scannant le code QR directement dans l'application.
- Sélectionnez le montant que vous souhaitez dépenser à partir de votre solde disponible
- Tapez sur "Envoyer" en bas de l'écran pour confirmer la transaction


Une fois que nous avons saisi l'adresse `sp1qq...`, le wallet dérive automatiquement une adresse Taproot correspondante `bc1p...` (P2TR) en arrière-plan, qui sera utilisée pour le paiement silencieux.


Nous avons la possibilité de rédiger une note interne pour chaque transaction, d'ajuster les paramètres de frais ou de sélectionner certaines UTXO pour la transaction à l'aide de la fonction `Coin Control`.


![image](assets/en/14.webp)


glissez-vous vers la droite pour confirmer la transaction.


Une fois la transaction envoyée, il vous sera demandé si vous souhaitez ajouter ce contact à votre carnet d'adresses.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Voyons ce qu'est le PayJoin (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin) :


payjoin v2 est une fonction de préservation de la vie privée et de réduction des frais dans Bitcoin qui permet à l'expéditeur et au destinataire d'une transaction de travailler ensemble pour créer une seule transaction. Cette transaction provient *à la fois* de l'expéditeur et du destinataire, ce qui permet de briser les techniques de surveillance les plus courantes contre la Bitcoin et de permettre une meilleure mise à l'échelle et des économies de frais dans certaines circonstances également


Pour en savoir plus sur PayJoin, vous pouvez également consulter le tutoriel suivant.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Pour utiliser la PayJoin, les deux parties ont besoin d'une wallet compatible avec la PayJoin, et le destinataire doit avoir au moins une pièce ou une sortie dans sa wallet. Pour commencer, veuillez suivre les étapes suivantes :


1. Tapez sur le "Menu hamburger" et tapez sur le bouton "Confidentialité"

2. Basculer l'option `Use Payjoin` (utiliser Payjoin)

3.  Tapez sur "Recevoir" sur l'écran d'accueil et vous verrez apparaître un code QR PayJoin et un bouton de copie (si vous avez sélectionné Segwit)


![image](assets/en/16.webp)


## 6️⃣ Autres caractéristiques


Il existe d'autres fonctionnalités comme les échanges multidevises, les options d'achat et de vente avec les connexions de différents vendeurs et les programmes spécifiques à Cake, comme "Cake Pay", qui vous permet d'acheter des cartes prépayées ou des cartes-cadeaux.


![image](assets/en/17.webp)


## 🎯 Conclusion


Voici notre avis sur le Cake Wallet, qui offre une protection pratique de la confidentialité Bitcoin grâce à des fonctions telles que les paiements silencieux (BIP-352) et Payjoin v2.


Les paiements silencieux remplacent les adresses jetables par des adresses furtives réutilisables afin d'empêcher le couplage on-chain des transactions entrantes. Bien que les problèmes de synchronisation des versions précédentes se soient considérablement améliorés, l'analyse et la détection des paiements silencieux requièrent davantage de ressources et de bande passante.


Payjoin v2 bouleverse l'analyse des chaînes en fusionnant les entrées de l'expéditeur et du destinataire en une seule transaction, sans frais supplémentaires ni coordination centrale. Cela rompt avec l'heuristique commune de propriété des intrants, ce qui est un avantage significatif car cela signifie que vous ne pouvez pas supposer que tous les intrants appartiennent à l'expéditeur.


Pour les utilisateurs qui privilégient l'anonymat financier, le Cake Wallet est une option viable. Il intègre les protocoles de confidentialité directement dans ses fonctionnalités de base, les rendant accessibles sans aucune complexité technique. Alors que la surveillance des blockchains publiques augmente, des outils comme celui-ci aident à maintenir la confidentialité des transactions là où elle compte le plus. Une mise en œuvre plus large de ces normes dans le paysage wallet serait une évolution bienvenue.


## 📚 Ressources


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/