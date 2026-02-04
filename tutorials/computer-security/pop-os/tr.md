---
name: Pop!_OS
description: Bir Linux dağıtımı olan Pop!_OS'u yükleme kılavuzu
---

![cover](assets/cover.webp)



## Giriş



Pop!OS, geliştiriciler, tasarımcılar ve ileri düzey kullanıcılar için makineler konusunda uzmanlaşmış Amerikalı bir üretici olan **System76** tarafından geliştirilen Linux tabanlı bir işletim sistemidir.



Modern, istikrarlı, yüksek performanslı bir ortam sunmak için tasarlanan Pop!OS, basit bir deneyim, güçlü araçlar ve üretkenliğe güçlü bir odaklanma ile ayırt edilir.



### System76 kimdir?



System76, 2005 yılında kurulan ve merkezi Denver'da bulunan, Linux için özel olarak tasarlanmış dizüstü bilgisayar, masaüstü bilgisayar ve sunucu üretiminde uzmanlaşmış bir Amerikan şirketidir.



System76, geleneksel üreticilerin aksine açık, onarılabilir ve yazılım özgürlüğüne yönelik olarak tasarlanmış makineler geliştirmektedir.



System76 sadece bilgisayar üretmiyor.



Şirket aynı zamanda :




- Pop!OS**, kendi Linux tabanlı işletim sistemi;
- COSMIC**, Pop!OS tarafından kullanılan modern, yüksek performanslı masaüstü ortamı;
- Coreboot tabanlı açık kaynaklı bir ürün yazılımı olan Open Firmware**;
- geliştiriciler ve tasarımcılar için araçlar.



Amaç, Apple ekosistemiyle karşılaştırılabilir, ancak tamamen açık ve Linux merkezli yüksek kaliteli donanım ve yazılım entegrasyonu sunmaktır.



## Modern, istikrarlı ve erişilebilir bir sistem



Pop!OS, Ubuntu'ın temelleri üzerine inşa edilerek mükemmel kararlılık, geniş donanım uyumluluğu ve büyük bir yazılım ekosistemine erişim sağlar.


Yeni kullanıcılar için bile akıcı, sezgisel ve özelleştirilebilir olacak şekilde tasarlanmış zarif bir arayüz olan COSMIC masaüstü sağlar.



## Geliştiriciler, tasarımcılar ve talepkar kullanıcılar için ideal bir seçim



Pop!OS özellikle :





- geliştiriciler (önceden yüklenmiş araçlar, gelişmiş döşeme yönetimi),
- nvidia veya AMD grafik kartlarına sahip kullanıcılar,
- güvenilir bir sistem arayan öğrenciler ve profesyoneller,
- basit bir geçiş yapmak isteyen Windows kullanıcıları.



Günlük kullanımı kolaylaştırmak için otomatik döşeme, net bir yazılım merkezi ve entegre üretkenlik araçları içerir.



## Pop!OS öne çıkanlar





- Düzenli güncellemeler sayesinde optimize edilmiş performans**.
- İki ISO sürümü mevcuttur**: standart ve Nvidia için optimize edilmiş.
- Gelişmiş güvenlik** (kurulumda LUKS şifreleme mevcuttur).
- Interface COSMIC** ergonomik ve modern.
- Ubuntu ve Flatpak yazılımı ile son derece uyumludur**.



## POP!OS'u güvenli bir şekilde indirin



### 1. Ön Koşullar



POP!OS'u indirmeden ve kurmadan önce kurulum ortamını doğru şekilde hazırlamak için yapmanız gereken birkaç şey vardır.



### Gerekli ekipman





- Uyumlu bir bilgisayar**: Intel veya AMD işlemci, Intel / AMD / Nvidia GPU.
- En az 4 GB RAM** (rahat kullanım için 8 GB önerilir).
- minimum 20 GB boş alan** (40 GB veya daha fazlası önerilir).
- Kurulum ortamını oluşturmak için en az 4 GB USB anahtarı**.



### İnternet bağlantısı



Sabit bir bağlantı, :





- iSO görüntüsünü indirin,
- kurulumdan sonra güncellemeleri yükleyin.



Pop!OS bağlantı olmadan da çalışabilir, ancak kurulum İnternet üzerinden çok daha sorunsuzdur.



### Veri yedekleme



Pop!OS başka bir sistemle (Windows, Ubuntu, vb.) değiştirilecekse veya birlikte kullanılacaksa, devam etmeden önce önemli dosyaların yedeklenmesi tavsiye edilir.



### Nvidia GPU'nun varlığını kontrol edin (varsa)



Nvidia grafik kartına sahip bilgisayarlar için, Nvidia sürücülerini içeren özel ISO görüntüsünü indirmeniz gerekir.


Bu kontrol çok basittir:





- pC teknik özelliklerine başvurarak,
- veya sistem ayarlarında grafik kartı modeline bakarak yapabilirsiniz.



### Resmi web sitesinden indirin



Pop!OS ISO görüntüsü doğrudan resmi System76 sayfasından indirilmelidir: [system76.com/pop](https://system76.com/pop/).



Bu sayfa her zaman donanımınıza uyarlanmış en yeni sürümü sunar.



![capture](assets/fr/03.webp)



### Sürüm seçin: Standart veya Nvidia veya Raspberry Pi (ARM64)



Pop!OS'nin üç çeşidi mevcuttur:



### Standart versiyon



Kullanan bilgisayarlar için önerilir:





- intel veya AMD işlemci;
- entegre bir Intel veya AMD GPU;
- bir AMD Radeon grafik kartı.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia sürümü



Nvidia grafik kartlarıyla donatılmış bilgisayarlar için önerilir.


Bu görüntü zaten Nvidia sürücülerini içeriyor, kurulumu kolaylaştırıyor ve grafik sorunlarını azaltıyor.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi sürümü (ARM64)



Raspberry Pi 4 ve 400 (ARM işlemci) için.


ARM mimarisine uyarlanan bu mini bilgisayarlar için özel bir sürümdür.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Önyüklenebilir bir USB anahtarı oluşturma



Balena Etcher gibi çeşitli araçlar kullanabilirsiniz:





- Balena Etcher](https://etcher.balena.io/) dosyasını indirin ve yükleyin.



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Balena Etcher'ı açın, ardından Pop!OS ISO görüntüsünü seçin.
- Hedef ortam olarak USB anahtarını seçin.
- Flash'e tıklayın ve işlemin bitmesini bekleyin.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Pop!OS'yi yükleme ve güvenliğini sağlama



### USB anahtarından önyükleme





- Bilgisayarı kapatın.
- USB anahtarını (Pop!OS içeren) takın.
- Bilgisayarınızı açın. Yeni bilgisayarlarda, sistem USB önyükleme anahtarını otomatik olarak tanımalıdır. Durum böyle değilse, BIOS/UEFI erişim tuşunu (markaya bağlı olarak genellikle F2, F12 veya Delete) basılı tutarak yeniden başlatın.
  - BIOS/UEFI menüsünde, önyükleme aygıtı olarak USB anahtarınızı seçin.
  - Kaydedin ve yeniden başlatın.



### Kurulumun başlatılması



Önyüklenebilir USB anahtarınızı başlangıç aygıtı olarak seçtiğinizde, bilgisayarınız Pop!OS Live ortamına önyükleme yapacaktır.



Dilinizi seçin.



![Capture](assets/fr/10.webp)



Bir konum seçin.



![Capture](assets/fr/11.webp)



Klavye girişi için bir dil seçin.



![Capture](assets/fr/12.webp)



Bir klavye düzeni seçin.



![Capture](assets/fr/13.webp)



Standart bir kurulum için `Temiz Kurulum` seçeneğini seçin. Bu yeni Linux kullanıcıları için en iyi seçenektir, ancak hedef sürücünün tüm içeriğini sileceğini unutmayın. Alternatif olarak, Pop!OS'u canlı ortamda test etmeye devam etmek için `Deneme Modu`nu seçebilirsiniz.



![Capture](assets/fr/14.webp)



GParted'a erişmek için `Custom (Advanced)` öğesini seçin. Bu araç çift önyükleme, ayrı bir `/home` bölümü oluşturma veya `/tmp` bölümünü farklı bir sürücüye yerleştirme gibi gelişmiş özellikleri yapılandırmanızı sağlar.



Pop!OS'u seçilen sürücüye yüklemek için `Sil ve Yükle'ye tıklayın.



![Capture](assets/fr/15.webp)



### Kullanıcı hesabı yapılandırması



Kurulum programının bir sonraki bölümü, yeni işletim sisteminizde oturum açabilmeniz için bir kullanıcı hesabı oluşturmanızda size yol gösterecektir.



Bir tam ad (bu, büyük veya küçük harf olmak üzere istediğiniz herhangi bir metni içerebilir) ve bir kullanıcı adı (küçük harfle yazılmalıdır) girin:



![Capture](assets/fr/16.webp)



Hesap oluşturulduktan sonra, yeni bir şifre belirlemeniz istenecektir.



![Capture](assets/fr/17.webp)



### Tam disk şifreleme



Sistem diski şifrelemesi gerekli değildir, ancak birinin cihaza yetkisiz fiziksel erişim sağlaması durumunda kullanıcı verilerinin güvenliğini garanti eder.



Sürücü, `Şifreleme parolası kullanıcı hesabı parolasıyla aynıdır` seçeneğini işaretleyerek oturum açma parolanız kullanılarak şifrelenebilir. Ayrıca bu kutunun işaretini kaldırabilir ve alttaki `Şifre Ayarla` seçeneğini seçebilirsiniz. Disk şifreleme işlemini yok saymak için `Şifreleme Yapma` seçeneğini seçin.



![Capture](assets/fr/18.webp)



Eğer `Parola Ayarla` düğmesini seçtiyseniz, şifreleme parolanızı ayarlamanız için ek bir istem göreceksiniz.



Kurulum programında bir sonraki adıma geçin. Pop!OS şimdi disk üzerine kuruluma başlayacaktır.



![Capture](assets/fr/19.webp)



Kurulum tamamlandığında, bilgisayarınızı yeniden başlatın ve kullanıcı hesabı yapılandırma işlemini tamamlamak için oturum açın.



Başlangıçta Canlı USB anahtarınıza öncelik vermek için önyükleme sırasını değiştirdiyseniz, bilgisayarı tamamen kapatın ve kurulum USB anahtarını çıkarın. Çift önyükleme modundaysanız, yapılandırmaya erişmek için uygun tuşlara basın ve Pop!OS kurulumunu içeren sürücüyü seçin.



![Capture](assets/fr/20.webp)



### NVIDIA Grafik



Intel/AMD ISO'dan kurulum yaptıysanız ve sisteminizde ayrı bir NVIDIA grafik kartı varsa veya daha sonraki bir tarihte eklediyseniz, optimum performans elde etmek için kartınızın sürücülerini manuel olarak yüklemeniz gerekecektir. Sürücüyü yüklemek için aşağıdaki komutu bir komut terminalinde çalıştırın:



```bash
sudo apt install system76-driver-nvidia
```



NVIDIA grafik sürücülerini Pop!_Shop'tan da yükleyebilirsiniz.



![Capture](assets/fr/20.webp)



## Temel araçların kurulumu



Pop!OS, Pop!Shop aracılığıyla geniş bir yazılım yelpazesi sunar, ancak birçok temel araç terminal üzerinden `apt` veya `flatpak` ile de kurulabilir. İşte eksiksiz bir çalışma ortamı için temel araçların nasıl kurulacağı.



### Terminal kurulumu




| Araç | Açıklama | Kurulum Komutu |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox | Özgür ve popüler web tarayıcısı | `sudo apt install firefox` |
| Brave | Gizlilik odaklı web tarayıcısı | Pop!_Shop veya resmi site üzerinden kurulum |
| Visual Studio Code (VS Code) | Geliştiriciler için güçlü kod düzenleyici | `flatpak install flathub com.visualstudio.code` |
| Git | Versiyon yöneticisi | `sudo apt install git` |
| Flatpak | Alternatif paket yöneticisi | `sudo apt install flatpak` |
| VLC | Çok yönlü medya oynatıcı | `sudo apt install vlc` |
| GNOME Terminal | Varsayılan terminal | Pop!OS üzerinde önceden yüklü |
| Curl | Çevrimiçi veri aktarım aracı | `sudo apt install curl` |
| Wget | HTTP/FTP üzerinden dosya indirme | `sudo apt install wget` |
| Docker | Uygulama konteynerleştirme | Resmi betik veya `apt` üzerinden kurulum |
| Node.js | Sunucu tarafı JavaScript ortamı | `apt` veya NodeSource üzerinden kurulum |
| Python3 | Programlama dili | `sudo apt install python3 python3-pip` |
| GIMP | Gelişmiş resim düzenleyici | `sudo apt install gimp` |
| Thunderbird | E-posta istemcisi | `sudo apt install thunderbird` |
| Transmission | Hafif BitTorrent istemcisi | `sudo apt install transmission-gtk` |
| Htop | Etkileşimli sistem monitörü | `sudo apt install htop` |

### Pop aracılığıyla kurulum! Shop (grafik arayüz)





- Ana menüden **Pop!_Shop** öğesini açın.
- İstediğiniz uygulamaları bulmak için arama çubuğunu kullanın (örneğin, "Brave").
- Her uygulama için **Yükle** seçeneğine tıklayın.
- Pop!_Shop bağımlılıkları ve güncellemeleri otomatik olarak yönetir.



## Sistem güncellemesi



### Seçenek 1: Grafik kullanıcı arayüzü (GUI) aracılığıyla



Pop!OS basit, sezgisel bir grafik güncelleme yöneticisine sahiptir.



1. Ana menüye** tıklayın (sol alttaki simge).


2. Aç **"Pop!_Shop "**.


3. Pop!_Shop'ta **"Güncellemeler "** sekmesine tıklayın.


4. Sistem otomatik olarak mevcut güncellemeleri kontrol edecektir.


5. Güncellemeleri yüklemeye başlamak için **"Tümünü güncelle "** seçeneğine tıklayın.


6. İstenirse şifrenizi girin.


7. İşlemin bitmesini bekleyin, ardından gerekirse yeniden başlatın.



### Seçenek 2: Terminal üzerinden



Bir terminal açın ve :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Kullanıcı yönetimi



Günlük işlemler için sudo haklarına sahip standart bir kullanıcı hesabı kullanmanızı öneririz.



Yeni bir kullanıcı oluşturmak için :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Oturumu kapatın, ardından bu yeni kullanıcıyla tekrar oturum açın.



### Grafik sürücüsü yönetimi





- Nvidia kartlar için, tescilli sürücülerin yüklü olup olmadığını kontrol edin:



```bash
sudo apt install system76-driver-nvidia
```





- AMD/Intel için sürücüler genellikle varsayılan olarak dahil edilir.



### Güvenlik duvarını etkinleştirin (UFW)



Pop!OS varsayılan olarak ağ trafiğini engellemez. Güvenliği artırmak için UFW'yi etkinleştirin:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Otomatik güncellemeleri yapılandırma



Manuel müdahale olmadan sistemi güncel tutmak:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Görünümü ve davranışı özelleştirme





- Açık veya koyu bir tema seçmek için **Sistem ayarları** → **Görünüm** öğesini açın.
- COSMIC yöneticisi aracılığıyla aktif köşeleri, animasyonları ve uzantıları yapılandırın.
- İş akışınızı optimize etmek için masaüstü düzenini ayarlayın.



### Otomatik yedeklemeyi yapılandırma



Pop!OS yedekleme için Deja Dup gibi araçları entegre eder:





- Menüden **Yedekleme** öğesini başlatın.
- Harici bir sürücü veya bir ağ konumu seçin.
- Düzenli yedeklemeler planlayın.



### Yararlı GNOME/COSMIC uzantılarını yükleme



İşte kullanıcı deneyimini geliştirmek için önerilen birkaç uzantı:





- Dash to Dock**: uygulama çubuğu her zaman görünür.
- GSConnect**: Android ile senkronizasyon.
- Pano Göstergesi**: gelişmiş pano yönetimi.



Aracılığıyla yükleyin:



```bash
sudo apt install gnome-shell-extensions
```



Ardından ayarlardan etkinleştirin.



### Bellek ve takas yönetimini optimize etme



Takas durumunuzu kontrol edin:



```bash
swapon --show
```



Gerekirse takas boyutunu artırın veya bir takas dosyası yapılandırın :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Otomatik montaj için `/etc/fstab` dosyasına ekleyin.



## Paket ve depo yönetimi



### Paket kaynaklarını anlama



Ubuntu tabanlı Pop!OS, temel olarak :





- Resmi Ubuntu** depoları: en kararlı yazılımlar için.
- System76** depoları: sürücüler, aygıt yazılımı ve özel araçlar için.
- Flatpak**: çok çeşitli kum havuzu uygulamalarına erişin.
- Snap** (isteğe bağlı): başka bir evrensel paket biçimi.



---

### PPA depoları ekleme ve yönetme



Sık güncellenen yazılımları yüklemek için belirli PPA'lar (Kişisel Paket Arşivleri) eklenebilir:



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Sonuç



Pop!OS, hem yeni başlayanlar hem de ileri düzey kullanıcılar için uygun, modern ve kararlı bir Linux dağıtımıdır.



Sezgisel COSMIC arayüzü ve entegre araçları sayesinde, ister geliştirme, oluşturma ister günlük kullanım için olsun, akıcı ve üretken bir deneyim sunar.



Bu eğitim temel aşamaları kapsamaktadır: hazırlık, indirme, kurulum, ilk ayarlar ve temel araçlar.



Pop!OS'u daha fazla keşfetmekten ve ondan en iyi şekilde yararlanmak için ortamınızı özelleştirmekten çekinmeyin.