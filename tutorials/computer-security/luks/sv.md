---
name: LUKS
description: Kryptera ett USB-minne med LUKS och cryptsetup
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Mickael Dorigny publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i den ursprungliga texten.*



___



## I. Presentation



Att kryptera ett USB-minne är ett bra sätt att skydda känsliga data. **I den här handledningen tittar vi på hur du använder LUKS (*Linux Unified Key Setup*) med cryptsetup för att kryptera ett USB-minne på ett Linux-system.** Den här metoden gör att du kan skydda dina data, särskilt i händelse av förlust eller stöld av ditt USB-minne.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) är en standard för diskkryptering som främst används i Linux-system. Den säkrar data genom att kryptera diskpartitioner med robusta algoritmer. Dess stöd på Linux-system underlättar hanteringen av krypteringsnycklar och lösenord, erbjuder standardiserad Interface och kompatibilitet med olika hanteringsverktyg.



För att följa denna handledning behöver du :





- uSB-tangenten;
- ett Linux-system med "**cryptsetup**" installerat (finns ofta som standard, annars ser vi hur man får tag på det).



## II. Installera cryptsetup



Först måste vi se till att vi har kommandot "**cryptsetup**" på vårt system:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Om du inte får något svar på detta kommando måste du installera "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Nu har vi allt vi behöver för att skapa vår krypterade USB-nyckel via LUKS.



I själva verket är det verktyget "**dm-crypt**" som utför krypteringsarbetet. "**cryptsetup**" är en Interface för kommandoraden som hanterar funktioner och åtgärder i **dm-crypt**.



## III. Skapa LUKS-partition och filsystem



### A. Identifiera USB-nyckeln



Vi ska nu skapa en krypterad LUKS-partition på vårt USB-minne. Om du inte redan har anslutit det till ditt system är det dags att göra det nu.



I den här handledningen krypterar jag hela mitt USB-minne, inte bara en partition. Det är också viktigt att veta att under denna procedur kommer **all befintlig data att raderas från nyckeln**.



Det första steget är att leta reda på den enhetsfil som motsvarar ditt USB-minne i katalogen "**/dev/**". Sätt i USB-minnet och identifiera dess enhetsnamn. Du kan använda följande kommando för att lista lagringsenheter:



```
$ lsblk
```



Leta reda på ditt USB-minne, t.ex. "**/dev/sdb**". Du kan också använda kommandot "**fdisk -l**" för att visa namnet på USB-nyckelns modell (det är bäst att inte göra ett misstag) och använda enhetens lagringsstorlek som en indikator:



![Image](assets/fr/019.webp)



Identifiera den USB-nyckel som ska krypteras med "**lsblk**" och "**fdisk**".



I mitt exempel finns min USB-nyckel i "**/dev/sdb**". Om du ser "**/dev/sdb1**", "**/dev/sdb2**" osv. är det de partitioner som för närvarande finns på din enhet. Det här är de partitioner som för närvarande finns på din nyckel. De kommer att raderas genom vår manipulation.



### B. Ta bort befintliga data



Vi ska nu radera alla data på vårt USB-minne. Åtgärden består i att fylla diskutrymmet på vårt USB-minne med 0:or.



**Se till att du riktar in dig på rätt enhetsfil!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Detta säkerställer att det inte kommer att finnas någon bestående klartextdata på vår nyckel.



### C. Kryptera USB-nyckeln med LUKS



Vi ska nu initiera LUKS-partitionen på vårt USB-minne. Detta innebär att skapa LUKS-partitionen:



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



Här initierar och formaterar underkommandot "`luksFormat`" enheten så att den använder LUKS-kryptering. Du uppmanas att bekräfta åtgärden genom att skriva `YES` med versaler och sedan definiera en *passphrase*. **Välj en robust *passphrase* för att säkerställa att angriparen inte kan upptäcka den via brute-force-attacker om den skulle gå förlorad.



Efter detta kommer disken "**/dev/sdb**" att formateras med LUKS och vara redo att användas som en krypterad volym.



### D. Formatera krypterad volym



Vi är nästan framme, och nu måste vi skapa en giltig partition inom vår LUKS-partition. På så sätt kan vi använda den som vilket annat filsystem som helst när den är upplåst. För att göra detta måste vi öppna den krypterade partitionen:



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



Här är "**usbkey1**" det namn som jag ger till partitionsmonteringen i mitt sammanhang. Du kan välja vilket du vill. Vi måste sedan formatera den här partitionen som finns i LUKS-partitionen, till exempel här som **ext4** :



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



**Här anges målplatsen** som "**/dev/mappe/usbkey1**"**, varför?



"**/dev/mapper/usbkey1**" är den "genväg" vi har gett till vår USB-nyckel ("**/dev/mapper**" är en generisk mappning i Linux). Den ger därför tillgång till vår dekrypterade partition. Det här är vad du ska se nu :



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



## IV. Använda den krypterade USB-nyckeln



### A. Öppna och redigera LUKS-volym



**Via Interface grafik** **:**



Under Debian finns "**dm-crypt**" som standard. Så i de flesta fall sker installationen direkt när USB-nyckeln ansluts. Du kommer då att bli ombedd att ange din passphrase i ett popup-fönster som det här:



![Image](assets/fr/018.webp)



Begäran om att ange dekryptering passphrase för LUKS-partitionen.



När passphrase har skrivits in kan ditt system läsa filsystemet på nyckeln och sedan montera detta filsystem, vilket visar vår monterade partition:



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



**På kommandoraden: **



Det är dock värt att veta hur man utför operationen på kommandoraden. Låt oss börja med att dekryptera den krypterade partitionen med hjälp av "**crypsetup**" och underkommandot "**luksOpen**":



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



Nu presenterar den dekrypterade volymen på vårt USB-minne en volym som vårt filsystem och operativsystem kan använda, så vi monterar dess innehåll i valfri mapp, till exempel "**/home/mickael/mnt**" i mitt fall:



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



Detta innebär att vi kan komma åt data på vårt USB-minne fritt och transparent.



### B. Stäng och ta bort LUKS-volymen



När vår operation är klar, glöm inte att stänga allt ordentligt för att se till att vi inte korrumperar vår volym. Det första steget är att avmontera :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Stäng sedan den krypterade partitionen själv:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Nu kan alla som använder vår USB-nyckel inte se något av innehållet förutom krypterade data.



## V. Slutsats



Grafiska användargränssnitt gör denna operation transparent, men det är fortfarande användbart att veta hur man formaterar, skapar, öppnar och stänger en krypterad LUKS-partition från kommandoraden. När den väl är formaterad är de manipulationer som krävs för att öppna och stänga en LUKS-partition minimala jämfört med säkerhetsvinsterna.