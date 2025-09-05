---
name: Şeftali
description: Peach kullanımı ve bitcoin alışverişi için eksiksiz kılavuz P2P
---
![cover](assets/cover.webp)


![peach](https://youtu.be/ziwhv9KqVkM)


## Giriş


KYC içermeyen eşler arası (P2P) borsalar, kullanıcıların gizliliğini ve finansal özerkliğini korumak için çok önemlidir. Kimlik doğrulamasına ihtiyaç duymadan bireyler arasında doğrudan işlem yapılmasını sağlarlar ki bu da gizliliğe önem verenler için çok önemlidir. Teorik kavramları daha derinlemesine anlamak için BTC204 kursuna bir göz atın:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Şeftali nedir?


Peach, kullanıcıların KYC olmadan bitcoin alıp satmalarına olanak tanıyan bir P2P Exchange platformudur. Sezgisel bir Interface ve gelişmiş güvenlik özellikleri sunar. Bisq, HodlHodl ve Robosat gibi diğer çözümlerle karşılaştırıldığında Peach, kullanım kolaylığı ve düşük ücretleriyle öne çıkmaktadır.


### 2. Gizlilik ve Veri Toplama


**Peach hangi bilgileri topluyor?


Peach, kullanıcıları hakkında mutlak minimum veriyi saklamaya çalışmaktadır. İşte sunucularında depolanan verilere genel bir bakış:




- Benzersiz uygulama tanımlayıcınızın (AdID) bir Hash'i
- Ödeme verilerinizin bir Hash'sı
- Şifrelenmiş konuşmalarınız
- Anonim kullanıcıların işlem limitini aşmamasını sağlamak için işlem verileri (kullanılan ödeme yöntemleri, alım ve satım tutarları)
- Emanet hesabından göndermek ve almak için kullanılan adresler
- Kullanım verileri (Firebase & Google Analytics), yalnızca sizin izninizle


Bir hatırlatma olarak, Hash, şifrelemeye benzer şekilde tanınmaz hale getirilmiş veridir. Aynı veri her zaman aynı Hash'yi üretecektir, bu da orijinal veriyi bilmeden kopyaları tespit etmeyi mümkün kılar.


*Hashing hakkında daha fazla bilgi için bu kursu takip edebilirsiniz:*


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Ödeme bilgilerimi kim görebilir?




- Ödeme bilgilerinizi yalnızca karşı taraf görebilir
- Veriler Peach sunucuları üzerinden iletilir ancak uçtan uca tamamen şifrelenir
- Bir anlaşmazlık durumunda, ödeme bilgileriniz ve görüşme geçmişiniz atanan Peach arabulucusu tarafından görülebilecektir


## Kurulum ve yapılandırma


### 1. Peach uygulamasını yükleyin


![Installation de Peach](assets/fr/01.webp)




- Uygulamayı [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/) adresinden indirin.
- Cihazınızdaki kurulum talimatlarını izleyin.
- Kurulum sırasında, Peach uygulamasını geliştirmek için belirli verileri paylaşmak isteyip istemediğinizi seçmeniz istenecektir (resim 1)
- Bir sonraki ekranda (resim 2) iki seçeneğiniz vardır:
 - Yeni bir kullanıcıysanız, yeni bir profil oluşturmak için "Yeni kullanıcı" üzerine tıklayın
 - Zaten bir hesabınız varsa, mevcut profilinizi geri yüklemek için "Geri Yükle" seçeneğini kullanın
- Eğer bir yönlendirme kodunuz varsa, buraya girebilirsiniz.
- Mevcut bir hesabı geri yüklemek için (resim 3), ihtiyacınız olacak :
 - Yedekleme dosyanız
 - Bu dosyanın şifresini çözmek için şifre


### 2. Ana Ekranlara Genel Bakış


Peach uygulaması, alt navigasyon çubuğundan erişilebilen dört ana ekran etrafında düzenlenmiştir:


![Navigation dans l'application](assets/fr/02.webp)




- Ana Sayfa** : Bitcoin alım ve satımı için ana ekran. Burası yeni işlemler oluşturabileceğiniz ve mevcut tekliflere erişebileceğiniz yerdir.
- Wallet**: Entegre Bitcoin Wallet'unuzu kullanmanıza olanak tanır:
 - Bakiyenizi kontrol edin
 - Bitcoin alma
 - Bitcoin gönder
 - İşlem geçmişinizi görüntüleyin
- Ticaret** : Bulabileceğiniz ticaret yönetim merkeziniz:
 - Mevcut işlemleriniz
 - Değişimlerinizin eksiksiz bir geçmişi
 - Her bir işlemin durumu
- Ayarlar** : Için hesap yapılandırma merkeziniz:
 - Ödeme yöntemlerinizi yönetin
 - Yedeklemelerinizi yapılandırın
 - Tercihlerinizi özelleştirin
 - Yardım ve desteğe erişim


### 3. Ödeme yöntemlerinizi yapılandırın


![Accès aux paramètres de paiement](assets/fr/03.webp)


Ayarlar sekmesi üzerinden ödeme yöntemlerine erişin (resim 8)


**Online ödemeler


![Configuration des paiements en ligne](assets/fr/04.webp)




- Yeni bir ödeme yöntemi eklemek için butona tıklayın
- Para biriminizi seçin
- Tercih ettiğiniz ödeme yöntemini seçin


*Mevcut ödeme yöntemi türleri:*


***Banka transferleri mevcuttur: ***




- SEPA (standart veya anında)
- SEPA banka bilgilerinizi girin


***Online cüzdanlar kabul edilir :***




- Ülkenize bağlı olarak çeşitli seçenekler mevcuttur (Revolut, Paypal, Wise, Strike, vb.)
- Giriş bilgilerinizi eklemek için talimatları izleyin


***Kullanılabilecek hediye kartı :***




- Amazon
- Kartın verildiği ülkeyi ve diğer gerekli bilgileri girin


***Ulusal ödeme seçenekleri:***


Ülkeye özgü ödeme sistemleri :




- Satispay (İtalya)
- MB Way (Portekiz)
- Bizum (İspanya)
- Hızlı Ödemeler (Birleşik Krallık)


***Şahsen ödemeler:***


![Configuration des paiements en personne](assets/fr/05.webp)




- "Buluşma" yı seçin
- Ardından listeden buluşmanızı seçin


### Kullanım talimatları




- Aynı anda birden fazla ödeme yöntemi ayarlayabilirsiniz
- Ne kadar çok yöntem eklerseniz, o kadar geniş bir teklif yelpazesine erişebilirsiniz
- Lütfen kayıt olmadan önce bilgilerinizin doğru olup olmadığını kontrol edin
- Ödeme yöntemlerinizi istediğiniz zaman değiştirebilir veya silebilirsiniz


**Güvenlik notu**: Ödeme bilgileriniz şifrelenir ve yalnızca bir işlem sırasında Exchange ortağınızla paylaşılır.


### 4. Wallet'nizi nasıl emniyete alırsınız


**Peach hesabınızı anlama


Peach hesabı geleneksel bir kullanıcı adı ve şifre hesabı değildir. Telefonunuzda yerel olarak depolanan bir dosyadır, yani Peach'in verilerinizi depolaması veya kimliğinizi bilmesi gerekmez: kontrol sizdedir. Bu dosya, Bitcoin Wallet anahtarlarınızdan ödeme bilgilerinize kadar tüm verilerinizi içerir.


Bu yaklaşım daha fazla gizliliği garanti eder, ancak aynı zamanda daha fazla sorumluluk anlamına gelir. Telefonunuzu yedeklemeden kaybetmek, Peach hesabınıza ve fonlarınıza erişimi kaybetmek anlamına gelir. Bu yüzden bu dosyayı yedeklemek ve güçlü bir parola ile korumak çok önemlidir.


**Yedeklerinizi oluşturun**


![Accéder aux sauvegardes](assets/fr/13.webp)




- Ana ekranın sağ alt tarafındaki sekmeden ayarlara erişin
- Ayarlar menüsünden "yedeklemeler" seçeneğini seçin


![Processus de sauvegarde](assets/fr/06.webp)


İki tür yedekleme mevcuttur:


**Hesap dosyasını kaydet (resim 14)**




- "Yeni yedek oluştur" üzerine tıklayın
- Yedekleme dosyanızı şifrelemek için güçlü bir parola oluşturun
- Bu dosyayı güvenli bir yerde saklayın


Dosya yedekleme, . dahil olmak üzere tüm Peach hesabınızı geri yükler:




- Wallet'iniz
- Ödeme yöntemleriniz
- Konuşma geçmişi
- Ödeme verileri
- Karşı taraf detayları ile işlem geçmişi


**Kurtarma ifadesini kaydetme (resim 15)**




- Kurtarma ifadenizi görüntülemek için talimatları izleyin
- Kelimeleri doğru sırayla dikkatlice yazın
- Bu yedeği güvenli bir yerde, ideal olarak hesap dosyasından farklı bir yerde saklayın


Kurtarma ifadesi yalnızca :




- Hesabınıza erişim
- Bitcoin fonlarınız


Kaybedeceksin:




- Konuşma geçmişi
- Ödeme verileri
- İşlem geçmişinde karşı taraf bilgileri


Optimum güvenlik için her iki yedekleme türünü de gerçekleştirmenizi öneririz.


## Bitcoin Alımı ve Satımı


### 1. Bitcoin nasıl satın alınır


![Création et vue des offres](assets/fr/07.webp)




- Ana ekranda "Satın Al" düğmesine tıklayın (resim 16)
- Satın alma işleminizi tercihlerinize göre yapılandırın (resim 17)
- Mevcut tekliflerin listesine göz atın (resim 18)


![Sélection et confirmation d'achat](assets/fr/08.webp)




- Sizin için doğru olan teklifi seçin (resim 19)
- Kararlaştırılan yöntemle ödeme yapın
- Uygulamada ödemeyi onaylayın ve işlemi değerlendirin (resim 20)


![Réception des bitcoins](assets/fr/09.webp)




- İşleminizin durumunu takip edin
- Bitcoinlerin alındığına dair onayı kontrol edin
- Fonlar Peach Wallet'nizde mevcut olacaktır


### 2. Bitcoin nasıl satılır


![Création d'un ordre de vente](assets/fr/10.webp)




- Satış teklifinizi yapılandırın (resim 24)
- Bitcoinleri sağlanan Address'e göndererek işlemi finanse edin (resim 25)
- İşlem onayı için bekleyin (resim 26)
- Teklifiniz artık alıcılar tarafından görülebilir (resim 27)


![Attente du paiement](assets/fr/11.webp)




- Teklifinizin durumunu izleyin
- Alıcıdan ödeme onayı bekleyin
- İşlem ayrıntılarını kontrol edin


![Finalisation de la vente](assets/fr/12.webp)




- Ödeme durumunu kontrol edin
- Ödemenin alındığını teyit edin
- İşlemi değerlendirin
- Bitcoinler otomatik olarak alıcıya verilir


**Başarılı bir işlem için ipuçları**




- Karşı tarafınızdan gelen mesajlara hızlı yanıt verin
- Ödeme ayrıntılarını dikkatlice kontrol edin
- Bir sorununuz varsa arabuluculuk hizmetini kullanmaktan çekinmeyin


**Güvenlik notu**: Hesabınıza geçtiğini doğrulamadan asla bir ödemenin alındığını onaylamayın.


## Avantajlar ve dezavantajlar


### Şeftali faydaları




- KYC gerekmez**: Kullanıcı gizliliğini korur.
- Banka bilgilerine erişim yok**: Peach'in banka bilgilerinize veya kimliğinize erişimi yoktur.
- Sezgisel Interface**: Orta düzey kullanıcılar için kullanımı kolay.
- Açık Kaynak** : Kaynak kodu herkese açıktır ve topluluk tarafından doğrulanabilir.


### Şeftali dezavantajları




- Sınırlı likidite**: Daha yerleşik platformlara göre daha az işlem hacmi.
- Düzenleyici risk** : Uygulama bir İsviçre şirketi tarafından yönetilmektedir. Bu nedenle, uygulamayı geliştirebilecek ve potansiyel olarak sansürleyebilecek İsviçre düzenlemelerine tabidir.


## Yararlı kaynaklar




- Fransızca açıklayıcı video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Hızlı başlangıç kılavuzu: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)