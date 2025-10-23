---
name: Seedkeeper x SeedSigner
description: Comment utiliser un Seedkeeper avec son SeedSigner ?
---

![cover](assets/cover.webp)

*Merci aux équipes de [Satochip](https://satochip.io/) d’avoir accepté la réutilisation [de leurs vidéos](https://www.youtube.com/@satochip/videos) dans ce tutoriel.*

---

Le SeedSigner est un hardware wallet que l’on assemble soi-même à partir de matériel informatique standard, le plus souvent autour d’un Raspberry Pi Zero. Ce portefeuille est dit "stateless" : contrairement à la plupart des autres modèles du marché (Coldcard, Trezor, Ledger, etc.), il ne conserve aucune donnée en mémoire permanente et fonctionne uniquement en live à partir de la mémoire vive. Ainsi, la seed de votre portefeuille n’est jamais enregistrée sur le SeedSigner. À chaque redémarrage, il est donc nécessaire de la renseigner pour permettre au dispositif de signer vos transactions. La méthode la plus courante consiste à sauvegarder votre seed sous la forme d’un QR code, que vous scannez ensuite à chaque utilisation (*SeedQR*).

Cette approche présente toutefois un risque important : la seed doit rester accessible en clair afin de pouvoir être scannée. En cas de vol ou d’intrusion, un attaquant pourrait donc facilement s’en emparer et dérober vos bitcoins.

Pour pallier cette faiblesse, il est possible d’associer le SeedSigner au [**Seedkeeper**](https://satochip.io/product/seedkeeper/), une carte à puce développée par Satochip. Celle-ci permet de stocker des phrases mnémoniques (ou d’autres secrets) dans un élément sécurisé protégé par un code PIN. L’applet du Seedkeeper est open-source et son élément sécurisé bénéficie d’une certification EAL6. Utilisé conjointement avec le SeedSigner, il offre un dispositif de sécurité très intéressant : vos clés restent gérées entièrement hors ligne, vous signez vos transactions sur un écran de confiance, et la seed est protégée physiquement dans une smartcard résistante aux attaques physique.

Pour réaliser cette installation, vous aurez simplement besoin des éléments suivants :  
- Le matériel habituel nécessaire à un SeedSigner classique : un Raspberry Pi Zero, un écran Waveshare 1.3", une caméra compatible et une carte microSD (vous trouverez davantage de détails dans le tutoriel consacré au SeedSigner ci-dessous) ;  
- Le kit d’extension pour SeedSigner, disponible [sur la boutique officielle de Satochip](https://satochip.io/product/seedsigner-extension-kit/), qui permet de lire et d’écrire sur la smartcard directement depuis votre SeedSigner ;  
- Un Seedkeeper, ou à défaut une smartcard vierge sur laquelle vous installerez l’applet du Seedkeeper (le kit d’extension vendu par Satochip inclut déjà une smartcard vierge).  

00

Ce tutoriel couvre deux cas de figure :
- Si vous disposez déjà d’un portefeuille Bitcoin géré via votre SeedSigner, il vous suffira d’installer le nouveau firmware. Vous pourrez alors continuer à utiliser votre portefeuille existant, cette fois en utilisant le Seedkeeper pour renforcer la sécurité.  
- Si vous n’avez pas encore de portefeuille Bitcoin associé à votre SeedSigner, il faudra suivre les étapes **5** et **6** du tutoriel mentionné ci-dessous. Ces sections expliquent comment générer une phrase mnémonique avec le SeedSigner, la sauvegarder via un *SeedQR*, puis connecter ce portefeuille à Sparrow Wallet pour le gérer. Je n’aborderai pas ces procédures ici et **je pars du principe que vous possédez déjà un portefeuille Bitcoin fonctionnel, configuré avec Sparrow et votre SeedSigner**.

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Installer le firmware

Pour utiliser votre SeedSigner avec un Seedkeeper, il est nécessaire d’installer un firmware alternatif, différent de celui du SeedSigner original, afin d’avoir la prise en charge de la lecture des cartes à puce. Pour cela, [je vous recommande d’utiliser le fork de "3rdIteration"](https://github.com/3rdIteration/seedsigner). Téléchargez [la dernière version de l’image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondant au modèle de Raspberry Pi que vous utilisez.

01

Si vous ne l'avez pas encore, téléchargez le logiciel [Balena Etcher](https://etcher.balena.io/), puis procédez comme suit :
- Insérez la carte microSD dans votre ordinateur ;
- Lancez Etcher ;
- Sélectionnez le fichier `.zip` que vous venez de télécharger ;
- Choisissez la carte microSD comme cible ;
- Cliquez sur `Flash!`.

02

Patientez jusqu’à la fin du processus : votre microSD est désormais prête à l’emploi. Vous pouvez à présent passer à l’assemblage de votre appareil.

Pour plus de détails concernant l’installation du firmware et la vérification du logiciel (étape que je vous recommande vivement de faire), consultez le tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Assembler le lecteur de smartcard

![video](https://youtu.be/jqE8HDMCImA)

Commencez par installer la caméra sur le Raspberry Pi Zero en l’insérant délicatement dans la broche prévue à cet effet, puis verrouillez-la avec la languette noire. Placez ensuite le Pi au fond du boîtier en veillant à bien aligner les ports avec les ouvertures correspondantes.

03

Fixez ensuite le lecteur de carte à puce sur les broches GPIO du Raspberry Pi Zero.

04

Glissez le cache en plastique sur le lecteur de carte à puce jusqu’à ce qu’il soit correctement positionné.

05

Ajoutez ensuite l’écran sur les broches GPIO de l’extension.

06

Insérez enfin la carte microSD contenant le firmware dans le port latéral du Raspberry Pi Zero.

07

Vous pouvez désormais brancher votre SeedSigner soit via le port Micro-USB du Raspberry Pi Zero, soit via le port USB-C de l’extension. Les deux options fonctionnent. Attendez quelques secondes le temps du démarrage, puis vous devriez voir apparaître l’écran d’accueil.

08

Pour plus de détails sur le paramétrage initial de votre SeedSigner, je vous recommande de consulter le tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flasher une smartcard avec l’applet Seedkeeper (optionnel)

![video](https://youtu.be/NF4HemyEcOY)

Si vous possédez déjà un Seedkeeper, vous pouvez passer cette étape et aller directement à l’étape 4. Dans cette section, nous allons voir comment installer l’applet du Seedkeeper sur une smartcard vierge (méthode DIY).

Pour commencer, ouvrez le menu `Tools > Smartcard Tools` sur votre SeedSigner.

09

Sélectionnez ensuite `DIY Tools > Install Applet`.

10

Insérez votre smartcard dans le lecteur du SeedSigner, puce orientée vers le bas, puis choisissez l’applet `SeedKeeper`.

11

Patientez pendant l’installation : le processus peut durer quelques dizaines de secondes.

12

Une fois l’applet installée avec succès, vous pouvez passer à l’étape 4.

13








## Comment sauvegarder un SeedQR existant sur le Seedkeeper ?

![video](https://youtu.be/X-vmFHU9Ec8)



## Comment charger une seed depuis le Seedkeeper ?

![video](https://youtu.be/ms0Iq_IyaoE)


## Comment supprimer une applet de la smartcard DIY ?

![video](https://youtu.be/N-i2E5VmpXA)
