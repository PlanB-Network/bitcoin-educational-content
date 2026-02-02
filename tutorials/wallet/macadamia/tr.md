---
name: Macadamia Wallet
description: Anonim ve anında BTC ödemeleri için Cashu mobil wallet
---

![cover](assets/cover.webp)



Macadamia Wallet, tamamen anonim Bitcoin ödemeleri sağlayan bir Chaumian ecash sistemi olan Cashu protokolünü uygulayan bir iOS mobil wallet'tür. Kör imzalar sayesinde, hiçbir gözlemci para yatırma işlemlerinizi harcamalarınızla ilişkilendiremez ve fiziksel nakit paraya benzer bir gizlilik sunar.



Bu eğitimde, Macadamia'yı nasıl kuracağınızı ve yapılandıracağınızı, ilk Cashu işlemlerinizi (Mint, Send, Receive, Melt) nasıl gerçekleştireceğinizi ve fonlarınızı güvence altına almak için birden fazla darphaneyi nasıl yöneteceğinizi inceleyeceğiz.



## Macadamia Wallet nedir?



### Cashu protokolü



Cashu, David Chaum tarafından icat edilen kör imzaları kullanır: bitcoinleri bir "mint" sunucusuna yatırırsınız, bu sunucu da satoshis cinsinden eşdeğer tokenlar çıkarır. Darphane bu tokenleri içeriklerini görmeden imzalayarak bir token'yi bir kullanıcıya bağlamayı imkansız hale getirir. Borsalar off-chain, eşler arası ve tamamen opaktır - darphane bile kimin kime ödeme yaptığını takip edemez.



Macadamia, Swift/SwiftUI'de geliştirilmiş açık kaynaklı bir wallet iOS'tur. Hesap veya KYC olmadan çalışır, tokenleriniz yerel olarak saklanır ve bir seed ifadesi ile korunur. Kod GitHub'da denetlenebilir ve tokenler diğer Cashu cüzdanlarıyla (Minibits, Cashu.me) birlikte çalışabilir.



### Saklama modeli ve uzlaşma



**Önemli**: Cashu bir emanet modeliyle çalışır. Jetonlar, darphanenin Bitcoin rezervleri tarafından desteklenen ödeme vaatleridir (IOU'lar). Darphane ortadan kalkarsa, jetonlarınız değerini kaybeder. Bu, maksimum gizlilik için bir uzlaşmadır.



Macadamia'yı fiziksel wallet olarak kullanın: sadece küçük miktarlarda. Riski seyreltmek için fonlarınızı birkaç darphaneye dağıtın.



## Ana Özellikler



Macadamia, Cashu protokolünün dört temel işlemini uygular. **Mint** satoshilerinizi bir Lightning faturası aracılığıyla tokenlara dönüştürür. **Gönder**, QR kodu veya bağlantı yoluyla tamamen off-chain ile ücretsiz token göndermenizi sağlar. **Receive** token veya generate Lightning faturası almanızı sağlar. **Erit** jetonlarınızı yok ederek bir Yıldırım faturası öder.



wallet aynı anda birden fazla darphanenin yönetimini destekler. Lightning aracılığıyla farklı darphaneler arasında token takası yapabilirsiniz.



## Desteklenen platformlar



Macadamia yalnızca iPhone ve iPad için iOS 17 veya üzeri sürümlerde kullanılabilir. Yerel Swift/SwiftUI uygulaması Apple ekosistemi ile optimum entegrasyon sunar.



Cashu protokolü cüzdanlar arasında birlikte çalışabilirliği garanti eder. seed ifadenizi Android'de Minibits veya masaüstünde Nutstash gibi diğer uygulamalarda geri yükleyebilirsiniz.



Mevcut sürüm TestFlight aracılığıyla dağıtılmaktadır. Bu beta sürümü ile sadece küçük miktarlarda kullanın.



## Kurulum



Macadamia şu anda Apple'ın beta test programı olan TestFlight aracılığıyla kullanılabilir. İşte nasıl yükleyeceğiniz:



### TestFlight aracılığıyla kurulum



**1. Adım: TestFlight'ı indirin**



Aygıtınızda TestFlight uygulaması yoksa App Store'da "TestFlight "ı arayın ve yükleyin. TestFlight, iOS uygulamalarının beta sürümlerini test etmek için Apple'ın resmi uygulamasıdır.



**2. Adım: Macadamia beta programına katılın** (Fransızca)



TestFlight yüklendikten sonra, iPhone veya iPad'inizden bu davet bağlantısını takip edin: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Bağlantı otomatik olarak TestFlight'ı açacak ve size Macadamia Wallet'yı yüklemenizi önerecektir. İndirmeyi başlatmak için "Kabul Et" ve ardından "Yükle" seçeneğine dokunun. Uygulama yaklaşık on megabayt ağırlığındadır ve yüklenmesi sadece birkaç saniye sürer.



![Installation TestFlight](assets/fr/01.webp)



### Beta sürümleri hakkında önemli bilgiler



Macadamia hala aktif geliştirme aşamasındadır. TestFlight sürümleri sık sık güncellenir ve yeni özellikler getirebilir veya hataları düzeltebilir. Ancak, her beta sürümünde olduğu gibi, arızalar meydana gelebilir. **Teknik bir sorun olması durumunda kaybolabileceğini kabul ettiğiniz küçük miktarlarda** kullanmanızı şiddetle tavsiye ederiz.



Macadamia, görüntülenen gizlilik politikasına göre herhangi bir kullanıcı verisi toplamaz. Yüklerken geliştiricinin cypherbase UG olduğunu kontrol ettiğinizden emin olun.



## İlk yapılandırma



Macadamia ilk açılışta 12 kelimelik bir BIP-39 cümlesi oluşturur. Bunları güvenli bir yere yazın - asla ekran görüntüsü olarak değil. Bu kelimeler wallet'nizi yeniden oluşturmanızı ve jetonlarınızı harcamanızı sağlar.



![Configuration initiale](assets/fr/02.webp)



Dört adımı izleyin: hoş geldiniz, şartları kabul edin, seed cümlesini kaydedin ve son onay.



![Interface principale](assets/fr/03.webp)



Yapılandırma tamamlandığında, Macadamia üç ana sekme sunar. **Wallet** bakiyenizi ve işlem geçmişinizi görüntüler. **Mints** Cashu sunucularınızı yönetmenizi sağlar. **Ayarlar** ayarlara ve seed ifadenize erişim sağlar.



![Ajout d'un mint](assets/fr/04.webp)



Şimdi bir darphane, yani tokenlarınızı yayınlayacak bir Cashu sunucusu yapılandırmanız gerekir. "Darphaneler" sekmesine gidin, "Yeni Darphane URL'si ekle" seçeneğine dokunun ve seçtiğiniz darphanenin adresini girin (örn. mint.cubabitcoin.org). Saygın halka açık darphaneler için bitcoinmints.com veya cashu.space adreslerine göz atın. Sadece itibarını kontrol ettiğiniz darphaneleri doğrulayın, çünkü satoshilerinizin velayeti onlarda olacaktır.



## Günlük kullanım



### Yeni jetonların oluşturulması (Mint)



wallet Macadamia'nızı ecash ile beslemek için bir "Mint" işlemi gerçekleştirmeniz gerekir (jeton oluşturmak için). "Al" öğesine dokunun, ardından "Yıldırım" seçeneğini seçin. İstediğiniz miktarı girin (örneğin 1000 sats), kullanılacak nane şekerini seçin ve ardından Lightning faturasını generate seçin.



![Opération Mint](assets/fr/05.webp)



Oluşturulan Lightning faturasını her zamanki wallet (Phoenix, Zeus, BlueWallet) ile ödeyin.



![Confirmation Mint](assets/fr/06.webp)



Cashu jetonları ödeme yapıldıktan sonra anında bakiyenizde görünür.



### Jeton gönder



Cashu jetonlarını başka bir kullanıcıya göndermek için, ana ekrandaki "Gönder" düğmesine dokunun, ardından "Ecash" seçeneğini seçin. Gönderilecek miktarı girin (örneğin 50 sats) ve gerekirse açıklayıcı bir not ekleyin.



![Envoi Ecash](assets/fr/07.webp)



QR kodunu veya oluşturulan metni iMessage, Signal veya Telegram aracılığıyla paylaşın. Alıcı fonları anında ve ücretsiz olarak talep eder.



### Jetonları alın



Başka bir kullanıcı tarafından gönderilen Cashu jetonlarını almak için "Al" öğesine dokunun ve ardından "Ecash" öğesini seçin. token QR kodunu tarayın veya aldığınız token bağlantısını yapıştırın.



![Réception Ecash](assets/fr/08.webp)



token'u talep etmek için "Redeem "a dokunun.



### Yıldırım (Erime) ödemeleri



Cashu tokenlarınızla bir Lightning faturası ödemek için "Gönder "e dokunun ve ardından "Lightning "i seçin. Ödemek istediğiniz bir BOLT11 faturasını yapıştırın.



![Paiement Lightning](assets/fr/11.webp)



Darphane tokenlarınızı yok eder ve Lightning ödemesini gerçekleştirir. Böylece anonimliğinizi koruyarak herhangi bir Lightning hizmeti için ödeme yapabilirsiniz.



### Naneler arasında değişim



Yapılandırmadığınız bir darphaneden jeton aldığınızda, Macadamia bu jetonları yönetmeniz için size çeşitli seçenekler sunar.



![Swap inter-mints](assets/fr/09.webp)



Yeni darphaneyi ekleyin veya tokenları mevcut bir darphaneyle takas edin. Takas, fonlarınızı anonim olarak aktarmak için Lightning'i bir köprü olarak kullanır.



### Gelişmiş çoklu darphane yönetimi



Macadamia, aynı anda birden fazla darphaneyi yönetmek ve fonlarınızı stratejik olarak tahsis etmek için sofistike araçlar sunar.



![Gestion multi-mints](assets/fr/10.webp)



"Fonları Dağıt" bakiyenizi otomatik olarak yüzdelere göre dağıtır (örneğin 50/50). "Transfer", risklerinizi çeşitlendirmek için madenler arasında manuel transferlere izin verir.



## Avantajlar ve sınırlamalar



**Öne Çıkanlar** :





- Maksimum gizlilik**: Darphane tarafından bile takip edilemeyen işlemler. Blok zinciri meta verisi yok, iz bırakmayan eşler arası değişimler.
- Hızlı ve ücretsiz**: Mikro ödemeler için ideal olan bir darphane içinde ücretsiz anında transferler.
- Birlikte çalışabilirlik**: diğer uyumlu cüzdanlarla (Minibits, Nutstash) kullanım için standartlaştırılmış Cashu tokenleri.
- Basitlik**: Interface iOS native, denetlenebilir (açık kaynak) kalırken yeni başlayanlar için erişilebilirdir.



**Kısıtlamalar** :





- Saklama modeli**: darphane güveni gereklidir. Bir darphane ortadan kalkarsa tokenlarınız değerini kaybeder.
- yalnızca iOS**: Android/masaüstü sürümü yok. Cashu birlikte çalışabilirliği, diğer cüzdanlar aracılığıyla erişime izin verir, ancak en uygun deneyim iOS olarak kalır.
- Mint bağımlılığı**: Mint çevrimdışı = müdahalesini gerektiren işlemleri gerçekleştiremiyor (Mint, Melt).
- Gelişmekte olan teknoloji** : Aktif geliştirme, olası hatalar, gelişen standartlar.



## En iyi uygulamalar





- Darphanelerinizi çeşitlendirin**: Riski seyreltmek için fişlerinizi birkaç saygın darphaneye dağıtın.
- Limit miktarları**: Macadamia'yı kasa olarak değil, günlük ödemeler için fiziksel bir wallet olarak kullanın.
- seed**'ünüzü güvence altına alın: 12 kelimelik cümlenizi kağıt üzerinde güvenli bir yerde saklayın. Ara sıra restorasyonu test edin.
- Darphaneleri kontrol edin**: Bir darphane eklemeden önce cashu.space ve topluluk forumlarına danışın. İyi çalışma süresine ve sağlam bir itibara sahip olanları seçin.
- VPN veya Tor**: Ağ gizliliğini en üst düzeye çıkarmak için IP'nizi VPN/Tor ile gizleyin.
- Topluluğa katılın**: Güncellemeler, darphane önerileri ve en iyi uygulamalar için Telegram/Discord Cashu grupları.



## Sonuç



Macadamia Wallet, fiziksel paranın özelliklerini dijital Bitcoin'e taşır. Chaum ve Lightning kör imzalarını birleştirerek işlem gizliliği için zarif bir çözüm sunar. Yerel iOS arayüzü, sofistike kriptografik teknolojiyi erişilebilir kılarken, açık kaynak kodlu ve Cashu ekosistemiyle birlikte çalışabilir.



Saklama modeli ihtiyat ve iyi güvenlik uygulamaları gerektirir. Doğru kullanıldığında Macadamia, anonimlik gerektiren günlük ödemeler için paha biçilmez bir araç haline gelir ve tasarruflar için saklama amaçlı olmayan cüzdanları tamamlar.



## Kaynaklar



### Resmi belgeler




- Resmi web sitesi: [macadamia.cash](https://macadamia.cash)
- Macadamia SSS: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub kaynak kodu: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu belgeleri




- Teknik dokümantasyon: [docs.cashu.space](https://docs.cashu.space)
- Halka açık darphanelerin listesi: [bitcoinmints.com](https://bitcoinmints.com)
- Resmi protokol web sitesi: [cashu.space](https://cashu.space)



### Topluluk




- Telgraf Cashu grubu: [t.me/cashu_ecash](https://t.me/cashu_ecash)