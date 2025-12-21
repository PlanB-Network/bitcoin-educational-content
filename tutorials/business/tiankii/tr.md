---
name: Tiankii
description: Perakendeciler ve tüketiciler için Lightning araç paketi
---

![cover](assets/cover.webp)



Bitcoin ekosisteminde, ödemeleri gerçek zamanlı olarak kabul etmek işletmeler ve bireyler için büyük bir zorluk olmaya devam etmektedir. Geleneksel çözümler genellikle ileri düzeyde teknik bilgi, bakımı karmaşık bir altyapı gerektirmekte veya fonların aracılar tarafından tutulmasını gerektirmektedir. Bu durum, Lightning Network'ın teknolojik ilerlemelerinin vaatlerine rağmen, Bitcoin'in günlük bir para birimi olarak kitleler tarafından benimsenmesini engellemektedir.



2021'de doğan Salvadorlu bir şirket olan Tiankii, erişilebilir, modüler bir Bitcoin altyapısı sunarak bu soruna yanıt veriyor. Tiankii, kapalı bir ekosistemin benimsenmesini zorlamak yerine, herkesin fonlarının kontrolünden ödün vermeden Bitcoin Lightning'i işlerine entegre etmelerini sağlayan birbirine bağlı bir araç paketi sunuyor.



## Tiankii nedir?



### Kökeni ve felsefesi



Nahuatl dilinde "herkesin erişebileceği açık hava pazarı" anlamına gelen Tiankii, El Salvador'un ilk %100 Bitcoin start-up'ıdır. Bitcoin'ün ülkenin yasal ödemesi olarak kabul edilmesinin ardından Darvin Otero tarafından kurulan şirket, Bitcoin'ü bir değer deposundan günlük alışverişler için işlem yapılabilir bir para birimine dönüştürmeyi amaçlıyor. Saklama platformlarının aksine Tiankii, kullanıcıların fonlarının kontrolünü ellerinde tuttukları ve altyapının yalnızca teknik bir aracı olarak hizmet verdiği saklama dışı bir yaklaşım benimsiyor.



### Teknik mimari



Tiankii, Lightning Network tabanlı Bitcoin-as-a-Service altyapısının sağlayıcısı olarak konumlanmaktadır. Bu ikinci katman teknolojisi, ihmal edilebilir maliyetlerle neredeyse anlık işlemlere olanak tanıyarak mikro ödemeleri ve günlük alışverişleri mümkün kılmaktadır.



Mimari üç sütun üzerine kurulmuştur:



**Önce Lightning**: Büyük miktarlar için on-chain işlem desteğini korurken, hızı ve düşük maliyetleri nedeniyle Lightning ağını sistematik olarak tercih edin.



**Açık standartlar**: Ödeme taleplerini otomatikleştirmek için LNURL kullanımı, okunabilir e-posta kimlikleri için Lightning Address ve birlikte çalışabilir NFC ödemeleri için Bolt Kartı.



**wallet'dan bağımsız modülerlik**: Farklı Lightning portföylerini (LNbits, Blink, BlueWallet) veya kendi düğümünüzü bağlama imkanı, gerekli uzmanlık ve özerklik düzeyine bağlı olarak maksimum esneklik sunar.



## Tiankii ekosistem araçları



### Bitcoin POS - Mağaza içi ödeme terminali



Uygulama, akıllı telefonu veya tableti bir Lightning terminaline dönüştürür. Satıcı tutarı yerel para birimi cinsinden girer ve uygulama bir Lightning QR kodu oluşturur veya bir Bolt Kartı kabul eder. İşlemler, 150'den fazla para biriminde otomatik dönüştürme, bahşiş yönetimi ve satış geçmişi ile komisyonsuz olarak anında kredilendirilir.



### Merchant Dashboard - Birleşik satış yönetimi



Interface web, wallet Lightning'i bağlamak, işlemleri gerçek zamanlı olarak izlemek, fatura ve generate muhasebe raporları düzenlemek için merkezileştirilmiştir. Platform tüm kanalları bir araya getirir: mağaza içi ödemeler (POS), çevrimiçi satışlar (e-ticaret eklentileri) veya API entegrasyonları. Ödemeler seçilen wallet üzerinde birleşir.



