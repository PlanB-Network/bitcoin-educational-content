---
name: Arch Linux
description: KISS felsefesine göre tasarlanmış minimalist, yüksek performanslı dağıtım.
---

![cover](assets/cover.webp)



Arch Linux, özellikle geliştirme amaçları için sağlamlığı, performansı ve uyarlanabilirliği ile tanınan bir dağıtımdır. Son derece hızlı ve güvenilir bir paket yöneticisi tarafından desteklenen mükemmel bir kararlılık ve özelleştirmeye elverişli bir ortam sunar. Felsefesi **KISS** (*Keep It Simple, Stupid*) ilkesine dayanmaktadır: kullanıcıya büyük ölçüde özgürlük bırakırken hafif, basit, hızlı ve düzenli bir dağıtım sunmak.



## Neden Arch Linux'u seçmelisiniz?





- Ücretsiz ve açık kaynak**: Çoğu Linux dağıtımı gibi Arch Linux da tamamen ücretsizdir. Lisans ücreti yoktur, bu da onu öğrenciler, serbest çalışanlar veya meraklılar için mükemmel bir seçim haline getirir.
- KISS** felsefesi: Arch basit, hafif ve verimli olacak şekilde tasarlanmıştır. Yalnızca temel unsurları sağlayarak ortamınızı alakart olarak oluşturmanıza olanak tanır.
- Pacman** paket yöneticisi: Pacman hızlı, güvenilir ve iyi tasarlanmış bir paket yöneticisidir. Yazılımın verimli bir şekilde kurulmasını ve güncellenmesini sağlar ve bağımlılıkları hassas bir şekilde yönetir.
- Kapsamlı dokümantasyon ve aktif bir topluluk**: [Arch Wiki] (https://wiki.archlinux.org) muhtemelen Linux dünyasındaki en iyi teknik dokümantasyonlardan biridir. Ne yaptığınızı anlamak için bir altın madeni. Çoğunlukla deneyimli profillerden oluşan topluluk çok aktiftir ve önceden biraz araştırma yapmış olmanız koşuluyla takıldığınızda size yardımcı olabilir.



## Kurulum ve yapılandırma



### Ön Koşullar



Gerekli malzemeler:





- En az **8 GB** boyutunda bir USB anahtarı
- minimum 2 GB** RAM
- En az 20 GB boş disk alanına sahip bir bilgisayar



### İndir



![0_1](assets/fr/01.webp)



2017'den beri Arch Linux artık 32 bit mimarileri desteklemiyor. Yalnızca 64 bit sürümler mevcuttur.





- ISO görüntüsünün en son resmi sürümünü indirmek için [resmi web sitesini] (https://mir.archlinux.fr/iso/latest/) ziyaret edin.



### Önyüklenebilir bir anahtar oluşturma



Önyüklenebilir bir USB flash sürücü oluşturmak için **Balena Etcher** gibi bir araç kullanabilirsiniz:





- Balena Etcher'ı [resmi web sitesinden] (https://etcher.balena.io) indirin.
- Yazılımı başlatın, Arch Linux ISO görüntüsünü seçin.
- Hedef cihaz olarak USB anahtarınızı seçin.
- Önyüklenebilir anahtarı oluşturmaya başlamak için **Flash** üzerine tıklayın.



![0_2](assets/fr/02.webp)



## Arch Linux Kurulumu



## USB anahtarında önyükleme





- Bilgisayarınızı tamamen kapatın
- Önyüklenebilir USB anahtarını takın
- Yeniden başlatın ve **F1**, **Escape**, **F9**, vb. tuşlarına basarak BIOS/UEFI'ye girin (modelinize bağlı olarak)
- Önyükleme menüsünde, önyükleme aygıtı olarak USB anahtarını seçin. Her şey doğru ayarlanmışsa, Arch Linux Interface önyükleme ekranına yönlendirileceksiniz.



## Kurulumun başlatılması



Açılış ekranında, kurulumu başlatmak için ilk seçeneği seçin. Arch Linux'un grafiksel bir yükleyici sunmadığını unutmayın. Bir kez başlatıldığında, kök modunda bir terminale yönlendirileceksiniz.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Klavye yapılandırması



Ile mevcut düzenleri görüntüleyebilirsiniz:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Ardından ile bir düzen yükleyin:



```shell
loadkeys nom-disposition
```



Varsayılan olarak klavye İngilizce'dir (qwerty), ancak `loadkeys fr` ile `azerty`ye geçebilirsiniz.



### Tarih ve saati ayarlama



Arch Linux sistem saatini yönetmek için `timedatectl` aracını kullanır.



![0_7](assets/fr/07.webp)





- Ile saat diliminizi ayarlayın:


```shell
timedatectl set-timezone Europe/Paris
```





- Ile otomatik senkronizasyonun etkinleştirildiğini kontrol edin:


```shell
timedatectl status
```





- Gerekirse etkinleştirin:


```shell
timedatectl set-ntp true
```




Bu, zaman sunucularıyla otomatik senkronizasyon protokolü olan NTP'yi etkinleştirir. Bu adım, daha sonra paketleri yüklerken veya SSL sertifikalarını yapılandırırken tarih hatalarını önlemek için önemlidir.



### Disk bölümleme





- Sisteminizin **UEFI** veya **BIOS** ile açılıp açılmadığını kontrol edin:



```shell
ls /sys/firmware/efi
```



Dosya mevcutsa, **UEFI** içindesiniz demektir. Aksi takdirde, **BIOS (Eski)** konumundasınızdır.




- Kullanılabilir diskleri listeleyin:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Partition Manager'ı başlatın:



```shell
cfdisk /dev/nom-du-disque
```



UEFI'de iseniz **GPT**, BIOS'ta iseniz **DOS** öğesini seçin.



![0_9](assets/fr/09.webp)



#### Oluşturulacak puanlar




- UEFI** modunda



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- BIOS'ta



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Yaz** öğesini seçin, **Evet** yazın ve ardından **Kapat** öğesini seçin.



### Bölümleri biçimlendirme





- UEFI**:



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- BIOS**:



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### Temel sistem kurulumu



Kök** bölümünü bağlayın:





- BIOS üzerinde:


```shell
mount /dev/sda2 /mnt
```




- uEFI üzerinde:


```shell
mount /dev/sda3 /mnt
```



Ardından temel paketleri yükleyin:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate **fstab** dosyası, işletim sisteminin her açılışta manuel müdahale olmadan bölüm montajını otomatik olarak yönetmesini sağlar:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Chroot** ortamına girin:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Sistem yapılandırması





- Düzenlemek için bir metin düzenleyici yükleyin:



```shell
pacman -S vim
```





- Dili ayarlayın:


Etc/locale.gen` dosyasını düzenleyin ve ardından `en_US.UTF-8 UTF-8` satırını kaldırın



![0_14](assets/fr/14.webp)





- Makine adını ayarlayın:



```shell
echo nom_machine > /etc/hostname
```





- Kök parolasını ayarlayın:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUB'u Yükleme



Yükleyin:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



İndirdikten sonra, disk bölümü formatına göre yüklemeniz gerekir.




- BIOS** için:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- UEFI** için:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Sonuçlandırma





- Chroot ortamından çıkın:


```shell
exit
```





- Bölümleri kaldırın:


```shell
umount -R /mnt
```





- Yeniden Başlat:


```shell
reboot
```



Başlangıçta, **root** kullanıcı adınız ve parolanızla oturum açın.



![0_18](assets/fr/18.webp)


## Yeniden başlatmadan sonra ağ bağlantısı



Yeniden başlatma sırasında hiçbir ağ bağlantısı etkin olmayabilir. Ile arayüzleri listeleyebilirsiniz:



```shell
ip link
```



Ardından terminale aşağıdaki metni girerek Interface ağını yapılandırın



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface grafikleri (GNOME)



Varsayılan olarak, **Arch Linux** grafiksel Interface içermez. Bir tane eklemek için:



Sistemi güncelleyin:



```shell
pacman -Syu
```



Aşağıdaki komutla **Xorg**'u kurun ve varsayılan seçenekleri korumak için her seferinde enter tuşuna basın:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Aşağıdaki komutla **GNOME**'u kurun ve varsayılan seçenekleri korumak için her seferinde girin:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Oturum yöneticisini** etkinleştirin:



```shell
systemctl enable gdm
systemctl start gdm
```



Sistem otomatik olarak yeniden başlatılır ve Interface grafik girişini alırsınız. Kök kullanıcı adı ve şifre ile oturum açın.



![0_21](assets/fr/21.webp)



## Kullanıcı oluşturma



Interface GNOME'a** girdikten sonra, daha fazla güvenlik ve daha güvenli, risksiz kullanım için yeni bir kullanıcı oluşturmanız gerekecektir. Uygulamalara girin ve terminali başlatmak için "konsol" seçeneğini seçin.





- Bir kullanıcı ekleyin:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Yükle **sudo**:


```shell
pacman -S sudo
```





- Sudo** haklarını etkinleştirin:



```shell
EDITOR=nano visudo
```





- Ardından satırdaki yorumu kaldırın:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Sistemi yeniden başlatın ve kullanıcı adınızla oturum açın.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Yazılım yükleme



Arch Linux minimalist olduğundan, birçok yazılım varsayılan olarak yüklü değildir. İhtiyacınız olanı eklemek için aşağıdaki komutu yazın:



```shell
pacman -S nom_du_paquet_a_installe
```



Örneğin, **nano** metin düzenleyicisini yüklemek için:



```shell
pacman -S nano
```



Firefox` gibi hafif bir web tarayıcısı yüklemek için:



```shell
pacman -S firefox
```



Son olarak, `net-tools` gibi temel ağ araçlarını eklemek istiyorsanız, komut şu şekilde olacaktır:



```shell
pacman -S net-tools
```



Birden fazla paketi ayrı ayrı listeleyerek tek bir komutla yükleyebileceğinizi unutmayın:



```shell
pacman -S vim firefox net-tools
```



Arch Linux, olağanüstü kararlılığı, minimalist felsefesi ve sağlamlığı ile öne çıkarak geliştirme ortamları için ideal bir seçimdir. Yalnızca temel unsurları sağlayarak, özel ihtiyaçlarınıza göre özelleştirilmesi kolay, hafif ve yüksek performanslı bir temel sunar. Bu minimalist yaklaşım aynı zamanda sistem üzerinde daha fazla kontrol sağlar ve saldırı yüzeyini sınırlandırarak güvenliği güçlendirir. Aktif topluluğu ve kapsamlı dokümantasyonu sayesinde Arch Linux, profesyonel gelişim için optimize edilmiş güvenli ve esnek bir ortam oluşturmanıza yardımcı olabilir.



Arch Linux ile başlamaktan keyif aldıysanız, ihtiyaçlarınıza ve kullanımlarınıza uyum sağlayan modüler, güvenli ve sağlam bir işletim sistemi olan **Fedora OS** hakkındaki eğitimimizi seveceksiniz.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1