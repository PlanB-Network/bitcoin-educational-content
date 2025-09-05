---
name: LUKS
description: Verschlüsseln eines USB-Sticks mit LUKS und cryptsetup
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Mickael Dorigny, die auf [IT-Connect](https://www.it-connect.fr/) veröffentlicht wurden. Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



Die Verschlüsselung eines USB-Sticks ist ein guter Weg, um Ihre sensiblen Daten zu schützen. **In diesem Tutorial zeigen wir Ihnen, wie Sie LUKS (*Linux Unified Key Setup*) mit cryptsetup verwenden, um einen USB-Stick auf einem Linux-System zu verschlüsseln.** Mit dieser Methode können Sie Ihre Daten schützen, insbesondere bei Verlust oder Diebstahl des USB-Sticks.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) ist ein Standard zur Festplattenverschlüsselung, der hauptsächlich auf Linux-Systemen verwendet wird. Er sichert Daten durch Verschlüsselung von Festplattenpartitionen mit robusten Algorithmen. Seine Unterstützung auf Linux-Systemen erleichtert die Verwaltung von Verschlüsselungsschlüsseln und Passwörtern und bietet standardisierte Interface und Kompatibilität mit verschiedenen Verwaltungstools.



Für dieses Tutorial benötigen Sie:





- uSB-Schlüssel;
- ein Linux-System, auf dem "**cryptsetup**" installiert ist (oft standardmäßig vorhanden, andernfalls werden wir sehen, wie man es bekommt).



## II. Installation von cryptsetup



Zunächst müssen wir sicherstellen, dass der Befehl **cryptsetup**" auf unserem System vorhanden ist:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Wenn Sie keine Antwort auf diesen Befehl erhalten, müssen Sie "**cryptsetup**" installieren:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Jetzt haben wir alles, was wir brauchen, um unseren verschlüsselten USB-Schlüssel über LUKS zu erstellen.



In Wirklichkeit ist es das Dienstprogramm "**dm-crypt**", das die Verschlüsselung vornimmt. "**cryptsetup**" ist ein Kommandozeilen-Interface, das die Funktionen und Aktionen von **dm-crypt** verwaltet.



## III. Erstellen der LUKS-Partition und des Dateisystems



### A. Identifizieren Sie den USB-Stick



Wir werden nun eine verschlüsselte LUKS-Partition auf unserem USB-Stick erstellen. Wenn Sie ihn noch nicht an Ihr System angeschlossen haben, ist jetzt der richtige Zeitpunkt dafür.



Für die Zwecke dieses Tutorials verschlüssele ich meinen gesamten USB-Stick, nicht nur eine Partition. Es ist auch wichtig zu wissen, dass während dieses Vorgangs **alle vorhandenen Daten auf dem Stick gelöscht werden**.



Der erste Schritt besteht darin, die Gerätedatei, die Ihrem USB-Stick entspricht, im Verzeichnis "**/dev/**" zu suchen. Stecken Sie Ihren USB-Stick ein und identifizieren Sie seinen Gerätenamen. Sie können den folgenden Befehl verwenden, um Speichergeräte aufzulisten:



```
$ lsblk
```



Suchen Sie Ihren USB-Stick, zum Beispiel "**/dev/sdb**". Sie können auch den Befehl "**fdisk -l**" verwenden, um den Namen des USB-Stick-Modells anzuzeigen (achten Sie darauf, keinen Fehler zu machen), und die Speichergröße des Geräts als Indikator verwenden:



![Image](assets/fr/019.webp)



Identifizieren Sie den zu verschlüsselnden USB-Stick mit "**lsblk**" und "**fdisk**".



In meinem Beispiel befindet sich mein USB-Stick in "**/dev/sdb**". Wenn Sie "**/dev/sdb1**", "**/dev/sdb2**" usw. sehen, sind dies die Partitionen, die sich derzeit auf Ihrem Laufwerk befinden. Dies sind die Partitionen, die sich derzeit auf Ihrem Schlüssel befinden. Sie werden durch unsere Manipulation gelöscht.



### B. Vorhandene Daten löschen



Wir werden nun alle Daten auf unserem USB-Stick löschen. Der Vorgang besteht darin, den Speicherplatz auf unserem USB-Stick mit 0en zu füllen.



**Achten Sie darauf, dass Sie die richtige Gerätedatei auswählen!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Dadurch wird sichergestellt, dass keine dauerhaften Klartextdaten auf unserem Schlüssel vorhanden sind.