### Bitcoin Temassız Kart (Bolt Kart)



NFC Bolt Kartı, Tiankii'nin Bitcoin'i halk için demokratikleştirme konusundaki en büyük yeniliğini temsil etmektedir. Temassız bir banka kartı gibi çalışan bu kart, Bitcoin Lightning satın alımları için sadece uyumlu bir terminale dokunarak ödeme yapmanızı sağlar.



Geleneksel saklama çözümlerinin aksine, bu kart birlikte çalışabilirliği garanti eden açık bir standardı takip eder. Kullanıcılar IBI uygulaması aracılığıyla kendi wallet'lerine bağlayabilir, böylece özel anahtarlarını ve ilgili fonlar üzerindeki tam kontrollerini koruyabilirler. Ödeme sadece bir saniye sürer, ödeme sırasında akıllı telefonunuzu çıkarmanıza veya aktif bir internet bağlantısına sahip olmanıza gerek yoktur.



Bu çözüm özellikle akıllı telefonlara aşina olmayan kişiler için kapsayıcıdır ve Bitcoin ekonomisine erişilebilir bir geçit sunar.



### IBI Uygulaması - Interface bireysel Bitcoin



IBI uygulaması (Bireysel Bitcoin Interface), Bitcoin Lightning'i günlük olarak kullanmak isteyen bireyler için tasarlanmıştır. Ana avantajı, e-posta formatında okunabilen bir ödeme tanımlayıcısı olan kişiselleştirilmiş bir Address Lightning'in oluşturulmasında yatmaktadır (örnek: alice@ibi.me).



Bu tanımlayıcı, ödemelerin alınmasını büyük ölçüde kolaylaştırır: her işlem için generate yeni bir faturaya gerek yoktur, gönderen sadece Lightning adresini girebilir. Arayüz ayrıca Bolt Kartınızı yönetmenize (etkinleştirme, devre dışı bırakma, harcama limitleri), çeşitli Lightning cüzdanlarına bağlanmanıza ve QR kodlarını tarayarak ödeme yapmanıza olanak tanır.



### E-ticaret eklentileri



WooCommerce, Shopify ve Cloudbeds için kullanıma hazır entegrasyonlar. Ödeme işlemine Bitcoin Lightning eklemek için dakikalar içinde yüklenir. Faydaları: sıfır komisyon (%2-3 kredi kartlarına kıyasla), anında ödeme, dünya çapında erişim, ters ibrazların ortadan kaldırılması. Ödemeler doğrudan satıcının bağlı wallet'una ulaşır.



### Bitcoin API ve geliştirici araçları



Tiankii SDK, Bitcoin Lightning'in kendi düğümünü korumadan mevcut uygulamalara entegre edilmesini mümkün kılar. API, Google Cloud üzerinde barındırılan sağlam bir altyapı aracılığıyla fatura oluşturma, ödeme doğrulama ve toplu postalama işlemlerini gerçekleştirir. Command Center, özel etki alanları, toplu ödemeler ve NFC terminalleri ve kartlarının merkezi yönetimi konusunda Address Lightning'e sahip kuruluşlar için teklifi tamamlar.



## Kurulum ve ilk adımlar



### Temel ön koşullar



Tiankii'yi kullanmak karmaşık teknik önkoşullar gerektirmez. Uygulamalar akıllı telefon, tablet veya bilgisayardaki bir web tarayıcısı üzerinden çalışır. Yerel uygulama kurulumu gerekmez: IBI veya Satıcı Panosuna erişmek için tek ihtiyacınız olan İnternet erişimi ve yeni bir tarayıcıdır.



**Özel kullanıcılar için (IBI Uygulaması)**: Önceden wallet Lightning gerekmez. Hesabınızı oluşturduğunuzda Tiankii, arka planda Liquid ağını kullanan düğümsüz bir uygulama olan [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html) aracılığıyla çalışan bir Address Lightning'i otomatik olarak yapılandırır. Herhangi bir teknik yapılandırma olmadan hemen ödeme alabilir ve gönderebilirsiniz. Bu çözüm, yeni başlayanlar için erişimi büyük ölçüde basitleştirirken, kendi kendine gözetim altında kalır.



