---
name: Elements ve Liquid Network ile Bina
goal: Elements açık kaynaklı Blockchain platformunu ve temel özelliklerini kullanmayı ve geliştirmeyi öğrenin
objectives: 

  - Elements Blockchain platformu ve Liquid yan zincirlerinin temel kavramlarını anlama.
  - Bağımsız ve Sidechain yapılandırmaları için Elements düğümlerini kurmayı ve çalıştırmayı öğrenin.
  - Birleştirilmiş block signing ve Federated 2-Way Peg ile pratik deneyim kazanın.
  - Gerçek dünya kullanım durumları için güvenli, verimli Blockchain ortamları kurun ve yönetin.

---

# Liquid ve Elements üzerine inşa edin


Liquid ve Elements'nin gelişmiş özelliklerini ve yeteneklerini keşfedin ve geliştirme projelerinizi geliştirmek için bu araçları nasıl etkili bir şekilde kullanacağınızı öğrenin. Bu eğitim, Confidential Transactions, Issued Assets ve Federated block signing gibi özelliklerde uzmanlaşmanızı sağlayan eksiksiz bir teorik ve pratik temel sağlar.


Elements çerçevesini temel alan Liquid, finansal ve teknik çözümler için gizliliği, ölçeklenebilirliği ve işlevselliği geliştirmek üzere tasarlanmıştır. Bu eğitimde, varlık ihracı ve yönetimi, Federated 2-Way Peg ve elementsd ve elements-cli gibi araçların kullanımı konusunda uygulamalı deneyim kazanacak ve ihtiyaçlarınıza göre uyarlanmış yenilikçi çözümler oluşturmanızı sağlayacaksınız.


Bu eğitim, tüm deneyim seviyelerindeki geliştiriciler için hazırlanmıştır. Yeni başlayanlar ve orta düzey kullanıcılar erişilebilir açıklamalar ve pratik örnekler bulurken, ileri düzey kullanıcılar Liquid ve Elements'ün teknik ayrıntılarını ve daha az bilinen özelliklerini daha derinlemesine inceleyebilirler.


Becerilerinizi geliştirmek, Liquid ve Elements'nın tüm potansiyelini ortaya çıkarmak ve Liquid inovasyonunun geleceği için etkili araçlar oluşturmak için bize katılın.

+++

# Giriş


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Kursa Genel Bakış


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


SID202 kursuna hoş geldiniz!


Elements Academy'nin* amacı, Liquid Sidechain'un üzerine inşa edildiği açık kaynak platformu olan *Elements'in* temel kavramlarını tanıtmak ve açıklamaktır. Bu kursun sonunda, Elements'in Confidential Transactions ve Issued Assets gibi temel özelliklerinin yanı sıra Elements Core'un çalıştırılmasıyla ilgili süreçler hakkında sağlam bir anlayışa sahip olmalısınız. Kursun her bölümü, açıklayıcı metinler ve videolar içeren dersler ve ardından bir sınav içermektedir.


Bu eğitim, Liquid Network'e odaklanarak açık kaynaklı Elements platformunu nasıl kullanacağınızı ve geliştireceğinizi öğretmeyi amaçlamaktadır. Bu teknolojilerin geliştirme projelerinizin gizliliğini, ölçeklenebilirliğini ve işlevselliğini nasıl artırabileceğini keşfedeceksiniz. İster yeni başlayan ister deneyimli bir geliştirici olun, bu eğitim size Elements ve Liquid'in temel kavramlarının yanı sıra pratik uygulamalarına hakim olmanız için güçlü bir temel sağlayacaktır.


**Bölüm 1: Giriş**

Elements kavramlarına kapsamlı bir genel bakış ile başlayacağız. Bu platformun Liquid gibi yan zincirleri oluşturmak için modüler ve esnek bir temel sağlamak üzere nasıl tasarlandığını öğreneceksiniz. Amaç, pratik uygulamalarına dalmadan önce Elements'nın yapısını anlamaktır.


**Bölüm 2: Elements**

Bu bölüm Elements'ın nasıl çalıştığına odaklanacaktır. Bir Elements düğümünü nasıl yapılandıracağınızı, bağımsız modda nasıl çalıştıracağınızı veya Sidechain olarak nasıl kullanacağınızı öğreneceksiniz.


**Bölüm 3: Elements Kullanımı - Pratik Kullanım Örnekleri**

Teorik temellere hakim olduktan sonra, Elements'ün pratik uygulamalarını ele alacağız. Confidential Transactions'yi nasıl gerçekleştireceğinizi, varlıkları nasıl ihraç edeceğinizi ve varlıkların yeniden ihracını nasıl yöneteceğinizi öğreneceksiniz.


**Bölüm 4: Elements Federasyonu**

Burada, federe block signing, Elements'yi Sidechain olarak kullanma ve bağımsız blok zincirleri oluşturma gibi gelişmiş mekanizmaları inceleyeceğiz. Bu bölüm, Elements tabanlı blok zincirlerinin güvenliğini, bütünlüğünü ve birlikte çalışabilirliğini nasıl sağlayacağınızı anlamanıza yardımcı olacaktır.


Elements ve Liquid Sidechain'in potansiyelini keşfetmeye hazır mısınız? Haydi başlayalım!



## Elements Genel Bakış


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements, Confidential Transactions ve Issued Assets gibi topluluk üyeleri tarafından geliştirilen güçlü özelliklere erişim sağlayan açık kaynaklı, Sidechain özellikli bir Blockchain platformudur.


Elements, özünde, dağıtılmış bir Blockchain Ledger'da depolanan varlıkların transferini ve oluşturulmasını yöneten işlem geçmişi ve kuralları etrafında fikir birliği oluşturulmasını sağlayan bir protokoldür.


Elements hakkında daha fazla arka plan bilgisi Elements Projesi web sitesinde (https://elementsproject.org/), resmi Liquid blogunda (https://blog.Liquid.net/) ve geliştirici portalında (https://Liquid.net/devs) kolayca bulunabilir.


### Elements


2015 yılında piyasaya sürülen Elements, dahili geliştirme ve araştırma maliyetlerini azaltır ve en son Blockchain teknolojisini kullanarak uygulama için birçok yeni kullanım alanı açar. Elements tabanlı bir Blockchain, bağımsız bir Blockchain olarak çalışabilir ya da başka bir Blockchain'e bağlanarak Sidechain olarak çalıştırılabilir. Elements'in bir Sidechain olarak çalıştırılması, varlıkların farklı blok zincirleri arasında doğrulanabilir bir şekilde aktarılmasını sağlar.


Bitcoin'in kod tabanı üzerine inşa edilen ve bu kod tabanını genişleten bitcoind API'sine aşina olan geliştiricilerin hızlı ve uygun maliyetli bir şekilde çalışan blok zincirleri oluşturmasına ve kavram kanıtı projelerini test etmesine olanak tanır. Bitcoin kod tabanı üzerine inşa edilmiş olması, Elements'nın Bitcoin protokolünün kendisinde yapılacak değişiklikler için bir test ortamı olarak işlev görmesini de sağlar.


Elements'un bazı temel özellikleri aşağıda listelenmiştir.


#### Confidential Transactions


Varsayılan olarak, Elements'teki tüm adresler Confidential Transactions kullanan blinded'tür. Körleme, transfer edilen varlık miktarı ve türünün katılımcılar ve Blinding key'yi ifşa etmeyi seçtikleri kişiler dışında herkesten kriptografik olarak gizlendiği süreçtir.


#### Issued Assets


Elements üzerindeki Issued Assets, birden fazla varlık türünün çıkarılmasına ve ağ katılımcıları arasında aktarılmasına olanak tanır. İhraç Edilen bir Varlık da Confidential Transactions'dan yararlanır ve ilgili reissuance token'ye sahip olan herkes tarafından yeniden ihraç edilebilir veya imha edilebilir.


#### Federated 2-Way Peg


Elements, varlıkların bir zincirden diğerine iki yönlü aktarımını sağlamak için mevcut bir Blockchain'e (Bitcoin gibi) "sabitlenebilen" genel amaçlı bir Blockchain platformudur. Elements'ü bir Sidechain olarak uygulamak, ana zincirde güvence altına alınan varlıklar tarafından sağlanan güvenliğin iyi bir derecesini korurken, ana zincirin bazı doğal özelliklerinin etrafında çalışmanıza olanak tanır.


#### İmzalı Bloklar


Elements, blokları güvenilir ve zamanında imzalayan ve oluşturan Blok İmzalayıcılar olarak adlandırılan bir Strong Federation imzacı kullanır. Bu, rastgele poisson dağılımı nedeniyle büyük blok zamanı varyansına tabi olan PoW Mining sürecinin işlem gecikmesini ortadan kaldırır. Federe block signing süreci, üçüncü taraf güvenine ya da hesaplamalı `algoritma` tabanlı Mining'e ihtiyaç duymadan güvenilir blok oluşturmayı başarır.


Elements, tüm bu özellikleri Bitcoin core kod tabanının üzerine ekleyerek mainchain protokolünün yeteneklerini genişletir ve bir Sidechain veya bağımsız bir Blockchain çözümü olarak dağıtıldığında yeni iş kullanım durumlarını mümkün kılar.


# Element


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Elements Nasıl Çalışır?


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements, Blockchain kullanıcılarının her gün karşılaştığı işlem gecikmesi, gizlilik eksikliği ve değiştirilebilirlik riski gibi sorunlara teknik bir çözüm sunmaktadır.


Elements, Federated block signing ve Confidential Transactions'yi kullanarak bu sorunların üstesinden gelir.


Bitcoin ağının aksine, Elements içindeki block signing süreci Dinamik Üyelik Çok Taraflı İmzalara (DMMS) ve Proof of Work'e (PoW) bağlı değildir. Bunun yerine Elements, Blok İmzalayıcılar olarak adlandırılan ve blokları güvenilir ve zamanında imzalayıp oluşturabilen bir Strong Federation imzacı kullanır. Bu, rastgele poisson dağılımı nedeniyle büyük blok süresi varyansına maruz kalan PoW Mining sürecinin işlem gecikmesini ortadan kaldırır. Federated block signing süreci, üçüncü taraf güvenine ihtiyaç duymadan güvenilir blok oluşturmayı sağlar.


Elements, Bitcoin gibi başka bir Blockchain'ya Sidechain olarak veya diğer ağlara bağımlılığı olmayan bağımsız bir Blockchain olarak çalışabilir.


Sidechain olarak kullanıldığında, Strong Federation ayrıca bir ana zincir ile bir Elements Sidechain arasında varlıkların güvenli ve kontrollü transferini sağlayan üyeler içerir. Varlıkların kontrollü transferi Federated 2-Way Peg olarak adlandırılır ve varlık transferi rolünü yerine getiren üyeler watchmen olarak adlandırılır.


Bir Elements ağının işleyişinde yer alan süreçler ve ağdaki katılımcıların rolleri, Elements'in nasıl çalıştığını anlamak açısından önemlidir.


İster Sidechain ister bağımsız bir Blockchain olarak uygulansın, Elements blok üretmek için Blok İmzalayıcıların Güçlü Federasyonlarını kullanır.


### Güçlü Federasyonlar


Elements, ilk olarak Blockstream tarafından önerilen ve Güçlü Federasyonlar olarak adlandırılan bir konsensüs modeli kullanır. Bir Strong Federation, Proof of Work'ye (PoW) ihtiyaç duymaz ve bunun yerine Fonksiyonerler olarak adlandırılan karşılıklı olarak güvensiz bir grup katılımcının ortak eylemlerine dayanır.


Bir Görevlinin bir Strong Federation içinde yerine getirebileceği roller şunlardır: Blok İmzalayıcılar ve watchmen. Elements'i Sidechain veya bağımsız Blockchain modunda çalıştırırsanız Blok İmzalayıcılar gerekirken, watchmen yalnızca bir Sidechain kurulumunda gereklidir.


Bir Strong Federation üyesinin gerçekleştirebileceği eylemler, güvenliği artırmak ve bir saldırganın neden olabileceği hasarı sınırlamak için iki farklı rol arasında bölünmüştür.


Bu katılımcıların rolleri birleştirildiğinde, Elements'un hem hızlı blok oluşturma (daha hızlı ve nihai işlem onayı) hem de garantili, devredilebilir varlıklar (başka bir Blockchain'e doğrudan bağlanabilen sabitlenmiş varlıklar) sunmasına olanak tanır.


