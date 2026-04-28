---
name: LUKS
description: La crittografia di una chiavetta USB con LUKS e cryptsetup
---
![cover](assets/cover.webp)

___

*Questa esercitazione si basa su un contenuto originale di Mickael Dorigny pubblicato su [IT-Connect](https://www.it-connect.fr/). Licenza [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Possono essere state apportate modifiche al testo originale.*

___


## I. Presentazione

La crittografia di una chiavetta USB è un buon modo per proteggere i dati sensibili. **In questa esercitazione vedremo come utilizzare LUKS (*Linux Unified Key Setup*) con cryptsetup per crittografare una chiavetta USB su un sistema Linux.** Questo metodo ti permetterà di proteggere i tuoi dati, soprattutto in caso di perdita o furto della chiavetta USB.

[**LUKS**](https://it.wikipedia.org/wiki/Linux_Unified_Key_Setup) (*Linux Unified Key Setup*) è uno standard di crittografia del disco utilizzato principalmente nei sistemi Linux. Protegge i dati criptando le partizioni del disco con algoritmi robusti. Il suo supporto sui sistemi Linux facilita la gestione delle chiavi di crittografia e delle password, offrendo un interfaccia standardizzata e la compatibilità con vari strumenti di gestione.

Per seguire questa esercitazione, è necessario avere:
- una chiave uSB;
- un sistema Linux con "**cryptsetup**" installato (spesso disponibile di default, altrimenti vedremo come ottenerlo).


## II. Installazione di cryptsetup

Per prima cosa, dobbiamo assicurarci di avere il comando "**cryptsetup**" sul nostro sistema:

```
# Verifica la presenza del comando cryptsetup
which cryptsetup
```

Se non si ottiene risposta a questo comando, è necessario installare "**cryptsetup**":

```
# Installer cryptsetup
# Su Debian e derivate
apt-get install cryptsetup

# Su Redhat e derivate
sudo yum install cryptsetup
# o
sudo dnf install cryptsetup
```

Ora abbiamo tutto ciò che ci serve per creare la nostra chiave USB crittografata tramite LUKS.

In realtà, è l'utilità "**dm-crypt**" a svolgere il lavoro di crittografia. "**cryptsetup**" è un interfaccia a riga di comando che gestisce le funzioni e le azioni di **dm-crypt**.


## III. Creazione della partizione e del file system LUKS

### A. Identificare la chiave USB

Ora creeremo una partizione LUKS crittografata sulla nostra chiavetta USB. Se non l'avete ancora collegata al sistema, è il momento di farlo.

Ai fini di questa esercitazione, sto crittografando l'intera chiavetta USB, non solo una partizione. È inoltre importante sapere che durante questa procedura, **tutti i dati esistenti verranno cancellati dalla chiave**.

Il primo passo consiste nell'individuare il file del dispositivo corrispondente alla chiavetta USB nella directory "**/dev/**". Inserisci la chiavetta USB e identifica il nome del dispositivo. È possibile utilizzare il seguente comando per elencare i dispositivi di archiviazione:

```
$ lsblk
```

Individua la chiave USB, ad esempio "**/dev/sdb**". È anche possibile utilizzare il comando "**fdisk -l**" per visualizzare il nome del modello di chiave USB (è meglio non sbagliare) e utilizzare le dimensioni del dispositivo come indicatore:

![Image](assets/fr/019.webp)

Identifica la chiave USB da crittografare con "**lsblk**" e "**fdisk**".

Nel mio esempio, la mia chiave USB si trova in "**/dev/sdb**". Se vedete "**/dev/sdb1**", "**/dev/sdb2**" e così via, queste sono le partizioni attualmente presenti sull'unità. Verranno eliminate dalla nostra operatività.

### B. Cancella i dati esistenti

Ora cancellerai tutti i dati presenti sulla tua chiavetta USB. L'operazione consiste nel riempire di 0 lo spazio su disco della nostra chiavetta USB.

**Assicurarsi di puntare al file del dispositivo giusto!**

```
# Riempire la chiave USB di 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```

In questo modo si garantisce che non ci saranno dati in chiaro persistenti sulla tua chiave.

### C. Crittografa la chiave USB con LUKS

Ora inizializzerai la partizione LUKS sulla tua chiave USB. Questo comporta la creazione della partizione LUKS:

```
# Formattazione di una partizione LUKS sulla chiavetta USB
$ sudo cryptsetup luksFormat /dev/sdb

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type 'yes' in capital letters): YES
Enter passphrase for /dev/sdb:
Verify passphrase:
```

Qui, il sottocomando "`luksFormat`" inizializza e formatta il dispositivo per utilizzare la crittografia LUKS. Verrà richiesto di confermare l'operazione digitando `YES` in maiuscolo, quindi di definire una *passphrase*. **Scegliere una *passphrase* robusta per garantire che, in caso di perdita, l'aggressore non possa scoprirla tramite attacchi di forza bruta.**

Al termine di questa operazione, il disco "**/dev/sdb**" sarà formattato con LUKS e pronto per essere utilizzato come volume crittografato.

### D. Formattare il volume crittografato

Ci siamo quasi e ora dobbiamo creare una partizione valida all'interno della nostra partizione LUKS. In questo modo, una volta sbloccata, potremo utilizzarla come qualsiasi altro file system. Per farlo, dobbiamo aprire la partizione crittografata:

```
# Apertura della partizione LUKS sulla chiavetta USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Lista dei dischi
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

Qui, "**usbkey1**" è il nome che do al montaggio della partizione nel mio contesto. Potete scegliere quello che preferite. Occorre poi formattare la partizione contenuta nella partizione LUKS, ad esempio qui come **ext4**:

```
# Formattazione della partizione in ext4
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

**Qui la posizione di destinazione** è specificata come "**/dev/mappe/usbkey1**", perché?

"**/dev/mapper/usbkey1**" è la "scorciatoia" che abbiamo dato alla nostra chiave USB ("**/dev/mapper**" è generico per Linux per la mappatura). Fornisce quindi l'accesso alla nostra partizione decriptata. Ecco cosa si dovrebbe vedere ora:

```
# Lista delle periferiche e le loro partizioni
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

### A. Apri e modifica il volume LUKS

**Via interfaccia grafica**:

In Debian, "**dm-crypt**" è presente per impostazione predefinita. Quindi, nella maggior parte dei casi, l'installazione avviene direttamente quando si inserisce la chiave USB. Verrà quindi richiesto di inserire la propria passphrase in una finestra pop-up come questa:

![Image](assets/fr/018.webp)

Richiesta di inserimento della passphrase di decodifica per la partizione LUKS.

Una volta inserita la passphrase, il sistema sarà in grado di leggere il file system sulla chiave e di montarlo, mostrando la partizione montata:

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
# Apertura della partizione LUKS sulla chiavetta USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Lista delle periferiche e delle loro partizioni
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
[...]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```

Ora, il volume decrittografato della nostra chiavetta USB presenta un volume che il nostro file system e il sistema operativo possono utilizzare, quindi monteremo il suo contenuto in una cartella qualsiasi, ad esempio "**/home/mickael/mnt**" nel mio caso:

```
# Monta il volume decifrato sul tuo file system
$ mkdir /home/mickael/mnt
$ sudo mount /dev/mapper/usbkey1 /home/mickael/mnt

$ ls /home/mickael/mnt -al
total 24
drwxr-xr-x  3 root    root     4096 Jun 11 14:38 .
drwx------ 31 mickael mickael  4096 Jun 11 21:44 ..
drwx------  2 root    root    16384 Jun 11 14:38 lost+found

```

Ciò significa che puoi accedere ai dati della tua chiavetta USB in modo libero e trasparente.

### B. Chiudi e rimuovi il volume LUKS

Una volta completata l'operazione, non dimenticare di chiudere tutto correttamente per essere sicuro di non danneggiare il volume. Il primo passo è smontare il file:

```
# Smontaggio del volume contenente la partizione cifrata
sudo umount /home/mickael/mnt
```

Quindi chiudi la partizione crittografata:

```
# Chiusura della partizione cifrata
sudo cryptsetup luksClose usbkey1
```

Ora, chiunque utilizzi la nostra chiave USB non vedrà nulla del suo contenuto, tranne i dati crittografati.


## V. Conclusione

Le interfacce grafiche rendono questa operazione trasparente, ma è comunque utile sapere come formattare, creare, aprire e chiudere una partizione LUKS crittografata dalla riga di comando. Una volta formattata, le manipolazioni necessarie per aprire e chiudere una partizione LUKS sono minime rispetto ai vantaggi in termini di sicurezza.