**Satıcılar için (Satıcı Panosu)** : Satış Noktası terminallerini kullanmak ve ödeme almak için mevcut bir wallet Lightning bağlantısı zorunludur. Tiankii birçok çözümü destekler: mobil cüzdanlar (Blink, Strike), kendi kendine barındırılan çözümler (LNbits, LND/CLN node) veya web cüzdanları (Alby). Ayrıntılı bağlantı kılavuzları bu eğitimin Kaynaklar bölümünde mevcuttur.



### Özel müşteriler için: IBI Uygulaması



**Hesap oluşturma



Hesabınızı oluşturmak için accounts.ibi.me adresine gidin. Bu sayfada iki hesap türü arasında seçim yapabilirsiniz: bireysel kullanım için "Kişisel Kullanım" veya ticari kullanım için "Ticari Kullanım". Bitcoin'de ödeme alma ve gönderme araçlarına erişmek için "Kişisel Kullanım "ı seçin.



![Choix du type de compte](assets/fr/01.webp)



"Kişisel Kullanım" seçeneğini seçtikten sonra, kaydınızı tamamlamak için otomatik olarak go.ibi.me adresine yönlendirileceksiniz. Bu işlem e-posta, telefon numarası veya Google, Microsoft veya Twitter hesabınız kullanılarak yapılabilir. Oluşturulduktan sonra, Lightning Address'niz zaten çalışır durumdayken IBI arayüzünüze hemen erişebilirsiniz.



![Création du compte](assets/fr/02.webp)



**Interface ana**



IBI arayüzü bakiyenizi satoshi ve yerel para birimi (USD) cinsinden gösterir. Üç düğme etkileşim kurmanızı sağlar: Ödeme almak için "Al", QR kodu taramak için "Tara" ve satoshi göndermek için "Gönder".



![Interface IBI](assets/fr/03.webp)



**Ödemeyi al**



Satoshileri almak için "Al" düğmesine basın. Uygulama otomatik olarak bir QR kodu oluşturur ve kişiselleştirilmiş Address Lightning'inizi görüntüler (nom@ibi.me formatında). Bu adresi veya QR kodunu gönderici ile paylaşın: para anında IBI hesabınıza ulaşır.



![Réception avec Lightning Address](assets/fr/04.webp)



Bakiyeniz kredilendirildikten sonra, bu satoshileri ödeme yapmak için kullanabilirsiniz.



**Ödeme gönderin**



Satoshi göndermek için "Gönder "e basın. Bir Lightning QR kodunu tarayabilir veya doğrudan bir Lightning Address hedefi girebilirsiniz.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



İstediğiniz tutarı satoshi cinsinden girin, yerel para birimindeki eşdeğer tutarı kontrol edin ve ardından ödemeyi onaylayın.



![Confirmation du montant](assets/fr/07.webp)



Bir başarı bildirimi, gönderilen miktar, işlem ücreti ve alıcı gibi ayrıntılarla birlikte gönderiyi onaylar.



![Paiement réussi](assets/fr/08.webp)



**Hesap yönetimi



Ayarlar'da Bitcoin NFC kartlarınızı (Bolt Kartları) yönetebilirsiniz. Arayüz, kartlarınızı etkinleştirmenizi, devre dışı bırakmanızı veya kartlarınız için harcama limitleri belirlemenizi sağlar.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Tüccarlar için: Satıcı Kontrol Paneli ve POS



**İşletme hesabı oluşturma



Hesabınızı oluşturmak için accounts.ibi.me adresine gidin. Satıcı araçlarına erişmek için "Ticari Kullanım "ı seçin. Bu hesap türü, Satıcı Panosuna ve satış noktası terminallerine erişimin kilidini açar.



"Ticari Kullanım "ı seçtikten sonra otomatik olarak Satıcı Panosuna (pay.tiankii.com) yönlendirileceksiniz. Bu sizi gelir takibi, işlemler ve ödeme araçlarını içeren işletme yönetimi arayüzüne götürür. Ödemeleri kabul etmeye başlamak için önce sayfanın üst kısmındaki bağlantıya tıklayarak wallet Lightning'inizi bağlamanız gerekir (resimdeki oka bakın).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** bağlantısı



Satış noktanızı etkinleştirmenin en önemli adımı: ödemeleri almak için wallet Lightning'inizi bağlayın. Arayüz çeşitli bağlantı seçenekleri sunar. Lütfen bazı seçeneklerin (Bitcoin Onchain ve Lightning Network) hala geliştirilme aşamasında olduğunu ve arayüzde gri renkte göründüğünü unutmayın.



![Options de connexion wallet](assets/fr/12.webp)



Bu eğitim için Chivo, Blink Wallet ve Strike ile uyumlu Lightning Address bağlantısını kullanıyoruz. Lightning Address'ünüzü (nom@domaine.com formatında) girin, örneğin LN Markets, Alby veya diğer uyumlu tedarikçilerden.



![Saisie de la Lightning Address](assets/fr/13.webp)



Giriş yaptıktan sonra hesabınız çalışır durumdadır. Artık POS'a erişebilir veya diğer ayarları yapılandırmak için kontrol paneline dönebilirsiniz.



![Connexion réussie](assets/fr/14.webp)



*ödeme Bağlantıları** *Ödeme Bağlantıları



"Ödeme Araçları" menüsü, ödeme bağlantıları oluşturmanızı ve yönetmenizi sağlayan "Ödeme Talebi "ne erişim sağlar. Bu özellik, e-posta veya mesajla gönderilecek kişiselleştirilmiş ödeme bağlantıları oluşturmak için kullanışlıdır: bağışlar, tek ödemeler, çoklu ödemeler ve hatta içeriği korumak için ödeme duvarları. İş ihtiyaçlarınıza uygun farklı bağlantı türleri oluşturabilirsiniz.



![Liens de paiement](assets/fr/15.webp)



**Satış terminali yapılandırması**



Mağaza içi ödemeleri kabul etmek için "Ödeme Araçları "ndan "Satış Terminali" menüsüne erişin. Bu bölüm POS terminallerinizi oluşturmanızı ve yönetmenizi sağlar (terminal sayısı planınıza bağlıdır, aşağıdaki Freemium ve Business planlarına bakın). Tarayıcınızda POS arayüzünü açmak için "Aç "a tıklayın.



![Gestion des terminaux](assets/fr/16.webp)




**Satış oluşturmak**



