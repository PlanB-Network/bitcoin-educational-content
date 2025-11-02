---
name: BTCPAY SERVER - Şemsiye
description: Bitcoin ve Lightning'i kabul etmek için Umbrel'e BTCPAY SERVER'in kurulması ve kullanılması
---

![cover](assets/cover.webp)



Bitcoin ekosisteminde, ödemeleri kabul etmek hem tüccarlar hem de işletmeler için büyük bir zorluk teşkil etmektedir. Geleneksel çözümler, ister bankacılık (kredi kartları, Stripe, PayPal) ister Bitcoin (BitPay, Coinbase Commerce) olsun, önemli ücretler alan, hassas iş verilerinizi toplayan ve işlemlerinizi kendi isteklerine göre BLOCK veya sansürleyebilen aracılar empoze eder. Bu bağımlılık Bitcoin'ün merkeziyetsizlik, gizlilik ve finansal egemenlik gibi temel ilkelerine ters düşmektedir.



BTCPAY SERVER bu soruna açık kaynaklı bir yanıt olarak ortaya çıkıyor. Bu kendi kendine barındırılan ödeme işlemcisi, kendi Bitcoin düğümünüzü, aracı olmadan, ek işlem ücreti olmadan ve gizlilikten ödün vermeden profesyonel bir altyapıya dönüştürür. 2017'den beri küresel bir katılımcı topluluğu tarafından geliştirilen BTCPAY SERVER, Bitcoin ve Lightning ödemelerini doğrudan cüzdanlarınıza almanıza ve fonlarınızın tam kontrolünü her zaman elinizde tutmanıza olanak tanır.



Geleneksel olarak BTCPAY SERVER kurulumu ileri düzey teknik beceriler gerektirir: Linux sunucu yapılandırması, Docker ustalığı, SSL sertifika yönetimi ve ağ güvenliği. Umbrel, Bitcoin ve LIGHTNING NODE'nize doğrudan entegre tek tıkla kurulum ile bu yaklaşımda devrim yaratıyor. Bu basitleştirme, daha önce deneyimli teknisyenler için ayrılmış olanı herkes için erişilebilir hale getirir.



**Anlaşılması önemli**: BTCPAY SERVER on Umbrel varsayılan olarak yalnızca yerel ağınızda çalışır. Ev ağınıza bağlı herhangi bir cihazdan (bilgisayar, akıllı telefon, tablet) fatura oluşturabilir, Lightning ve Bitcoin ödemelerini kabul edebilir ve muhasebenizi yönetebilirsiniz. Bu yapılandırma, yüz yüze hizmetleri faturalandırmak, yüz yüze ödemeleri yönetmek veya BTCPAY SERVER'u yerel ağınızdan kullanmak için idealdir. Öte yandan, BTCPAY SERVER'u İnternet üzerinden herkese açık bir çevrimiçi mağazaya entegre etmek için herkese açık ek bir yapılandırma gerekecektir (bu konuyu eğitimin sonunda ele alacağız).



Bu eğitimde BTCPAY SERVER'ün Umbrel'e tam kurulumu, Bitcoin Wallet ve LIGHTNING NODE'nin yapılandırılması, faturaların oluşturulması ve ödenmesi ve muhasebe raporlamasının yönetilmesi anlatılmaktadır. BTCPAY SERVER'ü yerel ağınızda nasıl etkili bir şekilde kullanacağınızı öğrenecek ve ardından bir e-ticaret sitesiyle entegre etmek istiyorsanız herkese açık görüntüleme için çözümlerden bahsedeceğiz.



## Ön Koşullar



Bu öğreticiyi takip etmek için Umbrel'in doğru şekilde kurulmuş ve yapılandırılmış olması gerekir. Henüz yapmadıysanız, lütfen Umbrel kurulumu hakkındaki eğitimimize bakın.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin core düğümünüzün Blockchain ile tamamen senkronize edilmesi gerekir (Umbrel'in Bitcoin uygulamasında %100). Bu ilk senkronizasyon, donanımınıza ve İnternet bağlantınıza bağlı olarak genellikle 3 gün ile 2 hafta arasında sürer.



Anında Lightning ödemelerini kabul etmek için Umbrel'e LND'yi (Lightning Network Daemon) de yüklemeniz gerekir. Bu özelliği etkinleştirmek istiyorsanız Umbrel'de LND'yi yükleme ve yapılandırma hakkındaki eğitimimize bakın.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

