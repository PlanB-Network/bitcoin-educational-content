---
name: Ledger Nano S Plus
description: Ledger Nano S Plus'ın kurulumu ve kullanımı
---
![cover](assets/cover.webp)


Bir Hardware Wallet, bir Bitcoin Wallet'ün özel anahtarlarını yönetmeye ve güvence altına almaya adanmış elektronik bir cihazdır. Genellikle internete bağlı genel amaçlı makinelere kurulan yazılım cüzdanlarının (veya Hot cüzdanlarının) aksine, donanım cüzdanları özel anahtarların fiziksel olarak izole edilmesini sağlayarak bilgisayar korsanlığı ve hırsızlık risklerini azaltır.


Bir Hardware Wallet'nın ana hedefi, saldırı yüzeyini azaltmak için cihazın işlevlerini mümkün olduğunca en aza indirmektir. Daha küçük bir saldırı yüzeyi aynı zamanda daha az potansiyel saldırı vektörü, yani saldırganların bitcoinlere erişmek için yararlanabileceği sistemde daha az zayıflık anlamına gelir.


Özellikle mutlak değer olarak veya toplam varlıklarınızın bir oranı olarak önemli miktarlara sahipseniz, bitcoinlerinizi güvence altına almak için bir Hardware Wallet kullanmanız önerilir.


Donanım cüzdanları, bir bilgisayar veya akıllı telefondaki Wallet yönetim yazılımı ile birlikte kullanılır. Bu yazılım işlemlerin oluşturulmasını yönetir, ancak bu işlemleri doğrulamak için gerekli kriptografik imza yalnızca Hardware Wallet içinde yapılır. Bu, özel anahtarların hiçbir zaman potansiyel olarak savunmasız bir ortama maruz kalmadığı anlamına gelir.


Donanım cüzdanları kullanıcı için ikili koruma sunar: bir yandan özel anahtarları çevrimdışı tutarak bitcoinlerinizi uzaktan saldırılara karşı korurlar, diğer yandan da genellikle anahtarları çıkarma girişimlerine karşı daha iyi fiziksel direnç sunarlar. İşte tam da bu 2 güvenlik kriterine göre piyasada bulunan farklı modeller değerlendirilebilir ve sıralanabilir.


Bu eğitimde, bu çözümlerden birini keşfetmeyi öneriyorum: **Ledger Nano S Plus**.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Ledger Nano S Plus'a Giriş


Ledger Nano S Plus, Fransız Hardware Wallet şirketi tarafından üretilen ve 79 € fiyatla pazarlanan bir Ledger'tür.


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus, donanıma yönelik fiziksel saldırılara karşı gelişmiş koruma sağlayan CC EAL6+ sertifikalı bir çip ("*secure element*") ile donatılmıştır. Ekran ve düğmeler doğrudan bu çip tarafından kontrol edilmektedir. Sıklıkla dile getirilen bir eleştiri noktası, bu çipin kodunun açık kaynaklı olmamasıdır, bu da bu bileşenin bütünlüğüne belirli bir güven duyulmasını gerektirir. Bununla birlikte, bu unsur bağımsız uzmanlar tarafından denetlenmektedir.


Kullanım açısından, Ledger Nano S Plus yalnızca kablolu bir USB-C bağlantısı üzerinden çalışır.


Ledger, örneğin Taproot veya Miniscript gibi yeni Bitcoin özelliklerini her zaman çok hızlı bir şekilde benimsemesiyle rakiplerinden ayrılıyor ve bu da çok takdir ediliyor.

Test ettikten sonra, Ledger Nano S Plus'ın mükemmel bir giriş seviyesi Hardware Wallet olduğunu gördüm. Makul bir fiyat karşılığında yüksek seviyede güvenlik sunuyor. Aynı fiyat aralığındaki diğer cihazlara kıyasla en büyük dezavantajı aygıt yazılımı kodunun açık kaynaklı olmaması. Ayrıca, Nano S Plus'ın ekranı Ledger Flex veya Coldcard Q1 gibi daha pahalı modellere kıyasla nispeten küçüktür. Bununla birlikte, Interface çok iyi tasarlanmıştır: iki düğmesi ve küçük ekranına rağmen, BIP39 passphrase gibi gelişmiş özellikler de dahil olmak üzere kullanımı kolaydır. Ledger Nano S Plus'ın bataryası, Air-gap bağlantısı, kamerası veya micro SD portu yoktur, ancak bu fiyat aralığı için bu oldukça normaldir.


