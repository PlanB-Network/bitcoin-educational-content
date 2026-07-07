---
name: İlk Lightning düğümünüzü kurma
goal: Bir Lightning düğümünü anlama, kurma, yapılandırma ve kullanma
objectives: 


  - Lightning düğümünün rolünü ve amacını anlayın.
  - Mevcut farklı yazılım çözümlerini tanımlayın.
  - Bir Lightning düğümü (LND) kurun ve yapılandırın.
  - Bir gider hesabı bağlayın.
  - Lightning düğümü kullanmanın risklerini bilin.


---

# Lightning'de özerkliğe doğru ilk adımınız



İlk sats'ünüzü zaten aldınız, öz saklama fonlarınızı güvence altına aldınız ve on-chain kullanımınızda egemen olmak için bir Bitcoin düğümü konuşlandırdınız. Bir sonraki adım Lightning'de de aynı özerkliği kazanmak: bu kursun amacı da tam olarak bu.



LNP202 orta düzey kullanıcılara yöneliktir ve ilk Lightning düğümünüzün kurulumunda ileri düzey teknik beceri gerektirmeden size adım adım rehberlik eder.



LND'yi Umbrel'ya nasıl kuracağınızı, kanallarınızı nasıl açacağınızı ve yöneteceğinizi, düğümünüzü nasıl denetleyeceğinizi ve mobil bir wallet'i nasıl bağlayacağınızı öğreneceksiniz, böylece fonlarınız üzerinde tam kontrol sahibi olurken saklama amaçlı bir wallet ile karşılaştırılabilir bir deneyimin keyfini çıkarabilirsiniz.



+++


# Giriş


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Kursa genel bakış


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202, kendi düğümünüzü işleterek Lightning'de otonom olmanızı sağlamak için tasarlanmış uygulamalı bir kurstur. Amaç basittir: halihazırda mevcut bir Bitcoin düğümü ile başlayın, LND'i Umbrel'a yerleştirin, düzgün bir şekilde güvence altına alın, ilk kanallarınızı açın ve yönetin, ardından düğümünüzü mobil bir wallet'dan günlük olarak kullanın. Bu eğitimde BTC 202'yi zaten almış olduğunuzu varsayıyorum, çünkü Bitcoin üzerindeki Umbrel düğümünüzün yerinde ve senkronize olduğunu varsayıyorum. Burada bir Bitcoin düğümünün nasıl kurulacağının üzerinden geçmeyeceğiz.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Lightning'in iç mekaniğini daha iyi anlamak için LNP 201 kursu da şiddetle tavsiye edilir, ancak bu kurs için bir ön koşul değildir:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bu LNP202 kursunun ilk bölümünde Lightning düğümünün gerçekte ne olduğunu, basit bir wallet'ten farkını ve sats'nızı güvenilir bir üçüncü tarafa devretmeden Lightning'i kullanmanın tek yolunun neden kişisel bir düğüm işletmek olduğunu inceleyeceğiz. Bu bölüm stratejik bir seçimle sona eriyor: en basit yaklaşımlardan bu kursta uygulayacağımız klasik Lightning düğümüne kadar hangi çözümün sizin için doğru olduğu.



Kursun 2. Bölümünde, LND'u Umbrel üzerine kuracak, ardından en maliyetli hataları önleyen unsurları uygulamaya koyacaksınız: gerçekçi bir yedekleme stratejisi ve bir gözetleme kulesi aracılığıyla hileye karşı koruma. Bu temel unsurları yerine getirdikten sonra ilk kanalınızı açacak ve böylece kendi altyapınızla Lightning üzerinden ödeme yapmaya başlayabileceksiniz.



Gördüğünüz gibi: bu LNP202 kursunda, orta düzey kullanıcılar için uygun hale getirmek için klasik komut satırı yaklaşımı yerine Umbrel aracılığıyla tak ve çalıştır modunda bir Lightning düğümü kuracağız. Komut satırı kurulumunu tercih ediyorsanız, aşağıdaki öğreticiyi izlemenizi tavsiye ederim. Diğer, daha gelişmiş, komut satırı odaklı Lightning kursları da hazırlık aşamasındadır.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Bölüm 3 daha sonra sizi çalışan bir düğümden nasıl kontrol edeceğinizi bildiğiniz bir düğüme götürecektir. Lightning düğümü operatör profilinizi (tüketici, tüccar veya yönlendirici) belirleyerek başlayacak, ardından kanallarınızı takip etmek ve topolojinizde temiz bir şekilde hareket etmek için eksiksiz bir yönetim yazılımı paketiyle başa çıkacaksınız. Son olarak, çok önemli bir Lightning noktasını ele alacaksınız: ister ücretli ister işbirlikçi çözümler yoluyla olsun, gelen likiditenin nasıl elde edileceği.



Bölüm 4 günlük kullanıma odaklanacaktır. Düğümünüz ile bir mobil müşteri arasında bir bağlantı kuracaksınız, böylece kendi gözetiminizden vazgeçmeden akıllı telefonunuzdan ödeme ve tahsilat yapabileceksiniz. Önce *Tailscale* aracılığıyla bir ağ yaklaşımına, ardından *Nostr Wallet Connect* aracılığıyla bir protokol yaklaşımına, ilgili avantajları ve ödünleriyle birlikte bakacağız. Kurs, hem operasyonel hem de pedagojik olarak kendi gözetiminizi sürdürmek için size doğru alışkanlıkları kazandıracak son bir bölümle sona erecek.



Bu LNP202 kursunu doğru sırayla takip ederseniz, sonunda Lightning düğümünüz için günlük kullanım için işlevsel ve her şeyden önce kontrol altında olan eksiksiz bir yapılandırmaya sahip olacaksınız.




## Lightning düğümlerini anlama


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Kendi düğümünüzü başlatmadan önce, bu bölüm [Lightning Network](https://planb.academy/resources/glossary/lightning-network)'nın arkasındaki temel teoriyi kısaca gözden geçirmektedir. İlgili mekanizmaları anlamak gerçekten de önemlidir, çünkü bu sayede riskleri belirleyebilir ve bunları sınırlandırmak için iyi uygulamalar benimseyebilirsiniz. Ancak bu kursun ana amacı bu olmadığı için burada ayrıntıya girmeyeceğim. Konuyu daha derinlemesine incelemek isterseniz, Fanis Michalakis'in bu alanda bir referans olan LNP 201 kursuna başvurmanızı şiddetle tavsiye ederim:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Lightning düğümü nedir?



Temellere geri dönelim: bir node'un ne olduğunu tanımlamadan önce, Lightning Network'in ne olduğunu anlamamız gerekir. Bitcoin'un üzerine inşa edilmiş, hızlı (neredeyse anında sonuçlanan) ve genellikle ucuz olan zincir dışı BTC işlemlerini mümkün kılmak için tasarlanmış bir üst katman protokolüdür. "Zincir dışı", Lightning üzerinde gerçekleştirilen işlemlerin ana Bitcoin blok zincirinde görünmesinin amaçlanmadığı anlamına gelir. Lightning aynı zamanda Bitcoin'un artan kullanımına ve sistemin ölçeklenebilirliği konusunda endişelere yol açan zincir üzerindeki tıkanıklığa kısmi bir yanıttır.



Lightning, faaliyet göstermek için katılımcılar arasında, işlemlerin Bitcoin blok zincirine tek tek kaydedilmesine gerek kalmadan neredeyse anında ve genellikle minimum ücretlerle gerçekleştirilebileceği ödeme kanallarının açılmasına dayanır. Bu kanallar çok uzun bir süre açık kalabilir ve yalnızca açılıp kapandıklarında zincir üzerinde işlem yapılmasını gerektirir.



Bir Lightning düğümü, Lightning ağında kanallar açan ve diğer düğümlerle ödeme yapan bir katılımcıdır. Somut olarak, bir Lightning düğümü, bir bilgisayarda çalışan ve Lightning Network protokolünü uygulayan bir yazılım parçasıdır. Örnekler arasında LND, Core Lightning veya Eclair sayılabilir. Bu yazılımın ana rolü şunlardır:




- ana blok zincirinden bilgi almak için bir Bitcoin düğümüne bağlanır;
- diğer düğümlerle çift yönlü ödeme kanalları oluşturabilir ve yönetebilir;
- tüm Lightning ağı ile mesaj alışverişinde bulunur.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: önemli bir ayrım



Bitcoin'da (onchain), "*wallet*" özel anahtarlarınızı yöneten, UTXO'lerinizden bakiyenizi hesaplayan ve işlemlerinizi oluşturan yazılımı ifade eder. Bu wallet, kendi Bitcoin düğümünüze veya bir başkasınınkine dayalı olabilir, ancak bugün, düğümün rolü ile zincir üzerindeki wallet'nin rolü açıkça farklıdır.



Lightning'de bu tür kelimeleri karışıklık yaratmadan yeniden kullanmak daha zordur. "*Lightning wallet*" terimi oldukça belirsizdir, çünkü gerçekte, bir düğüme dayanmadığı sürece, gerçekten kendi kendine emanet edilen bir Lightning wallet diye bir şey yoktur. Bu nedenle sadece iki durum mümkündür:



- Gerçek bir Lightning düğümüne sahip olmak için (yani gözetim altında olmayan): kullandığınız yazılım (örneğin Phoenix gibi bir mobil uygulama veya Umbrel üzerinde bir LND örneği) aslında bir düğüm çalıştırıyor ve bitcoinlerinizi almak için anahtarlara sahipsiniz. Bu durumda, "*Lightning wallet*" gerçekten de ister gömülü ister uzak olsun, bir Lightning düğümünün üzerindeki bir kullanıcı arayüzüdür.



- Bir saklama hizmeti kullanmak için: Lightning'de size sats'da bir bakiye gösteren bir uygulama kullanıyorsunuz, ancak arka planda fonlar bir sağlayıcının düğümünde (örneğin Wallet of Satoshi). Ne anahtarlara ne de kanalların kontrolüne sahipsiniz. Bakiyeniz yalnızca şirketin veri tabanındaki bir muhasebe girdisidir. Bu durum, tüm riskleriyle birlikte bitcoinlerinizi bir borsa platformunda bırakmaya benzer. Bu durumda, "*Lightning wallet*" yalnızca gerçek bir Lightning düğümü çalıştıran bir operatör tarafından yönetilen bir hesaba erişimdir.



Yani Lightning'de ikisinin arası yoktur: ya bir node'unuz vardır (gömülü bile olsa), yani kendi kendinizin velayetindesinizdir ya da yoktur, yani bir şirket sats'inizin sahibidir. Ancak ilerleyen bölümlerde göreceğimiz gibi, bu iki kullanımı ayırt etmek bazen zor olabilir. Örneğin, Phoenix gerçek bir Lightning düğümü içeren bir mobil uygulamadır, ancak işleyişinin tüm karmaşıklığı neredeyse tamamen gizli olduğundan kullanıcı bunun farkında olmayabilir.



### Lightning Network'un nasıl çalıştığına dair bir hatırlatma



Bu bölümde size Lightning'in nasıl çalıştığına dair hızlı bir hatırlatma yapacağım. Bir kez daha, teorik kavramların daha derinlemesine bir sunumunu istiyorsanız, sizi özel LNP 201 kursuna göz atmaya davet ediyorum.



#### Ödeme kanalları: açma, güncelleme ve kapatma



Lightning ağının kalbi çift yönlü ödeme kanallarına dayanmaktadır. Bir kanal açılabilir (yani oluşturulabilir), Lightning işlemleri gerçekleştikçe güncellenebilir ve son olarak kapatılabilir. Zincir içi bakış açısından, bir kanal 2/2 çoklu imza çıktısından başka bir şey değildir.



![Image](assets/fr/002.webp)



Lightning'in bakış açısından, likiditenin iki katılımcı arasında bölündüğü bir ödeme kanalıdır.



![Image](assets/fr/003.webp)





- Kanal açma:**



İki düğüm bir kanal açmaya karar verir. Bunlardan biri *funding transaction* adı verilen bir zincir içi işlemle bitcoinleri taahhüt eder. Bu işlem, 2'ye 2 çoklu imza komut dosyasına dayalı bir çıktı oluşturur, yani bu fonların Bitcoin'de harcanması için kanaldaki her iki düğümün de imzası gerekir. Bu işlemi gerçekleştirmeden önce, fon sağlayan taraf diğerinden zincir üzerinde gerçekleştirilmeyen, ancak bir sorun olması durumunda fonlarını geri almasını sağlayan bir *withdrawal transaction* imzalamasını ister.



![Image](assets/fr/004.webp)





- Commitment işlemleri:**



Kanalın durumu (yani sats'ün A ve B arasındaki dağılımı), her iki düğüm tarafından da bilinen ancak blok zincirinde hemen yayınlanmayan bir *commitment transaction* ile temsil edilir. Bu işlem, Lightning'de yapılan ödemelere göre kanal fonlarının zincir üzerinde nasıl yeniden dağıtılacağını açıklar.



Her Lightning ödemesinde, iki düğüm bir öncekinin yerini alan yeni bir durum imzalar. Eski durum, bir iptal anahtarı mekanizması sayesinde iptal edilir: katılımcılardan biri eski bir durumu yayınlamaya çalışırsa, diğeri ceza olarak fonların tamamını geri alabilir.



Buradaki önemli fikir, her zaman düğümler tarafından tutulan ve Lightning Network'te yapılan ödemelere göre birbirlerinin sats'lerinin yeniden dağıtılmasını sağlayan, zincir üzerinde yayınlanmayan imzalı bir Bitcoin işleminin olmasıdır.



![Image](assets/fr/005.webp)





- Kanal kapatma:**



Bir kanal, her iki taraf da kanalın son durumu üzerinde anlaştığında işbirliğine dayalı bir kapatma yoluyla temiz bir şekilde kapatılabilir veya katılımcılardan birinin işbirliğini bırakması veya ulaşılamaz hale gelmesi durumunda tek taraflı olarak (zorunlu bir kapatma) kapatılabilir. Her durumda, kapanış, 2/2 çıktısını harcayan ve fonları kanalın son geçerli durumuna göre katılımcılar arasında dağıtan bir zincir içi işlem şeklini alır.



![Image](assets/fr/006.webp)



Lightning böylece Bitcoin'e sabitlenmiş ikincil bir katman olarak işlev görür: ana blok zincirinde yalnızca belirli olaylar (kanalların açılması ve kapanması) görünür. Ara ödemeler zincir dışı kalır.



Daha ileri gitmeden önce, bir Lightning kanalının nasıl yönetileceğini anlamak için iki temel kavramı burada bulabilirsiniz:




- Liquidity*: kanalın bir tarafında mevcut olan sats miktarı;
- Kapasite*: 2/2 multisig çıkışında kilitli olan toplam miktardır, yani kanalın her iki tarafındaki likiditenin toplamıdır.



#### Bir kanal ve likidite ağı



Bir kanal sadece iki düğüm arasındaki ödemeler için değildir: birbirine bağlı kanallardan oluşan küresel bir ağın parçasıdır. Düğümünüz diğer kullanıcılar için ödemeleri kendi kanalları üzerinden yönlendirebilir ve iki düğümünüz arasında geçerli bir yol bulunduğu sürece, doğrudan kanalınız olmayan bir Lightning düğümüne sats gönderebilirsiniz.



Her düğüm, dedikodu protokolü aracılığıyla bu ağın bir haritasını bilir: hangi kanalların mevcut olduğu, hangi düğümlerin çift yönlü bir kanalla bağlandığı ve hangi kapasitelerin yayınlandığı. Doğrudan kanalı olmayan bir alıcıya ödeme göndermek için düğümünüz birkaç atlamadan oluşan bir rota hesaplar: düğümünüz → X düğümü → Y düğümü → alıcı düğümü. Her atlamada ödeme, ödeme yönünde yeterli likiditeye sahip olması gereken bir kanaldan geçer.



![Image](assets/fr/007.webp)



Bu nedenle bir kanalın likiditesi simetrik değildir: bir taraf ağır yük altındayken diğer taraf neredeyse boş olabilir. Bu likiditeyi yönetmek, yani sats'nin nerede olduğunu ve hangi yönde akabileceğini bilmek, bir Lightning düğümünü çalıştırmanın en önemli yönlerinden biridir. İlerideki uygulama bölümlerinde bu konuya daha ayrıntılı olarak bakacağız.



#### HTLC: Soyulmadan ödemenin taşınması



Lightning, ödemelerin güvene ihtiyaç duymadan ara düğümlerden geçmesini sağlamak için *HTLC* (*Hashed Time-Locked Contracts*) adı verilen akıllı sözleşmeleri kullanır. Basit bir ifadeyle, bir HTLC fon transferini bir sırrın ifşa edilmesine bağlı kılar ve işlemin başarısız olması durumunda göndereni korumak için bir zaman kısıtlaması içerir. Dolayısıyla her ödeme bir ön imajın (hash'i mutabık kalınan bir değere karşılık gelen bir sır) sunulmasına tabidir. Nihai alıcı bu ön görüntüyü sağlarsa, fonları talep edebilir ve bu da her aracı düğümün kendi fonlarını geri almasını sağlar.



![Image](assets/fr/008.webp)



HTLC'lerin nasıl çalıştığına dair teknik ayrıntılar bu kursun amaçları için gerekli olmadığından sizi bunlardan uzak tutacağım. LNP 201 teori kursunda derinlemesine bir açıklama bulacaksınız. Sadece HTLC'lerin atomik değişimleri mümkün kıldığını unutmayın: ya transfer tamamlanır ve yönlendirme sırasında kimse zarar görmez ya da başarısız olur ve her katılımcı başlangıçtaki fonlarını geri alır. İkisi arasında bir yol yoktur.



### Ana Lightning düğümü uygulamaları



Bitcoin'da olduğu gibi, Lightning protokolünün de çeşitli uygulamaları vardır. Bir dizi bağımsız ekip kendi versiyonlarını geliştirmektedir ve bunların hepsi aynı spesifikasyonlara (BOLT'lar) bağlı kaldıkları için birlikte çalışabilir. İşte bugün kullanımda olan ana uygulamalar.



#### LND (*Lightning Network Daemon*)



LND, Lightning protokolünün Go dilinde yazılmış ve Lightning Labs tarafından geliştirilmiş eksiksiz bir uygulamasıdır.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (eski adıyla *C-Lightning*) Blockstream tarafından geliştirilen bir uygulamadır. Bazı bileşenleri Rust'te olmak üzere C dilinde yazılmıştır.



![Image](assets/fr/010.webp)



#### Eclair



Eclair, Scala dilinde yazılmış ve Fransız ACINQ şirketi tarafından geliştirilmiş bir uygulamadır. ACINQ, Lightning ağındaki en önemli yönlendirme düğümlerinden birini Eclair ile işletmekte ve bu uygulamayı Phoenix uygulaması gibi kendi ürünleri için yazılım temeli olarak kullanmaktadır.



![Image](assets/fr/011.webp)



#### LDK (*Yıldırım Geliştirme Kiti*)



LDK (*Lightning Development Kit*), Spiral (Block, ex-Square) tarafından sürdürülen bir Rust geliştirme kitidir. daemon veya LND gibi kullanıma hazır bir CLN değil, Lightning'i doğrudan uygulamalarına entegre etmek isteyen geliştiriciler için bir kütüphanedir.



![Image](assets/fr/012.webp)



Bu LNP202 kursunda, esas olarak LND'e odaklanacağız: Umbrel gibi özel müşteriler için anahtar teslimi çözümlerde en yaygın olarak kullanılan uygulama.



Lightning'in nasıl çalıştığına dair bu kısa hatırlatma buraya kadar. Bir kez daha, anlamadığınız herhangi bir kavram varsa veya bunları uygulamaya koymadan önce biraz daha derine inmek istiyorsanız, Fanis Michalakis'in kursu konuyla ilgili temel referanstır:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Neden kendi Lightning düğümünüzü çalıştırmalısınız?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Retorik olduğu için bu soruyu yanıtlamak oldukça basit: kendi node'unuz olmadan artık Lightning'i gerçekten kullanmıyorsunuz, yalnızca bir şirketin altyapısında Lightning'in yanılsamasını kullanıyorsunuz.



Bir Lightning saklama wallet kullanmak, bitcoinlerin teknik olarak düğümü işleten şirkete ait olduğu anlamına gelir. Özel anahtarlara sahip değilsiniz ve kanalları kontrol etmiyorsunuz. wallet bakiyeniz yalnızca hizmet sağlayıcının veri tabanındaki bir satırdan ibarettir. Bu durum yeni başlayanlar için kesinlikle çok uygundur ve kullanıcı deneyimi genellikle akıcıdır, ancak temel soru şudur: Bitcoin ve Lightning'i geleneksel para birimlerinden ve bankalardan ayıran özelliklerden vazgeçerseniz, bunları kullanmanın avantajı nedir?



Bitcoin'in iki ana değer önermesi parasal egemenlik (artık ihraç ve tutma için merkezi bir otoriteye bağlı olmama) ve sansüre dirençtir (üçüncü bir tarafın ödemeleri engellemesi veya filtrelemesinin imkansızlığı). Lightning'deki bir saklama sistemi bu iki hedefe de ters düşmektedir: platformun dahili para arzını kontrol edemezsiniz ve tanım gereği, tüm fonları ve tüm kanalları elinde tutan bir operatör ödemelerinizi sansürleyebilir, geciktirebilir, önceliklendirebilir veya engelleyebilir. Bu koşullar altında kendimize haklı olarak **geleneksel devlet para sistemleriyle aynı güven ve bağımlılık kalıplarını yeniden üretecekse Lightning aracılığıyla bitcoin kullanmanın ne anlamı var** diye sorabiliriz.



> İhtiyaç duyulan şey, güven yerine kriptografik kanıta dayalı, istekli iki tarafın güvenilir bir üçüncü tarafa ihtiyaç duymadan doğrudan birbirleriyle işlem yapmasına olanak tanıyan bir elektronik ödeme sistemidir.
*Satoshi Nakamoto, Bitcoin Beyaz Kitap


Felsefe bir yana, sizin için daha somut dezavantajlar aşağıdaki gibidir. İlk olarak, şirketin gösterilen bakiyelere karşılık gelen bitcoinleri gerçekten elinde tuttuğunu doğrulamanın hiçbir yolu yoktur. Kısmi rezervle çalışabilir, hacklenebilir, iflas edebilir ya da basitçe ortadan kaybolabilir. Bu durumda, paranızı geri alacağınıza dair gerçek bir garanti olmadan sadece başka bir alacaklı olursunuz.



İkinci olarak, şirket düzenleyici risklere tabidir: ihtiyati tedbirler, fonların dondurulması, kullanıcıları veya işlemleri engelleme talepleri, güçlendirilmiş gözetim ve hatta belirli yargı bölgelerinde faaliyetin tamamen yasaklanması. Hizmet sağlayıcıya yüklenen her kısıtlama mekanik olarak size de yansır.



Gizlilik açısından da durum daha iyi değildir. Bir saklama operatörü tüm akışlarınızı görür: tutarlar, sıklıklar, alıcılar, bakiyeler, harcama alışkanlıkları. Uygulama tarafından sağlanan bilgiler ve muhtemelen Bitcoin'deki temel zincir analizi ile birleştirildiğinde, bu bilgiler finansal faaliyetlerinizin çok kesin bir profilini sağlayabilir. Bir kez daha, bu Bitcoin'in finansal izlemeyi azaltma amacından çok uzaktır.



İyi haber şu ki, bugün kendi Lightning düğümünüzü çalıştırmak, 2010'ların sonlarında olduğu gibi artık teknik uzmanların işi değil. Ev kullanıcıları için nispeten basit çözümler mevcuttur ve bunları bir sonraki bölümde ayrıntılı olarak açıklayacağız.




## İş için doğru çözümü seçme


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Bugün, Yıldırım gözetimindeki bir wallet'unkine çok yakın bir kullanıcı deneyimine sahip olmak ve aynı zamanda kendi gözetiminizde kalmak mümkündür. Bu bölümün amacı, profilinize en uygun yolu seçmenize yardımcı olmaktır.



### Seçenek 1: Lightning'i doğrudan kullanmayın



İlk çözüm, Lightning'i yerel olarak kullanmak değil, atomik takasları içeren bir Bitcoin veya Liquid wallet kullanmaktır. Örneğin, Aqua veya BULL Wallet uygulamaları bu yöntemi kullanarak, Lightning faturalarını bir Lightning düğümünü kendiniz çalıştırmadan, kendi gözetiminizde kalarak ödemenizi sağlar.



Prensip basittir: fonlarınız Bitcoin, on-chain veya Liquid'de kalır ve bunlara geleneksel şekilde anahtarları tuttuğunuz bir wallet aracılığıyla erişirsiniz. Bir Lightning faturasını taradığınızda, wallet'iniz bir atomik takas hizmetine bir işlem (on-chain veya Liquid) başlatır. Bu hizmet daha sonra on-chain veya Liquid aracılığıyla sağladığınız bitcoinleri kullanarak Lightning ödemesini kendi düğümü üzerinden yönetir. Sonuç olarak, herhangi bir Lightning kanalını kendiniz idare etmek zorunda kalmazsınız, ancak yine de Lightning faturalarını sorunsuz bir şekilde ödeyebilirsiniz.



![Image](assets/fr/013.webp)



Bu yaklaşımın geleneksel Lightning gözetimli wallet'e kıyasla en büyük avantajı, fonlarınıza her zaman %100 sahip olmanızdır. Bitcoinler, kendi anımsatıcı ifadenizle birlikte zincirinizde veya Liquid wallet'ünüzdedir. Takas sırasında bile, takas atomik olduğu için fonlarınıza sahip olmaya devam edersiniz. Yalnızca iki olası sonuç olmasını sağlayan bir kriptografik mekanizmaya dayanır: takas ya tamamen başarılı olur ya da başarısız olur ve hizmet fonlarınıza el koyamaz.



Bu tür bir işlevsellik sunan çoğu portföy, takasın teknik kısmı için [Boltz]'e (https://boltz.exchange/) güvenmektedir.



Bu çözüm, özellikle Liquid ile birlikte kullanıldığında, gizlilik açısından da ilginç avantajlar sunmaktadır. Yeni başlayanlar için kurulumu ve kaydetmesi de çok kolaydır: klasik bir anımsatıcı cümle, kanal yok, dengelenecek likidite yok...



Öte yandan, bu yaklaşımın sınırlamaları vardır. İlk olarak, telafi edilemez değildir: takas hizmetinin kullanılabilirliğine ve iyi niyetine bağlısınızdır. Artık hesabınızı işlemek istemezse veya faaliyetini durdurursa, Lightning faturalarını artık onun aracılığıyla ödeyemezsiniz. Bir de hiç de azımsanmayacak ücretler var: hem onchain veya Liquid işlem ücretlerini hem de takas hizmeti komisyonunu ödersiniz. Ayrıca, onchain ücretleri keskin bir şekilde yükselirse, Lightning'i kullanmak çok pahalı hale gelebilir.



Bu nedenle, ara sıra kullanım için hala kabul edilebilir, ancak çok aktif bir Lightning kullanıcısı için, gerçek bir Lightning düğümü ile işleri doğru yapmak daha iyidir.



### Seçenek 2: Yerleşik Lightning düğümleri



İkinci çözüm kategorisi, doğrudan bir mobil uygulamaya gömülü Lightning düğümlerine dayanmaktadır. Phoenix Wallet bu modele öncülük etmiştir ve bir referans noktası olmaya devam etmektedir. Günümüzde Zeus (gömülü modda) veya BitKit gibi diğer projeler de benzer yaklaşımlar sunmaktadır.



Fikir basittir: uygulama aslında bir Lightning düğümü çalıştırır, ancak tüm karmaşık işlemler arka planda otomatik olarak gerçekleştirilir. Yedekleme için anımsatıcı bir ifadeye sahip bir "*Lightning wallet*" arayüzünüz var, bir bakiye görüyor ve fatura ödüyorsunuz, ancak kanalları, likiditeyi veya çoğu parametreyi yönetmiyorsunuz.



![Image](assets/fr/014.webp)



Bu çözümler her zaman kendi kendine emanet edilebilir. Fonları kontrol eden anahtarlar generated'dir ve telefonunuzda saklanır ve yedekleme seed veya eşdeğer bir mekanizma aracılığıyla yapılır. Sadece bir hizmet sağlayıcıda hesabınız bulunmaz, aslında size ait olan ve çalınamayan kanallarda kilitli bitcoinlere sahip olursunuz.



LN yerleşik düğümlerinin avantajları çoktur:




- kurulumu ve kullanımı son derece kolaydır;
- lightning wallet'a yakın bir kullanıcı deneyimi, ancak kendi kendine saklama ile;
- kanalların veya likiditenin manuel yönetimi yok;
- nispeten basit bir yedekleme.



Ancak bu gömülü wallet'lerin de önemli sınırlamaları vardır. İlk olarak, gizlilik açısından, hizmet operatörü (örneğin Phoenix durumunda ACINQ) düğümünüzden geçen akışların oldukça ayrıntılı bir görünümüne sahiptir: miktarlar, frekanslar, alıcılar, özellikle *Trampoline Düğümlerinin* kademeli olarak benimsenmesiyle bu durum gelişecek olsa bile. İkinci olarak, ana Lightning eşiniz olarak bu operatöre büyük ölçüde bağımlısınız. ACINQ düğümü kullanılamaz hale gelirse (Phoenix durumunda), şirket düzenleyici baskı altına girerse veya iş modelini değiştirirse, kullanıcı deneyiminiz ciddi şekilde bozulabilir, hatta tehlikeye girebilir.



Son olarak, bu basitliğin bir bedeli vardır. Gömülü LN düğüm hizmetleri genellikle para yatırma, para çekme veya belirli kanal yönetimi işlemleri için belirli ücretler alır. Bence bu model sunulan hizmet açısından mantıklı, ancak yoğun kullanım için iyi yönetilen geleneksel bir Lightning düğümünden çok daha pahalı olabilir.



### Seçenek 3: Klasik Lightning düğümü



Bu LNP202 kursunda daha derinlemesine inceleyeceğimiz üçüncü çözüm, özel bir sunucu veya cihaz üzerinde geleneksel bir Lightning düğümü çalıştırmaktır.



"Klasik" derken, kendi Bitcoin düğümünüzün üzerine bir Lightning uygulamasını (örneğin LND) kendiniz kurup yapılandırdığınızı kastediyorum. Eşlerinizi seçer, kanallarınızı açar, gelen ve giden likiditenizi yönetir ve yönlendirme ücreti politikalarınızı belirlersiniz.



Egemenlik açısından bu en iyi çözümdür. Artık kanallarınız veya ödemeleriniz için belirli bir şirkete bağımlı değilsiniz: bir eşiniz sizi sansürlerse veya bir kanalı kapatırsa, farklı bir düğümle başka bir kanal açabilirsiniz. Bir hizmet ortadan kalkarsa, sats'niz kontrol ettiğiniz kanallarda kalır ve bunları zincir üzerinde geri alabilirsiniz. Ayrıca uzun vadeli maliyetlerinizi de optimize edebilirsiniz: kanallarınız doğru bir şekilde boyutlandırılıp yönetildiğinde, toplam ödeme maliyeti çok düşük olabilir.



Gizlilik açısından, tabii ki Lightning'in kendi modelinin sınırlamalarına tabisiniz, ancak tüm işinizi tek bir operatöre devretmiyorsunuz.



Buna karşılık, klasik bir Lightning düğümü kurmak açıkça daha karmaşıktır: kurmanız, yapılandırmanız, bakımını yapmanız, güncellemeleri izlemeniz, kanalların ve ücret politikalarının mantığını anlamanız, kanalları ve nakit akışını yönetmeniz vb. gerekir. Yanlış yapılandırma, özensiz yedekleme veya dikkatsiz yönetim, sats'in kaybına daha kolay yol açabilir. Düğüm ayrıca sürekli olarak çalışmalıdır.



Bu kursta izlemenizi önerdiğim yol tam olarak budur; riskleri sınırlandırmak ve yaklaşımınızı yapılandırmak için her adımda size eşlik ediyorum.



### Hangi kullanıcı profili için hangi çözüm?



Lightning kullanıcı profiliniz için doğru çözümü seçmek için iki faktörü göz önünde bulundurmanız gerekir: Lightning'i ne sıklıkta kullandığınız ve teknik yönetim konusundaki iştahınız.



Ara sıra çok fazla Lightning ödemesi yapmıyorsanız, ancak yine de zaman zaman telefonunuzdan LN faturalarını kendi kendine saklama özelliğinden vazgeçmeden ödeyebilmek istiyorsanız: takas işlevine sahip bir Bitcoin veya Liquid wallet muhtemelen en iyi seçenektir. Fonlarınızın mülkiyetini elinizde tutarsınız, düğüm yönetmezsiniz ve basitlik karşılığında biraz daha yüksek ücretleri kabul edersiniz.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Lightning'i oldukça düzenli bir şekilde kullanıyor ve gerçek bir node'un avantajlarından faydalanmak istiyor ancak kanalları, ücretleri veya altyapıyı yönetmek için zaman harcamak istemiyorsanız, mobil gömülü Lightning node'u iyi bir çözümdür. Fonlarınızın velayetini elinizde tutarsınız, UX çok erişilebilir kalır ve bir operatöre belirgin bir bağımlılık pahasına tüm karmaşıklık gizlenir.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Orta veya ileri düzey bir kullanıcıysanız, altyapınızı anlamak ve yönetmek için zaman ayırmaya istekliyseniz ve kanallarınız, likiditeniz ve maliyetleriniz üzerinde maksimum kontrol istiyorsanız: klasik bir sunucu tabanlı Lightning düğümü gitmenin yoludur. Bu en zorlu çözümdür, ancak aynı zamanda Bitcoin'ün egemenlik fikriyle de en tutarlı olanıdır.




# İlk Lightning düğümünüzü oluşturma


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## LND'in Umbrel ile Kurulumu


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Lightning'in temellerini ve mevcut çözümleri gözden geçirdiğimize göre artık işe koyulmanın zamanı geldi. Bu eğitimi almak için Umbrel ile senkronize edilmiş bir Bitcoin düğümüne ihtiyacınız olacak. Bu LNP202 eğitim kursu, BTC 202'nin devamı niteliğindedir; henüz bir Bitcoin düğümünüz yoksa, düğümünüz senkronize edildikten sonra buraya gelmeden önce sizi bu diğer eğitim kursunu almaya davet ediyorum. Çalışması, yapılandırması ve güvenlik önlemleri hakkında ayrıntıya girmeyeceğim için bu eğitime başvurmanızı şiddetle tavsiye ederim.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Bu ilk bölümde, LND'i Umbrel'unuza nasıl kuracağınıza bakacağız. Tek yapmanız gereken bir uygulama yüklemek olduğundan, Umbrel'un çalışma şekli bu adımı çok basit hale getirir.



Ana sayfadan, arayüzün alt kısmındaki `App Store`u açın.



![Image](assets/fr/015.webp)



Arama çubuğuna `Lightning Node` yazın ve ardından uygulamaya tıklayın.



![Image](assets/fr/016.webp)



Ardından kurulumu başlatmak için `Kur` düğmesine tıklayın.



![Image](assets/fr/017.webp)



Ana sayfadan, uygulamayı açmak için üzerine tıklayın ve ardından `Yeni bir düğüm kur` seçeneğini seçin.



![Image](assets/fr/018.webp)



Size 24 kelimelik bir anımsatıcı cümle verildi. Bunu güvenli bir yerde saklayın. Bir sonraki bölümde Lightning düğümünüze yeniden nasıl erişim sağlayacağınızı daha ayrıntılı olarak inceleyeceğiz (bu basit bir Bitcoin wallet'e göre çok daha karmaşık bir süreçtir), ancak şimdilik bu ifadenin çok önemli bir rol oynadığını ve son derece dikkatli bir şekilde saklanması gerektiğini unutmayın.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Bu ifadeyi geleneksel anımsatıcı ifadelerle aynı şekilde kaydedin: güvenli bir yerde saklanan fiziksel bir ortama (kağıt veya metal), ardından `NEXT` düğmesine tıklayın.



![Image](assets/fr/019.webp)



Ardından doğru yazıp yazmadığınızı kontrol etmek için cümlenizin kelimelerini girin.



![Image](assets/fr/020.webp)



Bir uyarı mesajı size uygulamanın beta sürümünde olduğunu ve Lightning Network'ün deneysel bir teknoloji olmaya devam ettiğini hatırlatacaktır. Açıkçası, Lightning düğümünüze asla kaybetmeye hazır olmadığınız miktarlar yüklemeyin.



Daha sonra Lightning düğümünüzün ana arayüzüne ulaşacaksınız. Sol tarafta, düğümünüzde barındırılan Bitcoin onchain wallet'yi bulacaksınız. Bu, az önce kaydettiğiniz 24 kelimelik ifadeden bir generated'dir.



Ortada, Lightning wallet'inizi bulacaksınız. Bu aslında [giden paranızı](https://planb.academy/resources/glossary/outbound-capacity), yani Lightning kanallarınızda sahip olduğunuz bitcoinleri temsil eder.



Sağ tarafta, düğümünüz hakkında birkaç önemli bilgi göreceksiniz:




- Bağlantı ve açık kanal sayısı;
- Toplam giden nakit akışınız, yani teorik olarak Lightning için harcayabileceğiniz miktar;
- Toplam gelen likiditeniz, yani teorik olarak Lightning üzerinden alabileceğiniz miktar.



![Image](assets/fr/021.webp)



Düğümümüzü özelleştirerek başlayalım. Arayüzün sağ üstündeki üç küçük noktaya ve ardından `Gelişmiş Ayarlar`a tıklayın. Kişiselleştirme` alt menüsünde, düğümünüz için genel bir ad tanımlayabilir (gerçek adınızı kullanmaktan kaçının) ve rengini seçebilirsiniz.



![Image](assets/fr/046.webp)



Ardından düğümünüzü yeniden başlatmak ve bu değişiklikleri uygulamak için yeşil `KAYDET VE YENİDEN BAŞLAT` düğmesine tıklayın.



Lightning node'unuz artık ödeme yapmak için ilk kanallarını açmaya hazır. Ama önce, sats'unuzu nasıl koruyacağınıza bir göz atalım!



## Lightning düğümünüzü kaydetme


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



İlk sats'nizi düğümünüze göndermeden önce, yedeklemenin nasıl çalıştığını ve ilgili risklerin neler olduğunu anlamak önemlidir. Basit bir Bitcoin onchain portföyünün aksine, bir Lightning node'unun yedeklenmesi oldukça karmaşıktır: yanlış strateji fonlarınızın kalıcı olarak kaybedilmesine yol açabilir. Bu bölümde, gerçekten neyin yedeklenmesi gerektiğine ve Umbrel'in bu süreci LND ile nasıl ele aldığına bakacağız.



Bu kursta LND (*Lightning Network Daemon*) uygulamasını kullanacağız. Prensipler diğer uygulamalarda benzer olsa da, bahsedeceğim kurtarma dosyaları ve prosedürleri LND'e özeldir.



### Lightning düğümünde ne kadar tasarruf etmeliyim?



Bir Yıldırım düğümünde, seed'yı kaydetmek ve her şeyin normale döneceğini ummak yeterli değildir. Çeşitli unsurlar farklı roller oynar, bu nedenle bunlar arasında ayrım yapmak önemlidir.



#### seed (*aezeed*)



LND'i başlattığınızda, 24 kelimelik bir seed alırsınız. Bu, "*aezeed*" adı verilen LND'e özgü bir formattır. Çok benzese de klasik bir seed BIP39 değildir. Bu seed'dan LND, Lightning düğümü ile ilişkili zincir üzerindeki wallet'inizin özel anahtarlarını, yani kanal kapanışlarının ardından bitcoin alabileceğiniz veya bitcoinleri geri gönderebileceğiniz adresleri türetir.



![Image](assets/fr/019.webp)



Bu nedenle bu seed, düğümünüzle ilişkili zincir üzerindeki wallet'yi yeniden oluşturmak ve zincir üzerinde zaten geri gönderilmiş olan fonları geri almak için kullanılabilir (örneğin, bir kanal kapatıldıktan sonra). Öte yandan, seed, kanallarınızın durumu hakkında gerekli bilgileri içermediğinden, hala açık olan Lightning kanallarınızı geri yüklemek için tek başına yeterli değildir.



#### Kanal veritabanı (`channel.db`)



LND, kanallarınızın ayrıntılı durumunu `channel.db` adlı bir veritabanında saklar. Bu veritabanı şunları içerir:




- açık kanallarınızın listesini görüntüleyin;
- akranlarınız ve onların tanımlayıcıları;
- her kanal için son commitment transaction'ler (kanalda kimin neye sahip olduğunu tanımlayan ve bir sorun olması durumunda zincir üzerindeki fonların kurtarılmasını sağlayan ardışık durumlar);
- eski bir raporu yayınlamaya çalışan bir eşin cezalandırılması için gereken bilgiler.



Bu veritabanıyla ilgili sorun, sürekli değişiyor olmasıdır: her ödeme, her yönlendirme, bir kanalın her açılması veya kapanması içeriğini değiştirir. Bu nedenle geleneksel bir yedekleme (örneğin `channel.db`nizin periyodik bir kopyası) tehlikelidir. Eğer `channel.db`nin çok eski bir versiyonunu geri yüklerseniz ve düğümü bu eski durumla yeniden birleştirirseniz, eşleriniz eski bir kanal durumu yayınladığınızı düşünebilir. Bu durumda, protokol bir ceza öngörür: eşiniz, hile yapmaya çalışmışsınız gibi, kanalın fonlarının tamamını geri alabilir.



Pratikte, `channel.db` bir yedekleme ortamı değildir. Düğümünüzün yaşayan durumudur. Düğümünüzü geri yüklemek için kullanmanın mantıklı olduğu tek durum, bu veritabanını doğrudan yeni arızalanmış bir makineden (örneğin hala okunabilir bir diskten) kurtarmanızdır. Bu durumda, en son durumu kurtarırsınız ve eski makine artık çalışmadığı için bu durumun mümkün olduğunca güncel olduğunu bilerek bu veritabanını temel alan başka bir makinede LND'yı yeniden başlatabilirsiniz. Bu yöntemin uygun bir yedekleme görevi görebileceği bir başka durum da, birinden diğerine dinamik, kalıcı bir kopyanın bulunduğu iki diskli bir yapılandırmadır. Ancak bu tür bir kurulumun uygulanması daha karmaşıktır.



Ancak `channel.db`nin periyodik kopyalarını almak ve bunları daha sonra geri yüklenmek üzere yedek olarak saklamak çok kötü bir fikirdir: bunları kullandığınız gün, kendinizi cezalandırma ve tüm sats'nizi kaybetme riskiyle karşı karşıya kalırsınız.



#### Statik Kanal Yedekleme (SCB)



Felaket kurtarmayı mümkün kılmak için LND *Statik Kanal Yedekleme* (SCB) mekanizmasını tanıttı. Bu, genellikle `channel.backup` olarak adlandırılan ve kanallarınız hakkında statik bilgiler içeren özel bir dosyadır: eşlerinizin kim olduğu, onlarla nasıl iletişim kuracağınız ve kanallarınızın ne olduğu.



Bu dosya ayrıntılı kanal durumu veya güncelleme geçmişi içermez. Kanalları tam olarak bulundukları durumda yeniden açmanıza veya bu Lightning düğümünü çalıştırmaya devam etmenize izin vermez. Bunun yerine, rolü, eşlerinizden tüm kanallarınızı temiz bir şekilde kapatmanıza yardımcı olmalarını istemek için bir bağlantı noktası görevi görmek ve böylece seed sayesinde alabileceğiniz anahtarlarda sats onchain'inizi almaktır. Dolayısıyla, her ödeme veya yönlendirme ile değiştirilen `channel.db` dosyasının aksine, SCB dosyası yalnızca bir kanal açıldığında veya kapatıldığında güncellenir.



SCB aracılığıyla kurtarma yaparken süreç aşağıdaki gibidir:




- seed'nizi (*aezeed*) geri yüklersiniz, bu da Lightning düğümü ile ilişkili zincir üzerindeki wallet'inizi yeniden oluşturur;
- LND'e en son SCB'nizi sağlıyorsunuz;
- LND, eşlerinizin listesini ve onlarla olan kanallarınızı bulmak için SCB'yi kullanır;
- Her bir eşle iletişime geçer, onlara bir veri kaybı yaşadığınızı söyler ve zincir üzerindeki paylaşımınızı kurtarabilmeniz için onlarla olan kanalınızı "zorla kapatmalarını" ister.



Buradaki fikir, veri kaybı bildirdiğinizi fark eden eşlerinizin son commitment transaction'lerini yayınlamaları ve güç kanalını kapatmalarıdır. Bu işlemler onaylandıktan sonra, fonlarınız zincir üzerindeki portföyünüzde (seed ile bağlantılı) yeniden görünür.



Ancak bu kurtarma mekanizması mükemmel değildir. İlk olarak, tüm kanallar kapatılacağı için Lightning düğümünüzü gerçekten geri yüklemez. Daha sonra sıfırdan yeni bir Lightning node'u oluşturmanız gerekecektir. İkinci olarak, bir sorun durumunda zincir içi bakiyelerinizi kurtarma şansınızı önemli ölçüde artırmasına rağmen %100 kurtarmayı garanti etmez. Aslında, bu kurtarma protokolü eşlerinizin işbirliğine ve kullanılabilirliğine bağlıdır: bunlardan biri çevrimdışıysa, kendi verilerini kaybetmişse veya işbirliği yapmayı reddederse, fonlarınız bloke kalabilir, hatta kalıcı olarak kaybolabilir. Bu nedenle Lightning düğümünüzde ulaşılamayan eşlerle kanalları uzun süre açık tutmamanız önemlidir. Bu noktada bir veri kaybı yaşarsanız ve eşe ulaşılamazsa, SCB aracılığıyla kurtarma imkansız olacak ve eş tekrar çevrimiçi olana kadar (belki de sonsuza kadar) fonlarınız kayıp kalacaktır.



Özetle, LND'de iyi bir Lightning yedekleme stratejisi üç temele dayanır:




- Zincir üstü katman için seed'iniz (*aezeed*);
- Güvenilir otomatik SCB yedeklemesi;
- Güvenilir eşler seçerek ve genellikle ulaşılamayanları önleyici olarak kapatarak iyi kanal yönetimi.



### Umbrel, LND düğümünüzün yedeklemesini nasıl yönetir?



Umbrel, LND düğümü için tam olarak SCB'ye dayanan basitleştirilmiş bir yedekleme mekanizması sunar. Buradaki fikir, sizi bu dosyayı kendiniz manipüle etme, yedeğini alma ve süreci mümkün olduğunca otomatikleştirme zahmetinden kurtarmaktır.



Düğümünüzü Umbrel üzerinde oluşturduğunuzda, ikili bir rol oynayan bir seed alırsınız:




- lightning düğümünüzle ilişkili Bitcoin onchain wallet'nızı türetir;
- uzak SCB yedeklemeleri için kullanılan bir yedekleme tanımlayıcısı ve şifreleme anahtarı türetmek için kullanılır.



Bu mekanizma sayesinde, Umbrel otomatik olarak SCB'nizin şifreli bir yedeğini alır ve Tor aracılığıyla sunucularında depolar. SCB, seed'unuzdan türetilen bir anahtar sayesinde şifrelenmiş olarak saklanır. Bu nedenle, veri kaybı durumunda tek yapmanız gereken, aynı veya başka bir makinede Umbrel'de bir Bitcoin ve Lightning düğümünü yeniden oluşturmak ve ardından seed'unuza girmektir. Daha sonra Umbrel sunucularından en son SCB durumunu alabilir, şifresini çözebilir ve fonlarınızı kurtarma işlemine başlayabilirsiniz.



Bu yedekler gönderilmeden önce düğümünüz tarafından yerel olarak şifrelenir, bu da verilerinizin gizliliğini garanti eder: Umbrel SCB'nin içeriğini okuyamaz. İletim Tor üzerinden gerçekleşir, bu da IP adresinizin sızdırılmasını önler. Dahası, Umbrel'iniz trafiğe gürültü ekleyerek (rastgele dolgu ve düzensiz aralıklarla gönderilen yanlış yedeklemeler) sunucunun bir kanalı tam olarak ne zaman açtığınızı veya kapattığınızı anlamasını engeller.



Bu yöntemin ana avantajı, Lightning düğümünüzün yedeklenmesini önemli ölçüde basitleştirmesidir: seed'inizi düğüm başlatma sırasında yalnızca bir kez yedeklemeniz gerekir. Bu, yalnızca SCB'nin yedeği olduğu için bir miktar risk içerir, ancak makul miktarlar için kabul edilebilir bir uzlaşmadır.



### Kayıp riskini sınırlandırmak için en iyi uygulamalar



Umbrel yedeklemesi olsa bile, birkaç basit iyi uygulama sats'ü kaybetme riskini büyük ölçüde azaltabilir:





- Akranlarınızın müsaitlik durumunu izleyin:



Önemli bir kanal sıklıkla ulaşılamayan veya kararsız bir eşle ilişkilendiriliyorsa, düğümünüz hala çalışırken kanalı temiz bir şekilde kapatmak daha güvenlidir. Önleyici bir işbirliği veya zorla kapatma, SCB kurtarma durumunda potansiyel bir sorun kaynağını ortadan kaldırır.





- Bilinmeyen emsaller üzerinde çok fazla likidite yoğunlaştırmaktan kaçının:



Bir eşin sizinle olan kanalı ne kadar büyükse, güvenilir olması o kadar önemlidir. Ciddi, iyi bağlanmış ve aktif düğümler seçin, böylece SCB aracılığıyla gelecekteki herhangi bir kurtarma sorunsuz çalışabilir.





- Umbrel'ü yerel yedeklemelerle destekleyin:



Umbrel'in otomatik yedeklemesine ek olarak, SCB dosyanızın (`channel.backup`) şifrelenmiş bir kopyasını harici bir ortamda da saklayabilir ve periyodik olarak güncelleyebilirsiniz. İdeal olarak, bir kanalı her açtığınızda veya kapattığınızda bunu yenilemelisiniz. Bu, herhangi bir nedenle Umbrel'in otomatik yedekleme hizmeti kullanılamaz hale gelirse size bir yedekleme çözümü sunar.





- seed'nızı doğru şekilde yönetme



seed Umbrel'iniz yalnızca zincir üzerindeki wallet'nizi geri yüklemekle kalmaz, aynı zamanda yedeklemeler için şifreleme anahtarını da türetir. Bu nedenle bu anahtara erişimi olan bir saldırgan, node'unuza fiziksel erişimi bile olmadan bir kurtarma işlemi başlatabilir ve fonlarınızı kendi wallet'sine aktarabilir.



Dolayısıyla, düğümünüzü geri yüklemeniz gerekiyorsa ancak artık seed'iniz yoksa, hiçbir şeyi kurtaramazsınız: tüm sats'ınız kaybolacaktır. Bu nedenle seed'inizi son derece dikkatli bir şekilde, yalnızca fiziksel ortamda (kağıt veya metal) saklamanız ve güvenli bir yerde tutmanız çok önemlidir. Bir seed'i yönetme hakkında daha fazla bilgi için lütfen bu eğitime başvurun:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Lightning düğümümü Umbrel'ye nasıl kaydedebilirim?



Teorinin nasıl işlediğini anladığınıza göre, şimdi işin özüne inelim. Lightning Node uygulamanızdan (ki bu aslında LND'tür), sağ üst köşedeki üç küçük noktaya tıklayın.



![Image](assets/fr/022.webp)



Burada yedekleme için ilgi çekici üç unsur vardır:




- Otomatik yedekleme seçeneğinin etkin olup olmadığını kontrol edin. Bu, şifrelenmiş SCB'nizi otomatik olarak Umbrel'ün sunucularına gönderecektir.
- Daha sonra `Tor üzerinden yedekle` seçeneğini kullanarak Tor veya clearnet üzerinden göndermeyi seçebilirsiniz. Önceki bölümlerde açıklandığı gibi, gizliliğinizi korumak için Tor kullanmanızı şiddetle tavsiye ederim.
- Son olarak, bir `channel.backup` dosyasını, yani SCB'nizin şifrelenmiş bir anlık görüntüsünü bilgisayarınıza indirmenize olanak tanıyan bir `Kanal yedekleme dosyasını indir` düğmesi vardır. Bu, otomatik olarak Umbrel sunucularına gönderilenlere ek olarak zaman zaman ek yerel yedeklemeler yapmanızı sağlar.



Artık Lightning düğümünüzün sats'sını veri kaybına karşı nasıl koruyacağınızı biliyorsunuz. Bir sonraki bölümde, düğümünüzü hile girişimlerine karşı nasıl koruyacağınıza bakacağız.




## Watchtower: rol ve kurulum


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



Lightning'de her kanal, yayınlanmamış commitment transaction'ler tarafından temsil edilen bir dizi ardışık duruma dayanır. Her Lightning ödemesi veya yönlendirmesi ile kanaldaki 2 katılımcı, kanaldaki mevcut fon dağılımını yansıtan yeni bir commitment transaction çifti oluşturur. Eski commitment transaction'ler kullanılmaz hale gelir.



Taraflardan biri güncel olmayan bir durum yayınlarsa, diğerinin bunu yaptırıma tabi tutma ve kanalın fonlarının tamamını geri alma hakkı vardır. Bu bölümde, bu mekanizmanın nasıl çalıştığına kısaca göz atacağız ve ardından Lightning düğümünüzü olası hile girişimlerinden korumak için bir sistem olan ***gözetleme kulesinin*** nasıl kurulacağını açıklayacağız.



### Gözetleme kulelerinin nasıl çalıştığını anlamak


Herhangi bir anda, kanaldaki her bir tarafın, yayınlandığı takdirde kanalı kapatmalarını ve fonlardan paylarını geri almalarını sağlayacak bir commitment transaction'u vardır. Bu süreç *zorla kapatma* olarak bilinir. Ancak, daha fazla sats'e sahip olduğu kanalın önceki bir durumuna karşılık gelen daha eski bir commitment transaction yayınlamaya çalışırlarsa, bu işlem bir hile girişimi olarak kabul edilir. Bu durumda, karşı taraf bu eski durumla ilişkili iptal anahtarını kullanarak kanaldaki tüm fon miktarını geri kazanabilirken, hile yapan kişi zaman kilidi tarafından geçici olarak engellenir.


Bu sistem, eski bir durumu yayınlamanın, yani hile yapmaya çalışmanın çok riskli olduğu anlamına gelir: diğer taraf bu işlemi zaman kilidi sona ermeden önce mempool'da veya blok zincirinde görürse, iptal anahtarını kullanabilir ve tüm fonları geri alabilir. **Bu nedenle, Lightning kanalınızın güvenliği, zaman kilidi tarafından uygulanan zaman penceresi içinde bir hile girişimini tespit etme yeteneğinize bağlıdır**.



#### Gözetleme kuleleri neden gereklidir?



Ceza mekanizması yalnızca zarar gören tarafın bunu yapabilmesi halinde işler:




- bir commitment transaction kanalının yayınlanıp yayınlanmadığını görmek için her yeni Bitcoin bloğunu izleyin;
- bu işlemin son geçerli duruma mı yoksa iptal edilmiş bir duruma mı karşılık geldiğini belirler;
- i̇ptal edilmiş bir durum söz konusu olduğunda, zaman kilidi sona ermeden önce tüm fonları kurtarmak için iptal anahtarını kullanarak yasal işlemi zamanında yayınlamak.



![Image](assets/fr/023.webp)



İdeal bir senaryoda, Lightning düğümünüz 7/24 çevrimiçidir, blok zincirini senkronize eder ve sürekli olarak izler. Bu nedenle, bir hile girişimini tek başına tespit edebilir ve tepki verebilir. Ancak pratikte, kişisel bir Lightning node'u, özellikle uzun süreli bir elektrik kesintisi veya İnternet bağlantısı arızası durumunda kapanabilir.



İşte tam da bu kesinti dönemlerinde risk gerçek olur: dürüst olmayan bir eş, düğümünüz çevrimdışıyken eski bir durum yayınlarsa ve zaman kilidi sizden herhangi bir tepki gelmeden biterse, hile etkili olur. Kanaldaki fonlarınızın bir kısmını ya da tamamını kaybedersiniz.



Watchtower'ler bu riski azaltmak için uygulamaya konmuştur. Gözetleme kulesi, blok zincirini sizin adınıza izleyen, kanallarınızdan birinde eski bir durumun olası yayınını tarayan ve gerekirse ceza işlemini sizin adınıza otomatik olarak yayınlayan harici bir hizmettir. Dolayısıyla, Lightning node'unuz uzun bir süre çevrimdışı kalsa bile, kullandığınız gözetleme kulesi çalışır durumda olduğu sürece, herhangi bir hile girişimini izleyerek ve tespit ettiği anda ilgili cezayı uygulayarak fonlarınızı koruyabilecektir.



#### Bir gözetleme kulesi nasıl çalışır?



Bir gözetleme kulesi, kanallarınız hakkında öğrendiği bilgileri en aza indirirken, bir sorun olması durumunda harekete geçmesini sağlayacak şekilde tasarlanmıştır:




- Bir eş ile her yeni kanal durumu için düğümünüz önceden potansiyel bir ceza işlemi hazırlar. Bu eşin hile yapması durumunda, bu işlem kanaldaki tüm fonları geri almanızı sağlayacaktır;
- Düğümünüz daha sonra bu ceza işlemini ilgili commitment transaction'ün TXID'sini kullanarak şifreler (hilekarın bir sahtekarlık girişiminde bulunması durumunda kullanılacak olan). Kapatma işlemi gerçekleşmediği sürece, gözetleme kulesi hile işleminin TXID'sini tam olarak bilmediği için bu işlemin şifresini çözemez;
- Düğümünüz gözetleme kulesine şifrelenmiş ceza işlemini ve olası hile işleminin TXID'sinin yarısını içeren bir paket gönderir.



Gözetleme kulesine iletilen TXID eksik olduğundan, adalet işleminin şifresini çözemez. Ancak, sahip olduğu kısımla eşleşen bir TXID için blok zincirini izleyebilir. Böyle bir işlem tespit ederse, ceza işleminizin şifresini çözmek için bu işlemin tam TXID'sini kullanmaya çalışır. Şifre çözme başarılı olursa, bunun bir hile girişimi olduğunu anlar ve sizin için ceza işlemini hemen yayınlar.



![Image](assets/fr/024.webp)



Bu nedenle gözetleme kulesi kanallarınızın ayrıntılarını göremez: ne eşlerinizin kimliği, ne bakiyeler, ne de işlemlerin yapısı. Sadece şifrelenmiş paketleri görür. Çıkarabileceği tek bilgi kanallarınızın güncellenme hızıdır, çünkü her yeni durum için bir paket alır, ancak içeriğini bilemez. Hile yapılması durumunda, ceza işleminin şifresini çözerek kanal bilgilerini kesinlikle keşfedecektir, ancak en azından sats'iniz kaydedilecektir.



Bu mekanizma bir uzlaşmaya dayanır: Gözetleme kulesine önceden imzalanmış bir ceza işlemi yayınlama yetkisi verirsiniz, ancak bu işlem bazı hileler gerçekleşene kadar gözetleme kulesi için tamamen opak kalır. Gözetleme kulesi ne alıcıları değiştirebilir ne de fonları yönlendirebilir, çünkü elinde sadece imzalanmış ve çıktıları sizin lehinize dondurulmuş bir işlem vardır. TXID'ler eşleşmediğinden, meşru bir zorunlu veya işbirlikçi kapanıştaki bir kanalın ayrıntılarını da bilemez. Öte yandan, watchtower asgari düzeyde güvenilir bir üçüncü taraf olmaya devam eder: çevrimiçi olmasına ve ihtiyaç duyduğunuzda adalet işleminizi düzgün bir şekilde yayınlamasına güvenmeniz gerekir.



#### Gözetleme kulesi olmak



Teorik olarak, herhangi bir Lightning düğümü, kendisi için bu rolü oynayan diğer düğümler tarafından korunurken, diğer düğümler için (aynı uygulamayı kullanıyorlarsa, örneğin LND) bir gözetleme kulesi olarak hareket edebilir. Aşağıdaki pratik bölümlerde, bu basit mekanizmayı LND'nizde Umbrel altında nasıl kuracağınızı göstereceğim.


Sonuç olarak, ilginç bir strateji, birbirlerinin gözetleme kulesi olarak hareket etmek için güvenilir bitcoiner arkadaşlarla anlaşmak olabilir. Siz onların kanallarını izlersiniz, onlar da sizinkileri.



### Fedakar bir gözetleme kulesi bulun



Çevrenizde gözetleme kulesi hizmeti verebilecek kimseyi tanımıyorsanız, bağlanabileceğiniz bir dizi fedakâr kamu gözetleme kulesi vardır. Örneğin, bu LNP202 kursunda, LN+ ve LND için bir gözetleme kulesi olan Voltage tarafından ortaklaşa sunulan gözetleme kulesi hizmetine bağlanmanızı öneririm.


Burada giriş bilgilerine sahipsiniz:



- Tor üzerinden:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Clearnet aracılığıyla:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Bu ücretsiz gözetleme kulesi hizmetini sağladıkları için onlara teşekkür etmek amacıyla [Lightning üzerinden bağış yapabilirsiniz](https://lightningnetwork.plus/donation).


Artık özgeci bir gözetleme kulesi hizmeti kullandığımıza göre, bunu Umbrel altındaki LND düğümümüzde nasıl yapılandıracağımızı görelim.


### Bir gözetleme kulesi kurmak


Lightning Node' uygulamasından, arayüzün sağ üst köşesindeki üç noktaya tıklayın ve ardından `Gelişmiş Ayarlar'ı seçin.


![Image](assets/fr/025.webp)


Ardından `Watchtower` menüsüne gidin.


![Image](assets/fr/026.webp)



Watchtower Client` seçeneğini etkinleştirin, ardından `SAVE AND RESTART NODE` düğmesine tıklayın. LND'ün yeniden başlamasını bekleyin.


![Image](assets/fr/027.webp)


Yeniden başlatma tamamlandığında, aynı menüye geri dönün ve seçtiğiniz fedakar gözetleme kulesinin kimliğini verilen alana girin. Ardından onaylamak için `ADD` düğmesine tıklayın. Ayrıca `Watchtower Müşteri Tarama Ücreti Oranı` parametresini de ayarlayabilirsiniz: bu, gözetleme kulesi tarafından yayınlanan olası bir adalet işlemi için ödemek istediğiniz ücret oranıdır. Aşırı yüksek bir oran seçmenize gerek yoktur, ancak çok düşük bir orandan da kaçınmalısınız, aksi takdirde yasal işlem zamanında onaylanmayacaktır.


Bu değişiklikleri uygulamak için `NOTU KAYDET VE YENİDEN BAŞLAT` düğmesini kullanarak düğümünüzü yeniden başlatın.


![Image](assets/fr/028.webp)



Aynı menüye geri dönerseniz, Lightning düğümünüzün artık yeni eklediğiniz gözetleme kulesi tarafından korunduğunu göreceksiniz.



![Image](assets/fr/029.webp)



Özellikle Lightning düğümünüze büyük miktarlarda para yatırmazsanız ve düğümünüzü iyi yönetirseniz (çok uzun süre kapalı bırakmayın), fedakar bir gözetleme kulesi genellikle yeterlidir. Daha da fazla güvenlik için, aynı işlemi tekrarlayarak birkaç tane de ekleyebilirsiniz.



## İlk Lightning kanalınızı açın


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Buraya kadar geldiyseniz, kanalı olmayan bir Lightning düğümünün boş bir wallet'ya benzediğini zaten biliyorsunuzdur: var, ama işe yaramaz. Ödeme gönderebilmek veya alabilmek için düğümünüzün bir kanal aracılığıyla Lightning ağındaki en az bir başka düğüme bağlı olması gerekir. Gelecekte, esneklik ve yönlendirme verimliliği nedenleriyle birkaç kanal açmanızı şiddetle tavsiye ediyoruz. İlerleyen bölümlerde, likit varlıklarınızı nasıl yöneteceğinize, kanal topolojinizi nasıl optimize edeceğinize ve Umbrel'deki temel LND arayüzünden daha gelişmiş araçları nasıl kullanacağınıza da bakacağız.



Ancak bu giriş bölümünde amaç sadece iyi bir Lightning eşini nasıl seçeceğinizi, eşlerinizi seçmek için ihtiyacınız olan bilgileri nerede bulacağınızı ve son olarak temel LND arayüzü üzerinden ilk kanalınızı nasıl açacağınızı anlamaktır.



### İyi bir Lightning akranı nasıl seçilir?



Bir kanal açtığınızda, bir eş seçmeniz gerekir: düğümünüzün bir kanal aracılığıyla doğrudan bağlanacağı başka bir Lightning düğümü. Bu eş seçimi, üzerinde doğrudan bir etkiye sahip olacağı için önemlidir:




- ödemelerinizin yolunu bulmasını kolaylaştırır;
- kanallarınızın zaman içindeki güvenilirliği;
- yönlendirme maliyetleriniz.



Herkes için mükemmel eşleşme diye bir şey yoktur, ancak iyi adayları belirlemek için bir dizi güvenilir kriter vardır.



#### 1. Düğüm bağlantısı



İyi bir eş, Lightning ağına iyi bağlanmış bir düğümdür. Bu, yalnızca çok sayıda kanala sahip olmak değil (bu bir gösterge olabilir), her şeyden önce diğer güvenilir düğümlere bağlı olmak ve ağ grafiğinde yeterince merkezi bir konuma sahip olmak anlamına gelir.



İyi bağlanmış bir düğüm, çoğu ödeme hedefine verimli bir rota bulma şansınızı artırır. Ayrıca ihtiyaç duyulan aracı düğüm sayısını azaltarak maliyetleri düşürür.



Tersine, ilk kanalınızı izole veya zayıf bağlantılı bir düğüme açmak olasılıklarınızı kısıtlayabilir: bu eşe ödeme yapabilirsiniz, ancak ağın geri kalanına ödeme yapmak çok daha zor olacaktır.



#### 2. Kapitalizasyon ve kanal kapasitesi



İyi bir eş aynı zamanda yeterince sermayelendirilmiş bir düğümdür. Bu, toplam kanal kapasitesi (tüm kanallarına taahhüt edilen sats'nin toplamı) ve ortalama kanal kapasitesi ile gösterilir (genellikle iyi sermayelendirilmiş birkaç kanala sahip olmak, birçok küçük kanala sahip olmaktan daha iyidir).



Kapasitesi çok düşük olan veya kanallarının tamamı küçük olan bir düğüm, büyük miktarlardaki ödemeleri yönlendiremeyecek ve bu da sizin için yönlendirme hatalarına neden olacaktır.



#### 3. Gider politikaları



Her düğüm kendi yönlendirme ücretlerini (`taban ücret` ve `ücret oranı`) belirler. İyi bir eş, stratejik kanallar için fahiş ücretler talep etmeyecektir. İlk kanal için, kendi ödemelerinizi engellememek için oldukça makul ücretleri olan bir düğüm seçmek en iyisidir.



Kendi yönlendirme ücretlerinizin de başkalarının sizi bir eş olarak nasıl algıladığını etkilediğini unutmayın: ücretlerini sürekli değiştiren veya saçma maliyetler uygulayan bir düğüm nadiren takdir edilir.



#### 4. İstikrar ve kıdem



Eş stabilitesi çok önemli bir kriterdir. İyi bir node yüksek çalışma süresine sahiptir (çok nadiren çevrimdışıdır), kanallarını uzun süre açık tutar ve sebepsiz yere sürekli kanal açıp kapatmaz.



Eski ve hala aktif kanallar iyi bir sinyaldir: ilişkinin eş için karlı olduğunu, düğümün sermayesini nasıl yöneteceğini bildiğini ve herhangi bir zamanda kapanmadığını gösterir, böylece kapatma ve yeniden açma için zincir üzerinde ücret ödemeye devam etmek zorunda kalmazsınız.



Tersine, sık sık çevrimdışı olan veya kanalları hızla kapatan bir eş, sizin için bir sorun kaynağı ve yeni kanallar açmak için ek maliyetler olabilir.



Bu kriterlerle bile ilk seferde mükemmel bir seçim yapamazsınız. Bu normaldir: bir eşin gerçek kalitesi kullanımıyla ortaya çıkar. Bu yüzden önemli olan:




- kanal etkinliğini izleyin (yönlendirilen hacimler, kullanılabilirlik vb.);
- amaca hizmet etmeyen veya eşleri çok sık çevrimdışı olan kanalları kapatın;
- sermayenizi zaman içinde daha iyi emsallere yeniden tahsis edin.



Buradaki fikir, her gün kanal açıp kapatmak değil (ki bu zincir içi maliyetler açısından pahalı olacaktır), ihtiyaçlarınızla uyumlu, güvenilir, iyi bağlanmış eşler kümesine yakınsamak için topolojinizi kademeli olarak geliştirmektir.



### Nasıl bir akran bulabilirim?



Bu kriterleri uygulamak için Lightning ağının görünürlüğünü sağlayan araçlara ihtiyacınız olacaktır. Bunu yapmak için çeşitli kaşifler ve hizmetler mevcuttur. En iyi bilinen Lightning kaşifleri arasında [1ML](https://1ml.com/) ve [Amboss](https://amboss.space/) bulunmaktadır.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Ancak burada, bir kanal açmak için en uygun olduğu düşünülen Lightning düğümlerinin bir sıralamasını (kuşkusuz kısmen öznel kriterlere dayalı) sağlayan [Lightning Labs'ın Lightning Terminal aracını](https://terminal.lightning.engineering/) kullanmanızı öneririm.



![Image](assets/fr/030.webp)



Bu sıralamanın en üstündeki çok büyük Lightning düğümleriyle ilgili sorun, çoğunun çok yüksek miktarların altındaki kanal açılışlarını kabul etmemesidir. Birçoğu ayrıca kanalınızın kapatılmasına yol açabilecek katı eş yönetimi politikaları uygular. Öte yandan, bu node'ların bağlantı sayıları göz önüne alındığında genellikle gelen likiditeye ihtiyaçları yoktur.



Bu nedenle, aşırı büyük olmadan, iyi bağlantılı, güvenilir ve ağ grafiğinde yeterince merkezi olan bir düğüm bulmak için sıralamada aşağı doğru ilerlemenizi tavsiye ederim. Örneğin, burada çok iyi bağlantılı, yüksek kapasiteli ve ağ grafiğinde merkezi bir konuma sahip olan stacker.news üzerindeki Lightning düğümünü belirledim.



![Image](assets/fr/031.webp)



Bir diğer ilginç yaklaşım ise, tanıdığınız bir tüccar, bir dernek veya bir topluluk gibi gelen likiditeye ihtiyaç duyan bir düğüme kanal açmaktır. Bu stratejinin üç avantajı vardır:




- Seçilen kuruluşun gelen likiditeye ihtiyacı olduğundan, mantıksal olarak kanalınızı sebepsiz yere kapatmak için daha az teşviki olacaktır;
- Ekonomik faaliyeti, bu kanal üzerinden yönlendirme ve dolayısıyla bazı ücretleri tahsil etme şansını artırmaktadır;
- Ekosisteme bir iyilik yapıyorsunuz ve diğer bitcoin kullanıcılarına değerli bir katkıda bulunuyorsunuz.



İlgili bir düğümü belirledikten sonra, Düğüm Kimliğini alabilirsiniz. Bu basitçe düğümün açık anahtarının, bir `@` ayırıcısının, IP veya Tor adresinin ve kullanılan bağlantı noktasının bir araya getirilmesidir. Bu kimliğe herhangi bir Lightning gezgininde düğümün profilinden kolayca erişilebilir.



### İlk kanalınızı LND üzerinden açın



Artık ilk kanalımızı açacağımız düğümü belirlediğimize göre, ona kilitlenmek için sats'ya ihtiyacımız var. Bunu yapmak için, LND ile ilişkili wallet zincirindeki Bitcoin'ü beslemeniz gerekir.



Ana LND arayüzünden `Bitcoin Wallet` adresinizi bulun, ardından `Yatır` düğmesine tıklayın. Zincir üzerinde bir alıcı adresi generated'dir: sats'i ona gönderin. Aktarmanız gereken miktar, ilk kanalınıza tahsis etmek istediğiniz kapasiteye bağlıdır, ancak hedeflenen kapasiteden biraz daha fazlasını göndermeniz gerektiğini unutmayın. Örneğin, 500.000 sats'lik bir kanal açmak istiyorsanız, tam olarak 500.000 sats değil, daha yüksek bir miktar gönderin.



![Image](assets/fr/032.webp)



İşlem yayınlandıktan sonra arayüzde görünür. Kanalı açmadan önce onaylanmasını bekleyin. Onaylandığında yanında yeşil bir ok göreceksiniz.



![Image](assets/fr/033.webp)



Ana arayüze kaydırın, ardından `+ KANAL AÇ` seçeneğine tıklayın.



![Image](assets/fr/034.webp)



Kanal açmak istediğiniz düğümün `Node ID`sini girin, kilitlemek istediğiniz miktarı belirtin ve ardından açılış işlem ücretini onchain ücret piyasasının durumuna göre ayarlayın. Elbette, önceden LND onchain portföyünüzde yeterli fon bulunduğundan emin olun.



Tüm parametreler ayarlandıktan sonra, `KANNEL AÇ` düğmesine tıklayın.



![Image](assets/fr/035.webp)



Açılış işleminin zincir üzerinde onaylanmasını bekleyin. İlk kanalınız artık resmi olarak faaliyette: tebrikler!



Şu an için kanalın likiditesinin %100'ünün benim tarafımda olduğunu görebilirsiniz: kanalı açan ben olduğum için bu normaldir. Ödemeler ve yönlendirme geliştikçe, bu dağılım değişecek, ancak kanalın toplam kapasitesi her zaman aynı kalacaktır.



![Image](assets/fr/036.webp)



Artık bir kanalınız olduğuna göre, seçilen düğümün ağa düzgün bir şekilde bağlı olması koşuluyla ilk Lightning ödemelerinizi yapabilirsiniz. Elbette, ilerleyen bölümlerde Lightning faturalarını cep telefonunuzdan ödemek için daha uygun bir yöntemin nasıl kurulacağına bakacağız. Ancak şimdilik, doğrudan LND'ten Umbrel'e ilk ödemeyi yapmayı deneyelim.



Bunu yapmak için, `Lightning Wallet` bölümünde `Gönder` düğmesine tıklayın, ardından ayarlanacak faturayı yapıştırın.



![Image](assets/fr/037.webp)



Fatura tutarı görüntülenir. Gönder düğmesine tıklayarak ödemeyi onaylayın.



![Image](assets/fr/038.webp)



Geçerli bir rota bulunursa, ilk Lightning ödemeniz başarılı olmalıdır.



![Image](assets/fr/039.webp)



Daha sonra kanaldaki likidite dağılımına bakarsak, eşimin şu anda kendi tarafında 5,002 sats olduğunu görürüz. Bu, az önce yaptığım ve alıcının düğümüne yönlendirdiği ödemenin 5.000 sats'sine karşılık gelir. Alıcı tam olarak 5.000 sats aldığı için ek 2 sats ödediğim yönlendirme ücretlerini temsil ediyor.



![Image](assets/fr/040.webp)



Ödemelerimizin güvenilirliğini artırmak için başka kanallar açmamız gerekeceği açıktır. Hedeflerimize bağlı olarak, Lightning üzerinden ödeme alabilmemiz için gelen likiditeyi kullanılabilir hale getirmenin bir yolunu bulmamız da gerekecektir. Bu, bir sonraki bölümün konusu olacaktır.



# Lightning düğümünüzü yönetme


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Düğüm operatörü profilinizi tanımlayın


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Artık Lightning düğümünüz hazır ve çalışır durumda olduğuna göre, bir sonraki adım yatırımcı profilinizi tanımlamaktır. Kanal açma stratejinizi, tercih ettiğiniz eşlerin türünü ve likiditeyi yönetme şeklinizi belirlediği için bu önemli bir seçimdir.



Lightning'de bunun işe yaraması için doğru yönde likiditeye ihtiyacınız vardır. Giden likidite, ödeme kabiliyetinize karşılık gelir (kanalların sizin tarafınızda bulunan sats). Gelen likidite ise alma kapasitenize karşılık gelir (eşlerinizin tarafında bulunan sats). Başka bir deyişle, profiliniz basit bir soruya indirgenir: sats'iniz çoğu zaman düğümünüzden çıkıyor mu, yoksa düğümünüze giriyor mu?



### Tüketici



Bu, kullanıcıların büyük çoğunluğunun profilidir. Düğümünüzü Lightning ödemeleri yapmak için kullanıyorsunuz: mal ve hizmet satın almak, fatura ödemek, bahşiş göndermek - kısacası, Lightning'i hızlı bir ödeme aracı olarak kullanmak için. Öte yandan, Lightning'den çok az veya sadece marjinal olarak, örneğin birkaç bağış, arkadaşlar arasında geri ödemeler veya birkaç mikro ödeme alıyorsunuz.



Bu profil yönetilmesi en kolay olanıdır, çünkü ana ihtiyacınız ödeme yapabilmektir. Pratik anlamda bu, giden likiditeye ihtiyacınız olduğu anlamına gelir. İstikrarlı, iyi bağlanmış düğümlere bir ya da daha fazla doğru boyutta kanal açtığınızda, giden ödemeleriniz mekanik olarak likiditeyi kanallarınızın diğer tarafına taşıyacaktır. İşte tam da bu hareket doğal olarak makul miktarda gelen likidite yaratır. Sonuç olarak, düzenli olarak alım yapmak istemeseniz bile, karmaşık bir strateji uygulamadan zaman zaman alım yapabileceksiniz. Dolayısıyla, gelen likiditeniz konusunda endişelenmenize gerek yoktur.



Bu LNP202 kursunda, Lightning'deki neredeyse tüm Bitcoin kullanıcılarına karşılık gelen bu "tüketici" düğüm operatörü profiline odaklanacağız.



### Perakendeci



Tüccar bir bakıma tüketicinin tam tersidir. Burada asıl amaç ödeme yapmak değil, tahsilat yapmaktır. Lightning kabul eden bir işletme, hizmet sağlayıcı, çevrimiçi mağaza veya satış noktası, bu düğümden çok sayıda gelen ödeme alacak ve nispeten az sayıda giden ödeme yapacaktır.



Lightning'de reddedilen bir ödeme potansiyel olarak kayıp bir satış anlamına geldiğinden, bu profil daha zorludur. Bu nedenle öncelik, gelen likidite haline gelir. Eğer node'unuzda yeterli gelen likidite yoksa, müşterileriniz paraları olsa bile ödemelerinin başarısız olduğunu görecektir, çünkü likiditeyi size doğru yönde ulaştıracak bir yol yoktur.



Tüccar için en büyük zorluk da kanalların doğal evriminden kaynaklanmaktadır. Tek yaptığınız almaksa, kanallarınız yavaş yavaş sizin tarafınızdan dolacaktır. Dolayısıyla, gelen likiditenizi korumak ve yenilemek için mekanizmalara ihtiyacınız vardır.



Bununla birlikte, daha basit bir durum vardır: karma tüketici/tüccar profili. Lightning üzerinden tahsilat yapıyor ve aynı zamanda Lightning üzerinden harcama yapıyorsanız (iş giderleri, tedarikçilere yapılan ödemeler ve hatta kişisel harcamalar), giden ödemeleriniz doğal olarak gelenleri yeniden oluşturur. Akışlar birbirini dengelediği için yönetim daha sorunsuz hale gelir ve yalnızca gelen likiditeyi geri kazanmak için tasarlanmış yapay mekanizmalara başvurmanıza daha az ihtiyaç duyarsınız.



### Yönlendirici



Yönlendirici belirli bir profildir. Lightning düğümünü ödeme yapmak veya tahsilat yapmak için değil, diğer kişilerin ödemelerini yönlendirmek ve ücretleri tahsil etmek için kullanır. Amaç, Lightning grafiği içinde kullanışlı, güvenilir ve ekonomik olarak rekabetçi bir rota olmaktır.



Dürüst olmak gerekirse, Lightning'de yönlendirici olmak göründüğünden daha karmaşık bir iştir ve kârlılık elde etmek zordur. Her şeyden önce, kanal açmak ve kapatmak zincir içi maliyetler açısından pahalıdır. Verimli bir şekilde yönlendirme yapmak için genellikle topolojinizi ayarlamanız, test etmeniz, düşük performans gösteren kanalları kapatmanız, yenilerini açmanız ve likiditenizi düzenli olarak yeniden dengelemeniz gerekir. İkincisi, rekabet çok şiddetli: büyük, yerleşik düğümler doğal olarak trafiğin büyük bir kısmını ele geçiriyor ve iyi büyüklükteki kanallara önemli miktarda sermaye bağlamadan bir yer edinmek zor.



Ayrıca yüksek bir operasyonel gereksinim de söz konusudur. Bir yönlendirme düğümü son derece istikrarlı olmalı, izlenmeli, uygun şekilde yedeklenmeli ve titizlikle yönetilmelidir. Kanal performansını izlemeniz, ücret politikanızı uyarlamanız, dengeli likiditeyi korumanız, eşleri yönetmeniz ve teknik sorunları hızla çözmeniz gerekir. Bu düzeyde bir katılım, teknik bir hobi veya altyapıya bir katkı olarak ilginç olabilir, ancak amacınız Lightning'i egemen bir şekilde kullanmaksa, para kazanmak için yönlendirmeye girmek nadiren önemlidir. Bu nedenle bu LNP202 kursu bu profili derinlemesine ele almamaktadır.



### Daha ileri gitmeden önce kendinizi net bir şekilde konumlandırın



Tüketici profiline uyuyorsanız, önceliğiniz basit bir yönetimle güvenilir bir şekilde ödeme yapabilmek olacaktır. Bir tüccarsanız, önceliğiniz hatasız bir şekilde nakde çevirmek olacaktır, bu da gelen bir likidite edinme stratejisi anlamına gelir. Yönlendirmeyi düşünüyorsanız, buna zorlu, ekonomik açıdan belirsiz ve zaman alıcı bir faaliyet olarak yaklaşmanız gerekir.



Bu profili şimdi tanımlamak, klasik bir tuzaktan kaçınmanıza yardımcı olacaktır: sadece ödeme yapmak isteyen bir kullanıcı olduğunuzda, bir tüccar veya yönlendirici için tasarlanmış bir kanal stratejisi uygulamak.



## Lightning düğüm yöneticisi kullanma


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Bu LNP202 eğitim kursunun önceki bölümünde, Umbrel üzerindeki `Lightning Node' uygulamasının temel arayüzünü kullandık. Bu arayüz temel işlemler (bakiyelerin kontrol edilmesi, nakit dağıtımının görüntülenmesi, kanalların açılması ve kapatılması) için yeterlidir, ancak kasıtlı olarak çok basitleştirilmiştir. Bu basitlik mevcut seçenekleri sınırlar ve LND düğümünüzün gelişmiş özelliklerinin çoğuna erişim sağlamaz. Bu nedenle, şimdi daha kapsamlı başka bir Lightning node yönetim yazılımı kullanacağız.



Bu ek yazılım sadece düğümünüz için tamamlayıcı bir yönetim arayüzü olacaktır. Bu, `Lightning Node` arayüzünü paralel olarak kullanmaya devam edebileceğiniz ve hatta isterseniz birkaç farklı arayüz kullanabileceğiniz anlamına gelir. Bunlar sadece aynı Lightning düğümü ile etkileşime geçmenin farklı yollarıdır.



En iyi bilinen yazılım programları arasında:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Üçü de iyi çözümlerdir. Dilerseniz, size en uygun olanı seçmeden önce üçünü de düğümünüzle test edebilirsiniz. Şahsen ben alışkanlıktan ve diğerlerinden daha eksiksiz göründüğü için ThunderHub'i kullanıyorum. Bu eğitim kursunda sunacağım araç budur, ancak diğer iki alternatiften birini de seçebilirsiniz. Plan ₿ Academy'de bu programların her biri için özel bir eğitimimiz var.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### ThunderHub'u kurun



Bu programların hepsi Umbrel Uygulama Mağazasından çok kolay bir şekilde kurulabilir. Dediğim gibi, burada ThunderHub'yi kullanacağız, ancak daha sonra başka bir tanesini test etmek isterseniz, prosedür benzer olacaktır.



![Image](assets/fr/041.webp)



Umbrel, ThunderHub'ye erişmeniz için size varsayılan bir parola sağlar. Kopyalayın: hemen ihtiyacınız olacak. Yazılımı her açtığınızda sizden isteneceği için parola yöneticinize kaydetmeyi de unutmayın.



![Image](assets/fr/042.webp)



Giriş`e tıklayın, ardından giriş yapmak için Umbrel tarafından sağlanan şifreyi yapıştırın.



![Image](assets/fr/043.webp)



Daha sonra Lightning düğümünüzle ilgili ana bilgileri görüntüleyen ThunderHub ana sayfasına yönlendirileceksiniz.



![Image](assets/fr/044.webp)



Başlangıç olarak, iki faktörlü kimlik doğrulamayı (2FA) etkinleştirmenizi tavsiye ederim. Ayarlarda, `2FA`yı etkinleştir` seçeneğinin yanındaki `Etkinleştir` seçeneğine tıklamanız ve ardından normal süreci takip etmeniz yeterlidir.



![Image](assets/fr/045.webp)



### ThunderHub kullanın



ThunderHub'nin öğrenilmesi nispeten kolaydır. Tüm menülere arayüzün sol sütunundan erişilebilir. Özetlemek gerekirse, işte her birinin ne yaptığı:




- ana sayfa: düğüme genel bakış, bakiyeler ve hızlı eylemler;
- gösterge tablosu: widget'lar ve metriklerle özelleştirilebilir gösterge tablosu;
- eşler: diğer Lightning düğümlerine olan bağlantıları görüntüleyin ve yönetin;
- kanallar': tam kanal yönetimi (likidite, ücretler, kapatma, vb.);
- rebalance": döngüsel ödemeler yoluyla kanalların yeniden dengelenmesi için bir araç;
- işlemler: gönderilen ve alınan Yıldırım ödemelerinin geçmişi;
- forwards`: düğümünüz tarafından generated yönlendirme istatistikleri ve maliyetleri;
- "Zincir": Bitcoin onchain portföyü (UTXO'lar ve işlemler);
- i̇zleme ve yedekleme için gW-201 entegrasyonu;
- araçlar: gelişmiş araçlar (yedeklemeler, raporlar, makaronlar, imzalar, vb.);
- takas: Boltz aracılığıyla yıldırım/zincir takasları;
- `Stats`: Lightning düğümünüzün genel istatistikleri ve performansı.



Bu fonksiyon seti ile Lightning düğümünüzü verimli bir şekilde yönetmek için ihtiyacınız olan tüm araçlara sahipsiniz. Her seçeneğe hemen ayrıntılı olarak hakim olmanız şart değil: bu kurs boyunca bunları aşamalı olarak inceleyeceğiz. Bununla birlikte, yazılımı daha derinlemesine kavramak istiyorsanız ThunderHub eğitimimize göz atın:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Burada en çok ilgilendiğimiz menü `Kanallar`. Düğümünüzdeki tüm kanalların likidite dağılımlarıyla birlikte ayrıntılı bir görünümünü sunar. Özellikle, hangi kanalların açık olduğunu `Açık`, hangilerinin açılmayı veya kapatılmayı beklediğini `Beklemede` ve hangilerinin zaten kapalı olduğunu `Kapalı` olarak görebilirsiniz.



![Image](assets/fr/047.webp)



Belirli bir kanal için eşin adına veya kanal kimliğine tıklayarak Amboss sayfasını açabilir ve daha fazla bilgi alabilirsiniz. Ayrıca, düğümünüz ödemeleri eşinizin düğümüne yönlendiriyorsa bu kanala uygulanan ücret politikası da dahil olmak üzere kanalın parametrelerini değiştirmek için kalem simgesine tıklayabilirsiniz.



![Image](assets/fr/048.webp)



Lightning düğümünüzü esas olarak bir "tüketici" olarak kullanıyorsanız, bu ücretleri değiştirmenize gerek yoktur: varsayılan değerleri koruyabilirsiniz. Öte yandan, Lightning'de yönlendirme ücretlerinin nasıl çalıştığını daha iyi anlamak istiyorsanız, LNP 201 eğitimini ve özellikle 4.1 bölümünü tavsiye ederim:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bir eşin yanındaki küçük çarpı işaretine tıklayarak bir kanalın kapatılmasını başlatabilirsiniz. Örneğin, bir eşin düzenli olarak aktif olmadığını fark ederseniz, sermayenizi daha güvenilir bir eşe yeniden tahsis etmek için bu kanalı kapatmak uygun olabilir.



O zaman iki seçeneğiniz var. Birincisi ve her zaman tercih edileni, işbirlikçi kapatmadır. Düğümünüz bu işlemi onaylayarak eşinizden kanalı ortaklaşa kapatmasını ister. Kabul ederse, zincir üzerinde kapanış işlemini yayınlayabilir ve fon payınızı geri alabilirsiniz. Bu yöntemin avantajları, işlem için zincir üzerindeki ücretleri seçmeniz, böylece gereksiz maliyetlerden kaçınmanız ve fonların herhangi bir zaman kilidi olmadan daha hızlı bir şekilde geri kazanılmasıdır.



![Image](assets/fr/049.webp)



İkinci seçenek zorla kapatmadır. Bu durumda, eşin onayını istemezsiniz ve elinizdeki son commitment transaction'i doğrudan yayınlarsınız. Son çare olmadıkça, örneğin eş sistematik olarak işbirliğine dayalı kapatmaları reddediyorsa veya artık yanıt vermiyorsa, bu yöntemi tavsiye etmem. Zorla kapatmanın iki büyük dezavantajı vardır: ücretler genellikle çok yüksektir, çünkü zincir içi ücretlerde bir artış öngörmek için önceden ayarlanmışlardır ve bir zaman kilidi tarafından engellendikleri için fonların geri alınmasında bir gecikme vardır. Bu zaman kilidi, eşinize bir hile girişimi durumunda tepki vermesi için zaman tanır (burada böyle bir durum söz konusu değildir, ancak yine de beklemeniz gerekir).



![Image](assets/fr/050.webp)



Son olarak, yeni bir kanal açmak için `Ana Sayfa` menüsüne gidin ve `Liquidity` bölümündeki `Kanal Aç` seçeneğine tıklayın. Daha sonra seçilen düğümün kimliğini, kanal kapasitesini, istenen Lightning yönlendirme ücretini ve açılış işlemi için zincir üzerindeki ücreti girebileceksiniz.



![Image](assets/fr/051.webp)



Bunlar ThunderHub üzerinde gerçekleştirmeniz gereken ana eylemlerdir. Bu LNP202 kursunda ilerledikçe diğer özellikleri de keşfedeceğiz.



## Gelen likiditenin elde edilmesi


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Gördüğünüz gibi, Lightning'de ödeme yapmak için giden likiditeye sahip olmak özellikle karmaşık değildir. Kendi inisiyatifinizle diğer düğümlere kanallar açmanız ve sats göndermeye başlamanız yeterlidir. Öte yandan, Lightning'de ödeme almak için gelen likiditeye sahip olmak daha karmaşıktır, çünkü ya size kanal açacak başka düğümlere ihtiyacınız vardır ya da ödeme yaparak likiditeyi kendiniz taşımanız gerekir.



Bir "tüketici" profili benimsiyorsanız, genellikle gelen likidite konusunda endişelenmenize gerek yoktur. Lightning düğümünü kullanımınız nakit para yerine ağırlıklı olarak ödeme odaklı olacaktır. Sadece birkaç Lightning ödemesi yaparak, zaman içinde doğal olarak gelen likidite yaratacaksınız.



Öte yandan, bir "tüccar" profiliniz varsa, durum tersine döner: esas olarak ödemeleri toplayacak ve bunlardan çok azını yapacaksınız. Dolayısıyla, gelen likidite için yalnızca kendi ödemelerinize güvenemezsiniz. Bu nedenle, diğer Lightning düğümlerinin sizinkine kanal açması gerekli hale gelir. Peki bu nasıl başarılabilir? Diğer operatörlerin sizin için sermaye bağlamasını nasıl sağlayabilirsiniz? Bu bölümde tam olarak bunu keşfedeceğiz.



### Gelen likiditenin satın alınması



Tahmin edebileceğiniz gibi, birini harekete geçirmenin en etkili yolu ona ödeme yapmaktır. Lightning düğümünüze gelen likidite için de prensip tamamen aynıdır. Kanalları düğümünüze getirmenin en basit yolu, hizmet ve ilgili sermaye bağlantısı için ödeme yapmaktır.



Bir işletme veya perakendeciyseniz, bu yaklaşım müşterilerinizden sürtünme olmadan ödeme toplamak için hızlı bir şekilde güvenilir kanallar elde edebileceğiniz anlamına gelir.



Gelen likidite satın almanın birçok yolu vardır. Şahsen kullandığım ve tavsiye ettiğim Amboss'in [Magma](https://magma.amboss.tech/) platformudur. Kullanımı çok kolaydır, bir kanal açmak hızlıdır ve oranlar genellikle makuldür. Magma, yapanlar ve alanlar olan bir pazar yeri gibi çalışıyor, ancak sürüm 2 deneyimi büyük ölçüde basitleştirdi: sadece bir talep oluşturun, Lightning aracılığıyla fiyatı ödeyin ve Magma otomatik olarak mevcut en iyi teklifle eşleştirin. Altı onchain onayından sonra, gelen likiditeye sahip kanalınız çalışmaya başlar. İşte nasıl çalıştığı:



Magma web sitesine] (https://magma.amboss.tech/buy), `Kanal Satın Al` bölümüne gidin.



![Image](assets/fr/052.webp)



Dilerseniz, satın alımlarınızı takip etmek için bir hesap oluşturabilirsiniz, ancak bu zorunlu değildir. Bir hesap oluşturmazsanız, Magma size sadece satın alımlarınızı daha sonraki bir tarihte geri almanızı sağlayacak bir oturum kimliği sağlayacaktır.



Siteye girdikten sonra, likidite satın almak için gerekli bilgileri doldurun. Tek seferlik bir satın alma işlemi için `Tek Seferlik` seçeneğini seçin, ardından gelen likidite için ödemek istediğiniz tutarı girin. Ödenen miktar ne kadar yüksek olursa, düğümünüze açılan kanalın kapasitesi de o kadar artar. Kanalın kapasitesine ilişkin bir tahmin aşağıda görünmektedir: nihai miktar Magma tarafından bulunan en iyi teklife bağlı olacağından, bu bir yaklaşık değerdir ve bazen daha yüksek, bazen daha düşük olabilir.



![Image](assets/fr/053.webp)



Ardından düğüm kimliğinizi girin. Örneğin, Umbrel üzerindeki `Lightning Node` uygulamasının `Node ID` menüsünde bulabilirsiniz.



![Image](assets/fr/054.webp)



Tüm bilgiler tamamlandıktan sonra, `İncele ve siparişi aç` düğmesine tıklayın.



![Image](assets/fr/055.webp)



Bir hesap oluşturmadıysanız, Magma size bir oturum anahtarı ve bir yedekleme dosyası sağlayacaktır. Bu iki öğeyi güvenli bir yerde saklayın, çünkü bunlar siparişi daha sonraki bir tarihte geri almanızı veya bir sorun olması durumunda durumunu takip etmenizi sağlayacaktır. Dosyayı kaydettikten sonra, `Pay with Lightning` düğmesine tıklayın.



![Image](assets/fr/056.webp)



Magma daha sonra seçtiğiniz tutar için bir Yıldırım faturası generate gönderir. Bunu ödemeniz gerekir. Lightning düğümünüzde zaten kanallarınız varsa, doğrudan ondan ödeme yapabilir veya başka bir harici Lightning wallet kullanabilirsiniz.



![Image](assets/fr/057.webp)



Ödeme yapıldıktan sonra, işlem Magma arayüzünde işleniyor olarak görünür.



![Image](assets/fr/058.webp)



Birkaç dakika sonra talep işleme alınır: Lightning düğümünüze sats ile bir kanal açılır. Açılış işlemi zincir üzerinde onaylandıktan sonra, ilgili gelen likiditeye erişebileceksiniz.



![Image](assets/fr/059.webp)



Magma ayrıca doğrudan ThunderHub'e entegre edilmiştir. Ana Sayfa sekmesinde, `Liquidity` bölümüne gidin ve `Gelen Liquidity Satın Al` seçeneğine tıklayın. Tek yapmanız gereken istediğiniz miktarı girmek ve onaylamaktır. ThunderHub ödemeyi düğümünüzden otomatik olarak aldığı için herhangi bir faturayı manuel olarak ödemenize gerek yoktur.



![Image](assets/fr/060.webp)



Bir tüccarsanız, bu tür bir hizmet özellikle uygundur, çünkü güvenilir düğümlerden hızlı bir şekilde büyük miktarda gelen likidite elde etmenizi sağlar ve müşterilerinizin size zorluk çekmeden ödeme yapabileceğini garanti eder. Öte yandan, özel bir kişiyseniz veya gelen likidite için ödeme yapmak istemiyorsanız, ücretsiz çözümler de vardır. Bir göz atalım.



### Kooperatif gelen likiditesi



Bir tüccar değilseniz ancak yine de gelen likiditeye ihtiyacınız varsa (örneğin, bazı ödemelerin yapılmasını beklerken başlangıçta düğümünüzü hazırlamak için) bunun için ödeme yapmak zorunda değilsiniz. Benim tercih ettiğim çözümlerden biri, gelen likiditeye ihtiyaç duyan diğer node operatörleriyle işbirliği yaparak birbirleri için Lightning kanalları açmaktır. Bu şekilde, bir kanal açmak size giden likidite getirirken, aynı zamanda size ücretsiz olarak gelen likidite sağlar (açılış için zincir üzerindeki ücretleri modüle ederek).



Elbette bunu doğrudan diğer bitcoin kullanıcılarıyla da düzenleyebilirsiniz. Ancak, bu tür dairesel açılışlara adanmış bir platform var: [Lightning Network +](https://lightningnetwork.plus/). Prensip, aynı kişiler arasında iki kanal açmak değil, en az üç katılımcıyı, hatta daha fazlasını içeren dairesel açılışlar kurmaktır.



Lightning Network+'ın nasıl çalıştığını anlamak için bir örnek verelim:




- A` isimli bir düğüm operatörü, iki kişiyle birlikte 1 milyon sats kanalı açmak istediğini belirten bir duyuru yayınlar;
- İlan, başka katılımcılar eklenene kadar aktif kalır;
- Daha sonra iki operatör, `B` ve `C`, `A` düğümü duyurusuna katılır. Üçgen artık tamamlanmıştır ve açılış aşaması başlayabilir.
- Düğüm `A`, düğüm `B`ye bir kanal açar;
- B düğümü C düğümüne bir kanal açar;
- Düğüm `C`, düğüm `A`ya bir kanal açar.



Operasyonun sonunda her düğüm 1 milyon sats giden likiditeye ve 1 milyon sats gelen likiditeye sahip olur. Bu şema dört ya da beş katılımcıya kadar genişletilebilir.



Elbette, bir katılımcının yaratmayı taahhüt ettiği kanalı gerçekten açacağını garanti edecek teknik bir mekanizma yoktur. Bu nedenle platform, operatörler taahhütlerini yerine getirdiğinde olumlu eleştirilere dayanan bir itibar sistemi kurmuştur. Ve en kötü senaryoda, işbirliği yapmayan biriyle karşılaşırsanız, herhangi bir para kaybetmiş olmayacaksınız: sadece gelen likidite için bir fırsatı kaçırmış olacaksınız.



Bu çözüm özellikle "tüketici" profiline uygundur, çünkü düğümünüzü diğer küçük operatörlere bağlarken gelen likiditeyi ücretsiz olarak elde etmenizi sağlar. Öte yandan, eğer bir tüccarsanız, bu yaklaşım genellikle uygun değildir: gelen likiditenin her bir satırı, giden likiditenin bir satırını bloke etmeyi gerektirir ve gelen likiditeye olan büyük ihtiyaçlarınız çok fazla sermaye bağlamayı gerektirir.



Lightning Network+'ı kullanmak için iki seçeneğiniz var: ya Umbrel'ye entegre edilmiş uygulamayı kullanın ya da klasik web sitesini kullanın ve düğümünüzden giriş yaparak bir hesap oluşturun. Entegre uygulama mevcut işlevlerin tamamını sunmadığı için ikincisini tavsiye ederim.



Lightning Network +](https://lightningnetwork.plus/) web sitesine gidin ve arayüzün sağ üst köşesindeki `Login` düğmesine tıklayın.



![Image](assets/fr/061.webp)



Kimliğinizi doğrulamak için, Lightning düğümünüzün özel anahtarını kullanarak sağlanan mesajı imzalamanız gerekir. ThunderHub ile bu işlem çok basittir. LN+ tarafından görüntülenen mesajı kopyalayarak başlayın.



![Image](assets/fr/062.webp)



ThunderHub'da `Araçlar` sekmesine gidin, ardından `Mesajlar` bölümündeki `İmzala` düğmesine tıklayın.



![Image](assets/fr/063.webp)



LN+ tarafından sağlanan kimlik doğrulama mesajını yapıştırın ve ardından `İmzala` düğmesine tıklayın.



![Image](assets/fr/064.webp)



ThunderHub daha sonra düğümünüzün özel anahtarını kullanarak bu mesajı imzalar. generated imzasını kopyalayın.



![Image](assets/fr/065.webp)



Bu imzayı LN+ sitesindeki ilgili alana yapıştırın ve ardından `Sign in` (Oturum aç) düğmesine tıklayın.



![Image](assets/fr/066.webp)



Artık Lightning düğümünüzle LN+'ya bağlısınız. Bu işlem, LN+'nın platformlarında talep ettiğiniz düğümün gerçek sahibi olduğunuzu doğrulamasını sağlar.



![Image](assets/fr/067.webp)



Dilerseniz LN+ profilinizi, örneğin kısa bir biyografi ekleyerek kişiselleştirebilirsiniz.



İlk dairesel kanal açılışınıza katılmak için, arayüzün üst kısmındaki `Takaslar' menüsüne gidin. Burada, düğümünüzün özelliklerine bağlı olarak şu anda mevcut olan tüm takasları bulacaksınız.



![Image](assets/fr/068.webp)



Mevcut bir takas teklifine katılmak için üzerine tıklamanız ve kaydolmanız yeterlidir. Bununla birlikte, LN+'da, bir takasın yaratıcısı katılımcılara minimum kanal sayısı veya minimum toplam düğüm kapasitesi gibi belirli koşullar getirebilir. Bu nedenle, özellikle ilk günlerde, düğümünüz için çok az teklifin mevcut olması mümkündür. Benim durumumda, halihazırda açık olan birkaç kanala rağmen, düğümüm için hiçbir teklif mevcut değildi. Bu yüzden kendi takasımı oluşturdum ve aynı durumdaysanız siz de aynısını yapabilirsiniz.



Liquidity Swap`ı Başlat`a tıklayın, ardından teklif parametrelerinizi girin:




- Toplam katılımcı sayısını seçin (3, 4 veya 5);
- Açılacak kanal miktarını belirtin (wallet zincirinizde en az bu miktarda kanal olduğundan emin olun);
- Kanal açık kalma süresini tanımlayın. Bu, katılımcıların kanalı kapatmamayı kabul ettikleri süredir;
- Sağ tarafta, katılımcılar için kısıtlamalar belirleyebilirsiniz: minimum kanal sayısı, minimum toplam kapasite ve kabul edilen bağlantı türü.



Tüm parametreler ayarlandıktan sonra, `Liquidity Swap`ı Başlat` düğmesine tıklayın.



![Image](assets/fr/069.webp)



Takas teklifiniz şimdi oluşturuldu. Şimdi tek yapmanız gereken diğer düğüm operatörlerinin kaydolmasını beklemek. Eğer koşullarınız çok kısıtlayıcı değilse, bu çok uzun sürmeyecektir. İlerleyen saatlerde veya günlerde takasınızın durumunu izlemeyi unutmayın.



![Image](assets/fr/070.webp)



Tüm takas yerleri alındı: şimdi kanal açma aşamasına geçiyoruz. Her katılımcı LN+ arayüzünden hangi düğüme bir Lightning kanalı açması gerektiğini görebilir.



![Image](assets/fr/084.webp)



Kendi tarafınızda, LN+ tarafından sağlanan Node ID'yi kullanarak ve belirtilen miktara uyarak kanalı açın. Önceki bölümlerde gördüğümüz gibi, bunu ThunderHub aracılığıyla, başka bir Lightning düğüm yöneticisiyle veya doğrudan temel Lightning Node uygulama arayüzünden yapabilirsiniz.



![Image](assets/fr/085.webp)



Açılış başlatıldıktan sonra, bekleyen kanallar bölümünde göründüğünü görebilirsiniz. Benim durumumda, bu `Plebian_fr` düğümüne sahip kanal.



![Image](assets/fr/086.webp)



Daha sonra kanal açmayı başlattığınızı onaylamak için LN+'a dönebilirsiniz. Bunun için `Kanal Açma Başlatıldı` düğmesine tıklamanız yeterlidir.



![Image](assets/fr/087.webp)



Diğer tüm katılımcılar da taahhüt ettikleri kanalı açtıklarında, onlara olumlu bir yorum bırakmayı unutmayın.



![Image](assets/fr/088.webp)



Zorluk veya gecikme durumunda, sayfanın altındaki yorumlar bölümü aracılığıyla meslektaşlarınızla doğrudan iletişime geçebilirsiniz.



![Image](assets/fr/089.webp)



Bazı katılımcılar kendilerine bir ödeme yaparak döngüsel kanalları en başından yeniden dengelemek isteyebilir. Bu, her kanalda dengeli bir nakit dağılımı sağlar. Eğer bir "tüketici" profilindeyseniz, bu gerekli değildir, ancak isterseniz bu yeniden dengelemeyi kendiniz yapabilir ya da bunu yapmak isteyen eşin işini kolaylaştırmak için kanal ücretlerinizi geçici olarak sıfıra ayarlayabilirsiniz. Bazen kimse bunu yapmak istemez.



![Image](assets/fr/090.webp)




# Lightning düğümünüzün potansiyelini açığa çıkarma


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Tailscale üzerinden bir mobil wallet bağlayın


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



İşte bu kadar, artık hem gelen hem de giden likiditeye sahip, iyi bağlanmış bir Lightning düğümünüz var. Böylece Lightning node'unuzu gerçek hayatta kullanmaya hazırsınız. Şimdiye kadar, her zaman doğrudan Umbrel üzerinde `Lightning Node` uygulaması veya `ThunderHub` arayüzü gibi arayüzler kullandık. Bu araçlar ödeme göndermek ve almak için çalışıyor, ancak günlük Lightning ödemeleri için açıkça optimize edilmemiş. Arayüz bir bilgisayarda kullanılmak üzere tasarlanmıştır, bir akıllı telefonda pratik değildir ve ayrıca düzgün çalışması için aynı ağa bağlantı gerektirir (Tor aracılığıyla uzaktan bağlanmak teknik olarak mümkün olsa da).



Pratikte, bitcoin kullanıcıları olarak aradığımız şey bir akıllı telefonda klasik bir Lightning wallet arayüzüdür: QR kodu aracılığıyla faturaları tarama yeteneği ve sats'yı ödemek ve nakde çevirmek için basit bir arayüz. Bu bölümde ve bir sonraki bölümde uygulayacağımız şey tam olarak budur. Genel fikir, akıllı telefonunuzda her yerden (sadece yerel ağınızdan değil) kullanılabilen, ancak arka planda ödeme göndermek ve almak için kendi Lightning düğümünüze dayanan bir mobil Lightning wallet uygulamasına sahip olmaktır.



### Mobil bir müşteriyi bağlamak için çözümler nelerdir?



Günümüzde, hem mobil uygulama hem de düğümünüz ile bu uygulama arasındaki bağlantı türü açısından bunu yapmanın çeşitli yolları vardır. Üç ana bağlantı modu şunlardır:




- ***Tor*** aracılığıyla;
- vPN ***Tailscale*** aracılığıyla;
- ***Nostr Wallet Connect*** aracılığıyla.



Birkaç yıl önce ***Tor*** üzerinden bağlanırdım, ancak kısa sürede bıraktım: arıza sayısı ve iletişim gecikmeleri çok fazlaydı. Teoride işe yarıyor, ancak pratikte kullanıcı deneyimi felaketti. Bu nedenle bu yaklaşıma karşı tavsiyede bulunuyorum.



Daha sonra benimsediğim alternatif, mobil uygulama ile düğüm arasındaki iletişimi sağlamak için bir ***Tailscale*** VPN kullanmak oldu. Bu çözüm çok iyi çalışıyor: düşük verimliliğe sahip mobil ağlarda bile, ödemelerim her zaman zorluk çekmeden gerçekleşiyor. Bu bölümde ilk olarak Zeus uygulaması ile tanıtacağım yöntem budur.



Bir sonraki bölümde, çok iyi çalışan başka, daha yeni bir çözüme bakacağız: ***Nostr Wallet Connect***. Bu kez size bir alternatif sunmak için Alby Go uygulamasını kullanacağız, ancak dilerseniz Zeus da NWC ile uyumludur.



### Tailscale'ün kurulması ve yapılandırılması



Bu ilk yöntem için Tailscale'e ihtiyacımız olacak. Bu, şifreleme, kimlik doğrulama ve NAT geçişini otomatik olarak yönetirken İnternet'e yayılmış cihazları güvenli bir şekilde bağlamanıza olanak tanıyan WireGuard tabanlı bir VPN çözümüdür. Basitçe söylemek gerekirse, tüm cihazlarınız İnternet üzerinde herhangi bir yerde olsalar bile yönlendiricinizle aynı LAN'a bağlıymış gibi.



Kullanmak için önce bir hesap oluşturun. Tailscale web sitesine gidin, ardından `Get Started` düğmesine tıklayın.



![Image](assets/fr/071.webp)



Ardından Tailscale hesabınız için bir kimlik sağlayıcı seçin. Şahsen ben oturum açmak için GitHub hesaplarımdan birini kullandım.



![Image](assets/fr/072.webp)



Giriş yaptıktan sonra, kullanımınız hakkında birkaç soru sorulacaktır. Devam etmek için bunları kısaca yanıtlayın.



![Image](assets/fr/073.webp)



Tailscale daha sonra makinenize bir istemci yüklemeyi teklif eder. Şu an için ilgilendiğimiz şey bu değil: doğrudan Umbrel'ye gidin ve App Store'dan Tailscale uygulamasını yükleyin.



![Image](assets/fr/074.webp)



Uygulama açıldığında, `Giriş Yap` seçeneğine tıklayın, ardından hesabınızı oluştururken kullandığınız yöntemi kullanarak kimlik doğrulama sürecini takip edin.



![Image](assets/fr/075.webp)



Onaylamak için `Bağlan` seçeneğine tıklayın. Umbrel'iniz artık VPN ağınıza bağlanmıştır.



![Image](assets/fr/076.webp)



Ardından Tailscale uygulamasını akıllı telefonunuza indirin ve aynı hesabı kullanarak oturum açın. Lütfen dikkat: Android'de aynı anda iki VPN kullanmak mümkün değildir. Tailscale'nin çalışması için diğer aktif VPN'leri devre dışı bırakmanız gerekir. Dahası, Lightning düğümünüzü Zeus aracılığıyla her kullanmak istediğinizde, Tailscale VPN'i etkinleştirmeniz gerekir, aksi takdirde bağlantı kurulmaz.



![Image](assets/fr/077.webp)



Tailscale sitesinde, artık en az iki istemci bağlı olduğuna göre, ağa bağlı tüm cihazlarınızın ve bunların Tailscale IP adreslerinin bir listesini içeren yönetim konsoluna erişebilirsiniz.



![Image](assets/fr/078.webp)



### Zeus'a Bağlanın



Zeus uygulamasını telefonunuza yükleyin. Açıldığında, `Gelişmiş Kurulum`u ve ardından `Bir wallet oluşturun veya bağlayın`ı seçin.



![Image](assets/fr/079.webp)



Wallet arayüzü` bölümünde `LND (REST)` öğesini seçin. Ardından Tailscale kontrol panelinizden veya doğrudan Umbrel'deki Tailscale uygulamasından bulabileceğiniz Umbrel'nizin Tailscale adresini girin. Bağlantı noktası için `8080` girin.



![Image](assets/fr/080.webp)



Zeus daha sonra sizden bir `Macaroon` sağlamanızı ister. Bu, bir uygulamaya (bu durumda Zeus) Lightning düğümünüzle etkileşime girmesi için verilen hakları tam olarak tanımlamanıza olanak tanıyan bir token yetkilendirmesidir. generate makaronu ThunderHub'dan, `Araçlar` menüsünden, `Bakery` alt menüsünden almak mümkündür, ancak bu amaç için en kolay yol doğrudan `Lightning Node` uygulamasından almaktır.



Arayüzün sağ üst köşesindeki üç küçük noktaya ve ardından `Wallet`ye Bağlan` seçeneğine tıklayın. İstirahat (Yerel Ağ)`ı seçin. Daha sonra uygun haklara sahip bir makaronu kopyalayabileceksiniz.



![Image](assets/fr/081.webp)



Zeus'ta ilgili alana yapıştırın, ardından `CÜZDAN KONFİGÜRÜNÜ KAYDET` düğmesine tıklayın.



![Image](assets/fr/082.webp)



Artık Lightning düğümünüze Zeus uygulamasından erişebilirsiniz. Bu, akıllı telefonunuzdan doğrudan Lightning düğümünüzde ödeme almak için generate faturalarını alabileceğiniz ve ayrıca nerede olursanız olun Lightning faturalarını ödeyebileceğiniz anlamına gelir.



![Image](assets/fr/083.webp)



İpucu: Tailscale, Lightning düğümünüzü uzaktan kullanmakla sınırlı değildir. Umbrel'unuzun tüm araçlarına diğer yazılımlardan, hatta uzaktan erişmenizi sağlar. Örneğin, Umbrel'unuzun Tailscale IP adresini kullanarak Bitcoin düğümünüzü (Electrs veya Fulcrum aracılığıyla) Tor üzerinden geçmeden Sparrow Wallet'e bağlayabilirsiniz. Bir kez daha, bu Tor'un doğasında olan yavaşlığı önler. Tailscale istemcisini bilgisayarınıza kurun ve ağınıza bağlayın.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Bir sonraki bölümde, bir mobil istemciyi Lightning düğümünüze bağlamanın eşit derecede etkili başka bir yolunu inceleyeceğiz: Nostr Wallet Connect. Zeus'tan farklı bir uygulama kullanacağız (Zeus da NWC ile uyumlu olmasına rağmen), yani Alby Go.



## NWC aracılığıyla mobil bir wallet bağlayın


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Tailscale bağlantısı sizi ikna etmediyse veya ikili VPN'i yönetmek çok zahmetli görünüyorsa, bu bölüm Lightning düğümünüz üzerinden sats için ödeme yapmak ve almak için uzak bir mobil istemci kullanmanın başka bir yolunu önermektedir: ***Nostr Wallet Bağlantısı***.



Bu örnek için, çok iyi tasarlanmış ve öğrenmesi özellikle kolay olan Alby Go mobil uygulamasını kullanacağız. Bununla birlikte, Zeus veya başka bir NWC uyumlu mobil uygulamayı da kullanabilirsiniz. Uyumlu uygulamaların bir listesini [the `awesome-nwc` GitHub repository](https://github.com/getAlby/awesome-nwc) adresinde bulabilirsiniz.



### Nostr Wallet Connect nasıl çalışır?



Nostr Wallet Connect, bir uygulamanın veya web sitesinin uzak bir Lightning düğümünde, bu düğümle doğrudan bir ağ bağlantısı kurmadan (API LND açıkta değil, VPN yok, `.onion` hizmeti yok...) eylemleri tetiklemesine olanak tanıyan standartlaştırılmış bir protokoldür. NWC, bir uygulamanın bir amacı (örneğin `pay_intece`) nasıl formüle ettiğini ve sonucu nasıl aldığını tanımlar.



Oldukça basit çalışır. Bir QR kodunu tarayarak veya `nostr+walletconnect:` derin bağlantısı aracılığıyla bir oturum başlatırsınız. Bu dize, oturum parametrelerini ve bir yetkilendirme sırrını içerir. Daha sonra, uygulama ödeme yapmak istediğinde, talebi serileştirir, şifreler ve bir Nostr rölesinde bir olay olarak yayınlar. Düğüm, röle üzerindeki olayı okur, şifresini çözer, yazarın bu oturum için yetkili olup olmadığını kontrol eder, ödemeyi gerçekleştirir ve ardından şifreli bir yanıt döndürür (ön görüntü ile başarı veya hata). Röle yalnızca bir aktarım aracısı olarak görev yapar: içeriği okuyamaz, ancak isteklerin zamanlamasını ve sıklığını gözlemleyebilir.



Tailscale veya Tor üzerinden bağlantı ile karşılaştırıldığında, NWC'nin ana avantajı düğümünüze dışarıdan doğrudan erişilememesidir. Bu, mobil kullanımı büyük ölçüde basitleştirir: düğümünüzün gelen bağlantıları kabul etmesi gerekmez, sadece bir röle ile iletişim kurabilmesi gerekir. Öte yandan, Nostr rölelerine işlevsel bir bağımlılık getirirsiniz: eğer kullanılamazlarsa, deneyim bozulur. Ayrıca, mesajlar şifrelenmiş olsa bile, röle belirli bir düzeyde etkinlik meta verisini gözlemleyebilir.



Güvenlik modellerindeki fark da önemlidir. Tailscale veya Tor ile son derece hassas sırlarla korunan düğümünüze (LND'nin API'i aracılığıyla) doğrudan erişim sağlarsınız. Bu güçlüdür, çünkü her şeyi yönetebilirsiniz, ancak aynı zamanda daha düşük katmanlı bir saldırı yüzeyidir. NWC ile erişim daha uygulamaya yöneliktir: yalnızca belirli eylemleri yetkilendiren bir token oturumunu yetkilendirirsiniz.



### Lightning düğümünüze Alby Hub'ü yükleyin



Önceden, Umbrel App Store'da özellikle NWC bağlantılarına adanmış bir uygulama vardı, ancak ne yazık ki bu artık mevcut değil. Artık bu tür bir bağlantı kurmak için Alby Hub kullanmanız gerekecek. Bunu yapmak için, Alby Hub uygulamasını doğrudan mağazadan yükleyerek başlayın.



![Image](assets/fr/091.webp)



Açılışta, giriş ekranlarını atlayın, ardından `Get Started (LND)` düğmesine tıklayın. Parantez içinde `LDK` değil `LND` yazdığını kontrol etmek önemlidir. Eğer `LND` görünüyorsa, bu Alby Hub'nın mevcut Lightning düğümünüzü doğru bir şekilde algıladığı ve kendisini bunun için arayüz olarak yapılandıracağı anlamına gelir. Öte yandan, `LDK` görüntülenirse, bu Alby Hub'nın düğümünüzü algılamadığını ve yeni bir tane oluşturmak üzere olduğunu gösterir, ki burada amaç bu değildir.



![Image](assets/fr/092.webp)



Daha sonra sizden bir Alby hesabı oluşturmanız istenecektir. NWC ile sınırlı kullanım için bu gerekli değildir, ancak Alby'in özel hizmetlerinden yararlanmak istiyorsanız bunu yapmak isteyebilirsiniz. Gerekmiyorsa, devam etmek için `Belki sonra` seçeneğine tıklayın.



![Image](assets/fr/093.webp)



Ardından güçlü, benzersiz bir parola seçin. Bu, düğümünüzdeki Alby Hub'a erişimi koruyacaktır. Parola yöneticinize kaydetmeyi unutmayın.



![Image](assets/fr/094.webp)



Bu sizi Alby Hub arayüzüne getirir. Lightning düğümünüzün ana yöneticisi olarak kullanmak istemiyorsanız, tüm yapılandırma sürecinden geçmeniz gerekmez. Daha önce gördüğümüz gibi, Alby Hub aslında düğümünüzün yönetimi için ThunderHub kullanımının yerini alabilir. Alby Hub'in seçenekleri hakkında daha fazla bilgi edinmek isterseniz, özel eğitimimize göz atın:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Bağlantılar menüsüne gidin.



![Image](assets/fr/095.webp)



Burada Lightning düğümünüze NWC aracılığıyla bağlanabilen tüm uygulamaları görebilirsiniz. Bunlar arasında bir önceki bölümde bahsedilen Zeus da bulunmaktadır. Burada, Alby Go'yi kullanacağız. Bağlantı işlemini başlatmak için Alby Go'ye ve ardından `Connect to Alby Go` düğmesine tıklayın.



![Image](assets/fr/096.webp)



### Alby Go'ün kurulumu ve bağlanması



Akıllı telefonunuza Alby Go uygulamasını yükleyin:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



Alby Hub'te, Lightning düğümünüzdeki Alby Go uygulamasına vermek istediğiniz hakları yapılandırın. Örneğin, dönem başına harcama limitleri, NWC bağlantısı için bir son kullanma tarihi belirleyebilir veya tüm kontrolü bırakabilirsiniz. Parametreleri ayarladıktan sonra `Sonraki` düğmesine tıklayın.



![Image](assets/fr/097.webp)



Alby Hub daha sonra Lightning düğümünüz ile Alby Go arasında NWC bağlantısı kurmak için generate bir QR kodu gönderir.



![Image](assets/fr/098.webp)



Alby Go uygulamasında, ilk açıldığında `Wallet`yi Bağla`ya tıklayın, ardından Alby Hub tarafından sağlanan QR kodunu tarayın.



![Image](assets/fr/099.webp)



Bu wallet'i tanımlamak için bir ad seçin. Artık Lightning düğümünüze Alby Go aracılığıyla uzaktan erişiminiz var. generate faturalarını düğümünüzde sats almak için kullanabilir veya Lightning faturalarını doğrudan onunla ayarlayabilirsiniz.



![Image](assets/fr/100.webp)



Örneğin, Alby Go arayüzünden 1543 sats gönderdim.



![Image](assets/fr/101.webp)



Umbrel'daki Lightning düğümümün temel arayüzüne gidersem, bu ödemenin gerçekten de düğümüm tarafından yapıldığını görebilirim.



![Image](assets/fr/102.webp)



Artık Lightning düğümünüzü her yerden nasıl kolayca kullanacağınızı biliyorsunuz.



## Lightning'de uzun ömürlü otonomi


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Bu LNP202 uygulamalı eğitiminin sonuna geldik. Artık Lightning Network'ı egemen bir şekilde kullanmak için ihtiyacınız olan temel bilgilere sahipsiniz: bir node'un gerçek rolünü, farklı yaklaşımların ödünleşimlerini anladınız ve tutarlı bir yedekleme ve koruma stratejisi ile Umbrel üzerinde bir LND örneği kurdunuz. Ayrıca ilk kanallarınızı açtınız, likiditeyi nasıl yöneteceğinizi öğrendiniz, ödemelerinizi günlük olarak güvenilir hale getirdiniz.



Operasyonel açıdan bakıldığında, düğümünüz artık bir bakım ritmine girmelidir. Önemli olan onu izlemek (çalışma süresi, senkronizasyon, kanal durumu, ödeme hataları, vb.), kararlı sürümler mevcut olduğunda Umbrel tarafından sunulan güncellemeleri uygulamak ve yedeklerinizin ve gözetleme kulesi yapılandırmanızın hala etkin olup olmadığını periyodik olarak kontrol etmektir.



Kanallar söz konusu olduğunda, pragmatik bir yaklaşım benimseyin: işinize yarayanları elinizde tutun, kalıcı olarak etkin olmayanları veya istikrarsız eşlerle ilişkili olanları kapatın ve sermayenizi kademeli olarak daha sağlam bir topolojiye doğru yeniden tahsis edin.



**Bu aşamadaki en yaygın tuzaklardan biri Lightning düğümünüze çok fazla sermaye ayırmaktır. Lightning düğümünüzün bir donanım wallet'ten çok daha az güvenli olduğunu ve kanallarınıza taahhüt edilen fonların kullanılabilirliğinin kusurlu kalan yedekleme mekanizmalarına bağlı olduğunu unutmayın. Bu nedenle, bir sorun olması durumunda kaybetmeyi göze alabileceğiniz makul miktarları tutmanız ve sats'nızın büyük kısmını her zaman zincir üzerindeki bir donanım wallet'te tutmanız çok önemlidir.



Araçlar söz konusu olduğunda, yeni gelişmelere karşı meraklı ve dikkatli olmanızı tavsiye ederim. Bu eğitim oturumunda, düğümünüzü yönetmek, bağlanabilirliği veya ödeme yapmak için uzaktan kullanım için olsun, bunlardan birkaçını keşfettik. Ancak, Lightning özellikle dinamik bir alandır. Her yıl yeni ve ilgili araçlar ortaya çıkıyor ve Umbrel'de de birçok yeni uygulama ortaya çıkıyor. Bu yeni gelişmeleri takip etmek, bu kursta sunulanlardan daha güçlü veya daha pratik çözümler keşfetmenizi sağlayabilir.



Eğitim cephesinde, eğer henüz yapmadıysanız, Fanis Michalakis'in LNP 201 teori kursunu almanızı şiddetle tavsiye ederim, Lightning Network'in çalışmasına adanmıştır. Bu LNP202 kursunda gerçekleştirilen manipülasyonları daha iyi anlamanıza yardımcı olacak ve düğümünüzün günlük yönetiminde size daha fazla güven verecektir.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Farklı bir bakış açısıyla, ancak bitcoin yolculuğunuz için aynı derecede önemli olarak, Ludovic Lars'ın Bitcoin'ün yaratılış tarihi hakkındaki mükemmel kursunu da tavsiye ederim.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Ancak devam etmeden önce, bu LNP202 kursunun bir incelemesini yazabilir ve elbette tüm içeriğini anladığınızı onaylamak için diplomayı alabilirsiniz.



# Son bölüm


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Yorumlar & Derecelendirmeler


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Final Sınavı


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Sonuç


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>