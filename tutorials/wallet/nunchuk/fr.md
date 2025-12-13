---
name: Nunchuk
description: Portefeuille mobile adapté à tous
---
![cover](assets/cover.webp)



## Un portefeuille puissant


Nunchuk est apparu fin 2020 avec une philosophie claire : faire de la multi-signature un standard. Il a donc été conçu pour exécuter des fonctions très avancées, avec le choix pertinent de bâtir sa conception directement sur Bitcoin Core, le logiciel de référence de l’écosystème Bitcoin.



Après plus de 4 ans de développement et d’utilisation, il est prêt à être testé à grande échelle. Si vous êtes débutant et que vous ne connaissez pas Nunchuk, ce guide vous aidera à faire vos premiers pas et à découvrir ce logiciel, dont vous pourrez ensuite approfondir les fonctions avancées après avoir surmonté la première impression. Le tutoriel lui-même s’adresse aux utilisateurs intermédiaires disposant des compétences nécessaires pour suivre toutes les étapes, mais il peut aussi être une source d’inspiration pour quiconque souhaitant développer ses connaissances. Nous commencerons avec la version mobile, et cette précision est nécessaire puisque Nunchuk dispose également d’un logiciel pour ordinateurs.



## Téléchargement


La première étape consiste évidemment à choisir où télécharger l’application. Rendez-vous sur le [site officiel](https://nunchuk.io/) où vous trouverez un peu de documentation (peu, mais c’est un début), une présentation des fonctionnalités ainsi que, tout en bas de la page, tous les liens de téléchargement.



📌 Pour ce tutoriel, j’ai choisi de vous montrer comment télécharger le portefeuille logiciel depuis le dépôt Github et comment vérifier la publication avant de l’installer sur votre téléphone. **La procédure suivante ne peut être réalisée que depuis un ordinateur**, je vous recommande donc d’effectuer toutes ces étapes sur votre poste fixe ou portable et, après toutes les vérifications, de transférer le fichier `.apk` sur votre téléphone.



![image](assets/en/01.webp)



Si vos compétences ne sont pas très avancées, vous pouvez choisir de télécharger le `.apk` depuis les magasins officiels et passer directement à la partie configuration de ce tutoriel. En revanche, si vous souhaitez franchir un cap, suivez la procédure pas à pas.



Depuis votre ordinateur de bureau, cliquez sur _Visit our open source repository_



Le lien vous dirigera vers la page Github de Nunchuk, où vous trouverez plusieurs dépôts. Nous nous concentrerons sur le dépôt _nunchuk-android_



![image](assets/en/02.webp)



Sur l’écran suivant, repérez à droite la section _Releases_ et choisissez _Latest_



![image](assets/en/03.webp)



Dans la section _Assets_, téléchargez la version publiée (dans cet exemple 1.67.apk), ainsi que les fichiers SHA256SUMS et SHA256SUMS.asc.



![image](assets/en/04.webp)



Pour trouver la clé GPG du développeur, retournez dans la section _Releases_ du dépôt et cherchez la version 1.9.53 (ou antérieure) qui contient le lien pour obtenir et télécharger la _clé GPG_



![image](assets/en/05.webp)



Nous allons procéder à la vérification grâce à un outil pratique proposé par le portefeuille Sparrow, qui dispose d’une fenêtre dédiée à cet effet et qui prend en charge les signatures PGP ainsi que les manifestes SHA256.



Lancez donc Sparrow et, depuis le menu _Tools_, choisissez _Verify Download_.



![image](assets/en/06.webp)



Dans la fenêtre qui s’ouvre, vous trouverez des champs à « remplir » : cliquez sur le bouton _Browse_ à droite et sélectionnez, pour chaque champ, les fichiers correspondants que vous venez de télécharger depuis Github. Lorsque vous aurez complété toutes les étapes, la fenêtre se présentera comme suit, avec des coches vertes et la confirmation du hachage du manifeste.



![image](assets/en/07.webp)



**N.B. La capture d’écran provient d’un PC sous Windows, mais la même pratique peut être appliquée sur tout système d’exploitation, à condition d’avoir installé, et vérifié, le portefeuille Sparrow.**



Vous trouverez le guide de Sparrow wallet pour télécharger ce portefeuille logiciel :  

https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d



Vous pouvez ensuite transférer le fichier `.apk` de votre ordinateur vers votre téléphone



![image](assets/en/08.webp)



et installer Nunchuk



![image](assets/en/09.webp)



Avant de lancer Nunchuk sur votre téléphone, ouvrez Orbot et ajoutez la nouvelle application à la liste de celles qui doivent être routées sous Tor.



![image](assets/en/11.webp)



Lancez maintenant Nunchuk. En raison des caractéristiques du projet, qui ne sont pas l’objet de ce tutoriel, Nunchuk, une fois ouvert, vous invitera à vous connecter via une adresse e-mail ou un profil Google. Tant que vous n’avez pas prévu de profiter des offres avancées de Nunchuk Inc., **évitez de vous connecter** et continuez en choisissant l’option _Continue as guest_.



![image](assets/en/12.webp)



## Paramètres


Nunchuk se présente avec une fenêtre _Home_ de présentation, qui permet de comprendre facilement sa philosophie de fonctionnement et que nous détaillerons dans un instant.



En bas, vous trouverez les menus et, comme première étape, choisissez _Profile_ pour accéder aux paramètres.



![image](assets/en/10.webp)



Sélectionnez ensuite _Display settings_, en continuant d’ignorer l’invitation à créer un compte.



![image](assets/en/14.webp)



Dans l’écran ci-dessous, vous pouvez vérifier si le portefeuille est en ligne et connecter votre serveur, en prêtant une attention particulière aux instructions fournies dans le lien accessible en cliquant sur _this guide_.



![image](assets/en/15.webp)



Enregistrez les paramètres avec la commande _Save network settings_, retournez dans le menu _Profile_ et sélectionnez _Security settings_.



![image](assets/en/16.webp)



Depuis ce menu, vous définissez le mode de protection de l’ouverture de l’application. Pour éviter tout accès indésirable, vous pouvez sécuriser Nunchuk avec la biométrie de votre téléphone et/ou ajouter un code PIN de sécurité.



![image](assets/en/17.webp)



Pensez aussi à consulter le menu _About_, que vous trouverez toujours dans la fenêtre _Profile_



![image](assets/en/18.webp)



il vous permettra de vérifier la version de l’application ou de contacter les développeurs en cas de besoin.



![image](assets/en/19.webp)



## Génération de clés et Portefeuille


Comme il est facile de le deviner à partir de la philosophie de Nunchuk, le logiciel se veut un outil utile pour la gestion de portefeuilles multi-signatures. Pour remplir cette fonction, Nunchuk permet la création de portefeuilles en les séparant des clés nécessaires à la réalisation des signatures numériques.



En effet, le fonctionnement idéal de Nunchuk implique la création de portefeuilles pouvant être en mode _watch-only_, dépendant de clés pouvant être « froides ».



Dans les écrans précédents, vous avez peut-être remarqué qu’il existe un menu en bas appelé _Keys_. Si vous venez de télécharger Nunchuk, dans _Home_ comme dans _Keys_, vous verrez un grand bouton vous invitant à ajouter une clé, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**C’est ainsi que fonctionne Nunchuk :** vous générez/importez d’abord les clés, puis vous créez le portefeuille en le configurant pour choisir quelles clés autoriseront le déverrouillage des fonds qui y sont stockés.



Même dans le cas d’un portefeuille _singlesig_, vous créez d’abord la clé, puis seulement ensuite le portefeuille. Et c’est exactement ce que nous allons faire maintenant, en commençant par un portefeuille _singlesig_ afin de briser la glace et découvrir les fonctions de Nunchuk.



Cliquez sur _Add Key_



![image](assets/en/22.webp)



Nunchuk affiche un certain nombre de dispositifs de signature pris en charge mais, pour commencer, choisissez _Software_.



![image](assets/en/23.webp)



Nunchuk va générer une phrase mnémonique qui sera stockée sur l’appareil. Vous devez alors noter la séquence de mots pour la sauvegarde, en vous assurant de créer les meilleures conditions possibles et de disposer du temps nécessaire pour le faire calmement. Le logiciel n’affiche la phrase mnémonique qu’une seule fois, que vous choisissiez de l’afficher maintenant ou plus tard, d’où l’intérêt de sélectionner _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk génère des phrases mnémoniques de 24 mots, qui apparaissent immédiatement sur l’écran suivant



![image](assets/en/25.webp)



puis effectue une vérification rapide en vous demandant de sélectionner le mot correct, parmi 3 choix, correspondant au numéro dans la séquence mnémonique.



Si vous avez correctement recopié la phrase mnémonique, le bouton _Continue_ devient actif. Appuyez dessus pour poursuivre.



![image](assets/en/26.webp)



Nommez votre clé et appuyez sur _Continue_.



![image](assets/en/27.webp)



À la fin de ces étapes, il vous sera demandé si vous souhaitez ajouter une [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) à votre phrase mnémonique. Si vous n’avez pas la pleine maîtrise de l’usage d’une passphrase, de son mode de sauvegarde ou de son fonctionnement, je vous recommande de choisir _I don't need a passphrase_.



![image](assets/en/28.webp)



La clé est enfin créée et vous est présentée dans le menu :



- Avec _Key Spec_, l’empreinte maîtresse est indiquée  
- Vous disposez de paramètres, accessibles par les trois points en haut à droite, où vous pouvez supprimer la clé ou signer un message  
- À côté du nom de la clé, vous trouverez une icône de stylo vous permettant de modifier ce nom, par exemple pour organiser vos clés à l’avenir  
- Enfin, vous pouvez vérifier l’état de la clé : en appuyant sur _Run health check_, l’application teste si une clé est compromise.



Quand tout est en ordre, cliquez sur _Done_



![image](assets/en/29.webp)



Dans le menu _Keys_, vous verrez apparaître votre première clé.



![image](assets/en/30.webp)



En allant dans le menu _Home_, l’option de création d’un portefeuille apparaît. Cliquez sur _Create new wallet_.



![image](assets/en/31.webp)



Nunchuk vous présente plusieurs possibilités, en lien pour la plupart avec des services proposés par l’entreprise, qui ne sont pas l’objet de ce tutoriel.



Dans ce guide, nous allons créer un _Hot Wallet_ et un _Custom wallet_ en détaillant les étapes.  


Commençons par le _Custom wallet_.



![image](assets/en/32.webp)



L’application vous demandera simplement de donner un nom à ce nouveau portefeuille et de choisir le script pour les adresses. Pour ce tutoriel, j’ai choisi de conserver le paramètre par défaut, _Native Segwit_. Lorsque vous avez terminé, cliquez sur _Continue_



![image](assets/en/33.webp)



La configuration du portefeuille vous demande ensuite de définir avec quelle clé les fonds de ce portefeuille seront déverrouillés. Si plusieurs clés existent, une liste vous sera proposée pour choisir. Pour le moment, nous n’avons créé qu’une seule clé : cochez celle-ci. En bas à droite, vous pouvez constater que Nunchuk prépare déjà la configuration des futurs portefeuilles multi-signatures, en augmentant le nombre de _Required keys_.



![image](assets/en/34.webp)



Comme nous créons un _singlesig_, nous laissons `1` et cliquons sur _Continue_.



Enfin, un écran de vérification apparaît, vous permettant de contrôler les caractéristiques du portefeuille :



- le nom  
- le tag `1/1 Multisig`, qui est la manière dont Nunchuk désigne un portefeuille _singlesig_  
- le type de script, `Native SegWit`  
- la clé `Keys`, avec son empreinte et son chemin de dérivation  



Lorsque tout est correct, appuyez sur _Create wallet_



![image](assets/en/35.webp)



Le portefeuille est créé et vous pouvez télécharger le fichier [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) comme sauvegarde. Pour revenir au menu principal, cliquez sur la flèche en haut à gauche.



![image](assets/en/36.webp)



Vous êtes dans _Home_, où le portefeuille nouvellement créé s’affiche avec son solde et l’état de la connexion. En cliquant sur l’espace bleu, vous accédez aux principales fonctions du portefeuille.



![image](assets/en/37.webp)



- L’icône de loupe, en haut à droite, permet d’effectuer une recherche de transaction ;  
- `View Wallet config` donne accès au menu de configuration, où vous pouvez modifier le nom du portefeuille et activer des options avancées, en haut à droite (dont il n’existe pas de captures d’écran). Ici, vous pouvez exporter la configuration du portefeuille, les étiquettes, remplacer des clés, modifier le [gap limit](https://planb.academy/en/resources/glossary/gap-limit), et plus encore.  



## Transactions avec Nunchuk



Choisissez _Receive_



![image](assets/en/38.webp)



L’application est conçue pour afficher le QR Code de l’adresse ou pour copier/partager le scriptPubKey afin de recevoir des fonds onchain.



![image](assets/en/39.webp)



Nous avons reçu un UTXO sur cette première adresse,



![image](assets/en/40.webp)



mais nous cliquons encore sur _Receive_ pour en recevoir un autre.



![image](assets/en/41.webp)



L’objectif est de vous montrer que Nunchuk vous indique cette nouvelle adresse comme une _Unused address_ mais vous signale également que vous avez des _Used addresses_ ainsi que leur nombre.



### Dépense avec coin control



Lorsque ce second UTXO est également arrivé, retournez sur l’écran principal du portefeuille pour vérifier l’état des deux transactions entrantes et, surtout, cliquez sur l’option _View coins_



![image](assets/en/42.webp)



où s’affichent vos UTXOs individuellement. Vous pouvez en examiner un en particulier en cliquant sur la petite flèche à côté du montant



![image](assets/en/43.webp)



et vérifier la date de réception, la description, bloquer l’UTXO afin qu’il ne soit pas dépensé, et plus encore.



![image](assets/en/44.webp)



Mais si vous revenez dans le menu _Coins_ en cliquant sur la flèche en haut à droite, vous pouvez activer le _Coin Control_ pour dépenser vos UTXOs de manière plus maîtrisée.



Dans l’exemple suivant, j’ai choisi de sélectionner un UTXO de 21 000 sats, puis de cliquer sur le symbole en bas à gauche.



![image](assets/en/45.webp)



Nunchuk ouvre automatiquement la fenêtre _New transaction_ pour dépenser cet UTXO. Dans la transaction de dépense, vous devez d’abord définir le montant manuellement, ou sélectionner _Send all selected_ pour envoyer l’intégralité du solde issu du coin control, sans générer de reste. Une fois le montant défini, choisissez _Continue_



![image](assets/en/46.webp)



Nunchuk vous montre ensuite où coller l’adresse à laquelle transférer les fonds, vous permet d’ajouter une description, puis de finaliser la transaction.



![image](assets/en/47.webp)


Choisir _Create transaction_ délègue la gestion automatique des frais et de la transaction à l’application. Je recommande de choisir _Custom transaction_ pour garder davantage de contrôle.



Dans ce nouvel écran, il est important de sélectionner :



- _Subtract fee from send amount_, afin d’éviter que les frais soient prélevés sur un autre UTXO présent dans le portefeuille, ce qui le dépenserait et générerait un reste (perte de confidentialité évitable) ;  
- puis définir les frais manuellement après vérification sur un explorateur.



Une fois ces étapes réalisées, cliquez sur _Continue_



![image](assets/en/48.webp)



L’écran suivant présente le récapitulatif complet de la transaction. Si tout est correct, confirmez en sélectionnant _Confirm and create transaction_.



![image](assets/en/49.webp)



Avec _Pending signatures_, Nunchuk vous avertit que la transaction attend votre signature pour autoriser la dépense, signature que vous apposez en cliquant sur _Sign_.



![image](assets/en/50.webp)



La commande _Broadcast_ apparaît en bas pour propager la transaction finalisée et signée.



![image](assets/en/51.webp)



### Dépense depuis le menu _Send_



Alors que sur la page principale du portefeuille nous voyons la transaction sortante en attente de confirmation, utilisons le menu _Send_ pour simuler une dépense quotidienne.



![image](assets/en/52.webp)



Cliquer sur _Send_ fait apparaître l’écran d’envoi de transaction, identique à celui que nous venons de voir mais sans passer par le coin control.



Dans ce second exemple également, j’ai choisi _Custom transaction_ et d’envoyer la totalité du montant, mais j’aurais pu le définir manuellement. Une fois le montant choisi, appuyez sur _Continue_.



![image](assets/en/53.webp)



Vérifiez ensuite si les frais sont bien soustraits de l’UTXO en question (dans cet exemple, le choix est forcé car il n’y en a qu’un), ajustez manuellement les frais selon la situation du mempool, puis appuyez sur _Continue_.



![image](assets/en/54.webp)



Si l’écran de résumé est satisfaisant, choisissez _Confirm and create transaction_.



![image](assets/en/55.webp)



Signez la transaction avec _Sign_



![image](assets/en/56.webp)



et diffusez-la sur le réseau.



![image](assets/en/57.webp)



Le portefeuille se retrouve alors avec un solde à zéro et l’historique en cours de mise à jour.



![image](assets/en/58.webp)

## Création d’un « Hot Wallet »



Enfin, afin de ne rien omettre des étapes initiales de Nunchuk mobile, voyons comment l’application crée ce qu’elle appelle un « Hot Wallet ».



Dans le menu _Home_ de Nunchuk, où apparaît la liste des portefeuilles, cliquez sur le `+` en haut à droite.



![image](assets/en/59.webp)



Choisissez _Hot wallet_ parmi les options



![image](assets/en/60.webp)



Nunchuk dispense quelques conseils concernant l’utilisation des Hot Wallets sur la page de présentation. Sélectionnez _Continue_ pour poursuivre.



![image](assets/en/61.webp)



Après quelques instants, le portefeuille est créé et apparaît dans la liste avec une couleur brunâtre. C’est la couleur utilisée par Nunchuk pour vous avertir que vous n’avez pas encore sauvegardé le portefeuille.



![image](assets/en/62.webp)



Cliquez sur le nom du portefeuille pour accéder à ses configurations : vous remarquerez une invitation à sauvegarder immédiatement la phrase mnémonique.



![image](assets/en/63.webp)



La procédure est la même que celle déjà vue précédemment, nous ne reviendrons donc pas dessus. Une fois la sauvegarde effectuée, Nunchuk vous amène à la page de la clé correspondante, que vous pouvez modifier comme celle que vous aviez créée via la procédure _Custom_.



![image](assets/en/64.webp)



Essayez également _Run health check_



![image](assets/en/65.webp)



ou encore affichez tous vos portefeuilles dans le _Home_ de l’application.



![image](assets/en/66.webp)



## À garder à l’esprit pour continuer de façon autonome


De la même manière qu’il existe un ordre pour la création, d’abord générer les clés, puis créer le portefeuille, il faut respecter l’ordre inverse lors de la suppression de ces éléments dans l’application.



Si vous devez supprimer l’une des clés, il est indispensable d’avoir au préalable supprimé le ou les portefeuilles qui utilisent cette clé de signature pour des transactions : d’abord supprimer les portefeuilles, ensuite seulement les clés. Si vous ne respectez pas cet ordre, vous ne pourrez pas retirer la clé.



Maintenant que vous savez comment débuter avec Nunchuk, vous pouvez continuer à explorer cette application et en découvrir les subtilités. Dans ce tutoriel, nous n’avons fait que les premiers pas, mais ce portefeuille logiciel peut répondre à des besoins plus avancés et à des usages plus sophistiqués.
