---
name: Manjaro
description: Rendre plus accessible la puissance d'Arch Linux
---
![cover](assets/cover.webp)

Arch Linux est un système d’exploitation très apprécié dans de nombreux domaines pour sa robustesse et sa stabilité. Cependant, il peut se révéler difficile à aborder pour les utilisateurs débutants. C’est précisément pour répondre à ce problème que **Manjaro** a été créé : offrir la puissance d’Arch Linux, mais avec une expérience plus simple et accessible en se basant sur une interface intuitive et facile à prendre en main.

## Débuter avec Manjaro

L’un des grands atouts de Manjaro réside dans son **système de mises à jour simple et efficace**. Inutile de les gérer manuellement : Manjaro s’en charge pour vous ! Une icône dans la zone de notification (l’emplacement varie selon l’édition) vous avertit lorsqu’une mise à jour est disponible. Il vous suffit ensuite de suivre les instructions et le processus se fait rapidement, sans effort.

Manjaro propose également un **vaste catalogue d’applications**. Puisque Manjaro est basée sur Arch Linux, elle bénéficie d’un accès direct à ses dépôts officiels, riches en logiciels variés, y compris des applications propriétaires. Manjaro retarde légèrement certaines mises à jour d’Arch Linux pour procéder à des tests supplémentaires ; cela améliore la stabilité au prix d’un léger décalage sur les nouveautés. Et si ce choix ne vous suffit pas, vous pouvez aussi accéder à l’**AUR (*Arch User Repository*)**, une immense bibliothèque gérée par la communauté. Si un programme n’existe pas dans les dépôts officiels, il y a de fortes chances qu’il soit disponible dans l’AUR.

Un autre avantage de Manjaro est qu’elle est **bien moins gourmande en ressources** que des systèmes comme Windows ou macOS. Elle consomme moins de mémoire vive (RAM) et de puissance de calcul, ce qui en fait un choix idéal pour les ordinateurs plus anciens ou moins performants : votre machine gagne en fluidité et en rapidité, retrouvant une seconde jeunesse.

En plus de tout cela, Manjaro est **entièrement gratuit**. Contrairement à Windows ou macOS, vous n’avez rien à payer pour l’installer et en profiter pleinement. Enfin, elle offre une **sécurité renforcée** grâce à des mises à jour régulières et rapides, limitant ainsi l’exposition aux failles. Sa communauté active veille également à corriger rapidement les éventuels problèmes et à proposer des solutions efficaces.

## Découvrir Manjaro OS

Avant de vous lancer dans l’installation de Manjaro, il est important de savoir que cette distribution est disponible en plusieurs éditions. Chacune de ces éditions propose un environnement de bureau unique qui influence à la fois votre flux de travail et la consommation des ressources système. On distingue principalement trois éditions officielles de Manjaro.

![0_01](assets/fr/01.webp)

- L’édition **KDE Plasma** est la plus personnalisable. Si vous recherchez un système à la fois visuellement élégant et performant, KDE Plasma est un excellent choix. Cet environnement de bureau stable est idéal pour les utilisateurs qui souhaitent un contrôle total et une expérience sur mesure.

- Pour les machines disposant de ressources plus limitées, l’édition **Xfce** est la solution idéale. Son interface est légère et intuitive, garantissant une utilisation fluide même sur des ordinateurs plus anciens. De plus, sa disposition rappelle celle de Windows, ce qui facilite la transition vers Linux pour les nouveaux utilisateurs.

- Enfin, l’édition **GNOME** propose une approche totalement différente. Son design épuré met l’accent sur la productivité et l’organisation grâce aux espaces de travail virtuels. Ce flux de travail, centré sur les activités, séduit particulièrement les utilisateurs déjà familiers avec Linux et en quête d’un environnement minimaliste et très efficace.

### Autres éditions de Manjaro

![0_02](assets/fr/02.webp)

En plus des éditions officielles, la communauté Manjaro propose également d’autres versions. Ces éditions alternatives sont conçues pour répondre à des besoins spécifiques et offrent des environnements de bureau variés.

L’édition **Cinnamon** est un excellent choix si vous débutez et recherchez une interface familière. Elle a été pensée pour être simple d’utilisation tout en conservant les conventions classiques des environnements de bureau traditionnels.