BTCPAY SERVER, veritabanları ve Lightning verileri için en az 50 GB boş disk alanı bırakın. Bağlantı kopmalarını önlemek için Ethernet kablosu üzerinden sabit bir İnternet bağlantısı şiddetle tavsiye edilir.



## BTCPAY SERVER'nin Şemsiyeye Takılması



Umbrel Interface'ten (`umbrel.local`) App Store'a gidin ve Bitcoin kategorisinde "BTCPAY SERVER "ü arayın.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Yükle'ye tıklayın. Umbrel otomatik olarak Bitcoin core ve LND'nin kurulu olup olmadığını kontrol eder, ardından dağıtımı başlatır (2-5 dakika).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kurulduktan sonra uygulamayı açın. Güçlü kimlik bilgilerine sahip bir yönetici hesabı oluşturmanız gerekecektir.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Hesabınız oluşturulduktan sonra, BTCPAY SERVER sizden hemen ilk mağazanızı kurmanızı isteyecektir. Profesyonel bir ad seçin ve bir referans para birimi seçin (EUR, USD veya BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Yerel ağınızda BTCPAY SERVER'a erişin



BTCPAY SERVER'a yerel ağınızdaki (WiFi veya Ethernet) herhangi bir cihazdan erişilebilir. Tarayıcınızdan erişim :



```url
http://umbrel.local
```



Ya da doğrudan :



```url
http://umbrel.local:3003
```



**Tailscale** ile uzaktan erişim: BTCPAY SERVER'e dünyanın herhangi bir yerinden erişmek için Tailscale kullanın. Bu güvenli VPN, Umbrel'inize yerel ağınızdaymış gibi bağlanmanızı sağlar. Umbrel'de Tailscale'e adanmış öğreticimize bakın.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin portföyünüzü yapılandırma



Ödemeleri kabul etmek için bir Bitcoin Wallet yapılandırmanız gerekir. BTCPAY SERVER, kontrol panelindeki yapılandırma seçeneklerini görüntüler.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Wallet Bitcoin'yı yapılandırmak için "Cüzdanlar" > "Bitcoin" seçeneğine gidin.



İki seçeneğiniz vardır: doğrudan BTCPay'de yeni bir portföy oluşturmak veya mevcut bir portföyü içe aktarmak. İçe aktarma için çeşitli yöntemler mevcuttur:




- Hardware Wallet**'e bağlanın (önerilir): Açık anahtarlarınızı Vault uygulaması aracılığıyla içe aktarın
- Wallet dosyasını içe aktar** (önerilir): Portföyünüzden dışa aktarılmış bir dosya yükleyin
- Genişletilmiş genel anahtarı girin**: XPub/YPub/ZPub anahtarınızı manuel olarak girin
- Wallet QR kodunu tarayın** : BlueWallet, Cobo Vault, Passport veya Specter DIY'den bir QR kodu tarayın
- Wallet seed** girin (önerilmez) : 12 veya 24 kelimelik kurtarma cümlenizi girin



![Options de création de portefeuille](assets/fr/06.webp)



Bu eğitim için yeni bir Hot Wallet oluşturacağız: özel anahtar bu nedenle Umbrel sunucumuzda saklanacaktır. Bu durumda, sunucuda büyük miktarlar depolamaktan kaçınmak için fonları düzenli olarak bir Cold Wallet'e taşımanızı şiddetle tavsiye ederiz.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Yapılandırıldıktan sonra BTCPAY SERVER, Wallet'inizin On-Chain ödemelerini kabul etmeye hazır olduğunu onaylar.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network'u etkinleştirin



Anında Lightning ödemelerini kabul etmek için Cüzdanlar > Lightning'e gidin. Ardından, LND düğümünüz Umbrel'de zaten yerinde olduğundan, BTCPAY SERVER'iniz ile LIGHTNING NODE'niz arasındaki bağlantıyı doğrulamak için "Kaydet" düğmesine tıklamanız yeterlidir.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Fatura oluşturma ve ödeme



Interface BTCPAY SERVER'te, Faturalar > Invoice Oluştur'a gidin. Tutarı girin, isteğe bağlı bir açıklama ekleyin ve Oluştur'a tıklayın.



![Création d'une nouvelle facture](assets/fr/10.webp)



Daha sonra Invoice'i görüntülemek için "Ödeme Yap" düğmesine tıklayabilirsiniz. BTCPay daha sonra Bitcoin Address ve Lightning Invoice'i içeren birleşik bir QR kodu (BIP21) ile bir Invoice oluşturur.



![Détails de la facture générée](assets/fr/11.webp)



Müşteriniz QR kodunu uyumlu herhangi bir Wallet ile tarayabilir.



![Page de paiement avec QR code](assets/fr/12.webp)



Ödeme yapıldıktan sonra Invoice, Lightning için birkaç saniye içinde "Yerleşmiş" hale gelir.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Ödeme yönetimi ve takibi



"Raporlama" bölümünde, "Faturalar" sekmesinde, tarih, tutar, durum ve ödeme yöntemiyle birlikte faturalarınızın eksiksiz bir geçmişini bulacaksınız. İsterseniz dışa aktarabilirsiniz.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Mağaza yapılandırması



BTCPAY SERVER, farklı parametrelere sahip birden fazla mağazayı yönetmenizi sağlar. Her mağaza ayrı bir ticari varlığı temsil eder: e-ticaret mağazası, fiziksel satış noktası veya hizmet faturalandırması.



Mağaza ayarlarında birkaç önemli bölüm bulacaksınız:



![Paramètres du magasin](assets/fr/15.webp)





- Genel Ayarlar**: Mağaza adı, referans para birimi (BTC, EUR, USD), Invoice sona erme süresi (varsayılan 15 dakika), gerekli Blockchain onay sayısı
- Oranlar**: Exchange kur kaynaklarının yapılandırılması ve fiat/Bitcoin dönüşümleri
- Ödeme Görünümü**: Ödeme sayfalarınızın görünümünü özelleştirin (logo, renkler, kişiselleştirilmiş mesajlar)
- E-posta Ayarları**: Alınan ödemeler için e-posta bildirimlerinin yapılandırılması
- Erişim Belirteçleri**: E-ticaret entegrasyonları için API token yönetimi (WooCommerce, Shopify, vb.)
- Kullanıcılar**: Farklı izin seviyeleriyle (Sahip, Misafir) mağazaya kullanıcı erişimini yönetin
- Webhooks**: Muhasebe veya ERP sisteminizle gerçek zamanlı senkronizasyon için Webhook yapılandırması



BTCPAY SERVER ayrıca e-ticaret entegrasyonları, satış noktası sistemleri ve ek araçlarla işlevselliği genişletmek için bir Eklentiler bölümü sunar.



![Gestion des plugins](assets/fr/16.webp)



## Yerel kullanımın avantajları ve sınırlamaları



**BTCPAY SERVER'un Şemsiye Üzerindeki Faydaları** :




- Tam egemenlik: özel anahtarların ve fonların münhasır kontrolü, hiçbir üçüncü taraf ödemelerinizi donduramaz veya sansürleyemez
- Önemli tasarruflar: geleneksel işlemcilerde %2-3'e kıyasla yalnızca Bitcoin ağ maliyetleri (Lightning'de birkaç sent)
- Maksimum gizlilik: kayıt, kimlik doğrulama veya üçüncü taraf şirketlerle veri paylaşımı yok
- Açık kaynak mimarisi, geniş bir geliştirici topluluğu aracılığıyla şeffaflığı, denetlenebilirliği ve sürdürülebilirliği garanti eder
- Umbrel aracılığıyla ileri teknik becerilere ihtiyaç duymadan kolay kurulum



**Önemli sınırlamalar** :




- Yalnızca yerel ağ**: Umbrel üzerindeki BTCPAY SERVER'e yalnızca ev ağınızdan erişilebilir. Yüz yüze faturalandırma, serbest hizmetler veya küçük fiziksel işletmeler için mükemmeldir, ancak İnternet üzerinden herkesin erişebildiği çevrimiçi mağazalar için uygun değildir.
- Tam teknik sorumluluk: düğüm bakımı, düzenli yedeklemeler, bağlantı izleme
- Yıldırım likidite yönetimi: yeterli gelen kapasiteye sahip kanalların açılması ve yönetilmesi
- Ticari bir müşteri hizmetleri departmanından daha fazla özerklik gerektiren, topluluk dokümantasyonu ve forumlarla sınırlı destek



Bu LAN sınırlaması, BTCPAY SERVER'nin müşterilerin ödeme sayfalarına İnternet üzerindeki herhangi bir yerden erişebilmeleri gereken bir e-ticaret mağazasına entegre edilmesinin önündeki ana engeldir.



## En iyi uygulamalar ve güvenlik



Otomatik Umbrel yedeklemelerini etkinleştirin ve bir kopyasını harici ortamda (USB bellek, Hard diski, şifrelenmiş bulut) saklayın. Bitcoin tohumlarınızı (kurtarma cümleleri) güvenli, fiziksel olarak ayrı bir yerde saklayın. Lightning kurtarma için LND channel.backup dosyasını kaydedin.



Bitcoin core senkronizasyonunu, Lightning kanallarını ve BTCPAY SERVER yanıtını düzenli olarak izleyin. Basit bir haftalık test: generate ve birkaç satoshis için bir fatura ödeyin. Umbrel'i güncel tutun (güvenlik yamaları, geliştirmeler). Büyük güncellemelerden önce bir yedekleme yapın. Profesyonel kullanım için, e-posta/SMS uyarıları ile harici izlemeyi (UptimeRobot) düşünün.



## Bir çevrimiçi mağaza için BTCPAY SERVER'u herkese açık olarak gösterin



BTCPAY SERVER'i web tabanlı bir e-ticaret mağazasına (WooCommerce, Shopify vb.) entegre etmek için müşterilerinizin ödeme sayfalarına yalnızca yerel ağınızdan değil, her yerden erişebilmesi gerekir.



**Çözüm: Nginx Proxy Yöneticisi**



Nginx Proxy Manager'ı (Umbrel App Store'da mevcuttur) kullanarak BTCPAY SERVER'i herkese açık hale getirebilirsiniz. Bu çözüm için :




