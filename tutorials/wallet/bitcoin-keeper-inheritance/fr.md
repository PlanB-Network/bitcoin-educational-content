---
name: Bitcoin Keeper - Plan d’héritage
description: Planifier la transmission de ses bitcoins avec Bitcoin Keeper
---

![cover](assets/cover.webp)

La transmission du patrimoine Bitcoin représente l'un des défis les plus sous-estimés par les détenteurs. Contrairement à un compte bancaire où l'établissement financier peut remettre les fonds aux ayants droit, Bitcoin repose entièrement sur la possession des clés privées. Un héritier parfaitement légitime sur le plan juridique ne pourra jamais accéder aux fonds sans ces clés, tandis qu'un individu malveillant en possession des secrets pourra les dépenser sans aucune formalité.

Dans ce second tutoriel consacré à Bitcoin Keeper, nous explorons les fonctionnalités premium dédiées à la planification successorale. L'application propose des outils avancés pour créer des coffres d'héritage (Enhanced Vaults) intégrant des mécanismes de protection temporisés grâce à Miniscript, ainsi que des documents d'accompagnement pour guider vos proches.

Ce guide suppose que vous maîtrisez déjà les bases de Bitcoin Keeper (création de portefeuille, multisig classique, ajout de clés hardware) telles qu'expliquées dans notre premier tutoriel :

https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)

## Les plans d'abonnement Bitcoin Keeper

Bitcoin Keeper fonctionne sur un modèle freemium avec trois niveaux d'abonnement offrant des fonctionnalités progressives. Pour accéder aux plans, rendez-vous dans l'onglet **More**, puis appuyez sur votre plan actuel (par défaut « Pleb ») pour ouvrir l'écran **Manage Subscription**.

