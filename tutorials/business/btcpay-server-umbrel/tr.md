---
name: BTCPay Sunucusu - Umbrel
description: Bitcoin ve Lightning kabul etmek için Umbrel'de BTCPay Sunucusunun kurulması ve kullanılması
---

![cover](assets/cover.webp)



Bitcoin ekosisteminde, ödemeleri kabul etmek hem tüccarlar hem de işletmeler için büyük bir zorluk teşkil etmektedir. Geleneksel çözümler, ister bankacılık (kredi kartları, Stripe, PayPal) ister Bitcoin (BitPay, Coinbase Commerce) olsun, önemli ücretler alan, hassas iş verilerinizi toplayan ve işlemlerinizi kendi isteklerine göre engelleyebilen veya sansürleyebilen aracılar dayatır. Bu bağımlılık Bitcoin'in temel ilkeleri olan merkeziyetsizlik, gizlilik ve finansal egemenliğe ters düşmektedir.



BTCPay Server bu soruna açık kaynaklı bir yanıt olarak ortaya çıkmaktadır. Bu kendi kendine barındırılan ödeme işlemcisi, kendi Bitcoin düğümünüzü, aracı olmadan, ek işlem ücreti olmadan ve gizlilikten ödün vermeden profesyonel bir altyapıya dönüştürür. 2017'den bu yana küresel bir katılımcı topluluğu tarafından geliştirilen BTCPay Server, Bitcoin ve Lightning ödemelerini doğrudan cüzdanlarınıza almanıza ve fonlarınızın tam kontrolünü her zaman elinizde tutmanıza olanak tanır.



Geleneksel olarak, BTCPay Server'ı kurmak ileri teknik beceriler gerektirir: Linux sunucu yapılandırması, Docker'da ustalık, SSL sertifika yönetimi ve ağ güvenliği. Umbrel, Bitcoin ve Lightning düğümünüzle doğrudan entegre tek tıklamayla kurulumla bu yaklaşımda devrim yaratıyor. Bu basitleştirme, daha önce deneyimli teknisyenler için ayrılmış olanı herkes için erişilebilir hale getirir.



**Anlamak önemlidir**: Umbrel'deki BTCPay Sunucusu varsayılan olarak yalnızca yerel ağınızda çalışır. Ev ağınıza bağlı herhangi bir cihazdan (bilgisayar, akıllı telefon, tablet) fatura oluşturabilir, Lightning ve Bitcoin ödemelerini kabul edebilir ve muhasebenizi yönetebilirsiniz. Bu yapılandırma, yüz yüze hizmetleri faturalandırmak, yüz yüze ödemeleri yönetmek veya BTCPay Server'ı yerel ağınızdan kullanmak için idealdir. Öte yandan, BTCPay Server'ı İnternet üzerinden herkesin erişebileceği bir çevrimiçi mağazaya entegre etmek için, herkese açık ek bir yapılandırma gerekecektir (bu konuyu eğitimin sonunda ele alacağız).



Bu eğitimde BTCPay Server'ın Umbrel'e tam kurulumunu, Bitcoin wallet ve Lightning düğümünüzü yapılandırmayı, fatura oluşturmayı ve ödemeyi ve muhasebe raporlamasını yönetmeyi öğreneceksiniz. BTCPay Server'ı yerel ağınızda nasıl verimli bir şekilde kullanacağınızı keşfedecek ve ardından bir e-ticaret sitesiyle entegre etmek istiyorsanız herkese açık görüntüleme için çözümlere bakacağız.



## Ön Koşullar



Bu öğreticiyi takip etmek için Umbrel'in doğru şekilde kurulmuş ve yapılandırılmış olması gerekir. Henüz yapmadıysanız, lütfen Umbrel kurulumu hakkındaki eğitimimize bakın.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin Core düğümünüzün blok zinciri ile tamamen senkronize edilmesi gerekir (Umbrel'in Bitcoin uygulamasında %100). Bu ilk senkronizasyon, donanımınıza ve internet bağlantınıza bağlı olarak genellikle 3 gün ile 2 hafta arasında sürer.



Anında Lightning ödemelerini kabul etmek için Umbrel'e LND'u (Lightning Network Daemon) da yüklemeniz gerekir. Bu özelliği etkinleştirmek istiyorsanız Umbrel'de LND'u yükleme ve yapılandırma hakkındaki eğitimimize bakın.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

