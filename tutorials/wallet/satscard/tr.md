---
name: Satscard
description: Nunchuk ile bir Satscard kurma ve kullanma
---
![cover](assets/cover.webp)


Bitcoin, eşler arası işlemler gerçekleştirmemizi sağlayan bir elektronik nakit sistemidir. Bununla birlikte, bir işlemin değişmez olduğuna ikna olmak için, gönderen tarafından herhangi bir çifte harcama girişimini önlemek için birkaç onay (genellikle 6) beklemek gerekir. Bu doğrulama gecikmesi, özellikle fiziksel nakit paraya benzer bir anlık kesinlik istendiğinde, bazen rahatsız edici olabilir. Bir banknotun mülkiyetinin anında devredildiği nakit paranın aksine, Bitcoin işlemleri kesin olarak geri alınamaz olarak kabul edilmeden önce bir bekleme süresi içerir.


İşte Satscard burada devreye giriyor. Bir On-Chain işlemi gerçekleştirmeye gerek kalmadan bitcoinlerin fiziksel ve anında aktarımını sağlayan bir yöntem sunar. Satscard, Bitcoin Ownership'in güvenli bir şekilde transfer edilmesini sağlayan bir hamiline kart olarak işlev görür ve böylece geleneksel nakit paraya daha yakın bir deneyim sunar. Bu eğitimde size bu çözümü tanıtacağım.


## Satscard nedir?


Coinkite tarafından üretilen Satscard, Opendime'ın halefidir. Fatura veya Coin'ya benzer şekilde bitcoinlerin fiziksel olarak iletilmesini sağlayan bir NFC kartıdır. Geleneksel Hardware Wallet'ün aksine, Satscard taşıyıcı bir karttır, yani karta fiziksel olarak sahip olmak, üzerinde depolanan anahtarlarla güvence altına alınan bitcoinlerin Ownership'ine eşittir. Fiyatı, seçilen tasarıma bağlı olarak 6.99 ila 17.99 $ arasında değişmektedir.


![SATSCARD](assets/notext/01.webp)


Satscard çipi, bitcoinleri 10 farklı adreste 10 defaya kadar saklamasına olanak tanıyan 10 yuva ile donatılmıştır. Her yuva bağımsız olarak çalışır ve teorik olarak bitcoinleri kilitlemek için yalnızca bir kez kullanılmalıdır. Bitcoinleri harcamak için, Satscard'ın arkasında belirtilen 6 haneli doğrulama kodunu girerek Nunchuk gibi uyumlu bir uygulama ile yuvanın mührünü açmanız yeterlidir.


Kart, Blockchain'deki bitcoinleri güvence altına alan özel anahtarın, karttan fiziksel olarak ayrıldıktan sonra eski sahibi tarafından tutulamamasını sağlar. Alıcı ayrıca Exchange sırasında bir yuvanın geçerliliğini ve içinde saklanan miktarı doğrulayabilir.


Bu sistem özellikle bitcoin ile fiziksel ürünler satın almak veya hediye olarak bitcoin vermek için kullanışlıdır.


## Satscard nasıl satın alınır?