Bence Ledger Nano S Plus, Bitcoin Wallet'nizi güvence altına almak için iyi bir seçenek ve hem yeni başlayanlar hem de orta düzey kullanıcılar için uygun. Ancak bu fiyat aralığında ben şahsen aşağı yukarı aynı seçenekleri sunan Trezor Safe 3'ü tercih ediyorum. Bana göre Trezor'un avantajı secure element'ün yönetiminde: Mnemonic cümle ve anahtarları yalnızca açık kaynak koduyla yönetiliyor, ancak yine de çipin korumasından faydalanıyor. Trezor'un dezavantajı ise Ledger'nın aksine yeni özellikleri uygulamada bazen çok yavaş kalması.


## Ledger Nano S Plus nasıl satın alınır?


Ledger Nano S Plus [resmi web sitesinde] (https://shop.Ledger.com/products/Ledger-nano-s-plus) satışa sunulmuştur. Fiziksel bir mağazadan satın almak için, Ledger web sitesinde [sertifikalı satıcıların listesini] (https://www.Ledger.com/reseller) de bulabilirsiniz.


## Ön Koşullar


Ledger Nano'nuzu aldıktan sonra, ilk adım ambalajın açılmadığından emin olmak için kontrol etmektir. Hasarlıysa, bu Hardware Wallet'un tehlikeye atıldığını ve orijinal olmayabileceğini gösterebilir.


Açıldığında, kutuda aşağıdaki öğeleri bulmalısınız:


- Ledger Nano S Plus;
- Bir USB-C - USB-A kablosu;
- Bir kullanım kılavuzu;
- Mnemonic cümlenizi yazmak için kartlar.


Bu eğitim için 2 yazılım uygulamasına ihtiyacınız olacak: Ledger'yı başlatmak için Ledger Live ve Bitcoin Wallet'nizi yönetmek için Sparrow wallet. Ledger Live](https://www.Ledger.com/Ledger-live) ve [Sparrow wallet](https://sparrowwallet.com/download/) yazılımlarını resmi web sitelerinden indirin.


![NANO S PLUS LEDGER](assets/notext/03.webp)

Bu iki yazılım için, makinenize yüklemeden önce hem orijinalliklerini (GnuPG ile) hem de bütünlüklerini (Hash ile) kontrol etmenizi şiddetle tavsiye ederim. Bunu nasıl yapacağınızdan emin değilseniz, bu diğer öğreticiyi takip edebilirsiniz:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Ledger Nano Nasıl Başlatılır?


Nano'nuzu Ledger Live ve Sparrow wallet'ın yüklü olduğu bilgisayarınıza bağlayın. Ledger'inizde gezinmek için, sola gitmek için sol düğmeyi ve sağa gitmek için sağ düğmeyi kullanın. Bir seçeneği seçmek veya onaylamak için her iki düğmeye de aynı anda basın.


![NANO S PLUS LEDGER](assets/notext/04.webp)


Farklı tanıtım sayfalarında gezinin ve ardından başlamak için 2 düğmeye tıklayın.


![NANO S PLUS LEDGER](assets/notext/05.webp)


"*Yeni bir cihaz olarak kur*" seçeneğini seçin.


![NANO S PLUS LEDGER](assets/notext/06.webp)


Ledger'ünüzün kilidini açmak için kullanılacak PIN kodunu seçin. Bu, yetkisiz fiziksel erişime karşı bir korumadır. Bu PIN kodu Wallet'ünüzün kriptografik anahtarlarının türetilmesinde rol oynamaz. Bu nedenle, bu PIN koduna erişiminiz olmasa bile, 24 kelimelik Mnemonic cümlenize sahip olmanız bitcoinlerinize yeniden erişmenizi sağlayacaktır.


![NANO S PLUS LEDGER](assets/notext/07.webp)


Mümkün olduğunca rastgele 8 haneli bir PIN kodu seçmeniz önerilir. Ayrıca, bu kodu Ledger Nano S Plus cihazınızın kayıtlı olduğu yerden farklı bir yere (örneğin, bir şifre yöneticisine) kaydettiğinizden emin olun.


Rakamlar üzerinde hareket etmek için düğmeleri kullanın, ardından her iki düğmeye aynı anda tıklayarak her bir rakamı seçin.


![NANO S PLUS LEDGER](assets/notext/08.webp)


Onaylamak için PIN kodunuzu ikinci kez girin.


![NANO S PLUS LEDGER](assets/notext/09.webp)


Nano'nuz, kurtarma ifadenizi nasıl yöneteceğinize ilişkin talimatlar sağlar.


**Bu Mnemonic ifadesi tüm bitcoinlerinize tam ve sınırsız erişim sağlar**. Bu ifadeye sahip olan herkes, Ledger'nize fiziksel erişimi olmasa bile fonlarınızı çalabilir. 24 kelimelik ifade, Ledger Nano'nuzun kaybolması, çalınması veya hasar görmesi durumunda bitcoinlerinize yeniden erişim sağlamanıza olanak tanır. Bu nedenle dikkatli bir şekilde kaydedilmesi ve güvenli bir yerde saklanması çok önemlidir.


Ledger'inizle birlikte verilen karton kağıda yazabilir veya daha fazla güvenlik için yangın, sel veya çökme risklerine karşı korumak amacıyla paslanmaz çelik bir ortama kazımanızı tavsiye ederim.


Sağ düğmeye tıklayarak bu talimatlara göz atabilir ve sayfaları atlayabilirsiniz.


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger, rastgele sayı üretecini kullanarak Mnemonic cümlenizi oluşturacaktır. Bu işlem sırasında gözlenmediğinizden emin olun. Ledger tarafından sağlanan kelimeleri seçtiğiniz fiziksel ortama yazın. Güvenlik stratejinize bağlı olarak, ifadenin birkaç tam fiziksel kopyasını çıkarmayı düşünebilirsiniz (ancak önemli olan, bölmeyin). Kelimelerin numaralandırılmış ve sıralı olması çok önemlidir.

***Açıkçası, bu eğitimde yaptığımın aksine, bu kelimeleri asla internette paylaşmamalısınız. Bu örnek Wallet sadece Testnet üzerinde kullanılacak ve eğitimden sonra silinecektir.***


![NANO S PLUS LEDGER](assets/notext/11.webp)


Sonraki kelimelere geçmek için sağ düğmeyi tıklayın.


![NANO S PLUS LEDGER](assets/notext/12.webp)


Tüm kelimeler not edildikten sonra, bir sonraki adıma geçmek için 2 düğmeye tıklayın.


![NANO S PLUS LEDGER](assets/notext/13.webp)


"*Kurtarma ifadenizi onaylayın*" iki düğmeye tıklayın, ardından Mnemonic ifadenizin kelimelerini doğru şekilde not ettiğinizi onaylamak için sırayla seçin. Seçenekler arasında gezinmek için sol ve sağ düğmeleri kullanın, ardından 2 düğmeye tıklayarak doğru kelimeyi seçin. Bu işleme 24. kelimeye kadar devam edin.


![NANO S PLUS LEDGER](assets/notext/14.webp)


Onaylamakta olduğunuz ifade Ledger'in bir önceki adımda size sağladığı ifadeyle tam olarak eşleşiyorsa devam edebilirsiniz. Eşleşmiyorsa, Mnemonic ifadesinin fiziksel yedeklemenizin yanlış olduğunu ve işlemi yeniden başlatmanız gerektiğini gösterir.


![NANO S PLUS LEDGER](assets/notext/15.webp)


Ve işte, seed'unuz Ledger Nano S Plus'ınızda doğru şekilde oluşturuldu. Bu seed'dan yeni bir Bitcoin Wallet oluşturmaya geçmeden önce, cihaz ayarlarını birlikte inceleyelim.


## Ledger'ınızın ayarları nasıl değiştirilir?


Ayarlara erişmek için 2 düğmesini birkaç saniye basılı tutun.


![NANO S PLUS LEDGER](assets/notext/16.webp)


"*Ayarlar*" menüsüne tıklayın.


![NANO S PLUS LEDGER](assets/notext/17.webp)


Ve "*Genel*" öğesini seçin.


![NANO S PLUS LEDGER](assets/notext/18.webp)


"*Language*" menüsünde ekran dilini değiştirebilirsiniz.


![NANO S PLUS LEDGER](assets/notext/19.webp)


"*Parlaklık*" menüsünde ekran parlaklığını ayarlayabilirsiniz. Şimdilik genel ayarların geri kalanıyla ilgilenmiyoruz.


![NANO S PLUS LEDGER](assets/notext/20.webp)


Şimdi, "*Güvenlik*" ayarları bölümüne gidin.


![NANO S PLUS LEDGER](assets/notext/21.webp)


"*PIN Değiştir*" PIN kodunuzu değiştirmenizi sağlar.

![NANO S PLUS LEDGER](assets/notext/22.webp)

"*passphrase*" bir BIP39 passphrase kurmanızı sağlar. passphrase, kurtarma ifadenizle birlikte Wallet'niz için ek bir Layer güvenliği sağlayan isteğe bağlı bir paroladır.


![NANO S PLUS LEDGER](assets/notext/23.webp)


Şu anda Wallet'nız 24 kelimeden oluşan bir Mnemonic cümlesinden üretilmektedir. Bu kurtarma cümlesi çok önemlidir çünkü kayıp durumunda Wallet'nızın tüm anahtarlarını geri yüklemenizi sağlar. Bununla birlikte, tek bir hata noktası (SPOF) oluşturur. Eğer ele geçirilirse, bitcoinleriniz tehlikeye girer. İşte burada passphrase devreye giriyor. Bu, Wallet'nın güvenliğini artırmak için Mnemonic ifadesine eklenen, isteğe bağlı olarak seçebileceğiniz bir paroladır.


passphrase PIN kodu ile karıştırılmamalıdır. Kriptografik anahtarlarınızın türetilmesinde rol oynar. Mnemonic cümlesiyle birlikte çalışarak anahtarların üretildiği seed'i değiştirir. Böylece, birisi 24 kelimelik cümlenizi ele geçirse bile, passphrase olmadan fonlarınıza erişemez. Bir passphrase kullanmak esasen farklı anahtarlara sahip yeni bir Wallet oluşturur. passphrase'nin (biraz bile olsa) değiştirilmesi generate'u farklı bir Wallet haline getirecektir.


passphrase, bitcoinlerinizin güvenliğini artırmak için çok güçlü bir araçtır. Ancak, Wallet'ünüze erişimi kaybetmemek için uygulamadan önce nasıl çalıştığını anlamak çok önemlidir. Bu nedenle, Ledger'ünüzde bir passphrase kurmak istiyorsanız, size özel bu diğer eğitime başvurmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

"*PIN kilidi*" menüsü, belirli bir süre kullanılmadığında Ledger'inizin otomatik olarak kilitlenmesini yapılandırmanıza ve etkinleştirmenize olanak tanır.


![NANO S PLUS LEDGER](assets/notext/24.webp)


"*Ekran koruyucu*" menüsü Ledger Nano'nuzun uyku modunu ayarlamanızı sağlar. "*PIN lock*" seçeneği uyku moduna karşılık gelecek şekilde etkinleştirilmediği sürece ekran koruyucunun uyandıktan sonra PIN girişi gerektirmediğini unutmayın. Bu özellik özellikle batarya ile donatılmış Ledger Nano X cihazlarının enerji tüketimini azaltmak için kullanışlıdır.


![NANO S PLUS LEDGER](assets/notext/25.webp)


Son olarak, "*Cihazı sıfırla*" menüsü Ledger'nizi sıfırlamanızı sağlar. Bu sıfırlama işlemine yalnızca bitcoinleri güvence altına alan herhangi bir anahtar içermediğinden eminseniz devam edin, çünkü fonlarınıza erişiminizi kalıcı olarak kaybedebilirsiniz. Bu seçenek boş bir kurtarma testi yapmak için faydalı olabilir, ancak bundan biraz daha sonra bahsedeceğim.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Bitcoin Uygulaması Nasıl Kurulur?


Bilgisayarınızda Ledger Live yazılımını başlatarak başlayın, ardından Ledger Nano'nuzu bağlayın ve kilidini açın. Ledger Live'da "*My Ledger*" menüsüne gidin. Nano'nuza erişim yetkisi vermeniz istenecektir.


![NANO S PLUS LEDGER](assets/notext/27.webp)


İki düğmeye tıklayarak Ledger'inize erişimi doğrulayın.


![NANO S PLUS LEDGER](assets/notext/28.webp)


İlk olarak, Ledger Live'da "*Genuine check*" (Orijinal kontrolü) göründüğünden emin olun. Bu, cihazınızın orijinal olduğunu onaylar.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Ledger Nano'nuzun aygıt yazılımı güncel değilse, Ledger Live otomatik olarak güncellemeyi önerecektir. Gerekirse, yüklemeyi başlatmak için "*Ürün yazılımını güncelle*" ve ardından "*Güncellemeyi yükle*" üzerine tıklayın. Ledger'nizde, onaylamak için iki düğmeye tıklayın, ardından kurulum sırasında bekleyin.


Son olarak, Bitcoin uygulamasını ekleyeceğiz. Bunu yapmak için, Ledger Live'da "*Bitcoin (BTC)*"nin yanındaki "*Yükle*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/30.webp)


Uygulama Nano'nuza yüklenecektir.


![NANO S PLUS LEDGER](assets/notext/31.webp)


Şu andan itibaren, Wallet'inizin düzenli yönetimi için artık Ledger Live yazılımına ihtiyacınız olmayacak. Yeni sürümler mevcut olduğunda aygıt yazılımını güncellemek için ara sıra geri dönebilirsiniz. Diğer her şey için, bir Bitcoin Wallet'i etkili bir şekilde yönetmek için çok daha kapsamlı bir araç olan Sparrow wallet'i kullanacağız.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Sparrow ile Yeni Bir Bitcoin Wallet Nasıl Kurulur?


Sparrow wallet'yi açın ve ana ekrana erişmek için giriş sayfalarını atlayın. Ekranın sağ alt kısmında bulunan anahtarı gözlemleyerek bir düğüme doğru şekilde bağlı olup olmadığınızı kontrol edin.


![NANO S PLUS LEDGER](assets/notext/33.webp)


Kendi Bitcoin düğümünüzü kullanmanızı şiddetle tavsiye ederim. Bu eğitimde, Testnet'te olduğum için genel bir düğüm (sarı) kullanıyorum, ancak normal kullanım için yerel bir Bitcoin core (Green) veya uzak bir düğüme (mavi) bağlı bir Electrum sunucusunu tercih etmek daha iyidir.


"*Dosya*" menüsüne ve ardından "*Yeni Wallet*" seçeneğine tıklayın.


![NANO S PLUS LEDGER](assets/notext/34.webp)


Bu Wallet için bir isim seçin ve ardından "*Wallet* Oluştur "a tıklayın.


![NANO S PLUS LEDGER](assets/notext/35.webp)


"*Script Type*" açılır menüsünde, bitcoinlerinizi güvence altına almak için kullanılacak script türünü seçin. "*Taproot*" veya mevcut değilse "*Native SegWit*" seçeneğini tercih etmenizi öneririm.


![NANO S PLUS LEDGER](assets/notext/36.webp)

"*Bağlı Hardware Wallet*" düğmesine tıklayın.

![NANO S PLUS LEDGER](assets/notext/37.webp)


Henüz yapmadıysanız, Ledger Nano S Plus'ınızı bilgisayara bağlayın, PIN kodunuzla kilidini açın ve ardından Bitcoin logosunun üzerindeki 2 düğmeye bir kez tıklayarak "*Bitcoin*" uygulamasını açın.


*Bu eğitimde Bitcoin Testnet uygulamasını kullanıyorum, ancak prosedür Mainnet için de aynıdır.*


![NANO S PLUS LEDGER](assets/notext/38.webp)


Sparrow üzerinde "*Tarama*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/39.webp)


Ardından "*Anahtar Deposunu Aktar*" seçeneğine tıklayın.


![NANO S PLUS LEDGER](assets/notext/40.webp)


Artık ilk hesabınızın genişletilmiş genel anahtarı da dahil olmak üzere Wallet'inizin ayrıntılarını görebilirsiniz. Wallet'in oluşturulmasını tamamlamak için "*Uygula*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Sparrow wallet'a erişimi güvence altına almak için güçlü bir parola seçin. Bu parola, Sparrow'daki Wallet verilerinize erişimin güvenliğini sağlayacak ve genel anahtarlarınızı, adreslerinizi, etiketlerinizi ve işlem geçmişinizi herhangi bir yetkisiz erişime karşı korumaya yardımcı olacaktır.


Unutmamak için bu şifreyi bir şifre yöneticisine kaydetmenizi tavsiye ederim.


![NANO S PLUS LEDGER](assets/notext/42.webp)


Ve işte oldu, Wallet'niz artık yaratıldı!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Wallet'ünüzdeki ilk bitcoinlerinizi almadan önce, **kuru çalıştırma kurtarma testi** yapmanızı şiddetle tavsiye ederim. Xpub'ınız gibi referans bir bilgiyi not edin, ardından Wallet hala boşken Ledger Nano'nuzu sıfırlayın. Daha sonra, kağıt yedeklerinizi kullanarak Wallet'ünüzü Ledger'e geri yüklemeyi deneyin. Geri yüklemeden sonra oluşturulan xpub'ın başlangıçta not ettiğinizle eşleşip eşleşmediğini kontrol edin. Eğer öyleyse, kağıt yedeklerinizin güvenilir olduğundan emin olabilirsiniz.


Kurtarma testinin nasıl yapılacağı hakkında daha fazla bilgi edinmek için bu diğer eğitime başvurmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ledger Nano ile bitcoin nasıl alınır?


"*Receive*" sekmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/44.webp)


