---
name: Blockstream App - Onchain
description: Mobil cihazlarda Blockstream Uygulamasını kurun ve onchain işlemlerini yönetin
---
![cover](assets/cover.webp)


## 1. Giriş


### 1.1 Eğitim hedefi





- Bu eğitimde **Blockstream App** mobil uygulamasının bir Bitcoin **onchain** Wallet'yi, yani doğrudan ana Blockchain Bitcoin'e kaydedilen işlemleri yönetmek için nasıl kullanılacağı açıklanmaktadır.
- Kurulum, ilk yapılandırma, bir Software Wallet oluşturma ve bitcoin alma ve gönderme işlemlerini kapsar.
- Not: Eklerdeki diğer eğitimler Liquid, Yalnızca İzle ve masaüstü sürümünü kapsamaktadır.



![image](assets/fr/01.webp)



### 1.2 Hedef kitle





- **Yeni başlayanlar**: Sezgisel bir mobil uygulama ile bitcoinlerini yönetmek isteyen kullanıcılar.
- **Orta düzey kullanıcılar**: Onchain işlevlerini ve Tor ya da SPV gibi gizlilik seçeneklerini anlamak isteyen kişiler.



### 1.3. Hot cüzdanları hakkında hatırlatmalar





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: Bitcoin Wallet'deki özel anahtarların yönetilmesini ve güvence altına alınmasını sağlayan akıllı telefon, bilgisayar veya İnternet bağlantılı herhangi bir cihaza yüklenen bir uygulamanın tüm adları.
- Anahtarları çevrimdışı olarak izole eden **Cold cüzdanları** olarak da bilinen **donanım cüzdanlarının** aksine, yazılım cüzdanları bağlı bir ortamda çalışır ve bu da onları siber saldırılara karşı daha savunmasız hale getirir.





- **Önerilen kullanım**:
    - Özellikle günlük işlemler için orta miktarda Bitcoin yönetimi için idealdir.
    - Hardware Wallet'nin gereksiz görünebileceği yeni başlayanlar veya sınırlı varlığa sahip kullanıcılar için uygundur.





- **Sınırlamalar**: Büyük fonları veya uzun vadeli tasarrufları saklamak için daha az güvenli. Bu durumda bir Hardware Wallet seçin.




## 2. Blockstream Uygulaması ile tanışın





- **Blockstream App**, Bitcoin portföylerini ve Liquid Network'teki varlıkları yönetmek için bir mobil (iOS, Android) ve masaüstü uygulamasıdır. [Blockstream](https://blockstream.com/) tarafından 2016 yılında satın alınan bu uygulama daha önce *Green Address* ve ardından *Blockstream Green* olarak adlandırılmıştır.
- **Temel özellikler**:
- Blockchain Bitcoin üzerinde **zincirleme** işlemler.
    - Ağ işlemleri **Liquid** (hızlı, gizli alışverişler için Sidechain).
- Anahtarlara erişim olmadan fonları izlemek için yalnızca **izle** portföyleri.
    - Gizlilik seçenekleri: **Tor** üzerinden bağlantı, Electrum üzerinden bir **kişisel düğüme** bağlantı veya üçüncü taraf düğümlere bağımlılığı azaltmak için **SPV** doğrulaması.
    - Onaylanmamış işlemleri hızlandırmak için **Replace-by-fee (RBF)** fonksiyonları.
- Uyumluluk**: Blockstream Jade** gibi donanım cüzdanlarını entegre eder.
- **Interface**: Yeni başlayanlar için sezgisel, uzmanlar için gelişmiş seçenekler.
- **Not**: Bu kılavuz zincir üzerinde kullanıma odaklanmaktadır. Ekler bölümündeki diğer eğitimler Liquid, Yalnızca İzle ve masaüstü sürümünü kapsamaktadır.



## 3. Blockstream Uygulamasını yükleme ve yapılandırma



### 3.1. İndirin





- **Android için**:
    - Google Play Store'dan [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) uygulamasını indirin.
    - Alternatif: Blockstream'in resmi GitHub](https://github.com/Blockstream/green_android) adresinde bulunan APK dosyası aracılığıyla yükleyin.
- **IOS için**:
    - App Store'dan [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) uygulamasını indirin.
- **Not**: Sahte uygulamalardan kaçınmak için resmi kaynaklardan indirdiğinizden emin olun.



### 3.2. ilk yapılandırma





- **Ana ekran**: İlk açıldığında, uygulama yapılandırılmış bir Wallet olmayan bir ekran görüntüler. Oluşturulan veya içe aktarılan portföyler daha sonra burada görünecektir.



![image](assets/fr/02.webp)





