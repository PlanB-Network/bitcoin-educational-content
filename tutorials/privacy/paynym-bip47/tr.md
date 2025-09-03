---
name: BIP47 - PayNym

description: PayNyms nasıl çalışır?
---
***UYARI:** Samourai Wallet'in kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, uygulama artık kendi Dojo'su olmayan kullanıcılar tarafından kullanılamıyor. BIP47, Sparrow wallet'da tüm kullanıcılar için ve **Samourai Wallet'de yalnızca Dojo'su olan kullanıcılar için kullanılabilir olmaya devam etmektedir**


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> "O çok büyük," dediler ve mahmuzlarla doğmuş olan ve kendini imparator sanan hindi horozu, tüm yelkenlerini açmış bir gemi gibi şişti ve gözleri ateş gibi kızarmış bir halde büyük bir öfkeyle ona doğru yürüdü. Zavallı küçük ördek yavrusu direnmekle kaçmak arasında kararsız kalmış ve bahçedeki tüm ördekler tarafından hor görüldüğü için çok mutsuz olmuş.

![BIP47, the ugly duckling illustration](assets/1.webp)


Bitcoin protokolündeki en önemli sorunlardan biri Address'nin yeniden kullanımıdır. Ağın şeffaflığı ve dağılımı bu uygulamayı kullanıcı gizliliği açısından tehlikeli hale getirmektedir. Bununla ilgili sorunlardan kaçınmak için, bir Wallet'e gelen her yeni ödeme için yeni bir boş alıcı Address kullanılması önerilir, ancak bazı durumlarda bunu başarmak karmaşık olabilir.


Bu uzlaşma Beyaz Kitap kadar eskidir. Satoshi, 2008'in sonlarında yayınlanan çalışmasında bizi bu risk konusunda uyarmıştı:


> Ek bir güvenlik duvarı olarak, her bir işlemin ortak bir sahibine bağlanmasını önlemek için yeni bir anahtar çifti kullanılmalıdır.

Address yeniden kullanımı olmadan birden fazla ödeme almak için birçok çözüm mevcuttur. Her birinin ödünleri ve dezavantajları vardır. Tüm bu çözümler arasında, Justus Ranvier tarafından geliştirilen ve 2015 yılında yayınlanan, yeniden kullanılabilir ödeme kodlarının oluşturulmasına olanak tanıyan bir öneri olan [BIP47] (https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki) bulunmaktadır. Amacı, bir Address'yı tekrar kullanmadan aynı kişiye birden fazla işlem yapılmasını sağlamaktır.


Başlangıçta, bu öneri topluluğun bir kısmı tarafından küçümseme ile karşılandı ve hiçbir zaman Bitcoin core'a eklenmedi. Ancak, bazı yazılımlar yine de bunu kendi başlarına uygulamayı seçti. Örneğin, Samourai Wallet kendi BIP47 uygulamasını geliştirdi: PayNym. Bugün, bu uygulama akıllı telefonlar için Samourai Wallet'da ve PC'ler için [Sparrow wallet](https://sparrowwallet.com/)'de mevcuttur.


Zaman içinde Samourai, doğrudan PayNym ile ilgili yeni özellikler programladı. Artık, PayNym ve BIP47'ye dayalı olarak kullanıcı gizliliğini optimize etmek için kullanılabilecek bütün bir araç ekosistemi var.

Bu makalede, BIP47 ve PayNym'in prensiplerini, bu protokollerin mekanizmalarını ve bunlardan kaynaklanan pratik uygulamaları keşfedeceksiniz. Şu anda PayNym için kullanılan BIP47'nin sadece ilk versiyonunu Address ile anlatacağım, ancak 2, 3 ve 4 versiyonları pratikte aynı şekilde çalışmaktadır.


**Tek büyük farkın bildirim işleminde olduğunu unutmayın:


- Sürüm 1, bildirim için OP_RETURN ile basit bir Address kullanır,
- Sürüm 2, OP_RETURN ile birlikte bir Multisig komut dosyası (bloom-Multisig) kullanır,
- Sürüm 3 ve 4 ise basitçe bir Multisig betiği kullanır (cfilter-Multisig).


Bu makalede ele alınan mekanizmalar, incelenen kriptografik yöntemler de dahil olmak üzere, bu nedenle dört versiyona da uygulanabilir. Bugüne kadar, Samourai Wallet ve Sparrow üzerindeki PayNym uygulaması BIP47'nin ilk versiyonunu kullanmaktadır.


## Özet:


1- Address'un yeniden kullanımı sorunu.


2- BIP47 ve PayNym İlkeleri.


3- Öğreticiler: PayNym Kullanımı.



- Samourai Wallet ile bir BIP47 işlemi oluşturmak.
- Sparrow wallet ile bir BIP47 işlemi oluşturmak.


4- BIP47'nin işleyişi.



- Yeniden kullanılabilir ödeme kodu.
- Kriptografik yöntem: Eliptik eğriler (ECDH) üzerine kurulmuş Diffie-Hellman anahtar Exchange.
- Bildirim işlemi.
- Bildirim işleminin oluşturulması.
- Bildirim işleminin alınması.
- BIP47 ödeme işlemi.
- BIP47 ödemesinin alınması ve özel anahtarın türetilmesi.
- BIP47 ödemesinin geri ödenmesi.


5- PayNym'in türetilmiş kullanımları.


6- BIP47 hakkındaki kişisel görüşüm.


## Address'ün yeniden kullanımı sorunu.


Alıcı Address bitcoinleri almak için kullanılır. Bir açık anahtardan hashlenerek ve belirli bir format uygulanarak oluşturulur. Böylece, sahibini değiştirmek için bir Coin üzerinde yeni bir harcama koşulu oluşturulmasına izin verir.


Bir alıcı Address oluşturma hakkında daha fazla bilgi edinmek için bu makalenin son bölümünü okumanızı tavsiye ederim: **Bitcoin Wallet - [ebook Bitcoin Démocratisé 2]'den** alıntı (https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).


Ayrıca, muhtemelen bilgili bir bitcoin kullanıcısından alıcı adreslerin tek seferlik kullanım için olduğunu ve generate'unuza gelen her yeni ödeme için yeni bir Wallet almanız gerektiğini duymuşsunuzdur. Tamam, ama neden?


Temel olarak, Address'in yeniden kullanımı fonlarınızı doğrudan tehlikeye atmaz. Eliptik eğriler üzerinde kriptografi kullanımı, ağa özel bir anahtara sahip olduğunuzu, bu anahtarı ifşa etmeden kanıtlamanıza olanak tanır. Bu nedenle, aynı Address üzerinde birden fazla farklı UTXO (Harcanmamış İşlem Çıkışı) kilitleyebilir ve bunları farklı zamanlarda harcayabilirsiniz. Bu Address ile ilişkili özel anahtarı ifşa etmezseniz, hiç kimse fonlarınıza erişemez. Address'in yeniden kullanımıyla ilgili sorun daha çok gizlilikle ilgilidir.


Giriş bölümünde de belirtildiği gibi, Bitcoin ağının şeffaflığı ve dağılımı, bir düğüme erişimi olan herhangi bir kullanıcının ödeme sisteminin işlemlerini gözlemleyebileceği anlamına gelir. Sonuç olarak, farklı adres bakiyelerini görebilirler. Satoshi Nakamoto daha sonra bir Wallet'e gelen her yeni ödeme için yeni anahtar çiftleri ve dolayısıyla yeni adresler üretme olasılığından bahsetti. Amaç, kullanıcının kimliği ile anahtar çiftlerinden biri arasında bir ilişki olması durumunda ek bir güvenlik duvarına sahip olmak olacaktır.


Günümüzde, zincir analiz şirketlerinin varlığı ve KYC'nin (Müşterini Tanı) gelişmesiyle birlikte, boş adres kullanımı artık ek bir güvenlik duvarı değil, gizliliğine biraz bile önem veren herkes için bir zorunluluktur.


Gizlilik arayışı, Maximalist Bitcoin kullanıcılarının bir konforu ya da fantezisi değildir. Kişisel güvenliğinizi ve fonlarınızın güvenliğini doğrudan etkileyen belirli bir parametredir. Bunu anlamanıza yardımcı olmak için işte size çok somut bir örnek:



- Bob, Dolar Maliyet Ortalaması (DCA) yoluyla Bitcoin satın alır, yani giriş fiyatının ortalamasını almak için düzenli aralıklarla az miktarda Bitcoin satın alır. Bob, satın aldığı fonları sistematik olarak aynı alıcı Address'ya gönderir. Her hafta 0,01 Bitcoin satın alır ve bunu aynı Address'ya gönderir. İki yıl sonra, Bob bu Address'da tam bir Bitcoin biriktirmiştir.
- Köşedeki fırıncı Bitcoin ödemelerini kabul ediyor. Bitcoin harcayabileceği için heyecanlanan Bob, bagetini satoshis olarak almaya gider. Ödeme yapmak için Address'unda kilitli olan fonları kullanır. Fırıncısı artık onun bir Bitcoin'a sahip olduğunu bilmektedir. Bu önemli miktar kıskançlık yaratabilir ve Bob gelecekte fiziksel bir saldırıya uğrama riskiyle karşı karşıya kalabilir.


Address'nin yeniden kullanımı, bir gözlemcinin farklı UTXO'larınız arasında ve bazen kimliğiniz ile tüm Wallet arasında inkar edilemez bir bağlantı kurmasını sağlar.

Bu nedenle Bitcoin Wallet yazılımlarının çoğu "Al" düğmesine tıkladığınızda otomatik olarak yeni bir alıcı Address oluşturur. Normal kullanıcılar için yeni adres kullanma alışkanlığı edinmek büyük bir rahatsızlık değildir. Ancak, çevrimiçi bir işletme, bir Exchange veya bir bağış kampanyası için bu kısıtlama hızla yönetilemez hale gelebilir.

Bu kuruluşlar için birçok çözüm bulunmaktadır. Her birinin avantajları ve dezavantajları var, ancak bugüne kadar ve daha sonra göreceğimiz gibi, BIP47 diğerlerinden gerçekten öne çıkıyor.


Address'in yeniden kullanımı konusu Bitcoin'da göz ardı edilebilir olmaktan çok uzaktır. Oxt.me web sitesinden alınan aşağıdaki grafikte de görebileceğiniz gibi, Bitcoin kullanıcılarının genel Address yeniden kullanım oranı şu anda %52'dir:

OXT.me'den alınan ve Address ağındaki genel Bitcoin yeniden kullanım oranının gelişimini gösteren grafik.


![image](assets/2.webp)

