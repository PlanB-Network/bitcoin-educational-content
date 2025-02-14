---
name: Passport - Foundation
description: Configurer et utiliser le hardware wallet Passport en mode manuel
---
![cover](assets/cover.webp)


Le Passport est un hardware wallet Bitcoin only conçu par Foundation Devices, une entreprise américaine fondée en avril 2020 et basée à Boston. 

Le Passport "Batch 2" que nous présentons dans ce tutoriel est le successeur du Passport "Founder's Edition". C'est un appareil imposant au design premium avec un écran en couleur haute résolution et un clavier physique ergonomique. Il foncitonne uniquement en connexion "Air-Gap", ce qui signifie que les clés de votre portefeuille sont totalement isolées, et la connexion se fait via une carte MicroSD ou par échange de QR codes. Il embarque donc une batterie amovible de 1200 mAh.

Niveau connectivité, le Passport dispose d'un port MicroSD, d'un port USB-C pour le chargement et d'une caméra à l'arrière pour scanner les QR codes.

En termes de sécurité, le Passport dispose un élément sécurisé, et le code utilisé par l'appareil est entièrement open-source. En termes de fonctionnalités, il dispose de tout ce que l'on peut attendre d'un bon hardware wallet Bitcoin. Pour le moment, le Passport ne supporte pas miniscript, mais l'implémentation est prévue pour le Q2 2025.

Le Passport est vendu $199, ce qui le positionne donc comme un hardware wallet haut de gamme, en concurrence avec le Coldcard Q, le Jade Plus, le Tezor Safe 5, ou encore les modèles haut de gamme de Ledger.

01

Pour gérer votre portefeuille sécurisé avec un Passport, vous avez du choix. Il est compatible avec la plupart des logiciels de gestion de portefeuille du marché notamment Sparrow Wallet, Specter Desktop, Nunchuk, Keeper... Dans ce tutoriel, nous allons découvrir comment l'utiliser avec Sparrow Wallet.

Vous pouvez également utiliser votre Passport avec l'application native Envoy développée par Foundation. C'est l'option la plus simple si vous êtes débutant. Pour savoir comment utiliser Envoy avec votre Passport, je vous propose de découvrir cet autre tutoriel :

LIEN ENVOY TUTO

## Unboxing du Passport

Lors de la réception de votre Passport, vérifiez que la boite et le sceau sur le carton sont en bon état afin d'être sûr que votre paquet n'a pas été ouvert. Nous ferons également une vérification de son authenticité et de son intégrité lors de la configuration.

02

Dans la boite vous trouverez :
- Le Passport ;
- Un carton pour noter votre phrase mnémonique ;
- Un câble USB-C pour le chargement ;
- Une carte MicroSD ;
- 2 adaptateurs MicroSD vers port Lightning ou port USB-C ;
- Des autocollants.

Sur l'appareil, on retrouve :
- Un clavier aA1 (1) ;
- Un port USB-C (2) ;
- Un bouton de suppression (3) ;
- Un bouton de retour (4) ;
- Un bouton de confirmation (5) ;
- Un pavé directionnel (6) ;
- Un bouton on/off (7) ;
- Un indicateur de statut (8) ;
- Un port Micro SD (9) ;
- Une caméra à l'arrière.

03

## Démarrage du Passport

Appuyez sur le bouton on/off sur le côté de l'appareil pour le démarrer.

04

Passer au menu suivant en cliquant sur le bouton de confirmation.

05

Dans ce tutoriel, nous allons utiliser Sparrow Wallet pour gérer le portefeuille sécurisé par le Passport. Vous pouvez donc cliquer sur "Manual Setup".

06

Vous devez ensuite accepter les conditions d'utilisation.

07

Puis vient l'étape de la vérification de votre appareil. Cette étape permet de vérifier que votre Passport est bien authentique et qu'il n'a subit aucune modification malicieuse durant le transport. On vous propose de scanner un QR code.

08

Rendez-vous sur [le site officiel de vérification](https://validate.foundationdevices.com/), et cliquez sur "Passport".

09

Scannez le QR code fournit par le site avec la caméra de votre Passport.

10

Votre appareil vous fournit ensuite 4 mots.

11

Notez-les sur le site web pour vérifier l'authenticité de votre Passport, puis cliquez sur le bouton "Validate".

12

Si vous voyez la mention "Passed", cela signifie que votre hardware wallet est bien authentique. Vous pouvez l'utiliser pour sécuriser un portefeuille Bitcoin.

13

Validez le résultat du test sur le Passport.

14

## Mise en place du code PIN

Vient ensuite l'étape du code PIN. Le code PIN permet de déverrouiller votre Passport. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 ou 24 mots vous permettra de retrouver l'accès à vos bitcoins.

15

Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Passport (par exemple, dans un gestionnaire de mot de passe).

Vous pouvez choisir un code PIN entre 6 et 12 chiffres. Je vous conseille de le faire le plus long possible.

Utilisez le clavier pour noter les numéros de votre code PIN. Une fois terminé, cliquez sur le bouton de confirmation.

16

Confirmez votre PIN une seconde fois.

17

Votre code PIN a bien été enregistré.

18

## Mettre à jour le firmware du Passport

Votre hardware wallet vous suggère ensuite de mettre à jour son micrologiciel. Je vous conseille de le faire immédiatement pour pouvoir bénéficier des éventuelles corrections des dernières versions. Cliquez sur le bouton de confirmation à droite pour continuer.

19

Votre Passport est près à recevoir le nouveau firmware via une carte MicroSD.

20

Pour ce faire, munissez-vous de la carte MicroSD présente dans la boite de votre Passport (ou une autre), et insérez-la dans votre ordinateur. Vous pouvez télécharger la dernière version du firmware soit sur [le site de documentation de Foundation](https://docs.foundation.xyz/firmware-updates/passport/), ou bien sur [leur dépôt GitHub](https://github.com/Foundation-Devices/passport2/releases).

21

Avant de l'installer sur votre appareil, je vous conseille fortement de vérifier l'authenticité et l'intégrité du firmware que vous venez de téléchager. Si vous ne savez pas comment le faire, vous pouvez consulter cet autre tutoriel : 

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Une fois le fichier `.bin` vérifié, placez-le sur votre MicroSD, puis insérez-la dans le Passport. L'explorateur de fichier de votre PAssport va s'ouvrir. Sélectionnez le fichier `vN.N.N-passport.bin`.

22

Cliquez sur "Select".

23

Puis, validez l'installation du firmware.

24

Patientez durant la mise à jour.

25

Une fois la mise à jour terminée, renseignez votre code PIN pour déverrouiller l'appareil et continuer la configuration.

26

## Créer un nouveau portefeuille Bitcoin

































