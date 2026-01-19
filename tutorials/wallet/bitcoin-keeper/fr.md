---
name: Bitcoin Keeper
description: Portefeuille mobile Bitcoin orienté sécurité et multisig
---

![cover](assets/cover.webp)

La gestion sécurisée de ses bitcoins représente un défi majeur pour tout détenteur conscient des enjeux de souveraineté financière. Entre la simplicité d'un portefeuille mobile et la robustesse d'une solution multisig, le fossé technique peut sembler intimidant pour de nombreux utilisateurs. Bitcoin Keeper se positionne précisément à cette intersection, proposant une approche progressive de la sécurité qui accompagne l'utilisateur dans son évolution.

Bitcoin Keeper est une application mobile open source, exclusivement dédiée à Bitcoin, développée par l'équipe BitHyve. Son ambition est de rendre accessible la gestion avancée de portefeuilles, notamment les configurations multisignatures, tout en conservant une interface intuitive pour les débutants. L'application adopte le slogan « Secure today, Plan for tomorrow », reflétant sa philosophie d'accompagnement sur le long terme.

Contrairement aux portefeuilles généralistes qui gèrent de multiples cryptomonnaies, Bitcoin Keeper maintient une focalisation stricte sur Bitcoin. Cette approche bitcoin-only réduit la surface d'attaque potentielle et simplifie considérablement l'expérience utilisateur. L'application se distingue également par son intégration native des portefeuilles matériels les plus répandus et ses fonctionnalités avancées de gestion des UTXO.

## Qu'est-ce que Bitcoin Keeper ?

### Philosophie et objectifs

Bitcoin Keeper a été conçu pour répondre aux besoins spécifiques des bitcoiners souhaitant garder le contrôle total de leurs clés privées. Le projet embrasse pleinement les principes fondamentaux de Bitcoin : code source ouvert et auditable, respect de la vie privée, et souveraineté de l'utilisateur. Aucune inscription ni information personnelle n'est requise pour utiliser l'application, et celle-ci peut même fonctionner en mode déconnecté pour les opérations de signature.

L'objectif central est de proposer un outil flexible et pérenne pour conserver ses BTC sur plusieurs années, voire plusieurs générations grâce aux fonctionnalités d'héritage. L'application permet de débuter simplement avec un portefeuille mobile, puis d'évoluer progressivement vers des solutions multisignatures plus sécurisées.

### Architecture de l'application

Bitcoin Keeper organise la gestion des fonds autour de deux concepts distincts. Le **Hot Wallet** constitue un portefeuille simple à clé unique (Single-Key), stocké sur le téléphone, destiné aux dépenses courantes et aux montants modestes. Les **Vaults** représentent des coffres-forts multisignatures (Multi-Key) nécessitant plusieurs clés pour autoriser une dépense, conçus pour le stockage sécurisé de long terme.

### Fonctionnalités principales

Bitcoin Keeper prend en charge la quasi-totalité des portefeuilles matériels du marché : Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport, et le Tapsigner de Coinkite. L'intégration s'effectue via différentes méthodes selon les appareils : scan de QR code, connexion NFC, ou import de fichier.

L'application offre également une gestion avancée des UTXO avec étiquetage des transactions, coin control pour sélectionner manuellement les inputs lors d'un envoi, et support du format PSBT pour les transactions partiellement signées.

## Installation et configuration initiale

Bitcoin Keeper est disponible gratuitement sur Android via le Google Play Store et sur iOS via l'App Store. L'éditeur indiqué est BitHyve. Avant de procéder à l'installation, assurez-vous que votre appareil est exempt de malwares, à jour, et non rooté ou jailbreaké.

Au premier lancement, l'application vous demande de créer un code PIN de sécurité. Ce code protège l'accès à votre portefeuille et chiffre localement les données sensibles. Choisissez un code robuste et mémorisez-le. Vous pouvez ensuite activer l'authentification biométrique (empreinte digitale ou Face ID) pour un déverrouillage plus rapide.

![Installation et configuration du PIN](assets/fr/01.webp)

L'application présente ensuite plusieurs écrans d'introduction expliquant ses trois piliers : la création de portefeuilles pour envoyer et recevoir des bitcoins, la gestion des clés avec compatibilité hardware wallets, et la planification de l'héritage pour transmettre ses bitcoins. Appuyez sur « Get Started » puis choisissez « Start New » pour créer une nouvelle configuration.

