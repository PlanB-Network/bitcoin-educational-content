---
name: VirtualBox
description: Installer VirtualBox sur Windows 11 et créer sa première VM
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian Burnel publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___


## I. Présentation

Dans ce tutoriel, nous allons apprendre à installer VirtualBox sur Windows 11 dans le but de créer des machines virtuelles, que ce soit pour faire tourner Windows 10, Windows 11, Windows Server ou une distribution Linux (Debian, Ubuntu, Kali Linux, etc.).

Ce tutoriel d'introduction à VirtualBox vous permettra de bien débuter avec cette solution de virtualisation open source développée par Oracle et qui est totalement gratuite. Par la suite, d'autres tutoriels seront mis en ligne pour approfondir le sujet.

Lorsqu'il s'agit d'effectuer de la virtualisation sur un poste de travail, notamment à des fins de tests dans le cadre d'un projet ou pendant ses études en informatique, VirtualBox est clairement une bonne solution. C'est également une alternative à d'autres solutions comme Hyper-V qui est intégré à Windows 10 et Windows 11 (ainsi qu'à Windows Server) et VMware Workstation (payant) / VMware Workstation Player (gratuit pour une utilisation personnelle).

Ma configuration : **un poste de travail sous Windows 11 où je vais installer VirtualBox**, mais vous pouvez installer VirtualBox sur Windows 10 (ou une version plus ancienne), ainsi que sur Linux. Concernant les machines virtuelles, VirtualBox prend en charge de nombreux systèmes, autant du Windows (exemple : Windows 10, Windows 11, Windows Server 2022, etc.), du Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), que du BSD (PfSense) ou encore macOS.

## II. Télécharger VirtualBox pour Windows 11

Pour télécharger VirtualBox dans le but de l'installer sur une machine Windows, il n'y a qu'une seule bonne adresse : le [site officiel de VirtualBox](https://www.virtualbox.org/wiki/Downloads) dans la section "**Downloads**". Il suffit de cliquer sur "Windows hosts" pour lancer le téléchargement de cet exécutable qui fait un peu plus de 100 Mo.

![Image](assets/fr/025.webp)

## III. Installer VirtualBox sur Windows 11

### A. Installation de VirtualBox

L'**installation de VirtualBox** s'effectue très simplement, et le processus est le même sur les différentes versions de Windows. Commencez par lancer l'exécutable de VirtualBox que l'on vient de télécharger, puis cliquez sur "**Suivant**".

![Image](assets/fr/026.webp)

Cette installation est personnalisable, mais je vous recommande d'installer toutes les fonctionnalités : ce qui est le cas avec la sélection par défaut. Au sein de l'image ci-dessous, on peut voir différents éléments, notamment :

- **VirtualBox USB Support** afin de permettre à VirtualBox de prendre en charge les périphériques USB
- **VirtualBox Bridged Network** afin d'intégrer la prise en charge du réseau en mode "Bridge" (la machine virtuelle peut se connecter à votre réseau local directement)
- **VirtualBox Host-Only Network** afin d'intégrer la prise en charge du réseau en mode "Host-Only" (la machine virtuelle peut communiquer uniquement avec votre hôte physique Windows 11 et les autres machines virtuelles dans ce mode)

Cliquez sur "**Suivant**" pour poursuivre.

![Image](assets/fr/001.webp)

Cliquez sur "**Oui**", tout en sachant que **le réseau sera interrompu un instant sur votre machine Windows 11**, le temps que VirtualBox effectue les modifications au niveau du réseau, dans le but de prendre en charge les différents types de réseau dont le mode "Bridge".

![Image](assets/fr/002.webp)

Dès que vous avez confirmé, l'installation démarre... Et une notification "**Voulez-vous installer ce logiciel de périphérique ?**" va apparaître. Cochez l'option "**Toujours faire confiance aux logiciels provenant de Oracle Corporation**" et cliquez sur "**Installer**". En fait, VirtualBox a besoin d'installer plusieurs pilotes sur votre ordinateur.

![Image](assets/fr/003.webp)

Voilà, l'installation est déjà terminée ! Cochez l'option "**Démarrer Oracle VM VirtualBox 6.1.34 après l'installation**" et cliquez sur "**Terminer**" afin que le logiciel se lance.

![Image](assets/fr/004.webp)

### B. Ajouter le pack d'extensions

Toujours sur le site officiel de VirtualBox (voir lien précédent), vous pouvez télécharger un pack d'extensions officiel, accessible sous la section "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" en cliquant sur le lien "**All supported platforms**". Ce pack va permettre d'ajouter des fonctionnalités supplémentaires à VirtualBox : ce n'est pas obligatoire de l'ajouter mais cela peut s'avérer utile ! Par exemple, cela intègre le support de l'USB 3.0 dans les VM, la prise en charge des webcams, mais aussi le chiffrement des disques.

Ouvrez VirtualBox, cliquez sur "**Fichier**" puis sur "**Paramètres**" dans le menu.

![Image](assets/fr/005.webp)

Cliquez sur "**Extensions**" à gauche (1), puis sur le bouton avec "**+**" sur la droite (2) afin de **charger le pack d'extensions VirtualBox** que vous venez de télécharger (3).

![Image](assets/fr/006.webp)

Confirmez en cliquant sur le bouton "**Installation**".

![Image](assets/fr/007.webp)

Cliquez sur "**OK**" : le pack d'extensions officiel est désormais installé sur votre instance VirtualBox !

![Image](assets/fr/008.webp)

Passons à la création de notre première machine virtuelle.

## IV. Créer sa première VM VirtualBox

Pour créer une nouvelle machine virtuelle sur VirtualBox, il suffit de cliquer sur le bouton "**Nouvelle**" afin de lancer l'assistant de création d'une VM. Puisqu'il s'agit du premier démarrage de VirtualBox, c'est l'occasion de vous donner quelques informations supplémentaires au sujet de l'interface et des autres boutons.

- **Paramètres** : configuration générale de VirtualBox (dossier par défaut des VMs, gestion des mises à jour, langue, réseaux NAT, extensions, etc.)
- **Importer** : importer une Appliance virtuelle, au format OVF
- **Exporter** : exporter une machine virtuelle existante au format OVF afin de créer une Appliance virtuelle
- **Ajouter** : ajouter à l'inventaire de votre VirtualBox une machine virtuelle existante, dans le format VirtualBox standard (.vbox) ou au format XML

Sur la gauche, la section "**Outils**" permet d'accéder à **des fonctions avancées notamment pour gérer la partie réseau virtuel, mais aussi pour gérer le stockage des VMs**. Sous l'entrée "**Outils**", vos machines virtuelles viendront s'ajouter par la suite.

![Image](assets/fr/009.webp)

### A. Processus de création d'une VM

**Débutons la création de la machine virtuelle.** Pour rappel, VirtualBox supporte une multitude de systèmes d'exploitation, aussi bien Windows, Linux que BSD. Dans cet exemple, je vais créer une machine virtuelle destinée à accueillir Windows 11. Plusieurs champs sont à renseigner :

- **Nom** : nom de la machine virtuelle (c'est le nom qui va s'afficher dans VirtualBox)
- **Dossier de la machine** : où stocker la machine virtuelle, tout en sachant qu'un sous-dossier avec le nom de la VM sera créé à cet emplacement
- **Type** : le type de système d'exploitation, en fonction de ce que vous souhaitez installer comme OS
- **Version** : la version du système que vous souhaitez installer, en l'occurrence Windows 11 pour ma part donc "**Windows11_64**"

Cliquez sur "**Suivant**" pour continuer.

![Image](assets/fr/010.webp)

En fonction du système d'exploitation que vous sélectionnez à l'étape précédente, **VirtualBox effectue des recommandations sur les ressources à attribuer à la machine virtuelle**. Ici, il s'agit de la mémoire vive, c'est-à-dire la RAM, que vous souhaitez affecter à la VM. Partons sur 4 Go, car effectivement c'est recommandé pour Windows 11, mais si vous manquez de ressources, indiquez plutôt 2 Go. **Poursuivez.**

**Note** : les ressources attribuées à la machine virtuelle sont modifiables par la suite.

![Image](assets/fr/011.webp)

En ce qui concerne le disque dur virtuel, nous partons de zéro donc il faut que l'on choisisse "**Créer un disque dur virtuel maintenant**" afin que la VM dispose d'un espace de stockage pour installer le système d'exploitation et stocker les données. Cliquez sur "**Créer**".

![Image](assets/fr/012.webp)

VirtualBox prend en charge trois formats différents pour les disques durs virtuels, ce qui est une différence majeure en comparaison d'autres solutions comme VMware et Hyper-V. Il y a le choix entre trois formats :

- **VDI** qui est le format officiel de VirtualBox
- **VHD** qui est le format officiel d'Hyper-V, même si l'on utilise plutôt le nouveau format VHDX de nos jours
- **VMDX** qui est le format officiel de VMware, que ce soit avec VMware Workstation ou VMware ESXi

Afin de créer une machine virtuelle qui sera utilisée uniquement sur cette instance VirtualBox, choisissez "**VDI**". Par contre, si le disque dur virtuel sera rattaché à un hôte Hyper-V par la suite, il peut être intéressant de partir sur le format VHD pour éviter de devoir le convertir. Cliquez sur "**Suivant**".

![Image](assets/fr/013.webp)

**Le disque virtuel peut être de taille dynamique ou de taille fixe.** Je m'explique. Lorsqu'il est de taille dynamique, le fichier qui représente **le disque virtuel (ici un fichier .vdi) va grossir au fur et à mesure que des données sont écrites dans le disque** jusqu'à atteindre sa taille maximale, mais il ne se réduira pas si l'on supprime des données. A l'inverse, lorsqu'il est de taille fixe, **l'espace de stockage total est alloué immédiatement (et donc réservé)**, ce qui permet d'avoir des performances un peu plus élevées mais c'est plus long lors de la création initiale du disque virtuel.

Personnellement, pour des machines virtuelles de test avec VirtualBox, j'estime que le mode "**Dynamiquement alloué**" est suffisant.

![Image](assets/fr/014.webp)

**L'étape suivante consiste à indiquer la taille du disque virtuel**, en sachant que par défaut, le disque sera stocké dans le répertoire de la VM (c'est modifiable lors de cette étape). J'indique une taille de 64 Go afin de respecter les prérequis de Windows 11, mais là encore, on pourrait attribuer une taille inférieure. Cliquez sur "**Créer**" pour créer la VM !

![Image](assets/fr/015.webp)

A cet instant, la VM est dans notre inventaire, elle est configurée, mais le système d'exploitation n'est pas installé. Nous devons finaliser la configuration de la VM avant de la démarrer.

### B. Attribuer une image ISO à une VM VirtualBox

Pour installer Windows 11, ou un autre système, nous avons besoin de sources d'installation. Dans la majorité des cas, on utilise une image disque au format ISO pour installer un système d'exploitation. **Il est nécessaire que l'on charge l'image ISO de Windows 11 dans le lecteur DVD virtuel de notre VM.**

Cliquez sur la VM dans l'inventaire VirtualBox (1) puis sur le bouton "**Configuration**" (2) qui donne accès à la configuration générale de cette machine virtuelle. C'est par l'intermédiaire de ce menu que l'on gère les ressources (par exemple : augmenter la RAM, configurer le processeur, etc.). Cliquez sur "**Stockage**" à gauche (3), sur le lecteur DVD où c'est indiqué "**Vide**" pour le moment (4) puis cliquez sur l'icône en forme de DVD (5) et "**Choose a disk file**".

![Image](assets/fr/016.webp)

Sélectionnez l'image ISO du système d'exploitation que vous souhaitez installer puis validez. Voici ce que j'obtiens :

![Image](assets/fr/017.webp)

Restez dans la section "**Configuration**" de la VM, j'ai encore deux trois petites choses à vous expliquer.

### C. Connexion au réseau de la VM

