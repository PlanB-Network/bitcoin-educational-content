---
name: Teoriden pratiğe RGB protokolü
goal: RGB'i anlamak ve kullanmak için gereken becerileri edinme
objectives: 

  - RGB protokolünün temel kavramlarını anlamak
  - Client-side Validation ve Bitcoin taahhütlerinin ilkelerine hakim olun
  - RGB sözleşmelerinin nasıl oluşturulacağını, yönetileceğini ve aktarılacağını öğrenin
  - RGB uyumlu bir Lightning düğümü nasıl çalıştırılır


---
# RGB protokolünü keşfetme


Bitcoin Blockchain'un fikir birliği kurallarına ve işlemlerine dayalı olarak sözleşmeler ve varlıklar biçiminde dijital hakları uygulamak ve yürürlüğe koymak için tasarlanmış bir protokol olan RGB dünyasına dalın. Bu kapsamlı eğitim, "Client-side Validation" ve "Tek Kullanımlık Mühürler" kavramlarından gelişmiş akıllı sözleşmelerin uygulanmasına kadar RGB'in teknik ve pratik temelleri konusunda size rehberlik eder.


Yapılandırılmış, adım adım ilerleyen bir program aracılığıyla Client-side Validation'nin mekanizmalarını, Bitcoin'teki deterministik taahhütleri ve kullanıcılar arasındaki etkileşim modellerini keşfedeceksiniz. RGB veya Bitcoin üzerinde Lightning Network tokenlarının nasıl oluşturulacağını, yönetileceğini ve transfer edileceğini öğrenin.


İster bir geliştirici, ister Bitcoin meraklısı olun ya da sadece bu teknoloji hakkında daha fazla bilgi edinmek isteyin, bu eğitim size RGB'de uzmanlaşmak ve Bitcoin üzerinde yenilikçi çözümler oluşturmak için ihtiyacınız olan araçları ve bilgileri sağlayacaktır.


Kurs, Fulgur'Ventures tarafından düzenlenen ve üç tanınmış öğretmen ve RGB uzmanı tarafından verilen canlı bir seminere dayanmaktadır.


+++
# Giriş


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## Kurs sunumu


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


Herkese merhaba ve Bitcoin ve Lightning Network üzerinde çalışan, istemci tarafında doğrulanmış bir Smart contract sistemi olan RGB'ye adanmış bu eğitim kursuna hoş geldiniz. Bu kursun yapısı, bu karmaşık konunun derinlemesine araştırılmasını sağlamak üzere tasarlanmıştır. Kurs şu şekilde düzenlenmiştir:


**Bölüm 1: Teori**


İlk bölüm, Client-side Validation ve RGB'in temellerini anlamak için gereken teorik kavramlara ayrılmıştır. Bu kursta keşfedeceğiniz gibi, RGB, genellikle Bitcoin'te görülmeyen bir dizi teknik kavramı tanıtmaktadır. Bu bölümde, RGB protokolüne özgü tüm terimlerin tanımlarını içeren bir sözlük de bulacaksınız.


**Bölüm 2: Uygulama**


İkinci bölüm, bölüm 1'de görülen teorik kavramların uygulanmasına odaklanacaktır. RGB sözleşmelerini nasıl oluşturacağımızı ve manipüle edeceğimizi öğreneceğiz. Ayrıca bu araçlarla nasıl programlama yapacağımızı da göreceğiz. Bu ilk iki bölüm Maxim Orlovsky tarafından sunulmuştur.


**Bölüm 3: Uygulamalar**


Son bölüm, gerçek hayattaki kullanım durumlarını vurgulamak için RGB tabanlı somut uygulamalar sunan diğer konuşmacılar tarafından yönetilmektedir.


---
Bu eğitim kursu aslında [Fulgur'Ventures] (https://fulgur.ventures/) tarafından Viareggio, Toskana'da düzenlenen iki haftalık bir ileri geliştirme eğitim kampından doğmuştur. Rust ve SDK'lara odaklanan ilk hafta, bu diğer kursta bulunabilir:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

Bu kursta, RGB'a odaklanan bootcamp'in ikinci haftasına odaklanıyoruz.


**Hafta 1 - LNP402:**


![RGB-Bitcoin](assets/fr/001.webp)


**2. Hafta - Güncel eğitim CSV402:**


![RGB-Bitcoin](assets/fr/002.webp)


Bu canlı kursları düzenleyenlere ve katılan 3 öğretmene çok teşekkürler:




- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, yapay zeka, robotik, transhümanizm. RGB, Prime, Radiant ve lnp_bp, mycitadel_io & cyphernet_io*'nun yaratıcısı;
- Hunter Trujilo: *Geliştirici, Rust, Bitcoin, Yıldırım, RGB*;
- Federico Tenga: *Dünyayı bir Cypherpunk distopyasına dönüştürmek için elimden geleni yapıyorum. Şu anda Bitfinex'te RGB üzerinde çalışıyorum*.


Bu eğitim kursunun yazılı versiyonu 2 ana kaynak kullanılarak hazırlanmıştır:




- Maxim Orlovsky, Hunter Trujilo ve Frederico Tenga'nın Lightning Bootcamp'teki seminerinin videoları;
- Üretimi [Bitfinex] (https://www.bitfinex.com/) tarafından desteklenen RGB dokümantasyonu.


RGB'nin karmaşık ve büyüleyici dünyasına dalmaya hazır mısınız? Hadi başlayalım!


# Teoride RGB


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## Dağıtık hesaplama kavramlarına giriş


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB, Bitcoin Blockchain'ın mutabakat kurallarına ve işlemlerine dayalı olarak dijital hakları (sözleşmeler ve varlıklar şeklinde) ölçeklenebilir ve gizli bir şekilde uygulamak ve yürürlüğe koymak için tasarlanmış bir protokoldür. Bu ilk bölümün amacı, RGB protokolü etrafındaki temel kavramları ve terminolojiyi sunmak ve özellikle Client-side Validation ve Tek Kullanımlık Mühürler gibi temel dağıtılmış bilgi işlem kavramlarıyla olan yakın bağlantılarını vurgulamaktır.


Bu bölümde, **dağıtık mutabakat sistemlerinin** temellerini inceleyeceğiz ve RGB'ün bu teknoloji ailesine nasıl uyduğunu göreceğiz. Ayrıca, RGB'ün neden Bitcoin'ün kendi mutabakat mekanizmasından bağımsız ve genişletilebilir olmayı amaçladığını anlamamıza yardımcı olan ana ilkeleri de tanıtacağız.


### Giriş


Bilgisayar biliminin belirli bir dalı olan dağıtık bilgi işlem, düğümlerden oluşan bir ağ üzerinde bilgi dolaşımı ve işlenmesi için kullanılan protokolleri inceler. Bu düğümler ve protokol kuralları birlikte dağıtılmış sistem olarak bilinen şeyi oluşturur. Böyle bir sistemi karakterize eden temel özellikler arasında bazıları şunlardır:




- Belirli verilerin her bir düğüm tarafından bağımsız olarak doğrulanması ve onaylanması **yeteneği**;
- Düğümlerin (protokole bağlı olarak) bilginin tam veya kısmi bir görünümünü oluşturma olasılığı. Bu görünümler dağıtılmış sistemin **durumlarıdır**;
- Verilerin güvenilir bir şekilde zaman damgalı olması ve olayların sırası (durumların sırası) konusunda bir fikir birliği olması için işlemlerin **kronolojik sırası**.


Özellikle, dağıtık bir sistemde **uzlaşma** kavramı iki yönü kapsar:




- Durum değişikliklerinin geçerliliğinin **tanınması** (protokol kurallarına göre);
- Bu durum değişikliklerinin sırası üzerinde anlaşmaya varılması, onaylanmış işlemlerin a posteriori olarak yeniden yazılmasını veya tersine çevrilmesini imkansız hale getirir (bu, Bitcoin'te "çift harcama koruması" olarak da bilinir).


Dağıtılmış bir mutabakat mekanizmasının ilk işlevsel, izinsiz uygulaması Satoshi Nakamoto tarafından Bitcoin ile tanıtıldı, Blockchain veri yapısı ve Proof-of-Work (PoW) algoritmasının birlikte kullanımı sayesinde. Bu sistemde, blok geçmişinin güvenilirliği, düğümler (madenciler) tarafından buna ayrılan hesaplama gücüne bağlıdır. Bu nedenle Bitcoin, herkese açık (*izinsiz*) dağıtılmış bir mutabakat sisteminin önemli ve tarihi bir örneğidir.


Blockchain ve dağıtık bilgi işlem dünyasında iki temel paradigmayı ayırt edebiliriz: *geleneksel anlamda **Blockchain*** ve üretimdeki en iyi örneği Lightning Network olan ***devlet kanalları***. Blockchain, açık, izinsiz bir ağ içinde fikir birliği ile çoğaltılan, kronolojik olarak sıralanmış olayların bir kaydı olarak tanımlanır. Öte yandan durum kanalları, iki (veya daha fazla) katılımcının güncellenmiş bir off-chain durumunu sürdürmesini sağlayan ve Blockchain'i yalnızca bu kanalları açarken ve kapatırken kullanan eşler arası kanallardır.


Bitcoin bağlamında, Mining'un ilkelerine, Blockchain'daki işlemlerin ademi merkeziyetçiliğine ve kesinliğine ve ayrıca ödeme kanallarının nasıl çalıştığına şüphesiz aşinasınız. RGB ile, Blockchain veya Lightning'den farklı olarak, bir Smart contract'in durum geçişlerini yerel olarak (istemci tarafında) depolamayı ve doğrulamayı içeren **Client-side Validation** adlı yeni bir paradigma sunuyoruz. Bu aynı zamanda diğer "DeFi" tekniklerinden (_rollups_, _plasma_, _ARK_, vb.) farklıdır; burada Client-side Validation, Double-spending'ü önlemek ve bir zaman damgalama sistemine sahip olmak için Blockchain'ya güvenirken, off-chain durumlarının ve geçişlerinin kaydını yalnızca ilgili katılımcılarla tutar.


![RGB-Bitcoin](assets/fr/003.webp)


Daha sonra, önemli bir terimi de tanıtacağız: "**Stash**" kavramı, bir Contract'ün durumunu korumak için gereken istemci tarafı veri kümesini ifade eder, çünkü bu veriler ağ genelinde küresel olarak çoğaltılmaz. Son olarak, Client-side Validation'den yararlanan bir protokol olan RGB'in arkasındaki mantığa ve neden mevcut yaklaşımları (Blockchain ve durum kanalları) tamamladığına bakacağız.


### Dağıtık bilişimde ikilemler


Client-side Validation ve RGB Address sorunlarının Blockchain ve Lightning tarafından nasıl çözülmediğini anlamak için dağıtık bilgi işlemdeki 3 büyük "üçlemeyi" keşfedelim:




- **Ölçeklenebilirlik, Ademi Merkeziyetçilik, Gizlilik**;
- **CAP Teoremi** (Tutarlılık, Kullanılabilirlik, Bölünme Toleransı);
- **CIA** trilemması (Gizlilik, Bütünlük, Kullanılabilirlik).


#### 1. Ölçeklenebilirlik, ademi merkeziyetçilik ve gizlilik




- **Blockchain (Bitcoin)**


Blockchain son derece merkezsizdir, ancak ölçeklenebilir değildir. Dahası, her şey küresel, halka açık bir kayıtta olduğu için gizlilik sınırlıdır. Sıfır bilgi teknolojileri (Confidential Transactions, mimblewimble şemaları, vb.) ile gizliliği artırmayı deneyebiliriz, ancak halka açık zincir işlem grafiğini gizleyemez.




- **Yıldırım/ Eyalet kanalları**


Devlet kanalları (Lightning Network'te olduğu gibi) Blockchain'e göre daha ölçeklenebilir ve daha özeldir, çünkü işlemler off-chain'da gerçekleşir. Bununla birlikte, belirli Elements'yi (finansman işlemleri, ağ topolojisi) kamuya duyurma zorunluluğu ve ağ trafiğinin izlenmesi gizliliği kısmen tehlikeye atabilir. Ademi merkeziyetçilik de zarar görür: yönlendirme nakit yoğundur ve büyük düğümler merkezileşme noktaları haline gelebilir. Lightning'de görmeye başladığımız olgu da tam olarak budur.




- **Client-side Validation (RGB)**


Bu yeni paradigma daha da ölçeklenebilir ve daha gizlidir, çünkü sadece sıfır ifşa bilgi kanıtı tekniklerini entegre etmekle kalmayız, aynı zamanda hiç kimse tüm kaydı tutmadığı için küresel bir işlem grafiği de yoktur. Öte yandan, ademi merkeziyetçilik konusunda da belirli bir taviz anlamına gelir: Smart contract'i çıkaran kişi merkezi bir role sahip olabilir (Ethereum'daki "Contract dağıtıcısı" gibi). Ancak, Blockchain'den farklı olarak, Client-side Validation ile yalnızca ilgilendiğiniz sözleşmeleri depolar ve doğrularsınız, bu da mevcut tüm durumları indirme ve doğrulama ihtiyacını ortadan kaldırarak ölçeklenebilirliği artırır.


![RGB-Bitcoin](assets/fr/004.webp)


#### 2. CAP Teoremi (Tutarlılık, Kullanılabilirlik, Bölme toleransı)


CAP teoremi, dağıtık bir sistemin *Tutarlılık*, *Kullanılabilirlik* ve *Bölüm toleransını* aynı anda karşılamasının imkansız olduğunu vurgulamaktadır.




- **Blockchain**


Blockchain tutarlılığı ve kullanılabilirliği tercih eder, ancak ağ bölümleme ile iyi sonuç vermez: bir bloğu göremiyorsanız, hareket edemez ve tüm ağ ile aynı görünüme sahip olamazsınız.




- **Yıldırım**


Durum kanalları sistemi kullanılabilirlik ve bölümleme toleransına sahiptir (çünkü ağ parçalansa bile iki düğüm birbirine bağlı kalabilir), ancak genel tutarlılık Blockchain üzerindeki kanalların açılıp kapanmasına bağlıdır.




- **Client-side Validation (RGB)**


RGB gibi bir sistem tutarlılık (her katılımcı kendi verilerini belirsizlik olmadan yerel olarak doğrular) ve bölümleme toleransı (verilerinizi özerk olarak tutarsınız) sunar, ancak küresel kullanılabilirliği garanti etmez (herkesin ilgili geçmiş parçalarına sahip olduğundan emin olması gerekir ve bazı katılımcılar hiçbir şey yayınlamayabilir veya belirli bilgileri paylaşmayı bırakabilir).


![RGB-Bitcoin](assets/fr/005.webp)


#### 3. CIA trilemması (Gizlilik, Bütünlük, Kullanılabilirlik)


Bu üçleme bize gizlilik, bütünlük ve kullanılabilirliğin hepsinin aynı anda optimize edilemeyeceğini hatırlatır. Blockchain, Lightning ve Client-side Validation bu dengeye farklı şekillerde girmektedir. Buradaki fikir, tek bir sistemin her şeyi sağlayamayacağıdır; her boyutta iyi garantiler sunan tutarlı bir paket elde etmek için çeşitli yaklaşımları (Blockchain'in zaman damgası, Lightning'in eşzamanlı yaklaşımı ve RGB ile yerel doğrulama) birleştirmek gerekir.


![RGB-Bitcoin](assets/fr/006.webp)


### Blockchain'ün rolü ve parçalama kavramı


Blockchain (bu durumda Bitcoin) öncelikle bir _zaman damgalama_ mekanizması ve çifte harcamaya karşı koruma görevi görür. Bir Smart contract veya merkezi olmayan sistemin tüm verilerini eklemek yerine, işlemlere (Client-side Validation anlamında, "durum geçişleri" olarak adlandıracağımız) **kriptografik taahhütleri** dahil ediyoruz. Böylece:




- Blockchain'i büyük miktarda veri ve mantıktan kurtarıyoruz;
- Her kullanıcı Global State'u kopyalamak yerine yalnızca Contract'ün kendi bölümü ("*Shard*") için gereken geçmişi depolar.


Parçalama, dağıtık veritabanlarında (örneğin Facebook veya Twitter gibi sosyal ağlar için MySQL) ortaya çıkan bir kavramdır. Veri hacmi ve senkronizasyon gecikmeleri sorununu çözmek için veritabanı _shards_ (ABD, Avrupa, Asya, vb.) olarak bölümlere ayrılır. Her bölüm yerel olarak tutarlıdır ve diğerleriyle yalnızca kısmen senkronize edilir.


RGB tipi akıllı sözleşmeler için, sözleşmelerin kendilerine göre Shard. Her Contract bağımsız bir _shard_'dır. Örneğin, yalnızca USDT token'larına sahipseniz, USDC gibi başka bir token'nin tüm geçmişini saklamanız veya doğrulamanız gerekmez. Bitcoin'te, Blockchain _sharding_ yapmaz: global bir UTXO setiniz vardır. Client-side Validation ile her katılımcı yalnızca elinde tuttuğu veya kullandığı Contract verilerini saklar.


Bu nedenle ekosistemi aşağıdaki gibi hayal edebiliriz:




- **Blockchain (Bitcoin)** minimal bir kaydın tam olarak çoğaltılmasını sağlayan bir temel olarak ve zaman damgası Layer olarak hizmet eder;
- Hızlı **Lightning Network**, **Confidential Transactions**, hala Bitcoin Blockchain'ün güvenliğine ve nihai uzlaşmasına dayanmaktadır;
- Blockchain'i karıştırmadan veya gizliliği kaybetmeden daha karmaşık Smart contract mantığı eklemek için **RGB ve Client-side Validation**.


![RGB-Bitcoin](assets/fr/007.webp)


Bu üç Elements, "Layer 2", "Layer 3" ve benzeri doğrusal bir yığın yerine üçgen bir bütün oluşturur. Lightning doğrudan Bitcoin'e bağlanabilir veya RGB verilerini içeren Bitcoin işlemleriyle ilişkilendirilebilir. Benzer şekilde, bir "BiFi" (Bitcoin üzerinde finans) gizlilik, ölçeklenebilirlik veya Contract mantığı ihtiyaçlarına göre Blockchain, Lightning ve RGB ile oluşturulabilir.


![RGB-Bitcoin](assets/fr/008.webp)


### Durum geçişleri kavramı


Herhangi bir dağıtık sistemde, doğrulama mekanizmasının amacı **durum değişikliklerinin geçerliliğini ve kronolojik sırasını belirleyebilmektir**. Amaç, protokol kurallarına uyulduğunu doğrulamak ve bu durum değişikliklerinin kesin, tartışılmaz bir sırayla birbirini takip ettiğini kanıtlamaktır.


Bu doğrulamanın **Bitcoin** bağlamında nasıl çalıştığını anlamak ve daha genel olarak Client-side Validation'nın arkasındaki felsefeyi kavramak için, önce Bitcoin Blockchain'nin mekanizmalarına bir göz atalım, ardından Client-side Validation'nın onlardan nasıl farklı olduğunu ve hangi optimizasyonları mümkün kıldığını görelim.


![RGB-Bitcoin](assets/fr/009.webp)


Bitcoin Blockchain durumunda, işlem doğrulaması basit bir kurala dayanır:




- Tüm ağ düğümleri her bloğu ve işlemi indirir;
- UTXO setinin (harcanmamış tüm çıktılar) doğru gelişimini doğrulamak için bu işlemleri onaylarlar;
- Bu verileri (bloklar şeklinde) depolarlar, böylece geçmiş gerektiğinde yeniden oynatılabilir.


![RGB-Bitcoin](assets/fr/010.webp)


Ancak bu modelin iki önemli dezavantajı vardır:




- **Ölçeklenebilirlik**: her düğümün herkesin işlemlerini işlemesi, doğrulaması ve arşivlemesi gerektiğinden, özellikle maksimum blok boyutuyla bağlantılı olarak işlem kapasitesinde bariz bir sınır vardır (çerezler hariç Bitcoin için 10 dakikada ortalama 1 MB);
- **Gizlilik**: her şey herkese açık olarak yayınlanır ve saklanır (miktarlar, hedef adresler, vb.), bu da alışverişlerin gizliliğini sınırlar.


![RGB-Bitcoin](assets/fr/012.webp)


Uygulamada, bu model Bitcoin için temel Layer (Layer 1) olarak çalışır, ancak aynı anda yüksek işlem hacmi ve belirli bir gizlilik derecesi gerektiren daha karmaşık kullanımlar için yetersiz kalabilir.


Client-side Validation tam tersi bir fikre dayanmaktadır: tüm ağın tüm işlemleri doğrulamasını ve saklamasını gerektirmek yerine, her katılımcı (istemci) geçmişin yalnızca kendisini ilgilendiren kısmını doğrulayacaktır:




- Bir kişi bir varlık (veya başka bir dijital mülk) aldığında, yalnızca bu varlığa yol açan işlemler zincirini (durum geçişleri) bilmesi ve doğrulaması ve meşruiyetini kanıtlaması gerekir;
- Bu işlemler dizisi, ***Genesis***'dan (ilk ihraç) en son işleme kadar, bir asiklik yönlendirilmiş grafik (DAG) veya Shard, yani genel geçmişin bir kısmını oluşturur.


![RGB-Bitcoin](assets/fr/013.webp)


Aynı zamanda, ağın geri kalanının (veya daha doğrusu, Bitcoin gibi temel Layer'in) bu verilerin ayrıntılarını görmeden son duruma kilitlenebilmesi için Client-side Validation, ***Commitment*** kavramına dayanır.


Bir *Commitment*, bir Bitcoin işlemine eklenen ve bu verileri ifşa etmeden özel verilerin dahil edildiğini kanıtlayan kriptografik bir Commitment, tipik olarak bir _hash_ (örneğin SHA-256).


Bu taahhütler sayesinde kanıtlayabiliriz:




- Bilginin varlığı (bir Hash'e bağlı olduğu için);
- Bu bilginin önceliği (çünkü Blockchain'te tarih ve blok sırası ile sabitlenmiş ve zaman damgalıdır).


Ancak tam içerik açıklanmamakta, böylece gizliliği korunmaktadır.


Somut olarak, bir RGB State Transition'nın nasıl çalıştığı aşağıda açıklanmıştır:




- Yeni bir State Transition hazırlıyorsunuz (örneğin bir RGB token'un transferi);
- Bu geçişe kriptografik bir generate eklersiniz ve bunu bir Bitcoin işlemine eklersiniz (bu taahhütler RGB protokolünde "*anchor*" olarak adlandırılır);
- Karşı taraf (alıcı) bu varlıkla ilişkili müşteri tarafı geçmişini alır ve Smart contract'in Genesis'sından ona ilettiğiniz geçişe kadar uçtan uca tutarlılığı doğrular.


![RGB-Bitcoin](assets/fr/014.webp)


Client-side Validation iki önemli avantaj sunmaktadır:




- **Ölçeklenebilirlik:**


Blockchain'e dahil edilen *komiteler* küçüktür (birkaç düzine bayt mertebesinde). Bu, yalnızca Hash'ın dahil edilmesi gerektiğinden blok alanının doymuş olmamasını sağlar. Ayrıca, her kullanıcının yalnızca kendi geçmiş parçasını (kendi _stash_'i) saklaması gerektiğinden, off-chain protokolünün gelişmesini sağlar.




- **Gizlilik:**


İşlemlerin kendileri (yani ayrıntılı içerikleri) On-Chain yayınlanmamaktadır. Sadece parmak izleri (*Hash*) yayınlanır. Böylece, tutarlar, adresler ve Contract mantığı gizli kalır ve alıcı önceki tüm geçişleri inceleyerek Shard'ün geçerliliğini yerel olarak doğrulayabilir. Alıcının bu verileri, bir anlaşmazlık veya kanıtın gerekli olduğu durumlar haricinde, kamuya açması için hiçbir neden yoktur.


RGB gibi bir sistemde, farklı sözleşmelerden (veya farklı varlıklardan) birden fazla durum geçişi tek bir _commitment_ aracılığıyla tek bir Bitcoin işleminde toplanabilir. Bu mekanizma, On-Chain işlemi ile off-chain verileri (istemci tarafında onaylanmış geçişler) arasında deterministik, zaman damgalı bir bağlantı kurar ve birden fazla parçanın aynı anda tek bir Anchor noktasına kaydedilmesini sağlayarak On-Chain maliyetini ve ayak izini daha da azaltır.


Uygulamada, bu Bitcoin işlemi onaylandığında, Blockchain'te zaten yazılı olan Hash'yi değiştirmek imkansız hale geldiğinden, temel sözleşmelerin durumunu kalıcı olarak "kilitler".


![RGB-Bitcoin](assets/fr/015.webp)


### Stash konsepti


Bir **Stash**, bir katılımcının bir RGB Smart contract'ün bütünlüğünü ve geçmişini korumak için kesinlikle saklaması gereken istemci tarafı veri kümesidir. Belirli durumların paylaşılan bilgilerden yerel olarak yeniden oluşturulabildiği bir Lightning kanalının aksine, bir RGB Contract'in Stash'sı başka bir yerde çoğaltılmaz: kaybederseniz, geçmişteki payınızdan sorumlu olduğunuz için kimse size geri yükleyemez. Bu nedenle RGB'de güvenilir yedekleme prosedürlerine sahip bir sistem benimsemeniz gerekir.


![RGB-Bitcoin](assets/fr/016.webp)


### Single-Use Seal: kökenleri ve işleyişi


Para birimi gibi bir varlığı kabul ederken iki garanti esastır:




- Alınan ürünün orijinalliği;
- Çifte masraftan kaçınmak için alınan ürünün benzersizliği.


Bir banknot gibi fiziksel varlıklar için, fiziksel mevcudiyet çoğaltılmadığını kanıtlamak için yeterlidir. Ancak, varlıkların tamamen bilgisel olduğu dijital dünyada, bilgi kolayca çoğalabildiği ve kopyalanabildiği için bu doğrulama daha karmaşıktır.


Daha önce gördüğümüz gibi, göndericinin durum geçişlerinin geçmişini ifşa etmesi, bir RGB token'nin gerçekliğinden emin olmamızı sağlar. Genesis işleminden bu yana gerçekleşen tüm işlemlere erişim sağlayarak token'nin gerçekliğini teyit edebiliriz. Bu ilke, geçerliliklerini doğrulamak için madeni paraların geçmişinin orijinal Coinbase Transaction'a kadar izlenebildiği Bitcoin'e benzer. Ancak, Bitcoin'den farklı olarak, RGB'teki durum geçişlerinin bu geçmişi özeldir ve istemci tarafında tutulur.


RGB belirteçlerinin Double-spending'ünü önlemek için "**Single-Use Seal**" adı verilen bir mekanizma kullanıyoruz. Bu sistem, bir kez kullanılan her bir token'nın hileli bir şekilde ikinci kez kullanılamamasını sağlar.


Tek Kullanımlık Mühürler, 2016 yılında Peter Todd tarafından önerilen ve fiziksel mühür kavramına benzeyen kriptografik ilkellerdir: bir Seal bir kaba yerleştirildikten sonra, Seal'i geri döndürülemez bir şekilde kırmadan açmak veya değiştirmek imkansız hale gelir.


![RGB-Bitcoin](assets/fr/018.webp)


Dijital dünyaya aktarılan bu yaklaşım, bir olaylar dizisinin gerçekten gerçekleştiğini ve artık a posteriori olarak değiştirilemeyeceğini kanıtlamayı mümkün kılmaktadır. Tek kullanımlık Mühürler böylece `Hash + Timestamp` basit mantığının ötesine geçerek **sadece bir kez** kapatılabilen bir Seal kavramını ekler.


![RGB-Bitcoin](assets/fr/017.webp)


Tek Kullanımlık Mühürlerin işe yaraması için, bir yayının varlığını veya yokluğunu kanıtlayabilecek ve bilgi yayıldıktan sonra tahrif edilmesi zor (imkansız olmasa da) bir yayın kanıt aracına ihtiyacınız vardır. Bir **Blockchain** (Bitcoin gibi) bu rolü yerine getirebilir, örnek olarak kamu tirajına sahip bir kağıt gazete de bunu yapabilir. Fikir şu şekildedir:




- Bir `h(m)` mesajı üzerindeki belirli bir Commitment'ün, `m` mesajının içeriğini ifşa etmeden bir kitleye yayınlandığını kanıtlamak istiyoruz;
- Commitment'in `h(m)` yerine başka bir rakip `h(m')` mesajının yayınlanmadığını kanıtlamak istiyoruz;
- Ayrıca `m` mesajının belirli bir tarihten önce var olup olmadığını da kontrol edebilmek istiyoruz.


Bir Blockchain bu rol için idealdir: bir işlem bir bloğa dahil edilir edilmez, tüm ağ bu işlemin varlığı ve içeriği hakkında aynı yanlışlanamaz kanıta sahip olur (en azından kısmen, çünkü _commitment_ mesajın gerçekliğini kanıtlarken ayrıntıları gizleyebilir).


Bu nedenle bir Single-Use Seal, bir mesajı (bu aşamada hala bilinmeyen) bir kez ve yalnızca bir kez, ilgili tüm taraflarca doğrulanabilecek şekilde yayınlamak için resmi bir söz olarak görülebilir.


Basit _commitments_ (Hash) veya varoluş tarihini kanıtlayan zaman damgalarının aksine, bir Single-Use Seal **hiçbir alternatif Commitment**'un bir arada bulunamayacağına dair ek bir garanti sunar: aynı Seal'i iki kez kapatamaz veya mühürlü mesajı değiştirmeye çalışamazsınız.


Aşağıdaki karşılaştırma bu ilkenin anlaşılmasına yardımcı olacaktır:




- **Kriptografik Commitment (Hash)**: Bir Hash işleviyle, Hash'ünü yayınlayarak bir veri parçasını (bir sayı) taahhüt edebilirsiniz. Veri, siz ön görüntüyü açıklayana kadar gizli kalır, ancak bunu önceden bildiğinizi kanıtlayabilirsiniz;
- **Timestamp (Blockchain)**: Bu Hash'yı Blockchain'e ekleyerek, onu kesin bir anda (bir bloğa dahil etme anında) bildiğimizi de kanıtlamış oluruz;
- **Single-Use Seal**: Tek kullanımlık mühürlerle, Commitment'u benzersiz hale getirerek bir adım daha ileri gidiyoruz. Tek bir Hash ile, paralel olarak birkaç çelişkili taahhüt oluşturabilirsiniz (aileye "*Bu bir erkek*" ve kişisel günlüğünde "*Bu bir kız*" diyen doktorun sorunu). Single-Use Seal, Commitment'u Bitcoin Blockchain gibi bir yayın kanıtı aracına bağlayarak bu olasılığı ortadan kaldırır, böylece UTXO'nin harcanması Commitment'u kesin olarak mühürler. Bir kez harcandıktan sonra, aynı UTXO, Commitment'un yerini almak üzere yeniden harcanamaz.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

Tek Kullanımlık Mühürler üç ana aşamada çalışır:


**Seal Definition:**




- Alice, Seal'in yayınlanmasına ilişkin kuralları önceden tanımlar (mesajın ne zaman, nerede ve nasıl yayınlanacağı);
- Bob bu koşulları kabul eder veya onaylar.


![RGB-Bitcoin](assets/fr/021.webp)


**Seal Kapanış:**




- Çalışma zamanında, Alice asıl mesajı yayınlayarak Seal'yi kapatır (genellikle bir _commitment_ şeklinde, örneğin bir Hash);
- Ayrıca Seal'in kapalı ve geri alınamaz olduğunu kanıtlayan bir **şahit** (kriptografik kanıt) sağlar.


![RGB-Bitcoin](assets/fr/019.webp)


**Seal Doğrulama:**




- Seal kapatıldıktan sonra, Bob artık onu açamaz: sadece kapatıldığını kontrol edebilir;
- Bob, Seal'yı, **tanığı** ve mesajı (veya Commitment'ini) toplayarak her şeyin eşleştiğinden ve rakip mühürler veya farklı versiyonlar olmadığından emin olur.


Süreç aşağıdaki şekilde özetlenebilir:


```txt
# Defined by Alice, validated or accepted by Bob
seal <- Define()
# Seal is closed by Alice with the message
witness <- Close(seal, message)
# Verification by Bob
bool <- Verify(seal, witness, message)
```


Ancak Client-side Validation bir adım daha ileri gider: eğer bir Seal'un tanımının kendisi Blockchain'un dışında kalırsa, birisinin söz konusu Seal'un varlığına veya meşruiyetine itiraz etmesi (teoride) mümkündür. Bu sorunun üstesinden gelmek için birbirine kenetlenen Tek Kullanımlık Mühürler zinciri kullanılır:




- Her kapalı Seal bir sonraki Seal'in tanımını içerir;
- Bu kapanışları (_commitments_ ile birlikte) Blockchain içinde (bir Bitcoin işleminde) kaydederiz;
- Dolayısıyla, önceki Seal'i değiştirmeye yönelik herhangi bir girişim Bitcoin'te yer alan tarihle çelişecektir.


RGB sisteminin yaptığı da tam olarak budur:




- Yayınlanan mesajlar, istemci tarafında doğrulanmış verilere _taahhütlerdir_;
- Seal Definition bir Bitcoin UTXO ile ilişkilidir;
- Bu UTXO harcandığında veya aynı Commitment'a yeni bir çıktı yatırıldığında Seal kapanır;
- Bu UTXO'ları harcayan işlem zinciri yayın kanıtına karşılık gelir: RGB üzerindeki her geçiş veya durum değişikliği böylece Bitcoin'e bağlanır.


Özetle:




- Mühür tanımı_ gelecekteki bir Commitment için Seal niyetinde olduğunuz UTXO'dir;
- Bu UTXO'u harcayarak Commitment'i içeren bir işlem oluşturduğunuzda _seal closing_ gerçekleşir;
- Tanık_, Seal'yi bu içerikle kapattığınızı kanıtlayan işlemin kendisidir;
- Bir Seal'in kapatılmadığını kanıtlayamazsınız (bir UTXO'nin zaten harcanmadığından veya henüz görmediğiniz bir blokta harcanmayacağından kesinlikle emin olamazsınız), ancak gerçekten kapatıldığını kanıtlayabilirsiniz.


Bu benzersizlik Client-side Validation için önemlidir: bir State Transition'ü doğruladığınızda, bunun daha önce rakip bir Commitment'te harcanmamış benzersiz bir UTXO'ye karşılık geldiğini kontrol edersiniz. Bu, off-chain akıllı sözleşmelerinde çifte harcamanın olmamasını garanti eden şeydir.


### Çoklu taahhütler ve kökler


Bir RGB Smart contract'un aynı anda birkaç Tek Kullanımlık Mühür (birkaç UTXO) harcaması gerekebilir. Dahası, tek bir Bitcoin işlemi, her biri kendi State Transition'ini mühürleyen birkaç farklı sözleşmeye referans verebilir. Bu durum, taahhütlerin hiçbirinin mükerrer olmadığını deterministik ve benzersiz bir şekilde kanıtlamak için bir **çoklu Commitment** mekanizması gerektirir. RGB'te **Anchor** kavramı burada devreye girer: bir Bitcoin işlemini ve her biri potansiyel olarak farklı bir Contract'e ait olan bir veya daha fazla istemci tarafı taahhüdünü (durum geçişleri) birbirine bağlayan özel bir yapı. Bir sonraki bölümde bu kavrama daha yakından bakacağız.


![RGB-Bitcoin](assets/fr/023.webp)


Projenin ana GitHub depolarından ikisi (LNPBP organizasyonu altında) ilk bölümde incelenen bu kavramların temel uygulamalarını bir araya getirmektedir:




- **client_side_validation**: Yerel doğrulama için Rust ilkellerini içerir;
- **single_use_seals**: Bu mühürleri güvenli bir şekilde tanımlamak ve kapatmak için mantığı uygular.


![RGB-Bitcoin](assets/fr/020.webp)


Bu yazılım tuğlalarının Bitcoin'dan bağımsız olduğunu unutmayın; teorik olarak, başka herhangi bir yayın kanıtı ortamına (başka bir kayıt defteri, bir dergi, vb.) uygulanabilirler. Uygulamada, RGB sağlamlığı ve geniş fikir birliği için Bitcoin'ya dayanır.


![RGB-Bitcoin](assets/fr/021.webp)


### Halktan gelen sorular


#### Tek Kullanımlık Mühürlerin daha geniş kullanımına doğru


Peter Todd ayrıca _Open Timestamps_ protokolünü yaratmıştır ve Single-Use Seal konsepti bu fikirlerin doğal bir uzantısıdır. RGB'in ötesinde, _merge mining_ veya BIP300 gibi drivechain ile ilgili tekliflere başvurmadan _sidechains_ oluşturulması gibi başka kullanım durumları da öngörülebilir. Tek bir Commitment gerektiren herhangi bir sistem prensipte bu kriptografik ilkelden faydalanabilir. Bugün, RGB ilk büyük tam ölçekli uygulamadır.


#### Veri kullanılabilirliği sorunları


Client-side Validation'de her kullanıcı geçmişin kendi bölümünü sakladığından, veri kullanılabilirliği küresel olarak garanti edilmez. Bir Contract ihraççısı belirli bilgileri saklar veya iptal ederse, teklifin gerçek gelişiminden haberdar olmayabilirsiniz. Bazı durumlarda (sabit coinler gibi), ihraççının dolaşımdaki hacmi kanıtlamak için kamuya açık verileri tutması beklenir, ancak bunu yapmak için teknik bir zorunluluk yoktur. Bu nedenle, sınırsız Supply ile kasıtlı olarak opak sözleşmeler tasarlamak mümkündür, bu da güven sorularını gündeme getirir.


#### Parçalama ve Contract izolasyonu


Her bir Contract izole edilmiş bir _shard_'ı temsil eder: Örneğin USDT ve USDC geçmişlerini paylaşmak zorunda değildir. Atomik takaslar hala mümkündür, ancak bu kayıtlarının birleştirilmesini içermez. Her şey kriptografik Commitment ile, tüm geçmiş grafiğini her katılımcıya ifşa etmeden yapılır.


### Sonuç


Client-side Validation kavramının Blockchain ve _state channels_ ile nerede uyum sağladığını, dağıtık bilgi işlem trilemmalarına nasıl yanıt verdiğini ve Double-spending'den kaçınmak ve *zaman damgalama* için Bitcoin Blockchain'den nasıl benzersiz bir şekilde yararlandığını gördük. Fikir, **Single-Use Seal** kavramına dayanıyor ve istediğiniz zaman yeniden harcayamayacağınız benzersiz taahhütlerin oluşturulmasını sağlıyor. Bu şekilde, her katılımcı yalnızca kesinlikle gerekli olan geçmişi yükler, akıllı sözleşmelerin ölçeklenebilirliğini ve gizliliğini artırırken Bitcoin'in güvenliğini bir arka plan olarak korur.


Bir sonraki adım, bu Single-Use Seal mekanizmasının Bitcoin'te (UTXO'lar aracılığıyla) nasıl uygulandığını, çapaların nasıl oluşturulduğunu ve doğrulandığını ve ardından RGB'te tam akıllı sözleşmelerin nasıl oluşturulduğunu daha ayrıntılı olarak açıklamak olacaktır. Özellikle, bir Bitcoin işleminin farklı sözleşmelerdeki birden fazla durum geçişini, güvenlik açıkları veya çifte taahhütler ortaya çıkarmadan aynı anda mühürlediğini kanıtlamanın teknik zorluğu olan çoklu taahhütler konusuna bakacağız.


İkinci bölümün daha teknik ayrıntılarına girmeden önce, temel tanımları (Client-side Validation, Single-Use Seal, çapalar, vb.) tekrar okumaktan çekinmeyin ve genel mantığı aklınızda tutun: Bitcoin Blockchain'nin güçlü yönlerini (güvenlik, ademi merkeziyetçilik, zaman damgası) off-chain çözümlerinin güçlü yönleriyle (hız, gizlilik, ölçeklenebilirlik) uzlaştırmaya çalışıyoruz ve RGB ve Client-side Validation'in başarmaya çalıştığı şey tam olarak budur.


## Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


Bu bölümde, Bitcoin Blockchain içinde Client-side Validation ve Tek Kullanımlık Mühürlerin uygulanmasına bakacağız. RGB'un bir Bitcoin işleminde bir Seal tanımlamak ve kapatmak için kullandığı **TxO2** şemasına özellikle odaklanarak RGB'un **Commitment Layer** (Layer 1) ana ilkelerini sunacağız. Daha sonra, henüz ayrıntılı olarak ele alınmamış iki önemli noktayı tartışacağız:




- Belirleyici Bitcoin taahhütleri_;
- Çoklu protokol taahhütleri.


Tek bir UTXO'nin ve dolayısıyla tek bir Blockchain'in üzerine birkaç sistemi veya sözleşmeyi yerleştirmemizi sağlayan şey bu kavramların birleşimidir.


Açıklanan kriptografik işlemlerin mutlak anlamda diğer blok zincirlerine veya yayın ortamlarına uygulanabileceği unutulmamalıdır, ancak Bitcoin'ün özellikleri (ademi merkeziyetçilik, sansüre karşı direnç ve herkese açıklık açısından) onu **RGB**'ün gerektirdiği gibi gelişmiş programlanabilirlik geliştirmek için ideal bir temel haline getirmektedir.


### Bitcoin'daki Commitment şemaları ve bunların RGB tarafından kullanımı


Kursun ilk bölümünde gördüğümüz gibi, Tek kullanımlık Mühürler genel bir kavramdır: bir işlemin belirli bir konumuna bir Commitment (_commitment_) ekleme sözü veririz ve bu konum bir mesajda kapattığımız bir Seal gibi davranır. Bununla birlikte, Bitcoin Blockchain'de, bu _commitment_'ın nereye yerleştirileceğini seçmek için çeşitli seçenekler vardır.


Mantığı anlamak için temel prensibi hatırlayalım: bir _tek kullanımlık mührü_ kapatmak için, mühürlü alanı belirli bir mesaja _commitment_ ekleyerek geçiririz. Bitcoin'de bu birkaç şekilde yapılabilir:




- **Açık anahtar veya Address** kullanın


Belirli bir açık anahtarın veya Address'in _tek kullanımlık mühür_ olduğuna karar verebiliriz. Bu anahtar veya Address bir işlemde On-Chain olarak görünür görünmez, Seal'nın belirli bir mesajla kapatıldığı anlamına gelir.




- Bir **Bitcoin** işlem çıktısı kullanın


Bu, bir _tek kullanımlık mühür_ün kesin bir _çıkış noktası_ (bir txid + çıkış numarası çifti) olarak tanımlandığı anlamına gelir. Bu _çıkış noktası_ harcanır harcanmaz Seal kapatılır.


RGB üzerinde çalışırken, bu mühürleri Bitcoin üzerinde uygulamak için en az 4 farklı yol belirledik:




- Seal'yi bir genel anahtar aracılığıyla tanımlayın ve bir _output_ içinde kapatın;
- Seal'ü bir _outpoint_ ile tanımlayın ve bir _output_ ile kapatın;
- Seal'ü bir genel anahtar değeri üzerinden tanımlayın ve bir _input_ içinde kapatın;
- Seal'i bir _outpoint_ ile tanımlayın ve bir _input_ ile kapatın.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


Bu yapılandırmaların her biri hakkında ayrıntıya girmeyeceğiz, çünkü RGB'de Seal**'nın tanımı olarak **bir _çıkış noktası_ kullanmayı ve _commitment_'ı bu _çıkış noktasını_ harcayan işlemin çıktısına yerleştirmeyi seçtik. Bu nedenle, devamında aşağıdaki kavramları tanıtabiliriz:




- **"Seal Definition"**: Belirli bir _çıkış noktası_ (txid + çıkış no. ile tanımlanır);
- **Seal kapanış**: Bir _commitment_'ın bir mesaja eklendiği bu _outpoint_'i harcayan işlem.


Bu şema RGB mimarisi ile uyumluluğu nedeniyle seçilmiştir, ancak diğer yapılandırmalar farklı kullanımlar için yararlı olabilir.


"TxO2 "deki "O2" bize hem tanımlamanın hem de kapatmanın bir işlem çıktısının harcanmasına (veya yaratılmasına) dayandığını hatırlatır.


### TxO2 diyagram örneği


Bir hatırlatma olarak, bir _tek kullanımlık mühür_ tanımlamak için mutlaka bir On-Chain işlemi yayınlamak gerekmez. Örneğin Alice'ün halihazırda harcanmamış bir UTXO'e sahip olması yeterlidir. Karar verebilir: "Bu _çıkış noktası_ (zaten mevcut) artık benim Seal'ümdür". Bunu yerel olarak (_istemci tarafında_) not eder ve bu UTXO harcanana kadar Seal açık olarak kabul edilir.


![RGB-Bitcoin](assets/fr/024.webp)


Seal'yi kapatmak istediği gün (bir olayı işaret etmek veya belirli bir mesajı Anchor'ya göndermek için), bu UTXO'i yeni bir işlemde harcar (bu işlem genellikle "_witness transaction_" olarak adlandırılır (_segwit_ ile ilgisi yoktur, sadece bizim verdiğimiz terimdir). Bu yeni işlem, mesajın _commitment_'ını içerecektir.


![RGB-Bitcoin](assets/fr/025.webp)


Bu örnekte şunu unutmayın:




- Bob (veya Alice'un tam kanıtı açıklamayı seçtiği kişiler) dışında hiç kimse bu işlemde belirli bir mesajın gizli olduğunu bilmeyecektir;
- Herkes _çıkış noktasının_ harcandığını görebilir, ancak yalnızca Bob mesajın gerçekten işleme bağlı olduğunun kanıtını elinde tutar.


Bu TxO2 şemasını göstermek için, bir PGP anahtarını iptal etme mekanizması olarak bir _tek kullanımlık mühür_ kullanabiliriz. Sunucularda bir iptal sertifikası yayınlamak yerine, Alice şöyle diyebilir: "Bu Bitcoin çıktısı, eğer harcanırsa, PGP anahtarımın iptal edildiği anlamına gelir".


Bu nedenle Alice, belirli bir durum veya verinin (yalnızca kendisi tarafından bilinen) yerel olarak (istemci tarafında) ilişkilendirildiği belirli bir UTXO'e sahiptir.


Alice, Bob'a bu UTXO'in harcanması halinde belirli bir olayın gerçekleşmiş sayılacağını bildirir. Dışarıdan bakıldığında tek gördüğümüz bir Bitcoin işlemidir; ancak Bob bu harcamanın gizli bir anlamı olduğunu bilir.


![RGB-Bitcoin](assets/fr/026.webp)


Alice bu UTXO'ü harcarken, Seal'yi yeni anahtarını veya sadece eskisinin iptalini belirten bir mesajla kapatır. Bu şekilde, On-Chain'yi izleyen herkes UTXO'ün harcandığını görecektir, ancak yalnızca tam kanıta sahip olanlar bunun PGP anahtarının tam olarak iptali olduğunu bilecektir.


![RGB-Bitcoin](assets/fr/027.webp)


Bob'nın veya ilgili herhangi birinin gizli mesajı kontrol edebilmesi için Alice'in ona off-chain bilgilerini sağlaması gerekir.


![RGB-Bitcoin](assets/fr/028.webp)


Bu nedenle Alice, Bob'e aşağıdakileri sağlamalıdır:




- Mesajın kendisi (örneğin, yeni PGP anahtarı);
- Mesajın işleme dahil olduğuna dair kriptografik kanıt (_extra transaction proof_ veya _anchor_ olarak bilinir).


![RGB-Bitcoin](assets/fr/029.webp)


Üçüncü taraflar bu bilgiye sahip değildir. Sadece bir UTXO'un harcandığını görürler. Dolayısıyla gizlilik güvence altındadır.


Yapıyı netleştirmek için süreci iki işlemle özetleyelim:




- **İşlem 1**: Bu, _mühür tanımını_, yani Seal olarak hizmet verecek _çıkış noktasını_ içerir.


![RGB-Bitcoin](assets/fr/031.webp)




- **İşlem 2**: Bu _çıkış noktasını_ harcar. Bu, Seal'i kapatır ve aynı işlemde mesaja _commitment_ ekler.


![RGB-Bitcoin](assets/fr/033.webp)


Bu nedenle ikinci işleme "_tanıklık işlemi_" adını veriyoruz.


Bunu başka bir açıdan göstermek için iki katmanı temsil edebiliriz:




- **Üst Layer (Blockchain, genel)**: herkes işlemi görür ve bir *çıkış noktası* harcandığını bilir;
- **Alt Layer (istemci tarafı, özel)**: sadece Alice (veya ilgili kişi) bu masrafın kriptografik kanıt ve yerel olarak tuttuğu mesaj aracılığıyla böyle bir mesaja karşılık geldiğini bilir.


![RGB-Bitcoin](assets/fr/034.webp)


Ancak Seal'yı kapatırken, _taahhüdün_ nereye eklenmesi gerektiği sorusu ortaya çıkmaktadır.


Önceki bölümde, Client-side Validation modelinin RGB ve diğer sistemlere nasıl uygulanabileceğinden kısaca bahsettik. Burada, **deterministik Bitcoin taahhütleri** ve bunların bir işleme nasıl entegre edileceği ile ilgili kısmı ele alıyoruz. Buradaki fikir, _witness transaction_ içine neden tek bir Commitment eklemeye çalıştığımızı ve her şeyden önce açıklanmamış başka rakip taahhütlerin olmamasını nasıl sağlayacağımızı anlamaktır.


### Bir işlemdeki Commitment konumları


Birisine bir işlemde belirli bir mesajın gömülü olduğuna dair kanıt verdiğinizde, aynı işlemde size açıklanmamış başka bir Commitment (ikinci, gizli bir mesaj) olmadığını garanti edebilmeniz gerekir. Client-side Validation'nin sağlam kalabilmesi için, _tek kullanımlık mührü_ kapatan işleme tek bir _commitment_ yerleştirmek için **deterministik** bir mekanizmaya ihtiyacınız vardır.


Tanıklık işlemi_ ünlü UTXO'yı (veya _mühür tanımını_) harcar ve bu harcama Seal'in kapanmasına karşılık gelir. Teknik olarak konuşursak, her bir çıkış noktasının yalnızca bir kez harcanabileceğini biliyoruz. Bitcoin'ün çifte harcamaya karşı direncinin altında yatan şey de tam olarak budur. Ancak harcama işlemi birkaç _giriş_, birkaç _çıkış_ içerebilir veya karmaşık bir şekilde oluşturulabilir (coinjoins, Lightning channels, vb.). Bu nedenle, bu yapıda _commitment_'ın nereye yerleştirileceğini açık ve tekdüze bir şekilde tanımlamamız gerekir.


Yöntem ne olursa olsun (PkO, TxO2, vb.), _commitment_ eklenebilir:




- Bir **Giriş** aracılığıyla:
- **Sigtweak** ("Sign-to-Contract" prensibine benzer şekilde ECDSA imzasının `r` bileşenini değiştirir);
- **Witweak** (işlemin _ayrıştırılmış tanık_ verileri değiştirilir).
- Bir **Çıktı** üzerinden:
- **Keytweak** (alıcının açık anahtarı mesajla birlikte "değiştirilir");
- **Opret** (mesaj harcanamaz bir çıktı olan `OP_RETURN` içine yerleştirilir);
- **Tapret** (veya _Taptweak_), bir Taproot anahtarının komit dosyası kısmına Commitment eklemek için Taproot'e dayanır, böylece açık anahtarı deterministik olarak değiştirir.


![RGB-Bitcoin](assets/fr/035.webp)


İşte her bir yöntemin ayrıntıları:


![RGB-Bitcoin](assets/fr/038.webp)


***Sig tweak (sign-to-Contract):***


Daha önceki bir şema, _commitment_'ı gömmek için bir imzanın (ECDSA veya Schnorr) rastgele kısmından yararlanmayı içeriyordu: bu, "**Sign-to-Contract**" olarak bilinen tekniktir. Rastgele oluşturulan Nonce'ü veriyi içeren bir Hash ile değiştirirsiniz. Bu şekilde imza, işlemde herhangi bir ek alan olmadan Commitment'nizi dolaylı olarak ortaya çıkarır. Bu yaklaşımın bir dizi avantajı vardır:




- On-Chain aşırı yüklemesi yok (temel Nonce ile aynı yeri kullanıyorsunuz);
- Teorik olarak, Nonce başlangıçta rastgele bir veri olduğundan, bu oldukça ayrık olabilir.


Bununla birlikte, 2 büyük dezavantaj ortaya çıkmıştır:




- Multisig, Taproot'dan önce: birden fazla imza sahibiniz olduğunda, hangi imzanın _commitment_ taşıyacağına karar vermeniz gerekir. İmzalar farklı şekilde sıralanabilir ve bir imzacı reddederse, _commitment_ sonucu üzerindeki kontrolünüzü kaybedersiniz;
- MuSig ve paylaşılan Nonce: Schnorr Multisig (*MuSig*) ile Nonce üretimi çok partili bir algoritmadır ve Nonce'yi bireysel olarak değiştirmek neredeyse imkansız hale gelir.


Uygulamada, **sig tweak** mevcut donanım (donanım cüzdanları) ve formatlarla (Lightning, vb.) da çok uyumlu değildir. Dolayısıyla bu harika fikri uygulamaya koymak Hard'tür.


***Anahtar ayarı (Contract'e ödeme):***


**Anahtar değiştirme** tarihsel *pay-to-contract* kavramını ele alır. Açık anahtar `X`i alır ve `H(mesaj)` değerini ekleyerek değiştiririz. Spesifik olarak, eğer `X = x * G` ve `h = H(mesaj)` ise, yeni anahtar `X' = X + h * G` olacaktır. Bu değiştirilmiş anahtar **Commitment**`i `mesaj`a gizler. Orijinal özel anahtarın sahibi, `x` özel anahtarına `h` ekleyerek, çıktıyı harcayacak anahtara sahip olduğunu kanıtlayabilir. Teorik olarak bu zarif bir yöntemdir, çünkü




- _commitment_ herhangi bir ek alan eklenmeden girilir;
- Herhangi bir ek On-Chain verisi depolamazsınız.


Ancak uygulamada aşağıdaki zorluklarla karşılaşıyoruz:




- Cüzdanlar, "değiştirildiği" için artık standart açık anahtarı tanımamaktadır, bu nedenle UTXO'yi normal anahtarınızla kolayca ilişkilendiremezler;
- Donanım cüzdanları, standart türevlerinden türetilmeyen bir anahtarla imzalamak üzere tasarlanmamıştır;
- Senaryolarınızı, tanımlayıcılarınızı vb. uyarlamanız gerekir.


RGB bağlamında, bu yol 2021 yılına kadar öngörülmüştü, ancak mevcut standartlar ve altyapı ile çalışmasını sağlamak için çok karmaşık olduğu kanıtlandı.


***Tanıklık tweak:***


Inscriptions Ordinals_ gibi bazı protokollerin uygulamaya koyduğu bir başka fikir de verileri doğrudan işlemin "tanık" bölümüne yerleştirmektir (bu nedenle "tanık tweak" ifadesi kullanılır). Ancak bu yöntem:




- Etkileşimi anında görünür hale getirir (ham verileri kelimenin tam anlamıyla tanığa yapıştırırsınız);
- Sansüre tabi olabilir (madenciler veya düğümler çok büyükse veya başka bir keyfi özellik varsa aktarmayı reddedebilir);
- RGB'un gizlilik ve hafiflik hedefine aykırı olarak bloklarda yer kaplar.


Buna ek olarak, witness belirli bağlamlarda budanabilir olacak şekilde tasarlanmıştır, bu da sağlam kanıtlara sahip olmayı daha karmaşık hale getirebilir.


***Açık dönüş (opret):***


Çalışması çok basit olan bir `OP_RETURN`, bir Hash veya mesajı işlemin özel bir alanında saklamanıza olanak tanır. Ancak hemen tespit edilebilir: herkes işlemde bir _commitment_ olduğunu görür ve sansürlenebilir veya atılabilir, ayrıca ekstra çıktı eklenebilir. Bu şeffaflığı ve boyutu artırdığından, bir Client-side Validation çözümü açısından daha az tatmin edici olduğu düşünülmektedir.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


Son seçenek ise *Tapret* şeması ile **Taproot** (BIP341 ile tanıtılmıştır) kullanımıdır. *Tapret*, Blockchain üzerinde kapladığı alan ve Contract işlemleri için gizlilik açısından iyileştirmeler getiren deterministik Commitment'ün daha karmaşık bir şeklidir. Ana fikir, Commitment'ü bir [Taproot işleminin] (https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) `Script Path Spend` kısmında gizlemektir.


![RGB-Bitcoin](assets/fr/036.webp)


Commitment'in bir Taproot işlemine nasıl eklendiğini açıklamadan önce, Commitment'in **imperatif olarak** aşağıdaki gibi 64 baytlık bir dizeye [oluşturulmuş] (https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) karşılık gelmesi gereken **tam biçimine** bakalım:


```txt
64-byte_Tapret_Commitment =

OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- 29 bayt `OP_RESERVED`, ardından `OP_RETURN`, sonra `OP_PUSHBYTE_33`, 31 baytlık _prefix_ kısmını oluşturur;
- Ardından 32 baytlık bir _commitment_ (genellikle **MPC**'den Merkle Root) gelir ve buna 1 bayt **Nonce** ekleriz (bu ikinci bölüm için toplam 33 bayt).


Dolayısıyla 64 baytlık `Tapret` yöntemi, 29 baytlık `OP_RESERVED` ön ekini eklediğimiz ve Nonce olarak fazladan bir bayt eklediğimiz bir `Opret` gibi görünür.


Uygulama, gizlilik ve ölçeklendirme açısından esnekliği korumak için Tapret şeması, gereksinimlere bağlı olarak çeşitli kullanım durumlarını dikkate alır:




- Bir Tapret Commitment'ün önceden var olan bir Script Path yapısı olmadan bir Taproot işlemine benzersiz bir şekilde dahil edilmesi;
- Bir Tapret Commitment'nın zaten bir Script Path ile donatılmış bir Taproot işlemine entegrasyonu.


Şimdi bu iki senaryoya daha yakından bakalım.


#### Mevcut Senaryo Yolu olmadan Tapret kuruluşu


Bu ilk durumda, yalnızca dahili genel anahtar `P` *(Dahili Anahtar*) içeren ve ilişkili bir komut dosyası yolu (*Script Path*) bulunmayan bir Taproot çıkış anahtarı (*Taproot Çıkış Anahtarı*) `Q` ile başlarız:


![RGB-Bitcoin](assets/fr/047.webp)




- p`: _Key Path Spend_ için dahili genel anahtar.
- g`: [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1) eliptik eğrisinin üretme noktası.

-t = tH_TWEAK(P)`, [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation) uyarınca bir _etiketli hash_ (örneğin `SHA-256(SHA-256(TapTweak) || P)`) aracılığıyla hesaplanan ince ayar faktörüdür. Bu, gizli bir komut dosyası olmadığını kanıtlar.


Bir **Tapret** Commitment dahil etmek için, aşağıdaki gibi **benzersiz bir komut dosyası** ile bir **Script Path Spend** ekleyin:


![RGB-Bitcoin](assets/fr/048.webp)




- t = tH_TWEAK(P || Script_root)` daha sonra **Script_root** dahil olmak üzere yeni ince ayar faktörü haline gelir.
- script_root = tH_BRANCH(64-byte_Tapret_Commitment)` bu **script**'in kökünü temsil eder ve basitçe `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)` türünde bir Hash'tür.


Burada Taproot ağacına dahil olma ve teklik kanıtı tek bir dahili açık anahtar olan `P`ye dayanmaktadır.


#### Önceden var olan bir Script Path'e Tapret entegrasyonu


İkinci senaryo, halihazırda birkaç komut dosyası içeren daha karmaşık bir `Q` **Taproot** çıktısıyla ilgilidir. Örneğin, 3 komut dosyasından oluşan bir ağacımız var:


![RGB-Bitcoin](assets/fr/049.webp)




- tH_LEAF(x)` bir yaprak betiğin normalleştirilmiş etiketlenmiş Hash işlevini belirtir.
- a, B, C` Taproot yapısına zaten dahil olan komut dosyalarını temsil eder.


Tapret Commitment'i eklemek için, ağacın ilk seviyesine bir *harcanamaz komut dosyası* eklememiz ve mevcut komut dosyalarını bir seviye aşağı kaydırmamız gerekir. Görsel olarak ağaç şöyle olur:


![RGB-Bitcoin](assets/fr/050.webp)




- tHABC`, `A, B, C` üst düzey gruplamasının etiketlenmiş Hash'unu temsil eder.
- tHT`, 64 baytlık `Tapret`e karşılık gelen komut dosyasının Hash'unu temsil eder.


Taproot kurallarına göre, her dal/yaprak sözlüksel bir Hash sırasına göre birleştirilmelidir. İki olası durum vardır:




- **tHT` > `tHABC`**: Tapret Commitment ağacın sağına doğru hareket eder. Teklik kanıtı sadece `tHABC` ve `P` gerektirir;
- **tHT` < `tHABC`**: Tapret Commitment sol tarafa yerleştirilmiştir. Sağda başka bir Tapret Commitment olmadığını kanıtlamak için, `tHAB` ve `tHC` böyle başka bir yazının olmadığını göstermek için ortaya çıkarılmalıdır.


İlk durum için görsel örnek (`tHABC < tHT`):


![RGB-Bitcoin](assets/fr/051.webp)


İkinci durum için örnek (`tHABC > tHT`):


![RGB-Bitcoin](assets/fr/052.webp)


#### Nonce ile Optimizasyon


Gizliliği artırmak için `<Nonce>` değerini (64 baytlık `Tapret`in son baytı) `tHABC < tHT` olacak şekilde bir Hash `tHT` elde etmek amacıyla "mayınlayabiliriz" (daha doğru bir terim "bruteforcing" olacaktır). Bu durumda, Commitment sağ tarafa yerleştirilir ve kullanıcıyı Tapret'in benzersizliğini kanıtlamak için mevcut komut dosyalarının tüm içeriğini ifşa etmek zorunda bırakmaz.


Özetle, `Tapret`, RGB'ün Client-side Validation ve Single-Use Seal mantığı için gerekli olan teklik ve belirsizlik gereksinimine saygı gösterirken, bir Commitment'i bir Taproot işlemine dahil etmenin ayrı ve deterministik bir yolunu sunar.


#### Geçerli çıkışlar


RGB Commitment işlemleri için, geçerli bir Bitcoin Commitment şeması için temel gereklilik aşağıdaki gibidir: İşlem (*Witness Transaction*) kanıtlanabilir bir şekilde tek bir Commitment içermelidir. Bu gereklilik, aynı işlem içinde istemci tarafında doğrulanmış veriler için alternatif bir geçmiş oluşturmayı imkansız hale getirir. Bu, _single-use seal_'in etrafında kapandığı mesajın benzersiz olduğu anlamına gelir.


Bu ilkeyi yerine getirmek için ve bir işlemdeki çıkış sayısına bakılmaksızın, **bir ve yalnızca bir çıkışın** bir Commitment içerebilmesini şart koşuyoruz. Kullanılan şemaların her biri için (*Opret* veya *Tapret*), bir RGB _commitment_ içerebilecek tek geçerli çıktılar şunlardır:




- Opret şeması için ilk çıktı `OP_RETURN` (mevcutsa);
- **Taproot** şeması için ilk Taproot çıktısı (mevcutsa).


Bir işlemin iki ayrı çıktıda tek bir `Opret` Commitment ve tek bir `Tapret` Commitment içermesinin oldukça mümkün olduğunu unutmayın. Seal Definition'nin deterministik yapısı sayesinde, bu iki taahhüt istemci tarafında doğrulanan iki farklı veri parçasına karşılık gelir.


### RGB'te analiz ve pratik seçimler


RGB'i başlattığımızda, bir _commitment_'ın deterministik bir şekilde bir işlemde nereye ve nasıl yerleştirileceğini belirlemek için tüm bu yöntemleri gözden geçirdik. Bazı kriterler tanımladık:




- Farklı senaryolarla uyumluluk (örn. Multisig, Lightning, donanım cüzdanları vb.);
- On-Chain alanı üzerindeki etkisi;
- Uygulama ve bakım zorluğu;
- Gizlilik ve sansüre karşı direnç.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






Çalışma sırasında, Commitment şemalarının hiçbirinin mevcut Lightning standardıyla (Taproot, _muSig2_ veya ek _commitment_ desteği kullanmayan) tam olarak uyumlu olmadığı anlaşılmıştır. Lightning'in kanal yapısını (*BiFrost*) RGB taahhütlerinin eklenmesine izin verecek şekilde değiştirme çabaları devam etmektedir. Bu, işlem yapısını, anahtarları ve kanal güncellemelerinin imzalanma şeklini gözden geçirmemiz gereken başka bir alandır.


Analiz, aslında, diğer yöntemlerin (key tweak, sig tweak, witness tweak, vb.) başka komplikasyon biçimleri sunduğunu göstermiştir:




- Ya büyük bir On-Chain hacmimiz var;
- Ya mevcut Wallet kodu ile radikal bir uyumsuzluk vardır;
- Ya çözüm, işbirliği yapmayan Multisig'te uygulanabilir değildir.


RGB için özellikle iki yöntem öne çıkmaktadır: *her ikisi de "İşlem Çıkışı" olarak sınıflandırılan ve protokol tarafından kullanılan TxO2 moduyla uyumlu olan **Opret*** ve ***Tapret***.


### Çoklu Protokol Taahhütleri - MPC


Bu bölümde, **RGB**'nin, bir Bitcoin işleminde kaydedilen tek bir Commitment (*Commitment*) içindeki birden fazla sözleşmenin (veya daha doğrusu bunların _geçiş demetlerinin_) deterministik bir şema aracılığıyla (`Opret` veya `Tapret`e göre) nasıl toplandığını ele alıyoruz. Bunu başarmak için, çeşitli sözleşmelerin Merkelizasyon sırası **MPC Ağacı** (_Multi Protocol Commitment Tree_) adı verilen bir yapıda gerçekleşir. Bu bölümde, bu MPC Ağacının yapısına, kökünün nasıl elde edileceğine ve birden fazla sözleşmenin aynı işlemi gizli ve açık bir şekilde nasıl paylaşabileceğine bakacağız.


Multi Protocol Commitment (MPC) iki ihtiyacı karşılamak üzere tasarlanmıştır:




- Mpc::Commitment` Hash'nin oluşturulması: bu, bir `Opret` veya `Tapret` şemasına göre Bitcoin Blockchain'a dahil edilecektir ve doğrulanacak tüm durum değişikliklerini yansıtmalıdır;
- Birden fazla sözleşmenin tek bir _commitment_ içinde eşzamanlı olarak depolanması, birden fazla varlık veya RGB sözleşmesi üzerindeki ayrı güncellemelerin tek bir Bitcoin işleminde yönetilmesini sağlar.


Somut olarak, her _geçiş demeti_ belirli bir Contract'ya aittir. Tüm bu bilgiler, kökü (`mpc::Root`) daha sonra `mpc::Commitment`i vermek için tekrar hash edilen bir **MPC Ağacı** içine yerleştirilir. Seçilen deterministik yönteme göre Bitcoin işlemine (_witness transaction_) yerleştirilen bu son Hash'dir.


![RGB-Bitcoin](assets/fr/042.webp)


#### MPC Kök Hash


Gerçekte On-Chain olarak yazılan değer (`Opret` veya `Tapret` içinde) `mpc::Commitment` olarak adlandırılır. Bu, formüle göre [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) şeklinde hesaplanır:


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


nerede?




- mpc_tag` bir etikettir: urn:ubideco:mpc:Commitment#2024-01-31`, [RGB etiketleme kurallarına] göre seçilmiştir (https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- `depth` (1 bayt) *MPC Ağacının* derinliğini gösterir;
- cofactor` (16 bit, Little Endian) ağaçtaki her bir Contract'e atanan konumların benzersizliğini desteklemek için kullanılan bir parametredir;
- `mpc::Root`, bir sonraki bölümde açıklanan işleme göre hesaplanan *MPC Ağacı*'nın köküdür.


![RGB-Bitcoin](assets/fr/044.webp)


#### MPC Ağaç yapımı


Bu MPC Ağacını oluşturmak için, her bir Contract'nın benzersiz bir yaprak konumuna karşılık gelmesini sağlamamız gerekir. Diyelim ki elimizde:




- c` sözleşmeleri `i` = {0,1,...,C-1} içinde `i` tarafından indekslenerek dahil edilecektir;
- Her Contract `c_i` için bir `ContractId(i) = c_i` tanımlayıcımız vardır.


Daha sonra `w` genişliğinde ve `d` derinliğinde bir ağaç oluşturuyoruz, öyle ki `2^d = w`, `w > C`, böylece her Contract ayrı bir _leaf_ içine yerleştirilebilir. Ağaçtaki her bir Contract'in pozisyonu `pos(c_i)` ile belirlenir:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


burada `kofaktör` her bir Contract için farklı pozisyonlar elde etme olasılığını artıran bir tamsayıdır. Uygulamada, yapı yinelemeli bir süreç izlemektedir:




- Minimum derinlikten başlıyoruz (tam sözleşme sayısını gizlemek için geleneksel olarak `d=3`);
- Farklı `kofaktörler` deniyoruz (performans nedenleriyle `w/2`ye kadar veya maksimum 500);
- Tüm sözleşmeleri çarpışma olmadan konumlandıramazsak, `d` değerini artırır ve yeniden başlarız.


Amaç, çarpışma riskini minimumda tutarken çok uzun ağaçlardan kaçınmaktır. Çarpışma olgusunun [Yıldönümü Paradoksu] (https://en.wikipedia.org/wiki/Birthday_problem) ile bağlantılı rastgele bir dağılım mantığı izlediğini unutmayın.


#### Yerleşik yapraklar


I = {0,1,...,C-1} sözleşmeleri için `C` farklı pozisyon `pos(c_i)` elde edildikten sonra, her sayfa bir Hash fonksiyonu (*etiketli Hash*) ile doldurulur:


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


nerede?




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, her zaman RGB'in Merkle kurallarına göre seçilir;
- 0x10` bir _sözleşme yaprağını_ tanımlar;
- `c_i` 32 baytlık Contract tanımlayıcısıdır (Genesis Hash'ten türetilmiştir);
- bundleId(c_i)`, `c_i` ile ilgili `Durum Geçişleri` kümesini tanımlayan 32 baytlık bir Hash'dır (bir *Transition Bundle* içinde toplanmıştır).


#### Issız yapraklar


Bir Contract'ye atanmamış kalan yapraklar (yani `w - C` yaprakları), "kukla" bir değerle (_entropi yaprağı_) doldurulur:


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


nerede?




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, her zaman RGB'in Merkle kurallarına göre seçilir;
- 0x11` bir _entropi yaprağını_ belirtir;
- entropi`, ağacı oluşturan kişi tarafından seçilen 64 baytlık rastgele bir değerdir;
- j` bu yaprağın ağaçtaki konumudur (32 bitlik Little Endian cinsinden).


#### MPC düğümleri


W` yapraklarını oluşturduktan sonra (yerleşik olsun ya da olmasın), merkelizasyona geçiyoruz. Herhangi bir iç düğüm aşağıdaki gibi karma hale getirilir:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


nerede?




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, her zaman RGB'un Merkle kurallarına göre seçilir;
- b` _branching faktörüdür_ (8 bit). Çoğu zaman `b=0x02` olur çünkü ağaç ikili ve tamdır;
- d` ağaçtaki düğümün derinliğidir;
- w` ağaç genişliğidir (256 bitlik Little Endian ikilisinde);
- tH1` ve `tH2`, yukarıda gösterildiği gibi hesaplanmış olan alt düğümlerin (veya yaprakların) hash'leridir.


Bu şekilde ilerleyerek `mpc::Root` kökünü elde ederiz. Daha sonra `mpc::Commitment`ü hesaplayabiliriz (yukarıda açıklandığı gibi) ve On-Chain'i ekleyebiliriz.


Bunu göstermek için, `C=3` (üç sözleşme) olan bir örnek hayal edelim. Konumlarının `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2` olduğu varsayılır. Diğer yapraklar (0, 1, 3, 5, 6 konumları) _entropi yaprakları_dır. Aşağıdaki diyagram ile köke giden hash dizisi gösterilmektedir:




- bundleId(c_i)`yi temsil eden `BUNDLE_i`;
- tH_MPC_LEAF(A)` vb. yaprakları temsil eder (bazıları sözleşmeler için, diğerleri entropi için);
- Her dal `tH_MPC_BRANCH(...)` iki alt dalının hash'lerini birleştirir.


Nihai sonuç **mpc::Root**, ardından `mpc::Commitment`dir.


![RGB-Bitcoin](assets/fr/053.webp)


#### MPC şaft kontrolü


Bir doğrulayıcı bir `c_i` Contract`ün (ve onun `BundleId`sinin) nihai `mpc::Commitment`e dahil edildiğinden emin olmak istediğinde, basitçe bir Merkle kanıtı alır. Bu kanıt, yaprakları (bu durumda, `c_i`nin _contract yaprağı_) köke kadar izlemek için gereken düğümleri gösterir. Tüm *MPC Ağacını* ifşa etmeye gerek yoktur: bu, diğer sözleşmelerin gizliliğini korur.


Örnekte, bir `c_2` doğrulayıcısı yalnızca bir ara Hash (`tH_MPC_LEAF(D)`), iki `tH_MPC_BRANCH(...)`, `pos(c_2)` konum kanıtı ve `cofactor` değerine ihtiyaç duyar. Daha sonra kökü yerel olarak yeniden yapılandırabilir, ardından `mpc::Commitment`i yeniden hesaplayabilir ve Bitcoin işleminde yazılanla karşılaştırabilir (`Opret` veya `Tapret` içinde).


![RGB-Bitcoin](assets/fr/054.webp)


Bu mekanizma şunları sağlar:




- C_2` ile ilgili durum gerçekten de toplam bilgi bloğuna dahil edilmiştir (istemci tarafı);
- Hiç kimse aynı işlemle alternatif bir geçmiş oluşturamaz, çünkü On-Chain _commitment_ tek bir MPC köküne işaret eder.


#### PPK yapısının özeti


Multi Protocol Commitment (MPC), RGB'nin birden fazla sözleşmeyi tek bir Bitcoin işleminde toplamasını ve diğer katılımcılara karşı taahhütlerin benzersizliğini ve gizliliğini korumasını sağlayan ilkedir. Ağacın deterministik yapısı sayesinde, her bir Contract benzersiz bir konuma atanır ve "kukla" yaprakların (**Entropi Yaprakları**) varlığı, işleme katılan toplam sözleşme sayısını kısmen maskeler.


Merkle Tree'ün tamamı asla istemcide saklanmaz. Biz sadece ilgili her Contract için alıcıya iletilmek üzere (daha sonra Commitment'ü doğrulayabilecek olan) bir _Merkle yolu_ generate oluştururuz. Bazı durumlarda, aynı UTXO'den geçen birkaç varlığınız olabilir. Daha sonra çok fazla verinin tekrarlanmasını önlemek için birkaç _Merkle yolunu_ çoklu protokol Commitment bloğu_ olarak adlandırılan bir blokta birleştirebilirsiniz.


Bu nedenle her _Merkle kanıtı_ hafiftir, özellikle de RGB'de ağaç derinliği 32'yi geçmeyeceği için. Ayrıca, birkaç dalı birleştirmek veya ayırmak için yararlı olan daha fazla bilgiyi (kesit, entropi vb.) koruyan bir "Merkle bloğu" kavramı da vardır.


RGB'i sonuçlandırmak bu yüzden bu kadar uzun sürdü. Genel vizyonumuz 2019'dan beri vardı: her şeyi istemci tarafına koymak, off-chain tokenlerini dolaşıma sokmak. Ancak birden fazla sözleşme için parçalama, Merkle Tree'un yapısı, çarpışmaların ve birleştirme kanıtlarının nasıl ele alınacağı gibi ayrıntılar için... tüm bunlar yinelemeler gerektirdi.


### Ankrajlar: küresel bir montaj


Taahhütlerimizin (`Opret` veya `Tapret`) ve MPC'mizin (*Multi Protocol Commitment*) oluşturulmasının ardından, RGB protokolünde **Anchor** kavramını Address yapmamız gerekir. Bir Anchor, bir Bitcoin Commitment'ün aslında belirli sözleşme bilgilerini içerdiğini doğrulamak için gereken Elements'ü bir araya getiren istemci tarafı onaylı bir yapıdır. Başka bir deyişle, bir Anchor yukarıda açıklanan _commitments_'ı doğrulamak için gereken tüm verileri özetler.


Bir Anchor üç sıralı alandan oluşur:




- `txid`
- `MPC Kanıtı`
- ekstra İşlem Kanıtı - ETP


Bu alanların her biri, ister altta yatan Bitcoin işleminin yeniden yapılandırılması ister gizli bir Commitment'in varlığının kanıtlanması (özellikle `Tapret` durumunda) olsun, doğrulama sürecinde bir rol oynar.


#### txid


txid alanı, `Opret` veya `Tapret` Commitment'ü içeren Bitcoin işleminin 32 baytlık tanımlayıcısına karşılık gelir.


Teorik olarak, Tek Kullanımlık Mühürlerin mantığını izleyerek, her bir Witness Transaction'ye işaret eden durum geçişleri zincirini takip ederek bu `txid'ı bulmak mümkün olacaktır. Ancak, doğrulamayı kolaylaştırmak ve hızlandırmak için, bu `txid` basitçe Anchor'a dahil edilir, böylece doğrulayıcıyı tüm off-chain geçmişine geri dönmek zorunda bırakmaz.


#### MPC Kanıtı


İkinci alan, `MPC Kanıtı`, bu belirli Contract'in (örneğin `c_i`) _Çoklu Protokol Taahhüdüne_ dahil edildiğinin kanıtını ifade eder. Bu şunların bir kombinasyonudur:




- `pos_i`, bu Contract'nin MPC ağacındaki konumu;
- kofaktör`, konum çakışmalarını çözmek için tanımlanan değer;
- merkle Kanıtı, yani MPC kökünü yeniden yapılandırmak ve Contract tanımlayıcısının ve `Transition Bundle`ün köke bağlı olduğunu doğrulamak için kullanılan düğümler ve karmalar kümesi.


Bu mekanizma, her bir Contract'in sayesinde benzersiz bir yaprak elde ettiği *MPC Ağacının* oluşturulmasıyla ilgili önceki bölümde açıklanmıştır:


```txt
pos(c_i) = c_i mod (w - cofactor)
```


Ardından, tüm yaprakları (sözleşmeler + entropi) toplamak için deterministik bir merkelizasyon şeması kullanılır. Sonunda, `MPC Proof` kökün yerel olarak yeniden yapılandırılmasına ve On-Chain dahil `mpc::Commitment` ile karşılaştırılmasına izin verir.


#### Ekstra İşlem Kanıtı - ETP


Üçüncü alan olan **ETP**, kullanılan Commitment tipine bağlıdır. Eğer Commitment `Opret` tipindeyse, ek bir kanıt gerekmez. Doğrulayıcı, işlemin ilk `OP_RETURN` çıktısını inceler ve `mpc::Commitment`i doğrudan orada bulur.


**Commitment `Tapret`** tipindeyse, *Ekstra İşlem Kanıtı - ETP* adı verilen ek bir kanıt sağlanmalıdır. Bu kanıt şunları içerir:




- *Commitment*'in gömülü olduğu Taproot çıktısının dahili genel anahtarı (`P`);
- Bu senaryonun Taproot ağacındaki tam yerini kanıtlamak için `Script Path Spend`in ortak düğümleri (Tapret *Commitment* bir senaryoya eklendiğinde):
 - Eğer `Tapret` *Commitment* sağ kolda ise, sol kol düğümünü (örneğin `tHABC`) ortaya çıkarırız,
 - Eğer `Tapret` *Commitment* soldaysa, sağ tarafta başka *Commitment* olmadığını kanıtlamak için 2 düğümü (örneğin `tHAB` ve `tHC`) ifşa etmeniz gerekir.
- Nonce`, *Commitment*'nin ağacın sağına yerleştirilmesine izin vererek (kanıt optimizasyonu) en iyi yapılandırmayı "çıkarmak" için kullanılabilir.


Bu ek kanıt çok önemlidir çünkü `Opret`in aksine `Tapret` Commitment, *Commitment*'un konumunu doğru bir şekilde doğrulamak için Taproot ağacının bir kısmının ortaya çıkarılmasını gerektiren bir Taproot betiğinin yapısına entegre edilmiştir.


![RGB-Bitcoin](assets/fr/045.webp)


Bu nedenle **Anchor`lar** RGB bağlamında bir Bitcoin Commitment`i doğrulamak için gereken tüm bilgileri kapsüller. Hem ilgili işlemi (`txid`) hem de Contract konumlandırma kanıtını (`MPC Kanıtı`) belirtirken, `Tapret` durumunda ek kanıtı (`ETP`) yönetirler. Bu şekilde bir Anchor, aynı işlemin diğer sözleşme verileri için yeniden yorumlanamamasını sağlayarak off-chain durumunun bütünlüğünü ve benzersizliğini korur.


### Sonuç


Bu bölümde şunları ele aldık:




- Bitcoin'de Tek Kullanımlık Mühürler konsepti nasıl uygulanır (özellikle bir _outpoint_ aracılığıyla);
- Bir _commitment_'ı bir işleme deterministik olarak eklemek için çeşitli yöntemler (Sig tweak, Key tweak, witness tweak, OP_RETURN, Taproot/Tapret);
- RGB'in Tapret taahhütlerine odaklanmasının nedenleri;
- Belirli bir noktayı kanıtlamak istediğinizde tüm bir durumu veya diğer sözleşmeleri ifşa etmek istemiyorsanız gerekli olan _multi-protocol commitments_ aracılığıyla çoklu Contract yönetimi;
- Ayrıca, her şeyi (txid, Merkle Tree proof ve Taproot proof işlemleri) tek bir pakette bir araya getiren _Anchors_'un rolünü de gördük.


Uygulamada, teknik uygulama birkaç özel Rust _crates_ arasında bölünmüştür (_client_side_validation_, _commit-verify_, _bp_core_, vb. içinde). Temel kavramlar oradadır:


![RGB-Bitcoin](assets/fr/046.webp)


Bir sonraki bölümde, RGB'in tamamen off-chain bileşenine, yani Contract mantığına bakacağız. Kısmen çoğaltılmış _sonsuz durum makineleri_ olarak düzenlenen RGB sözleşmelerinin, verilerinin gizliliğini korurken Bitcoin komut dosyalarından çok daha yüksek ifade gücüne nasıl ulaştığını göreceğiz.


## Akıllı sözleşmelere ve durumlarına giriş


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


Bu ve bir sonraki bölümde, RGB ortamında **Smart contract** kavramına bakacağız ve bu sözleşmelerin *durumlarını* tanımlayabilecekleri ve geliştirebilecekleri farklı yolları keşfedeceğiz. RGB mimarisinin, Tek Kullanımlık Mühürlerin sıralı dizisini kullanarak, çeşitli ***Contract İşlemlerini*** ölçeklenebilir bir şekilde ve merkezi bir kayıt defterinden geçmeden yürütmeyi neden mümkün kıldığını göreceğiz. Ayrıca ***Business Logic***'in Contract State'nin evrimini çerçevelemedeki temel rolüne de bakacağız.


### Akıllı sözleşmeler ve dijital taşıyıcı hakları


RGB'un amacı, Bitcoin üzerinde akıllı sözleşmelerin uygulanması için bir altyapı sağlamaktır. "Smart contract" ile birkaç taraf arasında, maddeleri uygulamak için insan müdahalesi olmaksızın otomatik ve hesaplamalı olarak uygulanan bir anlaşmayı kastediyoruz. Başka bir deyişle, Contract'nin yasası güvenilir bir üçüncü tarafça değil, yazılım tarafından uygulanır.


Bu otomasyon, ademi merkeziyetçilik sorusunu gündeme getirmektedir: Ownership ve Contract performansını yönetmek için kendimizi merkezi bir kayıttan (örneğin merkezi bir platform veya veritabanı) nasıl kurtarabiliriz? RGB tarafından ele alınan orijinal fikir, "hamiline enstrümanlar" olarak bilinen bir Ownership moduna geri dönmektir. Tarihsel olarak, belirli menkul kıymetler (tahviller, hisseler, vb.) hamiline yazılı olarak ihraç edilmiş ve belgeye fiziksel olarak sahip olan herkesin haklarını kullanmasına olanak sağlamıştır.


![RGB-Bitcoin](assets/fr/055.webp)


RGB bu kavramı dijital dünyaya uygular: haklar (ve yükümlülükler) off-chain manipüle edilen verilerde kapsüllenir ve bu verilerin durumu katılımcıların kendileri tarafından doğrulanır. Bu, a priori olarak, kamu kayıtlarına dayalı diğer yaklaşımların sunduğundan çok daha büyük bir gizlilik ve bağımsızlık derecesi sağlar.


### Smart contract'e giriş RGB durumu


Smart contract'deki bir RGB, tarafından tanımlanan bir durum makinesi olarak görülebilir:




- Bir **Durum**, yani Contract'un mevcut yapılandırmasını yansıtan bilgi kümesi;
- Durumun hangi koşullar altında ve kim tarafından değiştirilebileceğini açıklayan bir **Business Logic** (kurallar dizisi).


![RGB-Bitcoin](assets/fr/056.webp)


Bu sözleşmelerin tokenların basit bir şekilde transfer edilmesiyle sınırlı olmadığını anlamak önemlidir. Geleneksel varlıklardan (tokenlar, hisse senetleri, tahviller) daha karmaşık mekaniklere (kullanım hakları, ticari şartlar vb.) kadar çok çeşitli uygulamaları içerebilirler. Contract kodunun herkes tarafından erişilebilir ve çalıştırılabilir olduğu diğer blok zincirlerinin aksine, RGB'nin yaklaşımı Contract'e erişimi ve Contract hakkındaki bilgiyi katılımcılara ("***Contract katılımcıları***") ayırır. Birkaç rol vardır:




- Contract'ün Genesis'ünü ve başlangıç değişkenlerini tanımlayan **Contract'ün düzenleyicisi** veya yaratıcısı;
- **Hak sahibi taraflar** (*Ownership*) veya diğer yaptırım kabiliyetleri;
- **Gözlemciler**, potansiyel olarak belirli bilgileri görmekle sınırlıdır, ancak değişiklikleri tetikleyemezler.


Rollerin bu şekilde ayrılması, yalnızca yetkili kişilerin sözleşme durumuyla etkileşime girebilmesini sağlayarak sansüre karşı dirence katkıda bulunur. Aynı zamanda RGB'e yatay olarak ölçeklendirme yeteneği kazandırır: doğrulamaların çoğu Blockchain'nın dışında gerçekleşir ve Bitcoin'ye yalnızca kriptografik çapalar (*taahhütler*) yazılır.


### RGB'da Durum ve Business Logic


Pratik bir bakış açısından, Contract'nin **Business Logic**'i, RGB'ün **Schema** olarak adlandırdığı şekilde tanımlanan kurallar ve komut dosyaları biçimini alır. Schema kodlar:




- Devlet yapısı (hangi alanlar kamuya açık? Hangi alanlar hangi taraflara aittir?
- Geçerlilik koşulları (bir durum güncellemesine izin vermeden önce ne kontrol edilmelidir?);
- Yetkiler (kim *State Transition* başlatabilir? Kim sadece gözlemleyebilir?).


Aynı zamanda, **Contract State** genellikle iki bileşene ayrılır:




- A **Global State**: genel bölüm, potansiyel olarak herkes tarafından gözlemlenebilir (yapılandırmaya bağlı olarak);
- **Sahipli Durumlar**: Contract mantığında referans verilen UTXO'lar aracılığıyla özellikle sahiplere tahsis edilen özel parçalar.


İlerleyen bölümlerde göreceğimiz gibi, herhangi bir durum güncellemesinin (*Contract Operation*) geçerli sayılabilmesi için bir Bitcoin _commitment_ (`Opret` veya `Tapret` aracılığıyla) ile kenetlenmesi ve *Business Logic* komut dosyalarına uyması gerekir.


### Contract Operasyonlar: Devletin oluşumu ve evrimi


RGB evreninde bir ***Contract Operation***, Contract'ü **eski bir durumdan** **yeni bir duruma** değiştiren herhangi bir olaydır. Bu işlemler aşağıdaki mantığı izler:




- Contract'nın mevcut durumunu not ediyoruz;
- Kuralı veya işlemi uygularız (bir ***State Transition***, ilk durumsa bir ***Genesis*** veya yeniden tetiklenecek genel bir *Valency* varsa bir ***State Extension***);
- Değişikliği Anchor'de yeni bir _commitment_ ile Blockchain'de yapıyoruz, bir _single-use seal_'i kapatıp başka bir tane oluşturuyoruz;
- İlgili hak sahipleri, geçişin *Schema* ile uyumlu olduğunu ve ilgili Bitcoin işleminin kayıtlı On-Chain olduğunu yerel olarak (*istemci tarafı*) doğrular.


![RGB-Bitcoin](assets/fr/057.webp)


Sonuç, artık farklı bir duruma sahip güncellenmiş bir Contract'dir. Blockchain'de yalnızca küçük bir kriptografik parmak izi (_commitment_) kaydedildiğinden, bu geçiş tüm Bitcoin ağının ayrıntılarla ilgilenmesini gerektirmez. Tek kullanımlık Mühürler dizisi herhangi bir Double-spending veya Durumun çift kullanımını önler.


### Operasyon zinciri: Genesis'tan Terminal State'e


Bunu bir perspektife oturtmak gerekirse, bir RGB Smart contract ilk durum olan **Genesis** ile başlar. Daha sonra, çeşitli Contract İşlemleri birbirini takip ederek bir DAG (*Directed Acyclic Graph*) işlemi oluşturur:




- Her geçiş bir önceki duruma (veya yakınsak geçişler söz konusu olduğunda birkaç duruma) dayanır;
- Kronolojik sıra, her bir geçişin Bitcoin Anchor'e dahil edilmesiyle garanti altına alınır, zaman damgalıdır ve Proof-of-Work tarafından mutabakat sayesinde değiştirilemez;
- Devam eden başka bir işlem olmadığında, **Terminal Durumuna** ulaşılır: Contract'un en son ve eksiksiz durumu.


![RGB-Bitcoin](assets/fr/012.webp)


Bu DAG topolojisi (basit bir doğrusal zincir yerine), birbirleriyle çelişmedikleri sürece Contract'nin farklı bölümlerinin paralel olarak gelişebilme olasılığını yansıtmaktadır. RGB daha sonra ilgili her katılımcının *istemci tarafı* doğrulamasıyla herhangi bir tutarsızlığı önlemeye özen gösterir.


### Özet


RGB'teki akıllı sözleşmeler, merkezi olmayan ancak zaman damgası ve işlem sırasını garanti altına almak için Bitcoin'ye bağlı bir dijital taşıyıcı araç modeli sunar. Bu sözleşmelerin otomatik olarak yürütülmesi aşağıdakilere dayanmaktadır:




- Bir **Contract State**, Contract'in mevcut yapılandırmasını gösterir (haklar, bakiyeler, değişkenler, vb.);
- Hangi geçişlere izin verildiğini ve bunların nasıl doğrulanması gerektiğini tanımlayan bir **Business Logic** (*Schema*);
- **Contract İşlemleri**, Bitcoin işlemlerine bağlı taahhütler sayesinde bu durumu adım adım günceller.


Bir sonraki bölümde, bu ***durumların*** ve ***durum geçişlerinin*** off-chain düzeyinde somut temsili ve bunların Bitcoin'de gömülü olan UTXO'lar ve Tek Kullanımlık Mühürler ile nasıl ilişkili olduğu hakkında daha fazla ayrıntıya gireceğiz. Bu, RGB'ün Client-side Validation'a dayanan iç mekaniğinin, veri gizliliğini korurken akıllı sözleşmelerin tutarlılığını nasıl koruduğunu görmek için bir fırsat olacaktır.


## RGB Contract operasyonları


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


Bu bölümde, yine RGB protokolü dahilinde akıllı sözleşmelerdeki işlemlerin ve durum geçişlerinin nasıl çalıştığına bakacağız. Amaç aynı zamanda birkaç katılımcının bir varlığın Ownership transferini gerçekleştirmek için nasıl işbirliği yaptığını anlamak olacaktır.


### Durum geçişleri ve mekaniği


Genel prensip hala Client-side Validation'de olduğu gibidir; burada durum verileri mal sahibi tarafından tutulur ve alıcı tarafından doğrulanır. Bununla birlikte, burada RGB ile olan özgüllük, alıcı olarak Bob'in, UTXO'larından birine gizli bir referans yoluyla, alınan varlık üzerinde gerçek kontrole sahip olmak için Alice'ten Contract verilerine belirli bilgileri dahil etmesini istemesi gerçeğinde yatmaktadır.


Bir *State Transition* (RGB'deki temel ***Contract İşlemlerinden*** biridir) sürecini göstermek için, Alice ve Bob arasındaki bir varlık transferinin adım adım bir örneğini ele alalım:


**İlk durum:**


Alice'da yerel olarak doğrulanmış verilerden (*istemci tarafı*) oluşan bir ***Stash RGB*** vardır. Bu Stash, Bitcoin üzerindeki UTXO'larından birine işaret etmektedir. Bu, bu verilerdeki bir _seal tanımının_ Alice'a ait bir UTXO'e işaret ettiği anlamına gelir. Buradaki fikir, bir varlıkla bağlantılı belirli dijital hakları (örneğin RGB jetonları) Bob'ye aktarmasını sağlamaktır.


![RGB-Bitcoin](assets/fr/058.webp)


**Bob ayrıca UTXO'lara sahiptir:**


Öte yandan Bob'in kendine ait en az bir UTXO'ı vardır ve Alice'unkiyle doğrudan bağlantısı yoktur. Bob'in UTXO'ı olmaması durumunda, *Witness Transaction*'in kendisini kullanarak ona transfer yapmak hala mümkündür: bu işlemin çıktısı daha sonra Commitment'yı (_commitment_) içerecek ve yeni Contract'in Ownership'sini Bob ile dolaylı olarak ilişkilendirecektir.


![RGB-Bitcoin](assets/fr/059.webp)


**Yeni mülkün inşası (*Yeni Durum*):**


Bob, Alice'ya bir ***Invoice*** şeklinde kodlanmış bilgi göndererek (ilerleyen bölümlerde Invoice yapımı hakkında daha ayrıntılı bilgi vereceğiz) Contract'ün kurallarına uygun yeni bir durum oluşturmasını ister. Bu durum, Bob'nin UTXO'larından birine işaret eden yeni bir *Seal Definition* içerecektir. Bu şekilde, Bob'ye bu yeni durumda tanımlanan varlıklardan Ownership verilir, örneğin belirli bir miktar RGB jetonu.


![RGB-Bitcoin](assets/fr/060.webp)


**Örnek işlemin hazırlanması:**


Alice daha sonra bir önceki Seal'te referans verilen UTXO'ü harcayan bir Bitcoin işlemi oluşturur (onu sahibi olarak meşrulaştıran işlem). Bu işlemin çıktısında, bir *Commitment* (`Opret` veya `Tapret` aracılığıyla) yeni RGB durumunu Anchor'e eklenir. Opret` veya `Tapret` taahhütleri, farklı sözleşmelerden birkaç geçişi bir araya getirebilen bir *MPC ağacından* (önceki bölümlerde görüldüğü gibi) türetilir.


**Consignment'nın Bob'ye aktarımı:**


İşlemi yayınlamadan önce Alice, Bob'e gerekli tüm *istemci tarafı* verilerini (kendi *Stash*) ve Bob'in lehine olan yeni durum bilgilerini içeren bir ***Consignment*** gönderir. Bu noktada Bob, RGB mutabakat kurallarını uygular:




- Varlığın Ownership'ünü veren yeni durum da dahil olmak üzere *Consignment* içinde bulunan tüm RGB verilerini doğrular;
- Consignment'da bulunan *Anchors*'a dayanarak, tanık işlemlerinin kronolojisini (Genesis'den en son geçişe kadar) doğrular ve Blockchain'deki ilgili taahhütleri onaylar.


**Geçişin tamamlanması:**


Bob tatmin olursa, onayını verebilir (örneğin, *Consignment*'yi imzalayarak). Alice daha sonra hazırlanan örnek işlemi yayınlayabilir. Onaylandıktan sonra, bu daha önce Alice tarafından tutulan Seal'ü kapatır ve Ownership'i Bob tarafından resmileştirir. Anti-Double-spending güvenliği daha sonra Bitcoin'deki ile aynı mekanizmaya dayanır: UTXO harcanır ve Alice'ün artık onu yeniden kullanamayacağı kanıtlanır.


![RGB-Bitcoin](assets/fr/061.webp)


Yeni durum artık Bob'in UTXO'una atıfta bulunarak Bob'e daha önce Alice tarafından tutulan Ownership'yi verir. RGB verilerinin sabitlendiği Bitcoin çıktısı, Ownership'nin transferinin geri alınamaz kanıtı haline gelir.


İki Contract işlemi (bir **Genesis** ve ardından bir ***State Transition***) içeren minimal bir DAG (*Directed Acyclic Graph*) örneği, RGB durumunun (*istemci tarafı* Layer, kırmızı renkte) Bitcoin Blockchain'e (*Commitment* Layer, turuncu renkte) nasıl bağlandığını gösterebilir.


![RGB-Bitcoin](assets/fr/062.webp)


Bir Genesis'ün bir Seal (*Seal Definition*) tanımladığını, ardından bir *State Transition*'nin başka bir UTXO'da yeni bir tane oluşturmak için bu Seal'i kapattığını gösterir.


Bu bağlamda, terminolojiye ilişkin birkaç hatırlatma yapalım:




- Bir ***Assignment*** aşağıdakileri birleştirir:
    - Bir ***Seal Definition*** (bu da bir UTXO'a işaret ediyor);
- **Sahip Olunan Durumlar**, yani Ownership ile bağlantılı veriler (örneğin, transfer edilen token miktarı).
- Bir **Global State**, Contract'nin herkes tarafından görülebilen genel özelliklerini bir araya getirir ve evrimlerin küresel tutarlılığını sağlar.


*önceki bölümde açıklanan* **Durum Geçişleri**, Contract Operation'ün ana biçimidir. Bir veya daha fazla önceki duruma (Genesis veya başka bir State Transition'ten) atıfta bulunurlar ve bunları yeni bir duruma güncellerler.


![RGB-Bitcoin](assets/fr/063.webp)


Bu diyagram, bir **Durum Transition Bundle**'de, tek bir örnek işlemde birkaç mühür kapatılırken aynı anda yeni mühürlerin nasıl açılabileceğini göstermektedir. Aslında, RGB protokolünün ilginç bir özelliği ölçeklendirme yeteneğidir: birkaç geçiş bir Transition Bundle'de toplanabilir, her bir toplama **MPC ağacının** farklı bir yaprağı (benzersiz bir paket tanımlayıcı) ile ilişkilendirilir. **Deterministic Bitcoin Commitment** (DBC) mekanizması sayesinde, mesajın tamamı bir `Tapret` veya `Opret` çıktısına eklenirken, önceki mühürler kapatılır ve muhtemelen yenileri tanımlanır. **Anchor**, Blockchain'da saklanan Commitment ile Client-side Validation yapısı (*istemci tarafı*) arasında doğrudan bir bağlantı görevi görür.


İlerleyen bölümlerde, bir State Transition'ün oluşturulması ve doğrulanmasıyla ilgili tüm bileşenlere ve süreçlere bakacağız. Bu Elements'lerin çoğu **RGB Çekirdek Kütüphanesinde** uygulanan RGB konsensüsünün bir parçasıdır.


### Transition Bundle


RGB üzerinde, aynı Contract'e ait (yani Genesis **OpId**'den türetilen aynı **ContractId**'yi paylaşan) farklı Durum Geçişlerini paketlemek mümkündür. En basit durumda, yukarıdaki örnekte Alice ve Bob arasında olduğu gibi, bir **Transition Bundle** sadece bir geçiş içerir. Ancak çoklu mükellef işlemleri (eş birleşmeler, Yıldırım kanalı açılışları vb.) için destek, birkaç kullanıcının Durum Geçişlerini tek bir pakette birleştirebileceği anlamına gelir.


Bu geçişler toplandıktan sonra tek bir Bitcoin işleminde (MPC + DBC mekanizması ile) sabitlenir:




- Her bir State Transition karma hale getirilir ve bir Transition Bundle olarak gruplandırılır;
- Transition Bundle'nın kendisi hashlenir ve bu Contract'ye (bir BundleId) karşılık gelen MPC ağaç yaprağına eklenir;
- MPC ağacı son olarak Witness Transaction'deki `Opret` veya `Tapret` aracılığıyla devreye girer, böylece tüketilen mühürler kapatılır ve yeni mühürler tanımlanır.


Teknik olarak, MPC sayfasına eklenen **BundleId**, bundle'ın *InputMap* alanının katı serileştirmesine uygulanan etiketli bir Hash'dan elde edilir:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


Örneğin `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03`.


InputMap*, örnek işlemin her bir `i` girişi için ilgili State Transition'in *OpId* referansını listeleyen bir veri yapısıdır. Örneğin:


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- n`, işlemde bir `OpId`ye atıfta bulunan girişlerin toplam sayısıdır;
- opId(input_j)`, pakette bulunan Durum Geçişlerinden birinin işlem tanımlayıcısıdır.


Her bir girdiye yalnızca bir kez ve düzenli bir şekilde atıfta bulunarak, aynı Seal'nin aynı anda iki Durum Geçişinde iki kez harcanmasını önlüyoruz.


### Durum Oluşturma ve Aktif Durum


Durum Geçişleri bu nedenle bir varlığın Ownership bir kişiden diğerine aktarılması için kullanılabilir. Ancak, RGB protokolündeki tek olası işlemler bunlar değildir. Protokol üç **Contract İşlemi** tanımlar:




- **State Transition**;
- **Genesis**;
- State **Extension**.


Bunlar arasında **Genesis** ve **State Extension** bazen "*Durum Oluşturma işlemleri*" olarak adlandırılır, çünkü herhangi bir durumu hemen kapatmadan yeni durumlar oluştururlar. Bu çok önemli bir noktadır: **Genesis** ve **State Extension** bir Seal'ün kapatılmasını içermez. Aksine, Seal geçmişinde gerçekten doğrulanması için sonraki bir **State Transition** tarafından harcanması gereken yeni bir Blockchain tanımlarlar.


![RGB-Bitcoin](assets/fr/064.webp)


Bir Contract'in **Aktif Durumu** genellikle Genesis ile başlayan ve Bitcoin Blockchain'teki tüm çapaları takip eden işlemlerin geçmişinden (DAG) kaynaklanan en son durumlar kümesi olarak tanımlanır. Halihazırda kullanılmayan (yani harcanmış UTXO'lara bağlı) eski durumlar artık aktif olarak kabul edilmez, ancak geçmişin tutarlılığını kontrol etmek için gerekli olmaya devam eder.


### Genesis


Genesis, her RGB Contract'un başlangıç noktasıdır. Contract'u düzenleyen tarafından oluşturulur ve **Schema**'e uygun olarak başlangıç parametrelerini tanımlar. Bir RGB token durumunda, Genesis örneğin şunları belirtebilir:




- Başlangıçta oluşturulan jetonların sayısı ve sahipleri;
- Toplam olası ihraç tavanı;
- Herhangi bir yeniden düzenleme kuralı ve hangi katılımcıların uygun olduğu.


Contract'teki ilk işlem olan Genesis, önceki herhangi bir duruma referans vermez ve herhangi bir Seal'yi kapatmaz. Ancak, geçmişte görünmesi ve doğrulanması için Genesis'nın ilk State Transition tarafından **tüketilmesi** (kapatılması) gerekir (genellikle düzenleyicinin kendisine yapılan bir tarama/otomatik harcama işlemi veya kullanıcılara ilk dağıtım).


### State Extension


**Durum Uzantıları** akıllı sözleşmeler için orijinal bir özellik sunar. Redeem'u hemen kapatmadan Contract tanımında sağlanan belirli dijital hakların (*Valencies*) Seal'i mümkün kılarlar. Çoğu zaman, bu endişeler:




- Dağıtılmış token sorunları;
- Varlık takas mekanizmaları;
- Şartlı yeniden ihraçlar (diğer varlıkların imhasını içerebilir, vb.).


Teknik olarak, bir State Extension daha önce tanımlanmış bir *Valency*'ya (örneğin, Genesis veya başka bir State Transition'te) karşılık gelen bir *Redeem*'ye (belirli bir RGB girdi türü) atıfta bulunur. Yeni bir Seal tanımlar ve bundan yararlanan kişi veya koşul tarafından kullanılabilir. Bu Seal'in yürürlüğe girmesi için sonraki bir State Transition tarafından harcanması gerekir.


![RGB-Bitcoin](assets/fr/065.webp)


Örneğin: Genesis bir ihraç hakkı yaratır (*Valency*). Bu hak, daha sonra bir State Extension inşa eden yetkili bir aktör tarafından kullanılabilir:




- Valency'e (Redeem) atıfta bulunmaktadır;
- Bir UTXO'ye işaret eden yeni bir *Assignment* (yeni *Owned State* verileri) oluşturur;
- Bu yeni UTXO'un sahibi tarafından çıkarılan gelecekteki bir State Transition, yeni çıkarılan tokenleri gerçekten transfer edecek veya dağıtacaktır.


### Contract Operation Bileşenleri


Şimdi RGB'teki bir **Contract Operation**'i oluşturan Elements'ün her birine ayrıntılı bir şekilde bakmak istiyorum. Bir Contract Operation, bir Contract'nin durumunu değiştiren ve meşru alıcı tarafından deterministik bir şekilde istemci tarafında doğrulanan eylemdir. Özellikle, Contract Operation'in bir yandan Contract'nin **eski durumunu** ve diğer yandan **yeni durum** tanımını nasıl dikkate aldığını göreceğiz.


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


Yukarıdaki diyagrama bakarsak, bir Contract Operation'in **Yeni Durum**a atıfta bulunan Elements'yı ve güncellenmiş **Eski Durum**a atıfta bulunan diğerlerini içerdiğini görebiliriz.


**Yeni Devlet'in Elements'si:**




- **Atamalar**, içinde tanımlanmıştır:
 - **Seal Definition**;
 - **Owned State**.
- Değiştirilebilen veya zenginleştirilebilen **Global State**;
- **Değerlikler**, muhtemelen bir State Transition veya Genesis'de tanımlanmıştır.


Eski Devlet'e şu yolla atıfta bulunulur:




- Önceki durum geçişlerinin *Atamalarına* işaret eden **Girişler** (Genesis'te mevcut değildir);
- **Redeems**, önceden tanımlanmış Valenslere atıfta bulunur (yalnızca Eyalet Uzantılarında).


Buna ek olarak, bir Contract Operation operasyona özel daha genel alanlar içerir:




- `ffv` (*Hızlı ileri sürüm*): gW-845 sürümünü gösteren 2 baytlık tamsayı;
- `transitionType` veya `ExtensionType`: gW-846'ya göre Geçiş veya Uzantı türünü belirten 16 bitlik tamsayı;
- `ContractId`: gW-847 Genesis'in *OpId*'sine atıfta bulunan 32 baytlık sayı. Geçişler ve Uzantılara dahil edilmiştir, ancak Genesis'e dahil edilmemiştir;
- schemaId: sadece Genesis'de bulunur, bu Contract'un yapısını (*Schema*) temsil eden 32 baytlık Hash'dir;
- gW-855`: Testnet veya Mainnet ağında olup olmadığınızı gösteren boolean. Yalnızca Genesis;
- `altlayers1`: Bitcoin'ye ek olarak Anchor verileri için kullanılan alternatif Layer'ı (Sidechain veya diğer) tanımlayan değişken. Yalnızca Genesis'de mevcuttur;
- `metadata`: geçici bilgileri saklayabilen, karmaşık bir Contract'i doğrulamak için yararlı olan, ancak nihai durum geçmişine kaydedilmemesi gereken alan.


Son olarak, tüm bu alanlar, benzersiz bir parmak izi olan `OpId` üretmek için özelleştirilmiş bir karma işlemi ile yoğunlaştırılır. Bu `OpId` daha sonra Transition Bundle'ye entegre edilerek protokol içinde doğrulanmasını ve onaylanmasını sağlar.


Bu nedenle her *Contract Operation* `OpId` adlı 32 baytlık bir Hash ile tanımlanır. Bu Hash, işlemi oluşturan tüm Elements'in SHA256 Hash'sı ile hesaplanır. Başka bir deyişle, her *Contract Operation* işlemin gerçekliğini ve tutarlılığını doğrulamak için gereken tüm verileri içeren kendi kriptografik Commitment'üne sahiptir.


Bir RGB Contract daha sonra Genesis `OpId`den türetilen bir `ContractId` ile tanımlanır (çünkü Genesis öncesi bir işlem yoktur). Somut olarak, Genesis `OpId`yi alır, bayt sırasını tersine çevirir ve bir Base58 kodlaması uygularız. Bu kodlama `ContractId`nin işlenmesini ve tanınmasını kolaylaştırır.

### Durum güncelleme yöntemleri ve kuralları


**Contract State**, RGB protokolünün belirli bir Contract için izlemesi gereken bilgi kümesini temsil eder. Şunlardan oluşur:




- **Tek bir Global State**: bu, Contract'ün herkes tarafından görülebilen genel, küresel kısmıdır;
- Bir veya daha fazla **Sahipli Durum**: her Owned State benzersiz bir Seal (ve dolayısıyla Bitcoin üzerinde bir UTXO) ile ilişkilidir. Arasında bir ayrım yapılır:
    - Kamu Mülkiyetindeki Devletler,
    - Özel Mülkiyetli Devletler.


![RGB-Bitcoin](assets/fr/066.webp)


Global State* doğrudan *Contract Operation*'a tek bir blok olarak dahil edilmiştir. Sahip Olunan Durumlar* *Seal Definition* ile birlikte her bir *Assignment* içinde tanımlanır.


RGB'ün önemli bir özelliği, Global State ve Sahip Olunan Durumların değiştirilme şeklidir. Genel olarak iki tür davranış vardır:




- **Değiştirilebilir**: bir durum öğesi değiştirilebilir olarak tanımlandığında, her yeni işlem önceki durumu yeni bir durumla değiştirir. Eski veri daha sonra eski olarak kabul edilir;
- **Biriktirme**: bir durum öğesi biriktirme olarak tanımlandığında, her yeni işlem önceki durumun üzerine yazmadan ona yeni bilgiler ekler. Sonuç bir tür birikmiş geçmiş olur.


Contract'de bir durum öğesi değiştirilebilir veya kümülatif olarak tanımlanmamışsa, bu öğe sonraki işlemler için boş kalacaktır (başka bir deyişle, bu alan için yeni sürümler yoktur). Bir durumun (Global veya Sahipli) değiştirilebilir, kümülatif veya sabit olup olmadığını belirleyen Contract Schema'dur (yani kodlanmış Business Logic). Genesis tanımlandıktan sonra, bu özellikler yalnızca Contract'nin kendisi buna izin veriyorsa, örneğin belirli bir State Extension aracılığıyla değiştirilebilir.


Aşağıdaki tabloda her bir Contract Operation tipinin Global State ve Owned State'yi nasıl manipüle edebileceği (veya edemeyeceği) gösterilmektedir:


|                              | Genesis | State Extension | State Transition |
| ---------------------------- |:-----: |:-------------: |:--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`**: Contract'ün Schema'ü izin veriyorsa eylem mümkündür.


**`-`**: işlem sonraki bir State Transition tarafından onaylanmalıdır (State Extension tek başına Single-Use Seal'yı kapatmaz).


Ayrıca, her bir veri türünün zamansal kapsamı ve güncelleme hakları aşağıdaki tabloda ayırt edilebilir:


|                        | Metadata                                | Global State                                     | Owned State                                                                                              |
| ---------------------- | --------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Scope**              | Defined for a single Contract Operation | Defined globally for the contract                | Defined for each seal (*Assignment*)                                                                     |
| **Who can update it?** | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)        | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction) |
| **Temporal Scope**     | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


Global State genellikle "kimsenin sahip olmadığı, herkesin bildiği" olarak tanımlanır. Contract hakkında herkesin görebileceği genel bilgiler içerir. Örneğin, token yayınlayan bir Contract'de potansiyel olarak şunları içerir:




- Ticker (token'nin sembolik kısaltması): `ticker`;
- token'ün tam adı: `name`;
- Hassasiyet (ondalık basamak sayısı): `precision`;
- İlk teklif (ve/veya maksimum token limiti): `issuedSupply`;
- Yayın tarihi: `oluşturuldu`;
- Yasal veriler veya diğer kamuya açık bilgiler: `data`.


Bu Global State kamuya açık kaynaklara (web siteleri, IPFS, Nostr, Torrent, vb.) yerleştirilebilir ve topluluğa dağıtılabilir. Ayrıca, ekonomik teşvik (bu jetonları tutma ve aktarma ihtiyacı, vb.) doğal olarak Contract kullanıcılarını bu verileri kendileri korumaya ve yaymaya yönlendirir.


### Görevler


**Assignment** tanımlama için temel yapıdır:




- Belirli bir UTXO'a işaret eden Seal (*Seal Definition*);
- **Owned State**, yani bu Seal ile ilişkili özellik veya veri.


Bir *Assignment*, bir Bitcoin işlem çıktısının benzeri olarak görülebilir, ancak daha esnektir. Mülkiyet transferinin mantığı burada yatmaktadır: *Assignment* belirli bir varlık veya hak türünü (`AssignmentType`) bir Seal ile ilişkilendirir. Bu Seal ile bağlantılı UTXO'nin özel anahtarına sahip olan kişi (veya bu UTXO'yi harcayabilen kişi) bu *Owned State*'ün sahibi olarak kabul edilir.


RGB'in en güçlü yanlarından biri, *Seal Definition* ve *Owned State* alanlarını isteğe bağlı olarak *açığa çıkarma* veya gizleme (*gizleme*) yeteneğinde yatmaktadır. Bu, gizlilik ve seçiciliğin güçlü bir kombinasyonunu sunar. Örneğin, üçüncü taraflar yalnızca gizli sürümü (Hash) görürken, doğrulaması gereken kişiye açık sürümü sağlayarak tüm verileri ifşa etmeden bir geçişin geçerli olduğunu kanıtlayabilirsiniz. Uygulamada, bir geçişin `OpId`si her zaman *gizli* verilerden hesaplanır.


![RGB-Bitcoin](assets/fr/067.webp)


#### Seal Definition


**Seal Definition**, açıklanmış haliyle dört temel alana sahiptir: `txptr`, `vout`, `blinding` ve `method`:




- **txptr**: bu, Bitcoin üzerindeki bir UTXO'e referanstır:
    - Bir **Genesis Seal** söz konusu olduğunda, doğrudan mevcut bir UTXO'e (Genesis ile ilişkili olan) işaret eder;
    - Bir **Graph Seal** durumunda, sahip olabiliriz:
        - Belirli bir UTXO'a işaret ediyorsa basit bir `txid`,
        - Veya bir öz referansı belirten bir `WitnessTx`: Seal işlemin kendisine işaret eder. Bu özellikle harici bir UTXO mevcut olmadığında, örneğin Yıldırım kanalı açma işlemlerinde veya alıcının UTXO'ü yoksa kullanışlıdır.
- **vout**: `txptr` tarafından belirtilen işlemin çıkış numarası. Sadece standart Graph Seal için mevcuttur (`WitnessTx` için değil);
- **blinding**: gizliliği güçlendirmek ve UTXO'in kimliğine yönelik kaba kuvvet girişimlerini önlemek için 8 baytlık rastgele bir sayı;
- **method**: kullanılan ankraj yöntemini belirtir (`Tapret` veya `Opret`).


Seal Definition'nın *gizli* formu, RGB'e özgü bir etiketle birlikte bu 4 alanın birleştirilmesinden oluşan bir SHA256 Hash'dir (etiketli).


![RGB-Bitcoin](assets/fr/068.webp)


#### Sahip Olunan Devletler


Assignment'in ikinci bileşeni **Owned State**'tır. **Global State**'dan farklı olarak, genel veya özel biçimde var olabilir:




- **Herkese açık Owned State**: Seal ile ilişkili verileri herkes bilir. Örneğin, herkese açık bir görüntü;
- **Özel Owned State**: veriler gizlidir, yalnızca sahibi (ve gerekirse potansiyel olarak doğrulayıcı) tarafından bilinir. Örneğin, sahip olunan token sayısı.


RGB, bir Owned State için dört olası durum türü (*StateTypes*) tanımlar:




- **Bildirimsel**: sayısal veri içermez, sadece bildirimsel bir hak içerir (örneğin oy kullanma hakkı). Gizli ve açık formlar aynıdır;
- **Değiştirilebilir**: değiştirilebilir bir miktarı temsil eder (jetonlar gibi). Açık formda, `miktar` ve `körleme` vardır. Gizli formda, miktarı ve körlemeyi gizleyen tek bir *Pedersen commitment* vardır;
- **Structured**: yapılandırılmış verileri depolar (64 kB'a kadar). Açık biçimde, veri blobudur. Gizli formda, bu blobun etiketlenmiş bir Hash'idir:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


Örneğin:


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- **Ekler**: bir dosyayı (ses, görüntü, ikili, vb.) Owned State'a bağlar, Hash `file_hash` dosyasını, MIME türünü `media type` ve bir kriptografik tuzu `salt` depolar. Dosyanın kendisi başka bir yerde barındırılır. Gizli formda, önceki üç veri öğesi ile etiketlenmiş bir Hash'dir:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


Örneğin:


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


Özetlemek gerekirse, kamuya açık ve gizli formdaki 4 olası durum türü şunlardır:


```txt
State                      Concealed form                              Revealed form

+---------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+

```



| **Element**     | **Declarative** | **Fungible**                      | **Structured**       | **Attachments**        |
| --------------- | --------------- | --------------------------------- | -------------------- | ---------------------- |
| **Data**        | None            | Signed or unsigned 64-bit integer | Any strict data type | Any file               |
| **Info Type**   | None            | Signed or unsigned                | Strict types         | MIME Type              |
| **Privacy**     | Not required    | Pedersen commitment               | Hash with blinding   | Hashed file identifier |
| **Size Limits** | N/A             | 256 bytes                         | Up to 64 KB          | Up to ~500 GB          |


### Girişler


Bir *Contract Operation*'in Girişleri, bu yeni işlemde harcanan *Atamaları* ifade eder. Bir Giriş şunu gösterir:




- `prevOpId`: *Assignment*'nin bulunduğu önceki işlemin tanımlayıcısı (`OpId`);
- `assignmentType`: *Assignment* türü (örneğin, bir token için `assetOwner`);
- `Index`: gizli mühürlerin leksikografik sıralamasından sonra belirlenen, önceki `OpId` ile ilişkili listedeki *Assignment*'in indeksi.


Önceki Atamalar olmadığı için Girdiler Genesis'da asla görünmez. Durum Uzantılarında da görünmezler (çünkü Durum Uzantıları mühürleri kapatmaz; daha ziyade, Değerliklere dayalı olarak yeni mühürleri yeniden tanımlar).


Fungible` tipinde Sahipli Durumlarımız olduğunda, doğrulama mantığı (Schema'de sağlanan AluVM komut dosyası aracılığıyla) toplamların tutarlılığını kontrol eder: gelen belirteçlerin toplamı (*Girişler*) giden belirteçlerin toplamına eşit olmalıdır (yeni *Ödevler*'de).


### Metadata


**Metadata** alanı en fazla 64 KiB olabilir ve doğrulama için yararlı olan ancak Contract'ın kalıcı durumuna entegre edilmeyen geçici verileri dahil etmek için kullanılır. Örneğin, karmaşık komut dosyaları için ara hesaplama değişkenleri burada saklanabilir. Bu alanın global geçmişte saklanması amaçlanmamıştır, bu nedenle Sahipli Durumlar veya Global State kapsamı dışındadır.


### Değerlikler


**Değerlikler** orijinal bir RGB protokol mekanizmasıdır. Genesis, Durum Geçişleri veya Durum Uzantılarında bulunabilirler. Bir State Extension (*Redeems* aracılığıyla) tarafından etkinleştirilebilen ve ardından bir sonraki Geçiş ile sonlandırılabilen sayısal hakları temsil ederler. Her bir Valency bir `ValencyType` (16 bit) ile tanımlanır. Semantiği (yeniden düzenleme hakkı, token takası, yakma hakkı, vb.) Schema'te tanımlanmıştır.


Somut olarak, bir Genesis'un bir Valency "yeniden ihraç etme hakkı" tanımladığını düşünebiliriz. Bir State Extension, belirli koşullar yerine getirilirse, yeni bir token miktarı sunmak için onu (*Redeem*) tüketecektir. Ardından, bu şekilde oluşturulan Seal'nin sahibinden çıkan bir State Transition bu yeni jetonları transfer edebilir.


### Kurtarır


Kurtarmalar, Atamalar için Girişlerin Valency eşdeğeridir. Önceden tanımlanmış bir Valency'ün etkinleştirildiği yer burası olduğu için yalnızca Durum Uzantılarında görünürler. Bir Redeem iki alandan oluşur:




- `PrevOpId`: Valency'in belirtildiği işlemin `OpId`si;
- valencyType`: etkinleştirmek istediğiniz Valency türü (her `ValencyType` State Extension tarafından yalnızca bir kez kullanılabilir).


Örnek: Redeem, Valency'de neyin kodlandığına bağlı olarak bir CoinSwap uygulamasına karşılık gelebilir.


### RGB durum özellikleri


Şimdi RGB'deki bazı temel durum özelliklerine bir göz atacağız. Özellikle, şunlara bakacağız:




- Kesin ve tiplendirilmiş bir veri organizasyonu uygulayan **Strict Type System**;
- **Doğrulamayı** **Ownership**'den ayırmanın önemi;
- RGB'te *hızlı ileri* ve *geri itme* kavramlarını içeren **uzlaşma evrimi** sistemi.


Her zaman olduğu gibi, Contract durumu ile ilgili her şeyin protokolde belirtilen mutabakat kurallarına göre istemci tarafında doğrulandığını ve nihai kriptografik referansının Bitcoin işlemlerine bağlı olduğunu unutmayın.


#### Sıkı Tip Sistemi


RGB bir *Strict Type System* ve deterministik bir serileştirme modu (*Strict Encoding*) kullanır. Bu organizasyon, Contract verilerinin tanımlanması, işlenmesi ve doğrulanmasında mükemmel tekrarlanabilirliği ve hassasiyeti garanti etmek için tasarlanmıştır.


Birçok programlama ortamında (JSON, YAML...), veri yapısı esnek, hatta çok izin verici olabilir. RGB'de ise her bir alanın Yapısı ve Türleri açık kısıtlamalarla tanımlanmıştır. Örneğin:




- Her değişkenin belirli bir türü vardır (örneğin, 8 bitlik işaretsiz tamsayı `u8` veya 16 bitlik işaretli tamsayı vb;)
- Tipler oluşturulabilir (iç içe tipler). Bu, başka türlere dayalı bir tür tanımlayabileceğiniz anlamına gelir (örneğin, bir `u8` alanı, bir `bool` alanı vb. içeren bir toplama türü);
- Koleksiyonlar da belirtilebilir: listeler (*list*), kümeler (*set*) veya sözlükler (*map*), deterministik bir ilerleme sırası ile;
- Her alan sınırlandırılmıştır (*alt sınır* / *üst sınır*). Ayrıca koleksiyonlardaki Elements sayısına da sınırlama getiriyoruz (sınırlama);
- Veriler bayt hizalıdır ve serileştirme kesin olarak tanımlanmış ve nettir.


Bu katı kodlama protokolü sayesinde:




- Alanların sırası, kullanılan uygulama veya programlama dilinden bağımsız olarak her zaman aynıdır;
- Bu nedenle aynı veri seti üzerinde hesaplanan hash'ler tekrarlanabilir ve aynıdır (kesinlikle deterministik * taahhütler*);
- Sınırlar veri boyutunun kontrolsüz büyümesini önler (örn. çok fazla alan);
- Bu kodlama şekli kriptografik doğrulamayı kolaylaştırır, çünkü her katılımcı veriyi nasıl serileştireceğini ve Hash'ı tam olarak bilir.


Uygulamada, yapı (*Schema*) ve ortaya çıkan kod (*Interface* ve ilgili mantık) derlenir. Contract'yi (tipler, alanlar, kurallar) ve generate'ü katı bir ikili formatta tanımlamak için açıklayıcı bir dil kullanılır. Derlendiğinde sonuç şudur:




- Her alan için bir *Bellek Düzeni*;
- Anlamsal tanımlayıcılar (bellek yapısı aynı kalsa bile bir değişken adının değiştirilmesinin mantık üzerinde bir etkisi olup olmadığını gösterir).


Katı tip sistemi ayrıca değişikliklerin hassas bir şekilde izlenmesini sağlar: yapıdaki herhangi bir değişiklik (alan adındaki bir değişiklik bile) tespit edilebilir ve genel ayak izinde bir değişikliğe yol açabilir.


Son olarak, her derleme, kodun tam sürümünü (veri, kurallar, doğrulama) gösteren bir kriptografik tanımlayıcı olan bir parmak izi üretir. Örneğin, formun bir tanımlayıcısı:


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


Bu, ağda kullanılan sürümlerin ayrıntılı izlenebilirliğini sağlarken fikir birliği veya uygulama güncellemelerini yönetmeyi mümkün kılar.


Bir RGB Contract'in durumunun istemci tarafında doğrulanmasının çok zahmetli olmasını önlemek için, bir uzlaşma kuralı doğrulama hesaplamalarına dahil olan herhangi bir veri için maksimum `2^16` bayt (64 Kio) boyutunu dayatır. Bu, her değişken veya yapı için geçerlidir: 65536 bayttan fazla veya sayı olarak eşdeğeri (32768 16 bit tamsayı vb.). Bu aynı zamanda `2^16` Elements'yı geçemeyen koleksiyonlar (listeler, kümeler, eşlemeler) için de geçerlidir.


Bu limit garanti eder:




- Bir State Transition sırasında manipüle edilecek maksimum veri boyutunu kontrol eder;
- Doğrulama komut dosyalarını çalıştırmak için kullanılan sanal makine (*AluVM*) ile uyumluluk.


#### Doğrulama != Ownership paradigması


RGB'in en önemli yeniliklerinden biri, iki kavram arasındaki kesin ayrımdır:




- **Doğrulama**: bir State Transition'nin Contract'ün kurallarına (Business Logic, geçmiş, vb.) uyup uymadığının kontrol edilmesi;
- **Ownership** (Ownership veya kontrol): Single-Use Seal'nın harcanmasına (veya kapatılmasına) ve böylece State Transition'in gerçekleşmesine izin veren Bitcoin UTXO'a sahip olma gerçeği.


**Doğrulama** RGB yazılım yığını düzeyinde gerçekleşir (kütüphaneler, *taahhütler* protokolü, vb.). Rolü, Contract'un dahili kurallarına (miktarlar, izinler, vb.) uyulmasını sağlamaktır. Gözlemciler veya diğer katılımcılar da veri geçmişini doğrulayabilir.


*Öte yandan* **Ownership** tamamen Bitcoin'ün güvenliğine dayanır. Bir UTXO'in özel anahtarına sahip olmak, yeni bir geçiş başlatma (Single-Use Seal'yi kapatma) yeteneğini kontrol etmek anlamına gelir. Dolayısıyla, birisi verileri görebilse veya doğrulayabilse bile, ilgili UTXO'e sahip değilse durumu değiştiremez.


![RGB-Bitcoin](assets/fr/069.webp)


Bu yaklaşım, daha karmaşık blok zincirlerinde karşılaşılan klasik güvenlik açıklarını sınırlar (bir Smart contract'nın tüm kodunun herkese açık olduğu ve herkes tarafından değiştirilebildiği, bu da bazen saldırılara yol açmıştır). RGB'de, bir saldırgan On-Chain durumu ile basitçe etkileşime giremez, çünkü durum (*Ownership*) üzerinde hareket etme hakkı Bitcoin Layer tarafından korunmaktadır.


Dahası, bu ayrıştırma RGB'ün Lightning Network ile doğal bir şekilde entegre olmasını sağlar. Lightning kanalları, her seferinde On-Chain *taahhütlerini* devreye sokmadan RGB varlıklarını devreye sokmak ve taşımak için kullanılabilir. Kursun ilerleyen bölümlerinde RGB'ün Lightning üzerindeki bu entegrasyonuna daha yakından bakacağız.


#### RGB'teki konsensüs gelişmeleri


Anlamsal kod versiyonlamaya ek olarak, RGB, bir Contract'nın mutabakat kurallarını zaman içinde geliştirmek veya güncellemek için bir sistem içerir. İki ana evrim şekli vardır:




- **Hızlı ileri**
- **Geri itme**


Daha önce geçersiz olan bir kural geçerli hale geldiğinde hızlı ileri sarma gerçekleşir. Örneğin, Contract yeni bir `AssignmentType` türüne veya yeni bir alana izin verecek şekilde gelişirse:




- RGB, Client-side Validation'da çalıştığı ve Blockchain'un genel uyumluluğunu etkilemediği için bu klasik bir Blockchain hardfork ile karşılaştırılamaz;
- Pratik anlamda, bu tür bir değişiklik Contract Operation'deki `Ffv` (*fast-forward version*) alanı ile gösterilir;
- Mevcut sahipler zarar görmez: statüleri geçerliliğini korur;
- Öte yandan, yeni yararlanıcıların (veya yeni kullanıcıların) yeni kuralları tanımak için yazılımlarını (Wallet'lerini) güncellemeleri gerekir.


Geri itme, daha önce geçerli olan bir kuralın geçersiz hale gelmesi anlamına gelir. Bu nedenle kuralların "sertleştirilmesidir", ancak tam anlamıyla bir softfork değildir:




- Mevcut sahipler etkilenebilir (kendilerini yeni sürümde kullanılmayan veya geçersiz kılınan varlıklarla bulabilirler);
- Aslında yeni bir protokol oluşturduğumuzu düşünebiliriz: yeni kuralı benimseyen kişi eskisinden ayrılır;
- İhraççı, varlıkları bu yeni protokolde yeniden ihraç etmeye karar verebilir ve kullanıcıları her iki sürümü de yönetmek istiyorlarsa iki ayrı cüzdan (biri eski protokol için, diğeri yeni protokol için) tutmaya zorlayabilir.


RGB Contract işlemleri hakkındaki bu bölümde, bu protokolün altında yatan temel ilkeleri inceledik. Sizin de fark edeceğiniz gibi, RGB protokolünün doğasında var olan karmaşıklık birçok teknik terimin kullanılmasını gerektirmektedir. Bu nedenle, bir sonraki bölümde, bu ilk teorik bölümde ele alınan tüm kavramları özetleyen ve RGB ile ilgili tüm teknik terimlerin tanımlarını içeren bir sözlük sunacağım. Bir sonraki bölümde ise RGB sözleşmelerinin tanımına ve uygulamasına pratik bir bakış atacağız.


## RGB Sözlük


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


RGB dünyasında kullanılan önemli teknik terimlerin (alfabetik sıraya göre listelenmiştir) bu kısa sözlüğüne geri dönmeniz gerekirse, bunu yararlı bulacaksınız. İlk bölümde ele aldığımız her şeyi zaten anladıysanız bu bölüm gerekli değildir.


#### AluVM


AluVM kısaltması, Smart contract doğrulama ve dağıtık hesaplama için tasarlanmış kayıt tabanlı bir sanal makine olan "_Algoritmik mantık birimi Sanal Makinesi_" anlamına gelir. RGB sözleşmelerinin doğrulanması için kullanılır (ancak özel olarak ayrılmamıştır). Bir RGB Contract'da yer alan komut dosyaları veya işlemler böylece AluVM ortamında yürütülebilir.


Daha fazla bilgi için: [AluVM resmi web sitesi](https://www.AluVM.org/)


#### Anchor


Bir Anchor, bir işleme benzersiz bir _commitment_ dahil edildiğini kanıtlamak için kullanılan bir dizi istemci tarafı verisini temsil eder. RGB protokolünde, bir Anchor aşağıdaki Elements'ten oluşur:




- **Witness Transaction**'in Bitcoin işlem tanımlayıcısı (txid);
- **Multi Protocol Commitment (MPC)**;
- **Deterministic Bitcoin Commitment (DBC)**;
- Eğer **Tapret** Commitment mekanizması kullanılıyorsa **Ekstra İşlem Kanıtı (ETP)** (bu modele ayrılmış bölüme bakınız).


Bu nedenle bir Anchor, belirli bir Bitcoin işlemi ile RGB protokolü tarafından doğrulanan özel veriler arasında doğrulanabilir bir bağlantı kurmaya yarar. Bu verilerin, tam içerikleri kamuya açıklanmadan, gerçekten Blockchain'e dahil edildiğini garanti eder.


#### Assignment


RGB'nin mantığında, bir Assignment, bir Contract'ın durumu içinde belirli özellikleri değiştiren, güncelleyen veya oluşturan bir işlem çıktısına eşdeğerdir. Bir Assignment iki Elements içerir:




- A **Seal Definition** (belirli bir UTXO'e referans);
- Bir **Owned State** (bu yeni sahiple ilişkili durumu tanımlayan veriler).


Bu nedenle bir Assignment, devletin bir kısmının (örneğin bir varlık) artık bir UTXO'e bağlı bir Single-Use Seal aracılığıyla tanımlanan belirli bir sahibine tahsis edildiğini gösterir.


#### Business Logic


Business Logic, **Schema** (yani Contract'in kendi yapısı) tarafından tanımlanan bir Contract'in tüm kurallarını ve dahili işlemlerini bir araya getirir. Contract'in durumunun nasıl ve hangi koşullar altında gelişebileceğini belirler.


#### Client-side Validation


Client-side Validation, her bir tarafın (istemci) bir protokolün kurallarına göre özel olarak değiş tokuş edilen bir dizi veriyi doğruladığı süreci ifade eder. RGB durumunda, değiş tokuş edilen bu veriler **konşimentolar** olarak bilinen gruplarda bir araya getirilir. Tüm işlemlerin On-Chain yayınlanmasını gerektiren Bitcoin protokolünün aksine, RGB yalnızca _commitments_ (Bitcoin'e bağlı) kamuya açık olarak depolanmasına izin verirken, temel Contract bilgileri (geçişler, tasdikler, kanıtlar) off-chain olarak kalır ve yalnızca ilgili kullanıcılar arasında paylaşılır.


#### Commitment


Bir Commitment (kriptografik anlamda), `m` (mesaj) yapılandırılmış verisi ve `r` rastgele değeri üzerindeki bir işlemden deterministik olarak türetilen ve `C` olarak gösterilen matematiksel bir nesnedir. Şöyle yazıyoruz:


$$
C = \text{commit}(m, r)
$$


Bu mekanizma iki ana işlemden oluşmaktadır:




- **Commit**: `C` üretmek için bir kriptografik fonksiyon `m` mesajına ve rastgele bir `r` sayısına uygulanır;
- **Verify**: Bu Commitment'nin doğru olup olmadığını kontrol etmek için `C`, `m` mesajı ve `r` değerini kullanırız. Fonksiyon `True` veya `False` döndürür.


Bir Commitment iki özelliğe saygı göstermelidir:




- **Bağlama**: aynı `C`yi üreten iki farklı mesaj bulmak imkansız olmalıdır:


$$
m': \, | \,: m' \neq m \quad \text{and} \quad r': \, | \,: r' \neq r \quad
$$


Mesela:


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- **Gizleme**: `C` bilgisi `m` içeriğini açığa çıkarmamalıdır.


RGB protokolünde, bilginin kendisini ifşa etmeden belirli bir zamanda belirli bir bilginin varlığını kanıtlamak için bir Bitcoin işlemine bir Commitment dahil edilir.


#### Consignment


Bir **Consignment**, RGB'da Client-side Validation'e tabi olarak taraflar arasında değiş tokuş edilen verileri bir araya getirir. İki ana Consignment kategorisi vardır:




- **Contract Consignment**: *düzenleyici* (Contract düzenleyici) tarafından sağlanır, Schema, Genesis, Interface ve Interface Implementation gibi başlatma bilgilerini içerir.
- **Transfer Consignment**: ödeme yapan taraf (*ödeyen*) tarafından sağlanır. Terminal Consignment'ye kadar olan tüm durum geçişleri geçmişini içerir (yani, ödeyen tarafından alınan son durum).


Bu sevkiyatlar Blockchain'da kamuya açık olarak kaydedilmez; doğrudan ilgili taraflar arasında kendi seçtikleri iletişim kanalı üzerinden değiş tokuş edilir.


#### Contract


Bir Contract, RGB protokolü aracılığıyla birkaç aktör arasında dijital olarak yürütülen bir dizi haktır. Aktif bir durumu ve hangi işlemlerin yetkilendirildiğini (aktarımlar, uzatmalar, vb.) belirten bir Schema tarafından tanımlanan bir Business Logic'i vardır. Bir Contract'nin durumu ve geçerlilik kuralları Schema'te ifade edilir. Herhangi bir zamanda, Contract yalnızca bu Schema ve doğrulama komut dosyaları (örneğin AluVM'te çalıştırılır) tarafından izin verilenlere uygun olarak gelişir.


#### Contract Operation


Bir Contract Operation, Schema kurallarına göre gerçekleştirilen bir Contract durum güncellemesidir. RGB'da aşağıdaki işlemler mevcuttur:




- **State Transition**;
- **Genesis**;
- State **Extension**.


Her işlem belirli verileri ekleyerek veya değiştirerek durumu değiştirir (Global State, Owned State...).


#### Contract Participant


Bir Contract Participant, Contract ile ilgili operasyonlarda yer alan bir aktördür. RGB'da aşağıdakiler arasında bir ayrım yapılır:




- Genesis'i (Contract'nin kaynağı) oluşturan Contract'nin düzenleyicisi;
- Contract tarafları, yani Contract durumuna ilişkin hak sahipleri;
- Contract halkın erişimine açık Valilikler sunuyorsa, Devlet Uzantıları inşa edebilecek kamu tarafları.


#### Contract Rights


Contract Rights, bir RGB Contract'ya dahil olanlar tarafından kullanılabilecek çeşitli hakları ifade eder. Bunlar çeşitli kategorilere ayrılır:




- Belirli bir UTXO'un Ownership'i ile ilişkili **Ownership hakları** (bir _Seal Definition_ aracılığıyla);
- **Yürütme hakları**, yani Schema uyarınca bir veya daha fazla geçiş (Durum Geçişleri) oluşturma yeteneği;
- **Kamu hakları**, Schema belirli kamu kullanımlarına izin verdiğinde, örneğin bir Valency'nin itfası yoluyla bir State Extension'in oluşturulması.


#### Contract State


Contract State, bir Contract'nın belirli bir andaki mevcut durumuna karşılık gelir. Contract'nın durumunu yansıtan hem genel hem de özel verilerden oluşabilir. RGB aşağıdakiler arasında ayrım yapar:




- Contract'un genel özelliklerini içeren **Global State** (Genesis'ta ayarlanmış veya yetkili güncellemeler yoluyla eklenmiş);
- **Sahipli Devletler**, UTXO'ları tarafından tanımlanan belirli sahiplere aittir.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment (DBC), bir Bitcoin işleminde bir _commitment_'ı kanıtlanabilir ve benzersiz bir şekilde kaydetmek için kullanılan kurallar kümesidir. RGB protokolünde DBC'nin iki ana biçimi vardır:




- **Opret**
- **Tapret**


Bu mekanizmalar, Commitment'in deterministik olarak izlenebilir ve doğrulanabilir olmasını sağlamak için _commitment_'ın bir Bitcoin işleminin çıktısında veya yapısında nasıl kodlandığını tam olarak tanımlar.


#### Directed Acyclic Graph - DAG


Bir DAG (veya *Döngüsel Kılavuzlu Grafik*), topolojik zamanlamaya olanak tanıyan döngüsüz bir grafiktir. RGB sözleşmelerinin _shard_'ları gibi blok zincirleri de DAG'lar ile temsil edilebilir.


Daha fazla bilgi için: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### Gravür


Gravür, bir Contract'in sonraki sahiplerinin Contract geçmişine girebileceği isteğe bağlı bir veri dizesidir. Bu özellik örneğin **RGB21** Interface'de mevcuttur ve Contract geçmişine hatıra veya tanımlayıcı bilgilerin eklenmesini sağlar.


#### Ekstra İşlem Kanıtı - ETP


ETP (*Extra Transaction Proof*), Anchor'ün bir **Tapret** *Commitment* (_taproot_ bağlamında) doğrulamak için gereken ek verileri içeren kısmıdır. Diğer şeylerin yanı sıra, Taproot komut dosyasının dahili genel anahtarını (_internal PubKey_) ve _Script Path Spend_'e özgü bilgileri içerir.


#### Genesis


Genesis, bir Schema tarafından yönetilen ve RGB'deki herhangi bir Contract'nin başlangıç durumunu oluşturan veri kümesini ifade eder. Bitcoin'in _Genesis Block_ kavramı veya Coinbase Transaction kavramı ile karşılaştırılabilir, ancak burada _client-side_ ve RGB token seviyesinde.


#### Global State


Global State, Contract State'te yer alan genel özellikler kümesidir. Genesis'de tanımlanır ve Contract kurallarına bağlı olarak yetkili geçişler tarafından güncellenebilir. Sahip Olunan Durumların aksine, Global State belirli bir varlığa ait değildir; Contract içindeki bir kamu siciline daha yakındır.


#### Interface


Interface, bir Schema'de veya Contract işlemlerinde ve durumlarında derlenen ikili verilerin kodunu çözmek ve bunları kullanıcı veya Wallet'si için okunabilir hale getirmek için kullanılan talimatlar kümesidir. Bir yorumlama Layer görevi görür.


#### Interface Implementation


Interface Implementation, bir **Interface**'yı bir **Schema**'e bağlayan bildirimler kümesidir. Bir Contract'nin ham verilerinin kullanıcı veya ilgili yazılım (cüzdanlar) tarafından anlaşılabilmesi için Interface'nın kendisi tarafından gerçekleştirilen anlamsal çeviriyi sağlar.


#### Invoice


Bir Invoice, bir **State Transition** (ödeyici tarafından) oluşturulması için gerekli verileri içeren [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58)'de kodlanmış bir URL şeklini alır. Başka bir deyişle, karşı tarafın (*ödeyen*) varlığı transfer etmek veya Contract'in durumunu güncellemek için ilgili geçişi oluşturmasını sağlayan bir Invoice'dir.


#### Lightning Network


Lightning Network, Bitcoin üzerinde 2/2 çoklu imza cüzdanlarından oluşan merkezi olmayan bir ödeme kanalları ağıdır (veya _state channels_). Hızlı, düşük maliyetli _zincir dışı_ işlemler sağlarken, gerektiğinde tahkim (veya kapatma) için Bitcoin'in Layer 1'ine güvenir.


Lightning'in nasıl çalıştığı hakkında daha fazla bilgi için bu diğer kursa katılmanızı tavsiye ederim:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment (MPC), tek bir Bitcoin işlemine farklı sözleşmelerden birkaç **Geçiş Paketini** dahil etmek için RGB'de kullanılan Merkle Tree yapısını ifade eder. Buradaki fikir, blok alanının kullanımını optimize etmek için çeşitli taahhütleri (potansiyel olarak farklı sözleşmelere veya farklı varlıklara karşılık gelen) tek bir Anchor noktasında bir araya getirmektir.


#### Owned State


Bir Owned State, bir Contract State'in bir Assignment içine alınmış ve belirli bir sahibiyle (bir UTXO'e işaret eden bir Single-Use Seal aracılığıyla) ilişkilendirilmiş kısmıdır. Bu, örneğin, bir dijital varlığı veya o kişiye atanan belirli bir sözleşme hakkını temsil eder.


#### Ownership


Ownership, bir Seal Definition tarafından referans verilen bir UTXO'ü kontrol etme ve harcama yeteneğini ifade eder. Bir Owned State bir UTXO'e bağlandığında, bu UTXO'ün sahibi potansiyel olarak Contract'ün kurallarına göre ilişkili durumu transfer etme veya geliştirme hakkına sahiptir.


#### Partially Signed Bitcoin Transaction - PSBT


Bir PSBT (_Kısmen İmzalanmış Bitcoin İşlemi_) henüz tam olarak imzalanmamış bir Bitcoin işlemidir. İşlem On-Chain dağıtımı için hazır kabul edilene kadar, her biri belirli Elements (imzalar, komut dosyaları...) ekleyebilen veya doğrulayabilen birkaç varlık arasında paylaşılabilir.


Daha fazla bilgi için: [BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)


#### Pedersen commitment


Bir Pedersen commitment, toplama işlemine göre **homorfik** olma özelliğine sahip bir kriptografik Commitment türüdür. Bu, iki taahhüdün toplamını tek tek değerleri ortaya çıkarmadan doğrulamanın mümkün olduğu anlamına gelir.


Resmi olarak, eğer:


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


o zaman:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Bu özellik, örneğin, toplamları doğrulayabilirken, takas edilen jeton miktarlarını gizlemek için kullanışlıdır.


Daha fazla bilgi için: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


Bir State Extension'de, bir Redeem, daha önce beyan edilmiş bir **Valency**'u geri alma (veya kullanma) eylemini ifade eder. Valency bir kamu hakkı olduğundan, Redeem yetkili bir katılımcının belirli bir Contract State Extension'yi talep etmesine izin verir.


#### Schema


RGB'teki bir Schema, bir Contract'ün çalışmasını yöneten değişkenler, kurallar ve Business Logic (*Business Logic*) kümesini tanımlayan bildirimsel bir kod parçasıdır. Schema durum yapısını, izin verilen geçiş türlerini ve doğrulama koşullarını tanımlar.


#### Seal Definition


Seal Definition, bir Assignment'in _commitment_'ı yeni sahibin sahip olduğu bir UTXO ile ilişkilendiren kısmıdır. Başka bir deyişle, koşulun nerede bulunduğunu (hangi UTXO'da) belirtir ve bir varlığın veya hakkın Ownership'unu oluşturur.


#### Shard


Bir Shard, bir RGB Contract'nin Durum Geçişleri geçmişinin DAG'ındaki bir dalı temsil eder. Başka bir deyişle, Contract'nin genel geçmişinin tutarlı bir alt kümesidir ve örneğin _Genesis_'ten bu yana belirli bir varlığın geçerliliğini kanıtlamak için gereken geçişler dizisine karşılık gelir.


#### Single-Use Seal


Bir Single-Use Seal, gelecekte yalnızca bir kez ortaya çıkacak ve belirli bir kitlenin tüm üyeleri tarafından bilinmesi gereken, henüz bilinmeyen bir mesaj için Commitment'nin kriptografik bir vaadidir. Amaç, aynı Seal için birden fazla rakip taahhüdün oluşturulmasını önlemektir.


#### Stash


Stash, bir kullanıcının doğrulama amacıyla bir veya daha fazla RGB sözleşmesi için depoladığı istemci tarafı veri kümesidir (*Client-side Validation*). Buna geçiş geçmişi, sevkiyatlar, geçerlilik kanıtları vb. dahildir. Her tutucu geçmişin yalnızca ihtiyaç duyduğu kısımlarını saklar (*shard*).


#### State Extension


Bir State Extension, daha önce beyan edilen **Valansları** kullanarak durum güncellemelerini yeniden tetiklemek için kullanılan bir Contract Operation'tür. Etkili olabilmesi için, bir State Extension daha sonra bir State Transition (Contract'nin son durumunu güncelleyen) tarafından kapatılmalıdır.


#### State Transition


State Transition, bir RGB Contract'ün durumunu yeni bir duruma değiştiren işlemdir. Global State ve/veya Owned State verilerini değiştirebilir. Uygulamada, her geçiş Schema kuralları tarafından doğrulanır ve bir _commitment_ aracılığıyla Bitcoin Blockchain'ye bağlanır.


#### Taproot


Bitcoin'in [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) ve [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki) tarafından tanıtılan SegWit v1 işlem formatını ifade eder. Taproot, özellikle işlemleri daha kompakt hale getirerek ve birbirinden ayırt edilmesini zorlaştırarak komut dosyalarının gizliliğini ve esnekliğini artırır.


#### Terminal Consignment - Consignment Endpoint


Terminal Consignment (veya _Consignment Endpoint_), alıcının Invoice'inden (*payee*) oluşturulan State Transition dahil olmak üzere Contract'nin son durumunu içeren bir *transfer Consignment*'tir. Bu nedenle, Ownership veya durumun aktarıldığını kanıtlamak için gerekli verilerle birlikte bir aktarımın son noktasıdır.


#### Transition Bundle


Bir Transition Bundle, hepsi aynı ***Witness Transaction*** Bitcoin ile meşgul olan bir dizi RGB Durum Geçişidir (aynı Contract'ye ait). Bu, birkaç güncellemeyi veya aktarımı tek bir On-Chain Anchor içinde bir araya getirmeyi mümkün kılar.


#### UTXO


Bir Bitcoin UTXO (*Harcanan İşlem Çıktısı*), bir işlemin Hash'si ve çıktı indeksi (*vout*) ile tanımlanır. Bazen _çıkış noktası_ olarak da adlandırılır. RGB protokolünde, bir UTXO'e (bir **Seal Definition** aracılığıyla) yapılan referans, **Owned State**'un, yani Blockchain'de tutulan özelliğin konumunu sağlar.


#### Valency


Valency, devlet tarafından saklanmasını gerektirmeyen, ancak bir **State Extension** aracılığıyla kullanılabilen bir kamu hakkıdır. Bu nedenle, daha sonraki bir tarihte belirli bir genişletmeyi gerçekleştirmek için Contract mantığında beyan edilen, herkese (veya belirli oyunculara) açık bir olasılık biçimidir.


#### Witness Transaction


Witness Transaction, Multi Protocol Commitment (MPC) içeren bir mesajın etrafındaki Single-Use Seal'yi kapatan Bitcoin işlemidir. Bu işlem UTXO protokolüne bağlı Commitment'ü Seal yapmak için bir RGB harcar veya bir Seal oluşturur. Durumun zaman içinde belirli bir noktada ayarlandığına dair bir On-Chain kanıtı görevi görür.


# RGB üzerinde programlama


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## RGB sözleşmelerinin uygulanması


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


Bu bölümde, bir RGB Contract'in nasıl tanımlandığına ve uygulandığına daha yakından bakacağız. Bir RGB Contract'in bileşenlerinin neler olduğunu, rollerinin neler olduğunu ve nasıl oluşturulduklarını göreceğiz.


### Bir RGB Contract'ün bileşenleri


Şimdiye kadar, bir Contract'nın başlangıç noktasını temsil eden **Genesis**'yi tartıştık ve bunun bir *Contract Operation*'in mantığına ve protokolün durumuna nasıl uyduğunu gördük. Bununla birlikte, bir RGB Contract'nın tam tanımı yalnızca Genesis ile sınırlı değildir: birlikte uygulamanın kalbini oluşturan üç tamamlayıcı bileşen içerir.


İlk bileşen **Schema** olarak adlandırılır. Bu, Contract'un temel yapısını ve Business Logic'u (*Business Logic*) tanımlayan bir dosyadır. Kullanılan veri tiplerini, doğrulama kurallarını, izin verilen işlemleri (örneğin ilk token ihracı, transferler, özel koşullar, vb.), kısacası Contract'un nasıl çalıştığını belirleyen genel çerçeveyi belirtir.


İkinci bileşen **Interface**'tür. Kullanıcıların (ve buna bağlı olarak portföy yazılımının) bu Contract ile nasıl etkileşime gireceğine odaklanır. Semantiği, yani çeşitli alanların ve eylemlerin okunabilir temsilini tanımlar. Dolayısıyla, Schema Contract'ün teknik olarak nasıl çalıştığını tanımlarken, Interface bu işlevlerin nasıl sunulacağını ve ortaya çıkarılacağını tanımlar: yöntem adları, veri gösterimi vb.


Üçüncü bileşen, Schema ve Interface arasında bir tür köprü görevi görerek önceki ikisini tamamlayan **Interface Implementation**'dır. Başka bir deyişle, Interface tarafından ifade edilen semantiği Schema'de tanımlanan temel kurallarla ilişkilendirir. Örneğin, Wallet'da girilen bir parametre ile protokol tarafından dayatılan ikili yapı arasındaki dönüşümü veya doğrulama kurallarının makine dilinde derlenmesini yönetecek olan bu uygulamadır.


Bu modülerlik RGB'nin ilginç bir özelliğidir, çünkü protokolün mutabakat kurallarına uydukları sürece farklı geliştirici gruplarının bu yönler üzerinde ayrı ayrı çalışmasına izin verir (*Schema*, *Interface*, *Uygulama*).


Özetlemek gerekirse, her bir Contract şunlardan oluşur:




- Contract'in ilk durumu olan **Genesis** (ve bir varlığın, hakkın veya diğer parametrelendirilebilir verilerin ilk Ownership'ünü tanımlayan özel bir işleme benzetilebilir);
- Contract'in Business Logic'sini (veri türleri, doğrulama kuralları vb.) açıklayan **Schema**;
- **Interface**, hem cüzdanlar hem de insan kullanıcılar için anlamsal bir Layer sağlayarak işlemlerin okunmasını ve yürütülmesini netleştirir;
- Contract tanımının kullanıcı deneyimi ile tutarlı olmasını sağlamak için Business Logic ve sunum arasındaki boşluğu dolduran **Interface'ün uygulanması**.


![RGB-Bitcoin](assets/fr/070.webp)


Bir Wallet'nin bir RGB varlığını (değiştirilebilir bir token veya herhangi bir hak) yönetebilmesi için tüm bu Elements'ları derlemiş olması gerektiğine dikkat etmek önemlidir: *Schema*, *Interface*, *Interface Implementation* ve *Genesis*. Bu, bir ***Contract Consignment***, yani istemci tarafı Contract'i doğrulamak için gereken her şeyi içeren bir veri paketi aracılığıyla iletilir.


Bu kavramların açıklığa kavuşturulmasına yardımcı olmak için, RGB Contract'in bileşenlerini nesne yönelimli programlamada (OOP) veya Ethereum ekosisteminde halihazırda bilinen kavramlarla karşılaştıran özet bir tablo aşağıda verilmiştir:


| RGB Contract Component       | Meaning                        | OOP Equivalent                                     | Ethereum Equivalent                |
| ---------------------------- | ------------------------------ | -------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | Initial state of the contract  | Class constructor                                  | Contract constructor               |
| **Schema**                   | Business logic of the contract | Class                                              | Contract                           |
| **Interface**                | Semantics of the contract      | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                       |
| **Interface Implementation** | Mapping semantics and logic    | Impl (Rust) / Implements (Java)                    | Application Binary Interface (ABI) |


Sol taraftaki sütun RGB protokolüne özgü Elements'yi göstermektedir. Orta sütun her bir bileşenin somut işlevini göstermektedir. Ardından, "OOP eşdeğeri" sütununda, nesne yönelimli programlamadaki eşdeğer terimi buluyoruz:




- **Genesis**, *Sınıf kurucusuna* benzer bir rol oynar: Contract'un durumu burada başlatılır;
- **Schema** bir sınıfın tanımıdır, yani özelliklerinin, yöntemlerinin ve temel mantığının tanımıdır;
- **Interface**, *arayüzlere* (Java), *özelliklere* (Rust) veya *protokollere* (Swift) karşılık gelir: bunlar fonksiyonların, olayların, alanların genel tanımlarıdır...;
- **Interface Implementation**, Rust'daki *Impl* veya Java'daki *Implements*'e karşılık gelir; burada kodun Interface'te bildirilen yöntemleri gerçekte nasıl yürüteceğini belirtiriz.


Ethereum bağlamında, Genesis *Contract kurucusuna*, Schema Contract tanımına, Interface ERC-20 veya ERC-721 gibi bir standarda ve Interface Implementation Contract ile etkileşim biçimini belirten ABI'ye (*Uygulama İkilisi Interface*) daha yakındır.


RGB'nın modülerliğinin avantajı, farklı paydaşların *Schema* mantığına ve *Interface* semantiğine saygı duydukları sürece örneğin kendi Interface Implementation'lerini yazabilmelerinde yatmaktadır. Böylece, bir ihraççı Contract'ün mantığını değiştirmeden yeni, daha kullanıcı dostu bir ön uç (Interface) geliştirebilir veya tersine, işlevsellik eklemek için Schema'i genişletebilir ve eski uygulamalar temel işlevsellik için geçerli kalırken uyarlanmış Interface Implementation'nin yeni bir sürümünü sağlayabilir.


Yeni bir Contract derlediğimizde, bileşenlerinin (Schema, Interface, Interface Implementation) yanı sıra bir generate bir Genesis (varlığı ihraç etmenin veya dağıtmanın ilk adımı). Bundan sonra, Contract tamamen çalışır durumdadır ve cüzdanlara ve kullanıcılara yayılabilir. Genesis'nin bu üç bileşenle birleştirildiği bu yöntem, yüksek derecede özelleştirme (her Contract'in kendi mantığı olabilir), ademi merkeziyetçilik (herkes belirli bir bileşene katkıda bulunabilir) ve güvenlik (doğrulama, diğer blok zincirlerinde olduğu gibi keyfi on-chain code'e bağlı olmadan protokol tarafından sıkı bir şekilde tanımlanmaya devam eder) sağlar.


Şimdi bu bileşenlerin her birine daha yakından bakmak istiyorum: **Schema**, **Interface** ve **Interface Implementation**.


### Schema


Önceki bölümde, RGB ekosisteminde bir Contract'un birkaç Elements'den oluştuğunu gördük: başlangıç durumunu oluşturan Genesis ve diğer birkaç tamamlayıcı bileşen. Schema'nin amacı, Contract'un tüm Business Logic'lerini, yani veri yapısını, kullanılan türleri, izin verilen işlemleri ve bunların koşullarını açık bir şekilde tanımlamaktır. Bu nedenle, her katılımcı (örneğin bir Wallet) aldığı durum geçişlerinin Schema'de tanımlanan mantığa uygunluğunu kontrol etmek zorunda olduğundan, bir Contract'u istemci tarafında çalışır hale getirmede çok önemli bir unsurdur.


Bir Schema nesne yönelimli programlamadaki (OOP) bir "sınıfa" benzetilebilir. Genel olarak, bir Contract'in bileşenlerini tanımlayan bir model olarak hizmet eder, örneğin:




- Sahip Olunan Durumların ve Atamaların farklı türleri;
- Değerlikler, yani belirli işlemler için tetiklenebilen (*itfa edilebilen*) özel haklar;
- Global State alanları, Contract'in global, genel ve paylaşılan özelliklerini tanımlar;
- Genesis yapısı (Contract'u etkinleştiren ilk işlem);
- Durum Geçişlerinin ve Durum Uzantılarının izin verilen biçimleri ve bu işlemlerin durumu nasıl değiştirebileceği;
- Geçici veya ek bilgileri saklamak için her işlemle ilişkili meta veriler;
- Dahili Contract verilerinin nasıl gelişebileceğini belirleyen kurallar (örneğin, bir alanın değiştirilebilir veya kümülatif olup olmadığı);
- Geçerli kabul edilen işlem dizileri: örneğin, uyulması gereken bir geçiş sırası veya karşılanması gereken bir dizi mantıksal koşul.


![RGB-Bitcoin](assets/fr/071.webp)


RGB üzerindeki bir varlığın *vericisi* bir Contract yayınladığında, onunla ilişkili Genesis ve Schema'ü sağlar. Varlıkla etkileşime geçmek isteyen kullanıcılar veya cüzdanlar, Contract'nin arkasındaki mantığı anlamak ve daha sonra katılacakları geçişlerin meşru olduğunu doğrulayabilmek için bu Schema'ü alır.


Bir RGB varlığı (örneğin bir token transferi) hakkında bilgi alan herkes için ilk adım, bu bilgiyi Schema ile doğrulamaktır. Bu, Schema derlemesinin aşağıdakiler için kullanılmasını içerir:




- Sahip Olunan Durumların, Atamaların ve diğer Elements'un doğru tanımlandığını ve dayatılan tiplere (*sıkı tip sistemi* olarak adlandırılır) uyduklarını kontrol edin;
- Geçiş kurallarının (doğrulama komut dosyaları) yerine getirilip getirilmediğini kontrol edin. Bu komut dosyaları, istemci tarafında bulunan ve Business Logic'ün tutarlılığını doğrulamaktan sorumlu olan AluVM aracılığıyla çalıştırılabilir (transfer miktarı, özel koşullar, vb.).


Uygulamada Schema, chain code (Ethereum'daki EVM) üzerinde depolanan blok zincirlerinde görülebileceği gibi çalıştırılabilir kod değildir. Aksine, RGB, Business Logic'ü (bildirimsel) Blockchain'teki (kriptografik çapalarla sınırlı olan) çalıştırılabilir koddan ayırır. Böylece, Schema kuralları belirler, ancak bu kuralların uygulanması Client-side Validation ilkesine göre Blockchain'ün dışında, her katılımcının sahasında gerçekleşir.


Bir Schema, RGB uygulamaları tarafından kullanılmadan önce derlenmelidir. Bu derleme ikili bir dosya (örneğin `.RGB`) veya şifrelenmiş bir ikili dosya (`.rgba`) üretir. Wallet bu dosyayı içe aktardığında şunu bilir:




- Katı tip sistemi sayesinde her bir veri tipinin (tamsayılar, yapılar, diziler...) neye benzediği;
- Genesis'in nasıl yapılandırılması gerektiği (varlık başlatmayı anlamak için);
- Farklı işlem türleri (Durum Geçişleri, Durum Uzantıları) ve bunların durumu nasıl değiştirebileceği;
- AluVM motorunun işlemlerin geçerliliğini kontrol etmek için uygulayacağı komut dosyası kuralları (Schema'de tanıtılmıştır).


Önceki bölümlerde açıklandığı gibi, *sıkı tip sistemi* bize istikrarlı, deterministik bir kodlama biçimi sağlar: İster Sahipli Durumlar, ister Küresel Durumlar veya Değerlikler olsun, tüm değişkenler kesin olarak tanımlanır (boyut, gerekirse alt ve üst sınırlar, işaretli veya işaretsiz tip, vb.) Örneğin karmaşık kullanım durumlarını desteklemek için iç içe yapılar tanımlamak da mümkündür.


İsteğe bağlı olarak, Schema mevcut bir temel yapının (bir şablon) yeniden kullanımını kolaylaştıran bir kök `SchemaId`ye referans verebilir. Bu şekilde, bir Contract'ü geliştirebilir veya zaten kanıtlanmış bir şablondan varyasyonlar (örneğin yeni bir token türü) oluşturabilirsiniz. Bu modülerlik, tüm sözleşmeleri yeniden oluşturma ihtiyacını ortadan kaldırır ve en iyi uygulamaların standartlaştırılmasını teşvik eder.


Bir diğer önemli nokta da durum evrimi mantığının (transferler, güncellemeler, vb.) Schema'de komut dosyaları, kurallar ve koşullar şeklinde tanımlanmış olmasıdır. Dolayısıyla, Contract tasarımcısı bir yeniden kullanıma izin vermek veya bir yakma mekanizması (jetonların imhası) uygulamak isterse, Schema'in doğrulama bölümünde AluVM için ilgili komut dosyalarını belirtebilir.


#### Programlanabilir On-Chain blok zincirlerinden farkı


Smart contract kodunun (çalıştırılabilir) Blockchain'nin içine yazıldığı Ethereum gibi sistemlerin aksine, RGB Contract'ü (mantığını) off-chain derlenmiş bir bildirim belgesi şeklinde saklar. Bu şu anlama gelir:




- Bitcoin ağının her düğümünde çalışan Turing-complete VM yoktur. Bir RGB Contract'nin kuralları Blockchain'da değil, bir durumu doğrulamak isteyen her kullanıcıda yürütülür;
- Contract verileri Blockchain'u kirletmez: sadece kriptografik kanıtlar (*taahhütler*) Bitcoin işlemlerine gömülür (`Tapret` veya `Opret` aracılığıyla);
- Schema, Bitcoin Blockchain üzerinde bir Fork gerektirmeden güncellenebilir veya reddedilebilir (*fast-forward*, *push-back*, vb.). Cüzdanların yeni Schema'i içe aktarması ve mutabakat değişikliklerine uyum sağlaması yeterlidir.


#### İhraççı ve kullanıcılar tarafından kullanım


Bir *çıkarıcı* bir varlık yarattığında (örneğin, enflasyonist olmayan değiştirilebilir bir token), hazırlar:




- Emisyon, transfer vb. kurallarını açıklayan bir Schema;
- Bu Schema'a uyarlanmış bir Genesis (ihraç edilen toplam jeton sayısı, ilk sahibinin kimliği, yeniden ihraç için herhangi bir özel Valör, vb. ile birlikte).


Daha sonra derlenmiş Schema'yi (bir `.RGB` dosyası) kullanıcıların kullanımına sunar, böylece bu token aktarımını alan herkes işlemin tutarlılığını yerel olarak kontrol edebilir. Bu Schema olmadan, bir kullanıcı durum verilerini yorumlayamaz veya Contract kurallarına uygun olup olmadığını kontrol edemez.


Dolayısıyla, yeni bir Wallet bir varlığı desteklemek istediğinde, sadece ilgili Schema'i entegre etmesi gerekir. Bu mekanizma, Wallet'nın yazılım tabanını invaziv bir şekilde değiştirmeden yeni RGB varlık türlerine uyumluluk eklemeyi mümkün kılar: tek gereken Schema ikili dosyasını içe aktarmak ve yapısını anlamaktır.


Schema, RGB'teki Business Logic'i tanımlar. Bir Contract'nin evrim kurallarını, verilerinin yapısını (Sahip Olunan Durumlar, Global State, Değerlikler) ve ilgili doğrulama komut dosyalarını (AluVM tarafından yürütülebilir) listeler. Bu bildirimsel belge sayesinde, bir Contract'nin tanımı (derlenmiş dosya) kuralların fiili olarak yürütülmesinden (istemci tarafı) net bir şekilde ayrılmıştır. Bu ayrıştırma RGB'e büyük bir esneklik kazandırarak çok çeşitli kullanım durumlarına (değiştirilebilir tokenlar, NFT, daha sofistike sözleşmeler) olanak sağlarken programlanabilir On-Chain blok zincirlerinin tipik karmaşıklığından ve kusurlarından kaçınır.


#### Schema örneği


Bir RGB Contract için Schema'nin somut bir örneğine göz atalım. Bu, Rust'da `nia.rs' dosyasından ("*Şişirilemeyen Varlıklar*"ın baş harfleri) bir alıntıdır ve ilk Supply'lerinin (enflasyonist olmayan bir varlık) ötesinde yeniden ihraç edilemeyen değiştirilebilir jetonlar için bir model tanımlar. Bu tür token, RGB evreninde Ethereum'daki ERC20'nin eşdeğeri olarak görülebilir, yani belirli temel kurallara (örneğin transferler, Supply başlatma vb.) uyan değiştirilebilir tokenlar.


Kodun içine dalmadan önce, bir RGB Schema'nin genel yapısını hatırlamakta fayda var. Çerçeveleyen bir dizi bildirim vardır:




- Başka bir temel Schema'ün şablon olarak kullanıldığını gösteren olası bir `SchemaId`;
- **Küresel Devletler** ve **Sahip Olunan Devletler** (katı tipleriyle);
- **Değerlikler** (eğer varsa);
- Bu durumlara ve değerliklere referans verebilen **Operasyonlar** (Genesis, Durum Geçişleri, Durum Uzantıları);
- Verileri tanımlamak ve doğrulamak için kullanılan **Strict Type System**;
- **Doğrulama komut dosyaları** (AluVM aracılığıyla çalıştırılır).


![RGB-Bitcoin](assets/fr/072.webp)


Aşağıdaki kod Rust Schema'nin tam tanımını göstermektedir. Aşağıda (1)'den (9)'a kadar olan ek açıklamaları takip ederek parça parça yorumlayacağız:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {

// definitions of libraries and variables

// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),

// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},

// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},

// ===== PART 5: Valencies =====
valency_types: none!(),

// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},

// ===== PART 7: Extensions =====
extensions: none!(),

// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},

// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - **Fonksiyon başlığı ve Alt Şema**


Nia_schema()` fonksiyonu bir `SubSchema` döndürerek bu Schema'in daha genel bir Schema'den kısmen miras alabileceğini gösterir. RGB ekosisteminde bu esneklik, bir ana Schema'in belirli standart Elements'lerini yeniden kullanmayı ve ardından söz konusu Contract'a özgü kuralları tanımlamayı mümkün kılar. Burada, `subset_of` `None` olacağı için kalıtımı etkinleştirmemeyi seçiyoruz.




- (2) - Genel özellikler: **ffv, subset_of, type_system**


Fv` özelliği Contract'ün *hızlı ileri* sürümüne karşılık gelir. Burada `zero!()` değeri, 0 sürümünde veya bu Schema'ün ilk sürümünde olduğumuzu gösterir. Daha sonra yeni işlevler (yeni işlem türü, vb.) eklemek isterseniz, fikir birliği değişikliğini belirtmek için bu sürümü artırabilirsiniz.


Subset_of: None` özelliği kalıtımın olmadığını teyit eder. Type_system` alanı, `types` kütüphanesinde tanımlanmış olan katı tip sistemine atıfta bulunur. Bu satır, Contract tarafından kullanılan tüm verilerin söz konusu kütüphane tarafından sağlanan katı serileştirme uygulamasını kullandığını gösterir.




- (3) - Küresel Devletler


Global_types` bloğunda dört adet Elements bildiriyoruz. Daha sonra bunlara başvurmak için `GS_NOMINAL` veya `GS_ISSUED_SUPPLY` gibi bir anahtar kullanırız:




- `GS_NOMINAL`, oluşturulan token'nin çeşitli alanlarını (tam ad, ticker, hassasiyet...) tanımlayan bir `DivisibleAssetSpec` türünü ifade eder;
- gS_DATA` feragatname, meta veri veya diğer metinler gibi genel verileri temsil eder;
- `GS_TIMESTAMP` bir yayın tarihini ifade eder;
- `GS_ISSUED_SUPPLY` toplam Supply'i, yani oluşturulabilecek maksimum token sayısını ayarlar.


Once(...)` anahtar sözcüğü, bu alanların her birinin yalnızca bir kez görünebileceği anlamına gelir.




- (4) - Sahip Olunan Türler


Owned_types` içinde, değiştirilebilir bir durumu tanımlayan `OS_ASSET` bildiriyoruz. StateSchema::Fungible(FungibleType::Unsigned64Bit)` kullanıyoruz, bu da varlıkların (token) miktarının 64 bitlik işaretsiz bir tamsayı olarak saklandığını gösteriyor. Böylece, herhangi bir işlem bu token'dan belirli miktarda birim gönderecek ve bu katı tipli sayısal yapıya göre doğrulanacaktır.




- (5) - **Valanslar**


Valency_types: none!()` belirtiyoruz, bu da bu Schema'de Valency olmadığı anlamına gelir, başka bir deyişle özel veya ekstra haklar (yeniden düzenleme, koşullu yakma vb.) yoktur. Eğer bir Schema herhangi birini içeriyor olsaydı, bu bölümde beyan edilirlerdi.




- (6) - Genesis: ilk operasyonlar


Burada Contract Operasyonlarını beyan eden kısma giriyoruz. Genesis tarafından açıklanmaktadır:




- Metadata`nın yokluğu (alan `metadata: Ty::<SemId>::UNIT.id(None)`);
- Her biri bir kez bulunması gereken Küresel Durumlar (`Once`);
- OS_ASSET`in `OnceOrMore` olarak görünmesi gereken bir Atamalar listesi. Bu, Genesis'in en az bir `OS_ASSET` Assignment (bir ilk tutucu) gerektirdiği anlamına gelir;
- Hayır Valency: `valencies: none!()`.


İlk token ihracının tanımını bu şekilde sınırlandırıyoruz: ihraç edilen Supply'i (`GS_ISSUED_SUPPLY`) ve en az bir tutucuyu (`OS_ASSET` türünde bir Owned State) beyan etmeliyiz.




- (7) - Uzantılar


Uzantılar: yok!()` alanı bu Contract'de hiçbir State Extension öngörülmediğini belirtir. Bu, bir dijital hakkı (Valency) Redeem veya bir Geçişten önce bir State Extension gerçekleştirmek için herhangi bir işlem olmadığı anlamına gelir. Her şey Genesis veya Durum Geçişleri aracılığıyla yapılır.




- (8) - Geçişler: TS_TRANSFER


Geçişler` bölümünde, `TS_TRANSFER` işlem türünü tanımlıyoruz. Bunu açıklıyoruz:




- Meta verisi yoktur;
- Global State'i (Genesis'da zaten tanımlanmış olan) değiştirmez;
- Girdi olarak bir veya daha fazla `OS_ASSET` alır. Bu, mevcut Sahip Olunan Durumları harcaması gerektiği anlamına gelir;
- En az bir yeni `OS_ASSET` oluşturur (`assignments`) (başka bir deyişle, alıcı veya alıcılar belirteçleri alır);
- Yeni bir Valency oluşturmaz.


Bu, UTXO'de jetonları tüketen, daha sonra alıcılar lehine yeni Sahipli Durumlar yaratan ve böylece girdiler ve çıktılar arasındaki toplam miktarın eşitliğini koruyan temel bir transferin davranışını modeller.




- (9) - **AluVM senaryosu ve Giriş Noktaları** (Fransızca)


Son olarak, bir AluVM betiği bildiriyoruz (`Script::AluVM(AluScript { ... })`). Bu komut dosyası şunları içerir:




- Doğrulama sırasında kullanılacak bir veya daha fazla harici kütüphane (`libs`);
- AluVM kodunda, Genesis'in (`ValidateGenesis`) ve beyan edilen her Geçişin (`ValidateTransition(TS_TRANSFER)`) doğrulanmasına karşılık gelen fonksiyon ofsetlerini işaret eden giriş noktaları.


Bu doğrulama kodu Business Logic'ün uygulanmasından sorumludur. Örneğin, kontrol edecektir:




- Genesis sırasında `GS_ISSUED_SUPPLY` değerinin aşılmaması;
- TS_TRANSFER` için `girişler` (harcanan jetonlar) toplamının `atamalar` (alınan jetonlar) toplamına eşit olması.


Bu kurallara uyulmaması halinde geçiş geçersiz sayılacaktır.


Bu "*Şişirilebilir Olmayan Değiştirilebilir Varlık*" örneği Schema bize basit bir RGB fungible token Contract yapısını daha iyi anlamamızı sağlar. Veri tanımı (Global ve Sahip Olunan Durumlar), işlem bildirimi (Genesis, Geçişler, Uzantılar) ve doğrulama uygulaması (AluVM komut dosyaları) arasındaki ayrımı açıkça görebiliriz. Bu model sayesinde, bir token klasik bir değiştirilebilir token gibi davranır, ancak istemci tarafında doğrulanmış olarak kalır ve kodunu yürütmek için On-Chain altyapısına bağlı değildir. Sadece kriptografik taahhütler Bitcoin Blockchain'e bağlanır.


### Interface


Interface, bir Contract'yi hem kullanıcılar (insan okuması) hem de portföyler (yazılım okuması) tarafından okunabilir ve manipüle edilebilir hale getirmek için tasarlanmış Layer'dir. Bu nedenle Interface, nesne yönelimli bir programlama dilindeki (Java, Rust özelliği, vb.) bir Interface ile karşılaştırılabilir bir rol oynar, çünkü Business Logic'in iç ayrıntılarını ortaya çıkarmak zorunda kalmadan bir Contract'nin işlevsel yapısını ortaya çıkarır ve netleştirir.


Tamamen bildirimsel olan ve olduğu gibi kullanılması zor olan ikili bir dosyaya derlenen Schema'in aksine, Interface gerekli okuma anahtarlarını sağlar:




- Contract'de yer alan Küresel Durumları ve Sahip Olunan Durumları listeleyin ve açıklayın;
- Görüntülenebilmeleri için her bir alanın adlarına ve değerlerine erişin (örneğin, bir token için ticker'ını, maksimum miktarını vb. öğrenin);
- Verileri anlaşılabilir isimlerle ilişkilendirerek Contract İşlemlerini (Genesis, State Transition veya State Extension) yorumlayın ve oluşturun (örneğin, ikili bir tanımlayıcı yerine açıkça "miktar" belirterek bir transfer gerçekleştirin).


![RGB-Bitcoin](assets/fr/073.webp)


Interface sayesinde, örneğin bir Wallet'da alanları manipüle etmek yerine "token sayısı", "varlık adı" gibi etiketleri doğrudan manipüle eden kod yazabilirsiniz. Bu şekilde, bir Contract'u yönetmek daha sezgisel hale gelir. Bu şekilde, Contract yönetimi daha sezgisel hale gelir.


#### Genel operasyon


Bu yöntemin birçok avantajı vardır:




- **Standartlaştırma:**


Aynı tip Contract, birkaç Wallet uygulaması arasında paylaşılan standart bir Interface tarafından desteklenebilir. Bu, uyumluluğu ve kodun yeniden kullanımını kolaylaştırır.




- **Schema ve Interface arasında net ayrım:**


RGB tasarımında, Schema (Business Logic) ve Interface (sunum ve manipülasyon) iki bağımsız varlıktır. Contract mantığını yazan geliştiriciler, ergonomi veya veri gösterimi konusunda endişelenmeden Schema'a konsantre olabilirken, başka bir ekip (veya aynı ekip, ancak farklı bir zaman çizelgesinde) Interface'yi geliştirebilir.




- **Esnek evrim:**


Interface, varlık verildikten sonra Contract'ün kendisini değiştirmek zorunda kalmadan değiştirilebilir veya eklenebilir. Bu, Interface'ün (genellikle yürütme koduyla karışık) Blockchain'de dondurulduğu bazı On-Chain Smart contract sistemlerinden önemli bir farktır.




- Çoklu Interface özelliği


Aynı Contract, farklı ihtiyaçlara göre uyarlanmış farklı Arayüzler aracılığıyla açığa çıkarılabilir: son kullanıcı için basit bir Interface, karmaşık yapılandırma işlemlerini yönetmesi gereken düzenleyici için daha gelişmiş başka bir Interface. Wallet daha sonra kullanımına bağlı olarak hangi Interface'nin içe aktarılacağını seçebilir.


![RGB-Bitcoin](assets/fr/074.webp)


Uygulamada, Wallet bir RGB Contract aldığında (bir `.RGB` veya `.rgba` dosyası aracılığıyla), aynı zamanda derlenmiş olan ilişkili Interface'yi de alır. Çalışma zamanında, Wallet örneğin




- Okunamayan sayısal bir tanımlayıcı yerine kullanıcı Interface üzerinde Ticker, İlk Miktar, İhraç Tarihi vb. görüntülemek için devletler listesine göz atın ve adlarını okuyun;
- Açık parametre adları kullanarak bir işlem (transfer gibi) oluşturun: `assignments { OS_ASSET => 1 }` yazmak yerine, kullanıcıya bir formda bir "Amount" alanı sunabilir ve bu bilgiyi Contract tarafından beklenen kesin olarak yazılmış alanlara çevirebilir.


#### Ethereum ve diğer sistemlerden farkı


Ethereum'da Interface (ABI, *Application Binary Interface* ile tanımlanır) genellikle On-Chain saklı kodundan (Smart contract) türetilir. Contract'un kendisine dokunmadan Interface'in belirli bir bölümünü değiştirmek maliyetli veya karmaşık olabilir. Ancak, RGB tamamen off-chain mantığına dayanır ve veriler Bitcoin'deki *commitment'lara* bağlanır. Bu tasarım, iş kurallarının doğrulanması Schema ve referans alınan AluVM kodunda kaldığından, Interface'in (veya uygulamasının) Contract'un temel güvenliğini etkilemeden değiştirilmesini mümkün kılar.


#### Interface derleme


Schema'de olduğu gibi, Interface kaynak kodunda (genellikle Rust'da) tanımlanır ve bir `.RGB' veya `.rgba' dosyasına derlenir. Bu ikili dosya Wallet için gerekli tüm bilgileri içerir:




- Alanları ada göre tanımlayın;
- Her bir alanı (ve değerini) Contract'de tanımlanan katı sistem tipine bağlayın;
- İzin verilen farklı işlemleri ve bunların nasıl inşa edileceğini bilin.


Interface içe aktarıldıktan sonra Wallet, Contract'ü doğru bir şekilde görüntüleyebilir ve kullanıcıya etkileşimler önerebilir.


### LNP/BP birliği tarafından standartlaştırılmış arayüzler


RGB ekosisteminde, bir Interface, bir Contract'nin verilerine ve işlemlerine okunabilir ve manipüle edilebilir bir anlam vermek için kullanılır. Interface böylece Business Logic'i dahili olarak tanımlayan Schema'i tamamlar (katı tipler, doğrulama komut dosyaları, vb.). Bu bölümde, yaygın Contract türleri (değiştirilebilir belirteçler, NFT, vb.) için LNP/BP birliği tarafından geliştirilen standart Arayüzlere bir göz atacağız.


Bir hatırlatma olarak, her bir Interface'in Wallet tarafında bir Contract'in nasıl görüntüleneceğini ve manipüle edileceğini tanımlaması, alanları açıkça adlandırması (örneğin `spec`, `ticker`, `issuedSupply`...) ve olası işlemleri tanımlamasıdır (örneğin `Transfer`, `Burn`, `Rename`...). Birkaç Arayüz halihazırda çalışır durumdadır, ancak gelecekte daha da fazlası olacaktır.


#### Kullanıma hazır bazı arayüzler


**RGB20**, Ethereum'un ERC20 standardıyla karşılaştırılabilecek, değiştirilebilir varlıklar için Interface'tür. Bununla birlikte, daha kapsamlı işlevsellik sunarak bir adım daha ileri gider:




- Örneğin, ihraç edildikten sonra varlığı yeniden adlandırabilme (*etiket* veya tam ad değişikliği) veya hassasiyetini ayarlayabilme (*hisse senedi bölünmeleri*);
- Ayrıca, ihraççıya belirli koşullar altında varlıkları yok etme ve ardından yeniden yaratma yetkisi vermek için ikincil yeniden ihraç (sınırlı veya sınırsız) ve yakma ve ardından değiştirme mekanizmalarını da tanımlayabilir;


Örneğin, RGB20 Interface, şişirilemeyen bir başlangıç Supply uygulayan **Şişirilemeyen Varlık (NIA) şemasına** veya gerektiğinde diğer daha gelişmiş şemalara bağlanabilir.


**RGB21**, NFT tipi sözleşmelerle veya daha geniş anlamda, dijital medyanın temsili (görüntüler, müzik vb.) gibi herhangi bir benzersiz dijital içerikle ilgilidir. Tek bir varlığın ihraç ve transferini tanımlamanın yanı sıra, aşağıdaki gibi özellikleri de içerir:




- Bir dosyanın (16 MB'a kadar) Contract'ya doğrudan dahil edilmesi için entegre destek (istemci tarafından alım için);
- Sahibinin bir NFT'nin geçmiş Ownership'sini kanıtlamak için geçmişe bir "*gravür*" girme olasılığı.


**RGB25**, değiştirilebilir ve değiştirilemez yönleri birleştiren hibrit bir standarttır. Tek bir kök varlıkla bağlantıyı korurken bir mülkü bölmek istediğiniz gayrimenkul tokenizasyonu gibi kısmen değiştirilebilir varlıklar için tasarlanmıştır (başka bir deyişle, değiştirilebilir olmayan bir eve bağlı bir evin değiştirilebilir parçalarına sahipsiniz). Teknik olarak bu Interface, orijinal varlığı izlerken bölme kavramını dikkate alan **Collectible Fungible Asset (CFA)** Schema ile bağlantılı olabilir.


#### Geliştirilmekte olan arayüzler


Daha özel kullanımlar için başka Arayüzler de planlanmaktadır, ancak henüz mevcut değildir:




- **RGB22**, RGB ekosistemindeki tanımlayıcıları ve On-Chain profillerini yönetmek için dijital kimliklere adanmıştır;
- **RGB23**, gelişmiş zaman damgası için, *Opentimestamps*'ın bazı fikirlerini kullanarak, ancak izlenebilirlik özellikleriyle;
- **RGB24**, *Ethereum Name Service* benzeri merkezi olmayan bir alan adı sisteminin (DNS) eşdeğerini hedeflemektedir;
- **RGB26**, DAO'ları (*Merkezi Olmayan Otonom Organizasyon*) daha karmaşık bir biçimde (yönetişim, oylama vb.) yönetmek için tasarlanmıştır;
- **RGB30**, RGB20'ye çok benzer ancak merkezi olmayan ilk ihracı dikkate alma ve Devlet Uzantılarını kullanma özelliğine sahiptir. Bu, yeniden ihracı birkaç kuruluş tarafından yönetilen veya daha ince koşullara tabi olan varlıklar için kullanılacaktır.


Elbette, bu kursa başvurduğunuz tarihe bağlı olarak, bu arayüzler halihazırda çalışır durumda ve erişilebilir olabilir.


#### Interface örneği


Bu Rust kod parçacığı bir [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (değiştirilebilir varlık) göstermektedir. Bu kod, standart RGB kütüphanesindeki `rgb20.rs` dosyasından alınmıştır. Bir Interface'ün yapısını ve bir yandan Business Logic (Schema'te tanımlanmıştır) ile diğer yandan cüzdanlara ve kullanıcılara maruz kalan işlevler arasında nasıl bir köprü sağladığını anlamak için buna bir göz atalım.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());

Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


Bu Interface'da, Schema yapısıyla benzerlikler görüyoruz: Global State, Sahip Olunan Durumlar, Contract İşlemleri (Genesis ve Geçişler) ve hata işlemenin bir bildirimini buluyoruz. Ancak Interface, bir Wallet veya başka bir uygulama için bu Elements'in sunumuna ve manipülasyonuna odaklanır.


Schema ile arasındaki fark türlerin doğasında yatmaktadır. Schema katı tipler (`FungibleType::Unsigned64Bit` gibi) ve daha teknik tanımlayıcılar kullanır. Interface alan adları, makrolar (`fname!()`, `tn!()`) ve argüman sınıflarına referanslar (`ArgSpec`, `OwnedIface::Rights`...) kullanır. Buradaki amaç, Wallet için Elements'nın işlevsel olarak anlaşılmasını ve düzenlenmesini kolaylaştırmaktır.


Buna ek olarak, Interface, nihai olarak doğrulanmış istemci tarafı mantığı ile tutarlı kaldığı sürece, temel Schema'a ek işlevsellik (örneğin bir `burnEpoch' hakkının yönetimi) getirebilir. Schema'daki AluVM "script" bölümü kriptografik geçerliliği sağlarken, Interface kullanıcının (veya Wallet) bu durumlar ve geçişlerle nasıl etkileşime girdiğini açıklar.


#### Global State ve Atamalar


Global_state` bölümünde `spec` (varlık açıklaması), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply` gibi alanlar bulunur. Bunlar Wallet'ün okuyabileceği ve sunabileceği alanlardır. Örneğin:




- spec` token yapılandırmasını görüntüleyecektir;
- `issuedSupply` veya `burnedSupply` bize verilen veya yakılan toplam jeton sayısını vb. verir.


Atamalar bölümünde, çeşitli roller veya haklar tanımlarız. Örneğin:




- `assetOwner` belirteçlerin tutulmasına karşılık gelir (değiştirilebilir *Owned State*);
- burnRight` token yakma yeteneğine karşılık gelir;
- updateRight` varlığı yeniden adlandırma hakkına karşılık gelir.


Public` veya `private` anahtar sözcüğü (örneğin `AssignIface::public(...)`) bu durumların görünür (`public`) veya gizli (`private`) olduğunu gösterir. Request::NoneOrMore`, `Req::Optional` ise beklenen oluşumu belirtir.


#### Genesis ve geçişler


Genesis` kısmı varlığın nasıl başlatıldığını açıklar:




- Spec`, `data`, `created`, `issuedSupply` alanları zorunludur (`ArgSpec::required()`);
- AssetOwner` gibi atamalar birden fazla kopyada bulunabilir (`ArgSpec::many()`) ve tokenların birden fazla ilk sahibine dağıtılmasına izin verir;
- Genesis'a `inflationAllowance` veya `burnEpoch` gibi alanlar dahil edilebilir (veya edilmeyebilir).


Ardından, her Geçiş için (`Transfer`, `Issue`, `Burn`...), Interface işlemin girdi olarak hangi alanları beklediğini, işlemin çıktı olarak hangi alanları üreteceğini ve oluşabilecek hataları tanımlar. Örneğin:


**Geçiş:**




- Girdiler: `previous` → bir `assetOwner` olmalıdır;
- Atamalar: faydalanıcı` → yeni bir `varlıkSahibi` olacaktır;
- Hata: `NON_EQUAL_AMOUNTS` (Wallet böylece giriş toplamının çıkış toplamına karşılık gelmediği durumları idare edebilecektir).


**Geçiş `Sorunu`:**




- Ek emisyon mutlaka etkinleştirilmediğinden isteğe bağlıdır (`optional: true`);
- Girdiler: `used` → bir `inflationAllowance`, yani daha fazla jeton ekleme izni;
- Atamalar: `yararlanıcı` (alınan yeni jetonlar) ve `gelecek` (kalan `enflasyon ödeneği`);
- Olası hatalar: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, vb.


**Yanık geçişi:**




- Girdiler: `used` → a `burnRight`;
- Globals: `burnedSupply` gerekli;
- Görevler: `future` → her şeyi yakmadıysak `burnRight`ın olası bir devamı;
- Hatalar: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.


Bu nedenle her işlem bir Wallet için okunabilir bir şekilde tanımlanmıştır. Bu, kullanıcının açıkça görebileceği grafiksel bir Interface görüntülemeyi mümkün kılar: "Yakma hakkına sahipsiniz. Belirli bir miktar yakmak ister misiniz? Kod, bir `burnedSupply` alanını doldurmayı ve `burnRight`ın geçerli olup olmadığını kontrol etmeyi bilir.


Özetle, ne kadar eksiksiz olursa olsun bir Interface'ün tek başına Contract'in iç mantığını tanımlamadığını akılda tutmak önemlidir. İşin kalbi, katı tipler, Genesis yapısı, geçişler ve benzerlerini içeren **Schema** tarafından yapılır. Interface basitçe bu Elements'yı bir uygulamada kullanılmak üzere daha sezgisel ve adlandırılmış bir şekilde ortaya çıkarır.


RGB'in modülerliği sayesinde, Interface tüm Contract'u yeniden yazmak zorunda kalmadan yükseltilebilir (örneğin, bir `Rename` geçişi ekleyerek, bir alanın görüntüsünü düzelterek, vb. Bu Interface kullanıcıları, `.RGB` veya `.rgba` dosyasını günceller güncellemez bu iyileştirmelerden hemen faydalanabilirler.


Ancak bir Interface bildirdikten sonra, bunu ilgili Schema'e bağlamanız gerekir. Bu, her bir adlandırılmış alanın (örneğin `fname!("assetOwner")`) Schema'te tanımlanan katı kimliğe (örneğin `OS_ASSET`) nasıl eşleneceğini belirten ***Interface Implementation*** aracılığıyla yapılır. Bu, örneğin, bir Wallet bir `burnRight` alanını manipüle ettiğinde, bunun Schema'te belirteçleri yakma yeteneğini tanımlayan durum olmasını sağlar.


### Interface Implementation


RGB mimarisinde, her bir bileşenin (Schema, Interface, vb.) bağımsız olarak geliştirilebileceğini ve derlenebileceğini gördük. Bununla birlikte, bu farklı yapı taşlarını birbirine bağlayan vazgeçilmez bir unsur vardır: ***Interface Implementation***. Bu, Schema'de (Business Logic tarafında) tanımlanan tanımlayıcıları veya alanları Interface'da (sunum ve kullanıcı etkileşimi tarafında) bildirilen adlarla açıkça eşleştiren şeydir. Böylece bir Wallet bir Contract yüklediğinde, hangi alanın neye karşılık geldiğini ve Interface'da adlandırılan bir işlemin Schema'in mantığıyla nasıl ilişkili olduğunu tam olarak anlayabilir.


Önemli bir nokta, Interface Implementation'ün tüm Schema işlevlerini veya tüm Interface alanlarını ortaya çıkarması gerekmediğidir: bir alt küme ile sınırlandırılabilir. Pratikte bu, Schema'nın belirli yönlerini kısıtlamayı veya filtrelemeyi mümkün kılar. Örneğin, dört işlem türüne sahip bir Schema'nız olabilir, ancak belirli bir bağlamda bunlardan yalnızca ikisini eşleyen bir Uygulama Interface'iniz olabilir. Tersine, bir Interface ek uç noktalar öneriyorsa, bunları burada uygulamamayı seçebiliriz.


İşte bir *Şişirilemeyen Varlık* (NIA) Schema'u RGB20 Interface ile ilişkilendirdiğimiz klasik bir Interface Implementation örneği:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();

IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


Bu Uygulamada Interface:




- Nia_schema()` aracılığıyla Schema'e ve `Rgb20::iface()` aracılığıyla Interface'ye açıkça referans veriyoruz. Schema.schema_id()` ve `iface.iface_id()` çağrıları derleme tarafında Anchor Interface Implementation için kullanılır (bu iki bileşenin kriptografik tanımlayıcılarını ilişkilendirir);
- Schema Elements ve Interface Elements arasında bir eşleme kurulur. Örneğin, Schema'deki `GS_NOMINAL` alanı Interface tarafındaki `"spec"` dizesine bağlanır (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Aynı şeyi, Interface'te `"Transfer"` dizesine bağladığımız `TS_TRANSFER` gibi işlemler için de yaparız...;
- Bu NIA Contract'in bu özellikleri kullanmadığı gerçeğini yansıtan hiçbir değerlik (`valencies: none!()`) veya uzantı (`extensions: none!()`) olmadığını görebiliriz.


Derlemeden sonra sonuç, Schema ve Interface'a ek olarak Wallet'e aktarılacak ayrı bir `.RGB' veya `.rgba' dosyasıdır. Böylece yazılım, bu NIA Contract'i (mantığı Schema tarafından tanımlanan) "RGB20" Interface'a (insan isimleri ve değiştirilebilir belirteçler için bir etkileşim modu sağlayan) somut olarak nasıl bağlayacağını bilir ve bu Interface Implementation'u ikisi arasında bir geçit olarak uygular.


#### Neden ayrı Interface Implementation?


Ayırma esnekliği artırır. Tek bir Schema, her biri farklı bir işlevler kümesini eşleyen birkaç farklı Interface Uygulamasına sahip olabilir. Dahası, Interface Implementation'nın kendisi, Schema veya Interface'de bir değişiklik gerektirmeden gelişebilir veya yeniden yazılabilir. Bu, RGB'un modülerlik ilkesini korur: her bileşen (Schema, Interface, Interface Implementation), protokol tarafından dayatılan uyumluluk kurallarına uyulduğu sürece (aynı tanımlayıcılar, türlerin tutarlılığı, vb.) bağımsız olarak sürümlendirilebilir ve güncellenebilir.


Somut kullanımda, Wallet bir Contract yüklediğinde, yüklemelidir:




- Derlenmiş **Schema**'ü yükleyin (Business Logic'nin yapısını bilmek için);
- Derlenmiş **Interface** yükleyin (adları ve kullanıcı tarafı işlemlerini anlamak için);
- Derlenmiş **Interface Implementation**'i yükleyin (Schema mantığını Interface adlarına, işlem işlem, alan alan bağlamak için).


Bu modüler mimari, aşağıdaki gibi kullanım senaryolarını mümkün kılar:




- Belirli kullanıcılar için belirli işlemleri sınırlayın: örneğin yakma veya güncelleme işlevleri sunmadan yalnızca temel aktarımlara erişim sağlayan kısmi bir Interface Uygulaması sunun;
- Değişiklik sunumu: Interface'deki bir alanı yeniden adlandıran veya Contract'in temelini değiştirmeden farklı bir şekilde eşleyen bir Interface Implementation tasarlayın;
- Çoklu şemaları destekleme: Bir Wallet, yapılarının uyumlu olması koşuluyla, farklı şemaları (farklı token mantıkları) işlemek için aynı Interface tipi için birden fazla Interface Uygulaması yükleyebilir.


Bir sonraki bölümde, Contract transferinin nasıl çalıştığına ve RGB faturalarının nasıl oluşturulduğuna bakacağız.


## Contract transferleri


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


Bu bölümde, RGB ekosistemindeki bir Contract transfer sürecini analiz edeceğiz. Bunu göstermek için, bir Exchange varlığını RGB yapmak isteyen olağan kahramanlarımız olan Alice ve Bob'e bir göz atacağız. Ayrıca pratikte nasıl çalıştığını görmek için `RGB` komut satırı aracından bazı komut alıntıları göstereceğiz.


### RGB Contract transferini anlama


Alice ve Bob arasındaki bir transfer örneğini ele alalım. Bu örnekte, Bob'ün RGB'i kullanmaya yeni başladığını, Alice'un ise Wallet'inde zaten RGB varlıklarını tuttuğunu varsayıyoruz. Bob'ün ortamını nasıl kurduğunu, ilgili Contract'yı nasıl içe aktardığını, ardından Alice'dan bir aktarım talebinde bulunduğunu ve son olarak Alice'un Bitcoin Blockchain üzerinde gerçek işlemi nasıl gerçekleştirdiğini göreceğiz.


#### 1) RGB Wallet'nin Kurulması


Her şeyden önce, Bob'in bir RGB Wallet, yani protokolle uyumlu bir yazılım yüklemesi gerekir. Bu başlangıçta herhangi bir sözleşme içermez. Bob'in ayrıca şunlara ihtiyacı olacaktır:




- UTXO'larınızı yönetmek için bir Bitcoin Wallet;
- UTXO'larınızı tanımlayabilmeniz ve işlemlerinizi ağ üzerinde yayabilmeniz için bir Bitcoin düğümüne (veya bir Electrum sunucusuna) bağlantı.


Bir hatırlatma olarak, RGB'deki **Sahip Olunan Durumlar** Bitcoin UTXO'larına atıfta bulunur. Bu nedenle, RGB verilerine işaret eden kriptografik taahhütleri (`Tapret` veya `Opret`) içeren bir Bitcoin işleminde UTXO'ları her zaman yönetebilmeli ve harcayabilmeliyiz.


#### 2) Contract bilgi edinimi


Bob'in daha sonra ilgilendiği Contract verilerini alması gerekir. Bu veriler herhangi bir kanal üzerinden dolaşabilir: web sitesi, e-posta, mesajlaşma uygulaması... Pratikte, bunlar bir ***Consignment***, yani aşağıdakileri içeren küçük bir veri paketi içinde gruplandırılır:




- Contract'nın başlangıç durumunu tanımlayan **Genesis**;
- Business Logic'i açıklayan **Schema** (katı tipler, doğrulama komut dosyaları, vb.);
- Layer sunumunu tanımlayan **Interface** (alan adları, erişilebilir işlemler);
- Schema'ü somut olarak Interface'e bağlayan **Interface Implementation**.


![RGB-Bitcoin](assets/fr/075.webp)


Her bir bileşen genellikle 200 bayttan daha az ağırlığa sahip olduğundan toplam boyut genellikle birkaç kilobayt mertebesindedir. Bu Consignment'yı Base58'de, sansüre dayanıklı kanallar aracılığıyla (örneğin Nostr veya Lightning Network aracılığıyla) veya bir QR kodu olarak yayınlamak da mümkün olabilir.


#### 3) Contract içe aktarma ve doğrulama


Bob Consignment'i aldıktan sonra, bunu RGB Wallet'a aktarır. Bu daha sonra




- Genesis ve Schema'ün geçerli olup olmadığını kontrol edin;
- Interface ve Interface Implementation'ü yükleyin;
- İstemci tarafı verilerinizi güncelleyin Stash.


Bob artık varlığı Wallet'sinde görebilir (henüz sahibi olmasa bile) ve hangi alanların mevcut olduğunu, hangi işlemlerin mümkün olduğunu anlayabilir... Daha sonra, transfer edilecek varlığa gerçekten sahip olan bir kişiyle iletişime geçmesi gerekir. Bizim örneğimizde bu kişi Alice'dir.


Belirli bir RGB varlığının kimde olduğunu bulma süreci, bir Bitcoin mükellefi bulmaya benzer. Bu bağlantının ayrıntıları kullanıma bağlıdır (pazar yerleri, özel sohbet kanalları, faturalama, mal ve hizmet satışı, maaş...).


#### 4) Bir Invoice düzenlenmesi


Bir RGB varlığının transferini başlatmak için, Bob önce bir Invoice yayınlamalıdır. Bu Invoice aşağıdakiler için kullanılır:




- Alice'ye gerçekleştirilecek işlemin türünü söyleyin (örneğin, RGB20 Interface'dan bir `Transfer');
- Alice'a Bob'in *Seal Definition* adresini (yani varlığı almak istediği UTXO'yi) verin;
- Gerekli aktif bileşen miktarını belirtin (örn. 100 birim).


Bob komut satırında `RGB` aracını kullanır. Diyelim ki `ContractId`si bilinen bir token`den 100 birim istiyor, `Tapret`e güvenmek istiyor ve UTXO`ünü (`456e3..dfe1:0`) belirtiyor:


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


Bu bölümün sonunda RGB faturalarının yapısına daha yakından bakacağız.


#### 5) Invoice aktarımı


Oluşturulan Invoice (örneğin URL olarak: `RGB:2WBcas9.../RGB20/100+utxob:...`) Alice'ın aktarımı hazırlamak için ihtiyaç duyduğu tüm bilgileri içerir. Consignment'de olduğu gibi, kompakt bir şekilde kodlanabilir (Base58 veya başka bir format) ve bir mesajlaşma uygulaması, e-posta, Nostr...


![RGB-Bitcoin](assets/fr/076.webp)


#### 6) Alice tarafında işlem hazırlığı


Alice, Bob'nin Invoice'sını alır. RGB Wallet'sinde, transfer edilecek varlığı içeren bir Stash vardır. Varlığı içeren UTXO'i harcamak için, önce sahip olduğu UTXO'i kullanarak bir PSBT (*Partially Signed Bitcoin Transaction*), yani tamamlanmamış bir Bitcoin işlemi generate yapmalıdır:


```bash
alice$ wallet construct tx.psbt
```


Bu temel işlem (şimdilik imzasız) Bob'e transferle bağlantılı kriptografik Commitment'ü Anchor yapmak için kullanılacaktır. Alice'nın UTXO'si böylece harcanacak ve çıktıya Bob için `Tapret` veya `Opret` Commitment'ü yerleştireceğiz.


#### 7) Consignment transferinin oluşturulması


Ardından, Alice komutu aracılığıyla ***Terminal Consignment*** (bazen "Consignment aktarımı" olarak da adlandırılır) oluşturur:


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


Bu yeni `Consignment.RGB` dosyası şunları içerir:




- Varlığı günümüze kadar doğrulamak için gereken Durum Geçişlerinin tam geçmişi (Genesis'ten beri);
- Bob'un yayınladığı Invoice'ye göre, Alice'den Bob'a varlıkları aktaran yeni State Transition;
- Alice'ün Single-Use Seal'ini harcayan tamamlanmamış Bitcoin işlemi (*Witness Transaction*) (`tx.PSBT`), kriptografik Commitment'yi Bob'ya içerecek şekilde değiştirildi.


Bu aşamada, işlem henüz Bitcoin ağında yayınlanmamıştır. Consignment, varlığın meşruiyetini kanıtlamak için tüm geçmişi (*kanıt zinciri*) içerdiğinden, temel bir Consignment'den daha büyüktür.


#### 8) Bob, Consignment'u kontrol eder ve kabul eder


Alice bu **Terminal Consignment**'i Bob'e iletir. Bob daha sonra




- State Transition'ün geçerliliğini kontrol edin (geçmişin tutarlı olduğundan, Contract kurallarına uyulduğundan vb. emin olun);
- Yerel Stash'nıza ekleyin;
- Muhtemelen generate, incelendiğini ve onaylandığını kanıtlamak için Consignment üzerinde bir imza (`sig:...`) (bazen "*payslip*" olarak adlandırılır).


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/fr/077.webp)


#### 9) Seçenek: Bob onayı Alice'a geri gönderir (*payslip*)


Bob isterse bu imzayı Alice'e geri gönderebilir. Bu şunu gösterir:




- Geçişi geçerli olarak kabul eder;
- Bitcoin işleminin yayınlanmasını kabul ettiğini.


Bu zorunlu değildir, ancak Alice'e daha sonra devir konusunda herhangi bir anlaşmazlık yaşanmayacağına dair güvence sağlayabilir.


#### 10) Alice işlemi imzalar ve yayınlar


Alice o zaman:




- Bob'nin imzasını kontrol edin (`RGB check <sig>`);
- Hala bir PSBT olan *Witness Transaction*'u imzalayın (`Wallet işareti`);
- Witness Transaction'yi Bitcoin ağında yayınlayın (`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/fr/078.webp)


Onaylandıktan sonra, bu işlem transferin sonucuna işaret eder. Bob varlığın yeni sahibi olur: artık kontrol ettiği UTXO'yı işaret eden bir Owned State'ü vardır ve bu durum Commitment'in işlemdeki varlığı ile kanıtlanmıştır.


Özetlemek gerekirse, işte tam transfer süreci:


![RGB-Bitcoin](assets/fr/079.webp)


### RGB transferlerinin avantajları




- **Gizlilik**:


Yalnızca Alice ve Bob'nın tüm State Transition verilerine erişimi vardır. Bu bilgileri Blockchain dışında, sevkiyatlar yoluyla Exchange'e iletirler. Bitcoin işlemindeki kriptografik taahhütler varlığın türünü veya miktarını göstermez, bu da diğer On-Chain token sistemlerinden çok daha fazla gizliliği garanti eder.




- **Müşteri tarafı doğrulaması**:


Bob, *Consignment* ile Bitcoin Blockchain'deki *anchor*'ları karşılaştırarak aktarımın tutarlılığını kontrol edebilir. Üçüncü taraf doğrulamasına ihtiyacı yoktur. Alice, Blockchain'deki tüm geçmişi yayınlamak zorunda değildir, bu da temel protokol üzerindeki yükü azaltır ve gizliliği artırır.




- **Basitleştirilmiş atomiklik**:


Karmaşık değişimler (örneğin BTC ile bir RGB varlığı arasındaki atomik takaslar) tek bir işlem dahilinde gerçekleştirilebilir ve HTLC veya PTLC komut dosyalarına ihtiyaç duyulmaz. Anlaşma yayınlanmazsa, herkes UTXO'larını başka şekillerde yeniden kullanabilir.


### Transfer özet diyagramı


Faturalara daha detaylı bakmadan önce, bir RGB transferinin genel akışının özet bir diyagramını burada bulabilirsiniz:




- Bob bir RGB Wallet kurar ve ilk Contract Consignment'i elde eder;
- Bob, UTXO'e varlığın nereden alınacağını belirten bir Invoice yayınlar;
- Alice, Invoice'ü alır, PSBT'yı oluşturur ve Terminal Consignment'ü üretir;
- Bob bunu kabul eder, kontrol eder, verileri Stash'ye ekler ve gerekirse imzalar (*payslip*);
- Alice işlemi Bitcoin ağında yayınlar;
- İşlemin onaylanması transferi resmileştirir.


![RGB-Bitcoin](assets/fr/080.webp)


Transfer, RGB protokolünün tüm gücünü ve esnekliğini göstermektedir: istemci tarafında onaylanmış, Bitcoin Blockchain'ye minimal ve gizli bir şekilde sabitlenmiş ve protokolün en iyi güvenliğini koruyan (Double-spending riski yok) özel bir Exchange. Bu da RGB'yı, On-Chain programlanabilir blok zincirlerinden daha gizli ve ölçeklenebilir olan değer transferleri için umut verici bir ekosistem haline getirmektedir.


### Faturalar RGB


Bu bölümde, **faturaların** RGB ekosisteminde nasıl çalıştığını ve bir Contract ile işlemlerin (özellikle transferlerin) gerçekleştirilmesini nasıl sağladığını ayrıntılı olarak açıklayacağız. İlk olarak, kullanılan tanımlayıcılara, ardından bunların nasıl kodlandığına ve son olarak URL olarak ifade edilen bir Invoice'un yapısına (cüzdanlarda kullanım için yeterince kullanışlı bir format) bakacağız.


#### Tanımlayıcılar ve kodlama


Aşağıdaki Elements'in her biri için benzersiz bir tanımlayıcı tanımlanmıştır:




- Bir RGB Contract;
- Schema (Business Logic);
- Interface ve Interface Implementation;
- Varlıkları (tokenler, NFT, vb.),


Sistemin her bir bileşeninin ayırt edilebilir olması gerektiğinden bu benzersizlik çok önemlidir. Örneğin, bir Contract X başka bir Contract Y ile karıştırılmamalı ve iki farklı arayüz (örneğin RGB20 ve RGB21) farklı tanımlayıcılara sahip olmalıdır.


Bu tanımlayıcıları hem verimli (küçük boyutlu) hem de okunabilir hale getirmek için kullanıyoruz:




- Base58 kodlaması, kafa karıştırıcı karakterlerin (örneğin `0` ve `O` harfi) kullanımını önler ve nispeten kısa dizeler sağlar;
- Genellikle `RGB:` veya benzer bir URN şeklinde, tanımlayıcının niteliğini belirten bir önek.


Örneğin, bir `ContractId` aşağıdaki gibi bir şeyle temsil edilebilir:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


RGB:` öneki, bunun bir HTTP bağlantısı veya başka bir protokol değil, bir RGB tanımlayıcısı olduğunu onaylar. Bu önek sayesinde cüzdanlar dizeyi doğru şekilde yorumlayabilir.


#### Tanımlayıcı segmentasyonu


RGB tanımlayıcıları genellikle oldukça uzundur, çünkü temel (kriptografik) güvenlik 256 bit veya daha fazla alan gerektirebilir. İnsanların okumasını ve doğrulamasını kolaylaştırmak için, bu dizeleri bir tire (`-`) ile ayrılmış birkaç bloğa *parçalarız*. Yani, uzun, kesintisiz bir karakter dizisi yerine, onu daha kısa bloklara böleriz. Bu uygulama kredi kartı veya telefon numaraları için yaygındır ve doğrulama kolaylığı için burada da geçerlidir. Örneğin, bir kullanıcıya veya ortağa şu söylenebilir: "*Lütfen üçüncü bloğun `9GEgnyMj7`* olduğunu kontrol edin", tümünü bir kerede karşılaştırmak zorunda kalmak yerine. Son blok, bir hata veya yazım hatası tespit sistemine sahip olmak için genellikle bir **checksum** olarak kullanılır.


Örnek olarak, base58 kodlu ve bölümlenmiş bir `ContractId` olabilir:


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Tire işaretlerinin her biri dizeyi bölümlere ayırır. Bu kodun anlamını etkilemez, sadece sunumunu etkiler.


#### Faturalar için URL'leri kullanma


Bir RGB Invoice bir URL olarak sunulur. Bu, tıklanabileceği veya taranabileceği (QR kodu olarak) ve bir Wallet'ün bir işlem gerçekleştirmek için doğrudan yorumlayabileceği anlamına gelir. Bu basit etkileşim, çeşitli veri parçalarını kopyalayıp yazılımdaki farklı alanlara yapıştırmanız gereken diğer bazı sistemlerden farklıdır.


Değiştirilebilir bir token (örneğin bir RGB20 token) için bir Invoice şöyle görünebilir:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Bu URL'yi analiz edelim:




- gW-1888: **önek**: RGB protokolünü çağıran bir bağlantıyı gösterir (diğer bağlamlarda `http:` veya `Bitcoin:` ile benzerdir);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`: manipüle etmek istediğiniz token'un `ContractId`sini temsil eder;
- `/RGB20/100`: `RGB20` Interface'ın kullanıldığını ve varlıktan 100 birim talep edildiğini belirtir. Sözdizimi şöyledir: `/Interface/amount`;
- `+utxob:`**: alıcı UTXO (veya daha doğrusu Single-Use Seal'in tanımı) hakkındaki bilgilerin eklendiğini belirtir;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`: bu **blinded** UTXO (veya Seal Definition). Başka bir deyişle, Bob tam UTXO'ini maskelemiştir, bu nedenle gönderen (Alice) tam Address'ün ne olduğunu bilmemektedir. Sadece Bob tarafından kontrol edilen bir UTXO'e atıfta bulunan geçerli bir Seal olduğunu biliyor.


Her şeyin tek bir URL'ye sığması, kullanıcının hayatını kolaylaştırır: Wallet'de basit bir tıklama veya tarama ve işlem yürütülmeye hazırdır.


ContractId` yerine basit bir ticker`ın (örneğin `USDT`) kullanıldığı sistemler hayal edilebilir. Ancak bu büyük güven ve güvenlik sorunlarına yol açacaktır: bir ticker benzersiz bir referans değildir (birkaç sözleşme `USDT` olarak adlandırıldığını iddia edebilir). RGB ile benzersiz, kesin bir kriptografik tanımlayıcı istiyoruz. Bu nedenle, base58 ile kodlanmış ve bölümlere ayrılmış 256 bitlik dizginin benimsenmesi. Kullanıcı tam olarak kimliği `2WBcas9-yjz...` olan Contract'i manipüle ettiğini ve başka herhangi birini manipüle etmediğini bilir.


#### Ek URL parametreleri


URL'ye HTTP ile aynı şekilde ek parametreler de ekleyebilirsiniz, örneğin:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- `?sig=...`: örneğin, bazı cüzdanların doğrulayabileceği Invoice ile ilişkili bir imzayı temsil eder;
- Bir Wallet bu imzayı yönetmiyorsa, bu parametreyi yok sayar.


RGB21 Interface üzerinden bir NFT durumunu ele alalım. Örneğin, şöyle olabilir:


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


İşte görüyoruz:




- gW-1906: **URL öneki**;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`: **Contract KİMLİK (NFT)**;
- **rGB21**: Değiştirilemeyen varlıklar (NFT) için Interface;
- **dbwzvSu-4BZU81jEp-...**: NFT'nin benzersiz kısmına açık bir referans, örneğin veri bloğunun (medya, meta veriler...) bir Hash'u;
- **`+utxob:egXsFnw-...`**: Seal Definition.


Fikir aynıdır: Wallet'in yorumlayabileceği, aktarılacak benzersiz varlığı açıkça tanımlayan benzersiz bir bağlantı iletmek.


#### URL üzerinden diğer işlemler


RGB URL'leri yalnızca bir transfer talebinde bulunmak için kullanılmaz. Ayrıca yeni tokenlar vermek (*issuance*) gibi daha gelişmiş işlemleri de kodlayabilirler. Örneğin:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Burada bulduk:




- `RGB:`: protokol;
- 2WBcas9-...`: Contract ID;
- `/RGB20/issue/100000`: ek 100.000 jeton oluşturmak için "*Issue*" geçişini çağırmak istediğinizi belirtir;
- `+utxob:`: Seal Definition.


Örneğin, Wallet şöyle yazabilir: "Benden `RGB20` Interface'den, filanca Contract'de, filanca Single-Use Seal yararına 100.000 birimlik bir `ihraç` işlemi gerçekleştirmem istendi."


Şimdi RGB programlamanın ana Elements'ine baktığımıza göre, sizi bir sonraki bölümde bir RGB Contract'nin nasıl hazırlanacağına götüreceğim.


## Akıllı sözleşmelerin hazırlanması


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


Bu bölümde, `RGB` komut satırı aracını kullanarak bir Contract yazmak için adım adım bir yaklaşım izleyeceğiz. Amaç, CLI'nin nasıl kurulacağını ve manipüle edileceğini, bir **Schema**'nın nasıl derleneceğini, **Interface** ve **Interface Implementation**'ün nasıl içe aktarılacağını ve ardından bir varlığın nasıl yayınlanacağını (*issue*) göstermektir. Ayrıca derleme ve durum doğrulama dahil olmak üzere temel mantığa da bakacağız. Bu bölümün sonunda, süreci yeniden üretebilmeli ve kendi RGB sözleşmelerinizi oluşturabilmelisiniz.


Bir hatırlatma olarak, RGB'nin iç mantığı, geliştiriciler olarak Client-side Validation kısmını yönetmek için projelerinize aktarabileceğiniz Rust kütüphanelerine dayanmaktadır. Buna ek olarak, LNP/BP Association ekibi diğer diller için bağlayıcılar üzerinde çalışmaktadır, ancak bu henüz sonuçlandırılmamıştır. Buna ek olarak, Bitfinex gibi diğer kuruluşlar kendi entegrasyon yığınlarını geliştirmektedir (bunlar hakkında kursun son 2 bölümünde konuşacağız). Bu nedenle, şimdilik, `RGB` CLI, nispeten cilasız kalsa bile resmi referanstır.


### RGB aracının kurulumu ve sunumu


Ana komut basitçe `RGB` olarak adlandırılır. Sözleşmeleri manipüle etmek, onları çağırmak, varlık vermek vb. için bir dizi alt komutla `git`i anımsatacak şekilde tasarlanmıştır. Bitcoin Wallet şu anda entegre edilmemiştir, ancak yakın bir sürümde (0.11) olacaktır. Bu sonraki sürüm, PSBT üretimi, imzalama için harici donanımla (örneğin bir Hardware Wallet) uyumluluk ve Sparrow gibi yazılımlarla birlikte çalışabilirlik dahil olmak üzere kullanıcıların cüzdanlarını (tanımlayıcılar aracılığıyla) doğrudan `RGB`dan oluşturmalarını ve yönetmelerini sağlayacaktır. Bu, tüm varlık ihracı ve transfer senaryosunu basitleştirecektir.


#### Kargo aracılığıyla kurulum


Aracı Rust ile kuruyoruz:


```bash
cargo install rgb-contracts --all-features
```


(Not: sandık `RGB-contracts` olarak adlandırılır ve yüklenen komut `RGB` olarak adlandırılır. Eğer `RGB` adında bir sandık zaten mevcutsa, bir çarpışma olmuş olabilir, bu nedenle bu isim verilmiştir)


Kurulum çok sayıda bağımlılığı derler (örneğin komut ayrıştırma, Electrum entegrasyonu, sıfır bilgi kanıtları yönetimi, vb.)


Kurulum tamamlandıktan sonra:


```bash
rgb
```


RGB` (argümanlar olmadan) çalıştırıldığında `arayüzler`, `Schema`, `ithalat`, `ihracat`, `sorun`, `Invoice`, `aktarım` gibi mevcut alt komutların bir listesi görüntülenir. Yerel depolama dizinini (tüm günlükleri, şemaları ve uygulamaları tutan bir Stash) değiştirebilir, ağı (Testnet, Mainnet) seçebilir veya Electrum sunucunuzu yapılandırabilirsiniz.


![RGB-Bitcoin](assets/fr/081.webp)


#### Kontrollere ilk genel bakış


Aşağıdaki komutu çalıştırdığınızda, varsayılan olarak bir `RGB20` Interface'in zaten entegre edildiğini göreceksiniz:


```bash
rgb interfaces
```


Bu Interface entegre edilmemişse, klonlayın:


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Derle:


```bash
cargo run
```


Ardından seçtiğiniz Interface'yi içe aktarın:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-Bitcoin](assets/fr/082.webp)


Öte yandan, bize henüz hiçbir Schema'nin yazılıma aktarılmadığı söylendi. Stash'te bir Contract de yoktur. Bunu görmek için şu komutu çalıştırın:


```bash
rgb schemata
```


Daha sonra belirli şemaları almak için depoyu klonlayabilirsiniz:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/fr/083.webp)


Bu depo, `src/` dizininde, şemaları tanımlayan birkaç Rust dosyası (örneğin `nia.rs`) içerir ("*Şişirilebilir Olmayan Varlık*" için NIA, "*Benzersiz Dijital Varlık*" için UDA, vb.) Derlemek için daha sonra çalıştırabilirsiniz:


```bash
cd rgb-schemata
cargo run
```


Bu, derlenen şemalara karşılık gelen birkaç `.RGB` ve `.rgba` dosyası oluşturur. Örneğin, `NonInflatableAsset.RGB` dosyasını bulacaksınız.


#### Schema ve Interface Implementation'nın içe aktarılması


Artık şemayı `RGB` içine aktarabilirsiniz:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/fr/084.webp)


Bu, onu yerel Stash'a ekler. Aşağıdaki komutu çalıştırırsak, Schema'un artık göründüğünü görürüz:


```bash
rgb schemata
```


### Contract oluşturma (yayınlama)


Yeni bir varlık oluşturmak için iki yaklaşım vardır:




- Ya Rust'te Schema alanlarını (Global State, Sahip Olunan Devletler, vb.) doldurarak bir Contract oluşturan ve bir `.RGB' veya `.rgba' dosyası üreten bir komut dosyası veya kod kullanırız;
- Veya token'nin özelliklerini açıklayan bir YAML (veya TOML) dosyası ile doğrudan `issue` alt komutunu kullanın.


Rust'te `examples' klasöründe, bir `ContractBuilder'ı nasıl oluşturduğunuzu, `Global State'i (varlık adı, ticker, Supply, tarih, vb.) nasıl doldurduğunuzu, Owned State'i (hangi UTXO'e atandığını) tanımladığınızı ve ardından tüm bunları bir Stash'e aktarabileceğiniz, doğrulayabileceğiniz ve içe aktarabileceğiniz bir *Contract Consignment* olarak derlediğinizi gösteren örnekler bulabilirsiniz.


Diğer yol ise `ticker`, `name`, `Supply` ve benzerlerini özelleştirmek için bir YAML dosyasını elle düzenlemektir. Dosyanın adının `RGB20-demo.yaml` olduğunu varsayalım. Belirtebilirsiniz:




- `spec`: ticker, isim, hassasiyet;
- `terms`: yasal bildirimler için bir alan;
- `issuedSupply`: verilen token miktarı;
- `assignments`: Single-Use Seal'u (*Seal Definition*) ve kilidi açılmış miktarı gösterir.


İşte oluşturulacak bir YAML dosyası örneği:


```yaml
interface: RGB20Fixed

globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000

assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-Bitcoin](assets/fr/085.webp)


Ardından komutu çalıştırmanız yeterlidir:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/fr/086.webp)


Benim durumumda, benzersiz Schema tanımlayıcısı (tek tırnak içine alınmalıdır) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` ve herhangi bir ihraççı koymadım. Yani benim siparişim:


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Schema kimliğini bilmiyorsanız, komutu çalıştırın:


```bash
rgb schemata
```


CLI yeni bir Contract'nin yayınlandığını ve Stash'e eklendiğini yanıtlar. Aşağıdaki komutu yazarsak, artık yeni yayınlanan komuta karşılık gelen ek bir Contract olduğunu görürüz:


```bash
rgb contracts
```


![RGB-Bitcoin](assets/fr/087.webp)


Ardından, bir sonraki komut global durumları (isim, ticker, Supply...) ve Sahip Olunan Durumların listesini, yani tahsisatları (örneğin, UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`de tanımlanan 1 milyon `PBN` jetonu) görüntüler.


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/fr/088.webp)


### Dışa aktarma, içe aktarma ve doğrulama


Bu Contract'yi diğer kullanıcılarla paylaşmak için, Stash'den a'ya aktarılabilir:


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/fr/089.webp)


MyContractPBN.RGB` dosyası başka bir kullanıcıya verilebilir, o da komutla Stash'una ekleyebilir:


```bash
rgb import myContractPBN.rgb
```


İçe aktarma sırasında, eğer basit bir *Contract Consignment* ise, "`Importing Consignment RGB`" mesajı alırız. Eğer daha büyük bir *State Transition Consignment* ise, komut farklı olacaktır (`RGB accept`).


Geçerliliği sağlamak için yerel doğrulama işlevini de kullanabilirsiniz. Örneğin, şunu çalıştırabilirsiniz:


```bash
rgb validate myContract.rgb
```


#### Stash kullanımı, doğrulama ve görüntüleme


Bir hatırlatma olarak, Stash şemaların, arayüzlerin, uygulamaların ve sözleşmelerin (Genesis + geçişler) yerel bir envanteridir. "Import" komutunu her çalıştırdığınızda, Stash'ye bir öğe eklersiniz. Bu Stash, komut ile ayrıntılı olarak görüntülenebilir:


```bash
rgb dump
```


![RGB-Bitcoin](assets/fr/090.webp)


Bu, generate tüm Stash'un ayrıntılarını içeren bir klasör olacaktır.


### Transfer ve PSBT


Bir transfer gerçekleştirmek için, `Tapret` veya `Opret` taahhütlerini yönetmek üzere yerel bir Bitcoin Wallet'yi manipüle etmeniz gerekecektir.


#### generate ve Invoice


Çoğu durumda, bir Contract'teki katılımcılar (örneğin Alice ve Bob) arasındaki etkileşim bir Invoice'nın oluşturulması yoluyla gerçekleşir. Alice, Bob'un bir şey yapmasını isterse (bir token transferi, bir yeniden ihraç, bir DAO'da bir eylem, vb), Alice, Bob'a talimatlarını detaylandıran bir Invoice oluşturur. Yani elimizde:




- **Alice** (Invoice'un ihraççısı);
- **Bob** (Invoice'yi alan ve yürüten kişi).


Diğer ekosistemlerin aksine, bir RGB Invoice ödeme kavramıyla sınırlı değildir. Contract ile bağlantılı herhangi bir talebi içerebilir: bir anahtarı iptal etme, oylama, bir NFT üzerinde bir gravür (*gravür*) oluşturma vb. İlgili işlem Contract Interface'te tanımlanabilir. İlgili işlem Contract Interface'te açıklanabilir.


Aşağıdaki komut bir RGB Invoice oluşturur:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Ile:




- `$Contract`: Contract tanımlayıcısı (*ContractId*);
- `$Interface`: kullanılacak Interface (örneğin `RGB20`);
- `$ACTION`: Interface'de belirtilen işlemin adı (basit bir değiştirilebilir token transferi için bu "Transfer" olabilir). Interface zaten varsayılan bir eylem sağlıyorsa, bunu buraya tekrar girmenize gerek yoktur;
- `$STATE`: aktarılacak durum verisi (örneğin, değiştirilebilir bir token aktarılıyorsa bir miktar jeton);
- `$Seal`: faydalanıcının (Alice'in) Single-Use Seal'sı, yani bir UTXO'a açık bir referans. Bob bu bilgiyi Witness Transaction'i oluşturmak için kullanacak ve ilgili çıktı daha sonra Alice'e ait olacaktır (*blinded UTXO* veya şifrelenmemiş biçimde).


Örneğin, aşağıdaki komutlarla


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI, generate ve Invoice gibi olacaktır:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Herhangi bir kanal (metin, QR kodu vb.) aracılığıyla Bob'e iletilebilir.


#### Transfer yapma


Bu Invoice'dan transfer etmek için:




- Bob (tokenları Stash'ında tutan) bir Bitcoin Wallet'a sahiptir. Gerekli RGB tokenlarının bulunduğu UTXO'ları ve para birimi (Exchange) için bir UTXO harcayan bir Bitcoin işlemi (PSBT şeklinde, örneğin `tx.PSBT`) hazırlaması gerekir;
- Bob aşağıdaki komutu yürütür:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Bu, aşağıdakileri içeren bir `Consignment.RGB` dosyası oluşturur:
 - Alice'e jetonların gerçek olduğunu kanıtlayan geçiş geçmişi;
 - Jetonları Alice'nin Single-Use Seal'una aktaran yeni geçiş;
 - Bir Witness Transaction (imzasız).
- Bob bu `Consignment.RGB` dosyasını Alice'e gönderir (e-posta, bir paylaşım sunucusu veya bir RGB-RPC protokolü, Storm, vb. ile);
- Alice, `Consignment.RGB`ı alır ve bunu kendi Stash'una kabul eder:


```bash
alice$ rgb accept consignment.rgb
```




- CLI geçişin geçerliliğini kontrol eder ve Alice'nin Stash'üne ekler. Geçersizse, komut ayrıntılı hata mesajlarıyla birlikte başarısız olur. Aksi takdirde başarılı olur ve örnek işlemin henüz Bitcoin ağında yayınlanmadığını bildirir (Bob, Alice'nin Green ışığını bekliyor);
- Onaylama yoluyla, `accept` komutu Alice'in *Consignment*'yi doğruladığını göstermek için Bob'a gönderebileceği bir imza (*payslip*) döndürür;
- Bob daha sonra Bitcoin işlemini imzalayabilir ve yayınlayabilir (`--publish`):


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Bu işlem onaylanır onaylanmaz On-Chain, varlığın Ownership'ünün Alice'ye aktarıldığı kabul edilir. İşlemin Mining'ini izleyen Alice'nin Wallet'sı, yeni Owned State'nin kendi Stash'inde göründüğünü görür.


Bir sonraki bölümde, RGB'in Lightning Network'a entegrasyonuna daha yakından bakacağız.


## Lightning Network üzerinde RGB


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


Bu bölümde, RGB varlıklarını (tokenlar, NFT'ler, vb.) off-chain ödeme kanalları aracılığıyla entegre etmek ve taşımak için Lightning Network içinde RGB'in nasıl kullanılabileceğini incelemeyi öneriyorum.


Temel fikir, RGB State Transition'nın (*State Transition*) bir Bitcoin işlemine işlenebilmesi ve bunun da Lightning kanalı kapatılana kadar off-chain olarak kalabilmesidir. Böylece, kanal her güncellendiğinde, yeni bir RGB State Transition yeni taahhüt işlemine dahil edilebilir ve bu da eski geçişi geçersiz kılar. Bu şekilde, Lightning kanalları RGB varlıklarını aktarmak için kullanılabilir ve geleneksel Lightning ödemeleriyle aynı şekilde yönlendirilebilir.


### Kanal oluşturma ve finansman


RGB varlıklarını taşıyan bir Lightning kanalı oluşturmak için iki Elements'a ihtiyacımız var:




- Kanalın 2/2 Multisig'sini (kanal için temel UTXO) oluşturmak için Bitcoin fonu;
- Varlıkları aynı Multisig'e gönderen RGB finansmanı.


Bitcoin açısından, fonlama işlemi yalnızca küçük miktarda Sats içerse bile, referans UTXO'ü tanımlamak için var olmalıdır (bu yalnızca gelecekteki Commitment işlemlerindeki her çıktının Dust sınırının üzerinde kalması meselesidir). Örneğin, Alice 10 bin Sats ve 500 USDT (RGB varlığı olarak ihraç edilmiştir) sağlamaya karar verebilir. Fonlama işleminde, RGB State Transition'yi sabitleyen bir Commitment (`Opret` veya `Tapret`) ekleriz.


![RGB-Bitcoin](assets/fr/091.webp)


Fonlama işlemi hazırlandıktan (ancak henüz yayınlanmadıktan) sonra, taraflardan herhangi birinin kanalı istediği zaman tek taraflı olarak kapatabilmesi için Commitment işlemleri oluşturulur. Bu işlemler Lightning'in klasik Commitment işlemlerine benzer, ancak yeni State Transition'e bağlı RGB Anchor (OP_RETURN veya Taproot) içeren ek bir çıktı ekleriz.


RGB State Transition daha sonra varlıkları fonun 2/2 Multisig'ünden Commitment Transaction'in çıkışlarına taşır. Bu sürecin avantajı, RGB durumunun güvenliğinin Lightning'in cezalandırma mekaniğine tam olarak uymasıdır: Bob eski bir kanal durumu yayınlarsa, Alice onu cezalandırabilir ve hem Sats hem de RGB jetonlarını geri kazanmak için çıktıyı harcayabilir. Bu nedenle teşvik, RGB varlıkları olmayan bir Lightning kanalından daha da güçlüdür, çünkü bir saldırgan sadece Sats'i değil, aynı zamanda kanalın RGB varlıklarını da kaybedebilir.


Alice tarafından imzalanan ve Bob'ye gönderilen bir Commitment Transaction bu nedenle şu şekilde görünecektir:


![RGB-Bitcoin](assets/fr/092.webp)


Bob tarafından imzalanan ve Alice'ye gönderilen Commitment Transaction'e eşlik eden Commitment Transaction ise şu şekilde görünecektir:


![RGB-Bitcoin](assets/fr/093.webp)


### Kanal güncellemesi


İki kanal katılımcısı arasında bir ödeme gerçekleştiğinde (veya varlık dağılımını değiştirmek istediklerinde), yeni bir çift Commitment işlemi oluştururlar. Ana rolü geçerli UTXO'ların oluşturulmasını sağlamak olduğundan, her bir çıktıdaki Sats'deki miktar uygulamaya bağlı olarak değişmeden kalabilir veya kalmayabilir. Öte yandan, OP_RETURN (veya Taproot) çıktısı, kanaldaki varlıkların yeni dağılımını temsil eden yeni RGB Anchor'yi içerecek şekilde değiştirilmelidir.


Örneğin, Alice kanaldaki Bob'ye 30 USDT aktarırsa, yeni State Transition Alice için 400 USDT ve Bob için 100 USDT bakiye yansıtacaktır. Taahhüt işlemi, bu geçişi içerecek şekilde OP_RETURN/Taproot Anchor'e eklenir (veya Anchor tarafından değiştirilir). RGB'in bakış açısından, geçişin girdisinin ilk Multisig (kanal kapanana kadar On-Chain varlıklarının fiilen tahsis edildiği yer) olarak kaldığını unutmayın. Karar verilen yeniden dağıtıma bağlı olarak yalnızca RGB çıktıları (tahsisler) değişir.


Commitment Transaction tarafından imzalanan Alice, Bob tarafından dağıtılmaya hazır:


![RGB-Bitcoin](assets/fr/094.webp)


Commitment Transaction, Bob tarafından imzalandı, Alice tarafından dağıtılmaya hazır:


![RGB-Bitcoin](assets/fr/095.webp)


### HTLC yönetimi


Gerçekte, Lightning Network ödemelerin HTLC'ler (*Hashed Time-Locked Contracts*) kullanılarak birden fazla kanal üzerinden yönlendirilmesini sağlar. RGB'da da durum aynıdır: kanaldan geçen her ödeme için, taahhüt işlemine bir HTLC çıktısı eklenir ve bu HTLC'ye bağlı bir RGB tahsisi yapılır. Böylece, HTLC çıktısını harcayan kişi (sır sayesinde veya zaman kilidinin sona ermesinden sonra) hem Sats hem de ilişkili RGB varlıklarını geri alır. Öte yandan, hem Sats hem de RGB varlıkları açısından yolda yeterli paraya sahip olmanız gerektiği açıktır.


![RGB-Bitcoin](assets/fr/096.webp)


Bu nedenle RGB'in Lightning üzerindeki çalışması, Lightning Network'nin çalışmasıyla paralel olarak düşünülmelidir. Bu konuyu daha derinlemesine incelemek isterseniz, bu diğer kapsamlı eğitim kursuna göz atmanızı şiddetle tavsiye ederim:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### RGB kod haritası


Son olarak, bir sonraki bölüme geçmeden önce, size RGB'te kullanılan kod hakkında genel bir bilgi vermek istiyorum. Protokol, bir dizi Rust kütüphanesine ve açık kaynak spesifikasyonlarına dayanmaktadır. İşte ana depolara ve sandıklara genel bir bakış:


![RGB-Bitcoin](assets/fr/097.webp)


#### Client-side Validation




- **Depo**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Kasalar**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)


off-chain doğrulama ve Tek Kullanımlık Mühürler mantığının yönetimi.


#### Deterministik Bitcoin Taahhütleri (DBC)




- **Repo**: [bp-core](https://github.com/BP-WG/bp-core)
- **Sandık**: [bp-dbc](https://crates.io/crates/bp-dbc)


Bitcoin işlemlerinde (Tapret, OP_RETURN, vb.) deterministik ankraj yönetimi.


#### Multi Protocol Commitment (MPC)




- **Depo**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Sandık**: [commit_verify](https://crates.io/crates/commit_verify)


Çoklu angajman kombinasyonları ve farklı protokollerle entegrasyon.


#### Sıkı Tipler ve Sıkı Kodlama




- **Teknik Özellikler**: [web sitesi strict-types.org](https://www.strict-types.org/)
- **Depolar**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- **Kasalar**: [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)


Client-side Validation için kullanılan katı yazım sistemi ve deterministik serileştirme.


#### RGB Çekirdek




- **Repo**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- **Sandık**: [RGB-core](https://crates.io/crates/RGB-core)


RGB doğrulamasının ana mantığını kapsayan protokolün çekirdeği.


#### RGB Standart Kütüphane & Wallet




- **Depo**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- **Sandık**: [RGB-std](https://crates.io/crates/RGB-std)


Standart uygulamalar, Stash ve Wallet yönetimi.


#### RGB CLI




- **Depo**: [RGB](https://github.com/RGB-WG/RGB)
- **Kasalar**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


Sözleşmelerin komut satırı manipülasyonu için `RGB` CLI ve crate Wallet.


#### RGB Schema




- **Depo**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


Şema örnekleri (NIA, UDA, vb.) ve bunların uygulamalarını içerir.


#### AluVM




- **Bilgi**: [AluVM.org](https://www.AluVM.org/)
- **Depolar**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- **Kasalar**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)


Doğrulama komut dosyalarını çalıştırmak için kullanılan kayıt defteri tabanlı sanal makine.


#### Bitcoin Protokolü - BP




- **Depolar**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Bitcoin protokolünü desteklemek için eklentiler (işlemler, baypaslar, vb.).


#### Ubiquitous Deterministic Computing - UBIDECO




- **Depo**: [UBIDECO](https://github.com/UBIDECO)


Açık kaynaklı deterministik gelişmelerle bağlantılı ekosistem.


# RGB üzerine inşa ediliyor


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA ve Bitmask projesi


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


Kursun bu son bölümü, RGB bootcamp'inde çeşitli konuşmacılar tarafından yapılan sunumlara dayanmaktadır. RGB ve ekosistemi hakkındaki görüş ve düşüncelerin yanı sıra protokole dayalı araç ve projelerin sunumlarını içermektedir. Bu ilk bölüm Hunter Beast tarafından, sonraki iki bölüm ise Frederico Tenga tarafından yönetilmektedir.


### JavaScript'ten Rust'e ve Bitcoin ekosistemine


Hunter Beast ilk başta ağırlıklı olarak JavaScript'te çalıştı. Daha sonra, sözdizimi ilk başta çekici olmayan ve sinir bozucu görünen **Rust**'i keşfetti. Ancak, dilin gücünü, bellek üzerindeki kontrolünü (*heap* ve *stack*) ve bununla birlikte gelen güvenlik ve performansı takdir etmeye başladı. Rust'in bir bilgisayarın nasıl çalıştığını derinlemesine anlamak için mükemmel bir eğitim zemini olduğunu vurguluyor.


Hunter Beast, *Altcoin* ekosistemindeki Ethereum (Solidity, TypeScript vb. ile) ve daha sonra Filecoin gibi çeşitli projelerdeki geçmişini anlatıyor. Başlangıçta bazı protokollerden etkilendiğini, ancak tokenomik olmaları nedeniyle çoğundan hayal kırıklığına uğradığını açıklıyor. Şüpheli finansal teşvikleri, yatırımcıları sulandıran enflasyonist token yaratımını ve bu projelerin potansiyel olarak sömürücü yönünü kınıyor. Sonunda **Bitcoin Maximalist** duruşunu benimsemiştir; bunun nedeni, bazı insanların gözlerini Bitcoin'in daha sağlam ekonomik mekanizmalarına ve bu sistemin sağlamlığına açmasıdır.


### RGB'un cazibesi ve katmanlar üzerine inşa edilmesi


Kendi ifadesiyle, Bitcoin'ün önemi konusunda onu kesin olarak ikna eden şey, RGB'in ve katman kavramının keşfedilmesiydi. Diğer blok zincirlerindeki mevcut işlevlerin, temel protokolü değiştirmeden Bitcoin'ün üzerindeki daha yüksek katmanlarda yeniden üretilebileceğine inanıyor.


Şubat 2022'de, özellikle RGB ve özellikle **Bitmask** Wallet üzerinde çalışmak üzere **DIBA**'ya katıldı. O sırada Bitmask hala 0.01 sürümündeydi ve RGB'ü 0.4 sürümünde çalıştırıyordu, yalnızca tek belirteçlerin yönetimi için. Mantık kısmen sunucu tabanlı olduğu için bunun bugünkünden daha az kendi kendine saklama odaklı olduğunu belirtiyor. O zamandan beri mimari, bitcoin kullanıcıları tarafından çok takdir edilen bu modele doğru gelişti.


### RGB protokolünün temelleri


**RGB** protokolü, 2012-2013 yıllarında keşfedilmiş olan *colored coins* konseptinin en yeni ve en gelişmiş uygulamasıdır. O dönemde, birkaç ekip UTXO'lara farklı Bitcoin değerleri atamak istiyordu ve bu da çok sayıda dağınık uygulamaya yol açtı. Bu standardizasyon eksikliği ve o zamanki düşük talep, bu çözümlerin kalıcı bir yer edinmesini engelledi.


Günümüzde RGB, kavramsal sağlamlığı ve LNP/BP ilişkisi aracılığıyla birleştirilmiş özellikleri ile öne çıkmaktadır. İlke Client-side Validation'ye dayanmaktadır. Bitcoin Blockchain yalnızca kriptografik taahhütleri (_commitments_, Taproot veya OP_RETURN aracılığıyla) depolarken, verilerin çoğu (Contract tanımları, aktarım geçmişleri, vb.) ilgili kullanıcılar tarafından depolanır. Bu şekilde, depolama yükü dağıtılır ve Blockchain'i ağırlaştırmadan alışverişlerin gizliliği güçlendirilir. Bu yaklaşım, modüler ve ölçeklenebilir bir çerçeve içinde değiştirilebilir varlıkların (**RGB20** standardı) veya benzersiz varlıkların (**RGB21** standardı) oluşturulmasını sağlar.


### token işlevi (RGB20) ve benzersiz varlıklar (RGB21)


**RGB20** ile Bitcoin üzerinde değiştirilebilir bir token tanımlıyoruz. İhraççı bir *supply*, bir *precision* seçer ve daha sonra transferler yapabileceği bir *contract* oluşturur. Her transfer bir **Single-Use Seal** olarak hareket eden bir Bitcoin UTXO'a referans verilir. Bu mantık, kullanıcının aynı varlığı iki kez harcayamamasını sağlar, çünkü yalnızca UTXO'u harcayabilen kişi aslında istemci tarafı Contract'nın durumunu güncelleme anahtarına sahiptir.


**RGB21** benzersiz varlıkları (veya "NFT") hedefler. Varlığın Supply değeri 1'dir ve belirli bir alan aracılığıyla açıklanan meta verilerle (görüntü dosyası, ses vb.) ilişkilendirilebilir. Halka açık blok zincirlerindeki NFT'lerin aksine, veriler ve MIME tanımlayıcıları gizli kalabilir, sahibinin takdirine bağlı olarak eşler arası dağıtılabilir.


### Bitmask çözümü: RGB için bir Wallet


RGB'in yeteneklerinden pratikte yararlanmak için **DIBA** projesi [Bitmask] (https://bitmask.app/) adlı bir Wallet tasarlamıştır. Buradaki fikir, bir web uygulaması veya tarayıcı uzantısı olarak erişilebilen, gözetim altında olmayan, Taproot tabanlı bir araç sağlamaktır. Bitmask hem RGB20 hem de RGB21 varlıklarını yönetir ve çeşitli güvenlik mekanizmalarını entegre eder:




- Çekirdek kod Rust'da yazılmış, ardından JavaScript ortamında (React) çalıştırılmak üzere WebAssembly'de derlenmiştir;
- Anahtarlar yerel olarak oluşturulur, ardından yerel olarak şifrelenerek saklanır;
- Durum verileri (Stash) bellekte tutulur, serileştirilir ve Blake3 kullanarak sıkıştırma, hata düzeltme, şifreleme ve akış doğrulama gerçekleştiren **Carbonado** kütüphanesi aracılığıyla şifrelenir.


Bu mimari sayesinde, tüm varlık işlemleri istemci tarafında gerçekleşir. Dışarıdan bakıldığında, Bitcoin işlemi klasik bir Taproot harcama işleminden başka bir şey değildir ve kimse bunun aynı zamanda değiştirilebilir token veya NFT transferi taşıdığından şüphelenmez. On-Chain aşırı yüklemesinin olmaması (kamuya açık olarak saklanan meta verilerin olmaması) belirli bir gizlilik derecesini garanti eder ve olası sansür girişimlerine direnmeyi kolaylaştırır.


### Güvenlik ve dağıtık mimari


RGB protokolü her katılımcının işlem geçmişini saklamasını gerektirdiğinden (aldığı transferlerin geçerliliğini kanıtlamak için), depolama sorunu ortaya çıkmaktadır. Bitmask, bu Stash'yi yerel olarak serileştirmeyi ve ardından çeşitli sunuculara veya bulutlara (isteğe bağlı) göndermeyi önermektedir. Veriler kullanıcı tarafından **Carbonado** aracılığıyla şifrelenmiş olarak kalır, böylece bir sunucu bunları okuyamaz. Kısmi bozulma durumunda, hata düzeltme Layer içeriği yeniden oluşturabilir.


CRDT (_Conflict-free replicated data type_) kullanımı, Stash'nın farklı versiyonlarının ayrışması durumunda birleştirilebilmesini sağlar. Tek bir Full node varlıkla bağlantılı tüm bilgileri taşımadığından, herkes bu verileri istediği yerde barındırmakta özgürdür. Bu tam olarak *Client-side Validation* felsefesini yansıtmaktadır; burada her mal sahibi kendi RGB varlığının geçerliliğinin kanıtını saklamaktan sorumludur.


### Daha geniş bir ekosisteme doğru: pazar yeri, birlikte çalışabilirlik ve yeni işlevler


Bitmask'ın arkasındaki şirket kendisini basit bir Wallet geliştirmeyle sınırlamıyor. DIBA geliştirme niyetinde:




- Özellikle **RGB21** formundaki jetonları takas etmek için bir **pazar yeri**;
- Diğer cüzdanlarla uyumluluk (*Iris Wallet* gibi);
- Transfer gruplama teknikleri, yani birbirini takip eden birkaç RGB transferini tek bir işleme dahil etme imkanı.


Aynı zamanda, **WebBTC** veya **WebLN** (web sitelerinin Wallet'den Bitcoin veya Lightning işlemlerini imzalamasını istemesini sağlayan standartlar) ve Ordinals girişlerini "teleburn" etme yeteneği (Ordinals'ı daha gizli ve esnek bir RGB formatına geri göndermek istiyorsak) üzerinde çalışıyoruz.


### Sonuç


Tüm bu süreç, RGB ekosisteminin sağlam teknik çözümler aracılığıyla son kullanıcılar için nasıl konuşlandırılabileceğini ve erişilebilir hale getirilebileceğini göstermektedir. Altcoin perspektifinden daha Bitcoin merkezli bir vizyona geçiş, *Client-side Validation*'ün keşfiyle birleştiğinde, oldukça mantıklı bir yol göstermektedir: Blockchain'i çatallandırmadan, sadece Taproot işlemleri veya OP_RETURN'ler üzerindeki kriptografik taahhütlerden yararlanarak çeşitli işlevleri (değiştirilebilir tokenler, NFT, akıllı sözleşmeler...) uygulamanın mümkün olduğunu anlıyoruz.


**Bitmask** Wallet bu yaklaşımın bir parçasıdır: Blockchain tarafında, gördüğünüz tek şey sıradan bir Bitcoin işlemidir; kullanıcı tarafında, her türlü off-chain varlığını oluşturduğunuz, Exchange ve sakladığınız bir web Interface'yi manipüle edersiniz. Bu model, parasal altyapıyı (Bitcoin) ihraç ve transfer mantığından (RGB) net bir şekilde ayırırken, yüksek düzeyde gizlilik ve daha iyi ölçeklenebilirlik sağlar.


## Bitfinex'in RGB üzerindeki çalışmaları


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


Bu bölümde, Frederico Tenga tarafından yapılan bir sunuma dayanarak, Bitfinex ekibi tarafından RGB'a adanmış ve bu protokol etrafında zengin ve çeşitli bir ekosistemin ortaya çıkmasını teşvik etmek amacıyla oluşturulan bir dizi araç ve projeye bakıyoruz. Ekibin ilk amacı belirli bir ticari ürünü piyasaya sürmek değil, yazılım yapı taşları sağlamak, RGB protokolünün kendisine katkıda bulunmak ve mobil bir Wallet (*Iris Wallet*) veya RGB uyumlu bir Lightning düğümü gibi somut uygulama referansları önermektir.


### Arka plan ve hedefler


Bitfinex RGB ekibi, yaklaşık 2022 yılından bu yana RGB'ın verimli bir şekilde kullanılmasını ve test edilmesini sağlayan teknoloji yığınını geliştirmeye odaklanmaktadır. Çeşitli katkılar yapılmıştır:




- Geliştirme önerileri yazma, hataları düzeltme vb. dahil olmak üzere kaynak kodu ve protokol spesifikasyonlarına katılım;
- Geliştiriciler için RGB'in uygulamalarına entegrasyonunu basitleştiren araçlar;
- RGB kullanımına yönelik en iyi uygulamaları denemek ve göstermek için [Iris](https://iriswallet.com/) adlı bir mobil Wallet tasarımı;
- RGB varlıkları ile kanalları yönetebilen özelleştirilmiş bir Lightning düğümünün oluşturulması;
- Çeşitliliği ve güçlü bir ekosistemi teşvik etmek için RGB üzerinde çözümler geliştiren diğer ekipleri desteklemek.


Bu yaklaşım, bir Wallet'nın uygulanmasını sağlayan düşük seviyeli kütüphaneden (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*) üretim yönüne (bir Lightning düğümü, Android için bir Wallet, vb.) kadar tüm ihtiyaç zincirini kapsamayı amaçlamaktadır.


### RGBlib kütüphanesi: RGB uygulamalarının geliştirilmesini basitleştiriyor


RGB cüzdanlarının ve uygulamalarının oluşturulmasını demokratikleştirmenin önemli bir noktası, geliştiricilerin protokolün iç mantığı hakkında her şeyi öğrenmek zorunda kalmamaları için yeterince basit bir soyutlama sağlamaktır. Rust ile yazılmış **RGBlib**'in amacı da tam olarak budur.


RGBlib, önceki bölümlerde inceleyebildiğimiz RGB'ün son derece esnek (ancak bazen karmaşık) gereksinimleri ile bir uygulama geliştiricisinin somut ihtiyaçları arasında bir köprü görevi görür. Başka bir deyişle, token transferlerini, varlık ihracını, doğrulamayı vb. yönetmek isteyen bir Wallet (veya hizmet), her kriptografik ayrıntıyı veya özelleştirilebilir her RGB parametresini bilmeden RGBlib'e güvenebilir.


Kitapçı teklifleri:




- Varlık ihracı (_issuance_) için anahtar teslim işlevler (değiştirilebilir veya değil);
- Basit nesneleri (adresler, miktarlar, UTXO'lar, vb.) manipüle ederek varlıkları transfer etme (gönderme/alma) yeteneği;
- Client-side Validation için gerekli olan durum bilgilerini (*atamalar*) depolamak ve yüklemek için bir mekanizma.


Bu nedenle RGBlib, RGB'ye özgü karmaşık kavramlara (Client-side Validation, Tapret/Opret anchor'ları) dayanır, ancak bunları kapsüller, böylece son uygulamanın her şeyi yeniden programlaması veya riskli kararlar vermesi gerekmez. Dahası, RGBlib zaten birkaç dile (Kotlin ve Python) bağlanmıştır ve basit bir Rust evreninin ötesinde kullanımlara kapı açmaktadır.


### Iris Wallet: Android üzerinde bir RGB Wallet örneği


RGBlib'in etkinliğini kanıtlamak için Bitfinex ekibi, bu aşamada yalnızca Android'de **Iris Wallet**'i geliştirdi. Bu, sıradan bir Bitcoin Wallet'e benzer bir kullanıcı deneyimini gösteren bir mobil Wallet'dir: kendi kendine saklama modelinde kalırken bir varlık verebilir, gönderebilir, alabilir ve geçmişini görüntüleyebilirsiniz.


Iris'in bir dizi ilginç özelliği vardır:


**Bir Electrum sunucusu kullanarak:**


Herhangi bir Wallet gibi, Iris'in de Blockchain'deki işlem onayları hakkında bilgi sahibi olması gerekir. Tam bir düğüm yerleştirmek yerine, Iris varsayılan olarak Bitfinex ekibi tarafından tutulan bir Electrum sunucusunu kullanır. Bununla birlikte, kullanıcılar kendi sunucularını veya başka bir üçüncü taraf hizmetini yapılandırabilirler. Bu şekilde, Bitcoin işlemleri doğrulanabilir ve bilgiler modüler bir şekilde alınabilir (indeksleme).


**RGB proxy sunucusu:**


Bitcoin'den farklı olarak RGB, gönderici ve alıcı arasında off-chain meta verilerinin (*atamalar*) Exchange'sini gerektirir. Bu süreci basitleştirmek için Iris, iletişimin bir proxy sunucusu üzerinden gerçekleştiği bir çözüm sunar. Alıcı Wallet, göndericinin *istemci tarafı* verilerini nereye göndermesi gerektiğini belirten bir *Invoice* oluşturur. Varsayılan olarak URL, Bitfinex ekibi tarafından barındırılan bir proxy'ye işaret eder, ancak bu proxy'yi değiştirebilirsiniz (veya kendi proxy'nizi barındırabilirsiniz). Buradaki fikir, alıcının bir QR kodu görüntülediği ve gönderenin herhangi bir karmaşık ek manipülasyon olmadan işlem için bu kodu taradığı tanıdık bir kullanıcı deneyimine geri dönmektir.


**Sürekli yedekleme:**


Bitcoin bağlamında, seed'ünüzü yedeklemek genellikle yeterlidir (ancak bugünlerde bunun yerine seed'ü ve tanımlayıcıları yedeklemenizi öneriyoruz). RGB ile bu yeterli değildir: bir RGB varlığına gerçekten sahip olduğunuzu kanıtlayan yerel geçmişi de (*atamalar*) saklamanız gerekir. Her makbuz aldığınızda, cihaz sonraki harcamalar için gerekli olan yeni verileri kaydeder. Iris, kullanıcının Google Drive'ında şifrelenmiş bir yedeği otomatik olarak yönetir. Yedekleme şifreli olduğu için Google'a özel bir güven gerektirmez ve üçüncü taraf bir operatör tarafından herhangi bir sansür veya silme riskini önlemek için gelecekte daha sağlam seçenekler (kişisel bir sunucu gibi) planlanmaktadır.


**Diğer özellikler:**




- Deneme veya promosyon amaçlı jetonları hızlı bir şekilde test etmek veya dağıtmak için bir Faucet oluşturun;
- Meşru bir token'yı ünlü bir ticker'ı kopyalayan sahte bir token'dan ayırt etmek için bir sertifikasyon sistemi (şu anda merkezi). Gelecekte bu sertifikasyon daha merkezsiz hale gelebilir (DNS veya diğer mekanizmalar aracılığıyla).


Sonuç olarak Iris, RGBlib ve proxy sunucusu kullanımı sayesinde ek karmaşıklığı (Stash yönetimi, *Consignment* geçmişi, vb.) maskeleyerek klasik bir Bitcoin Wallet'a yakın bir kullanıcı deneyimi sunuyor.


### Proxy sunucusu ve kullanıcı deneyimi


Yukarıda tanıtılan proxy sunucusu, sorunsuz bir kullanıcı deneyiminin anahtarı olduğu için detaylandırılmayı hak ediyor. Göndericinin * gönderileri * alıcıya manuel olarak iletmek zorunda kalması yerine, RGB işlemi arka planda bir proxy sunucusu aracılığıyla gerçekleşir:




- Alıcı bir *Invoice* oluşturur (diğer şeylerin yanı sıra Address proxy'sini de içerir);
- Gönderici proxy'ye bir geçiş projesi (*Consignment*) gönderir (bir HTTP isteği aracılığıyla);
- Alıcı bu projeyi alır, *istemci tarafı* doğrulamasını yerel olarak yürütür;
- Alıcı daha sonra proxy aracılığıyla State Transition'in kabulünü (veya muhtemelen reddini) yayınlar;
- Gönderici doğrulama durumunu görüntüleyebilir ve kabul edilirse aktarımı sonlandıran Bitcoin işlemini yayınlayabilir.


Bu şekilde, Wallet neredeyse normal bir Wallet gibi davranır. Kullanıcı tüm ara adımlardan habersizdir. Kuşkusuz, mevcut proxy ne şifrelenmiş ne de doğrulanmıştır (bu da gizlilik ve bütünlükle ilgili endişelere yol açmaktadır), ancak bu iyileştirmeler sonraki sürümlerde mümkündür. Proxy konsepti, "Ben bir QR kodu gönderiyorum, siz tarayarak ödeme yapıyorsunuz" deneyimini yeniden yaratmak için son derece kullanışlı olmaya devam ediyor.


### Lightning Network üzerinde RGB entegrasyonu


Bitfinex ekibinin çalışmalarının bir diğer önemli odağı da Lightning Network'u RGB varlıklarıyla uyumlu hale getirmektir. Amaç, USDT'de (veya başka herhangi bir token'de) Lightning kanallarını etkinleştirmek ve Lightning'de Bitcoin ile aynı avantajlardan yararlanmaktır (neredeyse anlık işlemler, yönlendirme vb.). Somut olarak bu, şu şekilde değiştirilmiş bir Lightning düğümü oluşturmayı içerir:




- UTXO Multisig fonuna yalnızca satoshileri değil, aynı zamanda bir veya daha fazla RGB varlığını da yerleştirerek bir kanal açın;
- generate Lightning Commitment işlemlerine (Bitcoin tarafı) karşılık gelen RGB durum geçişleri eşlik eder. Kanal her güncellendiğinde, bir RGB geçişi Lightning çıktılarındaki varlık dağılımını yeniden tanımlar;
- Varlığın Lightning Network kurallarına (HTLC, zaman kilidi, ceza, vb.) uygun olarak özel bir UTXO'te alındığı tek taraflı kapatmayı etkinleştirin.


"**RGB Lightning Node**" olarak adlandırılan bu çözüm, LDK'yı (*Lightning Dev Kit*) temel olarak kullanır ve RGB belirteçlerini kanallara enjekte etmek için gereken mekanizmaları ekler. Lightning taahhütleri klasik yapısını (delinebilir çıkışlar, zaman kilidi...) ve ek olarak Anchor bir RGB State Transition'ü (`Opret` veya `Tapret` aracılığıyla) korur. Kullanıcı için bu, sabit coinlerde veya RGB aracılığıyla yayılan başka herhangi bir varlıkta Lightning kanallarının yolunu açar.


### DEX potansiyeli ve Bitcoin üzerindeki etkisi


Lightning aracılığıyla birkaç varlık yönetildiğinde, aynı gizli diziler ve zaman kilitleri mantığını kullanarak tek bir Lightning yönlendirme yolu üzerinde bir **atomik Exchange** hayal etmek mümkün hale gelir. Örneğin, A kullanıcısı bir Lightning kanalında Bitcoin'a sahiptir ve B kullanıcısı başka bir Lightning kanalında USDT RGB'a sahiptir. İki kanalı birbirine bağlayan bir yol oluşturabilir ve aynı anda USDT için Exchange BTC'yi güvene ihtiyaç duymadan kullanabilirler. Bu, birkaç atlamada gerçekleşen bir **atomik takastan** başka bir şey değildir ve dışarıdaki katılımcıların sadece bir yönlendirme değil, bir ticaret yaptıkları gerçeğinden neredeyse habersiz olmalarını sağlar. Bu yaklaşım şunları sunar:




- Lightning'de her şey off-chain olarak kaldığı için çok düşük gecikme.
- Üstün bir **gizlilik**: kimse bunun bir ticaret olduğunu ve normal bir yönlendirme olmadığını bilmiyor;
- On-Chain DEX için yinelenen bir sorun olan önden kaçıştan kaçınmak;
- Azaltılmış maliyetler (blok alanı ödemezsiniz, sadece Yıldırım yönlendirme ücretleri ödersiniz).


Daha sonra Lightning düğümlerinin takas fiyatları sunduğu (likidite sağlayarak) bir ekosistem hayal edebiliriz. Her düğüm, eğer isterse, Lightning üzerinde çeşitli varlıkları alıp satarak _piyasa yapıcı_ rolünü oynayabilir. Bu _layer-2_ DEX olasılığı, merkezi olmayan varlık borsaları elde etmek için Fork veya üçüncü taraf blok zincirlerinin kullanılmasının gerekli olmadığı fikrini güçlendirmektedir.


Bitcoin üzerindeki etkisi olumlu olabilir: Lightning'in altyapısı (düğümler, kanallar ve hizmetler), bu *kararlı paralar*, türevler ve diğer tokenler tarafından üretilen hacimler sayesinde daha tam olarak kullanılacaktır. Lightning üzerinde USDT ödemeleriyle ilgilenen tüccarlar, mekanik olarak Lightning üzerinde BTC ödemelerini keşfedecektir (aynı yığın tarafından yönetilir). Lightning Network altyapısının bakımı ve finansmanı da bu BTC dışı akışların çoğalmasından faydalanabilir ve bu da dolaylı olarak Bitcoin kullanıcılarına fayda sağlayacaktır.


### Sonuç ve kaynaklar


RGB'e adanmış Bitfinex ekibi, çalışmaları aracılığıyla protokol üzerinde yapılabileceklerin çeşitliliğini göstermektedir. Bir yanda, cüzdan ve uygulamaların tasarımını kolaylaştıran bir kütüphane olan RGBlib var. Diğer yanda, Android üzerinde düzgün bir son kullanıcı Interface'nın pratik bir gösterimi olan Iris Wallet var. Son olarak, RGB'in Lightning ile entegrasyonu, stabilcoin kanallarının mümkün olduğunu gösteriyor ve Lightning üzerinde potansiyel bir merkezi olmayan DEX'e giden yolu açıyor.


Bu yaklaşım büyük ölçüde deneyseldir ve gelişmeye devam etmektedir: RGBlib kütüphanesi ilerledikçe geliştirilmektedir, Iris Wallet düzenli geliştirmeler almaktadır ve özel Lightning düğümü henüz ana akım bir Lightning istemcisi değildir.


Daha fazla bilgi edinmek veya katkıda bulunmak isteyenler için, aşağıdakiler de dahil olmak üzere çeşitli kaynaklar mevcuttur:




- [GitHub RGB Araçlar depoları](https://github.com/RGB-Tools);
- gW-2341'i Android'de test etmek için [Iris Wallet'e adanmış bir bilgi sitesi] (https://iriswallet.com/).


Bir sonraki bölümde, bir RGB Lightning düğümünün nasıl başlatılacağına daha yakından bakacağız.


## RLN - RGB Yıldırım Düğümü


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


Bu son bölümde Frederico Tenga, Regtest ortamında bir Lightning RGB düğümü kurarak sizi adım adım yönlendiriyor ve bu düğüm üzerinde nasıl RGB tokenleri oluşturacağınızı gösteriyor. İki ayrı düğüm başlatarak, bunlar ve Exchange RGB varlıkları arasında bir Lightning kanalının nasıl açılacağını da keşfedeceksiniz.


Bu video, bir önceki bölümde anlattıklarımıza benzer bir eğitim niteliğindedir, ancak bu sefer özellikle Lightning'e odaklanmıştır!


Bu video için ana kaynak, bu yapılandırmayı Regtest'te başlatmanızı kolaylaştıran Github deposudur [RGB Lightning Node] (https://github.com/RGB-Tools/RGB-lightning-node).


### RGB uyumlu bir Lightning düğümü dağıtma


Bu süreç, önceki bölümlerde ele alınan tüm kavramları ele alır ve uygulamaya koyar:




- Bir Lightning kanalının 2/2 Multisig'unda bloke edilen **UTXO**'nin yalnızca bitcoin alabileceği değil, aynı zamanda RGB varlıklarının (değiştirilebilir veya değil) bir Single-Use Seal'i olabileceği fikri;
- Her Lightning angajman işleminde, RGB State Transition'yi sabitlemeye adanmış bir çıktının (`Tapret` veya `Opret`) eklenmesi;
- Bitcoin işlemlerini ve Exchange *istemci tarafı* verilerini doğrulamak için ilişkili altyapı (bitcoind/indexer/proxy).


### RGB-lightning-node ile tanışın


**RGB-lightning-node** projesi, bir kanaldaki RGB varlıklarının varlığını dikkate almak için değiştirilmiş bir **Rust-lightning** (LDK) Fork'a dayanan bir Rust daemon'dir. Bir kanal açıldığında, varlıkların varlığı belirtilebilir ve kanal durumu her güncellendiğinde, Yıldırım çıkışlarındaki varlığın dağılımını yansıtan bir RGB geçişi oluşturulur. Bu şunları sağlar:




- Örneğin USDT'de Lightning kanalları açın;
- Yönlendirme yollarının yeterli likiditeye sahip olması koşuluyla, bu tokenları ağ üzerinden yönlendirin;
- Lightning'in ceza ve zaman kilidi mantığından değişiklik yapmadan yararlanın: Commitment Transaction'nin ek bir çıkışında RGB geçişini Anchor yapmanız yeterlidir.


Kod hala alfa aşamasındadır: yalnızca **regtest** veya **Testnet** üzerinde kullanmanızı öneririz.


### Düğüm kurulumu


RGB-lightning-node` ikili dosyasını derlemek ve kurmak için, depoyu ve alt modüllerini klonlayarak başlıyoruz, ardından


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/fr/098.webp)




- Recurse-submodules` seçeneği de gerekli alt aygıtları klonlar (`Rust-lightning`in değiştirilmiş sürümü dahil);
- Shallow-submodules' seçeneği, indirmeyi hızlandırmak için klonun derinliğini kısıtlarken, yine de temel taahhütlere erişim sağlar.


Proje kökünden, ikili dosyayı derlemek ve yüklemek için aşağıdaki komutu çalıştırın:


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/fr/099.webp)




- locked`, bağımlılıkların sürümüne kesinlikle uyulmasını sağlar;
- `--debug` zorunlu değildir, ancak odaklanmanıza yardımcı olabilir (tercih ederseniz `--release` kullanabilirsiniz);
- `--path .`, `cargo install`a geçerli dizinden yükleme yapmasını söyler.


Bu komutun sonunda, `$CARGO_HOME/bin/` dizininizde bir `RGB-lightning-node` çalıştırılabilir dosyası bulunacaktır. Bu yolun `$PATH` dizininizde olduğundan emin olun, böylece komutu herhangi bir dizinden çağırabilirsiniz.


### Performans gereksinimleri


Çalışması için `RGB-lightning-node` daemon'un varlığı ve yapılandırılması gerekir:




- Bir **`bitcoind`** düğümü


Her RLN örneğinin On-Chain işlemlerini yayınlamak ve izlemek için `bitcoind` ile iletişim kurması gerekecektir. Kimlik doğrulama (giriş/parola) ve URL'nin (ana bilgisayar/port) daemon'e sağlanması gerekecektir.




- Bir **indeksleyici** (Electrum veya Esplora)


daemon, özellikle bir varlığın sabitlendiği UTXO'yi bulmak için On-Chain işlemlerini listeleyebilmeli ve keşfedebilmelidir. Electrum sunucunuzun veya Esplora'nın URL'sini belirtmeniz gerekir.




- Bir **RGB** proxy


Önceki bölümlerde görüldüğü gibi, **proxy sunucusu** Lightning eşleri arasındaki *atamaların* Exchange basitleştirmek için bir bileşendir (isteğe bağlı, ancak şiddetle tavsiye edilir). Bir kez daha, bir URL belirtilmelidir.


Kimlikler ve URL'ler, daemon API aracılığıyla _kilidi açıldığında_ girilir. Bu konuda daha sonra bilgi vereceğiz.


### Regtest lansmanı


Basit kullanım için, Docker aracılığıyla bir dizi hizmeti otomatik olarak başlatan bir `regtest.sh` betiği vardır: `bitcoind`, `electrs` (dizinleyici), `RGB-proxy-server`.


![RGB-Bitcoin](assets/fr/100.webp)


Bu, yerel, yalıtılmış, önceden yapılandırılmış bir ortam başlatmanıza olanak tanır. Her yeniden başlatmada kapsayıcıları ve veri dizinlerini oluşturur ve yok eder. Şunu başlatarak başlayacağız:


```bash
./regtest.sh start
```


Bu senaryo:




- Saklamak için bir `docker/` dizini oluşturun;
- Regtest`te `bitcoind`ün yanı sıra indeksleyici `electrs` ve `RGB-proxy-server`ı çalıştırın;
- Her şey kullanıma hazır olana kadar bekleyin.


![RGB-Bitcoin](assets/fr/101.webp)


Daha sonra, birkaç RLN düğümü başlatacağız. Ayrı kabuklarda, örneğin (3 RLN düğümü başlatmak için) çalıştırın:


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RGB-Bitcoin](assets/fr/102.webp)




- Ağ regtest` parametresi regtest yapılandırmasının kullanılacağını gösterir;
- `--daemon-listening-port` Lightning düğümünün API çağrıları için hangi REST bağlantı noktasını dinleyeceğini gösterir (JSON);
- `--ldk-peer-listening-port` hangi Lightning P2P bağlantı noktasının dinleneceğini belirtir;
- `dataldk0/`, `dataldk1/` depolama dizinlerine giden yollardır (her düğüm bilgilerini ayrı ayrı depolar).


RLN düğümlerinizdeki komutları tarayıcınızdan da çalıştırabilirsiniz:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Bir düğümün bir kanal açabilmesi için, öncelikle aşağıdaki komutla oluşturulan bir Address üzerinde bitcoinlere sahip olması gerekir (örneğin n°1 düğümü için):


```bash
curl -X POST http://localhost:3001/address
```


Cevap size bir Address sağlayacaktır.


![RGB-Bitcoin](assets/fr/103.webp)


bitcoind' Regtest'te birkaç bitcoin madenciliği yapacağız. Çalıştır:


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/fr/104.webp)


Yukarıda oluşturulan Address düğümüne para gönderin:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/fr/105.webp)


Ardından işlemi onaylamak için bir blok kazın:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/fr/106.webp)


### Testnet başlatma (Docker olmadan)


Daha gerçekçi bir senaryoyu test etmek istiyorsanız, Regtest yerine Testnet'de kamu hizmetlerine işaret eden 3 RLN düğümü başlatabilirsiniz:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Varsayılan olarak, herhangi bir yapılandırma bulunamazsa, daemon




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Giriş ile:




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


Bu Elements'i `init`/`unlock` API'si aracılığıyla da özelleştirebilirsiniz.


### Bir RGB token düzenlenmesi


Bir token yayınlamak için, "renklendirilebilir" UTXO'lar oluşturarak başlayacağız:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RGB-Bitcoin](assets/fr/107.webp)


Elbette siparişi uyarlayabilirsiniz. İşlemi onaylamak için, bir:


```bash
./regtest.sh mine 1
```


Şimdi bir RGB varlığı oluşturabiliriz. Komut, oluşturmak istediğiniz varlığın türüne ve parametrelerine bağlı olacaktır. Burada 1000 birimlik bir Supply ile "PBN" adında bir NIA (*Şişirilemeyen Varlık*) token oluşturuyorum. Hassasiyet' birimlerin bölünebilirliğini tanımlamanıza olanak tanır.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RGB-Bitcoin](assets/fr/108.webp)


Yanıt, yeni oluşturulan varlığın kimliğini içerir. Bu tanımlayıcıyı not etmeyi unutmayın. Benim durumumda, bu:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/fr/109.webp)


Daha sonra bunu On-Chain'ye aktarabilir veya bir Lightning kanalına tahsis edebilirsiniz. Bir sonraki bölümde yapacağımız şey tam olarak bu.


### Bir kanal açma ve bir RGB varlığı aktarma


Önce `/connectpeer` komutunu kullanarak düğümünüzü Lightning Network üzerindeki bir eşe bağlamanız gerekir. Benim örneğimde, her iki düğümü de kontrol ediyorum. Bu yüzden ikinci Lightning düğümümün ortak anahtarını bu komutla alacağım:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Komut, 2 numaralı düğümümün açık anahtarını döndürür:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RGB-Bitcoin](assets/fr/110.webp)


Daha sonra, ilgili varlığı (`PBN`) belirterek kanalı açacağız. Openchannel` komutu, kanalın boyutunu satoshis cinsinden tanımlamanıza ve RGB varlığını dahil etmeyi seçmenize olanak tanır. Ne oluşturmak istediğinize bağlı, ancak benim durumumda komut şu şekildedir:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Daha fazlasını burada bulabilirsiniz:




- `peer_pubkey_and_opt_addr`: Bağlanmak istediğimiz eşin tanımlayıcısı (daha önce bulduğumuz açık anahtar);
- `capacity_sat`: Satoshi cinsinden toplam kanal kapasitesi;
- `push_msat`: Kanal açıldığında başlangıçta eşe aktarılan milisatoshis cinsinden miktar (burada hemen 10.000 Sats aktarıyorum, böylece daha sonra bir RGB aktarımı yapabilir);
- `asset_amount`: Kanala taahhüt edilecek RGB varlıklarının miktarı;
- `asset_id`: Kanalda yer alan RGB varlığının benzersiz tanımlayıcısı;
- `public`: Kanalın ağ üzerinde yönlendirme için herkese açık hale getirilip getirilmeyeceğini belirtir.


![RGB-Bitcoin](assets/fr/111.webp)


İşlemi onaylamak için 6 blok çıkarılır:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/fr/112.webp)


Lightning kanalı artık açıktır ve ayrıca n°1 düğümü tarafında 500 `PBN` jetonu içerir. Eğer n°2 düğümü `PBN` jetonlarını almak isterse, generate ve Invoice yapmalıdır. İşte nasıl yapılacağı:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Ile:




- `amt_msat`: Milisatoshis cinsinden Invoice miktarı (minimum 3000 Sats);
- `expiry_sec`: Saniye cinsinden Invoice sona erme süresi;
- `asset_id`: Invoice ile ilişkili RGB varlığının tanımlayıcısı;
- varlık_miktarı`: Bu Invoice ile aktarılacak RGB varlığının tutarı.


Yanıt olarak bir RGB Invoice (önceki bölümlerde açıklandığı gibi) alacaksınız:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/fr/113.webp)


Şimdi bu Invoice'i, `PBN` token ile gerekli nakdi tutan ilk düğümden ödeyeceğiz:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/fr/114.webp)


Ödeme yapılmıştır. Bu, komutu çalıştırarak doğrulanabilir:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/fr/115.webp)


RGB varlıklarını taşıyacak şekilde değiştirilmiş bir Lightning düğümünün nasıl konuşlandırılacağı aşağıda açıklanmıştır. Bu gösterim temel alınmıştır:




- Bir regtest ortamı (`./regtest.sh` aracılığıyla) veya Testnet;
- Bir `bitcoind`, bir dizinleyici ve bir `RGB-proxy-server` tabanlı bir Lightning düğümü (`RGB-lightning-node`);
- Kanal açma/kapama, token verme, Lightning aracılığıyla varlık aktarma vb. için bir dizi JSON REST API'si.


Bu süreç sayesinde:




- Yıldırım angajman işlemleri, bir RGB geçişinin sabitlenmesiyle birlikte ek bir çıkış (OP_RETURN veya Taproot) içerir;
- Transferler, geleneksel Lightning ödemeleriyle tamamen aynı şekilde, ancak bir RGB token eklenerek yapılır;
- Birden fazla RLN düğümü, yol üzerinde hem bitcoin hem de RGB varlığında yeterli likidite olması koşuluyla, birden fazla düğüm arasında ödemeleri yönlendirmek ve denemek için bağlanabilir.


Proje henüz alfa aşamasındadır. Bu nedenle kendinizi test ortamlarıyla (regtest, Testnet) sınırlandırmanız şiddetle tavsiye edilir.


Bu LN-RGB uyumluluğunun ortaya çıkardığı fırsatlar oldukça fazladır: Lightning üzerinde sabit coinler, DEX Layer-2, değiştirilebilir tokenlerin veya NFT'lerin çok düşük maliyetle transferi... Önceki bölümlerde kavramsal mimari ve doğrulama mantığı ana hatlarıyla açıklanmıştır. Artık gelecekteki geliştirmeleriniz veya testleriniz için böyle bir düğümü nasıl kurup çalıştıracağınıza dair pratik bir görüşe sahipsiniz.


# Son Bölüm


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Yorumlar & Derecelendirmeler


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## Sonuç


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>