Ledger Nano S Plus'ınızı bilgisayara bağlayın, PIN kodunuzla kilidini açın ve ardından "*Bitcoin*" uygulamasını açın.


![NANO S PLUS LEDGER](assets/notext/45.webp)

Sparrow wallet tarafından sağlanan Address'yi kullanmadan önce, Ledger'nizin ekranında doğrulayın. Bu uygulama, Sparrow'de görüntülenen Address'nin sahte olmadığını ve Hardware Wallet'in gerçekten de bu Address ile güvence altına alınan bitcoinleri daha sonra harcamak için gerekli özel anahtara sahip olduğunu doğrulamanızı sağlar. Bu, çeşitli saldırı türlerinden kaçınmanıza yardımcı olur.

Bu doğrulamayı gerçekleştirmek için "*Address'ü Göster*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/46.webp)


Ledger'nızda görüntülenen Address'in Sparrow wallet'te belirtilenle eşleştiğinden emin olun. Geçerliliğinden emin olmak için Address'inizi gönderene vermeden hemen önce bu doğrulamayı yapmanız da önerilir. Address'in tamamını görüntülemek için düğmeleri kullanabilirsiniz.


![NANO S PLUS LEDGER](assets/notext/47.webp)


Ardından adresler gerçekten aynıysa "*Onayla*" seçeneğine tıklayın.


