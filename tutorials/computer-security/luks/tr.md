---
name: LUKS
description: LUKS ve cryptsetup ile bir USB flash sürücüyü şifreleme
---
![cover](assets/cover.webp)



___



*Bu eğitim Mickael Dorigny tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## I. Sunum



Bir USB belleği şifrelemek, hassas verilerinizi korumanın iyi bir yoludur. **Bu eğitimde, bir Linux sisteminde USB belleği şifrelemek için cryptsetup ile LUKS'un (*Linux Unified Key Setup*) nasıl kullanılacağına bir göz atacağız.** Bu yöntem, özellikle USB belleğinizin kaybolması veya çalınması durumunda verilerinizi güvence altına almanızı sağlayacaktır.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) esas olarak Linux sistemlerinde kullanılan bir disk şifreleme standardıdır. Disk bölümlerini sağlam algoritmalarla şifreleyerek verileri güvence altına alır. Linux sistemlerindeki desteği, standartlaştırılmış Interface ve çeşitli yönetim araçlarıyla uyumluluk sunarak şifreleme anahtarlarının ve parolalarının yönetimini kolaylaştırır.



Bu öğreticiyi takip etmek için ihtiyacınız olacak:





- uSB anahtarı;
- "**cryptsetup**" yüklü bir Linux sistemi (genellikle varsayılan olarak mevcuttur, aksi takdirde nasıl elde edeceğimizi göreceğiz).



## II. Cryptsetup'ı yükleme



İlk olarak, sistemimizde "**cryptsetup**" komutunun bulunduğundan emin olmamız gerekir:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Bu komuta yanıt alamazsanız, "**cryptsetup**" yüklemeniz gerekir:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Artık LUKS aracılığıyla şifrelenmiş USB anahtarımızı oluşturmak için ihtiyacımız olan her şeye sahibiz.



Gerçekte, şifreleme işini yapacak olan "**dm-crypt**" yardımcı programıdır. "**cryptsetup**", **dm-crypt**'in özelliklerini ve eylemlerini yöneten bir komut satırı Interface'dir.



## III. LUKS bölümünü ve dosya sistemini oluşturma



### A. USB anahtarını tanımlayın



Şimdi USB belleğimizde şifrelenmiş bir LUKS bölümü oluşturacağız. Henüz sisteminize bağlamadıysanız, şimdi bunu yapmanın tam zamanı.



Bu eğitimin amaçları doğrultusunda, sadece bir bölümü değil, tüm USB belleğimi şifreliyorum. Bu işlem sırasında **mevcut tüm verilerin anahtardan silineceğini** bilmek de önemlidir.



İlk adım, USB belleğinize karşılık gelen aygıt dosyasını "**/dev/**" dizininde bulmaktır. USB belleğinizi takın ve aygıt adını belirleyin. Depolama aygıtlarını listelemek için aşağıdaki komutu kullanabilirsiniz:



```
$ lsblk
```



USB anahtarınızı bulun, örneğin "**/dev/sdb**". USB anahtar modelinin adını görüntülemek için "**fdisk -l**" komutunu da kullanabilirsiniz (hata yapmamak en iyisidir) ve cihazın depolama boyutunu bir gösterge olarak kullanabilirsiniz:



![Image](assets/fr/019.webp)



Şifrelenecek USB anahtarını "**lsblk**" ve "**fdisk**" ile tanımlayın.



Benim örneğimde, USB anahtarım "**/dev/sdb**" içinde yer almaktadır. "**/dev/sdb1**", "**/dev/sdb2**", vb. görürseniz, bunlar sürücünüzde şu anda mevcut olan bölümlerdir. Bunlar şu anda anahtarınızda bulunan bölümlerdir. Manipülasyonumuz tarafından silineceklerdir.



### B. Mevcut verileri silme



Şimdi USB belleğimizdeki tüm verileri sileceğiz. İşlem, USB belleğimizdeki disk alanını 0'larla doldurmaktan ibarettir.



**Doğru cihaz dosyasını hedeflediğinizden emin olun!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Bu, anahtarımızda kalıcı düz metin verisi olmamasını sağlar.



### C. USB anahtarını LUKS ile şifreleyin



