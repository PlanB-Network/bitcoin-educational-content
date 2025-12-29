---
name: Bitcoin Keeper
description: Güvenlik için Bitcoin mobil wallet ve multi-sig
---

![cover](assets/cover.webp)



Bitcoinlerin güvenli yönetimi, finansal egemenliğin içerdiği risklerin bilincinde olan her kullanıcı için büyük bir zorluk teşkil etmektedir. Mobil bir wallet'nın basitliği ile bir multi-sig çözümünün sağlamlığı arasındaki teknik boşluk birçok kullanıcı için göz korkutucu görünebilir. Bitcoin Keeper tam da bu kesişme noktasında konumlanmış olup, kullanıcılara gelişirken eşlik eden ilerici bir güvenlik yaklaşımı sunmaktadır.



Bitcoin Keeper, BitHyve ekibi tarafından geliştirilen, yalnızca Bitcoin'e adanmış açık kaynaklı bir mobil uygulamadır. Amacı, yeni başlayanlar için sezgisel bir arayüzü korurken, özellikle çoklu imza yapılandırmaları olmak üzere gelişmiş portföy yönetimini erişilebilir kılmaktır. Uygulama, uzun vadeli destek felsefesini yansıtan "Bugün güvende ol, yarın için plan yap" sloganını benimsiyor.



Birden fazla kripto para birimini yöneten genel cüzdanların aksine Bitcoin Keeper, Bitcoin'a sıkı bir şekilde odaklanmaktadır. Yalnızca bitcoin'e yönelik bu yaklaşım, potansiyel saldırı yüzeyini azaltır ve kullanıcı deneyimini büyük ölçüde basitleştirir. Uygulama ayrıca en yaygın donanım cüzdanlarının yerel entegrasyonu ve gelişmiş UTXO yönetim özellikleriyle de öne çıkıyor.



## Bitcoin Keeper nedir?



### Felsefe ve hedefler



Bitcoin Keeper, özel anahtarlarının tam kontrolünü elinde tutmak isteyen bitcoin kullanıcılarının özel ihtiyaçlarını karşılamak üzere tasarlanmıştır. Proje, Bitcoin'ün temel ilkelerini tamamen benimsemektedir: açık ve denetlenebilir kaynak kodu, gizliliğe saygı ve kullanıcı egemenliği. Uygulamayı kullanmak için herhangi bir kayıt veya kişisel bilgi gerekmez ve hatta imzalama işlemleri için çevrimdışı çalışabilir.



Temel amaç, miras işlevleri sayesinde BTC'yi birkaç yıl ve hatta birkaç nesil boyunca saklamak için esnek, geleceğe dönük bir araç sunmaktır. Uygulama, kullanıcıların basitçe bir mobil wallet ile başlamasına ve daha sonra kademeli olarak daha güvenli çoklu imza çözümlerine doğru gelişmesine olanak tanır.



### Uygulama mimarisi



Bitcoin Keeper fon yönetimini iki farklı konsept etrafında düzenler. Hot Wallet**, günlük harcamalar ve mütevazı miktarlar için tasarlanmış, telefonda saklanan basit bir tek anahtarlı wallet'dir. Kasalar**, uzun süreli güvenli depolama için tasarlanmış, bir harcamayı yetkilendirmek için birkaç anahtar gerektiren çoklu imzalı (Çoklu Anahtar) kasalardır.



### Ana Özellikler



Bitcoin Keeper piyasadaki neredeyse tüm donanım cüzdanlarını destekler: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport ve Coinkite'ın Tapsigner'i. Entegrasyon, cihaza bağlı olarak farklı yöntemlerle gerçekleşir: QR kod tarama, NFC bağlantısı veya dosya içe aktarma.



Uygulama ayrıca işlem etiketleme ile gelişmiş UTXO yönetimi, gönderme sırasında girdileri manuel olarak seçmek için jeton kontrolü ve kısmen imzalanmış işlemler için PSBT format desteği sunar.



## Kurulum ve ilk yapılandırma



Bitcoin Keeper, Google Play Store aracılığıyla Android'de ve App Store aracılığıyla iOS'ta ücretsiz olarak kullanılabilir. Listelenen yayıncı BitHyve'dir. Yüklemeden önce, cihazınızın kötü amaçlı yazılım içermediğinden, güncel olduğundan ve root veya jailbreak yapılmadığından emin olun.



İlk açılışta, uygulama sizden bir güvenlik PIN kodu oluşturmanızı ister. Bu kod wallet'inize erişimi korur ve hassas verileri yerel olarak şifreler. Güçlü bir kod seçin ve ezberleyin. Daha sonra kilidi daha hızlı açmak için biyometrik kimlik doğrulamayı (parmak izi veya Face ID) etkinleştirebilirsiniz.



![Installation et configuration du PIN](assets/fr/01.webp)



Uygulama daha sonra üç ayağını açıklayan birkaç tanıtım ekranı sunar: Bitcoin göndermek ve almak için wallet oluşturma, donanım wallet uyumluluğu ile anahtar yönetimi ve bitcoinleri aktarmak için eski planlama. "Başlayın" düğmesine basın, ardından yeni bir yapılandırma oluşturmak için "Yeni Başla "yı seçin.



![Écrans d'introduction](assets/fr/02.webp)



## Arayüzün keşfedilmesi



Bitcoin Keeper'un arayüzü, alt gezinti çubuğundan erişilebilen dört ana sekme etrafında düzenlenmiştir:



![Les quatre onglets de l'application](assets/fr/03.webp)



Cüzdanlar** sekmesi cüzdanlarınızı ve bakiyelerini gösterir. Burası bitcoin göndermek ve almak için cüzdanlarınıza eriştiğiniz yerdir. "Hot Wallet" ve "Tek Anahtarlı" veya "Çok Anahtarlı" etiketleri, her bir wallet'nin türünü hızlı bir şekilde belirlemenizi sağlar.



Anahtarlar** sekmesi imza anahtarlarınızın yönetimini merkezileştirir. Burada uygulama tarafından oluşturulan Mobil Anahtarın yanı sıra donanım cüzdanlarından içe aktarılan tüm anahtarları bulacaksınız. Burası aynı zamanda yeni imza cihazları eklediğiniz yerdir.



Concierge** sekmesi destek hizmetleri sunar: destek ekibine sorularınızı gönderin ve kişiselleştirilmiş yardım için Bitcoin danışmanlarıyla bağlantı kurun.



Daha Fazla** (Diğer Seçenekler) sekmesi kişisel sunucu bağlantısı, anahtar yedekleme, miras belgeleri, ekran tercihleri ve wallet yönetimi gibi ayarlara erişim sağlar.



## Kendi sunucunuza bağlantı



Gizliliğinizi güçlendirmek için Bitcoin Keeper, varsayılan genel sunucuları kullanmak yerine uygulamayı kendi Electrum sunucunuza bağlamanızı sağlar.



![Configuration du serveur Electrum](assets/fr/04.webp)



Diğer sekmesinden, sunucu ayarlarını bulmak için aşağı kaydırın. Yeni bir bağlantı yapılandırmak için "Sunucu Ekle "ye basın. "Genel Sunucu" (önceden yapılandırılmış genel sunucular) ve "Özel Electrum" (kendi sunucunuz) arasında seçim yapabilirsiniz.



Özel bir sunucu için URL'yi (örneğin bir Umbrel düğümü için umbrel.local) ve bağlantı noktası numarasını (genellikle 50001) girin. Sunucunuz destekliyorsa SSL'yi etkinleştirin. Bir yapılandırma QR kodunu da tarayabilirsiniz. Parametreleri girdikten sonra "Sunucuya Bağlan" düğmesine basın.



Henüz kendi Bitcoin düğümünüz yoksa, kendi düğümünüzü atmanın basit ve ekonomik bir yolu olan Umbrel eğitimimize bir göz atın:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Bitcoin alma



Cüzdanlar sekmesinden, tuşuna basarak para almak istediğiniz wallet'ü seçin. wallet ekranında bakiye ve üç işlem düğmesi görüntülenir: Bitcoin Gönder, Bitcoin Al ve Tüm Paraları Görüntüle.



![Réception de bitcoins](assets/fr/05.webp)



"Bitcoin'i Al" düğmesine basın. Bitcoin Keeper, QR kodu ile birlikte Bech32 formatında (bc1... ile başlayan) yeni bir alım adresi oluşturur. Fon kaynağını tanımlamak için bu adrese bir etiket ekleyebilirsiniz. QR kodunu görüntüleyerek veya metin adresini kopyalayarak adresi gönderici ile paylaşın.



Uygulama, gizliliğinizi koruyarak her alım için otomatik olarak yeni bir adres oluşturur. Gerekirse boş bir adres almak için "Yeni Address Al" seçeneğini kullanın.



## UTXO yönetimi



Bitcoin Keeper, bakiyenizi oluşturan UTXO'nin (Harcanmamış İşlem Çıktıları) tam görünürlüğünü sunar. Bir wallet ekranından, köşe yöneticisine erişmek için "Tüm Paraları Görüntüle" düğmesine basın.



![Gestion des UTXO](assets/fr/06.webp)



"Madeni Paraları Yönet" ekranı her bir UTXO'i miktarı ve etiketiyle birlikte ayrı ayrı listeler. Bu görünüm, madeni paralarınızın kaynağını izlemenize ve onları düzenlemenize olanak tanır. Madeni para kontrolü ile göndermek için "Göndermek için Seç" aracılığıyla belirli UTXO'ları seçebilir, böylece farklı menşelerden gelen madeni paraların karışmasını önleyebilirsiniz.



## Bitcoin gönder



Göndermek için kaynak portföyü seçin ve "Bitcoin Gönder "e basın. Hedef adresi girin (yapıştırılmış veya QR kodu ile taranmış) ve isteğe bağlı olarak alıcıyı tanımlamak için bir etiket ekleyin.



![Envoi de bitcoins](assets/fr/07.webp)



Bir sonraki ekran gönderilecek tutarı girmenizi sağlar. Arayüz mevcut bakiyenizi ve fiat para birimi dönüşümünü görüntüler. Şarj önceliğini seçin: Düşük (ekonomi, ~60 dakika), Orta veya Yüksek (öncelik). sats/vbyte cinsinden tahmini ücretler gerçek zamanlı olarak görüntülenir. Devam etmek için "Gönder "e basın.



![Confirmation et envoi](assets/fr/08.webp)



Bir özet ekranı tüm ayrıntıları görüntüler: wallet kaynağı, hedef adresi, işlem önceliği, ağ ücretleri, gönderilen miktar ve toplam. Bitcoin işlemleri geri alınamaz olduğundan lütfen bu bilgileri dikkatlice kontrol edin. İşlemi göndermek için "Onayla ve Gönder" düğmesine basın.



Tam özetle birlikte bir "Başarılı Gönder" onayı görüntülenir. İşlem, etiketiyle birlikte "Son İşlemler" geçmişinde görünür.



## Anahtarlarınızı kaydedin



Kurtarma Anahtarınızı yedeklemek kritik bir adımdır. Diğer sekmesinden "Yedekleme ve Kurtarma" bölümüne gidin ve "Kurtarma Anahtarı "na tıklayın.



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Ekranda yedeklerinizin durumu görüntülenir. Yedeklemenizi doğrulamak için uygulama sizden ifadenizdeki belirli bir kelimeyi (örneğin 7. kelime) onaylamanızı ister. Bu doğrulama, kurtarma cümlenizi doğru bir şekilde yazdığınızdan emin olmanızı sağlar.



"Kurtarma Anahtarı Ayarları "ndan, "Kurtarma Anahtarını Görüntüle" aracılığıyla ifadenizin tamamını görüntüleyebilir ve anahtarınızın İmzalayan Parmak İzini görebilirsiniz. 12 kelimelik cümlenizi kağıt üzerinde, güvenli bir yerde, nemden ve ateşten uzak tutun. Asla bağlı bir cihazda saklamayın.



## Harici bir anahtar ekleyin (wallet donanımı)



Bitcoin Keeper'nin en önemli özelliklerinden biri donanım cüzdanlarının entegrasyonudur. Yeni bir imza cihazı eklemek için Anahtarlar sekmesinden "Anahtar ekle "ye basın.



![Ajout d'une clé hardware](assets/fr/10.webp)



Bir donanım wallet bağlamak için "Donanımdan anahtar ekle "yi seçin. Uygulama geniş bir cihaz yelpazesini destekler: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner ve Specter Solutions.



### Tapsigner yapılandırması



Tapsigner, Coinkite'ın özellikle mobil kullanıma uygun bir NFC kartıdır. Daha fazla bilgi edinmek istiyorsanız, özel bir eğitimimiz var:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Tapsigner'yı eklemek için donanım cüzdanları listesinden seçin.



![Configuration du Tapsigner](assets/fr/11.webp)



Önce kartınızın arkasında basılı olan 6-32 haneli PIN kodunu (yeni kartlarda varsayılan) veya önceden yapılandırılmışsa PIN kodunuzu girin. "Devam" düğmesine basın, ardından "Taramaya hazır" görüntülendiğinde Tapsigner'nizi telefonunuzun arkasına yaklaştırın. NFC iletişimi otomatik olarak genel anahtarı alır. Daha sonra bu anahtarı tanımlamak için bir açıklama (örneğin "Metro Kartı") ekleyebilirsiniz.



## Bir multisig portföyü oluşturun



Anahtarlarınızı ayarladıktan sonra, birkaç cihazı birleştiren çoklu-imzalı bir wallet oluşturabilirsiniz. Cüzdanlar sekmesinden "Wallet Ekle "ye tıklayın.



![Création d'un nouveau wallet](assets/fr/12.webp)



Üç seçeneğiniz vardır: yeni bir portföy için "Wallet Oluştur", mevcut bir wallet'yi geri yüklemek için "Wallet'i İçe Aktar" veya paylaşılan bir kasa için "Ortak Wallet". "Wallet Oluştur" ve ardından "Bitcoin Wallet "i seçin.



![Sélection du type de wallet](assets/fr/13.webp)



Bir sonraki ekran farklı konfigürasyonlar sunar: "Tek tuş", "2'li 3'lü çoklu tuş" veya "3'lü 5'li çoklu tuş". Özelleştirilmiş bir multi-sig için "Özel kurulum seç" düğmesine basın. Örneğin, "1 of 2" seçin: iki olası tuştan tek bir imza gereklidir.



Ardından Kasanızı oluşturacak anahtarları seçin. Örneğimizde "Mobil Anahtar "ı (telefon yazılım anahtarı) "TAPSIGNER" (Metro Kartı) ile birleştiriyoruz. Bu yapılandırma yedeklilik sunar: anahtarlardan birine erişilemezse, paranızı her zaman diğeriyle harcayabilirsiniz.



![Finalisation du wallet multisig](assets/fr/14.webp)



wallet'inizi adlandırın (örneğin "Test PlanıB"), isteğe bağlı bir açıklama ekleyin ve seçilen tuşları kontrol edin. "Wallet'ünüzü Oluşturun" düğmesine basın. wallet kurtarma dosyasını kaydetmenizi hatırlatan bir "Wallet Başarıyla Oluşturuldu" onay mesajı görüntülenir.



Yeni multisig wallet'nız artık Cüzdanlar sekmesinde "Çoklu anahtar" etiketi ve "2'den 1'i" göstergesi ile görünür.



### Yapılandırma dosyasını kaydet



**Kurtarma ifadesinin erişimi geri yüklemek için yeterli olduğu basit bir wallet'den farklı olarak, bir wallet multisig ayrıca kasanın yapısını açıklayan yapılandırma dosyasını da gerektirir (hangi anahtarlar katılır, kaç imza gereklidir). Bu dosya olmadan, tüm kurtarma ifadelerine sahip olsanız bile, wallet'nizi yeniden oluşturamazsınız.



![Export du fichier de configuration](assets/fr/15.webp)



Bu dosyayı dışa aktarmak için Cüzdanlar sekmesinde wallet multisig'inizi seçin, ardından sağ üst köşedeki Ayarlar simgesine (dişli) basın. "Wallet Ayarları "nda "Wallet yapılandırma dosyası "na tıklayın. Çeşitli dışa aktarma seçenekleri mevcuttur:





- PDF Dışa Aktar**: tüm wallet bilgilerini içeren bir PDF belgesi oluşturur
- QR** Göster: yapılandırmayı başka bir cihaza aktarmak için taranabilir bir QR kodu görüntüler
- Airdrop / Dosya Dışa Aktarma**: dosyayı telefonunuzun paylaşım seçenekleri aracılığıyla dışa aktarır
- NFC**: uyumlu bir cihazla NFC aracılığıyla paylaşım



Bu yapılandırma dosyasını kurtarma ifadelerinizden ayrı olarak, ideal olarak şifrelenmiş veya basılı bir ortamda saklayın. Telefonunuzu kaybederseniz, bu dosya her bir katılımcı anahtar için kurtarma ifadeleriyle birlikte wallet multisig'inizi Bitcoin Keeper veya başka bir uyumlu yazılım üzerinde yeniden oluşturmanızı sağlayacaktır.



## En iyi uygulamalar



### Fon organizasyonu



Bitcoinlerinizi kullanımlarına göre yapılandırın: sınırlı miktarlardaki cari harcamalar için sıcak bir wallet Tek Anahtar ve uzun vadeli tasarruflar için bir veya daha fazla Kasa Çoklu Anahtar. Sistematik UTXO etiketleme, fonlarınızın nereden geldiğini takip etmenize yardımcı olacaktır; bu, gizliliği yönetmek ve farklı kökenlerden gelen coinleri karıştırmaktan kaçınmak için özellikle yararlıdır.



Telefonunuzu güvende tutun: biyometrik kilidi etkinleştirin, sistem güncellemelerini düzenli olarak yapın ve yüklü uygulamalar konusunda dikkatli olun. Ve Bitcoin Keeper'i güvenlik yamaları ile güncel tutun.



### Yedek güvenlik



Her kurtarma ifadesinin en az iki kopyasını coğrafi olarak ayrı yerlerde saklanan kağıt üzerinde tutun. Büyük meblağlar için kazınmış, felaketlere dayanıklı metal kullanmayı düşünün. Bu ifadeleri asla internete bağlı bir cihazda saklamayın ve asla fotoğraflarını çekmeyin.



multi-sig Kasaları için, katılımcı açık anahtarları ve kasa yapısını içeren yapılandırma dosyasını (Wallet Kurtarma Dosyası) da kaydedin. Bu dosya, anahtar kurtarma ifadeleriyle birlikte, wallet'un Sparrow veya Spectre gibi herhangi bir uyumlu yazılımda yeniden oluşturulmasını sağlar.



## Avantajlar ve sınırlamalar



### Önemli Noktalar





- Yalnızca Bitcoin uygulaması karmaşıklığı ve riski azaltır
- Adım adım rehberlik ile multisig Kasaların yerel entegrasyonu
- Genişletilmiş donanım wallet desteği (Tapsigner, Coldcard, Ledger, Jade, vb.)
- Gelişmiş UTXO yönetimi ve madeni para kontrolü
- Kişisel bir Electrum sunucusuna bağlanabilir
- Açık, denetlenebilir kaynak kodu



### Dikkate alınması gereken kısıtlamalar





- Interface ağırlıklı olarak İngilizce
- Bazı premium özellikler (Cloud Backup, Assisted Server) yükseltme gerektirir
- Multisig yapılandırması başlangıç eğitimi gerektirir



## Sonuç



Bitcoin Keeper, bitcoinlerinizi yönetmek için ölçeklenebilir bir çözüm olarak öne çıkıyor. Basit sıcak wallet'den çoklu imza Kasalarına kadar ilerici yaklaşımı, ihtiyaçlar değiştikçe güvenliğin yükseltilebileceği anlamına gelir. Tapsigner gibi donanım cüzdanlarını kolayca entegre edebilme özelliği, aşırı karmaşıklık olmadan sağlam yapılandırmaların önünü açar.



Yalnızca bitcoin yönelimi, açık kaynak kodu ve gizliliğe saygı, onu Bitcoin ekosisteminin temel değerleriyle uyumlu bir seçim haline getirmektedir.



Bu eğitim Bitcoin Keeper'ün ücretsiz sürümündeki temel özelliklerini kapsamaktadır. Uygulama ayrıca özel bir eğitimin konusu olacak premium özellikler (Bulut Yedekleme, Destekli Sunucu Yedekleme, Kanarya Cüzdanlar) sunmaktadır. Gelecek bir rehberde, uygulamaya entegre edilmiş Gelişmiş Kasalar ve beraberindeki belgeler sayesinde bitcoinlerinizin sevdiklerinize aktarımını hazırlamanıza olanak tanıyan Miras Planlama özelliğini de inceleyeceğiz.



## Kaynaklar





- Resmi web sitesi: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Yardım Merkezi: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Kaynak kodu: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)