---
name: Plan d'héritage Bitcoin
description: Comment organiser la transmission de ses bitcoins à ses proches
---

![cover](assets/cover.webp)

La transmission de bitcoins représente un défi technique majeur que de nombreux détenteurs négligent. Contrairement aux actifs bancaires traditionnels où un établissement financier peut remettre les fonds aux ayants droit, Bitcoin fonctionne sans intermédiaire. Vos proches ne pourront jamais accéder à vos fonds sans les informations techniques nécessaires, quelle que soit leur légitimité juridique.

Ce tutoriel vous guide dans la création d'un plan d'héritage technique. Vous apprendrez comment fonctionnent les mécanismes on-chain permettant la transmission automatisée, comment documenter vos configurations, et comment choisir les solutions adaptées pour garantir que votre patrimoine Bitcoin reste accessible à vos proches.

## Pourquoi un plan d'héritage technique est indispensable

Bitcoin repose sur un principe cryptographique fondamental : celui qui possède les clés privées contrôle les fonds. Cette souveraineté devient une vulnérabilité majeure lorsque le détenteur disparaît sans avoir transmis les informations nécessaires.

Un plan d'héritage Bitcoin doit répondre à deux objectifs apparemment contradictoires : permettre à vos proches d'accéder à vos fonds le moment venu, tout en empêchant quiconque d'y accéder prématurément. Cet équilibre délicat repose sur les capacités de programmation native de Bitcoin.

La complexité technique ajoute une difficulté supplémentaire. Vos héritiers devront manipuler des concepts comme les phrases de récupération, les descripteurs de portefeuille, ou les chemins de dérivation. Sans préparation adéquate, même un héritier bien intentionné risque de commettre des erreurs irréversibles.

## Comment fonctionne l'héritage on-chain

Bitcoin permet d'encoder des conditions de dépense directement dans les transactions grâce à son langage de script. L'héritage on-chain exploite cette programmabilité pour créer des chemins de récupération alternatifs qui s'activent automatiquement.

### Les verrous temporels (timelocks)

Les timelocks constituent le mécanisme fondamental de l'héritage Bitcoin. Ils permettent de verrouiller des fonds jusqu'à ce qu'une condition temporelle soit remplie.

**CLTV (CheckLockTimeVerify)** : Ce timelock absolu vérifie qu'un moment spécifique (date ou hauteur de bloc) est atteint avant d'autoriser la dépense. Par exemple, "ces fonds ne peuvent être dépensés qu'après le bloc 900000" ou "après le 1er janvier 2026". L'avantage du CLTV est de permettre des délais longs (plusieurs années), mais la date est fixe et s'applique identiquement à tous les UTXO du portefeuille. Pour maintenir le contrôle de vos fonds, vous devez périodiquement créer un nouveau portefeuille avec une date d'expiration repoussée et y transférer vos fonds.

**CSV (CheckSequenceVerify)** : Ce timelock relatif vérifie qu'un certain nombre de blocs s'est écoulé depuis la création de l'UTXO. Par exemple, "ces fonds ne peuvent être dépensés que 52560 blocs (~1 an) après leur réception". L'avantage du CSV est que chaque UTXO possède son propre compteur indépendant. Chaque fois que vous effectuez une transaction, les nouveaux UTXO créés réinitialisent leur propre délai. La limite technique de 65535 blocs (~15 mois maximum) restreint cependant les délais possibles. Cette approche est plus naturelle pour un usage quotidien puisque votre activité normale repousse automatiquement les échéances.

### Les chemins de dépense multiples

Un portefeuille d'héritage combine plusieurs chemins de dépense (spending paths) dans chaque adresse :

- **Chemin principal** : Le propriétaire peut dépenser ses fonds à tout moment avec sa clé principale, sans condition temporelle.
- **Chemin(s) de récupération** : Une ou plusieurs clés alternatives peuvent dépenser les fonds uniquement après expiration d'un délai défini.

Chaque transaction effectuée par le propriétaire "rafraîchit" les UTXO, créant de nouvelles sorties avec des timelocks réinitialisés. Cette mécanique garantit que tant que le propriétaire reste actif, les chemins de récupération ne s'activent jamais.

### Miniscript et Taproot

**Miniscript** est un langage structuré développé par Andrew Poelstra, Pieter Wuille et Sanket Kanjalkar qui facilite l'écriture et l'analyse de scripts Bitcoin complexes. Il permet de composer des conditions de dépense lisibles et vérifiables, essentielles pour les configurations d'héritage impliquant plusieurs clés et timelocks.

