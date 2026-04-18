---
name: BULL Wallet
description: Découvrez comment utiliser BULL Wallet
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Ce tutoriel vidéo de BTC Sessions vous guide à travers le processus de mise en place et d'utilisation de BULL Wallet !*


Ce guide vous explique l'installation, la configuration et l'utilisation de BULL Wallet. Vous apprendrez à envoyer et à recevoir des fonds sur les réseaux Bitcoin on-chain, Liquid et Lightning, ainsi qu'à déplacer des bitcoins entre eux. Les nombreuses fonctionnalités de ce portefeuille en font un outil puissant et tout-en-un pour la gestion de vos bitcoins. Commençons.


## Introduction


BULL Wallet, développé par [Bull Bitcoin](https://www.bullbitcoin.com/), est un portefeuille Bitcoin **autonome**, ce qui signifie que vous avez le contrôle total de vos clés privées et donc de vos fonds, sans dépendre d'une tierce partie. Open source et ancré dans une philosophie Cypherpunk, ce portefeuille combine simplicité, confidentialité et fonctionnalités avancées telles que les swaps inter-réseaux et la prise en charge de PayJoin. Il vous permet de gérer vos bitcoins sur trois réseaux : **Bitcoin on-chain**, **Liquid** et **Lightning**, chacun adapté à des utilisations spécifiques.

Sur le [GitHub de Bull Bitcoin](https://github.com/orgs/SatoshiPortal/projects/49), vous pouvez consulter les sujets actuels et les développements à venir. Comme le projet est 100% open source et "construit en public", vous pouvez également envoyer vos suggestions et les bugs que vous rencontrez. Alors que certains portefeuilles prennent désormais en charge plusieurs réseaux, BULL Wallet se distingue par une intégration poussée des fonctions de confidentialité sur chacun d'entre eux, ce qui en fait un outil puissant pour gérer vos bitcoins sur tous les principaux réseaux.


## 1️⃣ Conditions préalables


Avant de commencer à utiliser **BULL Wallet**, assurez-vous que vous disposez des éléments suivants :



- **Smartphone compatible** : Un appareil **iOS** (iPhone ou iPad) ou **Android** ;
- **Connexion Internet** ;
- **Sécuriser les supports de sauvegarde** : Notez votre **phrase de récupération** (12/24 mots) sur du papier ou du métal, et conservez-la en lieu sûr ;
- **Connaissances de base** : Une compréhension minimale des concepts de Bitcoin (adresses, transactions, frais) est utile, bien que ce tutoriel explique chaque étape pour les débutants.


## 2️⃣ Installation


Vous pouvez installer l'application via :



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(pour les appareils iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (pour les appareils Android)


Les utilisateurs d'Android disposent également d'autres options :



- Télécharger l'APK directement depuis la page [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) ou ;
- Installer via le [Zapstore compatible Nostr](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap).


Après avoir installé l'application, suivez l'écran de bienvenue pour configurer votre compte.


## 3️⃣ Configuration initiale


À l'ouverture, les options suivantes vous sont proposées :



- `Créer un nouveau portefeuille`
- `Restaurer le portefeuille`
- `Options Avancées`


Commençons par cliquer sur `Options Avancées`.


Ici, nous pouvons configurer les paramètres avancés avant de créer ou de restaurer un portefeuille :


1. Activez le proxy Tor pour acheminer le trafic sur le réseau Tor. L'application [Orbot app](https://orbot.app/en/) doit être installée et fonctionner avant d'être activée. *Le proxy Tor ne s'applique qu'à Bitcoin (pas à Liquid) et peut entraîner une connexion plus lente.*

2. Configurer un serveur Electrum personnalisé.

3. Ajustez les paramètres de `Recover Bull`. *Nous en apprendrons plus sur le [Recover Bull](https://recoverbull.com/) plus tard.*

4. Choisissez la langue de l'application.


Après avoir effectué tous les ajustements optionnels, appuyez sur `Terminé`. Si vous souhaitez réutiliser un Wallet existant, cliquez sur `Restaurer le portefeuille` et remplissez les 12/24 mots de votre phrase de récupération.


Sinon, cliquez sur `Créer un nouveau portefeuille`.


![image](assets/en/01.webp)


## 4️⃣ Écran d'accueil


Avant d'aller plus loin, jetons un coup d'œil à l'écran d'accueil pour nous orienter :



- Les menus `Historique de transactions` et `Paramètres` sont situés en haut à droite.
- L'affichage du solde dispose d'une option de confidentialité qui peut être activée ou désactivée.
- Accédez à `Bull Bitcoin Exchange` pour acheter, vendre ou payer (cela dépend de la juridiction et peut nécessiter un KYC).
- Transfert de fonds entre portefeuilles.
- `Bitcoin sécurisé` équivaut au portefeuille on-chain.
- `Paiements instantanés` via Liquid et le Lightning Network. *(Note : BULL Wallet permet d'effectuer et de recevoir des paiements via Lightning. Les fonds reçus via le LN sont stockés sur [Liquid](https://liquid.net/) (dans le portefeuille Paiements instantanés) grâce à un échange automatique via [Boltz exchange](https://boltz.exchange/). Cela vous permet d'interagir avec Lightning sans avoir à gérer des canaux de liquidité, tout en restant en self-custody.)*
- Envoi et réception de fonds.


![image](assets/en/02.webp)


Tout d'abord, faisons quelques configurations importantes et commençons par la "Sauvegarde".


## 5️⃣ Sauvegarde


Pour commencer le processus de sauvegarde, appuyez sur l'icône de l'engin (⚙) dans le coin supérieur droit de l'application et sélectionnez `Sauvegarde du portefeuille`, puis `Démarrer la sauvegarde`. Deux méthodes de sécurisation de votre portefeuille vous seront présentées : `Coffre-fort chiffré` et `Sauvegarde physique`. Explorons chacune d'entre elles.


![image](assets/en/03.webp)


### Sauvegarde physique


Tapez sur `Sauvegarde physique` pour voir une liste de 12 mots qui représentent votre phrase de récupération ou seed. Tenez compte des éléments suivants :



- Rédigez votre "phrase de récupération" (*seed phrase*) avec le plus grand soin. Notez-la sur du papier ou du métal et conservez-la en lieu sûr (coffre-fort, emplacement hors ligne). Cette *seed* est votre seul moyen d'accéder à vos bitcoins en cas de perte de votre appareil ou de suppression de l'application.
- Il est également important de noter que toute personne possédant cet ensemble de mots peut voler tous vos bitcoins. Ne les stockez jamais sous forme numérique.
- Pas de capture d'écran.
- Pas de sauvegardes dans le cloud, par courriel ou par messagerie.
- Pas de copier/coller (risque d'enregistrement dans le presse-papiers).


![image](assets/en/25.webp)


L'écran suivant vous demandera de placer les mots dans le bon ordre pour vous assurer que vous avez bien écrit la phrase de récupération. Vous recevrez une confirmation lorsque le test sera terminé et réussi.


! **Ce point est critique**. Pour plus d'assistance :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Coffre-fort chiffré


Il est également possible d'effectuer une sauvegarde cryptée et anonyme dans le cloud. Mais n'avons-nous pas mentionné dans le dernier paragraphe que les sauvegardes dans le cloud sont risquées et devraient être évitées ? Cependant, l'équipe Bull Bitcoin a mis au point un moyen astucieux de sécuriser le processus. Voici comment cela fonctionne :


`Recoverbull` est un protocole de sauvegarde qui simplifie la sécurisation de votre portefeuille Bitcoin en divisant la sauvegarde en deux parties. Tout d'abord, le fichier de sauvegarde de votre portefeuille est crypté sur votre appareil à l'aide d'une clé de cryptage puissante. Vous pouvez enregistrer ce fichier crypté où vous le souhaitez, par exemple sur Google Drive ou sur votre appareil. Deuxièmement, la clé de chiffrement nécessaire pour déverrouiller le fichier est stockée par le serveur de clés Recoverbull. Pour récupérer votre portefeuille, vous avez besoin à la fois du fichier de sauvegarde crypté et de la clé, à laquelle vous accédez à l'aide de votre code PIN ou de votre mot de passe. Cette conception garantit que votre sauvegarde sur le cloud est inutile et que le serveur de clés est inutile sans votre fichier de sauvegarde spécifique. Vos fonds restent ainsi en sécurité même si l'une des parties est compromise.


Pensez-y comme à un coffre-fort. Le fichier de sauvegarde crypté est la *boîte*, que vous pouvez stocker n'importe où (comme Google Drive). Votre code PIN de récupération est la *clé*, qui est stockée séparément par le serveur de clés Recoverbull. Un voleur devrait obtenir à la fois votre boîte spécifique et votre clé spécifique pour l'ouvrir. Cette conception garantit que même si quelqu'un obtient votre fichier de sauvegarde, il est inutile sans la clé du serveur, et la clé du serveur est inutile sans votre fichier de sauvegarde unique.


Pour en savoir plus sur le protocole de sauvegarde de [Recoverbull](https://recoverbull.com/).


Tapez sur `Coffre-fort chiffré`, ensuite sur `Continue` pour confirmer l'utilisation du serveur par défaut. La connexion sera acheminée à travers le réseau `Tor` pour assurer la confidentialité et l'anonymat.


**Comprendre vos codes PIN**



- `App Unlock PIN` : Le PIN optionnel défini dans `Paramètres > Code PIN de sécurité` pour verrouiller l'application sur votre téléphone.
- `Recovery PIN` : Le PIN obligatoire créé pendant le processus de sauvegarde du coffre-fort chiffré utilisé pour décrypter votre fichier de sauvegarde pendant la récupération.


Il s'agit de deux codes PIN distincts. N'oubliez pas votre code PIN de récupération, car il est essentiel pour restaurer votre portefeuille.


**Configuration du code PIN de récupération:**



- Vous devez créer un code PIN ou un mot de passe pour récupérer l'accès à votre portefeuille.
- Le code PIN / mot de passe doit être composé d'au moins 6 chiffres (par exemple, évitez les séquences simples telles que 123456, qui ne sont pas acceptées).
- Sans ce code PIN, la récupération du portefeuille est impossible.


Sélectionnez ensuite un fournisseur de coffre-fort :



- `Google Drive` ou
- un `emplacement personnalisé` (par exemple, votre appareil)


![image](assets/en/04.webp)


Maintenant, sauvegardez le `fichier de sauvegarde`. Ensuite, tapez sur `Test Recovery`, sélectionnez votre fichier de sauvegarde ou votre chambre forte, puis tapez sur `Déchiffrer coffre-fort`. Entrez votre `PIN` ou `Password`. Si tout a fonctionné, l'écran "Test terminé avec succès" apparaîtra.


### Étiquettes d'importation et d'exportation


Maintenant que nous avons créé notre *Backup*, jetons un coup d'œil sur les `Étiquettes`. BULL Wallet améliore la confidentialité et l'organisation en permettant aux utilisateurs de créer des étiquettes personnalisées pour leurs adresses de réception et leurs transactions. Ces étiquettes vous aident à catégoriser vos fonds, car les transactions envoyées à une adresse étiquetée hériteront de cette étiquette, et vous pouvez également étiqueter les transactions sortantes pour suivre leur changement. 

Le portefeuille est entièrement compatible avec la norme [BIP-329](https://bip329.org/), ce qui signifie que vous pouvez exporter toutes vos étiquettes dans un fichier et les importer dans un autre portefeuille. Cette fonction vous permet de sauvegarder l'historique de vos transactions et leurs catégories, ou de les migrer entre différentes instances du portefeuille, sans perdre votre organisation personnalisée.


![image](assets/en/05.webp)


## 6️⃣ Paramètres


Une fois votre sauvegarde principale sécurisée, explorons les autres fonctionnalités disponibles dans les paramètres.


### A - Sécuriser l'accès


Pour sécuriser l'application, naviguez vers `Paramètres` > `Paramètres de l'application`, et choisissez `Code PIN de sécurité`. Créez un code PIN fort pour verrouiller l'accès à votre portefeuille. Bien que cette étape soit facultative, elle est fortement recommandée pour empêcher tout accès non autorisé si quelqu'un d'autre utilise votre téléphone.


![image](assets/en/06.webp)


### B - Connexion à un nœud personnel (facultatif)


BULL Wallet se connecte par défaut à des serveurs Electrum : le premier géré par Bull Bitcoin et un serveur secondaire de Blockstream, tous deux considérés comme ne conservant aucun journal, ce qui réduit le risque de traçage.


Pour plus de confidentialité, vous pouvez connecter l'application à votre propre nœud Bitcoin via un serveur Electrum. Pour ce faire, tapez sur `Paramètres` > `Paramètres Bitcoin` > `Paramètres du serveur Electrum`, puis sur `Ajouter un serveur personnalisé` pour entrer l'adresse et les informations d'identification de votre serveur.


![image](assets/en/07.webp)


### C - Monnaie


Le solde disponible est affiché sur l'écran principal en `sats` et en `USD`. Pour changer cela, naviguez vers `Paramètres` > `Devise`. Là, vous pouvez basculer entre `sats/BTC` et sélectionner votre `Devise fiduciaire par défaut`.


![image](assets/en/08.webp)


### D - Réglages Bitcoin


Le menu `Paramètres Bitcoin` offre un accès profond aux configurations et aux données de base de votre portefeuille. Ici, vous pouvez inspecter les détails fondamentaux de vos portefeuilles `Bitcoin sécurisé` et `Paiements instantanés`, vous donnant une transparence et un contrôle total. Les principales caractéristiques de ce menu sont les suivantes :



- **Détails du portefeuille:** Naviguez jusqu'à votre portefeuille `Bitcoin sécurisé` ou `Paiements instantanés` pour voir les informations spécifiques.
- **Wallet Fingerprint:** Un identifiant unique pour votre portefeuille.
- **Clé publique (Pubkey):** La clé utilisée pour générer vos adresses de réception Bitcoin.
- **Descriptor:** Résumé technique de la structure de votre portefeuille.
- **Chemin de dérivation:** Le chemin spécifique utilisé pour générer toutes les adresses à partir de votre clé privée principale.
- **Address View:** Accédez à une liste de vos adresses de réception inutilisées et changez d'adresse (bientôt disponible).


En outre, vous avez la possibilité de :



- Activer les paramètres de transfert automatique pour définir un solde maximum du "portefeuille instantanés", qui sera ensuite automatiquement transféré vers le portefeuille `Bitcoin sécurisé`.
- Importer des portefeuilles génériques via la phrase `Mnemonic` ou importer `watch-only`
- Connecter les "portefeuilles matériels" (Hardware Wallet) : les dispositifs actuellement pris en charge sont ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade, Foundation Passport et Keystone.


## 7️⃣ Bull Bitcoin Exchange


Directement à partir du Wallet, vous avez accès à [l'exchange Bull Bitcoin](https://www.bullbitcoin.com/), ce qui vous permet d'acheter, de vendre et de payer avec du bitcoin sans quitter l'application. Cette intégration constitue une solution pratique pour gérer vos besoins en Bitcoin. Veuillez noter que l'accès à la plateforme et à ses services peut être restreint en fonction de votre juridiction, et qu'une vérification de la connaissance du client (KYC) peut être nécessaire pour se conformer aux normes réglementaires et utiliser toutes les fonctionnalités de la plateforme.


Pour commencer, tapez sur `Exchange` dans le coin inférieur droit, puis sur `S'inscrire` ou `Se connecter` à votre compte.


La plateforme offre les [caractéristiques suivantes](https://www.bullbitcoin.com/) :



- Acheter du bitcoin en self-custody à partir de votre compte bancaire
- Non-custodial
- Personnes physiques ou morales
- Retrait immédiat
- Pas de frais cachés
- Lightning Network disponible
- Aucune limite de transaction
- Option d'achats récurrents


![image](assets/en/09.webp)


Pour en savoir plus, consultez ce tutoriel :


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Réception des fonds


La réception de fonds avec **BULL Wallet** est simple et flexible, car elle prend en charge trois réseaux distincts adaptés à différents cas d'utilisation :



- Le réseau `Bitcoin (on-chain)` pour un stockage sécurisé à long terme.
- Le réseau `Liquid` pour des transactions rapides et plus confidentielles.
- Le réseau `Lightning` pour des paiements instantanés et peu coûteux.


L'application génère automatiquement l'adresse ou la facture appropriée en fonction du réseau sélectionné. Voici comment procéder pour chaque réseau.


### Réception via on-chain (réseau Bitcoin)


Pour recevoir des fonds on-chain, vous pouvez soit sélectionner l'option `Bitcoin sécurisé` sur l'écran d'accueil et appuyer sur `Recevoir`, soit appuyer sur le bouton principal `Recevoir` et choisir le "réseau Bitcoin".


Vous disposez de deux modes principaux pour générer une adresse de réception :


**Mode par défaut** (URI avec paramètres d'entrée supplémentaires)


Par défaut, le portefeuille génère un [BIP21 URI](https://bips.dev/21/). Il s'agit d'un format standardisé qui contient plus d'informations qu'une simple adresse, notamment un montant, une note personnelle et des paramètres PayJoin pour améliorer la confidentialité. Cet URI complet est encodé dans un code QR et mis à disposition pour être copié. Le format est le suivant : `bitcoin:<adresse>?<paramètre1>=<valeur1>&<paramètre2>=<valeur2>`.



- **Paramètres d'entrée supplémentaires :**
    - **Montant :** Spécifiez le montant demandé en BTC, sats, ou en monnaie fiduciaire.
    - **Message :** Ajoutez une note personnelle qui sera visible par l'expéditeur.
    - **PayJoin :** Activez cette option pour améliorer la confidentialité en combinant les données de l'expéditeur et du destinataire de la transaction.


Exemple d'URI :


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


***Note importante : N'envoyez pas de fonds aux adresses indiquées dans ce tutoriel, le Wallet sera supprimé.***


![image](assets/en/10.webp)


**Copier ou scanner l'adresse uniquement activée**


Si l'option `Copier ou scanner l'adresse uniquement` est activée, l'application génère une adresse Bitcoin simple au format SegWit (bech32).


Exemple :


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Même si vous saisissez un montant ou une note, ils ne seront pas inclus dans le QR code ou l'adresse copiée.


![image](assets/en/11.webp)


### Réception via Liquid


Vous pouvez recevoir un paiement sur le réseau Liquid. Une fois sur l'écran `Recevoir`, vous avez les deux mêmes options pour générer une demande de paiement :


**1. Adresse simple :** Copiez l'adresse standard `Liquid`. Il s'agit d'un identifiant unique pour votre portefeuille sur le réseau Liquid et n'inclut pas de montant ou de message spécifique.


Exemple d'adresse :


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Demande de paiement détaillée (URI) :** Pour une demande plus structurée, vous pouvez spécifier un montant et une note personnelle. Ces informations sont automatiquement encodées dans un URI partageable et dans le code QR correspondant.



- **Montant :** Vous pouvez définir le montant en Bitcoin (BTC), en Satoshis (sats), ou en monnaie fiduciaire.
- **Note :** Ajoutez un message personnel pour identifier la transaction.


**Exemple d'URI :**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Pour terminer la transaction, fournissez à l'expéditeur l'adresse ou l'IRU. Vous pouvez le faire en le copiant dans votre presse-papiers ou en demandant à l'expéditeur de scanner le QR code directement à partir de votre écran.


![image](assets/en/12.webp)


### Réception via Lightning



BULL Wallet vous permet également d'envoyer et de recevoir des paiements via le Lightning Network. Une caractéristique clé est que les fonds reçus via Lightning sont automatiquement échangés et stockés sur `Liquid` au sein de votre portefeuille `Paiements instantanés`. Ce service est alimenté par `Boltz`. 

Cette conception vous permet de profiter de la vitesse et du faible coût du Lightning sans la complexité de la gestion des canaux de liquidité, tout en maintenant la self-custody complète de vos fonds. Bien que cette approche hybride soit auto-dépositaire et évite la complexité de la gestion des canaux, elle introduit un service tiers (Boltz), une petite commission de swap et une dépendance à la fédération de fonctionnaires Liquid Network en tant que détenteurs de clés, ce qui est différent d'un portefeuille Lightning traditionnel, non-dépositaire, où vous gérez vos propres canaux. Pour en savoir plus sur Liquid et son modèle de gouvernance, cliquez ici :


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- **Limites :**
    - **Montant minimum :** Un montant minimum de facturation est requis. Veuillez consulter l'application pour connaître la limite actuelle.
    - **Frais :** Vous, le destinataire, êtes responsable d'une petite commission d'échange. Ces frais sont déduits du montant transféré par l'expéditeur et sont susceptibles d'être modifiés.
- **Avantages :**
    - **Self-Custodial :** Vos fonds sont toujours sous votre contrôle, sécurisés sur le réseau Liquid.
    - **Évitez les frais on-chain élevés :** En utilisant Lightning et en stockant sur Liquid, vous évitez les frais on-chain associés à l'ouverture d'un canal Lightning traditionnel. Vous pouvez choisir de déplacer les fonds vers un canal on-chain plus tard, lorsque le montant accumulé justifie la dépense.
    - **Conseil :** Pour la transaction la plus rentable entre deux utilisateurs Bull Bitcoin, utilisez directement le **réseau Liquid** pour éviter les frais d'échange Lightning.


Pour recevoir un paiement, vous devez établir une "invoice" (une facture) :


1. **Entrer le montant** : Spécifiez le montant que vous souhaitez recevoir en Bitcoin (BTC), en Satoshis (sats), ou en monnaie fiduciaire.

2. **Ajouter une note** (Optionnel) : Inclure un mémo ou une note. Celle-ci sera intégrée à la facture et affichée dans l'historique des transactions une fois le paiement effectué, ce qui permettra de l'identifier plus facilement.

3. **Validité de l'invoice** : La facture Lightning est sensible au temps et expire après **12 heures**. Si elle n'est pas payée dans ce délai, elle devient invalide et vous devrez en générer une nouvelle.


Fournissez la facture à l'expéditeur en la copiant dans votre presse-papiers ou en lui permettant de scanner le QR code affiché sur votre écran.


![image](assets/en/13.webp)


## 9️⃣ Envoi de fonds


Vous pouvez accéder à l'écran d'envoi directement depuis la page d'accueil ou depuis n'importe lequel de vos portefeuilles. BULL Wallet simplifie le processus en détectant automatiquement le réseau de destination - `Bitcoin`, `Liquid` ou `Lightning` - en fonction de l'adresse ou de la facture que vous saisissez, qu'elle soit collée ou scannée via un QR code.


### Transmission on-chain via le réseau Bitcoin


L'envoi de fonds on-chain signifie que votre transaction est enregistrée directement sur la blockchain Bitcoin. Cette méthode est la meilleure pour les transferts importants ou les transferts non sensibles au temps. Pour commencer, vous pouvez appuyer sur le bouton `Envoyer` en bas à droite, et scanner ou entrer une adresse Bitcoin standard.


Si l'adresse que vous fournissez ne mentionne pas de montant spécifique, vous serez invité à remplir les détails sur l'écran d'envoi. Vous pouvez spécifier le montant dans l'unité de votre choix, comme BTC, satoshis ou un équivalent en monnaie fiduciaire. Vous avez également la possibilité d'ajouter une note personnelle, qui est un mémo privé pour votre propre référence afin de vous aider à identifier la transaction plus tard. Cette note n'est pas communiquée au destinataire.


Inversement, si la demande de paiement que vous scannez ou collez contient déjà tous les détails nécessaires, comme un URI BIP21 avec un montant prédéfini, le portefeuille contournera l'écran de saisie des données et vous amènera directement à l'écran de confirmation pour autoriser le paiement.


![image](assets/en/14.webp)


Avant que votre transaction ne soit diffusée, un écran de confirmation s'affiche. Il est essentiel de prendre un moment pour examiner attentivement chaque paramètre, en accordant une attention particulière à l'adresse du destinataire, au montant envoyé et aux frais de réseau. Cet écran fournit également des outils puissants pour personnaliser votre transaction.


Vous pouvez contrôler les frais de deux manières principales. La première méthode consiste à sélectionner une vitesse de transaction souhaitée, par exemple faible, moyenne ou élevée, et le portefeuille calculera automatiquement les frais appropriés. La seconde méthode permet un contrôle plus précis en vous permettant de fixer un tarif spécifique, soit sous la forme d'un total absolu en satoshis, soit sous la forme d'un taux relatif par octet, qui fournit ensuite une estimation du temps de confirmation.


Pour les utilisateurs avancés, le portefeuille offre plusieurs réglages pour affiner la transaction. `Replace-by-Fee` (RBF) est activé par défaut, ce qui est une fonction précieuse qui vous permet d'accélérer une transaction si elle est bloquée dans le mempool en la rediffusant avec un tarif plus élevé. Vous pouvez également sélectionner manuellement les "sorties de transactions non dépensées" (UTXOs) à partir desquelles vous pouvez dépenser. Il s'agit d'un outil puissant pour la consolidation d'UTXO, une stratégie qui consiste à combiner plusieurs petites entrées en une seule plus importante. Bien que cela puisse coûter plus cher en frais pour la transaction en cours, cela peut réduire considérablement les frais sur les transactions futures, en particulier si les frais de réseau sont susceptibles d'augmenter.


![image](assets/en/15.webp)


PayJoin est automatiquement tenté lorsque vous scannez la demande de paiement d'un destinataire (un URI BIP21) qui comprend un paramètre `pj=`. Si vous collez simplement une adresse sans paramètres supplémentaires, cette fonctionnalité ne sera pas activée. Cette méthode collaborative améliore la confidentialité en combinant les données de l'expéditeur et du destinataire, en brisant l'heuristique de la propriété commune des données et en permettant une meilleure mise à l'échelle et des économies de frais dans certaines circonstances.


### Envoi via Liquid


Le réseau `Liquid` est conçu pour des transactions rapides et confidentielles avec des frais minimes. Lorsque vous envoyez des fonds par le biais de Liquid, ils sont retirés de votre portefeuille `Paiements instantanés`. La procédure est simple : il suffit de saisir ou de scanner l'adresse du destinataire (Liquid).


Si l'adresse ne précise pas de montant, il vous sera demandé d'en indiquer un sur l'écran d'envoi. Vous pouvez saisir le montant en BTC, en satoshis ou en monnaie fiduciaire. L'un des principaux avantages de Liquid est son seuil minimum peu élevé. Comme pour les transactions on-chain, vous pouvez ajouter une note personnelle facultative pour vos propres dossiers. Si la demande de paiement comprend déjà un montant, le portefeuille passera directement à l'écran de confirmation.


Sur l'écran de confirmation d'une transaction Liquid, vous pouvez consulter les détails. Les frais sont particulièrement bas et sont calculés en fonction de la complexité de la transaction. Ils sont généralement de l'ordre de 0,1 sat/vB, ce qui, pour une transaction simple, représente seulement 20 à 40 satoshis (par exemple, 26 satoshis au 21 décembre 2025).


![image](assets/en/16.webp)


### Envoi via Lightning Network


Vous pouvez soit envoyer à une adresse Lightning (par exemple `runningbitcoin@rizful.com`) qui vous permet de définir le montant et une note facultative pour le destinataire, soit scanner une facture avec un montant prédéfini, ce qui vous permet d'accéder directement à l'écran de confirmation.


*Des montants minimums et des frais s'appliquent.*


BULL Wallet envoie des paiements Lightning en retirant des fonds de votre portefeuille `Paiements instantanés` (sur Liquid) et en les échangeant via `Boltz`. Cette approche hybride est entièrement autonome et évite les frais élevés de gestion d'un canal Lightning dédié, mais elle nécessite de payer des "frais d'échange". Pour le coût le plus bas, envoyez directement à l'adresse Liquid d'un destinataire s'il utilise également un BULL Wallet.


## 🔟 Transférer des fonds entre vos portefeuilles


BULL Wallet vous permet de transférer vos bitcoins entre vos portefeuilles `Bitcoin sécurisé` et `Paiements instantanés` sur le réseau Liquid, ou vers un portefeuille externe. Pour effectuer un transfert, il vous suffit de vous rendre dans la section `Transfer`, de sélectionner les portefeuilles source et destination, d'entrer le montant que vous souhaitez transférer et de confirmer la transaction.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Récupération de votre BULL Wallet


Cette section explique comment retrouver l'accès à vos fonds BULL Wallet si vous perdez votre appareil, désinstallez l'application, ou avez simplement besoin d'en changer. Comme nous l'avons déjà expliqué, il existe deux méthodes principales de récupération : la méthode unique `Recoverbull` et la méthode standard `BIP39 seed phrase`.


### Méthode 1 : Recoverbull


Récapitulation : Les sauvegardes de portefeuilles sont cryptées localement. Le fichier crypté peut être stocké dans un espace de stockage cloud, ou sur un autre appareil. La clé de chiffrement est stockée par le serveur de clés Recoverbull. Les deux sont séparés et doivent être combinés pour récupérer un portefeuille.


Pour commencer, je vais supprimer le portefeuille avec tous les fonds qu'il contient et le réinstaller. Nous arriverons à nouveau sur l'écran d'accueil. Cette fois, sélectionnez l'option `Restaurer le portefeuille`. Ensuite, naviguez vers la méthode `Coffre-fort chiffré`, confirmez l'utilisation du `Serveur de clés par défaut`, et sélectionnez l'emplacement ou le `Vault provider` où vous avez stocké le fichier de sauvegarde.


![image](assets/en/18.webp)


Il indique que le coffre-fort a été importé avec succès. Appuyez sur le bouton `Déchiffrer le coffre-fort` et entrez le "PIN". L'écran suivant affichera vos `balances` et le `nombre de transactions` qui ont été récupérées.


![image](assets/en/19.webp)


### Méthode 2 : Seed Phrase


Cette méthode utilise la phrase de récupération principale de votre portefeuille, une liste standard de 12/24 mots qui sert de sauvegarde ultime pour vos fonds. C'est la façon la plus universelle de récupérer un portefeuille Bitcoin, car elle n'est liée à aucun service ou serveur spécifique. Tant que vous avez cette phrase, vous pouvez restaurer votre portefeuille sur n'importe quel appareil compatible, même sans accès au serveur de clés Bull Bitcoin.


Dans l'écran de bienvenue, sélectionnez `Restaurer le portefeuille`. Cette fois, choisissez la méthode `Sauvegarde physique`. L'application présente une grille de mots. Sélectionnez soigneusement chaque mot de votre phrase de 12/24 mots dans le bon ordre. Soyez méticuleux, car une seule erreur se traduira par un portefeuille incorrect.


## 1️⃣2️⃣ Connexion d'un Hardware Wallet


Pour un niveau de sécurité maximal, de nombreux utilisateurs de Bitcoin choisissent de stocker leurs fonds dans un "Cold Wallet". Cela signifie que les "clés privées" qui contrôlent vos bitcoins sont conservées sur un appareil qui n'est jamais connecté à Internet. Un "Hardware Wallet" (ou dispositif de signature) est un dispositif physique spécialisé conçu à cette fin précise. Il agit comme un coffre-fort numérique pour vos clés, garantissant qu'elles ne sont jamais exposées aux menaces potentielles d'un ordinateur ou d'un smartphone en ligne.


En connectant un Hardware Wallet à l'application BULL Wallet, vous obtenez le meilleur des deux mondes : la sécurité sans compromis du stockage à froid de vos clés privées, combinée aux puissantes fonctions et à l'interface conviviale de BULL Wallet pour la consultation des soldes et la gestion des transactions. Dans ce dernier chapitre, nous vous montrerons comment connecter un Hardware Wallet, tel qu'un [Coldcard Q](https://coldcard.com/q), à votre BULL Wallet. Ce tutoriel n'aborde pas en profondeur la configuration d'un Coldcard Q ; vous pouvez en savoir plus à ce sujet ici :


https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importation d'un portefeuille


![image](assets/en/26.webp)


Tout d'abord, dans le menu principal de votre Coldcard Q, sélectionnez `Export Wallet`, puis choisissez `BULL Wallet`. Votre Coldcard va générer et afficher un QR code.


![image](assets/en/20.webp)


Ouvrez BULL Wallet et naviguez vers `Paramètres` > `Paramètres Bitcoin` > `Importer un portefeuille` et sélectionnez `Coldcard Q` sur votre téléphone et appuyez sur `Ouvrir la caméra` pour scanner le QR code afin d'importer les clés publiques de votre Hardware Wallet.


![image](assets/en/21.webp)


### Réception avec Coldcard Q


Pour recevoir du bitcoin en utilisant votre Coldcard Q, vous n'avez pas besoin que l'appareil soit physiquement connecté à votre téléphone. BULL Wallet a déjà importé les clés publiques nécessaires, ce qui lui permet de gérer les adresses de réception par lui-même.


1. Appuyez sur votre dispositif de signature Coldcard Q importé et sélectionnez `Recevoir`.

2. L'application affichera automatiquement une nouvelle adresse Bitcoin provenant du portefeuille de votre Coldcard.

3. Utilisez cette adresse pour recevoir des fonds. Les bitcoins seront sécurisés directement avec les clés du Hardware Wallet, même si l'appareil était hors ligne pendant le processus.


![image](assets/en/22.webp)


### Envoi avec Coldcard Q


L'envoi de bitcoin avec votre Coldcard Q nécessite votre confirmation physique pour autoriser toute transaction. Bien que l'application BULL Wallet soit utilisée pour créer la transaction, la signature finale ne peut être créée que sur le Hardware Wallet lui-même.


Pour commencer, ouvrez votre `Coldcard Q` et tapez sur `Envoyer`. Ensuite, ouvrez la caméra pour scanner le QR code de l'adresse de réception. Après avoir scanné, entrez le montant que vous voulez envoyer et ajustez la priorité des frais si nécessaire.


Pour plus d'options, vous pouvez consulter la rubrique `Paramètres avancés`. Vous y trouverez l'option `Replace by Fee` (RBF), qui est activée par défaut et vous permet d'accélérer une transaction bloquée ultérieurement. Vous avez également l'option `Coin Control`, qui vous permet de sélectionner manuellement les UTXOs spécifiques que vous souhaitez dépenser.


Une fois que vous avez examiné tous les détails, appuyez sur `Show PSBT` pour préparer la transaction.


![image](assets/en/23.webp)


Appuyez sur le bouton `Scan` de votre Coldcard Q et utilisez son appareil photo pour scanner le QR code affiché sur votre téléphone. L'écran du Coldcard vous montrera alors tous les détails de la transaction. Vérifiez soigneusement le montant, l'adresse du destinataire et votre adresse de change. Si tout est correct, appuyez sur le bouton `Entrer` du Coldcard Q pour signer la transaction. Ensuite, un QR code de la transaction signée apparaîtra sur l'écran.


![image](assets/en/24.webp)


Sur BULL Wallet, tapez sur `J'ai fini`, puis sur le bouton `Caméra` pour scanner le QR code de la transaction signée de votre Coldcard Q. BULL Wallet affichera alors un écran récapitulatif de la transaction signée. Passez-la en revue une dernière fois, puis appuyez sur le bouton `Diffuser la transaction`. Ceci finalise le processus en envoyant la transaction au réseau Bitcoin, et vos fonds seront en route.


## 🎯 Conclusion


Vous avez maintenant terminé votre parcours dans l'application BULL Wallet. L'application met de puissants outils de confidentialité et de sécurité à portée de main, en rendant les fonctionnalités avancées simples à utiliser. Elle vous aide à rester privé grâce à des fonctionnalités telles que `PayJoin`, qui cache vos transactions sur la blockchain, et l'intégration de Tor, qui masque votre activité réseau aux regards indiscrets. Pour ceux qui veulent un contrôle ultime, vous pouvez vous connecter à votre propre nœud Bitcoin pour ne plus dépendre de serveurs tiers, et utiliser un Hardware Wallet pour garder vos clés privées complètement hors ligne et en sécurité. Avec des options de sauvegarde intelligentes et un support transparent pour Bitcoin, Liquid et Lightning, BULL Wallet est un choix solide et tout-en-un pour tous ceux qui veulent garder leurs fonds privés, sécurisés et entièrement sous leur propre contrôle.


## 📚 Ressources BULL Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Site web ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)
