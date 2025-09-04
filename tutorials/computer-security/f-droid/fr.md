---
name: F-Droid
description: Le catalogue d'applications libres et gratuites.
---

![cover](assets/cover.webp)

A l'ère du numérique, les grandes entreprises et les institutionnels travaillent à rendre Internet plus centralisé, plaçant son contrôle entre leurs mains, ce qui entrave la confidentialité et la liberté de tous les utilisateurs. Ceci n'est pas une utopie, c'est déjà le cas. En étant bitcoiner, la décentralisation, le respect de la vie privée et des libertés individuelles sont des principes qui vous tiennent à cœur notamment sur les outils que vous utilisez au quotidien. Android, contrairement à iOS, autorise depuis des années la coexistence de plusieurs boutiques d'applications au sein de son écosystème vous offrant une liberté de trouver et d'installer vos applications selon vos sources favorites.

Dans ce tutoriel, nous découvrirons F-droid, un répertoire d'applications qui représente une alternative aux magasins d'applications tels que Google Play Store, Microsoft Store.

## Débuter avec F-Droid

F-Droid est un magasin d'applications et d'outils qui vous permet d'installer des applications libres et gratuites sur la plateforme Android. F-droid, lui-même est un projet open source débuté en 2010 par Ciaran Gultnieks et plusieurs autres contributeurs. L'objectif principal du projet est de rendre accessible des applications Open Source et de permettre aux initiateurs de projets Open Source de trouver une plateforme où publier leurs outils sans se référer à Google Play Store.

Malheureusement, F-Droid n'est pas une application disponible sur iOS, et contient beaucoup d'outils conçus pour les systèmes Android.

Vous pouvez télécharger F-droid depuis [le site officiel](https://f-droid.org/) sous format APK et l'installer manuellement sur votre téléphone Android.

![download](assets/fr/02.webp)

Sur Android, assurez-vous d'accorder les permissions d'installation pour le navigateur depuis lequel vous avez téléchargé F-Droid.

Une fois l'installation achevée, F-Droid lancera une mise à jour des répertoires d'applications Open Source afin d'enrichir les applications dans le magasin.

![repositories](assets/fr/03.webp)

Vous avez désormais des applications installables sur votre téléphone sans passer par Google Play Store.

## La librairie de F-Droid

Dans le magasin d'applications, vous trouverez plusieurs catégories d'applications qui correspondent à vos besoins. Dans l'onglet **Catégories**, il y a plus de 20 types d'applications, partant des navigateurs aux éditeurs de textes gratuits et nécessitant le moins d'informations de votre part.

Souhaitez-vous installer une application en particulier ? Cliquez sur le bouton **Rechercher** puis insérez le nom de l'application que vous recherchez.

![search](assets/fr/04.webp)

F-Droid vous met à disposition des informations complètes sur chaque application que vous souhaitez installer.

En cliquant sur l'application, vous trouverez notamment :
- Les fonctionnalités et les changements ajoutés dans la dernière version disponible
- Une description détaillée de l'application, ses fonctionnalités, les raisons de l'utiliser, la communauté Open Source derrière le projet.

![features](assets/fr/05.webp)

- La licence utilisé par le projet, les liens vers le code source et vers les problèmes rencontrés lors de l'utilisation de l'application
- Les permissions requises par l'application

![permissions](assets/fr/06.webp)

Découvrez plus en détails notre tutoriel sur Thunderbird :

https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid, vous présente toutes les informations dont vous avez besoin pour décider si l'utilisation d'une application protège vos données et renforce votre confidentialité. Analysez donc toutes les applications que vous souhaitez utiliser puis cliquez sur le bouton **Installer** pour télécharger et installer votre application.
Accordez le droit d'installation à F-Droid en activant l'option dans vos paramètres.

![settings](assets/fr/07.webp)

## Echangez vos applications

F-Droid encourage la pratique de l'open source et de la contribution communautaire notamment via son option d'échanges **Near By**. Connectez vous aux utilisateurs autour de vous via :
- La détection Bluetooth;
- Le même réseau Wi-Fi;
- Code QR ou une adresse IP:PORT à renseigner dans votre navigateur.

Vous pouvez, à partir de cette option, partager et recevoir des applications installées sur votre téléphone Android avec vos proches en quelques étapes.

![swap](assets/fr/08.webp)

## Les mises à jour

Dans l'onglet **Mise à jour**, consultez la liste des mises à jour disponible,  assurez vous de lire également les informations concernant les nouvelles versions de chaque application pour connaître les changements majeurs effectués par rapport à la version que vous utilisez.

![updates](assets/fr/09.webp)

Vous pouvez également mettre à jour la liste des applications disponibles en rafraîchissant la page (tirez vers le bas).

## Ajoutez vos propres applications

F-Droid est un projet Open Source qui encourage les contributions sur les applications qui priorisent la confidentialité des utilisateurs. Vous pouvez ajouter votre propre application mobile Android sur le magasin en passant par des contributions sur le code Source GitLab du F-Droid. 

Votre application doit être Open Source avec le code source disponible publiquement sur GitHub, GitLab par exemple. 
Vous devez ensuite préparer un fichier YAML (les métadonnées) qui décrit votre application y compris toutes informations et les permissions nécessaire pour son utilisation en vous suivant le [template de metadonnées](https://f-droid.org/docs/Build_Metadata_Reference/) proposé par F-Droid.

Retrouvez dans la section **Developers** de la [documentation](https://f-droid.org/en/docs/), toutes les ressources pour publier et maintenir vos applications sur F-Droid.

### Intégrité et Sécurité

Mettre une application en open source est souvent synonyme d'une sécurité grandissante mais également d'un risque non négligeable. Comment s'assurer qu'il n'y ait pas d'altération malicieuse dans le code source d'une application disponible sur F-Droid ?

F-Droid compile sur leur propres serveurs, les applications en se basant sur le code source officiel et des instructions de compilation. Chaque application publiée est donc reconstruite et vérifiée pour s'assurer qu'elle n'a pas été compromise. Cela permet de s'assurer que l'APK proposé est fidèle au code source publié par les développeurs. En outre, chaque application installée via F-Droid est signée numériquement puis l'empreinte de la signature est comparée avec celle annoncée par les développeurs de l'application sur le site officiel ou sur le dépôt Git.

Si vous avez apprécié ce tutoriel, découvrez notre cursus sur la sécurité informatique et la gestion des données :

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

