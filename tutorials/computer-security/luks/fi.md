---
name: LUKS
description: USB-muistitikun salaus LUKS:llä ja cryptsetupilla
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Mickael Dorignyn alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



USB-tikun salaaminen on hyvä tapa suojata arkaluonteiset tietosi. **Tässä oppaassa katsomme, miten voit käyttää LUKS:ää (*Linux Unified Key Setup*) ja cryptsetupia USB-tikun salaamiseen Linux-järjestelmässä.** Tämän menetelmän avulla voit suojata tietosi erityisesti siinä tapauksessa, että USB-tikku katoaa tai varastetaan.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) on levyn salausstandardi, jota käytetään pääasiassa Linux-järjestelmissä. Se suojaa tietoja salaamalla levyosioita vankoilla algoritmeilla. Sen tuki Linux-järjestelmissä helpottaa salausavainten ja salasanojen hallintaa tarjoamalla standardoidun Interface:n ja yhteensopivuuden eri hallintatyökalujen kanssa.



Tämän ohjeen seuraamiseen tarvitset :





- uSB-avain;
- linux-järjestelmä, johon on asennettu "**cryptsetup**" (usein saatavilla oletusarvoisesti, muuten katsotaan, miten se saadaan).



## II. Cryptsetupin asentaminen



Ensin meidän on varmistettava, että järjestelmässämme on komento "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Jos et saa vastausta tähän komentoon, sinun on asennettava "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Meillä on nyt kaikki, mitä tarvitsemme salatun USB-avaimen luomiseen LUKS:n avulla.



Todellisuudessa salaus tehdään "**dm-crypt**"-apuohjelmalla. "**cryptsetup**" on komentorivin Interface, joka hallitsee **dm-crypt**:n ominaisuuksia ja toimintoja.



## III. LUKS-osion ja tiedostojärjestelmän luominen



### A. Tunnista USB-tikku



Luomme nyt salatun LUKS-osion USB-tikulle. Jos et ole vielä liittänyt sitä järjestelmään, nyt on aika tehdä niin.



Tässä ohjeessa salaan koko USB-tikkuni, en vain yhtä osiota. On myös tärkeää tietää, että tämän toimenpiteen aikana **kaikki olemassa olevat tiedot poistetaan avaimesta**.



Ensimmäinen vaihe on etsiä USB-tikkua vastaava laitetiedosto hakemistosta "**/dev/**". Aseta USB-tikku paikalleen ja tunnista sen laitteen nimi. Voit käyttää seuraavaa komentoa tallennuslaitteiden luettelointiin:



```
$ lsblk
```



Etsi USB-muistitikku, esimerkiksi "**/dev/sdb**". Voit myös käyttää komentoa "**fdisk -l**" näyttämään USB-levyn mallin nimen (ei kannata erehtyä) ja käyttää laitteen tallennuskokoa osoituksena:



![Image](assets/fr/019.webp)



Tunnista salattava USB-avain merkinnöillä "**lsblk**" ja "**fdisk**".



Esimerkissäni USB-levy sijaitsee paikassa "**/dev/sdb**". Jos näet "**/dev/sdb1**", "**/dev/sdb2**" jne., nämä ovat asemallasi tällä hetkellä olevat osiot. Nämä osiot ovat tällä hetkellä näppäimessäsi olevat osiot. Manipulaatiomme poistaa ne.



### B. Poista olemassa olevat tiedot



Poistamme nyt kaikki tiedot USB-tikulta. Toimenpide koostuu USB-tikkumme levytilan täyttämisestä 0:lla.



**Varmista, että kohdistat oikeaan laitetiedostoon!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Näin varmistetaan, että avaimessamme ei ole pysyviä selkotekstitietoja.



### C. Salaa USB-avain LUKS:llä



Aloitamme nyt LUKS-osion alustamisen USB-levyllä. Tämä edellyttää LUKS-osion luomista:



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