POS terminali satış tutarını girmek için sayısal bir tuş takımı görüntüler. Tutarı yerel para biriminizde girin (örneğin 500 sats 630,74 ARS'ye karşılık gelir), ardından onaylamak için "OK" tuşuna basın.



![Saisie du montant](assets/fr/17.webp)



Uygulama anında bir Lightning QR kodu ve ödeme için bir Lightning Address oluşturur. Müşteriler QR kodunu wallet ile tarayabilir veya Bolt Kartlarını bir NFC terminalinde kullanabilirler.



![QR code de paiement](assets/fr/18.webp)



Ödeme alınır alınmaz, yerel para birimi ve satoshi cinsinden alınan tutarı gösteren bir onay ekranı görüntülenir. E-posta ile bir makbuz gönderebilir, bileti yazdırabilir veya hemen yeni bir satış başlatabilirsiniz.



![Paiement encaissé](assets/fr/19.webp)



**İzleme ve yönetim**



Tüm işlemler Satıcı Kontrol Panelinize kaydedilir. Dönemlere göre gelirlerin, toplam satış sayısının ve muhasebeniz için ayrıntılı geçmişin eksiksiz takibine sahip olursunuz.



Ayarlar arayüzü çeşitli yapılandırma sekmeleri sunar. "Genel Ayarlar" sekmesi satıcı profilinizi ve bildirimlerinizi yönetmenizi sağlar. "Kullanıcılar" sekmesi, ekibiniz için Satıcı Panosuna erişim eklemenizi ve yönetmenizi sağlar (planınıza göre çoklu kullanıcı yönetimi). "Geliştirme Çalışma Alanı" sekmesi gelişmiş entegrasyonlar için API anahtarlarına erişim sağlarken, "Abonelik" aboneliğinizi yönetmenizi sağlar.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs Kurumsal planlar



Tiankii, Merchant Dashboard için iki paket sunmaktadır. Freemium** planı (ücretsiz), sınırlamaları olan yeni başlayanlar için uygundur: tek bir satış noktası, tek bir kullanıcı, 1.000 USD ile sınırlı aylık hacim ve e-ticaret konektörlerine erişim yok. Business** planı (işlem başına %0,5 ücret) sınırsız terminal, sınırsız kullanıcı, sınırsız hacim, WooCommerce/Shopify/Cloudbeds eklentilerine erişim ve özel WhatsApp bildirimleri sunar.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Avantajlar ve kısıtlamalar



### Önemli Noktalar



**Kendi kendine emanet**: Özel anahtarlarınız ve fonlarınızın tam kontrolü sizde kalır. Hesap dondurma veya üçüncü taraf platform iflası riski yok.



**Basitlik**: E-posta adresi olarak Lightning Address, basit bir dokunuşla NFC ödemeleri, teknik uzmanlık gerektirmeyen sezgisel arayüz.



**Eksiksiz ekosistem**: İhtiyaçlarınıza uygun modüler entegrasyonlarla tüm profiller (bireyler, perakendeciler, geliştiriciler) için araçlar.



**Profesyonel uyumluluk**: Güvenli bulut barındırma, PCI-DSS uyumluluğu, Salvador mevzuat uyumluluğu.



### Sınırlamalar



**Yıldırım kısıtlamaları**: Kalıcı wallet bağlantısı, büyük hacimler için likidite yönetimi, alıcının çevrimdışı olması durumunda arıza riski gerektirir. Tiankii bu hususları entegre LSP'ler ile hafifletmektedir.



**SaaS bağımlılığı**: Tiankii kullanılamıyorsa, fatura oluşturma geçici olarak imkansızdır (fonlarınız güvende kalır).



**Gizlilik**: Tiankii işlem meta verilerini (tutarlar, tarihler) gözlemleyebilir. BTCPay Server gibi kendi kendine barındırılan bir çözümden daha az gizlidir.



## Sonuç



Tiankii, iyi tasarlanmış bir altyapının Bitcoin'ün günlük para birimi olarak kitleler tarafından benimsenmesini engelleyen teknik engelleri nasıl ortadan kaldırabileceğini göstermektedir. Lightning Network'ün gücünü gözetimci olmayan bir yaklaşım ve erişilebilir araçlarla birleştiren ekosistem, finansal egemenlik ile kullanım kolaylığı arasında dengeli bir yol sunuyor.



Tüccarlar için Tiankii, yeni bir müşteri tabanına erişirken işlem maliyetlerini önemli ölçüde azaltma fırsatını temsil etmektedir. Tüketiciler için ise Lightning Address ve NFC kartları, Bitcoin'yı teknik karmaşıklık olmadan pratik bir para birimine dönüştürüyor.



Bitcoin'nin yaygın olarak benimsenmesi eğitim ve zaman gerektiren bir zorluk olmaya devam etse de, Tiankii gibi altyapılar teknik araçların zaten var olduğunu göstermektedir. Bitcoin ödemelerini basitleştirme misyonu artık uzak bir vizyon değil, adım atmak isteyen herkesin erişebileceği bir gerçekliktir.



## Kaynaklar



### Resmi belgeler




- [Tiankii resmi web sitesi](https://tiankii.com)
- [Tiankii Yardım Merkezi](https://help.tiankii.com)
- [IBI başvurusu](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Komuta Merkezi](https://cc.ibi.me)



### Wallet bağlantı kılavuzları




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Topluluk




- [Lightning Network Plus](https://lightningnetwork.plus) - Yıldırım eğitim kaynağı
- [Bitcoin Plajı](https://www.bitcoinbeach.com) - Salvadorlu döngüsel ekonomi girişimi Bitcoin



### İlgili araçlar




- [Blink Wallet](https://blink.sv) - Wallet Lightning uyumlu önerilir
- [LNbits](https://lnbits.com) - Kendi kendine barındırılan wallet çözümü
- [Standart Bolt Kartı](https://github.com/boltcard) - NFC kartları için teknik özellikler