---
name: Blockstream Uygulaması - Liquid
description: Blockstream Uygulaması nasıl yapılandırılır ve Liquid Network nasıl kullanılır
---
![cover](assets/cover.webp)


## 1. Giriş


### 1.1 Eğitim hedefi





- Bu eğitim, bir **Bitcoin Liquid** portföyünü, yani doğrudan Bitcoin "Liquid" yan zincirine kaydedilen işlemleri yönetmek için **Blockstream App** mobil uygulamasının nasıl kullanılacağını açıklamaktadır.
- Kurulum, ilk yapılandırma, bir Software Wallet oluşturulması ve Liquid üzerinde bitcoin alma ve gönderme işlemlerini kapsar.
- Not: Ekler bölümündeki diğer eğitimler Onchain, Watch-Only ve masaüstü sürümünü kapsamaktadır.



### 1.2 Hedef kitle





- Yeni başlayanlar**: Liquid Network'yı entegre eden sezgisel bir mobil uygulama ile bitcoinlerini yönetmek isteyen kullanıcılar.
- Orta düzey kullanıcılar**: Onchain işlevlerini ve Tor ya da SPV gibi gizlilik seçeneklerini anlamak isteyen kişiler.



### 1.3 Liquid ile tanışın



**Liquid**, **[Blockstream](https://blockstream.com/Liquid/)** tarafından geliştirilen, ana Blockchain Bitcoin'e bağlı kalırken daha hızlı, daha fazla Confidential Transactions ve gelişmiş işlevsellik sunmak için tasarlanmış bir **Sidechain** Bitcoin'dir.



Sidechain, **iki yönlü peg** olarak bilinen bir mekanizma kullanarak Bitcoin ile paralel çalışan bağımsız bir Blockchain'tür. Bu sistem, bitcoinleri ana Blockchain'e kilitleyerek **Liquid-Bitcoins (L-BTC)**, orijinal bitcoinlerle değer eşitliğini koruyarak Liquid Network'te dolaşan tokenlar oluşturur. Fonlar herhangi bir zamanda Blockchain Bitcoin'ya iade edilebilir.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitcoinler (BTC) Liquid federasyonu tarafından ana Blockchain'e kilitlenir. Karşılığında, iki zincir arasında parite sağlayan eşdeğer miktarda Liquid-Bitcoins (L-BTC) Blockchain Liquid'da çıkarılır ve kullanıcıya gönderilir.





- (2) Bağımsız işlemler** : İşlemler, kullanıcı gereksinimlerine bağlı olarak ana Blockchain (BTC) ve Sidechain Liquid (L-BTC) üzerinde aynı anda ve bağımsız olarak çalışabilir.





- (3) Peg-out**: Kullanıcı Liquid-Bitcoinlerini (L-BTC) Liquid federasyonuna geri gönderir. Federasyon daha sonra ana Blockchain'te eşdeğer miktarda bitcoinin (BTC) kilidini açar ve bunları kullanıcıya aktarır.



Liquid, blok doğrulama ve iki taraflı sabitlemeyi yöneten güvenilir katılımcılardan (borsalar, tanınmış Bitcoin şirketleri) oluşan bir **federasyona** dayanır. Merkezi olmayan ve madencilere dayanan Blockchain Bitcoin'nın aksine, Liquid bir **federasyon** ağıdır, yani güvenliği ve yönetişimi bu katılımcılara bağlıdır. Bu, ademi merkeziyetçilikten ödün vermek anlamına gelse de, optimize edilmiş performans ve gelişmiş işlevsellik sağlar.



![image](assets/fr/18.webp)



##### Neden Liquid kullanılmalı?





- Hız**: Liquid'daki işlemler, bir doğrulayıcılar federasyonu tarafından her dakika oluşturulan bloklar sayesinde, zincir üzerindeki işlemler için 10 dakika veya daha fazla süreye kıyasla yaklaşık **1 dakika** içinde onaylanır.
- Geliştirilmiş gizlilik**: Liquid, aktarılan varlık miktarını ve türünü gizleyerek işlemleri daha gizli hale getiren **Confidential Transactions** kullanır (adresler görünür kalsa da).
- Düşük ücretler** : Liquid'deki işlemler genellikle daha ucuzdur, bu da onları sık transferler veya küçük miktarlar için ideal hale getirir.
- Birden fazla varlık**: L-BTC'lere ek olarak Liquid, belirli uygulamalarda kullanılmak üzere sabit paralar veya jetonlar gibi diğer dijital varlıkların çıkarılmasını da destekler.
- Kullanım alanları**: Liquid, Bitcoin'ün güvenliğine bağlı kalırken platformlar arası borsalar, hızlı ödemeler veya akıllı sözleşmeler gerektiren uygulamalar için özellikle uygundur.



**Not: Bu eğitim, Blockstream Uygulaması aracılığıyla Liquid kullanımına odaklanmaktadır. Liquid Network'yı derinlemesine anlamak için ekte kaynaklar bulacaksınız.



### 1.4. Hot Wallet hatırlatma





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: bir akıllı telefona, bilgisayara veya internete bağlı herhangi bir cihaza yüklenen ve bir Bitcoin Wallet'deki özel anahtarların yönetilmesini ve güvence altına alınmasını sağlayan bir uygulamanın tüm adları.
- Anahtarları çevrimdışı olarak izole eden **Cold cüzdanları** olarak da bilinen **donanım cüzdanlarının** aksine, yazılım cüzdanları bağlı bir ortamda çalışır ve bu da onları siber saldırılara karşı daha savunmasız hale getirir.





- Önerilen kullanım** :
    - Özellikle günlük işlemler için orta miktarda Bitcoin yönetimi için idealdir.
    - Hardware Wallet'nın gereksiz görünebileceği yeni başlayanlar veya sınırlı varlığa sahip kullanıcılar için uygundur.





- Sınırlamalar**: Büyük fonları veya uzun vadeli birikimleri saklamak için daha az güvenlidir. Bu durumda bir Hardware Wallet seçin.




## 2. Blockstream Uygulaması ile tanışın





- Blockstream App**, Bitcoin cüzdanlarını ve Liquid Network'daki varlıkları yönetmek için bir mobil (iOS, Android) ve masaüstü uygulamasıdır. Blockstream] (https://blockstream.com/) tarafından 2016 yılında satın alınan bu uygulama daha önce *Green Address* ve ardından *Blockstream Green* olarak adlandırılmıştır.
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
- Neden? **: IP Address'ünüzü gizleyin ve gizliliğinizi koruyun, ağınıza güvenmiyorsanız (örneğin halka açık Wi-Fi) idealdir.
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
- Dezavantaj**: Bazı bilgiler için üçüncü taraf düğümlere dayandığından Full node'dan daha az güvenlidir.
- Öneri**: Kişisel bir düğüm kullanamıyorsanız ancak optimum güvenlik için bir Full node tercih ediyorsanız SPV'yi etkinleştirin.





## 4. Bir Bitcoin onchain portföyü oluşturma



### 4.1. Oluşturmaya başlayın





- Dikkat**: Portföyünüzü kameraların veya gözlemcilerin olmadığı özel bir ortamda oluşturun.
- Ana ekrandan "Başlayın" seçeneğine tıklayın:



![image](assets/fr/04.webp)





- Bir **Cold Wallet** (çevrimdışı Wallet) yönetmek istiyorsanız: Hardware Wallet Blockstream Jade veya diğer uyumlu Cold cüzdanlarını kullanmak için **"Connect Jade "** seçeneğine tıklayın.



![image](assets/fr/05.webp)






- Sonraki ekran görüntülenir:



![image](assets/fr/06.webp)






- (1) **"Mobil Wallet Kurulumu "** : Yeni bir Hot Wallet (Hot Wallet) oluşturun.
- (2) **"Yedekten Geri Yükleme "**: Mevcut bir portföyü bir Mnemonic cümlesi (12 veya 24 kelime) kullanarak içe aktarın. Uyarı: İfadeyi bir Cold Wallet'den içe aktarmayın, çünkü bağlı bir cihazda açığa çıkacak ve güvenliğini geçersiz kılacaktır.
- (3) **"Yalnızca İzle "**: Mnemonic ifadesini açığa çıkarmadan bakiyeyi (örneğin Cold Wallet'inizin) görüntülemek için mevcut bir salt okunur portföyü içe aktarın. Ekteki "Sadece İzle" eğitimine bakın.



**Bu eğitimde**: Bir Hot Wallet oluşturmak için **"Setup Mobile Wallet"** üzerine tıklayın.


Wallet'iniz otomatik olarak oluşturulur ve burada "My Wallet 5" olarak adlandırılan Wallet ana sayfası görüntülenir:



![image](assets/fr/07.webp)



**Önemli**: Blockstream Uygulaması, 12 kelimelik seed ifadesini otomatik olarak görüntülemeyerek bir Wallet oluşturulmasını basitleştirmiştir. *Portföy artık tek bir tıklamayla oluşturulmuş olsa da, seed cümlenizi kaydetmezseniz fonlarınıza erişimi kaybetme riskiyle karşı karşıya kalırsınız*.



### 4.2. seed ifadesini kaydedin





- Wallet ana ekranında, "Güvenlik" sekmesine, ardından "Yedekle" istemine veya "Kurtarma İfadesi" menüsüne tıklayın:



![image](assets/fr/08.webp)



seed 12 kelimelik ifade kaydetmeniz için görüntülenecektir.





- Kurtarma ifadenizi son derece dikkatli bir şekilde yazın. Kağıt veya metal üzerine yazın ve güvenli bir yerde (güvenli, çevrimdışı konum) saklayın. Bu ifade, cihazınızın kaybolması veya uygulamanın silinmesi durumunda bitcoinlerinize erişmek için tek yolunuzdur.
- Bu ifadeye sahip herhangi birinin tüm bitcoinlerinizi çalabileceğini de unutmamak gerekir. Asla dijital olarak saklamayın:
 - Ekran görüntüsü yok
 - Bulut, e-posta veya mesajlaşma yedeklemesi yok
 - Kopyala/yapıştır yok (panoya kaydetme riski)



**! Bu nokta kritiktir**. Yedekleme hakkında daha fazla bilgi için :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. seed cümlesini kontrol edin



Bu seed ifadesiyle ilişkili bir Address'ye para göndermeden önce, 12 kelimenizin yedeğini test etmelisiniz.


Bunu yapmak için bir referans yazacağız, Wallet'ü sileceğiz, yedekle geri yükleyeceğiz ve referansın değişmediğini kontrol edeceğiz.





- Wallet ana ekranında, "Ayarlar" sekmesine, ardından "Wallet Ayrıntıları "na tıklayın ve zPub'ı ([genişletilmiş genel anahtar](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602)) kopyalayın:



![image](assets/fr/09.webp)



Not: "Yalnızca İzle" işlevi için Blockstream uygulamanıza bir zpub Address aktarılabilir (bkz. Ek).





- Uygulamayı silin, ardından Mnemonic ifadesini girerek **"Yedekten Geri Yükle "** aracılığıyla Wallet'i geri yükleyin ve zpub'ın değişmediğini kontrol edin. Evet ise, yedeklemeniz doğrudur ve Wallet'e para gönderebilirsiniz.





- Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için burada özel bir eğitim bulabilirsiniz:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Uygulamaya erişimin güvence altına alınması



Güçlü bir PIN kodu ile uygulamaya erişimi kilitleyin:




- Wallet ana ekranından **"Güvenlik "** öğesine gidin ve ardından **"PIN "** öğesine tıklayın
- Rastgele 6 haneli bir PIN kodu** girin ve onaylayın.



**Biyometrik seçenek**: Daha fazla kolaylık için kullanılabilir, ancak sağlam bir PIN kodundan daha az güvenlidir (yetkisiz erişim riski, örneğin uyku sırasında parmak izi veya yüz taraması).



**Not**: PIN cihazı güvence altına alır, ancak fonları kurtarmak için yalnızca seed ifadesi kullanılabilir.





## 5. Liquid Wallet'nin Kullanımı



### 5.1. "L-BTC" bitcoinleri alın



Liquid-Bitcoin (L-BTC) almak için çeşitli seçenekler mevcuttur. Aşağıda ayrıntıları verilen Liquid alan bir Address paylaşarak birinden size doğrudan bir miktar göndermesini isteyebilirsiniz.



Alternatif olarak, Exchange bitcoinlerinizi zincir üzerinde veya [Boltz gibi bir köprü] (https://boltz.Exchange/) kullanarak L-BTC için Lightning Network aracılığıyla: Address alan Liquid'inizi girin, tercih ettiğiniz şekilde ödeme yapın ve L-BTC'nizi alın.





- Portföy ana ekranından '"**İşlem**" ve ardından **"Al "** seçeneğine tıklayın.



![image](assets/fr/19.webp)





- Varsayılan olarak, uygulama boş bir **receipt Address, onchain** (SegWit v0 formatı, `bc1q...` ile başlar) görüntüler. Liquid Bitcoin** seçmek için "Bitcoin" üzerine tıklayın:



![image](assets/fr/20.webp)





- Seçenekler** :
 - (1) Bu seed cümlesine bağlı başka bir yeni Address seçmek için oklara tıklayın.
    - (2) Ayrıca sağ üstteki üç noktaya ve ardından "Adres Listesi "ne tıklayarak halihazırda kullanılan/görüntülenenler arasından bir Address seçebilirsiniz
    - (3) Belirli bir tutar talep etmek için sağ üstteki üç noktaya tıklayın, "Tutar talep et" seçeneğini seçin ve istediğiniz tutarı girin. QR güncellenecek ve Address, Bitcoin ödeme URI'si ile değiştirilecektir.



![image](assets/fr/21.webp)





- "**Paylaş**" üzerine tıklayarak, metni kopyalayarak veya QR kodunu tarayarak Address/URI'yi paylaşın.
- Doğrulama**: Hataları veya saldırıları (örn. panoyu değiştiren kötü amaçlı yazılımlar) önlemek için alıcıyla paylaşılan Address'u mümkün olduğunca kontrol edin.



### 5.2. bitcoin göndermek





- Portföy ana ekranından "**İşlem**" ve ardından **"Gönder "** seçeneğine tıklayın:



![image](assets/fr/22.webp)





- Ayrıntıları girin** :
    - (1) Alıcının **Address'sini** üzerine yapıştırarak veya bir QR kodunu tarayarak girin.
    - (2) Varlıkları ve fonların gönderildiği hesabı kontrol edin.
    - (3) Gönderilecek **miktarı** belirtin. Birimi seçebilirsiniz: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- Çek** :
    - Özet ekranında Address'i, tutarı ve ücretleri kontrol edin.
    - Bir Address hatası, geri dönüşü olmayan fon kaybına neden olabilir. Panoyu değiştiren kötü amaçlı yazılımlara karşı dikkatli olun.



![image](assets/fr/24.webp)





- Onaylama**: İşlemi imzalamak ve dağıtmak için "Gönder" düğmesini kaydırın.
- Takip**: Wallet "İşlem" sekmesinde, işlem "Onaylanmadı", ardından "Onaylandı" ve ardından "Tamamlandı" olarak görünür:



![image](assets/fr/25.webp)





- Liquid'te 2 blok arasındaki süre 1 dakikadır, bu nedenle işlem hızlı bir şekilde onaylanır ve tamamlanır.




## Ekler



### A1. Diğer Blockstream Uygulama eğitimleri



Onchain ağını kullanma



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

"Sadece İzle" modunda bir Wallet'in içe aktarılması ve izlenmesi



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Masaüstü sürümü



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. En iyi uygulamalar



Blockstream Uygulamasını** güvenli ve verimli bir şekilde kullanmak için bu önerileri izleyin. Bunlar, **Bitcoin (onchain)**, **Liquid** ve **Lightning** ağlarında paranızı korumanıza, işlemlerinizi optimize etmenize ve gizliliğinizi korumanıza yardımcı olacaktır.





- Kurtarma cümlenizi güvence altına alın** :
 - Eğitim: Mnemonic ifadenizi kaydetme



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Güvenli kimlik doğrulama kullanın** :
 - Uygulamaya erişimi korumak için bir **güçlü PIN** veya **biyometrik kimlik doğrulama** (parmak izi veya yüz tanıma) etkinleştirin.
 - PIN kodunuzu veya biyometrik verilerinizi asla paylaşmayın.





- Gizliliğinizi koruyun** :
 - generate her zincirleme alım için yeni bir Address veya Blockchain üzerindeki izlemeyi sınırlamak için Liquid.
 - "Geliştirilmiş Gizlilik", "Tor" ve "SPV" işlevlerini etkinleştirin.
 - Maksimum gizlilik için, Wallet'ünüzü genel düğümü kullanmak yerine bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayın





- İhtiyaçlarınıza en uygun ağı seçin** :
 - Onchain**: Uzun vadeli saklama veya büyük değerli işlemler için tercih edilir (ücretler tutara göre ihmal edilebilir).
 - Liquid**: Gelişmiş gizlilik ile hızlı, düşük maliyetli transferler için kullanın.
 - Lightning**: Küçük tutarlar için anında, düşük maliyetli transferleri seçin.





- Her zaman gönderim adreslerini kontrol edin** :
 - Para göndermeden önce Address'yı dikkatlice kontrol edin. Yanlış Address'ya gönderilen fonlar sonsuza kadar kaybolur. Kopyala/yapıştır veya QR kod taraması kullanın, asla bir Address'yı elle kopyalamayın/değiştirmeyin.





- Maliyetleri optimize edin** :
 - Zincir üzerindeki işlemler için, aciliyet ve ağ tıkanıklığına göre uygun ücretleri (yavaş, orta, hızlı) seçin.
 - Küçük miktarlar için Liquid veya Lightning kullanın.





- Uygulamayı güncel tutun




### A3. Ek kaynaklar





- Resmi bağlantılar:**
 - [Resmi web sitesi](https://blockstream.com/)**
 - [Mobil uygulama desteği](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokümantasyon ve sohbet
 - [GitHub](https://github.com/Blockstream/green_android)**





- Blok Kaşifleri :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
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