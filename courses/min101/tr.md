---
name: Bitcoin'a Giriş mining
goal: Bitcoin mining ve proof-of-work'yi sıfırdan anlamak
objectives: 


  - proof-of-work'i ve Bitcoin'daki rolünü anlayın.
  - Zorluk ayarlama mekanizmasını analiz edin.
  - mining ile ilişkili teknik terimlerin gerçekte ne anlama geldiğini bilin.
  - Bir Bitcoin bloğunun ve bileşenlerinin oluşturulmasında yer alan adımları açıklayın.
  - mining endüstrisindeki önemli gelişmeleri tanımlayabilecektir.


---

# Bitcoin mining'in temellerini keşfedin



proof of work'yi anlamak, Bitcoin'ün nasıl çalıştığını anlamak demektir. Bu icat ve onun ustaca kullanımı olmasaydı, Bitcoin var olamazdı. Bu kurs size bitcoin yolculuğunuz için ihtiyacınız olan tüm mining teorisini sunmaktadır.



MIN 101, tüm kavramları tam olarak sıfırdan açıkladığı için öncelikle yeni başlayanlara yöneliktir. Bununla birlikte, zaten orta düzeyde bir bilgiye sahipseniz, bu kurs anlayışınızı pekiştirmenizi, bazı yaklaşık sezgileri düzeltmenizi ve ana akım açıklamalarda genellikle eksik olan ayrıntıları keşfetmenizi sağlayacaktır.



Bu kursun sonunda, proof-of-work'nın nasıl çalıştığını basit ve titiz bir şekilde açıklayabileceksiniz. MIN 101 ayrıca teorik veya pratik olsun, Bitcoin mining ve Plan ₿ Academy'e adanmış diğer tüm daha ileri düzey kurslar için ideal bir giriş niteliğindedir.



+++


# Giriş


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Kursa genel bakış


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



mining sistemi içinde Proof-of-Work ve Bitcoin'nin temel teorik kavramlarını keşfedeceğiniz MIN 101 kursuna hoş geldiniz. Bu kurs, mining'in nasıl çalıştığını anlamak için bitcoiner yolculuğunuzdaki ilk adımdır. Bu kursu tamamladıktan sonra, daha ileri düzeydeki teori kurslarına geçebilecek veya uygulamalı olarak bitcoin madencisi olabileceksiniz!



Bu MIN 101 kursunda, doğrudan konunun özüne ineceğimiz için Bitcoin'nin temel kavramlarının üzerinden geçmeyeceğiz: mining. Eğer Bitcoin'yi hiç duymadıysanız veya temelleri sizin için hala biraz belirsizse, giriş niteliğindeki BTC 101 kursumuzla başlamanızı şiddetle tavsiye ederim. Bu temel bilgileri edindikten sonra, MIN 101'i güvenle ele alabileceksiniz:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Bölüm 1 - Giriş



Bu kursa, teknik mekanizmalara girmeden önce size net bir zihinsel resim sunmak için mining'in çok basitleştirilmiş bir açıklamasını sunduğum isteğe bağlı bir ilk bölümle başlayacağız.



Buradaki amaç size tüm teknik detayları vermek değil (bunlar kursun ilerleyen bölümlerinde yer alacak), size yol gösterici bir çerçeve sunmaktır. Bu çerçeve bir kez oluşturulduktan sonra, daha sonra tanıtılan her ileri düzey kavram doğal olarak bu yapıya uyacaktır.



### Bölüm 2 - proof of work nasıl çalışır?



Giriş bölümünden sonra, Bölüm 2 eğitim programının teknik temelini oluşturmaktadır. Amacı, Bitcoin'in geçerli blokları nasıl ürettiğini adım adım açıklamaktır. proof-of-work mekanizmasına girmeden önce bir bloğun yapısını keşfederek başlayacağız: hedefin rolü, nonce ve hash fonksiyonu. Son olarak, zorluk ayarlama mekanizması sayesinde Bitcoin'in hash gücündeki değişikliklere rağmen istikrarlı bir blok üretim oranını nasıl koruduğunu göreceğiz. Bu bölümün sonunda, Bitcoin'in proof-of-work'nin temel ilkelerini tam olarak anlamış olacaksınız.



### Bölüm 3 - Bitcoin mining teşvik sistemi



Üçüncü bölümde, madencilerin neden mining'e dürüstçe katılmaya teşvik edildiğine bakacağız. Blok ödülü ilkesini, bileşimini ve hesaplama yöntemini, yarılanmalar yoluyla zaman içindeki gelişimini ve coinbase işleminin özel rolünü detaylandıracağız.



### Bölüm 4 - Bitcoin mining endüstrisi



Dördüncü bölüm mining'i operasyonel gerçekliğine geri döndürmektedir. Mevcut donanım kısıtlamalarını anlamak için mining makinelerinin Bitcoin'ün başlangıcından modern ASIC'ya kadar olan evriminin izini sürüyor. Ayrıca madencilerin gelirlerindeki varyansı nasıl azalttıklarını anlamak için mining havuzlarının temellerine de bakıyoruz.



### Bölüm 5 - Son bölüm



Kursun son bölümünde, diplomanızı alarak mining hakkındaki bilginizi test edebilirsiniz.



Bu nedenle MIN 101 kursunun amacı, Bitcoin mining'u hem teknik hem de ekonomik olarak net, yapılandırılmış ve kalıcı bir şekilde anlamanızı sağlamaktır.



Bitcoin mining'i keşfetmeye hazır mısınız? Hadi başlayalım!




## Bitcoin mining artık daha kolay


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Bitcoin [mining](https://planb.academy/resources/glossary/mining)'in ayrıntılı ve daha teknik bir açıklamasına geçmeden önce, size kasıtlı olarak basit ve şematik olan prensibe genel bir bakış sunmak istiyorum. Zaten temel bilgilere sahipseniz, test sorularını yanıtladıktan sonra bir sonraki bölümde doğrudan konunun özüne inebilirsiniz. Bu bölüm, size nazik bir başlangıç sağlamak için öncelikle yeni başlayanlara yöneliktir.



Bitcoin'yı, kimin kime bitcoin gönderdiğini yazdığımız, herkes tarafından paylaşılan büyük bir not defteri olarak düşünün. Bu deftere [blok zinciri](https://planb.academy/resources/glossary/blockchain) denir. Tek bir kişi tarafından tutulamaz, aksi takdirde güvenilir olması gerekirdi. Bunun yerine, Bitcoin kolektif olarak çalışır: binlerce bilgisayar bu defterin aynı versiyonunu doğrular ve korur.



![Image](assets/fr/049.webp)



Bitcoin'de bir ödeme yaptığınızda bir [işlem](https://planb.academy/resources/glossary/transaction-tx) oluşturursunuz. Bu işlem anında not defterine eklenmez. Önce ağa gönderilir, ardından bir sonraki işlem paketine entegre edilmeyi bekler. Bu pakete [blok](https://planb.academy/resources/glossary/block) adı verilir.



![Image](assets/fr/050.webp)



Bir blok basitçe bir araya getirilmiş bir dizi işlemdir. Bir blok hazır olduğunda, onu yayınlamak yeterli değildir. Bloğun havuza eklenmeye değer olduğunu ağa kanıtlamanız gerekir. İşte mining burada devreye girer.



Mining, enerji tüketerek bir bloğu doğrulama işidir. Madenci adı verilen aktörler özel bilgisayarlar kullanır. Bu makineler, ağın kabul ettiği bir kanıt bulana kadar bir döngü içinde çok sayıda test yapmak için elektrik tüketir. Bir madenci bu kanıtı bulduğunda, bloğu geçerli kabul edilir.



Blok doğrulandıktan sonra ağa yayınlanır. Diğer düğümler kurallara uygunluğunu hızlıca kontrol eder ve ardından önceki blokların sırasına ekler. Buna "blok zinciri" denmesinin nedeni budur: her yeni blok diğerlerinden sonra sırayla gelir ve bu zincir yavaş yavaş büyür.



![Image](assets/fr/051.webp)



Özetlemek gerekirse, işlemler önce oluşturulur. Daha sonra bunlar bir blokta bir araya getirilir. Daha sonra bir madenci elektrik tüketerek bu bloğu doğrular. Son olarak, bu blok blok zincirine eklenir ve içerdiği işlemler onaylanmış olur.



Madenciler elektrik tüketiyorsa, bu gönüllü oldukları için değildir. Bunu yapıyorlar çünkü bir ödül var. Bir madenci bir bloğu doğruladığında, iki tür gelir elde eder. Bir yandan yeni yaratılan bitcoinleri alır. Diğer yandan, blokta yer alan işlemler için kullanıcılar tarafından ödenen ücretleri toplar. Başka bir deyişle, madenci hem programlanmış para ihracı yoluyla hem de bir piyasa tarafından belirlenen işlem ücretleri ile telafi edilir.



Bu aşamada, size kasıtlı olarak mining'in çok basit bir görünümü verilmektedir. Henüz bloğun nasıl inşa edildiği, madencilerin aradığı kanıtın tam olarak nasıl çalıştığı, Bitcoin'nin nasıl sabit bir hızda ilerlediği, ödülün tam olarak nasıl hesaplandığı ya da nasıl talep edildiği açıklanmıyor. Sorun değil, bu MIN 101 kursunun geri kalanında göreceğimiz tek şey bu!



Bu bölümün amacı sadece size net bir zihinsel yapı sunmaktı: işlemler → bloklar → mining → blok zinciri → ödül. Bu fikir zincirini aklınızda tutun. Kursun geri kalanında, her bölüm bu unsurlardan birine ilişkin bir teknik ayrıntı katmanı ekleyecek ve siz yalnızca neler olup bittiğini değil, aynı zamanda bunun nasıl ve neden güvenilir bir şekilde, büyük ölçekte, bir patron olmadan ve güvene ihtiyaç duymadan çalıştığını anlayana kadar devam edecektir.



# proof of work nasıl çalışır?


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Bitcoin işlem yolu


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Bitcoin mining'nın neyle ilgili olduğunu anlamak için öncelikle tipik bir Bitcoin işleminin izlediği yolu takip etmemiz gerekir. Bu size bloğun tam olarak nerede devreye girdiğini ve neden sistemin kalbinde yer aldığını gösterecektir. Bu ilk bölümde keşfetmenizi istediğim şey de bu.



Bitcoin'de bir işlem, bitcoinlerin sahipliğini bir kullanıcıdan diğerine aktaran bir veri yapısıdır. Somut bir ifadeyle, geçmiş işlemlerden ([UTXO'ler](https://planb.academy/resources/glossary/utxo) olarak adlandırılır) `girdi' olarak adlandırılan `çıktıları' tüketir ve ardından bu bitcoinlerin artık kime ait olduğunu ve daha sonra hangi koşullar altında harcanabileceğini tanımlayan yeni `çıktılar' oluşturur.



![Image](assets/fr/001.webp)



Bitcoin ile ilgili önemli bir nokta da harcama yetkisidir. Bitcoin'lar bankadaki paranız gibi bir hesapta bulunmaz, ancak harcama koşullarına göre kilitlenir. Bir [wallet](https://planb.academy/resources/glossary/wallet), bir UTXO'yi [girdi](https://planb.academy/resources/glossary/input) olarak kullanmak istediğinde, kilidi açma hakkına sahip olduğuna dair kriptografik kanıt sağlamalıdır. Bu kanıt genellikle [özel bir anahtardan](https://planb.academy/resources/glossary/private-key) alınan [dijital imza](https://planb.academy/resources/glossary/digital-signature) generated şeklini alır. Bitcoin kullanıcılarının özel anahtarlarınızı güvence altına almakta ısrar etmelerinin nedeni budur: bitcoinlerinize erişimin kilidini açan ve sonuç olarak onları harcamanızı sağlayan şey bunlardır.



![Image](assets/fr/002.webp)



Bitcoin'teki dijital imza iki önemli rol oynamaktadır:




- Harcama yetkisi: Bu, kullanıcının UTXO harcama koşulu tarafından beklenen özel anahtara sahip olduğunu kanıtlar;
- Bütünlük koruması: yetkilendirmeyi işlemin kesin ayrıntılarına (alıcılar, tutarlar, ücretler, vb.) bağlar. Birisi daha sonra işlemi değiştirirse, imza artık geçerli olmayacaktır.



İşlem doğru şekilde oluşturulduktan ve kullanıcının Bitcoin wallet'sı tarafından imzalandıktan sonra, Bitcoin ağında yayınlanmalıdır.



### Bitcoin düğümünün dağıtımdaki rolü



Bitcoin eşler arası bir ağdır: tüm işlemleri alan ve işleyen merkezi bir sunucu yoktur. Bu rol düğümler tarafından kolektif olarak oynanır. Bir Bitcoin düğümü, Bitcoin ağındaki diğer düğümlere bağlı olan ve ana görevi işlemleri ve blokları doğrulamak, depolamak ve iletmek olan bir yazılım parçasıdır (örneğin Bitcoin Core).



Bir wallet'dan bir işlem gönderdiğinizde, wallet bunu bir düğüme (sizin veya bir hizmetin) iletir. Bu düğüm öncelikle işlemin aşağıdaki gibi çeşitli kurallara uygun olup olmadığını kontrol edecektir:




- imzalar geçerlidir;
- girdiler mevcut UTXO'leri (yani var olan bitcoinleri) referans alır;
- bu UTXO zaten başka bir yere harcanmamıştır;
- çıktıların miktarı girdilerin miktarına eşit veya daha azdır (bitcoinler yoktan var edilmez);
- vs.



İşlem tüm bu kontrollerden geçerse, düğüm bunu ağdaki bağlı olduğu diğer düğümlere yayar. Onlar da işlemi kontrol eder ve iletir ve bu böyle devam eder. Birkaç saniye içinde işlem yayılır ve Bitcoin ağının tamamı ya da en azından büyük bir kısmı tarafından bilinir hale gelir.



![Image](assets/fr/003.webp)



### Mempool: işlem bekleme odası



Bir işlemin yayınlandığı an ile bir blokta onaylandığı an arasında beklemesi gerekir. Bu bekleme alanına **mempool** (`memory` ve `pool` kelimelerinin kısaltması) adı verilir. Bu nedenle mempool, geçerli ancak henüz onaylanmamış işlemler için geçici bir depolama alanıdır.



Önemli nokta: tek bir mempool diye bir şey yoktur, sadece mempool'lar vardır. Her düğüm kendi yerel kısıtlamaları ile kendi mempool'unu korur. Bu, herhangi bir anda iki düğümün biraz farklı mempool içeriğine sahip olabileceği anlamına gelir (ne aldıklarına, neyi reddettiklerine veya neyi temizlediklerine bağlı olarak).



![Image](assets/fr/004.webp)



Bu aşamada, ağ işlemden haberdardır, işlemi doğrulamıştır ve onaylanana kadar bellekte tutmaktadır. Ancak bu işlemin onaylanması ancak bir madenci bu işlemi bir bloğa eklediğinde ve bu blok ağ tarafından kabul edildiğinde gerçekleşecektir.



### Blockchain: kamuya açık bir zaman damgası kaydı



Bitcoin maddi olmayan bir para birimi olduğundan, bir sorunu ele almak zorundadır: merkezi bir otorite olmadan çifte harcamayı önlemek. Eğer iki işlem aynı UTXO'i harcamaya kalkışırsa, herkesin tek ve tutarlı bir durum üzerinde birleşebilmesi gerekir. Satoshi Nakamoto bu sorunu şu ünlü cümle ile özetlemektedir:



> Bir işlemin olmadığını teyit etmenin tek yolu tüm işlemlerden haberdar olmaktır.

Başka bir deyişle, bir bitcoin'in daha önce harcanmadığını bilmek için, geçmiş harcamaların ortak bir kaydına ihtiyacınız vardır.



Blok zincirinin rolü budur: işlemlerin geçmişini içeren halka açık bir kayıt. Ancak Bitcoin her bir işlemi gerçekleştiği anda yazmak yerine bunları bloklar halinde gruplandırır. Her blok bir geçmiş sayfası olarak işlev görür ve sistem böylece bir zaman damgası sunucusu gibi çalışır: işlemleri zaman içinde doğrulanabilir bir şekilde sıralar.



Basit bir prensip sayesinde bu kayıt yeniden yazılamaz: her blok bir önceki bloğun kriptografik parmak izini (hash) içerir. Böylece bloklar birbirine bağlanır: geçmişteki bir bloğu değiştirirseniz, hash'i değişir, bu da bir sonraki blokla olan bağlantıyı koparır, bu da ondan sonraki blokla olan bağlantıyı koparır ve bu böyle devam eder. "*blockchain*"e adını veren de bu bağımlılıklar zinciridir.



![Image](assets/fr/005.webp)



Bitcoin'in bu temel ilkelerini anladıktan sonra, bir madencinin amacını daha somut terimlerle tanımlayabiliriz: bekleyen işlemleri ekleyerek mevcut zinciri genişleten yeni bir blok oluşturmak ve ardından bunu geçerli kılmaya çalışmak (bu, daha sonraki bir bölümde inceleyeceğimiz ünlü "proof of work "dir). Ama önce, bir sonraki bölümde aday bir bloğun nasıl oluşturulduğunu birlikte keşfedelim.



## Bir Bitcoin bloğu oluşturma


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Artık bir Bitcoin işleminin nasıl çalıştığını ve blok zincirinin rolünü anladınız. Ancak, proof-of-work'in nasıl çalıştığına daha ayrıntılı olarak bakmadan önce, madencinin gerçekleştirmesi gereken önemli bir adım daha vardır: bir aday bloğun oluşturulması. Geçerli bir kanıt arayışına başlamadan önce aday bloğun ne olduğunu ve madencinin bunu nasıl oluşturduğunu birlikte öğrenelim.



### Aday blok



Miner'ler bloklarını madenciliğe başlamadan önce kendileri inşa etmek zorundadır. Her madenci, sırayla, kendi mempool'unda bekleyen işlemlerden [aday blok](https://planb.academy/resources/glossary/candidate-block) olarak bilinen bir blok oluşturur. Bu nedenle bir aday blok oluşturmak şunlardan oluşur:




- hangi işlemlerin dahil edileceğini seçin;
- bu işlemleri Bitcoin kuralları ile uyumlu bir şekilde düzenleyecektir;
- bloğun [başlığında](https://planb.academy/resources/glossary/block-header) saklanan meta verilerini üretir.



İşlemlerin seçimi basit bir ekonomik mantık izler: bir bloğun Bitcoin protokolü tarafından sınırlandırılmış bir kapasitesi vardır, bu nedenle madenci bu alan için kazancını maksimize etmeye çalışır. Öncelikli olarak, blokta kapladıkları alana göre en yüksek ücretleri sunan işlemleri seçer (bu, sats/vB cinsinden ifade edilen "ücret oranı" olarak bilinir). Ücretlerin ayrıntıları daha sonra ele alınacaktır; sadece alan verimliliğine göre sıralama fikrini hatırlayın.



Bir Bitcoin bloğu bu nedenle iki ana bölümden oluşur:




- işlemlerin bir listesi;
- bir bakıma bloğun kimlik kartı olarak hizmet veren bir blok başlığı.



![Image](assets/fr/006.webp)



Başlık, proof-of-work'nin temeli olarak kullanıldığı için çok önemlidir: Bitcoin'de bir bloğun tamamını doğrudan kazmazsınız; yalnızca bloğu zincire bağlamak ve içeriğini işlemek için gereken bilgileri özetleyen bir bloğun başlığını kazarsınız. Başlığın tüm işlemleri temsil etmesini sağlamak için Bitcoin kriptografik bir araç kullanır: Merkle ağacı.



### Merkle ağacı: büyük bir işlem kümesini özetleme



Başlıktaki tüm işlemleri listelemek imkansız olacaktır: bir blok binlerce işlem içerebilirken, başlığın sabit bir boyutu (80 bayt) vardır. Bu nedenle çözüm, bloktaki tüm işlemlere bağlı olan benzersiz bir hash hesaplamaktır: bu Merkle köküdür.



Prensip şu şekildedir:




- her bir işlemin kriptografik parmak izi (hash) hesaplanır;
- bu hash'ler eşleştirilir, birleştirilir ve ardından yeni bir hash katmanı oluşturmak için tekrar hash'lenir;
- bu işlem tek bir nihai hash elde edilene kadar tekrarlanır: Merkle kökü.



![Image](assets/fr/007.webp)



Dolayısıyla, tek bir işlem tek bir bitle bile değişirse, sonuç Merkle köküne yayılan parmak izinde bir değişiklik olur. Bu kök blok başlığına dahil edilir. Dolayısıyla, geçmiş bir işlemin değiştirilmesi, dahil edildiği blok başlığının ve dolayısıyla blok ayak izinin ve ardından sonraki bloklarla olan bağlantının değiştirilmesi anlamına gelir.



SegWit'dan bu yana, imzaları diğerlerinden ayırdık. Yani, gerçekte, her blokta iç içe geçmiş 2 Merkle ağacı vardır. Bu ayrımın bir bloğun boyutunu sayma şeklimiz ve belirli kriptografik taahhütler için sonuçları vardır, ancak temel fikir aynı kalır: başlık, bloğun tüm içeriğini kompakt bir şekilde taahhüt etmelidir.



### Blok başlığı



Blok başlığı 80 bayt uzunluğundadır ve tam olarak 6 alan içerir. Bir proof of work aranırken hash edilecek olan bu altı öğedir (sonraki bölüme bakın):





- Sürüm (`version`): Bu, bloğun hangi kurallara veya güncelleme sinyallerine bağlı olduğunu gösterir. Protokol uyumluluğunu ve evrimini sürdürmek için bir mekanizma görevi görür.




- Önceki blok karması (`previousblockhash`): Bu, önceki bloğun başlığının hash'idir. Blokları birbirine bağlayan şey budur. Bu alan olmadan bağımsız bloklarımız olurdu. Önceki bloğun başlığının hash'ini dahil ederek, her yeni bloğun bir öncekinin üzerine inşa edildiği bir zincir elde ederiz.





- Merkle kökü (`merkleroot`): Bu, bloktaki tüm işlemlerin parmak izidir (Merkle ağacı aracılığıyla). Başlığı içeriğe bağlar: madenci işlemlerin seçimini veya sırasını değiştirirse kök değişir.





- Zaman damgası: Bu, madenci tarafından (geçerlilik kısıtlamaları ile) seçilen ve bloğun ne zaman çıkarıldığını belirtmesi gereken bir zaman damgasıdır (Unix zamanı). Saniyesine kadar tam olarak doğru olması gerekmez, ancak ağ tarafından kabul edilebilir olması için belirli koşulları karşılaması gerekir.





- Kodlanmış zorluk hedefi (`nbits`): Bu alan mevcut zorluk hedefini kodlar. Zorluk bölümünde daha fazla ayrıntıya gireceğiz, ancak bu parametrenin başlığın bir parçası olduğunu unutmayın.





- Nonce (`nonce`): Bu, madencinin serbestçe değiştirebileceği bir değerdir. proof-of-work sırasında ayarlanabilir bir değişken olarak hizmet eder. Rolünü bir sonraki bölümde daha ayrıntılı olarak açıklayacağım, ancak nonce'un blok başlığının bir parçası olduğunu ve art arda denemelere izin vermek için tasarlandığını anlamak önemlidir.



Bunu görselleştirmeyi kolaylaştırmak için, işte onaltılık formatta (80 bayt) bir blok başlığı örneği:



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



İşte saha saha bir döküm:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Madenci tarafından oluşturulan bu aday blok başlığı, çalışmalarının temelini oluşturur. Geçerli bir proof-of-work ararken, doğrudan bir döngü içinde hash edilen işlem listesinin tamamı değil, bloğu geçmişe bağlamak ve içeriğini işlemek için gereken her şeyi içeren ve aynı zamanda bir sonraki bölümde inceleyeceğimiz mining mekanizması için gerekli parametreleri de içeren bu 80 baytlık bloktur.



## Hash, hedef ve nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Önceki bölümlerde, bir Bitcoin işleminin yolunu izlediniz: bir wallet tarafından oluşturuldu ve imzalandı, düğümler tarafından aktarıldı, mempool'larda saklandı, daha sonra bir madenci bunu ağ tarafından kabul edilen bir bloğa dahil ettiğinde onaylandı. Ancak henüz bir madencinin bloğunu blok zincirine nasıl ekleyebileceğini görmedik. mining'nın arkasındaki süreç nedir?



mining sürecini anlamak oldukça basittir. El ele giden 3 kavrama indirgenebilir: bir hash fonksiyonu, bir hedef değer ve madencinin değiştirebileceği bir değişken. Şimdi tüm bunların nasıl çalıştığına bir göz atalım.



### Hash fonksiyonu



Hash fonksiyonu, bir mesajı girdi olarak alan ve "*fingerprint*" veya "*hash*" olarak adlandırılan sabit boyutta bir çıktı üreten bir araçtır.



![Image](assets/fr/010.webp)



Hash fonksiyonu bilgisayar sistemlerinde ilginçtir çünkü belirli özelliklere sahiptir:





- Girdinin tek bir bitini değiştirirseniz, ortaya çıkan çıktı hash'i tamamen ve öngörülemez bir şekilde değişir;



![Image](assets/fr/011.webp)





- Çıktıdan girdiye gitmek mümkün değildir: işlev geri döndürülemez;



![Image](assets/fr/012.webp)





- Tam olarak aynı hash'i veren iki farklı mesaj bulmak imkansızdır.



![Image](assets/fr/013.webp)



Bitcoin`da mining için kullanılan hash fonksiyonu `[SHA256](https://planb.academy/resources/glossary/sha256)`dir ve art arda iki kez uygulanır. Bu çift SHA256 ya da `SHA256d` olarak bilinir. Bloğun parmak izini üreten bu çift hashtir.



```text
hash = SHA256(SHA256(message))
```



Bizim durumumuzda, `mesaj` aslında bir önceki bölümde gördüğünüz blok başlığına karşılık gelir. Bir hatırlatma olarak, başlık bloktaki her şeyi özetleyen küçük bir yapıdır.



![Image](assets/fr/014.webp)



### İş kanıtı: hedeften daha küçük bir hash bulma



Proof-of-Work genellikle karmaşık bir problemi çözmek olarak tanımlanır. Gerçekte, bu bir deneme-yanılma araştırması gibi bir problem değildir: madenci, hash'i (`SHA256d` hash fonksiyonundan geçtikten sonra) basit bir koşula uyan başlığın bir versiyonunu bulmalıdır: belirli bir hedeften daha küçük olmalıdır.



Bu koşul aşağıdaki şekilde formüle edilmiştir:




- blok başlığının hash'i bir hash fonksiyonu kullanılarak hesaplanır;
- bu hash'i bir sayı olarak yorumlarız;
- bloğun geçerli olabilmesi için bu sayının "*zorluk hedefi*" adı verilen bir değerden küçük veya bu değere eşit olması gerekir.



Başka bir deyişle, bir blok aşağıdaki durumlarda geçerlidir:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Hedef 256 bitlik bir sayıdır. SHA256d` tarafından üretilen hash de 256 bit olduğundan, iki sayı olarak karşılaştırılabilirler. Hedef ne kadar düşükse, bu eşiğin altında daha az olası sonuç olduğu için koşul o kadar zordur. Tersine, hedef ne kadar yüksek olursa, koşulun yerine getirilmesi o kadar kolay olur ve bir bloğu kazmak o kadar kolay hale gelir. İlerleyen bölümlerde bu hedefin nasıl belirlendiğine daha yakından bakacağız.



Bu sistemde hash fonksiyonu ilginçtir. Girdiden çıktıyı hesaplamanın kolay olduğunu, ancak yalnızca fonksiyonun çıktısını bilerek bir girdi bulmanın imkansız olduğunu unutmayın. mining'te madencilerden kesin bir hash bulmaları değil, hedef değerin altında bir hash bulmaları istenir. Bunu başarmanın tek yolu, aday bloklarının belirli bir başlığı hashlendiğinde bu hedeften daha küçük bir hash üretene kadar çok sayıda deneme yapmaktır.



Hedef yeterince düşük olduğunda, bu işlem maliyetli hale gelir. Madenci, aday bloğunun başlığının hashini hesaplar, sonucu kontrol eder ve koşul karşılanmazsa başlığı değiştirir ve hesaplamayı tekrarlar. Bu döngü geçerli bir başlık bulunana kadar tekrarlanır. Başlığın hash'i nihayet koşulu karşıladığında, proof of work kurulur, blok geçerli kabul edilir ve düğümlerin blok zincirlerine eklemeleri için Bitcoin ağında yayınlanabilir. Kazanan madenci daha sonra ilgili ödülü alırken (bileşimini daha sonra detaylandıracağız), tüm madenciler hemen bir sonraki blok için yeni ve geçerli bir başlık aramaya başlar.



Bu mekanizmanın temel avantajı asimetrik olmasında yatmaktadır. Bir proof of work üretmek, çok sayıda hash hesaplaması gerektirdiğinden madenciler için maliyetlidir. Öte yandan, doğrulayıcılar, yani ağ düğümleri için doğrulama son derece basittir: tek yapmaları gereken madenci tarafından sağlanan blok başlığını hash etmek ve elde edilen hash'in gerçekten de hedeften daha düşük olup olmadığını kontrol etmektir. Bu nedenle bir kanıt bulmak çok fazla çalışma ve kaynak gerektirirken, geçerliliğini doğrulamak hızlı ve ucuzdur. Verimli bir proof-of-work sistemini tanımlayan da tam olarak bu özelliktir.



### Nonce



Geriye pratik bir soru kalıyor: madenci tarafından oluşturulan aday bloğun başlığı geçerli bir hash vermiyorsa, madenci nasıl tekrar deneyebilir? Farklı bir hash elde etmek için başlıktaki bir şeyi değiştirmesi gerekir. Bu tam olarak nonce'un rolüdür.



Bir hash fonksiyonunun ilk özelliğini hatırlayın: girdinin tek bir bitini değiştirmek tamamen farklı ve öngörülemez bir çıktı hash'i üretmek için yeterlidir. Bu nedenle her hash hesaplaması rastgele bir çekilişe benzer.



![Image](assets/fr/016.webp)



Şansını tekrar denemek için madencinin aday bloğunun tüm başlığını değiştirmesi gerekmez: sadece küçük bir kısmını değiştirmesi gerekir, çünkü tek bir farklı bit bile tamamen yeni bir hash ile sonuçlanacaktır ve hedeften daha küçükse potansiyel olarak geçerli olacaktır.



Blok başlığının bir nonce içermesinin nedeni de tam olarak budur. Nonce 32 bitlik bir değerdir, bir kez kullanılır ve sonra değiştirilir. Pratik anlamda, aynı aday blok için bir madenci 4,29 milyar olası değeri test edebilir ("0" ile "2^32 - 1" arasında). Nonce'nin her bir varyasyonu blok başlığını değiştirir ve sonuç olarak `SHA256d` hash fonksiyonunu uyguladıktan sonra üretilen hash'i tamamen değiştirir.



mining süreci çok basittir:




- madenci bir aday blok oluşturur (işlemler + başlık);
- daha sonra `SHA256d(header)` hash'ini hesaplar;
- eğer sonuç hedeften büyükse, nonce'u değiştirir;
- yeniden başlar;
- vs.



![Image](assets/fr/017.webp)



Aslında, nonce değiştirilebilen tek alan değildir. Bir bloğun işlemlerinde yapılan herhangi bir değişiklik, Merkle ağacının kökünde bir değişikliğe ve dolayısıyla o bloğun başlığında bir değişikliğe neden olur. Modern hesaplama gücüyle, nonce'un 4,29 milyar olası değerini gözden geçirmek nispeten hızlı bir şekilde yapılabilir. Bu nedenle, genellikle "*extra-nonce*" olarak adlandırılan ve başlık varyasyonu olasılıklarını daha da çoğaltan başka bir alan daha vardır. Bu mekanizmaya daha sonraki bir bölümde daha ayrıntılı olarak geri döneceğiz.



### proof of work'ün amacı ne?



Buna "kanıt" diyoruz çünkü sonuç hemen doğrulanabilir: bir blok üretildikten sonra, herhangi bir düğüm, saniyenin çok küçük bir bölümünde, başlığının kriptografik özetinin gerçekten de gerekli hedefin altında olup olmadığını kontrol edebilir. Buna "iş" diyoruz çünkü bu hash'i elde etmek çok sayıda deneme ve dolayısıyla hesaplama ve enerji açısından gerçek bir maliyet gerektiriyor.



Bitcoin Beyaz Kitap'ta Satoshi Nakamoto, Bitcoin'da bir proof-of-work sistemi kullanmanın iki avantajını ortaya koymaktadır:





- Seal ekonomik tarihin incelenmesi:**



Hesaplama yükü harcandıktan sonra blok kilitlenir: değiştirilmesi o bloğun proof of work'inin yeniden yapılmasını gerektirir. Bloklar birbirine zincirlendiğinden, eski bir bloğun değiştirilmesi aynı zamanda sonraki tüm blokların yeniden hesaplanması ve ardından dürüst zincirin devam eden çalışmasına yetişilmesi ve aşılması anlamına gelecektir.



Başka bir deyişle, proof-of-work zaman damgalama sisteminin belkemiği olarak hizmet eder ve bloklar biriktikçe geçmişi tahrif etmeyi giderek daha maliyetli hale getirir. Yeni bir blok çıkarıldığında, proof of work tarafından sağlanan güvenlik mevcut tüm UTXO'lere aynı anda ve eşit olarak uygulanır. Eklenen her blokla birlikte, her UTXO böylece Proof-of-Work'dan ek bir güvenlik miktarı biriktirir.





- Çoğunluk kuralını (konsensüs) tanımlayın ve Sybil'i etkisiz hale getirin:**



Proof-of-Work ayrıca Bitcoin'ün "bir kimlik = bir oy" oylama kuralına dayanmadan fikir birliğine varmasını sağlar, bu da büyük miktarda kimlik (IP'ler, düğümler, anahtarlar...) oluşturulmasıyla kolayca değiştirilebilir.



Bitcoin'te "*çoğunluk*" en fazla sayıda katılımcı değil, **en fazla iş biriktiren zincirdir**. Satoshi'nın belirttiği gibi, bu bir "bir CPU = bir oy" ilkesidir, yani geçerli bloklar üretmek için harcanan gerçek bilgi işlem gücü ile ağırlıklandırılmış bir oy. Dolayısıyla, binlerce düğümün konuşlandırılması Bitcoin'e göre kendi başına hiçbir avantaj getirmez. Ek hesaplama gücü olmadan, daha fazla çalışma kanıtı biriktirilmez ve Sybil saldırısı işe yaramaz hale gelirken, karar kuralı nesnel kalır ve katılımcıların tanımlanmasını gerektirmez.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Eşler Arası Elektronik Nakit Sistemi.*](https://bitcoin.org/bitcoin.pdf)



Reşit olmayanların yararlılığı ve yetkileri ile ilgili ilkeler oldukça karmaşık bir konudur ve bu kursta daha fazla ayrıntıya girmeyeceğim. Ancak, gelecekteki MIN 201 eğitim kurslarında bu konuya derinlemesine döneceğiz.



Şu an için mining'in nasıl çalıştığını şu şekilde özetleyebilirsiniz: madenciler mempool'larda bekleyen işlemlerle bir aday blok oluşturur, ardından başlığının bir hedefe eşit veya daha az olan bir hash'ini (`SHA256d` aracılığıyla) ararlar. Bunu deneme yanılma yoluyla nonce'ları test ederek başarırlar.



Bir sonraki bölümde, proof-of-work prensibinin arka planını anlamak için kısa bir tarihsel gezintiye çıkacağız ve ardından zorluk hedefinin sistem tarafından nasıl belirlendiğine bakacağız.



## proof of work'in tarihçesi


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



İş ispatı Bitcoin için icat edilmemiştir. Satoshi Nakamoto, farklı bağlamlarda zaten keşfedilmiş olan birkaç eski fikri ele aldı ve bir araya getirdi.



### Hashcash



1990'ların sonlarında, e-posta spam sorunu önemli hale geldi. Gerçekten de, bir e-posta göndermenin neredeyse hiçbir maliyeti yoksa, bir spam gönderici milyonlarca gönderebilir. Ancak her mesaj küçük bir hesaplama çabası gerektiriyorsa, tek bir meşru mesaj göndermek normal bir kullanıcı için kolay kalırken, milyonlarca mesaj göndermek çok pahalı hale gelir.



Bu, proof-of-work ilkesinin icadı olarak kabul edilen Adam Back tarafından 1997 yılında önerilen Hashcash'in amacıdır. Hashcash prensibi mining'ye çok benzemektedir: bir koşula uyan bir hash üretmek (hash'in başında belirli sayıda sıfır olması). Bu kanıt daha sonra mesaja eşlik eder ve alıcı tarafından çok hızlı bir şekilde doğrulanabilir. Bu kanıtı içermeyen bir e-posta alınırsa, hemen spam olarak kabul edilebilir ve bu nedenle filtrelenebilir. Spam gönderenler daha sonra milyonlarca mesaj göndermek için önemli miktarda enerji harcamak zorunda kalırlar, bu da ister pazarlama ister dolandırıcılık amaçlı olsun bu tür operasyonların karlılığını büyük ölçüde azaltır (hatta tamamen ortadan kaldırır).



Günümüzde Hashcash e-posta için kullanılmamaktadır. Spam filtreleme artık büyük ölçüde merkezi sistemlere dayanmaktadır. Hashcash'in mevcut çözümlere göre avantajı, merkezi filtreleme gerektirmemesinde yatmaktadır: herkes parametreleri kendi kriterlerine göre ayarlayabilir. Hash araması anonim olarak gerçekleştirilebildiğinden kimlik tespiti de gerektirmez. Hepsinden önemlisi, öznel filtreleme biçimlerini ortaya çıkarma eğiliminde olan bir itibar sistemine dayanmamaktadır.



Hashcash para yaratmakla ilgili değildi. Kolayca otomatikleştirilebilen dijital bir eyleme marjinal bir maliyet yüklemeye çalışıyordu.



![Image](assets/fr/008.webp)



### Bit Altın



1990'ların sonu ve 2000'lerin başında Nick Szabo, proof of work'e dayalı dijital kıtlık fikrini araştırdı. Bit Gold adını verdiği kavramsal projesi, maliyetli bir proof of work çözerek değer birimlerinin yaratılmasını ve daha sonra bu kanıtların bir sahiplik biçimi oluşturmak için bir sicile kaydedilmesini öngörmektedir.



Bit Gold, Bitcoin gibi konuşlandırılmış bir sistemle sonuçlanmadı, ancak birkaç önemli içgörü içeriyor: hesaplamanın kıtlık üretebileceği fikri ve yeniden yazılması zor bir geçmiş oluşturmak için zaman içinde öğeleri damgalama fikri.



### RPOW



2004 yılında Hal Finney RPOW'u (*Yeniden Kullanılabilir İş Kanıtları*) önerdi. Buradaki fikir, basitçe tüketilmek yerine daha sonra takas edilebilecek iş kanıtları üretmekti. RPOW, proof of work'e dayalı dijital token'lar yaratmayı ve bu token'ları çoğaltmadan doğrulamak ve aktarmak için bir sistem oluşturmayı amaçlıyordu. RPOW, yine Bitcoin'in daha sonra yapacağı gibi tamamen merkezi olmayan bir kayıt defteri sorununu tatmin edici bir şekilde çözmedi, ancak Bitcoin'in en büyük öncülerinden biri olmaya devam ediyor.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold ve RPOW, bir maliyet yüklemek ve bir tür kıtlık yaratmak için proof-of-work'yi kullanır. Bitcoin bu mekanizmayı ele alır, ancak ona merkezi ve kolektif bir rol verir: proof-of-work yalnızca bir şey yaratmak için kullanılmaz, aynı zamanda kaydın bir sonraki sayfasını (bir sonraki blok) yazma hakkına kimin sahip olduğuna karar vermek ve bu kaydın tahrif edilmesini maliyetli hale getirmek için de kullanılır.



## Zorluk hedefini ayarlama


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Önceki bölümlerde, proof-of-work'nin kalbini gördünüz: madenciler aday bloklarının başlığını `SHA256d` ile hashler ve blok yalnızca elde edilen hash sayısal olarak hedef adı verilen bir referans değerden küçük veya ona eşitse geçerli kabul edilir. O zaman geriye şu soru kalıyor: bu hedef nereden geliyor ve sistem zaman içinde tutarlı kalmasını nasıl sağlıyor?



Bitcoin ortalama olarak her 10 dakikada bir blok bulmayı hedefliyor. Açıkçası, bu hız saniyesi saniyesine garanti edilmiyor. Uygulamada, bazı bloklar bir öncekinden birkaç saniye sonra bulunurken, diğerleri bir saatten fazla bir süre sonra bulunur. Burada önemli olan yeterince uzun bir sürenin ortalamasıdır.



![Image](assets/fr/019.webp)



Bu değişkenlik mining'ün olasılıksal doğasından kaynaklanmaktadır: her bir hash, hedefin altında bir sonuç üretme olasılığı sabit olan (hedefin değişmediği varsayılarak) bağımsız bir girişimdir. Bu nedenle sürekli çekilişi olan bir piyango ile karşılaştırılabilir: madenciler saniyede ne kadar çok hash yaparsa, geçerli bir bloğun ortaya çıkmasından önce beklenen gecikme o kadar kısa olur, ancak bir çekilişten diğerine rastgeleliği asla ortadan kaldırmaz.



### Neden bloklar arasında 10 dakika hedefliyorsunuz?



Buna dair bir kanıt olmamasına rağmen, Satoshi Nakamoto verimlilik ve güvenlik arasında pratik bir uzlaşma olarak 10 dakikayı seçmiştir. Daha kısa bir aralık daha sık onaylama sağlayacak, ancak daha fazla geçici ağ bölünmesine neden olacaktır. Bu noktayı anlamak için bir bloğun yayılma şekline geri dönmemiz gerekir.



Bir madenci geçerli bir blok bulduğunda, bunu hemen eşlerine dağıtır. Bunu alan düğümler geçerliliğini kontrol eder (işlemler, proof of work, mutabakat kuralları, vb.), ardından sırayla iletir. Bu yayılma, internet gecikmesi, bant genişliği ve her düğümün bloğu doğrulama yeteneği ile sınırlı olan belirli bir süre alır.



![Image](assets/fr/020.webp)



Bu yayılma gecikmesi sırasında başka bir madenci de aynı yükseklikte geçerli bir blok keşfederse, ağ geçici olarak bölünebilir: düğümlerin ve madencilerin bir kısmı A bloğuna güvenirken, diğeri B bloğuna güvenir.



![Image](assets/fr/021.webp)



Bu bölünmeler felaket değildir. Nakamoto mutabakatı, uzun vadede yalnızca bir dalın üstün geleceğini öngörmektedir: en çok iş biriktiren dal. Gerçekten de, örneğin A bloğunun üzerine yeni bir blok çıkarılır çıkarılmaz, tüm ağ bu dal üzerinde yeniden senkronize olur ve B bloğunu terk eder, bu da günlük dilde bazen hatalı bir şekilde "*yetim blok*" olarak adlandırılan bir "*[stale blok](https://planb.academy/resources/glossary/stale-block)*" haline gelir.



![Image](assets/fr/022.webp)



Öte yandan, bunların bir maliyeti vardır: birkaç dakika boyunca madencilerin bir kısmı terk edilecek bir dal üzerinde çalışır. Bu çalışma, nihai zincire katkıda bulunmadığı için genel güvenlik açısından boşa gitmiş olur. Her blok arasındaki aralık ne kadar hızlı olursa, yayılma süresi her blok arasındaki sürenin daha büyük bir oranını temsil ettiğinden, bu tür bölünmelerin olasılığı o kadar artar.



10 dakikalık aralık genellikle kazanan bloğun aynı yükseklikte rakip bir blok bulunmadan önce geniş çapta yayılması için yeterli zaman sağlar. Bu, bölünmeleri sınırlayan, boşa harcanan bilgi işlem gücünü azaltan ve ağın küresel ölçekte senkronize kalmasına yardımcı olan bir uzlaşmadır.



### hashrate'yı Anlamak



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" tek bir madenci, bir grup madenci ya da Bitcoin'deki tüm madenciler tarafından saniyede üretilen hash hesaplama miktarını ifade eder. H/s` (saniye başına hash) olarak ifade edilir ve `TH/s` (saniye başına terahash) veya `EH/s` (saniye başına exahash) gibi katları vardır. Bu, madencilerin hedeften daha düşük bir hash elde etmek için her saniye yapabilecekleri deneme sayısını temsil eder.



Hedef sabit kalırsa, o zaman:




- her denemenin sabit bir başarı olasılığı vardır;
- saniye başına daha fazla deneme yapmak, kazanan bir denemenin hızlı bir şekilde ortaya çıkma olasılığını artırır


Başka bir deyişle, yarının Bitcoin ağı, iki kat daha fazla mining makinesi bağlayarak hesaplama gücünü iki katına çıkarırsa, düzeltici bir mekanizma olmadan, bloklar ortalama iki kat daha hızlı bulunacaktır. Bu nedenle hedef, hashrate değişimlerini telafi edecek şekilde ayarlanmalıdır.



### Zorluk hedefini ayarlama



Bitcoin bu sorunu, mining'ün zorluğunu ayarlayan periyodik bir hedef ayarlama mekanizması ile çözmektedir. Prensip şu şekildedir: her 2016 blokta (yaklaşık 2 haftada bir), her düğüm bu 2016 blokları üretmek için gerçekte ne kadar zamana ihtiyaç duyulduğunu gözlemleyerek zorluk hedefini yeniden hesaplar.



Bu mekanizmanın amacı, makinelerin bağlantısının kesilmesi veya tam tersine yeni makinelerin eklenmesi nedeniyle ağın genel hashrate'ü sürekli değişirken, bir bloğun ortalama üretim süresini yaklaşık 10 dakikaya düşürmektir.



![Image](assets/fr/023.webp)



Hesaplama, geçen süre için gözlemlenen zamana dayanmaktadır:




- eğer son 2016 blokları çok hızlı bir şekilde bulunduysa, bu hashrate'in bu dönemde arttığı anlamına gelir; Bitcoin daha sonra bir sonraki dönem için hedefi düşürerek durumu daha da zorlaştırır;
- 2016 blokları çok yavaş bulunursa, bu hashrate'nin azaldığı anlamına gelir; Bitcoin hedefi artırarak durumu hafifletir.



Formül aşağıdaki gibidir:



```txt
Tn = To * (Ta / Tt)
```



Ile:




- `tn`: yeni hedef
- `to`: eski hedef
- ta`: son 2016 blok için geçen gerçek zaman
- `Tt`: hedef zaman (saniye cinsinden)



İki haftalık bir hedef süre ile, yani `Tt = 1,209,600` saniye:



```txt
Tn = To * (Ta / 1 209 600)
```



Bitcoin mining'in zorluğunun nasıl ayarlanacağını anlamak için, burada hayali değerlerle bir örnek verilmiştir:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Ile:



- `**To = 18,045,755,102**`: Eski hedef, yani ayarlamadan önceki referans değer.
- `**ta = 1.000.000 saniye**`: Son 2016 bloğu üretmek için fiilen harcanan süre. Bu süre hedef süreden daha az olduğu için ağ çok hızlı madencilik yapmıştır.
- `**1,209,600 saniye**`: Ayarlama için referans olarak kullanılan 2016 blokları için blok başına 10 dakikaya karşılık gelen hedef süre.
- `**tn = 14,918,779,020**`: Zorluk ayarlamasından sonra hesaplanan yeni hedef.



Burada yeni hedef eskisinden daha düşüktür, bu da mining'in bir sonraki dönemde blok üretimini yavaşlatmak için daha da zorlaştığı anlamına gelmektedir.


*Bu örnekteki hedef değerler öğretim amacıyla basitleştirilmiş ve ölçeklendirilmiştir; Bitcoin'de kullanılan gerçek hedef tamamen farklı büyüklükte 256 bitlik bir tamsayıdır.*



Bu hesaplama, bloklara girilen zaman damgalarına dayalı olarak her düğüm tarafından yerel olarak gerçekleştirilir. Tüm düğümler aynı kuralları uyguladıklarından aynı sonuca ulaşırlar ve yeni hedef sonraki 2016 blokları için ortak referans olur.



Bu ayarlamayla ilgili dikkat edilmesi gereken önemli bir ayrıntı var: **sınırlıdır**. Bitcoin, onu bloke edebilecek çok ani değişikliklerden kaçınmak için dönem başına zorluktaki değişimi sınırlar. Aslında, dikkate alınan gerçek zaman 4 katına eşdeğer bir aralıkta kalacak şekilde sınırlandırılmıştır (minimum eski hedefin dörtte biri, maksimum eski hedefin dört katı). Bu, zaman damgalarının son derece atipik olması veya manipüle edilmesi durumunda aşırı yeniden hedeflemeyi önler.



### Hedef temsil



Blok başlığında, çok fazla yer kaplayacağı için hedef tam 256 bit biçiminde görünmez. Bunun yerine, 32 bitlik `nBits` alanı hedefi 256 tabanlı bilimsel gösterimle karşılaştırılabilir kompakt bir formatta kodlar: bir üs (1 bayt) ve bir katsayı (3 bayt). Hedefin tamamı daha sonra bu iki değerden yeniden yapılandırılır. Konu nispeten karmaşık olduğu ve mining'ün anlaşılmasına hiçbir şey katmadığı için burada ayrıntıya girmeyeceğiz. Sadece hedefin blok başlığında ham formda değil, kompakt formda saklandığını unutmayın.



Bölüm I'in bu son bölümü ile proof-of-work'in Bitcoin'de nasıl çalıştığına dair bir tur attık: madenci kendi mempool'undan işlemleri seçerek bir aday blok oluşturur, aday blok başlığını hesaplar, hash eder, elde edilen hash'i dönem hedefiyle karşılaştırır, ardından geçerli bir hash elde edilene kadar nonce'u değiştirerek yeniden başlar. Son olarak, her 2016 blokta bir ağ, hashrate'daki sürekli değişimlere rağmen blok başına ortalama 10 dakikalık bir süreyi korumak için yeni bir hedefi yeniden hesaplar.




# Bitcoin mining teşvik sistemi


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Tahmin edebileceğiniz gibi, Bitcoin mining fedakar bir faaliyet değildir. Miner'lerin gerçek maliyetleri vardır: mining bilgisayarlarını çalıştırmak için elektrik, özel ekipman alımı, bakım için maaş, bazen bina ve soğutma sistemleri. Bitcoin sisteminin işleyebilmesi için madencilerin özel çıkarlarının ağın kolektif çıkarlarıyla uyumlu olması gerekir. mining ödülünün rolü de tam olarak budur. Madencileri proof of work'e yatırım yapmaya, geçerli işlemleri dahil etmeye ve protokolü bozmaya çalışmak yerine protokolün kurallarına saygı göstermeye teşvik eder.



Bu mantık oyun teorisine dayanır: protokol dürüstlüğü rasyonel hale getirir. Bir madenci, düğümler tarafından kabul edilen geçerli bir blok ürettiğinde para kazanır. Tersine, hile yapmaya çalışırsa, bloğu düğümler tarafından reddedilecek ve hiçbir şey alamayacaktır. Bir blok üretmenin bir maliyeti olduğundan, reddedilen bir blok doğrudan bir kaybı temsil eder. Binlerce oyuncunun aynı anda geçerli bir blok aradığı rekabetçi bir ortamda, çoğu zaman en karlı strateji kurallara sıkı sıkıya uymak ve gelirinizi dürüstçe maksimize etmektir.



Bunu başarmak için, Bitcoin protokolü, geçerli bir blok bulan madencinin, madenciye belirli bir BTC toplamı veren belirli bir işlemi dahil etme hakkını kazanmasını şart koşar. Bu **[blok ödülü](https://planb.academy/resources/glossary/block-reward)** olarak bilinir. Bu bölümün bu ilk kısmında amaç, bunun nelerden oluştuğunu ve nasıl belirlendiğini anlamaktır. Daha sonra, para yaratma kısmının zaman içinde nasıl geliştiğini (halvings ile) ve teknik olarak nasıl toplandığını (coinbase işlemi yoluyla) göreceğiz.



### Blok ödülü nelerden oluşuyor?



Önceki bölümlerde madencilerin geçerli bir bloğu nasıl bulduklarını gördük. Bir madenci, hash değeri hedeften küçük olan bir başlık bulduğunda, aday bloğu geçerli kabul edilir. Daha sonra bunu tüm Bitcoin ağına dağıtabilir. Blok, içerdiği işlemleri onaylayarak blok zincirinin geri kalanına eklenir.



Kazanan madenciye bir ödül verilmesini tetikleyen de tam olarak bu olaydır (bloğun blok zincirine fiilen eklenmesi). Bu ödül, birbirine eklenen iki farklı unsurdan oluşur:




- [blok sübvansiyon](https://planb.academy/resources/glossary/block-subsidy)**;
- işlem ücretleri**.



![Image](assets/fr/024.webp)



Şimdi ödülün bu iki bölümünün neye karşılık geldiğine bir göz atalım.



### Blok sübvansiyon



Blok sübvansiyonu, ödülün parasal yaratım kısmına karşılık gelir. Bir madenci geçerli bir blok ürettiğinde, protokol ona belirli sayıda yeni bitcoin yaratma ve bunları ödül olarak kendisine tahsis etme yetkisi verir. Bu bitcoinler ex nihilo olarak yaratılır. Daha önce var olmamışlardır.



Ancak, yeni yaratılan bitcoinlerin miktarı hiçbir şekilde keyfi değildir. Bitcoin protokol kuralları tarafından kesin olarak tanımlanmıştır ve tüm madenciler için aynıdır. Bir sonraki bölümde bu mekanizmaya daha yakından bakacağız, çünkü sübvansiyon sonsuza kadar sabit bir değer değildir: kesin bir programa göre periyodik olarak bölünür. Şimdilik sadece şunu hatırlayın:




- blok sübvansiyonu, blok ödülünün iki bileşeninden biridir;
- sınırlandırılmıştır ve madenci tarafından değil protokol tarafından belirlenir (madenci teknik olarak maksimum miktardan daha azını talep edebilse bile);
- havadan bitcoin yaratıyor.



Bu sübvansiyon Bitcoin protokolünde iki ana rol oynamaktadır. Birincisi, oyuncuları mining'a katılmaya teşvik etmektir. Bitcoin'un ilk yıllarında (ve bazen bugün hala), işlem ücretleri çok düşüktü. Bu nedenle sübvansiyon, madencileri çekmek ve sistem için bir güvenlik seviyesi sağlamak için yeterli tazminatı garanti etmiştir.



İkinci rol para biriminin dağıtımı ile ilgilidir. Her yeni para birimi, para birimlerinin nüfusa nasıl adil bir şekilde dağıtılacağı sorusuyla karşı karşıyadır. Blok sübvansiyonu bu soruna bir yanıt sağlamaktadır. mining aracılığıyla bitcoinler yaratarak, ilk dağıtımlarını açık ve tarafsız bir şekilde sağlar: mining'e katılmaları koşuluyla, önceden yetkilendirme veya kimlik tespiti gerekmeden herkes bunları elde edebilir.



Öte yandan, bu bitcoinler yoktan var edildikleri için, değerleri temelsiz değildir. Sübvansiyon, dolaşımdaki para miktarını arttırarak mevcut bitcoinlerin değerini mekanik olarak seyreltmektedir. Dolayısıyla bir tür parasal enflasyona yol açmaktadır. Ancak bir sonraki bölümde bu sübvansiyonun kademeli olarak ortadan kalkacağını ve enflasyonun eninde sonunda sona ereceğini göreceğiz.



![Image](assets/fr/025.webp)



### İşlem ücretleri



Blok ödülünün ikinci bileşeni sistem kullanımıyla bağlantılıdır: bir kullanıcı bir işlem gönderdiğinde, bunun onaylanmasını ister. Ancak blok alanı sınırlıdır ve bloklar ortalama olarak her 10 dakikada bir görünür. Bu nedenle blok alanı kıt bir kaynaktır. Talep arzı aştığında fiyat yükselir: bu işlem ücreti piyasasıdır. Geçerli bir blok üretmeyi başaran her madenci, bloğuna dahil ettiği tüm işlemlerle ilgili işlem ücretlerinin tamamını kendi hesabına tahsil etme hakkını elde eder.



Bunu bir açık artırma sistemi olarak düşünebilirsiniz: her işlem bir ücret tutarı önerir ve madenciler alan kısıtlamaları altında gelirlerini en üst düzeye çıkaranlara öncelik verir. Bu mekanizma doğal olarak çıkarları hizalar:




- acelesi olan kullanıcılar hızlı bir şekilde dahil olmak için daha fazla ödeme yapar;
- madenciler, blok alanı için en yüksek ücretleri ödeyen işlemleri dahil etmeye teşvik edilir.
- ağ spam'i önler, çünkü bir işlemi yayınlamanın bir maliyeti vardır.



#### İşlem ücretleri nasıl hesaplanır?



Genel kanının aksine, ücretler bir Bitcoin işleminin çıktısı değildir. Aslında, bir işlem girdileri harcar ve çıktıları oluşturur. Girdiler kullanılan bitcoinlerin kaynağını temsil ederken, çıktılar ödemelerin hedefini temsil eder. İşlem ücretleri basitçe **toplam girdiler ve toplam çıktılar arasındaki farktır**.



Başka bir deyişle, kullanıcının kendisine ait olan bitcoin girdileri, alıcılar için çıktılar yaratır, ancak girdiler tarafından tüketilen miktarın tamamını yeniden üretmez. İkisi arasındaki fark, madencinin toplayabileceği işlem ücretlerini temsil eder.



Bir örnek ele alalım. Bir işlem, biri `100.000 sats` diğeri `150.000 sats` olmak üzere iki girdi tüketir ve `35.000 sats`, `42.000 sats` ve `170.000 sats` olmak üzere üç çıktı oluşturur.



![Image](assets/fr/027.webp)



Dolayısıyla girdilerin toplamı `250,000 sats`, çıktıların toplamı ise `247,000 sats`tür. Bu, `3,000 sats`ün çıktılarda yeniden yaratılmadan girdilerde tüketildiği anlamına gelir: bu miktar, bu işlem tarafından önerilen ücretlere karşılık gelir.



![Image](assets/fr/028.webp)



Bir madenci bu işlemi geçerli bir bloğa dahil ederse, blokta yer alan diğer tüm işlemlerin ücretlerine ek olarak bu `3.000 sats`yı geri alma hakkına sahip olacaktır. Ancak, ücreti ödeyen işlem ile madenci tarafından fiilen tahsil edilen on-chain arasında doğrudan bir sats bağlantısı yoktur. Teknik olarak, ücretlerdeki `3.000 sats` yok edilir ve karşılığında madenci aynı miktarı kendisi için yeniden yaratma hakkını elde eder.



#### Ücret oranı



Bir blok işlem sayısı ile değil, toplam kapasitesi ile sınırlıdır (bugün pratikte bloğun ağırlığı ile). Bazı işlemler diğerlerinden daha fazla yer kaplar: çok sayıda girdi ve çıktısı olan bir işlem, tek girdi ve iki çıktısı olan basit bir işlemden daha büyük olacaktır. Kullanılan komut dosyaları da boyutu etkileyecektir.



![Image](assets/fr/026.webp)



Bu nedenle iki işlem mutlak olarak aynı miktarda ücret ödeyebilir, ancak madenci açısından ekonomik olarak eşdeğer olmayabilir. Biri iki kat daha büyükse, blokta iki kat daha fazla alana mal olur. Alan azdır, bu nedenle madenci birim alan başına gelirini maksimize etmeye çalışır.



Bu nedenle, uygulamada bir işlemin rekabet gücünü genellikle `sats/vB` (sanal bayt başına satoshis) cinsinden bir ücret oranıyla ifade ederiz. Bu oranın hesaplanması basittir:



```text
fee rate = fee / weight (in vB)
```



Örneğin, `141 vB` ağırlığında ve `1,974 sats` ücret tahsis eden bir işlemimiz varsa, `14 sats/vB` ücret oranına sahip olacaktır.



```text
1 974 / 141 ≈ 14 sats/vB
```



Bu oran madenciler tarafından yapılan ekonomik seçimleri açıklar: sabit kapasitede, yüksek oranlı işlemleri dahil etmek bloğun toplam ücretlerini ve dolayısıyla madencinin ücretini maksimize eder. Aynı zamanda düşük maliyetli işlemlerin mempool'larda neden uzun süre kuyrukta kaldığını da açıklar: birim alan başına daha fazla ödeme yapan diğer işlemlerle rekabet ederler.



### Spam'e karşı ağ koruması



Ücretler aynı zamanda operasyonel bir güvenlik amacına da hizmet eder: işlemlerin çoğaltılmasına bir maliyet getirirler. Bir işlemi yayınlamak ücretsiz olsaydı, ağı gereksiz işlemlerle doldurmak ve mempool'ları doyurmak kolay olurdu, bu da düğümler üzerindeki yükü artırırdı.



Uygulamada, düğümler yerel aktarım politikaları (mempool kuralları) uygular ve genellikle bir işlemi aktarmayacakları minimum bir ücret eşiği belirlerler (varsayılan olarak, `minRelayTxFee` aracılığıyla Bitcoin Core'da `0,1 sat/vB`). Bir işlem mutabakat kuralları açısından geçerli olabilir, ancak ücretleri çok düşükse çoğu düğüm tarafından iletilmeyebilir. Sonuç olarak, işlem dolaşıma girmez, madencilere ulaşmaz ve onaylanma şansı çok azdır.



Bu noktada, blok ödülünün özünü anladınız: kazanan madencinin tazminatına karşılık gelir ve iki farklı unsurdan oluşur. Bir yanda, protokol kuralları tarafından tanımlanan ve ex nihilo yeni bitcoinler yaratan bir blok sübvansiyonu. Diğer yanda ise, madenciliği yapılan bloğa dahil edilen işlemlerin ücretleri.



Bir sonraki bölümde, tam olarak nasıl hesaplandığını ve Bitcoin protokolünün kurallarına göre zaman içinde nasıl geliştiğini anlamak için blok sübvansiyona daha ayrıntılı olarak odaklanacağız.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



Bir önceki bölümde, geçerli bir blok üreten madencilerin, blokta yer alan işlemlerin ücretlerinden ve bir blok sübvansiyonundan oluşan bir ödül aldığını gördük. Ancak, bu sübvansiyon miktarının nasıl belirlendiğini henüz açıklamadık. Bu değeri belirleyen ve geliştiren mekanizma ***[halving](https://planb.academy/resources/glossary/halving)*** olarak bilinir.



### Yarıya indirmek nedir?



Halving, Bitcoin protokolünde programlanan ve blok sübvansiyonunu, yani kazanan madencinin her blokta yaratmasına izin verilen maksimum yeni bitcoin miktarını yarıya indiren bir olaydır. İşlem ücretlerini etkilemez: ücretler bağımsız olarak mevcuttur ve kullanıcı etkinliği ve blok alanı için rekabet tarafından belirlenmeye devam eder.



Bitcoin 2009 yılında piyasaya sürüldüğünde, blok sübvansiyonu çıkarılan her blok için 50 BTC olarak belirlenmişti. O zamandan bu yana, bu sübvansiyon her yarılanma için birkaç kez yarıya indirildi.



![Image](assets/fr/029.webp)



Halving bir tarih tarafından değil, blok yüksekliği tarafından tetiklenir. Her 210.000 blokta bir** çalıştırılır. Bitcoin blok başına yaklaşık 10 dakikalık bir ortalama aralığı hedeflediğinden, 210.000 blok kabaca dört yıla karşılık gelir.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Dolayısıyla, `n` halihazırda gerçekleşmiş olan yarılanma sayısını not edersek, BTC'daki blok sübvansiyon aşağıdaki gibi hesaplanabilir:



```text
subsidy(n) = 50 / 2^n
```



### Geçmiş yarılanmalar



İşte blok yüksekliği, tarihi ve olaydan sonra uygulanacak yeni blok sübvansiyonu ile birlikte halihazırda gerçekleşmiş olan yarılanmaların özet tablosu:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Sübvansiyon ne zaman ve nasıl sona eriyor?



Sübvansiyon sistemin minimum birimiyle ifade edilebildiği sürece Halving tekrarlanır: satoshi.



```text
1 BTC = 100 000 000 sats
```



Sübvansiyon yarıya indirildikçe, sonunda 1 satoshi'den daha az olacak kadar küçük bitcoin kesirlerine ulaşırız. Bu noktada, yarım birim satoshi yaratmak artık mümkün değildir. Blok sübvansiyonu yoluyla para yaratılması durur ve madenciler yalnızca işlem ücretleri temelinde telafi edilir. Bu noktadan itibaren, tüm bitcoinler dolaşımda olacak ve artık yeni birimler üretmek mümkün olmayacaktır.



Blok sübvansiyonlarının kesin sonu 6,930,000 blok seviyesinde, yani 33. ve son yarılanmada gelecektir. Bu olayın 2140 yılı civarında gerçekleşmesi beklenmekle birlikte, kesin bir tarih vermek mümkün değildir, çünkü o zamana kadar blokların bulunma hızına bağlı olacaktır.



Blok sübvansiyonu her yarılanmada 1/2 oranında geometrik bir dizi izlediğinden, Bitcoin'ün ilk günlerinde para yaratımı son derece yüksekti ve daha sonra çok hızlı bir şekilde azaldı. Yedinci yarılanmaya kadar bitcoinlerin %99'undan fazlası dolaşıma girmiş olacaktır. 99 eşiğinin 2032 ile 2036 yılları arasında aşılması beklenmektedir. Bu da bitcoinlerin kalan son %1'ini çıkarmak için 100 yıldan fazla zaman gerekeceği anlamına gelmektedir. Bitcoin piyasaya sürüldüğünde, para biriminin yaygın dağıtımını sağlamak için parasal enflasyon çok yüksekken, şimdi çok düşüktür ve dolaşımdaki arzı artık artamayan gerçek bir sabit para birimi seviyesine ulaşana kadar düşmeye devam edecektir.



![Image](assets/fr/030.webp)



### Neden hiçbir zaman 21 milyon BTC olmayacak?



Bitcoin'in maksimum para arzı genellikle 21 milyon BTC olarak sunulur. Bu, para politikasını anlamak için iyi bir yaklaşımdır, ancak tamamen teknik bir bakış açısından, toplam arz hiçbir zaman tam olarak 21.000.000 bitcoin'e ulaşmayacaktır.



Bunun ana nedeni mekaniktir. Birbirini takip eden yarılanmalarla blok sübvansiyonu sonunda minimum değer olan 1 sat'ın altına düşer ve bu da tam teorik toplama ulaşmadan önce ihracı sona erdirir. Bu minimum ayrıntı ve yuvarlama kurallarının bir sonucu olarak, sübvansiyon tarafından yaratılan toplam bitcoin sayısı 21 milyondan biraz daha azdır.



Buna ek olarak, protokolle ilgili marjinal sapmalar da buna katkıda bulunabilir. Örneğin, nadir durumlarda, bazı madenciler tam sübvansiyonlarını talep etmemiş olabilir, bu da gerçekte çıkarılan bitcoin miktarını kesin olarak azaltır. Ayrıca, Satoshi tarafından 3 Ocak 2009'da üretilen ve yaratılan bitcoinleri UTXO set'nin bir parçası olmayan genesis bloğundan ve yinelenen coinbase işlem tanımlayıcıları gibi hatalarla bağlantılı belirli tarihsel olaylardan da bahsedebiliriz.



Son olarak, imha edilen veya bloke edilen tüm bitcoinleri de hesaba katmalıyız:




- çözülemeyen senaryolarda kilitli bitcoinler;
- gW-219 senaryoları tarafından kasıtlı olarak yok edilenler;
- veya uygulama düzeyinde özel anahtarların kaybı.



Teorik olarak, Bitcoin'nin arzı bu nedenle 21 milyon ile sınırlıdır. Ancak pratikte hiçbir zaman dolaşımda 21 milyon bitcoin olmayacaktır.



## Coinbase işlemi


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Önceki bölümlerde iki önemli noktaya değinmiştik. İlk olarak, geçerli bir blok üretmeyi ve dağıtmayı başaran madenci bir ödül alır. Öte yandan, bu ödülün iki farklı unsurdan oluştuğunu gördük:




- blok sübvansiyonu (ex nihilo olarak yaratılan, maksimum miktarı protokol tarafından belirlenen ve yarılanmalar yoluyla kademeli olarak azaltılan bitcoinler);
- işlemleri bloğa dahil edilen kullanıcılar tarafından ödenen tüm işlem ücretleri.



Ancak geriye bir soru kalıyor: Madenci bu ödülü Bitcoin'de hangi mekanizma ile topluyor? Bu tam olarak "coinbase" adı verilen belirli bir işlemin rolüdür.



### Coinbase işlemi nasıl çalışır?



Dersin ilk bölümünde gördüğümüz gibi, her Bitcoin bloğu onaylayacağı bekleyen işlemlerin bir listesini içerir. Bunlardan ilki her zaman coinbase işlemidir. Kazanan madencinin ödülünü almasını sağlayan şey budur.



![Image](assets/fr/031.webp)



İlk bakışta, klasik bir Bitcoin işlemi gibi görünür: bir TXID'ye sahiptir, çıkış yapar ve bloğun Merkle ağacına dahil edilir. Ancak, önemli bir açıdan farklılık gösterir: mevcut herhangi bir UTXO'ü harcamaz.



Klasik bir Bitcoin işleminde, "girdiler" girdi değerini sağlayan önceki harcanmamış çıktıları (UTXO'lar) referans alır. Çıktılar daha sonra bu değeri yeni harcama koşullarıyla yeni UTXO'lara yeniden dağıtır. Başka bir deyişle, bitcoin göndermek için zaten bitcoin sahibi olmanız gerekir. Öte yandan coinbase işlemi girdi olarak bitcoin tüketmez: çıktı olarak doğrudan sıfırdan bitcoin yaratır.



Blok sübvansiyonu yoluyla yeni bitcoinlerin dolaşıma girmesini sağlayan ve madenciye bloğa dahil edilen işlemlerle ilgili ücretleri yatıran tam da bu mekanizmadır. Coinbase işlemi mevcut gerçek bir UTXO'ye referans veremez (aslında hayali bir UTXO'ye referans verir), çünkü rolü tam olarak değerin bir kısmını (sübvansiyon) yaratmak ve diğer kısmını (ücretler) önceki bir işlemden almadan geri almaktır. Tüm sistemin tutarlı kalması için, ücretlere karşılık gelen kısım, girdilerde tüketilen ancak bloğun diğer işlemlerinde çıktılarda yeniden yaratılmayan bitcoinlerin toplamına tam olarak eşit olmalıdır.



![Image](assets/fr/032.webp)



Bu işlem isteğe bağlı değildir. Bir coinbase işlemi içermeyen bir blok geçersizdir ve ağ düğümleri tarafından sistematik olarak reddedilecektir.



⚠️ Lütfen dikkat: "*coinbase*" teriminin aynı adı taşıyan borsa platformuyla hiçbir bağlantısı yoktur. Bitcoin'de "*coinbase*" tarihsel olarak blok ödülünü yaratan işlemi ifade eder. Şirket, adı için bu terimi benimsemiştir.



Coinbase işlemi aslında aynı anda birkaç rolü yerine getirir:




- Bunlardan ilki az önce detaylandırdığımız gibidir: madenciye geçerli bir blok ürettiği için hak ettiği ödülü verir.
- Daha teknik olan ikinci rolü ise, blokta yer alan SegWit işlemlerinin tanıklarına (imzalarına) kriptografik bağlılık sağlamaktır.
- Bu kez doğrudan protokolle ilgili olmayan ancak mining'un modern sanayileşmesiyle bağlantılı olan üçüncü bir rol, coinbase'in artık sıklıkla rastgele teknik verileri sabitlemek için kullanılmasıdır. Bu veriler genellikle mining havuzlarının işleyişi ve iç organizasyonlarıyla bağlantılıdır.



Bu farklı kullanımları anlamanıza yardımcı olmak için şimdi coinbase işleminin yapısına daha yakından bakacağız.



### Coinbase işleminin temel yapısı



Bir coinbase işlemi tam olarak bir girdi içermelidir. Basitlik adına, bazen girdisi olmadığını söyleriz, çünkü bu girdi gerçek bir UTXO harcamaz. Gerçekte, referanslı bir kaynağa sahip bir girdi vardır, ancak kasıtlı olarak var olmayan bir UTXO'e işaret eder.



Daha önce gördüğümüz gibi, her Bitcoin işlemi geçerli çıktılar oluşturmak için UTXO'leri girdi olarak tüketmelidir. Bitcoin işleminde bu tüketim, mevcut bir UTXO'ün girdi olarak referans alınması şeklinde gerçekleşir. Bu referanslama basitçe bir önceki işlemin (UTXO'ün oluşturulduğu işlem) tanımlayıcısının yanı sıra bu işlemin çıktıları arasındaki indeksinin belirtilmesiyle yapılır. Somut olarak, bir UTXO bir hash (önceki TXID) ve bir indeks ile tanımlanır.



Ancak coinbase işlemi söz konusu olduğunda, mevcut gerçek bir UTXO'e atıfta bulunmak yerine, girdi, herhangi bir gerçek TXID'ye karşılık gelmeyen sıfırlarla dolu bir TXID ile bu özel sahte UTXO'e işaret etmelidir:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Hemen ardından yanlış indeks gelir:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



Temel Bitcoin protokolünde, Satoshi Nakamoto'te açıklandığı gibi, bu yanlış girdi coinbase işlemine uygulanan tek kısıtlamadır.



Bir işlemin girdisinde referans verilen herhangi bir UTXO gibi, bir `scriptSig` alanı ile ilişkilendirilir. Geleneksel bir işlemde, bu `scriptSig` alanı `scriptPubKey`i karşılamak ve böylece harcanan UTXO'in kilidini açmak için gereken öğeleri içerir. Ancak coinbase'in özel durumunda, referans verilen UTXO kasıtlı olarak hayali olduğundan, `scriptSig` alanı tamamen serbesttir. Bu nedenle Miner'ler istedikleri herhangi bir veriyi girebilirler. Bu özgürlüğün nasıl kullanıldığına daha sonra bakacağız.


Bu yanlış girdiye ek olarak, madencinin Bitcoin adreslerinden birinde ödülden bitcoinleri toplamasını sağlayan bir veya daha fazla mükemmel standart çıktı vardır. Bu çıktılar bir `scriptPubKey` tarafından kilitlenmiş UTXO'lardır (örneğin madenci veya havuz tarafından kontrol edilen bir adrese işaret eden bir komut dosyası). Buradaki tek özellik, değerlerini hesaplama kuralında yatmaktadır: coinbase'in çıktılarının toplamı, blok ücretlerinin eklendiği izin verilen maksimum sübvansiyonu asla aşmamalıdır.



Tarihsel olarak coinbase işlemi şu basit şemaya indirgenmiştir: var olmayan bir UTXO'ye atıfta bulunan sahte bir girdi ve blok ödülünü kazanan madenciye dağıtmak üzere tasarlanmış bir veya daha fazla çıktı. Ancak günümüzde coinbase artık bu dağıtım rolüyle sınırlı değildir. Bloktaki özel konumu ve yapısının büyük esnekliği, hem protokolün kendisinde hem de mining havuz yönetim mekanizmalarında yeni kullanımlara yol açmıştır.



### Diğer coinbase kullanımları



Zaman içinde coinbase işlemi, mining ve blok yapısının kendisi için yararlı olan çeşitli bilgileri entegre etmek için özellikle uygun bir ekleme noktası haline geldi. Genel coinbase organizasyonunu daha iyi anlamak için bunlara bir göz atalım.



#### BIP-34



BIP-34, Bitcoin bloklarının 2. sürümünü tanıtan 227.930 numaralı bloktan başlayarak Mart 2013'te dağıtılan bir fork soft'tur. Bu yeni sürüm, her bloğun coinbase işleminin `scriptSig`inde, oluşturulmakta olan bloğun yüksekliğini içermesini gerektirir.



Bir yandan bu evrim, ağın blok yapısını ve fikir birliği kurallarını geliştirmeyi kabul etme şeklini netleştirir. İkinci olarak, her bloğun ve coinbase işleminin benzersizliğini sağlar.



Bu nedenle, coinbase'in `scriptSig'i tamamen serbest değildir. BIP-34'ün etkinleştirilmesinden bu yana, bu coinbase işleminin dahil olduğu bloğun yüksekliği ile başlamak için kısıtlanmıştır.



![Image](assets/fr/035.webp)



#### Ekstra-önce



Bu dersin ilk bölümlerinde gördüğümüz gibi, madencinin blok başlığında 32 bitlik bir nonce alanı vardır ve bu alanı deneme yanılma yoluyla değiştirerek hedefe eşit ya da hedeften küçük bir hash bulur. Bu 32 bitlik alan zaten çok sayıda kombinasyonun keşfedilmesine izin verir, ancak mining zorluğu yüksek olduğunda, bu aralık nispeten kısa bir süre içinde tamamen tükenebilir ve bu nedenle geçerli bir hash üreten hiçbir kombinasyon vermeyebilir. Eğer `nonce'un olası tüm değerleri başarısızlıkla test edilmişse, madenci blok başlığını değiştirmek için başka bir öğeyi değiştirmeli ve yeni bir dizi deneme başlatmalıdır.



Coinbase işlemi, girdisinin `scriptSig`i aracılığıyla boş bir alan sunduğundan, nonce alanını genişletmek için kullanılan çözüm, bu `scriptSig`in bir kısmını kullanmaktır. Bu genellikle ekstra nonce olarak adlandırılır. Ekstra nonce'u değiştirerek, madenci coinbase'in `scriptSig'ini, yani işlem tanımlayıcısını, ardından bloğun Merkle kökünü ve son olarak blok başlığının kendisini değiştirir. Bu şekilde, aday bloklarının diğer bileşenlerini değiştirmek zorunda kalmadan keşfedecekleri yeni bir hash arama alanı elde ederler.



![Image](assets/fr/036.webp)



#### Havuzların ve madencilerin belirlenmesi



Günümüzde dünyadaki hashrate'nin çok büyük bir kısmı mining havuzlarında organize edilmektedir. Bu yapılar bireysel madencileri bir araya getirerek işlerini birleştirmekte ve gelirlerindeki değişkenliği azaltmaktadır.



Operasyonel nedenlerden ötürü, mining havuzları ayrıca coinbase girdisinin `scriptSig' boş alanını kullanarak çeşitli bilgi parçaları ekler. Bunlar havuzdan havuza ve ağ protokolünden ağ protokolüne değişir, ancak genellikle havuz içinde iş tekrarını önlemek için her madenciye atanan benzersiz bir tanımlayıcı (genellikle birkaç alt parçaya yapılandırılmış ekstra bir nonce) içerir. Genellikle, bulunan blokların halka açık atıfları, mining istatistikleri ve diğer izleme amaçları için kullanılan bir havuz tanımlama etiketi eklenir.



![Image](assets/fr/037.webp)



#### SegWit'ün taahhüdü



SegWit yumuşak fork'nın 2017'de etkinleştirilmesinden bu yana, özellikle Bitcoin işlemlerinin şekillendirilebilirlik sorununu düzeltmek için tanık verileri (yani genellikle imzalar) işlem ana verilerinden ayrılmıştır. Dolayısıyla bu ayrım, blokta işlenecek yeni bir unsur ortaya çıkarmaktadır.



Bunu yapmak için tanıklar, kökü daha sonra bir `OP_RETURN` çıktısı aracılığıyla coinbase işlemine işlenen başka bir özel Merkle ağacında gruplandırılır.



![Image](assets/fr/038.webp)



Bu makalenin kapsamı dışında olduğu için bu derste bu mekanizma hakkında daha fazla ayrıntıya girmeyeceğim, ancak SegWit'in piyasaya sürülmesinden bu yana coinbase işleminin tüm SegWit tanıklarını özetleyen bir parmak izini bloğa sabitlemek için bir araç görevi gördüğünü unutmayın. Tanıklar bağımsız bir Merkle ağacına yerleştirilir, bu ağacın kökü coinbase işleminin bir çıktısına yazılır ve bu coinbase işleminin kendisi, kökü blok başlığında görünen diğer tüm işlemlerle birlikte ana Merkle ağacına dahil edilir. Bu şekilde, ana işlem verilerinden ayrı olarak saklanan tanıklar yine de blok başlığına işlenir.



![Image](assets/fr/039.webp)



#### Keyfi mesajlar



ScriptSig` madenci tarafından seçilen keyfi bilgilerin serbestçe eklenmesine izin verdiğinden, bazıları bu fırsattan yararlanarak teknik mesajlardan ziyade daha kişisel nitelikte mesajlar eklemişlerdir. En ünlü örnek elbette artık ikonik hale gelmiş mesajıyla Satoshi Nakamoto'dur:



> The Times 03/Jan/2009 Şansölye bankalar için ikinci kurtarma paketinin eşiğinde

Genesis bloğunda (Bitcoin'ın ilk bloğu) bulunan bu mesaj aslında coinbase işleminin `scriptSig'inde onaltılık olarak kodlanmıştır:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Vade süresi


Blok çıkarılıp dağıtıldıktan sonra, coinbase işlemi diğer işlemler gibi blok zincirinde görünür. Kazanan madenci için UTXO'ler yaratarak ödüllerini almalarını sağlar. Ancak, bu UTXO'ler hemen harcanamaz: bir vade süresine tabidirler. Bu vade, coinbase'i içeren bloktan sonraki 100 blok olarak belirlenmiştir. Somut bir ifadeyle, coinbase işleminin çıktılarının kazanan madenci tarafından harcanabilir hale gelmesi için toplam 101 onay alması gerekir.


![Image](assets/fr/040.webp)


Bu kuralın amacı zincirin yeniden düzenlenmesinin ekonomi üzerindeki etkisini sınırlamaktır. Önceki bölümlerde gördüğümüz gibi, aynı yükseklikte farklı madenciler tarafından neredeyse aynı anda iki farklı geçerli blok bulunabilir. Kısa bir süre için ağ bölünebilir: bazı düğümler önce A bloğunu alırken, diğerleri önce B bloğunu görür. Daha sonra, sonraki bloklar boyunca, iki daldan biri daha fazla iş biriktirir ve referans dal haline gelir. Diğer dal terk edilir ve blokları kullanılmaz hale gelir. İçerdiği işlemler daha sonra teorik olarak onay bekleyen mempool'lara geri dönebilir.



Uygulamada bu nadiren gerçekleşir, çünkü ücret piyasası genellikle neredeyse aynı işlemlerin aynı yükseklikte iki rakip blokta görünmesine neden olur. Bu, bir Bitcoin işleminin genellikle altı teyitten sonra değişmez hale geldiğinin düşünülmesinin nedenlerinden biridir: altı bloktan daha fazla yeniden düzenlemeler o kadar düşük bir ihtimaldir ki, makul bir şekilde imkansız olarak kabul edilebilirler.



![Image](assets/fr/041.webp)



Coinbase işlemi söz konusu olduğunda bu yeniden düzenlemelerle ilgili sorun, bunun sıradan bir işlem olmamasıdır. Bu işlem dolaşıma yepyeni bitcoinler sokmaktadır. Blok ödülü hemen harcanabilseydi, sorunlu bir kaskad durumu ortaya çıkabilirdi:




- bir madenci coinbase'den bitcoin harcıyor,
- bu bitcoinler ekonomide dolaşıma giriyor,
- daha sonra orijinal blok yeniden yapılanma sırasında terk edildi.



Bu durumda dolaşımdaki bitcoinler son zincirde hiç var olmamış olacak ve verildiği anda geçerli olan bir dizi işlem sonradan geçersiz hale gelecektir.



Vade süresi, bu senaryoyu gerçekçi olmaktan çıkaracak kadar uzun bir zaman dilimini dayatmaktadır. Pratikte 101 bloğun yeniden düzenlenmesinin imkansız olduğu düşünülmektedir (sonsuz küçük bir olasılık olsa bile). Satoshi'ün vade için neden bu kadar yüksek bir değer seçtiğini tam olarak bilmiyoruz, ancak mekanizmanın büyük ağ arızaları durumunda bile işlevsel kalması için seçilmiş olması muhtemeldir.



Bu kural, yeni yaratılan blok-ödül parasının, generated bloğu büyük miktarda birikmiş işin altına güvenli bir şekilde gömülmeden önce dolaşmaya başlamasını önler.



---

Bitcoin mining'nin nasıl çalıştığına dair açıklamamızın sonuna geldik. Artık ilgili temel mekanizmalar hakkında net bir resme sahip olmalısınız.



Kursun son bölümünde, Bitcoin mining'un gerçek dünyada nasıl gerçekleştiğini göstermek için daha somut yönlere döneceğiz: sanayileşmesi, kullanılan makineler, oyuncuların gruplandırılması vb. Amaç, size Bitcoin mining'un hem az önce gördüğümüz teorik ve protokol perspektifinden hem de pratik ve operasyonel yönünden genel bir görünümünü vermek olacaktır.



# Bitcoin mining endüstrisi


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## mining makinelerinin evrimi


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Bitcoin'ün ilk günlerinde mining endüstriyel bir faaliyet değildi. Bitcoin yazılımının bir parçasıydı ve genellikle meraktan, bazen ağı desteklemek için ve ikincil olarak da o zamanlar neredeyse hiç piyasa değeri olmayan bitcoinleri elde etmek için kişisel bir bilgisayarda başlatıldı.



Yıllar içinde bu faaliyet bir dönüşüm geçirdi: makineler değişti, zorluklar arttı ve mining kendi başına bir endüstri haline geldi. Şimdi Bitcoin mining'nın operasyonel yönlerine bir göz atalım.



### Başlarken: Bir CPU ile mining



2009 yılında ve ilk yıllarda, mining esas olarak geleneksel bir bilgisayarın CPU'su kullanılarak gerçekleştirilmiştir. Bitcoin o zamanlar sadece bir wallet, bir düğüm ve bir madenci olarak hizmet veren basit bir yazılım parçasıydı. Satoshi Nakamoto'in yazılımını kişisel bilgisayarınızda başlatmak, mining sürecine katılmak ve çoğu durumda blok bulmak için yeterliydi.



Bir CPU her şeyi yapabilir, ancak hiçbir şey için optimize edilmemiştir. Çok genel talimatları karmaşık bir mantıkla yürütür. Blok başlıklarının tekrarlayan hash'i gibi bir görev için ideal bir araç değildir, ancak ağ başlangıcında zorluk o kadar düşüktür ki blokları bulmak için fazlasıyla yeterlidir.



Bu dönem önemlidir, çünkü bize önemli bir noktayı hatırlatmaktadır: proof of work belirli bir ekipman kategorisine bağlı değildir. Önemli olan, belirli bir maliyetle hash'leri diğerlerinden daha hızlı hesaplama becerisidir. Teknik bir avantaj ortaya çıkar çıkmaz, otomatik olarak ekonomik bir avantaja dönüşür. Ancak mutlak anlamda, bugün hala geleneksel bir CPU kullanarak Bitcoin bloklarını bulmaya çalışmak mümkündür. Örneğin NerdMiner projesi tarafından benimsenen yaklaşım budur. Bir blok bulma şansı neredeyse sıfırdır, ancak yine de sonsuz küçük bir olasılık vardır.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### GPU'lara geçiş



Çok geçmeden madenciler darboğazın güç değil, çok sayıda benzer işlemi paralel olarak gerçekleştirme becerisi olduğunu fark etti. Grafik işlem birimlerinin (GPU'lar) yapabildiği de tam olarak buydu. Başlangıçta bir GPU, büyük miktarlarda veri üzerinde aynı işlemleri gerçekleştirmek üzere tasarlanmıştı. Bu mimari, tekrarlanan hashing gibi bir görev için mükemmel bir şekilde uygundu: çok yönlü birkaç çekirdeğe sahip olmak yerine, aynı talimatları aynı anda yürütebilen yüzlerce, daha sonra binlerce üniteye sahip olursunuz.



Karşılaştırılabilir güç tüketimi ile bir GPU, saniyede bir CPU'dan çok daha fazla hash üretebilir. Aynı zamanda, bitcoin dolar karşısında bir döviz kuruna sahipti, değeri artıyordu ve değişim platformları ortaya çıkıyordu. O andan itibaren mining'ün doğası değişmeye başladı. Artık sadece katılmakla ilgili değil, para kazanmakla ilgiliydi. Özel konfigürasyonlar ortaya çıktı: birkaç grafik kartı etrafında inşa edilmiş, bazen ekransız, minimal bir sisteme ve tek amacı madencilik yapmak olan özel yazılımlara sahip makineler.



İşte bu noktada mining'nın zorluğu patlamaya başladı. Hatta 2010 ortası ile 2011 ortası arasında 1.000 kat artmıştır. Mekanik olarak, tıpkı sanayileşmenin ilk biçimlerinde olduğu gibi uzmanlaşma başladı ve kişisel bilgisayarlarında Bitcoin yazılımını çalıştırmakla yetinen sıradan kullanıcıların geçerli bir blok bulma şansı artık çok az.



![Image](assets/fr/044.webp)



*Kaynak: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



GPU dönemi ile modern ASIC dönemi arasında bir ara aşama vardı: FPGA kullanımı. Bir FPGA yeniden programlanabilir bir bileşendir: belirli bir hesaplamaya, bu durumda `SHA256d`ye adanmış bir mantık devresini doğrudan uygulamak üzere yapılandırılabilir. Buradaki fikir, enerji verimliliği elde etmek için genel amaçlı donanımdan (CPU/GPU) daha da uzaklaşmaktı. Ancak yakında, FPGA'larda sanal olarak yapılan iyileştirmeler fiziksel olarak çiplerin kendilerine uygulanacaktı: ASIC'in gelişi budur.



### ASIC'nin gelişi



mining donanımının uzmanlaşmasındaki son aşama ASIC'ların (*Uygulamaya Özel Entegre Devreler*) ortaya çıkmasıydı. Bir ASIC tek bir görev için tasarlanmış bir çiptir. Bitcoin mining durumunda, bu görev tam olarak `SHA256d`nin maksimum hızda ve optimum enerji verimliliği ile yürütülmesidir. Bir GPU'nun aksine, ASIC oyun, 3D render veya yapay zeka çalıştırmak için kullanılmaz. Sadece hashing için kullanılır.



![Image](assets/fr/045.webp)



*Bitmain tarafından üretilen ASIC S21 XP*



Bu uzmanlaşmanın iki önemli sonucu vardır:




- Birincisi, performans ve verimlilikte bir sıçrama. Karşılaştırılabilir nesil cihazlar için bir ASIC, daha az güç tüketirken bir GPU'dan saniyede çok daha fazla karma üretir. GPU'lu Mining hızla rekabet edilemez hale geldi: teknik olarak işe yarasa da, elektrik maliyeti çoğu bağlamda beklenen gelirden çok daha ağır basıyordu;
- İkincisi ise bir model değişikliğidir: yatırım esas olarak endüstriyel sınıf donanıma kaymıştır. Mining artık bu amaç için tasarlanmış makinelerin satın alınmasını, sürekli olarak çalıştırılmasını, soğutulmasını, bakımının yapılmasını ve eskime sürelerinin absorbe edilmesini içeriyor. Çünkü bir ASIC ekonomik olarak ebedi değildir: yeni, daha verimli bir nesil piyasaya çıktığında, eski makineler işlevsel kalsalar bile giderek daha az karlı hale gelirler.



Bu noktadan sonra artık sadece bir hobiden bahsetmiyoruz. Rekabet gücünün bir denkleme bağlı olduğu bir sektörden bahsediyoruz:




- elektrik maliyeti;
- ekipman maliyeti ve amortisman;
- büyük ölçekte soğutma ve çalıştırma yeteneği;
- makine kullanılabilirliği ve güvenilirliği;
- iletişim hızı;
- vs.



### Mining çiftlikleri



İzole bir makine madencilik yapabilir, ancak yüzlerce, daha sonra binlerce ASIC'ü tek bir yerde gruplayarak sabit maliyetleri paylaşıyor, lojistiği optimize ediyor ve özel bir veri merkezi modeline yaklaşıyoruz.



En basit haliyle bir mining çiftliği, 7/24 çalışan ASIC'lerle dolu bir binadır (veya konteynerler kümesidir). Şimdi karşılaşılan zorluk, istikrarlı çalışma koşullarını sürdürmektir:




- büyük miktarlarda düşük maliyetli, istikrarlı elektrik gücü sağlar;
- enerji yoğunluğu önemli olduğundan, kısılmayı önlemek için ısıyı yönetin;
- tozu filtreleyin, nemi kontrol edin, temizleyin;
- makine performansının gerçek zamanlı izlenmesi (sıcaklıklar, donanım hataları, hashrate düşüşleri, vb.)



![Image](assets/fr/043.webp)



*Riot Platforms'un Austin, Teksas yakınlarındaki Rockdale tesisinde Bitcoin mining'e adanmış yedi binadan biri. Bu bina özellikle daldırma mining'e adanmıştır*



Mining şu anda, bazıları borsada işlem gören ve çok büyük ölçekli çiftlikler kurup işleten endüstriyel oyuncular tarafından yönlendirilmektedir. Bunlar arasında MARA Holdings (Nasdaq: `MARA`) ve Riot Platforms (Nasdaq: `RIOT`) bulunmaktadır.



![Image](assets/fr/042.webp)



Kârlılık modellerinin ayrıntılarına girmeden bile, mining'in neden bu şekli aldığını anlamak önemlidir. Proof-of-work rekabetçi bir mekanizmadır: bir blok bulma ve dolayısıyla para kazanma olasılığı, dağıttığınız hashrate'un payı ile orantılıdır. Sonuç olarak, hesaplama gücünü artırmak, hesaplama birimi başına maliyeti düşürmek ve kayıpları sınırlamak için sürekli bir baskı vardır. Sonuç olarak, daha ucuz elektrik, soğutmaya elverişli bir iklim veya bol miktarda enerji altyapısı sunan ortamlar doğal olarak daha cazip hale gelmektedir.



Mining Bitcoin böylece ilk günlerinde herkesin erişebildiği bir faaliyetten, özel ekipman ve profesyonel operasyonların hakim olduğu bir faaliyete dönüşmüştür. Bu durum protokolün kurallarını değiştirmemektedir. Teoride herkes herhangi bir makineyle madencilik yapabilir. Ancak pratikte, ASIC'in zorluk ve verimlilik seviyesi, yerel mining'ü çoğu bağlamda büyük ölçüde rekabetsiz hale getirmiştir.



Elbette, örneğin çok ucuz elektrikten faydalanıyorsanız veya kışın evinizi ısıtmak için madencinizin generated ısısını kullanıyorsanız, ev mining'in hala ilgi çekici olabileceği durumlar vardır. Ancak her durumda, yine de bir ASIC çipi ile donatılmış bir makine satın almanız gerekecektir. Dahası, mining gücünüz Bitcoin ağına göre son derece küçük kalacağından, gelirinizin varyansını azaltmanın bir yolunu bulmanız gerekecektir: bir sonraki bölümde tartışacağımız mining havuzlarının rolü tam olarak budur.



Isı geri kazanımlı ev mining çözümlerini keşfetmek isterseniz, hem kullanıma hazır hem de kendin yap çeşitli araçlar hakkında eğitimlerimiz var:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## mining havuzlarına gruplama


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin, başta makine güç tüketimi olmak üzere sürekli ve kaçınılmaz maliyetler içermektedir. Bu masraflar, mining'ten elde edilen gelirler doğası gereği nadir ve rastgele olsa da, herhangi bir sonuçtan bağımsız olarak gerçekleşir. Bir bloğun keşfi yalnızca madencinin hashrate'deki payına bağlıdır ve bu pay ne kadar küçükse kazançlar o kadar öngörülemez hale gelir. İşte tam da bu pratik sorun, mining havuzlarının hızla yaygınlaşmasına yol açmıştır. MIN 101 dersinin bu son bölümünde, mining'teki Bitcoin havuzlarının ilkelerine ve işleyişine bir giriş sunuyorum.



### mining havuzu nedir?



Bir mining havuzu, gruplarının blok bulma sıklığını artırmak için birçok bağımsız madencinin hesaplama gücünü bir araya getiren bir organizasyondur (genellikle çevrimiçi bir hizmettir). Havuz bir blok bulduğunda, blok ödülü daha sonra dahili havuz kurallarına göre katılımcılar arasında yeniden dağıtılır (MIN 101 için çok karmaşık oldukları için MIN 201 kursunda ele alınacaktır).



Bir mining havuzundaki katılımcılar artık tüm mining işlerini yapmadıkları, sadece havuz tarafından kendilerine iletilen verileri hash ettikleri için genellikle "madenci" yerine "hasher" olarak adlandırılırlar.



mining havuzu ile mining grubunu karıştırmamaya dikkat edin. Bunlar iki farklı kavramdır. Önceki bölümde gördüğümüz gibi, bir çiftlik, tek bir kuruluşun çok sayıda mining makinesini çalıştırdığı fiziksel bir sitedir. Öte yandan bir havuz her şeyden önce sanal bir gruplandırmadır: genellikle coğrafi olarak dağınık binlerce makine ortak bir koordinasyon altında çalışır. Bununla birlikte, bir çiftlik bir havuza katılabilir ve genellikle katılır.



![Image](assets/fr/048.webp)



### Gelir farklılığının azaltılması



Peki neden bir havuza katılalım? Basitçe, mining faaliyetinin sonucu olasılıksal olduğu için: her hash denemesinde, zorluk hedefini karşılaması ve dolayısıyla geçerli bir blok üretmesi için çok küçük bir şans vardır.



Çok uzun vadede, ortalama kazancınız toplam hashrate'deki payınızla orantılı olmalıdır. Bu ilke doğrudan olasılık yasalarından kaynaklanır: her hash hesaplaması bağımsız bir rastgele çekiliş oluşturur ve büyük sayılar yasası gereği, blokları keşfetme sıklığınız matematiksel olarak ağın toplam hashrate'indeki payınıza doğru yakınsar. Ancak kısa ve orta vadede, gerçek kazancınız son derece düzensiz olabilir. Teorik ortalama ile rastgele gerçeklik arasındaki bu uyumsuzluğa matematikte **varyans** diyoruz.



Prensibi açıklamak için basit bir örnek verelim:




- Bitcoin ağı günde ortalama 144 blok üretmektedir (yaklaşık her 10 dakikada bir blok);
- Toplam hashrate'ün `%0,0001'ine sahipseniz, beklentiniz `144 × 0,000001` veya `0,000144` blok/gündür;
- Başka bir deyişle, ortalama olarak her `1 / 0.000144` günde, yani her 6,944 günde veya yaklaşık 19 yılda bir blok bulmalısınız.



Ancak bu değer yalnızca matematiksel bir beklentiye karşılık gelir: keşif sürelerinin dağılımı rastgele bir yasayı takip eder, bu nedenle pratikte çok uzun bir süre boyunca bile tek bir blok keşfetmemek tamamen mümkündür. Şanssız olabilir ve yinelenen maliyetler (elektrik, bakım, ekipman amortismanı...) öderken çok uzun süre hiçbir şey bulamayabilirsiniz.



mining havuzu bu sorunun doğasını değiştirir: hashrate'leri birleştirerek havuz blokları daha sık bulur. Her katılımcı daha sonra bulunan her bloğun yalnızca bir kısmını, ancak çok daha sık almayı kabul eder. Bu, ödülleri paylaşmak ve hizmet ücreti ödemek pahasına, oldukça değişken, geniş aralıklı bir gelirden daha düzenli bir gelire dönüşümdür.



### Birlikte grupladığınızda varyans neden düşüyor?



Hesaplama gücünüz ne kadar yüksekse, beklenen blok bulma sıklığınız da o kadar yüksek olur. Daha da önemlisi, olaylar ne kadar sık olursa, gözlemlenen sonuçlar belirli bir dönemdeki istatistiksel ortalamaya o kadar yakın olur.



Tek başına çalışan küçük ölçekli bir madenci yıllarca tek bir blok bile bulamayabilir, sonra bir gün büyük bir ödeme alabilir, ardından hiçbir şey alamayabilir. Bir havuzda, aynı olasılıksal gerçeklik hala geçerlidir, ancak kolektif ölçekte yumuşatılmıştır: havuz daha sık blok bulur ve yeniden dağıtım bu olayları her katılımcı için daha düzenli ödemelere dönüştürür. **mining havuzu bu nedenle mining aktivitesinde öngörülebilirlik satar**.



### Tarihi yerler



Önceki bölümde gördüğümüz gibi, başlangıçta mining, zorluğu çok düşük olduğu için geleneksel bir bilgisayarla tek başına yapılabiliyordu. Ancak küresel hashrate patladıkça (GPU, ardından ASIC), solo mining çoğu katılımcı için çok zaman alan bir kumar haline geldi.



İlk havuzlar tam da bu yeni gerçekliğe yanıt olarak oluşturuldu. Braiins Pool (eski adıyla Slush Pool / Bitcoin.cz) ilk Bitcoin mining havuzudur: ilk bloğunu 16 Aralık 2010 tarihinde çıkarmıştır. Bu ilk mining havuzunun başarısı hızlı oldu, çünkü sadece birkaç gün içinde küresel hashrate'in yaklaşık %3,5'ini ele geçirdi.



![Image](assets/fr/047.webp)



Teknik açıdan, havuzlar daha sonra dağıtılmış işi verimli bir şekilde düzenlemek için havuz ve madenciler arasındaki özel iletişim protokolleri (örneğin Stratum, ardından Stratum V2) etrafında yapılandırıldı. MIN 201 eğitim kursumuzda bu kavramlara daha yakından bakacağız.



### Modern durum



Bu yazının yazıldığı sırada (2026'nın başları), küresel Bitcoin hashrate saniyede zetta-hash (= 1.000 EH/s = saniyede 1.000.000.000.000.000 hashes) büyüklüğündedir ve bulunan blokların neredeyse tamamı mining havuzlarından gelmektedir.



Burada bugüne kadar ana mining havuzlarının ve bunların hashrate'deki paylarının bir sıralaması yer almaktadır. Bu sıralama, siz bu dersi okurken muhtemelen değişecektir. Güncel veriler için lütfen [mempool.space](https://mempool.space/graphs/mining/pools) adresini ziyaret edin.



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Kaynak [mempool.space](https://mempool.space/graphs/mining/pools), bir aylık veriler, 16 Aralık 2025 - 16 Ocak 2025.*



Daha ileri düzey bir kursta, havuzların iç işleyişine (paylaşımlar, ağ protokolleri, ödeme yöntemleri...) daha fazla gireceğiz, çünkü hem madencinin karlılığını hem de Bitcoin için potansiyel etkileri belirleyen ayrıntılar burada devreye giriyor.



---

MIN 101'in sonuna gelmiş bulunuyoruz. Sonuna kadar takip ettiğiniz için teşekkür ederiz. Kurs boyunca edindiğiniz becerileri değerlendirmek isterseniz, bir sonraki bölümde sizi bir final sınavı bekliyor.



Yeni edindiğiniz temel bilgilerle, artık mining'te Plan ₿ Academy'deki gibi teorik veya daha pratik kurslar gibi daha gelişmiş kurslar alabilir, böylece siz de Bitcoin mining'e katılmaya başlayabilirsiniz!



# Son bölüm


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Yorumlar & Derecelendirmeler


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Final Sınavı


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Sonuç


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>