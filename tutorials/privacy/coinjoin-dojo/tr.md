---
name: CoinJoin - Dojo
description: Kendi Dojo'nuzla bir CoinJoin nasıl gerçekleştirilir?
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'ün kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Whirlpool aracı artık kendi Dojo'su olan veya Sparrow wallet kullanan kişiler için bile çalışmamaktadır. Bununla birlikte, bu aracın önümüzdeki haftalarda eski haline getirilmesi veya farklı bir şekilde yeniden başlatılması mümkün olmaya devam ediyor. Ayrıca, bu makalenin teorik kısmı, genel olarak (sadece Whirlpool değil) coinjoins'in ilke ve hedeflerini anlamak ve Whirlpool modelinin etkinliğini anlamak için geçerliliğini korumaktadır.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

Bu eğitimde, CoinJoin'nın ne olduğunu ve Samourai Wallet yazılımını ve Whirlpool uygulamasını kullanarak kendi Dojo'nuzu kullanarak nasıl gerçekleştireceğinizi öğreneceksiniz. Bana göre, bu yöntem şu anda bitcoinlerinizi karıştırmak için en iyisidir.


## Bitcoin üzerindeki CoinJoin nedir?

**CoinJoin, Blockchain** üzerindeki bitcoinlerin izlenebilirliğini kıran bir tekniktir. Aynı adı taşıyan belirli bir yapıya sahip işbirlikçi bir işleme dayanır: CoinJoin işlemi.


Coinjoins, harici gözlemciler için zincir analizini zorlaştırarak Bitcoin kullanıcılarının gizliliğini artırır. Yapıları, farklı kullanıcılardan gelen birden fazla coinin tek bir işlemde birleştirilmesine olanak tanıyarak izleri bulanıklaştırır ve giriş ve çıkış adresleri arasındaki bağlantıların belirlenmesini zorlaştırır.


CoinJoin'ün prensibi işbirlikçi bir yaklaşıma dayanmaktadır: bitcoinlerini karıştırmak isteyen birkaç kullanıcı aynı işlemin girdileri olarak aynı miktarları yatırmaktadır. Bu tutarlar daha sonra her kullanıcıya eşit değerde çıktılar olarak yeniden dağıtılır. İşlemin sonunda, belirli bir çıktıyı girdideki bilinen bir kullanıcıyla ilişkilendirmek imkansız hale gelir. Girdiler ve çıktılar arasında doğrudan bir bağlantı yoktur, bu da kullanıcılar ve UTXO'leri arasındaki ilişkiyi ve her bir Coin'ün geçmişini bozar.

![coinjoin](assets/notext/1.webp)


Bir CoinJoin işlemi örneği (benden değil): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Her kullanıcının fonları üzerinde her zaman kontrol sahibi olmasını sağlarken bir CoinJoin gerçekleştirmek için süreç, işlemin bir koordinatör tarafından oluşturulması ve daha sonra katılımcılara iletilmesiyle başlar. Her kullanıcı daha sonra işlemin kendisine uygun olduğunu doğruladıktan sonra imzalar. Toplanan tüm imzalar en sonunda işleme entegre edilir. Eğer bir kullanıcı ya da koordinatör tarafından CoinJoin işleminin çıktılarında bir değişiklik yapılarak fonların yönü değiştirilmeye çalışılırsa, imzaların geçersiz olduğu kanıtlanacak ve bu da işlemin düğümler tarafından reddedilmesine yol açacaktır.


CoinJoin'nin Whirlpool, JoinMarket veya Wabisabi gibi, her biri katılımcılar arasındaki koordinasyonu yönetmeyi ve CoinJoin işlemlerinin verimliliğini artırmayı amaçlayan çeşitli uygulamaları vardır.

Bu eğitimde, Bitcoin üzerinde coinjoins gerçekleştirmek için en verimli çözüm olduğunu düşündüğüm **Whirlpool** uygulamasını inceleyeceğiz. Çeşitli cüzdanlarda mevcut olmasına rağmen, bu eğitimde, Dojo olmadan Samourai Wallet mobil uygulamasıyla kullanımını özel olarak inceleyeceğiz.


## Neden Bitcoin'te eş birleştirmeler yapalım?

Herhangi bir eşler arası ödeme sistemindeki ilk sorunlardan biri çifte harcamadır: kötü niyetli kişilerin aynı para birimini birden fazla kez harcaması, hakemlik yapacak merkezi bir otoriteye başvurmadan nasıl önlenir?


Satoshi Nakamoto, herhangi bir merkezi otoriteden bağımsız olarak çalışan eşler arası bir elektronik ödeme sistemi olan Bitcoin protokolü aracılığıyla bu ikileme bir çözüm sundu. Beyaz kitabında, çifte harcamanın olmadığını belgelemenin tek yolunun ödeme sistemi içindeki tüm işlemlerin görünürlüğünü sağlamak olduğunu vurguluyor.


Her katılımcının işlemlerden haberdar olmasını sağlamak için bunların kamuya açıklanması gerekir. Bu nedenle, Bitcoin'nin çalışması, herhangi bir düğüm operatörünün elektronik imza zincirlerinin tamamını ve bir Miner tarafından oluşturulmasından itibaren her bir Coin'un geçmişini doğrulamasına olanak tanıyan şeffaf ve dağıtılmış bir altyapıya dayanır.


Bitcoin'in Blockchain'un şeffaf ve dağıtık yapısı, ağın herhangi bir kullanıcısının diğer tüm katılımcıların işlemlerini takip ve analiz edebileceği anlamına gelir. Sonuç olarak, işlem düzeyinde anonimlik mümkün değildir. Bununla birlikte, anonimlik bireysel kimlik düzeyinde korunur. Her hesabın kişisel bir kimlikle bağlantılı olduğu geleneksel bankacılık sisteminin aksine, Bitcoin'de fonlar kriptografik anahtar çiftleriyle ilişkilendirilir ve böylece kullanıcılara kriptografik tanımlayıcıların arkasında bir tür takma ad sunar.


