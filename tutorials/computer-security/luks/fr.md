---
name: LUKS
description: Chiffrer une clé USB avec LUKS et cryptsetup
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Mickael Dorigny publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

Chiffrer une clé USB est une bonne pratique pour protéger vos données sensibles. **Dans ce tutoriel, nous allons voir comment utiliser LUKS (*Linux Unified Key Setup*) avec cryptsetup pour chiffrer une clé USB sur un système Linux.** Cette méthode vous permettra de sécuriser vos données, notamment en cas de perte ou de vol de votre clé USB.

[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) est une norme de chiffrement de disque utilisée principalement sur les systèmes Linux. Il permet de sécuriser les données en chiffrant les partitions de disque avec des algorithmes robustes. Sa prise en charge sur les systèmes Linux facilite la gestion des clés de chiffrement et des mots de passe, offrant une interface standardisée et une compatibilité avec divers outils de gestion.

Pour suivre ce tutoriel, vous aurez besoin :

* d'une clé USB ;
* d'un système Linux avec "**cryptsetup**" installé (souvent disponible par défaut, sinon nous allons voir comment l'obtenir).

## II. Installation de cryptsetup

Dans un premier temps, nous devons nous assurer que nous disposons de la commande "**cryptsetup**" sur notre système :

```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```

Si vous n'obtenez aucune réponse à cette commande, c'est qu'il est nécessaire d'installer "**cryptsetup**" :

```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```

Nous avons maintenant tout le nécessaire pour créer notre clé USB chiffrée via LUKS.

En réalité, c'est l'utilitaire "**dm-crypt**" qui va faire le travail de chiffrement, "**cryptsetup**" est une interface en ligne de commande permettant de gérer les fonctionnalités et les actions de **dm-crypt**.

## III. Création de la partition LUKS et du système de fichier

### A. Identifier la clé USB

Nous allons à présent créer une partition LUKS chiffrée sur notre clé USB. Si celle-ci n'était pas encore branchée à votre système, c'est le moment de le faire.

Dans le cadre du tutoriel, je chiffre l'intégralité de ma clé USB, pas juste une partition. Il est également important de savoir que durant cette procédure, **toutes les données existantes seront effacées de la clé**.

La première étape consiste à repérer le fichier de périphérique correspondant à votre clé USB dans le répertoire "**/dev/**". Insérez votre clé USB et identifiez son nom de périphérique. Vous pouvez utiliser la commande suivante pour lister les périphériques de stockage :

```
$ lsblk
```

Repérez votre clé USB, par exemple "**/dev/sdb**". Vous pouvez également vous baser sur la commande "**fdisk -l**", pour afficher le nom du modèle de clé USB (il vaut mieux ne pas se tromper), aidez-vous notamment de la taille de stockage du périphérique comme indicateur :

![Image](assets/fr/019.webp)

Identification de la clé USB à chiffrer avec "**lsblk**" et "**fdisk**".

Dans mon exemple, ma clé USB est située dans "**/dev/sdb**". Si vous voyez apparaitre des "**/dev/sdb1**", "**/dev/sdb2**", etc. Il s'agit des partitions présentes actuellement sur votre clé. Elles seront supprimées par notre manipulation.

### B. Supprimer les données existantes

Nous allons à présent supprimer toutes les données sur notre clé USB, l'opération consiste à remplir l'espace disque de notre clé USB avec des 0.

**Assurez-vous de cibler le bon fichier de périphérique !**

```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```

Cela permet de s'assurer qu'il n'y aura pas de données en clair persistantes sur notre clé.

### C. Chiffrer la clé USB avec LUKS

À présent, nous allons initialiser la partition LUKS sur notre clé USB. Cette opération consiste à créer la partition LUKS :

```
# Formattage d'une partition LUKS sur la clé USB
$ sudo cryptsetup luksFormat /dev/sdb                                                                          

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type 'yes' in capital letters): YES
Enter passphrase for /dev/sdb: 
Verify passphrase: 
```

Ici, la sous-commande de "`luksFormat`" initialise et formate le périphérique pour utiliser le chiffrement LUKS. Vous serez invité à confirmer cette opération en tapant `YES` en majuscules, puis à définir une *passphrase*. **Choisissez une *passphrase* robuste** pour vous assurer qu'en cas de perte, l'attaquant ne puisse pas la découvrir via des attaques par brute force.

Après cela, le disque "**/dev/sdb**" sera formaté avec LUKS et prêt à être utilisé comme un volume chiffré.

### D. Formater le volume chiffré

Nous y sommes presque, il nous faut à présent créer une partition valide au sein de notre partition LUKS. De cette manière, une fois déverrouillée, nous pourrons l'utiliser comme n'importe quel système de fichier. Pour ce faire, il faut ouvrir la partition chiffrée :

