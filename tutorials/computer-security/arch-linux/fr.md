---
name: Arch Linux
description: Une distribution minimaliste et performante, conçue selon la philosophie KISS.
---

![cover](assets/cover.webp)

Arch Linux est une distribution reconnue pour sa robustesse, ses performances et son adaptabilité, notamment pour des objectifs de développement. Elle offre une excellente stabilité et un environnement propice à la personnalisation, le tout porté par un gestionnaire de paquets extrêmement rapide et fiable. Sa philosophie repose sur le principe du **KISS** (*Keep It Simple, Stupid*) : proposer une distribution légère, simple, rapide et épurée, tout en laissant une grande liberté à l’utilisateur.

## Pourquoi choisir Arch Linux ?

- **Libre et gratuit** : Comme la plupart des distributions Linux, Arch Linux est totalement gratuite. Aucun frais de licence à prévoir, ce qui en fait un excellent choix pour les étudiants, les indépendants ou les passionnés.
- **Philosophie KISS** : Arch est conçue pour rester simple, légère et efficace. Elle fournit uniquement l’essentiel, ce qui vous permet de construire votre environnement à la carte.
- **Gestionnaire de paquets Pacman** : Pacman est un gestionnaire de paquets rapide, fiable et très bien conçu. Il permet une installation et une mise à jour efficace des logiciels, et gère les dépendances avec précision.
- **Documentation complète et communauté active** : l’[Arch Wiki](https://wiki.archlinux.org) est probablement l’une des meilleures documentations techniques de l’univers Linux. Il s'agit d'une mine d’or pour comprendre ce que vous faites. La communauté, composée en majorité de profils expérimentés, est très active et peut vous aider en cas de blocage, à condition que vous ayez cherché un minimum au préalable.

## Installation et configuration

### Prérequis

Matériel nécessaire :

- Une clé USB d’au moins **8 Go**
- **2 Go** de RAM minimum
- Un ordinateur avec au moins 20 Go d’espace disque disponible

### Téléchargement

![0_1](assets/fr/01.webp)

Depuis 2017, Arch Linux ne prend plus en charge les architectures 32 bits. Seules les versions 64 bits sont disponibles.

- Rendez-vous sur [le site officiel](https://mir.archlinux.fr/iso/latest/) pour télécharger la dernière version officielle de l’image ISO.

### Créer une clé bootable

Pour créer une clé USB bootable, vous pouvez utiliser un outil comme **Balena Etcher** :

- Téléchargez Balena Etcher sur le [site officiel](https://etcher.balena.io).
- Lancez le logiciel, sélectionnez l’image ISO d’Arch Linux.
- Choisissez votre clé USB comme périphérique cible.
- Cliquez sur **Flash** pour lancer la création de la clé bootable.

![0_2](assets/fr/02.webp)

## Installation de Arch Linux

## Démarrage sur la clé USB

- Éteignez complètement votre ordinateur
- Branchez la clé USB bootable
- Redémarrez et entrez dans le BIOS/UEFI en appuyant sur **F1**, **Échap**, **F9**, etc. (selon votre modèle)
- Dans le menu de démarrage, choisissez la clé USB comme périphérique d’amorçage. Si tout est bien configuré, vous arriverez sur l’interface de démarrage d’Arch Linux.

## Lancement de l’installation

Sur l'écran de démarrage, choisissez la première option pour lancer l'installation. Notez que Arch linux ne propose pas d’installateur graphique. Une fois lancé, vous arriverez sur un terminal en mode root.

![0_3](assets/fr/03.webp)

![0_4](assets/fr/04.webp)

![0_5](assets/fr/05.webp)

### Configuration du clavier

Vous pouvez afficher les dispositions disponibles avec :

```shell
localectl list-keymaps
```

![0_6](assets/fr/06.webp)

Puis charger une disposition avec :

```shell
loadkeys nom-disposition
```

Par défaut, le clavier est en anglais (qwerty), mais vous pouvez passer en `azerty` avec `loadkeys fr`.

### Configuration de la date et de l’heure

Arch Linux utilise l’outil `timedatectl` pour gérer l’horloge système.

![0_7](assets/fr/07.webp)

- Définissez votre fuseau horaire avec :
```shell
timedatectl set-timezone Europe/Paris
```

- Vérifiez que la synchronisation automatique est activée avec :
```shell
timedatectl status
```

- Activez-la si besoin :
```shell
timedatectl set-ntp true
```


Cela active NTP, le protocole de synchronisation automatique avec les serveurs de temps. Cette étape est importante pour éviter des erreurs de date lors de l’installation des paquets ou de la configuration des certificats SSL plus tard.

### Partitionnement du disque

- Vérifiez si votre système démarre en **UEFI** ou **BIOS** avec :

```shell
ls /sys/firmware/efi
```

Si le dossier existe, vous êtes en **UEFI**. Sinon, vous êtes en **BIOS (Legacy)**.
- Listez les disques disponibles :
```shell
lsblk
```

![0_8](assets/fr/08.webp)

- Lancez le gestionnaire de partition :

```shell
cfdisk /dev/nom-du-disque
```

Choisissez **GPT** si vous êtes en UEFI, **DOS** si vous êtes en BIOS.

![0_9](assets/fr/09.webp)

#### Partitions à créer
- **En UEFI**

| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- **En BIOS**

| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)

Sélectionnez **Write**, tapez **yes**, puis **Quit**.

### Formatage des partitions

- **UEFI** :

```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```

- **BIOS** :

```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```

![0_11](assets/fr/11.webp)

### Installation du système de base

Montez la partition **root** :

- Sur le BIOS :
```shell
mount /dev/sda2 /mnt
```
- sur UEFI :
```shell
mount /dev/sda3 /mnt
```

Puis installez les paquets essentiels :

```shell
pacstrap -K /mnt base linux linux-firmware
```

![0_12](assets/fr/12.webp)

Générez le fichier **fstab** qui permet au système d'exploitation de gérer automatiquement le montage des partitions à chaque démarrage, sans intervention manuelle :

```shell
genfstab -U /mnt >> /mnt/etc/fstab
```

Entrez dans l’environnement **Chroot** :

```shell
arch-chroot /mnt
```

![0_13](assets/fr/13.webp)

### Configuration système

- Installez un éditeur de texte pour modifier les fichiers de configuration :

```shell
pacman -S vim
```

- Configurez la langue :
Éditez `/etc/locale.gen` puis décommentez la ligne`en_US.UTF-8 UTF-8`

![0_14](assets/fr/14.webp)

- Définissez le nom de la machine :

```shell
echo nom_machine > /etc/hostname
```

- Définissez le mot de passe root :

```shell
passwd
```

![0_15](assets/fr/15.webp)

### Installation de GRUB

Installez le paquet :

```shell
pacman -S grub
```

![0_16](assets/fr/16.webp)

Une fois télécharger vous devez l'installer en fonction du format de partition du disque.
- Pour **BIOS** :

```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

![0_17](assets/fr/17.webp)

- Pour **UEFI** :

```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

### Finalisation

- Quittez l’environnement chroot :
```shell
exit
```

- Démontez les partitions :
```shell
umount -R /mnt
```

- Redémarrez :
```shell
reboot
```

Au démarrage, connectez vous avez le login **root** et le mot de passe défini.  

![0_18](assets/fr/18.webp)
## Connexion réseau après redémarrage

Il se peut qu’au redémarrage, aucune connexion réseau ne soit active. Vous pouvez lister les interfaces avec :

```shell
ip link
```

Configurez ensuite l'interface réseau en entrant le texte suivant dans le terminal

```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```

## Interface graphique (GNOME)

Par défaut, **Arch Linux** ne contient aucune interface graphique. Pour en ajouter une :

Mettez à jour le système :

```shell
pacman -Syu
```

Installez **Xorg** avec la commande suivante et faites entré à chaque fois pour conserver les choix par défaut:

```shell
pacman -S xorg
```

![0_19](assets/fr/19.webp)

Installez **GNOME** avec la commande suivante et faites entré à chaque fois pour conserver les choix par défaut :

```shell
pacman -S gnome gnome-extra
```

![0_20](assets/fr/20.webp)

Activez le **gestionnaire de session** :

```shell
systemctl enable gdm
systemctl start gdm
```

Le système se relance automatiquement et vous avez l'interface de connexion graphique. Connectez-vous avec l'utilisateur root et son mot passe. 

![0_21](assets/fr/21.webp)

## Création d’un utilisateur

Une fois dans l'**interface GNOME**, vous devez créer un nouvel utilisateur pour plus de sécurité ainsi qu’une utilisation plus sûre et sans risque. Entrez dans les applications et choisissez l’option “console” pour lancer le terminal. 

- Ajoutez un utilisateur :

```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```

![0_22](assets/fr/22.webp)
 
- Installez **sudo** :
```shell
pacman -S sudo
```

- Activez les droits **sudo** :

```shell
EDITOR=nano visudo
```

- Puis décommentez la ligne :

```shell
%wheel ALL=(ALL:ALL) ALL
```

- Redémarrez le système et connectez-vous avec votre utilisateur.

![0_23](assets/fr/23.webp)

![0_24](assets/fr/24.webp)

## Installer des logiciels

Arch Linux étant minimaliste, beaucoup de logiciels ne sont pas installés par défaut. Pour ajouter ce dont vous avez besoin tapez la commande suivante:

```shell
pacman -S nom_du_paquet_a_installe
```

Par exemple, pour installer l’éditeur de texte **nano**, vous pouvez taper :

```shell
pacman -S nano
```

Pour installer un navigateur web léger comme `firefox`, utilisez :

```shell
pacman -S firefox
```

Enfin, si vous souhaitez ajouter des outils réseau essentiels comme `net-tools`, la commande sera :

```shell
pacman -S net-tools
```

N’oubliez pas que vous pouvez installer plusieurs paquets en une seule commande en les listant séparément :

```shell
pacman -S vim firefox net-tools
```

Arch Linux se distingue par sa stabilité remarquable, sa philosophie minimaliste et sa robustesse, ce qui en fait un choix idéal pour les environnements de développement. En fournissant uniquement l’essentiel, elle offre une base légère et performante, facile à personnaliser selon vos besoins spécifiques. Cette approche minimaliste favorise également une meilleure maîtrise du système, renforçant ainsi la sécurité en limitant la surface d’attaque. Grâce à sa communauté active et sa documentation exhaustive, Arch Linux vous accompagne efficacement dans la création d’un environnement sécurisé, flexible et optimisé pour le développement professionnel.

Si vous avez apprécié débuter avec Arch Linux, vous aimerez notre tutoriel sur **Fedora OS**, un système d'exploitation modulaire, sécurisé et robuste qui s'adapte à vos besoins et usages.

https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1