---
name: Lightning Network Teorisi
goal: Lightning Network'i teknik açıdan keşfedin
objectives:
- Ağ kanallarının işleyişini anlayın.
- HTLC, LNURL ve UTXO terimlerine aşina olun.
- Likidite yönetimini ve LNN ücretlerini asimile edin.
- Lightning Network'ü bir ağ olarak tanıyın.
- Lightning Network'in teorik kullanımlarını anlamak.
---

# Bitcoin'nın İkinci Layer'sine Yolculuk


Bitcoin işlemlerinin geleceği için temel bir sistem olan Lightning Network'in kalbine dalın. LNP201, Lightning'in teknik işleyişi üzerine teorik bir derstir. Bitcoin ödemelerini hızlı, ekonomik ve ölçeklenebilir hale getirmek için tasarlanan bu ikinci Layer ağının temellerini ve mekanizmalarını ortaya çıkarır.


Ödeme kanalları ağı sayesinde Lightning, her bir Exchange'ü Bitcoin Blockchain'e kaydetmeden hızlı ve güvenli işlemler yapılmasını sağlar. Bölümler boyunca, kanalların açılması, yönetilmesi ve kapatılmasının nasıl çalıştığını, güven ihtiyacını en aza indirirken ödemelerin aracı düğümler aracılığıyla nasıl güvenli bir şekilde yönlendirildiğini ve likiditenin nasıl yönetileceğini öğreneceksiniz. Commitment işlemlerinin, HTLC'lerin, iptal anahtarlarının, ceza mekanizmalarının, soğan yönlendirmenin ve faturaların ne olduğunu keşfedeceksiniz.


İster Bitcoin'ya yeni başlayan ister daha deneyimli bir kullanıcı olun, bu eğitim Lightning Network'i anlamak ve kullanmak için değerli bilgiler sağlayacaktır. İlk bölümlerde Bitcoin'nın çalışmasının bazı temellerini ele alacak olsak da, LNP201'e dalmadan önce Satoshi'nin icadının temellerine hakim olmak çok önemlidir.


Keşfinizin tadını çıkarın!


+++

# Giriş

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Kursa Genel Bakış

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


LNP201 kursuna hoş geldiniz!


Bu eğitim, hızlı ve genellikle düşük maliyetli Bitcoin işlemlerini kolaylaştırmak için tasarlanmış bir katman ağı olan Lightning Network hakkında derinlemesine bir teknik anlayış sağlamayı amaçlamaktadır. Ödeme kanallarının açılmasından yönlendirme tekniklerine ve likidite yönetimine kadar bu sistemi yöneten temel kavramları aşamalı olarak keşfedeceksiniz.


**Bölüm 1: Temel Bilgiler**

Lightning Network'ye genel bir giriş yaparak Bitcoin, adresleri, UTXO'ları ve işlemlerin nasıl çalıştığı hakkında temel bilgiler vererek başlayacağız. Bu temel inceleme, Lightning Network'nin güvenli bir şekilde çalışmak için altta yatan Blockchain mekanizmalarına nasıl dayandığını anlamak için gereklidir.


**Bölüm 2: Kanalların Açılması ve Kapatılması**

Bu bölümde, Lightning Network'ün temel taşı olan kanal açma sürecini inceleyeceğiz. Commitment işlemlerinin nasıl oluşturulduğunu, güvenlik için iptal anahtarlarının rolünü ve kanalların işbirliği içinde veya tek taraflı olarak nasıl kapatılabileceğini öğreneceksiniz. Tüm incelikleri kavramanıza yardımcı olmak için her adım kesin ve teknik olarak açıklanacaktır.


**Bölüm 3: Bir Likidite Ağı**

Lightning Network bireysel kanallarla sınırlı değildir; gerçek bir ödeme ağıdır. HTLC'ler kullanılarak işlemlerin aracı düğümler üzerinden nasıl yönlendirilebileceğini göreceğiz. Bu bölüm ayrıca sizi gelen ve giden likiditenin zorluklarıyla tanıştıracak.


**Bölüm 4: Lightning Network Araçları**

Bu bölümde Lightning Network'nin *Faturalar*, *LNURL* ve *Keysend* gibi pratik araçları sunulmaktadır. Ayrıca, sorunsuz ödemeler sağlamak ve Lightning'deki işlemlerinizin verimliliğini en üst düzeye çıkarmak için önemli bir husus olan kanallarınızın likiditesini nasıl yöneteceğinizi de öğreneceksiniz.


**Bölüm 5: Daha İleri Gitmek**

Son olarak, ele alınan kavramları özetleyerek ve Lightning Network hakkındaki bilgilerini derinleştirmek isteyenler için daha ileri konuların önünü açarak eğitimi tamamlayacağız.


Lightning Network'un teknik mekanizmalarını ortaya çıkarmaya hazır mısınız? Hadi içeri dalalım!


---

*İngilizce ders şemalarında karşılaşacağınız bazı terimler ve bunları kendi dilinizde daha iyi anlamanıza yardımcı olacak çevirileri şunlardır:*

| İngilizce          | Çeviri - açıklama             |
| ------------------ | ----------------------------- |
| *timelock*         | Zaman kilidi                  |
| *Revocation Key*   | İptal anahtarı                |
| *invoice*          | Fatura / ödeme talebi         |
| *sig* (signature)  | İmza                          |
| *secret*           | Sır                           |
| *amount*           | Tutar                         |
| *scan QR code*     | QR kodu tara                  |
| *Show QR code*     | QR kodu göster                |
| *Asks the invoice* | Faturayı ister                |
| *Give the invoice* | Faturayı verir                |
| *Payment*          | Ödeme                         |
| *Preimage*         | Ön imaj                       |

# Temel Bilgiler


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## Lightning Network'i Anlamak


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=4315a277-12fe-4946-bb49-a807e60c09a7:::



Lightning Network, Bitcoin protokolü üzerine inşa edilmiş, hızlı ve düşük maliyetli işlemlere olanak sağlamayı amaçlayan bir ödeme kanalları ağıdır. Her bir işlemi Blockchain'e ayrı ayrı kaydetmek zorunda kalmadan, işlemlerin neredeyse anında ve minimum ücretlerle yapılabileceği katılımcılar arasında ödeme kanallarının oluşturulmasına olanak tanır. Böylece Lightning Network, Bitcoin'ün ölçeklenebilirliğini geliştirmeyi ve düşük değerli ödemeler için kullanılabilir hale getirmeyi amaçlamaktadır.


"Ağ" yönünü keşfetmeden önce, Lightning'de **ödeme kanalı** kavramını, nasıl çalıştığını ve özelliklerini anlamak önemlidir. Bu, bu ilk bölümün konusudur.


### Ödeme Kanalı Kavramı


Bir ödeme kanalı iki tarafın, burada **Alice** ve **Bob**, Lightning Network üzerinden Exchange fonlarına izin verir. Her bir kahramanın bir daire ile sembolize edilen bir düğümü vardır ve aralarındaki kanal bir doğru parçası ile temsil edilir.


![LNP201](assets/en/001.webp)


Örneğimizde, Alice'un kanalın kendi tarafında 100.000 satoshi ve Bob'ın 30.000 satoshi olmak üzere toplam 130.000 satoshi vardır ve bu da **kanal kapasitesini** oluşturur.


**Ama Satoshi nedir?**


**Satoshi** (veya "sat") Bitcoin'de bir hesap birimidir. Avro için bir sente benzer şekilde, bir Satoshi basitçe Bitcoin'nin bir kesiridir. Bir Satoshi, **0,00000001 Bitcoin** veya bir Bitcoin'nin yüz milyonda birine eşittir. Bitcoin'nin değeri yükseldikçe Satoshi'ü kullanmak giderek daha pratik hale gelmektedir.


### Kanaldaki Fonların Tahsisi


Ödeme kanalına geri dönelim. Buradaki anahtar kavram "kanalın **tarafıdır**". Her katılımcının kanalın kendi tarafında fonları vardır: Alice 100,000 satoshis ve Bob 30,000. Gördüğümüz gibi, bu fonların toplamı kanalın toplam kapasitesini temsil eder ve bu rakam kanal açıldığında belirlenir.


![LNP201](assets/en/002.webp)


Bir Lightning işlemi örneğini ele alalım. Alice, Bob'ye 40.000 satoshi göndermek isterse, bu mümkündür çünkü yeterli parası (100.000 satoshi) vardır. Bu işlemden sonra Alice'nın elinde 60.000 satoshis, Bob'nin elinde ise 70.000 satoshis olacaktır.


![LNP201](assets/en/003.webp)


Kanal kapasitesi 130,000 satoshis olarak sabit kalmaktadır. Değişen şey fonların tahsisidir. Bu sistem, kişinin sahip olduğundan daha fazla fon göndermesine izin vermez. Örneğin, Bob Alice'e 80,000 satoshi geri göndermek isteseydi, bunu yapamazdı çünkü sadece 70,000 satoshi'si vardı.


Fon tahsisini hayal etmenin bir başka yolu da fonların kanal içinde nerede olduğunu gösteren bir **imleç** hayal etmektir. Başlangıçta, Alice için 100.000 ve Bob için 30.000 satoshi ile, imleç daha çok Bob tarafındadır, çünkü Alice'nin çok daha fazla fonu vardır. İmleç, 40.000 satoshi'lik işlemden sonra, artık 60.000 satoshi'ye sahip olan Alice'ye doğru hafifçe kayacaktır.


![LNP201](assets/en/004.webp)


Bu gösterim, bir kanaldaki fon dengesini hayal etmek için yararlı olabilir.


### Bir Ödeme Kanalının Temel Kuralları


Hatırlanması gereken ilk nokta **kanal kapasitesinin** sabit olduğudur. Bir nevi bir borunun çapı gibidir: kanaldan tek seferde gönderilebilecek maksimum fon miktarını belirler.

Bir örnek verelim: Alice'nin elinde 130.000 satoshi varsa, tek bir işlemde Bob'e en fazla 130.000 satoshi gönderebilir. Ancak, Bob daha sonra bu fonları kısmen veya tamamen Alice'ye geri gönderebilir.


Anlaşılması gereken önemli nokta, kanalın sabit kapasitesinin tek bir işlemin maksimum tutarını sınırladığı, ancak olası işlemlerin toplam sayısını veya kanal içinde değiş tokuş edilen toplam fon hacmini sınırlamadığıdır.


**Bu bölümden ne anlamalısınız?**



- Bir kanalın kapasitesi sabittir ve tek bir işlemde gönderilebilecek maksimum miktarı belirler.
- Bir kanaldaki fonlar iki katılımcı arasında dağıtılır ve her biri diğerine yalnızca kendi tarafında sahip olduğu fonları gönderebilir.
- Böylece Lightning Network, kanalların kapasitesinin getirdiği sınırlamalara uyarak fonların hızlı ve verimli bir şekilde Exchange'e aktarılmasını sağlar.


Lightning Network'nın temellerini attığımız bu ilk bölümün sonuna geldik. Gelecek bölümlerde, bir kanalın nasıl açılacağını göreceğiz ve burada tartışılan kavramları daha derinlemesine inceleyeceğiz.


## Bitcoin, Adresler, UTXO ve İşlemler


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Bu bölüm biraz özel çünkü doğrudan Lightning'e değil, Bitcoin'a adanacak. Aslında Lightning Network, Bitcoin'ın üstünde bir Layer'dir. Bu nedenle, sonraki bölümlerde Lightning'in işleyişini doğru bir şekilde kavramak için Bitcoin'ın bazı temel kavramlarını anlamak çok önemlidir. Bu bölümde, Bitcoin alıcı adreslerinin, UTXO'ların ve Bitcoin işlemlerinin işleyişinin temellerini gözden geçireceğiz.


### Bitcoin Adresler, Özel Anahtarlar ve Açık Anahtarlar


Bir Bitcoin Address, kendisi de bir **özel anahtardan** hesaplanan bir **genel anahtardan** türetilen bir dizi karakterdir. Kesinlikle bildiğiniz gibi, bitcoinleri kilitlemek için kullanılır, bu da onları Wallet'imizde almaya eşdeğerdir.


Özel anahtar **asla paylaşılmaması gereken** gizli bir unsurdur, açık anahtar ve Address ise güvenlik riski olmaksızın paylaşılabilir (ifşa edilmeleri yalnızca gizliliğiniz için bir risk teşkil eder). İşte bu eğitim boyunca benimseyeceğimiz ortak bir gösterim:



- **Özel anahtarlar** **dikey olarak** temsil edilecektir.
- **Açık anahtarlar** **yatay** olarak temsil edilecektir.
- Renkleri onlara kimin sahip olduğunu gösterir (Alice turuncu ve Bob siyah...).


