---
name: Ashigaru
description: Le fork de Samourai Wallet pour sécuriser, gérer et mixer vos bitcoins
---

![cover](assets/cover.webp)

Ashigaru est une application mobile de portefeuille Bitcoin qui s’inscrit dans la continuité du projet Samourai Wallet, sous une nouvelle forme. Ce logiciel est né dans un contexte particulier : en avril 2024, les fondateurs de Samourai Wallet ont été arrêtés par les autorités américaines, et leurs serveurs ont été saisis. Bien que l’application Samourai elle-même soit restée utilisable, elle n'est actuellement plus maintenue. Ashigaru est un fork libre de Samourai Wallet, maintenu par une équipe anonyme, pour garantir la pérennité des fonctionnalités de Samourai et la sauvegarde de sa philosophie initiale : défendre la confidentialité et la souveraineté des utilisateurs de Bitcoin.

Ashigaru reprend l’essentiel de l’ADN de Samourai : une interface similaire, une approche évidemment self-custodial, open source et axée sur la protection de la vie privée. Le code est distribué sous licence GNU GPLv3, ce qui assure à chacun la possibilité d’auditer, de modifier ou de redistribuer le logiciel.

L’application Ashigaru intègre un ensemble d’outils avancés pour la confidentialité et la gestion de vos UTXOs :
- **Whirlpool**, un protocole de coinjoin basé sur Zerolink, permettant de rompre les liens déterministes entre entrées et sorties de transactions, sans perte de souveraineté sur ses fonds.
- **PayNym**, qui implémente des codes de paiement réutilisables (BIP47), désormais représentés via un système d’avatars "Pepehash".
- **Ricochet**, une fonctionnalité ajoutant des sauts intermédiaires aux transactions pour compliquer leur traçage.
- Évidemment du ***Coin Control*** pour sélectionner, geler et étiqueter précisément ses UTXOs.
- Du ***Batch Spending***, permettant de réduire les frais en regroupant plusieurs paiements dans une seule transaction.
- Le **Stealth Mode**, qui cache l’application sur votre mobile derrière un lanceur factice pour passer inaperçue lors d’une inspection physique de votre téléphone.
- Des outils de dépense avancés pour optimiser votre confidentialité (payjoin, stonewall...).
- Un système de récupération optimisé avec l'utilisation de Passphrase BIP39.
- Un système d'optimisation automatique du choix des frais de transaction.

01

Ashigaru s’adresse donc aux utilisateurs conscients des enjeux liés à la traçabilité des transactions sur Bitcoin. Que vous soyez un utilisateur soucieux de préserver sa confidentialité, un bitcoiner aguerri attaché à la self-custody, ou encore un individu exposé à des risques de surveillance accrue, cette application de portefeuille vous fournit les outils nécessaires pour reprendre la main sur votre activité sur Bitcoin.

Ashigaru est disponible en version mobile via son application, que nous allons explorer dans ce tutoriel. Mais il peut également être utilisé sur ordinateur grâce à ***Ashigaru Terminal***, que nous présenterons dans un prochain tutoriel.

02

Je vous propose que, dans ce tutoriel, nous découvrions ensemble l’utilisation de base d’Ashigaru : installation, connexion au Dojo, sauvegarde, réception et envoi de bitcoins. Les outils avancés seront présentés dans d’autres tutoriels dédiés.

## 1. Prérequis pour Ashigaru

L’application nécessite quelques prérequis pour fonctionner correctement. Tout d’abord, il ne s’agit pas d’une application disponible sur les boutiques classiques comme le Google Play Store ou l’App Store. Elle s’installe manuellement sur votre téléphone uniquement à partir de son fichier `.apk`, téléchargeable via le réseau Tor. Par conséquent, si vous utilisez un iPhone, cette méthode ne fonctionnera pas : il vous faut impérativement un appareil Android.

