---
name: Ubuntu
description: Windows'a alternatif olarak Ubuntu'yu kurmak ve kullanmak için eksiksiz kılavuz
---
![cover](assets/cover.webp)


## Giriş


Bir işletim sistemi (OS), bilgisayarınızın tüm kaynaklarını yöneten ana yazılımdır. Ubuntu gibi alternatif bir işletim sistemi seçmek güvenlik, maliyet ve gizlilik açısından birçok avantaj sunabilir.


### Neden Ubuntu?




- Geliştirilmiş güvenlik**: Linux dağıtımları güvenlik ve sağlamlıklarıyla ünlüdür
- Sıfır maliyet**: Ubuntu ve çoğu Linux dağıtımı ücretsizdir
- Geniş topluluk**: Forumlar ve eğitimler aracılığıyla yardım etmeye hazır bir kullanıcı topluluğu
- Mahremiyete saygı**: Daha fazla şeffaflık için açık kaynak sistemi
- Basitlik**: Kullanıcı dostu Interface ve kullanım kolaylığı
- Zengin ekosistem**: Kapsamlı açık kaynak yazılım kataloğu
- Düzenli destek**: Canonical'dan güvenli güncellemeler


## Kurulum ve yapılandırma


### 1. Ön Koşullar


**Gerekli ekipman:**




- En az 12 GB'lık bir USB anahtarı
- En az 25 GB kullanılabilir alana sahip bir bilgisayar


### 2. İndir