### C. Verschlüsseln Sie den USB-Stick mit LUKS



Wir werden nun die LUKS-Partition auf unserem USB-Stick initialisieren. Dazu muss die LUKS-Partition erstellt werden:



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



Hier initialisiert und formatiert der Unterbefehl "`luksFormat`" das Gerät für die Verwendung von LUKS-Verschlüsselung. Sie werden aufgefordert, diesen Vorgang durch Eingabe von `YES` in Großbuchstaben zu bestätigen und dann eine *passphrase* zu definieren. **Wählen Sie eine robuste *passphrase*, um sicherzustellen, dass ein Angreifer sie im Falle eines Verlustes nicht durch Brute-Force-Angriffe herausfinden kann.



Danach wird der Datenträger "**/dev/sdb**" mit LUKS formatiert und kann als verschlüsselter Datenträger verwendet werden.



### D. Verschlüsseltes Volume formatieren



Wir haben es fast geschafft und müssen nun noch eine gültige Partition innerhalb unserer LUKS-Partition erstellen. Auf diese Weise können wir sie, sobald sie entsperrt ist, wie jedes andere Dateisystem verwenden. Zu diesem Zweck müssen wir die verschlüsselte Partition öffnen:



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



In diesem Fall ist "**usbkey1**" der Name, den ich der Partitionseinbindung in meinem Kontext gebe. Sie können jeden Namen wählen, den Sie möchten. Dann müssen wir diese Partition, die in der LUKS-Partition enthalten ist, formatieren, zum Beispiel hier als **ext4**:



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



**Hier ist der Zielspeicherort** als "**/dev/mappe/usbkey1**"** angegeben, warum?



"**/dev/mapper/usbkey1**" ist die "Abkürzung", die wir unserem USB-Stick gegeben haben ("**/dev/mapper**" ist ein allgemeiner Begriff für Linux für die Zuordnung). Er ermöglicht also den Zugriff auf unsere entschlüsselte Partition. Hier ist, was Sie jetzt sehen sollten:



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



## IV. Verwendung des verschlüsselten USB-Sticks



### A. LUKS-Volumen öffnen und bearbeiten



**Via Interface Grafik** **:**



Unter Debian ist "**dm-crypt**" standardmäßig vorhanden. Daher erfolgt die Installation in den meisten Fällen direkt, wenn der USB-Stick eingesteckt wird. Sie werden dann in einem Pop-up-Fenster wie diesem aufgefordert, Ihren passphrase einzugeben:



![Image](assets/fr/018.webp)



Aufforderung zur Eingabe der Entschlüsselung passphrase für die LUKS-Partition.



Sobald die passphrase eingegeben wurde, kann Ihr System das Dateisystem auf dem Schlüssel lesen und dieses Dateisystem einhängen, wodurch unsere eingehängte Partition angezeigt wird:



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



**Auf der Befehlszeile:**



Es lohnt sich jedoch zu wissen, wie man die Operation auf der Kommandozeile durchführt. Beginnen wir mit der Entschlüsselung der verschlüsselten Partition mit "**crypsetup**" und dem Unterbefehl "**luksOpen**":



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



Das entschlüsselte Volume unseres USB-Sticks stellt nun ein Volume dar, das unser Dateisystem und das Betriebssystem verwenden können, also werden wir seinen Inhalt in einen beliebigen Ordner mounten, in meinem Fall zum Beispiel "**/home/mickael/mnt**":



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



Das bedeutet, dass wir frei und transparent auf die Daten auf unserem USB-Stick zugreifen können.



### B. LUKS-Volumen schließen und entfernen



Sobald unsere Operation abgeschlossen ist, vergessen Sie nicht, alles ordnungsgemäß zu schließen, um sicherzustellen, dass wir unser Volume nicht beschädigen. Der erste Schritt ist das Aushängen der:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Schließen Sie dann die verschlüsselte Partition selbst:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Jeder, der unseren USB-Stick benutzt, sieht nichts von seinem Inhalt außer den verschlüsselten Daten.



## V. Schlussfolgerung



Grafische Benutzeroberflächen machen diesen Vorgang transparent, aber es ist dennoch nützlich zu wissen, wie man eine verschlüsselte LUKS-Partition über die Befehlszeile formatiert, erstellt, öffnet und schließt. Einmal formatiert, sind die zum Öffnen und Schließen einer LUKS-Partition erforderlichen Manipulationen im Vergleich zum Sicherheitsgewinn minimal.