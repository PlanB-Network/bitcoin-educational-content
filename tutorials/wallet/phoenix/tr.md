---
name: Phoenix
description: Phoenix Wallet'ı yükleme ve kullanma
---
![cover](assets/cover.webp)


![video](https://youtu.be/TpwnoPUyumA)


Phoenix, Lightning tabanlı yazılım çözümlerinde uzmanlaşmış bir Fransız şirketi olan ACINQ tarafından geliştirilen, kendi kendine emanet edilebilen bir Lightning Wallet ve düğümüdür. Bitcoinlerin üçüncü bir tarafça tutulduğu Wallet Satoshi gibi emanet Lightning cüzdanlarının aksine Phoenix, kullanıcıların özel anahtarlarının tam kontrolünü ellerinde tutmalarını sağlar.


Phoenix, telefonunuza gömülü gerçek bir Lightning düğümü olarak çalışır ve ACINQ'nun Lightning düğümü ile otomatik olarak bir kanal açar. Uygulama, mobil cüzdanlar için optimize edilmiş, Kotlin'de Lightning Network'ün platformlar arası bir uygulaması olan Lightning-KMP'ye dayanmaktadır. Diğer Lightning düğümü çözümlerinden farklı olarak Phoenix, yönetimi büyük ölçüde basitleştirir. Kullanıcının kanal açma ve kapama işlemlerini gerçekleştirmesi, bir Bitcoin düğümü çalıştırması veya Lightning Network üzerindeki likiditeyi yönetmesi gerekmez. Phoenix tüm bu teknik işlemleri arka planda halleder.


Bu uygulama, mobil Lightning cüzdanlarının kullanım kolaylığı ve rahatlığını gerçek bir kişisel Lightning düğümünün güvenliği ve egemenliği ile birleştirir. Phoenix, akıcı ve sezgisel bir kullanıcı deneyiminin keyfini çıkarırken Lightning Network'in güvenli, verimli ve otonom bir şekilde kullanılmasını mümkün kılar.


Karşılığında belirli ücretler uygulanır:




- Yıldırım ile göndermenin maliyeti tutarın %0,4'ü artı 4 Sats'dır;
- Lightning aracılığıyla almak için nakit gerekiyorsa, tutarın %1'i tahsil edilir;
- Her bir kanalın açılma maliyeti 1000 Sats'dir.


Bence Phoenix, emanet Lightning cüzdanları ile bir Lightning düğümünün manuel yönetimi arasında mükemmel bir ara çözümü temsil ediyor. Bu uygulama, kendi LND veya Core Lightning'lerini yönetmenin ayrıntılarıyla uğraşmayı tercih etmeyen yeni başlayanlar ve ileri düzey kullanıcılar için eşit derecede uygundur. Nasıl kullanılacağını öğrenelim!


![Image](assets/fr/01.webp)


## Uygulamayı yükleyin


Uygulama mağazanıza gidin ve Phoenix'i yükleyin:




- Google Play Store]'da (https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet);
- App Store]'da (https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB).


![Image](assets/fr/02.webp)


Uygulamayı [GitHub depolarındaki apk dosyası ile] de yükleyebilirsiniz (https://github.com/ACINQ/phoenix/releases).


![Image](assets/fr/03.webp)


## Portföy oluşturma


Uygulama başladıktan sonra, sunumu atlamak için "*Sonraki*" düğmesine ve ardından "*Başlat*" düğmesine tıklayın.


![Image](assets/fr/04.webp)


"*Yeni bir Wallet* oluştur" öğesini seçin.


![Image](assets/fr/05.webp)


İşte bu kadar, Lightning Wallet'niz ve düğümünüz artık oluşturulmuştur.


![Image](assets/fr/06.webp)


## Mnemonic ifadesini kaydedin


Başlamadan önce, 12 kelimelik Mnemonic cümlemizi kaydetmemiz gerekiyor. Bu ifade tüm bitcoinlerinize tam ve sınırsız erişim sağlar. Bu cümleye sahip olan herhangi biri, telefonunuza fiziksel erişimi olmasa bile paranızı çalabilir.


12 kelimelik ifade, telefonunuzun kaybolması, çalınması veya kırılması durumunda bitcoinlerinize erişimi geri kazandırır. Bu nedenle dikkatli bir şekilde kaydetmeniz ve güvenli bir yerde saklamanız çok önemlidir.


Bunu kağıda yazabilir veya daha fazla güvenlik için yangından, selden veya çökmeden korumak için paslanmaz çelik üzerine kazıyabilirsiniz. Mnemonic'iniz için ortam seçimi güvenlik stratejinize bağlı olacaktır, ancak Phoenix'i orta miktarda içeren bir Wallet harcaması olarak kullanıyorsanız, kağıt yeterli olacaktır.


Mnemonic ifadenizi kaydetmenin ve yönetmenin doğru yolu hakkında daha fazla bilgi için, özellikle de yeni başlayan biriyseniz, bu diğer öğreticiyi izlemenizi şiddetle tavsiye ederim:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Interface'in üst kısmında görüntülenen "*Wallet'unuzu kaydedin...*" mesajına tıklayın.


![Image](assets/fr/07.webp)


Ardından "*Wallet'mi kaydet*" üzerine tıklayın.


![Image](assets/fr/08.webp)


Ardından "*Anahtarımı görüntüle*" seçeneğine tıklayın ve Mnemonic ifadenizi fiziksel bir ortama kaydedin.


![Image](assets/fr/09.webp)


Yedeklemenin başarıyla tamamlandığını onaylamak için Interface'nin altındaki iki kutuyu işaretleyin.


![Image](assets/fr/10.webp)


## Uygulama kurulumu


İlk işlemlerinizi yapmadan önce, Interface'ün sol alt tarafındaki dişli çark simgesine tıklayarak ayarları özelleştirebilirsiniz.


![Image](assets/fr/11.webp)


"*Görüntü*" menüsünde uygulama temasını, Bitcoin için kullanılan kupürü ve yerel fiat para biriminizi seçebilirsiniz.


![Image](assets/fr/12.webp)


"*Ödeme seçenekleri*" bölümünde, Lightning ödemeleri için çeşitli gelişmiş ayarlar bulacaksınız. Varsayılan ayarları koruyabilirsiniz.


![Image](assets/fr/13.webp)


"*Kanal yönetimi*" bölümünde, bir Lightning kanalı açarken ödemeye hazır olduğunuz maksimum ücreti ayarlayın.


![Image](assets/fr/14.webp)


"*Erişim kontrolü*" menüsünde, telefonunuzdaki uygulamaya erişimi güvence altına almak için bir kimlik doğrulama sistemini etkinleştirmenizi şiddetle tavsiye ederim. Bu, kilidi açık telefonunuza erişimi olan herhangi birinin Phoenix'e erişmesini ve bitcoinlerinizi çalmasını önleyecektir.


![Image](assets/fr/15.webp)


"*Electrum server*" menüsünde, eğer bir Electrs sunucunuz varsa, işlemlerinizi yayınlamak için ona bağlanabilirsiniz.


![Image](assets/fr/16.webp)


Bağlantılarınızın gizliliğini artırmak için "*Tor*" menüsünden Tor üzerinden bağlantıları etkinleştirin. Tor kullanmak ödemelerinizi biraz yavaşlatsa ve alım sırasında Phoenix uygulamasının ön planda açık olmasını gerektirse de, gizliliğinizi önemli ölçüde artırır.


![Image](assets/fr/17.webp)


## On-Chain bitcoinleri alın


İlk kullanımda, Phoenix Wallet'nizi On-Chain fonlarıyla yükleme seçeneğiniz vardır. Bu ilk para yatırma işlemini doğrudan Lightning'den de yapabilirsiniz (sonraki bölüme bakın), ancak her iki durumda da ilk kanalınızı açmak için ek ücretler uygulanacaktır.


"*Receive*" düğmesine tıklayın.


![Image](assets/fr/18.webp)


Bitcoin alan bir Address'i ortaya çıkarmak için QR kodunu sola kaydırın. Phoenix'e yatırmak istediğiniz tutarı bu Address'e gönderin.


![Image](assets/fr/19.webp)


On-Chain ile alınan tutar ilk olarak Wallet bakiyenizin altında beklemede olarak görünecektir. Fonların kullanıma hazır hale gelmesi 3 onay alacaktır.


![Image](assets/fr/20.webp)


Para alındıktan sonra, Phoenix sizin için otomatik olarak bir Lightning kanalı açar. Artık Lightning Network üzerinden bitcoin gönderebilir ve alabilirsiniz.


![Image](assets/fr/21.webp)


## Lightning aracılığıyla bitcoin alın


Sats'ü Lightning Network üzerinden almak için "*Al*" düğmesine tıklayın.


![Image](assets/fr/22.webp)


Phoenix bir Yıldırım Invoice oluşturur. Bunu tarayabilir ya da Sats'yı size transfer etmek isteyen kişiye gönderebilirsiniz.


![Image](assets/fr/23.webp)


"*Düzenle*" düğmesine tıklayarak, Invoice üzerinde ödeyenin görebileceği bir açıklama ekleyebilir ve ödeyenin göndermesi gereken belirli bir tutarı tanımlayabilirsiniz.


![Image](assets/fr/24.webp)


Yukarıda belirtilen klasik faturalar yalnızca bir kez kullanılabilir. Yeniden kullanılabilir bir ödeme seçeneği için, bir BOLT12 teklifi olan yeniden kullanılabilir QR kodunuzu kullanabilirsiniz.


![Image](assets/fr/25.webp)


Invoice veya BOLT12 teklifi sonuçlandırıldığında, işlem Yıldırım Wallet'unuzda görünecektir.


![Image](assets/fr/26.webp)


## Lightning aracılığıyla bitcoin gönderme


Artık Phoenix'te Sats'e sahip olduğunuza göre, Lightning Network aracılığıyla ödeme yapmaya hazırsınız. "*Gönder*" düğmesine tıklayarak başlayın.


![Image](assets/fr/27.webp)


Sizin için çeşitli seçenekler mevcuttur. "*Karekod tara*" seçeneğine tıklayarak bir Lightning Invoice, bir BOLT12 teklifi veya hatta On-Chain ödemesi için bir alıcı Address tarayabilirsiniz.


![Image](assets/fr/28.webp)


Bu bilgileri Interface'in üst kısmındaki alana klavye aracılığıyla manuel olarak da girebilir veya bir Yıldırım Address (BOLT12 veya LNURL) girebilirsiniz. Ayrıca "*Yapıştır*" düğmesini kullanarak bilgileri doğrudan yapıştırabilirsiniz.


![Image](assets/fr/29.webp)


Bu örnek için, 10.000 Sats karşılığında bir Invoice taradım. Ödemeyi yapmak için "*Öde*" butonuna tıklamanız yeterlidir.


![Image](assets/fr/30.webp)


İşlem tamamlanmıştır.


![Image](assets/fr/31.webp)


Tebrikler, artık Phoenix'i nasıl yapılandıracağınızı ve kullanacağınızı biliyorsunuz. Bu öğreticiyi yararlı bulduysanız, aşağıya bir Green başparmak bırakırsanız minnettar olurum. Bu makaleyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Paylaştığınız için teşekkürler!


İşleri bir adım öteye taşımak için, kendi Lightning düğümünüzü başlatmaya yönelik bir başka yenilikçi ve kullanımı kolay çözüm olan Alby Hub hakkındaki bu eğitime göz atın:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Lightning Network'nin teknik çalışması hakkında daha fazla bilgi edinmek için Fanis Michalakis'in Plan ₿ Network ile ilgili mükemmel ücretsiz eğitimini bulabilirsiniz:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb