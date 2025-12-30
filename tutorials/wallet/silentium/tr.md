---
name: Silentium
description: Sessiz Ödemeler destekli aşamalı web wallet (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin adreslerinin yeniden kullanımı, kullanıcı gizliliğine yönelik en doğrudan tehditlerden biridir. Bir alıcı birden fazla ödeme almak için tek bir adresi paylaştığında, herhangi bir gözlemci tüm ilişkili işlemleri izleyebilir ve finansal geçmişlerini yeniden yapılandırabilir. Bu sorun özellikle, gizliliklerinden ödün vermeden bir bağış adresini herkese açık olarak görüntülemek isteyen içerik oluşturucuları, hayır kurumlarını veya aktivistleri etkiler.



Silentium bu soruna doğrudan tarayıcınızdan erişebileceğiniz zarif bir çözümle yanıt veriyor. Louis Singer tarafından Mayıs 2024'te başlatılan bu açık kaynaklı aşamalı web uygulaması (PWA), Silent Payments'ı (BIP-352) uygulamaktadır: işlemler arasında önceden etkileşim veya gözlemlenebilir bağlantı olmaksızın her ödemenin ayrı bir blok zinciri adresinde sonlandığı yeniden kullanılabilir bir statik adres.



**Önemli uyarı**: Silentium, Silent Payments'ın hafif cüzdanları için *kavram kanıtı* olarak hizmet veren deneysel bir projedir. Günlük wallet olarak veya önemli miktarları depolamak için kullanılmamalıdır. Geliştiriciler açıkça belirtmektedir:



> Kullanım riski size aittir.

Bu wallet'in bir test ağı veya regtest olarak kullanılabileceğini unutmayın.



## Silentium nedir?



### Felsefe ve hedefler



Silentium, hafif bir wallet tarayıcısında Sessiz Ödemeleri uygulamak için teknik bir gösteri görevi görür. Geleneksel Bitcoin adreslerini de desteklemesine rağmen, kullanıcıların bu gizlilik teknolojisini basit bir şekilde denemelerini sağlamak için Sessiz Ödemeler üzerinde durulmaktadır.



### Sessiz Ödemeler nasıl çalışır?



Sessiz Ödemeler (BIP-352) Eliptik Eğri Diffie-Hellman Anahtarı Exchange (ECDH) kullanır. Alıcı, iki açık anahtardan oluşan statik bir adres (mainnet'da `sp1...`, testnet'te `tsp1...`) oluşturur: ödemeleri tespit etmek için bir tarama anahtarı ve bunları kullanmak için bir harcama anahtarı.



Gönderici, kriptografik bir "ince ayar" oluşturan paylaşılan bir sırrı hesaplamak için kendi özel giriş anahtarlarını alıcının tarama anahtarıyla birleştirir. Harcama anahtarına eklenen bu ince ayar, her işlem için benzersiz bir Taproot adresi oluşturur. Alıcı, önceden herhangi bir etkileşim olmaksızın fonları tespit etmek ve harcamak için özel tarama anahtarıyla bu hesaplamayı yeniden üretir.



Avantajları: gönderici ve alıcı için gelişmiş gizlilik, üçüncü taraf sunucu gerektirmez, işlemler geleneksel Taproot ödemelerinden ayırt edilemez. Ana dezavantaj: ödemeleri tespit etmek için blok zincirinin yoğun bir şekilde taranması.



Sessiz Ödemelerin teorik işleyişi hakkında daha fazla bilgi edinmek için BTC,204 kursunun Plan ₿ Academy ile ilgili son bölümüne bakınız:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Desteklenen platformlar



Silentium, herhangi bir modern tarayıcıdan (mobil veya masaüstü) erişilebilen bir Aşamalı Web Uygulamasıdır (PWA). Doğrudan `app.silentium.dev` adresinde kullanın, tarayıcınız üzerinden yerel bir uygulama olarak yükleyin veya yerel olarak dağıtın. Kurulum, resmi mağazalardan geçmeden doğrudan tarayıcıdan yapılır.



## Web Uygulamasını Kullanma



### Erişim ve kurulum



[Tarayıcınızdan `https://app.silentium.dev/` adresine gidin] (https://app.silentium.dev/). Uygulama anında yüklenir ve ana ekranı görüntüler.



IOS'ta yerel bir uygulama olarak yüklemek için paylaş düğmesine (yukarı oklu kare) basın ve ardından "Ana ekranda" seçeneğini seçin. Android'de, tarayıcı genellikle doğrudan bir "Ana ekrana ekle" bildirimi sunar. Silentium yüklendikten sonra özel simgesiyle görünür ve yerel bir uygulama olarak çalışır, ancak işlemleri senkronize etmek için internet bağlantısı gerektirir.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Portföy oluşturma



İlk açılışta, yeni bir portföy generate oluşturmak için "Wallet Oluştur" veya mevcut bir kurtarma ifadesinden geri yüklemek için "Wallet Geri Yükle" seçeneğini seçin.



"Wallet Oluştur" seçeneğini seçin. Uygulama, dikkatlice yazmanız gereken 12 kelimelik bir cümle oluşturur. Bu ifade fonlarınızı kurtarmanın tek yoludur. Test ağında bile iyi yedekleme uygulamaları benimseyin. İfadenizi kaydettikten sonra "Devam" düğmesine basın.



Uygulama daha sonra wallet'ye erişimi güvence altına almak için bir parola belirlemenizi ister. Güçlü bir parola seçin ve onaylayın.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



İfade onaylandıktan ve şifre belirlendikten sonra ana arayüze yönlendirileceksiniz.



### Interface ana ve parametreleri



Ana arayüz, bakiyenizi satoshi cinsinden (başlangıçta 0 sats) gösterir ve altta üç düğme bulunur:




- Sync**: wallet'yi blockchain ile senkronize eder
- Receive**: fon almak için
- Gönder**: bitcoin göndermek için



Sağ üstteki simge (üç yatay çubuk) aracılığıyla Ayarlar'a erişin. Ayarlar menüsü çeşitli seçenekler sunar:





- Hakkında**: başvuru bilgileri
- Backup**: kurtarma ifadesinin yedeği
- Explorer**: blockchain explorer (varsayılan olarak Mempool) ve Silentiumd sunucusunu seçin
- Ağ**: ağ seçimi (mainnet/testnet)
- Şifre**: şifreyi değiştir
- Yeniden Doldur**: wallet'ü yeniden doldurma
- Sıfırla**: tamamen sıfırla
- Tema**: temayı değiştir



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Explorer** bölümü özellikle önemlidir: kullanılan blok zinciri gezginini seçmenizi sağlar (varsayılan olarak Mempool) ve ayrıca Silentiumd sunucusunun URL'sini görüntüler (mainnet için `https://bitcoin.silentium.dev/v1`). Kendi Silentiumd sunucunuzu barındırıyorsanız veya testnet kullanmak istiyorsanız, bu parametreleri yapılandırdığınız yer burasıdır.



### Fonların alınması



Ana arayüzden "Al" düğmesine basın. Varsayılan olarak, Silentium QR koduyla birlikte bir Sessiz Ödeme adresi görüntüler. Adres mainnet üzerinde `sp1...` veya testnet üzerinde `tsp1...` ile başlar.



Ekranın altındaki "Klasik adrese geç" / "Sessiz adrese geç" düğmesini kullanarak Sessiz Ödeme ve klasik Bitcoin adresleri arasında geçiş yapabilirsiniz.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




İşlem yayınlandıktan sonra lütfen birkaç dakika bekleyin. Sessiz Ödemeler için Silentium, size yönelik işlemler için blok zincirini otomatik olarak tarar. İşlemler, aşamalı olarak onaylanmadan önce "Onaylanmadı" durumuyla görünür.



### Ödeme gönderin



Ana arayüzden "Gönder" düğmesine basın. Gönderme ekranı size soracaktır:



1. **Address**: bir Sessiz Ödeme adresi (`sp1...` veya `tsp1...`) veya klasik bir Bitcoin adresi yapıştırın. Bir adresi taramak için QR tarama simgesini kullanabilirsiniz.


2. **Tutar**: gönderilecek tutarı satoshi cinsinden girin. Kolay giriş için sayısal bir tuş takımı görüntülenir. Mevcut bakiyeniz referans için en üstte görüntülenir.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Adresi ve tutarı girdikten sonra devam etmek için "Proceed" tuşuna basın. Uygulama, işlemi onaylamadan önce sizden istediğiniz ücret seviyesini seçmenizi isteyecektir.



## wallet kendi kendine barındırma



### Neden kendi kendine barındırma?



Silentium'un yerel barındırması tam egemenlik, kod doğrulama, geliştirme ortamı ve resmi site arızaları karşısında esneklik sunar.



### Ön Koşullar



Node.js (sürüm 14+), npm veya yarn, Git ve yaklaşık 500 MB disk alanı.



### Yerel kurulum



Depoyu klonlayın ve :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Başlatın ve kullanın



Uygulamayı geliştirme modunda başlatın:



```bash
yarn start
```



Tarayıcınızda `http://localhost:3000` adresine gidin. Optimize edilmiş bir üretim sürümü için :



```bash
yarn build
```



Build/` içinde oluşturulan dosyalar nginx, Apache veya herhangi bir web sunucusu ile sunulabilir. Silentium varsayılan olarak herkese açık `bitcoin.silentium.dev` sunucusuna bağlanır. Testnet veya kendi sunucunuzu kullanmak için parametrelerdeki bu ayarı değiştirin.



## Silentiumd sunucusu



### Rolü ve işleyişi



Silentium, ödeme tespitini optimize etmek için bir **Silentiumd** indeksleme sunucusu kullanır. Tüm Taproot işlemlerini taramak bir tarayıcı veya cep telefonu için çok zahmetli olacaktır.



Silentiumd her Taproot işlemi için ara verileri (ince ayarlar) önceden hesaplar. wallet'ünüz bu ince ayarları indirir (işlem başına birkaç bayt) ve son hesaplamayı yerel olarak gerçekleştirerek ödemenin sahipliğini doğrular. Sunucu, geleneksel Electrum sunucularının aksine, anahtarlarınızı asla bilmez veya işlemlerinizi tanımlayamaz.



Kompakt BIP158 filtreleri, wallet'inizin adreslerinizi ifşa etmeden hangi blokları tarayacağını belirlemesini sağlar, böylece gizliliğinizi korur.



### Genel sunucu



Vulpem Ventures tarafından desteklenen genel sunucu `bitcoin.silentium.dev` (mainnet) basit ve anında bir deneyim sunmaktadır. Her ne kadar gizlilik korunsa da, bu yaklaşım üçüncü taraf altyapısına göreceli bir güven anlamına gelmektedir.



### Kendi Silentiumd sunucunuzu barındırın



Tam egemenlik için kendi Silentiumd sunucunuzu barındırın. Önkoşullar: Txindex=1` ve `blockfilterindex=1` ile Bitcoin Core etiketsiz düğüm, Go 1.21+, 10-20 GB disk alanı, sistem yönetimi becerileri.



**Kurulum:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Ortam değişkenleri aracılığıyla yapılandırın (ayrıntılar için deponun `config.md` dosyasına bakın). Sunucu blok zincirini indeksler ve API'unuz tarafından sorgulanabilecek bir wallet ortaya çıkarır.



Şu anda Umbrel veya Start9 için paketlenmiş bir çözüm mevcut değildir ve bu da teknik olmayan kullanıcıların erişimini sınırlamaktadır.



## Avantajlar ve sınırlamalar



### Önemli Noktalar





- Maksimum erişilebilirlik**: herhangi bir tarayıcıdan kullanın, ağır kurulum gerektirmez
- Çoklu platform**: PWA teknolojisi sayesinde mobil (Android/iOS) ve masaüstünde çalışır
- Basit kendi kendine barındırma**: birkaç komutla yerel kurulum mümkün
- Açık kaynak**: GitHub'da tamamen denetlenebilir kod
- Gizlilik odaklı**: izleme yok, analiz yok, yerel kriptografik hesaplamalar
- Ayrı mimari**: wallet (istemci) ve indeksleme sunucusu arasında net ayrım
- Hesap olmadan**: kayıt veya kişisel veri gerekmez



### Dikkate alınması gereken kısıtlamalar





- Deneysel proje**: sadece kavram kanıtı, günlük kullanım veya üretim için tasarlanmamıştır
- Garanti yok**: hata riski, güvenlik açıkları, olası fon kaybı
- Sınırlı destek**: az kullanıcı dokümantasyonu, küçük topluluk, resmi destek yok
- Sunucu bağımlılığı**: çalışan bir Silentiumd sunucusu gerektirir (genel veya kendi kendine barındırılan)
- Yoğun tarama**: Sessiz Ödemeler tespiti bant genişliği tüketir
- Azaltılmış işlevsellik**: bozuk para kontrolü yok, Lightning yok, çoklu imza yok



## En iyi uygulamalar



### seed güvenlik



Testnet'te bile kurtarma ifadenizi ciddiye alın. Yazın ve güvenli bir yerde saklayın. Testnet ve mainnet için ayrı cüzdanlar tutun: gerçek fonlar için tasarlanmış bir wallet'te asla bir test seed kullanmayın.



### Kaynak kodu doğrulama



Kendi kendine barındırmanın avantajlarından biri, çalıştırmadan önce kaynak kodunu kontrol etme yeteneğidir. Silentium'u gerçek fonlarla kullanmayı planlıyorsanız, kodu denetlemek için zaman ayırın veya bunu yapması için güvenilir bir geliştirici bulun. Ayrıca, orijinalliği sağlamak için `app.silentium.dev` üzerinde dağıtılan kodun hash'ini GitHub deposununki ile karşılaştırın.



### Yedekleme ve geri yükleme



Sessiz Ödemeler fon kurtarma işlemi için BIP-352 protokolü ile uyumlu bir wallet gerekir. Standart bir wallet, UTXO Sessiz Ödemelerinizi almak için blok zincirini tarayamaz. Silentium'u kurulu tutun veya gerekirse fonlarınızı geri yüklemek için başka bir uyumlu wallet'e (Cake Wallet veya gelecekteki diğer uygulamalar gibi) erişiminiz olduğundan emin olun.



## Sonuç



Silentium, Silent Payments'ı teknik sürtüşme olmadan anlamak için erişilebilir bir test alanı sağlar. Bir kavram kanıtı olarak, bu gizlilik teknolojisinin kendi kendini saklarken bir wallet tarayıcısına nasıl entegre edilebileceğini göstermektedir. on-chain gizliliği için bu umut verici atılımı keşfetmek için testnet üzerinde deney yapın.



## Kaynaklar



### Resmi belgeler




- Silentium GitHub deposu (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub deposu (sunucu): https://github.com/louisinger/silentiumd
- Web uygulaması: https://app.silentium.dev/
- Silent Payments topluluk sitesi: https://silentpayments.xyz
- Spesifikasyon BIP-352: https://bips.dev/352



### Makaleler ve kaynaklar




- Resmi duyuru (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Sessiz Ödemeler: https://bitcoinops.org/en/topics/silent-payments/



### Testnet araçları




- Testnet musluk: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet