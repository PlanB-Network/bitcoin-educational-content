---
name: Bisq 2
description: Bisq 2 kullanımı ve bitcoin alışverişi için eksiksiz kılavuz P2P
---
![cover](assets/cover.webp)


## Giriş


KYC içermeyen eşler arası (P2P) borsalar, kullanıcıların gizliliğini ve finansal özerkliğini korumak için çok önemlidir. Kimlik doğrulamasına ihtiyaç duymadan bireyler arasında doğrudan işlem yapılmasını sağlarlar ki bu da gizliliğe önem verenler için çok önemlidir. Teorik kavramları daha derinlemesine anlamak için BTC204 kursuna bir göz atın:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Bisq 2 nedir?


Bisq 2, 2024 yılında piyasaya sürülen popüler merkezi olmayan Bisq Exchange'nin yeni sürümüdür. Selefinden farklı olarak Bisq 2, kullanıcılara daha fazla esneklik sunarak birden fazla Exchange protokolünü destekleyecek şekilde geliştirilmiştir.


**Anahtar yeni özellikler:**




- Çoklu gizlilik ağları için destek (Tor, I2P)
- Daha fazla gizlilik için çoklu kimlikler
- Ticaret botları için REST API
- Birden fazla Wallet tipi için destek
- BSQ'da zorunlu depozito ile rol sistemi


Bu kılavuz sadece şu anda mevcut olan tek protokol olan "Bisq Easy" üzerine odaklanmaktadır. Bisq Easy, özellikle yeni Bitcoin kullanıcıları için tasarlanmıştır. Bu protokol, kullanıcıların merkezi olmayan eşler arası bir platformda fiat para birimleri karşılığında Bitcoin alıp satmalarını sağlar. İşlemler 600 USD eşdeğeri ile sınırlıdır (minimum 6 USD ile) ve Exchange güvenliği BTC satıcılarının itibarına dayanır. Bisq Easy'nin işlem ücreti veya teminat yatırma zorunluluğu yoktur. Bisq Easy'nin 600 USD (veya eşdeğeri) altındaki nakit alışverişleri için Bisq 1'in yerini alması bekleniyor.


**Ana özellikler:**




- Platformlar arası masaüstü uygulaması
- Çeşitli Exchange protokolleri mevcuttur
- Merkezi olmayan P2P ağı
- Gizliliğe odaklanma (KYC yok, Tor kullanımı)
- Velayetsiz (fonlarınızın kontrolü sizde kalır)
- Açık kaynak (AGPL)


### Bisq 1 ile farklılıklar


**Alıcılar için:**




- Güvenlik depozitosu gerekmez
- İşlem ücreti yok
- Mining ücreti yok
- Satıcı itibarına dayalı güvenlik
- Alt işlem limitleri (600 USD'ye eşdeğer)


**Satıcılar için:**




- Güvenlik depozitosu gerekmez
- Bir itibar oluşturmak
- BSQ yakma veya BSQ bağları oluşturma olasılığı
- Potansiyel olarak daha yüksek satış primi (piyasanın %10-15 üzerinde)


**Önemli not:** Bisq Multisig protokolü Bisq 2'de uygulandıktan sonra, Bisq'in eski sürümü aşamalı olarak kaldırılabilir. Ancak Bisq 1, Bisq CAD ve BSQ-BTC borsaları için bir yönetim aracı olarak kullanılmaya devam edecektir.


### Exchange süreci




- Teklifi oluşturan kişi Exchange'in şartlarını tanımlar
- Tüccarlar şartlar (ödeme yöntemi ve fiyat) üzerinde anlaştıktan sonra Exchange başlar
- Satıcı banka bilgilerini alıcıya gönderir ve alıcı da Bitcoin Address bilgilerini satıcıya gönderir
- Alıcı ödemeyi nakit olarak yapar ve satıcıya bildirir
- Ödeme alındıktan sonra, satıcı bitcoinleri alıcının Address'ine gönderir
- Alıcı bitcoinleri aldığında Exchange tamamlanmış olur


### Önemli kurallar




- Ödeme bilgilerini değiştirmeden önce, Exchange gerekçe gösterilmeksizin iptal edilebilir
- Ayrıntılar değiş tokuş edildikten sonra, yükümlülüklerin yerine getirilmemesi sürgünle sonuçlanabilir
- Banka havaleleri için, **ödeme nedeninde asla "Bisq" veya "Bitcoin"** terimlerini kullanmayın (bu, fonların dondurulmasına veya hatta alıcının veya ödeyenin banka hesabının bloke edilmesine neden olabilir)
- Yatırımcılar süreci takip etmek için günde en az bir kez oturum açmalıdır
- Bir sorun olması halinde, tüccarlar bir arabulucunun hizmetlerine başvurabilir


## Kurulum ve yapılandırma


### 1. Bisq 2'yi İndirin ve Doğrulayın


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Bisq.network](https://bisq.network/downloads/) adresine gidin
- İşletim sisteminize uygun Bisq 2 sürümünü indirin (sayfayı aşağı kaydırın)
- İndirilen dosyanın gerçekliğini doğrulayın (şiddetle tavsiye edilir). İmza doğrulama ile ilgili ayrıntılı bir kılavuz için aşağıdaki eğitime bakın:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Sisteminize göre kurulum


Lütfen işletim sisteminize uygun kurulum adımlarını izleyin. Kurulum sırasında herhangi bir zorlukla karşılaşırsanız, [resmi Bisq wiki] (https://bisq.wiki/Downloading_and_installing) adresindeki ayrıntılı kılavuza başvurabilirsiniz.


### 3. İlk başlangıç




- Bisq 2'yi başlatın ve kullanım koşullarını kabul edin


![Conditions d'utilisation](assets/fr/01.webp)




- Bir isim ve avatar seçerek yeni bir profil oluşturun


![Création du profil](assets/fr/02.webp)




- Daha sonra uygulamanın ana kontrol paneline yönlendirilirsiniz; burada ilk bitcoinlerinizi satın almak veya satmak için Bisq Easy'yi başlatabilirsiniz


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Ödeme yöntemlerini ayarlama




- Ana menüden ödeme hesapları bölümüne erişin


![Liste des comptes de paiement](assets/fr/04.webp)




- Gerekli bilgileri doldurarak yeni bir ödeme yöntemi ekleyin


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Ödeme yöntemlerini önceden yapılandırmak isteğe bağlıdır, ancak işlem yaparken zaman kazanmak için önerilir. Ödeme yöntemlerinizi doğrudan bir işlem sırasında Exchange ortağınızla iletişime geçerek de yapılandırabilirsiniz.


### 5. Hesap güvenliği


**Veri yedekleme:**


Bisq 1'in aksine, Bisq 2 şu anda bir Bitcoin Wallet'i entegre etmemektedir: bu nedenle işlemler kendi harici cüzdanlarınız aracılığıyla gerçekleştirilir. Bununla birlikte, Bisq 2 veri klasörünüzü düzenli olarak yedeklemenizi öneririz. Veri klasörünüzü bulmak için [resmi Bisq wiki] (https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory) adresine bakın.


**Kimlik yönetimi:**


Bisq 2 birden fazla kimlik oluşturmanıza olanak tanır. Her kimlik farklı işlem türleri için kullanılabilir. Kimlikleriniz veri klasöründe saklanır.


## Bitcoin Alımı ve Satımı


### Bitcoin nasıl satın alınır


**Seçenek 1: Mevcut bir tekliften yararlanın**




- Ana ekranda, "Bisq Easy", "Başlarken" sekmesini seçin, ardından "İşlem sihirbazını başlat "a tıklayın


![Lancer trade wizard](assets/fr/06.webp)




- "Bitcoin Satın Al "ı seçin ve para biriminizi seçin


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Tercih ettiğiniz ödeme yöntemlerini ayarlayın (SEPA, Revolut, vb.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- Bu noktada, ya önceki kriterlerinize karşılık gelen tekliflerin bir listesine sahip olursunuz ya da "Offerbook "a gitmeniz gerekir


![Liste des offres](assets/fr/10.webp)




- İkinci durumda, Interface'ün sağ üst köşesindeki düğmeleri kullanarak teklifleri görüntüleyebilir ve filtreleyebilirsiniz


![Filtres des offres](assets/fr/11.webp)




- Teklifinizi seçtikten sonra tek yapmanız gereken ödeme yönteminizi seçmek ve ardından işlem özetini doğrulamaktır


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**2. Seçenek: Kendi teklifinizi oluşturun**




- "Bisq Easy" ve ardından "Offerbook "u seçin
- İşlem çiftinizi seçin (örn. BTC/EUR)
- "Teklif oluştur "a tıklayın
- Teklif oluşturma sihirbazını takip edin: Tutarı tanımlayın (sabit veya aralık)


![Configuration du montant](assets/fr/20.webp)




- Kabul edilen ödeme yöntemlerini seçin


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Özeti kontrol edin ve teklifi yayınlayın


![Récapitulatif et publication](assets/fr/22.webp)


Exchange başlatıldıktan sonra :




- Bitcoin Address veya Lightning Invoice'nizi satıcıya gönderin


![Envoi adresse Bitcoin](assets/fr/15.webp)




- Satıcının banka bilgilerini alın


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Ödemeyi yapın ("Bisq" veya "Bitcoin "den bahsetmeden)
- Ödemenizi satıcıya bildirin


![Notification paiement](assets/fr/18.webp)




- Bitcoinlerin gelmesini bekleyin


![Attente réception](assets/fr/19.webp)


### Bitcoin nasıl satılır?


Bisq 2'deki satış süreci, satın alma sürecine benzer bir mantık izler, aynı ana adımlar ancak ters sırada gerçekleşir. Kendi satış teklifinizi oluşturabilir veya mevcut bir satın alma teklifine yanıt verebilirsiniz. İşte süreçteki çeşitli seçeneklerin ve aşamaların bir dökümü:


**1. Seçenek: Bir satış teklifi oluşturun**




- "Bisq Easy" ve ardından "Offerbook "u seçin
- "Teklif oluştur "a tıklayın ve "Bitcoin Sat "ı seçin
- Teklifinizi yapılandırın :
 - Para birimi seçin (EUR, USD, vb.)
 - Kabul edilen ödeme yöntemlerini seçin
 - Tutarı ayarlayın (6 ile 600 USD eşdeğeri arasında)
 - Fiyatınızı belirleyin (sabit veya pazarın %'si)
- Ayrıntıları kontrol edin ve teklifi yayınlayın


**2. Seçenek: Mevcut bir teklifi kabul edin**




- "Offerbook" sekmesinde tekliflere göz atın
- Para birimi ve ödeme yöntemine göre filtreleme
- Size uygun bir teklif seçin
- Ayrıntıları kontrol edin ve teklifi kabul edin


**Satış süreci:**


Exchange başlatıldıktan sonra :




   - Banka bilgilerinizi alıcıya gönderin
   - Alıcının Bitcoin Address'ini bekleyin
   - Address'ün geçerli olup olmadığını kontrol edin


Ödeme bildiriminden sonra :




   - Hesabınıza ödeme yapılıp yapılmadığını kontrol edin
   - Tutar ve ayrıntıların eşleştiğini onaylayın
   - Sağlanan Address'e bitcoin gönderin
   - İşlemi tamamlandı olarak işaretleyin


Sonuçlandırma :




   - Alıcıdan onay bekleyin
   - İşlem hakkında geri bildirim bırakın
   - Gelecekteki satışlar için itibarınızı oluşturun


**Önemli not:** Bir satıcı olarak, ters ibraz riski konusunda özellikle dikkatli olmanız gerekir. Güvenli ödeme yöntemlerini tercih edin ve bitcoin göndermeden önce her zaman ödemenin alındığını kontrol edin.


## İyi Uygulamalar ve Güvenlik


### Güvenlik İpuçları


**Alıcılar için:**




- Küçük miktarlarla başlayın
- Satıcıların itibarını kontrol edin (minimum 30.000 puan)
- Yalnızca önerilen ödeme yöntemlerini kullanın
- Ödeme göndermeden önce satıcının aktif olup olmadığını kontrol edin
- Yalnızca Exchange sohbetinde verilen banka bilgilerini kullanın
- Bisq 2 platformu dışında asla iletişim kurmayın
- Ödeme kanıtını saklayın
- Asla hassas bilgiler göndermeyin


**Satıcılar için:**




- Yeni hesaplar konusunda dikkatli olun
- Ters ibrazlara duyarlı ödeme yöntemlerinden kaçının (PayPal, Venmo)
- Hesap bilgilerinin alıcıya uygun olup olmadığını kontrol edin
- İletişimi sohbet ile sınırlayın Bisq 2
- Şüphe durumunda bir arabuluculuk açın


### İtibar oluşturma (satış elemanları için)


Bir satıcı olarak Bisq'teki itibarınızı artırmak için düzenli işlemler gerçekleştirin ve alıcılarla profesyonel iletişim kurun. Olumlu bir deneyim sağlamak için alıcı taleplerine hızlı bir şekilde yanıt verin. Ayrıca platforma Commitment'nızı göstermek için bir BSQ bağı oluşturabilirsiniz. Bu eylemler güven oluşturacak ve daha fazla alıcı çekecektir.


### Uyuşmazlık Çözümü




- Sohbet yoluyla muhatabınızla iletişime geçin
- Gerekirse bir ihtilaf açın
- İstenen tüm kanıtları sağlayın
- Arabulucunun talimatlarını izleyin


### Gizlilik Politikası :




- Kayıt veya merkezi kimlik doğrulaması gerekmez
- Tüm bağlantılar Tor ağı üzerinden gerçekleşir (ve yakında I2P)
- Veri depolamak için merkezi sunucu yok
- İşlem detayları sadece ilgili taraflarca okunabilir


### Sansüre karşı koruma :




- Tamamen dağıtılmış P2P ağı
- Sansüre direnmek için Tor ağını (ve yakında I2P'yi) kullanmak
- Merkezi bir tüzel kişiliği olmayan bir DAO tarafından yönetilen açık kaynak projesi


## Avantajlar ve dezavantajlar


### Bisq 2'nin Faydaları




- Maksimum gizlilik**: KYC yok, Tor kullanımı
- Merkezsizleştirme**: Merkezi sunucu yok
- Güvenlik**: Açık kaynak, gözetim dışı kod
- Sezgisel Interface**: Bisq 1'den daha basit
- Esneklik**: Çoklu Exchange protokolleri


### Bisq 2 dezavantajları




- Sınırlı likidite** (şimdilik) :
 - Başlangıç aşamasında yeni protokol
 - Birkaç satış teklifi mevcut
 - Alıcı bulmak için potansiyel olarak uzun bekleme süreleri
- İşlem limitleri**: İşlem başına maksimum 600 USD (Bisq easy ile)
- Sadece masaüstü**: Mobil uygulama yok


## Gelecek Protokolleri


Bisq Easy şu anda mevcut olan tek protokol olmasına rağmen, Bisq 2 için başka protokoller de geliştirilmektedir:




- Bisq Lightning**: Exchange üzerinde çok partili hesaplama kriptografisi kullanan bir emanet sistemine dayalı Lightning Network protokolü.
- Bisq MuSig**: Ana protokolün Bisq 1'den Bisq 2'ye, 2'ye 2 Multisig kullanılarak, teminat depozitoları ile taşınması.
- BSQ Takasları**: BSQ ve BTC arasında anlık atomik takaslar.
- Liquid Swapları**: Atomik takaslar yoluyla Exchange üzerindeki varlıkların Liquid Network (USDT, BTC-L).
- Monero Takasları**: Bitcoin ve Monero arasında atomik takaslar.
- Liquid MuSig**: Multisig protokolünün daha düşük maliyet ve daha fazla gizlilik için L-BTC kullanan sürümü.
- Denizaltı Takasları**: Lightning Network ve Bitcoin On-Chain üzerindeki Bitcoin arasındaki değişimler.
- Stablecoin Takasları**: Bitcoin ve USD sabit coinleri arasında atomik değişimler.
- Multisig Opsiyonları**: Bir On-Chain Multisig işleminde BTC blokajlı P2P satım ve alım opsiyonlarının oluşturulması.
- Multisig Açık Sözleşmeler**: Arbitrajlı 2'ye 3 Multisig sistemi kullanarak özelleştirilmiş koşullu sözleşmelerin oluşturulmasını sağlar.


Bu protokoller şu anda geliştirilme aşamasındadır ve kullanıcılara özel ihtiyaçlarına göre daha fazla esneklik sunarak Bisq 2'ye aşamalı olarak entegre edilecektir.


## Yararlı Kaynaklar




- Resmi web sitesi: [bisq.network](https://bisq.network)
- Dokümantasyon: [Bisq Wiki](https://bisq.wiki)
- Destek: [Forum Bisq](https://bisq.community)
- Kaynak kodu : [GitHub](https://github.com/bisq-network)