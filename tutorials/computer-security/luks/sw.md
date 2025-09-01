---
name: LUKS
description: Kusimba kiendeshi cha USB flash kwa kutumia LUKS na cryptsetup
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Mickael Dorigny yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



Kusimba fimbo ya USB ni njia nzuri ya kulinda data yako nyeti. **Katika somo hili, tutaangalia jinsi ya kutumia LUKS (*Linux Unified Key Setup*) pamoja na cryptsetup ili kusimba fimbo ya USB kwenye mfumo wa Linux.** Njia hii itakuwezesha kulinda data yako, hasa ikitokea kupoteza au kuibiwa kwa fimbo yako ya USB.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Usanidi wa Ufunguo Unaounganishwa wa Linux*) ni kiwango cha usimbaji fiche cha diski kinachotumiwa hasa kwenye mifumo ya Linux. Inalinda data kwa kusimba sehemu za diski kwa kutumia algorithms thabiti. Usaidizi wake kwenye mifumo ya Linux hurahisisha usimamizi wa funguo za usimbaji fiche na manenosiri, ikitoa Interface sanifu na utangamano na zana mbalimbali za usimamizi.



Ili kufuata mafunzo haya, utahitaji:





- ufunguo wa uSB;
- mfumo wa Linux ulio na "**cryptsetup**" iliyosakinishwa (mara nyingi inapatikana kwa chaguo-msingi, vinginevyo tutaona jinsi ya kuipata).



## II. Inasakinisha cryptsetup



Kwanza, tunahitaji kuhakikisha kuwa tunayo amri ya "**cryptsetup**" kwenye mfumo wetu:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Ikiwa hautapata jibu kwa amri hii, unahitaji kusakinisha "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Sasa tuna kila kitu tunachohitaji ili kuunda ufunguo wetu wa USB uliosimbwa kwa njia fiche kupitia LUKS.



Kwa kweli, ni matumizi ya "**dm-crypt**" ambayo yatafanya kazi ya usimbaji fiche. "**cryptsetup**" ni safu ya amri ya Interface ambayo inadhibiti vipengele na vitendo vya **dm-crypt**.



## III. Kuunda kizigeu cha LUKS na mfumo wa faili



### A. Tambua kitufe cha USB



Sasa tutaunda kizigeu kilichosimbwa cha LUKS kwenye fimbo yetu ya USB. Ikiwa bado hujaiunganisha kwenye mfumo wako, sasa ndio wakati wa kufanya hivyo.



Kwa madhumuni ya mafunzo haya, ninasimba fimbo yangu yote ya USB, sio kizigeu kimoja tu. Pia ni muhimu kujua kwamba wakati wa utaratibu huu, **data zote zilizopo zitafutwa kutoka kwa ufunguo **.



Hatua ya kwanza ni kupata faili ya kifaa inayolingana na fimbo yako ya USB kwenye saraka ya "**/dev/**". Ingiza kijiti chako cha USB na utambue jina la kifaa chake. Unaweza kutumia amri ifuatayo kuorodhesha vifaa vya kuhifadhi:



```
$ lsblk
```



Tafuta ufunguo wako wa USB, kwa mfano "**/dev/sdb**". Unaweza pia kutumia amri "**fdisk -l**" ili kuonyesha jina la modeli ya ufunguo wa USB (ni bora usifanye makosa), na utumie saizi ya hifadhi ya kifaa kama kiashirio:



![Image](assets/fr/019.webp)



Tambua ufunguo wa USB utakaosimbwa kwa njia fiche "**lsblk**" na "**fdisk**".



Katika mfano wangu, ufunguo wangu wa USB uko katika "**/dev/sdb**". Ukiona "**/dev/sdb1**", "**/dev/sdb2**", n.k., hizi ndizo sehemu zilizopo kwenye hifadhi yako. Hizi ndizo sehemu zilizopo kwenye ufunguo wako kwa sasa. Watafutwa kwa ghiliba zetu.



### B. Futa data iliyopo



Sasa tutafuta data yote kwenye fimbo yetu ya USB. Uendeshaji unajumuisha kujaza nafasi ya diski kwenye fimbo yetu ya USB na sekunde 0.



**Hakikisha unalenga faili sahihi ya kifaa!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Hii inahakikisha kwamba hakutakuwa na data ya matini inayoendelea kwenye ufunguo wetu.



### C. Simba ufunguo wa USB kwa njia fiche kwa LUKS



Sasa tutaanzisha kizigeu cha LUKS kwenye ufunguo wetu wa USB. Hii inajumuisha kuunda kizigeu cha LUKS:



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



Hapa, amri ndogo ya "`luksFormat`" inaanzisha na kuunda kifaa ili kutumia usimbaji fiche wa LUKS. Utaombwa kuthibitisha utendakazi huu kwa kuandika `NDIYO` kwa herufi kubwa, kisha ubainishe *passphrase*. **Chagua *passphrase* thabiti ili kuhakikisha kuwa, ikitokea hasara, mvamizi hawezi kuigundua kupitia mashambulizi ya nguvu.



Baada ya hayo, diski ya "**/dev/sdb**" itaumbizwa na LUKS na iko tayari kutumika kama sauti iliyosimbwa.



### D. Fomati sauti iliyosimbwa



Tumekaribia, na sasa tunahitaji kuunda kizigeu halali ndani ya kizigeu chetu cha LUKS. Kwa njia hii, baada ya kufunguliwa, tunaweza kuitumia kama mfumo mwingine wowote wa faili. Ili kufanya hivyo, tunahitaji kufungua kizigeu kilichosimbwa:



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



Hapa, "**usbkey1**" ndio jina ninalotoa kwa mlima wa kizigeu katika muktadha wangu. Unaweza kuchagua chochote unachopenda. Kisha tunahitaji kufomati kizigeu hiki kilichomo kwenye kizigeu cha LUKS, kwa mfano, hapa kama **ext4**:



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



**Hapa, eneo lengwa** limebainishwa kama "**/dev/mappe/usbkey1**"**, kwa nini?



"**/dev/mapper/usbkey1**" ni "njia ya mkato" ambayo tumetoa kwa ufunguo wetu wa USB ("**/dev/mapper**" ni ya kawaida kwa Linux kwa uchoraji ramani). Kwa hivyo hutoa ufikiaji wa kizigeu chetu kilichosimbwa. Hivi ndivyo unavyopaswa kuona sasa:



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



## IV. Kwa kutumia ufunguo wa USB uliosimbwa kwa njia fiche



### A. Fungua na uhariri sauti ya LUKS



**Kupitia mchoro wa Interface** **:**



Chini ya Debian, "**dm-crypt**" inapatikana kwa chaguo-msingi. Kwa hivyo, katika hali nyingi, usakinishaji hufanyika moja kwa moja wakati ufunguo wa USB umechomekwa. Kisha utaombwa kuingiza passphrase yako katika dirisha ibukizi kama hili:



![Image](assets/fr/018.webp)



Ombi la kuweka usimbuaji wa passphrase kwa kizigeu cha LUKS.



Mara tu passphrase imeingizwa, mfumo wako utaweza kusoma mfumo wa faili kwenye ufunguo na kisha kuweka mfumo huu wa faili, ambao utaonyesha kizigeu chetu kilichowekwa:



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



**Kwenye mstari wa amri:**



Walakini, inafaa kujua jinsi ya kufanya operesheni kwenye mstari wa amri. Wacha tuanze kwa kusimbua kizigeu kilichosimbwa kwa kutumia "**crypsetup**" na amri ndogo ya "**luksOpen**":



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



Sasa, kiasi kilichosimbwa cha kiendeshi chetu cha USB flash kinawasilisha kiasi ambacho mfumo wetu wa faili na OS unaweza kutumia, kwa hivyo tutaweka yaliyomo kwenye folda yoyote, kwa mfano "**/home/mickael/mnt**" katika kesi yangu:



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



Hii inamaanisha kuwa tunaweza kufikia data kwenye fimbo yetu ya USB kwa uhuru na kwa uwazi.



### B. Funga na uondoe sauti ya LUKS



Operesheni yetu inapokamilika, usisahau kufunga kila kitu ipasavyo ili kuhakikisha kuwa hatuharibu sauti yetu. Hatua ya kwanza ni kuondoa:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Kisha funga kizigeu kilichosimbwa yenyewe:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Sasa, mtu yeyote anayetumia ufunguo wetu wa USB hataona chochote cha yaliyomo isipokuwa data iliyosimbwa.



## V. Hitimisho



Miingiliano ya mchoro ya mtumiaji hufanya operesheni hii kuwa wazi, lakini bado ni muhimu kujua jinsi ya kufomati, kuunda, kufungua na kufunga kizigeu kilichosimbwa cha LUKS kutoka kwa safu ya amri. Mara tu ikiwa imeumbizwa, ghiliba zinazohitajika ili kufungua na kufunga kizigeu cha LUKS ni chache ikilinganishwa na faida za usalama.