- **Ayarları özelleştirin**: "Uygulama ayarları" üzerine tıklayın, aşağıdaki seçenekleri ayarlayın, "Kaydet" üzerine tıklayın, uygulamayı yeniden başlatın ve portföyünüzü oluşturun.



![image](assets/fr/03.webp)



#### 3.2.1. Geliştirilmiş gizlilik (yalnızca Android)





- **İşlev**: Ekran görüntülerini devre dışı bırakır, görev yöneticisinde uygulama önizlemelerini gizler ve telefon kilitlendiğinde erişimi kilitler.
- Neden? Verilerinizi yetkisiz fiziksel erişime veya ekran yakalayan kötü amaçlı yazılımlara karşı korur.


#### 3.2.2. Tor üzerinden bağlantı





- **İşlev**: Ağ trafiğini, bağlantılarınızı şifreleyen anonim bir ağ olan **Tor** üzerinden yönlendirin.
- **Neden?**: IP Address'inizi gizleyin ve gizliliğinizi koruyun, ağınıza güvenmiyorsanız (örneğin halka açık Wi-Fi) idealdir.
- **Dezavantaj**: Şifreleme nedeniyle uygulamayı yavaşlatabilir.
- **Öneri**: Gizlilik öncelikliyse Tor'u etkinleştirin, ancak bağlantı hızını test edin.


#### 3.2.3. Kişisel bir düğüme bağlanma





- **İşlev**: Uygulamayı bir **Electrum** sunucusu aracılığıyla kendi **tamamlanmış Bitcoin düğümünüze** bağlar.
- Neden? Blockstream sunucularına bağımlılığı ortadan kaldırarak Blockchain verileri üzerinde tam kontrol sağlar.
- **Ön koşul**: Yapılandırılmış bir Bitcoin düğümü.
- **Tavsiye**: Maksimum egemenlik arayan ileri düzey kullanıcılar.


#### 3.2.4. SPV doğrulaması





- **İşlev**: Tüm zinciri indirmeden belirli Blockchain verilerini doğrudan doğrulamak için **Basitleştirilmiş Ödeme Doğrulaması (SPV)** kullanır.
- Neden? Mobil cihazlar için hafif kalırken Blockstream'in varsayılan düğümüne bağımlılığı azaltır.
- **Dezavantaj**: Bazı bilgiler için üçüncü taraf düğümlere dayandığından Full node'dan daha az güvenlidir.
- **Öneri**: Kişisel bir düğüm kullanamıyorsanız ancak optimum güvenlik için bir Full node tercih ediyorsanız SPV'yi etkinleştirin.





## 4. Bitcoin onchain portföyü oluşturma



### 4.1. Oluşturmaya başlayın





- **Dikkat**: Portföyünüzü kameraların veya gözlemcilerin olmadığı özel bir ortamda oluşturun.
- Ana ekrandan "Başlayın" seçeneğine tıklayın:



![image](assets/fr/04.webp)





- Bir **Cold Wallet** (çevrimdışı Wallet) yönetmek istiyorsanız: Hardware Wallet Blockstream Jade veya diğer uyumlu Cold cüzdanlarını kullanmak için **"Connect Jade "** seçeneğine tıklayın.



![image](assets/fr/05.webp)





- Sonraki ekran görüntülenir:



![image](assets/fr/06.webp)





- (1) **"Mobil Wallet Kurulumu "** : Yeni bir Hot Wallet (Hot Wallet) oluşturun.
- (2) **"Yedeklemeden Geri Yükle "**: Mnemonic cümlesi (12 veya 24 kelime) kullanarak mevcut bir portföyü içe aktarın. Dikkat: Bir Cold Wallet ifadesini içe aktarmayın, çünkü bağlı bir cihazda açığa çıkacak ve güvenliğini geçersiz kılacaktır.
- (3) **"Yalnızca İzle "**: Mnemonic ifadesini açığa çıkarmadan bakiyeyi (örneğin Cold Wallet'inizin) görüntülemek için mevcut bir salt okunur portföyü içe aktarın. Ekteki Yalnızca İzle eğitimine bakın.



**Bu eğitimde**: Bir Hot Wallet oluşturmak için **"Setup Mobile Wallet"** üzerine tıklayın.


Wallet'niz otomatik olarak oluşturulur ve burada "My Wallet 5" olarak adlandırılan Wallet ana sayfası görüntülenir:



![image](assets/fr/07.webp)



**Önemli**: Blockstream Uygulaması, 12 kelimelik seed ifadesini otomatik olarak görüntülemeyerek bir Wallet oluşturulmasını basitleştirmiştir. *Portföy artık tek bir tıklamayla oluşturulsa da, seed cümlenizi kaydetmezseniz fonlarınıza erişiminizi kaybetme riskiyle karşı karşıya kalırsınız*.



### 4.2. seed cümlesini kaydedin





- Wallet ana ekranında "Güvenlik" sekmesine, ardından "Yedekle" istemine veya "Kurtarma İfadesi" menüsüne tıklayın:



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

### 4.3. seed cümlesini onaylayın



Bu seed cümlesiyle ilişkili bir Address'a fon göndermeden önce, 12 kelimenizin yedeğini test etmelisiniz.



Bunu yapmak için bir referans yazacağız, Wallet'i sileceğiz, yedekle geri yükleyeceğiz ve referansın değişmediğini kontrol edeceğiz.





- Wallet ana ekranında, "Ayarlar" sekmesine, ardından "Wallet Ayrıntıları "na tıklayın ve zPub ([genişletilmiş genel anahtar](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602)) kopyalayın:



![image](assets/fr/09.webp)



Not: "Sadece İzle" işlevi için Blockstream uygulamanıza bir zpub Address aktarılabilir (bkz. Ek).





- Uygulamayı silin, ardından Mnemonic ifadesini girerek **"Yedekten Geri Yükle "** aracılığıyla Wallet'i geri yükleyin ve zpub'ın değişmediğini kontrol edin. Evet ise, yedeklemeniz doğrudur ve Wallet'e para gönderebilirsiniz.





- Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için burada özel bir eğitim bulabilirsiniz:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Uygulamaya erişimin güvence altına alınması



Güçlü bir PIN kodu ile uygulamaya erişimi kilitleyin:




- Wallet ana ekranından **"Güvenlik "** öğesine gidin ve ardından **"PIN "** öğesine tıklayın
- Rastgele 6 haneli bir **PIN kodu** girin ve onaylayın.



**Biyometrik seçenek**: Daha fazla kolaylık için kullanılabilir, ancak sağlam bir PIN kodundan daha az güvenlidir (yetkisiz erişim riski, örneğin uyku sırasında parmak izi veya yüz taraması).



**Not**: PIN cihazı güvence altına alır, ancak fonları geri almak için yalnızca seed ifadesi kullanılabilir.





## 5. Onchain Wallet'i kullanma



### 5.1. Bitcoin almak





- Portföy ana ekranından '"**İşlem**" ve ardından **"Al "** seçeneğine tıklayın.



![image](assets/fr/10.webp)





- Uygulama bir **boş alım Address** (SegWit v0 formatı, `bc1q...` ile başlar) görüntüler. Her Bitcoin aldığınızda yeni bir Address kullanmanız gizliliğinizi artırır.





- **Seçenekler**:
    - (1) "Bitcoin": bir zincir üstü veya Liquid sevkiyatı seçmek için tıklayın ve varlığı seçin.
    - (2) Bu seed cümlesine bağlı başka bir yeni Address seçmek için oklara tıklayın.
    - (3) Ayrıca sağ üstteki üç noktaya ve ardından "Adres Listesi "ne tıklayarak halihazırda kullanılan/görüntülenenler arasından bir Address seçebilirsiniz
    - (4) Belirli bir tutar talep etmek için sağ üstteki üç noktaya tıklayın, "Tutar talep et" seçeneğini seçin ve istediğiniz tutarı girin. QR güncellenecek ve Address'nin yerini bir Bitcoin ödeme URI'si alacaktır.




![image](assets/fr/11.webp)





- Address/URI'yi "**Paylaş**" üzerine tıklayarak, metni kopyalayarak veya QR kodunu tarayarak paylaşın.
- **Doğrulama**: Hataları veya saldırıları (örn. panoyu değiştiren kötü amaçlı yazılımlar) önlemek için alıcıyla paylaşılan Address'i mümkün olduğunca kontrol edin.



### 5.2. bitcoin göndermek





- Portföy ana ekranından "**İşlem**" ve ardından **"Gönder "** seçeneğine tıklayın:



![image](assets/fr/12.webp)





- **Ayrıntıları girin**:
    - (1) Alıcının **Address'ini** üzerine yapıştırarak veya bir QR kodunu tarayarak girin.
    - (2) Varlıkları ve fonların gönderildiği hesabı kontrol edin.
    - (3) Gönderilecek **miktarı** belirtin. Birimi seçebilirsiniz: BTC, satoshis, USD, ...


03/08/2025 tarihindeki minimum miktar (sus limiti) 546 Sats'dir.




    - (4) **işlem ücretlerini** seçin:
        - Aciliyete bağlı olarak önerilen seçeneklerden (örn. hızlı, orta, yavaş) birini seçin ve yaklaşık aktarım süresi görüntülenecektir.
        - Özelleştirilmiş ücretler için, vbyte başına Satoshi sayısını manuel olarak ayarlayın (piyasa oranları için [Mempool.space](https://Mempool.space/) adresine bakın).




![image](assets/fr/13.webp)





- **Çek** :
    - Özet ekranında Address, tutar ve ücretleri kontrol edin.
    - Bir Address hatası geri dönüşü olmayan fon kaybına neden olabilir. Panoyu değiştiren kötü amaçlı yazılımlara karşı dikkatli olun.



![image](assets/fr/14.webp)





- **Onaylama**: İşlemi imzalamak ve dağıtmak için "Gönder" düğmesini kaydırın.
- **Takip**: Wallet "İşlem" sekmesinde, işlem onaylanana kadar (1 ila 6 onay) "beklemede" olarak görünür:



![image](assets/fr/15.webp)





- İşlem onaylanmadığı sürece, "Replace by fee" işlevi (bkz. Ek) işlem ücretlerini artırarak işlemin gerçekleştirilmesini hızlandırmanıza olanak tanır:



![image](assets/fr/16.webp)




## Ekler



### A1. Diğer Blockstream eğitimleri



Liquid Network'un Kullanımı



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

"Sadece İzle" modunda bir Wallet'ı içe aktarma ve izleme



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Masaüstü sürümü



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Replace-by-fee'in Açıklaması (RBF)



**Tanım**: Replace-by-fee (RBF), göndericinin daha yüksek bir ücret ödemeyi kabul ederek bir **zincir üzerinde** işlemin onaylanmasını hızlandırmasına olanak tanıyan Bitcoin ağının bir özelliğidir.



**Limits** :




- RBF, Liquid veya Lightning işlemleri için kullanılamaz.
- İlk işlem oluşturulduğunda RBF uyumlu olarak işaretlenmelidir ve Blockstream App bunu otomatik olarak yapar.



**Daha fazla bilgi:**




- [Sözlük](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. En iyi uygulamalar



**Blockstream Uygulamasını** güvenli ve verimli bir şekilde kullanmak için bu önerileri izleyin. Bunlar, **Bitcoin (onchain)**, **Liquid** ve **Lightning** ağlarında paranızı korumanıza, işlemlerinizi optimize etmenize ve gizliliğinizi korumanıza yardımcı olacaktır.





- **Kurtarma cümlenizi güvence altına alın** :
 - Eğitim: Mnemonic ifadenizi kaydetme



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Güvenli kimlik doğrulama kullanın**:
 - Uygulamaya erişimi korumak için bir **güçlü PIN** veya **biyometrik kimlik doğrulama** (parmak izi veya yüz tanıma) etkinleştirin.
 - PIN kodunuzu veya biyometrik verilerinizi asla paylaşmayın.





- **Gizliliğinizi koruyun**:
 - generate Blockchain üzerindeki izlemeyi sınırlandırmak için her zincir üstü veya Liquid alımı için yeni bir Address.
 - "Geliştirilmiş Gizlilik", "Tor" ve "SPV" işlevlerini etkinleştirin.
 - Maksimum gizlilik için, Wallet'inizi genel düğümü kullanmak yerine bir Electrum sunucusu aracılığıyla kendi Bitcoin düğümünüze bağlayın





- **İhtiyaçlarınıza en uygun ağı seçin**:
- **Onchain**: Uzun vadeli saklama veya büyük değerli işlemler için tercih edilir (ücretler tutara göre ihmal edilebilir).
- **Liquid**: Gelişmiş gizlilik ile hızlı, düşük maliyetli transferler için kullanın.
- **Lightning**: Küçük tutarlar için anında, düşük maliyetli transferleri seçin.





- Her zaman gönderim adreslerini kontrol edin:
 - Para göndermeden önce Address'u dikkatlice kontrol edin. Yanlış Address'a gönderilen fonlar sonsuza kadar kaybolur. Kopyala/yapıştır veya QR kod taraması kullanın, asla bir Address'u elle kopyalamayın/değiştirmeyin.





- **Maliyetleri optimize edin**:
 - Zincir üzerindeki işlemler için, aciliyet ve ağ tıkanıklığına göre uygun ücretleri (yavaş, orta, hızlı) seçin.
 - Küçük miktarlar için Liquid veya Lightning kullanın.





- Uygulamayı güncel tutun




### A4. Ek kaynaklar





- **Resmi bağlantılar:**
- [Resmi web sitesi](https://blockstream.com/)
- [Mobil uygulama desteği](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/) : dokümantasyon ve sohbet
- [GitHub](https://github.com/Blockstream/green_android)





- Blok Kaşifleri :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blok Akış Bilgisi](https://blockstream.info/Liquid)**
 - Yıldırım: **[1ML (Lightning Network)](https://1ml.com/)**





- **Öğrenme ve dersler:** **[Plan ₿ Network](https://planb.network/)**:
 - Kurtarma ifadenizi güvence altına alma



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Sözlük](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Sözlük](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb