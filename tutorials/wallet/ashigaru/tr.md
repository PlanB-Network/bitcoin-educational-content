---
name: Ashigaru
description: Bitcoinlerinizi güvence altına almak, yönetmek ve karıştırmak için Samourai Wallet'dan fork
---

![cover](assets/cover.webp)



Ashigaru, Samourai Wallet projesinin devamı niteliğinde, ancak yeni bir formda olan bir Bitcoin mobil wallet uygulamasıdır. Bu yazılım özel bir bağlamda doğmuştur: Nisan 2024'te Samourai Wallet'ün kurucuları Amerikan makamları tarafından tutuklanmış ve sunucularına el konulmuştur. Samurai uygulamasının kendisi kullanılabilir durumda kalsa da, şu anda artık sürdürülmemektedir. Ashigaru, Samurai Wallet'ün ücretsiz bir fork sürümüdür ve Samurai'nin işlevselliğinin sürekliliğini garanti etmek ve orijinal felsefesini korumak için anonim bir ekip tarafından sürdürülmektedir: Bitcoin kullanıcılarının gizliliğini ve egemenliğini savunmak.



Ashigaru, Samourai'nin DNA'sının çoğunu alır: benzer bir arayüz, açıkça kendi kendine gözetim yaklaşımı, açık kaynak ve gizliliğe odaklanma. Kod, herkesin yazılımı denetleyebilmesini, değiştirebilmesini veya yeniden dağıtabilmesini sağlayan GNU GPLv3 lisansı altında dağıtılmaktadır.



Ashigaru uygulaması, UTXO'larınızın gizliliği ve yönetimi için bir dizi gelişmiş aracı entegre eder:




- Zerolink tabanlı bir coinjoin protokolü olan Whirlpool**, fonlarınız üzerindeki egemenliğinizi kaybetmeden işlem girişleri ve çıkışları arasındaki deterministik bağlantıları kırmanıza olanak tanır.
- Yeniden kullanılabilir ödeme kodları (BIP47) uygulayan PayNym**, artık bir "*Pepehash*" avatar sistemiyle temsil ediliyor.
- Ricochet**, işlemlerin izlenmesini zorlaştırmak için işlemlere ara sıçramalar ekleyen bir özellik.
- Ve tabii ki UTXO'larınızı hassas bir şekilde seçmek, dondurmak ve etiketlemek için ***Coin Control***.
- Toplu Harcama***, birkaç ödemeyi tek bir işlemde gruplayarak maliyetleri düşürmek için.
- Telefonunuzun fiziksel olarak incelenmesi sırasında fark edilmemesi için cep telefonunuzdaki uygulamayı sahte bir başlatıcının arkasına gizleyen **Gizli Mod**.
- Gizliliğinizi optimize etmek için gelişmiş harcama araçları (payjoin, stonewall...).
- Passphrase BIP39 kullanılarak optimize edilmiş bir kurtarma sistemi.
- İşlem ücretlerinin seçimini otomatik olarak optimize eden bir sistem.



![Image](assets/fr/01.webp)



Bu nedenle Ashigaru, Bitcoin'deki işlem izlenebilirliğini çevreleyen sorunların farkında olan kullanıcılara yöneliktir. İster gizlilik bilincine sahip bir kullanıcı, ister kendi kendini saklama konusunda kararlı deneyimli bir bitcoin kullanıcısı ya da artan gözetim risklerine maruz kalan bir birey olun, bu wallet uygulaması size Bitcoin'deki faaliyetlerinizin kontrolünü yeniden kazanmanız için gereken araçları sağlar.



Ashigaru, bu eğitimde keşfedeceğimiz uygulaması aracılığıyla mobil bir versiyonda mevcuttur. Ancak, gelecekteki bir eğitimde tanıtacağımız ***Ashigaru Terminal*** ile PC'de de kullanılabilir.



![Image](assets/fr/02.webp)



Bu eğitimde size Ashigaru'nun temel kullanımını tanıtmak istiyorum: kurulum, Dojo'ya bağlantı, yedekleme, bitcoin alma ve gönderme. Gelişmiş araçlar diğer özel eğitimlerde sunulacaktır.



## 1. Ashigaru için Ön Koşullar



Uygulamanın düzgün çalışması için birkaç ön koşul gerekiyor. Her şeyden önce, Google Play Store veya App Store gibi klasik mağazalarda bulunan bir uygulama değildir. Telefonunuza yalnızca Tor ağı üzerinden indirilebilen `.apk` dosyasından manuel olarak yüklenir. Yani bir iPhone kullanıyorsanız, bu yöntem işe yaramayacaktır: bir Android cihaza ihtiyacınız olacaktır.



Tor üzerinden `.apk` dosyasını indirmek için, `.onion` sitelerine erişebilen bir tarayıcıya ihtiyacınız olacaktır. Bunun en kolay yolu, [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) ya da doğrudan [kendi `.apk` dosyası aracılığıyla](https://www.torproject.org/download/#android) Tor Browser uygulamasını telefonunuza yüklemektir.



![Image](assets/fr/03.webp)



Yeni akıllı telefonların çoğu, varsayılan olarak bilinmeyen kaynaklardan gelen uygulamaların yüklenmesini engeller. Yüklemeye izin vermek için cihaz ayarlarınızda Tor Browser için bu seçeneği geçici olarak etkinleştirmeniz gerekir. Uygulama yüklendikten sonra, telefonunuzun güvenliğini güçlendirmek için bu işlevi devre dışı bırakmayı unutmayın.



Ashigaru'yu kullanmak için bir diğer önemli ön koşul da bir Bitcoin Dojo düğümüdür. Güvenlik ve egemenlik nedenleriyle, Ashigaru ekibi uygulamanızı bağlamak için merkezi bir sunucu bulundurmamaktadır. Bu nedenle kendi Dojo örneğinizi çalıştırmanız veya güvenilir bir tanesine bağlanmanız gerekir.



Dojo, Ashigaru uygulamanızın blok zinciri bilgilerine başvurmasını, adres bakiyelerinizi görüntülemesini ve işlemlerinizi Bitcoin ağında yayınlamasını sağlar.



Dojo hakkında daha fazla bilgi edinmek ve nasıl kurulacağını öğrenmek için sizi bu özel öğreticiyi takip etmeye davet ediyorum:



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Kendi Dojo'nuzu çalıştırmaya gerçekten gücünüz yetmiyorsa, [dojobay.pw] (https://www.dojobay.pw/mainnet/) adresinde örneklerini ücretsiz olarak paylaşmak isteyen kişiler bulabilirsiniz. Bu geçici bir çözüm olabilir, ancak uzun vadede, egemenliğinizi ve gizliliğinizi garanti altına almak için kendi Dojo'nuzu kullanmanızı tavsiye ederim.



## 2. Ashigaru uygulamasını kontrol edin ve yükleyin



### 2.1. Ashigaru uygulamasını indirin



Telefonunuzda Tor Browser'ı açın ve [resmi Ashigaru web sitesine] (https://ashigaru.rs/download/), `İndir` bölümüne gidin. Ardından kurulum dosyasını indirmek için `Android için İndir` düğmesine tıklayın.



![Image](assets/fr/04.webp)



Uygulamayı cihazınıza yüklemeden önce, gerçekliğini ve bütünlüğünü kontrol edeceğiz. Bu, özellikle bir uygulamayı doğrudan bir `.apk' dosyasından yüklerken çok önemli bir adımdır.



### 2.2. Ashigaru uygulamasını kontrol edin



Resmi Ashigaru web sitesine] (https://ashigaru.rs/download/) `İndir` bölümüne geri dönün, ardından APK dosyasının `SHA-256 Hash` başlığı altında görüntülenen mesajı kopyalayın. PGP İMZALI MESAJIN BAŞI`ndan PGP İMZASININ SONU`na kadar olan tüm bloğu kopyalayın.



![Image](assets/fr/05.webp)



Hala telefonunuzdayken Tor Browser'da yeni bir sekme açın ve [Keybase doğrulama aracına] (https://keybase.io/verify) gidin. Az önce kopyaladığınız mesajı verilen alana yapıştırın ve ardından `Doğrula` düğmesine tıklayın.



![Image](assets/fr/06.webp)



İmza orijinalse, Keybase dosyanın Ashigaru geliştiricileri tarafından imzalandığını onaylayan bir mesaj görüntüleyecektir. Ayrıca Keybase tarafından gösterilen `ashigarudev` profiline tıklayabilir ve anahtar parmak izinin tam olarak şuna karşılık geldiğini kontrol edebilirsiniz: a138 06B1 FA2A 676B`.



Ancak, bu aşamada bir hata görünürse, imzanın geçersiz olduğu anlamına gelir. Bu durumda, ** APK'yı yüklemeyin**. Baştan başlayın veya devam etmeden önce topluluktan yardım isteyin.



![Image](assets/fr/07.webp)



Keybase size uygulamanın hash'ini sağladı. Şimdi indirdiğiniz `.apk` dosyasının hash'inin Keybase'de doğrulanmış olanla eşleşip eşleşmediğini kontrol edeceğiz. Bunu yapmak için [HASH FILE ONLINE] (https://hash-file.online/) adresine gidin.



![Image](assets/fr/08.webp)



GÖZAT...` düğmesine tıklayın ve adım 2.1`de indirilen `.apk` dosyasını seçin.


Ardından `SHA-256` hash fonksiyonunu seçin ve dosyanızın hashini hesaplamak için `CALCULATE HASH` seçeneğine tıklayın.



![Image](assets/fr/09.webp)



Site, `.apk` dosyanızın hash'ini görüntüleyecektir. Keybase.io üzerinde doğruladığınız hash ile karşılaştırın. İki hash de aynıysa, özgünlük ve bütünlük kontrolü başarılı olmuştur. Artık uygulamayı yüklemeye devam edebilirsiniz.



![Image](assets/fr/10.webp)



### 2.3. Ashigaru uygulamasını yükleyin



Uygulamayı yüklemek için telefonunuzun dosya yöneticisini açın ve indirilenler klasörüne gidin. Ardından az önce kontrol ettiğiniz `.apk' dosyasına tıklayın ve istendiğinde kurulumu onaylayın.



![Image](assets/fr/11.webp)



Ashigaru şimdi telefonunuza yüklendi.



## 3. Uygulamayı başlatın ve bir Bitcoin portföyü oluşturun



Uygulamayı ilk kez başlatırken `MAINNET` seçeneğini seçin.



![Image](assets/fr/12.webp)



Ardından `Get Started` seçeneğine tıklayın.



![Image](assets/fr/13.webp)



Şimdi yeni bir Bitcoin portföyü oluşturacağız. Yeni bir wallet oluştur` düğmesine basın.



![Image](assets/fr/14.webp)



### 3.1. bir Bitcoin portföyü oluşturun



Ashigaru bir passphrase BIP39 gerektirir. passphrase'inizi seçin ve uygun alanlara girin. Kaba kuvvet saldırısına direnmek için mümkün olduğunca uzun ve rastgele olmalıdır.



Bu passphrase'un hemen fiziksel bir yedeğini alın. Bu çok önemli bir adımdır: telefonunuzu kaybederseniz, ** artık bu passphrase'a sahip değilseniz, Ashigaru wallet'nizle depolanan bitcoinlerinize ** artık erişemezsiniz. Aynı passphrase, wallet kurtarma dosyasını şifrelemek için de kullanılır.



passphrase'in ne olduğunu bilmiyorsanız veya nasıl çalıştığını tam olarak anlamadıysanız, bu ek öğreticiyi okumanızı şiddetle tavsiye ederim. Bu önemlidir, çünkü passphrase güvenliğinizin kritik bir unsurudur: kullanımının yanlış anlaşılması fonlarınızın kalıcı olarak kaybedilmesine neden olabilir.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase'nizi girdikten sonra `SONRAKİ'ye tıklayın.



![Image](assets/fr/15.webp)



Ardından bir PIN kodu seçin. Bu kod Ashigaru wallet'ünüzün kilidini açmak için kullanılacak ve onu yetkisiz fiziksel erişime karşı koruyacaktır. wallet anahtarlarınızın kriptografik türetilmesinde yer almaz. Bu, PIN kodunu bilmeden bile, anımsatıcı ifadenize ve passphrase'e sahip herhangi birinin bitcoinlerinize yeniden erişebileceği anlamına gelir.



Uzun, rastgele bir PIN kodu tercih edin. Aynı anda ele geçirilmelerini önlemek için yedek bir kopyayı telefonunuzdan ayrı bir yerde tutmayı unutmayın.



![Image](assets/fr/16.webp)



PIN kodu oluşturulduktan sonra Ashigaru, wallet'nızın anımsatıcı ifadesini görüntüler. Uyarı: Bu ifade, passphrase'inizle birlikte bitcoinlerinize tam erişim sağlar. Bunu elinde tutan herhangi biri, telefonunuza erişimi olmasa bile paranızı ele geçirebilir. Bu 12 kelimelik dizi, telefonunuzun kaybolması, çalınması veya kırılması durumunda wallet'nızı geri yüklemek için kullanılabilir. Bu nedenle, fiziksel bir ortamda (kağıt veya metal) azami özenle saklanması önemlidir.



Bu ifadeyi asla dijital olarak kaydetmeyin, aksi takdirde fonlarınızı hırsızlığa maruz bırakma riskiyle karşı karşıya kalırsınız. Güvenlik stratejinize bağlı olarak, birkaç fiziksel kopya oluşturabilirsiniz, ancak asla bölmeyin. Kelimeleri tam sırasına göre saklayın ve numaralandırıldıklarından emin olun.



Son olarak, anımsatıcıyı ve passphrase'yi asla aynı yerde saklamayın. Her ikisi de aynı anda ele geçirilirse, bir saldırgan wallet'inize erişim sağlayabilir.



![Image](assets/fr/17.webp)



Anımsatıcı ifadenizi nasıl güvence altına alacağınız hakkında daha fazla bilgi edinmek için lütfen bu tamamlayıcı eğitime başvurun:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru daha sonra sizden passphrase'unuzu yeniden onaylamanızı ister. Bu fırsatı fiziksel yedeklemenizin doğru olup olmadığını kontrol etmek için kullanın.



![Image](assets/fr/18.webp)



### 3.2. bir dojo bağlayın



Sırada Dojo'nuza bağlanma adımı geliyor. Giriş bölümünde açıklandığı gibi, Ashigaru'nun Bitcoin ağı ile etkileşime girebilmesi için bir Dojo'ya bağlı olması gerekir.



Dojo'nuzun "Bakım Aracı "nda oturum açın ve "ARAYANLAR" menüsünü açın.



![Image](assets/fr/19.webp)



Ashigaru'da, `Karekodu Tara` düğmesine basın, ardından DMT'niz tarafından görüntülenen bağlantı QR kodunu tarayın. Ardından onaylamak için `Devam`a tıklayın.



![Image](assets/fr/20.webp)



wallet'in kilidini açmak için PIN kodunuzu girin. Bu sizi senkronizasyon sayfasına götürecektir. wallet yeni olduğu için bu aşamada *PayNym* hataları görmeniz normaldir. Sadece `Devam`a tıklayın.



![Image](assets/fr/21.webp)



Daha sonra portföyünüzün ana sayfasına yönlendirileceksiniz.



![Image](assets/fr/22.webp)



Daha ileri gitmeden önce, wallet'de hala bitcoin yokken bir test kurtarma işlemi gerçekleştirmenizi tavsiye ederim. Bu, kağıt yedeklerinizin düzgün çalışıp çalışmadığını kontrol etmenizi sağlayacaktır. Nasıl yapılacağını öğrenmek için bu öğreticiyi izleyin:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Ashigaru uygulamasını kurma



Uygulama ayarlarına erişmek için sol üst köşedeki *PayNym* resmine tıklayın ve ardından `Ayarlar`ı seçin.



![Image](assets/fr/23.webp)



Burada Ashigaru'nun çalışmasını ihtiyaçlarınıza göre uyarlamak için çeşitli seçenekler bulacaksınız. Ancak, başlangıçtan itibaren 2 önemli parametreyi etkinleştirmenizi şiddetle tavsiye ederim.



Güvenlik > Gizli mod menüsünü açarak başlayın, ardından ihtiyacınız varsa bu özelliği etkinleştirin. Ashigaru uygulamasını, telefonunuzda yüklü sıradan bir uygulamanın adı, logosu ve arayüzünün arkasına gizler. Amaç, telefonunuzun fiziksel olarak incelenmesi durumunda herhangi birinin Ashigaru'yu tanımasını önlemektir.



![Image](assets/fr/24.webp)



Sunulan her sahte uygulama, gerçek Ashigaru arayüzünün kilidini açmak için belirli bir yönteme sahiptir. Örneğin, hesap makinesini seçerseniz, Ashigaru uygulaması ana ekranınızdan kaybolur ve yerini sahte bir hesap makinesine bırakır. Bunu açtığınızda, klasik çalışan bir hesap makinesi arayüzü görürsünüz, ancak Ashigaru'ya erişmek için tek yapmanız gereken `=' sembolüne beş kez hızlıca dokunmaktır.



Etkinleştirilmesi gereken ikinci önemli parametre [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Bu seçenek, maliyeti çok düşük olduğu için mempool'larda sıkışan bir işlemin maliyetini artırmanıza olanak tanır. Bunu `İşlemler > RBF kullanarak harca` menüsü üzerinden etkinleştirebilirsiniz.



![Image](assets/fr/25.webp)



İpucu: Ana sayfada görüntülenen toplam bakiyeye tıklayarak portföyünüzün görüntüleme birimini `BTC`den `sat`a değiştirebilirsiniz.



## 5. Ashigaru'da bitcoin alın



Artık portföyünüz çalışır durumda olduğuna göre, satss alabilirsiniz. Bunu yapmak için, arayüzün sağ alt kısmındaki `+` düğmesine ve ardından yeşil `Al` düğmesine basın.



![Image](assets/fr/26.webp)



Ashigaru daha sonra adresin yeniden kullanılmasını önlemek için wallet'ünüzdeki kullanılmayan ilk alıcı adresi gösterir (adresin yeniden kullanılması gizliliğiniz için çok kötü bir uygulamadır). Daha sonra bu adresi size bitcoin göndermesi gereken kişiye veya hizmete iletebilirsiniz.



![Image](assets/fr/27.webp)



İşlem ağda yayınlandıktan sonra, otomatik olarak uygulamanın ana sayfasında görünecektir.



![Image](assets/fr/28.webp)



## 6. Ashigaru ile bitcoin gönderin



Artık Ashigaru wallet'inizde bitcoinler olduğuna göre, onları da gönderebilirsiniz. Bunu yapmak için, sağ alttaki `+` düğmesine basın, ardından kırmızı `Gönder` düğmesini seçin.



![Image](assets/fr/29.webp)



Ardından harcamayı yapmak istediğiniz hesabı seçin. Şimdilik, daha sonraki bir derste inceleyeceğimiz coin birleşmeleri için ayrılmış olan `Postmix` hesabını henüz ele almadık. Bu yüzden ana mevduat hesabından para göndereceğiz.



![Image](assets/fr/30.webp)



İşlem ayrıntılarınızı girin: gönderilecek tutar ve alıcının Bitcoin adresi.



![Image](assets/fr/31.webp)



Sağ üst köşedeki üç küçük noktaya ve ardından `Harcanmamış çıktıları göster` seçeneğine tıklayarak, gizliliğinizi artırmak için tam olarak hangi UTXO'ları harcamak istediğinizi de seçebilirsiniz.



![Image](assets/fr/32.webp)



Tüm ayrıntıları doldurduktan sonra, devam etmek için arayüzün altındaki beyaz oka tıklayın.



Daha sonra işleminizin tüm ayrıntılarını gösteren bir özet sayfasına yönlendirileceksiniz. Birkaç önemli unsur görüntülenir:




- Hedef` bloğunda, alıcı adresinin ve gönderilen miktarın doğru olup olmadığını son bir kez kontrol edin;
- Ücretler` bloğunda, Ashigaru tarafından otomatik olarak seçilen ücret oranını görüntüleyebilir ve gerekirse `YÖNET` seçeneğine tıklayarak değiştirebilirsiniz;
- Transaction` bloğu gerçekleştirmek üzere olduğunuz işlem türünü belirtir. Burada basit bir işlemden bahsediyoruz, ancak Ashigaru, gelecekteki bir eğitimde ayrıntılı olarak ele alacağımız gizlilik için optimize edilmiş diğer işlem türlerini de desteklemektedir;
- Kırmızı `İşlem Uyarısı` bloğu, işleminiz zincir analiz araçları tarafından tanınabilecek ve gizliliğinizi tehlikeye atabilecek kalıplar gösteriyorsa sizi uyarır. Üzerine tıklayarak ayrıntıları görüntüleyebilirsiniz. Örneğin, benim durumumda, Ashigaru bana gönderilen miktarın yuvarlak olduğunu (`3000 sats`) söyleyerek, hangi çıktının gidere karşılık geldiğini ve hangisinin takas olduğunu anlamamı sağladı. Bu zincir analizi sezgiselleri hakkında daha fazla bilgi edinmek için sizi Plan ₿ Academy'deki BTC 204 eğitimimi takip etmeye davet ediyorum;
- Son olarak, amacının kaydını tutmak için işleminize bir etiket ekleyebilirsiniz.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Tüm bilgileri kontrol ettikten sonra, bitcoinleri göndermek için yeşil oku kullanın. Oku basılı tutun, ardından yüklemeyi onaylamak için sağa sürükleyin.



![Image](assets/fr/33.webp)



İşleminiz Bitcoin ağında yayınlanmıştır.



![Image](assets/fr/34.webp)



## 7. Ashigaru wallet'unuzun kurtarılması



Ashigaru wallet'nin kurtarılması, uygulama Samurai Wallet ile aynı yöntemleri kullandığından, klasik bir Bitcoin wallet'den biraz farklıdır. wallet'nize erişiminizi kaybederseniz (PIN kodunuzu unuttuğunuz, uygulamayı kaldırdığınız veya telefonunuzu kaybettiğiniz için), bitcoinlerinizi kurtarmanın birkaç yolu vardır.



Telefonunuza hala erişiminiz varsa veya bu dosyanın yedeğini aldıysanız, en basit yöntem `ashigaru.txt` yedek dosyasını kullanmaktır. Bu dosya, portföyünüzü yeni bir Ashigaru örneğinde (veya Sparrow Wallet'te) geri yüklemek için ihtiyacınız olan tüm bilgileri içerir, ancak bu eğitimin 3.1 adımında tanımladığınız passphrase ile şifrelenmiştir. Bu nedenle, bu yöntemi kullanmak için hem `ashigaru.txt` dosyasına hem de passphrase'e sahip olmanız gerekir.



Bu iki unsurla, örneğin portföyünüzü Sparrow Wallet üzerinde geri yükleyebilirsiniz.



![Image](assets/fr/35.webp)



Eğer `ashigaru.txt` dosyasına erişiminiz yoksa, diğer Bitcoin portföyleri için yaptığınız gibi passphrase anımsatıcı ifadenizi kullanarak fonlarınıza yeniden erişim sağlayabilirsiniz. Eğer Whirlpool kullanıyorsanız, bypass yollarını kolayca kurtarmak için bu geri yüklemeyi ya yeni bir Ashigaru örneğinde ya da doğrudan Sparrow Wallet üzerinde gerçekleştirmenizi tavsiye ederim. Alternatif olarak, türetme yollarını manuel olarak girerek bu bilgileri BIP39 uyumlu başka bir yazılıma aktarabilirsiniz.



Bu işlem hakkında daha fazla bilgi için lütfen bir Wallet Samurai wallet'ün kurtarılması hakkında yazdığım eğitimin tamamına bakın. Ashigaru bir fork olduğundan, prosedür aynıdır:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Gördüğünüz gibi, hangi restorasyon yöntemini kullanırsanız kullanın, passphrase vazgeçilmezdir. Bu yüzden dikkatlice yedeklediğinizden emin olun. Güvenlik stratejinize bağlı olarak birkaç kopya da oluşturabilirsiniz.



## 8. Uygulama güncelleme



Ashigaru uygulamasını güncellemek için, normal bir uygulama gibi Play Store üzerinden değil, bir `.apk' dosyasından yüklediğiniz için, güncellenmiş sürüme karşılık gelen yeni `.apk' dosyasını indirmeniz ve ardından manuel olarak yüklemeniz gerekir.



Bu eğitimin 2. bölümünde açıklanan adımları tekrarlayın, ancak yüklemeyi başlatmak için `.apk` dosyasına tıkladığınızda **Android telefonunuz size `Yükle` değil `Güncelle` seçeneğini sunmalıdır**.



![Image](assets/fr/41.webp)



Bu çok önemli bir noktadır: Android `Güncelle` yerine `Yükle` görüntülüyorsa, muhtemelen hileli bir sürüm yüklüyorsunuz demektir. Bu durumda, yükleme işlemini derhal durdurun.



İlk kurulumda olduğu gibi, güncellemeye devam etmeden önce lütfen `.apk` dosyasının gerçekliğini ve bütünlüğünü kontrol edin.



Yeni bir sürümün ne zaman mevcut olduğunu öğrenmek için, zaman zaman resmi Ashigaru web sitesini kontrol edin. İçiniz rahat olsun, Ashigaru Samourai Wallet'den miras kalan istikrarlı, olgun bir uygulamadır ve güncellemeler daha genç yazılımlara kıyasla nispeten seyrektir.



## 9. Ashigaru projesine bağışta bulunun



Ashigaru açık kaynaklı bir projedir. Gelişimini desteklemek isterseniz, PayNym aracılığıyla doğrudan uygulamadan bağış yapabilirsiniz.



Bunu yapmak için, arayüzün sağ üst kısmındaki PayNym'inize tıklayın, ardından `PM...` ile başlayan ödeme kodunuzu seçin.



![Image](assets/fr/36.webp)



Ardından ekranın sağ alt köşesindeki `+` düğmesine basın.



![Image](assets/fr/37.webp)



Alıcı olarak `Ashigaru Açık Kaynak Projesi`ni seçin.



![Image](assets/fr/38.webp)



BIP47 iletişim kanalını kurmak için `CONNECT` düğmesine tıklayın (bu protokol hakkında daha fazla bilgi için aşağıdaki eğitime bakın).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Bildirim işlemi onaylandıktan sonra, arayüzün sağ üst köşesindeki küçük beyaz oka tıklayarak bağışlarınızı projeye gönderebilirsiniz.



![Image](assets/fr/40.webp)



Artık Ashigaru uygulamasının temel özelliklerini nasıl kullanacağınızı biliyorsunuz. Gelecek eğitimlerde, Samuray Wallet'dan miras alınan coinjoin uygulaması Whirlpool'in yanı sıra gelişmiş harcama işlemlerinden nasıl yararlanacağınıza bakacağız.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
