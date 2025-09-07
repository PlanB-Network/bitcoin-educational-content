---
name: LUKS
description: Een USB flash drive versleutelen met LUKS en cryptsetup
---
![cover](assets/cover.webp)



___



*Deze tutorial is gebaseerd op originele inhoud van Mickael Dorigny gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



Het versleutelen van een USB-stick is een goede manier om je gevoelige gegevens te beschermen. **In deze tutorial bekijken we hoe je LUKS (*Linux Unified Key Setup*) met cryptsetup kunt gebruiken om een USB-stick te versleutelen op een Linux-systeem.** Met deze methode kun je je gegevens beveiligen, vooral in het geval van verlies of diefstal van je USB-stick.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) is een standaard voor schijfversleuteling die voornamelijk wordt gebruikt op Linux-systemen. Het beveiligt gegevens door schijfpartities te versleutelen met robuuste algoritmen. De ondersteuning ervan op Linux-systemen vergemakkelijkt het beheer van encryptiesleutels en wachtwoorden en biedt gestandaardiseerde Interface en compatibiliteit met verschillende beheertools.



Om deze tutorial te volgen, heb je nodig:





- uSB-sleutel;
- een Linux systeem met "**cryptsetup**" geïnstalleerd (vaak standaard beschikbaar, anders zullen we zien hoe je het krijgt).



## II. Cryptsetup installeren



Eerst moeten we ervoor zorgen dat we het "**cryptsetup**" commando op ons systeem hebben:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Als je geen antwoord krijgt op dit commando, moet je "**cryptsetup**" installeren:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



We hebben nu alles wat we nodig hebben om onze versleutelde USB-sleutel via LUKS te maken.



In werkelijkheid is het de "**dm-crypt**" utility die het versleutelingswerk doet. "**cryptsetup**" is een opdrachtregel Interface die de functies en acties van **dm-crypt** beheert.



## III. De LUKS-partitie en het bestandssysteem aanmaken



### A. De USB-stekker identificeren



We gaan nu een versleutelde LUKS-partitie aanmaken op onze USB-stick. Als je hem nog niet op je systeem hebt aangesloten, is het nu tijd om dat te doen.



In deze tutorial versleutel ik mijn hele USB-stick, niet slechts één partitie. Het is ook belangrijk om te weten dat tijdens deze procedure **alle bestaande gegevens worden gewist van de sleutel**.



De eerste stap is het vinden van het apparaatbestand dat overeenkomt met uw USB-stick in de map "**/dev/**". Plaats uw USB-stick en identificeer de apparaatnaam. U kunt het volgende commando gebruiken om een lijst van opslagapparaten te maken:



```
$ lsblk
```



Zoek je USB-sleutel, bijvoorbeeld "**/dev/sdb**". Je kunt ook de opdracht "**fdisk -l**" gebruiken om de naam van het model van de USB-sleutel weer te geven (vergis je niet) en de opslaggrootte van het apparaat als indicator te gebruiken:



![Image](assets/fr/019.webp)



Identificeer de USB-sleutel die moet worden versleuteld met "**lsblk**" en "**fdisk**".



In mijn voorbeeld bevindt mijn USB-sleutel zich in "**/dev/sdb**". Als u "**/dev/sdb1**", "**/dev/sdb2**", enz. ziet, dan zijn dat de partities die momenteel op uw schijf staan. Dit zijn de partities die momenteel aanwezig zijn op je sleutel. Ze zullen worden verwijderd door onze manipulatie.



### B. Bestaande gegevens verwijderen



We gaan nu alle gegevens op onze USB-stick verwijderen. De operatie bestaat uit het vullen van de schijfruimte op onze USB-stick met 0-en.



**Zorg ervoor dat je je richt op het juiste apparaatbestand!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Dit zorgt ervoor dat er geen hardnekkige platte tekst gegevens op onze sleutel staan.



### C. De USB-sleutel coderen met LUKS



