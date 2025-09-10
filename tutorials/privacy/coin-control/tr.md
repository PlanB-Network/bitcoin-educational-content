---
name: Coin Control
description: Bitcoin'de gizliliğinizi korumak için önemli bir araç olan Coin Control ile tanışın
---
![cover](assets/cover.webp)


*Bu eğitim [Officine Bitcoin dersinden](https://officinebitcoin.it/lezioni/coinco/) aktarılmıştır.*



## Giriş



Bitcoin protokolünün sağlamlığı basit temel kavramlarla garanti altına alınır. Bunların arasında şeffaflık öne çıkar: tüm Bitcoin işlemleri herkese açıktır ve herkes tarafından kolayca doğrulanabilir. Bu özellik dolandırıcılığı önlediği ve fonların gerçekliğini garanti ettiği için protokolün bir dönüm noktası olsa da, gizlilik açısından da bir zorluk teşkil edebilir. **Hiç bu kadar şeffaflığın mahremiyetinizi zedeleyebileceğini düşündünüz mü?**



Yapmalısınız. Satoshi non-kyc biriktirmek oldukça kolay olsa da, gizliliğiniz en çok harcama aşamasında risk altındadır.



### Bir UTXO harcadığınızda ne olur?



Bitcoin'in harcanması sadece değerin bir başkasına aktarılması değildir.



UTXO'larınızdan birini tüketerek, aslında protokol şeffaflığı için getirilen koşulları yerine getirmelisiniz, çünkü bu fonlara sahip olduğunuzu kanıtlama yükümlülüğünüz vardır. Bu nedenle kendinizi sorumlu hale getirirsiniz :




- açık anahtarınızı ifşa edin;
- dijital imza üretir.



Bu nedenle harcama zamanı en kritik zamandır: **Bitcoin harcamak bilinçli ve mümkün olduğunca kontrollü yapılması gereken bir eylemdir**.



## Coin Kontrol



Bitcoin protokolünde _account_ veya _monetary units_ gibi öğeler mevcut değildir. UTXO kavramı, şiddetle tavsiye ettiğim aşağıdaki kursta mükemmel bir şekilde açıklanmıştır:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Bitcoin ile biriktirdiğiniz ve daha sonra harcadığınız şey, Satoshi ile ölçülen küçük veya büyük hesap birimleridir, `harcanmamış işlem çıktıları` ile temsil edilir, **UTXO**, `para` olarak da adlandırılır. Bir işlem oluşturmak için UTXO'ları kullandığınızda, bunlar tamamen yok edilir ve yerlerine başka UTXO'lar oluşturulur.



Yazılım Cüzdanları, protokol tarafından sağlanan belirli algoritmaları benimseyerek "rastgele" seçilen coinleri kullanarak bu seçimi otomatik olarak yapmak için geliştirilmiştir. Bu algoritmaların karşıladığı tek kriter, harcama için gereken miktarı karşılamaktır.



Geliştiriciler tarafından seçilen algoritmaya bağlı olarak, farklı yaşlardaki UTXO'ları bir araya getirebilir veya en yeni veya "en eski" olanı harcamayı tercih edebilirler. En iyi Yazılım Cüzdanları, kullanıcıyı önemli bir seçimle baş başa bırakmayı da planlamaktadır.



"Coin Seçimi" olarak da adlandırılan "Coin Kontrolü", bazı Yazılım Cüzdanlarında bulunan ve işleminizi oluştururken harcayacağınız UTXO'ları **manuel olarak seçmenize** olanak tanıyan bir özelliktir.



Sırasıyla 21.000, 42.000 ve 63.000 Satoshi'lük 3 UTXO'ya sahip bir Wallet'imiz olduğunu varsayalım.



![img](assets/en/01.webp)



Eğer 24.000 Sats harcamanız ve otomatik seçimi bir algoritmanın yapmasına izin vermeniz gerekiyorsa, iyi bir Software Wallet, 24 bin Sats ve Miner ücretlerini ödemek için UTXO 1 + UTXO 2'yi birleştirmeyi seçebilir ve başlangıç Wallet'in dahili bir Address'sine geri dönen bir kalan yaratabilir.



![img](assets/en/02.webp)



İşlem sonrasında, sadece UTXO'ların sayıldığı Wallet'deki yeni durum şu şekilde özetlenebilir.



![img](assets/en/03.webp)



Ancak doğru yazılım ve farkındalığınızla farklı, bazı açılardan daha doğru bir seçim yapabilirdiniz. Örneğin, yalnızca UTXO2'yi seçerek (42.000 Sats'ten).



