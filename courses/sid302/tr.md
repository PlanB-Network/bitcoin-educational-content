---
name: Liquid Bootcamp Essentials
goal: Liquid Network ve Elements projesi hakkında kapsamlı bir anlayış kazanın ve gizli işlemler, tokenizasyon ve merkezi olmayan ağ mimarisinde gelişmiş çözümlerin nasıl uygulanacağını öğrenin.
objectives: 

  - Liquid mimarisinin temellerini ve Bitcoin ile ilişkisini anlamak.
  - Elements yazılımını kullanarak Liquid düğümlerini yapılandırmayı ve çalıştırmayı öğrenin.
  - Liquid Network'de gizli işlemlerin ve varlık ihracının kullanımını araştırın.
  - Sermaye piyasalarındaki uygulamalar için Liquid'in iş ve teknik yönlerini kavramak.

---

# Liquid ağına giriş


Liquid Network ve Elements projesinin derinlemesine anlaşılmasını sağlamak için tasarlanmış bir eğitim yolculuğuna çıkın. Bu bootcamp, Liquid'ün yeteneklerini uygulamak ve bunlardan yararlanmak için gerekli teknik, mimari ve iş temellerini öğretmek için teori ve pratiği birleştirir. Gizli işlemlerden ekosistem tasarımına kadar, bu kurs Bitcoin ekosistemindeki gelişmiş araçlar hakkındaki bilgilerini genişletmek isteyenler için idealdir.


Sektör uzmanlarının sunumlarının yer aldığı eğitimde Liquid mimarisi, tokenizasyon uygulamaları, Elements'ün teknik kavramları ve Breez SDK gibi yenilikçi kullanım alanları gibi konular ele alınmaktadır. Yeni başlayanlar ve orta düzey kullanıcılar için erişilebilir olacak şekilde tasarlanan kurs, projelerini optimize etmek için bir platform olarak Liquid'te ustalaşmak isteyen deneyimli geliştiricilere de değer sunuyor.

+++

# Giriş


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Kursa genel bakış


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Liquid Network ve Elements projesinden etkin bir şekilde yararlanmanızı sağlayacak bilgi ve becerilerle donatmak üzere tasarlanmış kapsamlı bir eğitim olan Liquid Bootcamp'e hoş geldiniz. Bu eğitim, Liquid'nin Confidential Transactions, varlık ihracı ve federe ağ mimarisi gibi ayırt edici özelliklerinin kapsamlı bir incelemesini sunarken, aynı zamanda Liquid'ye güç veren yazılım olan Elements'un temel kavramlarını da tanıtmaktadır.


Eğitim kampı boyunca, Liquid Network'in pratik uygulamalarını, düğümlerin kurulmasından ve çalıştırılmasından Bitcoin'nin sermaye piyasalarında ve tokenizasyonunda kullanımını anlamaya kadar keşfedeceksiniz. Sektör uzmanlarının sunumlarıyla HTLC'ler, Breez SDK ve Blockstream AMP projesi gibi gelişmiş konular hakkında da bilgi edineceksiniz.


Bu bootcamp başlangıçta canlı oturumlar için tasarlanmış yapılandırılmış bir programı (resimde gösterildiği gibi) takip eden yüz yüze bir etkinlik olarak yürütülmüştür. Ancak, bu kurs uyarlaması için içerik, çevrimiçi bir formata daha iyi uyacak ve öğrencilerin anlamasını kolaylaştıracak şekilde yeniden düzenlenmiştir. Yeni düzen, temel kavramlardan daha ileri ve teknik konulara doğru mantıklı bir ilerleme sağlayarak öğrenme deneyimini en üst düzeye çıkarmaktadır.


Bu yolculuk, teorik bilgi ve uygulamalı deneyimin bir karışımını sunarak, farklı uzmanlık seviyelerine sahip katılımcıları barındıracak şekilde yapılandırılmıştır. Bu eğitim kampının sonunda, Liquid'in mimarisi, Bitcoin ile entegrasyonu ve finansal çözümler oluşturmak ve optimize etmek için yenilikçi özelliklerinden nasıl yararlanılacağı hakkında sağlam bir anlayışa sahip olacaksınız.


Liquid yan zincir dünyasına dalın ve tam potansiyelini hemen şimdi ortaya çıkarın!

# Temel Bilgiler


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Liquid Mimarisi


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Mimarisi ve Mutabakat Modeli


Liquid Network, Elements kod tabanı üzerine inşa edilmiş, temel güvenliğine güvenirken Bitcoin'nin yeteneklerini genişletmek için tasarlanmış bir federe yan zincirdir. Bitcoin'nin [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work)'undan farklı olarak, Liquid bir Federe [Mutabakat](https://planb.academy/resources/glossary/consensus) modeli üzerinde çalışır. Ağ, borsalar, ticaret masaları ve altyapı sağlayıcıları da dahil olmak üzere küresel olarak dağıtılmış bir grup üye tarafından sürdürülmektedir. Bu üyelikten, blok imzalayıcı olarak hareket etmek üzere on beş "görevli" seçilir.


