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

## 1. Prérequis

L’application nécessite quelques prérequis pour fonctionner correctement. Tout d’abord, il ne s’agit pas d’une application disponible sur les boutiques classiques comme le Google Play Store ou l’App Store. Elle s’installe manuellement sur votre téléphone uniquement à partir de son fichier `.apk`, téléchargeable via le réseau Tor. Par conséquent, si vous utilisez un iPhone, cette méthode ne fonctionnera pas : il vous faut impérativement un appareil Android.

Pour télécharger le fichier `.apk` via Tor, vous aurez besoin d’un navigateur capable d’accéder aux sites en `.onion`. Le plus simple consiste à installer l’application Tor Browser sur votre téléphone, disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) ou directement [via son `.apk`](https://www.torproject.org/download/#android).

03

La plupart des smartphones récents bloquent par défaut l’installation d’applications provenant de sources inconnues. Vous devrez donc activer temporairement cette option pour Tor Browser dans les paramètres de votre appareil pour autoriser l’installation. Une fois l’application installée, pensez à désactiver cette fonction afin de renforcer la sécurité de votre téléphone.

Un autre prérequis indispensable pour utiliser Ashigaru est de disposer d’un nœud Bitcoin Dojo. Par souci de sécurité et de souveraineté, les équipes d’Ashigaru ne maintiennent aucun serveur centralisé pour connecter votre application. Vous devez donc obligatoirement faire tourner votre propre instance de Dojo, ou vous connecter à celle d’une personne de confiance.

Le Dojo permet à votre application Ashigaru de consulter les informations de la blockchain, de connaître le solde de vos adresses et de diffuser vos transactions sur le réseau Bitcoin.

Pour en savoir plus sur Dojo et apprendre à l’installer, je vous invite à suivre ce tutoriel dédié :

https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

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

## 3. Initialisation et création du portefeuille Bitcoin
































Ashigaru est un projet open-source. Si vous souhaitez faire un don pour aider au développement de l'application, vous pouvez le faire dans l'app PayNym.