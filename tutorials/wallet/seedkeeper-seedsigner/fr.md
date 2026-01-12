---
name: Seedkeeper x SeedSigner
description: Comment utiliser un Seedkeeper avec son SeedSigner ?
---

![cover](assets/cover.webp)

*Merci aux équipes de [Satochip](https://satochip.io/) d’avoir accepté la réutilisation [de leurs vidéos](https://www.youtube.com/@satochip/videos) dans ce tutoriel. Merci également à [Crypto Guide](https://www.youtube.com/@CryptoGuide/) pour son fork du firmware SeedSigner permettant la prise en charge des smartcards.*

---

Le SeedSigner est un hardware wallet que l’on assemble soi-même à partir de matériel informatique standard, le plus souvent autour d’un Raspberry Pi Zero. Ce portefeuille est dit "*stateless*" : contrairement à la plupart des autres modèles du marché (Coldcard, Trezor, Ledger, etc.), il ne conserve aucune donnée en mémoire permanente et fonctionne uniquement en live à partir de la mémoire vive. Ainsi, la seed de votre portefeuille n’est jamais enregistrée sur le SeedSigner. À chaque redémarrage, il est donc nécessaire de la renseigner pour permettre au dispositif de signer vos transactions. La méthode la plus courante consiste à sauvegarder votre seed sous la forme d’un QR code, que vous scannez ensuite à chaque utilisation (*SeedQR*).

Cette approche présente toutefois un risque important : la seed doit rester accessible en clair afin de pouvoir être scannée. En cas de vol ou d’intrusion, un attaquant pourrait donc facilement s’en emparer et dérober vos bitcoins.

Pour pallier cette faiblesse, il est possible d’associer le SeedSigner au [**Seedkeeper**](https://satochip.io/product/seedkeeper/), une carte à puce développée par Satochip. Celle-ci permet de stocker des phrases mnémoniques (ou d’autres secrets) dans un élément sécurisé protégé par un code PIN. L’applet du Seedkeeper est open-source et son élément sécurisé bénéficie d’une certification EAL6+. Utilisé conjointement avec le SeedSigner, il offre un dispositif de sécurité très intéressant : vos clés restent gérées entièrement hors ligne, vous signez vos transactions sur un écran de confiance, et la seed est protégée physiquement dans une smartcard résistante aux attaques physique.

Pour réaliser cette installation, vous aurez simplement besoin des éléments suivants :  
- Le matériel habituel nécessaire à un SeedSigner classique : un Raspberry Pi Zero, un écran Waveshare 1.3", une caméra compatible et une carte microSD (vous trouverez davantage de détails dans le tutoriel consacré au SeedSigner ci-dessous) ;
- Le kit d’extension pour SeedSigner, disponible [sur la boutique officielle de Satochip](https://satochip.io/product/seedsigner-extension-kit/), qui permet de lire et d’écrire sur la smartcard directement depuis votre SeedSigner. Une autre option consiste à utiliser un lecteur de carte à puce externe, pouvant être connecté par câble à un port Micro-USB du Raspberry Pi. Toutefois, je n'ai pas testé cette solution de mon côté ;
- Un Seedkeeper, ou à défaut une smartcard vierge sur laquelle vous installerez l’applet du Seedkeeper (le kit d’extension vendu par Satochip inclut déjà une smartcard vierge).

![Image](assets/fr/01.webp)

Ce tutoriel couvre deux cas de figure :
- Si vous disposez déjà d’un portefeuille Bitcoin géré via votre SeedSigner, il vous suffira d’installer le nouveau firmware. Vous pourrez alors continuer à utiliser votre portefeuille existant, cette fois en utilisant le Seedkeeper pour renforcer la sécurité.  
- Si vous n’avez pas encore de portefeuille Bitcoin associé à votre SeedSigner, il faudra suivre les étapes **5** et **6** du tutoriel mentionné ci-dessous. Ces sections expliquent comment générer une phrase mnémonique avec le SeedSigner, la sauvegarder via un *SeedQR*, puis connecter ce portefeuille à Sparrow Wallet pour le gérer. Je n’aborderai pas ces procédures ici et **je pars du principe que vous possédez déjà un portefeuille Bitcoin fonctionnel, configuré avec Sparrow et votre SeedSigner**.

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Installer le firmware

Pour utiliser votre SeedSigner avec un Seedkeeper, il est nécessaire d’installer un firmware alternatif, différent de celui du SeedSigner original, afin d’avoir la prise en charge de la lecture des cartes à puce. Pour cela, [je vous recommande d’utiliser le fork de "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Téléchargez [la dernière version de l’image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) correspondant au modèle de Raspberry Pi que vous utilisez.

![Image](assets/fr/02.webp)

Si vous ne l'avez pas encore, téléchargez le logiciel [Balena Etcher](https://etcher.balena.io/), puis procédez comme suit :
- Insérez la carte microSD dans votre ordinateur ;
- Lancez Etcher ;
- Sélectionnez le fichier `.zip` que vous venez de télécharger ;
- Choisissez la carte microSD comme cible ;
- Cliquez sur `Flash!`.

![Image](assets/fr/03.webp)

Patientez jusqu’à la fin du processus : votre microSD est désormais prête à l’emploi. Vous pouvez à présent passer à l’assemblage de votre appareil.

Pour plus de détails concernant l’installation du firmware et la vérification du logiciel (étape que je vous recommande vivement de faire), consultez le tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Assembler le lecteur de smartcard

![video](https://youtu.be/jqE8HDMCImA)

Commencez par installer la caméra sur le Raspberry Pi Zero en l’insérant délicatement dans la broche prévue à cet effet, puis verrouillez-la avec la languette noire. Placez ensuite le Pi au fond du boîtier en veillant à bien aligner les ports avec les ouvertures correspondantes.

![Image](assets/fr/04.webp)

Fixez ensuite le lecteur de carte à puce sur les broches GPIO du Raspberry Pi Zero.

![Image](assets/fr/05.webp)

Glissez le cache en plastique sur le lecteur de carte à puce jusqu’à ce qu’il soit correctement positionné.

![Image](assets/fr/06.webp)

Ajoutez ensuite l’écran sur les broches GPIO de l’extension.

![Image](assets/fr/07.webp)

Insérez enfin la carte microSD contenant le firmware dans le port latéral du Raspberry Pi Zero.

![Image](assets/fr/08.webp)

Vous pouvez désormais brancher votre SeedSigner soit via le port Micro-USB du Raspberry Pi Zero, soit via le port USB-C de l’extension. Les deux options fonctionnent. Attendez quelques secondes le temps du démarrage, puis vous devriez voir apparaître l’écran d’accueil.

![Image](assets/fr/09.webp)

Pour plus de détails sur le paramétrage initial de votre SeedSigner, je vous recommande de consulter le tutoriel suivant :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flasher une smartcard avec l’applet Seedkeeper (optionnel)

![video](https://youtu.be/NF4HemyEcOY)

Si vous possédez déjà un Seedkeeper, vous pouvez passer cette étape et aller directement à l’étape 4. Dans cette section, nous allons voir comment installer l’applet du Seedkeeper sur une smartcard vierge (méthode DIY).

Pour commencer, ouvrez le menu `Tools > Smartcard Tools` sur votre SeedSigner.

![Image](assets/fr/10.webp)

Sélectionnez ensuite `DIY Tools > Install Applet`.

![Image](assets/fr/11.webp)

Insérez votre smartcard dans le lecteur du SeedSigner, puce orientée vers le bas, puis choisissez l’applet `SeedKeeper`.

![Image](assets/fr/12.webp)

Patientez pendant l’installation : le processus peut durer quelques dizaines de secondes.

![Image](assets/fr/13.webp)

Une fois l’applet installée avec succès, vous pouvez passer à l’étape 4.

![Image](assets/fr/14.webp)

## 4. Sauvegarder un SeedQR existant sur le Seedkeeper

![video](https://youtu.be/X-vmFHU9Ec8)

Maintenant que votre Seedkeeper est opérationnel, vous pouvez sauvegarder la phrase mnémonique de votre portefeuille Bitcoin sur la smartcard. Pour commencer, allumez votre SeedSigner comme d'habitude, puis scannez le *SeedQR* de votre portefeuille afin de le charger dans l’appareil. Une fois la seed importée, sélectionnez simplement `Done`.

![Image](assets/fr/15.webp)

Lorsque la seed est chargée, accédez au menu `Backup Seed`.

![Image](assets/fr/16.webp)

Insérez ensuite votre Seedkeeper dans le lecteur du SeedSigner, puis choisissez l’option `To SeedKeeper`.

![Image](assets/fr/17.webp)

Le SeedSigner vous demandera alors d’entrer un code PIN pour votre Seedkeeper. Comme il s’agit d’une carte encore vierge, aucun code n’a encore été défini. Saisissez donc un code quelconque pour passer cette étape, puis validez.

![Image](assets/fr/18.webp)

Le SeedSigner détecte que le Seedkeeper n’a pas encore été initialisé (autrement dit, qu’aucun mot de passe n’est configuré). Cliquez sur `I Understand` pour poursuivre.

![Image](assets/fr/19.webp)

Choisissez à présent le nouveau code PIN de votre Seedkeeper, entre 4 et 16 caractères. Pour renforcer la sécurité, privilégiez un code long et aléatoire : c’est la seule barrière protégeant l’accès physique à votre phrase mnémonique.

Pensez à sauvegarder ce code PIN dès sa création, soit dans un gestionnaire de mots de passe fiable, soit sur un support physique séparé en fonction de votre stratégie. Dans ce dernier cas, veillez à ne jamais conserver le support contenant le PIN au même endroit que votre Seedkeeper, sans quoi la protection deviendrait inefficace. Il est important de disposer d’une copie de secours : **sans ce code PIN, vous ne pourrez plus accéder à votre seed, et donc vos bitcoins seront perdus**.

![Image](assets/fr/20.webp)

Vous pouvez ensuite définir un `Label` associé à votre phrase mnémonique. Cette étiquette est utile si vous enregistrez plusieurs secrets sur le Seedkeeper, afin de les identifier facilement.

![Image](assets/fr/21.webp)

Votre phrase mnémonique est désormais sauvegardée sur la smartcard.

![Image](assets/fr/22.webp)

En termes de stratégie de sécurisation, plusieurs approches sont possibles selon vos besoins et votre niveau d’exposition au risque. Personnellement, je vous recommande de conserver au minimum 2 copies de votre seed :
- Une première sur la smartcard, que vous garderez facilement accessible pour vos opérations courantes, comme la vérification d’adresses ou la signature de transactions. Cette méthode est pratique (comme nous le verrons dans la partie 5) et reste sûre grâce à la protection offerte par le code PIN, ce qui permet de la conserver accessible sans risque majeur ;
- Une seconde copie de votre phrase mnémonique en clair, servant de sauvegarde ultime de votre portefeuille, à utiliser uniquement en cas de perte ou de vol du Seedkeeper. Cette version étant non chiffrée, elle doit impérativement être conservée dans un lieu distinct et plus sécurisé, afin d’éviter toute compromission simultanée des 2 backups.

Selon votre stratégie de protection et votre profil de risque, vous pouvez aussi dupliquer la seed sur plusieurs Seedkeeper différents, ou créer plusieurs copies physiques de la phrase mnémonique. Pour approfondir ces pratiques, je vous invite à consulter le tutoriel suivant :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Charger une seed depuis le Seedkeeper

![video](https://youtu.be/ms0Iq_IyaoE)

Vous pouvez désormais utiliser votre Seedkeeper pour charger votre phrase mnémonique dans le SeedSigner au démarrage, et ainsi signer vos transactions Bitcoin. Pour commencer, allumez votre SeedSigner en le branchant, puis ouvrez le menu `Seeds`.

![Image](assets/fr/23.webp)

Sélectionnez ensuite l’option `From SeedKeeper`.

![Image](assets/fr/24.webp)

Insérez votre Seedkeeper dans le lecteur de carte à puce, puis saisissez votre code PIN pour le déverrouiller. Validez votre entrée en appuyant sur le bouton de confirmation situé en bas à droite, `KEY3`.

![Image](assets/fr/25.webp)

Le Seedkeeper peut contenir plusieurs secrets, donc le SeedSigner vous invite ensuite à choisir celui que vous souhaitez charger. L’étiquette affichée correspond au nom que vous aviez défini à l’étape 4. Si, comme dans mon cas, vous n’avez enregistré qu’une seule seed, une seule option sera disponible.

![Image](assets/fr/26.webp)

Votre seed est désormais chargée. Vérifiez qu’il s’agit bien du bon portefeuille en comparant l’empreinte affichée à l’écran avec celle indiquée dans les paramètres de votre Sparrow Wallet. Cette empreinte vous avait également été fournie lors de la création initiale du portefeuille.

Si vous utilisez une passphrase, vous pouvez l’appliquer à cette étape (voir la partie 6 de ce tutoriel). Dans le cas contraire, cliquez simplement sur `Done`.

![Image](assets/fr/27.webp)

Vous pouvez ensuite utiliser votre portefeuille normalement : vérifier vos adresses de réception et signer des transactions, comme avec un SeedSigner classique. Pour en savoir plus sur son utilisation, reportez-vous au tutoriel dédié :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Utiliser le Seedkeeper avec une passphrase BIP39

Vous utilisez une passphrase pour protéger votre portefeuille Bitcoin ? Sachez qu’il est également possible de l’enregistrer dans votre Seedkeeper, aux côtés de votre seed. Cette solution vous permettra de charger rapidement votre portefeuille sur le SeedSigner, sans avoir à saisir manuellement la passphrase sur le petit clavier à chaque utilisation.

Cette méthode me semble particulièrement intéressante, car elle vous fait bénéficier des avantages de sécurité apportés par la passphrase, tout en supprimant les contraintes liées à son usage au quotidien. Voici, à titre d’exemple, une configuration que je vous recommande :  
- Conservez dans un Seedkeeper votre seed et votre passphrase, protégées par un code PIN fort (c’est important). Cette sauvegarde vous permettra d’utiliser facilement votre portefeuille au quotidien. Vous pouvez, si vous le souhaitez, dupliquer ces informations sur un second Seedkeeper ;
- Conservez également une copie en clair de votre phrase mnémonique et de votre passphrase, sur papier ou sur métal. C'est votre backup de dernier recourt en cas de perte du Seedkeeper ou de son PIN. Veillez toutefois à stocker ces copies dans des lieux distincts, afin qu’elles ne puissent pas être compromises simultanément.

Dans cette configuration, si une personne met la main sur votre phrase mnémonique en clair seule, elle ne pourra rien voler sans connaître la passphrase (à condition, bien sûr, que celle-ci soit suffisamment solide pour résister à une attaque par brute force). Inversement, si quelqu’un découvre votre passphrase en clair, elle restera inutilisable sans la phrase mnémonique correspondante.

Enfin, si une personne parvient à accéder physiquement à votre Seedkeeper contenant la seed et la passphrase, elle ne pourra rien en extraire sans connaître le code PIN. Contrairement à une passphrase, ce dernier ne peut pas être bruteforcé, car la smartcard se bloque automatiquement après 5 tentatives invalides.

La sécurité de cette configuration repose donc sur 2 points essentiels :  
- Une **passphrase forte** : elle doit être longue, aléatoire et comporter une grande variété de caractères. Sa complexité n’est pas un problème pour vous, puisque vous ne l’entrerez qu’une seule fois au clavier lors de l’initialisation ; par la suite, elle sera transmise par le Seedkeeper ;  
- Un **code PIN fort** pour le Seedkeeper : lui aussi aléatoire et composé de 16 caractères.

Pour mettre en place ce setup, commencez par charger votre passphrase dans le SeedSigner de manière classique. Vous pouvez suivre la procédure détaillée dans ce tutoriel :  

https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe  

Une fois votre portefeuille avec passphrase correctement chargé sur le SeedSigner, ouvrez le menu `Seeds` et sélectionnez l’empreinte correspondant à ce portefeuille. Notez que cette empreinte diffère de celle du portefeuille sans passphrase.

![Image](assets/fr/28.webp)

Cliquez ensuite sur `Backup Seed`, insérez le Seedkeeper dans le lecteur, puis sélectionnez `To SeedKeeper`.

![Image](assets/fr/29.webp)

Entrez votre code PIN pour déverrouiller le Seedkeeper, puis attribuez un label à ce secret. Vous pouvez laisser l’empreinte comme label afin de conserver une certaine forme de déni plausible, ou bien indiquer explicitement `Passphrase Wallet`, par exemple.

![Image](assets/fr/30.webp)

Votre portefeuille avec passphrase est désormais enregistré sur le Seedkeeper.

![Image](assets/fr/31.webp)

Lors d’un prochain démarrage, il vous suffira d’insérer votre Seedkeeper dans le lecteur, puis de naviguer dans `Seeds > From SeedKeeper`.

![Image](assets/fr/32.webp)

Saisissez votre code PIN pour déverrouiller la smartcard, puis sélectionnez le portefeuille correspondant à votre passphrase.

![Image](assets/fr/33.webp)

Vérifiez la passphrase et l’empreinte de votre portefeuille, puis validez.

![Image](assets/fr/34.webp)

Vous pouvez à présent accéder à votre portefeuille avec passphrase et signer vos transactions comme on le fait normalement sur un SeedSigner.

## 7. Options supplémentaires

Dans le menu `Tools > Smartcard Tools`, vous trouverez plusieurs options permettant de gérer votre Seedkeeper :

- Dans le menu `Common Tools`, on peut :
	- Vérifier l’authenticité de la carte ;
	- Modifier le code PIN ;
	- Changer les labels associés à vos secrets ;
	- Désactiver la fonction NFC (recommandé si vous utilisez uniquement le lecteur de puce) ;
	- Effectuer un factory reset.

- Dans le menu `SeedKeeper Functions`, on peut :
	- Consulter la liste des secrets enregistrés ;
	- Sauvegarder un nouveau secret ;
	- Supprimer un secret existant ;
	- Sauvegarder ou charger vos descriptors (fonction utile pour les portefeuilles multisig).

- Dans le menu `DIY Tools`, on peut :
	- Compiler l’applet du Seedkeeper ;
	- Installer l'applet sur une carte vierge ;
	- Supprimer l’applet d’un Seedkeeper pour le réinitialiser et le rendre vierge à nouveau.

Vous savez désormais comment utiliser le Seedkeeper pour sauvegarder votre portefeuille de manière sécurisée en combinaison avec le SeedSigner.

Si ce setup vous a convaincu, n’hésitez pas à soutenir les projets qui le rendent possible :  
- En achetant votre matériel directement [sur le site de Satochip](https://satochip.io/shop/) ;
- En effectuant [un don au projet SeedSigner](https://seedsigner.com/donate/) ;
- En vous abonnant à [la chaîne YouTube de Crypto Guide](https://www.youtube.com/@CryptoGuide/), tenue par la personne qui maintient le dépôt GitHub hébergeant le firmware modifié.



