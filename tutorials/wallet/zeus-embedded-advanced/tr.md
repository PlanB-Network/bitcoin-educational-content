---
name: Zeus Embedded - İleri Düzey
description: Çok düğümlü kendi kendine gözetimli Wallet
---

![Zeus](assets/cover.webp)


## ZEUS Wallet'e Giriş


ZEUS, Bitcoin ödemelerini basitleştiren, kullanıcılara mali durumları üzerinde tam kontrol sağlayan ve daha ileri düzey kullanıcıların Lightning düğümlerini avuçlarının içinden yönetmelerine olanak tanıyan bir Bitcoin yıldırım Wallet'ün tüm işlevlerine sahip bir mobil Bitcoin Wallet ve düğüm yönetimi uygulamasıdır.


### ZEUS kimler içindir?

Şu anda ZEUS, kendi [Lightning Network Daemon (LND)](https://lightning.engineering/) veya [Core Lightning lightning (CLN)](https://blockstream.com/lightning/) ev / iş düğümlerini çalıştıran ve bunları Zeus aracılığıyla uzaktan yöneten kişiler içindir.


BTCPay](https://btcpayserver.org/) veya [LNBits](https://lnbits.com/) veya [Alby](https://getalby.com/) (veya başka herhangi bir LNDhub hesabı) kullanan tüccarlar da düğümlerine / hesaplarına ZEUS'tan bağlanabilir, bunları kullanabilir ve yönetebilir.


[v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/)'den itibaren ZEUS, entegre [Lightning Hizmet Sağlayıcısı (LSP)](https://docs.zeusln.app/lsp/intro) ile [yerleşik mobil Lightning düğümü](https://docs.zeusln.app/category/embedded-node)'ne sahip olarak mobil cihazlarından hızlı, ucuz Bitcoin ödemeleri yapmanın basit bir yolunu isteyen ortalama kullanıcılara hitap etmeye başlayacaktır.


### Önemli Zeus kaynakları:


- Zeus resmi web sayfası - [https://zeusln.app/](https://zeusln.app/)
- Zeus Dokümantasyonu - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github deposu](https://github.com/ZeusLN/zeus)
- [Zeus Telegram destek grubu](https://t.me/ZeusLN)
- [Zeus on NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus Blog Duyuruları](https://blog.zeusln.com)


### Zeus Özellikleri

#### Genel özellikler:


- Kendi kendine gözetim, Bitcoin ve Yıldırım sadece Wallet
- İşlem ücreti yok, KYC yok
- Tamamen açık kaynak (APGLv3)
- Çoklu düğüm / hesap desteği (kendi ana düğüm(ler)inizi yönetebilir, gömülü LND düğümünü çalıştırabilir, birden fazla LNDhub hesabına bağlanabilirsiniz)
- Kullanımı kolay aktivite menüsü
- PIN veya passphrase şifreleme, Gizlilik modu - hassas verilerinizi gizleyin
- İletişim defteri, çoklu tema, çoklu dil


#### Teknik özellikler


- Tor üzerinden bağlanın
- Tam LNURL desteği (Ödeme, para çekme, kimlik doğrulama, kanal), Lightning adreslerine gönderme
- Detaylı Aydınlatma kanalı yönetimi, MPP/AMP desteği, Keysend, yönlendirme ücretleri yönetimi
- Replace-by-fee (RBF) ve Ebeveyn için çocuk ödemesi (CPFP) desteği
- NFC ödemeleri ve talepleri, Mesajları imzala ve doğrula
- SegWit ve Taproot desteği
- Basit Taproot Kanalları
- Kendi kendine gözetim yıldırım adresleri (@zeuspay.com)
- Square tarafından Satış Noktası (yakında açık PoS)


### Kılavuzlar ve Video Öğreticiler

Zeus'u kullanabilmek ve Lightning kanallarını, likiditeyi, ücretleri vb. yönetebilmek için önce Lightning Network ile ilgili bazı önemli kılavuzları okumak daha iyidir.


#### Rehberler:


- [LND - Lightning Network Daemon Dokümantasyonu](https://docs.lightning.engineering/)
- [CLN - Core Lightning Documentation](https://lightning.readthedocs.io/index.html)
- [Yeni Başlayanlar için Yıldırım Kılavuzu](https://bitcoiner.guide/lightning/) - Bitcoin Q&A tarafından
- [Lightning Node Management](https://www.lightningnode.info/) - openoms tarafından
- [Lightning Network ve havaalanı benzetmesi](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Yıldırım Düğümü Likiditesini Yönetme](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Yıldırım Düğümü Bakımı](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### BTC Sessions tarafından hazırlanan eğitim videosu


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Mobil cihazınızda Zeus LN gömülü düğümünü kullanmaya nasıl başlayacağınızı anlatan bir kılavuz


![Image](assets/en/01.webp)


Bu kılavuzu, mobil cihazlarında kendi kendine saklama düğümü Wallet kullanarak yeni bir egemen yolculuğa başlamak isteyen tüm yeni Lightning Network (LN) kullanıcılarına ithaf ediyorum.


Tüm bu gözetimli LN cüzdanlarından zaten geçtiğinizi düşünelim, ancak henüz bir PUBLIC yönlendirme LN düğümü çalıştırmaya hazır değilsiniz, sadece Sats üzerine daha fazla LN istiflemek ve düzenli ödemelerinizi LN üzerinden yapmak istiyorsunuz.


İşte Zeus, [bloglarında duyurulan v0.8.0 sürümü] (https://blog.zeusln.com/new-release-zeus-v0-8-0/) ile başlayarak, artık uygulamaya gömülü bir LND düğümü sunuyor. Şimdiye kadar Zeus bir uzaktan düğüm yönetimi uygulaması + LNDhub hesaplarıydı. Ama şimdi... düğüm telefonun içinde!


![Image](assets/en/02.webp)


### Zeus Node için ana özelliklerin hızlı özeti:



- Özel LND düğümü** - Bu, bu düğümün diğer ödemeleri sizin düğümünüz üzerinden herkese açık olarak YÖNLENDİRMEYECEĞİ anlamına gelir. Düğüm ve kanallar habersizdir (özeldir, genel LN grafiğinde görünmez). Ödeme almak ve yapmak, bağlı LSP eşleriniz aracılığıyla yapılacaktır. UNUTMAYIN: Zeus Gömülü Düğümü genel yönlendirme YAPMAYACAKTIR!
- Kalıcı LND hizmeti** - kullanıcı bu özelliği etkinleştirebilir ve LND hizmetini herhangi bir normal LN düğümü gibi sürekli aktif tutabilir. Uygulamanın açık olması gerekmez, kalıcı hizmet tüm iletişimi çevrimiçi tutacaktır.
- Neutrino blok filtreleri** - blok senkronizasyonu [blok filtreleri ve Neutrino protokolü](https://bitcoinops.org/en/topics/compact-block-filters/) kullanılarak yapılır (kullanıcılarımızın On-Chain fonları hakkında hiçbir bilgi verilmemiştir). Hatırlatma: yüksek gecikmeli / yavaş internet bağlantıları için neutrino'ya dayalı bu blok senkronizasyonu bazen başarısız olabilir. Yakın bir neutrino sunucusuna geçmeyi denemek senkronizasyonu geri yüklemeye yardımcı olabilir. Bu senkronizasyon olmadan LND düğümünüz başlayamaz!
- Basit Taproot Kanalları** - Bu kanalları kapatırken, kullanıcılar daha az ücrete tabi tutulur ve On-Chain ayak izlerini incelerken diğer Taproot harcamaları gibi göründükleri için daha fazla gizlilik verilir.
- Entegre LSP** - Olympus, Zeus için yeni LSP düğümüdür. Kullanıcılar, daha önce LN kanalları kurmadan, Sats üzerinden hemen LN alabilirler. Sadece bir LN Invoice oluşturmaları ve Zeus 0-conf kanal hizmeti ile diğer herhangi bir LN Wallet'dan ödeme yapmaları gerekecektir. Zeus LSP hakkında daha fazlasını buradan okuyabilirsiniz. LSP ayrıca kullanıcılarımıza, düğümlerinin açık anahtarlarını ödeme yapanlardan gizleyen paketlenmiş faturalar sağlayarak ek gizlilik sağlar.
- Kişiler Defteri** - düzenli hedeflerinize kolay ödeme göndermek için kişileri manuel olarak kaydedebilir veya NOSTR'den içe aktarabilirsiniz.
- LNURL, LN Address gönderme ve alma için tam destek** - artık @zeuspay.com ile kendi gözetiminizdeki LN Address'yi kurabilirsiniz. Hatırlatma: Zeus'u LN kimlik doğrulaması ile giriş yapabileceğiniz sitelerde LN-auth için de kullanabilirsiniz. Çok kullanışlıdır.
- Satış Noktası** - Artık tüccar kullanıcılar kendi ürün kalemlerini kurabilir ve entegre PoS ile doğrudan Zeus'tan satış yapabilirler. Şu an için temel ihtiyaçları içerir ancak gelecekte genişletilmiş özellikler içerecektir.
- LND günlükleri** - kullanıcı LND hizmet günlüklerini gerçek zamanlı olarak okuyabilir ve bunları olası sorunları ayıklamak için kullanabilir (özellikle kötü bağlantılar için)
- Otomatik Yedeklemeler** - LN düğüm kanalları Olympus sunucusunda otomatik olarak yedeklenir. Bu otomatik yedekleme Wallet seed düğümünüzle şifrelenir (seed olmadan tamamen işe yaramaz). Kullanıcı ayrıca bir felaket kurtarma için manuel olarak bir SCB (statik kanal yedeklemesi) dışa aktarabilir.


### Zeus LN Node (LND gömülü) ile gemiye nasıl binilir


Bu kılavuzda sadece gömülü LND düğümünden bahsedeceğim ve bu muhteşem uygulamayı kullanmanın diğer yollarından (uzaktan düğüm yönetimi ve LNDhub hesapları) bahsetmeyeceğim. Diğer bağlantı türleri için lütfen [Zeus Docs sayfasına] (https://docs.zeusln.app/category/getting-started) bakın, bu çok iyi açıklanmıştır ve özel bir rehber yazmaya gerek yoktur.


#### ADIM 1 - ILK KURULUM


Zeus'un tam bir LND düğümü olması nedeniyle bazı ilk önerilerim olacak:



- Bu güçlü uygulamanın kullanımını etkileyebilecek eski bir cihaz kullanmayın. Özellikle senkronizasyon döneminde uygulama CPU ve RAM'i yoğun bir şekilde kullanabilir. Bunların eksikliği Zeus uygulamasını kullanmayı bile imkansız hale getirebilir.
- Mobil işletim sistemi olarak en az Android 11 kullanın ve mümkün olduğunca güncelleyin. IOS için de aynı şekilde, çok daha yüksek bir işletim sistemi sürümü kullanmaya çalışın.
- Veri depolama için en az 1GB disk alanına ihtiyacınız olacaktır. Zamanla daha fazla büyüyebilir, ancak veritabanını MBs seviyesine sıkıştırmak için bir işlev vardır.
- Zeus'u Tor veya Orbot hizmeti ile kullanmaya gerek YOKTUR. Lütfen işleri gereğinden fazla karmaşıklaştırmayın. Bu durumda Tor size daha fazla gizlilik sunmayacak, sadece ilk senkronizasyon için işleri daha da kötüleştirecektir. Ayrıca hangi VPN'leri kullandığınıza dikkat edin ve Neutrino sunucularına olan bağlantının gecikme süresini kontrol edin. Unutmayın, Neutrino blok filtresi cihaz kimliğinizi sızdırmaz veya izlemez, sadece bloklar sunar. LN trafiği de özel kanallara sahip bir LSP'nin arkasındadır, bu nedenle çok az bilgi dışarı çıkar, gizlilik konusunda korkmanıza gerek yoktur.
- İlk senkronizasyon için sabırlı olun, birkaç dakika sürebilir. Gecikme süresi iyi olan bir geniş bant internet bağlantısına bağlanmaya çalışın. Kendi Bitcoin düğümünüzü çalıştırıyorsanız, [neutrino hizmetini etkinleştirebilir] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) ve Zeus'unuzu dahili LAN'ı kullanarak bile kendi düğümünüze bağlayabilirsiniz, böylece maksimum hıza sahip olursunuz.


Bağlantı türünü "Gömülü düğüm" olarak ayarladığınızda, uygulama bir süre senkronizasyona başlayacaktır. Bu kısmı bitirmek için sabırla bekleyin, ardından ana Ayarlar sayfasına girin.


![Image](assets/en/03.webp)


Kısaca, Zeus'u kullanmaya başlamadan önce Ayarlar bölümlerinin her birine dalalım ve bazı ana özellikleri anlayalım:


**A - AYARLAR**


Bu, tüm uygulama için genel ayarların bulunduğu bir bölümdür


**1 - Yıldırım Hizmet Sağlayıcısı (LSP)**


Burada iki LSP hizmeti sunulmaktadır:



- _Just in time channels_ - açık kanalınız veya gelen likiditeniz olmadığında, hizmet etkinleştirilirse sizin için anında bir kanal açacaktır. Bu türden daha fazla kanal açmak istemiyorsanız bu seçenek devre dışı bırakılabilir.
- _Kanalları önceden talep edin_ - gelen kanalları Olympus LSP'den doğrudan uygulamada birden fazla seçenek ve miktarla (gelen ve giden için) satın alabilirsiniz.


LSP, düğümlerine ödeme kanalları açarak kullanıcıların Lightning Network'e bağlanmasına yardımcı olur. [LSP hakkında daha fazla bilgiyi burada bulabilirsiniz](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS, [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581) adı verilen ve yeni gömülü düğümü kullanan tüm kullanıcılar tarafından kullanılabilen yeni bir LSP'ye sahiptir.


Bu bölümde, varsayılan olarak Olympus LSP'dir (https://0conf.lnolymp.us), ancak yakında bu protokolü destekleyen başka bir 0conf LSP de ayarlayabilirsiniz.


aklında tut:_

olympus LSP ile sarılmış LN faturalarını kullanarak bir kanal açtığınızda, ayrıca 100k gelen likidite elde edersiniz! Bu, hemen daha fazla Sats almanız gerektiğinde gerçekten iyi bir seçenektir._

örnek: Bir LSP kanalı açmak için 400k Sats yatırıyorsunuz, ardından LSP Zeus düğümünüze doğru 500k Sats kapasiteli bir kanal açıyor ve yatırdığınız 400k Sats'u kendi tarafınıza doğru itiyor

"Gelen likidite" = kanalınızda almak için daha fazla "alan"._


Gelecekte Zeus'a entegre edilebilecek ve her birini alternatif olarak kullanabileceğimiz birçok başka LSP'ye sahip olabileceğimizi umuyoruz. Yeni LSP'lerin bu tür 0conf kanalları için açık bir standart benimsemeleri sadece bir zaman meselesidir.


Eğer "anında" yeni kanallar açmak istemiyorsanız, bu seçeneği devre dışı bırakabilirsiniz.


Aynı bölümde, LSP Zeus düğümünüze doğru bir kanal açtığında "Basit Taproot Kanalları talep et" seçeneğini de seçebilirsiniz. Bu Basit Taproot Kanalları daha iyi On-Chain gizliliği ve kanal kapanışında daha düşük ücretler sunar. Bunları kullanmak istememeniz için sadece iki neden vardır:



- Bunlar yenidir ve bunları kullanırken LND'de hala hatalar olabilir.
- Karşı tarafınız bunları desteklemiyor. LND düğümlerinin bile şimdilik bunları açıkça seçmesi gerekiyor.


**2 - Ödeme ayarları**


Bu özellik size LN veya onchain üzerinden ödemeler için kendi tercih ettiğiniz ücretleri belirlemenin yolunu sunacaktır. Ayrıca faturalarınız için zaman aşımını artırma veya azaltma seçeneği de sağlar.


LN ödemelerinizden bazıları başarısız olursa, daha iyi bir rota bulmak için ücreti artırabilirsiniz. Ayrıca zincirleme tx'ler yapıyorsanız, belirli bir ücret belirleyebilirsiniz, böylece yüksek ücret dönemlerinde tx'iniz uzun süre Mempool'te takılı kalmayabilir.


**3 - Fatura ayarları**


Bu bölümde generate faturaları için bazı seçenekler bulunmaktadır:



- Invoice'da görüntülenecek standart bir not ayarlayın generate
- Invoice'inizin ödenmesi için belirli bir süre, daha uzun veya daha kısa süre istemeniz durumunda saniye cinsinden sona erme süresi
- Rota ipuçlarını ekleyin - reklamı yapılmayan veya özel kanalları bulmak için bilgi sağlayın. Bu, ödemelerin ağda herkese açık olarak görünmeyen düğümlere yönlendirilmesine olanak tanır. Bir yönlendirme ipucu, alıcının özel düğümü ile herkese açık bir düğüm arasında kısmi bir rota sağlar. Bu yönlendirme ipucu daha sonra alıcı tarafından oluşturulan Invoice'e dahil edilir ve ödeyene verilir. Varsayılan olarak etkinleştirilmesini öneririm, aksi takdirde gelen ödemeler başarısız olabilir (rota bulunamadı).
- AMP Invoice - Atomik Çok Yollu Ödemeler, [Keysend] (https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend) kullanarak belirli bir Invoice olmadan Sats almaya izin veren LND tarafından uygulanan yeni bir Lightning ödeme türüdür. Pratik olarak statik bir ödeme kodudur. [Daha fazlasını buradan okuyun](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Özel ön resim alanını göster - bu seçeneği yalnızca ön resimde gerçekten özel alanlar kullanmak istediğiniz çok özel durumlarda kullanın. [Daha fazlasını buradan okuyun](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Bu bölümdeki bir diğer seçenek de kullanmak istediğiniz zincir üstü Address türünü nasıl ayarlayacağınızdır: SegWit iç içe, SegWit, Taproot.


![Image](assets/en/04.webp)


Üstteki tekerlek düğmesine tıklayın ve istediğiniz Address türünü seçmek için bir açılır ekran belirecektir. Bunu ayarladıktan sonra, bir sonraki sefer onchain için alma düğmesine bastığınızda, seçilen Address tipi generate olacaktır. İstediğiniz zaman değiştirebilirsiniz.


**4 - Kanal ayarları**


Bu bölümde, aşağıdaki gibi bazı açılış kanalları özelliklerini önceden ayarlarsınız:



- onay sayısı
- Kanalı duyur (varsayılan olarak kapalıdır), bu duyurulmamış kanallar olacağı anlamına gelir
- Basit Taproot Kanalları
- Kanal satın alma düğmesini göster


**5 - Gizlilik ayarları**


Burada Zeus uygulamasını kullanarak daha fazla gizlilik eklemek için bazı temel ayarları bulacaksınız:



- Block explorer tx ayrıntılarını açmak için (Mempool.space, blockstream.info veya özel kişisel bir tane)
- Panoyu oku - Zeus'un cihaz panonuzu okumasını istiyorsanız açma/kapama düğmesi
- Lurker modu - Zeus uygulamanızdan belirli hassas bilgileri gizlemek istiyorsanız açma / kapama geçişi. Demo veya ekran görüntüsü alırken iyi bir seçenektir.
- Mempool ücret önerisi - [Mempool.space] (https://Mempool.space/) adresinden önerilen ücret seviyelerini kullanmak istiyorsanız bu seçeneği etkinleştirin


**6 - Güvenlik**


Bu bölümde, açılışta uygulamanın güvenliğini sağlamak için yalnızca iki seçenek vardır: bir parola veya PIN belirleyin.


Uygulamayı açmak için bir PIN belirledikten sonra, bir "zorlama PIN'i" de belirleyebilirsiniz. Bu gizli ek PIN, tehdit altında olmanız durumunda SADECE zorlama durumunda kullanılacaktır. Bu PIN'i koyarsanız, yapılandırma tamamen SİLİNECEKTİR. Bu yüzden yedeklerinizi güncel tutsanız iyi olur. Otomatik yedeklemeler varsayılan olarak AÇIK'tır, ancak cihaz dışında kendi yedeklemelerinizin de olması iyidir.


**7 - Para Birimi**


Zeus uygulaması kullanımında fiat para birimi dönüşümünü görüntüleme seçeneğini etkinleştirin veya devre dışı bırakın. Şu anda dünya çapında 30'dan fazla fiat para birimini desteklemektedir.


**8 - Dil**


Zeus topluluğu tarafından ana dili İngilizce olan kişilerle incelenen birden fazla çeviri dili arasında geçiş yapabilirsiniz.


**9 - Ekran**


Bu bölümde Zeus ekranınızı kişiselleştirebilir, çeşitli renk temaları, varsayılan ekran (tuş takımı veya denge) seçebilir, düğüm takma adınızı gösterebilir, büyük tuş takımı düğmelerini etkinleştirebilir, daha fazla ondalık basamak gösterebilirsiniz.


**10 - Satış Noktası**


Bu, Zeus'a entegre bir PoS sistemini etkinleştirmek / devre dışı bırakmak için özel bir özelliktir. Bağımsız bir PoS çalıştırabilir veya bir Square PoS sistemine bağlayabilirsiniz. Şu anda bir PoS olarak temel işlevleri destekliyor, ancak iyi bir başlangıç için yeterli ve bu küçük tüccarların (barlar / restoranlar, marketler) BTC'yi yerel bir şekilde kabul etmeye başlamasına yardımcı olabilir.


Bu ayarların içinde, PoS'unuzu ayarlamak için çeşitli seçenekler bulacaksınız:



- Onay ödeme türü: Yalnızca LN, 0-conf, 1-conf
- PoS'u çalıştıran çalışan için ipuçlarını etkinleştirin / devre dışı bırakın
- Tuş takımını göster / gizle
- Bilet üzerinde uygulanacak vergi yüzdesi
- Ürünler ve ürün kategorileri oluşturma
- Tüm satışların basit bir listesi


İşte Zeus PoS'un nasıl kullanılacağına dair canlı bir demo video:


**B - Yedek Wallet**


ZEUS'taki gömülü düğüm LND'ü temel alır ve [aezeed seed formatını](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md) kullanır. Bu, benzer gibi görünse de çoğu Bitcoin cüzdanında gördüğünüz tipik [BIP39 formatından](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) farklıdır. Aezeed, kurtarma sırasında yeniden taramaların daha verimli bir şekilde gerçekleşmesine yardımcı olacak Wallet'in doğum tarihi de dahil olmak üzere bazı ekstra veriler içerir.


Aezeed anahtar formatı aşağıdaki mobil cüzdanlarla uyumlu olmalıdır: Blixt, BlueWallet ve Breez. Açık veya kapanmayı bekleyen kanallarınız varsa, seed'ün tek başına tüm bakiyelerinizi kurtarmak için yetersiz kalacağını unutmayın!


Yedekleme ve geri yükleme işlemi hakkında daha fazla bilgiyi [Zeus Docs sayfası] (https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery) adresinde bulabilirsiniz.


GÜÇ TAVSİYESİ: seed'inizi kaydettiğinizde, lütfen node pubkey'i de kaydedin! Bazen kurtarmayı doğrulamanız gerektiğinde seed ve SCB (Statik Kanal Yedekleme) ile birlikte elinizin altında olması iyi olur.


SCB yalnızca açık LN kanallarınız varsa gereklidir. Sadece zincir içi fonlarınız varsa, gerekli değildir.


Uzun bir süre sonra hala eski geçmiş tx'leri göstermediğini görürseniz, Embedded node - Peers'e gidin ve seçilen eşlerin listesini kullanma seçeneğini devre dışı bırakın (varsayılan olarak btcd.lnolymp.us). Bu yeniden başlatmayı tetikleyecek ve daha iyi bir zaman tepkisi ile mevcut ilk nötrino düğümüne bağlanacaktır. Ya da aşağıda belirtilen diğer iyi bilinen neutrino eşlerini kullanın.


Bir LND düğümü için daha fazla kurtarma seçeneği görmek istiyorsanız, [lütfen önceki kılavuzumu okuyun] (https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html), burada aezeed bir seed'u Sparrow wallet'ye veya diğer yöntemlere nasıl aktaracağınızı bulabilirsiniz.


**C - Gömülü Düğüm**


Bu bölümde entegre düğümü yönetmek için bazı temel araçlar bulacağız:



- _Disaster Recovery_ - LN kanalları için otomatik ve manuel yedeklemeler. Lütfen bu özelliğin nasıl kullanılacağını Zeus Docs sayfasında okuyun.
- _Express Graph Sync_ - Zeus uygulaması, daha hızlı ve daha iyi senkronizasyon için LN dedikodu veri grafiğini özel bir sunucudan indirecek ve en iyi ödeme yollarını sunacaktır. Başlangıçta önceki grafik verilerini temizlemeyi de seçebilirsiniz.
- _Peers_ - neutrino eşlerini ve 0-conf eşlerini yönetmek için bölüm. İlk senkronizasyonda sorun yaşıyorsanız, kanallar çevrimiçi olmuyorsa, bunun nedeni cihazınızın yapılandırılmış neutrino eşiyle yüksek gecikme süresine sahip olmasıdır. Tercih edilen eşler listesini değiştirmeyi deneyin veya senkronizasyon için daha iyi gecikme süresine sahip olduğunu bildiğiniz belirli eşinizi ekleyin. İyi bilinen neutrino sunucuları şunlardır:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - ABD bölgesi için
 - sg.lnolymp.us - Asya bölgesi için
 - btcd-Mainnet.lightning.computer - ABD bölgesi için
 - uswest.blixtwallet.com (Seattle) - ABD bölgesi için
 - europe.blixtwallet.com (Almanya) - AB bölgesi için
 - asia.blixtwallet.com - Asya bölgesi için
 - node.eldamar.icu - ABD bölgesi için
 - noad.sathoarder.com - ABD bölgesi için
 - bb1.breez.technology | bb2.breez.technology - ABD bölgesi için
 - neutrino.shock.network - ABD bölgesi



- _LND günlükleri_ - LN düğüm sorunlarınızda hata ayıklamak ve daha teknik bir düzeyde neler olup bittiğini derinlemesine kontrol etmek için çok kullanışlı bir araçtır.
- _Gelişmiş ayarlar_ - LND düğümünüzün kullanımını kontrol etmek için daha fazla araç:



 - _Pathfinding mode_ - bimodal veya apriori, LN ödemeleriniz için daha iyi bir rota bulmanın yolları ve ayrıca önceki rota bilgilerini sıfırlama. Lütfen yol bulma ile ilgili bu çok iyi kılavuzları okuyun: [Yol Bulma](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - Docs Lightning Engineering tarafından ve [LN Ödeme Yol Bulma](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - Voltage tarafından
 - _Persistent LND_ - LND hizmetinin arka planda sürekli çalışmasını ve düğümünüzü 7/24 çevrimiçi tutmasını istiyorsanız bu modu etkinleştirin. Zeus'u küçük bir dükkanda PoS olarak kullanıyorsanız veya LN Address üzerinden birçok LN ipucu alıyorsanız bu çok kullanışlıdır.
 - _Rescan wallet_ - bu seçenek, yeniden başlatma sırasında Wallet'inizin tüm zincir içi tx'lerinin tam taramasını tetikleyecektir. Bunu yalnızca Wallet'inizde bazı tx'lerin eksik olması durumunda etkinleştirin. Yeniden tarama görevi birkaç dakika zaman alacaktır, bu nedenle sabırlı olun ve ilerleme hakkında daha fazla ayrıntı görmek için günlükleri her zaman kontrol edin.
 - _Compact Database_ - Zeus uygulamanız cihazda çok fazla yer kaplıyorsa bu seçenek çok kullanışlıdır (cihaz ayarlarınızdaki uygulama ayrıntılarına bakın). Zeus'u kullanarak çok fazla etkinlik gerçekleştiriyorsanız, bu sıkıştırma işlemini daha sık yapmanızı tavsiye ederim. Zeus uygulaması için 1-1,5 GB'tan fazla veriniz olduğunu gördüğünüzde, sıkıştırma işlemini yapın. Yeniden başlayacak ve biraz zaman alacaktır, bu yüzden sabırlı olun.
 - _Delete Neutrino files_ - neutrino dosyalarını silmek için bu seçenek (yeniden başlatma ile) veri depolama kullanımını çok azaltacaktır. Veri kullanımının azaltılması, özellikle Zeus'u kalıcı modda kullanıyorsanız, pil kullanımını azaltarak pil kullanımında da büyük bir etkiye sahiptir.


**D - Düğüm Bilgisi**


Bu bölümde, Zeus düğümünüzün durumu hakkında daha fazla ayrıntı bulacaksınız:



- Takma ad - kısa düğüm kimliği
- Genel Anahtar - diğer düğümlerin düğümünüze giden yolu bulması için gereken düğümünüzün tam genel anahtarı. Bu ortak anahtarın normal LN Kaşiflerinde (Mempool, Amboss, 1ML vb.) GÖRÜNMEYECEĞİNİ unutmayın. Bu yayın anahtarına SADECE bağlı LN eşleriniz ve kanallarınız aracılığıyla erişilebilir.
- LN uygulama sürümü
- Zeus uygulama sürümü
- Zincirle senkronize edildi ve Grafik durumuyla senkronize edildi - çok önemli olanlar, düğümünüzün doğru durumunu gösterir. Bu ikisi "doğru" olarak görüntülenmiyorsa, düğümünüz hala senkronize ediliyor veya senkronizasyonda bazı sorunlar yaşıyor demektir. Bu nedenle LND günlüklerinize bakmanız veya biraz daha beklemeniz önerilir.
- Blok yüksekliği ve Hash - düğümünüzün gördüğü ve senkronize ettiği son bloğu ve Hash'yı gösterir.


**E - Ağ Bilgisi**


Bu bölüm, grafik senkronizasyon verilerinizden çıkarılan Lightning Network'nin genel durumu hakkında daha fazla ayrıntı görüntüler: mevcut genel kanal sayısı, düğüm sayısı, zombi kanal sayısı (çevrimdışı veya ölü), grafik çapı, grafik için ortalama ve maksimum derece.


Bu bilgi verileri hata ayıklamak için yararlı olabilir veya sadece istatistikler için kullanılabilir.


**F - Yıldırım Address**


Bu bölümde kullanıcı kendi öz saklama LN Address @zeuspay.com'unu kurabilir.


ZEUS PAY, 7/24 çevrimiçi olamayan kullanıcıların statik bir yıldırım Address'e ödeme almalarını sağlamak için kullanıcı tarafından oluşturulan ön imaj karmalarından, HODL faturalarından ve Zaplocker Nostr tasdik planından yararlanır. Kullanıcıların ödemeleri talep etmek için 24 saat içinde ZEUS cüzdanlarına giriş yapmaları yeterlidir, aksi takdirde gönderene iade edilirler.


"Kalıcı modu" etkinleştirirseniz, LN Address'ünüze yapılan tüm ödemeler anında alınacaktır.


Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) ödemelerinin nasıl çalıştığı ve [ZeusPay Ücretleri burada](https://docs.zeusln.app/lightning-Address/fees) hakkında daha fazla bilgi edinin.


**G - Zincirleme Adresler**


Bu bölümde, daha iyi bir Coin kontrolü için oluşturduğunuz zincir içi adreslere başvurabilirsiniz


**H - Kişiler**


Zeus v 0.8.0'da, arkadaşlarınıza ve ailenize hızlı bir şekilde ödeme göndermek için kullanabileceğiniz ve ayrıca kişilerinizi Nostr'dan içe aktarabileceğiniz yeni bir kişi defteri tanıtıldı.


Sadece Nostr npub veya insan tarafından okunabilir NIP-05 Address girin ve ZEUS tüm kişileriniz için Nostr'ı sorgulayacaktır. Buradan bir kişiye hızlı bir ödeme gönderebilir veya tüm kişileri veya belirli kişileri yerel kişi defterinize aktarabilirsiniz./<


İşte Zeus kişilerinizi nasıl yapılandıracağınızı ve kullanacağınızı gösteren kısa bir video:


**I - Araçlar**


Burada daha fazla araç içeren çeşitli alt bölümlerimiz var:



- hesaplar_ - burada Zeus düğüm kanallarınız için harici fon kaynağı olarak kullanmak veya kontrol etmek için harici hesapları / cüzdanları, Cold cüzdanlarını, Hot cüzdanlarını içe aktarabilirsiniz. Bu özellik hala deneyseldir.
- _İşlemi hızlandır_ - Bu özellik, Mempool'a sıkışmış bir tx'iniz olduğunda ve ücreti artırmak istediğinizde yardımcı olabilir. Tx ayrıntılarından tx çıktısını sağlamanız ve kullanmak istediğiniz yeni ücreti seçmeniz gerekecektir. Bir öncekinden daha yüksek olmalı ve Wallet zincirinizde daha fazla para bulundurmanızı gerektirmelidir.


![Image](assets/en/05.webp)


Bekleyen tx'inize gitmeli ve txid çıkış noktasını kopyalamalısınız. Ardından bu bölüme gelin ve yapıştırın, ardından çarpmak için kullanmak istediğiniz yeni ücreti seçin. O anda önerilen ücretleri içeren yeni bir ekran açılacaktır veya özel bir ücret belirleyebilirsiniz. Bir öncekinden daha yüksek olması gerektiğini unutmayın.


Zeus onchain Wallet'ünüzde maksimum 100k Sats ile bir UTXO bulundurmak, gerektiğinde ücretleri çarpmak için kullanabilmek için her zaman daha iyidir.



- _Sign or verify_ - Bu özellik ile Wallet anahtarlarınız ile belirli bir mesajı imzalayabilirsiniz. Ayrıca, belirli bir Wallet anahtarından geldiğini kanıtlamak için bir mesajı doğrulamak için de kullanılabilir.
- _Currency converter_ - BTC ve diğer fiat para birimleri arasındaki kur dönüşümünü hesaplamak için basit bir araç.


**J - Merch ve Destek**


Burada Zeus, çevrimiçi mağaza, sponsorlar, sosyal medya hakkında daha fazla bilgi ve bağlantı bulacaksınız.


**K - Yardım**


Bu son bölümde Zeus dokümantasyon sayfasına, Github sorunlarına (doğrudan uygulama geliştiricilerine bir hata veya istek göndermek istiyorsanız), e-posta desteğine bağlantılar bulacaksınız.



### ADIM 2 - ZEUS NODE KULLANMAYA BAŞLAYIN



Unutmayın, Zeus esas olarak LN üzerinden kolay ve hızlı ödemeler için bir Wallet olarak kullanılmak üzere tasarlanmıştır. Elbette, zincir üzerinde bir Wallet de içerir, ancak bu yalnızca LN kanallarını açmak / kapatmak için kullanılmalıdır, bir kahvenin düzenli ödemeleri için değil.


Lütfen [Stash'un 3 seviyesini kullanarak nasıl kendi bankanız olabileceğiniz] hakkındaki diğer rehberimi okuyun (https://darth-Coin.github.io/beginner/be-your-own-bank-en.html).


Bu anda kullanıcının Zeus'u kullanmaya başlamak için 2 yolu vardır:



- Olympus LSP'den 0-conf kanalını kullanarak doğrudan LN üzerinden
- Önce onchain Wallet'ye para yatırın ve ardından istediğiniz eş ile normal bir LN kanalı açın.


#### Yöntem A - Olympus LSP Kullanımı


Bu, yeni bir LN kullanıcısını Zeus'a dahil etmenin çok kolay ve basit bir yoludur. Bu, Bitcoin'ü olmayan tamamen yeni bir Sats kullanıcısı, bir arkadaş tarafından işe alınmış veya 1. LN ödemesine başlayan yeni bir tüccar olabilir.


Varsayılan olarak, Zeus kendi LSP'si Olympus'u kullanacaktır. Ancak daha sonra kanal açmak için bu 0-conf protokolünü destekleyen diğer LSP'lere de geçebilirsiniz.


Zeus'unuzda bir Invoice oluşturarak (miktarı girin ve "talep et" düğmesine tıklayın), bu Sats'leri hemen alabileceksiniz.


Invoice size generate [sarılmış] (https://docs.zeusln.app/lsp/wrapped-invoices) olacak ve ödenmeleri halinde hizmetle ilgili ücretler size sunulacaktır. Bu sarılmış Invoice, Zeus düğümünüze yönelik rota ipuçları içerir, böylece LSP yeni düğümünüzü bulabilir ve yatırdığınız yeni fonlarla bir kanal açabilir.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


LSP'den 1. kez almak istediğiniz fonlarla bir LN kanalı almak için, bu Invoice başka bir LN Wallet'den ödenmeli ve LSP kanalı Zeus düğümünüze doğru açana kadar birkaç dakika beklemeli, ücreti düşmeli ve ödemenin kalan miktarını kanalın sizin tarafınıza itmelidir.


Tek yapmanız gereken ZEUS'ta sizin için oluşturulan Invoice'ü başka bir yıldırım Wallet ile ödemek ve kanalınız anında açılacaktır. [Lütfen Zeus LSP ücretlerine bakın] (https://docs.zeusln.app/lsp/fees).


Bir kanal için ödeme yapmanın bir diğer avantajı da sıfır ücretli yönlendirmedir. Bu, ödemeleri yönlendirirken OLYMPUS by ZEUS üzerinden yapılan ilk atlamada yönlendirme ücreti alınmayacağı anlamına gelir. OLYMPUS by ZEUS'un ötesindeki atlamaların yine de ücretlendirileceğini unutmayın.


Kanal hazır olduğunda, Zeus kanallarını görüntüleyen ekranın altındaki sağ düğmeye tıklayın.


![Image](assets/en/08.webp)


Ve kanal dengesinin sizin tarafınızı gösteren bunun gibi bir kanal göreceksiniz:


![Image](assets/en/09.webp)


Bu kanaldan ne kadar çok harcama yaparsanız, o kadar çok gelen likiditeye sahip olursunuz. Bu kanala alacağınız daha fazla Sats için, daha az gelen likidite alanına sahip olacaksınız.


İşte LN kanallarının nasıl çalıştığına dair güzel ve basit bir görsel gösterim (Rene Pickhardt tarafından):


Şu anda, kanallar için demo ekranını göz önünde bulundurarak, kanal adına tıklayın ve bununla ilgili daha fazla ayrıntı göreceksiniz.


Olympus ile toplam 490.000 Sats kapasiteli tek bir kanalınız var, 378 bin Sats sizin tarafınızda ve 88 bin Sats Olympus tarafında. Bu da aynı kanaldan en fazla 88 bin Sats daha alabileceğiniz anlamına geliyor.


88k Sats'dan (bu durumda mevcut gelen likidite) daha fazlasını almanız gerekiyorsa, diyelim ki 500k Sats daha, sadece bu miktarla yeni bir LN Invoice oluşturarak Olympus LSP'ye yeni bir kanal talebini tetikleyecektir. Böylece 2. bir kanal elde edeceksiniz.


Bu nedenle, birden fazla kanal açmak için daha fazla ücret ödemekten kaçınmak için, ilk kez daha büyük bir kanal açmanız önerilir, örneğin 1-2M Sats. Bir kez açıldıktan sonra, bu kılavuzda açıklanan herhangi bir harici takas hizmetini kullanarak bu Sats'nin bir kısmını, diyelim ki %50'sini, zincirleme olarak takas edebilirsiniz.


Bu kanaldan diyelim ki %50 oranında çıktıktan ve Sats'ü kendi Zeus zincir üstü Wallet'ünüze geri aldıktan sonra, zincir üstü dengeden yeni bir kanal açmanın bir sonraki yöntemine geçmeye hazırsınız demektir.


#### Yöntem B - Zincir içi bakiyenizi kullanma


Bu yöntemle, aynı Olympus LSP dahil olmak üzere başka herhangi bir LN düğümüne doğru kanal açabilirsiniz. Ancak Olympus ile zaten bir kanalınız varsa, daha fazla güvenilirlik için başka bir düğümle de olması önerilir ve ayrıca MPP (çok parçalı ödeme) kullanabilir.


![Image](assets/en/10.webp)


Yukarıda MPP kullanarak bir LN Invoice ödemesine örnek verilmiştir. Ekranın altında görebileceğiniz gibi "ayarlar" var ve yapmak üzere olduğunuz ödeme için daha fazla ayrıntı içeren bir açılır sayfa açıyor. Bu ekranda, en az 2 kanalınız açıksa, MPP özelliği varsayılan olarak AÇIK olacaktır. Ayrıca AMP'yi (atomik çoklu yol) etkinleştirebilir ve istediğiniz belirli parçaları ayarlayabilirsiniz. Bu güçlü bir özelliktir!


Zeus gibi özel bir düğüm için, Sats'u LN üzerinden ödemek veya almak için tüm ihtiyaçlarınızı karşılayacak iyi LSP'lere ve iyi likiditeye sahip 2-3 iyi kanala (maks. 4-5) sahip olmanızı tavsiye ederim. [Bu kılavuzda daha fazla LN düğüm likiditesi tavsiyesine bakın](/nodes/managing-lightning-node-liquidity-en.html). Ayrıca burada Bitcoin Tasarım ekibinden başka bir [LN likiditesi hakkında genel kılavuz](https://Bitcoin.design/guide/how-it-works/liquidity/).


Doğru eşleri seçmenin deneyimli kullanıcılar için bile kolay bir iş olmadığını biliyorum. [Bu yüzden size başlangıç için bazı seçenekler sunacağım] (https://github.com/ZeusLN/zeus/discussions/2265), bunlar Zeus kullanarak kendim test ettiğim eş düğümler (uyumsuzluk sorunlarından kaçınmak için yalnızca LND düğümlerine bağlanmaya çalıştım)


Burada ayrıca Zeus için onaylanmış düğüm eşlerinin bir listesi de bulunmaktadır. Eğer iyi olanları biliyorsanız, onları bu listeye ekleyebilirsiniz.


Zeus'ta bir kanalı, ana görünümün sağ alt köşesindeki kanal simgesine tıklayarak ve ardından sağ üst köşedeki + simgesine basarak Kanallar görünümüne giderek açabilirsiniz.


![Image](assets/en/11.webp)


Belirli bir düğümle bir kanal açmak istiyorsanız, düğüm QR nodeID'sini taramak için (A) üst köşesine tıklayın (Mempool, Amboss, 1ML'de bu QR'yi elde edebilirsiniz) ve tüm eş ayrıntıları doldurulacaktır.


HATIRLATMA:


- Zeus gömülü düğüm Tor hizmetini kullanmaz! Bu yüzden lütfen Tor altında olan düğümlerle kanal açmaya çalışmayın! Kendinize daha fazla gizlilik katmaktan çok zarar veriyorsunuz. LN için Tor daha fazla gizlilik sunmaz, ancak daha fazla sorun ekler.
- eşlerinizi akıllıca seçin, iyi LSP'ler, iyi yönlendirme düğümleri olsun, kanallarınızı kapatabilecek ve iyi likidite sunamayacak rastgele pleb düğümler olmasın. [Burada likidite ve düğüm örnekleri hakkında özel bir rehber] (https://darth-Coin.github.io/nodes/managing-lightning-node-liquidity-en.html) yazdım.


Doğrudan "Olympus'a Kanal Aç" düğmesine tıklarsanız, [OLYMPUS by ZEUS] (https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581) adresine bir kanal açmak için gerekli alanları doldurursunuz.


Ücretli LSP kanallarının aksine, kanalınız zincir üzerindeki fonlarınızı kullanarak On-Chain onayı gerektirecektir (açık kanal görünümünde UTXO'larınızdan seçebilirsiniz); anında açılmayacaktır. Lütfen önce gerçek Mempool ücretlerine bakın ve bu kanalı ne kadar hızlı açmak istediğinize bağlı olarak bunları buna göre ayarlayın.


Kanalı açmak için düğmeye basmadan önce, gelişmiş seçenekleri aşağı kaydırın:


![Image](assets/en/12.webp)


Ayrıca kanalın duyurulmamış (özel) olduğundan emin olmanız gerekecektir. Varsayılan olarak bu seçenek duyurulan kanallar için kapalıdır. Bu seçeneğin Zeus gömülü düğüm için etkinleştirilmesi önerilmez, yalnızca Zeus'u uzak düğümünüzle birlikte genel bir yönlendirme düğümü olarak kullandığınızda kullanışlıdır.


Ücretli LSP kanallarının aksine, bu yöntemle kanal açarak sıfır ücretli yönlendirmeden faydalanamazsınız.


Ve bitti, sadece "Kanalı Aç" düğmesine tıklayın, tx'in madenciler tarafından onaylanmasını bekleyin. Kanal açıldıktan sonra, kanallarınızdan Sats ile istediğiniz gibi işlem yapabilirsiniz.


Bu kanalların tüm bakiyesinin SİZİN tarafınızda olacağını, dolayısıyla gelen likiditeye sahip olmayacağınızı unutmayın. Daha önce de söylediğim gibi, almak için "daha fazla yer açmak" için Sats'u LN üzerinden bir şeyler satın alarak değiştirin veya harcayın.


LN kanallarınızı bir bardak su gibi düşünün. Boş bir bardağa (kanalınıza) doldurana kadar biraz su (Sats) dökersiniz. Biraz içene (harcayana/değiştirene) kadar daha fazla su koyamazsınız. Bardak neredeyse boşaldığında, bir takas kullanarak içine daha fazla su (Sats) dökün. [Harici takas hizmetleri hakkında daha fazla bilgiyi burada bulabilirsiniz](https://darth-Coin.github.io/nodes/lightning-submarine-swaps-en.html).


Size gelen kanalları satan başka LSP hizmetleri de vardır: LNBig veya Bitrefill. Sanırım bunlar gibi daha fazla hizmet var ama şu anda hatırlayamıyorum.


Dolayısıyla, mevcut dolu kanallarınızda idare edebileceğinizden daha fazla ödeme almak için neredeyse boş bir LN kanalına ihtiyacınız varsa (bakiye başlangıçtan itibaren eş tarafta %100'dür), bu çok iyi bir seçenek olabilir. Bu kanalları açmak için belirli bir ücret ödersiniz ve bol miktarda gelen alan elde edersiniz.



## İPUÇLARI VE PÜF NOKTALARI


### Gelen rezerv limitleri


Şu anda, bazı LN kod sınırlamaları nedeniyle, "Gelen" bölümünde tam olarak ne kadar görüntülendiğini almak mümkün değildir. Faturalarınızı, sırasıyla "Kanal Yerel Rezerv" tutarından biraz daha az bir tutarla yapmanız gerektiğini daima aklınızda bulundurun.


![Image](assets/en/13.webp)


Yukarıdaki resimde görebileceğiniz gibi, "gelen" hala 5101 Sats alabileceğimi gösteriyor, ancak aslında şu anda daha fazlasını almak imkansız. Ve bunun "Yerel rezerv" ile aynı miktar olduğunu gözlemleyebilirsiniz.


Bu nedenle, alacak faturaları kestiğinizde, kanallarınızın likiditesine de bir göz atın ve alacak tutarının sınırlarını zorlamak istiyorsanız, yerel rezervi bu tutardan düşmeyi unutmayın.


### Zeus node ile başlayan yeni kullanıcılar için hızlı tavsiyeler:



- Yeni kanallarınızı doğru şekilde kullanın.


Örneğin, bir hafta içinde 1M Sats alacağınızı biliyorsanız, 2M Sats kanalı açın ve giden likiditenizin %50-60'ını onchain Wallet veya başka bir (geçici) saklama LN hesabına takas edin. Her zaman daha fazla likidite ile hazırlıklı olun. Zeus kanallarınızda daha fazla likiditeye ihtiyaç duyduğunuzda, bunu saklama hesaplarından geri taşıyabilirsiniz.


Diyelim ki haftada 500 bin Sats göndereceğinizi biliyorsanız, o zaman 1 milyon Sats kanalı açın. Bu şekilde, tekrar doldurana kadar hala bir rezerviniz olacaktır.



- Bir tüccarsanız ve her zaman düzenli olarak harcadığınızdan daha fazlasını alacaksanız, özel bir gelen kanal satın alın. En ucuz yoldur. Minimum bir ücret ödersiniz ve "boş" bir kanal elde edersiniz.



- 50-100-300-500k Sats'lik küçük anlamsız kanallar açmayın. Onları sadece zap için kullansanız bile birkaç gün içinde dolduracaksınız. Sadece bir kanal DEĞİL, daha büyük ve farklı kanallar açın.


Daha büyük bir kanal açtığınızda, Sats'yi zincir üzerindeki cüzdanlarınıza (zincir üzerindeki Zeus'a geri dönmek de dahil) taşımak için her zaman harici denizaltı takaslarını kullanabilirsiniz. Giriş ve çıkış likiditesi arasında bir denge sağlamak iyidir ve ayrıca isterseniz daha fazla kanal açmak için bu Sats'leri "yeniden kullanabilirsiniz".


### Sarılı Invoice


Aldığınızda daha fazla gizlilik eklemek istiyorsanız, "wrapped Invoice" yöntemini kullanabilirsiniz. Hatırlatma: Bunu yapabilmek için Olympus LSP ile bir kanala ihtiyacınız var. Sarılmış faturalar nihai hedefi (Zeus düğümünüzü) "gizleyecek" ve LSP düğümünüzü ödeme yapan kişiye hedef olarak gösterecektir.


Sarılmış bir Invoice elde etmek için ana tuş takımı ekranına gidin, miktarı girin ve istek tuşuna basın. Invoice'iniz için normal bir QR kodu görüntülenecektir. Şimdi, sağ üstteki "X" düğmesine tıklayın ve Invoice için daha fazla seçeneğe yönlendirileceksiniz.


![Image](assets/en/14.webp)


Şimdi üstteki "LSP'yi Etkinleştir" seçeneğini etkinleştirmeniz ve "Invoice Oluştur" düğmesine basmanız gerekecektir. Bu seçenek sarılmış Invoice'yı oluşturacak ve unutmayın, küçük bir ücret talep edecektir.


### Rota ipuçları içeren faturalar


Birden fazla gelen kanal likiditesini yönetmek istiyorsanız bu çok kullanışlı bir özelliktir. Pratik olarak Sats'i bir Invoice'den hangi gelen kanala almak istediğinizi belirtebilirsiniz.


Bu özellik, likiditeyi dolu bir kanaldan tükenmiş başka bir kanala taşımak istediğinizde dairesel yeniden dengeleme için de kullanılabilir.


Rota ipuçlarıyla bir Invoice nasıl oluşturulur?



- Ana ekranda, LN çekmecesini sağa kaydırın ve "Al" üzerine tıklayın
- Invoice kurulumunda alt kısma gidin ve "Rota ipuçlarını ekle" düğmesini etkinleştirin, ardından "Özel" sekmesini seçin. Mevcut tüm kanallarınızı içeren bir ekran açılacaktır. Almak istediğinizi seçin.
- Diğer tüm Invoice ayrıntılarını, tutarı, notu vb. doldurun ve "Invoice oluştur" seçeneğine tıklayın.
- Invoice'e ödeme yapmak Sats'ü belirtilen kanala getirecektir.


Invoice'i kendinize ödemek istiyorsanız (döngüsel yeniden dengeleme), aynı Zeus düğümünüzden ödeme yaptığınızda, ödeme ekranında, ödeme göndermek için kullanılmasını istediğiniz giden kanalı (daha fazla likiditeye sahip olanı) seçin.


### Keysend ile ödeme yapın


Keysend çok az değer verilen bir LN özelliğidir ve kullanıcılar bunu daha sık kullanmalıdır.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend), Lightning Network'daki kullanıcıların, düğümlerinin genel kanalları olduğu ve Keysend etkin olduğu sürece, doğrudan genel anahtarlarına başkalarına ödeme göndermelerine olanak tanır. Keysend, alacaklının bir Invoice yayınlamasını gerektirmez.


Peki bunu Zeus ile nasıl yapabilirsiniz?


Basitçe hedef nodeID'yi tarayın veya kopyalayın (veya normal hedef düğümlerinizi kişi olarak kaydetmek için Zeus kişilerini kullanın) ve ardından ana Zeus ekranından "Gönder" düğmesine tıklayın. Bu ekranda nodeID'yi yapıştırın veya kişilerinizden seçin.


Sats miktarını ve gerekirse bir mesaj yazın (evet, bunu LN üzerinden gizli sohbet olarak da kullanabilirsiniz) ve "Gönder" düğmesine tıklayın. Bitti!


![Image](assets/en/15.webp)


Hedef eş ile doğrudan bir kanalınız varsa, herhangi bir ücret söz konusu olmayacaktır.


Hedef eş ile doğrudan bir kanalınız yoksa, Keysend ödemesi ücretleri normal bir LN Invoice ödemesi olarak ödeyecek ve diğer herhangi bir ödeme gibi bir düzenleme yolunda yönlendirilecektir. Yalnız şunu unutmayın, LN Invoice olarak herhangi bir iz bırakmayacaktır.


## Conlusion


Daha fazla talimat ve kullanım örneği içeren [Zeus'un gelişmiş kullanımı] (https://darth-Coin.github.io/wallets/zeus-node-advanced-usage-en.html) takip kılavuzunu okumanızı tavsiye ederim.


Ve... işte bu kadar! Şu andan itibaren Zeus Node'u cep telefonunuzda normal bir BTC/LN Wallet olarak kullanabilirsiniz. Kullanıcı arayüzü oldukça basit ve kullanımı kolay, her tür kullanıcı için sezgisel, ödemelerin nasıl yapılacağı ve alınacağı hakkında daha fazla ayrıntı girmem gerektiğini sanmıyorum.


Sonuç olarak, işte bir karşılaştırmalı gizlilik tablosu:


![Image](assets/en/16.webp)