![NANO S PLUS LEDGER](assets/notext/48.webp)


Bu Address ile güvence altına alınacak bitcoinlerin kaynağını açıklamak için bir "*Etiket*" ekleyebilirsiniz. Bu, UTXO'larınızı daha iyi yönetmenize yardımcı olan iyi bir uygulamadır.


![NANO S PLUS LEDGER](assets/notext/49.webp)


Etiketleme hakkında daha fazla bilgi için bu diğer eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Daha sonra bu Address'i bitcoin almak için kullanabilirsiniz.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Ledger Nano ile bitcoin nasıl gönderilir?


Artık ilk Sats'ünüzü Nano S Plus ile güvence altına alınmış Wallet'nizde aldığınıza göre, onları da harcayabilirsiniz! Ledger'inizi bilgisayarınıza bağlayın, kilidini açın, Sparrow wallet'u başlatın ve ardından yeni bir işlem oluşturmak için "*Gönder*" sekmesine gidin.


![NANO S PLUS LEDGER](assets/notext/51.webp)


"*Coin kontrolü*" yapmak istiyorsanız, yani işlemde hangi UTXO'ların tüketileceğini özellikle seçmek istiyorsanız, "*UTXO'lar*" sekmesine gidin. Harcamak istediğiniz UTXO'ları seçin ve ardından "*Seçilenleri Gönder*" seçeneğine tıklayın. "*Gönder*" sekmesinin aynı ekranına yönlendirileceksiniz, ancak UTXO'larınız işlem için zaten seçili olacaktır.


