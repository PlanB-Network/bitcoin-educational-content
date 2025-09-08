---
name: LUKS
description: Szyfrowanie pamięci flash USB za pomocą LUKS i cryptsetup
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści Mickaela Dorigny'ego opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



Szyfrowanie pamięci USB to dobry sposób na ochronę poufnych danych. **W tym poradniku przyjrzymy się, jak używać LUKS (*Linux Unified Key Setup*) z cryptsetup do szyfrowania pamięci USB w systemie Linux.** Ta metoda pozwoli ci zabezpieczyć dane, szczególnie w przypadku utraty lub kradzieży pamięci USB.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) to standard szyfrowania dysków używany głównie w systemach Linux. Zabezpiecza on dane poprzez szyfrowanie partycji dyskowych za pomocą solidnych algorytmów. Jego obsługa w systemach Linux ułatwia zarządzanie kluczami szyfrowania i hasłami, oferując znormalizowane Interface i kompatybilność z różnymi narzędziami do zarządzania.



Aby skorzystać z tego samouczka, będziesz potrzebować:





- klucz uSB;
- system Linux z zainstalowanym "**cryptsetup**" (często dostępny domyślnie, w przeciwnym razie zobaczymy, jak go uzyskać).



## II. Instalacja cryptsetup



Po pierwsze, musimy upewnić się, że mamy w systemie polecenie "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Jeśli nie otrzymasz odpowiedzi na to polecenie, musisz zainstalować "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Mamy teraz wszystko, czego potrzebujemy, aby utworzyć nasz zaszyfrowany klucz USB za pośrednictwem LUKS.



W rzeczywistości jest to narzędzie "**dm-crypt**", które wykona pracę szyfrowania. "**cryptsetup**" to Interface wiersza poleceń, który zarządza funkcjami i działaniami **dm-crypt**.



## III. Tworzenie partycji LUKS i systemu plików



### A. Zidentyfikuj klucz USB



Teraz utworzymy zaszyfrowaną partycję LUKS na naszej pamięci USB. Jeśli jeszcze nie podłączyłeś go do systemu, nadszedł czas, aby to zrobić.



Na potrzeby tego samouczka szyfruję całą pamięć USB, a nie tylko jedną partycję. Ważne jest również, aby wiedzieć, że podczas tej procedury **wszystkie istniejące dane zostaną usunięte z klucza**.



Pierwszym krokiem jest zlokalizowanie pliku urządzenia odpowiadającego pamięci USB w katalogu "**/dev/**". Włóż pamięć USB i zidentyfikuj nazwę urządzenia. Możesz użyć następującego polecenia, aby wyświetlić listę urządzeń pamięci masowej:



```
$ lsblk
```



Zlokalizuj swój klucz USB, na przykład "**/dev/sdb**". Możesz również użyć polecenia "**fdisk -l**", aby wyświetlić nazwę modelu klucza USB (najlepiej nie popełnić błędu) i użyć rozmiaru pamięci urządzenia jako wskaźnika:



![Image](assets/fr/019.webp)



Zidentyfikuj klucz USB do zaszyfrowania za pomocą "**lsblk**" i "**fdisk**".



W moim przykładzie mój klucz USB znajduje się w "**/dev/sdb**". Jeśli widzisz "**/dev/sdb1**", "**/dev/sdb2**" itp., są to partycje aktualnie znajdujące się na dysku. Są to partycje aktualnie znajdujące się na kluczu. Zostaną one usunięte przez naszą manipulację.



### B. Usuń istniejące dane



Teraz usuniemy wszystkie dane z naszej pamięci USB. Operacja polega na wypełnieniu miejsca na dysku naszej pamięci USB zerami.



**Upewnij się, że wybierasz właściwy plik urządzenia!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Gwarantuje to, że na naszym kluczu nie będzie żadnych trwałych danych w postaci zwykłego tekstu.



### C. Zaszyfruj klucz USB za pomocą LUKS



Teraz zainicjujemy partycję LUKS na naszym kluczu USB. Obejmuje to utworzenie partycji LUKS:



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



