---
name: COLDCARD Q
description: COLDCARD Q'nun ayarlanması ve kullanılması
---
![cover](assets/cover.webp)


Bir Hardware Wallet, bir Bitcoin Wallet'nin özel anahtarlarını yönetmeye ve güvence altına almaya adanmış elektronik bir cihazdır. Genellikle internete bağlı genel amaçlı makinelere kurulan yazılım cüzdanlarının (veya Hot cüzdanlarının) aksine, donanım cüzdanları özel anahtarların fiziksel olarak izole edilmesini sağlayarak korsanlık ve hırsızlık riskini azaltır.


Bir Hardware Wallet'ün temel amacı, saldırı yüzeyini en aza indirmek için cihazın işlevselliğini mümkün olduğunca azaltmaktır. Daha az saldırı yüzeyi aynı zamanda daha az potansiyel saldırı vektörü, yani saldırganların bitcoinlere erişmek için sistemde yararlanabileceği daha az zayıf nokta anlamına gelir.


Özellikle mutlak değer olarak ya da toplam varlıklarınızın bir oranı olarak büyük miktarlara sahipseniz, bitcoinlerinizi güvence altına almak için bir Hardware Wallet kullanmanız tavsiye edilir.


Donanım cüzdanları, bir bilgisayar veya akıllı telefondaki Wallet yönetim yazılımı ile birlikte kullanılır. İkincisi işlemlerin oluşturulmasını yönetir, ancak bu işlemleri geçerli kılmak için gereken kriptografik imza yalnızca Hardware Wallet içinde gerçekleştirilir. Bu, özel anahtarların hiçbir zaman potansiyel olarak savunmasız bir ortama maruz kalmadığı anlamına gelir.


Donanım cüzdanları kullanıcı için çifte koruma sunar: bir yandan özel anahtarları çevrimdışı tutarak bitcoinlerinizi uzaktan saldırılara karşı korurlar, diğer yandan da genellikle anahtarları çıkarma girişimlerine karşı daha fazla fiziksel direnç sunarlar. İşte tam da bu 2 güvenlik kriterine göre piyasadaki farklı modelleri değerlendirebilir ve sınıflandırabiliriz.


Bu eğitimde size böyle bir çözümü tanıtmak istiyorum: **COLDCARD Q**.


---
COLDCARD Q çok sayıda işlev sunduğundan, kullanımını 2 derse bölmeyi öneriyorum. Bu ilk eğitimde, cihazın ilk yapılandırmasına ve temel işlevlerine bakacağız. Daha sonra, ikinci bir eğitimde, COLDCARD'ınızın tüm gelişmiş seçeneklerinden nasıl yararlanacağınıza bakacağız.


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## COLDCARD Q ile tanışın


COLDCARD Q, önceki MK modelleriyle tanınan Kanadalı Coinkite şirketi tarafından geliştirilen, yalnızca Bitcoin'a özel bir Hardware Wallet'dir. Q, bugüne kadarki en gelişmiş ürünlerini temsil eder ve nihai Bitcoin Hardware Wallet olarak konumlandırılmıştır.


Donanım açısından COLDCARD Q, optimum bir kullanıcı deneyimi için gereken tüm özelliklerle donatılmıştır:




- Geniş LCD ekran, navigasyonu ve kullanımı kolaylaştırır;
- Tam QWERTY klavye;
- QR kodlarını taramak için entegre kamera;
- İki microSD kart yuvası ;
- Üç adet AAA pil (dahil değildir) veya bir USB-C kablosu aracılığıyla tamamen izole edilmiş bir güç seçeneği;
- Daha fazla güvenlik için iki farklı üreticiden iki Secure Elements;
- NFC aracılığıyla iletişim kurma yeteneği.


Bana göre COLDCARD Q'nun sadece iki dezavantajı var. Birincisi, birçok özelliği nedeniyle oldukça hantal, neredeyse 13 cm uzunluğunda ve 8 cm genişliğinde, yani neredeyse küçük bir akıllı telefon boyutunda. Ayrıca pil bölmesi nedeniyle oldukça kalın. Eğer daha küçük, daha mobil bir Hardware Wallet arıyorsanız, çok daha kompakt olan MK4 daha iyi bir seçenek olabilir. İkinci dezavantajı ise, resmi web sitesinde **$239.99** olarak fiyatlandırılan, yani MK4'ten $72 daha fazla olan ve Q'yu Ledger Flex veya Foundation's Passport gibi premium donanım cüzdanlarıyla doğrudan rekabete sokan cihazın maliyetidir.


![CCQ](assets/fr/001.webp)


Yazılım tarafında ise COLDCARD Q, Coinkite'ın diğer cihazları gibi bir dizi gelişmiş özellik ile donatılmıştır:




- Kendi kurtarma cümlenizi generate için Zar Atın ;
- PIN kodu ;
- Son PIN kilidi için geri sayım ;
- BIP39 passphrase ;
- Son kilitleme PIN'i ;
- Bağlantı geri sayımı ;
- SeedXOR;
- BIP85...


Kısacası, COLDCARD Q, MK4'e göre gelişmiş bir kullanıcı deneyimi sunuyor ve daha fazla kullanım kolaylığı arayan orta ve ileri düzey kullanıcılar için ideal olabilir.


COLDCARD Q [resmi Coinkite web sitesinde] (https://store.coinkite.com/store/coldcard) satışa sunulmuştur. Ayrıca bir perakendeciden de satın alınabilir.


## Eğitimin hazırlanması


COLDCARD'ınızı aldıktan sonra ilk adım, açılmadığından emin olmak için ambalajı incelemektir. Ambalaj hasarlıysa, bu Hardware Wallet'in tehlikeye atıldığını ve orijinal olmayabileceğini gösterebilir.


![CCQ](assets/fr/002.webp)


Kutuyu açtığınızda aşağıdaki öğeleri bulmanız gerekir:




- COLDCARD Q mühürlü bir torba içinde;
- Mnemonic cümlenizi kaydetmek için bir kart.


![CCQ](assets/fr/003.webp)


Torbanın mühürünün açılmadığından veya hasar görmediğinden emin olun. Ayrıca çantanızın üzerindeki numaranın çantanın içindeki kağıttaki numarayla aynı olup olmadığını kontrol edin. Bu numarayı ileride başvurmak üzere saklayın.


![CCQ](assets/fr/004.webp)


COLDCARD'ınızı bilgisayara bağlamadan (hava boşluğu) çalıştırmayı tercih ediyorsanız, cihazın arkasına üç adet AAA pil takın. Alternatif olarak, bir USB-C kablosuyla bilgisayarınıza bağlayabilirsiniz.


![CCQ](assets/fr/005.webp)


Bu eğitim için, bilgisayarınızdaki Bitcoin Wallet'unuzu yönetmek için Sparrow wallet'ye de ihtiyacınız olacak. Resmi web sitesinden [Sparrow wallet](https://sparrowwallet.com/download/) dosyasını indirin. Kuruluma devam etmeden önce hem gerçekliğini (GnuPG ile) hem de bütünlüğünü (Hash ile) kontrol etmenizi şiddetle tavsiye ederim. Bunu nasıl yapacağınızı bilmiyorsanız, bu öğreticiyi izleyin:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## PIN kodu seçimi


Şimdi sol üst köşedeki düğmeye basarak COLDCARD'ınızı açabilirsiniz.


![CCQ](assets/fr/006.webp)


Kullanım koşullarını kabul etmek için "*ENTER*" düğmesine basın.


![CCQ](assets/fr/007.webp)


COLDCARD Q cihazınız daha sonra ekranın üst kısmında bir numara gösterecektir. Bu numaranın mühürlü poşetin ve poşetin içindeki plastik parçanın üzerindeki numarayla eşleştiğinden emin olun. Bu, paketinizin Coinkite tarafından paketlendiği zaman ile sizin onu açtığınız zaman arasında açılmamış olmasını sağlar. Devam etmek için "*ENTER*" tuşuna basın.


![CCQ](assets/fr/008.webp)


"*Choose PIN Code*" menüsüne gidin ve "*ENTER*" tuşu ile onaylayın.


![CCQ](assets/fr/009.webp)


Bu PIN kodu COLDCARD'ınızın kilidini açmak için kullanılır. Bu nedenle yetkisiz fiziksel erişime karşı bir korumadır. Bu PIN kodu, Wallet'nizin kriptografik anahtarlarının türetilmesinde yer almaz. Dolayısıyla, bu PIN koduna erişiminiz olmasa bile, Mnemonic ifadenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.


COLDCARD PIN kodları iki bölüme ayrılır: bir önek ve bir sonek, her biri 2 ila 6 hane arasında, toplam 4 ila 12 hane içerebilir. COLDCARD'ınızın kilidini açtığınızda, önce öneki girmeniz gerekir, ardından cihaz size 2 kelime gösterecektir. Ardından son eki girin. Bu iki kelime size bu yapılandırma adımı sırasında verilecektir ve COLDCARD'ınızın kilidini her açtığınızda ihtiyacınız olacağından dikkatlice kaydedilmelidir. Kilit açma sırasında görüntülenen iki kelime yapılandırma sırasında kaydettiklerinizle eşleşirse, bu, cihazınızın son kullanımından bu yana tehlikeye atılmadığını doğrulayacaktır.


"*PIN Seçiniz*" üzerine tekrar tıklayın


![CCQ](assets/fr/010.webp)


Uyarıları okuduğunuzu onaylayın.


![CCQ](assets/fr/011.webp)


Şimdi PIN kodunuzu seçeceksiniz. Uzun, rastgele bir PIN kodu öneririz. Bu kodu COLDCARD'ınızın saklandığı yerden farklı bir yerde sakladığınızdan emin olun. Bu kodu kaydetmek için paketinizde verilen kartı kullanabilirsiniz.


Seçtiğiniz öneki girin, ardından PIN kodunun ilk kısmını onaylamak için "*ENTER*" düğmesine basın.


![CCQ](assets/fr/012.webp)


Daha sonra iki kimlik avı önleme kelimesi ekranınızda görüntülenecektir. İleride başvurmak için bunları dikkatlice kaydedin. Bunları yazmak için paketinizde bulunan kartı kullanabilirsiniz.


![CCQ](assets/fr/013.webp)


Ardından PIN kodunuzun ikinci kısmını girin ve "*ENTER*" tuşuna basın.


![CCQ](assets/fr/014.webp)


PIN kodunuzu ikinci kez girerek onaylayın ve iki kimlik avı önleme kelimesinin daha önce kaydettiklerinizle eşleşip eşleşmediğini kontrol edin.


![CCQ](assets/fr/015.webp)


Şu andan itibaren, COLDCARD'ınızın kilidini her açtığınızda, PIN kodu önekinizi girdikten sonra ekranda görünen iki kimlik avı önleyici kelimenin geçerliliğini kontrol etmeyi unutmayın.


## Ürün yazılımı güncellemesi


Cihazınızı ilk kez kullanırken, aygıt yazılımını kontrol etmeniz ve güncellemeniz önemlidir. Bunu yapmak için "*Gelişmiş/Araçlar*" menüsüne erişin.


![CCQ](assets/fr/016.webp)


**Önemli:** Aygıt yazılımınızı yükseltmeyi planlıyorsanız ve bu COLDCARD'ı ilk kez kullanmıyorsanız (yani COLDCARD'da oluşturulmuş bir Wallet'iniz varsa), Mnemonic ifadenizin olduğundan ve işlevsel olduğundan emin olun (varsa isteğe bağlı passphrase'ün yanı sıra). Bu, cihaz güncellemesi sırasında bir sorun olması durumunda bitcoinlerinizi kaybetmemek için önemlidir.


"*Ürün Yazılımını Yükselt*" öğesini seçin.


![CCQ](assets/fr/017.webp)


"*Sürümü Göster*" öğesini seçin.


![CCQ](assets/fr/018.webp)


COLDCARD'ınızın mevcut aygıt yazılımı sürümünü kontrol edebilirsiniz. Örneğin, benim durumumda sürüm "*1.2.3Q*".


![CCQ](assets/fr/019.webp)


Daha yeni bir sürümün mevcut olup olmadığını görmek için [resmi COLDCARD web sitesinde] (https://coldcard.com/downloads) kontrol edin. Yeni aygıt yazılımını indirmek için "*İndir*" üzerine tıklayın.


![CCQ](assets/fr/020.webp)


Bu noktada, indirilen ürün yazılımının bütünlüğünü ve gerçekliğini kontrol etmenizi şiddetle tavsiye ederiz. Bunu yapmak için, [geliştiriciler tarafından imzalanmış tüm sürümlerin karmalarını içeren belgeyi](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt) indirin, imzayı [geliştiricinin ortak anahtarı](https://keybase.io/dochex) ile doğrulayın ve imzalı belgede belirtilen Hash'nın siteden indirilen ürün yazılımıyla eşleştiğinden emin olun. Her şey doğruysa, güncellemeye devam edebilirsiniz.


Bu doğrulama sürecine aşina değilseniz, bu öğreticiyi izlemenizi tavsiye ederim:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Bir microSD kart alın ve aygıt yazılımı dosyasını (belge `.dfu` olarak) buna aktarın. MicroSD kartı COLDCARD'ınızın bağlantı noktalarından birine takın.


![CCQ](assets/fr/021.webp)


Ardından, aygıt yazılımı güncelleme menüsünde "*MicroSD'den*" öğesini seçin.


![CCQ](assets/fr/022.webp)


Aygıt yazılımına karşılık gelen dosyayı seçin.


![CCQ](assets/fr/023.webp)


"*ENTER*" düğmesine basarak seçiminizi onaylayın.


![CCQ](assets/fr/024.webp)


Aygıt yazılımı güncellenirken lütfen bekleyin.


![CCQ](assets/fr/025.webp)


Güncelleme tamamlandığında, cihazın kilidini açmak için PIN kodunuzu girin.


![CCQ](assets/fr/026.webp)


Aygıt yazılımınız artık güncel.


## COLDCARD Q parametreleri


Dilerseniz, "*Ayarlar*" menüsüne erişerek COLDCARD'ınızın ayarlarını keşfedebilirsiniz.


![CCQ](assets/fr/027.webp)


Bu menüde, ekran parlaklığını ayarlama veya varsayılan ölçü birimini seçme gibi çeşitli özelleştirme seçenekleri bulacaksınız.


![CCQ](assets/fr/028.webp)


Diğer gelişmiş ayarlara bir sonraki eğitimde bakacağız:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Bitcoin Wallet Oluşturma


Şimdi yeni bir generate Bitcoin Wallet oluşturma zamanı! Bunu yapmak için bir Mnemonic cümlesi oluşturmanız gerekir. Coldcard'da bu ifadeyi oluşturmak için üç yönteminiz vardır:




- Yalnızca dahili rastgele sayı üretecini (TRNG) kullanın;
- Entropi eklemek için TRNG ve zar atmanın bir kombinasyonunu kullanın;
- Sadece zar atmayı kullanın.


**Yeni başlayanlar ve orta düzey kullanıcılar için sadece COLDCARD'ın dahili rastgele sayı üretecini kullanmanızı öneririz**


Sadece zar seçeneğini önermiyorum, çünkü kötü uygulama yetersiz entropiye sahip bir cümleye yol açabilir ve Wallet'ünüzün güvenliğini tehlikeye atabilir.


Bununla birlikte, en iyi seçenek kesinlikle TRNG kullanımını harici bir entropi kaynağı ile birleştiren ikinci seçenektir. Bu yöntem, tek başına TRNG'ninkine eşdeğer bir minimum entropiyi garanti eder ve dahili jeneratörün olası bir arızası durumunda (gönüllü olsun ya da olmasın) ekstra bir güvenlik seviyesi ekler. TRNG ve zar atmayı birleştiren bu seçeneği seçerek, sizin açınızdan kötü bir uygulama durumunda riskleri artırmadan cümlenin oluşturulması üzerinde daha fazla kontrol sahibi olursunuz.


"*Yeni seed Kelimeler*" üzerine tıklayın.


![CCQ](assets/fr/029.webp)


Cümlenizin uzunluğunu seçebilirsiniz. Yönetmesi daha az karmaşık olduğu ve 24 kelimelik bir cümleden daha az Wallet güvenliği sunmadığı için 12 kelimelik bir cümleyi tercih etmenizi öneririm.


![CCQ](assets/fr/030.webp)


COLDCARD daha sonra TRNG tarafından oluşturulan kurtarma cümlenizi görüntüleyecektir. Ek harici entropi eklemek isterseniz, "*4*" tuşuna basın.


![CCQ](assets/fr/031.webp)


Bu sizi zar atarak entropi ekleyebileceğiniz bir sayfaya götürecektir. Mümkün olduğunca çok atış yapın (en az 50 önerilir, ancak TRNG'nin entropisinden zaten yararlandığınız için daha azı önemli değildir) ve sonuçları "*1*" ila "*6*" tuşlarıyla kaydedin. Bitirdiğinizde, onaylamak için "*ENTER*" tuşuna basın.


![CCQ](assets/fr/032.webp)


Az önce sağladığınız entropiye ve TRNG'ninkine dayalı olarak yeni bir Mnemonic ifadesi görüntülenecektir.


**Uyarı: Bu Mnemonic tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu ifadeye sahip olan herkes, COLDCARD'ınıza fiziksel erişimi olmasa bile fonlarınızı çalabilir. 12 kelimelik ifade, COLDCARD'ınızın kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde saklamak ve güvenli bir yerde saklamak çok önemlidir.


COLDCARD'ınızla birlikte verilen kartona yazabilir veya daha fazla güvenlik için, yangın, sel veya çökme riskinden korumak için paslanmaz çelik bir destek üzerine kazımanızı tavsiye ederim. Her durumda, asla dijital bir ortama kaydetmeyin, aksi takdirde bitcoinlerinizi kaybedebilirsiniz.


Ekranda verilen kelimeleri seçtiğiniz fiziksel ortama yazın. Güvenlik stratejinize bağlı olarak, cümlenin birkaç tam fiziksel kopyasını çıkarmayı düşünebilirsiniz (ancak her şeyden önce, bölmeyin). Kelimelerin numaralandırılmış ve sıralı olması önemlidir.


Açıkçası, bu öğreticinin aksine, **bu kelimeleri asla internette paylaşmamalısınız**. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.


Kelimeleri yazdıktan sonra "*ENTER*" tuşuna basın.


![CCQ](assets/fr/033.webp)


İfadenizi doğru kaydettiğinizden emin olmak için sistem sizden belirli kelimeleri onaylamanızı isteyecektir. Tuş takımında her kelimeye karşılık gelen numarayı seçin.


![CCQ](assets/fr/034.webp)


Wallet'ınız şimdi oluşturuldu! Ekranın sağ üst köşesinde ana özel anahtar parmak izinizi görebilirsiniz. "*ENTER*" tuşuna basın.


![CCQ](assets/fr/035.webp)


Şimdi COLDCARD'ınızın ana menüsüne erişirsiniz.


![CCQ](assets/fr/036.webp)


## Sparrow üzerinde yeni bir Wallet kurulumu


Sparrow wallet yazılımı ile COLDCARD'ınız arasında iletişim kurmak için birkaç seçenek vardır. En basit olanı bir USB-C kablosu kullanmaktır. Ancak, varsayılan olarak COLDCARD'ınızda kablo ve NFC iletişimi devre dışıdır. Bunları yeniden etkinleştirmek için "*Ayarlar*", ardından "*Donanım Açık/Kapalı*" bölümüne gidin ve istediğiniz iletişim seçeneğini etkinleştirin.


![CCQ](assets/fr/037.webp)


COLDCARD'ınızı bilgisayarınızdan tamamen izole tutmayı tercih ediyorsanız, QR kodları veya bir microSD kart kullanarak dolaylı "hava boşluğu" iletişimini tercih edebilirsiniz. Bu eğitimde kullanacağımız yöntem budur.


"*Gelişmiş/Araçlar*" bölümüne gidin.


![CCQ](assets/fr/038.webp)


"*Export Wallet*" öğesini seçin.


![CCQ](assets/fr/039.webp)


Ardından "*Sparrow wallet*" öğesini seçin.


![CCQ](assets/fr/040.webp)


Yapılandırma dosyasını generate yapmak için "*ENTER*" tuşuna basın.


![CCQ](assets/fr/041.webp)


Ardından bu dosyanın Sparrow'ye nasıl gönderileceğini seçin. Bu örnekte, "*A*" yuvasına bir microSD yerleştirdim, bu yüzden "*1*" düğmesini seçeceğim. Ayrıca "*QR*" düğmesine basarak COLDCARD ekranınızda bilgileri bir QR kodu olarak görüntüleyebilir ve bu QR kodunu bilgisayarınızın web kamerasıyla tarayabilirsiniz.


![CCQ](assets/fr/042.webp)


Sparrow wallet'i başlatın ve ana ekrana ulaşmak için giriş sayfalarını atlayın. Ekranın sağ alt köşesindeki anahtarı kontrol ederek bir düğüme doğru şekilde bağlandığınızdan emin olun.


![CCQ](assets/fr/043.webp)


Kendi Bitcoin düğümünüzü kullanmanız şiddetle tavsiye edilir. Bu eğitim için, Testnet'de olduğum için genel bir düğüm (sarı) kullanıyorum, ancak üretim kullanımı için yerel olarak Bitcoin core (Green) veya uzak bir düğümde (mavi) bir Electrum sunucusu kullanmak en iyisidir.


"*Dosya*" menüsüne erişin ve "*Yeni Wallet*" öğesini seçin.


![CCQ](assets/fr/044.webp)


Wallet'ünüze bir isim verin ve "*Wallet* Oluştur "a tıklayın.


![CCQ](assets/fr/045.webp)


"*Script Type*" açılır menüsünde, bitcoinlerinizi güvence altına alacak script türünü seçin.


![CCQ](assets/fr/046.webp)


"*Havalandırılmış Hardware Wallet*" üzerine tıklayın.


![CCQ](assets/fr/047.webp)


"*Coldcard*" sekmesi altında, COLDCARD'ınızda görüntülenen QR kodunu taramayı planlıyorsanız "*Tara...*" seçeneğine veya microSD'den dosyayı içe aktarmak için "*Dosya İçe Aktar...*" seçeneğine tıklayın (bu `.json` dosyasıdır).


![CCQ](assets/fr/048.webp)


İçe aktardıktan sonra, Sparrow'da görüntülenen "*Ana parmak izinin*" COLDCARD'ınızda görüntülenenle eşleşip eşleşmediğini kontrol edin. "*Uygula*" düğmesine tıklayarak oluşturma işlemini onaylayın.


![CCQ](assets/fr/049.webp)


Sparrow wallet'nize erişimi güvence altına almak için güçlü bir parola oluşturun. Bu parola genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi yetkisiz erişime karşı koruyacaktır.


Unutmamak için bu parolayı kaydetmek iyi bir fikirdir (örneğin bir parola yöneticisinde).


![CCQ](assets/fr/050.webp)


Wallet'unuz artık Sparrow wallet'e ayarlanmıştır.


![CCQ](assets/fr/051.webp)


Wallet'ınıza ilk bitcoinlerinizi almadan önce, **Boş bir kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız gibi bazı referans bilgilerini yazın, ardından Wallet hala boşken COLDCARD Q'nuzu sıfırlayın. Ardından kağıt yedeklerinizi kullanarak Wallet'ınızı COLDCARD'a geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan xpub'ın başlangıçta yazdığınızla eşleşip eşleşmediğini kontrol edin. Eğer eşleşiyorsa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime başvurmanızı öneririm:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoin alma


İlk bitcoinlerinizi almak için, COLDCARD'ınızı açarak ve kilidini açarak başlayın.


![CCQ](assets/fr/052.webp)


Sparrow wallet'de "*Alma*" sekmesine tıklayın.


![CCQ](assets/fr/053.webp)


Sparrow wallet tarafından önerilen Address'ü kullanmadan önce COLDCARD ekranınızda kontrol edin. Bu uygulama, Sparrow'te görüntülenen Address'ün sahte olmadığını ve Hardware Wallet'nin daha sonra bu Address ile güvence altına alınan bitcoinleri harcamak için gereken özel anahtara gerçekten sahip olduğunu doğrulamanızı sağlar. Bu, çeşitli saldırı türlerinden kaçınmanıza yardımcı olur.


Bu kontrolü gerçekleştirmek için COLDCARD üzerindeki "*Address Explorer*" menüsüne tıklayın.


![CCQ](assets/fr/054.webp)


Sparrow üzerinde kullandığınız komut dosyası türünü seçin. Benim durumumda, bu SegWit P2WPKH. Üzerine tıklıyorum.


![CCQ](assets/fr/055.webp)


Daha sonra farklı türetilmiş adreslerinizi sırayla görebilirsiniz.


![CCQ](assets/fr/056.webp)


Address'in eşleşip eşleşmediğini Sparrow ile kontrol edin. Benim durumumda, `m/84'/1'/0'/0/0` türetme yoluna sahip Address gerçekten de hem Sparrow hem de COLDCARD üzerinde `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr`.


![CCQ](assets/fr/057.webp)


Bu Address'ün Ownership'sini doğrulamanın bir başka yolu da QR kodunu COLDCARD'ınızdan doğrudan Sparrow'e taramaktır. COLDCARD ana ekranınızdan "*Herhangi Bir QR Kodunu Tara*" seçeneğini seçin. Klavyedeki "*QR*" tuşunu da kullanabilirsiniz.


![CCQ](assets/fr/058.webp)


Sparrow wallet üzerinde görüntülenen Address'nın QR kodunu tarayın.


![CCQ](assets/fr/059.webp)


COLDCARD'ınızda görüntülenen Address'nin Sparrow'de gösterilenle eşleştiğinden emin olun. Ardından "*1*" düğmesine basın.


![CCQ](assets/fr/060.webp)


Address böylece başarıyla doğrulanmıştır.


![CCQ](assets/fr/061.webp)


Artık bu Address ile güvence altına alınacak bitcoinlerin kaynağını açıklamak için bir "*Etiket*" ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenizi sağlayan iyi bir uygulamadır.


![CCQ](assets/fr/062.webp)


Etiketleme hakkında daha fazla bilgi için bu diğer öğreticiyi de tavsiye ederim:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Daha sonra bu Address'i bitcoin almak için kullanabilirsiniz.


![CCQ](assets/fr/063.webp)


## Bitcoin gönder


COLDCARD güvenceli Wallet'nizde ilk Sats'ünüzü aldığınıza göre artık onları da harcayabilirsiniz!


Her zaman olduğu gibi, COLDCARD Q'nuzu açarak ve kilidini açarak başlayın, ardından Sparrow wallet'ü açın ve yeni bir işlem hazırlamak için "*Gönder*" sekmesine gidin.


![CCQ](assets/fr/064.webp)


"Coin kontrolü" istiyorsanız, yani işlemde hangi UTXO'ların tüketileceğini özellikle seçmek istiyorsanız, "*UTXOs*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesindeki aynı ekrana yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçilmiş olacak.


![CCQ](assets/fr/065.webp)


Hedef Address'yı girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.


![CCQ](assets/fr/066.webp)


Bu masrafın amacını hatırlamak için bir "*Etiket*" yazın.


![CCQ](assets/fr/067.webp)


Bu Address'ye gönderilecek tutarı seçin.


![CCQ](assets/fr/068.webp)


İşleminizin ücret oranını mevcut piyasaya göre ayarlayın.


![CCQ](assets/fr/069.webp)


Tüm işlem parametrelerinizin doğru olduğundan emin olun ve ardından "*İşlem Oluştur*" seçeneğine tıklayın.


![CCQ](assets/fr/070.webp)


Her şey sizi tatmin ediyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![CCQ](assets/fr/071.webp)


İşleminizi Sparrow'da oluşturduktan sonra, COLDCARD'ınızla imzalama zamanı gelmiştir. PSBT'ı (imzasız işlem) cihazınıza iletmek için birkaç seçeneğiniz vardır. Kablolu veri iletimi etkinse, işlemi diğer Hardware Wallet'lerde olduğu gibi doğrudan bir USB-C bağlantısı üzerinden gönderebilirsiniz. Bu durumda, Sparrow'da sağ alt köşedeki "*İmzala*" düğmesine tıklamanız gerekir. Benim örneğimde, COLDCARD kablo ile bağlı olmadığı için bu düğme engellenmiştir.


![CCQ](assets/fr/072.webp)


Hardware Wallet ile bilgisayarınız arasında doğrudan temas olmadan bir "hava boşluğu" bağlantısı kurmayı tercih ederseniz, 2 seçeneğiniz vardır. Birincisi ve daha karmaşık olanı bir microSD kart kullanmaktır. MicroSD kartı bilgisayarınıza takın, Sparrow'deki "*İşlemi Kaydet*" düğmesini kullanarak işlemi kaydedin, ardından bu kartı COLDCARD'ınızdaki bir bağlantı noktasına aktarın.


![CCQ](assets/fr/073.webp)


Ardından "*İmzalamaya Hazır*" menüsüne erişin.


![CCQ](assets/fr/074.webp)


Alıcı Address, gönderilen tutar ve işlem ücreti dahil olmak üzere COLDCARD'ınızdaki işlem ayrıntılarını inceleyin.


![CCQ](assets/fr/075.webp)


Her şey doğruysa, işlemi imzalamak için "*ENTER*" düğmesine basın.


![CCQ](assets/fr/076.webp)


Ardından microSD'yi bilgisayarınıza geri yerleştirin ve Sparrow'te imzalı işlemi microSD'den yüklemek için "*İşlem Yükle*" seçeneğine tıklayın. Daha sonra Bitcoin ağına yüklemeden önce son bir kontrol gerçekleştirebileceksiniz.


![CCQ](assets/fr/077.webp)


Air-Gap'te COLDCARD'ınızla imza atmanın microSD yönteminden çok daha basit olan ikinci yöntemi, PSBT'yi doğrudan cihazın kamerası aracılığıyla taramaktır. Sparrow'da "*Karekodu Göster*" seçeneğini seçin.


![CCQ](assets/fr/078.webp)


COLDCARD'da "*Herhangi bir QR Kodunu Tara*" öğesini seçin. Klavyedeki "*QR*" tuşunu da kullanabilirsiniz.


![CCQ](assets/fr/079.webp)


Sparrow üzerinde görüntülenen QR kodunu taramak için COLDCARD'ın kamerasını kullanın.


![CCQ](assets/fr/080.webp)


İşlem ayrıntıları doğrulama için tekrar görünecektir. Her şey sizi tatmin ediyorsa imzalamak için "*ENTER*" tuşuna basın.


![CCQ](assets/fr/081.webp)


COLDCARD'ınız daha sonra imzalanan işlemi bir QR kodu olarak görüntüleyecektir. Bu QR kodunu taramak için Sparrow'da "*Scan QR*" seçeneğini seçerek bilgisayarınızın web kamerasını kullanın.


![CCQ](assets/fr/082.webp)


İmzalı işleminiz artık Sparrow'de görülebilir. Her şeyin doğru olduğunu son bir kez kontrol edin, ardından Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" düğmesine tıklayın.


![CCQ](assets/fr/083.webp)


İşleminizi Sparrow wallet'nin "*İşlemler*" sekmesinden takip edebilirsiniz.


![CCQ](assets/fr/084.webp)


Tebrikler, artık Sparrow wallet ile COLDCARD Q'nun temel kullanımı konusunda hız kazandınız!


Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız çok minnettar olurum. Lütfen bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca COLDCARD Q'nun gelişmiş seçeneklerini tartıştığımız bu diğer eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0