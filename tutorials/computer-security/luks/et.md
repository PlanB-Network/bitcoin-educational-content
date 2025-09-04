---
name: LUKS
description: USB-mäluseadme krüpteerimine LUKS-i ja cryptsetupiga
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Mickael Dorigny originaalsel sisul, mis on avaldatud veebilehel [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



USB-pulga krüpteerimine on hea viis oma tundlike andmete kaitsmiseks. **Selles õpetuses vaatame, kuidas kasutada LUKS (*Linux Unified Key Setup*) koos cryptsetupiga USB-pulga krüpteerimiseks Linuxi süsteemis.** See meetod võimaldab teil kaitsta oma andmeid, eriti juhul, kui teie USB-pulk kaob või varastatakse.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) on peamiselt Linuxi süsteemides kasutatav kettakrüpteerimise standard. See kaitseb andmeid, krüpteerides kettapartitsioone tugevate algoritmidega. Selle toetus Linuxi süsteemides lihtsustab krüpteerimisvõtmete ja paroolide haldamist, pakkudes standardiseeritud Interface ja ühilduvust erinevate haldusvahenditega.



Selle õpetuse järgimiseks on vaja:





- uSB võti;
- linuxi süsteem, kus on installitud "**cryptsetup**" (sageli on see vaikimisi saadaval, vastasel juhul näeme, kuidas seda saada).



## II. Cryptsetup'i paigaldamine



Kõigepealt peame veenduma, et meie süsteemis on käsk "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Kui te ei saa sellele käsule vastust, peate installima "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Nüüd on meil kõik vajalik, et luua LUKS-i abil meie krüpteeritud USB-võti.



Tegelikkuses teeb krüpteerimistöö ära utiliit "**dm-crypt**". "**cryptsetup**" on käsurea Interface, mis haldab **dm-crypt** funktsioone ja tegevusi.



## III. LUKS partitsiooni ja failisüsteemi loomine



### A. USB-mäluseadme tuvastamine



Me loome nüüd meie USB-pulgale krüpteeritud LUKS-partitsiooni. Kui te pole seda veel oma süsteemiga ühendanud, siis on nüüd õige aeg seda teha.



Selle õpetuse jaoks krüpteerin ma kogu oma USB-pulga, mitte ainult ühe partitsiooni. Samuti on oluline teada, et selle protseduuri käigus **kustutatakse võtmelt kõik olemasolevad andmed**.



Esimene samm on leida USB-pulgale vastav seadmefail kataloogis "**/dev/**". Sisestage USB-pulk ja tuvastage selle seadme nimi. Salvestusseadmete loetlemiseks saate kasutada järgmist käsku:



```
$ lsblk
```



Leidke oma USB-mälu, näiteks "**/dev/sdb**". Võite kasutada ka käsku "**fdisk -l**", et kuvada USB-võtme mudeli nimi (parem on mitte eksida) ja kasutada seadme salvestusruumi suurust näitajana:



![Image](assets/fr/019.webp)



Määrake krüpteeritav USB-võti tähisega "**lsblk**" ja "**fdisk**".



Minu näites asub minu USB-mälu "**/dev/sdb**". Kui te näete "**/dev/sdb1**", "**/dev/sdb2**" jne, siis on need partitsioonid praegu teie kettal. Need on praegu teie võtmes olevad partitsioonid. Need kustutatakse meie manipulatsiooni abil.



### B. Olemasolevate andmete kustutamine



Nüüd kustutame kõik andmed meie USB-pulgalt. Operatsioon seisneb selles, et täidame meie USB-pulgal oleva kettaruumi 0-ga.



**Vajuta, et sihtmärgiks on õige seadmefail!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



See tagab, et meie võtmes ei ole püsivaid lihtkirjas olevaid andmeid.



### C. Krüpteerige USB-võti LUKSiga



Nüüd initsialiseerime LUKSi partitsiooni meie USB-mäluseadmel. See hõlmab LUKS-partitsiooni loomist:



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



Siin initsialiseerib ja vormindab seade LUKS-krüpteerimise kasutamiseks alamkäsuga "`luksFormat`". Teil palutakse seda toimingut kinnitada, kirjutades suurtähtedega `YES`, seejärel defineerige *passphrase*. **Valige tugev *passphrase*, et tagada, et ründaja ei saaks kaotsimineku korral seda brute-force rünnakute abil avastada.



Pärast seda on ketas "**/dev/sdb**" LUKS-iga vormindatud ja valmis kasutamiseks krüpteeritud andmemahuna.



### D. Krüpteeritud mahu vormindamine



Oleme peaaegu valmis ja nüüd peame looma kehtiva partitsiooni meie LUKS partitsiooni sees. Nii saame pärast avamist kasutada seda nagu iga teist failisüsteemi. Selleks peame avama krüpteeritud partitsiooni:



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



Siin on "**usbkey1**" nimi, mille ma annan oma kontekstis partitsiooni mount'ile. Te võite valida, mis teile meeldib. Seejärel peame selle LUKS partitsioonis sisalduva partitsiooni vormindama, siin näiteks kui **ext4**:



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



**See, sihtkoha** on määratud kui "**/dev/mappe/usbkey1**"**, miks?



"**/dev/mapper/usbkey1**" on "otsetee", mille me oleme andnud meie USB-klahvile ("**/dev/mapper**" on Linuxi jaoks üldine kaardistamiseks). Seega annab see ligipääsu meie dekrüpteeritud partitsioonile. Siin on see, mida te nüüd peaksite nägema:



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



## IV. Krüpteeritud USB-võtme kasutamine



### A. Avage ja redigeerige LUKS-köidet



**Via Interface graafik** **:**



Debianis on "**dm-crypt**" vaikimisi olemas. Seega toimub paigaldus enamasti otse siis, kui USB-mälu on ühendatud. Seejärel palutakse teil sisestada oma passphrase sellises hüpikaknas nagu see siin:



![Image](assets/fr/018.webp)



LUKS-partitsiooni dekrüpteerimise passphrase sisestamise taotlus.



Kui passphrase on sisestatud, saab teie süsteem lugeda võtmes olevat failisüsteemi ja seejärel monteerida selle failisüsteemi, mis näitab meie monteeritud partitsiooni:



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



**Käsureal:**



Siiski tasub teada, kuidas seda toimingut käsureal teha. Alustame krüpteeritud partitsiooni dekrüpteerimisest, kasutades "**crypsetup**" ja alamkäsku "**luksOpen**":



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



Nüüd on meie USB-mäluseadme dekrüpteeritud maht selline maht, mida meie failisüsteem ja operatsioonisüsteem saavad kasutada, nii et me ühendame selle sisu suvalisse kausta, näiteks minu puhul "**/home/mickael/mnt**":



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



See tähendab, et me saame oma USB-pulgal olevatele andmetele vabalt ja läbipaistvalt juurde pääseda.



### B. Sulgege ja eemaldage LUKS-i maht



Kui meie operatsioon on lõppenud, ärge unustage kõike korralikult sulgeda, et me ei rikuks meie mahtu. Esimene samm on eemaldada:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Seejärel sulgege krüpteeritud partitsioon ise:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Nüüd ei näe igaüks, kes kasutab meie USB-mälu, selle sisu peale krüpteeritud andmete.



## V. Kokkuvõte



Graafilised kasutajaliidesed muudavad selle toimingu läbipaistvaks, kuid on siiski kasulik teada, kuidas krüpteeritud LUKS-partitsiooni käsurealt vormindada, luua, avada ja sulgeda. Pärast vormindamist on LUKS-partitsiooni avamiseks ja sulgemiseks vajalikud manipulatsioonid minimaalsed, võrreldes turvateguritega.