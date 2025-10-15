---
name: SeedSigner
description: Construisez votre dispositif de signature, abordable et 100 % hors-ligne
---

![cover](assets/cover.webp)

Le SeedSigner est un hardware wallet Bitcoin open-source que chacun peut construire soi-même avec des composants électroniques généralistes bon marché. Contrairement à des produits commerciaux comme les Ledger, Coldcard ou Trezor, il ne s’agit pas d’un appareil prêt à l’emploi fabriqué par une entreprise : c’est un projet communautaire qui propose à chacun de créer son propre dispositif, en contrôlant chaque étape.

Le SeedSigner est conçu pour être 100 % ***air-gapped*** : il ne se connecte jamais à Internet, ne possède pas de Wi-Fi ni de Bluetooth (dans le cas du Raspberry Pi Zero v1.3) et n’est jamais branché à un ordinateur pour échanger des données. La communication se fait exclusivement via un système d’échange de QR codes. Concrètement, votre logiciel de gestion de portefeuille (comme Sparrow Wallet par exemple) affiche la transaction à signer sous forme de QR codes ; vous les scannez avec la caméra du SeedSigner, puis l’appareil signe la transaction en utilisant vos clés privées stockées temporairement dans sa mémoire vive. Enfin, il génère à son tour des QR codes contenant la transaction signée que vous scannez avec votre logiciel pour l’envoyer sur le réseau Bitcoin.

001

Le SeedSigner est également ***stateless***. Autrement dit, il n’enregistre pas votre seed ni vos clés privées de manière permanente, contrairement à d’autres hardware wallets. À chaque redémarrage, sa mémoire est totalement vide, sauf si vous configurez l’appareil pour sauvegarder vos paramètres sur une carte microSD. Vous devez donc réintroduire votre seed à chaque utilisation, la méthode la plus pratique consistant à la conserver sous forme de QR code, à scanner au démarrage grâce à la caméra du SeedSigner. Ce mode de fonctionnement réduit considérablement la surface d’attaque : même si un voleur s’empare de votre appareil, il n’y trouvera aucune information, puisqu’il est toujours vide par défaut.

Une autre option pour stocker votre seed et l’utiliser avec le SeedSigner est d'utiliser une carte à puce *SeedKeeper* associée à un lecteur compatible. Vous bénéficiez ainsi d’un *Secure Element* très robuste pour conserver votre seed, tout en utilisant l’écran du SeedSigner pour la signature des transactions. Mais cette configuration particulière est l’objet d’un autre tutoriel dédié. Ici, nous nous concentrerons sur l’utilisation de base du SeedSigner :

https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Le projet SeedSigner occupe une place importante dans l’écosystème Bitcoin, car il offre à chacun, partout dans le monde, la possibilité de bénéficier d’une sécurité avancée pour protéger ses bitcoins. Son principal atout réside dans son accessibilité : le matériel requis peut être acquis pour moins de 50 $. Plus encore, il permet aux personnes vivant dans des pays soumis à des restrictions de fabriquer leur propre hardware wallet à partir de composants informatiques standards, faciles à trouver et plus rarement soumis à des contraintes réglementaires.

Mais même en dehors de ces contextes particuliers, le SeedSigner peut représenter une option intéressante pour vous : il est open-source, fonctionne de manière stateless et airgapped, et permet de réduire les vecteurs d’attaques liés à la supply chain de votre hardware wallet.

## 1. Le matériel requis

Pour construire votre SeedSigner, vous aurez besoin des composants suivants :

