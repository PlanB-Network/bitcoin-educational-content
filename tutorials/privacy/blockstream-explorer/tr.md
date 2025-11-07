---
name: Blockstream Explorer
description: Bitcoin ve Liquid Network'ın ana katmanını keşfedin
---

![cover](assets/cover.webp)



Blockstream Explorer, Blockstream şirketi tarafından geliştirilen [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid'ün yanı sıra işlemlerin ve Bitcoin protokolünün küresel durumunun keşfedilmesini kolaylaştıran bir projedir.



2014 yılında Adam Back tarafından kurulan Blockstream şirketi tarafından başlatılan [blockstream.info](https://blockstream.info) explorer, Bitcoin için sağlam bir altyapı sağlamayı, katmanlar (on-chain ve Liquid) arasında birlikte çalışabilirliği ve işlem takibini garanti ederken, kullanıcı güvenliğini ve gizliliğini artırmayı amaçlamaktadır.



Bu eğitimde, onu diğerlerinden ayıran özellikleri, hizmetleri ve Bitcoin'in on-chain ve Liquid katmanlarının operasyonlarını ve durumlarını nasıl sorunsuz bir şekilde izlediğini inceleyeceğiz.



## Blockstream explorer ile çalışmaya başlama



### Ana kanalda gezinme



Blockstream.info gezginine gittiğinizde, "**Dashboard**" üzerinde, Bitcoin protokolü ana zinciri varsayılan olarak seçilir. Bu arayüzden, :





- Ana zincir boyutu: Yakın zamanda çıkarılmış bloklar.



![blocks](assets/fr/01.webp)



Bu bölümde son çıkarılan bloklar, zaman damgası, her blokta yer alan işlem sayısı, kilobayt (kB) cinsinden boyut ve her bloğun ağırlık birimi cinsinden ölçümü (**WU** = *Weight Units*) hakkında bilgi verilmektedir. Bu son ölçüm, ana zincirin her bir bloğunun `4.000.000 WU` veya `4.000 kWU` ile sınırlı olduğu göz önüne alındığında, bloğun optimizasyonunu değerlendirmemizi sağladığı için ilgi çekicidir.





- Son işlemler.



![transactions](assets/fr/02.webp)



İşlem bölümü, işlemin benzersiz tanımlayıcısı, ilgili bitcoin değeri, sanal bayt (vB) cinsinden boyutu - tüm verilerin (girdi ve çıktı) toplamını temsil eder - ve ilgili ücret oranı hakkında bilgi sağlar. Örneğin, `2 sat/vB` oranında `153 vB` büyüklüğünde bir işlem `306 satoshis` ücretine tabi olacaktır.



### Akışkan keşfi



"**Bloklar**" menüsünden, tüm ana zincirin geçmişini son çıkarılan bloğa kadar izleyebilirsiniz.



![blocs](assets/fr/03.webp)



Belirli bir bloğa tıklayarak, içerdiği bilgiler ve işlemler hakkında daha fazla ayrıntı elde edebilirsiniz. Örneğin, 919330 numaralı blok için: bloğun hash'ini göreceksiniz. Ayrıca, kazılan her blok (Genesis hariç) bir öncekine bağlı olduğundan ve bir öncekinin hash'ini koruduğundan, bir önceki bloğa da gidebilirsiniz.



![metadata](assets/fr/04.webp)



"Ayrıntılar "** düğmesine tıklayarak, bu blok hakkında, tutulan ve yayılan ana zincire eklendiğini doğrulayan durumu gibi daha fazla bilgi edinebilirsiniz. Ayrıca bu bloğun çıkarıldığı zorluk derecesine de sahipsiniz: bu zorluk derecesi mining'nin kriptografik problemini çözmek için gereken hesaplama gücünü temsil eder ve her 2016 blokta bir (yaklaşık 2 hafta) ayarlanır.



![details](assets/fr/05.webp)



Bu ayrıntılar bölümünün altında, bu bloğa dahil olan tüm işlemleri buluyoruz.



Bloktaki ilk işleme **transaction coinbase** adı verilir. Madencinin mining ödülünü (blokta yer alan işlemlerle ilişkili tüm ücretler ve blok hibesi) tahsis etmek için kullanılır. Bu işlemle yaratılan bitcoinler ancak 100 ardışık blok daha kazıldıktan sonra harcanabilir. Başka bir deyişle, madencinin bunları kullanabilmesi için **919430** bloğunun üretilmesini beklemesi gerekecektir. Bu, [*"vade süresi "*] (https://planb.academy/fr/resources/glossary/maturity-period) olarak bilinir.



Coinbase özel bir işlemdir: önceki bir işlemden herhangi bir bitcoin harcamadığı için gerçek girdisi olmayan tek işlemdir.




![coinbase](assets/fr/06.webp)



Diğer tüm işlemler iki bölüme ayrılır: girdiler ve çıktılar.



Bitcoinlerin yeni bir işlemde girdi olarak kullanılabilmesi için, işlemi başlatan kişinin belirli bir senaryoya karşılık gelen bir imza sağlayarak sahipliğini kanıtlaması gerekir. Her bir bitcoin parçası (UTXO), genellikle yalnızca sahibinin özel anahtarının sağlayabileceği belirli bir imza gerektiren bir komut dosyası içerir. Bu komut dosyaları ***scriptSig*** (ASM'de) olup Bitcoin Komut Dosyasında yazılmıştır ve çeşitli türlerde olabilir. Bu örnekte, kullanılan UTXO'ların P2WPKH (*Pay-to-Witness-Public-Key-Hash*) türündeki bir çıktıya P2SH türünde olduğunu görebiliriz.



Belirli bir UTXO'nin geçmişini sezgisel yöntemler kullanarak izleyebilirsiniz. Sizi farklı Bitcoin sezgisel yöntemlerini ve Bitcoin'daki işlemlerinizin gizliliğini güçlendirmenin yollarını keşfetmeye davet ediyoruz:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Bu işlemin giden masrafı örneğini ele alalım. İşlem tanımlayıcısına tıkladığımızda, işlem ayrıntıları sayfasındaki **İşlemler** bölümüne yönlendiriliriz.



![transaction](assets/fr/08.webp)



Bu sayfadan işlemin hangi bloğa dahil olduğunu öğrenebilirsiniz. Kullanılan adres türüne bağlı olarak, işlem verilerini (*sanal baytlar*) optimize edebilir ve bu nedenle daha az işlem ücreti ödeyebilir. Örneğin bu işlem, `bc1q` ile başlayan yerel bir SegWit Bech32 adres formatı kullanarak ücretlerde %53 tasarruf sağlamıştır.



![trx_details](assets/fr/09.webp)



## Liquid katmanı



Liquid Network bir [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) ve Bitcoin protokolü için açık kaynaklı bir seviye 2 çözümüdür. Özellikle, daha hızlı ve daha gizli bitcoin işlemlerine olanak sağlar.



Blockstream.info gezgininde, Liquid ağına geçmek için **"Liquid"** düğmesine tıklayın.



![liquid](assets/fr/10.webp)



İzlemek istediğimiz işlemlerden birine tıkladığımızda, bitcoin yığın tutarlarının "**Gizli**" sözcükleriyle değiştirildiğini görüyoruz. Bu ağda, işlemler gizli olabilir, bu nedenle işlemin içindeki veya dışındaki her bir UTXO miktarını göremeyiz.



![liquid_trx](assets/fr/11.webp)



Bununla birlikte, Bitcoin protokolünün ana katmanında bulunan ilke ve mekanizmaların aynı olduğunu belirtmek isteriz: bitcoin kilitleme komut dosyaları ve UTXO izlenebilirliği.



![liquid_details](assets/fr/12.webp)



Liquid Network ayrıca kuruluşlar tarafından kullanılabilecek depo dışı dijital varlıklar da sağlar. "Varlıklar "** menüsünde, kayıtlı varlıkların bir listesini, toplamlarını ve ilgili oldukları etki alanını bulacaksınız.



![assets](assets/fr/13.webp)



Her varlık için, ihraç ve yakma işlemlerinin geçmişini izleyebilirsiniz (dolaşımdaki toplamı silerek).



![assets_trxs](assets/fr/14.webp)




## Daha fazla seçenek



Blockstream.info gezgini ayrıca Testnet, Bitcoin, on-chain ve Liquid Network üzerindeki işlemlerin görselleştirilmesini ve izlenmesini de içerir.



![testnet](assets/fr/15.webp)



Testnet ağına gittiğinizde, gerçek bitcoin kullanmazsınız, ancak yukarıda açıklanan tüm özelliklere sahip olursunuz.



![liquid_testnet](assets/fr/16.webp)



Bu ağ, Bitcoin ve Liquid mekanizmalarının çalışmasını bağlayıp test edebileceğiniz farklı bir zincir uzunluğuna sahiptir.





- API bölümü, belirli Explorer işlevlerini kendi uygulamalarına entegre etmek isteyen herkese adanmıştır. Bu API aracılığıyla farklı katmanların (on-chain ve Liquid) ana zincirini sorgulayabilir, işlemleri takip edebilir ve örneğin bir bloktaki işlemler için ortalama ücretleri öğrenebilirsiniz.



![api](assets/fr/17.webp)



Artık Blockstream Explorer'ın on-chain ve Liquid katmanlarındaki blok zincirlerini sorgulama potansiyelinden tam olarak yararlanmaya hazırsınız. Bu öğreticiyi bilgilendirici bulduğunuzu umuyor ve başka bir Bitcoin gezgini hakkındaki öğreticimizi öneriyoruz:



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f