Tässä "`luksFormat`"-alakomento alustaa ja alustaa laitteen käyttämään LUKS-salausta. Sinua pyydetään vahvistamaan tämä toiminto kirjoittamalla `YES` suuraakkosin ja määrittele sitten *passphrase*. **Valitse vankka *passphrase* sen varmistamiseksi, että häviön sattuessa hyökkääjä ei voi löytää sitä brute-force-hyökkäyksillä.



Tämän jälkeen levy "**/dev/sdb**" alustetaan LUKS:llä ja se on valmis käytettäväksi salattuna tietovälineenä.



### D. Muotoile salattu tilavuus



Olemme melkein perillä, ja nyt meidän on luotava kelvollinen osio LUKS-osion sisällä. Näin voimme avata lukituksen ja käyttää sitä kuten mitä tahansa muuta tiedostojärjestelmää. Tätä varten meidän on avattava salattu osio:



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



Tässä "**usbkey1**" on nimi, jonka annan omassa kontekstissani osiolle. Voit valita haluamasi nimen. Sitten meidän on alustettava tämä LUKS-osion sisältämä osio, esimerkiksi tässä muodossa **ext4** :



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



**Tässä kohdepaikka** on määritelty "**/dev/mappe/usbkey1**"**, miksi?



"**/dev/mapper/usbkey1**" on "pikakuvake", jonka olemme antaneet USB-avaimellemme ("**/dev/mapper**" on yleinen Linuxin kartoitus). Se tarjoaa siis pääsyn purettuun osioon. Tässä on, mitä sinun pitäisi nyt nähdä :



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



## IV. Salatun USB-avaimen käyttäminen



### A. Avaa ja muokkaa LUKS-tietue



**Via Interface graphic** **:**:**



Debianissa "**dm-crypt**" on oletuksena mukana. Asennus tapahtuu siis useimmissa tapauksissa suoraan, kun USB-avain kytketään. Tämän jälkeen sinua pyydetään syöttämään passphrase-tietosi tämän kaltaisessa ponnahdusikkunassa:



![Image](assets/fr/018.webp)



Pyyntö syöttää LUKS-osion salauksen purku passphrase.



Kun passphrase on syötetty, järjestelmäsi pystyy lukemaan avaimessa olevan tiedostojärjestelmän ja mounttaa sen jälkeen tämän tiedostojärjestelmän, mikä näyttää mountatun osiomme:



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



**Komentorivillä:**



Kannattaa kuitenkin tietää, miten toiminto suoritetaan komentorivillä. Aloitetaan salauksen purkaminen salatusta osiosta käyttämällä "**crypsetup**"-ohjelmaa ja "**luksOpen**"-alakomentoa:



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



Nyt USB-muistitikkumme purettu tilavuus on tilavuus, jota tiedostojärjestelmämme ja käyttöjärjestelmämme voivat käyttää, joten liitämme sen sisällön mihin tahansa kansioon, esimerkiksi "**/home/mickael/mnt**" minun tapauksessani:



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



Tämä tarkoittaa, että voimme käyttää USB-tikulla olevia tietoja vapaasti ja avoimesti.



### B. Sulje ja poista LUKS-tilavuus



Kun operaatio on valmis, älä unohda sulkea kaikkea kunnolla varmistaaksemme, ettemme vahingoita tallennustilavuutta. Ensimmäinen askel on irrottaa :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Sulje sitten itse salattu osio:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Nyt kuka tahansa USB-avaimen käyttäjä ei näe sen sisällöstä mitään muuta kuin salattua tietoa.



## V. Päätelmät



Graafiset käyttöliittymät tekevät tästä toiminnosta läpinäkyvää, mutta on silti hyödyllistä tietää, miten salattu LUKS-osio voidaan alustaa, luoda, avata ja sulkea komentoriviltä. Kun LUKS-osio on alustettu, sen avaamiseen ja sulkemiseen vaadittavat toimenpiteet ovat minimaalisia verrattuna turvallisuushyötyihin.