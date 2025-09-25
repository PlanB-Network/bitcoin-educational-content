---
name: Blockstream App - Desktop
description: Blockstream Uygulaması ile Hardware Wallet'ınızı bir bilgisayarda nasıl kullanabilirsiniz?
---
![cover](assets/cover.webp)



## 1. Giriş



### 1.1 Eğitim hedefi





- Bu eğitimde, ana Blockchain Bitcoin'te kaydedilen işlemlerin güvenliğini sağlayarak bir **Hardware Wallet** ile bir Bitcoin **onchain** Wallet'ü yönetmek için bir bilgisayarda **Blockstream Uygulamasının** nasıl kullanılacağı açıklanmaktadır.
- Kurulum, ilk yapılandırma, bir Hardware Wallet bağlama ve zincir üzerinde bitcoin alma ve gönderme konularını kapsar.
- Not: Eklerdeki diğer eğitimler Liquid, Yalnızca İzle ve mobil uygulamayı kapsamaktadır.



### 1.2 Hedef kitle





- **Yeni başlayanlar**: Bitcoinlerini güvenli bir masaüstü yazılımı ve bir Hardware Wallet ile yönetmek isteyen kullanıcılar.
- **Orta düzey kullanıcılar**: Zincir üzerinde işlemler için Hardware Wallet'in nasıl kullanılacağını ve Tor ya da SPV gibi gizlilik seçeneklerini anlamak isteyen kişiler.



### 1.3. Donanım cüzdanlarının arka planı





- **Hardware Wallet**, **Cold Wallet**: Özel anahtarları çevrimdışı olarak saklayan ve **Hot cüzdanlarının** (bağlı cihazlardaki yazılım cüzdanları) aksine siber saldırılara karşı yüksek düzeyde güvenlik sunan fiziksel bir cihaz.
- **Önerilen kullanım**:
    - Büyük miktarları veya uzun vadeli birikimleri güvence altına almak için idealdir.
    - Fonlarını bağlı cihazlarla ilişkili risklerden korumak isteyen güvenlik odaklı kullanıcılar için uygundur.
- **Sınırlamalar**: Bakiyeleri, generate adreslerini görüntülemek ve Hardware Wallet imzalı işlemleri yayınlamak için Blockstream Uygulaması gibi bir yazılım gerektirir.



## 2. Blockstream Uygulaması ile tanışın





- **Blockstream App**, Bitcoin cüzdanlarını ve Liquid Network'teki varlıkları yönetmek için kullanılan bir mobil (iOS, Android) ve masaüstü uygulamasıdır. Blockstream tarafından 2016 yılında satın alındı, *GreenAddress* olarak adlandırıldı, *Blockstream Green* (2019) olarak yeniden adlandırıldı ve şimdi *Blockstream app* (2025) olarak adlandırılıyor.
- **Temel özellikler**:
- Blockchain Bitcoin üzerinde **zincirleme** işlemler.
- **Liquid** ağındaki işlemler (hızlı, gizli alışverişler için Sidechain).
- Anahtarlara erişim olmadan fonları izlemek için yalnızca **izle** portföyleri.
    - Gizlilik seçenekleri: **Tor** üzerinden bağlantı, Electrum üzerinden bir **kişisel düğüme** bağlantı veya üçüncü taraf düğümlere bağımlılığı azaltmak için **SPV** doğrulaması.
    - Onaylanmamış işlemleri hızlandırmak için **Replace-by-fee (RBF)** fonksiyonları.
- Uyumluluk**: Blockstream Jade** gibi donanım cüzdanlarını entegre eder.
- **Interface**: Yeni başlayanlar için sezgisel, uzmanlar için gelişmiş seçenekler.
- **Not**: Bu kılavuz, masaüstü sürümünde Hardware Wallet ile onchain kullanımına odaklanmaktadır. Ek olarak verilen diğer eğitimler mobil uygulamada, onchain, Liquid ve Yalnızca İzle özellikleri için kullanımı kapsamaktadır.



## 3. Blockstream App Desktop'ı yükleme ve ayarlama



### 3.1. İndirin





- Resmi web sitesine] (https://blockstream.com/app/) gidin ve "_Şimdi İndir_" seçeneğine tıklayın. İşletim sisteminize (Windows, macOS, Linux) karşılık gelen sürümü indirin.
- **Not**: Sahte yazılımlardan kaçınmak için resmi kaynaktan indirdiğinizden emin olun.



### 3.2. ilk yapılandırma





- **Ana ekran**: İlk açıldığında, uygulama yapılandırılmış bir Wallet olmadan bir ekran görüntüler. Oluşturulan veya içe aktarılan portföyler daha sonra burada görünecektir.



![image](assets/fr/02.webp)





- **Ayarları özelleştirin**: Sol alttaki ayarlar simgesine tıklayın, aşağıdaki seçenekleri ayarlayın, ardından devam etmek için Interface'den çıkın.



![image](assets/fr/03.webp)



#### 3.2.1. Genel parametreler





- Ayarlar menüsünde "**Genel**" üzerine tıklayın.
- **İşlev**: Yazılım dilini değiştirin ve gerekirse deneysel işlevleri etkinleştirin.



![image](assets/fr/04.webp)



#### 3.2.2. Tor üzerinden bağlantı





- Ayarlar menüsünde "**Ağ**" üzerine tıklayın.
- **İşlev**: Ağ trafiğini, bağlantılarınızı şifreleyen anonim bir ağ olan **Tor** üzerinden yönlendirin.
- **Neden?**: IP Address'inizi gizleyin ve gizliliğinizi koruyun, ağınıza güvenmiyorsanız (örneğin halka açık Wi-Fi) idealdir.
- **Dezavantaj**: Şifreleme nedeniyle uygulamayı yavaşlatabilir.
- **Öneri**: Gizlilik öncelikliyse Tor'u etkinleştirin, ancak bağlantı hızını test edin.



![image](assets/fr/05.webp)



#### 3.2.3. Kişisel bir düğüme bağlanma





- Ayarlar menüsünde "**Özel sunucular ve doğrulama**" üzerine tıklayın.
- **İşlev**: Uygulamayı bir **Electrum sunucusu** aracılığıyla kendi **tamamlanmış Bitcoin düğümünüze** bağlar.
- Neden? Blockstream sunucularına bağımlılığı ortadan kaldırarak Blockchain verileri üzerinde tam kontrol sağlar.
- **Ön koşul**: Yapılandırılmış bir Bitcoin düğümü.
- **Tavsiye**: Maksimum egemenlik isteyen ileri düzey kullanıcılar.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV doğrulaması





- Ayarlar menüsünde "**Özel sunucular ve doğrulama**" üzerine tıklayın.
- **İşlev**: Blok başlıklarını indiren ve işlemlerinizi Blockchain'nin tamamını saklamadan dahil etme kanıtı (Merkle) ile doğrulayan **Basitleştirilmiş Ödeme Doğrulaması (SPV)** kullanır.
- Neden? Cihazlar için hafif kalırken Blockstream'in varsayılan düğümüne bağımlılığı azaltır.
- **Dezavantaj**: Bazı bilgiler için üçüncü taraf düğümlere dayandığından Full node'ten daha az güvenlidir.
- **Öneri**: Kişisel bir düğüm kullanamıyorsanız ancak optimum güvenlik için bir Full node tercih ediyorsanız SPV'yi etkinleştirin.



![image](assets/fr/07.webp)



## 4. Bir Hardware Wallet'i Blockstream Uygulamasına Bağlama



### 4.1. Ön değerlendirmeler



#### 4.1.1. Ledger kullanıcıları için





- Blockstream Green, Ledger cihazlarında (Nano S, Nano X) yalnızca **Bitcoin Legacy** uygulamasını destekler.
- Cihazınızı bağlamadan önce **Ledger Live**'da izlenecek adımlar :


1. **"Ayarlar"** → **"Deneysel özellikler"** bölümüne gidin ve **geliştirici modunu** etkinleştirin.


2. **"My Ledger"** → **"App Catalogue"** bölümüne gidin, ardından **Bitcoin Legacy** uygulamasını yükleyin


3. Bağlantı kurmak için Blockstream Green'ü başlatmadan önce Ledger'inizde **Bitcoin Legacy** uygulamasını açın.




- **Not**: Ledger'nizin kilidinin PIN kodunuzla açıldığından ve bağlandığınızda Bitcoin Legacy uygulamasının etkin olduğundan emin olun.



#### 4.1.2 Bir Hardware Wallet'in Başlatılması





- Hardware Wallet'niz (Ledger, Trezor veya Blockstream Jade) hiç kullanılmadıysa (Blockstream Green ile veya Ledger Live gibi başka bir yazılımla), önce onu başlatmanız gerekecektir. Bu adım, kameraların veya gözlemcilerin olmadığı güvenli bir ortamda gerçekleştirilmelidir:


1. **seed cümle oluşturma / Mnemonic cümle** (12, 18 veya 24 kelime): Bir kağıda dikkatlice yazın.


2. **seed ifade doğrulaması**: Belirtilen kelimelerden Wallet içe aktarımını test edin, örneğin genişletilmiş açık anahtarı doğrulayarak. Wallet'e fon göndermeden ve seed ifadesini kalıcı olarak güvence altına almadan önce gerçekleştirilmelidir.


3. **seed ifadesinin güvenliğini sağlama**: İfadeyi fiziksel bir ortamda (kağıt veya metal) ve güvenli bir yerde saklayın. Asla dijital olarak saklamayın (ekran görüntüsü, bulut veya e-posta yok).




- **Önemli**: seed ibaresi, cihazın kaybolması veya arızalanması durumunda paranızı kurtarmak için tek yolunuzdur. Erişimi olan herkes bitcoinlerinizi çalabilir.
- **seed cümlesini yedeklemek ve kontrol etmek için kaynaklar**:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Bu eğitim için konfigürasyon :





- Hardware Wallet'un bir seed cümlesi ve bir kilitleme PIN kodu ile zaten başlatılmış olduğunu varsayacağız.
- Hardware Wallet'in Blockstream App'e hiç bağlanmadığını varsayıyoruz, bu da yeni bir hesap oluşturulmasını gerektirir. Hardware Wallet zaten Blockstream App ile kullanılmışsa, uygulama açıldığında hesap otomatik olarak görünecektir.



### 4.2. Bağlantıyı başlat





- Ana ekrandan "**Yeni bir Wallet Kur**" seçeneğine tıklayın, ardından hüküm ve koşulları onaylayın ve "**Başlayın**" seçeneğine tıklayın:



![image](assets/fr/08.webp)





- "**Hardware Wallet** üzerinde" seçeneğini seçin:



![image](assets/fr/09.webp)





- Eğer bir **Blockstream Jade** kullanıyorsanız, ilgili düğmeye tıklayın. Aksi takdirde, "**Farklı bir Donanım Aygıtı Bağlayın**" seçeneğini seçin:



![image](assets/fr/10.webp)





- Hardware Wallet'ünüzü USB aracılığıyla bilgisayara bağlayın ve Blockstream Uygulamasında seçin:



![image](assets/fr/22.webp)





- Blockstream App portföy bilgilerinizi içe aktarırken lütfen bekleyin:



![image](assets/fr/23.webp)



### 4.3. Bir hesap oluşturun





- Hardware Wallet'iniz Blockstream Uygulaması ile zaten kullanılmışsa, hesabınız içe aktarıldıktan sonra otomatik olarak Interface'da görünecektir. Aksi takdirde, "**Hesap Oluştur**" seçeneğine tıklayarak bir hesap oluşturun:



![image](assets/fr/24.webp)





- Klasik bir Bitcoin portföyü yapılandırmak için "**Standart**" seçeneğini seçin:



![image](assets/fr/25.webp)





- Hesabınız oluşturulduktan sonra ana Interface portföyünüze erişebilirsiniz:



![image](assets/fr/26.webp)





## 5. Zincir üstü Wallet'i bir Hardware Wallet ile kullanma



### 5.1. Bitcoin almak





- Ana portföy ekranından "**Aldık**" üzerine tıklayın:



![image](assets/fr/27.webp)





- Uygulama bir **boş alım Address** görüntüler. Her alım için yeni bir Address kullanmak gizliliğinizi artırır. Address'i kopyalamak için "**Address'i Kopyala**" üzerine tıklayın veya gönderenin görüntülenen QR kodunu taramasına izin verin:



![image](assets/fr/12.webp)



**Seçenekler** :




- (1) Portföyünüze bağlı yeni bir generate Address oluşturmak için oklara tıklayın.
- (2) Belirli bir tutar talep etmek için "**Daha fazla seçenek**" ve ardından "**Tutar iste**" üzerine tıklayın. QR güncellenecek ve Address, aşağıdaki gibi bir Bitcoin ödeme URI'si ile değiştirilecektir: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Önceki bir Address'yı tekrar kullanmak için, "**Daha fazla seçenek**" ve ardından "**Adres listesi**" üzerine tıklayın:



![image](assets/fr/14.webp)





- **Doğrulama**: Hataları veya saldırıları önlemek için paylaşılan Address'yi dikkatlice kontrol edin (örneğin, panoyu değiştiren kötü amaçlı yazılımlar).
- İşlem ağda yayınlandıktan sonra, Wallet'inizde görünecektir. İşlemin değiştirilemez olduğunu düşünmek için 1 ila 6 onay bekleyin.



![image](assets/fr/28.webp)



### 5.2. bitcoin göndermek





- Ana portföy ekranından "**Gönder**" seçeneğine tıklayın.



![image](assets/fr/29.webp)





- **Ayrıntıları girin**:
    - (1) Seçilen varlığın **Bitcoin** (onchain) olduğunu kontrol edin.
    - (2) Alıcının **Address numarasını** yapıştırarak veya web kameranızla bir QR kodu tarayarak girin.
    - (3) Gönderilecek **miktarı** belirtin (BTC, satoshis veya diğer birimler cinsinden).




![image](assets/fr/16.webp)





- **İşlem ücretlerini** seçin (isteğe bağlı) :
 - Tahmini onay süresiyle birlikte aciliyete göre önerilen seçeneklerden (hızlı, orta, yavaş) birini seçin.
 - Özelleştirilmiş ücretler için, vbyte başına satoshis sayısını manuel olarak ayarlayın. Bunlar ana ekranda gösterilir. Ayrıca bkz [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **UTXO'ların manuel seçimi** (isteğe bağlı): İşlemde kullanılacak belirli UTXO'ları seçmek için "**Manuel Coin seçimi**" üzerine tıklayın.



![image](assets/fr/18.webp)





- **Ön doğrulama**: Özet ekranında Address'ü, tutarı ve ücretleri kontrol edin, ardından "**İşlemi onayla**" seçeneğine tıklayın. Gerçekte, işlem, UTXO'ların (satoshis) borçlandırılacağı adreslerle ilişkili gizli anahtarlara sahip olan Hardware Wallet'ünüzle imzalayana kadar ağa bırakılmayacaktır.



![image](assets/fr/19.webp)





- Son kontrol ve imza**: Hardware Wallet** ekranınızda tüm işlem parametrelerinin doğru olduğundan emin olun ve ardından işlemi imzalayın. Bir Address hatası geri dönüşü olmayan fon kaybına neden olabilir.





- **Yayın**: Blockstream Uygulaması, imzalandıktan sonra işlemi otomatik olarak Bitcoin ağında yayınlar.



![image](assets/fr/20.webp)





- **Takip edin** :
 - İşlem, onaylanana kadar Wallet ana ekranında "beklemede" olarak görünür.
 - İşlem onaylanmadığı sürece, ücreti artırarak onayı hızlandırmak için **Replace-by-fee (RBF)** işlevi kullanılabilir (bkz. Ek).



![image](assets/fr/21.webp)



## Ekler



### A1. Diğer Blockstream eğitimleri





- Liquid Network'in Kullanılması :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- "Yalnızca İzle "de bir portföyü içe aktarın ve izleyin:



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Cep telefonlarında Blockstream Uygulamasını kullanma (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Replace-by-fee (RBF) Açıklaması





- **Tanım**: Replace-by-fee (RBF), göndericinin ücreti artırarak bir **zincir üzerinde** işlemin onaylanmasını hızlandırmasına olanak tanıyan Bitcoin ağının bir özelliğidir.
- **Sınırlar**:
    - RBF, Liquid veya Lightning işlemleri için kullanılamaz.
    - İlk işlem, Blockstream Uygulamasının otomatik olarak yaptığı RBF uyumlu olarak işaretlenmelidir.
- Daha fazla bilgi için [sözlüğümüze] (https://planb.network/resources/glossary/rbf-replacebyfee) bakınız.



### A3. En iyi uygulamalar





- **Kurtarma cümlenizi güvence altına alın** :
    - Hardware Wallet'ün Mnemonic ifadesini fiziksel bir ortamda (kağıt, metal) güvenli bir yerde saklayın.
    - Asla dijital olarak saklamayın (bulut, e-posta, ekran görüntüsü).
    - Öğretici : Mnemonic ifadenizi kaydedin:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Gizliliğinizi koruyun**:





    - generate her zincirleme alım için yeni bir Address.
    - İzlemeyi sınırlamak için **Tor** veya **SPV**'yi etkinleştirin.
    - Maksimum egemenlik için Electrum aracılığıyla kendi Bitcoin düğümünüze bağlanın.
- Her zaman gönderim adreslerini kontrol edin:





    - İmzalamadan önce Hardware Wallet ekranınızdaki Address'u kontrol edin.
    - Manuel hataları önlemek için kopyala/yapıştır veya QR kodu kullanın.
- **Maliyetleri optimize edin**:





    - Ücretleri aciliyete ve ağ tıkanıklığına göre ayarlayın (bkz. [Mempool.space](https://Mempool.space/)).
    - Zincir üzerinde güvenlik gerektirmeyen hızlı, düşük maliyetli işlemler için Liquid veya Lightning kullanın.
- **Yazılımı güncelleyin** :





    - Blockstream Uygulamanızı ve Hardware Wallet ürün yazılımınızı en son özellikler ve güvenlik yamaları ile güncel tutun.



### A4. Ek kaynaklar





- **Resmi bağlantılar**:
    - [Resmi web sitesi](https://blockstream.com/)
    - [Blockstream Uygulaması için Destek] (https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokümantasyon ve sohbet
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Blok Kaşifleri** :
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blok Akış Bilgisi](https://blockstream.info/Liquid)
    - Yıldırım : [1ML (Lightning Network)](https://1ml.com/)





- **Kurtarma ifadenizin güvenliğini sağlama:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Sözlük](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Sözlük](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb