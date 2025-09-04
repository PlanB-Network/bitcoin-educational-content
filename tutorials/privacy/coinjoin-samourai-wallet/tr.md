---
name: CoinJoin - Samourai Wallet
description: Samourai Wallet üzerinde bir CoinJoin nasıl gerçekleştirilir?
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'nın kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, Whirlpool aracı artık kendi Dojo'su olan veya Sparrow wallet kullanan kişiler için bile çalışmamaktadır. Bununla birlikte, bu aracın önümüzdeki haftalarda eski haline getirilmesi veya farklı bir şekilde yeniden başlatılması olasılığı devam etmektedir. Ayrıca, bu makalenin teorik kısmı, genel olarak (sadece Whirlpool değil) coinjoins'in ilke ve hedeflerini anlamak ve Whirlpool modelinin etkinliğini anlamak için geçerliliğini korumaktadır.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> *sokaklar için bir Bitcoin Wallet*

Bu eğitimde, CoinJoin'un ne olduğunu ve Samourai Wallet yazılımını ve Whirlpool uygulamasını kullanarak nasıl gerçekleştirileceğini öğreneceksiniz.


## Bitcoin üzerindeki CoinJoin nedir?

**CoinJoin, Blockchain** üzerindeki bitcoinlerin izlenebilirliğini kıran bir tekniktir. Aynı adı taşıyan belirli bir yapıya sahip işbirlikçi bir işleme dayanır: CoinJoin işlemi.


Coinjoins, harici gözlemciler için zincir analizini zorlaştırarak Bitcoin kullanıcılarının gizliliğini artırır. Yapıları, farklı kullanıcılardan gelen birden fazla coinin tek bir işlemde birleştirilmesine olanak tanıyarak izleri gizler ve giriş ve çıkış adresleri arasındaki bağlantıların belirlenmesini zorlaştırır.


CoinJoin prensibi işbirlikçi bir yaklaşıma dayanır: bitcoinlerini karıştırmak isteyen birkaç kullanıcı aynı işlemin girdileri olarak aynı miktarları yatırır. Bu tutarlar daha sonra her kullanıcıya eşit değerde çıktılar olarak yeniden dağıtılır. İşlemin sonunda, belirli bir çıktıyı girdideki bilinen bir kullanıcıyla ilişkilendirmek imkansız hale gelir. Girdiler ve çıktılar arasında doğrudan bir bağlantı bulunmaz, bu da kullanıcılar ve UTXO'ları arasındaki ilişkiyi ve her bir Coin'in geçmişini bozar.

![coinjoin](assets/notext/1.webp)


Bir CoinJoin işlemi örneği (benden değil): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Her kullanıcının fonları üzerinde her zaman kontrol sahibi olmasını sağlarken bir CoinJoin gerçekleştirmek için süreç, daha sonra katılımcılara ileten bir koordinatör tarafından işlemin oluşturulmasıyla başlar. Her kullanıcı daha sonra işlemin kendisine uygun olduğunu doğruladıktan sonra imzalar. Toplanan tüm imzalar en sonunda işleme entegre edilir. Eğer bir kullanıcı ya da koordinatör tarafından CoinJoin işleminin çıktıları değiştirilerek fonların yönü değiştirilmeye çalışılırsa, imzalar geçersiz olur ve bu da işlemin düğümler tarafından reddedilmesine yol açar.


CoinJoin'ün Whirlpool, JoinMarket veya Wabisabi gibi, her biri katılımcılar arasındaki koordinasyonu yönetmeyi ve CoinJoin işlemlerinin verimliliğini artırmayı amaçlayan çeşitli uygulamaları vardır.

Bu eğitimde, Bitcoin üzerinde coinjoins gerçekleştirmek için en verimli çözüm olduğunu düşündüğüm **Whirlpool** uygulamasını inceleyeceğiz. Birkaç cüzdanda mevcut olmasına rağmen, bu eğitimde, Dojo olmadan Samourai Wallet mobil uygulamasıyla kullanımını özel olarak inceleyeceğiz.


## Neden Bitcoin'de eş birleştirmeler yapılmalı?

Herhangi bir eşler arası ödeme sistemindeki ilk sorunlardan biri çifte harcamadır: kötü niyetli kişilerin aynı para birimini birden fazla kez harcaması, hakemlik yapacak merkezi bir otoriteye başvurmadan nasıl önlenir?


Satoshi Nakamoto, herhangi bir merkezi otoriteden bağımsız olarak çalışan eşler arası bir elektronik ödeme sistemi olan Bitcoin protokolü aracılığıyla bu ikileme bir çözüm sundu. Beyaz kitabında, çifte harcamanın olmadığını belgelemenin tek yolunun ödeme sistemi içindeki tüm işlemlerin görünürlüğünü sağlamak olduğunu vurguluyor.


Her katılımcının işlemlerden haberdar olmasını garanti altına almak için bunların kamuya açıklanması gerekir. Bu nedenle, Bitcoin'in çalışması, herhangi bir düğüm operatörünün elektronik imza zincirlerinin tamamını ve bir Miner tarafından oluşturulmasından itibaren her bir Coin'ün geçmişini doğrulamasına olanak tanıyan şeffaf ve dağıtılmış bir altyapıya dayanır.


Bitcoin'in Blockchain'ün şeffaf ve dağıtık yapısı, herhangi bir ağ kullanıcısının diğer tüm katılımcıların işlemlerini takip ve analiz edebileceği anlamına gelir. Sonuç olarak, işlem düzeyinde anonimlik mümkün değildir. Bununla birlikte, anonimlik bireysel kimlik düzeyinde korunur. Her hesabın kişisel bir kimlikle bağlantılı olduğu geleneksel bankacılık sisteminin aksine, Bitcoin'te fonlar kriptografik anahtar çiftleriyle ilişkilendirilir ve böylece kullanıcılara kriptografik tanımlayıcıların arkasında bir tür takma ad sunar.


Dolayısıyla, harici gözlemciler belirli UTXO'ları tanımlanmış kullanıcılarla ilişkilendirmeyi başardığında Bitcoin'deki gizlilik tehlikeye girer. Bu ilişki kurulduktan sonra, işlemlerini izlemek ve bitcoinlerinin geçmişini analiz etmek mümkün hale gelir. CoinJoin tam olarak UTXO'ların izlenebilirliğini kırmak için geliştirilmiş bir tekniktir ve böylece Bitcoin kullanıcılarına işlem düzeyinde belirli bir Layer gizliliği sunar.


## Whirlpool nasıl çalışır?

Whirlpool, tüm girdiler ve tüm çıktılar arasında kesinlikle hiçbir teknik bağlantının mümkün olmamasını sağlayan "_ZeroLink_" işlemlerini kullanarak diğer CoinJoin yöntemlerinden ayrılır. Bu mükemmel karışım, her katılımcının aynı miktarda girdiye katkıda bulunduğu (Mining ücretleri hariç) ve böylece tamamen eşit miktarlarda çıktılar ürettiği bir yapı ile elde edilir.

Girdilere yönelik bu kısıtlayıcı yaklaşım Whirlpool CoinJoin işlemlerine benzersiz bir özellik kazandırmaktadır: girdiler ve çıktılar arasında deterministik bağlantıların tamamen yokluğu. Başka bir deyişle, her bir çıktının herhangi bir katılımcıya atfedilme olasılığı, işlemdeki diğer tüm çıktılara kıyasla eşittir.

Başlangıçta, her bir Whirlpool CoinJoin'daki katılımcı sayısı 2 yeni katılımcı ve 3 remiksçi olmak üzere 5 ile sınırlıydı (bu kavramları daha sonra açıklayacağız). Ancak, 2023 yılında gözlemlenen On-Chain işlem ücretlerindeki artış, Samourai ekiplerini maliyetleri azaltırken gizliliği artırmak için modellerini yeniden düşünmeye sevk etti. Bu nedenle, ücretlerin piyasa durumunu ve katılımcı sayısını dikkate alarak, koordinatör artık 6, 7 veya 8 katılımcıyı içeren coinjoins düzenleyebilir. Bu geliştirilmiş oturumlar "_Surge Cycles_" olarak adlandırılır. Konfigürasyondan bağımsız olarak, Whirlpool coinjoin'lerde her zaman yalnızca 2 yeni katılımcının olduğunu unutmamak önemlidir.


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


Bu modelde, kullanıcı yalnızca havuza ilk girişinde ücret öder ve böylece ek ücret ödemeden çok sayıda remikse katılabilir. Remiksçiler için Mining ücretlerini karşılayanlar yeni giriş yapanlardır.


Bir Coin'ün geçmişte karşılaştığı akranlarıyla birlikte katıldığı her ek CoinJoin ile anonsetler katlanarak büyüyecektir. Bu nedenle amaç, her oluşumda her bir karışık Coin ile ilişkili anonsetlerin yoğunluğunu güçlendirmeye katkıda bulunan bu ücretsiz remikslerden yararlanmaktır.


Whirlpool iki önemli gereksinim dikkate alınarak tasarlanmıştır:


- Samourai Wallet'in öncelikle bir akıllı telefon uygulaması olduğu göz önüne alındığında, mobil cihazlarda uygulamanın erişilebilirliği;
- Yeniden karıştırma döngülerinin hızı, anonsetlerde önemli bir artışı teşvik eder.

Bu zorunluluklar Samourai Wallet'in geliştiricilerine Whirlpool'nın tasarımında rehberlik etmiş ve onları döngü başına katılımcı sayısını sınırlamaya yönlendirmiştir. Çok az sayıda katılımcı CoinJoin'nin verimliliğini tehlikeye atarak her döngüde üretilen anonsları büyük ölçüde azaltırken, çok fazla katılımcı mobil uygulamalarda yönetim sorunları yaratacak ve döngülerin akışını engelleyecekti.

**Sonuç olarak, Whirlpool'da CoinJoin başına yüksek sayıda katılımcı olmasına gerek yoktur, çünkü anonslar birkaç CoinJoin döngüsünün birikimiyle elde edilir.**


[-> Whirlpool anonsları hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Havuzlar ve CoinJoin ücretleri

Bu çoklu döngülerin karma sikkelerin anonsetlerini etkili bir şekilde artırması için, kullanılan UTXO miktarlarını kısıtlamak üzere belirli bir çerçeve oluşturulmalıdır. Whirlpool böylece farklı havuzları tanımlar.


Bir havuz, CoinJoin sürecini optimize etmek için kullanılacak UTXO miktarı üzerinde anlaşan ve birlikte karıştırmak isteyen bir grup kullanıcıyı temsil eder. Her havuz, kullanıcının katılmak için uyması gereken sabit bir UTXO miktarı belirler. Bu nedenle, Whirlpool ile coinjoins gerçekleştirmek için bir havuz seçmeniz gerekir. Şu anda mevcut olan havuzlar aşağıdaki gibidir:


- 0.5 bitcoin;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Bitcoinlerinizle bir havuza katıldığınızda, bunlar havuzdaki diğer katılımcılarınkiyle tamamen homojen olan generate UTXO'lara bölünecektir. Her havuzun bir maksimum limiti vardır; bu nedenle, bu limiti aşan miktarlar için, ya aynı havuza iki ayrı giriş yapmak ya da kendinizi daha yüksek bir miktarla başka bir havuza yönlendirmek zorunda kalacaksınız:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Daha önce de belirtildiği gibi, bir UTXO bir CoinJoin'e entegre edilmeye hazır olduğunda bir havuza ait olduğu kabul edilir. Ancak bu, kullanıcının mülkiyetini kaybettiği anlamına gelmez. **Farklı karıştırma döngüleri boyunca anahtarlarınızın ve dolayısıyla bitcoinlerinizin tam kontrolünü elinizde tutarsınız.** CoinJoin tekniğini diğer merkezi karıştırma tekniklerinden ayıran da budur.


Bir CoinJoin havuzuna girmek için Mining ücretlerinin yanı sıra hizmet ücretlerinin de ödenmesi gerekmektedir. Hizmet ücretleri her havuz için sabittir ve Whirlpool'in geliştirilmesi ve bakımından sorumlu ekiplere tazminat ödenmesini amaçlamaktadır.

Whirlpool'i kullanmak için hizmet ücretleri havuza girdikten sonra yalnızca bir kez ödenecektir. Bu adımdan sonra, herhangi bir ek ücret ödemeden sınırsız sayıda remikse katılma fırsatına sahip olursunuz. İşte her havuz için geçerli sabit ücretler:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Bu ücretler, CoinJoin'a koyduğunuz miktardan bağımsız olarak, esasen seçilen havuz için bir giriş bileti görevi görür. Dolayısıyla, 0.01 havuzuna ister tam olarak 0.01 BTC ile ister 0.5 BTC ile girin, ücretler mutlak değer olarak aynı kalacaktır.


Eş birleşimlere geçmeden önce, kullanıcı 2 strateji arasında seçim yapabilir:


- Karşılığında birkaç küçük UTXO alacaklarını bilerek hizmet ücretlerini en aza indirmek için daha küçük bir havuzu tercih edin;
- Ya da daha büyük bir havuzu tercih ederek, daha yüksek ücretler ödemeyi kabul ederek daha az sayıda ve daha değerli UTXO'lar elde edebilirsiniz.


Genel olarak CoinJoin döngülerinden sonra birkaç karışık UTXO'nun birleştirilmemesi tavsiye edilir, çünkü bu özellikle Ortak-Giriş-Ownership Sezgisel (CIOH) nedeniyle elde edilen gizliliği tehlikeye atabilir. Bu nedenle, çıktı olarak çok sayıda küçük değerli UTXO'ya sahip olmaktan kaçınmak için daha fazla ödeme yapmak anlamına gelse bile daha büyük bir havuz seçmek akıllıca olabilir. Kullanıcı tercih ettiği havuzu seçmek için bu ödünleri tartmalıdır.


Hizmet ücretlerinin yanı sıra, herhangi bir Bitcoin işlemine özgü Mining ücretleri de dikkate alınmalıdır. Bir Whirlpool kullanıcısı olarak, hazırlık işlemi (`Tx0`) için Mining ücretlerini ve ilk CoinJoin için olanları ödemeniz gerekecektir. Whirlpool'nin yeni katılımcıların ödemelerine dayanan modeli sayesinde sonraki tüm remiksler ücretsiz olacaktır.


Gerçekten de, her bir Whirlpool CoinJoin'de, girdiler arasında iki kullanıcı yeni girenlerdir. Diğer girdiler remiksçilerden gelmektedir. Sonuç olarak, işlemdeki tüm katılımcıların Mining ücretleri, daha sonra ücretsiz remikslerden de yararlanacak olan bu iki yeni katılımcı tarafından karşılanır:

![coinjoin](assets/en/6.webp)

Bu ücret sistemi sayesinde, Whirlpool kendisini diğer CoinJoin hizmetlerinden gerçekten ayırmaktadır çünkü UTXO'ların anonimleri kullanıcı tarafından ödenen fiyatla orantılı değildir. Böylece, sadece havuza giriş ücreti ve iki işlem için (`Tx0` ve ilk karışım) Mining ücretlerini ödeyerek oldukça yüksek anonimlik seviyelerine ulaşmak mümkündür.

Kullanıcının, aşağıdaki eğitimde tartışacağımız `mix to' seçeneğini seçmediği sürece, çoklu coin birleşimlerini tamamladıktan sonra UTXO'larını havuzdan çekmek için Mining ücretlerini de karşılaması gerekeceğini unutmamak önemlidir.


### Whirlpool tarafından kullanılan HD Wallet hesapları

Whirlpool aracılığıyla bir CoinJoin gerçekleştirmek için Wallet'in birkaç farklı hesabı generate yapması gerekir. Bir HD (*Hiyerarşik Deterministik*) Wallet bağlamında bir hesap, diğerlerinden tamamen yalıtılmış bir bölüm oluşturur, bu ayrım Wallet'in hiyerarşisinin üçüncü derinlik seviyesinde, yani `xpub' seviyesinde gerçekleşir.


Bir HD Wallet teorik olarak en fazla `2^(32/2)` farklı hesap türetebilir. Tüm Bitcoin cüzdanlarında varsayılan olarak kullanılan ilk hesap `0'` indeksine karşılık gelir.


Samourai veya Sparrow gibi Whirlpool'e uyarlanmış cüzdanlar için, CoinJoin sürecinin ihtiyaçlarını karşılamak üzere 4 hesap kullanılır:


- 0'` indeksi ile tanımlanan **depozito** hesabı;
- 2 147 483 644'` endeksi ile tanımlanan **kötü banka** (veya doxxic change) hesabı;
- 2 147 483 645'` endeksi ile tanımlanan **premix** hesabı;
- Postmix** hesabı, `2 147 483 646'` endeksi ile tanımlanmıştır.


Bu hesapların her biri CoinJoin süreci içerisinde belirli bir işlevi yerine getirmektedir.


Tüm bu hesaplar tek bir seed'ya bağlıdır, bu da kullanıcının kurtarma cümlesini ve varsa passphrase'ini kullanarak tüm bitcoinlerine erişimi geri kazanmasına olanak tanır. Ancak, bu kurtarma işlemi sırasında kullanılan farklı hesap dizinlerinin yazılıma belirtilmesi gerekmektedir.


Şimdi bu hesaplar dahilinde bir Whirlpool CoinJoin'in farklı aşamalarına bakalım.


### Whirlpool'daki eş birleşmelerin farklı aşamaları

**1. Aşama: Tx0**

Herhangi bir Whirlpool CoinJoin'in başlangıç noktası **deposit** hesabıdır. Bu hesap, yeni bir Bitcoin Wallet oluşturduğunuzda otomatik olarak kullandığınız hesaptır. Bu hesaba karıştırılmak istenen bitcoinler yatırılmalıdır.

Tx0', Whirlpool karıştırma işlemindeki ilk adımı temsil eder. Karışımın homojenliğini sağlamak için UTXO'yı seçilen havuzun miktarına karşılık gelen birimlere bölerek CoinJoin için hazırlamayı ve eşitlemeyi amaçlar. Eşitlenen UTXO daha sonra **premiks** hesabına gönderilir. Havuza giremeyen fark ise belirli bir hesaba ayrılır: **kötü banka** (veya "doxxic change").

Bu ilk işlem `Tx0` aynı zamanda karışım koordinatörüne ödenmesi gereken hizmet ücretlerinin ödenmesine de hizmet eder. Aşağıdaki adımlardan farklı olarak, bu işlem işbirliğine dayalı değildir; bu nedenle kullanıcı tüm Mining ücretlerini üstlenmelidir:

![coinjoin](assets/en/7.webp)


Bu `Tx0` işlemi örneğinde, **mevduat** hesabımızdan `372.000 Sats`lik bir girdi, aşağıdaki gibi dağıtılan birkaç UTXO çıktısına bölünür:


- 100.000 Sats`lik havuza girişe karşılık gelen hizmet ücretleri için koordinatöre yönelik 5.000 Sats`lik bir tutar;
- Karışım için üç UTXO hazırlandı, **premix** hesabımıza yönlendirildi ve koordinatöre kaydedildi. Bu UTXO'lerin her biri, gelecekteki ilk karışımları için Mining ücretlerini karşılamak üzere `108.000 Sats` olarak eşitlenmiştir;
- Çok küçük olduğu için havuza giremeyen fazlalık, zehirli değişim olarak kabul edilir. Kendi özel hesabına gönderilir. Burada bu değişim `40,000 Sats` tutarındadır;
- Son olarak, bir çıktı oluşturmayan ancak `Tx0`ı onaylamak için gerekli olan Mining ücretleri olan `3.000 Sats` vardır.


Örneğin, işte gerçek bir Whirlpool Tx0 (benden değil): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**2. Adım: Doxxic değişim**

Havuza entegre edilemeyen ve burada `40.000 Sats`a denk gelen fazlalık, Wallet'daki diğer UTXO'den kesin bir şekilde ayrılmasını sağlamak için "doxxic change" olarak da adlandırılan **bad bank** hesabına yönlendirilir.


Bu UTXO kullanıcının gizliliği açısından tehlikelidir, çünkü yalnızca geçmişine ve dolayısıyla muhtemelen sahibinin kimliğine bağlı olmakla kalmaz, aynı zamanda CoinJoin gerçekleştirmiş bir kullanıcıya ait olduğu da belirtilir.

Bu UTXO karışık çıktılarla birleştirilirse, özellikle Ortak Girdi-Ownership-Heuristic (CIOH) nedeniyle CoinJoin döngüleri sırasında kazanılan tüm gizliliği kaybedeceklerdir. Diğer doxxic değişikliklerle birleştirilirse, bu CoinJoin döngülerinin farklı girdilerini birbirine bağlayacağından kullanıcı gizliliğini kaybetme riskiyle karşı karşıya kalır. Bu nedenle dikkatle ele alınmalıdır. Bu toksik UTXO'yı yönetmenin yolu bu makalenin son bölümünde ayrıntılı olarak açıklanacak ve gelecekteki eğitimler bu yöntemleri PlanB Network'te daha derinlemesine ele alacaktır.


**3. Adım: İlk Karışım**

Tx0` tamamlandıktan sonra, eşitlenmiş UTXO'lar Wallet'imizin **premix** hesabına gönderilir ve "ilk karışım" olarak da adlandırılan ilk CoinJoin döngüsüne dahil edilmeye hazır hale gelir. Örneğimizde olduğu gibi, `Tx0` karıştırma için birden fazla UTXO üretirse, bunların her biri ayrı bir ilk CoinJoin'ye entegre edilecektir.


Bu ilk karışımların sonunda, **premix** hesabı boş olacak ve bu ilk CoinJoin için Mining ücretlerini ödemiş olan coinlerimiz tam olarak seçilen havuz tarafından tanımlanan miktara ayarlanacaktır. Örneğimizde, `108 000 Sats` olan ilk UTXO'larımız tam olarak `100 000 Sats`e düşürülmüş olacaktır.

![coinjoin](assets/en/8.webp)

**4. Adım: Remiksler**

İlk miksten sonra UTXO'lar **postmix** hesabına aktarılır. Bu hesap halihazırda karıştırılmış UTXO'ları ve yeniden karıştırılmayı bekleyenleri toplar. Whirlpool istemcisi aktif olduğunda, **postmix** hesabındaki UTXO'lar otomatik olarak remiks için hazır olur ve bu yeni döngülere katılmak üzere rastgele seçilir.


Bir hatırlatma olarak, remiksler %100 ücretsizdir: ek hizmet ücreti veya Mining ücreti gerekmez. UTXO'ları **postmix** hesabında tutmak, böylece değerlerini sağlam tutar ve aynı zamanda anonsetlerini iyileştirir. Bu nedenle, bu coinlerin birden fazla CoinJoin döngüsüne katılmasına izin vermek önemlidir. Bunun size kesinlikle hiçbir maliyeti yoktur ve anonimlik seviyelerini artırır.


Karışık UTXO'ları harcamaya karar verdiğinizde, bunu doğrudan bu **postmix** hesabından yapabilirsiniz. Ücretsiz remikslerden faydalanmak ve gizliliklerini azaltabilecek Whirlpool devresinden ayrılmalarını önlemek için karışık UTXO'ları bu hesapta tutmanız tavsiye edilir.


Bir sonraki eğitimde göreceğimiz gibi, karışık madeni paralarınızı belirli sayıda madeni para birleşiminden sonra otomatik olarak Cold Wallet gibi başka bir Wallet'ya gönderme imkanı sunan `mix to' seçeneği de vardır.

Teoriyi ele aldıktan sonra, Samourai Wallet Android uygulaması aracılığıyla Whirlpool kullanımına ilişkin bir eğitimle pratiğe geçelim!


## Eğitim: Samourai Wallet üzerinde CoinJoin Whirlpool

Whirlpool'ü kullanmak için çok sayıda seçenek vardır. Burada tanıtmak istediğim, Android'de açık kaynaklı bir Bitcoin Wallet yönetim uygulaması olan Samourai Wallet seçeneğidir (Dojo olmadan).


Dojo olmadan Samourai'de miks yapmak, kullanımı oldukça kolay, kurulumu hızlı ve bir Android telefon ve internet bağlantısından başka bir cihaz gerektirmeme avantajına sahiptir.


Ancak bu yöntemin iki önemli dezavantajı vardır:


- Coinjoins yalnızca Samourai arka planda çalışırken ve bağlıyken gerçekleşecektir. Bu, bitcoinlerinizi 7/24 karıştırmak ve remikslemek istiyorsanız, Samourai'yi sürekli açık tutmanız gerektiği anlamına gelir;
- Kendi Dojo'nuzu bağlamaya dikkat etmeden Whirlpool'yı Samourai Wallet ile kullanırsanız, uygulamanız Samourai ekipleri tarafından tutulan sunucuya bağlanmak zorunda kalacak ve Wallet'nizin `xpub`ını onlara açıklayacaksınız. Bu anonim bilgi parçaları, uygulamanızın işlemlerinizi bulması için gereklidir.


Bu sınırlamaların üstesinden gelmek için ideal çözüm, kişisel Bitcoin düğümünüzde bir Whirlpool CLI örneği ile ilişkili kendi Dojo'nuzu çalıştırmaktır. Bu şekilde, herhangi bir bilgi sızıntısını önleyecek ve tam bağımsızlık elde edeceksiniz. Aşağıda sunulan eğitim belirli hedefler veya yeni başlayanlar için faydalı olsa da, CoinJoin oturumunuzu gerçekten optimize etmek için kendi Dojo'nuzu kullanmanız önerilir. Bu yapılandırmanın kurulumuna ilişkin ayrıntılı bir kılavuz yakında PlanB Network'te mevcut olacaktır.


### Samourai Wallet'nin Kurulumu

Başlamak için Samourai Wallet uygulamasına ihtiyacınız olacak. APK'yı kullanarak doğrudan resmi web sitesinden, GitLab'larından veya Google Play Store'dan indirebilirsiniz.


### Bir Software Wallet Oluşturma

Yazılımı kurduktan sonra, Samourai üzerinde bir Bitcoin Wallet oluşturmaya devam etmeniz gerekecektir. Zaten bir tane varsa, doğrudan bir sonraki adıma geçebilirsiniz.


Uygulamayı açtıktan sonra mavi `Başlat` düğmesine basın. Daha sonra telefonunuzun dosyalarında yeni Wallet'nizin şifrelenmiş yedeğinin saklanacağı bir konum seçmeniz istenecektir.


![samourai](assets/notext/9.webp)

İlgili çentiğe tıklayarak Tor'u etkinleştirin. Bu aşamada, belirli bir Dojo seçme seçeneğiniz de vardır. Ancak, bu eğitimde varsayılan Dojo ile devam edeceğiz; bu nedenle seçeneği devre dışı bırakabilirsiniz. Tor bağlandığında, `Yeni bir Wallet oluştur` düğmesine basın.

![samourai](assets/notext/10.webp)


Samourai Wallet daha sonra sizden bir BIP39 passphrase belirlemenizi ister. Bu ek şifre, özel anahtarlarınızın türetilmesinde doğrudan etkili olduğu için çok önemlidir. Bu passphrase'un olası bir kaybı, bitcoinlerinize erişememenizle sonuçlanacak ve onları geri alınamaz bir şekilde kaybedecektir. Samourai Wallet'inizi geri yüklemek için hem 12 kelimelik kurtarma cümlenize hem de passphrase'a sahip olmanız zorunludur.


Bu nedenle, sağlam bir passphrase seçmeniz ve bitcoinlerinizin güvenliğini sağlamak için kağıt veya metalik bir ortamda bir veya daha fazla fiziksel kopya çıkarmanız çok önemlidir. Bu görevleri tamamladıktan sonra, `Kayıp durumunda...` kutusunu işaretleyin ve ardından `SONRAKİ` düğmesine basın.


![samourai](assets/notext/11.webp)


Daha sonra 5 ila 8 haneden oluşan bir PIN kodu tanımlamanız gerekir. Bu kod telefonunuzda Wallet'nize erişimi güvence altına alacaktır. Samourai uygulamasını her açmak istediğinizde istenecektir. Sağlam bir PIN kodu seçin ve yedek bir kopyasını sakladığınızdan emin olun. Bundan sonra `NEXT` düğmesine basabilirsiniz.


![samourai](assets/notext/12.webp)


Samourai onay için sizi PIN kodunuzu tekrar girmeye davet edecektir. Girin ve ardından `SONLANDIR` düğmesine basın.


![samourai](assets/notext/13.webp)


Daha sonra 12 kelimeden oluşan kurtarma cümlenize erişeceksiniz. Bu ifade, Wallet'ünüzü daha önce girilen passphrase ile kurtarmanızı sağlar. Bir sorun durumunda bitcoinlerinizin güvenliğini sağlamak için bu ifadenin bir veya daha fazla kopyasını kağıt veya metalik bir malzeme gibi fiziksel ortamlarda oluşturmanız şiddetle tavsiye edilir.


Bu yedeklemeleri yaptıktan sonra, yeni Samourai Wallet'nızın Interface'ine yönlendirileceksiniz.


![samourai](assets/notext/14.webp)


PayNym Botunuzu edinmeniz önerilmektedir. Eğitimimiz için gerekli olmasa da dilerseniz talep edebilirsiniz.


![samourai](assets/notext/15.webp)

Bu yeni Wallet'de bitcoin almaya devam etmeden önce, Wallet yedeklerinizin (passphrase ve kurtarma ifadesi) geçerliliğini yeniden kontrol etmeniz şiddetle tavsiye edilir. passphrase'yi doğrulamak için, ekranın sol üst köşesinde bulunan PayNym Botunuzun simgesini seçebilir ve ardından yolu takip edebilirsiniz:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


Doğrulamayı gerçekleştirmek için passphrase'unuzu girin.


![samourai](assets/notext/16.webp)


Samourai geçerli olup olmadığını teyit edecektir.


![samourai](assets/notext/17.webp)


Kurtarma cümlesinin yedeğini doğrulamak için, ekranın sol üst köşesinde bulunan PayNym Botunuzun simgesine erişin ve bu yolu izleyin:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai kurtarma cümlenizi içeren bir pencere görüntüleyecektir. Fiziksel yedeklemenizle tam olarak eşleştiğinden emin olun.


Daha ileri gitmek ve tam bir kurtarma testi gerçekleştirmek için, Wallet'inizin `xpub'lardan biri gibi bir tanık öğesini not edin, ardından Wallet'inizi silmeye devam edin (hala boş olması koşuluyla). Amaç, yalnızca fiziksel yedeklerinizi kullanarak bu boş Wallet'i geri yüklemeyi denemektir. Geri yükleme başarılı olursa, bu yedeklerinizin geçerli ve güvenilir olduğunu gösterir.


### Bitcoin alma

Wallet'inizi oluşturduktan sonra, `0'` indeksi ile tanımlanan tek bir hesapla başlayacaksınız. Bu, önceki bölümlerde bahsettiğimiz **deposit** hesabıdır. Coinjoins için tasarlanan bitcoinleri bu hesaba aktarmanız gerekecek.


Bunu yapmak için ekranın sağ alt kısmında bulunan mavi `+` sembolüne tıklayın.


![samourai](assets/notext/18.webp)


Ardından Green `Alıcı` düğmesine tıklayın.


![samourai](assets/notext/19.webp)


Samourai bitcoinleri almak için otomatik olarak generate yeni bir boş Address oluşturacaktır.


![samourai](assets/notext/20.webp)


Orada karıştırılmak üzere bitcoinleri gönderebilirsiniz.


![samourai](assets/notext/21.webp)


### Tx0'ın Yapılması

İşlem onaylandığında, coinjoins işlemini başlatabiliriz. Bunu yapmak için ekranın sağ altındaki mavi `+` düğmesine tıklayın.


![samourai](assets/notext/22.webp)


Ardından mavi renkli `Whirlpool` üzerine tıklayın.


![samourai](assets/notext/23.webp)


Whirlpool başlatılırken ve Samourai gerekli hesapları oluştururken bekleyin.


![samourai](assets/notext/24.webp)


Daha sonra Whirlpool ana sayfasına ulaşacaksınız. Başlat'a tıklayın.

![samourai](assets/notext/25.webp)

CoinJoin döngülerinde göndermek istediğiniz **deposit** hesabından UTXO'u seçin, ardından `Sonraki` üzerine tıklayın.


![samourai](assets/notext/26.webp)


Bir sonraki adımda, ilk karışımınızın yanı sıra `Tx0`a tahsis edilecek ücret seviyesini seçmeniz gerekecektir. Bu ayar, `Tx0` ve ilk CoinJoin'ınızın (veya ilk coinjoins) onaylanma hızını belirleyecektir. Unutmayın ki `Tx0` ve ilk miks için Mining ücretleri sizin sorumluluğunuzdadır, ancak sonraki remiksler için Mining ücreti ödemeniz gerekmeyecektir. Düşük, Normal veya Yüksek seçenekleri arasında seçim yapabilirsiniz.


![samourai](assets/notext/27.webp)


Aynı pencerede, gireceğiniz havuzu seçme seçeneğiniz de bulunmaktadır. Başlangıçta `454,258 Sats`lük bir UTXO seçtiğim göz önüne alındığında, tek olası seçeneğim `100,000 Sats` havuzu. Bu sayfa aynı zamanda Mining ücretlerine ek olarak havuzun hizmet ücretlerini de size sunarak bu CoinJoin döngüsü için toplam maliyeti bilmenizi sağlar. Her şey size uygunsa, uygun havuzu seçin ve mavi `DÖNGÜ DETAYLARINI DOĞRULA` düğmesine tıklayarak devam edin.


![samourai](assets/notext/28.webp)


Daha sonra CoinJoin döngünüzün tüm ayrıntılarını görebilirsiniz:


- havuza girecek UTXO'ların sayısı;
- çeşitli ücretler tahakkuk eder;
- doxic değişim miktarı...


Bilgileri doğrulayın, ardından Green `START CYCLE` düğmesine tıklayın.


![samourai](assets/notext/29.webp)


CoinJoin döngüsüne girişinizden kaynaklanan toksik değişikliği "harcanamaz" olarak işaretlemenizi öneren bir pencere açılacaktır. EVET'i seçtiğinizde, bu UTXO Wallet'unuzda görünmeyecek ve gelecekteki işlemler için seçilemeyecektir. Ancak, Wallet'unuzdaki UTXO'lar listesinde erişilebilir kalacaktır ve burada durumunu manuel olarak değiştirebilirsiniz. Daha sonra gizliliğinizi tehlikeye atabilecek herhangi bir işlem hatasından kaçınmak için bu seçeneği tercih etmeniz önerilir. Eğer `HAYIR` seçeneğini seçerseniz, toksik değişiklik Wallet'unuzda kullanılabilir durumda kalacaktır. Bu zehirli değişikliğin yönetimi ve kullanımı hakkında daha fazla bilgi edinmek istiyorsanız, bu eğitimin son bölümünü okumanızı tavsiye ederim.


![samourai](assets/notext/30.webp)


Samourai daha sonra Tx0'ınızı yayınlayacaktır.


![samourai](assets/notext/31.webp)


### Eş birleşimlerin yapılması

Tx0 yayınlandıktan sonra, bunu Whirlpool menüsünün `İşlemler` sekmesinde bulabilirsiniz.


![samourai](assets/notext/32.webp)

Karıştırılmaya hazır UTXO'larınız **Premix** hesabına karşılık gelen `Karıştırma devam ediyor...` sekmesindedir.

![samourai](assets/notext/33.webp)


Tx0' onaylandıktan sonra, UTXO'larınız otomatik olarak koordinatöre kaydedilecek ve ilk miksler otomatik bir şekilde art arda başlayacaktır.


![samourai](assets/notext/34.webp)


Postmix** hesabına karşılık gelen `Remixing` sekmesini kontrol ederek, ilk karışımlardan kaynaklanan UTXO'ları gözlemleyeceksiniz. Bu coinler, herhangi bir ek ücrete tabi olmayan sonraki remiksler için hazır kalacaktır. Yeniden karıştırma süreci ve bir CoinJoin döngüsünün verimliliği hakkında daha fazla bilgi edinmek için bu diğer makaleye başvurmanızı tavsiye ederim: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-Whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


Sağında bulunan duraklatma düğmesine basarak bir UTXO'in remiksini geçici olarak askıya almak mümkündür. Tekrar remikslemeye uygun hale getirmek için aynı düğmeye ikinci kez tıklamanız yeterlidir. Kullanıcı başına ve havuz başına aynı anda yalnızca bir CoinJoin gerçekleştirilebileceğini unutmamak önemlidir. Dolayısıyla, CoinJoin için hazır 6 adet `100 000 Sats` UTXO'nuz varsa, bunlardan yalnızca biri karıştırılabilir. Bir UTXO'i karıştırdıktan sonra Samourai Wallet, her bir Coin'nın yeniden karıştırılmasını çeşitlendirmek ve dengelemek için kullanılabilirliğinizden rastgele yeni bir UTXO seçmeye devam eder.


![samourai](assets/notext/36.webp)


UTXO'larınızın remiksleme için sürekli kullanılabilirliğini sağlamak için Samourai uygulamasını arka planda aktif tutmak gerekir. Telefonunuzda Whirlpool'un çalıştığını onaylayan bir bildirim görmelisiniz. Uygulamayı kapatmak veya telefonunuzu kapatmak, coinjoins'i duraklatacaktır.


### Eş birleşimlerin tamamlanması

Karıştırılmış bitcoinlerinizi harcamak için, Whirlpool menü sekmelerinde `Yeniden Karıştırma` olarak belirtilen **Postmix** hesabına gidin.


![samourai](assets/notext/37.webp)


Sağ altta bulunan mavi Whirlpool logosuna tıklayın.


![samourai](assets/notext/38.webp)


Ardından `Karma UTXO'ları Harcayın` seçeneğine tıklayın.


![samourai](assets/notext/39.webp)


Daha sonra Samourai Wallet ile yapılan diğer işlemlerde olduğu gibi alıcının Address'ünü ve gönderilecek tutarı girebilirsiniz. Mavi arka plan, fonların **deposit** hesabından değil, bir Whirlpool hesabından harcandığını gösterir.


![samourai](assets/notext/40.webp)


Sağ üstteki 3 küçük noktaya tıklayarak, belirli UTXO'ları seçme seçeneğine sahipsiniz.

![samourai](assets/notext/41.webp)

Pencerenin sağ üst tarafındaki beyaz kareye tıklayarak, alıcı Address'in QR kodunu kameranızla tarayabilirsiniz.


![samourai](assets/notext/42.webp)


Harcama işleminiz için gerekli bilgileri girin, ardından mavi renkli `İŞLEMİ DOĞRULA` düğmesine tıklayın.


![samourai](assets/notext/43.webp)


Bir sonraki adımda, işleminizle ilişkili ücret oranını değiştirme seçeneğiniz vardır. İlgili kutuyu işaretleyerek Stonewall seçeneğini de etkinleştirebilirsiniz. Stonewall seçeneği seçilebilir değilse, **Postmix** hesabınızda bu özel işlem yapısını desteklemek için yeterli büyüklükte bir UTXO bulunmadığı anlamına gelir.


[-> Stonewall işlemleri hakkında daha fazla bilgi edinin.](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Her şey sizi tatmin ediyorsa, Green `Gönder ... BTC` düğmesine tıklayın.


![samourai](assets/notext/44.webp)


Samourai daha sonra işleminizi ağda yayınlamadan önce imzalamaya devam edecektir. Bir Miner tarafından bloğa eklenene kadar beklemeniz yeterlidir.


![samourai](assets/notext/45.webp)


### Bir SCODE Kullanma

Bazen, Samourai Wallet takımları "SCODE'lar" sunar. SCODE, havuzun hizmet ücretlerinde indirim sağlayan bir promosyon kodudur. Samourai Wallet zaman zaman özel etkinlikler sırasında kullanıcılarına bu tür kodlar sunar. Gelecekteki SCODES'leri kaçırmamak için Samourai Wallet'yi] (https://twitter.com/SamouraiWallet) sosyal medyada takip etmenizi tavsiye ederim.


Samourai'ye bir SCODE uygulamak için, yeni bir CoinJoin döngüsüne başlamadan önce, Whirlpool menüsüne gidin ve ekranın sağ üst köşesinde bulunan üç küçük noktayı seçin.


![samourai](assets/notext/46.webp)


`SCODE (promosyon kodu) Whirlpool` üzerine tıklayın.


![samourai](assets/notext/47.webp)


Açılan pencereye SCODE'u girin ve ardından `Tamam'a tıklayarak doğrulayın.


![samourai](assets/notext/48.webp)


Whirlpool otomatik olarak kapanacaktır. Samourai'nin yüklenmesinin bitmesini bekleyin, ardından Whirlpool menüsünü tekrar açın.


![samourai](assets/notext/49.webp)


Üç küçük noktaya bir kez daha tıklayarak ve ardından `SCODE (promosyon kodu) Whirlpool`i seçerek SCODE'unuzun doğru şekilde kaydedildiğinden emin olun. Her şey yolundaysa, hizmet ücretlerinde indirimle yeni bir Whirlpool döngüsü başlatmaya hazırsınız demektir. Bu SCODE'ların geçici olduğunu unutmamak önemlidir: geçerliliğini yitirmeden önce birkaç gün boyunca geçerli kalırlar.


## CoinJoin döngülerimizin kalitesi nasıl anlaşılır?

Bir CoinJoin'nin gerçekten etkili olabilmesi için, girdi ve çıktıların miktarları arasında iyi bir tekdüzelik göstermesi esastır. Bu tekdüzelik, harici bir gözlemcinin gözünde olası yorumların sayısını artırır ve böylece işlemi çevreleyen belirsizliği artırır. Bir CoinJoin tarafından yaratılan bu belirsizliği ölçmek için, işlemin entropisini hesaplamaya başvurulabilir.


Bu göstergelerin derinlemesine incelenmesi için (Whirlpool modeli, eş birleşimlere en fazla homojenlik getiren model olarak kabul edilmektedir) sizi eğiticiye yönlendiriyorum: [BOLTZMANN CALCULATOR](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Daha sonra, birkaç CoinJoin döngüsünün performansı, bir Coin'in gizlendiği grupların kapsamına göre değerlendirilir. Bu grupların boyutu anonset olarak adlandırılan şeyi tanımlar. İki tür anons vardır: ilki elde edilen gizliliği geriye dönük bir analizle (günümüzden geçmişe), ikincisi ise ileriye dönük bir analizle (geçmişten günümüze) değerlendirir. Bu iki göstergenin ayrıntılı bir açıklaması için sizi öğreticiye başvurmaya davet ediyorum: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Postmix nasıl yönetilir?

CoinJoin döngülerini gerçekleştirdikten sonra, en iyi strateji UTXO'larınızı **postmix** hesabında tutmak ve gelecekte kullanılmalarını beklemektir. Hatta harcamanız gerekene kadar süresiz olarak remiks yapmalarına izin vermeniz tavsiye edilir.


Bazı kullanıcılar karışık bitcoinlerini bir Hardware Wallet ile güvence altına alınmış bir Wallet'e aktarmayı düşünebilir. Bu mümkündür, ancak elde edilen gizliliği tehlikeye atmamak için Samourai Wallet'ün önerilerini titizlikle takip etmek önemlidir.


UTXO'ların birleştirilmesi en sık yapılan hatayı oluşturmaktadır. CIOH'dan (*Common-Input-Ownership-Heuristic*) kaçınmak için karışık UTXO'ları karışık olmayan UTXO'larla aynı işlemde birleştirmekten kaçınmak gerekir. Bu, Wallet'nizdeki UTXO'larınızın özellikle etiketleme açısından dikkatli bir şekilde yönetilmesini gerektirir. CoinJoin'nın ötesinde, UTXO'ların birleştirilmesi genellikle düzgün yönetilmediğinde gizlilik kaybına yol açan kötü bir uygulamadır.

Karma UTXO'ların birbirleriyle birleştirilmesi konusunda da dikkatli olmalısınız. Karma UTXO'larınızda önemli anonsetler varsa orta düzeyde konsolidasyonlar mümkündür, ancak bu kaçınılmaz olarak coin'lerinizin gizliliğini azaltacaktır. Konsolidasyonların ne çok büyük olduğundan ne de yetersiz sayıda remiksten sonra yapıldığından emin olun, çünkü bu, UTXO'larınız arasında CoinJoin döngülerinden önce ve sonra çıkarılabilir bağlantılar kurma riski taşır. Bu işlemler hakkında şüphe duyulması halinde, en iyi uygulama karışım sonrası UTXO'ları birleştirmemek ve her seferinde yeni bir boş Address oluşturarak bunları tek tek Hardware Wallet'inize aktarmaktır. Bir kez daha, alınan her UTXO'i uygun şekilde etiketlemeyi unutmayın.


Ayrıca, postmix UTXO'larınızı yaygın olmayan komut dosyaları kullanarak bir Wallet'e aktarmamanız tavsiye edilir. Örneğin, `P2WSH' komut dosyalarını kullanarak bir Multisig Wallet'ten Whirlpool'ye girerseniz, orijinal olarak aynı Wallet türüne sahip diğer kullanıcılarla karıştırılma şansınız çok azdır. Postmix'inizden bu aynı Multisig Wallet'e çıkarsanız, karışık bitcoinlerinizin gizlilik seviyesi büyük ölçüde azalacaktır. Komut dosyalarının ötesinde, sizi kandırabilecek başka birçok Wallet parmak izi vardır.


Tüm Bitcoin işlemlerinde olduğu gibi, alıcı adreslerinin tekrar kullanılmaması da uygundur. Her yeni işlem yeni bir boş Address ile alınmalıdır.


En basit ve en güvenli çözüm, karışık UTXO'larınızı **postmix** hesaplarında dinlendirmek, yeniden karıştırmalarına izin vermek ve yalnızca harcamak için dokunmaktır. Samourai ve Sparrow cüzdanları, zincir analiziyle ilgili tüm bu risklere karşı ek korumalara sahiptir. Bu korumalar hata yapmaktan kaçınmanıza yardımcı olur.


## Doxxic değişim nasıl yönetilir?

Daha sonra, CoinJoin havuzuna giremeyen değişiklik olan doxxic değişikliği yönetirken dikkatli olmalısınız. Whirlpool kullanımından kaynaklanan bu toksik UTXO'lar, sizinle CoinJoin kullanımı arasında bir bağlantı kurduklarından gizliliğiniz için risk oluştururlar. Bu nedenle, bunları dikkatli bir şekilde ele almak ve diğer UTXO'larla, özellikle de karışık UTXO'larla birleştirmemek zorunludur. İşte bunların kullanımı için dikkate alınması gereken farklı stratejiler:


- Daha küçük havuzlarda karıştırın:** Zehirli UTXO'niz tek başına daha küçük bir havuza girecek kadar büyükse, karıştırmayı düşünün. Bu genellikle en iyi seçenektir. Ancak, farklı girişlerinizi birbirine bağlayabileceğinden, bir havuza erişmek için birkaç toksik UTXO'yu birleştirmemek çok önemlidir.
- Bunları "harcanamaz" olarak işaretleyin:** Başka bir yaklaşım da bunları kullanmayı bırakmak, özel hesaplarında "harcanamaz" olarak işaretlemek ve sadece HODL yapmaktır. Bu, onları yanlışlıkla harcamamanızı sağlar. Bitcoin'in değeri artarsa, toksik UTXO'larınıza daha uygun yeni havuzlar ortaya çıkabilir;
- Bağış yapın:** Bitcoin ve ilgili yazılımları üzerinde çalışan geliştiricilere mütevazı da olsa bağış yapmayı düşünün. BTC kabul eden kuruluşlara da bağışta bulunabilirsiniz. Toksik UTXO'larınızı yönetmek çok karmaşık görünüyorsa, bağış yaparak onlardan kurtulabilirsiniz;
- Hediye kartları satın alın:** [Bitrefill] (https://www.bitrefill.com/) gibi platformlar, çeşitli satıcılarda kullanılabilecek hediye kartları için Exchange bitcoin almanıza olanak tanır. Bu, ilgili değeri kaybetmeden toksik UTXO'larınızdan kurtulmanın bir yolu olabilir;
- Onları Monero'da birleştirin:** Samourai Wallet artık BTC ve XMR arasında bir atomik takas hizmeti sunuyor. Bu, toksik UTXO'ları Bitcoin'e geri göndermeden önce KYC aracılığıyla gizliliğinizden ödün vermeden Monero'da konsolide ederek yönetmek için idealdir. Ancak bu seçenek, likidite kısıtlamaları nedeniyle Mining ücretleri ve prim açısından maliyetli olabilir;
- Bunları Lightning Network'e gönderin:** Düşük işlem ücretlerinden yararlanmak için bu UTXO'ları Lightning Network'e aktarmak ilginç olabilecek bir seçenektir. Ancak, bu yöntem Lightning kullanımınıza bağlı olarak belirli bilgileri açığa çıkarabilir ve bu nedenle dikkatli bir şekilde uygulanmalıdır.


Bu farklı tekniklerin uygulanmasına ilişkin ayrıntılı eğitimler yakında PlanB Network'te sunulacaktır.


**Ek kaynaklar:**

[Samourai Wallet video tutorial](https://planb.network/tutorials/Wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Samourai Wallet Dokümantasyonu - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Coinjoins üzerine Twitter dizisi](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Coinjoins üzerine blog yazısı](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).