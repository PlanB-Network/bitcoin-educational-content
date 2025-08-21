---
name: OXT - Zincir Analizi
description: Bitcoin'da zincir analizinin temellerinde uzmanlaşın
---
![cover](assets/cover.webp)


***UYARI:** Samourai Wallet'ün kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından, **OXT.me web sitesine şu anda erişilemiyor**. Bununla birlikte, bu aracın önümüzdeki haftalarda yeniden piyasaya sürülmesi olasılığı devam etmektedir. Bu arada, Bitcoin üzerinde zincir analizinin temellerini anlamak için bu eğitimden yararlanabilirsiniz. Burada sunulan tüm sezgisel yöntemler ve modeller Bitcoin işlemleri için geçerli olmaya devam etmektedir. Bu araçlar OXT'den daha az optimize edilmiş olsa da, bu makalenin teorik kavramlarını uygulamaya koymak için geçici olarak [Mempool.space](https://Mempool.space/) veya [Bitcoin Explorer](https://bitcoinexplorer.org/) kullanabilirsiniz.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

Bu makalede, Bitcoin üzerinde temel zincir analizlerine başlamak ve daha da önemlisi sizi gözlemleyenlerin nasıl çalıştığını anlamak için gereken temel teorik temelleri öğreneceksiniz. Her ne kadar bu makale OXT aracı hakkında pratik bir eğitim olmasa da (gelecekteki bir eğitimde ele alacağımız bir konu), kullanımı için bir dizi önemli bilgiyi derlemektedir. Sunulan her model, metrik ve gösterge için, OXT'deki örnek bir işlemin bağlantısı verilmiştir, bu da kullanımını daha iyi anlamanıza ve okumanızın yanı sıra pratik yapmanıza olanak tanıyacaktır.


## Giriş

Paranın işlevlerinden biri de isteklerin çifte tesadüfü sorununu çözmektir. Takasa dayalı bir sistemde, bir Exchange'i tamamlamak sadece benim ihtiyacımı karşılayan bir malı teklif eden bir kişiyi bulmayı değil, aynı zamanda ona kendi ihtiyacını karşılayan eşdeğer değerde bir mal sağlamayı da gerektirir. Bu dengeyi bulmak karmaşık bir iş. Bu nedenle, değeri hem mekânda hem de zamanda hareket ettirmemizi sağlayan paraya başvuruyoruz.


Paranın bu sorunu çözebilmesi için, bir mal veya hizmet sağlayan tarafın bu meblağı daha sonra harcayabileceğine ikna olması şarttır. Dolayısıyla, ister dijital ister fiziksel olsun, bir para parçasını kabul etmek isteyen her rasyonel birey, bunun iki temel kriteri karşıladığından emin olacaktır:


- Coin sağlam ve orijinal olmalıdır;
- ve iki kez harcanmamalıdır.


Eğer fiziksel para kullanıyorsak, bu ilk özellik ileri sürülmesi en karmaşık olan özelliktir. Tarihin farklı dönemlerinde, metal sikkelerin bütünlüğü genellikle kırpma veya delme gibi uygulamalardan etkilenmiştir. Örneğin, antik Roma döneminde vatandaşların altın sikkelerin kenarlarını kazıyarak bir miktar değerli metal toplaması ve bunu yaparken de gelecekteki işlemler için saklaması yaygındı. Bu nedenle daha sonra sikkelerin kenarlarına yivler açılmıştır. Orijinallik aynı zamanda fiziksel bir parasal araç üzerinde doğrulanması zor bir özelliktir. Günümüzde sahtecilikle mücadele teknikleri giderek daha karmaşık hale gelmekte ve tüccarları pahalı doğrulama sistemlerine yatırım yapmaya zorlamaktadır.


Öte yandan, doğaları gereği, çifte harcama fiziksel para birimleri için bir sorun değildir. Size 10 €'luk bir banknot verirsem, geri dönülemez bir şekilde benim mülkiyetimden çıkıp sizin mülkiyetinize girer ve böylece temsil ettiği parasal birimlerin birden fazla harcanması olasılığını ortadan kaldırır.

Dijital para birimi için zorluk farklıdır. Bir Coin'nin gerçekliğini ve bütünlüğünü sağlamak genellikle daha basittir, ancak çifte harcamanın olmamasını sağlamak daha karmaşıktır. Her dijital mal esasen bilgidir. Fiziksel malların aksine, bilgi değiş tokuş sırasında bölünmez ancak çoğalarak yayılır. Örneğin, size e-posta ile bir belge gönderirsem, bu belge daha sonra çoğaltılır. Sizin tarafınızda, orijinal belgeyi sildiğimi kesin olarak doğrulayamazsınız.


Dijital bir malın bu şekilde çoğaltılmasını önlemenin tek yolu, sistemdeki tüm borsalardan haberdar olmaktır. Bu şekilde kimin neye sahip olduğu bilinebilir ve yapılan işlemlere göre herkesin hesabı güncellenebilir. Örneğin kutsal para ile yapılan budur. Bir tüccara kredi kartıyla 10 € ödediğinizde, banka bu Exchange'i not eder ve Ledger'u günceller.


Bitcoin'da çifte harcamanın önlenmesi de aynı şekilde yapılır. Söz konusu madeni paraların daha önce harcanmış olduğu bir işlemin olmadığını teyit etmeye çalışır. Eğer bunlar hiç kullanılmamışsa, o zaman çifte harcama olmayacağından emin olabiliriz. Bu, Beyaz Kitap'ta Satoshi Nakamoto'nun ünlü ifadesidir: "*Bir işlemin olmadığını teyit etmenin tek yolu tüm işlemlerden haberdar olmaktır.*"


Bankacılık modelinin aksine, Bitcoin'de merkezi bir varlığa güvenmek zorunda kalmak istemiyoruz. Bu nedenle, tüm kullanıcılar üçüncü bir tarafa güvenmeden bu çifte harcamanın olmadığını teyit edebilmelidir. Bu nedenle, herkes tüm Bitcoin işlemlerinden haberdar olmalıdır.


Bitcoin'te mahremiyetin korunmasını zorlaştıran da tam olarak bu kamuya açık bilgi yayımıdır. Geleneksel bankacılık sisteminde, teorik olarak, yapılan işlemlerden sadece finans kurumu haberdardır. Ancak Bitcoin'te tüm kullanıcılar kendi düğümleri aracılığıyla tüm işlemlerden haberdar olurlar.


Yayılma üzerindeki bu kısıtlama nedeniyle, Bitcoin'ün gizlilik modeli bankacılık sisteminden farklıdır. İkincisinde, işlemler kullanıcının kimliğiyle ilişkilendirilir, ancak güvenilir üçüncü taraf ile halk arasındaki bilgi akışı kesilir. Başka bir deyişle, bankacınız her sabah yerel fırından baget aldığınızı bilir, ancak komşunuz tüm bu işlemlerden haberdar değildir. Bitcoin durumunda, işlemler ve kamusal alan arasındaki bilgi akışı kesilemediğinden, gizlilik modeli kullanıcının kimliğini işlemlerin kendisinden ayırmaya dayanır.

![analysis](assets/en/1.webp)

*Beyaz Kitap'taki Satoshi Nakamoto'nun diyagramından esinlenilmiştir: Bitcoin: Eşler Arası Elektronik Nakit Sistemi, bölüm 10 "Gizlilik".*

Bitcoin işlemleri kamuya açık olduğundan, ilgili taraflar hakkında bilgi çıkarmak için bunlar arasında bağlantılar kurmak mümkün hale gelir. Hatta bu faaliyet, genellikle "zincir analizi" olarak adlandırılan başlı başına bir uzmanlık alanı oluşturmaktadır. Bu makalede, bitcoinlerinizin nasıl takip edildiğini anlamak için sizi zincir analizinin temellerini keşfetmeye davet ediyorum.


Zincir analizi konusunda uzmanlaşmış şirketlerin çoğu kara kutu olarak faaliyet göstermekte ve metodolojilerini açıklamamaktadır. Bu nedenle bu uygulama hakkında bilgi edinmek zordur. Bu makalenin yazımı için esas olarak mevcut birkaç açık kaynağa dayandım:


- Makalemin büyük kısmı, Samourai Wallet tarafından 2021 yılında üretilen [Understanding Bitcoin Privacy with OXT] (https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923) adlı dört makalelik seriden alınmıştır;
- Ayrıca [OXT Research]'ün (https://medium.com/oxt-research) çeşitli raporlarının yanı sıra ücretsiz zincir analiz aracını da kullandım;
- Daha geniş anlamda, bilgim [@LaurentMT](https://twitter.com/LaurentMT) ve [@ErgoBTC](https://twitter.com/ErgoBTC)'den gelen farklı tweetler ve içeriklerden geliyor;
- Ayrıca [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___) ve [@LaurentMT](https://twitter.com/LaurentMT) ile birlikte katıldığım [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji)'dan da ilham aldım.


Yazarlarına, geliştiricilerine ve yapımcılarına teşekkür etmek isterim. Onların çeşitli içerikleri ve yazılımları olmasaydı, bu makale var olamazdı. Ayrıca bu metni titizlikle düzelten ve uzman tavsiyeleriyle beni onurlandıran hakemlere de teşekkür ederim:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*Bilginiz olsun diye, bazı terimleri tanımlamak için makalenin sonuna teknik bir mini sözlük ekledim. Anlamadığınız bir kelimeyi yıldız işaretiyle görürseniz, tanımı sayfanın altındadır.*


## Zincir analizi nedir?

Zincir analizi, Blockchain üzerindeki Bitcoin akışlarının izlenmesine yönelik tüm yöntemleri kapsayan bir uygulamadır. Genel olarak zincir analizi, önceki işlemlerin örneklerindeki özelliklerin gözlemlenmesine dayanır. Daha sonra, analiz edilmek istenen bir işlemde aynı özelliklerin tanımlanmasını ve makul yorumların çıkarılmasını içerir. Yeterince iyi bir çözüm bulmak için pratik bir yaklaşıma dayanan bu problem çözme yöntemi sezgisel olarak adlandırılır.


Basitleştirmek için, zincir analizi iki ana adımda yapılır:

1. Bilinen özelliklerin tanımlanması;

2. Hipotezlerin çıkarımı.


Zincir analizinin amaçlarından biri, Bitcoin üzerindeki çeşitli faaliyetleri gruplandırarak bunları gerçekleştiren kullanıcının benzersizliğini belirlemektir. Daha sonra, bu faaliyetler demetini gerçek bir kimlikle ilişkilendirmeye çalışmak mümkün olacaktır.


Giriş bölümümü hatırlayın. Bitcoin'ün gizlilik modelinin neden başlangıçta kullanıcının kimliğini işlemlerinden ayırmaya dayandığını açıklamıştım. Bu nedenle, zincir analizinin gereksiz olduğunu düşünmek cazip gelebilir, çünkü On-Chain faaliyetlerini gruplandırmayı başarsak bile, bunlar gerçek bir kimlikle ilişkilendirilemez. Teorik olarak bu ifade doğrudur. Kriptografik anahtar çiftleri UTXO'lar üzerinde koşullar oluşturmak için kullanılır. Özü itibariyle bu anahtar çiftleri, sahiplerinin kimliği hakkında herhangi bir bilgi ifşa etmez. Dolayısıyla, farklı anahtar çiftleriyle ilişkili faaliyetleri gruplandırmayı başarsak bile, bu bize bu faaliyetlerin arkasındaki varlık hakkında hiçbir şey söylemez.


Ancak pratik gerçeklik çok daha karmaşıktır. Gerçek bir kimliği bir On-Chain faaliyetine bağlama riski taşıyan çok sayıda davranış vardır. Analizde buna giriş noktası denir ve bunlardan çok sayıda vardır. Elbette en yaygın olanı KYC'dir (Müşterini Tanı). Bitcoinlerinizi düzenlenmiş bir platformdan kişisel alıcı adreslerinizden birine çekerseniz, bazı kişiler kimliğinizi bu Address ile ilişkilendirebilir. Daha geniş anlamda, bir giriş noktası gerçek hayatınız ile bir Bitcoin işlemi arasındaki herhangi bir etkileşim şekli olabilir. Örneğin, sosyal ağlarınızda bir alıcı Address yayınlarsanız, bu analiz için bir giriş noktası olabilir. Fırıncınıza bitcoin ile ödeme yaparsanız, yüzünüzü (kimliğinizin bir parçası olan) bir Bitcoin Address ile ilişkilendirebilirler.

Bitcoin kullanılırken bu giriş noktaları neredeyse kaçınılmazdır. Her ne kadar kapsamları sınırlandırılmaya çalışılsa da, mevcut olmaya devam edeceklerdir. Bu nedenle gizliliğinizi korumaya yönelik yöntemleri birleştirmek çok önemlidir. Gerçek kimliğiniz ile işlemleriniz arasında kabul edilebilir bir ayrım sağlamak övgüye değer bir yaklaşım olsa da yetersiz kalmaktadır. Gerçekten de, tüm On-Chain faaliyetleriniz bir arada gruplandırılabilirse, en küçük giriş noktası bile oluşturduğunuz tek Layer gizliliğini tehlikeye atabilir.


Bu nedenle, Bitcoin kullanımımızda zincir analizi ile de ilgilenmek gerekir. Bunu yaparak faaliyetlerimizin toplanmasını en aza indirebilir ve bir giriş noktasının mahremiyetimiz üzerindeki etkisini sınırlayabiliriz. Zincir analizine daha iyi karşı koymak için, zincir analizinde kullanılan yöntemlere aşina olmaktan daha iyi bir yaklaşım olabilir mi? Bitcoin'te gizliliğinizi nasıl geliştireceğinizi bilmek istiyorsanız, bu yöntemleri anlamanız gerekir. Bu, [CoinJoin](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef) veya [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) gibi teknikleri daha iyi kavramanızı ve yapabileceğiniz hataları azaltmanızı sağlayacaktır.


Bu konuda kriptografi ve kriptanaliz ile bir analoji kurabiliriz. İyi bir kriptograf her şeyden önce iyi bir kriptanalisttir. Yeni bir şifreleme algoritması hayal etmek için, hangi saldırılarla karşılaşacağını bilmek ve önceki algoritmaların neden kırıldığını incelemek gerekir. Aynı prensip Bitcoin'da gizlilik için de geçerlidir. Zincirleme analiz yöntemlerini anlamak, buna karşı korunmanın anahtarıdır. Bu yüzden size bu makaleyi sunuyorum.


Zincir analizinin kesin bir bilim olmadığını anlamak çok önemlidir. Önceki gözlemlerden veya mantıksal yorumlardan türetilen sezgisel kurallara dayanır. Bu kurallar oldukça güvenilir sonuçlar elde edilmesini sağlar, ancak asla mutlak kesinlikte değildir. Başka bir deyişle, zincir analizi, varılan sonuçlarda her zaman bir olasılık boyutu içerir. İki adresin aynı varlığa ait olduğunu az çok kesin olarak tahmin edebiliriz, ancak tam kesinlik her zaman ulaşılamaz olacaktır.


Zincirleme analizin tüm amacı, hata riskini en aza indirmek için çeşitli sezgisel yöntemlerin bir araya getirilmesinde yatmaktadır. Bu, bir bakıma, gerçeğe yaklaşmamızı sağlayan bir kanıt birikimidir.


Bu ünlü sezgisel yöntemler, birlikte detaylandıracağımız farklı kategorilerde gruplandırılabilir:


- İşlem modelleri (veya işlem modelleri);
- İşlem için dahili sezgisel yöntemler;
- İşlem için harici sezgisel yöntemler.


Bitcoin'deki ilk iki sezgisel yöntemin Satoshi Nakamoto'nun kendisi tarafından formüle edildiğini belirtmek gerekir. Bunları Beyaz Kitap'ın 10. bölümünde tartışmaktadır. Daha sonra göreceğimiz gibi, bu iki sezgisel yöntemin bugün hala zincir analizinde üstünlüğünü koruduğunu gözlemlemek ilginçtir. Bunlar:


- ortak Girdi Ownership Sezgisel (CIOH);
- ve Address'ın yeniden kullanımı.


Gözlemlenebilir özellikleri ve bir analiz yapmak için çıkarılabilecek yorumları birlikte inceleyelim.


## İşlem kalıpları (veya işlem modelleri)

Bir işlem kalıbı basitçe Blockchain'de bulunabilen ve yorumu muhtemelen bilinen tipik bir işlem modelidir. Kalıpları incelerken, yüksek düzeyde analiz edeceğimiz tek bir işleme odaklanacağız. Başka bir deyişle, daha spesifik detaylar ya da çevre üzerinde durmadan sadece girdi ve çıktıların sayısına bakacağız. Gözlemlenen modelden, işlemin doğasını yorumlayabileceğiz. Daha sonra yapısı hakkında özellikler arayacak ve bir yorum çıkaracağız.


### Basit gönderim (veya basit ödeme)

Bu model, bir veya daha fazla UTXO'nun girdi olarak tüketimi ve iki UTXO'nun çıktı olarak üretimi ile karakterize edilir.


![analysis](assets/en/2.webp)


Bu modelin yorumu, bir gönderme veya ödeme işleminin varlığında olduğumuzdur. Kullanıcı, çıktıda bir ödeme UTXO ve bir değişiklik UTXO (aynı kullanıcıya geri gelen değişiklik) karşılamak için girdi olarak kendi UTXO'larını tüketmiştir. Bu nedenle, gözlemlenen kullanıcının muhtemelen artık çıktıdaki iki UTXO'dan birine (ödeme olan) sahip olmadığını, ancak diğer UTXO'ye (değişiklik olan) hala sahip olduğunu biliyoruz.


Bu noktada, hangi çıktının hangi UTXO'ü temsil ettiğini belirtmemiz mümkün değildir, çünkü bu modelin amacı bu değildir. Bunu, bir sonraki bölümde inceleyeceğimiz sezgisel yöntemlere dayanarak yapabileceğiz. Bu aşamada amacımız, söz konusu işlemin niteliğini belirlemekle sınırlıdır; bu durumda bu işlem basit bir göndermedir.


Örneğin, burada basit gönderme modelini benimseyen bir Bitcoin işlemi yer almaktadır:

### Süpürme (İngilizce'de "sweep")

Bu model, girdi olarak tek bir UTXO tüketimi ve çıktı olarak tek bir UTXO üretimi ile karakterize edilir.


![analysis](assets/en/3.webp)


Bu modelin yorumu, bir öz-transferin varlığında olduğumuzdur. Kullanıcı bitcoinlerini kendilerine, sahip oldukları başka bir Address'ya transfer etmiştir. Aslında, işlemde herhangi bir değişiklik olmadığından, bir ödeme ile karşı karşıya olmamız pek olası değildir. Bu durumda, gözlemlenen kullanıcının muhtemelen hala bu UTXO'ye sahip olduğunu biliyoruz.


Örneğin, burada süpürme modelini benimseyen bir Bitcoin işlemi bulunmaktadır:

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Bununla birlikte, bu tür bir model, bir Exchange hesabına (kripto para birimi Exchange platformu) kendi kendine yapılan bir transferi de ortaya çıkarabilir. Bilinen adreslerin incelenmesi ve işlemin bağlamı, bunun kendi kendine saklanan bir Wallet'e bir süpürme mi yoksa bir platforma para çekme mi olduğunu bilmemizi sağlayacaktır.


### Konsolidasyon

Bu model, girdi olarak birkaç UTXO tüketimi ve çıktı olarak tek bir UTXO üretimi ile karakterize edilir.


![analysis](assets/en/4.webp)


Bu modelin yorumu, bir konsolidasyonun var olduğu yönündedir. Bu, işlem ücretlerinde olası bir artış beklentisiyle birkaç UTXO'yu birleştirmeyi amaçlayan Bitcoin kullanıcıları arasında yaygın bir uygulamadır. Bu işlemi ücretlerin düşük olduğu bir dönemde gerçekleştirerek, gelecekteki ücretlerden tasarruf etmek mümkündür.


Bu işlemin arkasındaki kullanıcının muhtemelen girdideki tüm UTXO'lara sahip olduğu ve çıktıdaki UTXO'e hala sahip olduğu sonucuna varabiliriz. Bu nedenle, bu kesinlikle bir öz transferdir.


Tıpkı süpürme işleminde olduğu gibi, bu tür bir model de bir Exchange hesabına yapılan bir öz transferi ortaya çıkarabilir. Bilinen adreslerin incelenmesi ve işlemin bağlamı, bunun bir öz saklama Wallet'ya bir konsolidasyon mu yoksa bir platforma para çekme mi olduğunu anlamamızı sağlayacaktır.


Örneğin, burada konsolidasyon modelini benimseyen bir Bitcoin işlemi bulunmaktadır:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Toplu Harcama Modeli

Bu model, girdi olarak birkaç UTXO tüketimi (genellikle sadece bir tane) ve çıktı olarak birçok UTXO üretimi ile karakterize edilir.


![analysis](assets/en/5.webp)


Bu modelin yorumu, bir toplu harcamanın varlığında olduğumuzdur. Bu, örneğin Exchange gibi önemli bir ekonomik faaliyeti ortaya çıkarması muhtemel bir uygulamadır. Toplu harcama, bu kuruluşların harcamalarını tek bir işlemde birleştirerek ücretlerden tasarruf etmelerini sağlar.


UTXO girdisinin önemli ekonomik faaliyeti olan bir şirketten geldiği ve UTXO'ların çıktılarının dağılacağı sonucuna varabiliriz. Bazıları şirketin müşterilerine ait olacaktır. Diğerleri ortak şirketlere gidebilir. Son olarak, kesinlikle ihraç eden şirkete geri dönen bir değişiklik olacaktır.


Örneğin, burada toplu harcama modelini benimseyen bir Bitcoin işlemi bulunmaktadır:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Protokole Özel İşlemler

İşlem modelleri arasında, belirli bir protokolün kullanıldığını ortaya koyan modelleri de belirleyebiliriz. Örneğin, Whirlpool coinjoins, diğer klasik işlemlerden ayırt edilmelerini sağlayan kolayca tanımlanabilir bir yapıya sahip olacaktır.


![analysis](assets/en/6.webp)


Bu örüntünün analizi, muhtemelen işbirliğine dayalı bir işlemin varlığına işaret etmektedir. Bir CoinJoin gözlemlemek de mümkündür. Bu ikinci hipotezin doğru olduğu kanıtlanırsa, çıktıların sayısı bize katılımcıların sayısı hakkında yaklaşık bir tahmin sağlayabilir.


Örneğin, burada CoinJoin işbirlikçi işlem türünün modelini benimseyen bir Bitcoin işlemi bulunmaktadır:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Kendine özgü yapıları olan başka birçok protokol vardır. Böylece, örneğin Wabisabi tipi işlemleri veya Stamps işlemlerini ayırt edebiliriz.


## Dahili İşlem Sezgiselleri

İçsel sezgisel, bir işlemin kendi içinde, çevresini incelemeye gerek kalmadan tanımlanan ve çıkarımlar yapmamızı sağlayan belirli bir özelliktir. İşlemin genel yapısına odaklanan kalıpların aksine, iç sezgiseller çıkarılabilir veri kümesine dayanır. Buna şunlar dahildir:


- Hem gelen hem de giden farklı UTXO'ların miktarları;
- Komut dosyalarıyla ilgili her şey: adres alma, sürüm oluşturma, kilitlenme süreleri...


Genel olarak, bu tür bir sezgisel yöntem belirli bir işlemdeki değişikliği tanımlamamızı sağlar. Bunu yaparak, daha sonra bir varlığı birden fazla farklı işlem boyunca izlemeye devam edebiliriz.


Bir kez daha hatırlatmak isterim ki bu sezgisel yöntemler kesinlikle kesin değildir. Tek tek ele alındıklarında, sadece makul senaryoları belirlememizi sağlarlar. Belirsizliği hiçbir zaman tamamen ortadan kaldırmadan azaltmaya katkıda bulunan, çeşitli sezgisel yöntemlerin birikimidir.


### İç Benzerlikler

Bu sezgisel yöntem, aynı işlemin girdileri ve çıktıları arasındaki benzerliklerin incelenmesini içerir. İşlemin girdilerinde ve çıktılarından sadece birinde aynı özellik gözlemleniyorsa, bu çıktının değişikliği oluşturması muhtemeldir.


En belirgin özellik, bir alıcı Address'in aynı işlemde yeniden kullanılmasıdır.


![analysis](assets/en/7.webp)


Bu sezgisel yöntem şüpheye çok az yer bırakır. Özel anahtarları ele geçirilmediği sürece, aynı alıcı Address kaçınılmaz olarak tek bir kullanıcının faaliyetini ortaya çıkarır. Bunu takip eden yorum, işlem değişikliğinin girdi olarak aynı Address ile çıktı olduğudur. Bu, bu değişiklikten bireyi izlemeye devam etmemizi sağlar.


Örneğin, bu sezgisel yöntemin muhtemelen uygulanabileceği bir işlem aşağıda verilmiştir:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Girdiler ve çıktılar arasındaki bu benzerlikler Address'in yeniden kullanımıyla sınırlı değildir. Komut dosyalarının kullanımındaki herhangi bir benzerlik bir sezgiselin uygulanmasına izin verebilir. Örneğin, bazen bir girdi ile işlemin çıktılarından biri arasında aynı sürümleme gözlemlenebilir.


![analysis](assets/en/8.webp)

Bu diyagramda, 0 numaralı girdinin bir P2WPKH komut dosyasını ("bc1q" ile başlayan SegWit V0) açtığını görebiliriz. 0 numaralı çıktı da aynı türde bir komut dosyası kullanır. Ancak, 1 numaralı çıktı bir P2TR komut dosyası kullanır ("bc1p" ile başlayan SegWit V1). Bu özelliğin yorumu, girdi ile aynı sürümlendirmeye sahip Address'nin muhtemelen Address değişikliği olduğudur. Bu nedenle hala aynı kullanıcıya ait olacaktır.

İşte bu sezgisel yöntemin muhtemelen uygulanabileceği bir işlem:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


Bu işlemde, 0 numaralı girdi ve 1 numaralı çıktının P2WPKH komut dosyalarını (SegWit V0) kullandığını, 0 numaralı çıktının ise farklı bir komut dosyası türü olan P2PKH (Legacy) kullandığını görebiliriz.


### Yuvarlak Sayı Ödemeleri

Değişikliği belirlememize yardımcı olabilecek bir diğer içsel sezgisel de yuvarlak sayıdır. Genel olarak, basit bir ödeme modeliyle (1 girdi ve 2 çıktı) karşılaşıldığında, çıktılardan biri yuvarlak bir miktar harcıyorsa, bu ödemeyi temsil eder.


![analysis](assets/en/9.webp)


Eleme sürecine göre, bir çıktı ödemeyi temsil ediyorsa, diğeri değişikliği temsil etmektedir. Bu nedenle, girdideki kullanıcının hala değişiklik olarak tanımlanan çıktıya sahip olmasının muhtemel olduğu yorumunu yapabiliriz.


Ödemelerin çoğunluğu hala itibari para birimleriyle yapıldığından, bu sezgisel yöntemin her zaman geçerli olmadığı unutulmamalıdır. Gerçekten de, Fransa'daki bir tüccar Bitcoin kabul ettiğinde, genellikle Sats cinsinden sabit fiyatlar göstermezler. Bunun yerine, Euro cinsinden fiyat ile ödenecek bitcoin miktarı arasında bir dönüşüm yapmayı tercih ederler. Bu nedenle, işlem çıktısında yuvarlak bir sayı olmamalıdır. Bununla birlikte, bir analist, işlem ağda yayınlandığında geçerli olan Exchange oranını dikkate alarak bu dönüşümü gerçekleştirmeyi deneyebilir.


Eğer bir gün Bitcoin borsalarımızda tercih edilen hesap birimi haline gelirse, bu sezgisel yöntem analiz için daha da kullanışlı hale gelebilir.


Örneğin, bu sezgisel yöntemin muhtemelen uygulanabileceği bir işlem aşağıda verilmiştir:

### Büyük Harcama


Basit bir ödeme modelinde iki işlem çıktısı arasında yeterince büyük bir fark tespit edildiğinde, daha büyük olan çıktının muhtemelen değişim olduğu tahmin edilebilir.


![analysis](assets/en/10.webp)


En büyük çıktının bu sezgiselliği muhtemelen en kesin olmayanıdır. Tek başına tanımlandığında oldukça zayıftır. Ancak bu özellik, yorumumuzun belirsizliğini azaltmak için diğer sezgisel yöntemlerle birleştirilebilir.


Örneğin, yuvarlak tutarlı bir çıktı ve daha büyük tutarlı başka bir çıktı içeren bir işlemi incelersek, yuvarlak ödemeler sezgiselinin ve en büyük çıktıya ilişkin sezgiselin birlikte uygulanması belirsizlik düzeyimizi azaltmamızı sağlar.


Örneğin, burada bu sezgisel yöntemin uygulanabileceği bir işlem söz konusudur:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## İşlem için Harici Sezgisel Yöntemler

Harici sezgisel yöntemlerin incelenmesi, işlemin kendisine özgü olmayan belirli Elements'ün benzerliklerinin, kalıplarının ve özelliklerinin analiz edilmesidir. Başka bir deyişle, daha önce kendimizi içsel sezgisel yöntemlerle işleme özgü Elements'ten yararlanmakla sınırlandırdıysak, şimdi dışsal sezgisel yöntemler sayesinde analiz alanımızı işlemin çevresine doğru genişletiyoruz.


### Address Yeniden Kullanım

Bu, Bitcoin kullanıcıları arasında en iyi bilinen sezgisel yöntemlerden biridir. Address'nın yeniden kullanımı, farklı işlemler ve farklı UTXO'lar arasında bir bağlantı kurulmasını sağlar. Bitcoin alan bir Address birden fazla kez kullanıldığında gözlemlenir.


Address'in yeniden kullanımının yorumu, bu Address'e kilitlenen tüm UTXO'ların aynı varlığa ait olduğu (veya ait olduğu) şeklindedir. Bu sezgisel yöntem belirsizliğe çok az yer bırakır. Tanımlandığında, takip eden yorumun gerçekliğe karşılık gelme şansı yüksektir.

Giriş bölümünde açıklandığı üzere, bu sezgisel yöntem bizzat Satoshi Nakamoto tarafından keşfedilmiştir. Beyaz Kitap'ta, kullanıcıların bunu üretmesini önlemek için her yeni işlem için yeni bir Address kullanmak olan bir çözümden özellikle bahsetmektedir: "*Ek bir güvenlik duvarı olarak, her işlem için yeni bir anahtar çifti kullanılarak işlemlerin ortak bir sahiple bağlantılı olmaması sağlanabilir."


Örneğin, burada birden fazla işlemde yeniden kullanılan bir Address bulunmaktadır:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### Yazıların ve Wallet Parmak İzlerinin Benzerliği

Address'in yeniden kullanımının ötesinde, eylemleri aynı Wallet'ya veya bir adres kümesine bağlayabilen başka birçok sezgisel yöntem vardır.


İlk olarak, bir analist komut dosyası kullanımındaki benzerlikleri kullanabilir. Örneğin, Multisig gibi bazı azınlık scriptleri SegWit V0 scriptlerinden daha kolay tespit edilebilir. Saklandığımız grup ne kadar büyükse, bizi tespit etmek o kadar zor olur. CoinJoin Whirlpool protokolünde tüm katılımcıların tamamen aynı türde komut dosyası kullanmasının nedeni de budur.


Daha geniş anlamda, bir analist bir Wallet'in karakteristik parmak izlerine de odaklanabilir. Bunlar, izleme sezgiselleri olarak kullanılmak üzere tanımlanmaya çalışılabilecek bir kullanıma özgü süreçlerdir. Diğer bir deyişle, izlenen tüzel kişiye atfedilen işlemlerde aynı iç özelliklerin biriktiği gözlemlenirse, diğer işlemlerde de aynı özellikler tespit edilmeye çalışılabilir.


Örneğin, izlenen kullanıcının değişikliklerini sistematik olarak P2TR* adreslerine (bc1p...) gönderdiği tespit edilebilir. Bu işlem tekrarlanırsa, analizimizin devamı için bir sezgisel olarak kullanılabilir. UTXO'ların sırası, değişikliğin çıktılardaki yerleşimi, RBF (Replace-by-fee) sinyali, hatta sürüm numarası ve kilitlenme süresi gibi diğer parmak izleri de kullanılabilir.

LaurentMT](https://twitter.com/LaurentMT)'nin [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji)'da (Frankofon bir podcast) belirttiği gibi, Wallet parmak izlerinin zincir analizindeki faydası zaman içinde önemli ölçüde artmaktadır. Gerçekten de, artan senaryo türü sayısı ve bu yeni özelliklerin Wallet yazılımı tarafından giderek daha kademeli olarak kullanılması farklılıkları vurgulamaktadır. Hatta izlenen varlık tarafından kullanılan yazılımın doğru bir şekilde tespit edilebildiği de olmaktadır. Bu nedenle, bir Wallet'in parmak izinin incelenmesinin, 2010'ların başında başlatılan işlemlerden ziyade, özellikle yakın tarihli işlemlerle ilgili olduğunu anlamak önemlidir.

Özetlemek gerekirse, bir parmak izi, Wallet tarafından otomatik olarak veya kullanıcı tarafından manuel olarak gerçekleştirilen ve analizimize yardımcı olmak için diğer işlemlerde bulunabilecek herhangi bir özel uygulama olabilir.


### CIOH

"Girdilerin ortak Ownership sezgiselliği" veya "ortak harcama sezgiselliği" olarak çevrilebilecek olan CIOH, "Ortak Girdi Ownership Sezgiselliği" için, bir işlemin birden fazla girdisi olduğunda, bunların muhtemelen tek bir varlıktan geldiğini belirten bir sezgiseldir. Sonuç olarak, Ownership'leri ortaktır.


CIOH'u uygulamak için öncelikle birden fazla girdisi olan bir işlem gözlemlenir. Bu iki girdi olabileceği gibi otuz girdi de olabilir. Bu özellik tespit edildikten sonra, işlemin bilinen bir kalıba uyup uymadığı kontrol edilir. Örneğin, kabaca aynı miktarda 5 girdisi ve tam olarak aynı miktarda 5 çıktısı varsa, bunun bir CoinJoin Whirlpool yapısı olduğunu biliriz. Bu nedenle CIOH uygulanamaz.


Bununla birlikte, işlem bilinen herhangi bir işbirlikçi işlem modeline uymuyorsa, tüm girdilerin muhtemelen aynı varlıktan geldiği şeklinde yorumlanabilir. Bu, halihazırda bilinen bir kümeyi genişletmek veya izlemeye devam etmek için çok faydalı olabilir.


![analysis](assets/en/11.webp)


CIOH, Satoshi Nakamoto tarafından keşfedilmiştir. Beyaz Kitap'ın 10. bölümünde bunu tartışmaktadır: "*[...] bağlantı, girdilerinin aynı sahibine ait olduğunu zorunlu olarak ortaya çıkaran çok girdili işlemlerde kaçınılmazdır. Risk, bir anahtarın sahibi ortaya çıkarsa, bağlantıların aynı sahibine ait diğer işlemleri ortaya çıkarabilmesidir.*"

Satoshi Nakamoto'nun, Bitcoin'nin resmi olarak piyasaya sürülmesinden önce bile, kullanıcılar için iki ana gizlilik açığını, yani CIOH ve Address'in yeniden kullanımını zaten tanımlamış olduğunu belirtmek özellikle etkileyicidir. Bu iki sezgisel yöntem bugün bile zincir analizinde en faydalı yöntem olmaya devam ettiğinden, bu tür bir öngörü oldukça dikkat çekicidir.


### off-chain Verileri

Açıkçası, zincir analizi On-Chain verileriyle sınırlı değildir. Önceki bir analizden elde edilen veya internet üzerinden erişilebilen herhangi bir veri de bir analizi iyileştirmek için kullanılabilir.


Örneğin, izlenen işlemlerin sistematik olarak aynı Bitcoin düğümünden yayınlandığı gözlemlenirse ve IP'si Address tanımlanabilirse, aynı varlıktan gelen diğer işlemleri tespit etmek mümkün olabilir.


Analist ayrıca daha önce açık kaynaklı olarak yapılan analizlere veya kendi önceki analizlerine güvenme seçeneğine de sahiptir. Belki de daha önce tespit edilmiş bir adres kümesine işaret eden bir çıktı bulunabilir. Bazen, bu platformların adresleri genel olarak bilinen bir Exchange'e işaret eden çıktılara da güvenmek mümkündür.


Benzer şekilde, eleme yoluyla bir analiz gerçekleştirilebilir. Örneğin, iki çıktısı olan bir işlemin analizi sırasında, bunlardan biri izlenen varlıktan bilinen ancak farklı bir adres kümesine bağlıysa, diğer çıktının muhtemelen değişikliği temsil ettiği yorumlanabilir.


Zincir analizi aynı zamanda OSINT'in (Açık Kaynak İstihbaratı) internet aramaları ile biraz daha genel olan bir bölümünü de içerir. Bu nedenle, takma ad altında olsun ya da olmasın, alıcı adreslerinin doğrudan sosyal medyada veya bir web sitesinde yayınlanmaması tavsiye edilir.


### Zamansal Modeller

İnsanın aklına hemen gelmeyebilir, ancak bazı insan davranışları tanınabilir On-Chain. Bir çalışmada en yararlı olanı uyku düzeninizdir! Evet, uyurken muhtemelen Bitcoin işlemlerini yayınlamıyorsunuzdur. Genellikle yaklaşık aynı saatlerde uyuduğunuz için, On-Chain analizinde zamansal analizlerin kullanılması yaygındır. Bu basitçe, belirli bir varlığın işlemlerinin Bitcoin ağına yayınlandığı zamanların kaydedilmesini içerir. Bu zamansal kalıpları analiz etmek çok sayıda bilgi çıkarmamıza olanak tanır.

İlk ve en önemlisi, zamansal bir analiz bazen izlenen varlığın niteliğini belirleyebilir. İşlemlerin 24 saat boyunca tutarlı bir şekilde yayınlandığı gözlemlenirse, bu güçlü bir ekonomik faaliyete işaret edebilir. Bu işlemlerin arkasındaki kuruluş muhtemelen uluslararası ve belki de dahili olarak otomatikleştirilmiş prosedürlere sahip bir işletmedir.


Örneğin, bu örüntüyü birkaç hafta önce yanlışlıkla 19 bitcoin ücret tahsis edilen bir işlemi analiz ederken fark etmiştim. Basit bir zamansal analiz, otomatik bir hizmetle ve dolayısıyla muhtemelen Exchange gibi büyük bir kuruluşla karşı karşıya olduğumuzu varsaymamı sağlamıştı: https://twitter.com/Loic_Pandul/status/1701127409712452072


Nitekim birkaç gün sonra, fonların Paxos Exchange aracılığıyla PayPal'a ait olduğu anlaşıldı.


Tersine, zamansal örüntünün 16 belirli saate yayıldığı görülürse, o zaman bireysel bir kullanıcıyla veya değiş tokuş edilen hacimlere bağlı olarak belki de yerel bir işletmeyle karşı karşıya olduğumuz tahmin edilebilir.


Gözlemlenen varlığın doğasının ötesinde, zamansal örüntü bize kullanıcının yaklaşık konumunu da verebilir. Böylece diğer işlemleri ilişkilendirebilir ve bunların Timestamp'ünü analizimize eklenebilecek ek bir sezgisel olarak kullanabiliriz.


Örneğin, daha önce bahsettiğim birkaç kez tekrar kullanılan Address'te, ister gelen ister giden olsun, işlemlerin 13 saatlik bir aralıkta yoğunlaştığı gözlemlenebilir.

![analysis](assets/notext/12.webp)

*Kredi: OXT*


Bu aralık muhtemelen Avrupa, Afrika veya Orta Doğu'ya karşılık gelmektedir. Dolayısıyla bu işlemlerin arkasındaki kullanıcının orada yaşadığı yorumu yapılabilir.


Farklı bir kayıtta, Satoshi Nakamoto'nun Japonya'dan değil, aslında Amerika Birleşik Devletleri'nden faaliyet gösterdiği hipotezine izin veren de bu tür bir zamansal analizdir: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### Hacimlerin Analizi

Kullanılabilecek bir diğer harici sezgisel yöntem de işlem hacimlerinin analizidir. Bir işletmeye atfedilen her bir işlemde mevcut olan tutarlara dayanarak, bu bilgi analizin geri kalanı için ek bir sezgisel olarak kullanılabilir.

Bu sezgisel yöntemin oldukça zayıf olduğu açıktır, ancak diğer sezgisel yöntemlere eklendiğinde belirsizliği azaltmaya yardımcı olabilir.


## Zincirleme analize karşı kendinizi nasıl koruyabilirsiniz?

Bir Bitcoin kullanıcısı olarak, gizliliğinizi koruma hakkına sahipsiniz. Bu, herhangi bir yasal kısıtlamadan bağımsız olarak her bireyin doğasında bulunan kendinize sahip olma ve kendiniz üzerinde tasarrufta bulunma doğal haklarınızdan kaynaklanmaktadır.


Kişinin mahremiyetini korumaya yönelik bu doğal hak, İnsan Hakları Evrensel Beyannamesi'nin 12. Maddesinde yer alan "*Hiç kimse özel yaşamına, ailesine, konutuna ya da haberleşmesine keyfi olarak müdahale edilmesine, şeref ve itibarına saldırılmasına maruz bırakılamaz. Herkesin bu tür müdahale ve saldırılara karşı yasalarca korunma hakkı vardır*".


Ancak, zincir analizi konusunda uzmanlaşmış şirketlerin temel işi tam da özel alanınıza girerek yazışmalarınızın gizliliğini tehlikeye atmaktır. Yukarıda bahsi geçen hak iddiasına uygun olarak devletlerin mahremiyetimizi güçlü bir şekilde savunması umulurken, bunu yapmayı ihmal etmekle kalmıyor, aynı zamanda bu analiz şirketlerinin finansmanını da önemli ölçüde finanse ediyorlar. Yasa koyucu karşısında her türlü tavizi vermeye hazır görünen sektör derneklerinden destek ummak da boşuna olacaktır.


Fiili olarak, Bitcoin'de bu gizlilik hakkı iddiası mevcut değildir. Bu nedenle, doğal hakkınızı kullanmak ve yazışmalarınızın gizliliğini korumak size, yani kullanıcıya bağlıdır. Bu, zincir analizi için kullanılan sezgisel yöntemleri engellemenizi veya aldatmanızı sağlayacak çeşitli tekniklerin ve kullanım uygulamalarının benimsenmesini içerir.


### Sezgisel yöntemlere düşmekten kaçınma

Öncelikle, daha radikal yöntemleri değerlendirmeden önce, zincir analizi için kullanılan sezgisel yöntemlere maruz kalmamızı mümkün olduğunca sınırlandırmamız tavsiye edilir. Daha önce de belirtildiği gibi, en güçlü iki sezgisel yöntem Address yeniden kullanımı ve CoinJoin'dir.


Bitcoin'de gizliliğinizi sağlamanın temel ilkesi, Wallet'nize gelen her işlem için yeni ve temiz bir Address kullanmaktır. Address'un yeniden kullanımı Bitcoin'de gizliliğe yönelik başlıca tehdittir.

Bireysel bir kullanıcı için, gelen her ödeme için yeni bir Address oluşturmak çok basittir. Modern cüzdanlar bunu siz "Al" butonuna tıkladığınız anda otomatik olarak yapar. Bu nedenle, işlemlerinizin gizliliğine en ufak bir önem veriyorsanız, yeni adresler kullanmak minimum seviyeyi temsil eder. İnternette statik bir iletişim noktasına ihtiyacınız olursa, alıcı bir Address koymak yerine, [PayNym gibi BIP47 uygulayan] çözümleri kullanabilirsiniz (https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Daha sonra, zincir analizine karşı hareket etmek istiyorsanız, UTXO'ları bir işlemin girişinde birleştirmekten kaçının. En azından, gerçekten birleştirmeniz gerekiyorsa, aynı kaynağa sahip UTXO'ları tercih edin. Bu öneri UTXO'larınızı iyi yönetmeniz gerektiği anlamına gelir. Bitcoinlerinizi satın alırken, birleştirmek zorunda kalmadan yapabileceğiniz ödeme sayısını en üst düzeye çıkarmak için büyük miktarlar içeren transferleri tercih edin. Ayrıca, UTXO'larınızın kaynağını belirlemek ve farklı kaynaklardan birleştirme yapmaktan kaçınmak için yazılımınızda etiketlemenizi tavsiye ederim.


Daha genel olarak, diğer tüm sezgisel yöntemler için, bunlara düşmemeye çalışmak için bunları bilmeniz gerekir:


- Azınlık komut dosyalarını kullanmayın. SegWit V0 veya muhtemelen SegWit V1'i tercih edin;
- Ödemeleri yuvarlak sayılarla yapmayın. Örneğin, bir arkadaşınıza 100 bin Sats göndermeniz gerekiyorsa, ona 114,486 Sats gönderin. Karşılığında size bir içki ısmarlayacaklardır;
- Her zaman ödeme çıktısından çok daha büyük bir değişiklik yapmamaya çalışın;
- Alıcı adreslerinizi sosyal medyada paylaşmayın;
- İşlemlerinizi yayınlamak için Tor altında kendi düğümünüzü kullanın;
- Bitcoin işlemlerinizi her zaman aynı anda yayınlamamaya çalışın..


### Gizlilik araçlarını kullanma

Zincirleme analizi önlemek veya aldatmak için Bitcoin kullanımınızı belirsiz hale getiren yöntemlere de başvurabilirsiniz.


En popüler teknik şüphesiz CoinJoin'dur, aynı miktarlarda birkaç UTXO'yu harekete geçiren işbirlikçi bir işlem yapısıdır. Buradaki amaç deterministik bağlantıları kırmak, böylece günümüzden geçmişe ve geçmişten günümüze analiz yapılmasını engellemektir. CoinJoin, madeni paralarınızı ayırt edilemeyen büyük bir madeni para grubu içinde gizleyerek makul inkar edilebilirlik sağlar. CoinJoin hakkında hem teknik hem de pratik olarak daha fazla bilgi edinmek istiyorsanız, bu diğer makaleleri ve eğitimleri okumanızı öneririm:


- [CoinJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - Sparrow wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-Sparrow-Wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin, madeni paralar için makul inkar edilebilirlik yaratmak için mükemmel bir araçtır, ancak tüm kullanıcı gizliliği ihtiyaçları için optimize edilmemiştir. Özellikle, CoinJoin bir ödeme aracı olmak üzere tasarlanmamıştır. Makul inkar edilebilirlik üretimini mükemmelleştirmek için takas edilen miktarlar konusunda çok katıdır. Kişi işlem çıktılarının miktarını özgürce seçemediğinden, CoinJoin bitcoin ile ödeme yapmak için kullanılamaz.


Örneğin, gizliliğimi optimize ederken baget ekmek için bitcoin ile ödeme yapmak istediğimi düşünün. Ortaya çıkan UTXO'in miktarını CoinJoin'den seçmenin imkansızlığı göz önüne alındığında, harcama miktarımı fırıncı tarafından belirlenen fiyata göre ayarlayamayacağımı görürdüm. Bu nedenle, CoinJoin ödeme işlemleri için yetersiz kalmaktadır.


Daha özel kullanım durumlarında gizlilik ihtiyaçlarını karşılamak için başka araçlar da tasarlanmıştır. Örneğin, sadece iki katılımcıyı içeren ve ödemeye izin veren bir yapıya dayanan bir tür mini-CoinJoin olan [PayJoin] (https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) var.


PayJoin'nın benzersizliği, aslında iki kullanıcı arasında bir mini-CoinJoin olmasına rağmen sıradan görünen bir işlem üretebilmesinde yatmaktadır. Bu yapıda, işlemin alıcısı gerçek göndericinin yanında girdiler arasında yer alır. Böylece alıcı, gerçek ödemeyi kolaylaştıran işlemin içine kendisine bir ödeme ekler.


Örneğin, fırıncınızdan 10.000 Sats'lik bir UTXO'dan 6.000 Sats'e bir baget satın alırsanız ve bir PayJoin yapmak isterseniz, fırıncınız sezgiselleri aldatmak için orijinal işleminize bir girdi olarak kendilerine ait olan 15.000 Sats'lik bir UTXO ekleyecek ve bunu bir çıktı olarak tamamen geri kazanacaktır:


![analysis](assets/en/14.webp)


İşlem ücretleri, programın anlaşılmasını kolaylaştırmak için ihmal edilmiştir.


PayJoin'in hedefleri iki yönlüdür. İlk olarak, COH aracılığıyla bir tuzak oluşturarak harici bir gözlemciyi aldatmayı amaçlamaktadır. Gerçekten de, bir analist bu işlemi gözlemlediğinde, COH'u uygulayabileceğini düşünecek ve böylece farklı girdilerin ortak bir Ownership olduğunu varsayacaktır. Gerçekte bu varsayım yanlıştır, çünkü girdilerden biri göndericiye aitken diğeri alıcıya aittir. Bu nedenle, KB-161 analisti yanlış yola sevk ederek zincir analizini bozar.

PayJoin'nin ikinci amacı, çıktılarının özel yapısı sayesinde analisti işlemin gerçek tutarı konusunda aldatmaktır. Dolayısıyla PayJoin steganografi alanına girmektedir. İşlemin gerçek tutarının aldatıcı bir işlem içinde gizlenmesini sağlar.


Gerçekten de, baget satın almak için PayJoin kullanma örneğimize tekrar dönersek, dışarıdan bir gözlemci 4,000 Sats veya 21,000 Sats'lük bir ödeme ile karşı karşıya olduğumuzu düşünebilir. Gerçekte ise baget için yapılan ödeme 6.000 Sats'tür: 21.000 - 15.000 = 6.000. Dolayısıyla ödemenin gerçek değeri, zincir analizi için bir yem görevi gören sahte bir ödemenin içinde gizlidir.


PayJoin ve CoinJoin'nın ötesinde, zincir analizini bloke eden ya da aldatan başka birçok Bitcoin işlem yapısı vardır. Bunlar arasında, esnek bir mini CoinJoin yapmaya ya da esnek bir mini CoinJoin'yı taklit etmeye olanak tanıyan [Stonewall](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) ve [StonewallX2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) işlemlerinden bahsedebilirim. Ayrıca, kendine çok sayıda sahte transfer yaparak Ownership bitcoin değişimini simüle eden [Ricochet](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) işlemleri de vardır.


Tüm bu araçlar mobil cihazlarda Samourai Wallet'de ve PC'de Sparrow wallet'de mevcuttur. Bu özel işlem yapıları hakkında daha fazla bilgi edinmek istiyorsanız, eğitimlerimi keşfetmenizi tavsiye ederim:


- [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - Sparrow wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-Sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Sonuç

Zincir analizi, On-Chain bitcoinlerinin akışını izlemeye çalışmayı içeren bir uygulamadır. Bunu yapmak için analistler, az ya da çok makul hipotezler ve yorumlar çıkarmak amacıyla kalıplar ve özellikler ararlar.


Bu sezgisel yöntemlerin doğruluğu değişkenlik gösterir: bazıları diğerlerinden daha yüksek derecede kesinlik sağlar, ancak hiçbiri yanılmaz olduğunu iddia edemez. Bununla birlikte, yakınsayan birkaç sezgisel yöntemin bir araya gelmesi, bu doğal şüpheyi azaltabilir, ancak tamamen ortadan kaldırmak imkansızdır.

Bu yöntemleri üç farklı ana kategoriye ayırabiliriz:


- Kalıplar, her bir işlemin genel yapısına odaklanmıştır;
- Bir işlemin tüm ayrıntılarının bağlamına uzanmadan kapsamlı bir şekilde incelenmesine olanak tanıyan dahili sezgisel yöntemler;
- Harici sezgisel yöntemler, işlemin kendi ortamında analizinin yanı sıra içgörü sağlayabilecek her türlü harici veriyi de kapsar.


Bir Bitcoin kullanıcısı olarak, buna etkili bir şekilde karşı koymak ve böylece gizliliğinizi korumak için zincir analizinin temel ilkelerine hakim olmak çok önemlidir.


## Teknik Mini Sözlük:

**P2PKH:** Pay to Public Key Hash'ın kısaltmasıdır. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir komut dosyası modelidir. Bitcoinlerin bir açık anahtarın Hash'ına, yani bir alıcı Address'ye kilitlenmesine izin verir. Bu komut dosyası Legacy standardı ile ilişkilidir ve Bitcoin'in ilk sürümlerinde Satoshi Nakamoto tarafından tanıtılmıştır. Açık anahtarın betiğe açıkça dahil edildiği P2PK'dan farklı olarak, P2PKH açık anahtarın "alıcı Address" olarak da adlandırılan bazı meta verilerle birlikte kriptografik bir damgasını kullanır. Bu komut dosyası, açık anahtarın SHA256'sının RIPEMD160 Hash'ını içerir ve fonlara erişmek için alıcının bu Hash ile eşleşen bir açık anahtarın yanı sıra ilişkili özel anahtardan üretilen geçerli bir dijital imza sağlaması gerektiğini şart koşar. P2PKH adresleri Base58Check formatı kullanılarak kodlanır, bu da onlara bir sağlama toplamı kullanımı yoluyla yazım hatalarına karşı direnç kazandırır. Bu adresler her zaman 1 sayısı ile başlar.

**P2TR:** Taproot'e Öde ("köküne kadar öde") ifadesinin kısaltmasıdır. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modelidir. P2TR, Kasım 2021'de Taproot'in uygulanmasıyla birlikte tanıtılmıştır. Kriptografik anahtarları bir araya getirmek için Schnorr protokolünün yanı sıra MAST (Merkelized Alternative Script Tree) olarak bilinen alternatif senaryolar için Merkle ağaçlarını kullanır. Harcama koşullarının kamuya açık olduğu geleneksel işlemlerin aksine (bazen makbuzda, bazen harcamada), P2TR karmaşık senaryoların tek bir görünür açık anahtarın arkasına gizlenmesine izin verir. Teknik olarak, bir P2TR komut dosyası bitcoinleri K olarak gösterilen benzersiz bir Schnorr açık anahtarına kilitler. Ancak, bu K anahtarı aslında bir P açık anahtarı ve bir M açık anahtarının toplamıdır, ikincisi bir ScriptPubKeys listesinin Merkle Root'sinden hesaplanır. Anahtar birleştirme işlemi Schnorr imza protokolü kullanılarak gerçekleştirilir. Bir P2TR betiği ile kilitlenen Bitcoinler iki farklı şekilde harcanabilir: ya P açık anahtarı için bir imza yayınlayarak ya da Merkle Tree'te bulunan betiklerden birini yerine getirerek. İlk seçenek "anahtar yolu", ikincisi ise "komut dosyası yolu" olarak adlandırılır Böylece, P2TR kullanıcıların bitcoinleri ya bir açık anahtara ya da seçtikleri birden fazla komut dosyasına göndermelerine olanak tanır. Bu komut dosyasının bir diğer avantajı da, bir P2TR çıktısını harcamanın birden fazla yolu olmasına rağmen, harcama sırasında yalnızca kullanılanın açıklanması ve kullanılmayan alternatiflerin gizli kalmasına izin verilmesidir. Örneğin, Schnorr anahtar toplaması sayesinde, açık anahtar P'nin kendisi potansiyel olarak bir Multisig'ü temsil eden bir toplanmış anahtar olabilir. P2TR bir sürüm 1 SegWit çıktısıdır, yani P2TR girdileri için imzalar ScriptSig'de değil, bir işlemin tanığında saklanır. P2TR adresleri Bech32m kodlamasını kullanır ve bc1p ile başlar.

**P2WPKH:** Pay to Witness Public Key Hash'nin kısaltmasıdır. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir komut dosyası modelidir. P2WPKH, Ağustos 2017'de SegWit'in uygulanmasıyla birlikte tanıtılmıştır. Bu betik P2PKH'ye (Pay to Public Key Hash) benzer, çünkü o da bir açık anahtarın Hash'sine, yani bir alıcı Address'a dayalı olarak bitcoinleri kilitler. Aradaki fark, imzaların ve komut dosyalarının işleme nasıl dahil edildiğinde yatmaktadır. P2WPKH durumunda, imza komut dosyası bilgileri (ScriptSig) geleneksel işlem yapısından Witness adı verilen ayrı bir bölüme taşınır. Bu taşıma SegWit (Ayrılmış Tanık) güncellemesinin bir özelliğidir. Bu teknik, doğrulama için gerekli komut dosyası bilgilerini ayrı bir bölümde tutarken ana gövdede işlem verilerinin boyutunu azaltma avantajına sahiptir. Sonuç olarak, P2WPKH işlemleri genellikle Eski işlemlere kıyasla ücret açısından daha ucuzdur. P2WPKH adresleri Bech32 kodlaması kullanılarak yazılır, bu da BCH sağlama toplamı sayesinde daha özlü ve daha az hataya açık bir yazıma katkıda bulunur. Bu adresler her zaman bc1q ile başlar, bu da onları Eski alıcı adreslerinden kolayca ayırt edilebilir hale getirir. P2WPKH bir sürüm 0 SegWit çıktısıdır.


**UTXO:** Harcanmamış İşlem Çıktısının kısaltmasıdır. UTXO, henüz harcanmamış veya yeni bir işlem için girdi olarak kullanılmamış bir işlem çıktısıdır. UTXO'lar, bir kullanıcının sahip olduğu ve şu anda harcanabilecek bitcoinlerin bir kısmını temsil eder. Her UTXO, bitcoinleri harcamak için gerekli koşulları tanımlayan belirli bir çıktı komut dosyasıyla ilişkilidir. Bitcoin'teki işlemler bu UTXO'ları girdi olarak tüketir ve çıktı olarak yeni UTXO'lar yaratır. UTXO modeli, işlemlerin var olmayan ya da daha önce harcanmış bitcoinleri harcamaya çalışmadığının kolayca doğrulanmasını sağladığından Bitcoin için temel öneme sahiptir. Esasen, bir UTXO, Bitcoin'ün bir parçasıdır.