---
name: Envoy
description: Configurer et utiliser un Passport avec l'application Envoy
---
![cover](assets/cover.webp)


Envoy est une application de gestion de portefeuille Bitcoin développée par Foundation. Elle est spécialement conçue pour être utilisée avec le hardware wallet Passport.

Le Passport "*Batch 2*" que nous présentons dans ce tutoriel avec l'application Envoy est le successeur de l'édition "*Founder's Edition*". Il se distingue par son design premium, un écran couleur haute définition et un clavier physique ergonomique. Il fonctionne en mode "*Air-Gap*", ce qui garantit que les clés privées de votre portefeuille restent totalement isolées, avec des échanges possibles via une carte MicroSD ou par QR codes. L'appareil inclut une batterie amovible de 1200 mAh.

Pour ce qui est de la connectivité, le Passport est équipé d'un port MicroSD, d'un port USB-C pour le chargement, et d'une caméra arrière pour scanner les QR codes.

Sur le plan de la sécurité, le Passport intègre un élément sécurisé et le code source de l'appareil est entièrement open-source. Il offre toutes les fonctionnalités attendues sur un bon hardware wallet Bitcoin. À noter, le Passport ne prend pas encore en charge miniscript, mais cette fonctionnalité est prévue pour le deuxième trimestre de 2025.

Proposé à $199, le Passport se positionne comme un hardware wallet haut de gamme, en concurrence avec le Coldcard Q, le Jade Plus, le Tezor Safe 5, ainsi que les modèles haut de gamme de Ledger.

![Image](assets/fr/01.webp)

Pour gérer votre portefeuille sécurisé sur un Passport, vous disposez de plusieurs options. Ce hardware wallet est compatible avec la majorité des logiciels de gestion de portefeuille sur le marché, y compris Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, entre autres. 

Dans ce tutoriel, qui s'adresse aux utilisateurs débutants et intermédiaires, nous allons découvrir comment utiliser l'application Envoy avec votre Passport. C'est la méthode la plus simple pour exploiter les fonctionnalités de votre hardware wallet.

Si vous êtes un utilisateur avancé et souhaitez explorer des fonctionnalités plus complexes, je vous recommande de consulter cet autre tutoriel où nous configurons le Passport avec Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Unboxing du Passport

Lorsque vous recevez votre Passport, assurez-vous que la boîte et le sceau sur le carton sont intacts pour confirmer que le paquet n'a pas été ouvert. Une vérification logicielle de l'authenticité et de l'intégrité du dispositif sera également réalisée lors de sa configuration.

![Image](assets/fr/02.webp)

Le contenu de la boîte inclut :
- Le Passport ;
- Un papier cartonné pour noter votre phrase mnémonique ;
- Un câble USB-C pour le chargement ;
- Une carte MicroSD ;
- Deux adaptateurs MicroSD vers port Lightning ou USB-C ;
- Des autocollants.

Sur l'appareil, vous trouverez :
- Un clavier (1) ;
- Un port USB-C (2) ;
- Un bouton de suppression (3) ;
- Un bouton de retour (4) ;
- Un bouton de confirmation (5) ;
- Un pavé directionnel (6) ;
- Un bouton on/off (7) ;
- Un indicateur de statut (8) ;
- Un port MicroSD (9) ;
- Un bouton pour changer de mode aA1 (10) ;
- Une caméra arrière.

![Image](assets/fr/03.webp)


## Téléchargement de l'application Envoy