- **Raspberry Pi Zero**
    - La version 1.3 est recommandée, car elle ne dispose ni de Wi-Fi ni de Bluetooth, ce qui assure une isolation complète.
	- Les versions W et v2 sont également compatibles, mais elles intègrent une puce Wi-Fi/Bluetooth. Il est alors conseillé de la désactiver physiquement en retirant le module radio de la carte. L’opération reste relativement simple, mais demande de la précision (une pince fine suffit pour le Zero W, tandis qu’un stylo chauffant est nécessaire pour la v2 afin de retirer la plaque de métal qui cache le module). Je ne détaillerai pas cette manipulation dans ce tutoriel, mais vous trouverez toutes les instructions dans ce document : *[Disabling WiFi/Bluetooth by hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
	- Attention : certains modèles de Raspberry Pi Zero sont vendus sans broches GPIO présoudées. Vous pouvez soit acheter directement une version avec broches intégrées (solution la plus simple), soit acheter les broches séparément et les souder vous-même (solution plus complexe).
	- Pensez également à prévoir une alimentation en micro-USB.

002

- **Écran Waveshare 1.3" (240×240 px)**
    - Choisissez impérativement ce modèle précis : d’autres écrans similaires existent, mais avec une résolution différente. Sans la définition 240×240 px, l’affichage sera inutilisable.
    - Cet écran intègre trois boutons ainsi qu’un mini-joystick servant d’interface utilisateur.

003

- **Caméra compatible Raspberry Pi Zero**
    - Option 1 : la caméra standard avec une nappe dorée large (vérifiez bien la compatibilité avec votre boîtier).
    - Option 2 : la caméra "Zero", plus compacte, conçue spécifiquement pour le Pi Zero.

004

- **Carte microSD**
    - Capacité recommandée : entre 4 et 32 Go.

- **Boîtier (optionnel mais recommandé)**
    - Protège le dispositif et facilite son utilisation.
    - Le modèle le plus répandu est le "Orange Pill Case", dont [les fichiers STL open-source sont disponibles pour impression 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Vous pouvez également vous procurer des boîtiers auprès [de revendeurs indépendants liés au projet](https://seedsigner.com/hardware/).

005

Vous pouvez acheter ces composants séparément ou, pour plus de simplicité, opter pour des packs tout prêts qui regroupent l’ensemble du matériel nécessaire. Personnellement, j’ai commandé mon pack [sur ce site français](https://bitcoinbazar.fr/), mais vous trouverez également une liste de vendeurs pour chaque région du monde sur [la page hardware du projet SeedSigner](https://seedsigner.com/hardware/). Si vous préférez acquérir les composants individuellement, ils sont disponibles sur les grandes plateformes de e-commerce ou dans des boutiques spécialisées.

## 2. Préparation du logiciel

Une fois le matériel réuni, il faut préparer la carte microSD en y installant le système SeedSigner. Pour ce faire, rendez-vous sur votre oridnateur personnel de tous les jours, et branchez y votre microSD destinée au SeedSigner.

### 2.1. Téléchargement

Rendez-vous sur [le dépôt GitHub officiel du projet](https://github.com/SeedSigner/seedsigner/releases). Sur la dernière version du logiciel, téléchargez :
- L’image en `.img` correspondant à votre modèle de Pi.
- Le fichier `.sha256.txt`.
- Le fichier `.sha256.txt.sig`.

006

Avant de commencer l'installation, nous allons vérifier le logiciel.

### 2.2 Vérification sous Linux et macOS

Commencez par importer la clé publique officielle du projet SeedSigner directement depuis Keybase :

```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```

007

Le terminal doit vous indiquer qu’une clé a bien été importée ou mise à jour. Ensuite, exécutez la commande de vérification sur le fichier de signature (pensez à modifier la commande en fonction de votre version, ici `0.8.6.`) :

```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```

008

Si tout est correct, la sortie doit afficher `Good signature`. Cela signifie que le fichier `.sha256.txt` a été signé par la clé que vous venez d’importer et que la signature est valide. Ignorez le message d’avertissement du type `WARNING: This key is not certified with a trusted signature` : il est normal, puisqu’il vous appartient maintenant de vérifier que la clé utilisée appartient bien au projet SeedSigner.

Pour ce faire, comparez les 16 derniers caractères de l’empreinte affichée avec ceux disponibles sur [Keybase.io/SeedSigner](https://keybase.io/seedsigner), sur leur [Twitter officiel](https://twitter.com/SeedSigner/status/1530555252373704707), ou dans le fichier publié sur [SeedSigner.com](https://seedsigner.com/keybase.txt). Si ces identifiants correspondent exactement, vous pouvez être certain que la clé est bien celle du projet. En cas de doute ou de différence, arrêtez-vous immédiatement et demandez de l’aide à la communauté SeedSigner (Telegram, X, GitHub...).

Lorsque la clé a été validée, vous pouvez vérifier que l’image téléchargée n’a pas été modifiée (pensez à modifier la commande en fonction de votre version, ici `0.8.6.`) :

```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```

009

- Sous Linux, cette commande est intégrée.
- Sous macOS, attention : les versions antérieures à `Big Sur (11)` ne reconnaissent pas l’option `--ignore-missing`. Dans ce cas, retirez-la et ignorez les avertissements concernant les fichiers manquants.

Le résultat attendu est un `OK` à côté du fichier `.img`. Cela confirme que l’image téléchargée est identique à celle publiée par le projet et n’a pas été modifiée.

### 2.3 Vérification sous Windows

Sous Windows, la procédure est similaire mais les commandes sont différentes. Commencez par installer [Gpg4win](https://www.gpg4win.org/) et ouvrez l’application *Kleopatra*. Importez la clé publique du projet SeedSigner à partir de l’URL Keybase :

```
https://keybase.io/seedsigner/pgp_keys.asc
```

010

Ensuite, ouvrez PowerShell dans le dossier où se trouvent vos fichiers téléchargés (`Shift` + clic droit > `Open PowerShell here`). Lancez la commande suivante pour vérifier la signature du manifeste (pensez à modifier la commande en fonction de votre version, ici `0.8.6.`) :

```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```

011

Si tout est correct, la sortie doit afficher `Good signature`. Cela signifie que le fichier `.sha256.txt` a été signé par la clé que vous venez d’importer et que la signature est valide. Ignorez le message d’avertissement du type `WARNING: This key is not certified with a trusted signature` : il est normal, puisqu’il vous appartient maintenant de vérifier que la clé utilisée appartient bien au projet SeedSigner.

Pour ce faire, comparez les 16 derniers caractères de l’empreinte affichée avec ceux disponibles sur [Keybase.io/SeedSigner](https://keybase.io/seedsigner), sur leur [Twitter officiel](https://twitter.com/SeedSigner/status/1530555252373704707), ou dans le fichier publié sur [SeedSigner.com](https://seedsigner.com/keybase.txt). Si ces identifiants correspondent exactement, vous pouvez être certain que la clé est bien celle du projet. En cas de doute ou de différence, arrêtez-vous immédiatement et demandez de l’aide à la communauté SeedSigner (Telegram, X, GitHub...).

Une fois la clé validée, il faut contrôler que le fichier image n’a pas été corrompu. Pour cela, utilisez la commande suivante dans PowerShell :

```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```

Exemple pour un Raspberry Pi Zero 2 (pensez à modifier la commande en fonction de votre version, ici `0.8.6.`) :

```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```

012

PowerShell calcule alors le hash SHA256 de votre fichier image. Comparez ce hash à la valeur correspondante contenue dans `seedsigner.0.8.6.sha256.txt`.
- Si les deux valeurs sont strictement identiques, la vérification est réussie et vous pouvez continuer.
- Si elles diffèrent, cela signifie que le fichier est corrompu ou altéré. Ne l’utilisez pas et recommencez le téléchargement.

013

Une vérification réussie garantit que votre fichier `.img` est à la fois authentique (signé par SeedSigner) et intègre (non modifié). Vous pouvez alors passer à l’étape suivante en toute sécurité.

### 2.4. Flash l’image

Si vous ne l'avez pas encore, téléchargez le logiciel [Balena Etcher](https://etcher.balena.io/), puis :
- Insérez la carte microSD dans votre ordinateur.
- Lancez Etcher.
- Sélectionnez le fichier `.img` téléchargé et vérifié.
- Choisissez la carte microSD comme cible.
- Cliquez sur `Flash!`.

014

Patientez jusqu’à la fin du processus : votre microSD est prête à l’emploi. Nous pouvons maintenant passer à l'assemblage !

## 3. Assemblage du SeedSigner

Une fois votre carte microSD préparée et flashée avec le logiciel SeedSigner, vous pouvez procéder à l’assemblage final de l’appareil. Prenez votre temps, car certaines pièces sont fragiles (notamment la nappe, la caméra et les broches GPIO).

### 3.1 Préparation du boîtier

Avant toute chose, ouvrez votre boîtier. Vérifiez qu’il est propre et qu’aucun résidu de plastique d’impression 3D ne gêne les fixations internes. Repérez bien :
- L’emplacement de la caméra (petit orifice circulaire à l’avant).
- L’ouverture pour l’écran.
- Les découpes pour les ports micro-USB et le lecteur microSD du Raspberry Pi Zero.

### 3.2 Installation de la caméra

Repérez sur le Raspberry Pi Zero le connecteur de la nappe de la caméra : c’est une fine barrette noire située sur le côté de la carte, pouvant se soulever légèrement pour s’ouvrir. Relevez-la avec précaution, sans forcer : elle doit simplement basculer de quelques millimètres.

015

Insérez la nappe de la caméra. La partie marron/cuivrée doit être orientée vers le bas. Assurez-vous qu’elle est bien enfoncée dans le connecteur, sans torsion.

016

Refermez la barrette noire pour verrouiller la nappe (vous sentirez un léger clic). Vérifiez doucement qu’elle tient et ne bouge pas.

017

Placez ensuite le module caméra dans l’orifice prévu du boîtier. Selon le modèle, il peut s’emboîter directement ou nécessiter un petit adhésif pour le maintenir. L’objectif doit être parfaitement aligné face à l’extérieur.

### 3.3 Installation du Raspberry Pi Zero

Si vous utilisez un boîtier, insérez la carte Raspberry Pi Zero à l’intérieur. Alignez soigneusement les ports avec les ouvertures prévues.

Positionnez ensuite l’écran Waveshare au-dessus du Raspberry Pi Zero. Les broches GPIO du Pi doivent s’aligner parfaitement avec le connecteur femelle de l’écran. Enfoncez lentement l’écran sur les broches, en exerçant une pression uniforme de chaque côté afin d’éviter de les tordre.

018

Si vous avez un boîtier, terminez le montage en ajoutant la face avant et le joystick.

Enfin, insérez la carte microSD contenant le logiciel flashé dans le lecteur du Raspberry Pi Zero, situé sur la tranche. Assurez-vous qu’elle soit bien enclenchée.

### 3.4 Premier démarrage

Branchez un câble d’alimentation micro-USB sur le port dédié. Patientez environ une minute. Le logo SeedSigner devrait apparaître, suivi de l’écran d’accueil.

019

Pour commencer, vérifiez le bon fonctionnement des différents éléments en vous rendant dans le menu `Settings > I/O test`.

020

Testez tous les boutons et assurez-vous qu’ils répondent correctement. Cliquez ensuite sur le bouton `KEY1` pour vérifier que la caméra fonctionne comme prévu. Cela va prendre une photo.

021

### 3.5 Ajustement de la caméra

Selon la manière dont vous avez monté votre SeedSigner, il se peut que la caméra affiche une image inversée. Pour corriger cela, rendez-vous dans `Settings > Advanced > Camera rotation` et sélectionnez une rotation de 180° si nécessaire.

022

Si vous avez modifié l’orientation de la caméra ou souhaitez ultérieurement changer d’autres paramètres (comme la langue de l’interface), il faut activer la persistance des paramètres sur la microSD. Sinon, vos réglages reviendront par défaut à chaque redémarrage, car le Raspberry Pi Zero ne dispose pas de mémoire persistante.

Pour cela, ouvrez le menu `Settings > Persistent settings`, puis sélectionnez `Enabled`.

023

Si tout est fonctionnel, votre SeedSigner est désormais prêt à être utilisé !

## 4. Paramétrage du SeedSigner

Avant de créer votre portefeuille Bitcoin, nous allons configurer le SeedSigner. Comme il fonctionne sur un Raspberry Pi Zero dépourvu de mémoire persistante, ses réglages ne sont pas enregistrés automatiquement à moins de les sauvegarder sur la carte microSD. Assurez-vous donc d’avoir activé cette option, sinon ce paramétrage sera perdu au redémarrage (voir l’étape 3.5).

### 4.1 Accès au menu des paramètres

Démarrez votre SeedSigner et attendez l’apparition de l’écran d’accueil. À l’aide du joystick, naviguez jusqu’à l’option `Settings`, puis validez en appuyant sur le bouton central. Vous entrez alors dans le menu principal des paramètres.

024

### 4.2 Choisir le logiciel de gestion de portefeuille

Accédez ensuite au menu `Coordinator software`.

025

Le `Coordinator` désigne le logiciel de gestion de portefeuille avec lequel votre SeedSigner communiquera via des QR codes. Ce logiciel est installé soit sur votre ordinateur, soit sur votre smartphone. C’est lui qui vous permettra de gérer vos bitcoins, mais sans jamais avoir accès à vos clés privées. Le SeedSigner reste le seul appareil capable de signer vos transactions.

La version actuelle du firmware prend en charge plusieurs logiciels : Sparrow, Specter, BlueWallet, Nunchuk et Keeper. Dans mon cas, j’utilise **Sparrow Wallet**, que je vous recommande particulièrement pour sa simplicité et sa richesse fonctionnelle.

Si vous ne savez pas comment l’installer, vous pouvez suivre ce tutoriel :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sélectionnez simplement le logiciel de votre choix dans le menu.

026

### 4.3 Unités et affichage des montants

Dans le menu `Denomination Display`, vous pouvez choisir l’unité d’affichage des montants :
- `BTC`
- `mBTC` (milli-bitcoin, soit 0,001 BTC)
- `sats` (satoshis, soit 1/100 000 000 de BTC)

L’unité en **sats** est généralement la plus pratique pour les petites sommes.

027

### 4.4 Réglages avancés

Rendez-vous maintenant dans le menu `Advanced`. Vous y trouverez plusieurs options utiles :
- `Bitcoin network` : à modifier uniquement si vous souhaitez utiliser le SeedSigner sur le Testnet.
- `QR code density` : ajuste la quantité d’informations contenue dans chaque QR code. Vous pouvez laisser la valeur par défaut, sauf si vous rencontrez des difficultés de lecture lors du scan.
- `Xpub export` : permet d’activer ou de désactiver l’exportation de votre clé publique étendue (`xpub`, `ypub`, `zpub`) vers un logiciel de gestion de portefeuille via QR code (fonction que nous utiliserons plus loin, donc laissez la activée pour le moment).
- `Script types` : définit les types de scripts autorisés pour verrouiller vos bitcoins. Vous n’avez pas besoin de modifier ce paramètre, car le type de script sera défini directement sur Sparrow. Ici, il s’agit uniquement des scripts que le SeedSigner est autorisé à manipuler.

### 4.5 Choix de la langue

Enfin, dans le menu `Language`, vous pouvez modifier la langue de l’interface selon votre préférence.

028























**[Vous pouvez soutenir le développement du projet open-source SeedSigner en effectuant un don en bitcoins !](https://seedsigner.com/donate/)**

*Crédit : certaines images de ce tutoriel proviennent du [site officiel du projet SeedSigner](https://seedsigner.com/) et [du dépôt GitHub](https://github.com/SeedSigner/seedsigner).*