Pour les utilisateurs plus avancés, on retrouve des éditions comme **i3 Window Manager** ou **Sway**. Beaucoup plus légères et rapides, elles demandent toutefois une bonne maîtrise de la ligne de commande pour être configurées et exploitées pleinement. Ces environnements conviennent parfaitement à ceux qui veulent un contrôle total sur leur système et qui privilégient l’efficacité avant tout.

## Spécifications techniques requises

Pour que Manjaro puisse fonctionner de manière optimale, votre ordinateur doit répondre à quelques exigences minimales. Nous vous conseillons d'avoir au moins :

- **Un processeur 64 bits (x86_64)**
- **4 Go de RAM recommandés (2 Go minimum)**
- **30 Go d’espace disque (plus si vous créez une partition `/home` dédiée)**

## Installation de Manjaro

Pour télécharger, rendez-vous sur [le site officiel de Manjaro](https://manjaro.org/) et choisissez l’édition qui correspond le mieux à vos besoins. Une fois le fichier téléchargé, il faudra créer une clé USB bootable avec l’image ISO de Manjaro.

Allez ensuite sur le site du logiciel [Rufus](https://rufus.ie/fr/) et téléchargez-le. Lancez le programme, branchez votre clé USB, sélectionnez l’image ISO de Manjaro et démarrez le flashage. Attendez la fin du processus avant de retirer la clé. Vous pouvez alors redémarrer votre ordinateur.

![0_03](assets/fr/03.webp)

Pour installer Manjaro sur votre ordinateur, commencez par l’éteindre complètement. Branchez ensuite la clé USB, rallumez la machine et accédez au menu de démarrage ou au firmware UEFI/BIOS en appuyant sur **F2, F10, F12, Échap** ou **Suppr** (selon le fabricant).

Choisissez ensuite la clé USB comme périphérique d’amorçage afin de démarrer le processus d’installation de l’OS.

### Écran de démarrage

La première fois que vous lancez Manjaro depuis la clé USB, vous arrivez directement sur le menu d’installation. Avant de lancer l’installation, vous avez la possibilité de changer la disposition du clavier ou la langue du système.

Choisissez ensuite l’option **Boot with open source drivers** pour démarrer l’installation de Manjaro. Ces pilotes libres sont compatibles avec la plupart des matériels et suffisent dans la majorité des cas. Si vous possédez une carte graphique NVIDIA par exemple ou que vous souhaitez de meilleures performances graphiques, vous pouvez choisir l’option **Boot with proprietary drivers**, qui utilise les pilotes propriétaires.

![0_04](assets/fr/04.webp)

Le système se lancera en **mode live par défaut**. Cela vous permet de tester les fonctionnalités de Manjaro afin de vérifier si elle correspond bien à vos besoins avant de l’installer définitivement. Une fois prêt, cliquez sur l’option **Installer Manjaro Linux**.

Sélectionnez la langue souhaitée pour votre installation, puis cliquez sur **Suivant**.

![0_06](assets/fr/06.webp)

Choisissez ensuite votre emplacement afin de configurer correctement le fuseau horaire. À cette étape, vous pouvez aussi modifier la langue et le format de la date.

![0_07](assets/fr/07.webp)

Sélectionnez la disposition du clavier. Un champ de test est disponible pour vérifier que les touches tapées correspondent bien aux caractères attendus.

![0_08](assets/fr/08.webp)

### Partitionnement du disque
Deux options s’offrent à vous pour le partitionnement du disque.

- La première, la plus simple, consiste à effacer tout le disque et installer Manjaro dessus.
- La seconde permet un **partitionnement manuel**.

![0_09](assets/fr/09.webp)

Pour une installation propre, il est recommandé de créer au moins trois partitions :

- Une première partition de **516 Mo** (primaire) pour le **boot**.
- Une seconde partition de **2 Go** (logique) pour le **swap**.
- Une troisième partition pour vos **données personnelles**.

Si vous souhaitez installer un autre système en parallèle, vous devez diviser cette dernière partition et n’allouer qu’une partie à Manjaro (au moins **15 Go** pour garantir le bon fonctionnement du système).
### Création d’un compte utilisateur

Créez un compte utilisateur sur le système en renseignant les informations demandées. Enfin, définissez le mot de passe de l’administrateur (**root**). Cet administrateur est un **super-utilisateur** disposant de tous les droits sur le système et capable d’exécuter des commandes avancées.

![0_10](assets/fr/10.webp)

### Choisissez la suite bureautique adéquate

Manjaro vous permet de choisir entre **LibreOffice** et **FreeOffice**.

- **LibreOffice** est plus complet, avec un plus grand nombre de logiciels et des fonctionnalités avancées.
- **FreeOffice**, quant à lui, est plus léger et inclut uniquement les logiciels essentiels : **TextMaker**, **PlanMaker** et **Presentations**.

![0_11](assets/fr/11.webp)

### Résumé de la configuration

Un écran récapitulatif vous présente l’ensemble des paramètres que vous avez définis. Vous pouvez revenir en arrière pour effectuer des modifications si nécessaire, sans impacter les autres réglages déjà effectués.

Cliquez ensuite sur **Installer**, puis confirmez pour lancer l’installation proprement dite.

![0_12](assets/fr/12.webp)

![0_13](assets/fr/13.webp)

### Fin de l’installation

À la fin du processus, cochez la case **Redémarrer maintenant**, puis sur **Fait**. Le système redémarrera et **Manjaro sera prêt à être utilisé**.

![0_13](assets/fr/14.webp)

## Premiers pas avec Manjaro

L’installation de Manjaro n’est que la première étape. Pour profiter pleinement de votre système, voici quelques actions utiles à connaître.

### Mettre à jour le système

Manjaro simplifie grandement les mises à jour. Pour mettre à jour vos paquets :

```shell
sudo pacman -Syu
```

Cette commande télécharge et installe les dernières versions disponibles. Il est conseillé de l’exécuter régulièrement pour garder votre système **sécurisé et stable**.

### Configurer un environnement de développement

Pour développer des applications Web sur Manjaro, installez en une seule commande les outils essentiels :

```shell
sudo pacman -S nodejs npm git yarn
```

Cette commande installe Node.js et npm pour exécuter et gérer vos projets JavaScript et TypeScript, Git pour la gestion de versions, et Yarn comme gestionnaire de packages alternatif.

### Installer un portefeuille Bitcoin

Pour gérer vos bitcoins sur Manjaro, vous pouvez installer **Electrum**, un portefeuille léger et sécurisé :

```shell
sudo pacman -S electrum  # Install Electrum
```

Electrum vous permet de **recevoir et envoyer des bitcoins** facilement, tout en offrant des fonctionnalités avancées comme la gestion de plusieurs portefeuilles et la protection par phrase de récupération. Pour un guide complet sur l’utilisation d’Electrum, consultez notre tutoriel dédié qui explique comment créer un portefeuille, sécuriser vos fonds et effectuer des transactions.

https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Sécurisation de votre système Manjaro

La sécurité est un aspect crucial de toute installation Linux. Il est important pour vous de protéger votre confidentialité et l'intégrité de vos données.

### Configuration du pare-feu

Manjaro inclut UFW (*Uncomplicated Firewall*), un programme de gestion des par-feux de filtre réseau, mais il faut l'activer manuellement :

```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```

![verbose](assets/fr/15.webp)

### Gestion des permissions utilisateur

1. **Création d'un utilisateur non-privilégié**

```shell
sudo useradd -m username
sudo passwd username
```

2. **Configuration du fichier sudoers**

```shell
sudo EDITOR=nano visudo
```

Vous voilà maintenant prêt à utiliser Manjaro Linux sur votre machine. Grâce à son **installation simple**, ses **mises à jour faciles**, et sa **flexibilité**, vous disposez d’un système puissant et performant, adapté à la fois au développement, à l’utilisation quotidienne et à la gestion de vos bitcoins avec des outils comme Electrum.

Manjaro allie **stabilité, rapidité et sécurité**, tout en restant **entièrement gratuit**, ce qui en fait un choix idéal pour les débutants comme pour les utilisateurs avancés. Prenez le temps d’explorer ses différentes fonctionnalités et personnaliser votre environnement pour qu’il corresponde parfaitement à vos besoins. Si vous souhaitez plus d'expertise et découvrir le système Arch Linux, notre tutoriel vous est fortement recommandé.

https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973