Satscard [resmi Coinkite web sitesinden] (https://store.coinkite.com/store/category/satscard) satın alınabilir. Fiziksel bir mağazadan satın almak için sitede [sertifikalı satıcıların listesini] (https://coinkite.com/resellers) de bulabilirsiniz.

Ayrıca NFC iletişimiyle uyumlu bir telefona veya NFC kartlarını standart frekans olan 13,56 MHz'de okumak için bir USB cihazına ihtiyacınız olacaktır.

## Satscard'a bir slot nasıl yüklenir?


Satscard'ınızı aldıktan sonra ilk adım, açılmadığından emin olmak için ambalajı kontrol etmektir. Paket hasar görmüşse, bu durum kartın ele geçirildiğini ve orijinal olmayabileceğini gösterebilir.


Satscard'ı yönetmek için **Nunchuk Wallet** mobil uygulamasını kullanacağız. Akıllı telefonunuzun NFC uyumlu olduğundan emin olun, ardından Nunchuk'u [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) veya doğrudan [`.apk` dosyası](https://github.com/nunchuk-io/nunchuk-android/releases) üzerinden indirin.


![SATSCARD](assets/notext/02.webp)


Teorik olarak, Nunchuk kullanmadan Satscard'ınızın arkasında belirtilen Address'e doğrudan bitcoin gönderebilirsiniz. Ancak, ilk yuvadaki Address'in gerçekten de Satscard'da saklanan özel bir anahtardan türetildiğini ve sahte bir Address olmadığını doğrulayacağımız için bunu yapmamanızı tavsiye ederim.


Nunchuk'u ilk kez kullanıyorsanız, uygulama size bir hesap oluşturmanızı önerecektir. Bu eğitimin amaçları doğrultusunda, bir hesap oluşturmanız gerekli değildir. Bu nedenle, hesap oluşturmadan devam etmek için "*Misafir olarak devam et*" seçeneğini seçin.


![SATSCARD](assets/notext/03.webp)


Ardından "*Yardımsız Wallet*" üzerine tıklayın.


![SATSCARD](assets/notext/04.webp)


Ardından, "*Kendi başıma keşfedeceğim*" düğmesine tıklayın.


![SATSCARD](assets/notext/05.webp)


Nunchuk ana ekranına geldiğinizde, ekranın üst kısmındaki "*NFC*" logosuna tıklayın.


![SATSCARD](assets/notext/06.webp)


Taramak için Satscard'ınızı telefonunuzun arkasına tutun.


![SATSCARD](assets/notext/07.webp)


Nunchuk, Satscard'ınızın ilk yuvasına karşılık gelen alıcı Address'ü görüntüler. Normalde bu Address, kartınızın arkasında manuel olarak yazılı olanla aynı olmalıdır. Bu Address'ü kopyalayın ve bu yuva ile kilitlemek istediğiniz bitcoinleri transfer etmek için kullanın.


![SATSCARD](assets/notext/08.webp)


## Bir slottaki bitcoinler nasıl kontrol edilir?


İşlem onaylandıktan sonra, Nunchuk ile tarayarak Satscard'ınızın bir yuvasıyla ilişkili bakiyeyi kontrol edebilirsiniz. Böylece, bir işlem sırasında, bitcoinlerin alıcısı, Nunchuk uygulaması aracılığıyla kartın gerçekten kendisine borçlu olunan bitcoinleri içerdiğini anında doğrulayabilir.


![SATSCARD](assets/notext/09.webp)

Karşı taraf Nunchuk uygulamasına sahip değilse, yine de Satscard'ın geçerliliğini doğrulayabilir. Akıllı telefonlarında NFC'yi etkinleştirmeleri ve Satscard'ı cihazın arkasına yerleştirmeleri yeterlidir. Bu işlem, Satscard web sitesini otomatik olarak bir tarayıcıda açacak ve burada kartın geçerliliğinin yanı sıra kartla ilişkili bitcoin miktarı da kontrol edilebilecektir.

![SATSCARD](assets/notext/10.webp)


## Bir slottan bitcoin nasıl çekilir?


Artık Satscard'ın ilk yuvasına belirli miktarda bitcoin yüklendiğine göre, kartı ödeme alıcısına teslim edebilirsiniz.


![SATSCARD](assets/notext/11.webp)


Alıcı sizseniz, Nunchuk'u yüklemeniz gerekir. Uygulamaya girdikten sonra, ekranın üst kısmındaki "*NFC*" logosuna tıklayın.


![SATSCARD](assets/notext/12.webp)


Satscard'ınızı telefonunuzun arkasına yerleştirin.


![SATSCARD](assets/notext/13.webp)


Nunchuk, Address üzerinde güvence altına alınan miktarı gösterecektir.


![SATSCARD](assets/notext/14.webp)


Özel anahtarı açmak ve bitcoinleri sahip olduğunuz bir Address'e taşımak için "*Unseal and sweep balance*" düğmesine tıklayın.


![SATSCARD](assets/notext/15.webp)


"*Sweep to a Wallet*" seçeneği, bitcoinleri doğrudan Nunchuk uygulamanızda zaten mevcut olan bir Wallet'ye göndermenizi sağlar. Fonları farklı bir alıcı Address'ya aktarmak için "*Bir Address'ya Çek*" seçeneğini seçin.


![SATSCARD](assets/notext/16.webp)


Satscard tarafından güvence altına alınan bitcoinleri göndermek istediğiniz alıcı Address'i girin. Girilen Address'in doğru olduğundan emin olun (bu, doğrulayabileceğiniz tek zamandır), ardından "*İşlem oluştur*" düğmesine tıklayın.


![SATSCARD](assets/notext/17.webp)


Satscard'ınızın PIN kodunu girin. Bu 6 haneli kod fiziksel kartın arkasında belirtilmiştir.


![SATSCARD](assets/notext/18.webp)


NFC kartında saklanan özel anahtar ile işlemi imzalarken Satscard'ınızı akıllı telefonunuzun arkasında tutun.


![SATSCARD](assets/notext/19.webp)


İşleminiz artık imzalanmış ve Bitcoin ağında yayınlanmıştır, yani Satscard'ınızda kullanılan yuva artık boştur.


![SATSCARD](assets/notext/20.webp)


## Satscard nasıl tekrar kullanılır?


Opendime gibi tek kullanımlık çözümlerden farklı olarak Satscard, tek bir kartla 10 adede kadar işlem yapılmasına olanak tanıyan 10 bağımsız yuva içeren bir çip ile donatılmıştır. Coinkite tarafından fabrikada önceden yapılandırılan ilk yuva, Satscard'ınızın arkasında yazılı olan alıcı Address'ye karşılık gelir.


![SATSCARD](assets/notext/21.webp)

Diğer 9 yuvayı etkinleştirmek için Nunchuk uygulaması aracılığıyla anahtar çiftini generate ve Address yapmanız gerekecektir. Uygulamanın ana sayfasında, ekranın üst kısmındaki "*NFC*" logosuna tıklayın.

![SATSCARD](assets/notext/22.webp)


Satscard'ınızı telefonunuzun arkasına yerleştirin.


![SATSCARD](assets/notext/23.webp)


Nunchuk kartta hiçbir yuvanın aktif olmadığını gösterir, bu normaldir çünkü birincisi zaten kullanılmış ve ikincisi henüz oluşturulmamıştır. Daha önce kullanılmış yuvaları görmek için "*Mühürsüz yuvaları görüntüle*" seçeneğine tıklayın. On-Chain gizliliğinize zarar verecek Address yeniden kullanımına yol açacağından, bu yuvaların yeniden kullanılmaması şiddetle tavsiye edilir. Bu nedenle, "*Evet*" düğmesine tıklayarak yeni bir yuva oluşturacağız.


![SATSCARD](assets/notext/24.webp)


Şimdi ana chain code'inizi nasıl generate yapacağınızı seçmeniz gerekecektir.


Satscard üzerindeki yuvalar BIP32 standardını takip eder, yani bitcoinleri güvence altına alan kriptografik anahtarların türetilmesi BIP39 cüzdanlarında olduğu gibi bir Mnemonic ifadesine değil, doğrudan bir ana özel anahtara ve bir ana chain code'ye dayanır. Bu iki Elements, HMAC-SHA512 işlevinde girdi olarak kullanılarak generate alt anahtar çiftini oluşturur. Her yuvanın kendi ana anahtarı ve kendi ana chain code'si vardır. Her yuva için yalnızca bir türetme seviyesi vardır.


İlk yuvanın anahtar çifti Coinkite tarafından önceden oluşturulmuştur. Bu nedenle Nunchuk aracılığıyla doğrudan erişiminiz vardır ve alıcı Address'in NFC kartının arkasında yazılı olmasının nedeni budur. Ancak diğer yuvalar için anahtarları oluşturmak sizin sorumluluğunuzdadır.


Her slot için ana özel anahtar doğrudan Satscard tarafından oluşturulur ve ana zincir kodları dışarıdan sağlanmalıdır. Yeni yuvanızın chain code'si için iki seçeneğiniz vardır: "*Otomatik*" seçeneğini seçerek Nunchuk'un generate'ü otomatik olarak oluşturmasına izin verin veya "*Gelişmiş*" seçeneğini seçip özel alana girerek kendiniz oluşturun. chain code'nin etkili olabilmesi için mümkün olduğunca rastgele olması gerekir.


![SATSCARD](assets/notext/25.webp)


Satscard'ın arkasında belirtilen 6 haneli PIN kodunu girin.


![SATSCARD](assets/notext/26.webp)


Satscard'ınızı telefonunuzun arkasına yerleştirin.


![SATSCARD](assets/notext/27.webp)


Yeni bir slot başarıyla yapılandırıldı. Artık bitcoin yatırmak için alıcı Address'ü görebilirsiniz. Yükleme işlemine devam etmek için, bu eğitimin "*Satscard'a slot nasıl yüklenir? "* bölümündeki talimatları izleyin.

Bu işlemi her bir Satscard için 10 defaya kadar tekrarlayabilirsiniz.


Tebrikler, artık Satscard kullanımını hızlandırdınız! Bu eğitimi faydalı bulduysanız, aşağıya bir beğeni bırakırsanız çok memnun olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!