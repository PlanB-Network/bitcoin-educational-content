---
name: LUKS
description: Gushiramwo amakuru kuri USB na LUKS na cryptsetup
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Mickael Dorigny vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## I. Ugushikiriza



Gushiramwo amakuru yawe y’agaciro kuri USB ni uburyo bwiza bwo kurinda amakuru yawe y’agaciro. **Muri iyi nyigisho, turaza kuraba ingene wokoresha LUKS (*Linux Unified Key Setup*) n'ivy'ubuhinga bwa cryptsetup kugira ngo ukoreshe ubuhinga bwa USB kuri system ya Linux.** Ubu buryo buzogufasha gukingira amakuru yawe, cane cane iyo ushobora gutakaza canke kwiba ubuhinga bwawe bwa USB.



[**LUKS**](*Itegeko ry'urufunguzo rwa Linux*) ni urugero rwo gushiramwo amakuru y'urufunguzo rwa disiki rukoreshwa cane cane kuri sisitemu za Linux. Ikingira amakuru mu gupfuka ibice vya disiki bikoresheje ubuhinga bukomeye. Infashanyo yayo ku mirongo ya Linux yorosha gucunga imfunguruzo n’amajambo y’ibanga, itanga Interface igezweho n’uguhuza n’ibikoresho bitandukanye vyo gucunga.



Kugira ngo ukurikize iyi nyigisho, uzokenera:





- urufunguzo rwa uSB;
- ubuhinga bwa Linux bufise "**cryptsetup**" (kenshi buraboneka ku buryo busanzwe, ahandi ho tuzobona ingene twoburonka).



## II. Gushiramwo ububiko



Mbere, dukwiye kumenya neza ko dufise itegeko "**cryptsetup**" kuri sisitemu yacu:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Niwaba utaronse inyishu kuri iri tegeko, ukeneye gushiramwo "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Ubu turafise ivyo dukeneye vyose kugira ngo dukore urufunguzo rwacu rwa USB rwashizwemwo amakuru biciye kuri LUKS.



Mu vy'ukuri, ni ubuhinga bwa "**dm-crypt**" buzokora igikorwa co gupfuka. "**cryptsetup**" ni umurongo w'amabwirizwa Interface ucungera ibiranga n'ibikorwa vya **dm-crypt**.



## III. Gukora umugabane wa LUKS na sisitemu ya dosiye



### A. Menya urufunguzo rwa USB



Ubu tugiye gukora igice ca LUKS gipfutse ku nkoni yacu ya USB. Niba utarayifatanya na system yawe, ubu ni igihe co kubikora.



Kubera intumbero z’iyi nyigisho, ndiko ndashiramwo amakuru y’uruzitiro rwanje rwose rwa USB, atari uruzitiro rumwe gusa. Ni ngombwa kandi kumenya ko mu gihe c'iyi nzira, **amakuru yose ariho azokurwaho ku rufunguzo**.



Intambwe ya mbere ni ukurondera dosiye y'igikoresho ihuye n'inkoni yawe ya USB mu bubiko bwa "**/dev/**". Injiramwo USB yawe maze umenye izina ry’igikoresho cayo. Ushobora gukoresha iri tegeko kugira ngo ukore urutonde rw'ibikoresho vyo kubika:



```
$ lsblk
```



Rondera urufunguzo rwawe rwa USB, nk'akarorero "**/dev/sdb**". Ushobora kandi gukoresha itegeko "**fdisk -l**" kugira ngo ugaragaze izina ry'urufunguzo rwa USB (ni vyiza ko udakora ikosa), kandi ukoreshe ubunini bw'ububiko bw'igikoresho nk'ikimenyetso:



![Image](assets/fr/019.webp)



Menya urufunguzo rwa USB ruzoshirwamwo "**lsblk**" na "**fdisk**".



Mu karorero kanje, urufunguzo rwanje rwa USB ruri muri "**/dev/sdb**". Niwabona "**/dev/sdb1**", "**/dev/sdb2**", n'ibindi, ivyo ni vyo bice biri kuri drive yawe. Ivyo ni vyo bice biri ubu ku rufunguzo rwawe. Bizokurwaho n’ugukoresha nabi kwacu.



### B. Gukuraho amakuru asanzweho



Ubu tugiye gukuraho amakuru yose ari kuri USB stick yacu. Ico gikorwa gishingiye ku kwuzuza umwanya wo kuri disk kuri USB stick yacu n’ama 0s.



**Urabe neza ko wibanda kuri dosiye y'igikoresho ibereye!**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Ivyo bituma ata makuru y’inyandiko yoroshe azogumaho ku rufunguzo rwacu.



### C. Gushiramwo urufunguzo rwa USB na LUKS



Ubu tugiye gutanguza igice ca LUKS ku rufunguzo rwacu rwa USB. Ibi birimwo gukora igice ca LUKS:



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



Aha, itegeko rito "`luksFormat`" ritangura kandi rihindura igikoresho kugira ngo gikoreshe ububiko bwa LUKS. Uzosabwa kwemeza iki gikorwa wanditse `EGO` mu nyuguti nini, hanyuma usobanure *passphrase*. **Hitamwo *passphrase* ikomeye kugira ngo, iyo utakaje, uwuyitera ntashobora kuyibona biciye mu bitero vy'inguvu z'agahomerabunwa.**



Inyuma y'ivyo, disiki "**/dev/sdb**" izogira uburyo bwa LUKS kandi yiteguye gukoreshwa nk'igitabu gifise amakuru.



### D. Guhindura umubare washizwemwo



Turahejeje gushika, ubu rero turakeneye gukora igice gibereye mu gice cacu ca LUKS. Uko niko, iyo tumaze gufungura, turashobora kuyikoresha nk’iyindi nzira yose y’amadosiye. Kugira ivyo tubikore, dukeneye gufungura igice gipfutse:



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



Aha, "**usbkey1**" ni izina mpa umusozi w'imigabane mu gihe canje. Ushobora guhitamwo ico ukunda cose. Turakeneye rero guhindura iyi nzira iri mu nzira ya LUKS, nk'akarorero, hano nka **ext4**:



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



**Aha, ahantu h'intumbero** hagaragazwa nk'"**/dev/ikarita/usbkey1**", kuki?



"**/dev/mapper/usbkey1**" ni "inzira ngufi" twahaye urufunguzo rwacu rwa USB ("**/dev/mapper**" ni rusangi kuri Linux ku gukora ikarita). Ni co gituma itanga uburenganzira bwo gushika ku gice cacu ca decrypted. Ehe ivyo ukwiye kubona ubu:



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



## IV. Gukoresha urufunguzo rwa USB rwashizwemwo



### A. Gufungura no guhindura umuzingo wa LUKS



**Biciye ku gishushanyo ca Interface** **:**



Munsi ya Debian, "**dm-crypt**" iriho ku buryo busanzwe. Rero, kenshi, gushiramwo bishika ataco bimaze iyo urufunguzo rwa USB rushizwemwo. Uzoca usabwa kwinjiza passphrase yawe mw’idirisha rizoza nk’iri:



![Image](assets/fr/018.webp)



Gusaba kwinjira mu gusobanura passphrase ku bijanye n’igice ca LUKS.



passphrase imaze kwinjira, sisitemu yawe izoshobora gusoma sisitemu ya dosiye iri ku rufunguzo hanyuma ishireko iyi sisitemu ya dosiye, izokwerekana igice cacu cashizweko:



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



**Ku murongo w'itegeko:**



Ariko rero, birabereye kumenya ingene wokora igikorwa ku murongo w’amabwirizwa. Reka dutangure mu gukuraho igice gipfutse dukoresheje "**crypsetup**" n'itegeko rito "**luksOpen**":



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



Ubu, umubare w'amajambo ya USB yacu ugaragaza umubare systeme yacu ya dosiye na OS bishobora gukoresha, rero tuzoshira ibirimwo muri dosiye iyo ari yo yose, nk'akarorero "**/home/mickael/mnt**" mu gihe canje:



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



Ivyo bisigura ko dushobora gushika ku makuru ari kuri USB yacu mu mwidegemvyo kandi mu buryo buboneye.



### B. Funga kandi ukureho umubare wa LUKS



Igihe operation yacu irangiye, ntimwibagire gufunga vyose neza kugira ngo ntituzohonye ijwi ryacu. Intambwe ya mbere ni ugukuraho:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Hanyuma ufunge igice gipfutse ubwaco:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Ubu, umuntu wese akoresha urufunguzo rwacu rwa USB nta kintu na kimwe azobona mu birimwo kiretse amakuru yashizwemwo.



## V. Insozero



Ibishushanyo vy'abakoresha bituma iki gikorwa gica ibibatsi, ariko biracari ngirakamaro kumenya ingene wohindura, urema, ufungura no gufunga igice ca LUKS gipfutse uhereye ku murongo w'amabwirizwa. Iyo imaze gutegurwa, ibikorwa bisabwa kugira ngo umuntu yugurure no gufunga igice ca LUKS ni bike cane ugereranije n’inyungu z’umutekano.