Güçlü Federasyonlar teknik raporunu buradan okuyabilirsiniz: https://blockstream.com/strong-federations.pdf


### Blok İmzalayanlar


Bitcoin'ler gibi bir Blockchain, dinamik bir blok imzalayanlar grubunun bir parçasını oluşturan herhangi biri, harcanan Proof of Work'u göstererek zinciri genişlettiğinde genişletilir. Setin dinamik yapısı, bu tür sistemlere özgü gecikme sorunlarını da beraberinde getirir.


Federasyon modeli, sabit bir imzacı seti kullanarak dinamik seti bilinen bir set, çoklu imza şeması ile değiştirir. Blockchain'ü genişletmek için gereken katılımcı sayısının azaltılması sistemin hızını ve ölçeklenebilirliğini artırırken, tüm taraflarca yapılan doğrulama işlem geçmişinin bütünlüğünü sağlar.


Federated block signing birkaç aşamadan oluşmaktadır:



- Adım 1 - Blok İmzalayıcılar, diğer tüm katılımcı Blok İmzalayıcılara yuvarlak robin şeklinde aday bloklar önerir.



- Adım 2 - Her block signer, verilen aday bloğu imzalamayı önceden taahhüt ederek niyetini bildirir.



- Adım 3 - Commitment öncesi için verilen eşik karşılanırsa, her block signer bloğu imzalar.



- Adım 4 - İmza eşiği (3. adımdakinden farklı olabilir) karşılanırsa, blok kabul edilir ve ağa gönderilir. Strong Federation en son işlem bloğu üzerinde mutabakata varmıştır.



- Adım 5 - Bir sonraki blok daha sonra round-robin'deki bir sonraki block signer tarafından önerilir ve süreç tekrarlanır.


Bir Strong Federation'ın blok üretimi olasılıklı olmadığından ve sabit bir imzalayanlar kümesine dayandığından, hiçbir zaman çoklu blok yeniden düzenlemelerine tabi olmayacaktır. Bu, işlemlerin onaylanmasıyla ilgili bekleme süresinde önemli bir azalma sağlar. Aynı zamanda kâr amacıyla madencilik yapma teşvikini (yani blok ödüllerini) ortadan kaldırır ve bunun yerine tüm katılımcıların aynı ortak hedefe sahip olduğu bir ağa verimli bir şekilde katılma teşvikini getirir; ağın herkes için faydalı olacak şekilde işlemeye devam etmesini sağlamak. Bunu tek bir başarısızlık noktası ya da daha yüksek güven gereksinimleri getirmeden yapar.


### Sidechain olarak Elements - watchmen ve Federated 2-Way Peg


Bir Sidechain olarak çalıştırıldığında, Strong Federation'in bazı üyelerinin yerine getirmesi gereken ek bir rol vardır: watchmen. watchmen, `Peg-In` ve `Peg-Out` olarak bilinen süreçlerle varlıkların bir Elements Sidechain'ya aktarılmasından ve Sidechain'dan çıkarılmasından sorumludur.


Bir Sidechain'in güvenilir bir şekilde çalışabilmesi için katılımcıların varlıkların Supply'ünün kontrollü ve doğrulanabilir olduğunu doğrulamasına izin vermesi gerekir. Bir Elements Sidechain, varlıkların bir Elements Blockchain içine ve dışına iki yönlü transferini sağlamak için bir 2-Yönlü federated peg kullanır. Bu, kanıtlanabilir ihraç ve zincirler arası transfer gereksinimlerini karşılar.


Federated 2-Way Peg özelliği, bir varlığın diğer blok zincirleriyle birlikte çalışabilmesini ve başka bir Blockchain'in yerel varlığının temsilcisi olmasını sağlar. Blockchain'inizi bir diğerine bağlayarak, mainchain'nın yeteneklerini genişletebilir ve bazı doğal sınırlamalarının üstesinden gelebilirsiniz.


Yüksek seviyede, Sidechain'ye transferler, bir kişi mainchain varlıklarını çok imzalı bir watchmen Wallet tarafından kontrol edilen bir Address'a gönderdiğinde gerçekleşir. Bu, mainchain üzerindeki varlıkları etkin bir şekilde dondurur. watchmen daha sonra işlemi doğrular ve Sidechain içindeki ilişkili varlığın aynı miktarını serbest bırakır. Serbest bırakılan varlıklar, orijinal mainchain varlıkları üzerinde hak iddia edebilecek bir Sidechain Wallet'e gönderilir. Bu süreç varlıkları ana zincirden Sidechain'ye etkin bir şekilde taşır.


Varlıkları mainchain'e geri aktarmak için bir kullanıcı Sidechain üzerinde özel bir peg-out işlemi yapar. Bu işlem watchmen tarafından kontrol edilir ve ardından mainchain üzerinde kontrol ettikleri çoklu-imzalı Wallet'ten bir işlem harcaması imzalarlar. mainchain işleminin geçerli olabilmesi için federasyondaki eşik sayıda katılımcının imzalaması gerekir. watchmen bir varlığı mainchain'e geri gönderdiğinde, Sidechain'deki ilgili miktarı da yok ederek varlıkları blok zincirleri arasında etkin bir şekilde aktarır.


## Elements'nın Kurulumu ve Çalıştırılması


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Elements, Bitcoin kod tabanına dayandığından, işleyen bir ağı oluşturan bileşenler çok benzerdir.


Elements düğüm yazılımının kendisi `elementsd` olarak adlandırılır ve kullanıcının makinesinde bir daemon olarak çalışır. Bir daemon (veya Windows'ta hizmet), oturum açmış bir kullanıcının doğrudan kontrolünü gerektirmeden arka plan hizmeti olarak çalışan bir programdır.


Not: Bu belge boyunca elementsd'den her zaman daemon sürümü olarak bahsedeceğiz, ancak sunucu seçeneğinin etkinleştirilmesi koşuluyla her şey Elements-qt ile yapılabilir.


Elements daemon ağdaki diğer düğümlere bağlanır, böylece Exchange işlem ve blok verilerini alabilir, ağın Blockchain'inin yerel kopyasını doğrulayabilir ve genişletebilir.


Elements yazılımı ayrıca komut satırından elementsd'e Uzaktan Prosedür Çağrısı (RPC) komutları göndermenizi sağlayan `elements-cli` adlı bir istemci programından oluşur. Bu, örneğin bir Wallet bakiyesini sorgulamak, işlem veya blok verilerini görüntülemek veya bir işlemi yayınlamak için kullanılabilir. Bu kurulum, Bitcoin eşdeğerleri olan bitcoind ve bitcoin-cli'i kullanmış olan herkese tanıdık gelecektir.


Bir Elements düğümü, başlangıçta veya bir yapılandırma dosyası aracılığıyla parametreler geçirilerek yapılandırılabildiğinden, aynı makinede çalışan birden fazla örneğe sahip olmak mümkündür. Bu, tek bir makinede kendi yerel ağınızı kurabileceğiniz, her Elements düğümünün Blockchain verilerinin kendi kopyasına sahip olduğu, kendi onaylanmamış geçerli işlemler havuzunu yönettiği ve farklı bağlantı noktalarındaki RPC isteklerini dinlediği için test ve geliştirme amaçları için kullanışlıdır.


### Elements Kod Deposu ve Topluluğu


Elements açık kaynaklı bir projedir ve kaynak kodu https://github.com/ElementsProject/Elements adresindeki Elements GitHub deposunda bulunabilir. Depo, elementsd ve elements-cli programlarının kaynağının yanı sıra destekleyici kurulum ve derleme araçları, bir test paketi ve bazı eğitici belgeler içerir.


Kod deposunu tamamlamak için, Elements'ün ne olduğu, nasıl çalıştığı ve kapsamlı bir öğretici bölümün açıklamalarını içeren topluluk odaklı bir kaynak olan https://elementsproject.org web sitesi de bulunmaktadır. Öğretici, komut satırı örneklerini takip ederek Elements hakkında bilgi edinmeye odaklanır ve bunun üzerine basit masaüstü ve web uygulamalarının nasıl oluşturulacağını gösterir. Site ayrıca popüler Elements topluluk tartışma forumlarını listeler ve GitHub'da barındırılarak sitenin içeriğine topluluk katkıları yapılmasına olanak tanır.


Elements'i makinenizde çalıştırmak için öncelikle kaynak kodunu klonlamanız (bir kopyasını indirmeniz), kodun sahip olduğu tüm bağımlılıkları yüklemeniz ve son olarak daemon ve istemci yürütülebilir dosyalarını oluşturmanız gerekecektir. Elements yazılımı daha sonra yapılandırılmaya ve çalıştırılmaya hazırdır.


## Düğümleri ve Ağları Yapılandırma


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Yapılandırma ayarları, çalışma, verileri doğrulama, diğer düğümlere bağlanma ve Blockchain verilerini başlatma şeklini değiştirmek için başlangıçta bir Elements düğümüne aktarılabilir.


Ayarlar ya belirlenen `Elements.conf` dosyasından yüklenir ya da komut satırı üzerinden parametre olarak aktarılır.


Bu parametreler kullanılarak bazı şeyler değiştirilebilir:



- Bağımsız bir Blockchain uygulamasında kullanılan default asset'ün adı.
- Oluşturulan ilk varlığın numarası.
- Ağdaki işlem ücretlerini öderken kullanılacak varlık.
- Blockchain veri dosyalarının depolama konumu.
- Bir Bitcoin düğümüne bağlanmak için kullanılan RPC kimlik bilgileri.
- Karşılanması gereken `n of m` eşiği ve blokları imzalayabilecek geçerli açık anahtarlar.
- Varlıkları bir Sidechain'in içine ve dışına aktarmak için tatmin edici olması gereken komut dosyası.
- Bir Bitcoin düğümüne Sidechain olarak bağlanılıp bağlanılmayacağı.


Bunların çoğu ağın mutabakat kurallarının bir parçasını oluşturur, bu nedenle başlangıçta tüm düğümlere uygulanmaları önemlidir. Bazıları bir zincir başlatıldıktan sonra değiştirilebilir, ancak bazılarının bir zinciri başlatmak için kullanıldıktan sonra düzeltilmesi gerekir.


Parametrelerin kullanımı kursun ilerleyen bölümlerinde her bir bölümle ilgili olarak ele alınacaktır.


### Komut Satırını Kullanarak Temel İşlemler


Bu kurs, bir veya daha fazla Elements düğümüne RPC çağrıları yapmak için `elements-cli` programını kullanan örnekleri gösterecektir. Bu bir terminal oturumundan yapılacaktır ve komutları daha kısa hale getirmek için bir `alias` kullanılacaktır. Bu konvansiyona göre aşağıdaki komutlar gibi bir şey gördüğünüzde:


```bash
e1-dae

e1-cli getnewaddress
```


E1-dae` ve `e1-CLI` aslında terminalin `alias` özelliğini kullanan tipografik bir kısayoldur. Komut çalıştırıldığında `e1-dae` ve `e1-CLI` gerçekte yer değiştirecek ve çalışacak komut şuna benzer olacaktır:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


Yukarıda gördüğümüz, Elements daemon'i başlatmak için bir çağrı ve `$HOME/Elements/src` dizininde bulunan elements-cli programlarına bir çağrı ve `datadir` parametresi için bir değerdir. Datadir` parametresi, daemon ve istemci örneklerine yapılandırma dosyalarını nerede bulacaklarını ve daemon durumunda Blockchain kopyasını nerede saklayacaklarını söylememizi sağlar. Bir yapılandırma dosyasını paylaştıklarından, istemci daemon'e RPC çağrıları yapabilecektir.


Yukarıdaki komutu tekrar çalıştırarak, ancak farklı bir `datadir` değeriyle, her biri Blockchain ve yapılandırma ayarlarının kendi ayrı kopyasına sahip birden fazla Elements örneği başlatabiliriz. Bu kurala göre, e1'inkinden farklı bir datadir dizinine atıfta bulunmak için kursta `e2-dae` ve `e2-CLI` takma adlarını kullanacağız. Yani ikinci `e2` örneğimiz için yukarıdaki örnek şöyle olacaktır:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Bu, düğümler arasında varlıkların işlem görmesi, varlıkların ihraç edilmesi ve aynı ağdaki farklı düğümler arasında Confidential Transactions'de körleme kullanımının kontrol edilmesi gibi her türlü işlemi gerçekleştirmemize olanak tanıyacaktır.


# Element Kullanımı Pratik kullanım örneği


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


Bu bölümde Elements'ün Confidential Transactions özelliğini nasıl kullanacağınızı öğreneceksiniz.


Elements'daki tüm adresler varsayılan olarak Confidential Transactions kullanan blinded'dir, bu da aktarılan varlıkların miktarını ve türünü yalnızca işlemdeki katılımcılar (ve Blinding key'i ifşa etmeyi seçtikleri kişiler) tarafından görülebilir tutarken, mevcut olandan daha fazla coin harcanamayacağını kriptografik olarak garanti eder.


### Gizli Adresler ve Confidential Transactions


Varsayılan olarak, `getnewaddress` komutunu kullanarak Elements'de yeni bir Address oluşturduğunuzda, bu bir Confidential Address olarak oluşturulur.


Confidential Transactions'ü göstermek için e2'nin kendisine bir miktar para göndermesini ve ardından işlemi e1'den görüntülemeye çalışmasını sağlayacağız. Bu, Elements'teki işlemlerin gizli doğasını gösterecektir.


Bir Elements düğümü tarafından üretilen her yeni Address varsayılan olarak gizlidir. Bunu e2'nin generate'ya yeni bir Address göndermesini sağlayarak gösterebiliriz.


```
e2-cli getnewaddress
```


Address'un e1 ile başladığına dikkat edin. Bu onu bir Confidential Address olarak tanımlar. Getaddressinfo komutunu kullanarak Address'u daha ayrıntılı incelemek, Address hakkında daha fazla ayrıntı gösterir.


```
e2-cli getaddressinfo <address>
```


Bize bunun bir Confidential Address olduğunu söyleyen bir confidential_key özelliği olduğunu görebilirsiniz.


Confidential_key, Confidential Address'in kendisine eklenen genel Blinding key'dir. Bir Confidential Address'in bu kadar uzun olmasının nedeni budur.


Ayrıca ilişkili bir Unconfidential address'e sahiptir. Elements içinde normal, gizli olmayan işlemler kullanmak isterseniz, varlıklar lq1 önekine sahip olan yerine bu Address'e gönderilmelidir.


Şimdi e2'nin oluşturduğu Address'ya bir miktar para göndermesini sağlayabiliriz. Bu daha sonra e1'in işlem yapan taraflardan biri olmadığı için işlemin ayrıntılarını görüntüleyemeyeceğini gösterecektir.


```
e2-cli sendtoaddress <address>
```


transaction ID'yi not edin. İşlemi onaylayın.


```
e2-cli -generate 101
```


E2'nin kendisine bir miktar fon gönderdiği işleme e2'nin kendi perspektifinden bakmak.


```
e2-cli gettransaction <txid>
```


İşlem ayrıntılarını yukarı kaydırdığınızda, e2'nin gönderilen ve alınan tutarların yanı sıra işlem yapılan varlığı da görüntüleyebildiğini görebilirsiniz. Ayrıca, işleme dahil olmayan diğer düğümlerden ayrıntıları gizlemek için kullanılan amountblinder ve assetblinder özelliklerini de görebilirsiniz.


Aynı işlemin ayrıntılarını e1'den kontrol etmek için önce ham işlem ayrıntılarını almamız gerekir.


```
e1-cli getrawtransaction <txid>
```


Bu, ham işlem ayrıntılarını döndürür. Vout bölümüne bakarsanız üç örnek olduğunu görebilirsiniz. İlk iki örnek alma ve değiştirme tutarları, üçüncüsü ise işlem ücretidir. Bu üç tutar arasında, ücretin kendisi her zaman Elements içinde unblinded olduğundan, ücret bir değer görebileceğiniz tek tutardır.


### Kör Edici Anahtarlar


İlk iki vout bölümünün gösterdiği, değer tutarlarının "Blinded ranges" ve işlem gören gerçek varlık miktarı ve türünün kanıtı olarak işlev gören Commitment verileridir.


E2'nin özel anahtarını e1'in Wallet'üne aktarsak bile, e2 tarafından kullanılan Blinding key hakkında hiçbir bilgisi olmadığı için işlem gören varlık miktarlarını ve türünü yine de göremeyecektir. Bunu, e2'nin Wallet'ü tarafından kullanılan özel anahtarı e1'inkine aktararak kanıtlayacağız. Öncelikle anahtarı e2'den dışa aktarmamız gerekiyor


```
e2-cli dumpprivkey <address>
```


Ardından e1'e aktarın.


```
e1-cli importprivkey <privkey>
```


Şimdi e1'in hala değerleri göremediğini kanıtlayabiliriz.


```
e1-cli gettransaction <txid>
```


Gerçekten de, aslında 1 olan tx miktarı 0 olarak gösteriliyor.


Gerçek, çizgisiz değeri görebilmek için Blinding key'e ihtiyacımız var. Bunu yapmak için önce Blinding key'ü e2'den dışa aktarıyoruz.


```
e2-cli dumpblindingkey <address>
```


Ardından e1'e aktarın.


```
e1-cli importblindingkey <address> <blinding key>
```


Şimdi e1'den işlem ayrıntılarını aldığımızda.


```
e1-cli gettransaction <txid>
```


Blinding key içe aktarıldığında, artık işlem içindeki 1'in gerçek değerini görüntüleyebileceğimizi gösterir.


Bu bölümde, bir Blinding key kullanımının bir işlemdeki varlıkların miktarını ve türünü gizlediğini ve doğru Blinding key'yi içe aktararak bu değerleri ortaya çıkarabileceğimizi gördük. Pratik kullanımda, örneğin bir tarafın sahip olduğu varlıkların miktar ve türlerinin doğrulanması gerektiğinde bir denetçiye bir Blinding key verilebilir. Confidential Transactions'nın Elements özelliği ayrıca "aralık kanıtlarının" gerçekleştirilmesine de olanak tanır. Aralık kanıtları, bir varlık miktarının belirli bir aralıkta tutulduğunu, gerçek miktarın kendisini ifşa etmeye gerek kalmadan kanıtlayabilir.


Ayrıca Confidential Transactions'un isteğe bağlı olduğunu, ancak yeni bir Address oluşturulduğunda varsayılan olarak etkinleştirildiğini gördük.


Bu ders için bu kadar; sınavda iyi şanslar ve bir sonrakinde görüşmek üzere!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


Bu bölümde Issued Assets'nin Elements özelliğini nasıl kullanacağınızı öğreneceksiniz.


Issued Assets, Elements ağ katılımcıları arasında birden fazla varlık türünün çıkarılmasını ve aktarılmasını sağlar. Ağ üzerindeki herhangi bir düğüm kendi varlıklarını ihraç edebilir. İhraçlar, kuponlar, kuponlar, para birimleri, mevduatlar, tahviller, hisseler vb. dahil olmak üzere herhangi bir varlığın değiştirilebilir Ownership'ini temsil edebilir. Issued Assets, Trustless borsaları, opsiyonları ve kendi kendine Issued Assets içeren diğer gelişmiş akıllı sözleşmelerin oluşturulmasına kapı açar.


İhraç Edilen bir Varlık da Confidential Transactions'den yararlanır ve ilgili token'a sahip olan herkes tarafından yeniden ihraç edilebilir.


İlk adım olarak, e1 ve e2 olarak adlandıracağımız iki Elements node'una erişmemiz gerekecek. Düğümlerin blok zincirleri sıfırlandı ve default asset aralarında paylaştırıldı.


Bu iki düğüm aynı yerel ağda yer alır ve birbirlerine bağlıdır, dolayısıyla Mempool işlemlerinde aynı işlemleri ve aynı blok zincirlerini paylaşırlar. Aynı makine üzerinde çalışıyor olmalarına rağmen, aynı gerçek Blockchain dosyalarını paylaşmadıklarını belirtmek gerekir. Her düğüm aynı işlem geçmişini içeren Blockchain'nin kendi yerel kopyasını yönetir çünkü fikir birliği içindedirler ve birbirleriyle aynı protokol kurallarına uyarlar.


Her bir düğümün ağdaki mevcut varlık ihraçları hakkındaki görüşünü kontrol ederek başlayalım.


Bu işlem listissuances komutu kullanılarak yapılır.


```
e1-cli listissuances

e2-cli listissuances
```


Gördüğünüz gibi, her iki düğüm de aynı ihraç geçmişini göstermektedir. Her ikisi de bir varlığı, on chain başlatma ile oluşturulan 21 milyon Bitcoin'nın ilk ihracını göstermektedir. Yukarıdaki komutun çalıştırılmasının sonuçlarında varlığın hex id'sini ve ayrıca varlığa atanan 'Bitcoin' etiketini görebilirsiniz.


Zincir başlatıldığında default asset'ye her zaman bir etiket verildiğini belirtmek gerekir. Kendi varlıklarınızı yayınladığınızda, onlar için etiketleri kendiniz ayarlayabilirsiniz, ki bunu birazdan yapacağız. Bunu yapmadan önce, kendi varlığımızı yayınlamamız gerekir.


E1'in yeni varlığı yayınlamasını sağlayacağız. Bu işlem issueasset komutu kullanılarak yapılır.


```
e1-cli issueasset 100 1 false
```


gW-279` 3 parametre kabul eder.


Çıkarılacak yeni varlığın miktarı, biz 100 kullandık. Oluşturulacak token miktarı (tokenlar bir varlığın miktarını yeniden ihraç etmek için kullanılır), biz 1'i seçtik. Son parametre Elements'e varlık ihracını blinded ya da unblinded olarak oluşturmasını söyler. İhraç tutarlarını bir dakika içinde e2'den görüntülemek istediğimiz için unblinded'i kullanacağız, bu nedenle false gireceğiz.


Komutun çalıştırılması ihraçla ilgili verileri döndürür. Bunlar, daha sonra kullanmak üzere bir kopyasını alabileceğiniz transaction ID'ü, varlığın benzersiz hex değerini ve varlığın token'ünün benzersiz hex değerini içerir.


generate ihraç işlemini onaylamak için bir blok.


```
e1-cli -generate 1
```


listissuances` komutunu e1'e karşı tekrar çalıştırın.


```
e1-cli listissuances
```


Bu bize e1'in şu anda 2 ihraçtan haberdar olduğunu gösteriyor: Bitcoin'nin ilk ihracı ve 100 tanesini görebildiğimiz yeni ihraç edilen varlığımız. Yeni varlığın hex değerine ve Bitcoin ihracında olduğu gibi ilişkili bir varlık etiketi olmadığına dikkat edin.


E2'nin bilinen ihraçlar listesini tekrar kontrol edin.


```
e2-cli listissuances
```


Bu bize e2'nin e1'in yaptığı varlık ihracından haberdar olmadığını gösterir. Sadece zaten görebildiği Bitcoin'in ilk ihracını görebilir.


Bunun nedeni, e2'nin e1 tarafından yayınlandığında yeni varlığın gönderildiği Address'dan habersiz olması ve bunu izlememesidir.


E2 ihracın kendisini göremese de, e1'in e2'ye varlığın bir kısmını gönderebileceğini belirtmek gerekir. Bu durumda yeni varlık, orijinal ihracın farkında olmasa bile e2'nin Wallet'ında kullanılabilir bakiye olarak görünecektir.


E2'nin gerçek ihracı (ve dolayısıyla ihraç edilen tutarı) görmesini sağlamak için, Address'i e2'ye izlenen bir Address olarak eklememiz gerekir.


Bunu yapmak için varlığın gönderildiği Address'ü bulmamız gerekir. Bunun için, daha önce kopyaladığımız transaction ID'yi kullanacağız ve e1'in bu işlemin ayrıntılarını almasını sağlayacağız, böylece e2'nin Wallet izleme listesine eklemek için doğru Address'ü bulabiliriz.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


İşlem verilerinin hex değerini yukarı kaydırdığınızda, hex değeri ile tanımlanan yeni varlığımızdan 100 adet alan Address'i göreceksiniz.


Address'yı alın ve kopyalayın, böylece e2'ye aktarabiliriz.


Şimdi bu Address'i e2'ye aktaralım. Bunu yapmak için importaddress komutunu kullanacağız.


```
e2-cli importaddress <the-issued-to-address>
```


Şimdi e2'nin ihraçlar listesini kontrol edersek.


```
e2-cli listissuances
```


Yeni ihraç edilen varlığımızın artık listeye dahil edildiğini görebilirsiniz. İhraç bir unblinded ihracı olduğu için e2 düğümü, ilişkili token miktarıyla birlikte ihraç edilen varlığın miktarını da belirleyebilmektedir. Elements içinde varlık kimliği ile ad eşlemesinin kullanımını etkinleştirmek için önce Elements'ü durdurun.


```
e1-cli stop
```


Ardından, bir varlığın hex'ini sağlanan etiketle eşleştiren ek bir parametre ile yeniden başlatın. Bu, düğümün varlık hakkındaki verileri bize daha insan tarafından okunabilir bir biçimde göstermesini sağlar. İsterseniz bunu Elements.conf dosyasının sonuna ekleyebilirsiniz, böylece daemon'ü her başlattığınızda argümanı eklemenize gerek kalmaz. Örneğin:


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Ancak biz burada argüman yöntemini kullanacağız.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


İhraçların listesi için düğüm tekrar sorgulanıyor.


```
e1-cli listissuances
```


Bu bize varlığın hex değerinin etiketiyle eşlenmesinin çalıştığını gösterir. E2 düğümünün ihraçlar listesini tekrar kontrol ediyorum.


```
e2-cli listissuances
```


E2 düğümünün bu etikete erişimi olmadığını görebilirsiniz, çünkü etiketler yalnızca onları ayarlayan düğüm tarafından kullanılabilir. Aslında, e2'deki aynı varlık hex'ine e1'de yaptığımızdan farklı bir etiket atayabiliriz. Önce e2 düğümünü durdurun.


```
e2-cli stop
```


Yeni varlığımızın hex'ine atanmış farklı bir etiketle yeniden başlatma.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


E2'den ihraçların listelenmesi.


```
e2-cli listissuances
```


Varlık etiketleri her düğüm için yereldir, yalnızca varlığın altıgeni ağdaki diğer düğümler tarafından tanınır.


Etiketin varlık altıgeniyle eşleştirilmesi, bir varlığa atıfta bulunmak için kısa bir yol sağladığından, işlemler ve Wallet bakiye sorguları gibi eylemleri gerçekleştirirken kullanışlıdır. Örneğin, yeni varlığımızın bir kısmını (10'luk bir miktar) etiket kullanmadan e1'den e2'ye göndermek istersek.


Öncelikle varlığı göndermek için bir Address almamız gerekiyor.


```
e2-cli getnewaddress
```


Ardından sendtoaddress komutunu kullanın.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


Bir blok oluşturarak işlemi onaylayın.


```
generate 1
```


Varlığın e2 üzerinden alındığının kontrol edilmesi.


```
e2-cli getwalletinfo
```


Varlığın gerçekten alındığını görebiliriz.


E2'nin alınan varlığın hex'ini eşlediğini ve kendi etiketini kullanarak görüntülediğini unutmayın. Aynı şeyi yapmanın daha kolay bir yolu, gönderirken e1'in varlık etiketini kullanmak olacaktır.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Perde arkasında Elements, Issued Assets'nin kullanımını basitleştirmeye yardımcı olmak için yerel etiketleri onaltılık değerlerle eşleştirir.


Bu bölümde varlıkların nasıl ihraç edileceğini ve etiketleneceğini gördük. Bir sonraki bölümde, ihraç edilen bir varlığın yeniden ihraç edilmesi ve miktarlarının yok edilmesine bakacağız.


## Varlıkların Yeniden İhracı


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


Bu bölümde, halihazırda ihraç edilmiş bir varlıktan nasıl daha fazla ihraç edeceğinizi ve ayrıca ihraç edilmiş bir varlığın belirli bir miktarını nasıl yok edeceğinizi öğreneceksiniz.


Bir varlığın yeniden ihraç edilmesi (daha fazla yaratılması) veya bir miktarının yok edilmesi ihtiyacı, varlık sabit bir Supply'a sahip olmayan bir şeyi temsil ettiğinde ortaya çıkması muhtemel bir durumdur. Bu, örneğin bir kasada tutulan altını temsil eden varlıklar için geçerli olabilir; altın birimleri kasaya girip çıktıkça, kasanın Supply'unu temsil eden varlığın buna göre yukarı veya aşağı ayarlanması gerekir.


Bir varlık tutarının yeniden ihraç edilmesi, ilk ihraç edildiğinde varlıkla birlikte oluşturulmuş olan ilgili token'in Ownership'unu gerektirir.


Bir varlıktan daha fazla oluştururken, bir varlığın bir miktarını yeniden ihraç eden düğüm, genellikle varlığın reissuance token'si olarak adlandırılan şeye sahip olduğu sürece, varlığı ilk etapta hangi düğümün ihraç ettiği önemli değildir. Başlangıçta reissuance token'nin nasıl oluşturulacağına, bir varlık miktarını yeniden ihraç etmek için nasıl kullanılacağına ve ayrıca reissuance token'nin diğer düğümlere nasıl aktarılacağına bakacağız, böylece onlar da varlığı yeniden ihraç etme iznine sahip olacaklar.


E1 ve e2 olarak adlandıracağımız iki Elements düğümüne erişmemiz gerekecek. Düğümlerin blok zincirleri sıfırlandı ve default asset aralarında paylaştırıldı.


E1'in yeni bir varlıktan 100 adet ihraç etmesini ve aynı varlık için 1 adet reissuance token oluşturmasını sağlayacağız. Örneği basitleştirmek için ihracı unblinded olarak oluşturacağız. Şimdi devam edelim ve varlığı ve ilişkili reissuance token'i ihraç edelim.


```
e1-cli issueasset 100 1 false
```


Varlığın ve ayrıca (yeniden düzenlenen) token'nin kimliğine dikkat edin.


Daha sonra e2'den daha fazla varlığı yeniden yayınlayacağımız için, varlığın yayınlandığı transaction ID'i not almamız ve bunu varlığın gönderildiği Address'u içe aktarmak için kullanmamız gerekecektir.


İşlemi onaylayın.


```
e1-cli -generate 1
```


Şimdi gettransaction komutunu kullanarak işlemin ayrıntılarını kontrol edeceğiz:


```
e1-cli gettransaction <txid>
```


İşlem verilerinin altıgenini yukarı kaydırdığınızda, işlemde e1'in 1 reissuance token ve ilişkili varlıktan 100 tane aldığını göreceksiniz.


Address'nin bir kopyasını alın, böylece e2'ye aktarabiliriz.


Ve şimdi Address'ü e2'nin Wallet'üne aktarıyorum.


```
e2-cli importaddress <address>
```


Artık hem e1 hem de e2'nin varlık ihracından haberdar olduğunu görebiliriz.


```
e1-cli listissuances

e2-cli listissuances
```


Şu anda e1 bir miktar varlığa ve 1 reissuance token'e sahiptir ancak e2 sahip değildir.


```
e1-cli getwalletinfo
```


Ayrıca, işlem ücretlerini karşılamak için küçük bir miktar ödediği için e1'in eskisinden daha az default asset'ya sahip olduğunu unutmayın. Bu tutar, oluşturulan blok 100 blok derinliğinde olgunlaştığında e1 tarafından tahsil edilecektir.


```
e2-cli getwalletinfo
```


E1 reissuance token'yi elinde tuttuğu için daha fazlasını yeniden yayınlayabilir. Bu, reissueasset komutu kullanılarak yapılır. E1'in bu varlıktan 100 tane daha yayınlamasını sağlayalım.


```
e1-cli reissueasset <asset-id> 100
```


Yeniden düzenlemenin işe yarayıp yaramadığını kontrol ediyorum.


```
e1-cli getwalletinfo
```


Beklendiği gibi e1'in şu anda 200 varlık tuttuğunu görebilirsiniz.


E2'nin elinde reissuance token tutarı olmadığından, varlığı yeniden ihraç etmeye çalışırlarsa bir hata alacaklardır.


```
e2-cli reissueasset <asset-id> 100
```


Hata mesajına dikkat edin.


listissuances komutunu kullanarak e1'den yeniden yayınlama ayrıntılarını görüntüleyebiliriz.


```
e1-cli listissuances
```


Is_reissuance` bayrağına dikkat edin.


Şimdi e2'ye bir miktar reissuance token gönderirsek, varlığın bir miktarını kendileri yeniden düzenleyebilecekler. Öncelikle bunu göndermek için bir Address'e ihtiyacımız var. Bakiyeleri gönderirken ve görüntülerken reissuance token'in Elements'deki diğer varlıklarla aynı şekilde ele alındığını ve diğer varlıklar gibi daha küçük kupürlere bölünebileceğini belirtmek gerekir, bu nedenle varlığı yeniden ihraç edebilmesi için e2'ye 1 reissuance token göndermemiz gerekmez. Herhangi bir kupür yeterli olacaktır. E2'nin reissuance token'i alması için bir Address oluşturulması.


```
e2-cli getnewaddress
```


Ardından RIT'nin bir kısmını e1'den e2'ye gönderin.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


İşlemi onaylayın.


```
e1-cli -generate 1
```


Şimdi e2'nin gönderildiği 0,1'i tuttuğunu görebiliriz.


```
e2-cli getwalletinfo
```


Bu, e2'nin artık Wallet'ünde tuttuğu RIT ile ilişkili varlıktan daha fazlasını yeniden ihraç edebileceği anlamına gelir. E2'nin varlığın 500'ünü yeniden ihraç etmesini sağlayacağız.


```
e2-cli reissueasset <asset-id> 500
```


Yeniden düzenleme sonucunu kontrol edin.


```
e2-cli getwalletinfo
```


E2'nin artık yeniden ihraç edilen tutarı Wallet bakiyesinde tuttuğunu ve RIT'nin kendisinin varlığın yeniden ihracı sürecinde tüketilmediğini görebilirsiniz.


Bir varlığın bir miktarını imha etmek, en azından imha edilen miktarı elinde tutan herkesin yapabileceği bir şeydir, reissuance token tarafından yönetilmez.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


Bu bölümde bir varlığın nasıl ihraç edileceğini ve varlık ihracının bir parçası olarak isteğe bağlı olarak oluşturulan reissuance token'nin nasıl kullanılacağını gördük. Ayrıca bir reissuance token'yi transfer etmenin diğer herhangi bir varlığı transfer etmek kadar basit olduğunu ve herhangi bir miktarda reissuance token bulundurmanın sahibine ilgili varlıktan daha fazla ihraç etme hakkı verdiğini gördük. Bu nedenle, ağınızdaki yeniden ihraç tokenlarına kimin erişebileceğini kontrol etmek çok önemlidir. Ayrıca bir varlığın bir miktarının nasıl yok edileceğini ve bu sürecin reissuance token'ye sahip olmak tarafından kontrol edilmediğini gördük.


# Element Federasyonu


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements, geçerli bir blok üretmek için önerilen bir bloğu imzalaması gereken Strong Federation üyelerinin sayısını belirlemenize olanak tanıyan bir federasyon imzalama modelini destekler.


Daha önce ve örnek kolaylığı açısından, `generate` komutunu kullanarak bloklar oluşturuyorduk ve oluşturulan blokların ağ tarafından geçerli olarak kabul edilmesi için çoklu imza gereksinimini karşılaması gerekmiyordu.


Düğümlerimizi 2-of-2 Multisig blok oluşturma gerektirecek şekilde ayarlayacağız. Bu, yapılandırma dosyasına eklenebilen veya başlangıçta düğüme aktarılabilen signblockscript parametresi kullanılarak ayarlanacaktır. Bir zinciri bu parametre ile başlatmak için öncelikle bu zinciri oluşturan betiği oluşturmamız gerekir.


Bunu mevcut bazı düğümleri kullanarak yapacağız, çıkardıkları verileri kaydedeceğiz ve ardından zinciri sileceğiz, böylece signblockscript parametremizi kullanarak yeniden başlatabiliriz. Kod, ağın mutabakat kurallarının bir parçasını oluşturduğundan ve on chain başlatma ayarının yapılması gerekeceğinden bu gereklidir. Zaten var olan bir zincire daha sonraki bir tarihte eklenemez.


E1 ve e2 olarak adlandıracağımız iki Elements düğümüne erişmemiz gerekecek. Düğümlerin blok zincirleri sıfırlandı ve default asset aralarında paylaştırıldı.


Elements.conf dosyanızda con_max_block_sig_size parametresinin yüksek bir değere ayarlandığından emin olun, aksi takdirde bu bölümün ilerleyen kısımlarında block signing başarısız olacaktır. Biz bu eğitim için con_max_block_sig_size=2000 olarak ayarladık.


Blockchain'yi sıfırlayacağımız ve e1 ve e2 ile ilişkili cüzdanları sileceğimiz için, kullandığımız adreslerin, genel anahtarların ve özel anahtarların bir kopyasını daha sonra kullanabilmek için generate'e block signing betiğine almamız gerekecek.


İlk olarak, block signing düğümlerinin her birinin generate'e bir kopyasını almanız gereken yeni bir Address'ya ihtiyacımız var.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Daha sonra açık anahtarları adreslerden çıkarmamız ve daha sonra kullanmak üzere not etmemiz gerekir.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Ardından, Blockchain ve Wallet verilerimizi yeniden başlattıktan sonra düğümlerin blokları imzalayabilmesi için daha sonra yeniden içe aktaracağımız özel anahtarları çıkarın.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Şimdi 2'ye 2 çoklu imza gereksinimleri olan bir generate Redeem betiğine ihtiyacımız var. Bunu createmultisig komutunu kullanarak ve ilk parametreyi 2 olarak geçerek ve ardından iki açık anahtar sağlayarak yaparız. Ownership'un daha sonra blok oluşturulduğunda kanıtlamaya ihtiyaç duyduğu bu anahtarlardır.


E1 veya E2 düğümlerinden herhangi biri generate'ü Multisig'ye bağlayabilir.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


Bu bize daha sonra kullanmak üzere kopyalayabileceğiniz redeemscript'ümüzü verir.


Şimdi mevcut Blockchain ve Wallet verilerini silmemiz gerekiyor, böylece zincirin mutabakat kurallarının bir parçası olarak yeni signblockscript ile yeniden başlayabiliriz. Bu nedenle, yeni zincirde blokları imzalamak için kullanılacak özel anahtarlar gibi bazı verilerin bir kopyasını daha önce almamız gerekiyordu. Devam etmeden önce bunu yapmanız gerekir.


Mevcut Wallet ve zincir verilerimiz silindikten sonra artık düğümlerimizi başlatabilir ve signblockscript parametresini kullanarak yeni bir zincir başlatmalarını sağlayabiliriz. dynafed aktivasyonunu devre dışı bırakmak için -evbparams=dynafed:0:: geçelim, çünkü bu örnek için bu gelişmiş özelliğe ihtiyacımız yok.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Şimdi daha önce kaydettiğimiz özel anahtarları içe aktarmamız gerekiyor, böylece düğümlerimiz önerilen blokları imzalayabilir ve tamamlanmasına yardımcı olabilir.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


generate komutunun kullanımı artık düğümlerimiz tarafından uygulanan gerekli block signing kurallarını karşılayamadığı için hata vermelidir.


```
e1-cli -generate 1
```


Yeni bir blok önermek için herhangi bir düğüm getnewblockhex komutunu çağırabilir. Bu, ağımızdaki herhangi bir düğüm tarafından kabul edilmeden önce imzalanması gereken yeni bir bloğun hex'ini döndürür.


```
e1-cli getnewblockhex
```


Komutun sadece önerilen bir blok oluşturduğunu, generate oluşturmadığını unutmayın.


Bunu doğrulamak için Blockchain'imizde şu anda hiçbir blok olmadığını görebiliriz.


```
e1-cli getblockcount
```


Eğer blok hex'i önce imzalamadan göndermeyi denersek.


```
e1-cli submitblock <block-hex>
```


Bize blok kanıtının geçersiz olduğunu söyleyen bir mesaj alıyoruz. Bunun nedeni, henüz gerekli 2 taraftan 2'si tarafından imzalanmamış olmasıdır.


E1'in önerilen bloğu imzalamasını sağlayalım.


```
e1-cli signblock <block-hex>
```


E2'ye altıgeni imzalatın.


```
e2-cli signblock <block-hex>
```


E2'nin, e1'in önerilen bloğu imzalamasıyla oluşturulan çıktıyı imzalamadığına dikkat edin. Her ikisi de önerilen blok hex'i birbirlerinin sonuçlarından bağımsız olarak imzalar.


Şimdi e1 ve e2'nin blok imzalarını birleştirmemiz gerekiyor. Her iki düğüm de bunu yapabilir, tek ihtiyaçları olan diğer düğümün imzalı blok hex'idir.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


combineblocksigs komutunun imzalı bloğun onaltılık değerinin yanı sıra tamamlandı durumunun çıktısını verdiğini görebilirsiniz, bu da bize onaltılık değerin gönderilmeye hazır olduğunu söyler.


Şimdi herhangi bir düğüm tamamlanmış blok hex'i gönderebilir. Bunu e1'e yaptıracağız.


```
e1-cli submitblock <combined-signed-hex>
```


Gönderimin geçerli bir gönderim olup olmadığının kontrol edilmesi.


```
e1-cli getblockcount

e2-cli getblockcount
```


Hem e1 hem de e2'nin bloğu geçerli olarak kabul ettiğini ve Blockchain'nin yerel kopyalarının ucuna eklediğini görebilirsiniz.


Süreci özetlemek gerekirse. Bu bölümde:


- Bir blok önerdi.
- Her düğüme imzalattım.
- İmzaları birleştirdim.
- İmzaların geçerli olduğu ve zincirin redeemscript eşiğini karşıladığı kontrol edildi.
- Bloğu gönderdi.


Ağdaki her düğüm bloğu doğruladı ve Blockchain'un kendi yerel kopyasına ekledi.


### block signing


Süreç başlangıçta karmaşık görünse de, block signing'in Elements'deki sırası her zaman aynıdır ve ilk kurulumun yalnızca bir kez yapılması gerekir:


1. İlk kurulum (bir kez gerçekleştirilir)

2. Federasyon Blok İmzalayıcılarının açık anahtarları kullanılarak `signblockscript` adında çoklu-imzalı bir Address oluşturulur.

3. Bundan elde edilen Redeem komut dosyası yeni bir Blockchain başlatmak için kullanılır.

4. Blok üretimi (devam ediyor)

5. Önerilen bloklar oluşturulur ve imzalanmak üzere değiştirilir.


Önerilen blok eşik sayıda imzacı tarafından imzalandıktan sonra birleştirilir ve ağa gönderilir. Zincirin `signblockscript` kriterlerini karşılıyorsa, düğümler bunu geçerli bir blok olarak kabul eder.


## Yan Zincir Olarak Eleman


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements, Bitcoin gibi mevcut bir Blockchain'e "takılabilen" açık kaynaklı, genel amaçlı bir Blockchain platformudur. Başka bir Blockchain'e sabitlendiğinde, Elements'in bir `Sidechain` olarak çalıştığı söylenir. Yan zincirler, varlıkların bir zincirden diğerine iki yönlü olarak aktarılmasını sağlar. Elements'i bir Sidechain olarak uygulamak, mainchain'da güvence altına alınan varlıkların sağladığı güvenliğin iyi bir derecesini korurken, mainchain'ın bazı doğal sınırlamalarını aşmanıza olanak tanır.


Bir Sidechain, mainchain'ün ve işlem geçmişinin farkındayken, mainchain'ün Sidechain hakkında hiçbir farkındalığı yoktur ve çalışması için buna gerek yoktur. Bu, yan zincirlerin kısıtlama olmaksızın ya da mainchain protokolü iyileştirme önerileriyle ilişkili gecikmeler olmaksızın yenilik yapabilmelerini sağlar. Doğrudan değiştirmeye çalışmak yerine, ana protokolü genişletmek mainchain'ün kendisinin güvenli ve özel kalmasını sağlayarak Sidechain'ün sorunsuz çalışmasını destekler.


Bitcoin'un işlevselliğini genişleterek ve temel güvenliğinden yararlanarak, Elements tabanlı bir Sidechain, daha önce mainchain kullanıcıları için mevcut olmayan yeni işlevler sağlayabilir. Üretimde kullanılan Elements tabanlı bir Sidechain örneği Liquid Network'tir.


Bir Elements Blockchain'i bir Sidechain olarak başlatmak için federated peg script parametresini kullanmamız gerekir. Bu parametre bir düğümün yapılandırma dosyasında ayarlanabilir veya başlangıçta aktarılabilir.


federated peg script, Strong Federation'in hangi üyelerinin peg-in ve peg-out işlevlerini yerine getirebileceğini tanımlar. Bu görevliler, geçerli peg-in ve peg-out işlemleri için mainchain ve Sidechain'yi izledikleri ve geçerliyse bunları işleme koydukları için `watchmen` olarak adlandırılırlar. Peg-out etmek, sabitlenmiş varlıkları Sidechain'den çıkarıp mainchain'e taşımak ve peg-in etmek de sabitlenmiş varlıkları mainchain'den Sidechain'ye taşımak anlamına gelir. Sidechain'ye taşımak dediğimizde, aslında kastettiğimiz şey fonların mainchain'de çoklu-imzalı bir Address'de kilitlenmesi ve Elements'da Sidechain'ye karşılık gelen bir varlık miktarının yaratılmasıdır. Sidechain'den çık dediğimizde kastettiğimiz, varlıkların Elements Sidechain'de yok edildiği ve karşılık gelen miktarın mainchain'de tutulan kilitli fonlardan serbest bırakıldığıdır. Peg-in ve peg-out işlevlerini yerine getirme izni, görevlilerin federated peg script'te kullanılan açık anahtarların Ownership'yı kanıtlamasını gerektirir. Bu, ilgili özel anahtarların kullanılmasıyla yapılır.


Bu nedenle bir federated peg script oluşturmak için öncelikle her bir düğümümüzün generate bir açık anahtara sahip olması gerekir. Ayrıca, mevcut zincir verilerini silmemiz ve federated peg script'yi kullanarak yeni bir zincir başlatmamız gerekeceğinden, ilişkili özel anahtarları daha sonra kullanmak üzere saklamamız gerekir. Bunun nedeni, federated peg script'nin bir Sidechain'ün mutabakat kurallarının bir parçasını oluşturması ve daha sonraki bir tarihte mevcut, sabitlenmemiş bir Blockchain'e uygulanamamasıdır.


O halde her bir düğümümüzle bir generate bir Address yapalım, ilgili verileri daha sonra kullanmak üzere saklayalım ve Sidechain'mizi daha sonra başlatmak için kullanacağımız federated peg script'yı generate yapalım.


Öncelikle, ağımızda watchmen olarak görev yapacak her bir düğümümüzün generate'yi yeni bir Address'ye dönüştürmesi gerekmektedir.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Ardından açık anahtarları elde etmek için Address'ü doğrularız.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Ve ardından her bir Address ile ilişkili özel anahtarları alın.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Özel ve genel anahtarları daha sonra kullanmak üzere saklayın.


Şimdi bir federated peg script kullanarak yeni bir zincir başlatacağımız için mevcut Blockchain ve Wallet verilerini silmemiz gerekiyor. Bunu şimdi yapabilirsiniz. Sabitlememiz gereken Bitcoin daemon'u başlatmayı unutmayın.


Şimdi daha önce kaydettiğimiz açık anahtarlar kullanılarak oluşturulan bir federated peg script ile yeni bir zincir başlatabiliriz. Girdiğimiz ve açık anahtarlarımızı çevreleyen sayılar, kullanılan anahtar sayısını ve Sidechain'mize girip çıkmak için kanıtlanması gereken Ownership anahtarını tanımlar ve sınırlar.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Şimdi daha önce kaydettiğimiz özel anahtarları içe aktaracağız, böylece düğümlerimiz daha sonra zincirler arasındaki varlık transferini imzalayıp tamamlayabilir ve federated peg script'ün gerekliliklerini yerine getirebilir.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


Şimdi her iki zincirdeki bazı blokları olgunlaştırmamız gerekiyor. Blokların olgunlaşması, mainchain'daki blok yeniden düzenlemelerinin pegged asset Supply'nin Sidechain içinde şişmesine yol açmasına karşı koruma sağladığı için peg sürecinin bir gereğidir.


Bu bölümü federated peg'a odaklanmış halde tutmak için, son bölümde incelediğimiz block signing modelini kullanmadan bloklar oluşturacağız ve yeni bloklar oluşturmak için 'generate' komutunu kullanmaya geri döneceğiz.


```
b-cli generate 101

e1-cli generate 1
```


Elements için şu anda generate bloklarına ihtiyacımız yok. Ama yine de bir tane generate yapalım. Olası tutarsızlıkları önlemek için iyi bir uygulamadır.


Artık zincirimiz peg-in için hazır. Peg-in yapmak için getpeginaddress komutunu kullanarak generate'in özel bir türünü Address yapmamız gerekir. getpeginaddress ile bir peg-in Address oluşturmak ve claimpegin ile talep etmek arasındaki sürenin mümkün olduğunca küçük tutulması gerektiğini unutmayın. peg-in adresleri uzun süreli dayanıklı değildir ve tekrar kullanılmamalıdır.


```
e1-cli getpeginaddress
```


Komutun yeni bir mainchain Address ve peg-in fonlarını talep etmek için tatmin edilmesi gereken yeni bir komut dosyası oluşturduğunu görebilirsiniz. mainchain Address, Elements ağı içinde watchmen rolünü yerine getiren görevliler tarafından kullanılacak bir `pay to script Hash` Address'dir.


getnewaddress gibi, getpeginaddress de çağıran düğümün Wallet'üne yeni bir sır ekler, bu nedenle Wallet dosyasının yedeklenmesini düğüm yönetim sürecinize dahil etmeniz önemlidir.


Şimdi Bitcoin'den mainchain'ya bir miktar Sidechain göndereceğiz. mainchain regresyon testimiz Wallet zaten bir miktar fon tutuyor.


```
b-cli getwalletinfo
```


Wallet'ün 50 Bitcoin tuttuğunu görebiliriz. mainchain'dan Sidechain'a bir Bitcoin göndereceğiz. Düğümümüzün daha önce oluşturduğu mainchain Address'e para göndermemiz gerekiyor.


```
b-cli sendtoaddress <e1-pegin-address>
```


Bu işlemin kimliğini saklamamız gerekiyor çünkü daha sonra finansman kanıtı için buna ihtiyacımız olacak.


Artık mainchain Wallet bakiyesinin gönderdiğimiz miktar kadar azaldığını ve işlem ücretlerini karşılamak için küçük bir miktar daha eklendiğini görebiliyoruz.


```
b-cli getwalletinfo
```


İşlemi tekrar olgunlaştırmamız gerekiyor.


```
b-cli generate 101
```


Elements düğümümüzün peg-in fonlarını talep etmesi için peg-in işleminin yapıldığına dair "kanıt" elde etmemiz gerekir. Kriptografik kanıt, merkel yolunu hesaplamak için transaction ID fonunu kullanır ve işlemin onaylanmış bir blokta mevcut olduğunu kanıtlar.


```
b-cli gettxoutproof '["<tx-id>"]'
```


Ayrıca ham işlem verilerine de ihtiyacımız var.


```
b-cli getrawtransaction <tx-id>
```


Peg-in işleminin kanıtı ve ham verileri ile Elements düğümümüz artık ham işlemi ve işlem kanıtını kullanarak peg-in'i talep edebilir.


```
e1-cli claimpegin <raw> <proof>
```


claimpegin'a sağlayabileceğimiz isteğe bağlı üçüncü bir argüman olduğunu unutmayın. Bu üçüncü parametre, talep edilen fonların gönderileceği Sidechain Address'i belirtmek için kullanılabilir. Komutu, talep edilen fonların gideceği Address'in sahibi olan aynı düğümden çağırdığımız için örneğimizde buna gerek yoktu.


E1'in bakiyesi kontrol ediliyor.


```
e1-cli getwalletinfo
```


Talebi onaylamak için bir blok oluşturulması.


```
e1-cli generate 1
```


E1'in bakiyesi kontrol ediliyor.


```
e1-cli getwalletinfo
```


Peg-in'in başarılı bir şekilde talep edildiğini görebiliriz.


Sabitlemek için süreç benzerdir. Bir Address oluşturulur, fonlar buna gönderilir ve işlem geçerliyse fonlar serbest bırakılır. Bu dersin kapsamı dışında olan mainchain üzerinde çalışmayı içerdiği için tüm peg-out sürecini ele almayacağız. Elements olayları açısından adımlar, mainchain üzerinde bir Address oluşturulmasıdır.


```
b-cli getnewaddress
```


Fonlar sendtomainchain komutu kullanılarak bir Elements düğümünden mainchain Address'e gönderilir.


```
e1-cli sendtomainchain <new-address> 1
```


İşlemi onaylamak için bir blok oluşturma.


```
e1-cli generate 1
```


Düğümün Wallet bakiyesini kontrol edin.


```
e1-cli getwalletinfo
```


Ve bakiyenin azaldığını görün.


Bu bölümde nasıl yapılacağını gördük:


- generate a federated peg script.
- Komut dosyasını bir ağ mutabakat parametresi kuralı olarak kullanan yeni bir zincir başlatın.
- mainchain'ten Sidechain'ye para gönderin.
- Elements Sidechain kapsamındaki fonları talep edin.
- Fonların mainchain'ya geri gönderilmesinin nasıl başlatıldığını anlayın.


### FederatedPegScript



Elements'un bir Sidechain olarak çalışmasına izin vermek için, Blockchain'deki Genesis bloğu yerinde bir `fedpegscript` ile oluşturulmalıdır. Bu, düğüm başlatılırken `fedpegscript` parametresinin geçilmesiyle yapılır. Kod daha sonra Elements Blockchain'nin mutabakat kurallarının bir parçasını oluşturacak ve peg-in ve peg-out taleplerinin doğrulanmasına ve işleme konulmasına izin verecektir.


Fedpegscript`, peg eylemlerini gerçekleştirmeye yetkili kişiler tarafından kontrol edilen açık anahtarlardan oluşur. Aşağıda 2-of-2 çoklu-imzalı fedpegscript'in örnek formatı gösterilmektedir:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Not: Açık anahtarların dışındaki karakterler, açık anahtar ve `n of m` gereksinimlerini belirten sınırlayıcılardır. Örneğin, 1-of-1 fedpegscript için şablon '5121<pub key 1>51ae' olacaktır.


### Peg-in


Bir peg-in bir Elements Sidechain tarafından kabul edilmeden önce, mainchain üzerinde yeterli teyide sahip olmalıdır. Bu, mainchain'ün yeniden düzenlenmesinden kaynaklanabilecek Elements Sidechain üzerindeki pegged asset'in Supply'indeki enflasyonu önlemek için gereklidir.


Bitcoin Blockchain'nin ucunun kısa süreli yeniden düzenlenmesi, Proof of Work (PoW) mutabakat mekanizmasının normal işleyişinin bir parçası olarak beklenmektedir. Bu nedenle, Elements bir peg-in'i yalnızca Bitcoin Blockchain içinde yeterli derinliğe sahip olduğunda geçerli olarak kabul eder. Bu, Elements'in aynı peg-in'i birden fazla kez kabul etmesini önlemeye yarar.


### Peg-Out


Bir Elements düğümü, girdi olarak bir mainchain Address (peg-out hedefi) ve "çekilecek" pegged asset miktarını alan `sendtomainchain` komutunu çağırdığında bir peg-out gerçekleşir. Bu, Sidechain üzerinde bir peg-out işlemi yaratır. watchmen olarak hareket eden Fonksiyonerler, Sidechain'de peg-out işleminin onaylandığını tespit ettiklerinde, kursun önceki bölümlerinde öğrendiğimiz gibi, mainchain'teki varlığı peg-out hedefine gerçekten serbest bırakmaya özen gösterirler.


## Bağımsız bir Blockchain olarak Elements


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Şimdiye kadar Elements'ün bir Sidechain olarak nasıl çalıştırılacağını inceledik. Ancak, kendi varsayılan yerel varlığı ile bağımsız bir Blockchain çözümü olarak da çalışabilir. Bu kurulumda bir Elements Blockchain, Confidential Transactions ve Issued Assets gibi bir Sidechain uygulamasının tüm özelliklerini korur, ancak default asset miktarlarını dolaşıma eklemek veya dolaşımdan çıkarmak için peg-in veya peg-out'a ihtiyaç duymaz.


Bu bölümde şunları yapacağız:


Yeni bir Elements Blockchain'yı `newasset` adlı bir default asset ile başlatın.


Oluşturulacak 1.000.000 `newasset` ile birlikte bunun için 2 yeniden ihraç jetonu belirtin.


Tüm anyone-can-spend `newasset` paralarını talep edin.


'newasset' için tüm anyone-can-spend yeniden ihraç jetonlarını talep edin.


Varlığı ve reissuance token'sini başka bir düğümün Wallet'ine gönderin.


Her iki düğümden de daha fazla 'newasset' yayınlayın.


Bir Elements ağını bağımsız bir Blockchain olarak çalışacak şekilde başlatmak için her bir düğümün bazı temel parametrelerle başlatılması gerekir. Bunlar, düğüme başka bir Blockchain'ten peg-in'leri doğrulamaya çalışmamasını, ağın default asset'ünün adını ve oluşturulacak default asset ve ilişkili reissuance token miktarını söylemek için kullanılır.


Şimdi birbirine bağlı iki Elements düğümümüzde bu parametreleri kullanarak yeni bir zincir başlatacağız. default asset'ya `newasset' adını vereceğiz ve bunlardan bir milyon adet ve iki adet `newasset' reissueance token çıkaracağız.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Burada kullanılan miktarların ağın kabul edebileceği en küçük değerde olduğunu, dolayısıyla iki yüz milyon yeniden ihraç jetonunun aslında iki tam jetona eşit olduğunu unutmayın. Aynı durum ilk serbest jetonların değeri için de geçerlidir.


Düğümümüzün mevcut Wallet bakiyelerini kontrol edin.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Başlatma işleminin doğru şekilde çalıştığını görebiliriz.


Varlıkların ilk ihracı 'herkes harcayabilir' olarak oluşturulduğundan, e1'in hepsini talep etmesini sağlayacağız, böylece e2'nin bunlara erişimini kaldırabiliriz.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Zaten default asset olduğu için gönderilecek varlık olarak 'newasset' belirtmemize gerek olmadığını unutmayın. ve bu nedenle ağ ücretlerini ödemek için kullanılan default asset.


Elements içinde, aynı Address'ye birden fazla varlık türü gönderebilirsiniz, böylece default asset'u almak için yeni oluşturduğumuz Address'yi yeniden kullanabilir ve yeniden ihraç belirteçleri için hedef Address olarak kullanabiliriz.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


İşlemleri onaylayın.


```
e1-cli generate 101
```


Şimdi e1'in varlığın ve reissuance token'ün tek sahibi olup olmadığını kontrol edeceğiz.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Ki durumun gerçekten de böyle olduğunu görebiliyoruz.


Şimdi 'newasset'in bir kısmını şu anda sıfır bakiyeye sahip olan e2'ye göndereceğiz.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Gönderilecek varlık türünü belirtmek zorunda olmadığımızı unutmayın, çünkü `newasset` ağın default asset'ü olarak oluşturulmuştur


Ayrıca `newasset` için yeniden ihraç token'larından bazılarını e2'ye gönderelim.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


İşlemleri onaylayın.


```
e1-cli generate 101
```


Cüzdanların buna göre güncellendiğini kontrol edebiliriz.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Şimdi e1'den bazı default asset'leri yeniden yayınlayacağız. Bunu yapabilmenin initialreissuancetokens başlangıç parametresi tarafından etkinleştirildiğini unutmayın. Bu parametre atlanırsa veya sıfıra ayarlanırsa, daha sonraki bir tarihte yeniden düzenlenemeyen bir default asset ile sonuçlanacaktır.


```
e1-cli reissueasset newasset 100
```


Bir Elements zinciri her zaman kendi default asset'sını etiketlediği için hex id değerini sağlamak yerine `newasset` etiketini kullanabildik.


default asset'in yeniden basımının işe yarayıp yaramadığını kontrol ediyorum:


```
e1-cli generate 101

e1-cli getwalletinfo
```


Şimdi e2'nin bazı `newasset' yeniden ihraç belirteçlerine sahip olduğu için default asset'u da yeniden ihraç edebileceğini kanıtlayacağız.


```
e2-cli reissueasset newasset 100
```


default asset'ın e2 tarafından yeniden düzenlenmesinin işe yarayıp yaramadığını kontrol ediyorum.


```
e2-cli generate 101

e2-cli getwalletinfo
```


Bu bölümde Elements'yi bağımsız bir Blockchain olarak kurduk ve temel işlevlerin beklediğimiz gibi çalıştığını kontrol ettik.


Başlangıç parametrelerini şu amaçlarla kullandık:


'newasset' adlı bir default asset ile yeni bir Elements Blockchain başlatın.


on chain başlatma oluşturmak için default asset miktarını belirtin.


default asset için bazı yeniden yayınlama belirteçleri oluşturun ve her iki düğümden daha fazla default asset'i yeniden yayınlayın.


Bağımsız Blockchain Elements ağımızda, diğer tüm işlemsel işlemler kursun ana bölümlerinde ele alınan örneklerle aynı şekilde çalışacak, ancak varsayılan ve ücret varlığı olarak `Bitcoin` yerine 'newasset'i kullanacaktır.


### Düğüm Başlatma ve Zincir Başlatma Parametreleri


Bir Elements düğümüne bağımsız bir Blockchain olarak çalışmasını söylemek için birkaç parametrenin birlikte kullanılması gerekir. Şimdi her birine bir göz atacağız ve ne işe yaradıklarını öğreneceğiz.


#### `validatepegin=0`

Bağımsız bir Blockchain'ün herhangi bir peg-in veya peg-out işlemini doğrulaması gerekmediğinden, bu kontrolleri devre dışı bırakmamız gerekir. Bu ayarla, Elements ağı bağımsız olarak çalışacağından Bitcoin istemci yazılımını çalıştırmanıza veya Bitcoin Blockchain'ün bir kopyasını saklamanıza gerek yoktur.


#### `defaultpeggedassetname`

Bu, Blockchain başlatıldığında oluşturulan default asset'nin adını belirtmenizi sağlar.


#### `initialfreecoins`

Oluşturulacak default asset'un numarası (Bitcoin'ın Satoshi birimine eşdeğer olarak).


#### `ilkihraçdokümanları`

default asset için oluşturulacak yeniden ihraç jetonlarının sayısı (Bitcoin'ün Satoshi birimine eşdeğer olarak). Bu olmadan default asset'den daha fazla oluşturmak imkansız olacaktır. default asset'den daha fazla yaratmanın mümkün olmasını istemiyorsanız, bu sıfır olarak ayarlanabilir veya atlanabilir.


Bu parametreleri kullanarak, bir düğümü başlatmak için ortak olan aşağıdaki gibi görünecektir:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Temel İşlemler


Defaultpeggedassetname` parametresi default asset'e bir etiket uygular. Bu ayar olmadan, default asset otomatik olarak `Bitcoin` olarak adlandırılacaktır. Önceki bölümlerde, kendi yayınladığımız varlıkları başka bir düğüme gönderdiğimizde, Elements'ya hangi varlığı gönderdiğimizi söylemek için varlık hex'ini veya yerel olarak uygulanan varlık etiketini belirtmemiz gerekiyordu. Defaultpeggedassetname` tüm düğümlerde geçerli olduğundan, adı `Bitcoin` olmasa bile, gönderirken isim vermemize gerek yoktur. Daha önce varsayılan olarak `Bitcoin` gönderen her fonksiyon artık default asset'i ne olarak etiketlemeyi seçtiyseniz onu gönderecektir.


Yani 10 adet yeni default asset'i bir Address'a göndermek kadar basit:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Ayrıca düğüme `initialreissuancetokens' için sıfırdan büyük bir değer verdiyseniz, default asset'den daha fazlasını yeniden yayınlayabilirsiniz; bu, Elements'yi bir Sidechain olarak çalıştırdığınızda mümkün olmayan bir şeydir.


Bunu yapmak için, default asset ile ilişkili token miktarına sahip herhangi bir düğümün formda bir komut vermesi yeterlidir:


```
e1-cli reissueasset <default asset name> <amount>
```


Yukarıdaki parametreleri kullanarak Elements'yi, Bitcoin ve diğer blok zincirlerinden ayrılmış, kendi default asset'i olan bağımsız bir Blockchain olarak çalıştırabilirsiniz.


## Sonuç


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


Bu derste Elements'in bir Sidechain'den başka bir Blockchain'a veya bağımsız bir Blockchain çözümü olarak uygulanabilen açık kaynaklı bir ağ protokolü olduğunu öğrendik.


Elements (https://github.com/ElementsProject/Elements) kaynak kodunun ve web sitesinin GitHub'da barındırıldığını ve Build On L2 (https://community.Liquid.net/c/developers/) veya Liquid Developers Telegram (https://t.me/liquid_devel) gibi Elements ve Liquid'de uygulama dağıtma ve geliştirme hakkında daha fazla bilgi edinmek için kullanılabilecek topluluk tartışma forumları olduğunu gördük. Confidential Transactions ve Issued Assets gibi temel özelliklerin yanı sıra Strong Federation üyelerinin federe block signing ve 2 Yönlü Peg mekanizmasını nasıl etkinleştirdiği de ele alındı.


Bir sonraki adım, önceki tüm bölümleri kapsayan kümülatif bir sınavla kendinize meydan okumak ve ardından Elements yolculuğunuza başlamaktır... iyi şanslar!


# Son Bölüm


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Yorumlar & Derecelendirmeler


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Sonuç


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>