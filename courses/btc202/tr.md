---
name: İlk Bitcoin düğümünüzü kurma
goal: Bir Bitcoin düğümünün anlaşılması, kurulması, yapılandırılması ve kullanılması
objectives: 


  - Bir Bitcoin düğümünün rolünü ve amacını anlamak.
  - Mevcut farklı donanım ve yazılım çözümlerini tanımlama.
  - Bir Full node (Bitcoin core) kurun ve yapılandırın.
  - Interface Şemsiyeyi kullanın ve faydalı uygulamalar ekleyin.
  - Kişisel bir Wallet'yı kendi düğümüne bağlayın.
  - Gelişmiş ayarları ve en iyi güvenlik uygulamalarını keşfedin.


---
# Egemen bir bitcoin kullanıcısı olun



Bitcoinlerinizi kendinizin muhafaza etmesini teşvik eden "Anahtarlarınız yoksa, coin'leriniz de yok" atasözünü muhtemelen biliyorsunuzdur. Kendi anahtarlarınıza sahip olmak gerçekten de önemli bir ilk adımdır, ancak yeterli değildir. Gerçek parasal egemenliğe ulaşmak için kendi Bitcoin node'unuzu da kurmanız ve kullanmanız gerekir. Bu kurs, Bitcoin yolculuğunuzdaki bu temel adımda size rehberlik etmek için tasarlanmıştır!



BTC 202, teknik bir uzman olmasanız bile size kendi Bitcoin düğümünüzü nasıl atacağınızı öğretmek için tasarlanmış erişilebilir bir kurstur. Bitcoin düğümünün ne olduğunu, ne işe yaradığını ve kendi düğümünüzü atmanın neden kesinlikle gerekli olduğunu tanımlayarak başlayacağız. Daha sonra donanımınızı seçme, gerekli yazılımı yükleme, Wallet'unuzu bağlama ve daha ileri götürmek için ilk olası optimizasyonları yapma konusunda size adım adım rehberlik edeceğim.



Bir Bitcoin düğümü çalıştırmak sadece uzmanlar için bir seçenek değil; bir gerekliliktir. Her kullanıcının anlaması ve uygulaması gereken bir esneklik aracıdır. Bu kurs, egemen bir bitcoin kullanıcısı olmak için başlangıç noktanızdır!




+++




# Giriş


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Kursa genel bakış


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Bir Bitcoin düğümünü kolayca ve bağımsız olarak nasıl kuracağınızı, yapılandıracağınızı ve kullanacağınızı öğreneceğiniz BTC 202'ye hoş geldiniz. Ancak hepsi bu kadar değil: Bitcoin sistemindeki düğümlerin yeri ve işlevi hakkında da daha fazla bilgi edineceksiniz. Kurs, teorik açıklamalar ve rehberli uygulamalı pratik arasında gidip gelmektedir.



### Bölüm 1 - Giriş



Kursun bu ilk bölümünde, temel kavramları açıklığa kavuşturacağız ve ardından daha kesin tanımlara geçeceğiz. Düğüm nedir? Node, Wallet ve Miner arasındaki farklar nelerdir? Daha sonra Bitcoin core ve protokolün uygulamaları hakkında bilgi edineceksiniz. Amaç aynı dili konuşmak, kafa karışıklığını önlemek ve sağlam bir teorik temel oluşturmaktır.



### Bölüm 2 - Egemen bir bitcoin kullanıcısı olmak



Bu ikinci bölümde, kendi Bitcoin düğümünüzü çalıştırmanın neden önemli olduğunu açıklayarak başlayacağım. Daha sonra var olan farklı düğüm türlerini (tam, pruned, SPV...), nasıl çalıştıklarını ve teknik etkilerini inceleyeceğiz.



Ardından, avantajları ve dezavantajları da dahil olmak üzere bir Bitcoin düğümünü çalıştırmak için mevcut olan yazılıma genel bir bakış sunacağız. Son olarak, ihtiyaçlarınız ve bütçeniz için doğru donanımı seçmeye yönelik çok pratik bazı önerilerle bitireceğiz.



Dolayısıyla bu bölüm, egemen bir bitcoin kullanıcısının izleyeceği yolu göstermektedir: bir node çalıştırmanın neden gerekli olduğunu anlamak, node türünü seçmek, bu seçime bağlı olarak yazılımı seçmek ve seçilen yazılıma bağlı olarak uygun donanımı belirlemek.



### Bölüm 3 - Bir Bitcoin düğümünün kolayca kurulması



Bu hazırlık tamamlandıktan sonra, kendi kendini barındırmayı ve bir Bitcoin ve Lightning düğümünün kurulumunu basitleştiren ev bulut işletim sistemi Umbrel'e ayrılmış Bölüm 3 ile pratik yapma zamanı.



Umbrel'e kısa bir giriş yaptıktan sonra, kendi DIY makinenizde kurulum ve yapılandırma sürecinde size rehberlik edecek ayrıntılı bir eğitim vereceğiz. Bu bölümün amacı açıktır: ilk tamamen işlevsel ve senkronize Bitcoin düğümünüze sahip olmak.



### Bölüm 4 - Wallet'inizi düğümünüze bağlama



Artık bir Bitcoin düğümü kurduğunuza göre, sıra onu kullanmaya geldi! Bu bölümde, Wallet yönetim yazılımınızı (Sparrow wallet gibi) kendi Address dizinleyicinize (Electrs veya Fulcrum) veya doğrudan Bitcoin core'e nasıl bağlayacağınızı öğreneceksiniz, böylece artık genel sunuculara bağımlı olmayacaksınız.



Ayrıca indeksleyicilerin rolünü ve düğümünüze bağlanmanın çeşitli yöntemlerini (LAN, Tor, Tailscale, vb.) inceleyeceğiz. Son olarak, son bölümde, günlük bitcoin kullananlar için Umbrel'de bulunan en kullanışlı uygulamaları gözden geçireceğiz.



### Bölüm 5 - Gelişmiş kavramlar ve en iyi uygulamalar



BTC 202'nin bu son bölümünde amacımız bilginizi derinleştirmektir. İlk olarak, yeni Bitcoin node'unuzla benimsemeniz gereken en iyi uygulamalara ve uzun vadede onu nasıl koruyacağınıza bakacağız.



Daha sonra, IBD sürecini ve eş bulmayı ayrıntılı olarak anlamak, bir düğümün anatomisini keşfetmek ve son olarak ayarlarınıza ince ayar yapmak için `Bitcoin.conf` dosyasını nasıl kullanacağınızı öğrenmek de dahil olmak üzere, kursta daha önce ele alınan bazı teorileri gözden geçirmek için zaman ayıracağız.



### Bölüm 6 - Son bölüm



Tüm Plan ₿ Network kurslarında olduğu gibi, final bölümünde Bitcoin düğümleri hakkındaki bilginizi test etmek için bir final sınavı bulacaksınız.



Peki, ilk Bitcoin düğümünüzü açmaya hazır mısınız? Egemenlik için bir rota belirleyin!



## Bitcoin düğümü nedir?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Yaratıcısı Satoshi Nakamoto tarafından tanımlandığı üzere, Bitcoin kendisini eşler arası bir elektronik nakit sistemi olarak sunmaktadır. Beyaz Kitap'ın başlığı olan bu basit cümle, Bitcoin'ün doğasına ilişkin pek çok ipucu barındırmaktadır:




- Öncelikle, Satoshi, Bitcoin'i bir "sistem", başka bir deyişle, belirli bir hizmet sağlamak veya belirli bir işlevi yerine getirmek için etkileşime giren tutarlı bir donanım ve yazılım bileşenleri kümesi olarak tanımlamaktadır;
- Ardından, bu sistemin elektronik paranın, yani bir tür maddi olmayan para biriminin kullanılmasını sağladığını açıklıyor;
- Son olarak, bu sistemin herhangi bir merkezi varlığa bağlı olmadığına dikkat çekiyor: "eşler arası", yani sistemi işleten kullanıcıların kendileri.



Bitcoin bir sistem olduğu için mutlaka bilgisayarlar üzerinde çalıştırılmalıdır. Ve eşler arası yapısı nedeniyle, bu makineleri çalıştırma sorumluluğunu üstlenenler kullanıcıların kendileridir. "Bitcoin düğümü" dediğimiz şey, tam olarak Bitcoin protokolünü uygulayan yazılımın (Bitcoin core gibi, ancak buna daha sonra geri döneceğiz) üzerinde çalıştığı bilgisayardır. Bu, Bitcoin'in merkezi bir otorite olmadan çalışmasını sağlayan şeydir: doğrulama, binlerce kullanıcıya ait binlerce bağımsız makine tarafından dağıtılmış bir şekilde gerçekleştirilir.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Eşler Arası Elektronik Nakit Sistemi*. https://Bitcoin.org/Bitcoin.pdf



Bitcoin'in güvenliğini sağlayanlar tam da bu kullanıcılardır. Eric Voskuil'in *Cryptoeconomics* adlı kitabında açıkladığı gibi, Bitcoin'in güvenliği ne Blockchain'a, ne hash gücüne, ne doğrulamaya, ne ademi merkeziyetçiliğe, ne kriptografiye, ne açık kaynağa ne de oyun teorisine dayanır. Bitcoin'in güvenliği öncelikle kendilerini kişisel riske maruz bırakmaya istekli olan bireylere bağlıdır. Ademi merkeziyetçilik bu riskin çok sayıda bireye yayılmasını sağlar ve sistemin sağlamlığını sağlayan da yalnızca bu bireylerin direnme kabiliyetidir.



Bu prensibi anlamak kolaydır: Bitcoin tek bir kişinin sahip olduğu tek bir düğüme bağlı olsaydı, tüm riskleri tek başına üstleneceği için o kişiyi hapsetmek ağı kapatmak için yeterli olurdu. Dünyanın dört bir yanına yayılmış on binlerce düğümle risk yayılmaktadır: Bitcoin'nin kapatılması için bu operatörlerin her birinin etkisiz hale getirilmesi gerekecektir.



![Image](assets/fr/048.webp)



Bu nedenle, bu kursun geri kalanında bazı şeyleri açıklığa kavuşturmak için birkaç kavramı ayırt edebilir ve adlandırabiliriz:




- Bitcoin para birimi: bu sistem içindeki işlemler için kullanılan hesap birimi;
- Bitcoin ağı: tüm bağlı düğümlerin kümesi;
- Bitcoin düğümleri: Bitcoin'in bir uygulamasını çalıştıran makineler;
- Bitcoin uygulamaları: protokolü yürütülebilir talimatlara çeviren yazılım;
- Bitcoin protokolü: sistemin çalışmasını yöneten kurallar bütünü;
- Bitcoin sistemi: tüm bu Elements'in tutarlı bir kombinasyonu.



### Bitcoin düğümünün rolü



Bitcoin düğümleri birlikte Bitcoin ağı olarak bilinen yapıyı oluşturur. Tüm sistemin, merkezi bir otoriteye veya sunucu hiyerarşisine başvurmadan özerk bir şekilde çalışmasını sağlarlar.



Başlangıçtan itibaren Bitcoin, her kullanıcının kişisel bir düğüm çalıştırmasına izin verecek şekilde tasarlanmıştır. Bu durum, Bitcoin core ve node rollerini birleştiren günümüzün Wallet yazılımı ile geçerliliğini korumaktadır. Ancak günümüzde, bu işlev genellikle ayrıştırılmıştır: birçok modern Bitcoin cüzdanı sadece harici düğümlere (aynı kişiye ait olsun ya da olmasın) bağlanan cüzdanlardır.



### Blockchain'i saklayın



Bir düğümün ilk görevi Blockchain'nin yerel bir kopyasını muhafaza etmektir. Merkezi bir otoriteyi dahil etmeden Bitcoin üzerinde Double-spending'yı önlemek için, her kullanıcı sistemde hiçbir işlemin bulunmadığını kontrol etmelidir. Bundan emin olmanın tek yolu Bitcoin üzerinde yapılan tüm işlemleri bilmektir. Bu nedenle, tüm işlemler zaman damgalı ve bloklar halinde gruplandırılmıştır ve her düğüm Blockchain'nin tamamını saklar.



> Bir işlemin olmadığını teyit etmenin tek yolu tüm işlemlerden haberdar olmaktır.

Nakamoto, S. (2008). *Bitcoin: Eşler Arası Elektronik Nakit Sistemi*. https://Bitcoin.org/Bitcoin.pdf



Blockchain bu nedenle gelişen bir kayıttır: bir Miner tarafından her yeni blok yayınlandığında, düğüm bunu zincirin kendi yerel kopyasına eklemeden önce geçerliliğini kontrol eder. Bugün (Temmuz 2025) itibariyle, Blockchain'ın tamamı 675 GB'ı aşmaktadır ve ortalama her 10 dakikada bir yeni bir blok eklendiğinden bu boyut büyümeye devam etmektedir.



![Image](assets/fr/049.webp)



Düğüm ayrıca **UTXO seti** olarak bilinen, herhangi bir zamanda mevcut olan tüm UTXO'ların yerel bir kaydını tutar. Bu veritabanı harcanmamış tüm Bitcoin parçalarını içerir. Bu konuyu kursun son bölümünde ayrıntılı olarak tekrar ele alacağız.



### İşlemleri doğrulama ve dağıtma



Bir düğümün ikinci rolü, işlemlerin doğrulanmasını ve yayılmasını sağlamaktır. Yeni bir işlem düğüme ulaştığında (Wallet yazılımı veya başka bir düğüm aracılığıyla), bir dizi kurala (mutabakat kuralları ve röle kuralları) uygun olup olmadığını kontrol edecektir. Örneğin:




- harcanmış bitcoinler UTXO setinde (harcanmamış çıktıların veritabanı) bulunmalıdır;
- imzanın geçerli olması ve tüm harcama koşullarının karşılanması gerekir (geçerli komut dosyası);
- çıktıların toplam miktarı girdilerin toplam miktarını aşmamalıdır; bu da maliyetlerin negatif olamayacağı anlamına gelir.



![Image](assets/fr/050.webp)



Doğrulamadan sonra, işlem düğümün onaylanmamış işlemler için ayrılmış geçici bir bellek alanı olan Mempool'sinde saklanır ve daha sonra bağlı olduğu diğer ağ eşlerine iletilir. Bu dağıtım ve doğrulama mekanizması düğümden düğüme devam eder. Bu şekilde, işlem Bitcoin ağı boyunca yayılır ve her düğüm, daha sonra ilk onayına göre hareket eden bir Miner tarafından geçerli bir bloğa dahil edilene kadar Mempool'de saklar.



### Blokları kontrol edin ve dağıtın



Düğümün üçüncü rolü mayınlı blokları yönetmeyi içerir. Bir Miner geçerli bir Proof of Work ile yeni bir blok keşfettiğinde, bu blok ağda yayınlanır. Düğümler bunu alır, tüm protokol kurallarına uygun olup olmadığını kontrol eder ve geçerli ise kendi yerel Blockchain kopyalarına entegre eder. İşlemlerde olduğu gibi, yeni onaylanan bloklar daha sonra düğüme bağlı tüm eşlere iletilir. Bu süreç Bitcoin ağındaki tüm düğümler yeni bloktan haberdar olana kadar devam eder.



![Image](assets/fr/051.webp)



## Yay ile Wallet arasındaki fark nedir?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Bitcoin kullanırken iki farklı yazılım türünü birbirinden ayırmak önemlidir: düğüm ve Wallet.



Bir Bitcoin düğümü, yukarıda da belirtildiği gibi, eşler arası ağa aktif olarak katılan bir yazılım parçasıdır. Üç ana görevi yerine getirir:




- gW-77'nin yedeği,
- işlem doğrulama ve aktarma,
- blok doğrulama ve röle.



Bitcoin Wallet ise özel anahtarlarınızı saklamak ve yönetmek için tasarlanmış bir yazılım parçasıdır. Bu anahtarlar, kilitleme komut dosyalarını yerine getirerek (genellikle bir imza yoluyla) bitcoinlerinizi harcamanızı sağlar. Bir Wallet, Blockchain'in durumuna danışmak ve oluşturduğu işlemleri yayınlamak için bir düğüme (yerel veya uzak) bağlanabilir, ancak bu şekilde ağda bir katılımcı değildir.



Bazı durumlarda, hem Full node hem de Wallet olarak hizmet veren Bitcoin core'de olduğu gibi, bu iki işlev aynı yazılım içinde bir arada bulunur. Bununla birlikte, birçok popüler Wallet programı (Sparrow, BlueWallet, vb.) işlemleri yayınlamak ve Wallet bakiyesini belirlemek için harici bir düğüme (ister kendinizin ister üçüncü bir tarafın) bağlantı gerektirir.



![Image](assets/fr/052.webp)



## Bir düğüm ile bir Miner arasındaki fark nedir?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Düğüm ve Miner kavramları sıklıkla birbirine karıştırılmaktadır. Oysa bu iki Elements sistem içinde birbirinden tamamen farklı işlevler yerine getirir.



Başlangıçta, Bitcoin 2009 yılında Satoshi Nakamoto tarafından başlatıldığında, her kullanıcının ağa bir bütün olarak katılması bekleniyordu. Bu nedenle, orijinal Bitcoin yazılımı aynı anda birkaç işlevi birleştirdi: bir Wallet, bir düğüm ve aynı zamanda yeni bloklar üretebilen bir Miner olarak hareket etti. O zamanlar Mining'ın zorluğu çok düşüktü. Tek yapmanız gereken, blokları bulmak ve ödül olarak bitcoin almak için bilgisayarınızda Bitcoin yazılımını çalıştırmaktı.



Ancak Bitcoin'ün giderek yaygınlaşması ve madenci sayısının artmasıyla birlikte Mining'teki rekabet ortamı radikal bir değişim geçirmiştir. Günümüzde Mining, özel altyapılarla donatılmış endüstriyel oyuncuların hakimiyetinde olan son derece rekabetçi bir faaliyet haline gelmiştir. Yeni bir blok çıkarmak için gereken güç artık o kadar büyüktür ki, bireysel bir kullanıcının bunu yalnızca geleneksel bir bilgisayar kullanarak başarması neredeyse imkansızdır. Sonuç olarak, Mining artık öncelikle ASIC (*Uygulamaya Özel Entegre Devreler*) adı verilen özel makineler kullanılarak gerçekleştirilmektedir. Bu çipler, Bitcoin üzerinde Mining için kullanılan algoritma olan çift SHA-256'yı çalıştırmak üzere özel olarak optimize edilmiştir.



![Image](assets/fr/053.webp)



Bu evrim karşısında, Bitcoin düğümünün ve Miner'nın rolleri net bir şekilde farklılaşmıştır. Yukarıda gösterildiği gibi, bir Bitcoin düğümünün rolü tamamen bilgi ve doğrulama tabanlıdır. Miner'nın rolü ise farklıdır:




- Mempool'de bekleyen işlemleri seçer.
- Bu işlemleri entegre eden bir aday blok oluşturur.
- Deneme yanılma yöntemiyle geçerli bir Proof of Work arar.
- Geçerli bir kanıt bulursa, bloğu kendi düğümü üzerinden diğer düğümlere yayınlar.



Bir Miner ağ ile etkileşime geçmek için bir Bitcoin düğümüne ihtiyaç duyar.



Miner'ün rolü de bazen kıyıcıdan farklıdır. Kıyıcı, görevi bir havuzun sunucusu tarafından sağlanan Hash şablon bloklarını, Bitcoin'nin değil, paylaşımlar için tanımlanan zorluk hedefini karşılayan hash'leri aramak olan bir makinedir. Gerçek blok yapımı, işlem seçimi veya Bitcoin'nin kendi zorluk derecesine göre Proof-of-Work aramasının yanı sıra dağıtımı da içeren Mining sürecinin geri kalanı doğrudan havuzlar tarafından gerçekleştirilir.



![Image](assets/fr/054.webp)



Son olarak, Miner ile düğüm arasında ekonomik teşvik açısından önemli bir fark vardır. Bir Bitcoin düğümünü çalıştırmak doğrudan parasal fayda sağlamaz. Öte yandan, Mining'de yer almak, bulunan her blok için ödüller (sübvansiyonlar ve işlem ücretleri) getirir.



Bölüm 2'de, bir Bitcoin düğümü kurmanın ve kullanmanın tamamen finansal olmanın ötesinde pratik ve kişisel faydalarını daha ayrıntılı olarak inceleyeceğiz.



## Bitcoin core ve protokol uygulamaları


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin protokolü bir yazılım değildir: ağ kullanıcıları arasında paylaşılan bir dizi zımni kuraldır. İşlem geçerlilik koşullarını, para yaratma mekanizmalarını, blok formatını, Proof-of-Work koşullarını ve diğer birçok özelliği tanımlar. Bu protokolle etkileşime geçmek için kullanıcıların bu kuralları uygulayan bir yazılım çalıştırması gerekir: bu, Bitcoin'nin bir **uygulaması** olarak bilinir.



Bu nedenle bir uygulama düğüm yazılımıdır: Bitcoin ağındaki diğer makinelerle arayüz oluşturabilen, blokları ve işlemleri indirebilen, doğrulayabilen, depolayabilen ve yayabilen ve yerel olarak mutabakat ve röle kurallarını uygulayabilen bir program. Her uygulama, belirli bir programlama dilinde yazılmış, kendi mimarisi, performansı ve ergonomisi ile protokolün somut bir yorumudur. Her uygulamanın kendi sorumlulukları ile birlikte kendi geliştirme organizasyonu da olacaktır.



Bu uygulamalar arasında bir tanesi açık ara öndedir: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Bir ölçüt haline gelen tarihi bir uygulama



Bitcoin core, Bitcoin protokolü için referans yazılımdır. Satoshi Nakamoto tarafından 2008-2009 yıllarında yazılan orijinal koddan türetilmiştir ve onun doğrudan bir devamıdır. Başlangıçta "*Bitcoin*", daha sonra "*Bitcoin QT*" (Qt kütüphanesi aracılığıyla grafiksel bir Interface eklenmesi nedeniyle) olarak bilinen yazılım, yazılımı ağdan açıkça ayırmak için 2014 yılında "*Bitcoin core*" olarak yeniden adlandırılmıştır. 0.5 sürümünden bu yana iki bileşenle dağıtılmaktadır: `Bitcoin-qt` (grafiksel Interface) ve `bitcoind` (komut satırı Interface).



Teorik olarak, Bitcoin core, Bitcoin protokolünü temsil etmez; daha ziyade, birçok uygulama arasında sadece bir uygulamadır. Bununla birlikte, kitlesel olarak benimsenmesi, yaşı, kodunun sağlamlığı ve geliştirme sürecinin titizliği ile ayırt edilir. Sonuç olarak, uygulamada, Bitcoin core tarafından uygulanan kurallar fiilen Bitcoin protokolünün kurallarıdır: kullanıcılar, geliştiriciler, madenciler ve ekosistem hizmetleri neredeyse yalnızca bu protokole atıfta bulunur.



### Uygulamaların mevcut dağılımı



Ağustos 2025'te Luke Dashjr] (https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (ekosistemde tanınmış bir geliştirici) tarafından toplanan verilere göre, ağın halka açık düğümleri arasındaki uygulama dağılımı aşağıdaki gibidir:




- Bitcoin core**: 87.düğümlerin %3'ü
- Bitcoin Knots**: 12.5
- Diğer kümülatif uygulamalar**: 0.2 (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Başka bir deyişle, 10 genel düğümden yaklaşık 9'u Bitcoin core çalıştırmaktadır. Ağın geri kalanı daha marjinal istemcilere dayanıyor (Knots'un payı son aylarda, özellikle de `OP_RETURN` boyut sınırı konusundaki tartışmaların ardından keskin bir şekilde artmış olsa da). Bu alternatif uygulamalar genellikle tek bir kişi ya da küçük bir ekip tarafından sürdürülmektedir.



**Not:** Ancak bu rakamlar, öncelikle *dinleyen düğümlere*, yani gelen bağlantıları kabul eden düğümlere (8333 numaralı bağlantı noktası açık) dayandığından yine de tahmini rakamlardır. Dinlemeyen düğümleri* saymak çok daha karmaşıktır, çünkü onlara doğrudan bağlanmak imkansızdır: inisiyatifin giden bir bağlantı şeklinde onlardan gelmesini beklemeniz gerekir. Luke Dashjr'ın sitesi bu *dinlemeyen düğümleri* de saymaya çalıştığını iddia ediyor, ancak bunlar hakkında tamamen doğru veriler elde etmek imkansız ve bu istatistiklerin güncellenmesi kaçınılmaz olarak gerçeğin gerisinde kalıyor.



### Bitcoin core'nin dahili çalışması



Bitcoin core C++ dilinde yazılmıştır. Ayrıca, gönüllü olan veya çeşitli kuruluşlar tarafından (genellikle ekosistemde Core'un geliştirilmesinde menfaati olan şirketler tarafından) ödeme yapılan bir geliştirici topluluğu tarafından sürdürülen açık kaynaklı bir projedir. [Kod GitHub'da barındırılmaktadır] (https://github.com/Bitcoin/Bitcoin) ve geliştirme titiz bir şekilde takip edilmektedir:




- Katkıda bulunanlar** tekliflerini _pull requests_ (PR) şeklinde gönderirler. Prensip olarak, herkes bir değişiklik önerebilir, ancak bunun test edilmesi, belgelenmesi ve bir akran değerlendirme sürecinden geçmesi gerekir.
- Bakımcılar** PR'ları onaylama ve birleştirme hakkına sahiptir. Projenin tutarlılığını ve istikrarını garanti edenler onlardır. Temmuz 2025'te bunlardan beşi vardır: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao ve Ryan Ofsky.
- Şubat 2023'ten bu yana **baş bakım sorumlusu** bulunmamaktadır. Bu rol ilk olarak Satoshi'in lansmanında Bitcoin Nakamoto tarafından, daha sonra Nakamoto'nun 2011'in başlarında ayrılmasının ardından Gavin Andresen tarafından ve son olarak 2014'ten 2023'e kadar Wladimir J. Van Der Laan tarafından üstlenilmiştir.



![Image](assets/fr/057.webp)



Bitcoin core'nin geliştirilmesi meritokratik bir mantık izler: yeni katkıda bulunanlar, herhangi bir değişiklik önermeden önce kodu incelemeye ve test etmeye teşvik edilir. Kararlar teknik fikir birliğine dayanır ve büyük değişiklikler (özellikle fikir birliği olan alanlarda) posta listeleri veya PR inceleme kulüpleri gibi halka açık kanallarda yukarı akış tartışmalarını gerektirir.



### Diğer Bitcoin uygulamaları



Benimsenme açısından marjinal olsa da, başka istemciler de mevcuttur. Bunlardan en önemlisi Luke Dashjr tarafından geliştirilen Bitcoin Knots, Bitcoin core'in ek seçenekler ve geliştirmeye daha muhafazakar bir yaklaşım içeren bir Fork'sıdır. Bunlar arasında işlem formatları üzerinde daha sıkı kısıtlamalar bulunmaktadır.



![Image](assets/fr/058.webp)



Ayrıca şunu da belirtebiliriz:




- Libbitcoin**: Amir Taaki tarafından geliştirilen ve Eric Voskuil tarafından bakımı yapılan modüler bir C++ kütüphanesi;
- Bcoin**: artık aktif olarak bakımı yapılmayan bir JavaScript uygulaması;
- BTCD/btcsuit**e: Go'da bir uygulama.



Bu projeler ekosistemin çeşitliliğine katkıda bulunmaktadır, ancak benimsenmeleri çok sınırlı kalmaktadır ve bu da Bitcoin core'nin bağımsız olarak gelişmesini zorlaştırmaktadır.



### Çekirdek geliştiricilerin gücü



Bitcoin core geliştiricilerinin Bitcoin üzerinde doğrudan kontrole sahip olduğunu düşünebilirsiniz, ancak durum böyle değildir. Protokolde bir değişiklik dayatamazlar. Onların rolü kod önermektir. Bu kodu kullanıp kullanmamaya karar vermek, düğümleri aracılığıyla her kullanıcıya bağlıdır.



Bu, Bitcoin core'taki bir değişikliğin fikir birliğine varılamaması durumunda, Bitcoin core'ı güncellemeyerek ya da sadece uygulamayı değiştirerek düğümler tarafından göz ardı edilebileceği anlamına gelir. Tersine, kullanıcılar tarafından istenen bir özellik Çekirdek geliştirme sürecinde engellenirse, başka bir uygulamaya veya Fork projesine geçmek her zaman mümkündür.



Bu dersin ilerleyen bölümlerinde tartışacağımız üzere, protokolün kurallarına uyan birimleri kabul ederek protokolün bir versiyonuna (ve dolayısıyla ilgili para birimine) fayda sağlayan, ekonomik ağırlıklarına göre düğümlerdir (yani tüccarlar). Dolayısıyla Bitcoin üzerindeki gerçek yönetim gücü, geliştiricilerde değil bu tüccarlarda bulunmaktadır.




# Egemen bir bitcoin kullanıcısı olun


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Neden kendi düğümünü kendin atıyorsun?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Bir Bitcoin düğümünü işletmenin, kişisel kazanç olmaksızın, yalnızca ağın merkezsizleştirilmesine hizmet eden, tamamen fedakarca bir eylem olduğuna dair yaygın bir inanç vardır. Bazıları bunu bitcoin kullanıcılarının sistemi desteklemesi ve Bitcoin'e minnettarlıklarını göstermesi için bir görev olarak görüyor.



Gerçekten de, önceki bölümlerde de belirttiğimiz gibi, düğüm atmanın doğrudan maddi bir getirisi yoktur. Bu nedenle bunu yapmakta kişisel bir çıkar olmadığı düşünülebilir. Yine de kendi düğümünüzü işletmek birçok bireysel fayda sağlar. Sizi bu konuda ikna etmek için bu bölümde neden kendi Bitcoin düğümünüzü kurmanız ve kullanmanız gerektiğine dair hem teknik hem de stratejik tüm nedenleri sunacağım.



### İşlemlerin daha gizli yayılması



Wallet yazılımı harici bir düğüme bağlandığında, işlemlerini sizin kontrolünüz altında olmayan bir altyapıya iletir. Bu durum gözetim açısından bariz riskler doğurur: uzak düğümün operatörü, miktarlar ve sıklıklar dahil olmak üzere işlemlerinizin ayrıntılarını analiz edebilir ve belirli meta verileri (IP adresleri, zamanlar ve konumlar gibi) çapraz kontrol ederek bunları potansiyel olarak kimliğinizle ilişkilendirebilir.



Aslında, bir önceki bölümde belirtildiği gibi, cüzdanlar Bitcoin ağı ile sihirli bir şekilde iletişim kurmaz; bakiyelere danışmak veya işlemleri yayınlamak için bir düğüme bağlanmaları gerekir. Eğer kendi node'unuzu hiç kurmadıysanız, bu Wallet'nizin üçüncü bir tarafın (genellikle yazılımın arkasındaki şirket) altyapısına bağlı olduğu anlamına gelir. Bu üçüncü taraf, özellikle de bir şirket ise, bu verileri gözlemleyebilir, kullanabilir ve hatta ifşa edebilir: ticari nedenlerle, yasal kısıtlamalar altında veya korsanlığın bir sonucu olarak.



![Image](assets/fr/059.webp)



Kendi node'unuzu kullanarak işlemlerinizi aracıları atlayarak doğrudan ağa yayınlarsınız. Düğümünüzün güvenliğini düzgün bir şekilde sağladığınız (bunu daha sonra tartışacağız) veya belirli standartlara uyduğunuz sürece, hiçbir bilgi açığa çıkmaz: ne IP Address'iniz ne de işlemlerinizin ayrıntıları kontrol etmediğiniz bir varlıktan geçmez. Bu, Bitcoin üzerindeki gizliliğinizi korumak için temel bir ön koşuldur.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Sansüre tabi olmayan işlemler



Yukarıda belirtilen aynı nedenlerden dolayı, üçüncü taraf bir düğüme dayalı Wallet yazılımı sansür riskine karşı savunmasızdır: uzak düğümün operatörü çeşitli nedenlerle belirli işlemleri iletmeyi reddedebilir. Bunları şüpheli veya politikasına aykırı olarak değerlendirebilir. İşlem, düğümün aktarım kurallarına uymuyorsa da engellenebilir. Son olarak, operatör işlemlerinizin yayınlanmasını engellemek için özellikle IP Address'nizi hedefleyebilir.



Tersine, kendi düğümünüzü kullanarak, işlemlerinizin eşler arası ağ içinde yayılmasını sağlarsınız. Bu, bir aracıya bağımlı olmadan işlemlerinizin dağıtımı üzerinde tam kontrole sahip olduğunuz anlamına gelir. İşlem, size bağlı düğümlerin mutabakat ve aktarım kurallarına uygun olduğu sürece, ağda yayınlanacak ve daha sonra, yeterli ücretlerin dahil edilmesi koşuluyla, bir Miner tarafından bir bloğa entegre edilecektir. Kendi düğümünüzün olması, işlemlerinizin tarafsız, izinsiz onaylanmasını garanti eder.



### Bağımsız veri doğrulama



Kişisel bir node olmadan, Address bakiyeniz, işlem onay durumunuz ve blok geçerliliği gibi bilgilere erişim için üçüncü bir tarafa bağımlı kalırsınız. Bu, harici düğümün doğruluğuna ve bütünlüğüne zımni bir güven anlamına gelir.



![Image](assets/fr/060.webp)



Bir Full node çalıştırmak, her işlem ve her blok için tüm protokol kurallarını kendiniz kontrol edebileceğiniz anlamına gelir. Sonuç olarak, Wallet'nız tarafından görüntülenen bakiye uzak bir sunucudan alınan veriler değil, Blockchain'ün blok blok onaylanmış tam bir kopyasından yerel olarak hesaplanan bir sonuçtur. Bu yaklaşım, bitcoin kullanıcılarının özdeyişine tam bir anlam kazandırmaktadır:



> Güvenmeyin, doğrulayın.

### Sistem güvenliğinin daha iyi dağıtılması



Ağa katılan her düğüm Bitcoin'nin yedekliliğini ve esnekliğini güçlendirir. Bilginin yayılmasını kolaylaştırır ve yeni eşlerin birbirleriyle bağlantı kurmasını sağlar. Düğümler olmasaydı sistem çalışamaz hale gelirdi.



Gördüğümüz gibi, Bitcoin'in güvenliği ademi merkeziyetçiliğe, Mining'a veya kriptografiye dayanmamaktadır: her sistemde olduğu gibi, bireylere dayanmaktadır. Daha doğrusu, düğüm operatörlerinin baskıya direnme kabiliyetine bağlıdır.



Bitcoin gibi merkezi olmayan sistemleri diğerlerinden ayıran şey, riskin bu sistemlerin işleyişine dahil olan herkes arasında dağıtılmasıdır. Kendi Bitcoin düğümünüzü çalıştırmak, örneğinizin güvenliğini sağlayarak bu riskin bir kısmını kabul etmek anlamına gelir; bunu yaparken, diğer düğüm operatörlerinin risk yükünü de hafifletirsiniz.



Yani doğrudan kişisel bir fayda değil: bir düğüm çalıştırmak sizi ağın güvenliğinden kısmen sorumlu kılar. Hepsinden önemlisi, bu kolektif bir faydadır, çünkü katılımınız riskin yayılmasına yardımcı olur. Buna karşılık, Bitcoin'i güvenilir bir şekilde kullanma becerinizi artırırsınız.



### Sistem anlayışınızı derinleştirin



Full node'nin kurulumu önemsiz bir işlem değildir. Yazılım yüklemeyi, temel işleyişi anlamayı, senkronizasyonu izlemeyi, sorun olması durumunda günlükleri incelemeyi ve hatta terminali kullanmayı içerir. Bu, protokol anlayışınızı derinleştirmenize neden olacaktır. Bu dolaylı ama önemsiz olmayan bir avantajdır.



Bu bilgiyi edinmek alete olan güveninizi güçlendirir ve hata yapma veya dolandırıcılığa maruz kalma riskini azaltabilir. Kendi düğümünüzü atmak da bir öğrenme biçimidir.



### Hangi kuralların uygulanacağını seçme



Genellikle yanlış anlaşılan önemli bir husus, bir düğümü çalıştırmanın yerel olarak uyguladığınız kuralları seçmenize izin vermesidir. İki ana kural türü vardır:





- Konsensüs kuralları**:



Bunlar Bitcoin protokolünün temel kurallarıdır, sistemin bütünlüğünü sağlar ve işlemlerin ve blokların doğrulanması için kriterler oluşturur. Bu mutabakat kurallarına uymayan herhangi bir işlem asla geçerli bir bloğa dahil edilemez. Örneğin, girişlerinden birinde geçersiz imza bulunan bir işlem sistematik olarak hariç tutulacaktır.



Bu kuralları değiştirmek protokolü ve dolayısıyla para birimini değiştirmekle eşdeğerdir (Hard Fork). Bununla birlikte, kuralları değiştirmeye çalışmadan bile, mevcut kuralları katı bir şekilde uygulamanın basit gerçeği belirli bir güç sağlar: eğer bir blok kuralları ihlal ederse, düğüm bunu derhal reddeder.





- Röle kuralları**:



Bunlar, Mempool'da kabul edilen ve eşlere iletilen onaylanmamış işlemlerin yapısını tanımlamak için mutabakat kurallarına eklenen her bir Bitcoin düğümüne özgü kurallardır. Her düğüm bu kuralları yerel olarak yapılandırır ve uygular, bu da neden bir düğümden diğerine farklılık gösterebileceklerini açıklar. Bu kurallar yalnızca onaylanmamış işlemler için geçerlidir: bir düğüm tarafından "standart dışı" olarak kabul edilen bir işlem yalnızca geçerli bir blokta zaten görünüyorsa kabul edilecektir. Bu kuralların değiştirilmesi düğümü Bitcoin sisteminden çıkarmaz.



Örneğin, hiçbir ücreti olmayan bir işlem, mutabakat kurallarına göre tamamen geçerlidir, ancak Bitcoin core aktarım politikasına göre varsayılan olarak reddedilecektir, çünkü `minRelayTxFee` parametresi `0.00001` (BTC/kB cinsinden) olarak ayarlanmıştır. Bununla birlikte, kendi düğümünüzde, daha düşük ücretli işlemleri aktarmak için bu eşiği düşürmek veya tersine, düşük ücretli işlemlerin aktarılmasını önlemek için sınırı örneğin 2 Sats/vB'ye çıkarmak mümkündür.



Kendi düğümünüzü döndürmek, iddia etmek anlamına gelir: "Doğrulamayı seçtiğim şeyi, kendi benimsediğim kurallara göre doğrularım "*. Böylece sistemin yönetiminde bir aktör haline gelirsiniz, size kabul edilemez görünen bir evrimi reddedebilir veya kendi kriterlerinize göre bir güncellemeyi onaylayabilirsiniz.



Böylece düğümünüz sayesinde kurallar üzerinde ne kadar güce sahip olduğunuzu hızlıca anlamaya çalışabiliriz. Ve bu gücün kapsamı kuralın türüne bağlı olacaktır.



#### Röle kuralları için



Aktarma kuralları söz konusu olduğunda, esas olan ekonomik faaliyetinden bağımsız olarak bir düğüme sahip olmaktır. Burada söz konusu olan, belirli işlem türlerini aktarmayı kabul edip etmediğinizdir.



Örneğin, 1 sat/vB'den daha düşük ücretli işlemlerin Bitcoin'da kabul edilmesi gerektiğine inanıyorsanız, düğümünüzdeki bu kuralı bu işlemleri yayınlayacak şekilde ayarlayabilir, böylece bir Miner sonunda bunları geçerli bir bloğa dahil edene kadar ağda yayılmalarını kolaylaştırabilirsiniz. Esasen bu, işlemlerin yayılması üzerinde bir güç meselesidir: her düğümün karar verme gücü vardır, çünkü bir işlem türünü aktarmayı kabul etmek, Bitcoin ağında kabul edilmesini teşvik etmekle eşdeğerdir. Sonuç olarak, birden fazla düğüm işletiyorsanız, her düğümün ağ üzerinde kendi bağlantıları ve etki alanları olduğundan, aktarım politikası üzerinde daha fazla etkiye sahip olursunuz.



Aslında, belirli aktarım kuralları ile yapılandırılmış bir veya daha fazla düğüme sahip olmak, ağın hangi bölümünün belirli bir işlem türünü yaymayı kabul ettiğini belirlemek anlamına gelir. Bitcoin işlemlerinde olduğu gibi eşler arası bir grafikte bir mesajın yayılması, süzülme teorisinin mantığını takip eder. Her bir düğümü aktif (`p` = iletir) veya inaktif (`1-p`) olabilen bir site olarak düşünün. P` oranı kritik bir eşiği (`p_c`) geçer geçmez, dev bir bileşen ortaya çıkar: işlem ağı kat etmeyi başarır ve bir Miner'ye ulaşma şansına sahiptir. Her düğümün ortalama 8 giden bağlantıya sahip olduğu Bitcoin gibi bir ağda, `p_c` eşiği genellikle sadece yüzde birkaç olarak belirlenir, hatta bazı düğümlerin çok fazla sayıda bağlantısı varsa daha da düşüktür.



![Image](assets/fr/061.webp)



P`, `p_c` altında kaldığı sürece, bir işlem izole ceplerle sınırlı kalır ve bir Miner'e ulaşmaz. Bu eşik aşılır aşılmaz, neredeyse anında tüm ağa yayılır.



Nihayetinde, bir işlemin bir bloğa dahil edilip edilmeyeceğine karar veren her zaman madencilerdir. Bununla birlikte, düğümler işlemlerin dağılımını etkileyerek yukarı yönde müdahale eder: madencilerin belirli bir işlemden haberdar olup olmayacaklarını belirlerler. Eğer bir işlem madencilere iletilmezse, madencilerin bu işlemi bir bloğa dahil etmeleri imkansızdır.



Bu nedenle, ağ belirli bir işlem türü için zaten süzülme aşamasındaysa birkaç düğüm daha eklemek yalnızca marjinal bir etkiye sahip olacaktır, ancak süzülme eşiği yaklaştıkça belirleyici olabilir. Birkaç düğüme sahip olmak ya da onları etkilemek, özellikle de iyi bağlantılara sahiplerse, `p` değerini artırabilir ya da azaltabilir ve sonuç olarak hangi işlemlerin madenciler tarafından görüleceğini ve sonunda kabul edileceğini belirleyen röle kurallarını dolaylı olarak yönlendirebilir.



#### Uzlaşma kuralları için



Düğümünüzün mutabakat kuralları üzerindeki etkisi söz konusu olduğunda, ekonomik ağırlığı her şeyden önce belirleyici olacaktır. Bu çok önemli bir kavramdır: herhangi bir para biriminin değeri doğrudan Exchange'ü kolaylaştırma kabiliyetiyle ilgilidir. Gerçekten de, bir nesne Exchange'te mal veya hizmetler için kimse tarafından kabul edilmiyorsa, teorik olarak hiçbir parasal faydası yoktur. Örneğin, hiçbir tüccar çakıl taşlarını ödeme aracı olarak kabul etmiyorsa, bunların para olarak kullanımı yoktur. Elbette, fayda bireysel ölçekte öznel bir kavram olmaya devam etmektedir, ancak belirli bir bölgede, bir nesneyi KİS-174 aracı olarak kabul eden tüccar sayısı ne kadar fazlaysa, bu nesnenin bu bölgede yaşayan insanlar için parasal bir faydaya sahip olma olasılığı o kadar yüksektir.



Birçok tüccarın mal karşılığında Exchange cinsinden altın kabul ettiği bir köy örneğini ele alalım: altının köylüler için parasal bir faydası olması muhtemeldir. Bu, bir para biriminin faydasının doğrudan tüccarların onu kabul etme veya reddetme kararlarına bağlı olduğunu gösterir.



Bu kavram Bitcoin sistemindeki güç dinamiklerini anlamak için çok önemlidir. Satoshi şunu açıkça ortaya koymaktadır: Bitcoin bir elektronik nakit sistemidir; başka bir deyişle, bir tür para birimi olan Bitcoin (veya BTC) sunan bir hizmet sağlamaktadır. Protokol kuralları geriye dönük uyumlu olmayacak şekilde değiştirildiğinde (Hard Fork), bu yeni bir sistem ve dolayısıyla yeni bir para birimi yaratmak anlamına gelir. Bu Fork'un başarısı ya da başarısızlığı ekonomisinin büyüklüğüne bağlıdır ve bu da bu yeni para birimini kabul eden tüccarların sayısına göre belirlenir.



![Image](assets/fr/062.webp)



Bir örnek verelim: Bitcoin'nin bir Hard Fork'e maruz kaldığını varsayalım. Bu durumda 2 farklı para birimi olacaktır: BTC-1 (orijinal, değişmemiş versiyon) ve BTC-2 (farklı mutabakat kurallarına sahip yeni para birimi). BTC-1'i kabul eden tüm tüccarlar bunu yapmaya devam eder, ancak BTC-2'yi reddederse, teorik olarak BTC-2'nin parasal faydası çok sınırlı olacaktır. Bir kullanıcı olarak, Exchange'de hiçbir tüccarın mal veya hizmetler için BTC-2'yi istemeyeceğini bildiğimden, BTC-2'yi saklamak ve kullanmakla ilgilenmeyeceğim. Tersine, tüccarların %50'si yalnızca BTC-2'yi kabul etmeyi seçerse ve kalan %50 yalnızca BTC-1'i kabul ederse, BTC-1'in faydası teoride yarı yarıya azalmış olacaktır. "Teoride" terimini kullanıyorum çünkü fayda bireysel düzeyde öznel kalmaktadır ve vaka bazında anlaşılması zor olan çok sayıda faktöre (bölge ve tüketim alışkanlıkları gibi) bağlıdır.



Bitcoin'te, belirli bir ekonomik ağırlığa sahip herhangi bir varlık olarak anlaşılan "tüccar" rolü, elbette işletmeleri (fiziksel mağazalar, çevrimiçi satış siteleri, hizmet sağlayıcılar, vb.) ve aynı zamanda Exchange'te diğer para birimleri için Bitcoin'ü kabul ettikleri için Exchange platformlarını ve bir blokta bir işlemi dahil etme hizmeti için Exchange'te ücretler yoluyla Bitcoin'ü kabul ettikleri için madencileri içerir.



Mutabakat kuralları söz konusu olduğunda, düğümünüz ekonomik faaliyetinizi bir para birimine veya diğerine yönlendirmenize olanak tanır. Örneğin, evinizde 10 tam düğümünüz varsa, ancak önemli bir ekonomik faaliyetiniz yoksa, bir Fork sırasında etkiniz neredeyse sıfır olacaktır. Buna karşılık, Bitcoin'i kabul eden 200 mağazalık bir zinciri yönetmek için kullanılan tek bir düğüm önemli bir ekonomik ağırlık kazandırır.



Dolayısıyla önemli olan düğüm sayısı değil, destekledikleri ekonomik faaliyetin önemidir. Dahası, ekonomik faaliyetiniz kontrol etmediğiniz bir düğüme bağlıysa, o düğüme bağlı kaldığınız sürece hangi para birimini kullanacağınıza düğümün sahibi karar verecektir. Bu nedenle kendi düğümünüzü çalıştırmak ve kullanmak sistem yönetişimi bağlamında özellikle önemlidir:



> Senin düğümün değil, senin kuralların değil.


## Farklı Bitcoin düğüm tipleri


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Dolayısıyla bir Bitcoin düğümü, Bitcoin protokolünün bir uygulamasını çalıştıran bir makinedir. Düğümlerin bu ortak tanımının arkasında, hepsi aynı düzeyde özerklik, kaynak tüketimi ve ağ için kullanışlılık sunmayan birkaç olası yapılandırma vardır. Bu bölümde, kullanımınıza ve donanım kısıtlamalarınıza uygun bir düğüm mimarisi seçmenize yardımcı olmak için bu farklılıkları anlamaya çalışacağız.



### Tam düğüm



Bir Full node basitçe Bitcoin bloğundan tüm Blockchain'u indiren, her bloğu bağımsız olarak doğrulayan ve tüm bu Blockchain'un geçmişini yerel olarak saklayan bir Genesis düğümüdür. Bu, Bitcoin Nakamoto tarafından hayal edildiği şekliyle bir Satoshi düğümünün "normal" biçimidir.



![Image](assets/fr/063.webp)



Full node'ün kimseye güvenmesine gerek yoktur çünkü sistemdeki tüm bilgileri doğrular ve bilir. Size en fazla garantiyi veren düğüm türüdür: üçüncü bir tarafa güvenmeden, bir ödemenin geçerli olup olmadığını, bir bloğun geçerli olup olmadığını, bir yeniden düzenlemenin meşru olup olmadığını vb. bilirsiniz.



Pratikte, bir Full node, blok dosyaları için birkaç yüz gigabayt, komut dosyalarını doğrulayabilen bir işlemci, Mempool ve önbellekler için RAM ve sabit bant genişliği dahil olmak üzere önemsiz olmayan kaynaklar gerektirir. İlk senkronizasyon (*IBD*) tüm geçmişi okur ve doğrular: yoğun bir işlemdir, ancak yalnızca bir kez gerçekleşir. Bir Full node ağa aktif olarak katılır, blokları ve işlemleri aktarır ve diğer eşlere yardımcı olmak için gelen bağlantıları kabul edebilir.



İhtiyaçlarınıza bağlı olarak, Full node'inize bir indeksleyici ekleyebilirsiniz. Bitcoin core, belirli amaçlar için yararlı olabilecek isteğe bağlı bir özellik olarak işlem indeksleme sunar (varsayılan olarak devre dışıdır). Ancak, bireysel kullanıcılar için genellikle en çok aranan özellik olan Address indeksleyicisini içermez. Bunu düzeltmek için düğümünüze Electrs veya Fulcrum gibi özel bir yazılım yükleyerek ilişkili UTXO'lardan Address bakiye doğrulama sorgularını hızlandırabilirsiniz. Dizinleyicinin rolüne ayrı bir bölümde daha ayrıntılı olarak geri döneceğiz.



### pruned düğümü



pruned düğümü, Genesis bloğundan zincirin başına kadar her şeyi bir Full node olarak en çok çalışmayla doğrular, ancak **blok dosyalarının yalnızca en yeni bölümünü tutar**. Eski bloklar kontrol edildikten sonra, ayarlayabileceğiniz bir alan sınırının altında kalmak için bunları kademeli olarak siler. Disk alanı kısıtlamalarınız varsa bu yapılandırma idealdir: tüm Blockchain geçmiş arşivini depolamadan blok doğrulamasının bağımsızlığını korursunuz. Bu seçenek özellikle Bitcoin core'i özel bir makine kullanmadan sadece kişisel bilgisayarınıza kurmak istiyorsanız kullanışlıdır.



![Image](assets/fr/064.webp)



Bu seçeneğin teknik sonuçları oldukça basittir: pruned düğümü işlemlerinizi yayınlama, aktarıma katılma, blokları ve işlemleri doğrulama ve zinciri izleme konusunda mükemmel bir kapasiteye sahiptir. Öte yandan, diğer uygulamalar (örneğin, tam kaşifler, indeksleyiciler, cüzdanlar) için sınırlarının ötesinde bir geçmiş veri kaynağı olarak hizmet veremez. Bu nedenle arşiv (ya da global bir indeks) gerektiren işlevler kullanılamayacaktır.



Pratik açıdan, Sparrow wallet gibi Wallet yönetim yazılımını bağlamak için bir pruned düğümü kullanabilirsiniz. Ancak, Wallet'unuzda budama sınırından önceki işlemleri tarayamazsınız. Örneğin, 901 458 numaralı blokta kayıtlı bir işleminiz varsa, ancak düğümünüz yalnızca 905 402'den itibaren blokları tutuyorsa (çünkü en eskisi pruned olmuştur), bu işlemi tarayamazsınız. Öte yandan, düğümünüz hala bu blok yüksekliğine sahipken zaten taramış olsaydınız, Wallet yönetim yazılımınız bilgileri saklayacak ve ilgili UTXO'ların bakiyesini doğru şekilde görüntüleyecektir.



Kısacası, yazılımınız zaten bu düğüme bağlıyken yeni bir Wallet oluşturursanız, Wallet takibi bir pruned düğümünde sorunsuz çalışır. Öte yandan, eski bir Wallet'i geri yüklerseniz, düğüm tarafından artık tutulmayan geçmiş işlemler açıkça geri alınamayacağından zorluklarla karşılaşabilirsiniz.



### Hafif düğüm / SPV



Bir SPV (*Basitleştirilmiş Ödeme Doğrulaması*) düğümü veya hafif düğüm, işlem ayrıntılarını değil yalnızca blok başlıklarını tutar ve bir işlemin başlığına sahip olduğu bir blokta (ağaçlar aracılığıyla Merkle kanıtları) olduğuna dair kanıt elde etmek için diğer tam düğümlere güvenir. Basitleştirilmiş ödeme doğrulaması kavramı yeni değildir, Beyaz Kitap'ın 8. bölümünde Satoshi Nakamoto'nun kendisi tarafından önerilmiştir.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Eşler Arası Elektronik Nakit Sistemi*. https://Bitcoin.org/Bitcoin.pdf



Bu tür bir düğüm, depolama ve CPU kullanımı açısından bir Full node veya hatta bir pruned düğümünden çok daha hafiftir. Bu nedenle SPV düğümü daha küçük cihazlar ve kesintili bağlantılar için çok uygundur. Aslında, genellikle doğrudan Wallet'ya, özellikle de Blockstream Uygulaması gibi mobil yazılımlara entegre edilir.



Buradaki değiş tokuş güven ve gizliliktir: bir SPV istemcisi komut dosyalarını veya doğrulama politikalarını kendisi kontrol etmez; en çok işe sahip zincirin geçerli olduğunu varsayar ve yanıtlar için bir veya daha fazla tam düğüme bağlıdır. Bu nedenle bu tür bir düğüm kullanmak, üçüncü taraf bir düğüme bağlanmaktan daha iyi bir seçenektir; ancak yine de bir Full node veya hatta bir pruned düğümüne sahip olmaktan daha az avantajlıdır.



![Image](assets/fr/065.webp)



### Hangi ihtiyaç için hangi düğüm?





- Mobil / acemi kullanıcı



Mobil uygulamada sadece bir Wallet'u olan acemi bir kullanıcı için SPV düğümü kullanmak kesinlikle başlamak için en iyi yoldur. Kurulum hızlıdır, az kaynak gerektirir ve deneyim basit ve akıcıdır. Bu, belirli bilgileri kendiniz doğrulayabileceğiniz ve bu nedenle üçüncü taraf node'lara daha az güvenebileceğiniz ve aynı zamanda işlemlerin yayınlanması söz konusu olduğunda daha bağımsız olabileceğiniz anlamına gelir.





- PC / orta düzey kullanıcı



PC'si olan bir ara kullanıcı, Full node'nin neredeyse tüm avantajlarından yararlanmak için makinelerine günlük olarak aşırı yük bindirmeden bir pruned düğümü kurabilir: tam doğrulama, orta düzeyde disk kullanımı ve basit bakım. Özel bir makineye yatırım yapmadan veya disk alanınızı aşırı yüklemeden masaüstü cüzdanlarınızı bağlamak ve işlemlerinizin dağıtımında bağımsız kalmak için ideal bir çözümdür.





- Sovereign Bitcoiner / gelişmiş



Bitcoin kullanımınızda tamamen bağımsız olmak ve kendinizi daha sonra bir dizinleyici, bir Lightning düğümü veya hatta bir Block explorer gibi gelişmiş kullanımlarla sınırlamamak istiyorsanız, bir Full node en iyi çözüm olmaya devam etmektedir. Bu kursta keşfedeceğimiz şey de tam olarak bu!



## Yazılım çözümlerine genel bakış


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Yazılım tarafında, bir Bitcoin düğümünü çalıştırmanın 2 ana yolu vardır:




- doğrudan Bitcoin core (önerilen) veya Bitcoin Knots gibi bir protokol uygulaması yükleyin,
- veya bir Bitcoin uygulamasını aynı şekilde entegre eden, ancak aynı zamanda bir Interface yönetim sistemi, bir uygulama deposu ve kullanıma hazır araçlar (Lightning, tarayıcılar, dizin sunucuları, hatta Bitcoin dışında kendi kendini barındıran uygulamalar...) içeren anahtar teslimi bir dağıtım (genellikle "_node-in-a-box_" olarak adlandırılır) kullanın.



Her iki yaklaşım da aynı hedefe götürür: kendi düğümünüze sahip olmak, ancak Interface kurulumu ve kullanımı, bakım, genişletilebilirlik ve maliyet açısından farklılık gösterirler. Bu bölümde bunu inceleyeceğiz.



### Ham Bitcoin düğüm uygulamaları



Ham bir uygulama yüklemek, herhangi bir ek yazılım Layer olmadan doğrudan bir Bitcoin protokol uygulamasının (Core gibi) yazılımını kullanmak anlamına gelir. İhtiyaçlarınıza göre yapılandırmayı, güncellemeleri ve ilgili hizmetleri (indeksleme, API, Lightning, yedeklemeler vb.) kendiniz yönetirsiniz.



Bu en egemen ve esnek yaklaşımdır: tam olarak neyin çalıştığını, verilerin nerede olduğunu ve her şeyin nasıl çalıştığını bilirsiniz. Öte yandan, bir Bitcoin düğümünün basit çalışmasının ötesine geçmek istediğiniz anda daha karmaşık hale gelir. Amacınız sadece bir node'a sahip olmaksa, karmaşıklık bir node-in-a-box ile karşılaştırılabilir, hatta daha da azdır, çünkü bu sadece bir yazılım yükleme meselesidir.



#### Bitcoin core (ultra çoğunluklu müşteri)



[Bitcoin core ağın ultra çoğunluk istemcisidir] (https://bitcoincore.org/). Blockchain'yi indirir, doğrular ve bakımını yapar, RPC/REST API'leri sağlar ve bir Wallet entegre edebilir. Standart araçları tercih ediyorsanız ve kendiniz hizmet ekleme konusunda rahat hissediyorsanız (Electrum sunucusu, explorer ve LND gibi), Core'u olduğu gibi kullanmanız daha iyi olacaktır.



**Faydaları:** Maksimum kararlılık, öngörülebilir davranış, ham deneyim, kurulumu ve yapılandırması kolay.



**Dezavantajları:** Sadece bir Bitcoin düğümü yerine eksiksiz bir uygulama ortamı oluşturmak için yığının geri kalanını manuel olarak oluşturmanız gerekir.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (ana alternatif müşteri)



[Bitcoin Knots, Bitcoin core'ün bir Fork'sidir](https://bitcoinknots.org/), Luke Dashjr tarafından sürdürülmektedir. Bitcoin protokolünü uygulamak için Core'a alternatif ana istemcidir. Ağın geri kalanıyla tamamen uyumludur (hiçbir şekilde Bitcoin Cash gibi bir Hard Fork değildir), yine de Core'da bulunmayan veya bazılarının spam olarak kabul ettiği şeyleri sınırlamak için varsayılan olarak daha katı bir şekilde uygulanan röle politikası seçenekleri de dahil olmak üzere ek özellikler sunar.



Core yerine Knots'u seçmenin 2 olası nedeni vardır:




- Teknikler**: Düğümünüz tarafından hangi işlemlerin kabul edileceğini ve yayınlanacağını belirleyerek, özellikle röle yönetimi açısından Core'dan farklı seçenekler.
- Politika**: Bazı insanlar Knots gibi alternatif istemcileri teknik olmayan nedenlerle, özellikle de Core'a bir alternatifi desteklemek ve böylece onun tekelini azaltmak için kullanmayı tercih etmektedir. Eğer Core tehlikeye girerse, sadece sağlam, iyi bakımlı alternatif istemcilere sahip olmak değil, aynı zamanda bunları etkili bir şekilde nasıl kullanacaklarını bilmek de yararlı olacaktır. Diğerleri Knots'u protesto amacıyla kullanmaktadır, çünkü Core'un geliştiricilerine olan güvenlerini kaybetmişlerdir ya da istemci yönetiminin çoğunluğunu onaylamamaktadırlar.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Şahsen, güvenlik yamalarından daha hızlı yararlanmak için Core'u seçmenizi tavsiye ederim. Gerçekten de Knots'ta keşfedilen bazı güvenlik açıkları gecikmeli olarak düzeltilmektedir. Daha genel olarak, Core'un geliştirme süreci sağlam bir şekilde yapılandırılmış ve çok sayıda katılımcı tarafından desteklenirken, Knots tek bir kişi tarafından sürdürülüyor ve çok daha küçük bir topluluğa sahip. Öte yandan, röle kuralları, özellikle ağın sadece küçük bir kısmı tarafından uygulandığında (percolation teorisi gibi) günümüzde kullanışlılıklarını kaybetme eğilimindedir.



### Node-in-a-box dağıtımları



Kutudaki _node_, Bitcoin core'i (veya Knots'u) önceden yapılandırılmış bir işletim sistemi, bir Interface Web ve kendi kendini barındıran hizmetlerden oluşan bir Uygulama Mağazası (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, vb.) Tek bir tıklamayla bu farklı modülleri kurabilir, güncelleyebilir ve birbirine bağlayabilirsiniz.



Günlük olarak çok sayıda yardımcı uygulamayı başlatmak ve yönetmek için çok daha basit bir çözümdür. Dezavantajı ise bir sorun oluştuğunda (örneğin Docker imaj çakışması, hatalı güncelleme, bozuk veritabanı) dağıtımın kendi entegrasyonuna bağlı olduğunuz için hata ayıklamanın çok karmaşık hale gelebilmesidir. Dahası, topluluk veya resmi destek genellikle karmaşıktır.



Dolayısıyla, her şey düzgün çalıştığı sürece kutudaki bir düğümün kullanımı son derece kolaydır, ancak bir hata durumunda, uzun aramalar yapmaya, yardım beklemeye ve ellerinizi kirletmeye hazır olmalısınız.



Bu çözümlerin çoğu iki formatta mevcuttur:




- Önceden monte edilmiş makine: işletim sistemi önceden yüklenmiş eksiksiz bir bilgisayar. Bu kullandıkça öde makinelerin çalışır hale gelmesi için şebekeye takılması ve internete bağlanması yeterlidir. Bütçeniz izin veriyorsa, bu seçenek kurulumu çok basit olma, genellikle öncelikli destek sunma ve bu şirketlerin iş modeli genellikle donanım satışına dayandığından, geliştirme finansmanına katkıda bulunma avantajına sahiptir.
- Kendin Yap: Dağıtım işletim sistemini kendi makinenize kurun (eski PC, NUC, Raspberry Pi, ev sunucusu...). Bu, eski bir makineyi geri dönüştürebileceğiniz veya ihtiyaçlarınıza ve bütçenize tam olarak uyan donanımı seçebileceğiniz için en ekonomik çözümdür. Aynı zamanda en esnek ve yapılandırması en tatmin edici seçenektir. Kursun pratik bölümünde bu yaklaşımı inceleyeceğiz.



İşte (2025 yılında) mevcut ana kutu içinde düğüm çözümlerine genel bir bakış:



### Umbrel (umbrelOS & Umbrel Home)



[Bugün Umbrel, kutu içinde düğüm çözümlerinde lider konumdadır (https://umbrel.com/). Başarısı büyük ölçüde kurulumunun basitliği (basit bir Raspberry Pi üzerinde başlatıldığında), zarif ve sezgisel Interface ve hızla büyüyen ve şu anda son derece kapsamlı olan bir uygulama ekosisteminden kaynaklanmaktadır.



![Image](assets/fr/067.webp)



2020 yılında birkaç yardımcı uygulamanın eşlik ettiği basit bir Bitcoin düğümü olarak piyasaya sürülen Umbrel, kademeli olarak tam özellikli, modern bir ev bulutuna dönüştü.



Nasıl çalıştığı ve belirli özellikleri hakkında burada daha fazla ayrıntıya girmeyeceğim, çünkü bunları bir sonraki bölümün ilk bölümünde daha derinlemesine inceleyeceğiz. Aslında, bu BTC 202 kursunun amaçları doğrultusunda, yeni başlayanlar ve orta düzey kullanıcılar için mevcut en iyi node-in-a-box çözümü olduğuna inandığım UmbrelOS'u kullanmayı seçtim.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9, "egemen bilişim" için tasarlanmış bir sistem olan StartOS'u (https://start9.com/) sunuyor: amaç, herkesin kendi özel sunucusuna sahip olması ve yönetmesi, kendi kendine barındırılan uygulamalardan oluşan bir pazarla geliştirilmesidir. Bir Start9 sunucusu satın alabilir (Server One 619 $, Server Pure 899 $) ya da kendi makinenizde DIY modunda kendi sunucunuzu kurabilirsiniz.



Bitcoin tarafında, StartOS bir Full node, bir Lightning düğümü, BTCPay Sunucusu, Electrs ve diğer birçok hizmeti kurmanıza izin verir. Bununla birlikte, Start9'un cazibesi bunun ötesine uzanıyor: çeşitli yazılımları (dosya bulutu, mesajlaşma, izleme) tam kontrol ile birleşik bir şekilde keşfetme, yapılandırma ve açığa çıkarma imkanı sunuyor. Bu nedenle proje, sadece basit bir Bitcoin düğümü değil, sağlam bir kendi kendine barındırma platformu isteyen kullanıcıları hedefliyor. Muhtemelen Umbrel'den sonraki en eksiksiz ekosistemdir.



![Image](assets/fr/068.webp)



Umbrel ile arasındaki temel fark Interface'te yatıyor. Umbrel son derece cilalı bir kullanıcı arayüzüne dayanırken, Start9 daha kaba, daha işlevsel bir Interface sunuyor. Start9'un uygulama ekosistemi Umbrel'inkinden daha az zengindir, ancak bunu çeşitli teknik avantajlarla telafi eder: gelişmiş uygulama ayarlarına erişim basitleştirilmiştir, oysa Umbrel, istenen seçenek Interface tarafından sağlanmadığında hızla kısıtlayıcı hale gelir. Start9 ayrıca yedekleme yönetiminde de üstündür: Umbrel'in LND için etkili çözümü dışında, Start9'un aksine birleşik bir mekanizma yoktur. Dahası, daha erişilebilir izleme araçları ve şifreli bir uzak bağlantı (`https`) sunarken, Umbrel'e yerel erişim `http` üzerinden gerçekleşiyor.



Kısacası, Umbrel'in çok zengin ekosistemine özel bir ilgi duymadan sadece Bitcoin için temel uygulamalara ihtiyacınız varsa ve Interface kullanıcısı bir öncelik değilse, Start9 daha iyi bir seçenektir. Aksi takdirde, Umbrel daha iyi bir seçimdir.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode, yalnızca Bitcoin ve Lightning'e odaklanan bir dağıtımdır] (https://mynodebtc.com/), bir web Interface, bir uygulama pazarı ve tek tıklamayla yükseltmeler sunar. Kullanıma hazır donanım satın alabilir (*Model Two* 549 dolardan satılmaktadır) ya da MyNode'u kendi makinenize ücretsiz olarak kurabilirsiniz. Proje ayrıca yazılımın öncelikli destek ve gelişmiş özellikler içeren bir *Premium* sürümünü (94 $) sunmaktadır.



![Image](assets/fr/069.webp)



Pratikte MyNode, bir Full node'i çalıştırmak için gereken tüm temel yapı taşlarının yanı sıra Bitcoin kullanıcıları için gerekli uygulamaları bir araya getirir. Bu nedenle, Start9 ve Umbrel sistemlerinde bulunan kendi kendine barındırılan uygulamalar gibi Bitcoin ekosistemi dışındaki uygulamalara ihtiyaç duymuyorsanız uygun bir çözümdür.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz, Raspberry Pi'ye bir Bitcoin düğümü ve bir Lightning düğümü monte etmek için %100 açık kaynaklı bir projedir](https://docs.raspiblitz.org/) (MIT lisansı). Basitçe görüntüyü indirin, başlatın ve Raspberry Pi'nizde çalışan bir node-in-a-box'a sahip olmak için sihirbazı takip edin. Önceden monte edilmiş kitler, donanıma bağlı olarak genellikle 300 ila 400 dolar arasında üçüncü taraflardan da temin edilebilir. RaspiBlitz ayrıca bir dizi ek, kurulumu kolay uygulama da sunmaktadır.



![Image](assets/fr/070.webp)



Bir Raspberry Pi'niz varsa, Umbrel gibi daha eksiksiz sistemler bu tür mini PC'ler için giderek daha ağır hale geldiğinden, bu mükemmel bir seçenektir.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo, Samurai Dojo ve Whirlpool'in dağıtımını otomatikleştiren, özel bir Interface ve Samurai ekosistemi için özel olarak tasarlanmış eklentilere sahip, gizlilik odaklı bir kutu içinde düğümdür](https://wiki.ronindojo.io/en/home).



Prensip basit: Ashigaru Wallet (geliştiricilerinin tutuklanmasının ardından Samurai Wallet'nın Fork halefi) kullanıyorsanız veya gelişmiş gizlilik araçlarından yararlanmak istiyorsanız, RoninDojo tam size göre.



![Image](assets/fr/071.webp)



Proje daha önce Tanto adında önceden yapılandırılmış bir makine sunuyordu, ancak bu şu anda mevcut değil. Daha sonraki bir tarihte geri dönebilir. Bu arada, RoninDojo'yu bir Rock5B + veya Rockpro64'e veya hatta dolaylı olarak bir Raspberry Pi'ye kolayca kurmak mümkündür.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Bir başka [node-in-a-box çözümü de Nodl](https://www.nodl.eu/). Önceki projelerde olduğu gibi, önceden yapılandırılmış donanımı satın alabilir (modele bağlı olarak €599 ile €799 arasında) veya DIY modunda kendiniz kurabilirsiniz.



Yazılım tarafında Nodl, Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL'nin yanı sıra BTC RPC Explorer'ı entegre bir güncelleme zinciri ve MIT lisansı altında açık kaynak koduyla entegre ediyor.



![Image](assets/fr/072.webp)



Çeşitli yazılım çözümlerini inceledikten sonra, şimdi sıra node'unuzu barındıracak makineyi seçmeye geldi!




## Donanım çözümlerine genel bakış


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Tüm yazılım olanaklarını incelediğimize göre şimdi de node'unuz için gereken donanıma odaklanalım. Size bileşenlerinizi seçme konusunda bazı somut tavsiyelerin yanı sıra farklı bütçelere uygun yapılandırmalar sunacağım. Elbette bu benim kişisel görüşüm ve geribildirimim: burada sunulanlara ek olarak kesinlikle başka ilgili alternatifler de var. Ayrıca, bir önceki bölümde zaten ele aldığımız, node-in-a-box projeleri tarafından sunulan önceden monte edilmiş makineleri tekrar ziyaret etmeyeceğim. Burada yalnızca kendin yap çözümlerine odaklanacağız.



### Gerçekten özel bir makineye ihtiyacınız var mı?



Geçtiğimiz birkaç yıl içinde, bitcoin kullanıcıları, özellikle 2020'lerin başında node-in-a-box'ın popülerleşmesiyle birlikte yaygın bir yanlış anlamanın giderek daha fazla farkına vardı: bir Bitcoin node'u mutlaka yalnızca bu amaca adanmış bir makinede çalışmalıdır. Ancak bu doğru değildir. Bir Bitcoin düğümünü çalıştırmak için mutlaka özel bir bilgisayara ihtiyacınız yoktur: Bitcoin core günlük bilgisayarınızda mükemmel bir şekilde çalışabilir. Blockchain için yeterli disk alanınız varsa veya budamayı etkinleştirirseniz, zinciri doğrulayabilir, Wallet'inizi bağlayabilir ve hatta kullanmayı bitirdiğinizde programı kapatabilirsiniz. Bu yaklaşımın avantajı oldukça büyüktür: sıfır ilk yatırım ve minimum karmaşıklık.



![Image](assets/fr/074.webp)



Bununla birlikte, özel bir makine kullanmak genellikle daha rahattır. Sürekli (7/24) çalışabilir, her zaman uzaktan erişilebilir, ana makinenizin kaynaklarını tekelleştirmez ve her şeyden önce kullanımları izole eder (iyi bir güvenlik uygulaması: kişisel bilgisayarınız bir sorunla karşılaşırsa, düğümünüz çalışmaya devam eder ve bunun tersi de geçerlidir). Yani soru "Bir makine tahsis etmem gerekiyor mu?" değil, daha ziyade "Sürekli çevrimiçi olan, diğer cihazlar tarafından erişilebilen ve gelişebilen bir düğüme ihtiyacım var mı?" (Lightning, indeksleyiciler, ek uygulamalar...). Yanıt evet ise, ayrı bir makine tercih etmek işleri çok daha basit hale getirecektir.



### 3 edinim yöntemi: geri dönüşüm, ikinci el ve yeni



#### Eski bir bilgisayarın geri dönüşümü



Bu en ekonomik çözümdür. Çoğumuzun evinde ya da arkadaşlarında veya ailesinde Dust toplayan eski bir bilgisayar vardır: bu, onu tekrar hizmete sokmak için mükemmel bir fırsattır! Bitcoin düğümü olarak kullanıma uyarlamak için 2 TB SSD eklemeniz ve ihtiyaçlarınıza bağlı olarak RAM'i artırmak için RAM çubuklarını değiştirmeniz veya eklemeniz yeterlidir. Tamamen işlevsel bir makine için 100 ila 200 € arasında bir ödeme yapmayı bekleyin.



Herhangi bir donanım satın almadan önce, mevcut disk yuvalarının sayısını, bağlantı türünü (M.2 veya SATA), RAM biçimini (SODIMM veya DIMM) ve neslini (DDR4, vb.) kontrol edin. Optimum performans sağlamak için makineyi, özellikle de fanı temizleme fırsatını da değerlendirmelisiniz.



Ancak bir dizüstü bilgisayar kullanıyorsanız dikkatli olun: pil zamanla sorun yaratabilir (bu konuda daha fazla bilgi bölümün ilerleyen kısımlarında yer almaktadır).



#### Yenilenmiş veya kullanılmış



Pazar, *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* veya *Dell OptiPlex Micro* gibi yenilenmiş iş amaçlı mini PC'lerle doludur. Bu makineler sağlam, kompakt, sessiz ve enerji tasarrufludur. Fiyatları yeninin çok altındadır ve 6. ila 10. nesil i5/i7 işlemciler ve 8 ila 16 GB RAM ile donatılmış modelleri, yapılandırmaya bağlı olarak genellikle 70 ila 200 € arasında çok cazip fiyatlara bulmak kolaydır. Bana göre, Bitcoin düğümünüz için özel bir makine arıyorsanız, bu muhtemelen en iyi seçenektir.



![Image](assets/fr/075.webp)



Birkaç yıl öncesine ait, ilginç konfigürasyonlara sahip ve paranızın karşılığını fazlasıyla veren kullanılmış bilgisayarlar ve dizüstü bilgisayarlar bulmak da mümkün.



**Not:** *ThinkCentre Tiny* gibi kurumsal filolardaki makinelerde genellikle ekran için yalnızca bir *DisplayPort* (DP) bağlantı noktası bulunur, HDMI çıkışı yoktur. Bu nedenle, ihtiyacınız varsa bir adaptör veya DP-HDMI kablosu getirmeyi unutmayın.



#### Yeni satın alma



Bütçeniz elveriyorsa yeni bir makine de tercih edebilirsiniz. Özellikle kendi kendine barındırma için Umbrel veya Start9'u Bitcoin ekosistemi dışındaki ek uygulamalarla birlikte kullanmayı planlıyorsanız, iyi performansa sahip yeni bir donanıma sahip olmak istiyorsanız bu iyi bir seçenektir.



### Ne tür bir makine seçmeliyim?



#### Mini-PC "NUC" / barebone



Mini PC'ler, bence evde bir Bitcoin düğümü barındırmak için en iyi uzlaşmayı sunuyor. Yer tasarrufu sağlar, rafa kolayca sığar, minimum güç tüketir ve RAM ekleme ya da SSD değiştirme gibi kolay donanım değişikliklerine uygundur.



Şahsen ben ikinci el piyasasında (kurumsal filolardan) çok yaygın olan *Lenovo ThinkCentre Tiny* tercih ediyorum; özellikle sağlam ve modifiye edilmesi kolay. Elbette diğer üreticilerin de pek çok muadili var: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*.



![Image](assets/fr/001.webp)



**Öne çıkan özellikler:** az yer kaplaması, orta düzeyde güç tüketimi, düşük gürültü, ölçeklenebilirlik (modele bağlı olarak) ve güvenilirlik.



**Zayıf yönleri:** Raspberry Pi-tipi bir SBC'den biraz daha pahalı, dahili ekran yok (uzaktan erişim veya harici monitör aracılığıyla), pil yok (elektrik kesintisi durumunda ani kapanma).



#### Özel dizüstü bilgisayar



Mini PC'ye mükemmel bir düşük maliyetli alternatiftir: bugün, iyi işlemciler, çok sayıda bağlantı noktası ve entegre bir ekran ve klavye (ilk kurulum için çok pratik) ile donatılmış, düşük fiyatlarla kullanılmış veya hatta yeni dizüstü bilgisayarlar bulabilirsiniz. Hepsinden önemlisi, batarya doğal bir UPS görevi görür: elektrik kesintisi durumunda düğüm aniden kapanmaz ve hatta birkaç saat boyunca çalışmaya devam edebilir.



![Image](assets/fr/076.webp)



**Öne çıkan özellikler:** Hepsi bir arada çözüm, batarya UPS görevi görür (kesinti olmaz), entegre ekran ve klavye sayesinde basitleştirilmiş kurulum, entegre Wi-Fi kartı ve çok çeşitli ikinci el ve yeni pazarlar (bu da genellikle fiyat pazarlığı yapabileceğiniz anlamına gelir).



**Zayıf yönleri:** çıplak bir Mini-PC'den biraz daha yüksek güç tüketimi, 7/24 çalışmada kapasite kaybıyla birlikte kademeli pil aşınması, nadir de olsa pilin şişmesi veya yaşla birlikte termal kaçak riski. Mini-PC'yi dizüstü bilgisayardan daha iyi bir seçenek olarak görmeme neden olan şey esasen bu yönü: pilin kademeli olarak bozulması ve buna bağlı riskler.



Bu çözümü seçerseniz, herhangi bir tehlikeyi önlemek için akünün durumunu yakından takip etmenizi öneririm. Aşırı ısı, olağandışı kokular, dengesizlik veya deforme olmuş bir kabuk olup olmadığına dikkat edin. Bir alarm durumunda, bilgisayarı derhal kapatın ve fişini çekin, ardından pili özel bir geri dönüşüm tesisinde imha edin.



**İpucu:** BIOS/UEFI veya üreticinin aracı izin veriyorsa, pil ömrünü uzatmak için bir yük sınırı (örn. %60 veya %80) belirleyin.



#### Raspberry Pi ve diğer SBC'ler: yanlış fikir



2020'lerin başında, kutu içinde düğüm yazılımının yükselişiyle birlikte, Raspberry Pi çılgınlığı da bir Bitcoin düğümünü çalıştırmak için bir araç olarak ortaya çıktı. Fikir cazip görünüyordu: ucuz, kompakt ve erişilebilir.



![Image](assets/fr/073.webp)



Pratikte, amacınız yalnızca ek uygulamalar olmadan bir Bitcoin düğümü çalıştırmaksa, bir Raspberry Pi yeterli olabilir. Ancak Umbrel, Start9 veya daha zengin bir ekosistem (Block explorer, Address indeksleyici, Lightning düğümü, kendi kendini barındıran uygulamalar...) kullanmak istediğiniz anda, makine hızla sınırlarına ulaşır.



Raspberry Pi'nin bir dizi dezavantajı vardır:




- bazen belirli yazılımlarla uyumsuz olan veya daha fazla işlem gerektiren bir ARM mimarisine sahip çok ince işlemciler;
- Lehimli RAM, yükseltilmesi imkansız, sınırlı konfigürasyonlarla (genellikle maksimum 8 GB);
- kablo ile bağlanan SSD'ler için harici kutular, sık sık hata kaynakları, kararlı bir SSD için özel bir kart satın alınmasını gerektirir;
- çabuk ısınma eğilimi ve doğru soğutma sağlamada zorluk;
- ek donanım (kasa, fan, SSD kartı vb.) satın almanız gerekir;
- çok sınırlı bağlantı.



Geçmişte Raspberry Pi gibi SBC'lerin en büyük avantajı fiyatıydı: birkaç düzine Euro'ya özel bir makine alabiliyordunuz. Ancak günümüzde fiyatlar hızla yükseldi ve gerekli tüm ek donanımları eklediğinizde maliyet, bence çok daha fazla avantaj sunan ilk kullanılmış ya da yenilenmiş x86 mini PC'lere yaklaşıyor. Bu nedenle bir SBC tercih etmenizi önermiyorum.



### Bileşenlerin seçilmesi



#### Disk depolama alanı: SSD zorunlu, minimum 2 TB



Teknik olarak, bir HDD üzerinde bir Bitcoin düğümü çalıştırmak mümkündür. Sorun, her şeyin, özellikle de Bitcoin core'in diski önbellek olarak yoğun bir şekilde kullanması nedeniyle (özellikle UTXO seti için) aşırı derecede uzun olacak olan IBD'nin önemli ölçüde yavaşlamasıdır. Bu nedenle HDD kullanılmamasını şiddetle tavsiye ediyorum: gerçek bir darboğaz yaratır, gelecekteki gelişimi ciddi şekilde sınırlar (örneğin, bir Lightning düğümü için) ve hatta Blockchain kafasıyla bir senkronizasyon uyumsuzluğuna yol açabilir. Dahası, mekanik disk üzerindeki sürekli stres erken aşınma riskini artırır.



SSD'ler kullanıcı deneyiminizi kökten değiştirir: her şey daha hızlı, daha sorunsuz ve çok daha güvenilir hale gelir. Bu nedenle düğümünüz için bir SSD kullanımı (neredeyse) zorunludur ve özellikle yüksek kapasiteli modeller artık nispeten uygun fiyatlı olduğu için pişman olmayacaksınız.



![Image](assets/fr/077.webp)



Kapasite açısından, 2 TB yavaş yavaş yeni makul minimum olarak kendini kabul ettirmektedir. 2025 yazında, Blockchain şimdiden 700 GB'a yaklaşıyor ve Umbrel, bir Address indeksleyici ve birkaç uygulama eklerseniz, 1 TB SSD hızla doyacaktır. 2 TB ile gelecek yıllar için rahat bir marja sahip olursunuz (geniş bir tahminle 5 ila 15 yıl arasında). Umbrel'de çok sayıda uygulama kullanmayı, büyük dosyaları kendi kendine barındırmada depolamayı planlıyorsanız veya disk alanı ihtiyaçlarınızı büyük ölçüde tahmin etmek istiyorsanız 4 TB'ı da tercih edebilirsiniz.



![Image](assets/fr/078.webp)



Formata gelince, bu makinenizde bulunan bağlantı noktalarına bağlı olacaktır; ancak mümkünse bir NVMe M.2 SSD kullanmanızı öneririm.



#### Bellek (RAM): 8 ila 16 GB



Yalnızca Bitcoin core için (Umbrel kaplaması olmadan), geliştirici önerileri, ayarlar en düşük ayara ayarlandığında en az 256 MB RAM, varsayılan ayarlarla 512 MB ve normal kullanım için 1 GB olduğunu göstermektedir.



Öte yandan, Umbrel veya Start9 gibi bir kutu içinde düğüm sistemi kullanıyorsanız, RAM gereksinimleri önemli ölçüde daha yüksektir. Umbrel geliştiricileri en az 4 GB RAM önermektedir. Bu yalnızca Core'u çalıştırmak için yeterli olabilir, ancak kısa süre sonra sınırlanacaksınız. Bu nedenle 8 GB öneriyorlar ki ben de Bitcoin (Core, LND, indeksleyici ve birkaç uygulama) civarında temel bir yapılandırma için minimum olduğunu düşünüyorum. Benim deneyimlerime göre, Umbrel ve birkaç ek hizmetle 8 GB hala biraz dar. Gerçekten rahat olmak ve biraz marj elde etmek için 16 GB RAM öneririm.



#### İşlemci (CPU)



Bir Umbrel düğümü için minimum gereksinim Intel veya AMD'den çift çekirdekli 64 bit işlemcidir. Bitcoin core'e ek olarak birkaç uygulama kullanmak istiyorsanız, dört çekirdekli (veya daha yüksek) bir işlemci akışkanlık açısından gerçek bir fark yaratacaktır. Örneğin, 6. ila 10. nesil i5/i7 işlemciler ikinci el piyasasında mükemmel seçeneklerdir.



### Somut konfigürasyon örnekleri



Aşağıda, farklı bütçelere ve ihtiyaçlara uyarlanmış üç somut konfigürasyon ve bunları destekleyecek kesin modeller öneriyorum. Bu seçenekler, bu bölümdeki bilgileri açıklamak için örnek olarak sunulmuştur; tam olarak bu modelleri seçme zorunluluğunuz yoktur. Mini-PC'nin uzun vadede en iyi seçenek olduğunu düşündüğüm için, önerilen üç konfigürasyon için bu formata güveneceğim.



*Aşağıda gösterilen fiyatlar yalnızca gösterge niteliğindedir ve bölgeye, satıcıya ve döneme göre değişiklik gösterebilir*



Her şeyden önce, Blockchain'i barındıracak kadar büyük ve aynı zamanda manevra alanı bırakan bir SSD'ye ihtiyacınız vardır. SSD'lerin yazma döngüleri ve yazılan toplam veri hacmi açısından sınırlı bir ömrü vardır. Ancak bir Bitcoin düğümü, yazma sırasında diske önemli bir yük bindirir. Bu nedenle giriş seviyesi modelleri önermiyorum; bunun yerine çok daha iyi performans sunan bir NVMe SSD öneriyorum.



Örnek olarak, bu dersin amaçları doğrultusunda aşağıdaki modeli seçtim: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, Amazon'da yaklaşık 120 €'ya satılmaktadır. Crucial, Western Digital ya da Kingston gibi diğer tanınmış markaları da tercih edebilirsiniz.



![Image](assets/fr/046.webp)



#### Düşük bütçeli yapılandırma



Açıkçası, bütçeniz çok kısıtlıysa (200 €'nun altında), özel bir makineye yatırım yapmamanızı, bunun yerine Bitcoin core'yi doğrudan günlük bilgisayarınıza kurmanızı tavsiye ederim (disk alanınız yetersizse pruned modunda).



Aksi takdirde, giriş seviyesi bir bütçe için *HP EliteDesk 800 G2 Mini'yi* öneririm. Amazon'da 6. nesil Intel Core i5 işlemci ve 8 GB RAM ile donatılmış yenilenmiş bir modeli 96 €'ya buldum. Bu, yeni başlayanlar için özellikle ilginç bir seçenek: Bu işlemci ve bu miktarda bellek, Core'a çok fazla önbellek ayırmamanız koşuluyla, Umbrel'de Core'un yanı sıra Electrs indeksleyici, Lightning düğümü ve Mempool örneği gibi birkaç uygulamayı aynı anda çalıştırmak için fazlasıyla yeterli. Dahası, bu tür bir mini PC, örneğin ihtiyaç duyulması halinde RAM'i 16 GB'a yükseltmeyi kolaylaştırır (bir veya iki kaliteli bellek çubuğu için yaklaşık 30-40 € ekstra ödeme yapmayı bekleyin).



![Image](assets/fr/045.webp)



Daha sonra SSD'yi bütçeye eklemeniz yeterlidir. Samsung 2TB ile 120 €'dan başlarsak, eksiksiz ve işlevsel bir makine için toplam 216 €'luk bir maliyet elde ederiz.



#### Orta bütçeli yapılandırma



Node'unuzu barındıracak makine için ortalama 300 € civarında bir bütçeniz varsa, örneğin yüksek performanslı bir işlemci ve yeterli RAM ile donatılmış bir *Lenovo ThinkCentre Tiny* öneririm. Amazon'da 180€'ya 6. nesil Intel Core i7 işlemci ve 16GB RAM içeren yenilenmiş bir model buldum. 120€'luk 2TB SSD de eklendiğinde toplam maliyet 300€'ya geliyor.



![Image](assets/fr/044.webp)



Bu makine ile rahat bir konfigürasyona sahip olursunuz: hızlı bir IBD ve Umbrel veya Start9'unuzda çok sayıda uygulamayı zorlanmadan çalıştırma yeteneği. Bu BTC 202 kursu için kullandığım konfigürasyon tam olarak bu.



#### Üst düzey yapılandırma



Daha büyük bir bütçeyle, olasılıklar önemli ölçüde genişler. Bir DIY yapılandırması seçebilir veya hatta doğrudan bir node-in-a-box projesi tarafından sunulan önceden monte edilmiş bir makineyi tercih edebilirsiniz.



Örneğin, *ASUS NUC 14 Pro* Amazon'dan 540 €'ya yeni olarak temin edilebilir. Bu fiyata, 16 GB DDR5 RAM ile birlikte Intel Core Ultra 5 işlemci (yeni ve özellikle yüksek performanslı) elde edersiniz. Böyle bir yapılandırma ile bir IBD'yi rekor sürede tamamlayabilir ve zorlu uygulamaları zorlanmadan yükleyebilirsiniz.



Bu son derece rahat bir yapılandırmadır, hatta ilk hedef sadece bir Bitcoin düğümü çalıştırmaksa aşırıya kaçabilir. Öte yandan, Umbrel ve Start9'da bulunan tüm kendi kendini barındıran uygulamalardan tam olarak yararlanmak istiyorsanız, bu güç seviyesi tam size göre.



![Image](assets/fr/043.webp)



Kullanım amacınıza bağlı olarak, diğer konfigürasyonlarda olduğu gibi 2TB SSD'yi ya da kişisel dosyalarınızı da depolamak ve kendi kendine barındırma kullanımlarınızı genişletmek istiyorsanız doğrudan 260 € karşılığında 4TB SSD'yi tercih edebilirsiniz. 2TB SSD ile yapılandırmanın toplam maliyeti 660 € iken, 4TB SSD ile 800 €'ya ulaşmaktadır.



### Birkaç ipucu daha





- İkinci el ekipman satın almak ve bitcoin ile ödeme yapmak istiyorsanız, yakınınızdaki bir buluşmaya gelin! Diğer katılımcılarla sohbet ederek, Bitcoin etrafındaki döngüsel ekonomiyi canlı tutmaya yardımcı olurken, iyi bir fiyata uygun ekipman bulacağınızdan emin olabilirsiniz. Bu aynı zamanda topluluğun sağlam tavsiyelerinden yararlanmak için de bir fırsattır.





- İnternet bağlantısı için, en azından sistem kurulumu için elbette bir RJ45 Ethernet kablosuna ihtiyacınız olacaktır.





- Umbrel gibi bazı ortamlar daha sonra Wi-Fi kullanmanıza izin verir, ancak performans genellikle daha düşük olacaktır (özellikle Lightning düğümünüzü uzaktan kullanmak istiyorsanız, bunun bir etkisi olabilir). Wi-Fi'yi seçerseniz, makinenizde yerleşik bir kart olduğundan emin olun veya uyumlu bir dongle ekleyin.





- Makineniz için her zaman orijinal üreticinin Supply gücünü kullanın. Bu, ekipmanınızın zarar görmesini ve yangın çıkma riskini önlemek için çok önemlidir.





- Makinenizin dahili bir aküsü yoksa, ani kapanmaları önlemek için bir invertöre yatırım yapmak iyi bir fikirdir.





- Ekipmanınızın değerine ve coğrafi konumunuza bağlı olarak, doğrudan santralde veya kullanılan güç şeridinde bir yıldırım önleyici sistem de uygun olabilir.





- Son olarak, makinenizin soğutmasını optimize etmeyi unutmayın: düzenli olarak temizleyin ve aşırı ısınmayı önlemek için serin, iyi havalandırılan, düzenli bir yere kurun, bu da throttling'e (işlemcinizin hızının gönüllü olarak sınırlandırılması) yol açabilir.



# Bir Bitcoin düğümünü kolayca kurma


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: bir Bitcoin düğümünden çok daha fazlası


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel, kendi kendini barındırmayı erişilebilir kılmak için tasarlanmış kişisel bir sunucu işletim sistemidir: Umbrel'i kurar, `umbrel.local` üzerinde bir tarayıcı açar ve her şeyi basit bir uzak Interface aracılığıyla yönetirsiniz.



Proje ilk olarak tek tıklamayla Bitcoin ve Lightning düğümü fikrini popülerleştirdi, ardından gerçek bir "ev bulutuna" dönüştü: dosya ve fotoğraf depolama, multimedya akışı, ağ araçları, ev otomasyonu, yerel yapay zeka ve entegre bir App Store'dan yüklenebilen yüzlerce uygulama.



Umbrel'de her uygulama bir Docker konteynerinde çalışır (izolasyon, atomik güncellemeler, bağımsız başlatma/durdurma). Interface, tüm bu uygulamalara erişimi merkezileştirerek tek oturum açma (isteğe bağlı 2FA ile), işletim sistemi ve uygulamalar için tek tıklamayla güncelleme, makinenin canlı izlenmesi (CPU, RAM, sıcaklık, depolama), uygulamalar arasında izin yönetimi ve tüketimlerine genel bir bakış sunar.



Bu nedenle Umbrel'in amacı, sadece bir Bitcoin düğümünü çalıştırmanın ötesinde, bulut hizmetlerine güvenmeden verileriniz üzerindeki kontrolü ve gizliliği size geri vermektir.



### Umbrel Home vs umbrelOS



Umbrel iki farklı yaklaşım sunmaktadır:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): umbrelOS için özel olarak tasarlanmış ve optimize edilmiş, kullanıma hazır bir mini sunucudur. Kompakt, sessiz, Ethernet bağlantılı, bir NVMe SSD (isteğe bağlı 4 TB'a kadar), 16GB RAM ve dört çekirdekli bir CPU ile donatılmıştır. Sipariş ediyorsunuz, fişe takıyorsunuz ve `umbrel.local` adresine gidiyorsunuz. Dakikalar içinde çalışır durumda bir Umbrel'e sahip olabilirsiniz. Bu tak ve çalıştır seçeneği.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): Bu, kendi donanımınıza (mini-PC, NUC, kule, özel dizüstü bilgisayar...) yükleyebileceğiniz işletim sistemidir. Umbrel Home'da olduğu gibi aynı Interface ve aynı Uygulama Mağazasına sahipsiniz.



![Image](assets/fr/080.webp)



Her iki durumda da kullanıcı deneyimi yazılım tarafında aynıdır: tarayıcı tabanlı yönetim, tek tıklamayla güncellemeler, isteğe bağlı uygulama kurulumu... Kendin Yap çözümü genellikle bir Umbrel Home satın almaktan daha ekonomiktir (kullanılan makineye bağlı olarak). Bununla birlikte, iş modeli donanım satışına dayandığı için **Umbrel Home satın almak doğrudan projenin gelişimini finanse etmeye katkıda bulunduğundan** her zaman DIY seçeneğini tercih etmenizi tavsiye etmem. Ve açıkçası, 2 TB depolama alanı için 389 € olan fiyat, sunulan makinenin kalitesi göz önüne alındığında çok makul kalıyor.



![Image](assets/fr/079.webp)



Bir sonraki bölümde, umbrelOS DIY'i kendi makinenize nasıl kuracağınızı inceleyeceğiz. Ancak, Umbrel Home'u tercih ettiyseniz bu BTC 202 kursunu da aynı şekilde takip edebilirsiniz.



### Kullanım örneği: Bitcoin düğümünden ana buluta



Umbrel, ihtiyaçlarınıza bağlı olarak çok minimalist kalabilir ve yalnızca Bitcoin'e odaklanabilir veya gerçek bir çok işlevli kişisel sunucuya dönüşebilir. İşte Umbrel'in ana kullanım alanları:





- Basit Bitcoin düğümü**: Bu, Umbrel'in en başından beri dayandığı temel kullanımdır. Bitcoin core (veya Knots) çalıştırabilir, cüzdanlarınızı doğrudan düğümünüze bağlayabilir, bir Electrum sunucusunu açığa çıkarabilir, Blockchain'ü görüntülemek için Mempool Block explorer'nizi barındırabilir ve ücretleri tahmin edebilirsiniz... Bu kursta bu kullanımlara odaklanacağız.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel ayrıca kendi Lightning düğümünüzü yönetmek için Lightning Network'nin iki uygulaması olan LND veya Core Lightning'i dağıtmanıza olanak tanır. Mevcut birçok uygulama sayesinde kanallar açabilecek, likiditenizi yönetebilecek, ödemeler yapabilecek, dengelemeyi otomatikleştirebilecek, hizmetler sunabilecek, uzak bir Wallet'a bağlanabilecek veya gelişmiş Interface yönetiminden yararlanabileceksiniz. Bir sonraki LNP 202 kursumuzda bu özel kullanım durumunu inceleyeceğiz.



![Image](assets/fr/083.webp)





- Genel self-hosting**: Nextcloud, Immich, Jellyfin/Plex, DNS çapında reklam engelleyiciler (Pi-hole/AdGuard), VPN'ler (WireGuard, Tailscale), ev otomasyonu (Home Assistant), yedeklemeler, not yönetimi, ofis araçları, yerel AI (Ollama + Open WebUI) ile... Umbrel kişisel sunucunuz haline gelebilir ve verilerinizin kontrolünü yeniden kazanmanızı sağlar. Verileriniz ve gizliliğiniz üzerinde tam kontrol sahibi olurken, harici çözümlere çok benzeyen gösterişli bir kullanıcı deneyimi ile her gün kullandığınız hizmetleri kendiniz barındırırsınız.



Uygulamaları kapsayıcılarda dağıtarak Umbrel'i istediğiniz gibi şekillendirebilirsiniz: basit bir Bitcoin düğümü ve ekosistemine bağlı birkaç uygulama ile başlayın, ardından Bitcoin düğümünüzün yanına bir Lightning düğümü kurun ve örneğinizi ihtiyacınız olan kendi kendini barındıran uygulamalarla kademeli olarak zenginleştirin.



### Topluluk ve karşılıklı yardımlaşma



Umbrel'in rakiplerine göre en önemli avantajlarından biri geniş ve son derece aktif kullanıcı topluluğudur. Onlara çoğunlukla [Discord](https://discord.gg/efNtFzqtdx) ve [çevrimiçi forumları](https://community.umbrel.com/) üzerinden ulaşabilirsiniz. Burada yalnızca pratik tavsiyeler değil, her şeyden önce sorunları çözmek veya hataları düzeltmek için çözümler bulacaksınız. Başlamak, ilerlemek ve nihayetinde diğer kullanıcılara yardım etmek için harika bir yerdir, böylece Coin'nizle yalnız kalmazsınız.



![Image](assets/fr/084.webp)



### UmbrelOS lisansı



Umbrel'in kodu kamuya açıktır (görüntüleyebilir, Fork ve değiştirebilirsiniz), ancak gerçek bir açık kaynak lisansı altında değildir. Aslında, umbrelOS [*PolyForm Noncommercial 1.0*] lisansı (https://polyformproject.org/licenses/noncommercial/1.0.0/) altında dağıtılmaktadır, ancak bazı ilişkili geliştirme araçları MIT lisansı altında mevcuttur.



Pratik anlamda, kişisel, ticari olmayan kullanım için olduğu sürece umbrelOS ile istediğiniz her şeyi yapabilirsiniz: yasal bildirimlere uymanız koşuluyla, değişiklik, kar amacı gütmeyen amaçlar için yeniden dağıtım, kendiniz veya kar amacı gütmeyen kuruluşlar için türevler oluşturma.



Bununla birlikte, Umbrel veya türevlerini satmak (örneğin, umbrelOS önceden yüklenmiş önceden monte edilmiş bir makine), Umbrel ile ilgili hizmetleri ticari olarak sunmak veya kodunu kar amacıyla bir ürüne entegre etmek yasaktır.



Teknik olarak, bu lisans Umbrel'in kişisel kullanım için kurulumunu, denetimini veya uyarlanmasını kısıtlamaz. Yasal olarak, projeyi özellikle bulut sağlayıcıları tarafından yetkisiz yeniden satış veya ticari barındırmaya karşı korur. Bu nedenle Umbrel açık kaynak değildir, ancak koduna herkes tarafından erişilebilir.



Bununla birlikte, Mağaza'daki her uygulama, genellikle açık kaynak olmak üzere kendi lisansını korur.




## Full node'ün Şemsiye ile Kurulumu


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Artık gerekli tüm bilgilere sahip olduğumuza göre, ayrıntılara girmenin zamanı geldi. Bu eğitimde, UmbrelOS kullanarak eksiksiz bir Bitcoin düğümünün nasıl kurulacağını göstereceğiz.



### Gerekli malzemeler



Burada UmbrelOS x86 imajını (daha doğrusu x86_64 sürümünü) kullanacağız. ARM mimarili bir işlemciye sahip olmadığı sürece (Apple Silicon, Raspberry Pi, vb.) bu kılavuzu seçtiğiniz herhangi bir makinede takip edebilirsiniz. Bu, Umbrel'inizi nasıl kullanmayı düşündüğünüze bağlı olarak minimum gereksinimleri karşıladığı sürece Intel veya AMD 64 bit işlemcili herhangi bir bilgisayarın yeterli olacağı anlamına gelir (en azından çift çekirdekli bir işlemci önerilir).



Raspberry Pi 5'i tercih ettiyseniz (bir önceki bölümde belirtildiği gibi tavsiye etmediğim bir seçenek), kurulum biraz farklıdır. Daha sonra bu özel öğreticiyi takip edebilir ve Interface web `http://umbrel.local` adresinden kursuma geri dönebilirsiniz:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Önceki bölümde belirtildiği gibi, bu öğreticiyi iyi bir fiyata bulduğum yenilenmiş küçük bir bilgisayarda çalıştırmayı seçtim: Intel Core i7 işlemci ve 16 GB RAM ile donatılmış bir *Lenovo ThinkCentre M900 Tiny*. Bu, Umbrel'i çalıştırmak için, özellikle de bir Bitcoin düğümü için çok rahat bir yapılandırma. Ancak ben bu konfigürasyonu seçtim çünkü daha sonra bir Lightning düğümü ve daha zorlu uygulamalar kurmak istiyorum. Ayrıca ThinkCentre'ime 2 TB SSD ekleyerek Blockchain'nin tamamını kullanmaya devam ettim ve yine de rahat bir marj elde ettim. Bu yapılandırma ile toplam maliyet, tüm masraflar dahil 270 €'dur.



![Image](assets/fr/001.webp)



Lenovo'nun ThinkCentre Tiny serisini özellikle seviyorum, çünkü bunlar kompakt, sessiz ve çok sağlam makineler. Bu bilgisayarlar işletmeler arasında çok popüler ve bu nedenle 70 ila 200 € arasında ilginç konfigürasyonlar bulabileceğiniz ikinci el piyasasında bol miktarda bulunuyor.



Eğer benim gibi monitörü olmayan bir bilgisayar tercih ettiyseniz, **sadece kurulum süresince bir monitör ve klavye** bağlamanız gerekecektir. Daha sonra, aynı ağdaki başka bir bilgisayardan (veya daha sonraki bölümlerde ele alacağımız diğer yöntemlerle) uzaktan erişebileceksiniz. Ayrıca makinenizi yerel ağa bağlamak için bir RJ45 Ethernet kablosuna ve kurulum görüntüsünü saklamak için en az 4 GB'lık bir USB anahtarına ihtiyacınız olacak.



Özetlemek gerekirse, ekipman gereksinimleri şunlardır:




- X86_64 işlemcili bilgisayar (minimum Çift çekirdekli, önerilen Dört çekirdekli);
- RAM bellek (minimum 4 GB, uzun süreli kullanım için 8 GB veya daha fazlası önerilir);
- SSD (önerilen + 2 TB);
- UmbrelOS görüntü yüklemesi için USB anahtarı (+ 4 GB);
- Monitör ve klavye (bilgisayarda yoksa yalnızca ilk kurulum için kullanışlıdır);
- RJ45 Ethernet kablosu.



### Adım 1 - Bilgisayarın montajı



Seçtiğiniz donanıma bağlı olarak, ilk adım bilgisayarınızın çeşitli bileşenlerini bir araya getirmektir. Örneğin, benim durumumda, orijinal SSD'nin kapasitesi yalnızca 256 GB idi, bu nedenle başka bir kullanım için geri dönüştüreceğim ve 2 TB SSD ile değiştireceğim. RAM modüllerini de değiştirmek istiyorsanız, şimdi bunu yapmanın tam zamanı.



### Adım 2: Önyüklenebilir bir USB anahtarı hazırlayın



UmbrelOS'u makinenize kurmadan önce, işletim sistemini içeren önyüklenebilir bir USB anahtarı oluşturmanız gerekecektir. Adım 2'deki tüm adımlar kişisel bilgisayarınızda gerçekleştirilmelidir (doğrudan düğümünüz olacak bilgisayarda değil).





- UmbrelOS'un en son sürümünü USB formatında indirerek başlayın:



USB anahtar aracılığıyla kurulum için [ISO görüntüsünü indirmek için resmi Umbrel web sitesine] (https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) gidin. X86_64 mimarisiyle uyumlu sürümü seçtiğinizden emin olun (`umbrelos-amd64-usb-installer.iso` adlı dosya). İmaj oldukça büyük olduğu için indirme işlemi biraz zaman alabilir.



![Image](assets/fr/002.webp)





- Balena Etcher'ı kurun:



Önyüklenebilir USB bellek oluşturmak için [Balena Etcher] (https://www.balena.io/etcher/) adlı basit, platformlar arası bir araç kullanacaksınız. İndirin ve bilgisayarınıza kurun.



![Image](assets/fr/003.webp)





- En az 4 GB'lık boş bir USB anahtarı takın:



Bilgisayarınıza bir USB anahtarı takın (UmbrelOS ve Balena Etcher görüntüsünü indirdiğiniz). **Uyarı: anahtar üzerindeki tüm veriler silinecektir**. Önemli dosyalar içermediğinden emin olun.





- ISO görüntüsünü Balena Etcher ile USB belleğe yazdırın:



Balena Etcher'ı başlatın ve "*Dosyadan Flashla*" düğmesine tıklayarak indirdiğiniz "umbrelos-amd64-usb-installer.iso" ISO dosyasını seçin. Ardından, hedef cihaz olarak USB anahtarını seçin ve yazmaya başlamak için "*Flash!*" düğmesine tıklayın.



![Image](assets/fr/004.webp)



İşlem tamamlandığında, UmbrelOS içeren önyüklenebilir bir USB anahtarınız olacak ve makinenizde Umbrel'i önyüklemeye ve kurmaya hazır olacaksınız.



![Image](assets/fr/005.webp)



### Adım 3: Bilgisayarı USB anahtarından önyükleme



Artık UmbrelOS içeren önyüklenebilir USB belleğiniz hazır olduğuna göre, sistem kurulumunu başlatmak için bilgisayarınızı bu belleğe yükleyebilirsiniz. USB anahtarını ana bilgisayarınızdan çıkarın ve Umbrel'i ve Bitcoin düğümünüzü kurmak istediğiniz cihaza takın.



Bu bölümün başında açıklandığı gibi, kurulumu tamamlamak için bir görüntüleme cihazına ve bir giriş cihazına ihtiyacınız olacaktır. HDMI (veya bilgisayarınıza bağlı olarak başka bir bağlantı noktası) üzerinden bir ekran bağlayın ve USB üzerinden makinenize bir klavye bağlayın. Bu cihazlar yalnızca kurulum için gereklidir; Umbrel'e başka bir bilgisayardan uzaktan erişileceği için daha sonra bunlara ihtiyacınız olmayacaktır. Bu iki cihazı bilgisayarınıza bağlayın.



**İpucu:** Evde çevresel bir ekranınız yoksa, TV'nizi kullanabilirsiniz. HDMI (veya diğer) girişiyle, işletim sistemini kurarken geçici bir ekran olarak kullanılabilir.



Umbrel'in bir İnternet bağlantısına ihtiyacı olduğu açıktır. RJ45 Ethernet kablosunu cihazınız ile yönlendiriciniz arasına bağlayın.



![Image](assets/fr/006.webp)



Makinenizi açın. Çoğu durumda, USB anahtarını otomatik olarak algılaması ve ondan önyükleme yapması gerekir. Daha sonra UmbrelOS Interface kurulum ekranının göründüğünü göreceksiniz.



Aygıt başka bir sistemde önyükleme yapıyorsa veya bir hata mesajı görüntülüyorsa, bu muhtemelen USB anahtarından otomatik olarak önyükleme yapmadığı anlamına gelir. Bu durumda, yeniden başlatın ve BIOS/UEFI ayarlarına girin (bilgisayar üreticisine bağlı olarak genellikle `DEL`, `F2`, `F12` veya `ESC` tuşlarına basarak erişilir). Ardından, USB anahtarına öncelik vermek için önyükleme sırasını değiştirin. Ardından UmbrelOS'u başlatmak için cihazı yeniden başlatın.



### Adım 4: UmbrelOS'u bilgisayarınıza yükleyin



Cihaz USB bellekten önyüklendikten sonra, Interface UmbrelOS kurulumu tarafından karşılanacaksınız. Bu adım, sistemin doğrudan makinenizin dahili Hard diskine yüklenmesini içerir.



Görüntülenen ekranda bilgisayar tarafından algılanan tüm dahili depolama aygıtları listelenir. Her diske bir numara, bir ad ve bir depolama kapasitesi eşlik eder. Umbrel'i yüklemek istediğiniz diski bulun. **Uyarı: Bu diskteki tüm dosyalar kalıcı olarak silinecektir.**



![Image](assets/fr/007.webp)



Doğru diski belirledikten sonra (genellikle Blockchain'ü barındırmak için en büyük kapasiteye sahip olanı), ona atanan numarayı not edin. Örneğin, seçtiğiniz disk `2` numarası altında görünüyorsa, sadece `2` girin ve ardından klavyedeki `Enter` tuşuna basın.



![Image](assets/fr/008.webp)



Program seçilen diski biçimlendirecek, UmbrelOS'u yükleyecek ve sistemi otomatik olarak yapılandıracaktır. Bu işlem birkaç dakika sürebilir. İşlemin kesintisiz olarak çalışmasına izin verin.



![Image](assets/fr/009.webp)



Kurulum tamamlandığında, cihazı kapatmanız istenecektir. Bilgisayarı kapatmak için herhangi bir tuşa basın.



![Image](assets/fr/010.webp)



Artık Umbrel'iniz için gerekli olmayan USB anahtarını, klavyeyi ve ekranı çıkarabilirsiniz. Düğümünüzden geriye kalan tek şey Supply gücü ve RJ45 Ethernet kablosudur.



![Image](assets/fr/011.webp)



Cihazı yeniden başlatmadan önce aşağıdaki iki noktayı kontrol edin:





- USB anahtarının fişi çekilmiş**: bağlı kalırsa, sistem dahili disk yerine bu anahtarla yeniden başlatılabilir;
- Ethernet kablosu takılı**: cihazın çalışması için yönlendiricinize bağlı olması gerekir.



Güç düğmesine basın. Sistem otomatik olarak UmbrelOS'un kurulu olduğu dahili diskten açılır. İlk önyükleme yaklaşık **5 dakika** sürebilir. Bu süre zarfında Umbrel, hizmetlerini ve Interface'i başlatır.



Aynı yerel ağa** bağlı başka bir bilgisayardan (günlük bilgisayarınız), bir web tarayıcısı açın (Firefox, Chrome...) ve şu adrese gidin:



```
http://umbrel.local
```



Bu Address, Umbrel Interface grafiksel kullanıcı Interface'ya uzaktan erişmek ve yapılandırmaya başlamak için kullanılır.



En az 5 dakika bekledikten sonra Address `http://umbrel.local` tarayıcınızda çalışmazsa, sadece deneyin:



```
http://umbrel
```



Bu hala işe yaramazsa, Umbrel'inizin yerel IP Address'unu doğrudan tarayıcıya girin. Örneğin (`42` yerine Umbrel'i yerel ağda barındıran makinenizin numarasını yazın):



```
http://192.168.1.42
```



Umbrel IP Address'ınızı tanımlamak için en basitinden en gelişmişine kadar çeşitli yöntemler vardır:





- Yönlendiricinizin Interface yönetimine erişin ve yerel ağdaki Umbrel cihazının IP Address'sini bulun.





- Bağlı cihazları tespit etmek ve Umbrel'inizin IP Address'ünü bulmak için Angry IP Scanner gibi bir ağ tarama yazılımı kullanın.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Son çare olarak, cihaza bir monitör ve klavye bağlayın, oturum açın (varsayılan oturum açma adı: `umbrel`, parola: `umbrel`), ardından aşağıdaki komutu yazın:



```
hostname -I
```



Artık Umbrel'i kullanmaya hazırsınız!



### Adım 5: Umbrel ile çalışmaya başlama



Umbrel'inizi yapılandırmaya başlamak için "*Başlat*" düğmesine tıklayın.



![Image](assets/fr/013.webp)



#### Bir hesap oluşturun



Bir takma ad seçin veya adınızı girin, ardından güçlü bir parola belirleyin. Dikkatli olun: bu parola, ağınızdan Umbrel'inize (ve dolayısıyla Umbrel'de bir Lightning düğümü çalıştırıyorsanız potansiyel olarak bitcoinlerinize) erişimi koruyan tek engeldir. Ayrıca, bu hizmetler etkinleştirilmişse Tor veya VPN aracılığıyla uzaktan erişimi de korur.



Güçlü bir parola seçin ve en az bir yedek tuttuğunuzdan emin olun (bir parola yöneticisi önerilir).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Şifrenizi girdikten sonra "*Oluştur*" düğmesine tıklayın.



![Image](assets/fr/014.webp)



Umbrel yapılandırmanız artık tamamlandı.



![Image](assets/fr/015.webp)



#### Interface'ün Keşfi



Umbrel'in Interface'i oldukça sezgiseldir:





- Ana sayfada, yüklü uygulamalarınızı ve widget'larınızı görüntüleyebilirsiniz.



![Image](assets/fr/016.webp)





- "*App Store*" yeni uygulamalar yüklemenizi sağlar,



![Image](assets/fr/017.webp)





- "*Dosyalar*" menüsü Umbrel'inizde depolanan tüm belgeleri merkezileştirir.



![Image](assets/fr/018.webp)





- "*Ayarlar*" menüsü Umbrel'inizin ayarlarını değiştirmenize ve aşağıdakiler de dahil olmak üzere bilgilerine erişmenize olanak tanır:
    - Makinenizi güncelleyin, yeniden başlatın veya durdurun;
    - Kullanılabilir depolama alanına, RAM kullanımına ve işlemci sıcaklığına bakın;
    - Duvar kağıdını değiştir;
    - Tor aracılığıyla uzaktan erişimi yönetin, Wi-Fi'yi veya 2FA'yı etkinleştirin.



![Image](assets/fr/019.webp)



#### Güvenlik ve bağlantı ayarları



İlk ve en önemlisi, iki faktörlü kimlik doğrulamayı (2FA) etkinleştirmenizi şiddetle tavsiye ederim. Bu, şifrenize ekstra bir Layer güvenlik ekler. Umbrel'inizi kişisel dosyaları depolamak, bir Lightning düğümü çalıştırmak veya başka herhangi bir hassas etkinlik gerçekleştirmek için kullanmayı planlıyorsanız, neredeyse vazgeçilmezdir.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Bunu yapmak için ayarlardaki ilgili kutuya tıklayın.



![Image](assets/fr/020.webp)



Ardından kimlik doğrulama uygulamanızı kullanarak görüntülenen QR kodunu tarayın. Ardından 6 haneli dinamik kodu Umbrel'inizde verilen alana girin.



Şu andan itibaren, Umbrel'inize yapılan her yeni bağlantı için hem parola hem de iki faktörlü kimlik doğrulama (2FA) uygulamanız tarafından oluşturulan 6 haneli kod gerekecektir.



![Image](assets/fr/021.webp)



Tor üzerinden uzaktan erişimle ilgili olarak, ihtiyacınız yoksa, Umbrel'inizin saldırı yüzeyini sınırlamak için bu seçeneği devre dışı bırakmanızı öneririm. Varsayılan olarak, düğümünüze yalnızca aynı yerel ağa bağlı bir makineden erişilebilir. Tor üzerinden erişimi etkinleştirmek yine de Umbrel'inizi hareket halindeyken yönetmenize izin verecektir.



Bu özelliği etkinleştirirseniz, Tor Address'yi bilmesi koşuluyla dünyadaki herhangi bir makinenin düğümünüze bağlanmaya çalışması teorik olarak mümkün hale gelir. Ancak, parolanız ve 2FA sizi korumaya devam edecektir.



Bu seçeneği etkinleştirirseniz, iki faktörlü kimlik doğrulamayı (2FA) etkinleştirdiğinizden, güçlü bir parolanız olduğundan ve Tor bağlantınızı asla ifşa etmediğinizden emin olun Address.



Herhangi bir ağdan Umbrel'in Interface'una erişmek için Tor tarayıcınıza bu Tor Address'yi girmeniz yeterlidir.



![Image](assets/fr/026.webp)



Son olarak, bu ayarlar sayfasında Wi-Fi bağlantısını da etkinleştirebilirsiniz. Umbrel'i barındıran makinenizde bir Wi-Fi ağ kartı veya Wi-Fi dongle varsa, bu RJ45 kablosunu kullanmadan İnternet'e erişmenizi sağlar. Ancak, yapılandırmanıza bağlı olarak, bu çözüm bağlantıyı yavaşlatabilir, bu da ilk senkronizasyonu (IBD) ve düğümün gelecekteki kullanımını (örneğin, Lightning işlemleri için) etkileyebilir. Şahsen ben bu seçeneği önermiyorum çünkü bir node mobil kullanım için tasarlanmamıştır: her zaman uzaktan erişilir, bu nedenle fişe takılı bırakmanız daha iyi olur.



### Adım 6: Umbrel üzerine bir Bitcoin düğümü kurun



Artık UmbrelOS makinenize doğru bir şekilde kurulup yapılandırıldığına göre, Bitcoin node'unuzu kurmaya devam edebilirsiniz. Hiçbir şey daha basit olamazdı: App Store'a gidin, "*Bitcoin*" kategorisini açın, ardından "*Bitcoin Node*" uygulamasını seçin (aslında Bitcoin core'dir).



![Image](assets/fr/022.webp)



Ardından "*Yükle*" düğmesine tıklayın.



![Image](assets/fr/023.webp)



Kurulum tamamlandığında, Bitcoin düğümünüz IBD'sini (*İlk Blok İndirme*) başlatacaktır: Bitcoin'ün 2009'da oluşturulmasından bu yana tüm işlemleri ve blokları indirecek ve doğrulayacaktır.



![Image](assets/fr/024.webp)



Bu aşama özellikle zaman alıcıdır, çünkü süresi düğüm önbelleğine ayrılan RAM miktarı, disk hızı, İnternet bağlantı hızı ve işlemci gücü gibi çeşitli faktörlere bağlıdır. Bu nedenle yapılandırmaya bağlı olarak süre aralığı çok geniştir. Yüksek performanslı bir bilgisayarla (NVMe SSD, +32 GB RAM, güçlü işlemci ve iyi bir İnternet bağlantısı) IBD yaklaşık on saatte tamamlanabilir. Öte yandan, eski bir işlemci, düşük RAM veya daha da kötüsü mekanik bir Hard disk (kesinlikle önerilmez) bu işlemi birkaç haftaya kadar uzatabilir.



Normal konfigürasyona sahip bir bilgisayarla (iyi bir işlemci, 8 ila 16 GB RAM ve bir SSD), yaklaşık 2 ila 7 gün sürebilir.



IBD'yi biraz hızlandırmak için, `dbcache` parametresini kullanarak düğüm önbelleğine ayrılan RAM'i artırabilirsiniz (öncelikle UTXO seti için kullanılır, kursun ilerleyen bölümlerinde tekrar ele alacağız). Umbrel'de bu değişiklik düğüm parametrelerinizde, "*Optimizasyon*" sekmesinde yapılır.



![Image](assets/fr/025.webp)



Varsayılan olarak, Bitcoin core'deki `dbcache` parametresinin değeri 450 MiB veya yaklaşık 472 MB olarak ayarlanmıştır. Bu değeri artırarak IBD'yi biraz hızlandırabilirsiniz. Bununla birlikte, bu parametreyi çok yükseğe çıkarmanızı tavsiye etmem: 4 GiB'ye ayarlamak bile senkronizasyonu yalnızca yaklaşık %10 daha hızlı hale getirecektir ve IBD sırasında bir kesinti olması durumunda zaman kaybetmenize neden olabilir.



Makineniz için çok büyük bir değer ayırmamaya dikkat edin. UmbrelOS için mevcut RAM biterse, düğümünüz aniden durabilir, IBD'yi kesintiye uğratabilir ve manuel olarak yeniden başlatmanızı gerektirebilir, bu da önemli bir zaman kaybına neden olur.



Dbcache` parametresinin ilk senkronizasyon üzerindeki etkisi hakkında daha fazla bilgi edinmek için Jameson Lopp tarafından yapılan şu analizi tavsiye ederim: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Düğümünüzün IBD'si tamamlandığında (%100 senkronizasyon), artık tamamen işlevsel bir Bitcoin düğümüne sahipsiniz. Tebrikler, artık Bitcoin ağının ayrılmaz bir parçasısınız!



![Image](assets/fr/027.webp)



Bir sonraki bölümde, yeni node'unuzun pratik kullanımını inceleyeceğiz: Wallet'ınızı ona nasıl bağlayacağınız ve egemen bir Bitcoiner olmak için hangi uygulamaları yüklemeniz gerektiği.





# Wallet'inizi düğümünüze bağlama


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Dizinleyiciler: rol, çalışma ve çözümler


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Bu dersi almadan önce Bitcoin düğümlerini keşfettiyseniz, "indeksleyici" terimiyle karşılaşmış olabilirsiniz. Bunlar, bir Bitcoin core düğümüne eklenebilen Electrs veya Fulcrum gibi araçlardır. Ancak rolleri tam olarak nedir? Pratikte nasıl çalışırlar? Ve yeni Bitcoin düğümünüze bir tane kurmalı mısınız? İşte bu bölümde bunları inceleyeceğiz.



### İndeksleyici nedir?



Genel olarak bir indeksleyici, bir dizi ham veriyi tarayan, ilgili anahtarları (kelimeler, tanımlayıcılar ve adresler gibi) çıkaran ve "indeks" adı verilen ve her anahtarın külliyattaki verilerin tam yerini ifade ettiği bir yardımcı dosya oluşturan bir programdır. Bu ön işleme aşaması CPU zamanını kullanır ve bir miktar disk alanı gerektirir, ancak veritabanı her sorgulandığında tüm külliyatın işlenmesi ihtiyacını ortadan kaldırır; sadece dizinin sorgulanması neredeyse anında yanıt verir.



Daha basit bir ifadeyle, bir kitaptaki dizinle aynı prensiptir: belirli bir bilgiyi arıyorsanız, tüm kitabı yeniden okumak yerine, aradığınız bilginin bulunduğu sayfayı doğrudan bulmak için dizine başvurursunuz.



Bitcoin core gibi bir Bitcoin düğümünde, Blockchain verileri ham, kronolojik biçimde saklanır. Her blok, Address, tanımlayıcı veya Wallet'e göre herhangi bir özel sınıflandırma olmaksızın, sırayla girdiler ve çıktılar içeren işlemler içerir. Bu doğrusal organizasyon blok doğrulama için optimize edilmiştir, ancak hedefli aramalar için uygun değildir. Örneğin, indekslenmemiş bir düğümde belirli bir Address ile bağlantılı tüm işlemleri bulmak istiyorsanız, Blockchain'in tamamını blok blok ve işlem işlem manuel olarak incelemeniz gerekir. İşte tam da bu noktada Bitcoin düğümünüzdeki indeksleyici devreye girer.



![Image](assets/fr/085.webp)



İndeksleyici, bu ham veri yığınını (Blockchain, Mempool, UTXO seti) analiz eden ve işlem tanımlayıcıları, adresler ve blok yükseklikleri gibi anahtarları çıkaran özel bir yazılım programıdır. Bu anahtarlardan, her bir anahtarı düğümün depolama alanındaki bilginin tam konumuyla ilişkilendirerek dizinini oluşturur.



![Image](assets/fr/086.webp)



İndeksleme, düğümünüzdeki bilgileri hızlı, doğru ve verimli bir şekilde aramanızı sağlar. Örneğin, düğümünüze Sparrow gibi bir Wallet bağladığınızda, bir Address'ün bakiyesini neredeyse anında görüntüleyebilir. Somut olarak, dizinleyiciyi aşağıdaki gibi bir istekle sorgular: "_Which UTXOs are associated with this script-Hash? _" Dizinleyici, bu veriler zaten veritabanında listelendiği için Blockchain'nin tamamını yeniden okumak zorunda kalmadan neredeyse anında yanıt verir.



### Bitcoin core'nin bir indeksleyicisi var mı?



Ek yazılıma ihtiyaç duymayan Bitcoin core, Electrs veya Fulcrum gibi yazılımlarda bulunanlarla karşılaştırılabilir tam bir Address indeksleyici sunmamaktadır. Bununla birlikte, çeşitli dahili indeksleme mekanizmalarının yanı sıra sorgulama yeteneklerini genişletmek için isteğe bağlı seçenekler de içermektedir. Durumu tam olarak anlamak için projenin geçmişine bir göz atmamız gerekiyor.



Bitcoin core 0.8.0 sürümüne kadar, işlem doğrulama `txindex` olarak bilinen global bir işlem indeksine dayanıyordu. Bu dizin tüm Blockchain işlemlerini ve bunların çıktılarını referans alıyordu. Bir düğüm yeni bir işlem aldığında, tüketilen çıktıların (girdilerde) gerçekten var olduğunu ve daha önce harcanmadığını doğrulamak için bu dizine başvururdu. bu nedenle `txindex` o dönemde işlem doğrulama için vazgeçilmezdi.



Bununla birlikte, bu yaklaşımın sınırlamaları vardı: yavaştı, depolama açısından maliyetliydi ve bilgi açısından gereksizdi. Bunu düzeltmek için 0.8.0 sürümü ***Ultraprune*** adı verilen bir doğrulama modeli revizyonu getirmiştir. Bitcoin core, her şeyi işlem dizinleri şeklinde depolamak yerine, yalnızca UTXO'lara adanmış, `chainstate' adı verilen basit bir veritabanı tutar (günlük dilde bu "UTXO seti" olarak bilinir) ve çıktılar tüketildikçe ve oluşturuldukça listesini günceller.



Bu yöntem çok daha hızlıdır ve yalnızca kaydın mevcut durumunu saklar, böylece `txindex` indeksleyicisini gereksiz kılar. Bununla birlikte, geliştiriciler `txindex` kodunu silmek yerine, bu işlevi basit bir parametrenin (`txindex=1`) arkasında tutmayı seçtiler. Düğümünüzde bu seçeneği etkinleştirerek, herhangi bir işlemi `txid`den sorgulayabilirsiniz.



Genel kanının aksine Bitcoin core, Electrs veya Fulcrum gibi Address tabanlı indeksleme sunmaz. Bu seçimin birkaç nedeni var:





- Bitcoin core'in rolü tam bir Block explorer olmak ya da her kullanıma göre uyarlanmış bir API sağlamak değildir. Address tabanlı bir endeksin entegre edilmesi, yazılımın başlangıç kapsamının ötesine geçen uzun vadeli bir bakım Commitment anlamına gelecektir.





- Çoğu kullanım durumu zaten başka şekillerde ele alınabilir. Örneğin, bir Address'in bakiyesini tahmin etmek için, tam bir dizin gerektirmeden doğrudan UTXO kümesini sorgulayan `scantxoutset` komutunu kullanabilirsiniz.





- Her yazılım programının indekslenecek verilerin formatı veya türüne ilişkin özel gereksinimleri vardır (Address, Hash komut dosyası, tescilli etiket, vb.) Bu programların kendi özelleştirilmiş indekslerini oluşturmalarına izin vermek, Bitcoin core'te genel bir çözümü düzeltmekten daha esnek ve mantıklıdır.



Bitcoin core, tarihsel işleyişinin bir kalıntısı olan isteğe bağlı bir işlem dizinleyicisine (`txindex`) sahiptir, ancak bir Address dizini veya karmaşık aramalar için doğrudan bir Interface sağlamaz. Bu nedenle bazı durumlarda harici bir indeksleyici eklemek faydalı olabilir.



### Düğümünüze bir Address dizinleyici eklemeniz gerekir mi?



Electrs veya Fulcrum gibi bir Address indeksleyici eklemek zorunlu değildir; bu sizin özel ihtiyaçlarınıza bağlıdır.



Bakiyeleri görüntülemek ve işlemleri yayınlamak için düğümünüze Sparrow gibi bir Wallet bağlamak istiyorsanız, bu doğrudan Bitcoin core'in Interface RPC'i aracılığıyla yerel olarak veya Tor aracılığıyla uzaktan tamamen mümkündür.



Öte yandan, bir Mempool'i çalıştırmak gibi daha gelişmiş yazılımları kullanmak için Yerel olarak, bir Address indeksleyicisinin kurulumu, Block explorer alanı için vazgeçilmez hale gelir.



Dizinleyici belirli bir senkronizasyon süresi gerektirir (IBD'den daha az) ve ek disk alanı kaplar. Blockchain'u indirdikten sonra SSD'nizde hala yeterli boş alan varsa, kolayca bir dizinleyici ekleyebilirsiniz.



### Hangi indeksleyiciyi seçmeliyim?



Bu tür bir Address endeksi oluşturmak ve erişilebilir kılmak için yaygın olarak iki yazılım programı kullanılmaktadır: **Electrs** ve **Fulcrum**. Bu araçlar Blockchain'u script-Hash'e (adresler) göre indeksler ve ardından Electrum Wallet, Sparrow veya Phoenix gibi çok sayıda cüzdanın bağlandığı standartlaştırılmış bir Interface (Electrum protokolü) önerir.



![Image](assets/fr/087.webp)



Basitçe söylemek gerekirse, Electrs oldukça kompakttır: Blockchain'yı daha hızlı indeksler ve daha az disk alanı kaplar, ancak sorgularda Fulcrum'dan biraz daha az iyi performans gösterir. Buna karşılık, Fulcrum daha fazla disk alanı tüketir ve indekslemesi daha uzun sürer, ancak üstün sorgu performansı sunar.



Bireysel kullanım için Electrs'i öneririm: daha az yer kaplar, bakımı iyidir ve bazı isteklerde Fulcrum'dan biraz daha yavaş olsa da günlük kullanım için fazlasıyla yeterlidir. Eğer zamanınız ve disk alanınız varsa, Fulcrum'u da deneyebilirsiniz, özellikle doğrulanacak çok sayıda adresi olan cüzdanlarda çok daha iyi performans gösterecektir.



Somut olarak, Ağustos 2025'te Electrs yaklaşık 56 GB depolama alanına ihtiyaç duyarken, Fulcrum için bu rakam yaklaşık 178 GB olacaktır. Bu nedenle indeksleyici seçiminiz depolama kapasitenize de bağlıdır:




- Disk alanınız çok sınırlıysa, harici bir Address dizinleyici olmadan Bitcoin core ile idare etmeniz gerekecektir.
- Bir indeksleyici kullanmak istiyor ancak yine de kapasiteniz kısıtlıysa Electrs'i tercih edin.
- Eğer rahat bir disk alanınız varsa, Fulcrum tam da aradığınız şey olabilir.



Bu BTC 202 kursunun geri kalanında Electrs kullanacağım, ancak Fulcrum ile kolayca takip edebilirsiniz: kurulum prosedürü, Interface'un Wallet'ye bağlanması gibi aynıdır, çünkü her ikisi de bir Electrum sunucusunu açığa çıkarır.



### Umbrel'e nasıl indeksleyici yükleyebilirim?



Umbrel'inize Electrs (veya Fulcrum) yüklemek için prosedür basittir: App Store'a gidin, ilgili uygulamayı arayın (Bitcoin sekmesinde bulunur) ve ardından "*Yükle*" düğmesine tıklayın.



![Image](assets/fr/028.webp)



Kurulum tamamlandıktan sonra, Electrs birkaç saat sürebilecek bir senkronizasyon (indeksleme) aşamasına geçecektir.



![Image](assets/fr/029.webp)



Senkronizasyon tamamlandıktan sonra, Wallet yazılımınızı Umbrel'de barındırılan Electrum sunucunuza bağlayabilirsiniz.



## Wallet'ümü Bitcoin düğüme nasıl bağlarım?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Artık eksiksiz bir Bitcoin düğümüne sahip olduğunuza göre, onu iyi bir şekilde kullanmanın zamanı geldi! Bir sonraki bölümde Umbrel örneğiniz için diğer potansiyel kullanımları keşfedeceğiz. Ancak, temel bilgilerle başlayalım: Wallet yazılımınızı kendi Blockchain'inizden gelen bilgileri kullanmak ve işlemleri kendi düğümünüz üzerinden dağıtmak için bağlamak.



Yukarıda belirtildiği gibi, iki ana bağlantı arayüzü vardır:




- RPC üzerinden Bitcoin core'e doğrudan bağlantı;
- Veya bir Electrum sunucusuna (Electrs veya Fulcrum) bağlanın.



Bu eğitimde, yeni başlayanlar için hem basit hem de güvenli bir çözüm olduğundan, Tor üzerinden node'unuza bağlanmaya odaklanacağız. Yanlış yapılandırma, verilerinizin güvenliği ve gizliliği için önemli bir risk oluşturduğundan, düğümünüzün RPC bağlantı noktasını açıkta bırakmamanızı şiddetle tavsiye ederim. Tor üzerinden iletişimin en büyük dezavantajı yavaşlığıdır. Bir sonraki bölümde, düğümünüze uzaktan erişim için Tor'a hızlı ve güvenli bir alternatif keşfedeceğiz: VPN.



Bu bölümde örnek olarak Sparrow'i kullanacağız, ancak prosedür Electrum sunucularına bağlantı kabul eden diğer tüm Wallet yönetim yazılımları için aynıdır. Uygulama parametrelerinizde ilgili ayarı bulmanız yeterlidir (genellikle "*Server*", "*Network*", "*Node*"...).



Sparrow'te "*Dosya*" sekmesini açın ve "Ayarlar" menüsüne gidin.



![Image](assets/fr/030.webp)



Ardından bağlantı parametrelerine erişmek için "*Sunucu*" üzerine tıklayın.



![Image](assets/fr/031.webp)



Daha sonra yazılımınızı bir Bitcoin düğümüne bağlamak için üç seçenek keşfedeceksiniz:




- Genel Sunucu* (sarı): varsayılan olarak, bir Bitcoin düğümüne sahip değilseniz, bu seçenek sizi sahip olmadığınız bir genel düğüme (genellikle bir şirketin) bağlar. Umbrel'de kendi düğümünüz olduğu için bu seçenek burada geçerli değildir.
- Bitcoin core* (Green): bu seçenek Interface RPC üzerinden, yani doğrudan Bitcoin core'ya bağlantıya karşılık gelir.
- Özel Electrum* (mavi): bu seçenek indeksleyicinizin Interface Electrum Sunucusu (Electrs veya Fulcrum) üzerinden bağlanmanızı sağlar.



### Bitcoin core RPC'ye bağlantı



Umbrel düğümünüzün bir indeksleyicisi yoksa, seçmeniz gereken seçenek budur. Sparrow üzerinde "*Bitcoin core*" üzerine tıklayın.



![Image](assets/fr/032.webp)



Daha sonra düğümünüzle bağlantı kurmak için birkaç bilgi girmeniz gerekecektir. Tüm bu verilere Umbrel'deki "*Bitcoin Node*" uygulamasından Interface'in sağ üst köşesindeki "*Connect*" düğmesine tıklayarak erişebilirsiniz.



![Image](assets/fr/033.webp)



"*RPC Details*" sekmesi bağlantı için gerekli tüm bilgileri görüntüler. Tor Address üzerinden bağlanmayı seçin (`.onion` içinde).



![Image](assets/fr/034.webp)



Bu verileri Sparrow wallet üzerindeki ilgili alanlara girin ve ardından "*Bağlantıyı Test Et*" düğmesine tıklayın.



![Image](assets/fr/035.webp)



Bağlantı başarılı olursa, bir Green işareti ve bir onay mesajı görüntülenecektir.



![Image](assets/fr/036.webp)



Interface Sparrow wallet'in sağ alt tarafındaki tik işareti artık Green olacaktır (Bitcoin core'ye doğrudan bağlantı olduğunu gösterir).



**Not:** Bağlantının başarılı olması için düğümünüzün %100 senkronize olması gerekir. Eğer durum böyle değilse, lütfen IBD'nin sonuna kadar bekleyin.



### Elektriğe Bağlanın



Düğümünüzde bir dizinleyici varsa, sorgularınız daha hızlı işleneceği için doğrudan Bitcoin core kullanmak yerine ona bağlanmak daha iyidir.



Sparrow'da "*Özel Elektrum*" sekmesine gidin.



![Image](assets/fr/037.webp)



Daha sonra indeksleyicinizle bağlantı kurmak için birkaç bilgi girmeniz gerekecektir. Bu verileri Umbrel'deki "*Electrs*" uygulamasında (veya uygun olan yerlerde "*Fulcrum*") bulabilirsiniz.



Address `.onion` bağlantısını elde etmek için "*Tor*" sekmesini seçin. Bir mobil Wallet yazılımı bağlamak isterseniz, QR kodunu doğrudan da tarayabilirsiniz.



![Image](assets/fr/038.webp)



Electrum sunucunuzun Tor Address'unu "*URL*" alanına girmeniz ve ardından "*Bağlantıyı Test Et*" düğmesine tıklamanız yeterlidir.



![Image](assets/fr/039.webp)



Bağlantı başarılı olursa, bir onay işareti ve bir onay mesajı görüntülenecektir.



![Image](assets/fr/040.webp)



Interface Sparrow wallet'ın sağ alt köşesindeki onay işareti maviye dönecektir (Electrum sunucusuna bağlantı ile ilişkili renk).



**Not:** Bağlantının çalışması için indeksleyicinizin %100 senkronize olması gerekir. Eğer durum böyle değilse, indeksleme işlemi tamamlanana kadar bekleyin.



Artık Wallet'ünüzü Bitcoin düğümünüze nasıl bağlayacağınızı biliyorsunuz! Bir sonraki bölümde, Umbrel'de bulunan ve özellikle sevdiğim ve düğümünüz aracılığıyla Bitcoin'yi günlük kullanımınızı geliştirmenizi sağlayacak birkaç ek uygulamayı tanıtacağım.




## Mevcut uygulamalara genel bakış


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel kapsamlı bir uygulama mağazası sunmaktadır. Göreceğiniz gibi, Bitcoin ile ilgili birçok aracın yanı sıra çok farklı alanlarda çok çeşitli uygulamalar da var: hizmetler ve dosyalar için kendi kendine barındırma çözümleri, üretkenlik uygulamaları, daha genel finansal araçlar, medya yönetimi, ağ güvenliği ve yönetimi, geliştirme, yapay zeka, sosyal ağ ve hatta ev otomasyonu.



Bu BTC 202 kursunda, yalnızca Bitcoin ile ilgili uygulamalara odaklanacağız. Ancak, işinize yarayabilecek araçlar için kataloğun geri kalanını keşfetmekten çekinmeyin.



Elbette, tüm Bitcoin uygulamalarını burada listelemek imkansız olacaktır. Bu bölümde, size Bitcoin'yı günlük kullanımınızı kolaylaştıracak ve zenginleştirecek temel araçları tanıtmak istiyorum.



### Mempool.space



Bitcoin'in günlük kullanımında, gerçekten vazgeçilmez olan bir araç varsa, o da Block explorer'dir. İster çevrimiçi olarak erişilebilir ister yerel olarak yüklenmiş olsun, Blockchain'un ham verilerini yapılandırılmış, net ve okunması kolay bir formata dönüştürür. Ayrıca, kullanıcıların belirli bir bloğu, işlemi veya Address'i hızlı bir şekilde bulmalarını sağlayan bir arama motoruna sahiptir.



Somut olarak, gezgin işleminizin bir bloğa dahil edilmesi için gereken ücretleri tahmin etmenize, ardından ilerlemesini izlemenize olanak tanır: ücret piyasasına bağlı olarak yakın gelecekte dahil edilip edilmeyeceğini öğrenin ve son olarak gerçekten bir bloğa dahil edildiğini onaylayın. Ayrıca geçmiş işlemlerinizi analiz etme ve geçmişlerine bakma imkanı da sunar. Kısacası, bitcoiner'ın İsviçre Çakısı.



Daha önce de belirtildiği gibi, bir gezgin çevrimiçi olarak bir web sitesinde barındırılabilir veya makinenizde yerel olarak çalıştırılabilir. Çevrimiçi hizmetlerin en büyük dezavantajı gizliliğinizi tehlikeye atabilmeleridir. VPN veya Tor olmadan, gezgini barındıran sunucu IP Address'nizi görüntülediğiniz işlemlere bağlayabilir ve bu da zincir analizi için ideal bir giriş noktası sağlayabilir.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Dahası, İnternet Servis Sağlayıcınız (İSS) belirli bir işlemi Block explorer sitesi üzerinden görüntülediğinizi biliyor olabilir. Bu aynı zamanda bir güven sorununu da beraberinde getirir: doğruluğunu kendiniz teyit edemeden, işlemleriniz hakkında size doğru bilgi sağlaması için çevrimiçi hizmete güvenmeniz gerekir.



Bu yüzden kendi yerel Block explorer'ünüzü kullanmak her zaman en iyisidir. Bu şekilde, tüm sorgular İnternet üzerinden geçmeden doğrudan sizin kontrolünüzdeki bir makinede işlendiğinden, arama etkinliğinizle ilgili hiçbir veri dışarı sızmayacaktır. Dahası, yerel bir gezgin, kendi kurallarınıza göre kendi kendinize doğruladığınız ve güvenebileceğiniz kendi Bitcoin düğümünüzden gelen verilere dayanır.



Umbrel çeşitli blok kaşifleri sunar:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Ben özellikle node'uma yüklediğim Mempool.Space'i çok seviyorum. Lütfen dikkat: Umbrel'de çoğu blok kaşifini kullanmak için bir Address indeksleyici gereklidir. Bu nedenle %100 senkronize Blockchain'a sahip Bitcoin Node (ya da Bitcoin Knots) uygulamasının yanı sıra Electrs ya da Fulcrum gibi yine %100 senkronize bir indeksleyiciye ihtiyacınız var.



Uygulama yüklendikten sonra, kendi gezgininize erişmek için açmanız yeterlidir.



![Image](assets/fr/041.webp)



Mempool.Space gezginini kullanma hakkında daha fazla bilgi edinmek için bu kapsamlı öğreticiyi tavsiye ederim:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Yıldırım Düğümü



Artık kendi Bitcoin düğümünüze sahip olduğunuza göre, üçüncü taraf bir altyapıya güvenmeden off-chain işlemlerini gerçekleştirmek için kendi Lightning düğümünüzü de kurabilirsiniz.



Umbrel, Lightning düğümünüzü kurmanıza ve çalıştırmanıza yardımcı olacak bir dizi uygulama sunar. Halihazırda iki ana uygulama arasından seçim yapabilirsiniz:




- LND, *Lightning Node* uygulaması aracılığıyla;
- Çekirdek Yıldırım.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Daha sonra düğümünüzü ana Interface'den yönetebilir veya daha fazla işlevsellik ve gelişmiş seçenekler için *Ride The Lightning* veya *ThunderHub* yükleyebilirsiniz. Bu araçlar size düğümünüz için çok daha kapsamlı bir web tabanlı Interface yönetim sistemi sağlayacaktır.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Son olarak, kanal açabileceğiniz eşler bulmanızı sağlayan ve hem giden hem de gelen nakit işlemlerini mümkün kılan *Lightning Network+* uygulamasını tavsiye ederim.



![Image](assets/fr/089.webp)



Umbrel sayesinde, kişisel bir Lightning düğümünü yönetmek büyük ölçüde basitleştirilmiştir, ancak yine de nispeten karmaşıktır. Bu nedenle, gelecekte tamamen bu kullanıma ayrılmış bir kursta bu konuya daha yakından bakacağız.



### Kuyruk Ölçeği



Umbrel'de özellikle beğendiğim bir diğer uygulama da Tailscale. Dünyanın neresinde olurlarsa olsunlar, birden fazla cihaz arasında güvenli ağlar oluşturmayı basitleştirmek için tasarlanmış bir VPN uygulaması. Merkezi sunuculara dayanan geleneksel VPN'lerin aksine Tailscale, çeşitli makineleriniz arasında uçtan uca şifrelenmiş bağlantılar kurmak için WireGuard protokolünü kullanıyor. Bu, karmaşık ağ yapılandırmalarına gerek kalmadan sadece birkaç dakika içinde çalışan bir VPN kurabileceğiniz anlamına gelir.



Umbrel'de Tailscale kurulumu, Bitcoin düğümünüzü kendi sanal özel ağınıza bağlar. Düğümünüz yapılandırıldıktan sonra, yalnızca aynı Tailscale ağına bağlı diğer cihazlardan (bilgisayarlar, akıllı telefonlar ve tabletler gibi) erişilebilen özel bir Tailscale IP Address alır. Bu bağlantı uçtan uca şifrelenir ve korumasız bir genel ağdan geçmez, bu da şifrelenmemiş bir bağlantıya kıyasla güvenliği önemli ölçüde artırır.



![Image](assets/fr/090.webp)



Somut olarak, Tailscale, Umbrel'inizi kullanırken size çeşitli avantajlar sunar:





- Interface Umbrel'i yönetebilir veya düğümünüze bağlı uygulamalara (Mempool, Ride The Lightning, ThunderHub... gibi), aynı yerel ağdaymış gibi, internette bağlantı noktalarını açığa çıkarmadan ve çok yavaş olan Tor'dan geçmeden her yerden erişebilirsiniz;





- Electrum sunucunuza (Electrs veya Fulcrum) veya Tor'u atlayarak VPN'iniz aracılığıyla doğrudan Bitcoin core'e bağlanabilirsiniz. Bu, Tor kullanımıyla karşılaştırılabilir, ancak çok daha yüksek hız ve daha düşük gecikme ile güvenli bir bağlantı sağlar. Kısacası, Clearnet bağlantısının hızının keyfini çıkarırken Tor'un gizlilik ve güvenlik avantajlarını korursunuz. Bir On-Chain Wallet için bu kazanç marjinal görünebilir, ancak daha sonraki bir tarihte kendi Lightning düğümünüzü kurmayı planlıyorsanız, fark oldukça büyüktür. Gerçekten de, Tor üzerinde hareket halindeyken node'unuz aracılığıyla ödeme yapmak, gereken çok sayıda değişim nedeniyle son derece yavaşken, Tailscale ile mükemmel bir şekilde çalışır.





- NAT kurallarını yapılandırmaya, portları açmaya veya geleneksel bir VPN sunucusu kurmaya gerek yoktur. Uygulama Umbrel'e ve cihazlarınıza yüklendikten sonra ağ otomatik olarak kurulur.



Bu nedenle, gizlilik veya güvenlikten ödün vermeden düğümünüze dünyanın herhangi bir yerinden güvenli, yüksek performanslı ve yapılandırması kolay bir şekilde erişmek istiyorsanız Umbrel üzerindeki Tailscale çok ilginç bir çözümdür.



Tailscale'i Umbrel'inize kurmak ve yapılandırmak için bu eğitimin 4. bölümüne bakın: "*Umbrel'de Tailscale Kullanımı*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



"*Notes and Other Stuff Transmitted by Relays*" ifadesinin kısaltması olan Nostr, mesajların merkezi bir platforma bağlı olmadan İnternet üzerinde yayınlanmasını ve değiş tokuş edilmesini sağlamak için tasarlanmış açık, merkezi olmayan bir protokoldür. Her kullanıcının bir çift kriptografik anahtarı vardır: bir tanımlayıcı görevi gören açık anahtar (`npub`) ve mesajları imzalamak ve özgünlüklerini garanti etmek için kullanılan özel anahtar (`nsec`).



Mesajlar bağımsız rölelerden oluşan bir ağ üzerinden iletilir. Bu dağıtık mimari Nostr'u sansüre karşı dirençli hale getirir: tek bir sunucu erişimi veya dağıtımı kontrol etmez ve bir kullanıcı istediği kadar röleye bağlanabilir.



Bu protokol Bitcoin topluluğu içinde çok popülerdir çünkü Bitcoin gibi Nostr da dijital egemenlik ve veri kontrolü konularını ele almaktadır. Yaratıcısı Fiatjaf, sayısız katkısıyla ekosistemde zaten tanınan bir geliştiricidir.



Umbrel'iniz ile Nostr kullanımınızı optimize edebilirsiniz. Nostr Relay*** uygulamasını yükleyerek, kendi özel aktarıcınızı doğrudan makinenizde barındırabilir, Nostr'daki tüm gönderilerinizin ve etkileşimlerinizin yerel olarak kaydedilmesini ve genel aktarıcılar tarafından silinerek kaybedilmemesini sağlayabilirsiniz.



Nostr istemcileri ***noStrudel*** veya ***Snort*** da Umbrel'de mevcuttur. Bu uygulamalar sayesinde, Umbrel'inizdeki Interface web'den doğrudan Nostr ekosistemini yayınlayabilir, okuyabilir, profil arayabilir ve etkileşimde bulunabilirsiniz.



Son olarak, Umbrel'de Nostr'da yerel Lightning ödemelerini mümkün kılan ***Nostr Wallet Connect*** uygulaması var. Somut olarak, üçüncü taraf bir hizmetten geçmeye gerek kalmadan, içeriği ödüllendirmek veya paraya dönüştürülmüş bir şekilde etkileşimde bulunmak için "*zaps*" adı verilen mikro ödemeler göndermek üzere gelecekteki Lightning düğümünüzü Nostr müşterilerinize bağlayabilirsiniz. Bu ödemeler, kanallarınız aracılığıyla doğrudan kişisel düğümünüzden gönderilir.



Tüm bu uygulamaları nasıl kullanacağınızı öğrenmek için bu eğitimin tamamına göz atmanızı tavsiye ederim:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay Sunucusu



BTCPay Server, Bitcoin ve Lightning Network üzerinden aracılar olmadan ödeme kabul etmenizi ve fonların kendi kendine saklanmasını sağlayan ücretsiz, açık kaynaklı bir ödeme işlemcisidir.



BTCPay Server'ın mimarisi bir Bitcoin düğümüne ve Lightning için uyumlu bir uygulamaya (LND, Core Lightning...) dayanmaktadır, bu da onu tamamen gözetimsiz tek PoS çözümlerinden biri haline getirmektedir. Aynı zamanda takip ve muhasebe için en kapsamlı yazılımdır.



![Image](assets/fr/091.webp)



Bir işletmeniz varsa ve Bitcoin ödemelerini doğrudan Umbrel node'unuz üzerinden kabul etmek istiyorsanız, BTCPay Server uygulaması sizin için idealdir. Bu konuda daha fazla bilgi edinmek için aşağıdaki kaynaklara başvurmanızı tavsiye ederim:





- İşletmenizde Bitcoin kullanımı üzerine BIZ 101 kursu:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- BTCPay Sunucusunun kullanımına ilişkin POS 305 kursu:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- BTCPay Sunucu eğitimi:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Gelişmiş kavramlar ve en iyi uygulamalar


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Şemsiye düğümünüzün bakımı


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Bu son bölümü başlatmak için ve daha gelişmiş teoriye geçmeden önce, bu kısa bölümde Umbrel düğümünüz kurulduktan, senkronize edildikten ve doğru şekilde yapılandırıldıktan sonra yapabileceğiniz en iyi uygulamaları ve somut eylemleri incelemek istiyorum. Günlük olarak bakımını nasıl yapıyorsunuz?



### Ekipmanı sağlıklı tutmak



Güvenilir bir düğüm, sağlam bir donanımla başlar. Düğümünüzü barındıran makinenin uygun şekilde havalandırıldığından, Dust içermediğinden ve her türlü ısı ve nem kaynağından uzakta, kuru bir ortama kurulduğundan emin olun. Kapalı bir alana sıkıştırmaktan kaçının ve iyi havalandırılan bir yeri tercih edin.



Raspberry Pi ve mini PC'lerde, Dust sonunda soğutucuları tıkar, sıcaklığı yükseltir ve throttling'e (kaynak kullanımının gönüllü olarak sınırlandırılması) yol açar, bu da düğümünüzün verimliliğinde bir düşüşe neden olur. Bu nedenle hava girişini ve fanı periyodik olarak, ideal olarak birkaç ayda bir temizlemenizi öneririm.



Yüksek kaliteli bir Supply güç kaynağı kullandığınızdan emin olun, çünkü dengesiz voltaj sistemin bozulmasına ve hatta yangın tehlikesine neden olabilir. İdeal olarak, makinenizin üreticisi tarafından sağlanan orijinal Supply gücünü kullanmalısınız. Güç şeritlerinde Joule etkisi nedeniyle aşırı ısınmaya karşı da dikkatli olun: her zaman izin verilen maksimum güce uyun ve asla birkaç güç şeridini kademeli olarak bağlamayın.



Ayrıca bir UPS'e yatırım yapmanızı öneririm. Bu, düğümünüzü ani kapanmalardan korur, bir kesinti durumunda Umbrel'in temiz bir şekilde kapanmasını sağlar ve mikro kesintiler veya kısa süreli arızalar sırasında çalışmanın sürekliliğini sağlar.



Depolama tarafında, ilerlemeyi takip edin: disk doygunluğa yaklaşıyorsa, alan boşaltmayı (kullanılmayan uygulamaları kaldırın, dizinleyici ayarlarını yapın) veya daha büyük bir SSD'ye geçmeyi düşünün. Tam bir Bitcoin düğümünün dezavantajı, her 10 dakikada bir yeni bir blok oluşturulduğu ve eski bloklar silinemediği için (düğüm pruned değilse) depolama gereksinimlerinin sürekli artmasıdır. Bu nedenle donanımınızı satın alırken yeterince büyük bir kapasite planlamanızı tavsiye ederim (minimum 2 TB).



### Güncelleme



Düğüm güncellemeleri üç ana nedenden dolayı önemlidir: birincisi, güvenlik (güvenlik açığı yamaları, ağ sertleştirme ve DoS koruması); ikincisi, uyumluluk (röle politikası değişiklikleri, format değişiklikleri ve protokol yükseltmeleri); ve üçüncüsü, güvenilirlik ve performans (hata düzeltmeleri, kaynak tüketimi ve diğer iyileştirmeler). Bu nedenle UmbrelOS ve uygulamalarınızın güncel olup olmadığını düzenli olarak kontrol edin:





- Sistemi güncellemek için: Ayarlar menüsünü açın, ardından "*UmbrelOS*" parametresinin yanındaki "*Güncellemeyi Kontrol Et*" düğmesine tıklayın.



![Image](assets/fr/042.webp)





- Uygulamaları güncellemek için: App Store'a gidin. Uygulamalarınızdan herhangi birinin güncellenmesi gerekiyorsa, Interface'un sağ üst köşesinde kırmızı balonlu bir düğme görünecektir. Sadece üzerine tıklayın, ardından her bir uygulamayı güncelleyin.



İşletim sisteminizi ve uygulamalarınızı güncel tutmak için bu işlemi düzenli olarak gerçekleştirin.



### Yedeklemeler



İşlemlerinizi doğrulamak ve dağıtmak için yalnızca Bitcoin düğümünüzü kullanıyorsanız, ancak cüzdanlarınız Umbrel dışında yönetiliyorsa (örneğin, bir Hardware Wallet ve Sparrow wallet ile), doğrudan Umbrel'e yedeklenecek hiçbir şey yoktur. Bu durumda, temel yedekleme, harici Wallet'inizin kurtarma ifadesi ve Descriptor'ü olmaya devam eder ve bu, kendi düğümünüzü kullansanız da kullanmasanız da geçerlidir. Yani önceki yapılandırmanızda hiçbir şey değişmez.



Öte yandan, Umbrel'de kullandığınız ek uygulamalara bağlı olarak, daha fazla yedekleme gerekebilir. Bu durum özellikle Umbrel üzerinde bir Lightning düğümü çalıştırıyorsanız geçerlidir. Bu durumda, Lightning düğümünüzü kurduğunuzda verilen seed'yı yedeklemeniz kesinlikle çok önemlidir. seed'ya ek olarak, bir sorun durumunda Lightning düğümünüzü geri yükleyebilmek için güncel bir ***Statik Kanal Yedeğine (SCB)*** ihtiyacınız vardır. SCB, kanalları zorla kapatarak fonlarınızı kurtarmanıza olanak tanır. seed veya SCB eksikse, bir Lightning düğümünü geri yüklemek imkansızdır.



Umbrel, güncel bir dosyanın her zaman kullanılabilir olmasını sağlamak için bu SCB'yi Tor aracılığıyla sunucularında otomatik ve dinamik olarak yedekleme seçeneği de sunar. Bu durumda, düğümü geri yüklemek için yalnızca seed gereklidir.



Bu konuları bir sonraki LNP202 kursunda ayrıntılı olarak tekrar ele alacağız.



### Günlük operasyonel güvenlik



Güvenlik açısından, Interface Umbrel için uzun, benzersiz ve rastgele bir parola kullanın ve iki faktörlü kimlik doğrulamayı (2FA) etkinleştirmeyi unutmayın. Hem parola hem de 2FA koruması sunan uygulamalar için her zaman her ikisini de etkinleştirin ve varsayılan parolaları değiştirin.



Güvenli bir ağ geçidi (VPN, Tor veya yalnızca yerel erişim gibi) kullanmadan kontrol panelini asla İnternet'e açmayın. Saldırı yüzeyini azaltmak için yüklediğiniz uygulama sayısını sınırlayın ve artık ihtiyacınız olmayanları düzenli olarak silin.



Genel olarak bilgisayar güvenliği konusundaki bilginizi derinleştirmek için bu diğer ücretsiz kursa göz atmanızı şiddetle tavsiye ederim:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Teşhis ve kendi kendine yardım



Umbrel'inizde bir hata olması durumunda, önce UmbrelOS'un veya ilgili uygulamanın sorun giderme bölümü aracılığıyla generate bir tanılama paketi oluşturun, ardından uygulamayı temiz bir şekilde yeniden başlatın. Gerekirse, sistemi tamamen yeniden başlatmayı da deneyin.



Sorun devam ederse, [Discord'larındaki Umbrel kullanıcı topluluğuna katılmanızı] (https://discord.gg/efNtFzqtdx) tavsiye ederim. Daha önce aynı zorlukla karşılaşmış ve bir çözüm bulmuş birileri olup olmadığını belirlemek için bir arama yaparak başlayın. Eğer yoksa, `general-support` kanalına bir mesaj gönderebilirsiniz. Ayrıca [Umbrel forumunu](https://community.umbrel.com/) da kullanabilirsiniz.



Bu alanlar yalnızca güvenlik duyurularını ve güncellemelerini takip etmenizi değil, aynı zamanda soru sormanızı ve nihayetinde diğer kullanıcılara yardımcı olmanızı sağlayacaktır. En iyi uygulamalar genellikle bu paylaşımlarda keşfedilir.



Bu basit alışkanlıklarla Umbrel düğümünüz hem sizin için hem de Bitcoin ağı için istikrarlı, güvenli ve kullanışlı kalacaktır.




## IBD'yi ve eş keşif sürecini anlama


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Bitcoin düğümünüz işlem geçmişi hakkında herhangi bir ön bilgi olmadan başlar. Başlangıçta sadece yazılım (Bitcoin core veya benzeri) çalıştıran bir bilgisayardır. Tamamen senkronize ve operasyonel bir Bitcoin düğümü olmak için, Genesis bloğundan (Satoshi Nakamoto tarafından 3 Ocak 2009'da yayınlanan 0. blok) bu yana yayınlanan tüm blokları kontrol ederek Ledger'in durumunu yerel olarak yeniden yapılandırmalıdır. Bu adım **IBD (_Initial Block Download_)** olarak adlandırılır.



IBD, Blockchain'nın kendi versiyonunu oluşturmak için mutabakat kurallarını uygulayarak her bloğu ve işlemi ayrı ayrı indirip doğrulamaktan oluşur. Amaç basitçe doğrulanmamış verilerin bir kopyasını almak değil, ağın dürüst çoğunluğu olarak tamamen bağımsız bir şekilde aynı sonuca varmaktır.



![Image](assets/fr/092.webp)



### İBH kilometre taşları



Senkronizasyon _**headers-first**_ adımı ile başlar. Düğümünüz birkaç eşten blok başlıkları dizisini talep eder ve her biri için Proof of Work, zorluk ayarı, sözdiziminin yanı sıra Timestamp ve sürüm numarası kurallarını doğrular. Kısacası, alınan her başlığın mutabakat kurallarına uygun olmasını sağlar.



![Image](assets/fr/093.webp)



Bir hatırlatma olarak, bir Bitcoin bloğu 80 baytlık bir başlık ve bir işlem listesinden oluşur. Bloğun parmak izi, 6 alan içeren bu başlığa çift SHA-256 Hash uygulanarak elde edilir:




- versiyon
- Önceki bloğun Hash'i
- İşlemlerin Merkle Root
- Timestamp (önceki 11 bloğun medyan süresinden daha fazla)
- zorluk hedefi
- Nonce



![Image](assets/fr/094.webp)



İşlemler bir Merkle Tree'e işlenir. Bu, büyük bir veri kümesini (bu durumda, bloktaki tüm işlemler), hash'lerini ikişer ikişer tek bir "köke" toplayarak özetleyen ve böylece bir öğenin kümeye ait olduğunu kanıtlayan (ve herhangi bir değişikliği tespit eden) bir yapıdır. Bu şekilde, bir işlemde yapılan herhangi bir değişiklik Merkle Tree'in kökünü ve dolayısıyla blok başlığının parmak izini de değiştirir. SegWit, coinbase'e yerleştirilen çerezler (imzalar) için ayrı bir ek Commitment getirmiştir.



![Image](assets/fr/095.webp)



Bu _**headers-first**_ adımı, düğümün en çok iş yapılan şubeyi (blok sayısına bakılmaksızın) belirlemesini sağlar, bu da Bitcoin düğümlerinin senkronize olduğu şubedir. Bu şube belirlendikten sonra, düğüm blokların içeriğini birkaç bağlantıdan paralel olarak indirir, ardından her işlemi doğrular: format, komut dosyalarının geçerliliği (`assumevalid=1` hariç), miktarlar ve çift harcama olmaması. Her başarılı kontrolde, harcanmamış coinlerin (UTXO seti) mevcut durumu `chainstate/` veritabanında güncellenir: harcanan çıktılar kaldırılırken, yeni geçerli çıktılar eklenir.



Öte yandan Mempool yalnızca zincirin ucuna yaklaşıldığında devreye girer: düğüm geç kaldığı sürece depolayacak bekleyen işlemi yoktur.



IBD tamamlandıktan sonra düğüm normal aşamasına geçer: yeni blokları yayınlandıkça doğrular, Mempool'i aktarım kurallarına göre bekleyen işlemlerle korur, işlemleri ve blokları aktarır ve herhangi bir zincir yeniden düzenlemesini yönetir.



### AssumeValid



Bitcoin core, otonom doğrulama ilkesinin özünü korurken, bir düğümün tamamen çalışır hale gelmesi için gereken süreyi azaltmak üzere tasarlanmış bir mekanizma içerir: AssumeValid.



Assumevalid' parametresi, Hash'ü her yazılım sürümüne entegre edilmiş olan geçmiş bir referans bloğuna dayanmaktadır. IBD sırasında, düğümünüz bu bloğun gerçekten de en çok iş yapılan dalda olduğunu tespit ederse, bu noktadan önceki tüm işlemler için komut dosyası doğrulamasını göz ardı edebilir.



Diğer tüm kurallar (blok yapısı, Proof of Work, boyut limitleri, işlem miktarları, UTXO'lar, vb) tamamen doğrulanmaya devam eder. Yalnızca bu referans bloktan önceki senaryoların hesaplanması göz ardı edilir. İmza doğrulaması CPU yükünün büyük bir kısmını oluşturduğundan IBD'de performans kazancı önemlidir. Bu referans bloğunun ötesinde doğrulama normal durumuna döner.



Bitcoin.conf` dosyasındaki `assumevalid=0` parametresini kullanarak, çok daha uzun bir IBD pahasına bu mekanizmayı devre dışı bırakarak tüm komut dosyalarının tam olarak doğrulanmasını zorlayabilirsiniz.



### AssumeUTXO



`assumeutxo` mevcut başka bir parametredir, ancak `assumevalid`den farklı olarak varsayılan olarak etkinleştirilmemiştir. Bu mekanizma, yazılımın meta verileriyle birlikte UTXO setinin bir anlık görüntüsünü yüklemesini ve başlıkların gerçekten de en çok çalışılan Blockchain'ya götürdüğünü doğruladıktan sonra bunu geçici olarak bir referans durum olarak değerlendirmesini sağlar.



Böylece düğüm, ortak kullanımlar (RPC, cüzdanları bağlama vb.) için hızla çalışır hale gelirken, aynı zamanda arka planda kendi UTXO setinin eksiksiz, doğrulanmış yeniden yapılandırmasını başlatır. Bu aşama tamamlandığında, ilk anlık görüntü yerel olarak yeniden yapılandırılmış durumla değiştirilir. Bu yaklaşım, ikincisinden ödün vermeden hızlı düğüm sağlamayı tam doğrulamadan ayırır.



### Eş keşfi: Düğümünüz Bitcoin ağını nasıl buluyor?



Bir düğüm ilk kez başlatıldığında, henüz herhangi bir eş tanımaz. Ancak, IBD'sini tamamlamak için İnternet'teki diğer Bitcoin düğümlerini bulup başlıkları ve ardından blokları talep etmesi gerekir. Bu bağlantıları başlatmak için Bitcoin core önceliklendirilmiş bir mantık izler.



![Image](assets/fr/096.webp)



Düğüm zaten kullanıldıktan sonra yeniden başlatıldığında, Core ilk olarak `anchors.dat` dosyasında saklanan bilgilerle, kapatılmadan önce kaydedilen giden eşlere yeniden bağlanmayı dener. Ardından, onlara yeniden bağlanmak için daha önce karşılaşılan eşlerin listesini saklayan IP Address kitabına **`peers.dat`** başvurur. Bu sadece Core tarafından güncellenen ve saklanan yerel bir dosyadır. Öte yandan, yeni başlatılan bir düğüm için bu 2 dosya boştur, çünkü henüz diğer Bitcoin düğümleriyle hiç iletişim kurmamıştır.



Bu durumda, yazılım _**DNS tohumlarını**_ sorgular. Bunlar, aktif olduğu varsayılan düğümlerin IP adreslerinin bir listesini döndüren [tanınmış ekosistem geliştiricileri tarafından tutulan sunuculardır](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp). Bu adresler yeni düğümün ilk bağlantılarını başlatmasını ve IBD'den gerekli verileri talep etmesini sağlar. İşte bugüne kadar aktif olan *DNS tohumlarının* listesi (Ağustos 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



Vakaların büyük çoğunluğunda, *DNS tohumları* adımı diğer düğümlerle ilk bağlantıları kurmak için yeterlidir. İstisnai olarak, bu sunucular 60 saniye içinde yanıt vermezse, düğüm başka bir yönteme geçer: gW-569'un kodunda _tohum düğümlerinin_ [1.000'den fazla adresten oluşan statik bir liste] (https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) yerleşiktir ve düzenli olarak güncellenir. IP adresi elde etmenin ilk iki yöntemi başarısız olursa, bu son çözüm düğümün daha sonra yeni IP adresleri talep edebileceği bir ilk bağlantı kurar.



![Image](assets/fr/097.webp)



Son çare olarak, belirli bağlantıları zorlamak için `peers.dat` dosyası aracılığıyla IP adreslerini manuel olarak Supply yapabilirsiniz.



Önyükleme yapıldıktan sonra, dahili Address yöneticisi topolojik izolasyon riskini azaltmak için kaynakları çeşitlendirir (ayrı otonom ağlar, clearnet ve Tor'un yanı sıra çeşitli coğrafi alanlar). Düğüm bu giden bağlantıları kurar (kendi seçtiği ve bu nedenle daha güvenli olan bağlantılar).



Düğümünüz açık bir bağlantı noktasını (varsayılan olarak 8333) dinliyorsa, gelen bağlantıları kabul eder. Bunlar, kendi IBD'nize özel bir fayda sağlamadan, yeni düğümler için bir temas noktası sağlayarak ağın genel esnekliğini güçlendirir. Düğümünüz Tor üzerinde çalışıyorsa, mantık aynı kalır, ancak kullanılan adresler `.onion` hizmetleridir.




## Bitcoin düğümünüzün anatomisi


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Düğümünüz ilk senkronizasyonunu tamamladığında, blokları ve işlemleri doğrulamasına, ağ eşlerine hizmet vermesine ve durumunu korurken hızlı bir şekilde yeniden başlatmasına olanak tanıyan birkaç tamamlayıcı veri kümesini yerel olarak depolar. bir düğümde 3 ana tuğla gereklidir:




- gW-402 **bloklar** disk üzerinde depolanır,
- bir anahtar-değer veritabanında tutulan **UTXO seti**,
- ve **Mempool** RAM'de saklanır ve periyodik olarak serileştirilir.



Ek olarak, birkaç yardımcı dosya (eşler, ücret tahminleri, dışlama listeleri, cüzdanlar, vb. Tüm bu dosyaların rolünü keşfedelim.



### Düğümün verileri gerçekte nerede bulunur?



Varsayılan olarak, Bitcoin core verilerini belirli bir çalışma dizinine kaydeder. GNU/Linux altında bu genellikle `~/.Bitcoin/`, Windows altında `%APPDATA%\Bitcoin/` ve macOS altında `~/Library/Application Support/Bitcoin/` dizinidir. Paketlenmiş bir çözüm kullanıyorsanız (örneğin, bir düğüm dağıtımı içinde), bu dizin başka bir yere bağlanmış olabilir, ancak yapısı aynı kalır. Aşağıda açıklanan önemli alt klasörler ve dosyalar hala burada yer almaktadır.



![Image](assets/fr/098.webp)



### Bloklar



Bu nedenle Blockchain bir bloklar koleksiyonudur. Bir Full node bu blokları sıralı düz dosyalar olarak saklar ve hızlı erişim için paralel bir dizin tutar. Gerektiğinde (yeniden düzenleme, Wallet yeniden tarama, eş hizmeti), bu veriler olduğu gibi yeniden okunur.



**Not:** Yeniden düzenleme veya yeniden senkronizasyon, Blockchain'in aynı yükseklikteki rakip blokların varlığı nedeniyle yapısında bir değişikliğe uğradığı bir olgudur. Bu, Blockchain'in bir kısmı daha fazla miktarda birikmiş işe sahip başka bir zincirle değiştirildiğinde gerçekleşir. Bu yeniden senkronizasyonlar, farklı madencilerin neredeyse aynı anda yeni bloklar bulabildiği ve böylece Bitcoin ağını ikiye bölen Bitcoin'nin işleyişinin doğal bir parçasıdır. Bu gibi durumlarda ağ geçici olarak rakip zincirlere bölünebilir. Sonunda, bu zincirlerden biri daha fazla iş biriktirdikçe, diğer zincirler düğümler tarafından terk edilir ve blokları "eski bloklar" veya "yetim bloklar" olarak bilinir Bir zincirin diğeriyle değiştirildiği bu sürece yeniden senkronizasyon denir.



#### Blk*.dat dosyaları (ham blok verileri)



Alınan ve onaylanan bloklar `blocks/` klasöründe saklanan `blkNNNNN.dat` adlı sıralı konteynerlere yazılır. Her dosya maksimum 128 MiB boyutuna ulaşana kadar sırayla doldurulur, bu noktada Core bir sonraki dosyayı açar. İçeride, her blok ağ formatında serileştirilir, öncesinde sihirli bir tanımlayıcı ve bir uzunluk bulunur. Bu organizasyon diske hızlı yazmayı sağlar ve eşleri senkronize etmek için blok hizmetini kolaylaştırır.



![Image](assets/fr/099.webp)



pruned modunda düğüm, disk ayak izini sınırlamak için bu dosyaların yalnızca yakın tarihli bir penceresini tutar. Yapılandırılmış alan hedefine ulaşılır ulaşılmaz en eski `blk*.dat` konteynerlerini silerken, en iyi bilinen zincirle tutarlı kalmak için yeterli geçmişi korur. Dizin ve UTXO seti normal kalarak sonraki işlemlerin ve blokların doğrulanmasını sağlar.



#### Rev*.dat dosyaları (iptal verileri)



Bir yeniden düzenleme sırasında zamanda geriye gidebilmek için, Core her `blk` dosyasına paralel olarak `blocks/` içinde bir `revNNNNN.dat` dosyası kaydeder. Bu dosya, bir bloğun UTXO seti üzerindeki etkisini geri almak için gereken bilgileri içerir: blok tarafından tüketilen her çıktı için, ilgili UTXO'in önceki durumu saklanır (miktar, komut dosyası, yükseklik...). Bir bloğun iptal edilmesi durumunda düğüm, tüm zinciri yeniden taramak zorunda kalmadan önceki durumu hızlı bir şekilde yeniden oluşturabilir.



![Image](assets/fr/100.webp)



#### Blok dizini (bloklar/indeks)



Bir bloğu doğrudan düz dosyalarda aramak çok zaman alıcı olacaktır. Bu nedenle Core, bilinen her blok için Hash, yükseklik, doğrulama durumu, `blk` dosyası ve bulunduğu ofset gibi meta verileri listeleyen `blocks/index/` içinde bir LevelDB veritabanı tutar. Bir eş bir blok talep ettiğinde veya dahili bir bileşenin belirli bir bloğa erişmesi gerektiğinde, bu dizin hızlı erişim sağlar. Bu dizin olmadan çok fazla işlem yapılması gerekecektir.



![Image](assets/fr/101.webp)



#### İsteğe bağlı dizinler (indexes/)



Bazı dizinler isteğe bağlıdır ve disk ayak izini artırdıkları için varsayılan olarak devre dışıdır:




- daha önce bahsettiğimiz `indexes/txindex/`, bir işlem → konum eşleme tablosu sağlayarak, onaylanmış herhangi bir işlemi, onu içeren bloğu bilmeden almayı mümkün kılar. Bu, Wallet dışı `getrawtransaction` tipi RPC sorguları için kullanışlıdır, ancak oldukça pahalıdır.
- ince istemciler için kompakt blok filtreleri (BIP157/158) içerebilen indexes/blockfilter/`. Bu yapılar, dizinleyici düğümünde ek depolama pahasına istemci tarafı doğrulamayı hızlandırır.



### UTXO seti (chainstate)



UTXO (*Harcanmamış İşlem Çıktısı*) modeli, Bitcoin'in muhasebe temsilidir: harcanmamış her çıktı, gelecekteki bir işlem için girdi olarak kullanılabilecek mevcut bir "Coin "dir.



![Image](assets/fr/102.webp)



Belirli bir T anında tüm bu parçaların toplamı UTXO kümesini oluşturur: şu anda mevcut olan tüm parçaların büyük bir listesi. Düğüm, bir işlemin daha önceki bir işlemde kullanılmamış meşru birimleri harcayıp harcamadığına karar vermek için bu duruma başvurur (Double-spending'ten kaçınmak için).



![Image](assets/fr/103.webp)



UTXO seti, kompakt bir LevelDB veritabanı olarak `chainstate/` klasöründe saklanır. Her parça, işlemin Hash'sından türetilen bir anahtarı ve çıktı dizinini aşağıdakileri içeren bir değerle ilişkilendirir: miktar, `scriptPubKey` kilidi, oluşturma bloğunun yüksekliği ve bir coinbase göstergesi.



![Image](assets/fr/104.webp)



Düğüm, sık okuma ve yazma işlemlerini absorbe etmek için LevelDB üzerinde bir bellek önbelleği tutar. Bu önbelleğin boyutunu değiştirmek için `dbcache` parametresi kullanılabilir: ne kadar büyük olursa, IBD ve mevcut doğrulama daha yüksek RAM tüketimi pahasına daha fazla bellek erişiminden yararlanır. Bir Miner tarafından yeni bir blok bulunduğunda, düğüm, blokta yer alan işlemler tarafından harcanan (veya tüketilen) çıktıları UTXO setinden siler ve yeni oluşturulan çıktıları ekler.



Teorik olarak, bir çıktının hiç harcanmadığını kontrol etmek için blok geçmişini yeniden tarayarak bir işlemi doğrulayabiliriz. Ancak pratikte, her yeni işlem için tüm Blockchain'in taranması gerekeceğinden bu çok zaman alıcı olacaktır. Bu nedenle UTXO seti, Double-spending'ün yokluğunu yerel olarak ve makul bir süre içinde kanıtlamak için gereken minimum görünümü sağlar.



UTXO setinin genellikle Bitcoin'ün merkezsizleşmesiyle ilgili endişelerin merkezinde yer aldığını, çünkü boyutunun doğal olarak hızla arttığını unutmayın. Bu kısmen parçaların bölünmesini teşvik eden Bitcoin'ün artan fiyatından, kısmen de sistemin giderek daha fazla benimsenmesinden kaynaklanmaktadır: ne kadar çok kullanıcı varsa UTXO'lara olan talep de o kadar artmaktadır.



![Image](assets/fr/105.webp)



UTXO setinin büyümesi, Bitcoin üzerindeki basit ödeme işlemlerinin yapısından da kaynaklanmaktadır. Gerçekten de, bir ödeme yaptığınızda, girdi olarak tek bir UTXO tüketirsiniz ve çıktı olarak 2 yeni UTXO yaratırsınız (biri ödeme için diğeri Exchange için). Son olarak, CIOH (*Common Input Ownership Heuristic*) adı verilen bir zincir analizi sezgiselliği, Coin konsolidasyonundan kaçınmak için daha fazla teşvik sağlar.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

İşlemleri makul bir sürede doğrulamak için bir kısmının RAM'de tutulması gerektiğinden, UTXO seti bir Full node'un çalışmasını kademeli olarak çok maliyetli hale getirebilir. Bu sorunu çözmek için, başta [Utreexo] (https://planb.network/resources/glossary/utreexo) olmak üzere birkaç öneri zaten mevcuttur.



### Mempool



Mempool, alınmış ancak henüz onaylanmamış geçerli işlemlerin yerel kümesidir. Bir hatırlatma olarak, "onaylanmış bir işlem" geçerli bir bloğa dahil edilmiş bir işlemdir. Her düğüm kendi Mempool'ünü tutar ve bu Mempool ağdaki diğer düğümlerinkinden aşağıdakilere bağlı olarak farklılık gösterebilir:




- gW-614'e `maxmempool` parametresi aracılığıyla tahsis edilen boyut: daha büyük bir Mempool'e sahip bir düğüm, daha küçük bir Mempool'e sahip bir düğümden daha fazla işlem tutabilecektir (ikincisi boşalmadığı sürece);
- gW-433 kuralları: bunlar düğümün aktarım kurallarının bir alt kümesidir ve onaylanmamış bir işlemin Mempool'te kabul edilmesi için karşılaması gereken özellikleri tanımlar;
- işlem süzülmesi: çeşitli faktörler nedeniyle, belirli bir işlem ağın bir kısmına dağıtılmış, ancak henüz başka bir kısmına ulaşmamış olabilir.



Düğüm mempool'larının mutabakat değeri olmadığına dikkat etmek önemlidir. Her düğüm farklı bir Mempool'ye sahip olsa bile Bitcoin mükemmel çalışır. Nihayetinde, yetkili bloklar her zaman Blockchain'ye eklenen bloklardır. Örneğin, bir düğüm başlangıçta Mempool'sindeki belirli bir işlemi reddetse bile (mutabakat kurallarına göre geçerli), sonunda geçerli bir Proof of Work'ya sahip bir bloğa dahil edilirse kabul etmek zorunda kalacaktır. Bunu yapmaz ve mutabakat kurallarına uymasına rağmen bu bloğu reddederse, bir Hard Fork'i, yani tek başına olacağı yeni, ayrı bir Bitcoin'un oluşturulmasını tetikleyecektir.



#### Bellek politikası ve yönetimi



Bir işlem alındığında, Core mutabakat kurallarına (sözdizimi, geçerli komut dosyaları, çift harcama yok, vb.) ve yerel bir politika olan Mempool kurallarına (RBF, minimum ücret eşikleri, `OP_RETURN`deki veri sınırı, vb.) İşlem bu kurallara uyuyorsa bellekte saklanır.



Mempool'in boyutu `Bitcoin.conf' dosyasındaki `maxmempool' parametresiyle sınırlıdır (bu konuda daha fazla bilgi bir sonraki bölümde). Varsayılan olarak sınır 300 MB'tır. Dolduğunda, düğüm dinamik olarak minimum ücret eşiğini yükseltir ve en az kârlı işlemleri önce çıkarır (yani, önce çıkarılması gereken işlemleri tutar). Çok eski olan işlemlerin süresi de yapılandırılmış bir gecikmeden sonra dolabilir.



#### Mempool disk üzerinde kalıcılık



Yeniden başlatmayı hızlandırmak için Core, düğüm kapatıldığında Mempool'in durumunu periyodik olarak `Mempool.dat` dosyasında serileştirir. Bellekte kalan gerçek Mempool'e ek olarak, Core bu `Mempool.dat` dosyasını diskte saklar. Düğüm bir sonraki sefer başlatıldığında, bu anlık görüntüyü yeniden yükler ve geçerli Blockchain için artık geçerli olmayan her şeyi siler.



### Yardımcı dosyalar ve veritabanları



Block/`, `chainstate/` ve `indexes/` ile aynı seviyedeki diğer bazı dosyalar da sistemin düzgün çalışmasına katkıda bulunur:




- `peers.dat`, ilk DNS keşfi, ağ alışverişleri ve manuel eklemelerle beslenen potansiyel eşlerin IP Address defterini tutar. Düğüm başlatıldığında, giden bağlantıları kurmak için bu dosyadan yararlanabilir.
- Düğüm kapatıldığında, `anchors.dat` giden eşlerin adreslerini kaydeder, böylece bir dahaki sefere başlattığınızda onlarla tekrar hızlı bir şekilde iletişim kurmayı deneyebilirsiniz.
- `banlist.json`, düğümün bu belirli eşlerden yeniden bağlanmasını veya bağlantı kabul etmesini önlemek için operatör veya düğüm tarafından karar verilen yerel yasakları (tekrarlanan geçersiz davranış) içerir.
- fee_estimates.dat`, bir işlem oluşturulurken seçilen gecikme hedefleriyle tutarlı ücret oranları önermek için ücret tahmincisi tarafından kullanılan, gözlemlenen onaylara ilişkin zaman ufku istatistiklerini depolar.
- gW-446.conf` düğümünüzün yapılandırma parametrelerini içerir. Burası röle kurallarını ayarlayabileceğiniz yerdir. Bir sonraki bölümde bu konu hakkında daha fazla bilgi vereceğim.
- `settings.json`, `Bitcoin.conf` için ek parametreler içerir.
- debug.log`, bir hata durumunda düğüm etkinliğini anlamak için kullanılabilecek tanılama metin günlüğüdür.
- gW-448.pid` çalışma zamanında süreç tanımlayıcısını saklar ve diğer uygulamaların veya komut dosyalarının bitcoind'i (*Bitcoin daemon*) kolayca tanımlamasına ve gerekirse onunla etkileşime girmesine olanak tanır. Düğüm başlangıcında oluşturulur ve kapatıldığında silinir.
- ip_asn.map`, kova oluşturma ve eş çeşitlendirme (`-asmap` seçeneği) için kullanılan bir IP → ASN eşleme tablosudur (bağımsız sistem).
- onion_v3_private_key`, `-listenonion` seçeneği etkinleştirildiğinde, yeniden başlatmalar arasında sabit bir onion Address tutmak için Tor v3 hizmetinin özel anahtarını saklar.
- i2p_private_key`, I2P üzerinde giden ve muhtemelen gelen bağlantılar yapmak için `-i2psam=` kullanıldığında I2P özel anahtarını saklar.
- .cookie`, çerez kimlik doğrulaması kullanıldığında geçici bir RPC kimlik doğrulama token (başlangıçta oluşturulur, kapanışta silinir) içerir. Bu, örneğin Wallet yazılımını bağlamak için kullanılabilir.
- .lock`, birden fazla örneğin aynı veri dizinine aynı anda yazmasını engelleyen veri dizini kilididir.
- `guisettings.ini.bak`, `-resetguisettings` seçeneği kullanıldığında GUI ayarlarının (*Bitcoin Qt*) otomatik olarak kaydedilmesidir.



Bu BTC 202 kursunun ilk bölümlerinde gördüğümüz gibi, Bitcoin core hem Bitcoin node yazılımı hem de Wallet'tür. Bununla birlikte, Interface'ın temel kalması ve işlevlerinin Sparrow veya Liana gibi modern yazılımlarla karşılaştırıldığında sınırlı olması nedeniyle cüzdanlarınızı yönetmek için tavsiye edeceğim bir çözüm değildir. Core ayrıca cüzdanlarınızı yönetmek için dosyalar da içerir:





- wallets/` bir veya daha fazlasını barındıran varsayılan dizindir;
- `wallets/<name>/Wallet.dat` Wallet'in SQLite veritabanıdır (anahtarlar, tanımlayıcılar, işlem meta verileri, vb.);
- wallets/<name>/Wallet.dat-journal` SQLite geri alma günlüğüdür.



Özetlemek gerekirse, Bitcoin core dosya yapısı şöyledir:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Yeni bir blok için doğrulama yolu



Yeni bir blok aldığında, düğümünüz Proof of Work'i ve daha genel olarak mutabakat kurallarına uygunluğu kontrol eder. Her şey yolundaysa, değişiklikleri işlem işlem UTXO setine uygular: her girişin mevcut UTXO'ları geçerli bir komut dosyasıyla harcayıp harcamadığını kontrol eder, bu UTXO'ları siler ve yeni çıkışları ekler. Her şey geçerliyse, değişiklikler `chainstate/`'e işlenir.



Paralel olarak, geri alma verileri `rev*.dat` dosyasına ve meta veriler `blocks/index/` dizinine yazılır. Blok daha sonra doğru `blk*.dat` dosyasına serileştirilir. Bir yeniden düzenleme durumunda düğüm, terk edilen blokların bağlantısını temiz bir şekilde kesmek, UTXO setini geri yüklemek ve ardından yeni en iyi zincirin bloklarını bağlamak için `rev*.dat` dosyasını tersten okur.





## Bitcoin.conf'u Anlama


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Bitcoin.conf` dosyası Bitcoin core için ana Interface yapılandırma dosyasıdır. Kaynak kodunu yeniden derlemek veya komut satırı değişiklikleri yapmak zorunda kalmadan düğümünüzün davranışını ve parametrelerini ayarlamanıza olanak tanır. Somut olarak, anahtar-değer çiftleri şeklinde yapılandırılmış düz bir metin dosyasıdır, yani dosyanın her satırı belirli bir parametreye (anahtar) ve bu parametreyi ayarlamak için değiştirilebilen ilişkili değerine atıfta bulunur.



Ağ, işlem aktarımı, performans, indeksleme, günlük kaydı ve RPC erişim parametreleri `Bitcoin.conf` dosyasında tanımlanabilir. Ancak, bu yapılandırma dosyası protokolün mutabakat kurallarını asla değiştirmez: yalnızca düğümün yerel politikasını (aktarma kuralları), bağlanma, dizin oluşturma ve hizmetleri sunma şeklini belirler.



### Konum ve öncelik



Varsayılan olarak, `Bitcoin.conf` Bitcoin core veri dizininde bulunur. Bu, önceki bölümde bahsettiğimiz ünlü dizindir. Ancak, Umbrel gibi belirli ortamlar dışında bu dosya Bitcoin core tarafından otomatik olarak oluşturulmaz. Halihazırda mevcut değilse, `Bitcoin.conf` adında bir dosya oluşturarak ve ardından değişikliklerinizi yapmak için bir metin düzenleyicide açarak generate'i kendiniz oluşturmanız gerekir.



Bitcoin.conf`ta tanımlanan parametreler 2 katman tarafından geçersiz kılınabilir:




- `settings.json` (Interface grafikleri veya bazı RPC tarafından dinamik olarak yazılmıştır),
- ve komut satırları aracılığıyla değiştirilen seçenekler.



Bitcoin.conf`ta yapılan herhangi bir değişikliğin etkili olması için düğümün yeniden başlatılması gerektiğini unutmayın.



### Format ve yapı



Bu nedenle `Bitcoin.conf` formatı çok basittir: seçenek başına bir satır, `seçenek=değer` şeklinde. Gereksiz boşluklar ve boş satırlar göz ardı edilir ve kod yorumları `#` ile başlar.



Neredeyse tüm Boolean seçenekleri `no` önekiyle devre dışı bırakılabilir. Örneğin, `listen=0` ve `nolisten=1` sürümüne bağlı olarak eşdeğerdir.



Yapılandırmayı ağa göre bölümlere ayırmak için bölümleri kullanabilirsiniz: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternatif olarak, seçenek adının önüne `regtest.maxmempool=100` ekleyebilirsiniz.



### Bitcoin.conf'un yapabildikleri ve yapamadıkları



Yukarıda açıklandığı gibi, mutabakat kuralları `Bitcoin.conf` içinde yapılandırılamaz, çünkü bu bir Hard Fork yaratabilir. Öte yandan, diğer birçok husus yapılandırılabilir. Akılda tutulması gereken 3 faydalı sınıf vardır:




- Tamamen yerel parametreler. Bunlar yalnızca sizin düğümünüzü etkiler: önbellek boyutu (`dbcache`), pruned modu (`prune`), isteğe bağlı dizinler... Makinenizin performansını etkilerler, ancak ağı etkilemezler.
- Aktarım ve Mempool politikaları. Bunlar düğümünüzün onaydan önce neleri kabul edeceğine, saklayacağına ve aktaracağına karar verir: minimum ücret eşiği (`minrelaytxfee`), Mempool boyutu ve saklama süresi (`maxmempool`, `mempoolexpiry`), işlem değiştirme (RBF)... Bu kurallar mutabakatın bir parçası değildir, bu nedenle iki farklı düğüm farklı politikalara sahip olabilir ve yine de tamamen uyumlu olabilir. Öte yandan, bu parametrelerin Bitcoin ağı üzerinde bir etkisi olacaktır (ilk bölümde açıklandığı gibi, özellikle süzülme teorisi ile).
- Ağ bağlantısı. Bu seçenekler düğümünüzün eşleri nasıl bulacağını, dinleyeceğini, NAT'dan nasıl geçeceğini, Tor veya proxy kullanacağını ya da bant genişliğini nasıl sınırlayacağını belirler. Bunlar topolojinizi şekillendirir ancak işlemlerin aktarımını değiştirmez.



Bu ayrımı anlamak çok önemlidir: bir işlem mutabakat kurallarına uymuyorsa, düğümünüz her durumda bunu reddedecektir. Ancak daha katı bir yerel politika, mutabakat anlamında geçerli olan bir işlemi iletmeyi reddedebilir.



### Ağ ve topoloji



Her şeyden önce, bir Bitcoin düğümünün sahip olabileceği 2 bağlantı türü arasında net bir ayrım yapmak önemlidir:




- Giden bağlantılar, düğümümüz tarafından başka bir düğüme başlatılan bağlantılardır;



![Image](assets/fr/106.webp)





- Başka bir düğüm tarafından bizimkine başlatılan gelen bağlantılar.



![Image](assets/fr/107.webp)



Bu iki bağlantı türü, aynı verileri her iki yönde de mükemmel bir şekilde değiş tokuş edebilir; burada söz konusu olan akış yönünü sınırlamak değil, yalnızca bağlantıyı başlatan taraftaki farklılıktır. Düğümümüzün bakış açısından, giden bağlantılar genellikle daha güvenli kabul edilir, çünkü onları başlatırız ve tam olarak hangi düğüme bağlanacağımızı seçeriz, bu da bağlantının kötü niyetli olma olasılığını azaltır. Varsayılan olarak, Bitcoin core 10 giden bağlantı tutar (8 "*full-relay*" + 2 "*block-relay-only*").



Bir Full node, gelen bağlantıları kabul ederek ağa daha fazla değer katar. Listen=1` parametresi, söz konusu ağın varsayılan 8333 numaralı bağlantı noktasını dinlemeyi etkinleştirerek bu gelen bağlantıların clearnet üzerinden alınmasını sağlar. Bunun çalışması için bu portun yönlendiricinizde de açık olması gerekir. Aksi takdirde, düğümünüz yalnızca giden bağlantılarla çalışmaya devam edecek ve bu da Bitcoin'i kişisel kullanımınız üzerinde hiçbir etkiye sahip olmayacaktır. Gelen bağlantılara izin verip vermeme seçimi size aittir; "en iyi seçim" diye bir şey yoktur



Yönlendiricinizde bir bağlantı noktası açmamayı, ancak yine de gelen bağlantıları kabul etmeyi tercih ediyorsanız, `listenonion=1` parametresini etkinleştirebilirsiniz. Bu, aynı sonucu elde edecektir, ancak yalnızca clearnet yerine Tor ağı üzerinden.



Ağ düzeyinde, ayrıca




- addnode`: olağan keşfe ek olarak iletişim kurulacak dost bir eş ekler (birkaç kez belirtilebilir).
- connect`: bağlantıları sağlanan Address ile sıkı bir şekilde kısıtlar (birkaç kez belirtilebilir). Çekirdek başka hiçbir düğüme bağlanmayacaktır.
- `seednode`: yalnızca bir düğüme bağlanırken Address kitabını doldurmak için kullanılır, ardından bağlantıyı keser.
- `maxconnections`: gelen + giden bağlantılar için global tavanı tanımlar. Varsayılan olarak, bu parametre 125 olarak ayarlanmıştır, yani düğümünüz asla 125'ten fazla bağlantı kabul etmeyecektir.
- maxuploadtarget`: 24 saatlik kayan bir pencere boyunca bant genişliğini sınırlamak için yüklemeleri sınırlar. Bu sınır, temel son Elements'in yayılmasını feda etmez.
- onlynet`: giden bağlantıları yalnızca seçilen ağlarla sınırlar (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Örneğin, düğümünüzün Bitcoin ağına yalnızca Tor üzerinden bağlanmasını istiyorsanız, `onlynet=onion` parametresini etkinleştirebilir ve gelen bağlantıları devre dışı bırakabilirsiniz (veya yalnızca Tor üzerinden bağlantılara da izin verebilirsiniz).
- `dnsseed`: yerel Address havuzunuz düşük olduğunda _DNS tohumlarının_ eşler talep etmesine izin verir veya vermez (varsayılan: `-connect` veya `-maxconnections=0` olmadığı sürece `1`).
- forcednsseed`: stokta zaten adresleriniz olsa bile _DNS tohumlarının_ başlangıçta istenmesini zorlar (öntanımlı: `0`).
- `fixedseeds`: _DNS tohumları_ başarısız olursa veya devre dışı bırakılırsa *seed düğümlerinin* (sabit kodlanmış Address listesi) kullanımına izin ver (varsayılan: `1`).
- `dns`: Genel olarak DNS çözümlemelerini yetkilendirir (örneğin, `-addnode`/`-seednode`/`-connect` için).



Varsayılan olarak, düğümünüz clearnet, Tor ve I2P üzerinden iletişim kurar. Bu, clearnet üzerinde bağlandığı eşlerin Address genel IP'nizi görebileceği ve İSS'nizin muhtemelen bir Bitcoin düğümü çalıştırdığınızı tespit edebileceği anlamına gelir (P2P Transport V2, bir İSS'nin dinlemesini daha zor hale getirse de). Bu mutlaka bir sorun değildir, ancak bu bilgilerin sızmasını önlemek istiyorsanız, düğümünüzü yalnızca Tor ağı üzerinden bağlayabilirsiniz.



Tor'u tam olarak etkinleştirmek için, Bitcoin core'yı yalnızca bu ağı kullanmaya ve gelen bağlantılar için gizli bir hizmet oluşturmaya zorlamanız gerekir (bunları etkinleştirmek istiyorsanız). Bitcoin.conf` dosyasına bu yapılandırmayı eklemeniz gerekir:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Tüm P2P bağlantılarınız Tor üzerinden geçer. Düğümünüz gelen bağlantılar için bir `.onion` Address alır, bu nedenle yönlendiricide hiçbir bağlantı noktasının açılması gerekmez. İSS'niz yalnızca Tor trafiğini görür ve eşleriniz gerçek genel IP Address'inizden habersizdir.



Açıkta DNS çözümlemesinden kaçınmak için yapılandırmanıza `dnsseed=0` ve `dns=0` ekleyebilirsiniz. Daha sonra `.onion` eşlerini `seednode=` veya `addnode=` aracılığıyla manuel olarak sağlamanız gerekecektir, aksi takdirde yeni düğümlerin keşfi zor olacaktır.



Açıkçası, eğer yeni başlayan biriyseniz, tüm bu ağ ayarlarını şimdilik kendi haline bırakmanızı tavsiye ederim. Varsayılan yapılandırma genellikle yeterlidir.



### Mempool ve röle politikası



#### Temel parametreler



Mempool'nizin yönetimi ve onaylanmamış işlemlerin aktarılmasıyla ilgili `Bitcoin.conf` dosyanızda değiştirebileceğiniz temel parametreler şunlardır:





- `maxmempool=<n>`: Yerel Mempool'ün maksimum boyutunu `<n>` megabayt ile sınırlar (varsayılan: `300`). Limite ulaşıldığında, düğümünüz dinamik olarak etkin ücret eşiğini yükseltir ve limitin altında kalmak için en az kârlı işlemlere öncelik verir (mutlak değere değil, ücret oranına göre). Bu ayarı varsayılan olarak bırakabilirsiniz. Tek başınıza Mining kullanıyorsanız ya da Mempool tıkanıklığını daha doğru bir şekilde görmek ve ücret tahminini iyileştirmek istiyorsanız bu ayarı artırmak faydalı olabilir. Tersine, azaltmak RAM'den ve daha az ölçüde diğer sistem kaynaklarından tasarruf sağlayacaktır.





- `mempoolexpiry=<n>`: Mempool'te onaylanmamış işlemler için maksimum bekletme süresi (saat cinsinden, varsayılan: `336`). Bu süreden sonra, yer kalsa bile işlemler kaldırılır.





- `persistmempool=1`: Mempool'nın anlık görüntüsünü dururken kaydeder ve yeniden başlatıldığında yeniden yükler (varsayılan: `1`). Bu, yeniden başlatmadan sonra kurtarmayı hızlandırır ve ağ üzerinden durumu yeniden öğrenme ihtiyacını ortadan kaldırır.





- `maxorphantx=<n>`: Tutulan maksimum yetim işlem sayısı (UTXO setinde henüz görülmemiş UTXO'lardan gelen bağımlı girdiler, varsayılan: `100`). Bu eşiğin ötesinde, önbelleğin kontrolsüz büyümesini önlemek için en eski işlemler silinir.





- blocksonly=1`: Eşlerden alınan onaylanmamış işlemlerin kabulünü ve yeniden iletimini devre dışı bırakır (özel izinler verilmediği sürece). Düğüm artık sadece blokları yükler ve ilan eder. Yerel olarak oluşturulan işlemler hala yayınlanabilir (düğümünüzü Wallet yazılımınızla kullanmak için). Bu, aktarıcı için daha az kullanışlılık ve Mempool'e tamamen yabancılık pahasına da olsa bant genişliği ve RAM gereksinimlerini büyük ölçüde azaltır.





- `minrelaytxfee=<n>`: İşlemlerin düğümün Mempool'ünde kabul edilmediği ve eşlere iletilmediği minimum ücret oranı (BTC/kvB cinsinden) (varsayılan: `0.00001` = 1 sat/vB). Bu değer ne kadar yüksek olursa, düğümünüz düşük maliyetli işlemleri o kadar agresif bir şekilde filtreler.





- `mempoolfullrbf=1`: Değiştirilen işlemde açık RBF sinyali olmasa bile RBF işlemlerini kabul edin. Bu "*full-RBF*" politikası ile, daha yüksek bir ücret oranı sunan bir işlem, diğer değiştirme koşulları karşılanırsa Mempool'deki bir diğerinin yerini alabilir.



Bir hatırlatma olarak, RBF, göndericinin onaylamayı hızlandırmak için bir işlemi daha yüksek ücrete sahip bir işlemle değiştirmesini sağlayan işlemsel bir mekanizmadır. Ücreti çok düşük olan bir işlem bloke kalırsa, gönderici ücreti artırmak için *Replace-by-fee* kullanabilir ve mempool'larda ve madencilerde yedek işlemlerine öncelik verebilir.



#### Gelişmiş ve özel ayarlar



İşte Mempool ve aktarma ilkesi için gelişmiş ayarlar. Yeni başlayan biriyseniz, bu ayarları değiştirmeniz gerekmez:





- datacarrier=1`: Bir `OP_RETURN` çıkışı üzerinden finansal olmayan veri taşıyan işlemlerin aktarılmasına ve (düğüm üzerinden Mining ise) dahil edilmesine izin verir (varsayılan: `1`). Bu parametrenin devre dışı bırakılması, belirli kullanımlarla uyumluluğun azalması pahasına, finansal olmayan veri spam'i için yüzey alanını biraz azaltır. Her durumda, mayınlı `OP_RETURN` yı kabul etmelisiniz.





- `datacarriersize=<n>`: Düğümün ilettiği `OP_RETURN`un maksimum boyutu (bayt cinsinden) (varsayılan: `83`). Bu değerin düşürülmesi `OP_RETURN` üzerinden taşınan yükleri kısıtlar. Bu sınırın Bitcoin core'in gelecekteki bir sürümünde varsayılan olarak kaldırılacağını unutmayın.





- `bytespersigop=<n>`: İmza işlemlerini aktarım sınırı değerlendirmesi için eşdeğer baytlara dönüştüren parametre (varsayılan: `20`). Bu, yerel politika kurallarına göre `sigops` zengin işlemlerin kabulünü etkileyecektir.





- `permitbaremultisig=1`: Bare-Multisig* P2MS işlemlerinin aktarılmasına izin verir (varsayılan: `1`). Bu, bir UTXO üzerinde çoklu imza koşulları oluşturmak için kullanılan en eski komut dosyası şablonudur (2011 yılında Gavin Andresen tarafından icat edilmiştir).





- `whitelistrelay=1`: Beyaz listedeki gelen eşlere otomatik olarak aktarım izni verir (varsayılan: `1`). Bu eşlerin işlemleri, düğümünüz genel aktarım modunda olmasa bile aktarım tarafından kabul edilir.





- `whitelistforcerelay=1`: Varsayılan izinlere sahip beyaz listedeki eşlere "*forcerelay*" izni atar (varsayılan: `0`). Düğüm daha sonra Mempool'de zaten mevcut olsalar bile işlemlerini iletir, böylece artıklık önleme mekanizmalarını atlar.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Bir Interface veya Address aralığını bağlar ve ilgili eşlere ince taneli izinler atar: `relay`, `forcerelay`, `Mempool` (Mempool içerik isteği), `noban`, `download`, `addr`, `bloomfilter`. Bu, güvenilen eşlere (ağ geçitleri, LAN'lar ve dahili hizmetler gibi) ayrıcalıklı muamele sağlamak için yararlı olabilir.





- peerbloomfilters=1`: Filtrelenmiş blokları/işlemleri ince istemcilere sunmak için Bloom filtreleri (BIP37) desteğini etkinleştirin (varsayılan: `0`). Uyarı: Bu, kaynaklarınız üzerindeki yükü artırır.





- peerblockfilters=1`: BIP157 (*Neutrino*) kompakt filtrelerini eşlere sunar (varsayılan: `0`).





- `blockreconstructionextratxn=<n>`: Kompakt blokları yeniden oluşturmak için bellekte tutulan ek işlem sayısı (varsayılan: `100`). Kompakt senkronizasyonlar sırasında yeniden yapılandırmaların başarısını biraz bellek pahasına artırır.



Bir hatırlatma olarak, tüm bu röle kurallarının geçerli bir blokta yer alan işlemlerin geçerliliği üzerinde hiçbir etkisi yoktur. Bunlar röleye katkınızı ayarlamanıza, kaynaklarınızı korumanıza ve düğümünüzü kısıtlı ortamlarda öngörülebilir hale getirmenize hizmet eder, ancak mutabakat kurallarına uyan blokları reddetmenize asla izin vermez.



### Cüzdanlar



Cüzdanlarınızın yönetilme şeklini `Bitcoin.conf` dosyasından da ayarlayabilirsiniz. Wallet'i doğrudan Core'da kullanmıyorsanız, bunun yerine Sparrow veya Liana gibi harici bir yönetim yazılımı kullanıyorsanız, bu parametreler çok az önem taşıyacaktır:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Alım için Wallet tarafından oluşturulan adreslerin biçimini tanımlar.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Exchange Address biçimini zorla (tek bir ödemede bir girdinin geri kalanı).





- `Wallet=<path>`: Başlangıçta mevcut bir Wallet'yi yükler (birden fazla cüzdan yüklemek için tekrarlanabilir).





- `walletdir=<dir>`: Cüzdanları içeren dizin (varsayılan: varsa `<datadir>/wallets`, yoksa `<datadir>`). Cüzdanları ayrılmış veya şifrelenmiş bir birimde saklamak istiyorsanız bu yararlı olabilir.





- `walletbroadcast=1`: Yüklü cüzdanlar tarafından oluşturulan işlemleri otomatik olarak yayınlar (varsayılan: `1`). Yayını başka bir kanal üzerinden yönetmek istiyorsanız `0` olarak ayarlayın.





- `walletrbf=1`: Tüm işlemlerde RBF sinyali vermek için RBF tercihini etkinleştirir (varsayılan: `1`). Engellenen bir işlem durumunda ücretleri daha sonra artırmanıza olanak tanır.





- `txconfirmtarget=<n>`: İşlem için onay hedefi (blok sayısı olarak, varsayılan: `6`). Wallet, işlemin bu blok sayısı içinde onaylanması için ücreti otomatik olarak ayarlayacaktır.





- `paytxfee=<amt>`: Wallet işlemlerine uygulanan sabit ücret oranı (BTC/kvB). Genel olarak kaçının: `txconfirmtarget` aracılığıyla uyarlanabilir tahmin kullanın.





- fallbackfee=<amt>`: Tahmin edicinin verisi biterse kullanılan geri dönüş oranı (BTC/kvB) (varsayılan: `0,00`). 0 olarak ayarlamak geri dönüşü tamamen devre dışı bırakır.





- `mintxfee=<amt>`: Wallet'in işlem oluşturması için minimum eşik (BTC/kvB) (varsayılan: `0.00001`). Wallet bu eşiğin altında bir işlem oluşturmayı reddedecektir.





- `maxtxfee=<amt>`: Bir Wallet işlemi için toplam ücretlerde mutlak üst sınır (varsayılan: `0,10` BTC). Gereksiz yere bitcoinleri yok edecek anormal yüksek ücretlere karşı koruma sağlar.





- `avoidpartialspends=1`: Kısmi harcamaları önlemek için UTXO'ları Address kümelerine göre seçer.





- `spendzeroconfchange=1`: Onaylanmamış bir UTXO Exchange'ün yeni bir işlemde girdi olarak yeniden kullanılmasına izin verir (varsayılan: `1`).





- `consolidatefeerate=<amt>`: Wallet'nın konsolide etmek için gerekenden daha fazla girdi eklemekten kaçındığı maksimum oran (BTC/kvB). Bu, düşük fiyatlarda fırsatçı konsolidasyonlara izin verir ve maliyetler yüksek olduğunda maliyetleri azaltır.





- `maxapsfee=<n>`: Wallet'nin "*kısmi harcamalardan kaçın*" seçeneğini etkinleştirmek için ödemeyi kabul ettiği ek ücretler için bütçe (BTC, mutlak değer).





- `discardfee=<amt>`: Exchange'i ücrete ekleyerek atma toleransınızı gösteren oran (BTC/kvB). Bu oranda değerinin üçte birinden fazlasına mal olacak çıktılar atılır.





- `keypool=<n>`: Önceden oluşturulmuş Address havuzunun boyutu (varsayılan: `1000`). Çok küçük değerler eksik geri yükleme riskini artırır.





- `disablewallet=1`: Bitcoin core'ı Wallet alt sistemi olmadan başlatır ve ilişkili RPC'leri devre dışı bırakır. Düğüm yalnızca doğrulama/serbest bırakma için kullanılıyorsa saldırı yüzeyini ve ayak izini azaltır.



### Depolama, indeksleme ve performans



Yapılandırma dosyası, makinenizle ilgili parametreleri ayarlamanıza da olanak tanır. Bu, özellikle sınırlı kaynaklarınız veya tam tersine büyük miktarda kullanılabilir kapasiteniz varsa önemli olabilir:





- `datadir=<dir>`: Bitcoin core'nin ana veri dizinini ayarlar.





- `blocksdir=<dir>`: Blok dosyalarının (`blocks/blk*.dat` ve `blocks/rev*.dat`) konumunu `datadir`den ayırır. Bu, örneğin durum tabanını (`chainstate/`) daha hızlı bir ortamda tutarken blok arşivini farklı bir birime yerleştirmek için yararlı olabilir.





- dbcache=<n>`: Blok indeksi ve `chainstate` tarafından kullanılan veritabanı önbelleğine (*LevelDB*) `<n>` MiB ayırır (varsayılan: `450`). Değer ne kadar yüksek olursa, daha yüksek RAM tüketimi pahasına IBD ve mevcut doğrulama o kadar hızlı olur.





- `prune=<n>`: Blok dosyalarının budanmasını etkinleştirir ve MiB cinsinden bir disk alanı hedefi belirler (varsayılan: `0` = devre dışı; `1` = RPC aracılığıyla manuel budama; `>=550` = hedefin altında otomatik budama). Txindex=1` ile uyumsuz. Düğüm tamamen doğrulayıcı bir düğüm olarak kalır, ancak artık eski geçmişi sağlayamaz. Bu seçenek özellikle disk alanınız sınırlıysa, örneğin ev bilgisayarınıza bir düğüm kurarken kullanışlıdır.





- txindex=1`: Onaylanmış işlemlerin küresel bir dizinini oluşturur ve korur. Belirli sorgular (`getrawtransaction` non-Wallet) ve keşif amaçları için gereklidir, ancak disk ayak izini önemli ölçüde artırır. pruned modu ile uyumsuzdur.





- `assumevalid=<hex>`: Geçerli olduğu varsayılan bir bloğu belirtir ve ataları için kod kontrollerini atlamanıza izin verir (her şeyi kontrol etmek için `0` olarak ayarlayın). Daha fazla bilgi için önceki bölüme bakın.





- `reindex=1`: Diskteki `blk*.dat` dosyalarından blok dizinlerini ve durumu (`chainstate`) yeniden oluşturur. Ayrıca isteğe bağlı etkin dizinleri de yeniden oluşturur. Bu, bozuk bir veritabanını onarmak veya ağır indeksleri temiz bir şekilde etkinleştirmek/devre dışı bırakmak için kullanılması zaman alan bir işlemdir.





- `reindex-chainstate=1`: Geçerli blok dizininden yalnızca `chainstate`i yeniden oluşturur. Blok dosyaları sağlıklı olduğunda tercih edilir.





- blockfilterindex=<type>`: İnce istemciler (BIP157/158) ve bazı RPC'ler tarafından kullanılan kompakt blok filtrelerinin (örn. `basic`) indekslerini tutar. Varsayılan olarak devre dışıdır (`0`). Ek disk alanı ve indeksleme süresi tüketir.





- `coinstatsindex=1`: Gettxoutsetinfo` çağrısı tarafından işletilen bir UTXO set istatistik dizinini korur. Denetimler ve ölçümler için kullanışlıdır, maliyetli yeniden hesaplama ihtiyacını ortadan kaldırır. Varsayılan olarak devre dışıdır.





- `loadblock=<file>`: Başlangıçta blokları harici bir `blk*.dat` dosyasından içe aktarır. Başlatma işlemini hızlandırmak için geçmişi çevrimdışı bir kaynaktan (yerel kopya, harici medya) önceden yüklemek için kullanılır.





- `par=<n>`: Kod doğrulama iş parçacıklarının sayısını ayarlar (`-10` ile `15` arasında, `0` = otomatik, `<0` = bu sayıda çekirdeği boş bırakır). Doğrulama sırasında CPU paralelliğini ayarlamanıza izin verir. Otomatik mod çoğu durumda uygundur.





- `debuglogfile=<file>`: Debug.log` günlüğünün konumunu belirtir.





- `shrinkdebugfile=1`: Başlangıçta `debug.log` dosyasının boyutunu azaltır (varsayılan: `-debug` etkin değilken `1`).





- `settings=<dosya>`: Dinamik ayar dosyasının yolu `settings.json`.



### RPC erişim ve operasyonel güvenlik



Son olarak, `Bitcoin.conf` dosyası da düğümünüz için erişim parametrelerini yapılandırmanıza olanak tanır. Bu ayarlar konusunda dikkatli olun, özellikle de yeni başlıyorsanız: güvenlik açıklarına neden olabileceğinden, sonuçlarını tam olarak anlamadan bunları değiştirmekten kaçının.





- sunucu=1`: JSON-RPC sunucusunu etkinleştirir. bitcoind`i `bitcoin-cli` veya üçüncü taraf bir uygulama aracılığıyla kullanıyorsanız gereklidir. Herhangi bir API'yi açığa çıkarmayan veya zaten bir Electrum sunucusu kullanan, yalnızca doğrulama yapan bir düğümde devre dışı bırakın (`0`).





- rpcbind=<addr>[:port]`: RPC sunucusu Address/port'u dinliyor. Varsayılan olarak, dinleme yalnızca yerel olarak yapılır (`127.0.0.1` ve `::1`). Eğer `rpcallowip` de tanımlanmamışsa bu parametre yok sayılır. Interface'ü açıkça kısıtlamak için kullanın.





- `rpcport=<port>`: RPC portu (varsayılan: Mainnet üzerinde `8332`, Testnet üzerinde `18332`, bookmark üzerinde `38332`, regtest üzerinde `18443`).





- `rpcallowip=<ip|cidr>`: Belirli bir IP veya alt ağdan RPC istemcilerine izin verir (tekrarlanabilir). API'yi yalnızca güvenilir bir segmente (LAN/VPN) göstermek için `rpcbind` ile birlikte kullanın.





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Önerilen RPC kimlik doğrulama yöntemi (karma parola). Birden fazla girişe izin verir ve bir sırrın açık metin olarak saklanmasını önler.





- `rpccookiefile=<path>`: Kimlik doğrulama çerezinin yolu (varsayılan: `datadir/` altındaki `.cookie` dosyası). Bu, kalıcı parolaları yönetmeden aynı kullanıcı tarafından yerel erişim için kullanılır. Örneğin, Liana Wallet'ü aynı makinedeki Bitcoin core'nize bağlamak için kullanabilirsiniz.





- rpcuser=<user>` / `rpcpassword=<pw>`: Düz metin parolası ile klasik RPC kimlik doğrulaması. Bunu `rpcauth` veya bir çerez lehine kullanmaktan kaçının.





- `rpcthreads=<n>`: RPC çağrılarına hizmet edecek iş parçacığı sayısı (varsayılan: `4`). İzleme/harici araç tarafında yüksek çağrı piklerine sahipseniz artırın.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Yetkili API'lerin beyaz listesi. Erişilebilir yöntemleri kısıtlayarak saldırı yüzeyini azaltır.





- rpcwhitelistdefault=1|0`: Varsayılan beyaz liste davranışı: etkinleştirilmişse ve bir beyaz liste kullanılıyorsa, listelenmemiş çağrılar reddedilir. Bu ayrıca, hiçbir şey açıkça listelenmediği sürece varsayılan bir boş kümeyi (hiçbir çağrıya izin verilmez) zorlayabilir.





- rest=1`: Genel REST API'yi etkinleştirin (varsayılan olarak devre dışıdır). Yalnızca güvenilir bir ağda ifşa edilecek (JSON-RPC ile aynı dikkat).





- `conf=<dosya>`: Yalnızca komut satırında salt okunur bir yapılandırma dosyası belirtir. Operasyon tarafında bir yürütme profilini dondurmak (değişmez) için kullanışlıdır.





- `includeconf=<dosya>`: Ek bir yapılandırma dosyası yükler (`datadir/` dosyasına göre yol). Rollerin ayrılmasına izin verir: ortak temel + hassas yerel aşırı yük.





- gW-769=1` / `daemonwait=1`: bitcoind`i arka planda başlatır ve `daemonwait` ile devretmeden önce başlatmanın bitmesini bekler. Bu, denetleyicilerle (systemd, runit) entegrasyonu kolaylaştırır.





- `pid=<dosya>`: PID dosyasının konumu.





- `sandbox=<log-and-abort|abort>`: Deneysel sistem çağrıları kum havuzunu etkinleştirir: yalnızca beklenen sistem çağrılarına izin verilir.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Başlangıçta veya kapanışta bir komut çalıştırır.





- `alertnotify=<cmd>`: Bir uyarı alındığında bir komutu tetikler.





- `blocknotify=<cmd>`: Her yeni blok için bir komut çalıştırır.





- `debug=<category>|1` / `debugexclude=<category>`: Ayrıntılı günlük kategorilerini etkinleştirir/devre dışı bırakır (örneğin `net`, `Mempool`, `RPC`, `validation`...).





- logips=1`: IP adreslerini günlüğe kaydeder.





- logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Günlüklere sırasıyla kaynak konumları, iş parçacığı adları ve kesin zaman damgaları ekler.





- `printtoconsole=1`: İzleri/hataları konsola gönderir (*stdout*).





- help-debug=1`: Hata ayıklama seçeneği yardımını görüntüler ve çıkar.





- `uacomment=<cmt>`: User-Agent P2P'ye bir yorum ekler.



Artık yapılandırma parametrelerinin çoğunu listelemeyi bitirdik. Bu `Bitcoin.conf` dosyası düğümünüzün gerçek kontrol panelini oluşturur: ağ yapılandırmasını, Mempool yönetimini, disk ve bellek kullanımını, indekslemeyi ve genel yönetimi tanımlar. Bu dosya hakkında daha fazla bilgi edinmek ve ihtiyaçlarınıza uygun bir dosya oluşturmak isterseniz [Jameson Lopp's generator] (https://jlopp.github.io/Bitcoin-core-config-generator/) adresini kullanmanızı tavsiye ederim.



BTC 202 kursunun sonuna geldik, bu kurs sayesinde sadece node'ların nasıl çalıştığını ve sistem içinde nasıl etkileşime girdiklerini anlamakla kalmayacak, aynı zamanda kendi node'unuzu da kurabileceksiniz. Artık kendi öz saklama Wallet'inize sahip, işlemlerinizi kendi node'unuz üzerinden yayınlayan egemen bir Bitcoin kullanıcısısınız. Tebrikler!



Artık kursun son bölümüne geçebilir, burada BTC 202'yi değerlendirebilir ve ardından ele alınan tüm kavramlara hakim olduğunuzu kontrol etmek için diplomanızı alabilirsiniz.



Artık önünüzde birkaç seçenek var. Bir sonraki mantıklı adım, off-chain işlemleriniz için tamamen bağımsız olmanızı sağlayacak şekilde kendi Lightning düğümünüzü kurmaktır. Bu, 2025 sonbaharında Plan ₿ Network üzerine yayınlanacak olan gelecek bir kursun konusu olacaktır.



Bu arada, sizi Bitcoin kullanımınızda gizlilik koruma ilkelerini anlamanızı ve bu konuda uzmanlaşmanızı sağlayacak BTC 204 eğitimini keşfetmeye davet ediyorum:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Son bölüm


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Yorumlar & Derecelendirmeler


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Final Sınavı


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Sonuç


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>