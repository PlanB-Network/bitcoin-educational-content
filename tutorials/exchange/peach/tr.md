---
name: Peach
description: Peach'i kullanmak ve P2P'de bitcoin ticareti yapmak için eksiksiz kılavuz
---

![cover](assets/cover.webp)





## Giriş



KYC içermeyen eşler arası (P2P) borsalar, kullanıcıların gizliliğini ve finansal özerkliğini korumak için çok önemlidir. Kimlik doğrulamasına ihtiyaç duymadan bireyler arasında doğrudan işlem yapılmasını sağlarlar ki bu da gizliliğe önem verenler için çok önemlidir. Teorik kavramları daha derinlemesine anlamak için BTC204 kursuna bakınız:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Peach nedir?



Peach, kullanıcıların KYC olmadan bitcoin alıp satmalarına olanak tanıyan bir P2P değişim platformudur. Sezgisel bir arayüz ve gelişmiş güvenlik özellikleri sunar. Bisq, HodlHodl ve Robosat gibi diğer çözümlerle karşılaştırıldığında, Peach kullanım kolaylığı ile öne çıkmaktadır.


Bir multisignature emanet sistemi (2-2), işlemler sırasında fonların güvenliğini garanti eder. Peach çeşitli ödeme yöntemlerini destekler ve yatırımcılara eylemlerinde rehberlik etmek için bir itibar sistemine sahiptir. P2P platformlarında her zaman olduğu gibi, diğer tüccarlar nezdinde güvenilirliği korumak için iyi bir itibara sahip olmak önemlidir.



### 2. Gizlilik ve toplanan veriler



**Peach hangi bilgileri toplar?



Peach, kullanıcıları hakkında mutlak minimum veriyi saklamaya çalışmaktadır. Burada sunucularımızda depolanan verilere genel bir bakış yer almaktadır:





- Benzersiz uygulama tanımlayıcınızın (AdID) bir hash'ü
- Ödeme verilerinizin bir hash'i
- Şifrelenmiş konuşmalarınız
- Anonim kullanıcıların işlem limitini aşmamasını sağlamak için işlem verileri (kullanılan ödeme yöntemleri, alım ve satım tutarları)
- Emanet hesabından göndermek ve almak için kullanılan Address'lar
- Kullanım verileri (Firebase & Google Analytics), yalnızca sizin izninizle



Bir hatırlatma olarak, hash şifrelemeye benzer şekilde tanınmaz hale getirilmiş veridir. Aynı veri her zaman aynı hash'yi üretecektir, bu da orijinal veriyi bilmeden kopyaları tespit etmeyi mümkün kılar.



*hashing'in daha ayrıntılı bir açıklaması için bu kursa katılın:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Ödeme bilgilerimi kim görebilir?





- Ödeme bilgilerinizi yalnızca karşı taraf görebilir
- Veriler Peach sunucuları üzerinden iletilir, ancak uçtan uca tamamen şifrelenir
- Bir anlaşmazlık durumunda, ödeme bilgileriniz ve görüşme geçmişiniz atanmış Peach arabulucusu tarafından görülebilecektir



## Kurulum ve yapılandırma



### 1. Peach uygulamasını yükleyin



![Installation de Peach](assets/fr/01.webp)





- Uygulamayı [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/) adresinden indirin. IOS'ta öncelikle [testflight](https://apps.apple.com/us/app/testflight/id899247664) uygulamasını yüklemeniz gerekecektir.
- Cihazınızdaki kurulum talimatlarını izleyin.
- Kurulum sırasında, Peach uygulamasını geliştirmek için belirli verileri paylaşmak isteyip istemediğinizi seçmeniz istenecektir. (resim 1)
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





- Ana Sayfa (4)** : Satın almayı veya satmayı seçebileceğiniz, yeni işlemler oluşturabileceğiniz ve mevcut tekliflere erişebileceğiniz ana ekran:
 - aşağıdaki iki düğme ile teklif oluşturun (satın al / sat oluştur)
 - aşağıdaki iki düğmeyi ("Satın Al"/"Sat") kullanarak diğer kullanıcılar tarafından oluşturulan mevcut tekliflerden yararlanın.





- Wallet (5)** : Entegre bitcoin wallet'niz şunları yapmanızı sağlar:
 - Bakiyenizi kontrol edin
 - Bitcoin alma
 - Envoyer bitcoins (coin kontrolü ile)
 - İşlem geçmişinizi görüntüleyin
 - Satışlarınızın finansmanı





- İşlemler (6)**: mevcut ve geçmiş sözleşmeleriniz, üç sekme altında:
 - Devam eden alımlar
 - Devam eden satışlar
 - Borsalarınızın geçmişi





- Ayarlar (7)** : Için yapılandırma merkezi
 - Profilinizi görüntüleyin (itibar, rozetler, limitler, vb.)
 - Güvenliği yönetme (yedekleme, pin)
 - Ödeme yöntemlerinizi yönetin
 - İletişim desteği
 - Dili değiştir
 - vs.



### 3. Ödeme yöntemlerinizi yapılandırın



![Accès aux paramètres de paiement](assets/fr/03.webp)



Ödeme yöntemlerinizi ayarlardan yönetebilirsiniz (resim 8)



Peach çevrimiçi ödemeler ve yüz yüze ödemeler (yalnızca kayıtlı buluşmalarda) sunmaktadır.



**Online ödemeler



**Önemli:**


gW-30, kullanıcıları korumak için fon kaynağının ilan edilenle eşleşmesini gerektirir. Kendi güvenlikleri için durumun böyle olduğundan emin olmak yatırımcıların sorumluluğundadır.



![Configuration des paiements en ligne](assets/fr/04.webp)



Bir yöntem eklemek için :




- "Çevrimiçi" sekmesinde "para birimi/yöntem ekle" seçeneğine tıklayın
- Para biriminizi seçin
- Tercih ettiğiniz ödeme yöntemini seçin



*Mevcut ödeme yöntemi türleri:*



***Banka havaleleri için: ***




- SEPA (standart veya anında)
- SEPA banka bilgilerinizi girin.



***Online wallet'ler kabul edildi :***




- Ülkenize bağlı olarak çeşitli seçenekler mevcuttur (Revolut, Paypal, Wise, Strike, vb.)
- Giriş bilgilerinizi eklemek için talimatları izleyin



*kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:*** kullanılabilir hediye kartı:***




- Amazon, Steam, vb.
- Kartın verildiği ülkeyi ve diğer gerekli bilgileri girin



***Ulusal ödeme seçenekleri:***


Ülkeye özgü ödeme sistemleri :




- Satispay (İtalya)
- MB Way (Portekiz)
- Bizum (İspanya)
- Hızlı Ödemeler (Birleşik Krallık)
- vs.



***Yüz yüze ödemeler için: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- "Meetup "ı seçin (resim 12)
- Ardından listeden buluşmanızı seçin (resim 13)



### Kullanım talimatları





- Birkaç ödeme yöntemi ekleyebilirsiniz
- Ne kadar çok yöntem eklerseniz, o kadar geniş bir teklif yelpazesine erişebilirsiniz
- Kaydolmadan önce bilgilerinizin doğruluğunu kontrol edin
- Ödeme yöntemlerinizi istediğiniz zaman değiştirebilir veya silebilirsiniz



**Güvenlik notu**: Ödeme bilgileriniz şifrelenir ve bir Peach arabulucusunun da erişebileceği bir anlaşmazlık durumu dışında, yalnızca bir işlem sırasında borsa ortağınızla paylaşılır.



### 4. Portföyünüzü nasıl güvence altına alırsınız?



**Peach hesabınızı anlama



Bir Peach hesabının kullanıcı adı ve şifresi yoktur. Telefonunuzda yerel olarak depolanan bir dosyadır, yani Peach'ün verilerinizi depolaması veya kimliğinizi bilmesi gerekmez: kontrol sizdedir. Bu dosya tüm verilerinizi içerir: 12 bitcoin kurtarma kelimesi, PGP anahtarları, ödeme ayrıntıları vb. Bu yüzden bu dosyayı kaydetmek ve __sağlam__ bir parola ile korumak çok önemlidir.



Bu yaklaşım bir dereceye kadar gizliliği garanti eder ve veri ve yedekleme yönetimi sorumluluğunu kullanıcının ellerine bırakır. Telefonunuzu yedeklemeden kaybetmeniz, Peach hesabınıza ve fonlarınıza erişiminizi kaybetmeniz anlamına gelir.



**Yedeklerinizi oluşturun**






- Ana ekranın sağ alt tarafındaki sekmeden ayarlara erişin
- Ayarlar menüsünden "yedeklemeler" seçeneğini seçin



![Processus de sauvegarde](assets/fr/06.webp)



İki tür yedekleme mevcuttur:



**Hesap dosyasını kaydet (resim 14)**




- "Yeni yedek oluştur" üzerine tıklayın
- Yedekleme dosyanızı şifrelemek için **güçlü** bir parola oluşturun
- Bu dosyayı, telefonun kaybolması durumunda yedekliliğini sağlayacak bir konuma gönderin.



Dosya yedeklemesi, . dahil olmak üzere tüm Peach hesabınızı geri yükler:




- Portföyünüz
- Ödeme yöntemleriniz
- Ödeme verileri
- Karşı tarafların ve onlarla yapılan görüşmelerin ayrıntılarını içeren işlem geçmişi



**Kurtarma ifadesini kaydetme (resim 15)**




- Kurtarma ifadenizi görüntülemek için talimatları izleyin
- Kelimeleri doğru sırayla dikkatlice yazın
- Bu yedeği güvenli bir yerde, ideal olarak hesap dosyasından farklı bir yerde saklayın



Kurtarma ifadesi kurtarmanıza olanak tanır :




- İtibarınız, ticaretiniz
- Bitcoin fonlarınız



Ancak aşağıdakiler **HAYIR**:




- Güncel ve geçmiş konuşmalarınız
- Ödeme verileri
- İşlem geçmişinde karşı taraf bilgileri




## Bitcoin alım ve satımı



### 1.a Bitcoin nasıl satın alınır: Bir satış teklifi alın



Bir alıcının ilk refleksi, halihazırda bitcoin ile finanse edilen satış tekliflerini kontrol etmek olmalıdır.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Ana ekranda "Satın Al" düğmesine tıklayın (resim 16)
- Daha sonra emanet sistemine yerleştirilmiş ve satışa hazır bitcoinlerin bir listesine göz atabilirsiniz (resim 17). Miktarı, fiyatı (KYC piyasasına göre % olarak), ödeme yöntemlerini ve kabul edilen para birimlerini görebilirsiniz.
- Teklifleri sıralamak ve düzenlemek için filtreleri kullanın (resim 18).
- Not: Filtreler sayfasının altındaki düğme, filtrelerinizle eşleşen bir teklif yayınlandığında bildirim almanızı sağlar; ve "sıfırla" düğmesi, tüm filtreleri temizler (resim 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Size uygun teklifi görüntüleyin ve bir değişim talebi gönderin (resim 19)
- Birkaç değişim talebinde bulunabilirsiniz ve ilk olumlu teklif diğer taleplerinizi iptal edecektir.
- Ödemeyi kararlaştırılan yöntemle yapın.


**Hatırlatma:** fon kaynağı, ödeme yöntemini eklerken belirttiğiniz kaynakla eşleşmelidir.




- Ödemeniz biter bitmez uygulamada ödemenizi onaylayın**.
- Satıcının ödemeyi almasını bekleyin ve bu şekilde beyan edin (resim 20)
- Ve son olarak, satış elemanı ile yaşadığınız deneyimi değerlendirin (resim 21)



![Réception des bitcoins](assets/fr/09.webp)





- İşleminizin durumunu takip edin
- Bitcoinlerin alındığına dair onayı kontrol edin
- Fonlar Peach portföyünüzde mevcut olacaktır (resim 22 ve 23)



### 1.b Bitcoin nasıl satın alınır: Bir teklif oluşturun



Satmak için uygun bir teklif bulamazsanız, satın almak için bir teklif oluşturabilirsiniz. Bu aşamada herhangi bir bitcoin taahhüt edilmediğinden, özellikle geçmişiniz ve itibarınız zayıfsa ya da hiç yoksa, bir takas ortağı bulma şansınız daha az olacaktır. Bunu düzeltmek için, teklifi oluştururken, satıcıları teklifinizi seçmeye motive etmek için *yüksek primli bir teklif* yapmak önemlidir. Devam edelim:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Ana ekranda "Satın alma teklifi oluştur" düğmesine tıklayın (resim 24)
- Henüz yapmadıysanız bir ödeme yöntemi ekleyin ve tercihlerinizi (miktar, prim vb.) girin (resim 25).


"Anında" seçeneği bir işlem talebini otomatik olarak kabul etmenizi sağlar.




 - Devam etmek için "teklif oluştur "a tekrar tıklayın
- Oluşturulduktan sonra, değişim talebiyle size gelme sırası satıcılara geçer. Endişelenmeden uygulamayı kapatıp çıkabilirsiniz.
- Herhangi bir talep almazsanız primi değiştirebilirsiniz. Unutmayın: daha yüksek bir prim, satıcıları teklifinizi aramaya motive edecektir (resim 26).
- Teklifinizi, kendisi de "Exchange" penceresinde bulunan "Satın Al" sekmesinde bulacaksınız (şekil 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Bir satın alma talebi aldığınızda (resim 28) (ve resim 25'te anında ticareti devre dışı bırakmadıysanız), satıcının itibarını kontrol ettikten sonra işlemi kabul edin. Anında işlem etkinse, doğrudan resim 29'a atlayın.
- Satıcı daha sonra bitcoin'i emanet sistemine yerleştirmelidir ("kasayı fonlayın"). (resim 29)
- Ardından, Şekil 30'da gösterilen hedefte, kişisel bankacılık sisteminiz aracılığıyla satıcıya ödeme yapın. Bunu yapana kadar "Ödemeyi yaptım" imlecini sürüklemeyin!
- Satıcı ile mesajlaşma sistemi üzerinden iletişim kurabilirsiniz (P2P şifreli). Bir sorun olması durumunda, sağ üst köşedeki simgeye tıklayarak bir anlaşmazlık açabilirsiniz (resim 31). Daha sonra bir Peach arabulucusu tartışmaya girecektir.



![Offre de vente completée](assets/fr/12.webp)





- Satıcı parayı aldıktan sonra bunu bildirecek ve emanet sistemi bitcoin'i serbest bırakacak ve bu bitcoin wallet'inize doğru yola çıkacaktır (varsayılan olarak Peach'nin günde bir kez çalışan işlem gruplama sistemi GroupHug aracılığıyla),
- Satıcı ile olan deneyiminizi değerlendirin



Bu kadar!



**Yeni alıcılar için not:** satıcılar işlemlerini alıcıların itibarlarına dayandırır ve tamamlanmış işlemi olmayan alıcıların tekliflerinden kaçınma eğilimindedir. İlk etapta, mevcut satış tekliflerini alarak bir itibar oluşturmak daha kolaydır.




### 2.a Bitcoin nasıl satılır: Bir satış oluşturun



Peach'te satış yapmanın en hızlı ve en kolay yolu **satış teklifi** oluşturmaktır.



![Création d'un ordre de vente](assets/fr/13.webp)





- Ana sayfadan "Satış teklifi oluştur" seçeneğine tıklayın (resim 32)
- Teklifinizi ayarlayın, bir ödeme yöntemi ve doğru parametreleri eklediğinizden emin olun


ayrıca :




  - birkaç aynı teklif oluşturun
  - "anında takas" özelliğini etkinleştirin, böylece ilk gelen alıcı sözleşmeyi (sizin onayınız olmadan) alabilir ve ödemeye devam edebilir.
  - bir geri ödeme adresi seçin
  - gW-44 Peach'inizin bagajını finanse edin
- Bitcoinleri verilen adrese göndererek işlemi finanse edin (resim 34)
- İşlemin onaylanmasını bekleyin. İşlem tamamlandığında, teklifiniz piyasada görünür olacaktır.



![Attente du paiement](assets/fr/14.webp)





- Bir alıcının teklifinizi kabul etmesini bekleyin. İşleri hızlandırmak istiyorsanız primi (%) artırmayı düşünün (resim 36)
- Bir değişim talebi aldığınızda, alıcının itibarını kontrol edin. Profilin sizin için uygun olup olmadığına kendiniz karar verin ve uygunsa "kabul et" seçeneğine tıklayın. (37)
- Şimdi ödemeyi kendi bankasından sizin bankanıza yapma sırası alıcıda. Daha sonra ödemeyi size iletecektir. Alıcı ile sohbet yoluyla iletişime geçmekten çekinmeyin.
- paranin bankaniz* tarafindan alindiğini kontrol etti̇kten sonra "ödemeyi̇ aldim" butonuna tiklayarak parayi serbest birakin (resim 38). Bir ödemenin hesabınıza geçtiğini kontrol etmeden önce asla ödemenin alındığını onaylamayın.
- İşlemi değerlendirin
- Bitcoin'lar otomatik olarak alıcıya teslim edilir,



İşte böyle!



**Başarılı bir işlem için güvenlik notu ve ipuçları:**




 - Alıcının bilgilerini inceleyin ve paranın kaynağının Peach'de açıklanan kaynakla eşleşip eşleşmediğini kontrol edin Paranın kaynağı açıklanan kaynakla eşleşmiyorsa, Sohbete gidin ve bir tartışma açın (resim 39) ve parayı kaynağına geri gönderin.
 - Sarı kedideki talimatları izleyin.
 - Karşı tarafınızdan gelen mesajlara hızlı yanıt verin
 - özellikle az deneyimli bir profille çalışırken alıcının tutumuna karşı dikkatli olun
 - Bir sorununuz varsa arabuluculuk hizmetini kullanmaktan çekinmeyin



### 2.b Bitcoin nasıl satılır: teklif alın



Satın alma tekliflerini görüntülemek ve seçmek de mümkündür. Dolandırıcıların en çok bulunduğu yer burası olduğu için özellikle dikkatli olmanız gerekecektir.



![Prendre une offre d'achat](assets/fr/15.webp)





- Ana sayfadan "Satış" üzerine tıklayın (resim 40)
- En cazip teklifleri görüntülemek ve seçmek için filtreleri kullanın (resim 41)



![vérification de la réputation](assets/fr/16.webp)





- bir takas talebinde bulunmadan önce, alıcının profilinin uygunluğunu değerlendirmenizi öneririz. Profilini görmek için bir teklife ve ardından kullanıcının kimliğine tıklayabilirsiniz. Örneğin, resim 42'deki teklif "riskli" olarak değerlendirilebilir (yeni kullanıcı, nispeten yüksek miktar). Bu teklifi kabul ederken karşılaşacağınız "risk", parayı almadan bitcoinleri serbest bırakma hatasını yapmadığınız sürece, sadece zaman kaybetmektir. Bitcoinleri yine de kasaya yatırabilirsiniz.


Öte yandan, resim 43'teki teklif, geçmişinde herhangi bir anlaşmazlık bulunmayan deneyimli bir tüccardan (resim 44) gelmektedir. Bu nedenle daha az riskli bir tekliftir.



![Match avec vendeur](assets/fr/17.webp)





- Teklif talep edildikten sonra, alıcı talebinizi kabul ederse, uygulama sizi aşağıda açıklandığı gibi ticarete devam edebileceğiniz 34 numaralı resme götürecektir.




## Avantajlar ve dezavantajlar



### Peach avantajları





- KYC gerekmez**: Kullanıcı gizliliğini korur.
- Banka bilgilerine erişim yok**: Peach'un banka bilgilerinize veya kimliğinize erişimi yoktur.
- Interface sezgisel**: Orta düzey kullanıcılar için kullanımı kolay.
- Açık Kaynak** : Kaynak kodu herkese açıktır ve topluluk tarafından doğrulanabilir.



### Peach dezavantajları





- Sınırlı Liquidity**: Daha köklü platformlara göre daha az işlem hacmi.
- Düzenleyici risk** : Uygulama bir İsviçre şirketi tarafından yönetilmektedir. Bu nedenle, uygulamayı geliştirebilecek ve potansiyel olarak sansürleyebilecek İsviçre düzenlemelerine tabidir.



## Yararlı kaynaklar





- Fransızca açıklayıcı video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Hızlı başlangıç kılavuzu: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (dolandırıcılara dikkat edin, yöneticiler size asla önce özel mesajla yazmayacaktır)