BTCPay Server, veritabanları ve Lightning verileri için en az 50 GB boş disk alanı bırakın. Bağlantı kesilmelerini önlemek için Ethernet kablosu üzerinden sabit bir İnternet bağlantısı şiddetle tavsiye edilir.



## BTCPay Sunucusunu Umbrel'e Yükleme



Umbrel arayüzünden (`umbrel.local`) App Store'a erişin ve Bitcoin kategorisinde "BTCPay Server "ı arayın.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Yükle'ye tıklayın. Umbrel otomatik olarak Bitcoin Core ve LND'nin kurulu olup olmadığını kontrol eder, ardından dağıtımı başlatır (2-5 dakika).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Kurulduktan sonra uygulamayı açın. Güçlü kimlik bilgilerine sahip bir yönetici hesabı oluşturmanız gerekecektir.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Hesabınız oluşturulduktan sonra, BTCPay Server hemen ilk mağazanızı kurmanızı isteyecektir. Bir işletme adı seçin ve bir referans para birimi seçin (EUR, USD veya BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Yerel ağınızdaki BTCPay Sunucusuna erişin



BTCPay Sunucusuna yerel ağınızdaki (WiFi veya Ethernet) herhangi bir cihazdan erişilebilir. Tarayıcınızdan erişim :



```url
http://umbrel.local
```



Ya da doğrudan :



```url
http://umbrel.local:3003
```



**Tailscale** ile uzaktan erişim: BTCPay Sunucusuna dünyanın herhangi bir yerinden erişmek için Tailscale kullanın. Bu güvenli VPN, Umbrel'inize yerel ağınızdaymış gibi bağlanmanızı sağlar. Umbrel'de Tailscale'e adanmış öğreticimize bakın.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoin portföyünüzü yapılandırma



Ödemeleri kabul etmek için bir Bitcoin wallet yapılandırmanız gerekir. BTCPay Server, gösterge tablosunda yapılandırma seçeneklerini görüntüler.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



wallet Bitcoin'yı yapılandırmak için "Cüzdanlar" > "Bitcoin" seçeneğine gidin.



İki seçeneğiniz vardır: doğrudan BTCPay'de yeni bir portföy oluşturmak veya mevcut bir portföyü içe aktarmak. İçe aktarma için çeşitli yöntemler mevcuttur:




- wallet** donanımını bağlayın (önerilir): Açık anahtarlarınızı Vault uygulaması aracılığıyla içe aktarın
- wallet dosyasını içe aktar** (önerilir): Portföyünüzden dışa aktarılmış bir dosya yükleyin
- Genişletilmiş genel anahtarı girin**: XPub/YPub/ZPub anahtarınızı manuel olarak girin
- wallet QR kodunu tarayın** : BlueWallet, Cobo Vault, Passport veya Specter DIY'den bir QR kodu tarayın
- wallet seed** girin (önerilmez) : 12 veya 24 kelimelik kurtarma cümlenizi girin



![Options de création de portefeuille](assets/fr/06.webp)



Bu eğitim için yeni bir Hot wallet oluşturacağız: özel anahtar bu nedenle Umbrel sunucumuzda saklanacaktır. Bu durumda, sunucuda büyük miktarlar depolamaktan kaçınmak için fonları düzenli olarak soğuk bir wallet'e taşımanızı şiddetle tavsiye ederiz.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Yapılandırıldıktan sonra BTCPay Sunucusu, wallet'nızın on-chain ödemelerini kabul etmeye hazır olduğunu onaylar.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network'yi etkinleştirin



Anında Lightning ödemelerini kabul etmek için Cüzdanlar > Lightning'e gidin. Ardından, LND düğümünüz Umbrel'de zaten mevcut olduğundan, BTCPay Sunucunuz ile Lightning düğümünüz arasındaki bağlantıyı doğrulamak için "Kaydet" düğmesine tıklamanız yeterlidir.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Fatura oluşturma ve ödeme



BTCPay Sunucu arayüzünde, Faturalar > Invoice Oluştur'a gidin. Tutarı girin, isteğe bağlı bir açıklama ekleyin ve Oluştur'a tıklayın.