Dolayısıyla, harici gözlemciler belirli UTXO'ları tanımlanmış kullanıcılarla ilişkilendirmeyi başardığında Bitcoin'teki gizlilik tehlikeye girer. Bu ilişki kurulduktan sonra, işlemlerini izlemek ve bitcoinlerinin geçmişini analiz etmek mümkün hale gelir. CoinJoin tam olarak UTXO'ların izlenebilirliğini kırmak için geliştirilmiş bir tekniktir ve böylece Bitcoin kullanıcılarına işlem düzeyinde belirli bir Layer gizliliği sunar.


## Whirlpool nasıl çalışır?

Whirlpool, tüm girdiler ve tüm çıktılar arasında kesinlikle hiçbir teknik bağlantının mümkün olmamasını sağlayan "_ZeroLink_" işlemlerini kullanarak diğer CoinJoin yöntemlerinden ayrılır. Bu mükemmel karışım, her katılımcının aynı miktarda girdi (Mining ücretleri hariç) sağladığı ve böylece tamamen eşit miktarlarda çıktılar ürettiği bir yapı aracılığıyla elde edilir.

Girdilere yönelik bu kısıtlayıcı yaklaşım Whirlpool CoinJoin işlemlerine benzersiz bir özellik kazandırmaktadır: girdiler ve çıktılar arasında deterministik bağlantıların tamamen yokluğu. Başka bir deyişle, her bir çıktının herhangi bir katılımcıya atfedilme olasılığı, işlemdeki diğer tüm çıktılara kıyasla eşittir.

Başlangıçta, her bir Whirlpool CoinJoin'deki katılımcı sayısı 2 yeni katılımcı ve 3 remiksçi olmak üzere 5 ile sınırlıydı (bu kavramları daha sonra açıklayacağız). Ancak, 2023 yılında gözlemlenen On-Chain işlem ücretlerindeki artış, Samourai ekiplerini maliyetleri azaltırken gizliliği artırmak için modellerini yeniden düşünmeye sevk etti. Bu nedenle, ücretlerin piyasa durumunu ve katılımcı sayısını dikkate alarak, koordinatör artık 6, 7 veya 8 katılımcıyı içeren coinjoins düzenleyebilir. Bu geliştirilmiş oturumlar "_Surge Cycles_" olarak adlandırılır. Kurulumdan bağımsız olarak, Whirlpool coinjoin'lerinde her zaman yalnızca 2 yeni katılımcının olduğunu belirtmek önemlidir.


Dolayısıyla, Whirlpool işlemleri aynı sayıda girdi ve çıktı ile karakterize edilir:


- 5 giriş ve 5 çıkış;

![coinjoin](assets/notext/2.webp)


- 6 giriş ve 6 çıkış;

![coinjoin](assets/notext/3.webp)


- 7 giriş ve 7 çıkış;

![coinjoin](assets/notext/4.webp)


- 8 giriş ve 8 çıkış.

![coinjoin](assets/notext/5.webp)

Whirlpool tarafından önerilen model bu nedenle küçük CoinJoin işlemlerine dayanmaktadır. Anonsetlerin sağlamlığının tek bir döngüdeki katılımcıların hacmine dayandığı Wasabi ve JoinMarket'in aksine, Whirlpool birden fazla küçük boyutlu döngünün zincirlemesine dayanmaktadır.


Bu modelde, kullanıcı yalnızca havuza ilk girişinde ücret öder ve böylece ek ücret ödemeden çok sayıda remikse katılabilir. Remiksçiler için Mining ücretlerini karşılayanlar yeni giriş yapanlardır.


Bir Coin'un geçmişte karşılaştığı eşleriyle birlikte katıldığı her ek CoinJoin ile anonsetler katlanarak büyüyecektir. Bu nedenle amaç, her oluşumda her bir karışık Coin ile ilişkili anonsetlerin yoğunluğunu artırmaya katkıda bulunan bu ücretsiz remikslerden yararlanmaktır.


Whirlpool iki önemli gereksinim dikkate alınarak tasarlanmıştır:


- Samourai Wallet'in öncelikle bir akıllı telefon uygulaması olduğu göz önüne alındığında, mobil cihazlarda uygulamanın erişilebilirliği;
- Yeniden karıştırma döngülerinin hızı, anonsetlerde önemli bir artışı teşvik eder.

Bu zorunluluklar Samourai Wallet'ün geliştiricilerinin Whirlpool'nin tasarımındaki tercihlerine rehberlik etmiş ve onları döngü başına katılımcı sayısını sınırlamaya yöneltmiştir. Çok az sayıda katılımcı CoinJoin'ün verimliliğini tehlikeye atarak her döngüde üretilen anonsları büyük ölçüde azaltırken, çok fazla katılımcı mobil uygulamalarda yönetim sorunları yaratacak ve döngülerin akışını engelleyecekti.

**Sonuç olarak, anonslar birkaç CoinJoin döngüsünün birikimiyle elde edildiğinden, Whirlpool'te CoinJoin başına yüksek sayıda katılımcı olmasına gerek yoktur.**


[-> Whirlpool anonsları hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Havuzlar ve CoinJoin ücretleri

Bu çoklu döngülerin karma sikkelerin anonsetlerini etkili bir şekilde artırması için, kullanılan UTXO miktarlarını kısıtlamak üzere belirli bir çerçeve oluşturulmalıdır. Whirlpool böylece farklı havuzları tanımlar.


Bir havuz, CoinJoin sürecini optimize etmek için kullanılacak UTXO miktarı üzerinde anlaşan ve birlikte karıştırmak isteyen bir grup kullanıcıyı temsil eder. Her havuz, UTXO için kullanıcının katılmak için uyması gereken sabit bir miktar belirler. Bu nedenle, Whirlpool ile coinjoins gerçekleştirmek için bir havuz seçmeniz gerekir. Şu anda mevcut olan havuzlar aşağıdaki gibidir:


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

Daha önce de belirtildiği gibi, bir UTXO bir CoinJoin'a entegre edilmeye hazır olduğunda bir havuza ait kabul edilir. Ancak bu, kullanıcının UTXO'in mülkiyetini kaybettiği anlamına gelmez. **Farklı karıştırma döngüleri boyunca anahtarlarınızın ve dolayısıyla bitcoinlerinizin tam kontrolünü elinizde tutarsınız.** CoinJoin tekniğini diğer merkezi karıştırma tekniklerinden ayıran da budur.


Bir CoinJoin havuzuna girmek için Mining ücretlerinin yanı sıra hizmet ücretlerinin de ödenmesi gerekmektedir. Hizmet ücretleri her havuz için sabittir ve Whirlpool'in geliştirilmesi ve bakımından sorumlu ekiplere tazminat ödenmesini amaçlamaktadır.

Whirlpool'ü kullanmak için hizmet ücretleri havuza girdikten sonra yalnızca bir kez ödenmelidir. Bu adımdan sonra, herhangi bir ek ücret ödemeden sınırsız sayıda remikse katılma fırsatına sahip olursunuz. İşte her havuz için geçerli sabit ücretler:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Bu ücretler, CoinJoin'e koyduğunuz miktardan bağımsız olarak, esasen seçilen havuz için bir giriş bileti işlevi görür. Dolayısıyla, 0.01 havuzuna ister tam olarak 0.01 BTC ile ister 0.5 BTC ile katılın, ücretler mutlak değer olarak aynı kalacaktır.


Bu nedenle, eş birleşimlere geçmeden önce kullanıcı 2 strateji arasında seçim yapabilir:


- Karşılığında birkaç küçük UTXO alacaklarını bilerek hizmet ücretlerini en aza indirmek için daha küçük bir havuzu tercih edin;
- Ya da daha büyük bir havuzu tercih ederek, daha az sayıda daha büyük değerli UTXO'larla sonuçlanmak için daha yüksek ücretler ödemeyi kabul eder.


Özellikle Ortak-Giriş-Ownership Sezgisel (CIOH) nedeniyle elde edilen gizliliği tehlikeye atabileceğinden, genellikle CoinJoin döngülerinden sonra birkaç karışık UTXO'nun birleştirilmemesi tavsiye edilir. Bu nedenle, çıkışta çok sayıda küçük değerli UTXO'ya sahip olmaktan kaçınmak için daha fazla ödeme yapmak anlamına gelse bile daha büyük bir havuz seçmek akıllıca olabilir. Kullanıcı tercih ettiği havuzu seçmek için bu ödünleşimleri tartmalıdır.


Hizmet ücretlerine ek olarak, herhangi bir Bitcoin işlemine özgü Mining ücretleri de dikkate alınmalıdır. Bir Whirlpool kullanıcısı olarak, hazırlık işlemi (`Tx0`) için Mining ücretlerinin yanı sıra ilk CoinJoin ücretlerini de ödemeniz gerekecektir. Whirlpool'in yeni katılımcıların ödemelerine dayanan modeli sayesinde sonraki tüm remiksler ücretsiz olacaktır.


Gerçekten de, her bir Whirlpool CoinJoin'te, girdiler arasında iki kullanıcı yeni girenlerdir. Diğer girdiler remiksçilerden gelmektedir. Sonuç olarak, işlemdeki tüm katılımcıların Mining ücretleri, daha sonra ücretsiz remikslerden de yararlanacak olan bu iki yeni katılımcı tarafından karşılanır:

![coinjoin](assets/en/6.webp)

Bu ücret sistemi sayesinde Whirlpool kendisini diğer CoinJoin hizmetlerinden gerçekten farklılaştırmaktadır çünkü UTXO'ların anonimleri kullanıcı tarafından ödenen fiyatla orantılı değildir. Böylece, sadece havuza giriş ücreti ve iki işlem için (`Tx0` ve ilk karışım) Mining ücreti ödeyerek oldukça yüksek anonimlik seviyelerine ulaşmak mümkündür.

Kullanıcının, aşağıdaki eğitimde tartışacağımız `mix to' seçeneğini seçmediği sürece, çoklu coin birleşmelerini tamamladıktan sonra UTXO'larını havuzdan çekmek için Mining ücretlerini de karşılaması gerekeceğini unutmamak önemlidir.


### Whirlpool tarafından kullanılan HD Wallet hesapları

Whirlpool aracılığıyla bir CoinJoin gerçekleştirmek için Wallet'ün birkaç farklı hesabı generate yapması gerekir. Bir HD (*Hiyerarşik Deterministik*) Wallet bağlamında bir hesap, diğerlerinden tamamen izole edilmiş bir bölüm oluşturur, bu ayrım Wallet'ün hiyerarşisinin üçüncü derinlik seviyesinde, yani `xpub' seviyesinde gerçekleşir.


Bir HD Wallet teorik olarak en fazla `2^(32/2)` farklı hesap türetebilir. Tüm Bitcoin cüzdanlarında varsayılan olarak kullanılan ilk hesap `0'` indeksine karşılık gelir.


Samourai veya Sparrow gibi Whirlpool'ye uyarlanmış cüzdanlar için, CoinJoin sürecinin ihtiyaçlarını karşılamak üzere 4 hesap kullanılır:


- 0'` indeksi ile tanımlanan **depozito** hesabı;
- 2 147 483 644'` endeksi ile tanımlanan **kötü banka** (veya doxxic change) hesabı;
- 2 147 483 645'` endeksi ile tanımlanan **premix** hesabı;
- Postmix** hesabı, `2 147 483 646'` endeksi ile tanımlanmıştır.


Bu hesapların her biri CoinJoin içerisinde belirli bir işlevi yerine getirmektedir.


Tüm bu hesaplar tek bir seed'ye bağlıdır, bu da kullanıcının kurtarma cümlesini ve gerekirse passphrase'ini kullanarak tüm bitcoinlerine erişimi geri kazanmasına olanak tanır. Ancak, bu kurtarma işlemi sırasında kullanılan farklı hesap dizinlerinin yazılıma belirtilmesi gerekmektedir.


Şimdi bu hesaplar içinde bir Whirlpool CoinJoin'ün farklı aşamalarına bakalım.


### Whirlpool'teki eş birleşmelerin farklı aşamaları

**1. Aşama: Tx0**

Herhangi bir Whirlpool CoinJoin'nin başlangıç noktası **deposit** hesabıdır. Bu hesap, yeni bir Bitcoin Wallet oluşturduğunuzda otomatik olarak kullandığınız hesaptır. Bu hesaba karıştırılmak istenen bitcoinler yatırılmalıdır.

Tx0`, Whirlpool karıştırma işlemindeki ilk adımı temsil eder. Karışımın homojenliğini sağlamak için UTXO'yi seçilen havuzun miktarına karşılık gelen birimlere bölerek CoinJoin için hazırlamayı ve eşitlemeyi amaçlar. Eşitlenen UTXO daha sonra **premix** hesabına gönderilir. Havuza giremeyen fark ise özel bir hesaba ayrılır: **kötü banka** (veya "doxxic change").

Bu ilk işlem `Tx0` aynı zamanda karışım koordinatörüne ödenmesi gereken hizmet ücretlerinin ödenmesine de hizmet eder. Sonraki adımların aksine, bu işlem işbirliğine dayalı değildir; bu nedenle kullanıcı tüm Mining ücretlerini üstlenmelidir:

![coinjoin](assets/en/7.webp)


Bu `Tx0` işlemi örneğinde, **mevduat** hesabımızdan gelen `372.000 Sats` girişi, aşağıdaki gibi dağıtılan birkaç UTXO çıktısına bölünür:


- 100.000 Sats`lık havuza girişe karşılık gelen hizmet ücretleri için koordinatöre yönelik 5.000 Sats`lık bir tutar;
- Karışım için üç UTXO hazırlandı, **premix** hesabımıza yönlendirildi ve koordinatöre kaydedildi. Bu UTXO'ların her biri, gelecekteki ilk karışımları için Mining ücretlerini karşılamak üzere `108.000 Sats` olarak eşitlenmiştir;
- Çok küçük olduğu için havuza giremeyen fazlalık, zehirli değişim olarak kabul edilir. Kendi özel hesabına gönderilir. Burada bu değişim `40,000 Sats` tutarındadır;
- Son olarak, bir çıktı oluşturmayan ancak `Tx0`ı onaylamak için gerekli olan Mining ücretleri olan `3.000 Sats` vardır.


Örneğin, işte gerçek bir Whirlpool Tx0 (benden değil): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**2. Adım: Doxxic değişim**

Havuza entegre edilemeyen ve burada `40.000 Sats`ya denk gelen fazlalık, Wallet'teki diğer UTXO'den kesin bir şekilde ayrılmasını sağlamak için "doxxic change" olarak da adlandırılan **bad bank** hesabına yönlendirilir.


Bu UTXO kullanıcının gizliliği için tehlikelidir çünkü sadece geçmişine ve dolayısıyla muhtemelen sahibinin kimliğine bağlı olmakla kalmaz, aynı zamanda bir CoinJoin gerçekleştirmiş bir kullanıcıya ait olduğu da belirtilir.

Bu UTXO karışık çıktılarla birleştirilirse, özellikle Ortak Girdi-Ownership-Heuristic (CIOH) nedeniyle CoinJoin döngüleri sırasında kazanılan tüm gizliliği kaybedeceklerdir. Diğer doxxic değişikliklerle birleştirilirse, bu CoinJoin döngülerinin farklı girdilerini birbirine bağlayacağından kullanıcı gizliliğini kaybetme riskiyle karşı karşıya kalır. Bu nedenle dikkatle ele alınmalıdır. Bu zehirli UTXO'yi yönetmenin yolu bu makalenin son bölümünde ayrıntılı olarak açıklanacaktır ve gelecekteki eğitimler bu yöntemleri PlanB Network'te daha ayrıntılı olarak ele alacaktır.


**3. Adım: İlk Karışım**

Tx0` tamamlandıktan sonra, eşitlenmiş UTXO'lar Wallet'ümüzün **premix** hesabına gönderilir ve "ilk karışım" olarak da adlandırılan ilk CoinJoin döngüsüne dahil edilmeye hazır hale gelir. Örneğimizde olduğu gibi, `Tx0` karıştırma amaçlı birkaç UTXO üretirse, bunların her biri ayrı bir ilk CoinJoin'e entegre edilecektir.


Bu ilk karışımların sonunda, **premix** hesabı boş olacak ve bu ilk CoinJoin için Mining ücretlerini ödemiş olan coinlerimiz tam olarak seçilen havuz tarafından tanımlanan miktara ayarlanacaktır. Örneğimizde, `108 000 Sats`lik ilk UTXO'larımız tam olarak `100 000 Sats`ye düşürülmüş olacaktır.

![coinjoin](assets/en/8.webp)

**4. Adım: Remiksler**

İlk miksten sonra UTXO'lar **postmix** hesabına aktarılır. Bu hesap halihazırda karıştırılmış UTXO'ları ve yeniden karıştırılmayı bekleyenleri toplar. Whirlpool istemcisi aktif olduğunda, **postmix** hesabında bulunan UTXO'lar otomatik olarak remiks için hazır olur ve bu yeni döngülere katılmak üzere rastgele seçilir.


Bir hatırlatma olarak, remiksler %100 ücretsizdir: ek hizmet ücreti veya Mining ücreti gerekmez. UTXO'ları **postmix** hesabında tutmak, böylece değerlerini sağlam tutar ve aynı zamanda anonsetlerini iyileştirir. Bu nedenle, bu coinlerin birden fazla CoinJoin döngüsüne katılmasına izin vermek önemlidir. Bunun size kesinlikle hiçbir maliyeti yoktur ve anonimlik seviyelerini artırır.


Karışık UTXO'ları harcamaya karar verdiğinizde, bunu doğrudan bu **postmix** hesabından yapabilirsiniz. Ücretsiz remikslerden faydalanmak ve gizliliklerini azaltabilecek Whirlpool devresinden ayrılmalarını önlemek için karışık UTXO'ları bu hesapta tutmanız tavsiye edilir.


Bir sonraki eğitimde göreceğimiz gibi, belirli sayıda coin birleşiminden sonra karışık coinlerinizi otomatik olarak Cold Wallet gibi başka bir Wallet'ye gönderme imkanı sunan `mix to' seçeneği de vardır.

Teoriyi ele aldıktan sonra, Whirlpool CLI ve kendi Dojo'nuzdaki GUI ile senkronize edilmiş Samourai Wallet Android uygulaması aracılığıyla Whirlpool'ü kullanma üzerine bir eğitimle pratiğe dalalım!

## Eğitim: Kendi Dojo'nuz ile CoinJoin Whirlpool

Whirlpool'u kullanmak için birçok seçenek var. Burada tanıtmak istediğim Samourai Wallet seçeneği, Android'de açık kaynaklı bir Bitcoin Wallet yönetim uygulaması, ancak bu sefer **kendi Dojo'nuzla**.


Kendi Dojo'nuzu kullanarak Samourai Wallet aracılığıyla coinjoins gerçekleştirmek, bence bugüne kadar Bitcoin'te coinjoins gerçekleştirmek için en etkili stratejidir. Bu yaklaşım kurulum açısından bir miktar başlangıç yatırımı gerektirmektedir, ancak bir kez uygulandığında, Samourai uygulamanızı her zaman aktif tutmanıza gerek kalmadan, haftanın 7 günü, günün 24 saati bitcoinlerinizi sürekli olarak karıştırma ve yeniden karıştırma imkanı sunar. Gerçekten de, bir Bitcoin düğümü üzerinde çalışan Whirlpool CLI sayesinde, coin birleşmelerine katılmaya her zaman hazırsınız. Samourai uygulaması daha sonra size karışık fonlarınızı istediğiniz zaman, nerede olursanız olun, doğrudan akıllı telefonunuzdan harcama fırsatı verir. Dahası, bu yöntem sizi Samourai ekipleri tarafından yönetilen sunuculara asla bağlamama avantajına sahiptir, böylece `xpub`ınızı herhangi bir dış maruziyetten korur.


Bu nedenle bu teknik maksimum gizlilik ve en yüksek kalitede CoinJoin döngüleri arayanlar için idealdir. Bununla birlikte, elinizin altında bir Bitcoin düğümü olmasını gerektirir ve daha sonra göreceğimiz gibi, bazı kurulumlar gerektirir. Bu nedenle orta ve ileri düzey kullanıcılar için daha uygundur. Yeni başlayanlar için, CoinJoin ile Sparrow wallet veya Samourai Wallet'dan (Dojo olmadan) nasıl yapılacağını gösteren bu iki diğer öğretici aracılığıyla tanışmanızı öneririm:


- [Sparrow wallet CoinJoin tutorial](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### Kurulumu Anlama

Başlamak için bir Dojo'ya ihtiyacınız olacak! Dojo, Samourai ekipleri tarafından geliştirilen Bitcoin core tabanlı bir Bitcoin düğüm uygulamasıdır.


Kendi Dojo'nuzu çalıştırmak için, bir Dojo düğümünü bağımsız olarak kurma veya başka bir "kutu içinde düğüm" Bitcoin düğüm çözümünün üzerine Dojo'dan yararlanma seçeneğiniz vardır. Şu anda mevcut seçenekler şunlardır:


- [RoninDojo](https://ronindojo.io/), bir kurulum asistanı ve bir yönetim asistanı da dahil olmak üzere ek araçlarla geliştirilmiş bir Dojo'dur. RoninDojo'yu kurma ve kullanma prosedürünü bu diğer eğitimde detaylandırıyorum: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- "Samourai Server" uygulaması ile [Umbrel](https://umbrel.com/);
- "Dojo" uygulaması ile [MyNode](https://mynodebtc.com/);
- "Dojo" uygulaması ile [Nodl](https://www.nodl.eu/);
- "Samourai" uygulaması ile [Citadel](https://runcitadel.space/).

![coinjoin](assets/notext/9.webp)

Kurulumumuzda, üç farklı arayüz ile etkileşime gireceğiz:


- Samourai Wallet**, coinjoins'e adanmış Bitcoin Wallet'ümüze ev sahipliği yapacak. Android'de ücretsiz olarak kullanılabilen bu FOSS uygulaması, özellikle postmix'inizi akıllı telefonunuzdan geçirmek için miksaj Wallet'ünüzü kontrol etmenizi sağlar;
- Whirlpool CLI** (_Command Line Interface_), Dojo'yu barındıran düğüm üzerinde çalışacaktır. Bu yazılım Samourai Wallet'inizin anahtarlarına erişebilecektir. Koordinatör ile iletişim kurmaktan ve coinjoları sürekli olarak yönetmekten sorumludur. Samourai Wallet'inizin düğümünüzdeki bir kopyası olarak hareket eder ve her an coinjoin'lere katılmaya hazırdır;
- Whirlpool GUI** (_Graphical User Interface_), Whirlpool CLI'un faaliyetlerini izlemek ve uzaktan karıştırmayı başlatmak için kullanacağımız grafiksel kullanıcı Interface. Whirlpool GUI, Whirlpool CLI tarafından yürütülen işlemlerin görsel bir temsilini sağlar. Bu yazılım Dojo'dan ayrı bir bilgisayara yüklenmelidir. Umbrel, MyNode, Nodl ve Citadel kullanıcıları için Whirlpool GUI zorunludur. Bununla birlikte, RoninDojo ile Whirlpool GUI Interface, `Whirlpool` uygulaması aracılığıyla düğümünüzün web Interface'sine zaten entegre edilmiştir. Bu nedenle, ayrı bir bilgisayara yüklemeniz gerekmeyecektir.


Bana göre, RoninDojo'yu kullanmak bir Dojo ile coinjoins gerçekleştirmek için en iyi çözümü temsil ediyor. Bu node-in-box yazılımı Samourai ekipleriyle doğrudan ortaklık içinde olduğundan, RoninDojo bunu yapmak için çok daha optimize edilmiştir. Dahası, Whirlpool GUI'nin web Interface'e entegrasyonu kurulum sürecini önemli ölçüde basitleştiriyor. Bu eğitimde, Dojo'yu entegre eden diğer çözümlerle (Umbrel, Nodl, MyNode ve Citadel) nasıl yapılacağını açıklayacağım.


### Dojonuzu Hazırlama

Başlamak için Dojo'yu yüklemeniz ve uzaktan bağlanmanızı sağlayacak QR kodunu veya bağlantıyı edinmeniz gerekecektir. Bu bağlantı `.onion` ile biten bir Tor Address'dir. RoninDojo kullanıyorsanız, bu bilgilere erişmek için `Pairing` menüsüne gitmeniz yeterlidir.

![coinjoin](assets/notext/10.webp)


Samourai Dojo`nun altında, `Şimdi eşleştir` düğmesine tıklayın.


![coinjoin](assets/notext/11.webp)


Bağlantı QR kodunuz ve ilgili bağlantı görüntülenecektir.


![coinjoin](assets/notext/12.webp)


Umbrel kullanıyorsanız, App Store'a gidin ve `Samourai Server` uygulamasını arayın. Bu uygulama `Bitcoin` sekmesinde yer almaktadır.


![coinjoin](assets/notext/13.webp)


Uygulamayı yükleyin.


![coinjoin](assets/notext/14.webp)


Uygulamayı açtıktan sonra, Dojo'nuza bağlanmak için QR koduna erişebileceksiniz.


![coinjoin](assets/notext/15.webp)


MyNode, Citadel veya Nodl gibi başka bir node-in-box yazılımı kullanıyorsanız, süreç Umbrel'inkine benzer. Dojo'nuza bağlanmak için gerekli bilgileri elde etmek üzere Samourai veya Dojo uygulamasını yüklemeniz gerekir.


![coinjoin](assets/notext/16.webp)


### Samourai Wallet'ünüzü hazırlama

Dojo'nuza bağlantı bilgilerini aldıktan sonra, şimdi Wallet'inizi coinjoins için ayarlamanın zamanı geldi. İki senaryo var: Akıllı telefonunuzda henüz bir Samourai Wallet yoksa, işlem basittir, sadece yeni bir tane oluşturun.


Öte yandan, zaten bir Samourai Wallet'nız varsa, uygulamayı yeni bir Dojo ile ilişkilendirmek için yeniden yüklemeniz gerekecektir. Bu adım gereklidir çünkü bir Dojo ile bağlantı yalnızca uygulamanın ilk açılışında kurulabilir. Ancak, telefonunuzda Samourai tarafından otomatik olarak oluşturulan şifreli yedekleme dosyası sayesinde bu prosedür basit ve hızlıdır.


*Samourai'yi hiç kullanmadıysanız, bu ön adımları atlayabilir ve doğrudan uygulamanın kurulumuna geçebilirsiniz.*


Her şeyden önce, Samourai Wallet uygulamanızın güncel olduğundan emin olun. Bunu yapmak için Google Play Store'u kontrol edin veya `Ayarlar > Diğer` bölümündeki uygulamanızın sürümünü Samourai web sitesinde bulunan sürümle karşılaştırın.


![coinjoin](assets/notext/17.webp)


Samourai Wallet kurtarma ifadenizin olduğundan ve okunaklı olduğundan emin olun. Ardından, doğruluğunu onaylamak için `Ayarlar > Sorun Giderme > passphrase/Yedekleme testi` bölümüne giderek BIP39 passphrase'inizi test edin.


![coinjoin](assets/notext/18.webp)

passphrase'ınızı girin, ardından Samourai'nin geçerliliğini onayladığını doğrulayın.

![coinjoin](assets/notext/19.webp)


passphrase'iniz geçersizse veya kurtarma cümleniz yoksa, prosedürü derhal durdurmanız zorunludur! **Bu durumda, fonlarınızı başka bir Wallet'ye aktarmanız ve yeni bir boş Samourai Wallet ile başlamanız tavsiye edilir. Aşağıdaki adımlar yalnızca gerekli tüm yedekleme bilgilerine sahip olduğunuzdan ve passphrase'inizin geçerli olduğundan eminseniz izlenmelidir.


Ardından Wallet'ünüzün şifrelenmiş bir yedeğini oluşturmaya devam edin ve bunu panonuza kopyalayın. Bu işlemi gerçekleştirmek için ekranın sağ üst köşesinde bulunan üç küçük noktaya tıklayın ve ardından `Wallet yedeğini dışa aktar` seçeneğini seçin.


![coinjoin](assets/notext/20.webp)


**Bu adımdan itibaren panonuza başka bir şey kopyalamayın!** Kopyaladığınız yedeği saklamanız kesinlikle çok önemlidir.


Önceki adımları doğru bir şekilde uyguladıysanız, artık Samourai Wallet'ünüzü güvenli bir şekilde silebilirsiniz. Bunu yapmak için şu adrese gidin: `Ayarlar > Wallet > Wallet'ü güvenli bir şekilde sil`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Samourai'yi hiç kullanmadıysanız ve uygulamayı sıfırdan yüklüyorsanız, eğitime bu adımdan devam edebilirsiniz.*


Samourai uygulamanız artık sıfırlanmıştır. Uygulamayı açın ve ilk kez kullanıyormuş gibi kurulum adımlarına devam edin.


![coinjoin](assets/notext/23.webp)


Bir sonraki adımda, Dojo'nuzu yapılandırmak için ayrılmış sayfaya erişeceksiniz. Dojo` seçeneğini seçin, ardından Dojo'nuzun giriş bilgilerini girin. Bunu yapmak için, `Scan QR` tuşuna basarak bilgileri tarama seçeneğiniz vardır.


![coinjoin](assets/notext/24.webp)


*Samourai'nin yeni kullanıcıları için sıfırdan bir Wallet oluşturmak gerekecektir. Yardıma ihtiyacınız olursa, yeni bir Samourai Wallet kurma talimatlarına başvurabilirsiniz [bu eğitimde, özellikle "Software Wallet Oluşturma" bölümünde](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*


Mevcut bir Samourai Wallet'u geri yüklemeye devam ediyorsanız, `Mevcut Wallet'u geri yükle'yi seçin, ardından `Bir Samourai yedek dosyam var'ı seçin.


![coinjoin](assets/notext/25.webp)

Normalde, kurtarma dosyanız her zaman panonuzda olmalıdır. Ardından dosyanızı belirlenen konuma eklemek için `YAZDIR` seçeneğine tıklayın. Şifresini çözmek için, hemen aşağıda bulunan ilgili alana Wallet'inizin BIP39 passphrase'ünü de girmeniz gerekecektir. Bitirmek için `BİTİR` üzerine tıklayın.

![coinjoin](assets/notext/26.webp)


Daha sonra Samourai Wallet'nize yönlendirileceksiniz ve bu sefer kendi Dojo'nuza bağlanacaksınız.


![coinjoin](assets/notext/27.webp)


### Whirlpool GUI'nin Kurulması

Şimdi Whirlpool GUI'yi, yani CoinJoin çevrimlerinizi normal bilgisayarınızdan yönetmenizi sağlayacak grafik kullanıcı Interface'ü kurmanın zamanı geldi. RoninDojo kullanıcıları için bu adım gerekli değildir, çünkü coinjoins yönetimi doğrudan `Apps > Whirlpool` içindeki web Interface üzerinden yapılabilir. Ancak, başka bir Bitcoin "node-in-box" çözümü kullanıyorsanız, bu kuruluma devam etmeniz zorunludur.

![coinjoin](assets/notext/28.webp)

Kişisel bilgisayarınıza gidin ve işletim sisteminize karşılık gelen sürümü seçerek Whirlpool yazılımını resmi Samourai Wallet web sitesinden indirin.


![coinjoin](assets/notext/29.webp)


Whirlpool GUI'yi başlatmadan önce, makinenize JAVA 8 veya daha yüksek bir sürüm yüklemeniz gerekir. Bunun için [OpenJDK](https://adoptium.net/) yükleyebilirsiniz.

![coinjoin](assets/notext/30.webp)

Bilgisayarınızda Tor daemon veya Tor Browser'ın arka planda çalışır durumda olması da gereklidir. Her Whirlpool GUI kullanım oturumundan önce Tor'u başlattığınızdan emin olun. Tor henüz makinenizde kurulu değilse, [resmi proje web sitesinden indirip kurabilirsiniz] (https://www.torproject.org/download/), o zaman arka planda başlattığınızdan emin olun.


![coinjoin](assets/notext/31.webp)


JDK sisteminize yüklendikten ve Tor arka planda başlatıldıktan sonra, Whirlpool GUI'yi başlatabilirsiniz.


![coinjoin](assets/notext/32.webp)


Whirlpool GUI'den `Gelişmiş'e tıklayın: Dojo'nuzda bulunan Whirlpool CLI'nızı bağlamak için `Uzak CLI` seçeneğine tıklayın. Whirlpool CLI'nızın Tor Address'ine ihtiyacınız olacak.


![coinjoin](assets/notext/33.webp)


Tor Address'nizi Umbrel ve diğer "node-in-box" çözümlerinde bulmak için Samourai Server ya da Dojo uygulamasını (kullanılan yazılıma göre adı değişebilir) başlatmanız yeterlidir. Tor Address doğrudan uygulamanın sayfasında görünür olacaktır.

![coinjoin](assets/notext/34.webp)

Whirlpool GUI'de, `CLI Address` alanına daha önce elde ettiğiniz Tor Address'u girin. Http://` önekini koruyun, ancak sonuna `:8899` bağlantı noktasını eklemeyin. Yalnızca Address'u size sağlandığı şekilde yapıştırın.

![coinjoin](assets/notext/35.webp)


Tor Proxy alanına, Tor daemon kullanıyorsanız `socks5://127.0.0.1:9050` veya Tor Browser kullanıyorsanız `socks5://127.0.0.1:9150` girin. Whirlpool GUI aracılığıyla Whirlpool CLI'e ilk kez bağlandığınızda, API anahtarı alanını boş bırakmak mümkündür. Bu ilk bağlantınız değilse, lütfen API anahtarınızı ayrılmış alana girin. Bu anahtar Tor Address ile aynı sayfada bulunabilir.


![coinjoin](assets/notext/36.webp)


Her şeyi doldurduktan sonra `Bağlan` düğmesine tıklayın. Lütfen bekleyin, bağlantı birkaç dakika sürebilir.


![coinjoin](assets/notext/37.webp)


### Samourai Wallet'nızı Whirlpool GUI ile eşleştirme

*RoninDojo kullanıcıları için eğitime buradan devam edebilirsiniz.*


Şimdi daha önce yapılandırdığımız Samourai Wallet'i Whirlpool GUI yazılımı ile veya bu yazılımı kullananlar için doğrudan RoninDojo ile eşleştireceğiz. İster Whirlpool GUI ister RoninDojo kullanıyor olun, Samourai Wallet'inizin eşleştirme bilgilerini yapıştırmanız veya taramanız istenecektir.


![coinjoin](assets/notext/38.webp)


Bu bilgiyi bulmak için Wallet'unuzun ayarlarına gidin.


![coinjoin](assets/notext/39.webp)


İşlemler'e ve ardından Whirlpool GUI ile Eşleştir'e tıklayın.


![coinjoin](assets/notext/40.webp)


Samourai daha sonra bağlantıyı kurmak için size gerekli bilgileri sağlayacaktır. Dikkatli olun, bu veriler hassastır! Doğrudan kopyalayarak ya da QR kodu sembolüne tıkladıktan sonra bilgisayarınızın web kamerasını kullanarak görüntülenen QR kodunu tarayarak bilgisayarınıza aktarabilirsiniz.


![coinjoin](assets/notext/41.webp)


Bu işlemi gerçekleştirdikten sonra, Whirlpool GUI'de `Initialize GUI` seçeneğini seçin. Bu adım biraz zaman alabileceği için lütfen bekleyin.


![coinjoin](assets/notext/42.webp)


İster Whirlpool GUI ister RoninDojo kullanıyor olun, Samourai Wallet'ünüzün passphrase'sini girmeniz istenecektir. Bunu özel alana girin, ardından devam etmek için `Login` düğmesine basın.


![coinjoin](assets/notext/43.webp)


Daha sonra Whirlpool CLI'nın ana sayfasına ulaşacaksınız


![coinjoin](assets/notext/44.webp)


### Whirlpool GUI'den eş birleştirmelerin başlatılması

*RoninDojo kullanıcıları için izlenecek süreç aynıdır. RoninDojo'ya entegre edilmiş Whirlpool uygulaması Interface, masaüstündeki Whirlpool GUI yazılımı ile aynı seçenekleri ve işlevleri sunar. Bu nedenle, bu talimatları aynı şekilde takip edebilirsiniz.*

Artık her şey ayarlandığına göre, bitcoinlerinizi karıştırmaya başlamaya hazırsınız. Bunu yapmak için, karıştırmak istediğiniz bitcoinleri Samourai Wallet'inizin **Deposit** hesabına aktarın. Bu işlem doğrudan Samourai Wallet uygulaması üzerinden veya Whirlpool GUI üzerinden gerçekleştirilebilir. Ana sayfadan, sol üstte bulunan `+ Para Yatırma` düğmesine tıklayın.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI, alıcı bir Address'i generate yapacaktır. Ayrıca her bir CoinJoin havuzuna katılmak için gereken minimum miktarı da gösterecektir. Bu miktar ücret piyasasına bağlı olarak değişir. Gerekli minimum miktardan biraz daha yüksek bir miktar yatırmanız tavsiye edilir, çünkü Mining ücretleri düşmezse, UTXO'niz istediğiniz havuza kabul edilmeyebilir. Bu nedenle, bitcoinlerinizi sağlanan Address'e gönderin. Yeni bir Address almak için `Address`i Yenile` düğmesine tıklamanız yeterlidir.


![coinjoin](assets/notext/46.webp)


Depozito onaylandıktan sonra, Whirlpool GUI'deki **Depozito** hesabında göründüğünü görebileceksiniz.


![coinjoin](assets/notext/47.webp)


CoinJoin döngülerini başlatmak için, karıştırmak istediğiniz UTXO'ları seçin ve `Premix` düğmesine basın. Dikkatli olun: aynı anda birkaç farklı UTXO seçerseniz, bunlar `TX0` hazırlama işlemi sırasında birleştirilecektir. Bu birleştirme, özellikle UTXO'lar farklı kaynaklardan geliyorsa, Ortak Girdi Ownership Sezgiselliği (CIOH) nedeniyle gizliliğin azalmasına neden olabilir.


![coinjoin](assets/notext/48.webp)


Whirlpool yapılandırma sayfası açılır. Girmek istediğiniz havuzu seçebilirsiniz. Ayrıca `TX0` ve ilk coinjoins için ayrılmış Mining ücretlerini de seçin. Bu sayfanın altında, bir özet size doxxic değişim miktarının yanı sıra eşitlenecek ve CoinJoin döngülerine dahil edilecek UTXO'ların miktarını ve sayısını sunacaktır. Bu yapılandırmadan memnunsanız, CoinJoin döngülerini başlatmak için `Premix` düğmesine basın.

![coinjoin](assets/notext/49.webp)


TX0` oluşturulduktan sonra, eşitlenmiş UTXO'larınızı **Premix** hesabında onay için beklerken görebileceksiniz. Madeni paralarınızın haftanın 7 günü, günün 24 saati otomatik olarak yeniden karışmasını sağlamak için, `Ön karışım ve son karışımı otomatik olarak karıştır` seçeneğini etkinleştirmenizi öneririm. Bu özelliği Whirlpool GUI pencerenizin solunda bulunan `Configuration` sekmesinde bulabilirsiniz.

![coinjoin](assets/notext/50.webp)

Coinjoins'i başlattıktan sonra, Whirlpool GUI'den ve Samourai Wallet'den çıkabilirsiniz. Sürekli coinjoin'lere katılabilmek için yalnızca düğümünüzün bağlı kalması gerekir. Bununla birlikte, CoinJoin döngülerinizin ilerleyişini periyodik olarak kontrol etmeniz tavsiye edilir. UTXO'larınızın bir süredir CoinJoin için seçilmediğini fark ederseniz, bu bir hataya işaret ediyor olabilir. Bu durumda, Whirlpool CLI'e gidin ve `Başlat` seçeneğini seçerek coinjoins için uygunluğunuzu yeniden başlatın.


![coinjoin](assets/notext/51.webp)


Karma UTXO'larınız Whirlpool GUI üzerindeki **Postmix** hesabından görülebilir. Ayrıca, bunları Samourai Wallet'inizdeki Whirlpool Interface aracılığıyla doğrudan görüntüleme ve harcama seçeneğiniz de vardır. Bu menüye erişmek için ekranınızın altındaki mavi `+` işaretine tıklayın ve ardından `Whirlpool` öğesini seçin.


![coinjoin](assets/notext/52.webp)


Whirlpool hesapları Samourai Wallet üzerinde mavi renkleriyle kolayca tanımlanabilir. Bu, karışık UTXO'larınızı her yerden ve her zaman doğrudan akıllı telefonunuzdan harcamanıza olanak tanır.


![coinjoin](assets/notext/53.webp)


Otomatik coin birleşmelerinizi takip etmek için Sentinel uygulaması aracılığıyla bir Watch-only wallet kurmanızı da öneririm. Postmix** hesabınızın ZPUB'ını ekleyin ve CoinJoin döngülerinizin ilerleyişini gerçek zamanlı olarak izleyin. Sentinel'in nasıl kullanılacağını anlamak istiyorsanız, PlanB Network'teki bu diğer eğitime başvurmanızı tavsiye ederim: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)