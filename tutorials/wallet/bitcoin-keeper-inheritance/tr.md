---
name: Bitcoin Keeper - Miras planı
description: Bitcoin Keeper ile bitcoin iletiminizi planlayın
---

![cover](assets/cover.webp)



Bitcoin varlıklarının devri, sahipler tarafından en hafife alınan zorluklardan biridir. Finans kurumunun fonları yasal varislere aktarabildiği bir banka hesabının aksine, Bitcoin tamamen özel anahtarlara sahip olmaya dayanır. Tamamen meşru bir yasal varis bu anahtarlar olmadan fonlara asla erişemezken, sırları elinde bulunduran kötü niyetli bir kişi herhangi bir formalite olmadan fonları harcayabilecektir.



Bu ikinci Bitcoin Keeper eğitiminde, emlak planlamasına adanmış premium özellikleri keşfediyoruz. Uygulama, Miniscript sayesinde zamanlanmış koruma mekanizmaları ile Gelişmiş Kasalar oluşturmak için gelişmiş araçlar ve sevdiklerinize rehberlik etmek için eşlik eden belgeler sunar.



Bu kılavuz, ilk eğitimimizde açıklandığı gibi Bitcoin Keeper'ün temellerini (portföy oluşturma, klasik multisig, donanım anahtarları ekleme) zaten öğrendiğinizi varsayar:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper abonelik planları



Bitcoin Keeper, aşamalı işlevsellik sunan üç abonelik seviyesine sahip bir freemium modelinde çalışır. Planlara erişmek için **Daha Fazla** sekmesine gidin, ardından **Aboneliği Yönet** ekranını açmak için mevcut planınıza (varsayılan olarak "Pleb") dokunun.



![Plans d'abonnement](assets/fr/01.webp)



Pleb planı** (ücretsiz) temel özelliklere erişim sağlar: tek anahtarlı ve çok anahtarlı cüzdanların sınırsız oluşturulması, tüm büyük donanım cüzdanlarıyla uyumluluk (Coldcard, Trezor, Ledger, Jade, Tapsigner...), jeton kontrolü, etiketleme ve kişisel bir Electrum sunucusuna bağlantı. Bu plan standart kullanım ve hatta klasik multi-sig konfigürasyonları için yeterlidir.



Hodler planı** (aylık 9,99 €, yıllık ödenirse 1 ay ücretsiz) tüm Pleb özelliklerini içerir ve kasalarınızı herhangi bir cihazda geri yüklemek için buluta (iCloud veya Google Drive) şifreli yedeklemeler, otomatik harcama politikaları ve belirli bir eşiğin üzerinde 2FA eklemek için Sunucu Anahtarı ve anahtarlarınıza yetkisiz erişimi tespit etmek için Kanarya Cüzdanları ekler.



Elmas Eller planı** (ayda 29,99 €, yıllık ödeme yapılırsa 1 ay ücretsiz) miras planlaması için eksiksiz bir pakettir. Tüm Hodler planını içerir ve Miras Anahtarının (ertelenmiş aktivasyon), Acil Durum Anahtarının (kayıp durumunda kurtarma için acil durum anahtarı), Miras Planlama araçlarının ve belgelerinin kilidini açar ve yapılandırmanızı doğrulamak için Concierge ekibiyle bir destek görüşmesi yapar. Bu, miraslarını birkaç nesil boyunca aktarmak isteyen bitcoin kullanıcıları için bir tekliftir.



Önemli nokta: Oluşturduğunuz kasalar, ücretsiz plana geri dönseniz bile erişilebilir kalacaktır. Yapılandırmalarınız açık standartlara (BSMS, Miniscript) dayanır ve aboneliğinizden bağımsız olarak çalışır.



## Miras belgeleri



Diamond Hands aboneliğinizi etkinleştirdikten sonra, Diğer sekmesinden **Miras Belgeleri** bölümüne erişin. Bitcoin Keeper, emlak planınızı yapılandırmak için beş örnek belgenin yanı sıra bir ipuçları bölümü de sunmaktadır:



![Documents d'héritage](assets/fr/02.webp)





- Tohum Kelimeler Şablonu**: kurtarma ifadelerinizi düzenli bir şekilde not almanız için bir şablon
- Güvenilir Kişiler**: planınıza dahil olan güvenilir kişilerin (noter, avukat, varisler, anahtarcılar) iletişim bilgilerini listelemek için bir şablon
- Ek Paylaşım Anahtarı**: her bir anahtar için teknik bilgileri detaylandıran bir belge: PIN kodu, türetme yolu, fiziksel konum, cihaz türü ve anahtarın tanımlanması ve kullanılması için yararlı olan diğer bilgiler
- Geri Alma Talimatları**: varis veya lehtarın fonları geri alması için adım adım talimatlar
- Avukata Mektup**: avukatınız veya noteriniz için uyarlanabilecek önceden doldurulmuş bir mektup



Miras İpuçları** bölümü, mirasçılar için anahtarları güvence altına alma ve miras planınızı optimize etme konusunda pratik tavsiyeler sunar.



Bu belgeleri durumunuza uyacak şekilde özelleştirin ve anahtarlardan ayrı olarak güvenli bir yerde saklayın.



## Bulut Yedeklemeyi Yapılandırma



Eski kasanızı oluşturmadan önce, yapılandırma dosyalarınızı korumak için bulut yedeklemeyi etkinleştirin. Diğer sekmesinden **Kişisel Bulut Yedekleme** öğesine basın.



![Configuration Cloud Backup](assets/fr/03.webp)



Yedeklerinizi şifrelemek için güçlü bir parola seçin. Bu parola yalnızca wallet yapılandırma dosyalarını korur (özel anahtarlarınızı değil). Parolayı onaylayın ve **Onayla** düğmesine basın. Yedeklemeleriniz cihazınıza bağlı olarak iCloud veya Google Drive'da saklanacaktır. İlk yedeklemenizi başlatmak için **Şimdi Yedekle** düğmesine basın.



## Donanım anahtarlarınızı içe aktarın



Örneğimiz için, iki ek anahtarla (Miras ve Acil Durum) 3'te 2'lik bir kasa oluşturacağız. Gerekli tüm anahtarları **Anahtarlar** sekmesine aktararak başlayalım.



![Import des clés hardware](assets/fr/04.webp)



Bir donanım wallet bağlamak için **Tuş ekle** tuşuna basın, ardından **Bir donanımdan tuş ekle** öğesini seçin. Bitcoin Keeper birçok cihazı destekler: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ve Specter Solutions.



Yapılandırmamızda, :




- 2 **Coldcard** anahtarı (MK4SP ve MK4)
- 2 anahtar **Tapsigner** (Metro ve Genesis)



Bir Coldcard eklemek için listeden seçin ve açık anahtarı QR kodu, dosya, USB veya NFC aracılığıyla dışa aktarmak için ekrandaki talimatları izleyin. Bir Coldcard veya Tapsigner'ün nasıl kullanılacağı hakkında daha fazla bilgi için lütfen özel eğitimlerimize bakın:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Tüm anahtarlarınız içe aktarıldıktan sonra, bunları özel adlarıyla birlikte Anahtarlar sekmesinde bulabilirsiniz.



## Eski wallet'ü oluşturun



Bagaj oluşturmaya geçelim. Cüzdanlar** sekmesinden **Wallet** Ekle'ye basın, **Bitcoin Wallet**'yı seçin, ardından **Wallet** Oluştur'a basın.



![Création du wallet](assets/fr/05.webp)



wallet türünü seçin. Eski planımız için **2'li 3 çoklu anahtar** seçeneğini seçin. Ekranın alt kısmında **Gelişmiş Güvenlik Seçenekleri** seçeneğini etkinleştirin ve ardından **İlerle** düğmesine basın.



![Options de sécurité avancées](assets/fr/06.webp)



Gelişmiş Güvenlik Seçenekleri açılır penceresinde işaretleyin:




- Kalıtım Anahtarı**: belirli bir süre sonra çekirdeğe eklenecek ek bir anahtar
- Acil Durum Anahtarı**: anahtar kaybı durumunda fonları kurtarmak için ertelenmiş tam kontrole sahip bir anahtar



Değişiklikleri Kaydet** düğmesine basın. Ardından içe aktarılanlar arasından wallet'unuzu oluşturacak 3 anahtarı seçin (örn. Tohum Anahtarı, Coldcard MK4SP ve Tapsigner Metro).



## Özel önemli son tarihlerin belirlenmesi



Bir sonraki ekran Acil Durum Anahtarını ve Miras Anahtarını yapılandırmanızı sağlar. Bu özel anahtarların etkinleştirilmesini yöneten gecikmeleri tanımladığınız yer burasıdır.



![Configuration des délais](assets/fr/07.webp)



Acil Durum Anahtarı** için nihai yedekleme görevi görecek donanım anahtarını seçin (burada Coldcard MK4) ve aktivasyon gecikmesini seçin (örneğimizde: 2 yıl). Miras Anahtarından farklı olarak, Acil Durum Anahtarı yeter sayıya eklenmez: **multisig'i** tamamen atlamanıza izin verir ve zaman sınırı dolduktan sonra fonlar üzerinde tam kontrol sahibi olmanızı sağlar. Bu sizin son çare çözümünüzdür: birkaç anahtar kaybolur veya yok edilirse, bu tek anahtar her şeyi kurtarmanızı sağlar. Bu nedenle son derece titizlikle korunmalıdır.



Miras Anahtarı** için, mirasçı için tasarlanan anahtarı (burada Coldcard MK4SP) seçin ve gecikmeyi seçin (örneğimizde: 1 yıl). Hareketsiz geçen bir yılın ardından bu anahtar **imza yeter sayısına** eklenecektir. Pratik anlamda, wallet 2-of-3'ünüz bu süre geçtikten sonra bir wallet 2-of-4 haline gelecek ve varisin mevcut anahtarlarla birlikte imzaya katılmasını sağlayacaktır.



### Zaman saatleri nasıl çalışır?



Bitcoin Keeper, Miniscript tarafından mümkün kılınan **mutlak zaman kilitlerini** (CLTV - CheckLockTimeVerify) kullanır. Her UTXO alındığında başlayan göreceli zaman kilitlerinin (CSV) aksine, mutlak zaman kilitleri wallet oluşturulduğunda tanımlanan **sabit bir son kullanma tarihi** ile çalışır.



Somut olarak, bugün 1 yıllık bir Miras Anahtarı ile bir wallet oluşturursanız, aktivasyon tarihi "bugün + 1 yıl" olacaktır. Bu wallet'e yatırılan tüm fonlar, yatırılma tarihleri ne olursa olsun, aynı tarihte Miras Anahtarı aracılığıyla erişilebilir olacaktır.



Mutlak zaman saatlerinin avantajı, 15 ayın üzerinde teslim sürelerine (göreceli CSV zaman saatlerinin sınırı) izin vermesidir, bu da Bitcoin Keeper'in neden 2 yıl gibi seçenekler sunabildiğini açıklar.



### Yenileme mekanizması



Yaşam süreniz boyunca özel anahtarların etkinleştirilmesini önlemek için wallet'nızı periyodik olarak "yenilemeniz" gerekir. Mutlak zaman kilitleri ile bu, **wallet'yı geleceğe itilmiş yeni bir son kullanma tarihi** ile yeniden oluşturmayı ve ardından fonlarınızı bu yeni wallet'ya aktarmayı içerir.



Bitcoin Keeper entegre bir yenileme fonksiyonu ile bu süreci basitleştirir. Uygulama karmaşıklığı arka planda otomatik olarak ele alır: manuel olarak yeni bir wallet oluşturmanıza veya fonları kendiniz aktarmanıza gerek kalmadan yönlendirilen adımları izlemeniz yeterlidir. Bu işlemi, yapılandırılan en kısa zaman diliminin sona ermesinden çok önce düzenli olarak planlayın. Örneğin, 1 yıllık bir Miras Anahtarı ile, güvenlik marjını korumak için her 9-10 ayda bir yenileyin.



## Yapılandırmayı kaydetme ve dışa aktarma



wallet oluşturulduktan sonra, uygulama size yapılandırma dosyasını kaydetmenizi hatırlatır. **Bu adım kritiktir**: bu dosya olmadan mirasçılarınız wallet multisig'i yeniden oluşturamayacaktır.



![Export de la configuration](assets/fr/08.webp)



Wallet Kurtarma Dosyasını Yedekle** öğesine basın. Çeşitli dışa aktarma seçenekleri mevcuttur:




- PDF dışa aktarma**: tüm wallet bilgilerini içeren eksiksiz bir belge oluşturur
- QR** Göster: yapılandırmayı başka bir cihaza aktarmak için bir QR kodu görüntüler
- Airdrop / Dosya Dışa Aktar**: dosyayı paylaşım seçenekleri aracılığıyla dışa aktarır
- NFC**: uyumlu bir cihazla NFC aracılığıyla paylaşım



Kopyaları çoğaltın: biri noterde, biri banka kasasında, biri de şifrelenmiş dijital versiyonda. Yeni wallet'niz artık Cüzdanlar sekmesinde "Çoklu anahtar", "3'ün 2'si", "Miras anahtarı" ve "Acil durum anahtarı" etiketleriyle görünür.



## Bir Wallet Kanarya Oluşturun



Canary Wallet bir erken uyarı sistemidir. Fikir: wallet çoklu anahtarında kullanılan her anahtar ayrı bir wallet tekli anahtarında da kullanılabilir. Bu wallet "kanaryasına" küçük bir meblağ yatırıldığında, herhangi bir yetkisiz hareket anahtarın tehlikeye girdiğine işaret eder.



![Canary Wallets](assets/fr/09.webp)



Bir Wallet Kanaryasını yapılandırmanın iki yolu vardır. Daha Fazla** sekmesinden "Anahtarlar ve Cüzdanlar" bölümündeki **Kanarya Cüzdanları** seçeneğine basın. Ekranda prensip açıklanmaktadır: Birisi anahtarlarınızdan birine erişir ve ilişkili wallet tek anahtarında para bulursa, bunları kaldırmaya çalışacak ve bu da sizi uyaracaktır.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Kanarya'yı doğrudan bir tuştan da yapılandırabilirsiniz. Anahtarlar** sekmesinde bir anahtar seçin (örn. Tapsigner Genesis), **Ayarlar** (dişli) simgesine ve ardından **Kanarya Wallet** simgesine basın. İlgili wallet kanaryası açılır ve bazı gözetim satoshilerini almaya hazırdır.



Her bir Kanarya Wallet'ye küçük bir miktar (birkaç bin satoshi) yatırın. Bu fonlar sizin onayınız olmadan hareket ederse, ele geçirilen anahtarı derhal multisig kasalarınızdan çıkarın.



## En iyi uygulamalar



**Yapılandırmanızı** büyük bir meblağ koymadan önce küçük bir miktar para ile test edin. Kasaya birkaç bin satoshi gönderin, ardından her bir cihazla imzalama işleminde ustalaştığınızı kontrol etmek için giden bir harcama yapmayı deneyin. Ayrıca yedeklemenin çalıştığından emin olmak için yapılandırma dosyasını başka bir telefona aktarmayı test edin.



**Anahtarları akıllıca dağıtın**. Tapsigner'lar için, PIN ayrı olarak iletilerek (örneğin başka bir yerde saklanan Kurtarma Talimatları mektubunda) kapalı bir zarf içinde teslim edin. Klasik donanım cüzdanları için cihazı güvenilir bir üçüncü şahısta ve seed'ü kağıt veya metal üzerinde sizde veya başka bir üçüncü şahısta tutun. Karışıklığı önlemek için her bir anahtarın parmak izini ve yapılandırma dosyasındaki adını not edin.



**Periyodik testler** planlayın (yangın tatbikatları). Yıllık olarak, kasayı boş bir telefonda yedeklerden yeniden oluşturabileceğinizi kontrol edin. Bakiyeleri kontrol ederek Kanarya uyarılarını test edin. Kalan anahtar kombinasyonlarının yeterli olduğunu doğrulamak için kayıp senaryolarını simüle edin ("Coldcard'ı kaybedersem ne olur?").



**Yenilemeyi unutmayın**. Miras Anahtarınızı 1 yıl olarak ayarladıysanız, her 9-10 ayda bir yenileyin. Bu, üçüncü taraf müdahalesi olmadan otomatik iletim için ödediğiniz bedeldir.



**Planı güncel tutun**. Herhangi bir değişiklik (bir anahtarın değiştirilmesi, mirasçıların değiştirilmesi, son tarihin değiştirilmesi) tüm yedeklere ve belgelere yansıtılmalıdır. Her değişiklikten sonra PDF'leri yeniden oluşturun ve yeni sürümleri yeniden dağıtın.



## Sınırlar ve dikkat edilmesi gerekenler



Bu araçların gücüne rağmen, onları mümkün olduğunca etkili bir şekilde yönetmek için sınırlamalarını tanımak önemlidir.



Zaman kilitli bir multisig kasanın **karmaşıklığı** başlı başına bir risk olabilir: yanlış yapılandırma, varisler tarafından yanlış anlaşılma, birçok bileşen arasında kritik bir unsurun kaybı. Bitcoin Keeper deneyimi mümkün olduğunca basitleştirir, ancak teknik bir işlem olmaya devam eder. Bu planı yalnızca korunacak miktar bunu haklı çıkarıyorsa uygulayın. Küçük miktarlar için daha basit bir plan yeterli olabilir.



Uygulama bağımlılığı** üzerinde düşünmeye değer. Kod açık kaynak olmasına ve açık standartlara (Miniscript, BSMS) dayanmasına rağmen, bazı işlevler Keeper ekosistemine bağlıdır. Uygulamanın bir kopyasını (Android APK veya iOS IPA) saklayın ve mirasçılara mektuplarınızda fonları kurtarmak için diğer Miniscript uyumlu cüzdanları (Liana gibi) kullanma olasılığını belgeleyin.



Güvenilir aracılar** insani bir risk oluşturur. Kötü niyetli bir akrabanız kendisine emanet edilen anahtarı son teslim tarihinden önce kullanırsa ne olur? Ya da avukat belgelerinizi yanlış yere koyarsa? Bu kişileri dikkatli seçin, sorumluluklarını net bir şekilde açıklayın ve bir B planınız olsun. Kanarya Cüzdanlar, yedek yedekler ve multisig'in yapısı bu tehlikelere karşı en iyi korumanız olmaya devam ediyor.



## Sonuç



Bitcoin Keeper, Diamond Hands planı ile emlak planlaması için eksiksiz bir araç kutusu sunar: Zaman ayarlı anahtarlara sahip Geliştirilmiş Kasalar, eşlik eden belgeler, Kanarya Cüzdanları ve kişiselleştirilmiş destek.



Bu sadece teknik bir mesele değildir: mirasınızın mimarisini tasarlama, anahtarları ve bilgiyi akıllıca dağıtma ve sistemi düzenli olarak test etme meselesidir. İyi tasarlanmış bir Bitcoin miras planı, satoshilerinizi gerçek, devredilebilir bir mirasa dönüştürür.