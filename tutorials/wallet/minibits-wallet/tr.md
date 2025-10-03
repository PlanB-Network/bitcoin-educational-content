---
name: Minibits Wallet
description: Minibits Wallet için Kılavuz
---

![cover](assets/cover.webp)


Bu eğitimde, ecash kullanmak için Minibits Wallet'ü ayarlama konusunda size yol göstereceğim. Bitcoin ile birlikte çalışan güçlü bir gizlilik odaklı ödeme teknolojisi. Minibits, anında, ucuz ve özel değer transferleri sağlayan bir ecash ve Lightning Wallet'tür ve gizliliğin önemli olduğu günlük işlemler için idealdir.


Minibitlere dalmadan önce, ecash'in ne olduğu ve ne olmadığı konusunda net bir anlayışa sahip olalım. Birçok kişi ecash'i Bitcoin veya Blockchain teknolojisi ile karıştırmaktadır, ancak bunlar temelde farklı kavramlardır.


Ecash Bitcoin DEĞİLDİR. Kendinize ait Bitcoin Wallet'un yerini almaz, aksine onu tamamlar. Ecash bir Blockchain DEĞİLDİR ve herhangi bir halka açık Ledger üzerinde YAŞAMAZ. İlginç bir şekilde, ecash yeni bir teknoloji DEĞİLDİR - aslında 1980'lerde ve 1990'larda geliştirilen kavramlarla dünya çapındaki web'den önce gelir.


Ecash nedir: inanılmaz derecede özel (işlemler izlenebilir bir geçmiş bırakmaz), eşler arası (aracılar olmadan doğrudan transferler) ve dijital bir taşıyıcı araç olarak işlev görür (eğer ona sahipseniz, onu kontrol edersiniz). Önemli bir avantajı, ecash'in çevrimdışı kullanılabilmesidir - işlemler sırasında gönderici veya alıcının internet bağlantısı kesilebilir. Ecash tek bir tarafça veya güvenilir kuruluşlardan oluşan bir federasyon tarafından basılabilir ve Bitcoin için mükemmel bir tamamlayıcı teknolojidir, Bitcoin uzlaştırma Layer olarak hizmet verirken küçük, sık işlemleri gerçekleştirir.


Lütfen bu Minibits kurulumunun bir "saklama çözümü" olduğunu unutmayın; bu, fonlarınızı yönetmesi için Mint operatörüne güvendiğiniz anlamına gelir. Bu, devam etmeden önce anlamanız gereken belirli riskleri beraberinde getirir.


Projede bu önemli uyarı yer almaktadır:


- Bu Wallet sadece araştırma amaçlı kullanılmalıdır.
- Wallet, eksik işlevselliğe ve hem bilinen hem de bilinmeyen hatalara sahip bir beta sürümüdür.
- Büyük miktarlarda ecash ile kullanmayın.
- Wallet'te saklanan ecash darphane tarafından basılır
- elinizdekileri başka bir Bitcoin yıldırım Wallet'ya aktarana kadar darphanenin bunu Bitcoin ile destekleyeceğine güveniyorsunuz.
- Wallet'nin uyguladığı Cashu protokolü henüz kapsamlı bir inceleme veya testten geçmemiştir.


Minibit'lere bir tasarruf hesabı gibi değil, günlük Wallet gibi davranın ve burada asla önemli bir değer saklamayın.


## 1️⃣ Wallet'unuzun Kurulumu