Pour télécharger le fichier `.apk` via Tor, vous aurez besoin d’un navigateur capable d’accéder aux sites en `.onion`. Le plus simple consiste à installer l’application Tor Browser sur votre téléphone, disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) ou directement [via son `.apk`](https://www.torproject.org/download/#android).

03

La plupart des smartphones récents bloquent par défaut l’installation d’applications provenant de sources inconnues. Vous devrez donc activer temporairement cette option pour Tor Browser dans les paramètres de votre appareil pour autoriser l’installation. Une fois l’application installée, pensez à désactiver cette fonction afin de renforcer la sécurité de votre téléphone.

Un autre prérequis indispensable pour utiliser Ashigaru est de disposer d’un nœud Bitcoin Dojo. Par souci de sécurité et de souveraineté, les équipes d’Ashigaru ne maintiennent aucun serveur centralisé pour connecter votre application. Vous devez donc obligatoirement faire tourner votre propre instance de Dojo, ou vous connecter à celle d’une personne de confiance.

Le Dojo permet à votre application Ashigaru de consulter les informations de la blockchain, de connaître le solde de vos adresses et de diffuser vos transactions sur le réseau Bitcoin.

Pour en savoir plus sur Dojo et apprendre à l’installer, je vous invite à suivre ce tutoriel dédié :

https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Si vous n’avez vraiment pas la possibilité de faire tourner votre propre Dojo, vous pouvez trouver des personnes acceptant de partager gracieusement leur instance sur le site [dojobay.pw](https://www.dojobay.pw/mainnet/). Cela peut constituer une solution temporaire, mais à long terme, je vous recommande d’utiliser votre propre Dojo pour garantir votre souveraineté et votre confidentialité.

## 2. Vérifier et installer l'application Ashigaru

### 2.1. Télécharger l'application Ashigaru

Sur votre téléphone, ouvrez Tor Browser et rendez-vous sur [le site officiel d’Ashigaru](https://ashigaru.rs/download/), dans la section `Download`. Cliquez ensuite sur le bouton `Download for Android` pour télécharger le fichier d’installation.

04

Avant d’installer l’application sur votre appareil, nous allons vérifier son authenticité et son intégrité. Cette étape est très importante, surtout lorsque l’on installe une application directement à partir d’un fichier `.apk`.

### 2.2. Vérifier l'application Ashigaru

Retournez sur [le site officiel d’Ashigaru](https://ashigaru.rs/download/) dans la section `Download`, puis copiez le message affiché sous le titre `SHA-256 Hash of the APK file`. Copiez l’intégralité du bloc, de `BEGIN PGP SIGNED MESSAGE` jusqu’à `END PGP SIGNATURE`.

05

Toujours sur votre téléphone, ouvrez un nouvel onglet dans Tor Browser et accédez à [l’outil de vérification Keybase](https://keybase.io/verify). Collez dans le champ prévu le message que vous venez de copier, puis cliquez sur le bouton `Verify`.

06

Si la signature est authentique, Keybase affichera un message confirmant que le fichier a bien été signé par les développeurs d’Ashigaru. Vous pouvez également cliquer sur le profil `ashigarudev` indiqué par Keybase et vérifier que l’empreinte de leur clé correspond exactement à : `A138 06B1 FA2A 676B`.

En revanche, si une erreur apparaît à cette étape, cela signifie que la signature n’est pas valide. Dans ce cas, **n’installez pas l’APK**. Reprenez la procédure depuis le début ou demandez de l’aide à la communauté avant de poursuivre.

07

Keybase vous a fourni le hachage de l’application. Nous allons maintenant vérifier que le hachage du fichier `.apk` que vous avez téléchargé correspond bien à celui vérifié sur Keybase. Pour cela, rendez-vous sur le site [HASH FILE ONLINE](https://hash-file.online/).

08

Cliquez sur le bouton `BROWSE...` et sélectionnez le fichier `.apk` téléchargé à l’étape 2.1.  
Choisissez ensuite la fonction de hachage `SHA-256`, puis cliquez sur `CALCULATE HASH` pour calculer le hachage de votre fichier.

09

Le site vous affichera le hachage de votre fichier `.apk`. Comparez-le à celui que vous avez vérifié sur Keybase.io. Si les deux hachages sont identiques, la vérification d’authenticité et d’intégrité est réussie. Vous pouvez alors procéder à l’installation de l’application.

10

### 2.3. Installer l'application Ashigaru

Pour installer l’application, ouvrez le gestionnaire de fichiers de votre téléphone et accédez au dossier des téléchargements. Cliquez ensuite sur le fichier `.apk` que vous venez de vérifier, puis confirmez l’installation lorsque le système vous le propose.

11

Ashigaru est désormais installé sur votre téléphone.

## 3. Initialiser l'app et créer un portefeuille Bitcoin

Lors du premier lancement de l’application, sélectionnez `MAINNET`.

12

Cliquez ensuite sur `Get Started`.

13

Nous allons maintenant créer un nouveau portefeuille Bitcoin. Appuyez sur le bouton `Create a new wallet`.

14

### 3.1. Créer un portefeuille Bitcoin

Ashigaru fonctionne obligatoirement avec une passphrase BIP39. Choisissez votre passphrase et saisissez-la dans les champs correspondants. Elle doit être aussi longue et aléatoire que possible afin de résister à une attaque par brute force.

Effectuez immédiatement une sauvegarde physique de cette passphrase. C’est une étape très importante : en cas de perte de votre téléphone, **si vous n’avez plus cette passphrase, vous ne pourrez plus accéder à vos bitcoins** stockés avec votre portefeuille Ashigaru. Cette même passphrase sert également à chiffrer le fichier de récupération du portefeuille.

Si vous ne savez pas ce qu’est une passphrase ou si vous ne comprenez pas parfaitement son fonctionnement, je vous recommande vivement de lire ce tutoriel complémentaire. C’est important, car la passphrase est un élément critique de votre sécurité : une mauvaise compréhension de son usage pourrait entraîner la perte définitive de vos fonds.

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Une fois votre passphrase saisie, cliquez sur `NEXT`.

15

Choisissez ensuite un code PIN. Ce code servira à déverrouiller votre portefeuille Ashigaru et protège ainsi contre tout accès physique non autorisé. Il n’intervient pas dans la dérivation cryptographique des clés de votre portefeuille. Cela signifie que, même sans connaître ce code PIN, toute personne possédant votre phrase mnémonique et votre passphrase pourra retrouver l’accès à vos bitcoins.

Optez pour un code PIN long et aléatoire. Pensez à en conserver une copie de sauvegarde dans un lieu distinct de votre téléphone, afin d’éviter qu’ils ne soient compromis simultanément.

16

Une fois le code PIN créé, Ashigaru affiche la phrase mnémonique de votre portefeuille. Attention : cette phrase, combinée à votre passphrase, donne un accès complet à vos bitcoins. Toute personne qui la détient peut s’emparer de vos fonds, même sans avoir accès à votre téléphone. Cette suite de 12 mots permet de restaurer votre portefeuille en cas de perte, de vol ou de casse de votre téléphone. Il est donc important de la sauvegarder avec le plus grand soin sur un support physique (papier ou métal).

Ne sauvegardez jamais cette phrase sous forme numérique, au risque d’exposer vos fonds à un vol. Selon votre stratégie de sécurité, vous pouvez créer plusieurs copies physiques, mais ne la divisez jamais. Conservez les mots dans leur ordre exact et veillez à ce qu’ils soient numérotés.

Enfin, ne stockez jamais la phrase mnémonique et la passphrase au même endroit. Si les deux étaient compromis simultanément, un attaquant pourrait accéder à votre portefeuille.

17

Pour approfondir les bonnes pratiques de sécurisation de votre phrase mnémonique, je vous invite à consulter ce tutoriel complémentaire :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru vous demande ensuite de confirmer une nouvelle fois votre passphrase. Profitez-en pour vérifier que votre sauvegarde physique est exacte.

18

### 3.2. Connecter un Dojo

Vient ensuite l’étape de connexion à votre Dojo. Comme expliqué en introduction, Ashigaru doit être relié à un Dojo pour pouvoir interagir avec le réseau Bitcoin.

Connectez-vous au "Maintenance Tool" de votre Dojo et ouvrez le menu `PAIRING`.

19

Sur Ashigaru, appuyez sur le bouton `Scan QR`, puis scannez le QR code de connexion affiché par votre DMT. Cliquez ensuite sur `Continue` pour confirmer.

20

Entrez votre code PIN pour déverrouiller le portefeuille. Vous accéderez alors à la page de synchronisation. Il est normal d’y voir des erreurs liées à *PayNym* à ce stade, puisque le portefeuille est nouveau. Cliquez simplement sur `Continue`.

21

Vous arrivez ensuite sur la page d’accueil de votre portefeuille.

22

Avant d’aller plus loin, je vous recommande de réaliser un test de récupération tant que le portefeuille ne contient encore aucun bitcoin. Cela vous permettra de vérifier que vos sauvegardes papier fonctionnent correctement. Pour savoir comment procéder, suivez ce tutoriel :

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Paramétrer l'application Ashigaru

Pour accéder aux paramètres de l’application, cliquez sur l’image de votre *PayNym* située en haut à gauche, puis sélectionnez `Settings`.

23

Vous trouverez ici plusieurs options permettant d’adapter le fonctionnement d’Ashigaru à vos besoins. Cependant, je vous recommande vivement d’activer dès le départ 2 paramètres importants.

Commencez par ouvrir le menu `Security > Stealth mode`, puis activez cette fonctionnalité si vous en avez besoin. Elle permet de masquer l’application Ashigaru derrière le nom, le logo et l’interface d’une application ordinaire installée sur votre téléphone. L’objectif est d’empêcher quiconque d’identifier Ashigaru en cas d’inspection physique de votre téléphone.

24

Chaque fausse application proposée dispose d’une méthode spécifique pour déverrouiller la véritable interface d’Ashigaru. Par exemple, si vous choisissez la calculatrice, l’application Ashigaru disparaît de votre écran d’accueil et est remplacée par une fausse calculatrice. Lorsque vous l’ouvrez, vous voyez une interface classique de calculatrice fonctionnelle, mais pour accéder à Ashigaru, il vous suffit de taper cinq fois rapidement sur le symbole `=`.

Le second paramètre important à activer est le [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Cette option vous permettra d’augmenter les frais d’une transaction si elle reste bloquée dans les mempools à cause de frais trop faibles. Vous pouvez l’activer via le menu `Transactions > Spend using RBF`.

25

## 5. Recevoir des bitcoins sur Ashigaru





## 6. Envoyer des bitcoins avec Ashigaru





## 7. Récupérer son portefeuille Ashigaru

La récupération d’un portefeuille Ashigaru diffère légèrement de celle d’un portefeuille Bitcoin classique, car l’application reprend les méthodes de Samourai Wallet. Si vous perdez l’accès à votre portefeuille (que ce soit à cause d’un oubli de PIN, d’une désinstallation, ou de la perte du téléphone) plusieurs solutions s’offrent à vous pour récupérer vos bitcoins.

Si vous avez encore accès à votre téléphone, ou si vous aviez fait un backup de ce fichier, la méthode la plus simple consiste à utiliser le fichier de sauvegarde `ashigaru.txt`. Ce fichier contient toutes les informations nécessaires pour restaurer votre portefeuille sur une nouvelle instance d’Ashigaru (ou sur Sparrow Wallet), mais il est chiffré avec la passphrase que vous avez définie à l’étape 3.1 de ce tutoriel. Vous devez donc impérativement disposer à la fois du fichier `ashigaru.txt` et de votre passphrase pour utiliser cette méthode.

Avec ces deux éléments, vous pouvez par exemple restaurer votre portefeuille sur Sparrow Wallet.

000

Si vous n’avez pas accès au fichier `ashigaru.txt`, vous pouvez tout de même retrouver l’accès à vos fonds en utilisant votre phrase mnémonique et votre passphrase, comme pour n’importe quel autre portefeuille Bitcoin. Je vous recommande d’effectuer cette restauration soit sur une nouvelle instance d’Ashigaru, soit directement sur Sparrow Wallet, afin de récupérer facilement les chemins de dérivation de Whirlpool si vous l’utilisiez. Sinon, vous pouvez aussi importer ces informations dans n’importe quel autre logiciel compatible BIP39 en saisissant manuellement les chemins de dérivation.

Pour plus d’informations sur ce processus, je vous invite à consulter le tutoriel complet que j’ai rédigé sur la récupération d’un portefeuille Samourai Wallet. Puisqu’Ashigaru en est un fork, la procédure est identique :

https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Comme vous avez pu le constater, quelle que soit la méthode de restauration utilisée, la passphrase est indispensable. Assurez-vous donc de la sauvegarder avec soin. Vous pouvez également en faire plusieurs copies en fonction de votre stratégie de sécurisation.

## 8. Faire un don au projet Ashigaru

Ashigaru est un projet open-source. Si vous souhaitez faire un don pour aider au développement de l'application, vous pouvez le faire dans l'applicaiton via PayNym.

Pour ce faire, cliquez sur votre PayNym en haut à droite de l'interface