Tutaj podkomenda "`luksFormat`" inicjalizuje i formatuje urządzenie do korzystania z szyfrowania LUKS. Zostaniesz poproszony o potwierdzenie tej operacji poprzez wpisanie `YES` wielkimi literami, a następnie zdefiniowanie *passphrase*. **Wybierz solidny *passphrase*, aby upewnić się, że w przypadku utraty atakujący nie będzie mógł go wykryć za pomocą ataków siłowych.



Następnie dysk "**/dev/sdb**" zostanie sformatowany przy użyciu LUKS i będzie gotowy do użycia jako zaszyfrowany wolumin.



### D. Formatowanie zaszyfrowanego woluminu



Jesteśmy prawie na miejscu, a teraz musimy utworzyć prawidłową partycję na naszej partycji LUKS. W ten sposób, po odblokowaniu, możemy używać go jak każdego innego systemu plików. Aby to zrobić, musimy otworzyć zaszyfrowaną partycję:



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



Tutaj "**usbkey1**" to nazwa, którą nadaję partycji montowanej w moim kontekście. Możesz wybrać dowolną. Następnie musimy sformatować tę partycję zawartą w partycji LUKS, na przykład tutaj jako **ext4**:



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



**Tutaj lokalizacja docelowa** jest określona jako "**/dev/mappe/usbkey1**"**, dlaczego?



"**/dev/mapper/usbkey1**" to "skrót", który nadaliśmy naszemu kluczowi USB ("**/dev/mapper**" jest ogólny dla Linuksa do mapowania). Zapewnia on zatem dostęp do naszej odszyfrowanej partycji. Oto, co powinieneś teraz zobaczyć:



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



## IV. Korzystanie z zaszyfrowanego klucza USB



### A. Otwórz i edytuj wolumin LUKS



**Via Interface graphic** **:**



Pod Debianem "**dm-crypt**" jest domyślnie obecny. Tak więc w większości przypadków instalacja odbywa się bezpośrednio po podłączeniu klucza USB. Następnie zostaniesz poproszony o wprowadzenie passphrase w wyskakującym okienku, takim jak to:



![Image](assets/fr/018.webp)



Żądanie wprowadzenia deszyfrowania passphrase dla partycji LUKS.



Po wprowadzeniu passphrase system będzie mógł odczytać system plików na kluczu, a następnie zamontować ten system plików, co pokaże naszą zamontowaną partycję:



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



**W wierszu poleceń:**



Warto jednak wiedzieć, jak wykonać operację w wierszu poleceń. Zacznijmy od odszyfrowania zaszyfrowanej partycji za pomocą "**crypsetup**" i podkomendy "**luksOpen**":



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



Teraz odszyfrowany wolumin naszego dysku flash USB stanowi wolumin, z którego może korzystać nasz system plików i system operacyjny, więc zamontujemy jego zawartość w dowolnym folderze, na przykład "**/home/mickael/mnt**" w moim przypadku:



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



Oznacza to, że możemy uzyskać swobodny i przejrzysty dostęp do danych na naszej pamięci USB.



### B. Zamknij i usuń wolumin LUKS



Po zakończeniu naszej operacji nie zapomnij zamknąć wszystkiego poprawnie, aby upewnić się, że nie uszkodzimy naszego woluminu. Pierwszym krokiem jest odmontowanie woluminu:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Następnie zamknij zaszyfrowaną partycję:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Teraz każdy, kto korzysta z naszego klucza USB, nie zobaczy nic z jego zawartości poza zaszyfrowanymi danymi.



## V. Wnioski



Graficzne interfejsy użytkownika sprawiają, że operacja ta jest przejrzysta, ale nadal warto wiedzieć, jak sformatować, utworzyć, otworzyć i zamknąć zaszyfrowaną partycję LUKS z wiersza poleceń. Po sformatowaniu, manipulacje wymagane do otwarcia i zamknięcia partycji LUKS są minimalne w porównaniu z zyskami bezpieczeństwa.