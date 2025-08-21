---
name: Mempool
description: Tüm Bitcoin ekosistemini keşfedin.
---

![cover](assets/cover.webp)



Bitcoin protokolü, danışmaya açık, takma isimli, merkezi olmayan bir ağdır. Üyeler (düğümler), yani Bitcoin yazılımının bir örneğine sahip bilgisayarlar, Bitcoin'de yayınlanan tüm verilere sınırsız erişime sahiptir. Bununla birlikte, Bitcoin'nin ilk yıllarında, protokol bugün olduğu kadar geniş çapta erişilebilir değildi.


Bitcoin'ün ilk günlerinde, komut satırlarından ağı sorgulamak için uygun araçlara (bitcoin-cli) erişmek amacıyla bir Bitcoin düğümü çalıştırmak gerekiyordu.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Bu nedenle, Bitcoin topluluğunu genişletmek ve bir node'a sahip olmayan ve/veya gerekli teknik becerilere sahip olmayan herkes için daha erişilebilir hale getirmek için projeler başlatıldı.



Bu eğitimde **Mempool.space** projesine, özelliklerine ve Bitcoin ekosistemi üzerindeki etkisine bakacağız.



## Mempool.space nedir?



**Mempool.space**, çeşitli Bitcoin protokol ağlarındaki işlemler, işlem ücretleri, bloklar ve madenciler hakkında yararlı bilgiler sağlayan açık kaynaklı bir gezgindir. 2020 yılında kullanıma sunulan bu tarayıcı, temsili grafikler, akıcı animasyonlar ve düzenli arayüzler sayesinde kullanıcı deneyiminde önemli bir iyileşme sağlamaktadır.



Projeyi anlamak için, bir Mempool (bellek havuzu), Bitcoin ağında onay bekleyen tüm işlemlerin depolandığı sanal bir alandır. Mempool, Bitcoin işlemlerinin onaylanmayı beklediği bir "bekleme odası" gibidir. Ağdaki her bilgisayarın (düğüm) kendi bekleme odası vardır, bu da neden tüm işlemlerin aynı anda herkes tarafından görülemediğini açıklar.



Platformun Bitcoin ekosistemindeki ana etkisi, Bitcoin'te bulunan düğümlerin çoğunun bellek alanlarındaki çeşitli bilgilere bir tane çalıştırmanıza gerek kalmadan erişmenize izin vermesidir. Mempool.space, Bitcoin protokol ağlarını görüntülemek ve aramak için bir depodur.



Ekosistemde giderek yaygınlaşan kullanım ve Mempool.space'in açık kaynak olması, giderek daha fazla kişisel barındırma sistemine entegre edilmesini sağladı. Artık doğrudan kişisel düğümünüzde kendi Mempool.space örneğinize sahip olabilirsiniz. Umbrel node'unuzda Mempool.space'i yapılandırmaya ilişkin öğreticimizi aşağıda bulabilirsiniz.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Mempool.space'in temelleri



Yukarıda belirtildiği gibi, [Mempool.space] (https://Mempool.space), işlemlerinizi ve bunların seçilen Bitcoin ağındaki yayılımını grafiksel bir Interface'den gerçek zamanlı olarak izlemenizi sağlayan bir Bitcoin protokol gezginidir.



Mempool.space birçok Bitcoin protokol ağını destekler.


Menü çubuğunda aşağıdaki ağları bulacaksınız:




- Mainnet** : Gerçek Bitcoin işlemlerinin gerçekleştiği ana Bitcoin ağı.
- Signet**: Ana ağın gerektirdiği kaynakları gerektirmeden blokları doğrulamak için dijital imzaları kullanan bir test ağı.
- Testnet 3**: Bitcoin protokolü üzerinde risksiz bir test ve geliştirme ağı.
- Testnet 4** : Testnet 3'ün yeni sürümü, test ortamına daha fazla kararlılık ve yeni mutabakat kuralları getiriyor.



![reseaux](assets/fr/01.webp)



Ana sayfada, solda Green'de, onaylanmaya ve Bitcoin ağına entegre edilmeye (kazılmaya) hazır gelecekteki olası blokları (işlem grupları) göreceksiniz. Ortalama olarak, her on dakikada bir blok çıkarılır: bu bilgiyi saklayın, çünkü daha sonra geliştirmemizde kullanışlı olacaktır.


Morumsu renkte, sağ tarafta, Bitcoin'da çıkarılan son blokları bulacaksınız; çıkarılan son bloğun numarası ağın mevcut yüksekliğini temsil eder.



![blocs](assets/fr/02.webp)



İşlem Ücretleri** bölümü bir işlem ücreti tahmin edicisidir. İşleminize tahsis edilen ücretler ne kadar yüksekse, işleminizin çıkarılmaya hazır bir sonraki bloğa eklenme olasılığı o kadar yüksektir.


İşlem ücretleri, bir Miner'nin işleminizi Mining için aday bir bloğa eklemek için sizden alacağı maliyeti temsil eder. İşleminizin aday blokta kaplayacağı alan için ödediğiniz satoshis sayısını temsil eden sat/vB (Satoshi/Sanal Bayt) oranı ile tanımlanır.



⚠️ ÖNEMLİ: Mempool doygunluğu durumunda, madenciler en iyi Satoshi/vByte oranını sunan işlemlere öncelik verirler. İşleminiz ne kadar ağır (büyük) olursa, hızlı bir şekilde dahil edilmesi için o kadar fazla satoshiye ihtiyaç duyacaktır.



![fees-visualizer](assets/fr/03.webp)



**Mempool Goggles** bölümü, bir işlemin kapladığı alanı görselleştirmenizi sağlar.



![mempool](assets/fr/04.webp)



Madencilerin aday bloklarını kazılmış bloklar zincirine eklemek için sağlamaları gereken Proof of Work'nın zorluğu nedeniyle yaklaşık her on dakikada bir blok kazılır. Bu zorluk her **2016 blokta** değişir, bu da yaklaşık **2 haftaya** denk gelir. Bu zorluğun gelişimini burada görebilirsiniz.



![difficulty](assets/fr/05.webp)



Ana zincire yeni bir bloğun eklenmesi, onaylanan bloğun Miner'sine sabit bir kısım (her 210.000 blokta bir** yarıya indirilir, yarıya indirmeler sırasında yaklaşık 4 yıla** eşdeğerdir) ve işlem ücretlerinden oluşan bir ödül hakkı verir.



![halving](assets/fr/06.webp)



## İşlem ayrıntılarınıza erişin



Mempool.space arama çubuğuna, geçmişiniz hakkında daha fazla bilgi edinmek için Bitcoin Address veya transaction ID'inizi girebilirsiniz.



![search](assets/fr/07.webp)



İşlem ayrıntıları sayfasında, işleminizle ilgili genel bilgileri bulacaksınız:




- Durum**: Bir bloğa eklendiğinde onaylandı, bir Mempool'de beklerken onaylanmadı.
- İşlem ücretleri**.
- Tahmini varış süresi (ETA)** :  İşleminizin bir bloğa eklenmesi için geçecek yaklaşık süre. Bu işlemle ilişkili ücretleri oluşturan orana göre hesaplanır.



![general-txinfo](assets/fr/08.webp)



Akış** bölümü, işlem bileşenlerinizin bir grafiğini gösterir.



İşleminiz için kullanılan girdiler (önceki UTXO) ve alıcılara, harcamaları için gerekli imzayı sunarak her çıktıdan bitcoinleri kullanma hakkı veren çıktılar.



![flow](assets/fr/09.webp)



Kullanılan adresler hakkında daha fazla ayrıntı **Girişler ve Çıkışlar** bölümünde bulunabilir.



![address](assets/fr/10.webp)



Gizliliğinizi artırmak için farklı Bitcoin işlem şemalarını keşfedin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## İşlemlerinizi hızlandırın



Bitcoin ekosisteminde, işlemlerin madenciler tarafından doğrulanması, söz konusu işlemle ilişkili işlem ücretleriyle içsel olarak bağlantılıdır. Madenciler, daha yüksek ücret oranına (satoshis/vByte) sahip işlemlere öncelik verir; bu da madenciler tarafından kabul edilen makul ücretleri ödemezseniz işleminizin geçerliliğini etkileyebilir. İşleminiz, ücret oranını kabul eden bir bloğu beklerken Mempool'da takılıp kalabilir.



Neyse ki, işleminizin onaylanmasını hızlandırmak için Bitcoin ağında iki yöntem mevcuttur.





- RBF** - Ücrete Göre Değiştirme: Düşük ücretli işleminizle aynı girişleri harcamanıza izin veren bir yöntem, ancak bu sefer doğrulamayı hızlandırmak için işlem ücretini artırarak. Yeni işleminiz daha hızlı bir şekilde onaylanacak ve düşük ücretli işlemi geçersiz kılarak bir bloğa dahil edilecektir.



Bu mekanizmayı kabul eden cüzdanlarla bir ücret değiştirme işlemi gerçekleştirebilirsiniz. Örneğin, Blue Wallet Wallet hakkındaki makalemize bakın.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- CPFP** - Child pay for parent: RBF'ten esinlenen bir yaklaşım, ancak alıcı tarafında. Alıcısı olduğunuz işlem bir Mempool'de bloke edildiğinde, henüz onaylanmamış olmasına rağmen, bu yeni işleme daha fazla ücret tahsis ederek bu işlemin çıktılarını (UTXO'ları) harcama seçeneğiniz vardır, böylece ortalama ücretler - alıcısı olduğunuz işlemin ve başlatılan işlemin - madencileri her iki işlemi de bir bloğa dahil etmeye teşvik eder.



⚠️ İkinci işlemin onaylanabilmesi için ilk işlemin bir bloğa dahil edilmesi gerekir.



Tüm bu terimler biraz fazla teknik görünüyorsa, Bitcoin ve ekosistemiyle ilgili tüm teknik terimlerin tanımlarını içeren [sözlüğümüze] (https://planb.network/resources/glossary) başvurmanızı tavsiye ederim.



Bu yöntemlere ek olarak, Mempool.space, Bitcoin ağında bulunan madencilerin %80'inden fazlasıyla olan bağlantıları sayesinde, RBF'i etkinleştirmeyenler de dahil olmak üzere **onaylanmamış** işlemlerinizden herhangi birini, düşük maliyetli işleminizi çıkarılmaya hazır bir sonraki bloğa eklemek için Exchange'teki madencilere bir bedel ödeyerek hızlandırmanıza olanak tanır.



İşlem ayrıntıları sayfasında, **Hızlandır** düğmesine tıklayın, ardından karşı tarafınıza madencilere ödeme yapmaya devam edin.



![accelerate-section](assets/fr/11.webp)


## Küçükler



Bir Miner, bir madeni yöneten bir kişiyi, yani Proof-of-Work'a katılmaktan oluşan Mining sürecine dahil olan bir bilgisayarı ifade eder. Miner, Mempool'deki bekleyen işlemleri bir aday blok oluşturmak üzere gruplandırır. Daha sonra çeşitli nonce'ları değiştirerek bu bloğun başlığı için hedeften küçük veya hedefe eşit geçerli bir Hash arar. Geçerli bir Hash bulursa, bloğunu Bitcoin ağına yayınlar ve blok sübvansiyonu (yeni bitcoinlerin ex-nihilo yaratılması) ve işlem ücretinden oluşan ilgili maddi ödülü cebe indirir.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

madenciler, işlemleri doğrulayan ve bloklar halinde gruplandıran "doğrulayıcılar" gibidir. Bitcoin ağına yeni bir blok eklemek için karmaşık bir matematiksel bulmacayı (Proof-of-Work) çözmeleri gerekir. Bulmacayı çözen ilk Miner, bir Bitcoin ödülü kazanır (blok hibesi + bloğa dahil edilen işlemler için ücretler).



Bu Proof of Work'in zorluğu izlenir ve madenciler için gereken bilgi işlem gücünün gelişimini görselleştirmenize olanak tanır. Aşağıdaki bölümlerde bulacaksınız :





- Son zorluk ayarlaması sırasında madenciler tarafından elde edilen toplam ödüllerin bir tahmini ve her 210.000 blokta bir (yaklaşık 04 yıl) meydana gelen blok hibesinin bir sonraki Halving tahminleri.



![rewards](assets/fr/12.webp)



Bu zorluk her 2016 blokta bir (yaklaşık iki hafta) ayarlanır. Her 2016 blokta madencilerin Miner için harcadıkları ortalama süre ile ters orantılıdır.


Madenciler tarafından harcanan ortalama süre 10 dakikadan az olduğunda, zorluk artmakta ve bu da madencilerin Miner bloklarını doğrulamasının daha kolay olduğunu kanıtlamaktadır. Tersine, ortalama süre 10 dakikadan fazla olduğunda, zorluk azalır.



![mining-pool](assets/fr/13.webp)





- Madenci grupları: İlgili zorluk göz önüne alındığında, bir grup madenci Proof of Work'yi Bitcoin'te bulmaya yardımcı olmak için **pool** olarak adlandırdığımız bir grupta işbirliği yapar. Grup tarafından bir blok çıkarıldığında, elde edilen ödül, her bir Miner'in kısmi çözüm aramasındaki başarı yüzdesine göre, yani Proof-of-Work'ün aranmasında hesaplama gücündeki katkıya göre veya işbirliği tarafından kararlaştırılan ücretlendirme yöntemine göre dağıtılır.





![mining](assets/fr/14.webp)



## Lightning Network altyapısı



Mempool sadece Bitcoin'nin ağ altyapısı (ana zincir) hakkında bilgi sağlamakla kalmaz. Aynı zamanda Bitcoin'nin Lightning katmanı için görselleştirme ve keşif araçlarını da entegre eder.



Lightning** bölümünde, Lightning düğümleri arasındaki mevcut tüm bağlantıları görüntüleyebilirsiniz.



![network-stats](assets/fr/15.webp)



Bu Interface aşağıdakiler hakkında bilgi sağlar:





- Lightning Network istatistikleri.



![distribution](assets/fr/16.webp)




⚠️ **ÖNEMLI**: Bir ödeme kanalının kapasitesi, bir düğümün bir Lightning işlemi sırasında başka bir düğüme gönderebileceği maksimum miktarı belirler.





- Yıldırım düğümleri İnternet servis sağlayıcısına (barındırma hizmeti) ve isteğe bağlı olarak ödeme kanalı kapasitesine göre tahsis edilir.



![distribution](assets/fr/17.webp)





- Lightning Network'in toplam kapasitesinin geçmişi.


Ayrıca bu düğümlerin ödeme kanallarının kapasitesine göre bir sıralamasını da bulacaksınız.



![ranking](assets/fr/18.webp)



## Daha fazla grafik



Mempool.space, Bitcoin protokol ağlarıyla etkileşimin keyfini çıkarmak için ideal bir platformdur. Grafikler yalnızca ne zaman işlem yapacağınıza karar vermenize yardımcı olacak görsel veriler sağlamakla kalmaz, aynı zamanda Bitcoin ağının ve ilgili Yıldırım altyapılarının gücünü ve sağlığını gerçek zamanlı olarak görselleştirmenize olanak tanıyan hassas parametreler de sağlar.



Grafikler** bölümünde, Bitcoin ağı hakkındaki temel verileri görüntüleyebilirsiniz:




- Mempool boyut gelişimi: Mempool'in boyutunun nasıl dalgalandığını gözlemleyebilirsiniz, bu da ağdaki yüksek veya düşük etkinlik dönemlerini gösterebilir.



![graphs](assets/fr/19.webp)






- Seçilen ağdaki işlemlerin ve işlem ücretlerinin gelişimi: Saniye başına işlemlerdeki değişimleri takip ederek, tıkanıklık veya düşük aktivite dönemlerini öngörebilir ve işlem ücretlerinizi optimize edebilirsiniz. Bu grafik size ağın işlem hacmini idare etme kapasitesi hakkında bir perspektif sunar.



![graphs](assets/fr/20.webp)



Artık Mempool.space'deki yolculuğunuzun sonuna geldiğinize göre, kendi kaşifiniz olun ve işlemlerinizi gerçek zamanlı olarak takip edin. Lütfen Bitcoin **Public Pool** kaşifi hakkındaki makalemizi aşağıda bulabilirsiniz.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1