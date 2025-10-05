---
name: Bitcoin'ın Yaratılış Tarihi
goal: Bitcoin'in kökenlerinin, fırlatılışının ve ilk gelişmelerinin tarihini keşfedin.
objectives: 

  - Bitcoin'nin ortaya çıktığı teknik bağlamın anlaşılması
  - Satoshi Nakamoto'nun Bitcoin'ü nasıl tasarladığını kavrayın
  - Sistemin lansmanına ve gelişimine damgasını vuran olayları bilmek

---

# Bitcoin'in Yaratılış Tarihine Bir Dalış


Bitcoin'nın yaratılış tarihine adanmış bu kursa hoş geldiniz! Bir kullanıcı olarak, kullandığınız aracın nereden geldiğini merak etmiş olabilirsiniz. Dahası, bazen kripto paranın kısa tarihine damga vuran kişi ve olaylara yapılan atıfları anlamamış olabilirsiniz. Son olarak, bu tarihi incelemek, yavaş oluşumunu şekillendiren bağlamı ortaya çıkararak Bitcoin'yı daha iyi anlamanızı sağlayacaktır.


Bu derste Bitcoin'nin tasarımını, fırlatılışını ve ilk ekonomik inşa sürecini keşfedeceksiniz. İlk bölümde Bitcoin'nin ortaya çıktığı teknik bağlamı inceleyeceğiz. İkinci bölümde, doğuşuna ve önyüklemesine odaklanacağız. Üçüncü bölümde, Bitcoin'nin ekonomik kullanım, Mining üretimi ve yazılım geliştirme açısından nasıl büyüklük kazandığını inceleyeceğiz. Dördüncü bölümde ise Satoshi'in yaratıcısı Bitcoin Nakamoto'nun nasıl yavaş yavaş ortadan kaybolduğunu ve kripto para birimini gerçek anlamda kolektif bir proje haline getirerek topluluğun nasıl devraldığını takip edeceğiz.


Elbette bu ders, sözlerini ve eylemlerini keşfedeceğiniz Satoshi Nakamoto figürüne odaklanmaktadır. Yine de, varlığının ilk yıllarında Bitcoin'un gelişimine katılan diğer karakterleri de içeriyor. Böylece Hal Finney, Martti Malmi, Laszlo Hanyecz, Gavin Andresen, Jeff Garzik veya Amir Taaki gibi bu büyümede önemli öncüler olan kişileri tanıyacaksınız. Bitcoin'un başlangıç tarihine yaptığımız bu dalışın size fayda sağlayacağını umuyoruz!


+++

# Giriş

<partId>41dc2815-c63a-4ce1-9b88-e7b3825e958e</partId>


## Kursa genel bakış

<chapterId>85290407-1aa3-4cb4-890a-aed23441afb7</chapterId>

HIS201 kursuna hoş geldiniz!

Bu kurs size Bitcoin'nin yaratılış hikayesini daha önce hiç okumadığınız bir şekilde anlatmayı amaçlamaktadır. Büyüleyici ayrıntılarla dolu olmasına rağmen, genellikle göz ardı edilmektedir. Satoshi Nakamoto tarafından tasarlanmasından erken kayboluşuna ve topluluğa devredilmesine kadar tüm karmaşıklığıyla anlatmaya çalışacağız.


**Kısa Genel Bakış**


Bitcoin, Satoshi Nakamoto takma adını kullanan bir kişi (veya bir grup) tarafından tasarlanmıştır. 31 Ekim 2008 tarihinde, internetteki belirsiz bir e-posta listesi aracılığıyla modelini açıklayan bir beyaz kağıt paylaştı. 8 Ocak 2008'de yazılımın kaynak kodunu yayınlayarak ve zincirin ilk bloklarını Mining ile başlatarak konseptini hayata geçirdi. Kritik sayıda kullanıcıyı çekmeye hevesli olarak, yaratımını çeşitli iletişim kanallarında tanıttı.


Zorlu bir başlangıçtan sonra, sistemin önyüklemesi nihayet Ekim 2009'da, Bitcoin olarak da adlandırılan hesap biriminin bir fiyat kazanmasıyla gerçekleşti. İlk tüccar hizmetleri 2010 yılında, dolara köprü kuran Exchange hizmetleriyle başlayarak ortaya çıkmaya başladı. Yine bu dönemde, Laszlo Hanyecz'in girişiminin ardından, daha verimli bir grafik kartına sahip Mining ilk kez uygulandı ve fiziksel bir mal, özellikle de bir pizza için ilk Exchange gerçekleşti.


Proje, çok popüler bir site olan Slashdot'ta bir makalenin yayınlanmasının ardından 2010 yazında başladı. Dolar ile Exchange, Bitcoin Mining ve yazılım geliştirme bu dönemde önemli ölçüde gelişti. Sonbahardan itibaren, Satoshi Nakamoto yavaş yavaş geri çekilmeye başladı, halka açık yazıları durdurdu ve görevlerini kademeli olarak devretti. Sonunda 2011 baharında, erişim yetkisini sağ kolları Martti Malmi ve Gavin Andresen'e devrettikten sonra tamamen ortadan kayboldu. Topluluk sonunda görevi devraldı ve projeyi bugünkü haline getirmeyi başardı.


Bu anlatının yanı sıra Bitcoin'in bir de tarih öncesi var. Gerçekten de, birdenbire ortaya çıkmış bir nesne değildir. Yaratılışı belirli bir bağlamın parçasıdır: paranın özelliklerini siber uzaya aktarmanın bir yolunun aranması. Özellikle, onu oluşturan teknik Elements, kendisinden önceki onlarca yıllık araştırma ve deneylerin sonucudur. Bitcoin şuna dayanmaktadır:



- Asimetrik kriptografiden kaynaklanan dijital imza 1976 yılında doğmuştur;
- Dağıtılmış mutabakat, 1980'lerde İnternet'in ilk gelişmelerini takiben geliştirilmiştir;
- Belge zaman damgası, 90'ların başında ilk güçlü Hash işlevlerinin ortaya çıkmasıyla icat edildi;
- Proof of Work, 90'lı yıllarda tanımlanmış ve uygulanmıştır.


Bitcoin, Satoshi'u tasarlarken Nakamoto, kriptograf David Chaum tarafından 1982 yılında önerilen ve 1990'larda şirketi DigiCash aracılığıyla uygulanan bir konsept olan eCash modelinden büyük ölçüde esinlenmiştir. Kör imza sürecine dayanan bu model, kullanıcıların nispeten gizli bir şekilde alışveriş yapmalarına olanak tanıyordu. Ancak, Double-spending'i önlemek için müdahale eden merkezi bir banka ağına dayanıyordu. Bu nedenle, DigiCash iflas ettiğinde sistem çöktü. Bitcoin, güvenilir bir üçüncü taraf ihtiyacını ortadan kaldırarak bu sorunu düzeltti.


Bitcoin özel bir bağlamda ortaya çıkmıştır: 2008 yılında dijital altın para birimi e-gold ve 2013 yılında Liberty Reserve sistemi gibi özel para sistemlerinin ABD federal hükümeti tarafından kapatılması. Satoshi Nakamoto, BitTorrent gibi eşler arası paylaşım sistemlerine benzer şekilde riski katılımcıları arasında dağıtan bir modele dayanarak, devletten gelen doğrudan saldırılara dayanabilecek sağlam bir dijital para birimi modeli yarattı.


Bitcoin'ün yaratılması aynı zamanda e-gold ve Liberty Reserve gibi özel para sistemlerinin devlet tarafından kapatılması sırasında gerçekleşmiştir. Bitcoin, ABD federal hükümetinin doğrudan saldırılarına direnebilecek sağlam bir dijital para birimi modeli oluşturdu. BitTorrent gibi eşler arası paylaşım sistemlerine benzer şekilde riskin katılımcılar arasında dağıtılması, hayatta kalmasını sağladı.


Son olarak, Bitcoin projesi, kriptografinin proaktif kullanımı yoluyla İnternet'teki insanların mahremiyetini ve özgürlüğünü korumaya çalışan 90'lı yılların asi kriptograflarından oluşan bir hareket olan Cypherpunk hareketinin ethosunun mirasçısıdır. Bitcoin, bu kişiler tarafından 90'ların sonunda ve 2000'lerin başında hayal edilen b-money, bit gold ya da RPOW gibi projelerle aynı çizgidedir. Satoshi Nakamoto bunlardan bahsetmiş olsa da, Bitcoin'i tasarlamadan önce bunlardan habersizdi ve muhtemelen orijinal hareketin bir parçası değildi.


**Kurs Taslağı**


Bu ders, sırasıyla Bitcoin'nin kökenlerine (3 bölüm), yavaş yavaş ortaya çıkışına (3 bölüm), ilk yükselişine (3 bölüm) ve topluluğunun oluşumuna (4 bölüm) odaklanan dört bölüme ayrılmıştır. Toplamda, aşağıdaki gibi 12 bölüm içermektedir (ilgili dönem de belirtilmiştir):



- eCash: Chaumian elektronik parası (1976-1998)
- Özel Dijital Para Birimleri (1996-2013)
- Nakamoto Öncesi Merkezi Olmayan Modeller (1982-2012)
- Bitcoin'in Doğuşu (Ağustos 2008-Ocak 2009)
- Dünyaya Sunum (Ocak 2009-Ekim 2009)
- Kripto Paranın Önyüklenmesi (Ekim 2009-Nisan 2010)
- Grafik Kartları, Pizzalar ve Bedava Bitcoinler (Nisan 2010-Haziran 2010)
- Büyük Slashdotting (Haziran 2010-Temmuz 2010)
- İlk Teknik Sorunlar (Temmuz 2010-Eylül 2010)
- Dijital Altına Hücum (Eylül 2010-Ekim 2010)
- Ekosistemin Çiçek Açması (Ekim 2010-Aralık 2010)
- Satoshi'un Ortadan Kaybolması (Aralık 2010-Nisan 2011)
- Topluluk Devralıyor (Nisan 2011-Eylül 2011)


**Detaylar**


Tüm tarihler ve saatler UTC bölgesine (Greenwich Meridyenine karşılık gelir) göre verilmiştir ve bu nedenle Amerikan tarihlerinden farklı olabilir. Satoshi Nakamoto muhtemelen projesi üzerinde çalışırken Amerika Birleşik Devletleri'ndeydi. Ancak Bitcoin, özellikle Finlandiyalı geliştirici Martti Malmi'nin (Doğu Avrupa Saati, UTC+2 / UTC+3) katkılarını içeren uluslararası bir projedir ve biz evrensel saat dilimine atıfta bulunacağız. Bu nedenle, ana ağın etkin lansmanının Doğu Yakası saat dilimine (Pasifik Saati, UTC-8 / UTC-7) karşılık gelen 8 Ocak saat 6:54 yerine 9 Ocak saat 2:54'te gerçekleştiğini söylüyoruz.


İçerik kısmen bu dersin yazarı tarafından yazılan Fransızca kitaptan [*L'Élégance de Bitcoin*] (https://bitcoinbook.shop/products/lelegance-de-Bitcoin) (2024) uyarlanmıştır. İnternette arşivlenen doğrudan kaynaklara ek olarak, çeşitli referans çalışmalara da güveniyoruz. İşte bunlardan başlıcaları:



- aaron van Wirdum tarafından yazılan [*The Genesis Book*](https://store.bitcoinmagazine.com/products/the-Genesis-book), 2024 yılında yayımlanmıştır;
- nathaniel Popper tarafından [*Digital Gold*](https://www.amazon.com/Digital-Gold-Bitcoin-Millionaires-Reinvent/dp/006236250X), 2014 yılında yayınlanmıştır;
- phil Champagne tarafından [*The Book of Satoshi*](https://www.bookofsatoshi.com/), 2014 yılında yayınlanmıştır;
- finn Brunton tarafından [*Digital Cash*](https://press.princeton.edu/books/hardcover/9780691179490/digital-cash), 2019 yılında yayınlanmıştır;
- [*Bu Makine Sırları Öldürür*](https://penguinrandomhouselibrary.com/book/?isbn=9780142180495) Andy Greenberg tarafından 2012 yılında yayınlanmıştır.


Bu kursun İngilizce olmayan versiyonu için çoğu alıntının Amerikan İngilizcesinden geldiğini ve duruma göre tercüme edildiğini unutmayın. **Coin** terimi, hesap birimine atıfta bulunduğunda genellikle "unit" (parça değil) olarak çevrilir.


Bitcoin'nin yaratılışının inanılmaz destanını keşfetmeye hazır mısınız? O halde gelin bu olağanüstü hikayeye birlikte dalalım!


# Bitcoin'in Kökenleri

<partId>25a75ed6-f34b-4c9a-8224-e099a3e774dc</partId>


## eCash: Chaumian Dijital Nakit

<chapterId>e443d2ab-68ce-45c0-aec7-30b88d3acdc8</chapterId>


Bitcoin'nin Satoshi Nakamoto tarafından yaratılmasının gerçek hikayesine geçmeden önce, bunun öncesinde neler olduğunu tartışmak yerinde olacaktır. Konuyu üç aşamada ele alacağız: ilk olarak, yaygın olarak *eCash* olarak adlandırılan Chaumian dijital nakit kavramını tanıtacağız; daha sonra, e-gold gibi merkezi sistemlere dayalı özel para birimlerinden bahsedeceğiz; son olarak, Bitcoin olan sağlam dağıtık sistemin uygulanmasından önce hayal edilen teknik modelleri açıklayacağız.


İlk konsept olan eCash ile başlayalım. eCash, 1955 doğumlu Amerikalı bir bilgisayar bilimcisi ve kriptograf olan David Chaum'un çalışmalarından kaynaklanmaktadır. Kendisi anonim iletişim alanında bir öncü ve cypherpunk'ların öncüsü olarak kabul edilir. 1980'lerde kriptografinin gelişimine büyük katkıda bulunmuştur. Aynı zamanda dijital nakit modelini ("Chaumian") geliştirmiş ve 1990'larda şirketi DigiCash aracılığıyla uygulamaya çalışmıştır.


David Chaum'un eylemi kavramsal bir devrimi takip etti: 1976 yılında Whitfield Diffie ve Martin Hellman tarafından asimetrik kriptografinin ortaya çıkarılması. Dijital para fikri de bu ufuk açıcı keşiften doğmuştur. Asimetrik kriptografi, bir mesajın içerdiği bilgileri gizlemenin yanı sıra imza süreçlerinin oluşturulmasına da olanak tanıyordu. Böylece bir kişinin belirli bir miktarda dijital hesap birimine sahip olduğunu matematiksel olarak kanıtlaması mümkün hale geldi.


Bu bölümde asimetrik kriptografinin katkılarını, David Chaum'un bunu eCash'i tasarlamak için nasıl kullandığını ve konseptinin daha sonra nasıl uygulandığını inceleyeceğiz.


### Modern Kriptografinin Ortaya Çıkışı


Kriptografi, iletilen bilginin gizliliğini, gerçekliğini ve bütünlüğünü sağlayarak kötü niyetli üçüncü tarafların varlığında iletişimi güvenli hale getirmeyi amaçlayan bir disiplindir.

Yüzyıllar boyunca, bir mesajın içeriğini gizlemenin tek yöntemi, mesajın hem şifrelenmesi hem de şifresinin çözülmesi için benzersiz bir anahtara dayanan bir şifreleme türünü içeriyordu. Bu *simetrik* kriptografi olarak bilinir. Bir metindeki her harfin alfabede sabit bir uzaklıktaki başka bir harfle değiştirilmesini içeren [Sezar şifresi] (https://fr.wikipedia.org/wiki/Chiffrement_par_décalage) en iyi bilinen örnektir (seçilen mesafe daha sonra anahtar olur). Şifreleme algoritmaları, telekomünikasyonun gelişmesi ve 20. yüzyılda ilk hesaplama makineleri ve bilgisayarların yapılmasıyla önemli ölçüde daha karmaşık hale gelmiştir. Bununla birlikte, bu tür kriptografi çok iyi çalışsa da, önemli bir dezavantajı vardır: iletişim gerçekleşmeden önce anahtarın güvenli bir şekilde Exchange'ye ihtiyaç duyulması.


Bu sorunu çözmek için, açık anahtar kriptografisi olarak da bilinen *asimetrik* kriptografi geliştirilmiştir. İki farklı anahtara dayanır: gizli kalması gereken bir özel anahtar ve özel anahtardan türetilen bir açık anahtar. Teorik olarak, özel anahtar genel anahtardan kolayca bulunamaz, bu da genel anahtarın endişe duymadan herkesle paylaşılabileceği anlamına gelir.


Bu kriptografi türü hem şifreleme algoritmalarının hem de imza işlemlerinin uygulanmasına izin verir. Asimetrik şifreleme, şifreleme anahtarı olarak açık anahtarın ve şifre çözme anahtarı olarak özel anahtarın kullanılmasını içerir. Kullanıcı bir çift anahtar oluşturur, özel anahtarı saklar ve açık anahtarı mesaj gönderebilmeleri için muhabirleriyle paylaşır. Bu tür şifreleme, alıcının mektup almak için kullandığı ve yalnızca anahtarına sahip olduğu bir posta kutusuna benzer.


![Asymmetric encryption](assets/en/001.webp)


Öte yandan dijital imzalar, imza anahtarı olarak özel anahtarın ve doğrulama anahtarı olarak da açık anahtarın kullanılmasına dayanır. Kullanıcı bir anahtar çifti oluşturur, özel anahtarla bir mesajı imzalar ve açık anahtarı kullanarak gerçekliğini doğrulayabilecek muhabirlerine gönderir. Böylece, özel anahtarı bilmelerine asla gerek kalmaz.


![Digital signature](assets/en/002.webp)


1970'lerde birçok araştırmacı bağımsız olarak asimetrik kriptografiyi keşfetti. Ancak, bulduklarını ilk sunanlar Stanford Üniversitesi'nden iki kriptograf olan Whitfield Diffie ve Martin Hellman olmuştur. Kasım 1976'da *IEEE Transactions on Information Theory* dergisinde "[New Directions in Cryptography] (https://ee.stanford.edu/~hellman/publications/24.pdf)" başlıklı bir makale yayınladılar ve bu makalede bir anahtar Exchange algoritması (simetrik şifreleme için gizli anahtarların iletimi için tasarlanmıştır) ve bir dijital imza süreci tanımlandı. Bu makalenin giriş bölümünde şöyle yazmışlardır:

> "Bugün kriptografide bir devrimin eşiğinde duruyoruz. Ucuz dijital donanımın geliştirilmesi, mekanik hesaplamanın tasarım sınırlamalarından kurtarmış ve yüksek kaliteli kriptografik cihazların maliyetini, uzaktan para çekme makineleri ve bilgisayar terminalleri gibi ticari uygulamalarda kullanılabilecek seviyeye indirmiştir. Buna karşılık, bu tür uygulamalar güvenli anahtar dağıtım kanallarının gerekliliğini en aza indiren ve Supply yazılı imzaya eşdeğer yeni kriptografik sistem türlerine ihtiyaç yaratmaktadır. Aynı zamanda, bilgi teorisi ve bilgisayar bilimindeki teorik gelişmeler, bu eski sanatı bir bilime dönüştürerek kanıtlanabilir şekilde güvenli kriptosistemler sağlama konusunda umut vaat etmektedir."

İşte Stanford Haber Servisi için Chuck Painter tarafından 1977 yılında çekilmiş bir fotoğraf. Fotoğrafta Whitfield Diffie (sağda) ve Martin Hellman'ı (ortada) görüyorsunuz. Soldaki kişi ise aynı keşfi yapmak üzere olan kriptograf Ralph Merkle.


![Ralph Merkle, Martin Hellman, and Whitfield Diffie in 1977](assets/en/003.webp)


Diffie ve Hellman'ın makalesi birçok yeniliğin önünü açmıştır. Bunlardan biri, kriptograflar Ronald Rivest, Adi Shamir ve Leonard Adleman tarafından 1977 yılında tasarlanan ve 1983 yılında MIT tarafından patenti alınan [RSA kriptosistemidir] (https://people.csail.mit.edu/rivest/Rsapaper.pdf). Bu sistem, anahtarların rollerinin değiştirilmesi sayesinde mesajların hem şifrelenmesine hem de imzalanmasına izin verir. RSA ilk kez Ağustos 1977'de *Scientific American* dergisinde yayınlanan [Martin Gardner'ın makalesinde] (https://simson.net/ref/1977/Gardner_RSA.pdf) "Matematiksel Oyunlar" başlığıyla kamuoyuna sunulmuştur: Kırılması milyonlarca yıl sürecek yeni bir tür şifre."


Asimetrik kriptografinin keşfi, bir görüntünün hesaplanmasını (ileri yön) ve bir ön görüntünün elde edilmesini (geri yön) çok zor hale getiren tek yönlü fonksiyonların yaratılmasını da motive etti. Özellikle, değişken boyutlu bir mesajı sabit boyutlu bir özete dönüştüren ilk kriptografik Hash fonksiyonlarının geliştirilmesine yol açtı. 1989 ve 1991 yılları arasında Ronald Rivest, MIT için çeşitli hash algoritmaları (MD2, MD4 ve MD5) tasarlamıştır.


Bitcoin'nin temel kriptografik Elements'sı bu araştırmadan kaynaklanmaktadır. Geleneksel bir işlem için harcama yetkisi sağlayan ECDSA imza şeması 1992 yılında NIST için oluşturulmuştur. Protokolün birçok yerinde kullanılan SHA-256 Hash işlevi, 2001 yılında NSA tarafından kamuya açıklanan SHA-2 algoritma paketinin bir parçası olarak yayınlanmıştır. Bu konu hakkında daha fazla bilgi için Loïc Morel tarafından sunulan CYP201 kursuna bakınız.

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### Kör İmzalar ve Elektronik Nakit


Kriptografideki bu devrim, o zamanlar Berkeley Üniversitesi'nde doktora öğrencisi olan Batı Yakalı bilgisayar bilimcisi genç David Chaum'a da ilham verdi. Kısa sürede mahremiyetin korunması konusunda tutkulu hale geldi ve giderek bilgisayarlaşan bir toplumda özgürlük ve gizliliğin geleceği konusunda çok endişeliydi.


![David Chaum in the 90s](assets/en/004.webp)

90'larda David Chaum (kaynak: [Elixxir](https://www.youtube.com/watch?v=X45NmCBpYUw))


Temel makalesinde] (https://www.cs.ru.nl/~jhh/pub/secsem/chaum1985bigbrother.pdf), "Kimliksiz Güvenlik: 1985'te *Communications of the ACM* dergisinde yayınlanan "Büyük Birader'i Modası Geçmiş Hale Getirecek İşlem Sistemleri" başlıklı makalesinde şöyle yazmıştır:

> "Bilgisayarların, sıradan tüketici işlemlerinde toplanan verilerden bireylerin yaşam tarzlarını, alışkanlıklarını, nerede olduklarını ve ilişkilerini çıkarsamak için kullanılabileceği bir dosya toplumunun temelleri atılıyor. Verilerin, onları tutan ya da dinleyenler tarafından kötüye kullanılmaya karşı güvende kalıp kalmayacağı konusundaki belirsizlik, insanların gözlemlenebilir faaliyetlerini değiştirmelerine neden olarak 'caydırıcı bir etki' yaratabilir. Bilgisayarlaşma yaygınlaştıkça, bu sorunların ortaya çıkma potansiyeli de önemli ölçüde artacaktır."

Mahremiyetin korunması konusundaki bu takıntısı, 1979 gibi erken bir tarihte katkıda bulunduğu kriptografi alanına olan ilgisini açıklamaktadır. 1981 yılında, özellikle e-posta aktarım hizmetlerine (Mixmaster) ve Tor anonim ağına hizmet edecek olan karma ağlar aracılığıyla anonim iletişimin temellerini tanımladı. 1982 yılında, yıllık CRYPTO '82 konferansında Uluslararası Kriptolojik Araştırma Derneği'nin (IACR) kuruluşuna katıldı. Aynı yıl (ve bizi burada ilgilendiren de bu), "İzi Sürülemeyen Ödemeler için Kör İmza" başlıklı bir [makale] (https://sceweb.sce.uhcl.edu/yang/teaching/csci5234WebSecurityFall2011/Chaum-blind-signatures.PDF) ile gizliliğe saygılı dijital para birimi modeli eCash'in kalbinde yer alan kör imza sürecini yayınladı.


David Chaum'un 1996 yılında bir basın açıklamasında [açıkladığı] gibi (https://chaum.com/wp-content/uploads/2022/01/05-07-96-DigiCash_s-Ecash%E2%84%A2-to-be-Issued-by-Deutsche-Bank.pdf):


> "Ecash, kağıt paranın çalışamadığı yerlerde internette çalışan dijital bir nakit şeklidir. Nakit para gibi, tüketicilere satın aldıkları şeylerde gerçek bir gizlilik sunar."

ECash modeli, müşterilerin nispeten gizli ödemeler yapmasına olanak tanıyan bir dijital para birimi konseptidir. Bu bir nakit para biçimidir çünkü kullanıcılar dijital banknotları güvenilir bir üçüncü tarafça yönetilen bir hesap yerine doğrudan ellerinde tutabilirler. Ancak sistem, her işlemde kullanıcıların banknotlarını basan ve değiştiren banka veya darphane adı verilen sunuculara dayanır. Bir banknot transfer edildiğinde, alıcı bunu doğrulamaktan ve karşılığında bir veya daha fazla banknot vermekten sorumlu olan bankasına gönderir. Bankaların her biri Double-spending'u önlemek için harcanan banknotların bir kaydını tutar. Her eCash sistemi, yetkilendirmeleri yapan merkezi bir otorite tarafından denetlenir.


Dijital banknotlar teminatsız olarak çıkarılabilir veya desteklenebilir. İlk durumda, değer kazanması gereken bir temel para birimi oluştururlar. İkinci durumda, başka bir para birimi (tipik olarak dolar) tarafından desteklenirler ve kullanıcı, ilgili tutarı geri almak için istediği zaman bankalarına banknotlarını iade edebilir.


Teknik işleyişinde eCash modeli, imzalayan kişinin neyi imzaladığını görmeden bir şeyi imzalamasına olanak tanıyan kör imza sürecine dayanmaktadır. Bir kullanıcı her bir banknotu üretir ve daha sonra banka banknotu tanımlayamadan gerçekliğini sağlamak için bir banka tarafından imzalanır. Her bir banknot belirli miktarda parasal birimi (mezhep) temsil eder ve sistemdeki her bankanın her bir mezhep türünü imzalamak için bir özel anahtarı vardır. İlgili matematiksel prosedür (burada açıklamayacağız), kapalı bir zarf içine yerleştirilmiş [karbon kağıdı] (https://fr.wikipedia.org/wiki/Papier_carbone) üzerindeki fiziksel bir notun imzalanmasına benzer.


Burada bir Chaumian notasının oluşturulması ve değiştirilmesinde yer alan farklı adımların bir örneği yer almaktadır (*L'Élégance de Bitcoin*'dan):


![Creation and replacement of a Chaumian note](assets/en/005.webp)


Eylemler (her biri bir matematiksel işleme veya bir bilgi aktarımına karşılık gelir) aşağıdaki gibidir:


1. Alice adlı bir kullanıcı bir karbon kağıdı notu oluşturur.

2. Kapalı bir zarfın içine koyar.

3. Alice, banknotunu içeren zarfı bankaya gönderir ve istenen kupür miktarını bildirir.

4. Banka zarfı imzalayarak senedin kaç birimi temsil ettiğini belirtir ve bu da karbon kağıdının içinin imzalanmasını gerektirir.

5. Banka zarfı Alice'e iade eder.

6. Alice imzalı notunu almak için zarfı açar.

7. Bankanın imzasının gerçek olduğunu doğrular.

İmzalı notun transferi, Bob olarak adlandıracağımız sistemin başka bir kullanıcısına verilerek yapılır. Adımlar aşağıdaki gibidir:



- Alice notu Bob'ye gönderir.
- Bob, Alice'in bankasının bunu gerçekten imzaladığını doğrular;
- Aldığı notu hemen bankasına gönderir.
- Bob'in bankası senedin kullanılmadığını kontrol eder ve kullanılmışsa yeni bir senet imzalar veya Bob'in hesabına alacak kaydeder (destek varsa).


Tüm bunlar sistemdeki hiçbir bankanın ödemeyi Alice'in kimliğiyle ilişkilendiremeyeceği anlamına gelir ki bu da neden müşteri gizliliğinden bahsettiğimizi açıklar. Ancak, tüccar (burada Bob) ödemeyi onaylamak için bir bankadan geçmelidir ve bankası alınan tutarlardan haberdar olabilir. Dahası, sistem güvenilir bir üçüncü tarafa - katılımcı bankaları belirleyen merkezi otoriteye - bağlıdır ve bu da sistemi tasarımı itibariyle kırılgan hale getirmektedir.


### ECash Uygulamaları


1990 yılında David Chaum, elektronik para fikrini hayata geçirmek için Amsterdam, Hollanda merkezli Digicash B.V. şirketini kurdu. Bu şirket Chaum'un icadının patentlerini elinde bulunduruyordu. O dönemde İnternet henüz emekleme aşamasındaydı (Web henüz geliştirilme aşamasındaydı) ve e-ticaret mevcut değildi; dolayısıyla eCash modeli müthiş bir fırsat oluşturuyordu.


![DigiCash Logo](assets/en/006.webp)


Ancak, modeli ilk test eden David Chaum'un şirketi değildi: patentleri dikkate almadan uygulayan ve bunun için izin istemeyen cypherpunks idi. Böylece, Magic Money adlı bir protokol, Pr0duct Cypher adını kullanan anonim bir geliştirici tarafından 4 Şubat 1994 tarihinde cypherpunks posta listesinde [önerildi] (https://cypherpunks.venona.com/date/1994/02/msg00247.html). Bu protokol, bir eCash darphanesi olarak hizmet veren bir e-posta sunucusunu çalıştırarak kişinin kendi para birimini oluşturmasına izin veriyordu. Cypherpunk'lar Tacky Tokens, GhostMarks, DigiFrancs ve NexusBucks gibi her türlü hesap birimini oluştururken çok eğlendiler. Ancak, bu tokenlerin faydası çok azdı ve takasları çok nadirdi.

DigiCash tarafında, birkaç yıl süren geliştirmenin ardından, Mayıs 1994'te Cenevre'deki CERN'de World Wide Web üzerine düzenlenen ilk uluslararası konferansta bir prototip [sunuldu] (https://chaum.com/wp-content/uploads/2022/01/05-27-94-World_s-first-electronic-cash-payment-over-computer-networks.pdf). Şirket daha sonra aynı yılın 19 Ekim'inde "CyberBucks" adı verilen ve başka herhangi bir para birimi tarafından desteklenmeyen birimler çıkararak bir deneme gerçekleştirdi. Bu denemenin bir parçası olarak çeşitli tüccarlar CyberBucks'ı kabul etti. Şifre kırıcılar da bunu kabul ederek gerçek takaslar yapmak için kullandılar. Böylece CyberBucks piyasada değer kazandı. Ancak, eCash geleneksel bankacılık sisteminde kullanılmaya başlandığında bu değer çöktü.


![Photo (blurry) of the DigiCash team in 1995](assets/en/007.webp)

DigiCash ekibinin 1995 yılındaki fotoğrafı (bulanık): David Chaum en solda (kaynak: [Chaum.com](https://chaum.com/ecash/))


ECash'in bankacılık sistemine girişi, DigiCash'in Missouri'de küçük bir banka olan Mark Twain Bank ile ortaklığının başladığı Ekim 1995'te başladı. Exchange oranı değişken olan CyberBucks'ın aksine, hesap birimi ABD doları tarafından destekleniyordu. 1996 ve 1998 yılları arasında Mark Twain Bank'ı altı banka takip etti: Finlandiya'da Merita Bank, Almanya'da Deutsche Bank, Avustralya'da Advance Bank, Avusturya'da Bank Austria, Norveç'te Den norske Bank ve İsviçre'de Credit Suisse. Basın daha sonra bu sistem için parlak bir gelecek vaat etti.


Bununla birlikte, işler planlandığı gibi gitmedi. David Chaum, inatçılığı ve şüpheciliği nedeniyle şirketi üzerindeki kontrolü elinde tutmak istedi. ING ve ABN AMRO, Visa, Netscape ve Microsoft gibi büyük finansal oyuncularla ortaklık yapmayı reddetti. Şirket merkezini Kaliforniya'ya taşıdığında 1997'de görevinden ayrıldı. 1998 yılında, ortak bankalar eCash'i terk ettiklerini açıkladılar. DigiCash sonunda Kasım 1998'de iflas etti ve Chaumian elektronik nakit uygulamasına son verdi.


### David Chaum'un Modelinin Mirası


Ancak eCash modelinin geliştirilmesi sonuçsuz kalmadı. Çok sayıda girişim için zemin hazırladı.

1990'larda, İnternet üzerinden ödeme yapmaya yönelik diğer teknik çözümler eCash tarafından başlatılan trendden yararlandı: o zamanlar pratik olmayan, maliyetli ve güvensiz olan kredi kartı ödemelerinin dezavantajlarından yararlanan CyberCash, First Virtual veya Open Market'te durum böyleydi. CyberCoin (CyberCash tarafından yönetilen), NetBill ve MilliCent gibi mikro ödeme sistemleri de ortaya çıktı. Bu sistemler hiçbir zaman gerçekten gelişmedi, ancak 1999'da başlayan ve bir sonraki bölümde tartışacağımız PayPal'ın gelişimine zemin hazırladılar.

E-gold ve Liberty Reserve gibi diğer alternatif merkezi sistemler de paralel olarak ortaya çıktı. Bunlar özel dijital para birimlerini yönetmiş ve siber uzayda var olabilecek yasal belirsizlikten faydalanmışlardır. Bu konuyu da bir sonraki bölümde ele alacağız.


Daha sonra eCash, b-money, bit gold ve RPOW gibi modelleri geliştiren cypherpunk'lara ilham verdi. Proof of Work ve daha sonra Bitcoin'da bulunan diğer Elements'i eklediler. Bu kavramları Bölüm 3'te inceleyeceğiz.


Son olarak, David Chaum'un modeli Satoshi Nakamoto'yu para birimi kavramını geliştirirken önemli ölçüde etkilemiştir. Bu, [white paper](assets/pdf/Bitcoin-20090324.pdf) (başlık, 2. bölümdeki sorunun tanımı, Ağustos 2008'de Wei Dai'ye [gönderilen](https://gwern.net/doc/Bitcoin/2008-nakamoto) PDF'nin adı) ve özel ve kamusal müdahalelerindeki çok sayıda referansla kanıtlanmaktadır. Bu anlamda eCash, tek olmasa bile Bitcoin'nin ana öncülüdür.


Satoshi Nakamoto, Bitcoin ile sağlam ve gizli bir dijital para birimi, gerçek elektronik nakit yarattı. Bunu yaparken, 1999 yılında Ulusal Vergi Mükellefleri Birliği Vakfı ile yaptığı bir röportajda Nobel Ekonomi Ödülü sahibi ve Chicago Okulu'nun kurucusu Milton Friedman'ın [öngörüsünü] (https://www.youtube.com/watch?v=mlwxdyLnMXM&t=872s) gerçekleştirdi:


> "Bence internet, devletin rolünü azaltacak en önemli güçlerden biri olacak. Eksik olan ama yakında geliştirilecek olan tek şey güvenilir bir e-nakit, yani A'nın B'yi, B'nin de A'yı tanımadan internet üzerinden A'dan B'ye para transferi yapabileceğiniz bir yöntem."

## Özel Dijital Para Birimleri

<chapterId>43035fa3-2805-4331-a6fb-070931d749cf</chapterId>


Bir önceki bölümde, internetin ve modern kriptografinin ortaya çıkmasıyla ortaya çıkan ilk elektronik para biçimini incelemiştik: David Chaum'un eCash modeli. Bu model Satoshi Nakamoto'yu önemli ölçüde etkilemiş ve Bitcoin'e giden yolda önemli bir kilometre taşı olmuştur. Bununla birlikte, kripto paranın kökenlerinin hikayesi eCash ile bitmiyor; 1990'ların sonlarında geliştirilen İnternet üzerinde çalışan özel para birimleri ile ilgili deneyleri de içeriyor.


Bu bölümde Amerika Birleşik Devletleri'nde özel para birimleriyle neler yapıldığı incelenecektir. İlk olarak, Özgürlük Doları örneğini tartışacağız. Daha sonra e-gold ve Liberty Reserve gibi merkezi sistemleri inceleyeceğiz. Son olarak, yaklaşımı farklı olan ancak güvenilir bir üçüncü tarafa dayalı modelin aydınlatıcı bir örneği olarak hizmet veren PayPal hakkında konuşacağız.


Her durumda, yetkililer eninde sonunda bu sistemleri kapattı ya da mali düzenlemelere uymak zorunda kaldı. Bu nedenle, bu sistemleri iyi anlayan Satoshi Nakamoto, merkezi bir otoriteye dayanmayan alternatif bir sisteme olan ihtiyacı derinden anladı.


### Amerika Birleşik Devletleri'nde Parasal Özgürlük ve Özgürlük Doları


Amerika Birleşik Devletleri'nin tarihi, başlangıcından itibaren büyük bir parasal çoğulculuk ile karakterize edilmiştir. 17. yüzyıldan 19. yüzyılın ortalarına kadar, bağımsız bir cumhuriyete dönüşen İngiliz kolonisi, yabancı para birimlerinin serbest dolaşımına (ABD doları 1792'ye kadar resmi olarak oluşturulmadı) ve altın ve gümüş sikkelerin [özel basımına](https://fee.org/articles/private-coinage-in-america/) gerçekten de izin verdi. Göreceli bir [bankacılık özgürlüğü](https://iea.org.uk/wp-content/uploads/2023/12/Dowd-Free-Banking-Interactive.pdf) de 1837 ve 1863 yılları arasında hüküm sürdü.


Ancak, Birlik tarafından kazanılan İç Savaş ile birlikte, gücün merkezileştirilmesi sürecinde işler değişti. Böylece, 8 Haziran 1864 tarihinde Kongre'den çıkan bir yasa, özel sikke basımını yasakladı. Birleşik Devletler Kanunu'nun 18. başlığının 486. bölümü (*18 U.S. Code § 486*) haline gelen bu yasa [şöyle] (https://www.law.cornell.edu/uscode/text/18/486):

"Yasa tarafından yetkilendirilenler dışında, ister Birleşik Devletler'in ya da yabancı ülkelerin madeni paralarına benzesin, ister özgün tasarım olsun, altın, gümüş ya da diğer metallerden ya da metal alaşımlarından, geçerli para birimi olarak kullanılmak üzere madeni para üreten, tedavüle çıkaran ya da tedavüle çıkarmaya ya da tedavüle çıkarmaya teşebbüs eden herkes, bu başlık altında para cezasına ya da beş yıldan fazla olmamak üzere hapis cezasına ya da her ikisine birden çarptırılacaktır."


Bu kısıtlamaları uygulamak için Abraham Lincoln 1865 yılında bir devlet kurumu kurdu: Gizli Servis. Gizli Servis'in ilk görevi kalpazanlık ve genel olarak mali dolandırıcılıkla mücadele etmekti. Dolaylı olarak, para üretimi tekelini Birleşik Devletler Darphanesi'ne emanet ederek federal devletin senyorajını güçlendirdi.


Bu durum daha sonra daha da kısıtlı hale geldi. Federal Reserve of the United States adı verilen merkez bankası, 1907'deki bankacılık paniğinin ardından 1913'te kuruldu. Ardından, klasik altın standardı 1933 yılında F.D. Roosevelt'in Yeni Düzen'inin bir parçası olarak, Amerika Birleşik Devletleri'nde bulunan bireylerin ve şirketlerin altın tutmasını yasaklayan [Executive Order 6102] (https://fr.wikipedia.org/wiki/Executive_Order_6102) ile terk edildi. Parasal sistemde altına yapılan atıf nihayet 1971 yılında Richard Nixon'ın doların uluslararası alanda altına çevrilebilirliğinin sona erdiğini duyurmasıyla terk edilmiştir.

Altın bulundurma yasağının kaldırılması ve 1970'lerde başlayan internet gelişimiyle birlikte özel para birimleri kullanma fikri yeniden ortaya çıktı. Bernard von NotHaus 1998 yılında altın ve gümüşe dayalı, gümüş sikkeler ve temsili banknotlar halinde bulunabilen bir para birimi olan Liberty Dollar'ı piyasaya sürdü. NORFED (National Organization for the Repeal of the Federal Reserve and Internal Revenue Code'un kısaltması) adlı kar amacı gütmeyen bir kuruluş sistemi yönetti. 2003 yılından itibaren Liberty Doları, e-altın benzeri bir hesap sistemi aracılığıyla dijital olarak da kullanılmaya başlandı (bir sonraki bölüme bakınız). Bu sistem belli bir başarı elde etti. Dolaşımdaki madeni paraların yanı sıra, NORFED'in kasalarında paranın konvertibilitesini sağlamak için yaklaşık 8 milyon dolar değerli metal bulunuyordu ve bunun 6 milyon doları dijital birimi desteklemek içindi.


![2003 Silver Liberty Dollar](assets/en/008.webp)

2003 yılından gümüş Liberty Doları (10 dolar) (kaynak: [Numista](https://en.numista.com/catalogue/exonumia242820.html))


Eylül 2006'da ABD Darphanesi, Adalet Bakanlığı ile birlikte kaleme aldığı bir [basın açıklaması] (https://www.usmint.gov/news/press-releases/20060914-liberty-dollars-not-legal-tender-united-states-mint-warns-consumers) yayınlayarak NORFED'in madeni paralarının kullanımının Birleşik Devletler Kanunu'nun 18. başlığının 486. bölümünü ihlal ettiği ve "federal bir suç" teşkil ettiği sonucuna vardı Sonuç olarak, 2007 yılında NORFED'in tesislerine yapılan bir FBI baskınının ardından, 2009 yılında tutuklanan ve Mart 2011'de yargılanan NotHaus ve ortaklarına karşı ihlaller düzenlendi. Bernard von NotHaus 2014 yılında temyizde altı ay ev hapsi ve üç yıl denetimli serbestlik cezasına çarptırıldı.


### e-altın: Web'de Altın

Özel elektronik para biriminin sembolik bir örneği e-altın sistemidir. "Dijital altın para birimi" olarak bilinen bu sistem, elektronik olarak transfer edilen ve güvenli bir şekilde saklanan eşdeğer miktarda altınla tamamen desteklenen bir para birimi anlamına gelmektedir. Douglas Jackson ve Barry Downey tarafından 1996 yılında kurulmuştur. Douglas Jackson, Avusturyalı ekonomist Friedrich von Hayek'i takip eden ve e-altın ile "[daha iyi bir para] (https://blog.bettermoney.com/)" yaratmak isteyen Florida'da yaşayan Amerikalı bir onkologdu.

Prensip, her bir e-altın biriminin gerçek altına dönüştürülebilmesiydi. Altın rezervleri Amerika Birleşik Devletleri'nde bulunan Gold & Silver Reserve Inc. (G&SR) adlı bir şirket tarafından yönetiliyordu. Bilgisayar sistemi ise Karayipler'deki Saint Kitts ve Nevis'te kayıtlı e-gold Ltd. adlı ikinci bir şirket tarafından yönetiliyordu. Söz konusu olan tek metal altın değildi: kullanıcılar aynı model üzerine inşa edilmiş e-gümüş, e-platin ve e-paladyum da tutabiliyor ve Exchange kullanabiliyorlardı.


E-gold sistemi, yeni gelişmekte olan Web'den, özellikle de yeni Netscape tarayıcısından yararlandı. Her müşteri kendi hesabına özel bir yazılım kullanmak yerine web sitesinden erişebiliyordu. O zamanlar için, bankalar arası transferden esinlenen gerçek zamanlı bir brüt ödeme sistemi kullanan platform çok yüksek performans gösteriyordu. İşte 2005 yılında e-altın göndermenin nasıl göründüğü (o zamanki bir [tutorial](https://www.geocities.ws/rizuan_mahrol/setpbystep.html)'dan alınan görüntü):


![Sending on e-gold in 2005](assets/en/009.webp)


E-altın sistemi büyük bir başarı elde etti: 2006'daki zirvesinde 80 milyon dolardan fazla değere sahip 3,6 ton altını [garanti](https://web.archive.org/web/20060907024202if_/http://www.e-gold.com:80/examiner.html) etti, yıllık 3 milyar dolarlık bir hacim için günde 75.000 işlemi [işledi](https://web.archive.org/web/20060208044937/http://www.e-gold.com/stats.html) ve 2,7 milyondan fazla hesabı yönetti.

Bu başarı, Devletin müdahalesinin ardından aniden durduruldu. Gizli Servis tarafından yürütülen bir soruşturmanın ardından Douglas Jackson, iki şirketi ve ortakları 27 Nisan 2007'de Adalet Bakanlığı tarafından kara para aklamayı kolaylaştırmak ve lisanssız para transferi işi yapmaktan [suçlandı](https://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html). Kasım 2008'de Douglas Jackson suçlu bulundu ve elektronik gözetim altında 6 ay ev hapsi de dahil olmak üzere 3 yıl denetimli serbestlik cezasına çarptırıldı. Başarısız bir lisans girişiminin ardından, e-gold Kasım 2009'da kalıcı olarak kapanmak zorunda kaldı.


Aynı modeli izleyen başka sistemler de kuruldu. James Turk ve oğlu tarafından Şubat 2001'de kurulan GoldMoney günümüzde finansal düzenlemelere uyum sağlamıştır. e-Bullion, James Fayed tarafından Temmuz 2001'de kurulan sistem 2008'de kapılarını kapatmıştır. Son olarak, son dijital altın para birimlerinden biri de 2002 yılında Simon Davis tarafından Panama'da kurulan ve 2015 yılında bir çıkış dolandırıcılığının parçası olarak faaliyetlerini durduran Pecunix'tir.


### Özgürlük Rezervi, Federal Rezerv'e Alternatif


Merkezi özel para birimi sisteminin bir başka örneği de kullanıcıların ABD doları, avro veya altına sabitlenmiş elektronik para birimlerini tutmalarına ve transfer etmelerine olanak tanıyan Liberty Reserve'dir. Bu sistemi Ukrayna kökenli bir Amerikalı olan Arthur Budovsky ve Saint Petersburg'dan Rus bir göçmen olan Vladimir Kats yaratmıştır. Arthur Budovsky 2006 yılında, o zamanlar vergi cenneti olarak kabul edilen Kosta Rika'ya gitti ve Liberty Reserve S.A. adlı şirketini burada tescil ettirdi.


![Liberty Reserve logo in 2009](assets/en/010.webp)

2009'da Liberty Reserve logosu (kaynak: [Wikimedia](https://commons.wikimedia.org/wiki/File:LR_Logo-1-.webp))


Sistem e-gold'a oldukça benziyordu, ancak fonlar (esas olarak dolar cinsinden) özel kasalar yerine offshore banka hesaplarında tutuluyordu. Liberty Reserve, Douglas Jackson ve ortaklarının suçlanmasının ardından Nisan 2007'de e-gold'un kapatılmasından büyük fayda sağladı. Mayıs 2013'te [ABD Adalet Bakanlığı'na göre] (https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Indictment%20-%20Redacted_0.pdf), platformun 200.000'den fazlası ABD'de olmak üzere dünya çapında bir milyondan fazla kullanıcısı vardı ve toplam hacmi 1,4 milyar doları aşan yılda 12 milyon finansal işlem gerçekleştiriyordu. Kullanım öncelikle suç faaliyetleri içindi, ancak [bunlarla sınırlı değildi] (https://web.archive.org/web/20150422023243/https://www.theatlantic.com/magazine/archive/2015/05/bank-of-the-underworld/389555/): Liberty Reserve ayrıca Forex yatırımcıları tarafından veya denizaşırı transferler için de kullanıldı.


Ancak sistem sonunda e-gold ile aynı kaderi paylaştı. 2009 yılında Kosta Rika *Superintendencia General de Entidades Financieras* Liberty Reserve ile ilgilenerek lisans almasını istedi (şirket bunu yapmadı). Ardından, Kasım 2011'de ABD FinCEN, sistemin "suçlular tarafından küresel olarak para taşımak için anonim işlemler yapmak için kullanıldığını" belirten bir [bildirim] (https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Indictment%20-%20Redacted_0.pdf#page=12) yayınladı Son olarak, Liberty Reserve uluslararası bir operasyonun sonunda kapatıldı: 24 Mayıs 2013'te Arthur Budovsky ve ana ortakları farklı yargı bölgelerinde (İspanya, Amerika Birleşik Devletleri, Kosta Rika) suçlandı ve tutuklandı ve ana siteye Adalet Bakanlığı tarafından el konuldu. Arthur Budovsky 2016 yılında ABD'ye iade edildikten sonra kara para aklama suçundan 20 yıl hapis cezasına çarptırıldı.


Dolayısıyla bu örnek, yargı yetkisi arbitrajının para birimini devlet müdahalesinden korumak için yetersiz olduğunu göstermektedir.


### PayPal ve Peter Thiel'in Vizyonu

Son olarak PayPal örneğini tartışmalıyız. Her ne kadar yaratıcıları PayPal'ı mevcut sistemden bağımsız bir para birimi haline getirme niyetinde olmasalar da, Silikon Vadisi'nin yıkıcı ideolojisine uygun olarak bu ürünün toplumu etkileyeceğini öngörmüşlerdir. PayPal ürünü, birkaç ay önce Stanford Üniversitesi'nde tanışan Max Levchin ve Peter Thiel tarafından Aralık 1998'de San Francisco'da kurulan Confinity Inc. tarafından geliştirilmiştir. Başlangıçta FieldLink olarak adlandırılan şirket, PalmPilot el bilgisayarları üzerinde güvenli ödeme sistemleri geliştirmeyi amaçlıyordu.


PayPal, Ekim 1999'da bir şirket mühendisi tarafından oluşturuldu. E-posta adresleri arasında kolay ve ücretsiz ödemeler yapılmasına izin veriyordu ve bireyler arasında basit ödemeleri transfer etmeyi amaçlıyordu ("pay pal"). İş modeli, müşterilerin bankalarda tutulan fonlarından faiz kazanmaya dayanıyordu, bu da işletme maliyetlerini karşılıyor ve hissedarları ödüllendiriyordu. Dolayısıyla, Liberty Reserve'e benzer şekilde bankacılık sistemi üzerine inşa edilmiş bir hizmetti.


İnternet balonu zirveye ulaştığında, ürün ilk aylarda, özellikle de tavsiye sistemi sayesinde hızlı bir büyüme yaşadı. Bu başarı, çok daha fazla sermayeye sahip olan, fikri kopyalayan ve Confinity'nin zararına olacak şekilde hizmetin kendi versiyonunu başlatan rakiplerin dikkatini çekti. Bu nedenle şirket, Mart 2000'de bunlardan biri olan Elon Musk'ın sahibi olduğu çevrimiçi banka X.com ile birleşerek PayPal Inc. haline gelmek zorunda kaldı.


PayPal'ın orijinal vizyonu, Peter Thiel'in özgürlükçü vizyonu doğrultusunda devrim niteliğindeydi. Eric Jackson'ın 2012 yılında *The PayPal Wars* adlı kitabında aktardığı üzere, 1999 sonbaharında söyledikleri şöyledir


> "Elbette, Amerikalı kullanıcılar için 'kullanışlı' dediğimiz şey, gelişmekte olan dünya için devrim niteliğinde olacaktır. Bu ülkelerin birçoğunun hükümetleri para birimleriyle hızlı ve gevşek oynuyor. Enflasyonu ve bazen de geçen yıl Rusya ve bazı Güneydoğu Asya ülkelerinde gördüğümüz gibi toptan devalüasyonları, vatandaşlarının servetlerini ellerinden almak için kullanıyorlar. Oradaki sıradan insanların çoğu hiçbir zaman bir offshore hesabı açma ya da ellerine ABD doları gibi istikrarlı bir para biriminden birkaç banknottan fazlasını alma fırsatına sahip olamıyor. Eninde sonunda PayPal bunu değiştirebilecek. Gelecekte, hizmetimizi ABD dışında da kullanılabilir hale getirdiğimizde ve İnternet penetrasyonu tüm ekonomik katmanlara yayılmaya devam ettikçe, PayPal dünya çapındaki vatandaşlara para birimleri üzerinde daha önce hiç sahip olmadıkları kadar doğrudan kontrol sağlayacaktır. Yozlaşmış hükümetlerin eski yöntemlerle halklarının servetlerini çalmaları neredeyse imkansız hale gelecek, çünkü bunu denedikleri takdirde halk Dolar, Pound ya da Yen'e geçerek daha güvenli bir para birimi için değersiz yerel para birimini terk edecektir."

![Peter Thiel on October 20, 1999, during his speech in Oakland, California for the Independent Institute](assets/en/011.webp)

Peter Thiel 20 Ekim 1999 tarihinde Oakland, Kaliforniya'da Independent Institute için yaptığı konuşma sırasında (kaynak: [Youtube](https://www.youtube.com/watch?v=e-X8D1gOU1E))


Ancak işler istenilen yönde gelişmedi ve PayPal her türlü finansal düzenlemeye uymak zorunda kaldı, öyle ki hizmet artık dünya çapında ödeme sansürü ve hesap dondurmalarıyla ünlü. Böyle bir sistemin yerleşik güce meydan okuyabileceğine inanmak saflıktı.


### Merkezi Alternatifler ve Bitcoin

Bu nedenle, mevcut sisteme alternatif olarak merkezi hizmetler yaratma girişimlerinin hepsinin sonunda bir şekilde durdurulduğunu gözlemliyoruz. Bu modellerin dezavantajı, iflas edebilecek, fonları kaçırabilecek veya yetkililer tarafından kontrol edilebilecek güvenilir bir üçüncü tarafa dayanmalarıdır. İkinci durumda, söz konusu hizmet bir ikilemle karşı karşıya kalır: GoldMoney ve PayPal'ın yaptığı gibi finansal düzenlemelere uyarak uyum sağlamak ya da e-gold, Liberty Reserve ve Liberty Dollar'ın yaşadığı gibi uyum sağlamayı reddederek yok olmak.

Bu sistemlerin kapatılması Bitcoin'nın oluşturulması ve ilk günleriyle çağdaştı. Sonuç olarak, Satoshi Nakamoto ve Bitcoin'nın ilk kullanıcıları bunlardan haberdardı. Satoshi'ye gelince, e-gold tarafından kullanılan modelin [farkındaydı](https://www.metzdowd.com/pipermail/cryptography/2009-January/015041.html) ve kamuya açık ve özel müdahalelerinde birkaç kez Pecunix ve Liberty Reserve'den [bahsetti](https://bitcointalk.org/index.php?topic=87.msg807#msg807).


Merkezi sistemler kırılgan olduğundan, cypherpunk'lar da dahil olmak üzere özgürlük savunucuları *merkezi olmayan* bir para birimi yaratmaya çalıştılar. Tüm sistemin altyapısını tek bir hata noktasına dayandırmaktan kaçınmanın bir yolunu bulmak gerekiyordu. Bu nedenle 1990'ların sonunda ve 2000'lerin başında, Bitcoin'in keşfinden önce birkaç "güven azaltıcı" model ortaya çıktı. Bir sonraki bölüm bu modellere ayrılacaktır.


## Nakamoto'dan Önce Merkezi Olmayan Modeller

<chapterId>a104f23c-e9c3-4457-a194-d87cc5f35f13</chapterId>


Bitcoin dijital para biriminin merkezi olmayan bir modelini temsil etmektedir. Bunu yaparken, sistemde tek bir başarısızlık noktası oluşturacak güvenilir bir üçüncü taraf ihtiyacını ortadan kaldırmaktadır. ECash, dijital altın para birimleri ve Liberty Reserve örneklerinde görüldüğü üzere, mevcut sisteme alternatif olma niyetindeki bir sistemin merkezileştirilmesi kaçınılmaz olarak sistemin kapanmasına yol açmaktadır.

Bununla birlikte Bitcoin, önerilen ilk merkezi olmayan para birimi kavramı değildi. Bu tür modeller 1990'ların sonlarından bu yana, internette bireylerin özgürlüğü ve mahremiyetine takıntılı olan ve (David Chaum gibi) izleme sistemlerinin distopik bir geleceğe yol açtığına inanan cypherpunk'lar tarafından tanımlanmıştır. "Kod yazmak" için [çağrıda bulundular] (https://cypherpunks.venona.com/date/1993/03/msg00392.html) ve "elektronik parayı" idealleri için temel bir unsur olarak gördüler. (*orijinal: "Cypherpunk'lar kod yazıyor. (...) Gizliliğimizi kriptografi, anonim posta yönlendirme sistemleri, dijital imzalar ve elektronik para ile savunuyoruz. "*)


Bu bölümde, daha sonra Bitcoin'te kullanılan çeşitli temel teknik Elements'nin ortaya çıkışını inceleyeceğiz: dağıtılmış mutabakat, zaman damgası ve Proof of Work. Ardından, sırasıyla Wei Dai, Nick Szabo ve Hal Finney tarafından tasarlanan b-money, bit gold ve RPOW hakkında konuşacağız. Son olarak, modeli biraz farklı olan, ancak Bitcoin'ün yaratılış tarihinde yeri olan Ripple'ın durumunu tartışacağız.


### Dağıtılmış Konsensüs


1950'lerde bilgisayarların ortaya çıkmasıyla birlikte, onları birbirine bağlama olasılığı da ortaya çıktı. İlk bilgisayar ağları bu şekilde oluşturuldu ve 1970'lerde "ağların ağı" olan İnternet'in gelişmesine yol açtı. Bu ağların altyapısı sorunu kaçınılmaz olarak ortaya çıktı. Bu nedenle Polonyalı-Amerikalı bilgisayar bilimcisi Paul Baran, 1964 tarihli temel makalesinde (paket anahtarlamayı tanımlayan) üç tür ağ listeledi: tek bir düğüme dayanan merkezi ağ; her noktanın bir düğüm olduğu dağıtılmış ağ; birden fazla düğümden oluşan dağıtılmış bir ağa dayanan merkezi olmayan (dağıtılmamış) ağ.


![Centralized, decentralized, and distributed networks according to Paul Baran](assets/en/012.webp)


Bu düşüncelerden iki saf model türetilebilir: merkezi bir sunucunun istemcilerin isteklerine yanıt verdiği istemci-sunucu modeli ve her düğümün sistemde aynı role sahip olduğu eşler arası model. Bu son model özellikle 2000'li yıllarda BitTorrent ve diğer benzer protokollerin oluşturulmasıyla dosya paylaşımı için faydalı olmuştur. Tor ağı merkezi değildir, tamamen eşler arası değildir.

Dağıtık mimarilerde karşılaşılan bir sorun, genellikle Bizans Genelleri Sorunu olarak adlandırılan ve Leslie Lamport, Robert Shostak ve Marshall Pease tarafından 1982 yılında yayınlanan bir [makale] (https://lamport.azurewebsites.net/pubs/byz.pdf) ile resmileştirilen dağıtık mutabakat sorunudur. Bu sorun, eşler arası sistemlerde iletim güvenilirliği ve katılımcıların bütünlüğü sorununu ele alır ve bir bilgisayar sisteminin bileşenlerinin anlaşması gereken durumlarda geçerlidir.


Problem, Bizans İmparatorluğu'nun ordu generallerinin birlikleriyle bir düşman şehrini kuşattığı, saldırı niyetinde olduğu ve sadece haberciler aracılığıyla iletişim kurabildiği bir metafor olarak ifade edilmektedir. Amaç, hainlerin varlığını yönetebilecek ve saldırının başarılı olması için tüm sadık generallerin bir savaş planı üzerinde anlaşmasını sağlayacak bir strateji (yani bir algoritma) bulmaktır. İşte bir örnek (kaynak: *L'Élégance de Bitcoin*):


![The Byzantine Generals Problem](assets/en/013.webp)


Bu sorunun çözülmesi, bir hesap birimini yöneten dağıtık sistemler için önemlidir. Bu tür sistemler, katılımcıların hesap birimlerinin Ownership'i, yani kimin neye sahip olduğu konusunda anlaşmasını gerektirir.


Bitcoin'dan önce sorun, düğümlerin önceden bilinmesini ve bunlardan ikisinin dürüst olmasını gerektiren "klasik" algoritmalarla çözülüyordu. Bunlar arasında en bilineni muhtemelen 1999 yılında Miguel Castro ve Barbara Liskov tarafından geliştirilen ve belirli sayıda katılımcının saniyede binlerce isteği bir milisaniyeden daha az bir gecikmeyle yöneterek anlaşmasına olanak tanıyan [PBFT](https://css.csail.mit.edu/6.824/2014/papers/castro-practicalbft.pdf) (Practical Byzantine Fault Tolerance'ın kısaltması) konsensüs algoritmasıdır.


Bitcoin mutabakat algoritması ile Satoshi Nakamoto bu sorunu olasılıksal olarak çözmüş ve işlemlerin katı kesinliğinden ödün vererek belirli kısıtlamaların kaldırılmasına izin vermiştir. 13 Kasım 2008'de "Proof-of-Work zincirinin Bizans Generalleri Problemine bir çözüm olduğunu" [yazdı] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014849.html)


### Belge Zaman Damgası

Zaman damgası, bir olay veya belge gibi bilgilerle bir tarih ve saatin ilişkilendirilmesini içeren bir tekniktir. Yasal açıdan bakıldığında bu, örneğin bir Contract'in belirli bir tarihten önce var olmasını sağlayabilir. Gerçek dünyada, bir belgeyi kapalı bir zarf içinde göndermek veya bir zaman çizelgesini bir deftere kaydetmek gibi bir şeyi Timestamp yapmanın çok sayıda yolu vardır.

Ancak, zaman damgası özellikle dosyaların (metin, görüntü, ses veya video) kolayca değiştirilebildiği dijital dünyada kullanışlıdır. Zaman damgası, alınan belgelerin (veya parmak izlerinin) kaydedilmesinden ve bunların alındığı tarih ve saatle ilişkilendirilmesinden sorumlu olan merkezi hizmetler tarafından gerçekleştirilebilir. Bu, güvenilir zaman damgası olarak adlandırılır.


1991 yılında, New Jersey'de bulunan bir Ar-Ge konsorsiyumu olan Bell Communications Research Inc. (genellikle "Bellcore" olarak adlandırılır) için çalışan iki araştırmacı Stuart Haber ve Scott Stornetta tarafından gizli ve güvenli bir zaman damgası tekniği önerilmiştir. "Dijital bir belgeye zaman damgası nasıl vurulur" başlıklı [makalelerinde] (http://www.staroceans.org/e-book/Haber_Stornetta.pdf), sertifikalı bir zaman damgası hizmetinin müşteri belgelerinin gizliliğini ve sertifikasyonun güvenilirliğini artırmak için tek yönlü bir işlevi (MD4 Hash işlevi gibi) ve bir imza algoritmasını nasıl kullanabileceğini açıkladılar. Özellikle, fikir, tek yönlü işlevin uygulanmasına önceki Timestamp'yi dahil ederek bilgiyi zincirlemekti.


![Example of certified timestamping](assets/en/014.webp)

Sertifikalı zaman damgası örneği (kaynak: [Wikimedia](https://en.m.wikipedia.org/wiki/File:Trusted_timestamping.svg))


Haber ve Stornetta, 1992 yılında New York Times'ın seri ilanlarında kriptografik parmak izlerini (yararlı verilerin hash edilmesiyle elde edilen) yayınlayarak fikirlerini hayata geçirdiler. Daha sonra 1994 yılında kendilerini tamamen bu faaliyete adamak için kendi şirketleri olan Surety Technologies'i kurdular. Bu nedenle, Bitcoin Blockchain'ün habercisi olan, gazetede yayınlanacak yeni parmak izinin hesaplanmasında önceki parmak izinin dikkate alındığı ilk Timestamp zincirini oluşturdukları için [bilinmektedir] (https://www.vice.com/en/article/j5nzx4/what-was-the-first-Blockchain).

Haber ve Stornetta'nın üç makalesi Satoshi Nakamoto tarafından [Bitcoin white paper]'da (assets/pdf/Bitcoin-20090324.pdf) alıntılanmıştır: daha önce bahsedilen 1991 tarihli makale, 1993 tarihli bir [paper] (https://www.math.columbia.edu/~bayer/papers/Timestamp_BHS93.pdf), özellikle Merkle ağaçlarının kullanımı yoluyla bir öncekinde önerilen protokolleri geliştirmiştir ve 1997 tarihli bir [paper] (https://cdn.nakamotoinstitute.org/docs/secure-names-bit-strings.pdf), dosyaları evrensel olarak tek yönlü işlevler kullanarak adlandırmanın bir yolunu sunmuştur. Ayrıca Belçika'daki Louvain Katolik Üniversitesi'nde kriptografi araştırma grubunda çalışan Henri Massias, Xavier Serret-Avila ve Jean-Jacques Quisquater tarafından 1999 yılında yazılan yeni bir zaman damgası sistemini tanımlayan bir [paper](https://cdn.nakamotoinstitute.org/docs/secure-timestamping-service.pdf)'a da atıfta bulunulmuştur.

### Proof of Work ve Hashcash


Proof of Work, bir bilgisayar cihazının bir hizmete veya ayrıcalığa erişim için seçilmek üzere enerji harcadığını nesnel ve ölçülebilir bir şekilde göstermesini sağlayan bir süreçtir. Bir saldırganın herhangi bir itibar sistemini bozmak veya kontrolünü ele geçirmek için kimlikleri aşırı derecede çoğaltmasını zorlaştıran Sybil saldırılarına karşı koyma mekanizmasıdır.


Proof of Work konsepti ilk olarak 1992 yılında Kaliforniya'da San Jose'nin güneyinde bulunan IBM Almaden araştırma merkezinde çalışan bilgisayar bilimcileri Cynthia Dwork ve Moni Naor tarafından tanımlanmıştır. "Pricing via Processing or Combatting Junk Mail" başlıklı bir [araştırma makalesinde] (https://www.wisdom.weizmann.ac.il/~naor/PAPERS/pvp.pdf), e-posta gelen kutularında spam ile mücadele etmek için bir yöntem sundular. Model, kullanıcıları gönderilen her e-posta için kriptografik bir bulmaca çözmeye zorlamaktan oluşuyordu; böylece toplu e-posta gönderme yeteneği sınırlanırken, ara sıra gönderenlerin engellenmemesine izin veriliyordu. Ancak, bu fikirlerini hiçbir zaman hayata geçiremediler.

İnternetin 1990'larda yaygınlaşmasıyla birlikte, istenmeyen e-posta sorunu, cypherpunk'ların e-posta listesi de dahil olmak üzere giderek daha fazla baskı yaratmaya başladı. Bu nedenle Dwork ve Naor'un konsepti 1997 yılında genç İngiliz Cypherpunk Adam Back tarafından bir Hash fonksiyonu kullanarak basit çalışma kanıtları üreten bir algoritma olan Hashcash ile [uygulandı] (https://cypherpunks.venona.com/date/1997/03/msg00774.html). Daha spesifik olarak, söz konusu Hash fonksiyonunun kısmi bir çarpışmasını bulmayı, yani aynı veri bitleriyle başlayan bir ayak izine sahip iki mesaj elde etmeyi içerir (not: 2002'de yayınlanan 1.0 sürümünden itibaren, sıfır baskı için kısmi bir çarpışma keşfetmeyi, yani ayak izi belirli sayıda ikili sıfırla başlayan bir ön görüntü bulmayı içerir). Hash işlevi tek yönlü olduğundan, böyle bir başarı ancak farklı olasılıkları ayrı ayrı test ederek gerçekleştirilebilir, bu da bir enerji harcaması gerektirir.


![Adam Back in 2001](assets/en/015.webp)

Adam Back 2001 yılında (kaynak: [Adam Back'in kişisel sayfasının arşivi](https://web.archive.org/web/20040404011747/http://www.cypherspace.org/adam/))


Bununla birlikte, cypherpunk'lar Proof of Work'i spam'i sınırlandırmanın basit bir yolu olarak görmekle yetinmediler; aynı zamanda dijital bir para birimi üretmenin maliyetini garanti altına almak için de kullanmak istediler. Bu nedenle, 1997 yılında Adam Back [bu fikri] (https://cypherpunks.venona.com/date/1997/04/msg00822.html) kendisi tasarladı, ancak bu şekilde elde edilen çalışma kanıtlarının tamamen dağıtık bir şekilde aktarılamayacağının (Double-spending sorunu nedeniyle) ve bu nedenle eCash gibi merkezi bir sistemden geçmesi gerektiğinin farkındaydı. Benzer şekilde, 1996 yılında kriptograflar Ronald Rivest ve Adi Shamir, çalışma kanıtlarının üretimi sayesinde paralarının taklit edilmesinin imkansız olduğu varsayılan merkezi bir mikro ödeme sistemi olan [MicroMint]'i (https://people.csail.mit.edu/rivest/pubs/RS96a.pdf) tanımladılar.


Böyle bir modelin sağlam ve sürdürülebilir bir şekilde işlemesini sağlayacak uygun bir düzenlemenin bulunması gerekiyordu. Şifre kırıcılar Wei Dai, Nick Szabo ve Hal Finney bu konsepti, daha sonra inceleyeceğimiz b-money, bit gold ve RPOW gibi protokolleri aracılığıyla geliştirmeye çalıştılar. Satoshi Nakamoto bunu Hashcash'i Bitcoin tasarımına dahil ederek başarmıştır.


### b-money: merkezi̇ olmayan stablecoin

Cypherpunk hareketinden ortaya çıkan ilk protokol, 1998 yılında Wei Dai tarafından kavramsallaştırılan merkezi olmayan bir dijital para birimi modeli olan b-money idi. Seattle'da yaşayan ve Microsoft için çalışan genç bir Çinli-Amerikalı kriptograf olan Dai, 1994'ten itibaren posta listesine dahil oldu. Daha sonra Bitcoin yazılımında kullanılan açık kaynaklı Crypto++ kütüphanesini oluşturarak adını duyurdu.


Wei Dai, 26 Kasım 1998'de kişisel sayfasında b-money'nin açıklayıcı metnini yayınladı ve aynı gün Cypherpunk posta listesinin bağlantısını paylaştı. E-postasında] (https://cypherpunks.venona.com/date/1998/11/msg00941.html), b-money'i "takma adlar için parasal Exchange ve Contract uygulaması için yeni bir protokol" olarak tanımladı


Onun konseptinde sistem takip edilemez bir eşler arası ağa dayanıyordu. Her katılımcı bir "dijital takma ad", bir açık anahtar ile tanımlanıyordu. Her işlem mesajı gönderen tarafından imzalanıyor ve alıcı için şifreleniyordu. Her katılımcı, her bir takma ad tarafından tutulan b-para birimlerinin miktarlarını listeleyen bir veritabanı tutuyordu.


Para birimi yaratma, bilinen ve daha önce çözülmemiş bir hesaplama probleminin çözümünü yayınlayan Proof of Work aracılığıyla tüm katılımcılara açıktı. Yaratılan birim sayısı, birimin değerini "istikrarlı" bir denge noktası etrafında tutmak için standart bir mal sepetine (örneğin değerli metaller dahil) göre ifade edilen bu çabanın maliyetine bağlıydı. Sistem ayrıca ilkel bir emanet süreci sayesinde doğrudan ağ üzerinde sözleşme oluşturma ve yürütme imkanı da sunuyordu.


Oldukça dahiyane olmasına rağmen Wei Dai'nin b-para konsepti tamamen işlevsel değildi. Dolayısıyla, ağdaki Sybil saldırılarına karşı savunmasızlık (teorik olarak herkes ağa yeni düğümler ekleyebilir), sunucuların önceden seçilmesi durumunda ağ merkezileşmesi ve hesap biriminin istikrarı ile ilgili sorun (piyasadaki gözlemlenebilir fiyatları kim belirler?) gibi önemli kusurları vardı.

Listede yayınlanmasından sonra, b-money cypherpunk'ların ve özellikle de [Adam Back'in] dikkatini çekti(https://cypherpunks.venona.com/date/1998/12/msg00203.html). Ancak, Wei Dai modelini sadece işlevsiz olduğu için değil, aynı zamanda kriptografın kripto-anarşisine yönelik [hayal kırıklığı](https://www.lesswrong.com/posts/YdfpDyRpNyypivgdu/aalwa-ask-any-lesswronger-anything#XKwphuwm366RegQ3d) nedeniyle de hiçbir zaman uygulamadı. Bununla birlikte, b-para Bitcoin beyaz kağıdında alıntılanmış ve bu da onu öncülerinden biri haline getirmiştir.


![Citation of b-money in the Bitcoin white paper](assets/en/016.webp)


### bit gold: Bitcoin öncesi dijital altın


Cypherpunk'ların fikirlerinden ortaya çıkan ikinci model, Nick Szabo'nun 1998 yılında hayal ettiği bit gold fikriydi. Macar kökenli Amerikalı bir bilgisayar bilimcisi olan Szabo, altı ay boyunca DigiCash için danışman olarak çalışmıştı. Bir Cypherpunk olan Szabo, 1995 yılında akıllı sözleşmeler kavramını resmileştirmesiyle tanınıyor.


1994 yılında Nick Szabo libtech-l adında özel bir posta listesi oluşturdu. Adından da anlaşılacağı üzere, otoritelerin saldırılarına karşı bireysel özgürlüklerin korunmasını sağlayan özgürlükçü teknikler üzerine tartışmalara ev sahipliği yapmayı amaçlıyordu. Wei Dai ve Hal Finney gibi Cypherpunk'ların yanı sıra Hayekçi para birimi rekabeti ve serbest bankacılığın savunucuları olan ekonomistler Larry White ve George Selgin'in de erişimi vardı.


![Nick Szabo in 1997](assets/en/017.webp)

1997 yılında Nick Szabo (kaynak: [Adrien Chen](https://twitter.com/AdrianChen/status/456922865992863744/photo/1))


Nick Szabo konseptini ilk olarak libtech-l listesinde açıklamış, ardından 1999 yılında kişisel web sitesinde bir [taslak](https://web.archive.org/web/20140406003811/http://szabo.best.vwh.net/bitgold.html) yayınlamıştır. Daha sonra 2005 yılında Unenumerated adlı blogunda yayınladığı bir [makale](https://unenumerated.blogspot.com/2005/12/bit-gold.html) ile bit gold'u sundu.


Protokolün bir bit sanal altın kaynağının yaratılmasını ve Exchange'yi yönetmesi gerekiyordu. Fiziksel altın tarafından garanti edilen e-altın ya da teorik olarak bir mal sepetine endeksli olan b-paranın aksine, bit altın başka herhangi bir varlık tarafından desteklenmeyecek, ancak içsel, taklit edilemez bir kıtlığa sahip olacak ve böylece tamamen dijital bir altın oluşturacaktı.

Protokolün ana unsuru para yaratımının Proof of Work aracılığıyla yapılmasıydı: bit altınlar bilgisayarların hesaplama gücü kullanılarak yaratılıyor ve her çözüm bir diğerinden hesaplanarak bir iş ispatı zinciri oluşturuluyordu. Bu çalışma kanıtlarının üretim tarihi ve saati birden fazla Timestamp sunucusu kullanılarak onaylanmıştır. Sistem, açık anahtarları ile tanımlanan ve özel anahtarlarını kullanarak işlemleri yetkilendiren kullanıcıların mülklerine ve takaslarına atıfta bulunan bir kamu mülkiyeti siciline dayanıyordu. Kayıt defteri, [Byzantine Quorum System] (https://dahliamalkhi.wordpress.com/wp-content/uploads/2015/12/byzquorums-distcomputing1998.pdf) adı verilen klasik bir mutabakat algoritması tarafından koordine edilen "mülk kulübü" adı verilen bir sunucu ağı tarafından doğrulandı ve sürdürüldü.


Bit gold'un Bitcoin ile benzerliği dikkat çekicidir. Bit gold'da ayrı olan sistemin üç kurucu Elements'i (iş kanıtlarının üretimi, bunların zaman damgası ve mülkiyet kayıtlarının yönetimi) Bitcoin'de tek bir kavram olarak bulunur: Blockchain. Bu nedenle birçok kişi bunu Bitcoin'nin bir taslağı olarak görmüş ve Nick Szabo'nun Satoshi olabileceği spekülasyonunu yapmıştır.


Ancak, iki adamın vizyonları birbirinden ayrılıyordu. Bit gold'da dijital altın parçalarının üretilme şekli, bunların değiştirilebilir olmadığı, yani karıştırılamayacağı anlamına geliyordu: gerçek homojen bir hesap birimi için temel olarak kullanılmak üzere sistem dışındaki bir dış piyasada değerlendirilmeleri gerekiyordu. Bu nedenle bit altın modeli, nadir bir rezerv para birimini yönetmek için bir uzlaşma sistemi olarak düşünülmüştü ve bunun üzerine, mümkünse Chaumian modeli kullanılarak serbest bir bankacılık ekonomisi inşa edilecekti. Bu nedenle, Nisan 2008'de Nick Szabo blogundaki bir [yorumda] (https://web.archive.org/web/20171227190431/http://unenumerated.blogspot.com/2008/04/bit-gold-markets.html?showComment=1207799580000#c3741843833998921269) hala konseptini uygulamak için yardım istiyordu. Ancak bu uygulama hiçbir zaman gerçekleşmedi.


### RPOW: Yeniden Kullanılabilir Çalışma Kanıtları

Şifrecilerin zihninden çıkan üçüncü sistem, 2004 yılında Hal Finney tarafından geliştirilen ve Reusable Proofs of Work'ün kısaltması olan RPOW sistemidir. Hal Finney Los Angeles'ta yaşayan Amerikalı bir bilgisayar bilimcisi ve kriptograftır. İlk günlerden beri bir Cypherpunk olan Finney, David Chaum'un fikirlerine ve ünlü eCash modeline tutkuyla bağlıydı. 1996'dan beri Phil Zimmermann ile birlikte PGP şifreleme yazılımını geliştirmek için çalışıyordu.


Hal Finney, RPOW sistemini tasarlamak için eCash ve bit gold'un arkasındaki fikirleri benimsemiştir. Sisteminin benzersizliği, Hashcash tarafından üretilen iş kanıtlarının transferine izin veren şeffaf bir sunucuya dayanmasıydı. Bu sunucu, IBM tarafından tasarlanan bir kimlik doğrulama süreci aracılığıyla makinede hangi programların çalıştığını doğrulamaya izin veren, yüksek güvenlikli, kurcalamaya dayanıklı bir unsur olan IBM 4758 Secure Cryptographic Coprocessor'ı kullanıyordu. Böylece harici bir kullanıcı RPOW sunucusunun kamuya açık kodla doğru programı çalıştırdığından emin olabiliyordu.


Sunucu yeniden kullanılabilir Proof-of-Work jetonlarını yönetir ve RSA şifrelemesi kullanarak bunları imzalamaktan sorumludur. Bunlar Hashcash aracılığıyla bir Proof of Work üretilerek veya önceki bir RPOW token'den oluşturuldu. Bir ödeme sırasında, gönderici RPOW jetonlarını alıcıya verir, alıcı da derhal sunucu ile iletişime geçerek toplam değeri giriş değerine eşit olan bir veya daha fazla yeni jeton alırdı. Dolayısıyla RPOW'ların işleyişi eCash'teki dijital biletlerin işleyişine benzemektedir.


İşte Hal Finney'in kendisi tarafından [tasarlanmış] (https://nakamotoinstitute.org/finney/rpow/slides/slide004.html) bir illüstrasyon:


![Exchange in RPOW](assets/en/018.webp)


Hal Finney sadece modeli tasarlamakla kalmamış, aynı zamanda bizzat uygulamıştır. 15 Ağustos 2004 tarihinde cypherpunks posta listesinde RPOW sisteminin başlatıldığını [duyurdu](https://lists.cpunks.org/pipermail/cypherpunks-legacy/2004-August/134945.html) ve özel web sitesinde (rpow.net) işleyişini belgeledi. Daha sonra San Francisco'da düzenlenen CodeCon 2005 konferansında [sundu](https://web.archive.org/web/20050204193327/http://rpow.net/slides/slide001.html) ve burada Proof-of-Work tokenlerinin potansiyel kullanım alanlarını tartıştı: değer transferi, spam düzenlemesi, video oyunlarında ticaret, poker gibi çevrimiçi kumar ve BitTorrent gibi dosya paylaşım protokollerinde anti-leeching.

Ancak, RPOW'un neden beklenen başarıyı elde edemediğini açıklayabilecek içsel kusurları vardı:



- Merkezi bir sunucuya dayandığı için güvenlik modeli oldukça zayıftı;
- Para politikası (hashing'e dayalı), bilgi işlem performansındaki üstel artış nedeniyle özellikle cazip değildi.


Dolayısıyla, RPOW'un fiili kullanımı anekdot niteliğindeydi. Yine de Hal Finney, Satoshi Nakamoto'nun gelişinden dört yıl önce deneysel bir kavram kanıtı oluşturarak Bitcoin'a "[yolu açtığı] (https://mmalmi.github.io/Satoshi/#email-24)" (*orijinal: "bu meşaleyi taşıdığı "*) için övgüyü hak ediyor.


### Ripple: Kredinin Merkezsizleştirilmesi


Bitcoin'ün daha az bilinen ancak burada önemli olan bir başka öncül modeli de Kanadalı geliştirici Ryan Fugger tarafından 2004 yılında tasarlanan dağıtık kredi protokolü Ripple'dır. Genç Kanadalı, protokolünü tasarlamadan önce Vancouver'da deneyimlediği [yerel Exchange ticaret sistemi](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27%C3%A9change_local) (LETS) kavramından esinlenmiştir. Ripple [white paper](https://web.archive.org/web/20060221162102/http://ripple.sourceforge.net/decentralizedcurrency.pdf)'ı 14 Nisan 2004 tarihinde yayınladı. Ardından, merkezi bir sunucuda çalışan ve kullanıcıların yalnızca bir e-posta Address ile bağlanmasına izin veren RipplePay adlı bir kavram kanıtı aracılığıyla uyguladı.


![Ryan Fugger circa 2010](assets/en/019.webp)

Ryan Fugger 2010 dolaylarında (kaynak: [Crunchbase](https://www.crunchbase.com/person/ryan-fugger))


Ripple kavramı, paranın esasen IOU'lardan, yani krediden oluştuğu fikrine dayanıyordu. Bu, bağlantıları insanlar arasındaki kredi ilişkileri olacak eşler arası bir ağ kurmakla ilgiliydi. Ödemeler, tüm katılımcıların birbirlerine borç para veren bankacılar gibi hareket ettiği bir dizi kredinin yönlendirilmesiyle yapılıyordu. Alice, Bob'e 10 dolar borç vererek ve Bob'ten aynısını Carole'a yapmasını isteyerek David'e 10 dolar ödeyebiliyordu. Carole da aynısını David'e yaptı: David'in hesabına Alice'ün yarattığı paradan 10 dolar yatırıldı. Sistem bir şekilde dalgalanmalarla çalışıyordu, bu da projenin adını açıklıyor.


İşte Ripple'ın 2011 yılında yapılmış bir tanıtım videosu:


:::video id=056364f2-a222-4d79-a4a1-cb0dc4cea751:::


Topluluğunun ve birkaç bin kullanıcısının coşkusuna rağmen, Ripple'ın başarılı olmasını engelleyen büyük kusurları vardı. Özellikle, "merkezi olmayan Commitment sorunu "ndan [muzdaripti] (https://fiatjaf.com/3cb7c325.html): bir ödeme sırasında, katılımcılar kredi zincirini sağlamak için güvenli bir şekilde taahhütte bulunamazlardı. Lightning bu sorunu daha sonra çözecektir. (*orijinal: "merkezi olmayan taahhüt sorunu "*)


Projesinin hiçbir yere gitmediğini gören Ryan Fugger, Kasım 2012'de Ripple'ın dizginlerini şirketin liderleri OpenCoin Inc. şirketinden Chris Larsen ve Jed McCaleb'e devretti. Şirketin adı 2013 yılında Ripple Labs olarak değiştirildi. Bir konsensüs algoritmasına ve yerel bir hesap birimi olan XRP'ye dayanan ilk konseptten önemli ölçüde farklı bir protokol haline getirdiler. Ryan Fugger, karışıklığı önlemek için 2020 yılında konsept kanıtının adını [Rumplepay] (https://rumplepay.com/) olarak değiştirdi.


Ripple, Bitcoin ile çağdaştı ve ikincisiyle ilgilenen pek çok kişi birincisiyle de ilgileniyordu. Gerçekten de Ripple, Bitcoin ile paylaşılan bir özellik olan dağıtık bir mimariye dayanan yenilikçi bir model oluşturuyordu. Bu konuda Satoshi Nakamoto [şöyle yazmıştır] (https://diyhpl.us/~bryan/irc/Bitcoin-Satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February.txt.gz): "Ripple, güveni yoğunlaştırmak yerine yayması bakımından benzersizdir."


### Bitcoin, bir arayışın doruk noktası

Böylece, 2000'li yılların sonunda, Bitcoin'i oluşturan tüm Elements biliniyordu ve bunları birleştirmek için birkaç girişimde bulunulmuştu. Ancak, önerilen birleşimler ikna edici değildi. Özellikle cypherpunk'lar, gerçekten merkezi olmayan bir dijital para biriminin tasarımının imkansız olduğuna inanarak bu konuya olan ilgilerini yavaş yavaş kaybettiler. Satoshi Nakamoto onların yanıldığını kanıtladı.


Bitcoin gerçekten de tüm bu kavramların ustaca bir araya getirilmesinden oluşmaktadır. Diffie ve Hellmann tarafından 1976 yılında önerilen asimetrik kriptografiden kaynaklanan dijital imzaya dayanmaktadır. David Chaum'un 90'lı yıllarda uyguladığı eCash modelinin amaçladığı gibi "elektronik nakit "tir. Yenilikçi konsensüs algoritması, 1982 yılında Lamport, Shostak ve Pease tarafından ifade edilen Bizans Generalleri Problemini sağlam bir şekilde çözmektedir. Blockchain'ün eşler arası bir ağda yönetilmesiyle, Haber ve Stornetta'nın 1991'deki konseptini yeniden gözden geçiren bir "dağıtılmış Timestamp sunucusu" biçimidir. İşlem bloklarını seçmek ve birimleri üretmek için 1997 yılında Adam Back tarafından önerilen Hashcash'e benzer bir süreç olan Proof of Work'ü kullanır. Son olarak, tasarımında, Satoshi Nakamoto'nun bir şekilde saygı gösterdiği b-money, bit gold, RPOW ve Ripple projelerini hatırlatmaktadır.


Bitcoin böylece, devletlerin insafına kalmadan tamamen İnternet üzerinde var olan bir para birimi olan siber para birimi arayışının doruk noktasını oluşturmaktadır. Bu kursun geri kalanında, nasıl hayata geçtiğini ve ilk yıllarındaki önemli olayları anlatacağız. Bu hikaye benzersizdir ve buraya kadar geldiyseniz kesinlikle ilginizi çekecektir. Hazır olun!


# Bitcoin'un Yavaş Ortaya Çıkışı

<partId>7db760c0-dcce-4564-9c71-53873ee66d6d</partId>


## Bitcoin'ın Doğuşu

<chapterId>3d141918-e9c2-46e8-8c03-2bb4eb9b2150</chapterId>


Bitcoin'in nereden geldiğini öğrendikten sonra, tarihine odaklanacağız. Bu konu çok sayıda makale, podcast ve videoya konu olmuştur, öyle ki neredeyse bir kuruluş efsanesi haline gelmiştir. Gördüğümüz gibi, Bitcoin yaratıldığı bağlamdan ayrılamaz; aynı şey ilk yıllarında meydana gelen ve nitelikleri ve kusurlarıyla bugünkü halini şekillendiren olaylar için de geçerlidir.

Bitcoin, Japon olduğunu iddia eden bilinmeyen bir kişi olan Satoshi Nakamoto tarafından yaratıldı ve onu halka açıklamadan önce düşünceli bir şekilde tasarlamak için zaman ayırdı. Daha sonra, Bitcoin'nin en iyi koşullar altında piyasaya sürülmesini, tartışmalarda iyi bir şekilde sunulmasını ve artan sayıda insanın kullanmasını sağlamak için her şeyi yaptılar. Sonuçta, yaratıcının çabası, sistemin ilk tasarımında olduğu kadar, hatta daha fazla, ekonomik olarak başlatılmasında yatıyordu.


Bu bölüm 2008 sonbaharı ile 2009 kışı arasında gerçekleşen Bitcoin'ün doğuşunu ele almaktadır. Bu döneme iki önemli olay damgasını vurmuştur: sistemin teknik işleyişini açıklayan temel belge olan beyaz kitabın 31 Ekim 2008'de yayınlanması ve prototip ağın iki aydan biraz fazla bir süre sonra 9 Ocak 2009'da piyasaya sürülmesi. Bu nedenle, Satoshi Nakamoto'nun bu dönemdeki eylemlerine ve Bitcoin'ü ilk benimseyenler ve ilk karşı çıkanlarla olan az sayıdaki etkileşimine odaklanacağız.


### Keşif


Kendi](https://www.metzdowd.com/pipermail/cryptography/2008-November/014863.html) [ifadesine](https://bitcointalk.org/index.php?topic=13.msg46#msg46) göre, Satoshi Nakamoto 2007 baharında Bitcoin üzerinde çalışmaya başlamıştır. Dijital para birimleri üzerine çeşitli araştırmalar yaptıktan sonra, sonunda güvenilir bir üçüncü tarafa ihtiyaç duymadan Double-spending sorununu çözmenin bir yolunu buldu. Modelini bir yıldan fazla bir süre gizli tuttu ve sağlamlığını sağlamak için onu iyileştirmek istedi. Daha sonra [yazdığı] gibi (https://bitcointalk.org/index.php?topic=195.msg1617#msg1617):


> "Bir noktada, bunu hiç güven gerektirmeden yapmanın bir yolu olduğuna ikna oldum ve bu konuda düşünmeye devam etmekten kendimi alamadım. İşin büyük kısmı kodlamadan çok tasarımdı."

Doğru çalıştığından emin olmak için, Satoshi [programlandı] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html) teknik incelemeyi hazırlamadan önce bir prototip hazırladı. Bu yaklaşım, kavramların uygulamadan önce bilimsel makalelerde resmi olarak sunulduğu akademik toplulukta genellikle yapılanın tam tersidir. Bitcoin'un yaratıcısı [belirtmiştir](https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html):


> "Aslında bunu biraz tersten yaptım. Her problemi çözebileceğime kendimi ikna etmeden önce tüm kodu yazmam gerekti, sonra da makaleyi yazdım."

### Hazırlık


Ağustos 2008'de Satoshi, Bitcoin'in lansmanı için hazırlık yapmaya karar verdi. Ayın 18'inde anonim hizmet AnonymousSpeech aracılığıyla Bitcoin.org alan adını rezerve etti ([Netcoin.org](https://twitter.com/orweinberger/status/1573234325046558720)'un yanı sıra, muhtemelen konsepti için isim seçimini tamamlamamıştı). Bu alan adı ana Bitcoin sitesine ev sahipliği yapacaktı. Ancak Satoshi, daha sonra bir [spekülatör](https://mmalmi.github.io/Satoshi/#email-28) tarafından tutulan ve 2009 ile 2011 yılları arasında mikro ödemeler konusunda uzmanlaşmış Bitcoin Ltd. adlı bir şirket tarafından [kullanılacak](https://web.archive.org/web/20090719065532/http://www.Bitcoin.com/) olan Bitcoin.com alan adını rezerve edemedi.


20 Ağustos'ta Bitcoin'ün yaratıcısı Adam Back [https://s3.documentcloud.org/documents/24439625/adam-back-exhibit-ab1-1.pdf] ile temasa geçerek Hashcash ile ilgili makalesine beyaz kitapta nasıl atıfta bulunacağı konusunda tavsiye isteyen bir e-posta gönderdi. Bunu, Hashcash'in mucidinin yeni sisteminden haberdar olmasını sağlamak için bir bahane olarak görmemek Hard.


![Adam Back in 2012](assets/en/020.webp)

Adam Back 2012 yılında (kaynak: [Adam Back'in kişisel sayfası](http://www.cypherspace.org/adam/))


E-postada teknik raporun taslağına bir bağlantı yer alıyordu. PDF dosyasının adı `ecash.pdf`, başlığı ise "Güvenilir Üçüncü Taraf Olmadan Elektronik Nakit" idi Özet, Ekim ayında yayınlanacak olan ilk versiyonla tek kelimelik bir farkla aynı. Ne yazık ki belgenin tamamı elimizde bulunmamaktadır.

Satoshi'in özetini (ancak makaleyi değil) okuduktan bir gün sonra Adam Back onu Wei Dai'nin kendi konseptine benzer görünen b-para önerisine yönlendirir. Satoshi, Adam Back'e yönlendirmesi için teşekkür ederek ve "benim fikirlerim tam olarak bu noktadan başlıyor" diyerek yanıt verir Adam Back ayrıca MicroMint'in varlığından da bahseder, ancak Satoshi yanıt vermez.


Bundan bir gün sonra, 22 Ağustos'ta, Satoshi Wei Dai'ye bir e-posta göndererek "fikirlerinizi tam bir çalışma sistemine genişleten bir makale yayınlamaya hazırlandığını" söyler ve beyaz kitapta referans gösterebilmek için b-para ile ilgili sayfasının yayın yılını ister. Adam Back ile yaptığı Exchange'da olduğu gibi, beyaz kitabın taslağını Wei Dai ile paylaşır.


Bu etkileşimlere rağmen Adam Back ve Wei Dai, Satoshi'un konseptine hemen ilgi göstermedi. Bitcoin'e ancak yıllar sonra geri döneceklerdi: Wei Dai 2010-2011'de ve Adam Back 2013'te.


Satoshi ise buluşunu kamuoyuna duyurmak için hazırlıklarını tamamlar. 3 Ekim'de, artık ismi belirlenmiş olan Bitcoin beyaz kağıdının ilk versiyonunu tamamladı. 5 Ekim'de, açık kaynaklı yazılımın kaynak kodunun 2011 yılına kadar barındırılacağı ve korunacağı SourceForge proje yönetim platformuna kaydoldu.


### Beyaz kitabın yayınlanması


31 Ekim 2008'de Satoshi Nakamoto [beyaz kağıdın ilk versiyonunu] (assets/pdf/Bitcoin-20081003.pdf) kriptografiye adanmış ve kısaca "Kriptografi posta listesi" olarak adlandırılan bir e-posta listesinde yayınlar Bu liste 1996 yılından beri geliştirici Perry Metzger tarafından yönetilmektedir, [kuruluşu](https://cypherpunks.venona.com/date/1996/12/msg00102.html) ve [2003](https://www.metzdowd.com/pipermail/cryptography/2003-April/004484.html) yılından beri Metdowd.com adlı kişisel sitesinde barındırılmaktadır. Bu liste cypherpunks listesinin halefidir, tek farkı sıkı bir denetime tabi olmasıdır. 2008 yılında, John Gilmore, Hal Finney ve Len Sassaman gibi birkaç eski cypherpunks hala katılmıştır.


Listeye gönderdiği ilk [e-posta](https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html) adresinde Satoshi şöyle yazıyor:


> "Güvenilir bir üçüncü taraf olmadan, tamamen eşler arası çalışan yeni bir elektronik para sistemi üzerinde çalışıyorum."

Ayrıca modelinin temel özelliklerini de listelemektedir:



- "Double-spending eşler arası bir ağ ile engelleniyor."
- "Darphane veya diğer güvenilir taraflar yok."
- "Katılımcılar anonim olabilir."
- "Yeni birimler Hashcash tarzı bir Proof-of-Work'dan yapılmıştır."
- "Yeni üniteler üretmek için kullanılan Proof-of-Work, şebekenin Double-spending'yi önlemesini de sağlar."


E-postasında, halihazırda Bitcoin.org'da barındırılan beyaz kağıda bir bağlantı ekliyor. Bilimsel bir makale olarak sunulan 9 sayfalık bu kısa belge, Bitcoin'un teknik işleyişini anlatıyor ve çevrimiçi ödemeler sorununa odaklanıyor.


![Title and summary of the first version of the white paper (October 2008)](assets/en/021.webp)


Satoshi bu duyurunun ardından birkaç tepki aldı, ancak çoğu şüpheciydi. Özellikle üç şey için eleştirildi:



- İlk olarak, Cypherpunk James A. Donald [meydan okuyor](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) "gerekli boyuta ölçeklenmiyor gibi görünüyor" diyerek sistemin ölçeklenebilirliğini sorguluyor Satoshi [yanıtlar](https://www.metzdowd.com/pipermail/cryptography/2008-November/014815.html) "bant genişliği düşündüğünüz kadar engelleyici olmayabilir"
- İkinci olumsuz yorum ise *Internet for Dummies* kitabının yazarı ve e-posta altyapısı, spam filtreleme ve yazılım patentleri konularında uzmanlaşmış bir danışman olan John R. Levine'den geliyor. Levine, bilgisayar korsanları tarafından kontrol edilen bilgisayarlardan oluşan "zombi makine çiftliklerinin" sahip olduğu hesaplama gücünden bahsederek Bitcoin'ün güvenliğini [eleştiriyor] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014817.html). Özellikle internette "iyi adamların kötü adamlardan çok daha az hesaplama gücüne sahip olduğuna" dikkat çekiyor Satoshi [cevap veriyor] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014818.html) zekice: "Gereklilik, iyi adamların toplu olarak herhangi bir saldırgandan daha fazla hesaplama gücüne sahip olmasıdır."



- Son olarak, Ray Dillinger adlı bir kişi (ayı takma adını kullanarak) [hesap biriminin değerini merak eder](https://www.metzdowd.com/pipermail/cryptography/2008-November/014822.html), "hesaplamalı çalışma kanıtlarının içsel bir değeri olmadığı" gerçeğinden yakınır ve bilgisayar donanımının teknik evrimi nedeniyle enflasyonist doğalarını eleştirir. Satoshi [yanıtlar](https://www.metzdowd.com/pipermail/cryptography/2008-November/014831.html) "donanım hızındaki artış, üretim zorluğunun periyodik olarak ayarlanmasıyla" açıklanmaktadır.

Şüphecilik listedeki baskın tutum olsa da, e-posta listesine abone olan herkes tarafından paylaşılmıyor. Özellikle bir kişi coşkusuyla diğerlerinden ayrılıyor: Geleceğe iyimser bakan ve 90'lı yıllardaki başarısızlıklara rağmen elektronik para fikrinden asla vazgeçmeyen Hal Finney. Birkaç yıl sonra bu konuda "kriptografik gri sakallıların [...] sinik olma eğiliminde olduklarını" ancak kendisinin "kriptografiyi, gizemini ve paradoksunu her zaman sevdiği için" "daha idealist olduğunu" [belirtmiştir] (https://bitcointalk.org/index.php?topic=155054.msg1643833#msg1643833) (*orijinal: "Kriptografik gri sakallıların (ben 50'li yaşlarımın ortasındaydım) alaycı olma eğiliminde olduklarını fark ettim. Ben daha idealisttim; kriptoyu, gizemini ve paradoksunu her zaman sevdim. "*) Böylece, 7 Kasım'da listeye yazdığı bir [e-posta](https://www.metzdowd.com/pipermail/cryptography/2008-November/014827.html) ile "Bitcoin çok umut verici bir fikir gibi görünüyor" dedi ve Satoshi'nin modelini Nick Szabo'nun bit gold'u ile karşılaştırdı. (*orijinal: "Bitcoin çok umut verici bir fikir gibi görünüyor. "*)


![Hal Finney in 2007](assets/en/022.webp)

Hal Finney 2007 yılında


### Para Politikası ve Yazılım Kodu


Bitcoin, tüm ağ düğümlerinin, Hal Finney'in ilk e-postasında iki kelimeyle "blok zinciri" olarak bahsettiği bir Ledger'ün içeriği üzerinde anlaşmasına olanak tanıyan dağıtılmış bir mutabakat algoritması kullanır. Seçilen doğru Blockchain en fazla bloğa sahip olandır ve rakip bloklar üzerindeki çatışmalar bu basit ilkeye göre çözülür. Mekanizma [daha sonra] (https://sourceforge.net/p/Bitcoin/code/109/) blok sayısı yerine biriken iş miktarını hesaba katacak şekilde geliştirilecektir.


Bu mutabakat mekanizması, sistem içinde her türlü kural ve teşvikin (beyaz bültenin son cümlesini kullanmak gerekirse) uygulanmasına izin verir. Bitcoin dağıtılmış bir zaman damgası hizmeti oluşturduğundan, bu kuralların zamanla etkileşime girmesi de mümkündür. Dolayısıyla, yeni blokların ve ilgili bitcoinlerin üretimini düzenlemek için devreye giren zorluk ayarlama algoritması: belirli bir süre içinde üretilen blok sayısı çok yüksekse, üretim zorluğu artar; tersi durumda ise azalır. Dolayısıyla Bitcoin, çalışma kanıtlarının hesap birimlerini oluşturduğu RPOW'dan farklıdır.

Bu zorluk ayarı sayesinde, Bitcoin bir para politikasına sahip olabilir, yani protokol tarafından verilen yeni birimlerin miktarı önceden belirlenebilir. Başlangıçta, üretici düğümleri bilgi işlem güçlerini ağa katkıda bulunmaya teşvik etmek için parasal ihracın sabit olması planlanmaktadır ve herhangi bir işlem ücreti yoktur. Satoshi Nakamoto'nun [white paper]'ın "Teşvik" bölümünde yazdığı gibi (assets/pdf/Bitcoin-20081003.pdf):

> "Sabit miktarda yeni madeni paranın sürekli olarak eklenmesi, altın madencilerinin dolaşıma altın eklemek için kaynak harcamasına benzer."

Satoshi tarafından [e-posta listesinde](https://www.metzdowd.com/pipermail/cryptography/2008-November/014831.html) ve [özel yazışmalarında](https://mmalmi.github.io/Satoshi/#email-3) teyit edilen bu özellik James A. Donald'ın gözünden kaçmıyor. 9 Kasım'da, "kimin neye sahip olduğunu izleme işini" (yani Mining'i) "senyorajla ödendiği" ve "enflasyon gerektirdiği" için [eleştiriyor](https://www.metzdowd.com/pipermail/cryptography/2008-November/014837.html), ancak "öngörülebilir enflasyonun, serveti bir oy bloğundan diğerine aktarmak için zaman zaman sallanan enflasyondan daha az sakıncalı olduğunu" belirtiyor (*orijinal: "Önerilen sistemde kimin hangi madeni paraya sahip olduğunu takip etme işi senyorajla ödeniyor, bu da enflasyon gerektiriyor. Bu kabul edilemez bir kusur değildir - öngörülebilir enflasyon, serveti bir oylama bloğundan diğerine aktarmak için zaman zaman sallanan enflasyondan daha az sakıncalıdır. "*) Ayrıca, "umursamadığı tüm harcamaları görmezden gelen" bir Mining düğümünün "hiçbir olumsuz sonuca" maruz kalmadığını [not ediyor] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014841.html) ve böylece sansür sorununu vurguluyor. (*orijinal: "Eğer bir düğüm önemsemediği tüm harcamaları görmezden geliyorsa, hiçbir olumsuz sonuçla karşılaşmaz. "*)


Bu açıklamalar muhtemelen Satoshi'nın, yeni birimlerin oluşturulmasının yerini alarak ve madencileri "aldıkları tüm ödeme işlemlerini dahil etmeye" [teşvik ederek](https://www.metzdowd.com/pipermail/cryptography/2008-November/014843.html) her iki sorunu da çözen bir [işlem ücreti mekanizması](https://www.metzdowd.com/pipermail/cryptography/2008-November/014842.html) uygulayabileceğini fark etmesini sağladı (*orijinal: "düğümler aldıkları tüm ödeme işlemlerini dahil etmek için bir teşvike sahip olacaktır. "*)


Aynı zamanda, muhataplarından gelen sorular onu modelinin kaynak kodunu paylaşmaya sevk etti. Satoshi, 16 Kasım'da kodu Hal Finney, James A. Donald ve Ray Dillinger'a iletti. Ayın 17'sinde, James A. Donald'a posta listesinde yanıt olarak, [yazdı] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014863.html) ona "şu anda istek üzerine mevcut olan" "ana dosyaları" gönderdiğini ve "tam sürümlerinin" "yakında" gerçekleşeceğini söyledi (*orijinal: "I sent you the main files. &nbsp;(available by request at the moment, full release soon) "*) 2013 yılında Ray Dillinger tarafından [kamuya açıklanan](https://bitcointalk.org/index.php?action=printpage;topic=382374.0) kodun bu kısmında, Bitcoin'un tüm temel Elements'larının mevcut olduğu görülebilir: Blockchain (o zamanlar hala "timechain" olarak adlandırılıyordu), Proof of Work, Coin temsil modeli (UTXO), işlem programlanabilirliği, işlem ücretleri ve Halving.


Bununla birlikte, bazı parametreler farklılık göstermekte olup, bunların kendiliğinden veya [Satoshi'nın yazdığı gibi] (https://plan99.net/~mike/Satoshi-emails/thread1.html) "eğitimli tahmin" ile seçildiğini göstermektedir (*orijinal: "eğitimli tahmin "*) Her blok arasında hedeflenen süre olan blok süresi 10 yerine 15 dakikadır. Zorluk ayarlama süresi 2,016 blok (10 dakikalık bir blok süresi için 14 güne karşılık gelir) yerine 2,880 bloktur (15 dakikalık bir blok süresi için 30 güne eşdeğerdir). GetBlockValue` işlevinde bulunan Halving mekanizması, Halving'in her 100.000 blokta bir, yani kabaca 2 yıl 311 günde bir gerçekleşmesi gerektiğini belirtir:


```cpp
int64 GetBlockValue(int64 nFees)
{
int64 nSubsidy = 10000 * CENT;
for (int i = 100000; i <= nBestHeight; i += 100000)
nSubsidy /= 2;
return nSubsidy + nFees;
}
```


İlk 100.000 blok döneminde 100 bitcoin, ikinci dönemde 50 bitcoin vs. yaratılmış, böylece toplam bitcoin sayısı 20 milyona yaklaşmıştır. Her bir Bitcoin (Coin), 10.000 temel birime bölünebilen 100 sente (CENT) bölünebilir. Böylece bir Bitcoin, Ocak ayında yayınlanan 0.1 sürümündeki gibi 100 milyona değil, 1 milyon daha küçük birime bölünebilmektedir.


Hal Finney ve Ray Dillinger daha sonra kod üzerinde kapsamlı bir inceleme gerçekleştirdiler. Her biri sistemin belirli bir bölümüne odaklandı: Ray Dillinger mutabakat kısmıyla ilgilenirken, Hal Finney komut dosyası sistemini inceledi. 10 Aralık'ta Satoshi, SourceForge üzerinde barındırılan Bitcoin-list posta listesini [oluşturdu](https://web.archive.org/web/20131016004654/http://sourceforge.net/p/Bitcoin/mailman/Bitcoin-list/?viewmonth=200812). Bu liste, ilgilenen kişilerden yıllar içinde birkaç e-posta gönderilmesine rağmen çok az başarı elde etti. Yine de tüm bunlar, bir ay sonra, 2009'un başında gerçekleşecek olan prototipin lansmanı için her şeyin hazır olduğunu göstermektedir.


### Yazılım Yayını ve Ağ Lansmanı


8 Ocak 2009, saat 19:27'de Satoshi Nakamoto yazılımın ilk sürümünü (0.1.0 numaralı) Metzdowd.com posta listesinde yayınladı. C++ kaynak kodu MIT lisansı altında açık olarak yayınlandı, böylece herkes istediği gibi kopyalayabilir, değiştirebilir ve kullanabilirdi. Özellikle Genesis blok verilerini içerir, bu da zincirin ilk bloğudur ve ikincisinin uzaması gerekir. Yazılım yalnızca Windows üzerinde çalışmaktadır. Satoshi, [email](https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html) adresindeki duyurusunda şöyle yazmıştır:


> "Double-spending'ü önlemek için eşler arası bir ağ kullanan yeni bir elektronik para sistemi olan Bitcoin'ün ilk sürümünü duyuruyoruz. Hiçbir sunucu veya merkezi otorite olmadan tamamen merkezi olmayan bir sistemdir."

"Yazılımın hala alfa ve deneysel aşamada olduğunu" ve "gerekli olması halinde sistemin bir noktada yeniden başlatılmasının gerekmeyeceğinin garantisi olmadığını" belirtiyor (*orijinal: "Yazılım hala alfa ve deneysel aşamadadır. Gerekli olması halinde sistemin durumunun bir noktada yeniden başlatılması gerekmeyeceğinin garantisi yoktur "*) Bitcoin elde etmenin iki yolu vardır: başka birinden para alarak veya bir CPU kullanarak Coin üretimini etkinleştirerek. Birim göndermenin de iki yolu vardır: alıcının IP Address'ini kullanarak veya ödemeyi çevrimdışı göndermeye olanak tanıyan bir Bitcoin Address aracılığıyla. Son olarak, e-postada Bitcoin'nın bir sonraki bölümde tartışacağımız nihai para politikası açıklanmaktadır.

Yayınlanan kod sunulandan biraz daha karmaşıktır ve gelecekte bitcoin transferinden daha fazla işlevselliğe izin verecek bir Interface'in geliştirilmesi için yazılmıştır. Satoshi gerçekten de "eBay tarzı bir pazar yerinin" (*orijinal: "istemcide yerleşik bir eBay tarzı pazar yeri "*) temellerini istemciye [entegre etmiştir](https://plan99.net/~mike/Satoshi-emails/thread4.html) ve bu da [herkesin Exchange para birimini sunmasını kolaylaştırabilir](https://plan99.net/~mike/Satoshi-emails/thread1.html) (*orijinal: "herkesin Exchange para birimini sunmasını kolaylaştırır "*). Kod ayrıca doğrudan yazılım içinde bir poker uygulamasının potansiyel kurulumuna adanmış [bazı fonksiyonlar](https://github.com/trottier/original-Bitcoin/blob/4184ab26345d19e87045ce7d9291e60e7d36e096/src/uibase.cpp#L1573-L1731) içermektedir. Online poker 2003 yılından bu yana Amerika Birleşik Devletleri'nde fantastik bir patlama yaşıyordu ("Moneymaker etkisi" sayesinde) ancak 2006 yılında [Yasadışı İnternet Kumar Uygulama Yasası](https://www.pgt.com/news/what-if-poker-wasnt-part-of-the-uigea-back-in-2006)'nın kabul edilmesinin ardından bir tür finansal sansüre kurban gitti, bu da bu eklemeyi açıklıyor.


Duyurudan birkaç saat sonra, 8 Ocak'ı 9 Ocak'a bağlayan gece, Satoshi madencilik yapmaya başladı. Zincirin ikinci bloğu olan Blok 1'i 9 Ocak günü saat 2:54'te doğruladı. Bu bloğun üretimi ağın etkin bir şekilde başlatıldığına işaret ediyor ve ilerleyen saatlerde zincire başka halkalar da ekleniyor.


Bu yapıldıktan sonra, Satoshi bu lansman hakkında iletişim kurduğu çeşitli kişileri bilgilendirmeyi kendine görev edinir. Saat 5:21'de Hal Finney'e bir [e-posta] (https://www.coindesk.com/markets/2020/11/26/previously-unpublished-emails-of-Satoshi-nakamoto-present-a-new-puzzle/) göndererek "EXE ve tam kaynak kodlu Bitcoin v0.1 sürümünün Sourceforge'da mevcut olduğunu" bildirir (*orijinal: "the Bitcoin v0.1 release with EXE and full sourcecode is up on Sourceforge "*) Ertesi gün Adam Back ve Wei Dai ile iletişime geçerek onlara kişiselleştirilmiş bir e-posta gönderir. Bu son e-postalarda özellikle Hal Finney tarafından posta listesinde yayınlanan ve Proof of Work ve b-money'den bahseden bir açıklamaya yer verir.


10 Ocak'ta Hal Finney yazılımın çalıştırılabilir dosyasını çalıştırmayı denedi ancak bilgisayarını çökerten teknik bir sorunla karşılaştı. Kendisiyle [iletişime geçildi](https://web.archive.org/web/20140821141611/http://sourceforge.net/p/Bitcoin/mailman/message/21295694/) Satoshi ve bu konuda kendisiyle görüş alışverişinde bulunmaya başladı. Tüm zorluklara rağmen Hal Finney yazılımı çalıştırmayı başardı. Ocak ayının 10'unu 11'ine bağlayan gece saat 1'de ilk bloğunu ([blok 78](https://Mempool.space/block/00000000a2886c95400fd3b263b9920af80b118b28fee5d2a162a18e4d9d8b2f)) buldu ve böylece 50 bitcoin kazandı. Bir saat sonra, *Cryptography posta listesine* bir [övgü e-postası](https://www.metzdowd.com/pipermail/cryptography/2009-January/015004.html) göndererek Satoshi'i alfa sürümünün yayınlanması nedeniyle tebrik etti ve hesap biriminin para politikasını vurguladı. Son olarak, saat 03:33'te, deneyimini Twitter'da (o zamanlar yeni gelişmekte olan bir sosyal ağ) "\[r\]unning \[B\]itcoin" olduğunu belirterek [paylaştı] (https://twitter.com/halfin/status/1110302988). Bu, Bitcoin hakkındaki ilk tweet'tir.


Satoshi ve Hal Finney arasındaki bu yazışmalardan, 12 Ocak'ta [yayınlanan](https://web.archive.org/web/20171124135217/https://sourceforge.net/p/Bitcoin/mailman/message/21313152/) ve öncekilerden çok daha kararlı olan 0.1.3 sürümü ortaya çıktı. Satoshi ayrıca Hal Finney ile yaptığı görüşmeden yararlanarak ona biraz bitcoin verdi: 11 Ocak'ı 12 Ocak'a bağlayan gece saat 03:30'da Address IP'si üzerinden ona 10 bitcoin [gönderdi](https://Mempool.space/tx/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16). Bu, ağ üzerinde bir kişiden diğerine yapılan ilk transferdi.

Ancak Hal Finney o dönemde Bitcoin'ü deneyen tek kişi değildir. O sıralarda dijital para birimleriyle (ve özellikle de Liberty Dollar'ın elektronik versiyonuyla) ilgilenen Amerikalı bilgisayar güvenliği araştırmacısı Dustin D. Trammell de Bitcoin'ü e-posta listesi aracılığıyla keşfetmiştir. 11 Ocak'ta yazılımı iş makinelerinden birinde çalıştırır (ancak teknik bir sorun nedeniyle ilk [blok](https://Mempool.space/block/00000000d3ec2f50772c2d42d4afb054c283555766a0ca1d8da65b9b5058a49e) madenciliğini ayın 13'üne kadar yapmaz). 11'i 12 Ocak'a bağlayan gece boyunca Satoshi ile yoğun bir şekilde temasa geçer ve sonraki günlerde onunla [iletişim](https://www.dustintrammell.com/s/Satoshi_Nakamoto.zip) kurar. 15 Ocak'ta Dustin Trammell ondan da 25 bitcoin [alır](https://Mempool.space/tx/d71fd2f64c0b34465b7518d240c00e83f6a5b10138a7079d1252858fe7e6b577).


![Dustin Trammell](assets/en/023.webp)

Dustin Trammell (kaynak: [Dustin Trammell'in blog arşivi](https://web.archive.org/web/20100419181845/http://blog.dustintrammell.com/))


Daha sonra, diğer insanlar yazılımı çalıştırmayı dener. İngiliz avukat Nicholas Bohm, teknik bir sorunla karşılaştığı için 25 Ocak'ta Bitcoin listesine bir e-posta gönderdi ve Satoshi ile özel olarak görüştü. Jeff Kane adında biri 30 Ocak'ta 0.1.3 sürümünü çalıştırmayı başardı. Nicholas Bohm, Şubat ayı başında yayınlanacak olan yazılımın 0.1.5 versiyonunun jeneriğinde Dustin Trammell ile birlikte anılacak.


9 Ocak 2009'dan bu yana ağ durmadı. Bloktan sonra blok, zincir uzamaya devam edecek. Ve Bitcoin sonunda başarıya ulaşacaktır.


### İlerici Bir Tasarım


Bitcoin'nin tasarımına ilişkin bu anlatımdan çıkarabileceğimiz şey, bunun aşamalı olarak gerçekleştiğidir. İlk fikrin ortaya atıldığı 2007 baharı ile ağın fiilen faaliyete geçtiği 2009 kışı arasında bir buçuk yıldan fazla bir süre geçmiştir. Dahası, 31 Ekim 2008 tarihinde beyaz bültenin ilk versiyonunun yayınlanmasından sonra ortaya çıkan para politikası ve işlem ücreti mekanizmasında gördüğümüz gibi, modelin bazı Elements'ları evrim geçirmiştir.


Ancak bu çalışma yetersizdi ve sistemini başlatmak için Satoshi'nin azmi gerekti. Başından beri, çok az kişinin modelini ciddi olarak değerlendirdiğini ve yeni kullanıcıları ve katkıda bulunanları çekmenin karmaşık olacağını biliyordu. Bu nedenle generate, fikrini elinden geldiğince iyi satarak heyecan yaratmaya çalıştı. Bu konuyu 2009 yılının büyük bir kısmını kapsayan bir sonraki bölümde inceleyeceğiz.


## Dünyaya Sunum

<chapterId>28be3515-d9da-4d91-b7ff-f8691d51c562</chapterId>


Bitcoin'ün Satoshi Nakamoto tarafından nasıl tasarlandığını ve başlatıldığını inceledikten sonra, kamuya nasıl sunulduğuna odaklanalım. 2009'un başındaki lansmanının ardından ağ faaliyete geçti. Yine de, az sayıda üretici düğüm vardı (blokların çoğunu Satoshi çıkardı) ve faaliyet neredeyse hiç yoktu (Ocak ayı boyunca 32 gerçek işlem gerçekleşti). Projenin yalnızca basit bir web sitesi ve yazılımı indirmek için bir SourceForge sayfası vardı. Dahası, Bitcoin hakkındaki iletişim Metzdowd Cryptography e-posta listesiyle sınırlıydı ve bu listeyi en iyi ihtimalle kriptografi konusunda tutkulu birkaç yüz kişi takip ediyordu.


Bu nedenle, bu dönemin zorluğu Bitcoin'i tanıtarak amaca bir şekilde katkıda bulunabilecek kritik bir kullanıcı kitlesini çekmekti. Bu yüzden Satoshi siteyi geliştirmeye ve çeşitli insanlarla etkileşim kurmaya öncelik verdi. Keşfini dünyaya duyurmak istiyordu.


Bu bölümde, Satoshi'nin bankacılık sistemine ve 21 milyon limitine olan güvensizliği gibi iletişim çabalarından ortaya çıkan kültürel kodları inceleyeceğiz. Ayrıca Satoshi'nin icadını savunmak için muhalifleriyle yaptığı konuşmaları da yorumlayacağız. Son olarak, başkalarından aldığı yardımlardan, özellikle de ilk sağ kolu Martti Malmi'nin önemli yardımlarından bahsedeceğiz.


### Genesis Bloğu


Ocak 2009'daki lansman Satoshi Nakamoto'nun sisteminin sabit parametrelerini oluşturmasına olanak sağladı. Daha sonra [yazacağı] (https://bitcointalk.org/index.php?topic=195.msg1611#msg1611) gibi, Bitcoin'ın doğası gereği "0.1 sürümü yayınlandıktan sonra" temel işleyişi "varlığının geri kalanı için taşa oturtulmuştu" ve bu da sistem genişlemeden önce her şeyin doğru yapılmasını gerekli kılıyordu. (*orijinal: "once version 0.1 was released, the core design was set in stone for the rest of its lifetime "*) Özellikle iki temel Elements önemli kültürel öneme sahiptir: Genesis bloğunun içeriği ve 21 milyon birimlik sınır.


Genesis bloğu, genişletilmesi gereken Bitcoin Blockchain'ün temel bloğudur. Bu nedenle yazılıma sabit olarak kodlanmıştır. Ağı başlatmadan önce Satoshi, gerekli Proof of Work'ü üreterek ve 3 Ocak 2009, 18:15:05 UTC'de zaman damgası vurarak ilk bağlantıyı kurmuştur. Bu blokta (ve özellikle ödül işleminde) aşağıdaki mesajı yazmıştır:


```
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```


Bu, İngiliz *The Times* gazetesinin o günkü manşetidir ve Maliye Bakanı'nın (yani İngiliz maliye bakanının) bankaları ikinci kez kurtarmanın eşiğinde olduğunu göstermektedir. Bu manşetin blokta yer alması ikili bir role hizmet etmektedir:



- Bir yandan, Satoshi'in gazete yayınlanmadan önce manşetten haberdar olamayacağı için sistemin 3 Ocak'tan önce başlatılamayacağını kanıtlayarak ağın başlatılmasının geriye götürülmesini engellemektedir;
- Öte yandan, dönemin parasal ve finansal bağlamına atıfta bulunarak Bitcoin'un neye karşı durduğunu sembolik olarak göstermektedir.


![The Times: Chancellor on brink of second bailout for banks](assets/en/024.webp)


O dönemde dünya, 2007 yılında Amerika Birleşik Devletleri'nde subprime balonunun patlamasıyla başlayan mali krizin tüm etkilerini hissediyordu. Hükümetler, yatırım bankası Lehman Brothers'ın 15 Eylül 2008'de batmasının ardından daha fazla iflasın önüne geçmek için finansal kurumları kurtardı ve merkez bankaları finansal piyasalara likidite enjekte ederek niceliksel gevşemeye gitti. Bu vesileyle yaratılan kamu parasının kullanımı, bankacılık sisteminin aslında özel karlar ve toplumsallaştırılmış zararlardan oluştuğunu fark eden bir dizi vatandaşı tedirgin etti.


Öte yandan, Bitcoin güvenilir bir üçüncü tarafa dayanmaz ve bu nedenle bir merkez bankasının kaprislerine tabi değildir. Bu nedenle, miktarı para yaratmayı kontrol edenler tarafından keyfi olarak değiştirilebilen dolar veya euro gibi devlet para birimleriyle tezat oluşturmaktadır; Bitcoin'in para politikası gerçekten de önceden programlanmış, protokole yazılmış ve teorik olarak asla değiştirilemeyecek şekildedir.


### 21 Milyon Sınırı


Bu da bizi Satoshi tarafından ağın lansman gününde sunulan ikinci unsura getiriyor: 21 milyon sınırı. 8 Ocak'ta [tanıtım e-postasında] (https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html) bu para politikasını şu şekilde tanımladı:


> "Toplam dolaşım 21.000.000 birim olacaktır. Bunlar, blok oluşturdukça ağ düğümlerine dağıtılacak ve her 4 yılda bir verilen miktar Halving olacaktır.
>

> ilk 4 yıl: 10.500.000 adet
> önümüzdeki 4 yıl: 5.250.000 adet
> önümüzdeki 4 yıl: 2.625.000 adet
> önümüzdeki 4 yıl: 1.312.500 adet
> vs.
>

> bu tükendiğinde sistem gerekirse işlem ücretlerini destekleyebilir. Sistem açık piyasa rekabetine dayanıyor ve düğümler muhtemelen her zaman işlemleri ücretsiz olarak gerçekleştirmeye istekli olacaktır."

Birkaç gün sonra Hal Finney e-posta listesinde bu para politikasına olumlu tepki verdi] (https://www.metzdowd.com/pipermail/cryptography/2009-January/015004.html) ve "sistemin yalnızca belirli bir maksimum sayıda birimin üretilmesine izin verecek şekilde yapılandırılabileceği" gerçeğinden heyecan duydu E-postasında, Bitcoin'ün "dünya çapında kullanılan baskın ödeme sistemi" haline gelmesi durumunda, her bir birimin "yaklaşık 10 milyon dolarlık bir değere" sahip olacağını tahmin etti "Bugün birkaç sentlik hesaplama süresiyle birim üretme olasılığının" "çok iyi bir bahis" olabileceğini yazdı Tahmin tartışmalı olsa bile (Bitcoin'ün toplam küresel servete eşdeğer bir değerlemesine dayandığı için), mantık sağlamdır.


16 Ocak'ta Satoshi, e-posta listesiyle paylaştığı bir e-postada bu "uzun vadeli yatırım" fikrini yeniden ele aldı ve potansiyel kullanım durumlarını açıkladı. Kendisi] (https://www.metzdowd.com/pipermail/cryptography/2009-January/015014.html) "tutması ihtimaline karşı biraz almanın mantıklı olabileceğini belirtti. Yeterli sayıda insan aynı şekilde düşünürse, bu kendi kendini gerçekleştiren bir kehanet haline gelir." Bu iddiasını bir ay sonra [yineledi](https://p2pfoundation.ning.com/xn/detail/2003008:Comment:9562) ve sınırlı sayıda birimin "ne kadar çok kullanıcı olursa, değer o kadar artar ve bu da artan değerden faydalanmak isteyen daha fazla kullanıcıyı çekebilir" anlamında bir "pozitif geri besleme döngüsü" yaratmasının muhtemel olduğunu açıkladı Dolayısıyla, spekülatif unsur en başından beri mevcuttur ve sistemi başlatmayı amaçlamaktadır.


### Düzenleme, Zombi Ağları ve Ekoloji


Bunun ardından, e-posta listesinde başka bir tartışma gelişti. Satoshi bir kullanım örneği olarak spam sınırlamasından bahsetti ve bu da çeşitli katılımcıların tepkilerine yol açtı. Bitcoin'in yaratıcısı bu eleştirilere özel olarak yanıt vermeyi tercih etti, ancak Hal Finney kamuoyunda itiraz etmeyi kendine görev edindi. RPOW ile kendi dijital para birimini geliştirmeyi denediğinde bu konular üzerinde düşünmek için zamanı oldu.

İlk olarak, düzenleme ve hükümetlerin Bitcoin'yi potansiyel olarak yasaklaması sorunu ortaya çıkmaktadır. Bu konu, Bloomington'daki Indiana Üniversitesi'nin astronomi bölümünde araştırmacı olan ve e-posta listesinin müdavimlerinden Jonathan Thornburg tarafından [gündeme getirilmiştir] (https://www.metzdowd.com/pipermail/cryptography/2009-January/015016.html). Satoshi tarafından önerilen kullanım durumlarına yanıt veren e-postasında, küresel finansal gözetim durumunu özetliyor. Bitcoin'nin yetkililerin tolere ettiği eşiğin üzerindeki miktarların transferine izin verebileceğini belirtiyor. Akıl yürütmesinin mantıksal sonucu, "hiçbir büyük hükümetin Bitcoin'nin mevcut haliyle büyük ölçekte çalışmasına izin vermeyeceğidir."


Bu soru, 21 Ocak'ta "Bitcoin'a daha fazla anonimlik eklemenin yollarını arıyorum" şeklinde bir [tweet] (https://twitter.com/halfin/status/1136749815) yazan Hal Finney'in ilgisini çekiyor Ardından 24'ünde Jonathan Thornburg'a [yanıt] (https://www.metzdowd.com/pipermail/cryptography/2009-January/015036.html) yazarak "Kesinlikle geçerli bir nokta ve elektronik parayla ilgili yıllar boyunca yapılan tartışmalarda yaygın olarak tartışılan bir nokta. Bitcoin'un birkaç avantajı var: Birincisi, dağıtılmış olması, tek bir hata noktası olmaması, 'darphane' olmaması, mahkeme celbi gönderilebilecek, tutuklanabilecek ve kapatılabilecek memurları olan bir şirket olmaması."


Ardından, aynı e-postada Jonathan Thornburg, Satoshi'nin vurguladığı kullanım durumuna atıfta bulunarak, "ücretli e-posta filtrelerini atlatabilen" zombi bilgisayar ağları konusunu tartışıyor. Satoshi [ona özel olarak cevap verdi](https://mmalmi.github.io/Satoshi/#email-3) ve bu durumda "gönderme başına ödemeli e-posta adresleri kurarak ve tüm spam parasını toplayarak iyi bir kazanç elde edilebileceğini" açıkladı ve bu görüşünü ayın 25'inde listeye [aktardı](https://www.metzdowd.com/pipermail/cryptography/2009-January/015041.html). Öte yandan Hal Finney, Proof of Work'in "öncelikle işlem geçmişi veri tabanının güvenilirliğini sağlamayı amaçladığını" hatırlatıyor Proof-of-Work jetonlarının faydalı olması halinde makinelerin artık atıl kalmayacağını ve parazitliğin azalacağını da sözlerine ekliyor.


Son yorum ise cypherpunks'ın kurucu üyelerinden ve 1992'den 1997'ye kadar hareketin ilk e-posta listesinin koruyucusu olan John Gilmore'dan geliyor. Gilmore, 25 Ocak'ta gönderdiği bir e-postada, Bitcoin'ün sözde ekolojik sonuçlarını vurguluyor ve [yazıyor](https://www.metzdowd.com/pipermail/cryptography/2009-January/015042.html) "İhtiyacımız olan son şey, e-postaları veya spam'leri iletmek için küçük miktarlarda bitbux üretmek üzere tüm mevcut döngüleri yakmak, elektrik tüketmek ve karbondioksit üretmek üzere tasarlanmış bir sistemi İnternet'in her yerine yerleştirmektir." Satoshi [yanıtlar] (https://mmalmi.github.io/Satoshi/#email-3) ona özel olarak "ekonomik özgürlük ve çevre koruma arasında seçim yapmak zorunda kalmanın ironik olacağını" söyler "Proof of Work'ün eşler arası bir elektronik para sisteminin çalışması için bulduğu tek çözüm olduğunu" ve çok fazla enerji tüketecek olsa bile "yine de yerini alacağı emek ve kaynak yoğun geleneksel bankacılık faaliyetinden daha az israf edeceğini" ekliyor


![John Gilmore in 2007](assets/en/025.webp)

John Gilmore 2007 yılında (kaynak: [Flickr](https://www.flickr.com/photos/35034362831@N01/2115939762/))


Ayın 27'sinde Hal Finney, Proof of Work'nın hesaplanmasıyla ilişkili enerji dağılımını azaltmanın yollarından [bahsediyor](https://www.metzdowd.com/pipermail/cryptography/2009-January/015056.html). Bir saat sonra, Twitter'da](https://twitter.com/halfin/status/1153096538) "yaygın bir Bitcoin uygulamasından kaynaklanan CO2 emisyonlarını nasıl azaltabileceğimizi düşünüyorum" diye yazıyor

Bir başka destekçi de o sırada Tahoe-LAFS üzerinde çalışan Cypherpunk Zooko Wilcox-O'Hearn'den geliyor. Bu dosya paylaşım sistemi, 2000'li yılların başında popüler olan bir proje olan [Mojo Nation]'ın (https://www.salon.com/2000/10/09/mojo_nation/) halefidir. 26 Ocak'ta, e-posta listesindeki tartışmada, aynı gün blogunda yayınladığı ve çeşitli dijital para projelerinden (DigiCash, bit gold, b-money) bahsettiği ve Bitcoin'u övdüğü "[Decentralized Money](https://web.archive.org/web/20090303195936/http://testgrid.allmydata.org:3567/uri/URI:DIR2-RO:j74uhg25nwdpjpacl6rkat2yhm:kav7ijeft5h7r7rxdp5bgtlt3viv32yabqajkrdykozia5544jqa/wiki.html#%5B%5BDecentralized%20Money%5D%5D)" başlıklı bir yazının bağlantısını paylaştı. Özellikle şöyle yazıyor:


> "Benim istediğim, herkesin ucuz ve rahat bir şekilde kullanabileceği, ancak **kimsenin** manipüle etme gücüne sahip olmadığı bir para birimi. Kimsenin Supply para birimini şişirme ya da söndürme gücü yok, kimsenin işlemleri izleme, vergilendirme ya da engelleme gücü yok. Altının evrensel para birimi olduğu zamanlarda ve yerlerde, gerçekten de altının dijital eşdeğeri."

Bu metnin bir bağlantısı birkaç hafta sonra Bitcoin.org'a [eklendi](https://web.archive.org/web/20090303195936/http://Bitcoin.org/). Ve Satoshi bu küçük yardım için bir buçuk yıl sonra Zooko'ya şahsen teşekkür etti](https://bitcointalk.org/index.php?topic=890.msg10723#msg10723).


### Peer-to-Peer ve Merkez Bankalarına Güvensizlik


Söylediğimiz gibi, Satoshi'ün iletişimi başlangıçta Kriptografi posta listesiyle sınırlıyken, daha sonra başka ufuklara doğru genişledi. Şubat 2009'da, 2007'de kurulan ve eşler arası altyapıların toplum üzerindeki etkisini inceleyen bir kuruluş olan P2P Vakfı'nın forumuna ve posta listesine katıldı. Her zaman kendi modelini tanıtma niyetinde olan birkaç üyesiyle etkileşime girdi.

11 Şubat'ta Satoshi, forumda (p2pfoundation.ning.com) Bitcoin'i tanıtan bir [tanıtım mesajı] (https://p2pfoundation.ning.com/forum/topics/Bitcoin-open-source) yayınladı ve e-posta yoluyla listeye (P2P-research) bir [kopya] (https://diyhpl.us/~bryan/irc/Bitcoin-Satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February/001347.html) gönderdi. Bu metinde şunları yazmıştır:


> "Geleneksel para biriminin temel sorunu, işlemesi için gereken tüm güvendir. Merkez bankasına paranın değerini düşürmemesi için güvenmeliyiz, ancak itibari para birimlerinin tarihi bu güvenin ihlal edilmesiyle doludur. Bankalara paramızı tutmaları ve elektronik olarak transfer etmeleri konusunda güvenmeliyiz, ancak onlar paramızın çok az bir kısmını rezervlerinde tutarak kredi balonu dalgaları halinde borç veriyorlar. Gizliliğimizi korumaları, kimlik hırsızlarının hesaplarımızı boşaltmasına izin vermemeleri için onlara güvenmek zorundayız. Önemli genel giderleri mikro ödemeleri imkansız kılıyor."

Profilinde] (https://p2pfoundation.ning.com/profile/SatoshiNakamoto) Japon olduğunu iddia ediyor ama hepsi bu kadar değil. 2011'de yapılan bir Interface güncellemesi yaşını ortaya çıkardı: 35 yaşında, yani 2009'da 32 ya da 33 yaşındaydı. Ardından, 2014 yılında, belirli bir doğum tarihi belirttiği [keşfedildi](https://www.reddit.com/r/Bitcoin/comments/229qvr/happy_birthday_satoshi_nakamoto/): 5 Nisan 1975. Görünüşte zararsız olan bu tarih muhtemelen 1933-1975 yılları arasında Amerika Birleşik Devletleri'nde Amerikan vatandaşlarının altın sahibi olmalarının yasaklanmasına bir göndermedir. 5 Nisan günü, bu yasağın Başkan Franklin Delano Roosevelt tarafından 5 Nisan 1933 tarihinde imzalanan [Executive Order 6102] (https://www.presidency.ucsb.edu/documents/executive-order-6102-forbidding-the-hoarding-gold-Coin-gold-bullion-and-gold-certificates) ile tesis edildiği güne, 1975 yılı ise [Public Law 93-373] (https://www.govtrack.us/congress/bills/93/s2665/text) ile yürürlükten kaldırıldığı güne tekabül etmektedir. Bu ayrıntı çok önemlidir çünkü bu yasak klasik altın standardını (temsili bir banknot karşılığında Exchange cinsinden altın elde edilebildiği) sona erdirmiş, doların devalüasyonuna (1934'teki Altın Rezerv Yasası aracılığıyla) izin vermiş ve 1971 Nixon Şoku'nun ardından bildiğimiz dalgalı Exchange kuru parasal rejiminin kurulmasını kolaylaştırmıştır.

![Satoshi Nakamoto's profile on the P2P Foundation forum, captured on March 17, 2011](assets/en/026.webp)


Satoshi Nakamoto'nun 17 Mart 2011 tarihinde P2P Vakfı forumundaki profili (kaynak: [forum yakalama](https://web.archive.org/web/20110317060514/http://p2pfoundation.ning.com:80/profile/SatoshiNakamoto))


Satoshi'in iletişiminde değerli metallere yapılan tek atıf bu değildir. Bitcoin'ün yaratıcısı 18 Şubat'taki yorumlarda](https://p2pfoundation.ning.com/forum/topics/Bitcoin-open-source?commentId=2003008:Comment:9562) yazıyor:


> "Sepp'in sorusuna gelince, gerçekten de kullanıcı nüfusu arttıkça Supply parasını ayarlayacak bir merkez bankası ya da federal rezerv olarak hareket edecek kimse yok. Bunun için güvenilir bir tarafın değeri belirlemesi gerekirdi, çünkü yazılımın nesnelerin gerçek dünyadaki değerini bilmesinin bir yolunu bilmiyorum. Eğer akıllıca bir yol olsaydı ya da Supply parasını aktif olarak yönetecek birine güvenmek isteseydik, kurallar bunun için programlanabilirdi. Bu anlamda, değerli bir metale daha çok benziyor."

Satoshi Nakamoto, Hollandalı bir proje yönetimi danışmanı olan Martien van Steenbergen ile fikir alışverişinde bulunduğu e-posta listesinde de aktiftir. 13 Şubat'ta Bitcoin'nin programlanabilirliği konusunu ele alır ve ona [yazar] (https://diyhpl.us/~bryan/irc/Bitcoin-Satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February/001362.html):


> "Marc \[Fawzi\]'nin fikirleri ve burada tartışılan diğerleri tarafından tanımlandığı gibi programlanabilir P2P sosyal para birimlerini uygulamak istiyorsanız, Bitcoin'u bir köşe taşı, ilk adım olarak görüyorum. İlk olarak, temel ve normal bir P2P para biriminin çalışması gerekir. Bir kez kurulduktan ve kanıtlandıktan sonra, bir sonraki adıma, dinamik otomatik para birimine geçmek kolaydır.

Coğrafi aidiyeti olmayan, yeni ekonomik paradigmaları deneyen sanal topluluklar fikrini gerçekten seviyorum."


Tüm bunlar, Bitcoin'in yaratıcısının hedef kitlesine uyum sağlamaya çalıştığını ve insanların keşfine ilgi duymasını sağlamak için elinden geleni yaptığını gösteriyor.


### Mike Hearn ve 21 milyon

Satoshi'ün iletişim stratejisi yavaş yavaş meyvelerini vermeye başladı. Nisan 2009'da başkaları da onun icadıyla ilgilenmeye başladı. Bunlar arasında İsviçre'de Google için çalışan ve boş zamanlarını açık kaynaklı yazılımlar üzerinde geçiren İngiliz geliştirici Mike Hearn de vardı. Daha sonra dijital ödeme sistemleriyle, özellikle de Ryan Fugger'in projesi olan Ripple ile ilgilenmeye başladı. Genç bir Amerikalı bilgisayar bilimcisi ve girişimci olan Charles N. Wyble tarafından Mart ayında oluşturulan bir [tartışma başlığı] (https://groups.google.com/g/rippleusers/c/1GsQzGv9Y14) aracılığıyla Bitcoin'yi tam olarak Ripple Google Grubu'nda duydu.


12 Nisan'da Mike Hearn, Satoshi'e bir [e-posta] (https://plan99.net/~mike/Satoshi-emails/thread1.html) göndererek Bitcoin hakkında bir dizi soru sordu. "Gerçekten devrimci fikirlerle karşılaşmanın nadir olduğunu" belirtti ve Ripple'dan bahsetmeyi ihmal etmedi.


![Mike Hearn](assets/en/027.webp)


Mike Hearn ve Satoshi Nakamoto, Bitcoin'nın ölçeklendirme, mikro ödemeler, yazılımın nasıl çalıştığı ve ters ibrazların olmaması gibi çeşitli yönlerini tartıştı. Mike Hearn özellikle Satoshi'ye toplam bitcoin miktarı için neden "24 milyon" (*sic*) miktarını seçtiğini ve bunların alt bölümlere ayrılıp ayrılamayacağını sordu. Satoshi daha sonra aşağıdaki açıklamayı yapmıştır:


> "Madeni para sayısı ve dağıtım programı için yaptığım seçim eğitimli bir tahmindi. Bu zor bir seçimdi çünkü ağ bir kez kurulduktan sonra kilitleniyor ve ona bağlı kalıyoruz. Fiyatları mevcut para birimlerine benzer hale getirecek bir şey seçmek istedim, ancak geleceği bilmeden bu çok Hard. Sonunda ortada bir şey seçtim. Bitcoin küçük bir niş olarak kalırsa, birim başına mevcut para birimlerinden daha az değerli olacaktır. Dünya ticaretinin bir kısmı için kullanıldığını hayal ederseniz, o zaman tüm dünya için sadece 21 milyon madeni para olacak, bu yüzden birim başına çok daha değerli olacaktır. Değerler 8 ondalık basamaklı 64 bitlik tam sayılardır, yani 1 Coin dahili olarak 100000000 şeklinde temsil edilir. Tipik fiyatların küçük olması halinde bol miktarda ayrıntı vardır. Örneğin, 0.001 1 Euro değerindeyse, ondalık noktanın gösterildiği yeri değiştirmek daha kolay olabilir, bu nedenle 1 Bitcoin'iniz varsa artık 1000 olarak gösterilir ve 0.001 1 olarak gösterilir."

Daha sonra Mike Hearn'e "[blok başına] 100 BTC ve 42 milyonu düşündüğünü" ancak 42 milyonun kendisine yüksek geldiğini açıklayacaktı. ("100 BTC ve 42 milyonu düşündüm ama 42 milyon yüksek geldi.")


Mike Hearn, Satoshi ile iletişime geçtikten sonra yazılımı bilgisayarında kullanmaya başladı. Aralarında [blok 11,157]'nin de bulunduğu birkaç blok çıkardı (https://Mempool.space/block/00000000a630e2695d98b11707d053b12c583f58976f8b4ae6a6f289ee32797b). Tartışmalarına paralel olarak, iki adam bazı parasal alışverişler yaptı. Mike Hearn 18 Nisan'da Satoshi'ye 32,51 bitcoin gönderdi ve o da aynı gün iade etti. Ayrıca birbirlerine Mining çabalarından 50 bitcoin gönderdiler.


### Martti Malmi ve Bitcoin'ün Sunumu


Satoshi'nın iletişimi Martti Malmi adlı genç bir Finlandiyalı bilgisayar bilimleri öğrencisinin de dikkatini çekti. Bitcoin'i Nisan ayı başında P2P Vakfı forumundaki bir metin aracılığıyla keşfetti. Ayın 9'unda yazılımı kullanmaya başladı ve ilk bloğunu (blok 10,351) çıkardı. Akşam saatlerinde Bitcoin üzerine kısa bir sunum yazdı ve bu sunumda "P2P Para Birimi hükümeti yok edebilir mi?" şeklindeki anarşist hipotezi destekledi Metnini Trickster(n) takma adıyla farklı hassasiyetlere sahip iki liberter forumda yayınladı: anti-state.com (ASC) ve Freedomain Radio (anarko-kapitalist Stefan Molyneux'nun medyası) forumu. Martti yazdı:


> "Sistem anonimdir ve hiçbir hükümet işlemleri vergilendiremez ya da engelleyemez. Sınırsız yeni para yaratarak para biriminin değerini düşürebilecek bir merkez bankası yok. Böyle bir sistemin yaygın olarak benimsenmesi, devletin vatandaşlarını besleme yeteneği üzerinde yıkıcı bir etkiye sahip olabilecek bir şey gibi görünüyor."

![Martti Malmi in 2013](assets/en/028.webp)

Martti Malmi 2013 yılında (kaynak: [Business Insider](https://www.businessinsider.com/bitcoins-martti-malmi-not-worried-about-liberty-reserve-2013-5))


Martti daha sonra Satoshi'a bu metnin yazarı olduğunu belirten bir [e-posta] (https://mmalmi.github.io/Satoshi/#email-1) gönderir ve burada "henüz geliştirme konusunda fazla deneyimi olmamasına" rağmen "Bitcoin konusunda yardımcı olmak istediğini" yazar Satoshi Nakamoto'ya 2 Mayıs'ta yanıt verir ve "Bitcoin hakkındaki anlayışının" "tam isabet" olduğunu söyler


Bitcoin'un yaratıcısı, özellikle [Sıkça Sorulan Sorular] (https://mmalmi.github.io/Satoshi/#email-4) (SSS) bölümü yazarak projenin barındırıldığı platform olan SourceForge'daki [web sayfasına] (https://web.archive.org/web/20090511173000/http://Bitcoin.sourceforge.net/) katkıda bulunması için onu görevlendirdi. Ana sayfada (Bitcoin.sourceforge.net), Bitcoin'u "yeni para çıkarmak veya işlemleri izlemek için herhangi bir merkezi otoriteye" dayanmayan "eşler arası ağa dayalı anonim bir dijital para birimi" olarak sunuyor Aşağıdaki avantajları vurgulamaktadır:



- "Üçüncü şahıslara güvenmek zorunda kalmadan internet üzerinden kolayca para transferi yapın."
- "Hiçbir üçüncü taraf işlemlerinizi engelleyemez veya kontrol edemez."
- "Kendinizi kısmi rezerv bankacılığının ve merkez bankalarının kötü politikalarının neden olduğu istikrarsızlıktan koruyun. Bitcoin sisteminin para Supply'ünün sınırlı enflasyonu, bankalar tarafından tekelleştirilmek yerine tüm ağa eşit olarak (hesaplama gücü ile) dağıtılır."
- "Bitcoin ekonomisinin büyümesi enflasyon oranını aştıkça Bitcoin'ün değerinin artması muhtemeldir - Bitcoin'ü bir yatırım olarak düşünün ve bugün bir düğüm çalıştırmaya başlayın!"


Satoshi bu sunumu genel olarak [onaylıyor](https://mmalmi.github.io/Satoshi/#email-5), ancak bazı çekinceleri var. Özellikle Bitcoin'in bir "yatırım" olarak ilan edilmesinden [rahatsız](https://mmalmi.github.io/Satoshi/#email-19), muhtemelen böyle bir ifadenin yasal sonuçlarından korkuyor. Sayfa 6 Mayıs'ta [yayınlandı](https://mmalmi.github.io/Satoshi/#email-9) ve iki gün sonra Martti Malmi [Hackernews](https://news.ycombinator.com/item?id=599852) ve [Reddit](https://www.reddit.com/r/business/comments/8itlf/bitcoin_a_peertopeer_network_based_anonymous/) platformlarında bir bağlantı paylaşarak sayfanın tanıtımını yaptı. Bu açıklamanın biraz değiştirilmiş bir versiyonu 2009 sonunda ana web sitesinde [bulundu](https://web.archive.org/web/20100106082749/http://www.Bitcoin.org/).


2009 ilkbaharı, başlangıçta Bitcoin'ye atıfta bulunmak için kullanılan "kripto para" kelimesinin ortaya çıkışına da tanık oldu. 11 Mayıs'ta Satoshi Martti Malmi'ye [yazdı] (https://mmalmi.github.io/Satoshi/#email-19):


> "Birisi 'kripto para' kelimesini buldu... belki de Bitcoin'u tanımlamak için kullanmamız gereken bir kelimedir, beğendiniz mi?"

Genç Finli kabul eder ve "P2P Kripto Para Birimi "nin Bitcoin'ın sloganı olabileceğini önerir. Bu öneri hayata geçirilecektir: giriş sayfasının başlığı "Bitcoin P2P Kripto Para Birimi" olacak ve Temmuz 2010'da 0.3 sürümünün duyurusunda proje "Bitcoin, P2P kripto para birimi" olarak tanımlanacaktır


### Bitcoin'ye Adanmış İki Forum


Martti Malmi ayrıca halen SourceForge sayfasında bulunan bir forum ve bir wiki kurdu. Bu Elements 9 Haziran'da [açılır](https://mmalmi.github.io/Satoshi/#email-17). Ayın 13'ünde Malmi, SourceForge sayfasının, forumun ve wiki'nin varlığını Bitcoin posta listesinde [duyurur](https://web.archive.org/web/20131016004650/http://sourceforge.net/p/Bitcoin/mailman/Bitcoin-list/?viewmonth=200906):


> "Yeni Bitcoin web sitesi/portalı Bitcoin.sourceforge.net adresinde yayında. Forumlar ve bir wiki dahil edilmiştir, bu nedenle tartışmalara ve wiki belgelerine katılabilirsiniz."

Bu forum kendi kitlesini buluyor. Hatta Ağustos ayında geliştirme için özel bir IRC kanalının (#Bitcoin-dev) oluşturulmasına [yol açtığı] (https://mmalmi.github.io/Satoshi/#email-27) görülüyor. Ancak, sadece üyelerin erişimine açık olduğu için bir arşivimiz yok.


Aylar geçtikçe daha fazla insanın bu ilk foruma kaydolması ve katılması, Satoshi'un Malmi tarafından kurulan yazılım altyapısının yetersiz olduğunu fark etmesine neden olur. 5 Kasım'da genç Finn'e bir mektup yazarak daha yüksek trafiği kaldırabilecek yeni bir forum oluşturulmasını önerir:


> "Artık Bitcoin.sourceforge.net'teki forum tuttuğuna göre, tam gelişmiş forum yazılımını ücretsiz barındıran bir yer aramalıyız."

Benimsenecek teknik çözüm üzerine yapılan bazı tartışmalardan sonra Martti Malmi 17 Kasım'da forumu sunucusuna [yükler](https://mmalmi.github.io/Satoshi/#email-93) ve Satoshi 19 Kasım'da [yapılandırmaya](https://mmalmi.github.io/Satoshi/#email-99) başlar. Ayın 22'sinden itibaren, Bitcoin'in yaratıcısı eski forumdan gizlilik, Mining ve Linux gibi konuları kapsayan bazı Soru ve Cevapları aktarır. Ayrıca bir [hoş geldiniz mesajı] (https://bitcointalk.org/index.php?topic=5.msg28#msg28) yayınlar. Ayın 25'inde forum Bitcoin.org/smf adresinde [başlatılır](https://mmalmi.github.io/Satoshi/#email-110).


İlk kullanıcılar bir sonraki ayın başında kayıt olmaya başlar. 9 Aralık'ta, Satoshi dışında biri tarafından gönderilen [ilk mesaj](https://bitcointalk.org/index.php?topic=12.msg40#msg40) görünür ve bu da tartışmaları gerçekten başlatır. Örnek olarak, 29 Mayıs 2010 tarihinde forumun [ekran görüntüsü](https://web.archive.org/web/20100529193636/http://www.Bitcoin.org/smf/) aşağıda verilmiştir:


![Screenshot of the Bitcoin forum from May 29, 2010](assets/en/029.webp)


Yeni forumun açılışı, Satoshi Nakamoto ve Martti Malmi'nin aylardır üzerinde çalıştığı yazılımın [sürüm 0.2] (https://bitcointalk.org/index.php?topic=16.msg73#msg73) sürümünün 16 Aralık'ta yayınlanması için bir fırsat oldu. Bu sürüm görev çubuğuna küçültme, açılışta otomatik başlatma ve Mining üretimi için çoklu iş parçacığı gibi iyileştirmeler içeriyor. Malmi'nin katkıları ve yeni kurulan NewLibertyStandard (bir sonraki bölümde ele alınacak) tarafından gerçekleştirilen testler sayesinde yazılım Linux'a da uyarlandı.


Ağustos 2011'de BitcoinTalk adını alan bu forumda Satoshi 539 mesaj yazmıştır. Bu mesajlar, geride bıraktığı külliyatın büyük bir kısmını oluşturarak teknik açıklamalar yapmasına, çeşitli ekonomik mekanizmaları açıklamasına ve Bitcoin hakkındaki görüşlerini paylaşmasına olanak sağlamıştır.


### Aşamalı İletişim


Böylece 2009 yılının ilk bölümü iletişime adanmış oldu. Satoshi, keşfine çeşitli yollarla ve farklı yerlerde dikkat çekmeyi başardı. Aralarında Martti Malmi'nin de bulunduğu diğer kişiler de mesajın yayılmasına yardımcı oldu.


Bitcoin'in tanıtımı da birkaç aşamadan geçti: ilk olarak, Satoshi çevrimiçi ödemelere odaklandı; daha sonra sabit para politikasını ve 21 milyon birimlik sınırı vurguladı; ve son olarak, modelinin programlanabilirliğinden bahsetti.

2009 sonbaharında Bitcoin büyümeye hazır görünüyordu. Sistemin ekonomik önyüklemesi tam olarak o zaman gerçekleşti. Bir sonraki bölümde bu konu ele alınacaktır.


## Kripto Para Biriminin Önyüklenmesi

<chapterId>6b3418a7-125e-4ea1-a03a-f36090fac8a4</chapterId>


Önceki bölümlerde, Satoshi Nakamoto'nun fikrini nasıl hayata geçirdiğini ve Bitcoin'ü dünyaya tanıtmak için bu konuda nasıl iletişim kurduğunu gözlemledik. Ancak her şey ona bağlı değildi: insanların hesap birimine değer ataması da gerekiyordu. Bu, işlem ücretleri yoluyla madencilerin ücretlendirilmesine ve doğal deflasyon yoluyla tüccarların ödüllendirilmesine olanak tanıdığından, böyle bir takdir sistemin güvenliği için çok önemliydi.


Ancak Bitcoin'nın değerinin ortaya çıkması kolay bir iş değildi. Bu, tamamen öznel nedenlerle daha önce hiç olmayan bir nesneye ekonomik önem kazandırmakla ilgiliydi. Hal Finney, Cryptography posta listesine gönderdiği 11 Ocak 2009 tarihli [email](https://www.metzdowd.com/pipermail/cryptography/2009-January/015004.html) yazısında bunu çok iyi açıklamıştır:


> "Herhangi bir yeni para birimiyle ilgili ilk sorunlardan biri ona nasıl değer biçileceğidir. İlk başta neredeyse hiç kimsenin kabul etmeyeceği pratik sorun göz ardı edilse bile, birimler için sıfır olmayan belirli bir değer lehine makul bir argüman bulmakta hala bir zorluk vardır."

Dolayısıyla, parasal olgu parasal olmayan bir nedenle ilk değerlendirmeyi gerektirmiştir. Satoshi'nin Martti'ye yazdığı gibi] (https://mmalmi.github.io/Satoshi/#email-1), yanıcı bir maddenin tutuşması için bir "kıvılcım" olması gerekiyordu.


Bitcoin'un bu ekonomik önyüklemesi, Mining faaliyetiyle birlikte en başından itibaren kademeli olarak gerçekleşmiştir. Ancak, dolar karşısında ilk Exchange'in gerçekleştiği Ekim 2009'a kadar tam anlamıyla ortaya çıkmamıştır. Bu bölümde, bu önyüklemenin nasıl gerçekleştiğini ve farklı aktörleri hesap birimine değer atfetmeye iten sebepleri açıklamaya çalışacağız.


### İlk Madenciler

Ocak 2009'dan itibaren Bitcoin'ün başlatılması birkaç aşamada gerçekleşmiştir: ilk madencilerin gelişi, dolarla birlikte Exchange'nin ortaya çıkışı ve Bitcoin'ü kabul eden ilk hizmetlerin geliştirilmesi. Dolayısıyla, üretici düğümleri yerleştirenler, dolaylı olarak hesap birimine değer atayan ilk kişilerdir. Gerçekten de işlem bloklarına Proof of Work eklemek ve dolayısıyla bunları zincire eklemek için hesaplama güçlerine katkıda bulunurlar, bu da zaman (yazılım bakımı nedeniyle) ve enerji (süreçte tüketilen elektrik nedeniyle) açısından maliyetlidir. Bu çaba bitcoin olarak ödüllendirilir, dolayısıyla bu şekilde coin üretmek bir tür ekonomik KİS-372 oluşturur.


Ancak, giriş bölümünde de belirttiğimiz gibi, bitcoinlerin piyasa değeri yoktur. Bu nedenle madencilerin böyle bir çaba göstermek için öznel nedenler bulmaları gerekir. Başlıca nedenler teknik merak, ideolojik motivasyon ve spekülatif ilgidir.


İlk neden, muhtemelen en az önemli olanı, teknik meraktır. Bitcoin'i ilk benimseyenler gerçekten de genellikle bilgisayar meraklılarıdır ve çoğu zaman programlama veya mühendislikle ilgili mesleklerde çalışırlar. İşlerin "kaputun altında" nasıl çalıştığını bilmek isterler, bu da onları yazılımı başlatmaya ve generate biraz bitcoin almaya iter. Bu durum, özellikle 12 Nisan 2009 tarihinde Satoshi'ya sorularını yönelttikten sonra bilgisayarında "uygulamayı denemek" ve bazı bloklar üretmek için [acele eden] (https://plan99.net/~mike/Satoshi-emails/thread1.html) Mike Hearn için geçerlidir. (*orijinal: "Uygulamayı denedim "*)


Mining'nin ikinci nedeni ideolojik motivasyondur. Birçok ilk yazılım kullanıcısı bunu kişisel inançları nedeniyle "iyi bir amaç için" yapmaktadır. Merkezi bir otoriteye dayanmayan sağlam bir dijital para biriminin doğuşuna katkıda bulunmak için bilgi işlem güçlerini kullanıma sunarlar. Hal Finney, 13 Kasım 2008 tarihinde [yazarak] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014848.html) bu kavramı ilk vurgulayan kişidir:


> "Bitcoin sistemi, sınırsız bir serbest piyasayı savunan ve özellikle para birimi üzerindeki kontrolü konusunda devlete kesinlikle düşman olan Amerikan liberteryen hareketiyle önemli ölçüde uyumludur ("[End The Fed](https://en.wikipedia.org/wiki/End_the_Fed)"). Bu nedenle Satoshi [Hal Finney'e yanıt verir](https://www.metzdowd.com/pipermail/cryptography/2008-November/014853.html) argümanının "eğer düzgün bir şekilde açıklayabilirsek liberteryen bakış açısı için çok çekici" olduğunu belirtmiştir

Mining'yi başlatma kararının arkasındaki üçüncü itici güç spekülatif ilgidir. Önceki bölümde açıklandığı üzere, Bitcoin'in para politikası ana satış noktalarından biridir. Dolaşımdaki bitcoin miktarı sabit bir miktara (21 milyon adet) yaklaşacaksa, daha fazla insan ekonomiye katıldıkça birim fiyatları çok yükselebilir. Özellikle bu argüman, Dustin Trammell'i [özel yazışmalarında] Satoshi ile paylaştığı gibi, bitcoin üretmeye çok erken başlamaya ikna eder (https://www.dustintrammell.com/s/Satoshi_Nakamoto.zip):


> "Beni bu kadar hızlı bir şekilde bir node başlatmaya iten nedenlerden biri de buydu. Sistemlerim boştayken başka bir şey yapmıyor, o halde neden BitCoin yaratmayayım? Ve eğer bir gün değerli olurlarsa...? Bu da bir bonus olur!"

Son iki neden, insanları sürekli madencilik yapmaya motive ettiği için çok daha önemlidir. Dolayısıyla, 2009 yılı boyunca, bu nedenlerle hareket eden birçok kişi bilgisayar güçlerini ağa katarak çok sayıda blok üretmiştir. Bu kişiler arasında özellikle



- Hal Finney, ağın lansmanı ile Mart 2009 arasında bilgisayarını çalıştırarak 10.000'den fazla bitcoin biriktirdi.
- Dustin Trammell, 2009 yılı boyunca ve 2010 yılının başlarında etkileyici sayıda blok madenciliği yaparak [Address](https://Mempool.space/Address/12higDjoCCNXSA95xZMWUdPvXNmkAduhWv) ile bağlantılı faaliyetlerin de gösterdiği üzere 70.000'den fazla bitcoin elde etmiştir; - James Howells adında bir İngiliz mühendis, Şubat ve Nisan ayları arasında bilgisayarıyla 8.000 bitcoin [üretmiştir](https://Mempool.space/Address/198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi) (2013 yılında dizüstü bilgisayarını çöpe gönderecek ve birkaç ay sonra hatasını anlayacaktır; vakası daha sonra *The Guardian* tarafından [kamuoyuna](https://www.theguardian.com/technology/2013/nov/27/Hard-drive-Bitcoin-landfill-site) duyurulacaktır);
- Martti Malmi, Nisan 2009 ve 2010 arasında ağdaki blokların üretimine katkıda bulunmuş ve böylece 55.000'den fazla bitcoin [elde etmiştir](https://twitter.com/marttimalmi/status/1339908783187832834);
- NewLibertyStandard adlı bir kişi, Eylül 2009'da yeni ortaya çıkan Exchange servisine yakıt sağlamak için çok sayıda bitcoin üretti...


### İlk Exchange hizmeti ve ilk fiyat


Eylül 2009'un sonunda NewLibertyStandard (NLS olarak kısaltacağız) takma adını kullanan bir kişi Bitcoin'u keşfeder. Yazılımı dener ve Mining'yi başlatır. Ürettiği ilk blok [blok 23,940](https://Mempool.space/block/000000002f74e369b0cab9c836d7777aabb66ae11741910c61da819f17605a50). Kendisi bir Linux kullanıcısıdır ve bu nedenle yazılımı çalıştırmak için "emülatör" Wine kullanır. Forumdaki [avatar](https://bitcointalk.org/index.php?action=profile;u=26) üzerinde "özgürlük" yazan bir Amerikan Kartalı resminden de anlaşılacağı üzere siyasi özgürlük ve değerli metallerle ilgilenmektedir. Dolayısıyla Bitcoin'u dijital dünyada altının bir eşdeğeri olarak görüyor: [kişisel sayfasında](https://web.archive.org/web/20091229132559/http://newlibertystandard.wetpaint.com/) Satoshi Nakamoto'nun yaratımını "ekonomik bir devrim" ve "dijital para biriminin altın standardı" olarak sunuyor


![Avatar of NewLibertyStandard on the Bitcoin forum depicting an American Eagle](assets/en/030.webp)


Ekim 2009'da, insanların dolarlarını bitcoine ve bitcoinlerini tekrar dolara dönüştürmelerine olanak tanıyan ilk para birimi Exchange hizmeti kuruldu. Yaratıcı, SourceForge'daki Bitcoin'e adanmış foruma kaydoldu ve hizmetinin açılışını orada duyurdu. Exchange oranını tahmin etmek için, bulunduğu yerdeki elektrik fiyatını ve üretim sıklığını göz önünde bulundurarak bir birim elde etmek için gereken enerji maliyetini temel aldı. Sayfasında [yazdı](https://web.archive.org/web/20091229132610/http://newlibertystandard.wetpaint.com/page/Exchange+Rate):


> "Exchange oranımız, 1,00 $'ın bir yıl boyunca yüksek CPU kullanımına sahip bir bilgisayarı çalıştırmak için gereken ortalama elektrik miktarı olan 1331,5 kWh ile çarpılıp, bir önceki yıl için ABD'deki ortalama konut elektrik maliyeti olan 0,1136 $ ile çarpılıp 12 aya bölünmesi ve bilgisayarım tarafından son 30 gün içinde üretilen bitcoin sayısına bölünmesiyle hesaplanır."

İşte NLS'nin kişisel sayfasında da yayınlanan NLS hizmetinin gösterge niteliğindeki Exchange ücretleri:


![Indicative exchange rates of the NLS service](assets/en/031.webp)


İşlemler newlibertystandard@gmail.com adresinden e-posta yoluyla gerçekleştirilir. Dolar transferleri yalnızca PayPal aracılığıyla yapılır ve işlem için ücret alınır.


8 Ekim'de Martti Malmi, Satoshi'i NLS hizmetinin varlığı hakkında [bilgilendirdi](https://mmalmi.github.io/Satoshi/#email-34). Bitcoin'nin yaratıcısı bu habere olumlu tepki verdi, çünkü [bir süredir](https://mmalmi.github.io/Satoshi/#email-28) Mining'u ödüllendirmek ve sistemin ekonomik dinamiklerini harekete geçirmek için bitcoinlerin değerini garanti altına alacak bir araç oluşturmayı düşünüyordu. 16 Ekim'de sağ koluna [şöyle yazdı](https://mmalmi.github.io/Satoshi/#email-35):

"NewLibertyStandard sitesinde olduğu gibi daha fazla insanın bu konuya ilgi gösterdiğini görmek cesaret verici. Elektriğe dayalı değer tahminine yaklaşımını beğendim. İnsanların hangi açıklamaları benimsediğini görmek eğitici. Bu açıklamalar, [Bitcoin'ü] kitleler için daha erişilebilir kılan basitleştirilmiş bir anlama yolunun keşfedilmesine yardımcı olabilir. Dünyadaki pek çok karmaşık kavramın, insanların %80'ini tatmin eden basit bir açıklaması ve basit açıklamadaki kusurları gören diğer %20'yi tatmin eden eksiksiz bir açıklaması vardır."


NLS'nin duyurulmasının ardından Martti Malmi onunla temasa geçti. İkili bir Exchange yapmak üzere anlaştı. 11-12 Ekim 2009 gecesi, dolar karşılığında ilk bitcoin satışı tamamlandı: Martti, Mining çalışmalarından 5.050 bitcoini NLS'ye [transfer etti] (https://twitter.com/marttimalmi/status/423455561703624704), o da PayPal hesabına 5.02 dolar transfer etti. Bu da yaklaşık 0.001 dolarlık bir birim fiyata karşılık gelmektedir.


Takip eden haftalarda NLS, Supply hizmeti için daha fazla bitcoin biriktirdi. 19 Kasım'da birisi sahip olduğu 22.500 kadar bitcoini [satın alarak](https://Mempool.space/tx/67fc73c770d5001be14f65c95f2f37e04e26c3f8c6a49519d2e63c594ea26756) ilk Bitcoin satışını gerçekleştirdi. Birkaç saat sonra Satoshi, Martti Malmi'ye yazdığı bir [e-posta](https://mmalmi.github.io/Satoshi/#email-99) ile bu finansal operasyon hakkında heyecanlandı.


Takip eden aylarda NLS hizmeti Bitcoin'in ekonomik gelişiminin merkezi bir unsuru haline geldi ve Bitcoin ile dolar arasında Exchange için bir ölçüt oluşturdu. Ancak, 2010 yılının ilk yarısında daha verimli diğer Exchange hizmetlerinin ortaya çıkmasıyla rekabetle karşı karşıya kalmaya başladı.


### Ekonominin Başlangıcı

2010'un başlangıcı, kripto para birimindeki ticari borsaların ilk adımlarıyla işaretlenmiştir. Başka bir ekonomik mal (bu durumda dolar) karşılığında Bitcoin'u Exchange olarak almayı kabul eden ilk kişi olan NewLibertyStandard, aynı zamanda bu ekonomik patlamanın ilk destekçisidir. 19 Ocak 2010 tarihinde, yeni foruma kaydolduktan hemen sonra, aşağıdaki metni [yazdı] (https://bitcointalk.org/index.php?topic=15.msg111#msg111):


> "İnsanlar benden bitcoin aldı ve bana bitcoin sattı. Supply ve talep, düşük olsa bile, zaten var ve gerçekten gerekli olan tek şey bu. Exchange bitcoinleri başka bir para birimiyle değiştirmeyi teklif etmek, nihayetinde bitcoinleri mal veya hizmetlerle değiştirmekten farklı değildir. Para birimleri maldır ve bunları takas etmek bir hizmettir. ABD doları dışında bitcoin ile alınıp satılabilecek bir şey düşünmeye çalıştım ama hiçbir şey bulamadım. Lütfen bitcoin karşılığında ne satmaya karar verdiğiniz konusunda bizi haberdar etmekten çekinmeyin. Fonların tükenmesi konusuyla ilgili olarak, bütçemde günlük bir bağış planladım. Bugün tüm dolarlarımı veya bitcoinlerimi satın alabilirsiniz, ancak yarın ve ertesi gün her zaman daha fazlası olacaktır. Takasçılar da dahil olmak üzere bitcoin kullanarak mal alan veya satan herkes Bitcoin ekonomisini ilerletiyor. Herkes üzerine düşeni yapsın. Exchange'de bitcoin karşılığında bir şey satın alın ya da satın!"

Koordinasyon çabaları öncelikle forum üzerinden yürütülmektedir. 27 Ocak'ta giik adını kullanan Hollandalı bir kullanıcı, Bitcoin kabul eden çeşitli hizmetleri listelemeyi önerdiği "Bitcoin kabul ediyoruz" başlıklı bir [konu] (https://bitcointalk.org/index.php?topic=30.0) oluşturdu. Bu süre zarfında, yeni forum popülerlik kazanmaya başladı ve mesajlar çoğaldı. 7 Şubat'ta Satoshi Martti Malmi'ye [dikkat çekti] (https://mmalmi.github.io/Satoshi/#email-153) "forum kesinlikle yükseliyor. Bu kadar hızlı bir şekilde bu kadar çok faaliyet olmasını beklemiyordum."


5 Şubat'ta NLS, yabancı Exchange piyasasında işlem gören para birimleri gibi Bitcoin'nin de BTC ve Tayland bahtı (฿) sembolünü benimsemesini [önerdi](https://bitcointalk.org/index.php?topic=41.msg238#msg238). O zamana kadar yerleşik bir uygulama yoktu: örneğin, Satoshi ve Martti [yazışmalarında] birimleri tanımlamak için `bc` harflerini kullandılar (https://mmalmi.github.io/Satoshi/#email-119). BTC sembolünün kullanımı hızla standart hale geldi. 24 Şubat'ta para birimi sembolü (iki dikey çubukla kesişen büyük B) Satoshi tarafından [tasarlandı](https://bitcointalk.org/index.php?topic=64.msg504#msg504) ve ardından ilk gerçek Bitcoin logosu oluşturuldu.


![First real Bitcoin logo designed by Satoshi Nakamoto (2010)](assets/en/032.webp)


Yavaş yavaş, insanlar Bitcoin'u kabul etmeye başladı. Aralık 2009'da SmokeTooMuch adlı kullanıcı BTC 2 PSC adlı bir paysafecard hediye kartı satış hizmetinin varlığından haberdar oldu](https://web.archive.org/web/20191215200234/https://bitcointalk.org/index.php?topic=15.msg65#msg65). Bu hizmet daha sonra 4 Şubat 2010 tarihinde Satoshi tarafından olumlu bir şekilde [bahsedildi](https://mmalmi.github.io/Satoshi/#email-141). Bu durum, 9 Şubat'ta pul ve çıkartmaları satışa sunduğu Liberty Swap Variety Shop adlı kendi online mağazasını [açan](https://bitcointalk.org/index.php?topic=30.msg305#msg305) NLS için de geçerliydi.


Dolar ile Exchange de gelişti ve iki ay içinde en az üç platform kapılarını açtı:



- BitcoinFX (bitcoinfx.cz.cc), 15 Şubat'ta [duyurulan] (https://bitcointalk.org/index.php?topic=30.msg194#msg194) Liberty Reserve doları cinsinden bitcoin satmaya yönelik bir hizmet;
- BitcoinExchange (bitcoinexchange.com), Martti Malmi'nin kullanıcıların yatırdığı avro ve bitcoinleri dikkate alarak Supply ve talebi benzersiz bir şekilde [ölçen](https://mmalmi.github.io/Satoshi/#email-25) ve 2 Mart 2010 tarihinde [halka açılan](https://bitcointalk.org/index.php?topic=68.msg591#msg591) platformu;
- Bitcoin Market (bitcoinmarket.com), 16 Mart'ta dwdollar adlı biri tarafından [başlatılan] (https://bitcointalk.org/index.php?topic=20.msg726#msg726) ve Temmuz ayında Mt. Gox'un ortaya çıkmasından önce önemli bir başarı görecek olan PayPal kullanan eşler arası bir pazar yeri.


![Later capture of the Bitcoin Market interface, August 26, 2011](assets/en/033.webp)

gW-426 Market Interface'in [Yakalama] (https://web.archive.org/web/20110826231728/https://www.bitcoinmarket.com/market/trades/) daha sonra (Ağustos 2011)


11 Mart'ta BitcoinFX yöneticisi tarafından bitcoin içeren ilk poker oyunu [organize edildi](https://bitcointalk.org/index.php?topic=80.msg781#msg781) ve kumar ile kripto para birimi arasında var olacak güçlü ilişki başlatıldı. Oyunu [600 BTC](https://Mempool.space/tx/6477a88f0196e1fcf6c608e446be62c708556f34a79d169fbb05b1fee92f5761) kazanan dwdollar kazandı.


IP üzerinden ses hizmeti [Link2VoIP](https://bitcointalk.org/index.php?topic=30.msg733#msg733) 16 Mart'ta, web barındırma hizmeti [Vekja.net](https://bitcointalk.org/index.php?topic=30.msg1008#msg1008) 23 Nisan'da veya alan adı satıcısı [Privacy Shark](https://bitcointalk.org/index.php?topic=30.msg1035#msg1035) 30 Nisan'da Bitcoin'i kabul eden diğer hizmetler ortaya çıkar. Hizmetlerin bu şekilde çoğalması Martti Malmi'nin sonunda Bitcoin.org web sitesinde tüccarları listeleyen bir [sayfa](https://web.archive.org/web/20100517040312/http://www.Bitcoin.org:80/trade) barındırmasına yol açtı.


İlk özel Bitcoin saklama hizmeti de ortaya çıkıyor: MyBitcoin, özellikle mobil cihazlarda kripto para biriminin kolay ve sakin bir şekilde kullanılmasını sağlayan bir web uygulaması. Bu hizmet sayesinde kullanıcıların işlem göndermek ve almak için tüm zincir verilerini indirmelerine ya da özel anahtarlarını kaydederek bitcoinlerini kendilerinin saklamalarına gerek kalmıyor.


![Logo of MyBitcoin from the archive of the site mybitcoin.com](assets/en/034.webp)


O zamanlar hafif cüzdanlar ("SPV" olarak bilinir) mevcut değildi, bu nedenle Satoshi Nakamoto'nun kendisi, bu kullanım Bitcoin'un kalbindeki aracısızlaştırma ilkesine aykırı olsa da, bu tür bir yazılımın kullanılmasını kabul edilebilir buldu. 18 Mayıs 2010 tarihinde forumda [yazdı] (https://bitcointalk.org/index.php?topic=125.msg1149#msg1149):


> "Bu arada [vekja.net](http://vekja.net) ve [www.mybitcoin.com](http://www.mybitcoin.com) gibi siteler hesap tabanlı sistemleri denemektedir. Bir web sitesinde bir hesap oluşturuyor, bitcoinlerinizi orada tutuyor ve içeri ve dışarı transfer ediyorsunuz. Bir web sitesinde hesap oluşturmak, yazılım yüklemekten ve kullanmayı öğrenmekten çok daha kolaydır ve çoğu insan için daha tanıdık bir yöntemdir. Tek dezavantajı siteye güvenmek zorunda olmanızdır, ancak mikro ödemeler ve çeşitli harcamalar için tasarlanan küçük miktarlar için bu sorun değildir. Başlamak için kolay bir yol ve alınan miktarlar daha önemli hale gelirse gerçek Bitcoin yazılımına geçebilirsiniz."

Son olarak, 19 Mayıs'ta Teppy adını kullanan bir kullanıcı, yönettiği devasa çok oyunculu oyun *A Tale in the Desert* için Bitcoin [kabul] (https://bitcointalk.org/index.php?topic=30.msg1159#msg1159) etmeye başladı.


### Bitcoin'ün Değerinin Kökeni


2010 baharında Bitcoin birçok kişinin zihninde değer kazandı. Sistemin kullanımı henüz emekleme aşamasında olsa da, ister Mining, ister dolarla Exchange, ister hizmet satışı açısından olsun, Bitcoin'ya yönelik talep mevcuttu. Bu ekonomik önyüklemeyi 22 Mayıs'ta yaşanan sembolik bir olay kesinleştirdi: bitcoinlerle ilk kez fiziksel bir mal, özellikle de bir sonraki bölümde anlatacağımız bir pizza satın alındı.


Birçok kişi Bitcoin'in değerinin kaynağını açıklamakta zorlanmıştır. Değerin bu şekilde ortaya çıkması, özellikle Ludwig von Mises'in [regresyon teoremini] (https://en.wikipedia.org/wiki/Regression_theorem) dar bir şekilde yorumlayan Avusturya okulu savunucularını rahatsız etmiştir. Bu durum, forumda [aranan](https://bitcointalk.org/index.php?topic=583.msg5984#msg5984) dönüşümdeki değer aktarımını dolara dayandıran xc adlı belirli bir kişi için geçerliydi.


Ancak bu soru, yeni bir para biriminin önyüklemesini kesinlikle üstesinden gelinmesi zor ancak imkansız olmayan bir zorluk olarak gören Satoshi'u hiç rahatsız etmedi. Bu nedenle 27 Ağustos 2010 tarihinde forumda xc'ye cevaben kendi bakış açısını [ifade etti] (https://bitcointalk.org/index.php?topic=583.msg11405#msg11405):


> "Bir düşünce deneyi olarak, altın kadar az bulunan ancak aşağıdaki özelliklere sahip bir ana metal olduğunu hayal edin:
> \- sıkıcı gri renkte
> \- iyi bir elektrik iletkeni değildir
> \- özellikle güçlü değildir, ancak sünek veya kolay şekillendirilebilir de değildir
> \- herhangi bir pratik veya süsleme amacı için kullanışlı değil
>

> ve özel, büyülü bir özelliğe sahip:
> \- bir iletişim kanalı üzerinden taşınabilir
>

> Şu ya da bu nedenle bu metal herhangi bir değer kazanırsa, servetini uzak mesafelere transfer etmek isteyen herkes bir miktar satın alabilir, iletebilir ve alıcının bunu satmasını sağlayabilirdi.
>

> Belki de sizin önerdiğiniz gibi, Exchange için potansiyel faydasını öngören insanlar tarafından döngüsel olarak bir başlangıç değeri elde edebilir. (Ben kesinlikle isterdim) Belki koleksiyoncular ya da rastgele herhangi bir sebep bunu tetikleyebilir."

# Bitcoin'in İlk Yükselişi

<partId>557d792d-34d5-4a10-8977-82afdcfe402b</partId>


## Grafik Kartları, Pizzalar ve Bedava Bitcoinler

<chapterId>9cd228a4-58d3-46a3-9935-06098bafc954</chapterId>


Bir önceki bölümde, Bitcoin'nin nasıl ortaya çıktığını, halka nasıl tanıtıldığını ve ekonomik olarak nasıl başlatıldığını araştırdık. 2010 baharında, Bitcoin ticareti çiçek açmaya başlarken, Satoshi Nakamoto ve onu destekleyen birkaç kişi alevi canlı tutmaya kararlıydı. Neyse ki, başta Miner Laszlo Hanyecz ve geliştirici Gavin Andresen olmak üzere eylemleriyle öne çıkan başka kişiler de bu çabaya katıldı.


Bu bölümde, Mining'in grafik işlem birimi (GPU) ile ilk dağıtımını, Satoshi Nakamoto'nun servetini, bitcoinlerle ilk fiziksel mal alımını, ücretsiz birimler dağıtan bir Bitcoin Faucet'nin kuruluşunu ve Slashdot'tan önce yazılımın ve ağın gelişimini inceleyeceğiz.


### Grafik İşlem Birimi tarafından Mining


Bitcoin'ye yönelik giderek artan talebe, ağdaki Mining faaliyetlerinde kademeli bir artış eşlik etti. 2009 yılı boyunca ağın zorluk derecesi minimum 1 seviyesindeydi ve bu da tüm düğümlerin bir blok çıkarmak için yaklaşık 4,3 milyar hesaplama yapmasını gerektiriyordu. Ancak Aralık 2009'da, zorluk faktörünü 1'den 1.18'e çıkaran ayarlama algoritması sayesinde bu durum değişti.


Satoshi Nakamoto bu zorluk artışı konusunda çok endişeliydi ve Şubat 2010'dan itibaren forumda bir [geçmiş] (https://bitcointalk.org/index.php?topic=43.msg249#msg249) tuttu. İşte böyle görünüyordu:


![Evolution of the difficulty as described by Satoshi Nakamoto on the forum](assets/en/035.webp)


Ağdaki bilgi işlem gücünün artmasıyla ilgili bu coşkuya rağmen, Satoshi yine de birimlerin dağılımını desteklemek için Mining'ün uzmanlaşmasını yavaşlatmak istiyordu. O zamana kadar madenciler yeni bitcoinler çıkarmak için merkezi işlem birimlerini (CPU) kullanıyordu. Ancak bu işlemciler, bu tür tekrarlayan hesaplamalar için çok daha uygun olan grafik işlem birimlerine (GPU'lar) kıyasla, tekrarlayan işlemleri gerçekleştirmek için verimsiz olduklarını kanıtladılar. Sonuç olarak, Satoshi'ün kendisi de dahil olmak üzere herkes bu evrimin kaçınılmaz olduğunu biliyordu. 19 Aralık 2009 tarihinde aşağıdaki şekilde [belirtmiştir] (https://bitcointalk.org/index.php?topic=12.msg54#msg54):

"Ağın iyiliği için GPU silahlanma yarışını olabildiğince ertelemek üzere bir centilmenlik anlaşması yapmalıyız. GPU sürücüleri ve uyumluluk konusunda endişelenmek zorunda kalmayan yeni kullanıcıları hızlandırmak çok daha kolay. Şu anda sadece CPU'su olan herkesin eşit bir şekilde rekabet edebilmesi çok güzel."


Ancak birkaç ay sonra Pandora'nın kutusu açıldı. Baş belası Laszlo Hanyecz, Florida'da yaşayan 28 yaşında Macar kökenli Amerikalı bir geliştiricidir. Bitcoin'yı Nisan 2010'da keşfetti. Ayın 9'unda NLS'den yaklaşık 20 $ karşılığında 3.300 bitcoin [satın aldı] (https://Mempool.space/tx/faf172f5dc06b0ae03268555dddcd65be47e9a8a8bb44a122b12bfaf735f9a81#vout=1), ardından birkaç transfer yaparak sistemi test etti. Ayın 18'inde, [halka açık Address](https://Mempool.space/Address/1XPTgDRhN8RFnzniWCddobD9iKZatrvH4) işlemlerini çoğaltarak ağı tıkamaya çalıştı, ancak tıkandı.


![Laszlo Hanyecz with his son in May 2018](assets/en/036.webp)

Laszlo Hanyecz Mayıs 2018'de oğluyla birlikte (kaynak: [The Telegraph](https://www.telegraph.co.uk/technology/2018/05/22/inside-story-behind-famous-2010-Bitcoin-pizza-purchase-today/))


Daha sonra, yazılım kodunu Mac OS X işletim sisteminde çalışacak şekilde [uyarladı](https://bitcointalk.org/index.php?topic=116.msg972#msg972). Daha sonra GPU'nun](https://bitcointalk.org/index.php?topic=124.msg1100#msg1100) bitcoin üretmeye [dahil edilmesine] olanak tanıyan OpenCL ortamını kullanarak Mining'u optimize etmek için çalıştı. 10 Mayıs'ta [çalıştırılabilir](https://bitcointalk.org/index.php?topic=124.msg1100#msg1100) dosyasını yayınladı ve diğer madencilerin de bunu yapabilmesini sağlamak için yamalar yazmayı [teklif etti](https://bitcointalk.org/index.php?topic=133.msg1103#msg1103). Bu optimizasyon kısa sürede blok üretiminde önemli bir yer edinmesini sağladı.

Nisan sonunda Laszlo Satoshi ile temasa geçerek fikrini sordu, ancak Satoshi ancak 17 Mayıs'ta yanıt verdi. Bunun üzerine Bitcoin'ın yaratıcısı, Mining'nin en fazla sayıda kişi tarafından erişilebilir kalması için faaliyetlerini yavaşlatmasını [istedi](https://www.reddit.com/r/Bitcoin/comments/36vnmr/heres_what_satoshi_wrote_to_the_man_responsible/):

> "Yeni kullanıcılar için en büyük cazibe, bilgisayarı olan herkesin generate'e ücretsiz para yükleyebilmesi. 5000 kullanıcı olduğunda bu teşvik azalabilir, ancak şimdilik hala geçerli. GPU'lar bu teşviki yalnızca üst düzey GPU donanımına sahip olanlarla sınırlandıracaktır. GPU hesaplama kümelerinin eninde sonunda üretilen tüm coinleri yutması kaçınılmaz, ancak o günü hızlandırmak istemiyorum. (...) Sosyalist gibi görünmek istemem, zenginliğin yoğunlaşması umurumda değil, ancak şimdilik, bu parayı insanların %100'üne vererek %20'sine vermekten daha fazla büyüme elde ediyoruz. Dahası, GPU silahlanma yarışını ne kadar geciktirebilirsek, OpenCL kütüphaneleri o kadar olgunlaşır ve daha fazla insan OpenCL uyumlu ekran kartlarına sahip olur."

Laszlo bu uyarıyı dikkate almadı ve grafik kartıyla blok madenciliği yapmaya devam ederek sonraki aylarda on binlerce bitcoin üretti. Ancak GPU Mining Ekim ayına kadar yaygınlaşmadı.


### Satoshi'in Bitcoinleri


Mining'deki bu artışın da önemli bir sonucu oldu: Satoshi blok üretmeyi durdurdu. Ağın başlangıcından bu yana Mining yeterli bir onaylama hızı ve kabul edilebilir bir güvenlik seviyesi sağlamakla görevliydi. Yeni gücün devreye girmesiyle birlikte bu görevden vazgeçebilir ve diğer ağ üyelerinin yaratılan bitcoinlerin tamamından faydalanmasına izin verebilirdi.


Satoshi'in Mining aktivitesinin belirgin bir deseni vardır, bu da muhtemelen birkaç yanlış pozitif ile bulduğu blokları tanımlamayı mümkün kılar. Geliştirici Sergio Lerner 2013 yılında bu Mining modelini vurgulamış ve Patoshi Modeli olarak adlandırmıştır.


![Patoshi Pattern between blocks 0 and 50,000](assets/en/037.webp)


Satoshiblocks.info] (http://satoshiblocks.info/) web sitesinde gözlemlendiği gibi 0 ve 50.000 bloklar arasındaki Patoshi Örüntüsü: her nokta bir bloğa karşılık gelir. Mavi çizgiler Satoshi'in bloklarından oluşmakta, diğer çizgiler ise diğer madencilerin çıktılarını temsil etmektedir.


Whale Alert tarafından 2020 yılında yayınlanan bir araştırmaya göre, Satoshi yaklaşık 22.500 blok çıkarmış ve böylece planlanan 21 milyon birimin %5'inden fazlası olan 1.122.693 bitcoin biriktirmiştir. 2009 yılının büyük bir bölümünde ağ, kurucusunun hesaplama gücüne güvenmiştir. Bu bağımlılık, Mining faaliyetlerinin en kötü dönemi olan Ağustos 2009'da kendini göstermiş ve muhtemelen makinelerini daha az izleyen Satoshi için bir "duraklama" dönemine denk gelmiştir. Gerçekten de bu Ağustos ayı boyunca, beklenen 4.464 bloktan sadece 1.564'ü üretilmiştir ve bu da ortalama 28 dakika 30 saniyelik bir süreye karşılık gelmektedir.


2009'un sonbaharında bilgi işlem gücündeki artışla birlikte, Satoshi'ün bilgi işlem gücünün toplam ağ gücüne oranı kademeli olarak azaldı. Mart 2009'da %75 olan oran Eylül'de %60'a, Aralık'ta %15'e düşmüş ve Mayıs'ta %0'a ulaşmıştır. Aşağıda [Organofcorti] (https://organofcorti.blogspot.com/2014/08/167-satoshis-Hashrate.html) tarafından 2014 yılında yapılan bir grafik yer almaktadır:


![Estimation of the proportion of Satoshi's computing power relative to the total power between January 2009 and July 2010](assets/en/038.webp)


Dahası, Satoshi'nın Mining hakimiyetindeki düşüş sadece pasif değildir: aynı dönemde üretimini yavaşlatır. Aslında, Satoshi'nın belirtilen amacı herkesin katılımıdır: Madenciliği maddi kazanç için değil, teşvikler yürürlüğe girene kadar ağın çalışmasını sağlamak için yapmaktadır. Böylece, bu Mining döneminde Hash oranını (her saniyede yapılan hesaplama sayısı) üç kez düşürür: ilki Haziran 2009'da 4,5'ten 2,5 MH/s'ye, ikincisi Ekim ayında 2,5'ten 1 MH/s'ye ve üçüncüsü Mayıs 2010'da 1'den 0 MH/s'ye. İşte bu dönem boyunca Hash oranının gelişiminin bir grafiği ([Organofcorti](https://organofcorti.blogspot.com/2014/08/167-satoshis-Hashrate.html)):


![Estimation of Satoshi's hash rate between January 2009 and May 2010](assets/en/039.webp)


Satoshi'in Mining'si bu nedenle [Jameson Lopp'un işaret ettiği gibi](https://blog.lopp.net/was-Satoshi-a-greedy-Miner/) kesinlikle fedakârdır. Mining'yi 3 Mayıs 2010'da durdurduğunda (son bloğu [blok 54,316](https://Mempool.space/block/000000000d1e2cf92a7e6afdbed6d34fc3ac2cc863d9a236ca4db394a94ece2e)), bu Bitcoin'un yavaş gelişimindeki bir başka başarıyı teşkil eder: işlem onayının ekonomik aktörler tarafından devralınması.


### Bitcoin Pizza Günü


Temel bir olay da Mayıs 2010'a damgasını vurur: bitcoin ile ilk fiziksel mal alımı. Laszlo Hanyecz ilk adımı atar. Algoritması aracılığıyla 20.000'den fazla bitcoin biriktirdikten sonra, pizza alarak bunları ekonomiye yeniden kazandırmayı amaçlar. 18 Mayıs'ta forumda aşağıdaki [duyuruyu] (https://bitcointalk.org/index.php?topic=137.msg1141#msg1141) yazar:


> "Birkaç pizza için 10.000 bitcoin öderim... mesela 2 büyük pizza, böylece ertesi gün için biraz daha pizzam kalır. Daha sonra atıştırmak için pizza kalmasını seviyorum. Pizzayı kendiniz yapıp evime getirebilir ya da benim için bir teslimat yerinden sipariş edebilirsiniz, ancak hedeflediğim şey, Exchange'te bitcoin karşılığında kendim sipariş etmek veya hazırlamak zorunda olmadığım yiyecekleri teslim almak, bir otelde 'kahvaltı tabağı' sipariş etmek gibi bir şey, sadece size yiyecek bir şeyler getiriyorlar ve mutlu oluyorsunuz! (...) Eğer ilgileniyorsanız lütfen bana haber verin ve bir anlaşma yapalım."

Dört gün sonra bu teklif kabul edildi. Jeremy Sturdivant adlı genç bir Kaliforniyalı, IRC anlık mesajlaşma servisinde Exchange'yı kabul etti.


![Jeremy Sturdivant in May 2018](assets/en/040.webp)

Jeremy Sturdivant Mayıs 2018'de (kaynak: [The Telegraph](https://www.telegraph.co.uk/technology/2018/05/22/inside-story-behind-famous-2010-Bitcoin-pizza-purchase-today/))


22 Mayıs'ta Papa John's'tan iki pizza sipariş etmiş ve bunlar Jacksonville, Florida'daki Laszlo'ya teslim edilmiştir. Exchange'de 10.000 bitcoin [aldı](https://Mempool.space/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d), Bitcoin Piyasa kurunda yaklaşık 44 $ değerinde. İşte bu iki pizzanın Laszlo'nun kendisi tarafından [paylaşılan](https://web.archive.org/web/20110703134805/http://heliacal.net/~solar/Bitcoin/pizza/) bir fotoğrafı:


![Pizzas from Papa John's delivered to Laszlo Hanyecz on May 22, 2010](assets/en/041.webp)


Böylece, dolaylı da olsa, bitcoin ile yapılan ilk fiziksel mal satın alma işlemi tamamlanmış oldu. Laszlo, "büyük bir adım atıldığını" yazan [Martti Malmi](https://bitcointalk.org/index.php?topic=137.msg1196#msg1196) tarafından tebrik edildi NLS de bu konuda [olumlu bir yorum](https://bitcointalk.org/index.php?topic=137.msg1197#msg1197) ekliyor.


Laszlo Hanyecz 12 Haziran'da foruma yazdığı yazıyla teklifini [yineler] (https://bitcointalk.org/index.php?topic=137.msg1526#msg1526):


> "Bu arada bu açık bir teklif... Param olduğu sürece istediğim zaman bu pizzalardan 2 tanesi için 10.000 BTC takas edebilirim."

Bu nedenle, 4 Ağustos'a kadar aynı türden birkaç işlem daha gerçekleştirdi ve [yazdı] (https://bitcointalk.org/index.php?topic=137.msg7544#msg7544) artık "günde binlerce birim generate" yapamayacağı için "bunu yapmaya devam edemeyeceğini" söyledi Sebep: 11 Temmuz'da Slashdot'tan gelen akının getirdiği fiyat artışı, bu da ona forum üyelerinin alaycı sözlerini kazandırdı ve bitcoinlerini tutmasının daha iyi olacağını ima etti. Birkaç ay sonra, Kasım ayında, Bitcoin'nin fiyatı 25 sent civarında seyrederken, ribuck [yazdı] (https://bitcointalk.org/index.php?topic=137.msg25352#msg25352) kullanıcısı neredeyse kehanet gibi bir tavırla: "Bu sonunda dünyanın ilk milyon dolarlık pizzası mı olacak?"


Bununla birlikte, kripto para biriminin satın alma gücündeki artış, sembolizmini azaltmadı. Bitcoin topluluğu bu tarihi her yıl Bitcoin Pizza Günü olarak anmaktadır.


### Gavin Andresen ve Bitcoin Faucet


Bu dönem aynı zamanda Bitcoin tarihinde kilit bir figürün gelişine de tanıklık etti: Gavin Andresen, 2004 yılında ABD vatandaşlığına [geçen](https://gavinthink.blogspot.com/2007/06/seven-years-ago-today.html) ve o sırada Amherst, Massachusetts'te yaşayan 44 yaşında Avustralya doğumlu bir geliştirici. Avustralya'ya yaptığı bir seyahatten dönen ve geçici olarak işsiz olan Andresen, Mayıs ayı sonunda InfoWorld'de Neil McAllister tarafından yayınlanan bir [makale](https://www.infoworld.com/article/2627013/open-source-innovation-on-the-cutting-edge.html?page=3) aracılığıyla Bitcoin'yı keşfetti. Bu makale Satoshi Nakamoto'nun projesini "açık kaynaklı bir yenilik" olarak sunuyordu


![Profile photo of Gavin Andresen, taken in Townsville, Queensland, Australia](assets/en/042.webp)

Gavin Andresen Townsville, Queensland, Avustralya'da (kaynak: [CIO arşivi](https://web.archive.org/web/20110326160734/http://www.cio.com.au/article/380394/open_source_identity_bitcoin_technical_lead_gavin_andresen/))


Meraklı ve yaratıcı biri olarak hızla kişisel bir proje üzerinde çalışmaya başladı: talep eden herkese bitcoin veren bir "Bitcoin Faucet". 11 Haziran'da hizmetini [başlattı] (https://bitcointalk.org/index.php?topic=183.msg1488#msg1488) ve forumda aşağıdaki şekilde sundu:

"İlk Bitcoin programlama projem için kulağa gerçekten aptalca gelen bir şey yapmaya karar verdim: Bitcoin dağıtan bir web sitesi oluşturdum. (...) Neden? Çünkü Bitcoin projesinin başarılı olmasını istiyorum ve bence insanlar denemek için bir avuç birim alabilirlerse başarılı olma şansı daha yüksek."


Satoshi, hemen fark etmemiş olsa da bu hizmetin başlatılmasına olumlu tepki verdi. Bir hafta sonra, 18 Haziran'da, "ilk proje için mükemmel bir seçim" olduğunu yazarak yaratıcıyı [tebrik etti] (https://bitcointalk.org/index.php?topic=183.msg1620#msg1620) ve "başka kimse yapmasaydı tam olarak aynı şeyi yapmayı planladığını, böylece ölümlüler için Hard 50BTC generate için çok fazla olduğunda, yeni kullanıcıların hemen oynamak için biraz coin alabileceğini" söyledi


Gavin Andresen'in katkısı bununla da kalmadı. Bitcoin'ün nasıl çalıştığına derin bir ilgi duydu ve kodu incelemeye koyuldu. Protokoldeki yerleşik betik sistemini [keşfetti] (https://bitcointalk.org/index.php?topic=195.msg1606#msg1606) ve bunu forumda hızla paylaştı. Sistemin güvenliğini azalttığı ("karmaşıklık güvenliğin düşmanıdır") ve ikinci bir yazılım uygulaması geliştirmeyi daha zor hale getirdiği için bu özellik hakkındaki endişelerini dile getirdi. Satoshi [açıkladı] (https://bitcointalk.org/index.php?topic=195.msg1611#msg1611) Script adını verdiği bu mekanizmanın entegre edilmesinin arkasındaki nedeni:


> "Bitcoin'nın doğası gereği, 0.1 sürümü yayınlandıktan sonra, çekirdek tasarım ömrünün geri kalanı için taşa oturtulmuş oldu. Bu nedenle, aklıma gelebilecek her olası işlem türünü destekleyecek şekilde tasarlamak istedim. (...) Çözüm, işlem yapan tarafların işlemlerini düğüm ağının değerlendireceği bir yüklem olarak tanımlayabilmeleri için sorunu genelleştiren komut dosyasıydı. Düğümlerin işlemi yalnızca göndericinin koşullarının karşılanıp karşılanmadığını değerlendirecek kadar anlaması gerekiyor."

Gavin ayrıca Linux için önyükleme sırasında otomatik başlatmayı [uygulayarak](https://sourceforge.net/p/Bitcoin/code/101/), API'ye odaklanarak (0.3.3 sürümündeki iyileştirme için [kredilendirilecek](https://bitcointalk.org/index.php?topic=570.msg5707#msg5707)) ve test ağının dağıtımına katılarak (9 Haziran'da [tasarladığı](https://bitcointalk.org/index.php?topic=240.msg2104#msg2104)) yazılım geliştirmeye dahil oldu. Martti Malmi yeni tam zamanlı işiyle [çok meşgul](https://mmalmi.github.io/Satoshi/#email-191) olduğu için Exchange'nin fikirlerini Satoshi ile paylaşacak ve giderek onun sağ kolu haline gelecekti.


### Temel Etkinliklerle Dolu Bir Bahar


2010 baharı temel olaylar açısından zengin bir dönemdi. İlk olarak, Nisan sonunda geliştirici Laszlo Hanyecz, Satoshi'ün kısa vadede karşı çıktığı bir optimizasyon olan GPU Mining'i geliştirdi (her ne kadar uzun vadede kaçınılmazlığını kabul etse de). Bu gelişme, muhtemelen ağın Hash oranının yeterli olduğunu tahmin eden Satoshi'ün blok üretimini durdurmasıyla aynı zamana denk geldi. Ardından 22 Mayıs, Laszlo Hanyecz ve Jeremy Sturdivant arasında gerçekleşen ve bitcoinlerle ilk fiziksel mal alımını teşkil eden ünlü pizzaların Exchange'i ile işaretlendi. Son olarak, Haziran ayında Gavin Andresen geldi ve Bitcoin Faucet'ü yarattı ve hızla yazılım geliştirmeye dahil oldu. Tüm bu Elements, ekonominin Bitcoin etrafında cesaret verici bir ilerleme kaydettiğini gösterdi.


Bununla birlikte, Haziran ayı sonunda ağdaki faaliyet oldukça mütevazı kalmıştı. Birkaç yeni kullanıcı vardı ve parasal fenomenin alevi sönmemek için yeterliydi. 30 Haziran'da Cypherpunk James A, Bitcoin-list posta listesindeydi. Donald (son gelişmeleri takip etmemiş ya da forumun varlığından haberdar değilmiş gibi görünüyordu) [ilan etti] (https://web.archive.org/web/20131016002646/http://sourceforge.net/p/Bitcoin/mailman/Bitcoin-list/?viewmonth=201006) "Bitcoin \[ölmüştü\] bir nevi." Yanılıyor olsa da, yorumu göze batan bir iletişim eksikliğini ortaya koyuyordu: çok az insan projeden haberdardı ve daha fazla çaba gerekiyordu. Bitcoin'un "faydalı olabilmesi için bir kullanıcı ekolojisine" ihtiyacı vardı ve bu kritik kitle henüz oluşmamıştı. İki hafta sonra, bir sonraki bölümde Address'i ele alacağımız bir etkinlik bu yönde ilerleyecekti. (*orijinal: "Evet - Bitcoin bir nevi öldü. Sorun şu ki Bitcoin'un faydalı olabilmesi için bir kullanıcı ekolojisine ihtiyacı var. "*)


## Büyük Slashdotting

<chapterId>2eef715e-b018-445b-b360-1c6e1c1df462</chapterId>


Bitcoin, 2010 yazının başında, bazı cesaret verici ilk gelişmelere rağmen sallantılı bir temele dayanıyordu. Yazılımın Satoshi Nakamoto dışında çok az geliştiricisi vardı. Madenciler kişisel bilgisayarlarında amatörce çalışıyorlardı. Bitcoin ile ilgili yaklaşık yirmi hizmet vardı ve gerçek borsalar da bir o kadar nadirdi. Ancak, yılın ikinci yarısında işler büyük ölçüde değişmek üzereydi.


Bu bölümde, "büyük slashdotting "i, yani 11 Temmuz 2010 tarihinde popüler web sitesi Slashdot'ta Bitcoin'nin bir sunumunun yayınlanmasını takip eden ani kullanıcı akınını tartışmayı amaçlıyoruz. Bu metnin Satoshi'ün son iletişim çabası olarak nasıl ortaya çıktığını ve Bitcoin'nin bu popülerleşmesini takip eden doğrudan etkilerin neler olduğunu göreceğiz.


### Yazılımın 0.3 sürümü

Satoshi Nakamoto ve Martti Malmi'nin uzun süredir hazırladıkları yazılımın 0.3 sürümü 2010 yazının başında yayınlandı. Bir önceki yılın Aralık ayında yayınlanan 0.2 sürümüyle karşılaştırıldığında, bu sürüm [daemon](https://fr.wikipedia.org/wiki/Daemon_\(informatique\)) (bitcoind olacak), komut satırı kontrolü, bir API (JSON-RPC aracılığıyla), birim üretiminin optimizasyonu ve kullanıcının Hash oranını tahmin eden bir "hashmeter" gibi önemli iyileştirmeler içeriyor. Ayrıca Laszlo Hanyecz'in katkılarıyla Mac OS X için destek ve grafiksel Interface'ün Almanca, Hollandaca ve İtalyanca'ya çevirisini de içermektedir.

22 Haziran'da Satoshi [forum üyelerinden](https://bitcointalk.org/index.php?topic=199.msg1654#msg1654) bu yazılım sürümünü test etmelerini ister. Bu sürümün yayınlanmasını Bitcoin'un gelişiminde çok önemli bir an olarak görüyor ve numaralandırmayı doğrudan sürüm 1.3'e taşıyarak "beta" özelliğini bırakmayı bile düşünüyor](https://bitcointalk.org/index.php?topic=217.msg1803#msg1803). Ancak, kararından oldukça hızlı bir şekilde [geri döner](https://bitcointalk.org/index.php?topic=217.msg1928#msg1928).


6 Temmuz'da Satoshi Nakamoto yazılımın 0.3 sürümünün yayınlandığını duyurdu. Bu sürümün Bitcoin'nin ilerlemesi için önemli olabileceğini bilerek, sunumu dikkatlice hazırlar ve [yazar] (https://bitcointalk.org/index.php?topic=238.msg2004#msg2004):


> "İşte eşler arası kripto para birimi Bitcoin'ün 0.3 sürümü! Bitcoin, güvenilir bir merkezi sunucu ihtiyacını ortadan kaldırmak için kriptografi ve dağıtık bir ağ kullanan dijital bir para birimidir. Merkezi olarak yönetilen para birimlerinin keyfi enflasyon riskinden kurtulun! Bitcoin'ün toplam dolaşımı 21 milyon birimle sınırlıdır. Birimler, sağladıkları bilgi işlem gücüne göre ağın düğümlerine kademeli olarak dağıtılır, böylece boşta kalan CPU zamanınıza katkıda bulunarak bunlardan pay alabilirsiniz."

### Slashdot için Bir Sunum

Yeni yazılım sürümünün yayınlanması vesilesiyle, Teppy adlı bir forum kullanıcısı (Mayıs ayında Bitcoin'i kabul etmeye başlayan MMORPG'nin yöneticisi) [bilgisayar, video oyunları, bilim, İnternet gibi ineklere yönelik konuları kapsayan ve adını `/.` karakterlerinden alan çok popüler bir haber sitesi olan Slashdot'a reklam vermeyi önerir] (https://bitcointalk.org/index.php?topic=199.msg1662#msg1662). 22 Haziran'da forumda "biraz tanıtım yapmayı deneyip denemeyeceklerini" soruyor ve "Slashdot'un bulabilirsek iyi bir yer olduğunu" belirtiyor (*orijinal: "Biraz reklam yapmayı denemeli miyiz? Eğer başarabilirsek Slashdot iyidir. "*) Martti Malmi [yorumlar](https://bitcointalk.org/index.php?topic=199.msg1664#msg1664) "milyonlarca teknik açıdan yetkin okuyucusuyla Slashdot'a ulaşmak harika olur, belki de hayal edilebilecek en iyi şey!" diye yazıyor


5 Temmuz'da Teppy, Slashdot'a göndermeyi planladığı bir sunum yazar ve bunu forumda [yayınlar] (https://bitcointalk.org/index.php?topic=234.msg1969#msg1969):


> "Yıkıcı bir teknoloji için bu nasıl? Bitcoin, merkez bankası ve işlem ücreti olmayan, alıcı-anonim, satıcı-anonim bir kripto para birimidir. Hashcash'e benzer bir konsept kullanan müşteriler, eninde sonunda bulunacak 21.000.000 Bitcoin'den bazılarını keşfetmeye çalışırken CPU döngülerini yakmaktadır. Zaman içinde Bitcoin'lerin piyasa değerinin generate için gereken enerjiyle eşitlenmesi ve böylece herhangi bir hükümetin ulaşamayacağı enerji destekli bir para biriminin ortaya çıkması beklenmektedir."

Birkaç forum üyesi bu metnin geliştirilmesi için önerilerde bulunur. Satoshi ilk mesajdan birkaç saat sonra görüşünü bildirmek üzere [araya girer] (https://bitcointalk.org/index.php?topic=234.msg1976#msg1976). "Çabayı gerçekten takdir ettiğini" ancak "pek çok sorun olduğunu" yazıyor ve ardından kendisini rahatsız eden Elements'i sıralıyor:



- Devlet etkisinin yokluğuyla ilgili olarak, "kesinlikle bu tür bir provokasyon veya iddiada bulunmadığını" yazarak ihtiyatlı davranmaktadır; (*orijinal: "'Geliştiriciler, bunun herhangi bir hükümetin ulaşamayacağı, enerji açısından istikrarlı bir para birimiyle sonuçlanacağını umuyor - Kesinlikle böyle bir sataşma ya da iddiada bulunmuyorum. "*)
- Enerji desteğiyle ilgili olarak, para biriminin "enerji açısından istikrarlı olmadığını" düşünüyor ve ekliyor: "Bu konu tartışıldı. Enerji maliyetiyle bağlantılı değil. NLS'nin enerjiye dayalı tahmini iyi bir başlangıç noktasıydı, ancak piyasa güçleri giderek daha baskın hale gelecektir.";
- Sistemin anonim yönüyle ilgili olarak, "'anonim' yönünü vurgulamak" istemediğini ve bu konuda "ana sayfayı değiştirmeyi amaçladığını" belirtiyor. (*orijinal "Biz 'anonim' ile başlamak istemiyoruz. (Ana sayfayı düzenlemeyi düşünüyordum) "*)


Birkaç saat sonra Martti Malmi'ye gönderdiği bir [e-posta](https://mmalmi.github.io/Satoshi/#email-197)'da Satoshi, anonimliği önemsizleştirme niyetini açıklamak için iki ana neden gösteriyor: kullanıcı için tehlike ve kamuoyu algısı. Şöyle yazıyor:


> "Bence anonimlik konusuna vurgu yapmamalıyız. IP ile gönderim yerine Bitcoin adreslerinin popüler olmasıyla birlikte, her şeyin otomatik olarak anonim olduğu izlenimini veremeyiz. Sahte anonim olmak mümkün, ancak dikkatli olmalısınız. [Dahası, 'anonim' kulağa biraz şüpheli geliyor. Bence anonimlik isteyen insanlar bunu biz tanıtmadan da öğreneceklerdir."

Forumdaki mesajını şöyle tamamlıyor:


> "Mızmızlandığım için üzgünüm. Bu şeyin genel halk için bir tanımını yazmak lanet olası Hard. Bunu ilişkilendirecek hiçbir şey yok."

Daha sonra Teppy, önerileri dikkate alarak sunumu güncelledi. Böylece, Temmuz ayının başında, Bitcoin etrafındaki söylemin iyi kalibre edildiği ve benzeri görülmemiş bir akın için olgunlaştığı gözlemlendi.


### Slashdot'landı!


11 Temmuz 2010 tarihinde, Teppy tarafından yazılan Bitcoin sunumunun gözden geçirilmiş bir versiyonu Slashdot'ta [yayınlandı] (https://news.slashdot.org/story/10/07/11/1747245/Bitcoin-Releases-Version-03). Aşağıdaki gibi okunuyordu:


> "Yıkıcı bir teknoloji için bu nasıl? Bitcoin, merkez bankası ve işlem ücreti olmayan, eşler arası, ağ tabanlı bir dijital para birimidir. Proof-of-Work konseptini kullanan düğümler, bulgularını ağa yayınlayarak jeton demetlerini aramak için CPU döngülerini yakar. Enerji kullanımının analizi, Bitcoin'lerin piyasa değerinin halihazırda generate için gereken enerjinin değerinin üzerinde olduğunu ve bunun da sağlıklı bir talebe işaret ettiğini göstermektedir. Topluluk, para biriminin herhangi bir hükümetin erişimi dışında kalacağından umutlu."

![Slashdot Logo in 2010](assets/en/043.webp)


Yayın fark edildi ve birkaç gün içinde yaklaşık 500 yorum gönderildi. Bitcoin için bu başarı, siteye ve foruma büyük bir ziyaretçi akınına yol açtı. Blockchain'in kullanımı arttı: ağ üzerinde gerçekleştirilen işlem sayısı 10 Temmuz'da 42 iken 12'sinde 1.641'e yükseldi ve 14'ünde 5.554'e ulaşarak tüm zamanların en yüksek seviyesine ulaştı. Sistem artan yüke rağmen ayakta kaldı. Ayın 14'ünde geliştirici Gavin Andresen forumda [yazdı] (https://bitcointalk.org/index.php?topic=286.msg2745#msg2745):


> "Bence Satoshi harika bir iş çıkardı: Bitcoin'nin 'slashdotlandığı' son iki gün içinde, Bitcoin işlem kayıpları, yük nedeniyle ağ kesintisi veya temel işlevlerle ilgili herhangi bir sorun duymadım.

Bu akının ilk sonucu, Bitcoin'nin fiyatının bir hafta içinde 0,008$'dan 0,08$'a çıkarak meteorik bir yükseliş yaşaması oldu; bu on katlık bir artış demek!


Slashdot'tan gelen insan akınının bir diğer etkisi de ağ üzerinde kullanılan bilgi işlem gücünün artmasıdır. Birçok kişi yazılımı başlatıyor ve merkezi işlemcileri ile bloklar üretiyor. 11 Temmuz ile 17 Temmuz arasında Hash oranı 0.22 GH/s'den 2.78 GH/s'ye yükselmiştir.


### Mt. Gox'un Yaratılışı


Slashdot sayesinde Bitcoin'i keşfedenler arasında, 2000'li yıllarda eşler arası dosya paylaşım yazılımı eDonkey2000'in kurucu ortağı ve geliştiricisi olarak tanınan 35 yaşındaki Amerikalı girişimci ve programcı Jed McCaleb de vardı. Bitcoin'i dolar karşılığında Exchange olarak elde etmenin zorluğunu fark ederek, "bir hevesle" verimli bir pazar yaratmaya karar verdi. Bunu yapmak için 2007 yılında geliştirdiği eski projelerinden birini yeniden kullandı: Magic The Gathering Online Exchange (MTGOX), çevrimiçi oyun *Magic: The Gathering Online* için kart alım satımına izin veren bir web sitesi. Bu projenin alan adını (mtgox.com) yeniden kullandı ve bu yeni platformun adı oldu: Mt. Gox, "Gox Dağı" olarak telaffuz edilir.


![Jed McCaleb in 2013](assets/en/044.webp)

Jed McCaleb 2013 yılında (kaynak: Ariel Zambelich için [Wired](https://web.archive.org/web/20131001233752/http://www.wired.com/wiredenterprise/2013/09/jed_mccaleb/))


Bir hafta sonra, 18 Temmuz'da Jed McCaleb Exchange platformunu başlattı ve forumda [duyurdu](https://bitcointalk.org/index.php?topic=444.msg3866#msg3866). Uzmanlığı sayesinde, platformun modern çevrimiçi borsalara benzer şekilde otomatik bir pazar yeri olarak çalışmasını sağladı. [Ona göre](https://bitcointalk.org/index.php?topic=444.msg3891#msg3891), Bitcoin Market'ten farklıydı çünkü "her zaman çevrimiçiydi, otomatikti", "site daha hızlıydı ve özel barındırmaya sahipti" ve "Interface daha kullanıcı dostuydu." Sonuç olarak, Mt. Gox hızla Bitcoin'i satın almanın birincil yolu haline geldi ve kendisini dolar kotasyonları için bir ölçüt olarak belirledi.


![Interface of the Mt. Gox platform in February 2011](assets/en/045.webp)

Şubat 2011'de Mt. Gox platformunun Interface'u (kaynak: [Mt. Gox arşivi](https://web.archive.org/web/20110203031942/http://mtgox.com/))


Platform başlangıçta PayPal üzerinden ödeme kabul ediyordu. Ancak, Ekim 2010'da, çok fazla ters ibraz talebinin ardından PayPal, Jed McCaleb'in hesabını [bloke etti](https://bitcointalk.org/index.php?topic=1419.msg16421#msg16421) ve bu da onu platformdaki para yatırma ve çekme işlemlerini geçici olarak askıya almaya zorladı. Birkaç hafta sonra, Liberty Reserve'i bir ödeme yöntemi olarak ekleyerek transferleri [geri yükledi](https://bitcointalk.org/index.php?topic=1699.msg20700#msg20700). Daha sonra, talep üzerine [Paxum](https://bitcointalk.org/index.php?topic=2052.msg27809#msg27809) üzerinden işlemleri ve [dolar cinsinden](https://bitcointalk.org/index.php?topic=4187.msg60610#msg60610) (ACH) ve [avro cinsinden](https://bitcointalk.org/index.php?topic=2515.msg34040#msg34040) (SEPA) banka transferlerini de kabul etti.


### Slashdotting'in Hızlandırıcı Etkisi


Bitcoin'ın tanıtımının Slashdot'ta yayınlanmasının Satoshi Nakamoto'nun projesi üzerindeki etkisi muhteşem oldu. İlgilenen insanların akını rekor bir fiyata ve Hash oranında bir artışa yol açtı. Dahası, Jed McCaleb'in Bitcoin'ı keşfetmesine ve Mt. Gox adı altında hesap biriminin ticareti için değerli bir pazar yeri oluşturmasına neden oldu.

Takip eden aylarda, teknik, ekonomik ve Mining iyileştirmeleri gelişti ve Slashdot'u bir topluluk hareketi olarak Bitcoin'ün gerçek başlangıç noktası haline getirdi. Ancak en önemli değişiklikler yazılım ve protokol seviyelerinde meydana geldi: büyük güvenlik açıklarının giderilmesi gerekiyordu. Bir sonraki bölüm, Bitcoin'ün geliştirilmesinde önemli bir adım oluşturan bu teknik konulara odaklanmaktadır.


## İlk Teknik Sorunlar

<chapterId>30cc4fe4-22b0-429e-9874-029c9137c0aa</chapterId>


Son bölümde belirtildiği gibi, 11 Temmuz 2010'da Slashdot'tan gelen kullanıcı akını Satoshi Nakamoto'nun projesine büyük bir ilgi dalgasına neden oldu. Ağın kullanımı patladı ve Exchange oranı, sisteme adanan bilgi işlem gücü gibi on kat arttı. Böylece Bitcoin yaz boyunca benzeri görülmemiş bir büyüme yaşadı.


Ancak bu başarıya, yazılımda bazı güvenlik açıklarının keşfedilmesiyle birlikte teknik sorunlar da eşlik etti. Daha fazla popülerlik, daha fazla insanın kodu incelemesi ve operasyonel anormalliklerin ortaya çıkma olasılığının daha yüksek olması anlamına geliyordu. İşte 15 Ağustos'ta Bitcoin'in tarihindeki ilk "arıza" olan ve yaklaşık 15 saat süren değer taşması olayında tam da bu yaşandı. Bu dönem, doğal olarak, çeşitli tehditleri öngörmek ve kusurları mümkün olduğunca düzeltmek için yazılımda bir iyileştirme ile işaretlendi.


### Yazılım İyileştirme


Slashdot'tan gelen kullanıcı akını da yazılımın geliştirilmesini gerektirdi. Bulunan güvenlik açıklarının düzeltilmesi ve yeni özelliklerin entegre edilmesi gerekiyordu. Satoshi bu nedenle baskı altındaydı: 18 Temmuz'da Martti Malmi'ye özel olarak "aklımı kaybediyorum, yapılması gereken çok şey var" diye [itiraf etti] (https://mmalmi.github.io/Satoshi/#email-210) İki ay içinde yazılımın en az sekiz alt sürümü yayınlandı!

Ancak Bitcoin'in yaratıcısı kod üzerinde tek başına çalışmıyor. Haziran ayında gelen ve geliştirmeye giderek daha fazla dahil olan Gavin Andresen'e güvenebilir (9 Temmuz itibariyle SourceForge deposunda [credited](https://sourceforge.net/p/Bitcoin/code/101/)). Christian Decker (cdecker) ya da Michael Marquardt (daha çok Theymos takma adıyla tanınıyor) gibi sistemin nasıl çalıştığını merak eden ve karşılaştıkları sorunları bildiren bazı kişiler de var. Satoshi ayrıca ArtForz (bir sonraki bölümde göreceğimiz gibi bir Mining çiftliği kuran ilk kişi), Alman geliştirici Nils Schneider (tcatm), Michael Brown (knightmb) veya BlackEye gibi birim üretimini optimize etmenin yollarını bulmak için kodu değiştiren madenciler tarafından da desteklenmektedir.


Son olarak Jeff Garzik'ten (forumda jgarzik takma adını kullanıyor) bahsedebiliriz, Amerikalı bir geliştirici ve özgür yazılım dünyasına katkıda bulunuyor, özellikle Red Hat dağıtımı için ve Avusturya ekonomi okulunun özgürlükçü bir takipçisi. Bitcoin'ü Slashdot'taki makale aracılığıyla keşfetti ve hemen Bitcoin'e dahil oldu.


![Jeff Garzik in 2013](assets/en/046.webp)

Jeff Garzik 2013 yılında (kaynak: [Benson Samuel](https://bensonsamuel.com/Bitcoin-3/talking-Bitcoin-with-jeff-garzik/))


Satoshi'in ilk hedefi, son zamanlarda artan kullanımla başa çıkabilmek için yazılımı ve protokolü daha güvenli hale getirmektir. Gavin Andresen ile birlikte, meydana gelebilecek çeşitli saldırıları (hizmet reddi saldırıları dahil) göz önünde bulundururlar ve keşfedilen güvenlik açıklarını düzeltmeye çalışırlar. Bu şekilde 17 Temmuz'da ([v0.3.2](https://bitcointalk.org/index.php?topic=437.msg3807#msg3807)) zincirin belirli bir tarihten önce yeniden yazılmasını engelleyen bir kontrol noktaları sistemi eklenir ve 25 Temmuz'da ([v0.3.3](https://bitcointalk.org/index.php?topic=570.msg5707#msg5707)) düğümler tarafından doğru zincirin seçilmesi mekanizmasını iyileştirmek için çalışma kavramı entegre edilir.


Gavin ve Satoshi ayrıca birkaç hatayı da düzeltti. Bunlardan en önemlisi "1 RETURN bug", yani script sistemindeki bir açık, belirli bir script kullanarak herhangi bir Address'dan bitcoin harcamayı mümkün kılıyordu. ArtForz bu açığı 28 Temmuz'da bildirmiş ve bu açığı kullanarak kendini gizlice zenginleştirmek yerine keşfini Satoshi ve Gavin ile paylaşmayı tercih etmiştir. Satoshi hızlı bir şekilde düzeltmeyi yazılıma dahil etti ([v0.3.6](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451)) ve tüm kullanıcıların yükseltme yapmasını tavsiye etti. Böylece Bitcoin potansiyel bir felaketten kurtulmuş oldu. MITRE daha sonra bu güvenlik açığını [CVE-2010-5141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-5141) tanımlayıcısı altında kaydetmiştir.


İkinci hedef ise protokolü değiştirerek ya da yazılımın çalışmasını optimize ederek sistemin performansını arttırmaktı. Bu kategoride, Satoshi tarafından 29 Temmuz'da (v0.3.6) ihtiyatlı bir şekilde gerçekleştirilen ve tek [yorum] (https://sourceforge.net/p/Bitcoin/code/119/) "genişletme" kelimesi olan dahili komut sistemine `OP_NOP' işlem kodlarının eklenmesi yer almaktadır Bu işlem kodları, bir komut dosyasında mevcutsa hiçbir etkisi olmayan, ancak işlemi geçersiz kılmayan sessiz talimatlardır. Sonuç olarak, bu talimatların davranışı, komut dosyalarını eski bir protokol sürümüyle uyumsuz hale getirmeden değiştirilebilir, dolayısıyla Satoshi'in yorumu. Bu işlem kodları, `OP_NOP2` ve `OP_NOP3` talimatlarını sırasıyla `OP_CHECKLOCKTIMEVERIFY` ve `OP_CHECKSEQUENCEVERIFY` talimatlarına dönüştürerek 2015 ve 2016'da "Soft çatalları" olarak adlandırılan duruma izin verecektir.


Madenciler ayrıca bitcoin üretimini doğrudan ya da dolaylı olarak iyileştirmek için keşiflerini ana yazılımla paylaşmaktadır. İlk olarak, [Laszlo'nun kişisel optimizasyonu](https://bitcointalk.org/index.php?topic=199.msg1686#msg1686) 6 Temmuz'da yazılıma entegre edildi (v0.3.0). Ardından, Nils Schneider tarafından SHA-256 Hash işlevi için [bağlam önbellekleme](https://bitcointalk.org/index.php?topic=501.msg5815#msg5815) ve BlackEye tarafından [hesaplama optimizasyonu](https://bitcointalk.org/index.php?topic=453.msg5774#msg5774) 29 Temmuz'da yazılıma eklendi (v0.3.6). Son olarak, Nils Schneider (tekrar) tarafından önerilen [tek bir işlemci üzerinde hesaplamanın paralelleştirilmesi](https://bitcointalk.org/index.php?topic=648.msg6722#msg6722) 15 Ağustos'ta (v0.3.10) koda [entegre edildi](https://bitcointalk.org/index.php?topic=827.msg9590#msg9590).


Tüm bu gelişmeler, Bitcoin'ün yazılım işleyişi ve Mining performansı açısından her geçen gün daha da güçlendiği anlamına geliyor. Ancak, topluluğu derinden etkileyen bir olay bu yenilikçi ivmeyi biraz zedeliyor. Değer taşması olayı Ağustos ayında meydana geldi ve ağı yaklaşık on beş saat boyunca kesintiye uğrattı.


### Değer Taşması Olayı


15 Ağustos 2010 tarihinde, saat 17:00 (UTC) civarında, 184 *milyardan* fazla bitcoin yaratan bir işlem içeren bir blok zincire 74.638 yükseklikte eklendi. Bu olağanüstü yüksek ihraç, miktarların temsilinde bir bellek taşması açığından yararlandı: saldırgan, her biri 92,233,720,368.54277039 BTC'lik iki işlem çıktısı yarattı; bu, işaretli 64 bitlik bir tamsayı (protokolde kullanılan format) ile temsil edilebilecek maksimum birimlere yakın bir miktardır.


Bir saat sonra, sorun Jeff Garzik tarafından fark edildi ve forumdaki topluluğu "garip bir blok" konusunda [uyardı](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474). Satoshi'in yanıtı akşam 9 civarında geldi: forumda bir ön kod değişikliği [yayınladı](https://bitcointalk.org/index.php?topic=823.msg9530#msg9530) ve insanlara "üretmeyi bırakmalarını" [tavsiye etti](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531). Bazı revizyonlar yaptıktan ve bunları Sourceforge'a yükledikten sonra, sonunda saat 11:48'de Windows, Linux ve Mac OS X için bir yama [yayınladı](https://bitcointalk.org/index.php?topic=827.msg9590#msg9590).


Bu yama madencilerin suçlanan işlemi geçersiz olarak reddetmesine ve bu işlemi içermeyen alternatif bir dal oluşturmasına olanak sağlamıştır. Bu dalın [ilk bloğu] (https://Mempool.space/block/000000000069e1affe7161ab4bcbeacebb4ddf155b50e807f42de971b688a09b) saat 11:53'te bulunmuştur.


Ertesi sabah, sabah 8'den kısa bir süre sonra, çelişkili durum çözüldü. Doğru zincir diğerinden daha uzun hale geldi, bu da yamayı uygulasalar da uygulamasalar da tüm düğümlerin bu zinciri takip etmesi gerektiği anlamına geliyordu. Bu olay ağ faaliyetlerini yaklaşık 15 saat boyunca kesintiye uğrattı, ancak topluluğun duyarlılığı örnek teşkil etti. Satoshi [yazdı] (https://bitcointalk.org/index.php?topic=823.msg9734#msg9734) öğleden sonra 1 civarında:


> "Görünüşe göre kötü zinciri 74689 civarında bir yerde geçtik. &nbsp;0.3.9 ve daha düşük düğümler birkaç saattir mevcut blok numarasıyla yanıt veriyor. (...) Hızlı yanıt için herkese teşekkürler!"

### Uyarı Sistemi

Temmuz ayında 1 RETURN hatasını keşfettikten sonra Satoshi Nakamoto ağı kazalara karşı korumak için mümkün olan her şeyi yaptı. 3 Ağustos'ta yazılıma zincir bölünmesi durumunda devreye giren bir uyarı mekanizması ekledi ([v0.3.8](https://bitcointalk.org/index.php?topic=696.msg7364#msg7364)). Ancak bu mekanizmanın ayın 15'inde ortaya çıkan değer taşması hatasını tespit etmek için yararlı olmadığı kanıtlandı ve Satoshi'i daha gelişmiş bir mekanizma geliştirmek için [planını](https://bitcointalk.org/index.php?topic=823.msg9586#msg9586) hızlandırmaya sevk etti.


Olayı takip eden günlerde, Satoshi ağ üzerinde etkili bir uyarı sistemi kurdu ve bu sayede özel bir anahtarla teknik sorunlar olması durumunda düğümleri uyarabildi ve bazı API komutlarını askıya alabildi. 22 Ağustos'ta sistemini forumda [sundu] (https://bitcointalk.org/index.php?topic=898.msg10722#msg10722). Bu duyuru, bu sistemde merkezileştirici bir unsur ve bir devletin istismar edebileceği bir güvenlik açığı gören üyeler arasında endişelere yol açtı. Satoshi [iki gün sonra](https://bitcointalk.org/index.php?topic=898.msg11074#msg11074) cevap vererek bu düşünceleri "paranoyakça" olarak nitelendirdi ve sistemin kullanıcılar tarafından manuel olarak devre dışı bırakılabileceğini ve zaten geçici olacağını belirtti.


27 Ağustos'ta uyarı sistemi resmi olarak yazılıma entegre edildi ([v0.3.11](https://bitcointalk.org/index.php?topic=941.msg11439#msg11439)). İşlevleri askıya alma imkanı Aralık ayında [kaldırıldı](https://bitcointalk.org/index.php?topic=2228.msg29479#msg29479). Takip eden yıllarda uyarı sistemi, 2017'de yazılımdan kesin olarak [kaldırılmadan](https://Bitcoin.org/en/alert/2016-11-01-alert-retirement) önce, özellikle 2013'te kazara meydana gelen bir Fork için olmak üzere birkaç kez kullanıldı.


### Blok Boyutu Sınırı


Protokolü iyileştirme ve saldırılara karşı dirençli hale getirme çabalarının bir diğer unsuru da işlem bloğu boyutu sınırının eklenmesidir. Bu sınır, her bloğun bu boyuttan daha küçük olmasını gerektirerek sistemin işlem kapasitesini kısıtlar. İlk amacı ağa karşı hizmet reddi saldırılarını önlemekti.


Bu parametre 15 Temmuz'da Satoshi tarafından `MAX_BLOCK_SIZE' (v0.3.1) sabiti şeklinde koda gizlice [eklenmiş](https://sourceforge.net/p/Bitcoin/code/103/) ve daha sonra 1 megabayt (1,000,000 bayt) olarak ayarlanmıştır. Kısıtlamanın uygulanmasının programlanması 7 Eylül'de Bitcoin'nin yaratıcısı tarafından, yine kendisinden herhangi bir kamuya duyuru yapılmadan [gerçekleştirildi] (https://sourceforge.net/p/Bitcoin/code/103/) (v0.3.12). Boyut sınırının (bloklardaki imza operatörlerinin sayısını da kısıtlayan) 79,400 numaralı bloktan itibaren yürürlüğe girmesi öngörülmüştür. Etkinleştirme [gerçekleşti] (https://Mempool.space/block/000000000021d821ec06be7173f413690bc5c4bc648dfa70b3b6763236f055b7) 12 Eylül'de. Bu sınırlama o zamanlar oldukça zararsızdı: saniyede 7 standart işlem hacmine izin veriyordu ki bu da slashdot'tan sonra bile zamanın ekonomik faaliyetlerini desteklemek için fazlasıyla yeterliydi.


Her ne kadar Satoshi blok boyutu sınırının varlığından bahsetmemiş olsa da, birkaç kişi zaman içinde bunun koddaki varlığını fark etmiştir. Bu nedenle, 12 Ağustos gibi erken bir tarihte, throughput takma adını kullanan Rusça konuşan bir forum üyesi tarafından, nispeten olumlu bir tonda, "Bir başka ilginç husus da bloğun bayt boyutunun (dolayısıyla içindeki işlem sayısının) sınırlı olmasıdır" şeklinde [belirtilmiştir](https://bitcointalk.org/index.php?topic=788.msg8873#msg8873) Daha sonra, 30 Eylül'de Theymos başka bir üyeye](https://bitcointalk.org/index.php?topic=1314.msg14748#msg14748) "Bitcoin 1MB üzerindeki bloklara izin vermiyor, bu nedenle 216 baytlık (oldukça küçük) bir ortalama işlem boyutu varsayarsak, Bitcoin her 10 dakikada yalnızca 4.629 işlemi gerçekleştirebilir" dedi

Son olarak, bu parametrenin varlığı, "ölçeklenebilirlik konusunda hükümetin kapanmasından çok daha fazla endişe duyduğunu" [beyan eden] (https://bitcointalk.org/index.php?topic=1314.msg14750#msg14750) ve "dakika başına 463 işlem sınırı gibi yerleşik sınırlamalarla Bitcoin'yi ciddi yatırımcılara satmanın" nasıl mümkün olduğunu [soran] (https://bitcointalk.org/index.php?topic=1341.msg15107#msg15107) Jeff Garzik'i etkilemektedir Sonuç olarak, 3 Ekim'de forumda blok boyutu sınırını "PayPal'ın ortalama işlem oranına uyacak şekilde" 7.168 MB'a çıkarmak için bir yama öneriyor Theymos, "bu yamayı uygulamak sizi diğer Bitcoin istemcileriyle uyumsuz hale getirecektir" diyerek yanıt verir Bu mesaj, yamayı kullanmamayı [tavsiye eden] (https://bitcointalk.org/index.php?topic=1347.msg15139#msg15139) ve şunu belirten Satoshi Nakamoto tarafından onaylanmıştır: "İhtiyaç duymaya yaklaşırsak daha sonra bir değişiklik yapabiliriz." İkincisi, ertesi gün böyle bir protokol değişikliğinin nasıl yapılacağına dair yol göstererek düşüncelerini [açıklığa kavuşturur](https://bitcointalk.org/index.php?topic=1347.msg15366#msg15366).


![Message from Satoshi Nakamoto describing an increase in the block size limit in 2010](assets/en/047.webp)


Bu tartışma, sonunda 2015-2017 yılları arasında blok büyüklüğü savaşı olarak bilinen gerçek bir iç savaşa yol açacak olan ölçeklenebilirlik tartışmasının başlangıcına işaret etmektedir.


### Standart Senaryo Kalıpları


Eylül ayında, Satoshi kodda yeni bir kavramı da tanıttı: standart olmayan işlemler. Bunlar, varsayılan olarak yapılandırılmış düğümlerin aktarmadığı, mempool'larında tutmadığı ve ürettikleri bloklara dahil etmediği işlemlerdir. Ancak, bu işlemler geçerli kalır ve tüm ağ bunları içeren blokları kabul eder.


Bu normatif ayrım, programlanabilirlik üzerinde geçici bir kısıtlama pahasına, Bitcoin'ün oldukça zengin olan ve yeterince incelenmemiş olan komut dosyası sistemindeki potansiyel güvenlik açıklarının istismarını sınırlamaya yardımcı olur. Şu anda, iki tür çıktı komut dosyası ağ tarafından standart olarak tanımlanmıştır:



- Madenciler tarafından ve bir IP Address üzerinden transferler için kullanılan açık anahtar (*pubkey*) ile alındı;
- Bir Bitcoin Address üzerinden aktarımlar için kullanılan genel anahtar parmak izi (*pubkey Hash*) aracılığıyla alma.

7 Eylül'de, 0.3.12 sürümünde, Satoshi [dahil] (https://bitcointalk.org/index.php?topic=999.msg12240#msg12240) işlemlerin çok büyük olmamasını veya çok fazla imza operatörü içermemesini gerektiren bir sınırlama getirdi. Bu, kendisinin de açıkladığı gibi, ayrımın ilkel bir uygulamasıydı. Bu, üç ay sonra Gavin Andresen tarafından [resmileştirildi](https://bitcointalk.org/index.php?topic=2129.msg27744#msg27744) ve bir işlemin standart niteliğini doğrulayan bir işlev olan `IsStandard` işlevi koda eklendi. Programlanabilirliğe erişim 2012 yılında P2SH'nın protokole entegre edilmesiyle yeniden sağlanmıştır.


### Bir Gelişim Yazı


Olaylarla dolu bir dönem olan 2010 yazı boyunca Satoshi kendini Bitcoin'nin yazılım geliştirmesine adadı. Bitcoin tanıtım metninin Slashdot'ta yayınlanması, benzeri görülmemiş bir kullanıcı akınına yol açtı ve bu da sistemi risk altına soktu. Sonuç olarak, kurucu ve ona yardımcı olanlar (özellikle Gavin Andresen) güvenlik açıklarını düzeltmek için ellerinden geleni yaptılar. Ancak ağ, yazılım içinde Satoshi tarafından yönetilen bir uyarı sisteminin oluşturulmasına yol açan büyük bir olay olan değer taşması olayından kaçamadı. Son olarak, bu döneme Bitcoin'nin tarihinde temel bir unsur olan blok boyutu sınırının eklenmesi de damgasını vurdu.


Takip eden aylarda, teknik, ekonomik ve Mining iyileştirmeleri ortaya çıktı ve Bitcoin'u yavaş yavaş kolektif bir projeye dönüştürdü. "Bitcoin topluluğu" nihayet özerk bir varlık olarak hayata geçti. Bu dersin bir sonraki bölümünde bu konuyu inceleyeceğiz.


# Bitcoin Topluluğu

<partId>811e7c15-497a-46df-b67b-27eefbc73a63</partId>


## Dijital Altına Hücum

<chapterId>8e9899ca-e7a7-471b-8e69-847a56714d3b</chapterId>


Bir önceki bölümde Bitcoin sunumunun Slashdot'ta yayınlanmasının (slashdotting) yarattığı etkiyi ve Satoshi ile yardımcılarının başlangıçtaki teknik sorunları nasıl yönettiklerini incelemiştik. Yaz sonunda proje fırtınayı atlatmış ve giderek artan sayıda insanı ağırlamaya hazır hale gelmişti. Böylece 2010 sonbaharı Bitcoin için bir başarı dönemi oldu.

Bu dönem özellikle ilk GPU çiftliklerinin ve ilk kooperatifin ortaya çıkmasıyla önemli gelişmelerin yaşandığı Mining için altın bir dönemdi. Kullanılan kaynaklar artıyor ve özel algoritmaların performansı gelişiyordu. Zamanın bir blog yazarının (jimbobway takma adını kullanan) [yazdığı] gibi (https://web.archive.org/web/20100828094955/http://www.bitcoinblogger.com/2010/08/bitcoins-new-digital-gold-rush.html), "binlerce internet kullanıcısının" "servet umuduyla" Mining bitcoinleri olduğunu ve birçoğunun çok zengin olma umuduyla "bitcoinleri daha verimli bir şekilde çıkarmak için yazılım ve donanım araçları geliştirmeye" çalıştığını belirterek, bu bir tür "dijital altına hücum" idi. (*orijinal: "Bitcoins: Yeni Bir Dijital Altına Hücum (...) İnternetteki binlerce kullanıcı şu anda servet umuduyla bitcoin için Mining yapıyor. Birçoğu çok zengin olma umuduyla daha verimli bir şekilde bitcoin madenciliği yapmak için yazılım ve donanım araçları geliştirmeye çalışıyor. "*)


### İlk GPU Çiftliği


Temmuz 2010'da Bitcoin'nın slashdot edilmesinden sonra, fiyat artışından kaynaklanan yüksek mali ödül ve gelecekteki büyüme olasılığı, bireyleri kendilerini daha yoğun bir şekilde Bitcoin üretmeye adamaya teşvik etti. Bu nedenle 11 Temmuz'da 0.22 GH/s olan ağın [Hash oranı] (https://bitinfocharts.com/comparison/Bitcoin-Hashrate.html#alltime) 17'sinde 2.78 GH/s'ye, ardından 15 Ağustos'ta 5.79 GH/s'ye yükseldi ve sonunda 19 Eylül'de 9.94 GH/s'ye ve son olarak 29 Eylül'de 12.58 GH/s'ye ulaştı.


![Total network hash rate from July 11 to October 5, 2010](assets/en/048.webp)

11 Temmuz - 5 Ekim 2010 tarihleri arasındaki toplam ağ Hash oranı (kaynak: [CoinWarz](https://www.coinwarz.com/Mining/Bitcoin/Hashrate-chart))


Bu dönemin en büyük Miner'ü ArtForz adını kullanan bir Alman geliştiriciydi. Slashdot aracılığıyla Bitcoin'yi öğrendikten sonra, hızla yazılım geliştirmeye dahil oldu ve #Bitcoin-dev IRC kanalında çok zaman geçirdi. Özellikle, bilgisayarının grafik kartıyla çalıştırdığı OpenCL ile kendi GPU Mining algoritmasını geliştirdi.

Bitcoin üretmeye 19 Temmuz'da başlamıştır. 25 Temmuz'da, kullanıcıların Bitcoin varlıkları hakkında anket yaptığı bir başlıkta ArtForz [belirtti] (https://web.archive.org/web/20151121004205/https://bitcointalk.org/index.php?topic=564.msg5617#msg5617) 6 günde 1.700 bitcoin üretmişti, bu da Hash oranının %4'üne veya 80 MH/s'ye karşılık geliyordu. Yavaş yavaş, "ArtFarm" olarak bilinen büyük bir Mining çiftliği kurdu Ağustos ayında, çiftliği [dahil] (https://www.ofnumbers.com/2014/04/20/how-artforz-changed-the-history-of-Bitcoin-Mining/) 6 ATI Radeon HD 5770s, 9 Ağustos'ta 76 MH/s'den 13'ünde yaklaşık 450 MH/s'ye çıkmasını sağladı.


![ArtForz's mining production between August and October 2010](assets/en/049.webp)

ArtForz'un Ağustos ve Ekim 2010 tarihleri arasındaki Mining üretimi (kaynak: Blackburn ve diğerleri, "[Ademi merkeziyetçilik başarısızlıkları sırasında Bitcoin'i koruyan anonim bir grup arasındaki işbirliği](https://arxiv.org/pdf/2206.02871)")


Haftalar içinde ArtForz ağın bilgi işlem gücünün önemli bir bölümünü kontrol eder hale geldi. 2 Eylül'de Miner puddinpop [belirtti] (https://bitcointalk.org/index.php?topic=133.msg11957#msg11957) "OpenCL istemcisini kullanan yaklaşık 12 5770'e" sahip olduğunu ve "1 Ghash/s'den daha fazlasına" sahip olduğunu, bunun da kendisine "ağın Hash kapasitesinin %20'sini" verdiğini söyledi (*orijinal: "IRC'deki ArtForz'un kendi OpenCL istemcisini çalıştıran 12 kadar 5770'i var. Tüm ağ 5-6Ghash/s civarında bir şey yapıyor ve tek başına 1Ghash/s'nin üzerinde olduğunu belirtti. "*) 23 Eylül'de ArtForz [beyan etti] (https://web.archive.org/web/20180118035138/http://bitcoinstats.com:80/irc/Bitcoin-dev/logs/2010/09/23#l1285234390.0) yaklaşık 2 GH/s'lik bir Hash oranına sahipti ve hala hashing'in %20'sini temsil ediyordu. 3 Ekim'de theymos [belirtti] (https://bitcointalk.org/index.php?topic=1327.msg15118#msg15118) ArtForz'un "ağın işlem gücünün %20 ila 30'una sahip olduğunu" (*orijinal: "ağın CPU gücünün %20-30'una sahip "*)

Ancak sonbaharda sistemlerini güncelleyen diğer kişiler bu pozisyona hızla meydan okudu. Daha sonra ArtForz yazılım geliştirmeye odaklanmak için Mining faaliyetlerinden yavaş yavaş uzaklaştı. Ağustos 2011'de, ağın bilgi işlem gücünün %1'inden daha azına sahip olduğunu [belirtmiştir](https://bitcointalk.org/index.php?topic=37904.msg478671#msg478671).


### Mining Uzmanlık


2010 yazının sonunda, ArtForz'un örneği, grafik işlemcileriyle generate bitcoinleri için kendi yöntemlerini geliştirmek için acele eden diğer madencilere ilham verdi. Bunu yapmak için madenciler CUDA ya da OpenCL gibi programlama ortamlarını kullandılar. Bu sayede MH/s ile ölçülen hesaplama gücüne ulaştılar ve toplam gücün önemli bir bölümünü temsil ettiler.


2 Eylül'de Miner puddinpop [paylaştı](https://bitcointalk.org/index.php?topic=133.msg11940#msg11940) Mining istemcisinin çalıştırılabilir dosyasını CUDA kullanarak bir algoritmadan yararlandı. Bunu kullanan herkes için %10 ücret talep etti. Bu yaklaşım, özgür yazılım savunucusu olan forum üyeleri tarafından pek hoş karşılanmadı.


6 Eylül'de, bir forum üyesinin önerisi üzerine, "önemli bir bağış" alması halinde "kodu açık kaynak haline getirmeye istekli olabileceğini" [belirtmiştir](https://bitcointalk.org/index.php?topic=133.msg12107#msg12107) Ayın 15'inde Jeff Garzik bu konuda bir [teklif](https://bitcointalk.org/index.php?topic=133.msg12921#msg12921) yaptı ve puddinpop'a 10.000 bitcoin, yani o tarihte yaklaşık 600 dolar vermeyi önerdi. Puddinpop kabul etti: işlem 18'inde [gerçekleşti](https://Mempool.space/tx/f79314da84567196905f6e061e2bc9f3ee8b30d40f7b80dac90fcb1f4b4c71ea) ve algoritma kısa bir süre sonra puddinpop tarafından ücretsiz bir lisans altında [yayınlandı](https://bitcointalk.org/index.php?topic=133.msg13135#msg13135).

Diğer algoritmalar da aynı tarihlerde kamuoyuna duyuruldu. 9 Eylül'de nelisky adında bir forum üyesi CUDA kullanarak Mining algoritmasını [paylaştı](https://bitcointalk.org/index.php?topic=1009.msg12264#msg12264). 1 Ekim'de, foruma Şubat ayında katılan m0mchil adlı bir kişi, algoritmasını (POCLBM) "kitleler için OpenCL Miner" olarak tanımlayarak [yayınladı](https://web.archive.org/web/20101206143359/http://www.Bitcoin.org/smf/index.php?topic=1334.0)


Bu gelişme, teknik açıdan en yetenekli kişilerin generate'ye çok sayıda bitcoin kazandırmasını sağladı. ArtForz'un yanı sıra, Nils Schneider (tcatm) bu dönemin başlıca madencilerinden biri haline gelmiştir. 3 Ekim 2010 tarihinde, üç grafik işlemci tarafından üretilen 983 MH/s'lik bir hash oranına sahip olduğunu [iddia etti](https://bitcointalk.org/index.php?topic=1327.msg15111#msg15111). Bu sayı [şaşırtıcı](https://bitcointalk.org/index.php?topic=1327.msg15112#msg15112) Satoshi'ün kendisini etkiledi.


### İlk Mining Havuzları


Mining uzmanlaşmasına bağlı olarak Hash oranındaki büyük artış, merkezi bir işlemciyle bitcoin üretmeyi zorlaştırdı ve bu da giderek daha uygun fiyatlı hale geldi. Gerçekten de, bitcoin üretme olasılığı varyansa daha bağımlı hale geldi ve bazı bireyler asla bir blok üretmeyi başaramadı. Bu sorunun çözümü kooperatif Mining'tir.


1 Ekim'de m0mchil [yayınladı] (https://bitcointalk.org/index.php?topic=1333.msg14840#msg14840), istemci düğümlerinin `getwork' adlı yeni bir işlev aracılığıyla bir aday bloğu almasına ve bir çözüm bulunursa Proof of Work'yi döndürmesine olanak tanıyan API'de bir değişiklik yaptı. Bu düzeltmenin "harici Bitcoin madencilerinin önünü açtığını" ve "bir istemci için birden fazla madencinin kurulmasına izin verdiğini" yazdı

Aynı gün, "havuzlanmış Mining" fikri ilk kez bir forum üyesi tarafından "GPU Oligarkları Nasıl Devrilir" başlıklı bir başlıkta [dile getirildi](https://bitcointalk.org/index.php?topic=1332.msg14838#msg14838). 13 Ekim'de puddinpop [önerdi](https://bitcointalk.org/index.php?topic=1458.msg16906#msg16906) bu türden bir model. Miner'nin hesaplama gücü, her bir Hash bloğunun ilk baytını içeren bir tamponun damgası olan bir meta-Hash kullanılarak ölçülür. Sunucu daha sonra periyodik olarak istemcinin tanımlanan hesaplamayı gerçekleştirdiğini doğrulayabilir. Bu model karmaşıktır ve [hataya izin vermez](https://bitcointalk.org/index.php?topic=1458.msg17015#msg17015).


Bununla birlikte, kısmi Proof of Work, bir müşterinin Hash oranını ölçmenin çok daha basit bir yoludur. Bu yöntem puddinpop'un açıklamasını takiben ribuck, Nils Schneider ve Gavin Andresen tarafından [önerilmiştir] (https://bitcointalk.org/index.php?topic=1458.msg16951#msg16951). Aynı aday bloktan üretilen ağ zorluğundan daha düşük dereceli işin kısmi kanıtlarının alınmasını içerir. Toplanan kısmi kanıtlar, harcanan gücün olasılıksal bir tahminine izin verir.


23 Kasım'da `getwork' fonksiyonunun değiştirilmiş bir versiyonu [code](https://bitcointalk.org/index.php?topic=1901.msg23876#msg23876)'a eklendi ve 25'inde ana yazılımın yeni versiyonuna ([v0.3.17](https://bitcointalk.org/index.php?topic=1946.msg24460#msg24460)) dahil edildi. Aynı gün, Jeff Garzik (zincir yönetimi ve Mining'ü yazılım içinde ayırma fikrini [savunan](https://bitcointalk.org/index.php?topic=1688.msg20532#msg20532)) [bu işlevi kullanan CPU Mining yazılımını](https://bitcointalk.org/index.php?topic=1925.msg24217#msg24217) paylaştı.


27 Kasım'da, Marek Palatinus adlı genç bir Çek geliştirici, slush takma adını kullanarak, forumda `getwork' ve Jeff Garzik'in mantığından yararlanan bir model olan "kooperatif Mining "nin bir tanımını [yayınladı] (https://web.archive.org/web/20101206144824/http://www.Bitcoin.org/smf/index.php?topic=1976.0). Bu model, madenciler tarafından üretilen kısmi çalışma kanıtlarına dayanmaktadır (paylaşım başına ödeme). Ertesi gün, Satoshi Nakamoto konsepti [onayladı] (https://bitcointalk.org/index.php?topic=1976.msg25119#msg25119).


![Marek Palatinus (slush) at the Z-DAY conference in Prague on May 11, 2013](assets/en/050.webp)

Marek Palatinus (slush) 11 Mayıs 2013 tarihinde Prag'da düzenlenen Z-DAY konferansında


İki tahmin modeli Aralık ayında uygulanmıştır. İlk olarak, puddinpop konsepti 1 Aralık'ta doubled adlı kullanıcı tarafından uygulandı ve bu kullanıcı [davet etti](https://bitcointalk.org/index.php?topic=2027.msg25859#msg25859) kişileri havuzlanmış Mining sunucusuna bağlanmaya çağırdı. Oluşturulan grup 4 Aralık'ta ilk bloğunu (95.420) [üretti](https://bitcointalk.org/index.php?topic=2027.msg26688#msg26688). Birkaç gün sonra bir blok daha ürettikten sonra, doublec'in sunucusu ayın 15'inde [kapatıldı](https://bluishcoder.co.nz/Bitcoin-pool/). Hizmet, çok daha verimli bir kooperatifin ortaya çıkması nedeniyle 17'sinde kapılarını kalıcı olarak kapattı: Bitcoin.cz Mining.


Forumu inceledikten sonra Marek Palatinus, Mining kooperatif modelini uygulamaya karar verdi ve özellikle test ağı üzerinde denemeler yaptı. Ayrıca sunucunun CPU madencileri (Jeff Garzik'in yazılımı) ve GPU madencileri (m0mchil ve puddinpop'un istemcileri) tarafından erişilebilir olmasını sağladı.


Kooperatif 15 Aralık'ı 16 Aralık'a bağlayan gece Marek Palatinus tarafından ana ağda nihayet [başlatıldı](https://bitcointalk.org/index.php?topic=1976.msg30520#msg30520). İlk blok 16'sı sabahı [bulundu](https://bitcointalk.org/index.php?topic=1976.msg30655#msg30655) (97,834). Daha sonra birçok başka blok üretildi. Mining grubu başlangıçta başarılı oldu: birkaç gün içinde Hash oranı 4 GH/s'ye, yani toplam ağ gücünün %3.5'ine ulaştı.


Kooperatif, Bitcoin Mining'te bir ölçüt haline gelecektir. Yıllar boyunca çeşitli isimler [taşıdı] (https://en.Bitcoin.it/w/index.php?title=Slush_Pool&action=history): Bitcoin Pooled Mining (BPM), Bitcoin.cz Mining ve son olarak yaratıcısı hakkında Slush Pool. Eylül 2022'de Braiins Pool adını almıştır.


![Logo of Slush's cooperative in September 2011](assets/en/051.webp)

Slush kooperatifinin Eylül 2011'deki logosu (kaynak: sitenin [arşivi](https://web.archive.org/web/20110923151034/http://Mining.Bitcoin.cz:80/))


### Mining'de İleriye Doğru Büyük Atılım

Böylece, 2010 yılının ikinci yarısı Mining için önemli bir büyümeyi temsil etmiştir. GPU (Grafik İşlem Birimi) üretiminin benimsenmesinde uzmanlaşmıştır. ArtForz ve onun "ArtFarm "ı gibi birkaç kişi gerçek Mining çiftliklerine odaklandı ve kurdu Bu patlama sonunda kooperatiflerin ortaya çıkmasına yol açtı ve küçük madencilerin ödüllerin varyansını azaltmak için hesaplama güçlerini bir araya getirmelerine olanak tanıdı.


Ancak, sonbahar tek başarılı Mining yöntemi değildi. Aynı zamanda toplum ve ekonomik ekosistem için de bir başarıydı ki bunu bir sonraki bölümde ele alacağız.


## Ekosistemin Çiçek Açması

<chapterId>0404f877-8b5c-4c7f-81ab-a4e6d9b3da9c</chapterId>


Bir önceki bölümde Mining'in 2010 yılının ikinci yarısında nasıl geliştiğini incelemiştik. Sonbaharda bu ilerleme iyice yerleşmişti. Ancak, Bitcoin'in başarıya ulaşan tek yönü Mining değildi: ekosistemi de başarıya ulaştı.


Burada ilk olarak Address'nin uluslararası ihracatının başlangıcını Rus ve Fransız topluluklarının gelişimi ile ele alacağız. Daha sonra Bitcoin'ün birim fiyatında yeni bir artışa yol açan iletişim ve ekonomik büyümedeki gelişmeleri tartışacağız. Son olarak, Satoshi'ün ayrılışından önceki iki sembolik olaydan bahsedeceğiz: Electronic Frontier Foundation'ın Bitcoin'ü kabul etmesi ve Hal Finney'in dönüşü.


### Diğer Dillerde Bitcoin


Bitcoin uluslararası bir projedir ve bu nedenle İngilizce konuşulan alanın dışında mümkün olduğunca çok kişi tarafından erişilebilir olmalıdır. Bu nedenle topluluk [koordineli] (https://bitcointalk.org/index.php?topic=151.msg1259#msg1259) Mayıs 2010'da web sitesini ve yazılımın grafiksel Interface'sını çeşitli dillere çevirmeye başladı. İtalyanca, Almanca ve Hollandaca özellikle dahil edildi.


Ama hepsi bu kadar değil. Martti Malmi, Temmuz ayının sonunda İngilizce konuşmayanlara yönelik alt forumlar oluşturmaya başladı. Rus topluluğu ilk kurulan topluluk oldu: belirli bir bitcoinex'ten gelen bir talebi takiben, özel alt forum 28 Temmuz'da [oluşturuldu](https://bitcointalk.org/index.php?topic=151.msg6241#msg6241). Ardından, diğer dil topluluklarına adanmış [tartışma konuları](https://web.archive.org/web/20101018144227/http://www.Bitcoin.org:80/smf/index.php?board=11.0) oluşturuldu: Ağustos ayında İtalyanca, Hollandaca, Japonca ve Katalanca; Eylül ayında İspanyolca; ve son olarak Ekim ayında Almanca. Ancak hiçbir grup Rus topluluğuyla eşleşmedi ve sadece birkaç mesaj alışverişi yapıldı.


Fransız toplumunda işler, özellikle bir kişinin eylemleriyle değişti: Grondilu takma adıyla da bilinen Lucien Grondin. 26 Eylül'de Bitcoin'u keşfetti ve proje hakkında hemen heveslendi. Akşam geç saatlerde [IRC'de] (https://web.archive.org/web/20131201235643/http://www.bitcoinstats.com/irc/Bitcoin-dev/logs/2010/09/26#l1285544830) yazdı:


> "\[G\]osh Uyuyamıyorum! Bu harika şeyi düşünüp duruyorum. Bana göre Bitcoin "cyperspace gold" \[sic\]. Hayretler içindeyim."

Birkaç gün sonra, ayın 30'unda LinuxFr.org'da (DLFP) Fransızca bir [haber bülteni] (https://linuxfr.org/news/connaissez-vous-les-bitcoins) yayınladı. "Bitcoins hakkında bilginiz var mı?" başlıklı bu yayın, muhtemelen Bitcoin'in Molière dilinde yazılmış ilk sunumudur. Makale çok sayıda kişiye ulaşarak yaklaşık 350 yorum aldı. İşte o zamanki [göründüğü] (https://web.archive.org/web/20101003105210/http://linuxfr.org/2010/09/30/27430.html) haliyle ilk paragraf:


![Do you know about bitcoins?](assets/en/052.webp)


> **Makaleler: Bitcoin'i biliyor musunuz?** Bitcoin, 2009 yılında Satoshi Nakamoto adlı biri tarafından tasarlanmış elektronik bir para birimidir. Bu para birimi, tamamen merkeziyetsiz peer-to-peer yapısı ve temel kriptografik kavramların akıllıca kullanımıyla diğer elektronik paralardan ayrılır. C++ ile yazılmış ve özgür MIT lisansı altında yayımlanmış bir yazılıma dayanır.

Bu gönderi özellikle 29 yaşında Belçikalı bir blog yazarı ve özgür yazılım savunucusu olan gerçek adı Lionel Dricot olan Ploum'un dikkatini çekmektedir. 25 Ekim'de blogunda "Geek Currency, Monkey Money?" başlıklı bir makale [yayınladı] (https://ploum.net/monnaie-de-geek-monnaie-de-singe/) ve bu makalede ademi merkeziyetçiliği savunuyor ve Bitcoin ilkesini destekliyor. Fransızca konuşan pek çok internet kullanıcısı, 2017 yılında Bitcoin Cash'i yaratacak olan geliştirici [Amaury Séchet](https://www.reddit.com/r/Bitcoincash/comments/6y7ssg/ama_i_am_amaury_s%C3%A9chet_udeadalnix_bitcoin_abc/dml9h55/) de dahil olmak üzere Bitcoin'yi bu yolla duydu.


![Lionel Dricot (Ploum) in 2012, then a candidate under the banner of the Pirate Party for the Belgian communal and provincial elections](assets/en/053.webp)

Lionel Dricot (Ploum) 2012'de, o zaman Korsan Parti bayrağı altında Belçika belediye ve il seçimleri için aday (kaynak: [Framablog](https://framablog.org/2012/10/10/lionel-dricot-ploum-parti-pirate-belgique/))


Aynı gün Ploum, Bitcoin forumunda [tartışma başlığı] (https://bitcointalk.org/index.php?topic=1567.0) "Fransızca" açtı. Fransızca konuşan forum üyelerinden gelen mesajlar sonraki aylarda arttı. Özellikle, 17 Ekim'de kaydolan ve Bitcoin-Central'in gelecekteki kurucusu David François ([davout](https://bitcointalk.org/index.php?topic=1567.msg21218#msg21218)) ve 7 Kasım'da kaydolan ve Mt. Gox platformunun gelecekteki sahibi Mark Karpelès ([MagicalTux](https://bitcointalk.org/index.php?topic=1567.msg29336#msg29336)) katıldı. Ayrıca 23 Aralık'ta [Bitcoin.fr](https://web.archive.org/web/20110107145746/http://www.Bitcoin.fr:80/) sitesini açacak ve Ocak ayında [promote](https://bitcointalk.org/index.php?topic=1567.msg37524#msg37524) etmeye başlayacak olan Jean-Luc'un da katılımı görüldü. Sonunda Martti Malmi tarafından 1 Şubat 2011 tarihinde bir [Fransızca alt forum](https://web.archive.org/web/20110217005824/http://www.Bitcoin.org/smf/index.php?board=13.0) oluşturulacaktır.


### İletişimin Gelişimi

Dilsel toplulukların gelişimine ek olarak, Bitcoin hakkında iletişim için kullanılan yöntemlerde de belirli bir yenilik söz konusudur. 4 Ekim'de noagendamarket takma adını kullanan 38 yaşındaki bir Avustralyalı BitcoinMedia adlı bir girişimi [başlattı] (https://bitcointalk.org/index.php?topic=1355.msg15217#msg15217). Amaç, içerik oluşturarak ve izleyici çekmesi muhtemel yerlerde reklamını yaparak Bitcoin'ü tanıtmaktı. Bu girişim beklenen başarıyı yakalayamamış olsa da, Bitcoin'ten bahseden ilk videoların üretilmesine öncülük etme değerine sahiptir. Kanalın 5 Ekim'de [yayınlanan] (https://bitcointalk.org/index.php?topic=1355.msg15461#msg15461) ilk videosu, YouTube aracı kullanılarak oluşturulmuş bir Google Arama Hikayesidir (aşağıdaki ekran görüntüsüne bakın). Diğer videolar, önceden tasarlanmış bir dizi karakter ve ortamdan video dizileri oluşturmak için kolay bir araç olan Xtranormal ile oluşturulacak.


![First video on Bitcoin (Google Search Story)](assets/en/054.webp)


Bitcoin ile ilgili blog yazıları bu dönemde çoğalıyor. Bu durum özellikle dijital para birimleri, serbest bankacılık ve kriptografi konularını tartıştığı *The Monetary Future* adlı blogu yöneten Jon Matonis için geçerli. Mart ayında Bitcoin'i keşfetti ve Satoshi ile [değiş tokuş] (https://web.archive.org/web/20140511100607/https://bitcoinfoundation.org/forum/index.php?/topic/54-my-first-message-to-Satoshi/#entry514) yaptı, ardından konu hakkında yazmaya başladı. Ekim ayında, fiyat artışından bahsettiği ve ekosistemin yeniliklerini detaylandırdığı bir [üçüncü makale](https://themonetaryfuture.blogspot.com/2010/10/rally-in-Bitcoin.html) yayınladı.


![Profile picture of Jon Matonis in 2011](assets/en/055.webp)

Jon Matonis'in 2011 yılındaki profil resmi (kaynak: [Forbes](https://www.forbes.com/sites/jonmatonis/))


Şu anda, yeni bir Bitcoin logosu da önerilmiştir. 1 Kasım'da bitboy takma adını kullanan bir forum üyesi, kripto para birimini vurgulamak için Elements grafiğini [yayınladı] (https://bitcointalk.org/index.php?topic=1631.0). Bu Elements'lerden biri, B harfinin üzeri çizilmiş ve hafifçe eğilmiş turuncu bir logodur:


![Bitcoin logo designed by bitboy, November 2010](assets/en/056.webp)


### Büyüyen Bir Ekonomi

Bu dönem aynı zamanda ekosistemin ekonomik düzeyde kayda değer bir büyüme gösterdiği bir dönemdir. 2010 sonbaharında Mt. Gox, Bitcoin Market ve diğerleri gibi platformlar mevcuttu, ancak bu yeterli değildi. Tezgah üstü borsalar bu şekilde çoğalmaya başladı. Forumdaki özel mesajlar aracılığıyla yapılan alışverişlerin yanı sıra, biraz daha titiz bir sistem uygulanır: #Bitcoin-otc. Bu, 18 Ekim'de nanotube adını kullanan bir kullanıcı tarafından Freenode'da [açılan] (https://bitcointalk.org/index.php?topic=1491.msg17508#msg17508) bir IRC kanalıdır. Sipariş defteri [ilişkili web sitesinde] (https://web.archive.org/web/20101027090714/http://Bitcoin-otc.com/vieworderbook.php) barındırılır ve takaslar, çeşitli ödeme yöntemleri (PayPal, Liberty Reserve) aracılığıyla emanet depozitosu olmadan doğrudan taraflar arasında gerçekleşir. Bitcoin'u kabul eden hizmetlerin sayısı da, resmi sitenin listeleme sayfasının [kanıtladığı](https://web.archive.org/web/20101120224505/http://www.Bitcoin.org/trade) gibi, nispeten düşük kalsa bile artmaktadır.

Tüm bu Elements, fiyatın büyük ölçüde artmasına yol açıyor. Ağustos ayından bu yana 6 sent civarında sabitlenmişken, Ekim ayının başında yükselmeye başlar. Ay sonunda 10¢'e çıkarak 20¢'e ulaşır. 6 Kasım'da, forum üyelerini [heyecanlandırmaktan] (https://bitcointalk.org/index.php?topic=1681.0) geri kalmayan 50¢'i aşar.


![BTC Price between July 18 and October 18, 2010 on Mt. Gox](assets/en/057.webp)

Mt. Gox'ta 18 Temmuz ve 18 Ekim 2010 tarihleri arasında BTC Fiyatı (kaynak: [*The Monetary Future*](https://themonetaryfuture.blogspot.com/2010/10/rally-in-Bitcoin.html))


Bitcoin'nin yükselişi, fiyat, zincirdeki faaliyet veya Mining açısından her şeyin ölçülmeye başlandığı anlamına geliyor. Herkes ekosistemin bir miktar büyüme yaşadığını biliyor, ancak kimse bunu nasıl doğru tahmin edeceğini bilmiyor. Bu nedenle 2010 yılının ikinci yarısında ve 2011 yılının başında aralarında başlıcalarının da bulunduğu hizmetler ortaya çıkmıştır:



- Bitcoin Watch ([bitcoinwatch.com](https://web.archive.org/web/20100816161306/http://www.bitcoinwatch.com/)), Jeff Garzik (jgarzik) tarafından [geliştirilen](https://bitcointalk.org/index.php?topic=734.msg7954#msg7954) bir istatistik toplayıcısı;
- Bitcoin Charts ([bitcoincharts.com](https://web.archive.org/web/20101119023257/http://bitcoincharts.com/markets/)), 4 Kasım'da Nils Schneider (tcatm) tarafından bir fiyat izleme ve grafik ekranı Interface [başlatıldı](https://bitcointalk.org/index.php?topic=1659.0);
- Bitcoin Block explorer ([blockexplorer.com](https://web.archive.org/web/20101128030227/http://blockexplorer.com/)), 10 Kasım'da Theymos tarafından [kurulan](https://bitcointalk.org/index.php?topic=1727.msg21124#msg21124) ve herkesin bir web tarayıcısı ile Bitcoin bloklarının içeriğine ve işlemlerine erişmesine olanak tanıyan bir Block explorer;
- Bitcoin Ağ Grafikleri ([Bitcoin.sipa.be](https://web.archive.org/web/20110310155417/http://Bitcoin.sipa.be/)), 28 Ocak 2011 tarihinde Pieter Wuille (sipa) tarafından Bitcoin Hash oranının gelişiminin grafiklerini gösteren bir site [başlatıldı](https://bitcointalk.org/index.php?topic=3024.msg42173#msg42173);
- Bitcoin Monitor ([bitcoinmonitor.com](https://web.archive.org/web/20110605105433/http://www.bitcoinmonitor.com/)), işlemler, bloklar ve Exchange operasyonları için gerçek zamanlı bir görselleştirme aracı, Jan Vornberger (jav) tarafından 6 Şubat 2011 tarihinde [çevrimiçi](https://bitcointalk.org/index.php?topic=3218.msg45150#msg45150).


Bitcoin'ün başarısına işaret eden son bir unsur da bazılarının onun sınırlarını test etmeye çalışmasıdır. Bireyler 15-26 Kasım tarihleri arasında günlük sayıları binleri bulan bir işlem seli yaratarak kendilerini eğlendirdiler. Bu olağanüstü faaliyet 19'unda Jeff Garzik tarafından [rapor edildi] (https://bitcointalk.org/index.php?topic=1850.msg22870#msg22870). Bu durum Satoshi'i, Interface işlem ücretini [geri yükleyerek](https://bitcointalk.org/index.php?topic=1946.msg24460#msg24460) ve ücretsiz işlemlere sınırlar getirerek önlemler almaya zorladı.


### Electronic Frontier Foundation Bitcoin'yı kabul ediyor


2010 yılının sonunda Electronic Frontier Foundation'ın Bitcoin'yi kabul etmesi önemli bir olaydı. Bu kuruluş 1900 yılında Mitch Kapor, John Gilmore ve John Perry Barlow tarafından kurulmuş, İnternet üzerindeki özgürlükleri korumaya yönelik uluslararası bir organizasyondur. Bu, özünde cypherpunk olan Bitcoin'yi ilk benimseyenler için özellikle önemliydi. Bitcoin'yi kabul etmeye hevesliydiler.


![Logo of the Electronic Frontier Foundation](assets/en/058.webp)


Kiba adlı forum üyesi, 13 Ağustos 2010 tarihinde EFF ile temasa geçmeyi [teklif ederek](https://bitcointalk.org/index.php?topic=804.msg9021#msg9021) ve topluluktan [toplanan](https://bitcointalk.org/index.php?topic=778.msg8578#msg8578) bir bağışı kabul etmelerini önererek inisiyatif aldı. Bu amaçla, MyBitcoin'de bir [hesap](https://Mempool.space/Address/1MCwBbhNGp5hRm5rC1Aims2YFRe2SXPYKt) oluşturdu ve burada fonları topladı ve EFF'ye erişimi transfer etmek istedi. Ağustos sonunda gönderdiği (topluluk tarafından düzeltilen) bir e-posta taslağı hazırladı.


İki hafta sonra ikinci bir forum üyesi yardımına koştu ama yanıt alamadı. BrightAnarchist takma adını kullanan bu üye, kuruculardan birini tanıyordu ve 13 Eylül'de onlara e-posta gönderdi. Aynı gün bir yanıt aldı ve forumda "EFF kesinlikle Bitcoin almakla ilgileniyor!" diye [yazdı] (https://bitcointalk.org/index.php?topic=804.msg12631#msg12631) Hesap daha sonra organizasyona aktarıldı.


EFF'nin kamu bağışlarını kabul etmeye başlaması biraz zaman aldı. Müzakerelerin ardından, topluluk onları web sitelerinde bir bağış Address yayınlamaya ikna etti. 9 Kasım'da Address [bağış sayfasında](https://web.archive.org/web/20101130105838/http://www.eff.org/helpout) göründü. Bitcoin users [began](https://Mempool.space/tx/8ca2d206bc41b9ffa36cf4ea9ce9d3b0751fd653b6ec8f2979bfdddc4a631731) transferring funds.


Birkaç gün sonra, blog yazarı jimbobway tarafından konuyla ilgili olarak Bitcoin'e dikkat çeken bir [yazı](https://web.archive.org/web/20101117060233/http://www.bitcoinblogger.com/2010/11/Bitcoin-gains-legal-protection-through.html) yazıldı. Bu makale HackerNews'te [paylaşıldı](https://news.ycombinator.com/item?id=1905522). Ayrıca BitcoinMedia tarafından Xtranormal kullanılarak videoya dönüştürülmüştür:


:::video id=03dfd302-1e05-4cad-a91a-e5e65f1d0932:::


Her iki girişim de ortak değerleri paylaştığı için bu Bitcoin için çok iyi bir haber. Ayrıca EFF, Tor ve BitTorrent gibi gizliliğin korunması ve veri paylaşımı projelerine yasal koruma sağlamasıyla tanınmaktadır. Satoshi Nakamoto'nun kendisi de bunun farkındadır ve 6 Ocak 2011 tarihinde Gavin Andresen'e gönderdiği e-postalardan birinde yaptığı [yorum](https://mmalmi.github.io/Satoshi/#email-254)'da da görüldüğü gibi kuruluşun eylemlerini özellikle desteklemektedir:

> "EFF gerçekten çok önemli. Onlarla iyi ilişkiler sürdürmek istiyoruz. Takdir ettikleri bir projeyiz; TOR projesine yardımcı oldular ve P2P dosya paylaşımını korumak için çok şey yaptılar."

### Hal Finney'in Dönüşü


Nisan 2009'da Bitcoin'den ayrıldıktan sonra Hal Finney kısa süre içinde kendisine ALS teşhisi konulduğunu öğrenir; [teşhis] (https://www.lesswrong.com/posts/bshZiaLefDejvPKuS/dying-outside) Ağustos 2009'da konmuştur. Yaşam tarzını buna göre adapte eder, ancak motor becerileri giderek azalır.


30 Kasım'da Bitcoin forumuna kaydolur ve özellikle BitDNS projesiyle ilgili olan tartışmalara katılmaya başlar. Ekosistemde gelişen çeşitli projelere bağış yapmaktan çekinmez.


Dahası, lansmandan bu yana bakmadığı kodu inceler ve yapılan tüm çalışmaların farkına varır. Bu farkındalık onu 11 Aralık'ta forumda aşağıdaki yorumu [yazmaya] (https://bitcointalk.org/index.php?topic=2188.msg29223#msg29223) sevk eder:

> "Bu bana etkileyici bir iş gibi görünüyor, ancak daha fazla yorum olmasını isterdim. Çoğunlukla init, main, script ve biraz da net modüllerini inceledim. Bu çok güçlü bir makine."

İki saat sonra, Satoshi [yanıtlar](https://bitcointalk.org/index.php?topic=2188.msg29259#msg29259):

> "Bunu senden duymak çok anlamlı, Hal. Teşekkür ederim."

Bu, birkaç ay sonra ortadan kaybolacak olan Bitcoin'nin yaratıcısının sondan bir önceki kamu mesajıydı.


### Önemli Bir An

2010 sonbaharında Bitcoin'i çevreleyen ekosistem önemli ölçüde gelişti. İletişim iyileşti ve ekonomi gelişti. O dönemde Bitcoin kendi başına yola çıkmaya hazır görünüyordu. Tam da bu dönemde Satoshi ortadan kaybolmayı ve projenin dizginlerini topluluğa bırakmayı seçti.


## Satoshi'ün Ortadan Kaybolması

<chapterId>f7735239-4887-468f-9f06-1b07d00b30d9</chapterId>


Metnin Temmuz 2010'da Slashdot'ta yayınlanmasının ardından Bitcoin'ün nasıl uçuşa geçtiğini gördük. Sonbaharda yazılım, Mining ve ekonomideki çeşitli ilerlemelerle proje nihayet doğru yoldaydı. Bu nedenle bu dönem Satoshi Nakamoto'nun kademeli olarak geri çekilmesiyle aynı zamana denk geldi.


Bitcoin'nin yaratıcısının ayrılışının iki nedeni vardı: bir yandan statüsüne yönelik artan meydan okuma, daha ademi merkeziyetçi ve rızaya dayalı yönetim çağrısı; diğer yandan devlet yetkililerinden neredeyse paranoyakça korkması. Bu ikinci motivasyon özellikle Aralık 2010'da, artık geleneksel yollarla fon alamayan ve Bitcoin'nin uygun bir alternatif araç sağladığı WikiLeaks'in mali ablukası bağlamında ifade edildi. Bu bölümde, bu kayboluşun ortaya çıkışını ayrıntılı olarak anlatacağız.


### Kurucunun Statüsüne Meydan Okuma


2010'un ikinci yarısından itibaren geliştirme topluluğu, günlükleri Christian Decker'ın [Bitcoin Stats] (https://web.archive.org/web/20131201235340/http://www.bitcoinstats.com/irc/Bitcoin-dev/logs/2010/09) sitesinde yayınlanan #Bitcoin-dev kanalında toplandı. Bu kanal, Exchange'in teknik yönleri konusunda en rahat olanların Bitcoin hakkındaki ayrıntıları daha gayri resmi bir şekilde tartışmaları için ideal bir yerdi. Uzman madencileri (ArtForz, Diablo-D3, knightmb veya Nils Schneider gibi), protokolle ilgilenen geliştiricileri (Gavin Andresen, Jeff Garzik veya Wladimir van der Laan gibi) veya Bitcoin üzerinde hizmet sağlayan kişileri (Jed McCaleb, Michael Marquardt veya nanotube gibi) bir araya getirdi.


Bununla birlikte, Satoshi Nakamoto'nun hiçbir zaman onunla bağlantısı olmadı, bu nedenle orada konuşma forumdakinden daha özgürdü. Sık sık Satoshi'in geliştirme kararlarının sorgulandığı ve hatta Bitcoin'a göre statüsünün eleştirildiği oluyordu.

Satoshi gerçekten de açık kaynak yazılım dünyasında "[Yaşam için Hayırsever Diktatör] (https://fr.wikipedia.org/wiki/Benevolent_Dictator_for_Life)" olarak bilinen projenin belirlenmiş lideridir Onun rolü, herkes için kararlar alarak açık geliştirmenin istikrarını sağlamaktır, bu da isyan ve bölünme riskini sınırlar. Gavin Andresen tarafından [açıklandığı](https://buildingbitcoin.org/Bitcoin-dev/log-2010-09-27.html#l-528) gibi, o "kapı bekçisi "dir: "tüm kodlar ondan geçer."


Bununla birlikte, Bitcoin'ün kaynak kodu ücretsizdir, bu nedenle herkes onu kopyalayabilir ve değiştirebilir, bu da protokolün evriminin tamamen keyfi olmasını önler. Jeff Garzik tarafından 19 Kasım tarihinde [ifade edildiği] gibi (https://buildingbitcoin.org/Bitcoin-dev/log-2010-11-19.html#l-1538):


> "Satoshi hiç yoktan sihirli sayılar buldu ve biz de toplu olarak bu yönü destekliyoruz. [...] Satoshi'in topluluk tarafından desteklenmeyen çılgınca bir şey yaptığı an, protokolün/kod tabanının gerçekten çatallandığı andır."

Dolayısıyla, Satoshi'nin liderlik rolü eleştirilerin yapılmasını engellemiyor. Bu nedenle Temmuz ayından itibaren toplulukta yavaş yavaş gerginlikler ortaya çıkıyor. Örneğin, Ağustos ayında uyarı sisteminin [konuşlandırılması](https://bitcointalk.org/index.php?topic=898.msg10745#msg10745) veya Kasım ayında m0mchil'in `getwork' işlevinin [değiştirilmesi](https://bitcointalk.org/index.php?topic=1901.msg24050#msg24050) sırasında itirazlar ortaya çıkıyor. Bu diktatörce karar alma sürecine ilişkin hayal kırıklığı bazen IRC'de [çok daha açık bir şekilde](https://buildingbitcoin.org/Bitcoin-dev/log-2010-11-24.html#l-384) ifade edilmektedir.


Satoshi'a yakın olan ancak diğer geliştiricilerle de tartışan Gavin, bu durumun yarattığı sorunu açıkça görmektedir. 27 Eylül 2010'da IRC'de Gavin "Satoshi'u daha işbirlikçi bir geliştirme modeline geçmeye ikna edebilmeyi" istediğini [beyan eder](https://buildingbitcoin.org/Bitcoin-dev/log-2010-09-27.html#l-522) (*orijinal: "Keşke onu daha işbirlikçi bir geliştirme modeline geçmeye ikna edebilseydim. "*) Ekim ayında Gavin, SourceForge deposuna yazma erişimini [elde eder](https://sourceforge.net/p/Bitcoin/code/165/) ve işler düzelir. Aralık ayında, WikiLeaks olayının patlamasının ardından Satoshi'un ani çekilmesiyle sorun çözüldü.

### WikiLeaks Olayı


Satoshi'in ayrılışını tetikleyen olay WikiLeaks olayıdır. WikiLeaks, 2006 yılında Cypherpunk Julian Assange tarafından kurulan ve kaynaklarını koruyarak muhbirlere ve bilgi sızıntılarına ses vermeyi amaçlayan bir sivil toplum kuruluşudur. 2010 yılı boyunca, STK tarafından ortaya çıkarılan gizli belgeler büyük medya tarafından aktarıldı ve kamuoyunda heyecan yarattı. Bu belgeler özellikle Amerikan ordusunun Afganistan (Afgan Savaş Günlüğü) ve Irak'taki (Irak Savaş Günlükleri) sivil kayıplar ve işkence eylemleri gibi aşırı eylemleriyle ilgilidir.


![WikiLeaks logo in November 2010](assets/en/059.webp)


WikiLeaks'in finansmanı temel olarak kamu bağışlarına dayanıyor, bu nedenle kuruluş çevrimiçi ödemeleri almak için ödeme işlemcilerine güveniyor. Ancak, bu ifşaatların ardından, düzenleyicinin tepkisinden korkan bu aracılar üzerinde baskı oluşuyor. Bu nedenle online ödeme şirketi Moneybookers 14 Ekim'de STK'nın hesabını [dondurdu] (https://www.theguardian.com/media/2010/oct/14/wikileaks-says-funding-is-blocked).


Bu durum, herhangi bir güvenilir üçüncü tarafa dayanmayan ve finansal sansüre çok daha iyi direnecek olan Bitcoin'yi kullanmak için kraliyet yolunu açıyor. Kasım ayında, genjix takma adını kullanan 22 yaşındaki bir İngiliz-İranlı olan Amir Taaki, forumda hipotezi açtı.


![Amir Taaki in December 2012 in Bratislava](assets/en/060.webp)

Amir Taaki Aralık 2012'de Bratislava'da (kaynak: [Mitch Altman](https://www.flickr.com/photos/maltman23/8272321106/))


Hacker, anarşist ve [poker oyuncusu] (https://bitcointalk.org/index.php?topic=1487.0), kısa süre önce Satoshi Nakamoto'nun modelini öğrendi. WikiLeaks'in durumunu Bitcoin'ün faydasını göstermek için bir fırsat olarak görüyor. 10 Kasım'da forumda aşağıdaki mesajı [yazıyor](https://bitcointalk.org/index.php?topic=1735.msg21271#msg21271):


> "Wikileaks'e Bitcoin hakkında bir mektup göndermek istedim çünkü ne yazık ki geçmişte fonlarına el konulduğu birkaç olay yaşadılar. [...] Onlara nereden mesaj gönderebileceğimi bilen var mı?"

Bu öneriye verilen tepkiler karışıktır. [Bir kullanıcıya (ShadowOfHarbringer) göre](https://bitcointalk.org/index.php?topic=1735.msg21283#msg21283), "bu wikileaks için iyi olabilir, ancak Bitcoin için iyi olmayabilir." [Bir diğeri (creighto) ise](https://bitcointalk.org/index.php?topic=1735.msg21415#msg21415) "ne kadar geç olursa o kadar iyi. Hükümetler harekete geçmek için ne kadar uzun süre beklerse, Bitcoin ağı o kadar güçlenir ve ona zarar vermek o kadar zorlaşır."


Birkaç hafta sonra, 3 Aralık'ta PayPal WikiLeaks'in hesabını dondurmaya karar verir ve bir gecede bir [açıklama](https://web.archive.org/web/20101206112350/https://www.thepaypalblog.com/2010/12/paypal-statement-regarding-wikileaks/) yayınlar. Ertesi sabah, geliştirici Wladimir van der Laan bu haberi forumda [aktarır](https://bitcointalk.org/index.php?topic=1735.msg26737#msg26737):


> "Paypal az önce onları engelledi ve diğer ABD bankalarının da aynısını yapmasını sağlamaya çalışıyorlar. Bu Bitcoin bağışlarını açmak için harika bir an olurdu."
Durumun bu şekilde evrilmesi tartışmaları yoğunlaştırmaktadır. Özellikle bir kişi WikiLeaks'in Bitcoin'i kabul etmesinden yana: Utah'ta yaşayan, [blog yazarı] (https://www.blogger.com/profile/12496217305843430098) ve Wikipedia'ya katkıda bulunan ve Temmuz ayındaki slashdot'lamanın ardından Bitcoin'i keşfeden bir bilgisayar mühendisi olan Robert S. Horning. O gün, WikiLeaks'i desteklemenin ahlaki açıdan doğru olduğunu ve devletin er ya da geç Bitcoin'den haberdar olacağını açıklayan uzun bir metin yazdı. Yazısını şöyle bitiriyor:

> "Temel olarak, devam edelim. Wikileaks'i Bitcoin kullanmaya teşvik edelim ve ben de bu eylemden kaynaklanabilecek her türlü risk ya da serpintiyle yüzleşmeye hazırım."

### Satoshi'un Ani Ayrılışı


Satoshi Robert Horning'in görüşünü paylaşmıyor ve Bitcoin'nin WikiLeaks'e tanıtılmasına karşı çıkıyor. Sözleri ve eylemlerinin de gösterdiği gibi, devlet yetkilileri konusunda bazen [paranoyaya](https://mmalmi.github.io/Satoshi/#email-158) varan büyük bir ihtiyat göstermektedir. Sonuç olarak, 5 Aralık'ta ana destekçiye sert bir şekilde [yanıt vererek](https://bitcointalk.org/index.php?topic=1735.msg26999#msg26999) bu coşkuya tepki gösterir:


> "Hayır, 'getirme'.
>

> Yazılımın yol boyunca güçlendirilebilmesi için projenin kademeli olarak büyümesi gerekir.
>

> WikiLeaks'e Bitcoin'yi kullanmaya çalışmaması için bu çağrıyı yapıyorum. Bitcoin henüz emekleme aşamasında olan küçük bir beta topluluğudur. Cep harçlığından fazlasını alamazsınız ve getireceğiniz ısı bu aşamada muhtemelen bizi yok edecektir."

Takip eden günlerde, WikiLeaks'e karşı Mastercard ve Visa'nın yanı sıra Western Union, Bank of America ve diğer aktörlerin de dahil olduğu gerçek bir finansal abluka düzenlenir ve bu da STK'nın finansal hayatta kalmasını [tehlikeye atar] (https://wikileaks.org/Banking-Blockade.html). Bu saldırı Bitcoin'ün kabul edilmesini daha da önemli hale getirir ve fikir doğal olarak yayılır.


11 Aralık'ta, Bitcoin'ün Wikileaks tarafından kullanılma olasılığını vurgulayan bir makale, Amerika'nın en büyük bilgisayar web sitelerinden biri olan PC World'de [yayınlandı](https://www.pcworld.com/article/499375/could_wikileaks_scandal_lead_to_new_virtual_currency.html). Gazeteci [Keir Thomas](https://www.keirthomas.com/how-i-caused-the-Bitcoin-guy-to-go-into-hiding/) tarafından kaleme alınan bu metin "Wikileaks Skandalı Yeni Sanal Para Birimine Yol Açabilir mi?" başlığını taşıyor. Pandora'nın kutusu açılır: PC World makalesi, muhtemelen WikiLeaks yetkilileri de dahil olmak üzere birçok kişi tarafından okunacak ve STK'yı bu ödeme yöntemini düşünmeye itecektir. Makaleden forumda hızla bahsedilir ve Bitcoin'ün yaratıcısının tepkisi nettir. O [yazıyor] (https://bitcointalk.org/index.php?topic=2216.msg29280#msg29280):


> "Bu ilgiyi başka bir bağlamda görmek güzel olurdu. WikiLeaks arı kovanına çomak soktu ve sürü bize doğru geliyor."

Ertesi gün, Satoshi [yayınlar] (https://bitcointalk.org/index.php?topic=2228.msg29479#msg29479) forumdaki son herkese açık mesajını yayınlar ve hizmet reddi saldırılarının yönetimini önemli ölçüde geliştiren yazılımın yeni bir sürümünün (v0.3.19) yayınlandığını duyurur. Ardından, ilgi odağı olmaktan çekilir ve yalnızca en yakın işbirlikçileriyle özel olarak iletişim kurar.


Takip eden günlerde PC World'de yayınlanan makale etkisini gösterdi. 14 Aralık'ta Satoshi'nin icadından Electronic Frontier Foundation tarafından WikiLeaks'in sansürlenmesine ilişkin bir [metinde](https://www.eff.org/deeplinks/2010/12/constructive-direct-action-against-censorship) bahsedildi (daha sonra kuruluş Bitcoin'yı "sansüre dayanıklı bir dijital para birimi" olarak [tanımlayacak](https://www.eff.org/deeplinks/2011/01/Bitcoin-step-toward-censorship-resistant)). Ayın 23'ünde kripto para, Rus kanalı RT'de Max Keiser ve Stacy Herbert tarafından sunulan bir finans programı olan Keiser Report'ta yine WikiLeaks bağlamında [bahsedildi](https://web.archive.org/web/20180226161051/http://www.youtube.com/watch?v=VMngK0t5WkY). Medyada yer alan bu haber Bitcoin'ya gösterilen ilgiyi önemli ölçüde artırarak Satoshi'nin korkularını doğruladı.


### Erişimin Devri ve Son E-postalar

Aralık ayının başından itibaren Satoshi halefini organize etmeye başladı. Ayrılmayı ya da en azından geri adım atmayı planladığından, çeşitli sorumlulukları güvendiği kişilere, özellikle de Martti Malmi ve Gavin Andresen'e devretmesi gerekiyordu. Ancak bu niyetini onlara hiçbir zaman açıkça belirtmedi.


İlk olarak, e-posta adreslerini sitenin [iletişim sayfasına] (https://web.archive.org/web/20101215111454/http://www.Bitcoin.org/contact) eklemek istedi. 7 Aralık'ta Martti'ye "kendisini iletişim sayfasındaki proje geliştiricileri listesine ekleyip ekleyemeyeceğini" soran bir e-posta [gönderdi](https://mmalmi.github.io/Satoshi/#email-245) ve genç Finli bu isteği kabul etti. Bitcoin'un yaratıcısı aynı talebi Gavin'e de yaptı ve o da kabul etti. Satoshi onların adreslerini sayfaya ekledi ve kendisininkini kaldırdı. Gavin [birkaç yıl sonra] (https://www.huffingtonpost.co.uk/entry/gavin-andresen-bitcoin_n_3093316) diyecekti:


> "Satoshi benim Address e-postamı Bitcoin ana sayfasına koyup koyamayacağını sorarak bana bir oyun oynadı ve ben de evet dedim, benim Address e-postamı oraya koyduğunda kendisininkini kaldıracağını fark etmemiştim."

Ama hepsi bu değildi. Satoshi ayrıca yazılım üzerindeki kontrolünü Gavin Andresen'e devretmek istedi. [Ekim ayında](https://sourceforge.net/p/Bitcoin/code/165/) SourceForge'daki depoya zaten yazma erişimi verilmiş olan Gavin, deponun ana koruyucusu oldu. 19 Aralık'ta GitHub'daki depoyu [oluşturdu](https://api.github.com/repos/Bitcoin/Bitcoin), muhtemelen Git ile daha rahat hissediyordu. Aynı gün, forumda geliştirmeye daha fazla dahil olacağını açıklayan uzun bir mesaj yazdı. O [duyurdu](https://bitcointalk.org/index.php?topic=2367.msg31651#msg31651):


> "Satoshi'nin onayıyla ve büyük bir isteksizlikle, Bitcoin için daha aktif proje yönetimi yapmaya başlayacağım."

Satoshi web sitesi, forum ve wiki'nin kontrolünü zaten Elements ile birlikte yönetmekte olan Martti'ye devretti. Ardından, 2011 baharında kesin olarak ortadan kayboldu.

Satoshi ile iletişim kuran son kişiler arasında, iki yıl önce kendisine ulaşan Google mühendisi Mike Hearn de vardı. Hearn, Aralık 2010'da Bitcoin'in yaratıcısıyla daha fazla teknik soru sormak için yeniden temas kurdu. Hearn, "Android telefonlarda çalışan bir istemci oluşturmak amacıyla basitleştirilmiş ödeme doğrulamasının Java uygulaması" üzerinde [çalışıyordu](https://plan99.net/~mike/Satoshi-emails/thread3.html) (*orijinal: "Android telefonlarda çalışan bir istemci oluşturmak amacıyla basitleştirilmiş ödeme doğrulamasının Java uygulaması üzerinde çalışıyorum. "*) İki adam 23 Nisan'a kadar mesajlaştı. Satoshi, Mike Hearn'e gönderdiği [son e-postasında] (https://plan99.net/~mike/Satoshi-emails/thread5.html) "başka şeylere geçtiğini" ve Bitcoin'in "Gavin ve diğerleriyle emin ellerde" olduğunu beyan etmiştir (*orijinal: "Başka şeylere geçtim. Gavin ve diğerleriyle emin ellerde. "*).


26 Nisan 2011 tarihinde Satoshi, Gavin'e e-posta yoluyla bir [son mesaj] (http://gavinandresen.ninja/eleven-years-ago-today) göndermiş ve bu mesajda şunları yazmıştır


> "Keşke benden gizemli, karanlık bir figür olarak bahsetmeye devam etmeseniz, basın bunu sadece korsan para birimi açısına dönüştürüyor. Belki de bunun yerine açık kaynak projesi hakkında konuşun ve geliştiricilerinize daha fazla kredi verin; bu onları motive etmeye yardımcı olur."

Burada Satoshi, Andy Greenberg tarafından birkaç gün önce Forbes'in web sitesinde yayınlanan ve kendisinin "gizemli, mahremiyet takıntılı bir figür" (*orijinal: "gizemli, mahremiyet takıntılı bir figür "*) olarak sunulduğu ve Bitcoin'ün yasadışı uyuşturucu temin etmenin bir yolu olarak vurgulandığı bir [makaleye](https://www.forbes.com/forbes/2011/0509/technology-psilocybin-bitcoins-gavin-andresen-crypto-currency.html) atıfta bulunuyordu (aslında bu, İpek Yolu platformunun başarı kazanmaya başladığı dönemdi). Satoshi, Gavin'e gönderdiği e-postaya, ağı teknik sorunlar konusunda uyarmak için kullanılabilecek bir uyarı anahtarı da eklemiştir.


Son olarak Mayıs ayı başında Martti ile de vedalaştı. İlk sağ koluna son sözleri şunlar oldu:


> "Başka şeylere yöneldim ve muhtemelen gelecekte buralarda olmayacağım."
> Dijital Altın s. 81

### CIA, WikiLeaks ve EFF

26 Nisan 2011 tarihinde Gavin Andresen, Satoshi Nakamoto'ya bir [son e-posta](http://gavinandresen.ninja/eleven-years-ago-today) göndermiş ve Nakamoto bu e-postaya yanıt vermemiştir. Bu e-postada, CIA tarafından yönetilen bir Amerikan girişim sermayesi fonu olan In-Q-Tel tarafından Bitcoin'yı sunmak üzere davet edildiğini [belirtmiştir](http://gavinandresen.ninja/eleven-years-ago-today). Bu ziyaretin generate'e ne tür bir tepki vereceğinin çok farkındaydı ama yine de gitmeye karar verdi. Kararını Satoshi'ye yazarak gerekçelendirdi:


> "Umarım doğrudan 'onlarla' konuşarak ve daha da önemlisi sorularını/endişelerini dinleyerek, Bitcoin'i benim düşündüğüm gibi düşünürler - sadece daha iyi, daha verimli, daha az siyasete tabi bir para olarak. Anarşistler tarafından Sistemi yıkmak için kullanılacak güçlü bir karaborsa aracı olarak değil."

Ertesi gün Gavin [haberi](https://bitcointalk.org/index.php?topic=6652.msg97181#msg97181) forumda tüm şeffaflığıyla duyurdu. Bu gezi için kendisine 3,000 dolar ödendiğini belirtti. Ancak bu durum, güvensizlik haklı olsa da onun yaklaşımını anlayan topluluğu harekete geçirmedi. Gavin'in CIA merkezine yaptığı ziyaret 14 Haziran'da [gerçekleşti](https://twitter.com/gavinandresen/status/80785477342478336).


Sembolik olarak 14 Haziran aynı zamanda WikiLeaks'in Bitcoin bağışlarını kabul etmeye [başladığı](https://twitter.com/wikileaks/status/80774521350668288) tarihtir. Bu haber Forbes web sitesinde yer almıştır.


Paradoksal olarak, bu haber bir kuruluşun mevcut kabulünü kısmen geri itti: Electronic Frontier Foundation. 20 Haziran'da EFF, bu kabulün gerektirdiği yasal karmaşıklıklar nedeniyle Bitcoin bağışlarından gerçekten vazgeçtiğini [duyurdu](https://www.eff.org/deeplinks/2011/06/eff-and-Bitcoin). Alınan bitcoinleri Gavin Andresen'in Bitcoin Faucet'ine [iade etti](https://bitcointalk.org/index.php?topic=20185.msg456413#msg456413). Böylece Bitcoin, bir kuruluşun zararına diğerini kazanmış oldu.


### Satoshi Gizemi

Böylece, Satoshi'ün ortadan kaybolması, topluluğun slashdotting'den sonra büyümesinin ardından ve en önemlisi WikiLeaks olayı nedeniyle aniden gerçekleşti. Bitcoin'ün yaratıcısı projenin dizginlerini, geliştirme ve iletişim çabalarında kendisine destek olan Martti Malmi ve Gavin Andresen'e devretti.


Daha sonra ne olduğu bilinmemektedir. Çeşitli hesaplarından ([P2P Foundation](https://p2pfoundation.ning.com/forum/topics/Bitcoin-open-source?commentId=2003008:Comment:52186), [Vistomail](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-August/010238.html)) birkaç mesaj ortaya çıkmıştır, ancak bu hesaplar muhtemelen hacklenmiştir. Bu nedenle, Tor ve gizliliğe saygı duyan hizmetler aracılığıyla anonimliğini korumayı başaran Satoshi Nakamoto'nun kimliği bilinmemektedir.


Yıllar boyunca, onunla ilgili ipuçları verilmiş ve Nick Szabo, Hal Finney, Adam Back veya Len Sassaman gibi tanınmış şahsiyetlerin isimleri zikredilmiştir. Hatta 2014 yılında, Los Angeles'ın banliyölerinden Temple City'de annesiyle birlikte yaşayan Japon asıllı Amerikan vatandaşı bir telekomünikasyon mühendisi olan Dorian Prentice Satoshi Nakamoto'nun şahsında bulunduğuna inanılıyordu. Bununla birlikte, Satoshi bir [gizem] olarak kalmaya devam etmektedir (https://www.youtube.com/watch?v=0ETcLj5jBy4).


Bitcoin'un yaratıcısını çevreleyen bu gizemli yön, Haziran 2013'te, 2014'te ölmeden önce forumdaki [son mesajlarından birinde] (https://bitcointalk.org/index.php?topic=234330.msg2479328#msg2479328) yeni çıkan *Man of Steel* filminden bir alıntı paylaşan Hal Finney tarafından iyi bir şekilde özetlenmiştir:


> "Hayatı boyunca izini kaybettirmiş birini nasıl bulursunuz?
>

> Bazıları için o koruyucu bir melekti. Diğerleri içinse bir muamma, bir hayalet, her zaman biraz ayrı.
>

> S ne anlama geliyor?"


## Topluluk Devralıyor

<chapterId>16c5e6d6-2412-48c6-9687-6af92cf0d89a</chapterId>


Satoshi Nakamoto'nun ayrılmasından sonra, onsuz devam etmek gerekli hale geldi. Neyse ki Bitcoin herkesin katkıda bulunabileceği açık bir projeydi, bu nedenle kurucusunun ortadan kaybolması ölümcül değildi. Geliştirici Jeff Garzik'in Temmuz 2010'da yazdığı gibi (kurucunun yokluğu olasılığı ile ilgili olarak):


> "İnsanlar kurallar ve kural koyma konusunda çok endişeleniyor. Ancak burada herhangi bir Devletin Sürekliliği planına ihtiyaç yok. Kaynak kodu açık kaldığı sürece bu yeterlidir. Eğer bir ihtiyaç ve yeterli ilgi varsa, topluluk bunu sağlayacaktır. Topluluğa güvenin."

Ancak bu ortadan kayboluşun zorlukları da yok değildi. Satoshi'ün yokluğu, artık yönlendirme yapılabilecek bir otoritenin olmadığı anlamına geliyordu. Yazılım geliştirme ve dış iletişim açısından koordinasyon gerekliydi. Yeni oluşan Bitcoin topluluğunun üyeleri bu nedenle bu uygulamaları standartlaştırmak için çok çaba sarf etmek zorunda kaldı.


### Toplumsal Gelişim


Anlattığımız gibi, Gavin Andresen Aralık 2010'da GitHub deposunu oluşturarak projenin dizginlerini eline aldı. 13 Ocak 2011'de forumda "Core Bitcoin Development Help Wanted" başlıklı bir başlık açarak yardım istedi. Takip eden aylarda pek çok programcı bu çağrıya uydu ve sorunları çözmeye başladı. Bunlar arasında Jeff Garzik, Pieter Wuille (sipa) ve Wladimir van Der Laan (wumpus, laanwj) vardı. Luke-Jr veya Matt Corallo (BlueMatt) gibi yeni geliştiriciler de dahil oldu. Beyaz kitapta açıklandığı gibi basitleştirilmiş ödeme doğrulamasını (SPV) uygulamak için Mart 2011'de BitCoinJ adlı yeni bir yazılım uygulamasını kamuoyuna duyuran Mike Hearn (Aralık ayından beri topluluğa dahil) gibi diğer kişiler de ana yazılıma doğrudan katkıda bulunmadan yardımcı oldular.


Genel plan, projenin sürdürülebilir gelişimini sağlamaktır. Bu da daha geniş bir kitle nezdinde belli bir meşruiyetin tesis edilmesini içeriyor. 19 Mayıs'ta Mike Hearn [https://web.archive.org/web/20110522075653/http://forum.Bitcoin.org:80/index.php?topic=8954.0] projeye dahil olanların "gerçek isimlerini", yani sivil isimlerini kullanmalarını, böylece insanların şüphelenmemesini önerir. Gavin, Mike ve diğerleri forumdaki takma adlarını değiştirerek tam adlarını gösterirler. Ana geliştiricilerin bir listesi de web sitesinin ön sayfasında [yayınlanmaktadır] (https://web.archive.org/web/20110530221415/http://www.Bitcoin.org:80/). Mayıs ayı sonu itibariyle, bu şekilde sunulan geliştiriciler Gavin Andresen, Martti Malmi, Amir Taaki, Pieter Wuille, Nils Schneider ve Jeff Garzik'tir.


Koordinasyon da gelişir. Forum ve #Bitcoin-dev IRC kanalının yanı sıra, "Bitcoin-development" adlı geliştirmeye adanmış bir posta listesi ortaya çıkar. Jeff Garzik tarafından 12 Haziran'da [kurulur] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2011-June/000000.html). Bitcoin'da yapılacak değişikliklerin resmi olarak tartışılmasını sağlar. Projenin [yol haritası](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2011-August/000333.html) ile ilgili tartışmalar Ağustos ayında başlatılır. Liste başlangıçta SourceForge'da barındırılmaktadır; Haziran 2015'te Linux Foundation sitesine [taşınacak](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-June/008975.html) ve son olarak 2024'ün başında Google Groups'a [taşınacak](https://groups.google.com/g/bitcoindev/c/aewBuV6k-LI).


19 Eylül 2011 tarihinde Amir Taaki, Python programlama diline özgü Python Geliştirme Önerileri (PEP) model alınarak oluşturulan Bitcoin Geliştirme Önerileri sisteminin [açılışını] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2011-September/000554.html) yapmıştır. Bu BIP'ler, protokoldeki olası değişiklikleri açıklayan veya topluluğa genel bilgi sağlayan belgelerdir. Luke-Jr'ın BIP-2'sinin daha sonra yerini alacağı BIP-1 aracılığıyla süreci açıklıyor. Bu teklifler başlangıçta [Bitcoin wiki] (https://en.Bitcoin.it/w/index.php?title=Bitcoin_Improvement_Proposals&oldid=20743) adresinde barındırılmaktadır.


Gavin Andresen'in gözetimi altında, aylar boyunca yazılımın çeşitli sürümleri yayınlandı: 5 Mart'ta [v0.3.20](https://bitcointalk.org/index.php?topic=4167.msg60365#msg60365), 27 Nisan'da [v0.3.21](https://bitcointalk.org/index.php?topic=6642.msg97074#msg97074), 5 Haziran'da [v0.3.22](https://bitcointalk.org/index.php?topic=12269.msg170790#msg170790), 13 Haziran'da [v0.3.23](https://bitcointalk.org/index.php?topic=16553.msg215364#msg215364) ve 8 Temmuz'da [v0.3.24](https://bitcointalk.org/index.php?topic=27187.msg342270#msg342270). 23 Eylül 2011'de yeni bir ana sürüm olan 0.4 sürümü resmi olarak [yayınlandı](https://bitcointalk.org/index.php?topic=45410.msg541446#msg541446) ve sembolik olarak geliştirme sürecinin devam ettiğini gösterdi.


### Web Sitesi, Forum ve Wiki


Satoshi'in yokluğunda yönetilmesi gereken tek şey yazılım geliştirme değildir. Web sitesi, forum ve wiki gibi genel iletişim araçları da vardır. Bunlar gerçekten de projenin "vitrinleridir" ve nasıl yönetildikleri çok önemlidir.


Daha önce de belirttiğimiz gibi, Satoshi ayrıldıktan sonra sitenin kontrolünü Martti Malmi'ye devretti, bu da forumu (Bitcoin.org/smf) ve [wiki](https://web.archive.org/web/20110102000201/http://www.Bitcoin.org/wiki/doku.php) (Bitcoin.org/wiki) içeriyordu. Ancak Martti'nin bu göreve ayıracak çok az zamanı vardı. 2010 baharından itibaren bir stajyerlik ve ardından tam zamanlı bir işle [meşgul](https://mmalmi.github.io/Satoshi/#email-191) oldu ve yavaş yavaş geri adım attı.


Zaman yetersizliği nedeniyle Martti, Exchange platformu BitcoinExchange'i kademeli olarak kapatmak zorunda kaldı. Aralık 2010'da bir [sunucu değişikliği](https://mmalmi.github.io/Satoshi/#email-240) sırasında çevrimdışıydı. Ocak ayında, [yeniden açmamaya](https://bitcointalk.org/index.php?topic=2179.msg37575#msg37575) karar verdi. Ağustos başında, alan adını o tarihte 2.365 $'a denk gelen 250 bitcoin karşılığında [sattı](https://bitcointalk.org/index.php?topic=34357.msg427698#msg427698). Bağlantı daha sonra Mt. Gox'a yönlendirilecekti.


Ancak Martti'nin öncelikle web sitesi yönetimini devretmesi gerekiyor. 2010 sonu ve 2011 başında Bitcoin.org [bazı](https://bitcointalk.org/index.php?topic=2026.msg25845#msg25845) [sorunlarla](https://bitcointalk.org/index.php?topic=3328.msg46775#msg46775) karşılaştı. Martti 28 Mart'ta forumda teknik yardım isteyen [bir duyuru yayınladı](https://bitcointalk.org/index.php?topic=5052.msg73922#msg73922) ve birkaç yanıt aldı. Daha sonra barındırma [daha sağlam](https://bitcointalk.org/index.php?topic=13375.msg184002#msg184002) hale getirildi ve sitenin her büyük ziyaretçi akınında çevrimdışı kalması önlendi.


Görünüşü de değişti. Aralık 2010'da web sitesi hala Satoshi dönemindeki gibi görünüyordu. İşte 5 Aralık'tan bir [anlık görüntü] (https://web.archive.org/web/20101110005546/http://www.Bitcoin.org/):


![Snapshot of Bitcoin.org from December 5, 2010](assets/en/061.webp)


Böylece, 2011'in başlarında bir renk dokunuşu [eklendi] (https://web.archive.org/web/20110216125441/http://www.Bitcoin.org/):


![Snapshot of Bitcoin.org from February 16, 2011](assets/en/062.webp)


Nisan ayında, topluluk tarafından [organize edilen](https://bitcointalk.org/index.php?topic=4223.msg80581#msg80581) bir yeniden tasarım nedeniyle web sitesinin düzeni değişti. İşte o zaman [nasıl göründüğü](https://web.archive.org/web/20110411071904/http://www.Bitcoin.org/):


![Snapshot of Bitcoin.org from April 11, 2011](assets/en/063.webp)


Son olarak, Eylül 2011'de Nils Schneider tarafından yeni bir değişiklik [yapıldı](https://buildingbitcoin.org/Bitcoin-dev/log-2011-08-31.html#l-691). Bu olay için yeni bir GitHub deposu [oluşturuldu](https://github.com/Bitcoin/Bitcoin.org). Bu tasarım daha uzun sürecekti: 2013 yılına kadar değiştirilmeyecekti. İşte burada (Bitcoin-the-software'in daha sonra "topluluk odaklı bir açık kaynak projesi" olarak tanımlandığına dikkat edin):


![Snapshot of Bitcoin.org from September 23, 2011](assets/en/064.webp)


Wiki ile ilgili olarak, başlangıçta web sitesine entegre edilmiş ücretsiz bir motor olan DokuWiki'ye dayanıyordu. Ancak Aralık 2010'da, Japonya'da yaşayan ve forumda MagicalTux takma adını kullanan Fransız bir geliştirici olan Mark Karpelès, Bitcoin.it adresinde yeni bir wiki oluşturdu. Bu wiki, daha zarif ve kullanımı daha kolay bulduğu MediaWiki motoruna dayanmaktadır. Başlangıçtaki fikir mevcut belgelerin yerini almak değil, Mark'ın IRC'de [ifade ettiği] (https://buildingbitcoin.org/Bitcoin-dev/log-2010-12-16.html#l-2848) gibi, "daha az resmi, daha topluluk odaklı bir wiki" geliştirmektir


Bu yeni viki [Martti Malmi](https://bitcointalk.org/index.php?topic=2321.msg30873#msg30873) ve [Gavin Andresen](https://bitcointalk.org/index.php?topic=2321.msg31535#msg31535)'in ilgisini çeker, bu yüzden hemen ana viki yapmayı düşünürler. İşte 21 Mayıs'ta çekilmiş bir [anlık görüntü](https://web.archive.org/web/20110521044430/https://en.Bitcoin.it/wiki/Main_Page):


![Snapshot of the Bitcoin.it wiki on May 21, 2011](assets/en/065.webp)


Açılıştan birkaç gün sonra, Bitcoin.org ana sayfasındaki "wiki" başlıklı bağlantı [points] (https://bitcointalk.org/index.php?topic=2321.msg30872#msg30872) Bitcoin.it adresine yönlendirildi. İçerik DokuWiki sürümünden kademeli olarak aktarılır. 31 Ocak'ta Martti forumda bunun yeni wiki olduğunu [belirtir](https://bitcointalk.org/index.php?topic=293.msg42789#msg42789).


Üçüncü unsur ise Bitcoin forumu. Martti forumu yönetir, ancak kısa sürede moderatörleri de işe alır. Bunlardan biri olan Theymos (gerçek adı Michael Marquardt), özellikle forumun ortak yönetimi olmak üzere ek sorumluluklar kazanır. Forum Simple Machines Forum motoru üzerinde çalışmaktadır ve yıllar içinde görünümünü değiştirmemiştir. Bununla birlikte, URL'si iki kez değişti. İlk olarak, 17 Mayıs'ta forum forum.Bitcoin.org adresine [taşındı] (https://bitcointalk.org/index.php?topic=8696.msg125963#msg125963). Ardından, 1 Ağustos'ta yeni bir üst düzey alan adına [taşındı](https://bitcointalk.org/index.php?topic=33393.msg417531#msg417531): bitcointalk.org. Yıllar boyunca BitcoinTalk olarak adlandırılacaktır.

Martti Malmi, 2011 yazındaki değer artışıyla birlikte, Helsinki yakınlarında kendisine konforlu bir daire satın almak için bitcoinlerinin önemli bir kısmını [sattı](https://twitter.com/marttimalmi/status/1339908793736556544). Ardından, Japonya'da birkaç ay geçirmek için işinden [ayrıldı](https://x.com/marttimalmi/status/1339908797968637952). Web sitesini ve [forumu terk ederek](https://bitcointalk.org/index.php?topic=5129680.msg50617107#msg50617107) [onları](https://bitcointalk.org/index.php?topic=1603627.msg16115993#msg16115993) Theymos ve Martti tarafından "Satoshi tarafından güvenilen biri" olarak [tanımlanan](https://forum.Bitcoin.com/ama-ask-me-anything/i-m-martti-malmi-early-Bitcoin-developer-and-the-original-founder-of-the-bitcointalk-org-forums-ama-t2770.html#p8222) Cøbra'nın ellerine bıraktı İki adam sonraki yıllarda her iki platformu da birlikte yönetecekti.


### Konferanslar ve Toplantılar


Kurucunun ayrılması ve işbirliği yapma ihtiyacı sadece teknik yönü değil, aynı zamanda üyeler arasında bağlantılar oluşturarak topluluğun güçlenmesine yardımcı olan sosyal yönü de etkiler. Bu yüzden "gerçek hayatta" buluşmalar ve konferanslar düzenleniyor Bu etkinlikler aynı zamanda Bitcoin'i çevrimiçi içeriğe daha dirençli insanlarla tanıştırma avantajına da sahip.


İlk Bitcoin kullanıcı buluşmaları, teknik konularda televizyonda tartışmalar içeren bir [YouTube kanalının] (https://www.youtube.com/@vlogwrap) New York merkezli sunucusu Bruce Wagner tarafından başlatıldı ve Nisan 2011'de *Bitcoin Show* adlı bir program oluşturdu. İlk toplantı 11 Aralık 2010 (UTC) tarihinde New York'ta [gerçekleşti](https://bitcointalk.org/index.php?topic=1891.msg29174#msg29174). Daha sonra Washington D.C.'de aynı türden bir buluşma [gerçekleşti](https://web.archive.org/web/20110413231434/http://Bitcoin.meetup.com/). 5 Şubat 2011'de İsviçre'nin Zürih kentinde Mike Hearn tarafından Christian Decker ve Stefan Thomas'ın (justmoon) da katıldığı bir buluşma [düzenlendi](https://bitcointalk.org/index.php?topic=2716.msg36886#msg36886).

Şubat ayı aynı zamanda Gavin Andresen tarafından 8'inde memleketi Amherst, Massachusetts'te düzenlenen bir etkinlik sırasında gerçekleştirilen Bitcoin'in [filme alınan ilk sunumu] (https://www.youtube.com/watch?v=koIq58UoNfE) anlamına geliyor. Projenin yeni baş sorumlusu tarafından yapılan "Para Kazanmak" başlıklı sunum, Elements'nin önümüzdeki yıllarda kripto para biriminin sunuluş biçimini karakterize edecek çok sayıda dilini içeriyor.


:::video id=92b9aa30-1479-4d4f-b57f-f07b660145f2:::


İlk etkinlikler Amerika Birleşik Devletleri'nde gerçekleşmiş olsa da Fransız toplumu da geride kalmadı. Gavin Andresen'in Paris ziyareti münasebetiyle 25 Mayıs'ta La Défense bölgesinde Lucien Grondin, David François ve Jon Matonis (kendisi de ziyaretteydi) gibi önemli isimlerin katıldığı bir öğle yemeği düzenlendi.


![Meeting at La Défense in Paris with Gavin Andresen, in a pink shirt](assets/en/066.webp)

Pembe gömlekli Gavin Andresen ile Paris'te La Défense'da buluşma (kaynak: [forum arşivi](https://web.archive.org/web/20140715000000*/https://bitcointalk.org/index.php?topic=5587.40))


Bir ay sonra, 15 Haziran'da, Bitcoin'un Fransızca ilk halka açık sunumu [gerçekleşti](https://bitcointalk.org/index.php?topic=11384.msg225831#msg225831), yine Paris'te. Sunum, Bitcoin'u bir yıl önce keşfetmiş olan genç siber güvenlik uzmanı Renaud Lifchitz (nono2357) tarafından gerçekleştirildi. Sunulan içerik](https://prezi.com/tikwkjt9ouey/Bitcoin-une-monnaie-electronique-pour-tous/) çok yüksek kalitedeydi ve izleyici katılımı o kadar iyiydi ki salon tıklım tıklım doluydu.


![Bitcoin presentation by Renaud Lifchitz on June 15, 2011](assets/en/067.webp)

Renaud Lifchitz tarafından 15 Haziran 2011 tarihinde yapılan Bitcoin sunumu (kaynak: [forum arşivi](https://web.archive.org/web/20140406141205/https://bitcointalk.org/index.php?topic=11384.0))


Bu deneyimin ardından Paris toplumu 11 Temmuz'da bir sosyal toplantı [düzenledi](https://bitcointalk.org/index.php?topic=21991.msg276443#msg276443). Bu etkinlik Pierre Noizat ve Émilien Dutang gibi kişileri bir araya getirdi.

Uluslararası cephede, Bitcoin üzerine ilk toplu konferans 19-21 Ağustos tarihleri arasında New York'ta gerçekleşti. Bruce Wagner tarafından organize edilen bu toplantı Roger Ver, Jesse Powell, Jed McCaleb, Mark Karpelès ve Charlie Lee gibi şahsiyetleri bir araya getirdi. Wagner üç günlük etkinlik sözü vermesine rağmen, sadece dört sunum gerçekleşti: kendisinin ve Gavin Andresen, Jeff Garzik ve Stefan Thomas'ın sunumları.


:::video id=bca0217c-29ee-49b2-8d16-d9efe6f390da:::


Yılın ilerleyen aylarında, Kasım ayında, Prag'da bir Avrupa konferansı [gerçekleşecek](https://bitcointalk.org/index.php?topic=40272.msg490901#msg490901). Önemli konuşmacılar arasında geliştirici Amir Taaki, İsveç Korsan Partisi kurucusu Rick Falkvinge ve sunucu Max Keiser yer alacak. Ertesi yıl benzer bir etkinlik Londra'da [düzenlenecek](https://blog.bitmex.com/london-2012-the-2nd-Bitcoin-conference/).


### Medya Kapsamı


2011 yılı aynı zamanda medya kapsamının önemli ölçüde genişlediği bir yıl oldu. WikiLeaks davası ve Aralık ayında PC World'de yayınlanan makale Bitcoin'e büyük ölçüde dikkat çekti, öyle ki her türlü medya konuyu ele aldı. O dönemde Gavin Andresen'in [yazdığı] (https://bitcointalk.org/index.php?topic=8940.msg129623#msg129623) gibi "Bitcoin'e yönelik basın ilgisi çığ gibi büyüdü".


İlk olarak YouTube'da konuyla ilgili videolar çoğalmaya başladı. 22 Mart'ta Bitcoin ile ilgili ilk yüksek kaliteli video ortaya çıktı. "Bitcoin nedir?" başlıklı bu video, Stefan Thomas (justmoon) tarafından topluluktan [crowdfunding] (https://bitcointalk.org/index.php?topic=697.msg70001#msg70001) sayesinde üretildi. Kripto paranın eğitimi ve yaygınlaştırılmasına adanmış WeUseCoins portalında yayınlandı. Bunu Nisan ayında [howtovanish](https://www.youtube.com/watch?v=LSLByqTusaQ), [Reason](https://www.youtube.com/watch?v=yYTqvYqXRbY) veya Haziran ayında [Rocketboom](https://www.youtube.com/watch?v=9LaSrxtWfgc) gibi bağımsız olarak üretilen diğer tanıtım videoları takip etti.


:::video id=6147a351-da80-4331-9d79-d3156889ac62:::


Nisan ayında dijital para konusu [The Atlantic](https://www.theatlantic.com/business/archive/2011/04/how-to-start-your-own-private-currency/73327/), [Time Magazine](https://techland.time.com/2011/04/16/online-cash-Bitcoin-could-challenge-governments/) ve [Forbes](https://www.forbes.com/forbes/2011/0509/technology-psilocybin-bitcoins-gavin-andresen-crypto-currency.html) gibi önemli ana akım basın organlarında yer aldı. Mayıs ayında hareket ivme kazandı ve Bitcoin'ten [Wired UK](https://web.archive.org/web/20110517122859/http://www.wired.co.uk/news/archive/2011-05/16/Bitcoin-P2P-currency), [Slate](https://slate.com/business/2011/05/Bitcoin-why-the-new-electronic-currency-is-a-favorite-of-libertarian-hipsters-and-criminals.html), [Gizmodo](https://gizmodo.com/what-is-Bitcoin-5803124) ve [TechCrunch](https://techcrunch.com/2011/05/20/Bitcoin-ven-and-the-end-of-currency/) başta olmak üzere neredeyse her yerde bahsedildi.


![Gavin Andresen in Forbes in April 2011](assets/en/068.webp)

Gavin Andresen Nisan 2011'de Forbes'da (kaynak: [Forbes arşivi](https://web.archive.org/web/20110502052302/https://www.forbes.com/forbes/2011/0509/technology-psilocybin-bitcoins-gavin-andresen-crypto-currency.html))


Kripto para birimini tartışmak için radyo da kullanıldı. Kanada CBC Radyo programının bir bölümü 27 Şubat tarihinde para birimi ve Bitcoin konusuna [adanmıştır] (https://web.archive.org/web/20110227214049/http://www.cbc.ca/spark/2011/02/spark-139-february-27-march-2-2011/). Bitcoin'den Amerika Birleşik Devletleri'nde liberteryen odaklı bir program olan FreeTalkLive'ın birkaç bölümünde de bahsedildi. Konu özellikle 16 Mart 2011 tarihinde İpek Yolu'nun yükselişi bağlamında daha kapsamlı bir şekilde [tartışıldı](https://web.archive.org/web/20110318163416/http://www.freetalklive.com/content/podcast_2011_03_16). Son olarak, 24 Mayıs'ta Bitcoin, Amerika Birleşik Devletleri'ndeki Ulusal Halk Radyosu'nda [kısa bir bölüm](https://www.npr.org/2011/05/24/136620231/what-are-bitcoins) konusu olmuştur.


Bireysel blog yazarları da ilgileniyor. İsveç Korsan Partisi'nin kurucusu Rick Falkvinge'nin yayınladığı [birkaç](https://falkvinge.net/2011/05/11/with-the-napster-of-banking-round-the-corner-bring-out-your-popcorn/) [makaleler] (https://falkvinge.net/2011/05/19/the-information-policy-case-for-flat-tax-and-basic-income/) Mayıs ayında Satoshi Nakamoto'nun yaratılması hakkında. Bitcoin'i (ve Ripple gibi ilgili sistemleri) "bankacılığın Napster'ı" olarak tanımlamaktadır Onun argümanları ABD'deki mutualist [Kevin Carson](https://c4ss.org/content/7149) ya da Fransa'daki liberal blog yazarı [h16](https://h16free.com/2011/05/30/8585-revolution-numerique-aujourdhui-musique-et-cinema-et-demain) gibi pek çok kişi tarafından yankı buldu. Ayın 29'unda Rick Falkvinge [duyurdu](https://falkvinge.net/2011/05/29/why-im-putting-all-my-savings-into-Bitcoin/) "tüm birikimlerini Bitcoin'e yatırıyor"!


### İlk Baloncuk


Bitcoin'un yaygınlaşması fiyatının önemli ölçüde artması anlamına gelmektedir. Aralık 2010'da 20 sente kadar düşmüşken, 9 Şubat 2011'de dolar ile eşit seviyeye ulaştı. O dönemde Hal Finney [https://bitcointalk.org/index.php?topic=2734.msg37307#msg37307] topluluk üyelerinin "muhtemelen patlayıcı yeni bir fenomenin başlangıcında oldukları için gerçekten şanslı olduklarını" belirtmiştir İyi bir içgüdüye sahipti, çünkü bundan sonra olacaklar yıldırım hızıyla gerçekleşecekti.


![Photograph posted by jimbobway on the forum the day of parity with the dollar](assets/en/069.webp)

Jimbobway tarafından dolar ile parite günü forumda yayınlanan fotoğraf (kaynak: [Bitcointalk](https://bitcointalk.org/index.php?topic=2734.msg37144#msg37144))


Gerçekten de, baharın medya çılgınlığı yavaş yavaş benzeri görülmemiş bir spekülatif fenomen yaratır. Birkaç ay boyunca 1 $ civarında durgunlaştıktan sonra, fiyat yükseldi ve Nisan sonunda 3 $'a ulaştı. Son olarak, 8 Haziran'da Bitcoin'in fiyatı Mt. Gox'ta 32 $ gibi tarihi bir yüksekliğe ulaştı! Bu artış altı ay içinde 160 katlık bir artışa tekabül ediyor.


![Average price of BTC between January 1 and June 30, 2011](assets/en/070.webp)

BTC'nin 1 Ocak - 30 Haziran 2011 tarihleri arasındaki ortalama fiyatı (kaynak: [Bitbo.io](https://calendar.bitbo.io/price/))


Doğal olarak, bu spekülatif hareket bir finansal balonu, bir finansal ürünün temel değerine kıyasla aşırı değerlenmesini anımsatmaktadır. Bitcoin gibi bir para birimi söz konusu olduğunda, fiyatta baş döndürücü bir artışla sonuçlanan geçici bir coşku ve ardından yeni katılımcıların inanç eksikliğinden kaynaklanan keskin bir düşüş söz konusudur. Bitcoin'nin ilk "ölüm ilanlarından" birinde, 27 Mayıs'ta bir Reuters köşe yazarı tarafından fiyat evrimi bu şekilde bir "balon" olarak [tanımlanmıştır] (https://web.archive.org/web/20110530074512/http://blogs.reuters.com/columns/2011/05/27/virtual-bitcoins-are-appealing-but-probably-doomed/).


Ancak bu spekülatif hareket, ana akım basını konuyu ele almaya itiyor ve bu da her zaman tarafsız bir şekilde yapılmıyor. Böylece [New York Times](https://www.nytimes.com/2011/05/30/business/economy/30views.html), [The Economist](https://www.economist.com/babbage/2011/06/13/bits-and-Bob), İngiliz gazetesi [The Guardian](https://www.theguardian.com/technology/2011/jun/12/Bitcoin-online-currency-us-government), Alman haber sitesi [Der Spiegel Online](https://www.spiegel.de/netzwelt/netzpolitik/hacker-waehrung-Bitcoin-geld-aus-der-steckdose-a-765382.html), İtalyan gazetesi [La Repubblica](https://www.repubblica.it/tecnologia/2011/05/31/news/bitcoin_moneta_elettronica_hacker_cia-17030027/) veya Fransız gazetesi [Le Monde](https://www.lemonde.fr/technologies/article/2011/06/17/Bitcoin-les-deux-faces-de-la-monnaie-virtuelle_1537285_651865.html)'da makaleler yayınlanmaktadır. Bu da Bitcoin'ün medya kapsamını sağlamlaştırmaktadır. Artık gündemdedir ve azıcık meraklı olan herkes bunu duymuştur. Bitcoin'ün, Satoshi'ün varlığı ve projenin gizliliği ile karakterize edilen ilk dönemi artık sona ermiştir.


### Bitcoin'nın Oluşturulmasına İlişkin Genel Sonuç


Böylece 2011'in ilk yarısında proje, kurucusu Satoshi Nakamoto'nun varlığı olmadan büyüyebildi. Bu an, Bitcoin'nin tamamen topluluk güdümlü bir proje olarak başlangıcını işaret etti ve Bitcoin'nin 2007'den 2011'e kadar dört yıla yayılan yaratılış dönemini kapattı. Bu olaydan birkaç şey çıkarabiliriz.


Öncelikle, Bitcoin birdenbire ortaya çıkmamıştır. Siber uzayda faaliyet gösteren dijital nakit olarak, yaratılmasına yol açan onlarca yıllık araştırma ve deneylerin sonucudur. Özellikle David Chaum'un eCash modeli, e-altın gibi özel dijital para birimleri ve cypherpunk'ların kavramları tarafından öncelenmiştir. Bitcoin'un ortaya çıkışı ve Satoshi'ın ortadan kayboluşu sırasında Hal Finney'in varlığı bu nedenle çok sembolikti. Elektronik paranın 90'lı yıllardaki ilk denemelerine tanıklık etmiş ve 2004 yılında RPOW ile kendi modelini yaratmaya çalışmış bir kişi olarak, tam da Bitcoin'a yol açan arayışın sürekliliğini temsil ediyordu.


İkinci olarak, Bitcoin bir günde inşa edilmedi. Yazılımın 0.1 sürümünün Ocak 2009'da yayınlanmasından sonra bile proje hazır olmaktan uzaktı. Çok sayıda güvenlik açığının düzeltilmesi gerekiyordu. Bunlardan biri Ağustos 2010'da ağın yaklaşık on beş saat boyunca felç olduğu büyük bir olaya neden oldu, ancak en kötüsü önlendi. Satoshi'nin ayrılmasından sonra bile topluluk yazılımı geliştirmeye devam etmek zorunda kaldı.


Üçüncü olarak, Bitcoin organik olarak büyüdü. Gizlice gelişti ve yavaş yavaş insanları kendine çekti. Yaklaşık bir buçuk yıl boyunca sadece meraklıların ve meraklıların bildiği gizli bir projeydi. Ancak Temmuz 2010'daki slashdot olayından sonra patlamaya başladı. Spekülatif çılgınlık, fiyatın katlanarak 32 dolara yükseldiği 2011 yılına kadar başlamadı.


Dördüncü olarak, Bitcoin özgeci bir yaratımdı. Satoshi Nakamoto Bitcoin'ü dünyaya sundu. Programı ücretsiz bir lisans altında yayınladı. Ne şöhret, ne kar ne de güç peşindeydi. Ağın Mining güvenliğini bir yıldan fazla bir süre boyunca hiçbir karşılık beklemeden sağladı. Bir milyondan fazla bitcoin biriktirmesine rağmen bunları hiç harcamadı. Sonunda, esas olarak WikiLeaks davasının yarattığı ilgiyle ilgili korkular nedeniyle ortadan kayboldu ve projeyi tek bir baskın figür olmadan bir topluluğa bıraktı.


2011 yılında Satoshi ortadan kayboldu, ancak Bitcoin hayatta kaldı. Kripto para birimi, hem medya hem de ekonomik açıdan kesin olarak yükselişe geçti. Makine çalıştırıldı ve kimse onu durduramadı.


# Son Bölüm

<partId>89532d9b-af1f-49f3-b87a-b11987e303d5</partId>

## Yorumlar & Derecelendirmeler

<chapterId>8f27cc89-8759-4a4f-aff2-c1d3d9ecf14e</chapterId>

<isCourseReview>true</isCourseReview>
## Final Sınavı

<chapterId>d61dbdf3-b482-412b-b725-0a19006603b7</chapterId>

<isCourseExam>true</isCourseExam>
## Sonuç

<chapterId>9c501c44-0f1a-449e-8ab3-a5873abe4db6</chapterId>

<isCourseConclusion>true</isCourseConclusion>