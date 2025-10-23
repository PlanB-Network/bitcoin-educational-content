---
name: Seedkeeper x SeedSigner
description: Comment utiliser un Seedkeeper avec son SeedSigner ?
---

![cover](assets/cover.webp)

*Merci aux équipes de [Satochip](https://satochip.io/) d’avoir accepté la réutilisation [de leurs vidéos](https://www.youtube.com/@satochip/videos) dans ce tutoriel.*



Pour le émtairel

Le kit d’extension pour SeedSigner est disponible à l’achat [sur la boutique officielle de Satochip](https://satochip.io/product/seedsigner-extension-kit/).



Ce tutoriel s’applique à deux situations possibles selon votre cas :
- Si vous possédez déjà un portefeuille Bitcoin géré via votre SeedSigner, il vous suffira simplement d’installer le nouveau firmware. Vous pourrez alors continuer à utiliser votre portefeuille existant, cette fois avec le Seedkeeper en plus du SeedSigner.
- Si, en revanche, vous n’avez pas encore de portefeuille Bitcoin associé à votre SeedSigner, vous devrez suivre les étapes **5** et **6** de cet autre tutoriel ci-dessous. Vous y apprendrez à générer une phrase mnémonique depuis le SeedSigner, à la sauvegarder de manière classique via un SeedQR, puis à synchroniser ce portefeuille sur Sparrow Wallet afin de pouvoir le gérer facilement. Je ne reviendrai pas sur ces étapes dans le présent tutoriel, et **je pars du principe que vous disposez déjà d’un portefeuille Bitcoin géré avec Sparrow et votre SeedSigner**.

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