- Ubuntu.com/download](https://ubuntu.com/download) adresine gidin
- Kararlı sürümü seçin (LTS önerilir)
- ISO görüntüsünü indirin


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. Önyüklenebilir bir USB anahtarı oluşturma


Balena Etcher gibi çeşitli araçlar kullanabilirsiniz:




- Balena Etcher](https://etcher.balena.io/) dosyasını indirin ve yükleyin


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Balena Etcher'ı açın, ardından Ubuntu ISO görüntüsünü seçin
- Hedef ortam olarak USB anahtarını seçin
- Flash'a tıklayın ve işlemin bitmesini bekleyin


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Ubuntu'yu kurma ve güvenliğini sağlama


**4.1 USB bellek çubuğundan önyükleme** (Fransızca)




- Bilgisayarı kapatın
- USB anahtarını (Ubuntu içeren) takın
- Bilgisayarınızı açın. Yeni bilgisayarlarda, sistem USB önyükleme anahtarını otomatik olarak tanımalıdır. Durum böyle değilse, BIOS/UEFI erişim tuşunu (markaya bağlı olarak genellikle F2, F12 veya Delete) basılı tutarak yeniden başlatın
 - BIOS/UEFI menüsünde, önyükleme aygıtı olarak USB anahtarınızı seçin
 - Kaydet ve yeniden başlat


**4.2 Kurulumun başlatılması** (Fransızca)


**Başlangıç ekranı**


USB anahtarından önyükleme yaparken, Ubuntu'yu başlatmanızı sağlayan bu ekranı göreceksiniz.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**Dil seçimi


Kurulum ve sistem için tercih ettiğiniz dili seçin.


![Sélection de la langue](assets/fr/07.webp)


**Erişilebilirlik seçenekleri


Gerekirse erişilebilirlik seçeneklerini yapılandırın (ekran okuyucu, yüksek kontrast, vb.).


![Options d'accessibilité](assets/fr/08.webp)


**Klavye yapılandırması


Klavye düzeninizi seçin. Tuşların yapılandırmanıza uygun olup olmadığını kontrol etmek için bir test alanı mevcuttur.


![Configuration du clavier](assets/fr/09.webp)


**Ağ bağlantısı**


Kurulum sırasında güncellemeleri indirmek için Wi-Fi veya kablolu ağınıza bağlanın.


![Configuration réseau](assets/fr/10.webp)


**Kurulum türü


"Ubuntu'yu Dene" (yüklemeden test etmek için) veya "Ubuntu'yu Yükle" arasında seçim yapın.


![Choix du type d'installation](assets/fr/11.webp)


**Kurulum yöntemi


Etkileşimli kurulumu seçin.


![Mode d'installation](assets/fr/12.webp)


**Uygulama seçimi


Varsayılan kurulum veya genişletilmiş uygulama seçimi arasında seçim yapın.


![Sélection des applications](assets/fr/13.webp)


**Üçüncü taraf uygulamaları


Ek sürücüler ve tescilli yazılımlar yükleyip yüklemeyeceğinize karar verin.


![Installation applications tierces](assets/fr/14.webp)


**Bölümleme türü


İki ana seçeneğiniz var:




- "Diski sil ve Ubuntu'yu yükle": Ubuntu için tüm diski kullanır
- "Manuel kurulum: Windows ile çift önyükleme oluşturun veya bölümlerinizi özelleştirin


![Choix du partitionnement](assets/fr/15.webp)


**Kullanıcı hesabı oluşturma


Ubuntu hesabınız için kullanıcı adınızı ve parolanızı belirleyin.


![Création du compte](assets/fr/16.webp)


**Zaman dilimi


Sistem saatini ayarlamak için coğrafi bölgenizi seçin.


![Sélection du fuseau horaire](assets/fr/17.webp)


**Kurulum özeti**


Son kuruluma başlamadan önce tüm seçimlerinizi kontrol edin. "Yükle "ye tıkladığınızda işlem başlar.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 Kurulumdan sonra Ubuntu'yu yükseltme** (Fransızca)


Yeni bir kurulumdan sonra sisteminizi güncellemek önemli bir adımdır. İki seçeneğiniz vardır:


**Seçenek 1: Grafiksel kullanıcı Interface** aracılığıyla




- Uygulamalar menüsünde "Yazılım ve güncellemeler "i arayın
- Uygulama otomatik olarak mevcut güncellemeleri kontrol edecektir
- Güncellemeleri yüklemek için ekrandaki talimatları izleyin


**Seçenek 2: Terminal Üzerinden




- Terminali Aç (Ctrl + Alt + T)
- Mevcut güncellemeleri kontrol etmek için aşağıdaki komutu yazın:


```bash
sudo apt update
```




- Sorulduğunda şifrenizi girin
- Güncellemeleri yüklemek için, yazın:


```bash
sudo apt upgrade
```




- 'Y' yazıp Enter tuşuna basarak kurulumu onaylayın


### 5. Temel görevleri keşfetme


**5.1 İnternette Gezinme


Varsayılan olarak, Firefox'u genellikle başlatma çubuğunda bulursunuz.


Firefox'u başlatın ve gezinmeye başlayın.


Diğer tarayıcılar (Chrome, Brave, vb.) Yazılım Yöneticisi veya .deb paketleri aracılığıyla kurulabilir.


**5.2 Kelime işlem


Ubuntu, LibreOffice paketi (kelime işlem için Writer) ile birlikte gelir.


Açmak için: Etkinlikler > "LibreOffice Writer" için arama yapın veya çubukta görünüyorsa simgeye tıklayın.


Çeşitli formatlarda (.docx dahil) belgeler oluşturabilir, düzenleyebilir ve kaydedebilirsiniz.


**5.3 Uygulamaların yüklenmesi


Yazılım yöneticisi ("Ubuntu Software" olarak adlandırılır): uygulamaları aramak ve yüklemek için grafiksel Interface.


Terminal'den şu komutu kullanın:


```bash
sudo apt install nom-du-paquet
```


Örnek:


```bash
sudo apt install vlc
```


### 6. Sonuç ve ek kaynaklar


Artık Ubuntu'yu günlük olarak kullanmaya hazırsınız: sisteminizin güvenliğini sağlayın, göz atın, ofis işleri yapın, yazılım yükleyin ve işletim sisteminizi güncel tutun!


Dijital yaşamınızın güvenliğini bir adım öteye taşımak için, gizliliğinizi korumak için mükemmel bir şekilde uygun olan ve Ubuntu kurulumunuzu tamamlayan şifreli mesajlaşma hizmetimize göz atmanızı öneririz:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2