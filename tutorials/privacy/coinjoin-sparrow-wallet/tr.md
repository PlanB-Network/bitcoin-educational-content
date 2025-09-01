---
name: CoinJoin - Sparrow wallet
description: Sparrow wallet üzerinde bir CoinJoin nasıl gerçekleştirilir?
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'nın kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Whirlpool aracı artık kendi Dojo'su olan veya Sparrow wallet kullanan kişiler için bile çalışmamaktadır. Bununla birlikte, bu aracın önümüzdeki haftalarda eski haline getirilmesi veya farklı bir şekilde yeniden başlatılması olasılığı devam etmektedir. Ayrıca, bu makalenin teorik kısmı, genel olarak (sadece Whirlpool değil) coinjoins'in ilke ve hedeflerini anlamak ve Whirlpool modelinin etkinliğini anlamak için geçerliliğini korumaktadır.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

Bu eğitimde, CoinJoin'un ne olduğunu ve Sparrow wallet yazılımını ve Whirlpool uygulamasını kullanarak nasıl gerçekleştirileceğini öğreneceksiniz.


## Bitcoin üzerindeki CoinJoin nedir?

**CoinJoin, Blockchain** üzerindeki bitcoinlerin izlenebilirliğini kıran bir tekniktir. Aynı adı taşıyan belirli bir yapıya sahip işbirlikçi bir işleme dayanır: CoinJoin işlemi.


Coinjoins, harici gözlemciler için zincir analizini zorlaştırarak Bitcoin kullanıcılarının gizliliğini artırır. Yapıları, farklı kullanıcılardan gelen birden fazla coinin tek bir işlemde birleştirilmesine olanak tanır, böylece izleri bulanıklaştırır ve giriş ve çıkış adresleri arasındaki bağlantıların belirlenmesini zorlaştırır.


CoinJoin'in prensibi işbirlikçi bir yaklaşıma dayanmaktadır: bitcoinlerini karıştırmak isteyen birkaç kullanıcı aynı işlemin girdileri olarak aynı miktarları yatırmaktadır. Bu tutarlar daha sonra her kullanıcıya eşit değerde çıktılar olarak yeniden dağıtılır. İşlemin sonunda, belirli bir çıktıyı girdideki bilinen bir kullanıcıyla ilişkilendirmek imkansız hale gelir. Girdiler ve çıktılar arasında doğrudan bir bağlantı yoktur, bu da kullanıcılar ve UTXO'leri arasındaki ilişkiyi ve her bir Coin'nın geçmişini bozar.

![coinjoin](assets/notext/1.webp)


Bir CoinJoin işlemi örneği (benden değil): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Her kullanıcının fonları üzerinde her zaman kontrol sahibi olmasını sağlarken bir CoinJoin gerçekleştirmek için süreç, işlemin bir koordinatör tarafından oluşturulması ve daha sonra her katılımcıya iletilmesiyle başlar. Her kullanıcı daha sonra işlemin kendisine uygun olduğunu doğruladıktan sonra imzalar. Toplanan tüm imzalar en sonunda işleme entegre edilir. Eğer bir kullanıcı ya da koordinatör tarafından CoinJoin işleminin çıktılarında bir değişiklik yapılarak fonların yönü değiştirilmeye çalışılırsa, imzalar geçersiz olacak ve işlemin düğümler tarafından reddedilmesine yol açacaktır.


Her biri katılımcılar arasındaki koordinasyonu yönetmeyi ve CoinJoin işlemlerinin verimliliğini artırmayı amaçlayan Whirlpool, JoinMarket veya Wabisabi gibi çeşitli CoinJoin uygulamaları vardır.


Bu eğitimde, Bitcoin üzerinde coin birleştirmeleri gerçekleştirmek için en etkili çözüm olduğunu düşündüğüm **Whirlpool** uygulamasına odaklanacağız. Çeşitli cüzdanlarda mevcut olmasına rağmen, bu eğitim yalnızca Sparrow wallet Masaüstü yazılımı ile kullanımını araştırmaktadır.

## Neden Bitcoin üzerinde CoinJoins gerçekleştirmelisiniz?


Herhangi bir eşler arası ödeme sistemiyle ilgili ilk sorunlardan biri Double-spending'dir: kötü niyetli bireylerin tahkim için merkezi bir otoriteye başvurmadan aynı parasal birimleri birden fazla kez harcaması nasıl önlenir?


Satoshi Nakamoto, herhangi bir merkezi otoriteden bağımsız olarak çalışan eşler arası bir elektronik ödeme sistemi olan Bitcoin protokolü aracılığıyla bu ikileme bir çözüm sundu. Beyaz kitabında, Double-spending'in yokluğunu belgelemenin tek yolunun ödeme sistemi içindeki tüm işlemlerin görünürlüğünü sağlamak olduğunu vurguluyor.


Her katılımcının işlemlerden haberdar olmasını sağlamak için bunların kamuya açıklanması gerekir. Bu nedenle, Bitcoin'in çalışması, herhangi bir düğüm operatörünün elektronik imza zincirlerinin tamamını ve bir Miner tarafından oluşturulmasından itibaren her bir Coin'ün geçmişini doğrulamasına olanak tanıyan şeffaf ve dağıtılmış bir altyapıya dayanır.


Bitcoin'in Blockchain'ün şeffaf ve dağıtık yapısı, herhangi bir ağ kullanıcısının diğer tüm katılımcıların işlemlerini takip ve analiz edebileceği anlamına gelir. Sonuç olarak, işlem düzeyinde anonimlik mümkün değildir. Bununla birlikte, anonimlik bireysel kimlik düzeyinde korunur. Her hesabın kişisel bir kimlikle bağlantılı olduğu geleneksel bankacılık sisteminin aksine, Bitcoin'te fonlar kriptografik anahtar çiftleriyle ilişkilendirilir ve böylece kullanıcılara kriptografik tanımlayıcıların arkasında bir tür takma ad sunar.


Bu nedenle, harici gözlemciler belirli UTXO'ları tanımlanmış kullanıcılarla ilişkilendirmeyi başardığında Bitcoin'deki gizlilik tehlikeye girer. Bu ilişki kurulduktan sonra, işlemlerini izlemek ve bitcoinlerinin geçmişini analiz etmek mümkün hale gelir. CoinJoin tam olarak UTXO'ların izlenebilirliğini kırmak için geliştirilmiş bir tekniktir, böylece Bitcoin kullanıcılarına işlem düzeyinde belirli bir Layer gizliliği sunar.


## Whirlpool Nasıl Çalışır?


Whirlpool, tüm girdiler ve tüm çıktılar arasında kesinlikle hiçbir teknik bağlantının mümkün olmamasını sağlayan "_ZeroLink_" işlemlerini kullanarak diğer CoinJoin yöntemlerinden ayrılır. Bu mükemmel karışım, her katılımcının aynı miktarda girdiye katkıda bulunduğu (Mining ücretleri hariç) ve böylece tamamen eşit miktarlarda çıktılar ürettiği bir yapı ile elde edilir.


Girdiler üzerindeki bu kısıtlayıcı yaklaşım Whirlpool CoinJoin işlemlerine benzersiz bir özellik kazandırmaktadır: girdiler ve çıktılar arasında deterministik bağlantıların tamamen yokluğu. Başka bir deyişle, her bir çıktının herhangi bir katılımcıya atfedilme olasılığı, işlemin diğer tüm çıktılarına kıyasla eşittir.

Başlangıçta, her bir Whirlpool CoinJoin'daki katılımcı sayısı 2 yeni katılımcı ve 3 remiksçi olmak üzere 5 ile sınırlıydı (bu kavramları daha sonra açıklayacağız). Ancak, 2023 yılında gözlemlenen On-Chain işlem ücretlerindeki artış, Samourai ekiplerini maliyetleri azaltırken gizliliği artırmak için modellerini yeniden düşünmeye sevk etti. Bu nedenle, ücretlerin piyasa durumunu ve katılımcı sayısını dikkate alarak, koordinatör artık 6, 7 veya 8 katılımcıyı içeren coinjoins düzenleyebilir. Bu geliştirilmiş oturumlar "_Surge Cycles_" olarak adlandırılır. Kurulumdan bağımsız olarak, Whirlpool coinjoin'lerinde her zaman yalnızca 2 yeni katılımcının olduğunu unutmamak önemlidir.


Bu nedenle, Whirlpool işlemleri aynı sayıda girdi ve çıktı ile karakterize edilir:


- 5 giriş ve 5 çıkış;

![coinjoin](assets/notext/2.webp)


- 6 giriş ve 6 çıkış;

![coinjoin](assets/notext/3.webp)


- 7 giriş ve 7 çıkış;

![coinjoin](assets/notext/4.webp)


- 8 giriş ve 8 çıkış.

![coinjoin](assets/notext/5.webp)

Whirlpool tarafından önerilen model bu nedenle küçük CoinJoin işlemlerine dayanmaktadır. Anonsetlerin sağlamlığının tek bir döngüdeki katılımcıların hacmine bağlı olduğu Wasabi ve JoinMarket'in aksine, Whirlpool birkaç küçük boyutlu döngünün zincirlemesine dayanır.


Bu modelde, kullanıcı yalnızca havuza ilk girişinde ücret ödemekte ve böylece ek ücret ödemeden çok sayıda remikse katılabilmektedir. Remiksörler için Mining ücretlerini üstlenenler yeni giriş yapanlardır.


Bir Coin'ün geçmişte karşılaştığı eşleriyle birlikte katıldığı her ek CoinJoin ile anonsetler katlanarak büyüyecektir. Bu nedenle amaç, her oluşumda her bir karışık Coin ile ilişkili anonsetlerin yoğunluğunu güçlendirmeye katkıda bulunan bu ücretsiz remikslerden yararlanmaktır.


Whirlpool iki önemli gereksinim dikkate alınarak tasarlanmıştır:


- Samourai Wallet'in öncelikle bir akıllı telefon uygulaması olduğu göz önüne alındığında, mobil cihazlarda uygulamanın erişilebilirliği;
- Yeniden karıştırma döngülerinin hızı, anonsetlerde önemli bir artışı teşvik eder.


Bu zorunluluklar Samourai Wallet'in geliştiricilerinin Whirlpool'nın tasarımındaki seçimlerine rehberlik etmiş ve onları döngü başına katılımcı sayısını sınırlamaya yönlendirmiştir. Çok az sayıda katılımcı CoinJoin'nin etkinliğini tehlikeye atarak her döngüde üretilen anonsları büyük ölçüde azaltırken, çok fazla katılımcı mobil uygulamalarda yönetim sorunları yaratacak ve döngülerin akışını engelleyecekti.


**Sonuç olarak, anonslar birkaç CoinJoin döngüsünün birikimi üzerinden yapıldığından, Whirlpool'da CoinJoin başına yüksek sayıda katılımcı olmasına gerek yoktur.**

[-> Whirlpool anonsları hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### CoinJoin havuzlar ve ücretler

Çoklu döngülerin karma coinlerin anonsetlerini etkili bir şekilde artırmasını sağlamak için, kullanılan UTXO miktarlarını kısıtlamak üzere belirli bir çerçeve oluşturulmalıdır. Whirlpool bu amaç için farklı havuzlar tanımlamaktadır.


Bir havuz, CoinJoin sürecini optimize etmek için kullanılacak UTXO miktarı üzerinde anlaşan ve bir araya gelmek isteyen bir grup kullanıcıyı temsil eder. Her havuz, UTXO için kullanıcının katılmak için uyması gereken sabit bir miktar belirler. Bu nedenle, Whirlpool ile coinjoins gerçekleştirmek için bir havuz seçmeniz gerekir. Şu anda mevcut olan havuzlar aşağıdaki gibidir:


- 0.5 bitcoin;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Bitcoinlerinizle bir havuza katıldığınızda, bunlar havuzdaki diğer katılımcılarınkiyle tamamen homojen olan generate UTXO'lara bölünecektir. Her havuzun bir maksimum limiti vardır; bu nedenle, bu limiti aşan miktarlar için, ya aynı havuzda iki ayrı giriş yapmak ya da daha yüksek bir miktarla başka bir havuza geçmek zorunda kalacaksınız:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Daha önce de belirtildiği gibi, bir UTXO bir CoinJoin'ye entegre edilmeye hazır olduğunda bir havuza ait olduğu kabul edilir. Ancak bu, kullanıcının mülkiyetini kaybettiği anlamına gelmez. **Çeşitli karıştırma döngüleri boyunca anahtarlarınızın ve dolayısıyla bitcoinlerinizin tam kontrolünü elinizde tutarsınız.** CoinJoin tekniğini diğer merkezi karıştırma tekniklerinden ayıran da budur.


Bir CoinJoin havuzuna girmek için hizmet ücretlerinin yanı sıra Mining ücretlerinin de ödenmesi gerekmektedir. Hizmet ücretleri her havuz için sabittir ve Whirlpool'in geliştirilmesi ve bakımından sorumlu ekiplere tazminat ödemeyi amaçlamaktadır. Sparrow wallet kullanıcıları için bu ücretler Samourai ekipleri tarafından Sparrow geliştiricilerine aktarılır.


Whirlpool'u kullanmak için hizmet ücretleri havuza girdikten sonra bir kez ödenmelidir. Bu adım tamamlandıktan sonra, ek ücret ödemeden sınırsız sayıda remikse katılma fırsatına sahip olursunuz. İşte her havuz için geçerli sabit ücretler:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Bu ücretler, CoinJoin'e koyduğunuz miktardan bağımsız olarak, esasen seçilen havuza giriş bileti görevi görür. Yani, ister 0,01 havuzuna tam olarak 0,01 BTC ile katılın, ister 0,5 BTC ile girin, ücretler mutlak değer olarak aynı kalacaktır.


Bu nedenle, coinjoins işlemine geçmeden önce kullanıcı 2 strateji arasında seçim yapabilir:


- Karşılığında birkaç küçük UTXO alacaklarını bilerek hizmet ücretlerini en aza indirmek için daha küçük bir havuzu tercih edin;
- Ya da daha büyük bir havuzu tercih ederek, daha az sayıda daha büyük değerli UTXO'larla sonuçlanmak için daha yüksek ücretler ödemeyi kabul eder.


Özellikle Ortak-Giriş-Ownership Sezgisel (CIOH) nedeniyle elde edilen gizliliği tehlikeye atabileceğinden, genellikle CoinJoin döngülerinden sonra birkaç karışık UTXO'nun birleştirilmemesi tavsiye edilir. Bu nedenle, çıktı olarak çok sayıda küçük değerli UTXO'ya sahip olmaktan kaçınmak için daha fazla ödeme yapmak anlamına gelse bile daha büyük bir havuz seçmek akıllıca olabilir. Kullanıcı tercih ettiği havuzu seçmek için bu ödünleşimleri tartmalıdır.


Hizmet ücretlerine ek olarak, herhangi bir Bitcoin işlemine özgü Mining ücretleri de dikkate alınmalıdır. Bir Whirlpool kullanıcısı olarak, hazırlık işlemi (`Tx0`) için Mining ücretlerinin yanı sıra ilk CoinJoin ücretlerini de ödemeniz gerekecektir. Whirlpool'ün yeni katılımcıların ödemelerine dayanan modeli sayesinde sonraki tüm remiksler ücretsiz olacaktır.


Gerçekten de, her bir Whirlpool CoinJoin'de, girdiler arasında iki kullanıcı yeni girenlerdir. Diğer girdiler remiksçilerden gelmektedir. Sonuç olarak, işlemdeki tüm katılımcıların Mining ücretleri, daha sonra ücretsiz remikslerden de yararlanacak olan bu iki yeni katılımcı tarafından karşılanır:

![coinjoin](assets/en/6.webp)

Bu ücret sistemi sayesinde, Whirlpool kendisini diğer CoinJoin hizmetlerinden gerçekten ayırmaktadır çünkü UTXO'ların anonimleri kullanıcı tarafından ödenen fiyatla orantılı değildir. Böylece, sadece havuzun giriş ücretlerini ve iki işlem için (`Tx0` ve ilk karışım) Mining ücretlerini ödeyerek oldukça yüksek anonimlik seviyelerine ulaşmak mümkündür.


Kullanıcının, aşağıdaki eğitimde tartışacağımız `mix to' seçeneğini seçmediği sürece, çoklu coin birleşimlerini tamamladıktan sonra UTXO'larını havuzdan çekmek için Mining ücretlerini de karşılaması gerekeceğini unutmamak önemlidir.


### Whirlpool tarafından kullanılan HD Wallet hesapları

CoinJoin aracılığıyla bir Whirlpool gerçekleştirmek için, Wallet'un birkaç farklı hesabı generate yapması gerekir. Bir HD (Hiyerarşik Deterministik) Wallet bağlamında bir hesap, diğerlerinden tamamen izole edilmiş bir bölüm oluşturur, bu ayrım Wallet'un hiyerarşisinin üçüncü derinlik seviyesinde, yani `xpub' seviyesinde gerçekleşir.

Bir HD Wallet teorik olarak en fazla `2^(32/2)` farklı hesap türetebilir. Tüm Bitcoin cüzdanlarında varsayılan olarak kullanılan ilk hesap `0'` indeksine karşılık gelir.


Samourai veya Sparrow gibi Whirlpool'ye uyarlanmış cüzdanlar için, CoinJoin sürecinin ihtiyaçlarını karşılamak üzere 4 hesap kullanılır:


- 0'` indeksi ile tanımlanan **depozito** hesabı;
- 2 147 483 644'` endeksi ile tanımlanan **kötü banka** (veya doxxic change) hesabı;
- 2 147 483 645'` endeksi ile tanımlanan **premix** hesabı;
- Postmix** hesabı, `2 147 483 646'` endeksi ile tanımlanmıştır.


Bu hesapların her biri CoinJoin içerisinde belirli bir işlevi yerine getirmektedir.


Tüm bu hesaplar tek bir seed'ye bağlıdır, bu da kullanıcının kurtarma cümlesini ve varsa passphrase'sını kullanarak tüm bitcoinlerine erişimi geri kazanmasına olanak tanır. Ancak, bu kurtarma işlemi sırasında kullanılan farklı hesap dizinlerinin yazılıma belirtilmesi gerekmektedir.


Şimdi bu hesaplar dahilinde bir Whirlpool CoinJoin'un farklı aşamalarına bakalım.


### Whirlpool'daki eş birleşmelerin farklı aşamaları

**1. Aşama: Tx0**

Herhangi bir Whirlpool CoinJoin'nin başlangıç noktası **deposit** hesabıdır. Bu hesap, yeni bir Bitcoin Wallet oluşturduğunuzda otomatik olarak kullandığınız hesaptır. Bu hesaba karıştırmak istediğiniz bitcoinler yatırılmalıdır.


Tx0' Whirlpool karıştırma işleminin ilk aşamasını temsil eder. Karışımın homojenliğini sağlamak amacıyla UTXO'ları seçilen havuzun miktarına karşılık gelen birimlere bölerek CoinJoin için hazırlamayı ve eşitlemeyi amaçlar. Eşitlenen UTXO'lar daha sonra **premix** hesabına gönderilir. Havuza giremeyen fark ise özel bir hesaba ayrılır: **kötü banka** (veya "doxxic change").


Bu ilk işlem `Tx0` aynı zamanda karışım koordinatörüne ödenmesi gereken hizmet ücretlerinin ödenmesine de hizmet eder. Sonraki aşamaların aksine, bu işlem işbirliğine dayalı değildir; bu nedenle kullanıcı Mining ücretlerinin tamamını üstlenmelidir:

![coinjoin](assets/en/7.webp)

Bu `Tx0` işlem örneğinde, **mevduat** hesabımızdan `372.000 Sats`lik bir girdi, aşağıdaki gibi dağıtılan birkaç giden UTXO'ya bölünür:


- 100.000 Sats`luk havuza girişe karşılık gelen hizmet ücretleri için koordinatöre yönelik 5.000 Sats`luk bir tutar;
- Karışım için hazırlanan üç UTXO, **premix** hesabımıza yönlendirildi ve koordinatöre kaydedildi. Bu UTXO'lar, gelecekteki ilk karışımları için Mining ücretlerini karşılamak amacıyla her biri `108.000 Sats` olarak eşitlenmiştir;
- Çok küçük olduğu için havuza giremeyen fazlalık, zehirli değişim olarak kabul edilir. Kendi özel hesabına gönderilir. Burada bu değişim `40,000 Sats` tutarındadır;
- Son olarak, bir çıktı oluşturmayan ancak `Tx0`ı onaylamak için gerekli olan Mining ücretleri olan `3.000 Sats` vardır.


Örneğin, işte gerçek bir Tx0 Whirlpool (benden gelmiyor): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**2. Adım: Zehirli Değişim**

Havuza entegre edilemeyen ve burada `40.000 Sats`e denk gelen fazlalık, Wallet'deki diğer UTXO'lardan kesin bir şekilde ayrılmasını sağlamak için "toksik değişim" olarak da adlandırılan **kötü banka** hesabına yönlendirilir.


Bu UTXO kullanıcının gizliliği için tehlikelidir çünkü sadece her zaman geçmişine ve dolayısıyla muhtemelen sahibinin kimliğine bağlı olmakla kalmaz, aynı zamanda bir CoinJoin gerçekleştirmiş bir kullanıcıya ait olduğu da belirtilir.


Bu UTXO karışık çıktılarla birleştirilirse, özellikle CIOH (*Common-Input-Ownership-Heuristic*) nedeniyle CoinJoin döngüleri sırasında kazanılan tüm gizliliği kaybedecektir. Diğer toksik değişikliklerle birleştirilirse, bu CoinJoin döngülerinin farklı girişlerini birbirine bağlayacağından kullanıcı gizliliği kaybetme riskiyle karşı karşıya kalır. Bu nedenle dikkatle ele alınmalıdır. Bu toksik UTXO'ü yönetmenin yolu bu makalenin son bölümünde ayrıntılı olarak açıklanacaktır ve gelecekteki eğitimler PlanB Ağındaki bu yöntemleri daha derinlemesine inceleyecektir.


**3. Adım: İlk Karışım**

Tx0`ın tamamlanmasından sonra, eşitlenmiş UTXO'lar Wallet'imizin **premix** hesabına gönderilir ve "ilk karışım" olarak da adlandırılan ilk CoinJoin döngüsüne dahil edilmeye hazır hale gelir. Örneğimizde olduğu gibi, `Tx0` karıştırma amaçlı birden fazla UTXO üretirse, bunların her biri ayrı bir ilk CoinJoin'e entegre edilecektir.

Bu ilk karışımların sonunda, **premix** hesabı boş olacak ve bu ilk CoinJoin için Mining ücretlerini ödemiş olan coinlerimiz tam olarak seçilen havuz tarafından tanımlanan miktara ayarlanacaktır. Örneğimizde, `108 000 Sats`lik ilk UTXO'larımız tam olarak `100 000 Sats`e düşürülmüş olacaktır.

![coinjoin](assets/en/8.webp)

**4. Adım: Remiksler**

İlk miksten sonra UTXO'lar **postmix** hesabına aktarılır. Bu hesap halihazırda karıştırılmış UTXO'ları ve yeniden karıştırılmayı bekleyenleri toplar. Whirlpool istemcisi aktif olduğunda, **postmix** hesabında bulunan UTXO'lar otomatik olarak remiks için hazır olur ve bu yeni döngülere katılmak üzere rastgele seçilir.


Bir hatırlatma olarak, remiksler %100 ücretsizdir: ek hizmet ücreti veya Mining ücreti gerekmez. UTXO'ların **postmix** hesabında tutulması, değerlerinin bozulmadan kalmasını sağlar ve aynı zamanda anonsetlerini iyileştirir. Bu nedenle, bu coinlerin birden fazla CoinJoin döngüsüne katılmasına izin vermek önemlidir. Size kesinlikle hiçbir maliyeti yoktur ve anonimlik seviyelerini artırır.


Karma UTXO'ları harcamaya karar verdiğinizde, bunu doğrudan bu **postmix** hesabından yapabilirsiniz. Ücretsiz remikslerden faydalanmak ve gizliliklerini azaltabilecek Whirlpool devresinden ayrılmalarını önlemek için karışık UTXO'ları bu hesapta tutmanız tavsiye edilir.


Bir sonraki derste göreceğimiz gibi, karışık madeni paralarınızı belirli sayıda madeni para birleşiminden sonra otomatik olarak Cold Wallet gibi başka bir Wallet'e gönderme imkanı sunan `mix to' seçeneği de vardır.


Teoriyi tartıştıktan sonra, Whirlpool'yı Sparrow wallet masaüstü yazılımı aracılığıyla kullanmaya ilişkin bir eğitimle uygulamaya geçelim!


## Eğitim: CoinJoin Whirlpool üzerinde Sparrow wallet

Whirlpool'i kullanmak için çok sayıda seçenek vardır. Size tanıtmak istediğim ilk seçenek, PC için açık kaynaklı bir Bitcoin Wallet yönetim yazılımı olan Sparrow wallet seçeneğidir.

Sparrow'ü kullanmak oldukça kolay başlama, hızlı kurulum ve bir bilgisayar ve internet bağlantısı dışında hiçbir ekipman gerektirmeme avantajına sahiptir. Bununla birlikte, dikkate değer bir dezavantajı vardır: coinjoins yalnızca Sparrow başlatıldığında ve bağlandığında gerçekleşecektir. Bu, bitcoinlerinizi 7/24 karıştırmak ve yeniden karıştırmak istiyorsanız, bilgisayarınızı sürekli açık tutmanız gerektiği anlamına gelir.


### Sparrow wallet'i kurun

Başlamak için tabii ki Sparrow wallet yazılımına ihtiyacınız olacak. Yazılımı doğrudan [resmi web sitesinden](https://sparrowwallet.com/download/) veya [GitHub](https://github.com/sparrowwallet/Sparrow/releases) adresinden indirebilirsiniz.


Yazılımı yüklemeden önce, yeni indirdiğiniz çalıştırılabilir dosyanın imzasını ve bütünlüğünü doğrulamak önemli olacaktır. Sparrow yazılımının kurulum süreci ve doğrulaması hakkında daha fazla ayrıntı istiyorsanız, bu diğer öğreticiyi okumanızı tavsiye ederim: *[The Sparrow wallet Guides](https://planb.network/tutorials/Wallet/desktop/Sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Bir Software Wallet oluşturun

Yazılımı yükledikten sonra, bir Bitcoin Wallet oluşturmaya devam etmeniz gerekecektir. Coinjoin'lere katılmak için bir Software Wallet ("Hot Wallet" olarak da adlandırılır) kullanımının gerekli olduğunu unutmamak önemlidir. Bu nedenle, **bir Hardware Wallet tarafından güvence altına alınmış bir Wallet ile coinjoins gerçekleştirmek mümkün olmayacaktır**.


Zorunlu olmamakla birlikte, önemli miktarlarda karıştırmayı planlıyorsanız, bu Wallet için güçlü bir BIP39 passphrase kullanmayı tercih etmeniz şiddetle tavsiye edilir.


Yeni bir Wallet oluşturmak için Sparrow'u açın, ardından `Dosya` sekmesine ve `Yeni Wallet`e tıklayın.


![sparrow](assets/notext/9.webp)


Bu Wallet için bir isim seçin, örneğin: "CoinJoin Wallet". Wallet Oluştur düğmesine tıklayın.


![sparrow](assets/notext/10.webp)


Varsayılan ayarları bırakın, ardından `Yeni veya İçe Aktarılan Software Wallet` düğmesine tıklayın.


![sparrow](assets/notext/11.webp)


Wallet oluşturma penceresine eriştiğinizde, yeterli olduğu için 12 kelimelik bir dizi seçmenizi öneririm. Yeni bir kurtarma ifadesi generate oluşturmak için `generate Yeni` seçeneğini seçin ve bir BIP39 passphrase eklemek istiyorsanız `passphrase Kullan` seçeneğine tıklayın. Bitcoinlerinizin güvenliğini sağlamak için kurtarma bilgilerinizin kağıt üzerinde veya metal bir destek üzerinde fiziksel bir yedeğini almanız önemlidir.


![sparrow](assets/notext/12.webp)

Yedeklemeyi Onayla...`ya tıklamadan önce kurtarma ifadesi yedeğinizin geçerliliğinden emin olun. Sparrow daha sonra not aldığınızı doğrulamak için ifadenizi tekrar girmenizi isteyecektir. Bu adım tamamlandıktan sonra `Anahtar Deposu Oluştur` seçeneğine tıklayarak devam edin.

![sparrow](assets/notext/13.webp)


Önerilen türetme yolunu varsayılan olarak bırakın ve `Import Keystore` düğmesine basın. Benim örneğimde, bu eğitim için Testnet kullandığımdan türetme yolu biraz farklıdır. Sizin için görünmesi gereken türetme yolu aşağıdaki gibidir:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


Bundan sonra, Sparrow yeni Wallet'inizin türetme ayrıntılarını görüntüleyecektir. Bir passphrase ayarlamış olmanız durumunda, `Ana parmak izinizi` not etmeniz önemle tavsiye edilir. Bu ana anahtar parmak izi hassas bir veri olmamasına rağmen, daha sonra doğru Wallet'e eriştiğinizi doğrulamanız ve passphrase'unuzu girerken hata olmadığını teyit etmeniz için yararlı olacaktır.


"Uygula" düğmesine tıklayın.


![sparrow](assets/notext/15.webp)


Sparrow sizi Wallet'ünüz için bir şifre oluşturmaya davet eder. Bu parola Sparrow wallet yazılımı üzerinden erişim için gerekli olacaktır. Güçlü bir parola seçin, bir yedeğini alın ve ardından `Parola Ayarla` düğmesine tıklayın.


![sparrow](assets/notext/16.webp)


### Bitcoin alma

Wallet'inizi oluşturduktan sonra, başlangıçta `0'` indeksli tek bir hesabınız olacaktır. Bu, önceki bölümlerde bahsettiğimiz **deposit** hesabıdır. Bu, bitcoinleri karıştırmak için göndermeniz gereken hesaptır.


Bunu yapmak için, pencerenin sol tarafındaki `Receive` sekmesini seçin. Sparrow, bitcoinleri almak için otomatik olarak yeni bir boş generate Address oluşturacaktır.


![sparrow](assets/notext/17.webp)


Bu Address için bir etiket girebilir ve ardından karıştırılacak bitcoinleri ona gönderebilirsiniz.


![sparrow](assets/notext/18.webp)


### Tx0'ın Yapılması

İşleminiz onaylandıktan sonra `UTXOs` sekmesine gidebilirsiniz.


![sparrow](assets/notext/19.webp)


Ardından, CoinJoin döngülerine göndermek istediğiniz UTXO(ler)i seçin. Aynı anda birden fazla UTXO seçmek için, seçtiğiniz UTXO'lara tıklarken `Ctrl` tuşunu basılı tutun.


![sparrow](assets/notext/20.webp)


Ardından pencerenin altındaki `Seçilen Karışım` düğmesine tıklayın. Bu düğme Interface'ünüzde görünmüyorsa, bunun nedeni bir Hardware Wallet ile sabitlenmiş bir Wallet'da olmanızdır. Sparrow ile eş birleştirmeler yapmak için bir Software Wallet kullanmanız gerekir.

![sparrow](assets/notext/21.webp)

Whirlpool'nin nasıl çalıştığını açıklayan bir pencere açılır. Bu, önceki bölümlerde anlattıklarımın basitleştirilmiş halidir. Devam etmek için `Sonraki` üzerine tıklayın.


![sparrow](assets/notext/22.webp)


Bir sonraki sayfada, eğer varsa bir "SCODE" girebilirsiniz. SCODE, havuzun hizmet ücretlerinde indirim sunan bir promosyon kodudur. Samourai Wallet, özel etkinlikler sırasında zaman zaman kullanıcılarına bu tür kodlar sağlar. Gelecekteki SCODES'leri kaçırmamak için sosyal medyada [Samourai Wallet'i takip etmenizi] (https://twitter.com/SamouraiWallet) tavsiye ederim.


Aynı sayfada, `Tx0` ve ilk karışımınız için ücret oranını da ayarlamanız gerekecektir. Bu seçim, hazırlık işleminizin ve ilk CoinJoin'unuzun onaylanma hızını etkileyecektir. Tx0` ve ilk miks için Mining ücretlerinden sorumlu olduğunuzu, ancak sonraki remiksler için Mining ücreti ödemeyeceğinizi unutmayın. Premiks Önceliği` kaydırıcısını tercihlerinize göre ayarlayın, ardından `Sonraki` üzerine tıklayın.


![sparrow](assets/notext/23.webp)


Bu yeni pencerede, açılır listeyi kullanarak girmek istediğiniz havuzu seçme seçeneğiniz olacaktır. Benim durumumda, başlangıçta `456 214 Sats`lik bir UTXO seçtikten sonra, mümkün olan tek seçeneğim `100 000 Sats`lik havuzdur. Bu Interface, ödenecek hizmet ücretlerinin yanı sıra havuza entegre edilecek UTXO'ların sayısı hakkında da sizi bilgilendirir. Koşullar sizin için tatmin edici görünüyorsa, `Preview Premix` seçeneğine tıklayarak devam edin.


![sparrow](assets/notext/24.webp)


Bu adımdan sonra, Sparrow sizden Wallet'nız için yazılım üzerinde oluştururken belirlediğiniz şifreyi girmenizi isteyecektir. Şifre girildikten sonra, `Tx0`ınızın önizlemesine erişeceksiniz. Pencerenizin sol tarafında, Sparrow'in Whirlpool'ü kullanmak için gerekli farklı hesapları oluşturduğunu göreceksiniz (`Deposit`, `Premix`, `Postmix` ve `Badbank`). Ayrıca `Tx0` yapınızı farklı çıktılarla birlikte görüntüleme fırsatına da sahip olacaksınız:


- Hizmet ücretleri;
- Eşitlenmiş UTXO'ların havuza girmesi amaçlanmıştır;
- Toksik değişim (Doxxic Change).


![sparrow](assets/notext/25.webp)


İşlem istediğiniz gibiyse, `Tx0`ınızı yayınlamak için `İşlemi Yayınla` seçeneğine tıklayın. Aksi takdirde, girilen verileri silmek ve oluşturma işlemini baştan başlatmak için `Temizle`yi seçerek bu `Tx0`ın parametrelerini ayarlama seçeneğiniz vardır.


### Coinjoins Gerçekleştirme

Tx0 yayınlandıktan sonra, UTXO'larınızı `Premix` hesabında karıştırılmaya hazır bulacaksınız.

![sparrow](assets/notext/26.webp)


Tx0' onaylandıktan sonra, UTXO'larınız koordinatöre kaydedilecek ve ilk miksler otomatik olarak art arda başlayacaktır.


![sparrow](assets/notext/27.webp)


Postmix' hesabını kontrol ederek, ilk karışımlardan kaynaklanan UTXO'ları gözlemleyeceksiniz. Bu coinler, herhangi bir ek ücrete tabi olmayan sonraki remiksler için hazır kalacaktır.


![sparrow](assets/notext/28.webp)


Karışımlar sütununda, her bir coininiz tarafından gerçekleştirilen coinjoins sayısını görmek mümkündür. İlerleyen bölümlerde göreceğimiz gibi, asıl önemli olan remiks sayısı değil, ilişkili anonsetlerdir, ancak bu iki gösterge kısmen ilişkilidir.


![sparrow](assets/notext/29.webp)


Eş birleştirmeleri geçici olarak durdurmak için `Karıştırmayı Durdur` seçeneğine tıklamanız yeterlidir. İstediğiniz zaman `Karıştırmayı Başlat` seçeneğini seçerek işlemlere devam etme seçeneğiniz olacaktır.


![sparrow](assets/notext/30.webp)


UTXO'larınızın remiksleme için sürekli kullanılabilirliğini sağlamak için Sparrow yazılımını aktif tutmak gerekir. Yazılımın kapatılması veya bilgisayarınızın kapatılması coinjoins'i duraklatacaktır. Bu sorunu aşmak için bir çözüm, işletim sisteminizin ayarları aracılığıyla uyku işlevlerini devre dışı bırakmaktır. Ayrıca, Sparrow bilgisayarınızın otomatik olarak uyku moduna geçmesini engellemek için `Araçlar' sekmesi altında `Bilgisayarın Uyumasını Engelle' başlıklı bir seçenek sunar.


![sparrow](assets/notext/31.webp)


### Eş birleşimlerin tamamlanması

Karışık bitcoinlerinizi harcamak için birkaç seçeneğiniz vardır. En doğrudan yöntem `Postmix` hesabına erişmek ve `Gönder` sekmesini seçmektir.


![sparrow](assets/notext/32.webp)


Bu bölümde, Sparrow wallet ile yapılan diğer işlemlerde olduğu gibi, hedef Address'u, gönderilecek tutarı ve işlem ücretlerini girme seçeneğiniz olacaktır. İsterseniz, `Gizlilik` düğmesine tıklayarak Stonewall gibi gelişmiş gizlilik özelliklerinden de yararlanabilirsiniz.


![sparrow](assets/notext/33.webp)


[-> Stonewall işlemleri hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Harcanacak madeni paralarınız arasında daha kesin bir seçim yapmak isterseniz, `UTXOs` sekmesine gidin. Özellikle tüketmek istediğiniz UTXO'ları seçin, ardından işlemi başlatmak için `Seçilenleri Gönder` düğmesine basın.


![sparrow](assets/notext/34.webp)

Son olarak, Sparrow'de bulunan `Mix to...` seçeneği, seçilen bir UTXO'in ek ücret ödemeden CoinJoin döngülerinden otomatik olarak çıkarılmasını sağlar. Bu özellik, UTXO'in `Postmix` hesabınıza yeniden entegre edilmeyeceği, bunun yerine doğrudan başka bir Wallet'e aktarılacağı bir dizi remiksin belirlenmesini sağlar. Bu seçenek genellikle karışık bitcoinleri otomatik olarak bir Cold Wallet'e göndermek için kullanılır.

Bu seçeneği kullanmak için, Sparrow yazılımı içinde CoinJoin Wallet ile birlikte alıcı Wallet'i açarak başlayın.


![sparrow](assets/notext/35.webp)


Ardından, `UTXOs` sekmesine gidin, ardından pencerenin altındaki `Mix to...` düğmesine tıklayın.


![sparrow](assets/notext/36.webp)


Bir pencere açılır, açılır listeden hedef Wallet'u seçerek başlayın.


![sparrow](assets/notext/37.webp)


Para çekme işleminin otomatik olarak yapılacağı CoinJoin eşiğini seçin. Kişisel durumunuza ve gizlilik hedeflerinize göre değiştiğinden, size gerçekleştirmeniz gereken kesin bir remiks sayısı veremem, ancak çok düşük bir eşik seçmekten kaçının. Remiksleme süreci hakkında daha fazla bilgi edinmek için bu diğer makaleye başvurmanızı tavsiye ederim: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-Whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


İndeks aralığı` seçeneğini varsayılan değeri olan `Tam`da bırakabilirsiniz. Bu fonksiyon farklı istemcilerden aynı anda karıştırmaya izin verir, ancak bu derste yapmak istediğimiz bu değil. Sonlandırmak ve `Mix to...` seçeneğini etkinleştirmek için `Restart Whirlpool` düğmesine basın.


![sparrow](assets/notext/38.webp)


Ancak, `Mix to` seçeneğini kullanırken dikkatli olun, çünkü karışık paraları `Postmix` hesabınızdan kaldırmak gizliliğinizi tehlikeye atma riskini önemli ölçüde artırabilir. Bu potansiyelin nedenleri aşağıdaki bölümlerde ayrıntılı olarak açıklanmıştır.


## CoinJoin döngülerimizin kalitesi nasıl anlaşılır?

Bir CoinJoin'in gerçekten etkili olabilmesi için, girdi ve çıktıların miktarları arasında iyi bir homojenlik sunması esastır. Bu homojenlik, harici bir gözlemcinin gözünde olası yorumların sayısını artırır ve böylece işlemin etrafındaki belirsizliği artırır. Bir CoinJoin tarafından yaratılan bu belirsizliği ölçmek için işlemin entropisini hesaplamaya başvurulabilir. Bu göstergelerin derinlemesine incelenmesi için sizi eğiticiye yönlendiriyorum: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Whirlpool modeli, eş birleşimlerde en fazla homojenliği sağlayan model olarak kabul edilmektedir.

Daha sonra, birkaç CoinJoin döngüsünün performansı, bir Coin'in gizlendiği grupların boyutuna göre değerlendirilir. Bu grupların boyutu anonset olarak adlandırılan şeyi tanımlar. İki tür anons vardır: ilki geriye dönük analize (günümüzden geçmişe) karşı kazanılan gizliliği, ikincisi ise ileriye dönük analize (geçmişten günümüze) karşı kazanılan gizliliği değerlendirir. Bu iki göstergenin ayrıntılı bir açıklaması için sizi öğreticiye başvurmaya davet ediyorum: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Postmix nasıl yönetilir?

CoinJoin döngülerini gerçekleştirdikten sonra, en iyi strateji UTXO'larınızı **postmix** hesabında tutmak ve gelecekte kullanılmalarını beklemektir. Hatta harcamanız gerekene kadar süresiz olarak remiks yapmalarına izin vermeniz tavsiye edilir.


Bazı kullanıcılar karışık bitcoinlerini bir Hardware Wallet ile güvence altına alınmış bir Wallet'e aktarmayı düşünebilir. Bu mümkündür, ancak elde edilen gizliliği tehlikeye atmamak için Samourai Wallet'in önerilerini titizlikle takip etmek önemlidir.


UTXO'ların birleştirilmesi en sık yapılan hatadır. CIOH'dan (*Common-Input-Ownership-Heuristic*) kaçınmak için aynı işlemde karışık UTXO'ları karışık olmayan UTXO'larla birleştirmekten kaçınmak gerekir. Bu, UTXO'larınızın Wallet içinde, özellikle etiketleme açısından dikkatli bir şekilde yönetilmesini gerektirir. CoinJoin'ün ötesinde, UTXO'ların birleştirilmesi genellikle düzgün yönetilmediğinde gizlilik kaybına yol açan kötü bir uygulamadır.


Karma UTXO'ları birbirleriyle birleştirme konusunda da dikkatli olmak önemlidir. Karışık UTXO'larınızda önemli anonsetler varsa orta düzeyde konsolidasyonlar düşünülebilir, ancak bu kaçınılmaz olarak coin'lerinizin gizliliğini azaltacaktır. Konsolidasyonların ne çok büyük olduğundan ne de yetersiz sayıda remiksten sonra yapıldığından emin olun, çünkü bu, CoinJoin döngülerinden önce ve sonra UTXO'larınız arasında çıkarılabilir bağlantılar kurma riski taşır. Bu manipülasyonlar hakkında şüphe duyulması halinde, en iyi uygulama karışım sonrası UTXO'ları birleştirmemek ve her seferinde yeni bir boş Address oluşturarak bunları tek tek Hardware Wallet'inize aktarmaktır. Yine, alınan her UTXO'i uygun şekilde etiketlemeyi unutmayın.

Ayrıca, postmix UTXO'larınızı yaygın olmayan komut dosyaları kullanarak bir Wallet'e aktarmamanız tavsiye edilir. Örneğin, `P2WSH` komut dosyalarını kullanarak bir Multisig Wallet'den Whirlpool'a girerseniz, orijinal olarak aynı Wallet türüne sahip diğer kullanıcılarla karıştırılma şansınız çok azdır. Postmix'inizi bu aynı Multisig Wallet'e geri çekerseniz, karışık bitcoinlerinizin gizlilik seviyesi büyük ölçüde azalacaktır. Komut dosyalarının ötesinde, sizi kandırabilecek başka birçok Wallet parmak izi vardır.

Tüm Bitcoin işlemlerinde olduğu gibi, alıcı adreslerinin tekrar kullanılmaması da önemlidir. Her yeni işlem yeni, boş bir Address üzerinden alınmalıdır.


En basit ve en güvenli çözüm, karışık UTXO'larınızı **postmix** hesaplarında dinlendirmek, yeniden karıştırmalarına izin vermek ve yalnızca harcamak için dokunmaktır. Samourai ve Sparrow cüzdanları, zincir analiziyle ilgili tüm bu risklere karşı ek korumalara sahiptir. Bu korumalar hata yapmaktan kaçınmanıza yardımcı olur.


## Doxxic değişim nasıl yönetilir?

Daha sonra, CoinJoin havuzuna giremeyen değişiklik olan doxxic değişikliği yönetirken dikkatli olmanız gerekir. Whirlpool kullanımından kaynaklanan bu toksik UTXO'lar, sizinle CoinJoin kullanımı arasında bir bağlantı kurduklarından gizliliğiniz için risk oluştururlar. Bu nedenle, bunları dikkatli bir şekilde ele almak ve diğer UTXO'larla, özellikle de karışık UTXO'larla birleştirmemek zorunludur. İşte bunları kullanmak için göz önünde bulundurmanız gereken farklı stratejiler:


- Daha küçük havuzlarda karıştırın:** Toksik UTXO'niz tek başına daha küçük bir havuza girecek kadar önemliyse, karıştırmayı düşünün. Bu genellikle en iyi seçenektir. Ancak, bir havuza erişmek için birkaç toksik UTXO'yu birleştirmemek çok önemlidir, çünkü bu farklı girişlerinizi birbirine bağlayabilir;
- Bunları "harcanamaz" olarak işaretleyin:** Başka bir yaklaşım da bunları artık kullanmamak, özel hesaplarında "harcanamaz" olarak işaretlemek ve sadece HODL yapmaktır. Bu, onları yanlışlıkla harcamamanızı sağlar. Bitcoin'in değeri artarsa, toksik UTXO'larınıza daha uygun yeni havuzlar ortaya çıkabilir;
- Bağış yapın:** Bitcoin ve ilgili yazılımları üzerinde çalışan geliştiricilere mütevazı da olsa bağış yapmayı düşünün. BTC kabul eden kuruluşlara da bağışta bulunabilirsiniz. Toksik UTXO'larınızı yönetmek çok karmaşık görünüyorsa, bağış yaparak onlardan kurtulabilirsiniz;
- Hediye Kartları Satın Alın:** [Bitrefill] (https://www.bitrefill.com/) gibi platformlar, çeşitli satıcılarda kullanılabilecek hediye kartları için Exchange bitcoinleri almanıza olanak tanır. Bu, toksik UTXO'larınızı ilgili değeri kaybetmeden elden çıkarmanın bir yolu olabilir.
- Onları Monero üzerinde konsolide edin:** Samourai Wallet artık BTC ve XMR arasında bir atomik takas hizmeti sunuyor. Bu, toksik UTXO'ları Bitcoin'ye geri göndermeden önce CIOH aracılığıyla gizliliğinizden ödün vermeden Monero'da konsolide ederek yönetmek için idealdir. Ancak bu seçenek, likidite kısıtlamaları nedeniyle Mining ücretleri ve prim açısından maliyetli olabilir.
- Bunları Lightning Network'e gönderin:** Düşük işlem ücretlerinden yararlanmak için bu UTXO'ları Lightning Network'e aktarmak ilginç olabilecek bir seçenektir. Ancak, bu yöntem Lightning kullanımınıza bağlı olarak belirli bilgileri açığa çıkarabilir ve bu nedenle dikkatli bir şekilde uygulanmalıdır.


Bu farklı tekniklerin uygulanmasına ilişkin ayrıntılı eğitimler yakında PlanB Network'te sunulacaktır.


**Ek Kaynaklar:**

[Sparrow wallet Video Tutorial](https://planb.network/tutorials/Wallet/desktop/Sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet Video Tutorial](https://planb.network/tutorials/Wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Dokümantasyonu - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Twitter Thread on CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [CoinJoins Blog Yazısı] (https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).