Bu görevliler [blokları](https://planb.academy/resources/glossary/block) her dakika yeni bir blok üreterek deterministik bir round-robin tarzında üretirler. Bu hassas zamanlama Bitcoin'ün olasılıksal on dakikalık aralıklarına tezat oluşturmaktadır. Bir bloğun geçerli olabilmesi için 15 görevliden en az 11'inin imzası gerekmektedir (üçte iki artı bir eşiği). Bu mekanizma Liquid'e "iki blok kesinliği" sağlar, yani bir [işlem](https://planb.academy/resources/glossary/transaction-tx) iki onay aldıktan sonra (yaklaşık iki dakika), zinciri yeniden düzenlemek matematiksel olarak imkansızdır. Bu hız ve kesinlik arbitraj, otomatik ticaret ve borsalar arası hızlı mutabakat için kritik öneme sahiptir.


Federasyon dinamiktir. Dinamik Federasyon (Dynafed) protokolü sayesinde ağ, sabit bir [fork](https://planb.academy/resources/glossary/fork) gerektirmeden görevlileri değiştirebilir veya parametreleri güncelleyebilir. Bu, sistemin sürekli çalışmayı sürdürürken sorunsuz bir şekilde gelişmesine ve donanım veya üyeleri değiştirmesine olanak tanır.


### Confidential Transactions ve Varlık Yönetimi


Liquid'ın belirleyici bir özelliği, Confidential Transactions (CT) ve çoklu varlıklar için yerel desteğidir. Ana Bitcoin zincirinde tüm işlem detayları (gönderen, alıcı ve miktar) herkese açıktır. Liquid'ta CT, varlık türünü ve tutarını halka açık defterden gizlemek için kriptografik taahhütler kullanırken, ağın işlemin geçerli olduğunu (yani [şişirme](https://planb.academy/resources/glossary/inflation) olmadığını) doğrulamasına izin verir. Yalnızca körleme anahtarlarına sahip katılımcılar belirli değerleri görüntüleyebilir ve bu da büyük pozisyonları taşıyan kurumlar için gerekli olan ticari gizlilik seviyesini sunar.


Liquid, tüm varlıkları [blok zincirinin](https://planb.academy/resources/glossary/blockchain) "yerel" vatandaşları olarak ele alır. Buna Liquid Bitcoin (LBTC), USDT gibi sabit coinler ve güvenlik tokenları dahildir. Bir varlığın çıkarılması karmaşık akıllı sözleşmeler gerektirmez; bu protokolün temel bir işlevidir.


#### Düzenlenmiş Varlıklar ve AMP

Liquid, güvenlik tokenleri gibi uyumluluk gerektiren varlıklar için Blockstream Varlık Yönetim Platformunu (AMP) kullanır. Bu, işlemlerin bir yetkilendirme sunucusundan ikinci bir imza gerektirdiği izinli bir katman sunar. Bu, ihraççıların beyaz liste veya KYC gereksinimleri gibi kuralları ayrıntılı bir düzeyde uygulamasına olanak tanıyarak blok zincirinin verimliliğini geleneksel finansın düzenleyici kontrolleriyle birleştirir.


### Çift Yönlü Peg ve Güvenlik Altyapısı


Liquid ve Bitcoin arasındaki bağlantı iki yönlü bir peg aracılığıyla sağlanır. Bir kullanıcı "peg-in" yapmak için Bitcoin'i mainchain üzerinde oluşturulan bir adrese gönderir. Bu fonlar, yeniden yapılanma risklerini ortadan kaldırmak için 102 onay (yaklaşık 17 saat) boyunca kilitlenir. Onaylandıktan sonra, Liquid yan zincirinde eşdeğer miktarda LBTC basılır.


"Peg-out" süreci, kullanıcıların LBTC'yi Bitcoin karşılığında kullanmalarını sağlar. Bunun için LBTC'nin yakılması ve federasyondan kriptografik bir yetki alınması gerekir. Hırsızlığı önlemek için, peg-out'lar federasyon üyeleri tarafından tutulan Peg-out Yetki Anahtarları (PAK'lar) tarafından sıkı bir şekilde kontrol edilmektedir. Ayrıca, fonlar SideSwap gibi üçüncü taraf sağlayıcılar aracılığıyla anında takas edilebilir ve daha hızlı likidite için uzlaştırma gecikmesi atlanabilir.


#### Donanım Güvenlik Modülleri (HSM'ler)

Güvenlik kesinlikle donanım aracılığıyla sağlanır. Görevliler [özel anahtarları](https://planb.academy/resources/glossary/private-key) standart sunucularda tutmazlar; bunun yerine Donanım Güvenlik Modüllerini (HSM'ler) çalıştırırlar. Bu cihazlar ana sunucunun mantığından hava boşlukludur ve katı kurallarla programlanmıştır. Örneğin, bir HSM, yüksekliği bir öncekinden büyük olmayan bir bloğu imzalamayı reddederek geçmişin yeniden yazılmasını önler. Bu "düşmanca" güvenlik modeli ana sunucunun tehlikeye atılabileceğini varsayar ve fiziksel konum ihlal edilse bile anahtarların güvende kalmasını sağlar.


## Elements'in Temelleri


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Liquid'nin Kuruluşu


Elements, Bitcoin Core kod tabanından türetilmiş açık kaynaklı bir blok zinciri platformudur. Varlıkları Bitcoin'e ve Bitcoin'ten aktarabilen yan zincirlerden bağımsız blok zincirleri sağlayarak Bitcoin'ün işlevselliğini genişletir. Bitcoin Core, Bitcoin ağına güç sağlarken, Elements, Liquid Network ve diğer özel yan zincirlerin arkasındaki yazılım motorudur.


İlişki basittir: Liquid, federe mutabakat modeli ile üretim kullanımı için yapılandırılmış bir Elements yan zincirinin belirli bir "örneğidir". Bitcoin'ye aşina olan geliştiriciler, aynı RPC (Remote Procedure Call) arayüzünü ve komut satırı yapısını (`elements-cli`, `elements-d`, `elements-qt`) koruduğu için Elements'i sezgisel bulacaktır. Temel fark yapılandırmada yatmaktadır: `chain=liquidv1` ayarı bir düğümü ana Liquid ağına bağlarken, `chain=elementsregtest` geliştiricilerin generate bloklarını anında ve dış bağımlılıklar olmadan test edebilecekleri yerel bir regresyon testi ortamı oluşturur.


#### Varlık İhracı

Elements'in öne çıkan bir özelliği de yerel varlık ihracıdır. Tokenların karmaşık akıllı sözleşmeler olduğu Ethereum'un aksine, Elements'deki varlıklar basit bir RPC komutuyla (`issueasset`) oluşturulan birinci sınıf vatandaşlardır.


- Benzersiz Tanımlayıcılar:** Her varlık 64 karakterlik benzersiz bir onaltılık kimlik alır.
- Yeniden İhraç Tokenları:** İhraççılar isteğe bağlı olarak, sahibine daha sonra varlıktan daha fazla basma hakkı veren yeniden ihraç tokenları oluşturabilir (sabit coinler veya güvenlik tokenları için kullanışlıdır).
- Varlık Kayıt Defteri:** Hex ID'ler insan tarafından okunabilir olmadığından, Blockstream Varlık Kayıt Defteri bu ID'leri varlıklar için bir DNS'ye benzer şekilde adlara ve ticker'lara (örneğin, "USDT") eşler.


### Confidential Transactions aracılığıyla Gizlilik


Elements, halka açık blok zincirlerinin temel sınırlamalarından biri olan ticari gizlilik eksikliğini gidermektedir. Bitcoin'da her işlem tutarı tüm dünya tarafından görülebilir. Elements, ağın işlemin geçerliliğini doğrulamasına izin verirken miktarı ve varlık türünü kriptografik olarak gizleyen **Confidential Transactions (CT)**'yi sunar.


Bu, **Pedersen Commitments** ve **Range Proofs** kullanılarak gerçekleştirilir.


- Pedersen Taahhütleri** görünür miktarı kriptografik bir taahhütle değiştirir. Homomorfik şifreleme sayesinde doğrulayıcılar gerçek değerleri görmeden *Girdi Taahhütleri = Çıktı Taahhütleri + Ücretler* olup olmadığını kontrol edebilir.
- Aralık Kanıtları**, gizli değerin geçerli bir aralıkta pozitif bir tamsayı olduğunu matematiksel olarak kanıtlayarak bir kullanıcının yoktan para yaratmasını (örneğin, negatif sayılar kullanarak) önler.


Dışarıdan bir gözlemci için Gizli İşlem geçerli giriş ve çıkışları gösterir ancak *ne* gönderildiğini ve *ne kadar* gönderildiğini gizler. Yalnızca gönderici ve alıcı (kör edici anahtarlara sahip olan) açık metin verilerini görüntüleyebilir.


### Geliştirme ve RPC İş Akışı


Bir Elements düğümü ile etkileşim öncelikle JSON-RPC arayüzü aracılığıyla yapılır. Bu, Python, JavaScript veya Go ile yazılmış uygulamaların blok zinciri ile iletişim kurmasına olanak tanır.



- Kurulum:** Bir geliştirici genellikle `regtest` modunda başlar. Bu, canlı ağın 1 dakikalık blok süresini atlayarak işlemleri hemen onaylamak için blokların anında oluşturulmasına (`generateblock`) olanak tanır.
- Komutlar:** `getblockchaininfo` gibi standart Bitcoin komutlarının yanı sıra `dumpblindingkey` (CT'leri denetlemek için) veya `pegin` (BTC'yi yan zincire taşımak için) gibi Elements'e özgü komutlar da mevcuttur.
- Takma adlar:** Birden fazla düğümü yönetmek için (örneğin, test için bir "gönderici" ve "alıcı"), geliştiriciler genellikle tek bir makinede eşler arası bir ağı simüle ederek farklı veri dizinlerine işaret eden `e1-cli` ve `e2-cli` gibi kabuk takma adları kullanırlar.


Bu mimari, geliştiricilerin Bitcoin ekosisteminin sağlam ve tanıdık araçlarını kullanarak menkul kıymet platformları veya özel ödeme ağ geçitleri gibi sofistike finansal uygulamalar oluşturmalarını sağlar.


## Bitcoin Katmanlarının Bağlanması


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer Altyapısı ve HTLC'ler


Bitcoin ekosistemi çok katmanlı bir mimariye dönüşmüştür; Ana Zincir mutabakat sağlar, Lightning hız sunar ve Liquid gelişmiş varlık yetenekleri sağlar. Merkezi aracılar olmadan bu katmanlar arasında değer taşımak, güvenilir olmayan bir kriptografik ilkel gerektirir: [Hash](https://planb.academy/resources/glossary/hash-function) Zaman Kilitli Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Bir HTLC, bağımsız sistemleri atomik olarak birbirine bağlayan koşullu bir [ödeme kanalı](https://planb.academy/resources/glossary/payment-channel) oluşturur. İki temel kısıtlama aracılığıyla çalışır: bir **hash kilidi** ve bir **zaman kilidi**.


- Hash Kilidi:** Alıcı, belirli bir kriptografik hash ile eşleşen gizli bir "ön görüntü" ortaya çıkarırsa fonlar hemen harcanabilir.
- Zaman Kilidi:** Alıcı belirli bir zaman dilimi (blok yüksekliği) içinde sırrı açıklayamazsa, orijinal gönderici fonları geri alabilir.


Bu çift yollu yapı güvenliği sağlar. Çapraz katmanlı bir takasta, her iki ağda da aynı hash kilidi kullanılır. Alıcı bir katmanda (örneğin Liquid) fon talep etmek için sırrı açıkladığında, bu sır gönderen tarafından görülebilir hale gelir ve daha sonra diğer katmanda (örneğin Lightning) karşılıklı fon talep etmek için kullanabilir. Bu kriptografik bağlama, takasın her iki taraf için de başarılı bir şekilde tamamlanmasını ya da her ikisi için de başarısız olmasını garanti ederek bir tarafın fon kaybederken diğerinin fon kazanması riskini ortadan kaldırır.


### Taproot ve MuSig2 Yükseltmesi


Eski HTLC'ler (SegWit v0) iyi çalışıyordu ancak gizlilik ve verimlilik dezavantajlarından muzdaripti. Tüm senaryo mantığı on-chain'ün yayınlanmasını gerektiriyordu, bu da takas işlemlerini blok zinciri analistleri için kolayca tanımlanabilir ve veri boyutları nedeniyle daha pahalı hale getiriyordu. Taproot (SegWit v1) ve MuSig2 protokolünün kullanıma sunulması bu mimaride devrim yaratmıştır.


Taproot, MuSig2 aracılığıyla **Anahtar Birleştirmeye** izin verir. MuSig2, birden fazla açık anahtara sahip karmaşık bir senaryoyu ortaya çıkarmak yerine, takas katılımcılarının anahtarlarını tek bir birleştirilmiş açık anahtarda birleştirmelerini sağlar.


- İşbirlikçi "Anahtar Yol":** Her iki taraf da takası kabul ederse ("mutlu yol"), işlemi birlikte imzalarlar. Ağ için bu, standart, tek imzalı bir ödeme ile aynı görünür. Minimum blok alanı tüketir ve takas koşulları hakkında kesinlikle hiçbir bilgi vermez.
- Muhalif "Senaryo Yolu":** Taraflardan biri yanıt vermez veya kötü niyetli olursa, temel senaryo (karma/zaman kilitlerini içeren) ancak o zaman ortaya çıkar. Bu bir Merkle ağacında düzenlenir ve dürüst tarafın yalnızca fonları kurtarmak için gereken belirli dalı ifşa etmesine izin vererek sözleşme mantığının geri kalanını gizli tutar.


### Pratik Uygulama: Liquid-Yıldırım Takasları


Uygulamada, bu protokoller Bitcoin'un katmanları arasında sorunsuz değişim sağlar. Tipik bir Liquid-Lightning takası, bir müşterinin bir hizmet sağlayıcıdan takas talep etmesiyle başlar. Müşteri bir Lightning faturası sağlar ve sağlayıcı eşdeğer Liquid Bitcoin'u (L-BTC) Taproot özellikli bir HTLC adresine kilitler.


Atomiklik, ödeme gerçekleştiğinde uygulanır. L-BTC'yi talep etmek için hizmet sağlayıcının ön görüntüye sahip olması gerekir. Bu ön görüntüyü yalnızca müşterinin Lightning faturasını başarıyla ödediklerinde alırlar. Lightning ödemesi tamamlandığı anda, ön imaj ortaya çıkar ve sağlayıcının Liquid fonlarının kilidini açmasına izin verir.


#### Wallet Soyutlama ve UTXO Yönetimi

Son kullanıcılar için bu karmaşıklık tamamen soyutlanmıştır. Aqua gibi modern cüzdanlar anahtar oluşturma, fatura oluşturma ve imzalama işlemlerini arka planda gerçekleştirir. Kullanıcı sadece Liquid bakiyesini kullanarak bir Lightning faturasını "öder". Perde arkasında hizmet, wallet verimliliğini korumak ve yoğun trafik dönemlerinde ücret etkilerini en aza indirmek için küçük, talep edilmeyen veya iade edilen çıktıları periyodik olarak süpürerek UTXO konsolidasyonunu yönetir.


## Liquid Network Genel Bakış


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Mimari ve Konsensüs


Liquid Network, **Elements** kod tabanı üzerine inşa edilmiş federe bir yan zincir olarak çalışır. Bitcoin Çekirdeğinin bir fork'i olan Elements yazılım temelini sağlarken, Liquid üretim ağı uygulamasıdır. Bitcoin'in rekabetçi [mining](https://planb.academy/resources/glossary/mining)'ye dayanan Proof-of-Work'ünden farklı olarak, Liquid bir **Federasyon Konsensüsü** modeli kullanır.


Ağ, küresel olarak dağıtılmış on beş "görevli" tarafından sürdürülmektedir Bu kuruluşlar iki kritik rolü yerine getiren özel sunucular işletmektedir:

1.  **Blok Üretimi:** Görevliler blokları deterministik bir round-robin programında sırayla oluşturur ve tam olarak her dakika yeni bir blok üretir.

2.  **Blok İmzalama:** Bir bloğun geçerli olabilmesi için 15 görevliden en az 11'i tarafından imzalanmış olması gerekir.


Bu 15'te 11 eşiği, ağın durmadan dört düğüme kadar arızayı tolere edebilmesini sağlar. Bu değiş tokuşun birincil avantajı **deterministik kesinliktir**. Bitcoin olasılıklarla ilgilenirken, Liquid iki bloktan sonra (yaklaşık iki dakika) uzlaşma kesinliğine ulaşır. Bir bloğun üzerinde tek bir onay olduğunda, zincir yeniden düzenlenemez, bu da onu arbitraj ve hızlı uzlaşma için oldukça etkili hale getirir.


### Confidential Transactions ve Yerel Varlıklar


Liquid'in tanımlayıcı özelliği **Confidential Transactions (CT)**'nin varsayılan kullanımıdır. Bitcoin mainchain'te gönderici, alıcı ve miktar herkese açıktır. Liquid bunu, miktarı ve varlık türünü kriptografik olarak körleştirirken, gönderen ve alıcı adreslerini doğrulama için görünür bırakarak geliştirir.


Bir kullanıcının para basamayacağından emin olmak için (örneğin, negatif miktarlar göndererek), Liquid **Pedersen Commitments** ve **Range Proofs** kullanır. Bu kriptografik ilkeller, ağın *Girdi = Çıktı + Ücret* ve tüm değerlerin pozitif tam sayılar olduğunu, belirli sayıları genel deftere açıklamadan doğrulamasına olanak tanır. Sadece kör edici anahtarlara sahip katılımcılar şifresi çözülmüş verileri görüntüleyebilir.


#### Varlık İhracı

Liquid tüm varlıkları "yerel" olarak ele alır İster Liquid Bitcoin (L-BTC), ister USDT gibi bir stabilcoin ya da bir menkul kıymet token olsun, hepsi aynı mimariyi paylaşır. Bir varlığın çıkarılması için akıllı sözleşmeler gerekmez, yalnızca basit bir RPC çağrısı yeterlidir.


- Düzenlenmemiş Varlıklar:** Herkes tarafından izinsiz olarak ihraç edilebilir.
- Düzenlenmiş Varlıklar:** Blockstream Varlık Yönetimi Platformunu (AMP) kullanan ihraççılar, bir varlığın taşınabilmesi için bir yetkilendirme sunucusundan ikinci bir imza gerektirerek uyumluluk kurallarını (KYC/AML gibi) uygulayabilir.


### İki Yönlü Peg ve Dinamik Federasyon


Bitcoin ve Liquid arasındaki köprü **İki Yönlü Peg**'dir. Kullanıcıların BTC'yi yan zincire (Peg-in) ve mainchain'e (Peg-out) geri taşımasına olanak tanır.


**Peg-in Süreci:**

Bu izne tabi değildir. Bir kullanıcı federasyon kontrolündeki bir adrese BTC gönderir. Bitcoin blok zincirinin yeniden düzenlenmesine karşı koruma sağlamak için bu fonlar, eşdeğer L-BTC'nin yan zincirde basılmasından önce **102 onay** (yaklaşık 17 saat) beklemelidir.


**Peg-out Süreci:**

Bitcoin'e geri dönmek için L-BTC yakılır. Ancak, temel Bitcoin rezervlerinin çalınmasını önlemek için, peg-out'lar tam otomatik değildir. Bunlar için **Peg-Out Yetkilendirme Anahtarı (PAK)** sahibi bir üyenin yetkilendirmesi gerekir. Bitcoin fonlarının kendileri 11-of-15 çoklu-imzalı wallet'da güvence altına alınmıştır ve anahtarlar görevlilerin ana sunucularından hava boşluklu Donanım Güvenlik Modüllerinde (HSM'ler) tutulmaktadır.


**Dinamik Federasyon (Dynafed):**

Uzun ömürlülüğü sağlamak için Liquid, ağın sert bir fork olmadan görevlileri döndürmesine veya parametreleri güncellemesine olanak tanıyan bir protokol olan Dynafed'i kullanır. Bir görevlinin değiştirilmesi gerekiyorsa, ağ bir geçiş işlemi yayınlar. İki haftalık bir çakışma döneminden sonra yeni yapılandırma devreye girerek federasyonun kesintisiz çalışma süresini korurken sorunsuz bir şekilde gelişmesine olanak tanır.


## Ekosistem ve Sermaye Piyasaları


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: İş Stratejisi ve Ekosistem


Liquid teknik bir yan zincirden daha fazlasıdır; Bitcoin mainchain'in verimli bir şekilde destekleyemediği sermaye piyasalarının karmaşık gereksinimlerini karşılamak için tasarlanmış iş odaklı bir altyapı katmanıdır. Lightning Network yüksek frekanslı, düşük değerli ödemeler için optimize edilirken, Liquid yüksek değerli transferleri, varlık ihracını ve borsalar arası mutabakatı hedefler.


Ekosistem, borsalar, işlem masaları ve altyapı sağlayıcıları dahil olmak üzere ~73 şirketten oluşan bir konsorsiyum olan **Liquid Federasyonu** tarafından yönlendirilmektedir. Bu işbirlikçi model geleneksel finansal takas odalarını yansıtmakla birlikte daha fazla şeffaflık ve önemli ölçüde azaltılmış takas süreleri (T+2 güne karşılık 2 dakika) ile çalışmaktadır.


### Gerçek Dünya Varlıklarının (RWA) Tokenizasyonu


Liquid için temel iş durumu "Tokenizasyon "dur - gerçek dünya değerinin (hisse senetleri, tahviller, mining sözleşmeleri) blok zincirinde dijital tokenlar olarak temsil edilmesi. Bu üç temel avantaj sunmaktadır:

1.  **7/24 Küresel Piyasalar:** Bankacılık saatlerinin ve coğrafi kısıtlamaların kaldırılması.

2.  **Operasyonel Verimlilik:** Paylaşılan, değişmez bir defter aracılığıyla mutabakat hatalarının ortadan kaldırılması.

3.  **Atomik Mutabakat:** Teslimatın ödeme ile aynı anda gerçekleşmesini sağlayarak karşı taraf riskini azaltmak.


#### Düzenlenmiş Varlıklar ve AMP

Çoğu kurumsal varlık, yasal gereklilikler nedeniyle izinsiz işlem yapamaz. Varlık Yönetim Platformu (AMP)** bu kuralları uygulayan teknik standarttır.


- Beyaz Liste:** İhraççılar, elde tutma ve alım satım işlemlerini KYC tarafından doğrulanmış adreslerle kısıtlayabilir.
- Multisig Kontrolü:** Uyumluluk eylemleri (çalınan fonların dondurulması veya kayıp jetonların yeniden verilmesi gibi) çoklu imza yetkilendirmesi ile yönetilir ve tek bir çalışanın tek taraflı hareket edememesini sağlar.


Bu altyapı bugün yayında. Stalker** gibi platformlar Avrupa'da uçtan uca tokenizasyon hizmetleri sunarken **Sideswap** merkezi olmayan bir borsa ve gözetim dışı wallet olarak hareket ederek **Blockstream Mining Note (BMN)** ve tokenize MicroStrategy hisseleri (CMSTR) gibi varlıkların eşler arası ticaretine olanak sağlamaktadır.


### Gerçek Dünya Başarısı: Mayfell Örnek Olay İncelemesi


Liquid'ın faydasının en ikna edici kanıtı Meksika'daki **Mayfell** şirketinden geliyor. Geleneksel finansmanın kayıp, dolandırıcılık ve yavaş işleme eğilimli kağıt senetlere dayandığı bir pazarda Mayfell tüm altyapısını Liquid'a taşıdı.



- Ölçek:** **1,5 milyar $+** değerinde 25.000'in üzerinde senet düzenlenmiştir.
- Gizlilik:** Liquid'nin Confidential Transactions'ini kullanarak, kredi tutarları yalnızca borç veren ve borç alan tarafından görülebilir, bu da ticari gizliliği korurken denetçilerin defterin bütünlüğünü doğrulamasına olanak tanır.
- Etki:** Mayfell, banka dışı kredi verenleri blok zinciri aracılığıyla küresel sermaye piyasalarına bağlayarak maliyetleri düşürdü ve Meksikalı KOBİ'lerin krediye erişimini genişleterek Liquid'ün değer önerisinin spekülatif ticaretin çok ötesine uzandığını gösterdi.


### Diğer Zincirlere Karşı Stratejik Konumlandırma


Liquid, kalabalık bir tokenleştirme platformları (Ethereum, Solana, vb.) pazarında rekabet etmektedir, ancak belirgin stratejik avantajlara sahiptir:


- Düzenleyici Netlik:** Liquid, kendi yerel varlığı olarak Bitcoin (L-BTC) kullanır. Önceden mayınlanmış bir token veya bir ICO'ya sahip değildir ve diğer L1 blok zincirlerini rahatsız eden "kayıtsız güvenlik" risklerinden kaçınır.
- İstikrar:** Ethereum'un başarısız işlemlerin gaz ücretlerini yakmaya devam ettiği hesap modelinin aksine, Liquid'in UTXO modeli görev açısından kritik finansal veriler için deterministik ve güvenilirdir.
- Gizlilik:** Varsayılan gizlilik, çoğu finansal kurum için bir gerekliliktir ve Liquid'nin yerel olarak sunduğu bir özellik olup, genel zincirler karmaşık eklentiler olmadan uygulamakta zorlanır.


Geliştiriciler için bu ekosistem açık bir fırsat sunuyor: geleneksel finans ile Bitcoin'in güvenli mutabakat katmanı arasında köprü kuran araçlar (gösterge tabloları, cüzdanlar, uyumluluk entegrasyonları) oluşturmak.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Liquid üzerinde İzinli Varlık Kontrolü


Blockstream AMP (Varlık Yönetim Platformu), Liquid Network üzerinde kritik bir altyapı katmanı olarak hizmet vermekte olup, özellikle düzenlenmiş dijital menkul kıymetler ve sabit paralar ihraç edenler için tasarlanmıştır. Liquid, yerel varlık ihracı ile izinsiz bir temel katman sağlarken, düzenlenmiş kuruluşlar genellikle sıkı gözetim ve uyumluluk yeteneklerine ihtiyaç duyar. AMP, Liquid'in Confidential Transactions'ün gizlilik avantajlarından ödün vermeden belirli varlıklar üzerinde izinli bir kontrol katmanı sunarak bu boşluğu doldurmaktadır.


Platformun temel değer önerisi iki ana yeteneğe dayanmaktadır: kapsamlı ihraççı görünürlüğü ve işlem yetkilendirmesi. Tutarların ve türlerin katılımcılar dışında herkes için blinded olduğu standart Liquid varlıklarının aksine, AMP varlıkları ihraççının tamamen unblinded denetim izini korumasına olanak tanır. Bu şeffaflık, düzenleyici raporlama ve iç denetimler için gereklidir. Ayrıca AMP, ortak imza mekanizması aracılığıyla katı bir yetkilendirme modeli uygular. Bir AMP varlığının her transferi AMP sunucusundan bir imza gerektirir. Bu, ihraççıların hesapları dondurma, akredite yatırımcıları beyaz listeye alma veya transfer limitleri koyma gibi karmaşık kuralları off-chain uygulamalarına olanak tanır - merkezi olmayan bir ağ içinde etkili bir şekilde merkezi bir bekçi görevi görür.


#### Operasyonel Ödünleşimler

Bu mimari belirli ödünleşimleri beraberinde getirmektedir. Sistem AMP sunucusunun kullanılabilirliğine dayanır; sunucu bir ortak imzalayıcı olarak hareket eder ve çevrimdışı olursa, varlık likiditesi durur. Ayrıca, kullanıcıdan kullanıcıya gizlilik korunurken, yatırımcılar ihraççının varlıklarına tam görünürlük sağladığını kabul etmelidir. Bu model uyumlu güvenlik tokenları için idealdir ancak sansüre dayanıklı kripto paralar için uygun değildir.


### Mimari Evrimi ve Entegrasyon Yolları


AMP ekosistemi şu anda ilk iterasyonundan daha esnek, birlikte çalışabilir bir "Sürüm 2" mimarisine geçiş yapmaktadır. Eski sistem, düzenleyicilerin tamamen senkronize edilmiş Elements düğümlerini sürdürmelerini gerektiriyor ve geliştiricileri büyük ölçüde monolitik Green SDK'ya güvenmeye zorluyordu. İşlevsel olsa da, bu durum giriş için yüksek teknik engeller ve sınırlı wallet seçenekleri yaratmıştır.


Yeni nesil mimari, karmaşıklığı sunucuya kaydırarak bu gereksinimleri temelde basitleştirir. Bu yeni modelde AMP sunucusu işlem oluşturma, UTXO seçimi ve ücret hesaplama gibi ağır işleri üstlenir. İhraççıya sadece imza gerektiren Kısmen İmzalı bir Elements İşlemi (PSET) sunar. Bu "akıllı sunucu, aptal wallet" yaklaşımı, ihraççıların tam düğüm çalıştırma ihtiyacını ortadan kaldırır ve hazine yönetimi için donanım cüzdanlarının ve standart çoklu imza kurulumlarının kullanılmasını sağlar.


Geliştiriciler için bu evrim, tescilli SDK'lardan standart tanımlayıcılara ve PSET iş akışlarına doğru ilerlemek anlamına geliyor. Cüzdanlar artık yetkilendirme hakları oluşturmak için çoklu imza tanımlayıcılarını AMP sunucusuna kaydedebilir. Bu, AMP geliştirmeyi daha geniş Bitcoin wallet standartlarıyla uyumlu hale getirerek entegrasyonu PSBT/PSET formatlarını işleyebilen tüm uygulamalar için erişilebilir hale getirir. Bugün geliştirme yapan geliştiricilerin, bu modern, tanımlayıcı tabanlı mimarileri destekleyen Liquid Wallet Kiti (LWK) gibi araçları kullanmaları ve uygulamalarının yeni AMP standartları için geleceğe hazır olmasını sağlamaları teşvik edilmektedir.


### Liquid Wallet Ekosistemi ve Gizlilik


Liquid üzerinde uygulamalar oluşturmak, yerel varlıklar ve Confidential Transactions gibi özellikler nedeniyle standart Bitcoin geliştirmeye göre daha karmaşık bir yığında gezinmeyi gerektirir. Ekosistem katmanlı bir mimari ile desteklenmektedir: `secp256k1-zkp` gibi düşük seviyeli kütüphaneler kriptografik ilkelleri ele alırken, daha yüksek seviyeli araç setleri wallet mantığını yönetir.


Tarihsel olarak Green Geliştirme Kiti (GDK) kapsamlı ancak katı bir çözüm sunmuştur. Modern alternatif ise modüler bir yaklaşım sunan Liquid Wallet Kitidir (LWK). LWK, tanımlayıcıları, imzalamayı ve donanım iletişimini bağımsız olarak ele alarak endişeleri farklı kasalara ayırır ve geliştiricilere monolitik bir kütüphanenin ek yükü olmadan özel çözümler oluşturma esnekliği sağlar.


#### Confidential Transactions'in Kullanımı

Bu ekosistemdeki en belirgin zorluk, körleme yaşam döngüsünü yönetmektir. Liquid'de işlem çıktıları Elliptic Curve Diffie-Hellman (ECDH) anahtar değişimi kullanılarak şifrelenir. Bir gönderici, varlık miktarlarını ve türlerini şifrelemek için alıcının körleme açık anahtarını kullanır ve değerleri açığa çıkarmadan işlemin geçerliliğini doğrulayan bir aralık kanıtı oluşturur.


Bir wallet'nin çalışması için bu işlemi başarıyla tersine çevirmesi gerekir. Bir wallet gelen bir işlem tespit ettiğinde, özel körleme anahtarını kullanarak çıktının körlemesini kaldırmaya çalışır. Paylaşılan sır eşleşirse, wallet değerin şifresini çözebilir ve kullanıcının bakiyesine ekleyebilir. Bu süreç hesaplama açısından yoğundur ve işlemlerin matematiksel olarak dengeli olmasını sağlamak için körleme faktörlerinin hassas bir şekilde yönetilmesini gerektirir; LWK gibi araçların geliştirici için soyutlamayı amaçladığı bir karmaşıklıktır.


# Teknik


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Breez Liquid SDK'ya Giriş


Breez Liquid SDK, Liquid Network ve daha geniş Bitcoin ekosistemi arasındaki boşluğu doldurmak için tasarlanmış, kendi kendine yeten, açık kaynaklı bir araç setidir. Birincil görevi, Lightning Network düğüm yönetimi ve atomik takasların karmaşıklıklarını soyutlayarak geliştiricilerin sürtünmesiz finansal uygulamalar oluşturmasına olanak sağlamaktır.


"Mobil öncelikli" bir felsefeyle inşa edilen çekirdek mantık, performans ve güvenlik için Rust'te yazılmıştır, ancak Kotlin, Swift, Python, C#, Dart ve Flutter için yerel bağlamalar sağlamak için UniFFI (Unified Foreign Function Interface) kullanır. Bu, geliştiricilerin düşük seviyeli kriptografik işlemleri yönetmeden Bitcoin işlevselliğini tercih ettikleri ortama entegre edebilmelerini sağlar.


**Desteklenen İşlem Türleri:**

SDK, "ana üssü" olarak Liquid ile çalışır Üç özel işlemde mükemmeldir:

1.  **Liquid'dan Liquid'ya:** Doğrudan on-chain transferleri.

2.  **Liquid-to-Lightning:** Liquid fonları kullanılarak Lightning faturalarının ödenmesi.

3.  **Liquid'den Bitcoin'a:** Fonların doğrudan Bitcoin mainchain'e aktarılması.


*Not: SDK, doğrudan Lightning'den Lightning'e veya Bitcoin'den Bitcoin'e işlemleri desteklemez. Kesinlikle Liquid merkezli bir araçtır.*


### Ödeme Mimarileri: Denizaltı Takasları


Liquid, Lightning ve Bitcoin arasında merkezi saklayıcılar olmadan birlikte çalışabilirliği sağlamak için Breez **Denizaltı Takaslarına** dayanır. Bunlar, bir işlemin her iki ağda da başarıyla tamamlandığı veya her ikisinde de başarısız olduğu atomik işlemlerdir ve fonların aktarım sırasında asla kaybolmamasını sağlar.


#### Yıldırım Gönder (Denizaltı Takası)

Bir kullanıcı bir Lightning faturası ödediğinde, SDK Liquid Network'da bir "kilitleme" işlemi yayınlar. Bu, fonları etkin bir şekilde emanete alır. Takas sağlayıcısı (Boltz) bunu algılar, Lightning faturasını öder ve ardından kilitli Liquid fonlarını talep etmek için ödeme ön görüntüsünü (kriptografik makbuz) kullanır.


#### Yıldırım Alımı (Ters Denizaltı Takası)

Lightning'in alınması ters işlemdir. Kullanıcı bir fatura oluşturur ve takas sağlayıcısı fonları Lightning Network'da kilitler. SDK bu süreci WebSockets aracılığıyla izler. Kilit onaylandıktan sonra SDK, eşdeğer fonları kullanıcının Liquid wallet'ine taşımak için otomatik olarak bir talep işlemi yürütür.


#### Çapraz Zincir Bitcoin

Liquid'ten Bitcoin'e aktarımlar için mimari bir "ikili takas" mekanizması kullanır. Kilitleme işlemleri her iki zincirde de aynı anda gerçekleşir. Gönderici Bitcoin üzerinde fon talep ederken, alıcı Liquid üzerinde fon talep eder. Bu, federated peg çıkışlarına veya merkezi borsalara güvenmeksizin güvene dayalı köprüleme sağlar.


### Geliştirici Interface ve Otomatik Yönetim


Breez SDK, karmaşık finansal akışları standartlaştırılmış üç adımlı bir sürece yoğunlaştırarak geliştirici deneyimini basitleştirir: **Bağlan, Hazırla ve Yürüt**.


1.  **Bağlan:** wallet'yi başlatır, Liquid Wallet Kitini (LWK) kullanarak blok zinciri ile senkronize olur ve gerçek zamanlı izleme için WebSocket bağlantıları kurar.

2.  **Hazırla:** Fon taahhüdünde bulunmadan önce bu adım, ilgili tüm ağ ücretlerini ve takas maliyetlerini hesaplayıp iade ederek kullanıcı arayüzünün kullanıcıya net bir toplam sunmasını sağlar.

3.  **Yürüt:** Bu adım işlemi oluşturur, yayınlar ve takası başlatır.


#### Otomatik Güvenlik Mekanizmaları

SDK'nın en kritik özelliklerinden biri **Otomatik Geri Ödeme Yönetimi**. Bir ağ arızası veya işbirliği yapmayan bir karşı taraf durumunda, fonlar teorik olarak zaman kilitli bir sözleşmede sıkışıp kalabilir. SDK, kurtarma mantığını tamamen soyutlar. Her takasın durumunu izler; bir takas başarısız olursa veya zaman aşımına uğrarsa, SDK otomatik olarak fonları kullanıcının wallet'ine iade etmek için iade işlemini oluşturur ve yayınlar.


Ek olarak, SDK **Metadata Resolution** işlemlerini gerçekleştirir. off-chain takas verilerini (Boltz takasçısı tarafından sağlanan) on-chain işlem geçmişi ile birleştirir. Bu, kullanıcının işlem geçmişinin insan tarafından okunabilir olmasını ve yalnızca ham onaltılık işlem karmaları yerine fatura ayrıntılarını ve ödeme bağlamını görüntülemesini sağlar.


# Son Bölüm


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Yorumlar & Derecelendirmeler


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Final Sınavı


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Sonuç


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>