_COPYKredi: OXT_


Bu yeniden kullanımların çoğu, verimlilik ve kolaylık nedenleriyle aynı Address'yi birçok kez yeniden kullanan borsalardan gelmektedir. BIP47, bugüne kadar borsalar arasındaki bu olguyu durdurmak için en iyi çözüm olacaktır. Bu, bu kuruluşlar için çok fazla sürtüşmeye neden olmadan genel Address yeniden kullanım oranını azaltmaya yardımcı olacaktır.


Tüm ağ genelinde alınan bu küresel önlem, bu durumda özellikle önemlidir. Gerçekten de, Address'ün yeniden kullanımı sadece bu uygulamayı yapan kişi için değil, aynı zamanda onlarla işlem yapan herkes için bir sorundur. Bitcoin'teki gizlilik kaybı, kullanıcıdan kullanıcıya yayılan bir virüs gibi hareket eder. Tüm ağ işlemleri üzerinde küresel bir ölçütü incelemek, bu olgunun boyutunu anlamamızı sağlar.


## BIP47 ve PayNym ilkeleri.


BIP47, Address yeniden kullanımı olmadan birden fazla ödeme almak için basit bir yol sağlamayı amaçlamaktadır. Çalışması, yeniden kullanılabilir bir ödeme kodunun kullanımına dayanmaktadır.


Böylece, birden fazla gönderici, alıcının her yeni işlem için yeni bir boş Address sağlamasına gerek kalmadan, başka bir kullanıcının yeniden kullanılabilir tek bir ödeme koduna birden fazla ödeme gönderebilir.


Bir kullanıcı, normal bir Address veya açık anahtar almanın aksine, gizlilik kaybı riski olmadan ödeme kodunu (sosyal ağlarda, web sitelerinde...) özgürce paylaşabilir.

Bir Exchange gerçekleştirmek için, her iki kullanıcının da Samourai Wallet veya Sparrow wallet üzerinde PayNym gibi bir BIP47 uygulamasına sahip bir Bitcoin Wallet'ye sahip olması gerekir. İki kullanıcının ödeme kodlarının ilişkilendirilmesi, aralarında gizli bir kanal oluşturacaktır. Bu kanalın düzgün bir şekilde kurulması için göndericinin Bitcoin Blockchain üzerinde bir işlem yapması gerekir: bildirim işlemi (bu konuda daha sonra daha fazla açıklama yapacağım).


İki kullanıcının ödeme kodlarının ilişkilendirilmesi, kendileri generate çok sayıda benzersiz Bitcoin alıcı adresi (tam olarak 2^32) olan paylaşılan sırlar oluşturur. Dolayısıyla, gerçekte, BIP47 ile yapılan ödeme ödeme koduna değil, ilgili tarafların ödeme kodlarından türetilen tamamen normal adreslere gönderilir.


Ödeme kodu, Wallet seed'dan türetilen sanal bir tanımlayıcı görevi görür. HD Wallet türetme yapısında, ödeme kodu 3. derinlikte, Wallet hesap seviyesinde yer alır.


![image](assets/3.webp)


Türetme amacı BIP47'ye referansla 47' (0x8000002F) olarak belirtilmiştir. Örneğin, yeniden kullanılabilir bir ödeme kodu için türetme yolu şöyle olabilir: ** m/47'/0'/0'/**


Ödeme kodunun neye benzediği konusunda size bir fikir vermek için, işte benimki: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


İletişimi kolaylaştırmak için QR kodu olarak da kodlanabilir:


![image](assets/4.webp)


Twitter'da gördüğünüz robotlar olan PayNym Botlarına gelince, bunlar Samourai Wallet tarafından oluşturulan ödeme kodunuzun görsel temsilleridir. Bir Hash işlevi kullanılarak oluşturulurlar, bu da onları neredeyse benzersiz kılar. İşte benimki tanımlayıcısıyla birlikte: **+throbbingpond8B1**


![image](assets/5.webp)


Bu Botların gerçek bir teknik faydası yoktur. Bunun yerine, sanal bir görsel kimlik oluşturarak kullanıcılar arasındaki etkileşimleri kolaylaştırırlar.


Kullanıcı için PayNym uygulaması ile bir BIP47 ödemesi yapma süreci son derece basittir. Alice'un Bob'e ödeme göndermek istediğini düşünelim:


1. Bob QR kodunu veya doğrudan yeniden kullanılabilir ödeme kodunu paylaşır. Bunu web sitesine, çeşitli kamusal sosyal ağlarına yerleştirebilir veya başka bir iletişim aracıyla Alice'e gönderebilir.

2. Alice Samourai veya Sparrow yazılımını açar ve Bob'in ödeme kodunu tarar veya yapıştırır.

3. Alice kendi PayNym'ini Bob'inkine bağlar (İngilizce'de "Follow"). Bu işlem off-chain tarafından yapılır ve tamamen serbest kalır.

4. Alice kendi PayNym'ini Bob'ünkine bağlar (İngilizce'de "Connect"). Bu işlem "On-Chain" ile yapılır. Alice, Samourai'deki hizmet için Mining işlem ücretlerinin yanı sıra 15.000 Sats sabit ücret ödemek zorundadır. Sparrow'de hizmet ücretlerinden feragat edilir. Bu adım, bildirim işlemi olarak adlandırdığımız adımdır.

5. Bildirim işlemi onaylandıktan sonra Alice, Bob'a bir BIP47 ödeme işlemi oluşturabilir. Wallet otomatik olarak generate'e sadece Bob'un özel anahtarına sahip olduğu yeni bir boş alıcı Address gönderecektir.


Bildirim işlemini gerçekleştirmek, yani PayNym'ini bağlamak, BIP47 ödemeleri yapmak için zorunlu bir ön koşuldur. Ancak, bu yapıldıktan sonra, gönderici yeni bir bildirim işlemi gerçekleştirmeye gerek kalmadan alıcıya birden fazla ödeme yapabilir (tam olarak 2^32).


PayNym'leri birbirine bağlamak için iki farklı işlem olduğunu fark etmiş olabilirsiniz: "takip et" ve "bağlan". Bağlantı işlemi ("connecter") BIP47 bildirim işlemine karşılık gelir ve bu işlem basitçe bir OP_RETURN çıktısı aracılığıyla iletilen belirli bilgilere sahip bir Bitcoin işlemidir. Böylece, yeni boş alıcı adresleri oluşturmak için gerekli olan paylaşılan sırları üretmek üzere iki kullanıcı arasında şifreli iletişim kurulmasına yardımcı olur.


Öte yandan, bağlantı kurma işlemi ("follow" veya "relier"), Samourai ekipleri tarafından özel olarak geliştirilen Tor tabanlı şifreli bir iletişim protokolü olan Soroban'da bir bağlantıya izin verir.


Özetlemek gerekirse:



- İki PayNym'i birbirine bağlamak ("takip etmek") tamamen ücretsizdir. Özellikle Samourai'nin işbirlikçi işlem araçlarını (Stowaway veya StonewallX2) kullanmak için off-chain şifreli iletişim kurmaya yardımcı olur. Bu işlem PayNym'e özeldir ve BIP47'de açıklanmamıştır.
- İki PayNym'in bağlanması bir maliyete neden olur. Bu, bağlantıyı başlatmak için bildirim işleminin gerçekleştirilmesini içerir. Maliyet, hizmet ücretleri, Mining işlem ücretleri ve tünelin açıldığını bildirmek için alıcının bildirim Address'üne gönderilen 546 Sats'ten oluşur. Bu işlem BIP47 ile ilgilidir. Tamamlandığında, gönderici alıcıya birden fazla BIP47 ödemesi yapabilir.


İki PayNym'i bağlamak için bunların zaten bağlı olması gerekir.


## Eğitimler: PayNym Kullanımı.


Şimdi teoriyi gördüğümüze göre, pratiği birlikte çalışalım. Aşağıdaki eğitimlerin amacı Sparrow wallet'daki PayNym'imi Samourai Wallet'deki PayNym'ime bağlamaktır. İlk eğitim Samourai'den Sparrow'ye yeniden kullanılabilir ödeme kodunu kullanarak nasıl işlem yapacağınızı gösterir ve ikinci eğitim Sparrow'den Samourai'ye aynı mekanizmayı açıklar.


**Not:** Bu eğitimleri Testnet üzerinde gerçekleştirdim. Bunlar gerçek bitcoin değildir.


### Samourai Wallet ile bir BIP47 işlemi oluşturmak.


Başlamak için tabii ki Samourai Wallet uygulamasına ihtiyacınız var. Doğrudan Google Play Store'dan veya resmi Samourai web sitesinde bulunan APK dosyası ile indirebilirsiniz.


Wallet başlatıldıktan sonra, henüz başlatmadıysanız, sağ alttaki artıya (+) ve ardından "PayNym "e tıklayarak PayNym'inizi talep edin.


Bir BIP47 ödemesi yapmak için ilk adım, alıcımızdan yeniden kullanılabilir ödeme kodunu almaktır. Ardından, onlarla bağlantı kurabilecek ve daha sonra bağlantı kurabileceğiz:


![video](assets/6.mp4)


Bildirim işlemi onaylandıktan sonra, alıcıma birden fazla ödeme gönderebilirim. Her işlem otomatik olarak alıcının anahtarlarına sahip olduğu yeni bir boş Address ile yapılacaktır. Alıcının herhangi bir işlem yapmasına gerek yoktur, her şey benim tarafımdan hesaplanır.


Samourai Wallet üzerinde BIP47 işleminin nasıl yapılacağı aşağıda açıklanmıştır:


![video](assets/7.mp4)


### Sparrow wallet ile bir BIP47 işlemi oluşturmak.


Tıpkı Samourai'de olduğu gibi, Sparrow yazılımına sahip olmanız gerekir. Bu yazılım bilgisayarınızda mevcuttur. Resmi web sitelerinden indirebilirsiniz](https://sparrowwallet.com/).


Makinenize yüklemeden önce geliştiricinin imzasını ve indirilen yazılımın bütünlüğünü doğruladığınızdan emin olun.


Bir Wallet oluşturun ve üst çubuktaki "Araç" menüsünden "PayNym Göster" seçeneğine tıklayarak PayNym'inizi talep edin:


![image](assets/8.webp)


Ardından, PayNym'inizi alıcınızınkiyle ilişkilendirmeniz ve bağlamanız gerekecektir. Bunu yapmak için, "Kişi Bul" penceresine yeniden kullanılabilir ödeme kodunu girin, onları takip edin ve ardından "Kişiyi Bağla" seçeneğine tıklayarak bildirim işlemini gerçekleştirin:


![image](assets/9.webp)


Bildirim işlemi onaylandıktan sonra, yeniden kullanılabilir ödeme koduna ödeme gönderebilirsiniz. İşte nasıl yapılacağı:


![video](assets/10.mp4)


Şimdi BIP47'nin PayNym uygulamasının pratik yönünü inceleyebildiğimize göre, tüm bu mekanizmaların nasıl çalıştığını ve hangi kriptografik yöntemlerin kullanıldığını görelim.


## BIP47'nin iç işleyişi.


BIP47'nin mekanizmalarını incelemek için, hiyerarşik deterministik (HD) Wallet'in yapısını, alt anahtar çiftlerini türetme mekanizmalarını ve eliptik eğri kriptografisinin ilkelerini anlamak çok önemlidir. Neyse ki, bu bölümü anlamak için gerekli tüm bilgileri blogumda bulabilirsiniz:



- [Bir Bitcoin Wallet'un türetme yollarını anlamak](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-Bitcoin)



- [Bitcoin Wallet - Bitcoin Democratized 2 adlı e-kitaptan alıntı] (https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2)


### Yeniden kullanılabilir ödeme kodu.


Bu makalenin ikinci bölümünde açıklandığı üzere, yeniden kullanılabilir ödeme kodu HD Wallet'ün üçüncü derinliğinde yer almaktadır. Hem yerleşimi ve yapısı hem de rolü bakımından bir xpub ile karşılaştırılabilir.


İşte 80 baytlık bir ödeme kodunu oluşturan farklı parçalar:



- _Bayt 0_: Sürüm. BIP47'nin ilk sürümü kullanılıyorsa, bu bayt 0x01'e eşit olacaktır.
- bayt 1_: Bit alanı. Bu alan, özel kullanım durumunda ek göstergeler sağlamak için ayrılmıştır. Sadece PayNym kullanılıyorsa, bu bayt 0x00'a eşit olacaktır.
- bayt 2_: Y paritesi. Bu bayt, açık anahtarımızın y-koordinatının değerinin paritesine (çift veya tek sayı) bağlı olarak 0x02 veya 0x03'ü gösterir. Bu uygulama hakkında daha fazla bilgi için lütfen bu makalenin "Address türetme" bölümünün 1. adımını okuyun.
- _3. bayttan 34. bayta kadar_: X değeri. Bu baytlar açık anahtarımızın x koordinatını gösterir. X ve y paritesinin birleştirilmesi bize sıkıştırılmış açık anahtarımızı verir.
- _35. bayttan 66. bayta kadar_: chain code. Bu alan, yukarıda belirtilen açık anahtarla ilişkili chain code için ayrılmıştır.
- _67. bayttan 79. bayta kadar_: Dolgu. Bu alan gelecekteki olası gelişmeler için ayrılmıştır. Sürüm 1 için, bir OP_RETURN çıktısı için veri boyutu olan 80 bayta ulaşmak için burayı sıfırlarla dolduruyoruz.


İşte önceki bölümde sunulan yeniden kullanılabilir ödeme kodumun onaltılık gösterimi ve yukarıda sunulan baytlara karşılık gelen renkler:

Daha sonra, bir ödeme koduyla uğraştığımızı hızlı bir şekilde tanımlamak için "P" önek baytını da eklemeniz gerekir. Bu bayt 0x47'dir.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000**


Son olarak, bu ödeme kodunun sağlama toplamını HASH256 kullanarak hesaplıyoruz, yani SHA256 işleviyle çift hash yapıyoruz. Bu özetin ilk dört baytını alıyoruz ve sonunda birleştiriyoruz (pembe renkte).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4**


Ödeme kodu hazır, şimdi sadece onu Base 58'e dönüştürmemiz gerekiyor:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Gördüğünüz gibi, bu yapı "xpub" tipi genişletilmiş bir açık anahtarın yapısına çok benzemektedir.


Bu işlem sırasında ödeme kodumuzu elde etmek için sıkıştırılmış bir açık anahtar ve bir chain code kullandık. Bu iki Elements, aşağıdaki türetme yolunu izleyerek Wallet seed'den deterministik ve hiyerarşik bir türetmenin sonucudur: m/47'/0'/0'/


Somut olarak, yeniden kullanılabilir ödeme kodunun açık anahtarını ve chain code'i elde etmek için, seed'den ana özel anahtarı hesaplayacağız, ardından 47 + 2^31 indeksli bir alt çift türeteceğiz (sertleştirilmiş türetme). Ardından, 2^31 indeksli iki alt çift daha türeteceğiz (sertleştirilmiş türetme).


**Not:** Hiyerarşik deterministik bir Bitcoin Wallet içinde alt anahtar çiftleri türetme hakkında daha fazla bilgi edinmek istiyorsanız, CRYPTO301'i almanızı öneririm.


### Kriptografik yöntem: Eliptik Eğri Diffie-Hellman anahtarı Exchange (ECDH).


BIP47'nin özünde kullanılan kriptografik yöntem ECDH'dir (Eliptik-Eğri Diffie-Hellman). Bu protokol klasik Diffie-Hellman anahtarı Exchange'nın bir varyantıdır.


Diffie-Hellman, ilk versiyonunda, her biri bir çift açık ve özel anahtara sahip iki tarafın güvensiz bir iletişim kanalı üzerinden bilgi alışverişi yaparak paylaşılan bir sırrı belirlemesine olanak tanıyan ve 1976 yılında sunulan bir anahtar anlaşma protokolüdür.


![image](assets/11.webp)


Bu paylaşılan sır (kırmızı anahtar) daha sonra başka görevler için kullanılabilir. Tipik olarak bu paylaşılan sır, güvensiz bir ağ üzerinden iletişimi şifrelemek ve şifresini çözmek için kullanılabilir:


![image](assets/12.webp)


Bu Exchange'ye ulaşmak için Diffie-Hellman paylaşılan sırrı hesaplamak için modüler aritmetik kullanır. İşte nasıl çalıştığına dair basitleştirilmiş bir açıklama:



- Alice ve Bob ortak bir renkte, bu durumda sarı renkte hemfikirdir. Bu renk herkes tarafından bilinmektedir. Bu kamuya açık bir bilgidir.
- Alice gizli bir renk seçer, bu durumda kırmızı. İki rengi karıştırarak turuncu rengi elde eder.
- Bob gizli bir renk seçer, bu durumda deniz mavisi. İki rengi karıştırarak gök mavisini elde eder.
- Alice ve Bob elde ettikleri renkleri Exchange yapabilir: turuncu ve gök mavisi. Bu Exchange güvensiz bir ağ üzerinden gerçekleşebilir ve saldırganlar tarafından gözlemlenebilir.
- Alice, Bob'dan aldığı gök mavisi rengi kendi gizli rengiyle (kırmızı) karıştırır. Kahverengi elde eder.
- Bob, Alice'den aldığı turuncu rengi kendi gizli rengiyle (deniz mavisi) karıştırır. Ayrıca kahverengi de elde eder.


![image](assets/13.webp)


**Kredi:** Orijinal fikir: A.J. Han VinckVektör versiyonu: FlugaalÇeviri: Dereckson, Kamu malı, Wikimedia Commons aracılığıyla. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg


Bu basitleştirmede, kahverengi renk Alice ve Bob arasında paylaşılan sırrı temsil etmektedir. Gerçekte, saldırganın Alice veya Bob'ın gizli renklerini elde etmek için turuncu ve gök mavisi renklerini ayırmasının imkansız olduğu düşünülmelidir.


Şimdi, gerçek işleyişini inceleyelim. İlk bakışta Diffie-Hellman'ı kavramak karmaşık görünebilir. Gerçekte, çalışma prensibi neredeyse çocuk oyuncağıdır. Mekanizmalarını detaylandırmadan önce, ihtiyaç duyacağımız (ve tesadüfen diğer birçok kriptografik yöntemde de kullanılan) iki matematiksel kavramı hızlıca hatırlatacağım.


1. Asal sayı, sadece iki böleni olan doğal bir sayıdır: 1 ve kendisi. Örneğin, 7 sayısı asaldır çünkü yalnızca 1 ve 7 (kendisi) ile bölünebilir. Öte yandan, 8 sayısı asal değildir çünkü 1, 2, 4 ve 8 ile bölünebilir. Bu nedenle sadece iki bölen değil, dört tam ve pozitif bölen vardır.

2. "Modulo" ("mod" veya "%" olarak gösterilir), iki tam sayının ilk sayının ikinci sayıya Öklidyen bölümünden kalanı döndürmesini sağlayan matematiksel bir işlemdir. Örneğin, 16 mod 5 1'e eşittir.


Alice ve Bob arasındaki Diffie-Hellman anahtarı Exchange aşağıdaki gibi çalışır:



- Alice ve Bob iki ortak sayı belirler: p ve g. p bir asal sayıdır. Bu p sayısı ne kadar büyük olursa Diffie-Hellman o kadar güvenli olacaktır. g, p'nin ilkel köküdür. Bu iki sayı güvensiz bir ağ üzerinden düz metin olarak iletilebilir, bunlar yukarıdaki basitleştirmedeki sarı rengin eşdeğerleridir. Alice ve Bob'in p ve g için tam olarak aynı değerlere sahip olması gerekir.
- Parametreler seçildikten sonra, Alice ve Bob'nin her biri kendi başına gizli bir rastgele sayı belirler. Alice tarafından elde edilen rastgele sayı a (kırmızı renge eşdeğer) ve Bob tarafından elde edilen rastgele sayı b (deniz mavisi renge eşdeğer) olarak adlandırılır. Bu iki sayı gizli kalmalıdır.
- Bu a ve b sayılarını değiş tokuş etmek yerine, her bir taraf A (büyük harf) ve B'yi (büyük harf) şu şekilde hesaplayacaktır:


A, a modulo p'nin kuvvetine yükseltilmiş g'ye eşittir:

**A = g^a % p**


B, b modulo p'nin kuvvetine yükseltilmiş g'ye eşittir:

**B = g^b % p**



- Bu A (turuncu renge eşdeğer) ve B (gök mavisi renge eşdeğer) numaraları iki taraf arasında değiş tokuş edilecektir. Exchange güvensiz bir ağ üzerinden düz metin olarak yapılabilir.
- Artık B'yi bilen Alice, z değerini öyle hesaplayacaktır ki:


z, B'nin a modulo p kuvvetine yükseltilmiş haline eşittir:

**z = B^a % p**



- Bir hatırlatma olarak, B = g^b % p. Bu nedenle:

**z = B^a % p**

**z = (g^b)^a % p**


Üs alma kurallarına göre:

**(x^n)^m = x^nm**


Bu yüzden:

**z = g^ba % p**



- Artık A'yı bilen Bob, z'nin değerini de aşağıdaki gibi hesaplayacaktır:


z, b modulo p'nin kuvvetine yükseltilmiş A'ya eşittir:

**z = A^b % p**


Bu yüzden:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Modulo operatörünün dağılabilirliği sayesinde, Alice ve Bob z için tam olarak aynı değeri bulur. Bu sayı, önceki açıklamadaki kahverengi renge eşdeğer olan paylaşılan sırlarını temsil eder. Bu paylaşılan sırrı, güvensiz bir ağ üzerinde aralarındaki iletişimi şifrelemek için kullanabilirler.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


P, g, A ve B'ye sahip olan bir saldırgan a, b veya z'yi hesaplayamayacaktır. Bu işlemi gerçekleştirmek için üs alma işlemini tersine çevirmek gerekir ki sonlu bir alanla çalıştığımız için tüm olasılıkları tek tek denemek dışında bunu yapmak imkansızdır. Bu, döngüsel sonlu bir grupta üs alma işleminin tersi olan ayrık logaritmayı hesaplamaya eşdeğer olacaktır.


Bu nedenle, a, b ve p için yeterince büyük değerler seçtiğimiz sürece Diffie-Hellman güvenlidir. Tipik olarak, 2.048 bitlik parametrelerle (ondalık olarak 600 basamaklı bir sayı), a ve b için tüm olasılıkları test etmek pratik olmayacaktır. Bugüne kadar, bu büyüklükteki sayılarla algoritma güvenli kabul edilmektedir.


Diffie-Hellman protokolünün ana dezavantajı da tam olarak burada yatmaktadır. Güvenli olması için algoritmanın büyük sayılar kullanması gerekir. Sonuç olarak, artık Diffie-Hellman'ın cebirsel bir eğri, özellikle de eliptik bir eğri kullanan bir çeşidi olan ECDH algoritması tercih edilmektedir. Bu, eşdeğer güvenliği korurken çok daha küçük sayılarla çalışmamızı sağlar ve böylece gereken hesaplama ve depolama kaynaklarını azaltır.


Algoritmanın genel prensibi aynı kalmaktadır. Ancak, rastgele bir a sayısı ve a'dan modüler üs alma kullanılarak hesaplanan bir A sayısı kullanmak yerine, eliptik bir eğri üzerinde oluşturulmuş bir çift anahtar kullanacağız. Modulo operatörünün dağıtılabilirliğine güvenmek yerine, eliptik eğriler üzerindeki grup yasasını, özellikle de bu yasanın birleştirilebilirliğini kullanacağız.

Eğer özel ve açık anahtarların eliptik eğri üzerinde nasıl çalıştığı hakkında bilginiz yoksa, bu makalenin ilk altı bölümünde bu yöntemin temellerini açıklayacağım.


Kabaca özetlemek gerekirse, özel anahtar 1 ile n-1 arasında rastgele bir sayıdır (burada n eğrinin sırasıdır) ve açık anahtar, özel anahtar tarafından nokta toplama ve üreteç noktasından iki katına çıkarma yoluyla belirlenen eğri üzerindeki benzersiz bir noktadır, aşağıdaki gibi:


**K = k-G**


Burada K açık anahtar, k özel anahtar ve G üreteç noktasıdır.


Bu anahtar çiftinin özelliklerinden biri, k ve G'yi biliyorsanız K'yi belirlemenin çok kolay olmasıdır, ancak K ve G'yi biliyorsanız k'yi belirlemek şu anda imkansızdır.


Başka bir deyişle, özel anahtarı biliyorsanız açık anahtarı kolayca hesaplayabilirsiniz, ancak açık anahtarı biliyorsanız özel anahtarı hesaplamak imkansızdır. Bu güvenlik bir kez daha ayrık logaritmanın hesaplanmasının imkansızlığına dayanmaktadır.


Bu özelliği Diffie-Hellman algoritmamızı uyarlamak için kullanacağız. Böylece, ECDH'nin çalışma prensibi aşağıdaki gibidir:



- Alice ve Bob kriptografik olarak güvenli bir eliptik eğri ve parametreleri üzerinde anlaşır. Bu bilgi kamuya açıktır.
- Alice, özel anahtarı olacak rastgele bir ka sayısı üretir. Bu özel anahtar gizli kalmalıdır. Açık anahtarı Ka'yı seçilen eliptik eğri üzerinde noktalar ekleyerek ve ikiye katlayarak belirler.


**Ka = ka-G**



- Bob ayrıca kendi özel anahtarı olacak rastgele bir kb sayısı üretir. İlişkili açık anahtar Kb'yi hesaplar.


**Kb = kb-G**



- Alice ve Bob Exchange açık anahtarları Ka ve Kb'yi güvensiz bir genel ağ üzerinden.
- Alice kendi özel anahtarı ka'yı Bob'in açık anahtarı Kb'ye uygulayarak eğri üzerinde bir nokta (x, y) hesaplar.


**(x, y) = ka-Kb**



- Bob kendi özel anahtarı kb'yi Alice'nin açık anahtarı Ka'ya uygulayarak eğri üzerinde bir nokta (x, y) hesaplar.


**(x, y) = kb-Ka**



- Alice ve Bob eliptik eğri üzerinde aynı noktayı elde eder. Paylaşılan gizli bilgi bu noktanın x-koordinatı olacaktır.


Aynı paylaşılan sırrı elde ederler çünkü:


**(x, y) = ka-Kb = ka-kb-G = kb-ka-G = kb-Ka**


Güvensiz genel ağı gözlemleyen potansiyel bir saldırgan sadece her bir tarafın açık anahtarlarını ve seçilen eğri parametrelerini elde edebilir. Daha önce açıklandığı gibi, bu iki bilgi tek başına özel anahtarların belirlenmesine izin vermez, bu nedenle saldırgan sırra erişemez.

ECDH, anahtar Exchange'ya izin veren bir algoritmadır. Genellikle bir protokol tanımlamak için diğer kriptografik yöntemlerle birlikte kullanılır. Örneğin, ECDH, internet taşımacılığı Layer için kullanılan bir şifreleme ve kimlik doğrulama protokolü olan TLS'nin (Taşıma Layer Güvenliği) çekirdeğinde kullanılır. TLS, kalıcı gizlilik sağlamak için anahtarların geçici olduğu bir ECDH çeşidi olan Exchange anahtarı için ECDHE kullanır. ECDHE'ye ek olarak, TLS ayrıca ECDSA gibi bir kimlik doğrulama algoritması, AES gibi bir şifreleme algoritması ve SHA256 gibi bir Hash işlevi kullanır.


TLS, "https "deki "s" harfini ve internet tarayıcınızın sol üst köşesinde gördüğünüz küçük kilit simgesini tanımlar ve şifreli iletişimi garanti eder. Yani, bu makaleyi okuyarak şu anda ECDH kullanıyorsunuz ve muhtemelen farkında olmadan her gün kullanıyorsunuz.


### Bildirim işlemi


Önceki bölümde keşfettiğimiz gibi, ECDH, eliptik bir eğri üzerinde oluşturulan anahtar çiftlerini içeren Diffie-Hellman Exchange'un bir çeşididir. Neyse ki, Bitcoin cüzdanlarımızda bu standardı karşılayan çok sayıda anahtar çiftimiz var!


Buradaki fikir, aralarında paylaşılan ve geçici sırlar oluşturmak için her iki tarafın hiyerarşik deterministik Bitcoin cüzdanlarındaki anahtar çiftlerini kullanmaktır. BIP47'de bunun yerine ECDHE (Eliptik Eğri Diffie-Hellman Geçici) kullanılır.


ECDHE ilk olarak BIP47'de göndericinin ödeme kodunu alıcıya iletmek için kullanılır. Bu ünlü bildirim işlemidir. BIP47'nin kullanılabilmesi için her iki tarafın da (ödeme gönderen gönderici ve ödeme alan alıcı) birbirlerinin ödeme kodundan haberdar olması gerekir. Bu, geçici açık anahtarları ve dolayısıyla tahsis edilmiş alıcı adreslerini türetmek için gereklidir.


Bu Exchange öncesinde, gönderici mantıksal olarak alıcının ödeme kodunu zaten bilmektedir çünkü bu kodu off-chain örneğin web sitesinden veya sosyal medyadan elde etmiş olabilir. Ancak, alıcının göndericinin ödeme kodunu bilmesi gerekmeyebilir. Bu kodun kendilerine iletilmesi gerekmektedir, aksi takdirde geçici anahtarlarını elde edemeyecek ve dolayısıyla bitcoinlerinin nerede olduğunu bilemeyecek ve fonlarının kilidini açamayacaklardır. Başka bir iletişim sistemi kullanılarak off-chain onlara iletilebilir, ancak Wallet'ün seed'ten kurtarılması durumunda bu bir sorun teşkil edecektir.

Aslında, daha önce de belirttiğim gibi, BIP47 adresleri alıcının seed'sinden türetilmez (aksi takdirde, doğrudan xpub'larından birini kullanmak daha iyi olurdu), ancak hem alıcının ödeme kodunu hem de gönderenin ödeme kodunu içeren bir hesaplamanın sonucudur. Bu nedenle, alıcı Wallet'sını kaybeder ve seed'sinden geri almaya çalışırsa, BIP47 aracılığıyla kendisine bitcoin gönderen kişilerin tüm ödeme kodlarına sahip olması gerekecektir.


BIP47'yi bu bildirim işlemi olmadan kullanmak mümkün olabilir, ancak her kullanıcının kendi eşlerinin ödeme kodlarını yedeklemesi gerekecektir. Bu yedekleri oluşturmak, saklamak ve güncellemek için basit ve esnek bir yol bulunana kadar bu durum yönetilemez olmaya devam edecektir. Bu nedenle bildirim işlemi mevcut durumda neredeyse zorunludur.


Adından da anlaşılacağı gibi, ödeme kodlarını yedekleme rolüne ek olarak, bu işlem aynı zamanda alıcıya bir bildirim görevi de görür. Müşterilerine bir tünelin yeni açıldığını bildirir.


Bildirim işleminin teknik işleyişini daha ayrıntılı olarak açıklamadan önce, gizlilik modelinden biraz bahsetmek istiyorum. Gerçekten de BIP47 gizlilik modeli, bu ilk işlemi oluştururken alınan bazı önlemleri haklı çıkarmaktadır.


Ödeme kodunun kendisi doğrudan gizlilik için bir risk oluşturmaz. Özellikle açık anahtarları anonim tutarak kullanıcının kimliği ile işlemler arasındaki bilgi akışını kesmeye izin veren klasik Bitcoin modelinin aksine, ödeme kodu doğrudan bir kimlikle ilişkilendirilebilir. Bu zorunlu değildir, ancak bu bağlantı tehlikeli değildir.


Aslında, ödeme kodu BIP47 ödemelerini almak için kullanılan adresleri doğrudan türetmez. Bunun yerine, adresler her iki tarafın ödeme kodlarının alt anahtarları arasında ECDHE uygulanarak elde edilir.


Bu nedenle, bir ödeme kodu tek başına gizlilik için doğrudan bir risk oluşturmaz, çünkü yalnızca Address bildirimi bundan türetilir. Bundan bazı bilgiler çıkarılabilir, ancak normalde kiminle işlem yaptığınız bilinemez.


Bu nedenle, kullanıcıların ödeme kodları arasında kesin bir ayrımın sürdürülmesi esastır. Bu bağlamda, kodun ilk iletişim adımı ödeme gizliliği için kritik bir andır ve yine de protokolün düzgün işlemesi için zorunludur. Ödeme kodlarından biri herkese açık olarak alınabiliyorsa (örneğin bir web sitesinden), ikinci kod, yani gönderenin kodu, ilk kodla ilişkilendirilmemelidir.


Örneğin, Kanada'daki barışçıl bir protesto hareketine BIP47 ile bağış yapmak istediğimi düşünelim:



- Bu kuruluş ödeme kodunu doğrudan web sitesinde veya sosyal medya platformlarında yayınlamıştır.
- Dolayısıyla bu kod hareketle ilişkilendirilir.
- Bu ödeme kodunu alıyorum.
- Onlara bir işlem göndermeden önce, sosyal ağlarımdan işlem almak için kullandığım için kimliğimle de ilişkili olan kişisel ödeme kodumun farkında olduklarından emin olmalıyım.


Bunu onlara nasıl iletebilirim? Geleneksel iletişim araçlarını kullanarak onlara gönderirsem, bilgi sızabilir ve barışçıl hareketleri destekleyen bir kişi olarak tanımlanabilirim.


Bildirim işlemi, göndericinin ödeme kodunu gizlice iletmek için kesinlikle tek çözüm değildir, ancak şu anda birden fazla güvenlik katmanı uygulayarak bu rolü mükemmel bir şekilde yerine getirmektedir.


Aşağıdaki diyagramda kırmızı çizgiler bilgi akışının kesilmesi gereken anı, siyah oklar ise dışarıdan bir gözlemci tarafından yapılabilecek inkar edilemez bağlantıları temsil etmektedir:


![Privacy model diagram for reusable payment code](assets/15.webp)


Gerçekte, Bitcoin'in klasik gizlilik modeli için, özellikle uzaktan işlemler gerçekleştirirken, anahtar çifti ile kullanıcı arasındaki bilgi akışını tamamen kesmek genellikle zordur. Örneğin, bir bağış kampanyası söz konusu olduğunda, alıcının web sitesinde ya da sosyal medya platformlarında bir Address ya da açık anahtarı ifşa etmesi gerekecektir. BIP47'nin doğru kullanımı, yani bildirim işlemi ile, bu sorunu ECDHE ve üzerinde çalışacağımız şifreleme Layer aracılığıyla çözer.


Açıkçası, Bitcoin'in klasik gizlilik modeli, iki ödeme kodunun ilişkilendirilmesinden türetilen geçici açık anahtarlar düzeyinde hala gözlemlenmektedir. Bu iki model birbirine bağlıdır. Burada sadece, bitcoin almak için klasik açık anahtar kullanımının aksine, ödeme kodunun bir kimlikle ilişkilendirilebileceğini vurgulamak istiyorum çünkü "Bob, Alice ile bir işlem yapıyor" bilgisi başka bir anda bozulmaktadır. Ödeme kodu generate ödeme adresleri için kullanılır, ancak yalnızca Blockchain'ü gözlemleyerek, bir BIP47 ödeme işlemini, onu yapmak için kullanılan ödeme kodlarıyla ilişkilendirmek imkansızdır.


### Bildirim işleminin oluşturulması


Şimdi, bu bildirim işleminin nasıl çalıştığını görelim. Alice'in BIP47 kullanarak Bob'a para göndermek istediğini düşünelim. Örneğimde, Alice gönderici ve Bob alıcı olarak hareket etmektedir. Bob ödeme kodunu web sitesinde zaten yayınlamıştır, bu nedenle Alice zaten Bob'un ödeme kodundan haberdardır.


1- Alice, ECDH ile paylaşılan bir sır hesaplar:



- Ödeme kodundan farklı bir şubede bulunan HD Wallet'den bir çift anahtar seçer. Bu çiftin Alice'ün bildirimi Address veya Alice'ün kimliği ile kolayca ilişkilendirilmemesi gerektiğini unutmayın (önceki bölüme bakın).
- Alice bu çiftten özel anahtarı seçer. Biz buna **a** (küçük harf) diyeceğiz.



- Alice, Bob'nin Address bildirimi ile ilişkili açık anahtarı alır. Bu anahtar Bob'nin ödeme kodundan (indeks 0) türetilen ilk çocuktur. Bu açık anahtarı "B" (büyük harf) olarak adlandıracağız. Bu genel anahtarla ilişkili özel anahtar "b" (küçük harf) olarak adlandırılır. "B", "b" (özel anahtar) ile "G "den (üreteç noktası) eliptik eğri üzerinde nokta ekleme ve iki katına çıkarma yoluyla belirlenir.

**B = b-G**



- Alice, Bob'un açık anahtarı "B "ye kendi özel anahtarı "a "yı uygulayarak nokta toplama ve ikiye katlama yoluyla eliptik eğri üzerinde gizli bir "S" noktası (büyük harf) hesaplar.

**S = a-B**



- Alice ödeme kodunu şifrelemek için kullanılacak körleme faktörü "f "yi hesaplar. Bunu yapmak için HMAC-SHA512 işlevini kullanarak generate'e sözde rastgele bir sayı gönderir. Bu fonksiyona ikinci girdi olarak, sadece Bob'ün alabileceği bir değer kullanır: (x), önceden hesaplanmış gizli noktanın x koordinatıdır. İlk girdi (o), bu işlemin girdisi olarak tüketilen UTXO'dir (çıkış noktası).

**f = HMAC-SHA512(o, x)**


2- Alice kişisel ödeme kodunu taban 2'ye (ikili) dönüştürür.


3- Ödeme kodunun yükü üzerinde simetrik şifreleme yapmak için bu kör edici faktörü bir anahtar olarak kullanır. Kullanılan şifreleme algoritması basitçe XOR'dur. Yapılan işlem "one-time pad" olarak da bilinen Vernam şifrelemesine benzer:



- Alice ilk olarak kör edici faktörünü iki parçaya ayırır: ilk 32 bayt "f1" ve son 32 bayt "f2" olarak adlandırılır. Yani elimizde:

**f = f1 || f2**



- Alice, ödeme kodunun açık anahtarının (x) x-koordinatının şifreli metnini (x') hesaplar ve chain code'sının (c) şifreli metnini (c') ayrı ayrı hesaplar. "f1" ve "f2" şifreleme anahtarları olarak hareket eder ve XOR işlemi kullanılır.

**x' = x XOR f1**

**c' = c XOR f2**



- Alice, ödeme kodundaki açık anahtarın apsisinin (x) ve chain code'in (c) gerçek değerlerini şifrelenmiş (x') ve (c') değerleriyle değiştirir.


Bu bildirim işleminin teknik açıklamasına devam etmeden önce, XOR işlemini tartışmak için bir dakikanızı ayıralım. XOR, Boole cebirine dayanan bitsel bir mantıksal operatördür. İki bit işlenen verildiğinde, karşılık gelen bitler farklıysa 1 döndürür ve karşılık gelen bitler eşitse 0 döndürür. İşte D ve E işlenenlerinin değerlerine dayalı olarak XOR için doğruluk tablosu:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Örneğin:


**0110 XOR 1110 = 1000**


Ya da:


**010011 XOR 110110 = 100101**


ECDH ile XOR'un bir şifreleme Layer olarak kullanılması özellikle uyumludur. İlk olarak, bu operatör sayesinde şifreleme simetriktir. Bu, alıcının şifreleme için kullanılan aynı anahtarla ödeme kodunun şifresini çözmesine olanak tanır. Şifreleme ve şifre çözme anahtarı, ECDH kullanılarak paylaşılan sırdan hesaplanır.


Bu simetri, XOR operatörünün değişebilirlik ve birleşebilirlik özellikleri tarafından sağlanır:



- Diğer özellikler:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Değişkenlik:

D ⊕ E = E ⊕ D



- İlişkisellik:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Simetri:

Eğer: D ⊕ E = L

O zaman: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Ayrıca, bu şifreleme yöntemi, bugüne kadar bilinen koşulsuz (veya mutlak) güvenliğe sahip tek şifreleme algoritması olan Vernam şifresine (One-Time Pad) çok benzemektedir. Vernam şifresinin bu özelliğe sahip olabilmesi için şifreleme anahtarının tamamen rastgele olması, mesajla aynı boyutta olması ve yalnızca bir kez kullanılması gerekir. Burada BIP47 için kullanılan şifreleme yönteminde, anahtar gerçekten de mesajla aynı boyuttadır, kör edici faktör tam olarak açık anahtarın x-koordinatının chain code ödeme koduyla birleştirilmesiyle aynı boyuttadır. Bu şifreleme anahtarı gerçekten de sadece bir kez kullanılır. Ancak, bu anahtar bir HMAC olduğu için mükemmel rastgele bir kaynaktan türetilmemiştir. Daha ziyade sözde rastgeledir. Bu nedenle, bir Vernam şifrelemesi değildir, ancak yöntem benzerdir.


Bildirim işlemi yapımıza geri dönelim:


4- Alice şu anda şifrelenmiş bir yük ile ödeme koduna sahiptir. Girdi olarak açık anahtarı "A "yı, Bob'in bildirimi Address'e bir çıktıyı ve şifrelenmiş yük ile ödeme kodundan oluşan bir OP_RETURN çıktısını içeren bir işlem oluşturacak ve yayınlayacaktır. Bu işlem bildirim işlemidir.


OP_RETURN, bir Bitcoin işlem çıktısını geçersiz olarak işaretleyen bir komut dosyası olan bir Opcode'dur. Günümüzde, Bitcoin Blockchain üzerinde yayın yapmak veya Anchor bilgi vermek için kullanılmaktadır. Zincire kaydedilen ve bu nedenle diğer tüm kullanıcılar tarafından görülebilen 80 bayta kadar veri depolayabilir.


Önceki bölümde gördüğümüz gibi, Diffie-Hellman, potansiyel olarak saldırganlar tarafından gözlemlenen güvensiz bir ağ üzerinden iletişim kuran iki kullanıcı arasında paylaşılan bir sırrı generate için kullanılır. BIP47'de ECDH, doğası gereği birçok saldırgan tarafından gözlemlenen şeffaf bir iletişim ağı olan Bitcoin ağı üzerinde iletişim kurmak için kullanılır. Eliptik eğri üzerindeki Diffie-Hellman anahtarı Exchange aracılığıyla hesaplanan paylaşılan sır daha sonra iletilecek gizli bilgiyi şifrelemek için kullanılır: göndericinin (Alice'ün) ödeme kodu.


İşte BIP47'den alınan ve az önce tarif ettiğimiz şeyi gösteren bir diyagram:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Bu diyagramı daha önce anlattıklarımla eşleştirirsek:



- gW-226'nın tarafındaki "Wallet Priv-Key" aşağıdakilere karşılık gelir: a.
- gW-227'nin tarafındaki "Child Pub-Key 0" şuna karşılık gelir: B.
- "Bildirim Paylaşılan Sırrı" aşağıdakilere karşılık gelir: f.
- "Maskelenmiş Ödeme Kodu" şifrelenmiş ödeme koduna, yani şifrelenmiş ödeme yüküne karşılık gelir: x' ve c'.
- "Bildirim İşlemi" OP_RETURN'i içeren işlemdir.


Bir bildirim işlemi gerçekleştirmek için az önce uyguladığımız adımları tekrarlayalım:



- Alice, Bob'in ödeme kodunu alır ve Address'u bilgilendirir.
- Alice, ilgili anahtar çiftiyle HD Wallet'sinde kendisine ait olan bir UTXO seçer.
- ECDH kullanarak eliptik eğri üzerinde gizli bir nokta hesaplar.
- Bu gizli noktayı, körleştirici faktör olan HMAC'yi hesaplamak için kullanır.
- Bu kör edici faktörü kişisel ödeme kodunun yükünü şifrelemek için kullanır.
- Maskelenmiş ödeme kodunu Bob'ya aktarmak için bir OP_RETURN işlem çıktısı kullanır.


Çalışmasını, özellikle de OP_RETURN'nin kullanımını daha iyi anlamak için gerçek bir bildirim işlemini birlikte inceleyelim. Buraya tıklayarak bulabileceğiniz Testnet üzerinde bu tip bir işlem gerçekleştirdim:


https://Mempool.space/fr/Testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e**


![BIP47 Notification Transaction](assets/17.webp)


Kredi: https://blockstream.info/


Bu işlemi gözlemleyerek, tek bir girişe ve 4 çıkışa sahip olduğunu zaten görebiliriz:



- İlk çıktı, maskelenmiş ödeme kodumu içeren OP_RETURN'dir.
- 546 Sats'ün ikinci çıktısı alıcının Address bildirimine işaret eder.
- Üçüncü çıktı olan 15.000 Sats hizmet ücretini temsil etmektedir, çünkü bu işlemi oluşturmak için Samourai Wallet kullandım.
- İki milyon Sats'den oluşan dördüncü çıktı, değişimi, yani bana ait olan başka bir Address'ye geri dönen girdiden kalan farkı temsil eder.


İncelenmesi en ilginç olanı OP_RETURN kullanılarak elde edilen çıktı 0'dır. Ne içerdiğine daha yakından bakalım:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Kredi: https://blockstream.info/


Çıktının onaltılık kodunu keşfediyoruz: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000**


Bu senaryoda birkaç parçaya ayırabiliriz:

Opcode'lar arasında, OP_RETURN'yi ifade eden 0x6a ve OP_PUSHDATA1'i ifade eden 0x4c'yi tanıyabiliriz. Bu opkodu takip eden bayt, takip eden yükün boyutunu gösterir. Bu, 80 bayt olan 0x50'yi gösterir.


Ardından şifrelenmiş yük ile ödeme kodu gelir.


İşte bu işlemde kullanılan ödeme kodum:


58. tabanda: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU**


16 tabanında (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db**


Ödeme kodumu OP_RETURN ile karşılaştırırsak, HRP'nin (kahverengi) ve sağlama toplamının (pembe) iletilmediğini görebiliriz. Bu bilgiler insanlara yönelik olduğu için bu normaldir.

Daha sonra, (Green'de) sürümü (0x01), bit alanını (0x00) ve açık anahtar paritesini (0x02) tanıyabiliriz. Ve ödeme kodunun sonunda, toplam 80 bayta ulaşmak için dolgu yapılmasına izin veren siyah renkli boş baytlar (0x00). Tüm bu meta veriler düz metin (şifrelenmemiş) olarak iletilir.

Son olarak, açık anahtarın x koordinatının (mavi renkte) ve chain code'ün (kırmızı renkte) şifrelendiğini gözlemleyebiliriz. Bu, ödeme kodunun yükünü oluşturmaktadır.


### Bildirim işleminin alınması.


Şimdi Alice bildirim işlemini Bob'e gönderdiğine göre, bunu nasıl yorumladığını görelim.


Bir hatırlatma olarak, Bob, Alice'nın ödeme koduna erişebilmelidir. Bu bilgi olmadan, bir sonraki bölümde göreceğimiz gibi, Alice tarafından oluşturulan anahtar çiftlerini türetemeyecek ve bu nedenle BIP47 ile alınan bitcoinlerine erişemeyecektir. Şimdilik, Alice'nın ödeme kodu yükü şifrelenmiştir. Bob'nin bunu nasıl çözdüğünü birlikte görelim.


1- Bob, Address bildirimi ile çıktı oluşturan işlemleri izler.

2- Bir işlemin Address bildirimine bir çıktısı olduğunda, Bob bunu BIP47 standardına uygun bir OP_RETURN çıktısı içerip içermediğini görmek için analiz eder.

3- OP_RETURN yükünün ilk baytı 0x01 ise, Bob ECDH ile olası bir paylaşılan sır aramaya başlar:



- Bob işlem girdisindeki açık anahtarı seçer. Yani, Alice'in "A" adlı açık anahtarı ile: **A = a-G**
- Bob, kişisel bildirimi Address ile ilişkili özel anahtar "b "yi seçer: **b**
- Bob, eliptik eğri üzerindeki gizli nokta "S "yi (ECDH paylaşılan sırrı) noktaları toplayıp ikiye katlayarak hesaplar ve kendi özel anahtarı "b "yi Alice'un açık anahtarı "A "ya uygular: **S = b-A**
- Bob, Alice'in ödeme kodu yükünün şifresini çözmesini sağlayacak körleme faktörü "f "yi belirler. Alice'in daha önce hesapladığı şekilde, Bob HMAC-SHA512'yi (x) gizli nokta "S "nin x-koordinat değerine ve (o) UTXO'nin bu bildirim işleminde girdi olarak kullandığı değere uygulayarak "f "yi bulacaktır: **f = HMAC-SHA512(o, x)**


4- Bob, bildirim işleminin OP_RETURN'ündeki verileri bir ödeme kodu olarak yorumlar. "f" körleme faktörünü kullanarak bu potansiyel ödeme kodunun yükünün şifresini çözer.



- Bob kör edici faktör "f "yi iki parçaya ayırır: "f "nin ilk 32 baytı "f1" ve son 32 baytı "f2" olacaktır.
- Bob, Alice'nin ödeme kodu açık anahtarının şifrelenmiş x-koordinat değerinin (x') şifresini çözer:


**x = x' XOR f1**



- Bob, Alice'in ödeme kodunun şifrelenmiş chain code değerinin (c') şifresini çözer:


**c = c' XOR f2**


5- Bob, Alice'nin ödeme kodu açık anahtarının değerinin secp256k1 grubunun bir parçası olup olmadığını kontrol eder. Eğer öyleyse, bunu geçerli bir ödeme kodu olarak yorumlar. Aksi takdirde, işlemi yok sayar.


Artık Bob, Alice'ün ödeme kodunu bildiğine göre, bir daha böyle bir bildirim işlemi yapmasına gerek kalmadan ona 2^32'ye kadar ödeme gönderebilir.


Bu neden işe yarıyor? Bob, Alice ile aynı körleme faktörünü nasıl belirleyebilir ve ödeme kodunun şifresini nasıl çözebilir? Az önce anlattıklarımıza dayanarak ECDH sürecini daha ayrıntılı olarak inceleyelim.


İlk olarak, simetrik şifreleme ile uğraşıyoruz. Bu, şifreleme anahtarının ve şifre çözme anahtarının aynı değer olduğu anlamına gelir. Bu durumda, bildirim işlemindeki anahtar kör edici faktördür (f = f1 || f2). Alice ve Bob'un f için aynı değeri doğrudan iletmeden elde etmesi gerekir, çünkü bir saldırgan bu değeri ele geçirip gizli bilginin şifresini çözebilir.


Bu körleme faktörü iki değere HMAC-SHA512 uygulanarak elde edilir: gizli bir noktanın x koordinatı ve işlem girdisinde tüketilen UTXO. Bu nedenle, Bob'nin Alice'ın ödeme kodu yükünün şifresini çözmek için bu iki bilgiye sahip olması gerekir.


UTXO girişi için, Bob bildirim işlemini gözlemleyerek bunu kolayca alabilir. Gizli nokta için Bob'ün ECDH kullanması gerekecektir.


Diffie-Hellman ile ilgili bölümde görüldüğü gibi, Alice ve Bob kendi açık anahtarlarını değiş tokuş ederek ve özel anahtarlarını gizlice diğerinin açık anahtarına uygulayarak eliptik eğri üzerinde belirli ve gizli bir nokta bulabilirler. Bildirim işlemi bu mekanizmaya dayanır:


Bob'nin anahtar çifti: **B = b-G**


Alice'in anahtar çifti: **A = a-G**


Gizli bir S (x,y) noktası için: **S = a-B = a-b-G = b-a-G = b-A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Artık Bob, Alice'un ödeme kodunu bildiğine göre, BIP47 ödemelerini tespit edebilecek ve alınan bitcoinleri bloke eden özel anahtarları türetebilecektir.

![Bob interprets Alice's notification transaction](assets/20.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Bu diyagramı size daha önce anlattıklarımla eşleştirirsek:



- gW-303'ün tarafındaki "Wallet Pub-Key" aşağıdakilere karşılık gelir: A.
- gW-304'ün tarafındaki "Child Priv-Key 0" şu anlama gelir: b.
- "Bildirim Paylaşılan Sırrı" aşağıdakilere karşılık gelir: f.
- "Maskelenmiş Ödeme Kodu" Alice'in maskelenmiş ödeme koduna, yani şifrelenmiş ödeme yüküne karşılık gelir: x' ve c'.
- "Bildirim İşlemi" OP_RETURN'yı içeren işlemdir.


Bir bildirim işlemini almak ve yorumlamak için az önce birlikte gördüğümüz adımları özetleyeyim:



- Bob, Address bildirimine yönelik işlem çıkışlarını izler.
- Birini tespit ettiğinde, OP_RETURN'da bulunan bilgileri alır.
- Bob giriş açık anahtarını seçer ve ECDH kullanarak bir gizli nokta hesaplar.
- Bu gizli noktayı, körleştirici faktör olan HMAC'yi hesaplamak için kullanır.
- Bu kör edici faktörü Alice'nin OP_RETURN'de bulunan ödeme kodu yükünün şifresini çözmek için kullanır.


### BIP47 ödeme işlemi.


Şimdi BIP47 ile ödeme sürecini inceleyelim. Size durumun mevcut durumunu hatırlatmak için:



- Alice, Bob'ün web sitesinden aldığı ödeme kodundan haberdardır.



- Bob, bildirim işlemi sayesinde Alice'in ödeme kodundan haberdardır.



- Alice, Bob'e bir ilk ödeme yapacaktır. Aynı şekilde çok daha fazlasını yapabilir.


Bu süreci size açıklamadan önce, şu anda hangi endeksler üzerinde çalıştığımızı hatırlatmanın önemli olduğunu düşünüyorum:


Bir ödeme kodunun türetilme yolunu şu şekilde tarif ediyoruz: m/47'/0'/0'/.


Bir sonraki derinlik indeksleri aşağıdaki gibi dağıtır:



- İlk normal (sertleştirilmemiş) çocuk çifti, önceki bölümde tartıştığımız generate bildirimi Address için kullanılır: m/47'/0'/0'/0/.



- Normal alt anahtar çiftleri ECDH içinde generate BIP47 ödeme alıcı adresleri için kullanılır, bu bölümde göreceğimiz gibi: m/47'/0'/0'/ 0'dan 2,147,483,647/'ye kadar.



- Sertleştirilmiş alt anahtar çiftleri geçici ödeme kodlarıdır: m/47'/0'/0'/ 0' ile 2,147,483,647'/ arası.

Alice, Bob'e her ödeme göndermek istediğinde, yine ECDH protokolü sayesinde yeni bir benzersiz boş Address türetir:


- Alice, kişisel yeniden kullanılabilir ödeme kodundan türetilen ilk özel anahtarı seçer: **a**



- Alice, Bob'nin ödeme kodundan türetilen ilk kullanılmayan açık anahtarı seçer. Bu açık anahtara "B" adını vereceğiz. Yalnızca Bob'nin bildiği özel anahtar "b" ile ilişkilidir.

**B = b-G**



- Alice, noktaları toplayıp ikiye katlayarak eliptik eğri üzerinde gizli bir "S" noktası hesaplar ve kendi özel anahtarı "a "yı Bob'un açık anahtarı "B "ye uygular:

**S = a-B**



- Bu gizli noktadan, Alice paylaşılan gizli "s" (küçük harf) değerini hesaplayacaktır. Bunu yapmak için "S" gizli noktasının "Sx" olarak adlandırılan x koordinatını seçer ve bu değeri SHA256 Hash fonksiyonuna aktarır.

**s = SHA256(Sx)**


Güvenmeyin. Doğrulayın! Bir Hash fonksiyonunun temel prensiplerini anlamak istiyorsanız, bu makalede ihtiyacınız olanı bulacaksınız. Ve eğer NIST'e güvenmiyorsanız (haklısınız) ve SHA256'nın nasıl çalıştığını ayrıntılı olarak anlamak istiyorsanız, bu makalede her şeyi Fransızca olarak açıklıyorum.



- Alice, Address'ü alan bir Bitcoin ödemesini hesaplamak için bu paylaşılan sır "s "yi kullanır. İlk olarak, "s "nin secp256k1 eğrisinin sırası içinde olup olmadığını kontrol eder. Değilse, başka bir paylaşılan sır türetmek için Bob'nın açık anahtarının indeksini artırır.



- İkinci olarak, eliptik eğri üzerindeki "B" ve "s-G" noktalarını toplayarak bir açık anahtar "K0" hesaplar. Başka bir deyişle, Alice, Bob'in ödeme kodu "B "den elde edilen açık anahtarı, secp256k1 eğrisinin "G" üreteç noktasından paylaşılan gizli "s" ile noktaları ekleyip ikiye katlayarak eliptik eğri üzerinde hesaplanan başka bir nokta ile ekler. Bu yeni nokta bir açık anahtarı temsil eder ve biz buna "K0" adını veriyoruz:

**K0 = B + s-G**



- Bu açık anahtar "K0" ile Alice, standart bir şekilde boş bir alıcı Address türetebilir (örneğin, Bech32'de SegWit V0).


Alice, Bob'ye ait bu alıcı Address "K0 "a sahip olduğunda, HD Wallet'ünün başka bir dalında kendisine ait bir UTXO seçerek ve bunu Bob'nin "K0" Address'sine harcayarak standart bir Bitcoin işlemi oluşturabilir.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki

Bu diyagramı size daha önce anlattıklarımla eşleştirirsek:



- gW-349'un tarafındaki "Child Priv-Key" aşağıdakilere karşılık gelir: a.
- gW-350'nin yan tarafındaki "Child Pub-Key 0" şuna karşılık gelir: B.
- "Ödeme Sırrı 0" şuna karşılık gelir: s.
- "Payment Pub-Key 0" şu anlama gelir: K0.


BIP47 ödemesi göndermek için az önce birlikte uyguladığımız adımları özetleyeyim:



- Alice kişisel ödeme kodundan ilk türetilmiş çocuk özel anahtarını seçer.
- Bob'nin ödeme kodundan ilk kullanılmamış türetilmiş çocuk açık anahtarından ECDH kullanarak eliptik eğri üzerinde bir gizli nokta hesaplar.
- SHA256 ile paylaşılan bir sırrı hesaplamak için bu gizli noktayı kullanır.
- Bu paylaşılan sırrı eliptik eğri üzerinde yeni bir gizli nokta hesaplamak için kullanır.
- Bu yeni gizli noktayı Bob'ün açık anahtarına ekler.
- Sadece Bob'ün ilişkili özel anahtara sahip olduğu yeni bir geçici açık anahtar elde eder.
- Alice, türetilmiş geçici alıcı Address ile Bob'ye düzenli bir işlem gönderebilir.


İkinci bir ödeme yapmak isterse, yukarıdaki adımları tekrarlar, ancak Bob'un ödeme kodundan türetilen ikinci açık anahtarı seçer. Yani, bir sonraki kullanılmayan anahtarı. Daha sonra Bob'a ait ikinci bir alıcı Address'e sahip olacaktır, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Bu şekilde devam edebilir ve Bob'e ait 2^32'ye kadar boş adres türetebilir.


Dışarıdan bir bakış açısıyla, Bitcoin Blockchain'yi gözlemleyerek, bir BIP47 ödemesini normal bir ödemeden ayırt etmek teorik olarak imkansızdır. Aşağıda Testnet üzerindeki bir BIP47 ödeme işlemi örneği yer almaktadır:


https://blockstream.info/Testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Harcanan bir girdi, 210.000 Sats'lik bir ödeme çıktısı ve bozuk para ile normal bir işlem gibi görünüyor.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Kredi: https://blockstream.info/


### BIP47 ödemesinin alınması ve özel anahtarın türetilmesi.


Alice, Bob'e ait boş bir BIP47 Address'e ilk ödemesini az önce yaptı. Şimdi Bob'in bu ödemeyi nasıl aldığını görelim. Ayrıca Alice'un yeni oluşturduğu Address'in özel anahtarına neden erişemediğini ve Bob'in yeni aldığı bitcoinleri harcamak için bu anahtarı nasıl aldığını göreceğiz.


Bob, Alice'den bildirim işlemini alır almaz, kendisine herhangi bir ödeme göndermeden önce bile BIP47 açık anahtarı "K0 "ı türetir. Bu nedenle ilgili Address'e yapılan herhangi bir ödemeyi gözlemler. Aslında, hemen gözlemleyeceği birkaç adres türetir (K0, K1, K2, K3...). İşte bu açık anahtar "K0 "ı nasıl türetiyor:



- Bob ödeme kodundan türetilen ilk alt özel anahtarı seçer. Bu özel anahtar "b" olarak adlandırılır. Alice'ün önceki adımda kullandığı açık anahtar "B" ile ilişkilidir: **b**



- Bob, ödeme kodundan Alice'nın ilk türetilmiş açık anahtarını seçer. Bu anahtar "A" olarak adlandırılır. Alice'nın hesaplamalarında kullandığı ve yalnızca Alice'nın bildiği özel anahtar "a" ile ilişkilidir. Bob bu işlemi gerçekleştirebilir çünkü Alice'nın bildirim işlemi ile kendisine iletilen ödeme kodunu bilmektedir.

**A = a-G**



- Bob eliptik eğri üzerindeki noktaları toplayıp ikiye katlayarak gizli "S" noktasını hesaplar ve kendi özel anahtarı "b "yi Alice'in açık anahtarı "A "ya uygular. Burada, bu "S" noktasının hem Bob hem de Alice için aynı olacağını garanti eden ECDH'yi kullanıyoruz.

**S = b-A**



- Tıpkı Alice'in yaptığı gibi, Bob de bu "S" noktasının x koordinatını izole eder. Bu değere "Sx" adını verdik. Paylaşılan gizli "s" (küçük harf) değerini bulmak için bu değeri SHA256 fonksiyonundan geçirir.

**s = SHA256(Sx)**



- Alice ile aynı şekilde, Bob eliptik eğri üzerindeki "s-G" noktasını hesaplar. Ardından, bu gizli noktayı kendi açık anahtarı "B "ye ekler. Daha sonra eliptik eğri üzerinde "K0" açık anahtarı olarak yorumladığı yeni bir nokta elde eder:

**K0 = B + s-G**


Bob bu açık anahtar "K0 "a sahip olduğunda, bitcoinlerini harcamak için ilgili özel anahtarı türetebilir. Bu numarayı generate yapabilecek tek kişi odur.



- Bob kendi kişisel ödeme kodundan türetilmiş çocuk özel anahtarı "b "yi ekler. "b" değerini elde edebilecek tek kişi odur. Ardından, K0'ın özel anahtarı olan k0'ı elde etmek için "b "yi paylaşılan gizli "s "ye ekler: **k0 = b + s**



- Eliptik eğrinin grup yasası sayesinde, Bob tam olarak Alice tarafından kullanılan açık anahtara karşılık gelen özel anahtarı elde eder. Öyleyse elimizde: **K0 = k0-G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Bu diyagramı size daha önce anlattıklarımla eşleştirirsek:



- gW-390'ın tarafındaki "Child Priv-Key 0" şuna karşılık gelir: b.



- gW-391'in tarafındaki "Child Pub-Key 0" aşağıdakilere karşılık gelir: A.



- "Ödeme Sırrı 0" şuna karşılık gelir: s.



- "Payment Pub-Key 0" şu anlama gelir: K0.



- "Ödeme Özel Anahtarı 0" şu anlama gelir: k0.


Bir BIP47 ödemesi almak ve ilgili özel anahtarı hesaplamak için az önce birlikte gördüğümüz adımları özetleyeyim:



- Bob kişisel ödeme kodundan ilk türetilen çocuk özel anahtarını seçer.



- Alice'ün chain code'ten ilk türetilen çocuk açık anahtarından ECDH kullanarak eliptik eğri üzerinde bir gizli nokta hesaplar.



- Bu gizli noktayı SHA256 ile paylaşılan bir sırrı hesaplamak için kullanır.



- Bu paylaşılan sırrı eliptik eğri üzerinde yeni bir gizli nokta hesaplamak için kullanır.



- Bu yeni gizli noktayı kişisel açık anahtarına ekler.



- Alice'in ilk ödemesini göndereceği yeni bir geçici açık anahtar elde eder.



- Bob, ödeme kodundan türetilen alt özel anahtarını ve paylaşılan gizli anahtarı ekleyerek bu geçici açık anahtarla ilişkili özel anahtarı hesaplar.


Alice, Bob'un özel anahtarı olan "b "yi elde edemediğinden, Bob'un Address'yi alan BIP47 ile ilişkili özel anahtarı olan k0'ı belirleyemez.


Şematik olarak, paylaşılan sır "S "nin hesaplanmasını aşağıdaki gibi gösterebiliriz:


![Calculation of the shared secret with ECDHE](assets/25.webp)


Paylaşılan sır ECDH ile bulunduğunda, Alice ve Bob BIP47 ödeme açık anahtarı "K0 "ı hesaplar ve Bob de ilişkili özel anahtar "k0 "ı hesaplar:


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### BIP47 ödemesinin geri ödenmesi.


Bob, Alice'nin yeniden kullanılabilir ödeme kodunu bildiğinden, ona para iadesi göndermek için gerekli tüm bilgilere zaten sahiptir. Herhangi bir bilgi istemek için Alice ile iletişime geçmesi gerekmeyecektir. Özellikle seed ile BIP47 adreslerini kurtarabilmesi için onu bir bildirim işlemi ile bilgilendirecek ve ardından ona 2^32'ye kadar ödeme gönderebilecektir.

Bob daha sonra Alice'e gönderdiği ödemeleri aynı şekilde geri ödeyebilir. Roller tersine döndü:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Kredi: Hiyerarşik Deterministik Cüzdanlar için Yeniden Kullanılabilir Ödeme Kodları, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Artık BIP47'nin temsil ettiği bu muhteşem çözümün tüm ayrıntılarını biliyorsunuz.


## PayNym'in türetilmiş kullanımları.


Bu BIP47'nin Samourai Wallet üzerinde uygulanması, kullanıcıların ödeme kodlarından hesaplanan tanımlayıcılar olan PayNyms ile sonuçlanmıştır. Günümüzde bu tanımlayıcıların faydası BIP47 kullanımının çok ötesine geçmiştir.


Samourai ekibi yavaş yavaş kullanıcının PayNym'ine dayalı bir araç ve hizmet ekosistemi geliştiriyor. Bunlar arasında, bir işleme entropi ekleyerek ve böylece makul inkar edilebilirlik ekleyerek kullanıcının gizliliğini optimize etmeye izin veren tüm harcama araçları açıkça vardır.


Tor tabanlı şifreli iletişim ağı Soroban ve PayNyms'in birlikte kullanımı, iyi bir güvenlik seviyesini korurken, ortak işlemler oluştururken kullanıcı deneyimini büyük ölçüde optimize etmiştir. Böylece, Stowaway (PayJoin) ve StonewallX2 işlemlerini, böyle bir ortak işlem oluşturmak için gereken çok sayıda imzasız işlem alışverişini manuel olarak gerçekleştirmeden gerçekleştirmek kolaydır.


BIP47 kullanımından farklı olarak, bu işbirlikçi işlemler bir bildirim işlemi gerektirmediğinden, bu araçları kullanmak için PayNym'leri bağlamak yeterlidir. Bunları bağlamaya gerek yoktur.


İşbirliğine dayalı işlemler ve daha geniş anlamda Samourai Wallet'un tüm harcama araçları hakkında daha fazla bilgi edinmek istiyorsanız, bu makaledeki "Harcama Araçları" bölümünü okuyabilirsiniz. Her araç için teknik bir açıklama ve ayrıntılı bir öğretici bulacaksınız.


Bu işbirlikçi işlemlere ek olarak, son zamanlarda Samourai ekibinin PayNym ile bağlantılı bir kimlik doğrulama protokolü üzerinde çalıştığı gözlemlenmiştir: Auth47. Bu araç halihazırda uygulanmakta ve örneğin bu yöntemi kabul eden bir web sitesinde PayNym ile kimlik doğrulamasına izin vermektedir. Gelecekte, web üzerinde bu kimlik doğrulama olasılığının ötesinde, Auth47'nin BIP47/PayNym/Samourai ekosistemi etrafında daha büyük bir projenin parçası olacağını düşünüyorum. Belki de bu protokol, özellikle harcama araçlarının kullanımında Samourai Wallet'in kullanıcı deneyimini daha da optimize etmek için kullanılacaktır. Bunu zaman gösterecek...


## BIP47 hakkındaki kişisel görüşüm.


Açıkçası, BIP47'nin ana dezavantajı bildirim işlemidir. Kullanıcının Mining için ücret harcamasına neden olur, bu da bazıları için can sıkıcı olabilir. Ancak, Bitcoin Blockchain üzerindeki "spam" argümanı kesinlikle kabul edilemez. İşlemleri için ücret ödeyen herkes, amacı ne olursa olsun bunu Ledger'e kaydedebilmelidir. Aksini iddia etmek sansürü savunmaktır.


Gelecekte, göndericinin ödeme kodunu alıcıya iletmek ve alıcının bunu güvenli bir şekilde saklaması için daha az maliyetli başka çözümler bulunması mümkündür. Ancak şimdilik, bildirim işlemi en az taviz veren çözüm olmaya devam ediyor.


BIP47'nin tüm faydaları göz önünde bulundurulduğunda bu dezavantaj ihmal edilebilir düzeyde kalmaktadır. Bu Address yeniden kullanım sorununu çözmek için mevcut tüm öneriler arasında bana en iyi çözüm olarak görünüyor.


Daha önce de açıklandığı üzere, Address'nin yeniden kullanımının büyük bir kısmı borsalardan kaynaklanmaktadır. BIP47 bu sorunu kaynağında çözen tek makul çözümdür. Address tekrar kullanımlarının sayısını azaltmayı amaçlayan herhangi bir öneri bu konuya odaklanmalı ve çözümü sorunun ana kaynağına uyarlamalıdır.


Kullanılabilirlik açısından, iç işleyişi oldukça karmaşık olmasına rağmen, BIP47 ödeme prosedürü basittir. Bu nedenle yeniden kullanılabilir ödeme kodları acemi kullanıcılar tarafından bile kolayca benimsenebilir.


Gizlilik açısından BIP47 çok ilginçtir. Bildirim işlemiyle ilgili bölümde açıkladığım gibi, ödeme kodu türetilen geçici adresler hakkında herhangi bir bilgi vermez. Bu nedenle, alıcı Address'in geleneksel kullanımından farklı olarak, Bitcoin işlemi ile alıcının tanımlayıcısı arasındaki bilgi akışını keser.


Ve hepsinden önemlisi, BIP47'nin PayNym uygulaması çalışıyor! 2016'dan beri Samourai Wallet'de ve bu yılın başından beri Sparrow wallet'de mevcut. Bu bilimsel bir proje değil, dün test edilmiş ve bugün tamamen işlevsel olan bir çözümdür.


Umarım gelecekte bu yeniden kullanılabilir ödeme kodları ekosistem aktörleri tarafından benimsenir, Wallet yazılımında uygulanır ve Bitcoin kullanıcıları tarafından kullanılır.


Bitcoin'ün CA'ların oyun alanı ve hükümetlerin gözetim aracı haline gelmemesi için kullanıcı gizliliğine yönelik gerçekten olumlu herhangi bir çözüm tartışılmalı, zorlanmalı ve savunulmalıdır.

Her yerde nasıl zulüm gördüğünü ve hakarete uğradığını düşündü ve şimdi herkesin onun tüm bu güzel kuşların en güzeli olduğunu söylediğini duydu! Mürver bile dallarını ona doğru eğdi ve güneş öyle sıcak ve yardımsever bir ışık yaydı ki! Sonra tüyleri kabardı, ince boynu dikleşti ve tüm kalbiyle haykırdı, "Küçük çirkin bir ördek yavrusuyken bu kadar mutluluğu nasıl hayal edebilirdim?"


## Daha ileri gitmek için:



- CoinJoin'ü Bitcoin üzerinde anlama ve kullanma.



- Bir Bitcoin Wallet'nin türetme yollarının anlaşılması.



- RoninDojo Bitcoin düğümünüzü kurma ve kullanma.


### Dış kaynaklar ve teşekkür:


LaurentMT ve Théo Pantamis'e bana açıkladıkları ve bu makalede kullandığım sayısız kavram için teşekkür ederim. Umarım bunları doğru bir şekilde aktarabilmişimdir.


Bu metnin redaksiyonu ve uzman tavsiyeleri için Fanis Michalakis'e teşekkür ederiz.



- https://bitcoiner.guide/paynym/
- https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols