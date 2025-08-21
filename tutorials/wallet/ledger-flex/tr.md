---
name: Ledger Flex
description: Ledger Flex'in kurulumu ve kullanımı
---
![cover](assets/cover.webp)


![video](https://youtu.be/V3wnS9_Ieyc)


Bir Hardware Wallet, bir Bitcoin Wallet'ün özel anahtarlarını yönetmeye ve güvence altına almaya adanmış elektronik bir cihazdır. Genellikle internete bağlı genel amaçlı makinelere kurulan yazılım cüzdanlarının (veya Hot cüzdanlarının) aksine, donanım cüzdanları özel anahtarların fiziksel olarak izole edilmesini sağlayarak bilgisayar korsanlığı ve hırsızlık risklerini azaltır.


Bir Hardware Wallet'nın ana hedefi, saldırı yüzeyini azaltmak için cihazın işlevlerini en aza indirmektir. Daha az saldırı yüzeyi aynı zamanda daha az potansiyel saldırı vektörü, yani saldırganların bitcoinlere erişmek için sistemde yararlanabileceği daha az zayıf nokta anlamına gelir.


Özellikle mutlak değer olarak veya toplam varlıklarınızın bir oranı olarak önemli miktarlara sahipseniz, bitcoinlerinizi güvence altına almak için bir Hardware Wallet kullanmanız önerilir.


Donanım cüzdanları, bir bilgisayar veya akıllı telefondaki Wallet yönetim yazılımı ile birlikte kullanılır. Bu yazılım işlemlerin oluşturulmasını yönetir, ancak bu işlemleri doğrulamak için gerekli kriptografik imza yalnızca Hardware Wallet içinde yapılır. Bu, özel anahtarların hiçbir zaman potansiyel olarak savunmasız bir ortama maruz kalmadığı anlamına gelir.


Donanım cüzdanları kullanıcı için ikili koruma sunar: bir yandan özel anahtarları çevrimdışı tutarak bitcoinlerinizi uzaktan saldırılara karşı korurlar, diğer yandan da genellikle anahtarları çıkarma girişimlerine karşı daha iyi fiziksel direnç sunarlar. İşte tam da bu 2 güvenlik kriterine göre piyasada bulunan farklı modeller değerlendirilebilir ve sıralanabilir.


Bu eğitimde, bu çözümlerden birini keşfetmeyi öneriyorum: **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)


## Ledger Flex'e Giriş


Ledger Flex, Fransız Ledger şirketi tarafından üretilen ve 249 € fiyatla pazarlanan bir Hardware Wallet'dir.


![LEDGER FLEX](assets/notext/02.webp)


Siyah-beyaz bir ekran teknolojisi olan büyük bir E Ink dokunmatik ekrana sahiptir. Bu, elektronik okuyucularda bulunan teknolojinin aynısıdır. E Ink ekran parlak güneş ışığında bile net ve okunabilir bir görüntü sağlar ve çok az enerji tüketir ya da ekran durağan olduğunda hiç tüketmez. Siyah ve beyaz pigment parçacıkları içeren mikrokapsüller kullanarak çalışır. Bir elektrik yükü uygulandığında, siyah veya beyaz parçacıklar ekranın yüzeyine hareket eder ve böylece metin veya görüntülerin oluşmasını sağlar.

Ledger Flex, donanıma yönelik fiziksel saldırılara karşı gelişmiş koruma sağlayan CC EAL6+ sertifikalı "secure element" çip ile donatılmıştır. Ekran doğrudan bu çip tarafından kontrol edilir. Yaygın bir eleştiri noktası, bu çipin kodunun açık kaynaklı olmaması ve bu bileşenin bütünlüğüne belirli bir düzeyde güven duyulmasını gerektirmesidir. Ancak bu unsur bağımsız uzmanlar tarafından denetlenmektedir.