```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1                                                                    
Enter passphrase for /dev/sdb: 

# Lister les disques 
$ sudo fdisk -l                                                                                                
[...]

Disk /dev/sdb: 7.72 GiB, 8294236160 bytes, 16199680 sectors
Disk model: Flash Disk      
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/usbkey1: 7.71 GiB, 8277458944 bytes, 16166912 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

Ici, "**usbkey1**" est le nom que je donne dans mon contexte au montage de la partition. Vous pouvez choisir celui qui vous convient. Nous devons ensuite formater cette partition contenue dans la partition LUKS, par exemple, ici en **ext4** :

```
# Formattage de la partition en ext4  
$ sudo mkfs.ext4 /dev/mapper/usbkey1  
  
mke2fs 1.47.0 (5-Feb-2023)  
Creating filesystem with 2020864 4k blocks and 505920 inodes  
Filesystem UUID: cfa607d3-c31f-475d-bcfe-fa951b60a591  
Superblock backups stored on blocks:   
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632  
  
Allocating group tables: done                              
Writing inode tables: done                              
Creating journal (16384 blocks):   
done  
Writing superblocks and filesystem accounting information:        
done
```

**Ici, on précise comme emplacement cible** "**/dev/mappe/usbkey1**"**, pourquoi ?**

"**/dev/mapper/usbkey1**" est le "raccourci" que nous avons donné à notre clé USB ("**/dev/mapper**"est générique à Linux pour le mappage). Il permet donc d'accéder à notre partition déchiffrée. Voici ce que vous êtes censés voir à présent :

```
# Liste des périphériques et leurs partition
$ lsblk                                                                                                        
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda         8:0    0  200G  0 disk  
├─sda1      8:1    0  199G  0 part  /
├─sda2      8:2    0    1K  0 part  
└─sda5      8:5    0  975M  0 part  [SWAP]
sdb         8:16   1  7.7G  0 disk  
└─usbkey1 254:0    0  7.7G  0 crypt 
sr0        11:0    1 1024M  0 rom 
```

## IV. Utiliser la clé USB chiffrée

### A. Ouvrir et monter le volume LUKS

**Via l'interface graphique** **:**

Sous Debian, "**dm-crypt**" est présent par défaut. Le montage se fait donc dans la plupart des cas directement au branchement de la clé USB. Il vous est alors demandé de saisir votre passphrase dans un pop-up telle que celle-ci :

![Image](assets/fr/018.webp)

Demande de saisie de la passaphrase de déchiffrement de la partition LUKS.

Une fois la passphrase saisie, votre système pourra lire le système de fichier se trouvant sur la clé et ensuite monter ce système de fichier, on verra alors notre partition montée :

```
$ lsblk                                                                                                        
NAME                                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                                           8:0    0  200G  0 disk  
├─sda1                                        8:1    0  199G  0 part  /
├─sda2                                        8:2    0    1K  0 part  
└─sda5                                        8:5    0  975M  0 part  [SWAP]
sdb                                           8:16   1  7.7G  0 disk  
└─luks-425f7800-e461-47e9-b8cc-f76d0cefb853 254:0    0  7.7G  0 crypt /media/mickael/cfa607d3-c31f-475d-bcfe-fa95
sr0                                          11:0    1 1024M  0 rom   
```

**En ligne de commande :**

Cependant, cela vaut le coup de savoir réaliser l'opération en ligne de commande. Commençons par déchiffrer la partition chiffrée à l'aide de "**crypsetup**" et de la sous-commande "**luksOpen**" :

```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1                                                                    
Enter passphrase for /dev/sdb: 

# Liste des périphériques et leurs partition
$ lsblk                                                                                                        
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
[...]
sdb         8:16   1  7.7G  0 disk  
└─usbkey1 254:0    0  7.7G  0 crypt 
sr0        11:0    1 1024M  0 rom   
```

À présent, le volume déchiffré de notre clé USB présente un volume que notre système de fichier et notre OS peuvent utiliser, nous allons donc monter son contenu dans un dossier quelconque, par exemple "**/home/mickael/mnt**" dans mon cas :

```
# Monter le volume déchiffré sur notre système de fichier
$ mkdir /home/mickael/mnt 
$ sudo mount /dev/mapper/usbkey1 /home/mickael/mnt                                                             

$ ls /home/mickael/mnt -al                                                                                     
total 24
drwxr-xr-x  3 root    root     4096 Jun 11 14:38 .
drwx------ 31 mickael mickael  4096 Jun 11 21:44 ..
drwx------  2 root    root    16384 Jun 11 14:38 lost+found

```

On pourra donc accéder aux données de notre clé USB librement et de façon transparente.

### B. Fermer et démonter le volume LUKS

Une fois notre opération terminée, il ne faut pas oublier de fermer tout cela proprement afin de s'assurer de ne pas corrompre notre volume. Il faut dans un premier temps démonter le montage du système de fichier :

```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```

Puis refermer la partition chiffrée elle-même :

```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```

À présent, quiconque utilisant notre clé USB ne verra rien de son contenu sauf des données chiffrées.

## V. Conclusion

Les interfaces graphiques rendent cette opération transparente, mais il est toujours utile de savoir formater, créer, ouvrir et fermer une partition chiffrée LUKS en ligne de commande. Les manipulations à réaliser une fois le formatage fait pour ouvrir et fermer une partition LUKS sont minimes au regard du gain en sécurité.