![img](assets/en/04.webp)



Wallet'ünüzde, UTXO seviyesinde, öncekinden farklı görünen bir son durumla.



![img](assets/en/05.webp)



## Neden manuel coin control?



![img](assets/en/06.webp)



Yukarıdaki iki örnekte, bakiye aslında aynıdır `108,280 Sats`. 24.000 Sats harcadıktan sonra, manuel seçim olmadan Wallet'de 2 UTXO'umuz olacaktı; Coin manuel kontrolü ile toplam 3'ümüz var.



Kendimize sorabileceğimiz soru şudur: **neden bütün bunları yapıyoruz?** `UTXO1`'i kullanmamamızın çeşitli nedenleri vardır veya olabilir **ve bunların hepsi, harcama aşamasında manuel coin control'ü etkinleştirmenin takip edilmesi gereken iyi uygulamalardan biri olmasının temelini oluşturur**.



UTXO'ları seçmek, bazı yönleri diğerlerine tercih etmenize olanak tanır. Seçim gerçekten de ulaşmak istediğiniz hedeflere bağlıdır.



### Gizlilik



Manuel Coin kontrolü söz konusu olduğunda ana avantajlardan biri **harcama yapan için daha büyük bir gizliliktir**. Örneğimizi ele alalım: 24.000 Satoshi'ün _manuel Coin seçimi olmaksızın_ harcanması. Bitcoin'ün Blockchain'si kamuya açık bir kayıt olduğundan, dışarıdan bir gözlemci, 21.000 Sats'nın `UTXO1' ve 42.000 Sats'nın `UTXO2' girişlerinin yanı sıra 38.280 Sats'nın `UTXO5'inin **her üçünün de aynı kullanıcıya ait olduğunu** şüpheye yer bırakmayacak şekilde beyan edebilir.



Öte yandan, `UTXO2` manuel olarak seçildiğinde, `UTXO1` tamamen ayrılmış olarak kalır ve UTXO setinde oturarak daha uygun bir zamanda harcanmayı bekler.



UTXO1, Exchange'de mal ve hizmetler için alınan bir ödeme gibi bir KYC kaynağından gelebilirken, diğer UTXO'lar gelmeyebilir. Bir UTXO-kyc'yi daha gizli olan diğerleriyle karıştırmak, KYC olmayan fonların anonimlik setini tehlikeye atar.



**KYC fonları kaçınılmaz olarak ödeyenin kimliğine kadar izlenebilir. Eğer bu senin cüzdanın olsaydı, harici bir gözlemcinin kimliğini bu kadar mutlak bir kesinlikle tespit etmesini ister miydin?**



O halde, örneğin UTXO'ların manuel seçimini uygulayan Cüzdanların, bu tür durumlar ortaya çıktığında kullanılacak bir işlev olan **bir veya daha fazla UTXO'nun** ayrılmasına izin verdiğini düşünmeye çalışın.



KYC fonlarının kyc olmadan satın alınan Wallet'den ayrı bir Bitcoin'de tutulması gerektiğine ikna olmama rağmen, eğer durumunuz buysa, bazı adreslerinizin ayrılması önemli bir yardımcıdır ve harcama girdilerinizi manuel olarak seçmeyi öğrenerek bundan yararlanabilirsiniz.



### Ücretlerden tasarruf



Bir harcama yapmak için doğru UTXO'ün seçilmesi, **ücret optimizasyonuna** olanak sağlar. Yine ilk örneğimizden yola çıkarak, Software Wallet yapılacak harcamayı karşılamak için iki UTXO seçmiştir. İki UTXO, ağa gösterilecek iki imza anlamına gelir. Bu da işlemin vByte açısından daha büyük bir "ağırlığa" sahip olduğu anlamına gelir.



Öte yandan, Coin manuel kontrolünü kullanarak, yalnızca tutarı karşılamaya yeterli olanı seçebilir ve işlemin "ağırlığını" azaltarak ücretlerden tasarruf edebilirsiniz.



Ücretlerin yüksek olduğu, ancak Bitcoin On-Chain harcamak zorunda kaldığınız zamanlarda (örneğin, bir Lightning Network kanalı açmak için), Coin kontrolünün başvurulacak doğru ekonomik teşvik olduğu ortaya çıkar.



### Kalıntıların bir araya toplanması



Bir ödeme yaptığınızda ve Bitcoin On-Chain kullandığınızda, para üstü alma olasılığı neredeyse her zaman bir kesinlik haline gelir. Her kalan, ağa (ve özellikle ödemenin alıcısına) kaynak girişinizle ilişkilendirilebilecek bir Address'inizi ifşa ettiğinden, kendi başına küçük bir gizlilik kaybıdır.



En iyi Wallet HD'lerin kalıntılar için generate özel adresleri olduğunu düşünürsek, bunları kolayca tanıyabilir ve yapılan çeşitli işlemlerin tüm kalıntılarını "ayırabilirsiniz"; belirli bir miktara ulaştıklarında bunları manuel olarak seçebilir ve birleştirebilir veya Lightning Network'e geçebilir (benim tercih ettiğim yöntem) ve harcamalarda kaybedilen gizliliği yeniden kazanmak için bunları işleyebilirsiniz.



### Cold Wallet'dan yapılan harcamalar



Cold Wallet, uzun bir süre boyunca bir kenarda tutmak üzere herhangi bir miktarda fon depolamak için makul ölçüde iyi bir güvenlik derecesi elde edilebilecek bir araçtır. Bununla birlikte, öngörülemeyen olaylar meydana gelebilir, bu nedenle tasarruflara el atma ve bazı beklenmedik harcamaları karşılama ihtiyacı ortaya çıkar.



Benim yaklaşımımı kaç kişi paylaşabilir bilmiyorum ama tavsiyem **harcamayı asla doğrudan Cold Wallet'den yapmamanız, aynı adresler arasındaki değişikliği almamak için**. Harcamayı karşılamak için gereken UTXO'ları manuel olarak seçmeyi öğrenin, bunları bir Wallet Hot'e aktarın ve işleminizi ikincisinden hazırlayın. Daha sonra herhangi bir değişiklik olursa, bunu bir Cold Wallet Address'a geri gönderebilir (miktar yeterliyse), başka harcamalar için kullanabilir veya az önce gördüğümüz gibi yine de ayırabilirsiniz.



## Pratik sunum


Nedenin teknik tanıtımından sonra, Coin manuel kontrolünün masaüstü ve mobil olmak üzere farklı yazılımlarla nasıl uygulamaya konulacağını görelim. Size aralarındaki küçük farkları göstermek için her zaman seçilen araçların her birine aktarılmış aynı Wallet BIP39'u kullanacağız.



## Wallet Masaüstü



### Sparrow



Sparrow kullanıyorsanız, Wallet'unuzu açın ve soldaki menüden _UTXOs_ öğesini seçin. Wallet'unuzla ilişkili tüm UTXO'ların bir listesini göreceksiniz.



Bunlardan birinin üzerine fare ile tıklamanız ve ardından _Seçileni Gönder_ seçeneğini seçmeniz yeterlidir. Sparrow ayrıca seçimden sonra harcanabilecek toplam miktarı da komutun hemen yanında gösterir. Grafiksel olarak Sparrow, seçilen UTXO'i mavi renkle vurgulayarak gösterir.



![img](assets/en/07.webp)



Birden fazla da seçebilirsiniz. Listede bitişik olmayan UTXO'ları seçmek için_CTRL_ tuşu ile kendinize yardımcı olun.



![img](assets/en/08.webp)



UTXO'ü manuel olarak seçtikten sonra, işlemi oluşturmaya başlayabilirsiniz ve Sparrow size grafiksel olarak nasıl oluşturulduğunu gösterecektir.



![img](assets/en/09.webp)



#### UTXO'ün ayrıştırılması



Fonları ayırmak, onları Wallet içinde "kilitlemek" anlamına gelir, böylece bir işlemde girdi olarak kullanılamazlar. Sparrow, her zaman _UTXOs_ menüsünden erişilen bu işlevselliğe izin verir: fareyi "kilitlenecek" UTXO'nin üzerine getirin ve farenin sağ düğmesine tıklayın. Bu prosedürün özellikleri arasında _Freeze UTXO_ görünecektir. Sparrow cüzdanları ile Coin'leri bu şekilde ayırabileceksiniz.



![img](assets/en/29.webp)



### Elektrum



Wallet masaüstünüz Electrum ise, UTXO'ları ya _Adresler_ menüsünden ya da _Coinler_ menüsünden manuel olarak seçebileceğinizi bilmelisiniz. Her iki menüde de seçim, fareyi istenen UTXO'in üzerine getirip sağ tıkladıktan sonra _Coin kontrolüne ekle_ seçilerek yapılır.



![img](assets/en/10.webp)



Bu yazılımla bile birden fazla UTXO seçebilir, birbirlerine bitişik değillerse klavyenizdeki _CTRL_ tuşuyla yardımcı olabilirsiniz.



![img](assets/en/11.webp)



Grafiksel olarak Electrum, Green'de seçilen UTXO'ları vurgulayarak size seçimi gösterirken, altta Coin kontrolünden sonra mevcut bakiyeyi gösteren aynı renkte vurgulanmış bir çubuk görünür.



![img](assets/en/12.webp)



Çıktıyı veya çıktıları seçtikten sonra, _Gönder_ menüsünden her zaman yaptığınız gibi işleminizi oluşturabilirsiniz.



#### UTXO'ün ayrıştırılması



Electrum bu işlevi, belirli bir UTXO'yi seçmek için gideceğiniz _Coins_ menüsüne giderek ve ardından sağ tıklama ile _Freeze_ seçeneğini seçerek sağlar. Address'i _Adresler_ menüsünden para olmadan bile "dondurabilir" veya "Coin" yı harcamamak için "dondurabilirsiniz".



![img](assets/en/28.webp)



### Nunchuk



Nunchuk, açıldıktan sonra ana menüden UTXO'ları manuel olarak seçmenize olanak tanır. Nunchuk'u başlatın ve _Madeni paraları görüntüle_ seçeneğine tıklayın.



![img](assets/en/13.webp)



Bu, Wallet'inizdeki tüm UTXO'ları içeren pencereyi açar; burada her tutarın yanındaki onay işaretini etkinleştirerek bir veya daha fazlasını seçebilirsiniz. Seçiminizi yaptıktan sonra _COPYreate transaction_ ile devam edin.



![img](assets/en/14.webp)



Bundan sonra hedef Address'u girebilir ve miktarı ve ücretleri ayarlayabilirsiniz.



![img](assets/en/15.webp)



#### UTXO'ın ayrıştırılması



Bütünlük adına, Nunchuk özellikleri arasında bir (veya daha fazla) UTXO'yu ayırmaya da izin verir ve bunu iki farklı şekilde yapar. Paraları görüntüle_ menüsüne erişin ve paralar listesinden manuel olarak seçim yapın. Ardından sağ alttaki _More_ menüsüne tıklayın: _Lock coins_ seçeneğini seçebileceğiniz bir seçenekler listesi görünecektir.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Ayrıca _Coin details_ penceresine erişmek için UTXO için ayrılmış alana tıklayabilirsiniz. Burada söz konusu UTXO'i kilitleme/kilidini açma komutu sağ üst köşede görünür.



![img](assets/en/41.webp)



### Blockstream Uygulaması



Eskiden Green olarak bilinen Blockstream App masaüstü, işlemi oluşturmaya başladığınızda Coin seçimi yapmanıza olanak tanır. Bu nedenle, Wallet'nizi açın ve _Gönder_ seçeneğine tıklayın.



![img](assets/en/16.webp)



Hedef Address'i uygun alana yapıştırın ve ardından _Manuel Coin seçimi_ öğesini seçin.



![img](assets/en/17.webp)



Bu, bir veya daha fazla UTXO madeni para seçebileceğiniz pencereyi açar. Aşağıdaki örnekte iki madeni para seçtik. Bundan sonra, _Confirm Coin Selection_ seçeneğine tıklayarak seçiminizi onaylayın.



![img](assets/en/18.webp)



Tutarı ve ücretleri ayarlayın ve ardından işleminize normal şekilde devam edin.



![img](assets/en/19.webp)



⚠️ N.B. Green'ün _Coins_ menüsünde, UTXO'yi ayırma olasılığını öngören _Lock_/_Unlock_ öğeleri vardır. Bu özellik yalnızca Multisig olarak adlandırılan hesaplarda etkinleştirilir; ayrıca yalnızca `Dust` eşiğine yakın, çok küçük miktarda UTXO seçilerek etkinleştirilir.



## Wallet mobil



Cüzdanlar, UTXO'ların manuel olarak seçilmesine olanak tanıyan mobil cihazlardan da seçilebilir. İlk örnek olarak Blue Wallet'ü görelim.



### Mavi Wallet



Bu Wallet'nın kullanıcısıysanız, açın ve Cüzdanlarınızdan biriyle ilgili kontrol ekranlarına girmek için tıklayın. Coin kontrol kılavuzuna erişmek için harcama aşamasına girmeli ve ardından _Gönder_ seçeneğine tıklamalısınız.



![img](assets/en/21.webp)



Bir sonraki ekranda sağ üst köşedeki üç nokta ile gösterilen menüleri seçin. Bir dizi komut içeren bir açılır pencere açılır. Sonuncusunu seçin: _Coin Control_.



![img](assets/en/22.webp)



Bu noktada Mavi Wallet tüm UTXO'larınızı gösterir. Miktarlara ek olarak, farklı renklerle grafiksel olarak ayırt edilirler.



![img](assets/en/27.webp)



Seçmek için UTXO'u seçin ve ardından _Jeton Kullan_ öğesini seçin.



![img](assets/en/23.webp)



Blue Wallet, işlemi oluşturmaya devam etmek için sizi _Gönder_ penceresine geri götürür. Tutarı ve ücretleri ayarladıktan sonra _Sonraki_ öğesini seçin.



![img](assets/en/24.webp)



Bu noktada, genellikle yaptığınız gibi işlemi sonlandırabilirsiniz.



#### Bir UTXO'in ayrıştırılması



Blue Wallet ayrıca UTXO'ları ayırarak harcama için kullanılamaz hale getirmenize olanak tanır, bu da mobil bir cihazdan bir Wallet için fena bir işlev değildir. Coin kontrolüne az önce açıklanan prosedürle erişirsiniz ve UTXO'ü seçtikten sonra _Jeton Kullan_ yerine _Dondur_ seçeneğini belirleyin.



![img](assets/en/26.webp)



### Nunchuk



Nunchuk'un mobil sürümü, kullanıcının Coin kontrolü yapabilmesini de sağlar. Bu uygulamayı mobilden kullanıyorsanız, açın ve _Wallet_ menüsüne gidin. Oradan _Jetonları görüntüle_ seçeneğini seçin.



![img](assets/en/30.webp)



UTXO'ların listesinin göründüğü pencerede _Seç_ öğesine tıklayın.



![img](assets/en/38.webp)



Her UTXO'nın yanında bir seçim işlevi görünür. Masaüstü versiyonunda olduğu gibi, Nunchuk mobile'da da manuel seçim, miktarın yanındaki küçük kareyi işaretleyerek yapılır. Ekranda seçilen UTXO'ların sayısı ve mevcut toplam miktar gösterilir. Bitirdiğinizde, sol alt köşedeki ₿ sembolüne tıklayın; bu, işlemi oluşturmaya başlama komutudur.



![img](assets/en/31.webp)



Şimdi tutarı seçerek ve _Continue_ düğmesine tıklayarak işlemi tamamlayabilirsiniz.



![img](assets/en/32.webp)



Bir hedef Address, açıklama yapıştırarak ve ücret ayarlarını özelleştirerek her zaman yaptığınız gibi devam edin.



#### UTXO'in ayrıştırılması



UTXO'ları mobil Nunchuk ile de ayırabilirsiniz. Özel jeton listesi penceresine erişin ve ayırmak istediğiniz UTXO'un yanındaki oku seçin.



![img](assets/en/42.webp)



Sikke ayrıntıları_ için ayrılmış alanı göreceksiniz, burada _Bu sikkeyi kilitle_ seçeneğini seçebilirsiniz.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper bu kılavuzda göreceğimiz son Wallet'dir. İşlevselliğinin Coin kontrolüne bir Wallet tek-sig ile uygulandığını görüyoruz, ancak böyle bir kullanım bu özel uygulamanın amacı değildir. Keeper'ı telefonunuza kurduktan sonra başlatın ve bir miktar para içeren bir Wallet açın. Ana ekranın ortasında _Tüm Paraları Görüntüle_ seçeneğine tıklayın.



![img](assets/en/34.webp)



Keeper UTXO'lara genel bir bakış gösterir. Seçim ekranına erişmek için _Gönderilecek Seç_ seçeneğine tıklayın.



![img](assets/en/35.webp)



Uygun komuta tıklayarak paraları işaretleyerek seçebilirsiniz. İşiniz bittiğinde _Gönder_'e tıklayın.



![img](assets/en/36.webp)



Bitcoin Keeper sizi doğrudan _Gönder_ menüsüne götürür ve burada seçilen UTXO'lar ile işlemi oluşturabilirsiniz.



![img](assets/en/37.webp)



## Hardware Wallet



Bu kılavuzda görülen Yazılım Cüzdanlarının her biri, Donanım Cüzdanlarınızdan birinin yalnızca Interface saati olabilir. Bu, çevrimdışı imzalama cihazı için Coin kontrolünün şu ana kadar görülen adımlarla gerçekleştirildiği anlamına gelir.



### Genel tavsiyeler



Coin kontrolü, işlem girdilerinizi seçmek için çok etkili bir uygulamadır. Fonlarınızı satın alırken/alırken Satoshilerinizin kaynağını iyi etiketlediyseniz, manuel seçim daha da verimli olur. Bu tekniği iyi öğrenmek istiyorsanız, aşağıdaki öğreticiyi tavsiye ederim:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Daha önce `kalıntıların ayrıştırılması` hakkında konuşmuştuk. Kalıntıları daha sonra işlenmek üzere kilitlemek ve gizliliği yeniden kazanmak istiyorsanız (Layer 2'de takas), her aldığınızda onları `etiketlemeye' dikkat etmelisiniz. Şu ana kadar görülen Yazılım Cüzdanları arasında yalnızca Electrum, UTXO kalıntılarını bir bakışta görünür kılmak için grafiksel olarak renklendirmektedir. Sparrow gibi diğerleri ise UTXO'in türetilme yolundaki zinciri gösterir (`m/84'/0'/0'/1/11`).



Bu tekniği etkili bir şekilde uygulamak için, aldığınız değişikliğe her zaman bir açıklama eklemeyi unutmayın: paranızı gönderdiğiniz kişi (bir ödeme, bir eğitim veya başka bir şey), değişiklikle ilişkili Address'yi bilir ve birlikte yaptığınız işlemden geldiği için size ait olduğunu bilir!