![Création d'une nouvelle facture](assets/fr/10.webp)



Daha sonra faturayı görüntülemek için "Ödeme Yap" düğmesine tıklayabilirsiniz. BTCPay daha sonra Bitcoin adresini ve Lightning faturasını içeren birleşik QR kodlu (BIP21) bir fatura oluşturur.



![Détails de la facture générée](assets/fr/11.webp)



Müşteriniz QR kodunu uyumlu herhangi bir wallet ile tarayabilir.



![Page de paiement avec QR code](assets/fr/12.webp)



Ödeme yapıldıktan sonra, fatura Lightning için birkaç saniye içinde "Kapatılmış" hale gelir.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Ödeme yönetimi ve takibi



"Raporlama" bölümünde, "Faturalar" sekmesinde, faturalarınızın tarih, tutar, durum ve ödeme yöntemiyle birlikte eksiksiz bir geçmişini bulacaksınız. İsterseniz dışa aktarabilirsiniz.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Mağaza yapılandırması



BTCPay Server, farklı parametrelere sahip birden fazla mağazayı yönetmenize olanak tanır. Her mağaza ayrı bir ticari varlığı temsil eder: e-ticaret mağazası, fiziksel satış noktası veya hizmet faturalandırması.



Mağaza ayarlarında birkaç önemli bölüm bulacaksınız:



![Paramètres du magasin](assets/fr/15.webp)





- Genel Ayarlar**: Mağaza adı, referans para birimi (BTC, EUR, USD), fatura geçerlilik süresi (varsayılan 15 dakika), gerekli blok zinciri onay sayısı
- Oranlar**: Döviz kuru kaynaklarının yapılandırılması ve fiat/Bitcoin dönüşümleri
- Ödeme Görünümü**: Ödeme sayfalarınızın görünümünü özelleştirin (logo, renkler, kişiselleştirilmiş mesajlar)
- E-posta Ayarları**: Alınan ödemeler için e-posta bildirimlerinin yapılandırılması
- Erişim Belirteçleri**: E-ticaret entegrasyonları (WooCommerce, Shopify, vb.) için API belirteçlerinin yönetimi
- Kullanıcılar**: Farklı izin seviyeleriyle (Sahip, Misafir) mağazaya kullanıcı erişimini yönetin
- Webhooks**: Muhasebe veya ERP sisteminizle gerçek zamanlı senkronizasyon için Webhook yapılandırması



BTCPay Server ayrıca e-ticaret entegrasyonları, satış noktası sistemleri ve ek araçlarla işlevselliği genişletmek için bir Eklentiler bölümü sunar.



![Gestion des plugins](assets/fr/16.webp)



## Yerel kullanımın avantajları ve sınırlamaları



**BTCPay Sunucusunun Umbrel'e Göre Avantajları** :




- Tam egemenlik: özel anahtarların ve fonların münhasır kontrolü, hiçbir üçüncü taraf ödemelerinizi donduramaz veya sansürleyemez
- Önemli tasarruflar: geleneksel işlemcilerde %2-3'e karşılık yalnızca Bitcoin ağ maliyetleri (Lightning'de birkaç sent)
- Maksimum gizlilik: kayıt, kimlik doğrulama veya üçüncü taraf şirketlerle veri paylaşımı yok
- Açık kaynak mimarisi, geniş bir geliştirici topluluğu aracılığıyla şeffaflığı, denetlenebilirliği ve sürdürülebilirliği garanti eder
- Umbrel aracılığıyla ileri teknik becerilere ihtiyaç duymadan kolay kurulum



**Önemli sınırlamalar** :




- Yalnızca yerel ağ**: Umbrel üzerindeki BTCPay Sunucusuna yalnızca ev ağınızdan erişilebilir. Yüz yüze faturalandırma, freelance hizmetler veya küçük fiziksel işletmeler için mükemmeldir, ancak herkese açık çevrimiçi mağazalar için uygun değildir.
- Tam teknik sorumluluk: düğüm bakımı, düzenli yedeklemeler, bağlantı izleme
- Yıldırım likidite yönetimi: yeterli gelen kapasiteye sahip kanalların açılması ve yönetilmesi
- Ticari bir müşteri hizmetleri departmanından daha fazla özerklik gerektiren, topluluk dokümantasyonu ve forumlarla sınırlı destek



