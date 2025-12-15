---
name: ArkadeOS
description: Arkade portföyü ve Ark Protokolü için eksiksiz kılavuz
---

![cover](assets/cover.webp)



Bitcoin ağı büyük bir zorlukla karşı karşıyadır: ölçeklenebilirlik. Ana katman (katman 1) rakipsiz güvenlik ve ademi merkeziyetçilik sunarken, saniyede yalnızca sınırlı sayıda işlemi gerçekleştirebilir. Lightning Network, hızlı ve düşük maliyetli ödemelere olanak tanıyan umut verici bir ikinci katman (katman 2) çözümü olarak ortaya çıkmıştır. Ancak Lightning kendi kısıtlamalarını getirmektedir: kanal yönetimi, gelen likidite ihtiyacı ve yeni kullanıcıları uzaklaştırabilecek teknik karmaşıklık.



Bu, egemenlikten ödün vermeden basitleştirilmiş bir kullanıcı deneyimi sunmak üzere tasarlanmış yeni bir katman 2 protokolü olan **Ark**'ın arka planıdır. **ArkadeOS** (veya Arkade) bu protokolün ilk büyük uygulamasıdır ve yeni nesil bir Bitcoin portföyü sunmaktadır.



Bu eğitim size Arkade dünyasında rehberlik edecek. Ark protokolünün nasıl çalıştığını, Arkade wallet'ün nasıl kurulacağını ve yapılandırılacağını ve bitcoinleri anında, gizli bir şekilde ve olağan Lightning Network sürtüşmeleri olmadan göndermek ve almak için nasıl kullanılacağını keşfedeceğiz.



## Ark protokolünün anlaşılması



Arkade'nin kullanımına geçmeden önce, onu yönlendiren Ark protokolünün temel kavramlarını kavramak önemlidir. Ark ayrı bir blok zinciri değil, Bitcoin'in üzerinde yer alan akıllı bir koordinasyon mekanizmasıdır.



### VTXO konsepti


Ark'ın merkezinde **VTXO** (Sanal UTXO) yer almaktadır. Bir VTXO, henüz Bitcoin blok zincirinde yayınlanmamış bir UTXO'dir: ana zincirin (off-chain) dışında bulunur, ancak blok zincirinde önceden imzalanmış işlemlerle desteklenir.



Merkezi bir borsadaki bakiyenin aksine, bir VTXO gerçekten size aittir. Ark sunucusu ortadan kaybolsa bile, istediğiniz zaman blok zincirinde karşılık gelen gerçek bitcoinleri talep etmenize olanak tanıyan kriptografik bir kanıta sahip olursunuz. VTXO'lar, blok onaylarını beklemeden kullanıcılar arasında anında değer aktarımı yapmanızı sağlar.



### ASP'nin (Ark Hizmet Sağlayıcısı) rolü


Ark protokolü bir istemci-sunucu modeli üzerinde çalışır. Sunucu **ASP** (Ark Hizmet Sağlayıcısı) olarak adlandırılır. ASP iletken rolünü oynar:




- Şebeke için gerekli likiditeyi sağlar.
- Kullanıcılar arasındaki işlemleri koordine eder.
- Blok zinciri üzerinde uzlaşma "turları" düzenler.



ASP'nin **gözetimsiz** olduğunu unutmamak çok önemlidir. Özel anahtarlarınızı asla elinde tutmaz ve fonlarınızı çalamaz. Rolü tamamen teknik ve lojistiktir. Bir ASP işlemlerinizi sansürlerse veya kapanırsa, tek taraflı bir çıkış prosedürü ile fonlarınızı her zaman geri alabilirsiniz.



### Turlar ve gizlilik


Ark üzerindeki işlemler **Round** adı verilen gruplar halinde sonuçlandırılır. Periyodik olarak (örneğin birkaç saniyede bir), ASP bekleyen tüm işlemleri toplar ve bunları optimize edilmiş tek bir işlemde Bitcoin blok zincirine sabitler.


Bu mekanizma iki önemli avantaj sunmaktadır:




- Ölçeklenebilirlik**: Tek bir on-chain işlemi binlerce off-chain ödemesini doğrulayabilir ve kullanıcılar için maliyetleri büyük ölçüde azaltır.
- Gizlilik**: Her tur bir **CoinJoin** olarak hareket eder. Tüm katılımcılardan gelen fonlar, yeni VTXO'lar şeklinde yeniden dağıtılmadan önce ortak bir havuzda karıştırılır. Bu, gönderen ve alıcı arasındaki bağı koparır ve dışarıdan bir gözlemcinin ödemeleri takip etmesini imkansız olmasa da son derece zorlaştırır.



## ArkadeOS sunumu



ArkadeOS, Ark protokolünü genel halkın kullanımına sunan somut bir uygulamadır. Ark Labs tarafından geliştirilen ArkadeOS, bir portföy (Wallet), bir sunucu (Operatör) ve geliştirici araçlarından oluşan eksiksiz bir ekosistemdir.



Son kullanıcı için Arkade zarif, sezgisel bir web wallet (PWA - Progressive Web App) şeklini alır. VTXO'ların ve turların kriptografik karmaşıklığını tanıdık bir arayüzün arkasına gizler. Arkade ile, klasik bir wallet gibi, ancak Ark'ın anlıklığı ve gizliliğinin gücüyle, almak için bir adresiniz, göndermek için bir düğmeniz ve bir işlem geçmişiniz var.



## Kurulum ve yapılandırma



Arkade bir Aşamalı Web Uygulaması olduğundan, kurulumu özellikle kolaydır ve geleneksel uygulama mağazalarını içermesi gerekmez.



### Erişim ve kurulum


Arkade'ye doğrudan bilgisayar veya mobil cihazdaki herhangi bir modern web tarayıcısından (Chrome, Safari, Brave) erişebilirsiniz.





- Uygulamanın resmi web sitesini ziyaret edin: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Sizi Arkade'nin temel kavramlarını tanıtan bir dizi tanıtım ekranı karşılayacak: Bitcoin için yeni bir ekosistem, kendi kendini saklamanın önemi ve toplu işlemlerin faydaları.



![arkade onboarding](assets/fr/02.webp)





- Android'de (Chrome/Brave)** : Tarayıcı menüsüne (üç nokta) basın ve "Uygulama yükle" veya "Ana ekrana ekle "yi seçin.
- IOS'ta (Safari)**: Paylaş düğmesine (yukarı oklu kare) basın ve "Ana ekranda" seçeneğini seçin.



Kurulduktan sonra Arkade, tam ekran ve adres çubuğu olmadan yerel bir uygulama gibi başlatılır.



### Portföy oluşturma


İlk açılışta portföyünüzü yapılandırmanız istenecektir.





- "Yeni Wallet Oluştur "** üzerine tıklayın.



![create wallet](assets/fr/03.webp)





- wallet anında oluşturulur. Geleneksel Bitcoin cüzdanlarının aksine, **Arkade 12 veya 24 kelimelik bir kurtarma cümlesi kullanmaz**. Bunun yerine Arkade, wallet'inizi yedeklemek ve geri yüklemek için kullanılacak Nostr (nsec) formatında otomatik olarak bir **özel anahtar** oluşturur. Bu anahtarı hemen kaydetmeyi unutmayın (sonraki bölüme bakın).





- wallet'unuzun kullanıma hazır olduğunu onaylayan "Yeni wallet'unuz yayında!" ekranını göreceksiniz. Ana arayüze erişmek için **"CÜZDANA GİT "** üzerine tıklayın.



wallet'nize girdikten sonra Arkade'nin ana arayüzüne yönlendirilirsiniz. Burada bakiyenizi, para gönderme ve alma düğmelerini ve Boltz (Lightning borsası), LendaSat ve LendaSwap (borç verme hizmetleri) ve Fuji Money (sentetik varlıklar) gibi entegre uygulamalara erişim sağlayan bir "Uygulamalar" sekmesi bulacaksınız.



![wallet interface](assets/fr/04.webp)



### ASP'ye Bağlantı


Varsayılan olarak, portföy otomatik olarak resmi Arkade Labs ASP'ye bağlanacak şekilde yapılandırılmıştır. Hangi sunucuya bağlandığınızı **Ayarlar** > **Hakkında** bölümüne giderek kontrol edebilir ve sunucu adresini (şu anda `https://arkade.computer`) görebilirsiniz.



Arkade'nin mevcut sürümünde (Beta), ASP sunucusunu manuel olarak değiştirmek mümkün değildir. Uygulama otomatik olarak resmi Arkade Labs ASP'ye bağlanır. Gelecekte, kullanıcılar tercihlerine göre farklı ASP'ler arasında seçim yapabilecekler, ancak bu özellik henüz mevcut değil.



### Özel anahtarınızı yedekleme


**Arkade, yedekleme ve kurtarma yöntemi olarak Nostr (nsec) formatında bir özel anahtar kullanır. Özel anahtarınızı yedeklemek için :





- Ana ekrandan **Ayarlar** öğesine gidin.
- "Yedekleme ve gizlilik "** öğesini seçin.
- Özel anahtarınızın** `nsec...` biçiminde görüntülendiğini göreceksiniz. Bu uzun karakter dizisi wallet'inizi geri yüklemenin tek yoludur.
- Özel anahtarınızı kopyalamak için **"COPY NSEC TO CLIPBOARD "** düğmesine basın.
- Bu anahtarı güvenli bir yerde saklayın**: kağıda yazın, güvenli bir şifre yöneticisinde saklayın veya size uygun başka bir yedekleme yöntemi kullanın.
- Arkade ayrıca **"Nostr yedeklemelerini etkinleştir "** seçeneğini de sunar. Bu özellik, wallet'nizdeki belirli verileri şifrelenmiş biçimde Nostr rölelerine otomatik olarak yedeklemek için Nostr protokolünü (merkezi olmayan bir ağ) kullanır. Bu, birden fazla cihaz arasında senkronizasyonu kolaylaştırır ve wallet'nizin durumunun daha kolay kurtarılmasını sağlar.



**Önemli**: Nostr yedeklemeleri yalnızca bir **konfor** özelliğidir. Nsec anahtarınızın yedeğinin yerini almazlar. Nostr röleleri kalıcı veri depolamayı garanti etmez. Nsec özel anahtarınız, fonlarınızı kurtarmak için tek garantili yolunuz olmaya devam etmektedir.



![backup private key](assets/fr/05.webp)




## Arkade Kullanımı



wallet'ünüzü kurduktan sonra Arkade'nin yeteneklerini keşfetmeye hazırsınız demektir. Arayüz, farklı Bitcoin ödeme türlerini (On-chain, Lightning, Ark) sorunsuz bir şekilde birleştirmek için tasarlanmıştır.



### Fonların alınması



Portföyünüze para yatırmak için **"Al "** düğmesine basın. Arkade üç makbuz yöntemi sunar:





- Ark ödemesi**: Gönderici de Arkade kullanıyorsa, anında, gizli ve neredeyse ücretsiz bir transfer için Ark adresinizi paylaşın.
- Zincirleme depozito (Biniş)**: Klasik bir wallet'dan veya bir borsadan almak için Bitcoin adresini (`bc1p...`) kullanın. Fonlar VTXO'lara dönüştürülmeden önce onay için bekleyin (~10 dakika).
- Lightning takası**: Bir Lightning faturası oluşturun ve harici bir wallet Lightning'den ödeyin. Fonlar otomatik bir takas yoluyla anında ulaşır.



![receive amount](assets/fr/06.webp)



Makbuz ekranında mevcut tüm seçenekler görüntülenir: QR kodu, Ark adresi, Bitcoin (BIP21) adresi ve Lightning faturası. Lightning ödemeleri için, işlem sırasında uygulamayı açık tutun.



![receive confirmation](assets/fr/07.webp)



### Fon gönderme



Para göndermek için **"Gönder "** düğmesine basın ve alıcının adresini yapıştırın veya QR kodunu tarayın. Arkade gerekli ödeme türünü otomatik olarak algılar:





- Ark** ödemesi: Bir Ark adresine transfer anında, özel ve neredeyse ücretsizdir (0 SATS ücreti). Alıcının çevrimiçi olması gerekmez.
- Lightning** ödemesi: Bir Lightning faturasını (`lnbc...`) tarayın ve Arkade otomatik olarak bir takas gerçekleştirsin. ASP faturayı sizin için öder ve Arkade bakiyenizi borçlandırır.
- Zincirleme ödeme**: Klasik bir Bitcoin adresine (`bc1q...` veya `bc1p...`) yönelik olarak Arkade, bir sonraki on-chain turuna dahil edilecek bir "İşbirlikçi Çıktı" başlatır.



"İşlemi imzala" ekranındaki ayrıntıları kontrol edin, ardından **"İMZALAMAK İÇİN DOKUN "** ile onaylayın.



![send payment](assets/fr/08.webp)



**Mevcut sınırlama (Beta)**: on-chain çıkışları için 24 saatten daha kısa bir süre önce oluşturulan VTXO'lar kullanılamaz. Bir hatayla karşılaşırsanız, lütfen VTXO'larınız "olgunlaşana" kadar bekleyin.



**on-chain çıktı gizliliği**: Aşağıdaki örnek bir [mempool.space üzerinde Ark çıktı işlemini] (https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb) göstermektedir. CoinJoin gibi 4 farklı çıktıya dağıtılmış bir girdi gözlemliyoruz. Harici bir gözlemci için hangi miktarın hangi kullanıcıya ait olduğunu belirlemek imkansızdır.



![transaction ark mempool](assets/fr/11.webp)



## Gelişmiş özellikler



### VTXO sona erme yönetimi


Ark protokolünün teknik bir özelliği de VTXO'ların **sınırlı bir ömre** sahip olmasıdır. Bu zaman kısıtlaması protokolün tasarımının doğasında vardır. Sona erme süresi her ASP sunucusu tarafından yapılandırılabilir; resmi Arkade Labs ASP'de bu süre **4 hafta (≈30 gün)** civarındadır.



**Bu sınırlama, Ark sunucusunun likiditeyi verimli bir şekilde yönetmesini ve aktif olmayan kullanıcılardan VTXO'ları temizlemesini sağlar. Süre dolduktan sonra Ark sunucusu teknik olarak VTXO ağacında kalan fonları talep edebilir.



**VTXO'larınızı aktif tutmak için, süreleri dolmadan önce "yenilenmeleri" gerekir. Yenileme, süresi dolmak üzere olan VTXO'larınızın yeni bir tam geçerlilik süresine sahip (Arkade Labs ASP'de ≈30 gün) yeni VTXO'larla değiştirildiği yeni bir "tura" katılmaktan oluşur.



Arkade portföyü bu süreci otomatik olarak yönetir: uygulama VTXO'larınızın durumunu sürekli olarak izler ve süreleri dolmadan birkaç gün önce otomatik olarak yeniler. Uygulamanızı düzenli olarak açtığınız sürece (haftada en az bir kez), VTXO'larınız otomatik olarak aktif tutulacaktır.



**Portföyünüzü 4 haftadan daha uzun süre açmazsanız, VTXO'larınızın süresi dolar. Ancak, fonlarınızı kaybetmezsiniz: **tek taraflı çıkış** yoluyla fonlarınızı geri alma seçeneğiniz vardır (bir sonraki bölüme bakın). Bu prosedür daha maliyetli ve daha yavaştır, ancak fonlarınızın geri kazanılabilir kalmasını sağlar.



Uygulamayı düzenli olarak açma ihtiyacı, Arkade'yi uzun vadeli tasarruflar için bir kasa değil, günlük harcamalar için tasarlanmış bir **"Hot Wallet"** yapar. Bitcoinleri uzun süre kullanmadan saklamak için soğuk bir wallet donanımı tercih edin.



**VTXO'larınızın durumunu kontrol edin**: VTXO'larınızın durumunu **Ayarlar** > **Gelişmiş** bölümünden izleyebilirsiniz. Bir sonraki otomatik yenilemenin ne zaman yapılacağını görmek için "Sonraki Yenileme" ve tüm VTXO'larınızın son kullanma tarihleriyle birlikte ayrıntılı bir listesini görmek için "Sanal Paralar" bölümüne bakın.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Tek Taraflı Çıkış)



Tek taraflı çıkış, Ark protokolünün **temel bir kriptografik garantisidir** ve ASP ortadan kaybolsa, işlemlerinizi sansürlese veya işbirliği yapmayı reddetse bile paranızı geri almanızı sağlar. Teknik olarak, VTXO'larınız size ait **önceden imzalanmış Bitcoin işlemleridir**. Mutlak bir acil durumda, bu işlemleri Bitcoin blok zincirinde yayınlayarak kimsenin izni olmadan fonlarınızı geri alabilirsiniz.



**Nasıl çalışır? Süreç iki aşamada gerçekleşir. İlk olarak, **Unrolling**: işlem ağacında VTXO'larınızı oluşturan önceden imzalanmış işlemleri sırayla yayınlarsınız. Sonra **Sonlandırma**: zaman kilitlerinin süresi dolduğunda (genellikle 24 saat), bitcoinlerinizi standart bir adresten toplarsınız.



**Arkade'deki mevcut durum**: Beta sürümünde, tek taraflı çıktı için henüz bir düğme veya basit bir kullanıcı arayüzü yoktur. Bu işlevsellik şu anda Arkade SDK kullanımını ve TypeScript programlama teknik bilgisini gerektirmektedir.



**Prosedür bir düğmeye dokunarak erişilebilir olmasa bile, kriptografik garanti oradadır. VTXO'larınız yasal olarak size ait olan önceden imzalanmış işlemler içerir. Ark'ı **gözetimsiz** bir protokol haline getiren bu teknik garantidir: en kötü senaryoda bile, fonlarınız teknik olarak kurtarılabilir durumda kalır. Arkade'nin gelecek sürümlerinde muhtemelen basitleştirilmiş bir arayüz eklenecektir.



## Avantajlar ve sınırlamalar



Arkade'yi doğru bağlama oturtmak için mevcut güçlü ve zayıf yönlerini özetleyelim.



### Önemli Noktalar




- Kullanıcı Deneyimi (UX)**: Lightning'de olduğu gibi kanal yönetimi, gelen kapasite veya karmaşık kanal yedeklemeleri yok. Sadece kurun ve kullanın.
- Gizlilik** : Varsayılan CoinJoin mimarisi, standart on-chain veya Lightning işlemlerinden çok daha yüksek düzeyde anonimlik sunar.
- Birlikte Çalışabilirlik**: Herhangi bir Bitcoin QR kodunu (On-chain veya Lightning) tek bir arayüzden ödeyin.



### Kısıtlamalar




- Genç protokol**: Ark çok yeni bir teknolojidir. Hatalar mevcut olabilir. Ark'ın kaybı kritik olabilecek toplamları saklamak için kullanılmaması tavsiye edilir.
- ASP bağımlılığı**: Gözetim altında olmamasına rağmen, sistem akışkanlık için ASP kullanılabilirliğine dayanır. ASP çevrimdışıysa, artık anında işlem yapamazsınız (yalnızca on-chain fonlarınızı çıkarabilirsiniz).
- Yalnızca Hot Wallet** : VTXO'ları yenilemek için uygulamayı düzenli olarak açma ihtiyacı soğuk depolama (Cold Depolama) için uygun değildir.



## Karşılaştırma: Arkade vs Lightning vs Cashu



Arkade'nin konumunu daha iyi anlamak için onu diğer iki büyük ölçeklenebilirlik çözümüyle karşılaştıralım.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** ideal bir uzlaşmadır: Cashu'nun basitliği ve gizliliği, ancak Lightning'in egemenliği (gözetim dışı).



## Destek ve Yardım



Arkade'yi kullanırken herhangi bir sorunla karşılaşırsanız veya herhangi bir sorunuz olursa, uygulama çeşitli destek seçenekleri sunar:





- Ayarlar** > **Destek** bölümüne gidin.
- Birkaç seçenek bulacaksınız:
  - Müşteri desteği**: Portföyünüzle ilgili yardım alın, hataları bildirin veya soru sorun.
  - Güvenli Sohbet**: Görüşmeleriniz güvenli ve özeldir, oturumlar arasında geçmiş korunur.
  - Hata Raporları**: Karşılaştığınız sorunları, bunları yeniden üretme adımları da dahil olmak üzere bildirin.
  - İlerlemeyi Takip Edin**: Destek biletlerinizi ve görüşmelerinizi her zaman takip edin.



![support](assets/fr/10.webp)



Arkade ekibi, destek ve entegrasyon fırsatları için @arkade_os kanalı aracılığıyla Telegram'da da aktif.



## Önemli not: Uygulama Beta aşamasında



**⚠️ Arkade şu anda mainnet Bitcoin** üzerinde Genel Beta aşamasındadır. Uygulama gerçek bitcoinlerle işlevsel olsa da, bazı önlemlerin alınması önemlidir.



### Kullanım için öneriler




- Küçük miktarlar kullanın**: Arkade'de büyük meblağlar saklamaktan kaçının. Bu wallet'yi günlük harcamalarınız için kullanın ve birikimlerinizi soğuk bir wallet donanımında tutun.
- Olası hatalar ve sınırlamalar**: Aktif olarak geliştirilmekte olan her uygulamada olduğu gibi Arkade de hatalar veya beklenmedik davranışlar gösterebilir. Her türlü sorunu entegre destek aracılığıyla bildirin.
- Hızlı evrim** : Uygulama ve protokol sürekli olarak geliştirilmektedir. Gelecek sürümlerde bazı özellikler değişebilir veya eklenebilir.



### Bilinen mevcut sınırlamalar




- vTXO'larda 24 saatlik gecikme** : Yeni oluşturulan VTXO'lar on-chain çıkışları için hemen kullanılamaz.
- ASP benzersiz**: Uygulamada ASP sunucusunu değiştirmek henüz mümkün değildir.
- Teknik tek taraflı çıktı**: Tek taraflı çıkış için henüz basitleştirilmiş bir arayüz yok (SDK gerektirir).



Arkade Labs ekibi, gelecek sürümlerde bu sınırlamaları gevşetmek için aktif olarak çalışıyor.



## Sonuç



ArkadeOS, Bitcoin ekosisteminde büyük bir atılımı temsil etmektedir. Ark protokolünü uygulayarak, kullanım kolaylığını Bitcoin'un temel ilkeleriyle uzlaştırmanın mümkün olduğunu kanıtlıyor: güvenme, doğrula.



Henüz emekleme aşamasında olmasına rağmen Arkade, Bitcoin ödemelerinin geleceğinin nasıl görünebileceğine dair büyüleyici bir bakış sunuyor: anında, özel ve teknik önkoşul olmaksızın herkes tarafından erişilebilir. Güvenli tasarruf çözümünüzü (Cold Wallet) tamamlayan, günlük harcamalarınız için mükemmel bir araçtır.



Bu yeni protokolü kendiniz keşfetmek için Arkade'yi küçük miktarlarla test etmenizi öneririz. Ekosistem hızla gelişiyor ve Arkade bu yeniliğin ön saflarında yer alıyor.



## Kaynaklar



Daha fazla bilgi edinmek için resmi kaynaklara başvurun:





- Arkade** web sitesi: [arkadeos.com](https://arkadeos.com)
- Dokümantasyon**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark** protokolü: [ark-protocol.org](https://ark-protocol.org)
- Kaynak Kodu** : [GitHub Arkade](https://github.com/arkade-os)