**Taproot** (activé en novembre 2021) améliore significativement l'héritage on-chain. Grâce à sa structure en arbre (MAST), seule la condition de dépense utilisée est révélée sur la blockchain. Si le propriétaire dépense normalement ses fonds, les conditions d'héritage restent invisibles. Cette confidentialité réduit également les frais de transaction pour les chemins complexes.

## L'importance critique des descripteurs

Pour les portefeuilles d'héritage, la phrase de récupération (seed) ne suffit pas à restaurer l'accès aux fonds. Le **descripteur** devient l'élément critique.

Un descripteur est une chaîne de caractères qui décrit exhaustivement la structure d'un portefeuille : les clés publiques impliquées, les conditions de dépense, les chemins de dérivation, et les timelocks configurés. Voici un exemple simplifié :

```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```

Ce descripteur indique : "soit la clé principale peut dépenser immédiatement, soit la clé de récupération peut dépenser après 52560 blocs".

Décortiquons cet exemple :
- `wsh()` : Witness Script Hash, indique le type d'adresse (P2WSH)
- `or_d()` : Condition "ou" avec une branche par défaut
- `pk([fingerprint/path]xpub...)` : La clé publique principale avec son empreinte et chemin de dérivation
- `and_v()` : Condition "et" combinant la clé de récupération avec le timelock
- `older(52560)` : Le verrou temporel relatif de 52560 blocs

**Sans le descripteur, même avec toutes les phrases de récupération, vos héritiers ne pourront pas reconstruire le portefeuille.** Un portefeuille standard peut être restauré uniquement à partir de la seed car il suit des chemins de dérivation standardisés (BIP44, BIP84). En revanche, un portefeuille d'héritage utilise des scripts personnalisés qui ne peuvent être devinés. La sauvegarde du descripteur (ou du fichier de configuration exporté par votre logiciel) doit accompagner obligatoirement les phrases de récupération dans votre plan d'héritage.

## Les composants documentaires d'un plan d'héritage

Au-delà des mécanismes techniques, un plan d'héritage efficace repose sur trois piliers documentaires.

### La lettre d'héritage

Cette lettre personnelle constitue le point d'entrée de votre plan. Rédigée à l'attention de vos héritiers, elle explique le contexte et les précautions à prendre.

Votre lettre doit inclure des règles de sécurité explicites :
- Ne pas se précipiter et prendre le temps d'apprendre avant de déplacer des fonds
- Ne jamais communiquer une phrase de récupération complète à une personne unique
- Ne jamais saisir une phrase de récupération dans un logiciel ou ordinateur non vérifié
- Se méfier des arnaques et des personnes offrant de l'aide non sollicitée
- Solliciter l'avis d'au moins deux personnes de confiance avant toute décision

Cette lettre contient également les coordonnées de votre notaire et l'emplacement de votre testament. Elle ne doit jamais contenir de phrases de récupération ou de mots de passe.

### Le répertoire des contacts de confiance

Aucun héritier ne devrait affronter seul la récupération de bitcoins. Ce répertoire liste les personnes pouvant apporter leur aide technique ou juridique.

Pour chaque contact, documentez : nom complet, relation avec vous, rôle dans le plan, niveau de confiance, compétences Bitcoin, et coordonnées complètes. La règle fondamentale : vos héritiers doivent toujours consulter au moins deux personnes différentes avant de prendre une décision importante.

### L'inventaire des avoirs Bitcoin

Cette section cartographie l'ensemble de vos bitcoins avec les informations techniques nécessaires à leur récupération.

Pour chaque portefeuille, documentez :
- **Type de portefeuille** : matériel, logiciel, configuration (single-sig, multisig, héritage)
- **Localisation des appareils** : où se trouve physiquement le hardware wallet
- **Emplacement du descripteur/fichier de configuration** : critique pour les portefeuilles avancés
- **Emplacement de la phrase de récupération** : séparé du descripteur
- **Codes d'accès** : où sont stockés les PIN et passphrases
- **Délais configurés** : quand les chemins de récupération s'activent

## Les solutions techniques disponibles

Plusieurs logiciels implémentent les mécanismes d'héritage on-chain. Chacun présente des caractéristiques techniques distinctes.

### Liana