Rendez-vous sur votre store d'applications pour télécharger Envoy :
- Sur le [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy) ;
- Sur l'[App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818) ;
- Sur [F-Droid](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Vous pouvez aussi télécharger le fichier APK directement [depuis le dépôt GitHub de Foundation](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Une fois l'application ouverte, sélectionnez "*Manage Passport*".

![Image](assets/fr/52.webp)

Choisissez si vous souhaitez activer la connexion via Tor pour renforcer la confidentialité, puis appuyez sur "*Continue*".

![Image](assets/fr/53.webp)

Choisissez "*Connect an existing Passport*" si votre Passport est déjà configuré, ou "*Set up a new Passport*" si vous initialisez votre hardware wallet pour la première fois.

![Image](assets/fr/54.webp)

Acceptez les conditions d'utilisation.

![Image](assets/fr/55.webp)

Vous serez ensuite invité à vérifier l'authenticité du Passport. Cliquez sur "*Next*".

![Image](assets/fr/56.webp)

## Démarrage du Passport

Appuyez sur le bouton on/off situé sur le côté de l'appareil pour le démarrer.

![Image](assets/fr/04.webp)

Accédez au menu suivant en appuyant sur le bouton de confirmation.

![Image](assets/fr/05.webp)

Dans ce tutoriel, nous utilisons Envoy pour gérer le portefeuille sécurisé par le Passport. Sélectionnez donc "*Envoy App*".

![Image](assets/fr/57.webp)

Cliquez sur "*Continue on Envoy*".

![Image](assets/fr/58.webp)

L'étape suivante est la vérification de votre appareil. Cette vérification confirme l'authenticité de votre Passport et assure qu'il n'a pas été altéré durant le transport. Vous serez invité à scanner un QR code.

![Image](assets/fr/08.webp)

Scannez les QR codes dynamiques affichés dans l'application avec votre Passport. Une fois la numérisation terminée, cliquez sur "*Next*".

![Image](assets/fr/59.webp)

Utilisez ensuite votre téléphone pour scanner le QR code qui s'affiche sur votre Passport.

![Image](assets/fr/60.webp)

Si le message "*Your Passport is secure*" apparaît, cela confirme que votre hardware wallet est authentique. Vous pouvez désormais l'utiliser pour sécuriser un portefeuille Bitcoin.

![Image](assets/fr/61.webp)

Confirmez le résultat du test sur votre Passport.

![Image](assets/fr/14.webp)

## Mise en place du code PIN

Vient ensuite l'étape du code PIN. Le code PIN permet de déverrouiller votre Passport. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 ou 24 mots vous permettra de retrouver l'accès à vos bitcoins.

![Image](assets/fr/15.webp)

Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Passport (par exemple, dans un gestionnaire de mot de passe).

Vous pouvez choisir un code PIN entre 6 et 12 chiffres. Je vous conseille de le faire le plus long possible.

Utilisez le clavier pour noter les numéros de votre code PIN. Une fois terminé, cliquez sur le bouton de confirmation.

![Image](assets/fr/16.webp)

Confirmez votre PIN une seconde fois.

![Image](assets/fr/17.webp)

Votre code PIN a bien été enregistré.

![Image](assets/fr/18.webp)

## Mettre à jour le firmware du Passport

Votre hardware wallet vous propose de mettre à jour son micrologiciel. Je vous recommande de procéder à cette mise à jour immédiatement afin de bénéficier des améliorations et des corrections apportées par les dernières versions. Pour continuer, cliquez sur le bouton de confirmation à droite.

![Image](assets/fr/19.webp)

Votre Passport est prêt à recevoir le nouveau firmware via une carte MicroSD.

![Image](assets/fr/20.webp)

### Sans l'application Envoy

Pour cela, utilisez la carte MicroSD incluse dans la boîte de votre Passport (ou une autre), et insérez-la dans votre ordinateur. Téléchargez la dernière version du firmware depuis [le site de documentation de Foundation](https://docs.foundation.xyz/firmware-updates/passport/) ou [leur dépôt GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Avant de l'installer sur votre appareil, il est vivement conseillé de vérifier l'authenticité et l'intégrité du firmware téléchargé. Si vous avez besoin d'aide pour le faire, consultez ce tutoriel : 

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Avec l'application Envoy

L'autre option, qui est la plus simple, consiste à utiliser directement l'application Envoy. Cliquez sur "*Download Firmware*".

![Image](assets/fr/62.webp)

Utilisez l'adaptateur fourni avec votre Passport pour connecter la carte MicroSD à votre téléphone.

![Image](assets/fr/63.webp)

Sélectionnez la carte MicroSD dans votre explorateur de fichiers pour y sauvegarder le firmware.

![Image](assets/fr/64.webp)

Le firmware est désormais enregistré. Retirez la MicroSD de votre smartphone et insérez-la dans le Passport.

![Image](assets/fr/65.webp)

L'explorateur de fichiers du Passport s'ouvrira. Sélectionnez le fichier `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Cliquez sur "*Select*".

![Image](assets/fr/23.webp)

Confirmez ensuite l'installation du firmware.

![Image](assets/fr/24.webp)

Patientez pendant la mise à jour.

![Image](assets/fr/25.webp)

Une fois la mise à jour terminée, saisissez votre code PIN pour déverrouiller l'appareil et poursuivre la configuration.

![Image](assets/fr/26.webp)

## Créer un nouveau portefeuille Bitcoin

Il est maintenant temps de créer un nouveau portefeuille Bitcoin. Cliquez sur le bouton de confirmation.

![Image](assets/fr/27.webp)

Pour créer un nouveau portefeuille, cliquez sur "*Create New Seed*".

![Image](assets/fr/28.webp)

Vous pouvez choisir entre une phrase mnémonique de 12 ou 24 mots. La sécurité offerte par les deux options est similaire, donc vous pouvez opter pour celle qui est la plus simple à sauvegarder, soit 12 mots.

![Image](assets/fr/29.webp)

Cliquez sur "*Continue*".

![Image](assets/fr/30.webp)

Votre Passport va maintenant générer votre "*Backup Code*". Il s'agit d'une série de chiffres permettant de déchiffrer une sauvegarde de votre portefeuille enregistrée sur une MicroSD. Ce système de backup, propre aux appareils de Foundation, constitue une sauvegarde additionnelle à votre phrase mnémonique mais n'est pas compatible avec d'autres logiciels Bitcoin.

Si vous décidez d'utiliser ce "*Backup Code*", assurez-vous de le conserver dans un lieu différent de celui de votre MicroSD contenant la sauvegarde chiffrée de votre portefeuille. Vous pouvez cependant choisir de ne pas utiliser ce système si vous estimez qu'une bonne sauvegarde de votre phrase mnémonique est suffisante.

![Image](assets/fr/31.webp)

Saisissez votre "*Backup Code*" pour confirmer que vous l'avez correctement sauvegardé.

![Image](assets/fr/32.webp)

Si une MicroSD a été insérée, la sauvegarde chiffrée de votre portefeuille y a bien été enregistrée.

![Image](assets/fr/33.webp)

Votre Passport va vous afficher votre phrase mnémonique de 12 mots. Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Passport.

La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre Passport. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Cliquez sur le bouton de confirmation pour voir votre phrase mnémonique.

![Image](assets/fr/34.webp)

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.**_

Réalisez la sauvegarde physique de cette phrase.

![Image](assets/fr/35.webp)

La configuration de votre Passport a bien été réalisée. Cliquez sur le bouton de confirmation pour continuer.

![Image](assets/fr/36.webp)

## Configurer le portefeuille sur Envoy

Dans ce tutoriel, je vous présente l'utilisation du Passport avec l'application Envoy. Cependant, ce hardware wallet est également compatible avec Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter, et bien d'autres...

![Image](assets/fr/66.webp)

Utilisez l'application Envoy pour scanner le QR code affiché sur votre Passport.

![Image](assets/fr/67.webp)

Vos clés publiques sont maintenant importées dans l'application. Cliquez sur "*Validate receive address*".

![Image](assets/fr/68.webp)

Utilisez votre Passport pour scanner l'adresse affichée sur Envoy.

![Image](assets/fr/69.webp)

Votre Passport confirmera si le portefeuille importé sur Envoy est valide. Confirmez-le dans l'application.

![Image](assets/fr/70.webp)

Vous pouvez désormais accéder aux informations publiques de votre portefeuille sur Envoy, mais pour dépenser des bitcoins, vous devrez utiliser votre Passport.

![Image](assets/fr/71.webp)

## Découverte des menus du Passport

L'interface de votre Passport comprend trois menus principaux :
- "*Account*" ;
- "*More*" ;
- "*Settings*".

Pour naviguer entre ces menus, utilisez les flèches gauche et droite du pavé directionnel.

### Menu "*Account*"

Dans le menu "*Account*", vous trouverez les principales fonctionnalités de votre portefeuille Bitcoin. Vous avez la possibilité de signer une transaction soit via la caméra, soit via le port MicroSD.

![Image](assets/fr/37.webp)

Le sous-menu "*Account Tools*" offre des options telles que la vérification d'une adresse, la signature d'un message, ou la consultation des adresses de votre portefeuille.

![Image](assets/fr/38.webp)

Dans le sous-menu "*Manage Account*", vous avez la possibilité de connecter votre portefeuille Bitcoin à un logiciel gestionnaire de wallet (ce que nous aborderons dans les prochaines étapes de ce tutoriel), ou de consulter et de renommer votre compte.

![Image](assets/fr/39.webp)

### Menu "*More*"

Dans le menu "*More*", vous avez la possibilité de créer un nouveau compte dans votre portefeuille, qui sera lié à la même phrase mnémonique.

![Image](assets/fr/40.webp)

Vous pouvez aussi saisir une passphrase BIP39 ou utiliser une seed temporaire.

![Image](assets/fr/41.webp)

### Menu "*Settings*"

Dans le menu "*Settings*", vous retrouvez tous les paramètres relatifs à votre portefeuille et à votre appareil.

![Image](assets/fr/42.webp)

Le sous-menu "*Device*" vous offre des options pour personnaliser la luminosité de l'écran, régler le délai avant verrouillage automatique, changer le code PIN, ou renommer l'appareil.

![Image](assets/fr/43.webp)

Le sous-menu "*Backup*" permet d'exporter la sauvegarde chiffrée de votre portefeuille, de vérifier la validité d'une sauvegarde existante, ou de consulter de nouveau votre "*Backup Code*".

![Image](assets/fr/44.webp)

Le sous-menu "*Firmware*" est destiné à la mise à jour du micrologiciel de votre Passport. Il est recommandé de réaliser ces mises à jour régulièrement pour bénéficier des dernières corrections et fonctionnalités.

![Image](assets/fr/45.webp)

Le sous-menu "*Bitcoin*" vous permet de modifier l'unité affichée (BTC ou satoshis), de gérer un éventuel portefeuille Multisig, ou de passer en mode "*Testnet*".

![Image](assets/fr/46.webp)

Dans "*Advanced*", vous avez la possibilité de consulter les mots de votre phrase mnémonique, de réaliser des actions sur la MicroSD insérée, de réinitialiser votre Passport aux paramètres d'usine, ou de procéder à une vérification d'authenticité, comme effectué précédemment.

![Image](assets/fr/47.webp)

Vous pouvez activer les "*Security Words*", une fonctionnalité qui ajoute une couche de sécurité en affichant deux mots spécifiques lors du déverrouillage de l'appareil après saisie des quatre premiers chiffres du code PIN. Ces mots, à sauvegarder lors de leur configuration, permettent de s'assurer que le Passport n'a pas été remplacé ou altéré. En cas de différence lors d'une utilisation ultérieure, il est conseillé de ne pas utiliser l'appareil. Je vous conseille d'activer cette option pour prévenir la plupart des risques de compromission physique de l'appareil.

![Image](assets/fr/48.webp)

Enfin, le sous-menu "*Extensions*" permet d'activer des fonctionnalités spécifiques à certaines utilisations de l'appareil, telles que le protocole de coinjoins Whirlpool.

![Image](assets/fr/49.webp)

## Recevoir des bitcoins

Maintenant que votre Passport est configuré, vous êtes prêt à recevoir vos premiers sats sur votre nouveau portefeuille Bitcoin. Pour ce faire, sur Envoy, cliquez sur votre compte "*Primary 0*".

![Image](assets/fr/72.webp)

Cliquez sur le bouton "*Receive*".

![Image](assets/fr/73.webp)

Votre application Envoy vous affiche la première adresse vierge disponible sur votre portefeuille. Avant de l'utiliser, nous allons vérifier l'adresse sur l'écran du Passport pour nous assurer qu'elle appartient bien à notre portefeuille Bitcoin. Dans le menu "*Account*" de votre Passport, sélectionnez "*Account Tools*".

![Image](assets/fr/74.webp)

Cliquez sur "*Verify Address*", puis scannez le QR code affiché sur Envoy.

![Image](assets/fr/75.webp)

Assurez-vous que l'adresse affichée sur le Passport corresponde exactement à celle indiquée sur Sparrow et que la mention "*Verified*" apparaisse.

![Image](assets/fr/76.webp)

Vous pouvez désormais l'utiliser pour recevoir des bitcoins. Lorsque la transaction sera diffusée sur le réseau, elle apparaîtra sur Envoy. Attendez d'obtenir suffisamment de confirmations pour considérer la transaction comme définitive.

![Image](assets/fr/77.webp)

## Envoyer des bitcoins

Maintenant que vous avez quelques sats dans votre portefeuille, vous pouvez également en envoyer. Pour ce faire, cliquez sur le bouton "*Send*".

![Image](assets/fr/78.webp)

Saisissez l'adresse de réception du destinataire, soit en la collant directement, soit en scannant le QR code avec la caméra de votre smartphone.

![Image](assets/fr/79.webp)

Déterminez le montant que vous souhaitez envoyer, puis cliquez sur "*Confirm*".

![Image](assets/fr/80.webp)

Sélectionnez les frais de transaction en fonction de la situation actuelle du marché, puis vérifiez les informations de la transaction. Si tout est correct, cliquez sur "*Sign with Passport*".

![Image](assets/fr/81.webp)

Ajoutez une étiquette à votre transaction pour en garder une trace claire de son objectif.

![Image](assets/fr/82.webp)

Envoy vous affiche ensuite une PSBT (*Partially Signed Bitcoin Transaction*). L'application a construit la transaction, mais il manque encore la ou les signatures pour déverrouiller les bitcoins utilisés en input. Ces signatures ne peuvent être réalisées que par le Passport, qui héberge votre seed donnant accès aux clés privées nécessaires pour signer la transaction.

![Image](assets/fr/83.webp)

Sur votre Passport, accédez au menu "*Account*" et cliquez sur "*Sign with QR Code*".

![Image](assets/fr/84.webp)

Scannez la PSBT (*Partially Signed Bitcoin Transaction*) affichée sur Envoy.

![Image](assets/fr/85.webp)

Confirmez que l'adresse de réception et le montant envoyé sont corrects, puis appuyez sur le bouton de confirmation.

![Image](assets/fr/86.webp)

Vérifiez l'adresse de change. Dans mon exemple, il n'y en a pas, car la transaction comprend un seul output.

![Image](assets/fr/87.webp)

Assurez-vous que le montant des frais est celui que vous avez choisi.

![Image](assets/fr/88.webp)

Si toutes les informations sont bien justes, cliquez sur le bouton de confirmation pour signer la transaction.

![Image](assets/fr/89.webp)

Votre Passport vous montre donne votre transaction signée sous forme de QR code.

![Image](assets/fr/90.webp)

Sur l'application Envoy, cliquez sur l'icône de QR code, puis scannez la PSBT affichée sur l'écran de votre Passport.

![Image](assets/fr/91.webp)

Vérifiez une dernière fois les détails de votre transaction. Si tout est correct, appuyez sur "*Send Transaction*" pour la diffuser sur le réseau Bitcoin.

![Image](assets/fr/92.webp)

Votre transaction est maintenant en attente de confirmation. Vous pouvez suivre son statut directement depuis votre compte.

![Image](assets/fr/93.webp)

Félicitations, vous savez dorénavant comment configurer et utiliser le Passport avec l'application Envoy. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, vous pouvez également consulter notre tutoriel sur le logiciel Liana :

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