Kullanım açısından, Ledger Flex çeşitli bağlantı seçenekleri sunar: Bluetooth, USB-C ve NFC. Geniş ekran, işlem ayrıntılarınızın kolayca doğrulanmasını sağlar. Ledger, örneğin Miniscript gibi yeni Bitcoin özelliklerini hızla benimsemesiyle de rakiplerinden ayrılıyor.


Test ettikten sonra ürünün kalitesinden çok etkilendim. Kullanıcı deneyimi mükemmel ve cihaz sezgisel. Mükemmel bir Hardware Wallet. Ancak bence 2 büyük dezavantajı var: çipin kodunu doğrulayamaması ve elbette rakiplerinden önemli ölçüde daha yüksek olan fiyatı. Karşılaştırma yapmak gerekirse, Foundation'ın en gelişmiş modeli 199$'a, Coinkite'ınki 219.99$'a satılırken, geniş bir dokunmatik ekranla donatılmış en yeni Trezor 169€'dan satılıyor.


## Ledger Flex Nasıl Satın Alınır?


Ledger Flex [resmi web sitesinden] (https://shop.Ledger.com/pages/Ledger-flex) satın alınabilir. Fiziksel bir mağazadan satın almak için, Ledger web sitesinde [sertifikalı satıcıların listesini] (https://www.Ledger.com/reseller) de bulabilirsiniz.


## Ön Koşullar


Ledger Flex'inizi aldıktan sonra ilk adım, ambalajın açılmadığından emin olmak için ambalajı incelemektir.


![LEDGER FLEX](assets/notext/03.webp)


Ledger'ün ambalajında 2 adet mühürleme şeridi bulunmalıdır. Bu şeritlerin eksik veya hasarlı olması, Hardware Wallet'nin tehlikeye atıldığını ve orijinal olmayabileceğini gösterebilir.


![LEDGER FLEX](assets/notext/04.webp)


Açıldığında, kutuda aşağıdaki öğeleri bulmalısınız:


- Ledger Flex;
- Bir USB-C kablosu;
- Bir kullanım kılavuzu;
- Mnemonic cümlenizi yazmak için kartlar.


![LEDGER FLEX](assets/notext/05.webp)


Bu eğitim için 2 adet yazılıma ihtiyacınız olacak: Ledger Flex'i başlatmak için Ledger Live ve Bitcoin Wallet'unuzu yönetmek için Sparrow wallet. Ledger Live](https://www.Ledger.com/Ledger-live) ve [Sparrow wallet](https://sparrowwallet.com/download/) yazılımlarını resmi web sitelerinden indirin.


![LEDGER FLEX](assets/notext/06.webp)

Yakında indirdiğiniz yazılımların gerçekliğini ve bütünlüğünü nasıl doğrulayacağınıza dair bir eğitim sunacağız. Ledger Live ve Sparrow için bunu burada yapmanızı şiddetle tavsiye ederim.

## Ledger Live ile bir Ledger Flex Nasıl Başlatılır?


Sağ taraftaki düğmeye birkaç saniye basarak Ledger Flex'inizi açın.


![LEDGER FLEX](assets/notext/07.webp)


Farklı tanıtım sayfaları arasında gezinin.


![LEDGER FLEX](assets/notext/08.webp)


"*Ledger Live olmadan kur*" seçeneğini seçin, ardından "*Ledger Live'ı atla*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/09.webp)


Daha sonra Ledger'iniz için bir isim seçmeniz istenecektir. "*Adı belirle*" üzerine tıklayın ve ardından seçtiğiniz adı girin.


![LEDGER FLEX](assets/notext/10.webp)


Cihazınız için Ledger'nizin kilidini açmak için kullanılacak PIN kodunu seçin. Dolayısıyla bu, yetkisiz fiziksel erişime karşı bir korumadır. Bu PIN kodu Wallet'inizin kriptografik anahtarlarının türetilmesinde rol oynamaz. Bu nedenle, bu PIN koduna erişiminiz olmasa bile, 24 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.


Mümkün olduğunca rastgele 8 basamaklı bir PIN kodu seçmeniz önerilir. Ayrıca, bu kodu Ledger Flex'inizin depolandığı yerden farklı bir yere kaydettiğinizden emin olun (örneğin, bir şifre yöneticisine).


![LEDGER FLEX](assets/notext/11.webp)


Onaylamak için PIN kodunuzu ikinci kez girin.


![LEDGER FLEX](assets/notext/12.webp)


Ardından mevcut bir Wallet'ü kurtarmak veya yeni bir tane oluşturmak arasında seçim yapmanız istenecektir. Bu eğitimde sıfırdan yeni bir Wallet oluşturmayı ele alacağız, bu nedenle yeni bir generate ifadesi oluşturmak için "*Yeni bir Ledger* olarak kur" seçeneğini seçin.


![LEDGER FLEX](assets/notext/13.webp)


Flex'iniz iyileşme ifadenizi nasıl yöneteceğinize dair talimatlar verecektir.


**Bu Mnemonic ifadesi tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu ifadeye sahip olan herkes, Ledger'inize fiziksel erişimi olmasa bile fonlarınızı çalabilir. 24 kelimelik ifade, Ledger Flex'inizin kaybolması, çalınması veya hasar görmesi durumunda bitcoinlerinize erişimin yeniden sağlanmasına olanak tanır. Bu nedenle dikkatli bir şekilde kaydedilmesi ve güvenli bir yerde saklanması çok önemlidir.


Ledger'nızla birlikte verilen karton kağıda yazabilir veya daha fazla güvenlik için yangın, sel veya çökme risklerine karşı korumak amacıyla paslanmaz çelik bir ortama kazımanızı tavsiye ederim.


Ekrana dokunarak bu talimatlara göz atabilir ve sayfaları atlayabilirsiniz.


![LEDGER FLEX](assets/notext/14.webp)

Ledger, rastgele sayı üretecini kullanarak Mnemonic ifadenizi oluşturacaktır. Bu işlem sırasında gözlenmediğinizden emin olun. Ledger tarafından sağlanan sözcükleri seçtiğiniz fiziksel ortama yazın. Güvenlik stratejinize bağlı olarak, ifadenin birkaç tam fiziksel kopyasını çıkarmayı düşünebilirsiniz (ancak en önemlisi, bölmeyin). Kelimelerin numaralandırılmış ve sıralı olması önemlidir.

***Açıkçası, bu eğitimde yaptığımın aksine, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimin sonunda silinecektir.***


![LEDGER FLEX](assets/notext/15.webp)


Bir sonraki kelime grubuna geçmek için "*Sonraki*" düğmesine tıklayın. Tüm kelimeler not edildikten sonra, bir sonraki adıma geçmek için "*Bitti*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/16.webp)


"*Onaylamaya başla*" düğmesine tıklayın, ardından Mnemonic cümlenizdeki kelimeleri doğru şekilde not ettiğinizi onaylamak için sırayla seçin. Bu işleme 24. kelimeye kadar devam edin.


![LEDGER FLEX](assets/notext/17.webp)


Onaylamakta olduğunuz ifade Flex'in önceki adımda size sağladığı ifadeyle tam olarak eşleşiyorsa devam edebilirsiniz. Eşleşmiyorsa bu, Mnemonic ifadesinin fiziksel yedeklemesinin yanlış olduğunu ve işlemi yeniden başlatmanız gerektiğini gösterir.


![LEDGER FLEX](assets/notext/18.webp)


Ve işte, seed'nız Ledger Flex'iniz üzerinde doğru bir şekilde oluşturuldu. Bu seed'dan yeni bir Bitcoin Wallet oluşturmaya geçmeden önce, cihaz ayarlarını birlikte inceleyelim.


## Ledger'nizin ayarları nasıl değiştirilir?


Ledger'inizi kilitlemek ve kilidini açmak için yan düğmeye basın. Ardından bir önceki adımda belirlediğiniz PIN kodunu girmeniz istenecektir.


![LEDGER FLEX](assets/notext/19.webp)


Ayarlara erişmek için cihazınızın sol alt köşesindeki dişli simgesine tıklayın.


![LEDGER FLEX](assets/notext/20.webp)


"*Adı*" menüsü Ledger'unuzun adını değiştirmenize olanak tanır.


![LEDGER FLEX](assets/notext/21.webp)


"*Bu Ledger Hakkında*" bölümünde Flex'iniz hakkında bilgi bulabilirsiniz.


![LEDGER FLEX](assets/notext/22.webp)


"*Kilit ekranı*" menüsünde, "*Kilit ekranı resmini özelleştir*" seçeneğini seçerek kilit ekranında görüntülenen görüntüyü değiştirme seçeneğine sahipsiniz. Cihazın E Ink ekran teknolojisi sayesinde pil tüketmeden ekranı sürekli açık tutmak mümkündür. E Ink ekranlar statik bir görüntüyü korumak için enerji kullanmaz. Ancak ekran değişiklikleri sırasında enerji tüketirler.

"*Otomatik kilit*" alt menüsü, belirli bir süre kullanılmadığında Ledger'inizin otomatik olarak kilitlenmesini yapılandırmanıza ve etkinleştirmenize olanak tanır.

![LEDGER FLEX](assets/notext/23.webp)


"*Sesler*" menüsü Flex'inizin seslerini açmanızı veya kapatmanızı sağlar. "Dil" menüsünde ise ekran dilini değiştirebilirsiniz.


![LEDGER FLEX](assets/notext/24.webp)


Sağ oka tıklayarak diğer ayarlara erişebilirsiniz. "*PIN Değiştir*" PIN kodunuzu değiştirmenizi sağlar.


![LEDGER FLEX](assets/notext/25.webp)


"*Bluetooth*" ve "*NFC*" menüleri bu iletişimleri yönetmenizi sağlar.


![LEDGER FLEX](assets/notext/26.webp)


"*Batarya*" bölümünde Ledger'nin otomatik olarak kapanmasını ayarlayabilirsiniz.


![LEDGER FLEX](assets/notext/27.webp)


"*Gelişmiş*" bölümü daha gelişmiş güvenlik ayarlarına erişmenizi sağlar. Güvenliği artırmak için "*PIN shuffle*" seçeneğini etkin tutmanız tavsiye edilir. Ayrıca bu menüde bir BIP39 passphrase yapılandırabilirsiniz.


![LEDGER FLEX](assets/notext/28.webp)


passphrase, kurtarma ifadesiyle birlikte Wallet'iniz için ek bir Layer güvenlik sağlayan isteğe bağlı bir paroladır.


Şu anda Wallet'unuz 24 kelimeden oluşan bir Mnemonic cümlesinden üretilmektedir. Bu kurtarma cümlesi, kayıp durumunda Wallet'unuzun tüm anahtarlarını geri yüklemenizi sağladığı için çok önemlidir. Bununla birlikte, tek bir hata noktası (SPOF) oluşturur. Eğer tehlikeye girerse, bitcoinler tehlikeye girer. passphrase burada devreye girer. Bu, Wallet'un güvenliğini güçlendirmek için Mnemonic ifadesine eklenen, isteğe bağlı olarak seçebileceğiniz bir paroladır.


passphrase, PIN kodu ile karıştırılmamalıdır. Kriptografik anahtarlarınızın türetilmesinde rol oynar. Mnemonic cümlesiyle birlikte çalışarak anahtarların üretildiği seed'ü değiştirir. Böylece, birisi 24 kelimelik cümlenizi ele geçirse bile, passphrase olmadan fonlarınıza erişemez. Bir passphrase kullanmak esasen farklı anahtarlara sahip yeni bir Wallet oluşturur. passphrase'in (birazcık bile) değiştirilmesi generate'yi farklı bir Wallet haline getirecektir.


passphrase, bitcoinlerinizin güvenliğini artırmak için çok güçlü bir araçtır. Ancak, Wallet'nıza erişimi kaybetmemek için uygulamadan önce nasıl çalıştığını anlamak çok önemlidir. passphrase'in nasıl kullanılacağını başka bir özel eğitimde açıklayacağım.


![LEDGER FLEX](assets/notext/29.webp)


passphrase, bitcoinlerinizin güvenliğini güçlendirmek için çok güçlü bir araçtır. Ancak, Wallet'inize erişiminizi kaybetmemek için uygulamadan önce nasıl çalıştığını anlamak çok önemlidir. Bu yüzden her şeyi özel bir eğitimde açıklıyorum:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Son olarak, son ayarlar sayfası Ledger'unuzu sıfırlamanızı sağlar. Bu sıfırlama işlemine yalnızca bitcoinleri güvence altına alan herhangi bir anahtar içermediğinden eminseniz devam edin, çünkü fonlarınıza erişiminizi kalıcı olarak kaybedebilirsiniz.

![LEDGER FLEX](assets/notext/30.webp)


## Bitcoin uygulaması nasıl kurulur?


Bilgisayarınızda Ledger Live yazılımını başlatarak başlayın, ardından Ledger Flex'inizi bağlayın ve kilidini açın.


![LEDGER FLEX](assets/notext/31.webp)


Ledger Live'da "*My Ledger*" menüsüne gidin. Flex'inize erişim yetkisi vermeniz istenecektir.


![LEDGER FLEX](assets/notext/32.webp)


"*İzin ver*" düğmesine tıklayarak Ledger'ünüzdeki erişimi doğrulayın.


![LEDGER FLEX](assets/notext/33.webp)


Öncelikle, Ledger Flex cihazınızın aygıt yazılımı güncel değilse, Ledger Live otomatik olarak güncellemeyi önerecektir. Varsa, yüklemeyi başlatmak için "*Ürün yazılımını güncelle*" ve ardından "*Güncellemeyi yükle*" üzerine tıklayın.


![LEDGER FLEX](assets/notext/34.webp)


Ledger cihazınızda "*Yükle*" düğmesine tıklayın, ardından kurulum sırasında bekleyin.


![LEDGER FLEX](assets/notext/35.webp)


Ledger Flex'inizin aygıt yazılımı artık günceldir.


![LEDGER FLEX](assets/notext/36.webp)


Dilerseniz Ledger Flex'inizin kilit ekranı duvar kağıdını değiştirebilirsiniz. Bunu yapmak için "*Ekle >*" üzerine tıklayın.


![LEDGER FLEX](assets/notext/37.webp)


"*Bilgisayardan yükle*" düğmesine tıklayın ve fotoğraflarınızdan duvar kağıdınızı seçin.


![LEDGER FLEX](assets/notext/38.webp)


Resminizi kırpabilirsiniz.


![LEDGER FLEX](assets/notext/39.webp)


Farklı seçenekler arasından bir kontrast seçin, ardından "*Kontrastı onayla*" üzerine tıklayın.


![LEDGER FLEX](assets/notext/40.webp)


Flex'inizde "*Resim yükle*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/41.webp)


Görüntüden memnun kaldıysanız, kilit ekranı duvar kağıdınız olarak ayarlamak için "*Keep*"e tıklayın.


![LEDGER FLEX](assets/notext/42.webp)


Son olarak, Bitcoin uygulamasını ekleyeceğiz. Bunu yapmak için, Ledger Live'da "*Bitcoin (BTC)*"nin yanındaki "*Yükle*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/43.webp)


Uygulama Flex'inize yüklenecektir.


![LEDGER FLEX](assets/notext/44.webp)


Şu andan itibaren, Wallet'ünüzün düzenli yönetimi için Ledger Live yazılımına artık ihtiyacınız olmayacak. Yeni sürümler mevcut olduğunda aygıt yazılımını güncellemek için ara sıra geri dönebilirsiniz. Diğer her şey için, bir Bitcoin Wallet'ü verimli bir şekilde yönetmek için çok daha kapsamlı bir araç olan Sparrow wallet'ı kullanacağız.


## Sparrow ile yeni bir Bitcoin Wallet nasıl kurulur?

Sparrow wallet'yi açın ve ana ekrana erişmek için giriş sayfalarını atlayın. Ekranın sağ alt kısmında bulunan anahtarı gözlemleyerek bir düğüme doğru şekilde bağlı olup olmadığınızı kontrol edin.

![LEDGER FLEX](assets/notext/45.webp)


Kendi Bitcoin düğümünüzü kullanmanızı şiddetle tavsiye ederim. Bu eğitimde, Testnet'de olduğum için genel bir düğüm (sarı) kullanıyorum, ancak normal kullanım için yerel bir Bitcoin core (Green) veya uzak bir düğüme (mavi) bağlı bir Electrum sunucusu tercih etmek daha iyidir.


"*Dosya*" menüsüne ve ardından "*Yeni Wallet*" seçeneğine tıklayın.


![LEDGER FLEX](assets/notext/46.webp)


Bu Wallet için bir ad seçin ve ardından "*Wallet* Oluştur "a tıklayın.


![LEDGER FLEX](assets/notext/47.webp)


"*Script Type*" açılır menüsünde, bitcoinlerinizi güvence altına almak için kullanılacak script türünü seçin. "*Taproot*" veya mevcut değilse "*Native SegWit*" seçeneğini tercih etmenizi öneririm.


![LEDGER FLEX](assets/notext/48.webp)


"*Bağlı Hardware Wallet*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/49.webp)


Ledger Flex cihazınızı bilgisayara bağlayın, PIN kodunuzla kilidini açın ve ardından "*Bitcoin*" uygulamasını açın. Bu eğitimde "*Bitcoin Testnet*" uygulamasını kullanıyorum, ancak prosedür Mainnet için de aynıdır.


![LEDGER FLEX](assets/notext/50.webp)


Sparrow'de "*Tarama*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/51.webp)


Ardından "*Anahtar Deposunu Aktar*" seçeneğine tıklayın.


![LEDGER FLEX](assets/notext/52.webp)


Artık ilk hesabınızın genişletilmiş genel anahtarı da dahil olmak üzere Wallet'nizin ayrıntılarını görebilirsiniz. Wallet'nin oluşturulmasını tamamlamak için "*Uygula*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/53.webp)


Sparrow wallet'e erişimi güvence altına almak için güçlü bir parola seçin. Bu parola, Sparrow üzerindeki Wallet verilerinize erişimin güvenliğini sağlayacak ve açık anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi herhangi bir yetkisiz erişime karşı korumaya yardımcı olacaktır.


Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.


![LEDGER FLEX](assets/notext/54.webp)


Ve işte oldu, Wallet'nız artık yaratıldı!


![LEDGER FLEX](assets/notext/55.webp)

Wallet'inize ilk bitcoinlerinizi almadan önce, bir kuru çalıştırma kurtarma testi yapmanızı şiddetle tavsiye ederim. Xpub'ınız gibi referans bir bilgiyi not edin, ardından Wallet hala boşken Ledger Flex'inizi sıfırlayın. Daha sonra, kağıt yedeklerinizi kullanarak Wallet'inizi Ledger'ye geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan xpub'ın başlangıçta not ettiğinizle eşleşip eşleşmediğini kontrol edin. Eğer durum buysa, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


## Ledger Flex ile bitcoin nasıl alınır?


"*Receive*" sekmesine tıklayın.


![LEDGER FLEX](assets/notext/56.webp)


Ledger Flex'inizi bilgisayara bağlayın, PIN kodunuzla kilidini açın ve ardından "*Bitcoin*" uygulamasını açın.


![LEDGER FLEX](assets/notext/57.webp)


Sparrow wallet tarafından sağlanan Address'ü kullanmadan önce, Ledger Flex'inizin ekranında doğrulayın. Bu uygulama, Sparrow'te görüntülenen Address'ün sahte olmadığını ve Ledger'in gerçekten de bu Address ile güvence altına alınan bitcoinleri daha sonra harcamak için gerekli özel anahtara sahip olduğunu doğrulamanızı sağlar.


Bu doğrulamayı gerçekleştirmek için "*Address'yı Görüntüle*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/58.webp)


Ledger Flex'inizde görüntülenen Address'in Sparrow wallet'de belirtilenle eşleştiğinden emin olun. Geçerliliğinden emin olmak için Address'inizi gönderene vermeden hemen önce bu doğrulamayı yapmanız da önerilir.


![LEDGER FLEX](assets/notext/59.webp)


Bu Address ile güvence altına alınacak bitcoinlerin kaynağını açıklamak için bir "*Etiket*" ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenize yardımcı olan iyi bir uygulamadır.


![LEDGER FLEX](assets/notext/60.webp)


Etiketleme hakkında daha fazla bilgi için bu diğer eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Daha sonra bu Address'i bitcoin almak için kullanabilirsiniz.


![LEDGER FLEX](assets/notext/61.webp)


## Ledger Flex ile bitcoin nasıl gönderilir?


Artık Flex ile güvence altına alınmış Wallet'inizde ilk Sats'nızı aldığınıza göre, bunları da harcayabilirsiniz! Ledger'ünüzü bilgisayarınıza bağlayın, kilidini açın, Sparrow wallet'ü başlatın ve ardından yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.


![LEDGER FLEX](assets/notext/62.webp)


"*Coin kontrolü*" yapmak istiyorsanız, yani işlemde hangi UTXO'ların tüketileceğini özellikle seçmek istiyorsanız, "*UTXO'lar*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesinin aynı ekranına yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçilmiş olacak.

![LEDGER FLEX](assets/notext/63.webp)

Hedef Address'i girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.


![LEDGER FLEX](assets/notext/64.webp)


Bu masrafın amacını hatırlamak için bir "*Etiket*" not edin.


![LEDGER FLEX](assets/notext/65.webp)


Bu Address'a gönderilen tutarı seçin.


![LEDGER FLEX](assets/notext/66.webp)


İşleminizin ücret oranını mevcut piyasaya göre ayarlayın.


![LEDGER FLEX](assets/notext/67.webp)


İşleminizin tüm ayarlarının doğru olduğundan emin olun, ardından "*İşlem Oluştur*" seçeneğine tıklayın.


![LEDGER FLEX](assets/notext/68.webp)


Her şey sizi tatmin ediyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![LEDGER FLEX](assets/notext/69.webp)


"*İmzala*" üzerine tıklayın.


![LEDGER FLEX](assets/notext/70.webp)


Ledger Flex'inizin yanındaki "*İmzala*" düğmesine tıklayın.


![LEDGER FLEX](assets/notext/71.webp)


Alıcının Address alıcısı, gönderilen tutar ve ücret tutarı dahil olmak üzere Flex'inizin ekranındaki işlem ayarlarını doğrulayın.


![LEDGER FLEX](assets/notext/72.webp)


İmzalamak için parmağınızı "*İmzalamak için basılı tutun*" düğmesinin üzerinde tutun.


![LEDGER FLEX](assets/notext/73.webp)


İşleminiz artık imzalanmıştır. İşlemi Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" seçeneğine tıklayın.


![LEDGER FLEX](assets/notext/74.webp)


Bunu Sparrow wallet'ün "*İşlemler*" sekmesinde bulabilirsiniz.


![LEDGER FLEX](assets/notext/75.webp)


Tebrikler, artık Ledger Flex'in Sparrow wallet ile temel kullanımını öğrenmiş bulunuyorsunuz! Gelecekteki bir eğitimde, Miniscript'ten yararlanmak için Ledger Flex'i Liana ile nasıl kullanacağımızı göreceğiz.


Eğer bu yazıyı faydalı bulduysanız, aşağıda beğeninizi belirtmenizden memnuniyet duyarım. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!