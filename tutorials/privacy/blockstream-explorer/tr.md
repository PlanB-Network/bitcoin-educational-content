---
name: BLOCKSTREAM Explorer
description: Bitcoin ve Liquid Network'in ana Layer'ünü keşfedin
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer, işlemlerin ve Bitcoin protokolünün Global State'ünün yanı sıra BLOCKSTREAM şirketi tarafından geliştirilen [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid'in keşfedilmesini kolaylaştıran bir projedir.



Adam Back tarafından kurulan bir şirket olan BLOCKSTREAM tarafından 2014 yılında başlatılan [BLOCKSTREAM.info](https://BLOCKSTREAM.info) explorer, Bitcoin için sağlam bir altyapı sağlamayı, katmanlar (On-Chain ve Liquid) arasında birlikte çalışabilirliği ve işlem takibini garanti ederken, kullanıcı güvenliğini ve gizliliğini artırmayı amaçlamaktadır.



Bu eğitimde, Bitcoin'ü farklı kılan özellikleri, hizmetleri ve Bitcoin'ün On-Chain ve Liquid katmanlarının operasyonlarını ve durumlarını nasıl sorunsuz bir şekilde izleyebildiğini anlatıyoruz.



## BLOCKSTREAM ile çalışmaya başlama



### Ana kanalda gezinme



BLOCKSTREAM.info gezginine gittiğinizde, "**Pano**" üzerinde, ana Bitcoin protokol kanalı varsayılan olarak seçilir. Bu Interface'den, genel bir bakışa sahip olursunuz:





- Ana zincir boyutu: Yakın zamanda çıkarılmış bloklar.



![blocks](assets/fr/01.webp)



Bu bölümde son çıkarılan bloklar, Timestamp, her bir BLOCK'de yer alan işlem sayısı, kilobayt (kB) cinsinden boyut ve her bir BLOCK'in ağırlık birimleri cinsinden ölçümü (**WU** = *Weight Units*) hakkında bilgi verilmektedir. Bu son ölçüm, ana zincirin her bir BLOCK'inin `4.000.000 WU` veya `4.000 kWU` ile sınırlı olduğu göz önüne alındığında, BLOCK'in optimizasyonunu değerlendirmemizi sağladığı için ilgi çekicidir.





- Son işlemler.



![transactions](assets/fr/02.webp)



İşlem bölümü, işlemin benzersiz tanımlayıcısı, ilgili Bitcoin değeri, sanal bayt (vB) cinsinden boyutu - tüm verilerin (giriş ve çıkış) toplamını temsil eder - ve ilgili ücret oranı hakkında bilgi sağlar. Örneğin, `2 sat/vB` oranında `153 vB` boyutunda bir işlem `306 satoshis` ücretine tabi olacaktır.



### Akışkan keşfi



"**Bloklar**" menüsünden, tüm ana zincirin geçmişini son çıkarılan BLOCK'e kadar izleyebilirsiniz.



![blocs](assets/fr/03.webp)



Belirli bir BLOCK'e tıklayarak, içerdiği bilgiler ve işlemler hakkında daha fazla ayrıntı elde edebilirsiniz. Örneğin, BLOCK 919330 için: BLOCK'in Hash'sına sahipsiniz. Ayrıca, çıkarılan her BLOCK (Genesis hariç) bir öncekine bağlı olduğundan ve bir öncekinin Hash'sını koruduğundan, bir önceki BLOCK'e de gidebilirsiniz.



![metadata](assets/fr/04.webp)



"Ayrıntılar "** düğmesine tıklayarak, bu BLOCK hakkında, korunan ve yayılan ana zincire eklendiğini doğrulayan durumu gibi daha fazla bilgi edinebilirsiniz. Ayrıca, bu BLOCK'in çıkarıldığı zorluk derecesine de sahipsiniz: bu zorluk derecesi, Mining'nin kriptografik problemini çözmek için gereken hesaplama gücünü temsil eder ve her 2016 blokta bir (yaklaşık 2 hafta) ayarlanır.



![details](assets/fr/05.webp)



Bu ayrıntılar bölümünün altında, bu BLOCK'da yer alan tüm işlemleri buluyoruz.



BLOCK'deki ilk işlem **işlem coinbase** olarak adlandırılır. Miner'nin Mining ödülünü (BLOCK ve BLOCK hibesinde yer alan işlemlerle ilişkili tüm ücretler) tahsis etmek için kullanılır. Bu işlemle yaratılan bitcoinler ancak 100 ardışık blok daha kazıldıktan sonra harcanabilir. Başka bir deyişle, bunları kullanabilmek için Miner'nin BLOCK **919430** üretimini beklemesi gerekecektir. Bu, [*"vade süresi "*] (https://planb.network/fr/resources/glossary/maturity-period) olarak bilinir.



Coinbase özel bir işlemdir: önceki bir işlemden herhangi bir bitcoin harcamadığı için gerçek girdisi olmayan tek işlemdir.




![coinbase](assets/fr/06.webp)



Diğer tüm işlemler iki bölüme ayrılır: girdiler ve çıktılar.



Bitcoinlerin yeni bir işlemde girdi olarak kullanılabilmesi için, işlemi başlatan kişinin belirli bir senaryoya karşılık gelen bir imza sağlayarak sahipliğini kanıtlaması gerekir. Her bir bitcoin parçası (UTXO), genellikle yalnızca sahibinin özel anahtarının sağlayabileceği belirli bir imza gerektiren bir komut dosyası içerir. Bu komut dosyaları ***scriptSig*** (ASM'de), Bitcoin Komut Dosyasında yazılmıştır ve çeşitli türlerde olabilir. Bu örnekte, kullanılan UTXO'ların P2WPKH (*Pay-to-Witness-Public-Key-Hash*) tipindeki bir çıktıya P2SH tipinde olduğunu görebiliriz.



Belirli bir UTXO'un geçmişini sezgisel yöntemler kullanarak izleyebilirsiniz. Sizi farklı Bitcoin sezgisel yöntemlerini ve Bitcoin işlemlerinizin gizliliğini nasıl güçlendirebileceğinizi keşfetmeye davet ediyoruz:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Bu işlemin giden masrafı örneğini ele alalım. İşlem tanımlayıcısına tıkladığımızda, işlem ayrıntıları sayfasındaki **İşlemler** bölümüne yönlendiriliriz.



![transaction](assets/fr/08.webp)



Bu sayfadan, işlemin hangi BLOCK'e dahil olduğunu öğrenebilirsiniz. Kullanılan Address türüne bağlı olarak, işlem verilerini (*sanal baytlar*) optimize edebilir ve bu nedenle daha az işlem ücreti ödeyebilir. Örneğin bu işlem, `bc1q` ile başlayan yerel bir SegWit BECH32 Address formatı kullanarak ücretlerde %53 tasarruf sağlamıştır.



![trx_details](assets/fr/09.webp)



## Liquid kaplama



Liquid Network bir [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) ve Bitcoin protokolü için seviye 2 açık kaynak çözümüdür. Özellikle, daha hızlı ve daha gizli Bitcoin işlemleri sağlar.



BLOCKSTREAM.info gezgininde, Liquid Network'e geçmek için **"Liquid"** düğmesine tıklayın.



![liquid](assets/fr/10.webp)



Takip etmek istediğimiz işlemlerden birine tıkladığımızda, Bitcoin parçalarının miktarlarının "**Gizli**" kelimeleriyle değiştirildiğini görüyoruz. Bu ağda işlemler gizli olabilir, bu nedenle işlemin içindeki veya dışındaki her bir UTXO'nin miktarını göremeyiz.



![liquid_trx](assets/fr/11.webp)



Bununla birlikte, Bitcoin protokolünün ana Layer'ünde bulunan ilke ve mekanizmaların aynı olduğunu not ediyoruz: Bitcoin kilitleme komut dosyaları ve UTXO izlenebilirliği.



![liquid_details](assets/fr/12.webp)



Liquid Network ayrıca kuruluşlar tarafından kullanılabilecek depo dışı dijital varlıklar da sağlar. "Varlıklar "** menüsünde, kayıtlı varlıkların bir listesini, toplamlarını ve ilgili oldukları etki alanını bulacaksınız.



![assets](assets/fr/13.webp)



Her varlık için, ihraç ve yakma işlemlerinin geçmişini izleyebilirsiniz (dolaşımdaki toplamı silerek).



![assets_trxs](assets/fr/14.webp)




## Daha fazla seçenek



BLOCKSTREAM.info gezgini ayrıca Testnet, Bitcoin, On-Chain ve Liquid Network üzerindeki işlemlerin görselleştirilmesini ve izlenmesini de içerir.



![testnet](assets/fr/15.webp)



Testnet ağına gittiğinizde, gerçek bitcoin kullanmazsınız, ancak yukarıda açıklanan tüm özelliklere sahip olursunuz.



![liquid_testnet](assets/fr/16.webp)



Bu ağ, Bitcoin ve Liquid mekanizmalarının çalışmasını bağlayıp test edebileceğiniz farklı bir zincir uzunluğuna sahiptir.





- API bölümü, belirli Explorer işlevlerini kendi uygulamalarına entegre etmek isteyen herkese adanmıştır. Bu API aracılığıyla farklı katmanların (On-Chain ve Liquid) ana zincirini sorgulayabilir, işlemleri takip edebilir ve örneğin bir BLOCK'deki işlemler için ortalama ücretleri öğrenebilirsiniz.



![api](assets/fr/17.webp)



Artık On-Chain ve Liquid katmanlarındaki blok zincirlerini sorgulamak için BLOCKSTREAM Explorer'ın tüm potansiyelinden yararlanmaya hazırsınız. Bu öğreticiyi bilgilendirici bulduğunuzu umuyor ve başka bir Bitcoin Explorer hakkındaki öğreticimizi öneriyoruz:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f