- Bir alan adı (klasik veya DuckDNS, No-IP, Afraid.org üzerinden ücretsiz)
- Yönlendiricinizde bağlantı noktası yönlendirmeyi (80 ve 443 numaralı bağlantı noktaları) yapılandırma
- SSL sertifikalarını otomatik olarak yöneten Nginx Proxy Manager'ın kurulumu



Bu yapılandırma sunucunuzu internete açık hale getirir ve ekstra dikkat gerektirir (güçlü parolalar, 2FA, düzenli güncellemeler). Bu prosedürün tamamını detaylandıran özel bir eğitim hazırlayacağız.



## Sonuç



Umbrel üzerindeki BTCPAY SERVER, Bitcoin düğümünün gücünü Umbrel'in basitliği ile birleştirerek herkesin erişebileceği kendi kendine barındırılan profesyonel bir ödeme altyapısı oluşturur. Bu finansal egemenlik bir bakım sorumluluğunu da beraberinde getirir, ancak Umbrel operasyonel yükü faydalarına kıyasla büyük ölçüde basitleştirir: işlem ücretlerinin ortadan kaldırılması, gizliliğinizin korunması, sansüre karşı direnç ve fonlarınızın tam kontrolü.



Yerel ağ kullanımı halihazırda çok çeşitli uygulamaları kapsamaktadır: serbest hizmetler için faturalandırma, yüz yüze ödemeler, küçük fiziksel mağazalar veya sadece kontrollü bir ortamda Bitcoin ve Lightning ile öğrenme ve deneme. Herkese açık olmayı gerektiren e-ticaret ihtiyaçları için Nginx Proxy Manager çözümü mevcuttur, ancak özel bir eğitimde detaylandıracağımız ek teknik yapılandırma gerektirir.



İster bir işletme, ister yeni başlayan bir proje yürütüyor olun, ister sadece deney yapıyor olun, Umbrel'de BTCPAY SERVER tam bir finansal özerklik sunar. Yol, ilk mağaza, ilk Invoice, doğrudan egemen altyapınıza alınan ilk ödeme ile başlar.



## Kaynaklar



### Resmi belgeler




- [BTCPAY SERVER resmi web sitesi](https://btcpayserver.org)
- [BTCPAY SERVER belgelerinin tamamı](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale belgeleri](https://tailscale.com/kb)


### Topluluk ve destek




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)