![Écrans d'introduction](assets/fr/02.webp)

## Découverte de l'interface

L'interface de Bitcoin Keeper s'organise autour de quatre onglets principaux accessibles depuis la barre de navigation inférieure :

![Les quatre onglets de l'application](assets/fr/03.webp)

L'onglet **Wallets** affiche vos portefeuilles et leur solde. C'est depuis cet écran que vous accédez à vos wallets pour envoyer et recevoir des bitcoins. Les tags « Hot Wallet » et « Single-Key » ou « Multi-Key » permettent d'identifier rapidement le type de chaque portefeuille.

L'onglet **Keys** centralise la gestion de vos clés de signature. Vous y retrouvez la Mobile Key générée par l'application ainsi que toutes les clés importées depuis des hardware wallets. C'est également ici que vous ajoutez de nouveaux dispositifs de signature.

L'onglet **Concierge** propose des services d'assistance : soumission de questions à l'équipe support et mise en relation avec des conseillers Bitcoin pour un accompagnement personnalisé.

L'onglet **More** (More Options) donne accès aux paramètres : connexion à un serveur personnel, sauvegarde des clés, documents d'héritage, préférences d'affichage, et gestion des wallets.

## Connexion à son propre serveur

Pour renforcer votre confidentialité, Bitcoin Keeper permet de connecter l'application à votre propre serveur Electrum plutôt que d'utiliser les serveurs publics par défaut.

![Configuration du serveur Electrum](assets/fr/04.webp)

Depuis l'onglet More, faites défiler jusqu'à trouver les paramètres de serveur. Appuyez sur « Add Server » pour configurer une nouvelle connexion. Vous avez le choix entre « Public Server » (serveurs publics préconfigurés) et « Private Electrum » (votre propre serveur).

Pour un serveur privé, renseignez l'URL (par exemple umbrel.local pour un nœud Umbrel) et le numéro de port (généralement 50001). Activez SSL si votre serveur le supporte. Vous pouvez également scanner un QR code de configuration. Une fois les paramètres saisis, appuyez sur « Connect to Server ».

Si vous n'avez pas encore votre nœud Bitcoin, n'hésitez pas à consulter notre tutoriel sur Umbrel, une solution simple et accessible à tous pour faire tourner son propre nœud :

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Recevoir des bitcoins

Depuis l'onglet Wallets, sélectionnez le portefeuille sur lequel vous souhaitez recevoir des fonds en appuyant dessus. L'écran du wallet affiche le solde et trois boutons d'action : Send Bitcoin, Receive Bitcoin, et View All Coins.

![Réception de bitcoins](assets/fr/05.webp)

Appuyez sur « Receive Bitcoin ». Bitcoin Keeper génère une nouvelle adresse de réception au format Bech32 (commençant par bc1...) accompagnée de son QR code. Vous pouvez ajouter un label à cette adresse pour identifier la source des fonds. Partagez l'adresse à l'expéditeur en affichant le QR code ou en copiant l'adresse textuelle.

L'application génère automatiquement une nouvelle adresse pour chaque réception, préservant votre confidentialité. Utilisez « Get New Address » pour obtenir une adresse vierge si nécessaire.

## Gestion des UTXO

Bitcoin Keeper offre une visibilité complète sur les UTXO (Unspent Transaction Outputs) composant votre solde. Depuis l'écran d'un wallet, appuyez sur « View All Coins » pour accéder au gestionnaire de coins.

![Gestion des UTXO](assets/fr/06.webp)

L'écran « Manage Coins » liste chaque UTXO individuellement avec son montant et son label. Cette vue permet de tracer la provenance de vos coins et de les organiser. Vous pouvez sélectionner des UTXO spécifiques via « Select to Send » pour effectuer un envoi avec coin control, évitant ainsi de mélanger des coins d'origines différentes.

## Envoyer des bitcoins

Pour effectuer un envoi, sélectionnez le portefeuille source puis appuyez sur « Send Bitcoin ». Saisissez l'adresse de destination (collée ou scannée via QR code) et ajoutez optionnellement un label pour identifier le destinataire.

![Envoi de bitcoins](assets/fr/07.webp)

L'écran suivant permet de saisir le montant à envoyer. L'interface affiche votre solde disponible et la conversion en devise fiat. Sélectionnez la priorité des frais : Low (économique, ~60 minutes), Medium, ou High (prioritaire). Les frais estimés en sats/vbyte s'affichent en temps réel. Appuyez sur « Send » pour continuer.

![Confirmation et envoi](assets/fr/08.webp)

Un écran récapitulatif affiche tous les détails : wallet source, adresse destinataire, priorité de transaction, frais réseau, montant envoyé et total. Vérifiez attentivement ces informations car les transactions Bitcoin sont irréversibles. Appuyez sur « Confirm & Send » pour diffuser la transaction.

Une confirmation « Send Successful » apparaît avec le résumé complet. La transaction est visible dans l'historique « Recent Transactions » avec son label.

## Sauvegarder ses clés

La sauvegarde de votre Recovery Key (phrase de récupération) est une étape critique. Depuis l'onglet More, accédez à la section « Backup and Recovery » et appuyez sur « Recovery Key ».

![Sauvegarde de la Recovery Key](assets/fr/09.webp)

L'écran affiche l'état de vos sauvegardes. Pour vérifier votre sauvegarde, l'application vous demande de confirmer un mot spécifique de votre phrase (par exemple le 7ème mot). Cette vérification garantit que vous avez correctement noté votre phrase de récupération.

Depuis « Recovery Key Settings », vous pouvez consulter votre phrase complète via « View Recovery Key » et voir l'empreinte (Signer Fingerprint) de votre clé. Conservez votre phrase de 12 mots sur papier, en lieu sûr, à l'abri de l'humidité et du feu. Ne la stockez jamais sur un appareil connecté.

## Ajouter une clé externe (hardware wallet)

L'un des atouts majeurs de Bitcoin Keeper est l'intégration des hardware wallets. Depuis l'onglet Keys, appuyez sur « Add key » pour ajouter un nouveau dispositif de signature.

![Ajout d'une clé hardware](assets/fr/10.webp)

Choisissez « Add key from a hardware » pour connecter un portefeuille matériel. L'application supporte une large gamme d'appareils : BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, et Specter Solutions.

### Configuration d'un Tapsigner

Le Tapsigner est une carte NFC de Coinkite particulièrement adaptée à l'usage mobile. Si vous voulez en apprendre davantage, nous avons un tutoriel dédié :

https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Pour ajouter le Tapsigner, sélectionnez-le dans la liste des hardware wallets.

![Configuration du Tapsigner](assets/fr/11.webp)

Entrez d'abord le code PIN à 6-32 chiffres imprimé au dos de votre carte (par défaut sur les cartes neuves) ou bien votre PIN s'il est déjà configuré. Appuyez sur « Proceed » puis approchez votre Tapsigner du dos de votre téléphone lorsque « Prêt à scanner » s'affiche. La communication NFC importe automatiquement la clé publique. Vous pouvez ensuite ajouter une description (ex: « Métro Card ») pour identifier cette clé.

## Créer un portefeuille multisig

Une fois vos clés configurées, vous pouvez créer un portefeuille multisignature combinant plusieurs dispositifs. Depuis l'onglet Wallets, appuyez sur « Add Wallet ».

![Création d'un nouveau wallet](assets/fr/12.webp)

Trois options s'offrent à vous : « Create Wallet » pour un nouveau portefeuille, « Import Wallet » pour restaurer un wallet existant, ou « Collaborative Wallet » pour un coffre partagé. Sélectionnez « Create Wallet » puis « Bitcoin Wallet ».

![Sélection du type de wallet](assets/fr/13.webp)

L'écran suivant propose différentes configurations : « Single-key » (portefeuille simple), « 2 of 3 multi-key », ou « 3 of 5 multi-key ». Pour un multisig personnalisé, appuyez sur « Select custom setup ». Choisissez par exemple « 1 of 2 » : une seule signature requise parmi deux clés possibles.

Sélectionnez ensuite les clés qui composeront votre Vault. Dans notre exemple, nous combinons la « Mobile Key » (clé logicielle du téléphone) avec le « TAPSIGNER » (Métro Card). Cette configuration offre une redondance : si l'une des clés devient inaccessible, vous pouvez toujours dépenser vos fonds avec l'autre.

![Finalisation du wallet multisig](assets/fr/14.webp)

Nommez votre wallet (ex: « Test PlanB »), ajoutez une description optionnelle, et vérifiez les clés sélectionnées. Appuyez sur « Create Your Wallet ». Un message de confirmation « Wallet Created Successfully » apparaît, vous rappelant de sauvegarder le fichier de récupération du wallet.

Votre nouveau portefeuille multisig apparaît maintenant dans l'onglet Wallets avec le tag « Multi-key » et l'indication « 1 of 2 ».

### Sauvegarder le fichier de configuration

**Cette étape est critique pour les wallets multisig.** Contrairement à un portefeuille simple où la phrase de récupération suffit à restaurer l'accès, un wallet multisig nécessite également le fichier de configuration qui décrit la structure du coffre (quelles clés participent, combien de signatures requises). Sans ce fichier, même avec toutes les phrases de récupération, vous ne pourrez pas reconstruire votre wallet.

![Export du fichier de configuration](assets/fr/15.webp)

Pour exporter ce fichier, sélectionnez votre wallet multisig dans l'onglet Wallets, puis appuyez sur l'icône Settings (engrenage) en haut à droite. Dans « Wallet Settings », appuyez sur « Wallet configuration file ». Plusieurs options d'export s'offrent à vous :

- **Export PDF** : génère un document PDF contenant toutes les informations du wallet
- **Show QR** : affiche un QR code scannable pour importer la configuration sur un autre appareil
- **Airdrop / File Export** : exporte le fichier via les options de partage de votre téléphone
- **NFC** : partage via NFC avec un appareil compatible

Conservez ce fichier de configuration séparément de vos phrases de récupération, idéalement sur un support chiffré ou imprimé. En cas de perte de votre téléphone, ce fichier combiné aux phrases de récupération de chaque clé participante vous permettra de reconstruire votre wallet multisig sur Bitcoin Keeper ou tout autre logiciel compatible.

## Bonnes pratiques

### Organisation des fonds

Structurez vos bitcoins selon leur usage : un hot wallet Single-Key pour les dépenses courantes avec des montants limités, et un ou plusieurs Vaults Multi-Key pour l'épargne de long terme. L'étiquetage systématique des UTXO vous aidera à garder une trace de la provenance de vos fonds, ce qui est particulièrement utile pour la gestion de la confidentialité et éviter de mélanger des coins d'origines différentes.

Maintenez votre téléphone sécurisé : activez le verrouillage biométrique, effectuez les mises à jour système régulièrement, et restez vigilant sur les applications installées. Tenez également Bitcoin Keeper à jour pour bénéficier des correctifs de sécurité.

### Sécurité des sauvegardes

Conservez au minimum deux copies de chaque phrase de récupération sur papier, stockées en des lieux géographiquement distincts. Pour les sommes importantes, envisagez un support métallique gravé résistant aux sinistres. Ne stockez jamais ces phrases sur un appareil connecté à internet et ne les photographiez pas.

Pour les Vaults multisig, sauvegardez également le fichier de configuration (Wallet Recovery File) qui contient les clés publiques participantes et la structure du coffre. Ce fichier, combiné aux phrases de récupération des clés, permet de reconstruire le wallet sur n'importe quel logiciel compatible comme Sparrow ou Specter.

## Avantages et limitations

### Points forts

- Application bitcoin-only réduisant la complexité et les risques
- Intégration native des Vaults multisig avec guidance pas à pas
- Support étendu des hardware wallets (Tapsigner, Coldcard, Ledger, Jade, etc.)
- Gestion avancée des UTXO et coin control
- Connexion possible à un serveur Electrum personnel
- Code source ouvert et auditable

### Contraintes à considérer

- Interface principalement en anglais
- Certaines fonctionnalités premium (Cloud Backup, Assisted Server) nécessitent un upgrade
- La configuration multisig demande un apprentissage initial

## Conclusion

Bitcoin Keeper se distingue comme une solution évolutive pour la gestion de ses bitcoins. Son approche progressive, du simple hot wallet aux Vaults multisignatures, permet de faire évoluer sa sécurité en fonction de ses besoins. La possibilité d'intégrer facilement des hardware wallets comme le Tapsigner ouvre la voie à des configurations robustes sans complexité excessive.

L'orientation bitcoin-only, le code source ouvert et le respect de la vie privée en font un choix aligné avec les valeurs fondamentales de l'écosystème Bitcoin.

Ce tutoriel couvre les fonctionnalités essentielles de Bitcoin Keeper dans sa version gratuite. L'application propose également des fonctionnalités premium (Cloud Backup, Assisted Server Backup, Canary Wallets) qui feront l'objet d'un tutoriel dédié. Nous explorerons aussi dans un prochain guide la fonctionnalité d'héritage (Inheritance Planning), qui permet de préparer la transmission de ses bitcoins à ses proches grâce aux Enhanced Vaults et aux documents d'accompagnement intégrés à l'application.

## Ressources

- Site officiel : [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centre d'aide : [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Code source : [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X : [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)