Liana est un logiciel desktop (Linux, macOS, Windows) utilisant Miniscript pour créer des portefeuilles avec chemins de récupération temporisés. Le projet est développé par Wizardsardine, cofondé par Antoine Poinsot (contributeur Bitcoin Core).

**Architecture technique** : Liana crée des portefeuilles P2WSH (SegWit natif) par défaut, avec support Taproot disponible selon la compatibilité de votre hardware wallet. L'architecture repose sur un chemin principal et un ou plusieurs chemins de récupération. Le descripteur généré encode toutes les conditions et doit être sauvegardé impérativement.

**Timelocks utilisés** : Liana utilise des timelocks relatifs (CSV), limités à 65535 blocs (~15 mois). Pour maintenir le contrôle, vous devez effectuer une transaction de rafraîchissement avant expiration du délai.

**Intégration hardware wallets** : BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, et d'autres appareils sont compatibles pour signer les transactions.

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper

Bitcoin Keeper est une application mobile (iOS, Android) combinant multisig et timelocks via ses "Enhanced Vaults". L'approche mobile avec guidance intégrée la rend accessible aux utilisateurs moins techniques.

**Architecture technique** : Les Enhanced Vaults utilisent Miniscript pour créer des configurations multisig où des clés supplémentaires s'activent après des délais définis. L'Inheritance Key s'ajoute au quorum existant, tandis que l'Emergency Key peut bypasser complètement le multisig.

**Timelocks utilisés** : Bitcoin Keeper utilise des timelocks absolus (CLTV), permettant des délais supérieurs à 15 mois. La date d'activation est fixée à la création du wallet et s'applique à tous les UTXO. L'application intègre une fonction de "revaulting" qui gère automatiquement le rafraîchissement : l'utilisateur suit simplement les étapes guidées, sans avoir à créer manuellement un nouveau wallet.

**Fonctionnalités complémentaires** : Documents d'héritage intégrés, Canary Wallets pour détecter les compromissions de clés, et rappels de rafraîchissement.

https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Heritage

Heritage est une application desktop utilisant les scripts Taproot pour encoder les conditions d'héritage. L'utilisation de Taproot offre une confidentialité accrue puisque les chemins non utilisés restent invisibles sur la blockchain.

**Architecture technique** : Chaque adresse Heritage intègre un chemin principal et des chemins alternatifs pour chaque héritier avec des délais progressifs. La hiérarchisation permet de définir un backup personnel à 6 mois et des héritiers familiaux à 12-15 mois.

**Modes d'utilisation** : Version autonome avec votre propre nœud (gratuit) ou service géré ajoutant rappels et notifications aux héritiers (0,05%/an).

https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Le processus de récupération par l'héritier

Comprendre le processus de récupération aide à préparer un plan efficace. Voici les étapes techniques qu'un héritier devra suivre.

### Prérequis pour la récupération

L'héritier a besoin de :
1. **Le fichier de descripteur ou de configuration** du portefeuille d'origine (format JSON ou texte selon le logiciel)
2. **Sa phrase de récupération** (celle associée à sa clé d'héritage, généralement 12 ou 24 mots)
3. **Un logiciel compatible** (Liana, Bitcoin Keeper, Heritage, ou Sparrow/Specter pour les descripteurs standards)
4. **Une connexion à un nœud Bitcoin** pour vérifier l'état des timelocks et diffuser la transaction

### Étapes de récupération

1. **Installer le logiciel** sur un appareil sécurisé et configurer la connexion au réseau Bitcoin (nœud personnel ou serveur Electrum)
2. **Importer le descripteur** pour reconstruire la structure du portefeuille. Le logiciel générera automatiquement toutes les adresses utilisées
3. **Restaurer la clé d'héritage** depuis la phrase de récupération. Le logiciel vérifiera que cette clé correspond bien à l'une des clés autorisées dans le descripteur
4. **Synchroniser le portefeuille** pour découvrir tous les UTXO et leurs conditions de dépense
5. **Vérifier l'expiration des timelocks** : le logiciel indiquera pour chaque UTXO si le chemin de récupération est actif
6. **Créer la transaction de récupération** vers une adresse contrôlée uniquement par l'héritier (idéalement un nouveau portefeuille simple)
7. **Signer et diffuser** la transaction sur le réseau Bitcoin

Si le timelock n'est pas encore expiré, l'héritier devra attendre. Le logiciel affichera la date ou le bloc à partir duquel la récupération devient possible. Pendant cette période d'attente, les fonds restent sécurisés sur la blockchain.

### Points de vigilance pour l'héritier

L'héritier doit être particulièrement attentif à :
- **Vérifier l'authenticité du logiciel** téléchargé (checksums, signatures)
- **Ne jamais partager sa phrase de récupération** avec quiconque offrant de l'aide
- **Consulter au moins deux personnes de confiance** avant d'effectuer la récupération
- **Transférer les fonds vers un portefeuille simple** qu'il maîtrise complètement après récupération

## Bonnes pratiques

### Séparation des informations

Ne jamais stocker toutes les informations au même endroit. Le descripteur doit être séparé des phrases de récupération, elles-mêmes séparées des codes PIN. Cette distribution complique l'accès pour un attaquant tout en restant reconstituable par vos héritiers légitimes.

### Tests de récupération

Avant de déposer des fonds significatifs, testez le processus complet de récupération avec un petit montant. Vérifiez que vous pouvez restaurer le portefeuille depuis le descripteur et les phrases de récupération sur un appareil vierge. Documentez les étapes pour vos héritiers.

### Maintenance des timelocks

Planifiez le rafraîchissement de vos timelocks bien avant leur expiration. Pour un délai de 12 mois, effectuez une transaction tous les 9-10 mois. Les logiciels proposent généralement des rappels ou des fonctions de rafraîchissement automatisé.

### Mise à jour du plan

Votre configuration Bitcoin évolue. Chaque changement significatif (nouveau portefeuille, modification des délais, ajout d'héritier) doit se refléter dans votre documentation. Établissez une routine de révision annuelle.

## Choisir son approche

Le choix entre les différentes solutions dépend de votre profil technique et de vos besoins spécifiques.

**Liana** convient aux utilisateurs desktop préférant un logiciel open source avec contrôle total via leur propre nœud. La configuration reste accessible grâce à l'interface guidée. Les timelocks relatifs (CSV) simplifient la maintenance puisque votre activité normale repousse automatiquement les échéances. Limitation : délai maximum d'environ 15 mois (65535 blocs).

**Bitcoin Keeper** cible les utilisateurs mobiles souhaitant une interface intuitive avec documents d'accompagnement intégrés. L'application propose deux types de clés spéciales : l'Inheritance Key (qui s'ajoute au quorum) et l'Emergency Key (qui le contourne complètement). Les timelocks absolus (CLTV) permettent des délais supérieurs à 15 mois, avec une fonction de revaulting intégrée simplifiant le rafraîchissement. Le plan Diamond Hands débloque les fonctionnalités d'héritage avancées.

**Heritage** s'adresse aux utilisateurs techniques appréciant la confidentialité Taproot et la hiérarchisation des héritiers avec délais progressifs. La structure en arbre Taproot masque les conditions d'héritage lors des transactions normales, ne révélant que la condition utilisée lors de la récupération.

Les trois solutions partagent un point commun : elles requièrent un rafraîchissement périodique pour empêcher l'activation prématurée des chemins de récupération. Cette contrainte constitue à la fois le prix et la garantie de l'héritage on-chain sans tiers de confiance. Planifiez des rappels réguliers et intégrez cette maintenance à votre routine de gestion Bitcoin.

## Conclusion

Un plan d'héritage Bitcoin technique combine des mécanismes cryptographiques (timelocks, Miniscript, Taproot) avec une documentation rigoureuse. Les portefeuilles avancés permettent de transmettre vos bitcoins automatiquement après une période d'inactivité, sans intervention de tiers.

Les éléments critiques à transmettre à vos héritiers sont : le fichier de descripteur ou de configuration, leur phrase de récupération, les instructions de récupération détaillées, et les coordonnées de personnes compétentes pouvant les assister.

Commencez par choisir une solution technique adaptée à votre profil, testez-la avec un petit montant, puis documentez l'ensemble dans un plan structuré. La complexité initiale garantit une transmission souveraine de votre patrimoine Bitcoin.

## Ressources

### Modèle de plan d'héritage

- [Bitcoin Inheritance Plan Template (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Modèle de documentation Plan ₿ Network

### Références techniques

- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Spécification des timelocks absolus (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Spécification des timelocks relatifs (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Documentation officielle Miniscript par Pieter Wuille

### Sites officiels des solutions

- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7
