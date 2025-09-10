---
name: Bitcoin Geliştirme Felsefesi
goal: Bitcoin'in tasarım ilkelerine ilişkin derin bir felsefi anlayış geliştirin.
objectives: 

  - Bitcoin'nin temel savunma ödünleşimlerini ve mimari kararlarını analiz edin
  - Bitcoin protokolünde önerilen değişiklikleri ve yenilikleri nasıl değerlendireceğinizi öğrenin
  - On yılı aşkın Bitcoin Geliştirme geçmişini ve topluluk tartışmalarını sentezlemek
  - Yeni BIP'leri değerlendirirken eleştirel düşünme çerçevelerini uygulayın


---

# Bitcoin Geliştirme Felsefesine Derinlemesine Bakış



Bitcoin Geliştirme Felsefesi, Proof-of-Work, blok oluşturma ve işlem yaşam döngüsü gibi kavram ve süreçlerin temellerini zaten anlayan ve Bitcoin'nin tasarım ödünleri ve felsefesi hakkında daha derin bir anlayış kazanarak seviye atlamak isteyen Bitcoin geliştiricileri için bir kurstur.

Yeni geliştiricilerin on yılı aşkın bir süredir devam eden Bitcoin geliştirme ve kamuoyu tartışmalarından çıkarılan en önemli dersleri özümsemelerine yardımcı olurken, onlara yeni fikirleri (iyileri ve kötüleri!) değerlendirmeleri için faydalı bir bağlam sunacaktır.


### Ne beklemeliyiz?


Yukarıda belirtildiği gibi, bu Bitcoin geliştiricileri için pratik bir rehberdir. Bununla birlikte, Bitcoin geniş ve karmaşık bir konudur ve burada tüm yönlerini ele almamız mümkün değildir. Bu kursla, geliştirme faaliyetinizi başlatmak için gerekli özellikleri tartışmayı ve kendi başınıza daha fazla keşfetmenizi sağlamayı umuyoruz.


Bitcoin ile ilgilenen çok sayıda insan var; bazılarının karşıt görüşleri olduğu için burada çelişkili fikirleri ifade eden kaynaklar bulabilirsiniz. Ancak, biz her zaman görüşlerin önemli olmadığı gerçekler alanına bağlı kalmaya çalışıyoruz.


### Bunu kim yazdı?


Bu ders, ana yazarı Kalle Rosenbaum olan ve Linnéa Rosenbaum'un ortak yazar olarak katkıda bulunduğu aynı adlı kitaptan uyarlanmıştır.