Accédez à la section "**Réseau**" sur la gauche. Cette section permet de gérer le réseau de la machine virtuelle : nombre d'interfaces réseau virtuelles (jusqu'à 4 par VM), adresse MAC, ainsi que le mode d'accès réseau (NAT, accès par pont (bridge), réseau interne, etc...). **Si vous souhaitez que votre machine virtuelle ait accès à Internet, sélectionnez "NAT" ou "Accès par pont"** mais ce second mode nécessite qu'un serveur DHCP soit actif sur votre réseau ou alors il faudra configurer manuellement une adresse IP.

Note : Je vais revenir plus en détails sur la partie réseau dans un article dédié.

![Image](assets/fr/018.webp)

### D. Le nombre de processeurs virtuels

Comme un ordinateur physique, la machine virtuelle a besoin de mémoire vive, d'un disque dur et d'un processeur pour fonctionner. Lorsque nous avons créé la VM, vous avez peut être remarqué que l'assistant n'intégrait pas la configuration du processeur. Cependant, c'est bien configurable, à tout moment via l'onglet "**Système**" puis "**Processeur**" où il est possible de choisir le nombre de processeurs virtuels.

Note : l'option "**Activer VT-x/AMD-v imbriqué**" est nécessaire pour réaliser de la virtualisation imbriquée.

Dans mon cas, la machine virtuelle dispose de 2 processeurs virtuels :

![Image](assets/fr/019.webp)

**Validez puisque la machine virtuelle est prête !** N'hésitez pas à jeter un coup d'oeil aux autres sections du menu de configuration.

### E. Premier démarrage et installation de l'OS

Pour démarrer une machine virtuelle, il suffit de la sélectionner dans l'inventaire puis de cliquer sur le bouton "**Démarrer**". Une seconde fenêtre va s'ouvrir afin de donner un visuel sur la VM.

![Image](assets/fr/020.webp)

Aïe, j'obtiens une vilaine erreur et ma machine virtuelle ne souhaite pas démarrer ! L'erreur est "Echec de l'ouverture de session pour la machine virtuelle..." avec les détails suivants :

```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```

En fait, c'est normal car **la fonctionnalité permettant de faire de la virtualisation n'est pas activée sur mon ordinateur** ! Pour corriger ce problème, il est nécessaire de redémarrer l'ordinateur pour accéder au BIOS et activer la virtualisation.

![Image](assets/fr/021.webp)

Sans attendre, je redémarre mon ordinateur et **j'appuie sur la touche "SUPPR" pour accéder au BIOS** (la touche peut varier en fonction des machines, et cela peut être F2, par exemple) de ma carte mère ASUS . Pour activer la virtualisation, le "Mode SVM" doit être activé dans mon cas. Là encore, d'une carte mère à une autre, d'un fabricant à un autre, le nom peut changer. Recherchez une fonction faisant référence à **AMD-V** (pour un CPU AMD) ou **Intel VT-x** (pour un CPU Intel).

![Image](assets/fr/022.webp)

Dès que c'est fait, il faut sauvegarder la modification et relancer la machine physique... Cette fois-ci, **VirtualBox peut démarrer la machine virtuelle** et charger l'image ISO de Windows afin d'installer le système d'exploitation ! 🙂

![Image](assets/fr/023.webp)

Sur notre hôte physique Windows 11, où est installé VirtualBox, on peut voir que le dossier de la machine virtuelle Windows 11 contient différents fichiers.

- **Le fichier VBOX** (au format XML) qui correspond à la configuration de la VM (RAM, CPU, etc.)
- **Le fichier VBOX-PREV** qui est une sauvegarde de la configuration précédente
- **Le fichier VDI** correspondant au disque dur virtuel en mode dynamique, donc actuellement il fait seulement 13 Go alors que sa taille maximale est de 64 Go
- **Le fichier NVRAM** contient l'état du BIOS de la machine virtuelle, ce qui est un équivalent à la mémoire non volatile d'une machine physique

![Image](assets/fr/024.webp)

## V. Conclusion

**Voilà, VirtualBox est mis en place sur notre machine physique Windows 11 ! Il ne reste plus qu'à en profiter et créer des machines virtuelles !** Je vais revenir sur l'installation de Windows 11 dans une VM VirtualBox au sein d'un autre article. Pour Windows 10, Windows Server ou une distribution Linux (Ubuntu, Debian, etc...), il suffit de se laisser guider !