We gaan nu de LUKS-partitie op onze USB-sleutel initialiseren. Hiervoor moet de LUKS-partitie worden gemaakt:



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



Hier initialiseert en formatteert het `luksFormat` subcommando het apparaat om LUKS encryptie te gebruiken. Je wordt gevraagd om deze operatie te bevestigen door `YES` in hoofdletters te typen, definieer dan een *passphrase*. **Kies een robuuste *passphrase* om er zeker van te zijn dat, in het geval van verlies, de aanvaller het niet kan ontdekken via brute-force aanvallen.



Hierna zal de "**/dev/sdb**" schijf geformatteerd zijn met LUKS en klaar zijn om gebruikt te worden als een versleuteld volume.



### D. Versleuteld volume formatteren



We zijn er bijna en nu moeten we een geldige partitie aanmaken binnen onze LUKS-partitie. Op deze manier kunnen we het, eenmaal ontgrendeld, gebruiken zoals elk ander bestandssysteem. Om dit te doen, moeten we de versleutelde partitie openen:



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



Hier is "**usbkey1**" de naam die ik geef aan de partitie mount in mijn context. Je kunt zelf kiezen wat je wilt. Vervolgens moeten we deze partitie in de LUKS-partitie formatteren, bijvoorbeeld hier als **ext4**:



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



**Hier is de doellocatie** opgegeven als "**/dev/mappe/usbkey1**"**, waarom?



"**/dev/mapper/usbkey1**" is de "snelkoppeling" die we aan onze USB-sleutel hebben gegeven ("**/dev/mapper**" is algemeen voor Linux voor mapping). Het geeft daarom toegang tot onze gedecodeerde partitie. Dit is wat je nu zou moeten zien:



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



## IV. De versleutelde USB-sleutel gebruiken



### A. LUKS-volume openen en bewerken



**Via Interface grafiek** **:**



Onder Debian is "**dm-crypt**" standaard aanwezig. In de meeste gevallen vindt de installatie dus direct plaats als de USB-stick wordt aangesloten. Je wordt dan gevraagd om je passphrase in te voeren in een pop-up venster zoals dit:



![Image](assets/fr/018.webp)



Verzoek om de ontcijfering passphrase voor de LUKS-partitie in te voeren.



Zodra de passphrase is ingevoerd, zal je systeem het bestandssysteem op de sleutel kunnen lezen en vervolgens dit bestandssysteem mounten, wat onze gemounte partitie zal tonen:



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



**Op de commandoregel:**



Het is echter de moeite waard om te weten hoe je de bewerking uitvoert op de opdrachtregel. Laten we beginnen met het decoderen van de versleutelde partitie met "**crypsetup**" en het "**luksOpen**" subcommando:



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



Nu is het gedecodeerde volume van onze USB stick een volume dat ons bestandssysteem en OS kunnen gebruiken, dus we mounten de inhoud in een map, bijvoorbeeld "**/home/mickael/mnt**" in mijn geval:



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



Dit betekent dat we vrij en transparant toegang hebben tot de gegevens op onze USB-stick.



### B. LUKS-volume sluiten en verwijderen



Zodra onze operatie is voltooid, vergeet dan niet om alles goed af te sluiten om ervoor te zorgen dat we ons volume niet beschadigen. De eerste stap is om de:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Sluit vervolgens de versleutelde partitie zelf:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Nu ziet iedereen die onze USB-sleutel gebruikt niets van de inhoud, behalve versleutelde gegevens.



## V. Conclusie



Grafische gebruikersinterfaces maken deze handeling transparant, maar het is nog steeds nuttig om te weten hoe je een versleutelde LUKS-partitie formatteert, aanmaakt, opent en sluit vanaf de commandoregel. Eenmaal geformatteerd zijn de manipulaties die nodig zijn om een LUKS-partitie te openen en te sluiten minimaal vergeleken met de veiligheidswinst.