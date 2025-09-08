---
name: LUKS
description: Šifrování jednotky USB flash pomocí LUKS a nástroje cryptsetup
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Mickaela Dorignyho zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



Šifrování USB flash disku je dobrým způsobem ochrany citlivých dat. **V tomto návodu se podíváme na to, jak pomocí LUKS (*Linux Unified Key Setup*) s programem cryptsetup zašifrovat USB disk v systému Linux.** Tato metoda vám umožní zabezpečit vaše data, zejména v případě ztráty nebo krádeže USB disku.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) je standard pro šifrování disků používaný především v systémech Linux. Zabezpečuje data šifrováním diskových oddílů pomocí robustních algoritmů. Jeho podpora v systémech Linux usnadňuje správu šifrovacích klíčů a hesel, nabízí standardizovaný Interface a kompatibilitu s různými nástroji pro správu.



K provedení tohoto návodu budete potřebovat:





- uSB klíč;
- systém Linux s nainstalovaným programem "**cryptsetup**" (často je k dispozici ve výchozím nastavení, jinak se podíváme, jak jej získat).



## II. Instalace programu cryptsetup



Nejprve se musíme ujistit, že máme v systému příkaz "**cryptsetup**":



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Pokud na tento příkaz nedostanete žádnou odpověď, je třeba nainstalovat příkaz "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Nyní máme vše, co potřebujeme k vytvoření šifrovaného klíče USB prostřednictvím LUKS.



Ve skutečnosti se o šifrování stará nástroj "**dm-crypt**". "**cryptsetup**" je příkazový řádek Interface, který spravuje funkce a akce nástroje **dm-crypt**.



## III. Vytvoření oddílu a souborového systému LUKS



### A. Identifikace klíče USB



Nyní vytvoříme na našem disku USB šifrovaný oddíl LUKS. Pokud jste jej ještě nepřipojili k systému, je nejvyšší čas tak učinit.



Pro účely tohoto návodu zašifruji celý disk USB, nikoli pouze jeden oddíl. Je také důležité vědět, že během tohoto postupu budou z klíče **vymazána všechna existující data**.



Prvním krokem je vyhledání souboru zařízení odpovídajícího vašemu klíči USB v adresáři "**/dev/**". Vložte paměť USB a identifikujte název zařízení. Pro zobrazení seznamu úložných zařízení můžete použít následující příkaz:



```
$ lsblk
```



Najděte svůj klíč USB, například "**/dev/sdb**". Můžete také použít příkaz "**fdisk -l**", který zobrazí název modelu klíče USB (raději se nespleťte) a jako ukazatel použije velikost úložiště zařízení:



![Image](assets/fr/019.webp)



Identifikujte klíč USB, který má být zašifrován, pomocí "**lsblk**" a "**fdisk**".



V mém příkladu je můj klíč USB umístěn v adresáři "**/dev/sdb**". Pokud vidíte "**/dev/sdb1**", "**/dev/sdb2**" atd., jedná se o oddíly, které jsou aktuálně na vašem disku. Jedná se o oddíly aktuálně přítomné na vašem klíči. Při naší manipulaci budou odstraněny.



### B. Odstranění existujících dat



Nyní odstraníme všechna data na našem disku USB. Operace spočívá v tom, že místo na disku USB zaplníme nulami.



**Ujistěte se, že jste se zaměřili na správný soubor zařízení!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Tím je zajištěno, že na našem klíči nebudou žádná trvalá data v otevřeném textu.



### C. Šifrování klíče USB pomocí LUKS



Nyní inicializujeme oddíl LUKS na našem klíči USB. To zahrnuje vytvoření oddílu LUKS:



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



Zde se pomocí dílčího příkazu "`luksFormat`" inicializuje a naformátuje zařízení pro použití šifrování LUKS. Budete vyzváni k potvrzení této operace zadáním velkého písmene `YES` a poté definujte *passphrase*. **Zvolte robustní *passphrase*, abyste zajistili, že v případě ztráty jej útočník nebude moci odhalit pomocí útoků hrubou silou.



Poté bude disk "**/dev/sdb**" naformátován pomocí LUKS a připraven k použití jako šifrovaný svazek.



### D. Formátování zašifrovaného svazku



Jsme téměř u cíle a nyní musíme vytvořit platný oddíl v rámci našeho oddílu LUKS. Po odemčení jej tak můžeme používat jako jakýkoli jiný souborový systém. Za tímto účelem musíme zašifrovaný oddíl otevřít:



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



Zde je "**usbkey1**" název, který jsem dal připojení oddílu v mém kontextu. Můžete si zvolit, co se vám líbí. Poté musíme tento oddíl obsažený v oddílu LUKS naformátovat, například zde jako **ext4**:



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



**Tady je cílové umístění** zadáno jako "**/dev/mappe/usbkey1**"**, proč?



"**/dev/mapper/usbkey1**" je "zkratka", kterou jsme přidělili našemu klíči USB ("**/dev/mapper**" je pro Linux obecný název pro mapování). Poskytuje tedy přístup k našemu dešifrovanému oddílu. Zde je to, co byste nyní měli vidět:



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



## IV. Použití šifrovaného klíče USB



### A. Otevřete a upravte svazek LUKS



**Pomocí grafiky Interface** **:**



V Debianu je ve výchozím nastavení příkaz "**dm-crypt**". Ve většině případů tedy instalace probíhá přímo po připojení klíče USB. Poté budete vyzváni k zadání passphrase ve vyskakovacím okně, jako je toto:



![Image](assets/fr/018.webp)



Žádost o zadání dešifrování passphrase pro oddíl LUKS.



Po zadání kódu passphrase bude váš systém schopen přečíst souborový systém na klíči a poté tento souborový systém připojit, čímž se zobrazí náš připojený oddíl:



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



**Na příkazovém řádku:**



Vyplatí se však vědět, jak tuto operaci provést v příkazovém řádku. Začněme dešifrováním zašifrovaného oddílu pomocí příkazu "**crypsetup**" a dílčího příkazu "**luksOpen**":



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



Dešifrovaný svazek našeho USB flash disku nyní představuje svazek, který může náš souborový systém a operační systém používat, takže jeho obsah připojíme do libovolné složky, například "**/home/mickael/mnt**" v mém případě:



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



To znamená, že můžeme volně a transparentně přistupovat k datům na disku USB.



### B. Zavření a odebrání svazku LUKS



Po dokončení operace nezapomeňte vše řádně uzavřít, aby nedošlo k poškození svazku. Prvním krokem je odpojení souboru:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Poté zašifrovaný oddíl zavřete:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Kdokoli, kdo použije náš klíč USB, nyní neuvidí nic z jeho obsahu kromě zašifrovaných dat.



## V. Závěr



Grafické uživatelské rozhraní tuto operaci zpřehledňuje, ale přesto je užitečné vědět, jak formátovat, vytvářet, otevírat a zavírat šifrovaný oddíl LUKS z příkazového řádku. Po naformátování jsou manipulace nutné k otevření a zavření oddílu LUKS minimální v porovnání s přínosem pro zabezpečení.