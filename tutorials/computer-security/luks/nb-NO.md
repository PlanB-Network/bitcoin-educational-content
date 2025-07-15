---
name: LUKS
description: Kryptering av en USB-minnepinne med LUKS og cryptsetup
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Mickael Dorigny publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



Kryptering av en USB-pinne er en god måte å beskytte sensitive data på. **I denne veiledningen skal vi se på hvordan du bruker LUKS (*Linux Unified Key Setup*) med cryptsetup til å kryptere en USB-pinne på et Linux-system, slik at du kan sikre dataene dine, spesielt i tilfelle du mister eller blir frastjålet USB-pinnen din.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) er en diskkrypteringsstandard som hovedsakelig brukes på Linux-systemer. Den sikrer data ved å kryptere diskpartisjoner med robuste algoritmer. Støtten for Linux-systemer gjør det enklere å administrere krypteringsnøkler og passord, og tilbyr standardisert Interface og kompatibilitet med ulike administrasjonsverktøy.



For å følge denne opplæringen trenger du :





- uSB-nøkkel;
- et Linux-system med "**cryptsetup**" installert (ofte tilgjengelig som standard, ellers skal vi se hvordan du får tak i det).



## II. Installere cryptsetup



Først må vi sørge for at vi har kommandoen "**cryptsetup**" på systemet vårt:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Hvis du ikke får noe svar på denne kommandoen, må du installere "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Vi har nå alt vi trenger for å lage vår krypterte USB-nøkkel via LUKS.



I virkeligheten er det verktøyet "**dm-crypt**" som utfører krypteringsarbeidet. "**cryptsetup**" er en kommandolinje-Interface som administrerer funksjonene og handlingene til **dm-crypt**.



## III. Opprette LUKS-partisjonen og filsystemet



### A. Identifiser USB-nøkkelen



Vi skal nå opprette en kryptert LUKS-partisjon på USB-minnepinnen vår. Hvis du ikke allerede har koblet den til systemet ditt, er det på tide å gjøre det nå.



I denne veiledningen krypterer jeg hele USB-pinnen, ikke bare én partisjon. Det er også viktig å vite at under denne prosedyren vil **alle eksisterende data slettes fra nøkkelen**.



Det første trinnet er å finne enhetsfilen som tilsvarer USB-pinnen din i katalogen "**/dev/**". Sett inn USB-minnepinnen og identifiser enhetens navn. Du kan bruke følgende kommando for å få en liste over lagringsenheter:



```
$ lsblk
```



Finn USB-nøkkelen din, for eksempel "**/dev/sdb**". Du kan også bruke kommandoen "**fdisk -l**" for å vise navnet på USB-nøkkelmodellen (det er best å ikke gjøre en feil), og bruke enhetens lagringsstørrelse som en indikator:



![Image](assets/fr/019.webp)



Identifiser USB-nøkkelen som skal krypteres med "**lsblk**" og "**fdisk**".



I mitt eksempel er USB-nøkkelen min plassert i "**/dev/sdb**". Hvis du ser "**/dev/sdb1**", "**/dev/sdb2**" osv., er dette partisjonene som for øyeblikket finnes på stasjonen din. Dette er partisjonene som for øyeblikket finnes på nøkkelen din. De vil bli slettet ved vår manipulering.



### B. Slett eksisterende data



Vi skal nå slette alle dataene på USB-minnepinnen vår. Operasjonen består i å fylle diskplassen på USB-pinnen vår med 0-er.



**Sørg for at du velger riktig enhetsfil!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Dette sikrer at det ikke finnes vedvarende klartekstdata på nøkkelen vår.



### C. Krypter USB-nøkkelen med LUKS



Vi skal nå initialisere LUKS-partisjonen på USB-nøkkelen vår. Dette innebærer å opprette LUKS-partisjonen:



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



Her initialiserer og formaterer underkommandoen "`luksFormat`" enheten slik at den bruker LUKS-kryptering. Du blir bedt om å bekrefte denne operasjonen ved å skrive `YES` med store bokstaver, og deretter definere en *passphrase*. **Velg en robust *passphrase* for å sikre at angriperen ikke kan oppdage den via brute-force-angrep i tilfelle den går tapt.



Etter dette vil disken "**/dev/sdb**" være formatert med LUKS og klar til å brukes som et kryptert volum.



### D. Formater kryptert volum



Vi er nesten i mål, og nå må vi opprette en gyldig partisjon innenfor LUKS-partisjonen vår. På denne måten kan vi bruke den som et hvilket som helst annet filsystem når den er låst opp. For å gjøre dette må vi åpne den krypterte partisjonen:



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



Her er "**usbkey1**" navnet jeg gir til partisjonsmonteringen i min kontekst. Du kan velge hva du vil. Deretter må vi formatere denne partisjonen i LUKS-partisjonen, for eksempel her som **ext4** :



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



**Her er målplasseringen** spesifisert som "**/dev/mappe/usbkey1**"**, hvorfor?



"**/dev/mapper/usbkey1**" er "snarveien" vi har gitt til USB-nøkkelen vår ("**/dev/mapper**" er generisk for Linux for mapping). Den gir derfor tilgang til den dekrypterte partisjonen vår. Her er hva du skal se nå :



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



## IV. Bruk av den krypterte USB-nøkkelen



### A. Åpne og rediger LUKS-volumet



**Via Interface-grafikk** **:**



Under Debian er "**dm-crypt**" til stede som standard. Så i de fleste tilfeller skjer installasjonen direkte når USB-nøkkelen plugges inn. Du vil da bli bedt om å skrive inn din passphrase i et popup-vindu som dette:



![Image](assets/fr/018.webp)



Forespørsel om å angi dekryptering passphrase for LUKS-partisjonen.



Når passphrase er tastet inn, vil systemet ditt kunne lese filsystemet på nøkkelen og deretter montere dette filsystemet, noe som vil vise vår monterte partisjon:



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



**På kommandolinjen:**



Det er imidlertid verdt å vite hvordan du utfører operasjonen på kommandolinjen. La oss starte med å dekryptere den krypterte partisjonen ved hjelp av "**crypsetup**" og underkommandoen "**luksOpen**":



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



Nå er det dekrypterte volumet på USB-minnepinnen vår et volum som filsystemet og operativsystemet vårt kan bruke, så vi monterer innholdet i en hvilken som helst mappe, for eksempel "**/home/mickael/mnt**" i mitt tilfelle:



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



Det betyr at vi har fri og åpen tilgang til dataene på USB-pinnen vår.



### B. Lukk og fjern LUKS-volumet



Når operasjonen er fullført, må du ikke glemme å lukke alt ordentlig for å sikre at vi ikke ødelegger volumet vårt. Det første trinnet er å avmontere :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Deretter lukker du selve den krypterte partisjonen:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Nå vil alle som bruker USB-nøkkelen vår, ikke se noe av innholdet, bortsett fra krypterte data.



## V. Konklusjon



Grafiske brukergrensesnitt gjør denne operasjonen gjennomsiktig, men det er likevel nyttig å vite hvordan man formaterer, oppretter, åpner og lukker en kryptert LUKS-partisjon fra kommandolinjen. Når en LUKS-partisjon først er formatert, er manipulasjonene som kreves for å åpne og lukke den, minimale sammenlignet med sikkerhetsgevinsten.