![NANO S PLUS LEDGER](assets/notext/52.webp)


Hedef Address'i girin. "*+ Ekle*" düğmesine tıklayarak birden fazla adres de girebilirsiniz.


![NANO S PLUS LEDGER](assets/notext/53.webp)


Bu harcamanın amacını hatırlamak için bir "*Etiket*" not edin.


![NANO S PLUS LEDGER](assets/notext/54.webp)


Bu Address'ya gönderilen tutarı seçin.


![NANO S PLUS LEDGER](assets/notext/55.webp)


İşlem ücreti oranını mevcut piyasaya göre ayarlayın.


![NANO S PLUS LEDGER](assets/notext/56.webp)

İşleminizin tüm ayarlarının doğru olduğundan emin olun, ardından "*İşlem Oluştur*" seçeneğine tıklayın.

![NANO S PLUS LEDGER](assets/notext/57.webp)


Her şey size iyi görünüyorsa, "*İmzalama için İşlemi Sonlandır*" seçeneğine tıklayın.


![NANO S PLUS LEDGER](assets/notext/58.webp)


"*İmzala*" üzerine tıklayın.


![NANO S PLUS LEDGER](assets/notext/59.webp)


Ledger Nano S Plus'ınızın yanındaki "*İmzala*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Alıcının alıcı Address'i, gönderilen tutar ve ücret tutarı dahil olmak üzere Ledger'unuzun ekranındaki işlem ayarlarını doğrulayın.


![NANO S PLUS LEDGER](assets/notext/61.webp)


Her şey size iyi görünüyorsa, imzalamak için "*İşlemi imzala*" üzerindeki iki düğmeye basın.


![NANO S PLUS LEDGER](assets/notext/62.webp)


İşleminiz artık imzalanmıştır. Her şeyin sizin için iyi göründüğünü iki kez kontrol edin, ardından Bitcoin ağında yayınlamak için "*İşlemi Yayınla*" düğmesine tıklayın.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Bunu Sparrow wallet'in "*İşlemler*" sekmesinde bulabilirsiniz.


![NANO S PLUS LEDGER](assets/notext/64.webp)


Tebrikler, artık Ledger Nano S Plus'ın Sparrow wallet ile temel kullanımı konusunda hız kazandınız! Gelecekteki bir eğitimde, Miniscript'ten yararlanmak için Ledger'ü Liana ile nasıl kullanacağımızı göreceğiz.


Eğer bu yazıyı faydalı bulduysanız, aşağıya beğenilerinizi bırakırsanız çok memnun olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!


Ayrıca Ledger Flex hakkındaki bu tam eğitime de göz atmanızı tavsiye ederim:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a