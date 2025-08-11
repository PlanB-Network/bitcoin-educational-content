---
name: PureOS
description: La distibution Linux qui vous donne le contrôle sur votre vie numérique.
---

![cover](assets/cover.webp)

Protéger ses informations personnelles à l'ère du numérique est l'une des priorités pour tout internaute. Les entreprises, les organisations et même les systèmes d'exploitations sont des sources utiles d'informations pour définir votre profil et votre mode de vie. Choisir un bon système d'exploitation est la première étape pour renforcer la protection de sa vie privée sur internet. Dans ce tutoriel, nous découvrirons PureOS, une distribution Linux axée sur la protection de la vie privée.

https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Débuter avec PureOS

PureOS est un système d'exploitation basé sur Debian développé par l'entreprise Purism. PureOS convient aussi bien aux professionnels de l’informatique qu’aux utilisateurs recherchant une distribution simple et facile à prendre en main. Sa particularité est qu'il est entièrement libre (*Free Software*), et met l'accent sur la protection des données personnelles de ses utilisateurs en mettant en place un cadre de travail axé sur la vie privée, la liberté, la sécurité et la stabilité offertes par Debian.

### Pourquoi choisir PureOS ?

- **Interface simple et intuitive** : GNOME propose une interface bureautique claire, conçue pour être facile à utiliser, même pour les personnes peu à l’aise avec la ligne de commande.

- **Gratuit** : comme la majorité des distributions Linux, PureOS est entièrement gratuit et libre d’utilisation. Il est cependant possible de souscrire à un abonnement mensuel pour soutenir les développeurs.

- **Sécurité et grande stabilité** : l’architecture de PureOS et son mode de fonctionnement en font une distribution très sécurisée, garantissant la protection de vos données ainsi que la stabilité du système.

- **Documentation et communauté active** : PureOS dispose d’une documentation claire et accessible, ainsi que d’une communauté engagée et réactive, ce qui facilite la résolution des problèmes et l’apprentissage progressif du système.

## Installation et configuration

Installer et configurer PureOS sur votre ordinateur vous nécessitera des caractéristiques minimalistes suivantes :
- Une clé USB d'au moins 8Go pour flasher le système.
- 4 Go de RAM.
- 30 Go d'espace libre sur votre disque dur.

Rendez-vous sur le [site officiel de PureOS](https://pureos.net/) puis téléchargez l'image ISO du système d'exploitation selon l'architecture de votre machine.

Pour lancer l’installation de PureOS, il est nécessaire de créer une clé USB bootable à l’aide d’un logiciel de flash comme [Balena Etcher](https://www.balena.io/etcher).

En trois étapes simples, vous obtenez une clé USB bootée avec le système d'exploitation PureOS.

- Branchez la clé USB puis exécutez le logiciel Balena préalablement téléchargé.
- Sélectionnez ensuite l'image ISO de PureOS
- Choisissez la clé USB comme périphérie de sortie ensuite cliquez sur le bouton **Flash** puis attendez la fin du processus.

![0_01](assets/fr/01.webp)

Une fois la clé USB bootée, procédez à un redémarrage de l'ordinateur sur lequel vous souhaitez installer PureOS.

Lors du démarrage, accédez au BIOS en cliquant sur la touche `ESC`, `F9` ou `F11` selon votre machine. Sélectionnez la clé USB comme périphérie d'amorçage puis validez avec la touche `ENTRER`.

### Ecran de démarrage

PureOS vous offre plusieurs options de démarrage de son système d'exploitation. Choisissez l'option **Test or Install PureOS** pour lancer l'installation du système d'exploitation.

![0_02](assets/fr/02.webp)

Définissez la langue et la disposition du clavier que vous souhaitez utiliser sur votre ordinateur.

![0_03](assets/fr/03.webp)

![0_04](assets/fr/04.webp)

Autorisez ou non l’accès à votre **position géographique** aux applications pour des recommandations personnalisées en fonction de votre zone.

![0_05](assets/fr/05.webp)

Vous avez la possibilité de vous connecter à votre compte **NextCloud** existant pour retrouver les données liées à la suite bureautique que vous utilisez sur un autre système.

![0_06](assets/fr/06.webp)

Un tutoriel de prise en main vous est proposé mais vous avez la possibilité de fermer la fenêtre si vous voulez ignorer cette étape.

![0_08](assets/fr/08.webp)

### Lancement de l'installation

Cliquez sur le menu **Activities**  et explorez les applications et les outils préinstallés sur le système. Vous pourrez lancer l'installation en cliquant sur **Install PureOS**

![0_09](assets/fr/09.webp)

Configurez à votre souhait la langue et la disposition du clavier voulues pour le système puis configurez le mode de partitionnement du disque dur.

![0_10](assets/fr/10.webp)

![0_11](assets/fr/11.webp)

![0_12](assets/fr/12.webp)

![0_13](assets/fr/13.webp)

Deux options se présentent à vous pour le partitionnement de votre disque dur :
- **Erase disk** : Pour une installation complète de PureOS en supprimant toutes les données préexistantes sur votre disque dur.

![0_14](assets/fr/14.webp)

- **Manual Partitionning** pour créer vos partitions

⚠️ Lorsque vous créez manuellement les partitions pour votre système d'exploitation, assurez-vous d'allouer une partition de 2 Go minimum pour le fonctionnement de PureOS puis une autre partition pour les données.

![0_15](assets/fr/15.webp)

Activez le **chiffrement du disque** si vous souhaitez sécuriser vos données. Renseignez pour cela un mot de passe fort et complexe.

Associez un utilisateur à votre système d'exploitation en définissant un nom d'utilisateur et un mot de passe alphanumérique d'au moins 20 caractères pour renforcer la sécurité de vos données.

![0_16](assets/fr/16.webp)

Passez en revue, les configurations que vous avez effectuées et modifiez-les si nécessaire.

![0_17](assets/fr/17.webp)

Cliquez sur le bouton **Install** puis **Install Now** pour confirmer l'installation de PureOS sur votre ordinateur.

![0_18](assets/fr/18.webp)

![0_19](assets/fr/19.webp)

A la fin de l'installation, cochez la case **Restart now** pour redémarrer votre ordinateur puis confirmez :
- La langue.
- La disposition du clavier.
- Votre compte NextCloud (facultatif).

![0_25](assets/fr/25.webp)

## Mises à jour

Avant de commencer à utiliser PureOS, il est essentiel de mettre à jour votre système. Cela permet de bénéficier des dernières fonctionnalités, des correctifs de sécurité récents, et d’assurer une meilleure stabilité.

- **Mise à jour via l’interface graphique** :
Ouvrez l’application **Logiciels**, puis rendez-vous dans l’onglet **Mises à jour**. Les mises à jour disponibles s’affichent automatiquement. Cliquez sur **Télécharger**, puis sur **Installer** une fois le téléchargement terminé.

-  **Mise à jour via le terminal** :
Ouvrez le terminal, puis entrez la commande suivante pour mettre à jour la liste des paquets disponibles :

```shell
 sudo apt update
 ```
 
Entrez votre mot de passe et validez. Ensuite, installez les mises à jour avec :

```shell
sudo apt full-upgrade
```

## PureOS pour le développement

Par défaut, PureOS ne comprend pas tous les outils nécessaires au développement.  
Vous pouvez les installer rapidement à l’aide de la commande suivante :

```shell
sudo apt install build-essential git curl
```

Cela installera les outils de compilation, **Git** et **Curl**, utiles dans la majorité des environnements de développement.

## L'environnement PureOS

PureOS se distingue par son approche innovante de convergence réelle : un seul système d’exploitation assure un fonctionnement fluide et homogène sur divers appareils, tels que ordinateurs portables, tablettes, mini-PC et smartphones.

Les applications PureOS sont conçues pour être adaptatives : elles s’ajustent automatiquement à la taille de l’écran et au mode d’entrée (tactile ou clavier/souris). Par exemple, le navigateur GNOME Web adapte dynamiquement son interface pour offrir une expérience optimale aussi bien sur mobile que sur bureau.

PureOS intègre également la suite bureautique **LibreOffice**, qui comprend :

- **Writer** : un traitement de texte complet pour créer et éditer vos documents.
- **Calc** : un tableur puissant pour gérer vos données et calculs.
- **Impress** : un outil de création de présentations professionnelles.

Cette suite libre vous permet de travailler efficacement sans dépendre de logiciels propriétaires.

PureOS offre un environnement unifié, sécurisé et flexible, basé sur une distribution 100 % libre qui garantit un contrôle total et un respect strict de la vie privée. Sa convergence réelle facilite la création d’applications compatibles avec différents types d’appareils, comme les ordinateurs, les tablettes et les smartphones, sans nécessiter d’adaptation complexes.

Grâce à un accès natif aux outils essentiels, à des gestionnaires de paquets robustes et à un riche écosystème logiciel libre, PureOS simplifie le développement, le test et le déploiement d’applications dans un cadre sécurisé. Son architecture stable et son engagement envers la confidentialité en font une plateforme fiable, adaptée à divers usages, notamment le développement blockchain, le prototypage rapide ou les environnements de production.

Découvrez notre cours sur le renforcement de sa sécurité et la protection de sa vie privée numérique.

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1