![Plans d'abonnement](assets/fr/01.webp)

Le **plan Pleb** (gratuit) donne accès à l'essentiel : création illimitée de portefeuilles single-key et multi-key, compatibilité avec tous les hardware wallets majeurs (Coldcard, Trezor, Ledger, Jade, Tapsigner...), coin control, labeling, et connexion à un serveur Electrum personnel. Ce plan suffit pour une utilisation standard et même pour des configurations multisig classiques.

Le **plan Hodler** (9,99€/mois, avec 1 mois offert si paiement annuel) inclut toutes les fonctionnalités Pleb et ajoute les sauvegardes chiffrées sur le cloud (iCloud ou Google Drive) pour restaurer vos coffres sur n'importe quel appareil, le Server Key pour ajouter des politiques de dépense automatiques et la 2FA au-delà d'un certain seuil, et les Canary Wallets pour détecter les accès non autorisés à vos clés.

Le **plan Diamond Hands** (29,99€/mois, avec 1 mois offert si paiement annuel) constitue l'offre complète pour la planification successorale. Il inclut tout le plan Hodler et débloque l'Inheritance Key (clé d'héritage à activation différée), l'Emergency Key (clé d'urgence pour récupération en cas de perte), les outils et documents d'Inheritance Planning, et un appel d'accompagnement avec l'équipe Concierge pour valider votre configuration. C'est l'offre destinée aux bitcoiners qui souhaitent transmettre leur patrimoine sur plusieurs générations.

Point important : les coffres créés restent accessibles même si vous revenez au plan gratuit. Vos configurations sont basées sur des standards ouverts (BSMS, Miniscript) et fonctionnent indépendamment de l'abonnement.

## Les documents d'héritage

Une fois l'abonnement Diamond Hands activé, accédez à la section **Inheritance Documents** depuis l'onglet More. Bitcoin Keeper met à disposition cinq modèles de documents pour structurer votre plan de succession, ainsi qu'une section de conseils :

![Documents d'héritage](assets/fr/02.webp)

- **Seed Words Template** : un modèle pour noter proprement vos phrases de récupération de manière organisée
- **Trusted Contacts** : un template pour lister les coordonnées des personnes de confiance impliquées dans votre plan (notaire, avocat, héritiers, gardiens de clés)
- **Additional Share Key** : un document détaillant les informations techniques de chaque clé : code PIN, chemin de dérivation, localisation physique, type de dispositif, et toute autre information utile pour identifier et utiliser la clé
- **Recovery Instructions** : les instructions pas-à-pas destinées à l'héritier ou au bénéficiaire pour récupérer les fonds
- **Letter to Attorney** : une lettre pré-remplie à adapter pour votre avocat ou notaire

La section **Inheritance Tips** propose des conseils pratiques pour sécuriser les clés destinées aux héritiers et optimiser votre plan de transmission.

Personnalisez ces documents selon votre situation et conservez-les en lieu sûr, séparément des clés elles-mêmes.

## Configurer le Cloud Backup

Avant de créer votre coffre d'héritage, activez la sauvegarde cloud pour protéger vos fichiers de configuration. Depuis l'onglet More, appuyez sur **Personal Cloud Backup**.

![Configuration Cloud Backup](assets/fr/03.webp)

Choisissez un mot de passe robuste pour chiffrer vos sauvegardes. Ce mot de passe protège uniquement les fichiers de configuration des wallets (pas vos clés privées). Confirmez le mot de passe et appuyez sur **Confirm**. Vos sauvegardes seront stockées sur votre iCloud ou Google Drive selon votre appareil. Appuyez sur **Backup Now** pour lancer une première sauvegarde.

## Importer vos clés hardware

Pour notre exemple, nous allons créer un coffre 2-of-3 avec deux clés supplémentaires (Inheritance et Emergency). Commençons par importer toutes les clés nécessaires dans l'onglet **Keys**.

![Import des clés hardware](assets/fr/04.webp)

Appuyez sur **Add key**, puis sélectionnez **Add key from a hardware** pour connecter un portefeuille matériel. Bitcoin Keeper supporte de nombreux appareils : BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, et Specter Solutions.

Dans notre configuration, nous importons :
- 2 clés **Coldcard** (MK4SP et MK4)
- 2 clés **Tapsigner** (Métro et Genesis)

Pour ajouter une Coldcard, sélectionnez-la dans la liste et suivez les instructions à l'écran pour exporter la clé publique via QR code, fichier, USB ou encore NFC. Pour plus de détails sur l'utilisation d'un Coldcard ou bien d'un Tapsigner, référez-vous à nos tutoriels dédiés :

https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Une fois toutes vos clés importées, vous les retrouvez dans l'onglet Keys avec leurs noms personnalisés.

## Créer le wallet d'héritage

Passons à la création du coffre. Depuis l'onglet **Wallets**, appuyez sur **Add Wallet**, sélectionnez **Bitcoin Wallet**, puis **Create Wallet**.

![Création du wallet](assets/fr/05.webp)

Choisissez le type de wallet. Pour notre plan d'héritage, sélectionnez **2 of 3 multi-key**. En bas de l'écran, activez **Enhanced Security Options** puis appuyez sur **Proceed**.

![Options de sécurité avancées](assets/fr/06.webp)

Dans la popup Enhanced Security Options, cochez :
- **Inheritance Key** : une clé supplémentaire qui s'ajoutera au quorum après un délai défini
- **Emergency Key** : une clé avec contrôle total différé pour récupérer les fonds en cas de perte de clés

Appuyez sur **Save Changes**. Sélectionnez ensuite les 3 clés qui composeront votre wallet parmi celles importées (par exemple : Seed Key, Coldcard MK4SP, et Tapsigner Métro).

## Configurer les délais des clés spéciales

L'écran suivant vous permet de configurer l'Emergency Key et l'Inheritance Key. C'est ici que vous définissez les délais qui régissent l'activation de ces clés spéciales.

![Configuration des délais](assets/fr/07.webp)

Pour l'**Emergency Key**, sélectionnez la clé hardware qui servira de secours ultime (ici Coldcard MK4) et choisissez le délai d'activation (dans notre exemple : 2 ans). Contrairement à l'Inheritance Key, l'Emergency Key ne s'ajoute pas au quorum : elle permet de **bypasser complètement le multisig** et donne un contrôle total sur les fonds après expiration du délai. C'est votre solution de dernier recours : si plusieurs clés sont perdues ou détruites, cette clé unique permet de tout récupérer. Elle doit donc être protégée avec la plus grande rigueur.

Pour l'**Inheritance Key**, sélectionnez la clé destinée à l'héritier (ici Coldcard MK4SP) et choisissez le délai (dans notre exemple : 1 an). Après un an sans mouvement, cette clé **s'ajoutera au quorum de signature**. Concrètement, votre wallet 2-of-3 deviendra un wallet 2-of-4 une fois ce délai écoulé, permettant à l'héritier de participer à la signature aux côtés des clés existantes.

### Comment fonctionnent les timelocks ?

Bitcoin Keeper utilise des **timelocks absolus** (CLTV - CheckLockTimeVerify), rendus possibles par Miniscript. Contrairement aux timelocks relatifs (CSV) qui démarrent à la réception de chaque UTXO, les timelocks absolus fonctionnent avec une **date d'expiration fixe** définie à la création du wallet.

Concrètement : si vous créez un wallet aujourd'hui avec une Inheritance Key à 1 an, la date d'activation sera fixée à « aujourd'hui + 1 an ». Tous les fonds déposés dans ce wallet, quelle que soit leur date de dépôt, seront accessibles via l'Inheritance Key à cette même date.

L'avantage des timelocks absolus : ils permettent des délais supérieurs à 15 mois (la limite des timelocks relatifs CSV), ce qui explique que Bitcoin Keeper puisse proposer des options comme 2 ans.

### Le mécanisme de refresh

Pour empêcher l'activation des clés spéciales de votre vivant, vous devez périodiquement « rafraîchir » votre wallet. Avec les timelocks absolus, cette opération consiste à **recréer le wallet avec une nouvelle date d'expiration** repoussée dans le futur, puis à transférer vos fonds vers ce nouveau wallet.

Bitcoin Keeper simplifie ce processus via une fonction de refresh intégrée. L'application gère automatiquement la complexité en arrière-plan : vous n'avez qu'à suivre les étapes guidées, sans avoir à créer manuellement un nouveau wallet ni à transférer les fonds vous-même. Planifiez cette opération régulièrement, bien avant l'expiration du plus court délai configuré. Par exemple, avec une Inheritance Key à 1 an, effectuez un refresh tous les 9-10 mois pour garder une marge de sécurité.

## Sauvegarder et exporter la configuration

Une fois le wallet créé, l'application vous rappelle de sauvegarder le fichier de configuration. **Cette étape est critique** : sans ce fichier, vos héritiers ne pourront pas reconstituer le wallet multisig.

![Export de la configuration](assets/fr/08.webp)

Appuyez sur **Backup Wallet Recovery File**. Plusieurs options d'export s'offrent à vous :
- **Export PDF** : génère un document complet avec toutes les informations du wallet
- **Show QR** : affiche un QR code pour importer la configuration sur un autre appareil
- **Airdrop / File Export** : exporte le fichier via les options de partage
- **NFC** : partage via NFC avec un appareil compatible

Multipliez les copies : une chez votre notaire, une dans un coffre bancaire, une version numérique chiffrée. Votre nouveau wallet apparaît maintenant dans l'onglet Wallets avec les tags « Multi-key », « 2 of 3 », « Inheritance key » et « Emergency key ».

## Créer un Canary Wallet

Le Canary Wallet est un système d'alerte précoce. L'idée : chaque clé utilisée dans un wallet multi-key peut également servir dans un wallet single-key séparé. En déposant une petite somme sur ce wallet « canari », tout mouvement non autorisé signale une compromission de la clé.

![Canary Wallets](assets/fr/09.webp)

Pour configurer un Canary Wallet, deux chemins sont possibles. Depuis l'onglet **More**, appuyez sur **Canary Wallets** dans la section « Keys and Wallets ». L'écran explique le principe : si quelqu'un accède à l'une de vos clés et trouve des fonds dans le wallet single-key associé, il tentera de les retirer, ce qui vous alertera.

![Configuration Canary depuis une clé](assets/fr/10.webp)

Vous pouvez aussi configurer le Canary directement depuis une clé. Dans l'onglet **Keys**, sélectionnez une clé (par exemple Tapsigner Genesis), appuyez sur l'icône **Settings** (engrenage), puis sur **Canary Wallet**. Le wallet canari associé s'ouvre, prêt à recevoir quelques satoshis de surveillance.

Déposez une petite somme (quelques milliers de satoshis) sur chaque Canary Wallet. Si ces fonds bougent sans votre accord, retirez immédiatement la clé compromise de vos coffres multisig.

## Bonnes pratiques

**Testez votre configuration** avec un petit montant avant d'y placer une somme conséquente. Envoyez quelques milliers de satoshis sur le vault, puis tentez une dépense sortante pour vérifier que vous maîtrisez le processus de signature avec chaque dispositif. Testez également l'import du fichier de configuration sur un autre téléphone pour vous assurer que la sauvegarde fonctionne.

**Distribuez les clés intelligemment**. Pour les Tapsigners, remettez-les sous enveloppe scellée avec le PIN communiqué séparément (par exemple dans la lettre Recovery Instructions stockée ailleurs). Pour les hardware wallets classiques, conservez l'appareil chez un tiers de confiance et le seed sur papier ou métal chez vous ou chez un autre tiers. Notez le fingerprint de chaque clé et son nom dans le fichier de configuration pour éviter les confusions.

**Planifiez des tests périodiques** (fire drills). Annuellement, vérifiez que vous pouvez reconstruire le coffre à partir des sauvegardes sur un téléphone vierge. Testez les alertes Canary en vérifiant les soldes. Simulez des scénarios de perte (« et si je perdais la Coldcard ? ») pour confirmer que les combinaisons de clés restantes suffisent.

**N'oubliez pas le refresh**. Si vous avez configuré une Inheritance Key à 1 an, effectuez une transaction de refresh vers vous-même tous les 9-10 mois. Cette contrainte est le prix à payer pour bénéficier d'une transmission automatique sans intervention de tiers.

**Maintenez le plan à jour**. Tout changement (remplacement d'une clé, modification des héritiers, changement de délai) doit être répercuté sur toutes les sauvegardes et documents. Régénérez les PDF après chaque modification et redistribuez les nouvelles versions.

## Limites et considérations

Malgré la puissance de ces outils, il est important de reconnaître leurs limites pour les gérer au mieux.

La **complexité** d'un coffre multisig avec timelocks peut être un risque en soi : erreur de configuration, incompréhension par les héritiers, perte d'un élément critique parmi les nombreux composants. Bitcoin Keeper simplifie l'expérience au maximum, mais cela reste une opération technique. Ne déployez ce plan que si le montant à protéger le justifie. Pour de petits montants, un plan plus simple peut suffire.

La **dépendance à l'application** mérite réflexion. Bien que le code soit open source et basé sur des standards ouverts (Miniscript, BSMS), certaines fonctionnalités reposent sur l'écosystème Keeper. Conservez une copie de l'application (APK Android ou IPA iOS) et documentez dans vos lettres aux héritiers la possibilité d'utiliser d'autres wallets compatibles Miniscript (comme Liana) pour récupérer les fonds.

Les **tiers de confiance** introduisent un risque humain. Que se passe-t-il si un proche mal intentionné utilise la clé qui lui a été confiée avant l'expiration du délai ? Ou si l'avocat égare vos documents ? Choisissez ces personnes avec soin, expliquez clairement leurs responsabilités, et prévoyez des plans B. Les Canary Wallets, la redondance des sauvegardes, et la structure même du multisig restent vos meilleures protections contre ces aléas.

## Conclusion

Bitcoin Keeper, avec son plan Diamond Hands, offre une boîte à outils complète pour la planification successorale : Enhanced Vaults avec clés temporisées, documents d'accompagnement, Canary Wallets, et support personnalisé.

L'enjeu dépasse la technique : il s'agit de penser l'architecture de votre succession, de distribuer intelligemment les clés et les connaissances, et de tester régulièrement le dispositif. Un plan d'héritage Bitcoin bien conçu transforme vos satoshis en véritable patrimoine transmissible.