Bu yerel ağ sınırlaması, BTCPay Sunucusunun, müşterilerin İnternet üzerindeki herhangi bir yerden ödeme sayfalarına erişebilmeleri gereken bir e-ticaret mağazasına entegre edilmesinin önündeki ana engeldir.



## En iyi uygulamalar ve güvenlik



Otomatik Umbrel yedeklemelerini etkinleştirin ve bir kopyasını harici ortamda (USB bellek, sabit disk, şifrelenmiş bulut) saklayın. Bitcoin tohumlarınızı (kurtarma cümleleri) güvenli, fiziksel olarak ayrı bir yerde saklayın. Lightning kurtarma için LND'nın channel.backup dosyasını yedekleyin.



Bitcoin Core senkronizasyonunu, Lightning kanallarını ve BTCPay Sunucu yanıtını düzenli olarak izleyin. Basit bir haftalık test: generate ve birkaç satoshis için bir fatura ödeyin. Umbrel'i güncel tutun (güvenlik yamaları, geliştirmeler). Büyük güncellemelerden önce bir yedekleme yapın. Profesyonel kullanım için, e-posta/SMS uyarıları ile harici izlemeyi (UptimeRobot) düşünün.



## Çevrimiçi bir mağaza için BTCPay Sunucusunu herkese açık hale getirme



BTCPay Server'ı web tabanlı bir e-ticaret mağazasına (WooCommerce, Shopify vb.) entegre etmek için müşterilerinizin ödeme sayfalarına yalnızca yerel ağınızdan değil, her yerden erişebilmesi gerekir.



**Çözüm: Nginx Proxy Yöneticisi**



Nginx Proxy Manager (Umbrel App Store'da mevcuttur) kullanarak BTCPay Sunucusunu herkese açık hale getirebilirsiniz. Bu çözüm şunları gerektirir :




- Bir alan adı (klasik veya DuckDNS, No-IP, Afraid.org üzerinden ücretsiz)
- Yönlendiricinizde bağlantı noktası yönlendirmeyi (80 ve 443 numaralı bağlantı noktaları) yapılandırma
- SSL sertifikalarını otomatik olarak yöneten Nginx Proxy Manager'ın kurulumu



Bu yapılandırma sunucunuzu internete açık hale getirir ve ekstra dikkat gerektirir (güçlü parolalar, 2FA, düzenli güncellemeler). Bu prosedürün tamamını detaylandıran özel bir eğitim hazırlayacağız.



## Sonuç



Umbrel üzerindeki BTCPay Sunucusu, Bitcoin düğümünün gücünü Umbrel'in basitliği ile birleştirerek herkesin erişebileceği, kendi kendine barındırılan profesyonel bir ödeme altyapısı oluşturur. Bu finansal egemenlik bir bakım sorumluluğuyla birlikte gelir, ancak Umbrel, faydalarına kıyasla operasyonel yükü büyük ölçüde basitleştirir: işlem ücretlerinin ortadan kaldırılması, gizliliğinizin korunması, sansüre karşı direnç ve fonlarınızın tam kontrolü.



Yerel ağ kullanımı halihazırda çok çeşitli uygulamaları kapsamaktadır: serbest hizmetler için faturalandırma, yüz yüze ödemeler, küçük fiziksel mağazalar veya sadece kontrollü bir ortamda Bitcoin ve Lightning'i öğrenme ve deneme. Herkese açık olmayı gerektiren e-ticaret ihtiyaçları için Nginx Proxy Manager çözümü mevcuttur, ancak özel bir eğitimde detaylandıracağımız ek teknik yapılandırma gerektirir.



İster bir işletme, ister yeni başlayan bir proje yürütüyor olun, ister sadece deneme yapıyor olun, Umbrel'deki BTCPay Sunucusu tam bir finansal özerklik sunar. Yol, ilk mağazanızla, ilk faturanızla, doğrudan egemen altyapınıza alınan ilk ödemenizle başlar.



## Kaynaklar



### Resmi belgeler




- [Resmi BTCPay Sunucu web sitesi](https://btcpayserver.org)
- [BTCPay Sunucu belgelerinin tamamı](https://docs.btcpayserver.org)
- [GitHub BTCPay Sunucusu](https://github.com/btcpayserver/btcpayserver)
- [Tailscale belgeleri](https://tailscale.com/kb)


### Topluluk ve destek




- [Forum BTCPay Sunucusu](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)