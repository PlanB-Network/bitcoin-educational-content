---
name: SeedSigner
description: Kendin yap, vatansız, uygun fiyatlı ve tamamen hava boşluklu bir Hardware Wallet
---

![cover](assets/cover.webp)



SeedSigner, herkesin ucuz, genel amaçlı elektronik bileşenler kullanarak kendi kendine oluşturabileceği açık kaynaklı bir Hardware Wallet Bitcoin'dir. Ledger, Coldcard veya Trezor gibi ticari ürünlerin aksine, bu bir şirket tarafından üretilen kullanıma hazır bir cihaz değildir: herkesin kendi cihazını yaratmasına ve her adımı kontrol etmesine olanak tanıyan bir topluluk projesidir.



SeedSigner %100 ***hava boşluklu*** olacak şekilde tasarlanmıştır: asla internete bağlanmaz, Wi-Fi veya Bluetooth'a sahip değildir (Raspberry Pi Zero v1.3 durumunda) ve Exchange verileri için asla bir bilgisayara bağlanmaz. İletişim yalnızca QR kodlu bir Exchange sistemi üzerinden gerçekleşir. Somut olarak, portföy yönetim yazılımınız (Sparrow wallet gibi) imzalanacak işlemi QR kodları şeklinde görüntüler; bunları SeedSigner'ın kamerasıyla tararsınız, ardından cihaz RAM'inde geçici olarak saklanan özel anahtarlarınızı kullanarak işlemi imzalar. Son olarak, Bitcoin ağına göndermek için yazılımınızla taradığınız imzalı işlemi içeren QR kodları oluşturur.



![Image](assets/fr/001.webp)



SeedSigner ayrıca ***durumsuzdur***. Başka bir deyişle, diğer donanım cüzdanlarının aksine seed'nizi veya özel anahtarlarınızı kalıcı olarak kaydetmez. Cihazı ayarlarınızı bir microSD karta kaydedecek şekilde yapılandırmadığınız sürece, her yeniden başlattığınızda hafızası tamamen boşalır. Bu nedenle, seed'nizi her kullandığınızda yeniden girmeniz gerekir; en pratik yöntem, SeedSigner'ın kamerası kullanılarak başlangıçta taranacak bir QR kodu biçiminde saklamaktır. Bu çalışma modu saldırı yüzeyini önemli ölçüde azaltır: bir hırsız cihazınızı çalsa bile, varsayılan olarak her zaman boş olduğu için üzerinde herhangi bir bilgi bulamaz.



seed'unuzu saklamak ve SeedSigner ile kullanmak için bir başka seçenek de uyumlu bir okuyucu ile birlikte bir *SeedKeeper* akıllı kart kullanmaktır. Bu size işlemleri imzalamak için SeedSigner ekranını kullanırken seed'unuzu saklamak için çok sağlam bir *secure element* sağlar. Ancak bu özel yapılandırma başka bir özel eğitimin konusudur. Burada, SeedSigner'ın temel kullanımına odaklanacağız:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner projesi, dünyanın her yerinde herkese bitcoinlerini korumak için gelişmiş güvenlikten yararlanma imkanı sunduğu için Bitcoin ekosisteminde önemli bir yere sahiptir. Ana avantajı erişilebilirliğinde yatmaktadır: gerekli donanım 50 dolardan daha az bir fiyata satın alınabilir. Dahası, kısıtlı ülkelerde yaşayan insanların, bulunması kolay ve yasal kısıtlamalara daha az tabi olan standart bilgisayar bileşenlerinden kendi Hardware Wallet'larını oluşturmalarını sağlar.



Ancak bu özel bağlamların dışında bile SeedSigner sizin için ilginç bir seçenek olabilir: açık kaynak kodludur, durum bilgisi olmadan çalışır ve Hardware Wallet'nizin Supply zincirine bağlı saldırı vektörlerini azaltır.



## 1. Gerekli ekipman



SeedSigner'ınızı oluşturmak için aşağıdaki bileşenlere ihtiyacınız olacaktır:





- Raspberry Pi Zero
    - Ne Wi-Fi ne de Bluetooth'a sahip olmadığı ve tam izolasyon sağladığı için 1.3 sürümü önerilir.
 - W ve v2 versiyonları da uyumludur, ancak bir Wi-Fi/Bluetooth çipi içerir. Bu nedenle radyo modülünü karttan çıkararak fiziksel olarak devre dışı bırakmanız tavsiye edilir. İşlem nispeten basittir, ancak hassasiyet gerektirir (Zero W için ince pense yeterli olurken, v2 için modülü gizleyen metal plakayı çıkarmak için bir Hot kalem gerekir). Bu eğitimde ayrıntılara girmeyeceğim, ancak tüm talimatları bu belgede bulabilirsiniz: *[Donanımla WiFi/Bluetooth'u devre dışı bırakma](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Lütfen dikkat: Bazı Raspberry Pi Zero modelleri önceden lehimlenmiş GPIO pinleri olmadan satılmaktadır. Doğrudan entegre pinlere sahip bir versiyon satın alabilir (en basit çözüm) veya pinleri ayrı olarak satın alıp kendiniz lehimleyebilirsiniz (daha karmaşık çözüm).
 - Bir mikro-USB güç Supply eklemeyi unutmayın.



![Image](assets/fr/002.webp)





- Waveshare 1,3" ekran (240×240 px)** (Fransızca)
    - Bu özel modeli seçmek çok önemlidir: diğer benzer ekranlar mevcuttur, ancak farklı bir çözünürlüğe sahiptir. 240×240 piksel çözünürlük olmadan ekran kullanılamaz.
    - Ekranda üç düğme ve kullanıcının Interface'sı olarak hizmet veren bir mini joystick bulunmaktadır.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero** uyumlu kamera
    - Seçenek 1: geniş altın paspaslı standart kamera (muhafazanızla uyumluluğunu kontrol edin).
    - Seçenek 2: Pi Zero için özel olarak tasarlanmış daha kompakt "*Zero*" kamera.



![Image](assets/fr/004.webp)





- MicroSD** kart
    - Önerilen kapasite: 4 ila 32 GB arasında.





- Konut (isteğe bağlı, ancak tavsiye edilir)** (isteğe bağlı, ancak tavsiye edilir)** (isteğe bağlı, ancak tavsiye edilir)** (isteğe bağlı, ancak tavsiye edilir)** (tavsiye edilir)
    - Cihazı korur ve kullanımını kolaylaştırır.
    - En popüler model, [3D baskı için açık kaynaklı STL dosyalarının mevcut olduğu] "*Orange Pill Case*"dir (https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Kutular ayrıca [projeye bağlı bağımsız satıcılardan] (https://seedsigner.com/hardware/) temin edilebilir.



![Image](assets/fr/005.webp)



Bu bileşenleri ayrı ayrı satın alabilir veya daha fazla basitlik için gerekli tüm donanımı içeren hazır paketleri tercih edebilirsiniz. Şahsen ben paketimi [bu Fransız sitesinden] (https://bitcoinbazar.fr/) sipariş ettim, ancak [SeedSigner projesi donanım sayfasında] (https://seedsigner.com/hardware/) dünyanın her bölgesi için satıcıların bir listesini de bulacaksınız. Bileşenleri tek tek satın almayı tercih ederseniz, bunlar büyük e-ticaret platformlarında veya uzman mağazalarda mevcuttur.



## 2. Yazılımın hazırlanması



Donanımınızı bir araya getirdikten sonra, SeedSigner sistemini üzerine kurarak microSD kartı hazırlamanız gerekir. Bunu yapmak için, günlük kişisel bilgisayarınıza gidin ve SeedSigner için tasarlanmış microSD'nizi takın.



### 2.1. İndir



Projenin resmi GitHub deposuna](https://github.com/SeedSigner/seedsigner/releases) gidin. Yazılımın en son sürümünde, indirin :




- Pi modelinize karşılık gelen `.img` görüntüsü.
- .sha256.txt` dosyası.
- .sha256.txt.sig' dosyası.



![Image](assets/fr/006.webp)



Kuruluma başlamadan önce yazılımı kontrol edelim.



### 2.2 Linux ve macOS altında doğrulama



SeedSigner projesinin resmi açık anahtarını doğrudan Keybase'den içe aktararak başlayın:



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal size bir anahtarın içe aktarıldığını veya güncellendiğini söylemelidir. Ardından, imza dosyası üzerinde doğrulama komutunu çalıştırın (komutu sürümünüze göre değiştirmeyi unutmayın, burada `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Her şey doğruysa, çıktıda `Good signature` (İyi imza) yazmalıdır. Bu, `.sha256.txt` dosyasının yeni içe aktardığınız anahtar tarafından imzalandığı ve imzanın geçerli olduğu anlamına gelir. Uyarı mesajını dikkate almayın `UYARI: Bu anahtar güvenilir bir imza ile onaylanmamıştır`: bu normaldir, çünkü kullanılan anahtarın SeedSigner projesine ait olup olmadığını kontrol etmek artık size kalmıştır.



Bunu yapmak için, görüntülenen parmak izinin son 16 karakterini [Keybase.io/SeedSigner](https://keybase.io/seedsigner) adresinde, [resmi Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) adresinde veya [SeedSigner.com](https://seedsigner.com/keybase.txt) adresinde yayınlanan dosyada bulunanlarla karşılaştırın. Bu tanımlayıcılar tam olarak eşleşiyorsa, anahtarın gerçekten projeye ait olduğundan emin olabilirsiniz. Şüpheniz varsa, hemen durun ve SeedSigner topluluğundan (Telegram, X, GitHub...) yardım isteyin.



Anahtar doğrulandığında, indirilen görüntünün değiştirilmediğini kontrol edebilirsiniz (komutu sürümünüze göre değiştirmeyi unutmayın, burada `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Linux altında bu komut yerleşiktir.
- Uyarı: `Big Sur (11)`den önceki macOS sürümleri `--ignore-missing` seçeneğini tanımaz. Bu durumda, bu seçeneği kaldırın ve eksik dosyalarla ilgili uyarıları yok sayın.



Beklenen sonuç, `.img` dosyasının yanında bir `OK` işaretidir. Bu, yüklenen görüntünün proje tarafından yayınlananla aynı olduğunu ve değiştirilmediğini doğrular.



### 2.3 Windows doğrulaması



Windows'ta prosedür benzerdir ancak komutlar farklıdır. Gpg4win](https://www.gpg4win.org/) yükleyerek başlayın ve *Kleopatra* uygulamasını açın. SeedSigner projesinin ortak anahtarını Keybase URL'sinden içe aktarın:



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Ardından, indirdiğiniz dosyaların bulunduğu klasörde PowerShell'i açın (`Shift` + sağ tık > `Open PowerShell here`). Manifest imzasını kontrol etmek için aşağıdaki komutu çalıştırın (komutu sürümünüze göre değiştirmeyi unutmayın, burada `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Her şey doğruysa, çıktıda `Good signature` (İyi imza) yazmalıdır. Bu, `.sha256.txt` dosyasının yeni içe aktardığınız anahtar tarafından imzalandığı ve imzanın geçerli olduğu anlamına gelir. Uyarı mesajını dikkate almayın `UYARI: Bu anahtar güvenilir bir imza ile onaylanmamıştır`: bu normaldir, çünkü kullanılan anahtarın SeedSigner projesine ait olup olmadığını kontrol etmek artık size kalmıştır.



Bunu yapmak için, görüntülenen parmak izinin son 16 karakterini [Keybase.io/SeedSigner](https://keybase.io/seedsigner) adresinde, [resmi Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) adresinde veya [SeedSigner.com](https://seedsigner.com/keybase.txt) adresinde yayınlanan dosyada bulunanlarla karşılaştırın. Bu tanımlayıcılar tam olarak eşleşiyorsa, anahtarın gerçekten projeye ait olduğundan emin olabilirsiniz. Şüpheniz varsa, hemen durun ve SeedSigner topluluğundan (Telegram, X, GitHub...) yardım isteyin.



Anahtar doğrulandıktan sonra, görüntü dosyasının bozulup bozulmadığını kontrol etmeniz gerekir. Bunu yapmak için PowerShell'de aşağıdaki komutu kullanın:



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Raspberry Pi Zero 2 için örnek (komutu sürümünüze göre değiştirmeyi unutmayın, burada `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell daha sonra görüntü dosyanızın Hash SHA256 değerini hesaplar. Bu Hash'yi `seedsigner.0.8.6.sha256.txt'deki karşılık gelen değerle karşılaştırın.




- İki değer kesinlikle aynıysa, kontrol başarılıdır ve devam edebilirsiniz.
- Farklıysa, dosya bozuk veya bozulmuş demektir. Kullanmayın ve indirmeyi yeniden başlatın.



![Image](assets/fr/013.webp)



Başarılı doğrulama, `.img` dosyanızın hem orijinal (SeedSigner tarafından imzalanmış) hem de değiştirilmemiş (değiştirilmemiş) olduğunu garanti eder. Daha sonra güvenle bir sonraki adıma geçebilirsiniz.



### 2.4. Görüntüyü flaşlayın



Henüz sahip değilseniz, [Balena Etcher] yazılımını indirin (https://etcher.balena.io/), ardından :




- MicroSD kartı bilgisayarınıza takın.
- Launch Etcher.
- İndirilen ve doğrulanan `.img` dosyasını seçin.
- Hedef olarak microSD kartı seçin.
- "Flash!" üzerine tıklayın.



![Image](assets/fr/014.webp)



İşlem tamamlanana kadar bekleyin: microSD'niz kullanıma hazırdır. Şimdi montaj zamanı!



## 3. SeedSigner montajı



MicroSD kartınız hazırlandıktan ve SeedSigner yazılımı ile flaşlandıktan sonra, son montaja geçebilirsiniz. Bazı parçalar kırılgan olduğundan (özellikle masa örtüsü, kamera ve GPIO pinleri) acele etmeyin.



### 3.1 Muhafazanın hazırlanması



Her şeyden önce, kasanızı açın. Temiz olup olmadığını ve iç bağlantı elemanlarının önünde 3D baskı plastiği kalıntısı bulunup bulunmadığını kontrol edin. Şunlara dikkat edin :




- Kamera konumu (öndeki küçük dairesel delik).
- Ekran için açılış.
- Raspberry Pi Zero'nun micro-USB portları ve microSD yuvası için kesikler.



### 3.2 Kamera kurulumu



Raspberry Pi Zero üzerindeki kamera şerit konektörünü bulun: kartın yan tarafında, açmak için hafifçe kaldırılabilen ince siyah bir şerittir. Zorlamadan dikkatlice yukarı kaldırın: sadece birkaç milimetre eğilmelidir.



![Image](assets/fr/015.webp)



Kamera kapağını yerleştirin. Kahverengi/bakır kısım aşağı bakmalıdır. Bükmeden konektöre sıkıca oturduğundan emin olun.



![Image](assets/fr/016.webp)



Masa örtüsünü kilitlemek için siyah çubuğu kapatın (hafif bir tıklama hissedeceksiniz). Yerinde durduğunu ve hareket etmediğini yavaşça kontrol edin.



![Image](assets/fr/017.webp)



Ardından kamera modülünü muhafazadaki uygun deliğe yerleştirin. Modele bağlı olarak, doğrudan yerine oturabilir veya yerinde tutmak için küçük bir yapışkan şerit gerekebilir. Lens, dışa bakacak şekilde mükemmel bir şekilde hizalanmalıdır.



### 3.3 Raspberry Pi Zero'nun Kurulumu



Eğer bir kılıf kullanıyorsanız, Raspberry Pi Zero kartını içine yerleştirin. Bağlantı noktalarını sağlanan açıklıklarla dikkatlice hizalayın.



Ardından Waveshare ekranı Raspberry Pi Zero'nun üzerine yerleştirin. Pi'nin GPIO pinleri ekranın dişi konektörü ile mükemmel bir şekilde hizalanmalıdır. Ekranı yavaşça pimlerin üzerine bastırın, bükülmelerini önlemek için her iki tarafa eşit basınç uygulayın.



![Image](assets/fr/018.webp)



Eğer bir kasanız varsa, ön paneli ve kumanda kolunu ekleyerek montajı tamamlayın.



Son olarak, flaşlanmış yazılımı içeren microSD kartı Raspberry Pi Zero'nun kenara monte edilmiş yuvasına yerleştirin. Yerine oturduğundan emin olun.



### 3.4 İlk çalıştırma



Özel bağlantı noktasına bir mikro-USB güç kablosu bağlayın. Yaklaşık bir dakika bekleyin. SeedSigner logosu ve ardından ana ekran görünmelidir.



![Image](assets/fr/019.webp)



Başlangıç olarak, `Ayarlar > I/O testi` menüsüne giderek çeşitli bileşenlerin düzgün çalışıp çalışmadığını kontrol edin.



![Image](assets/fr/020.webp)



Tüm düğmeleri test edin ve doğru yanıt verdiklerinden emin olun. Ardından kameranın beklendiği gibi çalışıp çalışmadığını kontrol etmek için `KEY1` düğmesine tıklayın. Bu bir fotoğraf çekecektir.



![Image](assets/fr/021.webp)



### 3.5 Kamera ayarı



SeedSigner'ınızı nasıl monte ettiğinize bağlı olarak, kamera ters bir görüntü gösterebilir. Bunu düzeltmek için, `Ayarlar > Gelişmiş > Kamera döndürme` bölümüne gidin ve gerekirse 180° döndürmeyi seçin.



![Image](assets/fr/022.webp)



Kamera yönünü değiştirdiyseniz veya daha sonraki bir tarihte diğer ayarları (Interface dili gibi) değiştirmek istiyorsanız, microSD'de ayarların kalıcılığını etkinleştirmeniz gerekir. Aksi takdirde, Raspberry Pi Zero'nun kalıcı belleği olmadığından, her yeniden başlattığınızda ayarlarınız varsayılana geri dönecektir.



Bunu yapmak için, `Ayarlar > Kalıcı ayarlar` menüsünü açın ve ardından `Etkin` seçeneğini seçin.



![Image](assets/fr/023.webp)



Her şey çalışır durumdaysa, SeedSigner'ınız artık kullanıma hazırdır!



## 4. SeedSigner ayarları



Bitcoin Wallet'nizi oluşturmadan önce, SeedSigner'ı yapılandıralım. Kalıcı belleği olmayan bir Raspberry Pi Zero üzerinde çalıştığı için, microSD karta kaydetmediğiniz sürece ayarları otomatik olarak kaydedilmez. Bu yüzden bu seçeneği etkinleştirdiğinizden emin olun, aksi takdirde bu ayarlar yeniden başlatıldığında kaybolacaktır (bkz. adım 3.5).



### 4.1 Parametre menüsüne erişim



SeedSigner'ınızı başlatın ve ana ekranın görünmesini bekleyin. Kumanda kolunu kullanarak `Ayarlar` seçeneğine gidin, ardından orta düğmeye basarak onaylayın. Şimdi ana ayarlar menüsüne giriyorsunuz.



![Image](assets/fr/024.webp)



### 4.2 Portföy yönetim yazılımını seçme



Ardından `Koordinatör yazılımı` menüsüne erişin.



![Image](assets/fr/025.webp)



Koordinatör, SeedSigner'ınızın QR kodları aracılığıyla iletişim kuracağı portföy yönetim yazılımını ifade eder. Bu yazılım bilgisayarınıza ya da akıllı telefonunuza yüklenir. Özel anahtarlarınıza erişiminiz olmadan bitcoinlerinizi yönetmenizi sağlayacaktır. SeedSigner, işlemlerinizi imzalayabilen tek cihaz olarak kalır.



Mevcut aygıt yazılımı sürümü çeşitli yazılım paketlerini desteklemektedir: Sparrow, Spectre, BlueWallet, Nunchuk ve Keeper. Benim durumumda, basitliği ve zengin işlevselliği nedeniyle özellikle tavsiye ettiğim **Sparrow wallet** kullanıyorum.



Nasıl kurulacağını bilmiyorsanız, bu öğreticiyi takip edebilirsiniz:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Menüden istediğiniz yazılımı seçmeniz yeterlidir.



![Image](assets/fr/026.webp)



### 4.3 Birimler ve miktar göstergesi



Nominal Gösterge` menüsünde, tutarların gösterileceği birimi seçebilirsiniz:




- bTC`
- mBTC` (mili-Bitcoin veya 0,001 BTC)
- gW-20 (satoshis veya 1/100.000.000 BTC)



Sats** ünitesi genellikle küçük miktarlar için en pratik olanıdır.



![Image](assets/fr/027.webp)



### 4.4 Gelişmiş ayarlar



Şimdi `Gelişmiş` menüsüne gidin. Burada birkaç faydalı seçenek bulacaksınız:




- gW-22 network`: yalnızca Testnet üzerinde SeedSigner kullanmak istiyorsanız değiştirilmelidir.
- qR kod yoğunluğu`: her QR kodunda bulunan bilgi miktarını ayarlar. Tarama sırasında okumayı zor bulmadığınız sürece varsayılan değeri bırakabilirsiniz.
- `Xpub export`: genişletilmiş açık anahtarınızın (`xpub`, `ypub`, `zpub`) QR kodu aracılığıyla portföy yönetim yazılımına aktarılmasını etkinleştirir veya devre dışı bırakır (daha sonra kullanacağımız bir işlev, bu nedenle şimdilik etkin bırakın).
- script types`: bitcoinlerinizi kilitlemenize izin verilen script türlerini tanımlar. Komut dosyası türü doğrudan Sparrow olarak ayarlanacağı için bu parametreyi değiştirmenize gerek yoktur. Burada, yalnızca SeedSigner'ın manipüle etme yetkisine sahip olduğu komut dosyaları söz konusudur.



### 4.5 Dil seçimi



Son olarak, `Language` menüsünde, Interface'nin dilini tercihinize uyacak şekilde değiştirebilirsiniz.



![Image](assets/fr/028.webp)



## 5. seed'in oluşturulması ve kaydedilmesi



seed (veya Mnemonic ifadesi) Bitcoin portföyünüzün temelini oluşturur. Özel anahtarlarınızı ve adreslerinizi türetmek için kullanılır ve fonlarınıza erişim sağlar. SeedSigner bunu oluşturmak için bu bölümde inceleyeceğimiz çeşitli yöntemler sunar.



Başlamadan önce, birkaç önemli hatırlatma:




- Bu ifade size tüm bitcoinlerinize tam ve sınırsız erişim sağlar.** Bu ifadeye sahip olan herkes, SeedSigner'ınıza fiziksel erişimi olmasa bile fonlarınızı çalabilir;
- Genellikle, bir Hardware Wallet kaybolduğunda veya çalındığında Wallet'ü geri yüklemek için 12 kelimelik bir ifade kullanılır. Ancak SeedSigner *durumsuz* bir cihaz olduğu için seed'ünüzü asla kaydetmez. Dolayısıyla fiziksel yedekleriniz yalnızca yedek kopyalar değil, **Wallet'ünüzü kullanmanın tek yoludur**. Bu yedekleri kaybederseniz, bitcoinleriniz kalıcı olarak kaybolacaktır. Bu yüzden onları dikkatlice, çeşitli ortamlarda ve güvenli yerlerde yedekleyin;
- Yeni başlıyorsanız, bir Mnemonic ifadesini yönetirken karşılaşabileceğiniz riskleri ayrıntılı olarak anlamak için bu eğitimi okumanızı şiddetle tavsiye ederim:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 seed oluşturma aracına erişin



SeedSigner ana ekranından `Araçlar` menüsüne gidin.



![Image](assets/fr/029.webp)



Şimdi generate'nizi seed yapacaksınız. seed basitçe büyük bir rastgele sayıdır. Ne kadar rastgele üretilirse o kadar güvenli olur. SeedSigner bunu yapmak için iki yol sunar:




- kamera": seed bir fotoğrafın görsel gürültüsünden üretilir. Piksel değişimleri generate entropisi için kullanılan rastgele bir ortamın (nesne, manzara, yüz, vb.) görüntüsünü alırsınız. Hızlı bir yöntemdir, ancak tekrarlanabilir değildir.
- zar atar": gerekli entropiyi yaratmak için zar atarsınız. Daha fazla zaman alır, ancak tekrarlanabilir ve bu nedenle doğrulanabilir. Bu yöntemi tercih ederseniz, bu eğitimdeki tavsiyeleri izleyin (burada sağlama toplamını hesaplamanıza gerek yok, SeedSigner bunu hallediyor):



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Fotoğraf ile seed'in oluşturulması



Fotoğraf yöntemini seçerseniz, `Yeni seed` (kamera simgesi ile) üzerine tıklayın, bir fotoğraf çekin ve onaylayın. Daha sonra cümlenizin uzunluğunu seçin (12 veya 24 kelime), kaydedilmek üzere ekranda görünecektir. Aşağıdaki adımlar bölüm 5.3 ile aynıdır.



### 5.3 Zar ile seed Oluşturma



Bu eğitimde **Zar Atma** yöntemini kullanacağız. Yeni seed`e tıklayın (zar simgesi ile).



![Image](assets/fr/030.webp)



Ardından Mnemonic ifadenizin uzunluğunu seçin. 12 kelime zaten yeterli bir güvenlik seviyesi sunuyor, bu yüzden önerdiğim seçim bu.



![Image](assets/fr/031.webp)



Zarınızı atın ve ortaya çıkan sayıları imleci kullanarak girin. Her girişi doğrulamak için orta düğmeye basın. Eğer bir hata yaparsanız, geri dönebilirsiniz. Dengesiz zarların etkisini azaltmak için birkaç farklı zar kullanın. Bu işlem sırasında izlenmediğinizden emin olun.



![Image](assets/fr/032.webp)



50 atışınızı girdikten sonra SeedSigner cümlenizi oluşturur. **Yeni başlıyorsanız bu eğitimdeki talimatları dikkatlice izleyin:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 seed'nın görüntülenmesi ve kaydedilmesi



Mnemonic ifadenizin kelimelerini dikkatlice uygun bir fiziksel desteğin (kağıt veya metal) üzerine yazın.



![Image](assets/fr/033.webp)



### 5.5 Yedeklemenin kontrol edilmesi



Herhangi bir yedekleme hatasını önlemek için SeedSigner sizden yedeklemenizi doğrulamanızı ister. Doğrula'ya tıklayın.



![Image](assets/fr/034.webp)



Daha sonra istenen kelimeyi cümledeki sırasına göre girin. Örneğin, burada cümlemdeki üçüncü kelimeyi seçmem gerekiyor.



![Image](assets/fr/035.webp)



Bir hata yaparsanız, SeedSigner sizi bilgilendirecek ve size verildiğinde Mnemonic ifadenizi not ettiğinizden emin olarak yeniden başlamanız gerekecektir. Bu doğrulama adımı yedeklemenizin doğru ve eksiksiz olmasını sağlar. Doğrulama yapıldıktan sonra ekranda `Yedekleme Doğrulandı` yazısı görüntülenecektir.



![Image](assets/fr/036.webp)



Daha eksiksiz bir restorasyon testi için bu öğreticiyi izleyin:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 "Vatansız cihaz" kavramını anlamak



SeedSigner kalıcı hafızası olmayan bir cihazdır. Bu, seed'nizin asla cihazın içinde saklanmadığı anlamına gelir (örneğin bir Ledger, Trezor veya Coldcard'ın aksine). Gücü kapattığınız anda, seed RAM'inden tamamen kaybolur. SeedSigner yeniden başlatıldığında, boş bir duruma geri döner: işlemlerinizi imzalamak için seed'nizi tekrar vermeniz gerekir.



Bu temel koruma sağlar. Diğer donanım cüzdanlarının aksine SeedSigner, *secure element* dahil olmak üzere hiçbir fiziksel koruması olmayan bir Raspberry Pi Zero'ya dayanmaktadır. Ancak hiçbir hassas veri depolanmadığından, fiziksel olarak tehlikeye atılmış bir cihaz bile bir saldırganın özel anahtarlarınızı çıkarmasına veya bitcoinlerinizi harcamasına izin vermez.



Öte yandan, bu mimari ek bir sorumluluk anlamına gelir: yedekleme olmadan, fonlarınız kesinlikle kaybolur. Bu yüzden **çift yedekleme** öneriyorum. Kurtarma cümlenize zaten sahipsiniz: bu, güvenli bir yerde tutulması gereken uzun vadeli ana yedeğinizdir. Şimdi bu ifadenin **QR kodu** şeklinde bir kopyasını oluşturacağız.



SeedSigner'ı her kullandığınızda, bu QR kodunu cihazın kamerasıyla tararsınız, böylece siz işlemlerinizi imzalarken seed'nizi geçici olarak belleğine yükler. Günlük kullanım için tasarlanan bu ikinci yedek de son derece dikkatli bir şekilde saklanmalıdır: bu QR koduna sahip olan herkes bitcoinlerinize tam erişime sahiptir.


Ayrıca, bir hak talebi durumunda her şeyi kaybetmemek için QR kodunuzu ve Mnemonic ifadenizi iki ayrı yerde saklamanızı tavsiye ederim.



Son olarak, daha gelişmiş ve güvenli bir alternatif, SeedSigner'ı seed'i bir secure element'te saklayan bir **SeedKeeper** ile kullanmaktır. Daha fazlasını öğrenmek için bu eğiticiye bakın:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Ana anahtar parmak izi yaz



Doğrulama tamamlandığında, SeedSigner Wallet'nızın ana anahtarının parmak izini görüntüler. Bu parmak izi Wallet'nızı tanımlar ve gelecekte doğru kurtarma ifadesini kullanmanızı sağlar. Özel anahtarlarınız hakkında herhangi bir bilgi vermez, bu nedenle dijital bir ortamda güvenle saklayabilirsiniz. Sadece erişilebilir bir kopyasını sakladığınızdan ve asla kaybetmediğinizden emin olun.



![Image](assets/fr/037.webp)



Ayrıca bu aşamada Wallet'inizin güvenliğini güçlendirmek için bir **passphrase BIP39** ekleyebilirsiniz. Yedekleme stratejinize bağlı olarak bu seçenek faydalı olabilir, ancak aynı zamanda riskler de içerir: passphrase'yi kaybederseniz, bitcoinlerinize erişim kalıcı olarak kaybolacaktır.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

passphrase konseptine henüz aşina değilseniz, sizi konuyla ilgili bu kapsamlı eğitimi okumaya davet ediyorum:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 seed'ı QR formatında kaydetme (*SeedQR*)



SeedSigner, seed'nizi *SeedQR* adı verilen bir kağıt QR koduna dönüştürmenizi sağlar. Bu yöntem, her kelimeyi manuel olarak yeniden yazmayı önlediği için Wallet'inizi yeniden yüklemeyi basitleştirir.



Bunu yapmak için, Mnemonic ifadenizin uzunluğuna karşılık gelen boş bir kağıt veya metal QR koduna ihtiyacınız olacaktır. SeedSigner'ınız için komple bir paket satın aldıysanız, şablonlar genellikle pakete dahildir. Değilse, buradan indirebilir ve yazdırabilirsiniz (veya elle çoğaltabilirsiniz) :




- [12 kelimelik format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24 kelimelik format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompakt format 12 kelime](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompakt format 24 kelime](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



seed ekranınızdan `seed`ü Yedekle`yi seçin.



![Image](assets/fr/039.webp)



Ardından `Export as SeedQR` öğesini seçin.



![Image](assets/fr/040.webp)



Ardından mevcut kağıt şablonuna göre istediğiniz biçimi (normal veya kompakt) seçin.



![Image](assets/fr/041.webp)



TohumQR* oluşturmaya başlamak için `Başla` düğmesine tıklayın. SeedSigner daha sonra her biri kodun bir bölümüne karşılık gelen bir dizi ızgara (A1, A2, B1, vb.) görüntüleyecektir.



![Image](assets/fr/042.webp)



Kayıt sayfanızdaki her siyah noktayı dikkatlice yeniden oluşturun, ardından bir sonraki BLOCK'e geçmek için joystick'i kullanın. Acele etmeyin: basit bir yanlış hizalama QR kodunu kullanılamaz hale getirebilir.



Birkaç ipucu:




- Hataları düzeltebilmek için kurşun kalemle başlayın ve işiniz bittiğinde ince siyah bir kalem kullanmaya devam edin;
- İhtiyacınız olan tek şey karenin ortasında iyi ortalanmış bir noktadır, tamamen doldurmanıza gerek yoktur.



![Image](assets/fr/043.webp)



Ardından `Confirm SeedQR` seçeneğine tıklayın ve doğru çalışıp çalışmadığını kontrol etmek için QR kodunuzu tarayın.



![Image](assets/fr/044.webp)



Eğer `Başarılı` mesajı görüntülenirse, *SeedQR*'niz geçerlidir: bir sonraki adıma geçebilirsiniz.



![Image](assets/fr/045.webp)



**Bu sayfayı kurtarma ifadeniz kadar sıkı bir şekilde saklayın. Bu QR koduna sahip olan herkes özel anahtarlarınızı yeniden oluşturabilir ve bitcoinlerinizi çalabilir.**



Tebrikler, Bitcoin portföyünüz artık hazır ve çalışıyor! Şimdi kolayca yönetmek için genel bileşenlerini **Sparrow wallet**'ya aktaracağız.



## 6. Wallet'u Sparrow'e aktarın



SeedSigner'ınız kurulduktan ve seed'niz doğru şekilde oluşturulup kaydedildikten sonra, bir sonraki adım bu portföyü Sparrow wallet gibi bir yönetim yazılımına bağlamaktır. Portföyünüzün yalnızca halka açık kısmı Sparrow'e aktarılacağından seed'niz her zaman çevrimdışı kalacaktır. Bu, yazılımın bitcoinlerinizi harcayamadan adreslerinizi, işlemlerinizi görüntülemesini ve yeni işlemler oluşturmasını sağlayacaktır. Bitcoinlerinizi harcamak için SeedSigner'ınızın her zaman Sparrow tarafından hazırlanan işlemi imzalaması gerekecektir.



### 6.1 SeedSigner'ın Hazırlanması



İşletim sistemini içeren microSD'yi takın, SeedSigner'ınızı açın, ardından yedek QR kodunuzdan yeni oluşturduğunuz seed'ü yükleyin. Ana ekranda `Tarama` seçeneğini seçin, ardından SeedQR'nizi SeedSigner ile tarayın.



![Image](assets/fr/046.webp)



Ana anahtarınızdaki parmak izinin Wallet'inizdeki parmak iziyle eşleşip eşleşmediğini kontrol edin. Bir passphrase kullanıyorsanız, bu aşamada onu girin.



![Image](assets/fr/047.webp)



Bu sizi portföyünüzün menüsüne götürür, benim durumumda `d4149b27` olarak adlandırılmıştır. Ana ekrana geri döndüğünüzde, `Seeds` seçeneğini seçin, ardından portföyünüze karşılık gelen baskıyı seçin. Ardından `Export Xpub` seçeneğine tıklayın.



![Image](assets/fr/048.webp)



Portföy türünü seçin. Bizim durumumuzda, bu tek bir portföydür: `Single Sig` seçeneğini seçin.



![Image](assets/fr/049.webp)



Daha sonra komut dosyası standardı seçimi gelir. İşlem maliyetleri açısından en yeni ve en ekonomik olanı `Taproot`dır. Bu nedenle bu standardı seçmenizi tavsiye ederim.



![Image](assets/fr/050.webp)



Bir uyarı mesajı görünecektir. Bu normaldir: bu genişletilmiş genel anahtar (`xpub`), seed'nizden (ilk hesapta) türetilen tüm adresleri görüntülemenizi sağlar. Fonlarınızı harcamanıza izin vermez, ancak portföyünüzün yapısını ortaya çıkarır. Eğer sızarsa, bu gizliliğiniz için bir sorundur, ancak bitcoinlerinizin güvenliği için değil: onları görmenize izin verir, ancak harcamanıza izin vermez.



Görüntülenen bilgilerden memnunsanız `Anladım` ve ardından `Xpub'ı Dışa Aktar` seçeneğine tıklayın.



SeedSigner daha sonra portföyünüzü Sparrow wallet'de yönetmek için ihtiyaç duyduğunuz tüm verileri içeren dinamik bir QR kodu şeklinde xpub'ınızı oluşturur.



![Image](assets/fr/051.webp)



Daha kolay QR kodu taraması için ekran parlaklığını ayarlamak üzere joystick'i kullanabilirsiniz.



### 6.2 Yeni bir portföyün Sparrow wallet'a aktarılması



Bilgisayarınızda Sparrow wallet yazılımının yüklü olduğundan emin olun. Yazılımı nasıl indireceğinizi, kontrol edeceğinizi ve doğru şekilde yükleyeceğinizi bilmiyorsanız, lütfen konuyla ilgili tam eğitimimize bakın:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Bilgisayarınızda Sparrow wallet'i açın, ardından menü çubuğunda `Dosya → Wallet'yi İçe Aktar'a tıklayın.



![Image](assets/fr/052.webp)



SeedSigner'a kaydırın ve ardından `Tara...` öğesini seçin. Web kameranız açılacaktır: SeedSigner ekranınızda görüntülenen dinamik QR kodunu tarayın.



![Image](assets/fr/053.webp)



Portföyünüze bir isim atayın, ardından `Wallet Oluştur`a tıklayın. Sparrow daha sonra sizden bu Wallet'ya yerel erişimi kilitlemek için bir parola belirlemenizi isteyecektir. Güçlü bir parola seçin: Sparrow'teki portföy verilerinize (genel anahtarlar, adresler, etiketler ve işlem geçmişi) erişimi korur. Portföyü daha sonraki bir tarihte geri yüklemek için bu şifreye gerek yoktur: bu amaçla yalnızca Mnemonic ifadeniz (ve muhtemelen passphrase'ünüz) gereklidir.



Kaybetmemek için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.



![Image](assets/fr/054.webp)



Anahtar deponuz şimdi başarıyla içe aktarıldı.



![Image](assets/fr/055.webp)



Ardından Sparrow'de görüntülenen `Ana parmak izi`nin SeedSigner'ınızda daha önce kaydedilenle eşleşip eşleşmediğini kontrol edin.



SeedSigner'ınız ve Sparrow wallet artık güvenli bir şekilde bağlantılıdır. SeedSigner işlemlerinizi imzalayabilen tek cihaz olarak kalırken Sparrow, Interface'un tam bir yönetimi olarak görev yapar. Artık tamamen hava boşluklu bir konfigürasyonda bitcoin almaya ve göndermeye hazırsınız.



## 7. Bitcoin alma ve gönderme



SeedSigner'ınız ve Sparrow wallet artık birlikte çalışacak şekilde yapılandırılmıştır. Bu son bölümde, bu yapılandırmayı kullanarak bitcoinleri nasıl alacağımızı ve göndereceğimizi inceleyeceğiz.



### 7.1 Bitcoin alma



#### 7.1.1 Bir alımın oluşturulması Address



Bilgisayarınızda Sparrow wallet'ü açın ve şifrenizi kullanarak SeedSigner Wallet'ün kilidini açın. Yazılımın bir sunucuya bağlı olduğundan emin olun (sağ alttaki çentik). Kenar çubuğunda, `Alıcı` üzerine tıklayın.



![Image](assets/fr/056.webp)



Yeni bir Bitcoin Address görüntülenir. Göreceksiniz :




- Address metni (benim yaptığım gibi P2TR kullanıyorsanız `bc1p...` ile başlar),
- İlgili QR kodu,
- İşlemlerinizi izlemek için bir `Etiket` alanı.



Wallet'ünüzdeki her bir Bitcoin makbuzuna bir etiket eklemenizi şiddetle tavsiye ederim. Bu, her bir UTXO'in kaynağını kolayca tanımlamanıza ve gizlilik yönetiminizi geliştirmenize olanak sağlayacaktır. Bu önemli konuyu daha derinlemesine incelemek için Plan ₿ Academy'deki özel eğitime göz atabilirsiniz:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Etiket eklemek için `Etiket` alanına bir isim girmeniz ve ardından onaylamanız yeterlidir.



Örneğin:



```txt
Label : Sale of the Raspberry Pi Zero
```



Address'niz artık tüm Sparrow bölümlerinde bu etiketle ilişkilendirilmiştir.



![Image](assets/fr/057.webp)



#### 7.1.2 SeedSigner üzerinde Address doğrulaması



Aldığınız Address'yı paylaşmadan önce, bunun seed'inize ait olduğunu kontrol etmeniz çok önemlidir. Bu adım, SeedSigner'ınızın bu Address ile ilişkili işlemleri imzalayabilmesini sağlar. Ayrıca Sparrow'nin sahte bir Address görüntülediği olası saldırılara karşı da koruma sağlar. Sparrow'nin tamamen yalıtılmış olan SeedSigner'ınızdan çok daha büyük bir saldırı yüzeyine sahip olan güvensiz bir ortamda (bilgisayarınız) çalıştığını unutmayın. Bu nedenle, Hardware Wallet'inizle doğrulamadan Sparrow'de görüntülenen herhangi bir alıcı Address'ya asla körü körüne inanmamalısınız.



Sparrow'da, büyütmek için Address'un QR koduna tıklayın: daha sonra tam ekran görüntülenecektir.



![Image](assets/fr/058.webp)



SeedSigner'ınızda, ana menüden `Tarama` seçeneğini seçin. Bilgisayar ekranınızda görüntülenen QR kodunu tarayın, ardından Wallet'inize karşılık gelen seed'yi seçin (benim durumumda `d4149b27` parmak izi).



![Image](assets/fr/059.webp)



Taranan Address, seed'ünüzden elde edilenle eşleşirse, SeedSigner ekranında şu mesaj görüntülenecektir: "Address Doğrulandı".



![Image](assets/fr/060.webp)



Bu, Address'in Wallet'nıza ait olduğunu ve ondan güvenle bitcoin alabileceğinizi onaylar.



#### 7.1.3 Fonların teslim alınması



Artık bu Address'i (metin veya QR kodu biçiminde) size Satss göndermesi gereken kişiye veya departmana iletebilirsiniz. İşlem ağ üzerinde yayınlandıktan sonra, Sparrow wallet'nin `İşlemler` sekmesinde görünecektir.



![Image](assets/fr/061.webp)



### 7.2 Bitcoin gönderin



SeedSigner ile bitcoin göndermek 3 adımlı bir süreçtir:




- Sparrow'da işlem oluşturma;
- SeedSigner üzerindeki işlemin imzası;
- İşlemin Sparrow üzerinden nihai dağıtımı.



İki cihaz arasındaki tüm alışverişler yalnızca QR kodları kullanılarak yapılır.



#### 7.2.1 Sparrow'de işlem oluşturma



Sparrow wallet'de sol taraftaki kenar çubuğunda bulunan `Gönder` sekmesine tıklayabilirsiniz. Ancak ben "*Coin Kontrolü*" uygulamanızı sağlayan "UTXOs" sekmesini kullanmayı tercih ediyorum. Bu yöntem size kullanılan UTXO'lar üzerinde hassas kontrol sağlar, böylece işlem sırasında ortaya çıkardığınız bilgileri kontrol edebilirsiniz.



UTXOs sekmesinde, harcamak istediğiniz madeni paraları seçin ve ardından `Seçilenleri Gönder` seçeneğine tıklayın.



![Image](assets/fr/062.webp)



Ardından işlem alanlarını doldurun:




- 'Ödeme yapılacak' kısmına alıcının Address numarasını yapıştırın veya QR kodunu taramak için kamera simgesine tıklayın;
- Etiket` alanına, bu gideri izlemek için bir etiket ekleyin;
- Tutar` alanına gönderilecek tutarı girin;
- Son olarak, mevcut piyasa koşullarına göre ücret oranını seçin (tahminler [Mempool.space](https://Mempool.space/) adresinde mevcuttur).



Alanlar doldurulduktan sonra, bilgileri dikkatlice kontrol edin ve ardından `İşlem Oluştur >>` seçeneğine tıklayın.



![Image](assets/fr/063.webp)



Her şeyin doğru olduğundan emin olmak için işlem ayrıntılarını kontrol edin ve ardından `İmzalama için İşlemi Sonlandır` seçeneğine tıklayın.



![Image](assets/fr/064.webp)



İşlem artık hazır, ancak henüz imzalanmadı. PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) QR kodu olarak görüntülemek için `Kareyi Göster` seçeneğine tıklayın.



![Image](assets/fr/065.webp)



#### 7.2.2 SeedSigner ile işlemin imzalanması



SeedSigner'ınızı açın ve her zamanki gibi portföyünüze erişmek için SeedQR'nizi tarayın. Ana ekrandan `Tarama` seçeneğini seçin, ardından Sparrow üzerinde görüntülenen QR kodunu tarayın.



![Image](assets/fr/066.webp)



Ardından portföyünüze uygun seed'u seçin.



![Image](assets/fr/067.webp)



SeedSigner bunun bir PSBT olduğunu otomatik olarak algılar ve işlemin bir özetini görüntüler:




   - Gönderilen miktar,
   - Çıkış adresleri,
   - İlişkili işlem maliyetleri.



Ayrıntıları İncele'ye tıklayın ve doğrudan SeedSigner ekranındaki tüm bilgileri dikkatlice kontrol edin. Kontrol edilmesi gereken en önemli öğeler gönderilen miktar, alıcının Address numarası ve uygulanan ücretlerin miktarıdır.



![Image](assets/fr/068.webp)



Her şey doğruysa, ilgili özel anahtar(lar)ı kullanarak işlemi imzalamak için `PSBT`yi Onayla`yı seçin.



![Image](assets/fr/069.webp)



İmzalandıktan sonra SeedSigner, imzalanan işlemi içeren ve Sparrow tarafından taranmaya hazır yeni bir QR kodu oluşturur.



![Image](assets/fr/070.webp)



#### 7.2.3 İşlemin Sparrow'ten yayınlanması



Artık işlem geçerli olduğuna göre, Bitcoin ağında yayınlanması gerekir, böylece bir BLOCK'ya ekleyecek olan bir Miner'ye ulaşır.



Sparrow üzerinde `QR Taraması` üzerine tıklayın.



![Image](assets/fr/071.webp)



SeedSigner'ınız tarafından görüntülenen QR kodunu (imzalanan işlemin kodu) web kamerasına gösterin. Sparrow imzanın kodunu çözecek ve işlem detaylarının tamamını görüntüleyecektir. Tüm bilgilerin doğru olup olmadığını son bir kez kontrol edin, ardından Bitcoin ağında yayınlamak için İşlemi Yayınla'ya tıklayın.



![Image](assets/fr/072.webp)



İşleminiz şimdi Bitcoin ağına gönderildi. İşlemin ilerleyişini Sparrow wallet'in `İşlemler` sekmesinden takip edebilirsiniz.



![Image](assets/fr/073.webp)



Artık SeedSigner'ı kullanmanın temellerini öğrendiniz. Bilginizi derinleştirmek ve daha gelişmiş kullanımları keşfetmek için sizi aşağıdaki eğitime başvurmaya davet ediyorum:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[SeedSigner açık kaynak projesinin gelişimini bitcoin ile bağış yaparak da destekleyebilirsiniz!](https://seedsigner.com/donate/)**



*Kredi: Bu eğitimdeki bazı görseller [resmi SeedSigner proje web sitesi](https://seedsigner.com/) ve [GitHub deposu](https://github.com/SeedSigner/seedsigner)'dan alınmıştır.*