Başlamak için, tüm büyük platformlar için indirme seçeneklerini bulacağınız [Minibits Web Sitesi](https://www.minibits.cash/) adresini ziyaret edin. iOS kullanıcıları [App Store](https://testflight.apple.com/join/defJQgTD) adresinden indirebilirken, AB iOS kullanıcıları [Freedom Store](https://freedomstore.io/) adresinden yükleme seçeneğine sahiptir. Android kullanıcıları uygulamayı [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) adresinden edinebilir veya APK dosyasını doğrudan [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases) sayfasından indirebilirler.


Minibits'i kurarken, temel kavramları açıklayan tanıtım ekranları göreceksiniz; bunları okuyabilir veya teknolojiye zaten aşina iseniz atlayabilirsiniz. Bu ilk adımları tamamladıktan sonra, aşağıdakiler arasında seçim yapmanız istenecektir:


- yeni kullanıcılar için `Anladım, beni Wallet`ye götür` veya
- bir yedekten geri yükleme yapıyorsanız `Kayıp Wallet`i kurtarın.


![image](assets/en/01.webp)

İlk kurulumu tamamladıktan sonra, dikkat edilmesi gereken birkaç önemli Elements içeren Ana Ekrana geleceksiniz. ① Üst köşedeki profil simgesi sizi Minibitlerinize Wallet Address erişebileceğiniz ve `toplu alım' seçeneklerini seçebileceğiniz profil sayfanıza götürür. ② Ekranın ortasında kullanabileceğiniz naneleri göreceksiniz, varsayılan olarak Minibits nanesi seçilidir. ③ Aşağıdaki eylem satırı ecash veya lightning ödemeleri göndermek, QR kodu taramak ve ödeme almak için seçenekler sunar. ④ Son olarak, alt gezinme çubuğu Ana ekran, İşlem Geçmişi, Kişiler ve Ayarlar için kısayollar içerir.


![image](assets/en/02.webp)


## 2️⃣ Nane şekerlerini yönetin


Uygulamayı başlattığınızda varsayılan olarak Minibits darphanesi etkinleştirilir. Bununla birlikte, ecash'in güçlü yönlerinden biri, daha fazla merkeziyetsizlik ve güvenlik için birden fazla darphane kullanabilmesidir. Başka bir darphane eklemek için `Ayarlar`a gidin, ardından `Darphaneleri yönet`i seçin ve son olarak `Darphane ekle`ye dokunun.


[Bitcoinmints.com] (Bitcoinmints.com), saygın seçenekleri seçmenize yardımcı olmak için kullanıcı derecelendirmeleriyle birlikte mevcut darphanelerin kapsamlı bir listesini sunar. Birden fazla darphane kullanmak riskinizi azaltır. Bir darphanede sorun yaşanırsa, diğer darphanelerdeki fonlarınız erişilebilir kalır.


![image](assets/en/04.webp)


## 3️⃣ Yedekleme Oluşturma


Yedekleme, tüm kurulum sürecindeki tartışmasız en kritik adımdır. Yedekleme seçeneklerine erişmek için `Ayarlar`-> `Yedekleme` bölümüne gidin Burada iki temel seçenek bulacaksınız:

1. cihaz kaybı durumunda ecash bakiyenizi kurtarmanızı sağlayan `12 kelime` içeren `seed cümleniz`. Bu seed cümlesi, eklediğiniz tüm darphanelerdeki tüm ecash için ana anahtarınızdır. Bunu fiziksel bir ortama (kağıt veya metal) yazın ve birden fazla yerde güvenli bir şekilde saklayın. seed ifadenizi asla ele geçirilebileceği bir yerde dijital olarak saklamayın. Wallet'nızı korumaya yönelik en iyi uygulamalar için bu [öğretici] (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) adresini ziyaret etmeyi düşünün.

2. uzun bir yedekleme dizesi içeren `Wallet yedekleme`.


**Dikkat**: Wallet'unuzu kurtarmak için bu yedeği kullanırken hala seed ifadenize ihtiyacınız olacaktır.


![image](assets/en/05.webp)


## 4️⃣ Minibit Oluştur Wallet Address


Ardından alttaki `Kişiler` bölümüne gidin ve `Değiştir` -> `Wallet Address'ü Değiştir` seçeneğine dokunarak size özel `Minibits Wallet Address'ü özelleştirin. Tercih ettiğiniz Address'ü girin ve müsaitlik durumunu kontrol edin.


![image](assets/en/07.webp)


Address'inizi ayarladıktan sonra, projeyi desteklemek için küçük bir `Bağış` yapmanız istenecektir. Bu isteğe bağlı olsa da, hizmeti düzenli olarak kullanmayı planlıyorsanız bunu dikkate almanızı şiddetle tavsiye ederim. Minibits gibi açık kaynaklı projeler, geliştirme ve bakımı sürdürmek için topluluk desteğine güvenir. Küçük bir katkı bile projenin uzun ömürlü olmasını sağlamaya yardımcı olur.


![image](assets/en/08.webp)


## 5️⃣ Nostr Kurulumu


Nostr'da takip ettiğiniz kişilere bahşiş vermek istiyorsanız, `Kişiler` ve ardından `Kamuya açık` seçeneğini belirleyerek `Npub anahtarınızı ekleyin`. Bu, Minibits Wallet'nızı Nostr sosyal ağına bağlayarak sorunsuz bahşiş vermenizi sağlar.


Kendi Nostr Address ve anahtarınızı içe aktarmak için `Ayarlar` ve ardından `Gizlilik` bölümüne giderek `Kendi profilinizi kullanın` seçeneğine de sahipsiniz. Ancak, bunu yapmanın Wallet'inizin minibits.cash Nostr ve LNURL Address sunucularıyla iletişimini durduracağını ve bu da zap ve ödeme almak için yıldırım Address özelliklerini devre dışı bırakacağını unutmayın.


![image](assets/en/09.webp)


## 6️⃣ Fon almak


Başlangıçta para almak için, Wallet'inize bir yıldırım Invoice aracılığıyla para yüklemeniz gerekir. Bu işlem basittir: `Yükleme` üzerine dokunun, eklemek istediğiniz `Miktarı` girin, isteğe bağlı olarak bir `Memo` ekleyin ve ardından `Invoice Oluştur` üzerine dokunun. Daha sonra bu Invoice'ı başka bir Lightning Wallet kullanarak ödemeniz gerekecek, bu Bitcoin Lightning ödemelerini Minibits Wallet'inizde ecash tokenlara dönüştürür.


![image](assets/en/10.webp)


## 7️⃣ Para gönder


Artık Wallet'nizi finanse ettiğinize göre, iki farklı şekilde para gönderebilirsiniz.


### Ecash gönder


İlk seçenek doğrudan ecash göndermektir. Gönder`e dokunun, ardından `Ecash Gönder`i seçin, `Miktar`ı girin ve `token Oluştur`a dokunun. Bu, alıcıyla paylaşabileceğiniz veya doğrudan cihazlarıyla taramalarını sağlayabileceğiniz bir QR kodu generate oluşturacaktır. Alıcı, Blockchain ücreti veya onay gecikmesi olmaksızın jetonların neredeyse anında Wallet'lerinde göründüğünü görecektir.


![image](assets/en/11.webp)


### Lightning ile Ödeme


İkinci seçenek Lightning ile ödeme yapmaktır. Gönder'e dokunun, ardından Lightning ile Öde'yi seçin. Nostr `kişileriniz` arasından seçim yapabilir (npub'ınızı bağladıysanız) veya `Yapıştır` veya `tarama` seçeneğini kullanarak bir Lightning Address, Invoice veya LNURL ödeme kodu girebilir/yapıştırabilirsiniz. Alıcıyı "Onayladıktan" sonra, "Ödenecek Tutarı" girmeniz, isteğe bağlı olarak bir not eklemeniz ve ardından Lightning işlemini tamamlamak için "Onayla" ve ardından "Şimdi öde" seçeneğine dokunmanız istenecektir.


![image](assets/en/12.webp)


## 8️⃣ NWC bağlantısı oluşturma


Minibits'in bir başka güçlü özelliği de, diğer uygulamaların özel anahtarlarınızı ifşa etmeden Wallet'unuzdan ödeme talep etmesine olanak tanıyan `Nostr Wallet Connect (NWC)` bağlantıları oluşturma yeteneğidir.


Bunu ayarlamak için `Ayarlar`a gidin, ardından `Nostr Wallet Connect`i seçin ve `Bağlantı ekle`ye dokunun. Bağlantınıza hem uygulamayı hem de ilişkili kullanıcı hesabını tanımlayacak açıklayıcı bir isim verin. Bu bağlantı üzerinden ne kadar harcama yapılabileceğini kontrol etmek için makul bir maksimum günlük limit belirleyin, ardından kurulumu tamamlamak için `Kaydet`e dokunun.


Bu özellik, her işlemi manuel olarak onaylamadan otomatik bahşişi etkinleştirmek istediğiniz Nostr Clients gibi hizmetler için özellikle kullanışlıdır.


![image](assets/en/12.webp)


## 🎯 Sonuç


Minibits, Bitcoin varlıklarınızı tamamlayan gizlilik odaklı ödemeler sunarak ecash dünyasına erişilebilir bir giriş noktası sağlar. Her zaman uygun yedeklemeler yapmayı unutmayın, yedeklilik için birden fazla darphane kullanmayı düşünün ve bu saklama çözümünde yalnızca uygun miktarları saklayın.


Ek kaynaklar için Minibits GitHub deposuna, resmi web sitesine ve topluluğun gelişmeleri aktif olarak tartıştığı ve sorunları giderdiği Telegram kanalına göz atın


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Web sitesi](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Ecash ekosistemi hala gelişmektedir, ancak Minibits gibi araçlar bu güçlü gizlilik teknolojisini günlük kullanıcılar için giderek daha erişilebilir hale getirmektedir.