---
name: Blockstream Uygulaması - Yalnızca İzle
description: Blockstream Uygulamasında bir Watch-only wallet'ı nasıl yapılandırabilirim?
---

![cover](assets/cover.webp)


## 1. Giriş


### 1.1 Eğitimin amacı





- Bu eğitim, özel anahtarlarına erişmeden bir Bitcoin Wallet'yi izlemek için **Blockstream App** mobil uygulamasının **Watch-Only** özelliğinin nasıl kurulacağını ve kullanılacağını açıklar.
- Kurulum, ilk yapılandırma, genişletilmiş bir genel anahtarın içe aktarılması ve bakiyeleri ve generate alıcı adreslerini izlemek için kullanılması konularını kapsar.
- Not: Ekte verilen diğer eğitimler Onchain, Liquid ve masaüstü sürümünü kapsamaktadır.



### 1.2. Hedef kitle





- Yeni başlayanlar**: Bir Bitcoin portföyünü (genellikle bir Hardware Wallet ile ilişkili) sezgisel bir mobil uygulama aracılığıyla izlemek isteyen kullanıcılar.
- Orta düzey kullanıcılar**: Tor veya SPV gibi gizlilik seçeneklerini kullanırken salt okunur portföyleri yönetmek isteyen kişiler.
- Hardware Wallet sahipleri**: Cihazlarını bağlamadan bakiyelerini ve generate adreslerini kontrol etmek için.
- İşyerleri ve mağazalar** :
 - Özel anahtarlarınızı ifşa etmeden muhasebe amaçlı işlemlerinizi takip edin.
 - Çevrimiçi ödeme sistemlerinde özel anahtarlarını girmeden alınan işlemleri doğrulayın.
 - Çalışanların özel anahtarlara erişimi olmadan generate yeni resepsiyon adreslerini kullanabilmelerini sağlayın.
- Kuruluşlar ve kitlesel fonlama**: Fonlara erişime izin vermeden bağışçılara bakiyeyi şeffaf bir şekilde gösterin.



### 1.3. Yalnızca İzle ile tanışın



Bir **Sadece İzle** Wallet, özel anahtarlara erişiminiz olmadan bir Bitcoin Wallet'nin işlemlerini ve bakiyesini izlemenizi sağlar. Geleneksel bir Wallet'den farklı olarak, yalnızca **genişletilmiş **genel anahtar** ("**xpub**", ardından "zpub", "ypub" vb.) gibi genel verileri depolar, bu da alıcı adreslerini almasını ve Blockchain Bitcoin'deki işlem geçmişini izlemesini sağlar. Özel anahtarların bulunmaması, uygulamadan fon aktarımını imkansız hale getirerek gelişmiş güvenliği garanti eder.



![image](assets/fr/10.webp)



**Neden Watch-only wallet kullanıyorsunuz?





- Güvenlik**: Bağlı bir cihazdaki özel anahtarları açığa çıkarmadan bir **Hardware Wallet** tarafından güvence altına alınan bir portföyü izlemek için idealdir.
- Kolaylık**: Hardware Wallet'i bağlamadan bakiyeyi ve generate yeni alıcı adreslerini kontrol etmenizi sağlar.
- Gizlilik**: Üçüncü taraf sunuculara bağımlılığı sınırlamak için **Tor** veya **SPV** gibi seçeneklerle uyumludur.
- Kullanım durumları**: Hareket halindeki fonları takip etme, ödeme almak için adres oluşturma veya özel anahtarları riske atmadan işlemleri doğrulama.



![image](assets/fr/01.webp)



### 1.4. Genişletilmiş açık anahtarlar



Bir **genişletilmiş açık anahtar** (xpub, ypub, zpub, vb.), özel anahtarlara erişim vermeden tüm alt açık anahtarları ve bunlarla ilişkili alma adreslerini üreten bir Bitcoin Wallet'den türetilen bir veri parçasıdır.





