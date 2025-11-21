---
name: BTCPay Sunucusu
description: BTC ödemelerini aracılar olmadan kabul etme
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server, Nicolas Dorier tarafından oluşturulan ve bitcoin ödemelerinin aracılar olmadan kabul edilmesini sağlayan ücretsiz, açık kaynaklı bir yazılım paketidir. Özerklik ve finansal egemenlik sunmak üzere tasarlanan bu yazılım kendi sunucusuna kurulur ve faturalamadan on-chain veya Lightning Network ödemelerinin doğrulanmasına ve muhasebeye kadar eksiksiz bir işlem yönetimi sağlar. E-ticaret siteleriyle (WooComerce, Shopify, vb.) kolayca entegre olur veya fiziksel mağazalar (*POS*) için bir ödeme terminali olarak kullanılabilir.



BTCPay Server, bitcoin kabul etmek isteyen tüccarlar için şüphesiz en gelişmiş çözümdür. Güvenlik, egemenlik ve gizlilik açısından en kapsamlı ve sağlam yazılımdır. Öte yandan, kurulumu ve bakımı da en karmaşık olanıdır. Daha basit alternatifler de vardır: OpenNode gibi bazıları tamamen emanetçidir, diğerleri ise Swiss Bitcoin Pay gibi kullanım kolaylığı ve egemenlik arasında ilginç bir uzlaşma sunar:



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Bu eğitimin amacı, BTCPay Sunucusunun kurulumu, yapılandırılması ve kullanımı konusunda size adım adım rehberlik etmektir, böylece Bitcoin ethosuna uygun olarak güvenli, bağımsız bir ödeme altyapısı kurabilirsiniz.



## BTCPay Sunucu özellikleri



Örneğin *OpenNode* gibi merkezi Bitcoin satış noktası çözümleri kullanım kolaylığı sunar, ancak kendi kendine barındırılamadıkları ve çoğu durumda tescilli oldukları için üçüncü taraf bir şirkete güvenirler. Ödemelerin ayarlanmasını kolaylaştırsalar da, komisyon ücretleri içerirler ve kullanıcılarını hem fonların saklanması hem de gizlilik açısından BTCPay Server gibi bir çözümden daha fazla riske maruz bırakırlar.



BTCPay Sunucusu, bitcoin cinsinden bağış almak isteyen çevrimiçi veya fiziksel tüccarlara, derneklere ve kar amacı gütmeyen kuruluşlara yöneliktir. Ayrıca, topluluklarından doğrudan destek almak isteyen proje sahipleri ve geliştiriciler için de ideal bir çözümdür.



BTCPay Sunucusunun özel özellikleri şunları içerir :




- onun **tam özerkliği**,
- bir **KYC** prosedürünün bulunmaması,
- fonların tam kontrolü**,
- platform ücretlerinin** kaldırılması.



Kendi ödeme işlemciniz olarak, siz ve müşterileriniz arasındaki merkezi bir üçüncü tarafa olan bağımlılığı ortadan kaldırırsınız. Ödemeleri doğrudan bitcoin ve generate ödeme faturaları ile kabul edebilirsiniz. Bu, ne sizin ne de şirketinizin başka biri tarafından yasaklanmamasını sağlar. Her işlem için bir aracıya komisyon ödemek zorunda kalmadan hem banka hem de ödeme işlemcisi rolünü oynarsınız.



on-chain** için işlem ücretleri devam eder, ancak **Liquid** veya **Lightning** ağı kullanılarak azaltılabilir.



Buna ek olarak :




- Tamamen özelleştirilebilir arayüz ve faturalar;
- Gelişmiş gizlilik için yerel **Tor** desteği;
- Crowdfunding**, **POS** ve **ödeme butonları** için destek;
- Birçok para birimi ile uyumludur;
- Bitcoin doğrudan ve eşler arası ödemeler ;
- Özel anahtarlarınız üzerinde tam kontrol;
- Geliştirilmiş gizlilik ;
- Geliştirilmiş güvenlik ;
- Kendi kendine barındırılan yazılım ;
- SegWit** ve **Lightning ağı** için destek;
- Donanım portföylerinin entegrasyonu ile dahili, düğüm tabanlı portföy.



## BTCPay Sunucusunun Kurulması ve Yapılandırılması



### Barındırma modunuzu seçme



BTCPay Sunucusu birkaç farklı şekilde kurulabilir. İhtiyaçlarınıza ve kaynaklarınıza bağlı olarak, üç ana seçenek vardır:




- Üçüncü bir tarafça barındırılan BTCPay Sunucusu**: hizmeti sizin için barındıran bir platform kullanırsınız. Basittir, ancak genellikle ücretsiz değildir.
- BTCPay Sunucusu bir bulut sunucusunda kendi kendine barındırılır** (örneğin [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) veya başka bir sağlayıcı aracılığıyla). Bu, çoğu acemi tüccar için önerilen çözümdür.
- BTCPay Sunucusu kendi donanımınıza (yerel olarak)** yüklenir: bir bilgisayar, mini-PC veya Umbrel üzerinde. Bu yöntem daha tekniktir, ancak tam bağımsızlık sunar.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Yeni başlayan bir tüccar için **bir bulut sunucusunda** dağıtım, tüm teknik altyapıyı yönetmek zorunda kalmadan özerklik, basitlik ve güvenlik arasındaki en iyi uzlaşmadır.



BTCPay Sunucusu, bir dizi barındırma sağlayıcısından hızlı bir şekilde dağıtılabilir. Bunlar arasında **Voltage**, **güvenilir**, **profesyonel** ve **yabancı** bir altyapıya ihtiyaç duyan kullanıcılar için kıyaslama çözümü olarak öne çıkıyor.



### Voltage üzerinde bir BTCPay Sunucu örneği oluşturun



**Voltage**, karmaşık yapılandırma veya sunucu bakımı olmadan kendi BTCPay Sunucunuzu anında dağıtmanıza olanak tanıyan anahtar teslim bir Bitcoin ve Lightning barındırma platformudur.



Resmi Voltaj web sitesini] (https://voltage.cloud) ziyaret edin.



![capture](assets/fr/03.webp)



Geçerli bir e-posta adresi ve güçlü bir parola ile bir **kullanıcı hesabı** oluşturun.



![capture](assets/fr/04.webp)



Voltage **ücretsiz 7 günlük deneme** sunuyor. Lütfen 7 günlük ücretsiz denememizden sonra **düğümlerinizi aktif tutmaya** devam etmek için **aylık 25$** tutarında sabit bir aboneliğe kaydolmaya davet edileceğinizi unutmayın.



Voltage hesabınızı oluşturduktan ve ilk kez giriş yaptıktan sonra, iki ana bölümden oluşan ana sayfaya yönlendirileceksiniz:




- Lightning düğümlerini, Bitcoin Çekirdeğini, BTCPay Sunucusunu ve buluttaki diğer Bitcoin hizmetlerini yönetmek için bir **Altyapı** bölümü;
- ve Bitcoin ödemelerini özelleştirilmiş uygulamalara entegre etmek için Voltage'ın API Lightning'ine erişmenizi sağlayan bir **Ödemeler** bölümü.



BTCPay Server** örneğinizi dağıtmak için **Erişim altyapısı** üzerine tıklayın. Burası, Bitcoin düğümünüz ve BTCPay Sunucunuz dahil olmak üzere tüm hizmetlerinizi oluşturabileceğiniz, yönetebileceğiniz ve izleyebileceğiniz yerdir.



#### Bir grup oluşturun



Bir hizmeti dağıtmadan önce, platform sizden **bir grup** oluşturmanızı isteyecektir. Bir **grup** (çalışma alanı), tüm Bitcoin ve Lightning hizmetlerinizi bir araya getiren bir çalışma alanıdır (örneğin bir düğüm, bir BTCPay Sunucusu, bir gezgin vb.) Çeşitli projelerinizi içeren bir klasör gibidir.



![capture](assets/fr/05.webp)



Bu eğitimin amaçları doğrultusunda, oluşturduğumuz grup **Genesis** olarak adlandırılacaktır. İsterseniz bir profil resmi ekleyebilirsiniz. Bu işlem tamamlandıktan sonra **Oluştur** düğmesine tıklayın. Diğer kullanıcıları gruba katılmaya davet edebilir ve hatta dilerseniz grup adını değiştirebilirsiniz.



Grup ana sayfasında çeşitli seçenekler görünür:




- Lightning Düğümleri** : tam bir Lightning düğümü (LND) konuşlandırmak için;
- Bitcoin Çekirdek Düğümleri** : tam bir Bitcoin düğümü başlatmak için ;
- BTCPay Sunucusu** : kullanıma hazır bir BTCPay örneğini barındırmak için;
- Nostr Hesapları**: Nostr kimliklerini yönetmek için.



Hesabınızı ve hizmetlerinizi güvence altına almak için **çift kimlik doğrulamayı (2FA)** etkinleştirin (devre dışı bırakılırsa düğme kırmızı renkte görünür).



![capture](assets/fr/06.webp)



Seçenekler arasından **BTCPay Sunucusu** üzerine tıklayın, ardından **BTCPay Mağazası Başlat** üzerine tıklayın.



![capture](assets/fr/07.webp)



Voltage daha sonra sizden bir **hizmet adı** (1) seçerek ve Lightning ödemelerini etkinleştirerek (2) BTCPay Sunucu örneğinizi **oluşturmanızı ve yapılandırmanızı** isteyecektir.



Lightning ödemelerini kabul etmeye karar verirseniz bir Lightning düğümüne ihtiyacınız olacaktır.



Zaten bir Bitcoin veya Lightning düğümünüz yoksa, Voltage otomatik olarak bir tane oluşturmanızı önerecektir.



Bir Lightning düğümü oluştur** (3) üzerine tıklayın.



![capture](assets/fr/08.webp)



Düğüm oluşturma arayüzüne girdiğinizde, **standart** ve **profesyonel** düzenler arasında seçim yapmanız istenecektir.



Gerçek bir düğüm (**Mainnet**) veya bir test düğümü (**Testnet**) oluşturabilirsiniz. Ardından **Devam** düğmesine tıklayın.



![capture](assets/fr/09.webp)



Bu eğitim için standart planı kullanalım. Düğüm adını**, bir **parola** girin ve **Oluştur** düğmesine basın.



![capture](assets/fr/10.webp)



Birkaç dakika sonra düğümünüz çalışır hale gelecek ve 500.000 sats alım kapasitesine sahip ücretsiz bir kanal açabileceksiniz.



![capture](assets/fr/11.webp)



Sağ tarafta biraz daha aşağıda, düğümünüz hakkında ihtiyacınız olan tüm bilgileri bulacaksınız!



![capture](assets/fr/12.webp)



Lightning node'umuzu kurup çalıştırdığımıza göre, BTCPay sunucumuzu kurmaya geri dönelim. Şimdi **BTCPay Oluştur** düğmesine tıklayabilirsiniz.



![capture](assets/fr/13.webp)



İlk şifrenizi değiştirmenizi isteyen bir mesajla birlikte varsayılan giriş bilgilerinizi içeren bir sayfa açılacaktır. Bunu yaptıktan sonra, arayüzünüze erişmek için **Şimdi Giriş Yap** düğmesine tıklayın.



![capture](assets/fr/14.webp)



İşte bu kadar! BTCPay sunucunuz kullanıma hazırdır. Doğrudan BTCPay sunucunuzun giriş sayfasına yönlendirileceksiniz.



![capture](assets/fr/15.webp)



Giriş yaptıktan sonra, ilk **mağazanızı** yapılandırın:





- Ona bir **isim** verin.





- Varsayılan para birimini** seçin (EUR, USD, CFA, vb.).





- Bir **döviz kuru sağlayıcısı** seçin (örneğin CoinGecko).



![capture](assets/fr/16.webp)



Daha sonra mağazanızın kontrol paneline yönlendirileceksiniz. Pano arayüzünde, **Mağazanızı oluşturun** düğmesinin yeşil renkle işaretlendiğini göreceksiniz, çünkü bu adım zaten tamamlanmıştır.



![capture](assets/fr/17.webp)



Biraz daha aşağıda **wallet'ü yapılandır** ve **Yıldırım düğümünü yapılandır** düğmeleri bulunmaktadır. Bizim durumumuzda, voltaj üzerinde çalışan bir Lightning düğümüne zaten bağlandık. Bu yüzden burada yapmamız gerekmeyecek.



Bir portföy yapılandırmaya geçelim. Portföy yapılandır** düğmesine tıklayın.



BTCPay Server ile yeni başladığımız için, mevcut bir wallet'i bağlayalım. Bu yüzden **Mevcut bir portföyü bağla** düğmesine basın.



![capture](assets/fr/18.webp)



Daha sonra **ithalat yönteminizi** seçmelisiniz. Mevcut seçenekler arasından **Genişletilmiş genel anahtarı girin** seçeneğini seçin.



![capture](assets/fr/19.webp)



Mevcut bir wallet'yı bağlayarak, BTCPay sunucusunun özel anahtarınıza erişimi olmadan ödemelerinizi **doğrudan bu harici wallet** üzerinden alabilirsiniz. Dolayısıyla, sunucu saldırıya uğrasa veya genel anahtar (`xpub`) ele geçirilse bile, bir saldırgan işlem geçmişinizi görüntüleyebilir, ancak paranıza erişmesi **imkansızdır**.



Genişletilmiş genel anahtarı girin** düğmesine tıkladığınızda, bu anahtarı sağlamanız gereken sayfaya **yönlendirileceksiniz**.



Şimdi **genişletilmiş açık anahtarı** alalım.



### Bir Bitcoin wallet'in bağlanması



Ödemelerinizi almak için mağazanıza bir Bitcoin wallet bağlamanız gerekir. Bunu yapmak için birkaç seçeneğiniz vardır:





- Donanım portföyü** (Ledger, Trezor, Coldcard...) ;





- Yazılım portföyü** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Sunucusu** dahili wallet (daha az güvenli olduğu ve sunucunun hacklenmesi durumunda paranızı daha fazla açığa çıkardığı için önerilmez).



Bu eğitimde, ilk yapılandırma için daha erişilebilir olan bir **yazılım portföyü** kullanacağız. Bir dizi uyumlu uygulama arasından seçim yapabilirsiniz: **Electrum**, **Phoenix**, **Zeus**, **Muun**, vb.



Gösterim için **Electrum** kullanacağız. Electrum**'yi açın, **Portföy**'e ve ardından **Bilgiler**'e tıklayın:



![capture](assets/fr/20.webp)



Ardından, **ana ortak anahtarı (xpub)** kopyalayın.



![capture](assets/fr/21.webp)



Ana genel anahtarı kopyaladıktan sonra, BTCPay Sunucu sayfasında verilen alana yapıştırın.



![capture](assets/fr/22.webp)



Doğrulama işleminden sonra mağazanızın kontrol paneline yönlendirileceksiniz.



![capture](assets/fr/23.webp)



### Bir Satış Noktası (PoS) oluşturun



Mağazanızı ve portföyünüzü kurduktan sonra, artık doğrudan müşterilerinizden Bitcoin ödemeleri almaya başlamak için bir **Satış Noktası (PoS)** kurabilirsiniz.



BTCPay Server'ın** bu entegre özelliği, bir web sitesi** veya özel teknik beceriler olmadan Bitcoin** kabul etmek isteyen **tüccarlar, esnaflar, restorancılar veya hizmet sağlayıcılar** için idealdir.



### Satış noktası nedir?



PoS**, bir **Bitcoin ödeme terminali** olarak işlev gören bir **basitleştirilmiş POS arayüzüdür**.


Bu size izin verir :




- Sabit fiyatlı bir **ürün veya hizmet menüsü** oluşturun.
- Taramak için QR kodlu** bir **anlık fatura oluşturun.
- Akıllı telefon, tablet veya bilgisayar üzerinden erişilebilen bir **Ödeme URL'si** paylaşın.



Başka bir deyişle, PoS, BTCPay Sunucunuzu, her ödemenin **aracı olmadan kendi Bitcoin wallet**'nizde alındığı bir **doğrudan satış arayüzüne** dönüştürür.



### PoS'u Yapılandırma



BTCPay kontrol panelinde **PLUGINS** öğesine ve ardından **Point of sale** öğesine tıklayın.



Ardından **Yeni bir PoS uygulaması oluştur** seçeneğine tıklayın. Bu işlem, sanki mini bir dahili satış sitesi kuruyormuşsunuz gibi BTCPay mağazanıza **yeni bir uygulama** ekler.



Uygulamanızı oluşturmak için bir sayfa açılır. Bir **uygulama adı** tanımlayın: bu, yalnızca kontrol panelinizden görülebilen dahili bir addır (örneğin _Shoe Shop_).



Doğrulamak için **Oluştur** üzerine tıklayın.



![capture](assets/fr/24.webp)



Oluşturulduktan sonra, Satış Noktasının **Detaylı yapılandırma sayfasına** yönlendirileceksiniz.



### Satış arayüzünüzü özelleştirin



Bu sayfada, PoS'unuzun temel unsurlarını tanımlayabilirsiniz:





- Uygulama adı** (dahili yönetim adı, herhangi bir zamanda değiştirilebilir).





- Ekran başlığı** (müşterilerinizin sayfanın üst kısmında göreceği şey).





- Satış noktası stili** (**Açıklama** modu saç kesimi veya yemek gibi hizmetler için uygunken, **Ürün kataloğu** modu birkaç ürün sunan mağazalar için idealdir).





- Para birimini göster** (normal fiyatlarınıza göre **XOF**, **EUR** veya **USD** seçin).





- Ürün listesi** (ürünlerinizi, açıklamalarını ve fiyatlarını buraya ekleyin).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### PoS'unuzu kaydedin ve test edin



Yapılandırmayı tamamladığınızda, ayarlarınızı kaydetmek için **Kaydet** seçeneğine, ardından PoS'unuzu önizlemek için **Görüntüle** seçeneğine tıklayın.



Ürünlerinizin sunulduğu ve her düğmenin bir ürün veya hizmete karşılık geldiği bir sayfa göreceksiniz.



Bir müşteri bir ürünü seçer seçmez :



1. BTCPay otomatik olarak bir Bitcoin veya Lightning** faturası oluşturur.



2. Ekranda bir **QR kodu** görüntülenir.



3. Müşteriler Bitcoin wallet ile doğrudan **tarama ve ödeme** yapabilirler.




![capture](assets/fr/27.webp)



### Nihai sonuç



Artık kullanabileceğiniz eksiksiz bir **Bitcoin Satış Noktasına** sahipsiniz:





- Mağazanızdaki bir akıllı telefondan veya tabletten açın ;





- Müşterinin taraması için bir ekranda görüntülenir;





- Ya da basitleştirilmiş bir sipariş sayfası gibi herkese açık bir **URL** üzerinden paylaşın.



Her ödemede tutar, aracılar veya üçüncü taraf ücretleri olmadan otomatik olarak **kendi BTCPay wallet** hesabınıza yatırılır.


Bu, PoS'unuzu **tek başına bir Bitcoin ödeme terminaline** dönüştürür.




## Günlük kullanım



Herhangi bir gerçek ödemeyi nakde çevirmeden önce, her şeyin düzgün çalışıp çalışmadığını kontrol etmek için **bir test** yapmanızı öneririz.



### Bir ödemeyi test edin





- PoS arayüzünüzden bir fatura** oluşturun (örneğin, 1 satoshi ürün veya küçük bir miktar).





- Bir Bitcoin veya Lightning wallet (**Phoenix**, **Muun** veya **Wallet of Satoshi** gibi) kullanarak ekrandaki QR kodunu** tarayın.




![capture](assets/fr/28.webp)





- wallet'inizde ödemeyi** doğrulayın: işlem anında gönderilir.





- BTCPay Sunucusuna Dön**: fatura listede **Ödendi** olarak görünecektir.



![capture](assets/fr/29.webp)



Tebrikler! Satış Noktanız artık **işlevseldir**. Müşterilerinizden Bitcoin ödemelerini basit, hızlı ve aracısız bir şekilde almaya başlayabilirsiniz.



### Bir müşteri için fatura oluşturma



Faturalar** menüsünde **Yeni fatura** seçeneğine tıklayın.



![capture](assets/fr/30.webp)



Diğer ürün bilgilerinin yanı sıra **miktarı** ve **yerel para birimini** (BTCPay otomatik olarak BTC cinsinden eşdeğerini hesaplar) girin.



![capture](assets/fr/31.webp)



QR kodunu** veya **URL**'yi müşteri ile paylaşın.



![capture](assets/fr/32.webp)



### Alınan ödemeleri takip edin



Yine **Faturalar** menüsünde, tüm işlemlerinizin bir listesini göreceksiniz.


Olası durumlar şunlardır:





- Beklemede**: ödeme henüz onaylanmadı.





- Ödendi**: ödeme onaylandı.





- Süresi dolmuş**: son ödeme tarihine kadar ödenmemiş fatura.



### Müşteriye para iadesi



Faturalar** menüsünden geri ödemesi yapılacak faturayı seçin.



![capture](assets/fr/33.webp)



Geri Ödeme** üzerine tıklayın ve müşteri tarafından sağlanan Bitcoin adresini girin.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Raporlar ve veri aktarımı



BTCPay Server, işlemlerinizi **dışa aktarmanıza** (CSV veya Excel formatında) olanak tanır. Bu, muhasebe ve kasa takibiniz için çok pratiktir.



![capture](assets/fr/36.webp)



Rapor** menüsünde **Dışa Aktar** seçeneğine tıklayın: tüm işlemleriniz daha sonra yerel olarak başvurabileceğiniz bir CSV dosyasına kaydedilecektir.



## Güvenlik ve en iyi uygulamalar



BTCPay Sunucusu tarafından verilen özerklik (fonlarınız üzerinde tam egemenlik) gerçek bir güçtür. Ancak bu özgürlük, güvenlik açısından daha büyük sorumluluk getirir. Kendi ödemelerinizi yöneterek, kendi bankanızın rolünü üstlenirsiniz. Bu nedenle fonlarınızı, verilerinizi ve altyapınızı korumak için en iyi uygulamaları benimsemeniz zorunludur. İşte dikkate alınması gereken ana noktalar.



### Sunucunuza güvenli erişim





- Güçlü bir parola kullanın: büyük ve küçük harfleri, sayıları ve özel karakterleri birleştirin. Mevcut bir parolayı tekrar kullanmaktan kaçının.
- BTCPay arayüzünüze erişmek için iki faktörlü kimlik doğrulamayı (2FA) etkinleştirin.
- İşletim sisteminizi, BTCPay Server örneğinizi ve bağımlılıklarınızı (Docker, Bitcoin node, Lightning node...) düzenli olarak güncelleyin. Güncellemeler genellikle güvenlik açıklarını düzeltir.



### Özel anahtarları yönetme ve yedekleme





- Özel anahtarlarınızı ve seedphrase'lerinizi çevrimdışı olarak fiziksel ortama (kağıt veya metal) kaydedin.
- Tercihen bir wallet donanım wallet kullanın.
- Yedeklerinizin birkaç kopyasını ayrı, korumalı fiziksel konumlarda saklayın.



### Güvenli ödemeler ve gizlilik





- Sunucunuzun IP adresini gizlemek ve gizliliğinizi korumak için Tor ağını veya bir VPN kullanın.
- Sunucunuzdaki gereksiz bağlantı noktalarını devre dışı bırakın ve SSH bağlantılarını yalnızca güvenilir adreslerle kısıtlayın.
- BTCPay web arayüzünüze tüm bağlantılar için HTTPS'yi (SSL sertifikası) etkinleştirin.
- Yönetim arayüzünüzü asla Bitcoin portföy yönetimi konusunda eğitimli olmayan personel ile paylaşmayın.



### Lightning ağı için en iyi uygulamaların hayata geçirilmesi



Mağazanız, ağın teknik yönetimini önemli ölçüde basitleştiren Voltage** üzerinde barındırılan bir **Lightning düğümüne bağlıdır. Bununla birlikte, **iyi izleme ve güvenlik uygulamalarının** benimsenmesi önemini korumaktadır:





- Voltage node'unuzun API** oturum açma ve erişim anahtarlarını (BTCPay'in bağlanmasını sağlayan) kaydedin.
- Voltage hesabınızı** iki faktörlü kimlik doğrulama ve güçlü bir parola ile koruyun.
- Voltage panonuzdan düğüm ve kanal durumunu** izleyin: bu, herhangi bir anormalliği veya senkronizasyon bozukluğunu tespit etmenize yardımcı olur.
- API** kimlik bilgilerinizi paylaşmaktan veya herkese açık bir şekilde ifşa etmekten kaçının (örn. site kodunda).
- Geçiş durumunda, BTCPay ve Voltage** arasındaki bağlantıyı yeniden yapılandırmanız yeterlidir: kanalın manuel olarak kapatılmasına gerek yoktur.



Voltage ile **güvenli, yüksek kullanılabilirliğe sahip** ve **otomatik olarak yedeklenen** bir altyapıdan yararlanırken, Lightning ödemeleriniz üzerinde **tam egemenliği** elinizde tutarsınız.



### İç prosedürleri düzenlemek ve yapılandırmak





- Net bir erişim yönetimi politikası tanımlayın: kimler fatura oluşturabilir, ödemeleri görüntüleyebilir, düğüme erişebilir vb.
- Bir olay durumunda hızlı tepki verebilmek için yedekleme ve geri yükleme prosedürlerinizi belgeleyin.
- Düzgün çalıştıklarından emin olmak için yedeklerinizin geri yüklenmesini düzenli olarak test edin.
- Personelinizi veya ortak çalışanlarınızı temel operasyonel güvenlik konusunda eğitin: kimlik avına karşı dikkatli olma, güvenli şifreler kullanma, gizliliğe saygı duyma.



### Sürekli bakımı denetlemek ve kurmak





- Günlük tutma veya izleme araçlarını kullanarak sunucunuzun etkinliğini sürekli izleyin.
- Periyodik bir güvenlik incelemesi planlayın: güncellemeleri, erişimi, yedeklemeleri ve işlem tutarlılığını kontrol edin.



Tebrikler! Bu eğitimin sonuna ulaştınız. Artık BTCPay Server ile kendi başınıza çalışarak mağazanızı yönetmenizi kolaylaştırabilirsiniz.



Daha fazla bilgi edinmek için, Bitcoin'ü şirketinize entegre etme konusundaki eksiksiz eğitim kursumuzu almanızı tavsiye ederim:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a