### Bitcoin İşlemleri: Fon Gönderme ve Komut Dosyaları


Bitcoin'de bir işlem, bir Address'ten diğerine para göndermeyi içerir. Alice'nin Bob'e 0,002 Bitcoin göndermesi örneğini ele alalım. Alice, işlemi **imzalamak** için Address ile ilişkili özel anahtarı kullanır ve böylece bu fonları gerçekten harcayabildiğini kanıtlar. Peki bu işlemin arkasında tam olarak ne oluyor? Bir Bitcoin Address üzerindeki fonlar, fonları harcamak için belirli koşullar getiren bir tür mini program olan bir **komut dosyası** tarafından kilitlenir.


En yaygın komut dosyası, Address ile ilişkili özel anahtarla bir imza gerektirir. Alice kendi özel anahtarıyla bir işlemi imzaladığında, fonları bloke eden betiğin kilidini açar ve fonlar transfer edilebilir. Fonların transferi, bu fonlara yeni bir komut dosyası eklenmesini içerir ve bu kez onları harcamak için **Bob'nın** özel anahtar imzasının gerekli olacağını şart koşar.


![LNP201](assets/en/005.webp)


### UTXO'lar: Harcanmamış İşlem Çıkışları


Bitcoin'de, aslında Exchange doğrudan bitcoin değil, **[UTXO](https://planb.academy/resources/glossary/utxo)s** (_Unspent Transaction Outputs_), yani "harcanmamış işlem çıktıları".


Bir UTXO, herhangi bir değerde olabilen bir Bitcoin parçasıdır, örneğin **2.000 bitcoin**, **8 bitcoin** veya hatta **8.000 Sats**. Her UTXO bir komut dosyası tarafından kilitlenir ve harcamak için komut dosyasının koşullarını yerine getirmek gerekir, genellikle belirli bir alıcı Address'a karşılık gelen özel anahtarla bir imza.


UTXO'lar bölünemez. Temsil ettikleri bitcoin miktarını harcamak için kullanıldıkları her seferinde, bu harcama bütün olarak yapılmalıdır. Bu biraz banknotlara benzer: 10 €'luk bir faturanız varsa ve fırıncıya 5 € borçluysanız, faturayı ikiye bölemezsiniz. Ona 10 €'luk banknotu vermek zorundasınız ve o da size para üstü olarak 5 € verecektir. Bu, Bitcoin'teki UTXO'lar için de tamamen aynı prensiptir! Örneğin, Alice kendi özel anahtarıyla bir betiğin kilidini açtığında, UTXO'nın tamamının kilidini açmış olur. Bu UTXO tarafından temsil edilen fonların yalnızca bir kısmını Bob'ye göndermek isterse, bunu birkaç küçük parçaya "bölebilir". Daha sonra 0,0015 BTC'yi Bob'ye gönderecek ve geri kalan 0,0005 BTC'yi bir **değiştirme Address**'e gönderecektir.


İşte 2 çıkışlı bir işlem örneği:



- Bob'un özel anahtar imzasını gerektiren bir komut dosyası tarafından kilitlenen Bob için 0,0015 BTC'lik bir UTXO.
- Kendi imzasını gerektiren bir komut dosyası tarafından kilitlenen Alice için 0,0005 BTC'lik bir UTXO.


![LNP201](assets/en/006.webp)


### Çoklu İmza Adresleri


Tek bir açık anahtardan üretilen basit adreslere ek olarak, birden fazla açık anahtardan **çoklu-imzalı adresler** oluşturmak da mümkündür. Lightning Network için özellikle ilginç bir durum, iki açık anahtardan oluşturulan **2/2 çoklu-imzalı Address**'tür:


![LNP201](assets/en/007.webp)


Bu 2/2 çoklu-imzalı Address ile kilitlenen fonları harcamak için, açık anahtarlarla ilişkili iki özel anahtarla imzalamak gerekir.


![LNP201](assets/en/008.webp)


Bu tip Address tam olarak Lightning Network üzerindeki ödeme kanallarının Bitcoin Blockchain üzerindeki temsilidir.


**Bu bölümden ne anlamalısınız?**



- Bir **Bitcoin Address**, kendisi de bir özel anahtardan türetilen bir açık anahtardan türetilir.
- Bitcoin'deki fonlar **komut dosyaları** tarafından kilitlenir ve bu fonları harcamak için, genellikle ilgili özel anahtarla bir imza sağlamayı içeren komut dosyasını tatmin etmek gerekir.
- **UTXO'lar** komut dosyaları tarafından kilitlenen bitcoin parçalarıdır ve Bitcoin'deki her işlem bir UTXO'ün kilidini açıp karşılığında bir veya daha fazla yenisini oluşturmaktan oluşur.
- 2/2 **çoklu imza adresleri** fonları harcamak için iki özel anahtarın imzalanmasını gerektirir. Bu özel adresler Lightning bağlamında ödeme kanalları oluşturmak için kullanılır.


Bitcoin ile ilgili bu bölüm, bundan sonrası için bazı temel kavramları gözden geçirmemizi sağladı. Bir sonraki bölümde, özellikle Lightning Network üzerindeki kanalların açılmasının nasıl çalıştığını keşfedeceğiz.


# Kanalların Açılması ve Kapatılması


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Kanal Açma


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


Bu bölümde, Lightning Network üzerinde bir ödeme kanalının nasıl açılacağını daha net bir şekilde göreceğiz ve bu işlem ile temel Bitcoin sistemi arasındaki bağlantıyı anlayacağız.


### Yıldırım Kanalları


İlk bölümde gördüğümüz gibi, Lightning'deki bir **ödeme kanalı** iki katılımcı (örneklerimizde **Alice** ve **Bob**) arasında fon alışverişi için bir "boru" ile karşılaştırılabilir. Bu kanalın kapasitesi, her iki taraftaki mevcut fonların toplamına karşılık gelir. Örneğimizde, Alice **100.000 satoshis** ve Bob **30.000 satoshis** olmak üzere toplam **130.000 satoshis** kapasiteye sahiptir.


![LNP201](assets/en/009.webp)


### Bilgi Düzeyleri Exchange


Lightning Network üzerindeki farklı Exchange seviyelerini net bir şekilde ayırt etmek çok önemlidir:



- **Eşler arası iletişim (Lightning protokolü)**: Bunlar Lightning düğümlerinin iletişim kurmak için birbirlerine gönderdikleri mesajlardır. Bu mesajları diyagramlarımızda kesikli siyah çizgilerle göstereceğiz.
- **Ödeme kanalları (Lightning protokolü)**: Bunlar, Lightning'de fon alışverişi için kullanılan ve düz siyah çizgilerle göstereceğimiz yollardır.
- **Bitcoin işlemleri (Bitcoin protokolü)**: Bunlar, turuncu çizgilerle göstereceğimiz zincir üzerinde yapılan işlemlerdir.


![LNP201](assets/en/010.webp)


Bir Lightning düğümünün bir kanal açmadan P2P protokolü aracılığıyla iletişim kurabileceğini, ancak Exchange fonları için bir kanalın gerekli olduğunu belirtmek gerekir.


### Lightning Kanalı Açma Adımları



- **Mesaj Exchange**: Alice, Bob ile bir kanal açmak istiyor. Ona kanala yatırmak istediği miktarı (130.000 Sats) ve açık anahtarını içeren bir mesaj gönderir. Bob kendi açık anahtarını paylaşarak yanıt verir.


![LNP201](assets/en/011.webp)



- Çoklu-imzalı **Address**'nin oluşturulması: Bu iki açık anahtarla Alice bir **2/2 çoklu-imzalı Address** oluşturur, yani daha sonra bu **Address**'ye yatırılacak fonların harcanabilmesi için her iki imzanın da (Alice ve Bob) bulunması gerekir.


![LNP201](assets/en/012.webp)



- **Para yatırma işlemi**: Alice, bu çok-imzalı Address'e para yatırmak için bir Bitcoin işlemi hazırlar. Örneğin, bu çok-imzalı Address'e **130.000 satoshis** göndermeye karar verebilir. Bu işlem **oluşturulmuş ancak henüz Blockchain'te yayınlanmamıştır**.


![LNP201](assets/en/013.webp)



- **Para çekme işlemi**: Para yatırma işlemini yayınlamadan önce, Alice bir para çekme işlemi oluşturur, böylece Bob ile bir sorun olması durumunda fonlarını geri alabilir. Aslında, Alice para yatırma işlemini yayınladığında, Sats'u 2/2 çoklu-imzalı Address'de kilitlenecektir ve kilidin açılması için hem kendi imzası hem de Bob'un imzası gerekmektedir. Alice, fonlarını geri almasını sağlayan para çekme işlemini oluşturarak bu kayıp riskine karşı koruma sağlar.


![LNP201](assets/en/014.webp)



- **Bob'nin imzası**: Alice para yatırma işlemini kanıt olarak Bob'ye gönderir ve ondan para çekme işlemini imzalamasını ister. Para çekme işleminde Bob'nin imzası alındıktan sonra, Alice istediği zaman fonlarını geri alabileceğinden emin olur, çünkü artık çoklu imzanın kilidini açmak için yalnızca kendi imzası gereklidir.


![LNP201](assets/en/015.webp)



- **Para yatırma işleminin yayınlanması**: Bob'nın imzası alındıktan sonra, Alice para yatırma işlemini Bitcoin Blockchain üzerinde yayınlayabilir ve böylece iki kullanıcı arasındaki Lightning kanalını resmi olarak açabilir.


![LNP201](assets/en/016.webp)


### Kanal ne zaman açık?


Para yatırma işlemi bir Bitcoin bloğuna dahil edildiğinde ve belirli bir onay derinliğine (takip eden blok sayısı) ulaştığında kanal açık kabul edilir.


**Bu bölümden ne hatırlamalısınız?**



- Bir kanalın açılması, iki taraf arasındaki **mesajların** Exchange'i ile başlar (miktarların ve açık anahtarların Exchange'i).
- Bir **2/2 çoklu-imzalı Address** oluşturularak ve bir Bitcoin işlemi aracılığıyla bu kanala para yatırılarak bir kanal oluşturulur.
- Kanalı açan kişi, para yatırma işlemini yayınlamadan önce diğer tarafça imzalanmış bir para çekme işlemi yoluyla **fonlarını geri alabileceklerini** garanti eder.


Bir sonraki bölümde, bir kanal içindeki Lightning işleminin teknik işleyişini inceleyeceğiz.


## Commitment Transaction


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


Bu bölümde, Lightning Network'de bir kanal içindeki bir işlemin, yani fonların kanalın bir tarafından diğer tarafına taşınmasının teknik işleyişini keşfedeceğiz.


### Kanal yaşam döngüsünün hatırlatılması


Daha önce görüldüğü gibi, bir Lightning kanalı bir Bitcoin işlemi aracılığıyla bir **açılış** ile başlar. Kanal, yine bir Bitcoin işlemi aracılığıyla herhangi bir zamanda **kapatılabilir**. Bu iki an arasında, Bitcoin Blockchain'ten geçmeden kanal içinde neredeyse sonsuz sayıda işlem gerçekleştirilebilir. Kanaldaki bir işlem sırasında neler olduğunu görelim.


![LNP201](assets/en/017.webp)


### Kanalın ilk durumu


Kanalın açılması sırasında Alice, kanalın çoklu imzalı Address'ine **130.000 satoshis** yatırmıştır. Dolayısıyla, ilk durumda tüm fonlar Alice'nın tarafındadır. Kanalı açmadan önce, Alice ayrıca Bob'ye kanalı kapatmak istemesi halinde fonlarını geri almasını sağlayacak bir **çekme işlemi** imzalatmıştır.


![LNP201](assets/en/018.webp)


### Yayımlanmamış İşlemler: Commitment İşlemleri


Alice, Bob'e fon göndermek için kanalda bir işlem yaptığında, fon dağıtımındaki bu değişikliği yansıtmak için yeni bir Bitcoin işlemi oluşturulur. **Commitment Transaction** olarak adlandırılan bu işlem Blockchain'de yayınlanmaz ancak Lightning işleminin ardından kanalın yeni durumunu temsil eder.


Alice'ün Bob'e 30.000 satoshi gönderdiği bir örneği ele alalım:



- **Başlangıçta**: Alice'da 130,000 satoshis var.
- **İşlemden sonra**: Alice 100,000 satoshis ve Bob 30,000 satoshis'e sahiptir.

Bu transferi doğrulamak için Alice ve Bob, çok-imzalı Address'tan Alice'ye **100.000 satoshi** ve Bob'e **30.000 satoshi** gönderecek yeni bir **yayınlanmamış Bitcoin işlemi** oluşturur. Her iki taraf da bu işlemi bağımsız olarak, ancak aynı verilerle (miktarlar ve adresler) oluşturur. Oluşturulduktan sonra, her biri işlemi imzalar ve imzalarını diğeriyle değiştirir. Bu, taraflardan birinin ana Bitcoin Blockchain üzerindeki kanal payını geri kazanmak için gerekirse işlemi istediği zaman yayınlamasına olanak tanır.

![LNP201](assets/en/019.webp)


### Transfer Süreci: Invoice


Bob para almak istediğinde, Alice'ye 30.000 satoshis için bir **_[invoice](https://planb.academy/resources/glossary/invoice-lightning)_** gönderir. Alice daha sonra kanal içinde transferi başlatarak bu Invoice'ya ödeme yapmaya devam eder. Gördüğümüz gibi, bu süreç yeni bir **Commitment Transaction**'in oluşturulmasına ve imzalanmasına dayanır.


Her bir Commitment Transaction, transferden sonra kanaldaki yeni fon dağılımını temsil eder. Bu örnekte, işlemden sonra Bob'de 30.000 satoshis ve Alice'de 100.000 satoshis bulunmaktadır. İki katılımcıdan biri bu Commitment Transaction'u Blockchain'te yayınlamaya karar verirse, kanalın kapanmasına neden olur ve fonlar bu son dağıtıma göre dağıtılır.


![LNP201](assets/en/020.webp)


### İkinci Bir İşlemden Sonra Yeni Durum


Başka bir örnek verelim: Alice'ün Bob'e 30.000 satoshis gönderdiği ilk işlemden sonra, Bob Alice'e **10.000 satoshis** geri göndermeye karar verir. Bu, kanalda yeni bir durum yaratır. Yeni **Commitment Transaction** bu güncellenmiş dağılımı temsil edecektir:



- **Alice** şu anda **110,000 satoshis** değerine sahip.
- **Bob**'de **20,000 satoshis** var.


![LNP201](assets/en/021.webp)


Yine, bu işlem Blockchain'de yayınlanmaz ancak kanalın kapatılması durumunda herhangi bir zamanda yayınlanabilir.


Özetle, fonlar bir Lightning kanalı içinde transfer edildiğinde:



- Alice ve Bob, yeni fon dağılımını yansıtan yeni bir **Commitment Transaction** oluşturur.
- Bu Bitcoin işlemi her iki tarafça **imzalanır**, ancak kanal açık kaldığı sürece Bitcoin Blockchain'de **yayınlanmaz**.
- Commitment işlemleri, her katılımcının son imzalanan işlemi yayınlayarak Bitcoin Blockchain üzerinde istediği zaman fonlarını geri alabilmesini sağlar.


Ancak, bu sistemin bir sonraki bölümde Address olarak adlandıracağımız potansiyel bir kusuru vardır. Her bir katılımcının diğer tarafın hile yapma girişimine karşı kendini nasıl koruyabileceğini göreceğiz.


## İptal Anahtarı


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

Bu bölümde, her bir tarafın bir kanaldaki kurallara uymasını sağlayarak hileye karşı koruma mekanizmalarını tartışarak Lightning Network'de işlemlerin nasıl çalıştığını daha derinlemesine inceleyeceğiz.


### Hatırlatma: Commitment İşlemleri


Daha önce görüldüğü gibi, Lightning'deki işlemler yayınlanmamış **Commitment işlemlerine** dayanmaktadır. Bu işlemler kanaldaki mevcut fon dağılımını yansıtır. Yeni bir Lightning işlemi yapıldığında, kanalın yeni durumunu yansıtmak için yeni bir Commitment Transaction oluşturulur ve her iki tarafça imzalanır.


Basit bir örnek verelim:



- **İlk durum**: Alice'de **100.000 satoshis**, Bob'te **30.000 satoshis** vardır.
- Alice'in Bob'ya **40.000 satoshis** gönderdiği bir işlemden sonra, yeni Commitment Transaction fonları aşağıdaki gibi dağıtır:
  - Alice: **60,000 satoshis**
  - Bob: **70,000 satoshis**


![LNP201](assets/en/022.webp)


Her iki taraf da istediği zaman kanalı kapatmak ve fonlarını geri almak için imzaladığı **en son Commitment Transaction**'u yayınlayabilir.


### Kusur: Eski Bir İşlemi Yayınlayarak Hile Yapmak


Taraflardan biri eski bir Commitment Transaction yayınlayarak **hile** yapmaya karar verirse potansiyel bir sorun ortaya çıkar. Örneğin, Alice gerçekte sadece **60.000** satoshisi olmasına rağmen **100.000 satoshisi** olan eski bir Commitment Transaction yayınlayabilir. Bu sayede Bob'den **40.000 satoshis** çalabilir.


![LNP201](assets/en/023.webp)


Daha da kötüsü, Alice, kanal açılmadan önce **130.000 satoshis'e** sahip olduğu ilk para çekme işlemini yayınlayabilir ve böylece kanalın tüm fonlarını çalabilir.


![LNP201](assets/en/024.webp)


### Çözüm: İptal Anahtarı ve Zaman Kilidi


Alice tarafından bu tür hileleri önlemek için, Lightning Network'te, Commitment işlemlerine **güvenlik mekanizmaları** eklenmiştir:



- **Zaman kilidi**: Her Commitment Transaction, Alice'ın fonları için bir zaman kilidi içerir. Zaman kilidi, bir işlemin bir bloğa eklenmesi için karşılanması gereken bir zaman koşulu belirleyen bir Smart contract ilkelidir. Bu, Alice'un Commitment işlemlerinden birini yayınlaması durumunda belirli sayıda blok geçene kadar fonlarını geri alamayacağı anlamına gelir. Bu zaman kilidi Commitment Transaction'nin onaylanmasından itibaren uygulanmaya başlar. Süresi genellikle kanalın büyüklüğü ile orantılıdır, ancak manuel olarak da yapılandırılabilir.
- **İptal Anahtarı**: Alice'nin fonları, **iptal anahtarına** sahip olması halinde Bob tarafından da hemen harcanabilir. Bu anahtar, Alice tarafından tutulan bir sır ve Bob tarafından tutulan bir sırdan oluşur. Bu sırrın her Commitment Transaction için farklı olduğunu unutmayın.

Bu 2 birleşik mekanizma sayesinde, Bob, Alice'in hile yapma girişimini tespit etmek ve iptal anahtarıyla çıktısını geri alarak onu cezalandırmak için zamana sahiptir, bu da Bob için kanalın tüm fonlarını kurtarmak anlamına gelir. Yeni Commitment Transaction'ümüz şimdi şöyle görünecektir:


![LNP201](assets/en/025.webp)


Gelin bu mekanizmanın işleyişini birlikte detaylandıralım.


### İşlem Güncelleme Süreci


Alice ve Bob kanalın durumunu yeni bir Lightning işlemi ile güncellediklerinde, önceki Commitment Transaction için kendi **sırlarını** önceden Exchange yaparlar (eski hale gelecek olan ve birinin hile yapmasına izin verebilecek olan). Bu, kanalın yeni durumunda:



- Alice ve Bob, Lightning işleminden sonra fonların mevcut dağılımını temsil eden yeni bir Commitment Transaction'e sahiptir.
- Her biri bir önceki işlem için diğerinin sırrına sahiptir, bu da yalnızca biri Bitcoin düğümlerinin mempool'larında eski bir durumla bir işlem yayınlayarak hile yapmaya çalışırsa iptal anahtarını kullanmalarına izin verir. Aslında, diğer tarafı cezalandırmak için hem sırları hem de imzalı girdiyi içeren diğerinin Commitment Transaction'ünü tutmak gerekir. Bu işlem olmadan, iptal anahtarı tek başına işe yaramaz. Bu işlemi elde etmenin tek yolu, mempool'lardan (onay bekleyen işlemlerde) veya zaman kilidi sırasında Blockchain'teki onaylanmış işlemlerden almaktır, bu da diğer tarafın kasıtlı olsun ya da olmasın hile yapmaya çalıştığını kanıtlar.


Bu süreci iyi anlamak için bir örnek verelim:



- **Başlangıç Durumu**: Alice'de **100.000 satoshis**, Bob'de **30.000 satoshis** vardır.


![LNP201](assets/en/026.webp)



- Bob, Lightning kanalı aracılığıyla Alice'dan 40.000 satoshis almak istiyor. Bunu yapmak için:
   - Önceki Commitment Transaction'inin iptal anahtarı için sırrıyla birlikte ona bir Invoice gönderir.
   - Yanıt olarak Alice, Bob'in yeni Commitment Transaction'ü için imzasını ve önceki işleminin iptal anahtarı için sırrını sağlar.
   - Son olarak, Bob, Alice'nin yeni Commitment Transaction'sı için imzasını gönderir.
   - Bu takaslar, Alice'ın kendi kanalları aracılığıyla Lightning üzerinden Bob'e **40.000 satoshis** göndermesine olanak tanıyor ve yeni Commitment işlemleri artık bu yeni fon dağıtımını yansıtıyor.


![LNP201](assets/en/027.webp)



- Alice hala **100.000 satoshis** sahibi olduğu eski Commitment Transaction'yi yayınlamaya çalışırsa, iptal anahtarını elde eden Bob bu anahtarı kullanarak fonları hemen geri alabilirken, Alice zaman kilidi tarafından engellenir.


![LNP201](assets/en/028.webp)


Bu durumda, Bob'nın hile yapmaya çalışmakta hiçbir ekonomik çıkarı olmasa bile, yine de bunu yaparsa, Alice de kendisine aynı garantileri sunan simetrik korumadan yararlanır.


**Bu bölümden ne anlamalısınız?**


Lightning Network üzerindeki **Commitment işlemleri** hem hile yapma riskini hem de hile yapma teşviklerini azaltan güvenlik mekanizmaları içerir. Yeni bir Commitment Transaction imzalamadan önce, Alice ve Bob önceki Commitment işlemleri için kendi **sırlarını** Exchange yaparlar. Alice eski bir Commitment Transaction'yi yayınlamaya çalışırsa, Bob **iptal anahtarını** kullanarak tüm fonları Alice'den önce geri alabilir (çünkü zaman kilidi tarafından engellenmiştir), bu da onu hile yapmaya çalıştığı için cezalandırır.


Bu güvenlik sistemi, katılımcıların Lightning Network kurallarına uymalarını sağlar ve eski Commitment işlemlerini yayınlayarak kar elde edemezler.


Eğitimin bu noktasında, artık Lightning kanallarının nasıl açıldığını ve bu kanallar içindeki işlemlerin nasıl çalıştığını biliyorsunuz. Bir sonraki bölümde, bir kanalı kapatmanın ve ana Blockchain'teki bitcoinlerinizi kurtarmanın farklı yollarını keşfedeceğiz.


## Kanal Kapatma


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


Bu bölümde, tıpkı bir kanal açmak gibi bir Bitcoin işlemi aracılığıyla yapılan Lightning Network üzerindeki **bir kanalı kapatmayı** tartışacağız. Bir kanal içindeki işlemlerin nasıl çalıştığını gördükten sonra, şimdi bir kanalın nasıl kapatılacağını ve Bitcoin Blockchain üzerindeki fonların nasıl geri alınacağını görmenin zamanı geldi.


### Kanal yaşam döngüsünün hatırlatılması


Bir kanalın **yaşam döngüsü** bir Bitcoin işlemi aracılığıyla **açılmasıyla** başlar, ardından içinde Lightning işlemleri yapılır ve son olarak, taraflar fonlarını geri almak istediklerinde, kanal ikinci bir Bitcoin işlemi aracılığıyla **kapanır**. Lightning üzerinde yapılan ara işlemler, yayınlanmamış **Commitment işlemleri** ile temsil edilir.


![LNP201](assets/en/029.webp)


### Üç tür kanal kapanması


Bu kanalı kapatmanın **iyi, kaba ve kaçak** olarak adlandırılabilecek üç ana yolu vardır (Andreas Antonopoulos'un _Mastering the Lightning Network_ kitabından esinlenilmiştir):



- **İyi**: Alice ve Bob'nin kanalı kapatmayı kabul ettiği **işbirliğine dayalı kapatma**.
- **Kötü**: Taraflardan birinin kanalı dürüstçe, ancak diğerinin rızası olmadan kapatmaya karar verdiği **zorla kapatma**.
- **Çirkin**: Taraflardan birinin eski bir Commitment Transaction (fonların gerçek ve adil dağılımını yansıtan sonuncusu hariç herhangi biri) yayınlayarak fon çalmaya çalıştığı **hile ile kapatma**.


Bir örnek verelim:



- Alice **100.000 satoshis** ve Bob **30.000 satoshis** değerine sahiptir.
- Bu dağıtım, yayınlanmayan ancak kanalın kapatılması durumunda yayınlanabilecek **2 Commitment işlemine** (kullanıcı başına bir tane) yansıtılır.


![LNP201](assets/en/030.webp)


### İyi: kooperatif kapanışı


Bir **işbirlikçi kapatmada**, Alice ve Bob kanalı kapatmayı kabul eder. Şöyle olacak:



- Alice, kanalı kapatmayı önermek için Lightning iletişim protokolü aracılığıyla Bob'e bir mesaj gönderir.
- Bob kabul eder ve iki taraf kanalda başka işlem yapmaz.


![LNP201](assets/en/031.webp)



- Alice ve Bob **kapanış işleminin** ücretlerini birlikte müzakere eder. Bu ücretler genellikle kapanış anındaki Bitcoin ücret piyasasına göre hesaplanır. Kapanış ücretlerini ödeyenin **her zaman kanalı açan kişi** (örneğimizde Alice) olduğunu unutmamak önemlidir.
- Yeni bir **kapanış işlemi** oluştururlar. Bu işlem bir Commitment Transaction'e benzer, ancak zaman kilitleri veya iptal mekanizmaları yoktur, çünkü her iki taraf da işbirliği yapmaktadır ve hile riski yoktur. Bu işbirlikçi kapanış işlemi bu nedenle Commitment işlemlerinden farklıdır.


Örneğin, Alice **100.000 satoshis** ve Bob **30.000 satoshis** sahibiyse, kapanış işlemi zaman kısıtlaması olmaksızın Alice'in Address'ine **100.000 satoshis** ve Bob'in Address'ine **30.000 satoshis** gönderecektir. Bu işlem her iki tarafça imzalandıktan sonra Alice tarafından yayınlanır. İşlem Bitcoin Blockchain'de onaylandıktan sonra Lightning kanalı resmi olarak kapanacaktır.


![LNP201](assets/en/032.webp)


**Kooperatif kapatma** tercih edilen kapatma yöntemidir çünkü hızlıdır (zaman kilidi yoktur) ve işlem ücretleri mevcut Bitcoin piyasa koşullarına göre ayarlanır. Bu, işlemin mempool'larda bloke edilmesi riskine yol açabilecek çok az ödeme yapılmasını veya katılımcılar için gereksiz mali kayıplara yol açacak şekilde gereksiz yere fazla ödeme yapılmasını önler.


### Kötü: zorla kapatma


Alice'ün düğümü Bob'in düğümüne işbirlikçi bir kapatma isteyen bir mesaj gönderdiğinde, yanıt vermezse (örneğin, bir internet kesintisi veya teknik bir sorun nedeniyle), Alice **son imzalı Commitment Transaction'ü** yayınlayarak **zorla kapatma** ile devam edebilir.

Bu durumda, Alice basitçe son Commitment Transaction'yı yayınlayacaktır, bu da kanalın son Lightning işleminin doğru fon dağıtımıyla gerçekleştiği andaki durumunu yansıtır.


![LNP201](assets/en/033.webp)


Bu işlem, Alice'in fonları için bir **zaman kilidi** içermekte ve kapanışı daha yavaş hale getirmektedir.


![LNP201](assets/en/034.webp)


Ayrıca, Commitment Transaction'un ücretleri, işlem oluşturulduğunda, bazen birkaç ay önce belirlendiğinden, kapanış sırasında uygun olmayabilir. Genel olarak, Yıldırım müşterileri gelecekteki sorunlardan kaçınmak için ücretleri abartır, ancak bu aşırı ücretlere veya tersine çok düşük ücretlere yol açabilir.


Özetle, **zorla kapatma** eşin artık yanıt vermediği durumlarda son çare olarak başvurulan bir seçenektir. İşbirlikçi bir kapatmadan daha yavaş ve daha az ekonomiktir. Bu nedenle mümkün olduğunca kaçınılmalıdır.


### Hile: Hile yapmak


Son olarak, **hile** ile kapanış, taraflardan biri eski bir Commitment Transaction'ı yayınlamaya çalıştığında, genellikle olması gerekenden daha fazla fon tuttuklarında ortaya çıkar. Örneğin, Alice **120.000 satoshiye** sahip olduğu eski bir işlemi yayınlayabilir, oysa şu anda sadece **100.000** satoshiye sahiptir.


![LNP201](assets/en/035.webp)


Bob, bu hileyi önlemek için, Alice'nın eski bir işlemi yayınlamadığından emin olmak için Bitcoin Blockchain ve onun Mempool'ini izler. Bob bir hile girişimi tespit ederse, Alice'nın fonlarını kurtarmak için **iptal anahtarını** kullanabilir ve kanalın tüm fonlarını alarak onu cezalandırabilir. Alice, çıktısındaki zaman kilidi tarafından engellendiğinden, Bob'nin sahip olduğu bir Address'teki tüm tutarı kurtarmak için kendi tarafında bir zaman kilidi olmadan harcayacak zamanı vardır.


![LNP201](assets/en/036.webp)


Açıkçası, Bob, Alice'un çıktısı üzerindeki zaman kilidinin dayattığı süre içinde hareket etmezse hile potansiyel olarak başarılı olabilir. Bu durumda, Alice'un çıktısının kilidi açılır ve kontrol ettiği bir Address'e yeni bir çıktı oluşturmak için onu tüketmesine izin verilir.


**Bu bölümden ne anlamalısınız?**


Bir kanalı kapatmanın üç yolu vardır:



- **Kooperatif Kapatma**: Her iki tarafın da kanalı kapatmayı kabul ettiği ve özel bir kapanış işlemi yayınladığı hızlı ve daha ucuz.
- **Zorla Kapatma**: Potansiyel olarak uygun olmayan ücretler ve kapanışı yavaşlatan bir zaman kilidi ile bir Commitment Transaction yayınlamaya dayandığından daha az arzu edilir.
- **Hile**: Taraflardan biri eski bir işlemi yayınlayarak fon çalmaya çalışırsa, diğeri bu hileyi cezalandırmak için iptal anahtarını kullanabilir.


İlerleyen bölümlerde Lightning Network'yi daha geniş bir perspektiften inceleyerek ağının nasıl çalıştığına odaklanacağız.


# Bir Likidite Ağı


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Lightning Network


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


Bu bölümde, bir ödeme kanalıyla doğrudan bağlı olmasalar bile Lightning Network'teki ödemelerin bir alıcıya nasıl ulaşabileceğini keşfedeceğiz. Lightning aslında, fonların diğer katılımcıların kanalları aracılığıyla uzaktaki bir düğüme gönderilmesine olanak tanıyan bir **ödeme kanalları ağıdır**. Ödemelerin ağ boyunca nasıl yönlendirildiğini, likiditenin kanallar arasında nasıl hareket ettiğini ve işlem ücretlerinin nasıl hesaplandığını keşfedeceğiz.


### Ödeme Kanalları Ağı


Lightning Network'te bir işlem, iki düğüm arasında bir fon transferine karşılık gelir. Önceki bölümlerde görüldüğü gibi, Lightning işlemlerini gerçekleştirmek için biriyle bir kanal açmak gerekir. Bu kanal, On-Chain bakiyesini geri almak için kapatmadan önce neredeyse sonsuz sayıda off-chain işlemine izin verir. Ancak bu yöntemin, para almak veya göndermek için diğer kişiyle doğrudan bir kanal gerektirmesi gibi bir dezavantajı vardır, bu da her kanal için bir açılış işlemi ve bir kapanış işlemi anlamına gelir. Bu kişiyle çok sayıda ödeme yapmayı planlıyorsam, bir kanal açmak ve kapatmak uygun maliyetli hale gelir. Tersine, yalnızca birkaç Lightning işlemi gerçekleştirmem gerekiyorsa, doğrudan bir kanal açmak avantajlı değildir, çünkü sınırlı sayıda off-chain işlemi için bana 2 On-Chain işlemine mal olacaktır. Bu durum, örneğin, geri dönmeyi planlamadan bir satıcıda Lightning ile ödeme yapmak istendiğinde ortaya çıkabilir.


Bu sorunu çözmek için Lightning Network, bir ödemenin çeşitli kanallar ve aracı düğümler üzerinden yönlendirilmesine olanak tanır, böylece diğer kişiyle doğrudan bir kanal olmadan bir işlem yapılmasını sağlar.


Örneğin, şunu hayal edin:



- **Alice** (turuncu renkte) **Suzie** (gri renkte) ile kendi tarafında **100.000 satoshis** ve Suzie'nin tarafında **30.000 satoshis** olan bir kanala sahiptir.
- **Suzie**, **250.000 satoshis** sahibi olduğu ve **Bob**'un satoshis sahibi olmadığı **Bob** ile bir kanala sahiptir.


![LNP201](assets/en/037.webp)


Alice, Bob ile doğrudan bir kanal açmadan ona para göndermek isterse, Suzie üzerinden gitmek zorunda kalacak ve her kanalın her iki taraftaki likiditeyi ayarlaması gerekecektir. **Gönderilen satoshiler kendi kanalları içinde kalır**; aslında kanalları "geçmezler", ancak transfer her bir kanaldaki iç likiditenin ayarlanması yoluyla yapılır.


Alice'ün Bob'e **50.000 satoshis** göndermek istediğini varsayalım:



- **Alice** ortak kanallarından **Suzie**'ye 50.000 satoshi gönderir.
- **Suzie** bu transferi kendi kanalından **Bob**'ya 50.000 satoshi göndererek tekrarlar.


![LNP201](assets/en/038.webp)


Böylece ödeme, her bir kanaldaki likidite hareketi yoluyla Bob'a yönlendirilir. İşlemin sonunda, Alice 50,000 Sats'e sahip olur. Başlangıçta 100.000'i olduğu için gerçekten de 50.000 Sats transfer etmiştir. Bob ise kendi tarafında ilave 50.000 Sats'e sahip olur. Suzie (ara düğüm) için bu işlem nötrdür: başlangıçta Alice ile olan kanalında 30.000 Sats ve Bob ile olan kanalında 250.000 Sats olmak üzere toplam 280.000 Sats vardı. Operasyondan sonra, Alice ile olan kanalında 80.000 Sats ve Bob ile olan kanalında 200.000 Sats bulundurmaktadır, bu da başlangıçtaki toplamla aynıdır.


Dolayısıyla bu transfer, transfer yönündeki **mevcut likidite** ile sınırlıdır.


### Güzergah ve Likidite Limitlerinin Hesaplanması


Ile başka bir ağın teorik bir örneğini ele alalım:



- 130.000 satoshis **Alice'nin** tarafında (turuncu renkte) **Suzie** (gri renkte) ile kanalında.
- suzie'nin** tarafında 90.000 satoshis** ve **Carol'un** tarafında **200.000 satoshis** (pembe renkte).
- **150.000 satoshis** **Carol** tarafında ve **100.000 satoshis** **Bob** tarafında.


![LNP201](assets/en/039.webp)


Bu konfigürasyonda Alice'nin Bob'e gönderebileceği maksimum miktar **90.000 satoshidir**, çünkü **Suzie'den Carol'a** kanalda mevcut olan en küçük likidite ile sınırlıdır. Ters yönde (Bob'ten Alice'ye), **Suzie'nin** **Alice** ile olan kanaldaki tarafı hiç satoshi içermediğinden hiçbir ödeme mümkün değildir. Bu nedenle, bu yönde bir transfer için kullanılabilecek **hiçbir rota** yoktur.

Alice, kanallar aracılığıyla Bob'e **40.000 satoshis** gönderir:



- Alice, Suzie ile olan kanalına 40.000 satoshis transfer eder.
- Suzie, ortak kanallarından Carol'a 40.000 satoshis transfer eder.
- Carol sonunda 40,000 satoshiyi Bob'ye aktarır.


![LNP201](assets/en/040.webp)


Her kanalda gönderilen **satoshiler** kanalda kalır, bu nedenle Carol tarafından Bob'a gönderilen satoshiler Alice tarafından Suzie'ye gönderilenlerle aynı değildir. Aktarım yalnızca her bir kanalın içindeki likiditenin ayarlanmasıyla yapılır. Dahası, kanalların toplam kapasitesi değişmeden kalır.


![LNP201](assets/en/041.webp)


Önceki örnekte olduğu gibi, işlemden sonra kaynak düğüm (Alice) 40.000 satoshis daha az paraya sahip olur. Ara düğümler (Suzie ve Carol) aynı toplam miktarı tutarak işlemi onlar için nötr hale getirir. Son olarak, hedef düğüm (Bob) ilave 40.000 satoshi alır.


Ara düğümlerin rolü bu nedenle Lightning Network'nin işleyişinde çok önemlidir. Ödemeler için birden fazla yol sunarak transferleri kolaylaştırırlar. Bu düğümleri likiditelerini sağlamaya ve ödemelerin yönlendirilmesine katılmaya teşvik etmek için onlara **yönlendirme ücretleri** ödenir.


### Yönlendirme Ücretleri


Ara düğümler, ödemelerin kendi kanallarından geçmesine izin vermek için ücret uygular. Bu ücretler her kanal için **her düğüm tarafından belirlenir**. Ücretler 2 Elements'ten oluşur:



- "**Baz ücret**": kanal başına sabit bir miktar, genellikle varsayılan olarak **1 sat**, ancak özelleştirilebilir.
- "**Değişken ücret**": aktarılan miktarın **milyon başına parça (ppm)** olarak hesaplanan bir yüzdesi. Varsayılan olarak **1 ppm**'dir (aktarılan milyon satoshi başına 1 sat), ancak ayarlanabilir.


Ücretler transferin yönüne göre de farklılık gösterir. Örneğin, Alice'ten Suzie'ye bir transfer için Alice'ün ücretleri uygulanır. Tersine, Suzie'den Alice'e transferde Suzie'nin ücretleri kullanılır.


Örneğin, Alice ve Suzie arasındaki bir kanal için şunları yapabiliriz:



- **Alice**: 1 sat baz ücret ve değişken ücretler için 1 ppm.
- **Suzie**: 0,5 sat baz ücret ve değişken ücretler için 10 ppm.


![LNP201](assets/en/042.webp)


Ücretlerin nasıl işlediğini daha iyi anlamak için, daha önce olduğu gibi aynı Lightning Network'yi inceleyelim, ancak şimdi aşağıdaki yönlendirme ücretleri ile:



- Kanal **Alice - Suzie**: 1 Satoshi taban ücreti ve Alice için 1 ppm.
- Kanal **Suzie - Carol**: Suzie için 0 Satoshi ve 200 ppm baz ücret.
- Carol - **Bob** Kanal: Suzie 2 için 1 Satoshi ve 1 ppm baz ücret.

![LNP201](assets/en/043.webp)


Bob'e aynı **40.000 satoshis** ödemesi için Alice'ün biraz daha fazla göndermesi gerekecektir, çünkü her aracı düğüm kendi ücretini düşecektir:



- **Carol**, Bob ile kanalda 1,04 satoshi kesinti yapar:

$$ f_{\text{Carol-Bob}} = \text{baz ücret} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f_{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$



- **Suzie**, Carol ile kanalda 8 satoshis ücret keser:

$$ f_{\text{Suzie-Carol}} = \text{temel ücret} + \left(\frac{\text{ppm} \times \text{amount}}{10^6}\right) $$

$$ f_{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$


Bu ödemenin bu yoldaki toplam ücreti bu nedenle **9,04 satoshidir**. Dolayısıyla, Alice'nin Bob'den tam olarak **40.000 satoshi** alabilmesi için **40.009,04 satoshi** göndermesi gerekir.


![LNP201](assets/en/044.webp)


Bu nedenle likidite güncellenmiştir:


![LNP201](assets/en/045.webp)


### Soğan Yönlendirme


Bir ödemeyi göndericiden alıcıya yönlendirmek için Lightning Network "**soğan yönlendirme**" adı verilen bir yöntem kullanır. Her yönlendiricinin hedeflerine göre verilerin yönüne karar verdiği klasik verilerin yönlendirilmesinden farklı olarak, soğan yönlendirme farklı şekilde çalışır:



- **Gönderen düğüm tüm rotayı hesaplar**: Örneğin Alice, ödemesinin Bob'e ulaşmadan önce Suzie ve Carol'dan geçmesi gerektiğini belirler.
- **Her aracı düğüm sadece yakın komşusunu bilir**: Suzie yalnızca Alice'ten para aldığını ve bu parayı Carol'a aktarması gerektiğini bilmektedir. Ancak Suzie, Alice'in kaynak düğüm mü yoksa aracı düğüm mü olduğunu bilmez ve ayrıca Carol'ın alıcı düğüm mü yoksa sadece başka bir aracı düğüm mü olduğunu da bilmez. Bu ilke Carol ve yol üzerindeki diğer tüm düğümler için de geçerlidir. Böylece soğan yönlendirme, göndericinin ve nihai alıcının kimliğini maskeleyerek işlemlerin gizliliğini korur.

Soğan yönlendirmede verici düğümün alıcıya giden tam bir rota hesaplayabilmesini sağlamak için, topolojisini bilmek ve olası rotaları belirlemek için bir **ağ grafiği** tutması gerekir.

**Bu bölümden ne anlamalısınız?**



- Lightning'de ödemeler, aracı kanallar aracılığıyla dolaylı olarak bağlanan düğümler arasında yönlendirilebilir. Bu aracı düğümlerin her biri likidite aktarımını kolaylaştırır.
- Aracı düğümler, hizmetleri karşılığında sabit ve değişken ücretlerden oluşan bir komisyon alırlar.
- Soğan yönlendirme, verici düğümün kaynağı veya nihai hedefi bilen aracı düğümler olmadan tüm rotayı hesaplamasına olanak tanır.


Bu bölümde, Lightning Network üzerinde ödeme yönlendirmesini inceledik. Ancak bir soru ortaya çıkmaktadır: aracı düğümlerin gelen bir ödemeyi, işlemi engellemek amacıyla bir sonraki hedefe iletmeden kabul etmesini engelleyen nedir? Bir sonraki bölümde inceleyeceğimiz HTLC'lerin rolü tam olarak budur.


## HTLC - Karma Zaman Kilitli Contract


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


Bu bölümde, Lightning'in **[HTLC](https://planb.academy/resources/glossary/htlc)** (_Hashed Time-Locked Contracts_) sayesinde ödemelerin aracı düğümlere güvenmeye gerek kalmadan geçmesine nasıl izin verdiğini keşfedeceğiz. Bu akıllı sözleşmeler, her bir aracı düğümün ödemeyi yalnızca nihai alıcıya iletmesi durumunda kendi kanalından fon almasını sağlar, aksi takdirde ödeme doğrulanmaz.


Bu nedenle ödeme yönlendirmesi için ortaya çıkan sorun, aracı düğümlere ve aracı düğümlerin kendi aralarındaki gerekli güvendir. Bunu göstermek için 3 düğümlü ve 2 kanallı basitleştirilmiş Lightning Network örneğimizi tekrar ele alalım:



- Alice'in Suzie ile bir kanalı var.
- Suzie'nin Bob ile bir kanalı var.


Alice 40,000 Sats'ü Bob'e göndermek ister ancak onunla doğrudan bir kanalı yoktur ve bir kanal açmak istemez. Bir rota arar ve Suzie'nin düğümü üzerinden gitmeye karar verir.


![LNP201](assets/en/046.webp)


Alice, Suzie'nin bu meblağı Bob'ye aktaracağını umarak safça Suzie'ye 40.000 satoshi gönderirse, Suzie bu parayı kendine saklayabilir ve Bob'ye hiçbir şey iletmeyebilir.


![LNP201](assets/en/047.webp)

Bu durumdan kaçınmak için Lightning'de, aracı düğüme ödemeyi koşullu hale getiren HTLC'ler (Kareli Zaman Kilitli Sözleşmeler) kullanıyoruz, yani Suzie'nin Alice'in fonlarına erişmek ve bunları Bob'a aktarmak için belirli koşulları karşılaması gerekiyor.


### HTLC'ler Nasıl Çalışır?


Bir HTLC, iki ilkeye dayanan özel bir Contract'tir:



- **Erişim koşulu**: Alıcı, kendisine yapılacak ödemenin kilidini açmak için bir sırrı açıklamalıdır.
- **Sona erme**: Ödeme belirli bir süre içinde tam olarak tamamlanmazsa iptal edilir ve fonlar gönderene geri döner.


Bu sürecin Alice, Suzie ve Bob ile örneğimizde nasıl işlediği aşağıda açıklanmıştır:


![LNP201](assets/en/048.webp)


**Sırrın oluşturulması**: Bob _s_ (ön görüntü) olarak belirtilen rastgele bir sır üretir ve _h_ olarak belirtilen Hash fonksiyonu ile _r_ olarak belirtilen Hash'ünü hesaplar. Elimizde:


$$
r = h(s)
$$


Bir Hash fonksiyonu kullanmak _s_'yi sadece _h(s)_ ile bulmayı imkansız hale getirir, ancak _s_ sağlanmışsa, _h(s)_'ye karşılık geldiğini doğrulamak kolaydır.


![LNP201](assets/en/049.webp)


**Ödeme talebinin gönderilmesi**: Bob, Alice'e ödeme talebinde bulunan bir **Invoice** gönderir. Bu Invoice özellikle Hash _r_ içerir.


![LNP201](assets/en/050.webp)


**Şartlı ödemeyi gönderiyor**: Alice Suzie'ye 40,000 satoshilik bir HTLC gönderir. Suzie'nin bu parayı alabilmesinin koşulu, Alice'e aşağıdaki denklemi sağlayan gizli bir _s'_ vermesidir:


$$
h(s') = r
$$


![LNP201](assets/en/051.webp)


**HTLC'ün son alıcıya aktarılması**: Suzie, Alice'ten 40.000 satoshiyi elde etmek için, 40.000 satoshilik benzer bir HTLC'ü aynı koşula sahip olan Bob'e aktarmalıdır, yani Suzie'ye denklemi karşılayan gizli bir _s'_ sağlamalıdır:


$$
h(s') = r
$$


![LNP201](assets/en/052.webp)


**Gizli _s_** tarafından doğrulama: Bob, HTLC'de vaat edilen 40.000 satoshiyi almak için Suzie'ye _s_ sağlar. Suzie bu sır ile Alice'nın HTLC'sini açabilir ve Alice'dan 40.000 satoshiyi alabilir. Ödeme daha sonra doğru bir şekilde Bob'e yönlendirilir.


![LNP201](assets/en/053.webp)

Bu işlem Suzie'nin Alice'un fonlarını Bob'e transferi tamamlamadan tutmasını engeller, çünkü gizli _s_'yi elde etmek ve böylece Alice'un HTLC'ının kilidini açmak için ödemeyi Bob'e göndermesi gerekir. Rota birden fazla aracı düğüm içerse bile işlem aynı kalır: Suzie'nin adımlarını her bir aracı düğüm için tekrarlamak yeterlidir. Her düğüm HTLC'lerin koşulları tarafından korunur, çünkü alıcı tarafından son HTLC'ın kilidinin açılması otomatik olarak diğer tüm HTLC'lerin kilidinin açılmasını tetikler.


### Sorun durumunda HTLC'lerin son kullanma tarihi ve yönetimi


Ödeme işlemi sırasında aracı düğümlerden biri veya alıcı düğüm yanıt vermeyi durdurursa, özellikle internet veya elektrik kesintisi durumunda, HTLC'lerin kilidini açmak için gereken sır iletilmediği için ödeme tamamlanamaz. Örneğimizi Alice, Suzie ve Bob ile ele alırsak, örneğin Bob _s_ sırrını Suzie'ye iletmezse bu sorun ortaya çıkar. Bu durumda, yolun yukarısındaki tüm HTLC'ler ve güvence altına aldıkları fonlar da engellenir.


![LNP201](assets/en/054.webp)


Bunu önlemek için Lightning'deki HTLC'ler, belirli bir süre sonra tamamlanmadığı takdirde HTLC'ün kaldırılmasına olanak tanıyan bir sona erme süresine sahiptir. Süre sonu, önce alıcıya en yakın HTLC ile başladığından ve ardından kademeli olarak işlemi düzenleyene doğru ilerlediğinden belirli bir sırayı takip eder. Örneğimizde, Bob gizli _s_'yi Suzie'ye asla vermezse, bu ilk olarak Suzie'nin HTLC'ünün Bob'e doğru süresinin dolmasına neden olacaktır.


![LNP201](assets/en/055.webp)


Sonra Alice'dan Suzie'ye HTLC.


![LNP201](assets/en/056.webp)


Sona erme sırası tersine çevrilirse, Alice, Suzie olası bir hileden kendini koruyamadan önce ödemesini geri alabilir. Gerçekten de, Alice kendi HTLC'unu çoktan kaldırmışken Bob kendi HTLC'unu talep etmek için geri gelirse Suzie dezavantajlı duruma düşecektir. HTLC'un sona ermesinin bu kademeli sırası, böylece hiçbir aracı düğümün haksız kayıplara uğramamasını sağlar.


### Commitment işlemlerinde HTLC'lerin temsili


Commitment işlemleri HTLC'leri, Lightning'e yükledikleri koşulların bir HTLC'in ömrü boyunca zorunlu bir kanal kapanması durumunda Bitcoin'e aktarılabileceği şekilde temsil eder. Bir hatırlatma olarak, Commitment işlemleri iki kullanıcı arasındaki kanalın mevcut durumunu temsil eder ve sorun olması durumunda tek taraflı zorunlu kapatmaya izin verir. Kanalın her yeni durumunda, her bir taraf için bir tane olmak üzere 2 Commitment işlemi oluşturulur. Örneğimizi Alice, Suzie ve Bob ile tekrar ele alalım, ancak HTLC oluşturulduğunda Alice ve Suzie arasında kanal düzeyinde neler olduğuna daha yakından bakalım.

![LNP201](assets/en/057.webp)


Alice ve Bob arasındaki 40.000 Sats ödemesinin başlamasından önce, Alice'in Suzie ile olan kanalında 100.000 Sats bulunurken, Suzie'nin elinde 30.000 bulunmaktadır. Commitment işlemleri aşağıdaki gibidir:


![LNP201](assets/en/058.webp)


Alice, Bob'nın Invoice'sini henüz almıştır ve bu Hash, sırrın Hash'i olan _r_'yi içermektedir. Böylece Suzie ile 40.000 satoshilik bir HTLC oluşturabilir. Bu HTLC en son Commitment işlemlerinde, fonlar giden fonlar olduğu için Alice tarafında "**_HTLC Out_**" ve fonlar gelen fonlar olduğu için Suzie tarafında "**_HTLC In_**" olarak adlandırılan bir çıktı olarak temsil edilir.


![LNP201](assets/en/059.webp)


HTLC ile ilişkili bu çıkışlar tamamen aynı koşulları paylaşır, yani:



- Suzie gizli _s_'yi sağlayabilirse, bu çıktının kilidini hemen açabilir ve kontrol ettiği bir Address'e aktarabilir.
- Suzie _s_ sırrına sahip değilse, bu çıktının kilidini açamaz ve Alice bir zaman kilidinden sonra kilidi açarak kontrol ettiği bir Address'a gönderebilir. Böylece zaman kilidi Suzie'ye _s_'yi elde ederse tepki vermesi için bir süre tanır.


Bu koşullar yalnızca HTLC Lightning'de hala aktifken, yani Alice ve Bob arasındaki ödeme henüz sonuçlanmamış ve HTLC'lerin süresi henüz dolmamışken kanal kapatılırsa (yani bir Commitment Transaction, On-Chain'yi yayınlarsa) geçerlidir. Bu koşullar sayesinde Suzie, _s_ sağlayarak kendisine borçlu olunan HTLC'ün 40.000 satoshisini geri alabilir. Aksi takdirde, Alice zaman kilidinin sona ermesinden sonra fonları geri alır, çünkü Suzie _s_'yi bilmiyorsa, 40.000 satoshiyi Bob'e aktarmamış demektir ve bu nedenle Alice'ün fonları ona borçlu değildir.


Ayrıca, birkaç HTLC beklemedeyken kanal kapatılırsa, devam eden HTLC'ler kadar ek çıkış olacaktır.

Kanal kapatılmazsa, Lightning ödemesinin sona ermesinden veya başarılı olmasından sonra, kanalın yeni, artık kararlı olan durumunu, yani bekleyen HTLC'ler olmadan yansıtmak için yeni Commitment işlemleri oluşturulur. Bu nedenle HTLC'lerle ilgili çıktılar Commitment işlemlerinden kaldırılabilir.

![LNP201](assets/en/060.webp)


Son olarak, bir HTLC aktifken bir kooperatif kanalının kapanması durumunda, Alice ve Suzie yeni ödemeleri kabul etmeyi durdurur ve devam eden HTLC'lerin çözülmesini veya sona ermesini bekler. Bu, HTLC'lerle ilgili çıktılar olmadan daha hafif bir kapanış işlemi yayınlamalarına olanak tanır, böylece ücretleri azaltır ve olası bir zaman kilidi için beklemekten kaçınır.


**Bu bölümden ne anlamalısınız?**


HTLC'ler, Lightning ödemelerinin güvenmek zorunda kalmadan birden fazla düğüm üzerinden yönlendirilmesini sağlar. İşte hatırlanması gereken kilit noktalar:



- HTLC'ler ödemelerin güvenliğini bir sır (ön imaj) ve bir sona erme süresi ile sağlar.
- HTLC'lerin çözümlenmesi veya sona ermesi belirli bir sırayı takip eder: daha sonra her bir düğümü korumak için hedeften kaynağa doğru.
- Bir HTLC çözümlenmediği veya süresi dolmadığı sürece, en son Commitment işlemlerinde bir çıktı olarak muhafaza edilir.


Bir sonraki bölümde, Lightning işlemi düzenleyen bir düğümün, ödemesinin alıcı düğüme ulaşması için rotaları nasıl bulduğunu ve seçtiğini keşfedeceğiz.


## Yolunuzu Bulmak


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


Önceki bölümlerde, ödemeleri yönlendirmek için diğer düğümlerin kanallarını nasıl kullanacağımızı ve bir kanal aracılığıyla doğrudan bağlı olmadan bir düğüme nasıl ulaşacağımızı gördük. Ayrıca aracı düğümlere güvenmeden transferin güvenliğinin nasıl sağlanacağını da tartıştık. Bu bölümde, bir hedef düğüme ulaşmak için mümkün olan en iyi rotayı bulmaya odaklanacağız.


### Lightning'de Yönlendirme Sorunu


Gördüğümüz gibi, Lightning'de alıcıya giden tüm rotayı hesaplaması gereken ödeme gönderen düğümdür, çünkü bir soğan yönlendirme sistemi kullanıyoruz. Aracı düğümler ne başlangıç noktasını ne de son varış noktasını bilir. Sadece ödemenin nereden geldiğini ve hangi düğüme aktarılması gerektiğini bilirler. Bu, gönderen düğümün, mevcut Yıldırım düğümleri ve her biri arasındaki kanallarla birlikte, açılışları, kapanışları ve durum güncellemelerini dikkate alarak ağın dinamik bir yerel topolojisini sürdürmesi gerektiği anlamına gelir.


![LNP201](assets/en/061.webp)

Lightning Network'in bu topolojisinde bile, herhangi bir anda kanallardaki likiditenin tam dağılımı olan gönderen düğüm için erişilemez kalan yönlendirme için önemli bilgiler vardır. Aslında, her kanal yalnızca **toplam kapasitesini** gösterir, ancak fonların iç dağılımı yalnızca iki katılımcı düğüm tarafından bilinir. Bu durum, ödemenin başarısı özellikle miktarının seçilen rotadaki en düşük likiditeden az olup olmamasına bağlı olduğundan, verimli yönlendirme için zorluklar yaratmaktadır. Ancak likiditelerin tamamı gönderen düğüm tarafından görülemez.

![LNP201](assets/en/062.webp)


### Ağ Haritası Güncellemesi


Ağ haritalarını güncel tutmak için düğümler, "**_gossip_**" adı verilen bir algoritma aracılığıyla düzenli olarak Exchange mesajları gönderir. Bu, ağdaki tüm düğümlere salgın bir şekilde bilgi yaymak için kullanılan ve birkaç iletişim döngüsünde kanalların Exchange ve Global State senkronizasyonunu sağlayan dağıtılmış bir algoritmadır. Her düğüm bilgiyi rastgele seçilen veya seçilmeyen bir veya daha fazla komşuya yayar, bunlar da bilgiyi diğer komşulara yayar ve böylece küresel olarak senkronize bir durum elde edilene kadar devam eder.


Lightning düğümleri arasında değiş tokuş edilen 2 ana mesaj aşağıdaki gibidir:



- "**Kanal Duyuruları**": yeni bir kanalın açıldığını bildiren mesajlar.
- "**Kanal Güncellemeleri**": bir kanalın durumu, özellikle ücretlerin gelişimi (ancak likidite dağılımı değil) hakkında güncelleme mesajları.


Lightning düğümleri ayrıca kanal kapatma işlemlerini tespit etmek için Bitcoin Blockchain'ü de izler. Kapatılan kanal, artık ödemelerimizi yönlendirmek için kullanılamayacağından haritadan kaldırılır.


### Ödeme Yönlendirme


7 düğümlü küçük bir Lightning Network örneğini ele alalım: Alice, Bob, 1, 2, 3, 4 ve 5. Alice'nin Bob'e bir ödeme göndermek istediğini ancak aracı düğümlerden geçmesi gerektiğini düşünün.


![LNP201](assets/en/063.webp)


İşte bu kanallardaki fonların gerçek dağılımı:



- Alice ve **1** arasındaki kanal: gW-439 tarafında 250.000 Sats, 1 tarafında 80.000 (toplam 330.000 Sats kapasite).
- **1 ve 2 arasındaki kanal**: 1. tarafta 300.000 Sats, 2. tarafta 200.000 (toplam 500.000 Sats kapasite).
- **2 ve 3 arasındaki kanal**: 2. tarafta 50.000 Sats, 3. tarafta 60.000 (toplam 110.000 Sats kapasite).
- 2 ve 5 arasındaki kanal: 2. tarafta 90.000 Sats, 5. tarafta 160.000 (toplam 250.000 Sats kapasite).
- 2 ve 4 arasındaki kanal: 2. tarafta 180.000 Sats, 4. tarafta 110.000 (toplam 290.000 Sats kapasite).
- 4 ve 5 arasındaki kanal: 4. tarafta 200.000 Sats, 5. tarafta 10.000 (toplam 210.000 Sats kapasite).
- 3 ve **Bob** arasındaki kanal: 3. tarafta 50.000 Sats, Bob tarafında 250.000 (toplam 300.000 Sats kapasite).
- 5 ve **Bob** arasındaki kanal: 5. tarafta 260.000 Sats, Bob tarafında 100.000 (toplam 360.000 Sats kapasite).


![LNP201](assets/en/064.webp)


Alice'den Bob'ye 100.000 Sats'lik bir ödeme yapmak için yönlendirme seçenekleri her bir kanaldaki mevcut likidite ile sınırlıdır. Bilinen likidite dağılımlarına dayalı olarak Alice için en uygun rota `Alice → 1 → 2 → 4 → 5 → Bob` dizisi olabilir:


![LNP201](assets/en/065.webp)


Ancak Alice her bir kanaldaki fon dağılımını tam olarak bilmediğinden, aşağıdaki kriterleri göz önünde bulundurarak en uygun rotayı olasılıksal olarak tahmin etmelidir:



- **Başarı olasılığı**: daha yüksek toplam kapasiteye sahip bir kanalın yeterli likidite içermesi daha olasıdır. Örneğin, düğüm 2 ve düğüm 3 arasındaki kanalın toplam kapasitesi 110.000 Sats'tür, bu nedenle düğüm 2 tarafında 100.000 Sats veya daha fazlasını bulmak pek olası değildir, ancak yine de mümkündür.
- **İşlem ücretleri**: En iyi rotayı seçerken, gönderen düğüm her bir ara düğüm tarafından uygulanan ücretleri de dikkate alır ve toplam yönlendirme maliyetini en aza indirmeye çalışır.
- **HTLC'lerin sona ermesi**: bloke ödemelerden kaçınmak için HTLC'lerin sona erme süresi de dikkate alınması gereken bir parametredir.
- **Ara düğüm sayısı**: son olarak, daha genel olarak, gönderen düğüm, başarısızlık riskini azaltmak ve Yıldırım işlem ücretlerini sınırlamak için mümkün olan en az düğümle bir rota bulmaya çalışacaktır.


Gönderen düğüm bu kriterleri analiz ederek en olası rotaları test edebilir ve bunları optimize etmeye çalışabilir. Örneğimizde, Alice en iyi rotaları aşağıdaki gibi sıralayabilir:



- `Alice → 1 → 2 → 5 → Bob`, çünkü bu en yüksek kapasiteye sahip en kısa rotadır.
- `Alice → 1 → 2 → 4 → 5 → Bob`, çünkü bu rota ilkinden daha uzun olmasına rağmen iyi kapasiteler sunmaktadır.
- `Alice → 1 → 2 → 3 → Bob`, çünkü bu rota çok sınırlı kapasiteye sahip, ancak potansiyel olarak kullanılabilir kalan `2 → 3` kanalını içerir.


### Ödeme Yürütme


Alice ilk rotasını test etmeye karar verir (`Alice → 1 → 2 → 5 → Bob`). Bu nedenle düğüm 1'e 100.000 Sats'lük bir HTLC gönderir. Bu düğüm, düğüm 2 ile yeterli likiditeye sahip olduğunu kontrol eder ve iletime devam eder. Düğüm 2 daha sonra düğüm 1'den HTLC'ü alır, ancak düğüm 5 ile olan kanalında 100.000 Sats'lük bir ödemeyi yönlendirmek için yeterli likiditeye sahip olmadığını fark eder. Daha sonra düğüm 1'e bir hata mesajı gönderir ve o da mesajı Alice'ye iletir. Bu rota başarısız oldu.


![LNP201](assets/en/066.webp)


Alice daha sonra ödemesini ikinci rotasını kullanarak yönlendirmeye çalışır (`Alice → 1 → 2 → 4 → 5 → Bob`). Düğüm 1'e 100.000 HTLC'lik bir Sats gönderir, o da bunu düğüm 2'ye, ardından düğüm 4'e, düğüm 5'e ve son olarak Bob'a iletir. Bu sefer likidite yeterlidir ve rota işlevseldir. Her düğüm, Bob tarafından sağlanan ön görüntüyü (gizli _s_) kullanarak HTLC'sinin kilidini kademeli olarak açar ve bu da Alice'nın Bob'a yaptığı ödemenin başarıyla sonuçlanmasını sağlar.


![LNP201](assets/en/067.webp)


Rota arayışı şu şekilde gerçekleştirilir: gönderen düğüm mümkün olan en iyi rotaları belirleyerek başlar, ardından işlevsel bir rota bulunana kadar art arda ödeme yapmayı dener.


Bob'nin yönlendirmeyi kolaylaştırmak için Alice'e **Invoice**'deki bilgileri sağlayabileceğini belirtmek gerekir. Örneğin, yeterli likiditeye sahip yakındaki kanalları gösterebilir veya özel kanalların varlığını ortaya çıkarabilir. Bu göstergeler, Alice'in başarı şansı düşük olan rotalardan kaçınmasına ve ilk olarak Bob tarafından önerilen yolları denemesine olanak tanır.


**Bu bölümden ne anlamalısınız?**



- Düğümler, duyurular yoluyla ve Bitcoin Blockchain üzerindeki kanal kapanışlarını izleyerek ağ topolojisinin bir haritasını tutar.
- Bir ödeme için en uygun rota arayışı olasılıksaldır ve birçok kritere bağlıdır.
- Bob, Alice'nın yönlendirmesine rehberlik etmek ve onu olası olmayan rotaları test etmekten kurtarmak için **Invoice**'te göstergeler sağlayabilir.


Bir sonraki bölümde, Lightning Network'de kullanılan diğer bazı araçlara ek olarak özellikle faturaların işleyişini inceleyeceğiz.


# Lightning Network'un Araçları


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Invoice, LNURL ve Keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


Bu bölümde, Lightning **faturalarının** işleyişine, yani alıcı düğüm tarafından gönderici düğüme gönderilen ödeme taleplerine daha yakından bakacağız. Amaç, Lightning'de nasıl ödeme yapılacağını ve ödeme alınacağını anlamaktır. Ayrıca klasik faturalara 2 alternatifi de tartışacağız: LNURL ve Keysend.


![LNP201](assets/en/068.webp)


### Yıldırım Faturaların Yapısı


HTLC'lerle ilgili bölümde açıklandığı üzere, her ödeme alıcı tarafından bir **Invoice** oluşturulmasıyla başlar. Bu Invoice daha sonra ödemeyi başlatmak için ödeyene (bir QR kodu aracılığıyla veya kopyalayıp yapıştırarak) iletilir. Bir Invoice iki ana bölümden oluşur:



- **İnsan Tarafından Okunabilir Bölüm**: Bu bölüm, kullanıcı deneyimini geliştirmek için açıkça görülebilir meta veriler içerir.
- **Ödeme Yükü**: bu bölüm, makinelerin ödemeyi işlemesi için tasarlanan bilgileri içerir.


Bir Invoice'in tipik yapısı "Yıldırım" için `LN` tanımlayıcısı ile başlar, ardından Bitcoin için `bc` gelir, ardından Invoice'in miktarı gelir. Bir ayırıcı `1`, insan tarafından okunabilir kısmı veri (yük) kısmından ayırır.


Örnek olarak aşağıdaki Invoice'yi ele alalım:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Bunu zaten 2 kısma ayırabiliriz. Birincisi, İnsanların Okuyabileceği Kısım:


```invoice
lnbc100u
```


Sonra yük için tasarlanan parça:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


İki bölüm bir `1` ile ayrılmıştır. Bu ayırıcı, Invoice'in tamamının çift tıklanarak kolayca kopyalanıp yapıştırılmasına olanak sağlamak için özel bir karakter yerine seçilmiştir.


İlk bölümde bunu görebiliyoruz:



- `LN` bunun bir Lightning işlemi olduğunu gösterir.
- bc` Lightning Network'ın Bitcoin Blockchain üzerinde olduğunu (ve Testnet veya Litecoin üzerinde olmadığını) gösterir.
- 100u`, **microbitcoins** (`u` "mikro" anlamına gelir) cinsinden ifade edilen Invoice miktarını gösterir ve burada 10.000 Sats'e eşittir.


Ödeme tutarını belirlemek için, Bitcoin'nın alt birimleriyle ifade edilir. İşte kullanılan birimler:



- **Milibitcoin (`m` olarak gösterilir):** Bir Bitcoin'nin binde birini temsil eder.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$



- **Microbitcoin (`u` olarak gösterilir):** Bazen "bit" olarak da adlandırılır, bir Bitcoin'in milyonda birini temsil eder.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$



- **Nanobitcoin (`n` olarak gösterilir):** Bir Bitcoin'un milyarda birini temsil eder.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$



- **Picobitcoin (`p` olarak gösterilir):** Bir Bitcoin'ün trilyonda birini temsil eder.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$


### Bir Invoice'in Yükü


Bir Invoice'nin yükü, ödemenin işlenmesi için gerekli birkaç bilgi parçasını içerir:



- **Timestamp:** Invoice'ün yaratıldığı an, Unix Timestamp (1 Ocak 1970'ten bu yana geçen saniye sayısı) olarak ifade edilir.
- **Sırrın Hashing'i**: HTLC'lerle ilgili bölümde gördüğümüz gibi, alıcı düğüm gönderen düğüme ön görüntünün Hash'ini sağlamalıdır. Bu, HTLC'lerde işlemi güvence altına almak için kullanılır. Biz bunu "_r_" olarak adlandırdık.
- **Ödeme Sırrı**: Alıcı tarafından başka bir sır oluşturulur, ancak bu sefer gönderen düğüme iletilir. Soğan yönlendirmede ara düğümlerin bir sonraki düğümün nihai alıcı olup olmadığını tahmin etmesini önlemek için kullanılır. Böylece rotadaki son ara düğüme göre alıcı için bir çeşit gizlilik sağlanmış olur.
- **Alıcının Açık Anahtarı**: Ödeyene, ödeme yapılacak kişinin tanımlayıcısını gösterir.
- **Sona Erme Süresi**: Invoice'nın ödeneceği maksimum süre (varsayılan olarak 1 saat).
- **Yönlendirme İpuçları**: Gönderenin ödeme rotasını optimize etmesine yardımcı olmak için alıcı tarafından sağlanan ek bilgiler.
- **İmza**: Tüm bilgileri doğrulayarak Invoice'nin bütünlüğünü garanti eder.


Faturalar daha sonra Bitcoin SegWit adresleriyle aynı formatta (`bc1` ile başlayan format) **bech32** olarak kodlanır.


### LNURL Para Çekme


Mağaza satın alımı gibi geleneksel bir işlemde, ödenecek toplam tutar için Invoice oluşturulur. Invoice sunulduğunda (bir QR kodu veya karakter dizisi şeklinde), müşteri bunu tarayabilir ve işlemi tamamlayabilir. Ödeme daha sonra önceki bölümde incelediğimiz geleneksel süreci takip eder. Ancak bu süreç, alıcının Invoice aracılığıyla göndericiye bilgi göndermesini gerektirdiği için bazen kullanıcı deneyimi açısından çok zahmetli olabilir.


Çevrimiçi bir hizmetten bitcoin çekmek gibi belirli durumlar için geleneksel süreç çok zahmetlidir. Bu gibi durumlarda, **LNURL** para çekme çözümü, alıcının Wallet'sinin otomatik olarak Invoice oluşturmak için taradığı bir QR kodu görüntüleyerek bu işlemi basitleştirir. Hizmet daha sonra Invoice'i öder ve kullanıcı sadece anında bir para çekme işlemi görür.


![LNP201](assets/en/069.webp)


LNURL, Lightning düğümleri ve istemcilerin yanı sıra üçüncü taraf uygulamalar arasındaki etkileşimleri basitleştirmek için tasarlanmış bir dizi işlevi belirten bir iletişim protokolüdür. Az önce gördüğümüz gibi LNURL geri çekilmesi, diğer işlevler arasında sadece bir örnektir.

Bu protokol HTTP'ye dayanır ve ödeme talebi, para çekme talebi veya kullanıcı deneyimini geliştiren diğer işlevler gibi çeşitli işlemler için bağlantıların oluşturulmasına izin verir. Her LNURL, tarandığında Lightning Wallet üzerinde bir dizi otomatik eylemi tetikleyen lnurl önekine sahip bech32 kodlu bir URL'dir.

Örneğin, LNURL-Withdraw (LUD-03) özelliği, manuel olarak generate ve Invoice'ya ihtiyaç duymadan bir QR kodunu tarayarak bir hizmetten para çekmeye olanak tanır. Benzer şekilde, LNURL-auth (LUD-04) çevrimiçi hizmetlere parola yerine Lightning Wallet üzerindeki özel anahtarı kullanarak giriş yapmayı sağlar.


### Invoice olmadan Yıldırım Ödemesi Gönderme: Keysend


Bir diğer ilginç durum ise "**Keysend**" olarak bilinen, önceden bir Invoice almadan fon transferidir. Bu protokol, şifrelenmiş ödeme verilerine yalnızca alıcı tarafından erişilebilen bir ön görüntü ekleyerek para göndermeye izin verir. Bu ön görüntü, alıcının HTLC'nin kilidini açmasını ve böylece önceden bir Invoice oluşturmadan fonları almasını sağlar.


Basitleştirmek gerekirse, bu protokolde HTLC'lerde kullanılan sırrı alıcı yerine gönderen üretir. Pratikte bu, göndericinin alıcı ile önceden etkileşime girmek zorunda kalmadan ödeme yapmasına olanak tanır.


![LNP201](assets/en/070.webp)


**Bu bölümden ne anlamalısınız?**



- Bir **Lightning Invoice**, insan tarafından okunabilir bir kısım ve bir makine verisi kısmından oluşan bir ödeme talebidir.
- Invoice, kopyalamayı kolaylaştırmak için bir `1` ayırıcı ve ödemeyi işlemek için gerekli tüm bilgileri içeren bir veri bölümü ile **bech32** olarak kodlanır.
- Lightning'de, özellikle para çekme işlemlerini kolaylaştırmak için **LNURL-Withdraw** ve Invoice olmadan doğrudan transferler için **Keysend** olmak üzere başka ödeme süreçleri de mevcuttur.


Bir sonraki bölümde, bir düğüm operatörünün kanallarındaki likiditeyi nasıl yönetebileceğini, asla engellenmeyeceğini ve Lightning Network'de her zaman ödeme gönderip alabileceğini göreceğiz.


## Likiditenizi Yönetmek


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


Bu bölümde, Lightning Network'da likiditeyi etkin bir şekilde yönetmeye yönelik stratejileri inceleyeceğiz. Likidite yönetimi kullanıcı türüne ve bağlama göre değişir. Bu yönetimin nasıl optimize edileceğini daha iyi anlamak için ana ilkelere ve mevcut tekniklere bakacağız.


### Likidite İhtiyaçları


Lightning'de her biri belirli likidite ihtiyaçlarına sahip üç ana kullanıcı profili vardır:



- **Ödeyen**: Bu, ödemeleri yapan kişidir. Diğer kullanıcılara fon aktarabilmek için giden likiditeye ihtiyaçları vardır. Örneğin, bu bir tüketici olabilir.
- **Satıcı (veya Alacaklı)**: Bu, ödemeleri alan kişidir. Düğümlerine yapılan ödemeleri kabul edebilmek için gelen likiditeye ihtiyaçları vardır. Örneğin, bu bir işletme veya çevrimiçi bir mağaza olabilir.
- **Yönlendirici**: Genellikle ödemeleri yönlendirme konusunda uzmanlaşmış, mümkün olduğunca çok ödemeyi yönlendirmek ve ücret kazanmak için her kanaldaki likiditesini optimize etmesi gereken bir aracı düğüm.


Bu profiller tabii ki sabit değildir; bir kullanıcı işlemlere bağlı olarak ödeyen ve alacaklı arasında geçiş yapabilir. Örneğin, Bob maaşını işvereninden Lightning üzerinden alabilir ve bu da onu gelen likiditeye ihtiyaç duyan bir "satıcı" konumuna yerleştirir. Daha sonra, maaşını yiyecek satın almak için kullanmak isterse, bir "ödeyici" haline gelir ve o zaman giden likiditeye sahip olması gerekir.


Daha iyi anlamak için, üç düğümden oluşan basit bir ağ örneğini ele alalım: alıcı (Alice), yönlendirici (Suzie) ve satıcı (Bob).


![LNP201](assets/en/071.webp)


Alıcının satıcıya 30.000 Sats göndermek istediğini ve ödemenin yönlendiricinin düğümünden geçtiğini düşünün. Bu durumda her iki tarafın da ödeme yönünde minimum miktarda likiditeye sahip olması gerekir:



- Ödeyenin yönlendirici ile kanalın kendi tarafında en az 30.000 satoshisi olmalıdır.
- Satıcının bunları alabilmesi için karşı tarafta 30.000 satoshinin bulunduğu bir kanala sahip olması gerekir.
- Yönlendiricinin ödemeyi yönlendirebilmesi için kendi kanalında ödeme yapan tarafta 30.000 satoshi ve satıcı ile olan kanalında da kendi tarafında 30.000 satoshi olması gerekmektedir.


![LNP201](assets/en/072.webp)


### Likidite Yönetimi Stratejileri


Ödeyenler, giden likiditeyi garanti altına almak için kanalların kendi taraflarında yeterli likidite bulundurmayı sağlamalıdır. Bu likiditeye sahip olmak için yeni Lightning kanalları açmak yeterli olduğundan, bu işlemin nispeten basit olduğu kanıtlanmıştır. Gerçekten de, Multisig On-Chain'te kilitlenen ilk fonlar başlangıçta Lightning kanalında tamamen ödeyenin tarafındadır. Böylece kanallar yeterli fonla açıldığı sürece ödeme kapasitesi güvence altına alınmış olur. Giden likidite tükendiğinde, yeni kanallar açmak yeterlidir.

Öte yandan, satıcı için görev daha karmaşıktır. Ödeme alabilmeleri için kanallarının karşı tarafında likiditeye sahip olmaları gerekir. Bu nedenle, bir kanal açmak yeterli değildir: kendileri ödeme almadan önce likiditeyi diğer tarafa taşımak için bu kanalda bir ödeme de yapmaları gerekir. Tüccarlar gibi belirli Lightning kullanıcı profilleri için, düğümlerinin gönderdikleri ile aldıkları arasında açık bir orantısızlık vardır, çünkü bir işletmenin amacı öncelikle generate'ya kar sağlamak için harcadığından daha fazlasını toplamaktır. Neyse ki, belirli gelen likidite ihtiyaçları olan bu kullanıcılar için çeşitli çözümler mevcuttur:



- **Kanalları çekmek**: Satıcı, düğümlerinde beklenen gelen ödemelerin hacmi nedeniyle bir avantajdan yararlanır. Bunu dikkate alarak, işlem ücretlerinden gelir elde etmek isteyen ve ödemelerini yönlendirmek ve ilgili ücretleri tahsil etmek umuduyla kendilerine yönelik kanallar açabilecek yönlendirme düğümlerini çekmeye çalışabilirler.



- **Likidite hareketi**: Satıcı ayrıca bir kanal açabilir ve parayı başka bir şekilde iade edecek olan başka bir düğüme hayali ödemeler yaparak fonların bir kısmını karşı tarafa aktarabilir. Bu işlemin nasıl gerçekleştirileceğini bir sonraki bölümde göreceğiz.



- **Üçgen açılış**: Kanalları işbirliği içinde açmak isteyen düğümler için platformlar mevcuttur ve her birinin anında gelen ve giden likiditeden yararlanmasına olanak tanır. Örneğin, [LightningNetwork+](https://lightningnetwork.plus/) bu hizmeti sunmaktadır. Alice, Bob ve Suzie 100.000 Sats ile bir kanal açmak isterse, Alice'nin Bob'a, Bob'un Suzie'ye ve Suzie'nin Alice'ye bir kanal açması için bu platform üzerinde anlaşabilirler. Bu şekilde, her biri 100.000 Sats giden likiditeye ve 100.000 Sats gelen likiditeye sahip olurken, yalnızca 100.000 Sats'i kilitlemiş olur.


![LNP201](assets/en/073.webp)



- **Kanal satın alma**: Lightning kanallarını kiralamak için [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) veya [Lightning Labs Pool](https://lightning.engineering/pool/) gibi gelen likiditeyi elde etmek için hizmetler de mevcuttur. Örneğin, Alice ödeme alabilmek için kendi node'una bir milyon satoshilik bir kanal satın alabilir.


![LNP201](assets/en/074.webp)


Son olarak, hedefleri işlenen ödeme sayısını ve toplanan ücretleri en üst düzeye çıkarmak olan yönlendiriciler için şunları yapmaları gerekir:



- Stratejik düğümlerle iyi finanse edilen kanallar açın.
- Kanallardaki fon dağılımını ağın ihtiyaçlarına göre düzenli olarak ayarlayın.


### Loop Out Hizmeti


Lightning Labs tarafından sunulan [Loop Out](https://lightning.engineering/loop/) hizmeti, Bitcoin Blockchain'deki fonları geri alırken likiditenin kanalın karşı tarafına taşınmasına olanak tanır. Örneğin, Alice Lightning aracılığıyla bir döngü düğümüne 1 milyon satoshi gönderir ve bu düğüm de bu fonları On-Chain bitcoinleri olarak kendisine iade eder. Bu, kanalını her iki tarafta da 1 milyon satoshi ile dengeleyerek ödeme alma kapasitesini optimize eder.


![LNP201](assets/en/075.webp)


Dolayısıyla bu hizmet, kişinin On-Chain bitcoinlerini geri alırken gelen likiditeyi mümkün kılmakta, bu da Lightning ile ödeme kabul etmek için gereken nakdin hareketsiz kalmasını sınırlandırmaya yardımcı olmaktadır.


**Bu bölümden ne anlamalısınız?**



- Lightning'de ödeme göndermek için kanallarınızda yeterli likiditeye sahip olmanız gerekir. Bu gönderme kapasitesini artırmak için yeni kanallar açmanız yeterlidir.
- Ödemeleri almak için karşı tarafta kanallarınızda likidite olması gerekir. Bu alım kapasitesini artırmak daha karmaşıktır, çünkü başkalarının size doğru kanallar açmasını veya likiditeyi diğer tarafa taşımak için (hayali veya gerçek) ödemeler yapmasını gerektirir.
- Likiditeyi istenilen yerde tutmak, kanalların kullanımına bağlı olarak daha da zor olabilir. Bu nedenle kanalları istenilen şekilde dengelemeye yardımcı olacak araçlar ve hizmetler mevcuttur.


Bir sonraki bölümde, bu eğitimin en önemli kavramlarını gözden geçirmeyi öneriyorum.


# Daha ileri git


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Kurs Özeti



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


LNP201 eğitiminin sonuna işaret eden bu son bölümde, birlikte ele aldığımız önemli kavramları tekrar gözden geçirmeyi öneriyorum.


Bu eğitimin amacı size Lightning Network hakkında kapsamlı ve teknik bir anlayış sağlamaktı. Lightning Network'nın off-chain işlemlerini gerçekleştirmek için Bitcoin Blockchain'ye nasıl dayandığını ve Bitcoin'un temel özelliklerini, özellikle de diğer düğümlere güvenme ihtiyacının olmamasını nasıl koruduğunu keşfettik.


### Ödeme Kanalları


İlk bölümlerde, iki tarafın bir ödeme kanalı açarak Bitcoin Blockchain dışında nasıl işlem yapabileceğini araştırdık. İşte ele alınan adımlar:



- **Kanal Açma**: Kanalın oluşturulması, fonları 2/2 çoklu imza Address'te kilitleyen bir Bitcoin işlemi aracılığıyla yapılır. Bu para yatırma işlemi Blockchain üzerindeki Lightning kanalını temsil eder.


![LNP201](assets/en/076.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a [commitment transaction](https://planb.academy/resources/glossary/commitment-transaction).

![LNP201](assets/en/077.webp)



- **Güvence ve Kapanış**: Katılımcılar, fonları güvence altına almak ve herhangi bir hileyi önlemek için iptal anahtarlarını değiş tokuş ederek kanalın yeni durumunu taahhüt ederler. Her iki taraf da Bitcoin Blockchain üzerinde yeni bir işlem yaparak ya da son çare olarak zorunlu kapatma yoluyla kanalı işbirliği içinde kapatabilir. Bu son seçenek, daha uzun ve bazen ücretler açısından kötü değerlendirildiği için daha az verimli olsa da, yine de fonların geri kazanılmasına izin verir. Hile durumunda, mağdur Blockchain'teki kanaldan tüm fonları geri alarak hilekarı cezalandırabilir.


![LNP201](assets/en/078.webp)


### Kanallar Ağı


İzole kanalları inceledikten sonra, analizimizi kanal ağına genişlettik:



- **Yönlendirme**: İki taraf bir kanalla doğrudan bağlı olmadığında, ağ aracı düğümler üzerinden yönlendirmeye izin verir. Ödemeler daha sonra bir düğümden diğerine geçer.


![LNP201](assets/en/079.webp)



- **HTLC'ler**: Aracı düğümler üzerinden geçen ödemeler, ödeme uçtan uca tamamlanana kadar fonların kilitlenmesini sağlayan "_Hash Time-Locked Contracts_" (HTLC) ile güvence altına alınır.


![LNP201](assets/en/080.webp)



- **Soğan Yönlendirme**: Ödemenin gizliliğini sağlamak için, soğan yönlendirme son hedefi aracı düğümlere maskeler. Bu nedenle gönderen düğüm tüm rotayı hesaplamalıdır, ancak kanalların likiditesi hakkında tam bilgi olmadığında, ödemeyi yönlendirmek için ardışık denemeler yoluyla ilerler.


![LNP201](assets/en/081.webp)


### Likidite Yönetimi


Yıldırım'da ödemelerin sorunsuz akışını sağlamak için likidite yönetiminin bir zorluk olduğunu gördük. Ödeme göndermek nispeten basittir: sadece bir kanal açmayı gerektirir. Ancak ödeme almak, kanalların karşı tarafında likidite olmasını gerektirir. İşte tartışılan bazı stratejiler:



- **Kanalları Çekmek**: Bir kullanıcı, diğer düğümleri kendisine doğru kanal açmaya teşvik ederek gelen likiditeyi elde eder.



- **Hareketli Likidite**: Ödemelerin diğer kanallara gönderilmesiyle likidite karşı tarafa geçer.


![LNP201](assets/en/082.webp)



- **Loop ve Pool** gibi Hizmetleri Kullanma: Bu hizmetler, karşı tarafta likiditesi olan kanalların yeniden dengelenmesine veya satın alınmasına olanak tanır.

![LNP201](assets/en/083.webp)


- **İşbirlikçi Açılışlar**: Üçgen açılımlar gerçekleştirmek ve gelen likiditeye sahip olmak için bağlantı kurabileceğiniz platformlar da mevcuttur.


![LNP201](assets/en/084.webp)


Artık Lightning Network’ün teorik işleyişini anladığınıza göre, pratiğe geçebilir ve kullanımınızda daha fazla özerklik kazanmak için ilk Lightning düğümünüzü kurabilirsiniz. Bunun için LNP 202 kursunu takip edin:

https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

# Son Bölüm


<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>


## Yorumlar & Derecelendirmeler


<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Final Sınavı


<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Sonuç


<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>