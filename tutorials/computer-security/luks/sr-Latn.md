---
name: LUKS
description: Šifrovanje USB fleš drajva pomoću LUKS i cryptsetup
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Mickaela Dorignyja objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



Šifrovanje USB memorije je dobar način zaštite vaših osetljivih podataka. **U ovom vodiču, pogledaćemo kako koristiti LUKS (*Linux Unified Key Setup*) sa cryptsetup za šifrovanje USB memorije na Linux sistemu.** Ova metoda će vam omogućiti da osigurate vaše podatke, posebno u slučaju gubitka ili krađe vaše USB memorije.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) je standard za šifrovanje diskova koji se uglavnom koristi na Linux sistemima. Obezbeđuje sigurnost podataka šifrovanjem particija diska robusnim algoritmima. Njegova podrška na Linux sistemima olakšava upravljanje ključevima za šifrovanje i lozinkama, nudeći standardizovani Interface i kompatibilnost sa različitim alatima za upravljanje.



Da biste pratili ovaj vodič, trebat će vam :





- uSB ključ;
- sistem Linux sa instaliranim "**cryptsetup**" (često dostupan po defaultu, inače ćemo videti kako da ga nabavimo).



## II. Instaliranje cryptsetup



Prvo, moramo se uveriti da imamo komandu "**cryptsetup**" na našem sistemu:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Ako ne dobijete odgovor na ovu komandu, potrebno je da instalirate "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Sada imamo sve što nam je potrebno za kreiranje našeg enkriptovanog USB ključa putem LUKS-a.



U stvarnosti, to je "**dm-crypt**" alat koji će obaviti posao enkripcije. "**cryptsetup**" je komandno-linijski Interface koji upravlja funkcijama i akcijama **dm-crypt**.



## III. Kreiranje LUKS particije i datotečnog sistema



### A. Identifikujte USB ključ



Sada ćemo kreirati šifrovanu LUKS particiju na našem USB stik-u. Ako ga već niste povezali sa svojim sistemom, sada je vreme da to učinite.



Za potrebe ovog tutorijala, šifrujem ceo svoj USB stik, ne samo jednu particiju. Takođe je važno znati da će tokom ove procedure, **svi postojeći podaci biti obrisani sa ključa**.



Prvi korak je da pronađete datoteku uređaja koja odgovara vašem USB stiku u direktorijumu "**/dev/**". Ubacite vaš USB stik i identifikujte ime njegovog uređaja. Možete koristiti sledeću komandu da prikažete skladišne uređaje:



```
$ lsblk
```



Pronađite vaš USB ključ, na primer "**/dev/sdb**". Takođe možete koristiti komandu "**fdisk -l**" da prikažete naziv modela USB ključa (najbolje je ne pogrešiti), i koristite veličinu skladišta uređaja kao indikator:



![Image](assets/fr/019.webp)



Identifikujte USB ključ koji treba šifrovati pomoću "**lsblk**" i "**fdisk**".



U mom primeru, moj USB ključ se nalazi u "**/dev/sdb**". Ako vidite "**/dev/sdb1**", "**/dev/sdb2**", itd., to su particije trenutno prisutne na vašem disku. To su particije trenutno prisutne na vašem ključu. One će biti obrisane našom manipulacijom.



### B. Izbriši postojeće podatke



Sada ćemo obrisati sve podatke na našem USB stiku. Operacija se sastoji u popunjavanju prostora na disku našeg USB stika nulama.



**Uverite se da ciljate pravi uređajski fajl!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Ovo osigurava da neće biti trajnih podataka u običnom tekstu na našem ključu.



### C. Šifrujte USB ključ sa LUKS



Sada ćemo inicijalizovati LUKS particiju na našem USB ključu. Ovo uključuje kreiranje LUKS particije:



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



Ovde, podkomanda "`luksFormat`" inicijalizuje i formatira uređaj za korišćenje LUKS enkripcije. Bićete upitani da potvrdite ovu operaciju tako što ćete uneti `YES` velikim slovima, zatim definišite *passphrase*. **Izaberite robustan *passphrase* kako biste osigurali da, u slučaju gubitka, napadač ne može da ga otkrije putem brute-force napada.



Nakon ovoga, disk "**/dev/sdb**" će biti formatiran sa LUKS i spreman za korišćenje kao šifrovani volumen.



### D. Formatiraj šifrovani volumen



Skoro smo stigli, i sada treba da kreiramo važeću particiju unutar naše LUKS particije. Na ovaj način, kada je otključamo, možemo je koristiti kao bilo koji drugi fajl sistem. Da bismo to uradili, treba da otvorimo enkriptovanu particiju:



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



Ovde, "**usbkey1**" je ime koje dajem montiranoj particiji u mom kontekstu. Možete izabrati koje god želite. Zatim treba da formatiramo ovu particiju sadržanu u LUKS particiji, na primer, ovde kao **ext4** :



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



**Ovde, ciljana lokacija** je navedena kao "**/dev/mappe/usbkey1**"**, zašto?**



"**/dev/mapper/usbkey1**" je "prečica" koju smo dali našem USB ključu ("**/dev/mapper**" je generički za Linux za mapiranje). Stoga omogućava pristup našoj dekriptovanoj particiji. Evo šta bi sada trebalo da vidite:



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



## IV. Korišćenje enkriptovanog USB ključa



### A. Otvori i uredi LUKS volumen



**Preko Interface grafike** **:**



Pod Debianom, "**dm-crypt**" je prisutan po defaultu. Dakle, u većini slučajeva, instalacija se odvija direktno kada je USB ključ priključen. Zatim će vam biti zatraženo da unesete vaš passphrase u iskačućem prozoru kao što je ovaj:



![Image](assets/fr/018.webp)



Zahtev za unos dekripcije passphrase za LUKS particiju.



Jednom kada se unese passphrase, vaš sistem će moći da pročita sistem datoteka na ključu i zatim montira ovaj sistem datoteka, što će prikazati naš montirani particiju:



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



**Na komandnoj liniji:**



Međutim, vredi znati kako izvršiti operaciju u komandnoj liniji. Počnimo dešifrovanjem šifrovane particije koristeći "**crypsetup**" i podkomandu "**luksOpen**":



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



Sada, dekriptovani volumen našeg USB fleš drajva predstavlja volumen koji naš fajl sistem i operativni sistem mogu koristiti, tako da ćemo montirati njegov sadržaj u bilo koji folder, na primer "**/home/mickael/mnt**" u mom slučaju:



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



To znači da možemo slobodno i transparentno pristupiti podacima na našem USB stik-u.



### B. Zatvori i ukloni LUKS volumen



Kada naša operacija bude završena, ne zaboravite da sve pravilno zatvorite kako bismo bili sigurni da ne oštetimo naš volumen. Prvi korak je demontiranje :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Zatim zatvorite samu šifrovanu particiju:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Sada, svako ko koristi naš USB ključ neće videti ništa od njegovog sadržaja osim šifrovanih podataka.



## V. Zaključak



Grafički korisnički interfejsi čine ovu operaciju transparentnom, ali je i dalje korisno znati kako formatirati, kreirati, otvoriti i zatvoriti šifrovanu LUKS particiju iz komandne linije. Kada je formatirana, manipulacije potrebne za otvaranje i zatvaranje LUKS particije su minimalne u poređenju sa sigurnosnim dobicima.