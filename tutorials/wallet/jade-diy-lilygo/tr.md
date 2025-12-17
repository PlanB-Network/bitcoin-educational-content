---
name: Jade DIY
description: 15 dolarlık bir geliştirme kartını tamamen işlevsel bir Bitcoin donanım wallet'e dönüştürün
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Başlangıç Yapısı


**İzleyici kitlesi:** Gömülü sistem deneyimi çok az olan ya da hiç olmayan meraklı inşaatçılar.


**Süre:** 2 saat (esnek)


**Kazanımlar:** Sonunda öğrenciler şunları yapacaklardır:



- DIY donanım cüzdanlarının ticari cihazlara karşı güvenlik modelini tanıyın.
- Mikrodenetleyici tabanlı bir işaretleme cihazı monte edin.
- Açık kaynaklı ürün yazılımını flaş edin ve derleme sağlama toplamını doğrulayın.
- Yeni cihazlarını kullanarak bir mainnet işlemi imzalayın ve yayınlayın.


---

## Özet


Bu 2 saatlik atölye çalışması, yeni başlayanlara 15 dolarlık LilyGO T-Display kartına açık kaynaklı Jade aygıt yazılımını flaşlayarak işlevsel bir Bitcoin donanım wallet oluşturmayı öğretir. Öğrenciler, genel geliştirme donanımını 150 dolarlık ticari cüzdanlarla karşılaştırılabilir bir imza cihazına dönüştürerek, güvenlik temellerini yalnızca teori yerine uygulamalı deneyim yoluyla öğrenirler.


### Felsefe


Kendi imzalama cihazınızı oluşturmak sadece paradan tasarruf etmekle ilgili değildir; Bitcoin'nizi koruyan teknolojiyi anlamakla ilgilidir. Bu atölye çalışması, kara kutu güveni yerine "anlama yoluyla güvenliği" benimsiyor. Bileşenleri tedarik ederek, açık kaynaklı aygıt yazılımını yanıp sönerek ve entropiyi kendileri üreterek, öğrenciler güvenlik iddialarını eleştirel bir şekilde değerlendirmeyi öğrenirken tedarik zinciri riskini azaltırlar. Amaç, bilinçli özerkliktir: öğrenciler, sertleştirilmiş ticari alternatiflere kıyasla DIY cihazlarının hem gücünü hem de sınırlamalarını anlamalıdır.


---

## Kavram Tanıtımı (15 dakika)


### Kendi Kendine Velayet Nedir ve Neden Önemlidir?


Bitcoin, para sistemimizden bankalar ve şirketler gibi güvenilir üçüncü taraflara olan ihtiyacı ortadan kaldırmak için yaratılmıştır. Bitcoin, güven kullanmak yerine matematik, fizik ve kriptografi kullanarak herkesin kimsenin iznine ihtiyaç duymadan kendi parasına sahip olma ve kontrol etme gücüne sahip olmasını sağlar.


Bunun çalışma şekli, bitcoin'in banka hesabı gibi merkezi bir defter yerine bilgisayarlar tarafından yönetilen halka açık ve şeffaf bir defter olan blok zinciri veya bitcoin zaman zinciri adı verilen küresel bir dijital defterde var olmasıdır.


Anlaşılması gereken önemli nokta, bitcoin'i bir yerden başka bir yere taşımak için, bu işlemi özel anahtar adı verilen bir şeyle imzalamanız gerektiğidir. Bunu bir şifre ile bir kasanın kilidini açmak ve bitcoin'i başka birinin kasasına taşımak gibi düşünün. Bitcoin, paranızı sizin yerinize taşıması için bir bankaya güvenmek yerine, size bu kasanın anahtarlarını kendiniz tutma gücü verir.


Büyük güç büyük sorumluluk getirir, anahtarlarınızı kaybederseniz paranız sonsuza dek yok olur. Bu şekilde, kasanın anahtarlarını paranın kendisi olarak düşünebilirsiniz. Anahtarlar bitcoin ile aynı şey olmasa da, fonlarınızı hareket ettirme mekanizmasıdır ve bu nedenle korunması son derece önemlidir. Bu yüzden "anahtarlarınız değil, paralarınız" diyoruz.


Self-custody terimi kafa karıştırıcı gelebilir, ancak tüm anlamı kendi özel anahtarlarınızı tutmak ve kendi bitcoin'inizi kontrol etmektir. Eğer bu anahtarı siz tutmuyorsanız, sizin yerinize tutması için başka birine güveniyorsunuz demektir. Bitcoin'iniz bir ETF'de veya bir borsada (Mt. Gox, FTX, Coinbase, Binance, vb.) bulunuyorsa, bitcoin'e sahip değilsinizdir, bitcoin üzerinde bir hakkınız vardır. Bu da borsaların hacklenmesi ve bitcoin'inizi kaybetmeniz ya da şirketlerin paranızı ödünç verip size sadece bir kısmını rezerv olarak vermesi gibi her türlü riski beraberinde getirir. Ayrıca güvenilir üçüncü taraflar paranızın tam kontrolüne sahip olur ve para çekme işlemlerini sınırlayabilir ya da dondurabilir.


![image](assets/fr/01.webp)


Öz saklama ile güveni denklemden çıkarırsınız. Hiç kimse fonlarınızı donduramaz veya bir işlemi reddedemez, sınırların ötesine, herhangi birine, herhangi bir zamanda para gönderebilirsiniz ve bir banka hesabına, kimliğe veya kimsenin onayına ihtiyacınız yoktur. Hiç kimse sizi durduramaz, sansürleyemez ya da sizden çalamaz, bu da bitcoin'in özgürlük parası olarak tüm gücünün kilidini açar. İşte bu yüzden diyoruz ki, bitcoin ile kendi bankanız olabilirsiniz.


Bitcoin, mevcut sistemimizden bir çıkış yolu olarak güven ve paranın manipülasyonu sorununu çözmek için oluşturuldu, ancak çıkış sadece anahtarları alırsanız işe yarar. İşte bu yüzden öz saklama çok önemlidir.


### Wallet nedir?


wallet terimi biraz yanlış bir isimlendirmedir ve bu nedenle kafa karıştırıcı olabilir. Evet, bir bitcoin wallet'nin, fiziksel bir wallet gibi, değer depoladığı doğrudur. Ancak temel fark, bitcoin cüzdanlarının aslında herhangi bir bitcoin depolamamasıdır.


Bitcoin yalnızca halka açık blok zincirinde veya siber uzaydaki metaforik kasalarda bir defter girişi olarak bulunur. Bitcoin'i taşımak için kasanın kilidini açmak ve paraları başka bir yere taşımak için anahtarlarınızı kullanmanız gerektiğini unutmayın, özel anahtarlar bitcoin harcamak için kullanılan şeydir. wallet'ünüzle bir işlem yaptığınızda, işlemi imzalamak için gerçekten sadece anahtarlarınızı kullanırsınız. Bu şekilde paranın sahibi olduğunuzu ve bu paraları harcama hakkına sahip olduğunuzu kanıtlamış olursunuz.


Bitcoin cüzdanları aslında yalnızca özel anahtarlarınızı saklar, bu nedenle bunlara anahtar zinciri demek daha doğru olacaktır.


### Hot vs Cold Cüzdanlar


Hot wallet, telefonunuzda veya bilgisayarınızda bulunan bir yazılım uygulamasıdır. İnternete bağlıdır, bu nedenle kullanımı daha kolaydır ve işlemleri imzalamak daha hızlıdır, ancak bu aynı zamanda bilgisayar korsanlarına, kötü amaçlı yazılımlara ve kimlik avına daha fazla maruz kaldığı anlamına gelir. İnternete bağlı olduğu, fişe takılı olduğu ve açık olduğu için "sıcak" olarak adlandırılır. Örnek olarak bir telefon wallet veya bir tarayıcı wallet verilebilir.


Öte yandan soğuk wallet veya donanım wallet, anahtarınızı çevrimdışı olarak oluşturan ve saklayan bir cihazdır. Bu, birinin fonlarınızı hackleme olasılığını ortadan kaldırır ve uzun vadeli tasarruflar için çok daha güvenlidir, ancak her işlemi imzalamak için gereken bir cihazdır ve daha az kullanışlı olabilir.


### Hardware Wallet Tehdit Modeli


Donanım cüzdanları temel bir sorunu çözmek için vardır: özel anahtarlarınızı kötü amaçlı yazılımlar veya uzaktan saldırganlar tarafından ele geçirilebilecek internete bağlı bir bilgisayara maruz bırakmadan Bitcoin işlemlerini nasıl imzalarsınız? Temel tehdit modeli, günlük dizüstü bilgisayarınızın veya telefonunuzun potansiyel olarak düşmanca olduğunu varsayar. Donanımsal bir wallet, özel anahtarların cihazdan asla ayrılmadığı izole bir ortam yaratır ve işlem imzalama işlemi, anahtarın kendisini değil yalnızca imzayı ana bilgisayara geri ileten bir secure element veya mikrodenetleyicide gerçekleşir. Bilgisayarınız tamamen ele geçirilmiş olsa bile, bir saldırgan cihaza ve PIN kodunuza fiziksel erişim olmadan Bitcoin'nizi çalamaz.


Ancak donanım cüzdanları kendi tehditlerini de beraberinde getirir. Üreticinin arka kapılar eklemediğine, tedarik zincirine müdahale edilmediğine ve rastgele sayı üretiminin gerçekten rastgele olduğuna güvenmelisiniz. Fiziksel saldırganlar yan kanal saldırıları veya çip manipülasyonu yoluyla anahtarları çıkarabilir ve geçici erişimi olan biri cihazınızı değiştirebilir. Kendi wallet donanımınızı oluşturmak bu dengeleri anlamanıza yardımcı olur; genel amaçlı mikro denetleyicilere karşı güvenli öğeler, bir ekrandaki işlemlerin nasıl doğrulanacağı ve hem uzaktan hem de fiziksel tehditlere karşı nasıl korunacağınız konusunda kararlar alırsınız. Amaç mükemmel güvenlik değil, hangi tehditlere karşı korunduğunuzu ve hangilerinin kaldığını anlamaktır.


### Anahtar Kavramlar



- Entropi ve seed ifadeleri:** wallet'iniz ancak onu doğuran rastgelelik kadar güvenlidir. Cihazın rastgele sayı üretecini zar atma gibi insan dostu hilelerle karıştıracağız, bu entropiyi 12 veya 24 kelimelik bir [BIP39 ifadesine] (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) dönüştüreceğiz ve güvendiğiniz yazılı veya metal bir yedekle odadan çıkacağız.
- Tohum cümlesi hijyeni:** seed'ye birikimlerinizin ana anahtarları gibi davranın. Kelimeleri asla bir telefona veya bilgisayara yazmayın - keylogger'lar, ekran görüntüleri ve bulut yedeklemeleri sonsuza kadar sızdırabilir. İfadeyi çevrimdışı tutun, sadece sizin erişebileceğiniz bir yerde saklayın ve ayrılmadan önce yüksek sesle okuma alıştırması yapın.
- Güvenli eleman + mikrodenetleyici:** secure element'i kasa ve mikrodenetleyiciyi beyin olarak düşünün. secure element, özel anahtarları kurcalamaya karşı dirençle korurken, mikrodenetleyici ekranı, düğmeleri ve ürün yazılımı mantığını yönetir. Bugün inşa ettiğimiz donanım cüzdanlarının secure element'e sahip olmadığını unutmayın. Bu güvensiz olduğu anlamına gelmez, sadece bir koruma seviyesi daha azdır.
- Firmware'e güvenmek:** Firmware, wallet'un görünmez işletim sistemidir. Her zaman etiketli sürümlerden indirin, yayınlanan karmayı kontrol edin ve tekrarlanabilir yapıların birden fazla kişinin aynı kodu derlemesine ve tam olarak aynı ikili dosyaya ulaşmasına izin verdiğini anlayın. Sağlama toplamı eşleşmiyorsa, imzalamayın.


---

## Ne İnşa Ediyoruz?


Genel bir donanım olan LilyGo T-Display'i alıyoruz ve Jade SDK ürün yazılımını üzerinde yanıp sönüyoruz. Jade Plus] (https://blockstream.com/jade/jade-plus/), genellikle 150 dolara mal olan açık kaynaklı bir wallet'dur:


![image](assets/fr/02.webp)


Bugün, aygıt yazılımlarını 15 dolarlık bir donanıma yükleyeceğiz.


### Ne Satın Almalı


![image](assets/fr/03.webp)



- LilyGO T-Display (kabuklu 16MB, model K164)** - [Doğrudan LilyGO'dan sipariş edin] (https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) yaklaşık 15 $ karşılığında. Bu ESP32 kartı, Blockstream'in Jade Plus'ını yansıtan ekran, düğmeler ve USB arayüzü sağlar. Yerleşik ESP32 ayrıca Wi-Fi ve Bluetooth radyoları içerir; bunları devre dışı bırakan ürün yazılımı göndereceğiz, ancak tehdit modelinizi şekillendiriyorlar çünkü kötü amaçlı kod bunları tekrar açabilir.
- USB-C kablosu** - Aygıt yazılımını flaş edebilmeniz ve kartı doğrudan dizüstü bilgisayarınızdan çalıştırabilmeniz için veri özellikli bir kablo getirin (sınıf kullanımı için tamamen uygundur).


### Neden Kendi Hardware Wallet'inizi Oluşturmalısınız?



- Ticari bir cihaz satın almaya kıyasla yaklaşık 135 $ tasarruf edin.
- Ürün yazılımı yanıp sönmesi, güvenli öğeler ve wallet hijyeni ile konfor oluşturun.
- Tasarrufları birden fazla cüzdana yaymak için ek imzalama cihazları açın.
- Her bileşeni kendiniz tedarik ve monte ederek tedarik zinciri riskini azaltın.
- Lopp'un mantrasını aklınızda tutun: egemenlik ve kolaylık her zaman çelişkilidir.


## Fiziksel Kurulum


### Davanızı Hazırlayın


LilyGO T-Display kartınızı barındırmak için iki seçeneğiniz vardır: 3D baskılı bir kasa veya resmi LilyGO muhafazası. Basılı kasa [bu model] (https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure) adresinden bulunabilir ve yazdırılabilir. Cihazınız için hafif ve özelleştirilebilir bir kabuk sunar.


![image](assets/fr/04.webp)


Alternatif olarak, biraz daha farklı bir uyum ve bitiş sağlayan, daha sağlam koruma ve cilalı bir görünüm sunan resmi LilyGO kılıfını kullanabilirsiniz.


![image](assets/fr/05.webp)


Basılı ve resmi kasaların tasarım ve montaj açısından biraz farklılık gösterdiğini unutmayın. Hangi seçeneği seçerseniz seçin, bağlantıların gevşemesini veya hasar görmesini önlemek için kartın kasanın içine düzgün şekilde oturduğundan emin olun.


### Panoyu İnceleyin


Devam etmeden önce, LilyGO T-Display kartınızı görünür kusurlar veya kalıntılar açısından dikkatlice inceleyin. Ekranın, düğmelerin ve USB-C bağlantı noktasının temiz olduğundan ve toz veya lehim sıçraması olmadığından emin olun. Kartı dikkatli kullanın ve hassas bileşenlerin zarar görmesini önlemek için kendinizi topraklayarak veya bir ESD bilek kayışı kullanarak elektrostatik deşarj (ESD) güvenliğine uyun.


### Dizüstü Bilgisayarınıza Bağlanın


Veri özellikli bir USB-C kablosu kullanarak LilyGO kartını dizüstü bilgisayarınıza bağlayın. Bu bağlantı güç sağlayacak ve aygıt yazılımını flaşlamanıza izin verecektir.


Açılışta, aşağıdaki ekranla karşılaşacaksınız:


![image](assets/fr/06.webp)



Güç açıldığında, LilyGO düz renkler arasında geçiş yapan renkli bir test ekranı gösterecektir. Bu, aygıt yazılımını yanıp sönmeden önce ekranın ve kartın doğru çalıştığını onaylar.


Renk testi tamamlandığında, ekran varsayılan bir duruma yerleşecek ve kartın oluşturma sürecindeki sonraki adımlar için hazır olduğunu gösterecektir.


![image](assets/fr/07.webp)


## Kolay Yol ya da Hard Yolu


wallet donanım yazılımınızı flaşlamak için iki ana yaklaşım vardır: kolay yol ve zor yol. Kolay yol, aygıt yazılımını minimum girdi ile cihazınıza otomatik olarak yükleyen önceden yapılandırılmış araçları veya web tabanlı flaşörleri kullanır. Bu yöntem, hızlı bir kazanç elde etmek isteyen veya hata ayıklama ve komut satırı etkileşimlerinin karmaşıklığından kaçınmayı tercih eden yeni başlayanlar için idealdir. Süreci basitleştirir ve sizi daha hızlı çalışır hale getirerek gömülü geliştirme veya donanım cüzdanlarına yeni başlayanlar için erişilebilir hale getirir.


Öte yandan zor yol, aygıt yazılımını flaşlamak için komut satırı araçlarını manuel olarak kullanmayı içerir. Bu yaklaşım, orijinalliği ve bütünlüğü sağlamak için ürün yazılımı imzalarını ve sağlama toplamlarını doğrulamayı gerektirir ve size flaşlama işlemi ve ürün yazılımının donanımla nasıl etkileşime girdiği hakkında daha derin bir anlayış sağlar. Daha fazla çaba ve terminal komutlarına aşinalık gerektirse de, cihazınızın güvenliği konusunda daha fazla kontrol, şeffaflık ve güven sunar.


Her yöntemin kendine göre dezavantajları vardır: kolay yol, hız ve kolaylık için bir dereceye kadar güven ve anlayışı feda ederken, zor yol daha fazla zaman ve teknik beceri gerektirir, ancak sizi esneklik ve altta yatan teknolojiyi daha güçlü bir şekilde kavramakla ödüllendirir. Eğitmenler, öğrencileri kendi konfor seviyelerine ve meraklarına en uygun yolu seçmeye teşvik etmeli, hem güveni hem de keşfi teşvik etmelidir.


## Kolay Yol


ESP32'yi flaşlamanın en kolay yolu



- Resmi Blockstream Github'a gidin: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Kaynak dosyayı indirebilir ve web sitesini yerel olarak çalıştırabilirsiniz, ancak GitHub zaten [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/) adresinde barındırmaktadır. GitHub HTML, CSS, JavaScript, vb. doğrudan tarayıcınıza sunar, böylece geliştirici araçları yüklemeden cihazı flaşlayabilirsiniz.


![image](assets/fr/09.webp)



- Açılır menüyü açın (muhtemelen varsayılan olarak `M5Stack Core2`dir) ve geliştirme kartınızı seçin - bu sınıf için `LILYGO T-Display`i seçin.


![image](assets/fr/10.webp)



- Flaşa tıkladığınızda bu görünecektir. Hangi cihazın LILYGO olduğunu anlamak için, lilygo'nun fişini çekin ve tekrar takın. Lilygo'nun takılı olduğu com portu bir görünüp bir kaybolacaktır. Jade'in takılı olduğu COM portuna tıklayın


![image](assets/fr/11.webp)



- İşte bu kadar, bir ilerleme çubuğu görünmeli ve bittiğinde kurmaya hazırsınız


## Jade Wallet'in Kurulumu


Aygıt yazılımı başarıyla flaşlandıktan sonra, LilyGO T-Display'iniz artık tamamen işlevsel bir Jade donanım wallet'dir. Bu bölüm, seed ifadenizi oluşturmaktan cihazı wallet gibi Sparrow yazılımı veya Blockstream Green mobil uygulaması ile bağlamaya kadar ilk kurulum sürecinde size yol gösterecektir.


### İlk Önyükleme ve Aygıt Kurulumu



- Cihazı açın:** LilyGO hala USB-C üzerinden dizüstü bilgisayarınıza bağlıyken, Jade ürün yazılımı otomatik olarak önyükleme yapmalıdır. Ekranda Jade logosunun göründüğünü göreceksiniz.



- Kurulum moduna girin:** Cihaz size bir başlangıç menüsü sunacaktır. Gezinmek için kart üzerindeki iki fiziksel düğmeyi kullanın:
 - Sol düğme:** Yukarı/geri hareket
 - Sağ düğme:** Aşağı/ileri git
 - Her iki düğme aynı anda:** Seç/onayla



- "Kurulum "u seçin:** Kurulum seçeneğine gidin ve onaylamak için her iki düğmeye de basın. Cihaz, ilk yapılandırma işlemi boyunca size rehberlik edecektir.


### Wallet'ınızı Oluşturma



- "Kuruluma Başla "yı seçin:** Cihaz sizden wallet oluşturma işlemine başlamanızı isteyecektir. Seçiminizi onaylayın.



- "Yeni Wallet Oluştur "u seçin:** Size iki seçenek sunulacaktır:
 - Yeni Wallet Oluştur:** Yeni bir seed ifadesi oluşturur (atölye çalışması için bunu seçin)
 - Wallet'i Geri Yükleme:** Bir seed ifadesinden mevcut bir wallet'yı kurtarma (ileri düzey kullanıcılar için)



- "Yeni Wallet Oluştur" öğesini seçin ve onaylayın.



- Entropi oluştur:** Cihaz, kriptografik entropi oluşturmak için rastgele sayı üretecini kullanacaktır. Cihaz birden fazla kaynaktan rastgelelik topladığı için bu işlem birkaç saniye sürer.


### Tohum İfadenizi Kaydetme



- seed cümlenizi yazın:** Cihaz şimdi her seferinde bir kelime olmak üzere 12 kelimelik BIP39 seed cümlesini görüntüleyecektir. Bu, tüm süreçteki en kritik adımdır.


**Önemli güvenlik uygulamaları:**


- Her kelimeyi açık bir şekilde kağıda yazın (varsa verilen seed ifade kartlarını kullanın)
- Yazdığınız her kelimeyi iki kez kontrol edin
- seed ifadesinin fotoğrafını asla telefonunuzla çekmeyin
- Kelimeleri asla herhangi bir bilgisayara veya telefona yazmayın
- seed ifadenizi gizli tutun - ekranınızı paylaşmayın veya başkalarına göstermeyin



- seed cümlenizi doğrulayın:** 12 kelimenin tamamını yazdıktan sonra cihaz, doğru kaydettiğinizden emin olmak için cümleden birkaç kelimeyi onaylamanızı isteyecektir. Her istem için doğru kelimeyi seçmek için düğmelerini kullanın.


**Profesyonel ipucu:** Devam etmeden önce, seed cümlenizi kendinize yüksek sesle okuma alıştırması yapın (başkalarının duymaması için sessizce). Bu, herhangi bir el yazısı hatasını veya belirsizliği yakalamaya yardımcı olur.


### Bağlantı Yöntemi



- Bağlantı türünü seçin:** Jade aygıt yazılımı iki bağlantı yöntemini destekler:
 - USB:** USB-C kablosu ile kablolu bağlantı (bu atölye için önerilir)
 - Bluetooth:** Mobil cihazlara kablosuz bağlantı



- Masaüstü wallet yazılımı için en kolay seçenek olduğundan ve kablosuz saldırı vektörleri oluşturmadığından şimdilik **USB**'yi seçin.



- Cihaz adlandırma:** Jade, "Connect Jade A7D924" gibi benzersiz bir tanımlayıcı görüntüleyecektir. Bu tanımlayıcı, birden fazla donanım cüzdanı oluşturmanız durumunda bunları birbirinden ayırt etmenize yardımcı olur. İsterseniz bu tanımlayıcıyı not edin.


### Wallet Yazılımına Bağlanma


Artık yeni oluşturduğunuz donanım wallet ile arayüz oluşturmak için iki ana seçeneğiniz var: Blockstream Green mobil uygulaması (hareket halindeyken kullanım için) veya Sparrow Wallet (daha gelişmiş özelliklere sahip masaüstü kullanımı için). Bu atölye çalışmasında, Bitcoin işlemlerinin teknik ayrıntılarına daha iyi görünürlük sağladığı için Sparrow Wallet'a odaklanacağız.


#### Seçenek 1: Blockstream Green Mobil Uygulaması (Hızlı Başlangıç)


Cihazınızı bir mobil cihaz ile hızlı bir şekilde test etmek istiyorsanız:



- App Store (iOS) veya Google Play'den (Android) **Blockstream Green** uygulamasını indirin
- Uygulamayı açın ve "Hardware Wallet'e Bağlan "ı seçin
- Desteklenen cihazlar listesinden "Jade "i seçin
- Jade cihazınızı USB-C - USB-C kablosu (veya iPhone 15+ için USB-C - Lightning adaptörü) kullanarak telefonunuza takın
- Bağlanmak ve ilk wallet'inizi oluşturmak için ekrandaki talimatları izleyin


**Liquid hakkında not:** Blockstream Green uygulaması hem Bitcoin hem de Liquid'i (bir Bitcoin yan zinciri) destekler. Liquid özelliklerini kullanıyorsanız, sizden "Ana körleme anahtarını dışa aktarmanız" istenebilir - bu, uygulamanın Liquid ağındaki aksi takdirde gizli olan işlem tutarlarını görmesini sağlar. Bu atölye çalışması için Liquid özelliklerini atlayabilir ve standart Bitcoin işlemlerine odaklanabilirsiniz.


#### Seçenek 2: Sparrow Wallet (Atölye için önerilir)


Sparrow Wallet, Bitcoin işlemleriniz üzerinde ayrıntılı kontrol sağlayan ve Jade donanımınız wallet ile sorunsuz bir şekilde bağlanan güçlü bir masaüstü uygulamasıdır.


**Kurulum:**



- Sparrow Wallet'yı resmi web sitesinden indirin: [sparrowwallet.com](https://sparrowwallet.com)
- İndirme imzasını doğrulayın (ayrıntılar için Sparrow belgelerine bakın)
- Uygulamayı yükleyin ve başlatın


**C Jade'inizi Sparrow'e Bağlama:**



- Sparrow'da **Dosya → Yeni Wallet** öğesine gidin
- wallet'nize bir isim verin (örneğin, "My Jade Wallet")
- **Bağlı Hardware Wallet** öğesine tıklayın
- Sparrow takılı Jade cihazınızı otomatik olarak algılamalıdır
- İstenirse, her iki düğmeye de basarak Jade ekranında bağlantıyı onaylayın
- İstediğiniz senaryo türünü seçin:
 - Native Segwit (P2WPKH):** Yeni başlayanlar için önerilir - en düşük ücretler, modern cüzdanlarla en geniş uyumluluk
 - İç içe Segwit (P2SH-P2WPKH):** Eski hizmetlerle uyumluluk için
 - Taproot (P2TR):** En gelişmiş, en iyi gizliliği ve en düşük ücretleri sunar, ancak en ileri wallet desteğini gerektirir
- Bağlantıyı tamamlamak için **Anahtar Deposunu Aktar** öğesine tıklayın


**Sparrow'in Sunucu Bağlantısının Yapılandırılması:**


Bakiyenizi görebilmeniz veya işlemleri yayınlayabilmeniz için Sparrow'ün blok zinciri verilerini almak üzere bir Bitcoin düğümüne bağlanması gerekir. Her biri kolaylık, gizlilik ve güven arasında farklı ödünleşimlere sahip birkaç seçeneğiniz vardır:



- Genel Electrum Server (En kolay, en az özel):** Üçüncü bir tarafça işletilen genel bir sunucuya bağlanır. Kurulumu hızlıdır, ancak sunucu wallet'inizin adreslerini görebilir ve potansiyel olarak bunları IP adresinize bağlayabilir. Test ağında test etmek için iyidir.
 - Sparrow'da **Araçlar → Tercihler → Sunucu** bölümüne gidin
 - Genel Sunucu** öğesini seçin ve listeden bir sunucu seçin
 - Doğrulamak için **Bağlantıyı Test Et** seçeneğine tıklayın



- Bitcoin Core veya Knots Node (En özel, en çok iş):** Kendi tam Bitcoin düğümünüzü çalıştırın. Bu, her işlemi kendiniz doğruladığınız ve başkasının sunucusuna güvenmediğiniz için gizlilik ve doğrulama için altın standarttır. Bununla birlikte, tüm blok zincirini (~600GB) indirmeyi ve düğümünüzü senkronize tutmayı gerektirir.
 - Bitcoin Çekirdek veya Düğümleri takın ve senkronize edin
 - Sparrow'da **Araçlar → Tercihler → Sunucu** bölümüne gidin
 - **Bitcoin Core veya Knots** öğesini seçin ve düğümünüzün bağlantı ayrıntılarını girin



- Özel Electrum Server (İyi denge):** Bitcoin Core veya Knots düğümünüze bağlı kendi Electrum sunucunuzu (Fulcrum veya Electrs gibi) barındırın. Sparrow'i düğümünüzle aynı makinede çalıştırmanıza gerek kalmadan tam gizlilik sunar.
 - Bitcoin Core veya Knots düğümünüze işaret eden bir Electrum sunucusu kurun
 - Sparrow'de **Araçlar → Tercihler → Sunucu** bölümüne gidin
 - Özel Electrum**'u seçin ve sunucunuzun URL'sini girin


Bu atölye çalışmasında, testnet işlemleri için bir **Public Electrum Server** kullanmak gayet uygundur. Gerçek fonların bulunduğu bir üretim ortamında, maksimum gizlilik için kendi düğümünüzü çalıştırmayı veya güvenilir bir özel sunucu kullanmayı düşünebilirsiniz.


#### Seçenek 3: Blockstream Green Masaüstü Uygulaması (Hızlı Başlangıç)


Blockstream Green, JadeDIY'nin kurulumunu tamamlayan yazılımdır ve masaüstü sürümüyle birlikte olmalıdır



- Resmi Blockstream uygulamasını edinin - bu, web sitelerinden ona giden bağlantıdır. Oraya gittiğinizde [Şimdi indir] (https://blockstream.com/app/) seçeneğine tıklayın.


![image](assets/fr/12.webp)



- İndirmelerinizin nereye gittiğine bağlı olarak, dosya büyük olasılıkla İndirilenler klasörünüzde olacaktır. Orayı kontrol edin ve yazılımı yüklemek için çalıştırılabilir dosyaya çift tıklayın.


![image](assets/fr/13.webp)



- Yükleyiciyi çalıştırmak için yönetici hakları vermeniz gerekebilir. Bunu yaptığınızda, aşağıdaki resimdeki gibi görünmesi gereken bir pencere açılacaktır - **Sonraki** seçeneğine tıklayın.


![image](assets/fr/14.webp)



- Yüklenen uygulamanın nerede bulunmasını istediğinizi seçin (diğer programlarınızla birlikte bir konum veya bulunması kolay bir yer), ardından **Sonraki** öğesine tıklayın.


![image](assets/fr/15.webp)



- Yükleyici bir kısayol adı isteyecektir. Bir tane girin veya varsayılanı koruyun, ardından **Sonraki** öğesine tıklayın.


![image](assets/fr/16.webp)



- Bir masaüstü kısayolu istiyorsanız, kutuyu işaretleyin; aksi takdirde **Sonraki** öğesine tıklayın.


![image](assets/fr/17.webp)



- Son olarak, **Yükle** seçeneğine tıklayın ve kurulumun tamamlanması için birkaç dakika bekleyin.


![image](assets/fr/18.webp)



- İlerleme çubuğu sonuna kadar dolmalıdır.


![image](assets/fr/19.webp)



- Bittiğinde, yeni bir sayfa görünecektir - **Bitir** seçeneğine tıklayın.


![image](assets/fr/20.webp)



- Yeni yüklediğiniz Blockstream uygulamasını bulun (Windows 11 Başlat menüsünde gösterilen örnek).


![image](assets/fr/21.webp)



- Bulduğunuzda, başlatmak için tıklayın - bir açılış ekranı görünmelidir.


### Kurulumunuzu Doğrulama


Sparrow'e (veya başka bir wallet uygulamasına) bağlandıktan sonra:



- Adreslerinizi kontrol edin:** Sparrow, seed ifadenizden türetilen alıcı adreslerini görüntüleyecektir. Jade cihazınızdaki bir adresi Sparrow'daki "Receive" sekmesine gidip "Display Address "e tıklayarak doğrulayabilirsiniz - adres hem bilgisayar ekranınızda hem de Jade ekranında görünmelidir.



- Bir alıcı adresi oluşturun:** Sparrow'da **Alıcı** sekmesine tıklayın ve ilk Bitcoin alıcı adresinizi kopyalayın.



- İşlemler için hazır:** wallet donanımınız artık tamamen yapılandırılmıştır ve Bitcoin işlemlerini almaya ve imzalamaya hazırdır. Bir testnet işlemi imzalama alıştırması yapmak için bir sonraki bölüme geçin.



---

### Hızlı Kurulum Kontrol Listesi



- Jade ürün yazılımı başarıyla önyükleniyor
- 12 kelimelik seed ifadesiyle oluşturulan yeni wallet
- Tohum ifadesi açıkça yazılmış ve doğrulanmıştır
- USB bağlantı modu seçildi
- Wallet yazılımı (Sparrow) yüklü ve bağlı
- Sunucu bağlantısı yapılandırıldı (mainnet için genel Electrum)
- Cihazda oluşturulan ve doğrulanan ilk alıcı adresi



---

**MIT Lisansı**


**Telif hakkı (c) 2025 The Bitcoin Network NYC**


Bu yazılımın ve ilgili dokümantasyon dosyalarının ("Yazılım") bir kopyasını elde eden herhangi bir kişiye, Yazılımın kopyalarını kullanma, kopyalama, değiştirme, birleştirme, yayınlama, dağıtma, alt lisans verme ve/veya satma hakları dahil ancak bunlarla sınırlı olmamak üzere, kısıtlama olmaksızın Yazılım üzerinde işlem yapma ve Yazılımın verildiği kişilere aşağıdaki koşullara tabi olarak bunu yapma izni ücretsiz olarak verilmektedir:


Yukarıdaki telif hakkı bildirimi ve bu izin bildirimi Yazılımın tüm kopyalarına veya önemli kısımlarına dahil edilecektir.


YAZILIM, TİCARİ ELVERİŞLİLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME GARANTİLERİ DAHİL ANCAK BUNLARLA SINIRLI OLMAMAK ÜZERE AÇIK VEYA ZIMNİ HİÇBİR GARANTİ OLMAKSIZIN "OLDUĞU GİBİ" SUNULMAKTADIR. YAZARLAR VEYA TELİF HAKKI SAHİPLERİ HİÇBİR DURUMDA YAZILIMDAN VEYA YAZILIMIN KULLANIMINDAN YA DA YAZILIMLA İLGİLİ DİĞER İŞLEMLERDEN KAYNAKLANAN VEYA BUNLARLA BAĞLANTILI OLARAK ORTAYA ÇIKAN SÖZLEŞME, HAKSIZ FİİL VEYA BAŞKA TÜRLÜ BİR İDDİA, ZARAR VEYA DİĞER YÜKÜMLÜLÜKLERDEN SORUMLU TUTULAMAZ.


---