Şimdi USB anahtarımızdaki LUKS bölümünü başlatacağız. Bu, LUKS bölümünün oluşturulmasını içerir:



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



Burada, "`luksFormat`" alt komutu cihazı LUKS şifrelemesini kullanacak şekilde başlatır ve biçimlendirir. Büyük harflerle `Evet` yazarak bu işlemi onaylamanız istenir, ardından bir *passphrase* tanımlayın. **Kayıp durumunda saldırganın kaba kuvvet saldırıları yoluyla bunu keşfedemeyeceğinden emin olmak için sağlam bir *passphrase* seçin.



Bundan sonra, "**/dev/sdb**" diski LUKS ile biçimlendirilecek ve şifrelenmiş bir birim olarak kullanılmaya hazır olacaktır.



### D. Şifrelenmiş birimi biçimlendir



Neredeyse geldik ve şimdi LUKS bölümümüz içinde geçerli bir bölüm oluşturmamız gerekiyor. Bu şekilde, kilidi açtıktan sonra, diğer dosya sistemleri gibi kullanabiliriz. Bunu yapmak için şifrelenmiş bölümü açmamız gerekiyor:



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



Burada, "**usbkey1**" benim bağlamımda bölüm montajına verdiğim isimdir. Siz hangisini isterseniz onu seçebilirsiniz. Daha sonra LUKS bölümünde bulunan bu bölümü, örneğin burada **ext4** olarak biçimlendirmemiz gerekiyor:



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



**Burada, hedef konum** "**/dev/mappe/usbkey1**"** olarak belirtilmiş, neden?



"**/dev/mapper/usbkey1**" USB anahtarımıza verdiğimiz "kısayoldur" ("**/dev/mapper**" Linux'ta eşleme için geneldir). Bu nedenle şifresi çözülmüş bölümümüze erişim sağlar. İşte şimdi görmeniz gereken şey:



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



## IV. Şifrelenmiş USB anahtarını kullanma



### A. LUKS birimini açın ve düzenleyin



**Via Interface grafiği** **:**



Debian altında, "**dm-crypt**" varsayılan olarak mevcuttur. Bu nedenle, çoğu durumda kurulum doğrudan USB anahtar takıldığında gerçekleşir. Daha sonra bunun gibi bir açılır pencerede passphrase'ünüzü girmeniz istenecektir:



![Image](assets/fr/018.webp)



LUKS bölümü için şifre çözme passphrase'i girme isteği.



passphrase girildikten sonra, sisteminiz anahtardaki dosya sistemini okuyabilecek ve ardından bu dosya sistemini monte edebilecek ve bu da monte edilmiş bölümümüzü gösterecektir:



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



**Komut satırında:**



Bununla birlikte, komut satırında işlemin nasıl gerçekleştirileceğini bilmeye değer. "**crypsetup**" ve "**luksOpen**" alt komutunu kullanarak şifrelenmiş bölümün şifresini çözerek başlayalım:



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



Şimdi, USB flash sürücümüzün şifresi çözülmüş birimi, dosya sistemimizin ve işletim sistemimizin kullanabileceği bir birim sunar, bu nedenle içeriğini herhangi bir klasöre, örneğin benim durumumda "**/home/mickael/mnt**" bağlayacağız:



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



Bu, USB belleğimizdeki verilere özgürce ve şeffaf bir şekilde erişebileceğimiz anlamına gelir.



### B. LUKS birimini kapatın ve kaldırın



İşlemimiz tamamlandığında, birimimizi bozmadığımızdan emin olmak için her şeyi düzgün bir şekilde kapatmayı unutmayın. İlk adım,:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Ardından şifrelenmiş bölümün kendisini kapatın:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Artık USB anahtarımızı kullanan herhangi biri, şifrelenmiş veriler dışında içeriğine dair hiçbir şey göremeyecektir.



## V. Sonuç



Grafik kullanıcı arayüzleri bu işlemi şeffaf hale getirir, ancak yine de şifrelenmiş bir LUKS bölümünün komut satırından nasıl biçimlendirileceğini, oluşturulacağını, açılacağını ve kapatılacağını bilmek yararlıdır. Biçimlendirildikten sonra, bir LUKS bölümünü açmak ve kapatmak için gereken manipülasyonlar, güvenlik kazanımlarına kıyasla çok azdır.