Kitap, Bitcoin geliştirme hakkında bilgi edinmek isteyen geliştiriciler için eğitim programları yürüten bir geliştirme merkezi olan [Chaincode Labs] (https://learning.chaincode.com/) tarafından hazırlatılmış ve finanse edilmiştir.


+++



# Giriş

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Kursa genel bakış

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Bitcoin gelişim felsefesi hakkındaki bu PHI 301 kursuna hoş geldiniz.


Bitcoin bir kripto para biriminden çok daha fazlasıdır; merkeziyetsizlik, gizlilik, güvensizlik ve esneklik hakkında felsefi bir vizyona sahiptir. Bu eğitim, Bitcoin'ün teknik temellerine zaten aşina olan ve şimdi Bitcoin'ün tasarım ve yönetişiminin altında yatan ilkeler hakkındaki anlayışlarını derinleştirmek isteyen geliştiriciler için özel olarak tasarlanmıştır.


Bu kurs boyunca, Bitcoin'ün on yılı aşkın bir süredir gelişimine rehberlik eden temel değerler ve stratejiler hakkında netlik kazanacaksınız. Bu temaları derinlemesine inceleyerek, gelecekteki gelişmeleri güvenle değerlendirmek ve katkıda bulunmak için gereken eleştirel bakış açısını geliştireceksiniz.


### Bitcoin'in Temel Değerleri


Bitcoin'yı benzersiz kılan nedir? Bu bölüm, Bitcoin'nın tasarımının kalbindeki temel değerleri ortaya koymaktadır. Ağı tek bir varlığın kontrol etmemesini sağlayan temel taş olan **merkeziyetsizliği**; üçüncü taraflara bağımlılığı ortadan kaldırmanın anahtarı olan **güvensizliği**; hem bireysel özgürlük hem de sistem bütünlüğü için gerekli olan **mahremiyeti**; ve Bitcoin'nın ekonomik kimliğini şekillendiren kodlanmış kıtlık garantisi olan **sonsuz Supply**'yi keşfedeceksiniz. Bu kavramlara hakim olmak, Bitcoin'nın güçlü ve zayıf yönlerini tam olarak kavramanızı sağlayacaktır.


### Bitcoin Yönetişim


Bitcoin'un karmaşık yönetişim ortamında gezinmek teknik uzmanlıktan daha fazlasını gerektirir, Bitcoin'un fikir birliği ve karar alma konusundaki benzersiz yaklaşımını anlamayı gerektirir. Bu bölümde, protokol yükseltmeleri gibi kritik süreçlerin arkasındaki mekanizmaları ve felsefeleri, çekişmeli düşünmenin gerekliliğini, açık kaynaklı işbirliğinin gücünü, ölçeklendirmenin süregelen zorluklarını ve işler kaçınılmaz olarak ters gittiğinde gereken incelikli stratejileri inceleyeceksiniz. Bu bilgilerle donanmış olarak, sadece katılmak için değil, Bitcoin'un geleceğini etkili ve sorumlu bir şekilde şekillendirmek için de hazır olacaksınız.


Bitcoin yolculuğunuzda bir sonraki adımı atmaya hazır mısınız? Hadi başlayalım!


***N.B.**: Kurs sırasında Bitcoin ile ilgili bilmediğiniz terimlerle karşılaşırsanız, lütfen tanımları bulmak için [sözlüğe] (https://planb.network/resources/glossary) bakın.*




# Bitcoin Merkezi Değerler

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Adem-i Merkeziyetçilik

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Bu bölümde adem-i merkeziyetçiliğin ne olduğu ve Bitcoin'ün işleyebilmesi için neden gerekli olduğu analiz edilmektedir. Merkeziyetçilik ile

madencilerin ve tam düğümlerin merkezsizleştirilmesi ve Bitcoin'ün en merkezi özelliklerinden biri olan sansüre karşı direnç için masaya ne getirdiklerini tartışın.


Tartışma daha sonra, herhangi bir merkezi olmayan sistemin gerekli bir özelliği olan tarafsızlığı - ya da kullanıcılara, madencilere ve geliştiricilere karşı izinsizliği - anlamaya kaymaktadır. Son olarak, Hard gibi merkezi olmayan bir sistemi kavramanın ne kadar Bitcoin olabileceğine değiniyoruz ve bunu anlamanıza yardımcı olabilecek bazı zihinsel modeller sunuyoruz.


Herhangi bir merkezi kontrol noktası olmayan bir sistem *merkezi olmayan* olarak adlandırılır. Bitcoin, merkezi bir kontrol noktasına ya da daha doğrusu *merkezi bir sansür noktasına* sahip olmaktan kaçınmak için tasarlanmıştır.


Ademi merkeziyetçilik *sansüre direnç* elde etmek için bir araçtır.


Bitcoin'da adem-i merkeziyetçiliğin iki önemli yönü bulunmaktadır: Miner adem-i merkeziyetçilik ve Full node adem-i merkeziyetçilik.


Miner ademi merkeziyetçilik, işlemlerin herhangi bir merkezi kuruluş tarafından gerçekleştirilmediği veya koordine edilmediği gerçeğini ifade eder. Full node ademi merkeziyetçilik, blokların, yani madencilerin ürettiği verilerin doğrulanmasının birkaç güvenilir otorite tarafından değil, ağın ucunda, nihayetinde kullanıcıları tarafından yapılmasını ifade eder.


![](assets/decentralization-banner.webp)


### Miner ademi merkeziyetçilik



Bitcoin'ten önce dijital para birimleri yaratma girişimleri olmuştu, ancak bunların çoğu yönetişim ademi merkeziyetçiliği eksikliği ve sansür direnci nedeniyle başarısız oldu.


Bitcoin'teki Miner ademi merkeziyetçiliği, *işlemlerin sıralanmasının* tek bir varlık veya sabit bir varlık grubu tarafından gerçekleştirilmediği anlamına gelir. Buna katılmak isteyen tüm aktörler tarafından kolektif olarak gerçekleştirilir; bu madenci kolektifi dinamik bir kullanıcı kümesidir. Herkes istediği gibi katılabilir ya da ayrılabilir. Bu özellik Bitcoin'i sansüre dirençli hale getirir.


Bitcoin merkezileştirilmiş olsaydı, hükümetler gibi onu sansürlemek isteyenlere karşı savunmasız olurdu. Daha önceki dijital para yaratma girişimleriyle aynı kaderi paylaşacaktı. "Pegged Sidechains ile Blockchain İnovasyonlarını Etkinleştirmek" başlıklı [bir makalenin] (https://www.blockstream.com/sidechains.pdf) giriş bölümünde yazarlar, dijital paranın ilk versiyonlarının hasmane bir ortam için nasıl donanımlı olmadığını açıklamaktadır (ayrıca bir sonraki bölümdeki Hasmane Düşünme bölümüne bakınız).


David Chaum 1983 yılında, Double-spending'u önlemek için güvenilen merkezi bir sunucunun bulunduğu bir ortamda dijital parayı bir araştırma konusu olarak tanıttı. Bu merkezi güvenilir tarafın bireylere yönelik gizlilik riskini azaltmak ve değiştirilebilirliği sağlamak için Chaum, merkezi sunucunun imzalarının (madeni paraları temsil eden) bağlanmasını önlemek için kriptografik bir araç sağlamak için kullandığı kör imzayı tanıttı ve yine de merkezi sunucunun çift harcama önleme gerçekleştirmesine izin verdi.

Merkezi bir sunucu gereksinimi dijital paranın Aşil topuğu haline gelmiştir[Gri99]. Merkezi sunucunun imzasını birkaç imzacının eşik imzası ile değiştirerek bu tek hata noktasını dağıtmak mümkün olsa da, denetlenebilirlik açısından imzacıların farklı ve tanımlanabilir olması önemlidir. Her bir imzacı teker teker başarısız olabileceğinden ya da başarısızlığa uğratılabileceğinden, bu durum sistemi hala başarısızlığa karşı savunmasız bırakmaktadır.


İşlemleri sipariş etmek için merkezi bir sunucu kullanmanın yüksek sansür riski nedeniyle uygulanabilir bir seçenek olmadığı anlaşıldı. Merkezi sunucunun yerine, en az m tanesinin siparişi onaylaması gereken sabit bir n sunucu kümesinden oluşan bir federasyon kullanılsa bile, yine de zorluklar yaşanacaktı. Sorun gerçekten de kullanıcıların bu n sunucu kümesi üzerinde ve merkezi bir otoriteye güvenmeden kötü niyetli sunucuları iyi sunucularla nasıl değiştirecekleri konusunda anlaşmaları gereken bir soruna dönüşecektir.


Bitcoin'in sansürlenebilir olması halinde neler olabileceğini düşünelim. Sansürcü, işlemlerinin Blockchain'a girmesine izin vermeden önce kullanıcılara kendilerini tanıtmaları, paralarının nereden geldiğini veya bu parayla ne satın aldıklarını beyan etmeleri için baskı yapabilir.


Ayrıca, sansür direncinin olmaması, sansürcünün kullanıcıları yeni sistem kurallarını benimsemeye zorlamasına olanak tanıyacaktır. Örneğin, Supply parasını şişirmelerine ve böylece kendilerini zenginleştirmelerine izin veren bir değişiklik uygulayabilirler. Böyle bir durumda, blokları doğrulayan bir kullanıcının yeni kurallarla başa çıkmak için üç seçeneği olacaktır:



- Kabul edin: Değişiklikleri kabul edin ve Full node'e uyarlayın.
- Reddet: Değişiklikleri kabul etmeyi reddet; bu, sansürcünün blokları artık kullanıcının Full node'ü tarafından geçersiz sayıldığından, kullanıcıyı artık işlemleri işlemeyen bir sistemle baş başa bırakır.
- Taşıma: Yeni bir merkezi kontrol noktası atayın; tüm kullanıcılar nasıl koordine olacaklarını bulmalı ve ardından yeni merkezi kontrol noktası üzerinde anlaşmalıdır.


Eğer başarılı olurlarsa, sistemin eskisi kadar sansürlenebilir olduğu göz önüne alındığında, aynı sorunlar büyük olasılıkla gelecekte bir noktada yeniden ortaya çıkacaktır.


Bu seçeneklerin hiçbiri kullanıcı için faydalı değildir.


Bitcoin'yı diğer para sistemlerinden ayıran şey merkezsizleştirme yoluyla sansüre karşı dirençtir, ancak *Double-spending sorunu* nedeniyle bunu başarmak kolay bir şey değildir. Bu, hiç kimsenin aynı Coin'i iki kez harcayamayacağından emin olma sorunudur ve birçok insanın merkezi olmayan bir şekilde çözmenin imkansız olduğunu düşündüğü bir sorundur. Satoshi Nakamoto [Bitcoin whitepaper]'ında (https://planb.network/bitcoin.pdf) Double-spending sorununun nasıl çözüleceğini yazmıştır:


> Bu makalede, işlemlerin kronolojik sırasının generate hesaplamalı kanıtı için eşler arası dağıtılmış bir Timestamp sunucusu kullanarak Double-spending problemine bir çözüm öneriyoruz.


Burada kulağa tuhaf gelen "eşler arası dağıtılmış Timestamp sunucusu" ifadesini kullanıyor. Buradaki anahtar kelime *dağıtılmış* olup, bu bağlamda merkezi bir kontrol noktası olmadığı anlamına gelmektedir. Nakamoto daha sonra Proof-of-Work'nin nasıl bir çözüm olduğunu açıklamaya devam ediyor.

Yine de, hiç kimse bunu

[Gregory Maxwell Reddit'te] (https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), burada potansiyel %51 saldırılarını önlemek için madencilerin Hash gücünü sınırlamayı öneren birine yanıt veriyor:


> Bitcoin gibi merkezi olmayan bir sistemde halk seçimi kullanılır. Ancak merkezi olmayan bir sistemde sadece 'insanların' oylamasına sahip olamazsınız çünkü bu, merkezi bir tarafın insanlara oy kullanma yetkisi vermesini gerektirir. Bunun yerine, Bitcoin bilgi işlem gücünün oylamasını kullanır çünkü herhangi bir merkezi tarafın yardımı olmadan bilgi işlem gücünü doğrulamak mümkündür
üçüncü taraf.


Yazıda, merkezi olmayan Bitcoin ağının Proof-of-Work kullanımı yoluyla işlem sıralaması konusunda nasıl bir anlaşmaya varabileceği açıklanmaktadır.


Ardından, insanların Bitcoin'un ademi merkeziyetçilik özelliklerini önemsememesi veya anlamamasıyla karşılaştırıldığında, %51 saldırısının özellikle endişe verici olmadığını söyleyerek sonuca varıyor:


> Bitcoin için çok daha büyük bir risk, onu kullanan halkın anlamaması, umursamaması ve onu merkezi alternatiflere göre değerli kılan ademi merkeziyetçilik özelliklerini ilk etapta korumamasıdır.

Sonuç önemli bir sonuçtur. Eğer insanlar Bitcoin'nin sansüre karşı direncini temsil eden ademi merkeziyetçiliğini korumazlarsa, Bitcoin sansürün bir şey haline geleceği kadar merkezileşene kadar merkezileştirici güçlerin kurbanı olabilir. O zaman değer önerisinin tamamı olmasa da çoğu ortadan kalkar. Bu da bizi Full node ademi merkeziyetçiliği ile ilgili bir sonraki bölüme getiriyor.


### Full node ademi merkeziyetçilik



Yukarıdaki paragraflarda çoğunlukla Miner ademi merkeziyetçiliğinden ve madencilerin merkezileştirilmesinin sansüre nasıl izin verebileceğinden bahsettik. Ancak ademi merkeziyetçiliğin bir başka yönü daha var, yani *Full node ademi merkeziyetçiliği*.


Full node ademi merkeziyetçiliğinin önemi güvenilmezlikle ilgilidir. Bir kullanıcının, örneğin işletme maliyetindeki engelleyici bir artış nedeniyle kendi Full node'sını çalıştırmayı bıraktığını varsayalım. Bu durumda, Bitcoin ağı ile başka bir şekilde, muhtemelen web cüzdanları veya hafif cüzdanlar kullanarak etkileşime girmeleri gerekir, bu da bu hizmetlerin sağlayıcılarına belirli bir düzeyde güven gerektirir.


Kullanıcı, ağ mutabakat kurallarını doğrudan uygulamaktan başka birinin uygulayacağına güvenmeye geçer. Şimdi çoğu kullanıcının mutabakat uygulamasını güvenilir bir varlığa devrettiğini varsayalım. Bu durumda ağ hızla merkezileşebilir ve ağ kuralları komplo kuran kötü niyetli aktörler tarafından değiştirilebilir.


İçinde [a

Bitcoin Magazine makalesi] (https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446), Aaron van Wirdum, Bitcoin geliştiricileriyle merkeziyetsizlik hakkındaki görüşleri ve Bitcoin'in maksimum blok boyutunu artırmanın içerdiği riskler hakkında röportaj yapıyor. Bu tartışma, birçok kişinin daha fazla işlem hacmine izin vermek için blok boyutu sınırını artırmayı tartıştığı 2014-2017 döneminde bir Hot konusuydu.


Blok boyutunun artırılmasına karşı güçlü bir argüman, doğrulama maliyetini artırmasıdır Doğrulama maliyeti artarsa, bazı kullanıcıları tam düğümlerini çalıştırmayı bırakmaya itecektir. Bu da daha fazla insanın sistemi Trustless şekilde kullanamamasına yol açacaktır.


Pieter Wuille, Full node'in merkezileştirilmesinin risklerini açıkladığı makalede alıntı yapıyor:


> Çok sayıda şirket bir Full node çalıştırıyorsa, hepsinin farklı bir kural seti uygulamaya ikna edilmesi gerektiği anlamına gelir. Başka bir deyişle: blok doğrulamanın merkezsizleştirilmesi, mutabakat kurallarına ağırlıklarını veren şeydir.
> Ancak Full node sayısı çok düşerse, örneğin herkes aynı web-cüzdanlarını, borsaları ve SPV veya mobil cüzdanları kullandığı için, düzenleme bir gerçeklik haline gelebilir. Ve eğer yetkililer mutabakat kurallarını düzenleyebilirlerse, bu Bitcoin'ü Bitcoin yapan her şeyi değiştirebilecekleri anlamına gelir. Hatta 21 milyon Bitcoin limitini bile.

İşte bu kadar. Bitcoin kullanıcıları, düzenleyicileri ve büyük şirketleri mutabakat kurallarını değiştirmeye çalışmaktan caydırmak için kendi tam düğümlerini çalıştırmalıdır.


### Tarafsızlık



Bitcoin tarafsızdır ya da insanların dediği gibi izinsizdir. Bu, Bitcoin'nın kim olduğunuzu veya onu ne için kullandığınızı umursamadığı anlamına gelir.


Bitcoin tarafsızdır, ki bu iyi bir şeydir ve çalışabilmesinin tek yoludur. Eğer bir kuruluş tarafından kontrol ediliyor olsaydı, sadece başka bir sanal nesne türü olurdu ve hiç ilgilenmezdim


Kurallara göre oynadığınız sürece, kimseden izin istemeden istediğiniz gibi kullanmakta özgürsünüz. Buna *Mining*, *içinde işlem yapma* ve *Bitcoin'in üzerine protokoller ve hizmetler inşa etme* dahildir:



- Eğer *Mining* izinli bir süreç olsaydı, kimin madencilik yapmasına izin verileceğini seçecek merkezi bir otoriteye ihtiyacımız olurdu. Bu da büyük olasılıkla madencilerin yasal sözleşmeler imzalamak zorunda kalmalarına yol açacaktır

işlemlerin merkezi otoritenin kaprislerine göre sansürlenmesi, en başta Mining'in amacına aykırıdır.



- Eğer Bitcoin'de *işlem yapan* kişiler kişisel bilgilerini vermek, işlemlerinin ne için olduğunu beyan etmek veya işlem yapmaya layık olduklarını başka bir şekilde kanıtlamak zorunda olsalardı, kullanıcıları veya işlemleri onaylamak için merkezi bir otorite noktasına da ihtiyacımız olurdu. Bu da yine sansüre ve dışlanmaya yol açacaktır.



- Eğer geliştiriciler Bitcoin'ün üzerine *protokoller* inşa etmek için izin almak zorunda kalsalardı, sadece merkezi geliştirici onay komitesinin izin verdiği protokoller geliştirilebilirdi. Bu durum, devlet müdahalesi nedeniyle kaçınılmaz olarak tüm gizliliği koruyan protokolleri ve ademi merkeziyetçiliği geliştirmeye yönelik tüm girişimleri dışlayacaktır.


Her düzeyde, Bitcoin'ü kimin ne için kullanacağına dair kısıtlamalar getirmeye çalışmak, Bitcoin'e artık değer teklifini karşılayamayacağı noktaya kadar zarar verecektir.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518 [Stack Exchange ile ilgili bir soruyu yanıtlıyor] Blockchain'nın normal veritabanlarıyla nasıl ilişkili olduğu hakkında. Proof-of-Work'in ekonomik teşviklerle birlikte kullanılmasıyla izinsizliğin nasıl elde edilebileceğini açıklıyor.


Sonuca varıyor:


> PoW gibi Trustless konsensüs algoritmalarını kullanmak, başka hiçbir yapının size vermediği bir şey katar (izinsiz katılım, yani değişikliklerinizi sansürleyebilecek belirli bir katılımcı grubu yoktur), PoW gibi Trustless konsensüs algoritmalarını kullanmak bir şey katmaz, ancak yüksek bir maliyetle gelir ve ekonomik varsayımları, onu hemen hemen yalnızca kendi kripto para birimini tanımlayan sistemler için yararlı kılar.
> Muhtemelen dünyada bunlardan gerçekten kullanılmış bir veya birkaç tane için sadece bir yer vardır.

İzinsizliğe ulaşmak için, sistemin büyük olasılıkla kendi para birimine ihtiyaç duyduğunu ve böylece "kullanım durumlarını etkili bir şekilde sadece kripto para birimleriyle sınırladığını" açıklıyor. Bunun nedeni, izinsiz katılımın ya da Mining'ın, sistemin içine yerleştirilmiş ekonomik teşvikler gerektirmesidir.


### Ademi merkeziyetçiliği kavramak



Bitcoin'in ilgi çekici bir yönü, onu kimsenin kontrol etmediğini kavramanın ne kadar Hard olduğudur. Bitcoin'de komiteler ya da yöneticiler yoktur. Gregory Maxwell, yine [Bitcoin subreddit'inde] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), bunu ilgi çekici bir şekilde İngilizce diliyle karşılaştırıyor:


> Pek çok insan otonom sistemleri anlamakta zorlanıyor, hayatlarında İngilizce gibi pek çok şey var-- ama insanlar bunları kanıksıyor ve sistem olarak düşünmüyorlar bile. Bir 'şey' olarak düşündükleri her şeyin onu kontrol eden bir otoriteye sahip olduğu merkezi bir düşünce tarzına saplanıp kalmışlardır.
>

> Bitcoin hiçbir şeye odaklanmaz. Bitcoin'ü benimsemiş olan çeşitli insanlar kendi özgür iradeleriyle bunu teşvik etmeyi seçmişlerdir ve bunu nasıl yapacakları kendi bilecekleri iştir. Otorite saplantılı insanlar bu faaliyetleri görüp bunların Bitcoin otoritesinin bir operasyonu olduğuna inanabilirler, ancak böyle bir otorite yoktur.


Bitcoin'in ademi merkeziyetçilik yoluyla çalışma şekli, doğadaki birçok tür arasında bulunan olağanüstü kolektif zekaya benziyor. Bilgisayar bilimcisi Radhika Nagpal bir [Ted konuşmasında] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) balık sürülerinin kolektif davranışları ve bilim insanlarının robotları kullanarak bunu nasıl taklit etmeye çalıştıkları hakkında konuşuyor.


> İkincisi ve benim hala en dikkat çekici bulduğum şey, bu balık sürüsünü yöneten bir lider olmadığını bilmemizdir. Bunun yerine, bu inanılmaz kolektif akıl davranışı tamamen bir balığın diğeriyle etkileşiminden ortaya çıkıyor.
> Her nasılsa, komşu balıklar arasında her şeyin yolunda gitmesini sağlayan bu etkileşimler veya angajman kuralları vardır.

Doğal ya da yapay pek çok sistemin liderler olmadan da çalışabildiğine ve çalıştığına, güçlü ve dirençli olduklarına dikkat çekiyor. Her bir birey yalnızca yakın çevresiyle etkileşim halindedir, ancak birlikte muazzam bir şey oluştururlar.


![](assets/fishschool.webp)

*Balık sürülerinin liderleri yoktur*


Bitcoin hakkında ne düşünürseniz düşünün, merkezi olmayan yapısı kontrol edilmesini zorlaştırıyor. Bitcoin var ve bu konuda yapabileceğiniz hiçbir şey yok. Bu üzerinde çalışılması gereken bir şey, tartışılması değil.


### Yerinden Yönetim Hakkında Sonuç


Full node ademi merkeziyetçilik ile Mining ademi merkeziyetçilik arasında ayrım yapıyoruz. Mining ademi merkeziyetçilik sansüre karşı direnç elde etmek için bir araçken, Full node ademi merkeziyetçilik ağın konsensüs kurallarının kullanıcılar arasında geniş bir destek olmadan değişmesini Hard sağlayan şeydir.


Bitcoin'ün merkezi olmayan yapısı, geliştiricilere, kullanıcılara ve madencilere karşı tarafsızlığa izin verir. Herkes izin istemeden katılmakta özgürdür.


Merkezi olmayan sistemleri anlamak Hard olabilir, ancak yardımcı olabilecek bazı zihinsel modeller vardır, örneğin İngilizce dili veya balık okulları gibi.


## Güvenilmezlik

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Bu bölüm güvenilmezlik kavramını, bilgisayar bilimleri açısından ne anlama geldiğini ve Bitcoin'ün değer önerisini korumak için neden Trustless olması gerektiğini incelemektedir.

Daha sonra Bitcoin'yı Trustless şeklinde kullanmanın ne anlama geldiğini ve bir Full node'ün size ne tür garantiler verip veremeyeceğini konuşuyoruz.

Son bölümde, Bitcoin ile gerçek yazılımlar veya kullanıcılar arasındaki gerçek dünya etkileşimine ve herhangi bir şeyi yapabilmek için kolaylık ve güvenilmezlik arasında değiş tokuş yapma ihtiyacına bakıyoruz.


İnsanlar sık sık "Bitcoin harika çünkü Trustless" gibi şeyler söylüyor.


Trustless ile ne demek istiyorlar? Pieter Wuille bu yaygın kullanılan terimi [Stack Exchange] (https://Bitcoin.stackexchange.com/a/45674/69518) adresinde açıklıyor:


> "Trustless "te bahsettiğimiz güven soyut bir teknik terimdir. Dağıtılmış bir sistem, düzgün çalışması için herhangi bir güvenilir tarafa ihtiyaç duymadığında Trustless olarak adlandırılır.

Kısacası, *Trustless* kelimesi Bitcoin protokolünün mantıksal olarak "herhangi bir güvenilir taraf" olmadan çalışabilmesini sağlayan bir özelliğine atıfta bulunmaktadır. Bu, kaçınılmaz olarak çalıştırdığınız yazılım ya da donanıma duymak zorunda olduğunuz güvenden farklıdır. Güvenin bu ikinci yönü hakkında daha fazla bilgi bu bölümün ilerleyen kısımlarında ele alınacaktır.


Merkezi sistemlerde, merkezi bir aktörün güvenliğe dikkat edeceğinden ya da sorun çıkması halinde geri adım atacağından emin olmak için itibarına ve herhangi bir ihlali yaptırıma bağlayacak yasal sisteme güveniriz. Bu güven gereksinimleri takma isimli merkezi olmayan sistemlerde sorunludur - rücu imkanı yoktur, bu nedenle gerçekten herhangi bir güven olamaz. Bitcoin whitepaper]'ın (https://Bitcoin.org/Bitcoin.pdf) giriş bölümünde Satoshi Nakamoto bu sorunu açıklamaktadır:


> İnternet üzerinden yapılan ticaret, elektronik ödemelerin işlenmesi için neredeyse yalnızca güvenilir üçüncü taraflar olarak hizmet veren finans kuruluşlarına dayanır hale gelmiştir.
> Sistem çoğu işlem için yeterince iyi çalışıyor olsa da, güvene dayalı modelin doğasında var olan zayıflıklardan muzdariptir.  Finansal kurumlar anlaşmazlıklara aracılık etmekten kaçınamayacağı için tamamen geri döndürülemez işlemler gerçekten mümkün değildir. Arabuluculuk maliyeti işlem maliyetlerini artırmakta, minimum pratik işlem boyutunu sınırlamakta ve küçük gündelik işlem olasılığını ortadan kaldırmaktadır ve geri döndürülemeyen hizmetler için geri döndürülemeyen ödemeler yapma yeteneğinin kaybedilmesinde daha geniş bir maliyet vardır.
> Tersine dönme olasılığı ile birlikte güven ihtiyacı yayılır. Tüccarlar müşterilerine karşı dikkatli olmalı, onları normalde ihtiyaç duyacaklarından daha fazla bilgi için zorlamalıdır.  Dolandırıcılığın belirli bir yüzdesi kaçınılmaz olarak kabul edilmektedir. Bu maliyetler ve ödeme belirsizlikleri fiziksel para birimi kullanılarak bizzat önlenebilir, ancak güvenilir bir taraf olmadan bir iletişim kanalı üzerinden ödeme yapmak için hiçbir mekanizma mevcut değildir

Görünüşe göre güvene dayalı merkezi olmayan bir sisteme sahip olamayız ve bu yüzden Bitcoin'de güvensizlik önemlidir.


Bitcoin'yi Trustless tarzında kullanmak için, tam doğrulamalı bir Bitcoin düğümü çalıştırmanız gerekir. Ancak o zaman başkalarından aldığınız blokların mutabakat kurallarına uyduğunu doğrulayabilirsiniz; örneğin, Coin ihraç programına uyulduğunu ve Blockchain'da çifte harcama yapılmadığını. Bir Full node çalıştırmıyorsanız, Bitcoin bloklarının doğrulanmasını başka birine yaptırırsınız ve size doğruyu söyleyeceklerine güvenirsiniz, bu da Bitcoin'yi güvenle kullanmadığınız anlamına gelir.


David Harding, [Bitcoin.org web sitesinde] (https://Bitcoin.org/en/Bitcoin-core/features/validation) Full node çalıştırmanın - veya Bitcoin'i güvenle kullanmanın - aslında size nasıl yardımcı olduğunu açıklayan bir makale yazdı:


> Bitcoin para birimi yalnızca insanlar Exchange'daki bitcoinleri diğer değerli şeyler için kabul ettiğinde çalışır. Bu, ona değer veren ve Bitcoin'nin nasıl çalışması gerektiğine karar verenlerin bitcoinleri kabul eden insanlar olduğu anlamına gelir.
>

> Bitcoin kabul ettiğinizde, Bitcoin'in kurallarını uygulama gücüne sahip olursunuz; örneğin, herhangi bir kişinin bitcoinlerine, o kişinin özel anahtarlarına erişimi olmadan el konulmasını önlersiniz.
>

> Ne yazık ki, birçok kullanıcı yaptırım gücünü dışarıdan temin etmektedir. Bu da Bitcoin'un ademi merkeziyetçiliğini, bir avuç madencinin bir avuç banka ve ücretsiz hizmetle işbirliği yaparak Bitcoin'un kurallarını, güçlerini dış kaynak olarak kullanan ve doğrulama yapmayan tüm kullanıcılar için değiştirebileceği zayıf bir durumda bırakmaktadır.
>

> Diğer cüzdanların aksine, Bitcoin core kuralları uygulamaktadır; bu nedenle madenciler ve bankalar doğrulama yapmayan kullanıcıları için kuralları değiştirirse, bu kullanıcılar sizin gibi tam doğrulama yapan Bitcoin core kullanıcılarına ödeme yapamayacaktır.


Bir Full node çalıştırmanın, başkalarından aldığınız coinlerin gerçek olduğundan emin olmak için Blockchain'in her yönünü başka kimseye güvenmeden doğrulamanıza yardımcı olacağını söylüyor. Bu harika, ancak Full node'nin size yardımcı olamayacağı önemli bir şey var: zincirin yeniden yazılması yoluyla çifte harcamayı önleyemez:


> Bitcoin core de dahil olmak üzere tüm programlar zincirin yeniden yazılmasına karşı savunmasız olsa da Bitcoin'ün bir savunma mekanizması sağladığını unutmayın: işlemleriniz ne kadar çok onay alırsa o kadar güvende olursunuz. Bundan daha iyi bilinen bir merkezi olmayan savunma yoktur.

Yazılımınız ne kadar gelişmiş olursa olsun, coin'lerinizi içeren blokların yeniden yazılmayacağına güvenmeniz gerekir. Bununla birlikte, Harding'in de belirttiği gibi, bir dizi onay bekleyebilir ve ardından zincirin yeniden yazılma olasılığını kabul edilebilir olacak kadar küçük görebilirsiniz.


Bitcoin'yi Trustless şeklinde kullanmaya yönelik teşvikler, sistemin Full node ademi merkeziyetçilik ihtiyacı ile uyumludur. Ne kadar çok kişi kendi tam düğümlerini kullanırsa, Full node ademi merkeziyetçilik o kadar artar ve böylece Bitcoin protokoldeki kötü niyetli değişikliklere karşı o kadar güçlü durur. Ancak ne yazık ki, Full node ademi merkeziyetçilik bölümünde açıklandığı gibi, kullanıcılar genellikle güvenilmezlik ve kolaylık arasındaki kaçınılmaz değiş tokuşun bir sonucu olarak güvenilir hizmetleri tercih etmektedir.


Bitcoin'in güvenilmezliği sistem açısından kesinlikle zorunludur. 2018'de Matt Corallo, Riga'daki Baltık Honeybadger konferansında [güvenilmezlik hakkında konuştu] (https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/).


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


Bu konuşmanın özü, güvenilir bir sistemin üzerine Trustless sistemleri kuramayacağınız, ancak bir Trustless sisteminin üzerine güvenilir sistemler - örneğin, bir gözetim Wallet - kurabileceğinizdir.



![width=50%](assets/trust.webp)


Bir Trustless tabanı Layer, daha yüksek seviyelerde çeşitli ödünleşimlere izin verir


Bu güvenlik modeli, sistem tasarımcısının ödünleşimleri seçmesine olanak tanır

başkalarını zorlamadan kendileri için mantıklı olan değiş tokuşları yapabilirler.


### Güvenmeyin, doğrulayın



Bitcoin güvenle çalışır, ancak yine de yazılımınıza ve donanımınıza bir dereceye kadar güvenmeniz gerekir. Çünkü yazılımınız veya donanımınız kutunun üzerinde belirtilenleri yapmak üzere programlanmamış olabilir. Örneğin:



- CPU, özel anahtar kriptografik işlemlerini tespit etmek ve özel anahtar verilerini sızdırmak için kötü niyetli olarak tasarlanmış olabilir.
- İşletim sisteminin rastgele sayı üreteci iddia ettiği kadar rastgele olmayabilir.
- Bitcoin core, özel anahtarlarınızı bazı kötü aktörlere gönderecek bir kodu gizlice yerleştirmiş olabilir.


Dolayısıyla, bir Full node çalıştırmanın yanı sıra, amaçladığınız şeyi çalıştırdığınızdan da emin olmanız gerekir. Reddit kullanıcısı brianddk [bir makale yazdı] (https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) yazılımınızı doğrularken seçebileceğiniz çeşitli güven seviyeleri hakkında. "Kuruculara güvenmek" bölümünde, tekrarlanabilir yapılardan bahsediyor:


> Yeniden üretilebilir yapılar, yazılımı tasarlamanın bir yoludur, böylece birçok topluluk geliştiricisinin her biri yazılımı oluşturabilir ve oluşturulan son yükleyicinin diğer geliştiricilerin ürettikleriyle aynı olmasını sağlayabilir. Bitcoin gibi herkese açık, tekrarlanabilir bir projede tek bir geliştiriciye tamamen güvenilmesi gerekmez. Birçok geliştiricinin hepsi derleme işlemini gerçekleştirebilir ve orijinal kurucunun dijital olarak imzaladığı dosyayla aynı dosyayı ürettiklerini doğrulayabilir.

Makale 5 güven seviyesi tanımlıyor: siteye, kuruculara, derleyiciye, çekirdeğe ve donanıma güvenmek.


Tekrarlanabilir derlemeler konusunu daha da derinleştirmek için Carl Dong [Guix hakkında bir sunum yaptı] (https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) ve işletim sistemine, kütüphanelere ve derleyicilere güvenmenin neden sorunlu olabileceğini ve bugün Bitcoin core tarafından kullanılan Guix adlı bir sistemle bunun nasıl düzeltileceğini açıkladı.


> Peki, araç zincirimizin tekrarlanabilir şekilde kötü niyetli olabilecek bir grup güvenilir ikili dosyaya sahip olabileceği gerçeği konusunda ne yapabiliriz? Tekrar üretilebilir olmaktan daha fazlasına ihtiyacımız var. Bootstrappable olmamız gerekiyor. Başka kuruluşlar tarafından kontrol edilen harici sunuculardan indirmemiz ve güvenmemiz gereken çok sayıda ikili araca sahip olamayız.
>

> Bu araçların nasıl oluşturulduğunu ve tercihen çok daha küçük bir güvenilir ikili dosyalar kümesinden bunları yeniden oluşturma sürecinden nasıl geçebileceğimizi tam olarak bilmeliyiz. Güvenilir ikili dosyalarımızı mümkün olduğunca en aza indirmemiz ve bu araç zincirlerinden Bitcoin'yi nasıl oluşturacağımıza kadar kolayca denetlenebilir bir yola sahip olmamız gerekir. Bu, doğrulamayı en üst düzeye çıkarmamızı ve güveni en aza indirmemizi sağlar.

Daha sonra Guix'in sadece 357 baytlık minimal bir ikiliye güvenmemize nasıl izin verdiğini açıklıyor; bu ikiliyi doğrulayabilir ve talimatları nasıl yorumlayacağınızı biliyorsanız tam olarak anlayabilirsiniz. Bu oldukça dikkat çekicidir: 357 baytlık ikilinin yapması gerekeni yaptığı doğrulanır, ardından kaynak koddan tam derleme sistemini oluşturmak için kullanılır ve başka herhangi birinin derlemesinin tam bir kopyası olması gereken bir Bitcoin core ikilisi ile sonuçlanır.


Pek çok bitcoin kullanıcısının benimsediği bir mantra var ve bu mantra yukarıdakilerin çoğunu iyi bir şekilde özetliyor:


> Güvenmeyin, doğrulayın.

Bu, eski ABD başkanı Ronald Reagan'ın nükleer silahsızlanma bağlamında kullandığı "[güven, ama doğrula](https://en.wikipedia.org/wiki/Trust,_but_verify)" ifadesine gönderme yapmaktadır. [Bitcoin'ciler](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) güvenin reddini ve bir Full node çalıştırmanın önemini vurgulamak için bunu değiştirdi.


Kullandıkları yazılımı ve aldıkları Blockchain verilerini ne derece doğrulamak istediklerine karar vermek kullanıcılara kalmıştır. Bitcoin'teki diğer pek çok şeyde olduğu gibi, kolaylık ve güvenilirlik arasında bir denge vardır. Bitcoin core'ü kendi donanımınızda çalıştırmaktansa, gözetim altındaki bir Wallet'yı kullanmak neredeyse her zaman daha uygundur. Bununla birlikte, Bitcoin yazılımı olgunlaştıkça ve kullanıcı arayüzleri geliştikçe, zamanla güvenilmezlik için çalışmak isteyen kullanıcıları desteklemede daha iyi hale gelmelidir. Ayrıca, kullanıcılar zaman içinde daha fazla bilgi edindikçe, güveni denklemden kademeli olarak çıkarabilmelidirler.


Bazı kullanıcılar tersine düşünmekte ve çalıştırdıkları yazılımın çoğu yönünü doğrulamaktadır. Sonuç olarak, yalnızca bilgisayar donanımlarına ve işletim sistemlerine güvenmeleri gerektiğinden, güven ihtiyacını en aza indirirler. Bunu yaparken, bulabilecekleri herhangi bir sorun hakkında uyarmak için kamuoyunda seslerini yükselterek donanımlarını kapsamlı bir şekilde doğrulamayan insanlara da yardımcı olurlar. Bunun iyi bir örneği, birisinin madencilerin aynı işlemde iki kez çıktı harcamasına izin veren bir hata keşfettiği [2018'de meydana gelen bir olay] (https://bitcoincore.org/en/2018/09/20/notice/):


> 18 Eylül'de Bitcoin core'nin 0.16.3 ve 0.17.0rc4 sürümlerinde düzeltmesi yayınlanan CVE-2018-17144, hem bir Hizmet Reddi bileşeni hem de kritik bir enflasyon açığı içermektedir. Başlangıçta Bitcoin core üzerinde çalışan birkaç geliştiricinin yanı sıra ABC ve Unlimited dahil olmak üzere diğer kripto para birimlerini destekleyen projelere 17 Eylül'de yalnızca bir Hizmet Reddi hatası olarak bildirildi, ancak sorunun aynı zamanda aynı kök nedene ve düzeltmeye sahip bir enflasyon açığı olduğunu hızlı bir şekilde belirledik.

Burada, anonim bir kişi, raportörün fark ettiğinden çok daha kötü sonuçlanan bir sorunu bildirmiştir. Bu durum, kodu doğrulayan kişilerin genellikle güvenlik açıklarını istismar etmek yerine bildirdikleri gerçeğini vurgulamaktadır. Bu, her şeyi kendileri doğrulayamayanlar için faydalıdır.


Bununla birlikte, kullanıcılar kendilerini güvende tutmaları için başkalarına güvenmemeli, bunun yerine her zaman ve her ne yapabilirlerse kendileri doğrulamalıdır; kişi bu şekilde mümkün olduğunca egemen kalır ve Bitcoin bu şekilde gelişir. Yazılım üzerinde ne kadar çok göz olursa, kötü niyetli kodların ve güvenlik açıklarının sızma olasılığı da o kadar azalır.


### Güvensizlik Hakkında Sonuç



Bitcoin protokolü Trustless'dur çünkü kullanıcıların üçüncü bir tarafa güvenmeden onunla etkileşime girmesine izin verir. Ancak pratikte çoğu insan Bitcoin'ı çalıştırdıkları yazılım ve donanımın tamamını doğrulayamaz. Yazılım veya donanımı doğrulayan yetenekli kişiler, kötü amaçlı kod veya hatalar bulduklarında daha az yetenekli diğer kişileri uyarabilirler.


Güvensizlik olmadan ademi merkeziyetçiliğe sahip olamayız çünkü güven kaçınılmaz olarak bazı merkezi otorite noktalarını içerir. Bir Trustless sisteminin üzerine güvenilir bir sistem inşa edebilirsiniz, ancak güvenilir bir sistemin üzerine bir Trustless sistemi inşa edemezsiniz.


## Gizlilik

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Bu bölüm özel finansal bilgilerinizi kendinize nasıl saklayacağınızla ilgilidir. Bitcoin bağlamında gizliliğin ne anlama geldiği, neden önemli olduğu ve Bitcoin'ün takma ad olduğunu söylemenin ne anlama geldiği açıklanmaktadır. Ayrıca, hem On-Chain hem de off-chain'de özel verilerin nasıl sızabileceği de incelenmektedir.


Ardından, bitcoinlerin değiştirilebilir, yani diğer bitcoinlerle değiştirilebilir olması gerektiğinden ve değiştirilebilirlik ile gizliliğin nasıl el ele gittiğinden bahsediyor. Son olarak, bu bölüm sizin ve başkalarının gizliliğini artırmak için alabileceğiniz bazı önlemleri tanıtmaktadır.


Bitcoin, kullanıcıların açık anahtarlar şeklinde birden fazla takma ada sahip olduğu bir takma ad sistemi olarak tanımlanabilir. İlk bakışta bu, kullanıcıları kimliklerinin tespit edilmesinden korumak için oldukça iyi bir yol gibi görünse de aslında özel finansal bilgileri istemeden sızdırmak gerçekten çok kolaydır.


### Gizlilik ne anlama geliyor?



Gizlilik farklı bağlamlarda farklı anlamlara gelebilir. Bitcoin'da, genellikle kullanıcıların gönüllü olarak yapmadıkları sürece finansal bilgilerini başkalarına açıklamak zorunda olmadıkları anlamına gelir.


Özel bilgilerinizi bilerek ya da bilmeyerek başkalarına sızdırmanın birçok yolu vardır. Veriler kamuya açık Blockchain'den ya da başka yollarla, örneğin kötü niyetli kişiler internet iletişiminizi ele geçirdiğinde sızabilir.


### Gizlilik neden önemlidir?


Bitcoin'de gizliliğin neden önemli olduğu açık gibi görünebilir, ancak bunun hemen düşünülemeyecek bazı yönleri vardır. [Bitcoin Talk forumunda] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), Gregory Maxwell bize mahremiyetin neden önemli olduğunu düşündüğü birçok iyi nedeni anlatıyor. Bunlar arasında serbest piyasa, güvenlik ve insan onuru yer almaktadır:


> Finansal gizlilik, serbest piyasanın etkin bir şekilde işlemesi için temel bir kriterdir: eğer bir işletme işletiyorsanız, tedarikçileriniz ve müşterileriniz sizin isteğiniz dışında tüm işlemlerinizi görebiliyorsa, fiyatları etkin bir şekilde belirleyemezsiniz.
> Rakipleriniz satışlarınızı takip ediyorsa etkili bir şekilde rekabet edemezsiniz.  Hesaplarınız üzerinde gizliliğiniz yoksa, özel ilişkilerinizde bireysel olarak bilgi avantajınız kaybolur: ev sahibinize yeterli gizlilik olmadan Bitcoin ile ödeme yaparsanız, ev sahibiniz ne zaman maaş zammı aldığınızı görür ve sizden daha fazla kira isteyebilir.
>

> Finansal gizlilik kişisel güvenlik için çok önemlidir: hırsızlar harcamalarınızı, gelirinizi ve varlıklarınızı görebilirlerse, bu bilgileri sizi hedef almak ve sömürmek için kullanabilirler. Gizlilik olmadan kötü niyetli kişiler kimliğinizi çalmak, büyük alışverişlerinizi kapınızın önünden kaçırmak veya işlem yaptığınız işletmeleri size karşı taklit etmek için daha fazla yeteneğe sahip olurlar... sizi tam olarak ne kadar dolandırmaya çalışacaklarını söyleyebilirler.
>

> Finansal mahremiyet insan onuru için elzemdir: hiç kimse kahve dükkanındaki ukala baristanın ya da meraklı komşularının gelirleri ya da harcama alışkanlıkları hakkında yorum yapmasını istemez. Kimse bebek delisi kayınvalidesinin neden doğum kontrol hapı (ya da seks oyuncakları) aldığını sormasını istemez. İşvereniniz hangi kiliseye bağış yaptığınızı bilmek zorunda değildir. Ancak kimsenin başkası üzerinde gereksiz bir otoriteye sahip olmadığı mükemmel bir şekilde aydınlanmış ayrımcılıktan arınmış bir dünyada saygınlığımızı koruyabilir ve mahremiyetimiz yoksa otosansür olmadan yasal işlemlerimizi özgürce yapabiliriz.

Maxwell ayrıca bu bölümün ilerleyen kısımlarında tartışılacak olan değiştirilebilirlik konusuna ve mahremiyet ile kolluk kuvvetlerinin nasıl çelişkili olmadığı konusuna da değinmektedir.


### Takma ad


Yukarıda Bitcoin'in takma isimli olduğundan ve takma isimlerin açık anahtarlar olduğundan bahsetmiştik. Medyada sık sık Bitcoin'in anonim olduğunu duyarsınız ki bu doğru değildir. Anonimlik ve takma ad arasında bir ayrım vardır.


Andrew Poelstra [bir Bitcoin Stack Exchange gönderisinde açıklıyor] (https://Bitcoin.stackexchange.com/a/29473/69518) işlemlerde anonimliğin nasıl görüneceğini:


> Parayı harcadığınızda nereden geldiği ya da nereye gittiğine dair hiçbir iz olmaması anlamında tam anonimlik, teorik olarak kriptografik sıfır bilgi ispatı tekniği kullanılarak mümkündür.

Aradaki fark, anonim bir para biçiminde takma adlar arasındaki ödemeleri izleyebilmeniz, anonim bir para biçiminde ise izleyememeniz gibi görünüyor. Bitcoin ödemeleri takma adlar arasında takip edilebildiği için anonim bir sistem değildir.


Ayrıca takma adların genel anahtarlar olduğunu söyledik, ancak aslında genel anahtarlardan türetilen adresler. Neden adresleri takma ad olarak kullanıyoruz da başka bir şey, örneğin "watchme1984" gibi açıklayıcı isimler kullanmıyoruz? Bu, Tim S. kullanıcısı tarafından Bitcoin Stack Exchange'te de [iyi açıklanmıştır] (https://Bitcoin.stackexchange.com/a/25175/69518):


> Bitcoin'nın fikrinin işe yaraması için, yalnızca belirli bir özel anahtarın sahibi tarafından harcanabilecek coinlere sahip olmanız gerekir. Bu, gönderdiğiniz her şeyin bir şekilde bir açık anahtara bağlı olması gerektiği anlamına gelir.
>

> Rastgele takma adlar (örneğin kullanıcı adları) kullanmak, açık/özel anahtar kriptosunu etkinleştirmek için takma adı bir şekilde bir açık anahtara bağlamanız gerektiği anlamına gelir. Bu, çevrimdışı olarak güvenli bir şekilde adres/takma ad oluşturma yeteneğini ortadan kaldırır (örneğin, birisinin "tdumidu" kullanıcı adına para gönderebilmesi için, Blockchain'de "tdumidu "nun "a1c..." açık anahtarına ait olduğunu duyurmanız ve başkalarının bunu duyurmak için bir nedeni olması için bir ücret eklemeniz gerekir), anonimliği azaltır (sizi takma adları yeniden kullanmaya teşvik ederek) ve Blockchain'nin boyutunu gereksiz yere şişirir. Ayrıca, düşündüğünüz kişiye gönderdiğiniz konusunda yanlış bir güvenlik hissi yaratacaktır (eğer ondan önce "Linus Torvalds" adını alırsam, o zaman benimdir ve insanlar bana değil Linux'un yaratıcısına ödeme yaptıklarını düşünerek para gönderebilirler).

Adresleri veya açık anahtarları kullanarak, önceden bir şekilde takma ad kaydetme ihtiyacını ortadan kaldırmak, takma adın yeniden kullanımı için teşvikleri azaltmak, Blockchain şişkinliğini önlemek ve diğer insanları taklit etmeyi zorlaştırmak gibi önemli hedeflere ulaşıyoruz.


### Blockchain gizlilik



Blockchain gizliliği, Blockchain üzerinde işlem yaparak ifşa ettiğiniz bilgileri ifade eder. Hem gönderdiğiniz hem de aldığınız tüm işlemler için geçerlidir.


Satoshi Nakamoto, [Bitcoin whitepaper]'ının 7. bölümünde (https://Bitcoin.org/Bitcoin.pdf) On-Chain gizliliği üzerine düşünmektedir:


> Ek bir güvenlik duvarı olarak, her bir işlemin ortak bir sahibine bağlanmasını önlemek için yeni bir anahtar çifti kullanılmalıdır. Girdilerinin aynı sahibine ait olduğunu ortaya çıkaran çok girdili işlemlerde bir miktar bağlantı kaçınılmazdır. Risk, bir anahtarın sahibinin ortaya çıkması halinde, bağlantının aynı sahibine ait diğer işlemleri de ortaya çıkarmasıdır.

Bu makale, Blockchain gizliliğinin ana sorunlarını, yani Address yeniden kullanımı ve Address kümelemesini özetlemektedir. İlki kendi kendini açıklamaktadır, ikincisi ise bir dizi farklı adresin aynı kullanıcıya ait olduğuna belirli bir kesinlik düzeyinde karar verme yeteneğini ifade etmektedir.


![](assets/address-reuse-clustering.webp)


Blockchain'daki tipik gizlilik sızıntıları


Chris Belcher, Bitcoin Blockchain'de meydana gelebilecek farklı gizlilik sızıntıları hakkında [çok ayrıntılı olarak yazdı] (https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy). En azından "Blockchain gizlilik saldırıları" başlığı altındaki ilk birkaç alt bölümü okumanızı tavsiye ederiz


Buradan çıkarılacak sonuç, Bitcoin'daki gizliliğin mükemmel olmadığıdır. Özel olarak işlem yapmak önemli miktarda çalışma gerektiriyor. Çoğu insan gizlilik için bu kadar ileri gitmeye hazır değil. Gizlilik ve kullanılabilirlik arasında net bir denge var gibi görünüyor.


Gizliliğin bir diğer önemli yönü de kendi gizliliğinizi korumak için aldığınız önlemlerin diğer kullanıcıları da etkilemesidir. Eğer kendi gizliliğiniz konusunda özensiz davranırsanız, diğer insanlar da daha az gizlilik yaşayabilir. Gregory Maxwell bunu [yukarıda linkini verdiğimiz] aynı Bitcoin Talk tartışmasında çok açık bir şekilde açıklıyor (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252) ve bir örnekle sonlandırıyor:


> Bu aslında pratikte de işe yarıyor... IRC'de iyi bir beyaz şapkalı hacker beyin cüzdanı kırma ile oynuyordu ve içinde ~250 BTC olan bir cümleye ulaştı.  Sahibini yalnızca Address'den tespit edebildik, çünkü adresleri yeniden kullanan bir Bitcoin hizmeti tarafından ödeme yapılmıştı ve kullanıcıların iletişim bilgilerini vermeleri için onlarla konuşmayı başardı. Aslında kullanıcıyı telefonla aradı, şok oldular ve kafaları karıştı - ama Coin'lerini kaybetmedikleri için minnettarlardı.  Mutlu bir son. (Bu bunun tek örneği değil... ama en eğlenceli örneklerinden biri).

Bu olayda, hayırsever hacker sayesinde her şey yolunda gitti, ancak bir dahaki sefere buna güvenmeyin.


### Blockchain dışı gizlilik


Blockchain gizlilik sızıntılarının kötü şöhretli bir kaynağı olduğunu kanıtlasa da, Blockchain'i kullanmayan, bazıları diğerlerinden daha sinsi olan pek çok başka sızıntı vardır. Bunlar tuş kaydedicilerden ağ trafiği analizine kadar uzanmaktadır. Bu yöntemlerden bazılarını okumak için lütfen tekrar [Chris Belcher'ın makalesine] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), özellikle de "Gizliliğe yönelik Blockchain dışı saldırılar" bölümüne bakın.


Belcher, çok sayıda saldırı arasında, örneğin İSS'niz gibi birinin internet bağlantınızı gözetleme olasılığından bahsediyor:


> Eğer düşman sizin düğümünüzden daha önce girilmemiş bir işlem ya da blok çıktığını görürse, işlemin sizin tarafınızdan yapıldığını ya da bloğun sizin tarafınızdan kazıldığını neredeyse kesin olarak bilebilir. İnternet bağlantıları söz konusu olduğundan, düşman IP Address ile keşfedilen Bitcoin bilgileri arasında bağlantı kurabilecektir.

Bununla birlikte, en belirgin gizlilik sızıntıları arasında borsalar yer almaktadır. Genellikle KYC (Müşterini Tanı) ve AML (Kara Para Aklamayı Önleme) olarak adlandırılan ve faaliyet gösterdikleri ülkelerde geçerli olan yasalar nedeniyle, borsalar ve ilgili şirketler genellikle kullanıcıları hakkında kişisel veriler toplamak ve hangi kullanıcıların hangi bitcoinlere sahip olduğuna dair büyük veritabanları oluşturmak zorundadır. Bu veri tabanları, her zaman yeni kurbanlar arayan kötü niyetli hükümetler ve suçlular için harika birer bal küpüdür. Bu tür veriler için gerçek pazarlar vardır, burada bilgisayar korsanları

en yüksek teklifi verene veri satmak.


Daha da kötüsü, bu veri tabanlarını yöneten şirketler genellikle finansal verileri koruma konusunda çok az deneyime sahiptir, aslında birçoğu genç start-up'lardır ve halihazırda birkaç sızıntının meydana geldiğini biliyoruz. Birkaç örnek vermek gerekirse

[Hindistan merkezli MobiQwik](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) ve [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Yine, verileri bu geniş saldırı yelpazesine karşı korumak Hard'dür ve muhtemelen bunu tam olarak yapamayacaksınız. Sizin için en uygun olan kolaylık ve gizlilik arasındaki dengeyi seçmeniz gerekecektir.


### Mantarlaşabilirlik


Para birimleri bağlamında değiştirilebilirlik, bir Coin'in aynı para biriminden başka herhangi bir Coin ile değiştirilebilir olduğu anlamına gelir. Bu komik

kelimesine bölümün başlarında kısaca değinilmişti.


Burada ele alınan makalede Gregory Maxwell [şunları belirtmiştir] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Finansal gizlilik, Bitcoin'de değiştirilebilirlik için temel bir unsurdur: bir Coin'ü diğerinden anlamlı bir şekilde ayırt edebiliyorsanız, değiştirilebilirlikleri zayıftır. Eğer değiştirilebilirliğimiz pratikte çok zayıfsa, o zaman merkeziyetsiz olamayız: eğer önemli biri çalıntı coinlerin bir listesini ilan ederse ve bu coinlerden türetilen coinleri kabul etmeyeceğini açıklarsa, kabul ettiğiniz coinleri bu listeye göre dikkatlice kontrol etmeli ve başarısız olanları iade etmelisiniz.  Herkes çeşitli otoriteler tarafından yayınlanan kara listeleri kontrol etmek zorunda kalır çünkü böyle bir dünyada hepimiz kötü coin'lere mahkum olmak istemeyiz. Bu durum sürtünme ve işlem maliyetlerini artırır ve Bitcoin'yi bir para olarak daha az değerli hale getirir.

Burada, değiştirilebilirlik eksikliğinden kaynaklanan tehlikelerden bahsediyor. Elinizde bir UTXO olduğunu varsayalım. Bu UTXO'in geçmişi normalde birkaç atlama geriye doğru izlenebilir ve çok sayıda önceki çıktıya yayılabilir. Bu çıktılardan herhangi biri yasadışı, istenmeyen veya şüpheli bir faaliyete karışmışsa, Coin'ünüzün bazı potansiyel alıcıları bunu reddedebilir. Eğer ödeme yaptığınız kişilerin coinlerinizi merkezi bir beyaz liste ya da kara liste hizmetine göre doğrulayacağını düşünüyorsanız, ne olur ne olmaz diye aldığınız coinleri de kontrol etmeye başlayabilirsiniz. Sonuç olarak, kötü fungibility daha da kötü fungibility'yi destekleyecektir.


Adam Back ve Matt Corallo 2016 yılında Milano'da düzenlenen Scaling Bitcoin'da [fungibility hakkında bir sunum yaptı] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/). Onlar da aynı doğrultuda düşünüyorlardı:


> Bitcoin'nin çalışması için değiştirilebilirliğe ihtiyacınız var. Eğer sikke alırsanız ve onları harcayamazsanız, o zaman onları harcayıp harcayamayacağınızdan şüphe etmeye başlarsınız. Aldığınız madeni paralar hakkında şüpheleriniz varsa, insanlar lekeleme hizmetlerine gidip "bu madeni paralar kutsanmış mı" diye kontrol edecek ve sonra insanlar ticaret yapmayı reddedeceklerdir. Bunun yaptığı şey, Bitcoin'yi merkezi olmayan izinsiz bir sistemden, kara liste sağlayıcılarından bir "IOU" aldığınız merkezi izinli bir sisteme dönüştürmektir.

Görünüşe göre gizlilik ve değiştirilebilirlik el ele gitmektedir. Gizlilik zayıfsa, örneğin istenmeyen kişilerin coinleri kara listeye alınabileceğinden, değiştirilebilirlik zayıflayacaktır. Aynı şekilde, değiştirilebilirlik zayıfsa gizlilik de zayıflayacaktır: bir kara liste varsa, hangi coinleri kabul edeceğinizi kara liste sağlayıcılarına sormanız gerekecek ve böylece muhtemelen IP Address, e-posta Address ve diğer hassas bilgilerinizi ifşa edeceksiniz. Bu iki özellik o kadar iç içe geçmiştir ki, bunlardan herhangi biri hakkında tek başına konuşmak Hard.


### Gizlilik önlemleri



İnsanların kendilerini gizlilik sızıntılarından korumalarına yardımcı olmak için çeşitli teknikler geliştirilmiştir. En belirgin olanları arasında, Nakamoto tarafından daha önce belirtildiği gibi, benzersiz

her işlem için adresler, ancak birkaç tane daha var. Size nasıl gizlilik ninjası olacağınızı öğretecek değiliz. Bununla birlikte, Bitcoin Q+A'da [gizliliği artıran teknolojilerin hızlı bir özeti] (https://bitcoiner.guide/privacytips/) bulunmaktadır ve bunlar bir şekilde Hard'in nasıl uygulanacağına göre sıralanmıştır. Okuduğunuzda, Bitcoin gizliliğinin genellikle Bitcoin dışındaki şeylerle ilgili olduğunu fark edeceksiniz. Örneğin, bitcoinleriniz hakkında övünmemelisiniz ve Tor ve VPN kullanmalısınız.


Yazıda ayrıca Bitcoin ile doğrudan ilgili bazı tedbirler de listelenmektedir:


- Full node: Kendi Full node'ünüzü kullanmazsanız, Wallet'ünüz hakkında internetteki sunuculara birçok bilgi sızdırırsınız. Bir Full node çalıştırmak harika bir ilk adımdır.
- Lightning Network: Bitcoin'nin üzerinde çeşitli protokoller mevcuttur, örneğin Lightning Network ve Blockstream'in Liquid'i Sidechain.
- CoinJoin: Birden fazla kişinin işlemlerini tek bir işlemde birleştirmesi için bir yol, zincir analizi yapmayı zorlaştırıyor.


Breaking Bitcoin konferansındaki [bir konuşmada] (https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) Chris Belcher, gizliliğin nasıl geliştirildiğine dair ilginç bir pratik örnek verdi:


> Onlar bir Bitcoin kumarhanesiydi. ABD'de çevrimiçi kumar oynamaya izin verilmemektedir. Doğrudan Bustabit'e para yatıran tüm Coinbase müşterilerinin hesapları kapatılacaktı çünkü Coinbase bunun için izleme yapıyordu. Bustabit birkaç şey yaptı. Değişimden kaçınma adı verilen bir şey yaptılar ve değişim çıktısı olmayan bir işlem yapıp yapamayacağınızı gördünüz. Bu, Miner ücretlerinden tasarruf sağlar ve ayrıca analizi engeller.
>

> Ayrıca, yoğun olarak kullandıkları yeniden kullanılan para yatırma adreslerini joinmarket'e aktardılar. Bu noktada, coinbase.com müşterileri hiçbir zaman yasaklanmadı. Görünüşe göre Coinbase'in gözetim hizmeti bundan sonra analiz yapamadı, bu yüzden bu algoritmaları kırmak mümkün.

Bu örnekten, diğerlerinin yanı sıra, Bitcoin vikisindeki [Gizlilik sayfasında] (https://en.Bitcoin.it/Privacy) da bahsetmiştir.


Lightning Network'te olduğu gibi Bitcoin'in üzerine sistemler inşa ederek daha iyi gizlilik elde edilebileceğine dikkat edin:


![image](assets/privacy.webp)


Bitcoin'nın üstündeki katmanlar gizlilik sağlayabilir


Son raporda güven ihtiyacının sadece üstteki katmanlarla artabileceğini belirtmiştik, ancak üstteki katmanlarda keyfi olarak iyileştirilebilen veya daha kötü hale getirilebilen gizlilik için durum böyle görünmüyor. Bunun nedeni nedir? Gelecekteki Ölçeklendirme bölümündeki Katmanlı Ölçeklendirme paragrafında açıklandığı gibi, Bitcoin'in üzerindeki herhangi bir Layer, ara sıra On-Chain işlemlerini kullanmalıdır, aksi takdirde "Bitcoin'in üzerinde" olmazdı. Gizliliği artıran katmanlar genellikle açığa çıkan bilgi miktarını en aza indirmek için temel Layer'u mümkün olduğunca az kullanmaya çalışır.


Yukarıdakiler gizliliğinizi artırmanın biraz teknik yollarıdır. Ancak başka yollar da vardır. Bu bölümün başında Bitcoin'un takma isimli bir sistem olduğunu söylemiştik. Bu, Bitcoin'daki kullanıcıların gerçek adları veya diğer kişisel verileriyle değil, açık anahtarlarıyla bilindiği anlamına gelir. Açık anahtar, bir kullanıcının takma adıdır ve bir kullanıcının birden fazla takma adı olabilir. İdeal bir dünyada, şahsi kimliğiniz Bitcoin takma adlarınızdan ayrılır. Ne yazık ki, bu bölümde açıklanan gizlilik sorunları nedeniyle, bu ayrıştırma genellikle zaman içinde azalır.


Kişisel verilerinizin açığa çıkma riskini azaltmak için ilk etapta bu verileri vermemek ya da sızıntı yapabilecek büyük veritabanları oluşturan merkezi hizmetlere vermemek gerekir. Bitcoin Q+A [tarafından yazılan bir makale KYC] (https://bitcoiner.guide/nokyconly/) ve bundan kaynaklanan tehlikeleri açıklamaktadır. Ayrıca durumunuzu iyileştirmek için atabileceğiniz bazı adımları da öneriyor:


> Neyse ki KYC kaynakları olmadan Bitcoin satın almak için bazı seçenekler var. Bunların tümü, merkezi bir üçüncü tarafla değil, doğrudan başka bir bireyle işlem yaptığınız P2P (eşler arası) borsalardır. Ne yazık ki bazıları Bitcoin'nin yanı sıra diğer coinleri de satmaktadır, bu nedenle dikkatli olmanızı tavsiye ederiz.

Makale, KYC/AML gerektiren borsaları kullanmaktan kaçınmanızı ve bunun yerine özel olarak işlem yapmanızı veya [bisq] (https://bisq.network/) gibi merkezi olmayan borsaları kullanmanızı önermektedir.


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Karşı önlemler hakkında daha derinlemesine okuma için, daha önce bahsedilen [gizlilikle ilgili wiki makalesine] (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), "Gizliliği geliştirme yöntemleri (Blockchain dışı)" bölümünden başlayarak bakın.


### Gizlilik Hakkında Sonuç



Gizlilik çok önemlidir ancak Hard'ya ulaşmak zordur. Mahremiyet için sihirli bir değnek yoktur.


Bitcoin'de iyi bir gizlilik elde etmek için, bazıları maliyetli ve zaman alıcı olan aktif önlemler almanız gerekir.


## Sonlu Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Bu bölümde Bitcoin Supply sınırı olan 21 milyon BTC'yi ya da gerçekte ne kadar olduğunu inceleyeceğiz Bu limitin nasıl uygulandığından ve buna uyulduğunu doğrulamak için neler yapılabileceğinden bahsediyoruz. Dahası, kristal küreye bir göz atıyor ve Block reward sübvansiyon temelli olmaktan ücret temelli olmaya geçtiğinde devreye girecek dinamikleri tartışıyoruz.


İyi bilinen 21 milyon BTC'lik sonlu Supply, Bitcoin'nin temel bir özelliği olarak kabul edilmektedir. Ama bu gerçekten de kesin midir?


Mevcut mutabakat kurallarının Bitcoin'in Supply'sı hakkında ne söylediğine ve bunun ne kadarının gerçekten kullanılabilir olacağına bakarak başlayalım. Pieter Wuille bu konuda [Stack Exchange üzerine] bir yazı yazdı (https://Bitcoin.stackexchange.com/a/38998/69518) ve tüm madeni paralar çıkarıldıktan sonra kaç bitcoin olacağını saydı:


> Tüm bu rakamları toplarsanız 20999999.9769 BTC elde edersiniz.

Ancak coinbase işlemleriyle ilgili ilk sorunlar, istemeden izin verilenden daha az talepte bulunan madenciler ve özel anahtarların kaybı gibi bir dizi nedenden dolayı bu üst sınıra asla ulaşılamayacak. Wuille şu sonuca varıyor:


> Bu bize 20999817.31308491 BTC bırakıyor (528333 bloğuna kadar olan her şeyi hesaba katarak)

Ancak, çeşitli cüzdanlar kaybolmuş veya çalınmış, işlemler yanlış Address'ye gönderilmiş, insanlar Bitcoin'e sahip olduklarını unutmuşlardır. Bunların toplamı milyonlarca olabilir. İnsanlar bilinen kayıpları saymaya çalıştılar [burada](https://bitcointalk.org/index.php?topic=7253.0).


Bu da bizi: ??? BTC.


Dolayısıyla Bitcoin Supply'nin en fazla 20999817.31308491 BTC olacağından emin olabiliriz. Kaybolan veya doğrulanamayan bir şekilde yanan madeni paralar bu sayıyı düşürecektir, ancak ne kadar düşüreceğini bilmiyoruz. İşin ilginç yanı, bunun gerçekten önemli olmaması ya da daha iyisi, Bitcoin sahipleri için olumlu bir şekilde önemli olmasıdır,

gW-251 Nakamoto tarafından [açıklandığı gibi] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647):


> Kayıp madeni paralar sadece diğerlerinin madeni paralarının değerini biraz daha artırır.  Bunu herkese yapılan bir bağış olarak düşünün.

Sonlu Supply küçülecek ve bu da en azından teoride fiyat deflasyonuna neden olacaktır.


Dolaşımdaki madeni paraların tam sayısından daha önemlisi, Supply limitinin herhangi bir merkezi otorite olmaksızın uygulanma şeklidir. Alias chytrik bunu [Stack Exchange] (https://Bitcoin.stackexchange.com/a/106830/69518) adresinde çok iyi ifade ediyor:


> Yani cevap şu ki, Supply'yı artırmadığı için birine güvenmek zorunda değilsiniz. Sadece artırmadıklarını doğrulayacak bazı kodlar çalıştırmanız gerekir.

Bazı tam düğümler karanlık tarafa geçip daha yüksek değerli coinbase işlemleri içeren blokları kabul etmeye karar verse bile, geri kalan tüm tam düğümler onları görmezden gelecek ve her zamanki gibi iş yapmaya devam edecektir. Bazı tam düğümler kasıtlı ya da kasıtsız olarak kötü yazılımlar çalıştırabilir, ancak kolektif Blockchain'yi sağlam bir şekilde güvence altına alacaktır. Sonuç olarak, kimseye güvenmek zorunda kalmadan sisteme güvenmeyi seçebilirsiniz.


### Blok sübvansiyon ve işlem ücretleri



Bir Block reward, blok sübvansiyonu artı işlem ücretlerinden oluşur. Block reward'in Bitcoin'un güvenlik maliyetlerini karşılaması gerekir. Blok sübvansiyonu, işlem ücretleri, Bitcoin fiyatı, Mempool boyutu, Hash gücü, ademi merkeziyetçilik derecesi vb. açısından günümüz koşullarında, her oyuncunun kurallara göre oynaması için teşviklerin güvenli bir parasal sistemi korumak için yeterince yüksek olduğunu kesin olarak söyleyebiliriz.


Blok sübvansiyon sıfıra yaklaştığında ne olur? İşleri basit tutmak için, bunun gerçekten sıfıra eşit olduğunu varsayalım. Bu noktada, sistemin güvenlik maliyeti yalnızca işlem ücretleriyle karşılanır. Bu gerçekleştiğinde geleceğin bizim için ne getireceğini bilemeyiz. Belirsizlik faktörleri çok sayıda ve spekülasyonlara bırakılmış durumdayız. Örneğin, Paul Sztorc'un konuya katkısı [Truthcoin blogunda] (https://www.truthcoin.info/blog/security-budget/) çoğunlukla spekülasyonlardan ibarettir, ancak en azından bir sağlam noktası vardır (Sztorc tarafından atıfta bulunulan M2'nin bir fiat para Supply ölçümü olduğunu lütfen unutmayın):


> İkisi aynı "güvenlik bütçesi" içinde karıştırılsa da, blok sübvansiyon ve vergi harçları tamamen ve bütünüyle farklıdır. Birbirlerinden, "VISA'nın 2017'deki toplam kârı" ile "2017'deki toplam M2 artışı" kadar farklıdırlar.

Bugün güvenliğin bedelini (parasal enflasyon yoluyla) elinde tutanlar ödemektedir. Yarın ise aşağıda gösterildiği gibi bu yükü bir şekilde omuzlama sırası harcama yapanlara gelecektir.


![image](assets/finitesupply.webp)


Zaman geçtikçe, güvenlik maliyetlerinin yükü ellerinde tutanlardan harcayanlara geçecektir


İşlem ücretleri Mining için ana motivasyon olduğunda, teşvikler değişir. En önemlisi, bir Miner'nın Mempool'ü yeterli işlem ücreti içermiyorsa, bu Miner için Bitcoin'ün geçmişini genişletmek yerine yeniden yazmak daha karlı hale gelebilir. Bitcoin Optech'te David Harding tarafından yazılmış *fee sniping* adlı özel bir [bu davranışla ilgili bölüm] (https://bitcoinops.org/en/topics/fee-sniping/) bulunmaktadır:


> Bitcoin'nin sübvansiyonu azalmaya devam ettikçe ve işlem ücretleri Bitcoin'nin blok ödüllerini domine etmeye başladıkça, ücret sniping'i ortaya çıkabilecek bir sorundur. Eğer önemli olan tek şey işlem ücretleri ise, Hash oranının %x'ine sahip bir Miner'in bir sonraki blokta %x'lik bir Mining şansı vardır, bu nedenle dürüstçe Mining'un onlar için beklenen değeri, Mempool'lerindeki [en uygun işlem kümesinin] (https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) %x'idir.
>

> Alternatif olarak, bir Miner zinciri genişletmek için dürüst olmayan bir şekilde önceki bloğu ve tamamen yeni bir bloğu yeniden madencilikle elde etmeye çalışabilir. Bu davranışa fee sniping adı verilir ve dürüst olmayan Miner'ün diğer tüm Miner'ler dürüstse bunu başarma şansı `(x/(1-x))^2`dir. Ücret kesmenin dürüst Mining'e kıyasla genel olarak daha düşük bir başarı olasılığı olsa da, önceki bloktaki işlemlerin şu anda Mempool'deki işlemlerden önemli ölçüde daha yüksek ücretler ödemesi durumunda dürüst olmayan Mining'ü denemek daha karlı bir seçim olabilir - büyük miktarda küçük bir şans, küçük miktarda büyük bir şanstan daha değerli olabilir.

Geleceğe yönelik umutlarımızın üzerine ıslak bir battaniye atan gerçek şu ki, madenciler ücret avcılığı yapmaya başlarsa, bu diğerlerini de aynı şeyi yapmaya teşvik edecek ve daha az dürüst madenci bırakacaktır. Bu da Bitcoin'nın genel güvenliğini ciddi şekilde zedeleyebilir. Harding, işlemin Blockchain'in neresinde görünebileceğini kısıtlamak için işlem süresi kilitlerine güvenmek gibi alınabilecek birkaç karşı önlemi listelemeye devam ediyor.


Dolayısıyla, sonlu Supply üzerindeki fikir birliği devam ettiği sürece, blok sübvansiyonu - çok uzun vadeli bir enflasyon hatasını düzelten [BIP42] (https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki) sayesinde - 2140 yılı civarında sıfırlanacaktır. Bundan sonra işlem ücretleri ağı güvence altına almak için yeterli olacak mı?


Bunu söylemek mümkün değil ama birkaç şey biliyoruz:


- Bitcoin perspektifinden bakıldığında bir yüzyıl *uzun* bir süredir. Eğer hala buralardaysa, muhtemelen muazzam bir evrim geçirmiş olacaktır.
- Eğer ezici bir ekonomik çoğunluk kuralları değiştirmeyi ve örneğin sürekli yıllık %0.1 veya %1 parasal enflasyon getirmeyi gerekli görürse, Bitcoin'in Supply'i artık sonlu olmayacaktır.
- Sıfır blok sübvansiyonu ve boş ya da neredeyse boş bir Mempool ile, ücretler nedeniyle işler sallantılı hale gelebilir.


Ücretli Block reward'e geçiş çok uzak bir gelecekte olduğu için, hemen sonuca varmamak ve potansiyel sorunları elimizden geldiğince çözmeye çalışmak akıllıca olabilir. Örneğin Peter Todd, Bitcoin'ün güvenlik bütçesinin gelecekte yeterli olmayacağına dair gerçek bir risk olduğunu düşünüyor ve sonuç olarak Bitcoin'te küçük bir sürekli enflasyonu savunuyor. Bununla birlikte, [What Bitcoin Did podcast'inde söylediği gibi] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin) şu anda böyle bir konuyu tartışmanın iyi bir fikir olmadığını da düşünüyor:


> Ama bu 10, 20 yıl sonrası için bir risk. Bu çok uzun bir süre. Ve o zamana kadar risklerin ne olduğunu kim bilebilir ki?

Belki de Bitcoin'i organik bir şey olarak düşünebiliriz. Küçük, yavaş büyüyen bir meşe bitkisi hayal edin. Hayatınızda hiç tamamen büyümüş bir ağaç görmediğinizi de düşünün. O zaman bu bitkinin nasıl gelişip büyümesine izin verilmesi gerektiğine dair tüm kuralları önceden belirlemek yerine kontrol sorunlarınızı dizginlemeniz akıllıca olmaz mı?


### Sonlu Supply hakkında sonuç



Bitcoin Supply'in 21 milyonu geçip geçmeyeceğini bugünden söyleyemeyiz ve bu muhtemelen o kadar da kötü değil. Güvenlik bütçesinin yeterince yüksek kalmasını sağlamak çok önemli ama acil değil. Bu tartışmayı 10-50 yıl sonra, daha fazla şey öğrendiğimizde yapalım. Eğer hala geçerliyse.


# Bitcoin Gouvernance

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Yükseltme

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Bitcoin'ı güvenli bir şekilde yükseltmek son derece zor olabilir. Bazı değişikliklerin hayata geçirilmesi birkaç yıl alabilir. Bu bölümde, Bitcoin'ın yükseltilmesiyle ilgili ortak kelime dağarcığı hakkında bilgi ediniyor ve protokolündeki bazı tarihi yükseltme örneklerini ve bunlardan elde ettiğimiz içgörüleri keşfediyoruz. Son olarak, zincir bölünmeleri ve bunlarla ilgili riskler ve maliyetler hakkında konuşuyoruz.


Bu bölüme uyum sağlamak için [David Harding'in uyum ve uyumsuzluk hakkındaki yazısını] (https://bitcointalk.org/dec/p1.html) okumalısınız:


> Bitcoin uzmanları sık sık anlamı soyut ve Hard tam olarak belirlenemeyen konsensüsten bahsederler. Ancak konsensüs kelimesi Latince concentus kelimesinden evrilmiştir, "birlikte şarkı söyleme uyumu", bu nedenle Bitcoin konsensüsünden değil, Bitcoin uyumundan bahsedelim.
>

> Bitcoin'ün çalışmasını sağlayan şey uyumdur. Binlerce tam düğümün her biri, aldıkları işlemlerin geçerli olduğunu doğrulamak için bağımsız olarak çalışır ve hiçbir düğüm operatörünün başkasına güvenmesine gerek kalmadan Bitcoin Ledger'ün durumu hakkında uyumlu bir anlaşma üretir. Bu, her bir üyenin aynı anda aynı şarkıyı söyleyerek herhangi birinin tek başına üretebileceğinden çok daha güzel bir şey ürettiği bir koroya benzer.
>

> Bitcoin uyumunun sonucu, bitcoinlerin sadece küçük hırsızlardan (anahtarlarınızı güvende tutmanız koşuluyla) değil, aynı zamanda sonsuz enflasyondan, kitlesel veya hedefli müsadereden veya sadece eski finansal sistem olan bürokratik bataklıktan da güvende olduğu bir sistemdir.

Bu bölümde Bitcoin'nın anlaşmazlığa yol açmadan nasıl geliştirilebileceği tartışılmaktadır. Uyum içinde kalmak, yani fikir birliğini sürdürmek, gerçekten de Bitcoin'nın geliştirilmesindeki en büyük zorluklardan biridir. Yükseltme mekanizmalarında birçok nüans vardır ve bunlar en iyi önceki yükseltmelerin gerçek vakalarını inceleyerek anlaşılabilir. Bu nedenle, bu bölüm tarihi örneklere odaklanmakta ve bazı faydalı kelimelerle ortamı hazırlayarak başlamaktadır.


### Kelime dağarcığı



Wikipedia'ya göre [ileri uyumluluk] (https://en.wikipedia.org/wiki/Forward_compatibility), eski bir yazılımın anlamadığı kısımları göz ardı ederek daha yeni yazılımlar tarafından oluşturulan verileri işleyebilmesi durumunu ifade eder:


Daha önceki sürümlerle uyumlu bir ürün, anlamadığı yeni kısımları göz ardı ederek standardın sonraki sürümleri için tasarlanmış girdileri "incelikle" işleyebiliyorsa, bir standart ileriye dönük uyumluluğu destekler.


Tam tersi, [geriye dönük uyumluluk] (https://en.wikipedia.org/wiki/Backward_compatibility) eski bir yazılımdaki verilerin daha yeni yazılımlarda kullanılabilir olması anlamına gelir. Bir değişikliğin hem ileri hem de geri uyumlu olması durumunda tam uyumlu olduğu söylenir.


Bitcoin mutabakat kurallarında yapılan bir değişikliğin tam uyumlu olması halinde *Soft Fork* olduğu söylenir. Bu, bu bölümde daha sonra tartışacağımız bir dizi nedenden dolayı Bitcoin'u yükseltmenin en yaygın yoludur. Bitcoin mutabakat kurallarında yapılan bir değişiklik geriye doğru uyumlu ancak ileriye doğru uyumlu değilse buna *Hard Fork* denir.


Soft çatalları ve Hard çatallarına teknik bir genel bakış için lütfen [Grokking Bitcoin'ün 11. bölümünü] (https://rosenbaum.se/book/grokking-Bitcoin-11.html) okuyun. Bu terimleri açıklar ve ayrıca yükseltme mekanizmalarına dalar. Kesinlikle gerekli olmasa da, okumaya devam etmeden önce bu konuda bilgi sahibi olmanız önerilir.


### Tarihi iyileştirmeler



Bitcoin, Genesis bloğunun oluşturulduğu zamanki haliyle bugün aynı değildir. Yıllar boyunca çeşitli yükseltmeler yapılmıştır. 2018'de Eric Lombrozo [Breaking Bitcoin konferansında konuştu] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) Bitcoin'ün farklı yükseltme mekanizmaları hakkında konuştu ve bunların zaman içinde ne kadar geliştiğine dikkat çekti. Hatta Satoshi Nakamoto'nun bir zamanlar Bitcoin'ü bir Hard Fork aracılığıyla nasıl yükselttiğini açıkladı:


> Aslında Bitcoin'de Satoshi'in asla bu şekilde yapmayacağımız bir Hard-Fork vardı - bunu yapmak için oldukça kötü bir yol. Buradaki git commit açıklamasına bakarsanız [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], geri döndürülmüş makefile.unix wx-config sürüm 0.3.6 hakkında bir şeyler söylüyor. Doğru. Tüm söylediği bu. Kırıcı bir değişikliğe sahip olduğuna dair hiçbir gösterge yok. Temelde onu orada saklıyordu. Ayrıca [bitcointalk'a gönderdi] (https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) ve lütfen en kısa sürede 0.3.6'ya yükseltin dedi. Sahte işlemlerin kabul edilmiş olarak gösterilmesinin mümkün olduğu bir uygulama hatasını düzelttik. 0.3.6'ya yükseltene kadar Bitcoin ödemelerini kabul etmeyin. Hemen yükseltme yapamıyorsanız, yapana kadar Bitcoin düğümünüzü kapatmanız en iyisi olacaktır. Ve bunun da ötesinde, neden bunu yapmaya karar verdiğini bilmiyorum, aynı koda bazı optimizasyonlar eklemeye karar verdi. Bir hatayı düzeltin ve bazı optimizasyonlar ekleyin.

Kasıtlı olsun ya da olmasın, bu Hard Fork'in gelecekteki Soft çatalları, yani OP_NOP1-OP_NOP10 komut dosyası operatörleri (opcode) için fırsatlar yarattığına dikkat çekiyor. Bu kod değişikliğini cve-2010-5141'de daha ayrıntılı olarak inceleyeceğiz. Bu opcode'lar şimdiye kadar iki Soft fork'u için kullanıldı:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo ayrıca 2017 yılına kadar yükseltme mekanizmalarının yıllar içinde nasıl geliştiğine dair genel bir bakış sunuyor. O zamandan bu yana, yalnızca bir büyük yükseltme olan Taproot uygulanmıştır. Etkinleştirilmesine yol açan uzun ve biraz kaotik süreç, Bitcoin'teki yükseltme mekanizmaları hakkında daha fazla bilgi edinmemize yardımcı oldu.


#### SegWit yükseltmesi



SegWit'dan önceki tüm yükseltmeler az ya da çok sancısız olmuş olsa da bu yükseltme farklıydı. Ekim 2016'da SegWit aktivasyon kodu yayınlandığında, Bitcoin kullanıcıları arasında bu kod için büyük bir destek var gibi görünüyordu, ancak bazı nedenlerden dolayı madenciler bu yükseltme için destek sinyali vermedi ve bu da aktivasyonu görünürde bir çözüm olmadan durdurdu.


Aaron van Wirdum, Bitcoin Magazine makalesinde [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality) bu dolambaçlı yolu anlatıyor. SegWit'nin ne olduğunu ve blok boyutu tartışmasına nasıl girdiğini açıklayarak başlıyor. Van Wirdum daha sonra nihai aktivasyonuna yol açan olayların ana hatlarını çiziyor. Bu sürecin merkezinde, Shaolinfry adlı kullanıcı tarafından önerilen *kullanıcı tarafından etkinleştirilen Soft Fork* ya da kısaca UASF adı verilen bir yükseltme mekanizması vardı:


> Shaolinfry bir alternatif önerdi: kullanıcı tarafından etkinleştirilen Soft Fork (UASF). Hash güç aktivasyonu yerine, kullanıcı tarafından aktive edilen bir Soft Fork, düğümlerin gelecekte önceden belirlenmiş bir zamanda uygulamaya başladığı bir "'bayrak günü aktivasyonuna" sahip olacaktır Böyle bir UASF ekonomik bir çoğunluk tarafından uygulandığı sürece, bu madencilerin çoğunluğunu Soft Fork'ü takip etmeye (veya etkinleştirmeye) zorlamalıdır.

Diğer şeylerin yanı sıra, Shaolinfry'nin Bitcoin-dev posta listesine gönderdiği e-postaya atıfta bulunuyor. Bu vesileyle Shaolinfry [Miner'nın Soft çatallarını etkinleştirmesine karşı çıktı] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html) ve bunlarla ilgili bir dizi sorunu listeledi:


> İlk olarak, Hash gücünün aktivasyondan sonra doğrulanacağına güvenmeyi gerektirir.  BIP66 Soft Fork, Hashrate'un %95'inin hazır olma sinyali verdiği ancak gerçekte yaklaşık yarısının yükseltilmiş kuralları doğrulamadığı ve yanlışlıkla geçersiz bir blok üzerine madencilik yaptığı bir durumdu.
>

> İkinci olarak, Miner sinyali, Hashrate'in küçük bir yüzdesinin herkes için yükseltmenin düğüm aktivasyonunu veto etmesine izin veren doğal bir vetoya sahiptir. Bugüne kadar, Soft çatalları, geçerli bloklar oluşturan nispeten az sayıda Mining havuzunun bulunduğu nispeten merkezi Mining ortamından yararlanmıştır; daha fazla Hashrate ademi merkeziyetçiliğine doğru ilerledikçe, çoğu yükseltmeyi veto edecek olan "yükseltme ataletinden" giderek daha fazla zarar görmemiz muhtemeldir.

Shaolinfry ayrıca Miner sinyalinin yaygın bir şekilde yanlış yorumlandığına dikkat çekti: insanlar genellikle bunun, yükseltmelerin koordine edilmesine yardımcı olan bir eylemden ziyade madencilerin protokol yükseltmelerine karar verebilecekleri bir araç olduğunu düşündüler. Bu yanlış anlama nedeniyle madenciler, sanki teklife ağırlık kazandırıyormuş gibi, belirli bir Soft Fork hakkındaki görüşlerini kamuoyuna açıklamak zorunda hissetmiş olabilirler.


UASF önerisi özetle, düğümlerin belirli yeni kuralları uygulamaya başladığı bir "bayrak günü "dür. Bu şekilde, madencilerin yükseltmeyi koordine etmek için toplu bir çaba göstermesi gerekmez, ancak yeterli sayıda blok destek sinyali verirse bayrak gününden daha önce etkinleştirmeyi tetikleyebilir:


> Benim önerim her iki dünyanın da en iyisine sahip olmak. Kullanıcı tarafından etkinleştirilen bir Soft Fork'nin etkinleştirilmeden önce nispeten uzun bir teslim süresine ihtiyacı olduğundan, daha hızlı bir Hash güç koordineli etkinleştirme veya bayrak gününe göre etkinleştirme seçeneği sunmak için BIP9 ile birleştirebiliriz, hangisi daha erken olursa.
> Her iki durumda da BIP9'daki uyarı sistemlerinden yararlanabiliriz. Değişiklik nispeten basittir, BIP9 dağıtım zaman aşımı sona ermeden önce BIP9 durumunu LOCKED_IN'e geçirecek bir aktivasyon zamanı parametresi ekler.

Bu fikir çok ilgi çekti, ancak oybirliğine yakın bir desteğe ulaşamamış gibi görünüyordu, bu da potansiyel bir zincir bölünmesi endişesine neden oldu. Aaron van Wirdum'un makalesi, James Hilliard tarafından yazılan [BIP91] (https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki) sayesinde bu sorunun nasıl çözüldüğünü açıklıyor:


> Hilliard, her şeyi uyumlu hale getirecek biraz karmaşık ama akıllıca bir çözüm önerdi: Bitcoin core geliştirme ekibi tarafından önerilen Ayrılmış Tanık aktivasyonu, BIP148 UASF ve New York Anlaşması aktivasyon mekanizması. Onun BIP91'i Bitcoin'i en azından SegWit aktivasyonu boyunca bir bütün olarak tutabilir.

Bu BIP'nin dikkate alması gereken bazı daha karmaşık faktörler (örneğin "New York Anlaşması") söz konusuydu. Bu hikayedeki pek çok ilginç ayrıntıyı öğrenmek için Van Wirdum'un makalesinin tamamını okumanızı tavsiye ederiz.


#### SegWit sonrası tartışma


SegWit dağıtımından sonra, dağıtım mekanizmaları hakkında bir tartışma ortaya çıktı. Eric Lombrozo'nun [Breaking Bitcoin konferansındaki konuşmasında] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) ve Shaolinfry tarafından belirtildiği gibi, Miner'yi etkinleştiren bir Soft Fork ideal yükseltme mekanizması değildir:


> Bir noktada muhtemelen Bitcoin protokolüne daha fazla özellik eklemek isteyeceğiz. Bu kendimize sorduğumuz büyük bir felsefi soru. Bir sonraki için bir UASF yapacak mıyız? Hibrit bir yaklaşıma ne dersiniz? Tek başına aktive edilen Miner elendi. bip9'u tekrar kullanmayacağız.

Ocak 2020'de Matt Corallo, Bitcoin-dev posta listesine gelecekteki Soft Fork dağıtım mekanizmaları hakkında bir tartışma başlatan bir e-posta] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) gönderdi. Bir yükseltmede gerekli olduğunu düşündüğü beş hedefi listeledi. David Harding [bunları bir Bitcoin Optech bülteninde](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) şöyle özetliyor:


> Önerilen mutabakat kuralları değişikliklerine ciddi bir itiraz ile karşılaşılması durumunda iptal etme yeteneği. Güncellenmiş yazılımın yayınlanmasından sonra çoğu ekonomik düğümün bu kuralları uygulayacak şekilde yükseltilmesini sağlamak için yeterli zaman ayrılması . Ağ Hash oranının değişiklikten önce ve sonra ve herhangi bir geçiş sırasında aşağı yukarı aynı olacağı beklentisi . Yeni kurallara göre geçersiz olan ve yükseltilmemiş düğümlerde ve SPV istemcilerinde yanlış onaylara yol açabilecek blokların oluşturulmasının mümkün olduğunca önlenmesi. İptal mekanizmalarının, bilinen hiçbir sorunu olmayan ve yaygın olarak istenen bir yükseltmeyi engellemek için kederli kişiler veya partizanlar tarafından kötüye kullanılamayacağının güvence altına alınması

Corallo'nun önerdiği, Miner ile aktive edilmiş bir Soft Fork ve kullanıcı tarafından aktive edilmiş bir Soft Fork kombinasyonudur:


> Bu nedenle, biraz daha somut bir şey olarak, doğru emsal teşkil eden ve yukarıdaki hedefleri uygun bir şekilde dikkate alan bir aktivasyon yönteminin olacağını düşünüyorum:
>

> 1) bir yıllık zaman ufkuna sahip standart bir BIP 9 dağıtımı
95 Miner hazırlığı ile aktivasyon, +

> 2) bir yıl içinde herhangi bir aktivasyon gerçekleşmemesi durumunda, altı aylık bir
topluluğun analiz yapabileceği ve tartışabileceği sessizlik dönemi

aktivasyon olmamasının nedenleri ve +

> 3) mantıklı olması durumunda, orijinal dağıtım sürümünden beri desteklenen basit bir komut satırı/Bitcoin.conf parametresi, kullanıcıların bayrak günü aktivasyonu için 24 aylık bir zaman ufku olan bir BIP 8 dağıtımını seçmelerini sağlayacaktır (ayrıca bayrağı evrensel olarak etkinleştiren yeni bir Bitcoin core sürümü).
>

> Bu, daha fazla standart aktivasyon için çok uzun bir zaman ufku sağlarken, #5'teki hedeflerin karşılanmasını sağlar, bu durumlarda zaman ufkunun #3'ün hedeflerini karşılamak için önemli ölçüde uzatılması gerekse bile. Bitcoin'ı geliştirmek bir yarış değildir. Mecbur kalırsak, 42 ay beklemek, Bitcoin büyümeye devam ettikçe pişman olacağımız olumsuz bir emsal oluşturmamamızı sağlar.

#### Taproot yükseltmesi - Hızlı Yargılama



Taproot Ekim 2020'de konuşlandırılmaya hazır hale geldiğinde, yani uzlaşı kurallarıyla ilgili tüm teknik ayrıntılar uygulandığında ve topluluk içinde geniş bir onay aldığında, bunun gerçekten nasıl konuşlandırılacağına ilişkin tartışmalar ısınmaya başladı. Bu tartışmalar o noktaya kadar oldukça düşük düzeyde kalmıştı.


Aktivasyon mekanizmaları için pek çok öneri ortalıkta dolaşmaya başladı ve David Harding

[Bitcoin Wiki'de özetlenmiştir] (https://en.Bitcoin.it/wiki/Taproot_activation_proposals). Makalesinde, o zamanlar daha esnek hale getirmek için bazı yeni değişiklikler yapılmış olan BIP8'in bazı özelliklerini açıkladı.


> Bu belge yazılırken, [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) 2017'de öğrenilen dersler temel alınarak hazırlanmıştır. BIP 9+148'i takiben kayda değer bir değişiklik, zorunlu aktivasyonun artık geçen medyan zaman yerine blok yüksekliğine dayanmasıdır; ikinci kayda değer değişiklik ise, zorunlu aktivasyonun bir Soft Fork'ün aktivasyon parametreleri ilk dağıtım için ayarlandığında veya daha sonraki bir dağıtımda güncellendiğinde seçilen bir boolean parametresi olmasıdır.

Zorunlu aktivasyon olmadan BIP8, zaman aşımı ve gecikme ile [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) sürüm bitlerine çok benzer, tek önemli fark BIP9'un medyan zaman geçmişini kullanmasına kıyasla BIP8'in blok yüksekliklerini kullanmasıdır. Bu ayar denemenin başarısız olmasına izin verir (ancak daha sonra yeniden denenebilir).


Zorunlu aktivasyonlu BIP8, kurallarına uygun olarak üretilen tüm blokların, zorunlu olmayan aktivasyonlu aynı Soft Fork'nin daha önceki bir dağıtımında aktivasyonu tetikleyecek şekilde Soft Fork için hazır olma sinyali vermesi gereken zorunlu bir sinyal dönemi ile sonuçlanır. Başka bir deyişle, x düğümü sürümü zorunlu aktivasyon olmadan yayınlanırsa ve daha sonra madencileri aynı süre içinde hazır olma sinyali vermeye başlamaya zorlayan y sürümü yayınlanırsa, her iki sürüm de yeni mutabakat kurallarını aynı anda uygulamaya başlayacaktır.


Revize edilmiş BIP8 önerisinin bu esnekliği, diğer bazı fikirlerin BIP8 kullanılarak nasıl görünecekleri açısından ifade edilmesini mümkün kılmaktadır. Bu, birçok farklı öneriyi kategorize etmek için kullanılacak ortak bir faktör sağlar.


Bu noktadan sonra tartışmalar, özellikle `lockinontimeout`un `true` (Harding tarafından "zorunlu aktivasyonlu BIP8" olarak adlandırılan, kullanıcı tarafından aktive edilmiş bir Soft Fork'de olduğu gibi) veya `false` (Harding tarafından "zorunlu aktivasyonsuz BIP8" olarak adlandırılan, Miner tarafından aktive edilmiş bir Soft Fork'de olduğu gibi) olması gerektiği konusunda çok hararetli hale geldi.


Listelenen teklifler arasında bir tanesi "Bakalım ne olacak" başlığını taşıyordu. Nedense bu öneri yedi ay sonrasına kadar pek ilgi görmedi.


Bu yedi ay boyunca tartışma devam etti ve hangi dağıtım mekanizmasının kullanılacağı konusunda geniş bir fikir birliğine varmanın bir yolu yok gibi görünüyordu. Temel olarak iki kamp vardı: biri `lockinontimeout=true` (UASF kalabalığı) ve diğeri `lockinontimeout=false` ("dene ve başarısız olursa yeniden düşün" kalabalığı) tercih ediyordu. Bu seçeneklerden herhangi biri için ezici bir destek olmadığından, tartışma görünüşte ileriye dönük bir yol olmadan daireler çizdi. Bu tartışmaların bazıları IRC'de ##Taproot-activation adlı bir kanalda yapıldı, ancak [5 Mart 2021'de] (https://gnusha.org/Taproot-activation/2021-03-05.log) bir şeyler değişti:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


"Bakalım ne olacak" yaklaşımı nihayet insanların zihninde yer etmiş görünüyordu. Bu süreç, kısa sinyalizasyon süresi nedeniyle daha sonra "Hızlı Yargılama" olarak adlandırılacaktır. David Harding bu fikri daha geniş bir topluluğa şöyle açıklıyor

[Bitcoin-dev posta listesine e-posta](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> Bu teklifin önceki versiyonu 200 gün önce belgelendirildi ve Taproot'ün temel kodu 140 gün önce Bitcoin core ile birleştirildi.Taproot'ün birleştirildiği sırada Hızlı Deneme'ye başlamış olsaydık (ki bu biraz gerçekçi değil), Taproot'e sahip olmamıza iki aydan daha az bir süre kalmış olacaktı ya da bir ay önce bir sonraki etkinleştirme girişimine geçecektik.
>

> Bunun yerine, uzun uzun tartıştık ve posta listesinin bir yıldan uzun bir süre önce SegWit sonrası aktivasyon şemalarını tartışmaya başladığı zamandan daha geniş çapta kabul edilebilir bir çözüm olduğunu düşündüğüm şeye daha yakın görünmüyoruz Bence Speedy Trial, tartışmayı sona erdirecek (şimdilik, aktivasyon başarılı olursa) veya gelecekteki Taproot aktivasyon önerilerini temel alabileceğimiz bazı gerçek veriler sağlayacak generate hızlı ilerlemenin bir yoludur.

Bu dağıtım mekanizması iki ay boyunca geliştirildi ve ardından [Bitcoin core sürüm 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork)'de yayınlandı. Madenciler, dağıtım durumunu `LOCKED_IN` konumuna taşıyan bu yükseltme için hızla sinyal vermeye başladı ve bir ödemesiz dönemin ardından Taproot kuralları Kasım 2021 ortasında [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244) bloğunda etkinleştirildi.


#### Gelecekteki dağıtım mekanizmaları


Son Soft çatalları, SegWit ve Taproot ile ilgili sorunlar göz önüne alındığında, bir sonraki güncellemenin nasıl dağıtılacağı belli değil. Speedy Trial, Taproot'ü dağıtmak için kullanıldı, ancak UASF ve MASF kalabalıkları arasındaki uçurumu kapatmak için kullanıldı, en iyi bilinen dağıtım mekanizması olarak ortaya çıktığı için değil.


### Riskler


İster Hard ya da Soft, ister Miner ya da kullanıcı tarafından aktive edilmiş olsun, herhangi bir Fork'in aktivasyonu sırasında uzun süreli bir zincir bölünmesi riski vardır. Birkaç bloktan fazla süren bir bölünme, Bitcoin'nın etrafındaki duyarlılığa ve fiyatına ciddi zarar verebilir. Ancak hepsinden önemlisi, Bitcoin'nın ne olduğu konusunda büyük bir kafa karışıklığına neden olacaktır. Bitcoin bu zincir mi yoksa o zincir mi?


Kullanıcı tarafından etkinleştirilen bir Soft Fork'nin riski, Hash gücünün çoğunluğu bunları desteklemese bile yeni kuralların etkinleştirilmesidir. Bu senaryo, Hash gücünün çoğunluğu yeni kuralları benimseyene kadar devam edecek uzun süreli bir zincir bölünmesine neden olacaktır. Özellikle Hard, madencileri eski zincirdeki bölünmeden sonra zaten blok çıkarmışlarsa yeni zincire geçmeye teşvik edebilir, çünkü şubeyi değiştirerek kendi blok ödüllerinden vazgeçmiş olacaklardır. Bununla birlikte, dikkate değer bir olaydan bahsetmek gerekir: Mart 2013'te, kasıtsız bir Hard Fork nedeniyle uzun süreli bir bölünme meydana geldi ve bu teşviğin aksine, iki büyük Mining havuzu, konsensüsü yeniden sağlamak için bölünmenin kendi dalını terk etme kararı aldı.


Öte yandan, Miner'nin Soft Fork'yı aktive etmesiyle ilgili risk, madencilerin yanlış sinyalleme yapabileceği gerçeğinin bir sonucudur, bu da değişikliği destekleyen Hash gücünün gerçek payının göründüğünden daha küçük olabileceği anlamına gelir. Eğer gerçek destek Hash gücünün çoğunluğunu oluşturmuyorsa, muhtemelen bir önceki paragrafta anlatılana benzer uzun süreli bir zincirleme bölünme göreceğiz. Bu ya da en azından benzer bir sorun, BIP66 konuşlandırıldığında gerçekte yaşandı, ancak 6 blok içinde çözüldü.


#### Bölünme maliyetleri



Jimmy Song [Hard çatallarıyla ilgili maliyetler hakkında konuştu] (https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) Paris'teki Breaking Bitcoin'de, ancak söylediklerinin çoğu başarısız bir Soft Fork nedeniyle zincirin bölünmesi için de geçerlidir. Negatif dışsallıklardan* bahsetti ve bunları sizin kendi eylemleriniz için başkalarının ödemesi gereken bedel olarak tanımladı:


> Negatif dışsallığın klasik örneği bir fabrikadır. Belki bir petrol rafinerisi üretiyorlardır ve ekonomi için iyi olan bir mal üretiyorlardır ama aynı zamanda kirlilik gibi negatif dışsallık olan bir şey de üretiyorlardır. Bu sadece herkesin bedelini ödemek, temizlemek ya da acı çekmek zorunda olduğu bir şey değildir. Ama aynı zamanda 2. ve 3. dereceden etkiler de söz konusudur, örneğin fabrikaya gitmesi gereken daha fazla işçi nedeniyle fabrikaya doğru giden daha fazla trafik gibi. Ayrıca çevredeki bazı vahşi yaşamı da tehlikeye atabilirsiniz. Negatif dışsallıkların bedelini herkes ödemek zorunda değil, daha önce o yolu kullanan insanlar ya da o fabrikanın yakınında bulunan hayvanlar gibi belirli insanlar da ödeyebilir ve onlar da o fabrikanın maliyetini ödüyorlar.

Bitcoin bağlamında, 2017'deki bu konferanstan kısa bir süre önce oluşturulan Bitcoin'ün bir Hard Fork'si olan Bitcoin Cash'i (bcash) kullanarak negatif dışsallıkları örneklendirmektedir. Bir Hard Fork'nin negatif dışsallıklarını tek seferlik maliyetler ve kalıcı maliyetler olarak kategorize etmektedir.


Tek seferlik maliyetlerin birçok örneği arasında, borsalar tarafından üstlenilen maliyetlerden bahsetmektedir:


> Bu yüzden bir dizi borsamız var ve ödemek zorunda oldukları çok sayıda tek seferlik maliyetleri vardı. İlk olarak bu borsalarda para yatırma ve çekme işlemleri bir ya da iki günlüğüne durduruldu çünkü ne olacağını bilmiyorlardı. Bu borsaların çoğu Cold deposuna dalmak zorunda kaldı çünkü kullanıcıları bcash talep ediyordu. Bu onların güvene dayalı görevlerinin bir parçası, bunu yapmak zorundalar. Ayrıca yeni yazılımı denetlemek zorundasınız. Bu bizim itbit'te yapmamız gereken bir şeydi. Nakit harcamak istiyoruz, nasıl yapacağız? Electron Cash'i indirmek zorunda mıyız? Kötü amaçlı yazılım var mı? Gidip denetlememiz gerekiyor. Bunun iyi olup olmadığını anlamak için 10 günümüz vardı. Ve sonra karar vermek zorundasınız, sadece bir kerelik para çekmeye izin verecek miyiz, yoksa bu yeni Coin'yı listeleyecek miyiz? Bir Exchange'ün yeni Coin'yı listelemesi kolay değildir - Cold'nin depolanması, imzalanması, yatırılması, çekilmesi için bir sürü yeni prosedür vardır. Ya da sadece bir kereye mahsus olmak üzere, bir noktada paralarını verip bir daha hiç düşünmeyeceğiniz bir etkinlik düzenleyebilirsiniz. Ancak bunun da sorunları var. Ve son olarak, ne şekilde yaparsanız yapın, para çekme veya listeleme - tek seferlik bir para çekme olsa bile, bir şekilde bu token ile çalışmak için yeni bir altyapıya ihtiyacınız olacak. Bu tokenları kullanıcılarınıza vermenin bir yolunu bulmalısınız. Yine, kısa süreli. Değil mi? Bunu yapmak için zaman yok, hızlıca yapılmalı.

Ayrıca tüccarlar, ödeme işlemcileri, cüzdanlar, madenciler ve kullanıcılar tarafından katlanılan tek seferlik maliyetlerin yanı sıra gizlilik kaybı ve daha yüksek yeniden düzenleme riski gibi bazı kalıcı maliyetleri de listeliyor.


Gerçekten de, bir bölünme gerçekleştiğinde ve en genel kurallara sahip zincir daha katı kurallara sahip zincirden daha güçlü hale geldiğinde, bir reorg meydana gelecektir. Bu, silinen dalda gerçekleştirilen tüm işlemler üzerinde ciddi bir etkiye sahip olacaktır. Bu nedenlerden dolayı zincir bölünmelerinden her zaman kaçınmaya çalışmak gerçekten önemlidir.


### Yükseltme Hakkında Sonuç


Bitcoin zamanla büyür ve gelişir. Yıllar boyunca farklı yükseltme mekanizmaları kullanılmıştır ve öğrenme eğrisi diktir. Ağın nasıl tepki verdiği hakkında daha fazla şey öğrendikçe daha sofistike ve sağlam yöntemler icat edilmeye devam ediyor.


Bitcoin'u uyum içinde tutmak için Soft çatallarının ileriye dönük bir yol olduğu kanıtlanmıştır, ancak büyük soru hala tam olarak yanıtlanmamıştır: Soft çatallarını uyumsuzluğa neden olmadan nasıl güvenli bir şekilde dağıtabiliriz?


## Çekişmeli düşünme

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Bu bölüm, nelerin yanlış gidebileceğine ve düşmanların nasıl hareket edebileceğine odaklanan bir zihniyet olan *düşmanca düşünme* konusunu ele almaktadır. Bitcoin'nin güvenlik varsayımlarını ve güvenlik modelini tartışarak başlıyoruz, ardından sıradan kullanıcıların düşmanca düşünerek kendi egemenliklerini ve Bitcoin'nin Full node ademi merkeziyetini nasıl geliştirebileceklerini açıklıyoruz. Ardından, Bitcoin'ye yönelik bazı gerçek tehditlerin yanı sıra düşmanın zihnine de bakıyoruz. Son olarak, insanların neden ilk etapta Bitcoin üzerinde çalıştıklarını anlamanıza yardımcı olabilecek *direniş ekseni* hakkında konuşuyoruz.


Çeşitli sistemlerde güvenliği tartışırken, güvenlik varsayımlarının ne olduğunu anlamak önemlidir. Bitcoin'teki tipik bir güvenlik varsayımı "ayrık logaritma probleminin çözülmesi Hard'tür", yani basitçe söylemek gerekirse, belirli bir açık anahtara karşılık gelen bir özel anahtar bulmak neredeyse imkansızdır. Oldukça güçlü bir diğer güvenlik varsayımı da ağdaki hash gücünün çoğunluğunun dürüst olduğu, yani kurallara göre oynadıklarıdır. Bu varsayımların yanlış olduğu kanıtlanırsa, Bitcoin'ün başı dertte demektir.


2015 yılında Andrew Poelstra Hong Kong'da düzenlenen Scaling Bitcoin konferansında Bitcoin'in güvenlik varsayımlarını analiz ettiği bir konuşma yaptı] (https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/). Konuşmasına, birçok sistemin düşmanları bir dereceye kadar göz ardı ettiğini fark ederek başladı; örneğin, bir binayı her türlü düşmanca olaya karşı korumak gerçekten Hard'dır. Bunun yerine, genellikle birinin binayı yakma olasılığını kabul ediyoruz ve kolluk kuvvetleri vb. aracılığıyla bu ve diğer düşmanca davranışları bir dereceye kadar önlüyoruz.


Greg Maxwell'in bina benzetmesine bakın:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Ancak çevrimiçi işler farklıdır:


> Ancak çevrimiçi ortamda böyle bir durum söz konusu değil. Sahte ve anonim davranışlarımız var, herkes herkese bağlanabilir ve sisteme zarar verebilir. Sisteme zarar vermek mümkünse, bunu yapacaklardır. Görünür olacaklarını ve yakalanacaklarını varsayamayız.

Sonuç olarak, Bitcoin'deki bilinen tüm zayıflıklar bir şekilde halledilmelidir, aksi takdirde istismar edileceklerdir. Sonuçta, Bitcoin dünyadaki en büyük bal küpüdür.


Poelstra, Bitcoin'in nasıl yeni bir sistem türü olduğundan bahsetmeye devam ediyor; örneğin, çok net güvenlik varsayımları olan bir imzalama protokolünden daha belirsiz.


Yazılım mühendisi Jameson Lopp, kişisel blogunda [bu konuya dalıyor] (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> Gerçekte, Bitcoin protokolü resmi olarak tanımlanmış bir spesifikasyon veya güvenlik modeli olmaksızın inşa edilmiştir ve edilmektedir. Yapabileceğimiz en iyi şey, daha iyi anlamak ve tanımlamaya çalışmak için sistem içindeki aktörlerin teşviklerini ve davranışlarını incelemektir.

Dolayısıyla, pratikte çalışıyor gibi görünen ancak güvenli olduğunu resmi olarak kanıtlayamadığımız bir sistemimiz var. Muhtemelen şu nedenlerden dolayı bir kanıt mümkün değildir

sistemin kendi karmaşıklığı.


### Sadece Bitcoin uzmanları için değil



Karşıt düşüncenin önemi, yalnızca sıkı Bitcoin geliştiricileri ve uzmanları için değil, bir dereceye kadar günlük Bitcoin kullanıcıları için de geçerlidir. Ragnar Lifthasir bir [tweetstorm]'da (https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking) Bitcoin etrafındaki basit anlatıların - örneğin, "sadece HODL" - Bitcoin'in kendisini nasıl aşağılayıcı olabileceğinden bahsediyor ve sözlerini şöyle bitiriyor


> Bitcoin'ü ve kendimizi daha güçlü kılmak için Bitcoin'e katkıda bulunan yazılım mühendisleri gibi düşünmeliyiz. Onlar acımasızca kusurları arayarak akran değerlendirmesi yaparlar. Teknoloji etkinliklerinde bir teklifin başarısız olabileceği her türlü yol hakkında konuşurlar. Karşıt düşünürler. Muhafazakârdırlar

Bu basit anlatıları monomani olarak adlandırıyor. Bu tanımla, tek bir şeye odaklanarak - örneğin, "sadece HODL"- Bitcoin'inizi güvende tutmak veya Bitcoin'i Trustless tarzında kullanmak için elinizden gelenin en iyisini yapmak gibi tartışmasız daha önemli şeyleri gözden kaçırma riskiniz olduğunu söylüyor.


### Tehditler



Bitcoin'de bilinen birçok zayıflık vardır ve bunların birçoğu aktif olarak istismar edilmektedir. Bu konuda bir fikir edinmek için Bitcoin wiki'deki [Zayıflıklar sayfasına] (https://en.Bitcoin.it/wiki/Weaknesses) bir göz atın. Orada aşağıdakiler gibi çok çeşitli sorunlardan bahsedilmektedir

Wallet hırsızlığı ve hizmet reddi saldırıları:


> Eğer bir saldırgan ağı kendi kontrol ettiği istemcilerle doldurmaya çalışırsa, o zaman sadece saldırgan düğümlere bağlanma olasılığınız çok yüksek olacaktır. Bitcoin hiçbir zaman düğüm sayısını kullanmasa da, bir düğümü dürüst ağdan tamamen izole etmek diğer saldırıların yürütülmesinde yardımcı olabilir.

Bu saldırı türü *Sybil saldırısı* olarak adlandırılır ve tek bir varlık bir ağdaki birden fazla düğümü kontrol ettiğinde ve bunları birden fazla varlık olarak görünmek için kullandığında ortaya çıkar.


Alıntıda da belirtildiği gibi, Sybil saldırısı Bitcoin ağında etkili değildir çünkü düğümler veya diğer sayılabilir varlıklar aracılığıyla değil, daha ziyade bilgi işlem gücü aracılığıyla oylama yapılmaktadır. Bununla birlikte, bu düz yapı sistemi diğer saldırılara karşı hassas bırakmaktadır. Bitcoin wiki sayfası ayrıca bilgi gizleme (genellikle *eclipse attack* olarak adlandırılır) gibi diğer olası saldırıları ve Bitcoin core'un bu tür saldırılara karşı bazı sezgisel karşı önlemleri nasıl uyguladığını özetlemektedir.


Yukarıdakiler, ilgilenilmesi gereken gerçek tehditlere örnektir.


### Basit Sabotaj Alanı


![](assets/sabotage-manual.webp)


Basit Sabotaj Saha El Kitabından Alıntı


Düşmanın zihnini daha iyi anlamak için, nasıl çalıştıklarına dair bir fikir edinmek faydalı olabilir. İkinci Dünya Savaşı sırasında faaliyet gösteren ve amaçları arasında casusluk yapmak, sabotaj gerçekleştirmek ve propaganda yaymak olan Office of Strategic Services adlı bir ABD hükümet kuruluşu, personeline düşmana nasıl sabotaj yapılacağı konusunda bir [el kitabı] (https://www.gutenberg.org/ebooks/26184) hazırladı. Başlığı "Basit Sabotaj Saha El Kitabı" idi ve düşmanın içine sızarak hayatlarını Hard yapmak için somut ipuçları içeriyordu. İpuçları depoları yakmaktan, düşmanın gücünü azaltmak için tatbikatlarda yıpranmaya neden olmaya kadar uzanıyordu

verimlilik.


Örneğin, bir infiltratörün organizasyonları nasıl bozabileceği hakkında bir bölüm var. Bu tür taktiklerin herkesin katılımına açık olan Bitcoin geliştirme sürecini hedef almak için nasıl kullanılabileceğini görmek Hard değildir. Kendini işine adamış bir saldırgan, ilgisiz konularla ilgili bitmek bilmeyen endişelerle ilerlemeyi durdurabilir, kesin ifadeler üzerinde pazarlık yapabilir ve zaten kapsamlı bir şekilde ele alınmış olan tartışmaları tekrarlamaya çalışabilir. Saldırgan kendi etkinliğini artırmak için bir trol ordusu da kiralayabilir; buna sosyal Sybil saldırısı diyebiliriz. Sosyal Sybil saldırısını kullanarak, önerilen bir değişikliğe karşı gerçekte olduğundan daha fazla direnç varmış gibi gösterebilirler.


Bu durum, kararlı bir devletin düşmanı yok etmek için, onu içeriden çökertmek de dahil olmak üzere, elinden gelen her şeyi nasıl yapabileceğini ve yapacağını vurgulamaktadır. Bitcoin yerleşik itibari para birimleriyle rekabet eden bir para biçimi olduğundan, devletlerin Bitcoin'i bir düşman olarak görme ihtimali vardır.


### Direniş Aksiyomu


Eric Voskuil [Cryptoeconomics wiki sayfasında yazıyor] (https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) "direniş aksiyomu" dediği şey hakkında:


> Diğer bir deyişle, bir sistemin devlet kontrolüne direnmesinin mümkün olduğuna dair bir varsayım vardır. Bu bir gerçek olarak kabul edilmemekle birlikte, benzer sistemlerin davranışlarının ampirik olarak incelenmesi nedeniyle, sistemin dayandırılacağı makul bir varsayım olarak kabul edilmektedir.
>

> Direnç aksiyomunu kabul etmeyen biri Bitcoin'dan tamamen farklı bir sistem düşünmektedir. Bir sistemin devlet kontrollerine direnmesinin mümkün olmadığı varsayılırsa, sonuçlar Bitcoin bağlamında bir anlam ifade etmez - tıpkı küresel geometrideki sonuçların Öklid ile çelişmesi gibi. Aksiyom olmadan Bitcoin nasıl izinsiz ya da sansüre dirençli olabilir? Çelişki, kişinin çatışmayı rasyonalize etme çabası içinde bariz hatalar yapmasına yol açmaktadır.


Esasen söylediği şey, ancak devletlerin kontrol edemeyeceği bir sistem yaratmanın mümkün olduğu varsayıldığında denemenin anlamlı olduğudur.


Bu, Bitcoin üzerinde çalışmak için direnç aksiyomunu kabul etmeniz gerektiği, aksi takdirde zamanınızı başka projelere harcamanızın daha iyi olacağı anlamına gelir. Bu aksiyomu kabul etmek, geliştirme çabalarınızı eldeki gerçek sorunlara odaklamanıza yardımcı olur: devlet düzeyindeki düşmanlar etrafında kodlama. Başka bir deyişle, düşmanca düşünün.


### Çekişmeli Düşünme Hakkında Sonuç



Merkezi olmayan bir sistemin kendi dışında hesap verebilirliği olamaz, bu nedenle Bitcoin kötü niyetli davranışları geleneksel sistemlerden daha sıkı bir şekilde önlemelidir. Böyle bir sistemde düşmanca düşünmek zorunludur.


Bitcoin'u güvende tutabilmek için düşmanlarını ve onların teşviklerini bilmeniz gerekir. Tehditlerin çoğu, vergilendirme ve para basma yoluyla muazzam bir ekonomik güce sahip olan ulus devletlerde toplanıyor gibi görünüyor. Muhtemelen para basma ayrıcalıklarından kolay kolay vazgeçmeyeceklerdir.


## Açık Kaynak

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin açık kaynak kodlu yazılım kullanılarak inşa edilmiştir. Bu bölümde bunun ne anlama geldiğini, yazılımın bakımının nasıl yapıldığını ve Bitcoin'taki açık kaynak kodlu yazılımın izinsiz geliştirmeye nasıl izin verdiğini analiz ediyoruz. Kriptografik sistemlerde kütüphanelerin seçimi ve kullanımı ile ilgilenen *seçim kriptografisi* konusuna giriyoruz. Bu bölümde Bitcoin'ın inceleme süreci hakkında bir bölüm ve ardından Bitcoin geliştiricilerinin finansman bulma yolları hakkında bir başka bölüm yer alıyor. Son bölüm, Bitcoin'ın açık kaynak kültürünün dışarıdan nasıl gerçekten tuhaf görünebileceğinden ve bu algılanan tuhaflığın neden gerçekten iyi bir sağlık işareti olduğundan bahsediyor.


Çoğu Bitcoin yazılımı ve özellikle Bitcoin core açık kaynak kodludur. Bu, yazılımın kaynak kodunun inceleme, düzeltme, değiştirme ve yeniden dağıtım için genel kamunun kullanımına sunulduğu anlamına gelir. Açık kaynağın [](https://opensource.org/osd) adresindeki tanımı, diğerlerinin yanı sıra, aşağıdaki önemli noktaları içerir:


> Ücretsiz Yeniden Dağıtım: Lisans, herhangi bir tarafın yazılımı birkaç farklı kaynaktan programlar içeren bir toplu yazılım dağıtımının bileşeni olarak satmasını veya dağıtmasını kısıtlamayacaktır. Lisans, bu tür bir satış için telif hakkı veya başka bir ücret gerektirmeyecektir.
>

> Kaynak Kodu: Program kaynak kodu içermeli ve kaynak kodunun yanı sıra derlenmiş biçimde de dağıtıma izin vermelidir. Ürünün bir formunun kaynak koduyla birlikte dağıtılmadığı durumlarda, kaynak kodunun makul bir çoğaltma maliyetini aşmayacak şekilde, tercihen internet üzerinden ücretsiz olarak indirilerek elde edilebileceği iyi duyurulmuş bir yöntem bulunmalıdır. Kaynak kodu, bir programcının programı değiştireceği tercih edilen formda olmalıdır. Kasıtlı olarak gizlenmiş kaynak koduna izin verilmez. Bir ön işlemci veya çevirmen çıktısı gibi ara formlara izin verilmez.
>

> Türetilmiş Çalışmalar: Lisans, değişikliklere ve türetilmiş çalışmalara izin vermeli ve bunların orijinal yazılımın lisansı ile aynı koşullar altında dağıtılmasına izin vermelidir.

Bitcoin core, [MIT Lisansı] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING) altında dağıtılmak suretiyle bu tanıma uymaktadır:


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


"Güvenmeyin, Doğrulayın" bölümünde belirtildiği gibi, kullanıcıların çalıştırdıkları Bitcoin yazılımının "söylendiği gibi çalıştığını" doğrulayabilmeleri önemlidir. Bunu yapmak için, doğrulamak istedikleri yazılımın kaynak koduna sınırsız erişime sahip olmalıdırlar.


İlerleyen bölümlerde Bitcoin'daki açık kaynaklı yazılımın diğer bazı ilginç yönlerini inceleyeceğiz.


### Yazılım bakımı



Bitcoin core'nin kaynak kodu [GitHub] (https://github.com/Bitcoin/Bitcoin) üzerinde barındırılan bir Git deposunda tutulmaktadır. Herkes herhangi bir izin istemeden bu depoyu klonlayabilir ve ardından yerel olarak inceleyebilir, derleyebilir veya üzerinde değişiklik yapabilir. Bu, deponun dünya geneline yayılmış binlerce kopyası olduğu anlamına gelir. Bunların hepsi aynı deponun kopyalarıdır, peki bu özel GitHub Bitcoin core deposunu bu kadar özel yapan nedir? Teknik olarak hiç de özel değil, ancak sosyal olarak Bitcoin geliştirmesinin odak noktası haline geldi.


Bitcoin ve güvenlik uzmanı Jameson Lopp bunu "Bitcoin core'u Kim Kontrol Ediyor?" başlıklı [blog yazısında] (https://blog.lopp.net/who-controls-Bitcoin-core-/) çok iyi açıklıyor:


> Bitcoin core, bir komuta ve kontrol noktası olmaktan ziyade Bitcoin protokolünün geliştirilmesi için bir odak noktasıdır. Herhangi bir nedenle varlığı sona ererse, yeni bir odak noktası ortaya çıkacaktır - dayandığı teknik iletişim platformu (şu anda GitHub deposu) bir tanım / proje bütünlüğünden ziyade bir kolaylık meselesidir. Aslında, Bitcoin'nin geliştirme için odak noktasının platformları ve hatta isimleri değiştirdiğini zaten gördük!

Bitcoin core'ün yazılımının nasıl korunduğunu ve kötü niyetli kod değişikliklerine karşı nasıl güvence altına alındığını açıklamaya devam ediyor. Bu makalenin genel çıkarımı en sonunda özetlenmiştir:


> Bitcoin'ü kimse kontrol etmiyor.
>

> Bitcoin gelişiminin odak noktasını kimse kontrol etmemektedir.

Bitcoin core geliştiricisi Eric Lombrozo, "The Bitcoin core Merge Process" başlıklı [Medium post] (https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) yazısında geliştirme süreci hakkında daha fazla bilgi veriyor:


> Herkes Fork kod tabanı deposunu kullanabilir ve kendi deposunda keyfi değişiklikler yapabilir. Kendi depolarından bir istemci oluşturabilir ve isterlerse bunu çalıştırabilirler. Ayrıca başkalarının çalıştırması için ikili yapılar da oluşturabilirler.
>

> Birisi kendi deposunda yaptığı bir değişikliği Bitcoin core ile birleştirmek isterse, bir çekme isteği gönderebilir. Gönderildikten sonra, Bitcoin core'un kendisine commit erişimine sahip olup olmadıklarına bakılmaksızın herkes değişiklikleri inceleyebilir ve bunlar hakkında yorum yapabilir.

Çekme isteklerinin bakımcılar tarafından depoya birleştirilmesinin çok uzun zaman alabileceği ve bunun genellikle inceleme eksikliğinden kaynaklandığı unutulmamalıdır; bu da genellikle *inceleyici* eksikliğinden kaynaklanmaktadır.


Lombrozo ayrıca mutabakat değişikliklerini çevreleyen süreçten de bahsetmektedir, ancak bu bölümün kapsamının biraz dışındadır. Bitcoin protokolünün nasıl yükseltildiği hakkında daha fazla bilgi için önceki "Yükseltme" bölümüne bakın.


### İzinsiz geliştirme



Herkesin herhangi bir izin istemeden Bitcoin core için kod yazabileceğini, ancak bunun ana Git deposuyla birleştirilmesi gerekmediğini belirledik. Bu, grafiksel kullanıcı Interface'ün renk şemalarının değiştirilmesinden, eşler arası mesajların biçimlendirilme şekline ve hatta fikir birliği kurallarına, yani geçerli bir Blockchain'yi tanımlayan kurallar kümesine kadar her türlü değişikliği etkiler.


Muhtemelen eşit derecede önemli olan, kullanıcıların herhangi bir izin istemeden Bitcoin üzerinde sistem geliştirmekte özgür olmalarıdır. Bitcoin üzerine inşa edilmiş sayısız başarılı yazılım projesi gördük, örneğin:



- Lightning Network: Çok küçük miktarların hızlı bir şekilde ödenmesini sağlayan bir ödeme ağı. Çok az sayıda On-Chain Bitcoin işlemi gerektirir. Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) ve [Lightning Dev Kit](https://github.com/lightningdevkit) gibi çeşitli birlikte çalışabilir uygulamalar mevcuttur.
- CoinJoin: Birden fazla taraf, Address kümelemesini zorlaştırmak amacıyla ödemelerini tek bir işlemde birleştirmek için işbirliği yapar. Çeşitli uygulamalar mevcuttur.
- Yan zincirler: Bu sistem, başka bir Blockchain'de kilidini açmak için Bitcoin'ün Blockchain'indeki bir Coin'i kilitleyebilir. Bu, bitcoinlerin başka bir Blockchain'e, yani bir Sidechain'ye taşınmasına izin verir, böylece bu Sidechain'de bulunan özellikleri kullanabilir. Örnekler arasında [Blockstream's Elements] (https://github.com/ElementsProject/Elements) yer almaktadır.
- OpenTimestamps: Bitcoin'in Blockchain'sında özel bir şekilde [Timestamp bir belge] (https://opentimestamps.org/) yapmanızı sağlar. Daha sonra bu Timestamp'yi bir belgenin belirli bir zamandan önce var olması gerektiğini kanıtlamak için kullanabilirsiniz.


İzinsiz geliştirme olmasaydı, bu projelerin birçoğu mümkün olmazdı. Tarafsızlık bölümünde belirtildiği gibi, geliştiriciler Bitcoin'un üzerine protokoller inşa etmek için izin istemek zorunda kalsaydı, yalnızca merkezi geliştirici onay komitesinin izin verdiği protokoller geliştirilirdi.


Yukarıda listelenenler gibi sistemlerin açık kaynak yazılım olarak lisanslanması yaygındır, bu da insanların herhangi bir izin istemeden kodlarına katkıda bulunmalarına, yeniden kullanmalarına veya incelemelerine olanak tanır. Açık kaynak, Bitcoin yazılım lisanslamasının altın standardı haline gelmiştir.


### Sahte isim gelişimi



Bitcoin yazılımını geliştirmek için izin istemek zorunda olmamak, masaya ilginç ve önemli bir seçenek getiriyor: Bitcoin core veya başka bir açık kaynak projesinde kimliğinizi açıklamadan kod yazabilir ve yayınlayabilirsiniz.


Birçok geliştirici, takma bir isim altında çalışarak ve gerçek kimliklerinden ayrı tutmaya çalışarak bu seçeneği tercih eder. Bunu yapma nedenleri geliştiriciden geliştiriciye değişebilir. Takma isimli kullanıcılardan biri ZmnSCPxj'dir. Diğer projelerin yanı sıra, Bitcoin core ve Lightning Network'ün çeşitli uygulamalarından biri olan Core Lightning'e katkıda bulunmaktadır. [Web sayfasında](https://zmnscpxj.github.io/about.html) yazıyor:


> Ben ZmnSCPxj, rastgele oluşturulmuş bir internet kişisiyim. Zamirlerim he/him/his.
>

> İnsanların içgüdüsel olarak kimliğimi bilmek istediklerini anlıyorum. Ancak ben kimliğimin büyük ölçüde önemsiz olduğunu düşünüyorum ve işimle değerlendirilmeyi tercih ediyorum.
>

> Bağış yapıp yapmayacağınızı merak ediyorsanız ve yaşam maliyetimin veya gelirimin ne olduğunu merak ediyorsanız, lütfen doğru konuşursak, bana bulduğunuz faydaya göre bağış yapmanız gerektiğini anlayın
makaleler ve Bitcoin ve Lightning Network üzerindeki çalışmalarım.


Onun durumunda, takma ad kullanmasının nedeni, takma adın arkasındaki kişi veya kişilerin kim olduğu veya olduğu değil, kendi esasına göre değerlendirilmelidir. İlginç bir şekilde, CoinDesk'teki bir [makalede] (https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/) takma adın farklı bir nedenle oluşturulduğunu açıkladı.


> Takma ad kullanmamın ilk nedeni basitçe büyük bir hata yapmaktan endişe etmemdi; dolayısıyla ZmnSCPxj başlangıçta böyle bir durumda terk edilebilecek tek kullanımlık bir takma ad olarak tasarlanmıştı. Ancak çoğunlukla olumlu bir ün kazanmış gibi görünüyor, bu yüzden onu korudum

Takma ad kullanmak, aptalca bir şey söylemeniz veya büyük bir hata yapmanız durumunda kişisel itibarınızı riske atmadan daha özgürce konuşmanızı sağlar. Anlaşıldığı üzere, takma adı çok itibar kazandı ve 2019'da [bir geliştirme hibesi bile aldı] (https://twitter.com/spiralbtc/status/1204815615678177280), bu da Bitcoin'in izinsiz doğasının bir kanıtıdır.


Muhtemelen, Bitcoin'daki en iyi bilinen takma ad Satoshi Nakamoto'dur. Neden takma isim kullanmayı seçtiği belli değil, ancak geriye dönüp baktığımızda bunun birçok nedenden ötürü muhtemelen iyi bir karar olduğunu görüyoruz:


- Birçok kişi Nakamoto'nun çok sayıda Bitcoin'e sahip olduğunu düşündüğünden, kimliğinin bilinmemesi mali ve kişisel güvenliği için zorunludur.
- Kimliği bilinmediği için kimsenin yargılanma ihtimali yok, bu da çeşitli hükümet yetkililerine Hard zamanı veriyor.
- Örnek alınacak otoriter bir kişi yoktur, bu da Bitcoin'ü daha meritokratik ve şantaja karşı daha dirençli hale getirir.


Bu noktaların sadece Satoshi Nakamoto için değil, Bitcoin'te çalışan veya önemli miktarda para birimine sahip olan herkes için farklı derecelerde geçerli olduğuna dikkat edin.


### Seçim kriptografisi


Açık kaynak geliştiricileri genellikle başkaları tarafından geliştirilen açık kaynak kütüphanelerinden yararlanırlar. Bu, sağlıklı bir ekosistemin doğal ve harika bir parçasıdır. Ancak Bitcoin yazılımı gerçek parayla ilgilenir ve bunun ışığında, geliştiricilerin hangi üçüncü taraf kütüphanelerine bağlı olması gerektiğini seçerken çok dikkatli olmaları gerekir.


Kriptografi hakkında felsefi bir konuşmada] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/), Gregory Maxwell çok dar olduğuna inandığı "kriptografi" terimini yeniden tanımlamak istiyor. Temelde *bilginin özgür olmak istediğini* açıklıyor ve kriptografi tanımını buna dayanarak yapıyor:


> Kriptografi, bilginin temel doğasıyla mücadele etmek, onu siyasi ve ahlaki irademize göre bükmek ve tüm şans ve karşı koyma çabalarına rağmen onu insani amaçlara yönlendirmek için kullandığımız sanat ve bilimdir.

Daha sonra kriptografik araçları seçme sanatı olarak adlandırılan *seçim kriptografisi* terimini tanıtıyor ve bunun neden kriptografinin önemli bir parçası olduğunu açıklıyor. Kriptografik kütüphanelerin, araçların ve uygulamaların nasıl seçileceği ya da kendi deyimiyle "kriptosistem seçme kriptosistemi" etrafında dönmektedir.


Somut örnekler kullanarak, seçim kriptografisinin nasıl kolayca korkunç bir şekilde yanlış gidebileceğini gösteriyor ve ayrıca bunu uygularken kendinize sorabileceğiniz bir soru listesi öneriyor. Aşağıda bu listenin damıtılmış bir versiyonu yer almaktadır:


- Yazılım sizin amaçlarınız için mi tasarlandı?
- Kriptografik hususlar ciddiye alınıyor mu?
- İnceleme süreci nedir? Öyle bir süreç var mı?
- Yazarların deneyimi nedir?
- Yazılım belgelenmiş mi?
- Yazılım taşınabilir mi?
- Yazılım test edildi mi?
- Yazılım en iyi uygulamaları benimsiyor mu?


Bu başarı için nihai bir rehber olmasa da, seçim kriptografisi yaparken bu noktaların üzerinden geçmek çok yararlı olabilir.


Yukarıda Maxwell tarafından belirtilen sorunlar nedeniyle, Bitcoin core gerçekten Hard'ü [üçüncü taraf kütüphanelerine maruz kalmasını en aza indirmeye] çalışmaktadır (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Elbette, tüm dış bağımlılıkları ortadan kaldıramazsınız, aksi takdirde yazı tipi oluşturmadan sistem çağrılarının uygulanmasına kadar her şeyi kendiniz yazmak zorunda kalırsınız.


### İnceleme



Bu bölüm "Kod incelemesi" yerine "İnceleme" olarak adlandırılmıştır, çünkü Bitcoin'in güvenliği sadece kaynak koduna değil, birçok seviyede incelemeye dayanmaktadır. Dahası, farklı fikirler farklı seviyelerde inceleme gerektirir: bir fikir birliği kuralı değişikliği, bir renk şeması değişikliği veya yazım hatası düzeltmesine kıyasla daha fazla seviyede daha derin bir inceleme gerektirecektir.


Bir fikir nihai olarak benimsenme yolunda genellikle çeşitli tartışma ve inceleme aşamalarından geçer. Bu aşamalardan bazıları aşağıda listelenmiştir:



- Bitcoin-dev posta listesinde bir fikir yayınlanmıştır
- Bu fikir bir Bitcoin İyileştirme Teklifi (BIP) olarak resmileştirilmiştir
- BIP, Bitcoin core'e bir çekme isteği (PR) olarak uygulanmaktadır
- Dağıtım mekanizmaları tartışılmaktadır
- Bazı rakip dağıtım mekanizmaları Bitcoin core'e yapılan çekme taleplerinde uygulanmaktadır
- Çekme istekleri ana dal ile birleştirilir
- Kullanıcılar yazılımı kullanıp kullanmamayı seçer


Bu aşamaların her birinde farklı bakış açılarına ve geçmişlere sahip kişiler, kaynak kodu, bir BIP veya sadece gevşek bir şekilde tanımlanmış bir fikir gibi mevcut bilgileri gözden geçirir. Aşamalar genellikle yukarıdan aşağıya katı bir şekilde gerçekleştirilmez, aslında birden fazla aşama aynı anda gerçekleşebilir ve bazen bunlar arasında gidip gelirsiniz. Farklı aşamalar sırasında farklı kişiler de geri bildirim sağlayabilir.


Bitcoin core'daki en üretken kod gözden geçiricilerden biri Jon Atack'tır. Bitcoin core'da çekme isteklerinin nasıl gözden geçirileceği hakkında [bir blog yazısı] (https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) yazdı. İyi bir kod gözden geçiricinin en iyi nasıl değer katabileceğine odaklandığını vurguluyor.


> Yeni gelen biri olarak amaç, mümkün olduğunca çok şey öğrenirken, samimiyet ve alçakgönüllülükle değer katmaya çalışmaktır.
>

> İyi bir yaklaşım, konuyu kendinizle ilgili olmaktan çıkarıp "En iyi nasıl hizmet edebilirim?" haline getirmektir

İncelemenin Bitcoin core'de gerçekten sınırlayıcı bir faktör olduğunun altını çiziyor. Pek çok iyi fikir, hiçbir incelemenin yapılmadığı, beklemede olduğu bir arafta sıkışıp kalıyor. Gözden geçirmenin sadece Bitcoin için faydalı olmadığını, aynı zamanda yazılıma değer katarken yazılım hakkında bilgi edinmenin de harika bir yolu olduğunu belirtiyor. Atack'ın temel kuralı, kendi PR'ınızı yapmadan önce 5-15 PR'ı incelemektir. Yine, odak noktanız kendi kodunuzun nasıl birleştirileceği değil, topluluğa nasıl en iyi şekilde hizmet edebileceğiniz olmalıdır. Bunun da ötesinde, incelemeyi doğru seviyede yapmanın önemini vurguluyor: şu an ufak tefek hatalar ve yazım hataları için mi, yoksa geliştiricinin daha kavramsal odaklı bir incelemeye mi ihtiyacı var? Jon Attack ekliyor:


> Bir incelemeye başlarken sorulabilecek faydalı bir ilk soru, "Şu anda burada en çok neye ihtiyaç var?" olabilir Bu soruyu yanıtlamak deneyim ve birikmiş bağlam gerektirir, ancak en az zamanda en fazla değeri nasıl katabileceğinize karar vermede yararlı bir sorudur.

Yazının ikinci yarısı, incelemenin gerçekte nasıl yapılacağına ilişkin bazı yararlı uygulamalı teknik rehberlikten oluşuyor ve daha fazla okuma için önemli belgelere bağlantılar sağlıyor.


Bitcoin core geliştiricisi ve kod incelemecisi Gloria Zhao, bir inceleme sırasında genellikle kendisine sorduğu soruları içeren bir [makale] (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) yazdı. Ayrıca iyi bir inceleme için neleri göz önünde bulundurduğunu da belirtiyor:


> Ben şahsen iyi bir incelemenin, kendime halkla ilişkiler hakkında pek çok soru sorduğum ve cevaplardan tatmin olduğum bir inceleme olduğunu düşünüyorum
onlara. [Doğal olarak, kavramsal sorularla başlıyorum, sonra yaklaşımla ilgili sorular ve sonra da uygulama soruları. Genel olarak, taslak bir PR'ye C++ sözdizimiyle ilgili yorumlar bırakmanın yararsız olduğunu düşünüyorum ve yazar kod düzenleme önerilerimden 20'den fazlasını ele aldıktan sonra "bu mantıklı mı" sorusuna geri dönmek kabalık olur.


İyi bir incelemenin belirli bir zamanda en çok ihtiyaç duyulan şeye odaklanması gerektiği fikri, Jon Atack'ın tavsiyesiyle de uyumlu. O

inceleme sürecinin çeşitli aşamalarında kendinize sorabileceğiniz soruların bir listesini öneriyor, ancak bu listenin hiçbir şekilde kapsamlı veya doğrudan bir reçete olmadığını vurguluyor. Liste GitHub'dan gerçek hayattan örneklerle açıklanmıştır.


### Finansman



Birçok insan Bitcoin açık kaynak geliştirme ile ya Bitcoin core için ya da diğer projeler için çalışmaktadır. Birçoğu bunu boş zamanlarında herhangi bir ücret almadan yapıyor, ancak bazı geliştiriciler de bunu yapmak için para alıyor.


Bitcoin'ün sürekli başarısıyla ilgilenen şirketler, bireyler ve kuruluşlar, doğrudan ya da fonları bireysel geliştiricilere dağıtan kuruluşlar aracılığıyla geliştiricilere bağışta bulunabilirler. Ayrıca yetenekli geliştiricileri işe alarak Bitcoin üzerinde tam zamanlı çalışmalarını sağlayan bir dizi Bitcoin odaklı şirket de bulunmaktadır.


### Kültür Şoku



İnsanlar bazen Bitcoin geliştiricileri arasında çok fazla çekişme ve sonu gelmeyen hararetli tartışmalar olduğu ve karar vermekten aciz oldukları izlenimine kapılıyor.


Örneğin, Taproot dağıtım mekanizması, iki "kampın" oluştuğu uzun bir süre boyunca tartışıldı. Biri, madencilerin belirli bir andan sonra yeni kurallar için ezici bir çoğunlukla oy kullanmaması halinde yükseltmenin "başarısız" olmasını isterken, diğeri ne olursa olsun o andan sonra kuralları uygulamak istedi. Michael Folkson, iki kampın argümanlarını Bitcoin-dev posta listesine gönderdiği bir [e-posta](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) ile özetliyor.


Tartışma sonsuza kadar sürecekmiş gibi görünüyordu ve bu konuda yakın zamanda bir fikir birliği oluşması gerçekten Hard idi. Bu durum insanları sinirlendirdi ve sonuç olarak hararet arttı. Gregory Maxwell (nullc kullanıcısı olarak) [Reddit'te] (https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3) uzun tartışmaların yükseltmeyi daha az güvenli hale getireceğinden endişelendi:


> Bu noktada, ilave bekleme daha fazla inceleme ve kesinlik katmamaktadır. Bunun yerine, ek gecikme ataleti azaltıyor ve insanlar ayrıntıları unutmaya başladıkça, sonraki kullanımla ilgili çalışmaları geciktirdikçe (Wallet desteği gibi) ve etkinleştirme zaman çerçevesinden emin olsalar yatırım yapacakları kadar ek inceleme çabası harcamadıkça riski bir miktar artırıyor.

Sonunda bu anlaşmazlık David Harding ve Russel O'Connor'ın Speedy Trial (Hızlı Deneme) adını verdikleri ve madencilerin Taproot'in aktivasyonunu kilitlemeleri ya da hızlı bir şekilde başarısız olmaları için nispeten daha kısa bir sinyal süresi gerektiren yeni bir teklif sayesinde çözüldü. Eğer bu süre zarfında aktif hale getirirlerse, Taproot yaklaşık 6 ay sonra devreye sokulacaktı.


Bitcoin'nin gelişim sürecine alışkın olmayan biri muhtemelen bu hararetli tartışmaların son derece kötü ve hatta zehirli göründüğünü düşünecektir. Bazı insanların gözünde bunların kötü görünmesine neden olan en az iki faktör vardır:



- Kapalı kaynak şirketleriyle karşılaştırıldığında, tüm tartışmalar açıkta, düzenlenmeden gerçekleşir. Google gibi bir yazılım şirketi, çalışanlarının önerilen özellikleri açık bir şekilde tartışmasına asla izin vermez, hatta en fazla şirketin konuyla ilgili duruşu hakkında bir açıklama yayınlar. Bu da şirketlerin Bitcoin'e kıyasla daha uyumlu görünmesini sağlar.
- Bitcoin izne tabi olmadığından, herkesin görüşlerini dile getirmesine izin verilmektedir. Bu, bir avuç insanın fikir sahibi olduğu, genellikle benzer düşünen insanların bulunduğu kapalı kaynaklı bir şirketten temelde farklıdır. Bitcoin içinde ifade edilen görüşlerin çokluğu, örneğin PayPal ile karşılaştırıldığında şaşırtıcıdır.


Çoğu Bitcoin geliştiricisi, bu açıklığın iyi ve sağlıklı bir ortam yarattığını ve hatta en iyi sonucu elde etmek için gerekli olduğunu savunacaktır.


Tehdit bölümünde ima edildiği gibi, yukarıdaki ikinci madde çok faydalı olabilir ancak bir dezavantajı da vardır. Bir saldırgan, karar alma ve geliştirme sürecini bozmak için [Basit Sabotaj Saha El Kitabı] (https://www.gutenberg.org/ebooks/26184)'da özetlenenler gibi oyalama taktiklerini kullanabilir.


Bahsetmeye değer bir başka şey de, Bitcoin para olduğundan ve Bitcoin core akıl almaz miktarlarda parayı güvence altına aldığından, bu bağlamda güvenliğin hafife alınmamasıdır. Bu yüzden tecrübeli Bitcoin core

geliştiriciler çok Hard kafalı görünebilir, ki bu tutum genellikle haklıdır. Gerçekten de, arkasında zayıf bir gerekçe olan bir özellik kabul edilmeyecektir. Aynı şey, eğer bu özellik

yeniden üretilebilir derlemeler, yeni bağımlılıklar eklediyse veya kod Bitcoin'un [en iyi uygulamalarını] takip etmediyse (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Yeni (ve eski) geliştiriciler bu durum karşısında hayal kırıklığına uğrayabilir. Ancak, açık kaynaklı yazılımlarda alışılageldiği gibi, her zaman Fork deposunu kullanabilir, istediğinizi kendi Fork'unuzla birleştirebilir ve kendi ikili dosyanızı oluşturup çalıştırabilirsiniz.


### Açık Kaynak Hakkında Sonuç


Bitcoin core ve diğer çoğu Bitcoin yazılımı açık kaynak kodludur, bu da herkesin yazılımı istediği gibi dağıtmakta, değiştirmekte ve kullanmakta özgür olduğu anlamına gelir. GitHub'daki Bitcoin core deposu şu anda Bitcoin geliştirmesinin odak noktasıdır, ancak insanlar bakımcılarına veya web sitesinin kendisine güvenmemeye başlarsa bu durum değişebilir.


Açık kaynak, Bitcoin içinde ve üzerinde izinsiz geliştirmeye olanak tanır. İster kod yazın, ister kodu veya protokolleri gözden geçirin; açık kaynak, sözde olsun ya da olmasın, bunu yapmanızı sağlayan şeydir.


Bitcoin etrafındaki geliştirme süreci radikal bir şekilde açıktır, bu da Bitcoin'ün zehirli ve verimsiz bir yer gibi görünmesine neden olabilir, ancak Bitcoin'ü kötü niyetli aktörlere karşı dirençli tutan da budur.


## Ölçeklendirme

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



Bu bölümde, Bitcoin'in nasıl ölçeklenip ölçeklenmediğini araştırıyoruz. Geçmişte insanların ölçeklendirme konusunda nasıl mantık yürüttüklerine bakarak başlıyoruz. Ardından, bu bölümün büyük bir kısmında Bitcoin'i ölçeklendirmeye yönelik çeşitli yaklaşımlar, özellikle de dikey, yatay, içe doğru ve katmanlı ölçeklendirme açıklanmaktadır. Her bir açıklamayı, yaklaşımın Bitcoin'in değer önerisine müdahale edip etmediğine ilişkin değerlendirmeler takip etmektedir.


Bitcoin alanında, farklı kişiler "ölçek" kelimesine farklı tanımlar atfetmektedir. Bazıları bunu Blockchain işlem kapasitesinin artırılması olarak düşünürken, diğerleri Blockchain'nın daha verimli kullanılmasına eşit olduğuna inanıyor ve diğerleri bunu Bitcoin'nin üzerine sistemlerin geliştirilmesi olarak görüyor.


Bitcoin bağlamında ve bu kitabın amaçları doğrultusunda ölçeklendirmeyi *Bitcoin'in sansür direncinden ödün vermeden kullanım kapasitesinin artırılması* olarak tanımlıyoruz. Bu tanım birkaç şeyi kapsamaktadır

örneğin, bu tür değişiklikler:


- İşlem girdilerinin daha az bayt kullanmasını sağlama
- İmza doğrulama performansının iyileştirilmesi
- Eşler arası ağın daha az bant genişliği kullanmasını sağlamak
- İşlem gruplama
- Katmanlı mimari


Yakında ölçeklendirmeye yönelik farklı yaklaşımları inceleyeceğiz, ancak ölçeklendirme bağlamında Bitcoin'un geçmişine kısa bir genel bakışla başlayalım.


### Ölçeklendirmenin Tarihçesi



Ölçeklendirme, Bitcoin'ın Genesis'inden bu yana tartışmaların odak noktası olmuştur. Satoshi'nin Cryptography e-posta listesindeki Bitcoin whitepaper duyurusuna yanıt olarak [ilk e-postanın] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) ilk cümlesi gerçekten de ölçeklendirme hakkındaydı:


> Satoshi Nakamoto yazdı:
>

> "Güvenilir bir üçüncü taraf olmadan, tamamen eşler arası çalışan yeni bir elektronik para sistemi üzerinde çalışıyorum.  Makaleye http://www.Bitcoin.org/Bitcoin.pdf adresinden ulaşabilirsiniz."
>

> Böyle bir sisteme çok ama çok ihtiyacımız var, ancak teklifinizi anladığım kadarıyla gerekli büyüklükte ölçeklendirilebilecek gibi görünmüyor.

Bu konuşma kendi içinde çok ilginç ya da doğru olmayabilir, ancak ölçeklendirmenin en başından beri bir endişe kaynağı olduğunu gösteriyor.


Ölçeklendirme konusundaki tartışmalar, maksimum blok boyutu sınırının artırılıp artırılmayacağı ve nasıl artırılacağı konusunda birçok farklı fikrin dolaştığı 2015-2017 yılları arasında en yüksek ilgiye ulaştı. Bu, kaynak koddaki bir parametrenin değiştirilmesiyle ilgili oldukça ilgisiz bir tartışmaydı, temelde hiçbir şeyi çözmeyen ancak ölçeklendirme sorununu daha da geleceğe iten ve teknik borç oluşturan bir değişiklikti.


2015 yılında Montreal'de [Scaling Bitcoin] (https://scalingbitcoin.org/) adlı bir konferans düzenlenmiş, altı ay sonra Hong Kong'da ve daha sonra dünyanın çeşitli yerlerinde bir takip konferansı yapılmıştır. Odak noktası tam olarak Address'in nasıl ölçeklendirileceğiydi. Birçok Bitcoin geliştiricisi ve diğer meraklılar bu konferanslarda bir araya gelerek çeşitli ölçeklendirme konularını ve önerilerini tartıştılar. Bu tartışmaların çoğu blok boyutu artışları etrafında değil, daha uzun vadeli çözümler etrafında dönüyordu.


Aralık 2015'teki Hong Kong konferansından sonra Gregory Maxwell, bazı genel ölçeklendirme felsefesiyle başlayarak tartışılan birçok konu hakkındaki görüşlerini [özetledi] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html):


> Mevcut teknoloji ile ölçek ve ademi merkeziyetçilik arasında temel ödünleşimler vardır. Eğer sistem çok maliyetli ise insanlar sistemin kurallarını bağımsız olarak uygulamak yerine üçüncü taraflara güvenmek zorunda kalacaklardır. Bitcoin Blockchain'in mevcut teknolojiye göre kaynak kullanımı çok büyükse, Bitcoin eski sistemlere kıyasla rekabet avantajlarını kaybeder çünkü doğrulama çok maliyetli olacak (birçok kullanıcıyı dışarıda bırakacaktır) ve güveni sisteme geri dönmeye zorlayacaktır.  Kapasite çok düşükse ve işlem yapma yöntemlerimiz çok verimsizse, anlaşmazlıkların çözümü için zincire erişim çok maliyetli olacak ve yine güveni sisteme geri itecektir.

Verim ve ademi merkeziyetçilik arasındaki değiş tokuştan bahsediyor. Daha büyük bloklara izin verirseniz, bazı insanları ağın dışına itersiniz çünkü artık blokları doğrulayacak kaynaklara sahip olmayacaklardır. Öte yandan, blok alanına erişim daha pahalı hale gelirse, daha az sayıda insan bunu bir uyuşmazlık çözüm mekanizması olarak kullanmayı göze alabilecektir. Her iki durumda da kullanıcılar güvenilir hizmetlere doğru itilir.


Konferansta sunulan ölçeklendirmeye yönelik birçok yaklaşımı özetleyerek devam ediyor. Bunlar arasında hesaplama açısından daha verimli imza doğrulamaları, blok boyutu sınırı değişikliği de dahil olmak üzere *ayrılmış tanık*, daha fazla alan verimli blok yayma mekanizması ve katmanlar halinde Bitcoin'nin üzerine protokoller oluşturma yer almaktadır. Bunların çoğu

yaklaşımlar o zamandan beri uygulanmaktadır.


### Ölçeklendirme yaklaşımları



Yukarıda ima edildiği gibi, Bitcoin'in ölçeklendirilmesi illa ki blok boyutu sınırının ya da diğer sınırların artırılmasıyla ilgili olmak zorunda değildir. Şimdi ölçeklendirmeye yönelik bazı genel yaklaşımları inceleyeceğiz, bunlardan bazıları önceki bölümde bahsedilen verim-merkezileşme ödünleşiminden muzdarip değildir.


#### Dikey ölçeklendirme



Dikey ölçeklendirme, veri işleyen makinelerin bilgi işlem kaynaklarını artırma sürecidir. Bitcoin bağlamında, bu makineler tam düğümler, yani kullanıcıları adına Blockchain'yi doğrulayan makineler olacaktır.


Bitcoin'te dikey ölçeklendirme için en sık tartışılan teknik, blok boyutu sınırının artırılmasıdır. Bu, bazı tam düğümlerin artan hesaplama taleplerine ayak uydurmak için donanımlarını yükseltmelerini gerektirecektir. Dezavantajı ise bunun merkezileştirme pahasına gerçekleşmesidir.


Full node ademi merkeziyetçiliği üzerindeki olumsuz etkilerin yanı sıra, dikey ölçeklendirme Bitcoin'nın Mining ademi merkeziyetçiliğini ve güvenliğini daha az belirgin şekillerde de olumsuz etkileyebilir. Madencilerin nasıl çalışması "gerektiğine" bir göz atalım. Bir Miner'in 7. yükseklikte bir blok çıkardığını ve bu bloğu Bitcoin ağında yayınladığını varsayalım. Bu bloğun geniş kabul görmesi biraz zaman alacaktır ve bunun başlıca nedeni iki faktördür:


- Bloğun eşler arasında aktarılması bant genişliği sınırlamaları nedeniyle zaman alır.
- Bloğun doğrulanması zaman alır.


Blok 7 ağda yayılırken, birçok madenci blok 7'yi henüz almadıkları ve doğrulamadıkları için hala blok 6'nın üzerinde Mining'dur. Bu süre zarfında, bu madencilerden herhangi biri 7. yükseklikte yeni bir blok bulursa, o yükseklikte iki rakip blok olacaktır. Yükseklik 7'de (ya da başka herhangi bir yükseklikte) yalnızca bir blok olabilir, bu da iki adaydan birinin bayatlaması gerektiği anlamına gelir.


Kısacası, bayat bloklar oluşur çünkü her bloğun yayılması zaman alır ve yayılma ne kadar uzun sürerse, bayat blok olasılığı da o kadar yüksek olur.


Blok boyutu sınırının kaldırıldığını ve ortalama blok boyutunun önemli ölçüde arttığını varsayalım. Bu durumda bloklar bant genişliği sınırlamaları ve doğrulama süresi nedeniyle ağ boyunca daha yavaş yayılacaktır. Yayılma süresindeki artış aynı zamanda blokların bayatlama olasılığını da artıracaktır.


Madenciler, Block reward'larını kaybedecekleri için bloklarının mühürlenmesini istemezler, bu nedenle bundan kaçınmak için ellerinden geleni yaparlar

senaryo. Alabilecekleri önlemler şunları içerir:



- Doğrulamasız Mining* olarak da bilinen, gelen bir bloğun doğrulanmasının ertelenmesi. Madenciler sadece blok başlığının Proof-of-Work'ini kontrol edebilir ve bunun üzerine madencilik yapabilir, bu arada bloğun tamamını indirip doğrulayabilirler.
- Daha yüksek bant genişliğine ve bağlantıya sahip bir Mining pool'e bağlanma.


Doğrulamasız Mining, Full node ademi merkeziyetçiliğini daha da zayıflatır, çünkü Miner en azından geçici olarak gelen bloklara güvenmeye başvurur. Ayrıca, ağın bilgi işlem gücünün bir kısmı potansiyel olarak en güçlü ve geçerli zincir üzerine inşa edilmek yerine geçersiz bir Blockchain üzerine inşa edildiği için güvenliğe de bir dereceye kadar zarar verir.


İkinci madde Miner ademi merkeziyetçiliği üzerinde olumsuz bir etkiye sahiptir, çünkü genellikle en iyi ağ bağlantısına ve bant genişliğine sahip havuzlar aynı zamanda en büyük olanlardır ve madencilerin birkaç büyük havuza yönelmesine neden olur.


#### Yatay ölçeklendirme



Yatay ölçeklendirme, iş yükünü birden fazla makineye bölen teknikleri ifade eder. Bu, popüler web siteleri ve veritabanları arasında yaygın bir ölçeklendirme yaklaşımı olsa da, Bitcoin'da kolayca yapılamaz.


Birçok kişi bu Bitcoin ölçeklendirme yaklaşımını *sharding* olarak adlandırmaktadır. Temel olarak, her bir Full node'in Blockchain'in sadece bir kısmını doğrulamasına izin vermekten ibarettir. Peter Todd sharding kavramı üzerine çok kafa yormuştur. Sharding'i genel hatlarıyla açıklayan bir [blog yazısı] (https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) yazmış ve ayrıca *treechains* adlı kendi fikrini sunmuştur. Makale zor bir okuma, ancak Todd oldukça sindirilebilir bazı noktalara değiniyor:


> Parçalanmış sistemlerde "Full node savunması" en azından doğrudan çalışmaz. Bütün mesele, herkesin tüm verilere sahip olmamasıdır, bu nedenle mevcut olmadığında ne olacağına karar vermeniz gerekir.

Ardından sharding ya da yatay ölçeklendirmenin nasıl ele alınacağına dair çeşitli fikirler sunuyor. Yazının sonuna doğru şu sonuca varıyor:


> Yine de büyük bir sorun var: kutsal !@#$ Bitcoin ile karşılaştırıldığında yukarıdaki karmaşık! Sharding'in "çocuksu" versiyonu bile - zk-SNARKS yerine benim doğrusallaştırma şemam - muhtemelen şu anda Bitcoin protokolünü kullanmaktan bir veya iki kat daha karmaşıktır, ancak şu anda bu alandaki şirketlerin büyük bir kısmı ellerini kaldırmış ve bunun yerine merkezi API sağlayıcılarını kullanmış gibi görünüyor. Yukarıdakileri gerçekten uygulamak ve son kullanıcıların eline ulaştırmak kolay olmayacaktır.
>

> Öte yandan, merkeziyetsizleştirme ucuz değildir: PayPal'ı kullanmak Bitcoin protokolünden bir ya da iki kat daha basittir.

Vardığı sonuç, sharding'in teknik olarak mümkün olabileceği, ancak bunun muazzam bir karmaşıklığa mal olacağıdır. Birçok kullanıcının Bitcoin'yi zaten çok karmaşık bulduğu ve bunun yerine merkezi hizmetleri kullanmayı tercih ettiği göz önüne alındığında, onları daha da karmaşık bir şey kullanmaya ikna etmek Hard olacaktır.


#### İçe doğru ölçeklendirme



Yatay ve dikey ölçeklendirme, veritabanları ve web sunucuları gibi merkezi sistemlerde tarihsel olarak iyi sonuç vermiş olsa da, merkezileştirici etkileri nedeniyle Bitcoin gibi merkezi olmayan bir ağ için uygun görünmemektedir.


Çok az takdir gören bir yaklaşım da *içsel ölçeklendirme* olarak adlandırabileceğimiz ve "daha azıyla daha fazlasını yapmak" anlamına gelen yaklaşımdır. Bu, sistemin mevcut sınırları dahilinde daha fazlasını yapabilmemiz için halihazırda mevcut olan algoritmaları optimize etmek üzere birçok geliştirici tarafından sürekli olarak yapılan çalışmaları ifade eder.


İçe doğru ölçeklendirme yoluyla elde edilen gelişmeler en hafif tabirle etkileyicidir. Yıllar içindeki gelişmeler hakkında genel bir fikir vermek için Jameson Lopp [Blockchain senkronizasyonu üzerinde benchmark testleri yaptı](https://blog.lopp.net/Bitcoin-core-performance-evolution/) ve Bitcoin core'in 0.8 sürümüne kadar birçok farklı sürümünü karşılaştırdı.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Bitcoin core'ün çeşitli sürümlerinin ilk blok indirme performansı. Y ekseninde senkronize edilen blok yüksekliği, X ekseninde ise bu yüksekliğe senkronize etmek için geçen süre yer almaktadır


Farklı çizgiler Bitcoin core'ün farklı sürümlerini temsil etmektedir. En soldaki çizgi en son sürümdür, yani Eylül 2021'de yayınlanan ve tamamen senkronize olması 396 dakika süren 0.22 sürümüdür. En sağdaki ise Kasım 2013'te yayınlanan ve 3452 dakika süren 0.8 sürümüdür. Tüm bu - kabaca 10 kat - iyileşme içe doğru ölçeklendirmeden kaynaklanmaktadır.


İyileştirmeler ya alan tasarrufu (RAM, disk, bant genişliği, vb.) ya da hesaplama gücü tasarrufu olarak kategorize edilebilir. Her iki kategori de yukarıdaki diyagramdaki iyileştirmelere katkıda bulunur.


Hesaplamalı iyileştirmenin iyi bir örneği, diğer şeylerin yanı sıra dijital imzaları yapmak ve doğrulamak için gereken kriptografik ilkelleri uygulayan [libsecp256k1](https://github.com/Bitcoin-core/secp256k1) kütüphanesinde bulunabilir. Pieter Wuille bu kütüphaneye katkıda bulunanlardan biridir ve çeşitli çekme istekleri yoluyla elde edilen performans iyileştirmelerini sergileyen bir [Twitter başlığı](https://twitter.com/pwuille/status/1450471673321381896) yazmıştır.


![](assets/libsecp256k1speedups.webp)


Zaman çizelgesinde işaretlenmiş önemli çekme istekleri ile zaman içinde imza doğrulama performansı


Grafik, ARM ve x86 olmak üzere iki farklı 64-bit CPU türü için eğilimi göstermektedir. Performanstaki fark, daha az ve daha genel talimatlara sahip olan ARM mimarisine kıyasla x86'da bulunan daha özel talimatlardan kaynaklanmaktadır. Ancak genel eğilim her iki mimari için de aynıdır. Y ekseninin logaritmik olduğuna dikkat edin, bu da iyileştirmelerin gerçekte olduğundan daha az etkileyici görünmesini sağlar.


Ayrıca, performans artışına katkıda bulunan ve yerden tasarruf sağlayan iyileştirmelere ilişkin birkaç iyi örnek de bulunmaktadır. Bir

gW-588'in alan tasarrufuna katkısı hakkında [Medium blog yazısı] (https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3), kullanıcı Murch, Taproot'i çeşitli şekillerde kullanarak ve hiç kullanmayarak 3'te 2 eşik imzasının ne kadar blok alanı gerektireceğini karşılaştırıyor.


![](assets/murch-taproot.webp)


Farklı harcama türleri, Taproot ve eski sürümler için alan tasarrufu.


Yerel SegWit kullanan 3'te 2 Multisig toplam 104,5+43 vB = 147,5 vB gerektirirken, Taproot'in en az yer kaplayan kullanımı standart kullanım durumunda yalnızca 57,5+43 vB = 100,5 vB gerektirecektir. En kötü ve nadir durumlarda, örneğin standart bir imzalayıcının herhangi bir nedenle mevcut olmadığı durumlarda, Taproot 107,5+43 vB = 150,5 vB kullanacaktır. Tüm ayrıntıları anlamak zorunda değilsiniz, ancak bu size geliştiricilerin yerden tasarruf etme konusunda nasıl düşündükleri hakkında bir fikir vermelidir - her küçük bayt önemlidir.


Bitcoin yazılımında içe doğru ölçeklendirmenin yanı sıra, kullanıcıların da içe doğru ölçeklendirmeye katkıda bulunabilecekleri bazı yollar vardır. İşlem ücretlerinden tasarruf etmek ve aynı zamanda Full node gereksinimleri üzerindeki ayak izlerini azaltmak için işlemlerini daha akıllıca yapabilirler. Bu amaca yönelik yaygın olarak kullanılan iki teknik işlem gruplama ve çıktı birleştirme olarak adlandırılır.


İşlem gruplama ile amaçlanan, her ödeme için tek bir işlem yapmak yerine birden fazla ödemeyi tek bir işlemde birleştirmektir. Bu size çok fazla ücret tasarrufu sağlayabilir ve aynı zamanda blok alanı yükünü azaltabilir.


![](assets/tx-batching.webp)


İşlem gruplama, ücretlerden tasarruf etmek için birden fazla ödemeyi tek bir işlemde birleştirir.


Çıktı birleştirme, birden fazla çıktıyı tek bir çıktıda birleştirmek için blok alanı talebinin düşük olduğu dönemlerden yararlanmayı ifade eder. Bu, daha sonra blok alanı talebi yüksekken ödeme yapmanız gerektiğinde ücret maliyetinizi azaltabilir.


![](assets/utxo-consolidation.webp)


Çıktı konsolidasyonu: Daha sonra ücretlerden tasarruf etmek için ücretler düşükken madeni paralarınızı tek bir büyük Coin'te eritin.


Çıktı konsolidasyonunun içe doğru ölçeklendirmeye nasıl katkıda bulunduğu açık olmayabilir. Sonuçta, Blockchain verilerinin toplam miktarı bu yöntemle biraz daha artmaktadır. Bununla birlikte, UTXO seti, yani kimin hangi coin'e sahip olduğunu takip eden veritabanı küçülür çünkü yarattığınızdan daha fazla UTXO harcarsınız. Bu da tam düğümlerin UTXO setlerini muhafaza etme yükünü hafifletir.


Ancak ne yazık ki, bu iki *UTXO yönetimi* tekniği sizin veya alacaklılarınızın gizliliği için kötü olabilir. Gruplama durumunda, her alacaklı gruplanmış tüm çıktıların sizden diğer alacaklılara olduğunu bilecektir (muhtemelen değişiklik hariç). UTXO konsolidasyonu durumunda, konsolide ettiğiniz çıktıların aynı Wallet'e ait olduğunu ortaya çıkaracaksınız. Dolayısıyla maliyet verimliliği ile gizlilik arasında bir denge kurmanız gerekebilir.


#### Katmanlı ölçeklendirme



Ölçeklendirmeye yönelik en etkili yaklaşım muhtemelen katmanlamadır. Katmanlamanın arkasındaki genel fikir, bir protokolün Blockchain'e işlem eklemeden kullanıcılar arasındaki ödemeleri gerçekleştirebilmesidir.


Katmanlı bir protokol, aşağıdaki şekilde gösterildiği gibi, iki veya daha fazla kişinin Blockchain'e yerleştirilen bir başlangıç işlemi üzerinde anlaşmasıyla başlar.


![](assets/scaling-layer.webp)

Bitcoin, Layer 1'in üzerinde tipik bir Layer 2 protokolü.


Bu başlangıç işleminin nasıl oluşturulduğu protokoller arasında farklılık gösterir, ancak ortak bir tema, katılımcıların imzasız bir başlangıç işlemi ve başlangıç işleminin çıktısını çeşitli şekillerde harcayan önceden imzalanmış bir dizi ceza işlemi oluşturmasıdır. Daha sonra, başlangıç işlemi tamamen imzalanır ve Blockchain'te yayınlanır ve ceza işlemleri tamamen imzalanabilir ve yanlış davranan bir tarafı cezalandırmak için yayınlanabilir. Bu, katılımcıları sözlerini tutmaya teşvik eder, böylece protokol bir Trustless şekilde çalışabilir.


Başlangıç işlemi Blockchain'da gerçekleştiğinde, protokol yapması gerekenleri yapabilir. Örneğin, katılımcılar arasında süper hızlı ödemeler yapabilir, bazı gizlilik artırıcı teknikler uygulayabilir veya Bitcoin Blockchain tarafından desteklenmeyecek daha gelişmiş komut dosyası yazabilir.


Belirli protokollerin nasıl çalıştığını detaylandırmayacağız, ancak önceki şekilde görebileceğiniz gibi, Blockchain protokolün yaşam döngüsü boyunca nadiren kullanılır. Tüm ilgi çekici eylem *off-chain* ile gerçekleşir. Bunun doğru yapıldığında gizlilik için nasıl bir kazanım olabileceğini gördük, ancak ölçeklenebilirlik için de bir avantaj olabilir.


Gregory Maxwell, "Aya yolculuk için birden fazla aşamalı bir roket gerekir, aksi takdirde roket denklemi öğle yemeğinizi yer... herkesi palyaço arabası tarzında bir trebuchet'e paketlemek ve başarı ummak doğru değil." başlıklı bir [Reddit gönderisinde] (https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/), Bitcoin'u büyüklük sırasına göre ölçeklendirmek için neden katmanlamanın en iyi şansımız olduğunu açıklıyor.


Visa veya Mastercard'ı Bitcoin'in ana rakipleri olarak görmenin yanlışlığını vurgulayarak ve maksimum blok boyutunu artırmanın söz konusu rekabeti karşılamak için nasıl kötü bir yaklaşım olduğunu vurgulayarak başlıyor. Ardından katmanları kullanarak nasıl gerçek bir fark yaratılabileceğinden bahsediyor:


> Peki bu, Bitcoin'nin bir ödeme teknolojisi olarak büyük bir kazanan olamayacağı anlamına mı geliyor? Hayır. Ancak dünyanın ödeme ihtiyaçlarını karşılamak için gereken kapasiteye ulaşmak için daha akıllıca çalışmalıyız.
>

> Bitcoin en başından beri akıllı sözleşme özelliği sayesinde katmanları güvenli bir şekilde bir araya getirecek şekilde tasarlanmıştır (Ne yani, bunun sadece insanlar anlamsız "DAO'lar" hakkında felsefe yapabilsinler diye mi konulduğunu düşünüyorsunuz?) Aslında Bitcoin sistemini son derece erişilebilir ve mükemmel derecede güvenilir bir robot yargıç olarak kullanacağız ve işlerimizin çoğunu mahkeme salonunun dışında yürüteceğiz - ancak öyle bir şekilde işlem yapacağız ki bir şeyler ters giderse tüm kanıtlara ve yerleşik anlaşmalara sahip olacağız, böylece robot mahkemenin bunu düzelteceğinden emin olabiliriz. (Geek kenar çubuğu: Eğer bu imkansız görünüyorsa, işlemlerin kesilmesi hakkındaki bu eski yazıyı okuyun)
>

> Bu tam olarak Bitcoin'ün temel özellikleri nedeniyle mümkündür. Sansürlenebilir veya tersine çevrilebilir bir temel sistem, üzerine güçlü bir üst Layer işlem süreci inşa etmek için pek uygun değildir... ve eğer temel varlık sağlam değilse, onunla işlem yapmanın pek bir anlamı yoktur.

Yargıç benzetmesi, katmanların nasıl işlediğini oldukça açıklayıcıdır: bu yargıç bozulamaz olmalı ve fikrini asla değiştirmemelidir, aksi takdirde Bitcoin'nın temeli olan Layer'nin üzerindeki katmanlar güvenilir bir şekilde çalışmayacaktır.


Merkezi hizmetler hakkında bir noktaya değinerek devam ediyor. İşleri halletmek için önemsiz miktarda Bitcoin'e sahip merkezi bir sunucuya güvenmekte genellikle bir sorun yoktur: bu da katmanlı ölçeklendirmedir.


Maxwell'in yukarıdaki yazıyı yazmasının üzerinden uzun yıllar geçti ve söyledikleri hala doğru. Lightning Network'un başarısı, katmanlamanın Bitcoin'nin faydasını artırmak için gerçekten de ileriye dönük bir yol olduğunu kanıtlıyor.



### Ölçeklendirme Hakkında Sonuç



Bitcoin'i ölçeklendirmenin, Bitcoin'in kullanım kapasitesini artırmanın çeşitli yollarını tartıştık. Ölçeklendirme, Bitcoin'in ilk günlerinden beri bir endişe kaynağı olmuştur.


Bugün Bitcoin'nin dikey olarak ("daha büyük donanım satın alın") veya yatay olarak ("verilerin yalnızca bir kısmını doğrulayın") değil, daha ziyade içe doğru ("daha azıyla daha fazlasını yapın") ve katmanlar halinde ("Bitcoin'nin üzerine protokoller oluşturun") iyi ölçeklendiğini biliyoruz.


## İşler sarpa sardığında

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin insanlar tarafından inşa edilmiştir. İnsanlar yazılımı yazıyor ve daha sonra insanlar bu yazılımı çalıştırıyor. Bir güvenlik açığı ya da ciddi bir hata keşfedildiğinde - ikisi arasında gerçekten bir ayrım var mı? - her zaman insanlar tarafından keşfedilir, etten ve kemikten. Bu bölüm, ortalık karıştığında insanların ne yapması, ne yapması ve ne yapmaması gerektiğini ele almaktadır. İlk bölümde *sorumlu ifşa* terimi açıklanmaktadır; bu terim, bir güvenlik açığını keşfeden birinin bundan kaynaklanan zararı en aza indirmeye yardımcı olmak için nasıl sorumlu davranabileceğini ifade eder. Bölümün geri kalanında, yıllar içinde keşfedilen en ciddi güvenlik açıklarından bazıları ve bunların geliştiriciler, madenciler ve kullanıcılar tarafından nasıl ele alındığına dair bir tura çıkacaksınız. Bitcoin'ün ilk zamanlarında işler bugün olduğu kadar titiz değildi.


### Sorumlu açıklama



Bitcoin core'te bir hata keşfettiğinizi düşünün; bu hata, herhangi birinin özel olarak hazırlanmış bazı ağ mesajlarını kullanarak bir Bitcoin core düğümünü uzaktan kapatmasına olanak tanıyor. Ayrıca kötü niyetli olmadığınızı ve bu sorunun istismar edilmeden kalmasını istediğinizi düşünün. Ne yaparsınız? Bu konuda sessiz kalırsanız, muhtemelen başka biri sorunu keşfedecektir ve bu kişinin kötü niyetli olmayacağından emin olamazsınız.


Bir güvenlik sorunu keşfedildiğinde, bunu keşfeden kişi Bitcoin geliştiricileri arasında sıklıkla kullanılan bir terim olan _responsible disclosure_ terimini kullanmalıdır. Bu terim [Wikipedia'da açıklanmıştır] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Donanım ve yazılım geliştiricileri genellikle hatalarını onarmak için zamana ve kaynaklara ihtiyaç duyarlar. Çoğu zaman, bu hataları bulanlar etik bilgisayar korsanlarıdır
güvenlik açıkları. Hackerlar ve bilgisayar güvenlik bilimcileri, kamuoyunu güvenlik açıklarından haberdar etmenin sosyal sorumlulukları olduğu görüşündedir. Sorunları gizlemek yanlış bir güvenlik hissine neden olabilir. Bundan kaçınmak için, ilgili taraflar koordine olur ve güvenlik açığının onarılması için makul bir süre üzerinde müzakere ederler. Güvenlik açığının potansiyel etkisine, acil durum düzeltmesi veya geçici çözümün geliştirilmesi ve uygulanması için gereken süreye ve diğer faktörlere bağlı olarak bu süre birkaç gün ile birkaç ay arasında değişebilir.


Bu, bir güvenlik sorunu bulmanız halinde bunu sistemden sorumlu ekibe bildirmeniz gerektiği anlamına gelir. Peki bu Bitcoin bağlamında ne anlama geliyor? Bitcoin'yi kimse kontrol etmiyor, ancak şu anda Bitcoin'nin geliştirilmesi için bir odak noktası var, yani [Bitcoin core Github deposu] (https://github.com/Bitcoin/Bitcoin). Söz konusu deponun sorumluları depodaki koddan sorumludur, ancak bir bütün olarak sistemden sorumlu değildirler - kimse sorumlu değildir. Bununla birlikte, genel olarak en iyi uygulama security@bitcoincore.org adresine bir e-posta göndermektir.


Anthony Towns, 2017 tarihli "Hataların sorumlu bir şekilde ifşa edilmesi" başlıklı bir [e-posta dizisi] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) yazısında, mevcut en iyi uygulamalar olarak algıladıklarını özetlemeye çalışmıştır. Konuyla ilgili görüşünü bildirmek için çeşitli kaynaklardan ve farklı kişilerden girdiler toplamıştı.




- Güvenlik açıkları bitcoincore.org adresindeki security üzerinden bildirilmelidir
- Kritik bir sorun (hemen istismar edilebilecek veya halihazırda istismar edilmekte olan ve büyük zarara yol açan) şu şekilde ele alınacaktır:
  - en kısa sürede yayınlanmış bir yama
  - yükseltme (veya etkilenen sistemleri devre dışı bırakma) ihtiyacına ilişkin geniş bildirim
  - saldırıları geciktirmek için asıl sorunun asgari düzeyde açıklanması
- Kritik olmayan bir güvenlik açığı (istismar edilmesi zor veya pahalı olduğu için) şu şekilde ele alınacaktır:
  - olağan gelişim akışı içinde gerçekleştirilen yama ve inceleme
  - bir düzeltmenin veya geçici çözümün ana sürümden mevcut yayınlanan sürüme geri aktarılması
- Geliştiriciler, önerilen düzeltmeyi güvenlik açığından haberdar olmayan deneyimli geliştiricilere sunarak, onlara bir güvenlik açığını düzelttiğini söyleyerek ve güvenlik açığını tanımlamalarını isteyerek düzeltmenin yayınlanmasının güvenlik açığının doğasını ortaya çıkarmamasını sağlamaya çalışacaktır.
- Geliştiriciler, güvenlik açığını ortaya çıkarmadan yapabiliyorlarsa, düzeltme yayınlanmadan ve yaygın olarak dağıtılmadan önce diğer Bitcoin uygulamalarının güvenlik açığı düzeltmelerini benimsemelerini önerebilir; örneğin, düzeltmenin dahil edilmesini haklı çıkaracak önemli performans faydaları varsa.
- Bir güvenlik açığı kamuya açıklanmadan önce, geliştiriciler genellikle dost Altcoin geliştiricilerine düzeltmeleri yakalamalarını önerecektir. Ancak bu, düzeltmeler Bitcoin ağında geniş çapta dağıtıldıktan sonradır.
- Geliştiriciler genellikle düşmanca davranan (örneğin, başkalarına saldırmak için güvenlik açıklarını kullanan veya ambargoları ihlal eden) Altcoin geliştiricilerini bilgilendirmeyecektir.
- Bitcoin geliştiricileri, Bitcoin düğümlerinin >%80'i düzeltmeleri dağıtana kadar güvenlik açığı ayrıntılarını açıklamayacaktır. Güvenlik açığı keşfedenlerin aynı politikayı izlemesi teşvik edilir ve talep edilir. [1] [6]


Bu liste, Bitcoin için yama yayınlarken ne kadar dikkatli olunması gerektiğini göstermektedir, çünkü yamanın kendisi güvenlik açığını ele verebilir. Dördüncü madde, bir yamanın yeterince iyi gizlenip gizlenmediğinin nasıl test edileceğini açıkladığı için özellikle ilginçtir. Gerçekten de, birkaç deneyimli geliştirici yamanın bir güvenlik açığını düzelttiğini bilse bile bu açığı fark edemiyorsa, diğerlerinin bunu keşfetmesi muhtemelen gerçekten Hard olacaktır.


Bu e-postaya yol açan konu başlığı, altcoinlere ve Bitcoin'nın diğer uygulamalarına yönelik güvenlik açıklarının ifşa edilip edilmeyeceğini, ne zaman ve nasıl ifşa edileceğini tartışıyordu. Burada net bir cevap yok. "İyi adamlara yardım etmek" yapılması gereken mantıklı bir şey gibi görünüyor, ancak bunların kim olduğuna kim karar veriyor ve sınır nerede çiziliyor? Bryan Bishop, altcoinlerin ve hatta scamcoinlerin güvenlik açıklarına karşı kendilerini savunmalarına yardımcı olmanın ahlaki bir görev olduğunu [savundu] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html):


> Bitcoin'yi ve kullanıcılarını aktif tehditlerden korumak yeterli değildir, her türlü kullanıcıyı ve farklı yazılımı her türlü tehditten korumak için daha genel bir sorumluluk vardır, insanlar kişisel olarak bakımını yapmadığınız, katkıda bulunmadığınız veya savunmadığınız aptalca ve güvensiz yazılımlar kullanıyor olsalar bile. Bir güvenlik açığı bilgisini ele almak hassas bir konudur ve başlangıçta tanımlanandan daha ciddi doğrudan veya dolaylı etkiye sahip bir bilgi alıyor olabilirsiniz.

Ayrıca Town'ın yukarıdaki e-postasına öncülük eden Gregory Maxwell'in güvenlik açıklarının göründüğünden daha ciddi olabileceğini savunduğu bir [gönderi] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) vardı:


> Birçok kez Hard'un istismar edilmesi gereken bir sorunun doğru hileyi bulduğunuzda önemsiz hale geldiğini veya küçük bir dos sorununun çok daha ciddi hale geldiğini gördüm.
>

> Ustalıkla kullanılan basit performans hataları, potansiyel olarak ağı bölmek için kullanılabilir - Miner A ve Exchange B bir bölüme, diğer herkes başka bir bölüme gider ve iki katına çıkar.
>

> Ve bunun gibi.  Dolayısıyla, farklı şeylerin farklı şekilde ele alınması gerektiği ve alınabileceği konusunda kesinlikle hemfikir olsam da, bu her zaman bu kadar net değildir. Olayları bildiğinizden daha ciddi olarak ele almak akıllıca olacaktır.

Bu nedenle, bir güvenlik açığından yararlanmak Hard gibi görünse bile, bunun kolayca istismar edilebileceğini ve sadece nasıl yapılacağını henüz bulamadığınızı varsaymak en iyisi olabilir.


Ayrıca "bu başlığa ifşa ile ilgili bir şey demek biraz yanlış, bu başlık ifşa ile ilgili değil. İfşa, satıcıya söylediğiniz zamandır.  Bu konu başlığı yayınlama ile ilgili ve bunun çok farklı sonuçları var. Yayınlama, olası saldırganlara söylediğinizden emin olduğunuz zamandır". İfşa ve yayın arasındaki ayrıma ilişkin bu son gözlem önemli bir gözlemdir. İşin kolay kısmı sorumlu ifşadır; Hard kısmı ise mantıklı yayınlamadır.


### Bitcoin'ün Travmatik Çocukluğu



Bitcoin tek kişilik bir proje olarak başladı (en azından yaratıcısının takma adı bunu gösteriyor) ve Bitcoin'in başlangıçta çok az değeri vardı ya da hiç yoktu. Bu nedenle, güvenlik açıkları ve hata düzeltmeleri bugün olduğu kadar titizlikle ele alınmıyordu.


Bitcoin wiki'de Bitcoin'nın geçirdiği [yaygın güvenlik açıkları ve maruziyetler listesi] (https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE'ler) bulunmaktadır. Bu bölüm, Bitcoin'nın ilk yıllarındaki bazı güvenlik sorunlarının ve olaylarının küçük bir açıklamasını oluşturmaktadır. Hepsini ele almayacağız, ancak özellikle ilginç bulduğumuz birkaç tanesini seçtik.


#### 2010-07-28: Herkesin parasını harca (CVE-2010-5141)



28 Temmuz 2010'da ArtForz adında takma isimli bir kişi 0.3.4 sürümünde herhangi birinin başka birinden coin almasına izin veren bir hata keşfetti. ArtForz *sorumlu bir şekilde* bunu Satoshi Nakamoto'ya ve Gavin Andresen adlı başka bir Bitcoin geliştiricisine bildirdi.


Sorun, `OP_RETURN` kod operatörünün program yürütmesinden çıkmasıydı, bu nedenle scriptPubKey `<pubkey> OP_CHECKSIG` ve scriptSig `OP_1 OP_RETURN` ise, programın scriptPubKey içindeki kısmı asla yürütülmeyecekti. Olacak tek şey `1` değerinin yığına konması ve ardından `OP_RETURN` değerinin programdan çıkmasına neden olmasıdır. Program çalıştıktan sonra yığının tepesinde sıfır olmayan herhangi bir değer olması, harcama koşulunun yerine getirildiği anlamına gelir. Yığının en üstündeki `1` değeri sıfır olmadığından, harcama tamamlanmış olur.


Bu, `OP_RETURN`nin işlenmesine yönelik koddu:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

Pc = pend;` komutunun etkisi, programın geri kalanının atlanması, yani scriptPubKey içindeki herhangi bir kilitleme komut dosyasının göz ardı edilmesiydi. Düzeltme, `OP_RETURN` ifadesinin anlamını, bunun yerine hemen başarısız olacak şekilde değiştirmekten ibaretti.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi bu değişikliği yerel olarak yaptı ve ondan 0.3.5 sürümlü çalıştırılabilir bir ikili oluşturdu. Ardından Bitcointalk forumunda `\\*** ALERT \*** ASAP 0.3.5'e yükseltin` yazarak, kullanıcıları kaynak kodunu sunmadan bu ikili sürümünü yüklemeye çağırdı:


> Lütfen en kısa sürede 0.3.5 sürümüne yükseltin!  Sahte işlemlerin kabul edilmesinin mümkün olduğu bir uygulama hatasını düzelttik.  Sürüm 0.3.5'e yükseltene kadar Bitcoin işlemlerini ödeme olarak kabul etmeyin!

Orijinal mesaj daha sonra düzenlenmiştir ve artık tam haliyle mevcut değildir. Yukarıdaki pasaj bir [alıntı cevaptan] (https://bitcointalk.org/index.php?topic=626.msg6458#msg6458) alınmıştır. Bazı kullanıcılar Satoshi'ün ikili dosyasını denemiş, ancak sorunlarla karşılaşmışlardır. Kısa bir süre sonra, [Satoshi yazdı](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> SVN'yi güncellemek için henüz zamanım olmadı.  0.3.6'yı bekleyin, şu anda onu oluşturuyorum.  Bu arada düğümünüzü kapatabilirsiniz.

Ve 35 dakika sonra [şöyle yazdı] (https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN 0.3.6 sürümü ile güncellenmiştir.
>

> Şimdi 0.3.6'nın Windows derlemesini Sourceforge'a yüklüyorum, ardından linux'u yeniden oluşturacağım.

Bu noktada, orijinal gönderiyi 0.3.5 yerine 0.3.6'dan bahsedecek şekilde güncellemiş gibi görünüyordu:


> Lütfen en kısa sürede 0.3.6 sürümüne yükseltin!  Sahte işlemlerin kabul edilmiş gibi gösterilebildiği bir uygulama hatasını düzelttik.  Sürüm 0.3.6'ya yükseltene kadar Bitcoin işlemlerini ödeme olarak kabul etmeyin!
>

> Eğer 0.3.6'ya hemen geçemiyorsanız, geçene kadar Bitcoin düğümünüzü kapatmanız en iyisidir.
>

> Ayrıca 0.3.6'da daha hızlı hashing:
> - tcatm sayesinde midstate önbellek optimizasyonu
> - BlackEye sayesinde Crypto++ ASM SHA-256
> Toplam üretim hızı 2,4 kat daha hızlı.
>

> İndirin:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Windows ve Linux kullanıcıları: 0.3.5 aldıysanız hala 0.3.6'ya yükseltmeniz gerekiyor.

İlk mesajdaki sorunun nitelendirilmesindeki farka dikkat edin: "kabul edilmiş olarak gösterilebilir" vs "kabul edilebilir". Belki de Satoshi, asıl soruna çok fazla dikkat çekmemek için iletişiminde hatanın ciddiyetini küçümsemiştir. Her neyse, insanlar 0.3.6'ya yükseltti ve beklendiği gibi çalıştı. Bu özel sorun, şaşırtıcı bir şekilde, Bitcoin kaybı olmadan çözüldü.


Satoshi'ın mesajı ayrıca Mining için bazı performans optimizasyonlarını da açıklıyordu. Bunun neden kritik bir güvenlik düzeltmesine dahil edildiği belirsizdir, amacın gerçek sorunu gizlemek olması mümkündür. Ancak, Subversion deposunun geliştirme dalının başında ne varsa, ona eklenen güvenlik düzeltmesiyle birlikte yayınlamış olması daha olası görünüyor.


O zamanlar bugünkü kadar çok kullanıcı yoktu ve Bitcoin'nin değeri sıfıra yakındı. Bu hata müdahalesi bugün yapılsaydı, birçok nedenden dolayı tam bir saçmalık olarak değerlendirilirdi:



- Satoshi, düzeltmeyi içeren 0.3.5'in yalnızca ikili sürümünü yaptı. Belki de sorunu gizlemek için bir önlem olarak hiçbir yama veya kod sağlanmadı.
- 0.3,5 [çalışmadı bile] (https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- 0.3.6'daki düzeltme aslında bir Hard Fork idi.


Bir başka tartışmalı konu da kullanıcılardan düğümlerini kapatmalarının istenmesinin iyi mi kötü mü olduğudur. Bu bugün yapılamazdı, ancak o zamanlar pek çok kullanıcı güncellemeler için forumları aktif olarak takip ediyordu ve genellikle her şeyden haberdardı. Bunu yapmanın mümkün olduğu düşünüldüğünde, yapılması mantıklı bir şey olabilirdi.


#### 2010-08-15 Birleşik çıktı taşması (CVE-2010-5139)



Ağustos 2010 ortasında, Bitcointalk forum kullanıcısı jgarzik, nam-ı diğer Jeff Garzik,

(https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) 74638 blok yüksekliğindeki belirli bir işlemin alışılmadık derecede yüksek değere sahip iki çıktısı olduğunu [keşfetti]:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> Bu blok #74638'deki "değer çıkışı" oldukça gariptir:
>

> 92233720368.54277039 BTC?  Acaba bu UINT64_MAX mı?

Muhtemelen, iki int64 (Garzik'in sandığı gibi uint64 değil) çıktısının toplamının negatif bir değere -0,00997538 BTC'ye taşmasına neden olan bir hata vardı. Girdilerin toplamı ne olursa olsun, çıktıların "toplamı" daha küçük olacak ve o zamanki koda göre bu işlem tamam olacaktı.


Bu durumda, hata gerçek bir istismar yoluyla ifşa edilmiş ve yayınlanmıştır. Bunun talihsiz bir sonucu olarak yaklaşık 2x92 milyar Bitcoin yaratılmış ve bu da o sırada var olan yaklaşık 3,7 milyon coin'lik Supply parasını ciddi şekilde seyreltmiştir.


İlgili bir başlıkta, [Satoshi](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531) insanlar Mining'i (ya da o zamanki adıyla *üretmeyi*) durdurursa memnun olacağını belirtmiştir:


> İnsanlar üretmeyi bırakırsa yardımcı olur.  Muhtemelen mevcut dalın etrafında bir dalı yeniden yapmamız gerekecek ve ne kadar az generate yaparsanız bu o kadar hızlı olacaktır.
>

> İlk yama SVN rev 132'de olacak.  Henüz yüklenmedi.  Önce diğer bazı değişiklikleri aradan çıkarıyorum, sonra bunun için yamayı yükleyeceğim.

Planı, burada tartışılan gibi işlemleri geçersiz kılmak için bir Soft Fork yapmak ve böylece bu tür işlemleri içeren blokları (özellikle 74638 bloğu) geçersiz kılmaktı. Bir saatten kısa bir süre sonra, Subversion deposunun 132 numaralı revizyonuna bir [yama](https://sourceforge.net/p/Bitcoin/code/132/) işledi ve kullanıcıların ne yapması gerektiğini düşündüğünü açıklayan [foruma gönderdi](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548):


> Yama SVN rev 132'ye yüklendi!
>

> Şimdilik önerilen adımlar:
> 1) Kapatın.
> 2) knightmb'nin blk dosyalarını indirin.  (blk0001.dat ve blkindex.dat dosyalarınızı değiştirin)
> 3) Yükseltme.
> 4) 74000'den az blok ile başlamalıdır. Geri kalanını yeniden indirmesine izin verin.
>

> Knightmb'nin dosyalarını kullanmak istemiyorsanız, blk*.dat dosyalarınızı silebilirsiniz, ancak herkes tüm blok dizinini bir kerede indiriyorsa ağ üzerinde çok fazla yük olacaktır.
>

> Kısa süre içinde sürümleri oluşturacağım.

İnsanların belirli bir kullanıcıdan, yani Blockchain'sini diskinde göründüğü gibi yayınlayan knightmb'den blok verilerini, blkXXXX.dat ve blkindex.dat dosyalarını indirmelerini istedi. Blockchain verilerini sıfırdan senkronize etmek yerine bu şekilde indirmenin nedeni, ağ bant genişliği darboğazlarını azaltmaktı.


Bununla ilgili büyük bir uyarı vardı: kullanıcıların knightmb'den indireceği veriler başlangıçta Bitcoin yazılımı tarafından doğrulanmıyordu](https://Bitcoin.stackexchange.com/a/113682/69518). Blkindex.dat dosyası UTXO setini içeriyordu ve yazılım buradaki herhangi bir veriyi zaten doğrulamış gibi kabul ediyordu. knightmb kendisine ya da bir başkasına biraz bitcoin vermek için verileri manipüle edebilirdi.


Yine, insanlar bunu kabul etmiş gibi görünüyordu ve geçersiz bloğun ve ardıllarının tersine çevrilmesi başarılı oldu. Madenciler [74637] (https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) bloğunun yeni bir ardılı üzerinde çalışmaya başladı ve bloğun Timestamp'ine göre, sorunun keşfedilmesinden yaklaşık 6 saat sonra, 23:53 UTC'de bir ardıl ortaya çıktı. Ertesi gün 08:10'da, 16 Ağustos'ta, 74689 numaralı blok civarında, yeni zincir eski zinciri geride bıraktı, bu nedenle yükseltilmemiş tüm düğümler yeni zinciri takip etmek için yeniden birleşti. Bu, Bitcoin'nın tarihindeki en derin yeniden düzenleme - 52 blok - oldu.


OP_RETURN sorunu ile karşılaştırıldığında, bu sorun biraz daha temiz bir şekilde ele alınmıştır:


- Yalnızca ikili yama sürümü yok
- Yayınlanan yazılım amaçlandığı gibi çalıştı
- Hayır Hard Fork


Kullanıcılardan bu sorun sırasında Mining'i de durdurmaları istendi. Bunun iyi bir fikir olup olmadığını tartışabiliriz, ancak bir Miner olduğunuzu ve kötü bloğun üstündeki tüm blokların eninde sonunda derin bir yeniden düzenlemede silineceğine ikna olduğunuzu hayal edin: neden Mining lanetli bloklar için kaynak harcayasınız ki?


Nakamoto'nun önerdiği gibi yapmanın ve Blockchain seti de dahil olmak üzere UTXO'ü rastgele bir adamın Hard sürücüsünden indirmenin biraz şüpheli olduğunu da düşünebilirsiniz. Eğer öyleyse, haklısınız: bu şüpheli. Ancak, koşullar göz önüne alındığında, bu acil durum tepkisi mantıklı bir tepkiydi.


Bu vaka ile önceki OP_RETURN vakası arasında önemli bir fark var: bu sorun vahşi doğada istismar edildi ve bu nedenle bir düzeltme daha kolay yapılabilirdi. OP_RETURN vakasında, düzeltmeyi gizlemek ve sorunun ne olduğunu doğrudan ortaya koymayan kamu açıklamaları yapmak zorunda kaldılar.


#### 2013-03-11 DB kilitleri sorunu 0.7.2 - 0.8.0 (CVE-2013-3220)



Mart 2013'te çok ilginç ve eğitim açısından değerli bir konu ortaya çıktı. Blockchain'nın (aşağıdaki alıntıda "Fork" kelimesi kullanılmasına rağmen) 225429 numaralı bloktan sonra ayrıldığı görülmüştür. Bu olayın ayrıntıları [BIP50'de rapor edilmiştir] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). Özet şöyle diyor:


> Daha önce görülenden daha fazla sayıda toplam işlem girdisine sahip bir blok çıkarıldı ve yayınlandı. Bitcoin 0.8 düğümleri bunu idare edebildi, ancak bazı 0.8 öncesi Bitcoin düğümleri bunu reddederek Blockchain'un beklenmedik bir Fork'sine neden oldu. Bu noktada 0.8 öncesi uyumsuz zincir (bundan sonra 0.8 zinciri) Mining Hash gücünün yaklaşık %60'ına sahipti ve bölünmenin otomatik olarak çözülmemesini sağladı (0.8 öncesi zincirin toplam işte 0.8 zincirini geçmesi ve 0.8 düğümlerini 0.8 öncesi zincire yeniden organize olmaya zorlaması durumunda meydana geleceği gibi).
>

> BTCGuild ve Slush, kanonik bir zinciri mümkün olan en kısa sürede eski haline getirmek için Bitcoin 0.8 node'larını 0.7'ye düşürdü, böylece havuzları da daha büyük bloğu reddedecekti. Bu, büyük bloğun olmadığı zincire çoğunluk hash gücünü yerleştirdi ve böylece sonunda 0.8 düğümlerinin 0.8 öncesi zincire yeniden düzenlenmesine neden oldu.

Mining havuzları BTCGuild ve Slush'ın hızlı hareket etmesi bu acil durumda çok önemliydi. Hash gücünün çoğunluğunu bölünmenin 0.8 öncesi dalına aktarmayı başardılar ve böylece fikir birliğinin yeniden sağlanmasına yardımcı oldular. Bu da geliştiricilere sürdürülebilir bir çözüm bulmaları için zaman kazandırdı.


Bu konuda çok ilginç olan şey, 0.7.2 sürümünün önceki sürümlerde de olduğu gibi kendisiyle uyumsuz olmasıdır. Bu durum [BIP50'nin kök neden bölümünde] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause) açıklanmıştır:


> Yeterince yüksek olmayan BDB kilit yapılandırması ile, dolaylı olarak blok geçerliliğini belirleyen bir ağ konsensüs kuralı haline gelmişti (her ne kadar bir
kilit kullanımı düğümden düğüme değişebileceğinden tutarsız ve güvensiz bir kuraldır).


Kısacası sorun, Bitcoin core yazılımının bir bloğu doğrulamak için ihtiyaç duyduğu veritabanı kilidi sayısının deterministik olmamasıdır. Bir düğüm X kilide ihtiyaç duyarken başka bir düğüm X+1 kilide ihtiyaç duyabilir. Düğümlerin ayrıca Bitcoin'ün kaç kilit alabileceği konusunda bir sınırı vardır. İhtiyaç duyulan kilit sayısı limiti aşarsa, blok geçersiz sayılacaktır. Dolayısıyla, X+1 sınırı aşar ancak X aşmazsa, iki düğüm Blockchain'u bölecek ve hangi dalın geçerli olduğu konusunda anlaşmazlığa düşecektir.


İki havuz tarafından uzlaşmayı yeniden tesis etmek için alınan acil önlemlerin yanı sıra seçilen çözüm şuydu



- blokları hem boyut hem de 0.8.1 sürümünde gereken kilitler açısından sınırlandırın
- eski sürümleri (0.7.2 ve bazı eski sürümler) aynı yeni kurallarla yamalayın ve küresel kilit sınırını artırın.


İkinci maddedeki artırılmış küresel kilit limiti dışında, bu kurallar önceden belirlenmiş bir süre için geçici olarak uygulanmıştır. Plan, çoğu düğüm yükseltildikten sonra bu limitleri kaldırmaktı.


Bu Soft Fork mutabakatın bozulma riskini önemli ölçüde azalttı ve birkaç ay sonra, 15 Mayıs'ta, geçici kurallar ağ genelinde uyumlu bir şekilde devre dışı bırakıldı. Bu devre dışı bırakmanın aslında bir Hard Fork olduğunu, ancak tartışmalı olmadığını unutmayın. Dahası, bir önceki Soft Fork ile birlikte yayınlanmıştı, bu nedenle Soft-çatallı yazılımı çalıştıran kişiler bunu bir Hard Fork'in takip edeceğinin farkındaydı. Bu nedenle, Hard Fork etkinleştirildiğinde düğümlerin büyük çoğunluğu fikir birliği içinde kaldı. Ancak ne yazık ki, yükseltme yapmayan birkaç düğüm bu süreçte kayboldu.


Bunun bugün yapılabilir olup olmadığı merak edilebilir. Mining ortamı bugün daha karmaşıktır ve bölünmenin her iki tarafındaki Hash gücüne bağlı olarak, BIP50'deki gibi bir yamayı yeterince hızlı bir şekilde yayınlamak Hard olabilir. "Yanlış" daldaki madencileri blok ödüllerini bırakmaya ikna etmek muhtemelen Hard olacaktır.


#### BIP66



BIP66 ilginçtir çünkü şu hususların önemini vurgulamaktadır:



- iyi seçim kriptografi
- sorumlu bi̇lgi̇lendi̇rme
- güvenlik açığını ortaya çıkarmadan dağıtım
- Doğrulanmış blokların üstünde Mining


BIP66, Bitcoin Script'teki imza kodlamalarına ilişkin kuralları sıkılaştırmaya yönelik bir öneriydi. Motivasyon] (https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation), OpenSSL ve hatta OpenSSL'in son sürümleri dışındaki yazılım veya kütüphanelerle imzaları ayrıştırabilmekti. OpenSSL, Bitcoin core'in o dönemde kullandığı genel amaçlı kriptografi için bir kütüphanedir.


BIP 4 Temmuz 2015 tarihinde yürürlüğe girmiştir. Ancak, yukarıda belirtilenler doğru olmakla birlikte, BIP66 aynı zamanda BIP'de belirtilmeyen çok daha ciddi bir sorunu da çözmektedir.


##### Güvenlik açığı



Bu konunun tam açıklaması 28 Temmuz 2015 tarihinde Pieter Wuille tarafından

[Bitcoin-dev posta listesine e-posta gönderin] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Herkese merhaba,
>

> Eylül 2014'te keşfettiğim ve bu ayın başlarında BIP66'nın %95 eşiğine ulaşıldığında kullanılamaz hale gelen bir güvenlik açığını ifşa etmek istiyorum.
>

> Kısa açıklama:
>

> Özel olarak hazırlanmış bir işlem Blockchain'i düğümler arasında çatallayabilirdi:
>

> - openSSL'i 32 bit sistemlerde ve 64 bit Windows sistemlerinde kullanma
> - windows olmayan 64 bit sistemlerde (Linux, OSX, ...) OpenSSL kullanma
> - imzaları ayrıştırmak için OpenSSL olmayan bazı kod tabanlarının kullanılması

E-postada ayrıca sorunun nasıl keşfedildiği ve tam olarak neyin neden olduğu ile ilgili ayrıntılar da yer alıyor. Sonunda, olayların bir zaman çizelgesini sunuyor ve biz burada en önemlilerinden bazılarını tekrarlayacağız. Bazıları, yukarıdaki şekilde gösterildiği gibi, zaten açıklanmıştır.


![](assets/bip66-timeline-1.webp)


BIP66'yı çevreleyen olayların zaman çizelgesi. Siyah renkli maddeler yukarıda açıklanmıştır.


##### Keşiften önce



Kimsenin bu konudan haberi olmadan, işlemlerin yanlış şekillendirilebilme olasılığını azaltmaya yönelik bir öneri olan ve artık geniş bir alana yayılan BIP62 ile bu sorun çözülebilirdi. BIP62'de önerilen değişiklikler arasında imzaların kodlanması için mutabakat kurallarının sıkılaştırılması ya da "katı DER kodlaması" da vardı. Pieter Wuille, Temmuz 2014'te BIP'de sorunu çözecek bazı değişiklikler önerdi:


> 2014-Temmuz-18: Bitcoin'nin imza kodlama kurallarının OpenSSL'in özel ayrıştırıcısına bağlı olmaması için BIP62 teklifini, katı DER imzaları gerekliliğinin sürüm 1 işlemlerine de uygulanmasını sağlayacak şekilde değiştirdim. O sırada artık DER olmayan imzalar bloklara kazılmıyordu, bu nedenle bunun herhangi bir etkisi olmayacağı varsayıldı. Bkz. https://github.com/Bitcoin/bips/pull/90 ve http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. O sırada bilinmiyordu, ancak uygulanmış olsaydı bu güvenlik açığını çözmüş olacaktı.

Bu BIP'nin "katı DER kodlamasından" çok daha fazlasını kapsayan genişliği nedeniyle, sürekli değişiyordu ve hiçbir zaman dağıtıma yaklaşamadı. BIP daha sonra geri çekildi çünkü Segregated Witness, BIP141, işlem uyumsuzluğunu farklı ve daha eksiksiz bir şekilde çözdü.


##### Keşiften sonra



OpenSSL, Bitcoin'te en başından beri kullanılması halinde sorunu çözecek yamaları içeren yazılımlarının yeni sürümlerini yayınladı. Ancak, OpenSSL'in herhangi bir yeni sürümünü yalnızca Bitcoin core'ün yeni bir sürümünde kullanmak sorunları daha da kötüleştirecektir. Gregory Maxwell bunu Ocak 2015'te başka bir [e-posta dizisinde] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) açıklamaktadır:


> Çoğu uygulama için bazı imzaları hevesle reddetmek genellikle kabul edilebilir olsa da, Bitcoin tüm katılımcıların girdi verilerinin kesin geçerliliği veya geçersizliği konusunda genel olarak hemfikir olması gereken bir mutabakat sistemidir.  Bir anlamda tutarlılık "doğruluktan" daha önemlidir.
> [...]
> Bununla birlikte, yukarıdaki yamalar genel sorunun yalnızca bir belirtisini düzeltmektedir: mutabakat-normatif davranış için mutabakat kullanımı için tasarlanmamış veya dağıtılmamış yazılıma (özellikle OpenSSL) güvenmek.  Bu nedenle, artımlı bir iyileştirme olarak, BIP62'nin bir alt kümesini kullanarak, DER uyumluluğunu yakında sıkı bir şekilde uygulamak için hedeflenen bir Soft-Fork öneriyorum.

Mutabakat sistemlerinde kullanılmak üzere tasarlanmamış kodların kullanılmasının ciddi riskler oluşturduğuna dikkat çekiyor ve Bitcoin'in katı DER kodlaması uygulamasını öneriyor. Bu, iyi bir seçim kriptografisinin önemini gösteren çok açık bir örnektir.


Bu olaylar, Gregory Maxwell'in Pieter Wuille'in daha sonra yayınladığı güvenlik açığından haberdar olduğu, ancak asıl soruna çok fazla dikkat çekmeden bir önlem olarak gizlenmiş bir düzeltmenin gizlice yapılmasına yardımcı olmak istediği izlenimini verebilir. Öyle olabilir, ancak bu tamamen spekülasyondur.


Daha sonra, Maxwell tarafından önerildiği gibi, BIP66, yalnızca katı DER kodlamasını belirten BIP62'nin bir alt kümesi olarak oluşturuldu. Bu BIP görünüşe göre geniş çapta kabul gördü ve Temmuz ayında dağıtıldı, ancak *doğrulamasız Mining* nedeniyle ironik bir şekilde iki Blockchain bölünmesi meydana geldi. Bu bölünmeler bir sonraki bölümde ele alınmaktadır.


![](assets/bip66-timeline-2.webp)


Buradan çıkarılacak en önemli sonuç, BIP'lerin aşağı yukarı *atomik* olması gerektiğidir; yani faydalı bir şey sağlayacak veya belirli bir sorunu çözecek kadar eksiksiz, ancak kullanıcılar arasında geniş bir desteğe izin verecek kadar küçük olmalıdır. Bir BIP'nin içine ne kadar çok şey koyarsanız, kabul edilme şansı o kadar azalır.


##### Validasyonsuz Mining nedeniyle bölünmeler



Ne yazık ki BIP66'nın hikayesi burada bitmedi. BIP66 etkinleştirildiğinde, bazı madenciler genişletmeye çalıştıkları blokları doğrulamadıkları için oldukça karışık bir durum ortaya çıktı. Buna doğrulamasız Mining ya da SPV-Mining (Basitleştirilmiş Ödeme Doğrulaması gibi) deniyor. Bitcoin düğümlerine [sorunu açıklayan bir web sayfasına] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining) bağlantı içeren bir uyarı mesajı gönderildi:


> 4 Temmuz 2015 sabahı erken saatlerde 950/1000 (%95) eşiğine ulaşıldı. Bundan kısa bir süre sonra, küçük bir Miner (yükseltilmemiş %5'in bir parçası) geçersiz bir blok çıkardı; bu beklenen bir durumdu. Ne yazık ki, ağ Hash oranının yaklaşık yarısının blokları tam olarak doğrulamadan Mining olduğu (SPV Mining olarak adlandırılır) ve bu geçersiz bloğun üzerine yeni bloklar inşa ettiği ortaya çıktı.

Uyarı sayfası, Bitcoin core'nin eski sürümlerini kullanmaları durumunda kullanıcılara normalde beklediklerinden 30 ek onay beklemeleri talimatını veriyordu.


Yukarıda bahsedilen bölünme 2015-07-04 tarihinde 02:10 UTC'de [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e) blok yüksekliğinden sonra meydana gelmiştir. Bu sorun aynı gün saat 03:50'de, 6 geçersiz blok çıkarıldıktan sonra çözülmüştür. Ne yazık ki, aynı sorun ertesi gün, yani 2015-07-05'te 21:50'de tekrar meydana geldi, ancak bu sefer geçersiz dal sadece 3 blok sürdü.


![](assets/bip66-timeline-3.webp)

BIP66'ya yol açan olaylar, dağıtımı ve sonrası, Bitcoin geliştiricilerinin ne kadar dikkatli olması gerektiğine dair çok iyi bir vaka çalışmasıdır. BIP66'dan birkaç önemli çıkarım:



- Açıklık ile bir güvenlik açığını yayınlamamak arasındaki denge hassas bir dengedir.
- Yayınlanmamış güvenlik açıkları için düzeltmeler dağıtmak, oynaması zor bir oyundur.
- Tutma konsensüsü Hard'dur.
- Mutabakat sistemleri için tasarlanmamış yazılımlar genellikle risklidir.
- BIP'ler bir şekilde atomik olmalıdır.


### Sonuç hakkında When Shit Hits The Fan



Bitcoin'de hatalar vardır. Hataları keşfeden kişilerin bunları sorumlu bir şekilde Bitcoin geliştiricilerine ifşa etmeleri teşvik edilir, böylece hatayı kamuya açıklamadan düzeltebilirler. İdeal olarak, hata düzeltmesi bir performans iyileştirmesi veya başka bir sis perdesi olarak gizlenebilir.


Yıllar boyunca ortaya çıkan daha ciddi sorunlardan bazılarına ve bunların nasıl ele alındığına baktık. Bazıları açıklar yoluyla kamuya açık olarak keşfedilirken, diğerleri sorumlu bir şekilde ifşa edildi ve kötü niyetli aktörlerin bunları istismar etme şansı olmadan önce düzeltilebildi.


## Tartışma Soruları

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Bu tartışma soruları sadece "Bitcoin gelişim felsefesi" içeriğinin bir özeti değildir, sizi daha fazla araştırma yapmaya teşvik etmek içindir, bu yüzden dışarı çıkıp keşfettiğinizden emin olun.


Bu soru havuzundaki konuyu seçerek 100-300 kelimelik [mini-essay] (https://www.youtube.com/watch?v=N4YjXJVzoZY) yazarak anlayışınızın derinliğini test edebilirsiniz. Çalışmanızla ilgili geri bildirim almak isterseniz mini-essay@planb.network adresine gönderebilirsiniz, incelemekten memnuniyet duyarız.


#### Adem-i Merkeziyetçilik



- Ademi merkeziyetçilik Hard'tür. İşe yaraması için neden bu kadar zahmete katlanıyoruz? Bazı kısımların merkezileştirildiği ve diğerlerinin merkezileştirilmediği karma bir yaklaşımı tercih edebilir miyiz?
- Ademi merkeziyetçilik çifte harcama sorununu ortaya çıkarır mı, yoksa çifte harcama sorunu ademi merkeziyetçiliği mi gerektirir? Satoshi çifte harcama sorununu nasıl çözmüştür?
- Bitcoin hangi açılardan sansüre daha yatkındır ve sansür neden bu kadar kötü bir şeydir? Sansür lehine herhangi bir argüman var mı?
- Bitcoin'nın izinsiz olduğu belirtiliyor. İzinsiz olduğunu düşündüğünüz başka ödeme yöntemleri var mı?



#### Güvenilmezlik




- Güvensizlik genellikle bir spektrumdur, ikili değildir. Bitcoin'in hangi yönleri daha ziyade Trustless'dir ve hangileri tipik olarak daha yüksek bir güven seviyesi içerir? Bunlar hafifletilebilir mi?
- Tüm işlemleri tam olarak doğrulayabilmek için bir Full node çalıştırmak istiyorsunuz. Bitcoin core'u https://Bitcoin.org/en/download adresinden indiriyorsunuz. Nereye güvendiniz ve Trustless'i tam olarak nereye yerleştirdiniz?
- Güvenilir bir sistemin üzerine bir Trustless sistemi kurabilir misiniz?



#### Gizlilik




- Bir kullanıcı Bitcoin ile etkileşime girerken iyi bir gizlilik sağladığında elde ettiği bazı önemli faydalar nelerdir? Ağ için bazı özgecil faydalar nelerdir?
- Adresleri yeniden kullanmak gizliliğinizi nasıl etkiler?
- Bitcoin bir UTXO modeli kullanırken, bazı alternatif kripto para birimleri bir hesap modeli kullanır. Bu seçimin gizlilik üzerindeki etkileri nelerdir?



#### Sonlu Supply




- Bitcoin'un sonlu Supply'si ile Coinbase Transaction aracılığıyla Coin ihracı arasındaki ilişki nedir? Coin ihracı ile güvenlik bütçesi arasındaki ilişki nedir ve bunlar nasıl çelişmektedir?
- Satoshi, Bitcoin'nin Supply üst sınırını değiştirmek için hangi parametreleri değiştirmiş olabilir? Supply'ü 1 milyon ile sınırlamaya karar verseydi ne değişirdi? 1 trilyona ne dersiniz?
- Neden bazı insanlar Bitcoin Supply'nın artırılmasını savunuyor? Sizce bu gerçekleşecek mi?


#### Yükseltme



- Speedy Trial nedir ve Taproot'yi etkinleştirmek neden gerekliydi?
- Softfork'ta yükseltme yapmak için neden bu kadar yüksek bir madenci yüzdesine ihtiyacımız var? Eşik neden sadece %51 değil?



#### Çekişmeli düşünme




- Sybil saldırısı nedir ve merkezi olmayan bir ağı buna bu kadar yatkın kılan nedir?
- Bitcoin ağındaki tüm oyuncuların - sadece geliştiricilerin değil - karşıt düşünmesi neden önemlidir?



#### Açık kaynak




- Sadece bir avuç bakımcı [Bitcoin core](https://github.com/Bitcoin/Bitcoin) deposuna kod birleştirmek için gerekli GitHub izinlerine sahiptir. Bu izinsiz bir ağ ile çelişmiyor mu?
- Açık kaynak geliştirme süreci bir sybil saldırısına eğilimli midir? Eğer öyleyse, buna nasıl karşı koyarsınız?
- Üçüncü taraf açık kaynak kütüphanelerine güvenmenin faydaları ve dezavantajları nelerdir ve Bitcoin core ile benimsenen yaklaşım nedir?
- Kod incelemesinin ötesinde hangi şekillerde incelemeye ihtiyacımız var? Ne kadar gözden geçirmenin yeterli olduğunu nasıl belirleyebiliriz?
- Bitcoin üzerinde çalışan uzman kişilerin her zaman yeterli sayıda olmasını nasıl sağlayacağız? Olmadığında ne olur ve onların dürüstlüklerini ve niyetlerini nasıl değerlendiririz?



#### Ölçeklendirme




- Sharding'in karmaşıklık pahasına ölçeklendirme avantajları sunduğu savunulmaktadır. Teknolojik olarak sağlam görünseler bile anlaşılması zor oldukları için teknolojik gelişmeleri neden benimsemeliyiz ya da benimsememeliyiz?
- Bitcoin'te tanıtılan içe doğru ölçeklendirme yöntemlerine bazı örnekler nelerdir?
- Merkezi olmayan bir sistemde dikey ölçeklendirme neden çok daha zordur? Peki ya yatay ölçeklendirme?
- Tüm dünyayı Bitcoin'e nasıl dahil edebileceğimiz konusunda fikir birliğine varmış gibi görünmüyoruz. Satoshi'in 2009'daki ilk blok Mining'dan önce en azından oraya ulaşmanın bir yolunu düşünmesi gerekmez miydi?
- Aşağıdakilerin her birini nasıl sınıflandırırsınız (dikey, yatay, içe doğru veya bir ölçeklendirme tekniği değil): parçalama, blok boyutu artışı, SegWit, SPV düğümleri, merkezi borsalar, Lightning Network, blok aralığı azalması, Taproot, yan zincirler



# Son Bölüm


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Yorumlar & Derecelendirmeler


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Sonuç


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>