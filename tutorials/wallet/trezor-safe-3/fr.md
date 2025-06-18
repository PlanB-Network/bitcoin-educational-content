---
name: Trezor Safe 3
description: Configurer et utiliser le hardware wallet Safe 3
---
![cover](assets/cover.webp)

*Image credit: [Trezor.io](https://trezor.io/)*

Le Trezor Safe 3 est un hardware wallet conçu par SatoshiLabs et créé en 2023. C’est un modèle très compact et léger (14 grammes) pensé à la fois pour les débutants et les utilisateur intermédiaires. Il succède au célèbre Model One avec des apports importants, tout en conservant l’approche open-source de la marque qui la différencie de son principal concurrent, Ledger. Le Safe 3 est proposé à 79 €. Il se positionne donc dans le segment milieu de gamme des hardware wallets, en concurrence directe avec le Ledger Nano S Plus.

Le Safe 3 ne possède pas de batterie et fonctionne exclusivement via une connexion USB-C, utilisée à la fois pour l'alimentation et pour la communication. Il est équipé d'un petit écran OLED monochrome de 0,96 pouce et de deux boutons physiques.

![Image](assets/fr/01.webp)

Le Safe 3 offre toutes les fonctionnalités essentielles attendues d'un bon hardware wallet, avec notamment une excellente intégration de la passphrase BIP39. Cependant, il ne supporte pas encore Miniscript.

Ce modèle est particulièrement adapté aux débutants, et pourrait même être le hardware wallet que je recommanderais à un nouvel utilisateur. Il convient aussi bien aux utilisateurs intermédiaires. En revanche, il peut ne pas répondre à toutes les attentes des utilisateurs avancés qui recherchent des fonctionnalités plus spécifiques, disponibles sur des appareils comme le Coldcard. Néanmoins, si ces options avancées ne vous sont pas nécessaires, le Trezor Safe 3 peut s'avérer être un excellent choix.

## Le modèle de sécurité du Trezor Safe 3

Le Trezor Safe 3 est désormais équipé d'un **Secure Element certifié EAL6+**, une avancée significative par rapport aux modèles antérieurs tels que le Model One et le Model T. Il s'agit de la puce OPTIGA Trust M V3, qui ne stocke pas directement la seed mais joue un rôle de composant cryptographique pour en sécuriser l'accès. Le Secure Element retient un secret qui n'est accessible qu'après la saisie correcte du PIN par l'utilisateur. Ce secret est ensuite utilisé pour déchiffrer la seed, qui est conservée chiffrée dans la mémoire principale de l'appareil.

Ce système de sécurité hybride offre une meilleure protection physique, notamment contre les attaques par extraction ou analyse invasive, problèmes auxquels le Model One pouvait être sujet, notamment dans la gestion du code PIN. Ces vulnérabilités sont désormais contournées grâce à l'utilisation du Secure Element. Ce modèle maintient également une architecture logicielle open-source : le code qui gère la génération et l'utilisation des clés privées reste entièrement accessible et vérifiable. La puce OPTIGA gère uniquement le code PIN, un élément externe à la gestion des clés du portefeuille Bitcoin. Elle se limite à libérer un secret permettant de déchiffrer la seed. Aussi, la puce OPTIGA Trust M V3 bénéficie d'une licence relativement libre, qui autorise SatoshiLabs à publier librement les vulnérabilités potentielles.

Ce modèle de sécurité représente, à mon avis, l'un des meilleurs compromis disponibles sur le marché actuellement. Il combine les avantages d'un Secure Element avec une gestion logicielle open-source. Auparavant, les utilisateurs devaient choisir entre une sécurité physique renforcée avec une puce et la transparence avec l'open-source ; avec le Trezor Safe 3, il est possible de bénéficier des deux.

Dans ce tutoriel, vous allez découvrir comment configurer et utiliser de manière sécurisée votre Trezor Safe 3.

## Unboxing du Trezor Safe 3

Lorsque vous recevez votre Safe 3, assurez-vous que la boîte et le sceau sont intacts pour confirmer que le paquet n'a pas été ouvert. Une vérification logicielle de l'authenticité et de l'intégrité du dispositif sera également réalisée lors de sa configuration plus tard.

Le contenu de la boîte inclut :
- Le Trezor Safe 3 ;
- Une pochette contenant des papiers cartonnés pour noter votre phrase mnémonique, des autocollants, et une notice ;
- Un câble USB-C vers USB-C.

![Image](assets/fr/02.webp)

À l'ouverture, votre Trezor Safe 3 devrait être protégé par un plastique de protection et le port USB-C doit être sécurisé par un sceau holographique. Assurez-vous de sa présence.

![Image](assets/fr/03.webp)

La navigation sur l'appareil est assez simple : utilisez le bouton droit pour défiler vers la droite, et le bouton gauche pour défiler à gauche. Appuyez simultanément sur les deux boutons pour confirmer une action. 

![Image](assets/fr/04.webp)

## Prérequis

Pour ce tutoriel, je vais vous montrer comment utiliser le Trezor Safe 3 avec [le logiciel de gestion de portefeuille Sparrow Wallet](https://sparrowwallet.com/download/). Si vous n'avez pas encore installé ce logiciel, je vous invite à le faire dès maintenant. Si vous avez besoin d'aide, nous disposons également d'un tutoriel détaillé sur la configuration de Sparrow Wallet :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Vous aurez également besoin du logiciel Trezor Suite pour configurer le Safe 3, vérifier son authenticité et installer le firmware. Nous utiliserons ce logiciel uniquement pour cela ; puis par la suite, il sera nécessaire uniquement pour les mises à jour du firmware. Pour la gestion quotidienne du portefeuille, nous utiliserons exclusivement Sparrow Wallet, car il est optimisé pour Bitcoin et pratique à utiliser, même pour les débutants (Sparrow ne prend en charge que le bitcoin et non les altcoins).

[Téléchargez Trezor Suite depuis le site officiel.](https://trezor.io/trezor-suite)

![Image](assets/fr/05.webp)

Pour ces deux logiciels, je vous recommande fortement de vérifier à la fois leur authenticité (avec GnuPG) et leur intégrité (via le hash) avant de les installer sur votre machine. Si vous ne savez pas comment le faire, vous pouvez suivre cet autre tutoriel :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Démarrage du Trezor Safe 3

Branchez votre Safe 3 à votre ordinateur où Trezor Suite et Sparrow Wallet sont déjà installés.

![Image](assets/fr/06.webp)

Ouvrez Trezor Suite, puis cliquez sur "*Set up my Trezor*".

![Image](assets/fr/07.webp)

Sélectionnez "*Bitcoin-only firmware*", puis cliquez sur "*Install Bitcoin-only*".

![Image](assets/fr/08.webp)

Trezor Suite va alors procéder à l'installation du firmware sur votre Safe 3. Patientez pendant l'installation.

![Image](assets/fr/09.webp)

Cliquez sur "*Continue*".

![Image](assets/fr/10.webp)

Procédez ensuite au test d'authenticité pour vous assurer que votre hardware wallet n'est pas faux ou compromis.

![Image](assets/fr/11.webp)

Sur votre Safe 3, appuyez sur le bouton de droite pour confirmer.

![Image](assets/fr/12.webp)

Si votre Trezor est authentique, un message de confirmation apparaîtra dans Trezor Suite.

![Image](assets/fr/13.webp)

Vous pouvez ensuite passer les fenêtres avec les instructions de base d'utilisation.

![Image](assets/fr/14.webp)

## Création d'un portefeuille Bitcoin

Sur Trezor Suite, cliquez sur le bouton "*Create new wallet*".

![Image](assets/fr/15.webp)

Pour un portefeuille standard, vous pouvez opter pour le type de sauvegarde par défaut. Cela permet de créer un portefeuille single-sig classique avec une phrase mnémonique de 12 mots. Cliquez sur "*Create wallet*".

Si vous souhaitez en savoir plus sur les autres options de sauvegarde disponibles sur les Trezor, notamment le *Multi-share Backup*, je vous recommande de consulter également ce tutoriel :

https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)

Acceptez les conditions d'utilisation sur le hardware wallet.

![Image](assets/fr/17.webp)

Appuyez de nouveau sur le bouton droit pour créer un nouveau portefeuille.

![Image](assets/fr/18.webp)

Dans Trezor Suite, cliquez sur "*Continue to backup*".

![Image](assets/fr/19.webp)

Le logiciel vous fournit des instructions sur la manière de gérer votre phrase mnémonique.

Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Trezor Safe 3.

La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre hardware wallet. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Validez les instructions, puis cliquez sur le bouton "*Create wallet backup*".

![Image](assets/fr/20.webp)

Le Safe 3 va créer votre phrase mnémonique en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis sur l'écran sur le support physique de votre choix. Selon votre stratégie de sécurisation, vous pouvez envisager de réaliser plusieurs copies physiques complètes de la phrase (mais surtout, ne la divisez pas). Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

***Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.***

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)

Pour passer aux mots suivants, cliquez sur le bouton droit. Vous pouvez revenir en arrière en cliquant sur le bouton gauche. Une fois tous les mots notés, restez appuyé sur le bouton droit pour passer à l'étape suivante.

![Image](assets/fr/22.webp)

Sélectionnez les mots de votre phrase mnémonique en fonction de leur ordre pour confirmer que vous les avez correctement notés. Utilisez les boutons de gauche et de droite pour naviguer entre les propositions, puis sélectionnez le bon mot en cliquant sur les 2 boutons simultanément.

![Image](assets/fr/23.webp)

Une fois cette procédure de vérification terminée, cliquez sur le bouton de droite.

![Image](assets/fr/24.webp)

## Mise en place du code PIN

Vient ensuite l'étape du code PIN. Le code PIN permet de déverrouiller votre Trezor. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 mots vous permettra de retrouver l'accès à vos bitcoins.

Sur Trezor Suite, cliquez sur "*Continue to PIN*", puis sur le bouton "*Set PIN*".

![Image](assets/fr/25.webp)

Confirmez sur le Safe 3.

![Image](assets/fr/26.webp)

Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Trezor (par exemple, dans un gestionnaire de mot de passe). Vous avez la possibilité de définir un code PIN composé de 8 à 50 chiffres. Je vous recommande de choisir un code PIN aussi long que possible pour renforcer la sécurité.

Utilisez les boutons de droite et de gauche pour sélectionner chaque chiffre. Pour confirmer votre choix et passer au chiffre suivant, appuyez simultanément sur les deux boutons.

![Image](assets/fr/27.webp)

Une fois terminé, cliquez sur la coche "*ENTER*" au début des chiffres, puis confirmez votre PIN une seconde fois.

![Image](assets/fr/28.webp)

Votre code PIN a bien été enregistré.

![Image](assets/fr/29.webp)

Sur Trezor Suite, cliquez sur le bouton "*Complete setup*".

![Image](assets/fr/30.webp)

La configuration de votre Safe 3 est désormais terminée. Si vous le souhaitez, vous pouvez modifier le nom et la page d'accueil de votre hardware wallet.

![Image](assets/fr/31.webp)

Nous n'aurons plus besoin du logiciel Trezor Suite, sauf pour effectuer des mises à jour régulières du firmware de votre hardware wallet, ou bien si vous souhaitez faire un test de récupération. Nous allons maintenant utiliser Sparrow pour gérer le portefeuille, car ce logiciel est parfaitement adapté pour une utilisation Bitcoin-only.

## Configurer le portefeuille sur Sparrow Wallet

Commencez par télécharger et installer Sparrow Wallet [depuis le site officiel](https://sparrowwallet.com/) sur votre ordinateur, si ce n'est pas déjà fait.

Une fois Sparrow Wallet ouvert, assurez-vous que le logiciel est bien connecté à un nœud Bitcoin, ce qui est indiqué par la coche en bas à droite de l'interface. Si vous rencontrez des difficultés pour connecter Sparrow, je vous recommande de consulter le début de ce tutoriel :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Cliquez sur l'onglet "*File*", puis sur "*New Wallet*".

![Image](assets/fr/32.webp)

Nommez votre portefeuille, puis cliquez sur "*Create Wallet*".

![Image](assets/fr/33.webp)

Dans le menu déroulant "*Script Type*", sélectionnez le type de script qui sera utilisé pour sécuriser vos bitcoins. Je vous recommande d'opter pour "*Taproot*", ou à défaut, "*Native SegWit*".

![Image](assets/fr/34.webp)

Cliquez sur le bouton "*Connected Hardware Wallet*". Votre Safe 3 doit évidemment être connecté à l'ordinateur et déverrouillé.

![Image](assets/fr/35.webp)

Cliquez sur le bouton "*Scan*". Votre Safe 3 devrait apparaitre. Cliquez sur "*Import Keystore*".

![Image](assets/fr/36.webp)

Vous pouvez maintenant voir les détails de votre portefeuille, y compris la clé publique étendue de votre premier compte. Cliquez sur le bouton "*Apply*" pour finaliser la création du portefeuille.

![Image](assets/fr/37.webp)

Choisissez un mot de passe fort pour sécuriser l'accès à Sparrow Wallet. Ce mot de passe assurera la sécurité de l'accès aux données de votre portefeuille sur Sparrow, ce qui permet de protéger vos clés publiques, vos adresses, vos labels et l'historique de vos transactions contre tout accès non autorisé.

Je vous conseille de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour ne pas l'oublier.

![Image](assets/fr/38.webp)

Et voilà, votre portefeuille est bien importé sur Sparrow Wallet !

![Image](assets/fr/39.webp)

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub, puis réinitialisez votre Trezor Safe 3 tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille sur le Trezor en utilisant vos sauvegardes papier. Vérifiez que la xpub générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Comment recevoir des bitcoins avec le Trezor Safe 3 ?

Sur Sparrow, cliquez sur l'onglet "*Receive*".

![Image](assets/fr/40.webp)

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de votre Trezor. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que le hardware wallet détient bien la clé privée nécessaire pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse. Cela vous permet d'éviter plusieurs types d'attaques.

Pour effectuer cette vérification, cliquez sur le bouton "*Display Address*".

![Image](assets/fr/41.webp)

Vérifiez que l'adresse affichée sur votre Trezor correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité. Vous pouvez utiliser les boutons pour confirmer.

![Image](assets/fr/42.webp)

Vous pouvez ensuite ajouter un "*Label*" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

![Image](assets/fr/43.webp)

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

![Image](assets/fr/44.webp)

## Comment envoyer des bitcoins avec le Trezor Safe 3 ?

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille sécurisé avec le Safe 3, vous pouvez également les dépenser ! Connectez votre Trezor à votre ordinateur, déverrouillez-le à l'aide du code PIN, lancez Sparrow Wallet, puis allez dans l'onglet "*Send*" pour construire une nouvelle transaction.

![Image](assets/fr/45.webp)

Si vous souhaitez faire du *Coin Control*, c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "*UTXOs*". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "*Send Selected*". Vous serez redirigé vers le même écran de l'onglet "*Send*", mais avec vos UTXOs déjà sélectionnés pour la transaction.

![Image](assets/fr/46.webp)

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "*+ Add*".

![Image](assets/fr/47.webp)

Notez un "*Label*" pour vous souvenir de l'objet de cette dépense.

![Image](assets/fr/48.webp)

Choisissez le montant envoyé à cette adresse.

![Image](assets/fr/49.webp)

Ajustez le taux de frais de votre transaction en fonction du marché du moment. Vous pouvez par exemple utiliser [mempool.space](https://mempool.space/) pour choisir un taux de frais adapté.

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "*Create Transaction*".

![Image](assets/fr/50.webp)

Si tout vous convient, cliquez sur "*Finalize Transaction for Signing*".

![Image](assets/fr/51.webp)

Cliquez sur "*Sign*".

![Image](assets/fr/52.webp)

Cliquez sur "*Sign*" à côté de votre Trezor Safe 3.

![Image](assets/fr/53.webp)

Vérifiez les paramètres de la transaction sur l'écran de votre hardware wallet, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais. Une fois la transaciton vérifiée sur le Trezor, cliquez sur les deux bouton simultanément pour la signer.

![Image](assets/fr/54.webp)

Votre transaction est désormais signée. Vérifiez une dernière fois que tout vous convient, puis cliquez sur "*Broadcast Transaction*" pour la diffuser sur le réseau Bitcoin.

![Image](assets/fr/55.webp)

Vous pouvez la retrouver dans l'onglet "*Transactions*" de Sparrow Wallet.

![Image](assets/fr/56.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de base du Trezor Safe 3 avec Sparrow Wallet ! Pour aller plus loin, je vous recommande de consulter ce tutoriel complet sur l'utilisation d'un hardware wallet Trezor avec une passphrase BIP39 afin de renforcer votre sécurité :

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !
