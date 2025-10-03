---
name: Debian
description: Une distribution Linux réputée pour sa stabilité, sa robustesse et sa grande compatibilité.
---
 
![cover](assets/cover.webp)
 
Debian est une distribution GNU/Linux libre, reconnue pour sa robustesse et sa fiabilité. Son noyau Linux et l’ensemble de ses paquets font l’objet de tests rigoureux afin d’assurer une stabilité à toute épreuve et un niveau de sécurité élevé. Adaptée tant aux serveurs qu’aux postes de travail, Debian offre une expérience simple tout en proposant un vaste catalogue de logiciels. Que vous recherchiez un système sûr pour un usage quotidien ou un environnement de production, Debian constitue un choix judicieux.
 
## Pourquoi choisir Debian ?
 
- **Libre et gratuit** : Debian est entièrement open source, garantissant transparence et absence de frais de licence.
- **Stabilité et sécurité** : chaque version passe par un processus de tests approfondis, faisant de Debian l’une des distributions les plus fiables et sécurisées.
- **Communauté active** : une vaste communauté et une documentation exhaustive sont disponibles pour vous accompagner en cas de besoin.
- **Léger et modulable** : vous pouvez installer Debian sur des machines aux ressources modestes tout en conservant de bonnes performances.
- **Large catalogue de logiciels** : plus de 50 000 paquets officiels sont accessibles via les dépôts.
 
## Choisir une interface graphique
 
Debian propose plusieurs environnements de bureau selon vos besoins :
 
- **GNOME** : interface moderne et intuitive, idéale pour les débutants. Elle offre un menu graphique fluide et simple pour accéder aux applications.
- **XFCE** : légère et rapide, parfaite pour les machines moins puissantes.
- **KDE Plasma** : très personnalisable, avec une apparence proche de Windows.
- **Cinnamon** : interface élégante et simple, inspirée de Windows.
- **LXDE / LXQt** : ultralégères, adaptées aux anciens ordinateurs.
- **MATE** : simple et classique, proche de l’ancien GNOME.
 
💡 Pour une expérience confortable et facile à prendre en main, **GNOME est fortement recommandé**.
 
## Installation et configuration de Debian
### Prérequis matériels
 
Avant de lancer l’installation, veillez à disposer du matériel suivant :
 
- **Clé USB** : 8 Go minimum pour y placer l’image ISO bootable.
- **Mémoire vive (RAM)** : 4 Go pour garantir une installation et un fonctionnement fluide.
- **Espace disque** : au moins 15 Go d’espace libre pour accueillir le système et les mises à jour.
 
### Téléchargement
 
Le choix de l’image Debian dépend de l’architecture de votre processeur :
 
- **AMD64** : téléchargez l’édition “live hybrid” depuis la liste de [téléchargement](https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- **ARM64** : récupérez l’image DVD à partir sur le site officiel de [Debian](https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- **Autres architectures** : trouvez l’ISO correspondant à votre architecture [ici](https://debian.obspm.fr/debian-cd/12.11.0/).
 
![download](assets/fr/01.webp)
 
### Création de la clé USB bootable
 
Une fois l’image ISO adéquate téléchargée, procédez à la création de votre média d’installation :
-  **Téléchargez Balena Etcher** sur le [site officiel](https://etcher.balena.io/) puis récupérez le binaire pour votre système et installez-le.
 
![etcher](assets/fr/02.webp)
 
- **Lancez Etcher** : ouvrez le logiciel et sélectionnez l’image ISO de Debian précédemment téléchargée.
- **Choisissez la clé USB** : indiquez votre clé (8 Go+) comme cible.
- **Démarrez le flash** : cliquez sur **Flash!** et patientez jusqu’à la fin du processus.
 
![flash](assets/fr/03.webp)
 
Votre clé USB est maintenant prête à démarrer l’installation de Debian.
 
## Installation de Debian sur votre système

### Démarrage sur la clé USB

Pour lancer l’installation depuis votre clé USB :
- **Éteignez** complètement l’ordinateur.
- **Redémarrez** puis accédez au BIOS/UEFI en appuyant immédiatement sur `ESC`, `F2`, `F11` (ou la touche dédiée selon votre marque).
- Dans le menu de démarrage, **sélectionnez votre clé USB** comme périphérique d’amorçage.
- **Validez** avec la touche Entrée pour démarrer sur l’image Debian : vous arriverez alors sur l’écran d’accueil de l’installateur.
 
### Lancement de l'installation

Ecran de démarrage :
 
![starting](assets/fr/04.webp)
 
Au démarrage depuis la clé USB, l’écran d’accueil de Debian propose plusieurs options :
- **Live System** : lance Debian sans l’installer, idéal pour tester l’environnement.
- **Start Installer** : démarre directement l’installation sur le disque dur.
- **Advanced Install Options** : vous donne accès à des modes d’installation personnalisés.

Pour explorer Debian en mode live, choisissez **Live System** et validez avec **Entrée**. Vous pouvez ensuite lancer l’installation en cliquant sur **Install Debian** dans l’environnement live.

![system](assets/fr/05.webp)
 
- **Sélection de la langue**

Sélectionnez la langue principale de votre système Debian dans la liste proposée, puis validez.
 
![language](assets/fr/06.webp)
 
- **Fuseau horaire**

Choisissez votre zone géographique pour configurer automatiquement la date et l’heure.
 
![timezone](assets/fr/07.webp)
 
- **Disposition du clavier**

Sélectionnez la langue de votre clavier et la disposition correspondante. Utilisez le champ de test intégré pour vérifier que chaque touche produit le caractère attendu.
 
![keyboard](assets/fr/08.webp)
 
### Partitionnement du disque
 
- **Effacer le disque** : si vous disposez d’une partition dédiée, cette option supprimera tout son contenu.
- **Partitionnement manuel** : choisissez cette option pour créer, redimensionner ou supprimer des partitions selon vos besoins.
 
![disk](assets/fr/09.webp)
 
- **Création du compte utilisateur**

Indiquez votre nom complet, le nom de votre compte et un mot de passe fort pour garantir la protection de votre session.
 
![user](assets/fr/10.webp)
 
- **Résumé des paramètres**

Un récapitulatif de vos choix s’affiche : vérifiez chaque élément et revenez en arrière pour modifier si nécessaire.
 
![settings](assets/fr/11.webp)
 
- **Lancement de l’installation**

Cliquez sur **Installer** pour démarrer la copie des fichiers et la configuration du système puis patientez jusqu’à la fin du processus.
 
![install](assets/fr/12.webp)
 
- **Redémarrage**

Une fois l’installation terminée, redémarrez l’ordinateur pour appliquer toutes les configurations et accéder à votre nouveau système Debian.
 
![restart](assets/fr/13.webp)
 
Au démarrage, entrez le nom d’utilisateur ainsi que le mot de passe pour accéder au système.
 
![login](assets/fr/14.webp)
 
## Mise à jour du système
 
Avant de commencer à utiliser votre système, il est essentiel de le mettre à jour. Cela permet de bénéficier des derniers correctifs logiciels, des dépôts à jour, et dans certains cas, des correctifs de sécurité pour le système d'exploitation lui-même.
 
### Option 1 : Mise à jour via l’interface graphique (GNOME)
 
Si vous avez installé Debian avec l’environnement de bureau GNOME, vous pouvez effectuer les mises à jour graphiquement. Pour cela, ouvrez l’application **Logiciels**, puis allez dans l’onglet **Mises à jour**. Cliquez ensuite sur **Redémarrage et mise à jour** pour lancer le processus.
 
### Option 2 : Mise à jour via le terminal (recommandée)
 
Cette méthode offre un contrôle plus complet. Elle permet de mettre à jour les dépôts, les paquets logiciels, ainsi que le noyau si nécessaire.
- Ouvrez le terminal à l’aide du raccourci `Ctrl + Alt + T`.
- Mettez à jour la liste des paquets disponibles avec la commande suivante :

```shell
sudo apt update
```
  
  Entrez votre mot de passe lorsque demandé (notez qu’aucun caractère ne s'affichera lors de la saisie, c’est normal).
  
- Pour installer les mises à jour disponibles :
 
```shell    
sudo apt full-upgrade
```

## Découvrez les tâches de base
 
### Naviguer sur Internet
 
Le navigateur web par défaut sur Debian est **Firefox**. Si vous préférez un autre navigateur, vous pouvez en installer un autre, à condition qu’il soit disponible dans les dépôts Debian (comme Chromium, Brave...).

### Faire du traitement de texte
 
La suite **LibreOffice** est installée par défaut sur Debian.
 
- Pour rédiger des documents, utilisez **LibreOffice Writer**, l’équivalent de Microsoft Word.
- Pour les feuilles de calcul, **LibreOffice Calc** fait office d’alternative à Excel.
- Enfin, **LibreOffice Impress** vous permet de créer des présentations, comme avec PowerPoint.
 
## Installer des applications
 
Il existe deux méthodes pour installer des applications sur Debian :
 
### Méthode graphique :
 
Vous pouvez utiliser le **gestionnaire de logiciels** (accessible via l’interface graphique) pour rechercher et installer facilement des applications.

### Méthode en ligne de commande :
 
Si l'application que vous cherchez n'apparaît pas dans l'interface graphique, ou si vous préférez le terminal, utilisez la commande suivante :
 
```shell
sudo apt install <name>
```

Remplacez `<name>` par le nom du paquet. Par exemple, pour installer `curl` :

```shell
sudo apt install curl
```

### Installer un paquet téléchargé manuellement :
 
Si vous avez téléchargé un fichier `.deb` (paquet Debian), vous pouvez l’installer avec la commande suivante :
 
```shell
sudo apt install ./name.deb
```
 
https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af
 
Votre système Debian est maintenant installé et prêt à être utilisé pour vos tâches quotidiennes.  
Grâce à l’environnement de bureau **GNOME**, vous avez accès à de nombreuses applications accessibles via une interface graphique conviviale, idéale pour les débutants comme pour les utilisateurs avancés.
 
Sachez également qu’il est possible de changer d’environnement de bureau (par exemple passer à XFCE, KDE, etc.) sans avoir à réinstaller Debian. Pour cela, il suffit d’utiliser le terminal et d’installer le nouvel environnement de votre choix.
 
Pour approfondir vos connaissances sur Debian, et plus largement sur les distributions GNU/Linux, je vous recommande de consulter ce cours :

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1