- Nasıl çalışır** : Genişletilmiş açık anahtar, deterministik bir süreç (BIP-32) aracılığıyla seed ifadesinden üretilir. Her biri bir alıcı Address'ye dönüştürülebilen alt açık anahtarlardan oluşan hiyerarşik bir ağaç oluşturur. İzlenen Wallet ile aynı türetme yolunu (örneğin `m/44'/0'/0'`) kullanan Watch-only wallet, aynı adresleri üreterek fonların izlenmesini ve yeni alma adreslerinin oluşturulmasını sağlar.



![image](assets/fr/11.webp)





- Genişletilmiş açık anahtar türleri
 - xpub**: Eski portföyler ("1" ile başlayan adresler, BIP-44) ve Taproot portföyleri ("bc1p" ile başlayan adresler, BIP-86) için kullanılır.
 - ypub**: Uyumlu SegWit cüzdanları için tasarlanmıştır ("3" ile başlayan adresler, BIP-49).
 - zpub**: Yerel SegWit portföyleriyle ilişkilidir ("bc1q" ile başlayan adresler, BIP-84).
 - Diğerleri (tpub, upub, vpub, vb.)**: Alternatif ağlar (Testnet gibi) veya belirli standartlar için kullanılır. Örneğin, tpub Testnet ağı içindir.





- Ayrım** : Xpub, ypub veya zpub arasındaki seçim Address türüne (eski, SegWit, Taproot veya yuvalanmış SegWit) ve Wallet tarafından kullanılan BIP standardına bağlıdır. Blockstream App ile uyumluluğu sağlamak için kaynak portföyünüzün gerektirdiği formatı kontrol edin.





- Güvenlik ve gizlilik** : Genişletilmiş açık anahtar, fonların harcanmasına izin vermediği için güvenlik açısından hassas değildir (özel anahtarlara erişim yoktur). Ancak, tüm açık adresleri ve ilgili işlem geçmişini ortaya çıkardığı için gizlilik açısından hassastır.



**Öneri**: Genişletilmiş genel anahtarınızı hassas bilgi olarak koruyun.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet hatırlatma





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: bir akıllı telefona, bilgisayara veya internete bağlı herhangi bir cihaza yüklenen ve bir Bitcoin Wallet'in özel anahtarlarının yönetilmesini ve güvence altına alınmasını sağlayan bir uygulamanın tüm adları.
- Anahtarları çevrimdışı olarak izole eden **Cold cüzdanları** olarak da bilinen **donanım cüzdanlarının** aksine, yazılım cüzdanları bağlı bir ortamda çalışır ve bu da onları siber saldırılara karşı daha savunmasız hale getirir.





- Önerilen kullanım** :
    - Özellikle günlük işlemler için orta miktarda Bitcoin'i yönetmek için idealdir.
    - Hardware Wallet'un gereksiz görünebileceği yeni başlayanlar veya sınırlı varlığa sahip kullanıcılar için uygundur.





- Sınırlamalar**: Büyük fonları veya uzun vadeli tasarrufları saklamak için daha az güvenlidir. Bu durumda bir Hardware Wallet seçin.




## 2. Blockstream Uygulaması ile tanışın





- Blockstream App**, Bitcoin portföylerini ve Liquid Network'deki varlıkları yönetmek için bir mobil (iOS, Android) ve masaüstü uygulamasıdır. Blockstream] (https://blockstream.com/) tarafından 2016 yılında satın alınan bu uygulama daha önce *Green Address* ve ardından *Blockstream Green* olarak adlandırılmıştır.
- Temel özellikler** :
    - Blockchain Bitcoin üzerinde zincirleme** işlemler.
    - Liquid** ağındaki işlemler (hızlı, gizli alışverişler için Sidechain).
    - Anahtarlara erişim olmadan fonları izlemek için yalnızca izle** portföyleri.
    - Gizlilik seçenekleri: **Tor** üzerinden bağlantı, Electrum üzerinden bir **kişisel düğüme** bağlantı veya üçüncü taraf düğümlere bağımlılığı azaltmak için **SPV** doğrulaması.
    - Onaylanmamış işlemleri hızlandırmak için **Replace-by-fee (RBF)** fonksiyonları.
- Uyumluluk**: Blockstream Jade** gibi donanım cüzdanlarını entegre eder.
- Interface**: Yeni başlayanlar için sezgisel, uzmanlar için gelişmiş seçenekler.
- Not**: Bu kılavuz onchain kullanımına odaklanmaktadır. Ekler bölümündeki diğer eğitimler Onchain, Watch-Only ve masaüstü sürümünü kapsamaktadır.




## 3. Blockstream Uygulamasını yükleme ve yapılandırma



### 3.1. İndirin





- Android için** :
    - Google Play Store'dan [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) uygulamasını indirin.
    - Alternatif: Blockstream'in resmi GitHub](https://github.com/Blockstream/green_android) adresinde bulunan APK dosyası aracılığıyla yükleyin.
- IOS için** :
    - App Store'dan [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) uygulamasını indirin.
- Not**: Sahte uygulamalardan kaçınmak için resmi kaynaklardan indirdiğinizden emin olun.



### 3.2. ilk yapılandırma





- Ana ekran**: İlk açıldığında, uygulama yapılandırılmış bir Wallet olmayan bir ekran görüntüler. Oluşturulan veya içe aktarılan portföyler daha sonra burada görünecektir.



![image](assets/fr/02.webp)





- Ayarları özelleştirin**: "Uygulama ayarları" üzerine tıklayın, aşağıdaki seçenekleri ayarlayın, "Kaydet" üzerine tıklayın, uygulamayı yeniden başlatın ve portföyünüzü oluşturun.



![image](assets/fr/03.webp)



#### 3.2.1. Geliştirilmiş gizlilik (yalnızca Android)





- İşlev**: Ekran görüntülerini devre dışı bırakır, görev yöneticisinde uygulama önizlemelerini gizler ve telefon kilitlendiğinde erişimi kilitler.
- Neden? Verilerinizi yetkisiz fiziksel erişime veya ekran yakalayan kötü amaçlı yazılımlara karşı korur.



#### 3.2.2. Tor üzerinden bağlantı





- İşlev**: Ağ trafiğini, bağlantılarınızı şifreleyen anonim bir ağ olan **Tor** üzerinden yönlendirin.
- Neden? **: IP Address'nizi gizleyin ve gizliliğinizi koruyun, ağınıza güvenmiyorsanız (örneğin halka açık Wi-Fi) idealdir.
- Dezavantaj**: Şifreleme nedeniyle uygulamayı yavaşlatabilir.
- Öneri**: Gizlilik öncelikliyse Tor'u etkinleştirin, ancak bağlantı hızını test edin.



#### 3.2.3. Kişisel bir düğüme bağlanma





- İşlev**: Uygulamayı bir **Electrum sunucusu** aracılığıyla kendi **tamamlanmış Bitcoin düğümünüze** bağlar.
- Neden? Blockstream sunucularına bağımlılığı ortadan kaldırarak Blockchain verileri üzerinde tam kontrol sağlar.
- Ön koşul**: Yapılandırılmış bir Bitcoin düğümü.
- Tavsiye**: Maksimum egemenlik isteyen ileri düzey kullanıcılar.



#### 3.2.4. SPV doğrulaması





- İşlev**: Tüm zinciri indirmeden belirli Blockchain verilerini doğrudan doğrulamak için **Basitleştirilmiş Ödeme Doğrulaması (SPV)** kullanır.
- Neden? Mobil cihazlar için hafif kalırken Blockstream'in varsayılan düğümüne bağımlılığı azaltır.
- Dezavantaj**: Bazı bilgiler için üçüncü taraf düğümlere dayandığından Full node'den daha az güvenlidir.
- Öneri**: Kişisel bir düğüm kullanamıyorsanız ancak optimum güvenlik için bir Full node tercih ediyorsanız SPV'yi etkinleştirin.





## 4. Bitcoin "Yalnızca İzle" portföyü oluşturma



### 4.1. Genişletilmiş açık anahtarı kurtarma



Bir Watch-only wallet kurmak için öncelikle izlenecek Wallet'nin genişletilmiş genel anahtarını (xpub, ypub, zpub, vb.) edinmeniz gerekir. Bu bilgi genellikle yazılımınızın veya Hardware Wallet'nın ayarlar veya "Wallet bilgileri" bölümünde mevcuttur.





- Blockstream Uygulaması ile örnek: Wallet ana ekranından "Ayarlar "a, ardından "Wallet Ayrıntıları "na gidin ve zpub :



![image](assets/fr/09.webp)





- Alternatif 1: generate bir sonraki adımda taranmak üzere genişletilmiş açık anahtarı içeren bir QR kodu.
- Alternatif 2: Wallet'iniz bunu sağlıyorsa bir output descriptor kullanın.



### 4.2. Wallet Watch-only'yi içe aktarın





- Dikkat**: Portföyünüzü kameraların veya gözlemcilerin olmadığı özel bir ortamda oluşturun.
- Ana ekrandan "Yeni bir portföy oluşturun" ve ardından "Başlayın" seçeneğine tıklayın:



![image](assets/fr/04.webp)





- Sonraki ekran görüntülenir:



![image](assets/fr/06.webp)






- (1) **"Mobil Wallet Kurulumu "** : Yeni bir Hot Wallet oluşturun. Ekteki "Blockstream Uygulaması - Onchain" eğitimine bakın.
- (2) **"Yedekten Geri Yükleme "**: Mnemonic cümlesi (12 veya 24 kelime) kullanarak mevcut bir portföyü içe aktarın. Dikkat: İfadeyi bir Cold Wallet'dan içe aktarmayın, çünkü bağlı bir cihazda açığa çıkacak ve güvenliğini geçersiz kılacaktır.
- (3) **"Yalnızca İzle "**: bu eğitim için ilgilendiğimiz seçenek.





- Ardından "**Tek imza**" ve "**Bitcoin**" ağını seçin:



![image](assets/fr/12.webp)





- Genişletilmiş açık anahtarı (xpub, ypub, zpub, vb.) yapıştırın, ilgili QR kodunu tarayın veya bir output descriptor girin. Uygulama "xpub" belirtse bile, ypub, zpub vb. anahtarlar da yetkilendirilir. Ardından "Bağlan "a tıklayın:



![image](assets/fr/13.webp)




### 4.3. Yalnızca Wallet Saatini Kullanma



İçe aktarıldıktan sonra Watch-only wallet, genişletilmiş genel anahtardan türetilen adreslerin toplam bakiyesini ve işlem geçmişini görüntüler. Yalnızca zincir içi işlemler görülebilir (Liquid işlemleri yok sayılır). Bir Liquid Wallet'ü izlemek için, önceki adımda "Liquid "yi seçerek içe aktarma işlemini tekrarlayın.





- Bakiyeyi ve geçmişi görüntüle**: ana ekrandan toplam bakiyeyi ve zincir içi işlem geçmişini görüntüleyin:



![image](assets/fr/14.webp)





- generate bir alıcı Address**: Yeni bir onchain Address oluşturmak için "İşlem Yap" ve ardından "Al" seçeneğine tıklayın. Para almak için QR kodu veya kopyalama yoluyla paylaşın:



![image](assets/fr/15.webp)





- Para gönder**: Önce **"İşlem Yap "**, ardından **"Gönder "** seçeneğine tıklayın. Girebilirsiniz :
 - Alıcının Address'sı.
 - İşlemin tutarı.
 - İşlem ücretleri.



Ancak, Watch-only wallet özel anahtarları tutmadığından, doğrudan para gönderemezsiniz. İşlemi imzalamak için, QR kodlarını tarayarak Hardware Wallet veya Exchange PSBT'lerinizi bağlayın (örneğin Coldcard Q'da bulunan bir seçenek).



![image](assets/fr/16.webp)





- Not**: Hataları önlemek için her zaman alıcı Address'ı ve işlem ayrıntılarını kontrol edin. Yanlış Address'a gönderilen fonlar geri alınamaz.




## Ekler



### A1. Diğer Blockstream Uygulama eğitimleri





- Onchain ağını kullanma :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Liquid Network'in Kullanılması :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Masaüstü versiyonu :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Genişletilmiş açık anahtarlar





- Sözlük :
 - [Genişletilmiş genel anahtarlar](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurs :
 - [Les clés publiques étendues](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/les-cles-etendues-8dcffce1-31bd-5e0b-965b-735f5f9e4602)




### A3. En iyi uygulamalar



Blockstream Uygulamasını** güvenli ve verimli bir şekilde kullanmak için bu önerileri izleyin. Bunlar, **Bitcoin (onchain)**, **Liquid** ve **Lightning** ağlarında paranızı korumanıza, işlemlerinizi optimize etmenize ve gizliliğinizi korumanıza yardımcı olacaktır.





- Kurtarma cümlenizi güvence altına alın** :
 - Eğitim: Mnemonic ifadenizi kaydetme



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Güvenli kimlik doğrulama kullanın** :
 - Uygulamaya erişimi korumak için bir **güçlü PIN** veya **biyometrik kimlik doğrulama** (parmak izi veya yüz tanıma) etkinleştirin.
 - PIN kodunuzu veya biyometrik verilerinizi asla paylaşmayın.





- Gizliliğinizi koruyun** :
 - generate Blockchain üzerindeki izlemeyi sınırlandırmak için her zincir üstü veya Liquid alımı için yeni bir Address.
 - "Geliştirilmiş Gizlilik", "Tor" ve "SPV" işlevlerini etkinleştirin.
 - Maksimum gizlilik için, Wallet'ünüzü genel düğümü kullanmak yerine bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayın





- İhtiyaçlarınıza en uygun ağı seçin** :
 - Onchain**: Uzun vadeli saklama veya büyük değerli işlemler için tercih edilir (ücretler tutara göre ihmal edilebilir).
 - Liquid**: Gelişmiş gizlilik ile hızlı, düşük maliyetli transferler için kullanın.
 - Lightning**: Küçük tutarlar için anında, düşük maliyetli transferleri seçin.





- Her zaman gönderim adreslerini kontrol edin** :
 - Para göndermeden önce Address'yi dikkatlice kontrol edin. Yanlış Address'ye gönderilen fonlar sonsuza kadar kaybolur. Kopyala/yapıştır veya QR kod taraması kullanın, asla bir Address'yi elle kopyalamayın/değiştirmeyin.





- Maliyetleri optimize edin** :
 - Zincir üzerindeki işlemler için, aciliyet ve ağ tıkanıklığına göre uygun ücretleri (yavaş, orta, hızlı) seçin.
 - Küçük miktarlar için Liquid veya Lightning kullanın.





- Uygulamayı güncel tutun




### A4. Ek kaynaklar





- Resmi Blockstream bağlantıları:**
 - [Resmi web sitesi](https://blockstream.com/)**
 - [Mobil uygulama desteği](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokümantasyon ve sohbet
 - [GitHub](https://github.com/Blockstream/green_android)**





- Blok Kaşifleri :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blok Akış Bilgisi](https://blockstream.info/Liquid)**
 - Yıldırım: **[1ML (Lightning Network)](https://1ml.com/)**





 - Öğrenme ve dersler:** **[Plan ₿ Network](https://planb.network/)** :
  - Kurtarma ifadenizi güvence altına alma



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Sözlük](https://planb.network/fr/resources/glossary/Liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Sözlük](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb