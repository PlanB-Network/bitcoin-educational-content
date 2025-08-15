---
name: LUCCI
description: Crittografia di una chiavetta USB con LUKS e cryptsetup
---
![cover](assets/cover.webp)



___



*Questa esercitazione si basa su un contenuto originale di Mickael Dorigny pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale



___



## I. Presentazione



La crittografia di una chiavetta USB è un buon modo per proteggere i dati sensibili. **In questa esercitazione vedremo come utilizzare LUKS (*Linux Unified Key Setup*) con cryptsetup per crittografare una chiavetta USB su un sistema Linux.** Questo metodo vi permetterà di proteggere i vostri dati, soprattutto in caso di perdita o furto della chiavetta USB.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) è uno standard di crittografia del disco utilizzato principalmente nei sistemi Linux. Protegge i dati criptando le partizioni del disco con algoritmi robusti. Il suo supporto sui sistemi Linux facilita la gestione delle chiavi di crittografia e delle password, offrendo un Interface standardizzato e la compatibilità con vari strumenti di gestione.



Per seguire questa esercitazione, è necessario :





- chiave uSB;
- un sistema Linux con "**cryptsetup**" installato (spesso disponibile di default, altrimenti vedremo come ottenerlo).



## II. Installazione di cryptsetup



Per prima cosa, dobbiamo assicurarci di avere il comando "**cryptsetup**" sul nostro sistema:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Se non si ottiene risposta a questo comando, è necessario installare "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Ora abbiamo tutto ciò che ci serve per creare la nostra chiave USB crittografata tramite LUKS.



In realtà, è l'utilità "**dm-crypt**" a svolgere il lavoro di crittografia. "**cryptsetup**" è un Interface a riga di comando che gestisce le funzioni e le azioni di **dm-crypt**.



## III. Creazione della partizione e del file system LUKS



### A. Identificare la chiave USB



Ora creeremo una partizione LUKS crittografata sulla nostra chiavetta USB. Se non l'avete ancora collegata al sistema, è il momento di farlo.



Ai fini di questa esercitazione, sto crittografando l'intera chiavetta USB, non solo una partizione. È inoltre importante sapere che durante questa procedura, **tutti i dati esistenti verranno cancellati dalla chiave**.



Il primo passo consiste nell'individuare il file del dispositivo corrispondente alla chiavetta USB nella directory "**/dev/**". Inserire la chiavetta USB e identificare il nome del dispositivo. È possibile utilizzare il seguente comando per elencare i dispositivi di archiviazione:



```
$ lsblk
```



Individuare la chiave USB, ad esempio "**/dev/sdb**". È anche possibile utilizzare il comando "**fdisk -l**" per visualizzare il nome del modello di chiave USB (è meglio non sbagliare) e utilizzare le dimensioni del dispositivo come indicatore:



![Image](assets/fr/019.webp)



Identificare la chiave USB da crittografare con "**lsblk**" e "**fdisk**".



Nel mio esempio, la mia chiave USB si trova in "**/dev/sdb**". Se vedete "**/dev/sdb1**", "**/dev/sdb2**" e così via, queste sono le partizioni attualmente presenti sull'unità. Queste sono le partizioni attualmente presenti sulla chiave. Verranno eliminate dalla nostra manipolazione.



### B. Cancellare i dati esistenti



Ora cancelleremo tutti i dati presenti sulla nostra chiavetta USB. L'operazione consiste nel riempire di 0 lo spazio su disco della nostra chiavetta USB.



**Assicurarsi di puntare al file del dispositivo giusto!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



In questo modo si garantisce che non ci saranno dati in chiaro persistenti sulla nostra chiave.



### C. Crittografare la chiave USB con LUKS



Ora inizializzeremo la partizione LUKS sulla nostra chiave USB. Questo comporta la creazione della partizione LUKS:



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



Qui, il sottocomando "`luksFormat`" inizializza e formatta il dispositivo per utilizzare la crittografia LUKS. Verrà richiesto di confermare l'operazione digitando `YES` in maiuscolo, quindi di definire un *passphrase*. **Scegliere un *passphrase* robusto per garantire che, in caso di perdita, l'aggressore non possa scoprirlo tramite attacchi di forza bruta.



Al termine di questa operazione, il disco "**/dev/sdb**" sarà formattato con LUKS e pronto per essere utilizzato come volume crittografato.



### D. Formattare il volume crittografato



Ci siamo quasi e ora dobbiamo creare una partizione valida all'interno della nostra partizione LUKS. In questo modo, una volta sbloccata, potremo utilizzarla come qualsiasi altro file system. Per farlo, dobbiamo aprire la partizione crittografata:



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



Qui, "**usbkey1**" è il nome che do al montaggio della partizione nel mio contesto. Potete scegliere quello che preferite. Occorre poi formattare la partizione contenuta nella partizione LUKS, ad esempio qui come **ext4** :



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



**Qui la posizione di destinazione** è specificata come "**/dev/mappe/usbkey1**"**, perché?



"**/dev/mapper/usbkey1**" è la "scorciatoia" che abbiamo dato alla nostra chiave USB ("**/dev/mapper**" è generico per Linux per la mappatura). Fornisce quindi l'accesso alla nostra partizione decriptata. Ecco cosa si dovrebbe vedere ora:



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



## IV. Utilizzo della chiave USB crittografata



### A. Aprire e modificare il volume LUKS



**Via Interface graphic** **:**



In Debian, "**dm-crypt**" è presente per impostazione predefinita. Quindi, nella maggior parte dei casi, l'installazione avviene direttamente quando si inserisce la chiave USB. Verrà quindi richiesto di inserire il proprio passphrase in una finestra pop-up come questa:



![Image](assets/fr/018.webp)



Richiesta di inserimento della decodifica passphrase per la partizione LUKS.



Una volta inserito il passphrase, il sistema sarà in grado di leggere il file system sulla chiave e di montarlo, mostrando la partizione montata:



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



**Sulla linea di comando:**



Tuttavia, vale la pena di sapere come eseguire l'operazione alla riga di comando. Cominciamo a decifrare la partizione criptata usando "**crypsetup**" e il sottocomando "**luksOpen**":



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



Ora, il volume decrittografato della nostra chiavetta USB presenta un volume che il nostro file system e il sistema operativo possono utilizzare, quindi monteremo il suo contenuto in una cartella qualsiasi, ad esempio "**/home/mickael/mnt**" nel mio caso:



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



Ciò significa che possiamo accedere ai dati della nostra chiavetta USB in modo libero e trasparente.



### B. Chiudere e rimuovere il volume LUKS



Una volta completata l'operazione, non dimenticate di chiudere tutto correttamente per essere sicuri di non danneggiare il volume. Il primo passo è smontare il file :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Quindi chiudere la partizione crittografata:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Ora, chiunque utilizzi la nostra chiave USB non vedrà nulla del suo contenuto, tranne i dati crittografati.



## V. Conclusione



Le interfacce grafiche rendono questa operazione trasparente, ma è comunque utile sapere come formattare, creare, aprire e chiudere una partizione LUKS crittografata dalla riga di comando. Una volta formattata, le manipolazioni necessarie per aprire e chiudere una partizione LUKS sono minime rispetto ai vantaggi in termini di sicurezza.